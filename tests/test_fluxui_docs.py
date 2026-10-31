import json
import sys
import tempfile
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
ORIGINAL = b"> [!PRO]\n# Date picker\nReviewed API\n"
CHANGED = b"> [!PRO]\n# Date picker\nChanged API\n"
NEW = b"> [!PRO]\n# Datetime picker\nNew component API\n"
MIXED = b"# Select\n## Custom select\n> [!PRO]\nListbox API\n"
THEMING = b"# Theming\nOriginal theme guidance\n"
THEMING_CHANGED = b"# Theming\nUpdated theme guidance\n"
SIDEBAR = b"# Sidebar\nCurrent layout guidance\n"
MULTI_KIND_INDEX = (
    "# Flux UI\n## Components\n"
    f"- [Date picker]({DATE_URL}) - Pick dates.\n"
    "## Guides\n"
    f"- [Theming]({THEMING_URL}) - Style an application.\n"
    "## Layouts\n"
    f"- [Sidebar]({SIDEBAR_URL}) - Navigation shell.\n"
).encode()


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
        (self.root / "references").mkdir(parents=True)
        (self.root / "references" / "date-picker.md").write_text("# Local reviewed note\n")
        (self.root / "references" / "theming.md").write_text("# Local theming note\n")
        manifest = {
            "components": {
                "date-picker": {
                    "name": "Date picker",
                    "summary": "Local summary",
                    "source_url": DATE_URL,
                    "source_sha256": sha256(ORIGINAL),
                    "pro": True,
                    "note": "references/date-picker.md",
                }
            },
            "guides": {
                "theming": {
                    "name": "Theming",
                    "summary": "Local theming summary",
                    "source_url": THEMING_URL,
                    "source_sha256": sha256(THEMING),
                    "pro": False,
                    "note": "references/theming.md",
                }
            },
            "layouts": {},
        }
        (self.root / "manifest.json").write_text(json.dumps(manifest))

    def docs(self, pages):
        fetch = FakeFetch(pages)
        return Docs(self.root, self.cache, fetch), fetch

    def test_router_includes_new_component_before_selection(self):
        docs, fetch = self.docs({INDEX_URL: INDEX, DATETIME_URL: NEW})
        catalog = docs.catalog()
        new = next(x for x in catalog["components"] if x["slug"] == "datetime-picker")
        self.assertEqual(new["bundle_status"], "new-to-skill")
        result = docs.show("datetime-picker")
        self.assertEqual(result["content_source"], "live")
        self.assertEqual(result["verification"], "new")
        self.assertTrue(result["pro"])
        self.assertIn("New component API", result["content"])
        self.assertEqual(fetch.calls, [INDEX_URL, INDEX_URL, DATETIME_URL])

    def test_matching_hash_uses_bundled_note(self):
        docs, _ = self.docs({INDEX_URL: INDEX, DATE_URL: ORIGINAL})
        result = docs.show("date-picker")
        self.assertEqual(result["content_source"], "bundled")
        self.assertEqual(result["verification"], "matched")
        self.assertEqual(result["content"], "# Local reviewed note\n")

    def test_changed_hash_uses_live_page_immediately(self):
        docs, _ = self.docs({INDEX_URL: INDEX, DATE_URL: CHANGED})
        result = docs.show("date-picker")
        self.assertEqual(result["content_source"], "live")
        self.assertEqual(result["verification"], "changed")
        self.assertIn("Changed API", result["content"])

    def test_offline_uses_cached_new_page_and_bundled_known_note(self):
        online, _ = self.docs({INDEX_URL: INDEX, DATETIME_URL: NEW})
        online.show("datetime-picker")
        offline, fetch = self.docs({})
        new = offline.show("datetime-picker", offline=True)
        known = offline.show("date-picker", offline=True)
        self.assertEqual(new["content_source"], "cache")
        self.assertEqual(new["verification"], "unverified")
        self.assertEqual(known["content_source"], "bundled")
        self.assertEqual(known["verification"], "unverified")
        self.assertEqual(fetch.calls, [])

    def test_new_component_without_cached_page_fails_offline(self):
        docs, _ = self.docs({INDEX_URL: INDEX})
        docs.catalog()
        with self.assertRaisesRegex(ValueError, "no cached or bundled copy"):
            docs.show("datetime-picker", offline=True)

    def test_audit_reports_new_and_changed_components(self):
        docs, _ = self.docs({INDEX_URL: INDEX, DATE_URL: CHANGED, DATETIME_URL: NEW})
        result = docs.audit()
        self.assertEqual(result["unchanged"], 0)
        self.assertEqual([(item["slug"], item["status"]) for item in result["changes"]], [
            ("date-picker", "changed"), ("datetime-picker", "new"), ("theming", "removed")
        ])

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
        layout = catalog["layouts"][0]
        self.assertEqual(layout["slug"], "sidebar")
        self.assertEqual(layout["bundle_status"], "new-to-skill")
        result = docs.show("sidebar")
        self.assertEqual(result["kind"], "layouts")
        self.assertEqual(result["content_source"], "live")
        self.assertEqual(result["verification"], "new")

    def test_changed_guide_uses_live_page_and_offline_uses_cache(self):
        docs, _ = self.docs({INDEX_URL: MULTI_KIND_INDEX, THEMING_URL: THEMING_CHANGED})
        live = docs.show("theming")
        self.assertEqual(live["kind"], "guides")
        self.assertEqual(live["content_source"], "live")
        self.assertEqual(live["verification"], "changed")
        offline, _ = self.docs({})
        cached = offline.show("theming", offline=True)
        self.assertEqual(cached["kind"], "guides")
        self.assertEqual(cached["content_source"], "cache")
        self.assertIn("Updated theme guidance", cached["content"])

    def test_audit_includes_guides_and_layouts(self):
        docs, _ = self.docs({
            INDEX_URL: MULTI_KIND_INDEX,
            DATE_URL: ORIGINAL,
            THEMING_URL: THEMING_CHANGED,
            SIDEBAR_URL: SIDEBAR,
        })
        report = docs.audit()
        self.assertEqual(report["unchanged"], 1)
        self.assertEqual([(item["slug"], item["status"]) for item in report["changes"]], [
            ("sidebar", "new"), ("theming", "changed")
        ])


