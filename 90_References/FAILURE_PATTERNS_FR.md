# Failure Patterns & Counter-Cases : Quand la méthodologie Tiger AI ne devrait pas être appliquée / échouera

> 🌐 Langue : [繁體中文](FAILURE_PATTERNS.md) ｜ [English](FAILURE_PATTERNS_EN.md) ｜ [Deutsch](FAILURE_PATTERNS_DE.md) ｜ Français ｜ [Español](FAILURE_PATTERNS_ES.md) ｜ [日本語](FAILURE_PATTERNS_JA.md) ｜ [한국어](FAILURE_PATTERNS_KR.md)
>
> Apache License 2.0 · Auteur : Morris Lu · Tiger AI

Dernière mise à jour : 2026-05-16

---

> **Objectif** : Une méthodologie qui ne discute que du succès est du matériel de vente. Les clients académiques / régulatoires / sérieux demandent : « **Quand échoue-t-elle ? Quand ne devrait-elle pas être appliquée ? Qu'est-ce qui tourne mal quand on saute des niveaux ?** » Ce document enregistre publiquement les failure patterns connus et counter-cases comme preuve dure de la criticabilité et de l'améliorabilité de la méthodologie.

---

## 1. Pourquoi une méthodologie doit publier les failure modes

| Audience | Pourquoi ils ont besoin de voir les échecs |
| --- | --- |
| **Reviewers académiques** | Cas uniquement de succès = selection bias → non publiable |
| **Régulateurs** | L'évaluation des risques doit inclure failure modes + conditions d'early-warning |
| **Clients sérieux** | « **Dites-moi quand vous échouez** » est la vraie question de confiance |
| **Consultants** | Failure modes = mémoire institutionnelle = éviter la répétition |

> Une méthodologie qui **ne discute que du succès** est moins digne de confiance qu'une qui **admet l'échec**.

---

## 2. Échecs par saut de niveau

### 2.1 Sauter L1 → Sauter directement à L4 Agent

**Symptômes** : Pas d'adoption L1 à l'échelle de l'entreprise. Le patron voit une démo Agent et veut un Agent service client. 3 ingénieurs construisent un Agent en 3 mois. Une fois en prod : le personnel CS a peur de l'utiliser, QC ne signe pas, IT ne sait pas comment câbler les audit logs, Compliance demande « qui porte le risque ».

**Cause racine** : Le personnel n'a pas construit de **confiance personnelle** à travers L1 ; pas de L2 Skill Library → l'Agent manque de « logique de jugement écrite par l'entreprise » ; pas de L3 Workflow → l'Agent n'a pas de pipes légales pour agir sur les systèmes ; pas de fondation de gouvernance L1-L3 → l'Agent passe en prod comme boîte noire de compliance.

**Fin typique** : Agent décommissionné en 6 mois ; le Directeur IT est blâmé ; le budget IA coupé.

### 2.2 Sauter L2 → Construire directement L3 Workflow

**Symptômes** : IT regarde des tutoriels n8n → construit des chaînes Gmail → CRM → Slack. Mois 1 : ça marche. Le personnel se plaint « les outputs sont off-tone / ne citent pas nos SOPs ». Les ingénieurs tunent les prompts, mais **chaque Workflow a 10 prompts éparpillés dans les nodes n8n — pas d'Owner, pas de version, pas de docs**.

**Cause racine** : Pas de L2 Skill Library comme « prompts + jugement + données écrits par l'entreprise » → L3 devient « playground prompt personnel de l'ingénieur IT ».

**Fin typique** : La qualité du Workflow dérive avec le temps ; 3 mois plus tard le business unit demande à revert ; IT perd la confiance.

### 2.3 Aller en L3 / L4 sans HITL

**Symptômes** : Le Workflow envoie automatiquement des emails clients, crée automatiquement des factures, place automatiquement des commandes. Mois 1 : 70% de gain d'efficacité. Mois 2 : hallucination LLM → devis mal tarifé envoyé à un client tier-A → contrat NT$ 3M perdu.

**Cause racine** : Toute IA a un taux d'hallucination ~0.5-3%. **Pas de HITL = tôt ou tard frappe un scénario zéro-tolérance**.

**Fin typique** : C-suite bannit l'IA ; AI Champion pénalisé ; méthodologie étiquetée « non fiable ».

### 2.4 Précipiter L5 ClawTeam avant que L4 ne se stabilise

**Symptômes** : Le patron voit une démo multi-agent, veut un Agent Team Sales + CS + QC inter-dépt. Pas un seul Agent n'a passé Stage Gate 4A-4E, mais 3 Agents sont enchaînés. L'evidence trail se brise entre Agents → personne ne peut tracer les décisions.

**Cause racine** : Agent unique non gouverné → multi-Agent doit perdre le contrôle (personne ne peut épingler quel Agent a causé quel problème).

**Fin typique** : Le projet se dissout en 6 mois ; retombe aux Agents uniques ; six mois gaspillés.

---

