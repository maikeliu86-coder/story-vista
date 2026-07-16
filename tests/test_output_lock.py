from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from storyvista.output_lock import output_lock
from storyvista.pipeline import build


INPUT = ROOT / "skill" / "examples" / "minimal-novel-demo" / "input.txt"


class OutputLockTest(unittest.TestCase):
    def test_writer_commands_refuse_an_output_locked_by_another_process(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "demo"
            assets = root / "assets"
            assets.mkdir()
            build(str(INPUT), str(out), ROOT)
            original_atlas = (out / "atlas.html").read_text(encoding="utf-8")
            commands = [
                ["build", str(INPUT), "--out", str(out)],
                ["rebuild-atlas", str(out)],
                ["bind-images", str(out), "--assets", str(assets)],
                ["export-prompts", str(out), "--provider", "seedream"],
                ["validate", str(out)],
            ]

            with output_lock(out, "test-holder"):
                for command in commands:
                    completed = subprocess.run(
                        [sys.executable, str(ROOT / "scripts" / "storyvista.py"), *command],
                        cwd=ROOT,
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(completed.returncode, 2, command)
                    self.assertIn("already being modified", completed.stderr)

            completed = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "rebuild-atlas", str(out)],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual((out / "atlas.html").read_text(encoding="utf-8"), original_atlas)
            self.assertFalse(any(root.rglob("*.storyvista.lock")))


if __name__ == "__main__":
    unittest.main()
