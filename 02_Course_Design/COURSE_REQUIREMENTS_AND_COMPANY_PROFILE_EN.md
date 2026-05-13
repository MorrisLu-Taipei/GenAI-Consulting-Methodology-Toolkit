> 🌐 中文版本 / Chinese version: [COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md](COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md)

# Course Requirements Checklist and Company Profile Survey

Last updated: 2026-05-13

## 1. Purpose

This document complements the AI maturity course design.

A course cannot be arranged solely around tools, nor solely around what the customer subjectively wants to learn. Every course design must simultaneously consult:

1. The requirements checklist for each L1-L5 maturity level.
2. The customer's company profile and industry type.
3. The AI deployment mode best suited to the customer: cloud AI, hybrid, or fully on-premises.
4. The customer's existing system landscape: Gmail, Sheets, Notion, CRM, APIs, ERP, databases, internal systems.
5. The customer's risk conditions: information security, personal data, trade secrets, regulations, and IT operations capability.

The ultimate goal is to ensure the course is not merely "teaching tools" but is aligned with an AI transformation path the customer can actually execute.

## 2. L1-L5 Course Requirements Checklist

### 2.1 L1 Chat AI: OpenWebUI

#### Suitable Customer State

- Employees have not yet adopted AI at scale.
- The company wants to establish a secure AI gateway first.
- Leadership wants to lift personal productivity first.
- IT wants to centrally manage models and usage policy.

#### Requirements Checklist

- Is a unified internal AI gateway needed?
- Are account, permission, and model management needed?
- Does every employee need to log in with their own account rather than a shared account?
- Does every employee need their own chat history, folders, and personal Prompts?
- Does the Admin need to approve new accounts and configure roles, groups, and department permissions?
- Is it necessary to restrict file uploads, Web Search, API Keys, Tools, and chat sharing?
- Is there data that must not be uploaded to the public cloud?
- Is an AI usage policy needed?
- Is foundational Prompt training needed?
- Are department-specific scenario templates needed?

#### Course Focus

- OpenWebUI personal usage: login, personal chat area, chat history, folders, model selection.
- OpenWebUI Admin: account approval, roles, groups, permissions, model and feature governance.
- Prompt fundamentals.
- Enterprise AI usage policy.
- Document summarization, meeting summaries, email drafts, report drafts.
- AI usage boundaries and data security.

#### Recommended Deliverables

- Personal high-frequency work Prompts.
- Department-wide sample Prompt templates.
- Account / group / permission / model visibility configuration sheet.
- OpenWebUI Admin Runbook.
- AI usage advisories.
- L2 Skill candidate list.

### 2.2 L2 Skill AI: Antigravity / Claude Code / Codex

#### Suitable Customer State

- Some staff already use AI, but methods are scattered across individuals.
- The department has SOPs, templates, documents, or experience that needs to be captured.
- New-hire training relies on word-of-mouth from senior colleagues.
- There is a desire to convert Prompts, processes, and documents into reusable Skills.
- IT / engineering teams want to use Antigravity to build app prototypes, tests, documentation, and GCP pipeline PoCs.

#### Requirements Checklist

- Which high-frequency tasks rely most heavily on senior personnel?
- Which tasks can be distilled into SOPs, Checklists, and Templates?
- Is there an existing departmental knowledge base?
- Is a Skill Library needed?
- Should non-engineering departments also maintain Skills?
- Should documents, code, and processes be formalized?
- Is Antigravity Agentic Developer training required?
- Are Agents needed to generate app prototypes, unit tests, READMEs, or deployment scripts?
- Does the customer have a GCP project, gcloud access, and cloud deployment needs?
- Should the engineering artifacts produced become capabilities callable by L3 Workflows or the L4 Hermes Agent?
- Which L2 Skills will be converted into L3 Workflow Blueprints in the second half?
- Are trigger conditions, input fields, output formats, human review, and Log already defined?

#### Course Focus

- Definition and design methodology of Skills.
- Structuring Prompts, SOPs, Templates, and Checklists.
- Skill construction with Antigravity / Claude Code / Codex.
- Antigravity Agentic IDE: Agent Manager, Editor, Browser, permissions and review policy.
- Antigravity Builder: App prototype, unit test, README, walkthrough artifact.
- Antigravity GCP: GCS, Pub/Sub, Cloud Run, Gemini, BigQuery pipeline PoC.
- L2-to-L3 Bridge: converting Skills into trigger, input/output schema, n8n node map, human gate, log, error handling.
- Department Skill Library management.
- Skill version management and acceptance criteria.

#### Recommended Deliverables

- Department Skill list.
- 3-5 demonstrable Skills.
- Standard Skill template.
- Antigravity app prototype, test records, and documentation artifacts.
- GCP serverless pipeline PoC and deployment verification records.
- L3 Workflow Blueprint.
- Trigger / I/O schema / sample payload.
- n8n node map, human gate, log, error handling spec.
- Skill maintenance rules.
- L3 Workflow candidate list.

