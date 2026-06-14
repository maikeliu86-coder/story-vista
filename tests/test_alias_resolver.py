from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from storyvista.alias_resolver import resolve_aliases  # noqa: E402


class AliasResolverTest(unittest.TestCase):
    def test_western_rule_adds_surname_and_titleless_name(self) -> None:
        chars, ambiguous = resolve_aliases([{"entity_id": "c1", "canonical_name": "Lord Elias Varron", "aliases": []}], {"detected_name_system": "western"})
        self.assertIn("Elias Varron", chars[0]["aliases"])
        self.assertIn("Varron", chars[0]["aliases"])
        self.assertFalse(ambiguous)


if __name__ == "__main__":
    unittest.main()
