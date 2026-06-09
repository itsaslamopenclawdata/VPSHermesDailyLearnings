# 50x Self-Improve Loop — The Sunday Cron

> **What this is:** The automated weekly loop that keeps the 50x pattern library healthy — pruning dead patterns, promoting emerging ones, and updating the AGENTS.md pre-load table.
> **When:** Sunday 21:00 (after the weekly review at 20:00, before the next Monday morning).
> **Output:** Updated `50x-patterns.md`, `AGENTS.md`, and a Telegram summary.

---

## The full loop in 8 steps

```
┌──────────────────────────────────────────────────────────────┐
│                   50x Self-Improve Loop                       │
│                       (Sunday 21:00)                         │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │ 1. Read ~/.hermes/pattern-use.log (last 7 days)       │
  └────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │ 2. For each P##, count outcomes: helped/neutral/      │
  │    harmful. Identify dead patterns (≥3 harmful).      │
  └────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │ 3. Read ~/.hermes/emerging-patterns.md                │
  │    Identify promotion candidates (≥ 3 successful      │
  │    applications OR explicitly tagged "promote")       │
  └────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │ 4. RETIRE: For each dead pattern:                     │
  │    - Move to ~/.hermes/retired-patterns.md            │
  │    - Add to ~/.hermes/dead-patterns.txt               │
  │    - Remove from pre-load table in AGENTS.md          │
  │    - Log the retirement                               │
  └────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │ 5. PROMOTE: For each candidate emerging pattern:      │
  │    - Validate the 7 required fields                   │
  │    - Assign next P## number                           │
  │    - Append to ~/.hermes/profiles/<p>/references/     │
  │      50x-patterns.md                                  │
  │    - Update the index table at the top                │
  │    - Add to pre-load table in AGENTS.md               │
  │    - Remove from emerging-patterns.md                 │
  │    - Log the promotion                                │
  └────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │ 6. UPDATE PRE-LOAD TABLE:                             │
  │    - Find the top 5 most-applied patterns             │
  │    - For each, add a row in the pre-load table        │
  │    - In the AGENTS.md task-type → patterns mapping    │
  └────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │ 7. RE-ORDER the library:                              │
  │    - Move the top 10 patterns to the front of the     │
  │      index (so they're seen first)                    │
  │    - Archive patterns not used in 30 days to a        │
  │      "low-priority" section                           │
  └────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │ 8. REPORT: Post a summary to Telegram                │
  │    - X patterns retired                               │
  │    - Y patterns promoted                              │
  │    - Top 5 helpers this week                          │
  │    - Productivity delta                               │
  └────────────────────────────────────────────────────────┘
```

---

## The cron job

