# BARS Behaviorally Anchored Rating Scales: 6 Constructs × 0-4

> 🌐 中文版本 / Chinese version: [BARS_RUBRICS.md](BARS_RUBRICS.md)
>
> Apache License 2.0 · Author: Morris Lu · Tiger AI

Last updated: 2026-05-16

---

> **Purpose**: Upgrade the 6-construct × 0-4 scale from "abstract levels" to **Behaviorally Anchored Rating Scales (BARS)**, enabling any consultant to score the same company **near-consistently** (boosting inter-rater reliability).
>
> **Academic basis**: BARS originates from Smith & Kendall (1963) — a standard method in organizational behavior and performance assessment for improving scoring consistency. Each score has concrete observable behavior, avoiding subjective "gut scoring."
>
> **Application**: Operationalizes [`AI_MATURITY_SCORING_MODEL_EN.md`](AI_MATURITY_SCORING_MODEL_EN.md) §3.1 Construct Definition; serves as basis for [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) Inter-rater Reliability validation.

---

## 1. Discipline

| Rule | Description |
| --- | --- |
| **Score by behavior, not impression** | Score based on observable "has / hasn't" |
| **No half-points** | 0/1/2/3/4 integers only |
| **Lowest unmet level = actual score** | E.g., Level 3 requires (a)(b)(c)(d); missing (d) → score 2 |
| **Evidence must match Tool 8.9 Evidence Level** | High scores (3-4) require L3+ system logs or L4+ third-party audit |
| **Cross-rater disputes** | Bring in a third rater; if all three differ, return to "lowest unmet level" discipline |

---

## 2. Construct A: Tool Usage

| Score | Behavioral Anchor | Required Evidence |
| --- | --- | --- |
| **0** | No unified AI tool portal; no company AI accounts; no usage records; possibly private ChatGPT but ungoverned | L1 interviews + shadow IT observation |
| **1** | Sporadic self-funded AI use; **only some executives** have company accounts (≤ 20% staff); **no usage policy** or unsigned | L2 IT account list + interviews |
| **2** | Company AI portal exists; **some departments** (≥ 1) opened accounts (20-60% staff); **simple usage policy doc** (may not be signed); sporadic Prompt records | L2 account list + policy doc |
| **3** | **Company-wide** or **most depts** (≥ 60%) have accounts; **AI policy signed** (≥ 90% signed); **Prompt Library live** (≥ 30 entries with Owner); **monthly active ≥ 50% staff**; **shadow IT ≤ 10%** | L3 OpenWebUI / API Gateway audit log + Prompt Library Git |
| **4** | All L3 conditions + **cross-dept reuse ≥ 50%** (same Prompt used by ≥ 2 depts) + **full permission matrix** (role × resource × action) + **annual employee training audited** + **third-party audit passed** or ISO/IEC 42001 certification ready | L4 third-party audit + Audit Log |

---

## 3. Construct B: Knowledge Codification

| Score | Behavioral Anchor | Required Evidence |
| --- | --- | --- |
| **0** | No Skill Library / Wiki / SOPs; personal experience scattered in private notes, Slack DMs, oral transmission | L1 interviews + system inventory |
| **1** | Individual employees have "personal Prompt collections" (scattered in notes); no Owner / no version / unfindable by others | L2 interviews + sample personal notes |
| **2** | **Single department** (≥ 1) has dept Skill collection (≥ 5 items); **has Owner** but **incomplete version governance**; **other depts cannot reuse directly** | L2 dept Wiki / SharePoint |
| **3** | **Cross-dept Skill Library live**; **each Skill has Owner + version + IPOE doc**; **Git commit history traceable**; **monthly +≥ 10**; **cross-dept reuse occurring** (same Skill used by ≥ 2 depts) | L3 Git commit log + Wiki access log |
| **4** | All L3 + **monthly +≥ 20** + **new-hire onboarding Skill Library usage rate ≥ 80%** + **Skill auto-invocation** (Workflow / Agent auto-pulls Skill without manual selection) + **departing employee Skills don't leak** (mandatory SOP review before exit) | L3-L4 Wiki invocation log + new-hire interviews |

---

## 4. Construct C: Process Automation

| Score | Behavioral Anchor | Required Evidence |
| --- | --- | --- |
| **0** | All processes manually executed; no automation tools; no logs; no Workflow concept | L1 interviews + system inventory |
| **1** | Individuals or single depts use **scripts / Excel macros / Power Automate** for local tasks; **no AI reasoning**; **no HITL nodes**; no formal Owner | L2 sample scripts |
| **2** | **Few Workflows** (≥ 1 with AI step) but **unstable uptime < 95%**; **no formal Owner or log**; **demo stage, not in real business flow** | L2 Workflow design docs |
| **3** | **Cross-system Workflows ≥ 3 live** (with trigger / log / HITL); **each has Owner**; **uptime ≥ 95%**; **error handling + retry in place**; **monthly execution ≥ 100** | L3 n8n / orchestrator execution log |
| **4** | All L3 + **Workflows ≥ 10** + **version control (Git)** + **KPI longitudinal tracking** (≥ 6 months) + **cross-dept spread** + **error rate < 1%** + **Reviewer sign-off ≥ 95%** | L3-L5 system log + longitudinal KPI |

---

## 5. Construct D: System Integration

