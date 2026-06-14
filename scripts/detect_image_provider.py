#!/usr/bin/env python3
"""PEP-8 filename wrapper for the existing provider detector."""

from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("detect-image-provider.py")), run_name="__main__")
