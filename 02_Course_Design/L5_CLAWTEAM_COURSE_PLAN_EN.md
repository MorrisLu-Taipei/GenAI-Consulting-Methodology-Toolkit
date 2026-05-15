# L5 ClawTeam Course Plan

> 🌐 中文版本 / Chinese version: [L5_CLAWTEAM_COURSE_PLAN.md](L5_CLAWTEAM_COURSE_PLAN.md)

Version: v1.0
Author: Morris Lu (盧業興) · Tiger AI 虎智科技

---

## 0. Citation Notice

> This course uses **ClawTeam** (open-sourced by HKUDS under the MIT License) as the primary implementation platform for L5 Multi-Agent Organization.
> Upstream repo: <https://github.com/HKUDS/ClawTeam>
> Full citation and license details: [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md)

---

## 1. Course Objectives

Evolve the enterprise from **single Agent (L4 Hermes)** to **multi-Agent self-organizing team (L5 ClawTeam)**: a human issues one high-level goal and the Agent Team autonomously decomposes, delegates, executes in parallel, integrates, and submits to human Gate review.

### By the end of this course, learners can

1. Spawn a domain-specific Agent team using `clawteam team spawn-team`.
2. Author a dependency-aware (`--blocked-by`) task queue using `clawteam task create`.
3. Pass messages between Agents using `clawteam inbox send / broadcast`.
4. Monitor team progress with `clawteam board show / live`.
5. Design **cross-functional Agent Team role cards**, **task allocation tables**, **integration report templates**, and **Human Gate designs**.
6. Quantify the Agent Team's ROI, governance, permissions, and review mechanisms.

---

## 2. Audience

- Executives (CEO / COO / CTO)
- Cross-functional managers
- PM / Project managers
- IT / AI Center / Platform team
- L4-graduated seed team

## 3. Prerequisites

| Item | Description |
| --- | --- |
| **L4 graduated** | At least one Hermes Agent has passed Gates 4A-4E |
| **Environment** | Python 3.10+, `tmux`, `git`, any CLI agent (Claude Code / Codex / Gemini) |
| **Cross-functional task** | New-product launch / quality improvement / customer engagement / patient service / annual operations planning |
| **Data sources** | At least two of CRM, ERP, Sheets, Notion, API |
| **Human Gate** | Executive or project owner designated as Reviewer |

---

## 4. ClawTeam Architecture Primer

> See [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md) §2 for the full architecture overview.

| Layer | Maps to L5 Topic |
| --- | --- |
| **Team Management** | §6.2 Agent Team design |
| **Workspace Isolation (git worktree)** | §6.3 Workspace isolation & conflict management |
| **Task Tracking (Kanban + dependencies)** | §6.4 Task allocation & dependencies |
| **Inter-Agent Messaging (inbox + broadcast)** | §6.5 Inter-Agent communication design |
| **Transport (File / P2P / Redis roadmap)** | §6.7 Deployment modes: single-machine vs cross-machine |

### Three reference scenarios → localized mapping

| Upstream ClawTeam scenario | Localized L5 scenario |
| --- | --- |
| AutoResearch (8 Agents, H100) — ML autonomous hyperparameter experiments | **Manufacturing: Quality Improvement Agent Team** — parallel exploration of defect-rate root causes, process parameters, and SPC rules |
| Software Engineering (5 Agents) — Architect / Backend / Frontend / QA | **Retail: New-Product Launch Agent Team** — product design, pricing, copy, channels, launch QA |
| Hedge Fund (7 Agents) — Portfolio Manager + 5 Analysts + Risk Manager | **Hospital: Patient Service Improvement Agent Team** — medical admin, records, customer service, QA, integration |

---

## 5. Course Modules

Total duration: **8-12 hours (1.5 days)**

| # | Module | Time | Content | Method |
| ---: | --- | ---: | --- | --- |
| 1 | **The L4 → L5 boundary** | 30 min | Single-Agent vs Agent-Team; when to upgrade | Lecture |
| 2 | **Multi-Agent concepts** | 45 min | Solo 🤖 → Swarm 🦞🤖🤖🤖; ClawTeam's three reference cases | Lecture |
| 3 | **ClawTeam architecture primer** | 45 min | The five layers: Team / Workspace / Task / Inbox / Transport | Lecture + slides |
| 4 | **Install & profile** | 45 min | `pip install clawteam`, `clawteam profile wizard / test / doctor` | Hands-on |
| 5 | **Team & workspace** | 60 min | `team spawn-team`, git worktree auto-setup, `team snapshot/restore` | Hands-on |
| 6 | **Task design (role card + IPOE)** | 90 min | Agent role cards, Input/Process/Output/Evidence, dependency chains | Workshop |
| 7 | **Task CLI hands-on** | 75 min | `task create --blocked-by`, `task update`, `task list`, `task wait` — author dependency-aware tasks | Hands-on |
| 8 | **Inbox & broadcast** | 60 min | Point-to-point vs broadcast; signal convergence patterns (reference: Hedge Fund Risk Manager) | Hands-on |
| 9 | **Board monitoring & gource visualization** | 45 min | `board show / live / attach / gource / serve` — dashboards and visualization | Hands-on |
| 10 | **Integration Agent & Reviewer** | 60 min | Conflict detection (`context conflicts`), integration reports, Reviewer role | Workshop |
| 11 | **Governance, permissions, Human Gate** | 60 min | Stage Gate 5, Reviewer flow, permission model (v0.6 roadmap) | Lecture |
| 12 | **Team simulation** | 150 min | Complete one Agent Team case (manufacturing / hospital / retail) | Exercise |
| 13 | **ROI, recap, advanced (v0.4-v1.0)** | 60 min | KPI design, Redis transport, Web UI roadmap | Lecture |

