# Jekyll frontmatter vs an OKF concept

Both use YAML between `---` lines, so they look alike. They answer different questions: Jekyll asks how to publish a page, and OKF asks what this thing is and how we know.

## Side by side

**Jekyll post**: `_posts/2026-10-17-claude-code-mods.markdown`

```yaml
---
title: "Claude Code mods"
date: 2026-10-17 12:00:00
topic: AI agents
description: "Three small mods for Claude Code: a summary of the last turn, a notes pane shared across projects, and a pane of running sessions."
---
```

**OKF concept**: [`bundle/projects/claude-code-mods.md`](../bundle/projects/claude-code-mods.md)

```yaml
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
```

## What changes and why

| Field | Jekyll post | OKF concept | Why |
|---|---|---|---|
| `type` | none | `Project` | The one required field. It tells a reader what kind of thing this is. |
| `date` | when the post went out | none | A publish date matters for a blog. For knowledge, `generated.at` records when the content last changed. |
| `topic` | one site category | `tags` | A category files a page in one place. Tags cut across many. |
| `resource` | none | the repo URL | Points at the real thing being described, not at a page about it. |
| `sources` | none | the post and README | Shows where each claim came from. Body footnotes such as `[^readme]` use these ids. |
| `generated` | none | who wrote it, and when | An agent wrote this concept, and the file says so. |
| `description` | a teaser for readers | a plain summary | The index reuses it, so an agent can decide whether to open the file. |

## The bigger change: ideas, not posts

A post is one piece of writing on one date. A concept is one idea, however many posts mention it.

* The post [Fresh design and content with AI agents](https://ilya-paskhover.github.io/2026/10/16/fresh-design-and-content-with-ai-agents.html) feeds three concepts: [Personal site](../bundle/projects/personal-site.md), [Brief agents like a team](../bundle/practices/brief-agents-like-a-team.md) and [AI agents](../bundle/topics/ai-agents.md).
* The concept [Brief agents like a team](../bundle/practices/brief-agents-like-a-team.md) draws on two posts written nine months apart.

## Is a Jekyll post valid OKF?

No. Running `scripts/validate.py` on a folder holding a copy of the post gives:

```text
jk\claude-code-mods-post.md: frontmatter needs a non-empty type
jk\claude-code-mods-post.md: broken link /assets/images/claude-code-mods/turn-pulse.png
jk\claude-code-mods-post.md: broken link /assets/images/claude-code-mods/notes.png
jk\claude-code-mods-post.md: broken link /assets/images/claude-code-mods/sessions.png
```

Adding `type` alone would fix the first line. The link errors come from this project's stricter script, because those images live on the site, outside the folder. The OKF spec itself tells readers to tolerate broken links.
