from __future__ import annotations

import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PlaceholderAssetsTest(unittest.TestCase):
    def test_placeholder_contains_full_name_and_no_initials_policy(self) -> None:
        import subprocess
        import sys

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            subprocess.run([
                sys.executable, str(ROOT / "scripts" / "storyvista.py"), "build",
                str(ROOT / "skill" / "examples" / "minimal-novel-demo" / "input.txt"), "--out", str(out),
            ], cwd=ROOT, check=True, capture_output=True, text=True)
            svg = (out / "assets" / "placeholders" / "char_001.svg").read_text(encoding="utf-8")
            manifest = (out / "image-manifest.json").read_text(encoding="utf-8")
            self.assertIn("沈砚", svg)
            self.assertIn('"allow_initials_avatar": false', manifest)


if __name__ == "__main__":
    unittest.main()
