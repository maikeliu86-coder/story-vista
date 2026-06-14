from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "skill/examples/reader-visual-codex-demo/input.txt"
REQUIRED = {
    "source-index.json", "chunks.json", "language-profile.json", "reader-text.json",
    "entity-linking.json", "character-atlas.json", "relationship-web.json",
    "location-atlas.json", "map-plan.json", "object-lore-codex.json",
    "visual-evidence.json", "visual-asset-plan.json", "image-manifest.json",
    "spoiler-state.json", "provider-choice-state.json", "theme-profile.json",
    "atlas.html", "verification-report.md",
}


class ReaderVisualCodexDemoTest(unittest.TestCase):
    def test_quick_start_builds_complete_demo(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            result = subprocess.run([sys.executable, str(ROOT / "scripts/storyvista.py"), "build", str(INPUT), "--out", str(out), "--ui-language", "auto"], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(REQUIRED.issubset({path.name for path in out.iterdir()}))
            self.assertEqual(json.loads((out / "character-atlas.json").read_text())["characters"][0]["canonical_name"], "Lord Elias Alexander Varron")
            self.assertGreaterEqual(len(list((out / "assets/placeholders").glob("*.svg"))), 10)


if __name__ == "__main__":
    unittest.main()
