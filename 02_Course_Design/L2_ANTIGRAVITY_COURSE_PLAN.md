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
- agency-agents（msitarzewski，MIT License）：144+ 個 agent persona 定義庫，支援 Antigravity / Claude Code / Cursor  
  `https://github.com/msitarzewski/agency-agents`  
  引用與授權說明見 [`../90_References/AGENCY_AGENTS_REFERENCE.md`](../90_References/AGENCY_AGENTS_REFERENCE.md)

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

L2 課程必須分成「上半堂產生 Skill」與「下半堂銜接 L3」。如果 L2 只做到 Skill Library，成果會停在文件或程式碼；下半堂要把 Skill 轉成 n8n 可接手的 Workflow Blueprint。

| 時段 | 核心任務 | 產出 |
|---|---|---|
| 上半堂 | 建立 Business Skill 或 Antigravity engineering artifact | Skill、app prototype、test、README、GCP PoC |
| 下半堂 | 將 Skill 包裝成 L3 n8n 可串接的流程規格 | Trigger、I/O schema、node map、human gate、log、test payload |

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

目標：上午讓學員能用 Agent 建立可運行 app、文件與測試；下午將成果轉成 L3 Workflow Blueprint。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 60 分 | Web research task | 讓 Agent 擷取網站資料並摘要 | Research artifact |
| 90 分 | Flask app generation | 產生技術活動網站或部門內部工具 | Flask app |
| 60 分 | Iteration | 新增功能、修改需求、觀察 Agent 如何更新 plan | Change record |
| 60 分 | Unit test / docs | 產生測試、README、限制與維運文件 | Test suite、README |
| 90 分 | L2-to-L3 bridge | 將 app / Skill 定義成 n8n 可呼叫元件 | Workflow Blueprint |
| 60 分 | Input / Output contract | 定義 trigger、payload、output JSON、錯誤格式 | I/O schema |
| 60 分 | Human gate / log | 定義人工審核、通知、execution log、fallback | Gate / Log spec |
| 60 分 | Review | 非原作者用 payload 測試 Blueprint | Peer review |

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
| Day 2 AM | L2-to-L3 bridge | Trigger、I/O schema、n8n node map、human gate、log | Workflow Blueprint |
| Day 2 PM | Package | Skill 化、Runbook、Gate 2 驗收、L3/L4 候選 | L2 delivery package |

---

## 7. L2 下半堂：銜接 L3 Workflow Blueprint

### 7.1 下半堂目標

L2 下半堂的目標不是繼續美化 Skill，而是把 Skill 轉成 L3 可以直接開工的流程規格：

> 任何一個通過 L2 的 Skill，都必須能回答：由什麼事件觸發？吃什麼資料？輸出什麼 JSON？哪一步要人工審核？Log 存在哪裡？失敗時怎麼處理？n8n 要怎麼接？

### 7.2 L2-to-L3 Bridge 流程

| 步驟 | 問題 | 產出 |
|---|---|---|
| 1. 選 Skill | 哪個 Skill 最適合流程化？ | Workflow 候選卡 |
| 2. 定 Trigger | 由 Email、表單、Webhook、排程、檔案上傳或 CRM event 觸發？ | Trigger spec |
| 3. 定 Input | Skill 需要哪些欄位、檔案、系統資料？ | Input schema、sample payload |
| 4. 定 Process | n8n 要跑哪些 node？哪些步驟呼叫 AI / Skill / API？ | n8n node map |
| 5. 定 Output | 結果要寫到哪裡？Email、Sheets、Notion、CRM、ERP、DB？ | Output schema |
| 6. 定 Human Gate | 哪些情況要人審？誰審？多久內審？ | Human gate spec |
| 7. 定 Evidence | 如何證明流程有跑、AI 有引用、資料有寫入？ | Log / evidence spec |
| 8. 定 Error Handling | 失敗如何通知、重試、fallback、人工接手？ | Error handling spec |
| 9. 定 Gate 2 | 是否足以進 L3 實作？ | Gate 2 驗收表 |

