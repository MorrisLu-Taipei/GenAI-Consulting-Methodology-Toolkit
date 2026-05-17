# AI Governance Alignment : Méthodologie Tiger AI vs frameworks internationaux d'AI Governance

> 🌐 Langue : [繁體中文](AI_GOVERNANCE_ALIGNMENT.md) ｜ [English](AI_GOVERNANCE_ALIGNMENT_EN.md) ｜ [Deutsch](AI_GOVERNANCE_ALIGNMENT_DE.md) ｜ Français ｜ [Español](AI_GOVERNANCE_ALIGNMENT_ES.md) ｜ [日本語](AI_GOVERNANCE_ALIGNMENT_JA.md) ｜ [한국어](AI_GOVERNANCE_ALIGNMENT_KR.md)
>
> Apache License 2.0 · Auteur : Morris Lu · Tiger AI

Dernière mise à jour : 2026-05-16

---

> **Ce que ce document répond** : Comment la méthodologie Tiger AI se mappe-t-elle aux frameworks internationaux d'AI Governance (NIST AI RMF / EU AI Act / ISO/IEC 42001 / OECD AI Principles / Taiwan AI Basic Act / Singapore Model AI Governance) ? Boards / compliance / régulateurs ont besoin de points d'atterrissage spécifiques dans chaque framework.
>
> BPM / consulting / AI-maturity alignments sont dans [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md). **Ce doc se concentre sur AI Governance**, particulièrement la crédibilité institutionnelle L4-L5.

---

## 1. Pourquoi L4-L5 a besoin d'AI Governance Alignment formel

L4 Autonomous Agent + L5 Multi-Agent Organization = AI exécutant des actions business sans supervision humaine en temps réel.

Boards / régulateurs posent trois questions obligatoires :

1. **Qui porte la responsabilité** ? Qui est légalement / éthiquement responsable quand l'IA échoue ?
2. **Quel mécanisme d'early-warning** ? Qu'est-ce qui déclenche l'intervention humaine pour des décisions à haut risque ?
3. **Comment est-ce audité** ? Des tiers peuvent-ils vérifier indépendamment le comportement de l'IA ?

Les réponses doivent se mapper sur des **frameworks de gouvernance reconnus internationalement** pour être acceptables aux boards, compliance, régulateurs.

---

## 2. Huit stades × Frameworks AI Governance mainstream

| Framework de Gouvernance | Source / Nature | Stades Tiger AI couverts |
| --- | --- | --- |
| **NIST AI RMF** | US NIST, 2023 / volontaire mais largement adopté | Govern→Stage 8 ; Map→Stage 1-2 ; Measure→Stage 4+8 ; Manage→Stage 6-8 |
| **EU AI Act** | EU, 2024 / régulation obligatoire | High-risk AI mappe à L4-L5 ; transparence→Stage 8 Audit ; HITL→tous stades |
| **ISO/IEC 42001:2023 AI Management System** | ISO, 2023 / certifiable | AI policy→Stage 8 ; risk→Stage 4+8 ; amélioration continue→Phase C |
| **ISO/IEC 23894:2023 AI Risk Management** | ISO / focus risque | Risk Register→Stage 8 |
| **OECD AI Principles** | OECD+membres / principes de politique | 5 principes → Tool 7.2 + 8.8 |
| **Taiwan AI Basic Act (projet)** | Taiwan Legislative Yuan, en review | Mappe aux clients Taiwan high-compliance |
| **Singapore Model AI Governance Framework** | IMDA / volontaire | 4 pillars → Stage 7 To-Be + Stage 8 |
| **US AI Bill of Rights** | Maison Blanche / déclaration de politique | 5 protections → Tool 8.8 Ethics + protection données client |

---

## 3. NIST AI RMF (Référence globale la plus importante)

NIST AI RMF est le framework AI Governance **le plus largement adopté**. 4 fonctions core :

### 3.1 Govern

**NIST exige** : politique IA org-level, rôles, responsabilités, culture.

**Tiger AI** : Stage 8 §12.1 matrice RACI ; Tool 8.8 AI Ethics Checklist 15 items ; architecture 4-couches Layer 1 Governance (Policy / Ethics / Compliance / Risk Committee / Audit Owner) ; Tool 3.6 signature client 3-parties = commitment écrit corporate-level.

### 3.2 Map

**NIST exige** : inventaire du contexte du système IA, risques, stakeholders.

**Tiger AI** : Stage 1 As-Is (interviews, Systems Inventory, AI Usage Inventory, Swimlane) ; Tool 2.2 RM Mapping ; Tool 2.6 + 2.7 Component Map + 4-couches.

### 3.3 Measure

**NIST exige** : quantifier performance, impact, risque du système IA.

**Tiger AI** : Stage 2 radar 0-4 scoring ; Stage 4 Impact × Effort ; Stage 8 Tool 8.5 Value Tracking Matrix (5 dimensions) ; Tool 8.9 Evidence Hierarchy (L1-L5 evidence strength) ; revisit radar quarterly Gate C.

### 3.4 Manage

