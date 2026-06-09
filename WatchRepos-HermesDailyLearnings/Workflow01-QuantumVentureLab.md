# Workflow 01 — Quantum Venture Lab

> **Source repos:** `HermesOracleVPS` (system-of-record for quantum architecture)
> **Run mode:** FIRST-PASS FULL INGESTION
> **Last updated:** 2026-06-09
> **WatchRepos iteration:** 1

---

## 1. Purpose

The single-profile (`quantum-venture-lab`) workflow that fuses a **Quantum Tutor** (continuous upskilling) with a **Quantum Startup Studio** (idea validation + MVP shipping) into one operational harness.

## 2. Source repos and what they teach

### `HermesOracleVPS`
- **Files:** 6 · **.md count:** 4 · **Last commit:** `61bddc97` · 2026-06-07 · "docs: add Agency gBrain framework — agent company implementation guide"
- **Theme:** Quantum Venture Lab architecture, agency gBrain framework, profile setup playbook
- **Key files:**
  - `quantum-venture-lab.md` — full architecture (2-workflow design, 11 slash commands, 3 cron jobs)
  - `quantum-venture-lab-setup.md` — executable end-to-end setup (1,435 lines)
  - `agency-gbrain-framework.md` — multi-agent company-in-an-agency pattern
  - `last30days-guide.md` — Hermes quickstart based on "last 30 days" of community learnings
- **Learnings:** A **single profile, two workflows** is the right shape for synergistic work. Slash commands + skills + selective `delegate_task` beat "9 subagents." Problem-first learning beats 7-phase academic curricula. Customer discovery is the missing piece in most learning plans.

> **Excerpt from `quantum-venture-lab.md`:**
> # Quantum Venture Lab — Single-Profile Hermes Architecture

> **Author:** Hermes Agent (MiniMax-M3) · **Date:** 2026-06-03 · **For:** Aslam Shaik
> **Status:** Recommended architecture · **Target profile:** `quantum-venture-lab`
> **Repo:** https://github.com/itsaslamopenclawdata/HermesOracleVPS

---

## 1. Executive Summary

You want **two workflows inside a single Hermes profile**:

1. **Workflo

## 3. Detailed TODO ACTION STEPS — Build the Harness

### 3.1 Profile creation
- [ ] Run `hermes profile create quantum-venture-lab`
- [ ] Set as sticky default: `hermes profile use quantum-venture-lab`
- [ ] Wire model provider (OpenRouter or Anthropic), set `model.default` to `anthropic/claude-sonnet-4`
- [ ] Enable toolsets: `terminal, file, web, browser, vision, image_gen, tts, delegation, cronjob, kanban, session_search, memory, skills, todo, messaging, safe`
- [ ] Set `memory.memory_enabled: true`, `memory.user_profile_enabled: true`
- [ ] Configure Telegram gateway on this profile (reuse same bot token, or create dedicated Quantum Venture Lab bot via @BotFather)

### 3.2 Install skills
- [ ] `hermes skills install arxiv` — daily paper fetching
- [ ] `hermes skills install obsidian` — knowledge base I/O
- [ ] `hermes skills install claude-code` — hands-on coding (Qiskit/Pennylane)
- [ ] `hermes skills install codex` — full-stack web MVPs
- [ ] `hermes skills install github-pr-workflow` — shipping MVPs
- [ ] `hermes skills install github-issues` — issue tracking
- [ ] `hermes skills install github-repo-management` — repo ops
- [ ] `hermes skills install github-code-review` — pre-commit review
- [ ] `hermes skills install github-auth` — auth helper
- [ ] `hermes skills install ideation` — structured idea generation
- [ ] `hermes skills install excalidraw` — circuit diagrams
- [ ] `hermes skills install ascii-art` — circuit ASCII fallback
- [ ] `hermes skills install nano-pdf` — paper PDF editing
- [ ] `hermes skills install requesting-code-review` — pre-commit gate
- [ ] `hermes skills install test-driven-development` — for MVP code
- [ ] `hermes skills install writing-plans` — for /qmvp planning
- [ ] `hermes skills install plan` — for /qmvp mode
- [ ] `hermes skills install hermes-agent-skill-authoring` — to author the 4 custom skills
- [ ] `hermes skills install hermes-agent` — meta

