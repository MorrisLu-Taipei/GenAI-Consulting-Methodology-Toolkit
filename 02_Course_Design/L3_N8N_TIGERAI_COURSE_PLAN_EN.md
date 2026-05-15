> 🌐 中文版本 / Chinese version: [L3_N8N_TIGERAI_COURSE_PLAN.md](L3_N8N_TIGERAI_COURSE_PLAN.md)

# L3 n8n Workflow AI Course Plan

Version: v1.1
Author: Morris Lu (盧業興) · Tiger AI 虎智科技
Applicable Level: L3 Workflow Automation
Reference Sources:

- n8n / OpenGenie videos on the TigerAI YouTube channel
  Channel: `https://www.youtube.com/@%E8%99%8E%E6%99%BA%E7%A7%91%E6%8A%80TigerAI`
- TigerAI-n8n-Skill-Pack (Morris Lu, TigerAI Proprietary + partial MIT): 13 Skills + 8 cookbook recipes + 2,061 reference workflows that generate n8n workflow JSON from natural language, supporting Antigravity + Claude Code + n8n
  `https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`
  Citation and license notice: see [`../90_References/N8N_SKILL_PACK_REFERENCE.md`](../90_References/N8N_SKILL_PACK_REFERENCE.md)

---

## 1. Repositioning L3

L3 is not just about teaching students "how to drag n8n nodes." The true objective of L3 is:

> Take over from the Skills / Workflow Blueprints produced in L2 and use n8n to build executable, verifiable, operable, backup-protected enterprise process PoCs that can also be invoked by L4 Agents.

The L3 spirit conveyed by TigerAI videos is:

1. Start with L2 Skills and Workflow Blueprints.
2. Use n8n to connect Trigger, Credential, Data, AI, and Platform Action.
3. Use Data Tables / Sheets / DB to persist state.
4. Use Sub-workflows to form reusable process modules.
5. Use Execution Log, GitHub Backup, human gates, and error handling to make the workflow operable.
6. Finally, hand the working Workflow over to the L4 Hermes Agent to call.

### 1.1 The L3 Course Is Split into a First Half and a Second Half

The L3 course follows a "concepts first, generation second" principle and is split into two halves; students may not skip a half:

| Half | Content | Corresponding Course | Focus |
|---|---|---|---|
| **L3 First Half** | n8n / AI-workflow fundamentals and hand-building | §5.1 Foundation, §5.2 Builder | Hand-build Trigger / Node / AI / Gate / Log first, understanding the structure and governance of a workflow |
| **L3 Second Half** | Generating workflows from natural language with Antigravity (AG) + TigerAI-n8n-Skill-Pack | §5.3 Advanced, §5.5 AG + Skill Pack | On the foundation of understanding structure, use an AI IDE to turn natural-language intent directly into deployable workflow JSON |

> **Why learn the concepts before the Skill Pack:** TigerAI-n8n-Skill-Pack can turn a natural-language "sticky note" directly into workflow JSON, but if students have not first hand-built a workflow in the first half and do not understand the structure of Trigger / Credential / Human Gate / Error Handling, they cannot judge whether the generated result is correct, safe, or operable. **The Skill Pack is an accelerator, not a substitute for understanding.**

---

## 2. Course Objectives

After completing the L3 course, students should be able to:

1. Read and understand a Workflow Blueprint produced by L2.
2. Create Triggers, Nodes, Credentials, Webhooks, and Executions in n8n.
3. Integrate Gmail, LINE, Facebook, YouTube, Google Sheets, Data Tables, APIs, CRMs, ERPs, or other platforms.
4. Use Gemini / AI Nodes to process text, images, audio, video, and documents.
5. Build Sub-workflows to modularize reusable processes.
6. Build Data Tables Schemas or state tables.
7. Design human-review gates to prevent the AI from auto-publishing high-risk content.
8. Design error handling, notification, retry, and fallback.
9. Back up Workflows and Credentials to GitHub or a designated version repository.
10. Produce auditable Workflow JSON, Execution Logs, test logs, and operations Runbooks.

---

## 3. Prerequisites

