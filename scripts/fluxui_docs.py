#!/usr/bin/env python3
"""Discover Flux v2 documentation and select reviewed, live, or cached guidance."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
INDEX_URL = "https://fluxui.dev/llms.txt"
RESOURCE_LINE = re.compile(
    r"^- \[([^]]+)\]\((https://fluxui\.dev/(components|docs|layouts)/([a-z0-9-]+)\.md)\)(?:\s+-\s+(.*))?$"
)
RESOURCE_KIND = {"components": "components", "docs": "guides", "layouts": "layouts"}
Fetch = Callable[[str], bytes]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_official(url: str) -> bytes:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != "fluxui.dev":
        raise ValueError(f"Untrusted documentation URL: {url}")
    request = urllib.request.Request(
        url, headers={"User-Agent": "fluxui-adaptive-skill/1.0"}
    )
    with urllib.request.urlopen(request, timeout=12) as response:
        final = urllib.parse.urlsplit(response.url)
        if final.scheme != "https" or final.hostname != "fluxui.dev":
            raise ValueError(f"Documentation redirected outside Flux UI: {response.url}")
        data = response.read(2_000_001)
    if len(data) > 2_000_000:
        raise ValueError(f"Documentation page is too large: {url}")
    return data


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as temporary:
        temporary.write(data)
        temporary_path = Path(temporary.name)
    os.replace(temporary_path, path)


def parse_index(data: bytes) -> dict[str, dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    for line in data.decode("utf-8").splitlines():
        match = RESOURCE_LINE.fullmatch(line.strip())
        if match:
            name, url, path, slug, description = match.groups()
            if slug in entries:
                raise ValueError(f"Duplicate documentation slug: {slug}")
            entries[slug] = {
                "slug": slug,
                "name": name,
                "url": url,
                "description": description or "",
                "kind": RESOURCE_KIND[path],
            }
    if not entries:
        raise ValueError("Flux UI index contains no documentation links")
    return entries


def pro_sections(markdown: str) -> list[str]:
    """Find sections marked Pro inside an otherwise free component page."""
    current = None
    sections = []
    for line in markdown.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
        elif line == "> [!PRO]" and current and current not in sections:
            sections.append(current)
    return sections


class Docs:
    def __init__(
        self,
        root: Path = ROOT,
        cache_dir: Path | None = None,
        fetch: Fetch = fetch_official,
    ) -> None:
        self.root = root
        self.manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        self.bundled = {
            slug: {**entry, "kind": kind}
            for kind in ("components", "guides", "layouts")
            for slug, entry in self.manifest.get(kind, {}).items()
        }
        self.cache_dir = cache_dir or Path(
            os.environ.get("FLUXUI_SKILL_CACHE", Path.home() / ".cache" / "fluxui-development")
        )
        self.fetch = fetch

    def _index(self, offline: bool) -> tuple[dict[str, dict[str, str]], str, str | None]:
        error = None
        if not offline:
            try:
                data = self.fetch(INDEX_URL)
                entries = parse_index(data)
                atomic_write(self.cache_dir / "llms.txt", data)
                return entries, "live", None
            except (OSError, ValueError, UnicodeError) as exc:
                error = str(exc)
        cached = self.cache_dir / "llms.txt"
        if cached.exists():
            try:
                return parse_index(cached.read_bytes()), "cache", error
            except (OSError, ValueError, UnicodeError) as exc:
                error = str(exc)
        return {}, "bundled", error

    def catalog(self, offline: bool = False) -> dict:
        indexed, source, error = self._index(offline)
        entries = {"components": [], "guides": [], "layouts": []}
        for slug in sorted(indexed.keys() | self.bundled.keys()):
            live = indexed.get(slug)
            bundled = self.bundled.get(slug)
            kind = live["kind"] if live else bundled["kind"]
            entries[kind].append(
                {
                    "slug": slug,
                    "name": live["name"] if live else bundled["name"],
                    "description": live["description"] if live else bundled["summary"],
                    "url": live["url"] if live else bundled["source_url"],
                    "bundle_status": "bundled" if bundled else "new-to-skill",
                    "index_status": "listed" if live else "bundled-only",
                    "pro": bundled["pro"] if bundled else None,
                    "pro_sections": bundled.get("pro_sections", []) if bundled else [],
                    "kind": kind,
                }
            )
        return {"index_source": source, "index_error": error, **entries}

    def audit(self) -> dict:
        """Compare every live documentation page with the bundled snapshot."""
        indexed = parse_index(self.fetch(INDEX_URL))
        changes = []
        unchanged = 0
        for slug, entry in sorted(indexed.items()):
            data = self.fetch(entry["url"])
            data.decode("utf-8")
            digest = sha256(data)
            bundled = self.bundled.get(slug)
            if bundled is None:
                status = "new"
            elif digest != bundled["source_sha256"] or entry["url"] != bundled["source_url"]:
                status = "changed"
            else:
                unchanged += 1
                continue
            changes.append({"slug": slug, "status": status, "url": entry["url"], "source_sha256": digest})
        for slug in sorted(self.bundled.keys() - indexed.keys()):
            changes.append({"slug": slug, "status": "removed", "url": self.bundled[slug]["source_url"]})
        return {"checked_at": datetime.now(timezone.utc).isoformat(), "unchanged": unchanged, "changes": changes}

    def show(self, slug: str, offline: bool = False, force_live: bool = False) -> dict:
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            raise ValueError("Documentation slug must contain only lowercase letters, digits, and hyphens")
        catalog = self.catalog(offline=offline)
        entry = next((item for kind in ("components", "guides", "layouts") for item in catalog[kind] if item["slug"] == slug), None)
        if entry is None:
            raise ValueError(f"Unknown documentation page: {slug}")
        bundled = self.bundled.get(slug)
        cache_path = self.cache_dir / entry["kind"] / f"{slug}.md"
        remote = None
        fetch_error = None
        if not offline:
            try:
                remote = self.fetch(entry["url"])
                remote.decode("utf-8")
                atomic_write(cache_path, remote)
            except (OSError, ValueError, UnicodeError) as exc:
                fetch_error = str(exc)
        if remote is not None:
            digest = sha256(remote)
            remote_doc = remote.decode("utf-8")
            match = bundled is not None and digest == bundled["source_sha256"]
            if match and not force_live:
                content = (self.root / bundled["note"]).read_text(encoding="utf-8")
                content_source = "bundled"
            else:
                content = remote_doc
                content_source = "live"
            return self._result(
                slug, entry, content, content_source,
                "matched" if match else "changed" if bundled else "new",
                digest, remote_doc.startswith("> [!PRO]"),
                catalog["index_source"], None, pro_sections(remote_doc),
            )

        if cache_path.exists():
            cached = cache_path.read_bytes()
            content = cached.decode("utf-8")
            digest = sha256(cached)
            match = bundled is not None and digest == bundled["source_sha256"]
            if match and not force_live:
                content = (self.root / bundled["note"]).read_text(encoding="utf-8")
                content_source = "bundled"
                pro = bundled["pro"]
            else:
                content_source = "cache"
                pro = content.startswith("> [!PRO]")
            return self._result(
                slug, entry, content, content_source, "unverified", digest,
                pro, catalog["index_source"], fetch_error, pro_sections(cached.decode("utf-8")),
            )

        if bundled:
            content = (self.root / bundled["note"]).read_text(encoding="utf-8")
            return self._result(
                slug, entry, content, "bundled", "unverified",
                bundled["source_sha256"], bundled["pro"],
                catalog["index_source"], fetch_error, bundled.get("pro_sections", []),
            )
        raise ValueError(f"No documentation for {slug}: live page unavailable and no cached or bundled copy")

    @staticmethod
    def _result(
        slug: str, entry: dict, content: str, content_source: str,
        verification: str, digest: str, pro: bool, index_source: str,
        fetch_error: str | None, pro_only_sections: list[str],
    ) -> dict:
        return {
            "slug": slug,
            "kind": entry["kind"],
            "url": entry["url"],
            "content_source": content_source,
            "verification": verification,
            "index_source": index_source,
            "source_sha256": digest,
            "pro": pro,
            "pro_sections": pro_only_sections,
            "fetch_error": fetch_error,
            "checked_at": datetime.now(timezone.utc).isoformat() if verification != "unverified" else None,
            "content": content,
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("catalog", "show"):
        command = sub.add_parser(name)
        command.add_argument("--offline", action="store_true", help="Use cached or bundled data only")
        command.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    audit = sub.add_parser("audit", help="Compare all live pages with the bundled manifest")
    audit.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    sub.choices["show"].add_argument("slug")
    sub.choices["show"].add_argument("--live", action="store_true", help="Show the full page even when the bundled note matches")
    args = parser.parse_args()
    docs = Docs()
    try:
        if args.command == "catalog":
            result = docs.catalog(offline=args.offline)
        elif args.command == "show":
            result = docs.show(args.slug, offline=args.offline, force_live=args.live)
        else:
            result = docs.audit()
    except (OSError, ValueError, UnicodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.command == "catalog":
        print(f"Index: {result['index_source']}")
        if result["index_error"]:
            print(f"Index fetch failed: {result['index_error']}")
        for kind in ("guides", "layouts", "components"):
            print(f"{kind.title()}:")
            for item in result[kind]:
                print(f"- {item['name']} ({item['slug']}) [{item['bundle_status']}]: {item['description']}")
    elif args.command == "audit":
        print(f"Unchanged: {result['unchanged']}; changes: {len(result['changes'])}")
        for item in result["changes"]:
            print(f"- {item['slug']}: {item['status']} ({item['url']})")
    else:
        tier = "Pro" if result["pro"] else "Free with Pro variants" if result["pro_sections"] else "Free"
        category = result["kind"] if result["kind"] != "components" else f"component, {tier}"
        print(
            f"{result['slug']}: {result['content_source']}, {result['verification']}, "
            f"{category}, index={result['index_source']}"
        )
        if result["fetch_error"]:
            print(f"Live fetch failed: {result['fetch_error']}")
        print(result["content"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
