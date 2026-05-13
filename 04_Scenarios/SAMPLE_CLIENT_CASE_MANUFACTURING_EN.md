> 🌐 中文版本 / Chinese version: [SAMPLE_CLIENT_CASE_MANUFACTURING.md](SAMPLE_CLIENT_CASE_MANUFACTURING.md)

# Sample Client Case: R&D Manufacturing Industry

Last updated: 2026-05-13

## 1. Case Positioning

This case illustrates how the "Enterprise AI Transformation Maturity Diagnostic and Implementation Plan" delivers end-to-end value, from questionnaire and training through to the consulting diagnostic report.

Industry: R&D manufacturing  
Company scale: Approximately 500 employees  
Primary departments: Sales, Customer Service, R&D, Manufacturing, QA, Operations, Finance, IT  
Primary systems: Gmail, Google Sheets, Notion, CRM, ERP, QMS, internal APIs, file server  
Recommended deployment: Hybrid — core data remains on-premises while low-sensitivity work can use cloud AI

## 1.1 Case Delivery Logic

This case is not merely a description of "what is possible"; it demonstrates a complete consulting delivery flow:

1. Current-state data collection: Gather the system list, departmental processes, AI usage status, and data sensitivity.
2. Questionnaire diagnosis: Complete the 10-item quick diagnostic and the 25-item pre-training diagnostic.
3. Interview assessment: Interview management, customer service, operations, QA, and IT.
4. As-Is process inventory: Map the complaint handling and ERP anomaly order flows.
5. L1-L5 capability assessment: Define input, process, output, and evidence at each level.
6. Training and workshops: Allocate L1-L4 training based on maturity.
7. PoC design: Select "complaint email + CRM + ERP + QMS" as the first PoC.
8. Consulting diagnostic report: Produce the Roadmap, ROI, governance, and follow-on SOW.

Each stage must leave behind verifiable deliverables; verbal recommendations alone are not acceptable.

## 2. Client Story

The company already has many employees using AI. Sales reps use AI to write emails, R&D uses AI to summarize documents, and customer service uses AI to draft replies — but all outputs remain on personal laptops and in chat histories.

Management's frustration is:

- Everyone says AI is useful, but the company cannot see overall ROI.
- The ERP, CRM, and QMS hold abundant data, but AI has not truly entered the processes.
- Complaints, anomalous orders, and quality issues still rely on manual data lookup and report compilation.
- IT is concerned about data exfiltration and therefore reluctant to allow core data into the cloud.
- New hires take a long time to learn SOPs, quality standards, and customer specifications.

The focus of this case is therefore not to deploy the flashiest Agent first; it is to establish a governable AI entry point, departmental Skills, and n8n Workflows, and to adopt Hermes Agent progressively.

## 3. Questionnaire Response Summary

### 3.1 10-Item Quick Diagnostic Results

| Q# | Dimension | Score | Observation |
| --- | --- | ---: | --- |
| Q1 | AI tool entry point | 2 | Employees use cloud AI individually; no unified entry point yet |
| Q2 | AI usage frequency | 3 | Sales, R&D, and customer service have stable individual usage |
| Q3 | Prompt / SOP / Skill | 1 | Sporadic Prompts exist; no departmental Skill Library |
| Q4 | New-hire reuse of Skills | 1 | New hires still rely on senior colleagues for verbal instruction |
| Q5 | System integration | 1 | n8n is not yet used to integrate ERP / CRM / QMS |
| Q6 | Automated processes | 1 | A few scheduled reports exist, but AI has not entered the process |
| Q7 | Agent tasks | 0 | No Hermes Agent yet |
| Q8 | Multi-Agent collaboration | 0 | No ClawTeam scenario yet |
| Q9 | Governance and logging | 2 | IT has security awareness but lacks AI usage logs |
| Q10 | ROI metrics | 1 | Management wants to see ROI but has not yet defined KPIs |

