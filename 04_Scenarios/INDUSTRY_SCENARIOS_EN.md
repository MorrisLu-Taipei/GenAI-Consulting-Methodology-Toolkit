# Industry Recommended Scenarios

> 🌐 中文版本 / Chinese version: [INDUSTRY_SCENARIOS.md](INDUSTRY_SCENARIOS.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>

Recommended AI scenarios for 5 industries: retail, education, logistics, software, and professional services. Each section covers an industry intro, L1-L5 maturity baseline, Top 10 recommended scenarios, risk & governance, a 30-day quick win, and anti-patterns.

---

## 1. Retail

### 1.1 Industry Intro

Retail spans brick-and-mortar chains, e-commerce, and D2C brands. Key processes: products / orders / inventory / channels / loyalty / marketing. Regulated by personal data protection law, consumer protection law, and the FSC for credit-card flows.

**Taiwan retail AI maturity baseline (2026):** most enterprises sit between **L1 and L2**. Some chain brands have L3 PoCs (social listening, product copy). L4-L5 are pioneers.

### 1.2 Top 10 Recommended Scenarios

| # | Scenario | Department | L | Description | Systems / data | ROI lever | Complexity |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| R1 | Store-associate AI assistant (product / inventory lookup) | Store | L3 | Associates use a mobile app to chat-query products, inventory, prices | POS / WMS / product DB | Time | Medium |
| R2 | Bulk product copy generation | Merchandising / Marketing | L2 | Auto-produce multilingual product descriptions from specs | PIM / Sheets | Time + quality | Low |
| R3 | Dynamic pricing recommendations | Merchandising / Pricing | L4 | Pricing ranges combining competitors, inventory, season | competitor crawler / inventory / POS | Revenue | High |
| R4 | Returns/exchanges triage & summary | CS | L3 | Classify return reasons, prioritize handling | Email / CS system | Time + NPS | Medium |
| R5 | Loyalty engagement | Loyalty / Marketing | L3 | Personalized recommendations, birthday / anniversary messages | CRM / orders | Revenue | Medium |
| R6 | Replenishment recommendations (cross-store / cross-warehouse) | Operations | L4 | Recommend replenishment based on sell-through and safety stock | WMS / POS | Reduced stockouts | High |
| R7 | Footfall analysis (physical stores) | Operations | L4 | Camera + AI for footfall, dwell time, conversion | cameras / POS | Operational decisions | High |
| R8 | Social listening | Marketing / PR | L3 | Monitor FB / IG / Threads / Dcard brand mentions + sentiment | social APIs | Risk early warning | Medium |
| R9 | Online-offline inventory sync | Operations / IT | L3 | Unified view to avoid overselling / stockouts | OMS / WMS / e-commerce | Revenue + satisfaction | Medium |
| R10 | Customer 360 view | Marketing / Sales | L4 | Integrate online-offline member data + AI summary | CDP / CRM / POS | Revenue + LTV | High |

### 1.3 Risk & Governance

- **Personal data and payments:** member data and credit-card tokens must be redacted before entering the LLM
- **Brand consistency:** AI-generated copy needs a Brand Guidelines reviewer
- **Inventory decisions:** replenishment recommendations need a human Gate to avoid AI over-ordering
- **Dynamic pricing:** avoid discriminatory pricing (differential treatment by demographic)

### 1.4 30-Day Quick Win

> **R2 product copy + R8 social listening:** two low-risk, immediately effective items with high employee adoption.

### 1.5 Anti-Patterns

- ❌ Skipping L1 and jumping straight to dynamic pricing (no trust from store/merchandising colleagues)
- ❌ An AI chatbot replacing front-line CS (no fallback for high-sensitivity interactions)
- ❌ Putting AI copy live without Brand Guidelines review

---

## 2. Education

### 2.1 Industry Intro

Covers K-12, higher education, corporate training, and EdTech. Affected by personal data law (student records), Ministry of Education rules, and IP (course materials).

**Taiwan education AI maturity baseline:** L1. A few universities and EdTechs at L2-L3. Parent and student acceptance is gradually rising, but teacher resistance is still notable.

### 2.2 Top 10 Recommended Scenarios

| # | Scenario | Audience | L | Description | Systems / data | ROI lever | Complexity |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| E1 | Teacher lesson-plan draft | Teachers | L2 | Draft lesson plans from the syllabus + class data | Sheets / syllabus DB | Time | Low |
| E2 | Student assignment feedback (formative) | Teachers | L3 | Student work → AI summary of key points and weaknesses | LMS | Time + quality | Medium |
| E3 | Parent communication draft | Teachers / Admin | L2 | Drafts for mid-term reports, incidents, parent-meeting notices | Email / student DB | Time | Low |
| E4 | Admissions Q&A (chatbot) | Admissions | L3 | 24/7 admissions consulting, auto-routing questions to humans | website / FAQ | Admissions conversion | Medium |
| E5 | Course search & recommendation (RAG) | Students / University | L4 | A student asks "I want to study X" and AI gives a course combination | course DB | Student satisfaction | Medium |
| E6 | AI content checking (plagiarism + AI-text) | Teachers | L3 | Detect AI proportion + plagiarism in student work | LMS / third-party API | Academic integrity | Medium |
| E7 | Accessibility (TTS / translation / captions) | Teachers / Students | L2 | Auto-caption, translate, text-to-speech for course recordings | LMS | Inclusivity | Low |
| E8 | Grading rubric assistant | Teachers | L3 | AI gives a preliminary score by rubric, teacher confirms | LMS | Time | Medium |
| E9 | Alumni engagement | Admin | L3 | Alumni data updates, event recommendations | CRM | Fundraising + cohesion | Medium |
| E10 | Accreditation evidence collation | Admin / Departments | L4 | Auto-collate departmental accreditation documents, evidence links | Notion / Drive | Time + quality | High |

### 2.3 Risk & Governance

- **Student personal data:** minors' data needs enhanced protection; GDPR-K
- **AI content checking:** high false-positive risk, needs an appeal mechanism
- **Teacher professional authority:** AI cannot replace teaching decisions; human final confirmation required
- **Course-material IP:** clearly distinguish teacher / school / AI vendor ownership of materials

### 2.4 30-Day Quick Win

> **E1 lesson plan + E3 parent comms:** the two heaviest teacher tasks; immediate workload relief.

### 2.5 Anti-Patterns

- ❌ AI giving students answers directly instead of guiding
- ❌ AI grading entered as a grade without teacher confirmation
- ❌ Treating an AI admissions chatbot as "never needing a human"

---

## 3. Logistics

### 3.1 Industry Intro

3PL, freight forwarding, last-mile delivery, warehousing. Key processes: orders / picking / routing / shipping / exception handling. Affected by customs and transportation regulations.

**Taiwan logistics AI maturity baseline:** L1-L2. A few large 3PLs at L3 (route optimization, exception alerts).

### 3.2 Top 10 Recommended Scenarios

| # | Scenario | Department | L | Description | Systems / data | ROI lever | Complexity |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| L1-1 | Shipping exception triage | CS / Operations | L3 | Auto-classify exception cases (delay / damage / lost) | TMS / tickets | Time + NPS | Medium |
| L2-1 | Customs document drafting | Customs brokerage | L3 | Auto-produce customs document drafts from orders | ERP / customs rules | Time + accuracy | Medium |
| L3-1 | Route deviation interpretation | Operations | L4 | Route deviation / delay → AI explains the cause + recommendation | GPS / TMS | Operational decisions | High |
| L4-1 | Driver app FAQ assistant | Drivers / IT | L3 | Drivers ask about app operations / SOP / exception handling | LMS / knowledge base | Time | Medium |
| L5-1 | Warehouse SOP retrieval | Warehouse | L3 | Warehouse staff ask about SOP / safety / rules and get answers | Wiki | Time + safety | Medium |
| L6-1 | Customer ETA chatbot | CS | L3 | Auto-reply to customer shipment queries + predict ETA | TMS / WMS | CS workload reduction | Medium |
| L7-1 | Claims processing | CS / Legal | L3 | Classify claims cases, check evidence, calculate compensation | tickets / insurance | Time + accuracy | Medium |
| L8-1 | Daily operations KPI digest | Operations manager | L3 | Managers get key KPIs and anomalies at 8am daily | TMS / WMS | Manager time | Medium |
| L9-1 | Partner outreach | Sales / Procurement | L3 | Auto-generate solicitation emails, contract drafts | CRM | Sales time | Medium |
| L10-1 | Regulatory update tracking | Legal / Customs | L4 | Summary of changes to each country's customs / transport regulations | government website RAG | Risk early warning | High |

### 3.3 Risk & Governance

- **Driver privacy:** GPS / behavior data access must be restricted
- **Customs / regulations:** AI-drafted documents must be confirmed by Legal to avoid fines from mis-filing
- **Customer ETA prediction:** state explicitly as a prediction, not a guarantee, to avoid over-promising

### 3.4 30-Day Quick Win

> **L1-1 exception triage + L8-1 KPI digest:** what operations managers feel most.

### 3.5 Anti-Patterns

- ❌ AI route recommendations sent out without dispatcher confirmation
- ❌ AI auto-closing claims cases without notifying a human

---

## 4. Software (B2B SaaS, ISV)

### 4.1 Industry Intro

SaaS, on-prem ISVs, professional-services arms. Key processes: product / customers / engineering / support / sales. They are themselves early AI adopters with the lowest employee resistance.

**Taiwan software-industry AI maturity baseline:** L2-L3. Widespread real use of Copilot / Cursor / Claude Code. L4 Agents increasingly common.

### 4.2 Top 10 Recommended Scenarios

| # | Scenario | Department | L | Description | Systems / data | ROI lever | Complexity |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| SW1 | Support-ticket classification & draft | CS | L3 | Classify Zendesk / Intercom tickets + reply drafts | CS system | Time + FCR | Medium |
| SW2 | Doc generation (from code) | Engineering | L2 | Auto-produce docs from code comments + API specs | GitHub / Notion | Time | Medium |
| SW3 | Release notes drafting | PM / Engineering | L2 | Auto-produce release notes from commits / PRs | GitHub | Time | Low |
| SW4 | Customer churn-risk scoring | CS / Product | L4 | Compute churn from product usage + tickets + billing | own data | Revenue + LTV | High |
| SW5 | CSM customer brief | CS | L4 | Auto-brief the CSM before a meeting: last interaction, open tickets, contract | CRM / tickets | Customer quality | High |
| SW6 | QA auto test-case generation | QA / Engineering | L3 | Produce test cases from user stories | Jira / TestRail | Quality + time | Medium |
| SW7 | On-call shift summary | SRE / Engineering | L3 | At end of shift, AI summarizes incidents, decisions, todos | PagerDuty / Slack | Knowledge transfer | Medium |
| SW8 | Customer onboarding plan generation | CS | L3 | Auto-produce an onboarding plan from the customer profile | CRM | Time + customer NPS | Medium |
| SW9 | Code review companion | Engineering | L4 | Auto-suggest PR comments; does not replace the reviewer | GitHub | Quality + time | Medium |
| SW10 | Partner enablement Q&A | Sales / Channels | L3 | Partners ask about product features and get answers (RAG) | Notion / Wiki | Partner self-service | Medium |

### 4.3 Risk & Governance

- **Customer data:** SaaS multi-tenant data must be isolated; tenants must not be mixed
- **Code:** keep sensitive code off cloud LLMs; self-hosting can be used
- **Customer commitments:** an AI chatbot must not give committal answers (SLA / refunds)
- **Security:** AI-generated code must still pass SAST / DAST

### 4.4 30-Day Quick Win

> **SW2 docs + SW3 release notes:** immediate engineering workload relief, no risk.

### 4.5 Anti-Patterns

- ❌ AI directly merging PRs (bypassing code review)
- ❌ A customer chatbot giving vague commitments
- ❌ Training your own model on customer data without notice

---

## 5. Professional Services

### 5.1 Industry Intro

Law firms, accounting / tax, management consulting, design / creative agencies. Key processes: BD / engagement / delivery / billing / knowledge management. Affected by professional ethics codes (Lawyers Act, CPA Act) and client confidentiality.

**Taiwan professional-services AI maturity baseline:** L1-L2. Most partners use ChatGPT / Claude individually, but organizational adoption is low.

### 5.2 Top 10 Recommended Scenarios

| # | Scenario | Audience | L | Description | Systems / data | ROI lever | Complexity |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| PS1 | Client intake summarization | Lawyers / Consultants | L3 | Consultation recording → structured intake document | Zoom / Whisper / DMS | Time + quality | Medium |
| PS2 | Contract clause Q&A (RAG) | Lawyers | L4 | Ask "how is this clause used" against your own contract templates | DMS / Notion | Time + consistency | High |
| PS3 | Time-entry auto-categorization | Everyone | L3 | calendar + email + chat → time-entry categorization | Outlook / Slack | Billing accuracy | Medium |
| PS4 | Billing narrative drafting | Lawyers / Accountants | L2 | Auto-produce client-readable narratives from time entries | timekeeping system | Time + client satisfaction | Low |
| PS5 | Conflict check (Q&A) | Legal management | L3 | Conflict check of a new matter against existing clients / opposing parties | client DB | Risk + ethics | Medium |
| PS6 | Proposal RAG (over past work) | BD / Partners | L4 | RAG over past proposals / cases for a new proposal | DMS | Sales conversion | High |
| PS7 | Deliverable QA | Lawyers / Consultants | L3 | Check deliverables for format / citations / spelling / logic | Word / Notion | Quality | Medium |
| PS8 | Client onboarding brief | Partners | L4 | New client → auto-brief public info, industry, past collaboration | News / public DB | Time + client impression | Medium |
| PS9 | Knowledge management Agent | Everyone / KM | L4 | Put the firm-wide knowledge base behind an Agent interface, Q&A + citations | Wiki / DMS | Knowledge transfer | High |
| PS10 | BD outreach | Partners / BD | L3 | Produce personalized outreach emails for target clients | LinkedIn / CRM | Sales pipeline | Medium |

### 5.3 Risk & Governance

- **Client confidentiality:** legal / accounting data is extremely sensitive; Hybrid or full on-prem is recommended
- **Professional liability:** AI-drafted opinions must be confirmed by a lawyer / accountant; never issued directly
- **Conflict of interest:** AI conflict checking does not replace the formal conflict-check process
- **Billing accuracy:** AI time-entry / billing drafts must be confirmed by a lawyer to avoid billing errors

### 5.4 30-Day Quick Win

> **PS4 billing narrative + PS7 deliverable QA:** low-risk, high-frequency, immediately effective.

### 5.5 Anti-Patterns

- ❌ Processing confidential client documents with a cloud LLM without redaction
- ❌ Issuing an AI-drafted opinion directly to the client
- ❌ Sending a billing narrative to the client without confirmation

---

## Cross-Industry Recommendations

### Where to Start

Regardless of industry, the recommendation is:
1. L1 OpenWebUI org-wide kickoff (governance priority)
2. Find a pain point "employees feel daily" for an L2-L3 PoC
3. Prove ROI, then expand to L4 Agents
4. After 8-12 months, evaluate L5 Agent Teams

### Where to Be Careful

- **Level-skipping mistakes:** don't push L4 Agents before the L1 foundation is laid
- **No sponsor:** a project without executive commitment will fail within 6 months
- **No reviewer:** AI output must have a human sign-off mechanism
- **No audit log:** Compliance and Internal Audit must see the audit log before they trust you
- **No exit mechanism:** each Stage Gate must be able to stop if not passed — don't force it through

### Cite

Detailed scenario descriptions: `CUSTOMER_SCENARIO_LIBRARY.md`; cases: `SAMPLE_CLIENT_CASE_*.md`; courses: `02_Course_Design/`.
