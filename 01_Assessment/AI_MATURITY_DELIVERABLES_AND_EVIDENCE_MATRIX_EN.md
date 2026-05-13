# AI Maturity Deliverables, Evidence, and Stage Gate Master Matrix

> 🌐 中文版本 / Chinese version: [AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md](AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)

Version: v1.0  
Author: Morris Lu (盧業興) · Tiger AI 虎智科技  
Purpose: Convert the L1-L5 maturity theory into a consulting control matrix that is deliverable, acceptance-ready, and able to determine whether a level may proceed to the next stage.

---

## 1. Purpose of Use

An AI maturity model cannot simply describe "capability levels"; it must be able to answer:

1. When this level is completed, what should the customer have in hand?
2. What evidence proves it is not merely verbal completion?
3. Who is responsible for maintenance and review?
4. Which conditions indicate a fail?
5. Once passed, which next level can be entered?

Therefore, this matrix uses a fixed format:

`Level → Definition of Done → Deliverables → Evidence → Owner → Stage Gate → Fail Condition → Next Level Entry Criteria`

---

## 2. L1-L5 Master Matrix

| Level | Maturity Positioning | Definition of Done | Core Deliverables | Required Evidence | Primary Owner | Stage Gate | Next Level |
|---|---|---|---|---|---|---|---|
| L1 | Chat AI / OpenWebUI | The company has a controlled AI portal; each user can log in with their own account and complete basic knowledge work | OpenWebUI accounts/groups/permissions table, personal chat area, Prompt Library, AI usage guidelines | Login screenshots, personal chat screenshots, Admin Panel, permissions table, Prompt exercises, data case judgment | IT / HR / Consultant | Gate 1A-1F | L2 Skill AI |
| L2 | Skill AI / Antigravity / Claude Code / Codex | Personal experience, SOPs, Prompts, and engineering implementations can be consolidated into reusable Skills and converted into an L3 Blueprint | Skill Library, Skill template, Owner/version table, Antigravity artifacts, Workflow Blueprint | Skill test outputs, version records, Owner list, sample payload, n8n node map | Department Owner / IT / Consultant | Gate 2A-2F | L3 Workflow AI |
| L3 | Workflow AI / n8n | At least one workflow runs stably, with system integration, human review, Log, error handling, and backup | n8n Workflow JSON, Data Tables Schema, Sub-workflow Library, GitHub Backup SOP, L4 Workflow Contract | Execution Log, test payloads, Data Tables / Sheets records, backup commit, human review records, failure tests | IT / Process Owner | Gate 3A-3G | L4 Hermes Agent |
| L4 | Auto Agentic AI / Hermes Agent | Agent can use Wiki memory as a base to complete ingest/query/update/briefing and can call L2 Skill / L3 Workflow | Hermes Agent task card, L4 IPOE, Wiki, schema, ingest/query/update records, briefing, Runbook | Source page, SQLite query, log, briefing, tool invocation records, human review, Gate 4A-4E | Department Owner / IT | Gate 4A-4E | L5 ClawTeam |
| L5 | Agentic Team AI / ClawTeam | Multiple Agents have role assignment, task dispatch, integrated output, Reviewer, human Gate, and ROI measurement | ClawTeam role cards, task dispatch table, Agent Team IPOE, integrated report, Reviewer Gate, ROI table | Per-Agent outputs, integration records, Reviewer records, executive sign-off, ROI/KPI tracking | Management Sponsor / Consultant | Gate 5 | Institutionalization and expansion |

---

## 3. L1 Chat AI: OpenWebUI

### 3.1 Definition of Done

L1 completion is not "employees can ask AI questions" — it is:

- Every user has their own OpenWebUI account.
- Every user has their own chat area, history, folders, and personal Prompts.
- The Admin can manage accounts, roles, groups, permissions, models, and features.
- The company has AI usage guidelines and data-input boundaries.
- Users can complete basic knowledge work, such as summaries, emails, meeting notes, and report drafts.

### 3.2 Deliverables

| Deliverable | Required | Description |
|---|---|---|
| OpenWebUI user manual | Yes | Login, chat, models, documents, Prompt, data boundary |
| Account list | Yes | Each learner has an independent account; no shared accounts |
| Group and permissions table | Yes | Roles, groups, model visibility, feature permissions |
| Admin Runbook | Yes | Account approval, groups, models, features, sharing, data guidelines |
| Prompt Library v1 | Yes | Personal and departmental common Prompts |
| AI usage guidelines | Yes | What may be input, what is prohibited, what requires human confirmation |
| High-frequency work list | Yes | Source for L2 Skill candidates |

### 3.3 Evidence

- Login screenshot.
- Personal chat area screenshot.
- Admin Panel screenshot.
- Groups / Permissions configuration table.
- Prompt exercises.
- Data case judgment sheet.
- Gate 1 acceptance record.

### 3.4 Owner

