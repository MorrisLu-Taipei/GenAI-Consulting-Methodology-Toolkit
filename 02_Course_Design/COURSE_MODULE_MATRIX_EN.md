> 🌐 中文版本 / Chinese version: [COURSE_MODULE_MATRIX.md](COURSE_MODULE_MATRIX.md)

# L1-L5 Course Module Matrix

Last updated: 2026-05-13

## 1. Course Design Principles

The course is not a fixed menu; it is configured according to "maturity + company profile + deployment mode + industry scenario."

Before every class, the following must be completed:

1. AI maturity questionnaire.
2. Company profile survey.
3. Determination of cloud AI / hybrid / fully on-premises mode.
4. Selection of industry and departmental scenarios.
5. L1-L5 course ratio configuration.

## 2. Course Product Packages

| Product Package | Duration | Target Audience | Primary Purpose | Deliverables |
| --- | --- | --- | --- | --- |
| Half-day Experience Course | 3 hours | First-time prospects, executive alignment sessions | Establish a shared L1-L5 language and an initial diagnosis | Quick questionnaire, preliminary maturity assessment, course recommendation |
| One-day Workshop | 6 hours | Department managers and seed personnel | Complete L1-L2 capability buildout and L3 scenario inventory | Prompts, Skill list, Workflow candidate list |
| Two-day Onboarding Bootcamp | 12 hours | Seed team, IT, process owners | Complete L2-L3 PoC and introduce L4 Agent design | Skill Library, n8n PoC, Agent task cards |
| Consulting Diagnostic Project | 2-4 weeks | Leadership, cross-functional teams | Produce an AI transformation diagnostic report using the eight-stage methodology | Diagnostic report, roadmap, ROI and governance recommendations |

## 3. L1 Chat AI: OpenWebUI

### Course Objectives

Enable employees to perform high-frequency knowledge work through a controlled AI gateway and to understand data security and usage boundaries. The enterprise edition of L1 must achieve: every employee logs in with their own account, owns their own chat area, and Admins can manage accounts, roles, groups, models, features, and permissions.

### Course Outline

1. Overview of AI maturity L1-L5.
2. OpenWebUI personal operations: login, personal chat area, chat history, folders, model selection.
3. OpenWebUI Admin: account approval, roles, groups, permissions, model and feature governance.
4. Prompt fundamentals: role, task, data, format, constraints.
5. Document summarization, email drafts, meeting minutes, report drafts.
6. AI usage policy: what can be input, what cannot be input, what requires human confirmation.

### Hands-on Exercises

- Produce a customer email draft.
- Each learner creates 2 chat topics using their own account.
- Admin creates or approves test accounts and configures department groups.
- Summarize a set of meeting minutes.
- Distill a long document into an executive summary.
- Build a personal frequently-used Prompt set.

### Post-class Deliverables

- Personal high-frequency Prompts.
- Department-wide sample Prompts.
- Account / group / permission / model visibility configuration sheet.
- OpenWebUI Admin Runbook.
- Draft AI usage policy.
- L2 Skill candidate list.

### Instructor Notes

L1 must avoid only teaching "fun Prompts." The focus is showing the customer that AI can safely enter daily work and paving the way for L2 Skill-ification. If the enterprise cannot provide each user with an independent account, a personal chat area, and Admin permission governance, broad rollout should not be opened. The full L1 design is documented in `L1_OPENWEBUI_COURSE_PLAN.md`.

## 4. L2 Skill AI: Antigravity / Claude Code / Codex

### Course Objectives

Convert personal experience, Prompts, SOPs, templates, and Checklists into reusable departmental Skills. Engineering / IT teams use Antigravity to build Agentic Developer Skills so that Agents can assist with planning, development, testing, documentation, and cloud deployment.

### Course Outline

1. Definition of Skill AI: from personal know-how to departmental capability.
2. Skill structure: purpose, applicable scenarios, inputs, steps, outputs, acceptance criteria.
3. Antigravity Foundation: Agent Manager, Editor, Browser, permissions and review policies.
4. Antigravity Builder: App prototype, unit test, README, walkthrough artifact.
5. Antigravity GCP: GCS, Pub/Sub, Cloud Run, Gemini, BigQuery serverless pipeline PoC.
6. Claude Code: assisting with documentation, specifications, code, and knowledge work.
7. Codex: code, data processing, document automation, and process prototypes.
8. Skill Library management: versioning, Owner, examples, quality checks.
9. L2-to-L3 Bridge: trigger, input/output schema, n8n node map, human gate, log, error handling.

