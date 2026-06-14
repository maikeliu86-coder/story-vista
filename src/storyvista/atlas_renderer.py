from __future__ import annotations

import json
from pathlib import Path


def render_atlas(payload: dict, template_path: Path, output_path: Path) -> None:
    template = template_path.read_text(encoding="utf-8")
    serialized = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    html = template.replace("__STORYVISTA_DATA__", serialized)
    output_path.write_text(html, encoding="utf-8")
