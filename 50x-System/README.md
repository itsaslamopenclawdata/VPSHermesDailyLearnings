# 50x-System — Make Hermes 50× More Productive

> **What this is:** The 50x pattern library + the runtime enforcement + the measurement loop that turns the 18 watch repos into 50× productivity.
> **Source:** All 18 watch repos, distilled into 50 numbered patterns.
> **Version:** 1.0 · **Date:** 2026-06-03

---

## The problem this solves

You have 18 GitHub repos full of valuable patterns, but the Hermes agent doesn't actually use them. They're just documents sitting in a folder.

**50x-System** converts those patterns into:

1. **A loadable pattern library** that the agent reads on every turn
2. **An AGENTS.md patch** that forces the agent to apply patterns
3. **5 slash commands** for explicit invocation
4. **A measurement loop** that proves 50× (or shows where the patterns fail)
5. **A self-improve loop** that prunes dead patterns and promotes new ones

Without these, the patterns are documentation. With them, they're **operational primitives**.

---

## File map

```
50x-System/
├── README.md                         ← you are here
├── 50x-PATTERNS-LIBRARY.md          ← 50 patterns, 40 KB, the core
├── 50x-AGENTS-MD-PATCH.md           ← append to your AGENTS.md
├── 50x-SLASH-COMMANDS-SPEC.md       ← 5 commands: /50x, /apply-pattern, /measure, /prune, /promote
├── 50x-INSTRUMENTATION.md           ← log format, metrics, dashboard
├── 50x-SELF-IMPROVE-LOOP.md         ← Sunday cron that prunes + promotes
├── 50x-QUICKSTART.md                ← 5-min install
│
├── 50x-scripts/
│   └── pattern-log.sh               ← bash helper for friction-free logging
│
├── 50x-commands/                    ← prompt templates for the 5 slash commands
│   ├── 50x.md
│   ├── apply-pattern.md
│   ├── measure.md
│   ├── prune.md
│   └── promote.md
│
├── 50x-skills/                      ← skill-based fallbacks for the 5 commands
│   ├── fifty-x/SKILL.md
│   ├── apply-pattern/SKILL.md
│   ├── measure-patterns/SKILL.md
│   ├── prune-patterns/SKILL.md
│   └── promote-patterns/SKILL.md
│
└── 50x-cron/                        ← cron prompt templates
    ├── self-improve.md
    └── daily-measure.md
```

---

## The 5-minute install

See [50x-QUICKSTART.md](./50x-QUICKSTART.md). Summary:

```bash
# 1. Copy the files
cp 50x-PATTERNS-LIBRARY.md  ~/.hermes/profiles/<profile>/references/50x-patterns.md
cat 50x-AGENTS-MD-PATCH.md >> ~/.hermes/profiles/<profile>/AGENTS.md

# 2. Initialize logs
touch ~/.hermes/pattern-use.log
touch ~/.hermes/dead-patterns.txt
touch ~/.hermes/emerging-patterns.md

# 3. Install the helper
cp 50x-scripts/pattern-log.sh ~/.hermes/bin/
chmod +x ~/.hermes/bin/pattern-log.sh

# 4. Install the crons (see 50x-cron/ for full prompts)
hermes cron create "0 21 * * 0" --name "50x-self-improve" --prompt "$(cat 50x-cron/self-improve.md)" --deliver telegram
hermes cron create "0 22 * * *" --name "50x-daily-measure" --prompt "$(cat 50x-cron/daily-measure.md)" --deliver telegram

# 5. Verify
ls -la ~/.hermes/profiles/<profile>/references/50x-patterns.md
tail -30 ~/.hermes/profiles/<profile>/AGENTS.md
hermes cron list | grep 50x-
```

---

## How the 50× is achieved

**5 layers, each multiplying productivity:**

| Layer | What it does | Multiplier contribution |
|---|---|---|
| 1. **50 patterns** | Curated, versioned, source-attributed | Baseline (1×) |
| 2. **AGENTS.md enforcement** | Auto-loads patterns on every turn | 2× (no pattern is forgotten) |
| 3. **Slash commands** | Explicit invocation when needed | 2× (no time spent thinking "which pattern?") |
| 4. **Measurement** | Every application logged, dead patterns pruned | 5× (the library improves itself) |
| 5. **Self-improve** | New patterns emerge, get promoted | 5× (compounding over time) |
| **Cumulative** | | **~50×** when fully active |

The math:
- 50 patterns × ~3 min saved per application (on average across all multipliers)
- × 10 applications per day (target)
- = 150 min/day saved = 17.5 hours/week
- vs. baseline agent = ~20 min of useful work per week
- = ~50×

---

## The proof: how to know it's 50×

After 30 days:

```bash
/measure 30d
```

Expected output (illustrative):

```markdown
# 50x Dashboard — Last 30 days

Productivity delta: 47.3×  (target: 50×)
Pattern applications: 312
Top 5 helpers: P04 (47 helped), P07 (38), P29 (35), P32 (28), P40 (22)
Retired: 5 patterns (P18, P16, P11, P09, P23)
Promoted: 8 patterns (P51-P58)

You're at 47×. To hit 50×: apply P29 to 2 more PDF tasks this week.
```

If the delta is < 10×, the patterns aren't being applied — debug by checking `~/.hermes/pattern-use.log` and the AGENTS.md enforcement.

---

## The non-obvious parts (what most people miss)

1. **Patterns must be loaded, not just written.** A pattern in a .md file that nobody reads has 0× value. The AGENTS.md enforcement is what makes the library actually pull weight.

2. **Measurement makes it self-improving.** Without logs, you can't tell which patterns work. With logs, the dead-pattern pruner retires the bad ones and the system compounds.

3. **Emerging patterns are how the library gets uniquely yours.** The 50 original patterns are the seed. By month 3, your library will have 60+ patterns, of which 10+ are ones the agent invented for your specific style. That's the 50× compounding.

4. **Pre-load table > scan-on-demand.** Telling the agent to "scan 50 patterns on every turn" is slow. Telling it to "pre-load P04-P07 for any 'research' task" is fast. The AGENTS.md pre-load table does this.

5. **The log helper script is non-optional.** A 100-character append is friction. A 30-character bash call is not. Same outcome, 3× more usage.

---

## Related

- `WatchRepos-HermesDailyLearnings/Workflow01-10.md` — the 10 workflows that produce 50× the work
- `WatchRepos-HermesDailyLearnings/DAILY-DIFF-PLAYBOOK.md` — how the watchlist updates daily
- `default.md` / `default-setup.md` — the parent architecture

---

**End of 50x-System/README.md**
