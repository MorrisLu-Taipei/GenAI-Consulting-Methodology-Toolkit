# L1-L5 課程模組矩陣

更新日期：2026-05-13

## 1. 課程設計原則

課程不是固定菜單，而是依「成熟度 + 公司屬性 + 部署模式 + 產業場景」配置。

每次課前應先完成：

1. AI 成熟度問卷。
2. 公司屬性調查。
3. 雲 AI / Hybrid / 全地端判斷。
4. 產業與部門場景選擇。
5. L1-L5 課程比例配置。

## 2. 課程產品包

| 產品包 | 時長 | 適合對象 | 主要目的 | 交付物 |
| --- | --- | --- | --- | --- |
| 半日體驗課 | 3 小時 | 初次接觸客戶、主管共識會 | 建立 L1-L5 共同語言與初步診斷 | 快速問卷、成熟度初判、課程建議 |
| 一日工作坊 | 6 小時 | 部門主管與種子人員 | 完成 L1-L2 能力建置與 L3 場景盤點 | Prompt、Skill 清單、Workflow 候選清單 |
| 二日導入營 | 12 小時 | 種子團隊、IT、流程 Owner | 完成 L2-L3 PoC，帶入 L4 Agent 設計 | Skill Library、n8n PoC、Agent 任務卡 |
| 顧問診斷專案 | 2-4 週 | 管理層、跨部門團隊 | 用八階段方法產出 AI 轉型診斷報告 | 診斷報告、Roadmap、ROI 與治理建議 |

## 3. L1 Chat AI：OpenWebUI

### 課程目標

讓員工透過受控 AI 入口完成高頻知識工作，並理解資料安全與使用邊界。企業版 L1 必須做到每位員工用自己的帳號登入、擁有自己的聊天區域，Admin 可管理帳號、角色、群組、模型、功能與權限。

### 課程大綱

1. AI 成熟度 L1-L5 總覽。
2. OpenWebUI 個人操作：登入、個人聊天區、聊天歷史、資料夾、模型選擇。
3. OpenWebUI Admin：帳號審核、角色、群組、權限、模型與功能控管。
4. Prompt 基礎：角色、任務、資料、格式、限制。
5. 文件摘要、Email 草稿、會議紀錄、報告初稿。
6. AI 使用規範：可輸入、不可輸入、需人工確認。

### 實作練習

- 產出一封客戶 Email 草稿。
- 每位學員用自己的帳號建立 2 個聊天主題。
- Admin 建立或審核測試帳號，並設定部門群組。
- 摘要一份會議紀錄。
- 將長文件整理成主管摘要。
- 建立個人常用 Prompt。

### 課後產出物

- 個人高頻 Prompt。
- 部門常用 Prompt 範例。
- 帳號 / 群組 / 權限 / 模型可見性設定表。
- OpenWebUI Admin Runbook。
- AI 使用規範草案。
- L2 Skill 候選清單。

### 講師備註

L1 課程要避免只教「好玩的 Prompt」。重點是讓客戶看到 AI 可以安全進入日常工作，並為 L2 Skill 化鋪路。若企業無法做到每人獨立帳號、個人聊天區與 Admin 權限控管，就不應大規模開放使用。完整 L1 設計請見 `L1_OPENWEBUI_COURSE_PLAN.md`。

## 4. L2 Skill AI：Antigravity / Claude Code / Codex

### 課程目標

把個人經驗、Prompt、SOP、模板、Checklist 整理成部門可複用 Skill；工程 / IT 團隊則用 Antigravity 建立 Agentic Developer Skill，讓 Agent 協助規劃、開發、測試、文件化與雲端部署。

### 課程大綱

1. Skill AI 的定義：從個人技巧到部門能力。
2. Skill 結構：目的、適用情境、輸入、步驟、輸出、驗收標準。
3. Antigravity Foundation：Agent Manager、Editor、Browser、權限與審查政策。
4. Antigravity Builder：App prototype、unit test、README、walkthrough artifact。
5. Antigravity GCP：GCS、Pub/Sub、Cloud Run、Gemini、BigQuery serverless pipeline PoC。
6. Claude Code：文件、規格、程式與知識工作輔助。
7. Codex：程式、資料處理、文件自動化與流程原型。
8. Skill Library 管理：版本、Owner、範例、品質檢查。
9. L2-to-L3 Bridge：trigger、input/output schema、n8n node map、human gate、log、error handling。

### 實作練習

