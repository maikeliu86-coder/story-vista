from __future__ import annotations

import json
import re
import uuid
from pathlib import Path

from .output_lock import output_lock


EXPORT_PROVIDERS = {
    "openai-image": "openai-image-prompts.md",
    "midjourney": "midjourney-prompts.md",
    "jimeng": "jimeng-prompts.md",
    "seedream": "seedream-prompts.md",
    "qwen-image": "qwen-image-prompts.md",
    "minimax-image": "minimax-prompts.md",
    "comfyui": "comfyui-prompts.md",
}
SAFE_PROVIDER_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
INSTRUCTIONS = """# External Image Generation Instructions

1. Choose a provider prompt file under `prompts/`.
2. Generate each image using its expected filename.
3. Save PNG, JPG, JPEG, or WEBP files in `assets/generated/`.
4. Run `python scripts/storyvista.py bind-images OUTPUT --assets OUTPUT/assets/generated`.
5. Run `python scripts/storyvista.py rebuild-atlas OUTPUT` if needed.

Do not upload private manuscripts to an external provider without checking its privacy terms.
"""


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


def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)


def _remove_file(path: Path) -> None:
    try:
        path.unlink()
    except FileNotFoundError:
        pass


def _publish_prompt_files(files: list[tuple[Path, str]]) -> list[Path]:
    token = uuid.uuid4().hex
    staged: list[tuple[Path, Path]] = []
    backups: list[tuple[Path, Path]] = []
    published: list[Path] = []
    created_dirs: list[Path] = []
    for target, _content in files:
        if target.exists() and not target.is_file():
            raise IsADirectoryError(f"Prompt output path is not a file: {target}")
    try:
        for target, content in files:
            if not target.parent.exists():
                target.parent.mkdir(parents=True)
                created_dirs.append(target.parent)
            temporary = target.parent / f".{target.name}.storyvista-prompt-{token}.tmp"
            temporary.write_text(content, encoding="utf-8")
            staged.append((target, temporary))

        for target, _temporary in staged:
            if target.exists():
                backup = target.parent / f".{target.name}.storyvista-prompt-{token}.bak"
                _replace_file(target, backup)
                backups.append((target, backup))
        for target, temporary in staged:
            _replace_file(temporary, target)
            published.append(target)
    except BaseException:
        for target in published:
            _remove_file(target)
        for target, backup in reversed(backups):
            if backup.exists():
                _replace_file(backup, target)
        raise
    finally:
        for _target, temporary in staged:
            _remove_file(temporary)
        for target, backup in backups:
            if target.exists():
                _remove_file(backup)
        for directory in reversed(created_dirs):
            try:
                directory.rmdir()
            except OSError:
                pass
    return [target for target, _content in files]


def _export_prompts_in_place(root: Path, provider_id: str | None = None) -> list[Path]:
    plan = json.loads((root / "visual-asset-plan.json").read_text(encoding="utf-8"))
    provider_ids = [provider_id] if provider_id else list(EXPORT_PROVIDERS)
    for current in provider_ids:
        if not SAFE_PROVIDER_ID.fullmatch(current):
            raise ValueError(f"Unsafe provider id: {current!r}")

    prompt_dir = root / "prompts"
    files: list[tuple[Path, str]] = []
    for current in provider_ids:
        filename = EXPORT_PROVIDERS.get(current, f"{current}-prompts.md")
        path = (prompt_dir / filename).resolve()
        try:
            path.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"Provider prompt path escapes output directory: {path}") from exc
        body = [f"# StoryVista Prompts: {current}", "", "Generated for external image creation. Review inferred details before use.", ""]
        body.extend(_asset_section(item, current) for item in plan["assets"])
        files.append((path, "\n".join(body)))

    recommended = plan.get("selected_provider", "prompt-pack")
    pack = ["# StoryVista Prompt Pack", "", f"- Visual generation mode: `{plan.get('style_mode', 'creative-balanced')}`", f"- Recommended provider: `{recommended}`", "- Placeholder SVG files are display fallbacks, not final generated images.", ""]
    pack.extend(_asset_section(item, recommended) for item in plan["assets"])
    pack_path = root / "prompt-pack.md"
    instructions = root / "manual-generation-instructions.md"
    files.extend([(pack_path, "\n".join(pack)), (instructions, INSTRUCTIONS)])
    return _publish_prompt_files(files)


def export_prompts(output_dir: str | Path, provider_id: str | None = None) -> list[Path]:
    root = Path(output_dir).resolve()
    with output_lock(root, "export-prompts"):
        return _export_prompts_in_place(root, provider_id)