### 2.3 L3 Workflow AI: n8n

#### Suitable Customer State

- The department already has Skills or SOPs, but manual data movement remains.
- Work processes span multiple systems.
- Customer data, emails, spreadsheets, tasks, and ERP data are scattered.
- The goal is to let AI enter the workflow, not just answer questions.

#### Requirements Checklist

- Is Gmail or another corporate mail system in use?
- Are Google Sheets or Excel used as working spreadsheets?
- Is Notion used for tasks or as a knowledge base?
- Is there a CRM system?
- Is there an ERP system?
- Are there internal APIs available for integration?
- Are integrations required with LINE, Facebook, YouTube, Meta, GCS, GitHub, or similar platforms?
- Are there databases or vector databases?
- Are n8n Data Tables needed to persist state or interaction history?
- Are Sub-workflows needed to build reusable process templates?
- Do Workflows / Credentials need to be backed up to GitHub or an internal repository?
- Which processes have fixed trigger conditions?
- Which processes require human review?
- Which processes need notifications or retries on failure?

#### Course Focus

- n8n fundamentals.
- Triggers, Webhooks, Credentials, Nodes.
- Integration with Gmail, Sheets, Notion, CRM, APIs, ERP.
- Integration with LINE, Facebook, YouTube, Webhooks, Data Tables.
- Data cleansing and format conversion.
- Gemini, AI Node, RAG, multimodal applications.
- Sub-workflow modularization.
- Human review nodes.
- GitHub backup, Credential management, error handling, Log, and operations.

#### Recommended Deliverables

- 1-2 Workflow PoCs.
- System integration requirements list.
- Permissions and Credential list.
- Data Tables / Sheets / DB Schema.
- Sub-workflow Library.
- Human review and exception handling rules.
- GitHub Backup / version management SOP.
- L4 Workflow Contract.
- L4 Agent task candidate list.

### 2.4 L4 Auto Agentic AI: Hermes Agent

#### Suitable Customer State

- Callable Skills or Workflows already exist.
- Management wants AI to decompose tasks automatically.
- Users do not want to know how each system operates; they only want to issue tasks.
- AI is needed to assist with analysis, aggregation, execution, and reporting.
- Documents, SOPs, research, FAQs, tasks, and briefings should be converted into a continuously accumulating knowledge foundation.

#### Requirements Checklist

- Which roles need a personal or function-specific AI assistant?
- Which Skills can the Agent call?
- Which n8n Workflows can the Agent trigger?
- What content should the Agent's Wiki memory store?
- How are the Agent's `purpose.md` and `SCHEMA.md` defined?
- Who maintains the Agent's watchlist, queue, tasks, and briefing?
- Which tasks can be auto-completed?
- Which tasks must be human-confirmed?
- What are the Agent's permission boundaries?
- What are the Agent's output format and reporting cadence?
- Who handles Agent errors?
- Which evidence demonstrates that the Agent's output is traceable?

#### Course Focus

- Agentic AI concepts.
- Hermes Agent architecture: Wiki, SQLite, skills, tools, runtime schema.
- Orient-first, ingest, query, update, lint, briefing, discovery.
- Task decomposition.
- Tool Calling.
- Calling Skills and Workflows.
- Agent task boundaries.
- Permissions, review, Log, evidence, reporting, failure handling.

#### Recommended Deliverables

- Agent role card.
- L4 IPOE table.
- Initial Wiki structure with `purpose.md` / `SCHEMA.md`.
- Agent task list.
- Agent available-tools list.
- Agent permission sheet.
- Ingest / Query / Update test records.
- Briefing template.
- Gate 4A-4E acceptance sheet.
- L5 Agent Team candidate scenarios.

### 2.5 L5 Agentic Team AI: ClawTeam

#### Suitable Customer State

- Multiple Agents or cross-functional AI use cases already exist.
- The enterprise wants AI to support complex tasks such as new products, strategy, operational analysis, and cross-functional projects.
- Leadership wants AI to enable multi-role collaboration rather than single-point tools.

#### Requirements Checklist

- Which tasks require collaboration among multiple specialist roles?
- Which Agent roles are needed?
- What are each Agent's inputs, outputs, and permissions?
- Which Agent is responsible for integration?
- Which data sources require shared access?
- How is quality assurance performed?
- How are human review and final decisions handled?
- How is the Agent Team's ROI tracked?

#### Course Focus

- Multi-Agent collaboration.
- Agent role division.
- Task dispatch.
- Output integration.
- Quality assurance.
- Executive-level scenario drills.

#### Recommended Deliverables

- Agent Team scenario design.
- Agent role cards.
- Multi-Agent collaboration flowchart.
- Final output template.
- Agent Team governance recommendations.

