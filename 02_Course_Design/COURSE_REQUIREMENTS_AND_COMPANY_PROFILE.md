# 課程需求清單與公司屬性調查

更新日期：2026-05-13

## 1. 使用目的

本文件用來補強 AI 成熟度課程設計。

課程不能只依工具安排，也不能只依客戶主觀想學什麼來安排。每一次課程設計都應該同時參考：

1. L1-L5 各成熟度的需求清單。
2. 客戶公司屬性與產業型態。
3. 客戶適合的 AI 部署模式：雲 AI、Hybrid、全地端。
4. 客戶目前系統條件：Gmail、Sheets、Notion、CRM、API、ERP、資料庫、內部系統。
5. 客戶風險條件：資安、個資、商業機密、法規、IT 維運能力。

最後目標是讓課程配置不只是「教工具」，而是對準客戶真正可落地的 AI 轉型路徑。

## 2. L1-L5 課程需求清單

### 2.1 L1 Chat AI：OpenWebUI

#### 適合客戶狀態

- 員工尚未大量使用 AI。
- 公司想先建立安全的 AI 使用入口。
- 管理層希望先提升個人效率。
- IT 希望集中管理模型與使用規範。

#### 需求清單

- 是否需要公司內部統一 AI 入口？
- 是否需要帳號、權限、模型管理？
- 是否需要每位員工用自己的帳號登入，而不是共用帳號？
- 是否需要每位員工有自己的聊天歷史、資料夾與個人 Prompt？
- 是否需要 Admin 審核新帳號、設定角色、群組與部門權限？
- 是否需要限制文件上傳、Web Search、API Keys、Tools、聊天分享？
- 是否有資料不可上傳公有雲的限制？
- 是否需要建立 AI 使用規範？
- 是否需要 Prompt 基礎訓練？
- 是否需要部門常用情境範本？

#### 課程重點

- OpenWebUI 個人使用：登入、個人聊天區、聊天歷史、資料夾、模型選擇。
- OpenWebUI Admin：帳號審核、角色、群組、權限、模型與功能控管。
- Prompt 基礎。
- 企業 AI 使用規範。
- 文件摘要、會議摘要、Email 草稿、報告初稿。
- AI 使用邊界與資料安全。

#### 建議產出物

- 個人高頻工作 Prompt。
- 部門常用 Prompt 範本。
- 帳號 / 群組 / 權限 / 模型可見性設定表。
- OpenWebUI Admin Runbook。
- AI 使用注意事項。
- L2 Skill 候選清單。

### 2.2 L2 Skill AI：Antigravity / Claude Code / Codex

#### 適合客戶狀態

- 已有人會用 AI，但方法散落在個人。
- 部門有 SOP、模板、文件或經驗需要沉澱。
- 新人訓練依靠資深同仁口傳。
- 希望把 Prompt、流程、文件變成可複用 Skill。
- IT / 工程團隊希望用 Antigravity 建立 app prototype、測試、文件與 GCP pipeline PoC。

#### 需求清單

- 哪些高頻工作最依賴資深人員？
- 哪些工作可以被整理成 SOP、Checklist、Template？
- 是否已有部門知識庫？
- 是否需要建立 Skill Library？
- 是否需要讓非工程部門也能維護 Skill？
- 是否需要將文件、程式、流程規格化？
- 是否需要 Antigravity Agentic Developer 訓練？
- 是否需要用 Agent 產生 app prototype、unit test、README 或部署腳本？
- 是否具備 GCP 專案、gcloud 權限與雲端部署需求？
- 產出的工程 artifact 是否要成為 L3 Workflow 或 L4 Hermes Agent 可呼叫能力？
- 哪些 L2 Skill 要在下半堂轉成 L3 Workflow Blueprint？
- 觸發條件、輸入欄位、輸出格式、人工審核與 Log 是否已定義？

#### 課程重點

