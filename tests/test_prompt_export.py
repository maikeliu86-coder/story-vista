from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from storyvista.pipeline import build
from storyvista.prompt_export import export_prompts


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
            self.assertEqual(json.loads((out / "visual-asset-plan.json").read_text(encoding="utf-8"))["style_mode"], "creative-balanced")

    def test_failed_export_rolls_back_every_prompt_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            build(str(INPUT), str(out), ROOT)
            targets = [
                out / "prompts" / "jimeng-prompts.md",
                out / "prompt-pack.md",
                out / "manual-generation-instructions.md",
            ]
            originals = {path: path.read_text(encoding="utf-8") for path in targets}
            plan_path = out / "visual-asset-plan.json"
            plan = json.loads(plan_path.read_text(encoding="utf-8"))
            plan["assets"][0]["prompt"] = "UPDATED PROMPT THAT MUST ROLL BACK"
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            replace_count = 0

            def fail_once(source: Path, target: Path) -> None:
                nonlocal replace_count
                replace_count += 1
                if replace_count == 5:
                    raise OSError("forced prompt publish failure")
                source.replace(target)

            with patch("storyvista.prompt_export._replace_file", side_effect=fail_once):
                with self.assertRaisesRegex(OSError, "forced prompt publish failure"):
                    export_prompts(out, "jimeng")

            for path, original in originals.items():
                self.assertEqual(path.read_text(encoding="utf-8"), original)
            self.assertFalse(any(out.rglob("*.storyvista-prompt-*")))

    def test_provider_export_updates_requested_files_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            build(str(INPUT), str(out), ROOT)
            seedream_path = out / "prompts" / "seedream-prompts.md"
            original_seedream = seedream_path.read_text(encoding="utf-8")
            plan_path = out / "visual-asset-plan.json"
            plan = json.loads(plan_path.read_text(encoding="utf-8"))
            plan["assets"][0]["prompt"] = "TRANSACTIONAL PROMPT UPDATE"
            plan_path.write_text(json.dumps(plan), encoding="utf-8")

            written = export_prompts(out, "jimeng")

            self.assertEqual(
                written,
                [
                    (out / "prompts" / "jimeng-prompts.md").resolve(),
                    (out / "prompt-pack.md").resolve(),
                    (out / "manual-generation-instructions.md").resolve(),
                ],
            )
            self.assertIn("TRANSACTIONAL PROMPT UPDATE", written[0].read_text(encoding="utf-8"))
            self.assertIn("TRANSACTIONAL PROMPT UPDATE", written[1].read_text(encoding="utf-8"))
            self.assertEqual(seedream_path.read_text(encoding="utf-8"), original_seedream)

    def test_export_refuses_prompt_target_directory_before_writing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            build(str(INPUT), str(out), ROOT)
            target = out / "prompts" / "jimeng-prompts.md"
            target.unlink()
            target.mkdir()
            original_pack = (out / "prompt-pack.md").read_text(encoding="utf-8")

            with self.assertRaisesRegex(IsADirectoryError, "not a file"):
                export_prompts(out, "jimeng")

            self.assertTrue(target.is_dir())
            self.assertEqual((out / "prompt-pack.md").read_text(encoding="utf-8"), original_pack)


if __name__ == "__main__":
    unittest.main()
