# Eight-Stage Consulting Flow: Complete Scenario Story and Closed-Loop Design

> 🌐 中文版本 / Chinese version: [EIGHT_STAGE_FLOW_STORY.md](EIGHT_STAGE_FLOW_STORY.md)
>
> Apache License 2.0 · Author: Morris Lu · Tiger AI

Last updated: 2026-05-15

---

> **What this is**: The 8-stage consulting methodology written as a complete, reproducible, debatable closed-loop story. From questionnaire intake to implementation plan, every step has clear triggers, deliverables, signatures, and lock-in relationships with the next step.
>
> **What this isn't**: not a 6-week linear marathon narrative. Rather **a 3-phase contract model + mid-engagement client signature + quarterly loopback** complete scientific management process.

---

## 0. Improvements over a Linear Walk-Through (3 Better Design Choices)

A typical user's intuition:
> Questionnaire + AI As-Is assessment → compare to RM → maturity + cases benchmarking → score → show client report → client picks Ideal Practice → analyze what's needed → TO-BE recommendations → consulting report → Implementation plan

**The direction is right**. Tiger AI builds 3 improvements on this:

| # | Improvement | Why stronger |
| --- | --- | --- |
| **1** | **Three contract phases** (Phase A Diagnostic / Phase B Strategy / Phase C Implementation), not a 6-week marathon | Client commits low-risk to Phase A first, decides on B / C based on results; consultant avoids over-committing |
| **2** | **End of Phase A: a Mid-Engagement Assessment Report is signed as a deliverable** before launching Phase B Ideal Practice workshop | Client shocked by radar empty cells first, then picks Ideal — avoids fantasy; mid report is also a standalone deliverable |
| **3** | **Every quarter, revisit the Reference Model radar** (continues after entering Phase C Implementation) | Not "done is good" but **"did the structure actually become rounder?"** — this is the scientific closed-loop falsification mechanism |

> **Why stronger than a linear 6-week marathon**: linear forces client to commit 6 weeks + 24 months at once — psychological barrier too high; 3 phases split decisions, reduce risk, increase acceptance.

---

## 1. Three-Phase Contract Model Overview

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  Phase A: Diagnostic           Phase B: Strategy           Phase C:        ║
║                                                            Implementation  ║
║  ─────────────                ─────────────              ─────────────     ║
║  2 weeks · NT$ 800K           4 weeks · NT$ 2M           24 months · NT$ 7M║
║                                                                             ║
║  Stage 1 + 2 + 3 materials   Stage 3 Ideal Practice      Stage 7 + 8        ║
║                                + Stage 4 + 5                                ║
║                                                            (quarterly       ║
║                                                            radar revisit)  ║
║                                                                             ║
║  Deliverable:                Deliverable:                Deliverable:      ║
║  Mid-engagement              Full diagnostic report      Transformation    ║
║  assessment report           + Ideal Practice            Roadmap +         ║
║  (client receipts)           definition (3-party sign)   Change Mgmt +     ║
║                                                          Value Tracking +  ║
║                                                          Quarterly logs    ║
╚═══════════════════════════════════════════════════════════════════════════╝
                ↑                       ↑                       ↑
            Gate A                  Gate B                   Gate C
        Client decides to     Client decides to        Client decides each
        proceed to B          proceed to C             quarter to continue
```

**Scientific significance**: each Gate is "an exit point where the client can step off" — the consultant **designs this only with confidence** that the previous phase deliverable is **good enough that the client wants to continue**.

---

## 2. The Protagonist: Client M

> ⚠️ **"Client M / MingChang Packaging" is an AI-generated fictional company**, NOT a real client. All scale, KPI, budget, and timeline numbers are **illustrative only**, for methodology teaching purposes. See [`../04_Scenarios/README_EN.md`](../04_Scenarios/README_EN.md) for full academic integrity disclaimer.

- **Industry**: Semiconductor packaging & testing (FATP)
- **Scale**: 700 employees, NT$ 1.2B annual revenue
- **Trigger**: Three direct competitors deployed AI quality inspection and complaint Agents; Customer A's quarterly orders dropped 18%
- **Pain points**: Complaint response 5 days (industry 1 day); proposal turnaround 4 days (industry 1.5 days); defect rate 3.2% (industry 1.8%)
- **Constraints**: Budget cap NT$ 8M; process data on-prem; IT 2 FTE, no growth
- **Roles**: CEO (Sponsor), COO, IT Deputy (potential AI Champion), QC Head, Sales Head, CS Head, HR, Compliance

---

## 3. Phase A: Diagnostic (2 weeks, NT$ 800K)

### Trigger

M Company's CEO receives Tiger AI outreach email + sees the open-source methodology repo on GitHub; secretary schedules 30-min intro.

### Pre-Engagement: 10-Question Quick Survey (sent the following week)

CEO self-fills the 10-question version of [`01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) (5 min).

