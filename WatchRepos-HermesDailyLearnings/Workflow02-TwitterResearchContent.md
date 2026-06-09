# Workflow 02 — Twitter Research & Content Pipeline

> **Source repos:** `TwitterResearcherMyHermesAgent`, `content-pipeline`, `Content-Generation-Collab`, `research-feed`
> **Run mode:** FIRST-PASS FULL INGESTION
> **Last updated:** 2026-06-09
> **WatchRepos iteration:** 1

---

## 1. Purpose

Multi-agent pipeline that ingests Twitter (and adjacent social platforms), extracts pain points, validates problems, and produces content (tweet threads, blog posts, lead-gen collateral) for solopreneur / SMB audiences.

## 2. Source repos and what they teach

### `TwitterResearcherMyHermesAgent` (largest single source — 298 files)
- **Files:** 239 · **.md count:** 186 · **Last commit:** `375dea00` · 2026-06-09 · "Add Twitter summary: Workflow Trellis — B2B AI placement method (3 gates + 2x2 + 10 mechanisms, control-surface wedge for AI agencies)"
- **Theme:** Twitter research multi-agent pipeline, agent skills matrix, master cron job list
- **Key files:** `AGENT_SKILLS_MATRIX.md`, `mastercronjobslist.md`, `14DaysGoalsTODO/README.md`
- **Learnings:** The **AGENT_SKILLS_MATRIX** maps every agent role to its primary skills, supporting skills, and toolset — canonical "role → capabilities" reference. The **mastercronjobslist** is the operational heartbeat — every cron job name, schedule, prompt, delivery target.

> **Excerpt from `AGENT_SKILLS_MATRIX.md`:**
> # AGENT SKILLS MATRIX — Twitter Research Multi-Agent Pipeline

This document maps every agent role in the Twitter research pipeline to the specific Hermes skills, skill bundles, and tools that make it 100x more capable. Each agent gets its own primary skills (must-load), supporting skills (context), and toolset (execution environment).

Last updated: 2026-06-01
Profile: coding
Repo: TwitterResearc

> **Excerpt from `mastercronjobslist.md`:**
> # 🚀 Solopreneur OS v3.0 — Master Cron Jobs List & Autonomous Revenue Engine
**The 10x Improved Complete Operating System for Solo Founders**

