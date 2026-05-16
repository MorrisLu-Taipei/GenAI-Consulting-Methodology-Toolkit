# Résumé Exécutif : Toute la Méthodologie en 5 Minutes (10 Minutes pour la Vue Complète)

> 🌐 中文 / Chinese : [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) ｜ English : [EXECUTIVE_SUMMARY_EN.md](EXECUTIVE_SUMMARY_EN.md)
>
> **Version 5 minutes** : lisez §1 « Sur Une Page » + §2 « Modèle Central » — cela suffit.
> **Version 10 minutes** : ajoutez §3-§7 (livre vivant, théorie, cours, conseil, livrables, co-lecture, prochaines étapes).
> Cliquez dans les fichiers liés seulement quand vous voulez approfondir.

---

## 1. Sur Une Page : Ce qu'elle résout

Beaucoup d'entreprises adoptent l'IA en « **sautant directement aux outils** » — acheter ChatGPT, essayer n8n, vouloir construire des Agents. Le résultat : les employés ne savent pas s'en servir, les processus ne sont pas connectés, les données ne sont pas gouvernées, les PoC ne peuvent pas être validés, et la direction n'a aucune idée de la maturité réelle de l'IA de l'entreprise.

Cette méthodologie transforme « **l'usage IA dispersé** » en une « **capacité organisationnelle reproductible, gouvernable, mesurable et scalable** » — en utilisant une boucle fermée de **questionnaire + cours + conseil** pour amener une entreprise de **l'individu utilisant l'IA** jusqu'à **l'entreprise possédant une équipe IA**.

| Élément | En une phrase |
|---|---|
| **Outil de diagnostic** | Questionnaire 10 / 25 / 50 items → position L1-L5 objective + lacunes sur six dimensions |
| **Parcours d'éducation** | Cours sur 5 niveaux (OpenWebUI / Antigravity / n8n / Hermes / ClawTeam) + calibrage BARS |
| **Structure de conseil** | 8 étapes (Awareness → Acceptance Test) + contrat en 3 phases (A Diagnostic / B Stratégie / C Implémentation) |
| **Fondement académique** | 7 piliers théoriques (Rosemann / Cohen & Levinthal / Teece / Real Options / etc.) |
| **Support porteur** | **AI-Native Living Book** — une méthodologie vraiment *vivante*, co-lisible directement avec un AI IDE |

---

## 2. Modèle Central : Les Deux Axes de L1-L5

L1-L5 n'est pas « cinq outils » — c'est un chemin de maturité connecté par **deux axes** :

| Axe | Plage | Pilote | Couches | Outils |
|---|---|---|---|---|
| **Axe d'échelle** | L1 → L2 → L3 | **Humains** utilisent l'IA, **humains** supervisent l'IA | individu → département → inter-départemental / entreprise entière | OpenWebUI / Antigravity / n8n |
| **Axe d'autonomie IA** | L4 → L5 | **IA** fonctionne en autonomie ; humains se retirent en **gouverneur** | entité IA → équipe IA | Hermes Agent / ClawTeam |

**Frontière critique = L3 → L4** : passer de « les humains pilotent le travail » à « l'IA pilote le travail ». Même à L4-L5, **le cadre de gouvernance reste construit par les humains, qui conservent la supervision** — ce que l'IA fait en autonomie, c'est l'« exécution opérationnelle », pas la « décision de gouvernance ».

