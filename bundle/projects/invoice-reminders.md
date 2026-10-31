---
type: Project
title: Invoice Reminders
description: Next.js, Fastify and Postgres proof of concept that chases late invoices by email.
resource: https://github.com/ilya-paskhover/invoice-reminders
tags: [typescript, nextjs, fastify, postgres, docker, proof-of-concept]
generated: { by: claude-code/opus-5-5, at: 2026-10-31T14:55:00Z }
sources:
  - id: readme
    resource: https://github.com/ilya-paskhover/invoice-reminders#readme
    title: invoice-reminders README
---

# What it is

Imports overdue invoices, sends escalating reminder emails by rule (1, 10 and 30 days after the due date by default), and gives the customer a pay link that marks the invoice paid.[^readme]

# Facts

* Stack: Next.js 15, React 19, Fastify 5, Postgres 16, TypeScript, Docker Compose. Tests use Vitest. License: GPL-3.0.[^readme]
* Live demo: <https://invoice-reminders-web.onrender.com>. Data resets daily and no real emails are sent. The first visit can take about a minute.[^readme]
* A portfolio proof of concept: no authentication, and the Stripe import and pay page are mocks.[^readme]
* No blog post covers this project.

# Run it

Requires Docker with Compose.[^readme]

```bash
docker compose up -d --build --force-recreate --wait
```

Web app: <http://localhost:13000>. API: <http://localhost:14000>. Mailpit inbox: <http://localhost:18025>. Stop with `docker compose down`.

# Related

* Its README calls it a proof of concept, the kind described in [Answer one question with a proof of concept](../practices/one-question-poc.md).
* Its README says an AI agent team built it from a written spec and a checked task list, as in [Brief agents like a team](../practices/brief-agents-like-a-team.md).
* Listed under [Small apps](../topics/small-apps.md).

[^readme]: [invoice-reminders README](https://github.com/ilya-paskhover/invoice-reminders#readme)
