> 🌐 中文版本 / Chinese version: [SAMPLE_CLIENT_CASE_HOSPITAL.md](SAMPLE_CLIENT_CASE_HOSPITAL.md)

# Sample Client Case: Hospital / Healthcare Institution

Last updated: 2026-05-13

## 1. Case Positioning

This case demonstrates how a hospital can apply the "Enterprise AI Transformation Maturity Diagnostic and Implementation Plan" under highly sensitive data and stringent regulatory requirements, from AI usage inventory and training capability build-out through to a consulting diagnostic report that produces an actionable Roadmap.

Industry: Healthcare institution / regional hospital  
Company scale: Approximately 1,500 employees  
Primary departments: Medical administration, nursing, outpatient services, customer service center, medical records, IT, quality management, finance, HR  
Primary systems: Internal email, Excel / Sheets, SharePoint / Notion, HIS, EMR, LIS, PACS, registration system, customer service system, internal APIs  
Recommended deployment: Fully on-premises or strict Hybrid  
Core principle: Patient data, medical records, lab results, images, and PII must not go directly to the public cloud; all clinically related output must be reviewed by humans

## 1.1 Case Delivery Logic

This case is not intended to prove that the hospital can immediately deploy medical-diagnosis AI; rather, it demonstrates how to advance AI safely in a highly sensitive data environment using consulting methodology.

End-to-end delivery flow:

1. Current-state data collection: Inventory hospital systems, data classification, AI usage status, and regulatory constraints.
2. Questionnaire diagnosis: Complete the 10-item quick diagnostic and the 25-item pre-training diagnostic.
3. Risk assessment: Determine which AI scenarios are automatable, require review, or are prohibited.
4. Interview assessment: Interview medical administration, customer service center, nursing, IT, and quality management.
5. As-Is process inventory: Map the patient services customer service flow and the internal SOP lookup flow.
6. L1-L5 capability assessment: Define input, process, output, and evidence at each level.
7. Training and workshops: Start with L1 governance and L2 Skills, then move to low-risk L3 Workflows.
8. Consulting diagnostic report: Produce deployment recommendations, governance design, Roadmap, ROI, and follow-on SOW.

Each stage must leave behind verifiable deliverables; in healthcare scenarios in particular, logs, human review, and accountability must be preserved.

## 2. Client Story

This hospital already has some administrative and clinical staff who have started experimenting with AI. Administrative staff use AI to rewrite announcements and organize meeting notes; customer service staff use AI to draft replies; and IT has heard of n8n, automation, and Agents.

However, hospital management is very cautious:

- Patient data must not be leaked.
- Medical advice must not be auto-decided by AI.
- Clinical staff are busy and have no time to learn complex tools.
- Internal SOPs, announcements, regulations, and patient service flows are numerous, but lookup efficiency is low.
- The customer service center is occupied with repetitive questions about registration, visit flow, check-in, and pre-examination notices.
- IT is concerned that AI adoption could increase the operations burden.

The strategy for this case is therefore not to begin with medical-diagnosis AI, but to start with low-risk, high-volume, high-administrative-burden scenarios:

1. An internal AI usage entry point and guidelines.
2. Skill codification for hospital administration and customer service.
3. n8n integration for customer service, knowledge base, forms, and internal APIs.
4. Hermes Agent as an administrative and customer service assistant, not for direct clinical decision-making.
5. Subsequent evaluation of ClawTeam for quality management, patient service improvement, and administrative project collaboration.

## 3. Questionnaire Response Summary

### 3.1 10-Item Quick Diagnostic Results

| Q# | Dimension | Score | Observation |
| --- | --- | ---: | --- |
| Q1 | AI tool entry point | 1 | Staff use external AI sporadically; no unified internal entry point yet |
| Q2 | AI usage frequency | 2 | Administration and customer service have individual usage; clinical staff use it less |
| Q3 | Prompt / SOP / Skill | 1 | Many SOPs exist, but none have been converted into AI Skills |
| Q4 | New-hire reuse of Skills | 1 | New hires still depend on managers and senior colleagues for explanation |
| Q5 | System integration | 0 | HIS, customer service system, and knowledge base are not yet integrated |
| Q6 | Automated processes | 1 | Some form-based processes exist, but AI has not entered them |
| Q7 | Agent tasks | 0 | No Hermes Agent yet |
| Q8 | Multi-Agent collaboration | 0 | No ClawTeam scenario yet |
| Q9 | Governance and logging | 2 | Security and PII awareness exist, but AI usage governance is not yet in place |
| Q10 | ROI metrics | 1 | The hospital wants to reduce administrative and customer service burden but has not defined KPIs |

