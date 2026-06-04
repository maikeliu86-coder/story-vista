# StoryVista｜文景

## 跨 AI Agent 的故事世界可视化 Skill

![StoryVista 横幅：手稿、剧本和小说页转化为人物图谱、时间线、场景地图和世界图谱](assets/github-hero.png)

**StoryVista｜文景** 是一个 Codex-first、cross-agent compatible 的故事世界可视化 Skill，用于把小说、剧本、长文本、世界观设定、角色资料、地点设定和时间线转化为人物关系图、地点地图、时间线、概念索引、角色卡、视觉资产库和可交互故事地图。

它不是只给 Codex 用的工具。Codex 仍然是第一支持平台，但 StoryVista 的核心能力已经与具体 Agent 解耦，也与具体生图模型解耦。

英文说明：[README.md](README.md)

## StoryVista 能生成什么

- 人物画像、人物卡、别名、角色功能、人物弧光和关系图
- 地点图、地点卡、路线图、场景地图和 3D 空间节点
- 阵营、组织、家族、门派、公司、军队等结构图
- 物件、线索、符号、母题、技术、魔法体系和抽象概念索引
- 事件时间线、剧情阶段图和关键事件画面
- `story-atlas.json`、`visual-asset-plan.json`、`image-manifest.json`
- 没有生图工具时可用的语义 SVG placeholder
- 可打开、可浏览、可复盘的交互式 HTML atlas

## 支持的输入

小说、剧本、长篇散文、角色设定、地点设定、世界观资料、跑团设定、人物小传、时间线、设定集、创作笔记、中英文混合资料。

## 支持的 Agent / 平台适配方式

StoryVista 支持多种接入模式：

- **Core Skill Mode**：OpenAI Codex 或能直接读取 `skill/SKILL.md` 的 Agent。
- **Project Instruction Mode**：Claude Code、Cursor、Windsurf、OpenCode、GitHub Copilot Agent Mode、Qwen Code、百度 Comate / 文心快码等。
- **AGENTS.md Mode**：能读取仓库根目录 `AGENTS.md` 的 coding agent。
- **Prompt-Only Mode**：不能安装 Skill 的网页聊天 Agent，直接复制核心工作流。
- **Framework Adapter Mode**：Hugging Face smolagents、LlamaIndex、LangChain、CrewAI、AutoGen、Qwen-Agent 或自定义 Python agent。
- **BYO Image Model Mode**：用户自己用生图工具生成图片，再通过 `image-manifest.json` 绑定。
- **Manual Asset Binding Mode**：用户已有剧照、截图、概念图、人物图、地点图。
- **No-Image Mode**：没有图片也能先生成完整提示词、manifest 和语义占位图。

国内用户可以用通义千问 / Qwen Code、Qwen-Agent、MiniMax、腾讯混元、腾讯云智能体开发平台、百度文心 AgentBuilder、百度 Comate / 文心快码、智谱 GLM、DeepSeek、本地大模型、OpenHands 或其他中文 coding agent 适配。详见 [skill/references/cross-agent-compatibility.md](skill/references/cross-agent-compatibility.md) 和 [skill/agents/](skill/agents/)。

## 生图模型开放适配

StoryVista 只定义“需要哪些图”和“这些图绑定到哪里”，不强制用户使用某一个生图模型。

可适配：

- OpenAI image model / ChatGPT Image
- Midjourney
- Stable Diffusion
- Flux
- ComfyUI
- MiniMax Image
- 即梦
- 通义万相 / Qwen Image
- 腾讯混元生图
- 文心一格 / Baidu Wenxin Image
- Ideogram
- Leonardo
- 本地图片文件夹
- 手动素材
- 自定义 API
- semantic placeholder SVG

没有生图工具也可以工作：StoryVista 会先输出完整 `visual-asset-plan.json`、图片提示词、`image-manifest.json` 和语义 SVG placeholder。用户之后可以用任意生图工具生成图片，再替换 manifest 里的文件路径。

## 不再默认生成简称头像

