from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "skill/examples/reader-visual-codex-demo/expected"


class ReaderTextLinkingTest(unittest.TestCase):
    def test_links_support_bidirectional_jump_contract(self) -> None:
        reader = json.loads((OUT / "reader-text.json").read_text())
        links = json.loads((OUT / "entity-linking.json").read_text())
        paragraph_ids = {item["paragraph_id"] for item in reader["paragraphs"]}
        self.assertGreater(len(links["links"]), 10)
        self.assertTrue(all(item["paragraph_id"] in paragraph_ids for item in links["links"]))


if __name__ == "__main__":
    unittest.main()
