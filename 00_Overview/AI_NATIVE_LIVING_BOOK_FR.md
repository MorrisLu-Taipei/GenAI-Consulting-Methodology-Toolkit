# AI-Native Living Book : Méthodologie comme Executable Knowledge Artifact

> 🌐 Langue : [繁體中文](AI_NATIVE_LIVING_BOOK.md) ｜ [English](AI_NATIVE_LIVING_BOOK_EN.md) ｜ [Deutsch](AI_NATIVE_LIVING_BOOK_DE.md) ｜ Français ｜ [Español](AI_NATIVE_LIVING_BOOK_ES.md) ｜ [日本語](AI_NATIVE_LIVING_BOOK_JA.md) ｜ [한국어](AI_NATIVE_LIVING_BOOK_KR.md)
>
> Apache License 2.0 · Auteur : Morris Lu · Tiger AI

Dernière mise à jour : 2026-05-16

---

> **Ce que ce document répond** : La caractéristique la plus distinctive de cette méthodologie n'est pas son contenu — c'est son **medium porteur**. Les méthodologies de consulting traditionnelles sont des PDFs / PPTs / SOPs (documents statiques) ; ce repo est un **système de connaissance lisible, explicable, queryable et applicable par les AI IDEs**. Les utilisateurs ne « lisent pas des documents » — ils **conversent avec la méthodologie**. Ce document écrit formellement cette caractéristique dans le positionnement de la méthodologie et adresse sa classification académique + risk controls.

---

## 1. Positionnement / Tagline d'une phrase

> Ce repository n'est pas seulement un toolkit de méthodologie, mais un **AI-native living book** : lorsqu'ouvert dans une AI IDE, ses instructions agent embarquées ([`AGENTS.md`](../AGENTS.md) et [`CLAUDE.md`](../CLAUDE.md)) transforment la méthodologie statique en un **tuteur de co-lecture interactif et assistant de consulting**.

---

## 2. Pourquoi c'est une nouvelle forme de méthodologie

### 2.1 Méthodologie traditionnelle vs. AI-Native Living Book

| Dimension | Traditionnelle (PDF / PPT / SOP) | AI-Native Living Book (ce repo) |
| --- | --- | --- |
| **Medium** | Documents statiques, slide decks, Word | Markdown + fichiers d'instruction AI IDE (AGENTS.md / CLAUDE.md) |
| **Interaction utilisateur** | Lecture à sens unique | Conversation à deux sens (Q&R, application, génération) |
| **Barrière d'onboarding** | Élevée (doit lire 100+ pages) | Basse (AI auto-lit, devient tuteur de co-lecture) |
| **Comment appliquer** | Consultant traduit pour client | Client demande directement à AI d'appliquer à leur entreprise |
| **Peut être contesté** | Non (les documents ne répondent pas) | Oui (AI répond à toute question en temps-réel) |
| **Peut être réécrit** | Consultant doit éditer | Client forke + AI assiste avec vérification de cohérence |
| **Contrôle de version** | Habituellement aucun | Historique Git complet (inclus changements AGENTS.md) |
| **Citation académique** | Citer PDF | Citer hash de commit GitHub + environnement d'exécution reproductible |

### 2.2 Classifications académiques

Cette méthodologie peut être catégorisée comme une (ou plusieurs) de :

| Nom | Propriété emphasisée | Origine / Analogue |
| --- | --- | --- |
| **Executable Knowledge Artifact** | Connaissance qui peut être exécutée ; pas juste décrite, mais applicable | Jupyter Notebooks, computational essays |
| **AI-Mediated Methodology** | AI comme intermédiaire entre utilisateur et méthodologie | Intelligent Tutoring Systems (ITS) |
| **Interactive Consulting Playbook** | Manuel d'opérations consulting interactif | Game playbooks, decision-tree wizards |
| **Living Book with Embedded Tutor Agent** | Living book + tutor agent embarqué | Hypertext, knowledge graphs |

Tiger AI adopte **AI-native living book** comme terme primaire parce qu'il **capture simultanément** « living book » (le contenu évolue) + « AI-native » (designé pour AI) + « co-reading tutor » (personnalité de tuteur embarquée).

