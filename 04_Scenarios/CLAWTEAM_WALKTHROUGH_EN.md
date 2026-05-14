# L5 ClawTeam Hands-On Walkthrough

> 🌐 中文版本 / Chinese version: [CLAWTEAM_WALKTHROUGH.md](CLAWTEAM_WALKTHROUGH.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>
>
> This document walks through running a complete cross-functional Agent Team with **ClawTeam** (HKUDS, MIT License). Citation & license: see [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md). ClawTeam upstream: <https://github.com/HKUDS/ClawTeam>

---

## 0. Scenario for This Walkthrough

Uses the L5 course's **manufacturing quality-improvement Agent Team** (a localized version of ClawTeam's upstream AutoResearch example).

| Item | Content |
| --- | --- |
| Team mission | Reduce the monthly defect rate by 1% (from 3.2% → 2.2%) |
| Agent roles | RootCauseAgent, ParameterAgent, SPCAgent, ReportAgent, ReviewerAgent |
| Human Gate | Manufacturing Director (Coordinator / Human Gate) |
| Expected time | 2-3 hours sandbox exercise |

---

## 1. Environment Setup

### 1.1 Prerequisites

```bash
# Requirements
python --version      # 3.10+
tmux -V               # tmux installed
git --version         # git installed
claude --version      # or codex / gemini, any CLI agent
```

### 1.2 Install ClawTeam

```bash
pip install clawteam
# or from source:
# git clone https://github.com/HKUDS/ClawTeam.git && cd ClawTeam && pip install -e .
```

### 1.3 Configure Profile

```bash
clawteam profile wizard      # interactively configure the AI provider
clawteam profile test        # test the provider connection
clawteam profile doctor      # check for environment issues
```

> **Enterprise note:** for scenarios with sensitive process data, the profile should point to an on-prem LLM (Llama 70B) or an Azure OpenAI isolated tenant — do not use a public cloud API.

---

## 2. Create Team & Workspace

### 2.1 Create a git repo (the basis for Workspace isolation)

```bash
mkdir qa-improvement && cd qa-improvement
git init
echo "# QA Improvement Agent Team" > README.md
git add -A && git commit -m "init"
```

### 2.2 Spawn the Team

```bash
clawteam team spawn-team qa-team \
  -d "Reduce monthly defect rate by 1%: root cause → params → SPC → report" \
  -n leader
```

ClawTeam now creates the team state (JSON) under `~/.clawteam/qa-team/`.

### 2.3 Confirm Team status

```bash
clawteam team status qa-team
```

---

## 3. Design Tasks & Dependency Chain

Following the L5 course's IPOE table, break the Team mission into 4 dependency-aware tasks:

```bash
# T1: root-cause analysis (no dependency, runs first)
clawteam task create qa-team \
  --owner RootCauseAgent \
  --title "Identify top-3 defect modes from MES/SPC/QC data" \
  --id T1

# T2: process-parameter mapping (depends on T1)
clawteam task create qa-team \
  --owner ParameterAgent \
  --title "Map the 3 defect modes to process parameters" \
  --blocked-by T1 --id T2

# T3: SPC control recommendations (depends on T2)
clawteam task create qa-team \
  --owner SPCAgent \
  --title "Propose SPC control limits for the mapped parameters" \
  --blocked-by T2 --id T3

# T4: integration report (depends on T1 + T2 + T3)
clawteam task create qa-team \
  --owner ReportAgent \
  --title "Integrate findings into a QA improvement report" \
  --blocked-by T1,T2,T3 --id T4
```

### 3.1 Confirm the task board

```bash
clawteam task list qa-team
# Should show T1 ready, T2/T3/T4 blocked
```

---

## 4. Spawn Worker Agents

Each Agent runs in its own git worktree and tmux session, isolated from the others.

```bash
clawteam spawn --team qa-team --agent-name RootCauseAgent \
  --task "Work on T1. Query the QA data, identify top-3 defect modes."

clawteam spawn --team qa-team --agent-name ParameterAgent \
  --task "Work on T2 once T1 completes."

clawteam spawn --team qa-team --agent-name SPCAgent \
  --task "Work on T3 once T2 completes."

clawteam spawn --team qa-team --agent-name ReportAgent \
  --task "Work on T4 once T1/T2/T3 complete."
```

> Each spawn automatically injects the ClawTeam coordination prompt, teaching the Agent to use commands like `clawteam task` / `clawteam inbox`.

