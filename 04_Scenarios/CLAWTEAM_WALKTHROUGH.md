# L5 ClawTeam 實作 Walkthrough / L5 ClawTeam Hands-On Walkthrough

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>
>
> 本檔示範以 **ClawTeam** (HKUDS, MIT License) 跑通一個跨部門 Agent Team 的完整流程。
> 引用與授權詳見 [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md)。
> ClawTeam 上游：<https://github.com/HKUDS/ClawTeam>
>
> This document walks through running a complete cross-functional Agent Team with **ClawTeam** (HKUDS, MIT License). Citation & license: see [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md).

---

## 0. 這個 Walkthrough 的情境 / Scenario for This Walkthrough

採用 L5 課程之**製造業品質改善 Agent Team**（對應 ClawTeam 原始 AutoResearch 範例的在地化版本）。

| 項目 | 內容 |
| --- | --- |
| Team 任務 | 月度不良率降低 1%（從 3.2% → 2.2%） |
| Agent 角色 | RootCauseAgent、ParameterAgent、SPCAgent、ReportAgent、ReviewerAgent |
| 人工 Gate | 製造處長（Coordinator / Human Gate） |
| 預期時間 | sandbox 演練 2-3 小時 |

---

## 1. 環境準備 / Environment Setup

### 1.1 前置需求 / Prerequisites

```bash
# 需求
python --version      # 3.10+
tmux -V               # tmux 已安裝
git --version         # git 已安裝
claude --version      # 或 codex / gemini 等任一 CLI agent
```

### 1.2 安裝 ClawTeam / Install ClawTeam

```bash
pip install clawteam
# 或從原始碼 / or from source:
# git clone https://github.com/HKUDS/ClawTeam.git && cd ClawTeam && pip install -e .
```

### 1.3 設定 Profile / Configure Profile

```bash
clawteam profile wizard      # 互動式設定 AI provider
clawteam profile test        # 測試 provider 連線
clawteam profile doctor      # 檢查環境問題
```

> **企業注意**：機敏製程資料的情境，profile 應指向地端 LLM（Llama 70B）或 Azure OpenAI 隔離 tenant，不可用公開雲 API。

---

## 2. 建立 Team 與 Workspace / Create Team & Workspace

### 2.1 建立 git repo（Workspace 隔離基礎）

```bash
mkdir qa-improvement && cd qa-improvement
git init
echo "# QA Improvement Agent Team" > README.md
git add -A && git commit -m "init"
```

### 2.2 開出 Team

```bash
clawteam team spawn-team qa-team \
  -d "月度不良率降低 1%：root cause → params → SPC → report" \
  -n leader
```

此時 ClawTeam 在 `~/.clawteam/qa-team/` 建立 team 狀態（JSON）。

### 2.3 確認 Team 狀態

```bash
clawteam team status qa-team
```

---

## 3. 設計任務與依賴鏈 / Design Tasks & Dependency Chain

依 L5 課程的 IPOE 表，把 Team 任務拆成 4 個帶依賴的 task：

```bash
# T1：根因分析（無依賴，最先）
clawteam task create qa-team \
  --owner RootCauseAgent \
  --title "Identify top-3 defect modes from MES/SPC/QC data" \
  --id T1

# T2：製程參數對應（依賴 T1）
clawteam task create qa-team \
  --owner ParameterAgent \
  --title "Map the 3 defect modes to process parameters" \
  --blocked-by T1 --id T2

# T3：SPC 管制建議（依賴 T2）
clawteam task create qa-team \
  --owner SPCAgent \
  --title "Propose SPC control limits for the mapped parameters" \
  --blocked-by T2 --id T3

# T4：整合報告（依賴 T1 + T2 + T3）
clawteam task create qa-team \
  --owner ReportAgent \
  --title "Integrate findings into a QA improvement report" \
  --blocked-by T1,T2,T3 --id T4
```

### 3.1 確認任務板

```bash
clawteam task list qa-team
# 應看到 T1 ready，T2/T3/T4 blocked
```

---

## 4. 派出 Worker Agents / Spawn Worker Agents

每個 Agent 在自己的 git worktree 與 tmux session 執行，彼此隔離。

```bash
clawteam spawn --team qa-team --agent-name RootCauseAgent \
  --task "Work on T1. Query the QA data, identify top-3 defect modes."

clawteam spawn --team qa-team --agent-name ParameterAgent \
  --task "Work on T2 once T1 completes."

clawteam spawn --team qa-team --agent-name SPCAgent \
  --task "Work on T3 once T2 completes."

clawteam spawn --team qa-team --agent-name ReportAgent \
  --task "Work on T4 once T1/T2/T3 complete."
```

> 每個 spawn 會自動注入 ClawTeam 協作 prompt，教 Agent 使用 `clawteam task` / `clawteam inbox` 等命令。

### 4.1 確認 worktree 隔離

```bash
git worktree list
# 每個 Agent 一個分支，互不覆蓋
```

