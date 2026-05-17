# Pilot Study Protocol : Plan de recherche de validation empirique pour la méthodologie Tiger AI

> 🌐 Langue : [繁體中文](PILOT_STUDY_PROTOCOL.md) ｜ [English](PILOT_STUDY_PROTOCOL_EN.md) ｜ [Deutsch](PILOT_STUDY_PROTOCOL_DE.md) ｜ Français ｜ [Español](PILOT_STUDY_PROTOCOL_ES.md) ｜ [日本語](PILOT_STUDY_PROTOCOL_JA.md) ｜ [한국어](PILOT_STUDY_PROTOCOL_KR.md)
>
> Apache License 2.0 · Auteur : Morris Lu · Tiger AI

Dernière mise à jour : 2026-05-16
Version : v1.0 Research Design Protocol (pre-registration ready)

---

> **Objectif** : Faire évoluer la méthodologie Tiger AI d'un « framework de consulting bien conçu » à un « modèle recherchable ». Ce protocole définit une étude pilote empirique de 18-24 mois sur 5-10 entreprises, **soumettant la méthodologie à la falsification externe plutôt qu'à la seule auto-validation**.
>
> Ceci est un **document de design de recherche** prêt pour soumission IRB / pre-registration académique / candidatures à des subventions gouvernementales de recherche.

---

## 1. Contexte & Motivation

### 1.1 Pourquoi la recherche empirique

Force de l'evidence actuelle de la méthodologie Tiger AI :

| Élément | Evidence Level (Tool 8.9) | Statut |
| --- | --- | --- |
| Design du flow à 8 stades | L2 argument documentaire | Complet (Rosemann BPM + intégration de frameworks industriels) |
| 6 constructs × échelle 0-4 | L2 consensus d'experts | Complet (**pas de validation psychométrique**) |
| Bibliothèque de 7 cas | L2 composite anonymisé | Complet (**pas de vraies données longitudinales**) |
| Self-qualification (Tool 2.5) | L1 self-report | Complet (**auto-référentiel, pas validé externement**) |
| Inter-rater consistency | — | **Non fait** |
| Réponse KPI longitudinale à la méthodologie | — | **Non faite** |

**Conclusion** : La méthodologie est mature en « cohérence interne + fermeture logique » mais n'a pas été testée empiriquement pour « reproductibilité externe + validité prédictive ». Cette étude pilote adresse les deux.

### 1.2 Questions de recherche

**RQ1 — Inter-rater Reliability** : Différents consultants utilisant la même méthode peuvent-ils scorer la même entreprise de manière cohérente ?

- **H1** : Cohen's κ ≥ 0.60 (substantial agreement)

**RQ2 — Cohérence interne** : Quelle est la cohérence interne des 6 constructs ?

- **H2** : Cronbach's α ≥ 0.70 par construct

**RQ3 — Validité de construct** : Les 6 constructs émergent-ils proprement dans l'analyse factorielle ?

- **H3a** : EFA extrait 5-6 facteurs ; chaque item charge ≥ 0.5 sur son facteur assigné
- **H3b** : CFA modèle 6-facteurs fit : CFI ≥ 0.90, TLI ≥ 0.90, RMSEA ≤ 0.08

**RQ4 — Validité prédictive** : Les scores T0 peuvent-ils prédire l'amélioration des KPI business à T+12 mois ?

- **H4** : Contrôlant pour KPI baseline et taille d'entreprise, le score de maturité Tiger AI prédit positivement l'amélioration KPI à +12m (β ≥ 0.30, p < 0.05)

**RQ5 — Pattern longitudinal** : Les entreprises complétant Phase C 24 mois montrent-elles des radars « plus ronds » ?

- **H5** : T0 vs T24 aire de radar (somme 6-constructs) augmente significativement, et la croissance de chaque construct suit la décomposition Tool 6.1 (foundation → optimization → excellence)

---

## 2. Design d'étude

### 2.1 Type de design

