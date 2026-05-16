# 04 Scenarios — Scenarios, Cases & Case Index

> 🌐 Language: [繁體中文](README.md) ｜ English ｜ [Deutsch](README_DE.md) ｜ [Français](README_FR.md) ｜ [Español](README_ES.md) ｜ [日本語](README_JA.md) ｜ [한국어](README_KR.md)

> ⚠️ **Important Academic Integrity Disclaimer**
>
> **All 7 SAMPLE_CLIENT_CASE_*.md cases (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education) and any named story protagonists (e.g., "Ming" in [`../00_Overview/CLIENT_JOURNEY_STORY_EN.md`](../00_Overview/CLIENT_JOURNEY_STORY_EN.md)) are AI-generated fictional cases, NOT real client data.**
>
> - **Purpose**: Teaching demonstration, methodology explanation, Stage 1-8 tool practice
> - **Limitation**: All numbers (time, ROI, person-months, budget, KPI) are illustrative only; **must NOT be used as external marketing, contractual commitments, or academic empirical evidence**
> - **Evidence Level**: Per [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9, cases here are **L0 (AI-Simulated Teaching Case)**, below L1 self-report
> - **Real longitudinal cases** will replace these after the 18-24 month pilot study per [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md)

> 🌐 中文版本 / Chinese version: [README.md](README.md)

## 1. Purpose of This Directory

This directory is the whole methodology's **material library and evidence library**. `01`-`03`, `05`, `06` are "methods and processes"; this directory is "**giving the method real scenarios, cases, and pickable examples when it lands**."

The problem it solves: **the biggest sticking point when an enterprise adopts AI is not "we don't know how to do it" but "we don't know what can be done, how others do it, and what it will look like."** This directory provides four kinds of material: (1) **scenario stories** for each role/department (so the client can "see themselves"), (2) the **writing standard and control tables** for cases (so consultants write consistent cases), (3) **7 complete demonstration cases** across industries (a full run from questionnaire to Roadmap), and (4) a **case index of 150+ real LLM applications** (quick lookup along two axes: by L-level and by department).

Who uses this directory: consultants (use scenarios during Discovery to let clients see themselves, use the case index to pick PoCs), sales (use cases to substantiate value), course instructors (use cases as demo topics), clients (read complete cases to understand "what it looks like after adoption").

## 2. Position in the Methodology

| Axis | Mapping |
| --- | --- |
| Three-phase service flow | **Across the whole flow** — Discovery uses scenarios, Build uses cases as topics, Deliver uses cases as substantiation |
| Eight-stage consulting structure | Mainly supports **Stage 1 As-Is Snapshot (current-state scenarios), Stage 3 Best Practice Integration (industry best-practice benchmarking)** |
| L1-L5 maturity | The case index maps each case to an L-level (across the scale axis L1-L3 and the AI-autonomy axis L4-L5) |
| Engagement lifecycle | Sales (Discovery self-identification) + Build (demo topics) |

## 3. Goals & Benefits

| Goal | Benefit |
| --- | --- |
| Provide scenario stories for each role/department | Clients can "see themselves," Discovery focuses faster |
| Case writing standard and control tables | Consultants write structurally consistent, verifiable cases |
| 7 complete industry demonstration cases | Clients see "the full picture after adoption"; new consultants have a template |
| 150+ LLM application case index (two-axis lookup) | Clients/consultants instantly look up what's doable by "L-level" or "department" |
| Cross-level expectation management | When a client points at an L5 case, use the index to point out "you're at L2, you need to fill these first" |

**If you skip this directory**: clients have no idea "what can be done," PoC topics are picked out of thin air, case quality is inconsistent, and cross-level expectations cannot be managed.

## 4. Usage Flow & Logic

```text
Discovery phase
   → CUSTOMER_SCENARIO_LIBRARY (role scenarios, so the client sees themselves)
   → LLM_APPS_CASE_INDEX (by the client's L-level + department, pick cases the client "feels")
   → picked cases → PoC candidates

Course / proposal phase
   → SAMPLE_CLIENT_CASE_* (show the client a complete same-industry case)
   → LLM_APPS_CASE_INDEX (classroom demo topics, exercises)

When a consultant writes a new case
   → CASE_WRITING_STANDARD (the writing standard)
   → CASE_CONTROL_TABLES (control tables, copy and fill directly)
```

| Step | Who | When | Input | Output |
| --- | --- | --- | --- | --- |
| Client self-identification | Consultant | Discovery | Scenario story library | The pain points the client claims |
| Pick PoC candidates | Consultant | After diagnosis | L-level + department → case index | PoC candidate list |
| Show the client a complete case | Sales / consultant | Proposal | Same-industry sample case | Client understands the full picture |
| Write a new case | Consultant | After the project ends | Writing standard + control tables | A new sample case |

> Logic: scenario stories are for "**evoking resonance**" (the client says "yes, that's exactly me"); the case index is for "**fast material selection**" (instant lookup by L-level/department); the complete demonstration cases are for "**showing the full picture**" (from questionnaire to Roadmap); the writing standard is for "**ensuring consistency**" (stable quality for new cases).

## 5. File Descriptions

### Scenarios and standards

| File | Purpose |
| --- | --- |
| `CUSTOMER_SCENARIO_LIBRARY.md` | Scenario stories for each role/department: CEO, COO, IT, HR, and the Sales, Customer Service, Marketing, Operations, Finance, HR, and IT departments; each story includes Before, Trigger, AI Flow, Systems, Output, KPI. |
| `CASE_WRITING_STANDARD.md` | The case writing standard, specifying how to write the L1-L5 Input / Process / Output / Evidence and verifiable deliverables. |
| `CASE_CONTROL_TABLES.md` | Case control tables — copy and fill directly for assessment activities, L1-L5 IPOE, Evidence, Stage Gate, risk governance, Deliverables acceptance. |
| `INDUSTRY_SCENARIOS.md` | Recommended scenarios for 5 industries (retail/education/logistics/software/professional services); each industry includes an intro, L1-L5 baseline, Top 10 scenarios, risk governance, 30-day Quick Win, Anti-Patterns. |

### Complete demonstration cases (all clients are represented by codes)

| File | Case |
| --- | --- |
| `SAMPLE_CLIENT_CASE_MANUFACTURING.md` | A complete R&D/manufacturing case |
| `SAMPLE_CLIENT_CASE_HOSPITAL.md` | Hospital / medical institution (highly sensitive data, fully on-premises, human review) |
| `SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md` | Marketing agency (code: Agency M) |
| `SAMPLE_CLIENT_CASE_B2B_SALES.md` | B2B industrial-equipment vendor (code: Equipment Vendor B), focused on RFP, CRM governance, L5 Pre-RFP Team |
| `SAMPLE_CLIENT_CASE_FINANCIAL.md` | Finance (code: Regional Bank F), fully on-premises, dual review |
| `SAMPLE_CLIENT_CASE_GOVERNMENT.md` | Government agency (code: City Government Digital Bureau G), fully on-premises, triple review |
| `SAMPLE_CLIENT_CASE_EDUCATION.md` | Educational institution (code: University of Technology E), Hybrid, academic ethics |

> Every case runs the full process: questionnaire result → L-level determination → course ratio → in-class output → eight-stage analysis → diagnostic report summary → 30/60/90 Roadmap → ROI → risk governance.

### L5 implementation and case index

| File | Purpose |
| --- | --- |
| `CLAWTEAM_WALKTHROUGH.md` | A complete walkthrough of running a cross-department Agent Team with ClawTeam (HKUDS, MIT) — a manufacturing QA Team — covering environment setup, the task chain, the Human Gate, and the Gate 5 mapping. |
| `LLM_APPS_CASE_INDEX.md` | **The LLM application case index (multi-source).** 150+ real LLM apps, with **two lookup axes**: (1) by L1-L5 / course (2) by enterprise department/function (engineering/finance/HR/sales/marketing/R&D/operations/customer service/legal/data/design/management). Sources: awesome-llm-apps (Apache-2.0), ai-engineering-hub (MIT). |

### `*_EN.md`

The English-version siblings of the files above.

## 6. Mapping to Other Directories

| Directory | Relationship to this directory | Data flow |
| --- | --- | --- |
| `01_Assessment` | The diagnosis's L-level determines which cases to pick from the index | `01` L-level → `04` case filtering |
| `02_Course_Design` | The case/PoC index is the source of classroom demo and practice topics | `04` cases ↔ `02` course topics |
| `03_Consulting_Report` | Eight-stage Stage 3 industry benchmarking cites cases | `04` cases → `03` Stage 3 |
| `05_Sales` | Complete cases and scenarios substantiate sales material | `04` cases → `05` sales substantiation |
| `00_Overview` | Scenario stories are material for the storyline | `04` ↔ `00` |
| `90_References` | Third-party citations for the case index (awesome-llm-apps / ai-engineering-hub) | `90` citation → `04` |

## 7. Common Usage Scenarios

- **Discovery self-identification**: take `CUSTOMER_SCENARIO_LIBRARY.md`, match the client's role, and ask "which story is like you?"
- **Pick a PoC**: after diagnosing the L-level, go to `LLM_APPS_CASE_INDEX.md` §3 by L-level, or §4 by department, and pick 3-5 the client feels.
- **Proposal substantiation**: show a manufacturing client `SAMPLE_CLIENT_CASE_MANUFACTURING.md` to demonstrate the full adoption picture.
- **Cross-level expectation management**: a client points at an L5 case → use the index to point out their L-level and the prerequisite courses needed.
- **Write a new case**: after a project ends, follow `CASE_WRITING_STANDARD.md` + `CASE_CONTROL_TABLES.md` to write it up as a new sample case.

---

## ⭐ Cross-Topic Quick References: 5 Core Themes, Where to Find Them

The whole methodology has 5 main arteries running through every directory. How this directory connects to each:

| Cross-Topic | Primary location | How this directory connects |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + three-engine co-reading** | Root [`README_EN.md`](../README_EN.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](../00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | Cases can be run via Claude Code Tier 2 workflows: `/simulate-engagement` for a full 6-week engagement simulation, `/parallel-perspectives` for 6-stakeholder views, `/devil-pair-debate` to debate the value-laden assumptions of a case |
| 🎓 **Academic foundation (7 pillars)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | The ROI narrative in cases maps to **Real Options** (why Phase 1 with NPV ≈ 0 is still worth investing); the To-Be design in cases maps to **Task-Technology Fit** (which tasks should reach L4, which should stop at L2) |
| 📚 **L1-L5 course education** | [`../02_Course_Design/`](../02_Course_Design/) | The LLM Apps Case Index is classified by L-level and can be picked directly as PoCs; `POC_SCENARIO_SPECS.md` + `N8N_WORKFLOW_TEMPLATES.md` turn cases into L3 in-class hands-on topics |
| 🔁 **Consulting / 8 stages + Phase A→B→C closed-loop** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Cases are the "self-identification" material for Phase A Discovery** (so the client says "yes, that's exactly us"); industry Best Practice maps to eight-stage Stage 3; the 7 complete sample cases serve as templates for the Phase B consulting report |
| 📖 **References / acknowledgments** | [`../90_References/`](../90_References/) §2 acknowledgments | LLM Apps Case Index sources: `Shubhamsaboo/awesome-llm-apps` (Apache-2.0) + `patchy631/ai-engineering-hub` (MIT); full appreciation cards in [`../90_References/README_EN.md`](../90_References/README_EN.md) §2.4; ClawTeam Walkthrough comes from `HKUDS/ClawTeam` (MIT) |
