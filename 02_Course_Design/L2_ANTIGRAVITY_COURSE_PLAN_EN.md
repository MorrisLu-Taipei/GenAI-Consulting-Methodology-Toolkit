> 🌐 中文版本 / Chinese version: [L2_ANTIGRAVITY_COURSE_PLAN.md](L2_ANTIGRAVITY_COURSE_PLAN.md)

# L2 Antigravity Agentic Developer Course Plan

Version: v1.0
Author: Morris Lu (盧業興) · Tiger AI 虎智科技
Applicable Level: L2 Knowledge Codification
Reference Courses:

- Google Codelab: Getting Started with Google Antigravity
  `https://codelabs.developers.google.com/getting-started-google-antigravity?hl=zh-tw`
- Google Codelab: Building with Google Antigravity
  `https://codelabs.developers.google.com/building-with-google-antigravity?hl=zh-tw`
- Google Codelab: Build and Deploy to Google Cloud with Antigravity
  `https://codelabs.developers.google.com/build-and-deploy-gcp-with-antigravity?hl=zh-tw`
- agency-agents (msitarzewski, MIT License): a library of 144+ agent persona definitions, supporting Antigravity / Claude Code / Cursor
  `https://github.com/msitarzewski/agency-agents`
  Citation and license notice: see [`../90_References/AGENCY_AGENTS_REFERENCE.md`](../90_References/AGENCY_AGENTS_REFERENCE.md)

---

## 1. Repositioning L2

The original L2 positioning was to consolidate prompts, SOPs, templates, and checklists into reusable departmental Skills. With the addition of the three Google Antigravity codelabs, L2 can be split into two training tracks:

| Training Track | Audience | Goal |
|---|---|---|
| L2-A Business Skill AI | General departments, PMs, operations, customer service, sales, HR | Turn working experience, SOPs, and prompts into reusable Skills |
| L2-B Agentic Developer AI | IT, engineering, digital transformation, data teams | Use Antigravity to let Agents assist with planning, development, testing, documentation, and cloud deployment |

These three Google codelabs should sit within L2-B. They are not merely IDE tutorials but train students to convert "development work" into engineering capabilities that can be Agent-assisted, reviewed, and accompanied by artifacts and evidence.

---

## 2. Mapping the Three Codelabs to L2 Capabilities

| Codelab | L2 Capability | Course Use | Output |
|---|---|---|---|
| Getting Started with Google Antigravity | Agentic IDE fundamentals and governance | Installation, configuration, Agent Manager, Editor, Browser, permissions, and review policy | Antigravity operational settings table, governance configuration screenshots |
| Building with Google Antigravity | Agent-assisted development and testing | Web research, Flask app, Pomodoro app, unit tests, README / docs | App prototype, test logs, Walkthrough artifact |
| Build and Deploy to Google Cloud with Antigravity | Agent-assisted cloud architecture and deployment | GCS, Pub/Sub, Cloud Run, Gemini, BigQuery, gcloud, verification | Serverless pipeline PoC, deployment log, GCP verification screenshots |

---

## 3. Learning Objectives

> Written per the Bloom formula in [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) §4: **[Verb] + [Content] + [Context]** — assessable and measurable.

### 3.1 Four primary LOs for the CLP

By the end of the L2 course, learners can:

1. **Configure** Antigravity's three governance pillars (terminal execution policy / Review Policy / JavaScript execution policy), **producing** an auditable Agent operation policy table + governance screenshots for their team. (Apply)
2. **Use** Agent Manager to plan and execute a runnable application prototype, **accompanied** by three pieces of acceptable evidence: README + unit tests + walkthrough artifact. (Apply)
3. **Design** a GCP serverless document processing pipeline (GCS + Pub/Sub + Cloud Run + Gemini + BigQuery), **deploying** it to the cloud and completing one real sample end-to-end validation. (Create)
4. **Produce** an L2 Skill Library (≥ 3 reusable Skills), **evaluating** the L3 Workflow candidate and L4 Agent candidate for each Skill, **delivering** them to the L3 course as Workflow Blueprint input. (Evaluate)

### 3.2 Detailed capability list (section mapping)

