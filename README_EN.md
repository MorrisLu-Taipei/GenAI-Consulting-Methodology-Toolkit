# GenAI Consulting Methodology Toolkit

Language: [繁體中文](README.md) | English

Enterprise AI transformation maturity assessment and implementation methodology toolkit.

Original Author: **Tiger AI Morris Lu 盧業興**  
Role: **n8n Taipei Ambassador / PhD Student, Graduate Institute of Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australia**

License summary: this project is released under the **[Apache License 2.0](LICENSE)**. You may use, copy, modify, redistribute, and commercialize it; when redistributing, preserve the Apache 2.0 license text and the attribution notices in [`NOTICE`](NOTICE).

> **Only have 5 minutes?** Read [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) first — the whole methodology on one page.

## Read This as a Living Book: Read It With AI

This repo is a **living book**. `git clone` it or download the zip, and open it in an AI IDE (Antigravity / Claude Code / Codex, etc.) — the AI automatically reads [`AGENTS.md`](AGENTS.md) (and [`CLAUDE.md`](CLAUDE.md)) and acts as the **co-reading tutor** for this methodology.

Then you can:

- Ask it **any question** about the methodology;
- Have it **apply the methodology to your company's situation**;
- Walk through the L1-L5 self-diagnosis with it and find your next step.

The methodology isn't just to "read" — it's to "read with, ask, and apply" together.

## What This Toolkit Solves

Many companies start AI adoption by jumping directly into tools. They try a chatbot, then automation, then agents, but often lack a maturity baseline, process ownership, evidence, and stage gates.

This toolkit proposes a clearer path: start with a lightweight maturity questionnaire, map the client to L1-L5 AI maturity, design the training mix, generate verifiable deliverables during class, and then use an eight-stage consulting method to produce the final AI transformation diagnostic report, roadmap, ROI view, and governance recommendations.

## Future-State Story Before Class

Before clients choose an L1-L5 course mix, they need to see the future workday first. The story is not "we will learn five tools." The story is "this is how the company will work after the training."

Imagine a Monday morning three months later:

- **L1 Chat AI**: every employee logs in to OpenWebUI with their own account, personal chat workspace, history, and departmental permissions.
- **L2 Skill AI**: experienced employees convert their best methods into reusable Skills for writing, reporting, customer service, SOP review, and development work.
- **L3 Workflow AI**: n8n connects Gmail, Sheets, Notion, CRM, APIs, ERP, and other systems so work moves through real enterprise workflows.
- **L4 Auto Agentic AI**: Hermes Agent reads tasks, documents, workflow results, and Wiki memory to produce briefings, follow-up lists, evidence, and decisions that require HITL (Human-in-the-Loop) review.
- **L5 Agentic Team AI**: ClawTeam coordinates specialist agents across market, product, service, finance, and operations work.

This future-state story should be told before the course begins. Clients first understand the work scenario they want to reach, and only then discuss diagnosis, course ratio, deliverables, evidence, and acceptance gates (Stage Gates).

## AI Maturity Map

![AI Maturity Map](90_References/MD-Map.png)

## Methodology Overview

![Consulting Methodology: Eight-Stage Transformation Guide](90_References/Metholodgy.png)

## Core Flow

```text
AI maturity questionnaire
→ Company profile, industry scenario, and deployment-mode survey
→ L1-L5 course mix design
→ L1 OpenWebUI enterprise accounts and personal chat workspaces
→ L2 Antigravity / Claude Code / Codex Skill training
→ L3 n8n workflows connected to Gmail, Sheets, Notion, CRM, API, ERP, and other systems
→ L4 Hermes Agent for verifiable autonomous agentic work
→ L5 ClawTeam for Agentic Team collaboration
→ Scenario cases, evidence, and acceptance gates (Stage Gates)
→ Eight-stage AI transformation consulting diagnosis
→ AI transformation diagnostic report, roadmap, ROI, and governance recommendations
```

## L1-L5 Maturity Model

| Level | Name | Platform | Axis | Enterprise Positioning |
| --- | --- | --- | --- | --- |
| L1 | Chat AI | OpenWebUI | Scale axis · individual | Establish the enterprise's internal AI chat entry — every employee has their own account, AI chat workspace, and permission boundary |
| L2 | Skill AI | Antigravity / Claude Code / Codex | Scale axis · department | By department responsibility, organize personal knowledge, prompts, documents, and work methods into reusable Skills |
| L3 | Workflow AI | n8n | Scale axis · cross-department / company-wide | Connect cross-department Skills and link email, Sheets, Notes, CRM, API, ERP, and other systems, so AI enters company-wide automation processes |
| L4 | Auto Agentic AI | Hermes Agent | AI-autonomy axis · super-assistant | Combine a Wiki capability map, AI tools, Workflows, auto-scheduling, and autonomous learning into a verifiable, fully autonomous AI Agent super-assistant |
| L5 | Agentic Team AI | ClawTeam | AI-autonomy axis · AI team | Let multiple specialist Agents form a functional division of labor, collaboratively completing cross-department, cross-process enterprise tasks as an AI team |

