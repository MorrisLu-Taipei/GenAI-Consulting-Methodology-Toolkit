# 03 Consulting Report — Consulting Diagnosis & Report (Consulting Closed-Loop)

> 🌐 Language: [繁體中文](README.md) ｜ English ｜ [Deutsch](README_DE.md) ｜ [Français](README_FR.md) ｜ [Español](README_ES.md) ｜ [日本語](README_JA.md) ｜ [한국어](README_KR.md)

## 1. Purpose of This Directory

This directory is the **third phase of the three-phase service flow: Deliver**, and also the **core of the whole methodology's consulting practice**.

Diagnosis (`01`) gives an objective score, and Build (`02`) grows the client's capability — but what a consulting engagement ultimately hands to the client is a **diagnostic report that is structured, evidence-based, has a Roadmap, and is adoptable by decision-makers**. This directory provides everything needed to produce that report: **the tool tables of the eight-stage consulting structure, the classic consulting frameworks library, the report production workflow, and the report template**.

> 🔁 **This directory is not a "6-week linear marathon" — it's the "consulting closed-loop"**. The full closed-loop design is in [`../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md):
> **3-phase contract** (Phase A Diagnosis 2W + Phase B Strategy 4W + Phase C Implementation 24M) + **mid-term assessment report** + **quarterly radar review** (the falsification mechanism of scientific management).
> The point of the loop isn't "we're done when we deliver" — it's "**did the structure actually become rounder?**" — continuously self-falsifying against the Stage 2 Reference Model radar.

The problem it solves: **without a methodology, a consultant's diagnosis is personal craft based on experience — unscalable, non-replicable for new consultants, and inconsistent in quality.** This directory turns "how a consultant does a diagnosis" into a standard, teachable, replicable, and acceptable closed-loop.

Who uses this directory: consultants, senior consultants, new consultants (onboarding), project managers.

## 2. Position in the Methodology

| Axis | Mapping |
| --- | --- |
| Three-phase service flow | **Deliver** — the third phase |
| Eight-stage consulting structure | **This directory IS the tools and report body of the eight stages (Stage 1-8)** |
| **3-phase contract model** | **Phase A Diagnosis 2W → Phase B Strategy 4W → Phase C Implementation 24M + quarterly radar review** (consulting closed-loop) |
| L1-L5 maturity | The report cites the client's L-level and course observations |
| Engagement lifecycle | **Delivery — Handover** (the report is the core deliverable of Phase B; Phase C continuously produces quarterly radar review records) |

