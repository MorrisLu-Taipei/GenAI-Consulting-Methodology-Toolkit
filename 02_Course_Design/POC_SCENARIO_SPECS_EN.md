# PoC Scenario Specifications

> 🌐 中文版本 / Chinese version: [POC_SCENARIO_SPECS.md](POC_SCENARIO_SPECS.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>

An **implementable PoC scenario library** for the L3 Workflow AI and L4 Hermes Agent courses. 30 PoCs across 6 systems, each completable in 1-3 work days, with full input/output, AI steps, KPIs, and n8n node sequences.

---

## PoC Template

```
### PoC ID — Title
- Business outcome: one-sentence business result
- Trigger: trigger source
- Input: input data / event / source
- AI step: what the LLM does + prompt-design notes
- Systems touched
- Output: where the output goes
- Acceptance criteria: 3 bullets
- KPI
- Estimated effort: person-days
- L-level: L3 / L4
- Sample n8n node sequence: 5-10 nodes
```

---

## 1. Gmail PoCs (4)

### G-1 — Customer-Service Email Triage
- Business outcome: customer-service emails auto-classified into "complaint / inquiry / repair / other" and tagged P0-P3 priority
- Trigger: new mail in Gmail (Webhook / IMAP / Gmail API push)
- Input: sender, subject, body, attachments
- AI step: Claude / GPT-4 prompt — system prompt contains classification definitions and enterprise SLA; user prompt is the full email; output JSON `{category, priority, summary, suggested_action}`
- Systems touched: Gmail, Sheets (Log)
- Output: auto-add Gmail Label + route to the matching mailbox + Slack notification for P0
- Acceptance criteria: classification accuracy ≥ 90%, miss rate ≤ 5%, P0 notified within 5 min
- KPI: first response time ↓ 50%, missed cases ↓ 70%
- Effort: 1 person-day
- L-level: L3
- n8n nodes: Gmail Trigger → Set (extract) → OpenAI Chat → IF (P0) → Gmail Label / Move + Slack + Sheets Append

### G-2 — Sales Email Summary & Action List
- Business outcome: each sales rep gets a "past-24h customer email summary + must-do action list" email at 7am
- Trigger: Schedule (Cron 7am)
- Input: past-24h Gmail mail labeled "customer"
- AI step: consolidate → 2-line summary per email + tag "customer issue / quote / complaint / opportunity" + extract action items
- Systems touched: Gmail, Notion (Action DB)
- Output: email to the rep + write to Notion Action DB
- Acceptance: summary matches original intent ≥ 95%, action items directly actionable
- KPI: daily review time 90 min → 20 min
- Effort: 1.5 person-days
- L-level: L3
- n8n nodes: Schedule → Gmail (search 24h) → Loop Over → OpenAI Chat → Merge → Format Email → Gmail Send + Notion Create

### G-3 — Executive Daily Digest
- Business outcome: the manager isn't drowned by 200+ emails; a 1-page digest every morning
- Trigger: Schedule 8am
- Input: all of the manager's inbox over the past 24h
- AI step: filter by importance (CC, sender seniority, keywords, key-account list); produce "Top 5 must-read + Top 10 skimmable + a recommended action"
- Systems touched: Gmail
- Output: HTML email
- Acceptance: the manager agrees with the Top 5; tune the prompt weekly
- KPI: manager inbox processing time ↓ 60%
- Effort: 1 person-day
- L-level: L3
- n8n nodes: Schedule → Gmail (search) → Function (rank) → OpenAI → Format HTML → Gmail Send

### G-4 — Auto-Reply Draft
- Business outcome: within 30 seconds of receiving an email, the agent sees a "suggested reply draft" in a Gmail draft
- Trigger: Gmail Webhook
- Input: customer question
- AI step: RAG over the FAQ Notion DB → draft; tagged `[AI Draft - please review]`
- Systems touched: Gmail, Notion FAQ
- Output: Gmail Draft
- Acceptance: directly-sendable rate ≥ 60%; non-sendable cases do not damage trust
- KPI: average CS handling time ↓ 40%
- Effort: 2 person-days
- L-level: L3 / L4 (after upgrading to an Agent it can learn corrections)
- n8n nodes: Gmail Trigger → Notion Search (RAG) → OpenAI Chat → Gmail Create Draft

---

## 2. Google Sheets PoCs (5)

### S-1 — Questionnaire Ingestion & Auto-Scoring
- Business outcome: fill out the questionnaire → see score + customized recommendations within 24h
- Trigger: Google Form Submit
- Input: questionnaire answers
- AI step: Apps Script / Function scoring + LLM writes a personalized recommendation paragraph
- Systems touched: Form, Sheets, Gmail
- Output: Sheet update + email
- Acceptance: score correct, email sent within 1h
- KPI: time from submission to consultant contact 7d → 1d
- Effort: 1 person-day
- L-level: L3
- n8n nodes: Webhook (Form) → Set → Function (score) → OpenAI Chat → Sheets Append → Gmail

### S-2 — Monthly KPI Auto-Refresh
- Business outcome: at the start of the month, automatically pull each department's KPIs and consolidate them into a manager dashboard
- Trigger: Schedule, 1st of month, 6am
- Input: each department's Sheet / API
- AI step: consolidate + anomaly identification + text interpretation
- Systems touched: Sheets, various data sources
- Output: master dashboard + email digest
- Acceptance: each KPI has a source + anomaly annotation
- KPI: monthly-report production time 16 hr → 30 min
- Effort: 2 person-days
- L-level: L3
- n8n nodes: Schedule → HTTP (sources) → Function → Sheets Update → OpenAI → Email

### S-3 — Workflow Execution Log & Failure Monitoring
- Business outcome: all n8n workflow executions write to a Sheet; failures alert Slack in real time
- Trigger: n8n global Workflow End
- Input: execution metadata
- AI step: on failure, the LLM summarizes the root cause (reads the stack + compares with last success)
- Systems touched: n8n, Sheets, Slack
- Output: Sheet log + Slack alert
- Acceptance: all workflows are logged; failures alert within 30 sec
- KPI: MTTR (mean time to recover) ↓ 70%
- Effort: 1 person-day
- L-level: L3
- n8n nodes: Error Trigger → Set → OpenAI Chat → Slack + Sheets

### S-4 — Customer List De-dup & Classification
- Business outcome: merge, de-dup, and classify customer lists from 3 sources
- Trigger: Manual or Webhook
- Input: 3 Sheets/CSVs
- AI step: LLM handles fuzzy matching (name variations, EN-zh equivalents) + classification
- Systems touched: Sheets
- Output: merged Sheet
- Acceptance: de-dup accuracy ≥ 98%
- KPI: manual de-dup 8 hr → 30 min
- Effort: 1.5 person-days
- L-level: L3
- n8n nodes: Manual Trigger → Sheets (3 sources) → Merge → Function (initial dedup) → OpenAI (fuzzy) → Sheets Output

### S-5 — Budget vs Spend Variance
- Business outcome: at month-end, automatically produce an "actual vs budget" variance report + AI interpretation
- Trigger: Schedule, month-end
- Input: budget Sheet + ERP spend
- AI step: for variances > 10%, automatically list causes (based on historical data)
- Systems touched: Sheets, SAP/Oracle ERP
- Output: report + email
- Acceptance: variance list complete, AI interpretation reasonable
- KPI: CFO review time ↓ 50%
- Effort: 2 person-days
- L-level: L3
- n8n nodes: Schedule → SAP API + Sheets → Merge → Function (compare) → OpenAI → Format → Email

---

## 3. Notion PoCs (5)

### N-1 — Meeting Transcript → Summary + Action Items
- Business outcome: meeting recording → summary + actions in Notion within 5 minutes
- Trigger: Notion Page Webhook (audio file uploaded)
- Input: m4a / mp3
- AI step: Whisper transcription → Claude/GPT summary + extract action items (with owner, due)
- Systems touched: Notion, Whisper API
- Output: Notion child page (Meeting Notes + Actions DB rows)
- Acceptance: action items with an owner ≥ 80%
- KPI: post-meeting follow-up time 90 min → 5 min
- Effort: 2 person-days
- L-level: L3 / L4
- n8n nodes: Notion Trigger → HTTP (Whisper) → OpenAI Chat → Function (parse actions) → Notion Update + Notion Create (Actions DB)

### N-2 — Consulting Diagnostic Database
- Business outcome: each client has a complete Notion workspace: profile, interview notes, scoring, roadmap, actions
- Trigger: n8n Webhook (new client)
- Input: client basic information
- AI step: generate a customized structure from a template + pre-fill preliminary hypotheses
- Systems touched: Notion
- Output: structured Notion pages
- Acceptance: all required sections present, relations set correctly
- KPI: new-client onboarding 4 hr → 15 min
- Effort: 1.5 person-days
- L-level: L3
- n8n nodes: Webhook → OpenAI Chat (generate outline) → Loop → Notion Create (per page) → Notion Update (relations)

### N-3 — Skill Library Template & Versioning
- Business outcome: each Skill in Notion has IPOE, Owner, version, test cases
- Trigger: Manual (new Skill creation)
- Input: Skill name + brief description
- AI step: generate an IPOE draft and test-case examples from the Skill description
- Systems touched: Notion, GitHub (backup)
- Output: Notion page + GitHub markdown
- Acceptance: each Skill has IPOE + ≥ 3 test cases + Owner
- KPI: Skill onboarding time 60 min → 10 min
- Effort: 1.5 person-days
- L-level: L3 / L4
- n8n nodes: Webhook → OpenAI Chat → Notion Create → GitHub Create File

### N-4 — Auto Task Assignment
- Business outcome: tasks arriving from Sheets / Webhook automatically create a Notion task + assign an owner + notify
- Trigger: Sheets Append or Webhook
- Input: task description, deadline, dept
- AI step: the LLM determines the best owner from the dept skill matrix + breaks down subtasks
- Systems touched: Sheets / Notion / Slack
- Output: Notion task DB rows + Slack DM
- Acceptance: assignment accuracy ≥ 90%
- KPI: task assignment time ↓ 70%
- Effort: 2 person-days
- L-level: L3
- n8n nodes: Trigger → Notion Search (skill matrix) → OpenAI → Notion Create + Slack DM

### N-5 — Internal Q&A over Notion
- Business outcome: an employee asks a question in Slack, the bot answers from the company-wide Notion knowledge base
- Trigger: Slack message (DM or mention)
- Input: natural-language question
- AI step: embedding match → retrieve Top-5 chunks → Claude / GPT answer + source links
- Systems touched: Slack, Notion, Vector DB (Pinecone / Qdrant / Chroma)
- Output: Slack reply with sources
- Acceptance: 100% of answers have source links, answer accuracy ≥ 85%
- KPI: repeated HR / IT Q&A ↓ 60%
- Effort: 3 person-days (including the embedding pipeline)
- L-level: L4 (near the Agent boundary)
- n8n nodes: Slack Trigger → HTTP (embedding query) → HTTP (vector search) → OpenAI Chat → Slack Reply

---

## 4. CRM PoCs (5) — HubSpot / Salesforce as canonical examples

### C-1 — Conversational Customer Lookup
- Business outcome: a rep asks "what was Client X's last interaction" in Slack/Teams and gets an instant answer
- Trigger: Slack mention bot
- Input: customer name (fuzzy)
- AI step: fuzzy match → CRM API → summarized reply
- Systems touched: Slack, CRM
- Output: Slack reply
- Acceptance: fuzzy match accuracy ≥ 95%, reply < 10 sec
- KPI: rep lookup time ↓ 90%
- Effort: 1.5 person-days
- L-level: L3
- n8n nodes: Slack Trigger → CRM Search → OpenAI (summary) → Slack Reply

### C-2 — Opportunity Summary & Next-Step Recommendation
- Business outcome: every Sunday evening, automatically produce a Top 20 opportunity brief + recommended next steps
- Trigger: Schedule Sun 8pm
- Input: CRM Pipeline deals > NT$ 100K
- AI step: summarize stage, past interactions, industry context, recommend next step
- Systems touched: CRM, Email, Notion
- Output: each AE gets an email + Notion child page
- Acceptance: recommended next step is actionable ≥ 70%
- KPI: weekly 1-on-1 review time ↓ 50%
- Effort: 2 person-days
- L-level: L3 / L4
- n8n nodes: Schedule → CRM API → Loop → OpenAI Chat → Format → Email + Notion

### C-3 — Post-Visit Note Auto-Update
- Business outcome: a rep dictates visit highlights (Slack voice / text) → automatically written into the CRM
- Trigger: Slack DM to bot
- Input: voice / text
- AI step: Whisper + structured extraction (who, when, what was discussed, next step) → CRM update
- Systems touched: Slack, CRM, Whisper
- Output: CRM activity record
- Acceptance: field fill rate ≥ 90%
- KPI: CRM update rate ↑ 60%
- Effort: 2 person-days
- L-level: L3 / L4
- n8n nodes: Slack Trigger → Whisper → OpenAI (extract) → CRM Update

### C-4 — Complaint Tracking & Escalation
- Business outcome: complaints not responded to within SLA are automatically escalated
- Trigger: Schedule every 30 min + CRM Webhook
- Input: complaint case
- AI step: assess case sentiment, estimate time sensitivity, escalate to whom
- Systems touched: CRM, Slack
- Output: Slack alert + CRM flag
- Acceptance: SLA-violation rate ↓ 80%
- KPI: complaint escalation time ↓ 70%
- Effort: 1.5 person-days
- L-level: L3
- n8n nodes: CRM Webhook + Schedule → Function (SLA check) → OpenAI (sentiment) → Slack + CRM Update

### C-5 — Customer Health Score
- Business outcome: weekly churn-risk score per customer; Top 10 risks notify the CSM
- Trigger: Schedule Mon 9am
- Input: CRM interactions + product usage + billing
- AI step: Function computes the score + the LLM writes a why-it-changed narrative
- Systems touched: CRM, Product DB, Billing
- Output: CRM score field + Slack alert
- Acceptance: score is explainable, Top 10 triggers actual intervention
- KPI: annual churn rate ↓ 15%
- Effort: 3 person-days
- L-level: L4
- n8n nodes: Schedule → CRM + DB + Billing → Merge → Function → OpenAI → CRM Update + Slack

---

## 5. API PoCs (5)

### A-1 — Internal Webhook Subscriber
- Business outcome: subscribe to internal events (new customer, order, anomaly) and process them automatically
- Trigger: Webhook
- Input: JSON event payload
- AI step: classify the event, decide routing
- Systems touched: n8n, internal services
- Output: routed to the matching workflow
- Acceptance: every event has an audit log
- KPI: internal-event processing latency ↓ 80%
- Effort: 1 person-day
- L-level: L3
- n8n nodes: Webhook → Switch → route to sub-workflows

### A-2 — External API Integration
- Business outcome: a unified interface for reps to look up weather / shipping / maps / company data
- Trigger: Slack mention or chatbot
- Input: natural language
- AI step: determine which API is needed, compose the answer
- Systems touched: multiple external APIs
- Output: Slack reply
- Acceptance: correct API switching, integrated answer
- KPI: employee self-service lookup rate ↑
- Effort: 2 person-days
- L-level: L3 / L4
- n8n nodes: Slack Trigger → OpenAI (intent) → Switch → HTTP (matching API) → OpenAI (format) → Slack

### A-3 — Retry & Idempotency
- Business outcome: unstable APIs do not corrupt data
- Trigger: internal to an n8n workflow
- Input: API call
- AI step: N/A (pure logic)
- Systems touched: External API, Data Table (idempotency key)
- Output: success or dead-letter queue
- Acceptance: repeated calls with the same idempotency key are not double-processed
- KPI: duplicate data ↓ 100%
- Effort: 1 person-day
- L-level: L3
- n8n nodes: Function (gen key) → Data Table Lookup (skip if exists) → HTTP with retry → On Error → Data Table (DLQ)

### A-4 — Rate-Limit Handling & Scheduling
- Business outcome: avoid being blocked by the API vendor
- Trigger: Schedule + Queue
- Input: batch to process
- AI step: N/A
- Systems touched: External API
- Output: batch complete
- Acceptance: ≤ rate limit per second; overflow goes to a queue
- KPI: API failure rate ↓
- Effort: 1.5 person-days
- L-level: L3
- n8n nodes: Trigger → Loop with Wait → HTTP → If 429 → Wait + Retry

### A-5 — Multi-API Aggregation
- Business outcome: one query calls 3+ APIs and consolidates
- Trigger: Webhook / Slack
- Input: query
- AI step: distributed queries → result integration → answer
- Systems touched: 3+ APIs
- Output: merged result
- Acceptance: integration with no omissions
- KPI: query completion time ↓ 60%
- Effort: 2 person-days
- L-level: L3
- n8n nodes: Trigger → Split In Batches → HTTP (parallel) → Merge → OpenAI (synthesize) → Reply

---

## 6. ERP PoCs (6) — SAP B1 / Oracle / generic ERP as examples

### E-1 — Order Status Lookup
- Business outcome: sales / CS ask about an order in Slack and get an instant answer
- Trigger: Slack mention
- Input: order number or customer name
- AI step: fuzzy lookup → format
- Systems touched: Slack, ERP
- Output: Slack reply
- Acceptance: response < 5 sec
- KPI: CS order-lookup time ↓ 90%
- Effort: 1.5 person-days
- L-level: L3
- n8n nodes: Slack Trigger → ERP API → OpenAI (format) → Slack Reply

### E-2 — Inventory Anomaly Alert
- Business outcome: inventory below safety stock / expired / slow-moving auto-alerts
- Trigger: Schedule every 6 hr
- Input: inventory report
- AI step: rule check + LLM interprets "why the anomaly + recommendation"
- Systems touched: ERP, Slack
- Output: Slack alert
- Acceptance: alert accuracy ≥ 95%
- KPI: shortage / slow-moving cost ↓ 20%
- Effort: 2 person-days
- L-level: L3
- n8n nodes: Schedule → ERP API → Function (rule) → OpenAI → Slack

### E-3 — Shipping Delay Analysis
- Business outcome: daily root-cause analysis of shipping-delay cases
- Trigger: Schedule 6pm
- Input: the day's SOs + shipping records
- AI step: determine the delay cause (materials / logistics / customer / system)
- Systems touched: ERP, WMS, logistics system
- Output: email digest to the operations manager
- Acceptance: classification accuracy ≥ 85%
- KPI: time to identify delay root cause ↓ 70%
- Effort: 2.5 person-days
- L-level: L3 / L4
- n8n nodes: Schedule → ERP + WMS + logistics → Merge → OpenAI → Email

### E-4 — Purchase Reconciliation Diff
- Business outcome: invoice-vs-PO variance > 5% auto-flagged
- Trigger: Schedule month-end + Webhook
- Input: invoice OCR + PO
- AI step: reconciliation logic + variance-cause suggestions
- Systems touched: ERP, OCR
- Output: Sheet + Slack
- Acceptance: variance identification accuracy ≥ 95%
- KPI: reconciliation person-days ↓ 60%
- Effort: 3 person-days
- L-level: L3 / L4
- n8n nodes: Schedule → ERP API → OCR → Merge → Function → OpenAI → Sheets

### E-5 — Month-End Exception Summary
- Business outcome: the CFO receives an exception-item summary within 24h of month-end close
- Trigger: Schedule month-end + 1 day
- Input: general-ledger movements
- AI step: find exceptions (cross-month, new accounts, large amounts), consolidate a summary
- Systems touched: ERP, Email
- Output: CFO email + Notion archive
- Acceptance: CFO finds the summary useful ≥ 80%
- KPI: CFO month-end review time ↓ 50%
- Effort: 3 person-days
- L-level: L4
- n8n nodes: Schedule → ERP GL Query → Function → OpenAI → Email + Notion

### E-6 — Daily Cross-Functional KPI Digest
- Business outcome: managers receive a one-page cross-functional KPI digest at 8am daily
- Trigger: Schedule 8am
- Input: ERP + CRM + Sheets KPIs
- AI step: customize per role, highlight changes
- Systems touched: ERP, CRM, Sheets, Email
- Output: email per role
- Acceptance: each manager finds one thing worth acting on
- KPI: manager KPI review time 30 min → 5 min
- Effort: 2 person-days
- L-level: L4
- n8n nodes: Schedule → multiple sources → Merge → OpenAI per role → Email

---

## Selection Guide

### Recommended PoCs by client L-level

| Client starting point | Recommended priority PoCs | Why |
| --- | --- | --- |
| L1 → L2 | G-1, G-4, S-1 | employees feel it daily, low risk, immediate impact |
| L2 → L3 | S-2, S-3, N-1, C-1, A-1 | begin system integration, show ROI |
| L3 → L4 | C-2, C-5, N-5, E-5, E-6 | high complexity, need a Wiki and Reviewer |
| L4 → L5 | cross-PoC combinations (e.g., E-3 + C-4 + N-1 → ClawTeam) | multi-Agent chaining |

### Recommended by industry

| Industry | Top 3 PoCs |
| --- | --- |
| Manufacturing | E-2, E-3, S-2 |
| Hospital | N-5, G-1, C-4 (patient-service case) |
| Retail | C-2, C-5, S-2 |
| B2B SaaS | C-2, C-5, A-2 |
| Pro Services | N-1, N-3, N-5 |

### By data sensitivity

| Sensitivity | Recommended deployment | PoC rewrite |
| --- | --- | --- |
| Low | cloud OpenAI / Claude | all PoCs |
| Medium | Hybrid (LLM after redaction) | add a redaction step |
| High | full on-prem Llama 70B | change OpenAI Chat → Local LLM HTTP |

---

## Cross-Cutting Requirements

Regardless of detail, every PoC must:

- have an audit log (write to the `aid_audit` Data Table)
- have error handling (Error Trigger → DLQ)
- have an idempotency key (avoid duplicates)
- have a GitHub backup workflow (periodic export)
- have a Reviewer / Human Gate (for major decisions)
- pass Stage Gate 3 (L3) or 4 (L4) before going live

Full schema: see `01_Assessment/AI_DIAGNOSIS_SHEETS_SCHEMA.md`, `02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`.