Total score: 12 / 40  
Quick determination: L1, with localized L2 emerging  
Primary gaps: Skill codification, Workflow integration, governance, and ROI

### 3.2 25-Item Pre-Training Diagnostic Summary

| Dimension | Average Score | Judgment |
| --- | ---: | --- |
| Tool usage | 2.6 | Individual usage is established but lacks a unified entry point |
| Knowledge codification | 1.4 | SOPs and Prompts are not yet codified into Skills |
| Process automation | 1.2 | Processes still move data manually |
| System integration | 1.4 | ERP / CRM / QMS are not yet part of the AI flow |
| Agent application | 0.4 | No Agent foundation yet |
| Governance and ROI | 1.8 | Security awareness exists but institutionalized management is lacking |

Initial maturity: Overall L1, with some departments approaching L2  
Recommended goal: Stabilize at L2 within 90 days and complete 1 L3 Workflow PoC

## 4. Company Profile and Deployment Model Judgment

### 4.1 Company Profile

| Item | Judgment |
| --- | --- |
| Industry | R&D manufacturing |
| Data sensitivity | High, including customer specifications, BOM, quality records, orders, and shipping data |
| System closure | Medium-High; ERP, QMS, and internal APIs require IT support |
| IT capability | Medium; an IT team exists but with limited resources |
| Cloud policy | General data can go to the cloud; core data cannot be sent directly to the cloud |
| Adoption risk | Data permissions, incorrect decisions, process operations, cross-departmental accountability |

### 4.2 Recommended Deployment Model

Recommend Hybrid.

Rationale:

- OpenWebUI can serve as the controlled AI entry point.
- General document summarization, training, and copywriting can use cloud AI.
- ERP, QMS, customer specifications, and quality data remain in the controlled environment.
- n8n serves as a workflow bridging layer, integrating internal APIs under permission control.
- Hermes Agent initially performs only analysis, organization, and reminders, and does not directly modify core ERP data.

## 5. Recommended Training Mix

| Module | Ratio | Reason |
| --- | ---: | --- |
| L1 OpenWebUI | 25% | Establish a unified entry point, usage guidelines, and data security awareness |
| L2 Skill AI | 35% | Manufacturing knowledge is dense; codify SOPs, quality, complaints, and anomaly analysis Skills first |
| L3 n8n Workflow AI | 30% | Prioritize PoCs across ERP / CRM / QMS / Sheets |
| L4 Hermes Agent | 10% | Design Agent task cards for operations or customer service |
| L5 ClawTeam | 0% | Multi-Agent team foundation not yet in place; include in the future Roadmap |

Recommended training package: Two-day adoption bootcamp + consulting diagnostic project

## 6. Work Assets to Be Produced During Training

### 6.1 L1 Outputs

- Draft AI usage guidelines.
- OpenWebUI usage process.
- Common Prompts for Sales, Customer Service, R&D, and QA.

### 6.2 L2 Outputs

Prioritize five Skills:

1. Complaint Summary Skill.
2. 8D / 5Why Problem Analysis Skill.
3. ERP Anomaly Order Analysis Skill.
4. SOP / WI Document Summary Skill.
5. Customer Specification Variance Organization Skill.

### 6.3 L3 Outputs

Prioritize one PoC:

> Complaint Email and ERP Order Status Integration Workflow

Flow:

1. Gmail receives a complaint email.
2. AI determines complaint type, customer, product, and urgency.
3. The CRM is queried for the customer tier and case history.
4. The ERP is queried for order, shipment, and inventory status.
5. The QMS is queried for related quality records.
6. Notion creates a case task.
7. Sheets records handling status.
8. A customer service reply draft and executive summary are produced.

### 6.4 L4 Outputs

Hermes Agent task card:

Name: Customer Service Case Organization Agent  
Goal: After a complaint is received, automatically organize the customer background, order status, quality records, and reply draft.  
Available tools: Complaint Summary Skill, 8D / 5Why Skill, n8n complaint Workflow, CRM query, ERP query, QMS query.  
Constraints: Must not directly modify ERP / QMS production data; all external replies require human confirmation.  
Output: Case summary, recommended reply, follow-up list, risk reminders.

## 7. Eight-Stage Consulting Diagnostic Analysis

### Stage 1: As-Is Snapshot

Observations:

- AI usage stops at individual productivity.
- ERP, CRM, and QMS hold rich data, but processes are not connected.
- Complaint and anomaly analysis depends heavily on senior employees.

Output:

- AI usage inventory.
- As-Is Process Map for complaint handling.
- System and data source inventory.

### Stage 2: Reference Model Alignment

Judgments:

- Overall L1.
- Customer Service, R&D, and Sales show L2 potential.
- L3 is not yet reached because n8n Workflows and system integration are lacking.

Output:

- L1-L5 maturity evaluation table.
- Departmental maturity comparison.

### Stage 3: Best Practice Integration

Priority AI scenarios for manufacturing:

- Complaint analysis.
- ERP anomaly orders.
- Quality problem 8D / 5Why.
- SOP / WI lookup.
- R&D document summarization.

### Stage 4: Gap Analysis

| Type | Finding | Impact |
| --- | --- | --- |
| Missing | No Skill Library | Good methods cannot be replicated |
| Missing | No n8n Workflow | AI has not entered the process |
| Broken | Complaints require manual lookup across CRM / ERP / QMS | Slow response, prone to missing data |
| Redundant | Executive weekly reports are compiled manually | Time-consuming with inconsistent formatting |
| Missing | No ROI metrics | Hard for management to decide |

### Stage 5: Problem Definition

Executive Problem Statement:

> The company has built an individual AI usage foundation, but lacks departmental Skill codification, cross-system Workflow integration, and governance mechanisms. As a result, AI outcomes cannot be replicated, complaints and anomaly handling still depend heavily on manual effort, and management cannot measure AI investment returns.

### Stage 6: Benchmarking and Phased Goals

90-day goals:

- Establish OpenWebUI usage guidelines.
- Complete 5 L2 Skills.
- Complete 1 L3 complaint Workflow PoC.
- Establish a Customer Service Case Organization Hermes Agent task card.
- Define 5 ROI metrics.

### Stage 7: To-Be Design

To-Be architecture:

- L1: OpenWebUI as the controlled AI entry point.
- L2: Notion / Git / document repository as the Skill Library.
- L3: n8n integrating Gmail, CRM, ERP, QMS, Sheets, and Notion.
- L4: Hermes Agent invoking Skills and Workflows.
- L5: Plan ClawTeam in a second phase, e.g., a "Quality Improvement Agent Team."

### Stage 8: Implementation and Change

Governance recommendations:

- Set AI usage guidelines.
- Set data classification.
- ERP / QMS allow read-only queries; Agents are not allowed to modify them directly.
- All customer-facing external replies require human confirmation.
- n8n executions must retain logs.
- Conduct monthly reviews of ROI and process improvement.

## 8. Three-Phase Roadmap

### Phase 1: Days 0-30, AI Foundation and Skill Codification

Tasks:

- Roll out OpenWebUI or a unified AI entry point.
- Complete AI usage guidelines.
- Build 5 departmental Skills.
- Complete the complaint As-Is process inventory.

Acceptance:

- 20 seed users complete training.
- 5 Skills are ready for departmental use.
- Each Skill has an Owner and a version.

### Phase 2: Days 31-60, n8n Workflow PoC

Tasks:

- Integrate Gmail, CRM, ERP, QMS, Sheets, and Notion.
- Build the complaint Workflow PoC.
- Add a human review node.
- Build logging and error notifications.

Acceptance:

- Complaints can be classified automatically.
- Customer background, order status, and quality records can be summarized.
- Reply drafts must be sent only after human confirmation.