> Two orthogonal axes: **L1-L5 is the "capability axis" (`02`'s job); the eight stages are the "diagnostic axis" (this directory's job).** The two cross to produce verifiable deliverables.
>
> **L1-L5 itself is two axes** (scale axis L1-L3 + AI-autonomy axis L4-L5); see [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0.

## 3. Goals & Benefits

| Goal | Benefit |
| --- | --- |
| Every eight-stage step has a directly usable tool table | Consultants don't redo tool design; new consultants get up to speed fast |
| The classic frameworks library maps to the eight stages | At each step you know "which analytical framework to use" |
| The report production workflow | "Problem → deliverable report/deck" has an SOP, not craft |
| The report template has a fixed structure | Stable delivery quality; decision-makers can understand it |
| The consulting methodology is teachable and replicable | The consulting team can scale |

**If you skip this directory**: every consultant does diagnosis their own way, report quality is inconsistent, new consultants cannot replicate it, and diagnosis degrades into "the personal craft of a senior consultant."

## 4. Usage Flow & Logic (Three-Phase Contract + Quarterly Closed-Loop)

```text
01 diagnostic result + 02 course observations
   ↓
┌─ Phase A — Diagnosis (2 weeks) ────────────────────────────┐
│  First half of the eight stages: Awareness / Reference     │
│  Model / Discovery / Gap Analysis                          │
│  → Use CONSULTING_TOOLKIT_TEMPLATES.md tool tables         │
│  → Mid-term Diagnosis Report → client signs off            │
└────────────────────────────────────────────────────────────┘
   ↓ Gate A — client decides whether to renew into Phase B
┌─ Phase B — Strategy (4 weeks) ─────────────────────────────┐
│  Second half of the eight stages: Stakeholder /            │
│  Diagnosis / To-Be Design / Acceptance Test                │
│  → Use REPORT_PRODUCTION_WORKFLOW.md 8-step production     │
│  → Full 14-chapter diagnostic report + 24M Roadmap +       │
│     ROI + governance recommendations                       │
│  → Filled into CONSULTING_REPORT_TEMPLATE.md fixed structure│
└────────────────────────────────────────────────────────────┘
   ↓ Gate B — client signs Phase C SOW
┌─ Phase C — Implementation (24 months) ─ The closed-loop ──┐
│  Phased implementation + **Quarterly Gate C: re-check     │
│  Stage 2 radar**                                            │
│  → Did the structure actually become rounder? If not →    │
│     return to the corresponding Stage to fix               │
│  → Quarterly outputs: radar review records + Roadmap      │
│     correction notes                                        │
└────────────────────────────────────────────────────────────┘
```

| Phase | Duration | Stages | Main tools | Main deliverables |
| --- | --- | --- | --- | --- |
| **Phase A — Diagnosis** | 2 weeks | Stage 1-4 | TOOLKIT first half + FRAMEWORKS selector | **Mid-term assessment report** + signed Reference Model radar |
| **Phase B — Strategy** | 4 weeks | Stage 5-8 | TOOLKIT second half + REPORT_PRODUCTION_WORKFLOW + REPORT_TEMPLATE | **Full 14-chapter diagnostic report** + Roadmap + ROI + governance |
| **Phase C — Implementation** | 24 months | Quarterly review of Stage 2 | TOOLKIT quarterly-radar review tool + Risk Register | **Quarterly radar review records** + Roadmap corrections |

> Logic: `CONSULTING_TOOLKIT_TEMPLATES` is "the tools to do the diagnosis + the quarterly review tool"; `CONSULTING_FRAMEWORKS_LIBRARY` is "which analytical framework to use at each step"; `REPORT_PRODUCTION_WORKFLOW` is "how to efficiently turn the diagnosis into a deliverable"; `CONSULTING_REPORT_TEMPLATE` is "what the final report looks like." Together they = **a complete consulting closed-loop methodology** (not a linear marathon).

> 📖 Full 8-stage dialogue script + closed-loop story: [`../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) (incl. "Why the closed-loop is science" closing).

## 5. File Descriptions

### `CONSULTING_REPORT_TEMPLATE.md`

Markdown template for the AI transformation diagnostic report (v2.0 eight-stage aligned). 14-section structure: cover, Executive Summary (with standard-gap overview), methodology, As-Is Snapshot, Reference Model Alignment (APQC + Tiger AI dual coordinates), Best Practice Integration (excellence capability profile), Gap Analysis, Executive Problem Statement, Phased Goals, To-Be Design, Implementation Roadmap, Change Management Plan, Governance Design, Value Tracking & Risk Register, SOW recommendations.

### `CONSULTING_TOOLKIT_TEMPLATES.md`

The **directly usable tool tables** of the eight-stage consulting diagnosis (v2.0 image-aligned). Each stage maps to 1-5 tools: 40-question interview bank, AI/system inventory, As-Is swimlane, **Reference Model Selection (APQC/SCOR/eTOM/ITIL/CMMI) + Mapping Worksheet + Standard Capability Gap Checklist + dual radar**, Best-Practice Profile + Excellence Capability Profile, Missing/Broken/Redundant (**not a risk assessment**), Impact×Effort, **80/20 convergence + 5 Whys**, Problem Statement, **Ultimate Benchmark → Phased Goals + Organizational Absorption assessment**, **Phased To-Be Operating Model + Human-AI Collaboration Architecture (HITL)**, Skill/Workflow/Agent Map, Transformation Roadmap, **Change Management Playbook (with resistance handling)**, RACI, permissions, **Value Tracking Matrix (Time/Quality/Scale/Risk/Assets 5 dimensions)**, Risk Register, Audit, Ethics, **Phase A 2W + Phase B 4W standard schedule + Phase C quarterly-radar review tool** (consulting closed-loop). Copy-paste ready.

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

## 7. Common Usage Scenarios (By Closed-Loop Phase)

- **New consultant onboarding**: first read `CONSULTING_TOOLKIT_TEMPLATES.md` and run through all the samples once, then read [`../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) for the dialogue script, finally shadow a real interview.
- **Phase A — Diagnosis (2 weeks)**: use TOOLKIT's Stage 1-4 tools (40-question interview, AI/system inventory, Reference Model radar); produce the **Mid-term Diagnosis Report** at the end of the period for Sponsor sign-off.
- **Phase B — Strategy (4 weeks)**: use TOOLKIT's Stage 5-8 tools + the 8 steps of `REPORT_PRODUCTION_WORKFLOW.md` to turn diagnosis into a deck, fill into `CONSULTING_REPORT_TEMPLATE.md`, producing a **full 14-chapter report + 24M Roadmap + ROI**.
- **Phase C — Implementation (24 months, the closed-loop feedback phase)**: each quarter, use the radar-review tool in TOOLKIT to **re-run the Stage 2 Reference Model radar** — compare against the Phase A signed version, see whether "the structure actually became rounder"; if not → return to the corresponding Stage to fix the Roadmap.
- **Client asks "why this framework"**: use the framework selector in `CONSULTING_FRAMEWORKS_LIBRARY.md` to explain.
- **Client asks "what happens after the 6 weeks?"**: show them [`../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) §6 full closed-loop diagram — the point isn't the 6 weeks, it's the 24-month Phase C + quarterly radar review as the falsification mechanism.
