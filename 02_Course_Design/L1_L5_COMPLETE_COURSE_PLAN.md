# L1-L5 完整課程規劃與上課內容

更新日期：2026-05-13

## 1. 課程設計目標

本課程不是單純教工具，而是讓企業沿著 L1-L5 成熟度逐步建立可驗證的 AI 組織能力。

每一級課程都必須定義：

- 課程目標。
- 適合對象。
- 課前需求。
- 上課內容。
- 課堂實作。
- 課後作業。
- 完成標準。
- 可驗證 Deliverables。
- 能否進入下一級的 Stage Gate。

## 1.5 課前故事引導：先講未來，再講課程

L1-L5 課程開場應先讓客戶想像「上完課後，公司會具備什麼能力」。客戶不是先被工具吸引，而是先被未來工作情境吸引。

建議講師在課前共識會或第一堂課，用以下故事開場：

> 三個月後，員工不再各自使用不同 AI 工具。每個人用自己的 OpenWebUI 帳號登入，有自己的聊天區與權限；部門主管把高手方法整理成 Skill；n8n 把 Gmail、Sheets、Notion、CRM、API、ERP 串成流程；Hermes Agent 每天產生 briefing 與追蹤清單；ClawTeam 讓多個專業 Agent 協作完成跨部門任務。課程的目的，就是一步一步把公司帶到這個狀態。

| 等級 | 課前要讓客戶想像的未來能力 | 上課要產出的證明 |
| --- | --- | --- |
| L1 | 每位員工都有自己的受控 AI 工作區，知道什麼資料可以用、什麼資料不能用 | OpenWebUI 帳號 / 群組 / 權限表、個人聊天區截圖、Prompt Library |
| L2 | 部門高手方法可以被複製，新人能照 Skill 產出接近標準的成果 | Skill Library、Skill 標準模板、非原作者測試紀錄 |
| L3 | AI 能跨系統做事，不只回答問題 | n8n Workflow PoC、Execution Log、系統串接表、人工 Gate |
| L4 | Agent 能讀資料、查 Wiki、呼叫工具、產出 briefing，並留下 evidence | Hermes Agent 任務卡、Wiki 紀錄、briefing、Gate 4A-4E |
| L5 | 多個 Agent 能分工協作，支援跨部門任務 | Agent Team 角色卡、任務分派紀錄、整合報告模板 |

這段故事的目的，是讓客戶在上課前先知道自己要買的不是「一套課程」，而是一條從個人 AI 使用到企業 AI Operating Model 的能力路徑。

## 2. 課程總覽

| 等級 | 課程名稱 | 工具 / 平台 | 建議時數 | 核心產出 | Stage Gate |
| --- | --- | --- | ---: | --- | --- |
| L1 | Chat AI 基礎與企業使用規範 | OpenWebUI | 3-6 小時 | AI 使用規範、Prompt Library、個人效率案例 | Gate 1 |
| L2 | Skill AI 與部門知識沉澱 | Antigravity / Claude Code / Codex | 6-12 小時 | Skill Library、3-5 個 Skill、Owner 與版本 | Gate 2 |
| L3 | Workflow AI 與流程自動化 | n8n | 6-18 小時 | n8n Workflow PoC、系統串接表、Log 與審核節點 | Gate 3 |
| L4 | Auto Agentic AI 任務代理 | Hermes Agent | 6-12 小時 | Agent 任務卡、工具清單、權限表、測試紀錄 | Gate 4 |
| L5 | Agentic Team AI 多 Agent 協作 | ClawTeam | 6-12 小時 | Agent Team 角色卡、任務分派、整合報告模板 | Gate 5 |

## 3. 課程包裝建議

### 3.1 半日體驗課：3 小時

適合：初次接觸客戶、主管共識會、業務開發。  
內容：L1-L5 總覽、10 題快速診斷、1 個情境示範。  
產出：成熟度初判、課程比例建議、下一步提案。

### 3.2 一日工作坊：6 小時

適合：部門主管、HR、種子人員。  
內容：L1 + L2 + L3 場景盤點。  
產出：AI 使用規範草案、Prompt Library、Skill 候選清單、Workflow 候選清單。

### 3.3 二日導入營：12 小時

