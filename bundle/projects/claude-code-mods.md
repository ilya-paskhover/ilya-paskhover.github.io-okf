---
type: Project
title: Claude Code mods
description: "Three TypeScript plugins for Claude Code: last-turn summary, shared notes, running sessions."
resource: https://github.com/ilya-paskhover/claude-code-mods
tags: [claude-code, typescript, plugins]
generated: { by: claude-code/opus-5-5, at: 2026-10-31T14:55:00Z }
sources:
  - id: post
    resource: https://ilya-paskhover.github.io/2026/10/17/claude-code-mods.html
    title: Claude Code mods (post)
  - id: readme
    resource: https://github.com/ilya-paskhover/claude-code-mods#readme
    title: claude-code-mods README
---

# What it is

Three independent mods for Claude Code.[^post]

* **turn-pulse**: a band above the prompt showing the last turn's duration, edited files, tool results and usage-limit cost.
* **notes**: `/note` saves a note to a list shared across projects; `/notes` opens it in a side pane.
* **sessions**: `/sessions` lists the Claude Code sessions running on this machine and whether each is working or idle.

# Facts

* Language: TypeScript. License: MIT.[^readme]
* Built and tested on Windows, in the desktop app's Code tab. The mod API is early access and may change between releases.[^readme]

# Run it

Install from a terminal, one line per mod. `/plugin` is not available in the desktop app's Code tab.[^readme]

```bash
claude plugin marketplace add ilya-paskhover/claude-code-mods
claude plugin install turn-pulse@claude-code-mods
```

The other two mods install the same way: `notes@claude-code-mods` and `sessions@claude-code-mods`.

# Related

Part of the [AI agents](../topics/ai-agents.md) topic.

[^post]: [Claude Code mods](https://ilya-paskhover.github.io/2026/10/17/claude-code-mods.html)
[^readme]: [claude-code-mods README](https://github.com/ilya-paskhover/claude-code-mods#readme)
