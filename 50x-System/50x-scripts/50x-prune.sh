#!/usr/bin/env bash
# 50x-prune.sh — Identify and retire dead patterns
# Usage:
#   50x-prune.sh [--dry-run] [--window=7d]
set -euo pipefail

LOG="$HOME/.hermes/pattern-use.log"
DEAD="$HOME/.hermes/dead-patterns.txt"
RETIRED="$HOME/.hermes/retired-patterns.md"
PATTERNS_LIB="${PATTERNS_LIB:-$HOME/.hermes/profiles/default/references/50x-patterns.md}"
AGENTS_MD="$HOME/.hermes/profiles/default/AGENTS.md"
DRY_RUN=false
WINDOW="7 days ago"

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    --window=*) WINDOW="${arg#*=}" ;;
  esac
done

if [ ! -f "$LOG" ]; then
  echo "No log file at $LOG"
  exit 0
fi

# Filter to window
SINCE_TS=$(date -d "$WINDOW" -Iseconds 2>/dev/null || date -Iseconds)
FILTERED=$(awk -F'|' -v since="$SINCE_TS" '$1 >= since' "$LOG")

# Find patterns with ≥ 3 harmful in window
DEAD_PATTERNS=$(echo "$FILTERED" | awk -F'|' '
  /harmful/ { count[$2]++ }
  END {
    for (p in count) if (count[p] >= 3) print p, count[p]
  }
')

if [ -z "$DEAD_PATTERNS" ]; then
  echo "No patterns meet the retirement threshold (≥ 3 harmful in $WINDOW)."
  exit 0
fi

echo "Retirement candidates:"
echo "$DEAD_PATTERNS" | while read pid harmful_count; do
  echo "  $pid — $harmful_count harmful"
done

if $DRY_RUN; then
  echo ""
  echo "(dry-run mode: no changes made. Re-run without --dry-run to execute.)"
  exit 0
fi

# Execute retirement
echo ""
echo "Retiring..."
echo "$DEAD_PATTERNS" | while read pid harmful_count; do
  TODAY=$(date -I)
  # Append to dead-patterns.txt
  echo "$pid  $TODAY  $harmful_count harmful in $WINDOW" >> "$DEAD"
  # Move to retired-patterns.md
  if [ -f "$PATTERNS_LIB" ]; then
    PATTERN_BLOCK=$(awk "/^### $pid —/,/^### P[0-9]/ { print; if (/^### P[0-9]/ && !/^### $pid/) exit }" "$PATTERNS_LIB")
    if [ -n "$PATTERN_BLOCK" ]; then
      {
        echo ""
        echo "## $pid — RETIRED on $TODAY"
        echo ""
        echo "$PATTERN_BLOCK"
        echo ""
        echo "**Reason for retirement:** $harmful_count harmful in $WINDOW"
        echo ""
      } >> "$RETIRED"
    fi
  fi
  # Remove from AGENTS.md pre-load table (basic sed)
  if [ -f "$AGENTS_MD" ]; then
    # Remove the row containing this pattern in the pre-load table
    sed -i.bak "/$pid/d" "$AGENTS_MD"
  fi
  # Log the retirement
  TS=$(date -Iseconds)
  echo "$TS | RETIRED | $pid | $harmful_count harmful in $WINDOW" >> "$LOG"
  echo "  ✓ retired $pid"
done

echo ""
echo "Done. See $DEAD for the list. Run /measure to see the updated dashboard."
