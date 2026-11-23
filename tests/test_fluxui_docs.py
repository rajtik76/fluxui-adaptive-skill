import json
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))
from fluxui_docs import Docs, INDEX_URL, sha256  # noqa: E402


DATE_URL = "https://fluxui.dev/components/date-picker.md"
DATETIME_URL = "https://fluxui.dev/components/datetime-picker.md"
SELECT_URL = "https://fluxui.dev/components/select.md"
THEMING_URL = "https://fluxui.dev/docs/theming.md"
SIDEBAR_URL = "https://fluxui.dev/layouts/sidebar.md"
INDEX = (
    "# Flux UI\n## Components\n"
    f"- [Date picker]({DATE_URL}) - Pick dates.\n"
    f"- [Datetime picker]({DATETIME_URL}) - Pick dates and times.\n"
).encode()
MULTI_KIND_INDEX = (
    "# Flux UI\n## Components\n"
    f"- [Date picker]({DATE_URL}) - Pick dates.\n"
    "## Guides\n"
    f"- [Theming]({THEMING_URL}) - Style an application.\n"
    "## Layouts\n"
    f"- [Sidebar]({SIDEBAR_URL}) - Navigation shell.\n"
).encode()
ORIGINAL = b"> [!PRO]\n# Date picker\nReviewed API\n"
CHANGED = b"> [!PRO]\n# Date picker\nChanged API\n"
NEW = b"> [!PRO]\n# Datetime picker\nNew component API\n"
MIXED = b"# Select\n## Custom select\n> [!PRO]\nListbox API\n"
THEMING = b"# Theming\nOriginal theme guidance\n"
THEMING_CHANGED = b"# Theming\nUpdated theme guidance\n"
SIDEBAR = b"# Sidebar\nCurrent layout guidance\n"


class FakeFetch:
    def __init__(self, pages):
        self.pages = pages
        self.calls = []

    def __call__(self, url):
        self.calls.append(url)
        value = self.pages[url]
        if isinstance(value, Exception):
            raise value
        return value


class DocsTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "skill"
        self.cache = Path(self.temporary.name) / "cache"
        files = {
            "references/source/components/date-picker.md": ORIGINAL,
            "references/source/docs/theming.md": THEMING,
            "references/components/date-picker.md": b"# Date picker note\n",
            "references/guides/theming.md": b"# Theming note\n",
        }
        for path, data in files.items():
            (self.root / path).parent.mkdir(parents=True, exist_ok=True)
            (self.root / path).write_bytes(data)
        self.manifest = {
            "snapshot": "2026-11-01T00:00:00+00:00",
            "components": {
                "date-picker": {
                    "name": "Date picker",
                    "summary": "Local summary",
                    "source_url": DATE_URL,
                    "source_sha256": sha256(ORIGINAL),
                    "source": "references/source/components/date-picker.md",
                    "pro": True,
                    "note": "references/components/date-picker.md",
                }
            },
            "guides": {
                "theming": {
                    "name": "Theming",
                    "summary": "Local theming summary",
                    "source_url": THEMING_URL,
                    "source_sha256": sha256(THEMING),
                    "source": "references/source/docs/theming.md",
                    "pro": False,
                    "note": "references/guides/theming.md",
                }
            },
            "layouts": {},
        }
        (self.root / "manifest.json").write_text(json.dumps(self.manifest))

    def docs(self, pages):
        fetch = FakeFetch(pages)
        return Docs(self.root, self.cache, fetch), fetch

    def test_new_page_in_index_is_read_live(self):
        docs, fetch = self.docs({INDEX_URL: INDEX, DATETIME_URL: NEW})
        catalog = docs.catalog()
        new = next(x for x in catalog["components"] if x["slug"] == "datetime-picker")
        self.assertEqual(new["bundle_status"], "new-to-skill")
        result = docs.show("datetime-picker")
        self.assertEqual((result["content_source"], result["verification"]), ("live", "new"))
        self.assertTrue(result["pro"])
        self.assertIn("New component API", result["content"])
        self.assertEqual(fetch.calls, [INDEX_URL, INDEX_URL, DATETIME_URL])

    def test_bundled_page_skips_index_and_matches_by_hash(self):
        docs, fetch = self.docs({DATE_URL: ORIGINAL})
        result = docs.show("date-picker")
        self.assertEqual((result["content_source"], result["verification"]), ("bundled", "matched"))
        self.assertEqual(result["content"], ORIGINAL.decode())
        self.assertEqual(fetch.calls, [DATE_URL])
        self.assertFalse((self.cache / "components" / "date-picker.md").exists())

    def test_changed_page_is_read_live_and_cached(self):
        docs, _ = self.docs({DATE_URL: CHANGED})
        result = docs.show("date-picker")
        self.assertEqual((result["content_source"], result["verification"]), ("live", "changed"))
        self.assertIn("Changed API", result["content"])
        self.assertEqual((self.cache / "components" / "date-picker.md").read_bytes(), CHANGED)

    def test_offline_prefers_cache_newer_than_snapshot(self):
        online, _ = self.docs({THEMING_URL: THEMING_CHANGED})
        online.show("theming")
        offline, fetch = self.docs({})
        cached = offline.show("theming", offline=True)
        self.assertEqual((cached["content_source"], cached["verification"]), ("cache", "unverified"))
        self.assertIn("Updated theme guidance", cached["content"])
        self.assertEqual(fetch.calls, [])

    def test_offline_ignores_cache_older_than_snapshot(self):
        stale = self.cache / "guides" / "theming.md"
        stale.parent.mkdir(parents=True)
        stale.write_bytes(b"# Theming\nStale\n")
        old = time.mktime((2026, 1, 1, 0, 0, 0, 0, 0, -1))
        os.utime(stale, (old, old))
        docs, _ = self.docs({})
        result = docs.show("theming", offline=True)
        self.assertEqual(result["content_source"], "bundled")
        self.assertIn("Original theme guidance", result["content"])

    def test_failed_fetch_falls_back_to_bundle(self):
        docs, _ = self.docs({DATE_URL: OSError("offline")})
        result = docs.show("date-picker")
        self.assertEqual((result["content_source"], result["verification"]), ("bundled", "unverified"))
        self.assertEqual(result["fetch_error"], "offline")

    def test_new_page_without_cache_fails_offline(self):
        docs, _ = self.docs({INDEX_URL: INDEX})
        docs.catalog()
        with self.assertRaisesRegex(ValueError, "no cached or bundled copy"):
            docs.show("datetime-picker", offline=True)

    def test_brief_returns_note_without_network(self):
        docs, fetch = self.docs({})
        result = docs.brief("date-picker")
        self.assertEqual(result["content"], "# Date picker note\n")
        self.assertEqual(result["source"], "references/source/components/date-picker.md")
        self.assertEqual(fetch.calls, [])

    def test_free_component_can_contain_pro_only_sections(self):
        index = f"# Flux UI\n## Components\n- [Select]({SELECT_URL}) - Pick one.\n".encode()
        docs, _ = self.docs({INDEX_URL: index, SELECT_URL: MIXED})
        result = docs.show("select")
        self.assertFalse(result["pro"])
        self.assertEqual(result["pro_sections"], ["Custom select"])

    def test_router_lists_guides_and_new_layouts(self):
        docs, _ = self.docs({INDEX_URL: MULTI_KIND_INDEX, SIDEBAR_URL: SIDEBAR})
        catalog = docs.catalog()
        self.assertEqual([entry["slug"] for entry in catalog["guides"]], ["theming"])
        self.assertEqual(catalog["layouts"][0]["bundle_status"], "new-to-skill")
        result = docs.show("sidebar")
        self.assertEqual((result["kind"], result["content_source"]), ("layouts", "live"))

    def test_audit_reports_new_changed_missing_and_removed(self):
        (self.root / "references/source/docs/theming.md").unlink()
        docs, _ = self.docs({
            INDEX_URL: MULTI_KIND_INDEX,
            DATE_URL: CHANGED,
            THEMING_URL: THEMING,
            SIDEBAR_URL: SIDEBAR,
        })
        report = docs.audit()
        self.assertEqual([(item["slug"], item["status"]) for item in report["changes"]], [
            ("date-picker", "changed"), ("sidebar", "new"), ("theming", "missing")
        ])
        docs, _ = self.docs({INDEX_URL: INDEX, DATE_URL: ORIGINAL, DATETIME_URL: NEW})
        self.assertIn(("theming", "removed"), [(i["slug"], i["status"]) for i in docs.audit()["changes"]])

    def test_sync_updates_bundle_and_manifest(self):
        docs, _ = self.docs({INDEX_URL: INDEX, DATE_URL: CHANGED, DATETIME_URL: NEW})
        report = docs.sync()
        statuses = {item["slug"]: item["status"] for item in report["changes"]}
        self.assertEqual(statuses, {"date-picker": "changed", "datetime-picker": "new", "theming": "removed"})
        self.assertTrue(next(i for i in report["changes"] if i["slug"] == "date-picker")["note_review"])
        manifest = json.loads((self.root / "manifest.json").read_text())
        self.assertNotEqual(manifest["snapshot"], self.manifest["snapshot"])
        self.assertEqual(manifest["guides"], {})
        self.assertFalse((self.root / "references/source/docs/theming.md").exists())
        self.assertFalse((self.root / "references/guides/theming.md").exists())
        changed = manifest["components"]["date-picker"]
        self.assertEqual(changed["source_sha256"], sha256(CHANGED))
        self.assertEqual(changed["summary"], "Local summary")
        self.assertEqual(changed["note"], "references/components/date-picker.md")
        self.assertEqual((self.root / changed["source"]).read_bytes(), CHANGED)
        new = manifest["components"]["datetime-picker"]
        self.assertEqual(new["source"], "references/source/components/datetime-picker.md")
        self.assertEqual(new["summary"], "Pick dates and times.")
        self.assertTrue(new["pro"])
        self.assertNotIn("note", new)
        self.assertEqual((self.root / new["source"]).read_bytes(), NEW)

    def test_sync_without_changes_leaves_manifest_untouched(self):
        index = f"# Flux UI\n## Components\n- [Date picker]({DATE_URL}) - Pick dates.\n## Guides\n- [Theming]({THEMING_URL}) - Style.\n".encode()
        before = (self.root / "manifest.json").read_bytes()
        docs, _ = self.docs({INDEX_URL: index, DATE_URL: ORIGINAL, THEMING_URL: THEMING})
        self.assertEqual(docs.sync()["changes"], [])
        self.assertEqual((self.root / "manifest.json").read_bytes(), before)


