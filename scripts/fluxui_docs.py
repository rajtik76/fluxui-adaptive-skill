#!/usr/bin/env python3
"""Discover Flux v2 components and select reviewed, live, or cached guidance."""

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
COMPONENT_LINE = re.compile(
    r"^- \[([^]]+)\]\((https://fluxui\.dev/components/([a-z0-9-]+)\.md)\)(?:\s+-\s+(.*))?$"
)
Fetch = Callable[[str], bytes]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_official(url: str) -> bytes:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != "fluxui.dev":
        raise ValueError(f"Untrusted documentation URL: {url}")
    request = urllib.request.Request(
        url, headers={"User-Agent": "fluxui-development-prototype/0.1"}
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
        match = COMPONENT_LINE.fullmatch(line.strip())
        if match:
            name, url, slug, description = match.groups()
            entries[slug] = {
                "slug": slug,
                "name": name,
                "url": url,
                "description": description or "",
            }
    if not entries:
        raise ValueError("Flux UI index contains no component links")
    return entries


class Docs:
    def __init__(
        self,
        root: Path = ROOT,
        cache_dir: Path | None = None,
        fetch: Fetch = fetch_official,
    ) -> None:
        self.root = root
        self.manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        self.bundled = self.manifest["components"]
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
        entries = []
        for slug in sorted(indexed.keys() | self.bundled.keys()):
            live = indexed.get(slug)
            bundled = self.bundled.get(slug)
            entries.append(
                {
                    "slug": slug,
                    "name": live["name"] if live else bundled["name"],
                    "description": live["description"] if live else bundled["summary"],
                    "url": live["url"] if live else bundled["source_url"],
                    "bundle_status": "bundled" if bundled else "new-to-skill",
                    "index_status": "listed" if live else "bundled-only",
                }
            )
        return {"index_source": source, "index_error": error, "components": entries}

    def show(self, slug: str, offline: bool = False, force_live: bool = False) -> dict:
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            raise ValueError("Component slug must contain only lowercase letters, digits, and hyphens")
        catalog = self.catalog(offline=offline)
        entry = next((item for item in catalog["components"] if item["slug"] == slug), None)
        if entry is None:
            raise ValueError(f"Unknown component: {slug}")
        bundled = self.bundled.get(slug)
        cache_path = self.cache_dir / "components" / f"{slug}.md"
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
            match = bundled is not None and digest == bundled["source_sha256"]
            if match and not force_live:
                content = (self.root / bundled["note"]).read_text(encoding="utf-8")
                content_source = "bundled"
            else:
                content = remote.decode("utf-8")
                content_source = "live"
            return self._result(
                slug, entry, content, content_source,
                "matched" if match else "changed" if bundled else "new",
                digest, content.startswith("> [!PRO]") if content_source == "live" else bundled["pro"],
                catalog["index_source"], None,
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
                pro, catalog["index_source"], fetch_error,
            )

        if bundled:
            content = (self.root / bundled["note"]).read_text(encoding="utf-8")
            return self._result(
                slug, entry, content, "bundled", "unverified",
                bundled["source_sha256"], bundled["pro"],
                catalog["index_source"], fetch_error,
            )
        raise ValueError(
            f"No documentation for {slug}: live page unavailable and no cached or bundled copy"
        )

    @staticmethod
    def _result(
        slug: str, entry: dict, content: str, content_source: str,
        verification: str, digest: str, pro: bool, index_source: str,
        fetch_error: str | None,
    ) -> dict:
        return {
            "slug": slug,
            "url": entry["url"],
            "content_source": content_source,
            "verification": verification,
            "index_source": index_source,
            "source_sha256": digest,
            "pro": pro,
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
    sub.choices["show"].add_argument("slug")
    sub.choices["show"].add_argument("--live", action="store_true", help="Show the full page even when the bundled note matches")
    args = parser.parse_args()
    docs = Docs()
    try:
        result = docs.catalog(offline=args.offline) if args.command == "catalog" else docs.show(
            args.slug, offline=args.offline, force_live=args.live
        )
    except (OSError, ValueError, UnicodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.command == "catalog":
        print(f"Index: {result['index_source']}")
        if result["index_error"]:
            print(f"Index fetch failed: {result['index_error']}")
        for item in result["components"]:
            print(f"- {item['name']} ({item['slug']}) [{item['bundle_status']}]: {item['description']}")
    else:
        print(
            f"{result['slug']}: {result['content_source']}, {result['verification']}, "
            f"{'Pro' if result['pro'] else 'Free'}, index={result['index_source']}"
        )
        if result["fetch_error"]:
            print(f"Live fetch failed: {result['fetch_error']}")
        print(result["content"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
