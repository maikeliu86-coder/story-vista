from __future__ import annotations

import json
import re
import shutil
from difflib import SequenceMatcher
from pathlib import Path


EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def _normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def _match(stem: str, assets: list[dict]) -> tuple[dict | None, str]:
    normalized = _normalize(stem)
    for asset in assets:
        if normalized == _normalize(asset["asset_id"]) or normalized == _normalize(Path(asset.get("expected_file_path", "")).stem):
            return asset, "exact"
    candidates = []
    for asset in assets:
        keys = [asset["asset_id"], f"{asset.get('bound_to', '')}_{asset.get('asset_type', '')}"]
        score = max(SequenceMatcher(None, normalized, _normalize(key)).ratio() for key in keys)
        candidates.append((score, asset))
    score, asset = max(candidates, default=(0, None), key=lambda item: item[0])
    return (asset, "fuzzy") if score >= 0.72 else (None, "unmatched")


def bind_images(output_dir: str | Path, assets_dir: str | Path) -> dict:
    root = Path(output_dir).resolve()
    source = Path(assets_dir).resolve()
    manifest_path = root / "image-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    target_dir = root / "assets" / "generated"
    target_dir.mkdir(parents=True, exist_ok=True)
    matched = []
    unmatched = []
    for path in sorted(source.iterdir()):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        asset, method = _match(path.stem, manifest["assets"])
        if not asset:
            unmatched.append(path.name)
            continue
        target = target_dir / f"{asset['asset_id']}{path.suffix.lower()}"
        if path != target:
            shutil.copy2(path, target)
        asset["file_path"] = str(target.relative_to(root))
        asset["provider"] = "external-manual"
        asset["status"] = "generated_external" if method == "exact" else "user_provided"
        asset["binding_method"] = method
        asset["alt_text"] = f"{asset.get('bound_to', asset['asset_id'])} {asset.get('asset_type', 'story')} visual; externally bound"
        asset["license_note"] = "External image bound by the user. Record its source, license, and generation settings before publishing."
        matched.append({"file": path.name, "asset_id": asset["asset_id"], "method": method})
    manifest["provider_status"] = "external-assets-bound" if matched else manifest.get("provider_status", "prompt-workflow-ready")
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"matched": matched, "unmatched": unmatched, "matched_count": len(matched)}