**Auto-scored result**:

```
6-dimension radar:
  Tool usage              1 / 4 (some execs use ChatGPT privately)
  Knowledge sedimentation 0 / 4 (no Wiki, no SOP)
  Process automation      1 / 4 (Finance 1 Power Automate flow)
  System integration      2 / 4 (ERP/CRM in silos)
  Agent application       0 / 4 (none)
  Governance & ROI        1 / 4 (no AI policy)
Total: 5 / 24 → preliminary L1
```

CEO sees the radar → **first shock** → agrees to sign Phase A contract.

### Phase A Flow (Week 1-2)

#### Week 1 ── Stage 1 As-Is Snapshot: Listen, Observe, No Comment

| Day | Action | Tool | Output |
| --- | --- | --- | --- |
| Day 1-2 | Exec interviews (CEO/COO/CIO × 60 min) + Dept head interviews (QC/Sales/CS/IT/HR × 90 min) | Tool 1.1 (40-Q bank) | Recordings + summaries |
| Day 3 | Operator interviews (Line/Sales/CS × 3 each × 30 min) | Tool 1.1 Section C | Summaries |
| Day 4 | AI Usage Inventory + Systems Inventory | Tool 1.2 + 1.3 | Shadow IT risk map + system map |
| Day 5 | Walkthrough of 3 key processes + draw Swimlanes | Tool 1.4 | 3 As-Is Process Maps |

**End of Week 1**: Consultant tells client "now we know what your company is doing." **No comment, no recommendation.**

#### Week 2 ── Stage 2 Reference Model Alignment + Stage 3 Material Prep

| Day | Action | Tool | Output |
| --- | --- | --- | --- |
| Day 6 | Choose Reference Model: SCOR + APQC + Tiger AI L1-L5 | Tool 2.1 | RM selection rationale |
| Day 7-8 | Mapping Worksheet: locate As-Is in RM cells | Tool 2.2 | Mapping table |
| Day 9 | Standard Capability Gap Checklist + dual radar | Tool 2.3 + 2.4 | Two radars (APQC + Tiger AI) |
| Day 10 | Benchmark case prep (pick semiconductor from 5 stubs + 2 same-industry cases) | Tool 3.1 + 3.3 | 3 Best-Practice Profiles |

> **Phase A discipline**: Day 10 consultant **does NOT yet run Ideal Practice workshop**. Materials only — used next phase.

### Phase A Deliverable: Mid-Engagement Assessment Report (client receipts)

**Day 11-12 write report → Day 13-14 client review → Day 14 closeout meeting**

Mid-engagement report (10-15 pages):

1. **Executive Summary**: "Per international standards, your company shows structural gaps in SCOR Make/Deliver, APQC 11.x Knowledge, Tiger AI L1-L3."
2. **As-Is Snapshot**: interview summaries + system map + 3 Swimlanes
3. **Reference Model Mapping**: Standard Capability Gap Checklist
4. **Dual radar**: APQC + Tiger AI L1-L5 (dotted = benchmark, solid = company)
5. **Industry Best Practice Materials**: 3 same-industry Benchmark Profiles (materials only — **no conclusions drawn yet**)
6. **Next phase recommendation**: Phase B Ideal Practice Workshop (half day) + Stage 4-5 analysis

### Gate A: Client Decides Whether to Proceed to Phase B

**What happens at the closeout meeting**:

- CEO sees radar: "I thought we were doing okay — under the standard these cells are 0?" → **second shock**
- COO flips through Swimlanes: "Our complaint process really has these holes..." → pain points concretized
- IT Deputy sees shadow IT monthly spend: "Private ChatGPT burning NT$ 24,000 with data leaking..." → risk concretized

**90% of clients sign Phase B**. Because:

- Radar gaps aren't consultant-said — international standard-said → **objective**
- Pain is in employee interview recordings → **verifiable**
- Same-industry firms already did it → **achievable**

> **Phase A's design goal IS this shock**: client **sees the gap themselves**, not told by consultant.

