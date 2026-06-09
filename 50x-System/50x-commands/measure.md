# /measure — Show pattern usage metrics

The user invoked /measure with period=<period> (default: 7d)

## Step 1: Filter the log
```bash
LOG="$HOME/.hermes/pattern-use.log"
PERIOD="${1:-7d}"
case "$PERIOD" in
  today)  SINCE="today" ;;
  7d)     SINCE="7 days ago" ;;
  30d)    SINCE="30 days ago" ;;
  all)    SINCE="all" ;;
  *)      SINCE="7 days ago" ;;
esac
if [ "$SINCE" != "all" ]; then
  SINCE_TS=$(date -d "$SINCE" -Iseconds)
  awk -F'|' -v since="$SINCE_TS" '$1 >= since' "$LOG" > /tmp/measure-input.log
else
  cat "$LOG" > /tmp/measure-input.log
fi
```

## Step 2: Compute M1-M5

### M1 — Application rate
- Total: `wc -l < /tmp/measure-input.log`
- Per day: total / 7 (for 7d) or total / 30 (for 30d)

### M2 — Top 5 patterns
- For each P##, count outcomes (helped, neutral, harmful)
- Rank by helped count

### M3 — Dead patterns
- Patterns with ≥ 3 harmful in window

### M4 — Emerging patterns
- Count entries in ~/.hermes/emerging-patterns.md

### M5 — Productivity delta
- helped_count × 15 min = minutes saved
- vs. baseline (30 min/week for 7d, 120 min for 30d)

## Step 3: Output the dashboard

```markdown
# 50x Dashboard — Period: <period>

## Headline
- **Productivity delta: <N>×** (target: 5× by day 30, 50× by day 90)
- **Pattern applications: <N>**
- **Top helper: P## (<name>)** — <N> helped, <N> harmful
- **Retirees this period: <N>** (P##, P##, ...)

## M1 — Application rate
- Total: <N>
- Per day: <N.N>
- Trend: <↑/↓/→> vs previous period

## M2 — Top 5 patterns
| Pattern | Helped | Neutral | Harmful |
|---|---|---|---|
| P## | X | X | X |

## M3 — Dead patterns (≥ 3 harmful)
- P## — <N> harmful

## M4 — Emerging patterns
- <N> entries in ~/.hermes/emerging-patterns.md

## M5 — Productivity delta
- Helped applications: <N>
- Min saved: <N> (<H> hours)
- Baseline: <B> min
- Delta: <D>×

## Recommendations
1. <action 1>
2. <action 2>
```
