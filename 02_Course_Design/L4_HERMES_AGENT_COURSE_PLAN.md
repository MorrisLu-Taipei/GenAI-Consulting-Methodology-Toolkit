# L4 Hermes Agent 完整課程規劃

版本：v1.0  
作者：Morris  
適用層級：L4 Auto Agentic AI  
參考素材：Hermes `llm-wiki/starter-kit-v2`

---

## 1. L4 重新定位

L4 不只是「讓 AI 自己跑任務」。在本方法論中，L4 Hermes Agent 的定位是：

> 把 L1 Chat、L2 Skill、L3 Workflow 升級成可持續運行的知識型 Agent 作業系統。

Hermes Agent 不是單一 Prompt，也不是只會觸發 API 的機器人。它應該具備：

1. 可持續的任務記憶：以 Markdown Wiki 作為知識真相來源。
2. 可查詢的索引能力：以 SQLite / FTS 作為衍生索引與查詢快取。
3. 可組合的技能：以 `llm-wiki-manager`、`source-analysis-zh`、`keyword-extraction-zh`、`autonomous-discovery`、`briefing-generator` 等技能形成 Agent 能力。
4. 可驗證的工具鏈：用 deterministic tools 完成寫入、索引、驗證、抽取、快取、刪除保護與紀錄。
5. 可排程的工作節奏：用 nightly ingest、morning briefing、discovery ping、evening preview、weekly graph synthesis 形成固定營運節奏。
6. 可治理的人機協作：高風險動作保留人工 Gate，所有輸出需有證據、Log、來源與審核紀錄。

因此，L4 課程的重點不是讓學員相信 Agent 很厲害，而是讓企業知道如何把 Agent 放進可控流程中，讓它每天穩定產生可驗證的工作成果。

---

## 2. 課程目標

完成 L4 課程後，學員應能：

1. 說明 Hermes Agent 與 L1 Chat、L2 Skill、L3 Workflow 的差異。
2. 設計一個部門級 Hermes Agent 的使用情境、任務邊界、輸入來源與人工 Gate。
3. 建立 Hermes Agent 的知識作業結構：`purpose.md`、`SCHEMA.md`、`INBOX.md`、`queue.md`、`watchlist.md`、`tasks.md`、`wiki/`、`.index.db`。
4. 定義 L4 Agent 會吃什麼 input、執行什麼 process、產出什麼 output，以及用哪些 evidence 驗證。
5. 設計 ingest、query、update、lint、briefing、discovery、graph synthesis 的運作流程。
6. 將 L2 Skill 與 L3 Workflow 接入 Hermes Agent 的任務鏈。
7. 建立 Agent 操作 Runbook、權限表、證據表、Stage Gate 與上線檢查表。
8. 判斷哪些任務適合 L4，哪些任務必須留在 L1-L3 或延後到 L5。

---

## 3. 適合對象

| 對象 | 課程重點 |
|---|---|
| 部門主管 | Agent 能解決什麼管理問題、如何驗收成果、如何設 Gate |
| IT / 系統部門 | 部署、權限、資料路徑、工具、排程、Log、索引與維運 |
| 流程 Owner | 哪些工作可以交給 Agent 準備、整理、提醒、追蹤 |
| 知識工作者 | 如何把文件、資料、研究、會議與任務轉成 Agent 可長期累積的 Wiki |
| 顧問 / PM | 如何用 L4 作為 AI 轉型診斷後的 PoC 或導入方案 |

---

## 4. 課前條件

| 項目 | 最低要求 |
|---|---|
| L1 | 已有 OpenWebUI 或等效 Chat AI 入口 |
| L2 | 至少有 1-3 個可重複使用的 Skill 或 Prompt SOP |
| L3 | 至少有 1 個可呼叫的 n8n Workflow 或 API 流程 |
| 資料 | 有可訓練的範例文件、SOP、FAQ、報告、研究資料或客戶案例 |
| 治理 | 已定義不可碰資料、人工審核點、輸出責任人 |
| 技術 | 已確認雲端、Hybrid 或全地端部署模式 |