| Primary LO | Supporting capabilities |
| --- | --- |
| LO1 (governance) | Distinguish Antigravity vs traditional IDE / coding assistant; set safe mode; configure Review flow |
| LO2 (prototype) | Use Agent Manager to manage workspace / task / implementation plan; use Antigravity Browser for external data extraction; require Agent to produce README / tests / docs |
| LO3 (cloud architecture) | Plan GCP serverless architecture; generate and review IaC / Cloud Run service / Dockerfile / requirements / deployment steps |
| LO4 (L3 bridge) | Organize Skill Library; mark L3 Workflow candidates and L4 Agent candidates; deliver Workflow Blueprint |

### 3.3 Interactive Learning Design (Engagement + Formative + Summative)

> Per [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) §5.1 + §7 + §9.4.

**Engagement activity (within first 15 min of intro):**

> **Open Antigravity → Agent Manager → give Agent a small task (e.g., "research 3 n8n alternatives and compare") → observe Agent decomposing tasks / planning / running the browser end-to-end**. 15 min hands-on; learners see for the first time the difference between Agentic IDE vs traditional IDE.

**Formative gates (quick self-checks at section boundaries):**

| Section | Formative check | Duration |
|---|---|---|
| §6.1 Foundation end | Write Agent operation policy table + governance config screenshots | 10 min |
| §6.2 Builder end | Peer review Flask app: README complete? tests pass? | 15 min |
| §6.3 GCP end | Upload test file → check Cloud Run log → check BigQuery result (self-verify pipeline works) | 10 min |
| §7 L2-to-L3 Bridge end | Non-author tests Blueprint with payload (peer review) | 15 min |

**Summative gate (end of course):**

Maps to **Gate 2** (§9). 10 deliverables → see §10.

### 3.4 Reference materials list

| Type | Location | Use | Status |
|---|---|---|---|
| Antigravity operation policy table | TBD template | Three governance pillars (Terminal / Review / JS) + safe mode | ☐ TBD |
| Flask app skeleton | TBD (with README / pytest / Dockerfile) | Builder direct use | ☐ TBD |
| GCP `setup.sh` template | §6.3 in-class output | Enable APIs + create resources | ☑ In-class |
| Workflow Blueprint template | §7.3 (9 fields defined) | L2-L3 bridge standard format | ☑ Available |
| agency-agents persona library | `90_References/AGENCY_AGENTS_REFERENCE.md` | §7.6 reference | ☑ Available |
| Walkthrough artifact example | TBD | What a passing walkthrough looks like | ☐ TBD |

### 3.5 §7.6 agency-agents scope clarification

