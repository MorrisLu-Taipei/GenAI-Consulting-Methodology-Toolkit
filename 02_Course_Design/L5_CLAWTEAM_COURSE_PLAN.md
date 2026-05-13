# L5 ClawTeam 課程規劃 / L5 ClawTeam Course Plan

> 🌐 English version: [L5_CLAWTEAM_COURSE_PLAN_EN.md](L5_CLAWTEAM_COURSE_PLAN_EN.md)

版本 / Version：v1.0
作者 / Author：Morris Lu (盧業興) · Tiger AI 虎智科技

---

## 0. 引用聲明 / Citation Notice

> 本課程以 **ClawTeam** (HKUDS 開源、MIT License) 作為 L5 Agentic Team AI 的主要實作平台。
> 上游 repo：<https://github.com/HKUDS/ClawTeam>
> 引用細節與授權說明詳見：[`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md)
>
> This course uses **ClawTeam** (open-sourced by HKUDS under the MIT License) as the primary implementation platform for L5 Agentic Team AI.
> Upstream repo: <https://github.com/HKUDS/ClawTeam>
> Full citation and license details: [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md)

---

## 1. 課程目標 / Course Objectives

讓企業從 **單一 Agent (L4 Hermes)** 進化為 **多 Agent 自組成團隊 (L5 ClawTeam)**：人類下一個高階目標，Agent Team 自行完成任務拆解、分派、平行執行、整合、與人工 Gate 審核。

Evolve the enterprise from **single Agent (L4 Hermes)** to **multi-Agent self-organizing team (L5 ClawTeam)**: a human issues one high-level goal and the Agent Team autonomously decomposes, delegates, executes in parallel, integrates, and submits to human Gate review.

### 學員能在課後做到 / By the end of this course, learners can

1. 用 `clawteam team spawn-team` 開出一個指定領域的 Agent 團隊。
2. 用 `clawteam task create` 撰寫帶有依賴關係 (`--blocked-by`) 的任務隊列。
3. 用 `clawteam inbox send / broadcast` 在 Agent 之間傳訊。
4. 用 `clawteam board show / live` 監看 Team 進度。
5. 設計 **跨部門 Agent Team 角色卡**、**任務分派表**、**整合報告模板** 與 **Human Gate 設計**。
6. 量化 Agent Team 之 ROI、治理、權限與審核機制。

1. Spawn a domain-specific Agent team using `clawteam team spawn-team`.
2. Author a dependency-aware (`--blocked-by`) task queue using `clawteam task create`.
3. Pass messages between Agents using `clawteam inbox send / broadcast`.
4. Monitor team progress with `clawteam board show / live`.
5. Design **cross-functional Agent Team role cards**, **task allocation tables**, **integration report templates**, and **Human Gate designs**.
6. Quantify the Agent Team's ROI, governance, permissions, and review mechanisms.

---

## 2. 適合對象 / Audience

- 管理層 (CEO / COO / CTO) / Executives
- 跨部門主管 / Cross-functional managers
- PM / 專案管理 / Project managers
- IT / AI Center / Platform team
- 具備 L4 基礎的種子團隊 / L4-graduated seed team

## 3. 課前需求 / Prerequisites

| 項目 / Item | 說明 / Description |
| --- | --- |
| **L4 通過** / L4 graduated | 至少 1 個 Hermes Agent 已通過 Gate 4A-4E / At least one Hermes Agent has passed Gates 4A-4E |
| **環境** / Environment | Python 3.10+、`tmux`、`git`、任一 CLI agent (Claude Code / Codex / Gemini) / Python 3.10+, `tmux`, `git`, any CLI agent |
| **跨部門任務** / Cross-functional task | 新產品上市 / 品質改善 / 客戶經營 / 病患服務改善 / 年度營運規劃 / New-product launch / quality improvement / customer engagement / patient service / annual operations planning |
| **資料源** / Data sources | CRM、ERP、Sheets、Notion、API 至少 2 種 / At least two of CRM, ERP, Sheets, Notion, API |
| **人工 Gate** / Human Gate | 管理層或專案 Owner 已被指定為 Reviewer / Executive or project owner designated as Reviewer |

---

## 4. ClawTeam 架構導讀 / ClawTeam Architecture Primer

> 完整架構說明請見 [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md) §2。
> See [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md) §2 for the full architecture overview.

| 層次 / Layer | 對應 L5 課程主題 / Maps to L5 Topic |
| --- | --- |
| **Team Management** | §6.2 Agent Team 設計 / Team design |
| **Workspace Isolation (git worktree)** | §6.3 Workspace 隔離與衝突管理 / Isolation & conflict management |
| **Task Tracking (Kanban + dependencies)** | §6.4 任務分派與依賴 / Task allocation & dependencies |
| **Inter-Agent Messaging (inbox + broadcast)** | §6.5 Agent 間溝通設計 / Inter-Agent communication |
| **Transport (File / P2P / Redis roadmap)** | §6.7 部署模式：單機 vs 跨機 / Single-machine vs cross-machine deployment |

### 三個原始範例情境 → 在地化對應 / Three reference scenarios → localized mapping

| ClawTeam 原始情境 / Upstream scenario | 在地化 L5 情境 / Localized L5 scenario |
| --- | --- |
| AutoResearch (8 Agents, H100) — ML 自主超參數實驗 | **製造業：品質改善 Agent Team** — 多 Agent 平行探索不良率根因、製程參數、SPC 規則 / **Manufacturing: Quality Improvement Team** — parallel exploration of defect-rate root causes, process parameters, SPC rules |
| Software Engineering (5 Agents) — Architect / Backend / Frontend / QA | **零售：新產品上市 Agent Team** — 產品設計、定價、文案、通路、Launch QA / **Retail: New-Product Launch Team** — design, pricing, copy, channels, launch QA |
| Hedge Fund (7 Agents) — Portfolio Manager + 5 Analysts + Risk Manager | **醫院：病患服務改善 Agent Team** — 醫務行政、病歷、客服、品保、整合 / **Hospital: Patient Service Improvement Team** — admin, records, customer service, QA, integration |

---

## 5. 課堂內容 / Course Modules

總時數 / Total duration：**8-12 小時 (1.5 天)** / **8-12 hours (1.5 days)**

| # | 單元 / Module | 時間 / Time | 內容 / Content | 方法 / Method |
| ---: | --- | ---: | --- | --- |
| 1 | **L4 → L5 邊界 / The L4→L5 boundary** | 30 分 | 單 Agent 與 Agent Team 差異；何時該升級 / Single-Agent vs Agent-Team; when to upgrade | 講授 / Lecture |
| 2 | **Multi-Agent 觀念 / Multi-Agent concepts** | 45 分 | Solo 🤖 → Swarm 🦞🤖🤖🤖、ClawTeam 三大範例 / Solo→Swarm, ClawTeam's three reference cases | 講授 / Lecture |
| 3 | **ClawTeam 架構導讀 / Architecture primer** | 45 分 | Team / Workspace / Task / Inbox / Transport 五層 / The five layers | 講授 + 投影 / Lecture + slides |
| 4 | **環境安裝與 Profile / Install & profile** | 45 分 | `pip install clawteam`、`clawteam profile wizard / test / doctor` / Install, configure profiles | 上機 / Hands-on |
| 5 | **Team 與 Workspace / Team & workspace** | 60 分 | `team spawn-team`、git worktree 自動配置、`team snapshot/restore` / Team creation, git worktree auto-setup, snapshot/restore | 上機 / Hands-on |
| 6 | **Task 設計 (角色卡 + IPOE) / Task design (role card + IPOE)** | 90 分 | Agent 角色卡、Input/Process/Output/Evidence、依賴鏈 / Role cards, IPOE, dependency chains | 工作坊 / Workshop |
| 7 | **Task CLI 實作 / Task CLI hands-on** | 75 分 | `task create --blocked-by`、`task update`、`task list`、`task wait` / Author dependency-aware tasks | 上機 / Hands-on |
| 8 | **Inbox 與 Broadcast / Inbox & broadcast** | 60 分 | 點對點 vs 廣播、訊號匯合模式 (參考 Hedge Fund Risk Manager) / P2P vs broadcast, signal convergence patterns | 上機 / Hands-on |
| 9 | **Board 監看與 gource 視覺化 / Board & gource** | 45 分 | `board show / live / attach / gource / serve` / Dashboards and visualization | 上機 / Hands-on |
| 10 | **整合 Agent 與 Reviewer / Integration Agent & Reviewer** | 60 分 | 衝突偵測 (`context conflicts`)、整合報告、Reviewer 角色 / Conflict detection, integration reports, Reviewer role | 工作坊 / Workshop |
| 11 | **治理、權限、Human Gate / Governance, permissions, Human Gate** | 60 分 | Stage Gate 5、Reviewer 流程、權限模型 (v0.6 roadmap) / Stage Gate 5, Reviewer flow, permission model (v0.6) | 講授 / Lecture |
| 12 | **Team 演練 / Team simulation** | 150 分 | 完成 1 個 Agent Team 案例 (製造業 / 醫院 / 零售) / Complete one Agent Team case (manufacturing / hospital / retail) | 實作 / Exercise |
| 13 | **ROI、總結、進階 (v0.4-v1.0) / ROI, recap, advanced** | 60 分 | KPI 設計、Redis transport、Web UI roadmap / KPI design, Redis transport, Web UI roadmap | 講授 / Lecture |

---

## 6. 重點工作坊 / Key Workshops

### 6.2 Agent Team 設計工作坊 / Agent Team Design Workshop

每個 Team 必須完成 Agent 角色卡：
Each team must complete an Agent role card:

| 欄位 / Field | 範例：製造業品質改善 / Example: Manufacturing QA |
| --- | --- |
| **Team 任務** / Team mission | 月度不良率降低 1% / Reduce monthly defect rate by 1% |
| **Agent 角色** / Agent roles | RootCauseAgent、ParameterAgent、SPCAgent、ReportAgent、ReviewerAgent |
| **Input** | MES / SPC / QC 報表、生產日誌、客訴 / MES / SPC / QC reports, production logs, complaints |
| **Process** | 拆解 → 平行探索 → 訊號匯合 → 整合報告 / Decompose → parallel exploration → signal convergence → integration |
| **Output** | 不良率根因報告 + 製程參數建議 + SPC 規則更新 / Root-cause report, process-parameter recommendations, SPC rule updates |
| **Reviewer** | 製造處長 + QA 主管 / Manufacturing director + QA manager |
| **Human Gate** | 報告→ 製造處長簽核 → 試產驗證 → 量產 / Report → director sign-off → pilot run → mass production |
| **KPI** | 不良率、再現性、回收損耗、客訴下降 / Defect rate, repeatability, recovery loss, complaint reduction |

### 6.3 Workspace 隔離與衝突管理 / Workspace Isolation & Conflict Management

ClawTeam 透過 **git worktree** 讓每個 Agent 在獨立分支工作，避免互相覆蓋。學員必須學會：

ClawTeam uses **git worktree** to give every Agent its own branch — no overwrites. Learners must master:

- `git worktree list` 觀察各 Agent 分支 / Inspect each Agent's branch
- `clawteam context conflicts` 偵測衝突 / Detect conflicts
- `clawteam context inject` 將整合資訊注入 Agent 上下文 / Inject integrated context into Agents
- 合併策略：誰可以合併？誰先合併？/ Merge strategy: who merges, in what order?

### 6.4 任務分派與依賴 / Task Allocation & Dependencies

學員撰寫真實 task 鏈：
Learners write a real task chain:

```bash
# Manufacturing QA team example
clawteam task create my-team --owner RootCauseAgent --title "Identify top-3 defect modes" --id T1
clawteam task create my-team --owner ParameterAgent --title "Map defect modes to process params" --blocked-by T1 --id T2
clawteam task create my-team --owner SPCAgent --title "Propose SPC control limits" --blocked-by T2 --id T3
clawteam task create my-team --owner ReportAgent --title "Integrate findings" --blocked-by T1,T2,T3 --id T4
clawteam task wait my-team
```

### 6.5 Agent 間溝通設計 / Inter-Agent Communication

兩種模式 / Two patterns：

| 模式 / Pattern | 命令 / Command | 適用 / When to use |
| --- | --- | --- |
| **點對點 / Point-to-point** | `clawteam inbox send <team> <agent> "message"` | 直接交付資料 / Direct data handoff |
| **廣播 / Broadcast** | `clawteam inbox broadcast <team> "message"` | 全 Team 同步狀態、通知 Gate / Team-wide status, Gate notifications |
| **訊號匯合 / Signal convergence** | 多個 Analyst Agent → Risk Manager Agent (參考 Hedge Fund 案例) / Multiple Analyst Agents → Risk Manager Agent (Hedge Fund pattern) | 多源訊號統一決策 / Multi-source signals → consolidated decision |

### 6.7 單機 vs 跨機部署 / Single-Machine vs Cross-Machine Deployment

| 場景 / Scenario | Transport | 適用企業階段 / Enterprise stage |
| --- | --- | --- |
| **PoC / 小型部門** / PoC / small department | File-based (預設 / default) | L5 起步 / L5 starter |
| **跨工廠 / 跨院區** / Cross-plant / cross-site | P2P (ZeroMQ) | 中型企業 / Medium enterprise |
| **總部跨地區** / HQ multi-region | Redis (v0.4 roadmap) | 集團 / Enterprise group |
| **完整 Web UI** / Full Web UI | v1.0 roadmap | 集中監控 AI Team / Centralized AI Team monitoring |

---

## 7. 課後作業 / Post-Course Assignments

1. 完成 1 個 **Agent Team 角色卡**（至少 5 個 Agent 角色）/ Complete one Agent Team role card (≥ 5 Agent roles)
2. 完成 1 份 **任務分派表 + 依賴鏈** / One task allocation table with dependency chains
3. 完成 1 份 **IPOE 表** / One IPOE table
4. 完成 1 份 **整合報告模板** / One integration report template
5. 設計 1 個 **Reviewer / Human Gate 流程** / One Reviewer / Human Gate flow
6. 提出 1 份 **ROI 追蹤表** / One ROI tracking table
7. 在 sandbox 中跑 1 次完整的 `clawteam` 流程，提交 `board show` 截圖 + `task list` 輸出 / Run one full `clawteam` flow in a sandbox; submit `board show` screenshot + `task list` output

---

## 8. 完成標準 / Completion Criteria

| 標準 / Criterion | 驗證方式 / Verification |
| --- | --- |
| Agent 角色清楚 / Clear Agent roles | 角色卡 / Role card |
| 任務可分派 / Tasks are dispatchable | `task list` 輸出 + 依賴鏈 / `task list` output + dependency chain |
| 各 Agent Input/Output 清楚 / Clear I/O per Agent | IPOE 表 / IPOE table |
| 有整合與審核機制 / Has integration & review | 整合報告 + Reviewer 設計 / Integration report + Reviewer design |
| 有 ROI 指標 / Has ROI metrics | KPI 表 / KPI table |
| 已實際跑過 ClawTeam / Actually ran ClawTeam | board / task / inbox 操作截圖 / Screenshots of board / task / inbox ops |

---

## 9. L5 Deliverables

- ClawTeam 角色卡 / ClawTeam role card
- 多 Agent 任務分派表 (含依賴鏈) / Multi-Agent task allocation table (with dependency chains)
- Agent Team IPOE 表 / Agent Team IPOE table
- 整合報告模板 / Integration report template
- Reviewer / Human Gate 設計 / Reviewer / Human Gate design
- ROI 追蹤表 / ROI tracking table
- Sandbox 演練紀錄：`board show` + `task list` + `inbox` 截圖 / Sandbox dry-run records: `board show` + `task list` + `inbox` screenshots
- ClawTeam profile + team config (`~/.clawteam/`) 備份 / ClawTeam profile + team config backup

---

## 10. Gate 5：L5 完成標準 / Stage Gate 5

通過條件 / Pass criteria：

- 至少完成 1 個 Agent Team 情境設計（製造業 / 醫院 / 零售三選一）/ Complete ≥ 1 Agent Team scenario design (manufacturing / hospital / retail)
- 每個 Agent 有角色、Input、Output、限制 / Every Agent has role, Input, Output, constraints
- 有整合 Agent 或整合流程 / Has an integration Agent or integration flow
- 有 Reviewer / Human Gate / Has Reviewer / Human Gate
- 有 ROI 與治理設計 / Has ROI and governance design
- 已在 sandbox 中跑通 1 次完整的 `clawteam` 流程 / Successfully ran one full `clawteam` flow in a sandbox

---

## 11. 引用與授權 / Citation & License

本課程在地化引用 ClawTeam 之架構、CLI 與設計理念，**未重製、未 fork** 原始碼。學員與企業若於課堂衍生作品中再散布 ClawTeam 程式碼，必須遵守 **MIT License** 並保留原始著作權聲明。完整引用條款請見：

This course localizes citations of ClawTeam's architecture, CLI, and design principles. The upstream **source code is not reproduced or forked**. If learners or enterprises redistribute ClawTeam source in derivative works, they must comply with the **MIT License** and preserve the original copyright notice. Full citation terms:

📄 [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md)

**上游專案 / Upstream project**: HKUDS, *ClawTeam*, MIT License, <https://github.com/HKUDS/ClawTeam>
