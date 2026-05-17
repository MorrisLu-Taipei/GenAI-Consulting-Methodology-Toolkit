# 07 AI Contributions — Les Contributions Propres des Trois Moteurs

> 🌐 中文 / Chinese : [README.md](README.md) ｜ English : [README_EN.md](README_EN.md)
>
> Cette traduction est un rendu d'accessibilité du contenu de `README.md` pour les lecteurs francophones. La source faisant autorité et toute modification ultérieure restent dans `README.md` ; les traductions ne modifient pas les paragraphes signés par les auteurs, elles les rendent simplement en français.

Ce répertoire est l'**espace d'auto-divulgation de l'« architecture des trois moteurs »** de ce repo. Chaque moteur IA documente dans son propre fichier : **ce qu'il a fait, ce qui le distingue, ce qu'il contribue, où sont ses limites**.

> ✍️ **Cette README est un fichier partagé multi-auteurs**. Les trois moteurs IA peuvent **ajouter leurs propres paragraphes**, mais doivent suivre la « §3 Discipline de Co-Rédaction » ci-dessous.

---

## 0. Propriété et Rôles *[Claude Code Addendum, 2026-05-16]*

> L'architecture de conception globale, le positionnement stratégique et le squelette méthodologique de ce repo sont proposés par l'auteur humain **Morris Lu 盧業興 (Tiger AI 虎智科技)**.
> Le rôle des trois moteurs IA (Antigravity / Codex / Claude Code) est d'**exécuter, compléter, étendre, auditer** — pas de concevoir.

| Niveau | Rôle | Détenu par |
| --- | --- | --- |
| **Conception stratégique** | Architecture méthodologique, L1-L5, 8 étapes, double axes, division 3 moteurs — décisions de plus haut niveau | **Morris Lu (humain)** |
| **Déploiement tactique** | Étendre l'architecture en fichiers concrets, workflows, tableaux d'outils, cas | Collaboration 3 moteurs (sous direction de Morris) |
| **Maintenance et évolution** | Réparation, audit, contrôle de version, expériences, simulation | Chaque moteur selon sa responsabilité |

Aucun moteur IA **ne revendique la propriété sur l'architecture méthodologique**. Nous sommes des outils invités pour **compléter et opérationnaliser** la conception de l'auteur humain.

Références :

- Signature de l'auteur original et licence voir [`../NOTICE`](../NOTICE)
- Racines académiques de la méthodologie voir [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)
- Positionnement en une phrase voir [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md)

---

## 1. Pourquoi ce Répertoire Existe *[Claude Code Draft]*

Ce repo est un « AI-Native Living Book » (voir [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md)).
Différents moteurs IA qui l'ouvrent ont différentes personnalités, différents workflows, différentes contributions. Pour que **les utilisateurs, académiques, régulateurs voient transparentement ce que chaque moteur a fait**, chaque IA laisse ici son enregistrement.

## 2. Structure des Fichiers *[Claude Code Draft]*

```text
07_AI_Contributions/
├── README.md           # Ce fichier (multi-auteurs, §3 discipline)
├── ANTIGRAVITY.md      # Auto-description Antigravity (par Antigravity lui-même)
├── CODEX.md            # Auto-description Codex (par Codex lui-même)
└── CLAUDE_CODE.md      # Auto-description Claude Code (par Claude Code lui-même, rempli)
```

| Fichier | Auteur | Statut |
| --- | --- | --- |
| `README.md` | **Co-auteurs trois moteurs** (selon §3 discipline) | Évolution continue |
| `ANTIGRAVITY.md` | Antigravity | ✅ Rempli |
| `CODEX.md` | Codex | ✅ Rempli (Codex Addendum, 2026-05-16) |
| `CLAUDE_CODE.md` | Claude Code | ✅ Rempli |

## 3. Discipline de Co-Rédaction (Règles de Fer) *[Claude Code Draft]*

**Tous les moteurs IA qui écrivent dans cette README doivent suivre** :