➜ Histoire complète : [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0

---

## 3. AI-Native Living Book — Pourquoi ce Livre est *Vivant*

Cette méthodologie n'est pas un PDF / PPT / SOP — **c'est un livre vraiment *vivant*** :

| Génération | Forme | Limitation |
|---|---|---|
| Gén 1 — Livres imprimés | Papier | **Statique** — ne peut qu'être lu, ne répond pas |
| Gén 2 — Livres interactifs | Web / Wiki | **Interface vivante, contenu non** — ne suggère encore rien proactivement |
| **Gén 3 — AI-Native Books** (ce repo) | Markdown + AI IDE | **Vraiment vivant** — vous laisse demander, vous répond, pense avec vous, exécute des diagnostics / rédige des rapports / simule des scénarios selon la situation de votre entreprise |

**Modèle d'opération** : `git clone` → ouvrir avec un AI IDE (Antigravity / Claude Code / Codex) → l'IA lit le livre entier automatiquement → se positionne comme **tuteur de co-lecture** pour cette méthodologie → vous conversez, demandez et appliquez directement.

➜ Discussion complète : [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md)

### Trois moteurs IA, chacun spécialisé différemment

| Moteur | Rôle | Sa spécialité | Workflows |
|---|---|---|---|
| 🟦 **Antigravity** | Consultant de première ligne | Dialoguer avec les clients, exécuter les questionnaires, rédiger les rapports | `/diagnose`, `/generate-report` |
| 🟪 **Codex CLI** | Auditeur de la méthodologie | Tests inter-fichiers, red-team review, contrôle de versions, réparation | `/evidence-audit`, `/red-team-review`, `/bump-version` et 7 autres |
| 🟨 **Claude Code** | Partenaire de réflexion inter-fichiers | Synthèse profonde, débat multi-perspectives, simulation, forks client | `/simulate-engagement`, `/devil-pair-debate`, `/methodology-fork` et 7 autres |

➜ Auto-description des trois moteurs : [`../07_AI_Contributions/`](../07_AI_Contributions/) ｜ Guide d'installation : root [`../README_FR.md`](../README_FR.md) §🚀

---

## 4. Fondement Académique : 7 Piliers Théoriques

Cette méthodologie n'est pas ad-hoc. Chaque design clé **renvoie à une théorie classique** — la réponse standard quand l'académie, les régulateurs ou le conseil demandent « quelle est la base théorique ? » :

| # | Théorie | Fondateur | Rôle dans cette méthodologie |
|---|---|---|---|
| 1 | **Capability Maturity** | Rosemann (QUT) / CMMI | Le fondement scolaire pour la maturité L1-L5 |
| 2 | **Absorptive Capacity** | Cohen & Levinthal (1990) | Explique pourquoi certaines entreprises restent bloquées à L1 — manque de connaissance préalable |
| 3 | **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | Conception To-Be Étape 7 : quelles tâches doivent atteindre L4, lesquelles doivent rester à L2 |
| 4 | **Dynamic Capabilities** | Teece (1997, 2007) | sense / seize / transform — pourquoi la gouvernance IA est une « capacité », pas une « policy » |
| 5 | **Sociotechnical Systems & Trust in AI** | Bostrom (1977) / Dietvorst (2015) / Glikson (2020) | Pourquoi L4-L5 doivent garder HITL — les humains ne font pas confiance aveuglément à l'IA pure |
| 6 | **Real Options Theory** | Dixit & Pindyck (1994) / McGrath (1997) | Pourquoi Phase 1 avec NPV ≈ 0 vaut quand même l'investissement — vous achetez l'option d'expansion |
| 7 | **Executable Knowledge Artifact** | Knuth (1984) Literate Programming + extensions modernes | Pourquoi cette méthodologie est Markdown + co-lecture AI IDE au lieu de PDF |

➜ Discussion théorique complète (avec citations) : [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md)
➜ Patterns d'échec (où la théorie prédit l'échec) : [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md)
➜ Conception Pilot Study (étude empirique 18-24 mois) : [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md)

---

## 5. Éducation : Le Curriculum L1-L5 Complet

Chaque niveau a ses **propres matériels de cours + livrables vérifiables + acceptation Stage Gate** :

| Niveau | Nom | Outil | Plan de cours |
|---|---|---|---|
| L1 | Controlled AI Access | OpenWebUI | [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) |
| L3 | Workflow Automation | n8n + Tiger AI Skill Pack | [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) |
| L4 | Autonomous Agent | Hermes Agent + Wiki | [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) |
| L5 | Multi-Agent Organization | ClawTeam | (L5 inclus dans [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)) |

