# Alignement de la méthodologie Tiger AI avec les frameworks de l'industrie

> 🌐 Langue : [繁體中文](INDUSTRY_FRAMEWORK_ALIGNMENT.md) ｜ [English](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) ｜ [Deutsch](INDUSTRY_FRAMEWORK_ALIGNMENT_DE.md) ｜ Français ｜ [Español](INDUSTRY_FRAMEWORK_ALIGNMENT_ES.md) ｜ [日本語](INDUSTRY_FRAMEWORK_ALIGNMENT_JA.md) ｜ [한국어](INDUSTRY_FRAMEWORK_ALIGNMENT_KR.md)
>
> Apache License 2.0 · Auteur : Morris Lu · Tiger AI

Dernière mise à jour : 2026-05-15

---

> **Ce que ce document répond** : Comment la méthodologie Tiger AI se relie-t-elle aux cabinets de conseil mainstream (McKinsey / BCG / Bain / Deloitte / Accenture / PwC), aux écoles académiques (Rosemann BPM / CMMI / APQC / SCOR / TOGAF / Dragon1) et aux frameworks de maturité IA (Gartner / MIT / MMC / Forrester) ? Que dupliquons-nous, complétons-nous ou innovons-nous ?
>
> **Position centrale** : Tiger AI ne réinvente pas la roue mais **intègre les outils mainstream, complète la boucle fermée de l'industrie, et ajoute les essentiels de l'ère GenAI**. Tous les frameworks cités sont détaillés dans [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md) ; ce document mappe entre les cabinets.

---

## 1. Pourquoi cet alignement compte

| Public | Ce qu'il obtient |
| --- | --- |
| Grande entreprise IT/CIO | « Cette méthodologie est compatible avec notre TOGAF / ITIL / APQC existant » |
| Consultants d'autres cabinets | « Je viens de BCG/Deloitte — je vois quels outils je continue d'utiliser et lesquels sont spécifiques à Tiger AI » |
| Reviewers académiques | « Tiger AI n'est pas de la science marginale — elle se tient sur les épaules des écoles Rosemann/CMMI/APQC » |
| Régulateurs | « Les standards cités sont internationalement reconnus ; la gouvernance IA mappe vers les frameworks GRC existants » |
| Dirigeants client | « Ce pour quoi nous payons est le meilleur de l'industrie + complétion de l'ère GenAI, pas la méthode propriétaire d'un cabinet unique » |

---

## 2. Huit étapes vs. cabinets de conseil mainstream

### 2.1 Tableau d'alignement inter-cabinets

| Étape | Tiger AI | McKinsey | BCG | Bain | Deloitte | Accenture | PwC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1 As-Is Snapshot** | 40-Q interview + Inventory + Swimlane | 7-Step Step 1: Define Problem | Diagnostic Survey | Customer / Process Diagnostics | Business Architecture Discovery | Living Business Diagnostic | Value Creation Diagnostic |
| **2 Reference Model** | APQC + Tiger AI L1-L5 + 4 couches | (rarement fait) | Capability Maturity Map | (non-core) | TOGAF Capability Assessment | Industry Reference Architecture | Capability Framework |
| **3 Best Practice → Ideal** | Benchmark + Ideal Practice Workshop | Best Practice Research | Strategic Position vs Industry | NPS / Customer Loyalty | Industry Pulse | Industry Benchmarking | Industry Outlook |
| **4 Gap Analysis** | M/B/R + Impact×Effort | Issue Tree + MECE | Importance-Performance Map | Pareto + Lean | Capability Gap Heatmap | Maturity Gap Analysis | Gap Map |
| **5 Problem Definition** | 80/20 + 5 Whys + EPS | Day-1 + SCQ + Pyramid | Strategic Diagnosis | Bain Question Pyramid | Hypothesis-Driven | Outcome-Driven | Issue-Tree Synthesis |
| **6 Phased Goals** | Phased + Absorption | Workplan + Critical Path | Phased Transformation | Bain Way Multi-phase | Imagine-Deliver-Run | Wave Planning | Transformation Wave |
| **7 To-Be Design** | Phased To-Be + Human-AI | To-Be Operating Model | Operating Model Design | Bain Way (Org) | Target Operating Model | Future-State Blueprint | Future Operating Model |
| **8 Implementation & Change** | Roadmap + Change + Value Tracking | Influence Model + 7S | Smart Simplicity | Bain Results Delivery | Diamond Performance | Wired for Change | Project Delivery |

### 2.2 Ce que chaque cabinet contribue

