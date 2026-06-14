from __future__ import annotations

import re


TITLE_RE = re.compile(r"^(?:Mr\.?|Mrs\.?|Miss|Ms\.?|Dr\.?|Professor|Prof\.?|Captain|Capt\.?|Lord|Lady|Sir|Dame)\s+", re.I)


def resolve_aliases(characters: list[dict], language_profile: dict) -> tuple[list[dict], list[dict]]:
    name_system = language_profile["detected_name_system"]
    index: dict[str, str] = {}
    ambiguous = []
    for character in characters:
        canonical = character["canonical_name"]
        candidates = [canonical, *character.get("aliases", [])]
        if name_system == "western":
            stripped = TITLE_RE.sub("", canonical).strip()
            parts = stripped.split()
            if stripped != canonical:
                candidates.append(stripped)
            if len(parts) > 1:
                candidates.append(parts[-1])
        elif name_system == "chinese" and len(canonical) >= 3:
            candidates.extend([canonical[-2:]])

        unique = []
        for alias in candidates:
            alias = alias.strip()
            if not alias or alias in unique:
                continue
            owner = index.get(alias.casefold())
            if owner and owner != character["entity_id"]:
                ambiguous.append({"alias": alias, "candidate_entity_ids": [owner, character["entity_id"]]})
                continue
            index[alias.casefold()] = character["entity_id"]
            unique.append(alias)
        character["aliases"] = unique[1:]
        character["alias_resolution"] = {"rule_set": name_system, "status": "resolved"}
    return characters, ambiguous
