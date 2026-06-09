#!/usr/bin/env bash
# 50x-measure.sh — Compute the 50x dashboard from the pattern-use.log
# Usage:
#   50x-measure.sh [period]
# Period: today | 7d | 30d | all (default: 7d)
set -euo pipefail

LOG="$HOME/.hermes/pattern-use.log"
DEAD="$HOME/.hermes/dead-patterns.txt"
EMERGING="$HOME/.hermes/emerging-patterns.md"
RETIRED="$HOME/.hermes/retired-patterns.md"
PATTERNS_LIB="${PATTERNS_LIB:-$HOME/.hermes/profiles/default/references/50x-patterns.md}"

PERIOD="${1:-7d}"
case "$PERIOD" in
  today)  SINCE="today" ;;
  7d)     SINCE="7 days ago" ;;
  30d)    SINCE="30 days ago" ;;
  all)    SINCE="all" ;;
  *) echo "Invalid period: $PERIOD (today|7d|30d|all)" >&2; exit 1 ;;
esac

if [ ! -f "$LOG" ]; then
  echo "No log file at $LOG. Run pattern-log.sh at least once first."
  exit 0
fi

# Filter by period
if [ "$SINCE" != "all" ]; then
  SINCE_TS=$(date -d "$SINCE" -Iseconds 2>/dev/null || date -Iseconds)
  FILTERED=$(awk -F'|' -v since="$SINCE_TS" '$1 >= since' "$LOG")
else
  FILTERED=$(cat "$LOG")
fi

# Total applications
TOTAL=$(echo "$FILTERED" | grep -c '|' || echo 0)
TODAY=$(date -I)

echo "# 50x Dashboard — Period: $PERIOD (since $SINCE)"
echo ""
echo "## Headline"
echo "- **Total applications:** $TOTAL"
echo "- **Today:** $(echo "$FILTERED" | grep -c "$TODAY" || echo 0)"
echo "- **Log file:** $LOG ($TOTAL lines total)"
echo ""

# Top patterns by helped count
echo "## Top patterns (by helped count)"
echo "$FILTERED" | awk -F'|' '
  /helped/ { helped[$2]++ }
  /neutral/ { neutral[$2]++ }
  /harmful/ { harmful[$2]++ }
  END {
    for (p in helped) print helped[p], "helped,", neutral[p]+0, "neutral,", harmful[p]+0, "harmful,", p
  }
' | sort -rn | head -10 | awk '{printf "| %s | %s | %s | %s |\n", $7, $1, $3, $5}'
echo ""

# Dead patterns (≥ 3 harmful in period)
echo "## Dead patterns (≥ 3 harmful in $PERIOD)"
echo "$FILTERED" | awk -F'|' '
  /harmful/ { count[$2]++ }
  END {
    for (p in count) if (count[p] >= 3) print p, "(" count[p] " harmful)"
  }
' | sort
echo ""

# Emerging
echo "## Emerging patterns (from $EMERGING)"
if [ -f "$EMERGING" ]; then
  EMERGING_COUNT=$(grep -c '^## ' "$EMERGING" 2>/dev/null || echo 0)
  echo "Count: $EMERGING_COUNT"
  grep '^## ' "$EMERGING" | head -5
else
  echo "(no emerging patterns file)"
fi
echo ""

# Retired
echo "## Retired patterns (from $DEAD)"
if [ -f "$DEAD" ]; then
  cat "$DEAD" | tail -10
else
  echo "(no retired patterns file)"
fi
echo ""

# Productivity delta (rough estimate)
echo "## Productivity delta (rough estimate)"
HELPED_COUNT=$(echo "$FILTERED" | grep -c 'helped' || echo 0)
# Avg 15 min saved per helped application
MIN_SAVED=$((HELPED_COUNT * 15))
HOURS_SAVED=$((MIN_SAVED / 60))
echo "Helped applications: $HELPED_COUNT"
echo "Estimated minutes saved: $MIN_SAVED ($HOURS_SAVED hours)"
echo "Baseline (no patterns): ~30 min/week of agent useful work"
if [ $HOURS_SAVED -gt 0 ] && [ "$PERIOD" != "today" ]; then
  BASELINE_MIN=120  # 30 min × 4 weeks for 30d, or 30 min for 7d
  if [ "$PERIOD" = "30d" ]; then BASELINE_MIN=$((30 * 4)); fi
  DELTA=$(awk "BEGIN { printf \"%.1f\", $MIN_SAVED / $BASELINE_MIN }")
  echo "Productivity delta: ${DELTA}×"
fi
