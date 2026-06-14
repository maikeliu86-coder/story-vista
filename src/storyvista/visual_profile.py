from __future__ import annotations


FIELDS = ("age", "build", "face", "hair", "eyes", "clothing", "accessories", "posture", "palette", "distinctive_features")


def build_visual_profile(character: dict) -> dict:
    evidence = character.get("evidence", [])
    profile = {
        "identity": {
            "value": character["canonical_name"],
            "status": "confirmed",
            "evidence": evidence[:1],
        }
    }
    for field in FIELDS:
        profile[field] = {
            "value": "unknown",
            "status": "unknown",
            "evidence": [],
        }
    profile["role_impression"] = {
        "value": character.get("role_name", "unresolved"),
        "status": "contextual" if character.get("role_name") != "unresolved" else "unknown",
        "evidence": evidence[:1],
    }
    profile["faction_impression"] = {
        "value": character.get("faction", "unresolved"),
        "status": "inferred" if character.get("faction") != "unresolved" else "unknown",
        "evidence": evidence[:1],
    }
    return profile


def attach_visual_profiles(characters: list[dict]) -> list[dict]:
    for character in characters:
        character["visual_profile"] = build_visual_profile(character)
    return characters
