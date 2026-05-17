# 90 References — Documents de référence, sources & remerciements

> 🌐 中文 / Chinese : [README.md](README.md) ｜ English : [README_EN.md](README_EN.md)

## 1. Objectif de ce répertoire

Ce répertoire est la **bibliothèque de références, le centre de gouvernance des citations et la liste de remerciements** de toute la méthodologie. Les répertoires `00`-`07` couvrent « la méthode et les outils » ; ce répertoire répond à trois questions :

1. **Sur quoi reposent ces méthodes ?** (PDF original, schémas de méthodologie, notes d'apprentissage vidéo)
2. **Quels contenus citent des tiers ? Les licences sont-elles conformes ?** (chaque projet cité possède son propre `*_REFERENCE.md`)
3. **Sur les épaules de qui sommes-nous ?** (liste de remerciements)

Public : consultants, relecteurs, services juridiques, redistributeurs, **apprenants et enthousiastes cherchant les projets en amont**.

---

## 2. Remerciements : sur quelles épaules nous nous tenons

Organisés par niveau d'usage en quatre catégories : **Plateformes Core / Frameworks de conseil / Agent & Skill / Index de cas**. Chaque « carte de reconnaissance » contient **l'URL amont + où nous le citons + lien vers le `_REFERENCE.md` complet**.

### 2.1 Plateformes Core (la base d'exécution pour L1-L5)

Ce ne sont pas des « documents cités » — ce sont **les plateformes sur lesquelles tournent les cours L1-L5**. Sans elles, cette méthodologie ne peut pas être déployée.

#### 🎯 [`open-webui/open-webui`](https://github.com/open-webui/open-webui) (open-source, licence : voir LICENSE amont)

- **Ce que c'est** : interface chat IA d'entreprise open-source et auto-hébergeable. Prend en charge plusieurs fournisseurs LLM (OpenAI / Anthropic / Ollama / OpenRouter / Azure, etc.), comptes / groupes / rôles / permissions, espaces de chat personnels, contrôle des modèles, pipelines, function calling, bases de connaissances, RAG, upload image/audio/fichier.
- **Pourquoi nous l'apprécions** : l'une des rares solutions open-source qui rend « **le point d'entrée chat IA interne à l'entreprise** » à la fois « **installable en un clic, entièrement on-prem, à permissions hiérarchisées, auditable** ». Permet aux entreprises d'essayer les LLM sans envoyer de données vers le SaaS — critique pour les déploiements on-prem en manufacturing / santé / gouvernement. Communauté active, évolution rapide des versions.
- **Où nous l'utilisons** : **la plateforme core de L1 Controlled AI Access** — plan de cours complet dans [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) ; notes d'apprentissage vidéo dans [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md).

#### 🎯 [`n8n-io/n8n`](https://github.com/n8n-io/n8n) (Sustainable Use License, voir LICENSE.md amont)

- **Ce que c'est** : plateforme d'automatisation de workflow open-source. Éditeur visuel, 1000+ intégrations (Gmail, Sheets, Notion, Slack, CRM, API, ERP, bases de données, webhooks, nœuds personnalisés), bibliothèque de sous-workflows, tables de données, logs d'exécution, gestion d'erreurs, déclencheurs planifiés, nœuds AI / LangChain. Supporte self-host et cloud.
- **Pourquoi nous l'apprécions** : les « **briques LEGO** » de l'automatisation inter-systèmes — les consultants peuvent assembler un PoC en 1-2 jours pour démos clients. Communauté active, modèles riches, modèle économique sain. **Le self-hosting est critique pour l'adoption entreprise** (données restent en interne). L'auteur de la méthodologie est aussi n8n Taipei Ambassador.
- **Où nous l'utilisons** : **le moteur core de L3 Workflow Automation** — plan de cours complet dans [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) ; 35 spécifications PoC implémentables dans [`../02_Course_Design/POC_SCENARIO_SPECS.md`](../02_Course_Design/POC_SCENARIO_SPECS.md) ; 30 squelettes JSON de workflow dans [`../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md`](../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md) ; notes vidéo dans [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md).

#### 🎯 [`nousresearch/hermes-agent`](https://github.com/nousresearch/hermes-agent) (Nous Research, voir LICENSE amont)

- **Ce que c'est** : implémentation de référence open-source de Nous Research pour un **Knowledge-grade Autonomous Agent** — **Wiki-Capability-Map-Memory + ingest / query / update à trois étapes pour Knowledge-Compounding + tâches planifiées + Gate 4A-4E + HITL Human Review**. Objectif de conception : un « super-assistant IA agent entièrement autonome » vérifiable.
- **Pourquoi nous l'apprécions** : intègre « **Autonomous Agent + Knowledge Management** » dans un design pattern vérifiable — les **« Sept principes de conception pour Knowledge-grade Agents »** (light-day-heavy-night / Knowledge-Compounding-Loop / P1>P2 / Write-Read-Same-Source / Tool-vs-LLM-Division / Failure-driven Learning / Why-not-just-RAG) offrent un framework d'apprentissage complet pour L4 Agent Design.
- **Où nous l'utilisons** : **l'épine dorsale du design du cours L4 Autonomous Agent** — [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) §2 explique les sept principes. **Limite** : le cours **ne prend que concepts et design patterns — pas de reproduction du code source, pas de fork**.

#### 🎯 [`HKUDS/ClawTeam`](https://github.com/HKUDS/ClawTeam) (HKUDS, MIT)

- **Ce que c'est** : **framework open-source de Collaboration Multi-Agents** du HKU Data Science Lab (HKUDS). Architecture cinq couches (Team / Workspace / Task / Inbox / Transport), git worktree pour espaces de travail Agent isolés ; CLI-driven ; trois scénarios de référence.
- **Pourquoi nous l'apprécions** : pousse « Multi-Agent Team Collaboration » de l'échelle démo à « **collaboration auditable en workflow réel** » — chaque agent a son propre worktree, sa propre inbox, son propre transport. Pas un toy-demo de style chat, mais plus proche d'une division réelle du travail organisationnel. Fondement académique (HKUDS) + licence MIT.
- **Où nous l'utilisons** : **la plateforme d'implémentation de L5 Multi-Agent Organization** — plan de cours complet dans [`../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md`](../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md) ; walkthrough Manufacturing QA Team dans [`../04_Scenarios/CLAWTEAM_WALKTHROUGH.md`](../04_Scenarios/CLAWTEAM_WALKTHROUGH.md).
- **Citation complète** : [`CLAWTEAM_REFERENCE.md`](CLAWTEAM_REFERENCE.md)

### 2.2 Frameworks de conseil (influence 03_Consulting_Report)

#### 🎯 [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant) (MIT)

- **Ce que c'est** : organisation programmatique des frameworks d'analyse classiques du conseil (MECE, Pyramid Principle, Issue Tree, Porter's 5 Forces, SWOT, BCG Matrix, 5 Whys, Fishbone, Business Model Canvas, WBS/RACI, NPV/IRR, Lean/Six Sigma, etc. — 50+ frameworks)
- **Pourquoi nous l'apprécions** : transforme des frameworks de conseil épars en une **bibliothèque structurée, citable et composable** — pas une énième collection de PPT
- **Où nous l'utilisons** : [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) — adapté en 7 catégories + sélecteur de framework + mapping aux 8 stades
- **Citation complète** : [`CONSULTANT_FRAMEWORKS_REFERENCE.md`](CONSULTANT_FRAMEWORKS_REFERENCE.md)

#### 🎯 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills) (MIT)

- **Ce que c'est** : transforme l'artisanat de production « **Problème → Rapport / Deck** » des top consultants comme McKinsey en workflow exécutable en 8 étapes
- **Pourquoi nous l'apprécions** : le premier à mettre par écrit l'ensemble « Dummy Page → Dependency Management → 7 Page Layouts → Progressive Disclosure → Troubleshooting » dans une SOP enseignable — au lieu d'« artisanat implicite réservé aux seniors »
- **Où nous l'utilisons** : [`../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) — adapté en workflow consulting report en 8 étapes + §9 Troubleshooting Playbook
- **Citation complète** : [`MCKINSEY_SKILLS_REFERENCE.md`](MCKINSEY_SKILLS_REFERENCE.md)

#### 🎯 **Mirza Iqbal ([next8n.com](https://next8n.com)) — Workflow Delivery Framework** (MIT)

- **Ce que c'est** : la **SOP opérationnelle** pour le conseil delivery n8n — cycle de vie complet Discovery → Sprint → Handover, grilles de prix, modèles de communication client
- **Pourquoi nous l'apprécions** : un des rares à avoir open-sourcé la **SOP opérationnelle du travail de delivery** (pas seulement la SOP technique) — remplit le côté opérationnel dont l'industrie du conseil parle rarement
- **Où nous l'utilisons** : [`../06_Delivery/`](../06_Delivery/) — Engagement Lifecycle, Role SOPs, Business Document Templates en sont tous inspirés
- **Citation complète** : [`WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)
- **Obtenu via** : <https://github.com/MorrisLu-Taipei/AI-Workflow-Delivery-Framework> (le README indique Mirza Iqbal comme auteur original)

### 2.3 Agent & Skill (influence 02_Course_Design)

#### 🎯 [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) (MIT)

- **Ce que c'est** : bibliothèque de personas Agent pour 12 divisions (Marketing, Sales, Customer Service, HR, Finance, R&D, etc.) — directement utilisable
- **Pourquoi nous l'apprécions** : fait du « design de persona Agent » une bibliothèque réutilisable, économisant aux équipes l'écriture de system prompts à partir de zéro
- **Où nous l'utilisons** : [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6 module « utiliser des bibliothèques d'agents existantes »
- **Citation complète** : [`AGENCY_AGENTS_REFERENCE.md`](AGENCY_AGENTS_REFERENCE.md)

#### 🎯 [`MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack) (licence mixte)

- **Ce que c'est** : structure n8n Skill à trois couches (Workflow Library + Cookbook + DSL Spec), avec AI-generated Workflow Skill Pack
- **Pourquoi figure ici** : c'est le projet personnel de Morris Lu, auteur de la méthodologie, mais listé ici pour **démontrer la discipline de citation** — même pour ses propres projets, la licence et les sources tierces (`_vendor/` MIT) sont documentées avec le même standard
- **Où nous l'utilisons** : [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) seconde moitié
- **Citation complète** : [`N8N_SKILL_PACK_REFERENCE.md`](N8N_SKILL_PACK_REFERENCE.md)

### 2.4 Index de cas (influence 04_Scenarios)

#### 🎯 [`Shubhamsaboo/awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps) (Apache-2.0)

- **Ce que c'est** : liste curatée de 150+ cas d'applications LLM réelles (Agent / RAG / Fine-Tuning / Multimodal, etc.), maintenue par la communauté
- **Pourquoi nous l'apprécions** : haute qualité de curation, taxonomie claire, mise à jour continue ; la référence la plus rapide quand un consultant dit au client « **voilà comment d'autres font avec ce scénario** »
- **Où nous l'utilisons** : [`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index — mappé sur l'index dual-axis (L1-L5 × département entreprise) ; **le mapping est de nous**, la liste originale est sous copyright de Shubham Saboo et des contributeurs communautaires
- **Citation complète** : [`AWESOME_LLM_APPS_REFERENCE.md`](AWESOME_LLM_APPS_REFERENCE.md)

#### 🎯 [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) (MIT)

- **Ce que c'est** : 93+ projets pédagogiques d'AI Engineering (implémentations exécutables, de RAG à Multi-Agent)
- **Pourquoi nous l'apprécions** : chaque projet vient avec **code + vidéo pédagogique**, les apprenants peuvent démarrer directement ; complète les « cas curatés » d'awesome-llm-apps par le côté « implémentation hands-on »
- **Où nous l'utilisons** : [`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index seconde source — mappé sur démos exécutables des cours L2-L4
- **Citation complète** : [`AI_ENGINEERING_HUB_REFERENCE.md`](AI_ENGINEERING_HUB_REFERENCE.md)

---

## 3. Documents de référence originaux & schémas (faits maison ou domaine public)

| Fichier | Objectif |
| --- | --- |
| [`@AI-MD-PUBIC.pdf`](@AI-MD-PUBIC.pdf) | Manuel version publique d'AI Transformation Maturity Model (le PDF original du brouillon méthodologique) |
| [`MD-Map.png`](MD-Map.png) | AI Maturity Map, utilisée dans le README racine |
| [`Metholodgy.png`](Metholodgy.png) | Enterprise Consulting Eight-Stage Transformation Guide, utilisé dans le README racine |

## 4. Fondement académique & failure patterns (entièrement originaux, écrits par Tiger AI + les trois AI engines)

| Fichier | Objectif |
| --- | --- |
| [`FAILURE_PATTERNS.md`](FAILURE_PATTERNS.md) | 14 failure patterns (prédictions théoriques + cas réels + correctifs correspondants) |
| [`AI_GOVERNANCE_ALIGNMENT.md`](AI_GOVERNANCE_ALIGNMENT.md) | Alignement avec NIST AI RMF / EU AI Act / ISO 42001 |
| [`PILOT_STUDY_PROTOCOL.md`](PILOT_STUDY_PROTOCOL.md) | Design de recherche empirique 18-24 mois (Pilot Study) |

La théorie académique elle-même (les 7 piliers) se trouve dans [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md).

## 5. Notes d'apprentissage vidéo (notes dérivées ; copyright vidéo original aux créateurs)

| Fichier | Objectif |
| --- | --- |
| [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md) | Notes de la playlist publique OpenWebUI, mappées à l'usage du cours L1 |
| [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md) | Notes de la chaîne TigerAI, centrées sur n8n / usage du cours L3 |

---

## 6. Discipline de citation (les règles d'or pour les futurs contributeurs)

Pour citer quelque chose de tiers dans ce repo, **tous suivent ces principes « Approach A »** :

| # | Principe | Comment |
|---|---|---|
| 1 | **Adapter indépendamment — ne pas forker, ne pas reproduire le code source** | Référencer structure et concepts, puis réécrire dans la voix de cette méthodologie |
| 2 | **Attribution explicite, double notation** | (a) note d'en-tête dans le fichier citant ; (b) `*_REFERENCE.md` standalone dans ce répertoire |
| 3 | **Généraliser au scénario méthodologique** | Convertir le contenu spécifique au domaine dans le contexte du conseil en transformation IA L1-L5 |
| 4 | **Pas de licence = pas d'intégration** | Projets tiers sans LICENSE ne sont pas intégrés (uniquement cités comme URL d'exemple externe) |
| 5 | **Reconnaissance généreuse** | Dans le fichier de citation, **dire explicitement ce qui est bien**, pas juste « voir source ci-dessous » |
| 6 | **Honnête sur les échecs** | Si un outil cité se révèle inadapté, l'écrire honnêtement dans `FAILURE_PATTERNS.md` — pas que des success stories |

**Logique d'usage** : pour trouver « ce qui a été cité dans le fichier X du répertoire Y » → lire l'en-tête de ce fichier → sauter au `*_REFERENCE.md` correspondant dans ce répertoire pour la note de licence complète.

---

## 7. Mapping inter-répertoires

| Répertoire | Relation avec ce répertoire |
| --- | --- |
| [`../00_Overview/`](../00_Overview/) | Les schémas méthodologiques (Metholodgy.png / MD-Map.png) viennent d'ici ; la discussion des 7 piliers théoriques vit dans `00` |
| [`../02_Course_Design/`](../02_Course_Design/) | Citations tierces pour les cours L1/L2/L3/L5 (notes OpenWebUI, agency-agents, n8n-Skill-Pack, ClawTeam) |
| [`../03_Consulting_Report/`](../03_Consulting_Report/) | Citations tierces pour la bibliothèque de frameworks et le workflow de rapport (consultant, mckinsey-skills) |
| [`../04_Scenarios/`](../04_Scenarios/) | Citations tierces pour l'index de cas d'application LLM (awesome-llm-apps, ai-engineering-hub) |
| [`../06_Delivery/`](../06_Delivery/) | Citation tierce pour la couche d'opérations delivery (framework de Mirza Iqbal) |
| [`../07_AI_Contributions/`](../07_AI_Contributions/) | Les trois AI engines elles-mêmes sont aussi des « sujets de remerciement » — Antigravity / Codex CLI / Claude Code |

---

## 8. Scénarios d'usage courants

- **Se demander pourquoi un fichier est écrit d'une certaine manière** : lire l'en-tête du fichier → mapper au `*_REFERENCE.md` dans ce répertoire
- **Redistribuer / commercialiser cette méthodologie** : lire §6 Discipline de citation + exigences d'attribution dans [`NOTICE`](../NOTICE)
- **Onboarder un nouveau projet open-source** → suivre les 6 principes de §6 : confirmer la licence → adapter indépendamment → créer `*_REFERENCE.md` → ajouter à §2 Remerciements de ce README
- **Engager les communautés amont, interagir / reconnaître** : cliquer sur l'URL GitHub de chaque carte de reconnaissance pour star, follow, ouvrir issue, envoyer PR
- **Apprenants citant le contenu du repo dans leurs propres papers / decks** : selon §6, en citant cette méthodologie conserver l'attribution de l'auteur original ([`../NOTICE`](../NOTICE)) ; en citant du matériel tiers suivre le format de citation apprenant dans le `*_REFERENCE.md` correspondant

---

## 9. Remerciements

Tous les auteurs et communautés amont listés dans ce répertoire **sont les épaules sur lesquelles cette méthodologie repose**. Toute mauvaise interprétation, citation inappropriée ou déviation de l'objectif original est la seule responsabilité de l'auteur de la méthodologie **Tiger AI Morris Lu 盧業興** — pas des auteurs ou communautés amont.

Si vous êtes un auteur amont et estimez qu'une citation dans ce repo est inappropriée, doit être corrigée ou renforcée — merci d'ouvrir une issue ou de contacter Morris Lu, nous traiterons immédiatement.

> **Propriété de l'architecture** : l'architecture méthodologique de ce repo est proposée par l'auteur humain **Morris Lu (Tiger AI)**. Les trois AI engines (Antigravity / Codex / Claude Code) sont des outils qui **exécutent, complètent, étendent et auditent**. Voir [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0.
