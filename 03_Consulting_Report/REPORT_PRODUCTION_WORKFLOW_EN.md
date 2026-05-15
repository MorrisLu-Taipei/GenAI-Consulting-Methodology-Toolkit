# Consulting Report & Deck Production Workflow

> 🌐 中文版本 / Chinese version: [REPORT_PRODUCTION_WORKFLOW.md](REPORT_PRODUCTION_WORKFLOW.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **Attribution:** The 8-step production workflow, Dummy Page, dependency awareness, 7 page layouts, and progressive-disclosure concepts in this document are referenced from and rewritten based on [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills) (MIT License). This document **re-expresses it in this methodology's language and maps it onto the eight-stage consulting structure, `CONSULTING_REPORT_TEMPLATE.md`, and the 3 deck outlines.** See [`../90_References/MCKINSEY_SKILLS_REFERENCE.md`](../90_References/MCKINSEY_SKILLS_REFERENCE.md) for the citation and license note.

---

## 1. How to Use This Workflow

This methodology already has:

- **The eight-stage consulting structure** — "how to diagnose" ([`CONSULTING_TOOLKIT_TEMPLATES.md`](CONSULTING_TOOLKIT_TEMPLATES.md))
- **The diagnostic report template** — "what the report looks like" ([`CONSULTING_REPORT_TEMPLATE.md`](CONSULTING_REPORT_TEMPLATE.md))
- **3 deck outlines** — "what the deck says" ([`../05_Sales/`](../05_Sales/))
- **The classic frameworks library** — "which analytical tools to use" ([`CONSULTING_FRAMEWORKS_LIBRARY.md`](CONSULTING_FRAMEWORKS_LIBRARY.md))

But one piece was missing: **how to efficiently produce the eight-stage diagnostic output into a deliverable report/deck.** This workflow fills that gap.

> The eight stages produce the "diagnostic content"; this workflow *produces* that content into the deliverable in the client's hands.

**Core principles:**

1. **Hypothesis-driven** — set a hypothesis first, then find evidence; do not collect data aimlessly.
2. **Skeleton first, fill in later** (Dummy Page) — design each page's wireframe first, then research and produce.
3. **Page-by-page iteration** — handle one page at a time; do not expand everything at once (avoids context blow-up and aimless research).
4. **Dependency awareness** — some pages can only be done after others are complete (e.g., the executive summary is done last).
5. **Evidence trail** — keep each page's raw data, source URLs, and cleaning process, mapped to this methodology's Evidence discipline.
6. **Progressive disclosure** — when producing with an AI IDE, reference files are loaded only at the steps that need them and released afterward, to save context.

---

## 2. The 8-Step Production Workflow

> Total duration is about 90-150 minutes (depending on report size), mapping to the "deliverable production" phase **after** or **in parallel with** the eight-stage diagnosis.

### Phase A: Problem Decomposition (20-30 min)

**Step 1 — Define Problem Boundaries**
- Input: the client's business problem, the current state and vision from eight-stage Stages 1-2
- What to do: clarify what is in / out of scope, define success metrics
- Output: a problem statement with clear boundaries
- Maps to framework: SCQ (Situation-Complication-Question)
- Maps to eight stages: Stage 1 As-Is Snapshot, Stage 5 Problem Definition
- Loads no reference files, pure conversation

**Step 2-3 — Issue Tree + Hypotheses**
- Input: the problem statement
- What to do: use an Issue Tree to break the problem into MECE sub-problems; form 5-10 **verifiable** hypotheses; do 5-10 targeted verification searches per hypothesis
- Output: a problem decomposition tree + a prioritized hypothesis list (with evidence)
- Maps to frameworks: MECE, Issue Tree, Hypothesis-Driven (see frameworks library §4.1)
- Maps to eight stages: Stage 4 Gap Analysis

> **Hypothesis Tree**: a set of hypotheses about "why this problem exists and which levers can change it." E.g., "growth has stalled, possibly because (a) customer acquisition cost has risen (b) churn has accelerated (c) the market is saturated." Each hypothesis later becomes a section or page of the report.

### Phase B: Design Blueprint (30-40 min)

**Step 4-5 — Dummy Pages + Design Specs**
- Input: the verified hypotheses from Step 3
- What to do: for each hypothesis, choose one of the 7 layouts in §4; specify the color scheme, font sizes, information density; **tag each page's dependency status** (independent / depends on earlier pages / depends on later pages or the hypothesis tree); define each page's data sources and Excel needs
- Output: `[ProjectName]_DummyPages_[date].md` — a per-page blueprint of layout, visual hierarchy, and dependencies
- Maps to eight stages: Stage 6-7 (the presentation design of the solution and roadmap)

> **Dummy Page (wireframe page)**: not the final slide, but its "skeleton spec" — layout type, required data points, chart type, visual elements. Having a Dummy Page before researching avoids aimless data collection and supports "resuming in a different conversation."

### Phase C: Iterative Page Generation (40-80 min)

**Step 6-7 — Per-page data collection → report page + Excel (one loop per page)**

For each page:
1. **Dependency check**: confirm whether the required prerequisite pages are complete; if not, ask the user or offer an alternative
2. On the first iteration, load the Excel data spec
3. Do 2-5 verification searches for this page's data needs
4. Record raw data + URLs in Excel (Section A), then clean / process (Section B)
5. Produce a report page matching the Dummy design — color scheme, fonts, chart type fully aligned
6. Self-check 6 items: layout matches, real data, design consistent, Excel complete, URLs recorded, visual hierarchy
7. Pause and ask the user: "Page X complete — continue?"
8. Clear this page's verification results (release context)
9. Move to the next page

- Output: report pages / slides + an Excel workbook (one sheet per page, with the data trail)
- Maps to eight stages: the content of Stages 3-8 is all "produced" into pages here

**Step 8 — Optional: Word Full Report**
- Only when the user requests it; produces a complete document of narrative + data tables
- Maps to this methodology: the full version of `CONSULTING_REPORT_TEMPLATE.md`

**Step 9 — Iterative Refinement**
- Input: the user's feedback on color, clarity, missing data
- What to do: make common corrections per the §9 troubleshooting playbook
- Output: the revised pages
- **Typical revision cadence**: 2-4 rounds, 20-40 minutes — first draft generated → user feedback → targeted corrections → final polish. Do not expect to get it right in one shot.

---

## 3. The Dummy Page Concept

"Skeleton first, fill in later" is this workflow's most critical discipline.

| Without a Dummy Page | With a Dummy Page |
| --- | --- |
| Frantically research data first, then force a layout | Set the layout skeleton first, then research data with focus |
| Aimless research, an explosion of data collection | Only 2-5 data points researched per page, precise |
| If one conversation runs out, the work breaks | The skeleton remains, so work can resume in another conversation |
| Inconsistent design | Consistent layout, color scheme, font sizes across the whole report |

**Dummy Page spec fields**: page number / layout type (one of the 7 in §4) / assertion title / required data points / chart type / data source / dependency status / Excel needs.

---

## 4. The 7 Page Layout Templates

| # | Layout | Structure | When to use |
| --- | --- | --- | --- |
| 1 | **Title + single chart** | Assertion title at top; main chart in the middle taking 60-70% | A single-data narrative (line / bar / area chart) |
| 2 | **Title + two columns** | Side by side: chart + explanatory text | Text-image pairing, comparative analysis |
| 3 | **Title + 2×2 matrix** | Four-quadrant positioning (e.g., BCG matrix) | Strategic positioning |
| 4 | **Title + table** | A multi-dimensional comparison table | Competitor feature comparison, multi-option contrast |
| 5 | **Title + waterfall chart** | Decompose growth drivers / value change item by item | Decomposing contributions, bridge analysis |
| 6 | **Title + timeline** | A horizontal timeline + supporting chart | Historical progression, development phases |
| 7 | **Insight summary** | 3-5 numbered insight boxes | Section conclusions, recommendation convergence |

**Quick layout choice**: trend → single chart; comparison → two columns/table; strategy → 2×2 matrix; decomposition → waterfall chart; evolution → timeline; conclusion → insight summary.

> Assertion title: the title is itself the conclusion — not "Market Analysis" but "Market growth slowed 18%, mainly due to rising customer acquisition cost." Maps to the Pyramid Principle (frameworks library §4.1).

---

## 5. Dependency Awareness

Pages have three dependency states, which determine the production order:

| Dependency state | When to produce | Example |
| --- | --- | --- |
| **Independent** | Produce immediately | Industry background page, market size page |
| **Depends on earlier pages** | Wait for prerequisite pages to finish | A "summarizing the above three points" wrap-up page |
| **Depends on everything / the hypothesis tree** | Produce last | Executive summary, overall recommendations page |

> The executive summary is always done last — it depends on all other pages. Doing it first causes rework and information gaps.

---

## 6. The Excel Evidence Trail

Each page corresponds to one Excel sheet, in two sections:

- **Section A — raw data**: each data point + source URL + capture time
- **Section B — cleaned data**: data after processing / calculation / alignment, used for charts

This maps to this methodology's **Evidence discipline** (the E in IPOE, the required evidence of a Stage Gate): every number in the report is traceable to its source. When a client or internal audit wants to verify, the Excel is the audit trail.

---

## 7. Progressive Disclosure: Context Management When Producing with an AI IDE

This workflow was originally designed to be executed by an AI assistant (e.g., Claude Code / Antigravity). Key techniques:

- **Reference files are loaded only at the steps that need them** — e.g., the methodology explainer file is loaded only at Steps 2-3 and released afterward.
- **Process page by page, clear after use** — keep only ~5 verification results per page, clear them when done.
- **Effect**: a single conversation can handle 20-25 pages without blowing the token budget.

> This is also an extended application of this methodology's L2 / L4 courses: turning "consulting report production" itself into a Skill / Workflow that an AI IDE can execute.

---

## 8. Mapping to Existing Methodology Assets

| Element of this workflow | Maps to |
| --- | --- |
| Step 1-3 problem decomposition | Eight-stage Stages 1, 4, 5; frameworks library SCQ / MECE / Issue Tree |
| Step 4-5 Dummy Pages | Turning the 3 deck outlines (`05_Sales/*_DECK_OUTLINE.md`) into "per-page specs" |
| Step 6-7 page-by-page production | The actual filling-in of `CONSULTING_REPORT_TEMPLATE.md` sections |
| The 7 page layouts | Extends `05_Sales/VISUAL_ASSETS_SPEC.md` (which originally had only 3 specific visuals) |
| The Excel evidence trail | The Evidence in IPOE, the required evidence of a Stage Gate |
| Assertion titles | The Pyramid Principle in the frameworks library |
| Progressive disclosure | Context management in the L2 Antigravity / L4 Hermes courses |

---

## 9. Troubleshooting Playbook

> 7 common problems and fixes in the report/deck production process. Maps to Step 9 iterative refinement.
> The content is referenced from [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills)'s `troubleshooting.md` (MIT), re-expressed in this methodology's language.

| # | Problem | Symptom | Fix |
| --- | --- | --- | --- |
| 1 | **Text on a dark background is invisible** | Headers / insight boxes / number labels on a dark-blue background become invisible | Check each shape one by one; on a dark background always force white text (see the design rule "dark background must use white text") |
| 2 | **Elements overlap** | The title box and content box overlap, the chart is covered by text | Remove all shapes, systematically rebuild the layout; keep at least 0.2" spacing between elements |
| 3 | **Text overflow** | Content exceeds the container boundary | Pick one of three: shrink font size (9pt→8pt) / increase container height (×1.3) / condense the text |
| 4 | **Chart labels not fully shown** | The secondary labels of a bar chart disappear | The label box height is insufficient; increase the label box height to 0.35" to fit multiple lines |
| 5 | **Timeline and chart widths inconsistent** | The timeline and content chart widths do not align | Set a unified width constant (8.4") and use it for all content elements across the whole deck |
| 6 | **Information density too high** | A single page is packed with 10+ key points | Split into 2-3 pages, each focused, to improve readability (see the density standard) |
| 7 | **Shape style violation** | A large text box uses rounded corners | Large text boxes use only right-angle rectangles; rounded corners only for small labels < 1.5" |

> **Typical revision cadence**: 2-4 rounds, 20-40 minutes — first draft generated → user feedback → targeted corrections → final polish.

---

## 10. Citation & License

The 8-step workflow, Dummy Page, dependency awareness, 7 page layouts, and progressive-disclosure concepts in this workflow are referenced from and rewritten based on [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills) (MIT License, by @Kafurtan). This document has been re-expressed in this methodology's language and mapped to the eight-stage consulting structure and existing delivery assets; McKinsey Problem Solving, MECE, and the Pyramid Principle are public-domain management knowledge.

Full citation and license note: [`../90_References/MCKINSEY_SKILLS_REFERENCE.md`](../90_References/MCKINSEY_SKILLS_REFERENCE.md).