---

## 6. Key Workshops

### 6.2 Agent Team Design Workshop

Each team must complete an Agent role card:

| Field | Example: Manufacturing Quality Improvement |
| --- | --- |
| **Team mission** | Reduce monthly defect rate by 1% |
| **Agent roles** | RootCauseAgent, ParameterAgent, SPCAgent, ReportAgent, ReviewerAgent |
| **Input** | MES / SPC / QC reports, production logs, customer complaints |
| **Process** | Decompose → parallel exploration → signal convergence → integration report |
| **Output** | Root-cause report + process-parameter recommendations + SPC rule updates |
| **Reviewer** | Manufacturing director + QA manager |
| **Human Gate** | Report → director sign-off → pilot run → mass production |
| **KPI** | Defect rate, repeatability, recovery loss, complaint reduction |

### 6.3 Workspace Isolation & Conflict Management

ClawTeam uses **git worktree** to give every Agent its own branch — no overwrites. Learners must master:

- `git worktree list` — inspect each Agent's branch
- `clawteam context conflicts` — detect conflicts
- `clawteam context inject` — inject integrated context into Agents
- Merge strategy: who can merge, and in what order?

### 6.4 Task Allocation & Dependencies

Learners write a real task chain:

```bash
# Manufacturing QA team example
clawteam task create my-team --owner RootCauseAgent --title "Identify top-3 defect modes" --id T1
clawteam task create my-team --owner ParameterAgent --title "Map defect modes to process params" --blocked-by T1 --id T2
clawteam task create my-team --owner SPCAgent --title "Propose SPC control limits" --blocked-by T2 --id T3
clawteam task create my-team --owner ReportAgent --title "Integrate findings" --blocked-by T1,T2,T3 --id T4
clawteam task wait my-team
```

### 6.5 Inter-Agent Communication

Two patterns:

| Pattern | Command | When to use |
| --- | --- | --- |
| **Point-to-point** | `clawteam inbox send <team> <agent> "message"` | Direct data handoff |
| **Broadcast** | `clawteam inbox broadcast <team> "message"` | Team-wide status sync, Gate notifications |
| **Signal convergence** | Multiple Analyst Agents → Risk Manager Agent (Hedge Fund pattern) | Multi-source signals → consolidated decision |

### 6.7 Single-Machine vs Cross-Machine Deployment

| Scenario | Transport | Enterprise stage |
| --- | --- | --- |
| **PoC / small department** | File-based (default) | L5 starter |
| **Cross-plant / cross-site** | P2P (ZeroMQ) | Medium enterprise |
| **HQ multi-region** | Redis (v0.4 roadmap) | Enterprise group |
| **Full Web UI** | v1.0 roadmap | Centralized AI Team monitoring |

---

## 7. Post-Course Assignments

1. Complete one **Agent Team role card** (≥ 5 Agent roles).
2. Complete one **task allocation table with dependency chains**.
3. Complete one **IPOE table**.
4. Complete one **integration report template**.
5. Design one **Reviewer / Human Gate flow**.
6. Submit one **ROI tracking table**.
7. Run one full `clawteam` flow in a sandbox; submit a `board show` screenshot plus `task list` output.

---

## 8. Completion Criteria

| Criterion | Verification |
| --- | --- |
| Clear Agent roles | Role card |
| Tasks are dispatchable | `task list` output + dependency chain |
| Clear Input/Output per Agent | IPOE table |
| Has integration & review mechanism | Integration report + Reviewer design |
| Has ROI metrics | KPI table |
| Actually ran ClawTeam | Screenshots of board / task / inbox operations |

---

## 9. L5 Deliverables

- ClawTeam role card
- Multi-Agent task allocation table (with dependency chains)
- Agent Team IPOE table
- Integration report template
- Reviewer / Human Gate design
- ROI tracking table
- Sandbox dry-run records: `board show` + `task list` + `inbox` screenshots
- ClawTeam profile + team config (`~/.clawteam/`) backup

---

## 10. Stage Gate 5: L5 Completion Criteria

Pass criteria:

- Complete ≥ 1 Agent Team scenario design (choose one of manufacturing / hospital / retail).
- Every Agent has role, Input, Output, and constraints.
- Has an integration Agent or integration flow.
- Has Reviewer / Human Gate.
- Has ROI and governance design.
- Successfully ran one full `clawteam` flow in a sandbox.

---

## 11. Citation & License

This course localizes citations of ClawTeam's architecture, CLI, and design principles. The upstream **source code is not reproduced or forked**. If learners or enterprises redistribute ClawTeam source in derivative works, they must comply with the **MIT License** and preserve the original copyright notice. Full citation terms:

📄 [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md)

**Upstream project**: HKUDS, *ClawTeam*, MIT License, <https://github.com/HKUDS/ClawTeam>
