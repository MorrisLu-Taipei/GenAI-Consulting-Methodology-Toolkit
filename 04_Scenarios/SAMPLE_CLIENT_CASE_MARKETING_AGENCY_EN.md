# Sample Client Case: Marketing Agency

> 🌐 中文版本 / Chinese version: [SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md](SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>
>
> **Sample case for illustration. The client is referred to by the code "Agency M" (not a real company name). Content is synthesized from multiple real engagements; numbers are illustrative.**

---

## 1. Client Profile

| Field | Content |
| --- | --- |
| Client code | Agency M (digital marketing agency, anonymized) |
| Industry | Digital marketing agency (Performance + Content + Social) |
| Employees | 120 |
| Clients | 27 brand clients (FMCG / F&B / cosmetics / medical aesthetics) |
| Annual revenue | NT$ 320M |
| Department structure | Strategy 8 / Account 24 / Creative 32 / Media-Buy 18 / Data 12 / Production 18 / Admin 8 |
| Starting L-level | L1 (marginal) |
| Kickoff | 2026 Q1 |
| Budget | NT$ 4.8M (12 months) |
| Main pain points | Three fast, three slow: clients want it fast, content is slow; many reports, insight is slow; proposals are urgent, depth is slow |

## 2. Engagement Onboarding & Diagnostic

### 2.1 10-Question Quick Survey Results

| Q | Question | Score (0-4) |
| ---: | --- | ---: |
| Q1 | Employees use AI tools daily | 3 |
| Q2 | Prompts / experience centrally organized | 1 |
| Q3 | Has a definition of "good AI usage" | 1 |
| Q4 | AI connected to enterprise systems | 1 |
| Q5 | Has repeatable callable Skills / Workflows | 1 |
| Q6 | AI usage policy + Audit | 0 |
| Q7 | AI has quantifiable outcomes | 1 |
| Q8 | Has a clear next step (not relying on a vendor) | 2 |
| Q9 | Managers review regularly | 1 |
| Q10 | AI risk protection | 0 |
| **Average** | | **1.1 → L1** |

**Insight:** high individual usage (Q1=3) but zero governance (Q6=0, Q10=0). A textbook **shadow IT** stage, with very high sensitive-data leakage risk (brand-client data).

### 2.2 25-Question Six-Construct Scores

| Construct | Average | Bar |
| --- | ---: | --- |
| Tool usage | 2.8 | ▓▓▓▓▓▓░░░░ |
| Knowledge codification | 0.9 | ▓▓░░░░░░░░ |
| Process standardization | 1.2 | ▓▓▓░░░░░░░ |
| System integration | 1.0 | ▓▓░░░░░░░░ |
| Agent application | 0.5 | ▓░░░░░░░░░ |
| Governance & ROI | 0.4 | ▓░░░░░░░░░ |

Overall L1, with tool usage leaning toward L2. **A large local-maturity gap** — employees can use it but the organization has no capability.

### 2.3 Company Profile Bundle (key points)

```json
{
  "profile": { "industry": "marketing_agency", "headcount_bucket": "50-300", "markets": ["TW"] },
  "systems": { "wiki": ["Notion"], "crm": "HubSpot", "asana": true, "figma": true, "media_buy": ["GA4","Meta Ads","Google Ads"] },
  "risk": { "sensitive_data": ["brand confidential","client PII"], "regulations": ["personal data law"], "llm_retention_acceptance": "30d" },
  "deployment": { "preference": "Hybrid", "vendor_acceptance": ["OpenAI","Anthropic","Google"] },
  "course": { "l1_headcount": 120, "seed_team_headcount": 14, "objectives": ["workflow automation","Agent building"] },
  "budget": { "annual_bucket": "2M-10M", "kickoff": "1-3 months", "first_poc": "1-3 months" }
}
```

## 3. Recommended Course Mix

| Level | Ratio | Focus |
| ---: | ---: | --- |
| L1 | 35% | Org-wide OpenWebUI, AI usage policy, Brand Safety, brand / client data boundaries |
| L2 | 35% | Creative / Account / Media-Buy Skill Library; Antigravity for ETL and reporting |
| L3 | 20% | Report automation, social-listening Workflow, client monthly-report Pipeline |
| L4 | 8% | Client Onboarding Briefing Agent |
| L5 | 2% | Cross-functional Agent Team (campaign launch: Strategy + Copy + Design + Media-Buy + Report + Reviewer) |

Rationale: L1 governance is at zero and must be filled first; L2 Skills are the biggest lever for a marketing agency (massive content reuse); L3 connects GA4 / Ads / Meta APIs; L4-L5 are later phases.

## 4. In-Class Artifacts

### L1 OpenWebUI (4 weeks)

- 120 accounts provisioned + groups (Strategy / Account / Creative / Media / Data / Prod / Admin) + role matrix
- AI usage policy v1 (incl. the red line "do not provide unpublished client material to the LLM")
- 27 Brand Safety prompt templates (one per client)
- Prompt Library, 36 entries (deck drafts, campaign naming, social copy, report narrative...)
- Model visibility: sensitive brand-client data → Azure OpenAI; public material → cloud OpenAI

### L2 Skill AI (6 weeks)

13 Skills live:

| # | Skill | Owner | L-target |
| --- | --- | --- | --- |
| 1 | Brand Tone-of-Voice writing (per client) | Creative Lead | L2 |
| 2 | Social short-post batch (FB / IG / Threads / X) | Social Manager | L2 |
| 3 | Ad-creative brief→hook proposal | Copy Lead | L2 |
| 4 | Monthly GA4 + Meta + Google Ads report narrative | Data Lead | L2 |
| 5 | Client campaign recap draft | Account Lead | L2 |
| 6 | KOL list research and outreach-email draft | PR Lead | L2 |
| 7 | Internal meeting recording → action list | Account Lead | L2 |
| 8 | Client report cover / structure draft | Account Lead | L2 |
| 9 | Competitor social-listening summary | Strategy Lead | L2 |
| 10 | Proposal draft (RFP response) | Strategy Lead | L2 |
| 11 | Shoot brief structuring | Production Lead | L2 |
| 12 | Asana task ↔ Notion two-way conversion | Ops | L2 |
| 13 | Internal new-hire onboarding Q&A (RAG over Notion) | HR | L2 |

Each Skill has IPOE + ≥ 3 test cases + Owner + version (GitHub backup).

### L3 n8n Workflow (6 weeks)

5 Workflow PoCs:

1. **Client monthly-report Pipeline** — Schedule → GA4/Ads API → Sheets → Skill #4 → Notion monthly-report draft → Account review → send
2. **Social-listening Workflow** — Schedule 4 hr → social search API → Skill #9 → Slack notification to Strategy
3. **New-client RFP intake classification** — Gmail Trigger → OpenAI Chat → route to the matching Strategy + Notion task
4. **Shoot brief → production task breakdown** — Notion Trigger → Skill #11 → Asana batch create
5. **Weekly client Pulse Check** — Schedule → HubSpot + GA4 → AI digest → client Slack channel

Each Workflow includes Sub-workflows, Data Tables, GitHub Backup, Error DLQ.

### L4 Hermes Agent (4 weeks)

**Client Onboarding Agent** — activated after a new client signs:
- Wiki: industry, past collaboration, brand style, social sentiment, competitors
- Skills: #1, #6, #9, #10 above
- Workflows: monthly-report Pipeline, social listening
- Task card: within 7 days of new-client onboarding, produce a "client brief document + first campaign draft"
- Reviewer: Account Director
- Gates 4A-4E all passed

### L5 ClawTeam Exercise (2 weeks)

**New-product launch Agent Team** (based on HKUDS/ClawTeam, MIT):
- Strategy Agent (market positioning)
- Copy Agent (key-visual copy / social copy)
- Design Brief Agent (creative brief for designers)
- Media-Buy Agent (media plan draft)
- Report Agent (auto weekly recap after the campaign)
- Reviewer Agent (Brand Safety + compliance)
- Integration: Account Director as the Human Gate

Actual scenario: for one client's new-product launch, the past 14-day process was compressed to 5 days.

## 5. Eight-Stage Analysis

### Stage 1 Current-State Discovery
- Interviews: CEO, 3 Account Directors, Creative Lead, Data Lead, 1 IT, 3 front-line employees
- Pain density concentrated: client reporting (90% of departments), proposal RFPs (Strategy), social production (Creative)

### Stage 2 Vision Alignment
- CEO vision: within 18 months, compress 27 brand-client onboarding to 3 days (currently 14); proposal win rate 30%→45%
- Stakeholder RACI signed; CMO is the Sponsor, Strategy Director is the AI Champion

### Stage 3 Industry Benchmark
- International benchmarks: WPP / Publicis AI lab (too large); local: no clear AI leader
- Reference architecture: self-built (OpenWebUI + n8n + HubSpot)

### Stage 4 Gap Analysis

Missing/Broken/Redundant:
- **Missing:** Skill Library, Audit Log, Brand Safety prompt matrix, client-data boundary policy
- **Broken:** client monthly-report production process (6-8 hr per client)
- **Redundant:** deck templates (each Account has their own set)

Impact × Effort:
- Quick Win: client monthly-report Pipeline (L3-W1)
- Big Bet: Onboarding Agent (L4)
- Avoid: a self-built chatbot (not a current priority)

### Stage 5 Executive Problem Statement

```
CONTEXT: In the past 12 months, 3 competitors have claimed to be "AI-first agencies"; some
         clients are asking about our AI strategy. Without a response, an estimated NT$ 24M
         of contracts will be lost within 6 months.
TENSION: Employees use AI daily but the organization has zero capability (L1); monthly-report
         production at 6-8 hr drags down delivery.
COI:     If no action for 12 months: (1) NT$ 24M contract loss (2) NT$ 6M Creative recruiting cost.
DESIRED: Reach L4 in 12 months; client monthly report < 2 hr; onboarding < 3 days; proposal
         win rate +50%.
CONSTRAINT: NT$ 4.8M budget; CMO as Sponsor; must not disrupt the current delivery rhythm.
```

### Stage 6 Roadmap

| Phase | Month | Main deliverables | Stage Gate | KPI |
| --- | --- | --- | --- | --- |
| 1 | 1-2 | L1 OpenWebUI + policy | Gate 1 ✓ | weekly employee usage ≥ 80% |
| 2 | 3-4 | L2 13 Skills | Gate 2 ✓ | Skill Library ≥ 13 |
| 3 | 5-6 | L3 5 Workflows | Gate 3 ✓ | client monthly report < 2 hr |
| 4 | 7-9 | L4 Onboarding Agent | Gate 4 ✓ | onboarding < 3 days |
| 5 | 10-12 | L5 new-product launch Team | Gate 5 ✓ | new-product launch process ≤ 5 days |

### Stage 7 Solution Architecture

- Variant: **Hybrid**
- Cloud: OpenAI for public material; Azure OpenAI isolated tenant for sensitive client data
- On-prem: n8n self-host on AWS (avoid shared nodes)
- Notion as Wiki + Knowledge Base
- HubSpot as CRM; OAuth + Webhook + n8n integration

### Stage 8 Governance & ROI

- Permissions: Creative / Account / Media groups each see different models; Audit Log retained 1 year
- ROI Tracker: client monthly-report hours, onboarding days, proposal win rate, new-product launch days, employee NPS

## 6. Diagnostic Report Summary

> **Core finding:** Agency M's AI adoption is employee-driven (L1+, high shadow IT), with zero organizational capability (L0). Recommend completing the L1→L4 build-out within 12 months to avoid falling further behind competitors.
>
> **Recommended investment:** NT$ 4.8M (training NT$ 2.8M + platform NT$ 0.8M + consulting NT$ 1.2M).
>
> **Expected ROI:** quantifiable benefit of NT$ 18M over 12 months (time savings 12M + contract-loss protection 6M), ROI ≈ 275%.

## 7. 30/60/90-Day Roadmap

### 30 days
- L1 OpenWebUI 120 accounts live
- AI usage policy v1, signing rate ≥ 90%
- Brand Safety prompts × 27 complete
- 5 quick-win Skills live (#1, #2, #4, #7, #12)
- Gate 1 passed

### 60 days
- Skill Library, 13 complete
- Client monthly-report Pipeline Workflow live; first tried with 3 clients
- Antigravity artifacts complete
- Gate 2 passed

### 90 days
- All 5 Workflows live
- Client monthly report covers all 27 clients
- Client monthly-report hours 6-8 hr → 1.5 hr
- Gate 3 passed
- L4 Onboarding Agent planning kicked off

## 8. ROI Projection

| Initiative | Baseline | 12-month Target | NT$ impact |
| --- | --- | --- | --- |
| Client monthly-report production hours | 6-8 hr × 27 clients × 12 months | 1.5 hr | NT$ 5.4M / year |
| Onboarding days | 14 days | 3 days | NT$ 3.6M / year (Account freed up) |
| New-product launch process | 14 days | 5 days | NT$ 2.0M / year |
| Proposal win rate | 30% | 45% | NT$ 4.8M / year (new business) |
| Creative rework rate | 25% | 12% | NT$ 1.8M / year |
| Risk (contract-loss protection) | - | - | NT$ 6.0M |
| **Subtotal** | | | **NT$ 23.6M** |
| **Less investment** | | | **-4.8M** |
| **Net benefit** | | | **NT$ 18.8M / year** |

## 9. Risks & Governance

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Employees send unpublished client material to a cloud LLM | High | High | L1 policy + Brand Safety prompt + Audit log + DLP |
| AI copy misuses brand terms | High | Medium | Brand Safety Skill + Reviewer + client sign-off |
| Client confidential data leakage | Medium | Critical | Azure OpenAI tenant isolation; sensitive data on-prem |
| Employee resistance (fear of replacement) | Medium | Medium | L1 org-wide taster; CEO publicly commits to no layoffs |
| Budget overrun | Medium | Medium | monthly ROI Gate; pause if a Stage Gate fails |

## 10. Outcome Summary

After 12 months (hypothetical projection):
- Advanced from L1 to L4
- All 27 clients' monthly reports fully automated
- The Onboarding Agent has onboarded 12 new clients
- One ClawTeam has completed 3 new-product launches
- The CMO is promoted to group AI Lead; new business of NT$ 48M won

References: full PoC scenarios `02_Course_Design/POC_SCENARIO_SPECS.md`; industry recommendations `INDUSTRY_SCENARIOS.md`; consulting toolkit `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`.