StoryVista must not use initials-only avatars as the default visual output.

默认规则：

- 每个主要人物都必须有 `character_portrait` 规划。
- 每个关键地点都必须有 `location_keyart` 规划。
- 所有图片必须通过 `image-manifest.json` 绑定。
- 没有生图模型时，也要输出完整图片提示词和语义 placeholder。
- `allow_initials_avatar` 默认是 `false`。
- 只有用户明确要求轻量占位模式，并且最后兜底失败时，才允许 initials-only placeholder。

## Codex 安装

```bash
mkdir -p "$HOME/.codex/skills"
cp -R skill "$HOME/.codex/skills/story-vista"
```

使用方式：

```text
请使用 $story-vista，把这部小说、剧本或长篇文字做成人物、关系、场景、地点、时间线、视觉资产计划和交互式故事 atlas。
```

## Claude Code / Cursor / Copilot / Windsurf / OpenCode

这些工具不一定都有原生 Skill 系统。推荐做法：

1. 让 Agent 读取根目录 `AGENTS.md`。
2. 让 Agent 读取 `skill/SKILL.md`。
3. 使用 `skill/agents/` 下对应平台的 adapter 文档。
4. 要求先生成 `visual-asset-plan.json` 和 `image-manifest.json`，再生成最终页面。

## 通义千问 / Qwen Code / MiniMax / 腾讯混元 / 百度文心

如果平台支持项目说明，就把 `AGENTS.md` 和 `skill/SKILL.md` 作为项目指令。如果平台只支持提示词，就使用 Prompt-Only Mode。如果是框架型 agent，例如 Qwen-Agent、LangChain、LlamaIndex、CrewAI，就把 `skill/templates/` 里的 schema 当成输入输出契约。

中文生图可以使用通义万相、腾讯混元生图、文心一格、即梦、MiniMax、Stable Diffusion、Flux、ComfyUI、Midjourney 或 ChatGPT Image。StoryVista 不强制任何一个。

## Bring Your Own Images

如果你已经有人物图、剧照、截图、地点图或概念图：

1. 放到 `assets/images/` 或你的项目素材目录。
2. 在 `image-manifest.json` 中登记为 `status: "user_provided"`。
3. 绑定到人物卡、关系图节点、地点卡、时间线、3D 地图和详情面板。

## 示例

- 最小小说示例：[skill/examples/minimal-novel-demo](skill/examples/minimal-novel-demo)
- 剧本示例占位：[skill/examples/screenplay-demo](skill/examples/screenplay-demo)
- 自带图片示例占位：[skill/examples/bring-your-own-images-demo](skill/examples/bring-your-own-images-demo)

## 工作流

1. Parse source text
2. Extract entities
3. Classify entities by importance
4. Build story data model
5. Create visual asset plan
6. Generate image prompts and/or images
7. Create image manifest
8. Bind image assets to character cards, location cards, relationship graph, timeline, and 3D map
9. Generate final interactive atlas
10. Run verification checklist

## Roadmap

- 更多可运行 adapter 示例
- 更多中文平台适配说明
- Provider-specific prompt translator
- HTML atlas 模板
- manifest / schema 校验工具
- 更多小说、剧本、跑团和世界观 demo

## 局限

- 长篇作品可能需要分块处理。
- 复杂别名、非线性叙事、不可靠叙述会增加识别难度。
- 生图结果需要人工复核，尤其是人物和地点匹配。
- StoryVista 不替代文学判断、编剧判断、表演选择或人类创作决策。
- 不同 Agent 平台扩展机制不同，adapter 说明的是接入方式，不保证所有平台一键安装。

## 贡献

欢迎提交 adapter、schema、demo、文档改进、真实使用场景和 bug report。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 安全和隐私

不要在公开 issue 中粘贴未发表剧本、私人手稿、NDA 材料、API key、敏感个人信息或本地文件路径。详见 [SECURITY.md](SECURITY.md)。

## 开源许可证

MIT License。详见 [LICENSE](LICENSE)。
