# Story Interactive Archive｜故事交互档案 Skill

![Story Interactive Archive 横幅](assets/github-hero.png)

**Story Interactive Archive** 是一套 Codex skill，用来把小说、剧本、影视剧本和世界观资料，整理成可在 Obsidian 中打开、也可公开分享的交互式档案页面。

这套 skill 来自一个已经落地完成的科幻小说档案项目：人物关系树、人物索引、科技时间线、Image2 配图匹配、手机端交互、公开静态网站部署，以及实时 3D 宇宙空间关系图。

> 草稿状态：这个仓库目前只用于内部确认。未经确认前，不公开发布、不创建正式 release、不作为公开项目宣传。

## 它能帮助你做什么

- 生成 Obsidian 可打开的单页交互档案
- 制作可点击人物节点的人物关系树
- 制作带中英文名和头像的人物总览宫格
- 整理高科技、武器、特异能力与时间线
- 整理地点、星球、飞船、航线与空间关系
- 制作按故事比例压缩的实时 3D 空间图
- 将 Image2 / GPT-Image 生成图逐一匹配到人物、科技、地点或飞船
- 将本地 Obsidian 页面同步为手机可打开的公开网页

## 什么时候使用这套 Skill

当你想做以下事情时，可以调用它：

- 把一个新剧本做成交互式故事档案
- 梳理人物、派系、地点、科技和时间线
- 给每个人物或概念生成并绑定配图
- 为剧本制作人物关系树或世界地图
- 将 Obsidian 本地 HTML 同步到公开静态网站
- 将二维地点图改造成真正可旋转的 3D 空间关系图

## 本地安装

把 `skill` 文件夹复制到 Codex 的 skills 目录：

```bash
mkdir -p "$HOME/.codex/skills"
cp -R skill "$HOME/.codex/skills/story-interactive-archive"
```

之后在新的 Codex 会话中这样调用：

```text
请使用 $story-interactive-archive，把这个新剧本做成 Obsidian 中可打开、可公开分享的人物、科技与 3D 空间交互档案。
```

## 仓库结构

```text
.
├── README.md
├── README.zh-CN.md
├── assets/
│   └── github-hero.png
└── skill/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        └── implementation-notes.md
```

## 核心工作流

1. 找到源文本、Obsidian 文件、公开 HTML 副本和来源记录。
2. 先读剧本或小说，再分类人物、飞船、地点和技术。
3. 建立人物关系树、人物索引、科技时间线和空间图。
4. 将生成图或用户提供的图逐一匹配到正确实体。
5. 同时适配电脑端和手机端交互。
6. 用户要求 3D 空间时，使用真实 3D 几何，而不是二维图片卡片。
7. 本地验证渲染、手机布局、点击详情和控制台状态。
8. 同步 Obsidian、本地公开副本、来源记录和静态托管服务器。

## 已沉淀下来的设计原则

- 以文本证据为准，不为了视觉方便乱配图。
- 飞船、地点、星球不能误放进人物关系树。
- 用户要 3D 空间图时，不做“图片贴在 3D 空间里”的伪 3D。
- 当真实距离过大时，使用“压缩比例”，但保留远近层级。
- 公开分享链接要和 Obsidian 的 `file://` 本地路径区分开。
- 最终交付前必须验证页面真的可打开、可点击、可移动端使用。

## 内部确认清单

- [ ] 英文 README 表达准确。
- [ ] 中文 README 表达准确。
- [ ] GitHub 横幅配图符合项目气质。
- [ ] `skill/SKILL.md` 的触发条件清楚。
- [ ] `skill/references/implementation-notes.md` 记录的是可复用流程，不是只绑定某一本书。
- [ ] skill 能通过 `quick_validate.py` 校验。
- [ ] 未经确认前，仓库保持私有或草稿状态。

## 许可证

暂未指定公开许可证。请在确认是否公开发布前，先保持草稿或私有状态。
