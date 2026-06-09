# 50x Patterns Library — Distilled from 18 Watch Repos

> **Goal:** Make Hermes Agent 50× more productive by encoding proven patterns from the user's own watchlist into executable primitives.
> **Version:** 1.0 · **Date:** 2026-06-03
> **Source:** All 18 watch repos (see `00-SOURCE-MAP.md`)
> **License:** MIT

---

## How to read this file

Each pattern is **numbered P01–P50** and has the same structure:

```
P## — <Name>                                     (expected multiplier)
Source: <repo> → <file>
When: <trigger condition>
What: <one-line description>
How: <3-7 step recipe, with a copy-pasteable command>
Verify: <how to know it worked>
Dead signal: <when to prune this pattern>
```

Patterns are grouped by the source repo that originated them. The grouping does **not** limit which patterns apply where — most are cross-cutting. Use `grep -E "^P[0-9]+" /path/to/this/file.md` to see the full list, or `grep -A 5 "^P27" file.md` to inspect one.

**Multiplier conventions** (these are targets, not guarantees):
- 2× = doubles throughput (saves 1 step)
- 5× = saves 80% of the work (replaces a workflow)
- 10× = replaces a 1-person task (parallelizes what was serial)
- 50× = replaces a 5-person team (multiplies the agent's effective headcount)

---

## Index — All 50 Patterns

| # | Name | Source | Mult |
|---|---|---|---|
| P01 | AGENT_SKILLS_MATRIX as canonical role→capabilities map | TwitterResearcherMyHermesAgent | 5× |
| P02 | Master cron job list as single source of scheduling truth | TwitterResearcherMyHermesAgent | 5× |
| P03 | 14-day TODO arc as bounded work envelope | TwitterResearcherMyHermesAgent | 3× |
| P04 | Pain-extract → Validate → Narrate → Publish pipeline | TwitterResearcherMyHermesAgent | 10× |
| P05 | GEO Audit Factory pattern (one input → many outputs) | TwitterResearcherMyHermesAgent | 10× |
| P06 | "The Drip" low-pressure distribution | TwitterResearcherMyHermesAgent | 2× |
| P07 | Daily standup as cron-driven structured report | MyHermesResearcher | 3× |
| P08 | 20 daily-driver prompts as curated pattern set | MyHermesResearcher | 5× |
| P09 | AI Audit Consulting Playbook (scope→price→deliver) | MyHermesResearcher | 10× |
| P10 | Browser agents reality-check before promising them | MyHermesResearcher | 2× |
| P11 | "Learnings" file with date + topic tag | MyHermesResearcher | 2× |
| P12 | The 7-engine 10x Growth System (modular personal OS) | AslamTheEliteLeader | 10× |
| P13 | Daily Learning Accelerator (curated paper digests) | AslamTheEliteLeader | 3× |
| P14 | Knowledge Assimilation Engine (auto-notes format) | AslamTheEliteLeader | 3× |
| P15 | Opportunity Scanner with HOT/GROWING/COLD tiers | AslamTheEliteLeader | 5× |
| P16 | Communication Automation at scheduled times | AslamTheEliteLeader | 2× |
| P17 | Auto-Coding-Assistant daily challenge | AslamTheEliteLeader | 2× |
| P18 | Habit & Accountability Coach (morning + evening ping) | AslamTheEliteLeader | 2× |
| P19 | The 1-man-business Employee Manifesto | MyDayWorking | 5× |
| P20 | "While I was sleeping..." morning recap cron | MyDayWorking | 2× |
| P21 | Master BRAIN.md (single index of all repos + agents) | Daily-Working-Space | 5× |
| P22 | HEARTBEAT.md (every cron appends a line) | Daily-Working-Space | 3× |
| P23 | 10X_PLAN.md (track 10 businesses) | Daily-Working-Space | 5× |
| P24 | Identity files (SOUL.md, IDENTITY.md) | Daily-Working-Space | 2× |
| P25 | Skill Bundle = name + skills + skills-for-skills + examples | CodingDeveloperRules | 10× |
| P26 | Solopreneur Daily Intelligence (4-skill chain) | CodingDeveloperRules | 10× |
| P27 | Aslamskillidentifier (find best skills for any task) | CodingDeveloperRules | 5× |
| P28 | Race condition spec (file ownership + merge strategy) | CodingDeveloperRules | 5× |
| P29 | UltraPDFGen pattern: 28 specialists + 50x critique | UltraPDFGenSkill | 50× |
| P30 | Quality rubric pre-flight (99/100 target) | UltraPDFGenSkill | 5× |
| P31 | Pydantic schema as contract (22 schemas) | Ebook_EntireVibePipepline | 5× |
| P32 | 5-stage publish pipeline (Topic→Outline→Content→Polish→Publish) | Ebook_EntireVibePipepline | 10× |
| P33 | CI/CD with quality gate before deploy | Ebook_EntireVibePipepline | 3× |
| P34 | API integration test matrix | Ebook_EntireVibePipepline | 2× |
| P35 | Company Orchestration = CEO directives + agent org chart | company-orchestration | 10× |
| P36 | Method 0 pricing (sell agent, not output) | company-orchestration | 10× |
| P37 | Directive format (Objective+Background+Deliverables+…) | company-orchestration | 3× |
| P38 | Agent org chart with explicit reports-to | company-orchestration | 2× |
| P39 | 6-stage content production (Research→Brainstorm→Structure→Draft→Review→Publish) | VentureHQ | 10× |
| P40 | @VenturescoreBot in < 60s with score + decision | VentureHQ | 3× |
| P41 | 20-agent parallel evaluation panel (delegate_task batch) | VentureHQ | 10× |
| P42 | YouTube channels registry as upstream intelligence | MyWorkflowsIntelligenceLayer | 5× |
| P43 | Insight extraction: 1–3 per source, scored 1–10 | MyWorkflowsIntelligenceLayer | 3× |
| P44 | Routing layer (insight → downstream workflow) | MyWorkflowsIntelligenceLayer | 5× |
| P45 | Task-assignment template (Objective+Background+Deliverables+Format) | content-pipeline | 2× |
| P46 | Fit × Intent = Composite lead score | research-feed | 5× |
| P47 | 5-bot flagship content team (each has a clear role) | Content-Generation-Collab | 5× |
| P48 | "Git log heartbeat" as health check | Daily-Working-Space | 2× |
| P49 | Single "Use the source" rule (knowledge-base-first) | Quantum-Learning-Collab | 5× |
| P50 | Single-profile, two-workflow architecture | HermesOracleVPS | 10× |

**Total expected multiplier when all 50 are active: 50× (vs. baseline agent).**

---

# PATTERNS

## Group 1: Twitter Research (P01–P06) — From `TwitterResearcherMyHermesAgent`

### P01 — AGENT_SKILLS_MATRIX as canonical role→capabilities map
Source: `TwitterResearcherMyHermesAgent/AGENT_SKILLS_MATRIX.md`
When: Adding a new agent, or when an existing agent keeps picking the wrong skills.
What: One MD file that lists every agent, with primary skills (must-load), supporting skills (context), and toolset. The agent's "I am what I know" document.
How:
1. Create `WorkflowXX/AGENT_SKILLS_MATRIX.md`
2. For each agent, write 3 columns: Primary Skills, Supporting Skills, Toolset
3. Add a "When to load me" line per agent
4. The orchestrator's first move is to look up the agent in this matrix before invoking
Verify: Every agent invocation can be traced to a row in the matrix
Dead signal: Agent picks skills not in its matrix (matrix is out of date)

### P02 — Master cron job list as single source of scheduling truth
Source: `TwitterResearcherMyHermesAgent/mastercronjobslist.md`
When: ≥ 3 cron jobs, or when "which cron is responsible for X?" is asked more than once
What: One MD file with every cron job: name, schedule, prompt, skills, deliver. New crons get appended. Old crons are marked deprecated.
How:
1. Create `WorkflowXX/mastercronjobslist.md`
2. Header table: `| Name | Schedule | Prompt | Skills | Deliver | Status |`
3. On every `hermes cron create`, append a row
4. On every cron delete/move, update the row
Verify: `grep -c "^| " mastercronjobslist.md` equals `hermes cron list | wc -l` ± 1
Dead signal: Drift between file and `hermes cron list` > 10%

### P03 — 14-day TODO arc as bounded work envelope
Source: `TwitterResearcherMyHermesAgent/14DaysGoalsTODO/`
When: Starting any new initiative that has more than 7 sub-tasks
What: 14-day scope. Anything outside is parked. Forces focus and prevents bloat.
How:
1. Create `WorkflowXX/14days-todo/`
2. List every deliverable for the next 14 days
3. Each deliverable has: owner, deadline, status
4. At day 14, archive what didn't ship; start a new 14-day arc
Verify: At day 14, ≤ 5% of items rolled over
Dead signal: Rollovers > 20% (you're scoping wrong)

### P04 — Pain-extract → Validate → Narrate → Publish pipeline
Source: `TwitterResearcherMyHermesAgent` (pipeline pattern)
When: Building any content or product
What: 4-stage pipeline: raw signal → pain → validated problem → content/product
How:
1. Stage 1 — **Feed fetcher** (hourly cron): pull 50+ posts from tracked sources
2. Stage 2 — **Pain extractor** (daily 06:00): rank top 5 pains with verbatim quotes
3. Stage 3 — **Validator** (daily 09:00): score each pain (volume, WTP, market size)
4. Stage 4 — **Narrator/Publisher** (daily 11:00): turn the top pain into a tweet thread, blog post, or product spec
Verify: Each stage's output is a file the next stage reads; pipeline runs end-to-end in < 1 hour
Dead signal: A stage's output is consistently empty (input is wrong)

### P05 — GEO Audit Factory pattern (one input → many outputs)
Source: `TwitterResearcherMyHermesAgent/14DaysGoalsTODO/GEO-Audit-Factory/`
When: Need to produce many similar deliverables from one input
What: One "input spec" + a templated output generator. Each output is a unique artifact but follows a fixed structure.
How:
1. Define the input schema (e.g. `{company_name, url, industry, products[]}`)
2. Define N output templates (e.g. SEO audit, content audit, tech-stack audit, social audit)
3. For each input, run all N templates; produce N distinct files
4. Store all outputs in `WorkflowXX/factory-outputs/<input-slug>/`
Verify: 1 input → N outputs, each with 80%+ completion
Dead signal: Templates drift from input schema (refactor needed)

### P06 — "The Drip" low-pressure distribution
Source: `TwitterResearcherMyHermesAgent/14DaysGoalsTODO/The-Drip/`
When: Need sustained distribution without daily content creation
What: Pre-write 30 days of content, then "drip" it out via cron
How:
1. Spend 2 days writing 30 posts
2. Set up a cron that posts 1/day from the queue
3. Track which posts perform; double down on winners
Verify: 30 days of consistent output with < 30 min/day of manual work
Dead signal: Engagement drops monotonically (content is stale)

---

## Group 2: Daily Hermes Researcher (P07–P11) — From `MyHermesResearcher`

### P07 — Daily standup as cron-driven structured report
Source: `MyHermesResearcher/CLAUDE_DAILY_PROMPTS_WORKFLOWS.md`
When: Want visibility into what the agent did yesterday without asking
What: A cron that runs at 08:00 and produces a structured standup: Done / Planned / Blockers
How:
1. `hermes cron create "0 8 * * *"` — `daily-standup`
2. Prompt: "Inspect the last 24h of git log, kanban, and any output folders. Produce a standup: ## Done (yesterday) ## Planned (today) ## Blockers. Save to `~/Documents/<Vault>/daily-standups/<date>.md` and post a 3-bullet summary to Telegram."
3. Skills: `terminal, file, kanban, obsidian, session_search`
Verify: Every morning at 08:00 you have a 3-bullet Telegram message + a full MD
Dead signal: Standup becomes repetitive (agent is doing nothing new)

### P08 — 20 daily-driver prompts as curated pattern set
Source: `MyHermesResearcher/CLAUDE_DAILY_PROMPTS_WORKFLOWS.md`
When: Want a high-signal set of prompts that work for a solopreneur
What: 20 carefully chosen prompts (out of 200+ candidates) covering research, writing, coding, analysis, customer-facing, internal
How:
1. Copy the 20 prompts from the source
2. For each, document: name, use case, model, expected output
3. Build a `/prompt <name>` slash command that loads it
Verify: 20 prompts cataloged, each tested once
Dead signal: A prompt is never used (delete it)

### P09 — AI Audit Consulting Playbook (scope→price→deliver)
Source: `MyHermesResearcher/AI_AUDIT_CONSULTING_PLAYBOOK.md`
When: Selling AI services to SMBs
What: 5-step process: Discovery → Audit → Roadmap → Implementation → Handoff. Each has a price.
How:
1. Build `WorkflowXX/ai-audit-playbook.md`
2. Define the 5 steps with deliverables, time, price
3. For each client, create `<client-slug>/01-discovery/`, `02-audit/`, ...
4. Total price = sum of step prices; offer as a package
Verify: First audit sold, delivered, paid
Dead signal: Steps take 2x the planned time (scope creep)

### P10 — Browser agents reality-check before promising them
Source: `MyHermesResearcher/browser-agents-reality-playbook.md`
When: User asks "can your agent do X on a website?"
What: A pre-flight test that confirms the browser agent can do X before promising the user
How:
1. Have a 5-step reliability test for the browser agent
2. Run the test before promising any browser-based capability
3. If reliability < 80%, say "I can do this 80% of the time" instead of "I can do this"
Verify: No user is disappointed by a browser-agent failure
Dead signal: Failure rate > 20% on the canonical tasks

### P11 — "Learnings" file with date + topic tag
Source: `MyHermesResearcher/LearningsDetails-2026-04-24.md`
When: Discover something non-obvious that's worth keeping
What: One MD per learning, with: date, source, insight, why-it-matters, action
How:
1. Naming: `LearningsDetails-YYYY-MM-DD-<topic-slug>.md`
2. Schema: `## Source ## Key Insight ## Why It Matters ## Action Item`
3. Index in `LearningsIndex.md` (auto-updated)
4. `/learn <topic>` slash command searches the index
Verify: ≥ 1 learning/week; index always current
Dead signal: Learnings are restating obvious things (skip them)

---

## Group 3: AslamTheEliteLeader 10x Growth (P12–P18)

### P12 — The 7-engine 10x Growth System (modular personal OS)
Source: `AslamTheEliteLeader/README.md`
When: Building a personal operating system with multiple concerns (learning, business, skills, etc.)
What: 10 modular sub-engines that each handle one concern. Each has a cron, an output folder, a dashboard.
How:
1. List the 10 concerns (Daily Learning, Business Intel, Skill Stack, Research, Pipeline Tracking, Knowledge Assimilation, Opportunity Scanner, Communication, Coding, Habit Coach)
2. For each, create a folder + a cron + a dashboard MD
3. The daily schedule (7:00 AM – 11:00 AM) executes one engine per slot
Verify: All 10 engines have a cron + output folder + dashboard
Dead signal: Some engines never produce output (drop or merge them)

### P13 — Daily Learning Accelerator (curated paper digests)
Source: `AslamTheEliteLeader/01-Daily-Learning-Accelerator/README.md`
When: Need to stay current in a fast-moving field
What: Daily cron that fetches N papers, extracts 3 takeaways each, posts to Telegram
How:
1. `hermes cron create "30 8 * * *"` — `daily-learning`
2. Prompt: "Use the arxiv skill to fetch 5 papers from <categories>. For each, extract: title, 3-bullet summary, 1-line action. Post to Telegram. Save full digest to `~/Documents/<Vault>/learning/papers/<date>.md`."
3. Skills: `arxiv, obsidian`
Verify: Every morning at 08:30, Telegram has a 15-bullet digest
Dead signal: You're not reading the digests (drop or batch them)

### P14 — Knowledge Assimilation Engine (auto-notes format)
Source: `AslamTheEliteLeader/06-Knowledge-Assimilation-Engine/README.md`
When: Consuming content (video, article, paper) and want to keep the takeaways
What: Standard schema for notes: `## Source ## Key Points ## Why It Matters ## Action Item`
How:
1. Use the schema for every note
2. Auto-create the MD from any input via the `obsidian` skill
3. Spaced-repetition reminders for important notes
Verify: 100% of notes follow the schema
Dead signal: Schema is bypassed (just add a checklist to enforce it)

### P15 — Opportunity Scanner with HOT/GROWING/COLD tiers
Source: `AslamTheEliteLeader/07-Opportunity-Scanner/README.md`
When: Looking for revenue opportunities in the market
What: Cron that scans 6 sources (Upwork, Fiverr, LinkedIn, GitHub, PH, Twitter), tags each opportunity as 🔥 HOT / 📈 GROWING / 💡 INTERESTING / 🧊 COLD
How:
1. Define the 6 sources and what to look for at each
2. Cron: weekly — `opportunity-scan`
3. Output: `WorkflowXX/opportunities/<week>.md` with tiered lists
Verify: ≥ 1 actionable opportunity/week
Dead signal: Tiering is always the same (rubric is broken)

### P16 — Communication Automation at scheduled times
Source: `AslamTheEliteLeader/README.md` (08 System)
When: Need to publish content at consistent times
What: A cron that auto-drafts LinkedIn posts at 7:30 AM, ready for human review/publish
How:
1. `hermes cron create "30 7 * * *"` — `linkedin-draft`
2. Prompt: "Draft a LinkedIn post based on today's learning. Save to `drafts/linkedin/<date>.md`. Tag as 'READY' or 'NEEDS-HUMAN'."
Verify: 7:30 AM every day, you have a draft in the folder
Dead signal: Drafts are never published (kill the cron, draft manually)

### P17 — Auto-Coding-Assistant daily challenge
Source: `AslamTheEliteLeader/README.md` (09 System)
When: Want to keep coding skills sharp
What: Daily 9:00 AM — a small coding challenge (LeetCode-style, 30 min) with a tested solution
How:
1. `hermes cron create "0 9 * * *"` — `daily-code-challenge`
2. Prompt: "Generate a small coding challenge appropriate for a Principal Data Scientist. Provide the problem, a reference solution in Python, and 3 test cases. Post to Telegram."
3. Skills: `claude-code, file`
Verify: 7 challenges/week, ≥ 5 solved
Dead signal: Solved < 50% (challenges too hard)

### P18 — Habit & Accountability Coach (morning + evening ping)
Source: `AslamTheEliteLeader/README.md` (10 System)
When: Want consistent daily habits
What: Cron at 7:00 AM (motivation) and 6:00 PM (check-in). Asks 3 questions each time.
How:
1. `hermes cron create "0 7 * * *"` — `morning-motivation`
2. `hermes cron create "0 18 * * *"` — `evening-checkin`
3. Prompts: "Send a 1-line motivation, ask 3 questions about today's plan" / "Reflect on the day, ask 3 questions about what got done, what didn't, what to adjust"
Verify: 14 pings/week, ≥ 80% response rate from you
Dead signal: You mute the chat (kill the cron)

---

## Group 4: MyDayWorking — Employee Manifesto (P19–P20)

### P19 — The 1-man-business Employee Manifesto
Source: `MyDayWorking/EMPLOYEE_MANIFESTO.md`
When: Defining what the agent team is supposed to do
What: A short document that says: "I am a 1-man business. I work from wake to sleep. I need an employee taking as much off my plate as possible."
How:
1. Copy the manifesto to `WorkflowXX/employee-manifesto.md`
2. Translate every line into a measurable agent behavior
3. Add the behaviors to the AGENTS.md
Verify: Every agent behavior is traceable to a manifesto line
Dead signal: Behaviors that don't trace to the manifesto (drop them)

### P20 — "While I was sleeping..." morning recap cron
Source: `MyDayWorking/EMPLOYEE_MANIFESTO.md` (concrete expression)
When: Want to know what the agent team did overnight
What: A cron at 7:00 AM that summarizes every agent's last 24h of activity
How:
1. `hermes cron create "0 7 * * *"` — `morning-recap`
2. Prompt: "Inspect every agent's last 24h of activity (git log, kanban, output folders). Produce: ## What each agent did ## What was blocked ## What needs your attention. Post to Telegram as a 5-bullet summary."
3. Skills: `terminal, kanban, session_search`
Verify: Every morning, 5 bullets arrive in Telegram
Dead signal: The recap is always empty (agents aren't doing anything)

---

## Group 5: Daily-Working-Space (P21–P24)

### P21 — Master BRAIN.md (single index of all repos + agents)
Source: `Daily-Working-Space/BRAIN.md`
When: Working with > 5 repos or > 5 agents
What: A single MD that lists every repo (purpose, primary agent, current state, last activity) and every agent (role, profile, status)
How:
1. Create `WorkflowXX/BRAIN.md`
2. For each repo: name | purpose | primary agent | last commit | status
3. For each agent: name | role | profile | last output | status
4. Cron: daily 06:00 — refresh from `git log` and `hermes profile list`
Verify: BRAIN.md is current (last refresh < 24h ago)
Dead signal: BRAIN.md has stale rows (refresh failed)

### P22 — HEARTBEAT.md (every cron appends a line)
Source: `Daily-Working-Space/HEARTBEAT.md`
When: Want to verify the cron system is alive
What: Every cron, on completion, appends `[cron-name] alive at <timestamp>` to a shared HEARTBEAT.md
How:
1. Every cron prompt ends with: `echo "[$NAME] alive at $(date -Iseconds)" >> ~/.hermes/heartbeat.md`
2. Cron: every 6h — `heartbeat-check` — alerts if any expected cron hasn't pinged in 24h
Verify: All expected crons show entries in the last 24h
Dead signal: Silent cron > 24h (cron is broken)

### P23 — 10X_PLAN.md (track 10 businesses)
Source: `Daily-Working-Space/10X_PLAN.md`
When: Running multiple business lines in parallel
What: A table with 10 businesses, each with: name, current state, target, weekly delta, owner agent
How:
1. List the 10 businesses (or the 5 you have + 5 aspirational)
2. For each: state, target, owner, this-week-delta
3. Weekly cron updates the deltas
Verify: 1 measurable goal per business moves by ≥ 10% of weekly target
Dead signal: 0 businesses move (drop or replace them)

### P24 — Identity files (SOUL.md, IDENTITY.md)
Source: `Daily-Working-Space/SOUL.md`, `IDENTITY.md`
When: Want every agent to know "who" it is
What: Two short MDs that define the system's values (SOUL) and identity (IDENTITY)
How:
1. `SOUL.md` — 3-5 values, e.g. "ship > study", "customer > tech", "revenue > vanity"
2. `IDENTITY.md` — name, mission, capabilities, non-capabilities
3. AGENTS.md mandates: "Before every response, read SOUL.md and IDENTITY.md"
Verify: Every response aligns with the values
Dead signal: Agent violates a value (rewrite the SOUL or rewrite the agent)

---

## Group 6: CodingDeveloperRules — Skill Bundles (P25–P28)

### P25 — Skill Bundle = name + skills + skills-for-skills + examples
Source: `CodingDeveloperRules/SkillBundles/SKILL-BUNDLE-ARCHITECTURE.md`
When: Need a packaged, reusable unit that any agent can load
What: A directory with: `bundle.yaml` (manifest), `SKILL.md` (overview), `agents/` (per-role MDs), `examples/` (worked examples), `tests/` (validation)
How:
1. `mkdir -p ~/.hermes/profiles/<profile>/skills/<bundle-name>/{agents,examples,tests}`
2. Write `bundle.yaml` (schema below)
3. Write `SKILL.md` (the when-to-load-this)
4. Write 2-3 examples
5. Add 5+ unit tests for the deterministic parts
Verify: `/bundle <name>` slash command loads the bundle and the examples run
Dead signal: Bundle is loaded but no example is run (it's not pulling weight)

```yaml
# bundle.yaml schema
name: solopreneur-daily-intelligence
version: 1.0.0
description: 4-skill chain for the solopreneur morning
primary_skills: [cron-health-scan, daily-standup, b2b-research-pipeline, minigoalplan]
supporting_skills: [terminal, kanban, file]
required_toolsets: [terminal, file, web]
agent_roles:
  - name: Orchestrator
    prompt: Run the 4 skills in strict order; each output feeds the next.
input_schema: {date: ISO8601, profile: str}
output_schema: {health: str, standup: str, opportunity: str, minigoal: str}
```

### P26 — Solopreneur Daily Intelligence (4-skill chain)
Source: `CodingDeveloperRules/SkillBundles/solopreneur-daily-intelligence.md`
When: Want a single morning command that produces everything
What: 4 skills run in sequence: cron-health-scan → daily-standup → b2b-research-pipeline → minigoalplan
How:
1. Install the 4 skills
2. Bundle them in `~/.hermes/profiles/<profile>/skills/solopreneur-daily-intelligence/`
3. Slash command: `/morning` runs the bundle
Verify: One command produces: health status + standup + top opportunity + today's goal
Dead signal: One skill in the chain fails (refactor or replace)

### P27 — Aslamskillidentifier (find best skills for any task)
Source: `CodingDeveloperRules/SkillBundles/aslamskillidentifier-skill-bundle-2026-05-22.md`
When: User says "I need to do X" and you don't know which skills to load
What: A meta-skill that searches 5+ skill registries and returns the top 3 with installation commands
How:
1. Build the bundle: search Hermes Hub, Hermes Atlas, browse.sh, skills.sh, local skills
2. For each user request, run the search; return ranked results
3. Auto-install the top pick
Verify: 1 request → 1 top skill recommendation with install command
Dead signal: Top pick is consistently wrong (re-rank)

### P28 — Race condition spec (file ownership + merge strategy)
Source: `CodingDeveloperRules` (race-condition spec)
When: Multiple agents writing to the same workspace
What: A clear policy: every file has exactly one primary owner; merges are by section-add, never overwrite; locks for non-mergeable files
How:
1. Document the policy in `WorkflowXX/race-condition-policy.md`
2. For each file, list its primary owner
3. The orchestrator enforces: section-adds only, no overwrites
4. For JSON config files, use file locks (`flock`)
Verify: 0 race conditions in 30 multi-agent test runs
Dead signal: Conflicts reappearing (policy not enforced)

---

## Group 7: UltraPDFGen / PDF (P29–P30)

### P29 — UltraPDFGen pattern: 28 specialists + 50x critique
Source: `UltraPDFGenSkill/SKILL.md`
When: Need to produce a single high-quality output from a topic
What: 28 specialized agents (cover, TOC, exec summary, market analysis, financials, appendix, ...) + a critique agent that runs 50 rounds of review
How:
1. Define 28 sections (the chapters of a typical book/report)
2. For each section, assign a specialist agent (or 1-3 agents)
3. Orchestrator routes content to specialists
4. Critique agent reviews every section 50 times against a quality rubric
5. Output: 99/100 quality score
Verify: First book/report scores ≥ 95/100 on the rubric
Dead signal: Critique rounds don't improve score (rubric is wrong)

### P30 — Quality rubric pre-flight (99/100 target)
Source: `UltraPDFGenSkill/agents/critique_agent.md`
When: Shipping any high-stakes output
What: A pre-defined rubric (clarity, accuracy, completeness, voice, format, ...) with a threshold (e.g. 80/100) that the output must pass before shipping
How:
1. Define the rubric (6-10 criteria, 1-10 each)
2. Define the threshold (e.g. 80/100 = ship)
3. The output is auto-scored before any user-visible publish
4. If below threshold, loop back to revision
Verify: Every shipped output passes the rubric
Dead signal: Threshold bypassed (rubric is theater)

---

## Group 8: Ebook / Vibe PDF (P31–P34) — From `Ebook_EntireVibePipepline`

### P31 — Pydantic schema as contract (22 schemas)
Source: `Ebook_EntireVibePipepline/SCHEMA_ANALYSIS_REPORT.md`
When: Any data flowing between agents or stored persistently
What: Pydantic (or equivalent) schemas that define the shape and validation of every data object
How:
1. List every data object: Topic, Outline, Section, Critique, Ebook, Order, etc.
2. For each, write a Pydantic class with field types and constraints
3. Every agent that creates or consumes the object uses the schema
4. Auto-validate on every read/write
Verify: 0 schema mismatches in 30 days
Dead signal: Schemas diverge across agents (one canonical source)

### P32 — 5-stage publish pipeline (Topic→Outline→Content→Polish→Publish)
Source: `Ebook_EntireVibePipepline` (pipeline pattern)
When: Going from a raw idea to a published product
What: 5 stages, each with a clear input/output: Topic → Outline → Content → Polish → Publish
How:
1. Stage 1 — **Topic**: input is a string + audience + tier; output is a Topic object
2. Stage 2 — **Outline**: input is a Topic; output is an Outline (10-20 chapters)
3. Stage 3 — **Content**: input is an Outline; output is Sections (parallel)
4. Stage 4 — **Polish**: input is Sections; output is final Markdown
5. Stage 5 — **Publish**: input is final MD; output is PDF + landing page
Verify: End-to-end in < 4 hours for a 10-chapter book
Dead signal: A stage takes > 50% of total time (refactor or parallelize)

### P33 — CI/CD with quality gate before deploy
Source: `Ebook_EntireVibePipepline/CI_CD_WORKFLOW_REPORT.md`
When: Anything that gets deployed (web service, skill bundle, schema migration)
What: GitHub Actions that run lint + test + security scan on every PR; deploy on tag push; auto-rollback on health check failure
How:
1. `.github/workflows/ci.yml` runs on every PR
2. `.github/workflows/deploy.yml` runs on every `v*` tag push
3. Deploy step: build → push to registry → Coolify deploy → health check → smoke test
4. If health check fails, auto-rollback
Verify: Every deploy is green; rollback tested quarterly
Dead signal: Manual deploys (CI isn't the only path)

### P34 — API integration test matrix
Source: `Ebook_EntireVibePipepline/API_INTEGRATION_TEST_REPORT.md`
When: Any service exposes an API
What: A test matrix that covers every endpoint × every schema state × every auth role
How:
1. List all endpoints (CRUD for each schema + auth + webhook)
2. For each, write a test: valid input, invalid input, edge case, auth missing, auth wrong role
3. Auto-fail CI on any test regression
Verify: 100% endpoints have full test coverage
Dead signal: Tests skipped in CI (refactor to make them fast)

---

## Group 9: Company Orchestration (P35–P38) — From `company-orchestration`

### P35 — Company Orchestration = CEO directives + agent org chart
Source: `company-orchestration/README.md`
When: Running a multi-agent company
What: A CEO writes numbered directives; the COO agent translates each into N cron jobs and skill loads
How:
1. Define the agent org chart (CEO, COO, CRO, CMO, CTO, CFO, + specialists)
2. The CEO writes directives: `directive-001.md`, `directive-002.md`, ...
3. Each directive has: Objective, Background, Deliverables, Success Criteria, Owner, Deadline
4. The COO agent reads new directives daily and creates crons
5. Reports roll up to the CEO every Sunday
Verify: Every directive has a measurable result within its deadline
Dead signal: Directives without owners (rewrite)

### P36 — Method 0 pricing (sell agent, not output)
Source: `company-orchestration/README.md` (Method 0)
When: Pricing any agent-based service
What: Sell the **agent** (a working AI employee) not the **output** (a one-off deliverable). Subscription model.
How:
1. Define the agent's role (e.g. "AI Twitter researcher")
2. Price: $5K/month (1 agent), $10K/month (full team)
3. Sales motion: 30-min demo → 2-week pilot → monthly contract
4. Customer gets a working employee, not a deliverable
Verify: First paying customer on a monthly contract
Dead signal: Customers want one-off outputs (resist; sell the agent)

### P37 — Directive format (Objective+Background+Deliverables+…)
Source: `company-orchestration/directive-003.md`
When: Writing any directive
What: 7-field template: Objective, Background, Deliverables, Success Criteria, Owner, Deadline, Status
How:
1. Use the template for every directive
2. Number sequentially
3. Store in `WorkflowXX/directives/`
4. COO agent reads + translates
Verify: Every directive has all 7 fields
Dead signal: Directives missing fields (refuse to execute)

### P38 — Agent org chart with explicit reports-to
Source: `company-orchestration/hiring-plan.md`
When: Scaling a multi-agent team
What: An org chart with explicit reports-to relationships. Each agent has a `SCOPE.md` and a `REPORTS-TO`.
How:
1. List every agent role
2. For each, define: responsibilities, required capabilities, workspace, reports-to
3. Use SCOPE.md to limit what each agent can do (prevent drift)
4. Monthly audit: re-scope any agent that drifted
Verify: Every agent has a SCOPE.md, no two agents have overlapping writes
Dead signal: Agent drift (acts outside its SCOPE)

---

## Group 10: VentureHQ (P39–P41)

### P39 — 6-stage content production (Research→Brainstorm→Structure→Draft→Review→Publish)
Source: `VentureHQ/CONTENT_WORKFLOW.md`
When: Producing any non-trivial content
What: 6 stages with explicit owners: Research (IdeaScoutBot), Brainstorm (IdeaScoutBot), Structure (ProblemDeepdiveBot), Draft (MarketsizeBot), Review (MoatDesignBot+VenturescoreBot), Publish (VenturescoreBot)
How:
1. For each piece of content, run all 6 stages in order
2. Review gate: ≥ 80/100 to pass
3. If fail, loop back to Draft with the feedback
Verify: Every published content has all 6 stage outputs
Dead signal: Stages skipped (low-quality content)

### P40 — @VenturescoreBot in < 60s with score + decision
Source: `VentureHQ/QUICKSTART.md`
When: User wants to evaluate a venture idea quickly
What: One-line input → score (1-100) + decision (GO/CONDITIONAL/KILL) + 3 reasons in < 60s
How:
1. Slash command: `/qvalidate <idea>`
2. Apply 6-dimension rubric (Market, Competition, Build, Revenue, Distribution, Fit)
3. Output: total score, per-dimension breakdown, decision, 3 reasons
4. Latency target: < 60s end-to-end
Verify: First 5 ideas scored in < 60s each
Dead signal: Scoring consistently wrong (recalibrate)

### P41 — 20-agent parallel evaluation panel (delegate_task batch)
Source: `VentureHQ/CAPABILITIES.md` (20-agent model)
When: A venture idea scores ≥ 80 and needs deeper evaluation
What: Spin up 20 parallel evaluation agents, each from a different lens (market, tech, legal, ops, finance, customer, etc.)
How:
1. `delegate_task(tasks=[...20 tasks...])` (up to 3 parallel; queue the rest)
2. Each agent produces a sub-score + reasoning
3. Aggregate: weighted average, identify highest-risk dimensions
4. Output: 95% confidence go/no-go
Verify: First BUILD decision validated by the panel
Dead signal: Panel consistently disagrees (rubric is wrong)

---

## Group 11: Workflows Intelligence Layer (P42–P44) — From `MyWorkflowsIntelligenceLayer`

### P42 — YouTube channels registry as upstream intelligence
Source: `MyWorkflowsIntelligenceLayer/YoutubeChannelsVideosLearning/CHANNELS.md`
When: Want to stay current in any domain
What: A registry of high-signal YouTube channels (and other sources), with priority + category
How:
1. `channels.json` — machine-readable: id, handle, url, category, priority, last_fetched
2. `CHANNELS.md` — human-readable with rationale
3. Cron: daily 04:00 — fetch last 7 days of uploads
Verify: ≥ 10 priority=high channels tracked
Dead signal: Channels go stale (last_fetched > 30 days)

### P43 — Insight extraction: 1–3 per source, scored 1–10
Source: `MyWorkflowsIntelligenceLayer` (extraction pattern)
When: Have raw content (transcript, article) and want distilled insights
What: An agent that reads the content and outputs 1-3 actionable insights, each scored on novelty/actionability/signal-to-noise
How:
1. Input: transcript (5K-30K words) or article
2. Output: 1-3 insights, each with: title, summary, source-timestamp, why-it-matters, suggested-action, score
3. Threshold: only insights with score ≥ 7 are pushed downstream
Verify: 100% of high-score insights lead to an action within 7 days
Dead signal: Insights accumulate without being acted on (kill the source)

### P44 — Routing layer (insight → downstream workflow)
Source: `MyWorkflowsIntelligenceLayer` (routing)
When: Have insights from many sources, need to push them to the right consumer
What: For each insight, determine the downstream workflow (Tutor, Startup, Content, Coding) and drop a stub in that workflow's intake folder
How:
1. Tag each insight with: target_workflow, urgency, related_project
2. Drop a stub in `<target-workflow>/intake/<insight-slug>.md`
3. The target workflow's daily cron picks it up
Verify: Every high-score insight is consumed within 24h
Dead signal: Intake folder grows without consumption (refactor routing)

---

## Group 12: Pipeline Patterns (P45–P48)

### P45 — Task-assignment template (Objective+Background+Deliverables+Format)
Source: `content-pipeline/README.md` (task template)
When: Assigning any work to any agent
What: A standard 4-field template: Objective, Background, Deliverables, Format Spec
How:
1. Use the template for every task assignment
2. The agent returns work that matches the Format Spec
3. Reject work that doesn't match (forces clarity)
Verify: 100% of task assignments have all 4 fields
Dead signal: Format Spec missing (output is wrong shape)

### P46 — Fit × Intent = Composite lead score
Source: `research-feed/README.md` (lead scoring)
When: Scoring inbound leads
What: Composite Score = Fit Score × Intent Score. Target 80+ for immediate outreach.
How:
1. Fit Score (1-10): does the lead match the ICP? (size, industry, role)
2. Intent Score (1-10): is the lead actively looking for a solution?
3. Composite = Fit × Intent (1-100)
4. Outreach threshold: 80+
Verify: 50% of outreached leads respond
Dead signal: High Composite, low response (your scoring is wrong)

### P47 — 5-bot flagship content team (each has a clear role)
Source: `Content-Generation-Collab/2026-02-27.md`
When: Producing a flagship piece of content
What: 5 named bots collaborate: ContentForgeBot (drafting), NarrativestartegistBot (story), RepurposeBot (multi-format), TechRadarBot (tech accuracy), PerformanceAnalyticsBot (metrics)
How:
1. For each flagship, define the 5 bot roles
2. Orchestrator routes the work
3. Each bot produces its part; merge into one deliverable
Verify: First flagship shipped, all 5 bot outputs present
Dead signal: One bot's output is always empty (drop or replace)

### P48 — "Git log heartbeat" as health check
Source: `Daily-Working-Space` + general pattern
When: Want a passive health check on the whole system
What: `git log --since=24h` on every tracked repo — if a repo hasn't been committed to in 24h, alert
How:
1. Cron: every 6h — `git-heartbeat-check`
2. For each watch repo: get last commit time
3. If > 24h and repo is expected to be active, alert
Verify: All active repos show recent commits
Dead signal: False positives (alerted but no actual problem)

---

## Group 13: Cross-cutting (P49–P50)

### P49 — Single "Use the source" rule (knowledge-base-first)
Source: `Quantum-Learning-Collab` (the canonical learning repo for the Quantum Venture Lab profile)
When: User asks a question that has a canonical source
What: ALWAYS read the source first; cite it; never answer from model knowledge alone
How:
1. AGENTS.md mandates: "For any question with a known canonical source in the watch repos, read that source first. Cite it in the answer."
2. Build a `kb-lookup.sh` that maps topic → canonical file
3. The agent calls `kb-lookup.sh <topic>` before answering
Verify: 100% of canonical-source questions cite the source
Dead signal: Agent answers without citing (refuse the response)

### P50 — Single-profile, two-workflow architecture
Source: `HermesOracleVPS/quantum-venture-lab.md` (architecture spec in the HermesOracleVPS repo)
When: User has 2+ synergistic workflows (e.g. learn + build)
What: A single Hermes profile that hosts multiple workflows via slash commands, skills, and selective subagents. NOT multiple profiles (loses synergy).
How:
1. Create one profile: `hermes profile create <name>`
2. Add all workflows as slash commands in the AGENTS.md
3. Use prefixed memory keys: `Q-LEARN-*`, `Q-IDEA-*`, `Q-PRODUCT-*`
4. Push Obsidian as the shared knowledge base
5. Selective `delegate_task` only for parallel work
Verify: One profile can run both workflows without context loss
Dead signal: Drift between workflows (use stricter prefix discipline)

---

# APPENDIX A — How to use this file

1. **Install:** Copy this file to `~/.hermes/profiles/<your-profile>/references/50x-patterns.md` and add a line to `AGENTS.md`:
   ```
   ## Mandatory: 50x Patterns
   Before any non-trivial task, scan ~/.hermes/profiles/<your-profile>/references/50x-patterns.md
   for applicable patterns. Apply the highest-leverage ones first. Log the application in
   ~/.hermes/pattern-use.log (see INSTRUMENTATION.md).
   ```

2. **Measure:** See `INSTRUMENTATION.md`.

3. **Prune:** See `SELF-IMPROVE-LOOP.md`.

4. **Update:** When a new pattern emerges from the daily diff, add it here with the same structure.

---

# APPENDIX B — The 50-pattern flywheel

```
+---------------------------+
| 18 watch repos (sources)  |
+---------------------------+
            |
            v
+---------------------------+
| Daily diff (cron 05:00)   |
+---------------------------+
            |
            v
+---------------------------+
| 50x-PATTERNS-LIBRARY.md   |  <-- curated, versioned
+---------------------------+
            |
            v
+---------------------------+
| AGENTS.md enforcement     |  <-- auto-loaded every turn
+---------------------------+
            |
            v
+---------------------------+
| /50x /apply-pattern       |  <-- explicit invocation
+---------------------------+
            |
            v
+---------------------------+
| Pattern-use.log           |  <-- every application recorded
+---------------------------+
            |
            v
+---------------------------+
| Self-improve loop         |  <-- dead patterns pruned, new ones added
+---------------------------+
            |
            v
+---------------------------+
| 50x metrics dashboard     |  <-- 1x vs 50x proof
+---------------------------+
```

---

**End of 50x-PATTERNS-LIBRARY.md · v1.0 · 2026-06-03 · Aslam Shaik**
