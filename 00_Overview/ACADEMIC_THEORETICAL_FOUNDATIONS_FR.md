# Fondations théoriques académiques : Les sept piliers théoriques de la méthodologie Tiger AI

> 🌐 Langue : [繁體中文](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [English](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) ｜ [Deutsch](ACADEMIC_THEORETICAL_FOUNDATIONS_DE.md) ｜ Français ｜ [Español](ACADEMIC_THEORETICAL_FOUNDATIONS_ES.md) ｜ [日本語](ACADEMIC_THEORETICAL_FOUNDATIONS_JA.md) ｜ [한국어](ACADEMIC_THEORETICAL_FOUNDATIONS_KR.md)
>
> Apache License 2.0 · Auteur : Morris Lu · Tiger AI

Dernière mise à jour : 2026-05-16

---

> **Objectif** : Consolider les fondations théoriques académiques de la méthodologie Tiger AI éparpillées entre fichiers dans **un document autoritaire**. Lorsque tout chercheur / régulateur / consultant sérieux demande « quelle est la base théorique », ce document est la réponse.
>
> **Affirmation core** : La méthodologie Tiger AI n'est pas simplement une pratique de consulting mais une **intégration ingénierée de sept théories**.

---

## 1. Vue d'ensemble carte théorique

| Théorie | Fondateur / Référence classique | Problème core résolu | Mapping Tiger AI |
| --- | --- | --- | --- |
| **Capability Maturity & BPM Maturity** | Paulk et al. (1993) CMMI ; Rosemann & de Bruin (2005) | Comment scorer structurellement la capacité organisationnelle ? | L1-L5 + scoring Stage 2 |
| **Absorptive Capacity** | Cohen & Levinthal (1990) | Pourquoi les organisations diffèrent-elles tant dans l'**absorption** de nouvelle capacité ? | Tool 6.3 Organizational Absorption Assessment |
| **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | Quelles tâches conviennent / ne conviennent pas à l'IA ? | Stage 7 To-Be Design (pas tout département devrait atteindre L5) |
| **Dynamic Capabilities** | Teece et al. (1997) ; Teece (2007) | Comment une organisation **s'adapte-t-elle rapidement au changement externe** ? | Stage 7 + Stage 8 (de l'automatisation statique à la capacité dynamique) |
| **Sociotechnical Systems & Trust in AI** | Bostrom & Heinen (1977) ; Dietvorst et al. (2015) ; Glikson & Woolley (2020) | Pourquoi la collaboration humain-IA est-elle difficile ? Algorithm aversion / complacency | Stage 8 Change Management + HITL |
| **Real Options Theory** | Dixit & Pindyck (1994) ; McGrath (1997) | Comment valuer un investissement stratégique IA hautement incertain ? | Stage 8 §13 Value Tracking + ROI |
| **AI-Native Living Book / Executable Knowledge Artifact** | Knuth (1984) ; Anderson et al. (1995) ; cet auteur (2026) | La méthodologie elle-même peut-elle être exécutable par IA ? | AGENTS.md + AI_NATIVE_LIVING_BOOK |

---

## 2. Capability Maturity & BPM Maturity

### 2.1 Résumé de théorie

- **CMMI** : Paulk et al. (1993) au SEI ont défini capacité organisationnelle 5-level (Initial / Repeatable / Defined / Managed / Optimizing)
- **BPM Maturity Model** : Rosemann & de Bruin (2005, QUT) ont étendu maturity à Business Process Management, ajoutant 6 enablers : Process Awareness / Alignment / Methods / IT / People / Culture

### 2.2 Contribution à Tiger AI

- **L1-L5 deux axes** héritent de la logique « Process Awareness → Optimization » de BPM Maturity, ajoutant la double structure essentielle de l'ère GenAI « **axe scale + axe AI Autonomy** »
- **Échelle 0-4 + ancres comportementales BARS** dérivent de cette école
- **Stage Gate Criteria** = « Process Areas » de CMMI + acceptance de phase

### 2.3 Fichiers mappés