**NIST exige** : risk mitigation, monitoring, amélioration continue.

**Tiger AI** : Stage 6 Phased Goals + Stage Gate Criteria ; Stage 7 Human-AI Collaboration + HITL nodes ; Stage 8 Tool 8.6 Risk Register ; Tool 8.7 Audit Log ; Phase C 24-mois quarterly review.

> **Globalement** : NIST AI RMF 4 fonctions atterrissent entièrement dans Tiger AI 8 stades, **produisant directement des documents NIST compliance**.

---

## 4. EU AI Act (Régulation obligatoire)

EU AI Act classifie l'IA en 4 tiers de risque : Unacceptable / High-risk / Limited / Minimal.

### 4.1 Mapping de classification de risque

| EU AI Act Tier | Tiger AI L-level | Gouvernance requise |
| --- | --- | --- |
| **Unacceptable** (social scoring, real-time biometric ID, etc.) | ❌ Tiger AI **refuse d'assister** | — |
| **High-risk** (HR, credit, medical, education, judicial, critical infrastructure) | Surtout scénarios L4-L5 | Risk assessment obligatoire + transparence + human oversight + post-market monitoring |
| **Limited** (chatbots, deepfake) | Surtout scénarios L1-L3 | Obligations de transparence (marquer « AI-generated ») |
| **Minimal** (spam filtering, etc.) | Surtout scénarios L1-L2 | Obligations générales |

### 4.2 High-Risk AI Article Alignment

| EU AI Act Article | Mapping Tiger AI |
| --- | --- |
| **Art. 9 Risk Management System** | Stage 8 Tool 8.6 Risk Register |
| **Art. 10 Data Governance** | Tool 8.7 Audit Log + Tool 8.4 Permission Matrix |
| **Art. 11 Technical Documentation** | Rapport consulting 14-sections complet + docs architecture 4-couches |
| **Art. 12 Record-Keeping (logs)** | Tool 8.7 Audit Log 7 event types |
| **Art. 13 Transparency** | Tool 8.8 « AI-generated marking » + signature publique Ideal Practice |
| **Art. 14 Human Oversight** | Tool 7.2 Human-AI Collaboration + HITL nodes + Reviewer Workflow |
| **Art. 15 Accuracy, Robustness, Cybersecurity** | Stage 8 Tool 8.5 Value Tracking (dim qualité) + Audit Log + Security |
| **Art. 17 Post-Market Monitoring** | Phase C quarterly Gate C + revisit radar Stage 2 + value tracking 5-dim longitudinal |
| **Art. 26 Quality Management System** | Alignment ISO/IEC 42001 (voir §5) |
| **Art. 72 Serious Incident Reporting** | Tool 8.8 Ethics §11 « AI system incident response » |

> **Clients avec opérations EU** : les deliverables de la méthodologie Tiger AI (rapport 14-sections complet + governance docs) servent de package d'evidence compliance EU AI Act.

---

## 5. ISO/IEC 42001:2023 AI Management System

ISO 42001 est le premier standard AI management system **certifiable par tiers**. La structure reflète ISO 9001 / 27001.

### 5.1 Mapping section ISO 42001

| ISO 42001 Section | Mapping Tiger AI |
| --- | --- |
| **4. Context of the Organization** | Stage 1 As-Is + Stage 2 Reference Model |
| **5. Leadership** | Définition rôle Sponsor + AI Champion (RACI) + signature AI Policy |
| **6. Planning** | Stage 5 Problem Definition + Stage 6 Phased Goals + Tool 6.3 Absorption |
| **7. Support** | Change Management Playbook + plan de formation + planification de ressources |
| **8. Operation** | Stage 7 To-Be Operating Model + Human-AI Collaboration + HITL |
| **9. Performance Evaluation** | Tool 8.5 Value Tracking Matrix + Tool 8.7 Audit Log + radar quarterly Gate C |
| **10. Improvement** | Phase C quarterly review + accumulation Cases-as-Benchmarks |
| **Annex A Controls** | Tool 8.4 Permission + Tool 8.6 Risk + Tool 8.7 Audit + Tool 8.8 Ethics |

> **Objectif** : Les entreprises poursuivant la certification ISO/IEC 42001 peuvent utiliser les deliverables Tiger AI comme documentation management-system. Tiger AI **couvre entièrement toutes les sections ISO 42001**.

---

## 6. OECD AI Principles (5 principes)

OECD AI Principles sont largement adoptés par G20, APEC.

| OECD Principe | Mapping Tiger AI |
| --- | --- |
| **1. Inclusive growth, sustainable development and well-being** | Stage 8 Tool 8.5 Value Tracking inclut « employee experience » ; Change Management inclut « upgrader rôles, pas remplacer » |
| **2. Human-centered values and fairness** | Tool 8.8 Ethics §9 bias / discrimination assessment ; Tool 7.2 HITL obligatoire |
| **3. Transparency and explainability** | Tool 8.7 Audit Log + Tool 8.8 §7 « AI-generated marking » + full evidence trail |
| **4. Robustness, security and safety** | Stage 8 Risk Register + Tool 8.4 Permission + mode de déploiement (Hybrid / On-Prem 3 options) |
| **5. Accountability** | Matrice RACI + « **signature 3-parties Ideal Practice signée par client** » + Reviewer sign-off |