### Phase 3: Days 61-90, Hermes Agent and Governance

Tasks:

- Build the Customer Service Case Organization Hermes Agent.
- Allow the Agent to invoke L2 Skills and L3 Workflows.
- Build an ROI Dashboard.
- Evaluate the second-wave PoC: ERP anomaly order analysis.

Acceptance:

- The Agent can produce case summaries and follow-up lists.
- Management can see weekly KPIs.
- A next-stage SOW is formed.

## 9. ROI Metrics

| KPI | Current | 90-Day Target |
| --- | --- | --- |
| Initial complaint organization time | 30-60 minutes / case | Reduce to 10-15 minutes / case |
| CRM / ERP / QMS lookup count | Manual multi-system queries | Consolidated automatically by the Workflow |
| Customer service reply draft creation | Manually written | AI generates the draft; humans confirm |
| Complaint weekly report preparation | 2-4 hours / week | Reduce to under 30 minutes |
| Skill output | No formal Skills | 5 usable Skills |
| Process PoC | None | 1 L3 PoC |

## 10. Final Consulting Report Summary

Recommended conclusions for this case:

- Current maturity: Overall L1, locally L2.
- Target maturity: Stabilize at L2 within 90 days and complete an L3 PoC.
- Recommended deployment: Hybrid.
- Priority scenario: Complaint email integration with ERP / CRM / QMS.
- Recommended training: Two-day adoption bootcamp + consulting diagnostic project.
- Follow-on adoption: Customer Service Case Organization Hermes Agent, with second-wave expansion to ERP anomaly order analysis.

## 11. L1-L5 Input / Process / Output / Evidence

### 11.1 L1 Chat AI: OpenWebUI

| Item | Definition |
| --- | --- |
| Input | Employee daily documents, Email, meeting notes, SOPs, non-sensitive product data, AI usage status questionnaire |
| Process | Establish a controlled AI entry point, train Prompt fundamentals, define allowable and prohibited input data, and build personal productivity scenarios |
| Output | Personal common Prompts, AI usage guidelines, OpenWebUI usage process, departmental common-task examples |
| Evidence | OpenWebUI screenshots, account list, Prompt templates, usage guideline document, training sign-in and exercise outputs |
| Acceptance criteria | Seed users can use OpenWebUI to summarize, rewrite, draft emails, and prepare executive summaries; core confidential data must not be entered |

### 11.2 L2 Skill AI: Antigravity / Claude Code / Codex

| Item | Definition |
| --- | --- |
| Input | Senior employee expertise, complaint SOPs, 8D / 5Why templates, ERP anomaly handling rules, quality documents, customer specification summaries |
| Process | Convert personal expertise into Skills; define Skill goal, input, steps, output format, constraints, and acceptance criteria |
| Output | Complaint Summary Skill, 8D / 5Why Skill, ERP Anomaly Order Analysis Skill, SOP Summary Skill, Customer Specification Variance Skill |
| Evidence | Skill Library, Skill templates, version history, sample inputs and outputs, departmental Owner roster |
| Acceptance criteria | At least 5 Skills are usable by non-original authors with consistent output format; every Skill has an Owner and an update record |

### 11.3 L3 Workflow AI: n8n

| Item | Definition |
| --- | --- |
| Input | Gmail complaint emails, CRM customer data, ERP order / shipment / inventory data, QMS quality records, Sheets trackers, Notion task store |
| Process | Use n8n to build triggers, data queries, AI classification, Skill invocation, human review, logging, notification, and error handling |
| Output | Complaint case classification, customer background summary, order status summary, quality records summary, customer service reply draft, executive weekly report |
| Evidence | n8n Workflow JSON, execution logs, test cases, error notification records, human review records, data field mapping table |
| Acceptance criteria | Complete at least 10 test cases; can automatically classify, query data, and generate summaries and reply drafts; external replies require human confirmation |

