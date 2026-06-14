from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from storyvista.chunking import chunk_text  # noqa: E402
from storyvista.entity_model import extract_entities  # noqa: E402


class SourceEvidenceTest(unittest.TestCase):
    def test_explicit_story_claims_have_source_evidence(self) -> None:
        text = (ROOT / "skill" / "examples" / "minimal-novel-demo" / "input.txt").read_text(encoding="utf-8")
        atlas = extract_entities(text, chunk_text(text), "吴越夜雨")
        for group in (atlas["entities"]["characters"], atlas["entities"]["locations"], atlas["events"]):
            for item in group:
                self.assertTrue(item["evidence"], item.get("name") or item.get("title"))


if __name__ == "__main__":
    unittest.main()
