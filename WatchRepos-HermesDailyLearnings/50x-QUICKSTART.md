# 50x Quickstart — Make Hermes 50x More Productive

> **The whole system in one file.** Read this, run the 6 commands, you're done.
> The 10 `Workflow0X-*.md` files and the 18 `watchrepos-index/*.md` files are
> **reference material**, not templates. The real product is the loop below.

---

## The one-sentence pitch

> 18 watch repos → daily diff → 1 patterns file → 1 AGENTS.md enforcement → measured 50x.

---

## The 50x loop (the only diagram in this doc)

```
  18 watch repos
        │ (fetched at 05:00 every day by `watchrepos-daily-diff`)
        ▼
  /opt/data/watchrepo-harness/state/last-run.json
        │ (changed files since last run)
        ▼
  50x-PATTERNS-LIBRARY.md       ← curated, versioned, 50 patterns (P01–P50)
        │ (referenced by AGENTS.md on every turn)
        ▼
  AGENTS.md enforcement          ← auto-loads top 3 patterns per task type
        │ (agent applies them, mentions them, logs them)
        ▼
  ~/.hermes/pattern-use.log      ← measurement: every application recorded
        │ (Sunday self-improve cron reads it)
        ▼
  50x metrics dashboard          ← proves 1x vs 50x
```

---

## 6 commands to install the 50x system

```bash
# 0. Assumes the harness repo is at /opt/data/watchrepo-harness (this directory)

# 1. Install the patterns into your Hermes profile
mkdir -p ~/.hermes/profiles/quantum-venture-lab/references
cp /opt/data/watchrepo-harness/fifty_x/50x-PATTERNS-LIBRARY.md \
   ~/.hermes/profiles/quantum-venture-lab/references/50x-patterns.md

# 2. Append the runtime enforcement to AGENTS.md
cat /opt/data/watchrepo-harness/fifty_x/50x-AGENTS-MD-PATCH.md \
    >> ~/.hermes/profiles/quantum-venture-lab/AGENTS.md

# 3. Initialize the measurement log
touch ~/.hermes/pattern-use.log
touch ~/.hermes/emerging-patterns.md
touch ~/.hermes/dead-patterns.txt

# 4. Install the daily re-distill cron (one-time)
hermes cron create "0 5 * * *" \
    --name watchrepos-daily-diff \
    --prompt "Run the 50x distiller. Diff the 18 watch repos against /opt/data/watchrepo-harness/state/last-run.json. For each changed file, check if it adds/revises a pattern in 50x-PATTERNS-LIBRARY.md. If so, propose a patch and apply it. Re-push the file to VPSHermesDailyLearnings/WatchRepos-HermesDailyLearnings/. Post a 3-bullet Telegram summary." \
    --skills watchrepos-daily-learning,terminal,file,github \
    --deliver telegram

# 5. Install the Sunday self-improve cron
hermes cron create "0 20 * * 0" \
    --name fifty-x-self-improve \
    --prompt "Read ~/.hermes/pattern-use.log. Identify the top 5 most-applied patterns, the 3 worst-performing patterns, and any entries in ~/.hermes/emerging-patterns.md. (a) Move harmful-3x-in-7-days patterns to ~/.hermes/dead-patterns.txt and prepend 'DEAD: ' in the library. (b) Promote top emerging patterns into the library with a fresh P## number. (c) Output a metrics report: total applications, top helper, top dead, success rate. Post to Telegram." \
    --skills terminal,file,kanban \
    --deliver telegram

# 6. Start a new session and test it
hermes -p quantum-venture-lab
# Try: "Plan a 7-day launch of a quantum-portfolio-optimizer MVP"
# The agent should auto-load P31, P32, P33, P34, P40, P41 and announce the load.
```

---

## What you get on day 1

- **50 patterns** distilled from your 18 watch repos, each with: source, when-to-use, how-to-apply, verify, dead-signal
- **AGENTS.md enforcement** that forces the agent to consult the pattern index on every non-trivial task
- **Pre-loaded pattern sets** for 8 known task types (writing, building, evaluating, researching, etc.)
- **A pattern-use log** that records every application so you can measure the multiplier
- **Two crons** (daily diff, weekly self-improve) that keep the system current without your intervention
- **One Telegram message per cron** so you know it's working

## What you get on day 30

