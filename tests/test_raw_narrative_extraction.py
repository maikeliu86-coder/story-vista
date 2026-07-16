from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


RAW_NARRATIVE_TEXT = textwrap.dedent(
    """
    # 雾桥夜信

    雨水从渡口客栈的檐角落下，林砚推开木门时，柜台后的油灯已经快灭了。苏晚正把一块青铜令牌藏进袖中，她说这东西不是陆家的货，而是青鸦帮昨夜从北仓抢来的凭证。林砚看见墙上有三道新刻的鸦形暗号，便知道巡检司的人很快会到。

    黑衣人撞开后窗，几名捕快挤进客栈。王捕头命令众人放下刀，又盯着苏晚袖口的暗纹，问她是不是替青鸦帮送信。苏晚没有回答，只把短剑横在桌边。林砚把掌柜护到柱后，听见后巷传来马蹄声，像有人故意把退路堵住。

    老者从灶房里走出来，递给林砚一封密信。信上写着雾桥码头三更换船，收信人只署了一个“陆”字。老者说陆管事早已死在北仓，今晚来买令牌的人未必是陆家。苏晚低声说，如果王捕头真的效忠巡检司，就该先查青鸦帮，而不是抓她。

    王捕头皱眉，没有立刻下令。他让捕快甲守住前门，自己跟着林砚和苏晚冲向青石后巷。黑衣人却从屋顶落下，拔刀直取老者。苏晚回身挡住一击，林砚带着密信和青铜令牌奔向雾桥码头，雨雾里只剩巡检司的铜哨声。
    """
).strip()

BOUNDARY_REGRESSION_TEXT = textwrap.dedent(
    """
    # 霜灯码头

    林岑推开渡线车站的铁门时，轨道上的冷光在水洼里抖动。她把一枚裂纹罗盘藏进风衣内袋，想起父亲林鹤失踪在第七码头。沈砚没有解释，只递给她一枚旧警徽和潮汐档案馆的地下库通行票。

    一个戴银色面罩的男人站在售票亭旁，手里转着一把没有刀刃的黑伞；另一个矮小的黑衣人擦掉屏幕上的潮汐会标记。两人穿过地下换乘层，来到旧海关楼里的潮汐档案馆。门口守着没有编号的灰衣人，城防议会封存了这里，巡城署却仍然派人暗中巡查。

    地下库里，林岑找到碎裂的蓝晶芯片、被烧掉半边的航图和一封信。白发老妇推着小车出现，说罗盘不是钥匙，而是遗嘱。远处升起蓝光，墙上的金徽章一闪而过。
    """
).strip()

VISUAL_MODIFIER_REGRESSION_TEXT = textwrap.dedent(
    """
    # 雨夜旧桥

    沈砚陪林小姐推开红色的门时，蓝色火焰从门缝里卷出来。渡口客栈里，苏晚把黑色雨伞放在桌边，王捕头的金色徽章在灯下晃了一下。黑衣人从窗边闪过，老守门人守着角落，没有人把窗边、桌面或角落当成真正的去处。

    王捕头说，京城的城防议会只是在信里提过旧码头，今晚真正出事的是渡口客栈。沈砚没有理会，他把银色罗盘递给林小姐，又让苏晚记住那座破旧木桥的位置。

    三人穿过青石后巷，只停了一息。追兵没有在后巷交手，只留下脚步声。等他们赶到旧码头，蓝色火焰再次升起，黑衣人拔刀逼近，老守门人从破旧木桥下递出一封密信。
    """
).strip()

MIXED_DIRECTIVE_NARRATIVE_TEXT = textwrap.dedent(
    """
    # 灰港密令

    人物：林砚｜调查者｜巡城署｜主角
    地点：灰港档案馆｜地下档案馆｜潮湿，昏暗｜铁架，旧卷宗｜灰港北侧

    苏晚推开渡口客栈的木门时，林砚把裂纹罗盘递给她。黑衣人撞开后窗，潮汐会的人随即封锁了旧码头。苏晚带着林砚穿过后巷，又在灰港档案馆门前交出一封密信。
    """
).strip()


