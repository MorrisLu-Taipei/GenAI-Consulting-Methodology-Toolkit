# AI Governance Alignment: Tiger AI Methodology vs International AI Governance Frameworks

> 🌐 中文版本 / Chinese version: [AI_GOVERNANCE_ALIGNMENT.md](AI_GOVERNANCE_ALIGNMENT.md)
>
> Apache License 2.0 · Author: Morris Lu · Tiger AI

Last updated: 2026-05-16

---

> **What this answers**: How does Tiger AI methodology map to international AI governance frameworks (NIST AI RMF / EU AI Act / ISO/IEC 42001 / OECD AI Principles / Taiwan AI Basic Act / Singapore Model AI Governance)? Boards / compliance / regulators need specific landing points in each framework.
>
> BPM / consulting / AI-maturity alignments are in [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md). **This doc focuses on AI Governance**, especially L4-L5 institutional credibility.

---

## 1. Why L4-L5 Needs Formal AI Governance Alignment

L4 Autonomous Agent + L5 Multi-Agent Organization = AI executing business actions without real-time human supervision.

Boards / regulators ask three mandatory questions:

1. **Who bears liability**? Who's legally / ethically responsible when AI fails?
2. **What early-warning mechanism**? What triggers human intervention for high-risk decisions?
3. **How is it audited**? Can third parties independently verify AI behavior?

The answers must map to **internationally recognized governance frameworks** to be acceptable to boards, compliance, regulators.

---

## 2. Eight Stages × Mainstream AI Governance Frameworks

| Governance Framework | Source / Nature | Tiger AI Stages Covered |
| --- | --- | --- |
| **NIST AI RMF** | US NIST, 2023 / voluntary but widely adopted | Govern→Stage 8; Map→Stage 1-2; Measure→Stage 4+8; Manage→Stage 6-8 |
| **EU AI Act** | EU, 2024 / mandatory regulation | High-risk AI maps to L4-L5; transparency→Stage 8 Audit; HITL→all stages |
| **ISO/IEC 42001:2023 AI Management System** | ISO, 2023 / certifiable | AI policy→Stage 8; risk→Stage 4+8; continuous improvement→Phase C |
| **ISO/IEC 23894:2023 AI Risk Management** | ISO / risk focus | Risk Register→Stage 8 |
| **OECD AI Principles** | OECD+members / policy principles | 5 principles → Tool 7.2 + 8.8 |
| **Taiwan AI Basic Act (draft)** | Taiwan Legislative Yuan, in review | Maps to Taiwan high-compliance clients |
| **Singapore Model AI Governance Framework** | IMDA / voluntary | 4 pillars → Stage 7 To-Be + Stage 8 |
| **US AI Bill of Rights** | White House / policy statement | 5 protections → Tool 8.8 Ethics + client data protection |

---

## 3. NIST AI RMF (Most Important Global Reference)

NIST AI RMF is the **most widely adopted** AI governance framework. 4 core functions:

### 3.1 Govern

**NIST requires**: org-level AI policy, roles, responsibilities, culture.

**Tiger AI**: Stage 8 §12.1 RACI matrix; Tool 8.8 AI Ethics Checklist 15 items; 4-layer architecture Layer 1 Governance (Policy / Ethics / Compliance / Risk Committee / Audit Owner); Tool 3.6 client 3-party signature = corporate-level written commitment.

### 3.2 Map

**NIST requires**: inventory of AI system context, risks, stakeholders.

**Tiger AI**: Stage 1 As-Is (interviews, Systems Inventory, AI Usage Inventory, Swimlane); Tool 2.2 RM Mapping; Tool 2.6 + 2.7 Component Map + 4-layer.

### 3.3 Measure

**NIST requires**: quantify AI system performance, impact, risk.

**Tiger AI**: Stage 2 radar 0-4 scoring; Stage 4 Impact × Effort; Stage 8 Tool 8.5 Value Tracking Matrix (5 dimensions); Tool 8.9 Evidence Hierarchy (L1-L5 evidence strength); quarterly Gate C radar revisit.

### 3.4 Manage

**NIST requires**: risk mitigation, monitoring, continuous improvement.

**Tiger AI**: Stage 6 Phased Goals + Stage Gate Criteria; Stage 7 Human-AI Collaboration + HITL nodes; Stage 8 Tool 8.6 Risk Register; Tool 8.7 Audit Log; Phase C 24-month quarterly review.

> **Overall**: NIST AI RMF 4 functions fully land in Tiger AI 8 stages, **producing NIST compliance documents directly**.