- **McKinsey** MECE / Pyramid / Issue Tree **sont sources pour les outils Tiger AI Stage 4-5** (dans la Frameworks Library)
- **BCG** Capability Maturity thinking **inspire le scoring RM Tiger AI Stage 2**
- **Bain** Customer / Process Diagnostics **complètent la banque d'interviews Tiger AI Stage 1**
- **Deloitte** Imagine-Deliver-Run **s'aligne fortement avec les trois phases Tiger AI Stage 6**
- **Accenture** Wave Planning **cohérent avec Tiger AI Phase 1/2/3**
- **PwC** Value Creation Diagnostic **mappe vers le value tracking Tiger AI Stage 8**

> **Conclusion** : Aucune des 8 étapes n'est une « invention » Tiger AI. **L'innovation réside dans l'intégration de ces outils dispersés en une chaîne de raisonnement complète avec dépendances de données, signatures client et falsification en boucle fermée**.

---

## 3. Alignement des écoles Reference Model

### 3.1 Tiger AI 4 couches vs. principaux frameworks EA

| Couche | Tiger AI | Dragon1 EA | TOGAF ADM | Zachman | ArchiMate |
| --- | --- | --- | --- | --- | --- |
| **L1 Governance** | AI Governance | Enterprise Governance | (Architecture Vision) | Scope | Motivation + Strategy |
| **L2 Business** | AI Business (L1-L5 ici) | Business(es) | Business Architecture (B) | Business | Business Layer |
| **L3 Information** | AI Information | Information Facilities & Systems | Data + Application (C+D) | System | Application + Information |
| **L4 Technical** | AI Technical | IT Infrastructure(s) | Technology (E) | Technology | Technology + Implementation |

**Pourquoi cet alignement** : tous les frameworks EA mainstream convergent vers « **4 couches d'abstraction** » — pas une coïncidence mais un résultat nécessaire de l'axe scientifique « abstraction × volatilité » (voir [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) §5).

### 3.2 Alignement Process Reference Model

| Cas d'usage | Tiger AI recommande | APQC PCF | SCOR | eTOM | ITIL | CMMI |
| --- | --- | --- | --- | --- | --- | --- |
| **Processus inter-industries** | APQC PCF (défaut) | ✓ 13 Cat | — | — | — | — |
| **Supply chain / fab** | SCOR | — | ✓ 6 sections | — | — | — |
| **Télécom / abonnement** | eTOM | — | — | ✓ 3 niveaux | — | — |
| **IT service mgmt** | ITIL | — | — | — | ✓ 5 phases | — |
| **Maturité logicielle** | CMMI | — | — | — | — | ✓ 5 niveaux |
| **Maturité d'adoption IA** | **Tiger AI L1-L5 (DIY, comble lacune industrie)** | — | — | — | — | — |

> **Aucun RM industriel existant ne couvre l'adoption IA** — d'où la nécessité de Tiger AI L1-L5, auto-qualifié au Tool 2.5 score 9/10.

### 3.3 Racines de l'école BPM Maturity

| Concept | Source | Mapping Tiger AI |
| --- | --- | --- |
| Capability Maturity Levels (échelle 5 niveaux) | **Rosemann BPM Maturity** (QUT) + CMMI | Stage 2 0-4 scoring, Tiger AI L1-L5 |
| Process Excellence Characteristics | Rosemann + APQC | Stage 3 Excellence Capability Profile |
| Stage Gates | CMMI + Rosemann | Stage 6 acceptance gates |
| Organizational Absorption | Rosemann (recherche émergente) | Tool 6.3 Absorption Assessment |

> **Remerciement** : Prof. Michael Rosemann (QUT) est l'advisor de master de l'auteur ; les racines de l'école BPM de cette méthodologie proviennent directement de son mentorat de longue date.

---

## 4. Alignement des frameworks de maturité IA

### 4.1 Principaux frameworks de maturité IA mappés

| Framework | Niveaux | Mapping Tiger AI L1-L5 |
| --- | --- | --- |
| **Gartner AI Maturity Model** | Awareness / Active / Operational / Systemic / Transformational | L1 / L1+L2 / L3 / L4 / L5 |
| **MIT Sloan AI Capability** | Experimenters / Investigators / Pioneers / Empowerment | L1-L2 / L2-L3 / L3-L4 / L5 |
| **McKinsey AI Quotient (AIQ)** | (échelle continue, 4 drivers) | Mappe vers le radar six-dimensions Tiger AI |
| **Capgemini DELTA Maturity** | Data / Enterprise / Leadership / Targets / Analysts | Mappe vers axe gouvernance + déploiement |
| **Forrester AI Pulse Index** | (3 anneaux : People / Process / Tech) | Mappe vers l'architecture 4 couches Tiger AI |
| **Tiger AI L1-L5** | L1 Chat / L2 Skill / L3 Workflow / L4 Auto Agent / L5 Agent Team | (**axe d'échelle L1-L3 + axe d'autonomie IA L4-L5**) |

### 4.2 Apports de Tiger AI L1-L5 au mainstream