---

## 5. L4 Input / Process / Output / Evidence

| 類別 | 定義 |
|---|---|
| Input | 客戶任務、部門文件、PDF、SOP、FAQ、研究資料、API 回傳、n8n Workflow 結果、L2 Skill、`purpose.md`、`SCHEMA.md`、`watchlist.md`、`queue.md`、權限表 |
| Process | orient-first、bootstrap、ingest、source analysis、keyword extraction、index upsert、query、update、lint、autonomous discovery、briefing、graph synthesis、人工審核 |
| Output | Wiki pages、source analysis、concept/entity/claim pages、查詢回答、每日 briefing、待審 watchlist、任務追蹤清單、Agent 執行紀錄、改善建議、上線報告 |
| Evidence | `hermes doctor` 結果、技能安裝清單、設定檔、Wiki 檔案、Log、SQLite 查詢、queue/watchlist/tasks、briefing email、n8n 執行紀錄、人工審核紀錄、Gate 簽核 |

---

## 6. 完整課程版本

### 6.1 L4 Foundation：3 小時

目標：讓主管與種子團隊理解 Hermes Agent 的價值、限制與驗收方式。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 30 分 | L4 定位 | Agent vs Chat vs Skill vs Workflow | L4 共識圖 |
| 40 分 | Hermes 架構 | Wiki、SQLite、skills、tools、runtime schema、policy | Hermes 架構圖 |
| 40 分 | 企業情境 | 研發、製造、醫院、客服、法務、行銷案例 | L4 情境候選清單 |
| 40 分 | IPOE | Input / Process / Output / Evidence | L4 IPOE 表 |
| 30 分 | Stage Gate | Gate 4A-4E 與人工審核 | L4 Gate 表 |
| 40 分 | 工作坊 | 選一個部門任務改寫成 Hermes Agent 任務 | Agent 任務卡草稿 |

### 6.2 L4 Builder：1 天

目標：建立可運行的 Hermes Agent PoC。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 60 分 | 環境健康檢查 | `hermes doctor`、gateway、model、權限與路徑 | 環境檢查紀錄 |
| 60 分 | 技能安裝 | 安裝 5 個核心 skills | 技能安裝清單 |
| 60 分 | Config migrate | 設定 wiki path、language、embedding、email、lookback | Hermes config |
| 90 分 | Bootstrap wiki | 建立 `wiki/`、`SCHEMA.md`、`purpose.md`、`.index.db` | 初始 Wiki |
| 90 分 | Ingest 實作 | 匯入一份 PDF / SOP / FAQ，產生 source analysis | Source page 與 Log |
| 60 分 | Query / file-back | 用引用回答問題，將查詢結果回寫 Wiki | Query record |
| 60 分 | L2/L3 接入 | 呼叫 Skill 與 n8n Workflow，形成 Agent 任務鏈 | Agent test run |
| 60 分 | Gate 4 驗收 | 檢查 evidence、權限、Log、人工審核 | Gate 4A-4C 紀錄 |

### 6.3 L4 Operator：2 天

目標：讓 Hermes Agent 從 PoC 變成可維運的部門作業。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 90 分 | Orient-first SOP | 每次 Agent 開工前讀取 schema、runtime、purpose、INBOX、index、log | Agent 開工 SOP |
| 90 分 | Update mode | 讓 Agent 修改既有 Wiki 頁，保留 diff、原因與 log | 更新紀錄 |
| 90 分 | Lint / schema | 檢查 frontmatter、cross-ref、缺漏欄位、壞連結 | Lint report |
| 90 分 | Discovery | 設定 watchlist，從外部來源收集 metadata，不直接 ingest | P2 queue |
| 90 分 | Briefing | 產生 morning briefing、evening preview、2h ping | Briefing 報告 |
| 90 分 | Graph synthesis | 找概念關聯、矛盾、缺口與下一步任務 | Graph insight |
| 90 分 | Cron / Runbook | nightly ingest、morning briefing、discovery ping、weekly lint | 維運排程表 |
| 90 分 | Governance | 權限、資料分級、人工 Gate、fallback、事故處理 | L4 治理表 |
| 90 分 | Demo day | 每組展示一個 Hermes Agent 完整閉環 | Demo 與驗收 |
| 90 分 | Roadmap | 將 L4 對接 L5 ClawTeam 的前置條件 | L4-to-L5 Roadmap |

