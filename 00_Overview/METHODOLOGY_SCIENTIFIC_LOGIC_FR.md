# Logique scientifique de la méthodologie : Pourquoi ce rapport résiste au débat

> 🌐 Langue : [繁體中文](METHODOLOGY_SCIENTIFIC_LOGIC.md) ｜ [English](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) ｜ [Deutsch](METHODOLOGY_SCIENTIFIC_LOGIC_DE.md) ｜ Français ｜ [Español](METHODOLOGY_SCIENTIFIC_LOGIC_ES.md) ｜ [日本語](METHODOLOGY_SCIENTIFIC_LOGIC_JA.md) ｜ [한국어](METHODOLOGY_SCIENTIFIC_LOGIC_KR.md)
>
> Apache License 2.0 · Auteur : Morris Lu · Tiger AI

Dernière mise à jour : 2026-05-15

---

> **Ce que ce document répond** : Pourquoi cette méthodologie est-elle conçue ainsi ? Pourquoi 8 étapes, pas 5 ou 12 ? Pourquoi les données circulent-elles ainsi ? Pourquoi les cases doivent-elles être de niveau Benchmark ? **Ultimement** : quand les clients / conseils / régulateurs la défient, sur quelle base ce rapport de conseil tient-il ?
>
> **Affirmation centrale** : Cette méthodologie n'est pas une collection d'expérience de conseil mais une **logique de management scientifique en boucle fermée** — chaque étape satisfait les cinq conditions de la méthode scientifique : observable, quantifiable, reproductible, falsifiable, auditable.

---

## 1. Pourquoi les rapports de conseil ont besoin de « pouvoir argumentatif scientifique »

Scénarios d'échec communs :

| Scénario | Défi client | Réponse typique du consultant | Pourquoi cela échoue |
| --- | --- | --- | --- |
| Interrogation du conseil | « Comment savez-vous que nous sommes au L2 ? » | « Basé sur nos entretiens... » | Subjectif ; non vérifiable |
| Audit interne | « Pourquoi le service client avant les ventes ? » | « D'après notre expérience... » | L'expérience est non auditable |
| Vérification réglementaire | « Qui est responsable si l'IA échoue ? » | « Nous avons des politiques... » | Les politiques sans chaîne d'audit ne comptent pas |
| Changement de consultants | « La firme précédente disait L3 ; vous dites L2 — qui a raison ? » | « Méthodes différentes » | Non reproductible = pas scientifique |

**Objectif de design de Tiger AI** : chaque question de ce type a une **nombre vérifiable + évidence auditable + procédure reproductible** comme réponse.

---

## 2. Cinq conditions de la méthode scientifique vs. cette méthodologie

| Condition scientifique | Définition | Comment la méthodologie la satisfait |
| --- | --- | --- |
| **1. Observable** | Les conclusions reposent sur une évidence que d'autres peuvent voir | Enregistrements Stage 1 + inventaire système + As-Is Swimlanes ; chaque item horodaté avec source |
| **2. Quantifiable** | Conclusions réductibles à des nombres, pas des adjectifs | Scoring radar Stage 2 0-4 ; scoring Impact×Effort Stage 4 ; nombres d'impact-surface 80/20 Stage 5 ; value tracking Stage 8 5 dimensions |
| **3. Reproductible** | Différents consultants utilisant la même méthode obtiennent des conclusions similaires | Trois Reference Models (APQC / SCOR / Tiger AI L1-L5) sont des standards publics ; banque d'entretien 40 questions ; discipline MECE |
| **4. Falsifiable** | Les conclusions ont des conditions de réfutation explicites | Stage 6 Stage Gate Criteria listent explicitement pass/fail ; les checklists ont des conditions observables ; cible ratée = hypothèse réfutée |
| **5. Auditable** | Le processus peut être vérifié indépendamment par des tiers | Stage 8 Audit Log (appels LLM, changements de permissions, déploiements Skill, sign-offs Reviewer chaîne complète), rétention définie |

> **Ces cinq conditions ne sont pas des décorations**. Toute conclusion de consultant qui ne peut répondre à ces cinq n'est pas du management scientifique — seulement du partage d'expérience.

---

## 3. Pourquoi exactement 8 étapes (pas 5, pas 12)

Raisonnement en arrière depuis la méthode scientifique : un rapport de transformation IA défendable **doit traverser 5 actions de raisonnement**, avec des dépendances de données strictes entre elles :

