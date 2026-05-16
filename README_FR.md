# GenAI Consulting Methodology Toolkit

Langue : [繁體中文](README.md) | [English](README_EN.md) | [ภาษาไทย](README_TH.md) | [Deutsch](README_DE.md) | Français | [Español](README_ES.md) | [日本語](README_JA.md) | [한국어](README_KR.md)

Boîte à outils méthodologique pour l'évaluation de la maturité et la mise en œuvre de la transformation IA en entreprise (Enterprise AI Transformation Maturity Assessment & Implementation Methodology Toolkit).

Auteur original : **Tiger AI Morris Lu 盧業興**  
Rôle : **n8n Taipei Ambassador / Doctorant à l'Institut de Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australie**

Résumé de licence : Ce projet est publié sous **[Apache License 2.0](LICENSE)**. Il peut être librement utilisé, copié, modifié, redistribué et commercialisé. Lors de la redistribution, conservez le texte de licence Apache 2.0 et l'attribution dans [`NOTICE`](NOTICE).

> **Seulement 5 minutes ?** Commencez par [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) — toute la méthodologie sur une page.

---

## 🌟 Ceci n'est pas un livre, c'est un AI-Native Living Book — un livre réellement « vivant »

Les livres ont évolué de génération en génération. Chaque génération a résolu un problème mais a laissé une lacune — **aucun n'a jamais été vraiment « vivant »** :

- **1re génération — Livres imprimés** : préservent la connaissance et la transmettent au lecteur suivant. Mais ils **ne peuvent qu'être lus, ils ne répondent pas**, ne peuvent répondre à vos questions, et ne connaissent pas votre entreprise — ce sont du **papier figé**.
- **2e génération — Livres interactifs** : une fois portés sur le web et les wikis, ils peuvent être recherchés, liés, commentés. Ils offrent une « **interaction** » de plus que les livres imprimés, mais ils **ne vous suggèrent rien proactivement** et n'analysent encore moins pour vous — toujours passifs : l'interface est vivante, le contenu ne l'est pas.
- **3e génération — AI-Native Books (ce repo) — un livre réellement « vivant »** : la méthodologie est écrite en Markdown puis ouverte avec un AI IDE — l'IA lit le livre entier automatiquement, **vous laisse poser des questions, vous répond, pense avec vous**, et **donne des recommandations personnalisées selon la situation réelle de votre entreprise, exécute des diagnostics, rédige des brouillons de rapports, simule des scénarios**. Le livre lui-même répond, s'étend et fait pousser de nouveaux chapitres avec vos questions.

Autrement dit : les livres imprimés transmettent la connaissance, les livres interactifs la rendent consultable, **les AI-Native Books font pour la première fois que « le livre » devient véritablement vivant — il devient un partenaire qui pense avec vous**. La décision finale revient toujours à l'humain, mais vous n'êtes plus seul face à une méthodologie statique.

> *Three generations of books: printed (read-only, dead) → interactive (search & link, still passive) → **AI-native (truly alive — advises, analyzes, simulates, and grows with your questions)**. Open with an AI IDE; AI becomes your reading partner, consulting assistant, and auditor.*

### 🔱 Trois moteurs IA aux spécialités différentes

Le même contenu prend des **personnalités complètement différentes** selon l'AI IDE choisi :

| Moteur | Rôle | Sa spécialité |
| --- | --- | --- |
| 🟦 **Antigravity** | Consultant de première ligne | Dialoguer avec les clients, exécuter les questionnaires, rédiger les brouillons de rapports |
| 🟪 **Codex CLI** | Auditeur de la méthodologie | Tests inter-fichiers, exercices red-team, contrôle de versions, réparation de liens cassés |
| 🟨 **Claude Code** | Partenaire de réflexion inter-fichiers | Synthèse profonde, débats multi-perspectives, simulations, forks pour clients spécifiques |

Les trois moteurs ne se remplacent pas mais **se partagent le travail** : le matin Antigravity pour les rendez-vous clients, l'après-midi Codex pour auditer les brouillons de rapports, le soir Claude Code pour simuler des scénarios. Chaque espace de travail est indépendant (`.agent/` / `.codex/` / `.claude/`) sans interférence mutuelle.

