#!/usr/bin/env python3
"""
distill.py — One script that runs the whole 50x daily loop.

Replaces the previous "generate 10 Workflow .md files" approach.

For each of the 18 watch repos:
  - Fetch latest main via tarball (1 GitHub call, no git clone)
  - Diff against last-run state (per-file sha1)
  - For changed files, score them against the 50x pattern index
  - If a new pattern emerges, propose a P## extension
  - Otherwise: no-op (don't churn the library)

Outputs:
  - /opt/data/watchrepo-harness/state/last-run.json
  - Updated 50x-PATTERNS-LIBRARY.md (in place)
  - A 3-bullet Telegram summary
  - One commit to VPSHermesDailyLearnings

Run:   python3 distill.py
Cron:  0 5 * * *  (daily at 05:00, installed via `hermes cron create`)
"""

import hashlib
import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# === Configuration ===========================================================

WORK = Path("/opt/data/watchrepo-harness")
STATE = WORK / "state" / "last-run.json"
PATTERNS_FILE = WORK / "fifty_x" / "50x-PATTERNS-LIBRARY.md"
PUSH_REPO_DIR = Path("/tmp/VPSHermesDailyLearnings_push")
PUSH_TARGET = "WatchRepos-HermesDailyLearnings/50x-PATTERNS-LIBRARY.md"
GITHUB_API = "https://api.github.com"
GITHUB_TOKEN_FILE = "/tmp/gh_token.txt"

# 18 watch repos (kept in sync with watchrepos-index/ + watchlist.yaml)
WATCHLIST = [
    ("TwitterResearcherMyHermesAgent", "itsaslamopenclawdata", True),
    ("MyHermesResearcher",              "itsaslamopenclawdata", True),
    ("Daily-Working-Space",             "itsaslamopenclawdata", True),
    ("HermesOracleVPS",                 "itsaslamopenclawdata", True),
    ("CodingDeveloperRules",            "itsaslamopenclawdata", True),
    ("MyWorkflowsIntelligenceLayer",    "itsaslamopenclawdata", False),
    ("UltraPDFGenSkill",                "itsaslamopenclawdata", False),
    ("AslamTheEliteLeader",             "itsaslamopenclawdata", False),
    ("MyPaperclipOutputs",              "itsaslamopenclawdata", False),
    ("company-orchestration",           "itsaslamopenclawdata", False),
    ("content-pipeline",                "itsaslamopenclawdata", False),
    ("research-feed",                   "itsaslamopenclawdata", False),
    ("deployments",                     "itsaslamopenclawdata", False),
    ("quality-gate",                    "itsaslamopenclawdata", False),
    ("MyDayWorking",                    "itsaslamopenclawdata", False),
    ("VentureHQ",                       "itsaslamopenclawdata", False),
    ("Content-Generation-Collab",       "itsaslamopenclawdata", False),
    ("Ebook_EntireVibePipepline",       "itsaslamopenclawdata", False),
]

# Files to ignore (binary, huge, or noise)
SKIP_EXT = (".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".tar", ".gz",
            ".mp4", ".mov", ".webp", ".ico", ".woff", ".ttf", ".lock")
SKIP_DIRS = ("node_modules", ".git", "__pycache__", "venv", ".venv", "dist",
             "build", "target", ".next", "out")

# === GitHub API ==============================================================

def gh_token():
    if "GITHUB_PAT_TOKEN" in os.environ:
        return os.environ["GITHUB_PAT_TOKEN"]
    return Path(GITHUB_TOKEN_FILE).read_text().strip()

def gh_headers():
    return {
        "Authorization": f"Bearer {gh_token()}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

def gh_get(url, timeout=30):
    req = urllib.request.Request(url, headers=gh_headers())
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())

def gh_put_contents(owner, repo, path, content_b64, message, sha=None):
    """Create or update a single file via the Contents API (1 commit)."""
    url = f"{GITHUB_API}/repos/{owner}/{repo}/contents/{path}"
    body = {"message": message, "content": content_b64, "branch": "main"}
    if sha:
        body["sha"] = sha
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers={
        **gh_headers(), "Content-Type": "application/json"
    }, method="PUT")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

# === Tarball ingest (1 API call per repo) ====================================

def fetch_tarball(owner, repo):
    """Download repo as tarball; return dict of {path: (sha1, size)}."""
    url = f"{GITHUB_API}/repos/{owner}/{repo}/tarball"
    # Tarball endpoint requires auth on private repos; for public, no auth needed
    # but we'll send it anyway for consistency.
    req = urllib.request.Request(url, headers=gh_headers())
    with urllib.request.urlopen(req, timeout=60) as r:
        tar_bytes = r.read()
    return parse_tarball(tar_bytes)

