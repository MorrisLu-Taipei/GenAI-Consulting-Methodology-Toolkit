# Executive Summary: The Whole Methodology in 5 Minutes (10 Minutes for the Full Picture)

> 🌐 中文版本 / Chinese version: [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)
>
> **5-minute version**: read §1 "On One Page" + §2 "Core Model" — that's enough.
> **10-minute version**: add §3-§7 (living book, theory, courses, consulting, deliverables, co-reading, next steps).
> Click into the linked files only when you want to go deeper.

---

## 1. On One Page: What It Solves

Many enterprises adopt AI by "**jumping straight to tools**" — buy ChatGPT, try n8n, want to build Agents. The result: employees can't use it, processes aren't connected, data isn't governed, PoCs can't be accepted, and leadership has no idea how mature the company's AI actually is.

This methodology turns "**scattered AI usage**" into a "**reproducible, governable, measurable, scalable organizational capability**" — using a closed loop of **questionnaire + courses + consulting** to walk a company from **individuals using AI** all the way to **the enterprise owning an AI team**.

| Element | One sentence |
|---|---|
| **Diagnostic tool** | 10 / 25 / 50-item questionnaire → objective L1-L5 position + six-dimension gaps |
| **Education path** | 5-level courses (OpenWebUI / Antigravity / n8n / Hermes / ClawTeam) + BARS scoring calibration |
| **Consulting structure** | 8 stages (Awareness → Acceptance Test) + 3-phase contract (A Diagnosis / B Strategy / C Implementation) |
| **Academic foundation** | 7 theoretical pillars (Rosemann / Cohen & Levinthal / Teece / Real Options / etc.) |
| **Carrying medium** | **AI-Native Living Book** — a methodology that is truly *alive*, co-readable directly with an AI IDE |

---

## 2. Core Model: The Two Axes of L1-L5

L1-L5 is not "five tools" — it is a maturity path connecting **two axes**:

| Axis | Range | Driver | Layers | Tools |
|---|---|---|---|---|
| **Scale axis** | L1 → L2 → L3 | **Humans** use AI, **humans** supervise AI | individual → department → cross-department / company-wide | OpenWebUI / Antigravity / n8n |
| **AI-autonomy axis** | L4 → L5 | **AI** runs autonomously; humans step back to **governor** | AI entity → AI team | Hermes Agent / ClawTeam |

**Key boundary = L3 → L4**: crossing from "humans drive the work" to "AI drives the work." Even at L4-L5, **the governance framework is still built by humans, and humans retain oversight** — what AI is autonomous in is "operational execution," not "governance decisions."

