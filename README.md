# OKF in 5 minutes

A small example of Google's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) (OKF, spec v0.2), using one developer's public projects as sample data.

## What problem OKF solves

An AI agent starts every task knowing nothing about your work, and the facts it needs are scattered across READMEs, posts and people's heads. OKF puts those facts in a folder of plain Markdown files that people can read and agents can follow. There is nothing to install and no service to run.

## The whole spec in 5 bullets

* **Bundle**: a folder of Markdown files. Here, [`bundle/`](bundle/index.md).
* **Concept**: one Markdown file about one idea, such as a project or a practice.
* **ID = path**: a concept's ID is its path in the bundle without `.md`, so `projects/eth-monitor`.
* **Frontmatter**: YAML between `---` lines at the top of the file.
* **Only `type` is required**: everything else is optional, and you choose the type names.

Two filenames are reserved: `index.md` lists a folder's contents, and `log.md` records its history.

## What OKF is not

* **Not SEO.** It helps agents and people that read your files. It is not meant to change how web pages rank.
* **Not a platform.** There is no registry, server or required tool. A git repo is enough.
* **No security model.** Its trust fields are advisory, not access control. Anyone who can read the folder can read everything in it, so keep secrets out.

## Try it

You need Python 3.8 or newer and PyYAML: `pip install pyyaml`. Run everything from this folder.

**1. Open the minimal file.** [`demo/minimal/hello.md`](demo/minimal/hello.md) is a complete concept. Then compare it with a fuller one: [`bundle/projects/eth-monitor.md`](bundle/projects/eth-monitor.md).

**2. Run the validator.**

```bash
python scripts/validate.py
```

```text
OK: 13 files checked in bundle
```

**3. Break a file and watch it fail.** Delete the `type: Project` line from `bundle/projects/eth-monitor.md` and run the validator again. The path uses `\` on Windows.

```text
bundle/projects/eth-monitor.md: frontmatter needs a non-empty type
```

Put the line back. Then try renaming a concept: every link to it is reported as broken.

**4. Add your own concept.** Create `bundle/practices/my-practice.md`:

```markdown
---
type: Practice
description: One sentence about the lesson.
---

Say what to do. Link to something related: [AI agents](../topics/ai-agents.md).
```

Add a line for it to [`bundle/index.md`](bundle/index.md), so agents can find it, and run the validator.

**5. Ask Claude a question from [`demo/questions.md`](demo/questions.md).** [`CLAUDE.md`](CLAUDE.md) tells Claude to read the bundle first.

```bash
claude -p "How do I run invoice-reminders locally?"
```

Compare your answer with [`demo/results.md`](demo/results.md), which shows real runs with and without the bundle. To see how a blog post differs from a concept, read [`demo/jekyll-vs-okf.md`](demo/jekyll-vs-okf.md).

## Next steps

Add things when you feel the need, not before.

**More fields:**

* `verified`: once a person has checked a concept. Nothing here has it yet, so every concept counts as unverified.
* `status: deprecated`: when something is out of date but others still link to it.
* `stale_after`: when a fact has an expiry date.
* A custom key of your own: any tool reading OKF must accept unknown keys.

**More folders:**

* Start a new folder when a kind of concept has enough files to be hard to scan.
* Add an `index.md` to a folder when the root index gets too long.
* Add a `log.md` when people ask what changed.

**More links:**

* Add a link when knowing one concept helps someone use another, and say why in the sentence around it. OKF links have no types, so the sentence carries the meaning.
* This project uses relative links (`../topics/ai-agents.md`), which also work when browsing on GitHub. The spec recommends bundle-rooted links (`/topics/ai-agents.md`), which survive moving a file. The validator accepts both.

**A note on strictness:** `scripts/validate.py` fails on broken links to keep this example tidy. The spec is more relaxed: a broken link may simply be knowledge nobody has written yet, and tools reading OKF must not reject a bundle for it.
