from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "skill" / "examples" / "reader-visual-codex-demo" / "input.txt"
LOCKED_DETAILS = (
    "secret brotherhood oath",
    "The Oath Beneath the Dome",
    "A hidden oath connects the captain and the cartographer.",
)


class SpoilerSafeTest(unittest.TestCase):
    def test_safe_build_redacts_locked_details_while_full_build_preserves_them(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            safe = root / "safe"
            full = root / "full"
            for mode, output in (("safe", safe), ("full", full)):
                build = subprocess.run(
                    [
                        sys.executable,
                        str(ROOT / "scripts" / "storyvista.py"),
                        "build",
                        str(INPUT),
                        "--out",
                        str(output),
                        "--spoiler-mode",
                        mode,
                    ],
                    cwd=ROOT,
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(build.returncode, 0, build.stderr)

            safe_state = json.loads((safe / "spoiler-state.json").read_text(encoding="utf-8"))
            safe_atlas = json.loads((safe / "story-atlas.json").read_text(encoding="utf-8"))
            full_atlas = json.loads((full / "story-atlas.json").read_text(encoding="utf-8"))
            safe_chunks = json.loads((safe / "chunks.json").read_text(encoding="utf-8"))["chunks"]
            full_chunks = json.loads((full / "chunks.json").read_text(encoding="utf-8"))["chunks"]
            self.assertTrue(safe_state["enabled"])
            self.assertEqual(len(safe_state["locked_item_ids"]), 2)
            self.assertEqual(
                [(item["start_offset"], item["end_offset"]) for item in safe_chunks],
                [(item["start_offset"], item["end_offset"]) for item in full_chunks],
            )
            self.assertFalse(any(item["spoiler_status"] == "locked" for item in safe_atlas["relations"]))
            self.assertFalse(any(item["spoiler_status"] == "locked" for item in safe_atlas["events"]))
            self.assertTrue(any(item["spoiler_status"] == "locked" for item in full_atlas["relations"]))
            self.assertTrue(any(item["spoiler_status"] == "locked" for item in full_atlas["events"]))

            safe_text = "\n".join(
                path.read_text(encoding="utf-8", errors="ignore")
                for path in safe.rglob("*")
                if path.is_file() and path.suffix.lower() in {".json", ".html", ".md", ".txt"}
            )
            full_text = "\n".join(
                path.read_text(encoding="utf-8", errors="ignore")
                for path in full.rglob("*")
                if path.is_file() and path.suffix.lower() in {".json", ".html", ".md", ".txt"}
            )
            for detail in LOCKED_DETAILS:
                self.assertNotIn(detail, safe_text)
                self.assertIn(detail, full_text)

    def test_hidden_relationship_is_locked(self) -> None:
        expected = ROOT / "skill/examples/reader-visual-codex-demo/expected"
        state = json.loads((expected / "spoiler-state.json").read_text())
        web = json.loads((expected / "relationship-web.json").read_text())
        locked = [item for item in web["relationships"] if item["spoiler_status"] == "locked"]
        self.assertTrue(state["enabled"])
        self.assertTrue(locked)
        self.assertIn(locked[0]["relation_id"], state["locked_item_ids"])


if __name__ == "__main__":
    unittest.main()
