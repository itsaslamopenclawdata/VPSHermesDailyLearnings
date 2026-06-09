# /prune — Retire dead patterns

The user invoked /prune [--dry-run] [--window=7d]

## Step 1: Run the analysis
```bash
~/.hermes/bin/50x-prune.sh "$@"
```

This script:
1. Filters the log to the window
2. Identifies patterns with ≥ 3 harmful outcomes
3. (--dry-run) Lists them without action
4. (default) Moves them to ~/.hermes/retired-patterns.md
5. Adds them to ~/.hermes/dead-patterns.txt
6. Removes them from the AGENTS.md pre-load table
7. Logs the retirement to ~/.hermes/pattern-use.log

## Step 2: Output the summary
```
## Prune results
- Retired: <N> patterns
- Affected: P##, P##, ...
- Action: moved to retired-patterns.md, removed from pre-load table
- Next: run /measure to see updated dashboard
```
