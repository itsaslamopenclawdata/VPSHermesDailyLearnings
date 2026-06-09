# /apply-pattern — Apply a single named pattern

The user invoked /apply-pattern with: P## <task>

## Step 1: Load the pattern
Read the P## entry in ~/.hermes/profiles/default/references/50x-patterns.md. Extract:
- When (trigger condition)
- What (description)
- How (the recipe)
- Verify (how to know it worked)

## Step 2: Apply
Execute the "How" section step-by-step against the user's task.

## Step 3: Output the result
```
## Pattern: P## — <name>

## When applied
<restate the trigger condition and confirm it matches>

## How applied
<the actual steps you took>

## Result
<the output / artifact / state change>

## Log
~/.hermes/bin/pattern-log.sh P## <task-slug> applied
```

## Step 4: Log
Run `~/.hermes/bin/pattern-log.sh P## <task-slug> applied` at the end.