Total score: 9 / 40  
Quick determination: L0-L1  
Primary gaps: Unified AI entry point, data classification, Skill codification, auditable Workflow

### 3.2 25-Item Pre-Training Diagnostic Summary

| Dimension | Average Score | Judgment |
| --- | ---: | --- |
| Tool usage | 1.8 | Sporadic use; lacks a formal entry point and guidelines |
| Knowledge codification | 1.6 | Rich SOPs, but not yet codified into AI Skills |
| Process automation | 1.0 | Most processes still depend on manual lookup and transcription |
| System integration | 0.8 | HIS / EMR / customer service systems are not connected to AI |
| Agent application | 0.2 | No Agents in place |
| Governance and ROI | 2.2 | High security awareness, but detailed AI governance is insufficient |

Initial maturity: Overall L1 not yet stable  
Recommended goal: Within 90 days establish a controlled AI entry point, data classification guidelines, 3-5 low-risk Skills, and complete one customer-service-administration Workflow PoC

## 4. Company Profile and Deployment Model Judgment

### 4.1 Company Profile

| Item | Judgment |
| --- | --- |
| Industry | Healthcare / hospital |
| Data sensitivity | Critical, including patient PII, medical records, lab tests, images, and billing data |
| Regulation and audit | High; must comply with PII, medical data governance, and internal audit requirements |
| System closure | High; HIS, EMR, LIS, and PACS are mostly intranet core systems |
| IT capability | Medium-High; an IT department exists but with a heavy operations load |
| Cloud policy | Core medical data must not go to the cloud; general administrative data requires review |
| Adoption risk | PII leakage, incorrect medical advice, permission misuse, unclear accountability |

### 4.2 Recommended Deployment Model

Recommend fully on-premises or strict Hybrid.

Deployment principles:

- Patient PII, medical records, lab tests, images, and HIS / EMR data must not be sent directly to the public cloud.
- L1 OpenWebUI is recommended to run in a controlled internal environment.
- L2 Skills can first process administrative SOPs, customer service FAQs, internal regulations, and form-based processes.
- L3 n8n integration must follow the principle of least-privilege query.
- L4 Hermes Agent should initially perform administrative assistance, customer service summarization, and internal lookup only, and must not provide medical diagnosis or treatment advice.
- All content delivered to patients must be confirmed by a human.
- All processes must retain logs, inputs, outputs, operators, and timestamps.

## 5. Recommended Training Mix

| Module | Ratio | Reason |
| --- | ---: | --- |
| L1 OpenWebUI | 30% | Establish a controlled entry point, AI usage guidelines, data classification, and security awareness |
| L2 Skill AI | 35% | Convert administrative SOPs, customer service FAQs, and patient service flows into reusable Skills |
| L3 n8n Workflow AI | 25% | Start the PoC with low-risk administrative and customer service processes |
| L4 Hermes Agent | 10% | Design administrative / customer service assistant Agents while keeping human review |
| L5 ClawTeam | 0% | Defer multi-Agent teams until governance is mature |

Recommended training package: One-day workshop + consulting diagnostic project  
If IT and management are highly engaged, this can be upgraded to a two-day adoption bootcamp

## 6. Work Assets to Be Produced During Training

### 6.1 L1 Outputs

- Draft hospital AI usage guidelines.
- Data classification principles: public, internal, sensitive, medical-core data.
- OpenWebUI internal usage process.
- Common administrative and customer service Prompts.

### 6.2 L2 Outputs

Prioritize five low-risk Skills:

1. Internal Announcement Rewriting Skill.
2. Meeting Notes Organization Skill.
3. Patient Services FAQ Skill.
4. Registration and Check-in Process Explanation Skill.
5. Pre-Examination Notice Summary Skill.

Note: The Pre-Examination Notice Skill must cite hospital-approved content; the AI must not generate medical judgments on its own.

### 6.3 L3 Outputs

Prioritize one PoC:

> Patient Services FAQ and Customer Service Case Organization Workflow

Flow:

1. The customer service system or email receives a patient service question.
2. AI classifies the question type, e.g., registration, check-in, billing, pre-examination notices, or document requests.
3. Look up answers in the hospital-approved FAQ / SOP knowledge base.
4. If the question involves personal medical condition, medical records, lab tests, or medical advice, flag it for human handling.
5. Generate a customer service reply draft.
6. Send after human confirmation.
7. Write the case classification and handling result back to Sheets or the customer service system.