- Skill 的定義與設計方法。
- Prompt、SOP、Template、Checklist 結構化。
- Antigravity / Claude Code / Codex 的 Skill 建置應用。
- Antigravity Agentic IDE：Agent Manager、Editor、Browser、權限與審查政策。
- Antigravity Builder：App prototype、unit test、README、walkthrough artifact。
- Antigravity GCP：GCS、Pub/Sub、Cloud Run、Gemini、BigQuery pipeline PoC。
- L2-to-L3 Bridge：將 Skill 轉成 trigger、input/output schema、n8n node map、human gate、log、error handling。
- 部門 Skill Library 管理。
- Skill 版本管理與驗收標準。

#### 建議產出物

- 部門 Skill 清單。
- 3-5 個可展示 Skill。
- Skill 標準模板。
- Antigravity app prototype、測試紀錄與文件 artifact。
- GCP serverless pipeline PoC 與部署驗證紀錄。
- L3 Workflow Blueprint。
- Trigger / I/O schema / sample payload。
- n8n node map、human gate、log、error handling spec。
- Skill 維護規則。
- L3 Workflow 候選清單。

### 2.3 L3 Workflow AI：n8n

#### 適合客戶狀態

- 部門已有 Skill 或 SOP，但仍需要人工搬資料。
- 工作流程橫跨多個系統。
- 客戶資料、信件、表格、任務、ERP 資料分散。
- 希望讓 AI 進入流程，而不是只回答問題。

#### 需求清單

- 是否使用 Gmail 或其他企業信箱？
- 是否使用 Google Sheets 或 Excel 作為作業表？
- 是否使用 Notion 作為任務或知識庫？
- 是否有 CRM 系統？
- 是否有 ERP 系統？
- 是否有內部 API 可串接？
- 是否需要串 LINE、Facebook、YouTube、Meta、GCS、GitHub 等平台？
- 是否有資料庫或向量資料庫？
- 是否需要 n8n Data Tables 保存狀態或互動紀錄？
- 是否需要 Sub-workflow 建立可重複使用的流程模板？
- 是否需要 Workflow / Credential 備份到 GitHub 或內部版本庫？
- 哪些流程有固定觸發條件？
- 哪些流程需要人工審核？
- 哪些流程失敗時需要通知或重試？

#### 課程重點

- n8n 基礎。
- Trigger、Webhook、Credential、Node。
- Gmail、Sheets、Notion、CRM、API、ERP 串接。
- LINE、Facebook、YouTube、Webhook、Data Tables 串接。
- 資料清理與格式轉換。
- Gemini、AI Node、RAG、多模態應用。
- Sub-workflow 模組化。
- 人工審核節點。
- GitHub 備份、Credential 管理、錯誤處理、Log 與維運。

#### 建議產出物

- 1-2 個 Workflow PoC。
- 系統串接需求清單。
- 權限與 Credential 清單。
- Data Tables / Sheets / DB Schema。
- Sub-workflow Library。
- 人工審核與例外處理規則。
- GitHub Backup / 版本管理 SOP。
- L4 Workflow Contract。
- L4 Agent 任務候選清單。

### 2.4 L4 Auto Agentic AI：Hermes Agent

#### 適合客戶狀態

- 已有可呼叫的 Skill 或 Workflow。
- 主管希望 AI 能自動拆解任務。
- 使用者不想知道每個系統怎麼操作，只想下達任務。
- 需要 AI 協助分析、彙整、執行、回報。
- 需要把文件、SOP、研究、FAQ、任務與 briefing 變成可持續累積的知識底座。

#### 需求清單