- [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §3.0 histoire deux-axes
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) définitions L1-L5
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) ancres comportementales

---

## 3. Absorptive Capacity

### 3.1 Résumé de théorie

- **Cohen & Levinthal (1990)** dans *Administrative Science Quarterly* : la « **capacité d'une organisation à identifier, assimiler et appliquer la connaissance externe** » détermine sa capacité d'innovation
- Éléments core : **Prior Knowledge + Internal Knowledge Flow**
- Zahra & George (2002) divisent davantage en 4 dimensions : Acquisition / Assimilation / Transformation / Exploitation

### 3.2 Contribution à Tiger AI

- Explique pourquoi **la même opportunité IA yield des résultats radicalement différents** entre entreprises — la différence est l'absorptive capacity
- Tool 6.3 Organizational Absorption Assessment mappe directement sur cette théorie
- Renforce « **pourquoi les niveaux ne peuvent pas être sautés** » : sauter L1-L3 → absorptive capacity insuffisante → L4-L5 échouera (voir [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) §2)

### 3.3 Amélioration spécifique à Tool 6.3

Original Tool 6.3 6 dimensions (Budget / Champion / IT FTE / Governance / Literacy / Change capacity) **ajoutent 2 nouvelles dimensions** :

| Nouvelle dimension | Questions d'assessment | Score |
| --- | --- | --- |
| **Prior Knowledge** | L'entreprise a-t-elle : (a) expérience passée BPM / Lean / Six Sigma ? (b) tentatives passées IA / ML / RPA ? (c) capacité dev logicielle interne ? | 0-4 |
| **Internal Knowledge Flow** | Entre départements : (a) reviews inter-dept routinières ? (b) plateforme de documents partagés ? (c) système de mentor / instructeur interne ? | 0-4 |

→ Entreprises High Prior Knowledge + High Knowledge Flow peuvent gérer Phase 1/2/3 plus agressives ; inversement, doivent étendre timelines.

### 3.4 Références

- Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128-152.
- Zahra, S. A., & George, G. (2002). Absorptive capacity: A review, reconceptualization, and extension. *Academy of Management Review*, 27(2), 185-203.

---

## 4. Task-Technology Fit (TTF)

### 4.1 Résumé de théorie

- **Goodhue & Thompson (1995)** dans *MIS Quarterly* : le degré auquel la technologie améliore la performance dépend du fit **« demande de tâche ↔ capacité tech »**
- Classification de tâche : **Routine (répétitive, prévisible) vs Non-routine (judgment-heavy, créative)**

### 4.2 Contribution à Tiger AI

**Pas tout département devrait atteindre L5**. Déterminer le point final L-level approprié de chaque dept par caractéristiques de tâche :

| Type de tâche | Point final approprié | Rationale |
| --- | --- | --- |
| Highly Routine (CS FAQ, classification de facture) | L3-L4 | Fit IA élevé ; coût HITL bas |
| Medium Routine + jugement partiel (propositions de vente, anomalies de fin de mois) | L2-L3 + HITL | IA brouillonne + humain confirme ; balance efficacité et risque |
| Highly Non-routine (évaluation M&A, décisions stratégiques) | L1-L2 (assistant personnel) | IA assiste, humains mènent ; pousser L4-L5 nuit à la qualité de jugement |
| Highly compliance-sensitive (legal, diagnostic médical) | L2-L3 + strong HITL | Risque régulatoire trop élevé ; L4-L5 inapproprié |

### 4.3 Fichiers / Tools mappés

- Stage 7 Tool 7.2 Human-AI Collaboration → matrice TTF décide d'involvement IA par processus
- Ajouter **TTF Assessment Worksheet** à Tool 6.3 → scorer TTF par dept, déterminer L-level Ideal

### 4.4 Références

- Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. *MIS Quarterly*, 19(2), 213-236.
- Zigurs, I., & Buckland, B. K. (1998). A theory of task/technology fit and group support systems effectiveness. *MIS Quarterly*, 22(3), 313-334.

---

## 5. Dynamic Capabilities