### Hands-on Exercises

- Build a "Copy Generation Skill."
- Build a "Customer Meeting Summary Skill."
- Build an "Anomalous Order Analysis Skill."
- Convert an existing SOP into an AI-executable Skill template.
- Use Antigravity to build an app prototype.
- Use Antigravity to generate unit tests, README, and walkthrough evidence.
- Engineering classes may additionally build a GCP serverless pipeline PoC.
- In the second half, convert one Skill into an L3 Workflow Blueprint.
- Define sample payload, n8n node map, human review, and Log.

### Post-class Deliverables

- Department Skill list.
- 3-5 demonstrable Skills.
- Standard Skill template.
- Skill Library maintenance rules.
- Antigravity app prototype / test / docs artifacts.
- GCP Pipeline PoC and deployment verification records.
- L3 Workflow Blueprint.
- Trigger / I/O schema / sample payload.
- n8n node map, human gate, log, error handling spec.
- L3 Workflow candidate list.

### Instructor Notes

L2 is the pivot of the entire solution. Without L2, L3 degenerates into mere tool integration; with L2, Workflows can carry departmental knowledge. The second half of L2 must connect to L3 by converting Skills into Workflow Blueprints. If the customer is an IT, R&D, software, or digital team, `L2_ANTIGRAVITY_COURSE_PLAN.md` should be incorporated to convert the three Google Antigravity codelabs into engineering Skill training.

## 5. L3 Workflow AI: n8n

### Course Objectives

Use n8n to connect Gmail, Sheets, Notion, CRM, APIs, ERP, LINE, Facebook, YouTube, Data Tables, and other systems so that AI begins to enter processes and complete tasks that are verifiable, operable, and backed up.

### Course Outline

1. n8n core concepts: Trigger, Node, Credential, Webhook, Execution.
2. Taking over the L2 Blueprint: trigger, I/O schema, sample payload, node map.
3. Gmail / LINE / Facebook / YouTube / Webhook integration.
4. Google Sheets / Data Tables / Notion integration: data logging, state management, task creation.
5. CRM / API / ERP integration: customer, order, inventory, shipping, procurement, and finance data.
6. Gemini / AI Node / RAG / multimodal applications.
7. Sub-workflow modularization and reusable process templates.
8. GitHub backup, Credential management, Execution Log.
9. Error handling, human review, permissions, and operations.

### Hands-on Exercises

- Classify Gmail customer complaints and write them into Sheets.
- Auto-create a Notion task after a form submission.
- Generate a visit summary after a CRM customer lookup.
- Turn ERP anomalous order data into an executive summary.
- Notify the owner when an n8n execution fails.
- Facebook / LINE customer service Webhook + Data Tables + AI reply draft.
- HR resume screening: Gmail + Gemini + LINE / Email notification.
- Sub-workflow modularization and GitHub backup.

### Post-class Deliverables

- 1-2 n8n Workflow PoCs.
- System integration requirements list.
- Credential and permissions list.
- Data Tables Schema.
- Sub-workflow Library.
- Human review node design.
- GitHub Backup / version management SOP.
- L4 Workflow Contract.
- L4 Agent task candidate list.

### Instructor Notes

Even within L3, different industries call for different cases. Marketing and services firms can quickly showcase ROI using SaaS, social platforms, and Webhooks; customer service can use Facebook / LINE + Data Tables; HR can use Gmail + Gemini + notifications; R&D and manufacturing firms must prioritize ERP, internal APIs, data permissions, and human review. The full L3 design is documented in `L3_N8N_TIGERAI_COURSE_PLAN.md`.

## 6. L4 Auto Agentic AI: Hermes Agent

### Course Objectives

Enable Hermes Agent to form a sustainably operating knowledge-work loop: it can read departmental purpose and schema, ingest documents, build Wiki memory, call L2 Skills and L3 Workflows, generate briefings, and be validated through evidence and human Gates.

### Course Outline

1. Agentic AI concepts: differences between Agent and Chatbot / Skill / Workflow.
2. Hermes architecture: Wiki, SQLite, skills, tools, runtime schema, policy.
3. Orient-first: before working, the Agent first reads purpose, schema, INBOX, queue, watchlist, index, and log.
4. Ingest / query / update: document ingestion, source analysis, cited answers, write-back of results.
5. Briefing / discovery: morning briefing, 2h ping, watchlist, P2 queue.
6. Tool Calling: invoking Skills, n8n Workflows, APIs, and databases.
7. Agent task card: role, permissions, available tools, constraints, reporting format.
8. Human review, Stage Gate, Log, failure handling, and continuous improvement.

