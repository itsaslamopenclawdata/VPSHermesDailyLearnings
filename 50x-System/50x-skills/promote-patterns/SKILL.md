---
name: promote-patterns
description: "Promote an emerging pattern to the canonical 50x library. Trigger on /promote <name>. Validates the 7 required fields, assigns the next P## number, appends to 50x-patterns.md."
version: 1.0.0
author: Aslam Shaik
license: MIT
metadata:
  hermes:
    tags: [50x, promote, emerging, library]
    related_skills: [fifty-x, prune-patterns, measure-patterns]
---

# Promote-Patterns — From Emerging to Canonical

## When to load
- User invokes `/promote <name>`
- A pattern in `~/.hermes/emerging-patterns.md` has been used successfully 3+ times
- Sunday self-improve cron (Step 5)

## What this skill does
1. Finds the named pattern in `~/.hermes/emerging-patterns.md`
2. Validates the 7 required fields (Source, When, What, How, Verify, Dead signal, ...)
3. Assigns the next P## number
4. Appends to `~/.hermes/profiles/<profile>/references/50x-patterns.md`
5. Removes from `emerging-patterns.md`
6. Logs the promotion

## Run the bundled script
```bash
~/.hermes/bin/50x-promote.sh <name>
```

## The 7 required fields
1. Source (where it came from — usually "agent-invented" + date)
2. When (trigger condition)
3. What (one-line description)
4. How (3-7 step recipe)
5. Verify (how to know it worked)
6. Dead signal (when to retire)
7. Source multiplier (estimated time saved per application)

## Why this matters
The 50x library gets uniquely yours over time. Promoted patterns encode your style, your workflows, your preferences. That's how the system compounds.
