from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from storyvista.image_binding import bind_images
from storyvista.pipeline import build
from storyvista.prompt_export import export_prompts
from storyvista.validators import validate_output


INPUT = ROOT / "skill" / "examples" / "minimal-novel-demo" / "input.txt"


class SafetyValidationTest(unittest.TestCase):
    def test_prompt_export_rejects_path_traversal_provider(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            out.mkdir()
            (out / "visual-asset-plan.json").write_text(
                json.dumps({"assets": [], "selected_provider": "prompt-pack"}),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "provider"):
                export_prompts(out, "../../escaped")
            self.assertFalse((Path(tmp) / "escaped-prompts.md").exists())

    def test_image_binding_rejects_path_traversal_asset_id(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            assets = Path(tmp) / "assets"
            out.mkdir()
            assets.mkdir()
            manifest = {
                "assets": [{"asset_id": "../../../escaped", "expected_file_path": "assets/generated/escaped.png"}],
            }
            (out / "image-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            (assets / "escaped.png").write_bytes(b"not an image")

            with self.assertRaisesRegex(ValueError, "asset_id"):
                bind_images(out, assets)
            self.assertFalse((Path(tmp) / "escaped.png").exists())

    def test_image_binding_rejects_text_disguised_as_png(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            assets = Path(tmp) / "assets"
            out.mkdir()
            assets.mkdir()
            manifest = {
                "provider_status": "prompt-workflow-ready",
                "assets": [{"asset_id": "asset_char_001_portrait", "expected_file_path": "assets/generated/asset_char_001_portrait.png"}],
            }
            (out / "image-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            (assets / "asset_char_001_portrait.png").write_text("plain text", encoding="utf-8")

            result = bind_images(out, assets)

            self.assertEqual(result["matched_count"], 0)
            self.assertEqual(result["invalid"], ["asset_char_001_portrait.png"])
            self.assertFalse((out / "assets" / "generated" / "asset_char_001_portrait.png").exists())

    def test_empty_input_returns_nonzero_exit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "empty.txt"
            source.write_text("\n\t", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "build", str(source), "--out", str(Path(tmp) / "out")],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Input text is empty", result.stderr)

    def test_zero_extraction_returns_nonzero_exit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "no-entities.txt"
            source.write_text("天气很好。", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "build", str(source), "--out", str(Path(tmp) / "out")],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn("no extracted entities", result.stdout)

    def test_validate_checks_story_atlas_schema(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            result = build(str(INPUT), str(out), ROOT)
            self.assertFalse(result["warnings"])
            atlas_path = out / "story-atlas.json"
            atlas = json.loads(atlas_path.read_text(encoding="utf-8"))
            atlas["schema_version"] = "broken"
            atlas_path.write_text(json.dumps(atlas), encoding="utf-8")

            _, warnings = validate_output(out)

            self.assertTrue(any("Schema story-atlas.json" in item and "schema_version" in item for item in warnings))

    def test_validate_rejects_locked_details_in_safe_atlas(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            result = build(str(INPUT), str(out), ROOT)
            self.assertFalse(result["warnings"])
            atlas_path = out / "story-atlas.json"
            atlas = json.loads(atlas_path.read_text(encoding="utf-8"))
            atlas["relations"][0]["spoiler_status"] = "locked"
            atlas_path.write_text(json.dumps(atlas), encoding="utf-8")

            _, warnings = validate_output(out)

            self.assertTrue(any("Spoiler-safe atlas exposes locked items" in item for item in warnings))

    def test_validate_rejects_invalid_bound_image(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            result = build(str(INPUT), str(out), ROOT)
            self.assertFalse(result["warnings"])
            manifest_path = out / "image-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            asset = manifest["assets"][0]
            fake_path = out / "assets" / "generated" / f"{asset['asset_id']}.png"
            fake_path.parent.mkdir(parents=True, exist_ok=True)
            fake_path.write_text("plain text", encoding="utf-8")
            asset["file_path"] = str(fake_path.relative_to(out))
            asset["status"] = "generated_external"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

            _, warnings = validate_output(out)

            self.assertTrue(any("Invalid raster image" in item for item in warnings))

    def test_validate_checks_image_manifest_schema(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            result = build(str(INPUT), str(out), ROOT)
            self.assertFalse(result["warnings"])
            manifest_path = out / "image-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["allow_initials_avatar"] = True
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

            _, warnings = validate_output(out)

            self.assertTrue(any("Schema image-manifest.json" in item and "allow_initials_avatar" in item for item in warnings))

    def test_bind_cli_returns_nonzero_for_invalid_image(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            assets = Path(tmp) / "assets"
            assets.mkdir()
            result = build(str(INPUT), str(out), ROOT)
            self.assertFalse(result["warnings"])
            manifest = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))
            asset_id = manifest["assets"][0]["asset_id"]
            (assets / f"{asset_id}.png").write_text("plain text", encoding="utf-8")

            cli = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "bind-images", str(out), "--assets", str(assets)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(cli.returncode, 1)
            self.assertIn(f'"invalid": [\n    "{asset_id}.png"', cli.stdout)
            self.assertIn('"published": false', cli.stdout)
            self.assertFalse((out / "binding-report.json").exists())


if __name__ == "__main__":
    unittest.main()
