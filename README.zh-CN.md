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

## 生成前生图环境预检

在正式生成故事视觉页面前，StoryVista 会运行或提供 Preflight Image Provider Check。这个预检不是报错，也不是责怪用户配置不对，而是帮助用户知道：当前人物图、地点图、关键事件图会由哪个 image provider 生成、规划或占位。

StoryVista 不是某一个生图模型本身。它负责故事解析、视觉资产规划、提示词生成、图片绑定和页面生成；具体图片质量取决于用户当前配置或 Auto Mode 自动选择的 image provider。

## Auto Mode：小白用户默认自动选择

StoryVista 默认使用 Auto Mode。小白用户不用手动从一长串 provider 里选择。

- 如果用户显式配置了 provider，优先使用用户配置。
- 如果用户之前选过 provider，并且现在仍可用，优先使用上次选择。
- 如果检测到一个 verified provider，自动使用它。
- 如果检测到多个 provider，StoryVista 会自动推荐一个最适合当前环境和故事视觉化需求的 provider，并说明理由。
- 如果没有检测到 provider，不中断，继续生成完整提示词、`image-manifest.json` 和语义占位图。
- 高级用户可以随时手动切换。

## 为什么要检查生图模型

StoryVista 的核心能力是故事可视化工作流，不是把用户锁死到某一个生图引擎。预检可以避免用户误以为“StoryVista 生图失败”。更准确的说法通常是：当前环境没有可直接调用的 image provider，StoryVista 会继续生成 prompt-only 或 placeholder-svg 结果。

## 当前 provider 检测

StoryVista 可以检查配置文件、环境变量、本地 ComfyUI / SD WebUI 地址、手动素材目录和已有 manifest。检测报告只显示 `detected`、`not_found`、`configured_but_unverified`、`reachable`、`unreachable` 等状态，不输出完整 API Key。

```bash
node scripts/detect-image-provider.js --json --no-network
python3 scripts/detect-image-provider.py --json --no-network
```

## 检测到多个 Provider 时

StoryVista 不会直接把一大堆选项丢给新手。它会为候选 provider 打分，自动推荐一个，并说明原因。用户可以继续使用推荐 provider，也可以查看并切换其他 provider。

## 国内推荐 Provider

国内用户优先考虑：

- 通义万相 / Qwen Image / DashScope / 阿里云百炼
- 腾讯混元生图
- MiniMax Image / 海螺相关能力
- 百度文心 / 文心一格 / 百度智能云 AI 作画
- 即梦 / 剪映生态，通常作为 prompt-only 或 manual workflow
- LiblibAI / ComfyUI 中文生态
- 本地 Stable Diffusion / FLUX / ComfyUI

这不是绝对质量排名，而是默认选择偏好。实际选择仍取决于是否检测到、是否可调用、是否验证、是否适合当前任务。

## 海外 / 可访问海外服务用户推荐 Provider

可考虑：

- OpenAI GPT Image / ChatGPT Images
- Google Gemini Image / Imagen
- Stability AI / Stable Diffusion
- Black Forest Labs FLUX
- Midjourney，常作为 prompt-only 或 manual workflow
- Leonardo AI
- Ideogram
- Replicate
- fal.ai / Together / RunPod / Modal

如果某些服务在中国大陆访问受限，建议选择国内 provider 或手动导入图片。

## 如何切换生图引擎

通过 `image-provider.config.yaml`：

```yaml
image_provider:
  mode: "api"
  provider: "qwen-image"
  model: "user-defined"
  output_folder: "assets/images"
  fallback: "placeholder-svg"
  allow_initials_avatar: false
```

也可以通过环境变量切换，例如 `OPENAI_API_KEY`、`DASHSCOPE_API_KEY`、`BFL_API_KEY`、`STABILITY_API_KEY` 等。高级用户还可以使用 manual-assets、prompt-only 或 placeholder-svg 模式。

## 为什么会看到占位图

Placeholder mode 不是失败。它表示 StoryVista 已经完成故事模型、视觉资产规划、提示词和 manifest，只是当前环境没有可直接调用的生图引擎，或者用户选择了 prompt-only / manual 工作流。

语义占位图必须包含完整实体名称和实体类型，不再默认生成简称头像。

## 切换 Provider 后重新生成视觉资产

切换 provider 后，保持 `entity_id` 和 `asset_id` 稳定，更新或重新生成 `image-manifest.json`，再重新绑定页面。这样不会破坏人物卡、地点卡、关系图、时间线和 3D 地图的图片引用。

## Prompt-Only / Manual Assets / Placeholder Mode

Prompt-only 适合 Midjourney、即梦等当前 Agent 不能直接调用的工具。Manual assets 适合用户已有剧照、截图、概念图或人物图。Placeholder mode 用于没有任何可用 provider 的情况，并且是有效继续模式。

## 页面图片来源说明

生成页面应包含低干扰说明，而不是红色报错：

> 图片资产由当前配置的 image provider 生成或规划。你可以随时切换生图引擎并重新生成视觉资产。

如果是 prompt-only 或 placeholder-svg，则使用更完整说明。这个 attribution note 不是甩锅，而是告诉用户当前图片来源和可替换性。

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
5. Show Preflight Image Provider Check
6. Run or offer Image Provider Diagnosis
7. Apply Auto Mode provider selection
8. Select api / manual-assets / prompt-only / placeholder-svg mode
9. Create visual asset plan
10. Generate image prompts and/or images
11. Create image manifest
12. Bind image assets to character cards, location cards, relationship graph, timeline, and 3D map
13. Generate final interactive atlas
14. Add subtle provider attribution note
15. Run verification checklist

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
