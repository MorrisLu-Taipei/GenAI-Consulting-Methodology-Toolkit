# L2 Antigravity Agentic Developer 課程規劃

版本：v1.0  
作者：Morris  
適用層級：L2 Skill AI  
參考課程：

- Google Codelab：開始使用 Google Antigravity  
  `https://codelabs.developers.google.com/getting-started-google-antigravity?hl=zh-tw`
- Google Codelab：使用 Google Antigravity 建構  
  `https://codelabs.developers.google.com/building-with-google-antigravity?hl=zh-tw`
- Google Codelab：使用 Antigravity 建構及部署至 Google Cloud  
  `https://codelabs.developers.google.com/build-and-deploy-gcp-with-antigravity?hl=zh-tw`

---

## 1. L2 重新定位

原本 L2 的定位是把 Prompt、SOP、模板、Checklist 整理成部門可複用 Skill。加入 Google Antigravity 三套 codelab 後，L2 可以再拆成兩條訓練線：

| 訓練線 | 對象 | 目標 |
|---|---|---|
| L2-A Business Skill AI | 一般部門、PM、營運、客服、業務、HR | 把工作經驗、SOP、Prompt 變成可複用 Skill |
| L2-B Agentic Developer AI | IT、工程、數位轉型、資料團隊 | 用 Antigravity 讓 Agent 協助規劃、開發、測試、文件化與雲端部署 |

這三套 Google codelab 應放在 L2-B。它們不是單純教 IDE 操作，而是訓練學員如何把「開發工作」變成可被 Agent 協助、可被審查、可留下構件與 evidence 的工程技能。

---

## 2. 三套 Codelab 對應到 L2 能力

| Codelab | L2 能力 | 課程用途 | 產出 |
|---|---|---|---|
| 開始使用 Google Antigravity | Agentic IDE 基礎與治理 | 安裝、設定、Agent Manager、Editor、Browser、權限與審查政策 | Antigravity 操作設定表、治理設定截圖 |
| 使用 Google Antigravity 建構 | Agent 協助開發與測試 | 網頁研究、Flask app、Pomodoro app、單元測試、README / docs | App 原型、測試紀錄、Walkthrough artifact |
| 使用 Antigravity 建構及部署至 Google Cloud | Agent 協助雲端架構與部署 | GCS、Pub/Sub、Cloud Run、Gemini、BigQuery、gcloud、驗證 | Serverless pipeline PoC、部署紀錄、GCP 驗證截圖 |

---

## 3. 課程目標

完成本課程後，學員應能：

1. 說明 Antigravity 與傳統 IDE / coding assistant 的差異。
2. 設定 Agent 的終端機執行政策、Review Policy、JavaScript 執行政策與安全模式。
3. 使用 Agent Manager 管理 workspace、task、implementation plan、walkthrough artifact。
4. 使用 Antigravity Browser 完成外部網頁資料擷取、互動與驗證。
5. 使用 Agent 產生可運行的應用程式原型。
6. 要求 Agent 產生 README、測試、文件與驗證證據。
7. 使用 Antigravity 規劃 GCP serverless 架構。
8. 產生並審查基礎設施指令碼、Cloud Run service、Dockerfile、requirements、部署步驟。
9. 用 GCS、Pub/Sub、Cloud Run、Gemini、BigQuery 完成文件處理 pipeline PoC。
10. 將課程成果整理成 L2 Skill Library，並輸出 L3 Workflow / L4 Agent 候選任務。

---

## 4. 課前條件

| 項目 | 最低要求 |
|---|---|
| 帳號 | 可登入 Antigravity 的 Google 帳戶；GCP 課程需可使用 Google Cloud 專案 |
| 本機環境 | 已安裝 Antigravity、Chrome、必要開發工具 |
| 工程基礎 | 能閱讀基本 Python、Flask、Shell、Docker 概念 |
| GCP 基礎 | GCP 版需已安裝並驗證 `gcloud CLI` |
| 治理共識 | 終端機執行、瀏覽器 JavaScript、Artifact 審查需採「要求審查」或「審查導向」 |
| 課程資料 | 企業可使用的範例需求、內部 app idea、文件 pipeline idea |