- 哪些角色需要個人或職能型 AI 助理？
- Agent 可以呼叫哪些 Skill？
- Agent 可以啟動哪些 n8n Workflow？
- Agent 的 Wiki 記憶要保存哪些內容？
- Agent 的 `purpose.md` 與 `SCHEMA.md` 如何定義？
- Agent 的 watchlist、queue、tasks、briefing 由誰維護？
- 哪些任務可以自動完成？
- 哪些任務必須人工確認？
- Agent 的權限邊界是什麼？
- Agent 的輸出格式與回報頻率是什麼？
- Agent 錯誤時誰負責處理？
- 哪些 evidence 可以證明 Agent 的輸出可追溯？

#### 課程重點

- Agentic AI 觀念。
- Hermes Agent 架構：Wiki、SQLite、skills、tools、runtime schema。
- Orient-first、ingest、query、update、lint、briefing、discovery。
- 任務拆解。
- Tool Calling。
- Skill 與 Workflow 調用。
- Agent 任務邊界。
- 權限、審核、Log、evidence、回報、失敗處理。

#### 建議產出物

- Agent 角色卡。
- L4 IPOE 表。
- 初始 Wiki 結構與 `purpose.md` / `SCHEMA.md`。
- Agent 任務清單。
- Agent 可用工具清單。
- Agent 權限表。
- Ingest / Query / Update 測試紀錄。
- Briefing 範本。
- Gate 4A-4E 驗收表。
- L5 Agent Team 候選情境。

### 2.5 L5 Agentic Team AI：ClawTeam

#### 適合客戶狀態

- 已有多個 Agent 或跨部門 AI 應用需求。
- 企業想讓 AI 支援複雜任務，例如新產品、策略、營運分析、跨部門專案。
- 管理層希望 AI 能形成多角色協作，而不是單點工具。

#### 需求清單

- 哪些任務需要多個專業角色協作？
- 需要哪些 Agent 角色？
- 每個 Agent 的輸入、輸出、權限是什麼？
- 哪個 Agent 負責整合？
- 哪些資料源需要共同存取？
- 如何做品質檢查？
- 如何做人工審核與最終決策？
- 如何追蹤 Agent Team 的 ROI？

#### 課程重點

- Multi-Agent 協作。
- Agent 角色分工。
- 任務分派。
- 輸出整合。
- 品質檢查。
- 高階主管情境演練。

#### 建議產出物

- Agent Team 情境設計。
- Agent 角色卡。
- 多 Agent 協作流程圖。
- 最終輸出模板。
- Agent Team 治理建議。

## 3. 公司屬性調查

### 3.1 基本公司資料

| 調查項目 | 說明 |
| --- | --- |
| 產業類型 | 研發製造業、行銷服務業、金融、醫療、教育、政府、零售、其他 |
| 員工人數 | 影響課程規模、帳號管理、推廣節奏 |
| 部門結構 | 業務、客服、行銷、營運、研發、製造、財務、人資、IT |
| 主要系統 | Gmail、Google Workspace、Microsoft 365、Notion、CRM、ERP、MES、PLM、內部系統 |
| IT 團隊能力 | 是否能維運伺服器、Docker、API、資料庫、權限 |
| AI 使用現況 | 未使用、個人使用、部門使用、自動化流程、Agent |
| 管理層目標 | 效率、成本、品質、營收、創新、治理、資安 |

### 3.2 資料與風險屬性

| 調查項目 | 低風險 | 中風險 | 高風險 |
| --- | --- | --- | --- |
| 資料敏感度 | 公開資料、一般文件 | 客戶資料、內部 SOP | 研發機密、個資、財務、合約 |
| 法規要求 | 無特殊要求 | 有個資或合約限制 | 金融、醫療、政府、上市櫃高度控管 |
| 雲端政策 | 可使用公有雲 | 部分資料可上雲 | 禁止核心資料上雲 |
| 系統封閉度 | SaaS 工具為主 | 有部分內部系統 | ERP、MES、內網、舊系統為主 |
| IT 維運能力 | 無專職 IT | 有 IT 但資源有限 | 有基礎架構與資安團隊 |

### 3.3 產業 AI 搭配性

#### 研發製造業

常見特徵：

