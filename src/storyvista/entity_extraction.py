from __future__ import annotations

import re
from collections import defaultdict

from .evidence import build_evidence


LABELS = {
    "character": "characters", "人物": "characters",
    "location": "locations", "地点": "locations",
    "organization": "organizations", "组织": "organizations",
    "object": "objects", "item": "objects", "道具": "objects", "物品": "objects",
    "lore": "concepts", "concept": "concepts", "概念": "concepts", "设定": "concepts",
    "relation": "relations", "relationship": "relations", "关系": "relations",
    "event": "events", "事件": "events",
}


def _parts(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"[|｜]", value) if part.strip()]


def parse_directives(text: str) -> dict[str, list[list[str]]]:
    parsed: dict[str, list[list[str]]] = defaultdict(list)
    for line in text.splitlines():
        match = re.match(r"^\s*([^:：]+)\s*[:：]\s*(.+)$", line)
        if not match:
            continue
        key = LABELS.get(match.group(1).strip().lower()) or LABELS.get(match.group(1).strip())
        if key:
            parsed[key].append(_parts(match.group(2)))
    return parsed


def _id(prefix: str, index: int) -> str:
    return f"{prefix}_{index:03d}"


def _csv(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[,，、;/]", value) if item.strip()]


ZH_SURNAME = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜谢邹喻柏窦章云苏潘葛范彭鲁韦马苗方任袁柳史唐薛雷贺倪汤罗毕郝安常傅齐康伍余顾孟黄穆萧尹姚邵汪祁毛米贝明计成戴宋庞熊纪项祝董梁杜阮蓝季贾路江童颜郭梅盛林钟徐邱骆高夏蔡田胡凌虞万卢莫房解应宗丁宣邓洪包左石崔龚程邢裴陆荣翁荀惠曲封靳段富焦巴牧山谷车侯全秋宫宁仇祖武刘景龙叶黎白蒲鄂赖卓蔺池乔闻党谭劳姬申冉雍桑桂牛通边燕尚农温庄晏柴瞿阎充慕连习艾鱼向古易廖终居衡步耿满弘匡文寇广阙东殴沃利蔚越师巩聂晁勾冷辛简饶曾沙养须丰巢关蒯相查后荆红游竺权盖益桓公"
NAME_RE = re.compile(rf"([{ZH_SURNAME}][\u4e00-\u9fff]{{1,2}})(?=(?:说|问|道|把|向|在|从|看|听|推|走|拔|递|接|低|抬|护|挡|跟|带|命|站|坐|闯|转|皱|仍|先|却|只|没有|已经|，|。|、|：|；|！|？))")
ROLE_NAME_RE = re.compile(rf"([{ZH_SURNAME}](?:捕头|掌柜|将军|先生|姑娘|师父|大师|大人|夫人|公子|少爷|小姐|王爷|寨主|帮主|长老|校尉|统领|管事|郎中|侍卫|队长|船长))")
UNNAMED_RE = re.compile(r"(捕快甲|捕快乙|士兵甲|士兵乙|黑衣人|白衣人|灰袍人|老者|老人|老妪|老妇|少年|少女|孩子|小贩|掌柜|捕快|士兵|护卫|车夫|书生|和尚|道士|侍女|丫鬟|店小二|船夫|军官|仆人|男人|女人)(们|群)?")
LOCATION_RE = re.compile(r"([\u4e00-\u9fff]{1,8}(?:客栈|茶馆|酒楼|巡检司|码头|城门|山道|山谷|地牢|密室|书房|大殿|祠堂|城|镇|村|庄|街|巷|楼|阁|堂|殿|寺|观|庙|府|宅|院|门|山|谷|河|湖|江|桥|渡|港|关|营|站|船|舱|店|仓|井))")
OBJECT_RE = re.compile(r"([\u4e00-\u9fff]{0,6}(?:长刀|短刀|匕首|弓弩|书信|密信|药瓶|药丸|丹药|地图|卷轴|灯笼|火折子|玉佩|令牌|钥匙|铜镜|罗盘|符纸|铃铛|佩剑|木匣|账册|银票|印信|伞|刀|剑|信|药|灯))")
ORG_RE = re.compile(r"([\u4e00-\u9fff]{1,8}(?:巡检司|镖局|商会|书院|家族|门派|帮派|军营|卫所|王府|宗门|教团|军|营|司|衙|府|院|盟|阁|帮|派|门|家|族))")

NAME_STOPWORDS = {"他们", "我们", "你们", "这个", "那个", "有人", "没有", "只是", "已经", "忽然", "然后", "自己", "这里", "那里", "后窗", "后巷", "木门"}
LOCATION_STOPWORDS = {"他们", "我们", "你们", "门", "掌柜", "黑衣人", "白衣人"}
OBJECT_STOPWORDS = {"信号", "相信", "听信", "不信", "信息", "眼神", "心事", "事情"}
ORG_STOPWORDS = {"他们", "我们", "你们", "有人", "众人"}
EVENT_VERBS = ("到达", "走进", "进入", "离开", "发现", "看见", "递", "交给", "交出", "追", "追杀", "围住", "拔", "挡", "救", "护", "命令", "质问", "低声", "说", "喊", "逃", "躲", "打开", "封锁", "带着", "交付", "背叛")
NEGATIVE_VERBS = ("追", "追杀", "围", "杀", "逼", "威胁", "怀疑", "监视", "封锁")
POSITIVE_VERBS = ("救", "护", "扶", "递", "交给", "掩护", "相信")


def _has_directives(parsed: dict[str, list[list[str]]]) -> bool:
    return any(parsed.get(key) for key in ("characters", "locations", "organizations", "objects", "concepts", "relations", "events"))


def _clean_candidate(value: str, stopwords: set[str]) -> str:
    value = re.sub(r"^[在从往向于到和与的了着一只那这几数十]+", "", value.strip(" \t，。、“”‘’：:；;（）()《》[]"))
    value = re.split(r"(?:在|到|进|向|从|给|说|把|见|看|推开|递给|带着|冲向|挤进|放下|拔|送|要买|买|写着|知道|效忠|守住|剩|而是|不是|替|查|未必是)", value)[-1]
    classifier_match = re.search(r"(?:一封|一把|一柄|一块|这块|那块)(.+)", value)
    if classifier_match:
        value = classifier_match.group(1)
    value = re.sub(r"^(?:正|一封|一把|一柄|一块|这块|那块|几名|数名|众人)", "", value)
    value = re.sub(r"(?:正|已经|忽然)$", "", value)
    if not value or value in stopwords or len(value) > 12:
        return ""
    if stopwords is NAME_STOPWORDS and value[-1:] in {"窗", "巷", "信", "门", "灯", "刀", "剑", "声", "里"}:
        return ""
    if stopwords is LOCATION_STOPWORDS and any(term in value for term in ("换船", "三更", "铜哨声")):
        return ""
    if stopwords is LOCATION_STOPWORDS and value.endswith(("巡检司", "青鸦帮", "陆家")):
        return ""
    if any(mark in value for mark in ("#", "|", "｜")):
        return ""
    return value


def _evidence_from_chunk(chunk: dict, terms: list[str], status: str = "explicit") -> list[dict]:
    quote = chunk["text"].strip().replace("\n", " ")[:260]
    return [{
        "source_id": chunk["source_id"],
        "chunk_id": chunk["chunk_id"],
        "quote": quote,
        "summary": f"Source paragraph includes: {', '.join(term for term in terms if term)}",
        "confidence": "high" if status == "explicit" else "medium",
        "status": status,
    }]


def _remember(store: dict[str, dict], name: str, chunk: dict, **values: object) -> None:
    if not name:
        return
    item = store.setdefault(name, {"name": name, "chunks": [], "mentions": 0, **values})
    item["mentions"] += 1
    if chunk["chunk_id"] not in item["chunks"]:
        item["chunks"].append(chunk["chunk_id"])
    for key, value in values.items():
        if value and not item.get(key):
            item[key] = value


def _drop_contained_candidates(store: dict[str, dict]) -> dict[str, dict]:
    names = list(store)
    removable = {
        name for name in names
        if len(name) <= 4 and any(name != other and name in other for other in names)
    }
    return {name: item for name, item in store.items() if name not in removable}


def _first_chunk(chunks: list[dict], chunk_id: str | None) -> dict:
    return next((chunk for chunk in chunks if chunk["chunk_id"] == chunk_id), chunks[0])


def _raw_character_name(match: re.Match) -> tuple[str, str, list[str]]:
    if match.re is ROLE_NAME_RE:
        name = match.group(1)
        role = re.sub(rf"^[{ZH_SURNAME}]", "", name)
        return name, role, []
    value = match.group(1)
    return value, "source-observed character", []


def _extract_raw_narrative(text: str, chunks: list[dict]) -> dict:
    character_candidates: dict[str, dict] = {}
    location_candidates: dict[str, dict] = {}
    object_candidates: dict[str, dict] = {}
    org_candidates: dict[str, dict] = {}

    unnamed_counts: defaultdict[str, int] = defaultdict(int)
    unnamed_names: dict[str, str] = {}
    for chunk in chunks:
        chunk_text = chunk["text"]
        for regex in (ROLE_NAME_RE, NAME_RE):
            for match in regex.finditer(chunk_text):
                name, role, aliases = _raw_character_name(match)
                name = _clean_candidate(name, NAME_STOPWORDS)
                if name:
                    _remember(character_candidates, name, chunk, role_name=role, aliases=aliases, confidence="medium")

        for match in UNNAMED_RE.finditer(chunk_text):
            base = match.group(1)
            suffix = match.group(2) or ""
            label = f"{base}群体" if suffix or base in {"士兵", "护卫"} else base
            if label not in unnamed_names:
                unnamed_counts[label] += 1
                unnamed_names[label] = f"{label} {chr(64 + unnamed_counts[label])}"
            name = unnamed_names[label]
            _remember(character_candidates, name, chunk, role_name=label, aliases=[base], confidence="low")

        for match in LOCATION_RE.finditer(chunk_text):
            name = _clean_candidate(match.group(1), LOCATION_STOPWORDS)
            if name:
                _remember(location_candidates, name, chunk, location_type="narrative location", confidence="medium")

        for match in OBJECT_RE.finditer(chunk_text):
            name = _clean_candidate(match.group(1), OBJECT_STOPWORDS)
            if name:
                _remember(object_candidates, name, chunk, category="prop", confidence="medium")

        for match in ORG_RE.finditer(chunk_text):
            name = _clean_candidate(match.group(1), ORG_STOPWORDS)
            if name and name not in location_candidates:
                _remember(org_candidates, name, chunk, category="faction", confidence="medium")

    location_candidates = _drop_contained_candidates(location_candidates)
    object_candidates = _drop_contained_candidates(object_candidates)
    for org_name in org_candidates:
        location_candidates.pop(org_name, None)

    characters = []
    name_to_id: dict[str, str] = {}
    for index, item in enumerate(character_candidates.values(), 1):
        chunk = _first_chunk(chunks, item["chunks"][0] if item["chunks"] else None)
        entity_id = _id("char", index)
        name_to_id[item["name"].casefold()] = entity_id
        for alias in item.get("aliases", []):
            name_to_id[alias.casefold()] = entity_id
        characters.append({
            "entity_id": entity_id, "entity_type": "character",
            "canonical_name": item["name"], "name": item["name"], "localized_names": {}, "localized_aliases": {},
            "aliases": item.get("aliases", []),
            "memory_label": item.get("role_name", "source-observed character"),
            "role_name": item.get("role_name", "source-observed character"),
            "faction": "unresolved",
            "narrative_function": "inferred from raw narrative",
            "importance": "major" if index <= 5 else "supporting",
            "confidence": item.get("confidence", "medium"),
            "first_seen": chunk["chunk_id"],
            "evidence": _evidence_from_chunk(chunk, [item["name"]], "inferred" if item.get("confidence") == "low" else "explicit"),
        })

    locations = []
    location_to_id: dict[str, str] = {}
    for index, item in enumerate(location_candidates.values(), 1):
        chunk = _first_chunk(chunks, item["chunks"][0] if item["chunks"] else None)
        entity_id = _id("loc", index)
        location_to_id[item["name"]] = entity_id
        locations.append({
            "entity_id": entity_id, "entity_type": "location",
            "canonical_name": item["name"], "name": item["name"], "localized_names": {},
            "location_type": item.get("location_type", "narrative location"),
            "mood": ["source-derived"],
            "visual_keywords": [item["name"]],
            "spatial_notes": "Mentioned in raw narrative; exact geography remains unresolved.",
            "confidence": item.get("confidence", "medium"),
            "evidence": _evidence_from_chunk(chunk, [item["name"]]),
        })

    groups = {"organizations": [], "objects": [], "concepts": []}
    for key, store, prefix, entity_type in (
        ("organizations", org_candidates, "org", "organization"),
        ("objects", object_candidates, "obj", "object"),
    ):
        for index, item in enumerate(store.values(), 1):
            chunk = _first_chunk(chunks, item["chunks"][0] if item["chunks"] else None)
            groups[key].append({
                "entity_id": _id(prefix, index), "entity_type": entity_type,
                "canonical_name": item["name"], "name": item["name"], "localized_names": {},
                "category": item.get("category", entity_type),
                "description": "Extracted from raw narrative context; details are evidence-limited.",
                "visual_keywords": [item["name"]],
                "confidence": item.get("confidence", "medium"),
                "evidence": _evidence_from_chunk(chunk, [item["name"]]),
            })

    events = []
    for chunk in chunks:
        if not any(verb in chunk["text"] for verb in EVENT_VERBS):
            continue
        participants = [character["entity_id"] for character in characters if character["canonical_name"] in chunk["text"] or any(alias in chunk["text"] for alias in character.get("aliases", []))]
        location_id = next((location["entity_id"] for location in locations if location["canonical_name"] in chunk["text"]), None)
        title = re.split(r"[。！？!?]", chunk["text"].strip())[0][:28] or f"Raw narrative event {len(events) + 1}"
        events.append({
            "event_id": _id("evt", len(events) + 1), "title": title,
            "participants": participants[:6],
            "location_id": location_id,
            "summary": chunk["summary"],
            "timeline_order": len(events) + 1,
            "spoiler_status": "visible",
            "status": "explicit",
            "confidence": "medium",
            "evidence": _evidence_from_chunk(chunk, [title]),
        })
        if len(events) >= 8:
            break

    relations = []
    seen_relations: set[tuple[str | None, str | None, str]] = set()
    for chunk in chunks:
        chars_here = [character for character in characters if character["canonical_name"] in chunk["text"] or any(alias in chunk["text"] for alias in character.get("aliases", []))]
        if len(chars_here) < 2:
            continue
        relation_type = "同场互动"
        polarity = "neutral"
        if any(verb in chunk["text"] for verb in NEGATIVE_VERBS):
            relation_type, polarity = "冲突 / 追捕 / 怀疑", "negative"
        elif any(verb in chunk["text"] for verb in POSITIVE_VERBS):
            relation_type, polarity = "协助 / 保护 / 交付", "positive"
        for source, target in zip(chars_here, chars_here[1:]):
            key = (source["entity_id"], target["entity_id"], relation_type)
            if key in seen_relations:
                continue
            seen_relations.add(key)
            relations.append({
                "relation_id": _id("rel", len(relations) + 1),
                "source_entity_id": source["entity_id"],
                "target_entity_id": target["entity_id"],
                "source_name": source["canonical_name"], "target_name": target["canonical_name"],
                "relation_type": relation_type,
                "polarity": polarity,
                "strength": 0.65 if polarity != "neutral" else 0.45,
                "stage": "current",
                "spoiler_status": "visible",
                "status": "inferred",
                "confidence": "medium",
                "evidence": _evidence_from_chunk(chunk, [source["canonical_name"], target["canonical_name"]], "inferred"),
            })
        if len(relations) >= 8:
            break

    return {"characters": characters, "locations": locations, **groups, "relations": relations, "events": events}


def extract_story_entities(text: str, chunks_doc: dict) -> dict:
    parsed = parse_directives(text)
    chunks = chunks_doc["chunks"]
    if not _has_directives(parsed):
        return _extract_raw_narrative(text, chunks)

    characters = []
    for index, row in enumerate(parsed["characters"], 1):
        name = row[0]
        aliases = _csv(row[4]) if len(row) > 4 else []
        characters.append({
            "entity_id": _id("char", index), "entity_type": "character",
            "canonical_name": name, "name": name, "localized_names": {}, "localized_aliases": {},
            "aliases": aliases, "memory_label": row[5] if len(row) > 5 else (row[1] if len(row) > 1 else name),
            "role_name": row[1] if len(row) > 1 else "unresolved",
            "faction": row[2] if len(row) > 2 else "unresolved",
            "narrative_function": row[3] if len(row) > 3 else "unresolved",
            "importance": "major" if index <= 5 else "supporting",
            "evidence": build_evidence(chunks, [name]),
        })

    name_to_id = {}
    for character in characters:
        for value in [character["canonical_name"], *character["aliases"]]:
            name_to_id[value.casefold()] = character["entity_id"]

    locations = []
    for index, row in enumerate(parsed["locations"], 1):
        name = row[0]
        locations.append({
            "entity_id": _id("loc", index), "entity_type": "location",
            "canonical_name": name, "name": name, "localized_names": {},
            "location_type": row[1] if len(row) > 1 else "unresolved",
            "mood": _csv(row[2]) if len(row) > 2 else [],
            "visual_keywords": _csv(row[3]) if len(row) > 3 else [],
            "spatial_notes": row[4] if len(row) > 4 else "unresolved",
            "evidence": build_evidence(chunks, [name]),
        })

    groups = {}
    for key, prefix, entity_type in (("organizations", "org", "organization"), ("objects", "obj", "object"), ("concepts", "lore", "lore")):
        values = []
        for index, row in enumerate(parsed[key], 1):
            name = row[0]
            values.append({
                "entity_id": _id(prefix, index), "entity_type": entity_type,
                "canonical_name": name, "name": name, "localized_names": {},
                "category": row[1] if len(row) > 1 else entity_type,
                "description": row[2] if len(row) > 2 else (row[1] if len(row) > 1 else "unresolved"),
                "visual_keywords": _csv(row[3]) if len(row) > 3 else [],
                "evidence": build_evidence(chunks, [name]),
            })
        groups[key] = values

    relations = []
    for index, row in enumerate(parsed["relations"], 1):
        pair = re.split(r"\s*(?:->|→)\s*", row[0])
        source, target = (pair + [""])[:2]
        evidence = build_evidence(chunks, [source, target])
        spoiler = row[5].lower() if len(row) > 5 else "visible"
        relations.append({
            "relation_id": _id("rel", index),
            "source_entity_id": name_to_id.get(source.casefold()),
            "target_entity_id": name_to_id.get(target.casefold()),
            "source_name": source, "target_name": target,
            "relation_type": row[1] if len(row) > 1 else "unresolved",
            "polarity": row[2] if len(row) > 2 else "neutral",
            "strength": float(row[3]) if len(row) > 3 and re.fullmatch(r"\d+(?:\.\d+)?", row[3]) else 0.5,
            "stage": row[4] if len(row) > 4 else "current",
            "spoiler_status": "locked" if "lock" in spoiler or "隐藏" in spoiler else "visible",
            "status": "explicit" if evidence else "unresolved", "evidence": evidence,
        })

    events = []
    location_ids = {item["canonical_name"]: item["entity_id"] for item in locations}
    for index, row in enumerate(parsed["events"], 1):
        participants = _csv(row[1]) if len(row) > 1 else []
        events.append({
            "event_id": _id("evt", index), "title": row[0],
            "participants": [name_to_id[name.casefold()] for name in participants if name.casefold() in name_to_id],
            "location_id": location_ids.get(row[2]) if len(row) > 2 else None,
            "summary": row[3] if len(row) > 3 else row[0], "timeline_order": index,
            "spoiler_status": "locked" if len(row) > 4 and ("lock" in row[4].lower() or "隐藏" in row[4]) else "visible",
            "evidence": build_evidence(chunks, [row[0]]) or build_evidence(chunks, participants[:1]),
        })
    return {"characters": characters, "locations": locations, **groups, "relations": relations, "events": events}
