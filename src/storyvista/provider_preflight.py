from __future__ import annotations

import os


PROVIDERS = {
    "openai": ("OPENAI_API_KEY", "global"),
    "fal": ("FAL_KEY", "global"),
    "qwen": ("DASHSCOPE_API_KEY", "mainland-and-global"),
    "minimax": ("MINIMAX_API_KEY", "mainland-and-global"),
}


def build_provider_choice_state() -> dict:
    detected = []
    for name, (variable, region) in PROVIDERS.items():
        if os.environ.get(variable):
            detected.append({"provider": name, "signal": variable, "region": region, "verified": False})
    selected = detected[0]["provider"] if len(detected) == 1 else "placeholder-svg"
    return {
        "schema_version": "0.3.0", "mode": "auto", "detected_providers": detected,
        "selected_provider": selected, "fallback_provider": "placeholder-svg",
        "prompt_only": False, "status": "fallback-selected" if selected == "placeholder-svg" else "configuration-detected",
        "selection_reason": "No callable provider was verified; local semantic placeholders keep the build complete." if selected == "placeholder-svg" else "One configured provider signal was detected; runtime verification is still required.",
        "installation_policy": "recommend-only; never auto-install or create paid accounts",
    }