**Version**: 3.0 (May 2026) — 10x Clarity, Specificity, Execution Velocity, Revenue Predictability & Burnout Protection  
**Repo**: https://github.com/itsaslamopenclawdata/TwitterResearcherMyHermesAgent  
**Primary Channel**: Telegram @OneBhermesbot (chat_id

### `content-pipeline` (output workspace)
- **Files:** 1 · **.md count:** 1 · **Last commit:** `d724399b` · 2026-04-03 · "Initial task assignment for Content Agent"
- **Theme:** Content Agent workspace for tweet threads, blog posts, client deliverables
- **Learnings:** Task-assignment template (Objective, Background, Deliverables, Format Spec) — reuse this template for any agent workspace.

### `Content-Generation-Collab`
- **Files:** 4 · **.md count:** 4 · **Last commit:** `81d6a151` · 2026-02-27 · "Merge branch 'main' of https://github.com/itsaslamopenclawdata/Content-Generation-Collab"
- **Theme:** AI content team output: flagship content, narrative + analytics
- **Learnings:** Pattern: 5 named bots (ContentForgeBot, NarrativestartegistBot, RepurposeBot, TechRadarBot, PerformanceAnalyticsBot) collaborate on a single flagship deliverable. Each bot has a clear role.

> **Excerpt from `flagship-content.md`:**
> # AI Content Team - Flagship Content Package

**Generated:** 2026-02-27
**Status:** Ready for Distribution
**Team:** 5 AI Agents on MiniMax-M2.5

---

## 🎯 Narrative Angle

**Title:** "The Death of the Solo Creator — And the Rise of the AI Agent Team"

**The Hook:**
> "Everyone's using AI to write tweets. That's like using a Ferrari to deliver pizza."

**The Contrarian Stance:**
The biggest lie in

### `research-feed` (input workspace)
- **Files:** 1 · **.md count:** 1 · **Last commit:** `1cb89281` · 2026-04-03 · "Initial task assignment for Research Agent"
- **Theme:** Research Agent outputs — lead sourcing, market research, competitive intel
- **Learnings:** Qualification framework: Fit Score × Intent Score = Composite Score. Target 80+ for immediate outreach. Default lead sources: r/SaaS, r/MarketingStrategy, r/copywriting.

## 3. Detailed TODO ACTION STEPS — Build the Harness

### 3.1 Define the agent roster
- [ ] **ResearcherBot** — fetches tweets/posts via `web` toolset, scores pain-point density
- [ ] **PainExtractorBot** — reads 50+ posts/day, extracts 5 top pain points with verbatim quotes
- [ ] **ValidatorBot** — scores each pain (volume, willingness-to-pay, market size)
- [ ] **NarrativeBot** — converts pain + audience into hook, contrarian stance, 5-tweet thread
- [ ] **RepurposeBot** — turns the thread into LinkedIn post, blog post, newsletter
- [ ] **PerformanceBot** — tracks engagement, flags what to repeat or kill

### 3.2 Author the AGENT_SKILLS_MATRIX
- [ ] Create `Workflow02/AGENT_SKILLS_MATRIX.md` modeled on `TwitterResearcherMyHermesAgent/AGENT_SKILLS_MATRIX.md`
- [ ] For each of the 6 bots, list: primary skills (must-load), supporting skills, toolset, prompt skeleton, output schema

### 3.3 Set up the cron loop (mastercronjobslist)
- [ ] Hourly: `pain-feed-fetcher` (ResearcherBot) — pulls new posts from tracked accounts/hashtags
- [ ] Daily 06:00: `pain-extractor` — ranks 5 top pains
- [ ] Daily 09:00: `validator-run` — scores each pain
- [ ] Daily 11:00: `narrative-gen` — produces one tweet thread from the top-scored pain
- [ ] Daily 14:00: `repurpose-burst` — publishes to LinkedIn + blog + newsletter
- [ ] Daily 22:00: `performance-recap` — engagement report, kill/keep decisions

### 3.4 Define the data schemas
- [ ] `pains.json` schema: date, account, post_url, verbatim, score, theme
- [ ] `threads.json` schema: date, hook, stance, tweets list, cta, performance_metrics
- [ ] `leads.json` schema: date, source, handle, fit_score, intent_score, composite, contact_attempted

### 3.5 Build the content templates
- [ ] **Tweet thread template** (5–8 tweets): Hook → Contrarian → Problem → Solution → Story → Proof → CTA
- [ ] **LinkedIn post template** (150–300 words): first line is the hook, short paragraphs, 1 CTA at end
- [ ] **Blog post template** (800–1,500 words): H1, intro with hook, 3–5 H2 sections, conclusion with CTA
- [ ] **Newsletter template** (300 words): subject, preview, body, P.S. with offer

### 3.6 Quality gates
- [ ] Every thread reviewed by `CritiqueBot` (uses `requesting-code-review` skill, adapted for prose)
- [ ] Engagement threshold: any post under 1% engagement after 24h is auto-killed
- [ ] Pain score threshold: Composite under 60 → don't generate content from it

### 3.7 Track sources of truth
- [ ] `Workflow02/pain-sources.md` — list of tracked accounts, hashtags, subreddits
- [ ] `Workflow02/voice-guide.md` — tone, vocabulary, banned words
- [ ] `Workflow02/cta-library.md` — rotating set of CTAs (never repeat within 7 days)

### 3.8 Daily outputs committed to GitHub
- [ ] `Workflow02/threads/YYYY-MM-DD.md` — the day's threads
- [ ] `Workflow02/leads/YYYY-MM-DD.md` — qualified leads
- [ ] `Workflow02/recap/YYYY-MM-DD.md` — performance recap

## 4. Verification

- [ ] All 6 agents respond to their canonical prompt and produce the right output schema
- [ ] Cron jobs all fire on schedule (check logs after 24h)
- [ ] `pain-sources.md` has at least 10 tracked sources
- [ ] First week's recap shows ≥ 5 threads generated, ≥ 3 leads qualified

## 5. Success criteria (per week)

- [ ] 5 threads published
- [ ] 10 leads qualified
- [ ] 2 leads in active outreach
- [ ] At least 1 lead converts to a sales call
