from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReadmeProviderWorkflowTest(unittest.TestCase):
    def test_readme_documents_jimeng_seedream_and_placeholder_replacement(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for token in ("Why Am I Seeing Placeholders?", "Use Jimeng / 即梦", "Use Seedream / SeeDream", "export-prompts", "bind-images", "rebuild-atlas"):
            self.assertIn(token, readme)


if __name__ == "__main__":
    unittest.main()
