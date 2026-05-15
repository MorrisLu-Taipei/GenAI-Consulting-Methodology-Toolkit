> 🌐 中文版本 / Chinese version: [CASE_CONTROL_TABLES.md](CASE_CONTROL_TABLES.md)

# Case Control Tables: Evaluation, L1-L5 IPOE, Evidence, and Stage Gate

Last updated: 2026-05-13

## 1. Purpose

This document provides control tables that consultants can copy directly into every client case.

The control tables ensure that a case is not merely a story, but is traceable across:

> Which evaluations were performed first → what input is consumed at each of L1-L5 → what process is executed → what output is produced → which evidence proves it → which Stage Gate determines whether to advance to the next stage

Every client case should fill in at least the following seven tables:

1. Case Intake control table.
2. Evaluation Activities control table.
3. L1-L5 IPOE control table.
4. Evidence control table.
5. Stage Gate control table.
6. Risk and Governance control table.
7. Deliverables Acceptance control table.

## 2. Case Intake Control Table

| Field | Content to Fill | Example |
| --- | --- | --- |
| Client name | `[Client Company]` | ABC Hospital |
| Industry | `[Industry]` | Healthcare |
| Employee / user scale | `[Headcount]` | 1,500 people |
| Primary departments | `[Departments]` | Customer service, medical administration, IT |
| Primary systems | `[Systems]` | HIS, EMR, customer service system, Email |
| Data sensitivity | `[Low / Medium / High / Critical]` | Critical |
| Initial deployment model | `[Cloud AI / Hybrid / Fully On-Premises]` | Fully on-premises or strict Hybrid |
| Primary business goal | `[Goal]` | Reduce time spent handling repetitive customer service questions |
| Primary risks | `[Risks]` | PII leakage, incorrect medical advice |
| First-wave PoC candidate | `[Scenario]` | Patient services FAQ Workflow |

## 3. Evaluation Activities Control Table

| Evaluation Phase | Purpose | Input | Method | Output | Owner | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Questionnaire diagnosis | Determine maturity | 10-item / 25-item questionnaire | Online survey / interview-based completion | Initial maturity assessment | Consulting | Raw questionnaire data, scoring table | `[ ]` |
| Company profile survey | Determine industry and deployment model | Company data, system list | Interviews / forms | Company profile table | Consulting + client contact | Survey form | `[ ]` |
| Data sensitivity assessment | Determine usable data scope | Data inventory | Data classification workshop | Data classification table | IT / Compliance | Data classification document | `[ ]` |
| System inventory | Identify integrable systems | System list, API docs | IT interviews | System inventory table | IT | System list, API docs | `[ ]` |
| As-Is process inventory | Identify rework and bottlenecks | Process status | Workshops / interviews | As-Is Process Map | Department Owner | Process diagrams, interview notes | `[ ]` |
| Scenario screening | Select PoCs | Pain point list, system inventory | Impact x Effort | PoC scenario list | Consulting + management | Priority matrix | `[ ]` |
| Governance assessment | Mitigate adoption risk | Permission, log, and review requirements | IT / Compliance interviews | Governance requirements table | IT / Compliance | Permission table, review rules | `[ ]` |

## 4. L1-L5 IPOE Control Table

IPOE = Input / Process / Output / Evidence.

| Maturity | Input | Process | Output | Evidence | Owner | Acceptance Criteria | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L1 Controlled AI Access | `[Documents, Email, questionnaires, low-sensitivity data]` | `[OpenWebUI, Prompt training, usage guidelines]` | `[Prompts, AI usage guidelines, entry-point workflow]` | `[Screenshots, guideline documents, exercise outputs]` | `[HR / IT / Consulting]` | `[Seed users can complete basic tasks]` | `[ ]` |
| L2 Knowledge Codification | `[SOPs, templates, senior expertise, examples]` | `[Skill design, templatization, version management]` | `[Skill Library, 3-5 Skills]` | `[Skill documents, versions, test outputs]` | `[Department Owner]` | `[Non-original authors can use the Skill]` | `[ ]` |
| L3 Workflow Automation | `[Gmail, Sheets, Notion, CRM, API, ERP]` | `[n8n integration, triggers, AI classification, human review, logging]` | `[Workflow PoC, summaries, tasks, notifications]` | `[Workflow JSON, Execution Log, test cases]` | `[IT / Process Owner]` | `[Test cases succeed with review in place]` | `[ ]` |
| L4 Autonomous Agent | `[Skills, Workflows, tasks, documents, Wiki, schema, permissions]` | `[Hermes Agent orient, ingest, query, update, briefing, tool invocation, human Gate]` | `[Agent task card, Wiki pages, briefing, reports, follow-up list]` | `[Logs, SQLite queries, source pages, tool invocation records, human review records]` | `[Department Owner / IT]` | `[Agent output is traceable, auditable, and operable]` | `[ ]` |
| L5 Multi-Agent Organization | `[Cross-departmental tasks, roles, data sources]` | `[ClawTeam multi-Agent division, integration, review]` | `[Integrated report, improvement proposals, Roadmap]` | `[Outputs from each Agent, integration record, executive review]` | `[Management Sponsor]` | `[Role division, human Gate, and ROI in place]` | `[ ]` |