---

## 3. Trois couches : Repo comme Livre / Agent comme Tuteur / Méthodologie comme Executable Artifact

### 3.1 Couche 1 : Repo comme Livre

La structure du repo suit les conventions de livre :

| Élément de livre | Mapping repo |
| --- | --- |
| Couverture / position d'une phrase | Root [`README_EN.md`](../README_EN.md) + ce doc §1 |
| Préface / executive summary | [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) |
| Chapitre story | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) histoire de Ming |
| Méthodologie principale | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 |
| Chapitres d'implémentation | `01_Assessment` / `02_Course_Design` / `03_Consulting_Report` |
| Anthologie de cas | `04_Scenarios/` 7 cas Benchmark-grade |
| Support sales | `05_Sales/` |
| Delivery SOP | `06_Delivery/` |
| Argument académique | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) |
| Map d'alignment | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) |
| Failure modes (counter-cases) | [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) |
| Design de recherche | [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) |
| Références | Références de chaque fichier + `90_References/` |

> **Point clé** : Ce « livre » est **complet** — clients / consultants / académiques / régulateurs peuvent chacun trouver leur chapitre pertinent.

### 3.2 Couche 2 : Agent comme Tuteur (AGENTS.md est la « personnalité du tuteur »)

[`AGENTS.md`](../AGENTS.md) et [`CLAUDE.md`](../CLAUDE.md) ne sont pas des notes supplémentaires mais **embarquent le rôle, frontières et guidance de l'AI dans le repo**. Les AI IDEs (Claude Code / Cursor / Antigravity / Codex etc.) auto-lisent ces fichiers et se positionnent comme **« tuteurs de co-lecture pour cette méthodologie »**.

#### « Personnalité du tuteur » définie dans AGENTS.md

- **Rôle** : AI = tuteur de co-lecture + assistant consulting, PAS remplacement de consultant
- **Scope de questions répondables** : définitions de méthodologie, mapping L1-L5, outils Stage, application de cas, drafts de rapport
- **Scope de refus** : décisions finales clients, contourner judgment consultant, engagements ROI non vérifiés
- **Style de réponse** : rigueur académique + pratique consulting + compréhensible-client
- **Discipline de citation** : chaque conclusion étiquetée avec niveau d'evidence [E:L#] (par Tool 8.9)
- **Langue** : switching bilingue EN/ZH par utilisateur

> Ce design emprunte à **LangChain Agent Prompt + Claude Skills** : fichiers de configuration version-contrôlés dans le repo.

### 3.3 Couche 3 : Méthodologie comme Executable Artifact

Les utilisateurs peuvent directement demander à AI d'**exécuter la méthodologie**, pas juste la lire :

#### Interactions typiques

| Utilisateur demande | Tuteur de co-lecture AI exécute |
| --- | --- |
| « Nous sommes une usine packaging 700 personnes ; aide-moi à lancer le survey rapide 10-Q » | AI lance [`AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) version 10-Q + auto-score + produit radar |
| « Basé sur mes réponses, draft un squelette de rapport mid-engagement Phase A » | AI génère draft per structure [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) §3-§5 |
| « Nous sommes manufacturing ; quel cas est le plus proche de nous ? » | AI compare avec [`SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md) et calcule gap |
| « Prépare les matériaux pour le workshop Stage 3 Client Ideal Practice » | AI génère flow workshop + prompts sticky-note + impression 4-couches per Tool 3.6 |
| « Comment cela aligne avec McKinsey 7-Step ? » | AI mappe sur [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) §2.1 |
| « Mon radar Stage 2 devrait-il être plus rond après 24 mois ? » | AI guide l'utilisateur à travers review Quarterly Gate C |

> **C'est la signification de « Méthodologie comme Executable Artifact »** — la méthodologie n'est pas juste décrite ; elle est applicable en temps-réel via AI.

---

## 4. Abaisser les barrières d'adoption de méthodologie

### 4.1 Les entreprises craignent 100+ fichiers Markdown

Barrières de méthodologie traditionnelles :