### 11.4 L4 Auto Agentic AI: Hermes Agent

| Item | Definition |
| --- | --- |
| Input | Customer service cases, Complaint Summary Skill, 8D / 5Why Skill, n8n complaint Workflow, CRM / ERP / QMS query results |
| Process | Hermes Agent receives the task and decomposes it into data lookup, classification, summarization, risk judgment, reply recommendation, and follow-up reminders |
| Output | Case summary, handling recommendation, follow-up list, risk flag, executive report draft |
| Evidence | Agent task card, Agent available tool list, permission table, execution records, human takeover records |
| Acceptance criteria | The Agent must not directly modify ERP / QMS; all recommendations are traceable to their data source; high-risk cases are automatically flagged for human handling |

### 11.5 L5 Agentic Team AI: ClawTeam

| Item | Definition |
| --- | --- |
| Input | Complaint trends, quality anomalies, ERP delay data, customer tiers, product line data, improvement project goals |
| Process | Multi-Agent division of labor: quality analysis Agent, operations analysis Agent, customer service Agent, finance Agent, project integration Agent |
| Output | Quality improvement proposals, complaint root cause analysis, cost impact estimate, cross-departmental improvement Roadmap |
| Evidence | Agent Team role cards, task assignment records, per-Agent outputs, integration report, executive review records |
| Acceptance criteria | L5 is not a first-phase go-live target; pilot only after L3 Workflows and L4 Agents are stable, using a quality improvement project |

## 12. Evaluation Process and Verifiable Deliverables

| Stage | Evaluation Activity | Deliverables | Verification Method |
| --- | --- | --- | --- |
| Pre-diagnosis | Collect company systems, processes, and AI usage status | System inventory table, AI usage inventory table | Confirmed by IT and department heads |
| Questionnaire | 10-item and 25-item maturity questionnaires | Questionnaire results, dimension scores, initial maturity assessment | Raw questionnaire data and scoring table |
| Interviews | Interview customer service, operations, QA, IT, and management | Interview notes, pain point list | Interviewee-confirmed records |
| As-Is | Map the complaint and anomaly order flows | As-Is Process Map | Confirmed in departmental workshops |
| L2 | Build the Skill Library | 5 Skills, Owners, versions | Skill test inputs and outputs |
| L3 | Build the n8n PoC | Workflow JSON, logs, test data | 10 test cases run successfully |
| L4 | Build the Hermes Agent task card | Agent role card, permission table, tool list | Agent test records and human review |
| Consulting report | Eight-stage diagnosis and Roadmap | AI transformation diagnostic report | Management presentation and sign-off |

## 13. Stage Gate Acceptance Design

### Gate 1: L1 Usage Entry Point and Guidelines

Required evidence:

- OpenWebUI or an approved AI entry point is operational.
- AI usage guidelines are complete.
- Seed users complete at least 3 Prompt exercises.

### Gate 2: L2 Skill Library

Required evidence:

- At least 5 Skills.
- Each Skill has a purpose, input, steps, output, constraints, and Owner.
- At least 2 non-original authors can use the Skill to produce acceptable results.

### Gate 3: L3 Workflow PoC

Required evidence:

- The n8n Workflow runs end-to-end.
- It can integrate at least 3 categories among Gmail, CRM, ERP, QMS, Sheets, or Notion.
- Execution logs, error handling, and human review nodes are in place.

### Gate 4: L4 Hermes Agent

Required evidence:

- The Agent task card is complete.
- The Agent can invoke at least 1 Skill and 1 n8n Workflow.
- Agent output includes data source citations and a human confirmation mechanism.

### Gate 5: L5 ClawTeam Readiness

Required evidence:

- Stable L3 Workflows are in place.
- At least 1 controlled L4 Agent is in place.
- Cross-departmental tasks, Agent roles, and human Gates are defined.