```bash
hermes cron create "0 21 * * 0" \
  --name "50x-self-improve" \
  --prompt "Run the 50x self-improve loop.

## Step 1: Read the log
\`\`\`
cat ~/.hermes/pattern-use.log | tail -500 > /tmp/last-week-patterns.log
\`\`\`

## Step 2: Identify dead patterns
Parse /tmp/last-week-patterns.log. For each pattern_id (P##), count outcomes. Any pattern with ≥ 3 harmful outcomes in 7 days is a retirement candidate.

## Step 3: Identify emerging patterns
Read ~/.hermes/emerging-patterns.md. For each entry, check ~/.hermes/pattern-use.log for evidence of success (≥ 3 applications of the same pattern under different names). If found, mark for promotion.

## Step 4: Retire dead patterns
For each retirement candidate:
1. Append the full pattern block to ~/.hermes/retired-patterns.md with the date and a 1-line reason
2. Add to ~/.hermes/dead-patterns.txt: \`P## YYYY-MM-DD <reason>\`
3. Edit ~/.hermes/profiles/quantum-venture-lab/AGENTS.md to remove the pattern from the pre-load table
4. Log to ~/.hermes/pattern-use.log: \`<TS> | RETIRED | P## | <reason>\`

## Step 5: Promote emerging patterns
For each promotion candidate:
1. Validate the 7 fields: name, source, when, what, how, verify, dead-signal. If any missing, abort and list missing fields.
2. Determine the next P## number (look at the highest existing number in 50x-patterns.md, add 1).
3. Append the new pattern to ~/.hermes/profiles/quantum-venture-lab/references/50x-patterns.md in the appropriate group section (or create a new 'Cross-cutting' entry).
4. Update the index table at the top of 50x-patterns.md.
5. Edit AGENTS.md to add the new pattern to the pre-load table (or as a new row if the task type is novel).
6. Remove the entry from ~/.hermes/emerging-patterns.md.
7. Log to ~/.hermes/pattern-use.log: \`<TS> | PROMOTED | <emerging-name> -> P##\`

## Step 6: Update the pre-load table
Look at the last 7 days of applications. For each of the top 5 patterns by helped count, add or update a row in the AGENTS.md pre-load table under the appropriate task type.

## Step 7: Re-order the library
Move the top 10 patterns (by helped count in last 7d) to the top of the index table in 50x-patterns.md. Mark patterns with 0 applications in 30 days as 'low-priority' in a comment.

## Step 8: Report
Post a Telegram message:
\`\`\`
50x self-improve — week of YYYY-MM-DD
Retired: N patterns (P##, P##, ...)
Promoted: M patterns (P##, P##, ...)
Top 5 helpers: P## (X helped), P## (Y helped), ...
Productivity delta this week: Z× (vs last week: W×)
\`\`\`

Skills: file, terminal
Deliver: telegram" \
  --skills "file,terminal" \
  --deliver telegram
```

---

## Manual trigger (for testing)

```bash
# Run the self-improve loop right now
hermes cron run 50x-self-improve

# Or invoke the slash command if you created one
/50x-improve
```

---

## What "success" looks like (90 days)

By day 90, you should see:
- **30+ patterns** in the library (10 original + 20 promoted from emerging)
- **5-10 retired patterns** (you've learned what doesn't work)
- **Productivity delta ≥ 50×** (vs. baseline)
- **Top 5 helpers** clearly identified (you know which patterns to invest in)
- **Emerging pattern rate** ≥ 2/week (the agent is constantly learning your style)
- **AGENTS.md pre-load table** evolved to your actual usage (not the generic default)

By day 180:
- **50+ patterns** in the library
- **15+ retired patterns**
- **Productivity delta ≥ 100×** (the patterns compound)
- The library is **uniquely yours** — no other agent has this set

---

## Edge cases

### The loop can't make changes
- AGENTS.md is read-only or locked → log the error, retry on next Sunday
- 50x-patterns.md is missing → re-create from the upstream repo (this one)

### A pattern oscillates (helped one week, harmful the next)
- Don't auto-retire; mark as 'conditional' in the index
- The next week's data will resolve it

### Too many promotions at once
- Cap at 3 promotions per week
- If more candidates exist, prioritize the ones with the most successful applications

### The user's style changes (e.g. new job, new project)
- Many patterns will go from helped to neutral
- This is expected; let them naturally decay rather than forcibly retiring
- The emerging-patterns.md will start filling with new patterns that fit the new style

---

## Recovery

If the loop corrupts the library:

```bash
# 1. Restore from this upstream repo
cp 50x-PATTERNS-LIBRARY.md ~/.hermes/profiles/quantum-venture-lab/references/50x-patterns.md

# 2. Restore AGENTS.md from your last good state
# (always commit AGENTS.md to git so you can revert)

# 3. Re-build the log files
echo "" > ~/.hermes/pattern-use.log
# Keep emerging and retired (they're append-only)

# 4. Re-run the loop
hermes cron run 50x-self-improve
```

**Tip:** Commit `AGENTS.md` and `50x-patterns.md` to a private git repo weekly. The self-improve loop is a "trusted mutator" — anything that auto-edits your prompt context needs a backup.

---

**End of 50x-SELF-IMPROVE-LOOP.md**
