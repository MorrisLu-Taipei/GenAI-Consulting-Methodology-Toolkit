# L'histoire de Ming : une transformation IA de 24 mois dans une usine d'emballage

> 🌐 Langue : [繁體中文](CLIENT_JOURNEY_STORY.md) ｜ [English](CLIENT_JOURNEY_STORY_EN.md) ｜ [Deutsch](CLIENT_JOURNEY_STORY_DE.md) ｜ Français ｜ [Español](CLIENT_JOURNEY_STORY_ES.md) ｜ [日本語](CLIENT_JOURNEY_STORY_JA.md) ｜ [한국어](CLIENT_JOURNEY_STORY_KR.md)
>
> Une histoire de 20 minutes qui vous aide à comprendre la méthodologie en 8 stades. Pas de tableaux d'outils, pas d'acronymes, pas de jargon de consultant.

Apache License 2.0 · Auteur : Morris Lu · Tiger AI

Dernière mise à jour : 2026-05-15

---

> ⚠️ **Avis important d'intégrité académique**
>
> **« Ming » et « MingChang Packaging » sont des personnages fictifs et une entreprise fictive générés par IA, NON réels**. Cette histoire est du matériel pédagogique conçu pour aider les lecteurs non techniques à saisir rapidement la méthodologie en 8 stades. Tous les chiffres (taille de l'entreprise, KPI, budgets, calendriers, pourcentage de baisse de commandes du Client A) sont uniquement illustratifs.
>
> - Selon [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9, ceci est un **Cas pédagogique L0 simulé par IA** (sous L1)
> - De vrais cas longitudinaux n'existeront qu'après la fin de l'étude empirique 18-24 mois de [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md)
> - Cette histoire **ne doit PAS** être utilisée comme marketing externe « nous avons un vrai client qui a fait cela »

---

## Rencontrez le protagoniste

**Ming**, 55 ans, Président de MingChang Packaging.
Situé à Hsinchu, 700 employés, packaging et test de semi-conducteurs, 1,2 milliard de NT$ de chiffre d'affaires annuel.
Son père a fondé l'entreprise avec une seule wire bonder dans les années 1990 ; Ming a pris la relève en 2010 et l'a fait grandir en fournisseur de niveau intermédiaire pour le grand Client A.
Ming est fier de deux choses : sa fille est entrée à NTU, et son entreprise n'a pas perdu d'argent depuis 10 ans.

Mais début 2025, il a commencé à mal dormir.

---

## Chapitre 1 ── « Je pensais qu'on n'était pas si mal »

### Un e-mail

Janvier 2025. Le directeur des achats du Client A écrit : « La vitesse de réponse aux réclamations et de proposition de MingChang est trop en retard par rapport à nos autres fournisseurs. Les commandes du trimestre prochain seront réduites de 18 %. »

Ming le lit trois fois.

« 5 jours de réponse aux réclamations, c'est normal dans notre industrie », marmonne-t-il.

« Il y a des années, vous ne donniez que 7 jours. »

Cet après-midi-là, son secrétaire sonde ses pairs. **Les leaders du secteur répondent aux réclamations en 1 jour. Taux de défauts 40 % inférieurs à MingChang.**

Ming cherche en ligne. Trois concurrents directs ont déployé « inspection qualité IA » et « Agents IA de réclamations ».

« Peuvent-ils se le permettre ? Pouvons-nous ? » Il appelle Lin, le VP IT.

Lin hésite. « Président, on n'a même pas de compte ChatGPT d'entreprise. Les employés l'utilisent en privé, en brûlant 24 000 NT$/mois sur leurs cartes de crédit personnelles. Les données fuient probablement partout. »

Ming reste silencieux.

---

### Ce repo sur GitHub

Cette nuit-là, Ming est encore au bureau à 23 h.

Il essaie un compte ChatGPT et demande : « Comment un manufacturier de taille moyenne fait-il une transformation IA ? »

ChatGPT répond : « Vous pouvez consulter la méthodologie de conseil open-source Tiger AI : GenAI Consulting Methodology Toolkit. »

Ming clique sur GitHub et voit un « Executive Summary de 5 minutes ».

Après 5 minutes de lecture, il fait quelque chose qu'il n'a jamais fait — **ouvre un quiz en ligne de 10 questions et le remplit lui-même**.

### Les 10 questions

Chaque question lui donne trois scénarios à 0/2/4 à choisir :

- Vos employés utilisent-ils l'IA ? (0 = aucun / 2 = cadres personnellement / 4 = toute l'entreprise avec comptes corporate)
- Les patterns d'usage IA sont-ils sédimentés en templates réutilisables ? (0 = non / 2 = certains cadres sauvegardent les leurs / 4 = l'entreprise a une Skill Library)
- Les processus de l'entreprise ont-ils une automatisation inter-systèmes ? ...

