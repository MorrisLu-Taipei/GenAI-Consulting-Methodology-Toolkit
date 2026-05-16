# 04 Scenarios — Scénarios, Cas & Index de Cas

> 🌐 中文 / Chinese : [README.md](README.md) ｜ English : [README_EN.md](README_EN.md)

> ⚠️ **Déclaration importante d'intégrité académique / Important Academic Integrity Disclaimer**
>
> **Tous les 7 SAMPLE_CLIENT_CASE_*.md dans ce répertoire (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education) et tous les personnages principaux nommés (p. ex., « Ming » dans `00_Overview/CLIENT_JOURNEY_STORY.md`) sont des cas fictifs générés par IA, PAS des données clients réelles.**
>
> - **Usage** : démonstration pédagogique, explication méthodologique, exercices d'application des tableaux Stage 1-8
> - **Limites** : tous les chiffres (temps, ROI, person-month, budget, KPI) sont des exemples illustratifs, **ne doivent PAS être utilisés pour le marketing externe, des engagements contractuels ou des preuves empiriques académiques**
> - **Niveau d'evidence** : selon [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 8.9, les cas de ce répertoire sont **L0 (AI-Simulated Teaching Case)**, inférieur au questionnaire d'auto-évaluation L1
> - **Les vrais cas longitudinaux** seront remplacés seulement après l'étude empirique 18-24 mois de [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md)

## 1. Objectif de ce Répertoire

Ce répertoire est la **bibliothèque de matériel et evidence** de toute la méthodologie. `01`-`03`, `05`, `06` sont « méthode et processus » ; ce répertoire est « **fournir des scénarios, cas et cas sélectionnables réels pour la mise en œuvre** ».

Le problème qu'il résout : **le plus grand obstacle dans l'adoption IA n'est pas « on ne sait pas faire », c'est « on ne sait pas ce qui est possible, comment les autres font, à quoi ça ressemble après ».** Ce répertoire fournit quatre types de matériel : (1) **Stories de scénarios** par rôle/département (pour que les clients se « reconnaissent »), (2) **Standards d'écriture de cas et tableaux de contrôle** (cas cohérents), (3) **Cas de démo complets pour 7 secteurs** (du questionnaire à la Roadmap), (4) **Index de 150+ applications LLM réelles** (recherche rapide par L-level et département).

Qui utilise : consultants (scénarios Discovery, index de cas pour PoC), Sales (cas pour justifier valeur), formateurs (cas comme sujets de démo), clients (cas complets pour comprendre « à quoi ça ressemble après »).

## 2. Position dans la Méthodologie

| Axe | Mapping |
| --- | --- |
| Flux de service 3 phases | **Sur toute la durée** — Discovery utilise scénarios, Build utilise cas comme sujets, Deliver utilise cas pour justifier |
| Structure de conseil 8 étapes | Supporte principalement **Stage 1 As-Is Snapshot (scénarios actuels), Stage 3 Best Practice Integration (benchmark industrie)** |
| Maturité L1-L5 | Index de cas mappe chaque cas à un L-level |
| Engagement Lifecycle | Sales (Discovery reconnaissance) + Build (sujets de démo) |

## 3. Objectifs & Bénéfices

| Objectif | Bénéfice |
| --- | --- |
| Fournir stories de scénarios par rôle/département | Clients peuvent se « reconnaître », Discovery focalise plus vite |
| Standards d'écriture de cas et tableaux de contrôle | Consultants écrivent des cas structurellement cohérents et vérifiables |
| 7 cas de démo complets par secteur | Clients voient le « tableau complet d'implémentation » ; nouveaux consultants ont des modèles |
| Index 150+ applications LLM (recherche double axe) | Clients/consultants peuvent chercher par « L-level » ou « département » instantanément |
| Gestion d'attente cross-level | Quand client pointe un cas L5, avec l'index lui pointer « vous êtes L2, il faut rattraper avant » |

**Si ce répertoire est sauté** : client n'a pas idée « de ce qui est possible », sélection PoC à l'aveugle, qualité de cas inconsistante, pas de gestion d'attente cross-level.

## 4. Workflow & Logique