適合：種子團隊、IT、流程 Owner。  
內容：L2 Skill 建置 + L3 n8n PoC + L4 Agent 任務卡。  
產出：3-5 個 Skill、1 個 n8n PoC、1 張 Hermes Agent 任務卡。

### 3.4 顧問診斷專案：2-4 週

適合：管理層、跨部門團隊。  
內容：問卷、訪談、As-Is、差距分析、To-Be、Roadmap。  
產出：AI 轉型診斷報告、ROI 追蹤矩陣、後續 SOW。

## 4. L1 Chat AI：OpenWebUI

### 4.1 課程目標

讓員工透過受控 AI 入口，安全使用 AI 完成日常知識工作，並建立企業 AI 使用邊界。企業版 L1 的重點是：每位員工用自己的帳號登入 OpenWebUI，擁有自己的聊天區域；Admin / IT 能管理帳號、角色、群組、模型、功能與資料權限。

OpenWebUI 企業啟用課的完整設計請見 `L1_OPENWEBUI_COURSE_PLAN.md`。

### 4.2 適合對象

- 全體員工。
- 部門種子人員。
- HR / 訓練單位。
- IT 與資訊安全窗口。

### 4.3 課前需求

| 項目 | 說明 |
| --- | --- |
| AI 入口 | OpenWebUI 或公司核准 AI 工具 |
| 帳號 | 每位學員有自己的測試帳號，不共用帳號 |
| Admin 帳號 | IT / HR / AI 管理者具備 Admin 權限 |
| 群組 / 權限 | 預先規劃部門群組、模型可見性、文件上傳、Web Search、分享政策 |
| 範例資料 | 低敏感文件、會議紀錄、Email 範例 |
| 規範草案 | 若沒有，課中建立第一版 |

### 4.4 上課內容

| 單元 | 時間 | 內容 | 方法 |
| --- | ---: | --- | --- |
| L1-L5 成熟度導入 | 30 分 | 說明 AI 從個人使用到 Agent Team 的演進 | 講授 |
| OpenWebUI 個人操作 | 45 分 | 每人登入、個人聊天區、選模型、對話、檔案、歷史紀錄 | Demo |
| OpenWebUI Admin 管理 | 60 分 | 帳號審核、角色、群組、權限、模型與功能控管 | Demo + 實作 |
| Prompt 基礎 | 60 分 | 角色、任務、背景、限制、輸出格式 | 講授 + 練習 |
| 日常工作實作 | 90 分 | Email、摘要、會議紀錄、主管報告 | 實作 |
| AI 使用規範 | 45 分 | 可輸入 / 禁止輸入 / 人工確認 | 工作坊 |
| 成果檢核 | 30 分 | 展示 Prompt 與輸出 | 小組回饋 |

### 4.5 課堂實作

- 寫一封客戶 Email 草稿。
- 每位學員用自己的帳號建立 2 個聊天主題。
- Admin 建立或審核測試帳號，並設定至少 1 個部門群組。
- 將會議紀錄整理成待辦事項。
- 將長文件整理成主管摘要。
- 建立 3 個個人常用 Prompt。
- 判斷 10 個資料案例是否可輸入 AI。

### 4.6 課後作業

- 每位學員提交 3 個工作 Prompt。
- 每個部門提交 5 個高頻工作清單。
- IT / Admin 提交帳號、群組、權限、模型可見性設定表。
- IT / HR 補完 AI 使用規範草案。

### 4.7 完成標準

| 標準 | 驗證方式 |
| --- | --- |
| 學員能使用 OpenWebUI 完成基本任務 | 課堂練習輸出 |
| 每位學員能用自己的帳號登入並建立個人聊天 | 登入截圖、個人聊天截圖 |
| Admin 能管理帳號、角色、群組、模型與權限 | Admin Panel 截圖、權限表 |
| 學員知道資料輸入邊界 | 資料案例判斷表 |
| 部門有初步 Prompt Library | Prompt 清單 |
| 公司有 AI 使用規範草案 | 規範文件 |

### 4.8 L1 Deliverables

- AI 使用規範草案。
- Prompt Library 第一版。
- OpenWebUI 使用流程。
- OpenWebUI Admin Runbook。
- 帳號 / 群組 / 權限 / 模型可見性設定表。
- 高頻工作清單。
- L2 Skill 候選清單。

