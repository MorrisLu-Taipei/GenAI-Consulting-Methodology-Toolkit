# AI Governance Alignment: Tiger AI Methodik vs. internationale AI Governance Frameworks

> 🌐 Sprache: [繁體中文](AI_GOVERNANCE_ALIGNMENT.md) ｜ [English](AI_GOVERNANCE_ALIGNMENT_EN.md) ｜ Deutsch ｜ [Français](AI_GOVERNANCE_ALIGNMENT_FR.md) ｜ [Español](AI_GOVERNANCE_ALIGNMENT_ES.md) ｜ [日本語](AI_GOVERNANCE_ALIGNMENT_JA.md) ｜ [한국어](AI_GOVERNANCE_ALIGNMENT_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Letzte Aktualisierung: 2026-05-16

---

> **Was dieses Dokument beantwortet**: Wie mappt die Tiger AI Methodik auf internationale AI Governance Frameworks (NIST AI RMF / EU AI Act / ISO/IEC 42001 / OECD AI Principles / Taiwan AI Basic Act / Singapore Model AI Governance)? Boards / Compliance / Regulatoren brauchen spezifische Landing-Punkte in jedem Framework.
>
> BPM / Consulting / AI-Maturity Alignments sind in [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md). **Dieses Dokument fokussiert auf AI Governance**, insbesondere L4-L5 institutionelle Glaubwürdigkeit.

---

## 1. Warum L4-L5 formale AI Governance Alignment braucht

L4 Autonomous Agent + L5 Multi-Agent Organization = AI führt Business-Aktionen ohne Echtzeit-Menschen-Supervision aus.

Boards / Regulatoren stellen drei zwingende Fragen:

1. **Wer trägt Haftung**? Wer ist rechtlich / ethisch verantwortlich, wenn AI scheitert?
2. **Welcher Early-Warning-Mechanismus**? Was triggered menschliche Intervention für High-Risk-Entscheidungen?
3. **Wie wird es auditiert**? Können Dritte AI-Verhalten unabhängig verifizieren?

Die Antworten müssen auf **international anerkannte Governance Frameworks** mappen, um für Boards, Compliance, Regulatoren akzeptabel zu sein.

---

## 2. Acht Stufen × Mainstream AI Governance Frameworks

| Governance Framework | Quelle / Natur | Tiger AI Stufen abgedeckt |
| --- | --- | --- |
| **NIST AI RMF** | US NIST, 2023 / freiwillig aber weit übernommen | Govern→Stage 8; Map→Stage 1-2; Measure→Stage 4+8; Manage→Stage 6-8 |
| **EU AI Act** | EU, 2024 / verpflichtende Regulierung | High-risk AI mappt zu L4-L5; Transparenz→Stage 8 Audit; HITL→alle Stufen |
| **ISO/IEC 42001:2023 AI Management System** | ISO, 2023 / zertifizierbar | AI Policy→Stage 8; Risk→Stage 4+8; kontinuierliche Verbesserung→Phase C |
| **ISO/IEC 23894:2023 AI Risk Management** | ISO / Risk-Fokus | Risk Register→Stage 8 |
| **OECD AI Principles** | OECD+Mitglieder / Policy-Prinzipien | 5 Prinzipien → Tool 7.2 + 8.8 |
| **Taiwan AI Basic Act (Entwurf)** | Taiwan Legislative Yuan, in Review | Mappt auf Taiwan High-Compliance-Kunden |
| **Singapore Model AI Governance Framework** | IMDA / freiwillig | 4 Pillars → Stage 7 To-Be + Stage 8 |
| **US AI Bill of Rights** | Weißes Haus / Policy-Statement | 5 Schutzmaßnahmen → Tool 8.8 Ethics + Client-Daten-Schutz |

---

## 3. NIST AI RMF (Wichtigste globale Referenz)

NIST AI RMF ist das **am weitesten übernommene** AI Governance Framework. 4 Kernfunktionen:

### 3.1 Govern

**NIST verlangt**: org-level AI Policy, Rollen, Verantwortlichkeiten, Kultur.

**Tiger AI**: Stage 8 §12.1 RACI-Matrix; Tool 8.8 AI Ethics Checkliste 15 Items; 4-Schichten-Architektur Layer 1 Governance (Policy / Ethics / Compliance / Risk Committee / Audit Owner); Tool 3.6 Client 3-Parteien-Unterschrift = corporate-level schriftliches Commitment.

### 3.2 Map

**NIST verlangt**: Inventar von AI-System-Kontext, Risiken, Stakeholdern.

**Tiger AI**: Stage 1 As-Is (Interviews, Systems Inventory, AI Usage Inventory, Swimlane); Tool 2.2 RM Mapping; Tool 2.6 + 2.7 Component Map + 4-Schichten.

### 3.3 Measure

**NIST verlangt**: AI-System-Performance, Impact, Risk quantifizieren.

**Tiger AI**: Stage 2 Radar 0-4 Scoring; Stage 4 Impact × Effort; Stage 8 Tool 8.5 Value Tracking Matrix (5 Dimensionen); Tool 8.9 Evidence Hierarchy (L1-L5 Evidence Strength); Quarterly Gate C Radar Revisit.

### 3.4 Manage

**NIST verlangt**: Risk Mitigation, Monitoring, kontinuierliche Verbesserung.

**Tiger AI**: Stage 6 Phased Goals + Stage Gate Criteria; Stage 7 Human-AI Collaboration + HITL Nodes; Stage 8 Tool 8.6 Risk Register; Tool 8.7 Audit Log; Phase C 24-Monats Quarterly Review.

> **Insgesamt**: NIST AI RMF 4 Funktionen landen vollständig in Tiger AI 8 Stufen, **produzieren NIST-Compliance-Dokumente direkt**.

---

## 4. EU AI Act (Verpflichtende Regulierung)

EU AI Act klassifiziert AI in 4 Risk-Tiers: Unacceptable / High-risk / Limited / Minimal.

### 4.1 Risk-Klassifikation Mapping

| EU AI Act Tier | Tiger AI L-Level | Erforderliche Governance |
| --- | --- | --- |
| **Unacceptable** (Social Scoring, Real-Time Biometric ID usw.) | ❌ Tiger AI **lehnt Unterstützung ab** | — |
| **High-risk** (HR, Credit, Medical, Education, Judicial, Critical Infrastructure) | Meist L4-L5 Szenarien | Verpflichtende Risk Assessment + Transparenz + Human Oversight + Post-Market Monitoring |
| **Limited** (Chatbots, Deepfake) | Meist L1-L3 Szenarien | Transparenz-Verpflichtungen („AI-generated" markieren) |
| **Minimal** (Spam Filtering usw.) | Meist L1-L2 Szenarien | Allgemeine Verpflichtungen |

### 4.2 High-Risk AI Article Alignment

| EU AI Act Artikel | Tiger AI Mapping |
| --- | --- |
| **Art. 9 Risk Management System** | Stage 8 Tool 8.6 Risk Register |
| **Art. 10 Data Governance** | Tool 8.7 Audit Log + Tool 8.4 Permission Matrix |
| **Art. 11 Technical Documentation** | Voller 14-Sektionen Consulting Report + 4-Schichten-Architektur-Docs |
| **Art. 12 Record-Keeping (Logs)** | Tool 8.7 Audit Log 7 Event Types |
| **Art. 13 Transparency** | Tool 8.8 „AI-generated Markierung" + öffentliche Ideal Practice Unterschrift |
| **Art. 14 Human Oversight** | Tool 7.2 Human-AI Collaboration + HITL Nodes + Reviewer Workflow |
| **Art. 15 Accuracy, Robustness, Cybersecurity** | Stage 8 Tool 8.5 Value Tracking (Quality Dim) + Audit Log + Security |
| **Art. 17 Post-Market Monitoring** | Phase C Quarterly Gate C + Stage 2 Radar Revisit + 5-Dim Value Tracking Longitudinal |
| **Art. 26 Quality Management System** | ISO/IEC 42001 Alignment (siehe §5) |
| **Art. 72 Serious Incident Reporting** | Tool 8.8 Ethics §11 „AI System Incident Response" |

> **Kunden mit EU-Operations**: Tiger AI Methodik-Deliverables (voller 14-Sektionen Report + Governance Docs) dienen als EU AI Act Compliance Evidence Package.

---

## 5. ISO/IEC 42001:2023 AI Management System

ISO 42001 ist der erste **drittparteien-zertifizierbare** AI Management System Standard. Struktur spiegelt ISO 9001 / 27001 wider.

### 5.1 ISO 42001 Section Mapping

| ISO 42001 Section | Tiger AI Mapping |
| --- | --- |
| **4. Context of the Organization** | Stage 1 As-Is + Stage 2 Reference Model |
| **5. Leadership** | Sponsor + AI Champion Rollen-Definition (RACI) + AI Policy Unterschrift |
| **6. Planning** | Stage 5 Problem Definition + Stage 6 Phased Goals + Tool 6.3 Absorption |
| **7. Support** | Change Management Playbook + Trainingsplan + Ressourcenplanung |
| **8. Operation** | Stage 7 To-Be Operating Model + Human-AI Collaboration + HITL |
| **9. Performance Evaluation** | Tool 8.5 Value Tracking Matrix + Tool 8.7 Audit Log + Quarterly Gate C Radar |
| **10. Improvement** | Phase C Quarterly Review + Cases-as-Benchmarks Akkumulation |
| **Annex A Controls** | Tool 8.4 Permission + Tool 8.6 Risk + Tool 8.7 Audit + Tool 8.8 Ethics |

> **Ziel**: Unternehmen, die ISO/IEC 42001 Zertifizierung anstreben, können Tiger AI Deliverables als Management-System-Dokumentation verwenden. Tiger AI **deckt alle ISO 42001 Sections vollständig ab**.

---

## 6. OECD AI Principles (5 Prinzipien)

OECD AI Principles werden von G20, APEC breit übernommen.

| OECD Prinzip | Tiger AI Mapping |
| --- | --- |
| **1. Inclusive growth, sustainable development and well-being** | Stage 8 Tool 8.5 Value Tracking enthält „Employee Experience"; Change Management enthält „Rollen upgraden, nicht ersetzen" |
| **2. Human-centered values and fairness** | Tool 8.8 Ethics §9 Bias / Diskriminierungs-Assessment; Tool 7.2 HITL verpflichtend |
| **3. Transparency and explainability** | Tool 8.7 Audit Log + Tool 8.8 §7 „AI-generated Markierung" + voller Evidence Trail |
| **4. Robustness, security and safety** | Stage 8 Risk Register + Tool 8.4 Permission + Deployment-Modus (Hybrid / On-Prem 3 Optionen) |
| **5. Accountability** | RACI-Matrix + „**client-signed Ideal Practice 3-Parteien-Unterschrift**" + Reviewer Sign-off |

---

## 7. Taiwan AI Basic Act (Entwurf)

Taiwan Legislative Yuan AI Basic Act in Review (Stand 2026/05). Tiger AI Methodik **stimmt mit Hauptbestimmungen überein**:

| Entwurf-Highlight | Tiger AI Mapping |
| --- | --- |
| **AI Produkte/Services brauchen Risk Grading** | Stage 1-2 Identifikation + 4-Schichten-Architektur + Tool 8.6 Risk Register |
| **PII-Schutz über Model Training** | Tool 8.8 §2 PII nicht an LLM gesendet / redacted; Deployment defaults to on-prem für High-Sensitivity |
| **Algorithmus-Transparenz und Erklärbarkeit** | Tool 8.7 Audit Log + 8.8 §7 AI Markierung |
| **User-Rechte-Schutz** | Tool 8.8 §5 Mitarbeiter haben Recht zu wissen, dass Arbeit AI-prozessiert ist |
| **Operator Accountability** | RACI + Tool 8.8 §8 IP Attribution |
| **Government Regulatory Authority** | Tool 8.7 Audit Log Retention unterstützt Government Audit |

⚠️ Taiwan AI Basic Act noch nicht verabschiedet. Diese Alignment wird mit dem finalen Text aktualisiert.

---

## 8. Singapore Model AI Governance Framework

Singapore IMDA freiwilliges Framework, 4 Pillars:

| Singapore Pillar | Tiger AI Mapping |
| --- | --- |
| **1. Internal Governance Structures** | Layer 1 Governance + RACI |
| **2. Determining Level of Human Involvement** | Tool 7.2 Human-AI Collaboration (HITL Nodes) |
| **3. Operations Management** | Tool 8.4-8.7 voller Set (Permission / Value / Risk / Audit) |
| **4. Stakeholder Interaction & Communication** | Tool 8.2 Change Management Playbook + Stakeholder Map |

---

## 9. Regulatorische / Compliance Deliverables Map

Wenn Kunden mit Regulierung / Compliance / Internal Audit konfrontiert sind, welche Tiger AI Deliverables direkt eingereicht werden können:

| Regulatorischer Bedarf | Direktes Tiger AI Deliverable |
| --- | --- |
| AI Risk Assessment | Stage 4 Gap + Tool 8.6 Risk Register |
| AI Policy | Tool 8.8 Ethics Checkliste 15 Items + AI Policy Doc |
| Audit Evidence Package | Tool 8.7 Audit Log + Quarterly Gate C Logs + Stage 2 Radar Before/After |
| 3rd-Party Audit Prep | Voller 14-Sektionen Report + 4-Schichten-Architektur + 4 autoritative Docs |
| ROI / Benefit Substantiation | Tool 8.5 Value Tracking 5 Dimensionen + longitudinale KPI |
| Incident Response Flow | Tool 8.8 §12 + Tool 8.6 Risk Register Trigger |
| Employee Training Records | Change Management Training Records + Tool 8.8 §14 |

---

## 10. Zertifizierungs- / Labeling-Empfehlungen

Basierend auf Methodik-Reife können Tiger AI Kunden in Betracht ziehen:

| Zertifizierung | Gilt für | Geschätzte Timeline |
| --- | --- | --- |
| **ISO/IEC 42001 AI Management System** | L3+ Kunden (mit voller Governance) | 6-12 Monate |
| **ISO/IEC 27001 ISMS** | Alle Kunden (Security Baseline) | 6-12 Monate |
| **SOC 2 Type II** | US / multinationale Service-Kunden | 6-12 Monate |
| **EU AI Act CE Marking** (High-risk) | EU-Operations + High-risk AI Systeme | 12-24 Monate |

> Tiger AI Deliverables dienen als **90% der Zertifizierungs-Dokumentations-Basis**. Tatsächliche Zertifizierung erfordert Drittparteien-Audit.

---

## 11. Verwandte Dokumente

| Dokument | Beziehung |
| --- | --- |
| [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | Stimmt mit Consulting Firms / BPM / AI Maturity Frameworks überein; dieses Doc fügt AI Governance hinzu |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Warum Methodik der Debatte standhält |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | Methodik Failure Modes & Counter-Cases |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Stage 8 | Voller Governance Toolkit |

---

## 12. Referenzen

- NIST (2023). *AI Risk Management Framework (AI RMF 1.0)*.
- European Commission (2024). *Regulation on Artificial Intelligence (EU AI Act)*.
- ISO/IEC (2023). *ISO/IEC 42001:2023 — AI Management System*.
- ISO/IEC (2023). *ISO/IEC 23894:2023 — AI Risk Management*.
- OECD (2019, updated 2024). *OECD AI Principles*.
- The White House (2022). *Blueprint for an AI Bill of Rights*.
- Singapore IMDA (2020). *Model AI Governance Framework, 2nd Edition*.
- 立法院 (in Review). *Taiwan Artificial Intelligence Basic Act Draft*.

---

Lizenz & Zitation

Dieses Dokument ist Apache License 2.0; darf verwendet, modifiziert, kommerzialisiert werden, vorausgesetzt die [`../NOTICE`](../NOTICE) Attribution wird beibehalten.
