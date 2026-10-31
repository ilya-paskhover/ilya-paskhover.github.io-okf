---
type: Project
title: Personal site
description: The Jekyll blog and project showcase published on GitHub Pages.
resource: https://ilya-paskhover.github.io/
tags: [jekyll, ruby, github-pages, docker]
generated: { by: claude-code/opus-5-5, at: 2026-10-31T14:55:00Z }
sources:
  - id: readme
    resource: https://github.com/ilya-paskhover/ilya-paskhover.github.io#readme
    title: Site README
  - id: pages-post
    resource: https://ilya-paskhover.github.io/2026/10/04/how-github-pages-publishes-a-site.html
    title: How GitHub Pages publishes a site
  - id: design-post
    resource: https://ilya-paskhover.github.io/2026/10/16/fresh-design-and-content-with-ai-agents.html
    title: Fresh design and content with AI agents
---

# What it is

The blog and project showcase of Ilya Paskhover, principal software architect. Repository: <https://github.com/ilya-paskhover/ilya-paskhover.github.io>.[^readme]

# Facts

* Built with Jekyll. GitHub Pages publishes it from the root of the `master` branch. A workflow builds it and validates the HTML but does not publish it.[^pages-post]
* The current design and content were built by AI agents, with a human approving each step.[^design-post]
* The repository also hosts the built [Shallow Whale](shallow-whale.md) game.

# Run it

Requires Docker with Compose.[^readme]

```bash
docker compose up -d --build --force-recreate --wait
```

Open <http://localhost:14000>. Re-run the command after changing any file. Stop with `docker compose down`.

# Related

How the redesign ran is described in [Brief agents like a team](../practices/brief-agents-like-a-team.md).

[^readme]: [Site README](https://github.com/ilya-paskhover/ilya-paskhover.github.io#readme)
[^pages-post]: [How GitHub Pages publishes a site](https://ilya-paskhover.github.io/2026/10/04/how-github-pages-publishes-a-site.html)
[^design-post]: [Fresh design and content with AI agents](https://ilya-paskhover.github.io/2026/10/16/fresh-design-and-content-with-ai-agents.html)
