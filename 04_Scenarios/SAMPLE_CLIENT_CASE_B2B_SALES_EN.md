# Sample Client Case: B2B Sales

> 🌐 中文版本 / Chinese version: [SAMPLE_CLIENT_CASE_B2B_SALES.md](SAMPLE_CLIENT_CASE_B2B_SALES.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>
>
> **Sample case for illustration. The client is referred to by the code "Industrial Vendor B" (not a real company name). Content is synthesized from multiple real B2B engagements; numbers are illustrative.**

---

## 1. Client Profile

| Field | Content |
| --- | --- |
| Client code | Industrial Vendor B (industrial automation + software, anonymized) |
| Industry | Industrial automation equipment + software (PLC / SCADA / solution selling) |
| Employees | 380 (Sales + Engineering + Support) |
| Sales team | 60 (incl. SDR 12 + AE 32 + SE 8 + Sales Ops 8) |
| Clients | 240 active enterprise clients (manufacturing, energy, semiconductor, food) |
| Annual revenue | NT$ 1.2B |
| Average deal size | NT$ 3.8M |
| Average sales cycle | **9-14 months** |
| Starting L-level | L2 (partially L3) |
| Budget | NT$ 7.2M (12 months) |
| Main pain points | (1) Sales cycle too long (2) Fragmented CRM data (3) RFP response takes 14 days (4) SDR→AE handoff gap |

## 2. Engagement Onboarding & Diagnostic

### 2.1 10-Question Quick Survey Results

| Q | Score |
| ---: | ---: |
| Q1 Tool usage | 3 |
| Q2 Knowledge codification | 2 |
| Q3 Process standardization | 2 |
| Q4 System integration | 2 |
| Q5 Agent application | 1 |
| Q6 Governance + Audit | 2 |
| Q7 ROI quantifiable | 2 |
| Q8 Clear next step | 3 |
| Q9 Manager review | 2 |
| Q10 Risk protection | 2 |
| **Average 2.1 → L2-L3 borderline** | |

### 2.2 25-Question Six Constructs

| Construct | Average |
| --- | ---: |
| Tool usage | 3.0 |
| Knowledge codification | 2.1 |
| Process standardization | 1.8 |
| System integration | 2.0 |
| Agent application | 0.8 |
| Governance & ROI | 2.0 |

**Insight:** tools are widespread but Agent usage is zero; knowledge codification is concentrated in senior AEs' heads (high attrition risk).

### 2.3 Company Profile Bundle (key points)

```json
{
  "profile": {"industry":"b2b_industrial","headcount_bucket":"300-1000"},
  "systems": {"crm":"Salesforce","erp":"SAP","support":"Zendesk","cpq":"Salesforce CPQ","wiki":["Confluence"]},
  "risk": {"sensitive_data":["client facility data","RFP","pricing"],"regulations":["personal data law"],"llm_retention_acceptance":"reject"},
  "deployment": {"preference":"Hybrid","gpu_capacity":"L40 class","local_llm_plan":"yes"},
  "course": {"l1_headcount":380,"seed_team_headcount":18,"objectives":["workflow automation","Agent building"]},
  "budget": {"annual_bucket":"2M-10M","first_poc":"<1 month"}
}
```

## 3. Recommended Course Mix

| Level | Ratio | Focus |
| ---: | ---: | --- |
| L1 | 20% | Fill in policy and permissions; emphasize pricing / RFP red lines |
| L2 | 25% | RFP / Demo / technical-document Skills |
| L3 | 30% | CRM-to-Slack alerts, lead scoring, deal-stage automation, forecast aggregator |
| L4 | 20% | Account Briefing Hermes Agent |
| L5 | 5% | Pre-RFP Response ClawTeam |

Rationale: starting at L2-L3 → focus on filling in Skill codification + system-integration automation + Agents. RFPs are the sales cash cow, the highest lever.

## 4. In-Class Artifacts

### L1 OpenWebUI (3 weeks)

- 380 accounts + groups (Sales / Eng / Support / Admin)
- AI usage policy: client-data boundaries (facility layouts / RFP content forbidden from cloud LLMs)
- Prompt Library, 28 entries (pre-visit brief, post-visit follow-up, Demo intro, competitor comparison)

### L2 Skill AI (6 weeks)

15 Skills:

| # | Skill | Owner |
| --- | --- | --- |
| 1 | Pre-visit Account brief (auto-integrates CRM / news / public info) | AE |
| 2 | Post-visit follow-up email | AE |
| 3 | RFP section draft (technical / commercial / service) | SE / Sales |
| 4 | Demo opening and scenario stitching | SE |
| 5 | Competitor feature comparison table | Product Marketing |
| 6 | Customer ROI calculator worksheet draft | Sales |
| 7 | Quote narrative + alternative options | Sales |
| 8 | Legal/MSA common-clause Q&A | Legal |
| 9 | Existing-customer health summary | CSM |
| 10 | Onboarding playbook (by industry) | CSM |
| 11 | Technical document → customer FAQ | SE |
| 12 | Monthly QBR draft for the customer | AE / CSM |
| 13 | Forecast call narrative | Sales Manager |
| 14 | Lead-qualification rubric for SDRs | SDR Lead |
| 15 | Account map visualization (decision-makers, influencers, technical evaluators) | AE / SE |

### L3 n8n Workflow (8 weeks)

7 Workflow PoCs:

1. **Lead scoring + auto-assignment** — Form/HubSpot inbound → enrichment API → Skill #14 → Salesforce assignment + Slack DM
2. **CRM → Slack alert** — Salesforce Webhook → major stage change / large amount → Slack with brief
3. **Deal stage automation** — stage movement triggers a follow-up email, task, template defaults
4. **Weekly forecast aggregator** — Schedule Sun 9pm → Salesforce → Skill #13 → Sales Manager email
5. **Customer health score** — Schedule daily → Salesforce + Zendesk + product usage → Skill #9 → field update + alert
6. **RFP intake auto-classification** — Email Trigger → OpenAI → Notion task + AE assignment
7. **Competitor price crawler + summary** — Schedule weekly → web scrape → Skill #5 → Confluence

### L4 Hermes Agent — Account Briefing (4 weeks)

**Sales Account Briefing Agent:**
- Wiki: customer history (past interactions / contracts / litigation / management changes / public news)
- Skills used: #1, #5, #9, #15
- Workflows used: CRM alert, customer health
- Task card: 1 hour before each AE visit, automatically produce a brief
- Reviewer: AE acknowledges (reject / modify / accept)
- Evidence: full source traceability for every brief
- Gates 4A-4E passed

### L5 ClawTeam — Pre-RFP Response Team (2-week exercise)

Based on HKUDS/ClawTeam (MIT), composed of 6 Agents:

| Agent role | Task |
| --- | --- |
| **Solution Architect Agent** | Extract technical requirements from the RFP, map to product solutions |
| **Pricing Agent** | Give a pricing range based on the product mix and customer segment |
| **Legal Agent** | Compare against the MSA, identify risk points in the client's RFP clauses |
| **Reference Agent** | Find similar-customer case studies from the CRM |
| **Reviewer Agent** | Brand safety + commercial consistency |
| **Coordinator (Human Gate)** | Sales Director |

Actual scenario: for a semiconductor major-account RFP, the past 14-day response was compressed to 5 days, with broader coverage.

## 5. Eight-Stage Analysis

### Stage 1 Current-State Discovery
- Interviews: CSO, 3 Sales Managers, 2 Account Directors, SE Lead, CRM Admin, Legal
- Pain density: RFP response (90%), inaccurate forecasts (60%), SDR→AE handoff gap (45%)

### Stage 2 Vision Alignment
- CSO vision: within 18 months, sales cycle 9-14 months → 6-9 months; RFP 14 days → 5 days; win rate 22%→32%
- Stakeholder: CSO = Sponsor; Sales Ops Lead = AI Champion

### Stage 3 Industry Benchmark
- B2B Industrial: Salesforce Einstein, Gong, Outreach AI (features for reference but not directly adopted)
- Self-built (Hybrid) to protect RFP / pricing sensitivity

### Stage 4 Gap Analysis

Missing/Broken/Redundant:
- **Missing:** Account brief automation, RFP Library, lead-scoring model, forecast narrative
- **Broken:** CRM data quality — 35% of fields blank; SDR→AE handoff relies on email
- **Redundant:** 3 sets of follow-up email templates (each team makes its own)

Impact × Effort:
- Quick Win: Account brief Skill (L2-W2); CRM Slack alert (L3-W1)
- Big Bet: Pre-RFP ClawTeam (L5, months 11-12)
- Avoid: a self-built LLM-based forecasting model (insufficient data)

### Stage 5 Executive Problem Statement

```
CONTEXT: In the past 12 months, competitors Siemens / Rockwell increased the speed of their
         digital RFP responses; our 14-day RFP average lost 3 deals worth NT$ 28M. One of our
         senior AEs is about to retire — high knowledge-gap risk.
TENSION: Tools are widespread but the organization (L2) hasn't codified enough; senior AEs'
         personal knowledge is hard to replicate.
COI: If no action for 12 months: (1) estimated NT$ 60M RFP loss (2) after the senior AE retires,
     new-hire ramp-up is 12+ months.
DESIRED: Reach L4 in 12 months; RFP 5 days; forecast accuracy ±10%; new-hire ramp-up 3 months.
CONSTRAINT: NT$ 7.2M budget; RFP / pricing data cannot go to a cloud LLM; CRM must have data
            governance first.
```

### Stage 6 Roadmap

| Phase | Month | Main deliverables | Gate | KPI |
| --- | --- | --- | --- | --- |
| 1 | 1-2 | L1 + policy + CRM data cleanup | Gate 1 ✓ | CRM required-field rate ≥ 90% |
| 2 | 3-4 | L2 15 Skills | Gate 2 ✓ | RFP drafting 14d → 8d |
| 3 | 5-7 | L3 7 Workflows | Gate 3 ✓ | lead assignment < 5 min |
| 4 | 8-10 | L4 Account Briefing Agent | Gate 4 ✓ | visit-brief adoption rate ≥ 80% |
| 5 | 11-12 | L5 Pre-RFP ClawTeam | Gate 5 ✓ | RFP 14d → 5d |

### Stage 7 Solution Architecture

- **Hybrid deployment:**
  - Public data / public news → cloud (Anthropic Claude)
  - Customer history / RFP / pricing → on-prem Llama 70B (L40 GPU)
- **CRM:** Salesforce Webhook → n8n self-host
- **Wiki:** Confluence → embedding → Qdrant vector DB (on-prem)

### Stage 8 Governance & ROI

- Permissions: four tiers — Sales / SE / Manager / Director; field-level ACL on the CRM
- Audit Log: all LLM calls retained 1 year; RFP-related 3 years
- ROI Tracker: sales cycle, RFP days, win rate, forecast accuracy, AE ramp-up

## 6. Diagnostic Report Summary

> **Core finding:** Industrial Vendor B is at the L2-L3 borderline — tool usage is widespread but organizational knowledge codification is insufficient, and senior-employee attrition risk is about to trigger. Recommend advancing to L4 in 12 months (Account Briefing Agent + Pre-RFP Team), while strengthening CRM data governance.
>
> **Expected ROI:** quantifiable benefit of NT$ 44M over 12 months, ROI ≈ 511%.

## 7. 30/60/90-Day Roadmap

### 30 days
- L1 OpenWebUI 380 accounts + policy
- CRM data-governance sprint: required-field strategy, historical-data cleanup
- Launch Skill #1 pre-visit brief (quick win)
- Gate 1 passed

### 60 days
- Skill Library, 15 complete
- RFP Library structured (split past RFPs into sections, tag them)
- Workflow PoCs #1, #2 live
- Gate 2 passed
- RFP drafting 14 days → 10 days

### 90 days
- All 7 Workflows live
- Forecast aggregator runs in full for the first time
- Account Briefing Agent planning + Wiki construction kicked off
- Gate 3 passed
- Lead assignment time < 5 min; CRM required fields ≥ 90%

## 8. ROI Projection

| Initiative | Baseline | 12-month Target | NT$ impact |
| --- | --- | --- | --- |
| RFP response days | 14 days | 5 days | NT$ 6M (AE/SE freed up) |
| RFP loss (due to slowness) | 3 deals/year | 0 deals | NT$ 28M |
| Forecast accuracy | ±25% | ±10% | NT$ 4M (inventory + planning) |
| Account brief adoption | 25% | 80% | NT$ 6M (12 more visits per AE per year) |
| AE ramp-up | 12 months | 6 months | NT$ 5M (4 new hires/year) |
| Forecast call hours | 4 hr/week × 8 managers | 1 hr | NT$ 2.5M |
| **Subtotal** | | | **NT$ 51.5M** |
| **Less investment** | | | **-7.2M** |
| **Net benefit** | | | **NT$ 44.3M / year** |

## 9. Risks & Governance

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| RFP / pricing leaked to a cloud LLM | High | Critical | on-prem Llama; DLP; Audit log; employee education |
| AI hallucinates on technical specs | High | High | mandatory SE review; Hermes evidence mechanism |
| Low CRM data quality → garbage AI output | High | High | Month 1 project: CRM cleanup sprint |
| AEs don't adopt the Account brief | Medium | Medium | Champion AE leads; brief embeds auto deal updates |
| Forecast Agent deviates from reality | Medium | High | Human Gate; keep human override |

## 10. Outcome Summary

After 12 months:
- Advanced from L2 to L4 (Pre-RFP ClawTeam in pilot)
- RFP 14 days → 5 days; win rate 22% → 30% (heading toward 32%)
- Forecast accuracy ±25% → ±12%
- After one senior AE retires, new-hire ramp-up is 6 months (was 12)
- The CSO is promoted to group CDO; the Sales Ops Lead becomes the AI Practice Lead

References: full PoC `02_Course_Design/POC_SCENARIO_SPECS.md`; industry `INDUSTRY_SCENARIOS.md`; consulting toolkit `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`; ClawTeam citation `90_References/CLAWTEAM_REFERENCE.md`.