### 6.4 L4 Outputs

Hermes Agent task card:

Name: Patient Services Customer Support Assistant Agent  
Goal: Help customer service staff classify questions, look up approved FAQs, generate reply drafts, and track cases.  
Available tools: Patient Services FAQ Skill, Registration Process Skill, Pre-Examination Notice Summary Skill, n8n customer service Workflow, knowledge base lookup.  
Constraints: Must not provide diagnosis, treatment, or medication advice; must not query or output patient PII; any cases involving clinical conditions must be escalated to a human.  
Output: Question classification, FAQ source, reply draft, human-handling flag, case summary.

## 7. Eight-Stage Consulting Diagnostic Analysis

### Stage 1: As-Is Snapshot

Observations:

- Administration and customer service use AI sporadically but lack formal guidelines.
- The hospital has many SOPs and FAQs, but lookup cost is high.
- Patient service questions are highly repetitive.
- IT is highly sensitive to data exfiltration and operations risk.

Output:

- AI usage inventory.
- As-Is Process Map for customer service cases.
- Data classification and system inventory.

### Stage 2: Reference Model Alignment

Judgments:

- Overall L1 is not yet stable.
- Administration and customer service show potential for L2 Skill codification.
- L3 must begin from low-risk processes and must not touch core medical data directly.

Output:

- L1-L5 maturity evaluation table.
- Classification of AI scenarios into "can adopt" and "cannot adopt" for the hospital.

### Stage 3: Best Practice Integration

Priority AI scenarios for the hospital:

- Rewriting internal announcements and administrative documents.
- Organizing meeting notes and action items.
- Patient services FAQ.
- Registration, check-in, and billing process inquiries.
- Pre-examination notice summaries.
- Internal SOP lookup.
- Quality management incident summaries.

Not recommended in the first phase:

- Medical diagnosis.
- Treatment recommendations.
- Medication recommendations.
- Unapproved automated patient-record summaries for external output.
- Agents directly modifying HIS / EMR.

### Stage 4: Gap Analysis

| Type | Finding | Impact |
| --- | --- | --- |
| Missing | No AI usage guidelines | Staff are unsure which data may be used with AI |
| Missing | No data classification or AI scenario classification | Adoption stalls on security concerns |
| Missing | SOPs / FAQs not yet codified as Skills | Low lookup efficiency, inconsistent customer service answers |
| Broken | Repetitive patient questions are handled manually | High customer service workload |
| Redundant | Administrative announcements, meeting notes, and FAQ replies are rewritten repeatedly | Wasted administrative time |
| Missing | No logging or audit mechanism | Does not meet healthcare governance requirements |

### Stage 5: Problem Definition

Executive Problem Statement:

> The hospital's AI usage remains stuck at sporadic individual experimentation. While administrative and customer service scenarios show high repeatability and adoption value, the absence of data classification, AI usage guidelines, auditable Workflows, and human review mechanisms makes it difficult for AI to safely enter hospital processes.

### Stage 6: Benchmarking and Phased Goals

90-day goals:

- Establish hospital AI usage guidelines and data classification.
- Establish OpenWebUI or a controlled AI entry point.
- Complete 5 administrative / customer service Skills.
- Complete 1 Patient Services FAQ Workflow PoC.
- Establish a Hermes Agent task card and human review flow.
- Establish AI usage logs and initial KPIs.

### Stage 7: To-Be Design

To-Be architecture:

- L1: OpenWebUI as a controlled in-hospital entry point.
- L2: Administrative and customer service Skill Library.
- L3: n8n connecting the customer service system, FAQ knowledge base, email, Sheets, and internal APIs.
- L4: Hermes Agent as the Patient Services Customer Support Assistant Agent.
- L5: Future planning for ClawTeam, e.g., a "Quality Improvement Agent Team" or an "Administrative Project Agent Team."

### Stage 8: Implementation and Change

Governance recommendations:

- AI scenario classification: automatable, requires review, prohibited.
- Data classification: public, internal, sensitive, medical-core.
- All external replies require human confirmation.
- Agents must not provide medical diagnosis, treatment, or medication advice.
- HIS / EMR / LIS / PACS are not initially opened to Agent PII queries.
- All AI Workflows retain logs.
- Establish a tripartite review by IT, Compliance / Audit, and the business Owner.

## 8. Three-Phase Roadmap

### Phase 1: Days 0-30, AI Governance and Skill Codification

Tasks:

- Establish AI usage guidelines.
- Establish data classification and scenario classification.
- Establish a controlled AI entry point.
- Produce 5 administrative / customer service Skills.

Acceptance:

- 20-30 seed users complete training.
- 5 low-risk Skills are complete.
- A list of allowed / prohibited data for AI is complete.

### Phase 2: Days 31-60, Customer Service FAQ Workflow PoC

Tasks:

- Build the Patient Services FAQ knowledge base.
- Use n8n to integrate the customer service system, Email, FAQ, and Sheets.
- Build a human review node.
- Build logging and error notifications.

Acceptance:

- AI can classify common questions.
- AI can cite approved FAQs to generate reply drafts.
- Anything involving clinical conditions or PII is automatically routed to a human.
- Customer service case statistics are produced.

### Phase 3: Days 61-90, Hermes Agent and Governance Expansion

Tasks:

- Build the Patient Services Customer Support Assistant Hermes Agent.
- Allow the Agent to invoke the FAQ Skill and the customer service Workflow.
- Build a KPI Dashboard.
- Evaluate the second-wave PoC: internal SOP lookup or quality incident summaries.

Acceptance:

- Hermes Agent can produce question classification, FAQ sources, and reply drafts.
- All replies require human confirmation.
- Management can see customer service efficiency and AI adoption rates.

## 9. ROI Metrics

| KPI | Current | 90-Day Target |
| --- | --- | --- |
| Common-question reply draft time | 5-10 minutes / case | Reduce to 1-3 minutes / case |
| Customer service case classification | Manual classification | AI initial classification, human confirmation |
| FAQ lookup time | Depends on staff experience | AI cites the approved knowledge base |
| Administrative meeting notes organization | 1-2 hours / session | Reduce to 20-30 minutes |
| Skill output | No formal Skills | 5 low-risk Skills |
| Workflow PoC | None | 1 customer service FAQ PoC |
| AI usage governance | No formal records | Establish usage guidelines and logging |

## 10. Final Consulting Report Summary

Recommended conclusions for this case:

- Current maturity: Overall L1 not yet stable.
- Target maturity: Within 90 days establish an L1 governance foundation, complete L2 Skill codification, and complete 1 L3 PoC.
- Recommended deployment: Fully on-premises or strict Hybrid.
- Priority scenario: Patient Services FAQ and customer service case organization.
- Recommended training: One-day workshop + consulting diagnostic project.
- Follow-on adoption: Patient Services Customer Support Assistant Hermes Agent, with second-wave expansion to internal SOP lookup and quality incident summaries.

## 11. L1-L5 Input / Process / Output / Evidence

### 11.1 L1 Chat AI: OpenWebUI

| Item | Definition |
| --- | --- |
| Input | Internal announcements, administrative documents, meeting notes, low-sensitivity FAQs, AI usage status questionnaire, data classification guidelines |
| Process | Establish a controlled internal AI entry point, define the usable data scope, and train Prompt fundamentals and rules prohibiting use of medical data |
| Output | Hospital AI usage guidelines, data classification table, common administrative Prompts, OpenWebUI usage process |
| Evidence | AI usage guidelines, data classification list, OpenWebUI screenshots, course sign-in, Prompt exercise outputs |
| Acceptance criteria | Seed users can perform administrative summarization, announcement rewriting, and meeting notes organization; patient PII and medical record data must not be entered |

### 11.2 L2 Skill AI: Antigravity / Claude Code / Codex

| Item | Definition |
| --- | --- |
| Input | Hospital-approved SOPs, patient services FAQ, registration and check-in processes, pre-examination notices, administrative announcement templates |
| Process | Convert approved documents into Skills; define data sources, applicable scope, prohibited scope, output format, and human review rules |
| Output | Internal Announcement Rewriting Skill, Meeting Notes Skill, Patient Services FAQ Skill, Registration Process Skill, Pre-Examination Notice Skill |
| Evidence | Skill Library, approved source documents, Skill versions, test inputs and outputs, Owner roster |
| Acceptance criteria | At least 5 low-risk Skills; every Skill cites approved content and does not generate medical judgments on its own |

### 11.3 L3 Workflow AI: n8n

| Item | Definition |
| --- | --- |
| Input | Customer service questions, Email, customer service system data, approved FAQ / SOP knowledge base, Sheets statistical tables, human review results |
| Process | n8n receives the question, classifies it, queries the approved knowledge base, judges whether it involves clinical conditions / PII / medical advice, generates a reply draft, and routes it for human confirmation |
| Output | Question classification, FAQ source, reply draft, human-handling flag, customer service case statistics |
| Evidence | n8n Workflow JSON, execution logs, human review records, knowledge base source links, test cases |
| Acceptance criteria | Complete at least 20 low-risk customer service tests; anything involving clinical conditions, medical records, lab tests, medication, or treatment is escalated to a human |

