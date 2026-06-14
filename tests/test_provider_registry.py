from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from storyvista.providers.registry import PROVIDER_REGISTRY, get_provider  # noqa: E402


class ProviderRegistryTest(unittest.TestCase):
    def test_real_and_manual_provider_paths_are_distinct(self) -> None:
        provider_ids = {item["provider_id"] for item in PROVIDER_REGISTRY}
        for provider_id in ("jimeng", "jianying-jimeng", "bytedance-seedream", "volcengine-seedream", "prompt-pack", "placeholder-svg"):
            self.assertIn(provider_id, provider_ids)
        self.assertEqual(get_provider("jimeng")["provider_type"], "manual-web")
        self.assertEqual(get_provider("volcengine-seedream")["provider_type"], "direct-api")
        self.assertTrue(get_provider("bytedance-seedream")["supports_prompt_export"])
        self.assertTrue(get_provider("jimeng")["supports_manual_binding"])


if __name__ == "__main__":
    unittest.main()
