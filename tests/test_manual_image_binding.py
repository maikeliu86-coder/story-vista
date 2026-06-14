from __future__ import annotations

import base64
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "skill" / "examples" / "minimal-novel-demo" / "input.txt"
PNG_1X1 = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Z8Z8AAAAASUVORK5CYII=")


class ManualImageBindingTest(unittest.TestCase):
    def test_exact_filename_updates_manifest_and_rebuilds_atlas(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            assets = Path(tmp) / "external"
            assets.mkdir()
            subprocess.run([sys.executable, str(ROOT / "scripts" / "storyvista.py"), "build", str(INPUT), "--out", str(out)], cwd=ROOT, check=True, capture_output=True, text=True)
            manifest = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))
            asset_id = manifest["assets"][0]["asset_id"]
            (assets / f"{asset_id}.png").write_bytes(PNG_1X1)

            result = subprocess.run([sys.executable, str(ROOT / "scripts" / "storyvista.py"), "bind-images", str(out), "--assets", str(assets)], cwd=ROOT, check=False, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            rebound = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))["assets"][0]
            self.assertEqual(rebound["status"], "generated_external")
            self.assertEqual(rebound["file_path"], f"assets/generated/{asset_id}.png")
            self.assertIn(rebound["file_path"], (out / "atlas.html").read_text(encoding="utf-8"))
            self.assertTrue((out / "binding-report.json").exists())


if __name__ == "__main__":
    unittest.main()
