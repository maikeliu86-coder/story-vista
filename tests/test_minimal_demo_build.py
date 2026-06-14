from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "skill" / "examples" / "minimal-novel-demo" / "input.txt"


class MinimalDemoBuildTest(unittest.TestCase):
    def test_build_creates_complete_atlas(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "build", str(INPUT), "--out", str(out)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            for name in ("source-index.json", "chunks.json", "story-atlas.json", "visual-asset-plan.json", "image-manifest.json", "atlas.html", "verification-report.md"):
                self.assertTrue((out / name).exists(), name)
            payload = json.loads((out / "story-atlas.json").read_text(encoding="utf-8"))
            self.assertEqual(len(payload["entities"]["characters"]), 5)
            self.assertEqual(payload["metadata"]["title"], "吴越夜雨")
            self.assertTrue(payload["summary"].startswith("雨水沿宫门"))
            self.assertIn("warnings", result.stdout)


if __name__ == "__main__":
    unittest.main()
