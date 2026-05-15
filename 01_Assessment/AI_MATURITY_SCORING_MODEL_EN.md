# AI Maturity Scoring Model

> 🌐 中文版本 / Chinese version: [AI_MATURITY_SCORING_MODEL.md](AI_MATURITY_SCORING_MODEL.md)

Last updated: 2026-05-13

## 1. Scoring Purpose

This scoring model is used to convert the enterprise's current AI state into a maturity result that is communicable, comparable, and deployable.

Scoring is not for labeling, but to answer four questions:

1. Which maturity level does the enterprise primarily sit at today?
2. Which capabilities are already in place, and which remain gaps?
3. How should the course ratio be configured?
4. Which issues should the consulting diagnostic report prioritize?

## 2. L1-L5 Maturity Definitions

L1-L5 is **two axes**: the **scale axis (L1-L3)** — individual → department → cross-department / company-wide, humans supervise AI; and the **AI-autonomy axis (L4-L5)** — AI super-assistant → AI team, AI is operationally autonomous while humans step back to governor (retaining oversight). The key boundary is L3 → L4. Full story: [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §3.0.

> **Naming note (v2.0 dual naming)**: L1-L5 uses **capability-oriented naming**. The "Tiger AI Reference Implementation" column lists Tiger AI's **example tools**, not the definition — the same capability can be implemented with other tools (e.g. L1 could use OpenWebUI / LibreChat / a custom chat gateway). This preserves academic vendor-neutrality + practical implementability.

| Level | Capability Name | Legacy short tag | Tiger AI Reference Implementation | Axis | Maturity Definition | Completion Criteria |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | **Controlled AI Access** | `Chat AI` (deprecated) | OpenWebUI | Scale axis · individual | Employees use AI through a controlled portal to boost personal productivity | A unified portal, basic usage guidelines, common Prompts, and personal productivity cases exist |
| L2 | **Knowledge Codification** | `Skill AI` (deprecated) | Antigravity / Claude Code / Codex | Scale axis · department | By department responsibility, personal experience is consolidated into departmental reusable Skills | A Skill Library, SOPs, templates, Checklists, and departmental shared examples exist |
| L3 | **Workflow Automation** | `Workflow AI` (deprecated) | n8n | Scale axis · cross-department / company-wide | AI chains cross-department Skills and systems, entering company-wide workflows to execute tasks | Gmail, Sheets, Notion, CRM, API, ERP, and similar workflow PoCs or production flows exist |
| L4 | **Autonomous Agent** | `Auto Agentic AI` (deprecated) | Hermes Agent | AI-autonomy axis · super-assistant | A fully autonomous AI Agent uses Wiki memory as its base, calls Skills/Workflows, performs ingest, query, update, and briefing, and leaves evidence | Agent task cards, L4 IPOE, Wiki/schema, tool list, permission boundaries, Log, HITL review, and acceptance gate 4A-4E exist |
| L5 | **Multi-Agent Organization** | `Agentic Team AI` (deprecated) | ClawTeam | AI-autonomy axis · AI team | Multiple specialist Agents form a functional division of labor, collaborating to complete cross-departmental enterprise-class tasks | Agent Team role assignment, task dispatch, integrated output, quality check, and governance exist |

> Terminology: in this scoring model, **Stage Gate = acceptance gate**, and **HITL = Human-in-the-Loop** (a human-review checkpoint in the workflow).

## 3. Six Assessment Dimensions

| Dimension | Description | Primary Mapped Maturity |
| --- | --- | --- |
| A. Tool Usage | Whether employees use AI tools stably, safely, and effectively | L1 |
| B. Knowledge Consolidation | Whether Prompts, SOPs, templates, and experience are consolidated into reusable assets | L2 |
| C. Process Automation | Whether AI is connected to real processes and reduces manual rework | L3 |
| D. System Integration | Whether the integration of Gmail, Sheets, Notion, CRM, API, ERP, and DB is possible | L3 |
| E. Agent Application | Whether there is a traceable Agent that decomposes tasks, calls tools, accumulates memory, produces briefings, and executes reporting | L4-L5 |
| F. Implementation & Change | Whether there are permissions, audit, data classification, KPI, and ROI tracking | L1-L5 |

## 4. Per-Item Scoring Scale

All questionnaire items are scored 0-4.

| Score | Judgment Criteria |
| --- | --- |
| 0 | None at all, or unknown whether it exists |
| 1 | Sporadic individual use, but no standard or system |
| 2 | Department has an initial approach, but not yet stably reproduced |
| 3 | Standard processes, shared assets, or repeatable practices exist |
| 4 | Institutionalized, governable, measurable, and able to spread across departments |

## 5. Maturity Determination Method

### 5.1 Primary Maturity

Primary maturity is determined as the "highest stable level."

A level is considered stable when it simultaneously satisfies:

- The average score of the dimensions mapped to that level is at least 3.
- The capability of the preceding level is not below 2.5.
- The Implementation & Change dimension is not below 2.

### 5.2 Local Maturity

If a particular department or scenario has reached a higher level while the company as a whole has not, mark it as local maturity.

Example:

- The company overall is at L2.
- The customer service department has a PoC of n8n integrating Gmail, CRM, and Sheets.
- This can be marked as "Overall L2, Customer Service locally L3."

### 5.3 Recommended Score Ranges

| Total Score Range | Initial Assessment |
| --- | --- |
| 0-20 | L0-L1: stable AI usage not yet formed |
| 21-40 | L1: personal AI usage stage |
| 41-60 | L2: departmental Skill-ification stage |
| 61-78 | L3: Workflow automation stage |
| 79-92 | L4: Agentic AI initial operation |
| 93-100 | L5: Agent Team collaboration stage |

Note: Total score is only an initial assessment. The final determination must still reference primary maturity, local maturity, and governance scores.

## 6. L1-L5 Observable Indicators

### L1 Controlled AI Access

| Indicator | What to Observe |
| --- | --- |
| Unified portal | Whether OpenWebUI or an enterprise-approved AI portal exists |
| Frequency of use | Whether employees use AI stably each week for work |
| Prompt capability | Whether they can write effective questions and output specifications |
| Usage guidelines | Whether they know which data must not be input to AI |
| Personal benefit | Whether they can cite cases of time savings or quality improvement |

### L2 Knowledge Codification

| Indicator | What to Observe |
| --- | --- |
| Skill list | Whether the department has a list of commonly used Skills |
| Knowledge consolidation | Whether Prompts, SOPs, templates, and cases are organized as assets |
| Sharing mechanism | Whether Notion, Git, a document library, or an internal platform is used to manage them |
| New-hire onboarding | Whether new hires can directly apply Skills to complete work |
| Quality consistency | Whether quality gaps caused by individual differences are reduced |

### L3 Workflow Automation

| Indicator | What to Observe |
| --- | --- |
| Process inventory | Whether you know which processes can be automated |
| System integration | Whether Gmail, Sheets, Notion, CRM, API, ERP are integrated |
| Auto-triggering | Whether Trigger, Webhook, or schedules exist |
| Human review | Whether human confirmation is preserved at critical nodes |
| Operations logs | Whether Log, error notification, and retry mechanisms exist |

### L4 Autonomous Agent

| Indicator | What to Observe |
| --- | --- |
| Task decomposition | Whether the Agent can decompose goals into steps |
| Knowledge memory | Whether `purpose.md`, `SCHEMA.md`, Wiki, index, log exist |
| Ingest closed loop | Whether documents can be ingested, analyzed, written back to the Wiki, and the index updated |
| Query / Update | Whether the Agent can answer with evidence and retain write-back records |
| Briefing / Discovery | Whether periodic briefings can be produced based on watchlist, queue, tasks |
| Tool invocation | Whether the Agent can call Skills and Workflows |
| Permission boundary | Whether what the Agent can and cannot do is clearly defined |
| Reporting mechanism | Whether the Agent can report results, exceptions, next steps, and evidence |
| Human-machine collaboration | Whether humans can review, correct, and take over Agent tasks |

### L5 Multi-Agent Organization

| Indicator | What to Observe |
| --- | --- |
| Role assignment | Whether there are Agent roles for market, product, customer service, finance, etc. |
| Task dispatch | Whether enterprise-class tasks can be split for multi-Agent collaboration |
| Output integration | Whether there is a role or process that integrates Agent outputs |
| Quality check | Whether there is a Critic, Reviewer, or HITL review |
| Business value | Whether it supports cross-departmental decision-making, operations, or innovation tasks |

## 7. Deployment Mode Scoring

Deployment mode is not equivalent to maturity, but it affects the course and the deployment roadmap.

| Dimension | Cloud AI Tendency | Hybrid Tendency | Fully On-Premises Tendency |
| --- | --- | --- | --- |
| Data sensitivity | Low | Medium | High |
| Cloud policy | Public cloud allowed | Partially cloudable | Core data must not go to cloud |
| IT capability | Weak | Medium | Strong |
| Budget | Low | Medium | High |
| System landscape | Mainly SaaS | SaaS + internal systems | Mainly ERP/MES/DB/intranet |
| Regulatory requirements | Low | Medium | High |

### Recommended Judgment

- Cloud AI: Fast launch, suitable for low-sensitivity data and marketing/services scenarios.
- Hybrid: First choice for most enterprises, balancing cost, capability, data security, and deployment speed.
- Fully on-premises: Suitable for highly sensitive data, R&D/manufacturing, finance, healthcare, government, and strict-audit scenarios.

## 8. Course-Ratio Recommendation Logic

### 8.1 Recommended by Maturity

| Initial Maturity | L1 | L2 | L3 | L4 | L5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| L0-L1 | 40% | 35% | 20% | 5% | 0% |
| L1 | 30% | 35% | 25% | 10% | 0% |
| L2 | 15% | 30% | 40% | 10% | 5% |
| L3 | 5% | 20% | 35% | 30% | 10% |
| L4 | 5% | 15% | 25% | 30% | 25% |
| L5 | 0% | 10% | 20% | 30% | 40% |

### 8.2 Adjustment by Deployment Mode

- Cloud AI: Increase L1 and L2 ratios; L3 focuses on SaaS integration.
- Hybrid: Increase L3 ratio; strengthen data classification, API, Credential, and human review.
- Fully on-premises: Increase governance, system integration, and L3/L4 depth; cases lean toward ERP, DB, intranet, and RAG.

### 8.3 Adjustment by Industry

- R&D / manufacturing: Increase L2, L3, governance, and internal-system cases.
- Marketing / services: Increase L1, L2, L3 rapid PoCs and content-production cases.
- Highly sensitive industries: Increase data classification, permissions, audit, human review, and fully on-premises architecture.

## 9. Gap Taxonomy

| Gap Type | Description | Common Remediation |
| --- | --- | --- |
| Tool gap | No unified AI portal or licensed tools | L1 course, OpenWebUI, usage guidelines |
| Skill gap | Personal experience not consolidated | L2 Skill Workshop, templates and knowledge base |
| Workflow gap | Processes still rely on manual data transfer | L3 n8n PoC, system integration |
| System integration gap | Gmail, Sheets, Notion, CRM, API, ERP not integrated | API inventory, Credential, data routing |
| Agent gap | No AI capable of autonomously executing tasks | L4 Hermes Agent task design |
| Agent Team gap | Cross-departmental tasks lack multi-Agent collaboration | L5 ClawTeam scenario design |
| Governance gap | Permissions, audit, and ROI unclear | Governance sheet, acceptance gate (Stage Gate), KPI |
