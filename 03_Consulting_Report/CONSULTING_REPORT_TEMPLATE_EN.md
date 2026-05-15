# AI Transformation Diagnostic Report Template

> 🌐 中文版本 / Chinese version: [CONSULTING_REPORT_TEMPLATE.md](CONSULTING_REPORT_TEMPLATE.md)

Last updated: 2026-05-15 (Eight stages aligned to canonical methodology)

> This template aligns with the **Enterprise Management Consulting Methodology: Eight-Stage Transformation Guide** (Rosemann BPM school + Tiger AI L1-L5). Each section maps to the corresponding Stage tools in [`CONSULTING_TOOLKIT_TEMPLATES_EN.md`](CONSULTING_TOOLKIT_TEMPLATES_EN.md).

---

## Cover

Report name: Enterprise AI Transformation Maturity Diagnostic Report
Client: `[Client company]`
Diagnostic period: `[YYYY/MM/DD - YYYY/MM/DD]`
Consulting team: Tiger AI
Methodology: GenAI Consulting Methodology Toolkit · Eight-Stage Transformation Guide
Version: v2.0 (Eight-stage aligned)

---

## 1. Executive Summary

### 1.1 Core Conclusions

`[3-5 bullets for executives. Avoid technical detail. Focus on: standard gaps, distance to excellence, core problem, phased path, change risks.]`

Example:

- Using APQC PCF + Tiger AI L1-L5 dual coordinates, the company shows structural gaps in "Knowledge Management (APQC 11.x)" and "Workflow automation (Tiger AI L3)".
- Compared to industry excellence cases, customer service response, quote turnaround, and knowledge sedimentation are 3-5× behind benchmark.
- The core problem is not lack of tools, but "**no role, no tool, no incentive for knowledge as an asset**" — 80% of gaps stem from this.
- Recommend a three-phase rollout (Foundation 6m / Optimization 6m / Excellence 12m) to avoid one-shot failure.
- Recommended deployment: Hybrid — low-sensitivity tasks on cloud; core ERP and customer data stay in controlled environment.

### 1.2 Maturity and Standard-Gap Overview

| Item | Result |
| --- | --- |
| Reference Model adopted | `[APQC PCF / SCOR / eTOM / ITIL]` + Tiger AI L1-L5 |
| Standard completeness (industry RM) | `[X / 4, with N Missing Categories]` |
| AI adoption maturity (Tiger AI) | `[L1 / L2 / L3 / L4 / L5]` |
| Local maturity | `[e.g. CS L3, Marketing L2]` |
| Distance to industry benchmark | `[3-5× efficiency gap / close]` |
| Recommended deployment mode | `[Cloud AI / Hybrid / Full on-prem]` |
| Priority department | `[Department]` |
| Priority PoC | `[Scenario]` |
| Recommended course mix | `[L1 x%, L2 x%, L3 x%, L4 x%, L5 x%]` |

---

## 2. Methodology

This report is produced via the **Eight-Stage Consulting Methodology** (Rosemann BPM school + Tiger AI L1-L5):

| Stage | Name | Section in this report |
| --- | --- | --- |
| 1 | As-Is Snapshot | §3 |
| 2 | Reference Model Alignment | §4 |
| 3 | Best Practice Integration | §5 |
| 4 | Gap Analysis | §6 |
| 5 | Problem Definition | §7 |
| 6 | Benchmarking & Phased Goals | §8 |
| 7 | To-Be Design | §9 |
| 8 | Implementation & Change | §10-§13 |

### 2.1 Data Sources

1. AI maturity questionnaire (10 / 25 / 50 question versions).
2. Three-layer interviews — exec, dept head, operator (40-question bank).
3. AI Usage Inventory + Systems Inventory.
4. As-Is Process Map (Swimlane).
5. Reference Model Mapping Worksheet (APQC / SCOR / Tiger AI L1-L5).
6. Industry best-practice profiles (≥ 3 benchmark cases).

