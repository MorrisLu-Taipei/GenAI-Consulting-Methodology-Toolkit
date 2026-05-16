# 00 Overview — Vue d'Ensemble du Programme & Point d'Entrée

> 🌐 中文 / Chinese : [README.md](README.md) ｜ English : [README_EN.md](README_EN.md)

## 1. Objectif de ce Répertoire

Ce répertoire est le **point d'entrée unique** de l'ensemble du **AI Consulting Methodology Toolkit**. Il ne contient ni « outils » ni « livrables », seulement deux choses : **l'histoire de la méthodologie** et **le statut de la méthodologie**.

Quiconque rencontre ce repo pour la première fois — consultants apprenant la méthode, clients évaluant l'achat, nouveaux collègues en onboarding, reviewers auditant — devrait commencer ici. Construisez d'abord ici la compréhension globale (« qu'est-ce que la méthodologie, pourquoi conçue ainsi, où en sommes-nous »), puis entrez dans les répertoires fonctionnels `01`-`06`, afin de ne pas perdre la forêt à cause des arbres.

Le problème que ce répertoire résout : **sans entrée et statut clairs, les utilisateurs se perdent, abusent de la méthodologie, et ne savent pas ce qui est terminé ou en cours.**

## 2. Position dans la Méthodologie

| Axe | Mapping |
| --- | --- |
| Flux de service en 3 phases | Ne correspond pas à une seule phase ; une **carte aérienne** sur « Diagnose → Build → Deliver » |
| Structure de conseil en 8 étapes | Ne correspond pas à une seule étape ; une **vue d'ensemble** des 8 étapes |
| Maturité L1-L5 | Ne correspond pas à un seul niveau ; une **vue d'ensemble** de L1-L5 |
| Engagement Lifecycle | Ne correspond pas à une seule phase ; une **explication du point de départ** de tout le cycle |

> Positionnement logique : `00_Overview` répond à « **quoi et pourquoi** » ; `01`-`06` répond à « **comment** » ; `90_References` répond à « **base et citations** ».

## 3. Objectifs & Bénéfices

| Objectif | Bénéfice |
| --- | --- |
| Faire comprendre le squelette méthodologique aux nouveaux lecteurs en 5-10 min | Raccourcir l'onboarding ; réduire les mauvaises utilisations |
| Raconter le wertversprechen en langage client | Sales peut prendre directement la story pour un briefing client de 30 min |
| Maintenir un fichier de statut projet faisant autorité | Tout le monde peut vérifier « où nous en sommes, prochaine étape » — pas de passation orale |
| Relier la relation entre `01`-`06` et `90` | Les utilisateurs connaissent le rôle et l'ordre de chaque répertoire |

**Si ce répertoire est sauté** : les utilisateurs sautent directement dans les répertoires fonctionnels, sans comprendre « pourquoi ce répertoire existe ou comment il se connecte aux autres » — résultat : outils utilisés isolément, méthodologie devient un tas de fichiers dispersés.

## 4. Workflow & Logique

```text
Nouveau lecteur / client
   → Lire AI_TRANSFORMATION_STORY_AND_STRUCTURE.md (pourquoi + comment ça marche + produit)
   → Construire le modèle mental global « L1-L5 + 8 étapes + 3 phases »
   → Passer à 01_Assessment pour le diagnostic réel

Consultant / collègue / reviewer
   → Lire TODO_WBS.md (statut projet, changelog, prochains candidats, journal de travail)
   → Comprendre la situation avant d'agir
```

| Étape | Qui | Quand | Input | Output |
| --- | --- | --- | --- | --- |
| Lire la story | Consultant / client / nouveau | Premier contact avec le repo | aucun | Compréhension globale de la méthodologie |
| Briefer le client | Sales / consultant | Première réunion pré-engagement | Story | Client prêt à entrer en diagnostic |
| Consulter le statut du projet | Consultant / collègue / reviewer | Avant reprise / review | aucun | Situation actuelle + prochaine étape |
| Mettre à jour le statut | Consultant / AI responsable | Après chaque batch | Travail terminé | `TODO_WBS.md` mis à jour |

> Logique : la story est « externe » (pour clients + nouveaux) ; `TODO_WBS.md` est « interne » (pour exécutants). Externe + interne forment l'entrée complète.

## 5. Descriptions de Fichiers

### `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`

Story et structure de chapitres orientées client. Pas un document technique mais une **narration** — raconte « pourquoi les entreprises ont besoin de transformation IA, comment la méthodologie fonctionne étape par étape, ce que chaque étape produit d'acceptable » en une histoire cohérente que le client comprend. Inclut : positionnement de la solution, parcours en 3 phases, mapping L1-L5 ↔ outils, imagination future, propositions de valeur par rôle (CEO/COO/CIO/IT/RH/chef de département), §6 définition complète des 8 étapes + scénario 6 semaines. Utilisable directement dans la première réunion client.

### `EXECUTIVE_SUMMARY.md`

Toute la méthodologie en 5 minutes sur une page. Pour les cadres qui n'ont pas le temps des détails.

### `CLIENT_JOURNEY_STORY.md` 🆕

**L'histoire de Ming** — une story de scénario par laquelle CEO / conseil / famille comprennent la méthodologie en 20 minutes. Industrie de packaging semi-conducteur de 700 personnes en 24 mois de transformation — zéro tableau d'outils, zéro jargon. Utilisable pour communication externe, premier contact client, entretien de nouveau collaborateur.

### `EIGHT_STAGE_FLOW_STORY.md` 🆕

**Story de référence des 8 étapes** : modèle de contrat 3 phases (Phase A Diagnostic 2W + Phase B Stratégie 4W + Phase C Implémentation 24M) + rapport intermédiaire + revue radar trimestrielle comme boucle fermée complète. Lecture obligatoire pour la formation interne des consultants.

### `METHODOLOGY_SCIENTIFIC_LOGIC.md` 🆕

**Capacité de débat scientifique de la méthodologie** : valide avec les 5 critères de la méthode scientifique (observable, quantifiable, reproductible, falsifiable, auditable) pourquoi les 8 étapes résistent au questionnement client / conseil / régulateur. Obligatoire pour soumission académique, lobby politique, review du conseil.

### `INDUSTRY_FRAMEWORK_ALIGNMENT.md` 🆕

**Carte d'alignement avec frameworks industrie** : 8 étapes vs McKinsey / BCG / Bain / Deloitte / Accenture / PwC ; architecture 4 couches vs TOGAF / Zachman / Dragon1 ; L1-L5 vs Gartner / MIT / Forrester AI Maturity. Réponse à la question client « cela entre-t-il en conflit avec notre méthodologie existante ? »

### `AI_NATIVE_LIVING_BOOK.md` 🆕

**Discussion d'innovation sur le support de la méthodologie** : positionne cette méthodologie comme **AI-native living book** (un système de connaissance directement exécutable par AI IDE), pas seulement PDF / PPT. Inclut classification académique (executable knowledge artifact, AI-mediated methodology, interactive consulting playbook), conception à 3 couches (Repo as Book / Agent as Tutor / Methodology as Executable Artifact), 4 principes de contrôle des risques (AI ≠ consultant, evidence requise, AGENTS.md versionné, output AI marqué). Obligatoire pour soumission académique / différenciation méthodologique.

### `ACADEMIC_THEORETICAL_FOUNDATIONS.md` 🆕

**Énoncé unifié des 7 piliers théoriques** : Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Task-Technology Fit (Goodhue & Thompson 1995) + Dynamic Capabilities (Teece 1997/2007) + Sociotechnical Systems & Trust in AI (Bostrom 1977/Dietvorst 2015/Glikson 2020) + Real Options (Dixit & Pindyck 1994/McGrath 1997) + Executable Knowledge Artifact (Knuth 1984). Par théorie : résumé + fondateur + contribution à Tiger AI + position de mapping + citations. La réponse unique quand académie / régulateur / conseil demandent « quelle est la base théorique ».

### `../01_Assessment/BARS_RUBRICS.md` 🆕 (durcissement académique)

**Behaviorally Anchored Rating Scales** : tableau d'**ancres comportementales** 6 dimensions × 0-4 points (selon Smith & Kendall 1963). Chaque score a un comportement observable concret, **évite le scoring subjectif du consultant**, améliore l'inter-rater reliability. Aligné avec l'objectif Pilot Study Cohen's κ ≥ 0.60. Le mécanisme central pour que deux consultants donnent des scores proches à la même entreprise.

### `TODO_WBS.md`

Le **fichier de statut faisant autorité** de ce repo, l'unique source crédible pour « où nous en sommes ». Contient : aperçu WBS (items × priorité × statut), liste de fichiers terminés, détail des items terminés, TODOs ouverts, recommandation pour le prochain round, **changelog (par batch + hash commit)**, aperçu de statut actuel, **journal quotidien**. À lire avant toute reprise par consultant, review reviewer, ou continuation AI. À mettre à jour après chaque batch.

### `*_EN.md`

Versions anglaises sibling des fichiers ci-dessus, contenu correspondant aux versions chinoises.

## 6. Mapping vers Autres Répertoires

| Répertoire | Relation avec ce répertoire | Flux de données |
| --- | --- | --- |
| `01_Assessment` | La phase « Diagnostic » de la story est réalisée ici | `00` story → `01` outils de diagnostic |
| `02_Course_Design` | La phase « Build » de la story est réalisée ici | `00` story → `02` cours |
| `03_Consulting_Report` | La phase « Deliver » de la story est réalisée ici | `00` story → `03` rapport de conseil |
| `04_Scenarios` | Fournit scénarios clients et cas pour la story | `04` cas ↔ `00` story |
| `05_Sales` | Transforme la story en matériel vendable | `00` story → `05` matériel sales |
| `06_Delivery` | Transforme la méthodologie en business livrable et opérable | `00` story → `06` livraison & opérations |
| `90_References` | Base originale de la méthodologie + licences citations tierces | `90` base → soutient `00`-`06` |

## 7. Scénarios d'Usage Communs

- **Sales invite un client** : utilise le parcours 3 phases et le wertversprechen de `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md` pour un briefing méthodologie de 30 min.
- **Onboarding nouveau consultant** : d'abord lire la story pour la compréhension → puis `TODO_WBS.md` pour le statut actuel → puis répertoires selon le flux de données §6.
- **Reviewer audite** : lit directement changelog et journal de `TODO_WBS.md`, compare avec git log.
- **AI continue le travail** : lit « prochains candidats » et « journal » dans `TODO_WBS.md`, sait où reprendre.

---

## ⭐ Cross-Topic Quick References : 5 Thèmes Centraux, où Trouver

Toute la méthodologie a 5 artères principales traversant tous les répertoires. Comment ce répertoire se connecte à chacune :

| Cross-Topic | Lieu principal | Comment ce répertoire se connecte |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lecture trois moteurs** | Root [`README_FR.md`](../README_FR.md) §🌟 ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | **Ce répertoire EST le « point d'entrée story » du AI-Native Living Book** — [`AI_NATIVE_LIVING_BOOK.md`](AI_NATIVE_LIVING_BOOK.md) est la discussion complète ; les 4 fichiers concept de référence (CLIENT_JOURNEY / EIGHT_STAGE_FLOW / METHODOLOGY_SCIENTIFIC_LOGIC / INDUSTRY_FRAMEWORK_ALIGNMENT) vivent tous ici |
| 🎓 **Fondement académique (7 piliers)** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **La discussion unifiée des 7 piliers théoriques vit dans ce répertoire** : Rosemann / Cohen & Levinthal / TTF / Teece / Sociotechnical Trust / Real Options / Knuth |
| 📚 **Éducation L1-L5** | [`../02_Course_Design/`](../02_Course_Design/) | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 est le point d'entrée narratif de référence pour **L1-L5 comme deux axes** (axe d'échelle + axe d'autonomie IA) |
| 🔁 **Conseil / 8 étapes + Closed-Loop Phase A→B→C** | [`EIGHT_STAGE_FLOW_STORY.md`](EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **La story de la boucle fermée de conseil vit dans ce répertoire** — `EIGHT_STAGE_FLOW_STORY` §6 a le diagramme complet de la boucle (Phase A 2W + Phase B 4W + Phase C 24M + revue radar trimestrielle) |
| 📖 **Références / remerciements** | [`../90_References/`](../90_References/) §2 remerciements | Les stories de ce répertoire utilisent tout le matériel de `90_References` comme base (PDF / diagrammes / notes vidéo / citations théoriques) |