- 100+ pages à lire ❌
- Trop de terminologie ❌
- Ne savent pas quoi lire en premier ❌
- Ont besoin de consultant pour traduire ❌
- Doivent écrire le draft de rapport eux-mêmes ❌

### 4.2 Tuteur de co-lecture AI répond en temps-réel

Une fois repo + AI IDE ouvert, les utilisateurs demandent directement :

- « **À quel niveau est mon entreprise ?** » → AI lance survey 10-Q + auto-score
- « **Quel fichier dois-je lire en premier ?** » → AI recommande ordre de lecture par rôle (CEO / consultant / IT / académique)
- « **Comment j'applique ceci à manufacturing ?** » → AI cite cas manufacturing + flagge points de customisation
- « **S'il te plaît génère le premier draft du rapport diagnostic** » → AI produit squelette Phase A 10-15 pages
- « **Quelle est la frontière entre Stage 4 et Stage 8 ?** » → AI cite METHODOLOGY_SCIENTIFIC_LOGIC §4

> **Cela shifte la méthodologie de « lisible seulement par experts » à « les non-experts peuvent être guidés à travers ».**

### 4.3 Réduction attendue de la barrière d'adoption

Hypothèses validées par PILOT_STUDY_PROTOCOL :

- Méthodologie PDF traditionnelle : taux de complétion client < 15%
- **AI-native living book** : taux de « conversation » client > 70% (AI guide proactivement)
- Cycle d'adoption entreprise moyenne (100-500 personnes) : de « 3-mois évaluation nécessaire » → « Phase A dans 2 semaines »

---

## 5. Contrôles de risque

⚠️ Parce que AI interprète la méthodologie, **le tuteur de co-lecture AI ne doit PAS** faire ce qui suit :

### 5.1 Frontières du tuteur

| Peut | Ne peut pas |
| --- | --- |
| Expliquer contenu de méthodologie | ❌ Remplacer judgment formel de consultant |
| Lancer surveys, auto-scorer, produire radars | ❌ Promettre des chiffres ROI spécifiques aux clients |
| Citer cas pour calculer gaps | ❌ Signer Ideal Practice Definition Table (requiert signature humaine 3-parties) |
| Générer drafts de rapport | ❌ Remplacer client owner / review final de consultant |
| Guider self-assessment Stage Gate | ❌ Remplacer audit tiers |
| Appliquer 80/20 / 5 Whys / Issue Tree en temps-réel | ❌ Remplacer données réelles KPI longitudinales |

### 5.2 4 principes de contrôle de risque

