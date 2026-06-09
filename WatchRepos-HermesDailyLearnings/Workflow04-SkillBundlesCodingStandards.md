# Workflow 04 — Skill Bundles & Coding Standards

> **Source repos:** `CodingDeveloperRules`, `UltraPDFGenSkill`, `MyPaperclipOutputs`
> **Run mode:** FIRST-PASS FULL INGESTION
> **Last updated:** 2026-06-09
> **WatchRepos iteration:** 1

---

## 1. Purpose

Define the **skill bundle** primitive — a packaged set of skills + skills-for-skills + operational rules that any agent can load as one unit. The system also includes a **multi-agent race condition** spec (when multiple agents touch the same file) and a **content amplification** rule set for shipping.

## 2. Source repos and what they teach

### `CodingDeveloperRules`
- **Files:** 24 · **.md count:** 19 · **Last commit:** `5fee6526` · 2026-06-01 · "feat(skill-bundles): add content-amplification-pipeline + build-with-confidence bundles - 2026-06-01"
- **Theme:** Skill bundles, multi-agent race conditions, content amplification, daily intelligence
- **Key files:** `SkillBundles/SKILL-BUNDLE-ARCHITECTURE.md`, `SkillBundles/build-with-confidence.md`, `SkillBundles/solopreneur-daily-intelligence.md`, `SkillBundles/aslamskillidentifier-skill-bundle-2026-05-22.md`

> **Excerpt from `SkillBundles/SKILL-BUNDLE-ARCHITECTURE.md`:**
> # Skill Bundle Architecture — Full Reference

> **Purpose:** Complete documentation of the skill bundle system for autonomous application building in Hermes Agent. Covers the original skill table analysis, recommended bundles, manual intervention map, and why Hermes Agent is the right execution layer for solo operator workflows.

