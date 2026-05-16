# 01 Assessment — Diagnostic de Maturité IA

> 🌐 中文 / Chinese : [README.md](README.md) ｜ English : [README_EN.md](README_EN.md)

## 1. Objectif de ce Répertoire

Ce répertoire est la **première phase : Diagnostic (Diagnose)** du flux de service en 3 phases. Il résout l'un des problèmes les plus fondamentaux du travail de consultant : **« L'entreprise dit qu'elle 'utilise l'IA', mais à quel niveau exactement ? Que manque-t-il ? Par où commencer ? »**

Sans diagnostic objectif, les consultants ne peuvent composer les cours qu'à partir des descriptions subjectives du client — résultat fréquent : sauts de niveau (le client n'a même pas l'usage L1 généralisé mais veut faire un Agent L4) ou mauvaises priorités (la gouvernance manque mais on ajoute sans cesse des outils). Ce répertoire transforme avec trois longueurs de questionnaire + modèle de scoring + enquête de profil d'entreprise les « impressions floues » en **scores L1-L5 objectifs, quantifiables, comparables, et cartes radar de lacunes sur six dimensions**.

Qui utilise ce répertoire : Sales (version 10 items pour qualification lead), consultants (versions 25/50 items pour inventaire pré-cours et pré-entretien), IT/AI Champion (questionnaire profil entreprise).

## 2. Position dans la Méthodologie

| Axe | Mapping |
| --- | --- |
| Flux de service 3 phases | **Diagnostic** — première phase |
| Structure de conseil 8 étapes | **Étape 1 Saisie de l'existant** (le résultat du diagnostic est l'input central de l'étape 1) |
| Maturité L1-L5 | Ce répertoire est l'outil pour « **déterminer à quel niveau se situe le client** » |
| Engagement Lifecycle | **Sales — Lead Qualification (10 items) / Discovery (25/50 items)** |

## 3. Objectifs & Bénéfices

| Objectif | Bénéfice |
| --- | --- |
| Remplacer la conjecture subjective par des scores objectifs | Le consultant a une base pour composer les cours, pas seulement du feeling |
| Trouver les lacunes sur six dimensions (outils/savoir/processus/intégration/Agent/gouvernance-ROI) | Savoir où le client est fort / faible |
| Dériver directement trois recommandations | Ratio de cours + mode de déploiement + scénario PoC en une étape |
| Trois longueurs de questionnaire pour trois phases commerciales | Développement lead, pré-cours, pré-entretien — chacun son outil |
| Automatisable | Questionnaire → scoring → rapport entièrement automatique, le consultant n'interprète que |

