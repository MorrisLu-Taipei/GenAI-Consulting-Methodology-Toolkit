# Eight-Stage Consulting Toolkit Templates

> 🌐 中文版本 / Chinese version: [CONSULTING_TOOLKIT_TEMPLATES.md](CONSULTING_TOOLKIT_TEMPLATES.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

This document provides **ready-to-use toolkit templates** for the eight-stage consulting methodology: interview question banks, inventories, matrices, worksheets, and checklists. Each stage maps to 1-4 tools. Consultants can copy them directly into Notion / Google Docs / Word and start using them.

---

## Stage 1: Current-State Discovery

### Tool 1.1 Interview Question Bank (40 questions)

#### A. Executive level (CEO / COO / CIO) — 12 questions

1. What is your ideal future state of AI in the company?
2. What AI successes and failures have you seen in the past 12 months?
3. What is the company's biggest operational pain point right now? Can AI help?
4. What AI risks worry you most? (security, compliance, employee resistance, unclear ROI)
5. How much budget are you willing to invest in AI transformation annually?
6. Is there an owner driving AI in the company? (If not, who could take it on?)
7. Which L1-L5 level do you think we are at? Why?
8. Which level do you want to reach in 12 months?
9. Which department, if it adopts AI first, would have the greatest impact on the company?
10. Do you plan to build an internal AI team or rely on external consultants?
11. What is the board's / parent company's attitude toward AI investment?
12. What concrete outcome do you most want from this consulting project?

#### B. Department-manager level — 14 questions

13. What are your department's key KPIs and pain points?
14. How much time do employees spend on repetitive work each day?
15. Which tasks are "the same regardless of who does them" and could be AI-enabled?
16. Which tasks rely heavily on specific senior employees?
17. Which SaaS tools does your department use? How well are they integrated?
18. Do employees privately use ChatGPT / Claude? How often? What data boundaries?
19. What are your department's "golden SOPs"? Are they documented?
20. What is the biggest barrier to cross-functional collaboration?
21. Which block of your time do you want AI to free up?
22. What is your team's attitude toward AI? (enthusiastic / neutral / resistant)
23. How long does new-hire onboarding take? Can AI accelerate it?
24. Where is decision-making slow — data is hard to find, or communication is slow?
25. What AI attempts in the past 90 days are worth recording?
26. Does your department have a wishlist of "things I wanted to automate but never had time for"?

#### C. Operator / front-line employee — 14 questions

27. What are the 5 most repetitive tasks you do each day?
28. Which systems / tools do you open each day?
29. Which data do you spend a long time searching for and can't find?
30. Do you privately use AI tools? Which one? For what?
31. Where do you find AI helps, and where it doesn't?
32. When writing reports / emails / proposals, how much can AI speed it up?
33. Are you afraid AI will replace your job? (If so, which part?)
34. What would you like your manager to stop asking you to do?
35. What caused the last mistake? Could AI prevent it?
36. What is your "core expertise" that AI should not be able to replace?
37. Where do your colleagues use AI better than you?
38. How much time are you willing to spend learning AI?
39. Which tasks are "actually faster for a human than for AI"?
40. Give AI one wish — what would you want it to solve for you?

> **How to use:** each interview is 60-90 minutes; 12 questions for executives, 14 for department managers, 6-8 (selected) for operators. Record + summarize + code.

### Tool 1.2 AI Usage Inventory

| # | Dept | Current AI tool | Frequency | Users | Approved? | Sensitive-data risk | Monthly spend | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Marketing | ChatGPT Plus (personal account) | Daily | 8 | ❌ | High (brand data) | NT$24,000 | personal credit card |
| 2 | Sales | Copilot for Office | Weekly | 15 | ✓ | Medium | NT$45,000 | company-purchased |
| 3 | IT | Claude.ai (personal) | Daily | 3 | ❌ | Medium (code) | NT$9,000 | personal account |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

> **Output:** a shadow-IT risk map + procurement consolidation opportunities.

### Tool 1.3 Systems Inventory

| System name | Vendor / version | Dept owner | Users | Integration points (in/out) | Data sensitivity | API available? | Cloud/on-prem | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gmail Workspace | Google | IT | whole company 250 | OAuth API | Medium | ✓ | cloud | SSO enabled |
| Salesforce | SF Sales Cloud Pro | Sales | 35 | REST + Webhook | High (PII) | ✓ | cloud | expires in 12 months |
| SAP B1 | 9.3 | Finance | 18 | DI API + ODBC | High | ✓ | on-prem | legacy customizations |
| Notion | Plus | All | 80 | API + Webhook | Medium | ✓ | cloud | self-managed by departments |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

> **Output:** a systems map + a list of L3 Workflow PoC candidates.

### Tool 1.4 As-Is Process Map (Swimlane Template)

```
Process: Quote-to-Ship
========================================
Actor          | Step               | System        | Input         | Output        | Pain
---------------|--------------------|---------------|---------------|---------------|-------
Customer       | sends quote email  | Email         | requirements   | quote email   | -
Sales          | reads & triages    | Gmail         | quote email    | internal route| 30% missed
Sales          | checks ERP stock   | SAP B1        | part number    | stock & price | slow + errors
Sales          | writes quote       | Word + Sheet  | stock & price  | quote draft   | repetitive
Sales lead     | reviews quote      | Email         | quote          | sign / reject | waiting
Sales          | sends quote        | Gmail + PDF   | signed version | quote email   | -
Customer       | confirms order     | Email         | quote          | PO            | -
Sales          | creates SO         | SAP B1        | PO             | SO number     | re-keying
WMS operator   | picks stock        | WMS           | SO             | picking list  | wrong picks
Shipping       | prints waybill     | logistics sys | picking list   | waybill       | -
========================================
Total time: average 4-7 working days
Pain summary: missed mail, re-keying, slow price lookups, waiting on sign-off
AI candidates: L3 Gmail triage, L3 SAP quote auto-draft, L4 Agent sign-off summary
```

> **Output:** one swimlane per process; annotate pain density (0-3 dots per step); hand to Stage 4 for Impact × Effort.

---

## Stage 2: Vision Alignment

### Tool 2.1 L1-L5 Capability Explanation Handout (for clients)

| Level | What it looks like in practice | What clients often say | Common confusion to address |
| --- | --- | --- | --- |
| L1 Chat AI | Everyone has a company account, knows how to use it, has a policy | "We bought ChatGPT" | Buying ChatGPT ≠ everyone using it, ≠ governance |
| L2 Skill AI | Skill Library + version control | "I have a prompt library" | A prompt library ≠ reusable by others |
| L3 Workflow AI | n8n PoCs running + connected to systems | "We have automation" | RPA / Zapier ≠ AI Workflow |
| L4 Auto Agentic AI | An Agent passes the Gate + has a Wiki | "We use Agents" | A demo Agent ≠ a controlled Agent |
| L5 Agentic Team AI | Multiple Agents complete a cross-functional task | "We're doing an AI team" | A group of chatbots ≠ an Agent Team |

### Tool 2.2 Vision Worksheet (5 prompts)

1. In one sentence, how do you want customers to describe your company's AI use three years from now? ______
2. What concrete NT$ amount will AI save / create for you in three years? ______
3. Three years out, which department do you want most AI-enabled? Which to keep manual? ______
4. Three years out, what three things do you want AI governance to do "at minimum"? ______
5. If it fails in three years, what outcome do you least want to see? ______

### Tool 2.3 Stakeholder Alignment Matrix (RACI)

| Topic | Executive Sponsor | AI Champion | IT | Front-line users | Data Owner |
| --- | --- | --- | --- | --- | --- |
| Vision setting | A | R | C | I | I |
| Tool selection | A | C | R | C | C |
| Accounts / permissions | I | C | R | I | A |
| Skill / Workflow building | I | A | R | R | C |
| Audit / governance | A | C | R | I | R |
| ROI measurement | A | R | C | I | I |

(R=Responsible, A=Accountable, C=Consulted, I=Informed)

---

## Stage 3: Industry Benchmark

### Tool 3.1 Benchmark Case Summary Template

| Field | Description |
| --- | --- |
| Industry | industry |
| Company size | headcount / revenue |
| Their L-level start | L-level at the start |
| Their L-level today | current L-level |
| Time taken | months |
| Key wins | three key outcomes |
| Key failures | two failure lessons |
| Sources | public news / interviews / cases |

### Tool 3.2 Five Ready-Made Benchmark Stubs

#### Manufacturing — semiconductor packaging & test, 700 people
- L1 → L3 in 9 months
- Wins: process-anomaly summary Agent, SPC auto-analysis, complaint root-cause Agent Team
- Failures: early on, skipped L1 org-wide and relied on one IT person; data permissions not laid down

#### Hospital — medical center, 1,200 people
- L1 → L4 in 12 months
- Wins: patient onboarding RAG, HIS / EMR integration Agent, admin summaries
- Failures: first phase ignored nursing front-line resistance; an L1 course was added later

#### Retail — chain brand, 800 people
- L1 → L4 in 14 months
- Wins: product-copy Skill Library, social-listening Workflow, new-product-launch Agent Team
- Failures: no Reviewer designed early, AI copy misused brand terms

#### Financial Services — regional bank, 2,500 people
- L1 → L3 in 18 months
- Wins: KYC document summary Workflow, customer-service triage Agent
- Failures: compliance review was time-consuming; on-prem LLM performance insufficient

#### Government — city government, 5,000 people
- L1 → L2 in 24 months
- Wins: document summary, citizen-service FAQ
- Failures: procurement dragged; no AI Champion

---

## Stage 4: Gap Analysis

### Tool 4.1 Missing / Broken / Redundant Table

| Area | Type (M/B/R) | Description | Root Cause | Severity 1-5 | Owner |
| --- | --- | --- | --- | --- | --- |
| Customer-service email triage | Missing | No AI classification at all | No one thought of it | 4 | CS lead |
| Quote system | Broken | Sales manually copy-paste | Legacy system, no API | 5 | IT deputy manager |
| Ticket system | Redundant | Notion + Trello + Email, three systems | Each dept chose its own | 3 | COO |
| ... | ... | ... | ... | ... | ... |

### Tool 4.2 Impact × Effort Matrix

```
            Low Effort                   High Effort
           ┌──────────────────────┬──────────────────────┐
High       │  ★ Quick Wins        │  Big Bets            │
Impact     │  - Gmail triage      │  - ERP Agent          │
           │  - Sheet auto-score  │  - Cross-functional   │
           │                      │    Team               │
           ├──────────────────────┼──────────────────────┤
Low        │  Fill-ins            │  ✗ Avoid              │
Impact     │  - internal FAQ      │  - large custom       │
           │  - slide templates   │    chatbot            │
           └──────────────────────┴──────────────────────┘
```

**Placement rules:**
- Impact score: direct NT$ impact × number of beneficiaries × strategic importance, scored 1-5
- Effort score: person-days × risk × system-integration difficulty, scored 1-5
- ≥3 is High

### Tool 4.3 Prioritization Worksheet

| Candidate | Impact (1-5) | Effort (1-5) | Strategic Fit (1-5) | Score = (I × SF) / E | Rank |
| --- | ---: | ---: | ---: | ---: | ---: |
| CS email triage PoC | 4 | 1 | 5 | 20 | 1 |
| Sales proposal Skill | 4 | 2 | 4 | 8 | 4 |
| ERP Agent | 5 | 5 | 5 | 5 | 5 |
| Sheet auto-scoring | 3 | 1 | 3 | 9 | 3 |
| Cross-functional Team | 5 | 4 | 5 | 6.25 | (Big bet, later phase) |

---

## Stage 5: Executive Problem Statement

### Tool 5.1 Problem Statement Worksheet (5 sections)

```
1. CONTEXT
   What happened in the past 12 months that made AI a priority?

2. TENSION
   What is the gap between the current "reality" and the "expectation"? Quantify it.

3. COST OF INACTION
   What happens 12 months from now if we don't do AI? Amount?

4. DESIRED FUTURE
   What does success look like in 12 months? Three quantifiable indicators.

5. CONSTRAINTS
   Budget? Headcount? Compliance? Timeline? Which options are already ruled out?
```

### Tool 5.2 Common Pitfalls Checklist (10 anti-patterns)

- [ ] Framing AI as a technology issue (should be framed as a business issue)
- [ ] Not quantifying the "cost of inaction"
- [ ] Treating "adopting AI" as the goal (it should be a business KPI)
- [ ] Listing all departments as high priority (no focus)
- [ ] Only discussing opportunities, avoiding risks
- [ ] Using "security" as a shield to block any attempt
- [ ] Framing governance as an IT issue (it's a company-wide issue)
- [ ] Expecting a timeline that is too short / too long
- [ ] No sponsor / no champion
- [ ] No failure exit mechanism

### Tool 5.3 Sample Completed Problem Statement (manufacturing)

```
CONTEXT:
In the past 12 months, three direct competitors adopted AI quality inspection
and complaint Agents; the company's customers began questioning why our delivery
and complaint responses are slow. Client A's quarterly orders dropped 18%.

TENSION:
The company's current defect rate is 3.2% (industry leader 1.8%), complaints take
an average of 5 days to respond (industry 2 days), and sales proposals take 4 days
to produce (industry 1.5 days).

COST OF INACTION:
Without significant improvement within 12 months, we expect to lose Clients A, B,
and C, with an annual revenue impact of about NT$ 180M. Recruiting 8 additional QA
and sales staff would cost about NT$ 12M.

DESIRED FUTURE:
In 12 months: defect rate down to 2.0%, complaint response ≤ 1 day, proposal
production ≤ 1 day. Establish 1 process-improvement Agent Team and 1 sales Skill
Library.

CONSTRAINTS:
- Budget ceiling NT$ 8M (incl. training + platform + consulting)
- Process data must be handled on-prem (cannot go to the cloud)
- IT headcount of 2 FTE cannot be increased
- Parent-company audit in December — the first Quick Win must show within 6 months
```

---

## Stage 6: Roadmap & Stage-Gate Design

### Tool 6.1 30/60/90 Roadmap Template

| Quarter | Theme | Deliverables | Owner | Stage Gate Criteria | KPI |
| --- | --- | --- | --- | --- | --- |
| 30 days | Diagnose + L1 kickoff | OpenWebUI org-wide, AI policy, Prompt Library | IT + AI Champion | Gate 1 | 80% of employees use it weekly |
| 60 days | L2 + L3 PoC | 5 Skills, 3 n8n Workflow PoCs | AI Champion + departments | Gate 2 + 3 | Skill Library ≥3, Workflow uptime 95% |
| 90 days | L4 Pilot | 1 Hermes Agent (e.g., CS / sales) | AI Champion + IT | Gate 4 | Agent completes 5 tasks, Reviewer passes |
| 6 months | L4 Scale | 3 Agents, cross-functional integration | Dept Lead | Gate 4 ext. | monthly time saved ≥ 200 hr |
| 9-12 months | L5 Pilot | 1 ClawTeam (cross-functional task) | Sponsor + AI Champion | Gate 5 | Team completes ≥ 1 cross-functional task |

### Tool 6.2 Stage Gate Acceptance Checklist (Gates 1-5)

#### Gate 1 (L1 complete)
- [ ] OpenWebUI org-wide accounts created
- [ ] AI usage policy signing rate > 90%
- [ ] Prompt Library has ≥ 30 entries
- [ ] Admin Panel permissions matrix configured
- [ ] L2 candidate Skill list ≥ 5

#### Gate 2 (L2 complete)
- [ ] Skill Library has ≥ 3 Skills
- [ ] Each Skill has an Owner, version, IPOE document
- [ ] Antigravity / Claude Code artifacts submitted
- [ ] At least 3 Workflow Blueprints
- [ ] L3 candidate Workflow list

#### Gate 3 (L3 complete)
- [ ] n8n Workflow PoCs ≥ 3 live
- [ ] Sub-workflow Library structure complete
- [ ] Data Tables Schema finalized
- [ ] GitHub Backup SOP executed
- [ ] L4 Workflow Contract — spec for connecting to Hermes

#### Gate 4 (L4 complete)
- [ ] Hermes Agent passes sub-Gates 4A-4E
- [ ] Wiki ingest/query/update all work
- [ ] briefing template and a real brief example
- [ ] Evidence traceability: input → process → output → log
- [ ] L5 Agent Team candidate task list

#### Gate 5 (L5 complete)
- [ ] ClawTeam Role Cards complete
- [ ] Task allocation table with dependency chains
- [ ] 1 successful cross-functional Agent Team simulation
- [ ] Reviewer + Human Gate design
- [ ] ROI tracking matrix launched

### Tool 6.3 Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner | Trigger |
| --- | --- | --- | --- | --- | --- |
| Employee resistance | High | High | L1 org-wide taster + managers lead by example | HR + Sponsor | adoption < 50% in 30d |
| Sensitive-data leakage | Medium | Critical | redact policy + audit log + Hybrid deployment | CIO | DLP alert |
| LLM hallucination causing wrong decisions | High | Medium | Reviewer / Human Gate + evidence | AI Champion | any decision overturned |
| Budget overrun | Medium | Medium | monthly KPI / ROI review | CFO | monthly spend > 110% of budget |
| ... | ... | ... | ... | ... | ... |

---

## Stage 7: Solution Architecture

### Tool 7.1 Skill Map Template

| Skill | Owner | Inputs | Outputs | Tools used | L-level | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Customer proposal draft | Sales Lead | customer data + past proposals | Word proposal | Antigravity + Claude | L2 | Live |
| Complaint classification | CS Lead | Gmail emails | classification + priority | n8n + Claude | L3 | PoC |
| Month-end exception summary | Finance | SAP reports | exception table + actions | n8n + GPT-4 | L3 | Build |
| ... | ... | ... | ... | ... | ... | ... |

### Tool 7.2 Workflow Map Template

| Workflow | Trigger | Steps (n8n) | Systems | Skills called | Output | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| CS email classification | Webhook (Gmail) | Webhook → Set → OpenAI Chat → Switch → Gmail Label | Gmail | "complaint classification" | label + notification | CS Lead |
| Customer monthly report | Schedule (1st of month) | Schedule → SAP API → Sheet → Claude → Email | SAP, Sheets, Gmail | "month-end summary" | PDF + Email | Finance |
| ... | ... | ... | ... | ... | ... | ... |

### Tool 7.3 Agent Map Template

| Agent | Role | Skills used | Workflows used | Wiki | Reviewer | Gate |
| --- | --- | --- | --- | --- | --- | --- |
| CS Triage Agent | complaint triage and drafting | complaint classification, draft generation | CS email classification | FAQ + past cases | CS Manager | Gate 4 ✓ |
| Sales Briefing Agent | pre-visit brief | customer research, opportunity summary | CRM summary | customer history | Sales Lead | Gate 4 ✓ |
| ... | ... | ... | ... | ... | ... | ... |

### Tool 7.4 Integration Architecture (3 variants)

#### Variant A: Cloud-first
```
[OpenWebUI Cloud] → [n8n Cloud] → [Hermes Cloud Agent] → [SaaS APIs]
                                       ↓
                                 [Notion / Sheets / Gmail]
LLM: OpenAI / Claude / Gemini API
Suitable for: low sensitivity, fast PoC, limited budget
```

#### Variant B: Hybrid
```
[OpenWebUI On-Prem] → [n8n Self-host] → [Hermes Local Agent]
                            ↓                  ↓
                      [SaaS APIs]      [local SQL / ERP]
LLM routing: low sensitivity → cloud, sensitive → on-prem Llama
Suitable for: finance, healthcare, manufacturing sensitive data
```

#### Variant C: Full On-Prem
```
[OpenWebUI Local] → [n8n Local] → [Hermes Agent Local]
                       ↓                ↓
                 [Local APIs only]  [Local Llama 70B + Embedding]
No cloud LLM calls
Suitable for: government, defense, top-tier finance
```

---

## Stage 8: Governance & ROI

### Tool 8.1 Permission / Governance Matrix

| Role | Resource | Read | Write | Approve | Audit |
| --- | --- | --- | --- | --- | --- |
| Everyone | OpenWebUI personal area | ✓ | ✓ | ✗ | self |
| Dept Lead | dept Skill Library | ✓ | ✓ | ✓ | dept |
| AI Champion | company-wide Workflows | ✓ | ✓ | ✓ (≤ Gate 3) | all |
| IT Admin | everything + models + Audit Log | ✓ | ✓ | ✓ (Gate 4-5) | all |
| Sponsor / CIO | company-wide read + Approve | ✓ | ✗ | ✓ (Gate 5) | all |
| Compliance / Internal Audit | Audit Log only | ✓ | ✗ | ✗ | all |

### Tool 8.2 ROI Tracking Matrix

| Initiative | Baseline | Target | Actual | Period | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| CS email classification | 5 days resp | 1 day | 1.2 day | Month 3 | CS Lead | 🟡 95% |
| Sales proposals | 4 days | 1 day | 0.8 day | Month 4 | Sales Lead | 🟢 |
| Month-end exception summary | 3 days | 0.5 day | 0.6 day | Month 5 | Finance | 🟢 |
| Hermes Agent tasks | n/a | 50 / month | 38 | Month 6 | AI Champion | 🟡 |
| ClawTeam cross-functional | n/a | 1 / quarter | 0 | Month 9 | Sponsor | 🔴 (delay) |

### Tool 8.3 Audit Log Requirements

| Event Type | Captured by | Retention | Reviewer |
| --- | --- | --- | --- |
| LLM call (prompt + response) | n8n / OpenWebUI | 90 days hot, 1 year cold | AI Champion |
| Permission change | OpenWebUI Admin | 3 years | IT Admin + Compliance |
| Skill / Workflow deploy | GitHub | permanent | AI Champion |
| Agent task start/end | Hermes log | 1 year | AI Champion |
| Reviewer sign-off | in-system | permanent | Compliance |
| Gate pass record | consultant + client | permanent | Sponsor + consultant |
| Sensitive-data redaction triggered | DLP | 1 year | Security + Compliance |

### Tool 8.4 AI Ethics & Data Policy Checklist (15 items)

- [ ] Employee AI usage policy documented and signed
- [ ] Customer data / PII not sent to the LLM (or redacted first)
- [ ] The model vendor's data-retention policy has been reviewed
- [ ] Audit Log covers all LLM calls
- [ ] Employees have the right to know which work is processed by AI
- [ ] AI decisions have a Human Gate (for major matters)
- [ ] AI-produced content is marked "AI-generated"
- [ ] IP ownership clarified (employee / company / AI vendor)
- [ ] Bias / discrimination risk assessment (HR / customer-decision scenarios)
- [ ] High-sensitivity scenarios (minors / medical / legal) have separate rules
- [ ] LLM hallucination handling SOP (who is responsible for checking)
- [ ] AI system incident response process
- [ ] Third-party AI tool whitelist / blacklist
- [ ] Employee education at least once per year
- [ ] Government regulation tracking (EU AI Act, Taiwan AI Basic Act, personal data law) by Compliance

---

## Closing: How to Use This Toolkit

### 6-Week Standard Engagement Schedule

| Week | Stage | Main tools | Client role | Consultant deliverable |
| --- | --- | --- | --- | --- |
| W1 | Stage 1 | 1.1 interviews / 1.2 1.3 inventories | executive interviews, IT provides inventories | Discovery Report |
| W2 | Stage 1+2 | 1.4 As-Is Map / 2.1 2.2 2.3 | department walkthroughs | Vision Workshop Output |
| W3 | Stage 3+4 | 3.1 3.2 benchmarks / 4.1 4.2 4.3 | executive review | Gap Analysis + Priority |
| W4 | Stage 5+6 | 5.1 5.2 5.3 / 6.1 6.2 6.3 | executive + AI Champion | Problem Statement + Roadmap |
| W5 | Stage 7 | 7.1-7.4 | AI Champion + IT | Solution Architecture |
| W6 | Stage 8 + close-out | 8.1-8.4 | Sponsor + Compliance | Final Report + Roadmap + Governance |

### Weekly delivery rhythm

- Monday: review last week's tools + plan this week
- Wednesday: client interviews / workshops
- Friday: deliver draft + client review

### Consultant onboarding (for new consultants)

1. First read the README + AI_TRANSFORMATION_STORY_AND_STRUCTURE
2. Run through all the samples in this toolkit once
3. Shadow 1 Stage 1 interview and 1 Stage 5 workshop
4. Run a Stage 4 Impact × Effort yourself
5. Pass Tiger AI's internal mock review

---

## License & Citation

This toolkit is licensed under Apache License 2.0; any consultant, in-house team, or derivative consulting methodology may use, modify, and commercialize it, provided the attribution in the [`NOTICE`](../NOTICE) file is preserved.
