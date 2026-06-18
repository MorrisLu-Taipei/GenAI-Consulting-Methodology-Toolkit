# L5 ClawTeam 課程規劃 / L5 ClawTeam Course Plan

> 🌐 English version: [L5_CLAWTEAM_COURSE_PLAN_EN.md](L5_CLAWTEAM_COURSE_PLAN_EN.md)

版本 / Version：v1.0
作者 / Author：Morris Lu (盧業興) · Tiger AI 虎智科技

---

## 0. 引用聲明 / Citation Notice

> 本課程以 **ClawTeam** (HKUDS 開源、MIT License) 作為 L5 Multi-Agent Organization 的主要實作平台。
> 上游 repo：<https://github.com/HKUDS/ClawTeam>
> 引用細節與授權說明詳見：[`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md)
>
> This course uses **ClawTeam** (open-sourced by HKUDS under the MIT License) as the primary implementation platform for L5 Multi-Agent Organization.
> Upstream repo: <https://github.com/HKUDS/ClawTeam>
> Full citation and license details: [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md)

---

## 1. 課程目標 / Course Objectives

讓企業從 **單一 Agent (L4 Hermes)** 進化為 **多 Agent 自組成團隊 (L5 ClawTeam)**：人類下一個高階目標，Agent Team 自行完成任務拆解、分派、平行執行、整合、與人工 Gate 審核。

Evolve the enterprise from **single Agent (L4 Hermes)** to **multi-Agent self-organizing team (L5 ClawTeam)**: a human issues one high-level goal and the Agent Team autonomously decomposes, delegates, executes in parallel, integrates, and submits to human Gate review.

### Bloom 格式主 LO / Bloom-format primary LOs

> 本節以 [`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](ONLINE_COURSE_DESIGN_METHODOLOGY.md) §4 的 Bloom 公式撰寫：**[動詞] + [內容] + [情境]**，可驗收、可量測。
>
> Written per the Bloom formula in [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) §4: **[Verb] + [Content] + [Context]** — assessable and measurable.

#### 給 CLP 用的 4 條主 LO / 4 primary LOs for the CLP

完成本課程後，學員能夠：By the end of this course, learners can:

1. **建構** 一個指定領域的 Agent 團隊（用 `clawteam team spawn-team` 開團 + `task create --blocked-by` 撰寫依賴任務鏈），**完成** 1 個可平行執行的 5-Agent 任務佇列端到端 dry-run。
   **Build** a domain-specific Agent team (`clawteam team spawn-team` + dependency-aware `task create --blocked-by`), **completing** an end-to-end dry-run of a parallel-executable 5-Agent task queue. (Apply)

2. **設計** 跨部門 Agent Team 的 4 件核心構件：角色卡（≥ 5 Agent）、任務分派表、整合報告模板、Human Gate 設計，**產出** 至少 1 個產業情境（製造 / 零售 / 醫療擇一）的完整套件。
   **Design** the 4 core artifacts of a cross-functional Agent Team: role cards (≥ 5 Agents), task allocation table, integration report template, Human Gate design; **producing** one complete set for an industry scenario (manufacturing / retail / healthcare). (Create)

3. **使用** `clawteam inbox` + `board` 監看與協調 Team 進度，**辨識** workspace context 衝突 + 整合死鎖 + Agent 失誤三大失敗模式，**設計** 對應的偵測與恢復流程。
   **Use** `clawteam inbox` + `board` to monitor and coordinate team progress; **identify** the 3 failure modes (workspace context conflicts / integration deadlocks / Agent errors); **design** corresponding detection and recovery flows. (Analyze)

4. **評估** 公司候選任務的 L5 適配度，**量化** Agent Team 之 ROI / 治理 / 權限 / 審核成本，**判斷** 何時該升級到 L5、何時該留在 L4；**產出** L5 投資決策書。
   **Evaluate** the L5 fit of company candidate tasks, **quantifying** the Agent Team's ROI / governance / permissions / review cost; **judging** when to upgrade to L5 vs stay at L4; **producing** an L5 investment decision document. (Evaluate)

