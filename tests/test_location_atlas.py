from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LocationAtlasTest(unittest.TestCase):
    def test_locations_and_interpretive_map_exist(self) -> None:
        base = ROOT / "skill/examples/reader-visual-codex-demo/expected"
        locations = json.loads((base / "location-atlas.json").read_text())
        map_plan = json.loads((base / "map-plan.json").read_text())
        self.assertGreaterEqual(len(locations["locations"]), 3)
        self.assertEqual(map_plan["map_type"], "interpretive")
        self.assertIn("interpretive", map_plan["disclaimer"].lower())


if __name__ == "__main__":
    unittest.main()
