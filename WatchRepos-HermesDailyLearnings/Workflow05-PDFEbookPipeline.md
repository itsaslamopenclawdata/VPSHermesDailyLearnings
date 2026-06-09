# Workflow 05 — PDF / Ebook Generation Pipeline

> **Source repos:** `Ebook_EntireVibePipepline`, `UltraPDFGenSkill`, `MyPaperclipOutputs`
> **Run mode:** FIRST-PASS FULL INGESTION
> **Last updated:** 2026-06-09
> **WatchRepos iteration:** 1

---

## 1. Purpose

End-to-end pipeline that turns a topic into a publishable ebook / PDF: backend schemas, content agent testing, CI/CD, API integration testing. This is the **monetization** workflow — every published ebook generates revenue.

## 2. Source repos and what they teach

### `Ebook_EntireVibePipepline`
- **Files:** 177 · **.md count:** 70 · **Last commit:** `24aea04c` · 2026-02-26 · "Update Next_steps with completion status"
- **Theme:** Vibe PDF Platform backend, Pydantic schemas, CI/CD, API integration testing
- **Key files:** `SCHEMA_ANALYSIS_REPORT.md`, `CONTENT_AGENT_TESTING_REPORT.md`, `CI_CD_WORKFLOW_REPORT.md`, `API_INTEGRATION_TEST_REPORT.md`
- **Learnings:** 22 Pydantic schemas across 4 domain modules; comprehensive field validation with constraints; custom validators for data sanitization. Content agent has full testing harness. CI/CD with quality gates before deploy. API integration tests cover all endpoint contracts.

> **Excerpt from `SCHEMA_ANALYSIS_REPORT.md`:**
> # Pydantic Schemas Testing Report
## Vibe PDF Platform - Backend

**Generated:** 2026-02-17
**Schema Directory:** `Backend/app/schemas/`
**Total Schemas:** 22 schemas across 4 domain modules

---

## Executive Summary

The Vibe PDF Platform has a comprehensive, well-structured Pydantic schema implementation covering all major domain entities. All schemas follow Pydantic v2 conventions with proper 

> **Excerpt from `CONTENT_AGENT_TESTING_REPORT.md`:**
> # Content Agent Testing Report - US-AI-002

**Test Date:** 2026-02-17
**Component:** Content Writer Agent (`Backend/app/agents/content_agent.py`)
**Requirements:** US-AI-002 Chapter Content Writing

---

## Executive Summary

The Content Writer Agent has been thoroughly analyzed and tested against US-AI-002 requirements. The implementation demonstrates **full compliance** with all specified requir

> **Excerpt from `CI_CD_WORKFLOW_REPORT.md`:**
> # CI/CD Workflow Report - Vibe PDF Platform Testing

**Date:** 2026-02-20
**Project:** Vibe PDF Book Generation Platform
**Component:** Comprehensive Testing Pipeline
**Workflow File:** `.github/workflows/test.yml`

---

## Executive Summary

Successfully implemented a comprehensive GitHub Actions workflow for automated testing of the Vibe PDF Platform frontend application. The workflow provides m

### `UltraPDFGenSkill` (covered in detail in Workflow 04)
- Reuses: 28 specialized agents, orchestrator, critique agent, 50x critique depth

### `MyPaperclipOutputs` (output archive)
- Refined PDF outputs land here. Don't commit full PDFs to the source repo — just metadata, cover image, and a download link.

## 3. Detailed TODO ACTION STEPS — Build the Harness

### 3.1 Define the 5 pipeline stages
- [ ] **Stage 1: Topic** — input is a topic string, an audience, and a target quality tier ($40, $100, $400)
- [ ] **Stage 2: Outline** — orchestrator generates a 10–20-chapter outline; critic reviews; iterate
- [ ] **Stage 3: Content** — 28 specialist agents write each section in parallel; critic reviews; iterate (up to 50 rounds)
- [ ] **Stage 4: Polish** — copy editor, fact-checker, formatting, cover designer
- [ ] **Stage 5: Publish** — render to PDF, generate landing page, set up Stripe checkout, write launch copy

### 3.2 Build the Pydantic schemas (mirror Vibe PDF's 22)
- [ ] `Topic` — topic, audience, quality_tier, target_length
- [ ] `Outline` — chapters list, each with title, summary, target_words
- [ ] `Section` — chapter_id, content, sources, citations
- [ ] `Critique` — section_id, score_per_criterion, issues list, suggestions
- [ ] `Ebook` — title, author, chapters list, cover_image_url, pdf_url
- [ ] `Order` — customer_email, ebook_id, amount, stripe_charge_id, download_url

### 3.3 Build the content agent test harness
- [ ] Given a topic + outline, generate Section A
- [ ] Run 5 critique rounds on Section A
- [ ] Verify: word count within ±10% of target, all citations valid, no plagiarism, tone consistent
- [ ] Auto-fail if any criterion scores < 8/10

### 3.4 Set up the CI/CD pipeline
- [ ] GitHub Actions: on every push to main, run unit tests + integration tests
- [ ] Pre-deploy gate: every schema change requires migration script
- [ ] Deploy target: Coolify on Oracle VPS (already set up per Workflow 01)
- [ ] Smoke test after deploy: hit `/healthz`, run a 1-chapter generation end-to-end

### 3.5 Build the API integration tests
- [ ] Cover all 22 schema endpoints (create, read, update, delete for each)
- [ ] Cover the Stripe webhook → Order creation → download link flow
- [ ] Cover the email delivery (Resend or Postmark) flow
- [ ] Auto-fail CI on any test regression

### 3.6 Build the launch sequence
- [ ] Landing page: hero, problem, solution, sample chapter, testimonials, pricing, FAQ
- [ ] Email sequence: 5 emails over 14 days (welcome, value, story, scarcity, close)
- [ ] Social posts: 1 LinkedIn, 1 Twitter thread, 1 Reddit post (in relevant subs)
- [ ] Paid acquisition budget: $50/day for 7 days, pause if ROAS < 2

### 3.7 Daily outputs committed to GitHub
- [ ] `Workflow05/ebooks-published/YYYY-MM-DD.md` — books published today
- [ ] `Workflow05/revenue/YYYY-MM-DD.md` — orders, MRR, conversion rate
- [ ] `Workflow05/quality-scores/YYYY-MM-DD.md` — quality score distribution across all published books

## 4. Verification

- [ ] Full pipeline runs end-to-end on a test topic in < 4 hours
- [ ] Generated ebook scores ≥ 95/100 on the quality rubric
- [ ] Landing page loads in < 2s, Stripe checkout works
- [ ] CI/CD green on the main branch

## 5. Success criteria (per month)

- [ ] 1 ebook published
- [ ] 10 units sold (revenue ≥ $400 if priced at $40)
- [ ] Quality score median ≥ 95/100
- [ ] 0 schema-breaking changes in production
