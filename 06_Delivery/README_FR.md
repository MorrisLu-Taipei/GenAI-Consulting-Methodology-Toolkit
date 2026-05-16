# 06 Delivery — Acceptation de Livraison & Opérations d'Engagement

> 🌐 中文 / Chinese : [README.md](README.md) ｜ English : [README_EN.md](README_EN.md)

## 1. Objectif de ce Répertoire

Ce répertoire a deux niveaux qui résolvent ensemble une chose : **comment transformer un mandat de conseil professionnellement et de façon scalable en « business » et le « livrer ».**

- **Couche acceptation de livraison** : définit ce que ce programme livre au client, comment c'est accepté, quelle evidence prouve la complétion.
- **Couche opérations d'engagement** : définit tout le cycle d'engagement (Sales → Delivery → Support), SOP de rôles, modèles de documents commerciaux, checklists opérationnelles, gestion pricing et risque.

`01`-`03` sont « ce que fait le consultant » (méthodologie) ; `05` est « comment faire vouloir au client » (pré-vente) ; ce répertoire est « **après signature, comment exécuter tout le mandat comme un business : complet, propre, répétable** ». Le problème : **une firme de conseil avec seulement la méthodologie sans framework opérationnel sera écrasée par le scope creep, aura des cassures de handover, incidents de sécurité, ne pourra pas scaler.**

Qui utilise : chefs de projet, consultants, Sales (Closer), Technical Lead, Owner côté client.

## 2. Position dans la Méthodologie

| Axe | Mapping |
| --- | --- |
| Flux de service 3 phases | **Deliver** + cadre opérationnel qui emballe les trois phases dans « business » |
| Structure de conseil 8 étapes | Correspond à la **livraison et acceptation** des 8 étapes ; engagement lifecycle est la « coque commerciale » des 8 étapes |
| **Modèle de contrat 3 phases (boucle fermée de conseil)** | **Phase A Diagnostic 2W → Phase B Stratégie 4W → Phase C Implémentation 24M + revue radar trimestrielle** — la phase Delivery du cycle EST la boucle Phase A→B→C |
| Maturité L1-L5 | Acceptation du package de livraison couvre les livrables de tous les niveaux L1-L5 |
| Engagement Lifecycle | **Ce répertoire EST le corps du cycle d'engagement (Sales → Delivery → Support)** |

