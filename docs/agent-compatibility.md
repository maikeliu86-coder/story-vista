# Agent Compatibility

StoryVista's verified interface is the local Python CLI and generated file contract. Coding agents are optional orchestration layers.

| Tool family | Usage | Status |
| --- | --- | --- |
| Codex, Claude Code, Cursor, Qwen Code, Trae | Run the documented CLI in the repository | documented; not every release/runtime tested |
| GitHub Copilot and IDE agents | Run CLI through terminal/task integration | documented |
| Mainland agent platforms | Use the same local command where shell/file access exists | environment-dependent |
| CrewAI, LangChain, LlamaIndex, smolagents | Wrap CLI or JSON outputs in custom code | integration pattern only |
| No agent | Run Python directly | verified |

Do not claim native adapters merely because an instruction file exists. Agent authentication, filesystem access, browser policy, and shell permissions vary by product and region.
