# Sample Client Case: Financial Services

> 🌐 中文版本 / Chinese version: [SAMPLE_CLIENT_CASE_FINANCIAL.md](SAMPLE_CLIENT_CASE_FINANCIAL.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **Sample case for illustration. The client is referred to by the code "Regional Bank F" (not a real company name). Content is synthesized from multiple real financial engagements; numbers are illustrative.**

---

## 1. Client Profile

| Field | Content |
| --- | --- |
| Client code | Regional Bank F (regional commercial bank, anonymized) |
| Industry | Regional commercial bank (consumer + corporate + wealth management) |
| Employees | 2,500 (branches 1,600 / HQ 700 / IT 200) |
| Branches | 68 |
| Starting L-level | L1 (HQ IT partially L2) |
| Budget | NT$ 24M (18 months) |
| Regulation | FSC, personal data law, anti-money-laundering law, ISO 27001 |
| Main pain points | (1) Slow KYC / credit-review document processing (2) Manual customer-service triage (3) Insufficient compliance-check coverage (4) Large knowledge gap across branches |

## 2. Engagement Onboarding & Diagnostic

### 2.1 10-Question Quick Survey Results

Average **0.9 → L1**. Tool usage Q1=2 (employees use it privately), governance Q6=1, risk Q10=2 (the financial industry has relatively strong IT discipline but a governance gap for AI).

### 2.2 25-Question Six Constructs

| Construct | Average |
| --- | ---: |
| Tool usage | 1.8 |
| Knowledge codification | 1.0 |
| Process standardization | 2.2 (strong SOP culture in finance) |
| System integration | 1.5 |
| Agent application | 0.3 |
| Governance & ROI | 1.6 |

**Insight:** process standardization scores high (SOP culture), but tools and Agents are low. The financial-industry adoption pattern — a high governance threshold, but once cleared, it spreads fast.

### 2.3 Company Profile Bundle (key points)

```json
{
  "profile": {"industry":"financial","headcount_bucket":"1000-5000"},
  "systems": {"core_banking":"self-built mainframe","crm":"self-built","erp":"SAP","wiki":["SharePoint"],"kyc":"third-party"},
  "risk": {"sensitive_data":["PII","financial","credit","transactions"],"regulations":["FSC","personal data law","AML law","ISO 27001"],"llm_retention_acceptance":"reject"},
  "deployment": {"preference":"fully on-prem","gpu_capacity":"H100 class","local_llm_plan":"yes"},
  "course": {"l1_headcount":2500,"seed_team_headcount":40,"objectives":["governance establishment","workflow automation"]},
  "budget": {"annual_bucket":"10M+","kickoff":"3-6 months"}
}
```

## 3. Recommended Course Mix

| Level | Ratio | Focus |
| ---: | ---: | --- |
| L1 | 40% | Org-wide enablement + **governance priority**; on-prem OpenWebUI; financial-data red lines; strict model-visibility control |
| L2 | 25% | Credit-review / compliance / customer-service Skills; mandatory Reviewer |
| L3 | 25% | KYC document summary, customer-service triage, compliance-check Workflows |
| L4 | 8% | Compliance assistant Agent (highly controlled) |
| L5 | 2% | Not adopted yet; concept explanation only |

Rationale: the financial industry has the highest governance threshold, so L1 must be 40% (on-prem deployment + permissions + Audit + compliance education). L5 is not adopted before the regulatory picture is clear.

## 4. In-Class Artifacts

### L1 OpenWebUI (8 weeks, phased)

- 2,500 accounts brought online in 6 waves (HQ first, then branches)
- **Fully on-prem deployment:** H100 machine room + Llama 70B + on-prem embedding, zero cloud LLM calls
- AI usage policy v1 (benchmarked against the FSC): customer data / credit / transaction data absolutely cannot enter any external service
- Model visibility: branch tellers can only use the "customer-service FAQ" model; credit review only the "document summary" model; HQ IT has full access
- Prompt Library, 45 entries (all pre-reviewed by Compliance)
- Audit Log: all LLM calls written in real time, retained 3 years

### L2 Skill AI (8 weeks)

12 Skills (each dual-reviewed by Compliance + Security):

| # | Skill | Owner | Note |
| --- | --- | --- | --- |
| 1 | KYC document key-point summary | Credit Review | no egress, on-prem |
| 2 | Credit-report drafting assistance | Corporate Banking | Reviewer mandatory |
| 3 | Complaint email classification | Customer Service | - |
| 4 | Compliance regulation-change summary | Compliance | government website RAG |
| 5 | Branch SOP Q&A | All branches | RAG over SharePoint |
| 6 | Wealth-product plain-language explanation | Wealth Management | must not constitute investment advice |
| 7 | Internal audit working-paper draft | Internal Audit | - |
| 8 | Customer 360 summary (internal use) | Branch managers | strict permissions |
| 9 | AML case initial-screening explanation | Compliance | assistive only, human decision |
| 10 | New-hire onboarding Q&A | HR | - |
| 11 | Meeting notes and action items | HQ departments | - |
| 12 | Credit-card complaint reply draft | Card Division | Reviewer mandatory |

### L3 n8n Workflow (10 weeks)

5 Workflow PoCs (all on-prem n8n, on-prem LLM):

1. **KYC document summary Pipeline** — document upload → OCR → Skill #1 → credit-reviewer review queue
2. **Customer-service email triage** — internal mailbox → Skill #3 → routing + priority
3. **Regulation-change monitoring** — Schedule → FSC / government websites → Skill #4 → Compliance Slack
4. **Branch knowledge Q&A** — branch employees ask → RAG over SharePoint → answer + sources
5. **Internal audit working-paper assistance** — audit item → historical working-paper RAG → Skill #7 → auditor review

### L4 Hermes Agent (6 weeks)

**Compliance Assistant Agent** (highly controlled):
- Wiki: regulation library, internal rules, historical penalty cases, FAQ
- Skills: #4, #9
- Task card: compliance staff query "is a scenario compliant" → the Agent gives "relevant regulations + internal rules + similar cases + flagged uncertainties"
- **Reviewer: the Compliance manager mandatorily signs off on every item**
- Evidence: 100% source traceability
- Gates 4A-4E + an additional Gate 4F (Chief Compliance Officer signature)

### L5 ClawTeam

**Not adopted** in this phase. Concept explanation only in the course, to be evaluated once the FSC's AI supervisory guidelines become clear.

## 5. Eight-Stage Analysis

### Stage 1 Current-State Discovery
- Interviews: General Manager, Chief Compliance Officer, CIO, Head of Credit Review, Head of Customer Service, 3 branch managers, Internal Audit
- Pain density: KYC / credit review (corporate banking 100%), customer-service triage (consumer banking 90%), compliance coverage (Compliance 100%)

### Stage 2 Vision Alignment
- GM vision: within 18 months, halve KYC processing time, 100% compliance-check coverage, no AI-related penalties
- Sponsor = CIO + Chief Compliance Officer (dual sponsor, a financial-industry characteristic)

### Stage 3 Industry Benchmark
- International: DBS / HSBC AI labs (large scale gap); Taiwan: a few financial holding groups in PoC
- Self-built fully on-prem, benchmarked against the FSC's "Guidelines on the Use of AI by Financial Institutions"

### Stage 4 Gap Analysis

Missing/Broken/Redundant:
- **Missing:** AI governance framework, Skill Library, on-prem LLM infrastructure, audit mechanism
- **Broken:** KYC documents read page-by-page manually (40-60 min each)
- **Redundant:** each of the 68 branches has its own way of doing SOP Q&A (no unified knowledge base)

Impact × Effort:
- Quick Win: branch knowledge Q&A (L3-W4); customer-service triage (L3-W2)
- Big Bet: KYC Pipeline (L3-W1, needs OCR + on-prem LLM)
- Avoid: a consumer-facing AI chatbot (high regulatory risk, not done currently)

### Stage 5 Executive Problem Statement

```
CONTEXT: The FSC issued AI guidelines for financial institutions in 2025; peers have launched
         AI PoCs. Regional Bank F's KYC processing speed lags peers; corporate clients complain
         about slow account opening / credit review; compliance staffing is insufficient at only
         70% coverage.
TENSION: Process SOPs are mature (L2.5) but there are no AI tools; the 2,500 employees have a
         large knowledge gap.
COI: If no action for 18 months: (1) estimated NT$ 80M corporate-client loss (2) penalty risk
     from insufficient compliance coverage.
DESIRED: Reach L4 in 18 months; KYC processing -50%; compliance coverage 100%; zero AI-related
         penalties.
CONSTRAINT: NT$ 24M budget; fully on-prem, zero cloud LLM; every AI application requires dual
            Compliance + Security review; phased rollout.
```

### Stage 6 Roadmap

| Phase | Month | Main deliverables | Gate | KPI |
| --- | --- | --- | --- | --- |
| 1 | 1-3 | On-prem infrastructure + AI governance framework | Pre-Gate | H100 machine room ready, governance framework signed by Compliance |
| 2 | 4-7 | L1 org-wide (6 waves) | Gate 1 | weekly employee usage ≥ 70% |
| 3 | 8-11 | L2 12 Skills | Gate 2 | Skill Library ≥ 12, all dual-reviewed |
| 4 | 12-15 | L3 5 Workflows | Gate 3 | KYC processing -50% |
| 5 | 16-18 | L4 Compliance Assistant Agent | Gate 4 + 4F | compliance coverage 100% |

### Stage 7 Solution Architecture

- **Variant C, fully on-prem:**
  - OpenWebUI Local + n8n Local + Hermes Local
  - Llama 70B + bge-m3 embedding (4× H100)
  - Qdrant vector store (on-prem)
  - Zero cloud LLM calls, compliant with the FSC guidelines

### Stage 8 Governance & ROI

- Permissions: five tiers — teller / credit review / compliance / internal audit / IT; dual model-level + data-level ACL
- Audit: all LLM calls 3 years; compliance-related permanent
- Dual-review process: every Skill / Workflow / Agent is co-signed by Compliance + Security before going live
- ROI Tracker: KYC time, compliance coverage rate, customer-service triage accuracy, branch knowledge Q&A usage rate

## 6. Diagnostic Report Summary

> **Core finding:** Regional Bank F has mature process SOPs (L2) but a gap in AI tools and governance (L1). The financial-industry characteristic — a high adoption threshold (requires fully on-prem + dual review), but once the framework is established it spreads fast. Recommend advancing to L4 in 18 months, with the governance framework going first.
>
> **Expected ROI:** quantifiable benefit of NT$ 110M over 18 months, ROI ≈ 358%.

## 7. 30/60/90-Day Roadmap

### 30 days
- On-prem H100 machine-room planning + procurement kickoff
- AI governance framework draft (Compliance + Security + IT, three-party)
- L1 course material localization (financial scenarios)

### 60 days
- H100 machine room ready, Llama 70B deployment test
- AI governance framework signed by the Chief Compliance Officer
- L1 Wave 1 (HQ, 200 people) live
- Pre-Gate passed

### 90 days
- L1 Waves 2-3 (rest of HQ + first batch of branches)
- 3 quick-win Skills pass dual review
- Gate 1 evaluation kicked off

## 8. ROI Projection

| Initiative | Baseline | 18-month Target | NT$ impact |
| --- | --- | --- | --- |
| KYC / credit-review document processing | 40-60 min/item | 20 min | NT$ 32M/year (credit-review staff freed up) |
| Compliance coverage rate | 70% | 100% | NT$ 40M (penalty-risk protection) |
| Customer-service triage | manual | AI-assisted | NT$ 18M/year |
| Branch knowledge gap | high | unified knowledge base | NT$ 12M/year (errors + training cost) |
| Corporate-client loss protection | - | - | NT$ 80M (one-time risk) |
| **Subtotal (annualized + risk)** | | | **NT$ 182M** |
| **Less investment** | | | **-24M** |
| **Net benefit** | | | **NT$ 158M** |

## 9. Risks & Governance

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Customer / transaction data leakage | Low (on-prem) | Critical | fully on-prem, zero cloud, Audit, DLP |
| AI constituting an investment-advice violation | Medium | Critical | strict limits on the wealth-product Skill; Reviewer; Compliance review |
| Compliance Assistant Agent misjudgment | Medium | High | 100% human sign-off; the Agent is assistive only |
| FSC supervisory changes | Medium | High | Compliance tracks continuously; L5 deferred |
| Branch employee resistance | Medium | Medium | phased; branch managers lead; no-layoff commitment |
| Insufficient on-prem LLM performance | Medium | Medium | 4× H100; upgrade if needed; non-real-time scenarios prioritized |

## 10. Outcome Summary

After 18 months:
- Advanced from L1 to L4 (Compliance Assistant Agent live)
- KYC processing time halved; compliance coverage 100%
- Zero AI-related penalties
- The fully on-prem architecture becomes a peer-visit benchmark
- An "AI Governance Committee" jointly led by the CIO + Chief Compliance Officer is made permanent

References: full PoC `02_Course_Design/POC_SCENARIO_SPECS.md`; industry `INDUSTRY_SCENARIOS.md`; consulting toolkit `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`.
