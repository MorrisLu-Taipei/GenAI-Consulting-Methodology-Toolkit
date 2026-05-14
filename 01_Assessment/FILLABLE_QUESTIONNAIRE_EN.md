# Fillable Questionnaire Specifications

> 🌐 中文版本 / Chinese version: [FILLABLE_QUESTIONNAIRE.md](FILLABLE_QUESTIONNAIRE.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

Renders the 10/25/50-question versions of `AI_MATURITY_QUESTIONNAIRE.md` as form specs for Google Form / Tally / Notion Form. The schema aligns with `AI_DIAGNOSIS_SHEETS_SCHEMA.md`.

---

## Common Settings

| Field | Content |
| --- | --- |
| Form language | Chinese by default, with an EN toggle |
| Answer scale | 0-4 (0 = none at all, 4 = institutionalized with a Gate) |
| Required fields | All questions required; empty values not scored |
| On-submit | Google Sheets `Raw Responses` + n8n webhook |
| Privacy | No IP collected; email stored encrypted |
| Branding | Tiger AI logo + Apache 2.0 footer |

---

## A. 10-Question Version (Quick Diagnostic for Sales)

### Form intro

> 10 questions, ~3 minutes. Helps you quickly see your enterprise's AI maturity level (L1-L5). You will receive a customized interpretation within 24 hours.

### Page 1: Profile (4 questions)

- P1 Company name — short text
- P2 Your role — radio: CEO / COO / CIO·IT / Dept head / Other
- P3 Company size — radio: <50 / 50-300 / 300-1000 / 1000+
- P4 Industry — radio: manufacturing / hospital / retail / financial / gov / software / pro-services / other

### Page 2: Six constructs (10 questions, each scale 0-4)

| Q | Question | Construct |
| --- | --- | --- |
| Q1 | Our employees broadly use AI tools daily to get work done | Tool Usage |
| Q2 | Employees' prompts and experience are centrally organized | Knowledge Codification |
| Q3 | We have defined "what good AI usage looks like" | Process Standardization |
| Q4 | AI is connected to at least one enterprise system (Gmail / Sheets / CRM / ERP) | System Integration |
| Q5 | We have repeatable, callable AI Skills or Workflows | Agent Application |
| Q6 | We have an AI usage policy and an audit mechanism | Governance & ROI |
| Q7 | AI has produced concrete, quantifiable efficiency gains for us | ROI |
| Q8 | We have a clear next step for AI advancement (not relying on a vendor) | Strategy |
| Q9 | Managers regularly review AI adoption progress | Governance |
| Q10 | We have concrete protection against AI risks (security, compliance, hallucination) | Governance |

### Submit page

> Submitted. We will email your preliminary AI maturity report and recommendations within 24 hours.

### What happens next

> 1. Auto-scoring → level determination (L1-L5)
> 2. Sales contact to arrange a 30-minute 1-on-1 debrief
> 3. Customized proposal (1-day workshop / 2-day bootcamp / consulting project)

---

## B. 25-Question Version (Pre-Course Diagnostic)

### Form intro

> 25 questions, ~8 minutes. Deeper than the 10-question version: 4-5 questions per construct. Recommended to be completed by managers one week before L1 course delivery.

### Page 1: Profile (5)

P1-P4 as above + P5 Your department

### Pages 2-7: Six constructs × 4-5 questions

**Page 2 (Tool Usage)** — Q1-Q4
- Q1 How frequently employees use AI weekly
- Q2 Types of AI tools the company has purchased
- Q3 Whether employees share AI accounts (negative: score inverted)
- Q4 Whether employees explicitly note "AI-assisted" in meetings / reports

**Page 3 (Knowledge Codification)** — Q5-Q8
- Q5 Whether a Prompt Library exists
- Q6 Whether Skills / Workflows are periodically consolidated
- Q7 Whether experienced employees' AI know-how is documented
- Q8 Whether there is an AI onboarding process for new hires

**Page 4 (Process Standardization)** — Q9-Q12
- Q9 Whether an SOP defines the scope of AI usage
- Q10 Whether there is a review mechanism (human Gate)
- Q11 Whether high-frequency scenarios become repeatable processes
- Q12 Whether there are cross-functional AI processes

**Page 5 (System Integration)** — Q13-Q16
- Q13 Whether AI connects to Gmail / Outlook
- Q14 Whether AI connects to Google Sheets / Notion
- Q15 Whether AI connects to CRM (HubSpot / Salesforce)
- Q16 Whether AI connects to ERP / internal APIs

**Page 6 (Agent Application)** — Q17-Q20
- Q17 Whether an Agent autonomously executes multi-step tasks
- Q18 Whether the Agent has a Wiki / memory
- Q19 Whether the Agent has a Reviewer / Human Gate
- Q20 Whether there is multi-Agent collaboration (Agent Team)

**Page 7 (Governance & ROI)** — Q21-Q25
- Q21 Whether an AI permission matrix is defined
- Q22 Whether there is an audit log
- Q23 Whether sensitive-data redaction rules are defined
- Q24 Whether AI ROI tracking KPIs exist
- Q25 Whether managers regularly review AI outcomes

### Skip logic

- If Q1 ≤ 1 (very low tool usage) → skip Q17-Q20 (Agent questions)
- If Q15 = 0 and Q16 = 0 → skip Q12 (cross-functional process question)

### Submit + What's next

> Your report will be reviewed by a consultant and sent within 3 working days.

---

## C. 50-Question Version (Full Pre-Interview Inventory)

### Form intro

> 50 questions, ~20 minutes. Recommended to be completed by IT / AI Champion before the consulting interview. Covers the six constructs + deployment mode + systems inventory + governance.

### Page structure

| Page | Scope | Questions |
| --- | --- | --- |
| 1 | Profile + Industry + Size + Deployment preference | 8 |
| 2 | Tool Usage (which tools, who uses them, frequency) | 7 |
| 3 | Knowledge Codification | 7 |
| 4 | Process Standardization | 7 |
| 5 | System Integration (12 systems yes/no + integration depth) | 8 |
| 6 | Agent Application | 6 |
| 7 | Governance & ROI + Audit + Compliance | 7 |
| Submit | | 50 |

### Skip logic

- Q-Profile.industry = "manufacturing" → extra questions: MES / SPC / WMS systems
- Q-Profile.industry = "hospital" → extra questions: HIS / EMR / LIS / PACS
- Q-deployment = "on-prem" → extra questions: GPU, Llama, machine-room capacity

### Optional open questions

- O1 What is your biggest current AI pain point?
- O2 Your most successful AI case in the past 12 months?
- O3 Your most failed AI case in the past 12 months?
- O4 What topics do you most want to discuss in the consulting interview?

### Output → Eight-stage consulting Stage 1 pre-interview brief

Automatically organizes the 50 answers + open responses into Markdown. The consultant receives the brief 1 hour before the interview, containing:
- AI Usage Inventory (auto-populated)
- Systems Inventory (auto-populated)
- Inferred pain points (auto-derived from low-score constructs)
- Recommended interview focus

---

## D. Platform Rendering Hints

### Google Form
- Use Section headers to split into pages for Profile
- Use Linear Scale for the 0-4 scale
- Use "Go to section based on answer" for skip logic
- Results write to a connected Sheet → trigger Apps Script → send report

### Tally
- More flexible logic / multilingual switching / built-in webhook
- Recommended: an n8n webhook node listening directly to Tally submit

### Notion Form (Beta)
- Writes directly into a Notion Database
- Use Notion Automation to trigger page creation
- Suitable for Notion-first clients

---

## E. Onboarding for a Client

1. Consultant creates a client-specific Form (copy the template)
2. Set the client logo + email subject
3. Connect to the client's n8n instance webhook
4. Client IT confirms the webhook URL whitelist
5. Sales sends the form link to the target respondents
6. Monitor the n8n `aid_runs` Data Table to confirm inflow is normal
7. Client completes the form → auto report → consultant interpretation → 1-on-1

Full schema and n8n flow: see `AI_DIAGNOSIS_SHEETS_SCHEMA.md`.
