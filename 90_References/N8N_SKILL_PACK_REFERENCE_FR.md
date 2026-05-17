# TigerAI-n8n-Skill-Pack Avis de citation & licence

> 🌐 Langue : [繁體中文](N8N_SKILL_PACK_REFERENCE.md) ｜ [English](N8N_SKILL_PACK_REFERENCE_EN.md) ｜ [Deutsch](N8N_SKILL_PACK_REFERENCE_DE.md) ｜ Français ｜ [Español](N8N_SKILL_PACK_REFERENCE_ES.md) ｜ [日本語](N8N_SKILL_PACK_REFERENCE_JA.md) ｜ [한국어](N8N_SKILL_PACK_REFERENCE_KR.md)

La seconde moitié du cours **L3 Workflow Automation** dans cette méthodologie cite **TigerAI-n8n-Skill-Pack** comme plateforme pédagogique pour « générer des workflows n8n à partir du langage naturel avec Antigravity ». Ce document enregistre la source upstream, les termes de licence, l'orientation de citation et le scope d'usage.

---

## 1. Projet upstream

| Champ | Valeur |
| --- | --- |
| **Projet** | TigerAI-n8n-Skill-Pack |
| **Mainteneur** | Morris Lu (盧業興) — n8n Taipei Ambassador |
| **URL GitHub** | <https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack> |
| **Licence** | Mixte : Skills / Cookbook / Specs sont **TigerAI Proprietary** ; `skills/_vendor/` est **MIT** (de czlonkowski/n8n-skills) ; `reference-workflows/` est **MIT** (de Zie619/n8n-workflows, secrets nettoyés) |
| **Échelle** | 13 Skills (7 vendor + 6 custom), 8 recettes cookbook, 2 061 reference workflows, spec DSL v1.2, 3 exemples phares |
| **Outils supportés** | Antigravity (orchestration agentique native), Claude Code (CLI / VS Code), n8n (2.10.3+), tout assistant IA (via cookbook few-shot prompting) |

> **Note :** ceci est le projet personnel de l'auteur de la méthodologie Morris Lu ; il n'y a pas d'obstacle de licence tiers à le citer, mais les sources MIT sous `_vendor/` et `reference-workflows/` doivent toujours conserver leurs avis de copyright (voir `THIRD_PARTY_NOTICES.md` upstream).

## 2. Qu'est-ce que TigerAI-n8n-Skill-Pack

Il permet aux utilisateurs de générer des workflows n8n grade-entreprise à partir de **descriptions en langage naturel** plutôt que de configuration manuelle de nodes. Le système transforme l'intent en langage simple « sticky-note » en JSON de workflow complet, documenté, prêt pour le déploiement.

### Structure à trois couches

`intent sticky-note jaune` + `notes sticky-note bleue` + `nodes de workflow` — l'utilisateur écrit l'intent → l'IA génère le JSON à trois couches → déploiement via l'API n8n.

### Trois modes d'usage

1. **Copie cookbook** — sélectionner parmi les 8 templates de recettes pré-construits
2. **Mode Q&R** — l'IA guide l'utilisateur à travers la collecte des exigences
3. **Example finder** — découvrir des implémentations similaires parmi les 2 061 reference workflows

### Installation

`bash install.sh` (Unix) ou `install.ps1` (Windows).

## 3. Pourquoi il appartient à la seconde moitié de L3

Le cours L3 est divisé en moitiés sur un principe « concepts d'abord, génération ensuite » :

- **L3 première moitié** (§5.1 Foundation + §5.2 Builder) : les apprenants **construisent à la main** Trigger / Node / AI / Human Gate / Error Handling, comprenant la structure et la gouvernance des workflows.
- **L3 seconde moitié** (§5.5) : sur cette fondation, utiliser Antigravity + TigerAI-n8n-Skill-Pack pour générer le JSON de workflow directement à partir d'intent en langage naturel, et apprendre à **réviser** le résultat généré.

> **Principe core : le Skill Pack est un accélérateur, pas un substitut à la compréhension.** Sans construire des workflows à la main dans la première moitié, les apprenants ne peuvent juger si les résultats générés sont corrects, sûrs ou maintenables.

Cours correspondant : [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) §1.1, §5.5.

## 4. Résumé de la licence

| Partie | Licence | Obligation |
| --- | --- | --- |
| `skills/` (custom), `cookbook/`, `spec/` | TigerAI Proprietary | Licence par l'auteur Morris Lu ; pas d'obstacle à l'usage au sein de cette méthodologie ; obtenir le consentement de l'auteur pour la redistribution externe |
| `skills/_vendor/` | MIT (czlonkowski/n8n-skills) | Préserver l'avis de copyright MIT |
| `reference-workflows/` | MIT (Zie619/n8n-workflows) | Préserver l'avis de copyright MIT ; les secrets sont nettoyés mais vérifier vous-même quand même |

> ⚠️ **Important**
> Ce repo ne **redistribue pas** la source TigerAI-n8n-Skill-Pack. Nous **citons et enseignons** uniquement sa structure et son usage dans le cours L3 et dirigeons les apprenants à **installer upstream** eux-mêmes. Les workflows générés par les apprenants utilisant le Skill Pack appartiennent à l'entreprise.

## 5. Scope de citation

| Scope | Traitement |
| --- | --- |
| **Comme plateforme pédagogique** | La plateforme d'implémentation primaire pour la seconde moitié de L3 (§5.5) |
| **Source / Skills** | **Non reproduits, non forkés** ; les apprenants installent eux-mêmes via `install.sh` / `install.ps1` |
| **reference-workflows** | Cités pour la leçon « Example finder » ; les apprenants doivent confirmer l'absence de secrets / endpoints internes résiduels |
| **Output généré** | Le JSON de workflow généré est un actif de l'entreprise ; doit passer les Gates 3A-3G pour compter comme PoC grade-entreprise |

## 6. Format de citation pour les apprenants

> Built with TigerAI-n8n-Skill-Pack by Morris Lu — <https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack>

## 7. Disclaimer

TigerAI-n8n-Skill-Pack est le projet personnel de l'auteur de la méthodologie Morris Lu. Si ses Skills, cookbook, spec DSL ou installation changent dans des versions plus récentes, voir le [repository upstream](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack) et son `THIRD_PARTY_NOTICES.md`. Les workflows générés par IA doivent toujours subir une révision humaine et Gate 3 Acceptance — la génération n'est pas l'acceptance.
