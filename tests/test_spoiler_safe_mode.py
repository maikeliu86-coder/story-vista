from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SpoilerSafeTest(unittest.TestCase):
    def test_hidden_relationship_is_locked(self) -> None:
        expected = ROOT / "skill/examples/reader-visual-codex-demo/expected"
        state = json.loads((expected / "spoiler-state.json").read_text())
        web = json.loads((expected / "relationship-web.json").read_text())
        locked = [item for item in web["relationships"] if item["spoiler_status"] == "locked"]
        self.assertTrue(state["enabled"])
        self.assertTrue(locked)
        self.assertIn(locked[0]["relation_id"], state["locked_item_ids"])


if __name__ == "__main__":
    unittest.main()