§7.6 introduces [agency-agents](https://github.com/msitarzewski/agency-agents) (MIT, 144+ personas) as an **optional extension** for L2-B:

- **Not L2 core**: core is Foundation + Builder + GCP three tracks
- **When to use**: after §6.2 Builder, when learners want to expand Skill Library — pick a persona from agency-agents as starting point, then fork and customize per business
- **When not to use**: client has strict requirements for all Skills to be in-house, OR regulated industry (finance / medical / government) — third-party personas require additional legal review

---

## 4. Prerequisites

| Item | Minimum Requirement |
|---|---|
| Accounts | A Google account capable of signing in to Antigravity; the GCP course requires access to a Google Cloud project |
| Local environment | Antigravity, Chrome, and the necessary development tools installed |
| Engineering foundations | Ability to read basic Python, Flask, Shell, and Docker concepts |
| GCP foundations | The GCP version requires `gcloud CLI` already installed and authenticated |
| Governance consensus | Terminal execution, browser JavaScript, and artifact review must be set to "require review" or "review-oriented" |
| Course materials | Sample business requirements, internal app ideas, and document pipeline ideas that the enterprise may use |

---

## 5. L2 Antigravity IPOE

| Category | Definition |
|---|---|
| Input | User requirements, existing code, SOPs, website data, product specifications, test cases, GCP project, gcloud permissions, data processing requirements |
| Process | Agent planning, task list, implementation plan, code generation, browser verification, unit test generation, artifact review, cloud deployment, manual verification |
| Output | App prototype, Flask / Python code, README, unit tests, Walkthrough artifact, GCP setup script, Cloud Run service, Dockerfile, BigQuery dataset, deployment validation report |
| Evidence | Antigravity task artifact, implementation artifact, walkthrough artifact, Git diff, test results, browser verification video or screenshots, gcloud log, Cloud Run log, BigQuery query results, manual review records |

---

## 6. Full Course Versions

The L2 course must be split into "first half — produce Skills" and "second half — bridge to L3." If L2 stops at a Skill Library, the outcome remains as documents or code; the second half must convert Skills into Workflow Blueprints that n8n can take over.

| Segment | Core Task | Output |
|---|---|---|
| First half | Build Business Skills or Antigravity engineering artifacts | Skill, app prototype, test, README, GCP PoC |
| Second half | Package the Skill into a process specification connectable by L3 n8n | Trigger, I/O schema, node map, human gate, log, test payload |

### 6.0 Lecture Map (per [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) §5.3)

#### 6.0.1 §6.1 Foundation Complete Lecture Map (~45 lectures × avg 4 min = 180 min / 3 hr + 30 min buffer)

> Lecture type codes: **TH** = Talking Head / **S** = Screencast / **SL** = Slides / **VS** = Visual / **PR** = Practice / **EN** = Engagement / **RC** = Recap.

##### Section 0 — Introduction (10 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 0.1 | Welcome to L2 Antigravity | TH | 3 | Instructor intro + why Agentic Developer is IT's competitive edge |
| 0.2 | What you'll learn | TH+SL | 2 | 4 primary LOs preview |
| 0.3 | **Engagement: let Agent do a small research** | EN+S | 5 | Agent Manager → assign small task → watch plan / browser / artifact |

##### Section 1 — L2 Positioning (30 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 1.1 | L1 → L2 transition | SL | 5 | Chat vs Skill difference |
| 1.2 | L2 two tracks: Business Skill vs Agentic Developer | SL+VS | 5 | Track-split diagram |
| 1.3 | Antigravity vs traditional IDE | SL | 5 | 5-dimension comparison table |
| 1.4 | Agentic IDE design philosophy | SL | 5 | Agent autonomy + human review |
| 1.5 | Three codelabs mapped to L2 capabilities | SL | 5 | §2 table recap |
| 1.6 | Section recap | RC | 5 | L2 training track + learning path |

##### Section 2 — Install & Environment (45 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 2.1 | System requirements | SL | 4 | OS / RAM / network |
| 2.2 | Download Antigravity | S | 4 | Official site / platform choice |
| 2.3 | Installation steps | S | 5 | macOS / Windows / Linux |
| 2.4 | First login | S | 4 | Google account / company SSO |
| 2.5 | Chrome / Browser setup | S | 4 | Antigravity Browser intro |
| 2.6 | Workspace concept | S | 5 | One workspace = one project |
| 2.7 | Create first workspace | S | 5 | New workspace settings |
| 2.8 | Environment health-check list | SL | 5 | 9 check items |
| 2.9 | Section recap | RC | 4 | Install acceptance criteria |
| 2.10 | **Formative: env checklist** | PR | 5 | Learners tick all items |

##### Section 3 — Agent Manager / Editor (45 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 3.1 | Agent Manager UI overview | S | 4 | Left task / center editor / right artifact |
| 3.2 | Create a task | S | 4 | Task description → plan |
| 3.3 | Implementation plan | S | 5 | Agent self-decomposes |
| 3.4 | Watch Agent execute | S | 5 | Live view of Agent thinking |
| 3.5 | Walkthrough artifact | S | 5 | Evidence chain + reproducibility |
| 3.6 | Editor mode | S | 4 | Live view of Agent writing code |
| 3.7 | Diff review | S | 4 | Accept / reject / modify |
| 3.8 | Section recap | RC | 4 | Agent Manager workflow |
| 3.9 | **Formative: complete a small task** | PR | 10 | Learners give Agent a task |

##### Section 4 — Safety & Review Policy (45 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 4.1 | Why Agents need governance | TH | 5 | 3 runaway cases |
| 4.2 | Terminal execution policy | S | 5 | Allow / Review / Block |
| 4.3 | Review policy | S | 5 | Which actions require review |
| 4.4 | JavaScript execution policy | S | 4 | Browser JS risks |
| 4.5 | Safe Mode | S | 5 | When to enable |
| 4.6 | Audit Log | S | 5 | Capture all Agent actions |
| 4.7 | Three pillars vs enterprise audit | SL | 4 | ISO / SOC2 mapping |
| 4.8 | Section recap | RC | 4 | Governance checklist |
| 4.9 | **Formative: write your team's policy** | PR | 8 | Learners draft their team's policy |

##### Section 5 — Browser Agent (45 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 5.1 | Browser Agent intro | TH+S | 4 | Difference vs selenium |
| 5.2 | Open page + extract data | S | 5 | Single page / multi-page |
| 5.3 | Interaction: click / fill form | S | 5 | Simulate user |
| 5.4 | Handle login + cookie | S | 5 | Semi vs full auto |
| 5.5 | Structured data extraction | S | 5 | JSON / CSV output |
| 5.6 | Verification + screenshot | S | 4 | Evidence preservation |
| 5.7 | Anti-scraping & ethical limits | SL | 4 | robots.txt / rate limit / ToS |
| 5.8 | Section recap | RC | 4 | Browser Agent use-case list |
| 5.9 | **Formative: scrape a competitor site** | PR | 9 | Learners pick own target |

##### Section 6 — Conclusion (10 min)

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 6.1 | Course recap | TH | 3 | All 4 LOs met? |
| 6.2 | L2-B Builder / GCP preview | SL | 3 | §6.2 / §6.3 next |
| 6.3 | L3 transition: Workflow Blueprint | TH | 2 | Why also learn L3 |
| 6.4 | Congratulations + next steps | TH | 2 | Closing |

#### 6.0.2 §6.2 Builder Lecture Map (stub)

`8 hours = ~120 lectures. Section structure: Intro → Web research → Flask app → Iteration → Unit test/docs → L2-to-L3 bridge → I/O contract → Human gate/log → Review → Conclusion. Expand per §6.0.1 format.`

#### 6.0.3 §6.3 GCP Lecture Map (stub)

`8 hours = ~120 lectures. Section structure: Intro → GCP readiness → Architecture planning → IaC → Cloud Run service → Gemini integration → Pipeline deployment → Validation → Security extension → Conclusion.`

#### 6.0.4 §6.4 Enterprise Lab Lecture Map (stub)

`2 days = ~240 lectures. Recommended: split into 4 half-day mini-courses; expand each per §6.0.1.`

---

### 6.1 L2 Antigravity Foundation: 3 Hours

Goal: Establish Antigravity operations, governance, and Agentic IDE concepts.

| Time | Topic | Content | Output |
|---|---|---|---|
| 30 min | L2 positioning | Business Skill AI vs. Agentic Developer AI | L2 training-track diagram |
| 45 min | Installation and environment | Antigravity, Chrome, sign-in, workspace | Environment checklist |
| 45 min | Agent Manager / Editor | Workspace, task, plan, artifact, editor | Operation screenshots |
| 45 min | Security and review policy | Terminal, Review, JavaScript, Safe Mode | Permission configuration table |
| 45 min | Browser Agent | Open page, extract data, interact, verify | Browser test log |

### 6.2 L2 Antigravity Builder: 1 Day

Goal: In the morning, enable students to use the Agent to build runnable apps, documentation, and tests; in the afternoon, convert the outputs into an L3 Workflow Blueprint.

| Time | Topic | Content | Output |
|---|---|---|---|
| 60 min | Web research task | Have the Agent extract website data and summarize | Research artifact |
| 90 min | Flask app generation | Generate a tech-event website or an internal departmental tool | Flask app |
| 60 min | Iteration | Add features, modify requirements, observe how the Agent updates its plan | Change record |
| 60 min | Unit test / docs | Generate tests, README, constraints, and operations documentation | Test suite, README |
| 90 min | L2-to-L3 bridge | Define the app / Skill as a component callable from n8n | Workflow Blueprint |
| 60 min | Input / Output contract | Define trigger, payload, output JSON, error format | I/O schema |
| 60 min | Human gate / log | Define manual review, notifications, execution log, fallback | Gate / Log spec |
| 60 min | Review | A non-author tests the Blueprint with a payload | Peer review |

### 6.3 L2 Antigravity GCP: 1 Day

Goal: Enable engineering / IT teams to use Antigravity to plan and deploy a GCP serverless PoC.

| Time | Topic | Content | Output |
|---|---|---|---|
| 60 min | GCP readiness | Project, billing, gcloud, permissions, region | GCP checklist |
| 75 min | Architecture planning | GCS, Pub/Sub, Cloud Run, Gemini, BigQuery | Architecture plan |
| 90 min | IaC / setup script | Generate `setup.sh`, enable APIs, create resources | Setup script |
| 90 min | Cloud Run service | Python / Flask service, Dockerfile, requirements | Cloud Run app |
| 60 min | Gemini integration | Document analysis, metadata extraction, classification or translation | AI processing spec |
| 60 min | Pipeline deployment | Deploy Cloud Run, configure trigger, BigQuery streaming | Deployment log |
| 60 min | Validation | Upload a test file, inspect Cloud Run logs, query BigQuery | Validation report |
| 45 min | Security extension | DLQ, Secret Manager, Eventarc, cost control | Follow-up improvement list |

### 6.4 L2 Antigravity Enterprise Lab: 2 Days

Goal: Use a client-supplied topic to produce a deliverable engineering Skill and PoC.

| Time | Topic | Content | Output |
|---|---|---|---|
| Day 1 AM | Use case selection | Choose 1 internal app or document pipeline | Use case brief |
| Day 1 PM | Build | Agent planning, coding, testing, docs | App / pipeline prototype |
| Day 2 AM | L2-to-L3 bridge | Trigger, I/O schema, n8n node map, human gate, log | Workflow Blueprint |
| Day 2 PM | Package | Skill conversion, Runbook, Gate 2 acceptance, L3/L4 candidates | L2 delivery package |

---

## 7. L2 Second Half: Bridging to the L3 Workflow Blueprint

### 7.1 Second-Half Objective

The objective of the second half of L2 is not to keep polishing Skills but to convert them into a process specification that L3 can begin work on directly:

> Any Skill that has passed L2 must be able to answer: What event triggers it? What data does it consume? What JSON does it output? Which step requires human review? Where are logs stored? How are failures handled? How does it plug into n8n?

### 7.2 L2-to-L3 Bridge Process

| Step | Question | Output |
|---|---|---|
| 1. Select Skill | Which Skill is best suited for workflow automation? | Workflow candidate card |
| 2. Define Trigger | Triggered by Email, form, Webhook, schedule, file upload, or CRM event? | Trigger spec |
| 3. Define Input | Which fields, files, and system data does the Skill require? | Input schema, sample payload |
| 4. Define Process | Which nodes must n8n run? Which steps invoke AI / Skill / API? | n8n node map |
| 5. Define Output | Where are results written — Email, Sheets, Notion, CRM, ERP, DB? | Output schema |
| 6. Define Human Gate | Which scenarios require human review? Who reviews? Within how much time? | Human gate spec |
| 7. Define Evidence | How do we prove the process ran, the AI cited sources, and data was written? | Log / evidence spec |
| 8. Define Error Handling | How are failures notified, retried, handled with fallback, or escalated to humans? | Error handling spec |
| 9. Define Gate 2 | Is this sufficient to enter L3 implementation? | Gate 2 acceptance sheet |

### 7.3 Workflow Blueprint Standard Format

| Field | Description |
|---|---|
| Workflow name | The name of the process to be implemented in L3 |
| Business Owner | Business owner of the process |
| IT Owner | Owner of systems / APIs / permissions |
| Trigger | Email, Webhook, form, schedule, file, CRM / ERP event |
| Input Schema | Fields, data types, required flag, examples |
| Skill / Agent Step | Which L2 Skill or Antigravity artifact to invoke |
| System Nodes | Gmail, Sheets, Notion, CRM, API, ERP, DB |
| Human Gate | Review conditions, reviewer, review inputs and outputs |
| Output Schema | Output format, write-back location, notification method |
| Log / Evidence | n8n execution log, AI inputs and outputs, system write records |
| Error Handling | Retry, notification, fallback, human takeover |
| Test Payload | At least 2 normal cases and 1 error case |
| Gate 2 Result | Pass / Fail / Remediation |

### 7.4 Second-Half Practice Tasks

| Type | L2 Skill | L3 Workflow Blueprint |
|---|---|---|
| Customer service | Complaint classification and reply-draft Skill | Gmail trigger → AI classification → CRM lookup → human review → reply draft |
| Sales | Visit summary Skill | Meeting minutes upload → summary → CRM update → next-step tasks |
| Operations | ERP abnormal-order analysis Skill | Scheduled ERP query → AI analysis → Sheets report → manager notification |
| Hospital | FAQ reply-draft Skill | Form / email trigger → FAQ lookup → risk flagging → human review |
| Engineering | Antigravity deployment validation Skill | Git / Webhook trigger → tests → deployment verification → log / report |
| Documents | GCP document pipeline Skill | GCS upload → Pub/Sub → Cloud Run → Gemini → BigQuery |

### 7.5 Second-Half Deliverables

- L3 Workflow candidate card.
- Trigger spec.
- Input / Output schema.
- Sample payloads: 2 normal, 1 error.
- n8n node map.
- Human gate spec.
- Credential / API / system requirements list.
- Log / Evidence spec.
- Error handling spec.
- Gate 2 acceptance sheet.

### 7.6 L2-B Second-Half Extension: Leveraging a Ready-Made Agent Library (agency-agents)

> Citation: [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) (MIT License). Full citation and license notice: see [`../90_References/AGENCY_AGENTS_REFERENCE.md`](../90_References/AGENCY_AGENTS_REFERENCE.md).

In the second half of the L2-B Agentic Developer track, beyond converting Skills into Workflow Blueprints, students should also learn a key idea: **not every Skill needs to be built from scratch.** Mature agent-persona libraries already exist (e.g., agency-agents, with 144+ agent definitions across 12 divisions) and can serve as a starting point for building Skills.

#### 7.6.1 Teaching Objectives

After this segment, students should be able to:

1. Explain the trade-off between "building a Skill from scratch" and "adopting + customizing a ready-made agent persona."
2. Install agency-agents into Antigravity / Claude Code (`./scripts/install.sh`, with tool auto-detection).
3. Browse the 12 divisions (engineering / design / marketing / sales / product / testing, etc.) and select agents that match the enterprise scenario.
4. **Customize** a selected agent persona into an enterprise-specific Skill: rewrite the mission, add enterprise SOPs, set the Review Policy, and fill in the IPOE.
5. Judge which agents can be used directly, which need substantial rewriting, and which do not apply (avoiding "pasting a persona and calling it organizational capability").
6. Incorporate the customized agent persona into the L2 Skill Library, noting the source (agency-agents + version) and the Owner.

#### 7.6.2 Classroom Content (90 min)

| Time | Topic | Content | Output |
|---|---|---|---|
| 20 min | Ready-made agent library concept | Build vs. adopt; agency-agents' 12-division structure and license (MIT) | Trade-off decision table |
| 20 min | Install and browse | Install script, tool detection, select agents by enterprise scenario | Candidate agent list |
| 30 min | Customization practice | Rewrite mission / add SOP / set Review Policy / fill in IPOE | Customized agent persona |
| 20 min | Incorporate into the Skill Library | Note source, version, Owner; align with §8 Skill Library | Skill Library entry |

#### 7.6.3 Governance and Red Lines

- agency-agents is **third-party MIT content**; customized enterprise Skills belong to the enterprise, but it is recommended to note the original source in the Skill documentation.
- Instructions within an agent persona must still pass the enterprise's Terminal / Review / JavaScript security policies (see §6.1).
- Do not let an agent persona run in production without review; always pass Gate 2 after customization.
- The persona library is only a "starting point" — it cannot replace the §7 L2-to-L3 Bridge. Real workflow automation must still go through the Workflow Blueprint.

#### 7.6.4 Second-Half Deliverables (additional)

- agency-agents installation record (tool-detection screenshot).
- Enterprise scenario × candidate agent mapping table.
- At least 2 customized agent personas (with source attribution, IPOE, Owner).
- Build vs. adopt trade-off decision table.

---

## 8. L2 Skill Library Design

These three codelabs should not be treated as one-off exercises but should crystallize into reusable Skills.

| Skill | Use Scenario | Input | Output |
|---|---|---|---|
| Antigravity Workspace Setup Skill | Before a new project begins | Project name, repo, permission mode | Workspace configuration and governance sheet |
| Agent Planning Skill | Convert requirements into tasks | User requirements, constraints, tech stack | Task list, implementation plan |
| Web Research Skill | Extract website data | URL, question, fields | Research summary, source records |
| App Prototype Skill | Generate a small app | Functional needs, UI needs, data model | App prototype, README |
| Unit Test Skill | Backfill tests | Code, business rules | Test suite, coverage notes |
| GCP Serverless Pipeline Skill | Document processing pipeline | GCP project, file source, metadata fields | GCS / Pub/Sub / Cloud Run / BigQuery PoC |
| Deployment Validation Skill | Validate deployment | Test files, deployment URL, log | Validation report |
| Workflow Blueprint Skill | Convert L2 outputs into L3 specifications | Skill, trigger, systems, data fields | n8n Workflow Blueprint |

---

## 9. Stage Gate 2 Controls

| Gate | Check Question | Required Evidence | Verdict |
|---|---|---|---|
| Gate 2A: Tooling operational | Are Antigravity, Chrome, workspace, and sign-in ready? | Environment checklist, screenshots | Pass / Fail |
| Gate 2B: Governance operational | Do Terminal, Review, and JavaScript policies meet company risk requirements? | Permission configuration sheet | Pass / Fail |
| Gate 2C: Development loop operational | Can the Agent generate the app, modify it, test, and document it? | App, README, test result, walkthrough | Pass / Fail |
| Gate 2D: L3 Blueprint operational | Are trigger, I/O schema, node map, human gate, log, and test payloads present? | Workflow Blueprint, sample payload, system requirements list | Pass / Fail |
| Gate 2E: Cloud PoC operational | Can the GCP pipeline be deployed and validated? | gcloud log, Cloud Run log, BigQuery result | Pass / Fail |
| Gate 2F: Skill-ification operational | Has the process been distilled into a Skill Library? | Skill document, owner, version, test logs | Pass / Fail |

If Gates 2A-2C do not pass, do not proceed to L3 Workflow. If Gate 2D does not pass, the L2 second half has not completed the bridge and L3 implementation should not begin. If Gate 2E does not pass, you may enter regular L3 but not cloud-deployment-based PoCs. If Gate 2F does not pass, the course outputs have not yet become organizational capability.

---

## 10. Deliverables

| Deliverable | Description | Acceptance Method |
|---|---|---|
| Antigravity operational settings table | Installation, workspace, Agent Manager, Editor, Browser | Classroom check |
| Agent permission and review settings table | Terminal, Review, JavaScript, Safe Mode | IT / instructor review |
| App Prototype | Flask / productivity app / internal tool | Runnable demo |
| Unit Test Evidence | Test files, test results, fix records | Test output |
| README / Docs | Usage instructions, constraints, operations | Readable by a non-author |
| GCP Pipeline PoC | GCS, Pub/Sub, Cloud Run, Gemini, BigQuery | After file upload, BigQuery contains results |
| Validation Report | Automated and manual validation records | Logs, screenshots, SQL queries |
| L2 Skill Library | 3-5 engineering Skills | Owner, version, test logs |
| L3 Workflow Blueprint | Trigger, I/O schema, node map, human gate, log, test payload | L3 instructor / IT can begin work directly |
| L3 / L4 candidate list | Capabilities ready to plug into n8n or Hermes Agent | Roadmap review |

---

## 11. Bridge to L3 / L4

After L2 Antigravity training, the natural next steps are:

- L3 n8n: Plug the apps, APIs, GCP pipelines, and test flows produced by Antigravity into Workflows.
- L4 Hermes Agent: Let Hermes Agent invoke L2 Skills, read engineering documents, track deployment evidence, and generate briefings.

The point of L2 is not to ship a production project directly, but to turn engineering capability and development processes into reusable, reviewable, and verifiable Skills. Cross-system processes are then taken over by L3, while continuous operations and task delegation are taken over by L4.
