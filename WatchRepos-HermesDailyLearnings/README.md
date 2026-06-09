# WatchRepos — Hermes Daily Learnings

> **One patterns file, not 50 templates.** Read [`50x-QUICKSTART.md`](./50x-QUICKSTART.md) first.
> **Source:** All 18 watch repos, re-distilled daily by the `distill.py` cron at 05:00.
> **The 10 `Workflow0X-*.md` files and 18 `watchrepos-index/*.md` files are reference material** that the daily distiller uses; they are NOT what the agent reads at runtime. The agent reads exactly one file at runtime: [`50x-PATTERNS-LIBRARY.md`](./50x-PATTERNS-LIBRARY.md).

---

## The system in 30 seconds

1. **18 watch repos** are the raw material (see "Watchlist" below)
2. **`distill.py`** fetches them as tarballs (1 API call each), diffs against yesterday's state, and updates one file
3. **[`50x-PATTERNS-LIBRARY.md`](./50x-PATTERNS-LIBRARY.md)** holds the 50 distilled patterns (P01–P50)
4. **[`50x-AGENTS-MD-PATCH.md`](./50x-AGENTS-MD-PATCH.md)** is appended to your profile's `AGENTS.md` so the agent auto-loads patterns on every turn
5. **[`50x-QUICKSTART.md`](./50x-QUICKSTART.md)** is the 6-command install + the loop diagram

**Goal:** Make the agent 50× more productive by encoding your own watch repos into a measured, applied, self-improving pattern library.

---

## File map

```
WatchRepos-HermesDailyLearnings/
├── README.md                       ← you are here
├── 50x-QUICKSTART.md               ← the 6 commands + the loop diagram
├── 50x-PATTERNS-LIBRARY.md         ← 50 patterns (P01–P50) — the runtime artifact
├── 50x-AGENTS-MD-PATCH.md          ← runtime enforcement (append to AGENTS.md)
├── distill.py                      ← daily cron script (re-distills on change)
├── DAILY-DIFF-PLAYBOOK.md          ← how the daily diff loop works
├── Workflow01-…Workflow10-…md      ← reference material (delete if you only want 50x)
└── watchrepos-index/               ← per-repo excerpts (used by the distiller)
```

---

## Watchlist (18 repos)

| # | Repo | Visibility | Last pushed | Purpose |
|---|---|---|---|---|
| 1 | `TwitterResearcherMyHermesAgent` | private | 2026-06-09 | Hermes VPS daily notes |
| 2 | `MyHermesResearcher` | private | 2026-06-09 | Quantum Lab daily learnings |
| 3 | `Daily-Working-Space` | private | 2026-06-05 | Daily execution / 10x plan |
| 4 | `HermesOracleVPS` | private | 2026-06-07 | Quantum Venture Lab architecture |
| 5 | `CodingDeveloperRules` | private | 2026-06-01 | Skill bundles, coding rules |
| 6 | `MyWorkflowsIntelligenceLayer` | public | 2026-06-09 | Cron workflow intelligence |
| 7 | `UltraPDFGenSkill` | public | 2026-04-06 | 50-round PDF generator |
| 8 | `AslamTheEliteLeader` | public | 2026-04-04 | 10x growth system |
| 9 | `MyPaperclipOutputs` | public | 2026-04-04 | AI agent work products |
| 10 | `company-orchestration` | public | 2026-04-03 | CEO directives / orchestration |
| 11 | `content-pipeline` | public | 2026-04-03 | Content agent outputs |
| 12 | `research-feed` | public | 2026-04-03 | Research agent findings |
| 13 | `deployments` | public | 2026-04-02 | Website builds & deployments (empty) |
| 14 | `quality-gate` | public | 2026-04-02 | Verification standards (empty) |
| 15 | `MyDayWorking` | public | 2026-03-28 | 1-man business automation |
| 16 | `VentureHQ` | public | 2026-03-04 | Venture evaluation team |
| 17 | `Content-Generation-Collab` | public | 2026-02-27 | AI content pipeline |
| 18 | `Ebook_EntireVibePipepline` | public | 2026-02-26 | Topic-to-ebook pipeline |

---

## How this folder is updated

| Trigger | What happens | Command |
|---|---|---|
| Daily 05:00 | Fetch all 18 tarballs, diff, detect pattern changes, re-push | `python3 distill.py` (run by cron) |
| Weekly Sunday 20:00 | Prune dead patterns, promote emerging ones, log metrics | `fifty-x-self-improve` cron |
| Manual | "Run the daily distill now" | `python3 /opt/data/watchrepo-harness/distill.py` |

See [`50x-QUICKSTART.md`](./50x-QUICKSTART.md) for the full install + loop diagram.

---

**Owner:** Aslam Shaik · **Maintained by:** `watchrepos-daily-diff` cron (daily) + `fifty-x-self-improve` cron (weekly)
