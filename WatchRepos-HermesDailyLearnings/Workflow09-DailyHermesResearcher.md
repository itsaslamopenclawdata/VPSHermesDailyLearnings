# Workflow 09 — Daily Hermes Researcher

> **Source repos:** `MyHermesResearcher`
> **Run mode:** FIRST-PASS FULL INGESTION
> **Last updated:** 2026-06-09
> **WatchRepos iteration:** 1

---

## 1. Purpose

The **prompts + workflows** library — a curated set of 20 daily-driver prompts, 3 playbooks (AI audit consulting, browser agents reality, etc.), and thousands of learning artifacts. The operational brain of the research layer.

## 2. Source repos and what they teach

### `MyHermesResearcher` (largest — 9,306 files, 6,491 .md)
- **Files:** 8273 · **.md count:** 6491 · **Last commit:** `01e32dc9` · 2026-06-09 · "Morning pain audit: 2026-06-09"
- **Theme:** 20 daily Claude prompts, browser agents reality, AI audit consulting playbook, deep learnings
- **Key files:** `CLAUDE_DAILY_PROMPTS_WORKFLOWS.md`, `AI_AUDIT_CONSULTING_PLAYBOOK.md`, `browser-agents-reality-playbook.md`, `SKILLS-QUICKSTART.md`, `LearningsDetails-2026-04-24.md`

> **Excerpt from `CLAUDE_DAILY_PROMPTS_WORKFLOWS.md`:**
> # 20 Claude Prompts, Workflows & Automations — Daily Driver Edition

## Overview

Most prompt collections are academic — someone generates 200 prompts, tests none of them, and posts the list for engagement. This is different. Every item here is used daily or weekly, consistently, for months. If a prompt stopped working or a workflow wasn't worth the effort, it got cut. What remains are the 20 that

> **Excerpt from `AI_AUDIT_CONSULTING_PLAYBOOK.md`:**
> # AI Audit Consulting Playbook: Hermes Agent Implementation Guide

## The Business Model in 60 Seconds

Sell $$999 AI Tools Assessments to small businesses → 60% upgrade to $$3K-10K implementation → Work 15-20 hrs/week → Make $$10K-15K/month.

The core value prop: **translation gap arbitrage** — bridge the gap between "AI tools exist" and "here's exactly what to set up for YOUR business."

---

## St

> **Excerpt from `browser-agents-reality-playbook.md`:**
> # Browser Agents: The Reality of Building and Monetizing at Scale

There's a massive gap between what users think browser agents can do today and reality. You can replace your 100-person offshore form-filling team, but not with a 3-sentence prompt and 15 minutes. There's no playbook for when browser agents don't do what you tell them to — and in high-stakes environments, that's where it all falls 

## 3. Detailed TODO ACTION STEPS — Build the Harness

### 3.1 Catalog the 20 daily prompts
- [ ] For each prompt, document: name, use-case, when to use, model recommendation, expected output
- [ ] Group by: research, writing, coding, analysis, customer-facing, internal
- [ ] Tag with: required skills, output schema, quality bar
- [ ] Build a `/prompt <name>` slash command that loads the prompt + skills

### 3.2 Build the 3 playbooks
- [ ] **AI Audit Consulting Playbook** — how to scope, price, deliver an AI audit for an SMB
- [ ] **Browser Agents Reality Playbook** — what's actually possible with browser-using agents in 2026, what isn't, when to use them
- [ ] **Daily Workflow Playbook** — the 20 prompts organized into a daily rhythm

### 3.3 Build the learnings index
- [ ] `LearningsIndex.md` — every `LearningsDetails-*.md` file, tagged by date and topic
- [ ] `/learn <date or topic>` — search the learnings
- [ ] Cron: weekly — `learnings-summary` — surfaces the top 3 new learnings from the week

### 3.4 Build the skills quickstart
- [ ] Mirror `SKILLS-QUICKSTART.md` structure
- [ ] For each bundled skill: 1-paragraph description, when to load, example invocation
- [ ] Add a `/skills-search <query>` command that uses `hermes skills search`

### 3.5 Build the daily prompt rotation
- [ ] Cron: daily 08:00 — `daily-prompt-picker` — picks the prompt-of-the-day based on:
  - Day of week (Monday = research, Tuesday = writing, etc.)
  - Outstanding tasks in the kanban
  - Recent learnings that need follow-up
- [ ] Delivers the prompt + a filled-in template to Telegram

### 3.6 Build the prompt quality loop
- [ ] Track: prompt name, use count, satisfaction score, time saved
- [ ] Weekly: identify underperforming prompts (low satisfaction, high time)
- [ ] Iterate: rewrite, retest, redeploy

### 3.7 Daily outputs committed to GitHub
- [ ] `Workflow09/prompt-of-the-day/YYYY-MM-DD.md`
- [ ] `Workflow09/learnings-new/YYYY-MM-DD.md`
- [ ] `Workflow09/prompt-quality/weekly-YYYY-Www.md`

## 4. Verification

- [ ] 20 prompts cataloged with all required metadata
- [ ] 3 playbooks published
- [ ] First prompt-of-the-day delivered

## 5. Success criteria (per month)

- [ ] 30 prompt-of-the-day delivered
- [ ] 5 prompts iterated (rewritten based on quality data)
- [ ] 3 new learnings added to the index
- [ ] 1 new playbook published
