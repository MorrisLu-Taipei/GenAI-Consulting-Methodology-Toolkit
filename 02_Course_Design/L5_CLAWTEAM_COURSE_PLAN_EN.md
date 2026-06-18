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

### Bloom-format primary LOs

> Written per the Bloom formula in [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) §4: **[Verb] + [Content] + [Context]** — assessable and measurable.

#### Four primary LOs for the CLP

By the end of this course, learners can:

1. **Build** a domain-specific Agent team (`clawteam team spawn-team` + dependency-aware `task create --blocked-by`), **completing** an end-to-end dry-run of a parallel-executable 5-Agent task queue. (Apply)

2. **Design** the 4 core artifacts of a cross-functional Agent Team: role cards (≥ 5 Agents), task allocation table, integration report template, Human Gate design; **producing** one complete set for an industry scenario (manufacturing / retail / healthcare). (Create)

3. **Use** `clawteam inbox` + `board` to monitor and coordinate team progress; **identify** the 3 failure modes (workspace context conflicts / integration deadlocks / Agent errors); **design** corresponding detection and recovery flows. (Analyze)

4. **Evaluate** the L5 fit of company candidate tasks, **quantifying** the Agent Team's ROI / governance / permissions / review cost; **judging** when to upgrade to L5 vs stay at L4; **producing** an L5 investment decision document. (Evaluate)

### Interactive Learning Design

> Per [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) §5.1 + §7 + §9.4.

**Engagement activity (within first 10 min):**

> **Each learner writes one sentence: "the task I'd assign to an Agent Team"**; class votes which is most worth team collaboration. 10 min, makes L5 concrete.

**Formative gates (quick self-checks at section boundaries):**

| Module | Formative check | Duration |
|---|---|---|
| Module 1 (L4→L5 boundary) | Classify own tasks L4 vs L5 | 10 min |
| Module 3 (Task design workshop) | 1-page 5-Agent role card draft | 30 min |
| Module 5 (Team & workspace) | Peer review of worktree isolation setup | 15 min |
| Module 6 (Integration & Gate) | Peer review of integration report | 20 min |

**Summative gate (end of course):** Maps to Gate 5 (§10) → 7 post-course assignments (§7) + 1 L5 investment decision document.

### Reference materials list

| Type | Location | Use | Status |
|---|---|---|---|
| Agent role card 1-page template | §1.x below (added) | Module 3 in-class exercise | ☑ Added |
| Task allocation table template | §1.x below (added) | Module 4 in-class exercise | ☑ Added |
| Integration report template | §1.x below (added) | Module 6 in-class exercise | ☑ Added |
| Human Gate design template | §1.x below (added) | Module 6 in-class exercise | ☑ Added |
| ClawTeam CLI quick-reference card | TBD | 1-page cheat sheet for spawn-team / task / inbox / board | ☐ TBD |

### Agent Role Card Template (high-priority enhancement)

```markdown
# Team: [Team Mission, 1 sentence]
# Date: [YYYY-MM-DD] | Version: [v0.1]

## Agents (≥ 5)
| # | Role | Mission | Primary Skill(s) | Input source |
|---|---|---|---|---|
| 1 | PM Agent | task decomposition + scheduling | L2.task_decompose, L3.schedule_workflow | Inbox |
| 2 | Research Agent | gather domain data | L2.web_research, L3.crawl_workflow | URLs + DB |
| 3 | Analysis Agent | structure & analyze | L2.data_analysis, L4.knowledge_query | Research output |
| 4 | Writer Agent | produce deliverable | L2.draft, L4.style_consistency_check | Analysis output |
| 5 | Reviewer Agent | QC + escalation | L2.quality_check, escalate_to_human | Writer output |

## I/O Summary
- Team input: [high-level goal from human]
- Team output: [deliverable, e.g., 5-page report]

## Reviewer & escalation
- Internal: Reviewer Agent (auto)
- Human Gate: [role / SLA / criteria]

## KPI (3-5 metrics)
- Cycle time: target ≤ X hours
- Output quality (peer score): ≥ Y/10
- Human revision rate: ≤ Z%

## Risk register (top 3)
1. [Risk] → [Mitigation]
2. ...

## Success criteria
- [ ] All Agents complete tasks without deadlock
- [ ] Output passes Reviewer Agent QC
- [ ] Human Gate approval
- [ ] KPI met
```

