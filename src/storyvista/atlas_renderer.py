from __future__ import annotations

import json
from pathlib import Path


def render_atlas(atlas: dict, manifest: dict, template_path: Path, output_path: Path) -> None:
    template = template_path.read_text(encoding="utf-8")
    payload = json.dumps({"atlas": atlas, "manifest": manifest}, ensure_ascii=False).replace("</", "<\\/")
    html = template.replace("__STORYVISTA_DATA__", payload)
    output_path.write_text(html, encoding="utf-8")
