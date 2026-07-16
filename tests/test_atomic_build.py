from __future__ import annotations

import base64
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from storyvista.image_binding import bind_images
from storyvista.pipeline import build
from storyvista.validators import validate_output


INPUT = ROOT / "skill" / "examples" / "minimal-novel-demo" / "input.txt"
OTHER_INPUT = ROOT / "skill" / "examples" / "bilingual-demo" / "input.txt"
PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Z8Z8AAAAASUVORK5CYII="
)


class AtomicBuildTest(unittest.TestCase):
    def test_failed_build_preserves_existing_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "demo"
            out.mkdir()
            original_source_index = '{"stable": true}\n'
            (out / "source-index.json").write_text(original_source_index, encoding="utf-8")
            (out / "keep.txt").write_text("existing output", encoding="utf-8")

            with patch("storyvista.pipeline._render_payload", side_effect=RuntimeError("forced render failure")):
                with self.assertRaisesRegex(RuntimeError, "forced render failure"):
                    build(str(INPUT), str(out), ROOT)

            self.assertEqual((out / "source-index.json").read_text(encoding="utf-8"), original_source_index)
            self.assertEqual((out / "keep.txt").read_text(encoding="utf-8"), "existing output")
            self.assertFalse((out / "story-atlas.json").exists())
            self.assertFalse(any(root.glob(".demo-build-*")))

    def test_repeated_build_replaces_stale_output_and_preserves_bound_image(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "demo"
            assets = root / "external"
            assets.mkdir()

            first = build(str(INPUT), str(out), ROOT)
            self.assertFalse(first["warnings"])
            manifest = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))
            asset_id = manifest["assets"][0]["asset_id"]
            (assets / f"{asset_id}.png").write_bytes(PNG_1X1)
            bound = bind_images(out, assets)
            self.assertEqual(bound["matched_count"], 1)

            (out / "binding-report.json").write_text('{"stale": true}\n', encoding="utf-8")
            (out / "notes.txt").write_text("keep this", encoding="utf-8")
            unbound_image = out / "assets" / "generated" / "unbound-reference.png"
            unbound_image.write_bytes(PNG_1X1)

            second = build(str(INPUT), str(out), ROOT)

            self.assertFalse(second["warnings"])
            self.assertEqual((out / "notes.txt").read_text(encoding="utf-8"), "keep this")
            self.assertTrue(unbound_image.exists())
            preserved = out / "assets" / "generated" / f"{asset_id}.png"
            self.assertTrue(preserved.exists())
            rebound = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))["assets"][0]
            self.assertEqual(rebound["status"], "generated_external")
            self.assertEqual(rebound["file_path"], f"assets/generated/{asset_id}.png")
            binding_report = json.loads((out / "binding-report.json").read_text(encoding="utf-8"))
            self.assertTrue(binding_report["preserved_from_previous_build"])
            _, warnings = validate_output(out)
            self.assertFalse(warnings)

    def test_new_story_does_not_reuse_previous_story_image(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "demo"
            assets = root / "external"
            assets.mkdir()

            first = build(str(INPUT), str(out), ROOT)
            self.assertFalse(first["warnings"])
            old_manifest = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))
            asset_id = old_manifest["assets"][0]["asset_id"]
            (assets / f"{asset_id}.png").write_bytes(PNG_1X1)
            bound = bind_images(out, assets)
            self.assertEqual(bound["matched_count"], 1)

            second = build(str(OTHER_INPUT), str(out), ROOT)

            self.assertFalse(second["warnings"])
            self.assertEqual(second["preserved_images"], 0)
            self.assertTrue((out / "assets" / "generated" / f"{asset_id}.png").exists())
            new_asset = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))["assets"][0]
            self.assertEqual(new_asset["status"], "pending_external_generation")
            self.assertIn("Lady Amara Valecourt", new_asset["prompt"])

    def test_build_refuses_non_storyvista_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "personal-files"
            out.mkdir()
            note = out / "notes.txt"
            note.write_text("do not replace", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "non-StoryVista"):
                build(str(INPUT), str(out), ROOT)

            self.assertEqual(note.read_text(encoding="utf-8"), "do not replace")


if __name__ == "__main__":
    unittest.main()
