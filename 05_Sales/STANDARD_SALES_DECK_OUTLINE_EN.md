# Standard Sales Deck Outline (20 slides)

> 🌐 中文版本 / Chinese version: [STANDARD_SALES_DECK_OUTLINE.md](STANDARD_SALES_DECK_OUTLINE.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

Audience: department managers, PMs, IT lead, HR, AI Champion
Duration: 35-45 min
Purpose: Build trust in the methodology + show concrete deliverables + trigger a PoC conversation.

> ⚠️ **Disclaimer**: All client cases referenced in this deck (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education, "Company M / Ming," etc.) are **AI-generated fictional cases**, NOT real client data. All numbers are illustrative. Presenter must verbally state "These are AI-simulated teaching cases, not real clients." See [`../04_Scenarios/README_EN.md`](../04_Scenarios/README_EN.md).

---

## Slide 1 — Cover (same as Executive deck)

## Slide 2 — Who We Are

- Tiger AI 虎智科技 · Morris Lu (盧業興)
- Roles: n8n Taipei Ambassador · NTUST PhD student (Intelligent Manufacturing) · M.IT, Queensland University of Technology (QUT), Australia
- Mentor: Prof. Michael Rosemann (QUT)
- Visual: overlapping circles of individual + community + academic

## Slide 3 — Customer Observations

Three common patterns: shadow IT, PoCs forever stuck in demo, governance gap.

## Slide 4 — L1-L5 Maturity Model

Full 5 layers + tools + one-line positioning.

## Slide 5 — Layer-by-Layer Handoff

Each layer's output = the next layer's input; include the ASCII flow diagram.

## Slide 6 — Eight-Stage Consulting Structure

Diagnose → Vision → Strategy → Roadmap → Design → Implement → Govern → Sustain.

## Slide 7 — Diagnostic Tools

- 10-question version (sales development)
- 25-question version (pre-course)
- 50-question version (pre-consulting-interview)
- Company-profile questionnaire + deployment-mode scoring
- Visual: questionnaire → radar chart → level determination

## Slide 8 — L1 OpenWebUI Course

Audience: everyone. Content: accounts, groups, permissions, Prompt Library, Admin Panel, model control. Output: AI usage policy, Prompt Library, L2 candidate list. Gate 1 pass criteria.

## Slide 9 — L2 Knowledge Codification Course

Audience: core users. Content: Antigravity / Claude Code / Codex; Skill design, IPOE, version control. Output: 3-5 Skills, Workflow Blueprints. Gate 2A-2E.

## Slide 10 — L3 n8n Workflow Course

Audience: process designers, IT. Content: triggers, nodes, Sub-workflows, Data Tables, Webhook, GitHub Backup. Output: 3 Workflow PoCs + Execution Log. Gate 3A-3G.

## Slide 11 — L4 Hermes Agent Course

Audience: AI Champion + IT. Content: Wiki memory, 5 core Skills, ingest/query/update, briefing, Gate. Output: 1 Agent passing 4A-4E, task cards, Wiki, Evidence.

## Slide 12 — L5 ClawTeam Agentic Team Course

Audience: management + cross-functional. Content: based on HKUDS/ClawTeam (MIT). Five-layer architecture (Team/Workspace/Task/Inbox/Transport), git worktree, Role Card, Reviewer/Gate. Citation: <https://github.com/HKUDS/ClawTeam>

## Slide 13 — PoC Library

6 systems × 25-30 PoCs: Gmail / Sheets / Notion / CRM / API / ERP. Each PoC: trigger, input, AI step, systems, output, KPI, person-days. Details in `02_Course_Design/POC_SCENARIO_SPECS.md`.

## Slide 14 — Deployment Modes

Cloud AI · Hybrid · Full on-prem — three modes. Decided along three axes: data sensitivity, industry compliance, cost. Table: applicability conditions, pros/cons, course notes.

## Slide 15 — Stage Gate Governance

5 Gates + acceptance criteria per Gate. The "quality lock" that prevents advancing without passing.

## Slide 16 — ROI Cases

Three cases: manufacturing quality, hospital patient service, retail new-product launch. Each with Before/After numbers + roadmap summary.

## Slide 17 — Governance, Permissions, Audit

Permissions matrix · audit log requirements · 15-item AI ethics checklist. Mapped to ISO 42001 / EU AI Act / Taiwan's AI Basic Act.

## Slide 18 — Delivery Package & Acceptance

Full deliverables list (12 major items). Acceptance criteria per item. Details: `06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`.

## Slide 18b — 4 Authoritative Concept Docs (Showing IP Depth)

**Title**: The methodology isn't a black box — 4 open-sourced authoritative documents

**Content**:

- 📖 [`CLIENT_JOURNEY_STORY_EN.md`](../00_Overview/CLIENT_JOURNEY_STORY_EN.md) **Ming's Story** — 20-min methodology grasp, for CEOs
- 🔧 [`EIGHT_STAGE_FLOW_STORY_EN.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) **Full Flow** — 3-phase contract model + 6-week walkthrough, for consultants
- 🔬 [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) **Scientific Argument** — 5-condition validation, for boards / academia
- 🗺️ [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) **Industry Alignment Map** — vs McKinsey/BCG/Bain/Deloitte/TOGAF/Dragon1/Gartner/MIT/Forrester

> **These 4 docs + toolkit = total IP depth**, fully Apache 2.0 open source.

## Slide 18c — 3-Phase Contract Model

**Title**: No 24-month mega-contract — phased, with exit points

| Phase | Duration | Example $ | Deliverable | Exit Gate |
| --- | --- | --- | --- | --- |
| **A Diagnostic** | 2 weeks | NT$ 800K | Mid-engagement assessment report (client receipts) | Gate A |
| **B Strategy** | 4 weeks | NT$ 2M | Full consulting report + Ideal Practice signed | Gate B |
| **C Implementation** | 24 months | NT$ 7M | Transformation Roadmap + Change Mgmt + quarterly radar | Gate C every quarter |

**Core message**: clients **can disembark**, so they **dare to embark**. Each phase deliverable is good enough that clients **want to continue**.

## Slide 19 — Three Engagement Tiers

Half-day / 1-day / 2-day / consulting project. Chosen by company size, objectives, budget.

## Slide 20 — Next Step

30-minute discovery call → customized proposal. QR code + contact.

---

## Production Notes

- 16:9 ratio; 4-6 key points per slide
- Section color blocks: diagnose (blue) / course (green) / consulting (gold) / governance (gray)
- Page number + section footer throughout
- Back cover: Apache 2.0 + GitHub repo URL
