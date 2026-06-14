from __future__ import annotations


def build_theme_profile(text: str) -> dict:
    lower = text.lower()
    if any(term in text for term in ("竹林", "古道", "青瓦", "江湖", "朝堂")):
        theme = "ancient-chinese-literary"
        palette = ["#101512", "#d9d6c8", "#71806b", "#8e3e32", "#b59b62"]
        motifs = ["bamboo forest", "ink wash", "xuan paper", "mountain water landscape"]
    elif any(term in lower for term in ("starship", "space station", "holographic", "colony planet", "星舰", "空间站", "全息", "殖民星")):
        theme = "futuristic-sci-fi"
        palette = ["#070b12", "#d9edf2", "#55a7b7", "#d24d4d", "#667085"]
        motifs = ["deep space", "starship", "holographic interface", "cool light"]
    else:
        theme = "literary-archive"
        palette = ["#111315", "#e3ded3", "#b89456", "#6f8792", "#9a5550"]
        motifs = ["archival paper", "quiet library", "annotated map", "restrained cinematic light"]
    return {
        "schema_version": "0.3.0", "theme_id": theme, "confidence": "contextual",
        "palette": palette, "motifs": motifs,
        "background_prompt": f"Spoiler-free atmospheric reading background, {', '.join(motifs)}, no characters, no text, no plot events.",
        "background_enabled": True,
    }
