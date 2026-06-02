# StoryVista｜文景

![StoryVista 横幅](assets/github-hero.png)

**StoryVista｜文景** 帮助人们让文字世界看得见。

把小说、剧本、长篇文字和世界观设定，转换成人物关系、场景地图、时间线、概念卡片与 3D 世界图谱。

英文标语：**Make Text Worlds Visible**  
中文标语：**让文字世界看得见**

> 草稿状态：这个仓库目前只用于内部确认。未经确认前，不公开发布、不创建正式 release、不作为公开项目宣传。

## 读一个故事，不应该像丢了一张地图

长篇小说和剧本常常把结构藏在人名、地点、场景和伏笔里。StoryVista 把这些隐藏结构变成可以看的图谱。

![阅读痛点总览](assets/pain-points-overview.png)

## 四种常见阅读痛点

|  |  |
| --- | --- |
| ![人物名字混乱](assets/pain-name-overload.png)<br><br>**人物名字混乱**<br>人物、别名、译名、头衔和昵称太多，读到后面很容易分不清谁是谁。<br><br>**Name Overload**<br>Too many characters, aliases, translations, titles, and nicknames make it hard to remember who is who. | ![人物关系混乱](assets/pain-relationship-confusion.png)<br><br>**人物关系混乱**<br>同盟、敌对、亲属、导师、竞争者和隐藏身份不断变化，关系线越读越乱。<br><br>**Relationship Confusion**<br>Allies, enemies, families, mentors, rivals, and hidden identities shift across the story. |
| ![地点描述混乱](assets/pain-place-disorientation.png)<br><br>**地点描述混乱**<br>故事在城市、房间、星球、王国或时代之间跳转，读者还没形成地图，场景已经切走。<br><br>**Place Disorientation**<br>Scenes move between cities, rooms, planets, kingdoms, or timelines before the reader forms a mental map. | ![空间关系混乱](assets/pain-spatial-uncertainty.png)<br><br>**空间关系混乱**<br>路线、距离、世界、飞船、战场或幻想地理只存在于文字里，很难形成直观空间感。<br><br>**Spatial Uncertainty**<br>Routes, distances, worlds, ships, battlefields, or fantasy realms are described in text but hard to visualize. |

## 从文字到可探索的故事图谱

StoryVista 将叙事材料变成可浏览、可点击、可回看的结构，帮助读者和创作者快速重新进入故事。

- **Character Graphs｜人物关系图**  
  梳理人物姓名、别名、身份、派系与不断变化的关系。

- **Scene & Location Maps｜场景与地点地图**  
  连接房间、城市、星球、王国、路线和反复出现的地点。

- **Timelines & Concepts｜时间线与概念卡片**  
  跟踪剧情事件、科技、能力、母题、物件和伏笔。

- **3D World Maps｜3D 世界图谱**  
  当距离、地理、移动和空间关系重要时，建立可交互的 3D 视图。

![StoryVista 工作流](assets/storyvista-workflow.png)

## 为所有需要理解故事结构的人而做

- 想理清复杂故事的读者
- 想检查故事结构的作者
- 管理人物和场景的编剧
- 分析文学作品的学生和老师
- 管理地点、派系和设定的世界观创作者
- 将叙事材料转成知识图谱的研究者

## 它能帮助你做什么

- 制作可点击的人物关系树
- 生成人物或角色索引、头像和简介
- 整理场景、地点、物件、派系和世界地图
- 整理剧情、科技、能力、符号或母题时间线
- 用 Image2 / GPT-Image 为人物、地点和概念生成对应配图
- 将配图逐一匹配到正确的人物、场景或设定
- 制作适合手机浏览的交互档案页面
- 将 Obsidian 本地页面同步为公开可分享的静态网页
- 为有空间关系的故事制作实时 3D 地图

## 本地安装

把 `skill` 文件夹复制到 Codex 的 skills 目录：

```bash
mkdir -p "$HOME/.codex/skills"
cp -R skill "$HOME/.codex/skills/story-vista"
```

之后在新的 Codex 会话中这样调用：

```text
请使用 $story-vista，把这部小说、剧本或长篇文字做成人物、场景、时间线、概念和世界地图的交互式视觉档案。
```

## 仓库结构

```text
.
├── README.md
├── README.zh-CN.md
├── assets/
│   ├── github-hero.png
│   ├── pain-points-overview.png
│   ├── pain-name-overload.png
│   ├── pain-relationship-confusion.png
│   ├── pain-place-disorientation.png
│   ├── pain-spatial-uncertainty.png
│   └── storyvista-workflow.png
└── skill/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        └── implementation-notes.md
```

## 核心工作流

1. 找到源文本、笔记、Obsidian 文件、公开 HTML 副本和来源记录。
2. 先读文本，再分类人物、地点、物件、科技、派系和时间线。
3. 围绕读者真正关心的问题建结构：谁、在哪、何时、发生了什么、为什么重要。
4. 将生成图或用户提供的图逐一匹配到正确实体。
5. 同时适配电脑端和手机端交互。
6. 当空间关系重要时，使用真实 3D 几何，而不是二维图片卡片。
7. 本地验证渲染、手机布局、点击详情和控制台状态。
8. 按需同步 Obsidian、本地公开副本、来源记录和静态托管服务器。

## 设计原则

- 以文本证据为准，不为了视觉好看乱编关系。
- 飞船、城市、物件、组织不能误放进人物关系树。
- 用户要 3D 空间图时，不做“图片贴在 3D 空间里”的伪 3D。
- 当真实距离过大时，使用“压缩比例”，但保留远近层级。
- 公开分享链接要和 Obsidian 的 `file://` 本地路径区分开。
- 最终交付前必须验证页面真的可打开、可点击、可移动端使用。

## 内部确认清单

- [ ] 痛点区对不同文化背景的用户都清楚。
- [ ] 英文 README 首屏能说明这个 skill 的用途。
- [ ] 中文 README 面向读者、作者、编剧和世界观创作者。
- [ ] 新图片适合 GitHub 详情页。
- [ ] `skill/SKILL.md` 的触发条件清楚。
- [ ] `skill/references/implementation-notes.md` 记录的是可复用流程。
- [ ] skill 能通过 `quick_validate.py` 校验。
- [ ] 未经确认前，不推送 GitHub。

## 许可证

暂未指定公开许可证。请在确认是否公开发布前，先保持草稿或私有状态。
