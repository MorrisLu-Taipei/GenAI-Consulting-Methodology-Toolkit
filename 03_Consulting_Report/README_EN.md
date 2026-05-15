# 03 Consulting Report — Consulting Diagnosis & Report

> 🌐 中文版本 / Chinese version: [README.md](README.md)

## 1. Purpose of This Directory

This directory is the **third phase of the three-phase service flow: Deliver**, and also the **core of the whole methodology's consulting practice**.

Diagnosis (`01`) gives an objective score, and Build (`02`) grows the client's capability — but what a consulting engagement ultimately hands to the client is a **diagnostic report that is structured, evidence-based, has a Roadmap, and is adoptable by decision-makers**. This directory provides everything needed to produce that report: **the tool tables of the eight-stage consulting structure, the classic consulting frameworks library, the report production workflow, and the report template**.

The problem it solves: **without a methodology, a consultant's diagnosis is personal craft based on experience — unscalable, non-replicable for new consultants, and inconsistent in quality.** This directory turns "how a consultant does a diagnosis" into a standard process that can be taught, replicated, and accepted.

Who uses this directory: consultants, senior consultants, new consultants (onboarding), project managers.

## 2. Position in the Methodology

| Axis | Mapping |
| --- | --- |
| Three-phase service flow | **Deliver** — the third phase |
| Eight-stage consulting structure | **This directory IS the tools and report body of the eight stages (Stage 1-8)** |
| L1-L5 maturity | The report cites the client's L-level and course observations |
| Engagement lifecycle | **Delivery — Handover** (the report is the core deliverable) |

> Two orthogonal axes: **L1-L5 is the "capability axis" (`02`'s job); the eight stages are the "diagnostic axis" (this directory's job).** The two cross to produce verifiable deliverables. L1-L5 itself is two axes — the scale axis (L1-L3) and the AI-autonomy axis (L4-L5); see `../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md` §3.0.

## 3. Goals & Benefits

| Goal | Benefit |
| --- | --- |
| Every eight-stage step has a directly usable tool table | Consultants don't redo tool design; new consultants get up to speed fast |
| The classic frameworks library maps to the eight stages | At each step you know "which analytical framework to use" |
| The report production workflow | "Problem → deliverable report/deck" has an SOP, not craft |
| The report template has a fixed structure | Stable delivery quality; decision-makers can understand it |
| The consulting methodology is teachable and replicable | The consulting team can scale |

**If you skip this directory**: every consultant does diagnosis their own way, report quality is inconsistent, new consultants cannot replicate it, and diagnosis degrades into "the personal craft of a senior consultant."

## 4. Usage Flow & Logic

```text
01 diagnostic result + 02 course observations
   ↓
Execute the eight-stage consulting structure (Stage 1-8) stage by stage:
   each stage → use the matching tool table from CONSULTING_TOOLKIT_TEMPLATES.md
            → pick the matching classic framework from CONSULTING_FRAMEWORKS_LIBRARY.md
   ↓
Use the 8-step process in REPORT_PRODUCTION_WORKFLOW.md to "produce" the diagnostic output into a report/deck
   ↓
Fill into the fixed structure of CONSULTING_REPORT_TEMPLATE.md → deliver to the client
```

| Step | Who | When | Input | Output |
| --- | --- | --- | --- | --- |
| Run the eight-stage diagnosis | Consultant | Throughout the engagement (6-12 weeks) | Diagnostic result, course observations, interviews | Eight-stage analysis |
| Select analytical frameworks | Consultant | Each stage | Framework selector | The framework combination for that stage |
| Produce the report | Consultant | Later in the diagnosis | Eight-stage analysis | Report/deck pages |
| Fill the report template | Consultant | Before delivery | The produced content | Complete diagnostic report |
| Deliver | Consultant + PM | Handover | Complete report | Client sign-off |

> Logic: `CONSULTING_TOOLKIT_TEMPLATES` is "the tools to do the diagnosis"; `CONSULTING_FRAMEWORKS_LIBRARY` is "which analytical framework to use at each step"; `REPORT_PRODUCTION_WORKFLOW` is "how to efficiently turn the diagnosis into a deliverable"; `CONSULTING_REPORT_TEMPLATE` is "what the final report looks like." Together they = a complete consulting methodology.