Auto-description détaillée de chaque moteur : voir [`07_AI_Contributions/`](07_AI_Contributions/) ; étapes d'installation : voir [Guide d'installation et de démarrage des trois moteurs IA](#-guide-dinstallation-et-de-démarrage-des-trois-moteurs-ia--three-ai-engines-setup-guide) ci-dessous.

### Ce que cela signifie pour chaque type de lecteur

- **CEO / Direction** : déposez ce repo dans ChatGPT / Claude / Gemini, et 10 minutes de questions-réponses donneront un premier verdict « À quel niveau se trouve mon entreprise ? Par où commencer ? »
- **Consultants / Apprenants** : ouvrir avec un AI IDE pour exécuter l'expérience de conseil conversationnelle complète — du diagnostic au rapport jusqu'à la feuille de route de mise en œuvre sur 24 mois.
- **Académiques / Chercheurs** : exécuter directement `/devil-pair-debate`, `/thought-experiment` pour débattre des présupposés de valeur de la méthodologie, appuyés sur 7 piliers théoriques et 28 classiques citables.
- **Régulation / Conformité** : exécuter `/evidence-audit`, `/generate-traceability` pour obtenir une chaîne de preuves auditables, alignée sur NIST AI RMF / EU AI Act / ISO 42001.

> ⚠️ **Divulgation honnête** : L'architecture globale de la méthodologie a été conçue par **Morris Lu (humain)**. Les trois moteurs IA sont uniquement des outils d'exécution, de complément et d'audit. Détails dans [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0. Tous les cas dans le livre sont des exemples simulés par IA à des fins pédagogiques — **pas de données clients réelles**.

---

## Ce que cette méthodologie résout

Beaucoup d'entreprises sautent directement aux outils en adoptant l'IA : aujourd'hui acheter ChatGPT, demain essayer n8n, la semaine prochaine vouloir faire un Agent. Problèmes typiques : les employés ne savent pas s'en servir, les processus ne sont pas connectés, les données ne sont pas gouvernées, les PoC ne peuvent pas être validés, et finalement la direction ne sait pas à quel niveau de maturité l'IA de l'entreprise se trouve.

La stratégie de cette boîte à outils : d'abord diagnostiquer la maturité IA actuelle de l'entreprise avec un questionnaire simple, puis concevoir le ratio de cours et le chemin d'adoption selon L1-L5. Les cours ne s'arrêtent pas après la formation — chaque niveau laisse des livrables vérifiables. Enfin, utiliser le processus de conseil en 8 étapes pour la transformation IA, produisant un rapport de diagnostic complet, une feuille de route, une vue ROI et des recommandations de gouvernance.

## Imaginer l'avenir avant le début du cours

Avant que les clients décident de suivre les cours L1-L5, ils doivent d'abord voir une image de l'avenir : non pas « nous allons apprendre cinq outils », mais « **comment le travail quotidien de l'entreprise va-t-il changer après le cours ?** »

L'intrigue : **l'échelle s'étend couche par couche, et finalement « les humains utilisent l'IA » fait grandir « l'IA travaille toute seule »** : **individu → département → inter-départemental/entreprise entière → super-assistant IA (entité) → équipe IA**. Imaginez un lundi matin dans trois mois :

- **L1 Controlled AI Access ─ Axe d'échelle · Individu** : **chaque employé individuellement** se connecte à OpenWebUI avec son propre compte, dispose de son espace de chat, de son historique et des permissions du département. Les commerciaux rédigent des e-mails clients, RH résume les formations, les managers produisent les points clés des réunions — tout commence du même point d'entrée IA contrôlé. **L'unité est « l'individu »**, l'IA est à côté de chaque personne.
- **L2 Knowledge Codification ─ Axe d'échelle · Département** : **l'unité monte au niveau « département »**. Les collaborateurs expérimentés ne sont plus seulement individuellement compétents ; dans les limites de la **responsabilité du département**, ils empaquettent rédaction, rapports, réponses au service client, interprétations de SOP et méthodes de développement en Skills réutilisables. Les nouveaux et les autres membres du département utilisent la même méthode ; la qualité de sortie **du département entier** devient cohérente.
- **L3 Workflow Automation ─ Axe d'échelle · inter-départemental / entreprise entière** : **l'unité monte encore à « inter-départemental, entreprise entière »**. n8n connecte les Skills de chaque département avec les systèmes (Gmail, Sheets, Notion, CRM, API, ERP). Un e-mail de réclamation entrant peut **traverser plusieurs départements — ventes, service client, CRM, manager** automatiquement — le système interroge le CRM, met à jour les formulaires, crée des tâches, génère un résumé pour le manager ; l'humain ne fait que juger et approuver. L'IA entre maintenant dans les **processus de toute l'entreprise**.
- **L4 Autonomous Agent ─ Axe d'autonomie IA · Super-assistant (entité IA)** : **au-delà de la « troupe humaine », une entité IA supplémentaire se développe**. Hermes Agent lit chaque jour les tâches, documents, résultats de Workflow et la mémoire Wiki, produisant briefings, listes de suivi et points de décision nécessitant HITL (Human-in-the-Loop, revue humaine dans la boucle). L'entreprise possède maintenant une **entité IA de classe « knowledge-grade » vérifiable**, comme si elle embauchait un super-assistant entièrement automatique en plus.
- **L5 Multi-Agent Organization ─ Axe d'autonomie IA · Équipe IA** : **plusieurs entités L4 sont organisées en une « équipe IA »**. ClawTeam organise des Agents spécialisés — marketing, produit, service client, finance, opérations — en une division fonctionnelle du travail, collaborant pour lancer un nouveau produit, améliorer la qualité, améliorer le service patient ou gérer les clients. L'entreprise dispose **simultanément de deux équipes : équipe humaine + équipe IA**.

Cette histoire doit être racontée avant le début du cours. Une fois que le client comprend « **comment l'échelle s'étend couche par couche, comment l'IA passe d'outil à main-d'œuvre numérique** », il peut revenir comprendre pourquoi un diagnostic par questionnaire est nécessaire, pourquoi le cours est divisé en L1-L5 et pourquoi chaque niveau a besoin de livrables, evidence et Stage Gates.

> ⚠️ Une explication plus détaillée des deux axes (pourquoi L3 → L4 est la frontière critique, pourquoi la gouvernance reste toujours humaine) est disponible plus bas dans [§Les deux axes de L1-L5](#les-deux-axes-de-l1-l5).

## Carte de maturité IA

![AI Maturity Map](90_References/MD-Map.png)

## Vue d'ensemble de la méthodologie

![Enterprise Consulting Methodology: Eight-Stage Transformation Guide](90_References/Metholodgy.png)

## Fil narratif principal

```text
Questionnaire de maturité IA
→ Profil d'entreprise, contexte sectoriel, mode de déploiement
→ Conception du ratio de cours L1-L5
→ L1 Comptes OpenWebUI entreprise et espaces de chat personnels activés
→ L2 Formation Skill avec Antigravity / Claude Code / Codex
→ L3 n8n connecte Gmail, Sheets, Notion, CRM, API, ERP et autres systèmes
→ L4 Hermes Agent pour un travail d'Agent autonome vérifiable
→ L5 ClawTeam pour la collaboration en Agentic Team
→ Cas de scénarios, Evidence, Stage Gates
→ Diagnostic conseil de transformation IA en 8 étapes
→ Rapport de diagnostic de transformation IA, feuille de route, ROI, recommandations de gouvernance
```

## Modèle de maturité L1-L5

| Niveau | Nom | Outil / Plateforme | Axe | Positionnement entreprise |
| --- | --- | --- | --- | --- |
| L1 | Controlled AI Access | OpenWebUI | Axe d'échelle · Individu | Établit le point d'entrée de la conversation IA dans l'entreprise, chaque employé a son propre compte, espace de chat et frontières de permission |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | Axe d'échelle · Département | Avec la responsabilité du département comme unité, empaqueter connaissance personnelle, prompts, documents et méthodes de travail en Skills réutilisables |
| L3 | Workflow Automation | n8n | Axe d'échelle · inter-départemental / entreprise entière | Connecter les Skills inter-départementaux et coupler avec e-mail, Sheets, Notes, CRM, API, ERP et autres systèmes, faisant entrer l'IA dans l'automatisation de toute l'entreprise |
| L4 | Autonomous Agent | Hermes Agent | Axe d'autonomie IA · Super-assistant | Combine carte de compétences Wiki, outils IA, Workflow, planification automatique et apprentissage autonome en un super-assistant Agent IA entièrement autonome vérifiable |
| L5 | Multi-Agent Organization | ClawTeam | Axe d'autonomie IA · Équipe IA | Plusieurs Agents spécialisés forment une division fonctionnelle du travail, collaborent à des tâches d'entreprise inter-départementales et inter-processus en tant qu'équipe IA |

### Les deux axes de L1-L5

L1-L5 ne sont pas « cinq outils » mais un chemin de maturité connecté par **deux axes** :

- **L1 → L2 → L3 : Axe d'échelle (les humains utilisent / supervisent l'IA)**. Ces trois couches sont la phase « humain dans la boucle, humain utilise l'IA, humain supervise l'IA », passant à l'échelle suivant la taille de l'organisation — **L1 individu** (chaque employé utilise l'IA pour soi) → **L2 département** (avec la responsabilité du département comme unité, empaqueter la connaissance personnelle en Skills réutilisables) → **L3 inter-départemental / entreprise entière** (connecter les Skills inter-départementaux, coupler les systèmes, l'IA entre dans l'automatisation de toute l'entreprise).
- **L4 → L5 : Axe d'autonomie IA (l'IA fonctionne en autonomie sans supervision humaine en temps réel)**. Ces deux couches sont les entités IA que l'entreprise « **fait pousser en plus** » de la troupe humaine — **L4 super-assistant IA** (entité Agent IA entièrement autonome) → **L5 équipe IA** (plusieurs Agents spécialisés en division fonctionnelle du travail).