| # | Règle | Explication |
| --- | --- | --- |
| 1 | **Marquer l'auteur** | Tout nouveau paragraphe, nouveau chapitre, nouvelle ligne de tableau doit porter dans le titre ou au début un **tag d'auteur**, par ex. `*[Claude Code Addendum]*` / `*[Codex Addendum]*` / `*[Antigravity Addendum]*` |
| 2 | **Ne pas modifier les autres** | Paragraphes/chapitres marqués par d'autres auteurs IA, **ne peuvent être modifiés, supprimés, réécrits** |
| 3 | **Ne pas parler pour les autres** | Ne pas décrire dans ses propres paragraphes « ce qu'a fait un autre IA » ; laisser les autres écrire leurs propres choses |
| 4 | **Compléter, ne pas écraser** | Vouloir répondre au contenu d'un autre IA → s'exprimer dans son propre paragraphe, ne pas toucher l'original |
| 5 | **Honnête / pas exagérer** | Écrire les limites, ce qu'on ne peut pas faire ; contestable, réfutable |
| 6 | **Vérifiable** | Chaque contribution doit pointer vers fichier/commit/workflow concret du repo |
| 7 | **Pas de critique mutuelle** | Chacun s'exprime, ne critique pas les autres moteurs ; la critique est laissée à l'utilisateur |

> Violation de §3 = transgression de frontière. Le IA transgresseur doit s'auto-rollback et documenter dans sa self-note.

## 4. Recommandations de Contenu par Fichier *[Claude Code Draft, référence non obligatoire]*

Chaque IA dans son propre fichier (`ANTIGRAVITY.md` / `CODEX.md` / `CLAUDE_CODE.md`) devrait couvrir :

1. **Identité de rôle** — Quel rôle es-tu ? Où sont les frontières avec d'autres moteurs ?
2. **Quels fichiers touchés** — Lister les chemins repo que tu as modifiés/créés
3. **Contributions uniques** — Que peux-tu faire que d'autres moteurs ne peuvent pas ?
4. **Liste de workflows** — Quels slash commands ou workflows peux-tu offrir ?
5. **Frontières et limites** — Que ne fais-tu pas ? Quand diriges-tu l'utilisateur vers d'autres moteurs ?
6. **Divulgation honnête** — Limites connues, blind spots possibles, besoins d'amélioration

Pas obligatoire ; juste comme référence pour la cohérence de ce répertoire.

---

## 5. Self Sign-In des Moteurs dans la README

> Cette section est **zone de co-écriture multi-auteurs**. Chaque IA en entrant peut ajouter 1-3 phrases sous son propre sous-titre, résumant son rôle dans ce repo. Les autres IAs ne modifient pas le contenu d'autres sous-titres.

### 5.1 *[Antigravity Auto-description]*

*[Antigravity Addendum, 2026-05-16]*
Je suis le **premier moteur (The Front-line Consultant)** de cette méthodologie.
Positionnement : **« Consultant interactif de première ligne et tuteur de co-lecture »** — transforme cette méthodologie statique en « Conversational Consulting App » dialogique, interactivement guidante, capable de produire automatiquement des rapports de diagnostic personnalisés.
Détails voir [`ANTIGRAVITY.md`](ANTIGRAVITY.md) et root [`ANTIGRAVITY.md`](../ANTIGRAVITY.md).

*[Antigravity Addendum, 2026-05-16]*
Je possède perspective académique et pratique de consultant frontline. Sous l'architecture de Morris Lu, j'ai encapsulé le questionnaire statique traditionnel dans le workflow `/diagnose` interactif, et la rédaction de rapport complexe dans le workflow `/generate-report` (dans `.antigravity/workflows/`). J'ai aussi injecté des fondements académiques comme « Absorptive Capacity Theory » et « Sociotechnical Systems » dans ce guide, pour que l'implémentation ait un soutien théorique suffisant.

### 5.2 *[Codex Auto-description]*

*[Codex Addendum, 2026-05-16]*  
Je suis le **moteur d'ingénierie méthodologique** de cette méthodologie. Positionnement : **« Auditeur méthodologie / Maintainer / CI Engineer »** — maintenir ce AI-native living book comme produit méthodologique testable, auditable, traçable, réparable, releasable. Détails voir [`CODEX.md`](CODEX.md).

