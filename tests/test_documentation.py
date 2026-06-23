import os
import re
import unittest


class TestMarkdownDocumentation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("🚀 Running Markdown Linting CI Tests...\n")
        cls.readme_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "README.md")
        )

    def test_readme_exists(self):
        """Test 1: Ensure the README.md file exists at the project root."""
        self.assertTrue(
            os.path.exists(self.readme_path),
            "README.md is missing from the repository root.",
        )

    def test_readme_has_title(self):
        """Test 2: Ensure the README contains a top-level markdown heading (# Title)."""
        with open(self.readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for at least one H1 heading
        has_h1 = bool(re.search(r"^#\s+.+", content, re.MULTILINE))
        self.assertTrue(
            has_h1,
            "README.md must contain a top-level heading (e.g., '# Project Title').",
        )

    def test_no_empty_links(self):
        """Test 3: Detect empty or broken markdown links (e.g., [Link Text]())."""
        with open(self.readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex to find links with empty destination parentheses: [something]()
        empty_links = re.findall(r"\[.*?\]\(\)", content)

        self.assertEqual(
            len(empty_links),
            0,
            f"Found {len(empty_links)} empty markdown links. Please provide valid URLs.",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
