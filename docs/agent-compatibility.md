# Agent Compatibility

StoryVista is compatible with agents that can read files, run shell commands, and preserve a local project workspace. Its primary contract is the Python CLI and generated file outputs, not a hidden runtime integration.

## Codex

Codex is a strong fit because it can inspect the repository, run the CLI, review generated outputs, and manage follow-up tasks such as image binding, documentation updates, and validation.

## Claude Code

Claude Code can use the same repository workflow. The recommended path is to run StoryVista through the documented commands rather than trying to create a custom runtime abstraction.

## Trae

Trae is compatible when it can operate as a repository-aware coding agent with shell access. StoryVista should be treated as a local CLI tool with structured outputs.

## Marvis

Marvis is compatible only when it can keep a project directory, read files, and execute commands. If it cannot run the CLI, it can still help draft prompts and review outputs, but the actual build must happen elsewhere.

## Cursor

Cursor is a practical host for StoryVista because it supports repository context and terminal execution. Use it the same way you would use Codex or Claude Code: build, inspect, revise, validate.

## Other Skill Or Agent Workflow Tools

Any other tool is compatible if it can:

- access the repository files
- run Python commands
- preserve output directories
- avoid inventing unsupported provider behavior

## Recommended Compatibility Mindset

- treat StoryVista as a file-based workflow
- keep image provider logic explicit
- prefer prompt export over pretending generation succeeded
- validate outputs after each meaningful build

## What Not To Claim

Do not claim native integration merely because an instruction file or adapter note exists in the repository. Real compatibility depends on the tool's filesystem access, shell access, environment management, and image capability.
