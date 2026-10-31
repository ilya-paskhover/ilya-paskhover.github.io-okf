# Results: without the bundle vs with it

Each answer below is the agent's real output, unedited.

## How this ran

* 10 cold, headless `claude -p` runs on 2026-10-31, one per question and setup, all with model `claude-sonnet-5-5`.
* **Without**: an empty folder, no tools, and only the four repo names in the prompt.
* **With**: a folder holding only `bundle/`, with the `CLAUDE.md` rule as a system prompt, and the read-only tools `Read`, `Glob` and `Grep`. No web access.
* Global instructions were switched off with `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1`. A first batch was thrown away because the author's global `CLAUDE.md` had leaked into it.
* The answers were then checked against the repo READMEs and GitHub's language stats. All five "with" answers were correct.

```bash
# Without, run in an empty folder
claude -p "These are the public GitHub repos of ilya-paskhover: claude-code-mods, eth-monitor, invoice-reminders, ilya-paskhover.github.io. You have only these names. Question: <question> Answer in at most 3 sentences." --model claude-sonnet-5-5 --tools "" --setting-sources project --strict-mcp-config --no-session-persistence

# With, run in a folder holding bundle/ and CLAUDE.md
claude -p "Question: <question> Answer in at most 3 sentences." --append-system-prompt "$(cat CLAUDE.md)" --model claude-sonnet-5-5 --tools "Read,Glob,Grep" --setting-sources project --strict-mcp-config --no-session-persistence
```

**Limits**: one run per question, so wording will vary between runs. The same author wrote the questions and the bundle, so the bundle was bound to cover them. This shows the idea, and it is not a benchmark.

## 1. Which repo uses Python?

**Without:**

> From the names alone, **eth-monitor** is the most likely Python repo, since monitoring scripts and blockchain tooling are commonly written in Python. **invoice-reminders** is a plausible second candidate for the same reason (automation scripts). That's a guess, though; the names don't confirm any language, and I'd need to look at the repos' contents to be sure.

**With:**

> The ETH Monitor project uses Python. According to `bundle/index.md`, it's a Python script that sends a Telegram alert when a crypto, stock or FX price moves past a threshold. The other projects are listed as TypeScript, Next.js/Fastify, Jekyll, and a browser game. I didn't open `projects/eth-monitor.md`, so I haven't checked the details there.

**Difference:** a hedged guess with one wrong candidate became a sourced fact, found from the index alone.

## 2. How do I run invoice-reminders locally?

**Without:**

> I can't tell from the repo name alone, since I haven't seen its contents. As a general approach: clone it (`git clone https://github.com/ilya-paskhover/invoice-reminders`), read the README for setup steps, then install dependencies (e.g. `npm install` or `pip install -r requirements.txt`) and run the start command it lists (e.g. `npm start` or `python main.py`). If you'd like, I can fetch the repo and give you exact steps.

**With:**

> You need Docker with Compose. From the repo root, run `docker compose up -d --build --force-recreate --wait`. Then open the web app at http://localhost:13000, the API at http://localhost:14000 and the Mailpit inbox at http://localhost:18025, and stop everything with `docker compose down`.

**Difference:** generic commands that do not apply became the exact command and ports.

## 3. What is related to invoice-reminders?

**Without:**

> From the name alone, invoice-reminders is likely a tool that tracks unpaid invoices and sends payment reminders, probably to clients by email or similar. Among your repos, nothing else clearly relates to it: claude-code-mods, eth-monitor, and ilya-paskhover.github.io (likely your personal site) look like separate projects. I only have the repo names, so this is an inference; I'd need to look at the repo's README or code to confirm.

**With:**

> Invoice Reminders is linked to two practices: [Answer one question with a proof of concept](bundle/practices/one-question-poc.md), because its README calls it a proof of concept, and [Brief agents like a team](bundle/practices/brief-agents-like-a-team.md), because an AI agent team built it from a written spec and a checked task list. It's also listed under the [Small apps](bundle/topics/small-apps.md) topic. Its code is at https://github.com/ilya-paskhover/invoice-reminders, and no blog post covers it.

**Difference:** "nothing related" became three related concepts, each with a reason, because links carry relationships that names cannot.

## 4. Does eth-monitor only watch Ethereum?

**Without:**

> I can't say for sure from the repo name alone. "eth-monitor" suggests it focuses on Ethereum (ETH), but it could also track related things like ERC-20 tokens, gas prices, or other EVM chains. I'd need to look at the repo's README or code to confirm.

**With:**

> No. It defaults to ETH/USD, but it can also watch other crypto (via CoinGecko), stocks and FX (via Yahoo Finance), and US stocks (via Finnhub). The site's project list still describes it as ETH/USD only, but the README, which the bundle follows, says otherwise.

**Difference:** the name pointed the wrong way, and the bundle corrected it and flagged the outdated site description.

## 5. How many people use claude-code-mods?

**Without:**

> I can't tell from the repo names alone, since usage numbers (stars, forks, downloads) aren't in them. I could check the repo's GitHub page for stars and forks as a rough proxy if you'd like, but even those wouldn't give an actual user count.

**With:**

> The bundle doesn't say how many people use claude-code-mods. Its project page, `bundle/projects/claude-code-mods.md`, has no usage, install, download or star counts. To answer this, someone would need to add a usage figure to that file, for example from the GitHub repo's stats.

**Difference:** neither run invented a number, but only the bundle run named the file to fix, as `CLAUDE.md` asks.

## What this shows

The agent without the bundle was honest, not wrong: it mostly said it could not know. The bundle's gain is that it turned those hedges into specific, sourced answers.