### Integration Report Template

```markdown
# [Team Name] Integration Report — [YYYY-MM-DD]

## Executive summary (1 paragraph)
[What the team delivered, headline KPI]

## Agent contributions
| Agent | Tasks completed | Output | Time spent |
|---|---|---|---|
| ... | ... | ... | ... |

## Conflicts detected & resolved
| # | Conflict | Resolution |
|---|---|---|
| 1 | ... | ... |

## KPI status
| Metric | Target | Actual | Status |
|---|---|---|---|
| ... | ... | ... | ✅ / ⚠️ / ❌ |

## Next steps
- ...

## Sign-off
- Team lead Agent: ___ Date: ___
- Human reviewer: ___ Date: ___
```

---

### ClawTeam CLI Quick-Reference Card

> One-page summary of common ClawTeam CLI commands; required for in-class and post-course hands-on.

#### Team lifecycle

| Command | Purpose | Example |
| --- | --- | --- |
| `clawteam team spawn-team` | Spawn a new Agent team | `clawteam team spawn-team --name marketing-team --agents 5 --domain marketing` |
| `clawteam team list` | List existing teams | `clawteam team list` |
| `clawteam team snapshot` | Freeze current team state | `clawteam team snapshot --name pre-gate-review` |
| `clawteam team restore` | Restore team to prior snapshot | `clawteam team restore --snapshot pre-gate-review` |
| `clawteam team destroy` | Dismantle team | `clawteam team destroy --name marketing-team --confirm` |

#### Task management

| Command | Purpose | Example |
| --- | --- | --- |
| `clawteam task create` | Create a task | `clawteam task create --title "Draft Q2 plan" --assign-to PMAgent` |
| `clawteam task create --blocked-by` | Create a dependency-aware task | `clawteam task create --title "Write copy" --blocked-by 12,13` |
| `clawteam task list` | List tasks | `clawteam task list --status pending` |
| `clawteam task update` | Update task status | `clawteam task update 14 --status in-progress` |
| `clawteam task close` | Close task | `clawteam task close 14 --output report-q2.md` |

#### Inter-Agent messaging

| Command | Purpose | Example |
| --- | --- | --- |
| `clawteam inbox send` | Send P2P message | `clawteam inbox send --from PMAgent --to ResearchAgent --msg "Need TAM by EOD"` |
| `clawteam inbox broadcast` | Broadcast to whole team | `clawteam inbox broadcast --from PMAgent --msg "Standup at 10am"` |
| `clawteam inbox read` | Read an Agent's inbox | `clawteam inbox read --agent ResearchAgent` |
| `clawteam inbox clear` | Clear inbox | `clawteam inbox clear --agent ResearchAgent --confirm` |

#### Monitoring

| Command | Purpose | Example |
| --- | --- | --- |
| `clawteam board show` | Show team board | `clawteam board show --team marketing-team` |
| `clawteam board live` | Live-updating board | `clawteam board live --team marketing-team` |
| `clawteam log tail` | Tail Agent log | `clawteam log tail --agent PMAgent --follow` |

#### Workspace & context

| Command | Purpose | Example |
| --- | --- | --- |
| `git worktree list` | List per-Agent isolated worktrees | `git worktree list` |
| `clawteam context conflicts` | Detect inter-Agent context conflicts | `clawteam context conflicts --team marketing-team` |
| `clawteam context inject` | Inject integrated context back | `clawteam context inject --from integration-report.md` |

#### Human Gate

| Command | Purpose | Example |
| --- | --- | --- |
| `clawteam gate request` | Trigger human Gate request | `clawteam gate request --task 14 --reviewer morris@tigerai.tw` |
| `clawteam gate approve` | Approve gate | `clawteam gate approve --task 14 --reviewer morris@tigerai.tw` |
| `clawteam gate reject` | Reject gate | `clawteam gate reject --task 14 --reviewer morris@tigerai.tw --reason "..."` |

#### Most-used in-class command combos