---

## 5. L2 Antigravity IPOE

| 類別 | 定義 |
|---|---|
| Input | 使用者需求、現有程式碼、SOP、網站資料、產品規格、測試案例、GCP 專案、gcloud 權限、資料處理需求 |
| Process | Agent planning、task list、implementation plan、code generation、browser verification、unit test generation、artifact review、cloud deployment、manual verification |
| Output | App 原型、Flask / Python 程式、README、單元測試、Walkthrough artifact、GCP setup script、Cloud Run service、Dockerfile、BigQuery dataset、部署驗證報告 |
| Evidence | Antigravity task artifact、implementation artifact、walkthrough artifact、Git diff、測試結果、瀏覽器驗證影片或截圖、gcloud log、Cloud Run log、BigQuery 查詢結果、人工審查紀錄 |

---

## 6. 完整課程版本

### 6.1 L2 Antigravity Foundation：3 小時

目標：建立 Antigravity 的操作、治理與 Agentic IDE 觀念。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 30 分 | L2 定位 | Business Skill AI vs Agentic Developer AI | L2 訓練分流圖 |
| 45 分 | 安裝與環境 | Antigravity、Chrome、登入、workspace | 環境檢查表 |
| 45 分 | Agent Manager / Editor | workspace、task、plan、artifact、editor | 操作截圖 |
| 45 分 | 安全與審查政策 | Terminal、Review、JavaScript、Safe Mode | 權限設定表 |
| 45 分 | Browser Agent | 開啟網頁、擷取資料、互動、驗證 | Browser 測試紀錄 |

### 6.2 L2 Antigravity Builder：1 天

目標：讓學員能用 Agent 建立可運行 app、文件與測試。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 60 分 | Web research task | 讓 Agent 擷取網站資料並摘要 | Research artifact |
| 90 分 | Flask app generation | 產生技術活動網站或部門內部工具 | Flask app |
| 60 分 | Iteration | 新增功能、修改需求、觀察 Agent 如何更新 plan | Change record |
| 90 分 | Productivity app | 產生 Pomodoro 或部門效率工具 | App prototype |
| 90 分 | Unit test | 針對既有邏輯產生企業級單元測試 | Test suite |
| 60 分 | Docs | 產生 README、使用說明、限制與維運文件 | README / docs |
| 60 分 | Review | 非原作者測試 app 與文件 | Peer review |

### 6.3 L2 Antigravity GCP：1 天

目標：讓工程 / IT 團隊能用 Antigravity 規劃與部署 GCP serverless PoC。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 60 分 | GCP readiness | 專案、計費、gcloud、權限、區域 | GCP 檢查表 |
| 75 分 | Architecture planning | GCS、Pub/Sub、Cloud Run、Gemini、BigQuery | 架構計畫 |
| 90 分 | IaC / setup script | 產生 `setup.sh`、啟用 API、建立資源 | setup script |
| 90 分 | Cloud Run service | Python / Flask service、Dockerfile、requirements | Cloud Run app |
| 60 分 | Gemini integration | 文件分析、metadata extraction、分類或翻譯 | AI processing spec |
| 60 分 | Pipeline deployment | 部署 Cloud Run、設定 trigger、BigQuery streaming | 部署紀錄 |
| 60 分 | Validation | 上傳測試檔、查 Cloud Run log、查 BigQuery | 驗證報告 |
| 45 分 | Security extension | DLQ、Secret Manager、Eventarc、成本控管 | 後續改善清單 |

### 6.4 L2 Antigravity Enterprise Lab：2 天

目標：用企業自帶題目，做出可交付的工程 Skill 與 PoC。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| Day 1 AM | Use case selection | 選 1 個內部 app 或文件 pipeline | Use case brief |
| Day 1 PM | Build | Agent planning、coding、testing、docs | App / pipeline prototype |
| Day 2 AM | Deploy / integrate | 本機或 GCP 部署、API / DB / Workflow 接點 | Deployment evidence |
| Day 2 PM | Package | Skill 化、Runbook、Gate 2 驗收、L3/L4 候選 | L2 delivery package |

