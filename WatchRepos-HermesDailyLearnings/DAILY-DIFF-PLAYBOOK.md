# Daily Diff Loop — How To Run WatchRepos Hermes Daily Learnings

> **For:** Future Hermes Agent runs (and for Aslam, when he wants to re-trigger a daily run)
> **Created:** 2026-06-03
> **First pass:** All 10 workflow .md files (Workflow01..Workflow10) are committed below.
> **Daily diff:** This file explains how to run the next pass — only changed/added files since the last run.

---

## What "First Pass" and "Daily Diff" mean

### First pass (already done today, 2026-06-03)
- Cloned all 18 watch repos to `/tmp/watchrepos/`
- Indexed every file: path, size, sha1, last-commit, theme
- Sampled 39 high-signal files for content excerpts
- Generated **one .md per workflow** (10 workflows total)
- Each .md cites source repos, summarizes learnings, and lists **detailed TODO ACTION STEPS**
- All .md files were committed to `VPSHermesDailyLearnings/WatchRepos-HermesDailyLearnings/`

### Daily diff (how to run tomorrow, and every day after)
The goal is to detect **what changed** in each watch repo since the last successful run, and update the relevant workflow .md files with new TODOs / learnings.

---

## How to detect the diff

### 1. Identify the "last successful run" timestamp

The manifest of the previous run is stored at:
```
~/.hermes/watchrepos/last-run.json
```

This file contains:
- `last_run_at` (ISO 8601 timestamp)
- `per_repo` (dict: repo_name → { last_commit_sha, last_commit_date, file_count })

If this file doesn't exist (e.g. fresh install), the first run is treated as a full pass, and this file is created.

### 2. For each watch repo, compute the diff

```bash
cd /tmp/watchrepos/<repo>
git fetch origin
# Commits since last run:
git log --since="$(cat ~/.hermes/watchrepos/last-run.json | jq -r .last_run_at)" --oneline
# Files changed since last run:
git diff --name-status <last_commit_sha>..HEAD
```

### 3. Categorize the changes

For each changed file, decide which workflow it affects:

| Repo | Primary workflow(s) | Diffing pattern |
|---|---|---|
| `HermesOracleVPS` | W01 (Quantum Venture Lab) | md → W01 update |
| `TwitterResearcherMyHermesAgent` | W02 (Twitter Research & Content) | new threads/agents → W02 update |
| `content-pipeline` | W02 | new tasks → W02 update |
| `Content-Generation-Collab` | W02 | new content → W02 update |
| `research-feed` | W02 | new research → W02 update |
| `AslamTheEliteLeader` | W03 (Daily Intelligence / 10x) | new engines → W03 update |
| `MyDayWorking` | W03 | manifest changes → W03 update |
| `Daily-Working-Space` | W03 | brain/heartbeat/plan changes → W03 update |
| `CodingDeveloperRules` | W04 (Skill Bundles) | new bundles → W04 update |
| `UltraPDFGenSkill` | W04, W05 (PDF Pipeline) | version bump → W04 + W05 update |
| `MyPaperclipOutputs` | W04, W05 | new outputs → W04 + W05 update |
| `Ebook_EntireVibePipepline` | W05 (PDF/Ebook Pipeline) | new reports → W05 update |
| `company-orchestration` | W06 (CEO Directives) | new directives → W06 update |
| `HermesOracleVPS` (agency-gbrain-framework.md) | W06 | framework changes → W06 update |
| `MyWorkflowsIntelligenceLayer` | W07 (Workflows Intelligence Layer) | new channels → W07 update |
| `VentureHQ` | W08 (Venture Evaluation) | rubric changes → W08 update |
| `MyHermesResearcher` | W09 (Daily Hermes Researcher) | new prompts/playbooks → W09 update |
| `quality-gate`, `deployments` | W10 (Quality Gate & Deployments) | new files → W10 update |

### 4. Update the relevant Workflow .md

For each affected workflow:
1. Open the existing `WorkflowNN-<name>.md`
2. Find the "Source repos and what they teach" section
3. Update the "Last commit" line
4. If a new high-signal file appeared, add it to the "Key files" list and a new "Excerpt" block
5. Add any new TODO action steps to section 3
6. Update "WatchRepos iteration" to N+1 at the top
7. Update "Last updated" date

### 5. Commit + push

```bash
cd /tmp/VPSHermesDailyLearnings
git add WatchRepos-HermesDailyLearnings/
git commit -m "watchrepos daily diff: $DATE — updated workflows [W02 W03 ...]"
git push
```

The credential helper at `~/.git-credential-helpers/gh-cred-helper.sh` handles auth.

### 6. Update last-run.json

```bash
echo "{\"last_run_at\": \"$(date -Iseconds)\", \"per_repo\": {...}}" > ~/.hermes/watchrepos/last-run.json
```

---

## How to schedule this

Create a cron job that runs daily at 05:00 (before all other crons, so today's diffs are reflected in the morning digest):

```bash
hermes cron create "0 5 * * *" \
  --name "watchrepos-daily-diff" \
  --prompt "Run the WatchRepos Hermes Daily Learnings daily diff loop.

Steps:
1. Read ~/.hermes/watchrepos/last-run.json to find the last run timestamp.
2. For each of the 18 watch repos in /tmp/watchrepos/, run git fetch + git log to find new commits.
3. For each new commit, identify the workflow it affects (see the table in WatchRepos-HermesDailyLearnings/DAILY-DIFF-PLAYBOOK.md).
4. For each affected workflow, update the relevant Workflow .md in /tmp/VPSHermesDailyLearnings/WatchRepos-HermesDailyLearnings/.
5. Commit and push.
6. Update ~/.hermes/watchrepos/last-run.json.
7. Post a one-line summary to Telegram: 'WatchRepos diff: N workflows updated, M files added/changed.'

Skills: github-pr-workflow, github-repo-management, file, terminal.
Deliver: telegram." \
  --skills "github-pr-workflow,github-repo-management,file,terminal" \
  --deliver telegram
```

---

## Edge cases

### Repo deleted or renamed
- Detect via the GitHub API: `GET /repos/itsaslamopenclawdata/<repo>` returns 404
- Action: remove the repo from the watch list, mark its workflow .md as "(source repo removed)"

### Repo made private
- Same as above — API returns 404
- Action: same as deleted (treat as removed from watch list)

### Massive change (> 50% of files changed)
- Treat as a full re-ingestion
- Reset `last-run.json` so the next run is a full pass again

### Cron fails (network, git error, etc.)
- Don't update `last-run.json` — the next run will retry the missed diff
- Send a Telegram alert

---

## How to add a new watch repo

1. Clone: `git clone https://github.com/itsaslamopenclawdata/<new-repo>.git /tmp/watchrepos/<new-repo>`
2. Add to the cron prompt's list of 18 repos
3. Classify it: which workflow(s) does it affect?
4. Update the relevant workflow .md to cite the new repo
5. Update `~/.hermes/watchrepos/last-run.json` with the new repo's metadata

---

## Cost budget

- 18 repos × ~2-3 GitHub API calls per day = ~50 API calls/day (free tier is 5,000/hr)
- 1 commit + 1 push per day = ~10 KB egress
- LLM cost: only the diff-extraction step is LLM-driven; estimated 5-10K tokens/day at ~$0.01/day with Claude Haiku

**Total daily cost:** < $0.05/day. Well within budget.

---

**End of playbook.** For questions, open an issue at `https://github.com/itsaslamopenclawdata/HermesOracleVPS/issues`.
