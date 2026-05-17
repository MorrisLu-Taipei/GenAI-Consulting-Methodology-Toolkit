# Flow consulting 8-stades : Histoire de scénario complète et conception en boucle fermée

> 🌐 Langue : [繁體中文](EIGHT_STAGE_FLOW_STORY.md) ｜ [English](EIGHT_STAGE_FLOW_STORY_EN.md) ｜ [Deutsch](EIGHT_STAGE_FLOW_STORY_DE.md) ｜ Français ｜ [Español](EIGHT_STAGE_FLOW_STORY_ES.md) ｜ [日本語](EIGHT_STAGE_FLOW_STORY_JA.md) ｜ [한국어](EIGHT_STAGE_FLOW_STORY_KR.md)
>
> Apache License 2.0 · Auteur : Morris Lu · Tiger AI

Dernière mise à jour : 2026-05-15

---

> **Ce que c'est** : La méthodologie consulting en 8 stades écrite comme histoire en boucle fermée complète, reproductible, débattable. De l'intake questionnaire au plan d'implémentation, chaque étape a triggers clairs, deliverables, signatures et relations de lock-in avec l'étape suivante.
>
> **Ce que ce n'est pas** : pas un récit marathon linéaire de 6 semaines. Plutôt **un modèle de contrat à 3 phases + signature client mid-engagement + loopback trimestriel** processus complet de management scientifique.

---

## 0. Améliorations sur un walk-through linéaire (3 meilleurs choix de design)

Intuition typique de l'utilisateur :
> Questionnaire + AI As-Is assessment → comparer à RM → maturity + cas benchmarking → score → montrer rapport client → client choisit Ideal Practice → analyser ce qui est nécessaire → recommendations TO-BE → rapport consulting → plan d'implémentation

**La direction est juste**. Tiger AI construit 3 améliorations sur ceci :

| # | Amélioration | Pourquoi plus fort |
| --- | --- | --- |
| **1** | **Trois phases de contrat** (Phase A Diagnostic / Phase B Strategy / Phase C Implementation), pas un marathon de 6 semaines | Client commit à risque-bas d'abord à Phase A, décide sur B / C basé sur résultats ; consultant évite over-committing |
| **2** | **Fin de Phase A : un Mid-Engagement Assessment Report est signé comme deliverable** avant lancement du workshop Phase B Ideal Practice | Client choqué par les cellules vides du radar d'abord, puis choisit Ideal — évite fantasme ; mid-report est aussi un deliverable standalone |
| **3** | **Chaque trimestre, revisiter le radar Reference Model** (continue après entrée Phase C Implementation) | Pas « fait c'est bien » mais **« la structure est-elle réellement devenue plus ronde ? »** — c'est le mécanisme de falsification en boucle fermée scientifique |

> **Pourquoi plus fort qu'un marathon linéaire de 6 semaines** : linéaire force le client à committer 6 semaines + 24 mois d'un coup — barrière psychologique trop haute ; 3 phases divisent décisions, réduisent risque, augmentent acceptance.

---

## 1. Vue d'ensemble modèle contrat trois-phases

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  Phase A: Diagnostic           Phase B: Strategy           Phase C:        ║
║                                                            Implementation  ║
║  ─────────────                ─────────────              ─────────────     ║
║  2 semaines · NT$ 800K        4 semaines · NT$ 2M        24 mois · NT$ 7M ║
║                                                                             ║
║  Stage 1 + 2 + 3 matériaux   Stage 3 Ideal Practice      Stage 7 + 8        ║
║                                + Stage 4 + 5                                ║
║                                                            (radar revisit  ║
║                                                            trimestriel)   ║
║                                                                             ║
║  Deliverable :               Deliverable :               Deliverable :     ║
║  Rapport mid-engagement      Rapport diagnostic complet  Transformation    ║
║  d'assessment                + Ideal Practice            Roadmap +         ║
║  (client receipts)           définition (3-parties sign) Change Mgmt +     ║
║                                                          Value Tracking +  ║
║                                                          Logs trimestriels║
╚═══════════════════════════════════════════════════════════════════════════╝
                ↑                       ↑                       ↑
            Gate A                  Gate B                   Gate C
        Client décide de        Client décide de         Client décide chaque
        procéder à B           procéder à C             trimestre de continuer
