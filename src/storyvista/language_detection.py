from __future__ import annotations

import re


SUPPORTED_UI_LANGUAGES = ("en", "zh-CN", "zh-TW", "ja", "ko", "fr", "es", "de", "ru")


def detect_language_profile(text: str, requested_ui_language: str = "auto") -> dict:
    counts = {
        "han": len(re.findall(r"[\u3400-\u9fff]", text)),
        "kana": len(re.findall(r"[\u3040-\u30ff]", text)),
        "hangul": len(re.findall(r"[\uac00-\ud7af]", text)),
        "cyrillic": len(re.findall(r"[\u0400-\u04ff]", text)),
        "arabic": len(re.findall(r"[\u0600-\u06ff]", text)),
        "hebrew": len(re.findall(r"[\u0590-\u05ff]", text)),
        "latin": len(re.findall(r"[A-Za-z]", text)),
    }
    if counts["kana"]:
        language, script, name_system = "ja", "Japanese", "east-asian"
    elif counts["hangul"]:
        language, script, name_system = "ko", "Hangul", "east-asian"
    elif counts["han"] > max(10, counts["latin"] // 3):
        language, script, name_system = "zh-CN", "Han", "chinese"
    elif counts["cyrillic"]:
        language, script, name_system = "ru", "Cyrillic", "slavic"
    elif counts["arabic"]:
        language, script, name_system = "ar", "Arabic", "arabic"
    elif counts["hebrew"]:
        language, script, name_system = "he", "Hebrew", "hebrew"
    else:
        language, script, name_system = "en", "Latin", "western"

    if requested_ui_language == "auto":
        ui_language = language if language in SUPPORTED_UI_LANGUAGES else "en"
    elif requested_ui_language in SUPPORTED_UI_LANGUAGES:
        ui_language = requested_ui_language
    else:
        raise ValueError(f"Unsupported UI language: {requested_ui_language}")

    experimental = ui_language not in {"en", "zh-CN"}
    return {
        "schema_version": "0.3.0",
        "input_language": language,
        "input_script": script,
        "writing_direction": "rtl" if language in {"ar", "he", "fa", "ur"} else "ltr",
        "ui_language": ui_language,
        "secondary_ui_languages": [value for value in ("en", "zh-CN") if value != ui_language],
        "detected_name_system": name_system,
        "detected_culture_context": "unresolved",
        "translation_mode": "preserve-canonical-with-localized-labels",
        "translation_needed": ui_language != language,
        "aliases_need_localization": ui_language != language,
        "ui_locale_status": "experimental" if experimental else "supported",
        "notes": (["UI locale is experimental and falls back to English for missing keys."] if experimental else []),
    }
