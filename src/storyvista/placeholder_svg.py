from __future__ import annotations

from html import escape
from pathlib import Path


def entity_lookup(atlas: dict) -> dict:
    lookup = {}
    for group in atlas["entities"].values():
        for item in group:
            lookup[item["entity_id"]] = item
    for event in atlas["events"]:
        lookup[event["event_id"]] = event
    return lookup


def icon_for(entity_type: str) -> str:
    if entity_type == "character":
        return '<circle cx="160" cy="112" r="42"/><path d="M78 270c9-69 42-104 82-104s73 35 82 104"/>'
    if entity_type == "location":
        return '<path d="M70 258h180M94 258V142l66-52 66 52v116M132 258v-68h56v68"/>'
    if entity_type == "organization":
        return '<path d="M160 70l70 30v56c0 54-29 94-70 118-41-24-70-64-70-118v-56z"/>'
    return '<circle cx="160" cy="162" r="76"/><path d="M160 106v112M104 162h112"/>'


def svg_for(item: dict) -> str:
    entity_type = item.get("entity_type", "event" if "event_id" in item else "concept")
    name = item.get("name") or item.get("title") or item.get("entity_id") or item.get("event_id")
    subtitle = item.get("narrative_function") or item.get("location_type") or item.get("summary", "Story event")
    keywords = item.get("visual_keywords") or item.get("mood") or []
    keyword_text = " · ".join(keywords[:3]) if isinstance(keywords, list) else str(keywords)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 420" role="img" aria-labelledby="title desc">
<title id="title">{escape(str(name))}</title><desc id="desc">Semantic {escape(entity_type)} placeholder</desc>
<rect width="320" height="420" fill="#141617"/><rect x="18" y="18" width="284" height="384" fill="#1c1e20" stroke="#655c48"/>
<g fill="none" stroke="#c6a967" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{icon_for(entity_type)}</g>
<text x="30" y="322" fill="#d8d6d0" font-family="Georgia,serif" font-size="23">{escape(str(name)[:18])}</text>
<text x="30" y="350" fill="#c6a967" font-family="Arial,sans-serif" font-size="12" letter-spacing="2">{escape(entity_type.upper())}</text>
<text x="30" y="376" fill="#8d9093" font-family="Arial,sans-serif" font-size="12">{escape(str(subtitle)[:36])}</text>
<text x="30" y="395" fill="#6f7377" font-family="Arial,sans-serif" font-size="10">{escape(keyword_text[:48])}</text>
</svg>'''


def generate_placeholders(atlas: dict, manifest: dict, out_dir: Path) -> list[str]:
    lookup = entity_lookup(atlas)
    placeholder_dir = out_dir / "assets" / "placeholders"
    placeholder_dir.mkdir(parents=True, exist_ok=True)
    created = []
    for asset in manifest["assets"]:
        item = lookup.get(asset["bound_to"], {"name": asset["bound_to"], "entity_type": "concept"})
        path = out_dir / asset["file_path"]
        path.write_text(svg_for(item), encoding="utf-8")
        created.append(str(path))
    return created