### 2.2 Models Used

#### Tiger AI L1-L5 (AI adoption axis)

- L1 Controlled AI Access: OpenWebUI.
- L2 Knowledge Codification: Antigravity / Claude Code / Codex.
- L3 Workflow Automation: n8n.
- L4 Autonomous Agent: Hermes Agent.
- L5 Multi-Agent Organization: ClawTeam.

#### Industry Reference Model (business-structure axis)

- Cross-industry: APQC PCF (13 Categories, 1,000+ processes)
- Manufacturing / supply chain: SCOR (Plan / Source / Make / Deliver / Return / Enable)
- Telecom / SaaS: eTOM
- IT services: ITIL
- Software R&D: CMMI

> See [`CONSULTING_TOOLKIT_TEMPLATES_EN.md`](CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 2.1 Reference Model Selection Guide.

### 2.3 Six-Dimension Radar

| Dimension | Score | Observation summary |
| --- | ---: | --- |
| Tool usage | `[0-4]` | `[summary]` |
| Knowledge sedimentation | `[0-4]` | `[summary]` |
| Process automation | `[0-4]` | `[summary]` |
| System integration | `[0-4]` | `[summary]` |
| Agent application | `[0-4]` | `[summary]` |
| Governance & ROI | `[0-4]` | `[summary]` |

---

## 3. As-Is Snapshot (Stage 1)

### 3.1 Key Interview Findings

| Layer | Sessions | Key findings |
| --- | ---: | --- |
| Exec (CEO/COO/CIO) | `[N]` | `[3-5 bullets]` |
| Dept head | `[N]` | `[3-5 bullets]` |
| Front-line | `[N]` | `[3-5 bullets]` |

### 3.2 Systems Inventory Summary

| System | Purpose | API? | Cloud/on-prem | Integration potential |
| --- | --- | --- | --- | --- |
| Gmail / Email | `[purpose]` | `[✓/✗]` | `[Cloud/On-prem]` | `[High/Med/Low]` |
| Sheets / Excel | `[purpose]` | `[✓/✗]` | `[Cloud/On-prem]` | `[High/Med/Low]` |
| CRM | `[purpose]` | `[✓/✗]` | `[Cloud/On-prem]` | `[High/Med/Low]` |
| ERP | `[purpose]` | `[✓/✗]` | `[Cloud/On-prem]` | `[High/Med/Low]` |
| Notion / Wiki | `[purpose]` | `[✓/✗]` | `[Cloud/On-prem]` | `[High/Med/Low]` |
| ... | ... | ... | ... | ... |

### 3.3 Shadow IT Risk

`[List unauthorized AI tool usage, personal accounts handling company data, total monthly spend]`

### 3.4 As-Is Process Maps

Appendix A provides ≥ 3 swimlanes for key processes (with pain density annotations).

---

## 4. Reference Model Alignment (Stage 2)

> **This chapter answers**: By international standards, is the company's operating structure complete? Which Categories are "standard expects, company doesn't have"?

### 4.1 Reference Models Adopted

- **Industry Reference Model**: `[APQC PCF / SCOR / eTOM / ITIL]`
- **AI adoption Reference Model**: Tiger AI L1-L5

### 4.2 Reference Model Mapping Results

| Standard Category | Standard expected capability | Company state | Gap type |
| --- | --- | --- | --- |
| `[APQC 4.0 Deliver]` | `[Order, shipping, customer service]` | `[Complete/Partial/None]` | `[OK / Partial / Missing]` |
| `[APQC 11.0 Knowledge]` | `[Knowledge mgmt, Skill Library]` | `[Complete/Partial/None]` | `[OK / Partial / Missing]` |
| `[Tiger AI L1]` | `[Whole-company Chat AI entry]` | `[Complete/Partial/None]` | `[OK / Partial / Missing]` |
| `[Tiger AI L3]` | `[Workflow automation]` | `[Complete/Partial/None]` | `[OK / Partial / Missing]` |
| ... | ... | ... | ... |

### 4.3 Standard Completeness Radar

`[Insert two radar charts: industry RM Categories + Tiger AI L1-L5; dual lines = company current state vs standard completeness]`

### 4.4 Structural Gap List

| Gap | Mapped to Reference Model | Severity 1-5 |
| --- | --- | --- |
| `[Gap 1]` | `[Category]` | `[N]` |
| `[Gap 2]` | `[Category]` | `[N]` |
| ... | ... | ... |

> **Discipline**: This chapter only answers "is the structure complete"; does not answer "why" (§7); does not answer "what to do" (§8-§9).

---

## 5. Best Practice Integration (Stage 3)

> **This chapter answers**: Industry Best Practice is **input material**; client's Ideal Practice is the **target**. This chapter uses industry-leading patterns as input to help the client **expand their own desired future state**, locked in by 3-party signature.
>
> ⚠️ **Critical design**: §5.4 Ideal Practice Definition Table = **the anchor of the entire engagement**. All §6-§13 reasoning is based on this table. Once signed, the client **cannot deny their own chosen targets**.

### 5.1 Benchmark Case Summary

| Benchmark co. | Industry | Size | L-level start → current | Months | Key learnings |
| --- | --- | --- | --- | --- | --- |
| `[Company A]` | `[Industry]` | `[Headcount]` | `[Lx → Ly]` | `[N]` | `[3 bullets]` |
| `[Company B]` | `[Industry]` | `[Headcount]` | `[Lx → Ly]` | `[N]` | `[3 bullets]` |
| `[Company C]` | `[Industry]` | `[Headcount]` | `[Lx → Ly]` | `[N]` | `[3 bullets]` |

### 5.2 Excellence Capability Profile (this-company version)

| Capability | Excellence characteristics (specific, quantifiable) | Leading-case evidence | Distance from current |
| --- | --- | --- | --- |
| Customer service | `[90% complaints triaged in 1hr + 24hr response]` | `[Co. A]` | `[5 days vs 1 day]` |
| Quote turnaround | `[RFQ → quote ≤ 4hr]` | `[Co. B]` | `[4 days vs 4hr]` |
| Knowledge sedimentation | `[≥ 30 Skills added monthly]` | `[Co. C]` | `[0 vs 30/month]` |
| ... | ... | ... | ... |

### 5.3 What L1-L5 Excellence Should Look Like in This Company

| Level | What "excellence" means here |
| --- | --- |
| L1 Controlled AI Access | `[Concretized for company size]` |
| L2 Knowledge Codification | `[Concretized for dept structure]` |
| L3 Workflow Automation | `[Concretized for system map]` |
| L4 Autonomous Agent | `[Concretized for business model]` |
| L5 Multi-Agent Organization | `[Concretized for cross-dept patterns]` |

### 5.4 Client's Ideal Practice Definition Table (**3-Party Signed Version**)

> Produced at the end of Tool 3.6 Co-Creation Workshop, signed by CEO + Sponsor + AI Champion. **This is the anchor of the entire engagement**.

| # | Capability | Mapped RM Category (Stage 2) | Client's Ideal Practice (specific, quantifiable) | Target L-level in 12 mo | Evidence criteria (observable conditions) | Maps to Stage 4 Gap |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `[Customer service]` | `[APQC 4.4 + Tiger AI L3]` | `[90% triaged in 1hr + 24hr human reply]` | `[L3 = 3]` | `[n8n + Reviewer sign-off rate ≥ 95%]` | `[Gap = 5 days → 1 day]` |
| 2 | `[Knowledge sedimentation]` | `[APQC 11.x + Tiger AI L2]` | `[≥ 20 Skills added monthly]` | `[L2 = 3]` | `[Git + Owner + IPOE]` | `[Gap = 0 → 20/month]` |
| 3 | `[Process root cause]` | `[SCOR Make + Tiger AI L4]` | `[Anomaly → hypothesis ≤ 1hr]` | `[L4 = 2]` | `[Hermes Agent + 5 tasks Reviewer pass]` | `[Gap = 3 days → 1hr]` |
| ... | ... | ... | ... | ... | ... | ... |

#### Workshop Consensus Source

- ☑ Step 1: Material display (industry Best Practice + 4-layer architecture)
- ☑ Step 2: Independent voting (avoid executive anchoring)
- ☑ Step 3: Collective consensus
- ☑ Step 4: Organizational Absorption reality check (per §8.3)
- ☑ Step 5: Write into table above

#### Three-Party Signature

| Signer | Role | Name | Signature | Date |
| --- | --- | --- | --- | --- |
| Sponsor | `[CEO / Chairman / President]` | `[___________]` | _____________ | YYYY/MM/DD |
| AI Champion | `[Executive responsible for driving]` | `[___________]` | _____________ | YYYY/MM/DD |
| Consultant representative | `[Tiger AI Lead Consultant]` | `[___________]` | _____________ | YYYY/MM/DD |

> **Effective after signature**. Any subsequent modification requires **all three parties to re-sign** with version control (v1 / v2 ...). Each change records reason, serving as a trigger source for §8 Risk Register.

---

## 6. Gap Analysis (Stage 4)

> **This chapter answers**: Comparing §4 standard + §5 excellence — what's missing? By how much?
>
> ⚠️ **Discipline**: This chapter is **objective gap inventory**, **not risk assessment**. Risk belongs to §13 Risk Register.

### 6.1 Missing / Broken / Redundant Table

| Area | Type (M/B/R) | Description | Mapped to Reference Model | Mapped to excellence | Severity 1-5 | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| `[Area]` | `[M/B/R]` | `[Description]` | `[Category]` | `[Excellence char.]` | `[N]` | `[Owner]` |
| ... | ... | ... | ... | ... | ... | ... |

### 6.2 Impact × Effort Matrix

| Scenario | Impact (1-5) | Effort (1-5) | Strategic Fit (1-5) | Score = (I × SF) / E | Rank |
| --- | ---: | ---: | ---: | ---: | ---: |
| `[Scenario 1]` | `[N]` | `[N]` | `[N]` | `[N]` | `[N]` |
| `[Scenario 2]` | `[N]` | `[N]` | `[N]` | `[N]` | `[N]` |
| ... | ... | ... | ... | ... | ... |

### 6.3 Gap Distribution Observations

`[Observations by M/B/R distribution, by department, by Reference Model Category]`

---

## 7. Executive Problem Statement (Stage 5)

> **This chapter answers**: Using 80/20, what is the "core problem" the company actually needs to solve?

### 7.1 80/20 Convergence Result

`[From the §6 pile of gaps, find the 3-5 with the largest impact surface; chase 5 Whys to root causes]`

### 7.2 Executive Problem Statement

```
CONTEXT
[What happened in the past 12 months that made AI a priority?]

TENSION
[What is the gap between current "reality" and "expectation"? Quantify, citing §5 excellence characteristics.]

COST OF INACTION
[What happens in 12 months if we don't act? In NT$?]

DESIRED FUTURE
[What does success look like in 12 months? Three quantifiable metrics aligned with §5 excellence.]

CONSTRAINTS
[Budget? Headcount? Compliance? Schedule? Which options are already ruled out?]
```

### 7.3 Core Problem (one sentence)

> `[One sentence defining the core problem. Example: The company has individual-efficiency basics with AI, but lacks departmental Skill sedimentation, cross-system Workflow, and governance — making AI outcomes hard to replicate, hard to measure, and unable to support management decisions.]`

### 7.4 Root Causes

- `[Root cause 1]`
- `[Root cause 2]`
- `[Root cause 3]`

---

## 8. Benchmarking & Phased Goals (Stage 6)

> **This chapter answers**: Decompose §5 excellence into 3-4 "organizationally absorbable" steps, each with acceptance criteria.

### 8.1 Ultimate Benchmark → Phased Goals Decomposition

| Capability | Ultimate benchmark (§5 excellence) | Phase 1: Foundation (0-6m) | Phase 2: Optimization (6-12m) | Phase 3: Excellence (12-24m) |
| --- | --- | --- | --- | --- |
| `[Capability 1]` | `[Excellence]` | `[Phase 1 goal]` | `[Phase 2 goal]` | `[Phase 3 goal]` |
| `[Capability 2]` | `[Excellence]` | `[Phase 1 goal]` | `[Phase 2 goal]` | `[Phase 3 goal]` |
| ... | ... | ... | ... | ... |

### 8.2 Stage Gate Criteria

#### Phase 1 (Foundation)

- [ ] L1 Gate: `[item]`
- [ ] HITL design confirmed: `[item]`
- [ ] `[other 3-5 items]`

#### Phase 2 (Optimization)

- [ ] L2 Gate: `[item]`
- [ ] L3 Gate: `[item]`
- [ ] `[other 3-5 items]`

#### Phase 3 (Excellence)

- [ ] L4 Gate: `[item]`
- [ ] L5 Gate: `[item]`
- [ ] `[other 3-5 items]`

### 8.3 Organizational Absorption Capacity Assessment

| Dimension | Phase 1 needs | Phase 2 needs | Phase 3 needs | Current state | Gap |
| --- | --- | --- | --- | --- | --- |
| Budget (annual) | `[NT$]` | `[NT$]` | `[NT$]` | `[NT$]` | `[gap]` |
| AI Champion | `[N]` | `[N]` | `[N]` | `[N]` | `[gap]` |
| IT FTE | `[N]` | `[N]` | `[N]` | `[N]` | `[gap]` |
| Staff AI literacy | `[%]` | `[%]` | `[%]` | `[%]` | `[gap]` |
| Change capacity (parallel projects) | `[N]` | `[N]` | `[N]` | `[N]` | `[gap]` |

> **If absorption is insufficient**: extend the phase timeline or shrink the phase goals.

---

## 9. To-Be Design (Stage 7)

> **This chapter answers**: What does each Phase's To-Be Operating Model look like? How do humans and AI split the work?

### 9.1 Phased To-Be Operating Model

#### Phase 1 To-Be (Foundation)

```
[Individual layer] [description]
[Department layer] [description]
[Process layer]    [description]
[System layer]     [description]
[Governance layer] [description]
[Human-AI split]   [%/% ratio]
```

#### Phase 2 To-Be (Optimization)

```
[Same format]
```

#### Phase 3 To-Be (Excellence)

```
[Same format]
```

### 9.2 Human-AI Collaboration Architecture

| Process | Human role | AI role | HITL node | Acceptance criteria |
| --- | --- | --- | --- | --- |
| `[process 1]` | `[role]` | `[role]` | `[node]` | `[criteria]` |
| `[process 2]` | `[role]` | `[role]` | `[node]` | `[criteria]` |
| ... | ... | ... | ... | ... |

### 9.3 Skill / Workflow / Agent Maps

#### Skill Map

| Skill | Owner | Inputs | Outputs | L-level | Status |
| --- | --- | --- | --- | --- | --- |
| `[Skill 1]` | `[Owner]` | `[in]` | `[out]` | `[L]` | `[status]` |
| ... | ... | ... | ... | ... | ... |

#### Workflow Map

| Workflow | Trigger | Systems | Output | Owner |
| --- | --- | --- | --- | --- |
| `[Workflow 1]` | `[trigger]` | `[systems]` | `[output]` | `[Owner]` |
| ... | ... | ... | ... | ... |

#### Agent Map

| Agent | Role | Skills used | Reviewer | Stage acceptance |
| --- | --- | --- | --- | --- |
| `[Agent 1]` | `[Role]` | `[Skills]` | `[Reviewer]` | `[Lx ✓/✗]` |
| ... | ... | ... | ... | ... |

### 9.4 Integration Architecture Choice

Recommended deployment: `[Variant A Cloud / B Hybrid / C Full on-prem]`

Rationale:

- `[Reason 1]`
- `[Reason 2]`
- `[Reason 3]`

---

## 10. Implementation Roadmap (Stage 8 §1)

| Quarter | Phase | Theme | Deliverables | Owner | Stage acceptance | KPI |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | Phase 1 | `[theme]` | `[deliverables]` | `[owner]` | `[L1 Gate]` | `[KPI]` |
| Q2 | Phase 1→2 | `[theme]` | `[deliverables]` | `[owner]` | `[L2/L3 Gate]` | `[KPI]` |
| Q3 | Phase 2 | `[theme]` | `[deliverables]` | `[owner]` | `[L4 Gate]` | `[KPI]` |
| Q4 | Phase 2→3 | `[theme]` | `[deliverables]` | `[owner]` | `[L4 ext]` | `[KPI]` |
| Q5-Q6 | Phase 3 | `[theme]` | `[deliverables]` | `[owner]` | `[L5 Gate]` | `[KPI]` |

> **Mandatory at every quarter end**: revisit the §4 Reference Model radar — is it rounder? Which Categories remain empty?

---

## 11. Change Management Plan (Stage 8 §2)

### 11.1 Stakeholder Map + Communication Plan

| Dimension | Phase 1 | Phase 2 | Phase 3 |
| --- | --- | --- | --- |
| Stakeholder Map | `[Sponsor, Champion, IT, HR]` | `[+ Dept Leads]` | `[+ Whole company]` |
| Communication plan | `[Monthly meeting + monthly report]` | `[Bi-weekly stand-ups + dept reports]` | `[Quarterly all-hands]` |
| Training plan | `[L1 whole-company + L2 reps]` | `[L2 dept + L3 IT]` | `[L4-L5 advanced]` |
| Early adopters | `[5-10]` | `[Whole dept]` | `[Whole company]` |

### 11.2 Resistance-Handling Playbook

| Resistance type | Expected count | Handling | Owner |
| --- | --- | --- | --- |
| Fear of replacement | `[N]` | 1:1 conversation + role redefinition | HR |
| Can't use it | `[N]` | 1:1 mentor + simplified first-success | AI Champion |
| Distrust | `[N]` | Start with "human-review" scenarios | Dept Lead |
| Fear of accountability | `[N]` | Clear HITL nodes + accountability boundary | Sponsor |

---

## 12. Governance Design (Stage 8 §3)

### 12.1 RACI

| Topic | Sponsor | AI Champion | IT | Front-line | Data Owner |
| --- | --- | --- | --- | --- | --- |
| Vision / Roadmap | A | R | C | I | I |
| Reference Model selection | A | R | C | I | C |
| Tool selection | A | C | R | C | C |
| Accounts / permissions | I | C | R | I | A |
| Skill / Workflow build | I | A | R | R | C |
| Change management | A | R | C | C | I |
| Audit / governance | A | C | R | I | R |
| Value tracking / ROI | A | R | C | I | I |

### 12.2 Permission / Governance Matrix

`[Reference CONSULTING_TOOLKIT_TEMPLATES_EN.md Tool 8.4; fill per company roles]`

### 12.3 Audit Log Spec

`[Reference CONSULTING_TOOLKIT_TEMPLATES_EN.md Tool 8.7; fill per company compliance]`

### 12.4 AI Ethics & Data Policy

`[Check the 15-item list in CONSULTING_TOOLKIT_TEMPLATES_EN.md Tool 8.8]`

---

## 13. Value Tracking & Risk Register (Stage 8 §4)

### 13.1 Value Tracking Matrix (Five Dimensions)

| Initiative | Dimension | Baseline | Target | Period | Owner |
| --- | --- | --- | --- | --- | --- |
| `[Init 1]` | Time | `[base]` | `[target]` | `[period]` | `[owner]` |
| `[Init 1]` | Quality | `[base]` | `[target]` | `[period]` | `[owner]` |
| `[Init 1]` | Scale | `[base]` | `[target]` | `[period]` | `[owner]` |
| `[Init 1]` | Risk | `[base]` | `[target]` | `[period]` | `[owner]` |
| `[Init 1]` | Assets | `[base]` | `[target]` | `[period]` | `[owner]` |
| ... | ... | ... | ... | ... | ... |

#### Five Tracking Dimensions

1. **Time** — processing time reduction
2. **Quality** — error rate down, rework reduction
3. **Scale** — beneficiaries, throughput
4. **Risk** — missed cases, compliance violations, sensitive-data leakage
5. **Assets** — Skill count, Wiki entries, Agent count

### 13.2 Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner | Trigger |
| --- | --- | --- | --- | --- | --- |
| Employee resistance | `[H/M/L]` | `[H/M/L]` | `[strategy]` | `[Owner]` | `[trigger]` |
| Sensitive-data leakage | `[H/M/L]` | `[H/M/L]` | `[strategy]` | `[Owner]` | `[trigger]` |
| LLM hallucination | `[H/M/L]` | `[H/M/L]` | `[strategy]` | `[Owner]` | `[trigger]` |
| Budget overrun | `[H/M/L]` | `[H/M/L]` | `[strategy]` | `[Owner]` | `[trigger]` |
| AI vendor outage | `[H/M/L]` | `[H/M/L]` | `[strategy]` | `[Owner]` | `[trigger]` |
| Phase goals indigestible | `[H/M/L]` | `[H/M/L]` | `[strategy]` | `[Owner]` | `[trigger]` |
| ... | ... | ... | ... | ... | ... |

---

## 14. Next-Step SOW Proposal

### 14.1 Recommended Workpackages

| Workpackage | Content | Deliverables | Mapped Phase |
| --- | --- | --- | --- |
| AI usage entry build | OpenWebUI, accounts, models, policy | Entry + policy | Phase 1 |
| Skill Library build | Dept Skill design + templates | Skill Library | Phase 1-2 |
| n8n Workflow PoC | High-value process automation | Workflow PoC | Phase 2 |
| Hermes Agent rollout | Agent task design | Agent task cards + PoC | Phase 2-3 |
| ClawTeam design | Multi-Agent collaboration | Agent Team blueprint | Phase 3 |
| Change management | Training, resistance handling, milestone celebrations | Change plan + materials | Phase 1-3 |
| Governance & value tracking | Permissions, Logs, Stage acceptance, KPIs | Governance + value dashboard | Phase 1-3 |

### 14.2 Recommended Next Steps

1. Confirm §8 three-phase decomposition and the company's absorption assessment.
2. Select first-wave PoC department and scenarios.
3. Designate Business Owner, IT Owner, Change Owner, Sponsor.
4. Complete system and data permission inventory.
5. Launch the first 4-week PoC of Phase 1.
6. Conduct L1 Gate acceptance → revisit §4 Reference Model radar → adjust Roadmap.

---

## Appendices

- Appendix A: As-Is Process Maps (≥ 3 swimlanes)
- Appendix B: Full Reference Model Mapping Worksheet
- Appendix C: Industry Best-Practice Profiles (≥ 3 cases)
- Appendix D: Interview Notes Summary
- Appendix E: Full Systems Inventory Table
- Appendix F: Maturity Questionnaire Raw Responses
- Appendix G: Value Tracking Matrix Baseline Measurement Methods

---

License & Citation

This template is Apache License 2.0; consultants, in-house teams, and derivative methodologies may use, modify, and commercialize, provided the [`NOTICE`](../NOTICE) attribution is preserved.
