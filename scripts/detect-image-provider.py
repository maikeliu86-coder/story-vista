#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

PROVIDERS = [
    ("openai", "api", ["OPENAI_API_KEY"], 88, ["api_key_detected", "high_storyvista_fit", "supports_character_portraits", "supports_location_keyart"], False),
    ("google", "api", ["GOOGLE_API_KEY", "GEMINI_API_KEY"], 84, ["api_key_detected", "global_provider", "supports_multimodal_generation"], False),
    ("stability", "api", ["STABILITY_API_KEY"], 78, ["api_key_detected", "stable_diffusion_ecosystem"], False),
    ("flux", "api", ["BFL_API_KEY"], 82, ["api_key_detected", "high_location_keyart_quality"], False),
    ("replicate", "api", ["REPLICATE_API_TOKEN"], 76, ["api_key_detected", "multi_model_api"], False),
    ("leonardo", "api", ["LEONARDO_API_KEY"], 72, ["api_key_detected", "concept_art_workflow"], False),
    ("ideogram", "api", ["IDEOGRAM_API_KEY"], 70, ["api_key_detected", "good_text_rendering"], False),
    ("fal", "api", ["FAL_KEY"], 74, ["api_key_detected", "developer_model_hosting"], False),
    ("together", "api", ["TOGETHER_API_KEY"], 68, ["api_key_detected", "developer_model_hosting"], False),
    ("qwen-image", "api", ["DASHSCOPE_API_KEY", "QWEN_API_KEY", "ALIBABA_CLOUD_API_KEY_ID", "ALIBABA_CLOUD_API_KEY_SECRET"], 90, ["api_key_detected", "mainland_china_friendly", "chinese_prompt_support"], False),
    ("minimax-image", "api", ["MINIMAX_API_KEY"], 80, ["api_key_detected", "mainland_china_friendly"], False),
    ("tencent-hunyuan-image", "api", ["TENCENTCLOUD_SECRET_ID", "TENCENTCLOUD_SECRET_KEY"], 82, ["api_key_detected", "mainland_china_friendly", "cloud_provider"], False),
    ("baidu-wenxin-image", "api", ["BAIDU_API_KEY", "BAIDU_SECRET_KEY"], 74, ["api_key_detected", "mainland_china_friendly"], False),
    ("zhipu-image", "api", ["ZHIPUAI_API_KEY"], 66, ["api_key_detected", "china_provider_candidate"], False),
    ("volcengine-seedream", "api", ["VOLCENGINE_ACCESS_KEY", "VOLCENGINE_SECRET_KEY"], 78, ["api_key_detected", "seedream_candidate"], False),
    ("comfyui", "api", ["COMFYUI_API_URL"], 76, ["local_endpoint_configured", "supports_custom_workflow"], True),
    ("automatic1111", "api", ["AUTOMATIC1111_API_URL", "SD_WEBUI_API_URL"], 72, ["local_endpoint_configured", "stable_diffusion_local"], True),
    ("local-image-provider", "api", ["LOCAL_IMAGE_PROVIDER_URL"], 64, ["local_endpoint_configured"], True),
]

MANUAL_ENV = ["STORYVISTA_IMAGE_ASSETS_DIR", "STORYVISTA_MANUAL_ASSETS_DIR", "STORYVISTA_IMAGE_MANIFEST_PATH"]


def mask_secret(value):
    if not value:
        return ""
    if len(value) <= 8:
        return value[:2] + "***"
    return value[:3] + "***" + value[-4:]


def read_config(config_path):
    path = Path(config_path)
    if not path.exists():
        return None
    data = {"path": str(path), "mode": None, "provider": None}
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("mode:"):
            data["mode"] = stripped.split(":", 1)[1].strip().strip("\"'")
        if stripped.startswith("provider:"):
            data["provider"] = stripped.split(":", 1)[1].strip().strip("\"'")
    return data


def endpoint_reachable(url):
    try:
        with urlopen(url, timeout=2) as response:
            return response.status < 500
    except (ValueError, URLError, TimeoutError, OSError):
        return False


def score_provider(base, reasons, signal_count, verified):
    score = base
    risk = []
    selection = list(reasons)
    if verified:
        score += 8
        selection.insert(0, "verified_api_available")
    else:
        risk.append("provider_configured_but_unverified")
    if signal_count > 1:
        score += 2
        selection.append("multiple_config_signals_detected")
    return min(100, max(0, score)), selection, risk


