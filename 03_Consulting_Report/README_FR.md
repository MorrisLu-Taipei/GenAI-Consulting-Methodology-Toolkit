# 03 Consulting Report — Diagnostic & Rapport de Conseil (Boucle Fermée de Conseil)

> 🌐 中文 / Chinese : [README.md](README.md) ｜ English : [README_EN.md](README_EN.md)

## 1. Objectif de ce Répertoire

Ce répertoire est la **troisième phase du flux de service en 3 phases : Deliver**, et également le **cœur de la pratique de conseil** de toute la méthodologie.

Le diagnostic (`01`) donne des scores objectifs, le Build (`02`) fait croître la capacité du client — mais ce qu'un mandat de conseil livre finalement au client, c'est un **rapport de diagnostic structuré, basé sur l'evidence, avec Roadmap et adoptable par les décideurs**. Ce répertoire fournit tout ce qu'il faut pour produire ce rapport : **tableaux d'outils de la structure de conseil en 8 étapes, bibliothèque de frameworks classiques, workflow de production de rapport, modèle de rapport**.

> 🔁 **Ce répertoire n'est PAS un « marathon linéaire de 6 semaines », c'est la « boucle fermée de conseil »**. Conception complète de la boucle voir [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) :
> **Contrat 3 phases** (Phase A Diagnostic 2W + Phase B Stratégie 4W + Phase C Implémentation 24M) + **Rapport intermédiaire** + **Revue radar trimestrielle** (mécanisme de falsification de la gestion scientifique).
> Le point de la boucle n'est pas « fini quand livré » — mais « **la structure est-elle réellement devenue plus ronde ?** » — auto-falsification continue contre le radar Reference Model de l'étape 2.

Le problème qu'il résout : **sans méthodologie, le diagnostic du consultant est un artisanat personnel basé sur l'expérience — non scalable, non reproductible par de nouveaux consultants, qualité instable.** Ce répertoire transforme « comment un consultant fait un diagnostic » en boucle fermée standard, enseignable, réplicable et acceptable.

Qui utilise : consultants, consultants seniors, nouveaux consultants (onboarding), chefs de projet.

## 2. Position dans la Méthodologie

| Axe | Mapping |
| --- | --- |
| Flux de service 3 phases | **Deliver** — troisième phase |
| Structure de conseil 8 étapes | **Ce répertoire EST les outils et le corps du rapport des 8 étapes (Stage 1-8)** |
| **Modèle de contrat 3 phases** | **Phase A Diagnostic 2W → Phase B Stratégie 4W → Phase C Implémentation 24M + revue radar trimestrielle** (boucle fermée de conseil) |
| Maturité L1-L5 | Le rapport cite le niveau L et les observations de cours du client |
| Engagement Lifecycle | **Delivery — Handover** (le rapport est la livraison centrale de Phase B ; Phase C produit en continu des records de revue radar) |

