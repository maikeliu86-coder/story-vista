# StoryVista | 文景

**StoryVista｜文景，是一个面向全球读者的多语言小说视觉化阅读辅助 Skill。**

它把复杂小说中的人物、别名、关系、地点、地图、武器、科技、魔法、药剂和世界观设定整理成防剧透的游戏图鉴，并把小说原文放在同一页面的 Reader Sync Panel 中。

[English](README.md) · [Skill](skill/SKILL.md) · [完整演示](skill/examples/reader-visual-codex-demo) · [v0.4 生图工作流](docs/external-image-generation.md)

## 快速开始

```bash
python scripts/storyvista.py build skill/examples/reader-visual-codex-demo/input.txt --out output/reader-visual-codex-demo --ui-language auto
python scripts/storyvista.py validate output/reader-visual-codex-demo
```

打开 `output/reader-visual-codex-demo/atlas.html`。默认流程完全本地运行，会先生成图鉴、提示词包和语义占位图；真实图片可以在外部模型生成后绑定回来。

也可以让输入语言和 UI 语言不同：

```bash
python scripts/storyvista.py build english.txt --out output/zh-ui --ui-language zh-CN
python scripts/storyvista.py build chinese.txt --out output/en-ui --ui-language en
```

## 核心能力

- 人物画像图鉴：保留全名、姓氏、昵称、头衔、阵营、记忆标签和视觉证据状态。
- 人物关系网：展示人物和阵营关系，并对后续关系加锁。
- 小说地理地图：区分原文明确地理和解释性地图，不伪造精确距离。
- 物品与设定图鉴：支持武器、药剂、科技、魔法、神器、载具、生物和概念。
- Reader Sync Panel：右侧可收起、可拖动宽度，移动端可全屏阅读。
- 双向跳转：点击原文高亮跳到图鉴；点击图鉴证据跳回原文段落。
- 防剧透：默认隐藏标记为 `locked` 的关系和事件细节。
- 生图模型预检：只检查配置和提供建议，不自动安装、注册或付费。
- 气质主题：生成不含剧情剧透的主题色和背景提示词。
- 视觉证据：严格区分 `confirmed`、`contextual`、`inferred`、`unknown`。
- 多语言：英文和简体中文 UI 已支持，其他 locale 为实验性结构。
- 跨 Agent：任何能运行 Python 的编程智能体都可使用同一 CLI。

## 语言状态

英文与简体中文输入检测和 UI 路径已有自动测试。日文、韩文、俄文、阿拉伯文和希伯来文目前仅提供文字系统检测或实验性 locale，不声称具备完整语言理解能力。

专有名词默认保留 `canonical_name`，不会被强制翻译。需要时可补充 `localized_names`、`localized_aliases` 和 `memory_label`。

## 演示

- `reader-visual-codex-demo`：完整英文演示，含长名字、别名、蓝色发光药剂、红色声波武器和隐藏关系。
- `english-reader-demo`：英文小说片段。
- `chinese-reader-demo`：中文称谓、门派、地点和物品。
- `bilingual-demo`：英文输入、中文 UI。
- `ancient-chinese-demo`：古典文学主题。
- `futuristic-sci-fi-demo`：未来科幻主题。

## 生图模型与 fallback

StoryVista 会生成 `provider-choice-state.json`。没有可直接调用的 provider 时，它会推荐合适的生图选项并生成 `prompt-pack.md` 和各 provider 专用提示词；本地 `semantic placeholder SVG` 只是等待真实图片时的最终显示回退。第三方 provider 需要用户自行安装、配置并确认费用和隐私风险。

### 为什么我看到的是占位图？

这表示图鉴已经完成，但真实图片尚未绑定。点击页面中的“Copy prompt”，或打开 `prompt-pack.md`，在外部模型生成图片并按页面显示的文件名保存，然后执行：

```bash
python scripts/storyvista.py bind-images output/demo --assets output/demo/assets/generated
```

该命令会更新 `image-manifest.json` 并自动重建 `atlas.html`。

### 使用即梦 / Jimeng

```bash
python scripts/storyvista.py export-prompts output/demo --provider jimeng
```

打开 `output/demo/prompts/jimeng-prompts.md`，把中文提示词复制到即梦，下载后按 `Expected filename` 命名，放入 `output/demo/assets/generated/`，再运行 `bind-images`。

```bash
python scripts/storyvista.py rebuild-atlas output/demo
```

### 使用 Seedream / SeeDream

```bash
python scripts/storyvista.py export-prompts output/demo --provider seedream
```

`seedream-prompts.md` 可用于 ByteDance Seedream 或火山引擎 Seedream。API 配置与手动网页生图是两个独立入口；StoryVista 不会自动注册账号、安装服务或发起付费调用。

## 开发验证

```bash
.venv/bin/python -m pytest -q
.venv/bin/python scripts/storyvista.py validate skill/examples/reader-visual-codex-demo/expected
```

Actor、Writer、Director 工作台已从核心产品中降级，只保留为未来扩展方向。

## License

[MIT](LICENSE)
