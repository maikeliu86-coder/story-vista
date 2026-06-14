from __future__ import annotations

import json
from pathlib import Path


EXPORT_PROVIDERS = {
    "openai-image": "openai-image-prompts.md",
    "midjourney": "midjourney-prompts.md",
    "jimeng": "jimeng-prompts.md",
    "seedream": "seedream-prompts.md",
    "qwen-image": "qwen-image-prompts.md",
    "minimax-image": "minimax-prompts.md",
    "comfyui": "comfyui-prompts.md",
}


def _translate(item: dict, provider_id: str) -> str:
    prompt = item["prompt"]
    negative = item.get("negative_prompt", "")
    ratio = item.get("aspect_ratio", "4:5")
    if provider_id == "midjourney":
        return f"{prompt} --ar {ratio.replace(':', ':')} --stylize 250"
    if provider_id == "jimeng":
        return f"中文可复制提示词：{item.get('localized_prompt', prompt)}\n\nEnglish prompt: {prompt}\n\n画面比例：{ratio}，影视感，细节清晰，允许合理美术补全。"
    if provider_id == "seedream":
        return f"{prompt} High-fidelity cinematic rendering, 4K detail, maintain character consistency across the set. Aspect ratio {ratio}."
    if provider_id == "comfyui":
        return f"Positive prompt: {prompt}\n\nNegative prompt: {negative}\n\nWorkflow notes: use the project's preferred checkpoint and preserve character seed/reference when available."
    if provider_id == "qwen-image":
        return f"中英混合创作提示：{item.get('localized_prompt', prompt)} / {prompt}。比例 {ratio}，保持人物与场景语义一致。"
    if provider_id == "minimax-image":
        return f"影视感创作提示：{item.get('localized_prompt', prompt)}。构图自然，细节丰富，比例 {ratio}。"
    return f"{prompt}\n\nComposition: {item.get('composition_note', 'Choose a visually effective angle consistent with the asset type.')}\nAspect ratio: {ratio}"


def _asset_section(item: dict, provider_id: str) -> str:
    return "\n".join([
        f"## {item['asset_id']}", "",
        f"- Entity ID: `{item.get('entity_id') or item.get('location_id') or 'global'}`",
        f"- Asset type: `{item['asset_type']}`",
        f"- Entity name: {item.get('entity_name', 'Global atlas asset')}",
        f"- Provider recommendation: `{provider_id}`",
        f"- Aspect ratio: `{item.get('aspect_ratio', '4:5')}`",
        f"- Style mode: `{item.get('style_mode', 'creative-balanced')}`",
        f"- Evidence summary: {item.get('evidence_summary', 'Contextual source evidence; unknown details remain inferred.')}",
        f"- Generation notes: {item.get('generation_notes', '')}",
        f"- Expected filename: `{item['expected_filename']}`",
        f"- Place generated file in: `assets/generated/{item['expected_filename']}`", "",
        "### Prompt", "", _translate(item, provider_id), "",
        "### Negative Prompt", "", item.get("negative_prompt", ""), "",
    ])


def export_prompts(output_dir: str | Path, provider_id: str | None = None) -> list[Path]:
    root = Path(output_dir).resolve()
    plan = json.loads((root / "visual-asset-plan.json").read_text(encoding="utf-8"))
    prompt_dir = root / "prompts"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    provider_ids = [provider_id] if provider_id else list(EXPORT_PROVIDERS)
    written = []
    for current in provider_ids:
        filename = EXPORT_PROVIDERS.get(current, f"{current}-prompts.md")
        path = prompt_dir / filename
        body = [f"# StoryVista Prompts: {current}", "", "Generated for external image creation. Review inferred details before use.", ""]
        body.extend(_asset_section(item, current) for item in plan["assets"])
        path.write_text("\n".join(body), encoding="utf-8")
        written.append(path)

    recommended = plan.get("selected_provider", "prompt-pack")
    pack = ["# StoryVista Prompt Pack", "", f"- Visual generation mode: `{plan.get('style_mode', 'creative-balanced')}`", f"- Recommended provider: `{recommended}`", "- Placeholder SVG files are display fallbacks, not final generated images.", ""]
    pack.extend(_asset_section(item, recommended) for item in plan["assets"])
    pack_path = root / "prompt-pack.md"
    pack_path.write_text("\n".join(pack), encoding="utf-8")
    written.append(pack_path)

    instructions = root / "manual-generation-instructions.md"
    instructions.write_text("""# External Image Generation Instructions

1. Choose a provider prompt file under `prompts/`.
2. Generate each image using its expected filename.
3. Save PNG, JPG, JPEG, or WEBP files in `assets/generated/`.
4. Run `python scripts/storyvista.py bind-images OUTPUT --assets OUTPUT/assets/generated`.
5. Run `python scripts/storyvista.py rebuild-atlas OUTPUT` if needed.

Do not upload private manuscripts to an external provider without checking its privacy terms.
""", encoding="utf-8")
    written.append(instructions)
    return written
