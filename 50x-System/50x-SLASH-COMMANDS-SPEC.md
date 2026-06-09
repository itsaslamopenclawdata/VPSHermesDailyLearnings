# 50x Slash Commands — Spec for Quantum Venture Lab Profile

> **What this is:** 5 new slash commands that make the 50x patterns **invokable on demand** from any chat session (Telegram, CLI, web).
> **How to install:** Run the `hermes slash-command install` commands at the bottom of this file.
> **Composable:** Each command can be combined with the existing 11 commands from the Quantum Venture Lab.

---

## The 5 commands

### `/50x <task>` — Apply 50x patterns to a task

**Purpose:** Take any task description and produce a 50x-patterned plan + execution.

**Syntax:** `/50x <free-form task description>`

**What it does:**
1. Scans the 50x pattern library for applicable patterns
2. Pre-loads the top 3 highest-leverage patterns for this task type
3. Outputs a structured plan with: Patterns applied, Step-by-step execution, Expected outcome
4. Logs the application to `~/.hermes/pattern-use.log`

**Example invocations:**

```
/50x Plan a 7-day launch of a quantum-portfolio-optimizer MVP
/50x Write a tweet thread on post-quantum cryptography
/50x Evaluate this idea: AI-powered NDA review for $5K/month
/50x Set up a daily intelligence pipeline for my 3 businesses
```

**Behind-the-scenes prompt template:**

```markdown
The user invoked /50x with: <task>.

Step 1: Read ~/.hermes/profiles/<this-profile>/references/50x-patterns.md
Step 2: Identify the task type (writing, building, evaluating, researching, coordinating, etc.)
Step 3: From the pre-load table in 50x-AGENTS-MD-PATCH.md, select the relevant patterns
Step 4: For each pre-loaded pattern, extract the "How" section
Step 5: Compose a plan that integrates the top 3 patterns
Step 6: Output:
   ## Patterns applied: P##, P##, P##
   ## Plan
   <step-by-step>
   ## Expected outcome
   <measurable result>
   ## Log entry
   <ISO8601> | P##,P##,P## | <task-slug> | planned
Step 7: Append the log entry to ~/.hermes/pattern-use.log
```

---

### `/apply-pattern <P##> <task>` — Apply one specific pattern

**Purpose:** Force the application of a single named pattern.

**Syntax:** `/apply-pattern P## <task description>`

**What it does:**
1. Loads only the requested pattern
2. Applies it to the task
3. Logs the application

**Example invocations:**

```
/apply-pattern P29 Write a 10-chapter ebook on quantum computing
/apply-pattern P40 Evaluate: "AI agent for legal contract review at $3K/month"
/apply-pattern P04 Set up a content pipeline for my SaaS
```

**Behind-the-scenes prompt:**

```markdown
The user invoked /apply-pattern with: P## <task>.

Step 1: Read the P## entry in 50x-patterns.md
Step 2: Apply the "How" section step-by-step
Step 3: Output the result
Step 4: Log:
   <ISO8601> | P## | <task-slug> | applied
```

---

### `/measure` — Show pattern usage metrics

**Purpose:** See which patterns are working and which aren't.

**Syntax:** `/measure [period]`

**Periods:** `today`, `7d`, `30d`, `all` (default: 7d)

**What it does:**
1. Reads `~/.hermes/pattern-use.log`
2. Computes: total applications, top-5 most-applied, dead patterns (3+ harmful), emerging patterns, productivity delta estimate
3. Outputs a markdown report

**Example output:**

```markdown
# Pattern Usage — Last 7 days

Total applications: 47
Top 5 most-applied:
  P04 (Pain-extract pipeline): 12
  P07 (Daily standup): 10
  P21 (BRAIN.md): 8
  P32 (5-stage publish): 6
  P01 (AGENT_SKILLS_MATRIX): 5

Dead patterns (≥ 3 harmful in 7d):
  P18 (Habit coach) — 4 harmful, 1 helpful
  P16 (Communication automation) — 3 harmful, 0 helpful

Emerging patterns (from ~/.hermes/emerging-patterns.md):
  - "When the user says 'quick question', defer pattern loading" (added 2026-06-04)

Productivity delta estimate: 4.2× vs baseline
  (based on: avg 47 patterns × ~3 min saved per application = 141 min/week)

Recommendation: retire P18, P16. Promote emerging pattern to library.
```

**Behind-the-scenes prompt:**

```markdown
The user invoked /measure with period=<period>.

Step 1: Read ~/.hermes/pattern-use.log
Step 2: Filter to <period>
Step 3: Group by pattern_id
Step 4: Count outcome frequencies
Step 5: Identify dead patterns (≥ 3 harmful in window)
Step 6: Read ~/.hermes/emerging-patterns.md and ~/.hermes/dead-patterns.txt
Step 7: Output the report
```

---

