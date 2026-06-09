Run the 50x self-improve loop.

## Step 1: Read the log
Filter ~/.hermes/pattern-use.log to the last 7 days. Save to /tmp/last-week-patterns.log.

## Step 2: Identify dead patterns
For each P## in the log, count outcomes. Any pattern with ≥ 3 harmful in 7 days is a retirement candidate.

## Step 3: Identify promotion candidates
Read ~/.hermes/emerging-patterns.md. For each entry:
- If the pattern was logged ≥ 3 times in the last 7 days (under any name), mark for promotion
- If the user has explicitly tagged the entry "promote", mark for promotion

## Step 4: Retire dead patterns
For each retirement candidate, run:
```bash
~/.hermes/bin/50x-prune.sh
```

This script handles all the retirement logic (move to retired-patterns.md, add to dead-patterns.txt, remove from AGENTS.md pre-load, log).

## Step 5: Promote emerging patterns
For each promotion candidate, run:
```bash
~/.hermes/bin/50x-promote.sh <name>
```

The script validates the 7 fields, assigns the next P## number, and updates the library.

## Step 6: Update the pre-load table
For each of the top 5 patterns by helped count in the last 7 days, ensure it's in the AGENTS.md pre-load table under the appropriate task type. If it's not, add a row.

## Step 7: Re-order the library
Move the top 10 patterns (by helped count in last 7d) to the top of the index in 50x-patterns.md. Add a comment to patterns with 0 applications in 30 days: "<!-- low-priority: 0 applications in 30d -->"

## Step 8: Report
Post a Telegram message:
```
50x self-improve — week of YYYY-MM-DD
Retired: N patterns
Promoted: M patterns
Top 5 helpers: P## (X helped), ...
Productivity delta this week: Z× (vs last week: W×)
```

Also append a full dashboard section to ~/.hermes/50x-dashboard.md.

## Skills used
- file: read/write the log and library
- terminal: run the prune and promote scripts
- obsidian (optional): if the dashboard should land in the vault

## Deliver
- telegram (the summary)
- local (the full dashboard appended to ~/.hermes/50x-dashboard.md)
