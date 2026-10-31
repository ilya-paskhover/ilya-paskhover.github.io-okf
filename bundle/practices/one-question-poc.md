---
type: Practice
title: Answer one question with a proof of concept
description: Write one yes-or-no question first, fake everything else, and end with a decision.
tags: [proof-of-concept, planning]
generated: { by: claude-code/opus-5-5, at: 2026-10-31T14:55:00Z }
sources:
  - id: poc-post
    resource: https://ilya-paskhover.github.io/2023/12/28/a-proof-of-concept-should-answer-one-question.html
    title: A proof of concept should answer one question
---

# The practice

1. Write the question down before any code. Make it specific, with numbers and a yes-or-no answer.[^poc-post]
2. Build only what answers it. Fake the rest: a hard-coded config, a script instead of a service.[^poc-post]
3. Record the decision: the answer, what it means for the product, and what is still unknown. Then throw the code away, or keep it knowing it was not built to last.[^poc-post]

# Examples

* Good: "Can this gateway connect to X sensors of type Y in parallel, within a range of Z meters?"[^poc-post]
* Bad: "Let's see what the new sensor can do." It never ends.[^poc-post]

# Related

[Invoice Reminders](../projects/invoice-reminders.md) is a proof of concept. See also [Industrial IoT and hardware](../topics/iot-and-hardware.md).

[^poc-post]: [A proof of concept should answer one question](https://ilya-paskhover.github.io/2023/12/28/a-proof-of-concept-should-answer-one-question.html)