1. **Tuteur de co-lecture AI ≠ consultant** : tous drafts de rapport requièrent **review consultant humain ou client owner** avant usage externe
2. **Diagnoses importants requièrent evidence** : per [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9, conclusions majeures ont besoin de support L3+ (system log)
3. **Contrôle de version AGENTS.md** : éviter interprétation incohérente à travers AI IDEs — commit chaque changement AGENTS.md à Git et enregistrer dans CHANGELOG
4. **Marquage AI-generated** : per Tool 8.8 §7, tout contenu généré par AI doit être marqué « AI-generated »

### 5.3 Scénarios d'échec

Si le tuteur de co-lecture AI est mal utilisé (documenté dans [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md)) :

- AI erre et le client le prend au pied de la lettre → rapport erroné
- AI donne des chiffres ROI non vérifiés → client signe SOW basé sur faux espoir
- Différentes AI IDEs interprètent AGENTS.md différemment → conclusions incohérentes

**Mitigations** :

- AGENTS.md mandate explicitement « **Don't predict ROI without baseline data** »
- Chaque paragraphe de rapport requiert tag de niveau evidence [E:L#]
- Encourager les clients à cross-valider conclusions critiques avec ≥ 2 AI IDEs

---

## 6. Contribution académique

### 6.1 Contributions à IS / méthodologie consulting

| Contribution | Innovation |
| --- | --- |
| **Innovation de medium de méthodologie** | Première méthodologie consulting construite comme Markdown + agent config directement exécutable par AI IDEs |
| **AI-mediated knowledge transfer** | Utiliser AI comme « traducteur de connaissance » abaisse barrières d'adoption de méthodologie |
| **Open-source consulting framework** | Apache 2.0, peut être forké / adapté par d'autres consultants, académiquement reproductible |
| **Embedded tutor agent design pattern** | Pattern AGENTS.md / CLAUDE.md peut être emprunté par d'autres repos open-source |

### 6.2 Connexion à AI Pedagogy / ITS

- Recherche ITS des années 1980 étudiait « comment AI enseigne » → cette méthodologie est un nouveau cas de « **comment AI aide les adultes à apprendre méthodologies professionnelles** »
- Application du ZPD de Vygotsky (Zone of Proximal Development) : tuteur de co-lecture AI ajuste dynamiquement profondeur de prompt

### 6.3 Recherche future

- Cohérence cross-IDE de l'interprétation AGENTS.md (Claude Code / Cursor / Antigravity / Codex / Windsurf)
- Tracking longitudinal de l'effet du tuteur de co-lecture AI sur taux d'adoption de méthodologie (per design PILOT_STUDY_PROTOCOL)
- Recherche d'adoptability de méthodologie cross-language (EN / ZH / JA / KO)

---

## 7. Comment se combine avec d'autres documents

### 7.1 Statement dans différentes localisations

| Localisation | Message principal |
| --- | --- |
| Root [`README.md`](../README.md) | Positionnement d'une phrase (ZH §1) |
| Root [`README_EN.md`](../README_EN.md) | Positionnement d'une phrase (EN §1) |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) | Section « Living Book » |
| [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) | Section « How to Read This Book » |
| [`AGENTS.md`](../AGENTS.md) | Config concrète de personnalité du tuteur (au root du repo) |
| Sales decks | 1 slide highlighting différenciation « AI-native living book » |
| Submissions académiques | Chapitre entier comme contribution méthodologique |

### 7.2 Relation aux 4 autres docs de concept autoritatifs

| Document | Question qu'il répond |
| --- | --- |
| [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) | « Que vit l'utilisateur ? » |
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | « Comment fonctionne la méthodologie ? » |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | « Pourquoi la méthodologie résiste au débat ? » |
| [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | « Comment s'aligne avec les frameworks d'industrie ? » |
| **`AI_NATIVE_LIVING_BOOK_EN.md` (ce doc)** | **« Pourquoi le medium de la méthodologie est-il nouveau ? »** |

5 docs autoritatifs forment un argument méthodologique complet : **expérience + processus + science + alignment + innovation de forme**.

---

## 8. Références

- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors: Lessons learned. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.
- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Pérez, F., & Granger, B. E. (2007). IPython: A system for interactive scientific computing. *Computing in Science & Engineering*, 9(3), 21-29.
- Anthropic (2024). *Claude Code documentation* : <https://docs.anthropic.com/claude/docs/claude-code>
- OpenAI (2024). *Codex / Codex CLI*.
- Cursor (n.d.). *Cursor IDE documentation*.

---

## 9. Clôture : La prochaine phase de méthodologie

Évolution des méthodologies consulting :

```
1990s : Rapports consulting papier
   ↓
2000s : Decks PowerPoint
   ↓
2010s : Wikis SharePoint / Confluence
   ↓
2020s : Méthodologie GitHub-hosted + open source
   ↓
2025s : AI-Native Living Book (cette méthodologie)
```

**Quoi ensuite ?** Possiblement **équipe consulting multi-agent auto-running Phase A complète** (AI consultant + AI reviewer + AI client simulator, collaboration 3-Agent) — appliquant L5 Multi-Agent Organization à « la méthodologie elle-même ».

**Mais** : per §5.1, AI est toujours outil et tuteur, jamais remplacement. Judgment de consultant humain, prise de décision de client owner, audit tiers — ces **couches de gouvernance humaine** sont les garanties finales de la crédibilité de méthodologie.

---

Licence & Citation

Ce document est sous Apache License 2.0 ; peut être utilisé, modifié, commercialisé, à condition de préserver l'attribution [`../NOTICE`](../NOTICE).
