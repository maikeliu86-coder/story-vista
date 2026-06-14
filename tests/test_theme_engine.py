from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from storyvista.theme_engine import build_theme_profile  # noqa: E402


class ThemeEngineTest(unittest.TestCase):
    def test_ancient_and_scifi_presets(self) -> None:
        ancient = build_theme_profile("竹林古道青瓦江湖")
        scifi = build_theme_profile("starship space station holographic colony planet")
        self.assertEqual(ancient["theme_id"], "ancient-chinese-literary")
        self.assertIn("xuan paper", ancient["background_prompt"])
        self.assertEqual(scifi["theme_id"], "futuristic-sci-fi")
        self.assertIn("deep space", scifi["background_prompt"])


if __name__ == "__main__":
    unittest.main()
