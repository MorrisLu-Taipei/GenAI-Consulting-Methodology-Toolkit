# 05 Sales — Matériel de Vente Externe

> 🌐 中文 / Chinese : [README.md](README.md) ｜ English : [README_EN.md](README_EN.md)

## 1. Objectif de ce Répertoire

Ce répertoire est la première pièce pour **transformer la méthodologie en business** : **matériel de vente externe**.

`01`-`03` sont la méthodologie de conseil elle-même (très forte, mais « forte » ne se transforme pas seule en mandats) ; le problème que résout ce répertoire : **avant que le prospect entre dans le diagnostic — comment Sales le fait « vouloir acheter » ?** Ce répertoire fournit tout, du DM one-pager, trois longueurs d'outline de deck, spécifications visuelles, jusqu'à 20 FAQ ventes — pour que Sales ait du matériel prêt, cohérent, professionnel à toutes les étapes de Lead Gen, proposition, gestion d'objections.

Cela correspond à la **phase Sales** du cycle d'engagement : amène un lead froid à « prêt à remplir le questionnaire et entrer en diagnostic ».

Qui utilise : Sales (Lead Gen / Sales Rep / Closer), consultants (briefing méthodologie au C-level), designers (produisent les visuels réels selon spécification).

## 2. Position dans la Méthodologie

| Axe | Mapping |
| --- | --- |
| Flux de service 3 phases | **« Pré-vente » avant le diagnostic** — amène le client au point d'entrer en diagnostic |
| Structure de conseil 8 étapes | Ne correspond à aucune des 8 étapes (les 8 étapes sont après signature) |
| Maturité L1-L5 | Matériel de vente utilise le modèle L1-L5 comme argument |
| Engagement Lifecycle | **Sales — Lead Qualification / Discovery / Proposal** |

## 3. Objectifs & Bénéfices

| Objectif | Bénéfice |
| --- | --- |
| Matériel externe cohérent et professionnel | Différents Sales parlent la méthodologie de façon uniforme, marque pro |
| Trois longueurs de deck pour différents contextes | C-level 10 pages, standard 20 pages, méthodologie 30 pages, chacun adapté |
| 20 FAQ ventes | Sales a réponses standards aux objections, pas d'improvisation |
| Spécifications visuelles | Designers ont brief clair, assets visuels cohérents |
| One-pager DM | Premier contact avec client donne déjà un livrable pro |

**Si ce répertoire est sauté** : chaque Sales fait ses propres slides, discours inconsistants, objections improvisées, première impression de la méthodologie dispersée.

## 4. Workflow & Logique

```text
Lead Gen
   → ONE_PAGER_OUTLINE (DM one-pager, livrable premier contact)
Première réunion formelle
   → EXECUTIVE_DECK_OUTLINE (10 pages C-level, urgence + crédibilité méthodologie)
Proposition approfondie
   → STANDARD_SALES_DECK_OUTLINE (20 pages, pour chef de département/IT/RH)
   → CONSULTING_METHODOLOGY_DECK_OUTLINE (30 pages, profondeur méthodo, pour CIO/chef stratégie/académiques)
Gestion d'objections (continu)
   → SALES_FAQ (20 Q&R standards)
Produire visuels réels
   → VISUAL_ASSETS_SPEC (designer produit PNG/SVG/fichiers print selon spec)
```

| Étape | Qui | Quand | Input | Output |
| --- | --- | --- | --- | --- |
| Envoyer DM one-pager | Sales (Lead Gen) | Lead Gen | one-pager | Cognition client initiale |
| Briefing C-level | Sales / consultant | Première réunion | deck 10 pages | Client prêt pour discussion approfondie |
| Proposition approfondie | Closer | Phase proposition | deck 20/30 pages | Client prêt à signer SOW |
| Traiter objections | Sales / Closer | Continu | SALES_FAQ | Doutes du client levés |
| Produire visuels | Designer | Phase de production | VISUAL_ASSETS_SPEC | Fichiers visuels réels |

> Logique : matériel **de superficiel à profond** — one-pager (susciter intérêt) → 10 pages (créer urgence) → 20/30 pages (conviction profonde) → FAQ (lever doutes). Chacun pointe vers la même étape suivante : « remplir le questionnaire 10 items, entrer en diagnostic `01_Assessment` ».

## 5. Descriptions de Fichiers

### `SALES_VALUE_PROPOSITION.md`

Propositions de valeur par rôle et scripts de vente. Pour les douleurs de CEO / COO / CIO / IT / RH / chef de département, propositions de valeur correspondantes, plus scripts 30 secondes / 3 minutes / 10 minutes et objections courantes.

### `SALES_FAQ.md`