### 3.3 Author 4 custom skills
- [ ] `quantum-tutor` — `/qlearn <topic>`, knowledge-base-first, ML/finance analogies, runnable code, startup hook
- [ ] `quantum-curriculum` — `/qcurriculum`, 12-week problem-first track, week state in Obsidian
- [ ] `quantum-paper-explainer` — `/qpaper <arxiv-id or topic>`, 5-section summary + startup hook
- [ ] `quantum-quiz` — `/qquiz`, MCQs + short answer + code, scored in `Quiz-Log.md`

### 3.4 Set up AGENTS.md enforcement
- [ ] Write `~/.hermes/profiles/quantum-venture-lab/AGENTS.md` mandating: knowledge-base-first citations, no basics for a Principal DS, every answer ends with "Why this matters for a Quantum SaaS"
- [ ] Create `~/Documents/QuantumVentureLab/Learning/.kb-index.json` chapter map
- [ ] Create `~/Documents/QuantumVentureLab/Learning/kb-lookup.sh` helper
- [ ] Clone `https://github.com/itsaslamopenclawdata/Quantum-Learning-Collab` into the Obsidian vault
- [ ] Add weekly KB sync cron (Mon 06:30, `--no-agent` shell job)

### 3.5 Create the 3 primary cron jobs
- [ ] `hermes cron create "0 7 * * *"` — `daily-arxiv-digest` (skills: arxiv, obsidian, quantum-paper-explainer; deliver: telegram)
- [ ] `hermes cron create "0 9 * * 1"` — `weekly-idea-scan` (skills: web, ideation, obsidian; deliver: telegram)
- [ ] `hermes cron create "0 20 * * 0"` — `weekly-review` (skills: obsidian, quantum-curriculum; deliver: telegram)

### 3.6 Implement the 11 slash commands
- [ ] `/qlearn <topic>` — tutor
- [ ] `/qpaper <id>` — paper explainer
- [ ] `/qcurriculum` — progress
- [ ] `/qquiz` — knowledge check
- [ ] `/qbuild <task>` — hands-on code
- [ ] `/qidea <domain?>` — problem finder (parallel web subagents)
- [ ] `/qvalidate <idea>` — market scoring
- [ ] `/qdesign <idea>` — PRD + landing copy
- [ ] `/qmvp <spec>` — MVP build (parallel claude-code)
- [ ] `/qship <mvp>` — GitHub PR + Coolify deploy
- [ ] `/qrevenue <product>` — revenue model + interview plan

### 3.7 Knowledge base + customer discovery loop
- [ ] Maintain `Curriculum.md` (week state), `Quiz-Log.md` (scores), `Concepts/<topic>.md` (one per concept), `Startup/Ideas/`, `Startup/Products/`, `Startup/Customers/`
- [ ] Commit a copy of each daily/weekly output to `https://github.com/itsaslamopenclawdata/QuantumHermesDailyLearnings`
- [ ] 5 customer interviews per week via LinkedIn cold outreach

### 3.8 Deployment scaffolding
- [ ] Coolify on Oracle VPS
- [ ] gh CLI authenticated
- [ ] GitHub PAT stored in `~/.git-credential-helpers/`
- [ ] Coolify API token + project ID in `.env`

## 4. Verification

- [ ] `hermes --version` returns expected version
- [ ] `hermes doctor` shows no errors
- [ ] `hermes skills list | wc -l` returns ≥ 22 (18 bundled + 4 custom)
- [ ] `hermes cron list` shows 3 active jobs
- [ ] `/qlearn bell-state` returns a response with source citation from `Quantum-Learning-Collab`
- [ ] `hermes memory status` shows seeded facts

## 5. 90-day success criteria

- [ ] Day 30: Week 4 complete, 3 candidate ideas validated, 1 MVP repo created
- [ ] Day 60: Week 8 complete, 1 MVP deployed, 10 customer interviews done
- [ ] Day 90: 1 paying customer OR 20 leads OR 5,000 free users; 1 niche chosen for next 90 days