```

**Signification scientifique** : chaque Gate est « un point de sortie où le client peut descendre » — le consultant **conçoit ceci seulement avec confiance** que le deliverable de la phase précédente est **assez bon pour que le client veuille continuer**.

---

## 2. Le protagoniste : Client M

> ⚠️ **« Client M / MingChang Packaging » est une entreprise fictive générée par IA**, PAS un client réel. Tous les chiffres scale, KPI, budget et timeline sont **seulement illustratifs**, à des fins pédagogiques de méthodologie. Voir [`../04_Scenarios/README_EN.md`](../04_Scenarios/README_EN.md) pour le disclaimer complet d'intégrité académique.

- **Industrie** : Packaging et testing de semi-conducteurs (FATP)
- **Scale** : 700 employés, NT$ 1,2 Mrd de revenu annuel
- **Trigger** : Trois concurrents directs ont déployé inspection qualité IA et complaint Agents ; commandes trimestrielles Client A ont chuté 18%
- **Pain points** : Complaint response 5 jours (industrie 1 jour) ; turnaround proposition 4 jours (industrie 1,5 jours) ; taux défauts 3,2% (industrie 1,8%)
- **Contraintes** : Plafond budget NT$ 8M ; données process on-prem ; IT 2 FTE, pas de croissance
- **Rôles** : CEO (Sponsor), COO, IT Director (AI Champion potentiel), QC Head, Sales Head, CS Head, HR, Compliance

---

## 3. Phase A : Diagnostic (2 semaines, NT$ 800K)

### Trigger

CEO de M Company reçoit email outreach Tiger AI + voit le repo de méthodologie open-source sur GitHub ; secrétaire planifie intro de 30 min.

### Pre-Engagement : Quick Survey 10-questions (envoyée la semaine suivante)

CEO auto-remplit la version 10-questions de [`01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) (5 min).

**Résultat auto-scoré** :

```
Radar 6-dimensions :
  Usage outils            1 / 4 (certains execs utilisent ChatGPT privé)
  Sédimentation connais.  0 / 4 (pas de Wiki, pas de SOP)
  Automatisation process  1 / 4 (Finance 1 flow Power Automate)
  Intégration système     2 / 4 (ERP/CRM en silos)
  Application Agent       0 / 4 (aucune)
  Governance & ROI        1 / 4 (pas d'AI policy)
Total : 5 / 24 → L1 préliminaire
```

CEO voit le radar → **premier choc** → accepte de signer contrat Phase A.

### Flow Phase A (Semaine 1-2)

#### Semaine 1 ── Stage 1 As-Is Snapshot : Écouter, Observer, Pas de Commentaire

| Jour | Action | Tool | Output |
| --- | --- | --- | --- |
| Jour 1-2 | Interviews exec (CEO/COO/CIO × 60 min) + interviews dept head (QC/Sales/CS/IT/HR × 90 min) | Tool 1.1 (40-Q bank) | Enregistrements + résumés |
| Jour 3 | Interviews opérateurs (Line/Sales/CS × 3 chacun × 30 min) | Tool 1.1 Section C | Résumés |
| Jour 4 | AI Usage Inventory + Systems Inventory | Tool 1.2 + 1.3 | Shadow IT risk map + system map |
| Jour 5 | Walkthrough de 3 key processes + dessiner Swimlanes | Tool 1.4 | 3 As-Is Process Maps |

**Fin Semaine 1** : Consultant dit au client « maintenant nous savons ce que votre entreprise fait. » **Pas de commentaire, pas de recommandation.**

#### Semaine 2 ── Stage 2 Reference Model Alignment + Stage 3 Material Prep

| Jour | Action | Tool | Output |
| --- | --- | --- | --- |
| Jour 6 | Choisir Reference Model : SCOR + APQC + Tiger AI L1-L5 | Tool 2.1 | RM selection rationale |
| Jour 7-8 | Mapping Worksheet : localiser As-Is dans cellules RM | Tool 2.2 | Table mapping |
| Jour 9 | Standard Capability Gap Checklist + dual radar | Tool 2.3 + 2.4 | Deux radars (APQC + Tiger AI) |
| Jour 10 | Prep cas benchmark (choisir semi-conducteur parmi 5 stubs + 2 cas même industrie) | Tool 3.1 + 3.3 | 3 Best-Practice Profiles |

