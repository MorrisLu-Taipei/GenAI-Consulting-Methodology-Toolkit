# 02 Course Design — Conception de Cours L1-L5

> 🌐 中文 / Chinese : [README.md](README.md) ｜ English : [README_EN.md](README_EN.md)

## 1. Objectif de ce Répertoire

Ce répertoire est la **deuxième phase : Build (Build)** du flux de service en 3 phases. Le diagnostic (`01`) vous dit « à quel niveau est le client, ce qui manque » ; ce répertoire contient **les cours concrets qui comblent l'écart**.

Le problème qu'il résout : **la transformation IA ne réussit pas par le seul achat d'outils ou des conférences — l'entreprise doit traverser L1-L5 étape par étape et produire des assets acceptables.** Ce répertoire fournit pour chaque niveau L1 à L5 des curricula complets : objectifs de cours, public, prérequis, contenu, exercices, devoirs, standards d'achèvement, Stage Gate. Chaque niveau produit des **livrables acceptables** (L1 Prompt Library, L2 Skill, L3 Workflow, L4 Agent, L5 Agent Team) — pas du « oublié après le cours ».

Qui utilise : formateurs, AI Champions, IT, apprenants de tous niveaux.

## 2. Position dans la Méthodologie

| Axe | Mapping |
| --- | --- |
| Flux de service 3 phases | **Build** — deuxième phase |
| Structure de conseil 8 étapes | **Étape 7 To-Be Design** (les cours sont la mise en œuvre concrète de la solution) |
| Maturité L1-L5 | Ce répertoire est le corps des cours qui « **font passer le client de son niveau actuel au suivant** » ; couvre L1-L5 **deux axes** |
| Engagement Lifecycle | **Delivery — Build** |