---

## 4. Phase B: Strategy (4 weeks, NT$ 2M)

### Week 3 ── Stage 3 Ideal Practice Co-Creation Workshop (half day)

**Day 15 morning** ─ Tool 3.6 Co-Creation Workshop

| Step | Action | Time | Output |
| --- | --- | --- | --- |
| 1. Material display | Consultant **shows only, does not recommend** Tool 3.1/3.3/3.4/2.7 4-layer architecture | 30 min | Shared materials |
| 2. Independent voting | Each person **independently** writes on sticky notes "what I want us to become in 12 months" | 45 min | N sticky notes |
| 3. Collective consensus | Post to 4-layer architecture, find consensus / divergence | 60 min | v1 Ideal Practice draft |
| 4. Reality check | Consultant first intervenes, using Tool 6.3 to challenge feasibility | 45 min | v2 Ideal Practice |
| 5. Define table | Write v2 as "Ideal Practice Definition Table" | 30 min | Signed-version definition table |
| 6. **3-party signature** | CEO + Sponsor + AI Champion | 15 min | Public, auditable document |

**M Company's signed Ideal Practice Definition Table (excerpt)**:

| # | Capability | RM Category | 12-month target | Evidence criteria |
| --- | --- | --- | --- | --- |
| 1 | Complaint response | APQC 4.4 + Tiger AI L3 | 90% in 1hr + 24hr human reply | n8n + Reviewer sign-off rate ≥ 95% |
| 2 | Knowledge sedimentation | APQC 11.x + Tiger AI L2 | ≥ 20 Skills added monthly | Skill Library Git + Owner + IPOE |
| 3 | Process root cause | SCOR Make + Tiger AI L4 | Anomaly → hypothesis ≤ 1hr | Hermes Agent + 5 tasks Reviewer pass |

> **This table is the anchor of the entire engagement**. All subsequent Stage 4-8 computations are based on it; client cannot deny their own signed targets.

### Week 3-4 ── Stage 4 Gap Analysis + Stage 5 Problem Definition

#### Stage 4: Gap = (Client Ideal − Client As-Is)

| Day | Action | Tool | Output |
| --- | --- | --- | --- |
| Day 16-17 | M/B/R classification + Impact × Effort | Tool 4.1 + 4.2 | Gap matrix |
| Day 18 | Prioritization Worksheet | Tool 4.3 | Priority ranking |

#### Stage 5: 80/20 Convergence to Root Cause

| Day | Action | Tool | Output |
| --- | --- | --- | --- |
| Day 19 | 80/20 convergence + 5 Whys | Tool 5.1 + 5.2 | Core lesion list |
| Day 20-21 | Executive Problem Statement | Tool 5.3 + 5.4 | One-sentence definition |

**M Company's Executive Problem Statement**:

> M Company lacks the role, tool, and incentive for "knowledge asset-ization." 80% of gaps (slow complaints / slow quotes / no knowledge sedimentation / slow root cause) stem from "the same thing done repeatedly, no one sediments, no one reuses."

### Week 4 ── Stage 6 Phased Goals + Stage 7 To-Be Design

#### Stage 6: Decompose Ideal into Absorbable Steps

| Day | Action | Tool | Output |
| --- | --- | --- | --- |
| Day 22 | Ultimate Ideal → Phase 1/2/3 decomposition | Tool 6.1 | Decomposition table |
| Day 23 | Organizational absorption assessment (6 dimensions) | Tool 6.3 | Absorption score |
| Day 24 | Stage Gate Criteria | Tool 6.2 | L1-L5 Gate checklists |

> **M Company's absorption assessment finds IT only has 2 FTE; Phase 2 needs +0.5**. Decision: extend Phase 2 from 6 → 9 months. **This adjustment comes from the client looking at the data themselves, not from consultant recommendation**.

#### Stage 7: One To-Be Operating Model per Phase

| Day | Action | Tool | Output |
| --- | --- | --- | --- |
| Day 25-26 | Phased To-Be Operating Models (3 diagrams) | Tool 7.1 | 3 diagrams |
| Day 27 | Human-AI Collaboration + HITL nodes | Tool 7.2 | Per-process split |
| Day 28 | Skill/Workflow/Agent Map + Integration Architecture | Tool 7.3-7.6 | 3 maps + Variant B Hybrid |

### Phase B Deliverable: Full Diagnostic Report + Ideal Practice Definition Table