- **Étude longitudinale mixed-methods**
- **Convergent parallel design** : quantitatif (scale scoring, KPIs) + qualitatif (interviews semi-structurées, case studies) simultanément
- **Pre-registered** (hypothèses publiques, sampling, plan d'analyse ; évitant p-hacking)

### 2.2 Sample

| Item | Spécification |
| --- | --- |
| **Sample N cible** | 5-10 entreprises (stage pilote ; main study N=200+ pour CFA) |
| **Diversité industrie** | ≥ 3 industries (≥ 1 chacune de mfg, services, secteur public) |
| **Taille entreprise** | 100-5000 employés |
| **Point de départ IA** | L0-L2 (déjà L3+ exclu en raison d'espace d'intervention limité) |
| **Durée de commitment** | 18 mois (accord de collaboration de recherche) |
| **Incentive** | Consulting gratuit / discounted + opportunité de co-publication + contrôle d'anonymisation de cas |

### 2.3 Stratégie de recrutement

1. Via communauté n8n Taipei Ambassador, NTUST Intelligent Manufacturing, alumni QUT
2. Sollicitation publique + repo Apache 2.0 open comme signal de confiance
3. Accord de collaboration de recherche signé (usage de données, anonymisation, mécanisme d'exit)

### 2.4 Éthique / IRB

- Postuler pour approbation IRB NTUST ou QUT
- Consentement éclairé : tous participants par écrit
- Gestion de données sensibles : grading PII / secret business ; isolation de données double-blind
- Droit de retrait : toute entreprise peut sortir à tout moment ; données collectées retournées ou détruites

---

## 3. Design de scoring double-blind

### 3.1 Objectif

Valider l'**inter-rater reliability** du modèle de scoring Tiger AI.

### 3.2 Design

```
Phase de scoring T0 (par entreprise) :
  ↓
  Consultant A complète indépendamment :
    • Interviews (Tool 1.1 40-Q bank)
    • Inventory + Swimlane (Tools 1.2-1.4)
    • Reference Model Mapping (Tool 2.2)
    • 6-construct 0-4 scoring (Tool 2.3)
    • Jugement primaire de maturité (L1-L5)
  ↓
  Consultant B complète indépendamment (même entreprise, blinded à A) :
    • Répète toutes actions ci-dessus
  ↓
  Analyste de recherche (neutre) compare A vs B :
    • Gap de score 6-construct (weighted kappa)
    • Agreement de jugement primaire de maturité (unweighted kappa)
    • Overlap d'identification de gap (overlap tableau M/B/R)
```

### 3.3 Statistiques de cohérence

| Métrique | Tool | Interprétation |
| --- | --- | --- |
| **Cohen's κ (unweighted)** | κ = (Po - Pe) / (1 - Pe) | < 0.20 slight ; 0.21-0.40 fair ; 0.41-0.60 moderate ; 0.61-0.80 substantial ; > 0.80 almost perfect |
| **Weighted κ (linear / quadratic)** | Pour échelle ordinale (0-4) | Comme ci-dessus, mais plus strict sur « 1 point off » vs « 4 points off » |
| **ICC (Intraclass Correlation)** | Modèle mixte two-way | < 0.5 poor ; 0.5-0.75 moderate ; 0.75-0.9 good ; > 0.9 excellent |
| **Bland-Altman plot** | Visualiser le gap de score | Détecter le bias systématique |

---

## 4. Tracking longitudinal de KPI

### 4.1 Timepoints de mesure de KPI

| Timepoint | Nom | Mesure |
| --- | --- | --- |
| **T0** | Baseline | Après Phase A, avant Phase B |
| **T+6m** | Fin Phase 1 | L1 Gate Acceptance |
| **T+12m** | Milieu Phase 2 | L2/L3 Gate |
| **T+18m** | Fin Phase 2 | L3 complet |
| **T+24m** | Fin Phase 3 | L4/L5 Gate |

### 4.2 5 dimensions KPI (par Tool 8.5 Value Tracking)

| Dimension | KPIs exemple |
| --- | --- |
| **Time** | Complaint response, proposal turnaround, month-end close, decision cycle |
| **Quality** | Taux de défaut, taux d'erreur, complaint count, rework rate |
| **Scale** | Throughput, beneficiaries, automated task count |
| **Risk** | Missed case rate, compliance violations, sensitive-data leakage |
| **Assets** | Skill count, Wiki entries, Agent task count, training completion |

### 4.3 Qualité de données KPI (par Tool 8.9 Evidence Hierarchy)

- **L3 obligatoire** : Tous les KPIs time / scale depuis system logs (n8n / Audit Log / ERP)
- **L4 recommandé** : Sample-verifié par internal audit / external accountants
- **L1-L2 supplémentaire** : Employee NPS / interview summaries

---

## 5. Qualitatif : Interviews semi-structurées

### 5.1 Timepoints d'interview

Par entreprise : T0, T+6m, T+12m, T+18m, T+24m — 1 tour chacun (par interviewee).

### 5.2 Interviewees

- CEO / Sponsor
- AI Champion
- IT Lead
- ≥ 2 Department Heads
- ≥ 3 Front-line Users

### 5.3 Questions d'interview (extrait)

1. Quel est le changement IA le plus impactful des 6 derniers mois ?
2. Quels changements IA attendus ne sont pas arrivés ? Pourquoi ?
3. L'attitude du personnel / département envers IA a-t-elle shifté ?
4. Recommanderiez-vous / ne recommanderiez-vous pas cette méthodologie à des pairs ?
5. Quel Stage / Tool a été le plus utile ? Le moins ?
6. Cross-time : en regardant l'Ideal Practice signée il y a 12 mois, des regrets ?

### 5.4 Analyse qualitative

- Transcription verbatim + coding (NVivo / Atlas.ti)
- Reliability dual-coder ≥ 80%
- Analyse thématique pour extraire patterns / counter-examples

---

## 6. Plan d'analyse statistique

### 6.1 Statistiques descriptives

- Distribution de score par construct (mean, SD, median, IQR)
- Visualisation radar chart T0 vs T24
- Matrice de corrélation 6-construct (check de multicollinéarité)

### 6.2 Reliability & Validity

| Analyse | Tool | Mappe à l'hypothèse |
| --- | --- | --- |
| Cronbach's α | SPSS / R `psych::alpha()` | H2 |
| EFA + Bartlett's + KMO | SPSS / R `psych::fa()` | H3a |
| CFA + fit indices | Mplus / R `lavaan::cfa()` | H3b (**N ≥ 200 requis**) |
| Cohen's κ | R `irr::kappa2()` | H1 |
| ICC | R `irr::icc()` | H1 |

### 6.3 Statistiques inférentielles

| Analyse | Hypothèse | Tool |
| --- | --- | --- |
| Paired t-test (T0 vs T24) | H5 augmentation aire de radar | R `t.test(paired=TRUE)` |
| Mixed-effects model | H4 validité prédictive | R `lme4::lmer()` |
| ANCOVA | Contrôler KPI baseline + size | R `aov()` |
| Analyse de sensibilité | Contre missing data + dropout | R `mice` multiple imputation |

### 6.4 Significance & Ajustement

- α = 0.05 test principal
- Bonferroni correction pour multiple comparisons
- Reporting d'effect size : Cohen's d, η², partial η²

---

## 7. Timeline & Milestones

```
Mois 0 :     Finaliser design + soumission IRB
Mois 1-3 :   Recruter 5-10 entreprises + signer accord de recherche
Mois 4 :     Former Consultant A/B (SOP double-blind)
Mois 5-6 :   Scoring double-blind T0 + mesure KPI Baseline
Mois 6-12 :  Intervention Phase 1 + scoring T+6m + interviews
Mois 12-18 : Intervention Phase 2 + T+12m + T+18m
Mois 18-24 : Intervention Phase 3 + scoring final T+24m + interviews
Mois 24-27 : Analyse + rapport de recherche + soumission journal
Mois 27-30 : Revisions + soumission
```

---

## 8. Estimation budget

| Item | Est. (NT$) |
| --- | --- |
| Temps consultant (A + B 80-120 hrs chacun par entreprise) | 6-9M |
| Personnel de recherche (comparaison de scoring neutre + analyse qualitative) | 1.5-2.5M |
| Outils KPI system-log + transcription d'interview | 0.5-1M |
| IRB / legal / consultant statistique | 0.5-1M |
| Outils open-source + cloud data store | 0.3-0.5M |
| Contingence (15%) | 1.3-2M |
| **Total** | **NT$ 10.1-16M** |

⚠️ En échange de consulting gratuit, 5-10 entreprises committent à 18 mois de collecte de données → labor consultant offsetable par « equivalent consulting service », **outlay cash réel réductible à NT$ 4-7M**.

---

## 9. Stratégie de publication

### 9.1 Outputs attendus

| Output | Journal / Plateforme | Timing est. |
| --- | --- | --- |
| **Pre-registration** | OSF | Mois 0 |
| **Protocol paper** | BMJ Open / Pilot and Feasibility Studies | Mois 3 |
| **Methodology paper** | MIS Quarterly / Information Systems Research / Journal of Business Research | Mois 27 |
| **Industry white paper** | Bilingue, public Apache 2.0 | Mois 27 |
| **Case studies (anonymisées)** | HBR-style cases | Mois 30 |
| **Practitioner guide** | Mettre à jour toolkit + ajouter evidence empirique | Mois 30 |

### 9.2 Commitment Open Science

- Toutes données de recherche (de-identifiées) publiques sur OSF
- Scripts statistiques R / Python sur GitHub
- Identité d'interviewee confidentielle ; résultats agrégés entièrement transparents

---

## 10. Risques & Mitigation

| Risque | Probabilité | Impact | Mitigation |
| --- | --- | --- | --- |
| Withdrawal d'entreprise à mi-chemin (dropout) | Med | High | Over-recruter 12 ; analyse intention-to-treat |
| Bias / leakage Consultant A/B | Low | High | Formation SOP + audits + double-blind strict + bureaux différents |
| KPI system log inaccessible | Med | Med | T0 IT confirme disponibilité log ; indicateurs de substitution sinon |
| Délai de revue IRB | Med | Med | Soumission IRB Mois 0 concurrent avec recrutement |
| N insuffisant pour CFA | High | Med | EFA au pilote ; CFA attend main study N=200+ |
| Shortfall budget | Med | High | Postuler grants NSTC / MOE / QUT ; cost-sharing multi-entreprise |

---

## 11. Stopping Rules

Terminaison anticipée avec disclosure complète si :

- ≥ 50% entreprises se retirent
- Inter-rater κ < 0.40 (méthodologie incohérente → scale a besoin de redesign)
- IRB révoquée
- Issues éthiques sérieux (data leak, participant harm)

**Les études terminées de manière anticipée doivent toujours publier toutes les données collectées** (évitant publication bias).

---

## 12. Contributions attendues

| Contribution | Audience | Forme |
| --- | --- | --- |
| **Théorie** : premier modèle de maturité d'adoption GenAI empiriquement validé | Académie (IS / BPM / Strategy) | Paper peer-reviewed |
| **Méthode** : Cases-as-Benchmarks + protocole de workshop Client Ideal Practice | Industrie du consulting | Toolkit open-source (Apache 2.0) |
| **Politique** : evidence empirique pour alignment AI Governance | Régulateurs (Taiwan AI Basic Act / NIST / EU) | White paper + auditions législatives |
| **Industrie** : 5-10 cas réels longitudinaux d'entreprise | Clients pairs | Cas réels (remplaçant composites) |
| **Éducation** : intégrer dans curricula NTUST / QUT | Étudiants | Matériaux de cours |

---

## 13. Documents apparentés

| Document | Relation |
| --- | --- |
| [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) §3.1-3.3 | Définitions de constructs de scale ; cette étude valide |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Pourquoi la méthodologie a besoin de validation empirique |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | Failure modes connus → mitigation construite dans cette étude |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9 | Base Evidence Hierarchy pour grading d'evidence KPI |

---

## 14. Références

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297-334.
- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- Streiner, D. L., Norman, G. R., & Cairney, J. (2015). *Health measurement scales: A practical guide to their development and use* (5th ed.). Oxford University Press.
- Hair, J. F., et al. (2019). *Multivariate Data Analysis* (8th ed.). Cengage.
- Creswell, J. W. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). SAGE.
- Open Science Framework : <https://osf.io/>

---

Licence & Citation

Ce document est sous Apache License 2.0 ; peut être utilisé, modifié, commercialisé, à condition de préserver l'attribution [`../NOTICE`](../NOTICE). D'autres équipes de recherche peuvent **adopter, modifier, répliquer librement** ce design, à condition de suivre les mêmes commitments de pre-registration et open-science.