| Score | Behavioral Anchor | Required Evidence |
| --- | --- | --- |
| **0** | Systems (Gmail / Sheets / CRM / ERP) fully siloed; all data manually exported/imported | L1 interviews + system map |
| **1** | **Some manual inter-system integration** (e.g., IT cron jobs moving CSVs); **no API governance**; **no redact for sensitive data** | L2 system inventory + sampling |
| **2** | **Some systems API-integrated** (≥ 2 connected); **API auth by personal accounts**; **simple redact rules but incomplete coverage** | L2 integration docs + DLP sampling |
| **3** | **Core systems API-governed** (≥ 5 connected, OAuth / SSO); **API Gateway live** (rate limit + auth log); **sensitive-data redact coverage ≥ 80%**; **integration error rate < 5%** | L3 API Gateway audit log + DLP alert log |
| **4** | All L3 + **redact coverage 100%** + **Zero Trust architecture** + **third-party security audit passed** (SOC 2 / ISO 27001) + **Data Classification complete** | L4 third-party audit report |

---

## 6. Construct E: Agent Application

| Score | Behavioral Anchor | Required Evidence |
| --- | --- | --- |
| **0** | **No AI Agent concept**; possibly chatbots but **no Wiki memory / no multi-step / no tool calls** | L1 interviews |
| **1** | **Agent demos** (≤ 5 tasks) but **not in business flow**; **no Reviewer**; **no persistent Wiki memory** | L2 Agent demo docs |
| **2** | **1 Agent live** (single scenario, e.g., FAQ); **has HITL Reviewer**; **has task log**; **monthly tasks ≥ 20**; **not yet passed Stage Gate 4A-4E full acceptance** | L3 Agent task log + Reviewer log |
| **3** | **≥ 1 Agent passes full 4A-4E acceptance**; **Wiki ingest/query/update all running**; **monthly tasks ≥ 100**; **Reviewer pass rate ≥ 85%**; **evidence trail complete** (input → process → output → log) | L3 Agent log + Wiki audit |
| **4** | All L3 + **≥ 2 Agents live** + **cross-Agent task chains** + **L5 ClawTeam cross-dept rehearsal ≥ 1 successful** + **Reviewer pass rate ≥ 95%** + **Agent ROI longitudinal tracking** | L3-L5 system log + longitudinal KPI |

---

## 7. Construct F: Implementation Governance

| Score | Behavioral Anchor | Required Evidence |
| --- | --- | --- |
| **0** | **No AI Policy**; **no permission matrix**; **no Audit Log**; **no data classification**; no AI Champion / Sponsor role | L1 interviews |
| **1** | **Verbal AI guidelines** (no doc); **Sponsor confirmed** (CEO / CIO); **no Champion**; **chaotic permissions** | L2 interviews + Sponsor confirmation |
| **2** | **AI Policy doc exists** (written but signed < 50%); **AI Champion part-time**; **some systems have Audit Log**; **Risk Register exists but rarely updated** | L2 Policy doc + Champion confirmation |
| **3** | **Policy signed ≥ 90%** + **full Permission Matrix** + **Audit Log covers all LLM calls** (retention ≥ 90 days) + **5-dim Value Tracking live** + **Ethics Checklist ≥ 12/15 passed** + **quarterly Risk Register review** | L3 Audit Log + L4 internal audit report |
| **4** | All L3 + **ISO/IEC 42001 / 27001 certification ready or obtained** + **EU AI Act alignment** (if EU business) + **annual third-party audit passed** + **Ethics Checklist 100% passed** + **AI incident response drill ≥ 1/year** | L4 third-party certification + L5 longitudinal audit |

---

## 8. Inter-Rater Calibration

### 8.1 Dual-Rater Calibration Exercise

Before new consultant onboarding or formal scoring: **A and B raters** independently score the same "teaching simulation" company, then compare:

```
Step 1: A scores → don't inform B
Step 2: B scores → don't inform A
Step 3: Compare 6 construct scores
Step 4: If any construct differs by ≥ 2 → review meeting (usually anchor interpretation differs)
Step 5: After calibration, proceed to next company
```

**Target**: Cohen's κ ≥ 0.60 (substantial agreement). See [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) §3.

### 8.2 Common Scoring Disputes

| Scenario | Handling Principle |
| --- | --- |
| Client says "yes" but no evidence visible | Apply **"lowest unmet level"** rule (don't give high score) |
| One dept has it but not company-wide | Primary maturity = overall score; local maturity noted "CS dept L3 / company L1" |
| Tool exists but governance missing | Governance is Construct F; doesn't affect A-E |
| Employees can use but company hasn't opened accounts | Lower Construct A by one level (individual ≠ enterprise maturity) |

---

## 9. BARS Significance for Tiger AI Methodology

| Goal | Achieved by |
| --- | --- |
| **Improve Inter-rater Reliability** | Replace subjective judgment with concrete behavior descriptions |
| **Reduce client challenges** | Clients see "behavior checklist" basis, not "consultant impression" |
| **Support Pilot Study Cohen's κ ≥ 0.60** | BARS is the core mechanism |
| **Reduce new consultant onboarding time** | BARS table directly tells how to score, less mentoring needed |
| **Prepare for ISO/IEC 42001 certification** | Certifiers look for "objectivity of assessment method"; BARS is industry standard |

---

## 10. References

- Smith, P. C., & Kendall, L. M. (1963). Retranslation of expectations: An approach to the construction of unambiguous anchors for rating scales. *Journal of Applied Psychology*, 47(2), 149-155.
- Schwab, D. P., Heneman, H. G., & DeCotiis, T. A. (1975). Behaviorally anchored rating scales: A review of the literature. *Personnel Psychology*, 28(4), 549-562.
- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.

---

License & Citation

This document is Apache License 2.0; may be used, modified, commercialized, provided the [`../NOTICE`](../NOTICE) attribution is preserved.
