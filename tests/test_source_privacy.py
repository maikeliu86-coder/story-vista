from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "examples" / "visual-atlas-demo" / "story.md"


class SourcePrivacyTest(unittest.TestCase):
    def test_source_index_does_not_expose_absolute_input_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            private_root = Path(tmp) / "private-library" / "unshared-folder"
            private_root.mkdir(parents=True)
            input_path = private_root / "private-story.md"
            input_path.write_text(SOURCE.read_text(encoding="utf-8"), encoding="utf-8")
            output = Path(tmp) / "output"

            build = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "storyvista.py"),
                    "build",
                    str(input_path.resolve()),
                    "--out",
                    str(output),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(build.returncode, 0, build.stderr)

            source_index_text = (output / "source-index.json").read_text(encoding="utf-8")
            source_index = json.loads(source_index_text)
            self.assertEqual(source_index["sources"][0]["path"], input_path.name)
            self.assertNotIn(str(private_root), source_index_text)


if __name__ == "__main__":
    unittest.main()
