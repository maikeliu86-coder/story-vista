# StoryVista | 文景

**把故事文本变成可追溯、可交互的视觉故事图谱。**

![StoryVista Cinematic Bible Atlas](assets/docs/storyvista-overview-desktop.png)

StoryVista v0.2 已从“方法说明”升级为可运行的最小产品：使用 Python 标准库读取小说、剧本或设定文本，生成结构化数据、视觉资产计划、语义占位图、图片清单和静态交互 Atlas。

[English](README.md) · [Skill](skill/SKILL.md) · [最小演示](skill/examples/minimal-novel-demo) · [升级报告](docs/upgrade-report-v0.2.md)

## 先跑起来

```bash
python scripts/storyvista.py build skill/examples/minimal-novel-demo/input.txt --out output/minimal-novel-demo
python scripts/storyvista.py validate output/minimal-novel-demo
```

然后打开 `output/minimal-novel-demo/atlas.html`。不需要安装依赖，也不需要 API Key 或生图模型。

## 输出内容

- `source-index.json`：来源、标题、语言和文件信息
- `chunks.json`：带稳定 ID 和字符偏移的文本块
- `story-atlas.json`：人物、地点、关系、事件、Actor Mode 与证据
- `visual-asset-plan.json`：渲染前的视觉资产需求
- `image-manifest.json`：图片路径、状态、绑定和版权说明
- `assets/placeholders/*.svg`：本地语义占位图
- `atlas.html`：可搜索、可筛选、可查看证据的交互页面
- `verification-report.md`：自动验证结果

## v0.2 能做什么

- 抽取显式标注的人物、地点、组织、道具、概念、关系与事件
- 为事实、推断、歧义、矛盾和未解决内容保留不同证据状态
- 生成 Cinematic Bible 风格的静态交互 Atlas
- 提供人物卡、关系、时间线、地点、Visual Bible 和证据抽屉
- 提供 Actor Mode：场景目标、潜台词、情绪弧、可表演动作、服装道具、声音形体
- 在没有生图模型时生成带完整名称和类型的 SVG，而不是偷偷使用首字母头像

![Actor Mode](assets/docs/storyvista-actor-desktop.png)

## 当前边界

最小抽取器偏向确定性和可验证性，主要依赖可选的中文指令行；没有明确证据的内容会保持 `unresolved`。它不是一个被包装成“万能文学理解”的黑盒模型。

```text
人物：姓名｜角色｜阵营｜叙事功能
地点：名称｜类型｜氛围关键词｜视觉关键词
关系：人物A -> 人物B｜关系类型｜polarity｜0.8｜阶段
事件：事件名｜人物A、人物B｜地点｜摘要
表演：姓名｜场景目标｜秘密｜剧透信息｜潜台词｜情绪弧｜动作｜服装道具｜声音形体
```

完整示例见 [《吴越夜雨》输入文件](skill/examples/minimal-novel-demo/input.txt)。

## 生图模型是可选项

- Level 0：`placeholder-svg`，本地生成语义占位图和完整提示词
- Level 1：`manual-assets`，用户手动生成或提供图片，再写入 manifest
- Level 2：可调用 provider，由适配器读取视觉计划并生成图片

```bash
python scripts/detect_image_provider.py --no-network
```

StoryVista 可以推荐国内可访问和全球可访问的模型，但不会自动安装、注册或产生付费调用。切换方法见 [image-provider.md](skill/references/image-provider.md)。

## 验证

```bash
python -m unittest discover -s tests -v
python scripts/storyvista_validate.py output/minimal-novel-demo
```

验证覆盖文件、JSON、关系端点、证据状态、资产唯一性、manifest 绑定、占位图、主要人物肖像计划以及禁用首字母头像策略。

## 兼容性、隐私与权利

核心实现是普通文件和 Python CLI，可被 Codex、Claude Code、Cursor、Copilot、Qwen Code、MiniMax、混元、AgentBuilder、CrewAI、LangChain、LlamaIndex 和 smolagents 调用。最小流水线在本地处理文本；用户仍需确认源文本和图片的使用权，不应把机密稿件或完整密钥发送给未经授权的服务。

更多内容见 [产品愿景](docs/product-vision.md)、[数据契约](skill/references/data-contracts.md)、[权利说明](docs/legal-and-rights.md) 和 [路线图](docs/roadmap.md)。

## License

[MIT](LICENSE)
