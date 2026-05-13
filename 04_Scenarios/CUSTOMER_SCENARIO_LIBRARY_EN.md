> 🌐 中文版本 / Chinese version: [CUSTOMER_SCENARIO_LIBRARY.md](CUSTOMER_SCENARIO_LIBRARY.md)

# Client Scenario Story Library

Last updated: 2026-05-13

## 1. Purpose

Clients need stories to understand AI maturity; merely hearing tool names is not enough.

Every story follows the same format:

- Before: how it is done today and what the pain points are.
- Trigger: what event starts the AI workflow.
- AI Flow: how OpenWebUI, Skills, n8n, Hermes Agent, and ClawTeam intervene.
- Systems: which systems are integrated.
- Output: what is produced.
- KPI: how value is measured.

## 2. Management Stories

### 2.1 CEO: I want to know whether the AI investment has ROI

Before: Every department says they are using AI, but the CEO only hears scattered anecdotes and cannot judge investment impact.

Trigger: Before the quarterly meeting, the CEO asks the management team to present the current AI adoption status and next steps.

AI Flow:

1. Use the maturity questionnaire to obtain the L1-L5 status of each department.
2. Use n8n to collect survey results and write them to Sheets.
3. Hermes Agent summarizes departmental maturity, gaps, and recommendations.
4. The consulting team uses the eight-stage method to produce the AI transformation diagnostic report.

Systems: Google Forms, Sheets, Notion, CRM, ERP, n8n.

Output: AI maturity radar chart, three-phase Roadmap, ROI tracking matrix.

KPI: Number of quantifiable scenarios, estimated work hours saved, PoCs completed, Stage Gate achievement rate.

### 2.2 COO: I want to reduce process rework

Before: Cross-departmental processes rely on manual copy-and-paste, with data scattered across Gmail, Sheets, CRM, and ERP.

Trigger: Before each weekly operations meeting, orders, complaints, shipments, inventory, and anomalies must be consolidated.

AI Flow:

1. L2 builds an "Operations Anomaly Analysis Skill."
2. n8n periodically pulls data from ERP, CRM, and Sheets.
3. AI classifies anomaly causes according to the Skill.
4. Hermes Agent produces an executive summary and follow-up list.

Systems: ERP, CRM, Google Sheets, Email, n8n.

Output: Weekly operations anomaly report, list of responsible departments, improvement recommendations.

KPI: Weekly report preparation time, anomaly response time, duplicate entry count, missed-case count.

### 2.3 CIO / IT: I want AI to be governable

Before: Employees use cloud AI on their own; IT has no visibility into data flow, permissions, or risks.

Trigger: The company is preparing to adopt OpenWebUI, n8n, and Agents; IT must establish governance principles.

AI Flow:

1. L1 establishes a controlled AI entry point.
2. L3 sets up n8n credentials and permission management.
3. L4 defines the tools an Agent can invoke and the data it must not touch.
4. The consulting report establishes a governance matrix.

Systems: OpenWebUI, n8n, SSO, API, DB, ERP.

Output: AI usage guidelines, permission table, logging requirements, deployment model recommendation.

KPI: Reduction in unauthorized AI use, process log completeness, count of permission exceptions, number of security incidents.

### 2.4 HR: I want AI training to truly stick

Before: Employees are excited after AI training, but revert to their original work habits within a month.

Trigger: HR is planning AI training and the departmental seed-user program.

AI Flow:

1. Use a 25-item questionnaire before training to group participants.
2. During training, produce candidate Prompt, Skill, and Workflow lists per department.
3. After training, build the Skill Library in Notion.
4. Hermes Agent reminds departments weekly to update implementation results.

Systems: Google Forms, Sheets, Notion, OpenWebUI, n8n.

Output: Training group assignments, learning outcomes, departmental Skill Library, post-training follow-up tracker.

KPI: Number of trained employees, number of Skills produced, actual adoption rate, new-hire ramp-up time.

## 3. Departmental Stories

### 3.1 Sales: Client Visit Preparation and CRM Update

Before: Before a visit, sales reps must look up client data, review historical interactions, and write a proposal summary; after the visit they must update the CRM.

Trigger: A new client visit is added to the CRM.

AI Flow:

1. n8n pulls customer data and opportunity status from the CRM.
2. Recent correspondence is summarized from Gmail.
3. The L2 "Visit Preparation Skill" organizes client background, pain points, and recommended talking points.
4. Hermes Agent produces the visit preparation pack.
5. After the meeting, a CRM update draft is generated automatically.

Systems: CRM, Gmail, Google Calendar, Sheets, n8n.

Output: Visit summary, question list, proposal direction, CRM update draft.

KPI: Visit preparation time, CRM update rate, proposal turnaround speed, opportunity advancement rate.

### 3.2 Customer Service: Gmail Complaint Triage and Case Tracking

Before: Customer service reps manually read mail, classify, look up the CRM and ERP orders, then create follow-up tasks.

Trigger: A complaint or service email arrives in Gmail.

AI Flow:

1. n8n reads incoming Gmail messages.
2. AI determines complaint type, urgency, and sentiment.
3. The CRM is queried for the customer tier and case history.
4. The ERP is queried for order, shipment, or inventory status.
5. Notion creates a case task.
6. Hermes Agent produces a reply draft and follow-up reminder.

Systems: Gmail, CRM, ERP, Notion, Sheets, n8n.

Output: Case classification, reply draft, handling tasks, customer service weekly report.

KPI: First response time, classification accuracy, missed-case rate, customer service work hours.

### 3.3 Marketing: Campaign Planning and Performance Reports

Before: Marketing must collect competitor data, write copy, organize ad performance, and produce weekly reports, with data scattered across Sheets, social platforms, and the CRM.

Trigger: A manager requests a plan for next month's campaign.

AI Flow:

1. OpenWebUI assists with the initial market and competitive analysis.
2. The L2 "Campaign Planning Skill" produces themes, audiences, and copy directions.
3. n8n pulls lists and performance data from Sheets and CRM.
4. Hermes Agent organizes the campaign plan with estimated KPIs.

Systems: Sheets, CRM, Notion, Email, ad platform APIs.

Output: Campaign plan, copy assets, audience list, performance report.

KPI: Planning time, asset output volume, campaign conversion rate, report preparation time.

### 3.4 Operations: ERP Anomaly Order Analysis

Before: Operations managers export ERP orders daily and then use Excel to find delays, missing parts, and abnormal statuses.

Trigger: ERP shows a shipment delay, low inventory, or a high-value order anomaly.

AI Flow:

1. n8n periodically retrieves ERP order data.
2. The L2 "Anomaly Order Analysis Skill" classifies anomaly causes.
3. AI writes results to Sheets.
4. Hermes Agent produces an executive summary and follow-up list by responsible department.

Systems: ERP, Sheets, Email, Notion, n8n.

Output: Anomaly order list, cause categorization, follow-up tasks, executive summary.

KPI: Time to detect anomalies, manual collation work hours, delay improvement rate, follow-up completion rate.

### 3.5 Finance: Month-End Variance Analysis

Before: At month-end close, finance must manually reconcile expenses, budgets, departmental explanations, and report variances.

Trigger: Month-end close date or expense data update.

AI Flow:

1. n8n pulls expense data from the ERP or finance system.
2. Sheets organizes departmental budget versus actual expenses.
3. The L2 "Variance Explanation Skill" produces an initial explanation.
4. Hermes Agent consolidates the anomalous items that require human confirmation.

Systems: ERP, Sheets, Email, internal finance system, n8n.

Output: Month-end variance summary, list of items pending confirmation, manager report draft.

KPI: Month-end analysis time, manual review count, anomaly follow-up rate.

### 3.6 HR: New-Hire Onboarding and Knowledge Base

Before: New hires must ask many colleagues to find SOPs scattered across documents and chat logs.

Trigger: A new hire onboards or transfers to another department.

AI Flow:

1. L2 builds a "New-Hire Onboarding Skill."
2. Notion hosts the departmental knowledge base.
3. OpenWebUI provides a Q&A entry point for new hires.
4. n8n periodically prompts managers to fill in missing documents.

Systems: Notion, OpenWebUI, Sheets, Email, n8n.

Output: New-hire learning path, FAQ, SOP lookup, training completion record.

KPI: New-hire ramp-up time, repeated-question count, document completeness, training completion rate.

### 3.7 IT: API Integration and Process Operations

Before: Every department wants to integrate systems, but requirements are scattered and ownership of permissions and operations is unclear.

Trigger: A department raises a request for an n8n Workflow or Agent integration.

AI Flow:

1. IT uses the system inventory table to confirm data sources, APIs, and permissions.
2. n8n establishes credentials and execution logs.
3. Hermes Agent monitors workflow failures and notifies the Owner.
4. The consulting report consolidates governance and operations recommendations.

Systems: n8n, API Gateway, DB, ERP, CRM, log systems.

Output: System integration table, permission matrix, process operations rules.

KPI: Integration delivery time, workflow failure rate, permission exception count, operations work hours.

## 4. ClawTeam Senior Story: New Product Launch

Before: Launching a new product requires collaboration among market, product, marketing, customer service, and finance — usually multiple meetings just to produce an initial draft.

Trigger: The CEO issues a mandate: "Deliver a new product launch plan within three weeks."

AI Flow:

1. The Market Analysis Agent researches the market and competitors.
2. The Product Planning Agent organizes features, positioning, and Roadmap.
3. The Marketing Strategy Agent produces campaign and messaging plans.
4. The Customer Service Agent prepares the FAQ and service flow.
5. The Financial Analysis Agent estimates budget, cost, and ROI.
6. The Project Integration Agent forms a complete draft plan.
7. After the human Gate review, the plan goes to the executive meeting.

Systems: CRM, Sheets, Notion, ERP, external data APIs, n8n, ClawTeam.

Output: Market analysis, product plan, marketing strategy, customer service preparation, financial estimate, project plan.

KPI: Time to first draft, number of cross-departmental meetings, data completeness, decision speed.