### 互動學習設計 / Interactive Learning Design

> 對照 [`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](ONLINE_COURSE_DESIGN_METHODOLOGY.md) §5.1 + §7 + §9.4。

**Engagement activity（開頭 10 分鐘內必須有 / required in first 10 min）：**

> **每人寫下 1 句話「我想交給 Agent Team 做的任務」**，全班投票哪個最值得 Team 協作。10 分鐘把 L5 從抽象變具體。
>
> **Each learner writes one sentence: "the task I'd assign to an Agent Team"**; class votes which is most worth team collaboration. 10 min, makes L5 concrete.

**Formative gates（章節結尾的快速自我檢核）：**

| 章節 / Module | Formative 檢核 / Check | 時長 / Duration |
|---|---|---|
| Module 1 (L4→L5 boundary) | 學員判斷 §3.3 寫的任務該 L4 還 L5 / classify own tasks L4 vs L5 | 10 min |
| Module 3 (Task design workshop) | 每人完成 1 頁 5-Agent role card draft / 1-page 5-Agent role card draft | 30 min |
| Module 5 (Team & workspace) | 同儕互審 worktree 隔離設定 / peer review of worktree isolation | 15 min |
| Module 6 (Integration & Gate) | 同儕互審整合報告 / peer review of integration report | 20 min |

**Summative gate（全課程結尾）：對應 Gate 5（見 §10）→ 7 個 post-course assignments（§7）+ 1 個 L5 投資決策書。**

### Reference materials 清單 / Reference Materials List

| 類型 / Type | 位置 / Location | 用途 / Use | 狀態 / Status |
|---|---|---|---|
| Agent 角色卡 1 頁範本 | 下方 §1.x（已加） | Module 3 課堂作業 | ☑ 已加 / Added |
| 任務分派表範本 | 下方 §1.x（已加） | Module 4 課堂作業 | ☑ 已加 / Added |
| 整合報告範本 | 下方 §1.x（已加） | Module 6 課堂作業 | ☑ 已加 / Added |
| Human Gate 設計範本 | 下方 §1.x（已加） | Module 6 課堂作業 | ☑ 已加 / Added |
| ClawTeam CLI 速查卡 | 待補 | spawn-team / task / inbox / board 一頁 cheat sheet | ☐ 待補 / TBD |

### Agent 角色卡範本（高優先補強）/ Agent Role Card Template

```markdown
# Team: [Team Mission, 1 sentence]
# Date: [YYYY-MM-DD] | Version: [v0.1]

## Agents (≥ 5)
| # | Role | Mission | Primary Skill(s) | Input source |
|---|---|---|---|---|
| 1 | PM Agent | task decomposition + scheduling | L2.task_decompose, L3.schedule_workflow | Inbox |
| 2 | Research Agent | gather domain data | L2.web_research, L3.crawl_workflow | URLs + DB |
| 3 | Analysis Agent | structure & analyze | L2.data_analysis, L4.knowledge_query | Research output |
| 4 | Writer Agent | produce deliverable | L2.draft, L4.style_consistency_check | Analysis output |
| 5 | Reviewer Agent | QC + escalation | L2.quality_check, escalate_to_human | Writer output |

## I/O Summary
- Team input: [high-level goal from human]
- Team output: [deliverable, e.g., 5-page report]

## Reviewer & escalation
- Internal: Reviewer Agent (auto)
- Human Gate: [role / SLA / criteria]

## KPI (3-5 metrics)
- Cycle time: target ≤ X hours
- Output quality (peer score): ≥ Y/10
- Human revision rate: ≤ Z%

## Risk register (top 3)
1. [Risk] → [Mitigation]
2. ...

## Success criteria
- [ ] All Agents complete tasks without deadlock
- [ ] Output passes Reviewer Agent QC
- [ ] Human Gate approval
- [ ] KPI met
```

### 整合報告範本 / Integration Report Template

```markdown
# [Team Name] Integration Report — [YYYY-MM-DD]

## Executive summary (1 paragraph)
[What the team delivered, headline KPI]

## Agent contributions
| Agent | Tasks completed | Output | Time spent |
|---|---|---|---|
| ... | ... | ... | ... |

## Conflicts detected & resolved
| # | Conflict | Resolution |
|---|---|---|
| 1 | ... | ... |

## KPI status
| Metric | Target | Actual | Status |
|---|---|---|---|
| ... | ... | ... | ✅ / ⚠️ / ❌ |

## Next steps
- ...

## Sign-off
- Team lead Agent: ___ Date: ___
- Human reviewer: ___ Date: ___
```

### ClawTeam CLI 速查卡 / Quick-Reference Card

> 1 頁總覽常用 ClawTeam CLI 指令；課中與課後 hands-on 必備。/ One-page summary of common ClawTeam CLI commands; required for in-class and post-course hands-on.

#### Team lifecycle / 團隊生命週期

| 指令 / Command | 用途 / Purpose | 範例 / Example |
| --- | --- | --- |
| `clawteam team spawn-team` | 建立新 Agent 團隊 / spawn a new Agent team | `clawteam team spawn-team --name marketing-team --agents 5 --domain marketing` |
| `clawteam team list` | 列出現有團隊 / list existing teams | `clawteam team list` |
| `clawteam team snapshot` | 凍結團隊當前狀態 / freeze current team state | `clawteam team snapshot --name pre-gate-review` |
| `clawteam team restore` | 還原團隊到先前 snapshot / restore team to prior snapshot | `clawteam team restore --snapshot pre-gate-review` |
| `clawteam team destroy` | 解散團隊 / dismantle team | `clawteam team destroy --name marketing-team --confirm` |

#### Task management / 任務管理

| 指令 / Command | 用途 / Purpose | 範例 / Example |
| --- | --- | --- |
| `clawteam task create` | 建立任務 / create a task | `clawteam task create --title "Draft Q2 plan" --assign-to PMAgent` |
| `clawteam task create --blocked-by` | 建立有依賴的任務 / create a dependency-aware task | `clawteam task create --title "Write copy" --blocked-by 12,13` |
| `clawteam task list` | 列出任務 / list tasks | `clawteam task list --status pending` |
| `clawteam task update` | 更新任務狀態 / update task status | `clawteam task update 14 --status in-progress` |
| `clawteam task close` | 關閉任務 / close task | `clawteam task close 14 --output report-q2.md` |

#### Inter-Agent messaging / Agent 間溝通

| 指令 / Command | 用途 / Purpose | 範例 / Example |
| --- | --- | --- |
| `clawteam inbox send` | 點對點傳訊 / send P2P message | `clawteam inbox send --from PMAgent --to ResearchAgent --msg "Need TAM by EOD"` |
| `clawteam inbox broadcast` | 對整團隊廣播 / broadcast to whole team | `clawteam inbox broadcast --from PMAgent --msg "Standup at 10am"` |
| `clawteam inbox read` | 讀取某 Agent 收件匣 / read an Agent's inbox | `clawteam inbox read --agent ResearchAgent` |
| `clawteam inbox clear` | 清空收件匣 / clear inbox | `clawteam inbox clear --agent ResearchAgent --confirm` |

#### Monitoring / 監看

| 指令 / Command | 用途 / Purpose | 範例 / Example |
| --- | --- | --- |
| `clawteam board show` | 顯示團隊看板 / show team board | `clawteam board show --team marketing-team` |
| `clawteam board live` | 即時更新看板 / live-updating board | `clawteam board live --team marketing-team` |
| `clawteam log tail` | 追看 Agent log / tail Agent log | `clawteam log tail --agent PMAgent --follow` |

#### Workspace & context / 工作空間與上下文

| 指令 / Command | 用途 / Purpose | 範例 / Example |
| --- | --- | --- |
| `git worktree list` | 列出每個 Agent 的隔離 worktree / list per-Agent isolated worktrees | `git worktree list` |
| `clawteam context conflicts` | 偵測 Agent 間 context 衝突 / detect inter-Agent context conflicts | `clawteam context conflicts --team marketing-team` |
| `clawteam context inject` | 把整合後 context 注回 / inject integrated context back | `clawteam context inject --from integration-report.md` |

#### Human Gate / 人工審核

| 指令 / Command | 用途 / Purpose | 範例 / Example |
| --- | --- | --- |
| `clawteam gate request` | 觸發人工 Gate 請求 / trigger human Gate request | `clawteam gate request --task 14 --reviewer morris@tigerai.tw` |
| `clawteam gate approve` | 通過 Gate / approve gate | `clawteam gate approve --task 14 --reviewer morris@tigerai.tw` |
| `clawteam gate reject` | 拒絕 Gate / reject gate | `clawteam gate reject --task 14 --reviewer morris@tigerai.tw --reason "..."` |

#### 課中最常用組合 / Most-used in-class command combos

```bash
# 1. 開團 + 建任務鏈 / spawn team + create dependent task chain
clawteam team spawn-team --name demo-team --agents 5 --domain consulting
clawteam task create --title "Research" --assign-to ResearchAgent
clawteam task create --title "Analyze" --blocked-by 1 --assign-to AnalysisAgent
clawteam task create --title "Draft" --blocked-by 2 --assign-to WriterAgent

# 2. 監看進度 / monitor progress
clawteam board live --team demo-team

# 3. 完成後查整合 / post-completion integration check
clawteam context conflicts --team demo-team
clawteam team snapshot --name demo-completed
```

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

## 4.5 L5 三件套：平台 + 透鏡 + 實例 / The L5 Triad

> 新增（v1.1）：L5 不只教「平台」。完整的 L5 教學由三個互補件組成。
> Added (v1.1): L5 is not only about the platform. Complete L5 teaching rests on three complementary pieces.

| 角色 / Role | 是什麼 / What | 教什麼 / Teaches | 檔案 / File |
| --- | --- | --- | --- |
| **平台 / Platform** | ClawTeam（本課主體）| 機制：spawn / task / inbox / board / gate | 本檔 / This plan |
| **透鏡 / Lens** | Harness Engineering 六層 | 概念：為什麼 Agent Team 能可靠交付 | [`90_References/HARNESS_ENGINEERING_REFERENCE.md`](../90_References/HARNESS_ENGINEERING_REFERENCE.md) |
| **實例 / Worked case** | `ai-news-channel` | 示範：六層 + 治理長什麼樣 | [`ai-news-channel/TIGERAI_L5_CASE_NOTES.md`](ai-news-channel/TIGERAI_L5_CASE_NOTES.md) |

### Harness Engineering 六層（L5 概念骨架）/ The Six Harness Layers

「先設計系統，再挑模型。」六層是判斷一個 Agent Team 成不成熟的檢核軸：

| Harness 層 | 一句話 / One-line | 在 `ai-news-channel` 打開哪個檔 |
| --- | --- | --- |
| **Loop** | 固定順序、不跳步 | `CLAUDE.md` The Fixed Loop |
| **Tools** | 每個 Agent 只拿該拿的權限 | `.claude/agents/*.md` 的 `tools:` |
| **Context** | 全員先讀同一份憲法 | `CLAUDE.md` + `constitution/` |
| **Persistence** | 產出與決策永久落地 | `knowledge-base/` |
| **Verification** | 上線前機器 + 人雙檢核 | `supervisor.md` + `verify_build.sh` |
| **Constraints** | 角色能 / 不能白紙黑字 | `constitution/ai-member-boundaries.md` |

> 建議動線：**Harness 六層（透鏡）給心智模型 → 打開 `ai-news-channel`（實例）逐層對照 → 用 ClawTeam（平台）動手把自己的 Team 跑起來。** ClawTeam 的五層架構（§4）是 Harness 六層在 CLI 平台上的一種具體實作；HITL / Stage Gate 5 則是 Verification + Constraints 兩層在顧問場景的落地。
>
> 完整對應與來源文獻見 [`HARNESS_ENGINEERING_REFERENCE.md`](../90_References/HARNESS_ENGINEERING_REFERENCE.md)。

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

## 6.99 Lecture Map（依 [`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](ONLINE_COURSE_DESIGN_METHODOLOGY.md) §5.3 切細）

### 6.99.1 §6 完整 Lecture Map / Complete Lecture Map

> L5 是 ~8 小時 hands-on workshop，分 AM (Concept) + PM (Hands-on) 兩個半日。約 100 lectures × 平均 4.8 min = 480 min / 8 hr。
> L5 is a ~8-hour hands-on workshop, split into AM (Concept) + PM (Hands-on). ~100 lectures × avg 4.8 min = 480 min / 8 hr.
>
> 講座類型代碼 / Lecture type codes：**TH** / **S** / **SL** / **VS** / **PR** / **EN** / **RC**（同 L1 / Same as L1）。

#### AM1 — Introduction + L4→L5 Boundary（90 min）

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 0.1 | 歡迎來到 L5 ClawTeam / Welcome | TH | 4 | 講師 + 為什麼 Multi-Agent Team 是組織級槓桿 / Instructor + why Multi-Agent Team is org-level leverage |
| 0.2 | 你會學到什麼 / What you'll learn | TH+SL | 3 | 4 條主 LO / 4 primary LOs |
| 0.3 | **Engagement：寫一句最想交給 Agent Team 的任務** / Engagement: write the task you'd assign | EN+PR | 8 | 全班投票 / Class vote |
| 1.1 | L4 單 Agent 的極限 / Single-Agent L4 limits | SL | 5 | 為什麼一個 Agent 不夠 / Why one Agent isn't enough |
| 1.2 | Multi-Agent 的價值 / Multi-Agent value | SL | 5 | 平行 + 專業分工 / Parallelism + specialization |
| 1.3 | L5 不是 L4 加減版 / L5 is not L4 plus | SL | 5 | 範式轉移 / Paradigm shift |
| 1.4 | 何時該升 L5 / When to upgrade to L5 | SL | 5 | 6 個觸發條件 / 6 triggers |
| 1.5 | 何時 L5 過頭 / When L5 is overkill | TH | 5 | 失敗案例 / Failure cases |
| 1.6 | 章節 recap | RC | 5 | L4→L5 升級檢核 / L4→L5 upgrade checklist |
| 1.7 | **Formative：分類自己的任務 L4 vs L5** / Classify own tasks | PR | 10 | 用 §3.3 寫的任務試 / Use §3.3 tasks |
| 1.8 | break | — | 10 | — |
| 1.9 | 章節 buffer / wrap | RC | 5 | 進入 AM2 過渡 / Transition to AM2 |

#### AM2 — ClawTeam Architecture（90 min）

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 2.1 | 5 層架構總覽 / 5-layer overview | SL+VS | 5 | Team / Workspace / Task / Inbox / Transport |
| 2.2 | Team Management | S | 5 | spawn-team 概念 / spawn-team concept |
| 2.3 | Workspace Isolation (git worktree) | S | 5 | 為什麼用 worktree / Why worktree |
| 2.4 | Task Tracking + Dependencies | S | 5 | Kanban + blocked-by |
| 2.5 | Inter-Agent Messaging | S | 5 | inbox + broadcast |
| 2.6 | Transport: File / P2P / Redis | SL | 5 | 部署模式 3 階段 / 3 deployment stages |
| 2.7 | CLI 速查卡 walkthrough / CLI quick-ref walkthrough | S | 8 | §1.x 速查卡逐區介紹 / §1.x card section-by-section |
| 2.8 | Hedge Fund 案例導讀 / Hedge Fund pattern intro | SL | 6 | 訊號匯合範例 / Signal convergence example |
| 2.9 | 章節 recap | RC | 6 | 5 層 + 5 CLI 動作 / 5 layers + 5 CLI commands |
| 2.10 | break | — | 10 | — |
| 2.11 | **Formative：手動畫 5 層架構** / Sketch the 5 layers | PR | 5 | 紙筆 / Pen & paper |
| 2.12 | wrap | RC | 5 | 進入 PM1 過渡 / Transition to PM1 |

#### PM1 — Task Design Workshop + Agent Role Card（120 min）

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 3.1 | Agent 角色卡 1 頁範本 / Role card template | SL | 5 | 7 欄完整 / 7 fields |
| 3.2 | 範例角色卡 demo：製造業 / Example: manufacturing | S | 8 | 5 Agent 完整跑一次 / Full 5-Agent walkthrough |
| 3.3 | 任務分派表設計 / Task allocation design | S | 5 | blocked-by 鏈條 / blocked-by chain |
| 3.4 | 整合報告範本 / Integration report template | S | 5 | exec summary + contributions + conflicts |
| 3.5 | Human Gate 設計 / Human Gate design | S | 5 | 觸發 + reviewer + SLA |
| 3.6 | **Workshop Part 1：solo draft 角色卡** / Workshop Part 1: solo role card draft | PR | 15 | 學員用自己情境 / Learner's own scenario |
| 3.7 | **Workshop Part 2：pair review + feedback** | PR | 30 | 同儕互審 / Peer review |
| 3.8 | break | — | 10 | — |
| 3.9 | **Workshop Part 3：revision + team feedback** | PR | 25 | 修正 + 多人 review / Revise + multi-person review |
| 3.10 | **Workshop Part 4：gallery walk** | PR | 12 | 全班互看 + 投票最佳 / Class walkthrough + vote |

#### PM2 — Hands-on：spawn / task / board / inbox / Gate（120 min）

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 4.1 | 環境準備 / Environment prep | S | 5 | tmux / git / CLI agent ready |
| 4.2 | `clawteam team spawn-team` 實操 / hands-on | S | 8 | 跑一次 / Run once |
| 4.3 | 學員自己 spawn / Learner self-spawn | PR | 10 | 用 §3 角色卡 / Use §3 role card |
| 4.4 | `clawteam task create --blocked-by` | S | 8 | 建依賴鏈 / Build dependency chain |
| 4.5 | 學員自己建 task chain | PR | 10 | — |
| 4.6 | `clawteam board live` 監看 / monitor | S | 5 | 即時看 / Watch live |
| 4.7 | `clawteam inbox send / broadcast` 溝通 / messaging | S | 5 | Agent 間訊息 / Agent messaging |
| 4.8 | 學員實作 inbox 互動 / hands-on inbox | PR | 10 | — |
| 4.9 | `git worktree list` + `context conflicts` 偵測 / detect | S | 8 | 隔離 + 衝突 / Isolation + conflict |
| 4.10 | break | — | 10 | — |
| 4.11 | `context inject` 整合 / integrate | S | 6 | 把整合 context 注回 / Inject back |
| 4.12 | Human Gate 流程：request / approve / reject | S | 8 | 一條完整 Gate 流程 / Full gate flow |
| 4.13 | 學員實作 Human Gate / hands-on | PR | 10 | — |
| 4.14 | `team snapshot` + `restore` / snapshot & restore | S | 5 | 凍結與還原 / Freeze & restore |
| 4.15 | wrap | RC | 12 | 完整流程跑一次 / Full flow once |

#### Conclusion（30 min）

| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 5.1 | Demo Day：每組 5 分鐘展示 / 5-min team demo × N | PR | 20 | 學員展示 / Learner demo |
| 5.2 | ROI 計算範例 / ROI calculation example | SL | 5 | Agent Team 划算嗎 / Worth it? |
| 5.3 | Gate 5 完成標準回顧 / Gate 5 recap | SL | 3 | 8 個 evidence / 8 evidence items |
| 5.4 | 恭喜 + 結語 / Congratulations + closing | TH | 2 | 結束 / End |

### 6.99.2 Lecture-type mix / 講座類型比例

| Type | Count | Time share |
| --- | --- | --- |
| TH | 7 | ~ 6% |
| S | 27 | ~ 32% |
| SL | 21 | ~ 22% |
| PR / EN | 15 | ~ 31% |
| RC | 8 | ~ 9% |

> L5 是 hands-on workshop，PR 比例 ~ 31% 遠高於 L1（17%）—— 預期。L5 學員必須**動手做**才能掌握。/ L5 is a hands-on workshop; PR share ~31% is much higher than L1 (17%) — by design. L5 learners must **do** to master.

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
