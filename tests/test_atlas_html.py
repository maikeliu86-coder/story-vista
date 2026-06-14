from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AtlasHtmlTest(unittest.TestCase):
    def test_reader_sync_and_jump_controls_exist(self) -> None:
        html = (ROOT / "skill/examples/reader-visual-codex-demo/expected/atlas.html").read_text()
        for token in ("reader-handle", "reader-toggle", "entity-highlight", "data-paragraph", "localStorage", "themeProfile", "Objects & Lore", "Relationships", "Gallery"):
            self.assertIn(token, html)


if __name__ == "__main__":
    unittest.main()