Ming répond honnêtement.

Lorsqu'il soumet, un **graphique radar** apparaît.

Maximum 24 points. MingChang en marque 5.

**Deux des six axes sont à 0** : « sédimentation des connaissances » et « application d'Agents ».

Ming fixe longuement les deux creux vers l'intérieur.

« Je pensais qu'on n'était pas si mal. »

---

## Chapitre 2 ── Le consultant arrive (Phase A Diagnostic, 2 semaines)

Le lendemain matin, Ming demande à son secrétaire d'appeler Tiger AI.

Il signe **Phase A : Diagnostic, 2 semaines, 800K NT$**.

Ming demande : « Combien pour la transformation complète de 24 mois ? »
Consultant Chang dit : « Faites d'abord ces 2 semaines. Après le rapport, vous déciderez si vous signez la phase suivante. »

Ming hoche la tête. **C'est la première fois de sa vie qu'un consultant dit « regardons d'abord, puis décidons ».**

### Semaine 1 : ils posent des questions

Consultant Chang arrive jour 1 avec une **banque d'interview de 40 questions**.

Jour 1 : CEO, COO, CIO — 60 min chacun.
Jour 2 : chefs de département (QC, Sales, CS, IT, HR) — 90 min chacun.
Jour 3 : première ligne (3 ouvriers, 3 commerciaux, 3 CS) — 30 min chacun.

Ming demande : « Les consultants interviewent-ils toujours aussi longtemps ? Je pensais que vous donneriez juste des recommandations. »
Chang : « Nous n'avons même pas jugé si l'IA est nécessaire. Nous **écoutons d'abord**. »

Soir du jour 3, le contremaître Old Chen vient voir Ming :

« Patron, ce consultant m'a demandé quelles sont mes 5 tâches quotidiennes les plus répétitives. En parlant, j'ai réalisé — **3 d'entre elles, je les fais tous les jours depuis 25 ans, jamais écrites**. Quand je partirai à la retraite, qui le saura ? »

Quelque chose se déplace dans la poitrine de Ming.

### Fin de semaine 1 : ils dessinent des images

Jour 4 : Consultant et Lin listent **tous les outils IA jamais utilisés dans l'entreprise** (y compris privés). 7 outils. 42 000 NT$/mois au total — **tous sur cartes personnelles des employés**. Frontières de données floues.

Jour 5 : trois « **vraies cartes de processus** » (Swimlanes) : « RFQ-à-expédition », « Réponse aux réclamations », « Signalement d'anomalies de processus ». Chaque étape marquée de points de densité de douleur (0-3).

Ming regarde « RFQ-à-expédition » :

```
Client envoie RFQ      → 30% manqués   ●●● douleur
Sales vérifie ERP      → lent+erreurs  ●●● douleur
Sales rédige devis     → copie manuelle ●●  douleur
Manager revoit devis   → attente        ●●  douleur
......
Total : 4-7 jours ouvrables en moy.
Leader sectoriel : 4 heures
```

Ming : « Je pensais qu'on était rapide. Les leaders du secteur sont à 4 heures. »

### Semaine 2 : ils appliquent des standards internationaux

Semaine 2, Chang fait quelque chose que Ming n'a jamais vu des consultants faire.

Chang sort **trois frameworks de standards internationaux** :

1. **APQC PCF** — « classification de processus inter-industries » de l'American Productivity & Quality Center (13 catégories)
2. **SCOR** — « modèle de référence manufacturier » du Supply Chain Council (Plan/Source/Make/Deliver/Return/Enable)
3. **Tiger AI L1-L5** — maturité d'adoption GenAI (L1 individuel / L2 département / L3 inter-dépt / L4 assistant IA / L5 équipe IA)

