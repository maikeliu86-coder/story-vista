from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from storyvista.language_detection import detect_language_profile  # noqa: E402


class LanguageProfileTest(unittest.TestCase):
    def test_auto_and_override(self) -> None:
        self.assertEqual(detect_language_profile("A long English novel passage.")["ui_language"], "en")
        self.assertEqual(detect_language_profile("这是一个足够长的中文小说片段，人物走过古道。" * 3)["ui_language"], "zh-CN")
        self.assertEqual(detect_language_profile("English source", "zh-CN")["ui_language"], "zh-CN")
        self.assertEqual(detect_language_profile("中文来源" * 8, "en")["ui_language"], "en")


if __name__ == "__main__":
    unittest.main()