### 4.9 Gate 1：能否進入 L2

通過條件：

- 有受控入口或核准工具。
- 每位學員有自己的帳號與個人聊天區。
- Admin 能審核帳號、設定角色、群組、模型與功能權限。
- 種子人員完成 L1 練習。
- 有資料可用 / 禁用規範。
- 至少整理出 10 個部門高頻工作。

## 5. L2 Skill AI：Antigravity / Claude Code / Codex

### 5.1 課程目標

將個人經驗、Prompt、SOP、模板與 Checklist 整理成部門可複用 Skill。若對象是 IT / 工程 / 數位團隊，L2 也包含 Antigravity Agentic Developer 訓練，讓 Agent 協助規劃、開發、測試、文件化與 GCP 部署 PoC。

Antigravity 工程訓練的完整設計請見 `L2_ANTIGRAVITY_COURSE_PLAN.md`。

### 5.2 適合對象

- 部門主管。
- 資深員工。
- 種子人員。
- 文件 / SOP Owner。
- IT 或數位轉型窗口。

### 5.3 課前需求

| 項目 | 說明 |
| --- | --- |
| 高頻工作清單 | 由 L1 產出 |
| SOP / 模板 | 客服、業務、營運、行政等文件 |
| 範例輸入輸出 | 過去成功案例 |
| 工具 | Antigravity / Claude Code / Codex |
| 工程課需求 | Antigravity、Chrome、gcloud、GCP 專案、範例 app 或文件 pipeline 題目 |

### 5.4 Skill 標準格式

| 欄位 | 說明 |
| --- | --- |
| Skill 名稱 | 清楚描述用途 |
| 使用情境 | 何時使用 |
| Input | 需要哪些資料 |
| Process | AI 應依照哪些步驟處理 |
| Output | 輸出格式 |
| Constraints | 不可做事項 |
| Quality Check | 驗收標準 |
| Owner | 維護負責人 |

### 5.5 上課內容

| 單元 | 時間 | 內容 | 方法 |
| --- | ---: | --- | --- |
| Skill AI 觀念 | 45 分 | 個人技巧如何變成部門能力 | 講授 |
| Skill 拆解方法 | 60 分 | Input / Process / Output / Constraints | 工作坊 |
| Antigravity 應用 | 60 分 | 任務規劃、文件整理、規格化 | Demo + 實作 |
| Antigravity 工程實作 | 120 分 | Agent Manager、Browser、App prototype、unit test、README | Demo + 實作 |
| Antigravity GCP 實作 | 180 分 | GCS、Pub/Sub、Cloud Run、Gemini、BigQuery pipeline PoC | 工程班選修 |
| Claude Code 應用 | 60 分 | 文件、規格、程式與知識工作輔助 | Demo + 實作 |
| Codex 應用 | 60 分 | 程式、資料處理、文件自動化 | Demo + 實作 |
| Skill Library | 45 分 | 版本、Owner、命名、品質檢查 | 講授 |
| Skill 實作 | 120 分 | 每組建立 1-2 個 Skill | 實作 |
| L2-to-L3 Bridge | 120 分 | Trigger、Input / Output schema、n8n node map、人工 Gate、Log、錯誤處理 | 工作坊 |
| 成果評審 | 60 分 | 非原作者測試 Skill | Peer Review |

### 5.6 課堂實作

建議依產業選擇：

- 研發製造業：8D / 5Why Skill、ERP 異常訂單 Skill、SOP 摘要 Skill。
- 醫院：病患服務 FAQ Skill、掛號流程 Skill、會議紀錄 Skill。
- 行銷服務業：文案產生 Skill、提案產生 Skill、競品分析 Skill。
- B2B 業務：客戶研究 Skill、拜訪摘要 Skill、CRM 更新 Skill。
- IT / 工程：Antigravity app prototype Skill、unit test Skill、GCP serverless pipeline Skill。

### 5.7 課後作業

- 每部門提交 3-5 個 Skill。
- 每個 Skill 補上 Owner。
- 每個 Skill 完成至少 2 筆測試。
- 建立 Skill Library 第一版。
- 將至少 1 個 Skill 轉成 L3 Workflow Blueprint。
- 補上 trigger、sample payload、output schema、human gate、log 與錯誤處理。

