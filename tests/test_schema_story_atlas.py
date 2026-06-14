from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class StoryAtlasSchemaTest(unittest.TestCase):
    def test_schema_matches_v03_contract(self) -> None:
        schema = json.loads((ROOT / "skill" / "templates" / "story-atlas.schema.json").read_text(encoding="utf-8"))
        required = set(schema["required"])
        self.assertTrue({"metadata", "entities", "relations", "events", "actor_mode", "evidence_index"}.issubset(required))
        self.assertEqual(schema["properties"]["schema_version"]["const"], "0.3.0")


if __name__ == "__main__":
    unittest.main()