> **Discipline Phase A** : Jour 10 consultant **ne lance PAS ENCORE le workshop Ideal Practice**. Matériaux seulement — utilisés à la phase suivante.

### Phase A Deliverable : Mid-Engagement Assessment Report (client receipts)

**Jour 11-12 écrire rapport → Jour 13-14 client review → Jour 14 closeout meeting**

Rapport mid-engagement (10-15 pages) :

1. **Executive Summary** : « Par standards internationaux, votre entreprise montre gaps structurels en SCOR Make/Deliver, APQC 11.x Knowledge, Tiger AI L1-L3. »
2. **As-Is Snapshot** : résumés interviews + system map + 3 Swimlanes
3. **Reference Model Mapping** : Standard Capability Gap Checklist
4. **Dual radar** : APQC + Tiger AI L1-L5 (pointillé = benchmark, plein = entreprise)
5. **Matériaux Industry Best Practice** : 3 Benchmark Profiles même industrie (matériaux seulement — **pas encore de conclusions tirées**)
6. **Recommandation phase suivante** : Phase B Ideal Practice Workshop (demi-journée) + analyse Stage 4-5

### Gate A : Client Décide de Procéder à Phase B

**Ce qui arrive au closeout meeting** :

- CEO voit radar : « Je pensais qu'on faisait okay — sous le standard ces cellules sont 0 ? » → **deuxième choc**
- COO feuillette Swimlanes : « Notre process de complaint a vraiment ces trous... » → pain points concrétisés
- IT Director voit dépense mensuelle shadow IT : « ChatGPT privé brûlant NT$ 24,000 avec données leakant... » → risque concrétisé

**90% des clients signent Phase B**. Parce que :

- Gaps radar ne sont pas dit-par-consultant — dit par standard international → **objectif**
- Pain est dans enregistrements interviews employés → **vérifiable**
- Firmes même industrie l'ont déjà fait → **atteignable**

> **Le but de design de Phase A EST ce choc** : client **voit le gap lui-même**, pas dit par consultant.

---

## 4. Phase B : Strategy (4 semaines, NT$ 2M)

### Semaine 3 ── Stage 3 Ideal Practice Co-Creation Workshop (demi-journée)

**Jour 15 matin** ─ Tool 3.6 Co-Creation Workshop

| Étape | Action | Temps | Output |
| --- | --- | --- | --- |
| 1. Material display | Consultant **montre seulement, ne recommande pas** Tool 3.1/3.3/3.4/2.7 architecture 4-couches | 30 min | Matériaux partagés |
| 2. Voting indépendant | Chaque personne **indépendamment** écrit sur sticky notes « ce que je veux qu'on devienne en 12 mois » | 45 min | N sticky notes |
| 3. Consensus collectif | Poster sur architecture 4-couches, trouver consensus / divergence | 60 min | Draft v1 Ideal Practice |
| 4. Reality check | Consultant intervient d'abord, utilisant Tool 6.3 pour challenge feasibility | 45 min | v2 Ideal Practice |
| 5. Define table | Écrire v2 comme « Ideal Practice Definition Table » | 30 min | Definition table version-signée |
| 6. **Signature 3-parties** | CEO + Sponsor + AI Champion | 15 min | Document public, auditable |

**Ideal Practice Definition Table signée de M Company (extrait)** :

| # | Capability | RM Category | Target 12-mois | Critères evidence |
| --- | --- | --- | --- | --- |
| 1 | Complaint response | APQC 4.4 + Tiger AI L3 | 90% en 1hr + 24hr human reply | n8n + taux Reviewer sign-off ≥ 95% |
| 2 | Sédimentation connaissance | APQC 11.x + Tiger AI L2 | ≥ 20 Skills ajoutés mensuel | Skill Library Git + Owner + IPOE |
| 3 | Process root cause | SCOR Make + Tiger AI L4 | Anomalie → hypothèse ≤ 1hr | Hermes Agent + 5 tasks Reviewer pass |