```text
Phase Discovery
   → CUSTOMER_SCENARIO_LIBRARY (scénarios par rôle, reconnaissance client)
   → LLM_APPS_CASE_INDEX (par L-level + département, sélectionner cas « pertinents pour client »)
   → Cas sélectionnés → candidats PoC

Phase cours / proposition
   → SAMPLE_CLIENT_CASE_* (montrer cas complets du même secteur au client)
   → LLM_APPS_CASE_INDEX (sujets de démo, exercices en classe)

Consultant écrit nouveau cas
   → CASE_WRITING_STANDARD (standard d'écriture)
   → CASE_CONTROL_TABLES (tableau de contrôle, copier-coller et remplir)
```

| Étape | Qui | Quand | Input | Output |
| --- | --- | --- | --- | --- |
| Reconnaissance client | Consultant | Discovery | Bibliothèque de scénarios | Pain reconnu par client |
| Sélectionner candidats PoC | Consultant | Après diagnostic | L-level + département → index | Liste de candidats PoC |
| Montrer cas complets au client | Sales / consultant | Proposition | Sample case du même secteur | Client comprend le tableau complet |
| Écrire nouveaux cas | Consultant | Après fin de projet | Standard + tableau de contrôle | Nouveau sample case |

> Logique : les stories de scénarios sont « **provoquer la résonance** » (client dit « oui, c'est comme nous ») ; l'index de cas est « **sélection rapide** » (par L-level/département recherche instantanée) ; cas de démo complets montrent « **tableau complet** » (du questionnaire à Roadmap) ; standards d'écriture « **assurent la cohérence** » (qualité stable des nouveaux cas).

## 5. Descriptions de Fichiers

### Scénarios et Standards

| Fichier | Usage |
| --- | --- |
| `CUSTOMER_SCENARIO_LIBRARY.md` | Stories par rôle/département : CEO, COO, IT, RH, Sales, Customer Service, Marketing, Operations, Finance, RH, IT ; chaque story contient Before, Trigger, AI Flow, Systems, Output, KPI. |
| `CASE_WRITING_STANDARD.md` | Standard d'écriture, régit l'écriture de L1-L5 Input / Process / Output / Evidence et livrables vérifiables. |
| `CASE_CONTROL_TABLES.md` | Tableaux de contrôle de cas, copier-coller pour activités d'évaluation, L1-L5 IPOE, Evidence, Stage Gate, gouvernance risque, acceptation livrables. |
| `INDUSTRY_SCENARIOS.md` | Scénarios recommandés 5 secteurs (Retail/Education/Logistique/Software/Services professionnels), par secteur : intro, baseline L1-L5, Top-10 scénarios, gouvernance risque, Quick Win 30 jours, Anti-Patterns. |

### Cas de Démo Complets (clients avec codenames)

| Fichier | Cas |
| --- | --- |
| `SAMPLE_CLIENT_CASE_MANUFACTURING.md` | Industrie R&D-fabrication cas complet |
| `SAMPLE_CLIENT_CASE_HOSPITAL.md` | Hôpital / institution médicale (données très sensibles, full on-prem, revue humaine) |
| `SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md` | Agence marketing (codename : Agence M) |
| `SAMPLE_CLIENT_CASE_B2B_SALES.md` | Distributeur équipement industriel B2B (codename : Équipement B), focus RFP, gouvernance CRM, L5 Pre-RFP Team |
| `SAMPLE_CLIENT_CASE_FINANCIAL.md` | Industrie financière (codename : Banque régionale F), full on-prem, double revue |
| `SAMPLE_CLIENT_CASE_GOVERNMENT.md` | Agence gouvernementale (codename : Bureau digital de la ville G), full on-prem, triple revue |
| `SAMPLE_CLIENT_CASE_EDUCATION.md` | Institution éducative (codename : Université tech E), Hybrid, éthique académique |

> Chaque cas suit le flow complet : résultat questionnaire → jugement L-level → ratio de cours → output en classe → analyse 8 étapes → résumé du rapport de diagnostic → Roadmap 30/60/90 → ROI → gouvernance risque.

### Implémentation L5 et Index de Cas

| Fichier | Usage |
| --- | --- |
| `CLAWTEAM_WALKTHROUGH.md` | Walkthrough complet d'Agent Team inter-départemental avec ClawTeam (HKUDS, MIT) (Manufacturing QA Team), incl. setup environnement, chaîne de tâches, Human Gate, mapping Gate 5. |
| `LLM_APPS_CASE_INDEX.md` | **Index d'applications LLM (multi-sources)**. 150+ apps LLM réelles, **deux axes de recherche** : ① par L1-L5 / cours ② par département/processus d'entreprise (Engineering/Finance/RH/Sales/Marketing/R&D/Operations/Customer Service/Legal/Data/Design/Management). Sources : awesome-llm-apps (Apache-2.0), ai-engineering-hub (MIT). |

### `*_EN.md`

Versions anglaises sibling de certains fichiers.

## 6. Mapping vers Autres Répertoires

| Répertoire | Relation avec ce répertoire | Flux de données |
| --- | --- | --- |
| `01_Assessment` | L-level du diagnostic détermine quels cas sélectionner | `01` L-level → `04` filtre cas |
| `02_Course_Design` | Cas/index PoC sont source pour démos et exercices en classe | `04` cas ↔ `02` sujets cours |
| `03_Consulting_Report` | Stage 3 benchmark Best Practice industriel cite cas | `04` cas → `03` Stage 3 |
| `05_Sales` | Cas et scénarios complets sont justification du matériel Sales | `04` cas → `05` justification |
| `00_Overview` | Stories de scénarios sont matériel pour la story | `04` ↔ `00` |
| `90_References` | Citations tierces pour index de cas (awesome-llm-apps / ai-engineering-hub) | `90` citation → `04` |

## 7. Scénarios d'Usage Communs

- **Reconnaissance Discovery** : prendre `CUSTOMER_SCENARIO_LIBRARY.md` correspondant au rôle client, demander « quelle story vous ressemble ? ».
- **Sélectionner PoC** : après diagnostic L-level, dans `LLM_APPS_CASE_INDEX.md` §3 par L-level ou §4 par département, choisir 3-5 pertinents pour le client.
- **Justification proposition** : montrer `SAMPLE_CLIENT_CASE_MANUFACTURING.md` au client manufacturing, démontrer le tableau d'implémentation complet.
- **Gestion d'attente cross-level** : client pointe cas L5 → avec l'index lui pointer son L-level et les cours prérequis.
- **Écrire nouveau cas** : après fin de projet, suivre `CASE_WRITING_STANDARD.md` + `CASE_CONTROL_TABLES.md` pour l'écrire comme nouveau sample case.

---

## ⭐ Cross-Topic Quick References : 5 Thèmes Centraux, où Trouver

Toute la méthodologie a 5 artères principales traversant tous les répertoires. Comment ce répertoire se connecte à chacune :

| Cross-Topic | Lieu principal | Comment ce répertoire se connecte |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lecture trois moteurs** | Root [`README_FR.md`](../README_FR.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | Les cas peuvent être exécutés avec les workflows Tier 2 de Claude Code : `/simulate-engagement` simule un mandat complet de 6 semaines, `/parallel-perspectives` 6 vues stakeholders, `/devil-pair-debate` débat des présupposés de valeur |
| 🎓 **Fondement académique (7 piliers)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | L'argumentation ROI des cas correspond aux **Real Options** (pourquoi Phase 1 avec NPV ≈ 0 vaut quand même l'investissement) ; le To-Be Design correspond à **Task-Technology Fit** (quelles tâches doivent atteindre L4, lesquelles doivent rester à L2) |
| 📚 **Éducation L1-L5** | [`../02_Course_Design/`](../02_Course_Design/) | LLM Apps Case Index classifié par L-level, sélectionnable directement comme PoC ; `POC_SCENARIO_SPECS.md` + `N8N_WORKFLOW_TEMPLATES.md` transforment les cas en sujets hands-on de classe L3 |
| 🔁 **Conseil / 8 étapes + Closed-Loop Phase A→B→C** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Les cas sont le « matériel de reconnaissance » de Phase A Discovery** (faire dire au client « oui, c'est comme nous ») ; benchmark Best Practice industriel mappé à Stage 3 ; les 7 sample cases complets sont les modèles du rapport Phase B |
| 📖 **Références / remerciements** | [`../90_References/`](../90_References/) §2 remerciements | Sources de LLM Apps Case Index : `Shubhamsaboo/awesome-llm-apps` (Apache-2.0) + `patchy631/ai-engineering-hub` (MIT), appreciation cards complètes dans [`../90_References/README.md`](../90_References/README.md) §2.4 ; ClawTeam Walkthrough de `HKUDS/ClawTeam` (MIT) |