- A `~/.hermes/pattern-use.log` with ~200 entries (≈ 7 patterns/day × 30)
- Your **top 5 patterns** (the actual 50x force-multipliers) identified by data, not opinion
- **3+ dead patterns** pruned (you've learned what doesn't work for your style)
- **1+ emerging patterns** captured and promoted (you're inventing your own)
- A measurable productivity delta: tasks complete in fewer steps, fewer re-dos, more shipped

---

## Why this works (the actual 50x mechanism)

A patterns file **alone** gives you maybe 2x. The 50x comes from the loop:

1. **Auto-load** (AGENTS.md enforcement) — patterns are consulted on every turn, not when you remember to look
2. **Pre-load by task type** — the right patterns are ready before the agent even starts
3. **Explicit application** — the agent announces which patterns it used, so you can see the multiplier
4. **Measurement** — every application is logged; you can prove the multiplier
5. **Self-improve** — the weekly cron prunes dead patterns and promotes emerging ones; the system gets sharper every week
6. **Daily update** — the 18 watch repos get re-diffed; new patterns get added; the library never goes stale

That's not 50 templates. That's **one flywheel** that compounds. After 90 days, the agent knows your style better than a 5-person team because the log has captured every successful and failed application.

---

## The 50 patterns at a glance

| Group | Patterns | Source repos |
|---|---|---|
| Twitter Research | P01–P06 | TwitterResearcherMyHermesAgent |
| Daily Hermes | P07–P11 | MyHermesResearcher |
| 10x Growth | P12–P18 | AslamTheEliteLeader |
| Employee Manifesto | P19–P20 | MyDayWorking |
| Daily Working Space | P21–P24 | Daily-Working-Space |
| Skill Bundles | P25–P28 | CodingDeveloperRules |
| UltraPDFGen | P29–P30 | UltraPDFGenSkill |
| Ebook Pipeline | P31–P34 | Ebook_EntireVibePipepline |
| Company Orchestration | P35–P38 | company-orchestration |
| VentureHQ | P39–P41 | VentureHQ |
| Workflows Intelligence | P42–P44 | MyWorkflowsIntelligenceLayer |
| Pipeline Patterns | P45–P48 | content-pipeline, research-feed, Content-Generation-Collab |
| Cross-cutting | P49–P50 | Quantum-Learning-Collab, HermesOracleVPS |

Full text in [`50x-PATTERNS-LIBRARY.md`](./50x-PATTERNS-LIBRARY.md).

---

## Files in this folder (the 50x system, not 50 templates)

```
WatchRepos-HermesDailyLearnings/
├── README.md                       ← you are here (replaced by 50x-QUICKSTART below)
├── 50x-QUICKSTART.md               ← the 6 commands + the loop diagram
├── 50x-PATTERNS-LIBRARY.md         ← 50 patterns (P01–P50), the core asset
├── 50x-AGENTS-MD-PATCH.md          ← runtime enforcement to append to AGENTS.md
├── DAILY-DIFF-PLAYBOOK.md          ← how the daily cron re-distills
├── Workflow01-…Workflow10-…md      ← kept as reference (delete if you want only the 50x)
└── watchrepos-index/               ← per-repo excerpts (used by the daily distiller)
```

The 10 `Workflow0X-*.md` files and 18 `watchrepos-index/*.md` files are **reference material** that the daily cron uses. They are NOT templates the agent reads at runtime. The agent reads exactly **one** file at runtime: `50x-PATTERNS-LIBRARY.md`.

---

## Verifying the 50x is real

After 7 days:

```bash
# 1. Count applications
wc -l ~/.hermes/pattern-use.log

# 2. Top 5 patterns
awk -F'|' 'NR>0 {gsub(/^ +| +$/,"",$2); print $2}' ~/.hermes/pattern-use.log | \
    sort | uniq -c | sort -rn | head -5

# 3. Success rate
grep -c '| helped' ~/.hermes/pattern-use.log
grep -c '| neutral' ~/.hermes/pattern-use.log
grep -c '| harmful' ~/.hermes/pattern-use.log

# 4. Patterns that helped more than 80% of the time = your real 50x
awk -F'|' '{
  gsub(/^ +| +$/,"",$2); gsub(/^ +| +$/,"",$4);
  total[$2]++; if ($4=="helped") helped[$2]++
}
END {
  for (p in total) {
    rate = helped[p]/total[p]
    if (rate >= 0.8 && total[p] >= 3) printf "%s  %d/%d  %.0f%%\n", p, helped[p], total[p], rate*100
  }
}' ~/.hermes/pattern-use.log | sort -k3 -t' ' -nr | head -10
```

Patterns that show up with ≥ 80% help-rate and ≥ 3 applications are your **real** 50x force-multipliers. Everything else is noise.

---

**End of 50x-QUICKSTART.md** — the whole system, one file, 50x by next Sunday.