> Deux axes orthogonaux : **L1-L5 est la « verticale capacité » (`02` responsable) ; les 8 étapes sont l'« horizontale diagnostic » (ce répertoire responsable).** Les deux axes se croisent pour livrer du vérifiable.
>
> **L1-L5 est lui-même deux axes** (axe d'échelle L1-L3 + axe d'autonomie IA L4-L5) ; voir [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0.

## 3. Objectifs & Bénéfices

| Objectif | Bénéfice |
| --- | --- |
| Chaque étape a des tableaux d'outils directement utilisables | Le consultant n'a pas à refaire le design ; nouveaux consultants opérationnels vite |
| Bibliothèque classique mappée sur les 8 étapes | Chaque étape sait « quel framework d'analyse utiliser » |
| Workflow de production de rapport | « Problème → rapport/deck livrable » a un SOP, pas un artisanat |
| Structure de rapport fixée | Qualité de livraison stable ; décideur comprend |
| Méthodologie de conseil enseignable et réplicable | Équipe de consultants scale |

**Si ce répertoire est sauté** : chaque consultant diagnostique à sa façon, qualité de rapport inconsistante, nouveaux consultants ne peuvent répliquer, le diagnostic dégénère en « artisanat personnel du senior ».

## 4. Workflow & Logique (Contrat 3 Phases + Boucle Fermée Trimestrielle)

```text
01 résultat diagnostic + 02 observations de cours
   ↓
┌─ Phase A Diagnostic (2 semaines) ──────────────────────┐
│  Stage 1-4 première moitié des 8 étapes : Awareness /  │
│  Reference Model / Discovery / Gap Analysis            │
│  → Utiliser outils CONSULTING_TOOLKIT_TEMPLATES.md     │
│  → Rapport intermédiaire → signé par le client         │
└────────────────────────────────────────────────────────┘
   ↓ Gate A — le client décide de poursuivre Phase B
┌─ Phase B Stratégie (4 semaines) ───────────────────────┐
│  Stage 5-8 seconde moitié : Stakeholder / Diagnosis /  │
│  To-Be Design / Acceptance Test                        │
│  → Production 8 étapes REPORT_PRODUCTION_WORKFLOW.md   │
│  → Rapport complet 14 chapitres + Roadmap 24M + ROI + │
│     recommandations de gouvernance                     │
│  → Rempli dans structure CONSULTING_REPORT_TEMPLATE.md │
└────────────────────────────────────────────────────────┘
   ↓ Gate B — le client signe le SOW Phase C
┌─ Phase C Implémentation (24 mois) ─ phase feedback ────┐
│  Implémentation par phases + **Gate C trimestriel :    │
│  re-vérifier le radar Stage 2**                        │
│  → La structure est-elle vraiment devenue plus ronde ? │
│     Sinon → retour à la Stage correspondante, ajuster  │
│     la Roadmap                                          │
│  → Outputs trimestriels : records de revue radar +    │
│     notes de correction de Roadmap                     │
└────────────────────────────────────────────────────────┘
```

| Phase | Durée | Étapes | Outils principaux | Livrables principaux |
| --- | --- | --- | --- | --- |
| **Phase A Diagnostic** | 2 semaines | Stage 1-4 | TOOLKIT première moitié + sélecteur FRAMEWORKS | **Rapport intermédiaire** + radar Reference Model signé |
| **Phase B Stratégie** | 4 semaines | Stage 5-8 | TOOLKIT seconde moitié + REPORT_PRODUCTION_WORKFLOW + REPORT_TEMPLATE | **Rapport complet 14 chapitres** + Roadmap + ROI + gouvernance |
| **Phase C Implémentation** | 24 mois | Revue trimestrielle de Stage 2 | Outil de revue radar trimestrielle TOOLKIT + Risk Register | **Records de revue radar trimestrielle** + corrections de Roadmap |

> Logique : `CONSULTING_TOOLKIT_TEMPLATES` est « les outils de diagnostic + l'outil de revue trimestrielle » ; `CONSULTING_FRAMEWORKS_LIBRARY` est « quel framework d'analyse à chaque étape » ; `REPORT_PRODUCTION_WORKFLOW` est « comment transformer efficacement le diagnostic en livrable » ; `CONSULTING_REPORT_TEMPLATE` est « à quoi ressemble le rapport final ». Ensemble = **méthodologie complète de boucle fermée de conseil** (pas un marathon linéaire).

> 📖 Script complet de dialogue 8 étapes + story de boucle fermée : [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) (inclus conclusion « pourquoi la boucle fermée est de la science »).

## 5. Descriptions de Fichiers

### `CONSULTING_REPORT_TEMPLATE.md`

Modèle Markdown du rapport de diagnostic de transformation IA (v2.0 aligné 8 étapes). 14 chapitres fixés : couverture, Executive Summary (incl. vue d'ensemble des lacunes standard), méthode de diagnostic, As-Is Snapshot, Reference Model Alignment (double coordonnée APQC + Tiger AI), Best Practice Integration (profil d'excellence), Gap Analysis, Executive Problem Statement, Phased Goals, To-Be Design, Implementation Roadmap, Change Management Plan, Governance Design, Value Tracking & Risk Register, recommandations SOW.

### `CONSULTING_TOOLKIT_TEMPLATES.md`

**Tableaux d'outils directement utilisables** du diagnostic de conseil en 8 étapes (v2.0 image-aligned). Chaque étape mappe à 1-5 outils : banque d'entretien 40 questions, inventaire AI/système, swimlane As-Is, **sélection Reference Model (APQC/SCOR/eTOM/ITIL/CMMI) + Mapping Worksheet + Standard Gap Checklist + double radar**, Best-Practice Profile + profil d'excellence, Missing/Broken/Redundant (**pas évaluation de risque**), Impact×Effort, **convergence 80/20 + 5 Whys**, Problem Statement, **Ultimate Benchmark → Phased Goals + évaluation absorption organisationnelle**, **Phased To-Be Operating Model + Human-AI Collaboration (HITL)**, Skill/Workflow/Agent Map, Transformation Roadmap, **Change Management Playbook (incl. gestion résistance)**, RACI, permissions, **Value Tracking Matrix (Temps/Qualité/Échelle/Risque/Assets 5 dimensions)**, Risk Register, Audit, Ethics, **planning standard Phase A 2W + Phase B 4W + outil revue radar trimestrielle Phase C** (boucle fermée de conseil). Prêt à copier-coller.

### `CONSULTING_FRAMEWORKS_LIBRARY.md`

Bibliothèque de frameworks de conseil classiques. 50+ frameworks de l'industrie (MECE, Pyramid Principle, Issue Tree, Porter's 5 Forces, SWOT, BCG Matrix, 5 Whys, Fishbone, Business Model Canvas, WBS/RACI, NPV/IRR, Lean/Six Sigma, etc.) en 7 catégories. Inclut un « sélecteur de framework » (langage naturel → combinaison de frameworks), « chaînes de combinaison », chaque framework mappé sur les 8 étapes, et §4.8 approfondissement sur MECE / Issue Tree / formation d'hypothèses. Adapté de yoichiojima-2/consultant (MIT).