> **Cette table est l'ancre de tout l'engagement**. Tous les calculs Stage 4-8 subséquents sont basés dessus ; le client ne peut nier ses propres targets signés.

### Semaine 3-4 ── Stage 4 Gap Analysis + Stage 5 Problem Definition

#### Stage 4 : Gap = (Client Ideal − Client As-Is)

| Jour | Action | Tool | Output |
| --- | --- | --- | --- |
| Jour 16-17 | Classification M/B/R + Impact × Effort | Tool 4.1 + 4.2 | Gap matrix |
| Jour 18 | Prioritization Worksheet | Tool 4.3 | Ranking priorité |

#### Stage 5 : Convergence 80/20 vers Root Cause

| Jour | Action | Tool | Output |
| --- | --- | --- | --- |
| Jour 19 | Convergence 80/20 + 5 Whys | Tool 5.1 + 5.2 | Liste core lesion |
| Jour 20-21 | Executive Problem Statement | Tool 5.3 + 5.4 | Définition une-phrase |

**Executive Problem Statement de M Company** :

> M Company manque du rôle, outil et incitation pour « knowledge asset-isation. » 80% des gaps (complaints lents / quotes lents / pas de sédimentation connaissance / root cause lent) viennent de « la même chose faite à répétition, personne ne sédimente, personne ne réutilise. »

### Semaine 4 ── Stage 6 Phased Goals + Stage 7 To-Be Design

#### Stage 6 : Décomposer Ideal en étapes absorbables

| Jour | Action | Tool | Output |
| --- | --- | --- | --- |
| Jour 22 | Ultimate Ideal → décomposition Phase 1/2/3 | Tool 6.1 | Table de décomposition |
| Jour 23 | Évaluation d'absorption organisationnelle (6 dimensions) | Tool 6.3 | Absorption score |
| Jour 24 | Stage Gate Criteria | Tool 6.2 | Checklists L1-L5 Gate |

> **L'évaluation d'absorption de M Company trouve qu'IT n'a que 2 FTE ; Phase 2 a besoin de +0,5**. Décision : étendre Phase 2 de 6 → 9 mois. **Cet ajustement vient du client regardant les données lui-même, pas de recommandation consultant**.

#### Stage 7 : Un To-Be Operating Model par Phase

| Jour | Action | Tool | Output |
| --- | --- | --- | --- |
| Jour 25-26 | Phased To-Be Operating Models (3 diagrammes) | Tool 7.1 | 3 diagrammes |
| Jour 27 | Human-AI Collaboration + HITL nodes | Tool 7.2 | Split par-process |
| Jour 28 | Skill/Workflow/Agent Map + Integration Architecture | Tool 7.3-7.6 | 3 maps + Variant B Hybrid |

### Phase B Deliverable : Rapport diagnostic complet + Ideal Practice Definition Table

**Jour 29-30 écrire rapport → Jour 31-32 client review → Jour 32 closeout meeting**

Rapport diagnostic complet (30-50 pages) per structure 14-sections [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md).

### Gate B : Client Décide de Procéder à Phase C

**95% des clients signent Phase C**. Parce que :

- Ideal Practice a été **signée par eux** → indéniable
- Gap est calculé par soustraction → **vérifiable**
- Phase 1/2/3 fit l'absorption organisationnelle → **atteignable**

---

## 5. Phase C : Implementation (24 mois, NT$ 7M)

### Stage 8 Implementation & Change

**Premier mois (Mois 1)**

| Jour | Action | Tool | Output |
| --- | --- | --- | --- |
| Jour 33 | Transformation Roadmap (24 mo / 6 trimestres) | Tool 8.1 | Roadmap |
| Jour 34 | Change Management Plan + resistance Playbook | Tool 8.2 | Change plan |
| Jour 35 | RACI + Permission Matrix + Audit Log | Tool 8.3 + 8.4 + 8.7 | Docs gouvernance |
| Jour 36 | Value Tracking Matrix (5 dimensions) | Tool 8.5 | Dashboard spec |
| Jour 37 | Risk Register (incorporant case Failures) | Tool 8.6 | Risk log |
| Jour 38 | AI Ethics Checklist | Tool 8.8 | Signed ethics |
| Jour 39 | SOW + Phase 1 kickoff | — | Phase 1 lancée |