### 7.3 Workflow Blueprint 標準格式

| 欄位 | 說明 |
|---|---|
| Workflow 名稱 | 要讓 L3 實作的流程名稱 |
| Business Owner | 流程業務負責人 |
| IT Owner | 系統 / API / 權限負責人 |
| Trigger | Email、Webhook、表單、排程、檔案、CRM / ERP event |
| Input Schema | 欄位、資料型別、必填、範例 |
| Skill / Agent Step | 要呼叫哪個 L2 Skill 或 Antigravity artifact |
| System Nodes | Gmail、Sheets、Notion、CRM、API、ERP、DB |
| Human Gate | 審核條件、審核人、審核輸入與輸出 |
| Output Schema | 輸出格式、寫入位置、通知方式 |
| Log / Evidence | n8n execution log、AI 輸入輸出、系統寫入紀錄 |
| Error Handling | 重試、通知、fallback、人工接手 |
| Test Payload | 至少 2 筆正常案例與 1 筆錯誤案例 |
| Gate 2 Result | Pass / Fail / 補件 |

### 7.4 下半堂實作題

| 類型 | L2 Skill | L3 Workflow Blueprint |
|---|---|---|
| 客服 | 客訴分類與回覆草稿 Skill | Gmail 觸發 → AI 分類 → CRM 查詢 → 人工審核 → 回覆草稿 |
| 業務 | 拜訪摘要 Skill | 會議紀錄上傳 → 摘要 → CRM 更新 → 下一步任務 |
| 營運 | ERP 異常訂單分析 Skill | 排程查 ERP → AI 分析 → Sheets 報表 → 主管通知 |
| 醫院 | FAQ 回覆草稿 Skill | 表單 / Email 觸發 → FAQ 查詢 → 風險標記 → 人工審核 |
| 工程 | Antigravity deployment validation Skill | Git / Webhook 觸發 → 測試 → 部署驗證 → Log / 報告 |
| 文件 | GCP document pipeline Skill | GCS 上傳 → Pub/Sub → Cloud Run → Gemini → BigQuery |

### 7.5 下半堂 Deliverables

- L3 Workflow 候選卡。
- Trigger spec。
- Input / Output schema。
- Sample payload：2 筆正常、1 筆錯誤。
- n8n node map。
- Human gate spec。
- Credential / API / 系統需求清單。
- Log / Evidence spec。
- Error handling spec。
- Gate 2 驗收表。

### 7.6 L2-B 下半段擴充：善用現成 Agent 庫（agency-agents）

