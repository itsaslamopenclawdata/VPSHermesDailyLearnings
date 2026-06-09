---
name: apply-pattern
description: "Apply a single named pattern (P##) to a task. Trigger on /apply-pattern P## <task>. Loads one pattern, executes it, logs the application."
version: 1.0.0
author: Aslam Shaik
license: MIT
metadata:
  hermes:
    tags: [50x, patterns, single-pattern]
    related_skills: [fifty-x, measure-patterns]
---

# Apply-Pattern — One Pattern, One Task

## When to load
- User invokes `/apply-pattern P## <task>`
- User says "apply pattern 29" or "use the pipeline pattern"

## What this skill does
1. Loads the P## entry from `~/.hermes/profiles/<this-profile>/references/50x-patterns.md`
2. Applies its "How" section to the task
3. Logs the application

## Standard response
```
## Pattern: P## — <name>

## When applied
<restate the trigger>

## How applied
<steps taken>

## Result
<output / artifact>

## Log
~/.hermes/bin/pattern-log.sh P## <task-slug> applied
```

## Use case
- You know exactly which pattern fits. Don't need the full /50x scan.
- Faster than /50x (no task-type classification needed).
