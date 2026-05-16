# 90 References — References, Sources & Acknowledgments

> 🌐 中文版本 / Chinese version: [README.md](README.md)

## 1. Purpose of This Directory

This directory is the entire methodology's **reference library, citation governance center, and acknowledgments roll**. `00`-`07` are "method and tools"; this directory answers three things:

1. **What are these methods based on?** (original PDF, methodology diagrams, video learning notes)
2. **Which content cites third parties? Are the licenses compliant?** (every cited project has its own `*_REFERENCE.md`)
3. **Whose shoulders are we standing on?** (acknowledgments roll)

Who uses this directory: consultants, reviewers, legal, redistributors, **learners and enthusiasts looking for the upstream projects**.

---

## 2. Acknowledgments: Whose Shoulders We Stand On

Organized by usage layer into four categories: **core platforms / consulting-framework / agent & skill / case-index**. Each "appreciation card" includes the **upstream URL + where we cite it + link to the full _REFERENCE.md**.

### 2.1 Core Platforms (the runtime base for L1-L5)

These aren't "cited material" — they are **the platforms L1-L5 courses run on**. Without them, this methodology has no place to land.

| # | Platform | Role in this methodology | Upstream |
|---|---|---|---|
| 1 | **OpenWebUI** | The enterprise AI entry point for L1 Controlled AI Access (personal chat workspaces, accounts & permissions) | <https://github.com/open-webui/open-webui> |
| 2 | **n8n** | The core engine for L3 Workflow Automation (cross-system integration + Sub-workflow Library) | <https://github.com/n8n-io/n8n> |
| 3 | **Hermes Agent** | Reference implementation for L4 Autonomous Agent (Wiki ingest/query/update + Gate 4A-4E) | Internal knowledge-grade Agent design pattern (course only takes the concept, not the code) |
| 4 | **ClawTeam** | The Agentic Team framework for L5 Multi-Agent Organization | <https://github.com/HKUDS/ClawTeam> (HKUDS, MIT) |

➜ Video learning notes: [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md) ｜ [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md)
➜ ClawTeam full citation: [`CLAWTEAM_REFERENCE_EN.md`](CLAWTEAM_REFERENCE_EN.md)

### 2.2 Consulting Framework Class (impacts 03_Consulting_Report)

#### 🎯 [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant) (MIT)