| Action de raisonnement | Mappe vers Stage | Sauter cause |
| --- | --- | --- |
| **A. Observer l'état actuel** | Stage 1 As-Is | Pas de baseline objective → tout ce qui suit est devinette |
| **B. Appliquer des coordonnées internationales** | Stage 2 Reference Model | Pas de coordonnées externes → « nous ne sommes pas assez bons » est opinion de consultant |
| **C. Le client étend sa propre Ideal Practice** | Stage 3 Best Practice | Pas de cible signée par client → le client peut nier le gap |
| **D. Quantifier le gap** | Stage 4 Gap Analysis | Pas de gap structuré → ne peut prioriser |
| **E. Converger le problème central** | Stage 5 Problem Definition | Pas de 80/20 → « tout est important » = rien n'est fait |
| **F. Fixer des cibles absorbables** | Stage 6 Phased Goals | Pas de décomposition en phases → tentative one-shot de perfection = échec |
| **G. Concevoir un blueprint** | Stage 7 To-Be Design | Pas de diagramme To-Be → Roadmap ne landera pas sur org et systèmes |
| **H. Exécuter & gouverner** | Stage 8 Implementation | Pas de change mgmt + value tracking + Audit → le blueprint est papier peint |

**Pourquoi exactement 8** : chaque action de raisonnement est inséparable ; **sauter l'une laisse un défi sans réponse**.

- Sauter Stage 2 → « Quel est votre standard ? » sans réponse
- Sauter Stage 4 → « Pourquoi ceci avant cela ? » sans réponse
- Sauter Stage 6 → « Pourquoi 9 mois pas 3 ? » sans réponse
- Sauter Stage 8 → « Comment prouvez-vous l'amélioration ? » sans réponse

> 5 étapes est trop grossier (omet Reference Model, Phased Goals, Change Mgmt) ; 12 étapes est trop fin (sous-étapes redondantes). **8 est « la chaîne de raisonnement débattable complète minimale. »**

---

## 4. Pourquoi les données circulent ainsi (Raison scientifique pour chaque flèche)

```
Stage 1 ──────────► Stage 2 ──────────► Stage 3 ──────────► Stage 4
As-Is              Reference Model     Best Practice         Gap
réalité observée    coordonnées         Ideal du client       gap objectif
                    internationales     Practice (signée)
                                                              │
                                                              ▼
Stage 8 ◄────────── Stage 7 ◄────────── Stage 6 ◄────────── Stage 5
Implementation      To-Be Design       Phased Goals          Problem
landing + change    blueprint futur     étapes absorbables    convergence centrale
                                                              
        ↑                                                     ↓
        └─── Trimestriellement : revisiter Stage 2 radar (vérification en boucle fermée) ───┘
```

#### Pourquoi chaque flèche est causalement nécessaire

| Flèche | Pourquoi cette direction | Inverser cause |
| --- | --- | --- |
| **Stage 1 → 2** | Doit avoir « réalité » avant comparer contre « standard » | Inversé : cherry-pick l'évidence pour correspondre au standard |
| **Stage 2 → 3** | Doit confirmer « structure complète » avant discuter « Ideal du client » | Inversé : l'Ideal saute les gaps structurels |
| **Stage 3 → 4** | Doit avoir **Ideal Practice signée par client** avant calculer « Gap = (Ideal client − As-Is client) » | Sans signature client, gap = opinion de consultant, réfutable |
| **Stage 4 → 5** | Doit avoir « tous les gaps » avant convergence 80/20 vers « problème central » | Sans 4, définition de problème = devinette |
| **Stage 5 → 6** | Doit verrouiller « problème central » avant fixer « cibles » | Sans 5, cibles éparpillent |
| **Stage 6 → 7** | Doit avoir « cibles phasées » avant concevoir « blueprint » | Sans 6, blueprint tente one-shot |
| **Stage 7 → 8** | Doit avoir « blueprint » avant « exécution » | Sans 7, exécution aveugle |
| **Stage 8 ↑ Stage 2 (trimestriel)** | Après exécution, revisiter « radar standard plus rond ? » | Sans loopback, PoCs faits mais structure non vérifiée |

> **C'est le sens scientifique de « boucle fermée »** : pas « fait c'est bien » mais « les résultats peuvent être rétroactivement vérifiés / falsifiés. »

---

## 5. Pourquoi Reference Model est 4 couches (pas 3, pas 5)

Dérivé de l'axe « **abstraction × volatilité** » de la maturité (voir [`CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 2.7) :

| Abstraction | Volatilité | Couche | Pourquoi ne peut être fusionné ou omis |
| --- | --- | --- | --- |
| Le plus abstrait | Années | **L1 Governance** | Stratégie et politique ne peuvent mélanger avec processus (volatilité diffère 10×) |
| Abstrait | Trimestres-Années | **L2 Business** | Fonctions business ne peuvent mélanger avec services données |
| Moyen | Mois-Trimestres | **L3 Information** | Services données ne peuvent mélanger avec hardware/réseaux |
| Le plus concret | Semaines-Mois | **L4 Technical** | Hardware mélangé en couche Business verrouille choix tech |

