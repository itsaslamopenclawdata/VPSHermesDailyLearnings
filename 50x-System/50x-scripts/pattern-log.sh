#!/usr/bin/env bash
# pattern-log.sh — Friction-free logging of pattern applications
# Usage:
#   pattern-log.sh P## <task-slug> <outcome> [notes]
# Outcomes: helped | neutral | harmful | planned
# Examples:
#   pattern-log.sh P04 launch-quantum-mvp helped "saved 2h of pipeline design"
#   pattern-log.sh P18 habit-coach harmful "muted the chat"
set -euo pipefail

LOG="$HOME/.hermes/pattern-use.log"
PID="${1:?Usage: pattern-log.sh P## <task-slug> <outcome> [notes]}"
TASK="${2:?task slug required (e.g. 'launch-quantum-mvp')}"
OUT="${3:?outcome required (helped|neutral|harmful|planned)}"
NOTES="${4:-}"
TS="$(date -Iseconds)"

# Validate outcome
case "$OUT" in
  helped|neutral|harmful|planned) ;;
  *) echo "Invalid outcome: $OUT (must be helped|neutral|harmful|planned)" >&2; exit 1 ;;
esac

# Validate pattern id format
if ! [[ "$PID" =~ ^P[0-9]{2}$ ]] && [ "$PID" != "RETIRED" ] && [ "$PID" != "PROMOTED" ] && [ "$PID" != "SESSION_END" ]; then
  echo "Invalid pattern id: $PID (must be P##, RETIRED, PROMOTED, or SESSION_END)" >&2; exit 1
fi

# Append the entry
if [[ -n "$NOTES" ]]; then
  printf "%s | %s | %s | %s | %s\n" "$TS" "$PID" "$TASK" "$OUT" "$NOTES" >> "$LOG"
else
  printf "%s | %s | %s | %s\n" "$TS" "$PID" "$TASK" "$OUT" >> "$LOG"
fi

# Show the appended line
tail -1 "$LOG"

# Also show the running total
TOTAL=$(wc -l < "$LOG")
echo "(log now has $TOTAL entries)"