## 3. Company Profile Survey

### 3.1 Basic Company Information

| Survey Item | Description |
| --- | --- |
| Industry type | R&D / manufacturing, marketing / services, finance, healthcare, education, government, retail, other |
| Headcount | Affects course scale, account management, and rollout cadence |
| Departmental structure | Sales, customer service, marketing, operations, R&D, manufacturing, finance, HR, IT |
| Primary systems | Gmail, Google Workspace, Microsoft 365, Notion, CRM, ERP, MES, PLM, internal systems |
| IT team capability | Whether they can operate servers, Docker, APIs, databases, and permissions |
| Current AI usage | None, personal usage, departmental usage, automated workflows, Agents |
| Leadership objectives | Efficiency, cost, quality, revenue, innovation, governance, information security |

### 3.2 Data and Risk Profile

| Survey Item | Low Risk | Medium Risk | High Risk |
| --- | --- | --- | --- |
| Data sensitivity | Public data, general documents | Customer data, internal SOPs | R&D secrets, personal data, finance, contracts |
| Regulatory requirements | No special requirements | Personal data or contract constraints | Finance, healthcare, government, listed-company high-control regimes |
| Cloud policy | Public cloud allowed | Some data may go to the cloud | Core data forbidden from the cloud |
| System openness | SaaS tools dominate | Some internal systems exist | ERP, MES, intranet, legacy systems dominate |
| IT operations capability | No dedicated IT | IT exists but resource-constrained | Established infrastructure and information-security teams |

### 3.3 Industry-AI Fit

#### R&D and Manufacturing

Common characteristics:

- ERP, MES, PLM, QMS, and internal databases are prevalent.
- High data sensitivity involving BOM, processes, quality, customer specifications, and R&D documents.
- Processes are highly standardized but systems are relatively closed.

Recommended priority scenarios:

- ERP anomalous order analysis.
- Quality issue summaries.
- SOP / WI document lookup.
- Equipment maintenance record organization.
- R&D document summarization.
- Customer complaint and 8D / 5Why analysis.

Recommended adoption cadence:

- Start with the L1 controlled gateway and L2 knowledge capture.
- Then implement L3 controlled integration with internal systems or ERP.
- L4/L5 must reinforce permissions, review, and audit logging.

Deployment preferences:

- Most lean toward hybrid or fully on-premises.
- If cloud AI is used, data must first be classified and sensitive information masked.

#### Marketing and Services

Common characteristics:

- Heavy use of Gmail, Sheets, Notion, CRM, social platforms, and advertising platforms.
- Fast data flow and high content-generation demand.
- High acceptance of cloud SaaS.

Recommended priority scenarios:

- Customer proposal generation.
- Market and competitive research.
- Social and advertising copy.
- Customer meeting summaries.
- CRM opportunity updates.
- Campaign performance reports.

Recommended adoption cadence:

- L1 can be rolled out broadly and quickly.
- L2 prioritizes capturing copy, proposals, research, and customer service Skills.
- L3 rapidly integrates Gmail, Sheets, Notion, and CRM.
- L4/L5 can be applied to proposals, marketing planning, and project management.

Deployment preferences:

- Most can adopt cloud AI or hybrid.
- For handling confidential customer presentations or contracts, switch to hybrid or private models.

#### Finance, Healthcare, Government, and Highly Sensitive Sectors

Common characteristics:

- Highly sensitive data.
- High requirements for permissions, audit, regulation, and data retention.
- Slower adoption, but explicit governance needs.

Recommended priority scenarios:

- Internal knowledge lookup.
- Document summarization.
- Form and report assistance.
- Workflow automation on non-sensitive data.
- Human-review-style Agents.

Recommended adoption cadence:

- Start with a fully on-premises or strictly hybrid architecture.
- L1 requires explicit data classification.
- L2 requires an auditable Skill Library.
- L3 requires complete Logs, permissions, and human review.
- L4/L5 should focus on decision support; do not pursue fully automated decisions at the outset.

Deployment preferences:

- Most lean toward fully on-premises or strict hybrid.

## 4. AI Deployment Mode Survey

### 4.1 Cloud AI

#### Suitable State

- Limited budget, wants to start quickly.
- Low data sensitivity or can be anonymized.
- Primarily marketing, copywriting, research, and general knowledge work.
- Limited IT operations capability.

#### Advantages

- Lowest cost.
- Fastest start.
- Strong model capability.
- Low operational burden.

#### Risks and Limitations

- Concerns over data egress.
- Permissions and audit depend on the vendor.
- Unsuitable for handling core confidential data.

#### Course Notes

- Increase weight on L1 and L2.
- L3 can first integrate SaaS tools.
- L4/L5 must explicitly limit which data can be used.

### 4.2 Hybrid: Cloud + On-premises

