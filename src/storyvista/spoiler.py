from __future__ import annotations

from copy import deepcopy
import re


LOCKABLE_DIRECTIVE_RE = re.compile(
    r"^(?P<indent>\s*)(?P<label>relation|relationship|关系|event|事件)\s*[:：]\s*(?P<value>.*?)(?P<newline>\r?\n)?$",
    re.IGNORECASE,
)


def _is_locked_marker(value: str) -> bool:
    normalized = value.strip().casefold()
    return "lock" in normalized or "隐藏" in normalized


def redact_locked_directives(text: str, mode: str = "safe") -> str:
    if mode == "full":
        return text
    if mode != "safe":
        raise ValueError(f"Unsupported spoiler mode: {mode}")

    redacted = []
    for line in text.splitlines(keepends=True):
        match = LOCKABLE_DIRECTIVE_RE.match(line)
        parts = re.split(r"[|｜]", match.group("value")) if match else []
        if not match or not parts or not _is_locked_marker(parts[-1]):
            redacted.append(line)
            continue
        newline = match.group("newline") or ""
        body = line[:-len(newline)] if newline else line
        placeholder = f"{match.group('indent')}{match.group('label')}: [locked until full mode] | locked"
        redacted.append((placeholder[:len(body)].ljust(len(body)) + newline))
    return "".join(redacted)


def _spoiler_safe_evidence(payload: dict, chunks: list[dict]) -> dict:
    safe = deepcopy(payload)
    chunk_text = {item["chunk_id"]: item["text"].strip().replace("\n", " ")[:260] for item in chunks}
    for group in ("characters", "locations", "organizations", "objects", "concepts", "relations", "events"):
        for item in safe.get(group, []):
            for evidence in item.get("evidence", []):
                replacement = chunk_text.get(evidence.get("chunk_id"))
                if replacement:
                    evidence["quote"] = replacement
                    evidence["summary"] = "Source evidence retained from the spoiler-safe text view."
    return safe


def apply_spoiler_mode(extracted: dict, chunks: list[dict], mode: str = "safe") -> dict:
    if mode == "full":
        return deepcopy(extracted)
    if mode != "safe":
        raise ValueError(f"Unsupported spoiler mode: {mode}")
    safe = _spoiler_safe_evidence(extracted, chunks)
    safe["relations"] = [item for item in safe.get("relations", []) if item.get("spoiler_status") != "locked"]
    safe["events"] = [item for item in safe.get("events", []) if item.get("spoiler_status") != "locked"]
    return safe


def build_spoiler_state(relations: list[dict], events: list[dict], mode: str = "safe") -> dict:
    if mode not in {"safe", "full"}:
        raise ValueError(f"Unsupported spoiler mode: {mode}")
    locked = [item["relation_id"] for item in relations if item.get("spoiler_status") == "locked"]
    locked += [item["event_id"] for item in events if item.get("spoiler_status") == "locked"]
    return {
        "schema_version": "0.3.0", "mode": mode, "enabled": mode != "full",
        "progress": {"type": "uploaded-fragment", "value": "current"},
        "locked_item_ids": locked if mode != "full" else [],
        "reveal_policy": "hide-locked-details" if mode != "full" else "show-all",
    }