**Si ce répertoire est sauté** : ratio de cours deviné, attentes client non maîtrisables (montre un cas L5 « je veux ça » sans savoir qu'il est L2), rapport de conseil sans point de départ objectif.

## 4. Workflow & Logique

```text
Questionnaire rapide 10 items (développement lead, 3 min)
   → Qualification lead + position L initiale
Questionnaire 25 items (pré-cours, 8 min, rempli par managers client)
   → Scores six dimensions + diagramme radar
Questionnaire 50 items (pré-entretien consultant, 20 min, IT/AI Champion)
   → Inventaire complet + questions ouvertes
Questionnaire profil entreprise (35 items)
   → JSON Profile Bundle (système / risque / préférence déploiement / budget)
        ↓ Merge
   Auto-scoring → niveau L1-L5 + radar six dimensions
        ↓ Dérivation
   ① Ratio de cours recommandé  ② Mode de déploiement recommandé  ③ Scénario PoC recommandé
```

| Étape | Qui | Quand | Input | Output |
| --- | --- | --- | --- | --- |
| Quickscreen 10 items | Sales | Développement lead | Prospect | Qualification + niveau L initial |
| Diagnostic pré-cours 25 items | Groupe de managers client | 1 semaine avant le L1 | Questionnaire 25 items | Scores six dimensions |
| Inventaire complet 50 items | IT/AI Champion client | Avant entretien consultant | 50 items + profil entreprise | Profile Bundle complet |
| Auto-scoring | Système (Sheets/Notion/n8n) | Après soumission | Réponses | Niveau L + radar + 3 recommandations |
| Interprétation | Consultant | Après rapport auto | Rapport auto | Direction de proposition personnalisée |

> Logique : le questionnaire n'est qu'**input** ; le vrai output est « **niveau L + lacunes six dimensions + 3 recommandations** ». Ces trois alimentent — ratio de cours → `02_Course_Design` ; mode de déploiement → To-Be Design de `03` ; scénario PoC → index de cas de `04_Scenarios`. Le diagnostic n'est pas la fin, c'est l'interrupteur qui « allume » les trois répertoires suivants.

## 5. Descriptions de Fichiers

### `AI_MATURITY_QUESTIONNAIRE.md`

Questionnaire de maturité IA en trois longueurs 10 / 25 / 50 items. Version 10 items pour évaluation rapide commerciale ; version 25 items 4-5 questions par dimension pour pré-cours ; version 50 items plus mode de déploiement et inventaire système pour pré-entretien. Les trois versions partagent l'échelle 0-4 et l'architecture six dimensions.

### `AI_MATURITY_SCORING_MODEL.md`

Logique de scoring et règles de décision. Inclut : scoring des six dimensions (usage outils, capitalisation savoir, standardisation processus, intégration systèmes, application Agent, gouvernance-ROI), seuils de points totaux correspondant à L1-L5, **maturité principale vs maturité locale** (pourquoi un département peut être localement L4 mais globalement L2), règles de recommandation du mode de déploiement et du ratio de cours.

### `AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`

Definition of Done, Deliverables, Evidence, Owner, Stage Gate, Fail Condition, Next Level Entry Criteria pour chaque niveau L1-L5. Définit « à quoi ressemble 'fini' à chaque niveau, quelle evidence comme preuve » — base de l'acceptation Stage Gate.

### `FILLABLE_QUESTIONNAIRE.md`

Spécification de rendu transformant 10/25/50 items en formulaires remplissables — types de questions (radio / échelle 0-4 / multi-choix / réponse courte), segmentation, skip logic, page de soumission et page « ce qui va se passer ». Avec consignes de rendu pour Google Form / Tally / Notion Form.

### `COMPANY_PROFILE_QUESTIONNAIRE.md`

Questionnaire de profil entreprise 35 items, 6 sections (Profile / Systems / Risk / Deployment / Course / Budget). Output : JSON Profile Bundle, plus **règles de dérivation** : du Bundle dériver automatiquement recommandations de déploiement, fine-tuning du ratio de cours, suggestions PoC. Lié au questionnaire de maturité par `submission_id`.

### `AI_DIAGNOSIS_SHEETS_SCHEMA.md`

Schéma d'implémentation pour automatiser tout le diagnostic. Trois plateformes : Google Sheets (formules de scoring, formatage conditionnel, Apps Script), Notion (4 structures de database et formules), n8n (flow auto-diagnostic 13 nodes, incl. idempotency). Du questionnaire au scoring à la génération de rapport et notification au consultant, tout automatique.

### `*_EN.md`

Versions anglaises sibling des fichiers ci-dessus.

## 6. Mapping vers Autres Répertoires

| Répertoire | Relation avec ce répertoire | Flux de données |
| --- | --- | --- |
| `00_Overview` | Le diagnostic est la première phase de la story | `00` story → `01` réalisation |
| `02_Course_Design` | Le « niveau L + ratio de cours » du diagnostic détermine directement la configuration | `01` ratio → `02` configuration |
| `03_Consulting_Report` | Le résultat du diagnostic est l'input de l'étape 1 ; le rapport cite les scores et le radar | `01` scores → `03` rapport |
| `04_Scenarios` | Après diagnostic, selon le niveau L, utiliser `LLM_APPS_CASE_INDEX.md` pour choisir des PoC | `01` niveau L → `04` sélection cas |
| `06_Delivery` | Le diagnostic correspond à la phase Sales du cycle d'engagement | `01` ↔ `06` phase Sales |
| `90_References` | Base méthodologique du modèle de scoring | `90` base → `01` |

## 7. Scénarios d'Usage Communs

- **Développement commercial** : prospect remplit la version 10 items → rapport auto sous 24 h → Sales va à la rencontre avec le niveau L.
- **Préparation pré-cours** : 1 semaine avant le démarrage, envoyer la version 25 items aux managers → le consultant reçoit le radar six dimensions, ajuste le ratio.
- **Avant entretien consultant** : IT/AI Champion remplit 50 items + profil entreprise → le consultant reçoit 1 h avant l'entretien le Profile Bundle complet comme brief.
- **Pour scaler** : avec `AI_DIAGNOSIS_SHEETS_SCHEMA.md` déployer le flow auto-diagnostic dans le n8n du client, le consultant n'interprète que la fin.

---

## ⭐ Cross-Topic Quick References : 5 Thèmes Centraux, où Trouver

Toute la méthodologie a 5 artères principales traversant tous les répertoires. Comment ce répertoire se connecte à chacune :

| Cross-Topic | Lieu principal | Comment ce répertoire se connecte |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lecture trois moteurs** | Root [`README_FR.md`](../README_FR.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | Le questionnaire peut être rempli en interactif via Antigravity `/diagnose` ; AI_DIAGNOSIS_SHEETS_SCHEMA automatise le questionnaire (n8n + Google Sheets + Notion) ; le résultat peut entrer dans Codex `/consistency-review` pour alignement inter-fichiers |
| 🎓 **Fondement académique (7 piliers)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **[`BARS_RUBRICS.md`](BARS_RUBRICS.md) de ce répertoire correspond à l'inter-rater reliability** (Smith & Kendall 1963) ; les six dimensions correspondent à Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Sociotechnical Trust |
| 📚 **Éducation L1-L5** | [`../02_Course_Design/`](../02_Course_Design/) | **La détermination du niveau L + radar six dimensions + recommandation du ratio** du diagnostic détermine directement la configuration `02` — c'est le « pré-requis » de `02` |
| 🔁 **Conseil / 8 étapes + Closed-Loop Phase A→B→C** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Diagnostic = input central de la Phase A** (Étape 1 saisie de l'existant + Étape 2 signature radar Reference Model) ; la revue radar trimestrielle de la Phase C EST « **refaire le diagnostic** » — la structure est-elle réellement devenue plus ronde ? Le diagnostic est à la fois entrée et mécanisme de falsification de la boucle |
| 📖 **Références / remerciements** | [`../90_References/`](../90_References/) §2 remerciements | Modèle de scoring référence BARS (Smith & Kendall 1963) + 7 piliers théoriques ; plan empirique 18-24 mois Pilot Study voir [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) (valide l'objectif Cohen's κ ≥ 0.60 du questionnaire) |