| Apport | Pourquoi l'industrie en manque | Tiger AI le comble |
| --- | --- | --- |
| **Mapping d'outils explicite** | Gartner/MIT décrivent niveaux abstraitement, pas de landing outil | L1=OpenWebUI, L2=Antigravity, L3=n8n, L4=Hermes, L5=ClawTeam |
| **Axe d'échelle séparé de l'axe d'autonomie** | L'industrie les mélange, brouillant L4-L5 | Échelle (humain-led) vs Autonomie (IA-led), frontière critique L3→L4 |
| **Spécifique GenAI (pas ML traditionnel)** | La plupart des frameworks bloqués sur ML traditionnel / modèles prédictifs | Pleinement focalisé sur paradigme LLM / Agent / Workflow |
| **Acceptance d'étape vérifiable** | Frameworks industriels surtout échelles d'auto-évaluation | Chaque niveau a Stage Gate Criteria, indépendamment vérifiable |
| **Coordonnées duales cross-RM** | Frameworks industriels uniaxiaux | Tiger AI orthogonal au RM industriel (APQC/SCOR), radar dual |

---

## 5. Alignement des outils analytiques classiques

Détaillés dans [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md). Résumé :

### 5.1 Outils stratégie

Porter's 5 Forces (Stage 3), PESTEL (Stage 3), BCG Growth-Share (Stage 3), SWOT (Stage 3/4), Blue Ocean (Stage 7), Wardley Map (Stage 6/7).

### 5.2 Outils analyse de problèmes

MECE (Stage 2/4), Issue Tree (Stage 4/5), Pyramid Principle (Stage 5), SCQ (Stage 5), 5 Whys (Stage 5), Fishbone (Stage 4/5), Hypothesis-Driven (Stage 1-5), 80/20 (Stage 5).

### 5.3 Outils change management

Kotter 8 Steps (Stage 8), ADKAR (Stage 8), Stakeholder Map (Stage 8), RACI (Stage 8), Influence Model (Stage 8), 7S (Stage 2/8).

### 5.4 Outils financiers / ROI

NPV/IRR (Stage 8), Payback (Stage 8), Break-Even (Stage 8), Sensitivity Analysis (Stage 8), Balanced Scorecard (Stage 8), OKR (Stage 6/8).

---

## 6. Éléments uniques / innovants Tiger AI

La plupart des outils viennent de l'industrie, mais Tiger AI a ces **intégrations ou innovations uniques** :

| Innovation | Pourquoi l'industrie en manque | Design Tiger AI |
| --- | --- | --- |
| **Tiger AI L1-L5 GenAI Adoption RM** | RMs industriels encore sur IT / ML traditionnel | Premier RM conçu spécifiquement pour LLM/Agent/Workflow, remplit Tool 2.5 10 conditions 9/10 |
| **Client Ideal Practice Co-Creation Workshop** | L'industrie fait Best Practice benchmarking mais rarement Ideal signé par client | Tool 3.6 : client **signe lui-même**, ne peut nier raisonnement ultérieur |
| **Cases-as-Benchmarks format 9 champs** | Cases industriels surtout narratifs, pas de calcul de gap | Tool 3.5 : cases obligatoirement 9 champs, client auto-calcule gap en 30 min |
| **Loopback radar Stage 2 trimestriel** | Roadmaps industriels surtout linéaires, pas de mécanisme d'auto-falsification | Phase C chaque trimestre Gate C doit revisiter radar, vérifier structure réellement plus ronde |
| **Modèle de contrat 3-Phase + sorties Gate A/B/C** | Industrie surtout grands contrats fixed-scope | Phase A diagnostic / Phase B strategy / Phase C implementation, client phase ses décisions |
| **Axe d'échelle vs axe d'autonomie IA orthogonaux** | L'industrie mélange sur un seul axe | L1-L3 échelle + L4-L5 autonomie, frontière critique L3→L4 |
| **RM 4 couches × L1-L5 coordonnées duales** | Industrie uniaxiale (soit RM soit maturité) | Tiger AI exige cross-mapping dual-axes |
| **Nœuds HITL explicites par Process** | L'industrie parle gouvernance, spécifie rarement emplacement HITL | Tool 7.2 chaque processus explicitement marqué avec nœud HITL + critères d'acceptance |

---

## 7. Question client commune : Cela entre-t-il en conflit avec notre méthodologie ?

### 7.1 Client utilise TOGAF / Zachman

**Pas de conflit**. Tiger AI 4 couches **s'aligne directement avec TOGAF BDAT** (Business/Data/Application/Technology). Dire : « Nous bâtissons sur votre architecture TOGAF existante, ajoutant la dimension d'adoption GenAI (L1-L5) et la boucle fermée radar trimestrielle. »

### 7.2 Client utilise ITIL

