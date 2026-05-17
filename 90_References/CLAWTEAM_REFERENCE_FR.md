# ClawTeam Avis de citation & licence

> 🌐 Langue : [繁體中文](CLAWTEAM_REFERENCE.md) ｜ [English](CLAWTEAM_REFERENCE_EN.md) ｜ [Deutsch](CLAWTEAM_REFERENCE_DE.md) ｜ Français ｜ [Español](CLAWTEAM_REFERENCE_ES.md) ｜ [日本語](CLAWTEAM_REFERENCE_JA.md) ｜ [한국어](CLAWTEAM_REFERENCE_KR.md)

Le cours **L5 Multi-Agent Organization** dans cette méthodologie adopte **ClawTeam** comme plateforme d'implémentation. Ce document enregistre la source upstream, les termes de licence, l'orientation de citation et le scope de notre usage.

---

## 1. Projet upstream

| Champ | Valeur |
| --- | --- |
| **Projet** | ClawTeam |
| **Tagline** | The Evolution of AI Agents: Solo 🤖 → Swarm 🦞🤖🤖🤖 |
| **Mainteneur** | HKUDS (HKU Data Science Lab / 香港大學資料科學實驗室) |
| **URL GitHub** | <https://github.com/HKUDS/ClawTeam> |
| **Licence** | **MIT License** |
| **Version au moment d'écrire** | v0.2 — v0.3 (Stabilization → Multi-User + Web UI) |
| **Langage** | Python 3.10+ |
| **Dépendances** | `tmux`, `git`, tout agent CLI (Claude Code / Codex / nanobot / OpenClaw, etc.) |

## 2. Qu'est-ce que ClawTeam

ClawTeam est un **framework CLI pour équipes multi-agent auto-organisantes** : un humain émet un objectif de haut niveau, et l'Agent Team décompose, délègue, collabore et merge autonomement. Ce n'est pas un SDK mais un ensemble de commandes CLI + un filesystem partagé + isolation git-worktree + une couche de messaging — **tout agent CLI (Claude Code, Codex, Gemini, …) peut être orchestré par lui**.

### Architecture core

| Couche | Contenu |
| --- | --- |
| **Team Management** | Un pool d'Agents partageant workspace & task queue |
| **Workspace Isolation** | Chaque Agent tourne dans son propre git worktree & branch — pas de conflits |
| **Task Tracking** | Style Kanban avec chaînes de dépendances et auto-unblocking |
| **Inter-Agent Messaging** | Inboxes point-à-point + broadcasts |
| **Couche de transport** | Basée sur fichiers par défaut ; P2P optionnel (ZeroMQ) ; Redis sur roadmap |
| **Storage** | Tout en JSON dans `~/.clawteam/` ; pas de base de données, pas de serveur central |

### Catégories de commandes CLI core

| Catégorie | Commandes clés |
| --- | --- |
| **Team** | `clawteam team spawn-team`, `status`, `snapshot`, `restore` |
| **Task** | `clawteam task create`, `update`, `list`, `wait` (incl. `--blocked-by`) |
| **Inbox** | `clawteam inbox send`, `broadcast`, `receive`, `peek` |
| **Board** | `clawteam board show`, `live`, `attach`, `gource`, `serve` |
| **Profile** | `clawteam profile wizard`, `test`, `doctor`, `generate-profile` |
| **Context** | `clawteam context inject`, `conflicts`, `log` |
| **Spawn** | `clawteam spawn [backend] [command] --profile ...` |

### Trois scénarios de référence depuis upstream

1. **AutoResearch (8 Agents sur H100)** — 8 Agents d'exploration ont autonomement conçu 2 430+ expériences ; val_bpb amélioré 1,044 → 0,977 (+6,4%).
2. **Full-Stack Software Engineering (5 Agents)** — Architect, Backend (OAuth2 + DB), Frontend (React), Test/QA — branches parallèles auto-mergées.
3. **AI Hedge Fund (7 Agents)** — Portfolio Manager + Value/Growth/Technical/Fundamentals/Sentiment Analysts + Risk Manager — signaux convergent à travers la couche de messaging.