---

## 4. EU AI Act (Mandatory Regulation)

EU AI Act classifies AI into 4 risk tiers: Unacceptable / High-risk / Limited / Minimal.

### 4.1 Risk Classification Mapping

| EU AI Act Tier | Tiger AI L-level | Governance Required |
| --- | --- | --- |
| **Unacceptable** (social scoring, real-time biometric ID, etc.) | ❌ Tiger AI **refuses to assist** | — |
| **High-risk** (HR, credit, medical, education, judicial, critical infrastructure) | Mostly L4-L5 scenarios | Mandatory risk assessment + transparency + human oversight + post-market monitoring |
| **Limited** (chatbots, deepfake) | Mostly L1-L3 scenarios | Transparency obligations (mark "AI-generated") |
| **Minimal** (spam filtering, etc.) | Mostly L1-L2 scenarios | General obligations |

### 4.2 High-Risk AI Article Alignment

| EU AI Act Article | Tiger AI Mapping |
| --- | --- |
| **Art. 9 Risk Management System** | Stage 8 Tool 8.6 Risk Register |
| **Art. 10 Data Governance** | Tool 8.7 Audit Log + Tool 8.4 Permission Matrix |
| **Art. 11 Technical Documentation** | Full 14-section consulting report + 4-layer architecture docs |
| **Art. 12 Record-Keeping (logs)** | Tool 8.7 Audit Log 7 event types |
| **Art. 13 Transparency** | Tool 8.8 "AI-generated marking" + public Ideal Practice signing |
| **Art. 14 Human Oversight** | Tool 7.2 Human-AI Collaboration + HITL nodes + Reviewer Workflow |
| **Art. 15 Accuracy, Robustness, Cybersecurity** | Stage 8 Tool 8.5 Value Tracking (quality dim) + Audit Log + Security |
| **Art. 17 Post-Market Monitoring** | Phase C quarterly Gate C + Stage 2 radar revisit + 5-dim value tracking longitudinal |
| **Art. 26 Quality Management System** | ISO/IEC 42001 alignment (see §5) |
| **Art. 72 Serious Incident Reporting** | Tool 8.8 Ethics §11 "AI system incident response" |

> **Clients with EU operations**: Tiger AI methodology deliverables (full 14-section report + governance docs) serve as EU AI Act compliance evidence package.

---

## 5. ISO/IEC 42001:2023 AI Management System

ISO 42001 is the first **third-party-certifiable** AI management system standard. Structure mirrors ISO 9001 / 27001.

### 5.1 ISO 42001 Section Mapping

| ISO 42001 Section | Tiger AI Mapping |
| --- | --- |
| **4. Context of the Organization** | Stage 1 As-Is + Stage 2 Reference Model |
| **5. Leadership** | Sponsor + AI Champion role definition (RACI) + AI Policy signing |
| **6. Planning** | Stage 5 Problem Definition + Stage 6 Phased Goals + Tool 6.3 Absorption |
| **7. Support** | Change Management Playbook + training plan + resource planning |
| **8. Operation** | Stage 7 To-Be Operating Model + Human-AI Collaboration + HITL |
| **9. Performance Evaluation** | Tool 8.5 Value Tracking Matrix + Tool 8.7 Audit Log + quarterly Gate C radar |
| **10. Improvement** | Phase C quarterly review + Cases-as-Benchmarks accumulation |
| **Annex A Controls** | Tool 8.4 Permission + Tool 8.6 Risk + Tool 8.7 Audit + Tool 8.8 Ethics |

> **Goal**: Enterprises pursuing ISO/IEC 42001 certification can use Tiger AI deliverables as management-system documentation. Tiger AI **fully covers all ISO 42001 sections**.

---

## 6. OECD AI Principles (5 Principles)

OECD AI Principles are broadly adopted by G20, APEC.

| OECD Principle | Tiger AI Mapping |
| --- | --- |
| **1. Inclusive growth, sustainable development and well-being** | Stage 8 Tool 8.5 Value Tracking includes "employee experience"; Change Management includes "upgrade roles, not replace" |
| **2. Human-centered values and fairness** | Tool 8.8 Ethics §9 bias / discrimination assessment; Tool 7.2 HITL mandatory |
| **3. Transparency and explainability** | Tool 8.7 Audit Log + Tool 8.8 §7 "AI-generated marking" + full evidence trail |
| **4. Robustness, security and safety** | Stage 8 Risk Register + Tool 8.4 Permission + deployment mode (Hybrid / On-Prem 3 options) |
| **5. Accountability** | RACI matrix + "**client-signed Ideal Practice 3-party signature**" + Reviewer sign-off |

