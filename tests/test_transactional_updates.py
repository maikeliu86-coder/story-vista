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

from storyvista.pipeline import bind_images_and_rebuild, build, rebuild_atlas


INPUT = ROOT / "skill" / "examples" / "minimal-novel-demo" / "input.txt"
PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Z8Z8AAAAASUVORK5CYII="
)


class TransactionalUpdateTest(unittest.TestCase):
    def test_failed_rebuild_preserves_existing_html_and_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "demo"
            build(str(INPUT), str(out), ROOT)
            original_html = (out / "atlas.html").read_text(encoding="utf-8")
            original_report = (out / "verification-report.md").read_text(encoding="utf-8")

            def fail_after_write(staging: Path, _repo_root: Path) -> None:
                (staging / "atlas.html").write_text("partial rebuild", encoding="utf-8")
                raise RuntimeError("forced rebuild failure")

            with patch("storyvista.pipeline._render_payload", side_effect=fail_after_write):
                with self.assertRaisesRegex(RuntimeError, "forced rebuild failure"):
                    rebuild_atlas(str(out), ROOT)

            self.assertEqual((out / "atlas.html").read_text(encoding="utf-8"), original_html)
            self.assertEqual((out / "verification-report.md").read_text(encoding="utf-8"), original_report)
            self.assertFalse(any(root.glob(".demo-rebuild-*")))

    def test_rebuild_warnings_do_not_publish_new_html_or_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            build(str(INPUT), str(out), ROOT)
            original_html = (out / "atlas.html").read_text(encoding="utf-8")
            original_report = (out / "verification-report.md").read_text(encoding="utf-8")
            manifest_path = out / "image-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["allow_initials_avatar"] = True
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

            result = rebuild_atlas(str(out), ROOT)

            self.assertFalse(result["published"])
            self.assertTrue(any("allow_initials_avatar" in warning for warning in result["warnings"]))
            self.assertEqual((out / "atlas.html").read_text(encoding="utf-8"), original_html)
            self.assertEqual((out / "verification-report.md").read_text(encoding="utf-8"), original_report)

    def test_failed_bind_rebuild_preserves_manifest_and_generated_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "demo"
            assets = root / "external"
            assets.mkdir()
            build(str(INPUT), str(out), ROOT)
            original_manifest = (out / "image-manifest.json").read_text(encoding="utf-8")
            original_html = (out / "atlas.html").read_text(encoding="utf-8")
            manifest = json.loads(original_manifest)
            asset_id = manifest["assets"][0]["asset_id"]
            (assets / f"{asset_id}.png").write_bytes(PNG_1X1)

            def fail_after_write(staging: Path, _repo_root: Path) -> None:
                (staging / "atlas.html").write_text("partial bind rebuild", encoding="utf-8")
                raise RuntimeError("forced bind rebuild failure")

            with patch("storyvista.pipeline._render_payload", side_effect=fail_after_write):
                with self.assertRaisesRegex(RuntimeError, "forced bind rebuild failure"):
                    bind_images_and_rebuild(str(out), str(assets), ROOT)

            self.assertEqual((out / "image-manifest.json").read_text(encoding="utf-8"), original_manifest)
            self.assertEqual((out / "atlas.html").read_text(encoding="utf-8"), original_html)
            self.assertFalse((out / "assets" / "generated" / f"{asset_id}.png").exists())
            self.assertFalse((out / "binding-report.json").exists())
            self.assertFalse(any(root.glob(".demo-bind-*")))

    def test_invalid_bind_is_reported_without_publishing_changes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "demo"
            assets = root / "external"
            assets.mkdir()
            build(str(INPUT), str(out), ROOT)
            original_manifest = (out / "image-manifest.json").read_text(encoding="utf-8")
            original_html = (out / "atlas.html").read_text(encoding="utf-8")
            asset_id = json.loads(original_manifest)["assets"][0]["asset_id"]
            (assets / f"{asset_id}.png").write_text("not an image", encoding="utf-8")

            result = bind_images_and_rebuild(str(out), str(assets), ROOT)

            self.assertFalse(result["published"])
            self.assertEqual(result["invalid"], [f"{asset_id}.png"])
            self.assertEqual((out / "image-manifest.json").read_text(encoding="utf-8"), original_manifest)
            self.assertEqual((out / "atlas.html").read_text(encoding="utf-8"), original_html)
            self.assertFalse((out / "binding-report.json").exists())

    def test_successful_bind_and_rebuild_publish_together(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "demo"
            assets = root / "external"
            assets.mkdir()
            build(str(INPUT), str(out), ROOT)
            manifest = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))
            asset_id = manifest["assets"][0]["asset_id"]
            (assets / f"{asset_id}.png").write_bytes(PNG_1X1)

            result = bind_images_and_rebuild(str(out), str(assets), ROOT)

            self.assertTrue(result["published"])
            self.assertEqual(result["matched_count"], 1)
            rebound = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))["assets"][0]
            self.assertEqual(rebound["status"], "generated_external")
            self.assertIn(rebound["file_path"], (out / "atlas.html").read_text(encoding="utf-8"))
            self.assertTrue((out / "binding-report.json").exists())


if __name__ == "__main__":
    unittest.main()
