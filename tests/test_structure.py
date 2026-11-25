import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = {
    "google-ads-audit", "meta-ads-audit", "seo-content-audit",
    "paid-media-budget-allocation", "competitor-analysis", "landing-page-audit",
    "marketing-experiment-planner", "campaign-performance-report",
}

class PackageTests(unittest.TestCase):
    def test_skill_inventory(self):
        self.assertEqual({p.parent.name for p in ROOT.glob("skills/*/SKILL.md")}, NAMES)

    def test_front_matter(self):
        for name in NAMES:
            with self.subTest(name=name):
                raw = (ROOT / "skills" / name / "SKILL.md").read_text()
                header = re.match(r"^---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n", raw)
                self.assertIsNotNone(header)
                self.assertEqual(header.group(1), name)
                self.assertLessEqual(len(header.group(2)), 1024)

    def test_required_sections(self):
        for name in NAMES:
            with self.subTest(name=name):
                raw = (ROOT / "skills" / name / "SKILL.md").read_text()
                for heading in ("Required context", "Method", "Deliverable", "Safeguards", "Validation checklist"):
                    self.assertIn("## " + heading, raw)
                self.assertIn("without separate explicit authorization", raw)

    def test_fixtures(self):
        for name in NAMES:
            with self.subTest(name=name):
                p = ROOT / "skills" / name / "examples" / "example.md"
                self.assertTrue(p.is_file())
                raw = p.read_text()
                self.assertIn("## Input", raw)
                self.assertIn("## Expected checks", raw)
                self.assertIn("fictional", raw)

    def test_readme_links(self):
        raw = (ROOT / "README.md").read_text()
        links = re.findall(r"\]\((skills/[^)]+)\)", raw)
        self.assertEqual(len(links), 2 * len(NAMES))
        for link in links:
            self.assertTrue((ROOT / link).is_file(), link)

if __name__ == "__main__":
    unittest.main()
