# AGENTS.md Patch — Force 50x Pattern Loading

> **What this is:** The exact text to add to your existing `~/.hermes/profiles/quantum-venture-lab/AGENTS.md` (or any other profile) so that the agent **auto-loads and applies the 50x patterns** on every turn.
> **How to install:** `cat 50x-AGENTS-MD-PATCH.md >> ~/.hermes/profiles/quantum-venture-lab/AGENTS.md`
> **Reversible:** Delete the section if you don't want it.

---

## Patch text (append verbatim to your existing AGENTS.md)

```markdown
---

## 50x Pattern Enforcement (mandatory)

You have access to **50 proven patterns** distilled from 18 watch repos. They live at:
`~/.hermes/profiles/<this-profile>/references/50x-patterns.md`

### Rule 1: Load on every turn
At the start of every non-trivial task, open that file and scan the index (P01–P50) for applicable patterns. Apply the **top 3 highest-leverage** ones before responding.

### Rule 2: Apply explicitly
When you apply a pattern, mention it in your response:
> "Applied: P29 (UltraPDFGen 28-specialist pattern), P32 (5-stage pipeline)"

### Rule 3: Log every application
After every applied pattern, append a line to `~/.hermes/pattern-use.log`:
```
<ISO8601> | <pattern_id> | <task_slug> | <outcome: helped|neutral|harmful>
```
This is the **measurement** that makes 50x provable. Without it, you're just hoping.

### Rule 4: Skip the load for trivial tasks
If the task is < 3 steps (e.g. "what time is it", "fix this typo", "summarize this 1-paragraph email"), skip the pattern scan. The overhead would slow you down.

### Rule 5: Pre-load these for known task types
When the task matches a known type, **pre-load** the relevant patterns without scanning:

| Task type | Pre-loaded patterns |
|---|---|
| Writing content (tweet, blog, email) | P04, P39, P47 |
| Building a product (spec → ship) | P31, P32, P33, P34 |
| Evaluating a venture idea | P40, P41, P46 |
| Researching a topic | P13, P14, P42, P43, P44 |
| Multi-agent coordination | P01, P02, P25, P28, P35, P37, P38 |
| Knowledge/learning | P14, P49, P50 |
| Daily ops | P07, P20, P21, P22, P23, P48 |
| Personal productivity | P03, P12, P15, P18, P19 |

### Rule 6: At end of every session, output a pattern-use summary
Append to `~/.hermes/pattern-use.log`:
```
<ISO8601> | SESSION_END | patterns_applied=[P01,P04,...] | top_helper=P## | dead_patterns=[P##,...]
```

### Rule 7: When you invent a new pattern, capture it
If during a task you find yourself doing something repeatable that isn't in the 50x library, write it to `~/.hermes/emerging-patterns.md` with the same structure (name, source, when, what, how, verify, dead signal). The Sunday self-improve cron will promote it into the library.

### Rule 8: When a pattern fails 3 times in a row, mark it dead
If `~/.hermes/pattern-use.log` shows the same pattern_id with outcome=harmful 3 times in 7 days, that pattern is misaligned with your style. Add it to `~/.hermes/dead-patterns.txt`. The Sunday self-improve cron will retire it.

---

## Where the patterns came from

| Pattern group | Source repos | Count |
|---|---|---|
| Twitter Research (P01–P06) | TwitterResearcherMyHermesAgent | 6 |
| Daily Hermes (P07–P11) | MyHermesResearcher | 5 |
| 10x Growth (P12–P18) | AslamTheEliteLeader | 7 |
| Employee Manifesto (P19–P20) | MyDayWorking | 2 |
| Daily Working Space (P21–P24) | Daily-Working-Space | 4 |
| Skill Bundles (P25–P28) | CodingDeveloperRules | 4 |
| UltraPDFGen (P29–P30) | UltraPDFGenSkill | 2 |
| Ebook Pipeline (P31–P34) | Ebook_EntireVibePipepline | 4 |
| Company Orchestration (P35–P38) | company-orchestration | 4 |
| VentureHQ (P39–P41) | VentureHQ | 3 |
| Workflows Intelligence (P42–P44) | MyWorkflowsIntelligenceLayer | 3 |
| Pipeline Patterns (P45–P48) | content-pipeline, research-feed, Content-Generation-Collab, Daily-Working-Space | 4 |
| Cross-cutting (P49–P50) | Quantum-Learning-Collab, HermesOracleVPS | 2 |
| **Total** | **18 repos** | **50** |

---

## Verification

After 7 days of running, you should see:
- `~/.hermes/pattern-use.log` has ≥ 50 entries (≈ 7 patterns/day)
- Top 5 most-applied patterns identified (these are your 50x force-multipliers)
- ≥ 1 pattern marked dead (you've learned what doesn't work for you)
- ≥ 1 pattern in `emerging-patterns.md` (you've started inventing your own)
- A measurable productivity delta: tasks complete in fewer steps, fewer re-dos, more shipped
```

---

## What this patch does

Before this patch, the 50 patterns are just **documentation** — they sit in a file that the agent never reads.

After this patch:
1. The agent **scans the pattern index** on every non-trivial turn
2. **Pre-loads** the right patterns for known task types
3. **Logs every application** to `~/.hermes/pattern-use.log`
4. **Captures emerging patterns** when it invents new ones
5. **Retires dead patterns** when they fail repeatedly

This converts the patterns from "nice to have" to **operational primitives that the agent uses on every turn**. That's where the 50x comes from — not the patterns themselves, but the **forced application + measurement loop**.

---

## One-time install (5 commands)

```bash
# 1. Download the pattern library to your profile
mkdir -p ~/.hermes/profiles/quantum-venture-lab/references
cp 50x-PATTERNS-LIBRARY.md ~/.hermes/profiles/quantum-venture-lab/references/50x-patterns.md

# 2. Append the patch to your AGENTS.md
cat 50x-AGENTS-MD-PATCH.md >> ~/.hermes/profiles/quantum-venture-lab/AGENTS.md

# 3. Initialize the log files
touch ~/.hermes/pattern-use.log
touch ~/.hermes/emerging-patterns.md
touch ~/.hermes/dead-patterns.txt

# 4. (Optional) Verify the install
ls -la ~/.hermes/pattern-use.log ~/.hermes/profiles/quantum-venture-lab/references/50x-patterns.md
wc -l ~/.hermes/pattern-use.log

# 5. Start a new session
hermes -p quantum-venture-lab
# Try: "Plan a 7-day launch of a quantum-portfolio-optimizer MVP"
# The agent should auto-load P31, P32, P33, P34, P40, P41 and log the application
```

---

## Daily cadence (already aligns with Workflow 03 from the Quantum Venture Lab)

- **Every turn:** Apply patterns + log
- **Every morning 07:00:** `/measure` — show last 24h pattern usage
- **Sunday 20:00:** Self-improve cron — prune dead, promote emerging, log metrics

---

**End of 50x-AGENTS-MD-PATCH.md**
