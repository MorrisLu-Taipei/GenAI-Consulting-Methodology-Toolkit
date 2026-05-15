# ClawTeam 引用與授權說明 / ClawTeam Citation & License Notice

> 🌐 English version: [CLAWTEAM_REFERENCE_EN.md](CLAWTEAM_REFERENCE_EN.md)

本方法論的 **L5 Multi-Agent Organization** 課程以 **ClawTeam** 作為實作基礎平台。本檔詳列原始來源、授權條款、引用方式與我們的使用範圍。

The **L5 Multi-Agent Organization** course in this methodology adopts **ClawTeam** as its implementation platform. This document records the upstream source, license terms, citation guidance, and the scope of our use.

---

## 1. 原始專案 / Upstream Project

| 項目 / Field | 內容 / Value |
| --- | --- |
| **專案名稱 / Project** | ClawTeam |
| **副標 / Tagline** | The Evolution of AI Agents: Solo 🤖 → Swarm 🦞🤖🤖🤖 |
| **作者 / Maintainer** | HKUDS (HKU Data Science Lab / 香港大學資料科學實驗室) |
| **GitHub URL** | <https://github.com/HKUDS/ClawTeam> |
| **授權 / License** | **MIT License** |
| **撰寫本檔時版本 / Version at time of writing** | v0.2 — v0.3 (Stabilization → Multi-User + Web UI) |
| **語言 / Language** | Python 3.10+ |
| **依賴 / Dependencies** | `tmux`, `git`, 任一 CLI agent (Claude Code / Codex / nanobot / OpenClaw 等) |

## 2. ClawTeam 是什麼 / What is ClawTeam

ClawTeam 是一個 **多 Agent 自組成團隊的 CLI 框架**：人類只下一個高階目標，Agent Team 自行完成任務拆解、分派、協作、合併。它不是一個 SDK，而是一組 CLI 命令 + 共享檔案系統 + git worktree 隔離 + 訊息傳遞層，**任何 CLI agent (Claude Code、Codex、Gemini …) 都可被它編排**。

ClawTeam is a **CLI framework for multi-agent self-organizing teams**: a human issues one high-level goal, and the Agent Team autonomously decomposes, delegates, collaborates, and merges. It is not an SDK but a set of CLI commands + a shared filesystem + git-worktree isolation + a messaging layer — **any CLI agent (Claude Code, Codex, Gemini, …) can be orchestrated by it**.

### 核心架構 / Core Architecture

| 層次 / Layer | 內容 / Content |
| --- | --- |
| **Team 管理 / Team Management** | 一組共享工作區與任務隊列的 Agent 群 / A pool of Agents sharing workspace & task queue |
| **Workspace 隔離 / Workspace Isolation** | 每個 Agent 跑在自己的 git worktree 與獨立分支，避免衝突 / Each Agent runs in its own git worktree & branch — no conflicts |
| **任務追蹤 / Task Tracking** | Kanban 風格、支援 dependency chains、自動 unblock / Kanban-style with dependency chains and auto-unblocking |
| **Inter-Agent 訊息 / Messaging** | 點對點 inbox + broadcast / Point-to-point inboxes + broadcasts |
| **Transport Layer** | 預設 File-based；可選 P2P (ZeroMQ)；Roadmap 含 Redis / File-based by default; optional P2P (ZeroMQ); Redis on roadmap |
| **儲存 / Storage** | `~/.clawteam/` 全為 JSON，無資料庫無中央伺服器 / All JSON in `~/.clawteam/`; no database, no central server |

### 核心 CLI 命令類別 / Core CLI Command Categories

| 類別 / Category | 主要命令 / Key Commands |
| --- | --- |
| **Team** | `clawteam team spawn-team`, `status`, `snapshot`, `restore` |
| **Task** | `clawteam task create`, `update`, `list`, `wait` (含 `--blocked-by`) |
| **Inbox** | `clawteam inbox send`, `broadcast`, `receive`, `peek` |
| **Board** | `clawteam board show`, `live`, `attach`, `gource`, `serve` |
| **Profile** | `clawteam profile wizard`, `test`, `doctor`, `generate-profile` |
| **Context** | `clawteam context inject`, `conflicts`, `log` |
| **Spawn** | `clawteam spawn [backend] [command] --profile ...` |

### 原始專案三個範例情境 / Three Reference Scenarios from Upstream

1. **AutoResearch (8 Agents on H100)** — 8 個探索 Agent 自主設計 2,430+ 實驗，val_bpb 自 1.044 改善到 0.977 (+6.4%)。
   8 exploration Agents autonomously designed 2,430+ experiments; val_bpb improved 1.044 → 0.977 (+6.4%).
2. **Full-Stack Software Engineering (5 Agents)** — Architect、Backend (OAuth2 + DB)、Frontend (React)、Test/QA，平行分支自動合併。
   Architect, Backend (OAuth2 + DB), Frontend (React), Test/QA — parallel branches auto-merged.
3. **AI Hedge Fund (7 Agents)** — Portfolio Manager + Value/Growth/Technical/Fundamentals/Sentiment Analyst + Risk Manager，訊號透過 messaging 層匯合。
   Portfolio Manager + Value/Growth/Technical/Fundamentals/Sentiment Analysts + Risk Manager — signals converge through the messaging layer.

### Roadmap 摘要 / Roadmap Summary

