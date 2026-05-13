> 🌐 中文版本 / Chinese version: [DELIVERY_PACKAGE_AND_ACCEPTANCE.md](DELIVERY_PACKAGE_AND_ACCEPTANCE.md)

# AI Transformation Maturity Consulting Program: Delivery Package and Acceptance Criteria

Version: v1.0  
Author: Morris Lu (盧業興) · Tiger AI 虎智科技

---

## 1. Delivery Positioning

This program is fully deliverable and should not be packaged as merely "training." A complete delivery is:

> Use a questionnaire to rapidly diagnose AI maturity, configure courses and workshops according to L1-L5, produce usable assets during the courses, and after the courses use the eight-stage consulting methodology to form an AI transformation diagnostic report, with acceptance based on evidence and Stage Gates.

What the client buys is not a tool tour but an AI transformation implementation package that can be jointly validated by management, IT, process Owners, and consultants.

---

## 2. Delivery Overview

| Delivery Phase | Client-Facing Description | Main Deliverables | Acceptance Method |
|---|---|---|---|
| D1 Diagnosis | Know what level the company is at | Questionnaire, maturity scores, gap analysis, recommended course mix | Diagnostic briefing and management sign-off |
| D2 Course Design | Not a fixed curriculum, but a maturity-based course mix | L1-L5 syllabus, company attribute survey, deployment mode recommendation | Pre-course meeting sign-off |
| D3 Course Implementation | Produce their own assets during the course | Prompts, Skills, Workflows, Agent task cards, control sheets | Classroom demos and assignments |
| D4 L4 Hermes Agent PoC | Build a traceable Agent loop | Wiki, schema, ingest/query/update, briefing, Gates 4A-4E | Demo, logs, evidence |
| D5 Consulting Diagnosis | Produce a formal transformation report after the course | Eight-stage diagnostic report, Roadmap, ROI, risk and governance | Consulting report meeting |
| D6 Follow-on Implementation | Move from PoC to production and scale-out | 90-day implementation plan, Owners, KPIs, operational Runbook | Project kickoff meeting |

---

## 3. D1 Maturity Diagnosis Delivery Package

### 3.1 Delivery Content

- AI maturity questionnaire: 10-question quick version / 25-question standard version / 50-question full version.
- Initial L1-L5 maturity assessment.
- Scores across six dimensions: tool use, knowledge accumulation, process automation, system integration, Agent application, governance and ROI.
- Company attribute survey: industry, departments, data sensitivity, IT capability, decision-making process.
- Deployment mode recommendation: cloud AI, Hybrid, fully on-premise.
- Course mix recommendation: ratios for L1/L2/L3/L4/L5.

### 3.2 Evidence

| Evidence | Description |
|---|---|
| Raw questionnaire responses | Traceable source for each score |
| Maturity radar chart | Visualizes gaps across the six dimensions |
| Course mix table | Translates diagnostic results into class arrangements |
| Management sign-off record | Confirms diagnostic assumptions align with the field |

### 3.3 Acceptance Criteria

- The client understands which of L1-L5 they are at.
- The client can name three most important gaps.
- The client agrees to the first-wave course mix and PoC scope.

---

## 4. D2 L1-L5 Course Delivery Package

| Level | Course Deliverables | Evidence | Gate |
|---|---|---|---|
| L1 OpenWebUI | AI usage guidelines, Prompt Library, departmental cases, account/group/permission sheet, Admin Runbook | Prompt templates, classroom assignments, usage guidelines, login screenshots, personal chat area screenshots, Admin Panel screenshots | Gate 1 |
| L2 Skill AI | Skill Library, SOPs, Checklists, templates, Antigravity app prototype / test / docs / GCP PoC, L3 Workflow Blueprint | Skill documentation, test records, Owner list, Agent artifacts, deployment validation records, trigger / I/O schema / node map / sample payload | Gate 2 |
| L3 n8n Workflow | Workflow PoC, integration requirements, Execution Log, Data Tables Schema, Sub-workflow Library, GitHub Backup SOP, L4 Workflow Contract | n8n JSON, API permissions, execution records, failure tests, backup commits, human review records | Gate 3 |
| L4 Hermes Agent | Agent task cards, Wiki, L4 IPOE, briefings, Gates 4A-4E | Logs, SQLite queries, source pages, briefings, human review | Gate 4 |
| L5 ClawTeam | Agent Team role cards, task allocation, integrated report template | Agent outputs, Reviewer records, integrated report | Gate 5 |

---

## 5. D3-L2 Antigravity Engineering Training Deliverables

The three Antigravity codelabs serve as L2 engineering training. They should deliver not only exercise screenshots but reusable engineering skills.

