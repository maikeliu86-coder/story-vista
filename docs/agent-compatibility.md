# Agent Compatibility

## Status

- **CLI**: implemented and preferred in v0.2.
- **Codex Skill**: documented and preferred when installed.
- **adapter-docs**: available under `skill/agents/`.
- **adapter-runtime**: not fully implemented; framework files are integration guidance only.
- **API server**: planned for a later release.

Every supported agent can use the same portable command:

```bash
python scripts/storyvista.py build input.txt --out output/story
```

Agents with file and shell access should run the CLI and inspect `verification-report.md`. Chat-only agents can follow the six-step workflow in `skill/SKILL.md` and return JSON matching the schemas. Framework agents may wrap each phase as a tool but must preserve stable IDs, evidence statuses, and manifest binding rules.

Provider, browser, and image capabilities are optional. Without them, the output remains complete through semantic placeholders and a static HTML atlas. Platform documents must not be described as working runtime adapters unless executable integration code exists.