### Hands-on Exercises

- Design an "Operations Weekly Report Agent."
- Design a "Customer Service Case Summary Agent."
- Design a "Sales Visit Preparation Agent."
- Design an "R&D Literature / Technical Document Organization Agent."
- Draft `purpose.md` and `SCHEMA.md`.
- Ingest a PDF / SOP / FAQ and produce source analysis and log.
- Produce a morning briefing.
- Have the Agent call an n8n Workflow.

### Post-class Deliverables

- Hermes Agent role card.
- L4 IPOE table.
- Initial Wiki structure.
- Agent task list.
- Agent available-tools list.
- Ingest / Query / Update test records.
- Briefing template.
- Permissions and review rules.
- Gate 4A-4E acceptance sheet.
- L5 Agent Team candidate scenarios.

### Instructor Notes

L4 should not promise fully automated decision-making out of the gate. A better positioning is: "Let the Agent handle preparation, analysis, organization, reminders, drafts, and briefings; keep critical decisions, deletions, schema changes, and high-risk updates behind a human Gate." The full L4 design is documented in `L4_HERMES_AGENT_COURSE_PLAN.md`.

## 7. L5 Agentic Team AI: ClawTeam

### Course Objectives

Compose multiple specialist Agents into an AI Team that collaboratively executes cross-functional, enterprise-grade tasks.

### Course Outline

1. Concepts of Multi-Agent collaboration.
2. Agent role design: market, product, marketing, customer service, finance, project integrator.
3. Task dispatch and output integration.
4. Quality assurance: Reviewer, Critic, human Gate.
5. Agent Team governance: permissions, data, Log, ROI.
6. Executive-level scenario drills.

### Hands-on Exercises

- New product launch Agent Team.
- Customer engagement strategy Agent Team.
- Operational anomaly analysis Agent Team.
- Annual planning draft Agent Team.

### Post-class Deliverables

- ClawTeam scenario design.
- Agent role cards.
- Multi-Agent collaboration flowchart.
- Final output template.
- Agent Team governance recommendations.

### Instructor Notes

The customer-facing language for L5 should emphasize management value rather than technical detail. The focus is: "The AI Team supports cross-functional decision-making and pre-execution preparation."

## 8. Course Ratio Configuration

| Customer State | Suggested Ratio | Course Focus |
| --- | --- | --- |
| AI beginner enterprise | L1 40%, L2 35%, L3 20%, L4 5%, L5 0% | Establish gateway, usage policy, Prompts and Skills |
| Personal AI adoption exists | L1 30%, L2 35%, L3 25%, L4 10%, L5 0% | Turn personal know-how into departmental capability |
| Departmental Skills exist | L1 15%, L2 30%, L3 40%, L4 10%, L5 5% | Stitch Skills into Workflows |
| Workflows already exist | L1 5%, L2 20%, L3 35%, L4 30%, L5 10% | Upgrade Workflows into Agents |
| Agent foundation exists | L1 5%, L2 15%, L3 25%, L4 30%, L5 25% | Agent Team and governance |

## 9. Impact of Deployment Mode on the Course

| Deployment Mode | Course Adjustments |
| --- | --- |
| Cloud AI | More L1/L2 weight; cases use Gmail, Sheets, Notion, CRM to demonstrate efficiency quickly |
| Hybrid | More L3 weight; cases add data classification, SaaS + internal APIs, ERP, and human review |
| Fully on-premises | More weight on governance, internal systems, on-premises models, RAG, ERP/DB/APIs, logging, and audit |

## 10. Industry Case Mapping

| Industry | Priority Cases | Recommended Focus |
| --- | --- | --- |
| R&D / Manufacturing | ERP anomalous orders, quality analysis, SOP lookup, 8D/5Why customer complaints | Hybrid / fully on-premises, L2-L3, permissions and audit |
| Marketing / Services | Proposals, copywriting, competitive analysis, CRM updates, campaign reports | Cloud AI / Hybrid, L1-L3 rapid PoC |
| Finance / Healthcare / Government | Document summarization, internal knowledge lookup, report assistance, human-review workflows | Fully on-premises / strict Hybrid, governance first |
| B2B Sales | Customer research, visit summaries, opportunity updates, proposal generation | L1-L3, CRM and Email integration |
| IT / Systems Department | API integration, permission governance, Log, process operations | L3-L4, governance and operations |
