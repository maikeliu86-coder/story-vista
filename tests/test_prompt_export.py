from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "skill" / "examples" / "minimal-novel-demo" / "input.txt"


class PromptExportTest(unittest.TestCase):
    def test_build_and_provider_export_create_actionable_prompt_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            subprocess.run([sys.executable, str(ROOT / "scripts" / "storyvista.py"), "build", str(INPUT), "--out", str(out)], cwd=ROOT, check=True, capture_output=True, text=True)
            result = subprocess.run([sys.executable, str(ROOT / "scripts" / "storyvista.py"), "export-prompts", str(out), "--provider", "jimeng"], cwd=ROOT, check=False, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            jimeng = (out / "prompts" / "jimeng-prompts.md").read_text(encoding="utf-8")
            self.assertIn("中文可复制提示词", jimeng)
            self.assertIn("Expected filename", jimeng)
            self.assertTrue((out / "prompts" / "seedream-prompts.md").exists())
            self.assertTrue((out / "prompt-pack.md").exists())
            self.assertTrue((out / "manual-generation-instructions.md").exists())
            self.assertEqual(__import__("json").loads((out / "visual-asset-plan.json").read_text(encoding="utf-8"))["style_mode"], "creative-balanced")


if __name__ == "__main__":
    unittest.main()
