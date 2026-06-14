from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEYS = {"overview", "characters", "relationships", "locations", "maps", "objects_lore", "timeline", "gallery", "evidence", "settings", "reader_panel"}


class LocaleTest(unittest.TestCase):
    def test_supported_and_experimental_locales(self) -> None:
        for name in ("en", "zh-CN"):
            locale = json.loads((ROOT / f"locales/{name}.json").read_text())
            self.assertEqual(locale["_status"], "supported")
            self.assertTrue(KEYS.issubset(locale))
        for name in ("zh-TW", "ja", "ko", "fr", "es", "de", "ru"):
            self.assertEqual(json.loads((ROOT / f"locales/{name}.json").read_text())["_status"], "experimental")


if __name__ == "__main__":
    unittest.main()
