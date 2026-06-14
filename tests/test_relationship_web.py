from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RelationshipWebTest(unittest.TestCase):
    def test_relationships_have_spoiler_status(self) -> None:
        data = json.loads((ROOT / "skill/examples/reader-visual-codex-demo/expected/relationship-web.json").read_text())
        self.assertTrue(data["relationships"])
        self.assertTrue(all(item["spoiler_status"] in {"visible", "locked"} for item in data["relationships"]))


if __name__ == "__main__":
    unittest.main()