### 5.8 完成標準

| 標準 | 驗證方式 |
| --- | --- |
| 至少產出 3-5 個 Skill | Skill Library |
| Skill 有完整 IPOC | Skill 模板 |
| 非原作者可使用 | 測試紀錄 |
| Skill 有 Owner 與版本 | Owner 表與版本紀錄 |
| Skill 可進入 L3 | Workflow Blueprint、sample payload、n8n node map |

### 5.9 L2 Deliverables

- Skill Library。
- Skill 標準模板。
- 3-5 個可用 Skill。
- Skill Owner 與版本表。
- Antigravity app prototype / test / docs artifacts。
- GCP Pipeline PoC 與部署驗證紀錄。
- L3 Workflow Blueprint。
- Trigger / Input / Output schema。
- n8n node map、human gate、log、error handling spec。
- L3 Workflow 候選清單。

### 5.10 Gate 2：能否進入 L3

通過條件：

- 至少 3 個 Skill 可被重複使用。
- 已選出 1-2 個可流程化場景。
- 已盤點所需系統與資料來源。
- 已定義 trigger、input/output schema、sample payload。
- 已完成 n8n node map、human gate、log 與錯誤處理草案。
- 已定義人工審核需求。

## 6. L3 Workflow AI：n8n

### 6.1 課程目標

用 n8n 串接 Gmail、Sheets、Notion、CRM、API、ERP 等系統，讓 AI 進入流程並完成可驗證 PoC。

TigerAI n8n 深度課程請見 `L3_N8N_TIGERAI_COURSE_PLAN.md`。L3 應從 L2 Workflow Blueprint 接手，並補上 Trigger、Credential、Data Tables、Sub-workflow、Execution Log、GitHub 備份、人工 Gate 與 L4 Workflow Contract。

### 6.2 適合對象

- IT。
- 流程 Owner。
- 部門種子人員。
- 數位轉型 / 自動化人員。

### 6.3 課前需求

| 項目 | 說明 |
| --- | --- |
| L2 Skill | 至少 1 個可被流程呼叫的 Skill |
| 系統清單 | Gmail、Sheets、Notion、CRM、API、ERP |
| 測試帳號 | 避免直接操作正式資料 |
| 測試資料 | 去識別化或低敏感資料 |
| 權限 | Credential、API Key、Webhook 權限 |

### 6.4 上課內容

| 單元 | 時間 | 內容 | 方法 |
| --- | ---: | --- | --- |
| n8n 基礎 | 60 分 | Trigger、Node、Credential、Execution | Demo |
| 資料流設計 | 45 分 | Input、Transform、AI、Output | 講授 |
| L2 Blueprint 接手 | 45 分 | trigger、I/O schema、sample payload、node map | 工作坊 |
| Gmail / Email | 60 分 | 收信、分類、摘要、回覆草稿 | 實作 |
| Webhook / LINE / Meta | 75 分 | LINE Bot、Facebook Webhook、YouTube 留言或外部平台事件 | 實作 |
| Sheets | 45 分 | 寫入紀錄、問卷計分、KPI | 實作 |
| Data Tables | 60 分 | 狀態管理、客服 FAQ、互動紀錄、黑白名單 | 實作 |
| Notion | 45 分 | 任務建立、知識庫、會議紀錄 | 實作 |
| CRM / API | 75 分 | 查詢客戶資料、Webhook、內部 API | Demo + 實作 |
| ERP 規劃 | 45 分 | 訂單、庫存、出貨、採購、財務資料 | 架構設計 |
| AI Node / RAG | 60 分 | 分類、摘要、資料查詢 | Demo |
| Gemini / 多模態 | 60 分 | 圖片、語音、影片、文件分析 | Demo |
| Sub-workflow | 60 分 | 模組化、重複使用、流程模板 | 實作 |
| 人工審核 | 45 分 | Human-in-the-loop、Gate、通知 | 實作 |
| Log / Error | 45 分 | 錯誤通知、重試、fallback | 實作 |
| GitHub 備份 | 45 分 | Workflow / Credential 備份與版本治理 | 實作 |
| PoC 實作 | 180 分 | 小組完成 1 個 Workflow | 實作 |

