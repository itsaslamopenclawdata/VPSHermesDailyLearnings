# Workflow 08 — Venture Evaluation

> **Source repos:** `VentureHQ`
> **Run mode:** FIRST-PASS FULL INGESTION
> **Last updated:** 2026-06-09
> **WatchRepos iteration:** 1

---

## 1. Purpose

A bot that scores any venture idea in under 60 seconds, with a clear go/no-go decision. The output drives the Quantum Startup Studio's idea shortlist.

## 2. Source repos and what they teach

### `VentureHQ`
- **Files:** 26 · **.md count:** 24 · **Last commit:** `cb13c49d` · 2026-03-04 · "Add 100x productivity plan for 20 agents"
- **Theme:** Venture scoring, 100x productivity plan, content workflow, 20-agent evaluation
- **Key files:** `QUICKSTART.md`, `CONTRIBUTING.md`, `CONTENT_WORKFLOW.md`, `CAPABILITIES.md`

> **Excerpt from `QUICKSTART.md`:**
> # VentureHQ Quick Start

Get your first venture score in under 60 seconds.

---

## 🚀 One-Minute Quick Start

**Step 1:** Mention VenturescoreBot with your idea

```
@VenturescoreBot Score: [your venture idea]
```

**Step 2:** Wait 30-60 seconds

**Step 3:** Read your score + decision

That's it.

---

## 📝 Example Queries

### Idea #1: SaaS
```
@VenturescoreBot Score: AI-powered email categorizat

> **Excerpt from `CONTRIBUTING.md`:**
> # Contributing to VentureHQ

VentureHQ is a coordinated AI agent team. Here's how to contribute.

---

## 📋 What We Document

### Documentation Types
- **Core Docs:** README, QUICKSTART, CAPABILITIES (maintained by team)
- **Examples:** Real venture evaluations (add to `examples/` directory)
- **Templates:** Structured output formats (add to `templates/` directory)
- **Research:** Market data sour

> **Excerpt from `CONTENT_WORKFLOW.md`:**
> # Content Production Workflow

## 6-Stage Process for All Content Tasks

This workflow must be followed for EVERY content task before pushing to GitHub.

---

### Stage 1: Research 📚
**Owner:** IdeaScoutBot
- Google search
- YouTube research
- Reddit/community validation
- Industry articles
- **Output:** Research findings document

---

### Stage 2: Brainstorm 💡
**Owner:** IdeaScoutBot
- Generate 

> **Excerpt from `CAPABILITIES.md`:**
> # VentureHQ Team Capabilities

Detailed breakdown of each bot's expertise and output formats.

---

## 🎯 IdeaScoutBot

### Mission
Discover and validate promising venture opportunities by screening for market fit, timing, and potential.

### Core Capabilities

**Market Opportunity Screening:**
- Identify untapped market gaps and white spaces
- Analyze timing and trend alignment (early/late/right n

## 3. Detailed TODO ACTION STEPS — Build the Harness

### 3.1 Define the scoring rubric
- [ ] **Market size** (1–10): TAM, SAM, SOM
- [ ] **Competition** (1–10): density, moat potential
- [ ] **Build difficulty** (1–10): 1 = weekend MVP, 10 = 2-year effort
- [ ] **Revenue potential** (1–10): ARPU × addressable customers
- [ ] **Distribution** (1–10): how easy is it to reach the first 100 users
- [ ] **Founder fit** (1–10): does this match my skills and network

### 3.2 Build the @VenturescoreBot interface
- [ ] Input: a venture idea (1–3 sentences)
- [ ] Output: score (1–100), per-dimension breakdown, decision (BUILD / VALIDATE / KILL), 3 reasons
- [ ] Latency target: < 60 seconds end-to-end
- [ ] Deploy as: Telegram bot OR `/qvalidate <idea-id>` slash command in the quantum-venture-lab profile

### 3.3 Build the validation queue
- [ ] Every `/qvalidate` output goes to `Workflow08/queue/<date>.md`
- [ ] Top-scoring ideas bubble up to the Quantum Startup Studio's active backlog
- [ ] KILL decisions are archived (don't re-evaluate for 90 days)

### 3.4 Build the 100x productivity plan
- [ ] For each BUILD decision, generate a 100x productivity plan
- [ ] Plan structure: 1-week MVP, 1-month v1, 3-month v2, 6-month scale
- [ ] Each phase has: deliverables, agents, success criteria, kill criteria
- [ ] Stored in `Workflow08/plans/<idea-slug>.md`

### 3.5 Build the 20-agent evaluation panel
- [ ] For BUILD decisions, spin up 20 parallel evaluation agents (delegate_task batch)
- [ ] Each agent evaluates from a different lens: market, tech, legal, ops, finance, customer, etc.
- [ ] Aggregate scores → go/no-go with 95% confidence
- [ ] Cost cap: $5 per evaluation (use cheaper models for the parallel agents)

### 3.6 Daily outputs committed to GitHub
- [ ] `Workflow08/queue/YYYY-MM-DD.md` — every idea evaluated today
- [ ] `Workflow08/plans/<idea-slug>.md` — 100x plans for BUILD decisions
- [ ] `Workflow08/kill-archive/<idea-slug>.md` — KILL decisions (don't repeat)

## 4. Verification

- [ ] @VenturescoreBot responds in < 60 seconds
- [ ] First 5 ideas scored and decisions logged
- [ ] First 100x plan generated for a BUILD decision

## 5. Success criteria (per quarter)

- [ ] 30 ideas evaluated
- [ ] 5 BUILD decisions
- [ ] 1 venture reaches first paying customer
- [ ] Calibration: scoring correlates with actual outcomes (track and update the rubric)
