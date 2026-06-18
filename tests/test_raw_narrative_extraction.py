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


class RawNarrativeExtractionTest(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