class BundleTest(unittest.TestCase):
    def test_every_guide_and_layout_has_a_usable_note(self):
        manifest = json.loads((SKILL / "manifest.json").read_text())
        for kind, path, count in (("guides", "docs", 8), ("layouts", "layouts", 2)):
            bundled = manifest[kind]
            self.assertEqual(len(bundled), count)
            self.assertEqual(len(list((SKILL / "references" / kind).glob("*.md"))), count)
            for slug, entry in bundled.items():
                with self.subTest(kind=kind, slug=slug):
                    self.assertRegex(entry["source_sha256"], r"^[0-9a-f]{64}$")
                    self.assertEqual(entry["source_url"], f"https://fluxui.dev/{path}/{slug}.md")
                    note = (SKILL / entry["note"]).read_text()
                    self.assertIn(f"# {entry['name']}", note)
                    self.assertIn(entry["source_url"], note)

    def test_every_snapshot_component_has_a_usable_note(self):
        bundled = json.loads((SKILL / "manifest.json").read_text())["components"]
        self.assertEqual(len(bundled), 52)
        self.assertEqual(len(list((SKILL / "references" / "components").glob("*.md"))), len(bundled))
        for slug, entry in bundled.items():
            with self.subTest(slug=slug):
                self.assertRegex(entry["source_sha256"], r"^[0-9a-f]{64}$")
                self.assertEqual(entry["source_url"], f"https://fluxui.dev/components/{slug}.md")
                note = (SKILL / entry["note"]).read_text()
                self.assertIn("**Starter:**", note)
                self.assertIn("## How to customize", note)
                self.assertIn("## Capabilities", note)
                self.assertIn("## Component API", note)
                self.assertIn(entry["source_url"], note)
                self.assertIn("Flux Pro" if entry["pro"] else "Flux (free)", note)

        self.assertIn("Custom select", bundled["select"]["pro_sections"])

    def test_offline_references_expose_less_obvious_capabilities(self):
        examples = {
            "accordion": ("Findable content", "transition", "exclusive"),
            "select": ("Backend search", "Combobox", "Multiple select"),
            "chart": ("Pie chart", "Formatting", "flux:chart.axis"),
            "datetime-picker": ("Timezones", "DateTimeRange", "time-format"),
        }
        for slug, capabilities in examples.items():
            with self.subTest(slug=slug):
                note = (SKILL / "references" / "components" / f"{slug}.md").read_text()
                for capability in capabilities:
                    self.assertIn(capability, note)


if __name__ == "__main__":
    unittest.main()