---

## 7. 五個核心技能如何進入課程

| Skill | 課程定位 | 學員要會什麼 |
|---|---|---|
| `llm-wiki-manager` | Hermes Agent 的主控技能 | bootstrap、ingest、query、update、lint、graph-synthesis、schema-evolve |
| `source-analysis-zh` | 嚴謹來源分析技能 | 將 PDF、文章、報告、法規、影片逐一轉成 10 段式分析 |
| `keyword-extraction-zh` | 知識擴張技能 | 從新資料抽出 keyword candidate，交由人工 approve / reject |
| `autonomous-discovery` | 自主發現技能 | 根據 watchlist 到外部來源找 metadata，加入 queue，但不直接 ingest |
| `briefing-generator` | 營運節奏技能 | 產生 morning briefing、evening preview、2h ping、weekly graph digest |

---

## 8. L4 Stage Gate 控制

| Gate | 檢查問題 | 必備 Evidence | 判定 |
|---|---|---|---|
| Gate 4A：環境可用 | Hermes、模型、gateway、權限是否可用？ | `hermes doctor`、model list、gateway status | Pass / Fail |
| Gate 4B：知識底座可用 | Wiki、schema、purpose、index 是否建立？ | `SCHEMA.md`、`purpose.md`、`.index.db`、初始化 log | Pass / Fail |
| Gate 4C：Ingest 閉環可用 | Agent 能否吃文件、分析、寫入、索引、留 Log？ | source page、concept/entity/claim、log、SQLite 查詢 | Pass / Fail |
| Gate 4D：查詢與更新可用 | Agent 能否用證據回答、回寫結果、保留紀錄？ | query record、update diff、引用來源、人工審核紀錄 | Pass / Fail |
| Gate 4E：營運與治理可用 | 是否有排程、briefing、watchlist、queue、人工 Gate？ | cron 設定、briefing、queue、watchlist、權限表、Gate 簽核 | Pass / Fail |

未通過 Gate 4A-4C 時，不進入部門上線。未通過 Gate 4D-4E 時，可以做展示，但不能宣稱為可營運的 L4 Agent。

---

## 9. L4 控制表

| 控制項 | 欄位 | 說明 |
|---|---|---|
| Agent 任務卡 | 角色、任務、使用者、資料源、禁止事項、人工 Gate | 定義 Agent 能做什麼與不能做什麼 |
| Input Register | 文件、API、Workflow、Skill、資料等級、Owner | 確認 Agent 吃進來的資料可用且可授權 |
| Process Map | orient、ingest、query、update、briefing、discovery、lint | 確認每一步有 SOP |
| Output Register | Wiki page、報告、摘要、提醒、任務、更新 | 確認輸出可被業務使用 |
| Evidence Register | Log、索引、引用、執行紀錄、審核紀錄 | 確認成果可驗證 |
| Risk Register | 幻覺、錯誤引用、資料外洩、過度自動化、未授權修改 | 確認風險有控制 |
| Stage Gate | 4A-4E | 確認能否進下一階段 |

---

## 10. 課堂練習

### 練習 1：L4 任務拆解

將「每週整理客訴與改善建議」改寫為 Hermes Agent 任務。

必填：

- 使用者是誰？
- Agent 每天或每週何時執行？
- 需要吃哪些文件、系統與 Workflow？
- 哪些動作只能產生草稿，不能自動送出？
- 主管用什麼 evidence 驗收？