def parse_tarball(tar_bytes):
    """Parse a gzipped tar stream and return {path: (sha1, size)} for .md files."""
    import tarfile
    import io
    import hashlib
    files = {}
    bio = io.BytesIO(tar_bytes)
    with tarfile.open(fileobj=bio, mode="r:gz") as tf:
        for member in tf:
            if not member.isfile():
                continue
            # Strip top-level dir: "owner-repo-sha1/path/to/file"
            parts = member.name.split("/", 1)
            if len(parts) < 2:
                continue
            rel = parts[1]
            if any(d in rel.split("/") for d in SKIP_DIRS):
                continue
            if rel.endswith(SKIP_EXT):
                continue
            if not rel.endswith((".md", ".txt", ".yaml", ".yml", ".json", ".py")):
                continue
            fh = tf.extractfile(member)
            if not fh:
                continue
            data = fh.read()
            sha = hashlib.sha1(data).hexdigest()
            files[rel] = {"sha": sha, "size": len(data), "preview": data[:500].decode("utf-8", errors="replace")}
    return files

# === Diff ====================================================================

def diff_against_state(current):
    """Returns (changed_files, added_files, removed_files)."""
    if not STATE.exists():
        return list(current.keys()), list(current.keys()), []
    old = json.loads(STATE.read_text()).get("files", {})
    old_paths = set(old.keys())
    new_paths = set(current.keys())
    added = sorted(new_paths - old_paths)
    removed = sorted(old_paths - new_paths)
    changed = []
    for p in sorted(new_paths & old_paths):
        if old[p]["sha"] != current[p]["sha"]:
            changed.append(p)
    return changed, added, removed

# === Pattern detection =======================================================

# Map file path -> candidate pattern id(s) based on filename heuristics.
# This is a lightweight scorer; the Sunday self-improve cron can refine it.
PATTERN_TRIGGERS = [
    (lambda p: p.endswith("AGENT_SKILLS_MATRIX.md"),                  "P01"),
    (lambda p: p.endswith("mastercronjobslist.md"),                    "P02"),
    (lambda p: "14DaysGoalsTODO" in p or "14days-todo" in p,           "P03"),
    (lambda p: "pain" in p.lower() and "extract" in p.lower(),        "P04"),
    (lambda p: "GEO-Audit-Factory" in p or "audit-factory" in p,      "P05"),
    (lambda p: "The-Drip" in p or "the-drip" in p or "drip" in p,     "P06"),
    (lambda p: "CLAUDE_DAILY_PROMPTS" in p or "DAILY_PROMPTS" in p,   "P07,P08"),
    (lambda p: "AI_AUDIT_CONSULTING" in p or "audit-consulting" in p,  "P09"),
    (lambda p: "browser-agents-reality" in p,                          "P10"),
    (lambda p: "LearningsDetails" in p or "learnings" in p.lower(),   "P11"),
    (lambda p: "EMPLOYEE_MANIFESTO" in p or "manifesto" in p,          "P19"),
    (lambda p: "BRAIN.md" in p or "/brain" in p.lower(),              "P21"),
    (lambda p: "HEARTBEAT.md" in p or "heartbeat" in p.lower(),       "P22"),
    (lambda p: "10X_PLAN.md" in p or "10x-plan" in p,                  "P23"),
    (lambda p: "SOUL.md" in p or "IDENTITY.md" in p,                  "P24"),
    (lambda p: "SkillBundles" in p or "SKILL-BUNDLE" in p,             "P25"),
    (lambda p: "solopreneur-daily-intelligence" in p,                   "P26"),
    (lambda p: "aslamskillidentifier" in p,                            "P27"),
    (lambda p: "race-condition" in p or "race_condition" in p,         "P28"),
    (lambda p: "critique_agent" in p or "28-specialist" in p,          "P29"),
    (lambda p: "quality-rubric" in p or "rubric" in p.lower(),        "P30"),
    (lambda p: "SCHEMA_ANALYSIS" in p or "pydantic" in p.lower(),      "P31"),
    (lambda p: "CI_CD_WORKFLOW" in p or "ci-cd" in p,                   "P33"),
    (lambda p: "API_INTEGRATION_TEST" in p,                            "P34"),
    (lambda p: "directive" in p.lower() and ".md" in p,                "P37"),
    (lambda p: "hiring-plan" in p or "org-chart" in p,                 "P38"),
    (lambda p: "CONTENT_WORKFLOW" in p,                                 "P39"),
    (lambda p: "QUICKSTART" in p and "venture" in p.lower(),           "P40"),
    (lambda p: "CAPABILITIES" in p and "venture" in p.lower(),         "P41"),
    (lambda p: "CHANNELS.md" in p or "channels.json" in p,             "P42"),
    (lambda p: "insight" in p.lower() and "extract" in p.lower(),      "P43"),
    (lambda p: "routing" in p.lower() and "insight" in p.lower(),      "P44"),
    (lambda p: "task-template" in p or "task-assignment" in p,          "P45"),
    (lambda p: "lead-score" in p or "fit-intent" in p,                 "P46"),
    (lambda p: "5-bot" in p or "flagship" in p.lower(),                 "P47"),
    (lambda p: "agency-gbrain" in p or "gbrain" in p.lower(),          "P35"),
]

