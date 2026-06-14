from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ObjectLoreCodexTest(unittest.TestCase):
    def test_demo_contains_potion_weapon_and_lore(self) -> None:
        base = ROOT / "skill/examples/reader-visual-codex-demo/expected"
        codex = json.loads((base / "object-lore-codex.json").read_text())
        text = json.dumps(codex, ensure_ascii=False).lower()
        self.assertIn("azure lumen tonic", text)
        self.assertIn("resonance pistol", text)
        self.assertIn("glass meridian", text)
        plan = json.loads((base / "visual-asset-plan.json").read_text())
        types = {item["asset_type"] for item in plan["assets"]}
        self.assertTrue({"character_portrait", "location_keyart", "interpretive_map", "object_lore_keyart", "spoiler_safe_background"}.issubset(types))
        self.assertTrue(all(item["prompt_language"] == "en" for item in plan["assets"]))


if __name__ == "__main__":
    unittest.main()
