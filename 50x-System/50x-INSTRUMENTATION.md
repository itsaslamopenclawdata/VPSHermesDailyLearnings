# 50x Instrumentation — Measurement That Proves 50x

> **Why this exists:** Without measurement, "50×" is a slogan. With it, it's a number.
> **What this is:** The instrumentation spec — the log format, the metrics, the dashboard.
> **One-time setup:** 5 commands (below). After that, the system runs itself.

---

## The 3 log files

All three live under `~/.hermes/`:

### 1. `pattern-use.log` — every application recorded

**Format:** `<ISO8601> | <pattern_id> | <task_slug> | <outcome> | <notes>`

**Example entries:**
```
2026-06-03T07:14:22+05:30 | P04 | launch-quantum-portfolio-mvp | helped | "saved 2 hours of pipeline design"
2026-06-03T08:30:00+05:30 | P13 | daily-learning-digest | helped | "3 papers extracted, all relevant"
2026-06-03T09:15:45+05:30 | P18 | habit-coach-morning | harmful | "Muted the chat, this is noise"
2026-06-03T10:00:12+05:30 | P29 | ebook-quantum-finance | helped | "10 chapters, 99/100 quality"
2026-06-03T11:30:00+05:30 | P18 | habit-coach-evening | harmful | "Muted again"
2026-06-03T14:22:18+05:30 | P40 | validate-ai-nda-review | helped | "Score 78, CONDITIONAL GO"
2026-06-03T15:00:00+05:30 | SESSION_END | patterns_applied=[P04,P13,P29,P40] | top_helper=P29 | dead_patterns=[P18]
```

**Outcome values:**
- `helped` — pattern saved time or improved quality
- `neutral` — pattern was applied but no measurable effect
- `harmful` — pattern slowed things down or was wrong for the task
- `planned` — pattern was used to plan a task, not yet executed

### 2. `emerging-patterns.md` — patterns the agent invented

**Format:** Same as 50x-patterns.md entries (name, source, when, what, how, verify, dead signal), but the source is "agent-invented" instead of a watch repo.

**Example entry:**
```markdown
## "Skip pattern load for trivial tasks"

Source: agent-invented (2026-06-04)
When: User says "quick question" or "just tell me" or task is < 3 steps
What: Bypass the 50x pattern scan; respond directly
How:
  1. Detect triggers: "quick", "just", "what is", "summarize", task < 3 steps
  2. Skip ~/.hermes/profiles/<profile>/references/50x-patterns.md read
  3. Respond directly
Verify: Trivial tasks complete in < 30s (vs 60+ s with pattern scan)
Dead signal: User says "stop skipping the patterns"
```

### 3. `dead-patterns.txt` — retired patterns

**Format:** One line per retired pattern: `<P##>  <retired-date>  <reason>`

```
P18  2026-06-10  Muted 4/4 times in 7 days. Habit coach is noise for this user.
P16  2026-06-12  3/5 times user rewrote the draft. Quality bar too low.
```

---

## Metrics (computed from the log)

### M1 — Pattern application rate
**Formula:** `count(pattern-use.log last 7d) / 7`
**Target:** ≥ 10 applications/day
**Interpretation:** Below 10 = agent isn't applying patterns. Above 50 = good adoption.

### M2 — Top 5 patterns (helped count)
**Formula:** `top 5 by helped count in last 7d`
**Target:** ≥ 3 patterns with ≥ 5 helped
**Interpretation:** These are the 50x force-multipliers. Optimize for them.

### M3 — Dead pattern count
**Formula:** `count(dead-patterns.txt) added in last 30d`
**Target:** 1-3 per month (healthy pruning)
**Interpretation:** 0 = no learning. > 5 = patterns are wrong for you.

### M4 — Emerging pattern count
**Formula:** `count(emerging-patterns.md) created in last 30d`
**Target:** ≥ 2 per month
**Interpretation:** The agent is learning your style. < 2 = not enough novelty.

### M5 — Productivity delta (the headline metric)
**Formula:** `sum(estimated_minutes_saved per helped pattern in last 7d) / baseline_minutes_per_week`
**Target:** ≥ 5× within 30 days, ≥ 50× within 90 days
**Interpretation:** The "50×" claim. If this doesn't show up here, the patterns aren't pulling weight.

Each pattern has an `estimated_minutes_saved` value (from the 50x-patterns.md multiplier column):
- 2× pattern = 5 min saved per application
- 5× pattern = 20 min saved
- 10× pattern = 45 min saved
- 50× pattern = 240 min saved

**Example calculation:**
- 7 days × 10 applications/day × avg 15 min saved = 1,050 min = 17.5 hours/week
- vs. baseline of 4 hours/week of agent work
- Productivity delta = 4.4×

---

## The 50x Dashboard

Generate this with `/measure 7d`:

```markdown
# 50x Dashboard — Last 7 days (2026-05-28 to 2026-06-03)

## Headline
- **Productivity delta: 4.4×** (target: 5× by day 30, 50× by day 90)
- **Pattern applications: 47** (target: ≥ 70/week)
- **Top helper: P29 (UltraPDFGen)** — 12 helped, 0 harmful
- **Retirees this week: 1** (P18 — habit coach)

## M1 — Application rate
- Today: 8
- 7-day average: 6.7/day
- Trend: ↑ 12% week-over-week

## M2 — Top 5 patterns
| Pattern | Helped | Neutral | Harmful | Net |
|---|---|---|---|---|
| P04 (Pain-extract pipeline) | 12 | 1 | 0 | +12 |
| P07 (Daily standup) | 10 | 0 | 0 | +10 |
| P21 (BRAIN.md) | 8 | 1 | 0 | +8 |
| P32 (5-stage publish) | 6 | 0 | 0 | +6 |
| P01 (AGENT_SKILLS_MATRIX) | 5 | 0 | 0 | +5 |

## M3 — Recently retired
- P18 (Habit coach) — 2026-06-10 — muted 4/4 times

## M4 — Emerging patterns
- "Skip pattern load for trivial tasks" (2026-06-04)
- "Pre-draft tweet hook when user mentions 'post this'" (2026-06-05)

## M5 — Productivity delta
| Week | Applications | Min saved | vs. baseline | Trend |
|---|---|---|---|---|
| 2026-05-28 | 31 | 470 | 1.9× | baseline |
| 2026-06-03 | 47 | 1,050 | 4.4× | ↑ 2.3× |

## Recommendations
1. **Promote** "Skip pattern load for trivial tasks" → P51
2. **Pre-load P04** for any task that mentions "research" or "find"
3. **Retire P18** (already done)
4. **Try** P29 on the next PDF/ebook task — it has 0 harmful outcomes

## Verification
- Log file: ~/.hermes/pattern-use.log (47 lines)
- Retired: ~/.hermes/dead-patterns.txt (1 entry)
- Emerging: ~/.hermes/emerging-patterns.md (2 entries)
- Pattern library: ~/.hermes/profiles/quantum-venture-lab/references/50x-patterns.md (50 patterns)
```

---

## The "log helper" script

A small bash script that makes logging friction-free:

`~/.hermes/bin/pattern-log.sh`:

```bash
#!/usr/bin/env bash
# Append a pattern-use entry to ~/.hermes/pattern-use.log
# Usage: pattern-log.sh P## <task-slug> <outcome> [notes]
set -euo pipefail
LOG="$HOME/.hermes/pattern-use.log"
PID="${1:?pattern id required}"
TASK="${2:?task slug required}"
OUT="${3:?outcome required (helped|neutral|harmful|planned)}"
NOTES="${4:-}"
TS="$(date -Iseconds)"
if [[ -n "$NOTES" ]]; then
  echo "$TS | $PID | $TASK | $OUT | $NOTES" >> "$LOG"
else
  echo "$TS | $PID | $TASK | $OUT" >> "$LOG"
fi
# Tail to confirm
tail -1 "$LOG"
```

Make it executable:
```bash
chmod +x ~/.hermes/bin/pattern-log.sh
```

The AGENTS.md patch can then instruct the agent:
> "After every applied pattern, run: `~/.hermes/bin/pattern-log.sh P## <task-slug> <outcome> [notes]`"

This makes logging a **single bash call** instead of a 100-character append.

---

## One-time install

```bash
# 1. Create the log files
mkdir -p ~/.hermes/bin
touch ~/.hermes/pattern-use.log
touch ~/.hermes/emerging-patterns.md
touch ~/.hermes/dead-patterns.txt

# 2. Create the log helper script
cat > ~/.hermes/bin/pattern-log.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
LOG="$HOME/.hermes/pattern-use.log"
PID="${1:?pattern id required}"
TASK="${2:?task slug required}"
OUT="${3:?outcome required (helped|neutral|harmful|planned)}"
NOTES="${4:-}"
TS="$(date -Iseconds)"
if [[ -n "$NOTES" ]]; then
  echo "$TS | $PID | $TASK | $OUT | $NOTES" >> "$LOG"
else
  echo "$TS | $PID | $TASK | $OUT" >> "$LOG"
fi
tail -1 "$LOG"
EOF
chmod +x ~/.hermes/bin/pattern-log.sh

# 3. Initialize the dashboard (empty)
cat > ~/.hermes/50x-dashboard.md <<'EOF'
# 50x Dashboard — run `/measure` to populate

(Initial state — no applications logged yet)
EOF

# 4. Verify
ls -la ~/.hermes/pattern-use.log ~/.hermes/emerging-patterns.md ~/.hermes/dead-patterns.txt ~/.hermes/50x-dashboard.md
~/.hermes/bin/pattern-log.sh TEST-INSTALL install ok
# Then delete the test line:
sed -i '/TEST-INSTALL/d' ~/.hermes/pattern-use.log
```

---

## The dashboard cron (optional)

```bash
# Daily 22:00 — generate and post the daily 50x digest
hermes cron create "0 22 * * *" \
  --name "50x-daily-measure" \
  --prompt "Generate today's 50x dashboard:

1. Read ~/.hermes/pattern-use.log and filter to today
2. Compute M1-M5
3. Append a 1-paragraph summary to ~/.hermes/50x-dashboard.md under '## YYYY-MM-DD'
4. Post a 3-bullet summary to Telegram: top helper, top harm, delta vs yesterday

Skills: file, terminal
Deliver: telegram" \
  --skills "file,terminal" \
  --deliver telegram
```

---

**End of 50x-INSTRUMENTATION.md**