### 練習 2：建立目的與 Schema

為一個部門 Agent 建立：

- `purpose.md`
- `SCHEMA.md`
- 來源類型
- 概念類型
- 禁止事項
- Domain-specific red flags

### 練習 3：Ingest 一份資料

輸入一份 PDF、SOP、FAQ 或報告，產出：

- source analysis
- source page
- keyword candidates
- log
- SQLite 查詢結果

### 練習 4：產生 Briefing

根據 `INBOX.md`、`queue.md`、`watchlist.md`、`tasks.md` 產生一份主管可讀的 morning briefing。

### 練習 5：設計 Gate 4

每組設計自己的 Gate 4A-4E 判定表，並說明哪些 evidence 不足時不能上線。

---

## 11. L4 Deliverables

| Deliverable | 說明 | 驗收方式 |
|---|---|---|
| L4 Hermes Agent 任務卡 | 定義角色、任務、邊界、工具、人工 Gate | 部門主管簽核 |
| L4 IPOE 表 | 定義 input、process、output、evidence | 顧問與 IT 審核 |
| Hermes Agent 架構圖 | 說明 Wiki、SQLite、skills、tools、cron、OpenWebUI / n8n 的關係 | 課堂展示 |
| 初始 Wiki | 建立 purpose、schema、INBOX、queue、watchlist、tasks | 檔案與截圖 |
| Ingest 測試紀錄 | 至少匯入 1 份真實或樣本文件 | source page、log、index |
| Query / Update 測試紀錄 | 至少完成 3 個可追溯查詢與 1 次回寫 | query record、update diff |
| Briefing 範本 | morning briefing 或 weekly briefing | 報告樣本 |
| L4 Stage Gate 表 | Gate 4A-4E | 簽核紀錄 |
| 維運 Runbook | 排程、監控、fallback、人工審核、事故處理 | IT / Owner 驗收 |

---

## 12. 產業調整

| 產業 | L4 推薦切入點 | 特別注意 |
|---|---|---|
| 研發製造業 | 技術文件 Wiki、客訴摘要、異常原因整理、ERP 異常報告草稿 | 不直接改 ERP 核心資料，先做建議與追蹤 |
| 行銷服務業 | 提案素材庫、競品監控、活動 briefing、客戶週報草稿 | 可較快導入外部 discovery，但需標記來源可信度 |
| 醫院 / 醫療 | 院內 SOP 查詢、客服 FAQ 草稿、品質事件摘要、研究文獻 briefing | 不做診斷與治療建議，高風險內容必須人工審核 |
| 法務 / 金融 | 法規追蹤、案例摘要、風險提醒、投研資料整理 | 強化引用、版本、審核、資料留存與合規 |
| 內部管理 | 會議紀錄、任務追蹤、政策問答、跨部門進度 briefing | 明確資料權限與責任歸屬 |

---

## 13. 部署模式調整

| 模式 | L4 課程調整 |
|---|---|
| 雲 AI | 快速展示 Agent 閉環，適合 PoC、知識整理、非機敏文件 |
| Hybrid | 文件與索引可留在內部，模型或部分 API 走雲端，適合多數企業導入 |
| 全地端 | 強化模型、gateway、內網資料、權限、Log、備份、稽核與維運，課程需增加技術實作時間 |

---

## 14. L4 到 L5 的銜接條件

只有當 L4 已具備以下能力時，才建議進入 L5 ClawTeam：

1. 至少 1 個 Hermes Agent 通過 Gate 4A-4E。
2. Agent 的 input、process、output、evidence 都可追溯。
3. 已有穩定的 Wiki 記憶、Log、索引與 briefing 節奏。
4. 已有至少 2 個可重複呼叫的 L2 Skill。
5. 已有至少 1 個穩定的 L3 Workflow。
6. 高風險決策有人工 Gate 與責任 Owner。

L5 不是把多個不穩定 Agent 放在一起，而是讓已經可治理的 L4 Agent 進入團隊協作。

