# /promote — Promote an emerging pattern to the library

The user invoked /promote <emerging-pattern-name>

## Step 1: Run the promotion
```bash
~/.hermes/bin/50x-promote.sh <name>
```

This script:
1. Finds the pattern in ~/.hermes/emerging-patterns.md
2. Validates the 7 required fields
3. Assigns the next P## number
4. Appends to ~/.hermes/profiles/quantum-venture-lab/references/50x-patterns.md
5. Removes from emerging-patterns.md
6. Logs the promotion

## Step 2: Output
```
## Promotion result
- Pattern '<name>' → P##
- ✓ Added to 50x-patterns.md
- ✓ Removed from emerging-patterns.md
- Next: edit AGENTS.md to add P## to the pre-load table
```