- ERP、MES、PLM、QMS、內部資料庫較多。
- 資料敏感度高，涉及 BOM、製程、品質、客戶規格、研發文件。
- 流程標準化程度較高，但系統較封閉。

適合優先場景：

- ERP 異常訂單分析。
- 品質問題摘要。
- SOP / WI 文件查詢。
- 設備維護紀錄整理。
- 研發文件摘要。
- 客訴與 8D / 5Why 分析。

建議導入節奏：

- 先做 L1 受控入口與 L2 知識沉澱。
- 再做 L3 內部系統或 ERP 的受控串接。
- L4/L5 必須強化權限、審核與稽核紀錄。

部署偏好：

- 多數偏向 Hybrid 或全地端。
- 若使用雲 AI，需先分級資料與遮罩敏感資訊。

#### 行銷服務業

常見特徵：

- 使用 Gmail、Sheets、Notion、CRM、社群、廣告平台較多。
- 資料流動快，內容產出需求高。
- 雲端 SaaS 接受度較高。

適合優先場景：

- 客戶提案生成。
- 市場與競品研究。
- 社群與廣告文案。
- 客戶會議摘要。
- CRM 商機更新。
- 活動成效報告。

建議導入節奏：

- L1 可快速普及。
- L2 優先沉澱文案、提案、研究、客服 Skill。
- L3 快速串接 Gmail、Sheets、Notion、CRM。
- L4/L5 可用於提案、行銷企劃、專案管理。

部署偏好：

- 多數可採雲 AI 或 Hybrid。
- 若處理客戶機密簡報或合約，需切換到 Hybrid 或私有模型。

#### 金融、醫療、政府與高敏感單位

常見特徵：

- 資料高度敏感。
- 權限、稽核、法規、資料留存要求高。
- 導入速度較慢，但治理需求明確。

適合優先場景：

- 內部知識查詢。
- 文件摘要。
- 表單與報告輔助。
- 非敏感資料流程自動化。
- 人工審核型 Agent。

建議導入節奏：

- 先做全地端或嚴格 Hybrid 架構。
- L1 需明確資料分級。
- L2 需建立可稽核 Skill Library。
- L3 需有完整 Log、權限與人工審核。
- L4/L5 以決策支援為主，不宜一開始完全自動決策。

部署偏好：

- 多數偏向全地端或嚴格 Hybrid。

## 4. AI 部署模式調查

### 4.1 雲 AI

#### 適合狀態

- 預算有限，希望快速開始。
- 資料敏感度低或可匿名化。
- 以行銷、文案、研究、一般知識工作為主。
- IT 維運能力有限。

#### 優點

- 成本最低。
- 啟動最快。
- 模型能力強。
- 維運負擔低。

#### 風險與限制

- 資料外流疑慮。
- 權限與稽核依賴供應商。
- 不適合處理核心機密資料。

#### 課程備註

- 可加重 L1、L2。
- L3 可先串 SaaS 工具。
- L4/L5 需明確限制可使用資料。

### 4.2 Hybrid：雲 + 地端

#### 適合狀態

- 有部分資料可上雲，部分資料必須留在內部。
- 希望兼顧模型能力與資料安全。
- 需要串接內部 ERP、CRM、資料庫或 API。
- 有基本 IT 維運能力。

#### 優點

- 彈性高。
- 可依資料敏感度分流。
- 成本與安全可取得平衡。
- 適合多數企業第一階段落地。

#### 風險與限制

- 架構設計較複雜。
- 需要資料分級與路由規則。
- 需要 Credential、權限、Log 管理。

#### 課程備註

- L1 需教資料分類。
- L2 需建立可控 Skill Library。
- L3 是重點，尤其是 n8n 串接與資料路由。
- L4/L5 可先從人工審核型任務開始。

### 4.3 全地端

#### 適合狀態

