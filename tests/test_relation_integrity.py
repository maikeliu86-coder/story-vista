from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from storyvista.chunking import chunk_text  # noqa: E402
from storyvista.entity_model import extract_entities  # noqa: E402


class RelationIntegrityTest(unittest.TestCase):
    def test_relation_endpoints_and_evidence_resolve(self) -> None:
        text = (ROOT / "skill" / "examples" / "minimal-novel-demo" / "input.txt").read_text(encoding="utf-8")
        atlas = extract_entities(text, chunk_text(text), "吴越夜雨")
        entity_ids = {item["entity_id"] for item in atlas["entities"]["characters"]}
        for relation in atlas["relations"]:
            self.assertIn(relation["source_entity_id"], entity_ids)
            self.assertIn(relation["target_entity_id"], entity_ids)
            self.assertTrue(relation["evidence"] or relation["status"] == "unresolved")


if __name__ == "__main__":
    unittest.main()
