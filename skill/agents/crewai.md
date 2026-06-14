# CrewAI Adapter

Invocation: wrap the six pipeline phases as bounded tasks and use the JSON Schemas as handoff contracts.

Capabilities: shared artifact storage is required; shell, browser, and image tools are optional.

Limit: one role owns each artifact; a verifier checks the integrated output.

Mode: Framework Adapter Mode.

Suggested roles:

- story analyst: entity extraction and importance classification
- visual planner: prompts and visual asset plan
- manifest builder: image manifest and binding targets
- atlas builder: final interactive output
- verifier: checklist and asset status report

All roles must obey the no initials-only avatar default.
