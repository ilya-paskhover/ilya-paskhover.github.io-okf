---
type: Practice
title: Brief agents like a team
description: Give agents a written goal, the context they cannot guess, a check to pass, and a human review.
tags: [ai-agents, process]
generated: { by: claude-code/opus-5-5, at: 2026-10-31T14:55:00Z }
sources:
  - id: managing-post
    resource: https://ilya-paskhover.github.io/2026/01/20/from-managing-people-to-managing-agents.html
    title: From managing people to managing agents
  - id: design-post
    resource: https://ilya-paskhover.github.io/2026/10/16/fresh-design-and-content-with-ai-agents.html
    title: Fresh design and content with AI agents
---

# The practice

1. Write the task with a clear finish line.[^managing-post]
2. Write the context an agent cannot guess: project rules, what not to touch, how to check the result. An agent starts from zero every task.[^managing-post]
3. Set a check it must pass before a human looks. Tests act as the contract.[^design-post]
4. Review before merging, and ask for pushback, since agents rarely object to a bad plan unprompted.[^managing-post]
5. Have agents stop and ask before anything that matters: the plan, a blocker, a commit.[^design-post]

# Examples

The site redesign used a setup called poc-dev-team: a planner writes the spec and task list, developers each own one part, and a QA agent tests each task without editing files. A command runs one task at a time, commits each pass, and stops after three failed attempts.[^design-post]

# Related

Used on the [Personal site](../projects/personal-site.md) and described for [Invoice Reminders](../projects/invoice-reminders.md). Pairs with [Evaluate agents on real tasks](evaluate-agents-on-real-tasks.md).

[^managing-post]: [From managing people to managing agents](https://ilya-paskhover.github.io/2026/01/20/from-managing-people-to-managing-agents.html)
[^design-post]: [Fresh design and content with AI agents](https://ilya-paskhover.github.io/2026/10/16/fresh-design-and-content-with-ai-agents.html)
