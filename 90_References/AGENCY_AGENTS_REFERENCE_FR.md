# agency-agents Avis de citation & licence

> 🌐 Langue : [繁體中文](AGENCY_AGENTS_REFERENCE.md) ｜ [English](AGENCY_AGENTS_REFERENCE_EN.md) ｜ [Deutsch](AGENCY_AGENTS_REFERENCE_DE.md) ｜ Français ｜ [Español](AGENCY_AGENTS_REFERENCE_ES.md) ｜ [日本語](AGENCY_AGENTS_REFERENCE_JA.md) ｜ [한국어](AGENCY_AGENTS_REFERENCE_KR.md)

La seconde moitié du cours **L2 Knowledge Codification** dans cette méthodologie (spécifiquement le parcours L2-B Agentic Developer) cite **agency-agents** comme matériel pédagogique pour le module « bibliothèque de personas d'agent prêts à l'emploi ». Ce document enregistre la source upstream, les termes de licence, l'orientation de citation et le scope d'usage.

---

## 1. Projet upstream

| Champ | Valeur |
| --- | --- |
| **Projet** | agency-agents |
| **Mainteneur** | @msitarzewski (maintenu par la communauté) |
| **URL GitHub** | <https://github.com/msitarzewski/agency-agents> |
| **Licence** | **MIT License** |
| **Échelle** | 144+ personas d'agent sur 12 divisions |
| **Outils supportés** | Claude Code, GitHub Copilot, Cursor, Aider, Windsurf, OpenCode, Antigravity, Gemini CLI, OpenClaw, Qwen Code, Kimi Code |

## 2. Qu'est-ce qu'agency-agents

agency-agents est une **collection de définitions de personas d'agent IA** : chaque agent est un fichier markdown contenant traits d'identité, mission core, spécifications techniques, processus de workflow et critères de succès mesurables. Ce n'est pas un ensemble de templates de prompt génériques mais un roster de « spécialistes virtuels déployables ».

### 12 divisions

`engineering` (25+ agents : Frontend Developer, Backend Architect, Security Engineer…), `design`, `marketing`, `sales`, `product`, `project-management`, `testing`, `support`, `finance`, `game-development`, `academic`, `specialized`, `spatial-computing`.

### Installation

Installé via `./scripts/install.sh`, qui auto-détecte les outils IA installés et les traite en parallèle.

## 3. Pourquoi il appartient à L2

Le cœur de L2 Knowledge Codification est « emballer l'expérience de travail en Skills réutilisables ». La seconde moitié du parcours L2-B Agentic Developer enseigne une idée clé : **chaque Skill n'a pas besoin d'être construit depuis zéro.** agency-agents fournit 144+ personas d'agent matures comme point de départ — les apprenants sélectionnent, customisent et les incorporent dans la Skill Library de l'entreprise au lieu de réinventer la roue.

Cours correspondant : [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6.

## 4. Résumé de la licence

agency-agents est publié sous **MIT License**. MIT permet l'usage libre, la modification, la redistribution et l'usage commercial, y compris comme partie d'un produit propriétaire ; **la seule condition** est que la redistribution doit préserver l'avis de copyright MIT et le texte de licence originaux. MIT n'exige pas strictement d'attribution visible aux utilisateurs finaux (bien que l'auteur note qu'elle est appréciée).

> ⚠️ **Important**
> Ce repo ne **redistribue pas** la source agency-agents. Nous **citons et enseignons** uniquement sa structure et son usage dans le cours L2 et dirigeons les apprenants à **installer upstream** eux-mêmes. Les personas d'agent customisés par les apprenants appartiennent à l'entreprise, mais il est recommandé de noter la source originale (agency-agents + version) dans la documentation Skill.

## 5. Scope de citation

| Scope | Traitement |
| --- | --- |
| **Comme matériel pédagogique** | Utilisé comme cas « bibliothèque d'agents prête à l'emploi » dans la seconde moitié de L2-B ; enseigne installer, parcourir, sélectionner, customiser |
| **Source / fichiers de persona** | **Non reproduits, non forkés** ; les apprenants installent eux-mêmes via `./scripts/install.sh` |
| **Output customisé** | Les personas customisés deviennent des entrées de la Skill Library de l'entreprise ; attribution de source recommandée |

## 6. Format de citation pour les apprenants

> Basé sur agency-agents par @msitarzewski — <https://github.com/msitarzewski/agency-agents> (MIT License)

## 7. Disclaimer

Toute description, application ou orientation de customisation pour agency-agents dans cette méthodologie représente l'interprétation de l'auteur de la méthodologie (Morris Lu / Tiger AI 虎智科技) et ne représente pas la position officielle de @msitarzewski ou de la communauté agency-agents. Si la structure, l'installation ou la taxonomie d'agent d'agency-agents change dans des versions plus récentes, voir le [repository upstream](https://github.com/msitarzewski/agency-agents).
