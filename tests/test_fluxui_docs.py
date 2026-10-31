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
INDEX = (
    "# Flux UI\n## Components\n"
    f"- [Date picker]({DATE_URL}) - Pick dates.\n"
    f"- [Datetime picker]({DATETIME_URL}) - Pick dates and times.\n"
).encode()
ORIGINAL = b"> [!PRO]\n# Date picker\nReviewed API\n"
CHANGED = b"> [!PRO]\n# Date picker\nChanged API\n"
NEW = b"> [!PRO]\n# Datetime picker\nNew component API\n"


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
            }
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


if __name__ == "__main__":
    unittest.main()
