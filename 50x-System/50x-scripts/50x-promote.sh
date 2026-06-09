#!/usr/bin/env bash
# 50x-promote.sh — Promote an emerging pattern to the canonical library
# Usage:
#   50x-promote.sh <emerging-pattern-name>
# The pattern must exist in ~/.hermes/emerging-patterns.md
set -euo pipefail

EMERGING="$HOME/.hermes/emerging-patterns.md"
PATTERNS_LIB="${PATTERNS_LIB:-$HOME/.hermes/profiles/default/references/50x-patterns.md}"
AGENTS_MD="$HOME/.hermes/profiles/default/AGENTS.md"
LOG="$HOME/.hermes/pattern-use.log"

NAME="${1:?Usage: 50x-promote.sh <emerging-pattern-name>}"
TODAY=$(date -I)

if [ ! -f "$EMERGING" ]; then
  echo "No emerging patterns file at $EMERGING"
  exit 1
fi

# Find the pattern block
PATTERN=$(awk "/^## \"$NAME\"/,/^## \"[^\"]+\"/ { print; if (/^## \"/ && !/^## \"$NAME\"/) exit }" "$EMERGING")

if [ -z "$PATTERN" ]; then
  echo "Pattern '$NAME' not found in $EMERGING"
  echo "Available patterns:"
  grep '^## ' "$EMERGING" | head -10
  exit 1
fi

# Validate the 7 required fields are present
for field in "Source" "When" "What" "How" "Verify" "Dead signal"; do
  if ! echo "$PATTERN" | grep -q "$field"; then
    echo "Missing field: $field. Cannot promote."
    exit 2
  fi
done
echo "✓ All 7 required fields present"

# Determine the next P## number
if [ -f "$PATTERNS_LIB" ]; then
  LAST_P=$(grep -oE "P[0-9]{2}" "$PATTERNS_LIB" | sort -u | tail -1)
  NEXT_P=$(printf "P%02d" $((10#${LAST_P#P} + 1)))
else
  echo "Pattern library not found at $PATTERNS_LIB. Create it first."
  exit 3
fi
echo "Assigning $NEXT_P"

# Append to the library
{
  echo ""
  echo "### $NEXT_P — $NAME (promoted from emerging $TODAY)"
  echo ""
  echo "$PATTERN"
  echo ""
} >> "$PATTERNS_LIB"

# Remove from emerging
awk -v name="$NAME" '
  /^## "/ { keep = !($0 ~ "\""name"\"") }
  !/^## "/ || keep { print }
' "$EMERGING" > "${EMERGING}.tmp" && mv "${EMERGING}.tmp" "$EMERGING"

# Log the promotion
TS=$(date -Iseconds)
echo "$TS | PROMOTED | $NAME -> $NEXT_P" >> "$LOG"

echo ""
echo "✓ Promoted '$NAME' to $NEXT_P"
echo "✓ Added to $PATTERNS_LIB"
echo "✓ Removed from $EMERGING"
echo ""
echo "Next: edit $AGENTS_MD to add $NEXT_P to the pre-load table for the relevant task type."