### Phase 1 (Mois 1-6) : Foundation

- L1 OpenWebUI pan-entreprise live
- 5 Skills core publiés
- AI policy signée par > 90%
- Prompt Library ≥ 30 entrées

**Fin Mois 6 → L1 Gate acceptance + revisit Stage 2 radar** :

```
APQC 11.x Knowledge:  0 → 2 (Skill library démarrage)
Tiger AI L1:          0 → 4 (OpenWebUI complet + 92% policy signée)
Tiger AI L2:          0 → 2 (5 Skills)
```

> Le radar **est réellement plus rond**. Client est ému : « Donc voilà management scientifique. »

### Phase 2 (Mois 6-15) : Optimization

- L2 Skill Library ≥ 15 entrées
- L3 n8n Workflow ≥ 3 live
- HITL nodes pleinement en place

**Fin Mois 15 → L2/L3 Gate + radar revisit** :

```
APQC 4.0 Deliver: 1 → 3 (complaint response 5 jours → 1 jour) ✓ Ideal atteint
APQC 11.x:        2 → 3 (sédimentation connaissance stable) ✓ Ideal atteint
Tiger AI L3:      0 → 2 (n8n PoC live)
```

### Phase 3 (Mois 15-24) : Excellence

- L4 Hermes Agent passe 4A-4E
- L5 ClawTeam cross-dept 1 répétition réussie

**Fin Mois 24 → L4/L5 Gate + radar final** :

```
SCOR Make + Tiger AI L4: 0 → 3 (Hermes Agent passe) ✓ Ideal atteint
Tiger AI L5:             0 → 2 (ClawTeam cross-dept répétition)
```

### Gate C Trimestriel : Client Peut Décider Chaque Trimestre

Chaque trimestre doit :

1. Quarter Gate acceptance (per Tool 6.2 checklist)
2. Revisit Stage 2 radar (quantifier amélioration)
3. Value tracking matrix review 5-dimensions
4. Client décide d'avancer, ajuster ou pauser le trimestre suivant

> Après 24 mois : M Company complaint response 1 jour, taux défaut 2,0%, churn client zéro, Stage 2 radar **change de ligne en dents de scie à presque rond**.

---

## 6. Diagramme complet de boucle fermée

```
                          ┌──────────────────┐
                    ┌────►│ Phase A Diag 2W   │
                    │     │ Stage 1 + 2 + 3   │
                    │     │   prep matériaux  │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Mid Report        │ ← Phase A Deliverable
                    │     │ (client receipts) │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate A
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase B Strat 4W  │
                    │     │ Stage 3 Ideal     │
                    │     │ + Stage 4 + 5     │
                    │     │ + Stage 6 + 7     │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Rapport complet   │ ← Phase B Deliverable
                    │     │ + Ideal Practice  │
                    │     │ (sign 3-parties)  │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate B
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase C Impl 24M  │
                    │     │ Stage 8           │
                    │     │ Transformation +  │
                    │     │ Change + Value    │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase 1/2/3       │
                    │     │ Stage Gate accept │
                    │     └────────┬─────────┘
                    │              │
                    │     Gate C trimestriel
                    │              │
                    │     ┌────────▼─────────┐
                    └─────┤ Revisit Stage 2 │
                          │ Radar (plus rond?)│
                          └──────────────────┘
                                  
                          Cette ligne de feedback
                          est le mécanisme core
                          de falsification de la
                          boucle fermée scientifique
```

---

## 7. Pourquoi ce flow résiste au débat client

Pour chaque challenge possible, la location de réponse :