| Deliverable | Content | Acceptance Criteria |
|---|---|---|
| Antigravity configuration sheet | Agent Manager, Editor, Browser, workspace, permission policies | Trainee can complete a basic task and leave an artifact |
| App Prototype | Flask app, productivity app, or internal small tool | Runs locally or is demoable |
| Unit Test Evidence | Test files, test results, fix records | A non-author can re-run the tests |
| README / Docs | Usage instructions, limits, operational notes | A non-author can operate per the docs |
| GCP Pipeline PoC | GCS, Pub/Sub, Cloud Run, Gemini, BigQuery | Uploading a test file produces results in BigQuery |
| Deployment Validation | gcloud logs, Cloud Run logs, BigQuery queries, screenshots | IT / instructor can validate |
| L2 Engineering Skill | Reusable SOP for app prototype, test, deployment, validation | Has Owner, version, test records |
| L3 Workflow Blueprint | Trigger, input/output schema, n8n node map, human gate, log, error handling, sample payload | L3 instructors and IT can directly proceed to n8n implementation |

---

## 6. D4 L4 Hermes Agent Deliverables

L4 Hermes Agent is the segment most easily challenged by clients with "did you actually build it?", so it must be accepted on the basis of evidence.

### 6.1 Mandatory Deliverables

| Deliverable | Content | Acceptance Criteria |
|---|---|---|
| Hermes Agent task card | Role, task, data sources, tools, constraints, human Gates | Department head and IT sign-off |
| L4 IPOE table | Input / Process / Output / Evidence | Each item points to an actual file or record |
| Initial Wiki | `purpose.md`, `SCHEMA.md`, INBOX, queue, watchlist, tasks | Files exist and content matches the task |
| Ingest test | Import PDFs / SOPs / FAQs / reports | Source pages, logs, and indexes exist |
| Query test | At least 3 traceable queries | Answers include cited sources |
| Update test | At least 1 write-back or update | Diff, rationale, and review record exist |
| Briefing template | Morning briefing or weekly briefing | Manager can read it directly |
| Gates 4A-4E sheet | Environment, knowledge base, ingest, query/update, governance | Each Gate has Pass / Fail |
| Operations Runbook | Schedule, Owner, failure handling, human handoff | IT / Owner can take over |

### 6.2 Optional Deliverables

- Autonomous discovery watchlist.
- Weekly graph synthesis report.
- OpenWebUI operation command card.
- n8n Workflow triggering Hermes Agent.
- Departmental Agent Dashboard.

---

## 7. D5 Eight-Stage Consulting Diagnostic Report Delivery Package

| Eight Stages | Report Chapter | Deliverable Content |
|---|---|---|
| 1. Problem Definition | Current state and pain points | Why the client needs AI transformation |
| 2. Data Collection | Diagnostic data | Questionnaires, interviews, systems, processes, documents |
| 3. Analysis and Diagnosis | Maturity and gaps | L1-L5 scores, six dimensions, bottlenecks |
| 4. Hypothesis Validation | PoC and course outcomes | Classroom assets, Workflows, Hermes Agent evidence |
| 5. Solution Design | Roadmap | 30/60/90-day plan and role allocation |
| 6. Execution Planning | Implementation plan | Owners, resources, schedule, risks |
| 7. Benefit Measurement | KPI / ROI | Hours saved, quality, speed, error rate |
| 8. Institutionalization | Governance and diffusion | AI policy, Stage Gates, operations, next wave of cases |

---

## 8. Delivery Acceptance Meeting Flow

1. Review diagnostic results: confirm original maturity and gaps.
2. Review course outputs: showcase L1-L5 assets one by one.
3. Demo the L4 Hermes Agent: run a real task once through input → process → output → evidence.
4. Check Stage Gates: confirm which have passed and which cannot proceed to the next phase.
5. Present the consulting report: propose Roadmap, KPIs, risks, and follow-on implementation recommendations.
6. Decide next steps: go-live, scale the PoC, supplementary training, governance strengthening, or moving into L5.

---

## 9. A Client-Friendly Story

What the client's executives see is not technical jargon, but a clear story:

> We first use a questionnaire to learn that the company is only using AI in a scattered way. We then use the courses to turn employees' Prompts into Skills, turn repetitive processes into n8n Workflows, and hand departmental documents, FAQs, SOPs, and process outputs to Hermes Agent to form a traceable knowledge-work loop. After the course, we deliver not just handouts, but a maturity diagnosis, course assets, Agent evidence, Stage Gates, and a 90-day Roadmap, so the executives know where the next investment should go.

That is the core of what this program can deliver.