> Principe central 1 : **L1-L5 enchaîné — l'output du niveau inférieur est l'input du suivant.** Sans usage L1 généralisé, pas de Skills pour L2 ; sans Skills L2, les Workflows L3 sont des tuyaux vides ; sans Workflows L3, l'Agent L4 n'a pas d'outils ; sans Agents L4, l'équipe L5 n'a pas de membres. **Pas de saut de niveau.**
>
> Principe central 2 : **L1-L5 sont deux axes** — axe d'échelle (L1 individu → L2 département → L3 inter-départemental / entreprise entière, humain supervise IA) et axe d'autonomie IA (L4 super-assistant → L5 équipe IA, IA autonome, humain recule en gouverneur). Frontière critique à L3 → L4. Voir [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0. Terminologie : **Stage Gate = porte d'acceptation par étape**, **HITL = Human-in-the-Loop (humain dans la boucle de review)**.

## 3. Objectifs & Bénéfices

| Objectif | Bénéfice |
| --- | --- |
| Chaque niveau a un curriculum complet et livrable | Le formateur peut directement enseigner, sans refaire le design |
| La production en cours laisse des assets acceptables | Les résultats deviennent capacité organisationnelle, pas « oublié après le cours » |
| Chaque niveau a un Stage Gate | Pas d'avance sans passage, évite les sauts ratés |
| Ratio de cours configuré selon les scores de diagnostic | Ressources client concentrées sur les lacunes, pas gaspillées |
| L3/L4 avec bibliothèque de scénarios PoC + squelettes n8n | Exercices pratiques avec sujets et templates prêts, pas de départ à zéro |

**Si ce répertoire est sauté** : le client achète des outils sans capacité, les PoC restent éternellement en demo, l'IA ne scale pas.

## 4. Workflow & Logique

```text
01_Assessment diagnostic → niveau L + recommandation de ratio
   ↓
COURSE_REQUIREMENTS_AND_COMPANY_PROFILE (confirmer prérequis, profil, mode de déploiement)
   ↓
COURSE_MODULE_MATRIX (voir outline L1-L5 et configuration des ratios)
   ↓
L1_L5_COMPLETE_COURSE_PLAN (curriculum global) + curricula profonds par niveau :
   L1 OPENWEBUI → L2 ANTIGRAVITY → L3 N8N → L4 HERMES → L5 CLAWTEAM
   ↓ par niveau
   Cours → exercices (avec POC_SCENARIO_SPECS / N8N_WORKFLOW_TEMPLATES comme sujets)
   → Produire des assets acceptables → passer Stage Gate → puis niveau suivant
```

| Étape | Qui | Quand | Input | Output |
| --- | --- | --- | --- | --- |
| Confirmer prérequis | Consultant + IT client | Avant cours | Résultat diagnostic, profil | Checklist pré-cours passée |
| Configurer ratio | Consultant | Avant cours | Niveau L + recommandation | Configuration horaire L1-L5 |
| Cours (par niveau) | Formateur | Phase build | Curricula profonds | Résultats apprenants |
| Exercices | Apprenants | En cours chaque niveau | Scénario PoC / squelette n8n | Prompt/Skill/Workflow/Agent/Team |
| Acceptation Stage Gate | Consultant + manager client | Après chaque niveau | Output en cours | Gate passé → niveau suivant |

> Logique : les cours ne sont pas « enseigner l'usage d'outil » mais « construire une capacité organisationnelle vérifiable le long de la maturité ». Chaque niveau suit la structure « première moitié produire, deuxième moitié connecter au suivant ».

## 5. Descriptions de Fichiers

### `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md`

Liste des exigences de cours L1-L5 et enquête de profil d'entreprise. Définit pour chaque niveau les prérequis, données de base, attributs données et risque, inventaire système, conditions d'éligibilité et notes de cours pour trois modes de déploiement (cloud IA / hybride / on-prem complet). Utilisé avant le cours pour confirmer « le client est-il prêt ? ».

### `COURSE_MODULE_MATRIX.md`

Matrice des modules de cours L1-L5. Un tableau montre pour chaque niveau : objectifs, exercices, output devoirs, packaging (demi-journée expérience / atelier d'une journée / bootcamp deux jours / projet conseil) et règles de recommandation de ratio selon la maturité.

### `L1_L5_COMPLETE_COURSE_PLAN.md`

Planification complète L1-L5. Par niveau : objectifs, contenu, exercices, devoirs, standard d'achèvement et résumé Stage Gate. Curricula profonds par niveau dans les cinq fichiers suivants.

### `L1_OPENWEBUI_COURSE_PLAN.md`

Curriculum profond L1 Controlled AI Access. Référence playlist publique OpenWebUI, inclut login par personne, espace chat personnel, Admin Panel, comptes/rôles/groupes/permissions, contrôle des modèles, normes de données, carte de référence vidéo.

### `L2_ANTIGRAVITY_COURSE_PLAN.md`

Curriculum profond L2 Knowledge Codification. Référence trois codelabs Google Antigravity, inclut Agentic IDE, App Prototype, Unit Test, GCP Serverless Pipeline, Gate 2A-2E. **§7.6** inclut module « utiliser bibliothèque Agent existante (agency-agents) ». Deuxième moitié : Bridge L2→L3.

### `L3_N8N_TIGERAI_COURSE_PLAN.md`

Curriculum profond L3 Workflow Automation. **§1.1** divise L3 en première moitié (concept n8n et construction manuelle) et deuxième moitié (AG + TigerAI-n8n-Skill-Pack génération en langage naturel, **§5.5**). Référence vidéos chaîne TigerAI n8n / OpenGenie, inclut Gemini, multimodal, Sub-workflow, Data Tables, Webhook, GitHub Backup, Gate 3A-3G.

### `L4_HERMES_AGENT_COURSE_PLAN.md`

Curriculum profond L4 Autonomous Agent. **§2** « sept principes de design d'Agent knowledge-grade » (jour léger / nuit lourde, boucle de capitalisation savoir, P1>P2, écriture-lecture-même-source, division outils/LLM, apprentissage piloté par failure-mode, pourquoi pas que RAG). Inclut combinaison master + skills spécialisés, mémoire Wiki, ingest/query/update, Gate 4A-4E. **Ce cours ne prend que les concepts, pas le code interne.**

### `L5_CLAWTEAM_COURSE_PLAN.md`

Curriculum profond L5 Multi-Agent Organization. Sur la base de HKUDS/ClawTeam (MIT) comme plateforme d'implémentation, inclut architecture cinq couches Team/Workspace/Task/Inbox/Transport, git worktree, CLI hands-on, trois scénarios localisés, Gate 5.

### `POC_SCENARIO_SPECS.md`

Bibliothèque de scénarios PoC pour cours L3/L4. 7 catégories au total 35 PoCs implémentables (Gmail / Sheets / Notion / CRM / API / ERP + comptabilité), chacun avec trigger, input, AI step, systems, output, acceptance, KPI, person-day, séquence node n8n. Choisir directement les sujets d'exercice ici.

### `N8N_WORKFLOW_TEMPLATES.md`

Organiser les PoCs en squelettes workflow n8n importables (JSON). Inclut 30 squelettes PoC, flow export/import, spécification de nommage de version, SOP GitHub Backup, flow d'utilisation en cours.

### `*_EN.md`

Versions anglaises sibling des fichiers ci-dessus.

## 6. Mapping vers Autres Répertoires

| Répertoire | Relation avec ce répertoire | Flux de données |
| --- | --- | --- |
| `01_Assessment` | Niveau L + ratio de cours du diagnostic détermine la configuration | `01` ratio → `02` configuration |
| `00_Overview` | Les cours sont la phase « Build » de la story | `00` story → `02` réalisation |
| `03_Consulting_Report` | Output et observations en cours alimentent le rapport 8 étapes | `02` output → `03` rapport |
| `04_Scenarios` | Sujets de démo depuis l'index de cas ; PoCs peuvent devenir cas | `04` cas ↔ `02` sujets de cours |
| `06_Delivery` | Cours correspondent à Delivery — Build du cycle ; livrables vers acceptance | `02` output → `06` acceptance |
| `90_References` | Citations tierces par niveau (OpenWebUI / Antigravity / n8n-Skill-Pack / ClawTeam / agency-agents) | `90` citation → `02` |

## 7. Scénarios d'Usage Communs

- **Configurer ratio de cours** : prendre le ratio du diagnostic → utiliser `COURSE_MODULE_MATRIX.md` pour configurer les heures → ouvrir le curriculum profond correspondant.
- **Donner cours L3** : utiliser première moitié de `L3_N8N_TIGERAI_COURSE_PLAN.md` pour le concept, deuxième moitié pour AG+Skill Pack ; sujets d'exercice depuis `POC_SCENARIO_SPECS.md`, squelettes importés depuis `N8N_WORKFLOW_TEMPLATES.md`.
- **Apprenants cherchent sujets** : selon département et niveau L, choisir depuis `POC_SCENARIO_SPECS.md` ou `04_Scenarios/LLM_APPS_CASE_INDEX.md`.
- **Acceptance** : après chaque niveau, passer Stage Gate contre `01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`.

---

## ⭐ Cross-Topic Quick References : 5 Thèmes Centraux, où Trouver

Toute la méthodologie a 5 artères principales traversant tous les répertoires. Comment ce répertoire se connecte à chacune :

| Cross-Topic | Lieu principal | Comment ce répertoire se connecte |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lecture trois moteurs** | Root [`README_FR.md`](../README_FR.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | **L2 Knowledge Codification enseigne directement les trois moteurs** — Antigravity / Codex / Claude Code sont les outils des apprenants L2 ; en cours, les trois moteurs peuvent être mobilisés pour démos, encapsulation Skill, tests inter-fichiers |
| 🎓 **Fondement académique (7 piliers)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **Architecture 5 couches L1-L5 selon Capability Maturity (Rosemann/CMMI)** ; règle anti-saut selon Absorptive Capacity (Cohen & Levinthal 1990) ; sept principes design L4 Hermes selon Sociotechnical & Knowledge Compounding |
| 📚 **Éducation L1-L5** | [`../02_Course_Design/`](ce répertoire) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](L1_L5_COMPLETE_COURSE_PLAN.md) | **Ce répertoire EST le corps de l'éducation L1-L5** — 5 curricula profonds indépendants (L1 OPENWEBUI / L2 ANTIGRAVITY / L3 N8N / L4 HERMES / L5 CLAWTEAM) + COURSE_MODULE_MATRIX configuration ratio + POC_SCENARIO_SPECS 35 sujets hands-on |
| 🔁 **Conseil / 8 étapes + Closed-Loop Phase A→B→C** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Output en cours alimente rapport Phase B** (devient le chapitre « observations de cours » des 14 chapitres) + suivi radar trimestriel Phase C ; chaque Stage Gate correspond aux Gates A/B/C du closed-loop |
| 📖 **Références / remerciements** | [`../90_References/`](../90_References/) §2 remerciements | **L1 → OpenWebUI** ｜ **L2 → Antigravity / Codex / Claude Code + agency-agents** ｜ **L3 → n8n + TigerAI-n8n-Skill-Pack** ｜ **L4 → nousresearch/hermes-agent** ｜ **L5 → HKUDS/ClawTeam**. Appreciation cards complètes dans [`../90_References/README.md`](../90_References/README.md) §2.1-2.3 |
