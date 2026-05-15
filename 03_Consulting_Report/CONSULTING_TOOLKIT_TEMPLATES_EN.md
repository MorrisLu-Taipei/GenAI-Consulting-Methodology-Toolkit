# Eight-Stage Consulting Toolkit Templates

> 🌐 中文版本 / Chinese version: [CONSULTING_TOOLKIT_TEMPLATES.md](CONSULTING_TOOLKIT_TEMPLATES.md)
>
> Apache License 2.0 · Author: Morris Lu · Tiger AI
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

This document provides ready-to-use **toolkit templates** for the eight-stage consulting methodology: interview question banks, inventories, reference-model mappings, matrices, worksheets, and checklists. Each stage maps to 1-5 tools and a set of Output KPIs.

> **Core thinking**: operating-model transformation as the center, deploy resources via 80/20, build a continually evolving capability system.
>
> **Methodology backbone** (Rosemann BPM school): As-Is truth → international standard coordinates → industry excellence patterns → objective gaps → core problem → organizationally absorbable phased goals → multi-phase blueprint → change landing.

| Stage | Name | Output KPI |
| --- | --- | --- |
| 1 | As-Is Snapshot | Assessment Report, As-Is Process Maps |
| 2 | Reference Model Alignment | Standard Capability Gap Checklist, Operating Structure Completeness |
| 3 | Best Practice Integration | Industry Benchmark Operating Model, Excellence Capability Profile |
| 4 | Gap Analysis | Gap Matrix (Impact × Effort) — **NOT a risk assessment** |
| 5 | Problem Definition | Executive Problem Statement |
| 6 | Benchmarking & Phased Goals | Stage Gate Criteria |
| 7 | To-Be Design | Phased To-Be Operating Model, Future Process Maps |
| 8 | Implementation & Change | Transformation Roadmap, Change Management Plan, Value Tracking Matrix |

---

## Stage 1: As-Is Snapshot

> **Purpose**: Map information flow and decision flow via interviews and data inventory; identify labor-intensive nodes and bottlenecks. **Answer "what is actually happening" — no comments, no recommendations.**
>
> **Output KPI**: Assessment Report, As-Is Process Maps.

### Tool 1.1 Interview Question Bank (40 questions)

#### A. Executive layer (CEO / COO / CIO) — 12 questions

1. What is your ideal future state of AI in the company?
2. What AI successes and failures have you seen in the past 12 months?
3. What is the company's biggest operational pain point? Can AI help?
4. What AI risks worry you most? (security, compliance, employee resistance, unclear ROI)
5. How much annual budget will you commit to AI transformation?
6. Is there a person accountable for AI? If not, who could take it on?
7. What L1-L5 level do you think we're at? Why?
8. What level do you want to reach in 12 months?
9. Which department, if AI-ed first, would have the biggest company impact?
10. Do you plan to build an internal AI team or rely on external consultants?
11. What's the board's / parent company's attitude toward AI investment?
12. What concrete outcome do you most want from this engagement?

#### B. Department head layer — 14 questions

13. What are the department's key KPIs and pain points?
14. How much of staff time is spent on repetitive work daily?
15. Which work is "the same regardless of who does it" and could be AI-ed?
16. Which work depends heavily on specific senior staff?
17. What SaaS tools does the department use? Integration status?
18. Do staff use ChatGPT / Claude privately? Frequency? Data boundaries?
19. What "golden SOPs" does your department have? Documented?
20. What are the biggest cross-department collaboration obstacles?
21. Which slice of your time do you most want AI to free up?
22. What's the staff attitude toward AI? (enthusiastic / neutral / resistant)
23. How long is new-hire onboarding? Can AI accelerate it?
24. Where are decisions slow — finding data or communication?
25. What AI experiments are worth recording from the past 90 days?
26. Does the department have an "I wish I could automate but never had time" wish list?

#### C. Operator / front-line — 14 questions

27. What are the 5 most repetitive things you do daily?
28. Which systems / tools do you open daily?
29. Which data takes you a long time to find?
30. Do you use AI tools privately? Which one? For what?
31. Where does AI help / not help you?
32. How much faster does AI make report / email / proposal writing?
33. Are you afraid of being replaced by AI? (If yes, in what part)
34. What do you wish your manager would stop asking you to do?
35. Why did the last mistake happen? Could AI have prevented it?
36. What "core expertise" of yours should AI never replace?
37. Where do colleagues use AI better than you?
38. How much time would you spend learning AI?
39. What things are you "faster doing manually than with AI"?
40. Give AI one wish — what should it solve for you?

> **How to use**: 60-90 min per interview; 12 Q for execs, 14 Q for dept heads, 6-8 Q for operators (curated). Record + summarize + code.

---

### Tool 1.2 AI Usage Inventory

| # | Dept | AI tool | Frequency | Users | Approved? | Sensitive data risk | Monthly spend | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Marketing | ChatGPT Plus (personal) | Daily | 8 | ❌ | High (brand) | NT$24,000 | Personal card |
| 2 | Sales | Copilot for Office | Weekly | 15 | ✓ | Medium | NT$45,000 | Corp purchase |
| 3 | IT | Claude.ai (personal) | Daily | 3 | ❌ | Medium (code) | NT$9,000 | Personal acct |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

> **Output**: Shadow IT risk map + procurement consolidation opportunities.

---

### Tool 1.3 Systems Inventory

| System | Vendor / version | Dept owner | Users | Integration (in/out) | Data sensitivity | API available? | Cloud/on-prem | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gmail Workspace | Google | IT | All 250 | OAuth API | Medium | ✓ | Cloud | SSO enabled |
| Salesforce | SF Sales Cloud Pro | Sales | 35 | REST + Webhook | High (PII) | ✓ | Cloud | Renews Dec |
| SAP B1 | 9.3 | Finance | 18 | DI API + ODBC | High | ✓ | On-prem | Heavy customization |
| Notion | Plus | All | 80 | API + Webhook | Medium | ✓ | Cloud | Dept-managed |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

> **Output**: System map + L3 Workflow PoC candidate list.

---

### Tool 1.4 As-Is Process Map (Swimlane Template)

```
Process: Quote-to-Ship
========================================
Actor          | Step                 | System        | Input         | Output        | Pain
---------------|----------------------|---------------|---------------|---------------|-------
Customer       | Send RFQ email       | Email         | Requirements  | RFQ email     | -
Sales          | Triage email         | Gmail         | RFQ email     | Internal route| 30% missed
Sales          | Look up ERP price    | SAP B1        | Part #        | Price list    | Slow + errors
Sales          | Draft quote          | Word + Sheet  | Price list    | Quote draft   | Repetitive
Sales Lead     | Approve quote        | Email         | Quote draft   | Sign / reject | Wait
Sales          | Send quote           | Gmail + PDF   | Approved quote| Quote email   | -
Customer       | Place order          | Email         | Quote         | PO            | -
Sales          | Create SO            | SAP B1        | PO            | SO #          | Re-key
WMS Op         | Pick goods           | WMS           | SO            | Pick list     | Mismatches
Shipping       | Print waybill        | Logistics     | Pick list     | Waybill       | -
========================================
Total time: 4-7 working days avg
Pain summary: missed emails, re-key, slow price lookup, approval wait
AI candidates: L3 Gmail triage, L3 SAP quote auto-draft, L4 Agent approval summary
```

> **Output**: One swimlane per process; mark pain density (0-3 dots per step); pass to Stage 4 for Impact × Effort.

---

## Stage 2: Reference Model Alignment

> **Purpose**: Introduce international standard frameworks (e.g. APQC PCF, SCOR, eTOM, ITIL) to establish a health-check coordinate system for the operating structure. **This is the core of the Rosemann BPM school — instead of subjective consultant judgment, use industry-recognized "standard operating models" to verify whether the company structure is complete.**
>
> **Output KPI**: Standard Capability Gap Checklist, Operating Structure Completeness Analysis.

### Tool 2.1 Reference Model Selection Guide

