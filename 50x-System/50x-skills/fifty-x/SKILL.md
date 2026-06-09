---
name: fifty-x
description: "Apply 50x patterns to any task. Trigger on /50x <task>. Scans 50 patterns from the 18 watch repos, pre-loads the top 3 for the task type, executes, logs the application."
version: 1.0.0
author: Aslam Shaik
license: MIT
metadata:
  hermes:
    tags: [50x, patterns, productivity, harness]
    related_skills: [apply-pattern, measure-patterns, prune-patterns, promote-patterns]
---

# 50x — Apply 50x Patterns to Any Task

## When to load
- User invokes `/50x <task>`
- User says "make this 50x" or "apply the 50x patterns"
- User asks "what's the most efficient way to..."

## What this skill does
1. Identifies the task type
2. Pre-loads the top 3 patterns from the 50x library for that type
3. Composes a plan that integrates the patterns
4. Executes (or hands back the plan)
5. Logs every pattern application via `~/.hermes/bin/pattern-log.sh`

## The 50x library
Lives at: `~/.hermes/profiles/<this-profile>/references/50x-patterns.md`
50 patterns distilled from 18 watch repos. Each has: source, when, what, how, verify, dead signal.

## Pre-load table (by task type)
| Task type | Patterns |
|---|---|
| writing | P04, P39, P47 |
| building | P31, P32, P33, P34 |
| evaluating | P40, P41, P46 |
| researching | P13, P14, P42, P43, P44 |
| coordinating | P01, P02, P25, P28, P35, P37, P38 |
| learning | P14, P49, P50 |
| ops | P07, P20, P21, P22, P23, P48 |
| personal | P03, P12, P15, P18, P19 |
| general | P21, P25, P35 |

## Standard response
```
## Patterns applied: P##, P##, P##

## Plan
<step-by-step>

## Expected outcome
<measurable>

## Log
~/.hermes/bin/pattern-log.sh P## <task-slug> applied
```

## What this skill is NOT
- Not a substitute for thinking. The patterns encode best practices, not magic.
- Not a documentation dump. Only the top 3 patterns are surfaced; full library is 1 read away.
- Not a measurement tool. Use `/measure` for that.
