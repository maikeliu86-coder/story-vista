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
        self.assertEqual(state["status"], "prompt-workflow-ready")
        self.assertEqual(state["selected_provider"], "openai-image")
        self.assertEqual(state["fallback_provider"], "placeholder-svg")
        self.assertTrue(state["prompt_only"])
        self.assertEqual(state["installation_policy"], "recommend-only; never auto-install or create paid accounts")

    def test_multiple_configured_providers_recommend_a_configured_provider(self) -> None:
        with patch.dict(os.environ, {"OPENAI_API_KEY": "masked", "FAL_KEY": "masked"}, clear=True):
            state = build_provider_choice_state()
        self.assertEqual(state["recommended_provider"], "openai-image")
        self.assertFalse(state["prompt_only"])
        self.assertEqual({item["status"] for item in state["detected_providers"]}, {"detected-but-unverified"})


if __name__ == "__main__":
    unittest.main()