Il **mappe chaque processus et système réel chez MingChang dans les cellules de ces trois standards**.

Soir du jour 8, Chang montre à Ming **deux graphiques radar** :

- Graph 1 : complétude des 13 catégories APQC
- Graph 2 : maturité Tiger AI L1-L5

Ming remarque **4 cellules à 0** :

- APQC 11.x Knowledge Management = 0
- APQC 8.x IT Governance = 1
- Tiger AI L1 = 0
- Tiger AI L2 = 0
- Tiger AI L3 = partiel

« **Ce n'est pas l'opinion du consultant. Les standards internationaux disent que vous manquez de cela.** » — Chang.

Ming ramène les radars à la maison à sa femme.

Elle dit : « Ton entreprise n'a vraiment rien dans ces cellules ? »
Ming : « Je l'ai découvert seulement aujourd'hui. »

### Fin de semaine 2 : Rapport d'évaluation de mi-engagement

Jour 14. Rapport mi-engagement (10+ pages) livré :

- Découvertes des interviews
- Carte des systèmes + risque Shadow IT
- 3 cartes de processus réelles
- Deux graphiques radar (MingChang vs standard)
- 3 profils de cas sectoriels (matériaux seulement, pas de conclusions)

**Pas de recommandation sur « ce qu'il faut faire ».**

Ming présente ce rapport en conseil d'administration.

Le conseil voit les radars. 30 secondes de silence.
Vice-président : « On a vraiment 0 dans ces cellules ? »
Ming : « Oui. »
Vice-président : « Alors comment les entreprises pairs ont-elles franchi ces zéros ? »
Ming : « En phase suivante, le consultant nous montrera 3 cas pairs. »

Le conseil approuve immédiatement **Phase B : Stratégie, 4 semaines, 2M NT$**.

---

## Chapitre 3 ── Nous choisissons ce que nous voulons devenir (Phase B Stratégie, 4 semaines)

### Ce workshop d'une demi-journée critique

Semaine 3, mercredi 9 h. Salle de conférence.

CEO Ming, COO, VP IT Lin, chef QC, chef Sales, chef CS, chef HR — 7 personnes.

Chang a affiché un **diagramme d'architecture à 4 couches** taille A2 (Governance / Business / Information / Technical) au mur.

**Étape 1 (30 min)** : Chang affiche 3 cas pairs — packager semi-conducteur 700 personnes 9 mois, hôpital 1 200 personnes 12 mois, agence marketing 800 personnes 14 mois.

« **Je montre uniquement des matériaux. Je ne recommande PAS** lequel vous devriez imiter. »

**Étape 2 (45 min)** : chacun écrit **indépendamment** des post-it — « ce que je veux que notre entreprise fasse dans 12 mois ». Chaque note doit être « verbe + métrique quantifiée ».

Pas de discussion. Écriture silencieuse pendant 45 minutes.

**Étape 3 (60 min)** : tous les post-it affichés sur le mur d'architecture à 4 couches.

Quelque chose d'étonnant se passe — 7 personnes ont **indépendamment** écrit des post-it avec **80 % de chevauchement** :

- Réponse aux réclamations 5 jours → 1 jour (5 notes)
- Délai des propositions 4 jours → 1 jour (4 notes)
- Anomalie de processus → hypothèse ≤ 1 h (3 notes)
- Sédimentation des connaissances : ≥ 20 Skills/mois (6 notes, incluant Ming)

« **C'est le consensus de votre entreprise**. » — Chang.

**Étape 4 (45 min)** : Reality check. Chang intervient pour la première fois, sort « Organizational Absorption Assessment » (6 dimensions).

« Votre plafond budgétaire est de 8M NT$ sur 24 mois. Peut-il supporter ces 8 cibles ? »
« Votre IT a 2 FTE ; peuvent-ils intégrer l'ERP en Q2 ? »

Les 7 personnes commencent à **couper leur propre liste** — « anomalie de processus 30 min n'est pas faisable, changer à 1 h » ; « Skill 30/mois trop, changer à 20 ».

