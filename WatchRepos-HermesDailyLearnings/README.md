# WatchRepos — Hermes Daily Learnings

> **One .md per Workflow, regenerated daily by the `watchrepos-daily-diff` cron.**
> **Source:** All 18 watch repos (see "Watchlist" below).
> **Updated:** See each workflow file's `Last updated` header.

---

## What is this folder?

This folder is the **second brain** of the Hermes agent's watch-list system. Every day, the `watchrepos-daily-diff` cron:

1. Fetches all 18 watch repos
2. Detects what changed since the last run
3. Updates the relevant **Workflow .md** below
4. Commits + pushes
5. Posts a summary to Telegram

Each **Workflow** is a domain-spanning topic (not a 1:1 mapping to a repo). A workflow is synthesized from one or more watch repos that share a theme. This means a single change in a repo can affect multiple workflows.

---

## The 10 Workflows

| # | Workflow | Primary source repos | What it teaches |
|---|---|---|---|
| 01 | [Quantum Venture Lab](./Workflow01-QuantumVentureLab.md) | `HermesOracleVPS` | Single-profile architecture for Quantum Tutor + Quantum Startup Studio |
| 02 | [Twitter Research & Content](./Workflow02-TwitterResearchContent.md) | `TwitterResearcherMyHermesAgent`, `content-pipeline`, `Content-Generation-Collab`, `research-feed` | Multi-agent pipeline: research → pain-extract → validate → narrate → publish |
| 03 | [Daily Intelligence & 10x Growth](./Workflow03-DailyIntelligence10x.md) | `AslamTheEliteLeader`, `MyDayWorking`, `Daily-Working-Space` | Personal-OS layer: 1-man business + 61 AI agents + $1B goal |
| 04 | [Skill Bundles & Coding Standards](./Workflow04-SkillBundlesCodingStandards.md) | `CodingDeveloperRules`, `UltraPDFGenSkill`, `MyPaperclipOutputs` | Skill bundle primitive, race-condition spec, content amplification |
| 05 | [PDF / Ebook Generation Pipeline](./Workflow05-PDFEbookPipeline.md) | `Ebook_EntireVibePipepline`, `UltraPDFGenSkill`, `MyPaperclipOutputs` | Topic → outline → content → polish → publish (Vibe PDF Platform pattern) |
| 06 | [Multi-Agent Orchestration & CEO Directives](./Workflow06-MultiAgentOrchestration.md) | `company-orchestration`, `HermesOracleVPS` | CEO directives, agent org chart, Method 0 pricing, agency gBrain |
| 07 | [Workflows Intelligence Layer](./Workflow07-WorkflowsIntelligenceLayer.md) | `MyWorkflowsIntelligenceLayer` | Upstream feed: YouTube channels → insights → routed to downstream workflows |
| 08 | [Venture Evaluation](./Workflow08-VentureEvaluation.md) | `VentureHQ` | @VenturescoreBot, 100x productivity plans, 20-agent evaluation panel |
| 09 | [Daily Hermes Researcher](./Workflow09-DailyHermesResearcher.md) | `MyHermesResearcher` | 20 daily prompts, 3 playbooks, learnings index, prompt quality loop |
| 10 | [Quality Gate & Deployments](./Workflow10-QualityGateDeployments.md) | `quality-gate`, `deployments` | "Ready to ship" rubric, CI/CD pipeline, Coolify deploys, monitoring |

Each Workflow .md has the same structure:
1. **Purpose** — what this workflow is
2. **Source repos and what they teach** — manifest + excerpts
3. **Detailed TODO ACTION STEPS — Build the Harness** — the agent's playbook
4. **Verification** — how to know it's working
5. **Success criteria** — when to consider it done

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

| Trigger | What happens | Cron / command |
|---|---|---|
| First run (today) | Full ingestion: clone all 18, sample 39 files, generate 10 workflows, commit + push | `python3 /tmp/generate_workflows.py` (one-time) |
| Daily 05:00 | Diff detection: fetch all 18, find changes since last run, update relevant workflows | `watchrepos-daily-diff` cron |
| Manual | "Run the daily diff now" | `hermes cron run watchrepos-daily-diff` |

See [`DAILY-DIFF-PLAYBOOK.md`](./DAILY-DIFF-PLAYBOOK.md) for the full operational spec.

---

## File map

```
WatchRepos-HermesDailyLearnings/
├── README.md                              ← you are here
├── DAILY-DIFF-PLAYBOOK.md                 ← how to run the daily diff
├── Workflow01-QuantumVentureLab.md
├── Workflow02-TwitterResearchContent.md
├── Workflow03-DailyIntelligence10x.md
├── Workflow04-SkillBundlesCodingStandards.md
├── Workflow05-PDFEbookPipeline.md
├── Workflow06-MultiAgentOrchestration.md
├── Workflow07-WorkflowsIntelligenceLayer.md
├── Workflow08-VentureEvaluation.md
├── Workflow09-DailyHermesResearcher.md
└── Workflow10-QualityGateDeployments.md
```

---

**Last updated:** 2026-06-03 (first pass — full ingestion)
**Next scheduled run:** 2026-06-04 05:00 (daily diff cron)
**Owner:** Aslam Shaik · **Maintained by:** `watchrepos-daily-diff` cron