### 5.1 Résumé de théorie

- **Teece, Pisano & Shuen (1997)** dans *Strategic Management Journal* : l'avantage compétitif provient d'« **intégrer, construire, reconfigurer les ressources internes et externes** »
- **Teece (2007)** décompose en trois micro-foundations :
  1. **Sensing** : identifier opportunités et menaces
  2. **Seizing** : décision et allocation de ressources
  3. **Transforming** : reconfiguration organisationnelle pour exploiter opportunités

### 5.2 Contribution à Tiger AI

**De l'automatisation statique → capacité adaptive dynamique**. Tiger AI ne fait pas que IA-iser processus APQC existants mais **construit aux clients la nouvelle capacité de s'adapter continuellement au changement externe** :

| Dynamic Capability | Mapping Tiger AI |
| --- | --- |
| **Sensing** | L3 Workflow + L4 Agent monitorent continuellement signaux marché / client / processus |
| **Seizing** | Décomposition Phase 1/2/3 = conversion de signaux sensés en décisions d'investissement concrètes |
| **Transforming** | L5 Multi-Agent Organization + radar quarterly Gate C = reconfiguration org continue |

### 5.3 Amélioration spécifique à Stage 7

Ajouter **Dynamic Capability Worksheet** à Stage 7 To-Be Design :

```
Par Teece (2007) trois micro-foundations, chaque To-Be design doit répondre :

1. Sensing : Quel signal externe ce design IA aide-t-il l'entreprise à "sense" ?
   Ex. complaint Agent monitore tendances satisfaction client
2. Seizing : Avec quelle rapidité l'entreprise peut-elle "seize" quand signaux apparaissent ?
   Ex. Quick Win complaint response 5d → 1d compresse fenêtre de perte client
3. Transforming : Comment ce IA permet-il "self-reconfiguration" organisationnelle ?
   Ex. L5 ClawTeam inter-dept = org ne dépend plus de personnel senior spécifique
```

→ Un To-Be qui ne répond pas à ces 3 est juste « automatiser le statut quo », pas vraie transformation.

### 5.4 Références

- Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal*, 18(7), 509-533.
- Teece, D. J. (2007). Explicating dynamic capabilities. *Strategic Management Journal*, 28(13), 1319-1350.

---

## 6. Sociotechnical Systems & Trust in AI

### 6.1 Résumé de théorie

- **Sociotechnical Systems Theory** (Bostrom & Heinen, 1977) : performance organisationnelle = output joint de **système social + système technique** ; ne peut pas optimiser l'un seul
- **Algorithm Aversion** : Dietvorst, Simmons & Massey (2015) dans *JEP* : les gens **préfèrent jugement humain pire aux algorithmes après avoir vu l'algorithme errer**, même en sachant que l'algorithme est plus précis
- **Automation Complacency** : Parasuraman & Manzey (2010) : sur-confiance dans l'automation cause perte de vigilance, menant à plus grands incidents
- **Trust in AI** : Glikson & Woolley (2020) intègrent trust cognitif + émotionnel

### 6.2 Contribution à Tiger AI

La vraie challenge de la collaboration humain-IA n'est pas seulement « peur de remplacement », mais aussi :

1. **Algorithm Aversion** : après première erreur IA, personnel collectivement la rejette → commun après lancement L3-L4
2. **Automation Complacency** : personnel arrête de réviser → HITL échoue → incidents plus grands
3. **Ambiguïté d'accountability** : qui est responsable quand IA erre ? Personnel craint blâme → gap de sécurité psychologique
4. **Reshape d'identité professionnelle** : de « Doer » à « Reviewer » → charge cognitive et sens d'accomplissement shifte

### 6.3 Amélioration à Stage 8 Change Management

Ajouter 2 nouveaux types de resistance à Tool 8.2 :

| Type de resistance | Signal typique | Handling |
| --- | --- | --- |
| **Algorithm Aversion** | Rejet collectif après une erreur IA | Transparence sur taux d'erreur (humain vs IA) + trust-building graduel (commencer par scénarios low-risk) |
| **Automation Complacency** | Personnel approuve sans réviser | Random sampling obligatoire dans Reviewer Workflow + re-formation après erreurs détectées |

