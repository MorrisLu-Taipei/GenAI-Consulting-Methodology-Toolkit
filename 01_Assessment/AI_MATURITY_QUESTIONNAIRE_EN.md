# AI Maturity Questionnaire

> 🌐 中文版本 / Chinese version: [AI_MATURITY_QUESTIONNAIRE.md](AI_MATURITY_QUESTIONNAIRE.md)

Last updated: 2026-05-13

## 1. How to Use

This questionnaire is provided in three versions:

- 10-item quick diagnostic: for business development, first meetings, and pre-proposal use.
- 25-item pre-course diagnostic: for planning course ratios and case selection.
- 50-item consulting deep-dive diagnostic: for use after the course, when entering the eight-stage consulting diagnostic.

Each item is scored 0-4:

| Score | Description |
| --- | --- |
| 0 | None at all |
| 1 | Sporadic individual use |
| 2 | Department has an initial approach |
| 3 | Standard practice exists and is repeatable |
| 4 | Institutionalized, governable, and measurable |

## 2. 10-Item Quick Diagnostic

| No. | Question | Dimension |
| --- | --- | --- |
| Q1 | Does the company have an approved AI usage portal, such as OpenWebUI or a designated cloud AI tool? | Tool Usage |
| Q2 | Do employees use AI stably each week for documents, email, summarization, analysis, or reports? | Tool Usage |
| Q3 | Have departments consolidated shareable Prompts, SOPs, templates, or Skills? | Knowledge Consolidation |
| Q4 | Can new hires quickly complete standard work via shared Skills or documents? | Knowledge Consolidation |
| Q5 | Does the company already use AI or n8n to integrate Gmail, Sheets, Notion, CRM, API, ERP, and similar systems? | System Integration |
| Q6 | Are there processes that can be automatically triggered, executed, notified, and logged? | Process Automation |
| Q7 | Is there an AI Agent that can decompose tasks, call tools, and report back results? | Agent Application |
| Q8 | Has multi-Agent collaboration been attempted, such as market, product, marketing, customer service, and finance Agents working together? | Agent Application |
| Q9 | Are there data classification, permission controls, human review, or AI usage logs? | Governance & ROI |
| Q10 | Has management defined AI deployment KPIs, such as time saved, error rate, response speed, cost, or revenue? | Governance & ROI |

### Quick Interpretation

- 0-10 points: L0-L1, must first establish an AI usage portal and foundational training.
- 11-20 points: L1, individual usage exists; should start Skill-ification.
- 21-28 points: L2, departmental capabilities are accumulating; suitable for pushing into Workflow.
- 29-34 points: L3, foundational workflows exist; suitable for deploying Agents.
- 35-40 points: L4-L5, can evaluate Agent Team and governance expansion.

## 3. 25-Item Pre-Course Diagnostic

### A. Tool Usage

| No. | Question |
| --- | --- |
| A1 | Does the company have a unified or approved AI tool portal? |
| A2 | Do employees know which data can or cannot be input into AI? |
| A3 | Can employees use AI to complete summarization, rewriting, translation, classification, and report drafts? |
| A4 | Are there departmental or company-level AI usage guidelines? |
| A5 | Can specific cases of personal AI productivity improvement be cited? |

### B. Knowledge Consolidation

| No. | Question |
| --- | --- |
| B1 | Does the department have shared Prompts or task templates? |
| B2 | Has senior staff experience been turned into SOPs, Checklists, or Skills? |
| B3 | Is there a centralized location to manage Skills, such as Notion, Git, or a document library? |
| B4 | Can new hires apply Skills directly to complete high-frequency work? |
| B5 | Is there an Owner, version, and quality check mechanism for each Skill? |

### C. Process Automation

| No. | Question |
| --- | --- |
| C1 | Has there been an inventory of high-frequency processes that can be automated? |
| C2 | Is n8n or a similar tool already used to integrate workflows? |
| C3 | Are there processes that can auto-trigger, execute, notify, and log? |
| C4 | Are there human review nodes that prevent AI from making high-risk decisions directly? |
| C5 | Are there error notifications, retries, and execution logs? |

### D. System Integration

| No. | Question |
| --- | --- |
| D1 | Is integration with Gmail or enterprise email required? |
| D2 | Is integration with Google Sheets, Excel, or reporting systems required? |
| D3 | Is integration with Notion, SharePoint, Confluence, or a knowledge base required? |
| D4 | Is integration with CRM, ERP, MES, PLM, QMS, or internal systems required? |
| D5 | Are there APIs, databases, or Webhooks available for AI Workflows to use? |

### E. Agent Application

| No. | Question |
| --- | --- |
| E1 | Are there well-defined Agent tasks, such as compiling weekly reports, analyzing anomalies, or producing proposals? |
| E2 | Can Agents call Skills or n8n Workflows? |
| E3 | Are Agent permissions, data sources, and executable actions clearly defined? |
| E4 | Do Agents have a reporting format, exception handling, and human-handover mechanism? |
| E5 | Is there demand or experimentation around multi-Agent collaboration? |