## 3. Échecs de Organizational Misfit

### 3.1 Pas d'AI Champion (driver exécutif)

**Précondition** : Chaque Phase a besoin d'au moins un Champion qui peut « coordonner inter-dépt, décider, reporter au Sponsor ».

**Échec** : Le CEO signe Phase A mais ne désigne pas de Champion → les chefs de département se rejettent la faute pendant les interviews → As-Is incomplet → qualité Phase A pauvre → le client ne signe pas Phase B.

**Refus Tiger AI** : Si aucun Champion n'est en place avant Phase B, **le consultant devrait refuser de signer** ou exiger d'abord la nomination du Champion.

### 3.2 Capacité IT insuffisante pour L3+

**Précondition** : L3 Workflow + L4 Agent ont besoin de 0,5-2 IT FTE pour la maintenance continue.

**Échec** : L'entreprise a 1 personne IT déjà maxée sur ERP / réseau / Helpdesk. 5 Workflows passent en prod → personne ne les maintient → 50% échouent en 6 mois → le personnel retombe au manuel.

**Refus Tiger AI** : Si Tool 6.3 Organizational Absorption « IT FTE » < minimum Phase 2 (0,5 FTE dédiés), **conseiller fortement au client d'ajouter d'abord de l'IT**.

### 3.3 Compliance/Régulation insuffisante (industries sensibles)

**Précondition** : Financial / Healthcare / Government / Legal ont de fortes exigences de compliance.

**Échec** : L'hôpital déploie une IA CS sans révision HIPAA / PIPA / droits des patients → audité 3 mois plus tard par le ministère de la Santé → IA retirée, amendée, dans les news → non seulement le plan IA échoue mais toute la gouvernance IT est questionnée.

**Refus Tiger AI** : Industries sensibles sans Compliance Officer / révision avocat dédiés → **le rapport de fin Phase A doit marquer « compliance non vérifiée → suspendre Phase B »**.

### 3.4 Le turnover exécutif casse la roadmap 24 mois

**Précondition** : Phase C 24 mois a besoin d'un support Sponsor stable.

**Échec** : Phase A signée par CEO ; CEO part au mois 9 de Phase C → nouveau CEO en désaccord → Phase C gelée → NT$ 9,8M investis, outputs partiels (L1-L3) retenus mais L4-L5 abandonnés.

**Mitigation Tiger AI** : Mécanisme d'exit Quarterly Gate C de Phase C = même si le Sponsor change, chaque trimestre est ré-évaluable indépendamment, pas sunk-cost-all-lost.

---

## 4. Limitations connues de la méthodologie

### 4.1 Le modèle de scoring manque de validation psychométrique

**Statut** : 6 constructs × échelle 0-4 et frontières L1-L5 sont **consensus d'experts**, **pas encore validés** via Cronbach's α / EFA / CFA / inter-rater reliability.

**Problèmes potentiels** :

- Deux consultants scorant la même entreprise peuvent yielder L2 vs L3
- « 50-60 = frontière L2 vs 41-60 = L2 » manque de base empirique
- Les constructs peuvent avoir collinéarité ; le nombre de facteurs réel peut différer

**Réponse Tiger AI** : Le rapport marque explicitement « version expert-consensus, en attente de validation psychométrique » ; `PILOT_STUDY_PROTOCOL.md` planifie la recherche empirique ; les submissions académiques devraient baisser la force de claim à « a proposed framework ».

### 4.2 Evidence Level de la bibliothèque de cas

**Statut** : 7 cas sont des **composites anonymisés** avec Evidence Level 2 (par Tool 8.9).

**Problèmes potentiels** : Les clients peuvent demander « ces chiffres sont-ils réels ou fabriqués ? » ROI ~358%, taux de défaut 3,2 → 2,0% **ne peut être utilisé comme commitments contractuels pour aucun client unique**.

**Réponse Tiger AI** : Chaque header de cas marque Evidence Level et nature Composite ; le SOW utilise la baseline propre du client, pas les chiffres de cas ; remplacer progressivement par de vrais cas longitudinaux L3-L5.

### 4.3 Reconnaissance Tiger AI L1-L5 encore nouvelle

**Statut** : Tool 2.5 self-qualification 9/10 ; Condition 6 (large reconnaissance industrielle) est △ partielle.

**Problèmes potentiels** : Les contacts initiaux demandent « APQC, SCOR sont reconnus internationalement — par quelle autorité Tiger AI L1-L5 ? » Les citations académiques n'ont pas atteint une masse critique.

**Réponse Tiger AI** : Open-source (Apache 2.0 + GitHub) ; engager proactivement avec les groupes de travail ISO/IEC / discussions IEEE AI Maturity standards ; construire de la recherche conjointe avec des institutions partenaires académiques (partenaires spécifiques divulgués après signature MOU).

---

## 5. Anti-patterns au niveau consultant (échecs internes)

### 5.1 Sauter Phase A → Signer directement Phase B-C

