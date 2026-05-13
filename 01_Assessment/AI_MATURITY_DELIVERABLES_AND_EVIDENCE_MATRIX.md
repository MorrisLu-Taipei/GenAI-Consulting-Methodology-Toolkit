# AI 成熟度交付物、證據與 Stage Gate 總矩陣

版本：v1.0  
作者：Morris  
用途：將 L1-L5 成熟度理論轉成可交付、可驗收、可判斷能否進下一階段的顧問控制表。

---

## 1. 使用目的

AI 成熟度模型不能只描述「能力等級」，必須能回答：

1. 這一級完成時，客戶手上應該拿到什麼？
2. 用什麼 evidence 證明不是口頭完成？
3. 誰負責維護與審核？
4. 哪些狀況代表不能通過？
5. 通過後才可以進入哪一級？

因此，本矩陣採用固定格式：

`Level → Definition of Done → Deliverables → Evidence → Owner → Stage Gate → Fail Condition → Next Level Entry Criteria`

---

## 2. L1-L5 總覽矩陣

| Level | 成熟度定位 | Definition of Done | 核心 Deliverables | 必備 Evidence | 主要 Owner | Stage Gate | Next Level |
|---|---|---|---|---|---|---|---|
| L1 | Chat AI / OpenWebUI | 公司有受控 AI 入口，每位使用者能用自己帳號登入並完成基本知識工作 | OpenWebUI 帳號/群組/權限表、個人聊天區、Prompt Library、AI 使用規範 | 登入截圖、個人聊天截圖、Admin Panel、權限表、Prompt 作業、資料案例判斷 | IT / HR / 顧問 | Gate 1A-1F | L2 Skill AI |
| L2 | Skill AI / Antigravity / Claude Code / Codex | 個人經驗、SOP、Prompt、工程實作可被沉澱為可複用 Skill，並轉成 L3 Blueprint | Skill Library、Skill 模板、Owner/版本表、Antigravity artifacts、Workflow Blueprint | Skill 測試輸出、版本紀錄、Owner 名單、sample payload、n8n node map | 部門 Owner / IT / 顧問 | Gate 2A-2F | L3 Workflow AI |
| L3 | Workflow AI / n8n | 至少一個 workflow 可穩定執行，有系統串接、人工審核、Log、錯誤處理與備份 | n8n Workflow JSON、Data Tables Schema、Sub-workflow Library、GitHub Backup SOP、L4 Workflow Contract | Execution Log、測試 payload、Data Tables / Sheets 紀錄、備份 commit、人工審核紀錄、失敗測試 | IT / 流程 Owner | Gate 3A-3G | L4 Hermes Agent |
| L4 | Auto Agentic AI / Hermes Agent | Agent 能以 Wiki 記憶為底座，完成 ingest/query/update/briefing，並能呼叫 L2 Skill / L3 Workflow | Hermes Agent 任務卡、L4 IPOE、Wiki、schema、ingest/query/update 紀錄、briefing、Runbook | source page、SQLite 查詢、log、briefing、工具呼叫紀錄、人工審核、Gate 4A-4E | 部門 Owner / IT | Gate 4A-4E | L5 ClawTeam |
| L5 | Agentic Team AI / ClawTeam | 多個 Agent 有角色分工、任務分派、整合輸出、Reviewer、人工 Gate 與 ROI 衡量 | ClawTeam 角色卡、任務分派表、Agent Team IPOE、整合報告、Reviewer Gate、ROI 表 | 各 Agent 輸出、整合紀錄、Reviewer 紀錄、主管簽核、ROI/KPI 追蹤 | 管理 Sponsor / 顧問 | Gate 5 | 制度化與擴散 |

---

## 3. L1 Chat AI：OpenWebUI

### 3.1 Definition of Done

L1 完成不是「員工會問 AI 問題」，而是：

- 每位使用者有自己的 OpenWebUI 帳號。
- 每位使用者有自己的聊天區域、歷史紀錄、資料夾與個人 Prompt。
- Admin 能管理帳號、角色、群組、權限、模型與功能。
- 公司有 AI 使用規範與資料輸入邊界。
- 使用者能完成基本知識工作，例如摘要、Email、會議紀錄、報告草稿。