**Principe de conception** : les clients ne doivent pas faire tout L1-L5 d'un coup. Utilisez le questionnaire pour trouver **la couche qui produit les livrables les plus immédiats**, puis bâtissez au-dessus. Le mix de cours est déterminé par le profil d'entreprise, le secteur, le mode de déploiement (cloud / hybride / on-prem) et les exigences de risque.

➜ Package de cours complet : [`../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
➜ Calibrage de scoring (éviter la subjectivité) : [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) BARS

---

## 6. Conseil : 8 Étapes + Modèle de Contrat 3 Phases

### 6.1 Les Huit Étapes

| # | Étape | Action principale |
|---|---|---|
| 1 | **Awareness** | Établir la conscience IA et la vision du client |
| 2 | **Reference Model** | Guider le client pour signer le radar Ideal Practice |
| 3 | **Discovery** | Collecter l'état As-Is, le Shadow IT, l'inventaire système |
| 4 | **Gap Analysis** | Comparer Ideal Practice vs As-Is ; identifier les écarts à fort impact |
| 5 | **Stakeholder Mapping** | Identifier Sponsor, AI Champion, RH, Compliance |
| 6 | **Diagnosis** | Analyse inter-couche (incl. ancrage sur les 7 piliers théoriques) |
| 7 | **To-Be Design** | Utiliser TTF / Real Options pour concevoir une Roadmap par paliers |
| 8 | **Acceptance Test** | Sign-off Stage Gate + revue radar trimestrielle |

### 6.2 Contrat en Trois Phases

| Phase | Durée | Livrable principal |
|---|---|---|
| **Phase A — Diagnostic** | 2 semaines | Rapport de diagnostic intermédiaire + Ideal Practice signé |
| **Phase B — Stratégie** | 4 semaines | Rapport de conseil complet 14 chapitres + Roadmap 24 mois + ROI + recommandations de gouvernance |
| **Phase C — Implémentation** | 24 mois | Implémentation par phases + revue radar trimestrielle + évolution continue |

➜ Histoire complète 8 étapes (avec exemples de dialogue) : [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md)
➜ Modèle de rapport de conseil : [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)
➜ Modèles de toolkit de conseil : [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md)
➜ Package de livraison & acceptation : [`../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)

---

## 7. Livrables Vérifiables : Ce que Chaque Niveau Laisse

Le « cours » de chaque niveau ne se termine pas quand la conférence finit — il laisse une evidence auditable :

| Niveau | Livrables principaux | Evidence |
|---|---|---|
| L1 | Espace chat personnel, Prompt Library | Tableau des comptes, tableau des permissions, logs de login, exemples de Prompt |
| L2 | Skill Library, artifacts Agentic | Documents Skill, cas de test, historique de versions, exemples de sortie |
| L3 | n8n Workflow PoC, Sub-workflow Library, Data Tables | Logs d'exécution, logs de retry, captures d'intégration système |
| L4 | Agent vérifiable, briefings, task cards | Agent log, versions Wiki, records de sign-off HITL |
| L5 | Fiches de rôles Agent Team, flow de collaboration, résultats inter-départementaux | Team run log, records de handover, records de gouvernance |
| **Niveau conseil** | Rapport de diagnostic 14 chapitres, Roadmap 30/60/90 jours, ROI, recommandations de gouvernance | Records sign-off Stage Gate, revue radar trimestrielle |