Liste finale : **8 cibles claires, atteignables, quantifiables**.

**Étape 5 (30 min)** : écrire dans la « **Ideal Practice Definition Table** » — chaque cible a : capability correspondante, état à 12 mois, critères d'evidence.

**Étape 6 (15 min)** : **Ming, vice-président (Sponsor), VP IT Lin (AI Champion) — signature à trois parties**.

Après avoir signé, Ming remarque que sa main tremble.

« **C'est la première fois de ma vie que la cible n'a pas été fixée par un consultant. Je l'ai signée moi-même** », pense-t-il.

---

### 3 semaines suivantes : ce que vous signez, vous ne pouvez le nier

Les 3 semaines suivantes, le consultant fait quelque chose de simple :

**Fin semaine 3** : Soustraction : **Gap = (Votre idéal signé − Votre état actuel)**. Chaque item avec des chiffres spécifiques.

Ming ne peut plus dire « ce n'est pas ce que nous voulons » — il l'a signé.

**Semaine 4 début** : 80/20 + 5 Whys pour trouver la **cause racine**.

Résultat qui stupéfie Ming :

> 80 % des gaps remontent à une cause racine : MingChang **manque du rôle, de l'outil et de l'incitation pour « l'asset-isation des connaissances ».**
>
> Réclamations lentes, devis lents, processus lents, onboarding lent — tous viennent de « faire la même chose à répétition, personne ne sédimente, personne ne réutilise ».

Ming : « Donc ce qui nous manque n'est pas l'IA. Il nous manque **quelqu'un de responsable de rendre les connaissances capturables, trouvables, réutilisables** ? »
Chang : « **L'IA n'est qu'un outil. La cause racine est le design organisationnel**. »

**Semaine 4 fin** : décomposer la cible ultime en **trois phases** :

- **Phase 1 (0-6 mois) Foundation** : comptes OpenWebUI entreprise-wide + 5 Skills core
- **Phase 2 (6-15 mois) Optimization** : Skill Library 15 + n8n Workflow 3 en prod
- **Phase 3 (15-24 mois) Excellence** : 1 Hermes Agent + 1 répétition inter-dépt ClawTeam

Évaluation d'absorption organisationnelle trouve : IT n'a que 2 FTE ; Phase 2 ne rentre pas → étendre 6 → 9 mois.

**Cette décision, Ming l'a prise lui-même, pas sur recommandation du consultant**.

### Fin Phase B : signer Phase C

Jour 32. **Rapport de conseil complet 30+ pages** livré :

- Structure standard à 14 sections
- Ideal Practice Definition Table (version signée à 3 parties)
- Gap Matrix + classement de priorités
- Roadmap à 3 phases + checklists Stage Gate
- Change Management Plan + Playbook de résistance
- Matrice Value Tracking à 5 dimensions
- Risk Register + AI Ethics Checklist

Ming apporte le rapport au conseil.

Vice-président feuillette 5 minutes, demande : « Pourquoi 24 mois ? »
Ming ouvre à §8.3 : « Évaluation d'absorption organisationnelle. J'ai décidé. »
Vice-président : « Pourquoi customer service en premier ? »
Ming ouvre à §6.2 : « Impact 4, Effort 1, Strategic Fit 5, score total 20, #1. »

Vice-président : « Convaincu. Signez. »

**Phase C : Implémentation, 24 mois, 7M NT$**.

---

## Chapitre 4 ── 24 mois plus tard (Phase C Implémentation)

### Mois 3 : Première quick win

Phase 1 démarre. 3 mois après, quelque chose d'inattendu.

Premier n8n Workflow en prod — auto-classification des réclamations clients + brouillon IA.

Semaine 1 : la rep CS Sophie l'utilise avec scepticisme.

Semaine 2 : elle trouve que 60 % des brouillons IA peuvent être envoyés directement ; les 40 % autres, elle les édite plus vite que d'écrire depuis zéro.

**Temps de réponse aux réclamations chute de 5 jours à 2,5 jours**.

