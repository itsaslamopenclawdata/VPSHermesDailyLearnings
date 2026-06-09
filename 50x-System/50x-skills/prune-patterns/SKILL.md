---
name: prune-patterns
description: "Retire dead patterns from the 50x library. Trigger on /prune [--dry-run]. Identifies patterns with ≥ 3 harmful outcomes in 7 days, moves them to retired-patterns.md, removes from AGENTS.md pre-load."
version: 1.0.0
author: Aslam Shaik
license: MIT
metadata:
  hermes:
    tags: [50x, prune, retire, dead-patterns]
    related_skills: [measure-patterns, promote-patterns, fifty-x]
---

# Prune-Patterns — Retire the Dead

## When to load
- User invokes `/prune` or `/prune --dry-run`
- Sunday self-improve cron (Step 4)

## What this skill does
1. Identifies patterns with ≥ 3 harmful outcomes in last 7 days
2. Moves the full pattern block to `~/.hermes/retired-patterns.md`
3. Adds to `~/.hermes/dead-patterns.txt`
4. Removes from the AGENTS.md pre-load table
5. Logs the retirement

## Run the bundled script
```bash
~/.hermes/bin/50x-prune.sh [--dry-run] [--window=7d]
```

## Why this matters
Without pruning, the library accumulates dead weight. Pruning keeps the agent focused on what works.

## Safety
- `--dry-run` mode lists candidates without action
- Retired patterns are never deleted — they go to `~/.hermes/retired-patterns.md` for archaeology