## 5. Detailed L1-L5 Control Tables

### 5.1 L1 Controlled AI Access Control Table

| Control Item | Content to Fill | Evidence | Completed |
| --- | --- | --- | --- |
| AI entry point | `[OpenWebUI / approved tool]` | Tool screenshots, URL, account list | `[ ]` |
| Personal accounts | `[Per-trainee account]` | Account list, login screenshots | `[ ]` |
| Personal chat area | `[Chat / history / folders]` | User operation screenshots | `[ ]` |
| Admin management | `[Admin / User / Pending]` | Admin Panel screenshots | `[ ]` |
| Group permissions | `[Departments / seed teams / Power Users]` | Groups / Permissions table | `[ ]` |
| Model and feature controls | `[Models, files, Web Search, Tools, sharing]` | Model access / feature permission table | `[ ]` |
| Audience | `[Seed users / departments]` | Roster, sign-in sheet | `[ ]` |
| Allowed input data | `[Data types]` | Data classification table | `[ ]` |
| Prohibited input data | `[Data types]` | AI usage guidelines | `[ ]` |
| Prompt templates | `[Template list]` | Prompt Library | `[ ]` |
| Training exercises | `[Exercises]` | Trainee outputs | `[ ]` |
| L1 Gate | `[Pass / Fail]` | Gate 1 acceptance record | `[ ]` |

### 5.2 L2 Knowledge Codification Control Table

| Control Item | Content to Fill | Evidence | Completed |
| --- | --- | --- | --- |
| Skill name | `[Skill]` | Skill document | `[ ]` |
| Skill Owner | `[Person / department]` | Owner roster | `[ ]` |
| Input definition | `[Data / documents / examples]` | Skill template | `[ ]` |
| Process definition | `[Steps]` | Skill template | `[ ]` |
| Output definition | `[Format]` | Output sample | `[ ]` |
| Constraints | `[What must not be done]` | Skill template | `[ ]` |
| Test results | `[Results]` | Test input/output | `[ ]` |
| L2 Gate | `[Pass / Fail]` | Gate 2 acceptance record | `[ ]` |

### 5.3 L3 Workflow Automation Control Table

| Control Item | Content to Fill | Evidence | Completed |
| --- | --- | --- | --- |
| Workflow name | `[Name]` | n8n Workflow | `[ ]` |
| Trigger | `[Email / Webhook / Schedule / Form]` | Node configuration screenshots | `[ ]` |
| Integrated systems | `[Gmail / Sheets / Notion / CRM / API / ERP]` | System integration list | `[ ]` |
| Credentials | `[Permission scope]` | Credential list | `[ ]` |
| AI processing nodes | `[Classify / summarize / draft / judge]` | Node configuration | `[ ]` |
| Human review nodes | `[Reviewer / condition]` | Review records | `[ ]` |
| Log | `[Logged content]` | Execution Log | `[ ]` |
| Error handling | `[Notification / retry / fallback]` | Test records | `[ ]` |
| L3 Gate | `[Pass / Fail]` | Gate 3 acceptance record | `[ ]` |

### 5.4 L4 Hermes Agent Control Table