| Challenge | Location | Evidence |
| --- | --- | --- |
| « Comment savez-vous qu'on est à L1 ? » | Phase A mid-report §2 radar | Survey 10-Q + enregistrements + system inventory |
| « Pourquoi ces cellules sont 0 ? » | Phase A §3 RM Mapping | Standards publics APQC / Tiger AI |
| « Qui a fixé le target ? » | Phase B §5 Ideal Practice table | **Client lui-même signé, signature 3-parties** |
| « Pourquoi le gap est si grand ? » | Phase B §6 Gap Analysis | Formule Gap = (votre Ideal signé − votre As-Is) |
| « Pourquoi customer service avant sales ? » | Phase B §6.2 | Matrix Impact × Effort |
| « Pourquoi 24 mois ? » | Phase B §8 + Tool 6.3 | Case Benchmark + Organizational Absorption |
| « Et si ça ne marche pas ? » | Phase C §13 Risk Register | Trigger + Owner + Mitigation |
| « Comment prouvez-vous que ça a amélioré ? » | Quarterly Gate C | Stage 2 radar + Value Tracking 5 dimensions |
| « Dernier consultant a dit L3, vous dites L2 — qui a raison ? » | Échelle 0-4 publique + evidence | Tout tiers peut vérifier indépendamment |

---

## 8. Mapping sur le flow original de l'utilisateur

| Étape utilisateur | Phase | Stage | Amélioration |
| --- | --- | --- | --- |
| 1. Questionnaire + AI As-Is | Phase A W1 | Stage 1 | + 10-Q quick screen comme pre-engagement |
| 2. Comparer à RM | Phase A W2 | Stage 2 | Architecture 4-couches + dual radar |
| 3. Maturity + cas benchmarking → score | Phase A fin W2 | Stage 3 matériaux | Cas doivent être Benchmark-grade (9 champs) |
| 4. **Client voit rapport assessment** | **Phase A Deliverable** | — | **Nouveau : mid-report comme deliverable standalone + client receipt** |
| 5. Client choisit Ideal Practice | Phase B W3 | Stage 3 Tool 3.6 | **Client signe, pas consultant prescrit** |
| 6. Analyser ce qui est nécessaire | Phase B W3-W4 | Stage 4 + 5 | Gap = Ideal − As-Is, convergence 80/20 |
| 7. Recommendations TO-BE | Phase B W4 | Stage 6 + 7 | Phased + évaluation Organizational Absorption |
| 8. Rapport consulting | Phase B Deliverable | — | Rapport complet 14-sections + Ideal Practice signée |
| 9. Plan d'implémentation | Phase C kickoff | Stage 8 | Change Mgmt + Value Tracking + Audit |
| **(manquant)** | **Revisit trimestriel** | — | **Nouveau : chaque trimestre revisit Stage 2 radar (boucle fermée scientifique)** |

---

## 9. Relation aux autres documents

| Document | Relation à celui-ci |
| --- | --- |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 | Fournit définitions 8-stages et flow de données ; ce doc est la narrative complète du process |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Fournit argument scientifique « pourquoi conçu ainsi » ; ce doc est « comment ça tourne réellement » |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | Fournit tables d'outils par-stage |
| [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) | Fournit structure 14-sections du Phase B Deliverable |
| [`../04_Scenarios/`](../04_Scenarios/) | Fournit cas Benchmark-grade pour Phase A |
| [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) | Fournit SOP engagement / pricing / delivery |

---

## 10. Clôture : Pourquoi la boucle fermée est science

Ce flow **n'est pas un marathon linéaire** mais **une boucle fermée avec feedback** :

- **Chaque Gate est un point de sortie** → consultant **a confiance** pour concevoir ainsi (le deliverable précédent doit être assez bon pour que le client veuille continuer)
- **Chaque Deliverable a signature client** → raisonnement subséquent ne peut être nié
- **Chaque trimestre revisit Stage 2 radar** → structure réellement devenant plus ronde = succès, pas « PoC fait = succès »

**C'est management scientifique** :

- Point de départ objectif (standard international + signature client)
- Process vérifiable (chaque Stage Gate Criteria)
- Point final falsifiable (dual radar before/after + Value Tracking 5 dimensions)

Si quelqu'un dit « la méthodologie Tiger AI ne marche pas », ils doivent **challenger** :

- APQC PCF est-il faux ?
- L'école Rosemann BPM est-elle fausse ?
- L'Ideal Practice signée par le client lui-même ne compte pas ?
- Notre loopback radar trimestriel ne compte pas ?

**Difficile à faire.** C'est pourquoi nous avons investi dans ce design en boucle fermée.

---

Licence & Citation

Ce document est sous Apache License 2.0 ; peut être utilisé, modifié, commercialisé, à condition de préserver l'attribution [`../NOTICE`](../NOTICE).
