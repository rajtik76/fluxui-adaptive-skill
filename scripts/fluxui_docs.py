#!/usr/bin/env python3
"""Discover Flux v2 documentation and select bundled, live, or cached pages."""

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
KINDS = ("components", "guides", "layouts")
Fetch = Callable[[str], bytes]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def fetch_official(url: str) -> bytes:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != "fluxui.dev":
        raise ValueError(f"Untrusted documentation URL: {url}")
    request = urllib.request.Request(
        url, headers={"User-Agent": "fluxui-adaptive-skill/2.0"}
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


def is_pro(markdown: str) -> bool:
    return markdown.lstrip().startswith("> [!PRO]")


def pro_sections(markdown: str) -> list[str]:
    """Find sections marked Pro inside an otherwise free component page."""
    current = None
    sections = []
    for line in markdown.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
        elif line.strip() == "> [!PRO]" and current and current not in sections:
            sections.append(current)
    return sections


def source_path(url: str) -> str:
    """Map an official page URL to its bundled copy, mirroring the site path."""
    return "references/source/" + urllib.parse.urlsplit(url).path.lstrip("/")


class Docs:
    def __init__(
        self,
        root: Path = ROOT,
        cache_dir: Path | None = None,
        fetch: Fetch = fetch_official,
    ) -> None:
        self.root = root
        self.manifest_path = root / "manifest.json"
        self.manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        self.cache_dir = cache_dir or Path(
            os.environ.get("FLUXUI_SKILL_CACHE", Path.home() / ".cache" / "fluxui-adaptive")
        )
        self.fetch = fetch

    @property
    def bundled(self) -> dict[str, dict]:
        return {
            slug: {**entry, "kind": kind}
            for kind in KINDS
            for slug, entry in self.manifest.get(kind, {}).items()
        }

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
        bundled = self.bundled
        entries: dict[str, list] = {kind: [] for kind in KINDS}
        for slug in sorted(indexed.keys() | bundled.keys()):
            live = indexed.get(slug)
            local = bundled.get(slug)
            kind = live["kind"] if live else local["kind"]
            entries[kind].append(
                {
                    "slug": slug,
                    "name": live["name"] if live else local["name"],
                    "description": live["description"] if live else local["summary"],
                    "url": live["url"] if live else local["source_url"],
                    "bundle_status": "bundled" if local else "new-to-skill",
                    "index_status": "listed" if live else "bundled-only",
                    "pro": local["pro"] if local else None,
                    "pro_sections": local.get("pro_sections", []) if local else [],
                    "kind": kind,
                }
            )
        return {
            "index_source": source,
            "index_error": error,
            "snapshot": self.manifest.get("snapshot"),
            **entries,
        }

    def _compare(self) -> tuple[dict, dict[str, bytes], list[dict], int]:
        indexed = parse_index(self.fetch(INDEX_URL))
        bundled = self.bundled
        pages: dict[str, bytes] = {}
        changes = []
        unchanged = 0
        for slug, entry in sorted(indexed.items()):
            data = self.fetch(entry["url"])
            data.decode("utf-8")
            pages[slug] = data
            digest = sha256(data)
            local = bundled.get(slug)
            if local is None:
                status = "new"
            elif not local.get("source") or not (self.root / local["source"]).is_file():
                status = "missing"
            elif (
                digest != local["source_sha256"]
                or entry["url"] != local["source_url"]
                or entry["kind"] != local["kind"]
            ):
                status = "changed"
            else:
                unchanged += 1
                continue
            changes.append({"slug": slug, "status": status, "url": entry["url"], "source_sha256": digest})
        for slug in sorted(bundled.keys() - indexed.keys()):
            changes.append({"slug": slug, "status": "removed", "url": bundled[slug]["source_url"]})
        return indexed, pages, changes, unchanged

    def audit(self) -> dict:
        """Compare every live documentation page with the bundled snapshot."""
        _, _, changes, unchanged = self._compare()
        return {"checked_at": now(), "unchanged": unchanged, "changes": changes}

    def sync(self) -> dict:
        """Bring bundled pages and the manifest up to date with the live site."""
        indexed, pages, changes, unchanged = self._compare()
        if not changes:
            return {"synced_at": self.manifest.get("snapshot"), "unchanged": unchanged, "changes": []}
        bundled = self.bundled
        for change in changes:
            slug = change["slug"]
            local = bundled.get(slug)
            if local is not None:
                del self.manifest[local["kind"]][slug]
            if change["status"] == "removed":
                for key in ("source", "note"):
                    if local.get(key):
                        (self.root / local[key]).unlink(missing_ok=True)
                continue
            live = indexed[slug]
            data = pages[slug]
            text = data.decode("utf-8")
            path = source_path(live["url"])
            if local is not None and local.get("source") and local["source"] != path:
                (self.root / local["source"]).unlink(missing_ok=True)
            atomic_write(self.root / path, data)
            entry = {
                "name": local["name"] if local else live["name"],
                "summary": local["summary"] if local else live["description"],
                "source_url": live["url"],
                "source_sha256": sha256(data),
                "source": path,
                "pro": is_pro(text),
            }
            if live["kind"] == "components":
                sections = pro_sections(text)
                if sections and not entry["pro"]:
                    entry["pro_sections"] = sections
            if local and local.get("note"):
                entry["note"] = local["note"]
                change["note_review"] = True
            self.manifest.setdefault(live["kind"], {})[slug] = entry
        for kind in KINDS:
            self.manifest[kind] = dict(sorted(self.manifest.get(kind, {}).items()))
        self.manifest["snapshot"] = now()
        atomic_write(
            self.manifest_path,
            (json.dumps(self.manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        )
        return {"synced_at": self.manifest["snapshot"], "unchanged": unchanged, "changes": changes}

    def _snapshot_time(self) -> float:
        snapshot = self.manifest.get("snapshot")
        return datetime.fromisoformat(snapshot).timestamp() if snapshot else 0.0

    def brief(self, slug: str) -> dict:
        """Return the short routing note for a bundled page, without network access."""
        local = self.bundled.get(slug)
        if local is None:
            raise ValueError(f"No bundled page for {slug}; use show to read the live page")
        if not local.get("note"):
            raise ValueError(f"{slug} has no short note; use show for the full page")
        return {
            "slug": slug,
            "kind": local["kind"],
            "url": local["source_url"],
            "source": local["source"],
            "pro": local["pro"],
            "pro_sections": local.get("pro_sections", []),
            "content": (self.root / local["note"]).read_text(encoding="utf-8"),
        }

    def show(self, slug: str, offline: bool = False) -> dict:
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            raise ValueError("Documentation slug must contain only lowercase letters, digits, and hyphens")
        local = self.bundled.get(slug)
        index_source = None
        if local is not None:
            kind, url = local["kind"], local["source_url"]
        else:
            catalog = self.catalog(offline=offline)
            index_source = catalog["index_source"]
            entry = next((item for k in KINDS for item in catalog[k] if item["slug"] == slug), None)
            if entry is None:
                raise ValueError(f"Unknown documentation page: {slug}")
            kind, url = entry["kind"], entry["url"]
        cache_path = self.cache_dir / kind / f"{slug}.md"

        fetch_error = None
        if not offline:
            try:
                remote = self.fetch(url)
                text = remote.decode("utf-8")
                digest = sha256(remote)
                match = local is not None and digest == local["source_sha256"]
                if not match:
                    atomic_write(cache_path, remote)
                return self._result(
                    slug, kind, url, text, "bundled" if match else "live",
                    "matched" if match else "changed" if local else "new",
                    digest, index_source, None,
                )
            except (OSError, ValueError, UnicodeError) as exc:
                fetch_error = str(exc)

        # Offline: a cached page fetched after the snapshot is newer than the bundle.
        if cache_path.exists() and (local is None or cache_path.stat().st_mtime > self._snapshot_time()):
            cached = cache_path.read_bytes()
            return self._result(
                slug, kind, url, cached.decode("utf-8"), "cache", "unverified",
                sha256(cached), index_source, fetch_error,
            )
        if local is not None:
            text = (self.root / local["source"]).read_text(encoding="utf-8")
            return self._result(
                slug, kind, url, text, "bundled", "unverified",
                local["source_sha256"], index_source, fetch_error,
            )
        raise ValueError(f"No documentation for {slug}: live page unavailable and no cached or bundled copy")

    def _result(
        self, slug: str, kind: str, url: str, content: str, content_source: str,
        verification: str, digest: str, index_source: str | None, fetch_error: str | None,
    ) -> dict:
        return {
            "slug": slug,
            "kind": kind,
            "url": url,
            "content_source": content_source,
            "verification": verification,
            "index_source": index_source,
            "snapshot": self.manifest.get("snapshot"),
            "source_sha256": digest,
            "pro": is_pro(content),
            "pro_sections": pro_sections(content) if kind == "components" else [],
            "fetch_error": fetch_error,
            "checked_at": now() if verification != "unverified" else None,
            "content": content,
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    commands = {
        "catalog": "List bundled and live pages",
        "show": "Print the full official page, live when reachable",
        "brief": "Print the short bundled note for a page",
        "audit": "Compare all live pages with the bundle",
        "sync": "Update bundled pages and the manifest from the live site",
    }
    for name, help_text in commands.items():
        command = sub.add_parser(name, help=help_text)
        command.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
        if name in ("show", "brief"):
            command.add_argument("slug")
        if name in ("catalog", "show"):
            command.add_argument("--offline", action="store_true", help="Use cached or bundled data only")
    args = parser.parse_args()
    docs = Docs()
    try:
        if args.command == "catalog":
            result = docs.catalog(offline=args.offline)
        elif args.command == "show":
            result = docs.show(args.slug, offline=args.offline)
        elif args.command == "brief":
            result = docs.brief(args.slug)
        elif args.command == "audit":
            result = docs.audit()
        else:
            result = docs.sync()
    except (OSError, ValueError, UnicodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.command == "catalog":
        print(f"Index: {result['index_source']}; bundle snapshot: {result['snapshot']}")
        if result["index_error"]:
            print(f"Index fetch failed: {result['index_error']}")
        for kind in ("guides", "layouts", "components"):
            print(f"{kind.title()}:")
            for item in result[kind]:
                print(f"- {item['name']} ({item['slug']}) [{item['bundle_status']}]: {item['description']}")
    elif args.command in ("audit", "sync"):
        print(f"Unchanged: {result['unchanged']}; changes: {len(result['changes'])}")
        for item in result["changes"]:
            print(f"- {item['slug']}: {item['status']} ({item['url']})")
    elif args.command == "brief":
        print(f"{result['slug']}: bundled note; full page: {result['source']}")
        print(result["content"])
    else:
        tier = "Pro" if result["pro"] else "Free with Pro sections" if result["pro_sections"] else "Free"
        category = result["kind"] if result["kind"] != "components" else f"component, {tier}"
        print(
            f"{result['slug']}: {result['content_source']}, {result['verification']}, "
            f"{category}, snapshot={result['snapshot']}"
        )
        if result["fetch_error"]:
            print(f"Live fetch failed: {result['fetch_error']}")
        print(result["content"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