| Control Item | Content to Fill | Evidence | Completed |
| --- | --- | --- | --- |
| Agent name | `[Name]` | Agent task card | `[ ]` |
| Agent goal | `[Goal]` | Agent task card | `[ ]` |
| Purpose | `[Why this Agent exists]` | `purpose.md` | `[ ]` |
| Schema | `[Knowledge fields and rules]` | `SCHEMA.md` | `[ ]` |
| Wiki structure | `[INBOX / queue / watchlist / tasks / wiki]` | Wiki file list | `[ ]` |
| Callable Skills | `[Skill list]` | Tool inventory | `[ ]` |
| Callable Workflows | `[Workflow list]` | Tool inventory | `[ ]` |
| Ingest test | `[Documents / SOPs / FAQs]` | Source pages, logs, index | `[ ]` |
| Query test | `[Query items]` | Query records, citation sources | `[ ]` |
| Update test | `[Write-back content]` | Update diff, review record | `[ ]` |
| Briefing | `[morning / weekly]` | Briefing report | `[ ]` |
| Discovery / Watchlist | `[Keywords]` | Watchlist, queue | `[ ]` |
| Accessible data | `[Data scope]` | Permission table | `[ ]` |
| Prohibited actions | `[Forbidden behaviors]` | Permission table | `[ ]` |
| Reporting format | `[Format]` | Output sample | `[ ]` |
| Human takeover | `[Conditions and owner]` | Takeover records | `[ ]` |
| L4 Gate | `[4A / 4B / 4C / 4D / 4E]` | Gate 4A-4E acceptance record | `[ ]` |

### 5.5 L5 ClawTeam Control Table

| Control Item | Content to Fill | Evidence | Completed |
| --- | --- | --- | --- |
| Team mission | `[Cross-departmental task]` | Task description | `[ ]` |
| Agent roles | `[Role list]` | Role cards | `[ ]` |
| Task assignment | `[Assignment rules]` | Task assignment table | `[ ]` |
| Per-Agent input | `[Data sources]` | Input list | `[ ]` |
| Per-Agent output | `[Outputs]` | Output samples | `[ ]` |
| Integration Agent | `[Role]` | Integration report | `[ ]` |
| Reviewer / Critic | `[Review role]` | Review records | `[ ]` |
| Human Gate | `[Reviewer]` | Sign-off records | `[ ]` |
| L5 Gate | `[Pass / Fail]` | Gate 5 acceptance record | `[ ]` |

## 6. Evidence Control Table

| Evidence Type | Applicable Maturity | Requirement | Example | Storage Location | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Raw questionnaire data | L1-L5 | Required | Google Form / Sheets | `[URL / Path]` | Consulting | `[ ]` |
| Maturity scoring sheet | L1-L5 | Required | L1-L5 scores | `[URL / Path]` | Consulting | `[ ]` |
| AI usage guidelines | L1 | Required | Allowed / prohibited data | `[URL / Path]` | IT / Consulting | `[ ]` |
| Prompt Library | L1 | Recommended | Frequently used Prompts | `[URL / Path]` | Department | `[ ]` |
| Skill Library | L2 | Required | 3-5 Skills | `[URL / Path]` | Department Owner | `[ ]` |
| Workflow JSON | L3 | Required | n8n Export | `[URL / Path]` | IT | `[ ]` |
| Execution Log | L3 | Required | n8n execution record | `[URL / Path]` | IT | `[ ]` |
| Human review records | L3-L5 | Required | Review forms / sign-off | `[URL / Path]` | Department Owner | `[ ]` |
| Agent task card | L4 | Required | Hermes Agent task card | `[URL / Path]` | Consulting / Department | `[ ]` |
| Hermes Wiki | L4 | Required | purpose, schema, INBOX, queue, watchlist, tasks | `[URL / Path]` | IT / Department | `[ ]` |
| Ingest / Query / Update records | L4 | Required | source page, query record, update diff | `[URL / Path]` | Consulting / IT | `[ ]` |
| Briefing templates | L4 | Recommended | morning / weekly briefing | `[URL / Path]` | Department Owner | `[ ]` |
| Agent execution records | L4 | Required | Tool invocation records, logs, SQLite queries | `[URL / Path]` | IT | `[ ]` |
| Agent Team role cards | L5 | Required | ClawTeam role cards | `[URL / Path]` | Consulting | `[ ]` |
| ROI tracking table | L3-L5 | Required | Work hours / error rate / response speed | `[URL / Path]` | Management Sponsor | `[ ]` |

## 7. Stage Gate Control Table