**Day 29-30 write report → Day 31-32 client review → Day 32 closeout meeting**

Full diagnostic report (30-50 pages) per [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) 14-section structure.

### Gate B: Client Decides Whether to Proceed to Phase C

**95% of clients sign Phase C**. Because:

- Ideal Practice was **signed by them** → undeniable
- Gap is computed by subtraction → **verifiable**
- Phase 1/2/3 fits organizational absorption → **achievable**

---

## 5. Phase C: Implementation (24 months, NT$ 7M)

### Stage 8 Implementation & Change

**First month (Month 1)**

| Day | Action | Tool | Output |
| --- | --- | --- | --- |
| Day 33 | Transformation Roadmap (24 mo / 6 quarters) | Tool 8.1 | Roadmap |
| Day 34 | Change Management Plan + resistance Playbook | Tool 8.2 | Change plan |
| Day 35 | RACI + Permission Matrix + Audit Log | Tool 8.3 + 8.4 + 8.7 | Governance docs |
| Day 36 | Value Tracking Matrix (5 dimensions) | Tool 8.5 | Dashboard spec |
| Day 37 | Risk Register (incorporating case Failures) | Tool 8.6 | Risk log |
| Day 38 | AI Ethics Checklist | Tool 8.8 | Signed ethics |
| Day 39 | SOW + Phase 1 kickoff | — | Phase 1 launched |

### Phase 1 (Months 1-6): Foundation

- L1 whole-company OpenWebUI live
- 5 core Skills published
- AI policy signed by > 90%
- Prompt Library ≥ 30 entries

**End of Month 6 → L1 Gate acceptance + revisit Stage 2 radar**:

```
APQC 11.x Knowledge:  0 → 2 (Skill library starting)
Tiger AI L1:          0 → 4 (full OpenWebUI + 92% policy signed)
Tiger AI L2:          0 → 2 (5 Skills)
```

> The radar **really is rounder**. Client tears up: "So this is scientific management."

### Phase 2 (Months 6-15): Optimization

- L2 Skill Library ≥ 15 entries
- L3 n8n Workflow ≥ 3 live
- HITL nodes fully in place

**End of Month 15 → L2/L3 Gate + radar revisit**:

```
APQC 4.0 Deliver: 1 → 3 (complaint response 5 days → 1 day) ✓ Ideal met
APQC 11.x:        2 → 3 (knowledge sedimentation stable) ✓ Ideal met
Tiger AI L3:      0 → 2 (n8n PoC live)
```

### Phase 3 (Months 15-24): Excellence

- L4 Hermes Agent passes 4A-4E
- L5 ClawTeam cross-dept 1 successful rehearsal

**End of Month 24 → L4/L5 Gate + final radar**:

```
SCOR Make + Tiger AI L4: 0 → 3 (Hermes Agent passes) ✓ Ideal met
Tiger AI L5:             0 → 2 (ClawTeam cross-dept rehearsal)
```

### Gate C Quarterly: Client Can Decide Each Quarter

Every quarter must:

1. Quarter Gate acceptance (per Tool 6.2 checklist)
2. Revisit Stage 2 radar (quantify improvement)
3. Value tracking matrix 5-dimension review
4. Client decides whether to advance, adjust, or pause next quarter

> After 24 months: M Company complaint response 1 day, defect rate 2.0%, customer churn zero, Stage 2 radar **changes from jagged line to nearly round**.

---

## 6. Complete Closed-Loop Diagram

```
                          ┌──────────────────┐
                    ┌────►│ Phase A Diag 2W   │
                    │     │ Stage 1 + 2 + 3   │
                    │     │   material prep   │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Mid Report        │ ← Phase A Deliverable
                    │     │ (client receipts) │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate A
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase B Strat 4W  │
                    │     │ Stage 3 Ideal     │
                    │     │ + Stage 4 + 5     │
                    │     │ + Stage 6 + 7     │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Full Report       │ ← Phase B Deliverable
                    │     │ + Ideal Practice  │
                    │     │   (3-party sign)  │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate B
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase C Impl 24M  │
                    │     │ Stage 8           │
                    │     │ Transformation +  │
                    │     │ Change + Value    │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase 1/2/3       │
                    │     │ Stage Gate accept │
                    │     └────────┬─────────┘
                    │              │
                    │     Quarterly Gate C
                    │              │
                    │     ┌────────▼─────────┐
                    └─────┤ Revisit Stage 2  │
                          │ Radar (rounder?)  │
                          └──────────────────┘
                                  
                          This feedback line is
                          the core falsification
                          mechanism of the
                          scientific closed loop
```