> Frontière critique : **L1-L3 c'est « l'humain assiste / supervise l'IA », l'IA est un outil ; L4-L5 c'est « l'IA fonctionne en autonomie », l'IA est une main-d'œuvre numérique supplémentaire de l'entreprise.** Dans l'ordre d'adoption, L1-L3 amène d'abord les humains et l'organisation à niveau, L4-L5 fait ensuite pousser une IA autonome sur une base solide.
>
> Même en L4-L5, **le cadre de gouvernance est toujours construit par l'humain, qui conserve l'autorité de supervision** — ce que l'IA fait en autonomie c'est « l'exécution opérationnelle », non « la décision de gouvernance ». Chaque couche conserve HITL (Human-in-the-Loop) et les Stage Gates ; plus l'IA est autonome, plus le rôle de l'humain s'élève vers « gouverneur » — sans être remplacé.

## Comment valider chaque niveau

| Niveau | Input | Process | Output | Evidence | Stage Gate |
| --- | --- | --- | --- | --- | --- |
| L1 | Rôles des employés, tâches fréquentes, points de douleur IA, besoins de permission | Mettre en place OpenWebUI, comptes / groupes / permissions, espaces de chat, formation Prompt de base | Point d'entrée IA entreprise, liste de Prompts, liste de use cases | Tableau des comptes, tableau des permissions, logs de connexion, captures de l'espace chat, exemples de Prompt | Peut-on se connecter en sécurité, séparer les permissions et laisser des traces traçables ? |
| L2 | Prompts L1 fréquents, documents, SOPs, méthodes de travail personnelles | Avec Antigravity / Claude Code / Codex empaqueter la connaissance en Skills et artifacts réutilisables | Skill Library, Agentic artifacts, Workflow Blueprint | Documents Skill, cas de test, historique de versions, exemples de sortie | Les Skills peuvent-ils être réutilisés par d'autres et produire un output stable ? |
| L3 | Skills L2, blueprint de processus, inventaire système, permissions API/CRM/ERP/Sheet | Avec n8n construire workflows automatisés, Data Tables, Execution Logs, gestion d'erreurs | Workflow PoC, Sub-workflow Library, Data Tables, L4 Workflow Contract | Workflow n8n, execution logs, logs de retry, captures d'intégration | Le workflow fonctionne-t-il de façon stable sur données et systèmes réels ? |
| L4 | Workflow L3, Skill L2, Wiki entreprise, règles de tâches, points HITL | Avec Hermes Agent créer task cards, Wiki ingest/query/update, scheduling, appels d'outils et Gate 4A-4E | Agent vérifiable, briefings, logs de traitement, sign-offs | Agent log, versions Wiki, task cards, briefings, approbations humaines | L'Agent peut-il accomplir des tâches en autonomie dans des limites contrôlées et laisser des evidence ? |
| L5 | Plusieurs L4 Agents, tâches inter-départementales, responsabilités de rôles, règles de gouvernance | Avec ClawTeam constituer une Agentic Team, définir rôles, règles de collaboration, transferts et supervision | Agent Team, fiches de rôles, flow de collaboration, résultats inter-départementaux | Team run log, fiches de rôles, logs de transfert, documents de résultats, logs de gouvernance | L'Agent Team peut-il collaborer de façon stable et produire des résultats imputables ? |