---

## 5. 監看與協調 / Monitor & Coordinate

### 5.1 即時看板

```bash
clawteam board attach qa-team       # 進入即時看板
clawteam board live qa-team         # 終端機即時更新
clawteam board gource qa-team       # gource 視覺化（選用）
```

### 5.2 Leader 發訊息給 Agent

```bash
# 點對點：給特定 Agent 補充 context
clawteam inbox send qa-team RootCauseAgent \
  "優先看 5 月的 SPC 異常，客訴集中在端子壓接。"

# 廣播：通知全 Team
clawteam inbox broadcast qa-team \
  "製造處長要求週五前完成 T4 初稿。"
```

### 5.3 等待任務完成

```bash
clawteam task wait qa-team          # 阻塞直到所有 task 完成
```

---

## 6. 衝突處理與整合 / Conflict Handling & Integration

### 6.1 偵測衝突

```bash
clawteam context conflicts qa-team
# 檢查各 Agent worktree 是否有衝突的修改
```

### 6.2 注入整合 context

```bash
clawteam context inject qa-team ReportAgent \
  --from T1,T2,T3
# 把前三個 task 的產出注入 ReportAgent 的上下文
```

### 6.3 查看協作 log

```bash
clawteam context log qa-team
```

---

## 7. Human Gate：製造處長審核 / Human Gate Review

ReportAgent 完成 T4 後，**不直接結案**，進入 Human Gate：

1. 製造處長閱讀整合報告（ReportAgent 的 worktree 分支）。
2. 檢查每個建議是否有 evidence 追溯（哪個 defect mode → 哪個參數 → 哪條 SPC 規則）。
3. 三種決策：
   - **接受** → `clawteam task update qa-team T4 --status completed`
   - **退回** → `clawteam inbox send qa-team ReportAgent "退回原因：..."` + task 重開
   - **部分接受** → 標註需人工的部分，其餘 completed

> Human Gate 是 L5 的核心治理機制 — Agent Team 自主協作，但**重大決策永遠有人簽核**。

---

## 8. 結案與快照 / Close-out & Snapshot

```bash
# 確認所有 task 完成
clawteam task list qa-team

# 快照 team 狀態（保存演練紀錄）
clawteam team snapshot qa-team --label "qa-improvement-2026-05-run1"

# 匯出證據（給 L5 課程 Gate 5 驗收）
clawteam board show qa-team > evidence/board-final.txt
clawteam task list qa-team > evidence/task-list-final.txt
```

---

## 9. L5 課程 Gate 5 驗收對應 / Mapping to L5 Gate 5

| Gate 5 通過條件 | 本 walkthrough 對應證據 |
| --- | --- |
| 完成 ≥ 1 個 Agent Team 情境設計 | qa-team 完整跑通 |
| 每個 Agent 有角色、Input、Output、限制 | RootCause/Parameter/SPC/Report/Reviewer 角色卡 |
| 有整合 Agent 或整合流程 | ReportAgent + `context inject` |
| 有 Reviewer / Human Gate | 製造處長審核流程（§7） |
| 有 ROI 與治理設計 | 不良率 KPI + Audit log + snapshot |
| 已在 sandbox 跑通 1 次完整流程 | §8 snapshot + evidence 匯出 |

---

## 10. 常見問題 / Troubleshooting

| 問題 | 處理 |
| --- | --- |
| `clawteam spawn` 後 Agent 沒動作 | 檢查 `clawteam profile doctor`；確認 CLI agent 已安裝 |
| Agent 卡在 blocked task | 確認上游 task 已 `--status completed` |
| worktree 衝突 | `clawteam context conflicts` → 手動 merge → `context inject` |
| tmux session 找不到 | `tmux ls` 確認；ClawTeam 預設用 tmux backend |
| 機敏資料疑慮 | profile 改指地端 LLM；不要用公開雲 API |

---

## 11. 從 Walkthrough 到正式導入 / From Walkthrough to Production

| 階段 | 動作 |
| --- | --- |
| Sandbox 演練（本檔） | 跑通流程、理解 5 層架構、產出 Gate 5 證據 |
| 部門試點 | 真實資料（去識別化）、File transport、單機 |
| 跨廠 / 跨院區 | P2P (ZeroMQ) transport |
| 集團 | Redis transport（ClawTeam v0.4 roadmap） |
| 集中監控 | Web UI（ClawTeam v1.0 roadmap） |

---

## 引用 / Citation

本 walkthrough 之 ClawTeam 命令、架構、設計理念皆引用自上游 HKUDS/ClawTeam (MIT License)。本 repo **未重製、未 fork** 原始碼；學員需自行 `pip install clawteam`。完整引用條款見 [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md)。

The ClawTeam commands, architecture, and design principles in this walkthrough are cited from upstream HKUDS/ClawTeam (MIT License). This repo does **not** reproduce or fork the source; learners install upstream via `pip install clawteam`. Full citation: [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md).