**Last Updated:** May 2026
**Repo:** [CodingDeveloperRules](https://

> **Excerpt from `SkillBundles/build-with-confidence.md`:**
> # Build With Confidence

**Generated:** 2026-06-01  
**Bundle Slug:** `/build-with-confidence`  
**Category:** software development + production deployment

---

## Trigger

When to use this bundle: You have a SPEC.md and a plan, and you're ready to implement. This is the BUILD phase of the full spec-to-production pipeline — it assumes the spec exists and the plan is defined. If no spec exists, us

### `UltraPDFGenSkill`
- **Files:** 8 · **.md count:** 4 · **Last commit:** `088413df` · 2026-04-06 · "UltraPDFGen v10.0: 100x Premium PDF Generation System"
- **Theme:** UltraPDFGen v10.0 — 100x PDF generation, 28 specialized agents, 50x critique depth
- **Key files:** `SKILL.md`, `agents/orchestrator.md`, `agents/critique_agent.md`

> **Excerpt from `SKILL.md`:**
> # UltraPDFGen Skill v10.0 — 100x Premium PDF Generation System

**Version:** 10.0.0  
**Quality Standard:** $$400+ Ultra Premium  
**Performance Multiplier:** 100x Agent Capacity | 50x Critique Depth  
**Generated:** 2026-04-06  
**Overall Quality Score:** 99.2/100  

---

## Executive Summary

UltraPDFGen represents a quantum leap in AI-powered document generation. Where the original PDFGen skill 

> **Excerpt from `agents/orchestrator.md`:**
> # UltraPDFGenOrchestrator Agent (AGT-001)

**Role:** MetaOrchestrator — Central coordinator for 100x PDF generation pipeline

---

## 100x Capability Enhancements

The UltraOrchestrator represents a quantum leap from the original PDFGenOrchestrator:

| Metric | Original | Ultra (100x) |
|--------|----------|--------------|
| Agents Coordinated | 14 | 28 |
| Coordination Rounds | 1 | 7 (adaptive) |

> **Excerpt from `agents/critique_agent.md`:**
> # UltraCritiqueAgent (AGT-027) — 50-Round Deep Analysis System

**Role:** Premium quality auditor performing 50 sequential critique rounds

---

## 50x Critique Depth: A Revolutionary Approach

The UltraCritiqueAgent performs **50 sequential critique rounds**, each with progressive depth. This is a 50x improvement over the original critique system.

### Critique Rounds Breakdown

| Phase | Rounds 

### `MyPaperclipOutputs`
- **Files:** 1 · **.md count:** 1 · **Last commit:** `c454ca51` · 2026-04-04 · "Add PopularPDFRefinedOutputs folder"
- **Theme:** Refined PDF outputs (output-only archive)
- **Learnings:** Outputs go here; skills go in the source repos. Keep them separate.

## 3. Detailed TODO ACTION STEPS — Build the Harness

### 3.1 Define the Skill Bundle schema
- [ ] **Bundle manifest** (`bundle.yaml`): name, version, description, primary_skills, supporting_skills, required_toolsets, agent_roles, input_schema, output_schema
- [ ] **SKILL.md** at the bundle root: human-readable overview, when to load, what it produces
- [ ] **agents/**: one MD per agent role (orchestrator, critic, specialist X, ...)
- [ ] **examples/**: 2–3 worked examples of the bundle in action
- [ ] **tests/**: 5+ unit tests for the bundle's deterministic pieces

### 3.2 Author 3 starter bundles
- [ ] `solopreneur-daily-intelligence` — daily content + lead + ops
- [ ] `aslamskillidentifier` — auto-detect and install the right skills for a task
- [ ] `content-amplification` — turn one idea into 10 distribution-ready assets

### 3.3 Solve the multi-agent race condition
- [ ] Define ownership: every file in a multi-agent workspace has exactly one primary owner
- [ ] Define merging: if two agents must write to the same file, one writes a section, the other appends, never both overwrite
- [ ] Define locks: for files that can't be safely merged (e.g. JSON config), use file locks or queue-based serialization
- [ ] Add a `requesting-code-review` step to every PR — it's the deconfliction mechanism

### 3.4 Build the PDF generation bundle (UltraPDFGen pattern)
- [ ] 28 specialized agents: each handles a section type (cover, TOC, executive summary, market analysis, financials, appendix, ...)
- [ ] Orchestrator: routes content to agents, assembles the final PDF
- [ ] Critique agent: 50x critique depth — every section is reviewed 50 times against a quality rubric
- [ ] Target output: $400+ premium quality, 99/100 quality score
- [ ] Track: time-to-generate, cost-per-generation, quality score, customer-satisfaction

### 3.5 Bundle lifecycle
- [ ] v0.1 — internal use only, no public docs
- [ ] v0.5 — internal + select power users
- [ ] v1.0 — public, with full docs, examples, tests
- [ ] v1.x — backward-compatible additions
- [ ] v2.0 — breaking changes, migration guide required

### 3.6 Bundle registry
- [ ] Create `Workflow04/bundle-registry.md` — list of all bundles, version, status, owner
- [ ] Cron: weekly — `bundle-health-check` — verifies each bundle's dependencies are present, no broken examples
- [ ] Add a `/bundle <name>` slash command that loads a bundle + its dependencies

### 3.7 Daily outputs committed to GitHub
- [ ] `Workflow04/bundle-changelog/YYYY-MM-DD.md` — bundles updated today
- [ ] `Workflow04/race-condition-log/YYYY-MM-DD.md` — any deconfliction events
- [ ] `Workflow04/published-outputs/...` — sample PDFs (don't commit full PDFs; commit metadata + cover image)

## 4. Verification

- [ ] 3 starter bundles load and run their canonical examples successfully
- [ ] Bundle registry is up to date
- [ ] Multi-agent test scenario produces no race conditions (run 5x)
- [ ] UltraPDFGen-style PDF bundle produces a 99/100 quality document on the test case

## 5. Success criteria

- [ ] 5 bundles published (v1.0+) within 90 days
- [ ] 1 bundle used by ≥ 3 different agents/workflows
- [ ] 0 race conditions in the multi-agent test scenario over 30 runs