## Principes de conception des cours

Le ratio de cours est déterminé par la maturité, le secteur, le mode de déploiement et les scénarios cibles du client. Toutes les entreprises ne doivent pas couvrir L1-L5 en une fois — trouver d'abord la couche qui peut produire des résultats livrables les plus immédiats, puis bâtir au-dessus.

| Dimension d'enquête | But |
| --- | --- |
| Profil de l'entreprise | Déterminer s'il s'agit de R&D-fabrication, de services marketing, d'institution de santé, d'opérations internes ou autre |
| Mode de déploiement | Cloud IA, hybride (cloud + on-prem) ou entièrement on-prem |
| Paysage système | Inventaire de Gmail, Sheets, Notion, CRM, API, ERP, bases de données, systèmes internes |
| Maturité des processus | Existence de SOPs, process owners, champs de données, gestion des exceptions |
| Exigences de risque | Évaluer sécurité, vie privée, conformité santé / fabrication / finance et besoins de sign-off humain |

## Structure du répertoire

| Répertoire | But |
| --- | --- |
| [`00_Overview`](00_Overview/) | Vue d'ensemble de la solution, fil narratif, WBS |
| [`01_Assessment`](01_Assessment/) | Questionnaire de maturité IA, modèle de scoring, livrables et matrice d'evidence |
| [`02_Course_Design`](02_Course_Design/) | Plans de cours L1-L5, profil d'entreprise, modes de déploiement, matrice de modules |
| [`03_Consulting_Report`](03_Consulting_Report/) | Modèle de rapport de diagnostic de transformation IA |
| [`04_Scenarios`](04_Scenarios/) | Scénarios clients, tableaux de contrôle, cas industrie, cas hôpital |
| [`05_Sales`](05_Sales/) | Proposition de valeur, argumentaire commercial, FAQ |
| [`06_Delivery`](06_Delivery/) | Package de livraison et critères d'acceptation |
| [`90_References`](90_References/) | PDF original, diagrammes méthodologiques, notes vidéo, citations |

