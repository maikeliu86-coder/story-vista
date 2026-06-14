from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from storyvista.visual_profile import build_visual_profile  # noqa: E402


class CharacterVisualProfileTest(unittest.TestCase):
    def test_statuses_are_explicit(self) -> None:
        profile = build_visual_profile({"canonical_name": "Mira", "role_name": "doctor", "faction": "clinic", "evidence": []})
        statuses = {item["status"] for item in profile.values()}
        self.assertTrue({"confirmed", "contextual", "inferred", "unknown"}.issubset(statuses))


if __name__ == "__main__":
    unittest.main()