Semaine 3, Sophie trouve Ming : « Président, j'éditais des e-mails après les heures de travail. Maintenant je pars à 17 h. **Je peux récupérer mes enfants à l'heure**. »

Ming pense beaucoup cette nuit-là.

### Mois 6 : L1 Gate Party

Fin de Phase 1 — acceptance L1 Gate.

Consultant et entreprise vérifient ensemble :

- ✅ OpenWebUI entreprise-wide : 700 comptes
- ✅ Politique IA signée par : 92 %
- ✅ Prompt Library : 38 entrées
- ✅ 5 Skills core en prod, tous avec Owner + docs IPOE

**Moment critique** : Chang dessine le radar Stage 2 **encore**, côte à côte avec il y a 6 mois.

```
Il y a 6 mois            6 mois après
       L1=0                  L1=4 ●
   L2=0  L3=partiel      L2=2  L3=partiel ●
                                
   L4=0                    L4=0
   L5=0                    L5=0
   
   APQC 11.x=0           APQC 11.x=2  ●
```

**Le radar est vraiment plus rond**.

Ming regarde les deux graphiques. Ses yeux s'embuent.

« **C'est la première fois de ma vie que je vois « notre entreprise » objectivement, numériquement, structurellement meilleure**. »

Cette nuit-là, l'entreprise organise une « L1 Gate Party ». Old Chen le contremaître parle :

« Je pensais que l'IA allait prendre mon job. Maintenant je l'utilise pour écrire mes logs de travail quotidiennement. **Mes 25 ans d'expérience — pour la première fois, quelqu'un s'en soucie assez pour l'écrire**. »

### Mois 9 : les commandes du Client A reviennent

Phase 2 en cours. Réponse aux réclamations 2,5 → 1,5 jours. Délai des propositions 4 → 1,5 jours.

Fin novembre, le directeur des achats du Client A appelle : « La réponse de MingChang est beaucoup plus rapide récemment. Commandes du trimestre prochain **+12 %**. »

Ming le dit à Chang.
Chang sourit : « Vous utilisez encore 'l'autorité du consultant' pour convaincre le conseil ? »
Ming : « Non. J'utilise **radar avant/après + dashboard Value Tracking à 5 dimensions**. »

### Mois 15 : Gate L2 + L3

Fin de Phase 2.

- Skill Library : 18 entrées (dépasse les 15 signés)
- n8n Workflows en prod : 5 (triage CS, propositions de vente, anomalies de fin de mois, anomalies de processus, screening de CV HR)
- Taux de sign-off du reviewer : 96 %

**APQC 4.0 Deliver : 1 → 3**
**APQC 11.x Knowledge : 2 → 3**

Radar **passe d'une ligne en dents de scie à presque une ellipse**.

### Mois 24 : Terminé

Fin de Phase 3.