class RawNarrativeExtractionTest(unittest.TestCase):
    def test_structured_directives_overlay_raw_narrative(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            input_path = tmp_path / "mixed-input.txt"
            out = tmp_path / "out"
            input_path.write_text(MIXED_DIRECTIVE_NARRATIVE_TEXT, encoding="utf-8")

            build = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "build", str(input_path), "--out", str(out), "--ui-language", "zh-CN"],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(build.returncode, 0, build.stderr)

            atlas = json.loads((out / "story-atlas.json").read_text(encoding="utf-8"))
            characters = atlas["entities"]["characters"]
            names = [item["canonical_name"] for item in characters]
            locations = {item["canonical_name"] for item in atlas["entities"]["locations"]}
            objects = {item["canonical_name"] for item in atlas["entities"]["objects"]}
            organizations = {item["canonical_name"] for item in atlas["entities"]["organizations"]}
            entity_ids = {item["entity_id"] for group in atlas["entities"].values() for item in group}

            self.assertEqual(names.count("林砚"), 1, names)
            self.assertIn("苏晚", names)
            self.assertTrue(any("黑衣人" in name for name in names), names)
            self.assertEqual(next(item for item in characters if item["canonical_name"] == "林砚")["role_name"], "调查者")
            self.assertTrue({"灰港档案馆", "渡口客栈", "旧码头"}.issubset(locations), locations)
            self.assertTrue(any("罗盘" in item for item in objects), objects)
            self.assertTrue(any("密信" in item for item in objects), objects)
            self.assertTrue({"巡城署", "潮汐会"}.issubset(organizations), organizations)
            self.assertTrue(atlas["events"])
            self.assertTrue(atlas["relations"])
            for relation in atlas["relations"]:
                self.assertIn(relation["source_entity_id"], entity_ids)
                self.assertIn(relation["target_entity_id"], entity_ids)

    def test_raw_chinese_narrative_builds_story_atlas(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            input_path = tmp_path / "raw-narrative.txt"
            out = tmp_path / "out"
            input_path.write_text(RAW_NARRATIVE_TEXT, encoding="utf-8")

            build = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "build", str(input_path), "--out", str(out), "--ui-language", "zh-CN"],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(build.returncode, 0, build.stderr)

            validate = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "validate", str(out)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(validate.returncode, 0, validate.stderr)

            atlas = json.loads((out / "story-atlas.json").read_text(encoding="utf-8"))
            plan = json.loads((out / "visual-asset-plan.json").read_text(encoding="utf-8"))
            manifest = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))
            html = (out / "atlas.html").read_text(encoding="utf-8")

            names = {item["canonical_name"] for item in atlas["entities"]["characters"]}
            locations = {item["canonical_name"] for item in atlas["entities"]["locations"]}
            objects = {item["canonical_name"] for item in atlas["entities"]["objects"]}
            organizations = {item["canonical_name"] for item in atlas["entities"]["organizations"]}

            self.assertIn("林砚", names)
            self.assertIn("苏晚", names)
            self.assertTrue(any("黑衣人" in name for name in names), names)
            self.assertTrue(any("捕快" in name for name in names), names)
            self.assertIn("渡口客栈", locations)
            self.assertIn("雾桥码头", locations)
            self.assertIn("青铜令牌", objects)
            self.assertIn("密信", objects)
            self.assertIn("青鸦帮", organizations)
            self.assertTrue(atlas["events"])
            self.assertTrue(atlas["relations"])
            self.assertTrue(plan["assets"])
            self.assertFalse(manifest["allow_initials_avatar"])
            self.assertFalse(any(asset["status"] == "placeholder" for asset in manifest["assets"]))
            self.assertIn("relationship-atlas", html)
            self.assertIn("fallback-character", html)

    def test_raw_chinese_narrative_filters_boundary_false_positives(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            input_path = tmp_path / "boundary-regression.txt"
            out = tmp_path / "out"
            input_path.write_text(BOUNDARY_REGRESSION_TEXT, encoding="utf-8")

            build = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "build", str(input_path), "--out", str(out), "--ui-language", "zh-CN"],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(build.returncode, 0, build.stderr)

            atlas = json.loads((out / "story-atlas.json").read_text(encoding="utf-8"))
            plan = json.loads((out / "visual-asset-plan.json").read_text(encoding="utf-8"))
            validate = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "validate", str(out)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(validate.returncode, 0, validate.stderr)

            names = {item["canonical_name"] for item in atlas["entities"]["characters"]}
            locations = {item["canonical_name"] for item in atlas["entities"]["locations"]}
            objects = {item["canonical_name"] for item in atlas["entities"]["objects"]}
            organizations = {item["canonical_name"] for item in atlas["entities"]["organizations"]}
            pseudo_people = {"冷光", "通道走", "解释", "车经过", "封存", "明白", "蓝光"}

            self.assertTrue({"林岑", "沈砚", "林鹤"}.issubset(names), names)
            self.assertFalse((pseudo_people | {"金徽章", "东西"}) & names, names)
            self.assertTrue(any("男人" in name for name in names), names)
            self.assertTrue(any("黑衣人" in name for name in names), names)
            self.assertTrue({"渡线车站", "第七码头", "潮汐档案馆", "地下换乘层", "地下库"}.issubset(locations), locations)
            self.assertFalse({"铁门", "门", "库门", "柜门", "是为了打开船", "潮汐会一座城"} & locations, locations)
            self.assertTrue({"潮汐会", "巡城署", "城防议会"}.issubset(organizations), organizations)
            self.assertFalse({"门", "渡线车站的铁门", "议会"} & organizations, organizations)
            self.assertTrue(any("罗盘" in item for item in objects), objects)
            self.assertTrue(any("蓝晶芯片" in item for item in objects), objects)
            self.assertTrue(any("航图" in item for item in objects), objects)
            self.assertTrue(any("信" in item for item in objects), objects)
            self.assertTrue(any("警徽" in item for item in objects), objects)
            self.assertTrue(any("黑伞" in item for item in objects), objects)
            self.assertFalse({"别相信", "整座霜灯", "座沉睡多年的灯", "刀"} & objects, objects)
            self.assertGreaterEqual(len(atlas["events"]), 3)
            for relation in atlas["relations"]:
                self.assertNotIn(relation["source_name"], pseudo_people)
                self.assertNotIn(relation["target_name"], pseudo_people)
            self.assertLess(len(plan["assets"]), 60)

    def test_visual_modifiers_survive_extraction_and_prompts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            input_path = tmp_path / "visual-modifier-regression.txt"
            out = tmp_path / "out"
            input_path.write_text(VISUAL_MODIFIER_REGRESSION_TEXT, encoding="utf-8")

            build = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "build", str(input_path), "--out", str(out), "--ui-language", "zh-CN"],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(build.returncode, 0, build.stderr)

            atlas = json.loads((out / "story-atlas.json").read_text(encoding="utf-8"))
            plan = json.loads((out / "visual-asset-plan.json").read_text(encoding="utf-8"))
            validate = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "storyvista.py"), "validate", str(out)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(validate.returncode, 0, validate.stderr)

            names = {item["canonical_name"] for item in atlas["entities"]["characters"]}
            locations = [item["canonical_name"] for item in atlas["entities"]["locations"]]
            objects = {item["canonical_name"]: item for item in atlas["entities"]["objects"]}
            prompts = "\n".join(asset["prompt"] for asset in plan["assets"])

            self.assertTrue({"沈砚", "林小姐", "王捕头", "苏晚"}.issubset(names), names)
            self.assertTrue(any("黑衣人" in name for name in names), names)
            self.assertTrue(any("老守门人" in name or "守门人" in name for name in names), names)
            self.assertFalse({"窗边", "桌面", "角落", "火焰", "徽章", "雨伞"} & names, names)

            self.assertIn("渡口客栈", locations)
            self.assertIn("旧码头", locations)
            self.assertLess(locations.index("渡口客栈"), locations.index("青石后巷"), locations)
            self.assertLess(locations.index("旧码头"), locations.index("青石后巷"), locations)
            self.assertFalse({"门", "红色的门", "窗边", "桌面", "角落"} & set(locations), locations)

            for expected in ("红色的门", "蓝色火焰", "金色徽章", "黑色雨伞", "银色罗盘", "破旧木桥"):
                self.assertIn(expected, objects, objects)
                self.assertNotEqual(objects[expected]["canonical_name"], "的门")
                self.assertTrue(objects[expected]["visual_keywords"], objects[expected])

            self.assertIn("red-painted door", prompts)
            self.assertIn("blue flame", prompts)
            self.assertIn("golden badge", prompts)
            self.assertIn("black umbrella", prompts)
            self.assertIn("silver compass", prompts)
            self.assertIn("weathered wooden bridge", prompts)
            self.assertNotIn("visual study of 的门", prompts)


if __name__ == "__main__":
    unittest.main()