➜ Full story: [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0

---

## 3. AI-Native Living Book — Why This Book Is *Alive*

This methodology is not a PDF / PPT / SOP — **it's a book that is truly *alive***:

| Generation | Form | Limitation |
|---|---|---|
| Gen 1 — Printed books | Paper | **Static** — can only be read, doesn't respond |
| Gen 2 — Interactive books | Web / Wiki | **Interface alive, content not** — still doesn't proactively suggest |
| **Gen 3 — AI-Native Books** (this repo) | Markdown + AI IDE | **Truly alive** — lets you ask, answers for you, thinks with you, and runs diagnostics / drafts reports / runs simulations based on your company's situation |

**Operation model**: `git clone` → open with an AI IDE (Antigravity / Claude Code / Codex) → AI auto-reads the entire book → positions itself as the **co-reading tutor** for this methodology → you converse, ask, and apply directly.

➜ Full discussion: [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md)

### Three AI Engines, Each Specializing in Different Things

| Engine | Role | What it's best at | Workflows |
|---|---|---|---|
| 🟦 **Antigravity** | Front-line consultant | Talking with clients, running questionnaires, drafting reports | `/diagnose`, `/generate-report` |
| 🟪 **Codex CLI** | Methodology auditor | Cross-file testing, red-team review, version control, repair | `/evidence-audit`, `/red-team-review`, `/bump-version` and 7 more |
| 🟨 **Claude Code** | Cross-file thinking partner | Deep synthesis, multi-perspective debate, simulation, client forks | `/simulate-engagement`, `/devil-pair-debate`, `/methodology-fork` and 7 more |

➜ Three-engine self-disclosure: [`../07_AI_Contributions/`](../07_AI_Contributions/) ｜ Setup guide: root [`../README_EN.md`](../README_EN.md) §🚀

---

## 4. Academic Foundation: 7 Theoretical Pillars

This methodology isn't ad-hoc. Every key design **maps to a classic theory** — the standard answer when academia, regulators, or boards ask "what's the theoretical basis":

| # | Theory | Founder | Role in this methodology |
|---|---|---|---|
| 1 | **Capability Maturity** | Rosemann (QUT) / CMMI | The school-of-thought foundation for L1-L5 maturity |
| 2 | **Absorptive Capacity** | Cohen & Levinthal (1990) | Explains why some companies stay stuck at L1 — they lack prior knowledge |
| 3 | **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | Stage 7 To-Be design: which tasks should reach L4, which should stop at L2 |
| 4 | **Dynamic Capabilities** | Teece (1997, 2007) | sense / seize / transform — why AI governance is a "capability," not a "policy" |
| 5 | **Sociotechnical Systems & Trust in AI** | Bostrom (1977) / Dietvorst (2015) / Glikson (2020) | Why L4-L5 must keep HITL — humans don't blindly trust pure-autonomous AI |
| 6 | **Real Options Theory** | Dixit & Pindyck (1994) / McGrath (1997) | Why Phase 1 with NPV ≈ 0 is still worth investing in — you're buying the option to expand |
| 7 | **Executable Knowledge Artifact** | Knuth (1984) Literate Programming + modern extensions | Why this methodology is Markdown + AI-IDE co-read instead of PDF |

➜ Full theoretical discussion (with citations): [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md)
➜ Failure patterns (where theory predicts failure): [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md)
➜ Pilot Study design (18-24 month empirical plan): [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md)

---

## 5. Education: The Complete L1-L5 Course Curriculum

Every level has its **own course material + verifiable deliverables + Stage Gate acceptance**:

| Level | Name | Tool | Course Plan |
|---|---|---|---|
| L1 | Controlled AI Access | OpenWebUI | [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) |
| L3 | Workflow Automation | n8n + Tiger AI Skill Pack | [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) |
| L4 | Autonomous Agent | Hermes Agent + Wiki | [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) |
| L5 | Multi-Agent Organization | ClawTeam | (L5 included in [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)) |

**Design principle**: clients don't have to do all of L1-L5 in one go. Use the questionnaire to find **the layer that produces the most immediate deliverables**, then layer up. The course mix is determined by company profile, industry, deployment mode (cloud / hybrid / on-prem), and risk requirements.

➜ Complete course package: [`../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
➜ Scoring calibration (avoid subjectivity): [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) BARS

---

## 6. Consulting: 8 Stages + 3-Phase Contract Model

### 6.1 The Eight Stages

| # | Stage | Main action |
|---|---|---|
| 1 | **Awareness** | Establish AI awareness and the client's vision |
| 2 | **Reference Model** | Guide the client to sign the Ideal Practice radar |
| 3 | **Discovery** | Collect As-Is current state, shadow IT, system inventory |
| 4 | **Gap Analysis** | Compare Ideal Practice vs As-Is; identify high-impact gaps |
| 5 | **Stakeholder Mapping** | Identify Sponsor, AI Champion, HR, Compliance |
| 6 | **Diagnosis** | Cross-layer analysis (incl. anchoring to the 7 theoretical pillars) |
| 7 | **To-Be Design** | Use TTF / Real Options to design a stepped Roadmap |
| 8 | **Acceptance Test** | Stage Gate sign-off + quarterly radar review |

### 6.2 Three-Phase Contract

| Phase | Duration | Main deliverable |
|---|---|---|
| **Phase A — Diagnosis** | 2 weeks | Mid-term diagnostic report + signed Ideal Practice |
| **Phase B — Strategy** | 4 weeks | Full 14-chapter consulting report + 24-month Roadmap + ROI + governance recommendations |
| **Phase C — Implementation** | 24 months | Phased implementation + quarterly radar review + continuous evolution |

➜ Full 8-stage story (with dialogue examples): [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md)
➜ Consulting report template: [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)
➜ Consulting toolkit templates: [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md)
➜ Delivery package & acceptance: [`../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)

---

## 7. Verifiable Deliverables: What Each Level Leaves Behind

Every level's "course" doesn't just end when the lecture ends — it leaves auditable evidence behind:

| Level | Main deliverables | Evidence |
|---|---|---|
| L1 | Personal chat workspace, Prompt Library | Account table, permission table, login records, Prompt examples |
| L2 | Skill Library, Agentic artifacts | Skill documents, test cases, version history, output examples |
| L3 | n8n Workflow PoC, Sub-workflow Library, Data Tables | Execution logs, retry-after-failure logs, system-integration screenshots |
| L4 | Verifiable Agent, Briefings, task cards | Agent log, Wiki versions, HITL sign-off records |
| L5 | Agent Team role cards, collaboration flow, cross-department results | Team run log, handoff records, governance records |
| **Consulting layer** | 14-chapter diagnostic report, 30/60/90-day Roadmap, ROI, governance recommendations | Stage Gate sign-off records, quarterly radar review |

➜ Full deliverables + evidence matrix: [`../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)

---

## 8. How to Use This Book (5 Entry Paths by Role)

| You are | Start here (20 min → 1 hour) |
|---|---|
| **CEO / Owner / Family member who wants to grasp the methodology** | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) — Ming's story |
| **Consultant / Trainee** | [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) — full 8-stage flow |
| **Board / Regulator / Academic** | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — scientific argument |
| **Enterprise IT / Cross-firm consultant** | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — alignment with McKinsey/BCG/TOGAF/Gartner |
| **Methodology researcher / AI Pedagogy academic** | [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) — why this is a new form of methodology |

---

## 9. Reference Quick Index

### 9.1 Academic Theory & Failure Modes

- [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — full discussion of the 7 theoretical pillars
- [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) — 14 failure modes (theory-predicted)
- [`../90_References/AI_GOVERNANCE_ALIGNMENT.md`](../90_References/AI_GOVERNANCE_ALIGNMENT.md) — alignment with NIST AI RMF / EU AI Act / ISO 42001
- [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) — 18-24 month empirical study design

### 9.2 Education & Assessment

- [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) — 10/25/50-item questionnaire (plain-language)
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL.md) — scoring model
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) — BARS scoring calibration (avoid subjectivity)
- [`../02_Course_Design/`](../02_Course_Design/) — full L1-L5 course plans

### 9.3 Consulting Delivery

- [`../03_Consulting_Report/`](../03_Consulting_Report/) — consulting report + toolkit templates
- [`../04_Scenarios/`](../04_Scenarios/) — 7 industry scenario cases (manufacturing / hospital / marketing / B2B / financial / government / education)
- [`../05_Sales/`](../05_Sales/) — sales talking points + FAQ
- [`../06_Delivery/`](../06_Delivery/) — delivery package + acceptance criteria + Engagement Lifecycle

### 9.4 Three-Engine Self-Disclosure

- [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) — three-engine co-edited README + §3 co-authoring discipline
- [`../07_AI_Contributions/ANTIGRAVITY.md`](../07_AI_Contributions/ANTIGRAVITY.md) ｜ [`CODEX.md`](../07_AI_Contributions/CODEX.md) ｜ [`CLAUDE_CODE.md`](../07_AI_Contributions/CLAUDE_CODE.md)
- [`../CHANGELOG.md`](../CHANGELOG.md) — three-engine co-edited changelog

### 9.5 Source Material

- [`../90_References/@AI-MD-PUBIC.pdf`](../90_References/@AI-MD-PUBIC.pdf) — original PDF methodology
- [`../90_References/MD-Map.png`](../90_References/MD-Map.png) — AI Maturity Map
- [`../90_References/Metholodgy.png`](../90_References/Metholodgy.png) — Eight-Stage Transformation Guide diagram
- [`../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) — video learning notes
- [`../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

---

## 10. Next Steps: 3 Suggested Paths

| Your need | Recommended next step |
|---|---|
| **Build the overall mental model** | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) (incl. §3.0, the full two-axis story) |
| **Find out which level your company is at** | The 10-item quick diagnostic in [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) |
| **Read this book directly with AI** | Open this repo with an AI IDE → first read root [`../README_EN.md`](../README_EN.md) §🚀 Three AI Engines Setup Guide and pick an engine to launch |

---

> ⚠️ **Academic Integrity Disclaimer**: All named cases in this repo (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 SAMPLE_CLIENT_CASE files) and all story protagonists (e.g., "Ming" and "MingChang Packaging") are **AI-generated fictional examples**, NOT real client data. All numbers (time, ROI, person-months, budget, KPI) are **illustrative only** and **must NOT be used for external marketing, contractual commitments, or academic empirical evidence**. Real longitudinal cases will replace these only after the 18-24 month empirical study described in [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) is complete.
>
> **Architecture Ownership**: The methodology architecture in this repo is proposed by the human author **Morris Lu (Tiger AI)**. The three AI engines (Antigravity / Codex / Claude Code) are tools that **execute, complete, elaborate, and audit**. See [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0.
