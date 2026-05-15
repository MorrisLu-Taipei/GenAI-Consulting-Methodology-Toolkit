# ClawTeam Citation & License Notice

> 🌐 中文版本 / Chinese version: [CLAWTEAM_REFERENCE.md](CLAWTEAM_REFERENCE.md)

The **L5 Multi-Agent Organization** course in this methodology adopts **ClawTeam** as its implementation platform. This document records the upstream source, license terms, citation guidance, and the scope of our use.

---

## 1. Upstream Project

| Field | Value |
| --- | --- |
| **Project** | ClawTeam |
| **Tagline** | The Evolution of AI Agents: Solo 🤖 → Swarm 🦞🤖🤖🤖 |
| **Maintainer** | HKUDS (HKU Data Science Lab / 香港大學資料科學實驗室) |
| **GitHub URL** | <https://github.com/HKUDS/ClawTeam> |
| **License** | **MIT License** |
| **Version at time of writing** | v0.2 — v0.3 (Stabilization → Multi-User + Web UI) |
| **Language** | Python 3.10+ |
| **Dependencies** | `tmux`, `git`, any CLI agent (Claude Code / Codex / nanobot / OpenClaw, etc.) |

## 2. What is ClawTeam

ClawTeam is a **CLI framework for multi-agent self-organizing teams**: a human issues one high-level goal, and the Agent Team autonomously decomposes, delegates, collaborates, and merges. It is not an SDK but a set of CLI commands + a shared filesystem + git-worktree isolation + a messaging layer — **any CLI agent (Claude Code, Codex, Gemini, …) can be orchestrated by it**.

### Core Architecture

| Layer | Content |
| --- | --- |
| **Team Management** | A pool of Agents sharing workspace & task queue |
| **Workspace Isolation** | Each Agent runs in its own git worktree & branch — no conflicts |
| **Task Tracking** | Kanban-style with dependency chains and auto-unblocking |
| **Inter-Agent Messaging** | Point-to-point inboxes + broadcasts |
| **Transport Layer** | File-based by default; optional P2P (ZeroMQ); Redis on roadmap |
| **Storage** | All JSON in `~/.clawteam/`; no database, no central server |

### Core CLI Command Categories

| Category | Key Commands |
| --- | --- |
| **Team** | `clawteam team spawn-team`, `status`, `snapshot`, `restore` |
| **Task** | `clawteam task create`, `update`, `list`, `wait` (incl. `--blocked-by`) |
| **Inbox** | `clawteam inbox send`, `broadcast`, `receive`, `peek` |
| **Board** | `clawteam board show`, `live`, `attach`, `gource`, `serve` |
| **Profile** | `clawteam profile wizard`, `test`, `doctor`, `generate-profile` |
| **Context** | `clawteam context inject`, `conflicts`, `log` |
| **Spawn** | `clawteam spawn [backend] [command] --profile ...` |

### Three Reference Scenarios from Upstream

1. **AutoResearch (8 Agents on H100)** — 8 exploration Agents autonomously designed 2,430+ experiments; val_bpb improved 1.044 → 0.977 (+6.4%).
2. **Full-Stack Software Engineering (5 Agents)** — Architect, Backend (OAuth2 + DB), Frontend (React), Test/QA — parallel branches auto-merged.
3. **AI Hedge Fund (7 Agents)** — Portfolio Manager + Value/Growth/Technical/Fundamentals/Sentiment Analysts + Risk Manager — signals converge through the messaging layer.

### Roadmap Summary

- **v0.3** — Config system, Multi-User (`CLAWTEAM_USER`), Web UI dashboard, SSHFS / cloud-based cross-machine sharing
- **v0.4** — Redis transport (cross-machine messaging)
- **v0.5** — Shared state layer (NFS or Redis); `RedisTeamStore` / `RedisTaskStore`
- **v0.6** — Identity, permissions, namespacing, token auth (distributed teams)
- **v1.0** — Full Web UI, real-time WebSocket, multi-team overview

---

## 3. License Summary

ClawTeam is released under the **MIT License**. MIT permits you to:

- Use, modify, and redistribute freely
- Use commercially
- Include as part of a proprietary product

**The only condition**: when redistributing, you must preserve the original **MIT copyright notice** and **MIT License text**.

> ⚠️ **Important**
> This repo does **not redistribute** ClawTeam source code. We only **cite and teach** its architecture, CLI, and design principles in the L5 course and direct learners to **install upstream** themselves (`pip install clawteam`). If any course derivative (e.g., a fork, distribution, or customization) redistributes ClawTeam code, it must include the original MIT license notice.

---

## 4. Scope of Citation in This Methodology

| Scope | Treatment |
| --- | --- |
| **Architecture & design concepts** | Used as the **primary teaching platform** for L5; the syllabus describes its Team / Workspace / Task / Inbox / Transport architecture |
| **CLI commands** | Used **directly** during L5 hands-on sessions |
| **Three reference scenarios** | Used as **inspiration**; this methodology localizes them into manufacturing, hospital, and retail enterprise scenarios |
| **Source code** | **Not reproduced, not forked**; learners `pip install` from upstream |
| **Brand / Logo** | Cited by name "ClawTeam" in the course and this doc; no logo reproduction |

## 5. Citation Format for Learners

When citing ClawTeam in slides, reports, PoCs, or derivative works, use the following format:

**APA-style:**

> HKUDS. (2026). *ClawTeam: Agent Swarm Intelligence* (Version 0.2-0.3) [Computer software]. GitHub. https://github.com/HKUDS/ClawTeam

**Short form:**

> Built on ClawTeam by HKUDS — <https://github.com/HKUDS/ClawTeam> (MIT License)

**Academic citation:**

> ClawTeam [Software]. HKUDS, 2026. Available at: https://github.com/HKUDS/ClawTeam. MIT License.

## 6. Acknowledgments

We thank **HKUDS (HKU Data Science Lab)** for open-sourcing ClawTeam, which has elevated enterprise multi-agent collaboration from a research project into a teachable, learnable, and deployable engineering practice. The L5 course design in this methodology is deeply informed by its architecture and localized for enterprise adoption in Taiwan and the Chinese-speaking world.

---

## 7. Disclaimer

- Any description, application, or local adaptation of ClawTeam in this methodology represents the interpretation of the methodology author (Morris Lu / Tiger AI 虎智科技) and does **not** represent the official position of HKUDS or the ClawTeam maintainers.
- If ClawTeam's API, commands, or architecture change in newer versions, refer to the [upstream repository](https://github.com/HKUDS/ClawTeam) for the authoritative current state.
- The methodology author reserves the right to update this document in line with upstream ClawTeam changes.
