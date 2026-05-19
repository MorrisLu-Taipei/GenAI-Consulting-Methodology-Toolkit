# Sample Client Case: K-12 Through-school

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **Sample case for illustration.** Client referred to as **"Through-school K"** (anonymized). Synthesized from real K-12 client patterns + the implementation capability of [`mihozip/google-workspace-admin-project-workflow`](https://github.com/mihozip/google-workspace-admin-project-workflow) (MIT). All numbers are illustrative.
>
> **Evidence Level:** 🔵 **L0 — AI-Simulated Teaching Case** (per Tool 8.9 Evidence Hierarchy)

---

## 0. Benchmark-grade Summary (Tool 3.5, 9 columns)

| # | Field | This case |
| --- | --- | --- |
| 1 | Industry + scale | Education (private through-school), 200 staff / 1,500 students |
| 2 | Starting L-level | L0.5 (teachers use ChatGPT informally; no governance) |
| 3 | Ending L-level | L3 (admin workflow automation live) |
| 4 | Duration | 9 months |
| 5 | RM Category traversed | Tiger AI L1-L3, SME Lite Path 4 phases |
| 6 | Investment | NT$ 800K / 12 person-months (external consultant) + 5-person internal core team at 50% time |
| 7 | Key wins (quantified) | Doc routing 3 days → 4 hours; parent notification drafting 3h → 30min; teacher satisfaction 6.2 → 8.1 |
| 8 | Key failures | Month 4 AI-drafted parent notification went out with errors; HITL Gate redesigned, no recurrence |
| 9 | Applicability | 50-500 staff private / public K-12; using Google Workspace; principal personally supports |

**Deployment mode / code:** Hybrid (cloud Workspace + on-prem OpenWebUI for sensitive student data) / **Through-school K**

---

## 1. Client Profile

| Field | Content |
| --- | --- |
| Client code | Through-school K (private, junior + senior high integrated) |
| Scale | 200 staff (150 teachers / 50 admin); 1,500 students; 50 classes |
| Starting state | L0.5 — 30% of teachers privately use ChatGPT; no governance; no shared tooling; admin fully paper-based |
| Budget | NT$ 800K (9 months) |
| Regulations | Personal Data Protection Act / Child & Youth Welfare Act / MoE AI Ethics Guidelines / Private School Act |
| Primary pains | (1) Paper doc routing takes 3 days (2) Parent notification drafting takes hours (3) Teacher prep load high (4) Repetitive admissions inquiries |

## 2. Consultant Engagement + Diagnostic (Phase A, 3 days)

### 2.1 25-question self-assessment results

Teachers (n=120) + admin (n=40) + principal & deans (n=10) = 170 responses.

| Dimension | Mean / 5 |
|---|---|
| Tool usage | 1.8 (30% private use, no shared) |
| Knowledge codification | 0.8 |
| Process standardization | 1.4 |
| System integration | 0.6 |
| Agent application | 0.2 |
| Governance & ROI | 0.5 |

**Overall L = L0.5**

### 2.2 Interview key findings

- Teachers **highly receptive** to AI (70% want to learn more); admin **suspicious** (afraid of replacement)
- Principal **strongly supports** and willing to personally demo (critical success factor)
- IT center has **only 1 person**; no capacity to deploy LLM independently; must rely on cloud or consultant
- Existing Google Workspace for Education in use for 3 years; staff already familiar

### 2.3 Peer benchmarks (3 cases)

| Peer case | L-level | Tools | Implication |
|---|---|---|---|
| Similar private through-school A | L1.5 | OpenWebUI + Gemini | All-teacher training, 8 weeks reaches L1 |
| Similar private elementary B | L3 | Workspace + Apps Script | L3's main ROI is parent notification automation |
| Neighboring public junior high C | L2 | NotebookLM | Seed-subject teachers can build subject NotebookLM in 6 months |

> Benchmark material adapted from [`mihozip/google-workspace-admin-project-workflow`](https://github.com/mihozip/google-workspace-admin-project-workflow) admin workflow design (MIT).

---

## 3. CEO (Principal) Decision: Primary Pain (Phase B Stage 5)

**Selected:** **"Doc routing + parent notification"** dual pains (highest manual cost + most impact on parent experience)

**Reasoning:**
- ROI most quantifiable (time-cost calculable)
- Doesn't directly touch teaching content (low teacher resistance risk)
- Failure won't explode publicly (doc is internal + parent notification has HITL safeguards)

**Backup:**
- Backup 1: AI admissions assistant
- Backup 2: Teacher prep aid

---

## 4. 90-day Roadmap (Phase B Stage 6-7)

### Sprint 1 (M1: L1 all-hands AI enablement)

- W1: Principal + deans hands-on first (top-down example)
- W2-3: School-wide teacher L1 training (3-hr × 4 sessions) + personal AI account
- W4: Gate 1 acceptance (≥ 95% teachers have accounts + 5 personal prompts each)

**Interim KPI:** Teacher active-usage rate ≥ 60%

### Sprint 2 (M2: L3 doc routing PoC)

- W5: Build first-version doc routing using [`mihozip` repo](https://github.com/mihozip/google-workspace-admin-project-workflow) Apps Script
- W6-7: Pilot 5 doc types (leave / event / procurement / business-trip / class-swap)
- W8: M2 monthly review + admin head demo

**Interim KPI:** Doc routing time from 3 days → 1 day

### Sprint 3 (M3: L3 parent notification PoC)

- W9-10: Parent notification workflow + HITL Gate (**no auto-send to parents**)
- W11: Pilot 3 notification types (school closure / events / parent-teacher conference)
- W12: M3 monthly review + principal + parent representative demo + Gate 3 acceptance

**Final KPI:**
- Doc routing time 3 days → 4 hours (87% reduction)
- Parent notification drafting 3 hr → 30 min (83% reduction)
- 0 AI mis-send incidents to parents
- Admin head can operate independently

---

## 5. Phase C Implementation + Continuous Tuning (M4-M9)

### M4 (critical incident month)

**Incident:** An event-postponement notification — AI-drafted; homeroom teacher clicked "Send" without careful review; sent with a typo + wrong time. Parent group exploded.

**Response (within 24 hours):**
1. Principal personally LINE'd apology + paper letter
2. Paused all AI parent notifications for 1 week
3. Post-mortem: HITL design too lax (teacher pressed send without seeing the diff)
4. Strengthened: UI forces display of "AI-drafted version" + "final version you'll send" side-by-side + must tick 5 items before sending

**Result:** **No similar incident** after re-launch. Parent group gradually accepted "human review + AI acceleration."

### M5-M6

- Complete procurement + event-application use cases
- Start L2 seed-subject teacher training (3 subjects: Chinese / English / Science)
- Teacher NotebookLM construction begins

### M7-M9

- L2 seed subjects continue deepening
- L3 admin 4 use cases all live
- Consultant gradually exits; admin head + AI Champion take over operations
- Monthly meetings shift from monthly → quarterly

---

## 6. Key Wins / Quantified Outcomes

| Metric | Baseline | After 9 months |
|---|---|---|
| Doc routing time (5 doc types avg) | 3 days | 4 hours |
| Parent notification drafting (single) | 3 hours | 30 minutes |
| Teacher AI usage rate | 30% (private) | 85% (public) |
| Teacher job satisfaction (1-10) | 6.2 | 8.1 |
| Admin staff job satisfaction | 5.8 | 7.5 |
| AI mis-send incidents | N/A | 1 (M4, fixed) |
| Parent communication satisfaction (PTA survey) | 7.2 | 8.4 |

## 7. Key Failures / Lessons

1. **M4 parent notification mis-send** — HITL UI design insufficient; teacher pressed send without careful review
2. **L2 seed teachers — couldn't find 4th-5th subjects** — PE + arts teachers showed low AI interest; only 3 subjects reached L2
3. **Consultant exited too quickly** — Consultant left in M7; in M8 a small Apps Script bug emerged with no one to fix it; took 1 week. Subsequent contract added 4-week backup support

## 8. Applicability

| Condition | Required / Bonus |
|---|---|
| 50-500 staff private / public K-12 | Required |
| Using Google Workspace for Education | Required (other systems require major rewrite) |
| **Principal personally supports + demos** | **Required** |
| At least 1 IT center staff (proficiency not required) | Required |
| Teachers overall positive toward AI | Bonus |
| Has parent representative / PTA mechanism | Bonus |
| Budget NT$ 500K-1.5M | Required |

**Not applicable:**
- Principal has strong AI doubts → run a half-day awareness session before deciding
- Teacher union strongly opposes AI involvement → negotiate before launch
- All-paper culture / zero IT foundation → build foundation first

---

## 9. References to Main Toolkit + Overlay

| What was used | Source |
|---|---|
| SME Lite Path 4-phase compression | [`00_Overview/SME_LITE_PATH_EN.md`](../00_Overview/SME_LITE_PATH_EN.md) |
| L1 teacher training deliverables | [`02_Course_Design/_deliverables/L1_*.md`](../02_Course_Design/_deliverables/) |
| L1-L3 school implementation guide | [`02_Course_Design/TigerAI-School-Workspace-Workflow-overlay/TIGERAI_SCHOOL_L1_L3_GUIDE.md`](../02_Course_Design/TigerAI-School-Workspace-Workflow-overlay/TIGERAI_SCHOOL_L1_L3_GUIDE.md) |
| Stage Gate design | [overlay/TIGERAI_STAGE_GATES_SCHOOL.md](../02_Course_Design/TigerAI-School-Workspace-Workflow-overlay/TIGERAI_STAGE_GATES_SCHOOL.md) |
| HITL Gate design | [overlay/TIGERAI_HITL_GATES_SCHOOL.md](../02_Course_Design/TigerAI-School-Workspace-Workflow-overlay/TIGERAI_HITL_GATES_SCHOOL.md) |
| L3 Apps Script implementation | [mihozip/google-workspace-admin-project-workflow](https://github.com/mihozip/google-workspace-admin-project-workflow) (MIT) |

---

## 10. Open Questions

- Does an L4 "school history Hermes Agent" have ROI for medium through-schools? Current judgment: no, but 1-2 cases needed to validate
- When applying the same approach to **public** schools, how do procurement + admin decision-making differences affect timeline? Estimated +50% time
- For multi-school (district-level) unified adoption, are different central-vs-school-based overlays needed?

---

**Version:** v1.0 (2026-05-20)
**Author:** Tiger AI Morris Lu 盧業興
**License:** Apache License 2.0