---

## 7. Why This Flow Withstands Client Debate

For every possible challenge, the response location:

| Challenge | Location | Evidence |
| --- | --- | --- |
| "How do you know we're at L1?" | Phase A mid-report §2 radar | 10-Q survey + recordings + system inventory |
| "Why are these cells 0?" | Phase A §3 RM Mapping | APQC / Tiger AI public standards |
| "Who set the target?" | Phase B §5 Ideal Practice table | **Client themselves signed, 3-party signature** |
| "Why is the gap so large?" | Phase B §6 Gap Analysis | Gap = (your signed Ideal − your As-Is) formula |
| "Why customer service before sales?" | Phase B §6.2 | Impact × Effort matrix |
| "Why 24 months?" | Phase B §8 + Tool 6.3 | Case Benchmark + Organizational Absorption |
| "What if it doesn't work?" | Phase C §13 Risk Register | Trigger + Owner + Mitigation |
| "How do you prove it improved?" | Quarterly Gate C | Stage 2 radar + Value Tracking 5 dimensions |
| "Last consultant said L3, you say L2 — who's right?" | Public 0-4 scale + evidence | Any 3rd party can independently verify |

---

## 8. Mapping to the User's Original Flow

| User's step | Phase | Stage | Improvement |
| --- | --- | --- | --- |
| 1. Questionnaire + AI As-Is | Phase A W1 | Stage 1 | + 10-Q quick screen as pre-engagement |
| 2. Compare to RM | Phase A W2 | Stage 2 | 4-layer architecture + dual radar |
| 3. Maturity + cases benchmarking → score | Phase A end W2 | Stage 3 materials | Cases must be Benchmark-grade (9 fields) |
| 4. **Client sees assessment report** | **Phase A Deliverable** | — | **New: mid-report as standalone deliverable + client receipt** |
| 5. Client picks Ideal Practice | Phase B W3 | Stage 3 Tool 3.6 | **Client signs, not consultant prescribes** |
| 6. Analyze what's needed | Phase B W3-W4 | Stage 4 + 5 | Gap = Ideal − As-Is, 80/20 convergence |
| 7. TO-BE recommendations | Phase B W4 | Stage 6 + 7 | Phased + Organizational Absorption assessment |
| 8. Consulting report | Phase B Deliverable | — | 14-section full report + signed Ideal Practice |
| 9. Implementation plan | Phase C kickoff | Stage 8 | Change Mgmt + Value Tracking + Audit |
| **(missing)** | **Quarterly revisit** | — | **New: each quarter revisit Stage 2 radar (scientific closed loop)** |

---

## 9. Relationship to Other Documents

| Document | Relationship to this |
| --- | --- |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 | Provides 8-stage definitions and data flow; this doc is the full process narrative |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Provides "why designed this way" scientific argument; this doc is "how it actually runs" |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | Provides per-stage tool tables |
| [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) | Provides Phase B Deliverable 14-section structure |
| [`../04_Scenarios/`](../04_Scenarios/) | Provides Benchmark-grade cases for Phase A |
| [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) | Provides engagement / pricing / delivery SOP |

---

## 10. Closing: Why the Closed Loop Is Science

This flow **is not a linear marathon** but **a closed loop with feedback**:

- **Each Gate is an exit point** → consultant **has confidence** to design this way (the previous deliverable must be good enough that the client wants to continue)
- **Each Deliverable has client signature** → subsequent reasoning cannot be denied
- **Each quarter revisits Stage 2 radar** → structure actually getting rounder = success, not "PoC done = success"

**That is scientific management**:

- Objective starting point (international standard + client signature)
- Verifiable process (every Stage Gate Criteria)
- Falsifiable endpoint (dual radar before/after + Value Tracking 5 dimensions)

If anyone says "Tiger AI methodology doesn't work," they must **challenge**:

- Is APQC PCF wrong?
- Is Rosemann BPM school wrong?
- Doesn't the client's own signed Ideal Practice count?
- Doesn't our quarterly radar loopback count?

**Hard to do.** That's why we invested in this closed-loop design.

---

License & Citation

This document is Apache License 2.0; may be used, modified, commercialized, provided the [`../NOTICE`](../NOTICE) attribution is preserved.