**3 couches insuffisant** : omet généralement L3 Information → services données comprimés dans L2 ou L4 → perte de focus.
**5 couches excessif** : la couche supplémentaire est généralement une sous-couche de L2 ou L3 → viole MECE.

> **L'école Dragon1 insiste sur 4 couches** pour cette raison scientifique. Tiger AI Enterprise AI Reference Model la suit strictement.

---

## 6. Pourquoi les cases doivent être Benchmark-grade (pas narratifs)

La science requiert « **reproductibilité** » — le même case lu par différents consultants / clients devrait donner des « estimations de gap » similaires.

- **Case narratif** : « Société X a fait inspection qualité IA et a réussi » → non reproductible (chaque lecteur interprète différemment)
- **Case Benchmark-grade** : 9 champs obligatoires (industrie + échelle + L de départ + L de fin + durée + investissement + Wins + Failures + applicabilité) → **reproductible** (estimation gap/temps/budget de tout lecteur tombe dans plage similaire)

Voir Tool 3.5 Cases-as-Benchmarks.

> **C'est pourquoi tous les 7 cases Tiger AI suivent le même modèle 9 champs** — pas pour cohérence visuelle mais pour la condition scientifique de **reproductibilité**.

---

## 7. Checklist « pouvoir argumentatif scientifique » du rapport

Quand les clients / conseils / régulateurs posent les questions suivantes, cette méthodologie a des emplacements de réponse spécifiques :

| Défi | Emplacement de réponse | Évidence |
| --- | --- | --- |
| « Comment savez-vous que nous sommes au L2 ? » | §3 As-Is + §4 RM Mapping | Enregistrements d'entretien, inventaire système, radar RM 0-4 |
| « Pourquoi APQC / Tiger AI L1-L5 ? » | §4.1 + Tool 2.5 | Scorecard de qualification 10 conditions |
| « À quelle distance sommes-nous de notre idéal ? » | §5 + §6.1 | **Table de définition Ideal Practice signée par client** + Benchmark de case ; Gap = (votre Ideal signé − votre As-Is), les deux extrémités sont vos affirmations |
| « Pourquoi service client avant ventes ? » | §6.2 + §6.3 | Matrice Impact × Effort + Score de Priorisation |
| « Pourquoi le problème central est ‹ asset-isation de la connaissance › ? » | §7 | Nombres d'impact-surface 80/20 + chaîne 5 Whys |
| « Pourquoi 9 mois pas 3 ? » | §8 + Tool 6.3 | Décomposition phasée + Organizational Absorption (6 dimensions) + durée de case benchmark |
| « Que faire si le PoC échoue ? » | §13.2 | Risk Register + Triggers + Mitigation Owners |
| « Comment prouvez-vous l'amélioration ? » | §13.1 + revue radar trimestrielle | Value Tracking 5 dimensions + Stage 2 radar before/after |
| « Qui est responsable si l'IA échoue ? » | §12.1 + Tool 8.8 | RACI + AI Ethics Checklist + Audit Log chaîne complète |
| « Votre méthodologie peut-elle être reproduite ? » | Méthodologie entière | Apache 2.0 + GitHub + Tool 2.5 auto-qualification 9/10 |
| « Le dernier consultant disait L3, vous dites L2 — qui a raison ? » | §3 évidence de scoring | Échelle 0-4 publique + chaque score a évidence observable → **vérifiable par tiers** |
| « Pourquoi exactement 8 étapes ? » | Ce document §3 | Argument « chaîne de raisonnement débattable complète minimale » |

> **Le rapport devient un document débattable** : le client ne « fait pas confiance à l'autorité du consultant » mais « suit la chaîne d'évidence pour atteindre la même conclusion lui-même. » C'est du management scientifique.

---

## 8. Comparaison avec méthodologies de conseil mainstream