- 建立一個「文案產生 Skill」。
- 建立一個「客戶會議摘要 Skill」。
- 建立一個「異常訂單分析 Skill」。
- 將既有 SOP 轉成 AI 可執行的 Skill 模板。
- 使用 Antigravity 建立一個 app prototype。
- 使用 Antigravity 產生 unit test、README 與 walkthrough evidence。
- 工程班可加做 GCP serverless pipeline PoC。
- 下半堂把 1 個 Skill 轉成 L3 Workflow Blueprint。
- 定義 sample payload、n8n node map、人工審核與 Log。

### 課後產出物

- 部門 Skill 清單。
- 3-5 個可展示 Skill。
- Skill 標準模板。
- Skill Library 維護規則。
- Antigravity app prototype / test / docs artifacts。
- GCP Pipeline PoC 與部署驗證紀錄。
- L3 Workflow Blueprint。
- Trigger / I/O schema / sample payload。
- n8n node map、human gate、log、error handling spec。
- L3 Workflow 候選清單。

### 講師備註

L2 是整套方案的樞紐。沒有 L2，L3 會變成只串工具；有 L2，Workflow 才能承載部門知識。L2 下半堂必須銜接 L3，把 Skill 轉成 Workflow Blueprint。若客戶是 IT、研發、軟體或數位團隊，應加入 `L2_ANTIGRAVITY_COURSE_PLAN.md`，把 Google Antigravity 三套 codelab 轉成工程 Skill 訓練。

## 5. L3 Workflow AI：n8n

### 課程目標

用 n8n 串接 Gmail、Sheets、Notion、CRM、API、ERP、LINE、Facebook、YouTube、Data Tables 等系統，讓 AI 開始進入流程並完成可驗證、可維運、可備份的任務。

### 課程大綱

1. n8n 核心概念：Trigger、Node、Credential、Webhook、Execution。
2. L2 Blueprint 接手：trigger、I/O schema、sample payload、node map。
3. Gmail / LINE / Facebook / YouTube / Webhook 串接。
4. Google Sheets / Data Tables / Notion 串接：資料紀錄、狀態管理、任務建立。
5. CRM / API / ERP 串接：客戶、訂單、庫存、出貨、採購、財務資料。
6. Gemini / AI Node / RAG / 多模態應用。
7. Sub-workflow 模組化與可重複流程模板。
8. GitHub 備份、Credential 管理、Execution Log。
9. 錯誤處理、人工審核、權限與維運。

### 實作練習

- Gmail 客訴信分類並寫入 Sheets。
- 表單填寫後自動建立 Notion 任務。
- CRM 客戶資料查詢後產生拜訪摘要。
- ERP 異常訂單資料轉成主管摘要。
- n8n 執行失敗時通知負責人。
- Facebook / LINE 客服 Webhook + Data Tables + AI 回覆草稿。
- HR 履歷篩選：Gmail + Gemini + LINE / Email 通知。
- Sub-workflow 模組化與 GitHub 備份。

### 課後產出物

- 1-2 個 n8n Workflow PoC。
- 系統串接需求清單。
- Credential 與權限清單。
- Data Tables Schema。
- Sub-workflow Library。
- 人工審核節點設計。
- GitHub Backup / 版本管理 SOP。
- L4 Workflow Contract。
- L4 Agent 任務候選清單。

### 講師備註

同樣是 L3，不同產業要換不同案例。行銷服務業可先用 SaaS、社群平台、Webhook 快速展示 ROI；客服可用 Facebook / LINE + Data Tables；HR 可用 Gmail + Gemini + 通知；研發製造業要優先處理 ERP、內部 API、資料權限與人工審核。完整 L3 設計請見 `L3_N8N_TIGERAI_COURSE_PLAN.md`。

## 6. L4 Auto Agentic AI：Hermes Agent

### 課程目標

讓 Hermes Agent 形成可持續運行的知識工作閉環：能讀取部門目的與 schema、吸收文件、建立 Wiki 記憶、呼叫 L2 Skill 與 L3 Workflow、產生 briefing，並用 evidence 與人工 Gate 驗證。

### 課程大綱

1. Agentic AI 觀念：Agent 與 Chatbot / Skill / Workflow 的差異。
2. Hermes 架構：Wiki、SQLite、skills、tools、runtime schema、policy。
3. Orient-first：Agent 開工前先讀目的、schema、INBOX、queue、watchlist、index、log。
4. Ingest / query / update：文件吸收、來源分析、引用回答、結果回寫。
5. Briefing / discovery：morning briefing、2h ping、watchlist、P2 queue。
6. Tool Calling：呼叫 Skill、n8n Workflow、API、資料庫。
7. Agent 任務卡：角色、權限、可用工具、限制、回報格式。
8. 人工審核、Stage Gate、Log、失敗處理與改善。