## 5. File Descriptions

### `CONSULTING_REPORT_TEMPLATE.md`

Markdown template for the AI transformation diagnostic report (v2.0 eight-stage aligned). 14-section structure: cover, Executive Summary (with standard-gap overview), methodology, As-Is Snapshot, Reference Model Alignment (APQC + Tiger AI dual coordinates), Best Practice Integration (excellence capability profile), Gap Analysis, Executive Problem Statement, Phased Goals, To-Be Design, Implementation Roadmap, Change Management Plan, Governance Design, Value Tracking & Risk Register, SOW recommendations.

### `CONSULTING_TOOLKIT_TEMPLATES.md`

The **directly usable tool tables** of the eight-stage consulting diagnosis (v2.0 image-aligned). Each stage maps to 1-5 tools: 40-question interview bank, AI/system inventory, As-Is swimlane, **Reference Model Selection (APQC/SCOR/eTOM/ITIL/CMMI) + Mapping Worksheet + Standard Capability Gap Checklist + dual radar**, Best-Practice Profile + Excellence Capability Profile, Missing/Broken/Redundant (**not a risk assessment**), Impact×Effort, **80/20 convergence + 5 Whys**, Problem Statement, **Ultimate Benchmark → Phased Goals + Organizational Absorption assessment**, **Phased To-Be Operating Model + Human-AI Collaboration Architecture (HITL)**, Skill/Workflow/Agent Map, Transformation Roadmap, **Change Management Playbook (with resistance handling)**, RACI, permissions, **Value Tracking Matrix (Time/Quality/Scale/Risk/Assets 5 dimensions)**, Risk Register, Audit, Ethics, standard 6-week schedule.

### `CONSULTING_FRAMEWORKS_LIBRARY.md`

The classic consulting frameworks library. 50+ industry frameworks (MECE, Pyramid Principle, Issue Tree, Porter's 5 Forces, SWOT, BCG Matrix, 5 Whys, Fishbone, Business Model Canvas, WBS/RACI, NPV/IRR, Lean/Six Sigma, etc.) in 7 categories. Includes a "framework selector" (natural language → framework combination), "framework combination chains," each framework mapped to the eight stages, and a §4.8 deep-dive on the operating rules for MECE / Issue Tree / hypothesis formation. Adapted from yoichiojima-2/consultant (MIT).

### `REPORT_PRODUCTION_WORKFLOW.md`

The 8-step production workflow for "problem → deliverable report/deck." Includes the Dummy Page (skeleton first, fill in later), dependency management, 7 page layouts, the Excel evidence trail, progressive disclosure, and a §9 troubleshooting playbook (7 common problems + fixes). Adapted from Kafurtan/mckinsey-consultant-skills (MIT).

### `*_EN.md`

The English-version siblings of the files above.

## 6. Mapping to Other Directories

| Directory | Relationship to this directory | Data flow |
| --- | --- | --- |
| `01_Assessment` | The diagnostic scores and radar are the core input to eight-stage Stage 1 | `01` scores → `03` report |
| `02_Course_Design` | In-class outputs and observations are material for the report's "course observations" section | `02` course observations → `03` report |
| `00_Overview` | The report is the "Deliver" phase of the storyline | `00` story → `03` realization |
| `04_Scenarios` | Eight-stage Stage 3 industry benchmarking cites cases | `04` cases → `03` Stage 3 |
| `06_Delivery` | The report is the core deliverable of the delivery package; maps to Handover | `03` report → `06` delivery acceptance |
| `90_References` | Third-party citations for the frameworks library and report workflow (consultant / mckinsey-skills) | `90` citation → `03` |

## 7. Common Usage Scenarios

- **New consultant onboarding**: first read `CONSULTING_TOOLKIT_TEMPLATES.md` and run through all the samples once, then shadow a real interview.
- **Running a consulting engagement**: use the standard 6-week schedule, each week mapping to certain eight-stage stages, using the corresponding tool tables + frameworks.
- **Producing the report**: use the 8 steps of `REPORT_PRODUCTION_WORKFLOW.md` to turn the diagnostic output into a deck, filled into `CONSULTING_REPORT_TEMPLATE.md`.
- **Client asks "why this framework"**: use the framework selector in `CONSULTING_FRAMEWORKS_LIBRARY.md` to explain.
