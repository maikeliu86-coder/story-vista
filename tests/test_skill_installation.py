from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillInstallationTest(unittest.TestCase):
    def test_installer_refuses_to_overwrite_existing_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "existing-skill"
            target.mkdir()
            sentinel = target / "keep.txt"
            sentinel.write_text("keep", encoding="utf-8")

            install = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "install_skill.py"), "--target", str(target)],
                cwd=tmp,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(install.returncode, 2)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")

    def test_installed_skill_builds_outside_repository(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            target = tmp_path / "installed-storyvista"
            workdir = tmp_path / "detached-workdir"
            output = workdir / "output"
            workdir.mkdir()

            install = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "install_skill.py"),
                    "--target",
                    str(target),
                ],
                cwd=workdir,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(install.returncode, 0, install.stderr)
            report = json.loads(install.stdout)
            self.assertEqual(Path(report["target"]), target.resolve())
            self.assertTrue((target / "SKILL.md").is_file())

            input_path = target / "skill" / "examples" / "minimal-novel-demo" / "input.txt"
            launcher = target / "scripts" / "storyvista.py"
            build = subprocess.run(
                [sys.executable, str(launcher), "build", str(input_path), "--out", str(output)],
                cwd=workdir,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(build.returncode, 0, build.stderr)
            self.assertTrue((output / "atlas.html").is_file())

            validate = subprocess.run(
                [sys.executable, str(launcher), "validate", str(output)],
                cwd=workdir,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(validate.returncode, 0, validate.stderr)


if __name__ == "__main__":
    unittest.main()
