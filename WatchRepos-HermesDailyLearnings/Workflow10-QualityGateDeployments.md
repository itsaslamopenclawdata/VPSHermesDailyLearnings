# Workflow 10 — Quality Gate & Deployments

> **Source repos:** `quality-gate`, `deployments` (both currently empty)
> **Run mode:** FIRST-PASS FULL INGESTION
> **Last updated:** 2026-06-09
> **WatchRepos iteration:** 1

---

## 1. Purpose

The **last mile** workflow: define what "ready to ship" means, run the verification gates, deploy via Coolify, monitor for regressions. Both source repos are currently empty — this workflow designs the canonical structure and seeding plan.

## 2. Source repos and what they teach

### `quality-gate`
- **Files:** 0 (empty repo)
- **Status:** Not yet created. Designed in this workflow.

### `deployments`
- **Files:** 0 (empty repo)
- **Status:** Not yet created. Designed in this workflow.

## 3. Detailed TODO ACTION STEPS — Build the Harness

### 3.1 Define the Quality Gate rubric
- [ ] **Code quality**: lint passes, type-check passes, no secrets in code, no console.logs in prod
- [ ] **Test coverage**: ≥ 80% on changed lines, all new functions have at least 1 test
- [ ] **Documentation**: README updated, every new function has a docstring, CHANGELOG entry
- [ ] **Security**: no critical CVEs in deps, no high-severity `npm audit` / `pip audit` issues
- [ ] **Performance**: p95 latency ≤ 200ms, no N+1 queries, cold start ≤ 2s
- [ ] **Observability**: every endpoint emits metrics, errors are traceable

### 3.2 Build the pre-commit hook
- [ ] Install `pre-commit` framework
- [ ] Hooks: `ruff check`, `ruff format`, `mypy`, `gitleaks`, `pytest --collect-only`
- [ ] Config: `.pre-commit-config.yaml` in every repo

### 3.3 Build the CI pipeline
- [ ] GitHub Actions: on every PR
  - [ ] Lint + format check
  - [ ] Type check
  - [ ] Unit tests (≥ 80% coverage gate)
  - [ ] Integration tests
  - [ ] Security scan (`pip-audit`, `npm audit`, `gitleaks`)
  - [ ] Build the Docker image
  - [ ] Push to a staging environment
  - [ ] Run smoke tests on staging
- [ ] Branch protection: PR cannot merge until all checks pass

### 3.4 Build the Deployments workflow
- [ ] Source: a release tag (e.g. `v1.0.0`)
- [ ] Trigger: tag push to main
- [ ] Steps:
  - [ ] Build production Docker image
  - [ ] Push to GitHub Container Registry
  - [ ] Trigger Coolify deploy via API
  - [ ] Wait for health check
  - [ ] Run smoke tests on production
  - [ ] Send deployment notification to Telegram
  - [ ] Auto-create release notes
- [ ] Rollback: if health check fails within 5 min, auto-rollback to last good tag

### 3.5 Build the monitoring layer
- [ ] Prometheus + Grafana for metrics
- [ ] Sentry for error tracking
- [ ] Better Uptime for synthetic checks
- [ ] Alert rules: p95 > 1s, error rate > 1%, CPU > 80%

### 3.6 Build the post-deploy audit
- [ ] Cron: 1h after every deploy — `post-deploy-audit` — verifies all KPIs are within bounds
- [ ] Cron: 24h after every deploy — `24h-stability-check` — verifies no late-breaking regressions
- [ ] Auto-create a postmortem template if any check fails

### 3.7 Seed the (currently empty) source repos
- [ ] In `quality-gate/`: add `RUBRIC.md`, `pre-commit-config.yaml`, `.github/workflows/ci.yml`, `README.md`
- [ ] In `deployments/`: add `RELEASE.md`, `.github/workflows/deploy.yml`, `coolify-deploy.sh`, `rollback.sh`, `README.md`

### 3.8 Daily outputs committed to GitHub
- [ ] `Workflow10/deployments/YYYY-MM-DD.md` — every deploy today (service, version, status, smoke-test result)
- [ ] `Workflow10/quality-gate-failures/YYYY-MM-DD.md` — any gate failures
- [ ] `Workflow10/incidents/YYYY-MM-DD-<slug>.md` — postmortems

## 4. Verification

- [ ] Both empty repos seeded with the canonical structure
- [ ] A test PR triggers the full CI pipeline and all checks pass
- [ ] A test deploy goes through end-to-end (staging → production → smoke test)
- [ ] Rollback works (test by deploying a bad version)

## 5. Success criteria (per quarter)

- [ ] 30 successful deploys
- [ ] 0 production incidents (or all resolved within 24h with postmortems)
- [ ] p95 latency on all services ≤ 200ms
- [ ] Test coverage across all repos ≥ 80%