### 3.2 Deliverables

| Deliverable | 必備 | 說明 |
|---|---|---|
| OpenWebUI 使用者操作手冊 | 是 | 登入、聊天、模型、文件、Prompt、資料邊界 |
| 帳號清單 | 是 | 每位學員獨立帳號，不共用帳號 |
| 群組與權限表 | 是 | 角色、群組、模型可見性、功能權限 |
| Admin Runbook | 是 | 帳號審核、群組、模型、功能、分享、資料規範 |
| Prompt Library v1 | 是 | 個人與部門常用 Prompt |
| AI 使用規範 | 是 | 可輸入、禁止輸入、需人工確認 |
| 高頻工作清單 | 是 | L2 Skill 候選來源 |

### 3.3 Evidence

- 登入截圖。
- 個人聊天區截圖。
- Admin Panel 截圖。
- Groups / Permissions 設定表。
- Prompt 作業。
- 資料案例判斷表。
- Gate 1 驗收紀錄。

### 3.4 Owner

| 項目 | Owner |
|---|---|
| OpenWebUI 環境 | IT |
| 帳號與權限 | IT / HR |
| AI 使用規範 | IT / HR / 法遵 |
| Prompt Library | 部門 Owner |
| Gate 1 驗收 | 顧問 + IT + HR |

### 3.5 Fail Condition

- 使用者共用帳號。
- Admin 無法管理角色、群組與權限。
- 無資料輸入規範。
- 員工不知道哪些資料不能輸入 AI。
- 沒有產出任何高頻工作清單。

### 3.6 Next Level Entry Criteria

可進入 L2 的條件：

- 至少 10 個高頻工作被整理出來。
- 有 Prompt Library v1。
- 有資料可用 / 禁用規範。
- 至少一組種子人員完成 L1 練習。

---

## 4. L2 Skill AI：Antigravity / Claude Code / Codex

### 4.1 Definition of Done

L2 完成不是「學員會用 AI 寫東西」，而是：

- 至少 3-5 個 Skill 可被非原作者重複使用。
- 每個 Skill 有 input、process、output、constraints、quality check。
- 每個 Skill 有 Owner 與版本。
- 工程團隊可產出 Antigravity app / test / docs artifacts。
- 至少一個 Skill 被轉成 L3 Workflow Blueprint。

### 4.2 Deliverables

| Deliverable | 必備 | 說明 |
|---|---|---|
| Skill Library | 是 | 3-5 個可重複使用 Skill |
| Skill 模板 | 是 | IPOC / constraints / quality check |
| Skill Owner 與版本表 | 是 | 維護責任與版本紀錄 |
| Skill 測試紀錄 | 是 | 至少 2 筆測試輸入輸出 |
| Antigravity artifacts | 視客戶 | app prototype、unit test、README、deployment evidence |
| L3 Workflow Blueprint | 是 | trigger、I/O schema、sample payload、node map、human gate、log、error handling |

### 4.3 Evidence

- Skill 文件。
- 測試輸入輸出。
- Owner 名單。
- 版本紀錄。
- Antigravity task / implementation / walkthrough artifact。
- Sample payload。
- n8n node map。
- Gate 2 驗收紀錄。

### 4.4 Owner

| 項目 | Owner |
|---|---|
| Skill 內容 | 部門 Owner |
| Skill Library | 顧問 / 部門窗口 |
| 工程 artifact | IT / 工程 Owner |
| L3 Blueprint | 流程 Owner + IT |
| Gate 2 驗收 | 顧問 + 部門主管 |

### 4.5 Fail Condition

- Skill 只有 Prompt，沒有 input/process/output。
- Skill 只有原作者會用。
- 沒有 Owner 或版本。
- 沒有測試紀錄。
- 沒有轉成 L3 Workflow Blueprint。

### 4.6 Next Level Entry Criteria

