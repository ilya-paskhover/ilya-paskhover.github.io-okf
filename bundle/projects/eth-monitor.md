---
type: Project
title: ETH Monitor
description: Python script that sends a Telegram alert when a crypto, stock or FX price moves past a threshold.
resource: https://github.com/ilya-paskhover/eth-monitor
tags: [python, telegram, monitoring, crypto, stocks]
generated: { by: claude-code/opus-5-5, at: 2026-10-31T14:55:00Z }
sources:
  - id: readme
    resource: https://github.com/ilya-paskhover/eth-monitor#readme
    title: eth-monitor README
  - id: projects-data
    resource: https://github.com/ilya-paskhover/ilya-paskhover.github.io/blob/master/_data/projects.yml
    title: Site project list
---

# What it is

Fetches one price and sends a Telegram alert when it moves more than a set percentage from the last alerted price.[^readme]

# Facts

* Language: Python 3.10 or newer. License: MIT.[^readme]
* Defaults to ETH/USD, but the name undersells it: it also watches other crypto (CoinGecko), stocks and FX (Yahoo Finance), and US stocks (Finnhub).[^readme]
* The site's project list still describes it as ETH/USD only.[^projects-data] This concept follows the README.
* No blog post covers this project.

# Run it

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py --test
python main.py
```

Set `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in `.env` first. `--test` sends a test message. Schedule `main.py` with cron to keep watching. Run the tests with `python -m pytest tests/ -v`.[^readme]

# Related

Covers the same subject as [Shallow Whale](shallow-whale.md), though the sources show no shared code. Listed under [Small apps](../topics/small-apps.md).

[^readme]: [eth-monitor README](https://github.com/ilya-paskhover/eth-monitor#readme)
[^projects-data]: [Site project list](https://github.com/ilya-paskhover/ilya-paskhover.github.io/blob/master/_data/projects.yml)