```bash
# 1. Spawn team + create dependent task chain
clawteam team spawn-team --name demo-team --agents 5 --domain consulting
clawteam task create --title "Research" --assign-to ResearchAgent
clawteam task create --title "Analyze" --blocked-by 1 --assign-to AnalysisAgent
clawteam task create --title "Draft" --blocked-by 2 --assign-to WriterAgent

# 2. Monitor progress
clawteam board live --team demo-team

# 3. Post-completion integration check
clawteam context conflicts --team demo-team
clawteam team snapshot --name demo-completed
```

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

## 4.5 The L5 Triad: Platform + Lens + Worked Case

> Added (v1.1): L5 is not only about the platform. Complete L5 teaching rests on three complementary pieces.

| Role | What | Teaches | File |
| --- | --- | --- | --- |
| **Platform** | ClawTeam (this plan's subject) | Mechanics: spawn / task / inbox / board / gate | This plan |
| **Lens** | Harness Engineering — six layers | Concept: why an Agent Team can reliably deliver | [`90_References/HARNESS_ENGINEERING_REFERENCE_EN.md`](../90_References/HARNESS_ENGINEERING_REFERENCE_EN.md) |
| **Worked case** | `ai-news-channel` | Demonstration: what the six layers + governance look like | [`ai-news-channel/TIGERAI_L5_CASE_NOTES.md`](ai-news-channel/TIGERAI_L5_CASE_NOTES.md) |

### The Six Harness Layers (L5 conceptual skeleton)

"Design the system first, then pick the models." The six layers are the axes for judging whether an Agent Team is mature:

| Harness layer | One-line | Open this file in `ai-news-channel` |
| --- | --- | --- |
| **Loop** | Fixed order, never skip | `CLAUDE.md` The Fixed Loop |
| **Tools** | Each agent gets only the scope it needs | `tools:` in `.claude/agents/*.md` |
| **Context** | Everyone reads the same constitution first | `CLAUDE.md` + `constitution/` |
| **Persistence** | Outputs & decisions durably stored | `knowledge-base/` |
| **Verification** | Machine + human check before shipping | `supervisor.md` + `verify_build.sh` |
| **Constraints** | Each role's CAN / CANNOT in writing | `constitution/ai-member-boundaries.md` |

> Suggested flow: **the six-layer lens gives the mental model → open `ai-news-channel` (the worked case) to see each layer concretely → go hands-on with ClawTeam (the platform) to run your own team.** ClawTeam's five-layer architecture (§4) is one concrete implementation of the six Harness layers on a CLI platform; HITL / Stage Gate 5 is the consulting-setting instantiation of the Verification + Constraints layers.
>
> Full mapping and source references: [`HARNESS_ENGINEERING_REFERENCE_EN.md`](../90_References/HARNESS_ENGINEERING_REFERENCE_EN.md).

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

## 6.99 Lecture Map (per [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) §5.3)

### 6.99.1 §6 Complete Lecture Map

> L5 is a ~8-hour hands-on workshop, split into AM (Concept) + PM (Hands-on). ~100 lectures × avg 4.8 min = 480 min / 8 hr.
>
> Lecture type codes: **TH** / **S** / **SL** / **VS** / **PR** / **EN** / **RC** (same as L1).

#### AM1 — Introduction + L4→L5 Boundary (90 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 0.1 | Welcome to L5 ClawTeam | TH | 4 | Instructor + why Multi-Agent Team is org-level leverage |
| 0.2 | What you'll learn | TH+SL | 3 | 4 primary LOs |
| 0.3 | **Engagement: write the task you'd assign** | EN+PR | 8 | Class votes most worth team |
| 1.1 | Single-Agent L4 limits | SL | 5 | Why one Agent isn't enough |
| 1.2 | Multi-Agent value | SL | 5 | Parallelism + specialization |
| 1.3 | L5 is not L4 plus | SL | 5 | Paradigm shift |
| 1.4 | When to upgrade to L5 | SL | 5 | 6 triggers |
| 1.5 | When L5 is overkill | TH | 5 | Failure cases |
| 1.6 | Section recap | RC | 5 | L4→L5 upgrade checklist |
| 1.7 | **Formative: classify own tasks L4 vs L5** | PR | 10 | Use §3.3 tasks |
| 1.8 | break | — | 10 | — |
| 1.9 | Buffer / wrap | RC | 5 | Transition to AM2 |

#### AM2 — ClawTeam Architecture (90 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 2.1 | 5-layer overview | SL+VS | 5 | Team / Workspace / Task / Inbox / Transport |
| 2.2 | Team Management | S | 5 | spawn-team concept |
| 2.3 | Workspace Isolation (git worktree) | S | 5 | Why worktree |
| 2.4 | Task Tracking + Dependencies | S | 5 | Kanban + blocked-by |
| 2.5 | Inter-Agent Messaging | S | 5 | inbox + broadcast |
| 2.6 | Transport: File / P2P / Redis | SL | 5 | 3 deployment stages |
| 2.7 | CLI quick-ref walkthrough | S | 8 | §1.x card section-by-section |
| 2.8 | Hedge Fund pattern intro | SL | 6 | Signal convergence example |
| 2.9 | Section recap | RC | 6 | 5 layers + 5 CLI commands |
| 2.10 | break | — | 10 | — |
| 2.11 | **Formative: sketch the 5 layers** | PR | 5 | Pen & paper |
| 2.12 | wrap | RC | 5 | Transition to PM1 |

#### PM1 — Task Design Workshop + Agent Role Card (120 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 3.1 | Role card template | SL | 5 | 7 fields |
| 3.2 | Example: manufacturing | S | 8 | Full 5-Agent walkthrough |
| 3.3 | Task allocation design | S | 5 | blocked-by chain |
| 3.4 | Integration report template | S | 5 | Exec summary + contributions + conflicts |
| 3.5 | Human Gate design | S | 5 | Trigger + reviewer + SLA |
| 3.6 | **Workshop Part 1: solo role card draft** | PR | 15 | Learner's own scenario |
| 3.7 | **Workshop Part 2: pair review + feedback** | PR | 30 | Peer review |
| 3.8 | break | — | 10 | — |
| 3.9 | **Workshop Part 3: revision + team feedback** | PR | 25 | Revise + multi-person review |
| 3.10 | **Workshop Part 4: gallery walk** | PR | 12 | Class walkthrough + vote |

#### PM2 — Hands-on: spawn / task / board / inbox / Gate (120 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 4.1 | Environment prep | S | 5 | tmux / git / CLI agent ready |
| 4.2 | `clawteam team spawn-team` hands-on | S | 8 | Run once |
| 4.3 | Learner self-spawn | PR | 10 | Use §3 role card |
| 4.4 | `clawteam task create --blocked-by` | S | 8 | Build dependency chain |
| 4.5 | Learner builds task chain | PR | 10 | — |
| 4.6 | `clawteam board live` monitor | S | 5 | Watch live |
| 4.7 | `clawteam inbox send / broadcast` messaging | S | 5 | Agent messaging |
| 4.8 | Hands-on inbox | PR | 10 | — |
| 4.9 | `git worktree list` + `context conflicts` detect | S | 8 | Isolation + conflict |
| 4.10 | break | — | 10 | — |
| 4.11 | `context inject` integrate | S | 6 | Inject back |
| 4.12 | Human Gate flow: request / approve / reject | S | 8 | Full gate flow |
| 4.13 | Hands-on Human Gate | PR | 10 | — |
| 4.14 | `team snapshot` + `restore` | S | 5 | Freeze & restore |
| 4.15 | wrap | RC | 12 | Full flow once |

#### Conclusion (30 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 5.1 | Demo Day: 5-min team demo × N | PR | 20 | Learner demos |
| 5.2 | ROI calculation example | SL | 5 | Is Agent Team worth it? |
| 5.3 | Gate 5 acceptance criteria recap | SL | 3 | 8 evidence items |
| 5.4 | Congratulations + closing | TH | 2 | End |

### 6.99.2 Lecture-type mix

| Type | Count | Time share |
| --- | --- | --- |
| TH | 7 | ~ 6% |
| S | 27 | ~ 32% |
| SL | 21 | ~ 22% |
| PR / EN | 15 | ~ 31% |
| RC | 8 | ~ 9% |

> L5 is a hands-on workshop; PR share ~31% is much higher than L1 (17%) — by design. L5 learners must **do** to master.

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