可進入 L3 的條件：

- 至少 1 個 Skill 被選為流程化候選。
- 已定義 trigger、I/O schema、sample payload。
- 已完成 n8n node map。
- 已定義 human gate、log、error handling。
- 已盤點所需系統與 credential。

---

## 5. L3 Workflow AI：n8n

### 5.1 Definition of Done

L3 完成不是「Workflow demo 跑一次」，而是：

- Workflow 能處理正常與錯誤 payload。
- 至少串接 2 個系統或平台。
- 有 AI 處理步驟與可檢查輸出。
- 有人工審核 Gate。
- 有 Execution Log、錯誤處理與 GitHub 備份。
- 有 L4 Workflow Contract。

### 5.2 Deliverables

| Deliverable | 必備 | 說明 |
|---|---|---|
| n8n Workflow JSON | 是 | 可匯入 / 匯出的流程檔 |
| Workflow Blueprint | 是 | L2 接手文件 |
| Credential / API / Webhook 權限表 | 是 | 權限範圍與 Owner |
| Data Tables / Sheets / DB Schema | 是 | 狀態與資料記錄 |
| Sub-workflow Library | 建議 | 可重複使用模組 |
| Execution Log | 是 | 成功、失敗、重跑 |
| Human Gate 設計 | 是 | 審核人、條件、結果 |
| Error Handling / Retry / Fallback | 是 | 失敗通知與處理 |
| GitHub Backup SOP | 是 | Workflow / Credential 備份與版本 |
| L4 Workflow Contract | 是 | Hermes Agent 可呼叫方式 |

### 5.3 Evidence

- n8n Execution Log。
- 2 筆正常 payload 與 1 筆錯誤 payload。
- Node 設定截圖。
- Data Tables / Sheets 紀錄。
- AI input/output。
- 人工審核紀錄。
- GitHub backup commit。
- 失敗測試紀錄。

### 5.4 Owner

| 項目 | Owner |
|---|---|
| Workflow 設計 | 流程 Owner |
| n8n 建置 | IT / 自動化人員 |
| Credential | IT |
| Human Gate | 部門主管 |
| Backup / 維運 | IT |
| Gate 3 驗收 | IT + 流程 Owner + 顧問 |

### 5.5 Fail Condition

- Workflow 只在講師電腦跑，客戶不能重現。
- 沒有 Execution Log。
- 沒有錯誤處理。
- 沒有人工審核。
- Credential 權限不明。
- 沒有備份。
- 沒有 L4 Workflow Contract。

### 5.6 Next Level Entry Criteria

可進入 L4 的條件：

- 至少 1 個 Workflow 穩定執行。
- 有可被 Hermes Agent 呼叫的方式。
- 有權限邊界與輸出格式。
- 有 Log、錯誤處理與人工 Gate。
- 有 IT / 流程 Owner 維護責任。

---

## 6. L4 Auto Agentic AI：Hermes Agent

### 6.1 Definition of Done

L4 完成不是「有一個 Agent demo」，而是：

- Hermes Agent 有明確任務卡與邊界。
- Agent 有 Wiki 記憶與 schema。
- Agent 能完成 ingest、query、update、briefing。
- Agent 能呼叫 L2 Skill 與 L3 Workflow。
- Agent 的輸出有 evidence 與人工 Gate。
- Agent 有維運 Runbook。

### 6.2 Deliverables

| Deliverable | 必備 | 說明 |
|---|---|---|
| Hermes Agent 任務卡 | 是 | 角色、任務、限制、資料源、工具 |
| L4 IPOE 表 | 是 | input/process/output/evidence |
| `purpose.md` / `SCHEMA.md` | 是 | 知識底座與規則 |
| 初始 Wiki | 是 | INBOX、queue、watchlist、tasks、wiki pages |
| Ingest 測試紀錄 | 是 | 至少 1 份文件 |
| Query / Update 測試紀錄 | 是 | 可引用、可回寫 |
| Briefing 範本 | 是 | morning / weekly briefing |
| Gate 4A-4E 表 | 是 | 環境、知識、ingest、query/update、治理 |
| 維運 Runbook | 是 | 排程、Owner、fallback、人工接手 |