- **v0.3** — Config system、Multi-User (`CLAWTEAM_USER`)、Web UI dashboard、SSHFS/雲端可跨機共用
- **v0.4** — Redis transport (跨機訊息)
- **v0.5** — 共享 state layer (NFS or Redis)；`RedisTeamStore` / `RedisTaskStore`
- **v0.6** — 身份、權限、namespacing、token auth (分散式團隊)
- **v1.0** — 完整 Web UI、WebSocket 即時、多 team overview

---

## 3. 授權條款摘要 / License Summary

ClawTeam 採用 **MIT License**。MIT 允許您：

- 自由使用、修改、再散布
- 商業使用
- 將其作為閉源產品的一部分

**唯一條件**：再散布時必須保留原始 **MIT 著作權聲明** 與 **MIT License 文字**。

ClawTeam is released under the **MIT License**. MIT permits you to:

- Use, modify, and redistribute freely
- Use commercially
- Include as part of a proprietary product

**The only condition**: when redistributing, you must preserve the original **MIT copyright notice** and **MIT License text**.

> ⚠️ **重要 / Important**
> 本 repo **不重新散布** ClawTeam 的原始碼。我們僅在 L5 課程中 **教學引用** 其架構、CLI 與設計理念，並引導學員 **自行從 GitHub 安裝** 原專案 (`pip install clawteam`)。若任何課程衍生品 (e.g. Fork、Distribution、Customization) 需重新散布 ClawTeam 程式碼，請務必同時附上原始 MIT 授權聲明。
> This repo does **not redistribute** ClawTeam source code. We only **cite and teach** its architecture, CLI, and design principles in the L5 course and direct learners to **install upstream** themselves (`pip install clawteam`). If any course derivative (e.g., a fork, distribution, or customization) redistributes ClawTeam code, it must include the original MIT license notice.

---

## 4. 在本方法論的引用範圍 / Scope of Citation in This Methodology

| 範圍 / Scope | 處理方式 / Treatment |
| --- | --- |
| **架構與設計概念** / Architecture & design concepts | 在 L5 課程中作為**主要教學平台**；課綱描述其 Team / Workspace / Task / Inbox / Transport 五層架構 / Used as the **primary teaching platform** for L5; the syllabus describes its Team / Workspace / Task / Inbox / Transport architecture |
| **CLI 命令** / CLI commands | 在 L5 上機操作課程中**直接使用** `clawteam` 命令 / Used **directly** during L5 hands-on sessions |
| **三個範例情境** / Three reference scenarios | 作為**靈感來源**，本方法論在地化為製造業、醫院、零售三類企業情境 / Used as **inspiration**; this methodology localizes them into manufacturing, hospital, and retail enterprise scenarios |
| **程式碼** / Source code | **未重製、未 fork**；學員直接從上游 `pip install` / **Not reproduced, not forked**; learners `pip install` from upstream |
| **品牌 / Logo** | 在課程與本文件中以 "ClawTeam" 名稱引用，無 logo 重製 / Cited by name "ClawTeam" in the course and this doc; no logo reproduction |

## 5. 學員引用建議格式 / Citation Format for Learners

於課堂簡報、報告、PoC、衍生作品中引用 ClawTeam 時，建議使用以下格式：

When citing ClawTeam in slides, reports, PoCs, or derivative works, use the following format:

**APA 格式 / APA-style:**

> HKUDS. (2026). *ClawTeam: Agent Swarm Intelligence* (Version 0.2-0.3) [Computer software]. GitHub. https://github.com/HKUDS/ClawTeam

**簡短格式 / Short form:**

> Built on ClawTeam by HKUDS — <https://github.com/HKUDS/ClawTeam> (MIT License)
> 基於 HKUDS 之 ClawTeam — <https://github.com/HKUDS/ClawTeam> (MIT 授權)

**論文 / Academic citation:**

> ClawTeam [Software]. HKUDS, 2026. Available at: https://github.com/HKUDS/ClawTeam. MIT License.

## 6. 鳴謝 / Acknowledgments

特別感謝 **HKUDS (HKU Data Science Lab)** 開源 ClawTeam，使企業導入 multi-agent collaboration 從研究專案走向可教、可學、可導入的工程實踐。本方法論的 L5 課程設計受其架構深度啟發，並在地化為適合台灣與中文世界企業導入的形式。

We thank **HKUDS (HKU Data Science Lab)** for open-sourcing ClawTeam, which has elevated enterprise multi-agent collaboration from a research project into a teachable, learnable, and deployable engineering practice. The L5 course design in this methodology is deeply informed by its architecture and localized for enterprise adoption in Taiwan and the Chinese-speaking world.

---

## 7. 免責聲明 / Disclaimer

- 本方法論中對 ClawTeam 之任何描述、應用、在地化調整，皆為本方法論作者 (Morris Lu / Tiger AI 虎智科技) 的學習詮釋，**不代表** HKUDS 或 ClawTeam 維護團隊的官方立場。
- 若 ClawTeam 之 API、命令、架構有版本變動，請以 [上游 repo](https://github.com/HKUDS/ClawTeam) 之最新版本為準。
- 本方法論作者保留依 ClawTeam 上游更新而修訂本檔之權利。

- Any description, application, or local adaptation of ClawTeam in this methodology represents the interpretation of the methodology author (Morris Lu / Tiger AI 虎智科技) and does **not** represent the official position of HKUDS or the ClawTeam maintainers.
- If ClawTeam's API, commands, or architecture change in newer versions, refer to the [upstream repository](https://github.com/HKUDS/ClawTeam) for the authoritative current state.
- The methodology author reserves the right to update this document in line with upstream ClawTeam changes.
