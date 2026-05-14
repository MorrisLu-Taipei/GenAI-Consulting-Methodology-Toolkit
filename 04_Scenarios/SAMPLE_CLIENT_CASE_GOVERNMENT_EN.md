# Sample Client Case: Government Agency

> 🌐 中文版本 / Chinese version: [SAMPLE_CLIENT_CASE_GOVERNMENT.md](SAMPLE_CLIENT_CASE_GOVERNMENT.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>
>
> **Sample case for illustration. The client is referred to by the code "City Digital Bureau G" (not a real agency name). Content is synthesized from multiple real public-sector engagements; numbers are illustrative.**

---

## 1. Client Profile

| Field | Content |
| --- | --- |
| Agency code | City Digital Bureau G (coordinates 22 city departments, anonymized) |
| Nature | Municipal government's digital-transformation coordination unit |
| Population covered | 5,000 city-government employees (this project pilots 3 departments, 800 people) |
| Starting L-level | L1 (marginal) |
| Budget | NT$ 18M (24 months, budgeted by fiscal year) |
| Regulation | Personal data law, Freedom of Government Information Law, agency document-system rules, Cybersecurity Management Act |
| Main pain points | (1) High document-processing volume (2) Many repeated citizen-service 1999 Q&A (3) Knowledge does not flow across departments (4) Lengthy procurement procedures |

## 2. Engagement Onboarding & Diagnostic

### 2.1 10-Question Quick Survey Results

Average **0.8 → L1**. Tool usage Q1=1 (civil servants' private use is restricted), governance Q6=1, next step Q8=1 (no AI Champion).

### 2.2 25-Question Six Constructs

| Construct | Average |
| --- | ---: |
| Tool usage | 1.2 |
| Knowledge codification | 1.5 (document-filing culture) |
| Process standardization | 2.5 (rigorous regulatory processes) |
| System integration | 1.0 |
| Agent application | 0.2 |
| Governance & ROI | 1.3 |

**Insight:** process standardization is highest (regulation-driven), but tools and integration are low. The public-sector adoption pattern — slow procurement, hard cross-department coordination, but once a benchmark is established it can be rolled out city-wide.

### 2.3 Company Profile Bundle (key points)

```json
{
  "profile": {"industry":"government","headcount_bucket":"5000+"},
  "systems": {"document":"document system (self-built)","wiki":["SharePoint"],"citizen_service":"1999 system","erp":"accounting system"},
  "risk": {"sensitive_data":["citizen PII","official documents","procurement"],"regulations":["personal data law","Freedom of Government Information Law","Cybersecurity Management Act"],"llm_retention_acceptance":"reject"},
  "deployment": {"preference":"fully on-prem","gpu_capacity":"none (procurement needed)","local_llm_plan":"yes"},
  "course": {"l1_headcount":800,"seed_team_headcount":24,"objectives":["workflow automation","governance establishment"]},
  "budget": {"annual_bucket":"10M+","kickoff":">6 months"}
}
```

## 3. Recommended Course Mix

| Level | Ratio | Focus |
| ---: | ---: | --- |
| L1 | 45% | Org-wide for the 3 pilot departments; on-prem deployment; official-document / citizen-data red lines; civil-servant AI usage policy |
| L2 | 25% | Document / 1999 / procurement Skills |
| L3 | 22% | Document summary, citizen FAQ, cross-department knowledge Q&A Workflows |
| L4 | 8% | Citizen-service Agent (pilot, the 1999 scenario) |
| L5 | 0% | Not adopted |

Rationale: the public sector has the highest governance threshold (personal data + freedom-of-information + cybersecurity laws), so L1 must be 45%. Procurement cycles are long, so on-prem infrastructure needs to be planned early.

## 4. In-Class Artifacts

### L1 OpenWebUI (12 weeks, phased by department)

- 800 accounts (3 pilot departments: Civil Affairs, Social Affairs, Research & Evaluation)
- **Fully on-prem deployment:** government machine room + Llama 70B + on-prem embedding
- Civil-servant AI usage policy (benchmarked against personal data + freedom-of-information laws)
- Model visibility: tiered by department and rank
- Prompt Library, 38 entries (all pre-reviewed by Government Ethics + Legal)
- Audit Log: meets the audit requirements of the Cybersecurity Management Act

### L2 Skill AI (10 weeks)

10 Skills:

| # | Skill | Owner |
| --- | --- | --- |
| 1 | Document summary and routing recommendation | Document Section |
| 2 | Document first-draft drafting (standard types) | Each section |
| 3 | Citizen 1999 case classification | 1999 Center |
| 4 | Citizen petition reply draft | Each department |
| 5 | Plain-language explanation of regulation clauses | Legal Affairs |
| 6 | Procurement specification drafting assistance | Procurement |
| 7 | Cross-department knowledge Q&A (RAG) | Research & Evaluation |
| 8 | Meeting notes and resolution tracking | Secretariat |
| 9 | New civil-servant onboarding Q&A | Personnel |
| 10 | Statistical-report narrative drafting | Accounting |

### L3 n8n Workflow (10 weeks)

4 Workflow PoCs (all on-prem):

1. **Document summary Pipeline** — document system → Skill #1 → handler review queue
2. **1999 case triage** — 1999 system → Skill #3 → route to each department + priority
3. **Cross-department knowledge Q&A** — employee asks → RAG over SharePoint + public data → answer + sources
4. **Citizen petition reply assistance** — petition case → Skill #4 → handler review

### L4 Hermes Agent (6 weeks)

**Citizen-Service Agent (1999 pilot):**
- Wiki: city-government FAQ, each department's functions, common petition types, handling SOPs
- Skills: #3, #4
- Task card: a 1999 case arrives → the Agent classifies + drafts a preliminary reply + flags the parts needing human input
- **Reviewer: the 1999 Center supervisor signs off**
- Evidence: 100% source traceability
- Gates 4A-4E + an additional Gate 4G (Government Ethics + Legal signature)

### L5 ClawTeam

**Not adopted.**

## 5. Eight-Stage Analysis

### Stage 1 Current-State Discovery
- Interviews: Director-General of the Digital Bureau, Chair of Research & Evaluation, 3 department directors, Document Section, 1999 Center, Government Ethics, Legal Affairs
- Pain density: documents (22 departments, 100%), repeated 1999 Q&A (1999 Center 100%), cross-department knowledge (Research & Evaluation 90%)

### Stage 2 Vision Alignment
- Director-General vision: within 24 months, document-processing time -40%, 1999 first-line resolution rate +30%, establish a replicable city-wide benchmark
- Sponsor = Director-General of the Digital Bureau + Chair of Research & Evaluation

### Stage 3 Industry Benchmark
- International: Singapore GovTech, Estonia e-Estonia (vision reference); Taiwan: relevant PoCs at the Ministry of Digital Affairs
- Self-built fully on-prem, benchmarked against the personal data + Cybersecurity Management acts

### Stage 4 Gap Analysis

Missing/Broken/Redundant:
- **Missing:** AI governance policy, on-prem infrastructure, an AI Champion position, Skill Library
- **Broken:** documents read word-by-word manually (15-30 min each); repeated 1999 Q&A (40% of cases can be standardized)
- **Redundant:** the 22 departments' knowledge is scattered (no unified search)

Impact × Effort:
- Quick Win: cross-department knowledge Q&A (L3-W3); 1999 triage (L3-W2)
- Big Bet: document summary Pipeline (L3-W1, needs document-system integration)
- Avoid: an open-ended citizen-facing AI chatbot (information-accuracy risk)

### Stage 5 Executive Problem Statement

```
CONTEXT: The Ministry of Digital Affairs is promoting public-sector AI applications; citizens'
         expectations of city-service speed are rising; document volume grows 8% per year, with
         a hiring freeze.
TENSION: Regulatory processes are rigorous (L2.5) but there are no AI tools; knowledge does not
         flow across departments.
COI: If no action for 24 months: (1) document backlog worsens (2) 1999 satisfaction declines
     (3) falling behind other counties' / cities' benchmarks.
DESIRED: In 24 months, the 3 pilot departments reach L3-L4; document processing -40%; 1999
         first-line resolution +30%; produce a city-wide-replicable model.
CONSTRAINT: Budget allocated by fiscal year; fully on-prem; long procurement cycles; every
            application requires triple Government-Ethics + Legal + Security review; phased
            rollout by department.
```

### Stage 6 Roadmap

| Phase | Month | Main deliverables | Gate | KPI |
| --- | --- | --- | --- | --- |
| 1 | 1-6 | Procurement + on-prem infrastructure + AI governance policy | Pre-Gate | machine room ready, policy passes triple review |
| 2 | 7-12 | L1 for the 3 pilot departments, 800 people | Gate 1 | weekly employee usage ≥ 60% |
| 3 | 13-18 | L2 10 Skills + L3 4 Workflows | Gate 2+3 | document processing -40% |
| 4 | 19-24 | L4 Citizen-Service Agent + city-wide rollout plan | Gate 4+4G | 1999 first-line resolution +30% |

### Stage 7 Solution Architecture

- **Variant C, fully on-prem:** government machine room + Llama 70B + Qdrant; zero cloud
- Integrates the document system, 1999 system, SharePoint (all on the intranet)

### Stage 8 Governance & ROI

- Permissions: tiered by department + rank; official documents / citizen data graded
- Audit: meets the Cybersecurity Management Act; auditable by Government Ethics
- Triple-review process: co-signed by Government Ethics + Legal + Security
- ROI Tracker: document-processing time, 1999 resolution rate, cross-department Q&A usage rate, citizen satisfaction

## 6. Diagnostic Report Summary

> **Core finding:** City Digital Bureau G has mature process standardization (L2.5) but a gap in AI tools (L1). The public-sector adoption pattern — long procurement and triple-review cycles, but once a benchmark is established it can be replicated across all 22 departments. Recommend piloting 3 departments to L3-L4 over 24 months, with the focus on a replicable model.
>
> **Expected ROI:** pilot benefit of NT$ 62M over 24 months; estimated annualized benefit of NT$ 280M after city-wide rollout.

## 7. 30/60/90-Day Roadmap

### 30 days
- On-prem machine-room procurement specification (procurement process kicked off)
- AI governance policy draft (Government Ethics + Legal + Security)
- 3 pilot departments confirmed + AI Champion assigned

### 60 days
- Procurement evaluation work
- AI governance policy triple review
- L1 course material localization (public-sector scenarios)

### 90 days
- Machine-room construction kicked off
- AI governance policy approved
- L1 Wave 1 (Civil Affairs Department) preparation

## 8. ROI Projection (3 pilot departments, 24 months)

| Initiative | Baseline | Target | NT$ impact |
| --- | --- | --- | --- |
| Document-processing time | 15-30 min/item | -40% | NT$ 24M/year (staff freed up) |
| 1999 first-line resolution rate | 55% | 85% | NT$ 18M/year |
| Cross-department knowledge lookup | manual inquiry | unified search | NT$ 12M/year |
| Procurement specification drafting | slow | -50% | NT$ 8M/year |
| **Pilot subtotal (annualized)** | | | **NT$ 62M** |
| **Less investment** | | | **-18M** |
| **Pilot net benefit** | | | **NT$ 44M/year** |
| After city-wide rollout to 22 departments | - | - | estimated annualized NT$ 280M |

## 9. Risks & Governance

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Citizen personal data leakage | Low (on-prem) | Critical | fully on-prem, zero cloud, Audit |
| AI document errors causing administrative faults | Medium | High | mandatory handler review; the Agent is assistive only |
| Procurement-process delays | High | Medium | start 6 months early; budget by fiscal year |
| Difficulty coordinating across departments | High | Medium | Director-General + Research & Evaluation dual sponsor; pilot demonstration |
| Civil-servant resistance / union concerns | Medium | Medium | no-layoff commitment; positioned as "workload reduction" not "replacement" |
| Continuity affected by changes of administration | Medium | High | institutionalize as a permanent policy; document benchmark results |

## 10. Outcome Summary

After 24 months:
- The 3 pilot departments advance from L1 to L3-L4
- Document-processing time -40%; 1999 first-line resolution rate 55% → 85%
- A "City Government AI Adoption Standard Operating Model" is produced, replicable for the 22 departments
- The Digital Bureau becomes a visit benchmark for other counties / cities
- The AI governance policy is incorporated into the city government's permanent rules

References: full PoC `02_Course_Design/POC_SCENARIO_SPECS.md`; industry `INDUSTRY_SCENARIOS.md`; consulting toolkit `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`.