**Pas de conflit**. Tiger AI Stage 8 Audit Log / Permission Matrix / Risk Register se connecte directement à ITIL Service Operation. Dire : « Nous complétons avec logs d'appels LLM GenAI-spécifiques, simulation Reviewer, gouvernance versions Skill. »

### 7.3 Client utilise CMMI

**Pas de conflit**. Tiger AI L1-L5 et CMMI 5 niveaux **sont apparentés** — tous deux extensions de l'école maturity capability. Dire : « CMMI for AI est une direction émergente ; Tiger AI L1-L5 est une version d'atterrissage. »

### 7.4 Client utilise frameworks internes BCG / McKinsey / Bain

**Pas de conflit, renforcement mutuel**. Tiger AI cite les outils centraux de ces cabinets (Issue Tree, MECE, Pyramid, Bain Way). Dire : « Nous ne remplaçons pas votre méthodologie de conseil stratégique ; nous ajoutons la boucle fermée d'adoption GenAI et le Reference Model 4 couches. »

### 7.5 Client utilise Gartner / Forrester AI Maturity

**Pas de conflit, plus concret**. Tiger AI L1-L5 a **des outils d'atterrissage plus concrets** que les 5 niveaux de Gartner (L1=OpenWebUI, etc.). Dire : « Gartner dit ‹Operational AI› ; nous disons ‹n8n Workflow 3 live + taux sign-off Reviewer 95%›. »

---

## 8. Alignement des citations académiques

Citations dans les References de chaque fichier respectif. Sélection :

### 8.1 École BPM / Maturity

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT. **(Racine théorique centrale)**
- Paulk, M. et al. (1993). *Capability Maturity Model for Software*. CMU/SEI.
- Curtis, B. et al. (2009). *People CMM*.

### 8.2 Reference Model / Enterprise Architecture

- APQC (2024). *Process Classification Framework Version 7.3*.
- APICS / ASCM. *SCOR Reference Model*.
- TM Forum. *eTOM Business Process Framework*.
- ISACA. *COBIT / ITIL Framework*.
- The Open Group. *TOGAF Standard 9.2*.
- Zachman, J. *Zachman Framework*.
- Dragon1. *Enterprise Architecture Reference Model*.

### 8.3 Méthodologies de conseil

- Minto, B. (2009). *The Pyramid Principle*.
- Rasiel, E. (1999). *The McKinsey Way*.
- Bain & Company. *Bain Way / Results Delivery*.
- Iansiti, M., Lakhani, K. (2020). *Competing in the Age of AI*.

### 8.4 Change Management

- Kotter, J. (1996). *Leading Change*.
- Hiatt, J. (2006). *ADKAR*. Prosci.
- Mendelow, A. (1991). *Stakeholder Mapping*.

### 8.5 Stratégie GenAI

- Gartner. *AI Maturity Model*.
- Davenport, T., Mittal, N. (2022). *All-in on AI*.
- Brynjolfsson, E., McAfee, A. (2014). *The Second Machine Age*.

---

## 9. Clôture : Sur les épaules de géants + complétion de la boucle fermée de l'industrie

Philosophie de design de la méthodologie Tiger AI :

1. **Pas de réinvention de roues** : analyse stratégie (McKinsey), change mgmt (Kotter), outils financiers (NPV/IRR), frameworks EA (TOGAF/Dragon1) — utiliser le meilleur de l'industrie
2. **Intégration + boucle fermée** : lier les outils dispersés en une chaîne de raisonnement complète avec dépendances de données, signatures client et mécanismes de falsification
3. **Combler les lacunes GenAI** : les frameworks industriels n'ont pas rattrapé l'ère LLM/Agent/Workflow → Tiger AI L1-L5 + 4 couches + Cases-as-Benchmarks + design HITL le comble
4. **Reproductible par d'autres** : Apache 2.0 + GitHub + citations académiques claires → pas un actif privé d'un cabinet

> **C'est le sens de « sur les épaules de géants + complétion de la boucle fermée de l'industrie »** — ce que les clients achètent est intégration des meilleurs de l'industrie + complétion de l'ère GenAI, pas la méthode propriétaire d'un cabinet unique.

---

## 10. Documents liés

| Document | Relation |
| --- | --- |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) §8 | Version compacte de ce document §2 (vs McKinsey/BCG/Gartner/MIT) |
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | Comment les 8 étapes tournent réellement dans une vraie engagement |
| [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md) | 50+ frameworks détaillés (ce document = carte d'alignement ; ce fichier = dictionnaire de frameworks) |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | Tables d'outils par étape |

---

Licence & Citation

Ce document est sous Apache License 2.0 ; peut être utilisé, modifié, commercialisé, à condition que l'attribution [`../NOTICE`](../NOTICE) soit préservée.
