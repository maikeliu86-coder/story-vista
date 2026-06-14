from __future__ import annotations

import os

from .providers.registry import PROVIDER_REGISTRY


def _configured(provider: dict) -> tuple[bool, list[str]]:
    signals = [name for name in provider.get("env_vars", []) if os.environ.get(name)]
    return bool(signals), signals


def build_provider_choice_state(input_language: str = "en") -> dict:
    available = []
    prompt_only = []
    manual_web = []
    direct_api = []
    local_api = []
    detected = []

    for item in PROVIDER_REGISTRY:
        provider = dict(item)
        configured, signals = _configured(provider)
        provider_type = provider["provider_type"]
        if configured:
            state = "configured"
            detected.append({
                "provider_id": provider["provider_id"], "status": "detected-but-unverified",
                "signals": signals, "verified": False,
            })
        elif provider_type == "prompt-only":
            state = "prompt-only"
        elif provider_type == "manual-web":
            state = "manual-web"
        elif provider_type == "manual-assets":
            state = "manual-assets"
        elif provider_type == "fallback":
            state = "fallback"
        else:
            state = "unavailable"
        summary = {"provider_id": provider["provider_id"], "display_name": provider["display_name"], "status": state}
        if state in {"configured", "prompt-only", "manual-web", "manual-assets"}:
            available.append(summary)
        if provider_type == "prompt-only":
            prompt_only.append(summary)
        elif provider_type == "manual-web":
            manual_web.append(summary)
        elif provider_type in {"direct-api", "custom-api", "agent-native"}:
            direct_api.append(summary)
        elif provider_type == "local-api":
            local_api.append(summary)

    configured_direct = [item for item in [*direct_api, *local_api] if item["status"] == "configured"]
    recommended = configured_direct[0]["provider_id"] if configured_direct else ("jimeng" if input_language.startswith("zh") else "openai-image")
    if len(configured_direct) == 1:
        reason = "One direct or local provider configuration was detected, but it remains unverified until a real adapter check succeeds."
    elif len(configured_direct) > 1:
        reason = "Multiple provider configurations were detected. The first registry-ranked configured provider is recommended; manual override remains available."
    else:
        reason = "No verified direct image provider is available. Prompt packs and manual binding are ready; semantic SVG remains the display fallback."
    return {
        "schema_version": "0.4.0",
        "mode": "auto",
        "status": "configured-unverified" if configured_direct else "prompt-workflow-ready",
        "available_providers": available,
        "detected_providers": detected,
        "prompt_only_providers": prompt_only,
        "manual_web_providers": manual_web,
        "direct_api_providers": direct_api,
        "local_api_providers": local_api,
        "recommended_provider": recommended,
        "selected_provider": recommended,
        "fallback_provider": "placeholder-svg",
        "reason": reason,
        "warnings": ["Configuration detection is not runtime verification."] + ([] if configured_direct else ["No direct generation adapter was verified."]),
        "next_actions": [
            "Review prompt-pack.md or export a provider-specific prompt file.",
            "Generate images externally or configure a supported adapter.",
            "Save files in assets/generated using the expected filenames.",
            "Run storyvista.py bind-images, then rebuild-atlas.",
        ],
        "prompt_only": not bool(configured_direct),
        "installation_policy": "recommend-only; never auto-install or create paid accounts",
    }