### 11.4 L4 Auto Agentic AI: Hermes Agent

| Item | Definition |
| --- | --- |
| Input | Patient service questions, FAQ Skill, Registration Process Skill, Pre-Examination Notice Skill, n8n customer service Workflow, human review rules |
| Process | Hermes Agent decomposes tasks, classifies questions, invokes Skills / Workflows, cites approved FAQs, flags risks, and generates customer service drafts |
| Output | Question classification, citation source, reply draft, risk flag, human-handling recommendation, case summary |
| Evidence | Agent task card, permission table, available tool list, Agent execution records, human takeover records |
| Acceptance criteria | The Agent does not query personal medical records, does not output diagnosis / treatment / medication advice; all external replies require human confirmation |

### 11.5 L5 Agentic Team AI: ClawTeam

| Item | Definition |
| --- | --- |
| Input | Customer service statistics, administrative process data, quality incident summaries, internal SOPs, improvement project goals |
| Process | Multi-Agent division of labor: customer service analysis Agent, quality improvement Agent, administrative process Agent, IT governance Agent, project integration Agent |
| Output | Patient services improvement proposals, customer service FAQ gaps, quality incident improvement recommendations, administrative process optimization Roadmap |
| Evidence | Agent Team role cards, task assignment records, per-Agent outputs, integration report, executive and compliance review records |
| Acceptance criteria | L5 is not a first-phase go-live target; pilot only after L1-L4 governance, logging, and human Gates are mature |

## 12. Evaluation Process and Verifiable Deliverables

| Stage | Evaluation Activity | Deliverables | Verification Method |
| --- | --- | --- | --- |
| Pre-diagnosis | Collect systems, data classification, and AI usage status | System inventory table, data classification draft, AI usage inventory table | Confirmed by IT and the management unit |
| Questionnaire | 10-item and 25-item maturity questionnaires | Questionnaire results, dimension scores, initial maturity assessment | Raw questionnaire data and scoring table |
| Risk assessment | Scenario classification: automatable, requires review, prohibited | AI scenario classification table | Confirmed by IT, Compliance / Audit, and the business unit |
| Interviews | Interview customer service, administration, nursing, IT, and quality management | Interview notes, pain point list | Interviewee-confirmed records |
| As-Is | Map the patient services customer service flow | As-Is Process Map | Confirmed by the customer service center and IT |
| L2 | Build low-risk Skills | 5 Skills, approved sources, Owners | Skill test inputs and outputs |
| L3 | Build the n8n customer service FAQ PoC | Workflow JSON, logs, human review records | 20 test cases run successfully |
| L4 | Build the Hermes Agent task card | Agent role card, permission table, tool list | Agent test records and human review |
| Consulting report | Eight-stage diagnosis and Roadmap | AI transformation diagnostic report | Confirmed via presentation to management and IT |

## 13. Stage Gate Acceptance Design

### Gate 1: L1 Controlled Entry Point and Data Classification

Required evidence:

- Hospital AI usage guidelines are complete.
- Data classification list is complete.
- OpenWebUI or a controlled AI entry point is operational.
- The rule prohibiting patient PII and medical record input is published.

### Gate 2: L2 Low-Risk Skill Library

Required evidence:

- At least 5 low-risk Skills.
- Every Skill has an approved source document.
- Every Skill has an Owner and a version history.
- No Skill produces medical diagnosis, treatment, or medication advice on its own.

### Gate 3: L3 Customer Service FAQ Workflow

Required evidence:

- The n8n Workflow runs end-to-end.
- It can query the approved FAQ / SOP.
- Any questions involving PII, clinical condition, lab tests, treatment, or medication are automatically escalated to a human.
- Logs, human review, and error notifications are in place.

### Gate 4: L4 Hermes Agent

Required evidence:

- The Hermes Agent task card is complete.
- The Agent can invoke at least 1 Skill and 1 n8n Workflow.
- The Agent's permissions are explicit: no querying medical records and no medical advice.
- All external replies require human confirmation.

### Gate 5: L5 ClawTeam Readiness

Required evidence:

- L1-L4 have stable governance and logging.
- A non-clinical or quality-improvement task suitable for multi-Agent is defined.
- A tripartite human Gate involving Compliance / Audit / business is designed.