### 6.5 課堂實作

標準 PoC：

> Email / 表單進件 → AI 分類 → 查資料 → 產生摘要 → 人工審核 → 寫入 Sheets / Notion → 通知 Owner

依產業變形：

- 製造業：客訴信件 + CRM + ERP + QMS。
- 醫院：客服問題 + FAQ 知識庫 + 人工審核。
- 行銷服務業：客戶需求表 + CRM + 提案草稿。
- 財務：費用資料 + 差異分析 + 主管摘要。
- 客服：Facebook / LINE Webhook + Data Tables + AI 回覆草稿。
- HR：Gmail 履歷進件 + Gemini 篩選 + LINE / Email 通知。
- 行銷：商品圖 / 主題輸入 + 文案 / 圖片 / 影片生成 + 人工審核 + 多平台發布。

### 6.6 課後作業

- 完成 Workflow 流程圖。
- 匯出 n8n Workflow JSON。
- 完成測試資料與測試紀錄。
- 補上權限、Log、人工審核與錯誤處理。
- 補上 Data Tables / Sheets / DB Schema。
- 補上 Sub-workflow Library。
- 補上 GitHub 備份紀錄。
- 補上 L4 Hermes Agent 可呼叫的 Workflow Contract。

### 6.7 完成標準

| 標準 | 驗證方式 |
| --- | --- |
| Workflow 可執行 | n8n Execution Log |
| 至少串接 2-3 個系統 | 系統串接表 |
| 有人工審核節點 | 審核紀錄 |
| 有錯誤處理 | 失敗測試紀錄 |
| 有備份與版本治理 | GitHub backup commit |
| 可銜接 L4 | Workflow Contract |
| 可產出明確業務結果 | 測試輸出 |

### 6.8 L3 Deliverables

- n8n Workflow PoC。
- Workflow JSON。
- 系統串接表。
- Credential / 權限表。
- Data Tables / Sheets / DB Schema。
- Sub-workflow Library。
- Execution Log。
- 人工審核紀錄。
- GitHub Backup / 版本管理 SOP。
- L4 Workflow Contract。
- L4 Agent 任務候選清單。

### 6.9 Gate 3：能否進入 L4

通過條件：

- 至少 1 個 Workflow 可穩定執行。
- 有 Log、人工審核、錯誤處理。
- 有備份、版本治理與權限表。
- 已定義可被 Agent 呼叫的工具或 Workflow。
- 已完成 L4 Workflow Contract。
- 已定義 Agent 權限邊界。

## 7. L4 Auto Agentic AI：Hermes Agent

### 7.1 課程目標

設計可控、可驗證、可維運的 Hermes Agent，讓 Agent 能以 Wiki 作為長期記憶，呼叫 L2 Skill 與 L3 Workflow，完成資料吸收、分析、查詢、更新、提醒與回報，並保留人工 Gate。

L4 的完整課程設計請見 `L4_HERMES_AGENT_COURSE_PLAN.md`。本節保留為 L1-L5 總課綱摘要。

### 7.2 適合對象

- 部門主管。
- 流程 Owner。
- IT。
- 種子人員。
- 知識工作者。
- 管理層助理 / PM。

### 7.3 課前需求

| 項目 | 說明 |
| --- | --- |
| L2 Skill | Agent 可呼叫的 Skill |
| L3 Workflow | Agent 可啟動的 Workflow |
| 任務場景 | 週報、客服、營運、業務、行政、研究、文件管理 |
| 知識底座 | `purpose.md`、`SCHEMA.md`、`INBOX.md`、`queue.md`、`watchlist.md`、`tasks.md`、`wiki/` |
| 技術底座 | Hermes Agent、五個核心 skills、tools、SQLite / FTS index、排程機制 |
| 權限表 | Agent 可做與不可做的事 |
| 人工 Gate | 何時需要人工確認 |

### 7.4 Agent 任務卡格式

| 欄位 | 說明 |
| --- | --- |
| Agent 名稱 | 角色名稱 |
| 任務目標 | 要完成什麼 |
| Input | 任務所需資料 |
| Tools | 可呼叫 Skill / Workflow / API |
| Process | 任務拆解步驟 |
| Output | 回報格式 |
| Constraints | 禁止事項 |
| Escalation | 轉人工條件 |
| Evidence | 執行紀錄、來源引用、Log、審核紀錄 |