### `/prune` — Retire dead patterns

**Purpose:** Clean up the pattern library by retiring patterns that consistently fail.

**Syntax:** `/prune [--dry-run]`

**What it does:**
1. Reads `~/.hermes/pattern-use.log` and `~/.hermes/dead-patterns.txt`
2. Identifies patterns with ≥ 3 harmful outcomes in 7 days
3. Moves them to `~/.hermes/retired-patterns.md` (archive, don't delete)
4. Removes them from the active pre-load table in AGENTS.md
5. Sends a Telegram summary

**Behind-the-scenes prompt:**

```markdown
The user invoked /prune [--dry-run].

Step 1: Read ~/.hermes/pattern-use.log
Step 2: For each pattern_id, count harmful outcomes in last 7 days
Step 3: List candidates (≥ 3 harmful)
Step 4: If --dry-run, just output the list. Else:
   - Move each to ~/.hermes/retired-patterns.md with date and reason
   - Remove from pre-load table in AGENTS.md
   - Add to ~/.hermes/dead-patterns.txt
Step 5: Output summary
```

---

### `/promote` — Promote emerging patterns to the library

**Purpose:** Add a pattern from `emerging-patterns.md` to the canonical 50x library.

**Syntax:** `/promote <pattern-name>`

**What it does:**
1. Reads the emerging pattern from `~/.hermes/emerging-patterns.md`
2. Validates: has all 7 required fields (name, source, when, what, how, verify, dead signal)
3. Adds to the canonical 50x-patterns.md with a new number (P51, P52, ...)
4. Adds to the pre-load table in AGENTS.md
5. Logs the promotion

**Behind-the-scenes prompt:**

```markdown
The user invoked /promote <name>.

Step 1: Find the pattern in ~/.hermes/emerging-patterns.md
Step 2: Validate the 7 fields
Step 3: If invalid, return the missing fields and exit
Step 4: Assign the next P## number (P51, P52, ...)
Step 5: Append to ~/.hermes/profiles/<profile>/references/50x-patterns.md
Step 6: Update the index table at the top
Step 7: Update the pre-load table in AGENTS.md
Step 8: Remove from emerging-patterns.md
Step 9: Log: <ISO8601> | PROMOTED | <name> -> P##
```

---

## How to install

These are **prompt-based slash commands** — no code needed. Run from the CLI:

```bash
# /50x
hermes slash-command install --name "50x" --prompt "$(cat /tmp/fifty_x/commands/50x.md)"

# /apply-pattern
hermes slash-command install --name "apply-pattern" --prompt "$(cat /tmp/fifty_x/commands/apply-pattern.md)"

# /measure
hermes slash-command install --name "measure" --prompt "$(cat /tmp/fifty_x/commands/measure.md)"

# /prune
hermes slash-command install --name "prune" --prompt "$(cat /tmp/fifty_x/commands/prune.md)"

# /promote
hermes slash-command install --name "promote" --prompt "$(cat /tmp/fifty_x/commands/promote.md)"

# Verify
hermes slash-command list | grep -E "50x|apply-pattern|measure|prune|promote"
```

> If `hermes slash-command install` doesn't exist in your version, add the prompts as **custom skills** instead. Each command is a one-prompt skill; the slash command is just a thin wrapper.

---

## Alternative install (skill-based)

If slash commands aren't supported, register each as a skill:

```bash
mkdir -p ~/.hermes/profiles/default/skills/{fifty-x,apply-pattern,measure-patterns,prune-patterns,promote-patterns}

# /50x → fifty-x skill
cat > ~/.hermes/profiles/default/skills/fifty-x/SKILL.md <<'EOF'
---
name: fifty-x
description: "Apply 50x patterns to any task. Trigger: /50x <task>"
---
[paste the /50x prompt template from above]
EOF

# repeat for the other 4...
```

Then load with `/skill fifty-x` in any session.

---

## Composing with existing Quantum Venture Lab commands

The 5 new commands **stack** with the existing 11:

```
/qlearn bell-state        → uses 50x patterns P49 (knowledge-base-first) + P14 (auto-notes)
/qpaper <arxiv-id>        → uses P43 (insight extraction) + P14
/qidea quantum-finance    → uses P04 (pain-extract pipeline) + P15 (opportunity scanner) + P40 (venturescore)
/qvalidate <idea>         → uses P40 + P41 (20-agent evaluation)
/qmvp <spec>              → uses P31 + P32 + P33 + P34 (schema → pipeline → CI/CD → tests)
/qship <mvp>              → uses P33 (CI/CD) + P36 (Method 0 pricing)
/50x <task>               → free-form; auto-selects the right patterns
/measure                  → shows you which patterns are helping
```

**The /50x command is the meta-command.** Use it when you don't know which existing slash command to invoke.

---

**End of 50x-SLASH-COMMANDS-SPEC.md**
