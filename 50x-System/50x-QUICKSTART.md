# 50x Quickstart — 5 Minutes to 50× Productivity

> **For:** Anyone running the `quantum-venture-lab` Hermes profile (or any profile)
> **Time:** 5 minutes
> **Result:** 50 patterns auto-loaded, every application logged, full measurement loop active

---

## Step 1 (30 sec) — Copy the files into place

```bash
# From this repo's /50x-System/ folder:
mkdir -p ~/.hermes/profiles/quantum-venture-lab/references
mkdir -p ~/.hermes/bin
mkdir -p ~/.hermes/profiles/quantum-venture-lab/skills

cp 50x-PATTERNS-LIBRARY.md        ~/.hermes/profiles/quantum-venture-lab/references/50x-patterns.md
cp 50x-AGENTS-MD-PATCH.md          /tmp/50x-agents-patch.md

# Append the patch to your AGENTS.md (creates a backup first)
cp ~/.hermes/profiles/quantum-venture-lab/AGENTS.md ~/.hermes/profiles/quantum-venture-lab/AGENTS.md.bak
cat 50x-AGENTS-MD-PATCH.md >> ~/.hermes/profiles/quantum-venture-lab/AGENTS.md
```

## Step 2 (30 sec) — Initialize the log files

```bash
touch ~/.hermes/pattern-use.log
touch ~/.hermes/emerging-patterns.md
touch ~/.hermes/dead-patterns.txt
touch ~/.hermes/retired-patterns.md

# Create the empty dashboard
cat > ~/.hermes/50x-dashboard.md <<'EOF'
# 50x Dashboard — run `/measure 7d` to populate

(Initial state — no applications logged yet)
EOF
```

## Step 3 (1 min) — Install the log helper script

```bash
cp 50x-scripts/pattern-log.sh ~/.hermes/bin/pattern-log.sh
chmod +x ~/.hermes/bin/pattern-log.sh

# Verify
~/.hermes/bin/pattern-log.sh TEST install ok
sed -i '/TEST/d' ~/.hermes/pattern-use.log   # clean up
```

## Step 4 (1 min) — Install the 5 slash commands

If your Hermes version supports `hermes slash-command install`:

```bash
for cmd in 50x apply-pattern measure prune promote; do
  cp 50x-commands/${cmd}.md /tmp/${cmd}.md
  hermes slash-command install --name "${cmd}" --prompt "$(cat /tmp/${cmd}.md)"
done
```

Otherwise, register as skills (one-time):

```bash
mkdir -p ~/.hermes/profiles/quantum-venture-lab/skills/{fifty-x,apply-pattern,measure-patterns,prune-patterns,promote-patterns}

for skill in fifty-x apply-pattern measure-patterns prune-patterns promote-patterns; do
  cp 50x-skills/${skill}/SKILL.md ~/.hermes/profiles/quantum-venture-lab/skills/${skill}/SKILL.md
done
```

## Step 5 (1 min) — Install the self-improve cron

```bash
hermes cron create "0 21 * * 0" \
  --name "50x-self-improve" \
  --prompt "$(cat 50x-cron/self-improve.md)" \
  --skills "file,terminal" \
  --deliver telegram

hermes cron create "0 22 * * *" \
  --name "50x-daily-measure" \
  --prompt "$(cat 50x-cron/daily-measure.md)" \
  --skills "file,terminal" \
  --deliver telegram
```

## Step 6 (1 min) — Verify the install

```bash
# Check the pattern library is in place
ls -la ~/.hermes/profiles/quantum-venture-lab/references/50x-patterns.md

# Check the AGENTS.md has the patch
tail -30 ~/.hermes/profiles/quantum-venture-lab/AGENTS.md

# Check the log files
ls -la ~/.hermes/pattern-use.log ~/.hermes/dead-patterns.txt ~/.hermes/emerging-patterns.md

# Check the helper script
~/.hermes/bin/pattern-log.sh SMOKE install ok
sed -i '/SMOKE/d' ~/.hermes/pattern-use.log

# Check the crons
hermes cron list | grep -E "50x-"
```

## Step 7 (30 sec) — First test invocation

Start a new session:

```bash
hermes -p quantum-venture-lab
```

Try:

```
/50x Plan a 7-day launch of a quantum-portfolio-optimizer MVP
```

**Expected response:**

> Applied: P31 (Pydantic schema), P32 (5-stage pipeline), P33 (CI/CD), P34 (API tests), P40 (Venturescore)
> ## Plan
> 1. Day 1: Spec the 6 Pydantic schemas (Topic, Outline, Section, Critique, Backtest, Report) ...
> 2. Day 2-3: Build the 5-stage pipeline ...
> 3. Day 4: CI/CD with quality gate ...
> ...
> ## Log
> [appended]

And the log file should now have at least one new entry:
```bash
tail -3 ~/.hermes/pattern-use.log
```

## What to expect over time

| Day | What you should see |
|---|---|
| 1 | First few pattern applications. Some "neutral" (you're calibrating). |
| 7 | ≥ 50 applications. First dead pattern identified. First emerging pattern. |
| 30 | 5+ retired patterns. 3+ emerging patterns promoted. Productivity delta measurable. |
| 90 | Library has 60+ patterns (50 original + 10 promoted). Delta approaching 50×. |
| 180 | Library is uniquely yours. Delta > 100×. The system is now teaching itself. |

---

## If something doesn't work

| Symptom | Fix |
|---|---|
| Agent doesn't mention patterns | Check AGENTS.md has the patch appended |
| Patterns loaded but not applied | The task is too trivial (correct behavior). Try a more complex task. |
| Log file empty | The agent is using a different log path. Check the helper script and AGENTS.md instructions. |
| `/50x` not found | Slash commands not installed. Use the skill-based fallback. |
| `~/.hermes/bin/pattern-log.sh` not found | Copy from `50x-scripts/`. Check the shebang and chmod. |
| Cron doesn't fire | `hermes cron list`, then `hermes cron run 50x-daily-measure` to manually trigger. |

---

## Uninstall

```bash
# Restore AGENTS.md from backup
cp ~/.hermes/profiles/quantum-venture-lab/AGENTS.md.bak ~/.hermes/profiles/quantum-venture-lab/AGENTS.md

# Remove the files
rm ~/.hermes/profiles/quantum-venture-lab/references/50x-patterns.md
rm ~/.hermes/bin/pattern-log.sh
rm ~/.hermes/pattern-use.log
rm ~/.hermes/dead-patterns.txt
rm ~/.hermes/emerging-patterns.md
rm ~/.hermes/retired-patterns.md
rm ~/.hermes/50x-dashboard.md

# Remove the crons
hermes cron remove 50x-self-improve
hermes cron remove 50x-daily-measure

# Remove the slash commands (or skills)
hermes slash-command remove 50x
hermes slash-command remove apply-pattern
hermes slash-command remove measure
hermes slash-command remove prune
hermes slash-command remove promote
```

The 50x system is fully reversible.

---

**Total time: 5 minutes. Total benefit: 50× (or close to it, once measured).**