| Gate | Corresponding Maturity | Required Deliverables | Pass Criteria | Reviewer | Result | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Gate 1 | L1 | AI entry point, usage guidelines, Prompt templates | Seed users can complete basic AI tasks and understand data boundaries | HR / IT / Consulting | `[Pass / Fail]` | `[Notes]` |
| Gate 2 | L2 | Skill Library, Skill Owners, test outputs | Non-original authors can use the Skill to produce acceptable results | Department head / Consulting | `[Pass / Fail]` | `[Notes]` |
| Gate 3 | L3 | n8n Workflow, logs, human review | The Workflow runs test cases successfully with error handling | IT / Process Owner | `[Pass / Fail]` | `[Notes]` |
| Gate 4 | L4 | Hermes Agent task card, L4 IPOE, Wiki, permission table, tool list, logs, briefing | The Agent can perform ingest/query/update, invoke Skills / Workflows, and produce traceable, auditable, operable output | Department head / IT | `[Pass / Fail]` | `[Notes]` |
| Gate 5 | L5 | ClawTeam role cards, task assignment, integration report | Multi-Agent has role division, integration, Reviewer, and human Gate | Management Sponsor | `[Pass / Fail]` | `[Notes]` |

## 8. Risk and Governance Control Table

| Risk Type | Description | Impact Level | Corresponding Control | Evidence | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Data leakage | Sensitive data entered into an unapproved AI | High | Data classification, prohibited-data list, controlled entry | AI usage guidelines | IT / Compliance | `[ ]` |
| Incorrect output | AI answer used directly without verification | Medium-High | Human review, source citation, confidence labeling | Review records | Department Owner | `[ ]` |
| Permission misuse | Agent queries or modifies data it should not | High | Permission table, least privilege, logging | Permission table, logs | IT | `[ ]` |
| Process failure | Workflow breaks down without notification | Medium | Error notification, retry, fallback | Execution Log | IT | `[ ]` |
| Unclear accountability | Unclear who reviews AI output | Medium | Owner / Gate / sign-off | RACI, review form | Management Sponsor | `[ ]` |
| Unclear ROI | Unable to demonstrate adoption value | Medium | KPI, before/after measurement, dashboard | ROI tracking table | Consulting / Department | `[ ]` |

## 9. Deliverables Acceptance Control Table

| Deliverable | Corresponding Stage | Required | Acceptance Criteria | Reviewer | Status |
| --- | --- | --- | --- | --- | --- |
| AI maturity questionnaire results | Diagnosis | Yes | Questionnaire completed and scorable | Consulting | `[ ]` |
| Company profile survey | Diagnosis | Yes | Industry, systems, data, deployment model are explicit | Consulting / client contact | `[ ]` |
| As-Is Process Map | Stage 1 | Yes | Department confirms the process is accurate | Department Owner | `[ ]` |
| Maturity evaluation report | Stage 2 | Yes | L1-L5 judgments and evidence are complete | Management Sponsor | `[ ]` |
| Scenario priority matrix | Stage 3-4 | Yes | Impact x Effort is explicit | Management Sponsor | `[ ]` |
| Executive Problem Statement | Stage 5 | Yes | Core problem expressed in one sentence and endorsed by management | Management Sponsor | `[ ]` |
| Stage Gate Criteria | Stage 6 | Yes | Acceptance criteria for each stage are explicit | Consulting / client contact | `[ ]` |
| To-Be Operating Model | Stage 7 | Yes | L1-L5 target architecture is complete | Management Sponsor / IT | `[ ]` |
| Transformation Roadmap | Stage 8 | Yes | 30 / 60 / 90 day tasks are clear | Management Sponsor | `[ ]` |
| ROI tracking matrix | Stage 8 | Yes | KPIs, measurement methods, and Owners are explicit | Management Sponsor | `[ ]` |
| Follow-on SOW recommendation | Stage 8 | No | Can be converted into a quotation or implementation project | Sales / Consulting | `[ ]` |

## 10. Case Completion Check

| Check Item | Completed |
| --- | --- |
| Questionnaire diagnosis completed | `[ ]` |
| Company profile and deployment model judgment completed | `[ ]` |
| As-Is process inventory completed | `[ ]` |
| L1-L5 IPOE control table completed | `[ ]` |
| Evidence control table completed | `[ ]` |
| Stage Gate control table completed | `[ ]` |
| Risk and governance control table completed | `[ ]` |
| Deliverables acceptance control table completed | `[ ]` |
| 30 / 60 / 90 day Roadmap completed | `[ ]` |
| ROI tracking matrix completed | `[ ]` |
