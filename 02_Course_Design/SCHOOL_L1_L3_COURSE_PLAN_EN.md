# K-12 School L1-L3 AI Adoption Course Plan

> Version: v1.0 (2026-05-20)
> Author: Morris Lu (盧業興)
> Applicable level: L1 → L3 (cross-level for K-12 schools)
> Reference case: [`04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL_K12_EN.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL_K12_EN.md)
> Overlay: [`TigerAI-School-Workspace-Workflow-overlay/`](TigerAI-School-Workspace-Workflow-overlay/)
> Upstream: [mihozip/google-workspace-admin-project-workflow](https://github.com/mihozip/google-workspace-admin-project-workflow) (MIT)
> Methodology basis: [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md)

## 1. Positioning

This course is Tiger AI Methodology's cross-level (L1-L3) adoption plan for **K-12 schools**. It is **not** a school-version replacement for the separate L1_OPENWEBUI / L2_ANTIGRAVITY / L3_N8N courses, but rather **integrates them into a 9-month school-paced adoption course**.

### Why K-12 needs cross-level integration

| Factor | Explanation |
|---|---|
| **Academic calendar** | Schools operate by semester. Three separate courses would take 1.5-2 academic years; integrated = 9 months = 1 semester + 1 summer |
| **Limited teacher time** | Teachers teach + grade + admin + counsel; can't simultaneously take 3 separate courses |
| **Admin and teachers need synchronized progress** | L1 all-hands → L2 seed → L3 admin has sequential dependencies; cannot run parallel |
| **Principal needs a single window** | One overall course + one overall budget = easier decision-making |

---

## 2. Required Capabilities (Stage Gates)

Each L tier ends with one Stage Gate (see [overlay/TIGERAI_STAGE_GATES_SCHOOL.md](TigerAI-School-Workspace-Workflow-overlay/TIGERAI_STAGE_GATES_SCHOOL.md)).

| Capability | L-level | Completion criteria |
|---|---|---|
| Personal teacher AI use | L1 | ≥ 95% teachers have accounts + Prompt Library v1 |
| Subject NotebookLM library | L2 | ≥ 5 subjects with NotebookLM + seed teachers sharing |
| Admin workflow automation | L3 | ≥ 2 use cases live + HITL Gate triggered + admin head operates independently |
| Governance policy + signed | L1-L3 throughout | AI usage policy passed by school council + signed by all |

---

## 3. Learning Objectives

> Written per [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) §4 Bloom formula.

### 3.1 Four primary LOs for the CLP

By the end of the K-12 L1-L3 course, learners can:

1. **Apply** AI tools to daily teaching tasks (lesson plans / Email / translation / comments), **producing** a personal Prompt Library of ≥ 5 prompts. (Apply)
2. **Build** a subject NotebookLM library (≥ 10 documents + ≥ 5 subject-specific prompts), **demonstrating** cross-class / cross-grade sharing. (Create)
3. **Design** AI automation for school admin workflows (doc routing / events / procurement / parent notifications), **deploying** ≥ 2 use cases with full HITL Gates. (Create + Apply)
4. **Evaluate** the ROI and Stage Gate achievement of school AI adoption, **producing** a results report for principal + parent representative + next-phase recommendations. (Evaluate)

### 3.2 Detailed capability list

| Primary LO | Supporting capabilities |
| --- | --- |
| LO1 (personal AI) | Login / model selection / 5-element prompts / data boundary judgment / personal Prompt Library |
| LO2 (subject NotebookLM) | NotebookLM setup / material upload / subject prompt design / cross-class sharing mechanism |
| LO3 (admin automation) | Apps Script basics / Workspace integration / HITL Gate design / 4 use-case implementations |
| LO4 (evaluation & reporting) | KPI design / Stage Gate self-assessment / principal briefing / parent representative communication |

### 3.3 Interactive Learning Design

**Engagement activity (required within first 10 min):**

> **Principal + deans go hands-on first**. Let teachers see "if the principal can, so can I." Top-down demo beats any training slides.

**Formative gates (quick self-checks):**

| Section | Formative check | Duration |
|---|---|---|
| L1 training end | Learner completes 1 of today's actual tasks with a prompt on the spot | 10 min |
| L2 training end | Learner opens NotebookLM and asks one of their own course questions | 10 min |
| L3 training end | Learner reads Apps Script flow diagram, identifies HITL Gate | 10 min |
| Governance section end | 10-case data boundary Quiz (90% to pass) | 15 min |

**Summative gate (end of course):** Maps to Gate 1 + Gate 2 + Gate 3 (see §9) + 1 principal-to-parent-representative results report.

### 3.4 Reference materials

| Type | Location | Status |
|---|---|---|
| L1-L3 school implementation guide | [overlay/TIGERAI_SCHOOL_L1_L3_GUIDE.md](TigerAI-School-Workspace-Workflow-overlay/TIGERAI_SCHOOL_L1_L3_GUIDE.md) | ☑ Added |
| Stage Gate full design | [overlay/TIGERAI_STAGE_GATES_SCHOOL.md](TigerAI-School-Workspace-Workflow-overlay/TIGERAI_STAGE_GATES_SCHOOL.md) | ☑ Added |
| HITL Gate full design | [overlay/TIGERAI_HITL_GATES_SCHOOL.md](TigerAI-School-Workspace-Workflow-overlay/TIGERAI_HITL_GATES_SCHOOL.md) | ☑ Added |
| AI usage policy template | [_deliverables/L1_AI_USAGE_POLICY_TEMPLATE.md](_deliverables/L1_AI_USAGE_POLICY_TEMPLATE.md) | ☑ Generic version |
| Teacher Prompt Library starter | [_deliverables/L1_PROMPT_LIBRARY_STARTER.md](_deliverables/L1_PROMPT_LIBRARY_STARTER.md) | ☑ Generic version |
| Data boundary Quiz | [_deliverables/L1_DATA_BOUNDARY_QUIZ.md](_deliverables/L1_DATA_BOUNDARY_QUIZ.md) | ☑ Generic version |
| Admin Runbook | [_deliverables/L1_ADMIN_RUNBOOK.md](_deliverables/L1_ADMIN_RUNBOOK.md) | ☑ Generic version (for school IT) |
| School-specific Prompt Library | TBD (≥ 10 prompts for teacher work contexts) | ☐ TBD |
| School-specific data boundary cases | TBD (10 cases for student data, parent communication) | ☐ TBD |
| L3 Apps Script implementation | [mihozip upstream](https://github.com/mihozip/google-workspace-admin-project-workflow) (MIT) | ☑ Upstream |
| Upstream basic + advanced lesson materials | mihozip `basic-lesson/` + `advanced-lesson/` | ☑ Upstream |

---

## 4. Prerequisites

| Item | Minimum requirement |
|---|---|
| **Principal commitment** | Written commitment to personally participate ≥ 2 hours per month |
| **IT center** | At least 1 person with basic Google Workspace admin rights |
| **Workspace** | Google Workspace for Education in use ≥ 6 months |
| **Budget** | NT$ 500K-1.5M (per scale) |
| **Parent representatives** | PTA exists or can be convened |
| **Teacher willingness** | Teacher representative meeting approved "willing to pilot AI adoption" |
| **Legal / privacy review** | Internal or contracted legal counsel available to review AI usage policy before launch |
| **Network / devices** | All teachers have usable devices + stable on-campus Wi-Fi |

---

## 5. K-12 School L1-L3 IPOE

| Category | Definition |
|---|---|
| **Input** | Teacher work experience, school doc formats, parent communication templates, subject materials, student assignments (de-identified), admin process SOPs, AI usage policy, Google Workspace accounts, Apps Script code (from upstream repo) |
| **Process** | All-hands L1 training → seed-subject L2 training → admin L3 training → Stage Gate acceptance (×3) → HITL Gate design + launch + operations |
| **Output** | Personal Prompt Library v1 / subject NotebookLM × N / admin use cases × 2-4 / AI usage policy / Gate 1-3 acceptance records / principal + parent representative results report |
| **Evidence** | Account list, Prompt Library screenshots, NotebookLM links, execution logs, Apps Script commit history, HITL approval records, KPI comparison table, Stage Gate sign-off forms |

---

## 6. Course Versions

### 6.0 Lecture Map (Foundation version fully broken down)

Per [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) §5.3.

> Lecture type codes: **TH** Talking Head / **S** Screencast / **SL** Slides / **PR** Practice / **EN** Engagement / **RC** Recap

#### §6.1 Half-day School AI Experience (4 hours = ~50 lectures × avg 4.8 min)

| Section | Duration | Lectures | Focus |
|---|---|---|---|
| Intro | 30 min | 5 lectures (incl. Engagement) | Why schools need AI; 4 LO preview; principal 5-min demo |
| L1 Quick Tour | 60 min | 12 lectures | Personal AI use + 5-element prompt + 5 examples |
| Data Boundary | 30 min | 8 lectures | Student data / parent communication red lines + 10-case Quiz |
| L2 / L3 Preview | 60 min | 12 lectures | Subject NotebookLM showcase + admin automation demo (using mihozip repo) |
| Governance Discussion | 30 min | 8 lectures | AI usage policy + Stage Gate + HITL Gate concepts |
| Conclusion | 30 min | 5 lectures | Wrap-up + next steps (proceed to full 9-month course?) |

#### §6.2 Full 9-Month School AI Adoption Course (consultant-led + internal team)

| Phase | Duration | Main activities | Maps to Gate |
|---|---|---|---|
| Phase A Diagnostic | M0 (3 days) | Interviews + 25-q self-assessment + 3-case benchmark + principal picks primary pain | — |
| Phase B Strategy | M0-M1 (2 weeks) | 90-day roadmap + PoC spec + HITL design + Gate criteria | — |
| **L1 All-Hands Enablement** | M1-M2 | Principal + deans first → school-wide 4 × 3-hr sessions → personal Prompt Library | **Gate 1** |
| **L3 Doc Routing PoC** | M2-M3 | Build first use case using mihozip's Apps Script → launch → monthly review | (Part of Gate 3) |
| **L3 Parent Notification PoC** | M3-M4 | HITL Gate design → workflow build → pilot + post-mortem | (Part of Gate 3) |
| **L2 Seed Subject Launch** | M5-M6 | 3-5 subject teachers training → NotebookLM build → cross-class sharing | **Gate 2** |
| **L3 Complete Use Cases** | M6-M7 | Events / procurement use cases live | **Gate 3** |
| **Continuous Tuning** | M7-M9 | Teacher Q&A / admin operations / consultant exit / KPI review | — |

### 6.3 1-Day Workshop (compressed, for schools already at L1)

| Section | Duration | Focus |
|---|---|---|
| AM1: L2 Seed Subject Hands-on | 90 min | NotebookLM build + subject prompts |
| AM2: L3 Concept + Demo | 90 min | mihozip repo walkthrough |
| PM1: HITL Gate Design Workshop | 120 min | 4 category practice |
| PM2: Stage Gate Self-Assessment + Roadmap | 90 min | Principal + deans approve 90-day path |

---

## 7. L1 → L2 → L3 Tier Transition Logic

```text
L1 All-Hands AI Enablement ──────────┐
(Teachers + admin use personal AI;     │
 policy in place)                      │
                                       │
        ↓ L2 trigger: teachers ask     │
"How do I make subject-specific AI?"   │
                                       │
L2 Seed Subject NotebookLM ──────────┤
(5+ subjects with KB; seed teachers    │
 continuously share)                   │
                                       │
        ↓ L3 trigger: admin asks       │
"I see teachers using this; what       │
 about us in admin?"                   │
                                       │
L3 Admin Workflow Automation ────────┤
(Doc / event / procurement / parent    │
 notification × 4 use cases live;      │
 HITL Gates fully in place)            │
                                       │
        ↓ School achieves cross-level   │
School-wide AI culture established ◄──┘
```

**Core discipline: no level-skipping.** Without L1, jumping to L3 = admin auto runs but no one understands; AI becomes a black box.

---

## 8. Mapping to mihozip Upstream Repo

| Upstream file | Use in this course |
|---|---|
| `basic-lesson/` | L1 all-hands teacher training material (use directly + add Tiger AI governance) |
| `advanced-lesson/` | L2 seed-subject teacher training material |
| `src/Code.gs` | L3 admin automation base code; students adapt to own doc format |
| `admin-project-workflow.png` | L3 concept diagram |
| `admin_ai_workflow_detailed_implementation.html` | L3 implementation material |
| `docs/install.md` | L3 deployment SOP |
| `docs/workflow.md` | L3 workflow design reference |
| `docs/privacy.md` | L1-L3 governance reference + Tiger AI HITL Gate complement |
| `docs/testing.md` | L3 testing SOP |
| `docs/troubleshooting.md` | L3 operations SOP |
| `notebooklm_gemini_admin_workflow_agent_*.html` | L2 advanced interactive examples |

> Legal: this course **references upstream MIT files**, **does not copy them to this repo**. Students clone upstream themselves. See [overlay NOTICE.md](TigerAI-School-Workspace-Workflow-overlay/NOTICE.md).

---

## 9. Stage Gates (Overview, full design in overlay)

| Gate | Timing | Signers | Main evidence |
|---|---|---|---|
| **Gate 1** | End of M2 (L1 complete) | Principal + academic dean + IT + AI Champion | Teacher accounts + Prompt Library + signed policy + passed Quiz |
| **Gate 2** | End of M6 (L2 complete) | Academic dean + curriculum head + ≥ 3 subject heads | NotebookLM ≥ 5 subjects + seed teacher sharing records |
| **Gate 3** | End of M9 (L3 complete) | **Principal MUST sign** + dept heads + IT + legal + **parent representative** | ≥ 2 use cases live + KPI comparison + HITL trigger records + legal review |

**No level-skipping without passing Gate.** See [overlay/TIGERAI_STAGE_GATES_SCHOOL.md](TigerAI-School-Workspace-Workflow-overlay/TIGERAI_STAGE_GATES_SCHOOL.md).

---

## 10. Deliverables

After the 9-month course, the school will own:

| Deliverable | Description |
|---|---|
| 1. School AI usage policy v1.0 | Passed by school council, signed by all |
| 2. Personal Prompt Library | Each teacher ≥ 5; school-wide shared ≥ 50 |
| 3. Subject NotebookLM ≥ 5 | Each subject ≥ 10 documents + ≥ 5 subject prompts |
| 4. L3 admin use cases ≥ 2 live | Full Apps Script + HITL Gate + Runbook |
| 5. Stage Gate 1/2/3 acceptance records | Sign-off + KPI comparison + Post-mortem |
| 6. HITL approval log (≥ 6 months) | For future audit |
| 7. Results report to parent representatives / PTA | 1 page |
| 8. ROI calculation table for principal | Time / satisfaction / budget comparison |
| 9. Internal AI Champion development plan | 5-person seed team takeover training records |
| 10. Next-phase recommendations | Proceed to L4? Expand L3? Exit? |

---

## 11. Course Packaging (for sales / platform listing)

| Package | Hours | Audience | Price | SME Lite mapping |
|---|---|---|---|---|
| **Half-day School AI Experience** | 4 hr | All teachers | NT$ 30K-80K | Probing client |
| **1-Day School AI Workshop** | 8 hr | Academic + admin heads | NT$ 80K-200K | SOHO Path |
| **90-Day School AI PoC** | 3 months | Principal + seed team | NT$ 300K-600K | SME Lite Path (reduced) |
| **Full 9-Month School AI Adoption** | 9 months | School-wide + seed + principal | NT$ 600K-1.5M | SME Lite Path (full) |

---

## 12. Relation to Main Toolkit + Other Courses

| Main toolkit / other course | Relationship to this course |
|---|---|
| [`L1_OPENWEBUI_COURSE_PLAN_EN`](L1_OPENWEBUI_COURSE_PLAN_EN.md) | L1 teacher training can reference its §6.1 lecture sequence directly |
| [`L2_ANTIGRAVITY_COURSE_PLAN_EN`](L2_ANTIGRAVITY_COURSE_PLAN_EN.md) | L2 subject NotebookLM concept can reference its Skill design section |
| [`L3_N8N_TIGERAI_COURSE_PLAN_EN`](L3_N8N_TIGERAI_COURSE_PLAN_EN.md) | Provides another L3 route (n8n vs Apps Script) — choose per school's existing systems |
| [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) | This course written per this SOP — includes Bloom LO, interactive learning design, Stage Gates |
| [`../00_Overview/SME_LITE_PATH_EN`](../00_Overview/SME_LITE_PATH_EN.md) | Schools are SMEs; this course is the education-sector implementation of SME Lite Path |
| [`../04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL_K12_EN`](../04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL_K12_EN.md) | Released alongside this course as reference case |
| [overlay/](TigerAI-School-Workspace-Workflow-overlay/) | Source of this course's methodology basis + governance design |

---

**Version:** v1.0 (2026-05-20)
**Author:** Morris Lu (盧業興) · Tiger AI
**License:** Apache License 2.0