➜ Livrables complets + matrice evidence : [`../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)

---

## 8. Comment Utiliser ce Livre (5 Chemins d'Entrée par Rôle)

| Vous êtes | Commencer ici (20 min → 1 h) |
|---|---|
| **CEO / propriétaire / proche voulant saisir la méthodologie** | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) — histoire de Ming |
| **Consultant / apprenant** | [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) — flow complet 8 étapes |
| **Conseil / régulation / académique** | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — argumentation scientifique |
| **IT entreprise / consultant transfuge** | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — alignement avec McKinsey/BCG/TOGAF/Gartner |
| **Chercheur en méthodologie / académique AI Pedagogy** | [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) — pourquoi c'est une nouvelle forme de méthodologie |

---

## 9. Index de Référence Rapide

### 9.1 Théorie Académique & Modes d'Échec

- [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — discussion complète des 7 piliers théoriques
- [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) — 14 modes d'échec (prédits par la théorie)
- [`../90_References/AI_GOVERNANCE_ALIGNMENT.md`](../90_References/AI_GOVERNANCE_ALIGNMENT.md) — alignement avec NIST AI RMF / EU AI Act / ISO 42001
- [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) — conception étude empirique 18-24 mois

### 9.2 Éducation & Évaluation

- [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) — questionnaire 10/25/50 items (plain-language)
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL.md) — modèle de scoring
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) — calibrage BARS (éviter la subjectivité)
- [`../02_Course_Design/`](../02_Course_Design/) — plans de cours L1-L5 complets

### 9.3 Livraison de Conseil

- [`../03_Consulting_Report/`](../03_Consulting_Report/) — rapport de conseil + modèles de toolkit
- [`../04_Scenarios/`](../04_Scenarios/) — 7 cas de scénarios sectoriels (fabrication / hôpital / marketing / B2B / financier / gouvernement / éducation)
- [`../05_Sales/`](../05_Sales/) — argumentaire de vente + FAQ
- [`../06_Delivery/`](../06_Delivery/) — package de livraison + critères d'acceptation + Engagement Lifecycle

### 9.4 Auto-Divulgation des Trois Moteurs

- [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) — README co-édité par les trois moteurs + §3 discipline de co-rédaction
- [`../07_AI_Contributions/ANTIGRAVITY.md`](../07_AI_Contributions/ANTIGRAVITY.md) ｜ [`CODEX.md`](../07_AI_Contributions/CODEX.md) ｜ [`CLAUDE_CODE.md`](../07_AI_Contributions/CLAUDE_CODE.md)
- [`../CHANGELOG.md`](../CHANGELOG.md) — changelog co-édité par les trois moteurs

### 9.5 Matériel Source

- [`../90_References/@AI-MD-PUBIC.pdf`](../90_References/@AI-MD-PUBIC.pdf) — PDF méthodologie original
- [`../90_References/MD-Map.png`](../90_References/MD-Map.png) — AI Maturity Map
- [`../90_References/Metholodgy.png`](../90_References/Metholodgy.png) — diagramme Eight-Stage Transformation Guide
- [`../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) — notes d'apprentissage vidéo
- [`../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

---

## 10. Prochaines Étapes : 3 Chemins Suggérés

| Votre besoin | Prochaine étape recommandée |
|---|---|
| **Construire le modèle mental global** | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) (incl. §3.0, l'histoire complète des deux axes) |
| **Découvrir à quel niveau est votre entreprise** | Le diagnostic rapide 10 items dans [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) |
| **Lire ce livre directement avec l'IA** | Ouvrir ce repo avec un AI IDE → lire d'abord root [`../README_FR.md`](../README_FR.md) §🚀 Guide d'installation des trois moteurs et lancer un moteur |

---

> ⚠️ **Déclaration d'intégrité académique** : Tous les cas nommés dans ce repo (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 fichiers SAMPLE_CLIENT_CASE) et tous les personnages principaux (p. ex., « Ming » et « MingChang Packaging ») sont **des exemples fictifs générés par IA**, PAS des données clients réelles. Tous les chiffres (temps, ROI, person-month, budget, KPI) sont **uniquement illustratifs** et **ne doivent PAS être utilisés pour le marketing externe, des engagements contractuels ou des preuves empiriques académiques**. Les cas longitudinaux réels remplaceront ceux-ci seulement après l'étude empirique 18-24 mois décrite dans [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md).
>
> **Propriété de l'architecture** : L'architecture méthodologique dans ce repo est conçue par l'auteur humain **Morris Lu (Tiger AI)**. Les trois moteurs IA (Antigravity / Codex / Claude Code) sont des outils qui **exécutent, complètent, étendent et auditent**. Voir [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0.
