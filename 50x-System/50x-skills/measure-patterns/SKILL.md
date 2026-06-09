---
name: measure-patterns
description: "Show 50x pattern usage metrics. Trigger on /measure [period]. Computes M1-M5 from ~/.hermes/pattern-use.log and outputs the dashboard."
version: 1.0.0
author: Aslam Shaik
license: MIT
metadata:
  hermes:
    tags: [50x, metrics, dashboard, measurement]
    related_skills: [fifty-x, prune-patterns]
---

# Measure-Patterns — The 50x Dashboard

## When to load
- User invokes `/measure` or `/measure 7d` or `/measure 30d`
- User asks "is the 50x working?" or "show me the dashboard"
- Sunday self-improve cron (for the weekly summary)

## What this skill does
1. Filters `~/.hermes/pattern-use.log` to the period
2. Computes M1-M5
3. Reads `~/.hermes/emerging-patterns.md` and `~/.hermes/dead-patterns.txt`
4. Outputs a markdown dashboard

## Metrics
- **M1 — Application rate:** total applications / period
- **M2 — Top 5 patterns:** by helped count
- **M3 — Dead patterns:** ≥ 3 harmful in window
- **M4 — Emerging patterns:** count of new patterns discovered
- **M5 — Productivity delta:** helped × 15 min vs baseline

## Standard output
See `50x-INSTRUMENTATION.md` for the full dashboard template.

## Run the bundled script
```bash
~/.hermes/bin/50x-measure.sh [period]
```

## What this skill is NOT
- Not a self-improver. Use `/prune` and `/promote` for that.
- Not a forecaster. Past metrics only.