| Reference Model | Domain | Coverage | When to use |
| --- | --- | --- | --- |
| **APQC PCF (Process Classification Framework)** | Cross-industry | 13 Categories, 1,000+ processes | Whole-company operating-structure mapping (default) |
| **SCOR (Supply Chain Operations Reference)** | Supply chain, manufacturing, logistics | Plan / Source / Make / Deliver / Return / Enable | Manufacturing, retail, logistics |
| **eTOM (Business Process Framework)** | Telecom, subscription | Strategy / Operations / Enterprise | Telecom, SaaS, subscription |
| **ITIL** | IT service mgmt | Service Strategy / Design / Transition / Operation / CSI | IT, MSP |
| **CMMI** | Software dev, process maturity | 5 maturity levels | Software, R&D |
| **Tiger AI L1-L5** | AI adoption maturity | L1 individual → L2 dept → L3 cross-dept → L4 AI autonomy → L5 AI team | AI transformation (**this methodology's AI-axis Reference Model**) |

> **Rule of thumb**: every engagement uses **at least 1 industry Reference Model + Tiger AI L1-L5**. The former checks "business-structure completeness", the latter "AI adoption maturity". The two coordinates intersect to reveal real gaps.

### Tool 2.2 Reference Model Mapping Worksheet

Map the real processes / systems / roles inventoried in Stage 1 onto the chosen Reference Model's standard categories.

| Standard Category | Standard expected capability | Company current state | Mapped As-Is process | Gap type |
| --- | --- | --- | --- | --- |
| APQC 4.0 Deliver Products and Services | Order mgmt, shipping, customer service | Partial | "Quote-to-Ship" swimlane | Partial (see Stage 4) |
| APQC 8.0 Manage Information Technology | IT Governance, API mgmt | Weak | (none) | Missing |
| APQC 11.0 Manage Knowledge | Knowledge sedimentation, Skill Library | Absent | (none) | Missing — AI opportunity |
| SCOR Plan | Demand forecast, supply balancing | Excel manual | (no formal process) | Broken |
| SCOR Source | Procurement, vendor evaluation | Mature | "Procurement" swimlane | OK |
| Tiger AI L1 | Whole-company Chat AI entry | None | (none) | Missing |
| Tiger AI L2 | Dept Skill Library | None | (none) | Missing |
| Tiger AI L3 | n8n / Workflow automation | 1-2 trials | (scattered) | Partial |
| ... | ... | ... | ... | ... |

> **How to use**: dual-axis cross-check — vertical = industry standard categories, horizontal = Tiger AI L1-L5; place every As-Is process into a cell; empty cells = "structural gaps".

### Tool 2.3 Standard Capability Gap Checklist

> The core Output of Stage 2. Answers for management: "By international standards, is your company structure complete?"

| Capability | Standard expects | Company has? | Completeness 0-4 | Evidence | Observation (**no comments, no recommendations**) |
| --- | --- | --- | --- | --- | --- |
| Order mgmt | APQC 4.2 | ✓ | 3 | SAP B1 SO module | Process exists but labor-intensive |
| Knowledge mgmt | APQC 11.x | ✗ | 0 | (no SOP / Wiki) | Completely missing |
| AI governance | (emerging, no standard) | ✗ | 0 | (no policy) | Completely missing |
| Workflow automation | APQC 8.x + Tiger AI L3 | Partial | 1 | 1 n8n trial | Pilot stage |
| ... | ... | ... | ... | ... | ... |

> **Discipline**: Stage 2 only answers "is the structure complete"; **does not answer "why incomplete"** (Stage 5); **does not answer "what to do"** (Stage 6-7).

### Tool 2.4 Operating Structure Completeness Radar

Using completeness scores from Tool 2.3, draw two radar charts: industry Reference Model Categories + Tiger AI L1-L5 (dotted = industry benchmark; solid = this company).

> **Output**: two radars + narrative on "Categories where the company is significantly below standard".

---

## Stage 3: Best Practice Integration

> **Purpose**: Identify industry-leading patterns; define the specific maturity targets and characteristics of "excellence". **Stage 2 used standard frameworks to check "is it complete"; Stage 3 uses industry-leading cases to define "what excellence looks like".**
>
> **Output KPI**: Industry Benchmark Operating Model, Excellence Capability Profile.

### Tool 2.5 Reference Model Qualification Check — Using Maturity Thinking to Derive "What Counts as a Qualified Reference Model"

> **Core logic**: Maturity models themselves tell us "what a qualified reference framework should look like." Applied in reverse, we can (a) judge whether an off-the-shelf RM is qualified, and (b) **DIY one for domains with no off-the-shelf RM** (this is how Tiger AI L1-L5 was created).

#### 10 Qualification Conditions

| # | Condition | Why important | Failure mode |
| --- | --- | --- | --- |
| 1 | **Completeness** | Covers the target domain comprehensively | Loses coordinate value if discoveries don't fit |
| 2 | **MECE** | Categories don't overlap | Same process maps to 2 cells → chaos |
| 3 | **Hierarchical** | ≥ 2-3 levels of decomposition | Too coarse: can't locate; too fine: loses focus |
| 4 | **Measurable Maturity Levels** | 0-4 / Initial→Optimizing scoring | Subjective scoring → client distrust |
| 5 | **Evolution Trajectory** | Stages from "0 to excellence" defined | "What's next?" has no answer |
| 6 | **Industry Recognition** | Maintained by recognized body or backed by cases | Client suspects "you made it up" |
| 7 | **Cross-Org Portability** | Usable across companies | Cannot accumulate experience |
| 8 | **Implementation-Independent** | Describes WHAT, not HOW | Locks in vendor/tech |
| 9 | **Observable Evidence** | Each maturity level has observable signals | Scoring becomes "feeling" |
| 10 | **Versioned & Updatable** | Has owner / version / updates | Can't keep up with new capabilities |

#### Qualification Scorecard

| Reference Model | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Total | Verdict |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | ---: | --- |
| **APQC PCF** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10 | Qualified (cross-industry default) |
| **SCOR** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10 | Qualified (supply chain) |
| **eTOM** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | △ | ✓ | ✓ | ✓ | 9 | Qualified (telecom) |
| **ITIL** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | △ | ✓ | 9 | Qualified (IT services) |
| **CMMI** | △ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 9 | Qualified (software / process maturity) |
| **Tiger AI L1-L5** | ✓ | ✓ | ✓ | ✓ | ✓ | △ | ✓ | ✓ | ✓ | ✓ | 9 | Qualified (AI adoption, new; recognition accumulating) |
| Some consultant-made "AI 8-Step" | ? | ? | ✗ | ✗ | ✗ | ✗ | ? | ? | ✗ | ✗ | < 5 | Unqualified |

> △ = partially met; ✓ = met; ✗ = not met.

#### DIY a Reference Model — 7-Step Process (for domains with no off-the-shelf RM)

When entering a domain with no existing RM (AI, sustainability, ESG, emerging industries), follow these 7 steps. **Tiger AI L1-L5 was built using exactly this logic**:

```
Step 1: Define domain scope            → Conditions 1 + 7
Step 2: List all capability categories  → Condition 2 (MECE)
Step 3: Define 3-5 maturity stages per category → Conditions 4 + 5
Step 4: Define observable maturity features per stage → Condition 9
Step 5: Define inter-stage dependencies → Condition 5
Step 6: Cross-industry validation (≥ 3 industries) → Condition 7
Step 7: Establish owner + version + updates → Conditions 10 + 6
```

#### Why Tiger AI L1-L5 Qualifies

| Condition | How Tiger AI L1-L5 implements it |
| --- | --- |
| 1 Completeness | Covers full spectrum of individual → team AI adoption |
| 2 MECE | L1-L3 scale axis + L4-L5 autonomy axis (orthogonal) |
| 3 Hierarchical | Each L has 5 layers: capability / tools / curriculum / deliverables / acceptance |
| 4 Measurable | 5 observable indicators × 0-4 scale per level |
| 5 Evolution | Clear L1→L2→L3→L4→L5 path; critical L3→L4 boundary |
| 6 Recognition | New (2025), community adoption accumulating (Apache 2.0 + GitHub) |
| 7 Portability | Validated in 7 industries: mfg/hospital/marketing/B2B/financial/gov/education |
| 8 Neutral | Describes WHAT (capability), not bound to specific LLM vendor/tool |
| 9 Auditable | Each level has explicit Stage Gate Criteria |
| 10 Maintained | Version control (GitHub), regular updates, community feedback |

#### Practical Use

1. **Client asks "why APQC / Tiger AI L1-L5?"** — show this table, tick each condition
2. **Client used a consultant's home-made "maturity model" that feels off** — score it; usually 4/5/9/10 fail
3. **Entering a no-RM domain** — run Step 1-7 to DIY
4. **Academic submission / methodology publication** — mandatory self-qualification chapter

---

### Tool 2.6 Reference Model Component Map — Using Maturity Thinking to Derive "Which Components Are Needed"

> **Core logic**: Tool 2.5 solves "is this RM well-designed?" (meta layer); Tool 2.6 solves "**what components should this RM contain?**" (content layer). Visual paradigm: **Dragon1 Enterprise Architecture Reference Model** — flattens all EA-domain components onto one diagram.

#### 5 Derivation Questions

For any new RM domain, ask these 5:

| Question | Component type | Example (AI domain) |
| --- | --- | --- |
| **Q1: Who governs?** | Governance Component | AI Policy, Ethics, Compliance, Risk Committee, Audit Owner |
| **Q2: What is the core?** | Core Capability Component | L1 Chat / L2 Skill / L3 Workflow / L4 Agent / L5 Agent Team |
| **Q3: What enables?** | Enabling Layer Component | Knowledge Mgmt, Data Pipeline, LLM Router, Vector DB, MLOps |
| **Q4: What infrastructure?** | Infrastructure Component | GPU, API Gateway, Identity (SSO), Monitoring, Secret Mgmt |
| **Q5: What's cross-cutting?** | Cross-Cutting Component | Talent/AI literacy (left axis), Risk/Security (right axis top), Value/ROI (right axis bottom), Change Mgmt (across all) |

#### Enterprise AI Reference Model — Component Map (Tiger AI, Dragon1 style)

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                         AI Governance (top governance layer)                      ║
║ ┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐    ║
║ │ AI Policy    │ AI Ethics    │ Compliance   │ Risk Committee│ Audit Owner │    ║
║ └──────────────┴──────────────┴──────────────┴──────────────┴──────────────┘    ║
╠══════╦═══════════════════════════════════════════════════════════════════╦═══════╣
║ Human║                 Core AI Capabilities (L1-L5)                       ║ Risk  ║
║ Capt ║ ┌──────────────────────┐  ┌──────────────────────┐                ║ Sec.  ║
║ axis ║ │ Scale axis (human-led)│  │ AI autonomy axis     │                ║       ║
║      ║ │ L1 Controlled AI Access            │  │ L4 Auto Agent        │                ║ DLP   ║
║ AI   ║ │ L2 Knowledge Codification           │  │ L5 Agent Team        │                ║ Redact║
║ Lit  ║ │ L3 Workflow Automation        │  │  (HITL retained)     │                ║ Audit ║
║      ║ ╠═══════════════════════════════════════════════════════════════╣ Log   ║
║Champ ║              Enabling Layer (supporting)                          ║       ║
║      ║ ┌────────────┬────────────┬────────────┬────────────┬───────────┐ ║       ║
║      ║ │ Knowledge  │ Data        │ LLM Router │ Vector DB  │ Skill Lib │ ║Value/ ║
║      ║ │ Mgmt(Wiki) │ Pipeline    │ (litellm)  │ Embedding  │ Versioned │ ║ROI    ║
║      ║ ├────────────┼────────────┼────────────┼────────────┼───────────┤ ║axis   ║
║      ║ │ MLOps/Eval │ Prompt Lib │ Evaluation │ Reviewer   │ Audit Log │ ║       ║
║      ║ ╠═══════════════════════════════════════════════════════════════╣Time   ║
║      ║              AI Infrastructure (base layer)                       ║Quality║
║      ║ ┌─────────────┬─────────────┬─────────────┬─────────────────────┐ ║Scale  ║
║      ║ │ GPU/Infer   │ API Gateway │ Identity    │ Monitoring          │ ║Risk   ║
║      ║ │ Servers     │ (Rate/Auth) │ SSO + RBAC  │ Grafana/Tracing     │ ║Assets ║
║      ║ ├─────────────┼─────────────┼─────────────┼─────────────────────┤ ║       ║
║      ║ │ Secret Vault│ Backup/HA   │ Deployment: │ Change Mgmt/CI/CD   │ ║       ║
║      ║ │             │             │ Cloud/Hybrid/On-Prem            │ ║       ║
║      ║ └─────────────┴─────────────┴─────────────┴─────────────────────┘ ║       ║
╚══════╩═══════════════════════════════════════════════════════════════════╩═══════╝
```

#### How to Compare Client's Reality

**Step 1**: Print the blank component map (A3 color).
**Step 2**: Based on Stage 1 As-Is inventory, place each existing component into its cell with 3-color tag:
- 🟢 Green: complete and working
- 🟡 Yellow: exists but broken / incomplete
- 🔴 Red: completely missing
- 🔵 Blue duplicate: same cell occupied by multiple systems (Redundant)

**Step 3**: Output a visual "Company AI As-Is Component Map vs Reference Model."
**Step 4**: Gaps → feed directly into Stage 4 M/B/R table and Stage 6 Phased Goals ranking.

---

### Tool 2.7 Four-Layer Architectural Reference Model — Deriving "Why These 4 Layers"

> Tool 2.6 = flat component map. Tool 2.7 upgrades to **4 stacked diamond architecture** (mirroring Dragon1 EA RM), deriving why exactly 4 layers based on the "abstraction × volatility" axis from maturity thinking.

#### Why 4 Layers — Derivation

| Layer | Abstraction | Volatility | Question answered | Cannot merge/skip because |
| --- | --- | --- | --- | --- |
| **L1 Governance Architecture** | Most abstract | Years | Why exist? What to become? | Strategy/policy can't mix with processes (10× volatility difference) |
| **L2 Business Architecture** | Abstract | Quarters-Years | What business? How organized? | Business functions can't mix with data services |
| **L3 Information Architecture** | Medium | Months-Quarters | What info services for business? | Services can't mix with hardware/networks |
| **L4 Technical Architecture** | Most concrete | Weeks-Months | What technology runs it? | Tech mixed into Business locks in choices |

**Planning ↓**: upper layer pushes intent down (Governance sets goals → Business sets processes → Information sets data → IT sets infrastructure).
**Alignment ↑**: lower layer reports reality up (IT constraints → Information constraints → Business constraints → Governance re-adjusts).

#### Tiger AI Enterprise AI Reference Model — 4-Layer (AI Domain Version)

```
                          ◆ Layer 1: AI Governance Architecture
                         ╱  Directing AI, Managing Risk & Compliance
                        ╱   Components: AI Mission / Vision / Owner Identity /
                       ◆      AI Strategy / Enterprise AI Goals / Ethics /
                      ╱       Policy / Compliance / Risk Committee /
              Planning↓        AI Champion / Sponsor / Audit Owner /
              Alignment↑      Third-party AI adoption rules / Trends
                      ╲   
                       ╲   ◆ Layer 2: AI Business Architecture
                        ╲ ╱  AI Operations Delivering Value
                         ◆    Components: Business Goals with AI / L1-L5 /
                        ╱      Scale axis (L1 Chat → L2 Skill → L3 Workflow) /
                  Planning↓    AI Autonomy axis (L4 → L5) /
                  Alignment↑   Human-AI split (HITL nodes) / Dept AI Roles /
                       ╲       Skill / Workflow / Agent Libraries /
                        ╲      Stage Gate Criteria / ROI / Value Tracking
                         ◆ ─── 
                        ╱   ◆ Layer 3: AI Information Architecture
                       ╱   ╱  Delivering AI Information Services
                 Planning↓   Components: Knowledge Mgmt (Wiki) / Prompt Library /
                 Alignment↑   Skill Definitions / Workflow Specs / Agent Specs /
                       ╲      Data Pipeline / Vector DB / Embedding /
                        ╲     Evaluation Suite / Reviewer Workflow / Audit Log
                         ◆ ─  
                        ╱   ◆ Layer 4: AI Technical Architecture
                       ╱    ╱  Delivering AI Infrastructure
                      ╱     Components: GPU / Inference Servers / LLM Router /
                            API Gateway / Identity SSO + RBAC / Monitoring /
                            Secret Vault / Storage / Networks / Backup HA /
                            Deployment (Cloud/Hybrid/On-Prem) / CI/CD
```

#### Cross-Layer Concerns (4 orbital components per layer)

Each diamond's 4 corners track: **Changes/Transformations / Costs-Benefits / Capacity-Capability / Projects-Programs** — every layer manages these.

| Concern | At Governance | At Business | At Information | At IT |
| --- | --- | --- | --- | --- |
| **Changes** | Company AI strategy pivot | Business model AI reorg | Skill/Workflow versioning | LLM vendor swap, on-prem migration |
| **Costs/Benefits** | Total AI investment ROI | Dept AI business value | Knowledge asset value | LLM token costs / GPU depreciation |
| **Capacity** | Strategic AI capability | Dept AI capability inventory | Knowledge mgmt capability | GPU/network bandwidth |
| **Projects** | AI Transformation Program | Dept PoC projects | Wiki rollout project | Inference server deployment |

#### Operational Flow (consultant practice)

```
Day 1 AM: Governance layer  ← CEO + Sponsor + Compliance
Day 1 PM: Business layer    ← COO + Dept heads + AI Champion
Day 2 AM: Information layer ← AI Champion + Knowledge head + IT Lead
Day 2 PM: IT Tech layer     ← CIO + IT Admin + Security
```

Each cell tagged 🟢 / 🟡 / 🔴 by client. Then run **Alignment ↑** reverse verification: from IT layer up, ask "can we really support the upper layer's needs?" Often discovers Governance ambitions hit IT reality.

#### Tool 2.5 / 2.6 / 2.7 Relationship — Full Closed-Loop

| Tool | Solves | Analogy |
| --- | --- | --- |
| **Tool 2.5** | **Meta layer**: is this RM well-designed? (10 conditions + DIY 7 steps) | "Building code" compliance |
| **Tool 2.6** | **Content layer (flat)**: what components? (5 questions + flat map) | House blueprint listing rooms |
| **Tool 2.7** | **Architecture layer (3D)**: why these layers? how connected? (4-layer + Planning↑↓) | Building master plan + floor relationships |

**Full sequence**: Tool 2.1 (pick RM) → Tool 2.5 (qualify) → **Tool 2.6 (flat components)** → **Tool 2.7 (4-layer architecture)** → Tool 2.2 (As-Is mapping) → Tool 2.3 (gap checklist) → Tool 2.4 (completeness radar).

---

### Tool 3.1 Industry Best-Practice Profile Template

| Field | Description |
| --- | --- |
| Industry | Industry |
| Company size | Headcount / revenue |
| Their L-level start | Starting L-level |
| Their L-level today | Current L-level |
| Time taken | Months |
| Excellence practices vs. Reference Model | Where in APQC / SCOR did they reach excellence? What concretely did they do? |
| Key wins | Three key outcomes |
| Key failures | Two failure lessons |
| Portability | What's transferable to this company? What isn't? |
| Sources | Public news / interviews / case studies |

### Tool 3.2 Excellence Capability Profile

Translate industry-leading patterns into **specific measurable excellence characteristics for this company**.

| Capability | Specific excellence characteristics (quantified) | Leading-case evidence | Distance from current state |
| --- | --- | --- | --- |
| Customer service response | 90% complaints AI-triaged in 1hr + human reply in 24hr; root cause auto-classified | Co. A (industry 1) | 5 days vs 1 day; no root-cause system |
| Quote turnaround | RFQ → quote ≤ 4hr; 80% AI draft + sales fine-tune | Co. B (industry 2) | 4 days vs 4hr |
| Knowledge sedimentation | ≥ 30 Skills added monthly; ≥ 1 contribution per employee per month | Co. C (industry 3) | 0 vs 30/month |
| ... | ... | ... | ... |

> **How to use**: each Reference Model Category should map to ≥ 1 "excellence characteristic". Stage 6 will decompose these into phased goals.

### Tool 3.3 Five Ready-to-Use Benchmark Stubs

#### Manufacturing — semiconductor packaging, 700 staff

- L1 → L3 in 9 months
- Maps to SCOR: Plan / Make / Deliver fully AI-enabled
- Wins: process anomaly summary Agent, SPC auto-analysis, complaint root-cause Agent Team
- Failures: skipped L1 whole-company early; relied on a single IT person; data permissions weren't laid down

#### Hospital — medical center, 1,200 staff

- L1 → L4 in 12 months
- Maps to APQC: 4.0 Deliver, 11.0 Knowledge
- Wins: patient onboarding RAG, HIS/EMR integration Agent, admin summaries
- Failures: ignored nursing front-line resistance early; backfilled L1 training

#### Retail — chain brand, 800 staff

- L1 → L4 in 14 months
- Maps to SCOR Deliver + APQC 3.0 Marketing
- Wins: product copy Skill Library, social-listening Workflow, new-product launch Agent Team
- Failures: no Reviewer early; AI copy misused brand language

#### Financial Services — regional bank, 2,500 staff

- L1 → L3 in 18 months
- Maps to APQC 4.0 + 13.0 Compliance
- Wins: KYC document summarization Workflow, customer service triage Agent
- Failures: compliance review slow; on-prem LLM performance lacking

#### Government — city government, 5,000 staff

- L1 → L2 in 24 months
- Maps to APQC 13.0 Governance + 11.0 Knowledge
- Wins: official document summarization, citizen FAQ
- Failures: procurement process drag; lacked AI Champion

### Tool 3.5 Cases-as-Benchmarks — Deliberately Writing Cases as Comparable Benchmarks

> **Core insight**: **Maturity ≡ Benchmarking**. Both fundamentally measure "current state's distance from a reference point." Maturity uses abstract L1-L5; benchmarking uses concrete peer cases.
>
> When a case is **deliberately written in structured benchmark format**, it is simultaneously "story" and "ruler" — client doesn't just see "what others did" but **immediately computes their own gap + estimates time to close**.

#### Case → Benchmark Conversion Rules

Narrative cases ("Company X did AI quality inspection successfully") give only inspiration, no comparability.

**Benchmark-grade cases** mandatorily have these 9 fields:

| # | Mandatory Field | Why it enables comparability |
| --- | --- | --- |
| 1 | **Industry + Size (headcount/revenue)** | Same industry + scale → comparable |
| 2 | **Start L-level + evidence** | Defined start → gap computable |
| 3 | **End L-level + evidence** | Defined end → target alignable |
| 4 | **Duration (months)** | Client estimates own timeline |
| 5 | **Key capability transitions (mapped to RM Category)** | Not "they're great" but "APQC 4.x rose from 1 to 3" |
| 6 | **Investment per phase (person-months + NT$)** | Client estimates own budget |
| 7 | **Key wins (3 quantified)** | "Complaint response 5 days → 1 day" not "satisfaction up" |
| 8 | **Key failures (2 mistakes)** | Failure lessons > success stories |
| 9 | **Applicability conditions (replicable by whom)** | Not all companies can replicate; preconditions must be stated |

> **Missing any field ≠ Benchmark**. Drop one and it degrades back to "story", uncomputable.

#### Benchmark-Grade Case Template (M Company, 700-staff packaging)

```
Industry / Scale:    Semiconductor packaging, 700 staff, NT$ 1.2B revenue
Start L-level:       L0 (no corp accounts) + APQC 11.x = 0
End L-level:         L3 + APQC 11.x = 3
Duration:            9 months (Phase 1 0-6m + Phase 2 6-9m)
RM Category transitions:
  ├ APQC 4.0 Deliver:    1 → 3 (complaint response 5 days → 1 day)
  ├ APQC 11.0 Knowledge: 0 → 3 (Wiki + Skill Lib live)
  ├ Tiger AI L1:         0 → 4 (whole-co OpenWebUI + 92% policy signed)
  └ Tiger AI L3:         0 → 2 (n8n Workflow 5 live)
Investment per phase:
  ├ Phase 1 (0-6m):      12 person-months + NT$ 2.8M
  └ Phase 2 (6-9m):       8 person-months + NT$ 1.8M

Key wins (quantified):
  1. Complaint response:  5 days → 1 day (-80%)
  2. Proposal turnaround: 4 days → 1 day (-75%)
  3. Defect rate:         3.2% → 2.4% (heading to 2.0% target)

Key failures (mistakes encountered):
  1. Ignored 50 senior line workers' resistance month 1 → factory-wide
     training boycott; resolved by reframing role as "AI Supervisor"
  2. n8n PoC without GitHub backup → host re-image wiped everything;
     added Workflow Git backup SOP afterward

Applicability:
  ✓ 300-1500 staff manufacturers
  ✓ Process data must stay on-prem (Hybrid suitable)
  ✓ Has IT Deputy who can double as AI Champion (0.5-1 FTE)
  ✓ Budget NT$ 4-8M acceptable
  ✗ Not applicable: < 100 staff (unprofitable scale)
  ✗ Not applicable: full-cloud-prohibition financials (must change to Variant A)
```

#### Client Self-Service: 30-Min Gap Calculation

Print the template; let client fill the "Our company" column:

| Field | M Co. (Benchmark) | Our company | Gap |
| --- | --- | --- | --- |
| Scale | 700 staff | 1,200 staff | Similar scale, comparable |
| Start APQC 11.0 | 0 | 0 | Same |
| End APQC 11.0 | 3 | Target 3 | Same |
| Duration | 9 months | Estimate 9-12 months | Slightly longer for larger scale |
| Budget | NT$ 4.6M | Estimate NT$ 7M | Slightly more for larger scale |
| Mistakes to avoid | Resistance / backup | Both must be avoided | — |

Client completes self-diagnosis in 30 min. **More persuasive than 3 weeks of consultant interviews** — not consultant says, peer case says.

#### Connection to Stage 1-8

```
Stage 1 As-Is         →  Client's own start L-level + RM Category scores
                                       ↓
Stage 3 Best Practice →  Benchmark case provides "end + duration + investment"
                                       ↓
Stage 4 Gap           →  Gap = (case end − client start), auto-quantified
                                       ↓
Stage 6 Phased Goals  →  Borrow case's Phase 1/2/3 distribution
                                       ↓
Stage 8 Risk Register →  Case's Key failures feed Risk Register
```

**Cases feed 4 stages simultaneously, not just Stage 3** — the methodological closed loop.

#### 5 Disciplines for Case → Benchmark

- [ ] **All 9 fields present** (missing one → return to author)
- [ ] **Quantified evidence**: "5 days → 1 day" ✓; "satisfaction up" ✗
- [ ] **Failures ≥ 2**: only-success cases not credible
- [ ] **Applicability explicit**: include "applicable" and "not applicable"
- [ ] **Anonymized but comparable**: codes (M/B/F/E/G) replace names; scale/industry/time data must be real

---

### Tool 3.6 Client Ideal Practice Co-Creation Workshop — Let Client Expand Their "Desired State" Themselves

> **Core logic**: Industry Best Practice = **input material** (Tool 3.1-3.5 all material); Client Ideal Practice = **target benchmark**. Stage 3's final output must be "client's **own selected and specified** Ideal Practice", not consultant prescription.
>
> **Why client must expand it themselves**:
> 1. **Client won't deny their own target** (consultant-set targets can be refuted)
> 2. **In Gap = (Ideal − As-Is), both numerator and denominator are client's words** (scientific argumentative power locked in)
> 3. **All Stage 4-8 reasoning becomes unshakable** (no one rejects targets they themselves chose)

#### Workshop Flow (half day, 3-4 hours)

**Participants**: CEO + Dept heads + AI Champion + IT Lead (≥ 5)
**Facilitator**: Consultant
**Prep**: Print Tool 3.1 Best-Practice Profiles (≥ 3); Tool 3.3 5 Benchmark Stubs; Tool 3.4 L1-L5 excellence
**Venue**: Whiteboard + sticky notes + Tool 2.7 4-layer architecture printed A2

#### Step 1: Material Display (30 min)

Consultant **shows only, does NOT recommend**:
- "Here are 3 industry-leading peer cases" → read Tool 3.1 profile
- "Here are 5 ready Benchmark Stubs" → read Tool 3.3
- "Here is what L1-L5 excellence looks like in practice" → read Tool 3.4
- "Here is the 4-layer architecture component map" → unfold Tool 2.7

> **Discipline**: consultant **forbidden from saying "I recommend..."** — only "industry does this..." / "we see this in the field..."

#### Step 2: Independent Voting (45 min)

Each participant **independently** writes sticky notes:
- "**What state do I want our company to reach in 12 months**"
- Mapped to cells in Tool 2.7 4-layer architecture
- Each: "**verb + quantified metric**" (e.g. complaint response 5 days → 1 day)

**Independent, no discussion**: avoids executive anchoring; lets dept heads' real opinions surface.

#### Step 3: Collective Consensus (60 min)

Post all sticky notes to the 4-layer architecture cells. Facilitator guides:
- Cells where many posted → **consensus targets** (direct to Ideal Practice)
- Cells with only 1-2 → **discuss whether to keep**
- Empty cells → **ask: is it unimportant or forgotten**

Form v1 Ideal Practice draft.

#### Step 4: Reality Check (45 min)

Consultant **first actively intervenes** using Tool 6.3 Organizational Absorption (6 dimensions):
- "Your budget cap NT$ 8M — can it support these targets?"
- "Your IT has 2 FTE — can ERP integration in Q2 work?"
- "Parent company audit in December — do you commit to Quick Win in 6 months?"

Let client **themselves** cut what's infeasible. Form v2 Ideal Practice.

#### Step 5: Ideal Practice Definition Table (30 min)

Fix v2 into this table (**this table = Stage 3 Output KPI, feeds Stage 4 Gap directly**):

| # | Capability | RM Category | Client Ideal Practice (quantified) | 12-month target L | Evidence criteria |
| --- | --- | --- | --- | --- | --- |
| 1 | Customer service | APQC 4.4 + Tiger AI L3 | 90% 1hr triage + 24hr human reply | L3 = 3 | n8n + Reviewer ≥ 95% |
| 2 | Knowledge sedimentation | APQC 11.x + Tiger AI L2 | ≥ 20 Skills/month | L2 = 3 | Skill Library Git + Owner + IPOE |
| 3 | Process root cause | SCOR Make + Tiger AI L4 | Anomaly → hypothesis ≤ 1hr | L4 = 2 | Hermes Agent + 5 tasks Reviewer pass |
| ... | ... | ... | ... | ... | ... |

**Each row is a client-signed commitment**. Stage 4 Gap directly subtracts using this table.

#### Step 6: Three-Party Signature (15 min)

CEO / Sponsor / AI Champion three-party sign the Ideal Practice Definition Table. **This signing is the engagement's turning point** — any later "we actually don't want this" must go back to revise this table; **cannot be denied out of thin air**.

#### Why This 6-Step Order Cannot Be Reversed

| Order | Why this | Reversing causes |
| --- | --- | --- |
| 1 Display → 2 Vote | See material first, then write; avoid daydream. Independent writing avoids exec anchoring | Discuss-then-vote → CEO sets tone |
| 2 Vote → 3 Consensus | Differences before consensus | Skip independent voting → false consensus |
| 3 Consensus → 4 Reality | Ideal first, ground later | Ground first → self-limiting |
| 4 Reality → 5 Define | Feasibility confirmed before commit | Direct table → skips feasibility |
| 5 Define → 6 Sign | Specific text before signing | Sign-without-text → empty commitment |

#### Tool 3.6 Lock-In with Stage 4-8

```
Tool 3.6 Client Ideal Practice Definition Table (signed)
        │
        ▼
Stage 4 Gap Analysis
  Gap = (Client Ideal − Client As-Is)  ← Both ends client-said, undeniable
        │
        ▼
Stage 5 Problem Definition
  80/20 convergence target = "client's own picked targets"  ← cannot say "not what we want"
        │
        ▼
Stage 6 Phased Goals
  Decompose client Ideal into Phase 1/2/3  ← cannot deny endpoint
        │
        ▼
Stage 8 Value Tracking Matrix
  Tracking targets = client's signed metrics  ← cannot deny measurement
```

> **This is the bottom-layer mechanism of "scientific argumentative power"**: all later reasoning starts at Y (Ideal) and ends at X (As-Is), both client-said. Consultant only computes Gap = Y − X and Roadmap decomposition. **The only way client can refute conclusions is to go back and modify their own signed Ideal Practice Definition Table** — a highly public, signed document.

#### Anti-Patterns (Consultant Mistakes to Avoid)

- ❌ Directly using Tool 3.4 L1-L5 excellence as client target: "We recommend L4 in 12 months" → client can refute "we're different"
- ❌ Using Tool 3.2 excellence characteristics as client Ideal without client participation
- ❌ Skipping Step 6 signature: unsigned Ideal can be modified anytime → reasoning chain collapses
- ✅ **Correct**: Use Tool 3.1-3.5 all as input, run 6-step workshop, get client-signed Ideal Practice

---

### Tool 3.4 What Excellence Looks Like at Each L-level

| Level | What it looks like in practice | Common client claim | Common misconception to clarify |
| --- | --- | --- | --- |
| L1 Controlled AI Access | Whole company has corp accounts, uses it, has rules | "We bought ChatGPT" | Buying ChatGPT ≠ everyone uses it ≠ governed |
| L2 Knowledge Codification | Skill Library + version control | "I have a Prompt library" | Prompt library ≠ reusable by others |
| L3 Workflow Automation | n8n PoC running + system-connected | "We have automation" | RPA / Zapier ≠ AI Workflow |
| L4 Autonomous Agent | Agent passes stage gates + has Wiki | "We're using Agents" | Demo Agent ≠ governed Agent |
| L5 Multi-Agent Organization | Multiple Agents complete cross-dept tasks | "We're building an AI team" | A bunch of chatbots ≠ Agent Team |

---

## Stage 4: Gap Analysis

> **Purpose**: Structurally compare "Stage 1 current state" against "Stage 2 standard + Stage 3 excellence"; classify into Missing / Broken / Redundant.
>
> **Output KPI**: Gap Matrix (Impact × Effort).
>
> ⚠️ **Core discipline**: Gap Analysis is "objective gap inventory", **NOT a risk assessment**. Risk belongs to Stage 8's Risk Register. Gap Analysis only answers "what's missing, by how much, what's the impact"; **it does NOT answer "what bad things will happen if we don't act"**. Mixing the two turns Stage 4 into subjective judgment.

### Tool 4.1 Missing / Broken / Redundant Table

| Area | Type (M/B/R) | Description | Mapped to Reference Model | Mapped to excellence characteristic | Severity 1-5 | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| Customer email triage | **Missing** | No AI triage at all | APQC 4.4 customer service | Excellence = 1hr triage | 4 | CS Lead |
| Quote system | **Broken** | Sales manually copy-paste | SCOR Source + Deliver | Excellence = 4hr quote | 5 | IT Deputy |
| Ticket system | **Redundant** | Notion + Trello + Email, three stacks | APQC 8.x | (no excellence mapping) | 3 | COO |
| Knowledge mgmt | **Missing** | No Wiki, no SOP | APQC 11.x | Excellence = 30/month added | 5 | HR + AI Champion |
| ... | ... | ... | ... | ... | ... | ... |

#### M / B / R Definitions

- **Missing**: should exist but doesn't (the empty cells found via the Stage 2 standard framework)
- **Broken**: exists but malfunctions (manual workaround, errors, slow, unauditable)
- **Redundant**: duplicate, surplus, low-value (multiple systems doing the same thing, manual data shuffling)

### Tool 4.2 Impact × Effort Matrix

```
            Low Effort                   High Effort
           ┌──────────────────────┬──────────────────────┐
High       │  ★ Quick Wins        │  Big Bets            │
Impact     │  - Gmail triage       │  - ERP Agent          │
           │  - Sheet auto-score   │  - Cross-dept Team    │
           ├──────────────────────┼──────────────────────┤
Low        │  Fill-ins            │  ✗ Avoid              │
Impact     │  - Internal FAQ       │  - Heavy custom bot   │
           │  - Slide template     │                       │
           └──────────────────────┴──────────────────────┘
```

**Placement rules**:

- Impact: direct NT$ impact × beneficiaries × strategic importance, score 1-5
- Effort: person-days × system-integration difficulty (**not risk — risk belongs to Stage 8**), score 1-5
- ≥3 = High

### Tool 4.3 Prioritization Worksheet

| Candidate | Impact (1-5) | Effort (1-5) | Strategic Fit (1-5) | Score = (I × SF) / E | Rank |
| --- | ---: | ---: | ---: | ---: | ---: |
| Customer email triage PoC | 4 | 1 | 5 | 20 | 1 |
| Sales proposal Skill | 4 | 2 | 4 | 8 | 4 |
| ERP Agent | 5 | 5 | 5 | 5 | 5 |
| Sheet auto-scoring | 3 | 1 | 3 | 9 | 3 |
| Cross-dept Team | 5 | 4 | 5 | 6.25 | (Big bet, later) |

> **Output**: Gap matrix + priority ranking. **Hand all of it to Stage 5 for 80/20 convergence into the core problem.**

---

## Stage 5: Problem Definition

> **Purpose**: Apply 80/20 to converge issues; lock onto the high-leverage core lesion; distinguish symptoms from root causes.
>
> **Output KPI**: Executive Problem Statement.

### Tool 5.1 80/20 Convergence Worksheet

From the pile of Stage 4 gaps, find the core lesion where "fixing 20% of the gaps resolves 80% of the pain".

```
Step 1: List all Stage 4 gaps (mix M/B/R)
Step 2: For each gap, mark "# processes affected", "# departments affected", "# KPIs affected"
Step 3: Find the 3-5 gaps with the largest impact surface → core-lesion candidates
Step 4: For each candidate, ask "why" 5 levels deep → find root cause
Step 5: If 1-2 root causes are repeatedly cited → that is the core problem
```

#### Example (Manufacturing)

```
High-impact gaps:
A. Slow customer service → 3 processes, 4 depts, customer-satisfaction KPI
B. Slow quotes           → 5 processes, 3 depts, revenue KPI
C. No knowledge sediment → all depts, onboarding KPI
D. Slow process anomaly  → 2 processes, 1 dept, defect-rate KPI

5 Whys (C: no knowledge sediment):
  Why? → No one writes
  Why no one writes? → No one uses what's written
  Why not used? → Scattered, can't find
  Why can't find? → No central Wiki
  Why no central Wiki? → **No owner + no tool + no incentive** ← root cause

Core problem (candidate):
The company lacks the role, tool, and incentive for "knowledge as an asset" —
80% of gaps (A/B/C/D) all stem from "doing the same thing repeatedly,
no one sediments, no one reuses".
```

### Tool 5.2 Problem Statement Worksheet (5 sections)

```
1. CONTEXT
   What happened in the past 12 months that made AI a priority?

2. TENSION
   What is the gap between current "reality" and "expectation"? Quantify (cite Stage 3 excellence characteristics).

3. COST OF INACTION
   What happens in 12 months if we don't act? In NT$?

4. DESIRED FUTURE
   What does success look like in 12 months? Three quantifiable metrics (aligned with Stage 3 excellence).

5. CONSTRAINTS
   Budget? Headcount? Compliance? Schedule? Which options are already ruled out?
```

### Tool 5.3 Common Pitfalls Checklist (10 anti-patterns)

- [ ] Framing AI as a tech issue (should be a business issue)
- [ ] No quantification of "cost of inaction"
- [ ] Treating "deploying AI" as the goal (should be a business KPI)
- [ ] Marking all departments as high-priority (no focus)
- [ ] Only discussing opportunities, avoiding risks
- [ ] Using "security" as a shield to block any attempt
- [ ] Framing governance as an IT issue (should be company-wide)
- [ ] Expectation timeline too short / too long
- [ ] No sponsor / no champion
- [ ] No failure-exit mechanism

### Tool 5.4 Sample Complete Problem Statement (Manufacturing)

```
CONTEXT:
In the past 12 months, three direct competitors deployed AI quality inspection and
complaint Agents. Customers began questioning our slower lead time and complaint
response. Customer A's quarterly orders dropped 18%.

TENSION:
Defect rate 3.2% (industry-leading 1.8%); complaint response 5 days (industry 2 days);
sales proposal turnaround 4 days (industry 1.5 days).

COST OF INACTION:
Without significant improvement in 12 months, expect to lose customers A, B, C —
annual revenue impact ~NT$ 180M. Recruiting 8 QC + sales staff costs ~NT$ 12M.

DESIRED FUTURE:
12 months out: defect rate 2.0%; complaint response ≤ 1 day; sales proposal ≤ 1 day.
Build 1 process-improvement Agent Team and 1 sales Skill Library.

CONSTRAINTS:
- Budget cap NT$ 8M (training + platform + consulting)
- Process data must stay on-prem (no cloud)
- IT capacity 2 FTE, no growth
- Parent-company audit in December — first Quick Win must show within 6 months
```

---

## Stage 6: Benchmarking & Phased Goals

> **Purpose**: Decompose Stage 3's "ultimate benchmark" into multiple "**organizationally absorbable**" phased goals (e.g. Foundation, Optimization, Excellence) and define each phase's acceptance criteria (Stage Gate Criteria).
>
> **Output KPI**: Phased goal definitions and Stage Gate Criteria.
>
> **Core thinking**: Pursuing the ultimate benchmark in one shot = failure. Organizations have an "absorption ceiling" — culture, headcount, IT, budget can't swallow large jumps. Stage 6's job is to break excellence into 3-4 small, digestible steps.

### Tool 6.1 Ultimate Benchmark → Phased Goals Decomposition

| Capability | Ultimate benchmark (Stage 3 excellence) | Phase 1: Foundation (0-6m) | Phase 2: Optimization (6-12m) | Phase 3: Excellence (12-24m) |
| --- | --- | --- | --- | --- |
| Customer service | 90% triaged in 1hr + 24hr response | Whole-company Chat AI + prompt templates | n8n auto-triage + Reviewer | Hermes Agent auto-draft + root cause |
| Quote turnaround | RFQ → quote ≤ 4hr | Sales Skill writes proposals | n8n quote-draft Workflow | Agent reads ERP + drafts quote |
| Knowledge sedimentation | 30 Skills added monthly | 5 core Skills + Owner | 15 Skills + cross-dept reuse | 30 Skills + Wiki auto-citation |
| Whole-company AI governance | Full Audit + ROI dashboard | Policy + Admin Panel | Dept Skill governance | Whole-company governance dashboard |

> **How to use**: every Stage 3 "excellence characteristic" must map to a Phase 1→2→3 path. Any plan that skips from Phase 1 to Phase 3 is a red flag for organizational absorption.

### Tool 6.2 Stage Gate Criteria

#### Phase 1 Acceptance (Foundation)

- [ ] **L1 Gate**: OpenWebUI accounts opened for the whole company
- [ ] AI usage policy signed by > 90%
- [ ] Prompt Library ≥ 30 entries
- [ ] Admin Panel permission matrix configured
- [ ] 5 core Skills published (with Owner, version, IPOE)
- [ ] L2 Skill candidate list ≥ 5
- [ ] **HITL design confirmed**: every external output (customer, compliance) has a human-review node

#### Phase 2 Acceptance (Optimization)

- [ ] **L2 Gate**: Skill Library ≥ 15 Skills published
- [ ] Every Skill has Owner, version, IPOE doc
- [ ] Antigravity / Claude Code artifacts submitted
- [ ] **L3 Gate**: n8n Workflow PoC ≥ 3 in production
- [ ] Sub-workflow Library structure complete
- [ ] Data Tables Schema confirmed
- [ ] GitHub Backup SOP executed
- [ ] L4 Workflow Contract and Hermes interface spec

#### Phase 3 Acceptance (Excellence)

- [ ] **L4 Gate**: Hermes Agent passes sub-acceptances 4A-4E
- [ ] Wiki ingest/query/update all running
- [ ] briefing template + actual brief case
- [ ] Evidence trail: input → process → output → log
- [ ] **L5 Gate**: ClawTeam Role Cards complete
- [ ] Task allocation table with dependency chain
- [ ] 1 successful cross-dept Agent Team rehearsal
- [ ] Reviewer + HITL design
- [ ] ROI tracking matrix activated

### Tool 6.3 Organizational Absorption Capacity Assessment

Avoid setting "indigestible" phased goals. Assess these 6 dimensions before launching each phase:

| Dimension | Phase 1 needs | Phase 2 needs | Phase 3 needs | Current state |
| --- | --- | --- | --- | --- |
| **Budget** (annual) | NT$ 0.5-1.5M | NT$ 1.5-4M | NT$ 4M+ | `[fill]` |
| **AI Champion** | 1 (part-time) | 1 (full-time) + dept leads | 2-3 dedicated team | `[fill]` |
| **IT FTE** | 0.2 | 0.5-1 | 1-2 | `[fill]` |
| **Data permission governance** | Policy + Admin | Dept permission matrix | Whole-company Audit Log | `[fill]` |
| **Staff AI literacy** | 70% can use Chat | 30% can write Skills | 10% can design Workflows | `[fill]` |
| **Change capacity** (parallel projects) | 1-2 | 2-3 | 3-5 | `[fill]` |

> **Insufficient absorption → extend phase timeline or shrink phase goals**. Don't push.

---

## Stage 7: To-Be Design

> **Purpose**: Design a concrete, deployable "**multi-phase evolution blueprint**" and "**human-AI collaboration architecture**", not just a tech architecture diagram. Each phase has its own To-Be Operating Model.
>
> **Output KPI**: Phased To-Be Operating Model, Future Process Maps.

### Tool 7.1 Phased To-Be Operating Model

Draw one To-Be Operating Model per phase. Includes:

```
Phase 1 To-Be Operating Model (Foundation)
==========================================
[Individual layer] Whole-company OpenWebUI accounts → policy, Admin Panel
[Department layer] Each dept produces 5 core Prompts / Skills
[Process layer]    Not yet automated (manual + AI assistance)
[System layer]     Gmail / Sheets / Notion connected
[Governance layer] AI policy + permission matrix + monthly review
[Human-AI split]   100% human-driven, AI as personal assistant

Phase 2 To-Be Operating Model (Optimization)
============================================
[Department layer] Skill Library 15+ entries
[Process layer]    3-5 high-value Workflows automated (n8n)
[System layer]     Gmail/Sheets/CRM/ERP bidirectional
[Governance layer] Dept Owner + Workflow uptime monitoring
[Human-AI split]   70% human-driven + 30% Workflow auto + HITL review

Phase 3 To-Be Operating Model (Excellence)
==========================================
[Org layer]        1-2 Hermes Agents + 1 ClawTeam
[Governance layer] Whole-company Audit Log + ROI dashboard
[Human-AI split]   50% human-driven + 30% Workflow + 20% Agent autonomous (with HITL)
```

### Tool 7.2 Human-AI Collaboration Architecture

For each key process, define what humans do, what AI does, and where HITL sits.

| Process | Human role | AI role | HITL node | Acceptance criteria |
| --- | --- | --- | --- | --- |
| Customer service reply | Review draft + proactive care | Triage, prioritize, draft | 100% human review before send | Send-without-edit rate ≥ 60% |
| Sales proposal | Customer relationship, pricing, decision | Draft content, search history | 100% human review before submit | Proposal turnaround ≤ 1 day |
| Month-end anomalies | Judgment, action | Find anomalies, summarize | 100% human review before action | Anomaly discovery ≤ 1 day |
| Process root cause | Cross-dept coordination, decision | Organize data, hypothesize | 100% human review before action | Root-cause report ≤ 2 days |

### Tool 7.3 Skill Map Template

| Skill | Owner | Inputs | Outputs | Tools used | L-level | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Customer proposal draft | Sales Lead | Customer data + past proposals | Word proposal | Antigravity + Claude | L2 | Live |
| Complaint triage | CS Lead | Gmail messages | Category + priority | n8n + Claude | L3 | PoC |
| Month-end anomaly summary | Finance | SAP reports | Anomaly table + actions | n8n + GPT-4 | L3 | Build |
| ... | ... | ... | ... | ... | ... | ... |

### Tool 7.4 Workflow Map Template

| Workflow | Trigger | Steps (n8n) | Systems | Skills called | Output | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| Customer email triage | Webhook (Gmail) | Webhook → Set → OpenAI Chat → Switch → Gmail Label | Gmail | "Complaint triage" | Label + notify | CS Lead |
| Customer monthly report | Schedule (1st of month) | Schedule → SAP API → Sheet → Claude → Email | SAP, Sheets, Gmail | "Month-end summary" | PDF + Email | Finance |
| ... | ... | ... | ... | ... | ... | ... |

### Tool 7.5 Agent Map Template

| Agent | Role | Skills used | Workflows used | Wiki | Reviewer | Stage acceptance |
| --- | --- | --- | --- | --- | --- | --- |
| Customer-service Triage Agent | Triage + draft | Complaint triage, draft generation | Email triage | FAQ + past cases | CS Manager | L4 ✓ |
| Sales Briefing Agent | Pre-visit briefing | Customer research, opportunity summary | CRM summary | Customer history | Sales Lead | L4 ✓ |
| ... | ... | ... | ... | ... | ... | ... |

### Tool 7.6 Integration Architecture (3 variants)

#### Variant A: Cloud-first

```
[OpenWebUI Cloud] → [n8n Cloud] → [Hermes Cloud Agent] → [SaaS APIs]
                                       ↓
                                 [Notion / Sheets / Gmail]
LLM: OpenAI / Claude / Gemini API
Use case: low sensitivity, fast PoC, limited budget
```

#### Variant B: Hybrid

```
[OpenWebUI On-Prem] → [n8n Self-host] → [Hermes Local Agent]
                            ↓                  ↓
                      [SaaS APIs]      [Local SQL / ERP]
LLM routing: low sensitivity → cloud; sensitive → on-prem Llama
Use case: financial, healthcare, manufacturing sensitive data
```

#### Variant C: Full On-Prem

```
[OpenWebUI Local] → [n8n Local] → [Hermes Agent Local]
                       ↓                ↓
                 [Local APIs only]  [Local Llama 70B + Embedding]
No cloud LLM calls
Use case: government, defense, top-tier financial
```

---

## Stage 8: Implementation & Change

> **Purpose**: Adopt a "**phase-first, gradual rollout**" strategy; every phase acceptance reverts to checking against the Reference Model (Stage 2). Beyond executing the Roadmap, change management, risk governance, and value tracking must all land.
>
> **Output KPI**: Transformation Roadmap, Change Management Plan, Value Tracking Matrix.
>
> **Core thinking**: The first 7 stages are "design"; Stage 8 is where success or failure actually happens — change management (people), governance (rules), tracking (data) must all land.

### Tool 8.1 Transformation Roadmap

| Quarter | Phase | Theme | Deliverables | Owner | Stage acceptance (Stage 6) | KPI |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | Phase 1 | Diagnose + L1 launch | Whole-company OpenWebUI, AI policy, Prompt Library | IT + AI Champion | L1 Gate | 80% staff weekly use |
| Q2 | Phase 1→2 | L2 + L3 PoC | 5 Skills, 3 n8n Workflow PoCs | AI Champion + depts | L2 + L3 Gate | Skills ≥3, Workflow uptime 95% |
| Q3 | Phase 2 | L4 Pilot | 1 Hermes Agent | AI Champion + IT | L4 Gate | Agent completes 5 tasks, Reviewer pass |
| Q4 | Phase 2→3 | L4 Scale | 3 Agents, cross-dept integration | Dept Leads | L4 ext. | Monthly time saved ≥ 200 hr |
| Q5-Q6 | Phase 3 | L5 Pilot | 1 ClawTeam | Sponsor + AI Champion | L5 Gate | Team completes ≥ 1 cross-dept task |

> **Mandatory at every quarter end**: revisit the Stage 2 Reference Model completeness radar — is it rounder? Which Categories remain empty? This decides whether the next quarter advances or backfills.

### Tool 8.2 Change Management Plan

| Dimension | Phase 1 (Foundation) | Phase 2 (Optimization) | Phase 3 (Excellence) |
| --- | --- | --- | --- |
| **Stakeholder Map** | Sponsor, AI Champion, IT, HR | + Dept Leads | + Whole company |
| **Communication plan** | Monthly meeting + monthly report + Wiki | Bi-weekly stand-ups + dept reports | Quarterly all-hands + quarterly report |
| **Training plan** | L1 whole-company 4hr + L2 dept reps 8hr | L2 whole dept + L3 IT/Champion | L4-L5 advanced training |
| **Resistance handling** | Lead by example + recognize early adopters | Embed in performance KPIs | Cultural internalization + talent promotion |
| **Early adopters** | 5-10 (cross-dept) | Whole dept | Whole company |
| **Milestone celebrations** | L1 Gate Party | First Workflow live | First Agent acceptance |

#### Resistance-Handling Playbook (by resistance type)

| Resistance type | Typical signal | Handling |
| --- | --- | --- |
| **Fear of replacement** | "AI will take my job" | 1:1 conversations + redefine role (upgrade to AI supervisor) |
| **Can't use it** | "I can't learn this" | 1:1 mentor + simplify first success experience |
| **Distrust** | "AI makes mistakes" | Start with "human-review" scenarios + accumulate trust |
| **Fear of accountability** | "Who's responsible if it goes wrong?" | Clear HITL nodes + accountability boundary doc |
| **Vested-interest loss** | "This affects my dept's control" | Sponsor intervenes + reallocate KPIs |

### Tool 8.3 RACI / Stakeholder Alignment Matrix

| Topic | Sponsor | AI Champion | IT | Front-line user | Data Owner |
| --- | --- | --- | --- | --- | --- |
| Vision and Roadmap | A | R | C | I | I |
| Reference Model selection | A | R | C | I | C |
| Tool selection | A | C | R | C | C |
| Accounts / permissions | I | C | R | I | A |
| Skill / Workflow build | I | A | R | R | C |
| Change management | A | R | C | C | I |
| Audit / governance | A | C | R | I | R |
| Value tracking / ROI | A | R | C | I | I |

(R=Responsible, A=Accountable, C=Consulted, I=Informed)

### Tool 8.4 Permission / Governance Matrix

| Role | Resource | Read | Write | Approve | Audit |
| --- | --- | --- | --- | --- | --- |
| All staff | OpenWebUI personal area | ✓ | ✓ | ✗ | self |
| Dept Lead | Dept Skill Library | ✓ | ✓ | ✓ | dept |
| AI Champion | Whole-company Workflow | ✓ | ✓ | ✓ (≤ L3 phase) | all |
| IT Admin | All + models + Audit Log | ✓ | ✓ | ✓ (L4-L5 phase) | all |
| Sponsor / CIO | Whole-company read + Approve | ✓ | ✗ | ✓ (L5 phase) | all |
| Compliance / Internal Audit | Audit Log only | ✓ | ✗ | ✗ | all |

### Tool 8.5 Value Tracking Matrix

> Replaces the older "ROI Tracking" single-perspective view. Value is not only money — it includes time, risk, knowledge assets, employee experience.

| Initiative | Dimension | Baseline | Target | Actual | Period | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Customer email triage | Time | 5 days | 1 day | 1.2 day | M3 | CS Lead | 🟡 95% |
| Customer email triage | Risk | Missed 5%/mo | 1%/mo | 1.5%/mo | M3 | CS Lead | 🟡 |
| Sales proposal | Time | 4 days | 1 day | 0.8 day | M4 | Sales Lead | 🟢 |
| Sales proposal | Employee experience | Satisfaction 6/10 | 8/10 | 8.5/10 | M4 | Sales Lead | 🟢 |
| Month-end anomaly summary | Time | 3 days | 0.5 day | 0.6 day | M5 | Finance | 🟢 |
| Hermes Agent tasks | Scale | n/a | 50/month | 38 | M6 | AI Champion | 🟡 |
| Knowledge assets | Accumulation | 0 | 30 entries | 22 entries | M6 | AI Champion | 🟡 |
| ClawTeam cross-dept | Scale | n/a | 1/quarter | 0 | M9 | Sponsor | 🔴 (delay) |

#### Five Tracking Dimensions

1. **Time** — processing time reduction
2. **Quality** — error rate down, rework reduction
3. **Scale** — beneficiaries, throughput
4. **Risk** — missed cases, compliance violations, sensitive-data leakage
5. **Assets** — Skill count, Wiki entries, Agent count

### Tool 8.6 Risk Register

> Moved from the original Stage 6 to Stage 8 — risk belongs to Implementation (what could go wrong during execution), not Gap Analysis (what's missing now).

| Risk | Likelihood | Impact | Mitigation | Owner | Trigger |
| --- | --- | --- | --- | --- | --- |
| Employee resistance | High | High | Change-mgmt Playbook + L1 whole-company experience | HR + Sponsor | adoption < 50% in 30d |
| Sensitive-data leakage | Medium | Critical | redact policy + audit log + Hybrid deployment | CIO | DLP alert |
| LLM hallucination causing wrong decisions | High | Medium | Reviewer / HITL + evidence | AI Champion | any decision overturned |
| Budget overrun | Medium | Medium | Monthly KPI / value-tracking review | CFO | monthly spend > 110% budget |
| AI vendor outage / price hike | Medium | High | Multi-vendor LLM routing + on-prem fallback | IT Admin | vendor outage > 4hr |
| Phase goals indigestible | Medium | High | Stage 6 absorption assessment + extend timeline | Sponsor | phase acceptance delay > 30d |
| ... | ... | ... | ... | ... | ... |

### Tool 8.7 Audit Log Requirements

| Event Type | Captured by | Retention | Reviewer |
| --- | --- | --- | --- |
| LLM call (prompt + response) | n8n / OpenWebUI | 90 days hot, 1 year cold | AI Champion |
| Permission change | OpenWebUI Admin | 3 years | IT Admin + Compliance |
| Skill / Workflow deploy | GitHub | Permanent | AI Champion |
| Agent task start/end | Hermes log | 1 year | AI Champion |
| Reviewer sign-off | In-system | Permanent | Compliance |
| Phase acceptance pass | Consultant + client | Permanent | Sponsor + Consultant |
| Sensitive-data redaction trigger | DLP | 1 year | Security + Compliance |

### Tool 8.8 AI Ethics & Data Policy Checklist (15 items)

- [ ] Employee AI usage policy documented and signed
- [ ] Customer data / PII not sent to LLM (or redacted)
- [ ] Model vendor data-retention policy reviewed
- [ ] Audit Log covers all LLM calls
- [ ] Employees have the right to know which work is AI-processed
- [ ] AI decisions have HITL (for material matters)
- [ ] AI-generated content explicitly marked "AI-generated"
- [ ] IP ownership clarified (employee / company / AI vendor)
- [ ] Bias / discrimination risk assessed (HR / customer-decision scenarios)
- [ ] High-sensitivity scenarios (minors / healthcare / legal) have additional rules
- [ ] LLM hallucination handling SOP (who reviews)
- [ ] AI system incident response process
- [ ] Third-party AI tool whitelist / blacklist
- [ ] Annual employee training (≥ 1 / year)
- [ ] Government regulation tracking (EU AI Act, Taiwan AI Basic Act, PIPA) by Compliance

---

## Closing: How to Use This Toolkit

### 6-Week Standard Engagement

| Week | Stage | Main tools | Client role | Consultant deliverable |
| --- | --- | --- | --- | --- |
| W1 | Stage 1 | 1.1 Interviews / 1.2 1.3 inventories / 1.4 As-Is Map | Exec interviews, IT inventories | Discovery Report + As-Is Maps |
| W2 | Stage 2+3 | 2.1-2.4 Reference Model / 3.1-3.4 Best Practice | IT + dept walkthrough | Standard gap checklist + excellence profile |
| W3 | Stage 4+5 | 4.1-4.3 / 5.1-5.4 | Exec review + 80/20 workshop | Gap Matrix + Problem Statement |
| W4 | Stage 6 | 6.1-6.3 Phase decomposition + absorption | Exec + AI Champion + HR | Phased Goals + Stage Gate Criteria |
| W5 | Stage 7 | 7.1-7.6 To-Be Design | AI Champion + IT | Phased To-Be Operating Model |
| W6 | Stage 8 + closeout | 8.1-8.8 | Sponsor + Compliance + HR | Roadmap + Change Plan + Value Tracking + Final Report |

### Weekly delivery rhythm

- Mon: previous week tool review + this week plan
- Wed: client interviews / workshops
- Fri: deliverable draft + client review

### Consultant onboarding (for new consultants)

1. Read README + AI_TRANSFORMATION_STORY_AND_STRUCTURE
2. Read [`CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](CONSULTING_FRAMEWORKS_LIBRARY_EN.md) to understand the schools behind the eight stages
3. Run all samples in this toolkit once
4. Shadow 1 Stage 1 interview, 1 Stage 5 workshop
5. Run 1 Stage 4 Impact × Effort + 1 Stage 6 phase decomposition yourself
6. Pass Tiger AI internal mock review

---

License & Citation

This toolkit is Apache License 2.0; consultants, in-house teams, and derivative methodologies may use, modify, and commercialize, provided the [`NOTICE`](../NOTICE) attribution is preserved.