20 FAQ ventes externes. Questions les plus posées (différence avec Big-4, structure de prix, timeline, customisation, cloud/on-prem, sécurité, ROI, IP, choix modèle AI, gestion d'échec…), 2-4 phrases de réponse standard chacune, zh+en parallèles.

### `ONE_PAGER_OUTLINE.md`

Script de contenu et brief de layout pour PDF / imprimé one-pager (env. 600 mots). Inclut Hero tagline, trois douleurs, flux 3 phases, carte L1-L5, livrables vérifiables, applicabilité 3 secteurs, ROI proof point, CTA, plus suggestions layout/couleurs/typo pour designer.

### `EXECUTIVE_DECK_OUTLINE.md`

Outline deck C-level 10 pages. Cible CEO/COO/CIO/CTO. Chaque page : titre, message clé, contenu, suggestion visuelle, notes orateur. Couvre vision, urgence, méthodologie, L1-L5, story arc, ROI, gouvernance, différenciation compétitive, prix, étapes suivantes.

### `STANDARD_SALES_DECK_OUTLINE.md`

Outline deck standard 20 pages. Cible chefs de département, PM, IT Lead, RH, AI Champion. Plus large que 10 pages, inclut teasers de cours par niveau, scénarios PoC, Stage Gate, package de livraison, démarrage 3 phases.

### `CONSULTING_METHODOLOGY_DECK_OUTLINE.md`

Outline deck méthodologie 30 pages. Cible CIO, chef stratégie, gros offices de transformation digitale, académiques. Profondeur méthodologie — 8 étapes, enchaînement L1-L5, modèle de scoring, extraits de cas, gouvernance, racines académiques (Prof. Michael Rosemann, QUT).

### `VISUAL_ASSETS_SPEC.md`

Spec ASCII et brief designer pour 3 assets visuels externes : diagramme flux service 3 phases, carte maturité L1-L5, visuel liste livrables vérifiables. Chacun avec spec ASCII, alternatives de layout, exigences couleur/typo/taille/accessibilité.

### `*_EN.md`

Versions anglaises sibling des fichiers ci-dessus.

## 6. Mapping vers Autres Répertoires

| Répertoire | Relation avec ce répertoire | Flux de données |
| --- | --- | --- |
| `00_Overview` | Squelette story du matériel de vente vient de la story | `00` story → `05` matériel |
| `01_Assessment` | Tout le matériel de vente pointe vers « remplir questionnaire → diagnostic » | `05` → drive vers `01` |
| `02_Course_Design` | Teasers de cours dans les decks viennent du design de cours | `02` cours → `05` teaser |
| `03_Consulting_Report` | Deck méthodologie 30 pages cite les 8 étapes et frameworks | `03` méthodologie → `05` deck |
| `04_Scenarios` | Matériel de vente utilise cas et scénarios complets pour justifier valeur | `04` cas → `05` justification |
| `06_Delivery` | Prix/packages du deck correspondent au cycle et pricing | `06` pricing ↔ `05` deck |

## 7. Scénarios d'Usage Communs

- **Lead Gen** : Sales envoie DM one-pager fait à partir de `ONE_PAGER_OUTLINE.md`.
- **Première réunion** : utiliser `EXECUTIVE_DECK_OUTLINE.md` pour briefing 15-20 min C-level, finir par « remplir questionnaire 10 items ».
- **Proposition approfondie** : selon cible choisir 20 pages (chef de département) ou 30 pages (CIO/chef stratégie).
- **Client dit « trop cher / on a déjà ChatGPT / les données sont sécurisées ? »** : ouvrir `SALES_FAQ.md` pour réponse standard.
- **Faire des visuels** : donner `VISUAL_ASSETS_SPEC.md` au designer pour produire fichiers réels.

---

## ⭐ Cross-Topic Quick References : 5 Thèmes Centraux, où Trouver

Toute la méthodologie a 5 artères principales traversant tous les répertoires. Comment ce répertoire se connecte à chacune :

| Cross-Topic | Lieu principal | Comment ce répertoire se connecte |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lecture trois moteurs** | Root [`README_FR.md`](../README_FR.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | **AI-Native Living Book + trois moteurs est un nouvel argument de vente** — après adoption, le client a « méthodologie + partenaire AI de co-lecture » ; le deck 30 pages peut pitcher la différenciation de la division des trois moteurs (frontline Antigravity / audit Codex / stratégie Claude Code) |
| 🎓 **Fondement académique (7 piliers)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **Le deck 30 pages cite Prof. Rosemann (QUT) + 7 piliers théoriques** comme différenciation (pour académiques, CIO, conseil) ; `SALES_FAQ.md` utilise les 7 piliers comme base pour « différence avec Big-4 / McKinsey » |
| 📚 **Éducation L1-L5** | [`../02_Course_Design/`](../02_Course_Design/) | **Le deck 20 pages contient teasers de cours par niveau** (chemin L1-L5, scénarios PoC, Stage Gate) ; ONE_PAGER contient carte L1-L5 ; decks citent ratio de cours et curricula profonds de `02` |
| 🔁 **Conseil / 8 étapes + Closed-Loop Phase A→B→C** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Tout matériel de vente dirige vers « remplir questionnaire → démarrer Phase A »** ; deck 20/30 pages contient modèle de contrat 3 phases (Phase A 2W + Phase B 4W + Phase C 24M) + revue radar trimestrielle ; EXECUTIVE_DECK contient story arc 8 étapes |
| 📖 **Références / remerciements** | [`../90_References/`](../90_References/) §2 remerciements | **Les decks Sales sont majoritairement self-authored** (pas de citations tierces) ; `SALES_FAQ.md` cite les 7 piliers comme base ; remerciements citent Prof. Rosemann (QUT) ; si client demande « pourquoi ces outils », pointer vers les appreciation cards de 90_References §2 |