### `REPORT_PRODUCTION_WORKFLOW.md`

Workflow de production en 8 étapes pour « problème → rapport/deck livrable ». Inclut Dummy Page (squelette d'abord, remplir ensuite), gestion des dépendances, 7 layouts de page, piste d'evidence Excel, divulgation progressive, §9 troubleshooting playbook (7 problèmes courants + corrections). Adapté de Kafurtan/mckinsey-consultant-skills (MIT).

### `*_EN.md`

Versions anglaises sibling des fichiers ci-dessus.

## 6. Mapping vers Autres Répertoires

| Répertoire | Relation avec ce répertoire | Flux de données |
| --- | --- | --- |
| `01_Assessment` | Scores et radar du diagnostic sont input central de Stage 1 | `01` scores → `03` rapport |
| `02_Course_Design` | Output et observations en cours sont matière pour le chapitre « observations de cours » | `02` observations → `03` rapport |
| `00_Overview` | Le rapport est la phase « Deliver » de la story | `00` story → `03` réalisation |
| `04_Scenarios` | Stage 3 benchmark Best Practice industriel cite des cas | `04` cas → `03` Stage 3 |
| `06_Delivery` | Le rapport est la livraison centrale du package ; mappe au Handover | `03` rapport → `06` acceptation livraison |
| `90_References` | Citations tierces pour la bibliothèque de frameworks et workflow rapport (consultant / mckinsey-skills) | `90` citation → `03` |

## 7. Scénarios d'Usage Communs (par phase de boucle fermée)

- **Onboarding nouveau consultant** : d'abord lire `CONSULTING_TOOLKIT_TEMPLATES.md` et parcourir tous les samples, puis lire [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) pour le script de dialogue, enfin shadower un vrai entretien.
- **Phase A Diagnostic (2 semaines)** : utiliser outils TOOLKIT Stage 1-4 (entretien 40 questions, inventaire AI/système, radar Reference Model), produire en fin de période **rapport intermédiaire** pour signature Sponsor.
- **Phase B Stratégie (4 semaines)** : utiliser outils TOOLKIT Stage 5-8 + `REPORT_PRODUCTION_WORKFLOW.md` production 8 étapes pour transformer diagnostic en deck, remplir dans `CONSULTING_REPORT_TEMPLATE.md`, produire **rapport complet 14 chapitres + Roadmap 24M + ROI**.
- **Phase C Implémentation (24 mois, phase de feedback boucle)** : trimestriellement avec l'outil de revue radar TOOLKIT, **relancer le radar Reference Model Stage 2** — comparer contre version signée Phase A, voir si « la structure est devenue réellement plus ronde » ; sinon → retour à la Stage correspondante, ajuster Roadmap.
- **Client demande « pourquoi ce framework »** : utiliser le sélecteur de framework dans `CONSULTING_FRAMEWORKS_LIBRARY.md` pour expliquer.
- **Client demande « que se passe-t-il après les 6 semaines ? »** : montrer [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 diagramme complet de boucle fermée — le point n'est pas les 6 semaines, c'est Phase C 24 mois + mécanisme de falsification par revue radar trimestrielle.