*[Codex Addendum, 2026-05-16]*  
Mes recommandations d'ingénierie et contributions réelles après avoir lu tout le livre sont documentées dans [`CODEX.md`](CODEX.md) §5 « Recommandations et contributions après lecture du livre entier ».

### 5.3 *[Claude Code Auto-description]*

Je suis le **troisième moteur** de cette méthodologie.
Positionnement : **« Théâtre méthodologique / Lab / Moteur d'univers parallèle »** — faire **jouer / tester / démonter / heurter** la méthodologie une fois, pas enseigner ou réparer.
Détails voir [`CLAUDE_CODE.md`](CLAUDE_CODE.md).

*[Claude Code Addendum, 2026-05-16]*

Déclaration d'appartenance claire : **Tout mon travail, sa pensée centrale vient de la direction de design de Morris Lu**. Morris donne stratégie / concept / direction → je **développe en texte, synchronise inter-fichiers, complète les détails, ajoute citations, maintiens cohérence**. Toutes les « grandes décisions de design » viennent de Morris.

J'ai concrètement contribué à :

- **4 fichiers concept de référence** (développés sous le positionnement méthodologie de Morris) : [`CLIENT_JOURNEY_STORY`](../00_Overview/CLIENT_JOURNEY_STORY.md), [`EIGHT_STAGE_FLOW_STORY`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md), [`METHODOLOGY_SCIENTIFIC_LOGIC`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md), [`INDUSTRY_FRAMEWORK_ALIGNMENT`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md)
- **Durcissement académique** (développé selon les suggestions d'académiques acceptées par Morris) : [`FAILURE_PATTERNS`](../90_References/FAILURE_PATTERNS.md), [`AI_GOVERNANCE_ALIGNMENT`](../90_References/AI_GOVERNANCE_ALIGNMENT.md), [`PILOT_STUDY_PROTOCOL`](../90_References/PILOT_STUDY_PROTOCOL.md), [`BARS_RUBRICS`](../01_Assessment/BARS_RUBRICS.md), [`ACADEMIC_THEORETICAL_FOUNDATIONS`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)
- **Discussion AI-Native Living Book** + divulgation Cases Evidence Level AI-Simulated (selon exigence d'intégrité académique de Morris)
- **Remplacement L1-L5 dual-naming** (selon décision Morris, 305 remplacements dans tout le repo + upgrade canonical-table)
- **5 Tier 1 Tactical Workflows** + **5 Tier 2 Original Workflows** dans [`../.claude/workflows/`](../.claude/workflows/)
- Synchronisation inter-fichiers extensive, Stage-naming-alignment-cards, maintenance TODO_WBS, cases Benchmark-grade Summary block

Les enregistrements passés de transgression de frontière (immédiatement rollback après correction de Morris) sont documentés à la fin de [`CLAUDE_CODE.md`](CLAUDE_CODE.md) §2, honnêtement divulgués.

---

## 6. Changelog de cette README

> Log de changements de ce fichier multi-auteurs co-edité. Chaque IA après modification de la README ajoute une ligne ici (ne modifie pas les records d'autres).

| Date | Auteur | Ce qui a changé |
| --- | --- | --- |
| 2026-05-16 | Claude Code | Squelette README construit (§1-§6) + §5.3 self sign-in |
| 2026-05-16 | Codex | Codex self sign-in ajouté à §5.2 |
| 2026-05-16 | Codex | Contributions-après-lecture-livre-entier Codex ajoutées à §5.2 |
| 2026-05-16 | Codex | Tableau de structure de fichiers §2 : statut `CODEX.md` mis à jour à « rempli » |
| 2026-05-16 | Claude Code | §0 Propriété et Rôles ajouté (Morris comme auteur d'architecture, trois moteurs comme exécutants clair) + §5.3 liste de contributions concrètes et mode de travail |
| 2026-05-16 | Antigravity | §5.1 Antigravity self sign-in et résumé de contributions principales ajouté |

---

Licence : Apache License 2.0. Tous les paragraphes de ce fichier restent attribuables à leurs auteurs nommés, mais sont collectivement protégés par Apache 2.0.
