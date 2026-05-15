# Consulting Frameworks Library

> 🌐 中文版本 / Chinese version: [CONSULTING_FRAMEWORKS_LIBRARY.md](CONSULTING_FRAMEWORKS_LIBRARY.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **Attribution:** The framework list and taxonomy in this library are referenced from and rewritten based on [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant) (MIT License). This document **re-expresses it in this methodology's language and maps it onto our eight-stage consulting structure and L1-L5 maturity model.** See [`../90_References/CONSULTANT_FRAMEWORKS_REFERENCE.md`](../90_References/CONSULTANT_FRAMEWORKS_REFERENCE.md) for the citation and license note.

---

## 1. How to Use This Library

This methodology's core is the **eight-stage consulting structure** (see [`CONSULTING_TOOLKIT_TEMPLATES.md`](CONSULTING_TOOLKIT_TEMPLATES.md)). The eight stages are the "process skeleton"; this library is the set of "analytical tools you can pull into each stage."

> The eight stages tell you *what to do now*; the framework library tells you *which tool can do that step well*.

**Principles of use:**

1. **Locate the stage first, then choose the framework** — do not use a framework for the sake of using a framework.
2. **Frameworks are combined, not used alone** — most business problems need 2-4 frameworks cross-applied.
3. **Answer-First** — give a preliminary hypothesis answer (Day-1 Answer) first, then use frameworks to verify or refute it.
4. **MECE is the underlying discipline** — any decomposition must be "mutually exclusive, collectively exhaustive."

---

## 2. Framework Selector

When a client / learner describes a problem in natural language, use this table to quickly route to the framework combination to use:

| Client says / "I need to…" | Recommended framework combination | Maps to stage |
| --- | --- | --- |
| "I have a complex problem and don't know where to start" | McKinsey 7-Step + MECE + Issue Tree | Stage 1, 4 |
| "I need to explain this clearly / write it as a report" | Pyramid Principle + SCQ + Storyboarding | Stage 5 |
| "Why is profit declining?" | Profitability Framework + Issue Tree + 5 Whys | Stage 4 |
| "I need to evaluate whether to enter this market" | Market Entry + Market Sizing + Porter's 5 Forces | Stage 3 |
| "I need to do overall strategic planning" | PESTEL → Porter's 5 Forces → 3C → SWOT → Issue Tree | Stage 2, 3 |
| "I need to evaluate an M&A / investment" | M&A Framework + Due Diligence + NPV / IRR | Stage 3, 8 |
| "I need to find where the process is going wrong" | 5 Whys + Fishbone + Value Stream Mapping | Stage 1, 4 |
| "I need to prioritize" | 80/20 (Pareto) + Impact×Effort + MECE | Stage 4 |
| "I need to plan this transformation project" | WBS + RACI + Kotter + OKR | Stage 6, 8 |
| "I need to prove this investment is worth doing" | ROI + NPV + IRR + Payback + Break-even | Stage 8 |
| "I need to design a new business / service model" | Business Model Canvas + Design Thinking + Customer Journey | Stage 7 |
| "I need to persuade the organization to accept change" | Kotter 8 Steps + ADKAR + Stakeholder Map | Stage 8 |
| "I need to break an ultimate goal into phases the org can absorb" | Capability Maturity Model + Phased Goal Decomposition + Organizational Absorption | Stage 6 |
| "I need to check whether the company's operating structure is complete" | APQC PCF / SCOR / eTOM + Standard Capability Gap Checklist | Stage 2 |
| "I need to analyze our competitive position" | Porter's 5 Forces + SWOT + Value Chain + Core Competency | Stage 3 |
| "I need to set pricing" | Pricing Framework + Value-Based Pricing + Break-even | Stage 7 |
| "I need to track adoption outcomes" | Balanced Scorecard + OKR + KPI Tree | Stage 8 |

---

## 3. Framework × Eight-Stage Mapping

| Eight Stages | Primary applicable frameworks |
| --- | --- |
| **Stage 1 As-Is Snapshot** | 5 Whys, Fishbone, Issue Tree, McKinsey 7-Step, Value Chain, Value Stream Mapping |
| **Stage 2 Reference Model Alignment** | **APQC PCF, SCOR, eTOM, ITIL, CMMI, Capability Maturity Model**, McKinsey 7S (internal-structure lens), BPM Reference Architecture |
| **Stage 3 Best Practice Integration** | Porter's 5 Forces, PESTEL, 3C, SWOT, BCG Matrix, Core Competency, Benchmarking, Best-in-Class Profiling |
| **Stage 4 Gap Analysis** | MECE, Issue Tree, 80/20 (Pareto), Hypothesis-Driven, Profitability Framework, Impact×Effort, Missing/Broken/Redundant |
| **Stage 5 Problem Definition** | Pyramid Principle, SCQ, Day-1 Answer, MECE, 5 Whys (deep root cause), Hypothesis-Driven |
| **Stage 6 Benchmarking & Phased Goals** | **Capability Maturity Model decomposition, Phased Goal Decomposition, Organizational Absorption Assessment**, OKR (phased targets), Pyramid Principle (phased narrative), Wardley Map |
| **Stage 7 To-Be Design** | **Target Operating Model (TOM), Operating Model Canvas**, Business Model Canvas, Design Thinking, Customer Journey, Jobs-to-be-Done, Service Blueprint, Pricing |
| **Stage 8 Implementation & Change** | **Kotter 8 Steps, ADKAR, Stakeholder Map (the three pillars of change management)**, WBS, RACI, Gantt, PDCA, Lean, Six Sigma, ROI, NPV, IRR, Payback, Break-even, Sensitivity Analysis, Balanced Scorecard, OKR (tracking) |

---

## 4. The Library (by 7 Categories)

> Each framework: **name** | one-line purpose | when to use | maps to our stage.
> For detailed steps, examples, and common pitfalls, consultants are advised to expand this list into their own worksheets (format in §6).

### 4.1 Problem-Solving

| Framework | One-line purpose | When to use | Stage |
| --- | --- | --- | --- |
| **MECE** (mutually exclusive, collectively exhaustive) | Break a problem into non-overlapping, gapless sub-items | The underlying discipline of any decomposition | 1,4,5 |
| **Pyramid Principle** | Conclusion-first, top-down organization of an argument | Writing reports, making presentations, framing problems | 5 |
| **Issue Tree** | Break a big problem layer by layer into verifiable small problems | Structuring a problem | 1,4 |
| **McKinsey 7-Step** | The standard process: define → structure → prioritize → analyze → recommend → communicate → implement | The overall process for a complex problem | 1-6 |
| **SCQ** (Situation-Complication-Question) | Frame a problem with Situation-Complication-Question | Problem definition, report opening | 5 |
| **Hypothesis-Driven** | Set a hypothesis first, then find evidence — do not collect data aimlessly | Analysis efficiency | 4 |
| **80/20 (Pareto)** | Find the 20% of key factors contributing 80% of the result | Prioritization | 4 |
| **Day-1 Answer** | Give a preliminary hypothesis answer at the start, then verify | Answer-first | 5 |

### 4.2 Strategic Analysis

| Framework | One-line purpose | When to use | Stage |
| --- | --- | --- | --- |
| **Porter's 5 Forces** | Analyze industry competitive intensity (buyers, suppliers, new entrants, substitutes, existing rivals) | Industry attractiveness assessment | 3 |
| **SWOT** | Strengths/Weaknesses/Opportunities/Threats four quadrants | Quick competitive-position inventory | 3 |
| **PESTEL** | Political/Economic/Social/Technological/Environmental/Legal macro scan | External environment analysis | 3 |
| **BCG Matrix** | Sort businesses into Stars/Cash Cows/Question Marks/Dogs by market share × growth | Business portfolio decisions | 3 |
| **McKinsey 7S** | Organizational consistency check across 7 S's | Organizational diagnosis, vision alignment | 2 |
| **3C** | Customer / Competitor / Company triangle analysis | The opening move of strategy | 3 |
| **Value Chain** | Decompose enterprise activities to find sources of value and cost | Source-of-competitive-advantage analysis | 1,3 |
| **Ansoff Matrix** | Growth options across existing/new markets × products | Growth strategy | 2 |
| **Core Competency** | Identify the key capabilities hard to imitate | Competitive-advantage positioning | 3 |
| **Blue Ocean** | Escape red-ocean competition, create new demand space | Vision and differentiation | 2 |
| **Scenario Planning** | Prepare for multiple future scenarios | Vision under uncertainty | 2 |

### 4.3 Case Frameworks

| Framework | One-line purpose | When to use | Stage |
| --- | --- | --- | --- |
| **Profitability Framework** | Profit = revenue − cost, decomposed layer by layer | "Why is/isn't it making money" | 4 |
| **Market Sizing** | Estimate market size top-down / bottom-up | Opportunity assessment, entry decisions | 3 |
| **M&A Framework** | Strategic rationale → target analysis → due diligence → synergies | M&A evaluation | 3,8 |
| **Pricing Framework** | The three pricing logics: cost / competition / value | Pricing decisions | 7 |
| **Market Entry** | Whether to enter, how to enter, the entry mode | New-market decisions | 3 |

### 4.4 Business Design

| Framework | One-line purpose | When to use | Stage |
| --- | --- | --- | --- |
| **Business Model Canvas** | Draw the full picture of a business model in 9 boxes | Business/service model design | 7 |
| **Design Thinking** | Empathize → define → ideate → prototype → test | User-centered solution design | 7 |
| **Customer Journey** | Map the experience at every customer touchpoint | Service design, pain-point location | 1,7 |
| **Jobs-to-be-Done** | What job does the customer "hire" the product to do | Demand insight, product positioning | 7 |

### 4.5 Project & Change

| Framework | One-line purpose | When to use | Stage |
| --- | --- | --- | --- |
| **WBS** (Work Breakdown Structure) | Break a project layer by layer into executable work packages | Project planning | 6 |
| **RACI** | Clarify the Responsible/Accountable/Consulted/Informed for each thing | Role accountability | 6 |
| **Gantt Chart** | Visualize the schedule of timeline × work items | Schedule management | 6 |
| **Kotter 8 Steps** | The eight steps of change management | Driving organizational change | 6 |
| **ADKAR** | Awareness-Desire-Knowledge-Ability-Reinforcement | Individual-level change | 6 |
| **OKR** | Objectives and Key Results | Goal alignment and tracking | 2,6,8 |
| **Balanced Scorecard** | Four perspectives: financial/customer/process/learning & growth | Performance measurement | 8 |
| **Stakeholder Map** | Position stakeholders by influence × interest | Change communication strategy | 6 |

### 4.6 Financial Analysis

| Framework | One-line purpose | When to use | Stage |
| --- | --- | --- | --- |
| **ROI** (Return on Investment) | (benefit − cost) / cost | Whether an investment is worth it | 8 |
| **NPV** (Net Present Value) | Sum of future cash flows discounted to present | Cross-period investment decisions | 8 |
| **IRR** (Internal Rate of Return) | The discount rate that makes NPV = 0 | Comparing investment options | 8 |
| **Payback Period** | How long to recoup the investment | Risk and liquidity assessment | 8 |
| **Break-even** | The volume/price point where revenue = cost | Pricing, capacity decisions | 7,8 |
| **Sensitivity Analysis** | The impact of key-assumption changes on the result | Risk assessment | 8 |

### 4.7 Operations

| Framework | One-line purpose | When to use | Stage |
| --- | --- | --- | --- |
| **Lean** | Eliminate waste, keep only value-adding activities | Process improvement | 7 |
| **Six Sigma** | Reduce variation and defects via DMAIC | Quality improvement | 7 |
| **5 Whys** | Ask "why" five times to dig down to the root cause | Root-cause analysis | 1,4 |
| **Fishbone / Ishikawa** | Find causes from multiple angles (people/machine/material/method/environment) | Structuring root causes | 1,4 |
| **PDCA** | The Plan-Do-Check-Act continuous-improvement cycle | The iteration cadence of improvement | 8 |
| **Pareto Analysis** | Use a chart to find the few key problems | Problem prioritization | 4 |
| **Value Stream Mapping** | Map the time and waste of an end-to-end process | Process diagnosis | 1,7 |

---

## 4.8 Deep-Dive: MECE / Issue Tree / Hypothesis Formation

> Each framework in the §4 tables has only a one-liner. This section expands the three **most-used, most-easily-done-wrong** frameworks into operating rules.
> The deep-dive content is referenced from [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills)'s `methodology.md` (MIT), re-expressed in this methodology's language.

### 4.8.1 MECE Operating Rules

| Rule | Description |
| --- | --- |
| **Every layer must be mutually exclusive and collectively exhaustive** | The sub-items at the same layer do not overlap (mutually exclusive) and together cover everything (collectively exhaustive); no duplicate or missing categories |
| **Decompose by logic, not by intuition** | Use business logic, data structure, or an existing framework to decompose — do not group things arbitrarily by feel |
| **2-3 layers is enough early on** | Decompose 2-3 MECE layers at the start; whether to drill further depends on research needs |
| **Verification method** | After decomposing, ask yourself: is there a case that fits into two categories? (not mutually exclusive) Is there a case that fits into no category? (not collectively exhaustive) |

### 4.8.2 Issue Tree Construction Rules

| Rule | Description |
| --- | --- |
| **Decompose with a business-logic formula** | Prefer a quantifiable business formula as the decomposition skeleton. E.g., `market size = number of users × penetration rate × paying rate × unit price`; `profit = revenue − cost`; decompose each factor further |
| **Multi-dimensional decomposition** | Usable cuts: customer type (B2B / B2C / C2C), timeline (history / current / forecast), competitive comparison (peer benchmark / regional differences) |
| **Decompose until "quickly verifiable"** | The endpoint of decomposition is a granularity that "can be verified with one quick data check" — do not over- or under-decompose |
| **Every leaf node must be answerable** | Every terminal sub-question of an Issue Tree must be a question that "can be answered once you find the data" |

### 4.8.3 Hypothesis Formation Rules

| Step | Description |
| --- | --- |
| **1. Preliminary reasoning** | First make a "preliminary judgment" using industry experience and common sense to form a direction |
| **2. Quick verification** | Do 5-10 quick searches to obtain framing information — **not** a full research effort — just verifying whether the direction is right |
| **3. Form the hypothesis** | Write the judgment as "a high-probability judgment + a clear verification path" |
| **Key attribute** | A hypothesis must be **verifiable** — you must be able to point out "which data could prove or refute it." Something unverifiable is not a hypothesis, it's a guess |

### 4.8.4 3-Layer Search Strategy for Data Collection

When verifying hypotheses and filling out an Issue Tree, search in three layers, from coarse to fine:

| Layer | Goal | Example |
| --- | --- | --- |
| **Layer 1: Framing** | Obtain categories and definitions | How the market is categorized, key term definitions |
| **Layer 2: Core metrics** | Obtain quantitative data | Market size, growth rate, market-share leaders |
| **Layer 3: Detail** | Obtain supporting evidence | Cases, user behavior, detailed figures |

**Cross-validation requirement**: cross-validate key data with at least **2-3 sources**; prefer company financial reports, authoritative research institutions, and industry publications.

---

## 5. Framework Combination Chains

Most business problems are not a single framework but a framework chain. Below are common combinations that can be plugged directly into the eight stages:

| Scenario | Framework chain | Falls in which stages |
| --- | --- | --- |
| **Overall strategic planning** | PESTEL → Porter's 5 Forces → 3C → SWOT → Issue Tree | Stage 2-3 |
| **Profit improvement / enterprise transformation** | Profitability Analysis → 5 Whys / Fishbone → Value Chain → Lean / Six Sigma | Stage 4, 7 |
| **M&A evaluation** | Strategic rationale → Market Sizing → Due Diligence → NPV / IRR → Synergies | Stage 3, 8 |
| **New market entry** | PESTEL → Market Sizing → Porter's 5 Forces → Market Entry → NPV | Stage 3, 8 |
| **Driving a transformation project** | Issue Tree → WBS → RACI → Kotter / ADKAR → OKR → Balanced Scorecard | Stage 6, 8 |
| **From problem definition to report** | SCQ → Day-1 Answer → MECE → Issue Tree → Pyramid Principle | Stage 4-5 |

> This methodology's **AI transformation eight stages** is itself a "localized framework chain" — a standard consulting process that localizes and AI-adapts the classic frameworks above and strings them together.

---

## 6. Per-Framework Expansion Format

If a consultant wants to expand a framework into a complete worksheet (for clients or new consultants), a unified format is recommended:

```text
Framework name (中 / EN)
├─ Origin: who proposed it, why
├─ Core Concept: one paragraph + one diagram
├─ Steps: a numbered list
├─ Application: how to actually do it
├─ Example: the decomposition of one concrete business scenario
├─ Common Pitfalls: 3-5 anti-patterns
└─ Maps to: which of this methodology's eight stages
```

This format is referenced from yoichiojima-2/consultant's per-framework document structure, with a "maps-to-stage" column added to align with this methodology.

---

## 7. Citation & License

The framework list, taxonomy, and the "framework selector" / "combination chains" concepts in this library are referenced from and rewritten based on [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant) (MIT License, by @yoichiojima-2). This document has been re-expressed in this methodology's language and mapped to the eight-stage consulting structure; the classic consulting frameworks themselves (MECE, Porter's 5 Forces, etc.) are public-domain management knowledge.

Full citation and license note: [`../90_References/CONSULTANT_FRAMEWORKS_REFERENCE.md`](../90_References/CONSULTANT_FRAMEWORKS_REFERENCE.md).