---

## 7. Taiwan AI Basic Act (Draft)

Taiwan Legislative Yuan AI Basic Act in review (as of 2026/05). Tiger AI methodology **aligns with main provisions**:

| Draft Highlight | Tiger AI Mapping |
| --- | --- |
| **AI products/services need risk grading** | Stage 1-2 identification + 4-layer architecture + Tool 8.6 Risk Register |
| **PII protection over model training** | Tool 8.8 §2 PII not sent to LLM / redacted; deployment defaults to on-prem for high-sensitivity |
| **Algorithm transparency and explainability** | Tool 8.7 Audit Log + 8.8 §7 AI marking |
| **User rights protection** | Tool 8.8 §5 employees have right to know AI-processed work |
| **Operator accountability** | RACI + Tool 8.8 §8 IP attribution |
| **Government regulatory authority** | Tool 8.7 Audit Log retention supports government audit |

⚠️ Taiwan AI Basic Act not yet passed. This alignment will update with final text.

---

## 8. Singapore Model AI Governance Framework

Singapore IMDA voluntary framework, 4 pillars:

| Singapore Pillar | Tiger AI Mapping |
| --- | --- |
| **1. Internal Governance Structures** | Layer 1 Governance + RACI |
| **2. Determining Level of Human Involvement** | Tool 7.2 Human-AI Collaboration (HITL nodes) |
| **3. Operations Management** | Tool 8.4-8.7 full set (Permission / Value / Risk / Audit) |
| **4. Stakeholder Interaction & Communication** | Tool 8.2 Change Management Playbook + Stakeholder Map |

---

## 9. Regulatory / Compliance Deliverables Map

When clients face regulatory / compliance / internal audit, which Tiger AI deliverables can be directly submitted:

| Regulatory Need | Direct Tiger AI Deliverable |
| --- | --- |
| AI risk assessment | Stage 4 Gap + Tool 8.6 Risk Register |
| AI policy | Tool 8.8 Ethics Checklist 15 items + AI Policy doc |
| Audit evidence package | Tool 8.7 Audit Log + quarterly Gate C logs + Stage 2 radar before/after |
| 3rd-party audit prep | Full 14-section report + 4-layer architecture + 4 authoritative docs |
| ROI / benefit substantiation | Tool 8.5 Value Tracking 5 dimensions + longitudinal KPI |
| Incident response flow | Tool 8.8 §12 + Tool 8.6 Risk Register triggers |
| Employee training records | Change Management training records + Tool 8.8 §14 |

---

## 10. Certification / Labeling Recommendations

Based on methodology maturity, Tiger AI clients may consider:

| Certification | Applies to | Est. Timeline |
| --- | --- | --- |
| **ISO/IEC 42001 AI Management System** | L3+ clients (with full governance) | 6-12 months |
| **ISO/IEC 27001 ISMS** | All clients (security baseline) | 6-12 months |
| **SOC 2 Type II** | US / multinational service clients | 6-12 months |
| **EU AI Act CE Marking** (High-risk) | EU operations + High-risk AI systems | 12-24 months |

> Tiger AI deliverables serve as **90% of certification documentation base**. Actual certification requires third-party audit.

---

## 11. Related Documents

| Document | Relationship |
| --- | --- |
| [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | Aligns with consulting firms / BPM / AI maturity frameworks; this doc adds AI Governance |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Why methodology withstands debate |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | Methodology failure modes & counter-cases |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Stage 8 | Full governance toolkit |

---

## 12. References

- NIST (2023). *AI Risk Management Framework (AI RMF 1.0)*.
- European Commission (2024). *Regulation on Artificial Intelligence (EU AI Act)*.
- ISO/IEC (2023). *ISO/IEC 42001:2023 — AI Management System*.
- ISO/IEC (2023). *ISO/IEC 23894:2023 — AI Risk Management*.
- OECD (2019, updated 2024). *OECD AI Principles*.
- The White House (2022). *Blueprint for an AI Bill of Rights*.
- Singapore IMDA (2020). *Model AI Governance Framework, 2nd Edition*.
- 立法院 (in review). *Taiwan Artificial Intelligence Basic Act Draft*.

---

License & Citation

This document is Apache License 2.0; may be used, modified, commercialized, provided the [`../NOTICE`](../NOTICE) attribution is preserved.