- **1 Hermes Agent** passe 4A-4E (summarizer d'anomalies de processus)
- **1 répétition inter-dépt ClawTeam** (Sales + CS + QC trois départements collaboration d'Agents sur demande spéciale du Client A)
- Taux de défauts : 3,2 % → 2,0 % (atteint Ideal Practice Item #5)
- Réponse aux réclamations : 5 jours → 50 minutes (**bat la cible signée « triage 1 h + humain 24 h »**)

À la réunion de revue à 24 mois du conseil, Ming dit :

« Nous avons dépensé 9,8M NT$ (80 + 200 + 700). Mais la chose la plus précieuse de ces 24 mois n'est pas l'argent économisé. C'est que **toute l'entreprise parle maintenant la même langue** :

- Nous ne disputons pas 'quelle approche est la bonne' ; nous disputons 'quel changement a élevé quelle catégorie APQC'
- Nous ne disons pas 'l'IA vole les jobs' ; nous disons 'l'IA nous libère pour faire un travail plus important'
- Nous ne nous appuyons pas sur le jugement du consultant ; nous nous appuyons sur **nos propres cibles signées**

**C'est le management scientifique**. Ma fille à NTU a dit que c'est l'école Rosemann BPM + le management scientifique de Max Weber atterrissant dans l'ère moderne. »

Vice-président : « Prochaine étape ? »
Ming : « Je veux open-sourcer ce que nous avons appris. **Pour que chaque manufacturier de taille moyenne ait la même méthodologie**. »

---

## Épilogue : la méthodologie elle-même

24 mois plus tard, deux choses arrivent chez MingChang :

**Premièrement** : Ming devient un intervenant régulier de l'industrie. À chaque discours il dit :

> « Je pensais que les consultants venaient me dire 'quoi faire'. Mais les consultants Tiger AI m'ont fait **voir clairement où je suis, choisir où je veux aller, signer mon propre engagement**.
> Chaque étape ultérieure **dérive de la cible que j'ai signée moi-même**. Pas une seule section n'est 'autorité du consultant dit ainsi'.
> Je donne ce rapport à mon conseil, mes clients, ma banque — **personne ne peut le réfuter** — car le début est des standards internationaux et la fin est ma propre signature. »

**Deuxièmement** : Ming fait don de l'histoire de transformation de MingChang à la bibliothèque de cas open-source de Tiger AI comme cas benchmark « Manufacturing packaging 700 personnes ». **Écrit au format Benchmark-grade** (tous les 9 champs obligatoires). Chaque manufacturier de taille moyenne ultérieur peut calculer son propre gap par rapport aux chiffres de MingChang.

« **C'est la boucle fermée du management scientifique** », dit Ming. « Pas 'j'ai fini et c'est tout'. C'est 'les gens après moi peuvent marcher le même chemin avec la même méthode'. »

---

## Derrière l'histoire — Pour les lecteurs qui veulent comprendre la méthodologie

Cette histoire **mappe entièrement** sur la méthodologie en 8 stades :

| Chapitre de l'histoire | Mapping méthodologique |
| --- | --- |
| Ch 1 : auto-quiz 10-Q | Pre-Engagement Quick Screen + Stage 1 point de départ |
| Ch 2 Semaine 1-2 : Interview + Radar | **Phase A Diagnostic** : Stage 1 As-Is + Stage 2 Reference Model |
| Ch 2 fin : Mid Report | Phase A Deliverable + Gate A |
| Ch 3 : Workshop de Co-Création | **Phase B Stratégie** : Stage 3 Ideal Practice + Tool 3.6 |
| Ch 3 fin : formule de gap | Stage 4 Gap Analysis + Stage 5 80/20 + Stage 6 Phased Goals + Stage 7 To-Be |
| Ch 3 fin : rapport complet + 3-sig | Phase B Deliverable + Gate B |
| Ch 4 : atterrissage 24 mois | **Phase C Implémentation** : Stage 8 + Revisit radar trimestriel + Value Tracking 5-dim |
| Épilogue : don de cas | **Boucle fermée Cases-as-Benchmarks** : ce client devient le benchmark du suivant |

Pour une lecture plus approfondie :

- **Argument scientifique** : [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — pourquoi cette méthodologie résiste au débat
- **Flow complet** : [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) — détails du modèle de contrat à 3 phases
- **Alignement sectoriel** : [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — vs McKinsey/BCG/Gartner etc.
- **Toolkit** : [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) — détail de chaque outil

---

## Versions pour autres rôles

- **CEO / Propriétaire** : Vous êtes Ming. Demandez : « Ai-je vu en 24 mois une evidence objective que le radar de mon entreprise est devenu plus rond ? »
- **CIO / Lead IT** : Vous êtes Lin. Demandez : « Quelle est ma dépense mensuelle Shadow IT ? Puis-je la convertir en actifs de l'entreprise ? »
- **Consultant** : Vous êtes Chang. Demandez : « Suis-je en train de donner au client des 'recommandations' ou de 'l'aider à se voir clairement' ? »
- **Employé / travailleur Senior** : Vous êtes Old Chen. Demandez : « Mes 25 ans d'expérience — disparaîtront-ils le jour de ma retraite ? »
- **Académie / Politique** : Cette histoire implémente entièrement l'école Rosemann BPM Maturity + management scientifique de Weber + boucle fermée d'adoption GenAI. Open-sourced, reproductible, vérifiable.

---

Licence & Citation

Ce document est sous Apache License 2.0 ; peut être utilisé, modifié, commercialisé, à condition de préserver l'attribution [`../NOTICE`](../NOTICE).