### 6.4 Amélioration à HITL Design (Tool 7.2)

Ajouter **colonnes sécurité psychologique et accountability** :

| Processus | HITL Node | **Accountability Statement** | **Sécurité psychologique** |
| --- | --- | --- | --- |
| CS reply | 100% révision humaine avant envoi | Responsabilité IA draft = AI Champion ; responsabilité reply finale = personnel CS | Personnel a droit de « rejeter sans révision si IA est faux » sans blâme |
| Process root cause | 100% révision humaine avant action | Responsabilité hypothèse IA = développeur Agent ; responsabilité action = manager de processus | Manager a SOP formel pour « rejeter suggestion IA » |

### 6.5 Références

- Bostrom, R. P., & Heinen, J. S. (1977). MIS problems and failures: A socio-technical perspective. *MIS Quarterly*, 1(3), 17-32.
- Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion. *JEP: General*, 144(1), 114-126.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3), 381-410.
- Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence. *Academy of Management Annals*, 14(2), 627-660.
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *ASQ*, 44(2), 350-383.

---

## 7. Real Options Theory

### 7.1 Résumé de théorie

- **Dixit & Pindyck (1994)** dans *Investment Under Uncertainty* : valeur d'investissement hautement incertain = valeur d'exécution immédiate + valeur de « **future optionality** »
- **McGrath (1997)** appliqué à la stratégie : « **l'investissement d'aujourd'hui préserve le droit d'expandre dans le futur** »
- Contre la sous-estimation NPV sous incertitude : NPV assume certitude, mais flexibilité manageriale a valeur élevée sous incertitude

### 7.2 Contribution à Tiger AI

L'investissement IA hautement incertain L4-L5 est **nécessairement sous-estimé par NPV / IRR traditionnel** (parce que cash flows 18-24 mois sont incertains). Real Options fournit un meilleur framing :

| Investissement | Vue NPV (sous-estime) | Vue Real Options (justifiée) |
| --- | --- | --- |
| Phase 1 Foundation (NT$ 2,8M) | Cash flow unclear → NPV ≈ 0 | Acheter l'« **option d'expandre rapidement L4-L5 dans futur à coût plus bas** », vaut bien plus que NT$ 2,8M |
| L1 Chat AI pan-entreprise | ROI court-terme unclear | Literacy IA employés = **actif foundational pour toutes futures applications IA** |
| L2 Skill Library | ROI invisible | Codification de connaissance = option de l'entreprise de « **brancher plusieurs applications IA simultanément** » dans futur |
| L4 Hermes Agent Pilot | Un Agent vaut-il la peine ? | Pilot = apprendre L4 = option vers L5 ClawTeam |

### 7.3 Real Options Valuation (Black-Scholes simplifié)

Pour investissements L4-L5, estimer via :

```
Option Value = max(0, future_payoff - exercise_cost)

Où :
  future_payoff = revenu d'exercer option (ex. expandre à L5)
  exercise_cost = coût en exerçant (ex. Phase 3 investissement)
  volatility (σ) = incertitude marché / tech
  time-to-expiration = fenêtre d'opportunity
```

⚠️ Pas besoin de Black-Scholes exact ; **argument niveau narratif suffit pour convaincre CFO** de justifier investissement « ROI court-terme invisible mais long-terme précieux ».

### 7.4 Amélioration à Stage 8 §13 Value Tracking

Original 5 dimensions (Time / Quality / Scale / Risk / Assets), **ajouter 6e dimension** :

| Dimension | Contenu |
| --- | --- |
| **Strategic Options** | Quel « **future exercise right** » cet investissement a-t-il préservé ? Ex. L1 foundation → peut expandre L4 rapidement dans futur ; L2 Skill Library → peut brancher tout futur Agent ; L3 Workflow → peut intégrer tout nouveau système |

### 7.5 Références