| Item | Minimum Requirement |
|---|---|
| L2 Blueprint | At least 1 Workflow Blueprint including trigger, I/O schema, sample payload, and human gate |
| n8n environment | Access to n8n Cloud or a self-hosted instance |
| Test accounts | Test accounts for Gmail, LINE, Facebook, YouTube, Google / Meta / API |
| Credentials | API keys, OAuth, Webhook permissions, test tokens |
| Test data | De-identified emails, resumes, product images, comments, customer service questions, lookup data |
| Governance rules | Whether to allow automated posting, replies, external APIs, AI image generation, or video generation |
| Backup strategy | GitHub repo or internal version repository |

---

## 4. L3 n8n IPOE

| Category | Definition |
|---|---|
| Input | L2 Workflow Blueprint, trigger event, sample payload, API credential, test data, AI prompt, table schema, human review rules |
| Process | Build workflow, configure trigger, read/write data, invoke AI, transform formats, integrate platforms, human review, error handling, execution logs, backup |
| Output | n8n Workflow JSON, Data Tables, platform replies, notifications, reports, post drafts, customer service drafts, HR screening results, backup repo, operations documents |
| Evidence | Execution Log, test payload, output screenshots, Data Tables / Sheets records, GitHub backup commit, review records, error test logs |

---

## 5. Course Versions

### 5.1 L3 Foundation: 3 Hours

Goal: Build n8n fundamentals and the ability to take over from L2.

| Time | Topic | Content | Output |
|---|---|---|---|
| 30 min | L3 positioning | From L2 Blueprint to n8n Workflow | L3 consensus |
| 45 min | n8n fundamentals | Trigger, Node, Credential, Webhook, Execution | Basic flow |
| 45 min | Blueprint conversion | Trigger, I/O schema, sample payload, node map | Conversion sheet |
| 45 min | AI Node / Gemini | AI processing for text, images, and documents | AI node demo |
| 45 min | Gate / Log | Human review, Execution Log, failure tests | Gate / Log sheet |

### 5.2 L3 Builder: 1 Day

Goal: Complete a verifiable n8n Workflow PoC.

| Time | Topic | Content | Output |
|---|---|---|---|
| 60 min | Trigger implementation | Webhook, Gmail, LINE, Facebook, or schedule | Trigger node |
| 60 min | Data handling | Set, Code, Merge, Data Tables, Sheets | Data schema |
| 90 min | AI processing | Gemini / AI classification, summarization, drafting, multimodal analysis | AI step |
| 90 min | Platform action | LINE reply, Gmail notification, Facebook reply, Sheets / CRM write | System output |
| 60 min | Human Gate | Human review for posting, replies, resume screening, CS drafts | Review node |
| 60 min | Error / retry | Error notification, retry, fallback | Error test |
| 90 min | Demo / Review | Test with 2 normal and 1 error payload | Execution Log |

### 5.3 L3 Advanced: 1 Day

Goal: Round out enterprise operations, modularization, and governance.

| Time | Topic | Content | Output |
|---|---|---|---|
| 90 min | Sub-workflow | Modularize AI classification, notification, review, and data-table writes | Sub-workflow library |
| 75 min | Data Tables | Customer service status, FAQ, allow/deny lists, interaction history | Data Tables schema |
| 75 min | GitHub backup | Workflow / Credential backup strategy | Backup SOP |
| 60 min | Credential governance | API key, OAuth, permissions, environment variables | Credential matrix |
| 60 min | Monitoring | Execution Log, failure notification, manual rerun | Operations sheet |
| 90 min | L4 readiness | Wrap the workflow into a task callable by Hermes Agent | Workflow contract |

### 5.4 L3 Enterprise Lab: 2 Days

Goal: Use the client's own scenario to complete a deliverable PoC.

| Time | Topic | Content | Output |
|---|---|---|---|
| Day 1 AM | Use case selection | Pick a process from L2 Blueprint | PoC Brief |
| Day 1 PM | Build | Trigger, AI, Data, Platform Action | Workflow PoC |
| Day 2 AM | Governance | Human Gate, Log, Error, Backup, Credential | Operations and governance |
| Day 2 PM | Acceptance | Demo, Execution Log, documentation, L4 contract | Gate 3 acceptance |

### 5.5 L3 Second-Half Core: AG + TigerAI-n8n-Skill-Pack: 1 Day