### 7.5 Hermes Agent IPOE

| 類別 | 定義 |
| --- | --- |
| Input | 客戶任務、部門文件、PDF、SOP、FAQ、研究資料、API 回傳、n8n Workflow 結果、L2 Skill、`purpose.md`、`SCHEMA.md`、`watchlist.md`、`queue.md`、權限表 |
| Process | orient-first、bootstrap、ingest、source analysis、keyword extraction、index upsert、query、update、lint、autonomous discovery、briefing、graph synthesis、人工審核 |
| Output | Wiki pages、source analysis、concept/entity/claim pages、查詢回答、每日 briefing、待審 watchlist、任務追蹤清單、Agent 執行紀錄、改善建議 |
| Evidence | `hermes doctor` 結果、技能安裝清單、設定檔、Wiki 檔案、Log、SQLite 查詢、queue/watchlist/tasks、briefing email、n8n 執行紀錄、人工審核紀錄 |

### 7.6 上課內容

| 單元 | 時間 | 內容 | 方法 |
| --- | ---: | --- | --- |
| L4 定位 | 45 分 | Agent vs Chatbot vs Skill vs Workflow；L4 到 L5 的邊界 | 講授 |
| Hermes 架構 | 60 分 | Wiki、SQLite、skills、tools、runtime schema、policy、排程 | Demo |
| 任務拆解 | 60 分 | 目標、步驟、工具、輸出、風險、人工 Gate | 工作坊 |
| Knowledge Base | 60 分 | `purpose.md`、`SCHEMA.md`、INBOX、queue、watchlist、tasks | 實作 |
| Ingest 閉環 | 90 分 | 文件匯入、來源分析、keyword、index、log | 實作 |
| Query / Update | 75 分 | 引用回答、結果回寫、diff、人工審核 | 實作 |
| Tool Calling | 60 分 | 呼叫 Skill、n8n、API、DB | Demo |
| Briefing / Discovery | 75 分 | morning briefing、2h ping、watchlist、P2 queue | Demo |
| 權限與治理 | 60 分 | 最小權限、資料分級、人工 Gate、Log、fallback | 講授 |
| Agent 測試 | 120 分 | 設計並測試 1 個 Hermes Agent 閉環 | 實作 |

### 7.7 課堂實作

可選 Agent：

- 客服案件整理 Agent。
- 營運週報 Agent。
- 業務拜訪準備 Agent。
- 病患服務客服輔助 Agent。
- 行銷活動分析 Agent。
- 研發文獻 / 技術文件整理 Agent。

每組需完成：

- Hermes Agent 任務卡。
- L4 IPOE 表。
- `purpose.md` 與 `SCHEMA.md` 草稿。
- 一份文件 ingest 測試。
- 三個可追溯 query。
- 一份 briefing。
- Gate 4A-4E 驗收表。

### 7.8 課後作業

- 完成 Agent 任務卡。
- 完成 Agent 權限表。
- 完成 Agent 測試紀錄。
- 完成人工接手規則。
- 完成 Wiki / Log / Index / Briefing evidence。
- 選出 L5 Agent Team 候選任務。

### 7.9 完成標準

| 標準 | 驗證方式 |
| --- | --- |
| Agent 任務明確 | Agent 任務卡 |
| Agent 有知識底座 | `purpose.md`、`SCHEMA.md`、Wiki 結構 |
| Agent 可完成 ingest / query / update | source page、query record、update diff |
| Agent 可呼叫 Skill / Workflow | 工具呼叫紀錄、n8n execution log |
| Agent 權限邊界清楚 | 權限表 |
| 高風險任務可轉人工 | 人工接手紀錄 |
| Agent 輸出可追溯 | 執行 Log、SQLite 查詢、引用來源 |
| Agent 可營運 | briefing、watchlist、queue、排程表 |

### 7.10 L4 Deliverables

