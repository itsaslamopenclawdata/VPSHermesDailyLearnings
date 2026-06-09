# Workflow 06 — Multi-Agent Orchestration & CEO Directives

> **Source repos:** `company-orchestration`, `HermesOracleVPS` (agency-gbrain-framework.md)
> **Run mode:** FIRST-PASS FULL INGESTION
> **Last updated:** 2026-06-09
> **WatchRepos iteration:** 1

---

## 1. Purpose

CEO-level orchestration layer: define the agent org chart, write directives that are unambiguous, enforce reporting lines, and ship via the "Method 0" pricing model (sell agents, not outputs). $10K/month MRR target.

## 2. Source repos and what they teach

### `company-orchestration`
- **Files:** 8 · **.md count:** 8 · **Last commit:** `a08bdd76` · 2026-04-03 · "Add SOL-16 task memory - 20 subgoals for pain→PDF workflow"
- **Theme:** CEO directives, AI agent services company, $10K MRR goal via 'Method 0'
- **Key files:** `README.md`, `directive-003.md`, `research-agent-instructions.md`, `content-agent-instructions.md`, `hiring-plan.md`

> **Excerpt from `README.md`:**
> # Company Orchestration

**Purpose**: CEO directives and orchestration for AI Agent Services company

## Status

Company is **ACTIVE** and forming.

## Mission

Build an AI agent services business that helps solopreneurs and SMBs automate their operations using:
- **OpenClaw** (orchestration)
- **Hermes** (outreach)
- **Paperclip** (skill building)

**Revenue Goal**: $$10K+/month recurring via Meth

> **Excerpt from `directive-003.md`:**
> # CEO Directive 003: Phase 2 Hiring - Content + Research Agents

**Issued**: 2026-04-02
**Status**: READY FOR EXECUTION (pending Orchestrator configuration)
**Priority**: HIGH

## Context

With the Orchestrator agent now online (pending configuration), we move to Phase 2 of our hiring plan. Content and Research agents are our core revenue-generating team - they will find leads and create the outre

> **Excerpt from `research-agent-instructions.md`:**
> # RESEARCH AGENT

## Role
You are the Research Agent for an AI Agent Services company. You find and qualify leads, research markets, and enable data-driven outreach.

## Mission
Feed the sales pipeline with high-quality, qualified leads and market insights.

## Stack
- **Primary**: Claude (via Paperclip)
- **Lead Sources**: Reddit API, web research
- **Outreach**: Hermes (via F:\MyHermesagent)
- *

### `HermesOracleVPS/agency-gbrain-framework.md`
- **Theme:** Agency gBrain Framework — one brain, scoped agents, isolated client pods, less drift, more leverage

> **Excerpt from `agency-gbrain-framework.md`:**
> # Agency gBrain Framework — How to Build an Agent Company Inside Your Agency

A comprehensive, step-by-step implementation guide.

**Core Philosophy:** One brain. Scoped agents. Isolated client pods. Better output. Less drift. More leverage.

---

## Table of Contents

- [The Goal](#step-0-the-goal)
- [Phase 1: Build the Agency gBrain (The Company Brain)](#phase-1-build-the-agency-gbrain-the-compa

## 3. Detailed TODO ACTION STEPS — Build the Harness

### 3.1 Define the agent org chart
- [ ] **CEO** (you, Aslam) — strategic decisions, approvals, final go/no-go
- [ ] **COO** (OrchestratorAgent) — translates directives into cron jobs and skill loads
- [ ] **CRO** (RevenueAgent) — owns the sales pipeline, customer interviews, MRR
- [ ] **CMO** (ContentAgent) — owns content production, distribution, engagement
- [ ] **CTO** (BuilderAgent) — owns MVP builds, deploys, technical debt
- [ ] **CFO** (FinanceAgent) — owns invoicing, expense tracking, runway
- [ ] **Specialists** (5–10) — domain experts (e.g. QuantumAgent, PDFAgent, TwitterAgent)

### 3.2 Adopt the directive format
- [ ] Every directive has: Objective, Background, Deliverables, Success Criteria, Owner, Deadline
- [ ] Numbered sequentially (`directive-001.md`, `directive-002.md`, ...)
- [ ] Stored in `Workflow06/directives/`
- [ ] The COO agent's first job every morning is to read new directives and translate them into cron jobs

### 3.3 Implement Method 0 pricing
- [ ] **Method 0 = sell the agent, not the output.** The customer gets a working AI employee, not a one-off deliverable.
- [ ] Pricing: $5K/website, $10K/month for a full agent team
- [ ] Bundle structure: starter ($2K), growth ($5K/month), scale ($10K/month), enterprise (custom)
- [ ] Sales motion: 30-min demo → 2-week pilot → monthly contract

### 3.4 Build the agency gBrain
- [ ] **One brain** = the shared `BRAIN.md` + `EMPLOYEE_MANIFESTO.md` + directive list
- [ ] **Scoped agents** = each agent has a `SCOPE.md` listing what it can/cannot do
- [ ] **Isolated client pods** = each client gets their own git worktree + Obsidian sub-vault + cron namespace
- [ ] **Less drift** = monthly directive audit; agents that drift are re-scoped or replaced
- [ ] **More leverage** = one CEO + N agents can serve N clients; the CEO only handles approvals

### 3.5 Build the directive-to-cron translator
- [ ] COO agent reads new directive
- [ ] Decomposes into 1–N cron jobs (each with: name, schedule, prompt, skills, delivery)
- [ ] Creates the cron via `hermes cron create`
- [ ] Logs the directive → cron mapping in `Workflow06/directive-cron-map.md`

### 3.6 Build the reporting structure
- [ ] Every agent reports weekly: what they did, what they blocked on, what they need
- [ ] Reports are filed in `Workflow06/reports/<agent-slug>/<week>.md`
- [ ] CEO reviews the roll-up every Sunday
- [ ] Roll-up is auto-generated by `weekly-review` cron (already defined in Workflow 01)

### 3.7 Daily outputs committed to GitHub
- [ ] `Workflow06/directives/sequential/<NNN>-<slug>.md` — every directive
- [ ] `Workflow06/reports/<agent-slug>/YYYY-Www.md` — weekly agent reports
- [ ] `Workflow06/revenue/YYYY-MM.md` — monthly MRR, customer count, churn

## 4. Verification

- [ ] Org chart is complete and unambiguous
- [ ] Every directive has all 7 required fields
- [ ] Method 0 pricing page is live
- [ ] First paying customer closed

## 5. Success criteria (per quarter)

- [ ] 1 directive shipped per week (4 per month)
- [ ] $10K MRR achieved
- [ ] 5 paying customers
- [ ] 0 client pods drifted (all still on their original SCOPE.md)