> Citation: [`MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack). Full citation and license notice: see [`../90_References/N8N_SKILL_PACK_REFERENCE.md`](../90_References/N8N_SKILL_PACK_REFERENCE.md).
>
> **Prerequisite: students must first complete the L3 first half (§5.1 Foundation + §5.2 Builder)** and must have hand-built at least 1 workflow that includes Trigger / AI / Human Gate / Error Handling.

Goal: On the foundation of understanding n8n workflow structure, use Antigravity (AG) + TigerAI-n8n-Skill-Pack to turn natural-language intent directly into deployable, verifiable workflow JSON, and learn to review the generated results.

| Time | Topic | Content | Output |
|---|---|---|---|
| 45 min | Skill Pack concepts | Three-layer structure (yellow sticky-note intent + blue sticky-note annotations + workflow nodes), DSL v1.2, 13 Skills / 8 cookbook / 2,061 reference workflows | Skill Pack structure notes |
| 30 min | Install and configure | `install.sh` / `install.ps1`, AG and Claude Code integration, n8n 2.10.3+ | Installation record |
| 60 min | Cookbook mode | Pick a template from the 8 cookbook recipes, rewrite the intent in natural language | First generated workflow |
| 75 min | Q&A generation mode | AI-guided requirements gathering → three-layer JSON generation → compare against the L2 Workflow Blueprint | Second generated workflow |
| 60 min | Reviewing generated results | Use the structural knowledge from the first half to check: Is the Trigger right? Are Credential / Human Gate / Error Handling present? Is it operable? | Generated-result review sheet |
| 45 min | Example finder | Find similar implementations among the 2,061 reference workflows, compare and borrow | Reference-implementation comparison |
| 45 min | Deploy and accept | Deploy via the n8n API, run the Execution Log, align with Gate 3 | Execution Log + Gate 3 comparison |

#### 5.5.1 Governance and Red Lines

- TigerAI-n8n-Skill-Pack's `skills/_vendor/` and `reference-workflows/` are **MIT**; the remaining Skills / Cookbook / Spec are **TigerAI Proprietary**. For citation and redistribution, follow [`../90_References/N8N_SKILL_PACK_REFERENCE.md`](../90_References/N8N_SKILL_PACK_REFERENCE.md).
- **Generation is not acceptance:** AI-generated workflows must always be reviewed by students using first-half knowledge and must pass Gates 3A-3G; without passing, they cannot be claimed as enterprise-grade PoCs.
- For sensitive-data scenarios: if a generated workflow contains an LLM node, switch it to an on-prem / Azure OpenAI isolated tenant and prepend redaction.
- The reference workflows have had secrets scrubbed, but you must still confirm there are no residual internal endpoints / accounts before using them as templates.

#### 5.5.2 §5.5 Deliverables

- TigerAI-n8n-Skill-Pack installation record.
- At least 2 workflow JSON files generated with AG + Skill Pack (1 in cookbook mode, 1 in Q&A mode).
- Generated-result review sheet (compared against first-half structural knowledge).
- Reference-workflow implementation comparison.
- Deployment Execution Log + Gate 3 comparison sheet.

---

## 6. TigerAI Videos Mapped to Course Modules

| Course Module | Reference Video | Course Use |
|---|---|---|
| L3 entry point | OpenGenie Unit 7: Integrating n8n with Automated Workflows | Explains how OpenGenie / OpenWebUI connect with n8n |
| AI Node | n8n 27: Gemini analysis for images, audio, video, documents | AI multimodal processing |
| Sub-workflow | n8n 28: Sub-workflow modularization | Build reusable process templates |
| Query Bot | n8n 29: HSR timetable lookup bot | LINE + API lookup |
| HR process | n8n 30: Automated resume screening | Gmail + Gemini + LINE notification |
| Marketing process | n8n 31, 32, 38, 39 | Images, copy, keywords, video, social publishing |
| Community interaction | n8n 33 | YouTube comment auto-reply |
| Operations governance | n8n 34: GitHub Backup | Workflow / Credential backup |
| Customer service process | n8n 35, 36, 37 | Facebook Webhook, Data Tables, image and message replies |
| Management feedback | OpenGenie Unit 10 | Oversight, feedback, quality improvement |

---

## 7. PoC Case Pack

### 7.1 Customer Service Automation PoC

Reference videos: n8n 35, 36, 37.

Flow:

`Facebook / LINE / Email intake → Webhook → Data Tables FAQ / status lookup → AI reply draft → Human Gate → Reply / notification → Log`

Deliverables:

- Webhook Trigger.
- Data Tables Schema.
- AI reply Prompt.
- Human Gate.
- Execution Log.
- CS manager acceptance sheet.

### 7.2 HR Resume Screening PoC

Reference video: n8n 30.

Flow:

`Gmail receives resume → Attachment / body extraction → Gemini screening → Score and summary → LINE / Email notification → Sheets / DB record`

Deliverables:

- Resume data schema.
- Scoring rules.
- AI screening Prompt.
- Notification node.
- Human review node.

### 7.3 Marketing Automation PoC

Reference videos: n8n 31, 32, 33, 38, 39.

Flow:

`Product / topic input → AI finds keywords / images / copy / video → Generate drafts → Human review → Multi-platform scheduled publishing → Performance recording`

Deliverables:

- Content Brief.
- Keyword / image / copy pipeline.
- Post drafts.
- Human review Gate.
- Multi-platform publishing log.

### 7.4 Real-time Query Bot PoC

Reference video: n8n 29.

Flow:

`LINE question → Webhook → API lookup → AI formats answer → LINE reply → Log`

Deliverables:

- Webhook URL.
- API query spec.
- Reply format.
- Error fallback.

---

## 8. L3 Control Sheet

| Control | Required Content | Evidence |
|---|---|---|
| Workflow name | `[Name]` | Workflow Blueprint |
| Business Owner | `[Department / Person]` | Owner sheet |
| Trigger | `[Webhook / Gmail / LINE / FB / Schedule / API]` | Trigger test |
| Input Schema | `[Field / Type / Example]` | Sample payload |
| Credential | `[API Key / OAuth / Token]` | Credential matrix |
| Data Store | `[Data Tables / Sheets / DB / BigQuery]` | Schema / write log |
| AI Step | `[Gemini / LLM / Prompt]` | AI input/output |
| Platform Action | `[Reply / post / write / notify]` | Output screenshot |
| Human Gate | `[Review conditions / reviewer]` | Review record |
| Error Handling | `[Retry / notify / fallback]` | Failure test |
| Backup | `[GitHub / Repo / JSON export]` | Backup commit |
| Execution Log | `[Success / failure / rerun]` | n8n log |
| L4 Contract | `[How Hermes invokes it]` | Workflow contract |

---

## 9. Stage Gate 3

| Gate | Check Question | Required Evidence | Verdict |
|---|---|---|---|
| Gate 3A: Blueprint usable | Is the L2 Blueprint complete? | Trigger, I/O schema, sample payload | Pass / Fail |
| Gate 3B: Workflow runnable | Can the n8n Workflow process a normal payload? | Execution Log | Pass / Fail |
| Gate 3C: System integration usable | Are at least 2 systems or platforms integrated? | Node settings, output screenshots | Pass / Fail |
| Gate 3D: AI processing verifiable | Can AI classification, summarization, drafting, or multimodal processing be inspected? | AI input/output, test cases | Pass / Fail |
| Gate 3E: Human Gate usable | Are high-risk actions subject to human review? | Review records | Pass / Fail |
| Gate 3F: Operations usable | Are Log, Error, Retry, and Backup present? | Failure tests, GitHub backup | Pass / Fail |
| Gate 3G: L4-ready | Can the Hermes Agent invoke or reference this Workflow? | Workflow contract | Pass / Fail |

If Gate 3F does not pass, the workflow is only a demo, not an enterprise-grade PoC. If Gate 3G does not pass, you may take L3 to production but you cannot claim L4 readiness.

---

## 10. L3 Deliverables

- n8n Workflow Blueprint.
- n8n Workflow JSON.
- Sub-workflow Library.
- Credential / API / Webhook permission sheet.
- Data Tables / Sheets / DB Schema.
- Sample Payload: 2 normal, 1 error.
- Execution Log.
- Human Gate design.
- Error Handling / Retry / Fallback design.
- GitHub Backup / version management SOP.
- L4 Hermes Agent Workflow Contract.