### 4.1 Confirm worktree isolation

```bash
git worktree list
# One branch per Agent, no overwrites
```

---

## 5. Monitor & Coordinate

### 5.1 Live board

```bash
clawteam board attach qa-team       # enter the live board
clawteam board live qa-team         # live terminal updates
clawteam board gource qa-team       # gource visualization (optional)
```

### 5.2 Leader sends messages to Agents

```bash
# Point-to-point: give a specific Agent extra context
clawteam inbox send qa-team RootCauseAgent \
  "Prioritize May's SPC anomalies; complaints concentrate on terminal crimping."

# Broadcast: notify the whole Team
clawteam inbox broadcast qa-team \
  "The Manufacturing Director wants a T4 first draft by Friday."
```

### 5.3 Wait for tasks to complete

```bash
clawteam task wait qa-team          # block until all tasks complete
```

---

## 6. Conflict Handling & Integration

### 6.1 Detect conflicts

```bash
clawteam context conflicts qa-team
# Check whether the Agents' worktrees have conflicting changes
```

### 6.2 Inject integration context

```bash
clawteam context inject qa-team ReportAgent \
  --from T1,T2,T3
# Inject the outputs of the first three tasks into ReportAgent's context
```

### 6.3 View the collaboration log

```bash
clawteam context log qa-team
```

---

## 7. Human Gate: Manufacturing Director Review

After ReportAgent completes T4, it **does not close out directly** — it enters the Human Gate:

1. The Manufacturing Director reads the integration report (ReportAgent's worktree branch).
2. Checks that each recommendation has evidence traceability (which defect mode → which parameter → which SPC rule).
3. Three decisions:
   - **Accept** → `clawteam task update qa-team T4 --status completed`
   - **Reject** → `clawteam inbox send qa-team ReportAgent "Rejection reason: ..."` + reopen the task
   - **Partial accept** → flag the parts that need human input, mark the rest completed

> The Human Gate is the core governance mechanism of L5 — the Agent Team collaborates autonomously, but **major decisions always have a human sign-off**.

---

## 8. Close-out & Snapshot

```bash
# Confirm all tasks complete
clawteam task list qa-team

# Snapshot the team state (preserve the exercise record)
clawteam team snapshot qa-team --label "qa-improvement-2026-05-run1"

# Export evidence (for L5 course Gate 5 acceptance)
clawteam board show qa-team > evidence/board-final.txt
clawteam task list qa-team > evidence/task-list-final.txt
```

---

## 9. Mapping to L5 Course Gate 5

| Gate 5 pass criterion | Corresponding evidence in this walkthrough |
| --- | --- |
| Complete ≥ 1 Agent Team scenario design | qa-team fully run through |
| Each Agent has role, Input, Output, constraints | RootCause/Parameter/SPC/Report/Reviewer role cards |
| Has an integration Agent or integration flow | ReportAgent + `context inject` |
| Has Reviewer / Human Gate | Manufacturing Director review process (§7) |
| Has ROI and governance design | defect-rate KPI + Audit log + snapshot |
| Successfully ran one full flow in a sandbox | §8 snapshot + evidence export |

---

## 10. Troubleshooting

| Problem | Resolution |
| --- | --- |
| Agent does nothing after `clawteam spawn` | check `clawteam profile doctor`; confirm the CLI agent is installed |
| Agent stuck on a blocked task | confirm the upstream task is `--status completed` |
| worktree conflicts | `clawteam context conflicts` → manual merge → `context inject` |
| tmux session not found | `tmux ls` to confirm; ClawTeam uses the tmux backend by default |
| Sensitive-data concern | switch the profile to an on-prem LLM; don't use a public cloud API |

---

## 11. From Walkthrough to Production

| Stage | Action |
| --- | --- |
| Sandbox exercise (this doc) | run through the flow, understand the 5-layer architecture, produce Gate 5 evidence |
| Department pilot | real data (de-identified), File transport, single machine |
| Cross-plant / cross-site | P2P (ZeroMQ) transport |
| Enterprise group | Redis transport (ClawTeam v0.4 roadmap) |
| Centralized monitoring | Web UI (ClawTeam v1.0 roadmap) |

---

## Citation

The ClawTeam commands, architecture, and design principles in this walkthrough are all cited from upstream HKUDS/ClawTeam (MIT License). This repo does **not** reproduce or fork the source code; learners install upstream via `pip install clawteam`. Full citation terms: [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md).
