---
mode: agent
description: Provide recommendations for improving the single-source requirement of the documentation.
---

Run the shared **recommendations** analysis for the `single-source-requirement` criteria area.

1. Read the criteria definition in `.github/prompts/criteria/single-source-requirement.md`.
2. Read and follow the shared procedure in `.github/prompts/recommendations.prompt.md`, treating `single-source-requirement` as the selected area.

Optional output filename override: `${input:title}` — if non-empty, use it as the output filename; otherwise use the engine's default (`<project-slug>-<stem>-recommendations.md`).