---

## 7. Taiwan AI Basic Act (Projet)

Taiwan Legislative Yuan AI Basic Act en review (au 2026/05). La méthodologie Tiger AI **s'aligne sur les principales provisions** :

| Highlight du projet | Mapping Tiger AI |
| --- | --- |
| **Produits/services IA ont besoin de risk grading** | Identification Stage 1-2 + architecture 4-couches + Tool 8.6 Risk Register |
| **Protection PII sur le training de modèle** | Tool 8.8 §2 PII non envoyé au LLM / redacted ; déploiement par défaut on-prem pour haute-sensibilité |
| **Transparence et explicabilité d'algorithme** | Tool 8.7 Audit Log + 8.8 §7 marquage IA |
| **Protection des droits utilisateur** | Tool 8.8 §5 les employés ont droit de savoir que le travail est traité par IA |
| **Accountability de l'opérateur** | RACI + Tool 8.8 §8 attribution IP |
| **Autorité régulatoire gouvernementale** | Tool 8.7 Audit Log retention supporte audit gouvernemental |

⚠️ Taiwan AI Basic Act pas encore adopté. Cet alignment sera mis à jour avec le texte final.

---

## 8. Singapore Model AI Governance Framework

Singapore IMDA framework volontaire, 4 pillars :

| Singapore Pillar | Mapping Tiger AI |
| --- | --- |
| **1. Internal Governance Structures** | Layer 1 Governance + RACI |
| **2. Determining Level of Human Involvement** | Tool 7.2 Human-AI Collaboration (HITL nodes) |
| **3. Operations Management** | Tool 8.4-8.7 set complet (Permission / Value / Risk / Audit) |
| **4. Stakeholder Interaction & Communication** | Tool 8.2 Change Management Playbook + Stakeholder Map |

---

## 9. Map des deliverables régulatoires / compliance

Quand les clients font face à régulatoire / compliance / audit interne, quels deliverables Tiger AI peuvent être soumis directement :

| Besoin régulatoire | Deliverable Tiger AI direct |
| --- | --- |
| AI risk assessment | Stage 4 Gap + Tool 8.6 Risk Register |
| AI policy | Tool 8.8 Ethics Checklist 15 items + AI Policy doc |
| Audit evidence package | Tool 8.7 Audit Log + logs quarterly Gate C + Stage 2 radar before/after |
| Préparation audit 3e partie | Rapport 14-sections complet + architecture 4-couches + 4 docs autoritatifs |
| ROI / substantiation de bénéfice | Tool 8.5 Value Tracking 5 dimensions + KPI longitudinal |
| Flow de réponse à incident | Tool 8.8 §12 + triggers Tool 8.6 Risk Register |
| Records de formation employé | Records de formation Change Management + Tool 8.8 §14 |

---

## 10. Recommandations de certification / labeling

Basé sur la maturité de la méthodologie, les clients Tiger AI peuvent considérer :

| Certification | S'applique à | Timeline est. |
| --- | --- | --- |
| **ISO/IEC 42001 AI Management System** | Clients L3+ (avec gouvernance complète) | 6-12 mois |
| **ISO/IEC 27001 ISMS** | Tous clients (baseline sécurité) | 6-12 mois |
| **SOC 2 Type II** | Clients US / service multinational | 6-12 mois |
| **EU AI Act CE Marking** (High-risk) | Opérations EU + systèmes IA High-risk | 12-24 mois |

> Les deliverables Tiger AI servent de **base de 90% de la documentation de certification**. La certification réelle nécessite un audit tiers.

---

## 11. Documents apparentés

| Document | Relation |
| --- | --- |
| [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | S'aligne sur firmes consulting / BPM / AI maturity frameworks ; ce doc ajoute AI Governance |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Pourquoi la méthodologie résiste au débat |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | Failure modes & counter-cases de la méthodologie |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Stage 8 | Toolkit gouvernance complet |

---

## 12. Références

- NIST (2023). *AI Risk Management Framework (AI RMF 1.0)*.
- European Commission (2024). *Regulation on Artificial Intelligence (EU AI Act)*.
- ISO/IEC (2023). *ISO/IEC 42001:2023 — AI Management System*.
- ISO/IEC (2023). *ISO/IEC 23894:2023 — AI Risk Management*.
- OECD (2019, updated 2024). *OECD AI Principles*.
- The White House (2022). *Blueprint for an AI Bill of Rights*.
- Singapore IMDA (2020). *Model AI Governance Framework, 2nd Edition*.
- 立法院 (en review). *Taiwan Artificial Intelligence Basic Act Draft*.

---

Licence & Citation

Ce document est sous Apache License 2.0 ; peut être utilisé, modifié, commercialisé, à condition de préserver l'attribution [`../NOTICE`](../NOTICE).