### The Two Axes of L1-L5

L1-L5 is not "five tools" — it is a maturity path connecting **two axes**:

- **L1 → L2 → L3: the scale axis (humans use / supervise AI).** These three levels are the "human-in-the-loop, humans use AI, humans supervise AI" stage, scaling up along the organization — **L1 individual** (each employee uses AI on their own) → **L2 department** (by department responsibility, package personal knowledge into reusable Skills) → **L3 cross-department / company-wide** (connect cross-department Skills and link systems, so AI enters company-wide automation).
- **L4 → L5: the AI-autonomy axis (AI runs autonomously, without real-time human supervision).** These two levels are the AI entities the enterprise "grows in addition to" its human workforce — **L4 AI super-assistant** (a fully autonomous AI Agent entity) → **L5 AI team** (multiple specialist Agents collaborating in a functional division of labor).

> The key boundary: **L1-L3 is "humans assist / supervise AI" — AI is a tool; L4-L5 is "AI runs autonomously" — AI is the enterprise's extra digital workforce.** In adoption order, L1-L3 first brings people and the organization up to speed; L4-L5 only grows autonomous AI on a solid foundation.
>
> Even at L4-L5, **the governance framework is still built by humans, and humans retain oversight** — what AI is autonomous in is "operational execution," not "governance decisions." Every level keeps HITL (Human-in-the-Loop) review and acceptance gates; the more autonomous AI becomes, the more the human role is upgraded to "governor" rather than replaced.

## Verification Logic

Each level defines clear input, process, output, evidence, and acceptance-gate (Stage Gate) criteria. The output of a lower level becomes the input for the next level, so clients can verify maturity instead of relying on abstract AI claims.

## Repository Structure

| Folder | Purpose |
| --- | --- |
| [`00_Overview`](00_Overview/) | Overall narrative, story, and WBS |
| [`01_Assessment`](01_Assessment/) | AI maturity questionnaire, scoring model, deliverables, and evidence matrix |
| [`02_Course_Design`](02_Course_Design/) | L1-L5 course plans, company profile, deployment modes, and course module matrix |
| [`03_Consulting_Report`](03_Consulting_Report/) | AI transformation diagnostic report template |
| [`04_Scenarios`](04_Scenarios/) | Client scenarios, control tables, manufacturing case, and hospital case |
| [`05_Sales`](05_Sales/) | Value proposition, sales talking points, and FAQ |
| [`06_Delivery`](06_Delivery/) | Delivery package and acceptance criteria |
| [`90_References`](90_References/) | Source PDF, diagrams, video learning notes, and references |

## Recommended Reading Order

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md)
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md)
4. [`01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)
5. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
6. [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md)
7. [`02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md)
8. [`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md)
9. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md)
10. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md)
11. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)
12. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)

## Acknowledgments

Special thanks to **Prof. Michael Rosemann**, Queensland University of Technology (QUT), Brisbane, Australia.  
Profile: <https://www.qut.edu.au/about/our-people/academic-profiles/m.rosemann>

The theoretical foundation of this consulting methodology was shaped by the author's studies at QUT and by Prof. Michael Rosemann's long-term inspiration and teaching in **Business Process Management (BPM)**, **Capability Maturity Models**, and **enterprise innovation methodology**.

Two core parts of this work are especially influenced by that foundation:

- **Eight-stage consulting structure**: enterprise process diagnosis, capability assessment, transformation path design, and governance implementation.
- **L1-L5 AI Maturity Model**: a localized five-layer enterprise AI adoption framework informed by capability-maturity logic.

Disclaimer: any errors, omissions, local adaptations, or AI-domain extensions in this methodology are solely the responsibility of Tiger AI Morris Lu 盧業興 and do not represent the views or positions of Prof. Michael Rosemann or QUT.

## License And Attribution

This project is released under the **[Apache License 2.0](LICENSE)**. You may use, copy, modify, adapt, redistribute, teach, deliver consulting work with, and commercialize it.

When redistributing, adapting, packaging commercially, using in course materials, consulting deliverables, or product documentation, preserve the Apache 2.0 license text and the attribution notices in [`NOTICE`](NOTICE):

```text
Original Author: Tiger AI Morris Lu 盧業興
Role: n8n Taipei Ambassador / PhD Student, Graduate Institute of Intelligent Manufacturing, National Taiwan University of Science and Technology
Source: https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit
```

Third-party platform names, trademarks, videos, external projects, and cited materials remain the property of their respective owners.