def main():
    parser = argparse.ArgumentParser(description="Detect StoryVista image provider configuration.")
    parser.add_argument("--json", action="store_true", help="Output JSON. JSON is the default output.")
    parser.add_argument("--verify", action="store_true", help="Verify local endpoints when network is allowed.")
    parser.add_argument("--config", default="image-provider.config.yaml", help="Path to image-provider config.")
    parser.add_argument("--no-network", action="store_true", help="Disable network checks.")
    args = parser.parse_args()

    config = read_config(args.config)
    detected = []

    for provider, mode, env_names, base, reasons, is_endpoint in PROVIDERS:
        signals = [name for name in env_names if os.environ.get(name)]
        if not signals:
            continue
        verified = False
        status = "detected"
        if is_endpoint and args.verify and not args.no_network:
            verified = endpoint_reachable(os.environ[signals[0]])
            status = "reachable" if verified else "unreachable"
        score, selection_reason, risk_reasons = score_provider(base, reasons, len(signals), verified)
        detected.append({
            "provider": provider,
            "source": "local_endpoint" if is_endpoint else "environment_variable",
            "signals": signals,
            "masked_signals": {name: mask_secret(os.environ[name]) for name in signals},
            "status": status,
            "verified": verified,
            "safe_to_use": "yes" if verified else "unknown",
            "mode": mode,
            "score": score,
            "selection_reason": selection_reason,
            "risk_reasons": risk_reasons,
            "notes": "Availability was verified." if verified else "Detected configuration, but no test call was made."
        })

    for name in MANUAL_ENV:
        value = os.environ.get(name)
        if not value:
            continue
        exists = Path(value).exists()
        detected.append({
            "provider": "manual-assets" if name == "STORYVISTA_IMAGE_MANIFEST_PATH" else "local-folder",
            "source": "existing_manifest" if name == "STORYVISTA_IMAGE_MANIFEST_PATH" else "manual_assets_dir",
            "signals": [name],
            "masked_signals": {name: value},
            "status": "detected" if exists else "configured_but_unverified",
            "verified": exists,
            "safe_to_use": "yes" if exists else "unknown",
            "mode": "manual-assets",
            "score": 70 if exists else 56,
            "selection_reason": ["manual_assets_available"] if exists else ["manual_assets_configured"],
            "risk_reasons": [] if exists else ["provider_configured_but_unverified"],
            "notes": "Manual asset path exists." if exists else "Manual asset path was configured but not found."
        })

    if config and config.get("provider") and config["provider"] != "auto":
        found = next((item for item in detected if item["provider"] == config["provider"]), None)
        if found:
            found["score"] = min(100, found["score"] + 6)
            found["selection_reason"].insert(0, "explicit_user_config")
        else:
            detected.append({
                "provider": config["provider"],
                "source": "config_file",
                "signals": [config["path"]],
                "masked_signals": {},
                "status": "configured_but_unverified",
                "verified": False,
                "safe_to_use": "unknown",
                "mode": config.get("mode") or "api",
                "score": 58,
                "selection_reason": ["explicit_user_config"],
                "risk_reasons": ["provider_configured_but_unverified"],
                "notes": "Provider was configured in image-provider config but no availability signal was detected."
            })

    detected.sort(key=lambda item: item["score"], reverse=True)
    selected = detected[0] if detected else None
    auto_selection = {
        "enabled": True,
        "selected_provider": selected["provider"] if selected else "placeholder-svg",
        "selected_mode": selected["mode"] if selected else "placeholder-svg",
        "score": selected["score"] if selected else 40,
        "selection_reason": ["highest_scoring_detected_provider"] + selected["selection_reason"] if selected else ["no_directly_callable_provider_detected", "auto_fallback"],
        "manual_override_available": True
    }

    missing = []
    for _, _, env_names, _, _, _ in PROVIDERS:
        missing.extend([name for name in env_names if not os.environ.get(name)])

    report = {
        "storyvista_image_provider_report": {
            "status": "provider_detected" if selected else "no_provider_detected",
            "config_file": config,
            "detected_providers": detected,
            "auto_selection": auto_selection,
            "missing_recommended_providers": missing[:12],
            "selected_mode": auto_selection["selected_mode"],
            "recommended_next_steps": [
                "Continue with the recommended image provider.",
                "Or configure another image provider in image-provider.config.yaml.",
                "Or continue with prompt-only mode and generate images externally."
            ] if selected else [
                "Continue with prompt-only or semantic placeholder mode.",
                "Configure an image provider later and regenerate visual assets.",
                "Provide manual images and bind them through image-manifest.json."
            ],
            "user_facing_message": (
                f"StoryVista selected {auto_selection['selected_provider']} for image asset generation or planning."
                if selected else
                "Current environment has no directly callable image provider. StoryVista will continue with prompts, image-manifest.json, and semantic placeholders."
            )
        }
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if selected else 1)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({
            "storyvista_image_provider_report": {
                "status": "detection_failed_non_blocking",
                "detected_providers": [],
                "auto_selection": {
                    "enabled": True,
                    "selected_provider": "placeholder-svg",
                    "selected_mode": "placeholder-svg",
                    "score": 40,
                    "selection_reason": ["detection_failed_non_blocking", "auto_fallback"],
                    "manual_override_available": True
                },
                "selected_mode": "placeholder-svg",
                "recommended_next_steps": ["Continue with semantic placeholders.", "Run diagnosis again later."],
                "user_facing_message": "Image provider diagnosis failed non-blocking; StoryVista can continue with semantic placeholders.",
                "error": str(exc)
            }
        }, ensure_ascii=False, indent=2))
        raise SystemExit(2)