| Item | Owner |
|---|---|
| OpenWebUI environment | IT |
| Accounts and permissions | IT / HR |
| AI usage guidelines | IT / HR / Compliance |
| Prompt Library | Department Owner |
| Gate 1 acceptance | Consultant + IT + HR |

### 3.5 Fail Conditions

- Users share accounts.
- Admin cannot manage roles, groups, and permissions.
- No data-input guidelines.
- Employees do not know which data must not be input to AI.
- No high-frequency work list produced.

### 3.6 Next Level Entry Criteria

Conditions to enter L2:

- At least 10 high-frequency work items have been consolidated.
- A Prompt Library v1 exists.
- Allowed-/prohibited-data guidelines exist.
- At least one seed cohort has completed the L1 exercises.

---

## 4. L2 Skill AI: Antigravity / Claude Code / Codex

### 4.1 Definition of Done

L2 completion is not "learners can use AI to write things" — it is:

- At least 3-5 Skills can be reused by someone other than the original author.
- Each Skill has input, process, output, constraints, and quality check.
- Each Skill has an Owner and a version.
- The engineering team can produce Antigravity app / test / docs artifacts.
- At least one Skill is converted into an L3 Workflow Blueprint.

### 4.2 Deliverables

| Deliverable | Required | Description |
|---|---|---|
| Skill Library | Yes | 3-5 reusable Skills |
| Skill template | Yes | IPOC / constraints / quality check |
| Skill Owner and version table | Yes | Maintenance responsibility and version history |
| Skill test records | Yes | At least 2 test input/output records |
| Antigravity artifacts | Customer-dependent | App prototype, unit test, README, deployment evidence |
| L3 Workflow Blueprint | Yes | Trigger, I/O schema, sample payload, node map, human gate, log, error handling |

### 4.3 Evidence

- Skill document.
- Test input/output.
- Owner list.
- Version history.
- Antigravity task / implementation / walkthrough artifact.
- Sample payload.
- n8n node map.
- Gate 2 acceptance record.

### 4.4 Owner

| Item | Owner |
|---|---|
| Skill content | Department Owner |
| Skill Library | Consultant / department liaison |
| Engineering artifact | IT / Engineering Owner |
| L3 Blueprint | Process Owner + IT |
| Gate 2 acceptance | Consultant + department manager |

### 4.5 Fail Conditions

- The Skill has only a Prompt; no input/process/output.
- Only the original author can use the Skill.
- No Owner or version.
- No test records.
- Not converted into an L3 Workflow Blueprint.

### 4.6 Next Level Entry Criteria

Conditions to enter L3:

- At least 1 Skill is selected as a workflow-ification candidate.
- Trigger, I/O schema, and sample payload are defined.
- An n8n node map is completed.
- Human gate, log, and error handling are defined.
- Required systems and credentials are inventoried.

---

## 5. L3 Workflow AI: n8n

### 5.1 Definition of Done

L3 completion is not "the Workflow demo runs once" — it is:

- The Workflow can handle both normal and error payloads.
- It integrates at least 2 systems or platforms.
- It has an AI processing step with verifiable output.
- It has a human-review Gate.
- It has Execution Log, error handling, and GitHub backup.
- It has an L4 Workflow Contract.

### 5.2 Deliverables

| Deliverable | Required | Description |
|---|---|---|
| n8n Workflow JSON | Yes | Importable/exportable workflow file |
| Workflow Blueprint | Yes | L2 handover document |
| Credential / API / Webhook permissions table | Yes | Permission scope and Owner |
| Data Tables / Sheets / DB Schema | Yes | Status and data records |
| Sub-workflow Library | Recommended | Reusable modules |
| Execution Log | Yes | Success, failure, rerun |
| Human Gate design | Yes | Reviewers, conditions, results |
| Error Handling / Retry / Fallback | Yes | Failure notifications and handling |
| GitHub Backup SOP | Yes | Workflow / Credential backup and versioning |
| L4 Workflow Contract | Yes | How Hermes Agent can call it |

### 5.3 Evidence

- n8n Execution Log.
- 2 normal payloads and 1 error payload.
- Node configuration screenshots.
- Data Tables / Sheets records.
- AI input/output.
- Human review records.
- GitHub backup commit.
- Failure test records.

### 5.4 Owner

| Item | Owner |
|---|---|
| Workflow design | Process Owner |
| n8n implementation | IT / automation staff |
| Credential | IT |
| Human Gate | Department manager |
| Backup / operations | IT |
| Gate 3 acceptance | IT + Process Owner + Consultant |

### 5.5 Fail Conditions

- The Workflow only runs on the instructor's laptop; the customer cannot reproduce it.
- No Execution Log.
- No error handling.
- No human review.
- Credential permissions unclear.
- No backup.
- No L4 Workflow Contract.

### 5.6 Next Level Entry Criteria

Conditions to enter L4:

- At least 1 Workflow runs stably.
- It can be called by Hermes Agent.
- Permission boundaries and output format are defined.
- Log, error handling, and human Gate exist.
- IT / Process Owner has maintenance responsibility.

---

## 6. L4 Auto Agentic AI: Hermes Agent

### 6.1 Definition of Done

L4 completion is not "there is one Agent demo" — it is:

- Hermes Agent has a clear task card and boundary.
- The Agent has Wiki memory and schema.
- The Agent can complete ingest, query, update, and briefing.
- The Agent can call L2 Skills and L3 Workflows.
- The Agent's output has evidence and a human Gate.
- The Agent has an operations Runbook.

### 6.2 Deliverables

| Deliverable | Required | Description |
|---|---|---|
| Hermes Agent task card | Yes | Role, task, constraints, data sources, tools |
| L4 IPOE table | Yes | Input/process/output/evidence |
| `purpose.md` / `SCHEMA.md` | Yes | Knowledge base and rules |
| Initial Wiki | Yes | INBOX, queue, watchlist, tasks, wiki pages |
| Ingest test records | Yes | At least 1 document |
| Query / Update test records | Yes | Can cite, can write back |
| Briefing template | Yes | Morning / weekly briefing |
| Gate 4A-4E table | Yes | Environment, knowledge, ingest, query/update, governance |
| Operations Runbook | Yes | Schedule, Owner, fallback, human handover |

### 6.3 Evidence

- `hermes doctor` or environment check.
- Wiki files.
- Source page.
- Log.
- SQLite query.
- Query record.
- Update diff.
- Briefing.
- Tool invocation records.
- Human review records.

### 6.4 Owner

| Item | Owner |
|---|---|
| Agent task | Department Owner |
| Hermes environment | IT |
| Wiki / schema | Consultant + Department Owner |
| Workflow / Skill tools | IT + Process Owner |
| Human Gate | Department manager |
| Gate 4 acceptance | Department manager + IT + Consultant |

### 6.5 Fail Conditions

- The Agent has no task boundary.
- The Agent cannot trace data sources.
- No Wiki / schema.
- It can only chat, with no ingest/query/update/briefing.
- No human Gate.
- No Runbook.

### 6.6 Next Level Entry Criteria

Conditions to enter L5:

- At least 1 Hermes Agent has passed Gate 4A-4E.
- The Agent can call at least 1 L2 Skill and 1 L3 Workflow.
- Agent output is traceable, reviewable, and operable.
- Multi-Agent collaboration candidate tasks have been defined.

---

## 7. L5 Agentic Team AI: ClawTeam

### 7.1 Definition of Done

L5 completion is not "there are many Agents" — it is:

- Multiple Agents have clear role assignment.
- Task dispatch, collaboration, integration, and a Reviewer exist.
- A human Gate and management review exist.
- ROI / KPI measurements exist.
- Cross-departmental integrated reports or decision-support outputs can be produced.

### 7.2 Deliverables

| Deliverable | Required | Description |
|---|---|---|
| ClawTeam role cards | Yes | Per-Agent role, capability, constraints |
| Task dispatch table | Yes | Task decomposition, responsible Agent, input/output |
| Agent Team IPOE | Yes | Per-Agent input/process/output/evidence |
| Integrated report template | Yes | Format for integrating multi-Agent output |
| Reviewer / Critic design | Yes | Quality check and conflict resolution |
| Human Gate design | Yes | Management review and sign-off |
| ROI / KPI table | Yes | Work hours, quality, speed, error rate |

### 7.3 Evidence

- Agent role cards.
- Task dispatch records.
- Per-Agent outputs.
- Integrated report.
- Reviewer records.
- Manager sign-off records.
- ROI / KPI tracking sheet.

### 7.4 Owner

| Item | Owner |
|---|---|
| Agent Team task | Management Sponsor |
| Per-Agent role | Department Owner |
| Integrated report | Consultant / PM |
| Reviewer | Designated reviewer role |
| ROI / KPI | Management Sponsor / Consultant |
| Gate 5 acceptance | Management |

### 7.5 Fail Conditions

- Multiple Agents have no role assignment.
- No Reviewer.
- No human Gate.
- No integrated output.
- ROI cannot be quantified or explained.
- L4 Agent is not yet stable but L5 has been entered.

### 7.6 Next Level Entry Criteria

After passing L5, enter institutionalization and expansion:

- Establish AI Agent Team governance guidelines.
- Expand to more departments and processes.
- Establish quarterly KPI / ROI reviews.
- Build the next-wave Agent Team backlog.

---

## 8. Maturity Determination Principles

1. No evidence means not done.
2. No Owner means not operable.
3. No Stage Gate means no entry to the next level.
4. No fail conditions turn acceptance into a subjective judgment.
5. No next-level entry criteria reduce the maturity model to static scoring, rather than a transformation roadmap.