### 實作練習

- 設計「營運週報 Agent」。
- 設計「客服案件摘要 Agent」。
- 設計「業務拜訪準備 Agent」。
- 設計「研發文獻 / 技術文件整理 Agent」。
- 建立 `purpose.md` 與 `SCHEMA.md` 草稿。
- 匯入一份 PDF / SOP / FAQ，產生 source analysis 與 log。
- 產出一份 morning briefing。
- 讓 Agent 呼叫一個 n8n Workflow。

### 課後產出物

- Hermes Agent 角色卡。
- L4 IPOE 表。
- 初始 Wiki 結構。
- Agent 任務清單。
- Agent 可用工具清單。
- Ingest / Query / Update 測試紀錄。
- Briefing 範本。
- 權限與審核規則。
- Gate 4A-4E 驗收表。
- L5 Agent Team 候選情境。

### 講師備註

L4 不宜一開始承諾全自動決策。比較好的說法是「先讓 Agent 做準備、分析、整理、提醒、草稿與 briefing，關鍵決策、刪除、schema 變更與高風險更新保留人工 Gate」。完整 L4 設計請見 `L4_HERMES_AGENT_COURSE_PLAN.md`。

## 7. L5 Agentic Team AI：ClawTeam

### 課程目標

讓多個專業 Agent 組成 AI Team，協同完成跨部門企業級任務。

### 課程大綱

1. Multi-Agent 協作觀念。
2. Agent 角色設計：市場、產品、行銷、客服、財務、專案整合。
3. 任務分派與輸出整合。
4. 品質檢查：Reviewer、Critic、人工 Gate。
5. Agent Team 治理：權限、資料、Log、ROI。
6. 高階主管情境演練。

### 實作練習

- 新產品上市專案 Agent Team。
- 客戶經營策略 Agent Team。
- 營運異常分析 Agent Team。
- 年度規劃草案 Agent Team。

### 課後產出物

- ClawTeam 情境設計。
- Agent 角色卡。
- 多 Agent 協作流程圖。
- 最終輸出模板。
- Agent Team 治理建議。

### 講師備註

L5 的客戶語言要偏管理價值，不要陷入技術細節。重點是「AI Team 支援跨部門決策與執行前置作業」。

## 8. 課程比例配置

| 客戶狀態 | 建議比例 | 課程重點 |
| --- | --- | --- |
| AI 初學企業 | L1 40%、L2 35%、L3 20%、L4 5%、L5 0% | 建立入口、使用規範、Prompt 與 Skill |
| 已有個人使用 | L1 30%、L2 35%、L3 25%、L4 10%、L5 0% | 個人經驗變部門能力 |
| 已有部門 Skill | L1 15%、L2 30%、L3 40%、L4 10%、L5 5% | Skill 串 Workflow |
| 已有 Workflow | L1 5%、L2 20%、L3 35%、L4 30%、L5 10% | Workflow 升級 Agent |
| 已有 Agent 基礎 | L1 5%、L2 15%、L3 25%、L4 30%、L5 25% | Agent Team 與治理 |

## 9. 部署模式對課程的影響

| 部署模式 | 課程調整 |
| --- | --- |
| 雲 AI | 多放 L1/L2，案例用 Gmail、Sheets、Notion、CRM，快速展示效率 |
| Hybrid | 多放 L3，案例加入資料分級、SaaS + 內部 API、ERP、人工審核 |
| 全地端 | 多放治理、內部系統、地端模型、RAG、ERP/DB/API、Log 與稽核 |

## 10. 產業案例對應

| 產業 | 優先案例 | 建議重點 |
| --- | --- | --- |
| 研發製造業 | ERP 異常訂單、品質分析、SOP 查詢、客訴 8D/5Why | Hybrid / 全地端、L2-L3、權限與稽核 |
| 行銷服務業 | 提案、文案、競品分析、CRM 更新、活動報告 | 雲 AI / Hybrid、L1-L3 快速 PoC |
| 金融醫療政府 | 文件摘要、內部知識查詢、報告輔助、人工審核流程 | 全地端 / 嚴格 Hybrid、治理優先 |
| B2B 業務 | 客戶研究、拜訪摘要、商機更新、提案產出 | L1-L3、CRM 與 Email 串接 |
| IT / 系統部門 | API 串接、權限治理、Log、流程維運 | L3-L4、治理與維運 |
