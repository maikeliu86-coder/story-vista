from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from storyvista.provider_preflight import build_provider_choice_state  # noqa: E402


class ProviderPreflightTest(unittest.TestCase):
    def test_missing_provider_falls_back_without_failure(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            state = build_provider_choice_state()
        self.assertEqual(state["selected_provider"], "placeholder-svg")
        self.assertEqual(state["installation_policy"], "recommend-only; never auto-install or create paid accounts")


if __name__ == "__main__":
    unittest.main()