## Cinq profils de lecteurs, par où commencer

| Vous êtes | Commencer par |
| --- | --- |
| **CEO / propriétaire / proche** — comprendre la méthodologie en 20 min | [`00_Overview/CLIENT_JOURNEY_STORY_EN.md`](00_Overview/CLIENT_JOURNEY_STORY_EN.md) — histoire de Ming |
| **Consultant / apprenant** — savoir comment se déroulent les 8 étapes, comment les contrats se découpent | [`00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) — flow complet |
| **Conseil d'administration / régulation / académique** — pourquoi cette méthodologie résiste au débat | [`00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — argumentation scientifique |
| **IT grande entreprise / consultant transfuge** — alignement avec McKinsey/BCG/TOGAF/Gartner | [`00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — carte d'alignement |
| **Cadre pressé** — seulement 5 minutes | [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) — résumé exécutif |
| **Chercheur en méthodologie / académique AI Pedagogy** — pourquoi est-ce une nouvelle forme de méthodologie | [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) — design AI-Native Living Book |
| **Académique / régulation / CA** — 7 piliers théoriques (Rosemann / Cohen & Levinthal / Teece / Real Options etc.) | [`00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — fondements théoriques académiques |
| **Consultant / calibration de scoring** — comment scorer 0-4 objectivement | [`01_Assessment/BARS_RUBRICS_EN.md`](01_Assessment/BARS_RUBRICS_EN.md) — BARS Behavioral Anchors |

## Ordre de lecture recommandé

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md)
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md)
4. [`01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)
5. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
6. [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md)
7. [`02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md)
8. [`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md)
9. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md)
10. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md)
11. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)
12. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)

## Livrables vérifiables

- Questionnaire de maturité IA et résultats de scoring
- Enquête de profil d'entreprise et de mode de déploiement
- Evidence d'achèvement des cours L1-L5
- Tableau des comptes / groupes / permissions OpenWebUI et logs d'activation des espaces de chat
- Skill Library et artifacts Antigravity / Claude Code / Codex
- n8n Workflow PoC, Execution Log, Data Tables, Sub-workflow Library
- Hermes Agent task cards, Wiki, logs ingest/query/update, briefings et Gate 4A-4E
- ClawTeam Agent Team fiches de rôles, logs de collaboration et documents de résultats
- Logs d'acceptation Stage Gate
- Rapport de diagnostic de transformation IA
- Feuille de route 30 / 60 / 90 jours

## Références

- [`90_References/@AI-MD-PUBIC.pdf`](90_References/@AI-MD-PUBIC.pdf)
- [`90_References/MD-Map.png`](90_References/MD-Map.png)
- [`90_References/Metholodgy.png`](90_References/Metholodgy.png)
- [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md)
- [`90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

## Remerciements

Remerciements particuliers à **Prof. Michael Rosemann**, Queensland University of Technology (QUT), Brisbane, Australie.  
Profil : <https://www.qut.edu.au/about/our-people/academic-profiles/m.rosemann>

Le fondement théorique de toute la méthodologie de conseil de ce repo provient des études de l'auteur à QUT et de l'inspiration et de l'enseignement de longue date du Prof. Michael Rosemann en **Business Process Management (BPM)**, **Capability Maturity Models** et **méthodologie d'innovation d'entreprise**.

Deux conceptions de cœur sont particulièrement influencées :

- **Structure de conseil en huit étapes** : correspond au diagnostic de processus, à l'évaluation des capacités, à la conception du chemin de transformation et à la mise en œuvre de la gouvernance.
- **Modèle de maturité IA L1-L5** : informé par la logique Capability Maturity et localisé en un cadre d'adoption IA à cinq couches pour les entreprises.

Déni de responsabilité : toute erreur, omission, adaptation locale ou extension au domaine de l'IA dans cette méthodologie relève de la responsabilité exclusive de l'auteur Tiger AI Morris Lu 盧業興 et ne représente pas les vues ou positions du Prof. Michael Rosemann ou de QUT.

## Licence et attribution

Ce projet est publié sous la licence **[Apache License 2.0](LICENSE)**. Vous pouvez librement l'utiliser, le copier, le modifier, l'adapter, le reproduire, le distribuer, l'enseigner, le livrer en conseil et le commercialiser.

Lors de la redistribution, adaptation, packaging commercial, utilisation dans des supports de cours, livrables de conseil ou documentation produit, conservez le texte de licence Apache 2.0 et l'attribution suivante de [`NOTICE`](NOTICE) :

```text
Original Author: Tiger AI Morris Lu 盧業興
Role: n8n Taipei Ambassador / PhD Student, Graduate Institute of Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australia
Source: https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit
```

Les noms de plateformes tierces, marques, vidéos, projets externes et contenus cités restent la propriété de leurs ayants droit respectifs. Ce repo n'utilise les données tierces qu'à des fins d'apprentissage, de citation, d'organisation et de référence pour la conception des cours.

---

## Faire vivre ce livre : lire avec l'IA

Le guide d'installation ci-dessous vous accompagne pour connecter le repo à un AI IDE. Avant de commencer, comprenez le modèle d'opération et une ligne rouge.

**Modèle d'opération en une phrase** : `git clone` ou télécharger le zip → ouvrir avec un AI IDE (Antigravity / Claude Code / Codex etc.) → l'IA lit [`AGENTS.md`](AGENTS.md) (et le `<ENGINE>.md` propre à chaque moteur) automatiquement et se positionne comme **tuteur de lecture commune de cette méthodologie**. Vous pouvez ensuite (1) lui poser n'importe quelle question sur la méthodologie, (2) lui demander d'appliquer la méthodologie à votre entreprise, (3) faire avec lui l'autodiagnostic L1-L5 et trouver l'étape suivante.

Discussion complète : [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md).

> ⚠️ **Déclaration d'intégrité académique / Academic Integrity Disclaimer**
>
> **Tous les cas nommés dans ce repo (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 SAMPLE_CLIENT_CASE) et personnages principaux (ex : « Ming » / « MingChang Packaging ») sont des exemples fictifs générés par IA**, PAS des données clients réelles.
> Tous les chiffres (temps, ROI, person-month, budget, KPI) sont **uniquement illustratifs** et **ne doivent pas être utilisés pour le marketing externe, des engagements contractuels ou des preuves empiriques académiques**.
> Les cas longitudinaux réels remplaceront ceux-ci seulement après l'étude empirique de 18-24 mois selon [`90_References/PILOT_STUDY_PROTOCOL_EN.md`](90_References/PILOT_STUDY_PROTOCOL_EN.md).
>
> **All named cases and story protagonists in this repo are AI-generated fictional examples**, NOT real client data.

## 🚀 Guide d'installation et de démarrage des trois moteurs IA / Three AI Engines Setup Guide

Les **rôles et la répartition** des trois moteurs ont été présentés plus haut dans « 🔱 Trois moteurs IA aux spécialités différentes ». Cette section se concentre sur **comment installer, comment démarrer, comment invoquer les workflows**. Les trois sous-sections sont indépendantes — choisissez le moteur que vous voulez utiliser et lisez uniquement cette section-là.

> ⚠️ **Selon [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0** : l'architecture méthodologique, L1-L5, les huit étapes et la répartition des trois moteurs sont tous des designs stratégiques proposés par **Morris Lu (humain)**. Les trois moteurs IA, sous la direction de Morris, **exécutent, complètent, étendent et auditent** — ils ne revendiquent pas la propriété de l'architecture méthodologique. L'auto-description détaillée de chaque moteur se trouve dans le fichier correspondant sous [`07_AI_Contributions/`](07_AI_Contributions/).

---

### 🟦 1. Utilisateurs Antigravity — Consultant interactif de première ligne

> Faites évoluer ce « livre vivant statique » directement vers votre « **Conversational Consulting App** ».

**Installation et utilisation :**

1. **Charger le projet** : `git clone` ou télécharger le zip du projet en local
2. **Lancer l'IDE** : ouvrir le dossier du projet avec Antigravity
3. **Auto-initialisation** : Antigravity lit [`ANTIGRAVITY.md`](ANTIGRAVITY.md) et [`SKILL.md`](SKILL.md) automatiquement et se positionne comme « **tuteur de lecture commune** »
4. **Exécuter les Workflows (Slash Commands)** : taper la commande dans le chat pour lancer l'interaction

**Commandes Antigravity courantes :**

- `/diagnose` ── lance un dialogue réaliste qui vous guide (ou votre client) à travers le diagnostic L1-L5 de maturité IA d'entreprise
- `/generate-report` ── verse les résultats du diagnostic et de la discussion précédente dans le modèle standard de rapport de conseil et produit un brouillon

Voir [`.agent/workflows/`](.agent/workflows/) et [`07_AI_Contributions/ANTIGRAVITY.md`](07_AI_Contributions/ANTIGRAVITY.md).

> Valeur principale d'Antigravity : transformer la méthodologie en une expérience de conseil que **les clients comprennent et peuvent immédiatement interagir avec**.

---

### 🟪 2. Utilisateurs Codex — Moteur d'ingénierie méthodologique

> Considérez ce repo comme un « **workspace d'ingénierie méthodologique** » — maintenez ce livre vivant AI-native comme un produit méthodologique **testable, auditable, traçable, réparable, releasable**.

**Installation et utilisation :**

1. **Charger le projet** : `git clone` ou télécharger le zip du projet en local
2. **Lancer Codex** : ouvrir le dossier du projet dans Codex
3. **Lire le fichier d'entrée Codex** : faire lire à Codex [`CODEX.md`](CODEX.md) et [`.codex/README.md`](.codex/README.md) d'abord
4. **Exécuter les workflows Codex** : taper le nom du workflow dans le chat ou demander explicitement à Codex de suivre le fichier correspondant

**Commandes Codex courantes (10) :**

| Catégorie | Commande | But |
| --- | --- | --- |
| Production | `/diagnose` | Pré-évaluation interactive de maturité IA |
| Production | `/generate-report` | Brouillon de rapport de diagnostic de conseil |
| Quality | `/evidence-audit` | Vérifier la chaîne d'evidence du rapport |
| Quality | `/consistency-review` | Vérification inter-documents de la cohérence L1-L5, Stage Gate, HITL, Evidence |
| Evolution | `/academic-upgrade` | Convertir les recommandations académiques en plan de réparation méthodologique |
| Evolution | `/harvest-insights` | Récolter les insights communs depuis plusieurs rapports de livraison |
| Defense | `/test-methodology` | Stress-tester la méthodologie sur des scénarios extrêmes |
| Defense | `/red-team-review` | Red-team review des brouillons de rapport de conseil |
| Audit | `/generate-traceability` | Produire la matrice de traçabilité questionnaire → maturité → evidence → rapport |
| DevOps | `/bump-version` | Suggérer un bump de version sémantique et un CHANGELOG |

**Mode d'invocation recommandé :**

```text
Veuillez suivre .codex/workflows/evidence-audit.md pour vérifier ce brouillon de rapport de conseil.
```

Voir [`.codex/workflows/`](.codex/workflows/) et [`07_AI_Contributions/CODEX.md`](07_AI_Contributions/CODEX.md).

> Valeur principale de Codex : donner à cette méthodologie un cycle de vie d'ingénierie « **testable, auditable, traçable, réparable, releasable** ».

---

### 🟨 3. Utilisateurs Claude Code — Moteur de réflexion stratégique inter-fichiers et d'expérimentation

> **Jouer / tester / démonter / heurter** la méthodologie une fois. Utiliser le contexte 1M de Claude Code + multi-persona parallèle + raisonnement abstrait inter-domaine pour **simuler, expérimenter, débattre, forker**.

**Installation et utilisation :**

1. **Charger le projet** : `git clone` ou télécharger le zip du projet en local
2. **Lancer Claude Code** : ouvrir le dossier du projet dans Claude Code CLI / IDE
3. **Lire le fichier d'entrée Claude Code** : faire lire à Claude Code [`CLAUDE.md`](CLAUDE.md) et [`.claude/README.md`](.claude/README.md) d'abord
4. **Exécuter les workflows Claude Code** : taper le nom du workflow dans le chat

**Commandes Claude Code courantes (10) :**

| Catégorie | Commande | But |
| --- | --- | --- |
| Tier 1 Tactical | `/deep-synthesize` | Synthèse profonde multi-fichiers (contexte 1M) |
| Tier 1 Tactical | `/theory-bridge` | Contexte client ↔ 7 piliers théoriques |
| Tier 1 Tactical | `/scenario-planning` | À partir de contraintes, produire 3 roadmaps contrastées + trade-offs |
| Tier 1 Tactical | `/socratic-challenge` | Questionnement socratique pour aiguiser la pensée de l'utilisateur |
| Tier 1 Tactical | `/cross-stage-trace` | Tracer l'impact downstream d'un changement unique |
| Tier 2 Original | `/simulate-engagement` | Exécuter un mandat de conseil complet de 6 semaines en 30 min (12+ livrables) |
| Tier 2 Original | `/parallel-perspectives` | 6 parties prenantes **simultanément** sur la même décision + carte de conflits |
| Tier 2 Original | `/thought-experiment` | Stress test contrefactuel de la méthodologie (« Et si l'EU AI Act interdisait L4 ? ») |
| Tier 2 Original | `/devil-pair-debate` | Débat adversarial Two-Claude + synthèse de juge |
| Tier 2 Original | `/methodology-fork` | Forker la méthodologie standard en variante client (Methodology-as-Code) |

**Mode d'invocation recommandé :**

```text
Veuillez suivre .claude/workflows/simulate-engagement.md pour simuler un mandat de conseil
de 6 semaines pour un client industriel de 500 personnes.
```

Voir [`.claude/workflows/`](.claude/workflows/) et [`07_AI_Contributions/CLAUDE_CODE.md`](07_AI_Contributions/CLAUDE_CODE.md).

> Valeur principale de Claude Code : faire évoluer la méthodologie d'« **un standard** » vers « **standard + N dérivés + simulations complètes + débats multi-perspectives** » — un livre vivant expérimentable.

---

### Suggestions de workflow trois moteurs / Three-Engine Workflow Suggestions

Rythme de collaboration fréquent en pratique :

```text
Phase A — Diagnostic client
  → Antigravity exécute /diagnose pour collecter l'état actuel
  → Claude Code exécute /theory-bridge pour le diagnostic théorique
  → Antigravity exécute /generate-report pour un brouillon de rapport intermédiaire
  → Codex exécute /evidence-audit sur la chaîne d'evidence
  → Codex exécute /consistency-review pour l'alignement inter-fichiers

Phase B — Conception stratégique
  → Claude Code exécute /scenario-planning pour 3 roadmaps
  → Claude Code exécute /parallel-perspectives pour 6 vues de parties prenantes
  → Codex exécute /red-team-review contre l'optimisme excessif
  → Claude Code exécute /devil-pair-debate pour débattre des présupposés de valeur

Phase C — Mise en œuvre et évolution
  → Codex exécute /generate-traceability pour des audits trimestriels
  → Claude Code exécute /thought-experiment pour des stress tests contrefactuels
  → Codex exécute /bump-version pour la maintenance des versions méthodologiques
  → Claude Code exécute /methodology-fork pour des dérivés destinés aux grands comptes
```

> Les workflows des trois moteurs ne sont pas exclusifs — **le point est que chaque moteur fasse ce qu'il fait le mieux**, et l'humain (consultant / client owner / sponsor) décide quand passer à un autre moteur.
