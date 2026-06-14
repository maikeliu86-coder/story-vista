from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProviderDetectionTest(unittest.TestCase):
    def test_dotenv_provider_is_detected_and_masked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            env_file = Path(tmp) / ".env"
            env_file.write_text("COMFYUI_API_URL=http://127.0.0.1:8188\nOPENAI_API_KEY=sk-test-secret-value\n", encoding="utf-8")
            result = subprocess.run([
                sys.executable, str(ROOT / "scripts" / "detect_image_provider.py"),
                "--no-network", "--env-file", str(env_file), "--config", str(Path(tmp) / "missing.yaml"),
            ], cwd=ROOT, check=False, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)["storyvista_image_provider_report"]
            providers = {item["provider"]: item for item in report["detected_providers"]}
            self.assertIn("comfyui", providers)
            self.assertIn("openai", providers)
            self.assertNotIn("sk-test-secret-value", result.stdout)


if __name__ == "__main__":
    unittest.main()