### 6.3 Evidence

- `hermes doctor` 或環境檢查。
- Wiki 檔案。
- source page。
- log。
- SQLite 查詢。
- query record。
- update diff。
- briefing。
- 工具呼叫紀錄。
- 人工審核紀錄。

### 6.4 Owner

| 項目 | Owner |
|---|---|
| Agent 任務 | 部門 Owner |
| Hermes 環境 | IT |
| Wiki / schema | 顧問 + 部門 Owner |
| Workflow / Skill 工具 | IT + 流程 Owner |
| Human Gate | 部門主管 |
| Gate 4 驗收 | 部門主管 + IT + 顧問 |

### 6.5 Fail Condition

- Agent 沒有任務邊界。
- Agent 無法追溯資料來源。
- 沒有 Wiki / schema。
- 只能聊天，無 ingest/query/update/briefing。
- 沒有人工 Gate。
- 沒有 Runbook。

### 6.6 Next Level Entry Criteria

可進入 L5 的條件：

- 至少 1 個 Hermes Agent 通過 Gate 4A-4E。
- Agent 可呼叫至少 1 個 L2 Skill 與 1 個 L3 Workflow。
- Agent output 可追溯、可審核、可維運。
- 已定義多 Agent 協作候選任務。

---

## 7. L5 Agentic Team AI：ClawTeam

### 7.1 Definition of Done

L5 完成不是「有很多 Agent」，而是：

- 多個 Agent 有清楚角色分工。
- 有任務分派、協作、整合與 Reviewer。
- 有人工 Gate 與管理層審核。
- 有 ROI / KPI 衡量。
- 能產出跨部門整合報告或決策支援成果。

### 7.2 Deliverables

| Deliverable | 必備 | 說明 |
|---|---|---|
| ClawTeam 角色卡 | 是 | 各 Agent 角色、能力、限制 |
| 任務分派表 | 是 | 任務拆解、負責 Agent、輸入輸出 |
| Agent Team IPOE | 是 | 每個 Agent 的 input/process/output/evidence |
| 整合報告模板 | 是 | 多 Agent 輸出的整合格式 |
| Reviewer / Critic 設計 | 是 | 品質檢查與衝突處理 |
| Human Gate 設計 | 是 | 管理層審核與簽核 |
| ROI / KPI 表 | 是 | 工時、品質、速度、錯誤率 |

### 7.3 Evidence

- Agent 角色卡。
- 任務分派紀錄。
- 各 Agent 輸出。
- 整合報告。
- Reviewer 紀錄。
- 主管審核紀錄。
- ROI / KPI 追蹤表。

### 7.4 Owner

| 項目 | Owner |
|---|---|
| Agent Team 任務 | 管理 Sponsor |
| 各 Agent 角色 | 部門 Owner |
| 整合報告 | 顧問 / PM |
| Reviewer | 指定審核角色 |
| ROI / KPI | 管理 Sponsor / 顧問 |
| Gate 5 驗收 | 管理層 |

### 7.5 Fail Condition

- 多個 Agent 沒有角色分工。
- 沒有 Reviewer。
- 沒有人工 Gate。
- 沒有整合輸出。
- 無法量化或說明 ROI。
- L4 Agent 尚未穩定就進入 L5。

### 7.6 Next Level Entry Criteria

L5 通過後進入制度化與擴散：

- 建立 AI Agent Team 治理規範。
- 擴大到更多部門與流程。
- 建立季度 KPI / ROI review。
- 建立下一波 Agent Team backlog。

---

## 8. 成熟度判定原則

1. 沒有 evidence，不算完成。
2. 沒有 Owner，不算可維運。
3. 沒有 Stage Gate，不應進下一級。
4. 沒有 fail condition，驗收會變成主觀判斷。
5. 沒有 next level entry criteria，成熟度模型會變成靜態評分，而不是轉型路線圖。