- 核心資料不得出公司。
- 有高度資安、法規、稽核要求。
- 有內部 IT 或基礎架構團隊。
- 需要私有模型、內網部署、地端 RAG。

#### 優點

- 資料掌控度最高。
- 符合高敏感場景。
- 可與內部系統深度整合。

#### 風險與限制

- 初期成本較高。
- 模型能力、硬體資源、維運能力是限制。
- 導入週期較長。

#### 課程備註

- L1 要導入 OpenWebUI 與私有模型使用規範。
- L2 要強化內部知識與文件治理。
- L3 需搭配內部 API、ERP、資料庫與權限。
- L4/L5 需有嚴格審核、Log、權限與 fallback 流程。

## 5. 課程配置判斷規則

### 5.1 先判斷成熟度，再判斷部署模式

同樣是 L3 n8n 課程，不同公司屬性會有不同教法：

- 雲 AI 客戶：重點是快速串接 Gmail、Sheets、Notion、CRM。
- Hybrid 客戶：重點是資料分級、SaaS 與內部 API 串接。
- 全地端客戶：重點是內網部署、ERP、DB、權限與稽核。

### 5.2 產業會影響課程案例

研發製造業：

- 案例應放在 ERP、品質、製程、SOP、客訴分析。
- L3/L4 課程要強調權限、內部系統與人工審核。

行銷服務業：

- 案例應放在提案、文案、CRM、社群、活動報告。
- L1/L2/L3 可以快速推進，L4/L5 可用於多角色企劃。

高敏感產業：

- 案例應避免敏感資料直接上雲。
- 課程要強調治理、資料分級、稽核、人工決策。

### 5.3 建議課程設計流程

1. 先做 AI 成熟度問卷。
2. 再做公司屬性調查。
3. 判斷部署模式：雲 AI、Hybrid、全地端。
4. 判斷產業案例方向。
5. 產出 L1-L5 課程比例。
6. 產出課程練習題與 PoC 題目。
7. 課後將產出物納入八階段顧問診斷報告。

## 6. 公司屬性調查題目草案

### 6.1 部署與資安

1. 公司是否允許員工使用公有雲 AI 工具處理工作資料？
2. 是否有資料不得離開公司內網？
3. 是否有個資、合約、研發、財務或客戶機密資料？
4. 是否已有資料分級制度？
5. 是否需要保留 AI 使用紀錄與稽核紀錄？
6. 是否有內部 IT 團隊可維護 Docker、資料庫、API 或伺服器？

### 6.2 系統與資料

1. 公司主要使用哪些協作工具？
2. 是否使用 Gmail 或 Microsoft 365？
3. 是否使用 Google Sheets、Excel 或內部報表系統？
4. 是否使用 Notion、Confluence、SharePoint 或內部知識庫？
5. 是否使用 CRM？
6. 是否使用 ERP、MES、PLM、QMS 或其他核心系統？
7. 是否有內部 API？
8. 是否有資料庫或資料倉儲？

### 6.3 產業與場景

1. 公司主要產業類型是什麼？
2. 哪些部門最需要 AI？
3. 哪些工作最重複？
4. 哪些工作最依賴資深人員？
5. 哪些流程最常出錯或延遲？
6. 哪些報告最耗時間？
7. 管理層最想看到哪種 ROI？

## 7. 顧問備註

- 客戶如果只想買課程，也要先做簡版公司屬性調查，避免課程案例不貼近。
- 雲 AI 最便宜，但不一定最適合所有企業。
- Hybrid 通常是多數企業最務實的第一階段選項。
- 全地端不是一開始就推薦給所有客戶，應該依資料敏感度、IT 能力與預算判斷。
- 研發製造業通常要更重視資料權限、ERP/MES/內部系統與審核流程。
- 行銷服務業通常可以更快從 L1/L2 推到 L3/L4，且更容易展示短期 ROI。
- 課程比例應該由「成熟度 + 公司屬性 + 部署模式 + 產業場景」共同決定。