### Résumé roadmap

- **v0.3** — Système de config, Multi-User (`CLAWTEAM_USER`), dashboard Web UI, SSHFS / partage cross-machine cloud-based
- **v0.4** — Transport Redis (messaging cross-machine)
- **v0.5** — Couche d'état partagé (NFS ou Redis) ; `RedisTeamStore` / `RedisTaskStore`
- **v0.6** — Identity, permissions, namespacing, token auth (équipes distribuées)
- **v1.0** — Web UI complète, WebSocket temps-réel, vue d'ensemble multi-team

---

## 3. Résumé de la licence

ClawTeam est publié sous **MIT License**. MIT vous permet de :

- Utiliser, modifier et redistribuer librement
- Utiliser commercialement
- Inclure comme partie d'un produit propriétaire

**La seule condition** : lors de la redistribution, vous devez préserver l'avis de **copyright MIT** original et le **texte de License MIT**.

> ⚠️ **Important**
> Ce repo ne **redistribue pas** le code source ClawTeam. Nous **citons et enseignons** uniquement son architecture, CLI, et principes de design dans le cours L5 et dirigeons les apprenants à **installer upstream** eux-mêmes (`pip install clawteam`). Si tout dérivé du cours (ex. un fork, distribution ou customisation) redistribue le code ClawTeam, il doit inclure l'avis de licence MIT original.

---

## 4. Scope de citation dans cette méthodologie

| Scope | Traitement |
| --- | --- |
| **Architecture & concepts de design** | Utilisé comme **plateforme pédagogique primaire** pour L5 ; le syllabus décrit son architecture Team / Workspace / Task / Inbox / Transport |
| **Commandes CLI** | Utilisées **directement** durant les sessions hands-on L5 |
| **Trois scénarios de référence** | Utilisés comme **inspiration** ; cette méthodologie les localise en scénarios d'entreprise manufacturing, hôpital et retail |
| **Code source** | **Non reproduit, non forké** ; les apprenants `pip install` depuis upstream |
| **Brand / Logo** | Cité par nom « ClawTeam » dans le cours et ce doc ; pas de reproduction de logo |

## 5. Format de citation pour les apprenants

Lors de citer ClawTeam dans des slides, rapports, PoCs ou œuvres dérivées, utiliser le format suivant :

**Style APA :**

> HKUDS. (2026). *ClawTeam: Agent Swarm Intelligence* (Version 0.2-0.3) [Computer software]. GitHub. https://github.com/HKUDS/ClawTeam

**Forme courte :**

> Built on ClawTeam by HKUDS — <https://github.com/HKUDS/ClawTeam> (MIT License)

**Citation académique :**

> ClawTeam [Software]. HKUDS, 2026. Available at: https://github.com/HKUDS/ClawTeam. MIT License.

## 6. Remerciements

Nous remercions **HKUDS (HKU Data Science Lab)** d'avoir open-sourcé ClawTeam, qui a élevé la collaboration multi-agent d'entreprise d'un projet de recherche à une pratique d'engineering enseignable, apprenable et déployable. Le design du cours L5 dans cette méthodologie est profondément informé par son architecture et localisé pour l'adoption en entreprise à Taïwan et dans le monde sinophone.

---

## 7. Disclaimer

- Toute description, application ou adaptation locale de ClawTeam dans cette méthodologie représente l'interprétation de l'auteur de la méthodologie (Morris Lu / Tiger AI 虎智科技) et ne représente **pas** la position officielle de HKUDS ou des mainteneurs de ClawTeam.
- Si l'API, les commandes ou l'architecture de ClawTeam changent dans des versions plus récentes, voir le [repository upstream](https://github.com/HKUDS/ClawTeam) pour l'état autoritaire courant.
- L'auteur de la méthodologie se réserve le droit de mettre à jour ce document en ligne avec les changements de ClawTeam upstream.