#### Suitable State

- Some data can go to the cloud while other data must remain internal.
- Wants to balance model capability and data security.
- Needs to integrate with internal ERP, CRM, databases, or APIs.
- Has basic IT operations capability.

#### Advantages

- High flexibility.
- Routing by data sensitivity is possible.
- Balances cost and security.
- Suits most enterprises in their first landing phase.

#### Risks and Limitations

- More complex architecture design.
- Requires data classification and routing rules.
- Requires Credential, permission, and Log management.

#### Course Notes

- L1 must teach data classification.
- L2 must build a controlled Skill Library.
- L3 is the focal point, especially n8n integration and data routing.
- L4/L5 can start with human-review tasks first.

### 4.3 Fully On-premises

#### Suitable State

- Core data must not leave the company.
- High information security, regulatory, and audit requirements.
- Has an internal IT or infrastructure team.
- Requires private models, intranet deployment, and on-premises RAG.

#### Advantages

- Highest data control.
- Suitable for highly sensitive scenarios.
- Deep integration with internal systems is possible.

#### Risks and Limitations

- Higher upfront cost.
- Model capability, hardware resources, and operational capability are constraints.
- Longer adoption cycle.

#### Course Notes

- L1 must introduce OpenWebUI and private-model usage policy.
- L2 must strengthen internal knowledge and document governance.
- L3 must accompany internal APIs, ERP, databases, and permissions.
- L4/L5 must have strict review, Logs, permissions, and fallback workflows.

## 5. Course Configuration Decision Rules

### 5.1 Determine Maturity First, Then Deployment Mode

The same L3 n8n course is taught differently depending on company profile:

- Cloud AI customers: focus on quickly integrating Gmail, Sheets, Notion, and CRM.
- Hybrid customers: focus on data classification and integration of SaaS with internal APIs.
- Fully on-premises customers: focus on intranet deployment, ERP, DB, permissions, and audit.

### 5.2 Industry Drives Case Selection

R&D and manufacturing:

- Cases should focus on ERP, quality, processes, SOPs, and customer complaint analysis.
- L3/L4 courses must emphasize permissions, internal systems, and human review.

Marketing and services:

- Cases should focus on proposals, copywriting, CRM, social media, and campaign reports.
- L1/L2/L3 can advance quickly; L4/L5 can serve multi-role planning.

Highly sensitive industries:

- Cases should avoid sending sensitive data directly to the cloud.
- The course must emphasize governance, data classification, audit, and human decision-making.

### 5.3 Recommended Course Design Workflow

1. Start with the AI maturity questionnaire.
2. Then conduct the company profile survey.
3. Determine the deployment mode: cloud AI, hybrid, or fully on-premises.
4. Determine industry case direction.
5. Produce the L1-L5 course ratio.
6. Produce hands-on exercises and PoC topics.
7. After class, feed the deliverables into the eight-stage consulting diagnostic report.

## 6. Draft Survey Items for the Company Profile

### 6.1 Deployment and Information Security

1. Does the company allow employees to use public-cloud AI tools to process work data?
2. Is there data that must not leave the corporate intranet?
3. Are there personal data, contracts, R&D, finance, or customer confidential data?
4. Is there an existing data classification regime?
5. Must AI usage records and audit logs be retained?
6. Is there an internal IT team able to maintain Docker, databases, APIs, or servers?

### 6.2 Systems and Data

1. Which collaboration tools does the company primarily use?
2. Is Gmail or Microsoft 365 in use?
3. Are Google Sheets, Excel, or internal reporting systems in use?
4. Are Notion, Confluence, SharePoint, or an internal knowledge base in use?
5. Is a CRM in use?
6. Are ERP, MES, PLM, QMS, or other core systems in use?
7. Are there internal APIs?
8. Are there databases or data warehouses?

### 6.3 Industry and Scenarios

1. What is the company's primary industry type?
2. Which departments need AI the most?
3. Which tasks are the most repetitive?
4. Which tasks rely most on senior personnel?
5. Which processes most frequently fail or are delayed?
6. Which reports are the most time-consuming?
7. Which ROI does leadership most want to see?

## 7. Consultant Notes

- Even when a customer only wants to buy a course, a lightweight company profile survey is still required to keep the cases close to their reality.
- Cloud AI is the cheapest, but not necessarily the most suitable for every enterprise.
- Hybrid is usually the most pragmatic first-phase option for most enterprises.
- Fully on-premises should not be recommended to all customers from the start; it should be evaluated against data sensitivity, IT capability, and budget.
- R&D and manufacturing typically need stronger emphasis on data permissions, ERP/MES/internal systems, and review workflows.
- Marketing and services can usually move faster from L1/L2 to L3/L4 and more easily showcase short-term ROI.
- The course ratio should be jointly determined by "maturity + company profile + deployment mode + industry scenario."