> 🔁 **Cycle d'engagement ↔ boucle fermée de conseil** : la « phase Delivery » de ce répertoire **n'est pas un marathon 6 semaines** mais la **boucle fermée** décrite dans [`../03_Consulting_Report/README.md`](../03_Consulting_Report/README.md) §4 et [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 : rapport intermédiaire Phase A signé → Gate A → rapport complet Phase B → Gate B → implémentation 24 mois Phase C + **revue radar trimestrielle** (mécanisme de falsification de la gestion scientifique). La phase Support correspond à Retainer / Maintenance après Phase C.

## 3. Objectifs & Bénéfices

| Objectif | Bénéfice |
| --- | --- |
| Package de livraison et critères d'acceptation clairs | Client et consultant d'accord sur « est-ce fini », pas de dispute |
| Cycle d'engagement complet | De lead à closeout a SOP, pas artisanat personnel |
| SOP de rôles | Scalable (pas une personne fait tout), handover sans cassure |
| Modèles de documents commerciaux | SOW/contrat/facture/change order prêts, pas réécrits à chaque fois |
| Checklists opérationnelles | pre-project/security/QA/handover/offboarding rien oublié |
| Framework pricing et risque | Scope creep ne mange pas la marge, savoir quand dire « non » |

**Si ce répertoire est sauté** : méthodologie forte mais business ne scale pas — scope creep, travail pour rien, cassure handover, incident sécurité, dépendance personne clé, créances irrécouvrables.

## 4. Workflow & Logique

```text
Cycle d'engagement (ENGAGEMENT_LIFECYCLE) :
  Sales (Lead → Discovery → Proposal → Contract)
     → Utiliser BUSINESS_DOCUMENT_TEMPLATES (proposition, SOW)
     → Utiliser PRICING_AND_RISK (pricing, risk register)
  Delivery (Kickoff → Build → Test → Security → Handover)
     → Utiliser DELIVERY_CHECKLISTS (pre-project / security / QA / handover)
     → Utiliser DELIVERY_PACKAGE_AND_ACCEPTANCE (acceptation package)
     → Utiliser DELIVERY_ROLE_SOPS (qui responsable de quelle phase)
  Support (Retainer → Maintenance → Offboarding)
     → Utiliser DELIVERY_CHECKLISTS (offboarding)
Continu : 7 Pillars comme principe de base
```

| Étape | Qui | Quand | Input | Output |
| --- | --- | --- | --- | --- |
| Faire tourner le cycle | PM | Mandat complet | `ENGAGEMENT_LIFECYCLE` | Avancement des phases |
| Produire documents commerciaux | Closer / PM | Sales / lors de changement | `BUSINESS_DOCUMENT_TEMPLATES` | Proposition / SOW / Change Order |
| Pricing et évaluation risque | Closer / PM | Proposal / Kickoff | `PRICING_AND_RISK` | Devis + Risk Register |
| Faire tourner checklists | PM / Technical Lead | Chaque phase livraison | `DELIVERY_CHECKLISTS` | Chaque phase passée |
| Acceptation livraison | PM + client | Handover | `DELIVERY_PACKAGE_AND_ACCEPTANCE` | Signature client |
| Division des rôles | Toute l'équipe | Continu | `DELIVERY_ROLE_SOPS` | Responsabilité claire et handover |

> Logique : `ENGAGEMENT_LIFECYCLE` est le tronc (lifecycle) ; les 5 autres sont outils pour les phases — modèles, pricing & risque, checklists, SOP rôles, acceptation. **7 Pillars** (client possède, client paie, sécurité d'abord, tester à fond, documentation complète, handover propre, scope clair) traversent tout.

## 5. Descriptions de Fichiers

### Couche Acceptation de Livraison

| Fichier | Usage |
| --- | --- |
| `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` | Liste de livraison et tableau d'acceptation item-by-item pour diagnostic maturité IA, cours L1-L5, L4 Hermes Agent, rapport de diagnostic de conseil 8 étapes. |

### Couche Opérations d'Engagement (adapté de Mirza Iqbal / next8n.com Workflow Automation Delivery Framework, MIT, generalized pour contexte L1-L5 transformation IA ; citation voir `../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`)

| Fichier | Usage |
| --- | --- |
| `ENGAGEMENT_LIFECYCLE.md` | Cycle 3 phases (Sales → Delivery → Support), sous-phases et outputs de chaque phase, 7 Pillars, cycle × 8 étapes cross-référence, checklist pré-engagement. |
| `DELIVERY_ROLE_SOPS.md` | 7 SOP de rôles livraison (Lead Gen / Sales Rep / Closer / PM / Technical Lead / Developer / Client), chaque rôle : responsabilité, livrables clés, points handover, partenaires collaboration, phase cycle, plus matrice rôle × cycle et règle d'or handover. |
| `BUSINESS_DOCUMENT_TEMPLATES.md` | 8 modèles documents commerciaux : proposition, SOW, MSA outline, change order, facture, document handover, contrat maintenance, e-mails critiques. **Avec disclaimer légal — squelettes ne sont pas documents juridiques, doivent être revus par juriste.** |
| `DELIVERY_CHECKLISTS.md` | 5 checklists opérationnelles : pre-project, security, QA, handover, offboarding ; différence avec Stage Gate méthodologique. |
| `PRICING_AND_RISK.md` | Deux principes de séparation du pricing, 4 modèles de pricing, ligne produits par paliers, risques courants de mandat et mitigation, quand dire « non », processus de gestion d'incident. |

### `*_EN.md`

Versions anglaises sibling de certains fichiers.

## 6. Mapping vers Autres Répertoires

| Répertoire | Relation avec ce répertoire | Flux de données |
| --- | --- | --- |
| `01_Assessment` | Diagnostic correspond à phase Sales du cycle | `01` ↔ `06` Sales |
| `02_Course_Design` | Output en classe entre dans acceptation package | `02` output → `06` acceptation |
| `03_Consulting_Report` | Rapport de conseil est livraison centrale du package | `03` rapport → `06` acceptation |
| `05_Sales` | Prix/packages du deck correspondent au cycle et pricing | `05` deck ↔ `06` pricing |
| `00_Overview` | Cycle d'engagement est le cadre qui transforme la story en business | `00` story → `06` opérations |
| `90_References` | Citation tierce pour couche opérations (framework Mirza Iqbal) | `90` citation → `06` |

## 7. Scénarios d'Usage Communs

- **Nouveau mandat reçu** : PM utilise la « checklist pré-engagement » de `ENGAGEMENT_LIFECYCLE.md` pour vérifier la préparation, `DELIVERY_ROLE_SOPS.md` pour assigner les rôles.
- **Sur le point de signer** : Closer utilise le modèle SOW de `BUSINESS_DOCUMENT_TEMPLATES.md` (in/out of scope clairement écrits), `PRICING_AND_RISK.md` pour le pricing.
- **Chaque phase de livraison** : faire tourner les checklists pre-project / security / QA / handover contre `DELIVERY_CHECKLISTS.md`.
- **Livraison au client** : utiliser `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` pour acceptation item-by-item + document handover de `BUSINESS_DOCUMENT_TEMPLATES.md`.
- **Client ajoute sans cesse des exigences** : utiliser mitigation scope creep de `PRICING_AND_RISK.md` + change order de `BUSINESS_DOCUMENT_TEMPLATES.md`.
- **Closeout** : faire tourner checklist offboarding de `DELIVERY_CHECKLISTS.md`.

---

## ⭐ Cross-Topic Quick References : 5 Thèmes Centraux, où Trouver

Toute la méthodologie a 5 artères principales traversant tous les répertoires. Comment ce répertoire se connecte à chacune :

| Cross-Topic | Lieu principal | Comment ce répertoire se connecte |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lecture trois moteurs** | Root [`README_FR.md`](../README_FR.md) §🌟 ｜ [`AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | Pendant le mandat les trois moteurs peuvent être mobilisés en division du travail : Antigravity pour réunions client / Codex pour audit SOW et brouillons de rapport / Claude Code pour simulation Phase B et review multi-perspectives |
| 🎓 **Fondement académique (7 piliers)** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | « Sécurité d'abord / HITL » des 7 Pillars correspond à Sociotechnical Systems & Trust (Bostrom / Dietvorst / Glikson) ; scope creep / échecs de saut de niveau correspondent aux failure patterns Real Options + Absorptive Capacity |
| 📚 **Éducation L1-L5** | [`../02_Course_Design/`](../02_Course_Design/) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md) | Acceptation package couvre livrables vérifiables de tous L1-L5 ; output en cours entre dans [`DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](DELIVERY_PACKAGE_AND_ACCEPTANCE.md) pour acceptation item-by-item |
| 🔁 **Conseil / 8 étapes + Closed-Loop Phase A→B→C** | [`EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Ce répertoire EST la « coque commerciale » de la boucle fermée de conseil** — cycle Sales→Delivery→Support correspond à Phase A→B→C + revue radar trimestrielle |
| 📖 **Références / remerciements** | [`../90_References/`](../90_References/) §2 remerciements | Couche opérations cite Mirza Iqbal / next8n.com Workflow Delivery Framework (MIT), détails dans [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) |