- Dixit, A. K., & Pindyck, R. S. (1994). *Investment Under Uncertainty*. Princeton University Press.
- McGrath, R. G. (1997). A real options logic for initiating technology positioning investments. *Academy of Management Review*, 22(4), 974-996.
- Trigeorgis, L. (1996). *Real Options*. MIT Press.

---

## 8. AI-Native Living Book comme Executable Knowledge Artifact

### 8.1 Résumé de théorie

- **Literate Programming** : Knuth (1984) a argumenté que code et docs devraient s'intégrer en un seul document « lisible-humain + exécutable-machine »
- **Intelligent Tutoring Systems (ITS)** : Anderson et al. (1995) ont designé IA comme systèmes de tutoring personnalisés
- **Open Educational Resources (OER) + IA** : tendance contemporaine combinant matériaux open avec IA comme systèmes de connaissance interactifs

### 8.2 Contribution à Tiger AI

Cette méthodologie elle-même est un **cas pratique** de cette théorie :

- repo + AGENTS.md = **executable knowledge artifact**
- AI co-reading tutor = **adaptive ITS** appliqué à l'éducation professionnelle adulte
- Client conversant avec méthodologie = OER customisé

Voir [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) pour discussion complète.

### 8.3 Références

- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society*. Harvard University Press.

---

## 9. Comment les 7 théories coopèrent : Modèle intégré de Tiger AI

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   [Capability Maturity]  ────►  scoring structuré L1-L5           │
│         │                                                        │
│         ▼                                                        │
│   [Absorptive Capacity] ────►   pourquoi entreprises diffèrent  │
│         │                       dans absorption                  │
│         ▼                                                        │
│   [Task-Technology Fit] ────►  quelles tâches à quel L ?         │
│         │                                                        │
│         ▼                                                        │
│   [Dynamic Capabilities]────►  L3-L5 pas juste automatisation    │
│         │                       mais construction de capacité    │
│         │                       adaptive                         │
│         ▼                                                        │
│   [Sociotechnical Trust]────►  vraies challenges de              │
│         │                       collaboration humain-IA          │
│         │                       (trust, accountability)          │
│         ▼                                                        │
│   [Real Options]        ────►  justifier investissement          │
│         │                       stratégique L4-L5 sous           │
│         │                       incertitude                      │
│         ▼                                                        │
│   [AI-Native Living Book]──►   méthodologie elle-même exécutable │
│                                                                  │
└────────────────────────────────────────────────────────────────┘

7 théories ne sont pas des couches isolées mais une chaîne complète :
scoring → absorption → matching → adaptation → trust → investment → execution
```

---

## 10. Recommandations de submission académique

Par ces 7 théories, plusieurs papers peuvent être dérivés :

| Titre de paper (suggéré) | Théorie principale | Journal cible |
| --- | --- | --- |
| A GenAI Adoption Maturity Model: Extending BPM Maturity for the LLM Era | Capability Maturity + AI-Native | MIS Quarterly / Information Systems Research |
| Absorptive Capacity in Enterprise AI Adoption: Empirical Evidence from 7 Industries | Absorptive Capacity | Strategic Management Journal |
| Task-Technology Fit Beyond Routine Work: When Should Departments Adopt L4-L5 Agents? | TTF | Information & Management |
| From Automation to Dynamic Capability: How AI Reshapes Organizational Sensing | Dynamic Capabilities | Strategic Management Journal |
| Algorithm Aversion in Workflow Automation: A Mixed-Methods Study | Sociotechnical / Trust | Organization Science |
| Valuing AI Foundation Investments as Real Options | Real Options | SMJ / California Management Review |
| AI-Native Living Books: Methodology as Executable Knowledge Artifact | AI-Native LB | Communications of the ACM |

---

## 11. Bibliographie complète

Voir §3-8 pour références par théorie et la bibliographie complète dans la version chinoise.

---

Licence & Citation

Ce document est sous Apache License 2.0 ; peut être utilisé, modifié, commercialisé, à condition de préserver l'attribution [`../NOTICE`](../NOTICE).