---

## 7. L2 Skill Library 設計

這三套課不能只當作一次性練習，應沉澱成可複用 Skill。

| Skill | 使用情境 | Input | Output |
|---|---|---|---|
| Antigravity Workspace Setup Skill | 新專案開始前 | 專案名稱、repo、權限模式 | workspace 設定與治理表 |
| Agent Planning Skill | 需求轉任務 | 使用者需求、限制、技術棧 | task list、implementation plan |
| Web Research Skill | 擷取網站資料 | URL、問題、欄位 | research summary、來源紀錄 |
| App Prototype Skill | 產生小型 app | 功能需求、UI 需求、資料模型 | app prototype、README |
| Unit Test Skill | 補測試 | 程式碼、業務規則 | test suite、coverage notes |
| GCP Serverless Pipeline Skill | 文件處理 pipeline | GCP 專案、檔案來源、metadata 欄位 | GCS / Pub/Sub / Cloud Run / BigQuery PoC |
| Deployment Validation Skill | 驗證部署 | 測試檔、部署 URL、log | validation report |

---

## 8. Stage Gate 2 控制

| Gate | 檢查問題 | 必備 Evidence | 判定 |
|---|---|---|---|
| Gate 2A：工具可用 | Antigravity、Chrome、workspace、登入是否完成？ | 環境檢查表、截圖 | Pass / Fail |
| Gate 2B：治理可用 | Terminal、Review、JavaScript policy 是否符合公司風險？ | 權限設定表 | Pass / Fail |
| Gate 2C：開發閉環可用 | Agent 能否產生 app、修改、測試、文件化？ | App、README、test result、walkthrough | Pass / Fail |
| Gate 2D：雲端 PoC 可用 | GCP pipeline 是否能部署並驗證？ | gcloud log、Cloud Run log、BigQuery result | Pass / Fail |
| Gate 2E：Skill 化可用 | 是否把流程沉澱成 Skill Library？ | Skill 文件、Owner、版本、測試紀錄 | Pass / Fail |

未通過 Gate 2A-2C 時，不建議進入 L3 Workflow。未通過 Gate 2D 時，可進入一般 L3，但不建議進入雲端部署型 PoC。未通過 Gate 2E 時，代表課程成果尚未形成組織能力。

---

## 9. Deliverables

| Deliverable | 說明 | 驗收方式 |
|---|---|---|
| Antigravity 操作設定表 | 安裝、workspace、Agent Manager、Editor、Browser | 課堂檢查 |
| Agent 權限與審查設定表 | Terminal、Review、JavaScript、Safe Mode | IT / 講師審核 |
| App Prototype | Flask / productivity app / 內部工具 | 可運行 demo |
| Unit Test Evidence | 測試檔、測試結果、修正紀錄 | test output |
| README / Docs | 使用說明、限制、維運方式 | 非原作者可閱讀 |
| GCP Pipeline PoC | GCS、Pub/Sub、Cloud Run、Gemini、BigQuery | 上傳檔案後 BigQuery 有結果 |
| Validation Report | 自動與手動驗證紀錄 | log、截圖、SQL 查詢 |
| L2 Skill Library | 3-5 個工程 Skill | Owner、版本、測試紀錄 |
| L3 / L4 候選清單 | 可串 n8n 或 Hermes Agent 的能力 | Roadmap 審核 |

---

## 10. 與 L3 / L4 的銜接

L2 Antigravity 訓練完成後，應自然接到：

- L3 n8n：把 Antigravity 產出的 app、API、GCP pipeline、測試流程接進 Workflow。
- L4 Hermes Agent：讓 Hermes Agent 可呼叫 L2 Skill、讀取工程文件、追蹤部署 evidence、產生 briefing。

L2 的重點不是直接變成正式上線專案，而是把工程能力與開發流程變成可複用、可審查、可驗證的 Skill。真正跨系統流程由 L3 承接，持續營運與任務代理由 L4 承接。