**Symptômes** : Pression de vente → sauter Phase A → signer directement un engagement 6 mois.
**Résultat** : Pas d'As-Is / RM / Ideal signé par le client → au Stage 4+ le client peut nier « ce n'est pas ce que nous voulions » → consultant sur la défensive.
**Discipline** : **Ne jamais sauter Phase A**. C'est l'ancre pour tout ce qui suit.

### 5.2 Rédiger l'Ideal Practice du client pour lui

**Symptômes** : Le consultant rédige l'Ideal Practice pour que le client signe, pour gagner du temps.
**Résultat** : Le client ne ressent pas d'ownership → conteste plus tard chaque item → la chaîne de raisonnement s'effondre.
**Discipline** : **Doit lancer Tool 3.6 Co-Creation Workshop 6 étapes**. Vote indépendant, consensus collectif, reality check, table de définition, signature à 3 parties — aucune étape ne peut être sautée.

### 5.3 Rapport basé uniquement sur L1 Self-Report

**Symptômes** : Écriture précipitée → toutes les conclusions du questionnaire d'auto-évaluation du client.
**Résultat** : Audité par l'audit interne du client / société mère → « insufficient evidence » → projet entier retourné.
**Discipline** : Par Tool 8.9 Evidence Hierarchy, **toute conclusion majeure a besoin de support L3+ (system log)**. Chaque paragraphe marque `[E:L#]`.

### 5.4 Mélanger Risk dans Gap Analysis

**Symptômes** : Le chapitre Stage 4 mélange « ce risque est élevé, non recommandé » jugement subjectif.
**Résultat** : Stage 4 devient subjectif → le client conteste « pourquoi penses-tu que c'est risqué » → chapitre réécrit.
**Discipline** : **Stage 4 = inventaire objectif de gap, PAS d'évaluation de risque**. Le risque appartient à Stage 8 Risk Register.

### 5.5 Sauter le revisit radar Stage 2 trimestriel à Gate C

**Symptômes** : Pendant l'implémentation, focus sur les PoCs, ne rapporte que le progrès chaque trimestre, pas de revisit radar.
**Résultat** : PoCs faits mais complétude structurelle inchangée → 24 mois plus tard « avons-nous réellement amélioré ? » sans réponse.
**Discipline** : **Quarterly Gate C doit revisiter le radar**. Ne pas le faire = négligence du consultant.

---

## 6. Hard Refusal Conditions

Tiger AI **devrait refuser** de signer Phase C sous ces conditions (même si le client le veut) :

- [ ] **Phase A + B non complétées** → pas d'Ideal Practice signé → refuser Phase C
- [ ] **Pas d'AI Champion confirmé en place** → refuser Phase C
- [ ] **IT FTE insuffisant pour la Phase cible** → recommander fortement de retarder + ajouter de l'IT d'abord
- [ ] **Industrie sensible sans Compliance Officer / révision avocat** → refuser Phase C
- [ ] **Sponsor pas en place (pas de support CEO clair)** → refuser Phase C
- [ ] **Le client veut sauter des niveaux (ex. sauter L1-L3 → L4-L5)** → refuser, exiger la fondation Phase 1
- [ ] **Budget insuffisant pour la phase actuelle** → refuser, conseiller la réduction de scope

---

## 7. Customer Exit Protocol

Si une Phase A / B / C échoue, Tiger AI s'engage :

1. **Échec Phase A** : Le client conserve le mid-engagement report + interview summaries + radar → **peut s'exécuter lui-même ou engager le prochain consultant**
2. **Échec Phase B** : Rapport complet + table Ideal Practice signée préservés → **peut transférer à un autre consultant**
3. **Échec Phase C mi-chemin (décision Quarterly Gate C de stopper)** : Phases complétées préservées + docs de gouvernance préservés + code / Skills / Workflows entièrement transférés au client (le consultant **ne détient aucun asset client**)
4. **Pas de prise en otage des assets client** : par [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) 7 Pillars #1 « Client Hosts »

---

## 8. Comment utiliser ce document

| Rôle | Usage |
| --- | --- |
| **Formation interne consultants** | Lecture obligatoire d'onboarding ; revue trimestrielle d'équipe « quels failure patterns avons-nous frappés le trimestre dernier » |
| **Pré-signature avec client** | Le consultant partage proactivement ce doc → le client fait confiance « ce consultant ne vend pas que du succès, discute honnêtement de l'échec » |
| **Submissions académiques** | Citer comme preuve de criticité / falsifiabilité de la méthodologie |
| **Documents régulatoires / bid** | Joindre comme preuve d'évaluation des risques + mitigation |

> **Discuter honnêtement de l'échec = forme la plus élevée de skill de vente**. Les clients n'achètent pas « succès garanti » mais « nous savons quoi faire quand ça échoue ».

---

Licence & Citation

Ce document est sous Apache License 2.0 ; peut être utilisé, modifié, commercialisé, à condition de préserver l'attribution [`../NOTICE`](../NOTICE).