| Méthodologie | Force | Manquant (sous lentille de complétude scientifique) |
| --- | --- | --- |
| **McKinsey Issue Tree + Pyramid** | Raisonnement logique rigoureux, narrative forte | Pas de Reference Model (pas de coordonnées) ; pas de Phased Goals (pas de décomposition de phases) |
| **BCG Digital Maturity** | Maturité 5 étapes claire | Pas de Best Practice quantifié (excellence décrite par consultant) ; pas d'évaluation d'absorption organisationnelle |
| **Gartner AI Maturity** | Reconnu dans l'industrie | Pas de discipline d'entretien As-Is ; pas de benchmarks de case reproductibles |
| **MIT AI Capability** | Académiquement rigoureux | Manque outils de landing Implementation & Change |
| **Tiger AI (cette méthodologie)** | **Chaîne de raisonnement 8 étapes complète + Reference Model 4 couches + boucle fermée Cases-as-Benchmarks** | Nouveau (lancé 2025, cases s'accumulent) |

> **Ne dit pas que les autres méthodologies sont mauvaises** — dit qu'elles ont chacune des forces mais **boucles fermées incomplètes**. L'objectif de design de Tiger AI est de compléter cette boucle pour que le rapport ait **évidence pour chaque phrase de la couverture à la dernière page**.

---

## 9. Mérite de citation académique et réglementaire

Pourquoi cette méthodologie peut être validée, citée, améliorée par communautés académiques :

1. **Public** : Apache 2.0, repo GitHub, bilingue zh/en
2. **Auto-qualifiable** : Tool 2.5 auto-évaluation, 9 conditions sur 10 satisfaites
3. **Racines théoriques transparentes** : école Rosemann BPM Maturity (QUT) + CMMI + APQC + Dragon1 EA chacun cité
4. **Validé inter-industries** : Fabrication / Hôpital / Marketing / B2B / Financier / Gouvernement / Éducation — 7 cases industriels (valide portabilité)
5. **Falsifiable** : chaque Stage Gate Criteria a conditions de réfutation
6. **Critiquable** : ce document et Tool 2.5 notent tous deux explicitement « nouveau, reconnaissance s'accumule »

> **Le gold standard de la citation académique est « quelqu'un d'autre peut-il appliquer cette méthode à un problème différent et obtenir des conclusions similaires ? »** — la méthodologie Tiger AI répond Oui, parce que toutes les étapes, outils et critères de scoring sont publics.

---

## 10. Discipline opérationnelle pour les consultants

Quand vous écrivez ce rapport, chaque paragraphe doit répondre :

```
Quelle est l'évidence pour cette affirmation ?       ← Observable
Comment ce nombre a-t-il été calculé ?                ← Quantifiable
Un autre consultant obtiendrait-il le même ?          ← Reproductible
Si c'est faux, que verrais-je ?                       ← Falsifiable
Qui a signé pour ce processus ?                       ← Auditable
```

**Répondre à tous les 5 → ce paragraphe est du management scientifique**.
**Tout inrepondable → ce paragraphe est opinion personnelle ; ajouter évidence ou supprimer.**

---

## 11. Promesse aux clients

Cette méthodologie promet :

1. **Chaque conclusion a évidence numérotée** — Appendices A-G entièrement traçable
2. **Chaque nombre a formule de calcul** — pas de « basé sur jugement du consultant »
3. **Chaque recommandation a Stage Gate Criteria** — vous pouvez vérifier
4. **Chaque risque a Trigger + Owner + Mitigation** — vous pouvez gérer
5. **Chaque case est Benchmark-grade** — vous pouvez calculer le gap vous-même
6. **Chaque fin de phase revisite le radar Reference Model** — vous voyez la structure devenir réellement plus ronde

**Si un paragraphe se sent comme « autorité du consultant décide », pointez-le. Nous ajouterons évidence, réviserons la formule, ou supprimerons.**

---

## 12. Clôture : Cette méthodologie elle-même est un Reference Model

Une observation auto-référentielle finale :

- Cette méthodologie applique les 10 conditions de Tool 2.5 pour **auto-évaluer** : 9 sur 10 satisfaites (condition 6 « reconnaissance industrielle large » s'accumule encore)
- Cette méthodologie applique les 5 questions de dérivation de Tool 2.6 pour **auto-inventorier composants** : 8 étapes + 4 couches + 5 dimensions de tracking toutes présentes
- Cette méthodologie applique l'architecture 4 couches de Tool 2.7 pour **s'auto-organiser** : Governance (ce doc) + Business (Stages 1-8) + Information (toolkit + cases) + Technical (repo GitHub + AGENTS.md + CLAUDE.md)
- Cette méthodologie applique Cases-as-Benchmarks de Tool 3.5 pour **auto-prouver reproductibilité** : 7 cases industriels suivent tous le template 9 champs

> **C'est la boucle fermée du management scientifique** : une méthodologie n'analyse pas seulement les autres, mais **peut s'analyser elle-même avec ses propres outils** — en académie appelée « cohérence auto-référentielle », la marque de la théorie rigoureuse.

---

## Références

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- APQC (2024). *Process Classification Framework Version 7.3*.
- CMMI Institute (2018). *CMMI for Development V2.0*.
- Dragon1 (n.d.). *Enterprise Architecture Reference Model*. <https://www.dragon1.com/reference-models/enterprise-architecture-reference-model>
- Pyramid Principle: Minto, B. (2009). *The Pyramid Principle*.
- 80/20: Koch, R. (1997). *The 80/20 Principle*.
- 5 Whys: Ohno, T. (1988). *Toyota Production System*.
- Change Management: Kotter, J. (1996). *Leading Change*. Prosci ADKAR.

---

Licence & Citation

Ce document est sous Apache License 2.0 ; peut être utilisé, modifié, commercialisé, à condition que l'attribution [`../NOTICE`](../NOTICE) soit préservée.