- Hermes Agent 任務卡。
- L4 IPOE 表。
- Hermes Agent 架構圖。
- 初始 Wiki：`purpose.md`、`SCHEMA.md`、INBOX、queue、watchlist、tasks。
- Agent 可用工具清單。
- Agent 權限表。
- Ingest / Query / Update 測試紀錄。
- Briefing 範本。
- Stage Gate 4A-4E 紀錄。
- 人工接手規則。
- 維運 Runbook。
- L5 Agent Team 候選情境。

### 7.11 Gate 4：能否進入 L5

通過條件：

- 至少 1 個 Hermes Agent 通過 Gate 4A-4E。
- Agent 可呼叫至少 1 個 Skill 與 1 個 Workflow。
- Agent 的 input、process、output、evidence 都可追溯。
- 有 Wiki 記憶、Log、索引、briefing 與人工 Gate。
- 已定義跨部門任務與 Agent 角色分工。

## 8. L5 Agentic Team AI：ClawTeam

> 📌 **引用聲明 / Citation Notice**
> 本節以 **ClawTeam** (HKUDS 開源、MIT License) 作為 L5 主要實作平台。上游 repo：<https://github.com/HKUDS/ClawTeam>。完整引用、授權條款與深度課綱請見：
> [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md) 與 [`L5_CLAWTEAM_COURSE_PLAN.md`](L5_CLAWTEAM_COURSE_PLAN.md)
>
> This section adopts **ClawTeam** (open-sourced by HKUDS under the MIT License) as the L5 implementation platform. Upstream: <https://github.com/HKUDS/ClawTeam>. Full citation, license terms, and detailed syllabus:
> [`90_References/CLAWTEAM_REFERENCE.md`](../90_References/CLAWTEAM_REFERENCE.md) and [`L5_CLAWTEAM_COURSE_PLAN.md`](L5_CLAWTEAM_COURSE_PLAN.md)

### 8.1 課程目標

設計多 Agent 協作模式，讓不同角色 Agent 共同完成跨部門企業級任務。ClawTeam 提供五層架構 (Team / Workspace / Task / Inbox / Transport)，搭配 git worktree 隔離與 CLI 編排，使任何 CLI agent (Claude Code / Codex / Gemini …) 都可被組成自主團隊。

### 8.2 適合對象

- 管理層。
- 跨部門主管。
- PM / 專案管理。
- IT / AI Center。
- 具備 L4 基礎的種子團隊。

### 8.3 課前需求

| 項目 | 說明 |
| --- | --- |
| L4 Agent | 至少 1 個受控 Agent |
| 跨部門任務 | 新產品、品質改善、客戶經營、營運分析 |
| Agent 角色 | 市場、產品、行銷、客服、財務、整合 |
| 資料源 | CRM、ERP、Sheets、Notion、API |
| 人工 Gate | 管理層或專案 Owner 審核 |

### 8.4 Agent Team 標準格式

| 欄位 | 說明 |
| --- | --- |
| Team 任務 | 要完成的跨部門任務 |
| Agent 角色 | 各 Agent 負責內容 |
| Input | 各 Agent 需要資料 |
| Process | 任務分派、協作、整合 |
| Output | 各 Agent 與最終輸出 |
| Reviewer | 審核角色 |
| Human Gate | 人工決策點 |
| KPI | 效益衡量 |

### 8.5 上課內容

> 本節為總綱摘要；完整 13 單元、ClawTeam CLI 操作、三大在地化情境 (製造業 / 醫院 / 零售) 請見 [`L5_CLAWTEAM_COURSE_PLAN.md`](L5_CLAWTEAM_COURSE_PLAN.md)。
> This section is a summary; for the full 13-module syllabus, ClawTeam CLI hands-on, and three localized scenarios (manufacturing / hospital / retail), see [`L5_CLAWTEAM_COURSE_PLAN.md`](L5_CLAWTEAM_COURSE_PLAN.md).