> 引用：[`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents)（MIT License）。完整引用與授權說明見 [`../90_References/AGENCY_AGENTS_REFERENCE.md`](../90_References/AGENCY_AGENTS_REFERENCE.md)。

L2-B Agentic Developer 線的下半段，除了把 Skill 轉成 Workflow Blueprint，還要教學員一個關鍵觀念：**不是每個 Skill 都要從零寫。** 業界已有成熟的 agent persona 庫（如 agency-agents，144+ 個 agent 定義、12 大類），可作為 Skill 建置的起點。

#### 7.6.1 教學目標

完成本段後，學員應能：

1. 說明「自建 Skill」與「採用 + 客製現成 agent persona」的取捨。
2. 安裝 agency-agents 到 Antigravity / Claude Code（`./scripts/install.sh`，工具自動偵測）。
3. 瀏覽 12 大類（engineering / design / marketing / sales / product / testing 等）並挑出與企業情境相符的 agent。
4. 把選定的 agent persona **客製化**為企業專屬 Skill：改寫 mission、加入企業 SOP、設定 Review Policy、補上 IPOE。
5. 判斷哪些 agent 可直接用、哪些需大幅改寫、哪些不適用（避免「貼一個 persona 就當成組織能力」）。
6. 把客製後的 agent persona 納入 L2 Skill Library，並標註來源（agency-agents + 版本）與 Owner。

#### 7.6.2 上課內容（90 分）

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 20 分 | 現成 Agent 庫觀念 | 自建 vs 採用；agency-agents 的 12 類結構與授權（MIT） | 取捨判斷表 |
| 20 分 | 安裝與瀏覽 | install 腳本、工具偵測、依企業情境挑 agent | 候選 agent 清單 |
| 30 分 | 客製化實作 | 改 mission / 加 SOP / 設 Review Policy / 補 IPOE | 客製化 agent persona |
| 20 分 | 納入 Skill Library | 標註來源、版本、Owner、與 §8 Skill Library 對齊 | Skill Library 條目 |

#### 7.6.3 治理與紅線

- agency-agents 為 **第三方 MIT 內容**；客製後的企業 Skill 屬企業所有，但建議於 Skill 文件中標註原始來源。
- agent persona 內的指令仍須通過企業的 Terminal / Review / JavaScript 安全政策（見 §6.1）。
- 不可未經審查直接讓 agent persona 在生產環境執行；客製化後一律先過 Gate 2。
- persona 庫只是「起點」，不能取代 §7 的 L2→L3 Bridge — 真正的流程化仍須走 Workflow Blueprint。

#### 7.6.4 下半段 Deliverables（追加）

- agency-agents 安裝紀錄（工具偵測截圖）。
- 企業情境 × 候選 agent 對照表。
- 至少 2 個客製化後的 agent persona（含來源標註、IPOE、Owner）。
- 自建 vs 採用之取捨判斷表。

---

## 8. L2 Skill Library 設計

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
| Workflow Blueprint Skill | 將 L2 成果轉成 L3 規格 | Skill、trigger、系統、資料欄位 | n8n Workflow Blueprint |

---

## 9. Stage Gate 2 控制

| Gate | 檢查問題 | 必備 Evidence | 判定 |
|---|---|---|---|
| Gate 2A：工具可用 | Antigravity、Chrome、workspace、登入是否完成？ | 環境檢查表、截圖 | Pass / Fail |
| Gate 2B：治理可用 | Terminal、Review、JavaScript policy 是否符合公司風險？ | 權限設定表 | Pass / Fail |
| Gate 2C：開發閉環可用 | Agent 能否產生 app、修改、測試、文件化？ | App、README、test result、walkthrough | Pass / Fail |
| Gate 2D：L3 Blueprint 可用 | 是否有 trigger、I/O schema、node map、human gate、log、test payload？ | Workflow Blueprint、sample payload、系統需求清單 | Pass / Fail |
| Gate 2E：雲端 PoC 可用 | GCP pipeline 是否能部署並驗證？ | gcloud log、Cloud Run log、BigQuery result | Pass / Fail |
| Gate 2F：Skill 化可用 | 是否把流程沉澱成 Skill Library？ | Skill 文件、Owner、版本、測試紀錄 | Pass / Fail |

未通過 Gate 2A-2C 時，不建議進入 L3 Workflow。未通過 Gate 2D 時，代表 L2 下半堂沒有完成銜接，不應開 L3 實作。未通過 Gate 2E 時，可進入一般 L3，但不建議進入雲端部署型 PoC。未通過 Gate 2F 時，代表課程成果尚未形成組織能力。

---

## 10. Deliverables

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
| L3 Workflow Blueprint | trigger、I/O schema、node map、human gate、log、test payload | L3 講師 / IT 可直接開工 |
| L3 / L4 候選清單 | 可串 n8n 或 Hermes Agent 的能力 | Roadmap 審核 |

---

## 11. 與 L3 / L4 的銜接

L2 Antigravity 訓練完成後，應自然接到：

- L3 n8n：把 Antigravity 產出的 app、API、GCP pipeline、測試流程接進 Workflow。
- L4 Hermes Agent：讓 Hermes Agent 可呼叫 L2 Skill、讀取工程文件、追蹤部署 evidence、產生 briefing。

L2 的重點不是直接變成正式上線專案，而是把工程能力與開發流程變成可複用、可審查、可驗證的 Skill。真正跨系統流程由 L3 承接，持續營運與任務代理由 L4 承接。