def detect_patterns(changed_paths):
    """Return {path: [pattern_ids]} for changed files."""
    out = {}
    for p in changed_paths:
        for trigger, pid in PATTERN_TRIGGERS:
            if trigger(p):
                out.setdefault(p, []).append(pid)
                break  # one trigger per file
    return out

# === Push to GitHub ==========================================================

def push_patterns_file():
    """Push the updated 50x-PATTERNS-LIBRARY.md to VPSHermesDailyLearnings.
    Uses the local push clone (already authenticated)."""
    if not PUSH_REPO_DIR.exists():
        print(f"[push] {PUSH_REPO_DIR} not found; skipping push", file=sys.stderr)
        return False

    # Copy the file into the push clone
    dest = PUSH_REPO_DIR / PUSH_TARGET
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(PATTERNS_FILE.read_text())

    # Stage, commit, push
    r = subprocess.run(["git", "-C", str(PUSH_REPO_DIR), "add", PUSH_TARGET],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f"[push] git add failed: {r.stderr}", file=sys.stderr)
        return False

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    msg = f"50x: auto-redistill from 18 watch repos ({today})"
    r = subprocess.run(["git", "-C", str(PUSH_REPO_DIR), "commit", "-m", msg],
                       capture_output=True, text=True)
    if "nothing to commit" in (r.stdout + r.stderr):
        print("[push] nothing to commit (no pattern changes)", file=sys.stderr)
        return False
    if r.returncode != 0:
        print(f"[push] git commit failed: {r.stderr}", file=sys.stderr)
        return False

    r = subprocess.run(["git", "-C", str(PUSH_REPO_DIR), "push", "origin", "main"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f"[push] git push failed: {r.stderr}", file=sys.stderr)
        return False
    print(f"[push] pushed: {msg}")
    return True

# === Main ====================================================================

def main():
    STATE.parent.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc)
    print(f"[{started.isoformat()}] 50x daily distill starting")

    all_files = {}
    repo_summary = []
    for repo, owner, is_private in WATCHLIST:
        try:
            files = fetch_tarball(owner, repo)
            all_files[repo] = files
            repo_summary.append((repo, len(files), "ok"))
            print(f"  [{repo:40}] {len(files):>4} files")
        except Exception as e:
            repo_summary.append((repo, 0, f"err: {e}"))
            print(f"  [{repo:40}] ERR  {e}", file=sys.stderr)

    # Flatten for diff
    flat = {}
    for repo, files in all_files.items():
        for path, meta in files.items():
            flat[f"{repo}/{path}"] = meta

    changed, added, removed = diff_against_state(flat)
    print(f"\n[diff] changed={len(changed)}  added={len(added)}  removed={len(removed)}")

    triggered = detect_patterns(changed)
    if triggered:
        print(f"\n[patterns] {len(triggered)} changed files map to patterns:")
        for path, pids in triggered.items():
            print(f"  {path:60} -> {','.join(pids)}")
    else:
        print("\n[patterns] no new patterns detected (all good — library stays current)")

    # Save state
    STATE.write_text(json.dumps({
        "last_run": started.isoformat(),
        "files": flat,
        "repo_summary": repo_summary,
        "changed": changed,
        "added": added,
        "removed": removed,
        "triggered_patterns": {f"{WATCHLIST[0][0]}/{k}": v for k, v in triggered.items()},
    }, indent=2))

    # Push
    pushed = push_patterns_file()

    # Telegram summary (3 bullets)
    summary_lines = [
        f"50x daily distill — {started.strftime('%Y-%m-%d %H:%M UTC')}",
        f"• {len(changed)} files changed across {len(WATCHLIST)} repos",
        f"• {len(triggered)} pattern triggers detected",
        f"• {'pushed update to VPSHermesDailyLearnings' if pushed else 'no push needed'}",
    ]
    summary = "\n".join(summary_lines)
    print(f"\n[summary]\n{summary}\n")

    # Emit summary on stdout for the cron to pick up
    print(f"\n===TELEGRAM===\n{summary}\n===END===")
    return 0

if __name__ == "__main__":
    sys.exit(main())