| 單元 | 時間 | 內容 | 方法 |
| --- | ---: | --- | --- |
| Multi-Agent 觀念 | 45 分 | Solo 🤖 → Swarm 🦞🤖🤖🤖；ClawTeam 三大原始情境 (AutoResearch / SWE / Hedge Fund) | 講授 |
| ClawTeam 架構導讀 | 45 分 | Team / Workspace / Task / Inbox / Transport 五層；git worktree 隔離 | 講授 |
| 環境安裝與 Profile | 45 分 | `pip install clawteam`、`clawteam profile wizard/test/doctor` | 上機 |
| 角色設計 | 60 分 | Agent 角色卡：市場、產品、行銷、客服、財務、整合 | 工作坊 |
| 任務分派 (Task CLI) | 75 分 | `task create --blocked-by`、依賴鏈、`task wait` | 上機 |
| Inbox 與 Broadcast | 60 分 | 點對點 vs 廣播、訊號匯合 (Hedge Fund 模式) | 上機 |
| Board 監看 | 45 分 | `board show/live/attach/gource/serve` | 上機 |
| 輸出整合 | 60 分 | 衝突偵測 (`context conflicts`)、整合報告 | 實作 |
| Reviewer / Critic | 45 分 | 品質檢查、風險檢查、Human Gate | 講授 |
| 治理與 ROI | 45 分 | 權限 (v0.6 roadmap)、Log、Stage Gate、KPI | 講授 |
| Team 演練 | 150 分 | 完成 1 個 Agent Team 案例 (含 `board show` + `task list` 截圖) | 實作 |

### 8.6 課堂實作

可選 Agent Team：

- 新產品上市 Agent Team。
- 品質改善 Agent Team。
- 客戶經營 Agent Team。
- 病患服務改善 Agent Team。
- 年度營運規劃 Agent Team。

### 8.7 課後作業

- 完成 Agent Team 角色卡。
- 完成任務分派表。
- 完成最終輸出模板。
- 完成 Reviewer / Human Gate 設計。
- 完成 ROI 指標。

### 8.8 完成標準

| 標準 | 驗證方式 |
| --- | --- |
| Agent 角色清楚 | 角色卡 |
| 任務可分派 | 任務分派表 |
| 各 Agent Input / Output 清楚 | IPOE 表 |
| 有整合與審核機制 | 整合報告與 Reviewer 設計 |
| 有 ROI 指標 | KPI 表 |

### 8.9 L5 Deliverables

- ClawTeam 角色卡。
- 多 Agent 任務分派表。
- Agent Team IPOE 表。
- 整合報告模板。
- Reviewer / Human Gate 設計。
- ROI 追蹤表。

### 8.10 Gate 5：L5 完成標準

通過條件：

- 至少完成 1 個 Agent Team 情境設計。
- 每個 Agent 有角色、Input、Output、限制。
- 有整合 Agent 或整合流程。
- 有 Reviewer / Human Gate。
- 有 ROI 與治理設計。

## 9. L1-L5 課程完成總控制表

| 等級 | 課程完成證據 | 可驗證 Deliverables | 是否可進下一級 |
| --- | --- | --- | --- |
| L1 | 課堂練習、Prompt、使用規範 | AI 使用規範、Prompt Library、L2 候選清單 | Gate 1 通過 |
| L2 | Skill 測試、Owner、版本 | Skill Library、3-5 個 Skill、L3 候選流程 | Gate 2 通過 |
| L3 | Workflow 執行、Log、審核 | n8n Workflow JSON、系統串接表、Execution Log | Gate 3 通過 |
| L4 | Agent 測試、工具呼叫、權限 | Hermes Agent 任務卡、權限表、測試紀錄 | Gate 4 通過 |
| L5 | Agent Team 演練、整合報告 | ClawTeam 角色卡、任務分派表、ROI 表 | Gate 5 通過 |

## 10. 講師交付檢查表

| 項目 | 說明 | 是否完成 |
| --- | --- | --- |
| 課前問卷完成 | 10 題或 25 題 | `[ ]` |
| 公司屬性調查完成 | 產業、部署、系統、資料敏感度 | `[ ]` |
| 課程比例確認 | L1-L5 比例 | `[ ]` |
| 課程案例確認 | 對應產業場景 | `[ ]` |
| 實作資料準備 | 低敏感或去識別資料 | `[ ]` |
| 學員分組完成 | 部門 / 角色 / 技術能力 | `[ ]` |
| Deliverables 收齊 | Prompt、Skill、Workflow、Agent、Roadmap | `[ ]` |
| Stage Gate 評估完成 | Gate 1-5 | `[ ]` |
| 課後顧問報告輸入完成 | 可納入診斷報告 | `[ ]` |
