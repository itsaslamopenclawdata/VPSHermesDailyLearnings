# Workflow 07 — Workflows Intelligence Layer

> **Source repos:** `MyWorkflowsIntelligenceLayer`
> **Run mode:** FIRST-PASS FULL INGESTION
> **Last updated:** 2026-06-09
> **WatchRepos iteration:** 1

---

## 1. Purpose

The **upstream intelligence feed** for all other workflows: continuously ingest high-signal content (YouTube channels, blogs, podcasts, arxiv, Twitter lists), extract the 1–3 actionable insights per source, and pipe them into the relevant downstream workflow (Tutor, Startup Studio, Content, etc.).

## 2. Source repos and what they teach

### `MyWorkflowsIntelligenceLayer`
- **Files:** 120 · **.md count:** 68 · **Last commit:** `5ddcd525` · 2026-06-09 · "[youtube] add Google Cloud Tech channel + Antigravity 2.0 deep dive note"
- **Theme:** YouTube channels registry, tracked content, intelligence layer feeds
- **Key files:** `YoutubeChannelsVideosLearning/CHANNELS.md`, `YoutubeChannelsVideosLearning/INDEX.md`, `channels.json`

> **Excerpt from `YoutubeChannelsVideosLearning/CHANNELS.md`:**
> # Tracked YouTube Channels

Human-readable list of every YouTube channel tracked in this folder. The machine-readable registry is `channels.json`.

## Hyperautomation Labs

- **Channel ID:** UCiax-xbEI0P6Y8C8VwZGMgQ
- **Handle:** @hyperautomationlabs1045
- **URL:** https://www.youtube.com/@hyperautomationlabs1045
- **Folder:** `channels/hyperautomation-labs/`
- **Category:** ai-automation
- **Why 

> **Excerpt from `YoutubeChannelsVideosLearning/INDEX.md`:**
> # YouTube Channels — Video Index

Auto-regenerated. One line per video, newest first. Sorted by published date, descending.

**Last updated:** 2026-06-09 05:50 UTC
**Total videos:** 51 across 12 channels

| Date | Channel | Title | Duration | Video ID | Note |
|------|---------|-------|----------|----------|------|
| 2026-06-09 | AI Engineer | 2026 AI Engineer Vibe Reel | 1:07 | [gUMwt4-5kn0](http

## 3. Detailed TODO ACTION STEPS — Build the Harness

### 3.1 Define the channel taxonomy
- [ ] **AI/Automation** — Hyperautomation Labs, AI agents, n8n/Make/Zapier
- [ ] **SaaS / Startups** — Greg Isenberg, My First Million, Y Combinator
- [ ] **Quantum** — IBM Quantum, AWS Quantum, PennyLane, Qiskit
- [ ] **Productivity** — Ali Abdaal, Thomas Frank, Cal Newport
- [ ] **Investing / Business** — Patrick Boyle, Naval, Stripe
- [ ] **Coding** — Theo, Fireship, CodeAesthetic

### 3.2 Author the channel registry
- [ ] `channels.json` — machine-readable list: id, handle, url, category, priority, last_fetched
- [ ] `CHANNELS.md` — human-readable version with rationale per channel
- [ ] `INDEX.md` — index by category, by priority, by freshness

### 3.3 Build the fetch pipeline
- [ ] Use the YouTube Data API (or yt-dlp for transcript-only) to fetch the last 7 days of uploads
- [ ] Fetch transcripts (auto-generated or manual)
- [ ] Store raw transcripts in `Workflow07/transcripts/<channel>/<video-id>.txt`
- [ ] Cron: daily 04:00 — fetch all priority=high channels

### 3.4 Build the extraction agent
- [ ] Input: a transcript (5,000–30,000 words)
- [ ] Output: 1–3 actionable insights, each with: title, summary, source-timestamp, why-it-matters, suggested-action
- [ ] Use a strong model (Claude Sonnet) for extraction
- [ ] Score each insight (1–10) on: novelty, actionability, signal-to-noise
- [ ] Only insights with score ≥ 7 are pushed downstream

### 3.5 Build the routing layer
- [ ] For each insight, determine the downstream workflow: Tutor (→ workflow 1), Startup Studio (→ workflow 1), Content (→ workflow 2), Coding (→ workflow 4), ...
- [ ] Drop a stub entry in the downstream workflow's intake folder
- [ ] The downstream workflow's daily cron picks it up

### 3.6 Build the daily digest
- [ ] Top 5 insights of the day, by score
- [ ] Grouped by category
- [ ] One-paragraph action recommendation
- [ ] Delivered to Telegram at 07:30

### 3.7 Daily outputs committed to GitHub
- [ ] `Workflow07/insights/YYYY-MM-DD.md` — all extracted insights for the day
- [ ] `Workflow07/digest/YYYY-MM-DD.md` — the daily digest
- [ ] `Workflow07/transcripts/...` — raw transcripts (git-ignored if too large; otherwise monthly archive)

## 4. Verification

- [ ] At least 10 priority=high channels tracked
- [ ] First daily digest generated and posted
- [ ] At least 1 insight successfully routed to a downstream workflow

## 5. Success criteria (per month)

- [ ] 30 daily digests generated
- [ ] 100+ high-score insights extracted
- [ ] 10+ insights translated into actions (1 insight → 1 task completed)
- [ ] 1 new channel added per month