### 25-Item Diagnostic Output

Each item is scored 0-4, total 100 points.

Output fields:

- Total score.
- Six-dimension scores.
- Initial maturity assessment.
- Recommended course ratio.
- Recommended deployment mode.
- Recommended priority PoC.

## 4. 50-Item Consulting Deep-Dive Diagnostic

The 50-item version adds company profile, deployment mode, and ROI on top of the 25-item version.

### F. Company Profile

| No. | Question |
| --- | --- |
| F1 | Is the company's main industry R&D/manufacturing, marketing/services, finance, healthcare, government, education, retail, logistics, software, or other? |
| F2 | Which departments need AI the most? |
| F3 | Which work is the most repetitive, time-consuming, and error-prone? |
| F4 | Which work relies most heavily on senior employee experience? |
| F5 | Does management most value efficiency, cost, quality, revenue, innovation, governance, or security? |

### G. Deployment Mode

| No. | Question |
| --- | --- |
| G1 | Does the company allow public-cloud AI to process general working data? |
| G2 | Is there core data that must not leave the corporate intranet? |
| G3 | Is there PII, R&D, financial, contractual, customer confidential, or regulated data? |
| G4 | Is there an existing data classification system? |
| G5 | Is there an internal IT team able to maintain servers, Docker, APIs, databases, or permissions? |

### H. System Inventory

| No. | Question |
| --- | --- |
| H1 | Is the main collaboration tool Google Workspace, Microsoft 365, Notion, SharePoint, or other? |
| H2 | Is a CRM used? What is the system name? |
| H3 | Is an ERP / MES / PLM / QMS used? What are the system names? |
| H4 | Are there internal APIs or databases that can be read? |
| H5 | Are there mechanisms for permissions, Credentials, accounts, and audit management? |

### I. ROI and Governance

| No. | Question |
| --- | --- |
| I1 | Can you estimate how much time is saved per AI scenario? |
| I2 | Can you track error rates, response speed, throughput, or quality improvements? |
| I3 | Are there an AI Project Owner, IT Owner, and Department Owner? |
| I4 | Are there Stage Gate acceptance criteria? |
| I5 | Are AI deployment outcomes reviewed regularly and the Roadmap adjusted accordingly? |

### J. Consulting Diagnostic Focus

| No. | Question |
| --- | --- |
| J1 | Which department or process do you most want to improve first? |
| J2 | What is the most concerning risk in AI deployment? |
| J3 | Which processes, if automated, would managers most appreciate? |
| J4 | Which data or systems are the largest obstacles to AI deployment? |
| J5 | What outcomes do you hope to see within 90 days? |

## 5. Deployment Mode Determination Items

Can be used together with the 25-item or 50-item versions.

| Item | Cloud AI | Hybrid | Fully On-Premises |
| --- | ---: | ---: | ---: |
| Low data sensitivity | +2 | +1 | 0 |
| Partially sensitive data | 0 | +2 | +1 |
| Core data must not go to cloud | 0 | +1 | +2 |
| Limited IT operations capability | +2 | +1 | 0 |
| Has IT and security teams | 0 | +1 | +2 |
| SaaS tools as the main stack | +2 | +1 | 0 |
| ERP / MES / internal systems as the main stack | 0 | +1 | +2 |
| Limited budget, must start quickly | +2 | +1 | 0 |
| High audit or regulatory requirements | 0 | +1 | +2 |

The highest score indicates the recommended deployment mode. If Hybrid and fully on-premises are close, we recommend starting with a Hybrid pilot, keeping core data on-premises.

## 6. Diagnostic Result Text Templates

### L1 Example

Your company's current AI applications mainly sit at the L1 Chat AI stage. Employees have started using AI to boost personal productivity, but knowledge has not yet been consolidated into departmental assets. We recommend first establishing an OpenWebUI unified portal, AI usage guidelines, and departmental high-frequency Prompts, before moving on to L2 Skill-ification.

### L2 Example

Your company already has a preliminary L2 Skill AI foundation. Departments have some SOPs, Prompts, or templates, but a stable and maintainable Skill Library has not yet formed. We recommend that the course focus on Skill design, departmental knowledge consolidation, and inventorying L3 Workflow candidate scenarios.

### L3 Example

Your company has the conditions for L3 Workflow AI. The next step is to select high-value processes and use n8n to integrate Gmail, Sheets, Notion, CRM, API, ERP, and similar systems, completing 1-2 demonstrable PoCs while establishing permission, logging, and human-review mechanisms.

### L4 Example

Your company has the foundation to deploy Hermes Agent. We recommend starting from a single departmental task by designing Agent role cards, task boundaries, callable Skills, triggerable Workflows, and reporting formats, while avoiding letting the Agent handle high-risk decisions from the outset.

### L5 Example

Your company has the conditions to explore ClawTeam. We recommend selecting cross-departmental tasks — such as new product planning, customer management, or operational anomaly analysis — and designing multi-Agent role assignments, output integration, and quality-check processes, so the AI Team becomes a decision-support capability for management.