class BundleTest(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((SKILL / "manifest.json").read_text())

    def test_every_page_is_bundled_unmodified(self):
        prefixes = {"components": "components", "guides": "docs", "layouts": "layouts"}
        self.assertIsNotNone(self.manifest["snapshot"])
        sources = set()
        for kind, prefix in prefixes.items():
            for slug, entry in self.manifest[kind].items():
                with self.subTest(kind=kind, slug=slug):
                    self.assertEqual(entry["source_url"], f"https://fluxui.dev/{prefix}/{slug}.md")
                    self.assertEqual(entry["source"], f"references/source/{prefix}/{slug}.md")
                    data = (SKILL / entry["source"]).read_bytes()
                    self.assertEqual(sha256(data), entry["source_sha256"])
                    self.assertEqual(entry["pro"], data.startswith(b"> [!PRO]"))
                    sources.add(entry["source"])
        on_disk = {str(p.relative_to(SKILL)) for p in (SKILL / "references" / "source").rglob("*.md")}
        self.assertEqual(on_disk, sources)
        self.assertIn("Custom select", self.manifest["components"]["select"]["pro_sections"])

    def test_notes_route_to_full_pages_without_api_lists(self):
        for kind in ("components", "guides", "layouts"):
            for slug, entry in self.manifest[kind].items():
                if "note" not in entry:
                    continue
                with self.subTest(kind=kind, slug=slug):
                    note = (SKILL / entry["note"]).read_text()
                    self.assertIn(f"# {entry['name']}", note)
                    self.assertIn(f"`{entry['source']}`", note)
                    self.assertIn(entry["source_url"], note)
                    if kind == "components":
                        self.assertIn("## Capabilities", note)
                        self.assertNotIn("## Component API", note)
                        self.assertIn("Flux Pro" if entry["pro"] else "Flux (free)", note)

    def test_license_excludes_bundled_documentation(self):
        self.assertIn("references/source/", (SKILL / "LICENSE.md").read_text())


if __name__ == "__main__":
    unittest.main()
