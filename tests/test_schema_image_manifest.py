from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ImageManifestSchemaTest(unittest.TestCase):
    def test_manifest_disables_initials_avatar(self) -> None:
        schema = json.loads((ROOT / "skill" / "templates" / "image-manifest.schema.json").read_text(encoding="utf-8"))
        self.assertFalse(schema["properties"]["allow_initials_avatar"]["const"])
        self.assertIn("bound_to", schema["properties"]["assets"]["items"]["required"])


if __name__ == "__main__":
    unittest.main()