- **What it is**: a programmatic organization of classic consulting analytical frameworks (MECE, Pyramid Principle, Issue Tree, Porter's 5 Forces, SWOT, BCG Matrix, 5 Whys, Fishbone, Business Model Canvas, WBS/RACI, NPV/IRR, Lean/Six Sigma, etc. — 50+ frameworks)
- **Why we appreciate it**: turns consulting frameworks scattered across many sources into **a structured, citable, composable library** — not yet another PPT collection
- **Where we use it**: [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) — adapted into 7 categories + a framework selector + mapping to the eight stages
- **Full citation**: [`CONSULTANT_FRAMEWORKS_REFERENCE_EN.md`](CONSULTANT_FRAMEWORKS_REFERENCE_EN.md)

#### 🎯 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills) (MIT)

- **What it is**: turns the "**problem → report / deck**" production craft of top-tier consultants like McKinsey into an executable 8-step workflow
- **Why we appreciate it**: the first to write the whole "Dummy Page → dependency management → 7 page layouts → progressive disclosure → troubleshooting" set into a learnable SOP — instead of "the implicit craft only senior consultants have"
- **Where we use it**: [`../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) — adapted into an 8-step consulting report production workflow + §9 troubleshooting playbook
- **Full citation**: [`MCKINSEY_SKILLS_REFERENCE_EN.md`](MCKINSEY_SKILLS_REFERENCE_EN.md)

#### 🎯 **Mirza Iqbal ([next8n.com](https://next8n.com)) — Workflow Delivery Framework** (MIT)

- **What it is**: the **operational SOP** for n8n delivery consultancy — the full Discovery → Sprint → Handover lifecycle, pricing tables, client communication templates
- **Why we appreciate it**: one of the few people who open-sourced the **operational SOP for delivery work** (not just technical SOP) — fills the operational side that the consulting industry rarely talks about
- **Where we use it**: [`../06_Delivery/`](../06_Delivery/) — Engagement Lifecycle, Role SOPs, Business Document Templates are all inspired by this
- **Full citation**: [`WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE_EN.md`](WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE_EN.md)
- **Accessed via**: <https://github.com/MorrisLu-Taipei/AI-Workflow-Delivery-Framework> (README clearly credits Mirza Iqbal as original creator)

### 2.3 Agent & Skill Class (impacts 02_Course_Design)

#### 🎯 [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) (MIT)

- **What it is**: a 12-division agent persona library (marketing, sales, customer service, HR, finance, R&D, etc.) — ready to use
- **Why we appreciate it**: turns "Agent persona design" into a reusable library, sparing teams from writing system prompts from scratch every time
- **Where we use it**: [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6 "leveraging a ready-made Agent library" module
- **Full citation**: [`AGENCY_AGENTS_REFERENCE_EN.md`](AGENCY_AGENTS_REFERENCE_EN.md)

#### 🎯 [`MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack) (mixed license)

- **What it is**: n8n Skill three-layer structure (Workflow Library + Cookbook + DSL Spec), with an AI-generated workflow Skill Pack
- **Why it sits here**: this is the methodology author Morris Lu's own project, but it's still listed here to **demonstrate the citation discipline** — even for our own project, license and third-party origins (`_vendor/` MIT) are documented to the same standard
- **Where we use it**: [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) second half
- **Full citation**: [`N8N_SKILL_PACK_REFERENCE_EN.md`](N8N_SKILL_PACK_REFERENCE_EN.md)

### 2.4 Case-Index Class (impacts 04_Scenarios)

#### 🎯 [`Shubhamsaboo/awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps) (Apache-2.0)

- **What it is**: a curated list of 150+ real LLM application cases (agent / RAG / fine-tuning / multimodal, etc.), maintained by the community
- **Why we appreciate it**: high curation quality, clear taxonomy, continuously updated; the fastest reference when a consultant tells a client "**this is how others tackled this scenario**"
- **Where we use it**: [`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index — mapped onto a dual-axis index (L1-L5 × enterprise department); **the mapping is ours**, the original case list is copyrighted to Shubham Saboo and community contributors
- **Full citation**: [`AWESOME_LLM_APPS_REFERENCE_EN.md`](AWESOME_LLM_APPS_REFERENCE_EN.md)

#### 🎯 [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) (MIT)

- **What it is**: 93+ AI engineering teaching projects (executable implementations from RAG to multi-agent)
- **Why we appreciate it**: every project comes with **code + a teaching video**, so learners can dive in directly; complements awesome-llm-apps's "curated cases" with the "hands-on implementation" side
- **Where we use it**: [`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index second source — mapped to L2-L4 course-level executable demos
- **Full citation**: [`AI_ENGINEERING_HUB_REFERENCE_EN.md`](AI_ENGINEERING_HUB_REFERENCE_EN.md)

---

## 3. Original Reference Material & Diagrams (self-made or public-domain)

| File | Purpose |
| --- | --- |
| [`@AI-MD-PUBIC.pdf`](@AI-MD-PUBIC.pdf) | AI Transformation Maturity Model public-version manual (the original PDF methodology draft) |
| [`MD-Map.png`](MD-Map.png) | AI Maturity Map, used in the root README |
| [`Metholodgy.png`](Metholodgy.png) | Enterprise consulting eight-stage transformation guide, used in the root README |

## 4. Academic Foundation & Failure Patterns (fully original, written by Tiger AI + the three AI engines)

| File | Purpose |
| --- | --- |
| [`FAILURE_PATTERNS.md`](FAILURE_PATTERNS.md) | 14 failure patterns (theory-predicted + real cases + corresponding fixes) |
| [`AI_GOVERNANCE_ALIGNMENT.md`](AI_GOVERNANCE_ALIGNMENT.md) | Alignment with NIST AI RMF / EU AI Act / ISO 42001 |
| [`PILOT_STUDY_PROTOCOL_EN.md`](PILOT_STUDY_PROTOCOL_EN.md) | 18-24 month empirical research design (Pilot Study) |

The academic theory body itself (the 7 pillars) is in [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md).

## 5. Video Learning Notes (derivative notes; original video copyright belongs to the creators)

| File | Purpose |
| --- | --- |
| [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md) | Learning notes from the OpenWebUI public playlist, mapped to L1 course application |
| [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md) | Learning notes from the TigerAI channel, focused on n8n / L3 course application |

---

## 6. Citation Discipline (the iron rules for future contributors)

To cite any third-party material in this repo, **everyone follows these "Approach A" principles**:

| # | Principle | How |
|---|---|---|
| 1 | **Adapt independently — don't fork, don't reproduce source code** | Reference the structure and concepts, then rewrite in this methodology's voice |
| 2 | **Explicit attribution, dual-noted** | (a) header note in the file that cites it; (b) standalone `*_REFERENCE.md` in this directory |
| 3 | **Generalize to this methodology's scenario** | Convert domain-specific content into the L1-L5 AI transformation consulting context |
| 4 | **No license = no integration** | Third-party projects without LICENSE are not integrated (only cited as external example URLs) |
| 5 | **Generous appreciation** | In the citation file, **state explicitly what's good about it**, not just "see source below" |
| 6 | **Honest about failure** | If a cited tool turned out unsuitable, honestly write it in `FAILURE_PATTERNS.md` — not just success stories |

**Usage logic**: to find "what was cited by file X in directory Y" → read that file's header → jump to the corresponding `*_REFERENCE.md` in this directory for the full license note.

---

## 7. Cross-Directory Mapping

| Directory | Relationship to this directory |
| --- | --- |
| [`../00_Overview/`](../00_Overview/) | The methodology diagrams (Metholodgy.png / MD-Map.png) come from here; the 7 theoretical pillars discussion lives in `00` |
| [`../02_Course_Design/`](../02_Course_Design/) | Third-party citations for L1/L2/L3/L5 courses (OpenWebUI notes, agency-agents, n8n-Skill-Pack, ClawTeam) |
| [`../03_Consulting_Report/`](../03_Consulting_Report/) | Third-party citations for the frameworks library and report workflow (consultant, mckinsey-skills) |
| [`../04_Scenarios/`](../04_Scenarios/) | Third-party citations for the LLM application case index (awesome-llm-apps, ai-engineering-hub) |
| [`../06_Delivery/`](../06_Delivery/) | Third-party citation for the delivery operations layer (Mirza Iqbal framework) |
| [`../07_AI_Contributions/`](../07_AI_Contributions/) | The three AI engines themselves are also "acknowledgment subjects" — Antigravity / Codex CLI / Claude Code |

---

## 8. Common Usage Scenarios

- **Wondering why a file is written a particular way**: read the file header → map to the `*_REFERENCE.md` in this directory
- **Redistributing / commercializing this methodology**: read §6 citation discipline + the [`NOTICE`](../NOTICE) attribution requirements
- **Want to onboard a new open-source project** → follow the 6 principles in §6: confirm the license → adapt independently → create `*_REFERENCE.md` → add it to this README §2 acknowledgments roll
- **Want to engage upstream communities, want to interact / acknowledge**: click the GitHub URL on each appreciation card to star, follow, open an issue, or send a PR
- **Learner citing this repo's content in their own paper / deck**: per §6, when citing this methodology preserve the original author attribution ([`../NOTICE`](../NOTICE)); when citing third-party material follow the learner-citation format in the corresponding `*_REFERENCE.md`

---

## 9. Acknowledgments

All upstream authors and communities listed in this directory **are the shoulders this methodology stands on**. Any misinterpretation, inappropriate citation, or deviation from the original intent is the sole responsibility of the methodology author **Tiger AI Morris Lu 盧業興** — not of the upstream authors or communities.

If you are an upstream author and feel any citation in this repo is inappropriate, needs correction, or should be reinforced — please open an issue or contact Morris Lu, and we'll handle it immediately.

> **Architecture Ownership**: The methodology architecture in this repo is proposed by the human author **Morris Lu (Tiger AI)**. The three AI engines (Antigravity / Codex / Claude Code) are tools that **execute, complete, elaborate, and audit**. See [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0.
