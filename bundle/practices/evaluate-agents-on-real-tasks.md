---
type: Practice
title: Evaluate agents on real tasks
description: Grade real tasks with code first, rerun on every change, and read the failures.
tags: [ai-agents, evaluation, testing]
generated: { by: claude-code/opus-5-5, at: 2026-10-31T14:55:00Z }
sources:
  - id: eval-post
    resource: https://ilya-paskhover.github.io/2026/06/25/evaluating-ai-agents-before-you-trust-them.html
    title: Evaluating AI agents before you trust them
  - id: sofa-post
    resource: https://ilya-paskhover.github.io/2026/10/30/stack-overflow-for-agents-ab-test.html
    title: Does Stack Overflow for Agents improve Claude's answers?
---

# The practice

1. Collect a few dozen real tasks with known good results, and grade with code where you can.[^eval-post]
2. Where code cannot decide, choose a method on purpose (model judge, repeated runs, side-by-side comparison, human review) and spot-check the judge's grades by hand.[^eval-post]
3. Run the set on every change to a prompt, model or tool, and compare with the last run.[^eval-post]
4. Read the failed cases. They show what changed and supply the next task for the set.[^eval-post]

# Examples

An 8-question blind A/B test of Stack Overflow for Agents barely moved answer scores, because most answers hit the maximum. The post treats that as a limit of the test: learning more would take harder questions and rubrics verified independently.[^sofa-post]

# Related

Pairs with [Brief agents like a team](brief-agents-like-a-team.md). Part of the [AI agents](../topics/ai-agents.md) topic.

[^eval-post]: [Evaluating AI agents before you trust them](https://ilya-paskhover.github.io/2026/06/25/evaluating-ai-agents-before-you-trust-them.html)
[^sofa-post]: [Does Stack Overflow for Agents improve Claude's answers?](https://ilya-paskhover.github.io/2026/10/30/stack-overflow-for-agents-ab-test.html)
