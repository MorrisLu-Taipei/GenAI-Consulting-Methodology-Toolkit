# 案例控制表格：評估、L1-L5 IPOE、Evidence 與 Stage Gate

更新日期：2026-05-13

## 1. 使用目的

本文件提供顧問在每個客戶案例中可直接複製使用的控制表格。

控制表格用來確保案例不是只寫故事，而是能追蹤：

> 先經過哪些評估 → L1-L5 各自吃什麼 input → 做什麼 process → 產出什麼 output → 用哪些 evidence 證明 → 用 Stage Gate 判斷能不能進下一階段

每個客戶案例都應至少填完以下 7 張表：

1. Case Intake 控制表。
2. 評估活動控制表。
3. L1-L5 IPOE 控制表。
4. Evidence 控制表。
5. Stage Gate 控制表。
6. 風險與治理控制表。
7. Deliverables 驗收控制表。

## 2. Case Intake 控制表

| 欄位 | 填寫內容 | 範例 |
| --- | --- | --- |
| 客戶名稱 | `[客戶公司]` | ABC 醫院 |
| 產業 | `[產業]` | 醫療 |
| 員工 / 使用者規模 | `[人數]` | 1,500 人 |
| 主要部門 | `[部門]` | 客服、醫務行政、資訊室 |
| 主要系統 | `[系統]` | HIS、EMR、客服系統、Email |
| 資料敏感度 | `[低 / 中 / 高 / 極高]` | 極高 |
| 初步部署模式 | `[雲 AI / Hybrid / 全地端]` | 全地端或嚴格 Hybrid |
| 主要商業目標 | `[目標]` | 降低客服重複問題處理時間 |
| 主要風險 | `[風險]` | 個資外洩、錯誤醫療建議 |
| 第一波 PoC 候選 | `[場景]` | 病患服務 FAQ Workflow |

## 3. 評估活動控制表

| 評估階段 | 評估目的 | Input | 方法 | Output | Owner | Evidence | 狀態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 問卷診斷 | 判斷成熟度 | 10 題 / 25 題問卷 | 線上問卷 / 訪談填寫 | 成熟度初判 | 顧問 | 問卷原始資料、分數表 | `[ ]` |
| 公司屬性調查 | 判斷產業與部署模式 | 公司資料、系統清單 | 訪談 / 表單 | 公司屬性表 | 顧問 + 客戶窗口 | 調查表 | `[ ]` |
| 資料敏感度評估 | 判斷資料可用範圍 | 資料清單 | 資料分級工作坊 | 資料分級表 | IT / 法遵 | 資料分級文件 | `[ ]` |
| 系統盤點 | 判斷可串接系統 | 系統清單、API 文件 | IT 訪談 | 系統盤點表 | IT | 系統清單、API 文件 | `[ ]` |
| As-Is 流程盤點 | 找出重工與瓶頸 | 流程現況 | 工作坊 / 訪談 | As-Is Process Map | 部門 Owner | 流程圖、訪談紀錄 | `[ ]` |
| 場景篩選 | 選 PoC | 痛點清單、系統盤點 | Impact x Effort | PoC 場景清單 | 顧問 + 管理層 | 優先級矩陣 | `[ ]` |
| 治理評估 | 降低導入風險 | 權限、Log、審核要求 | IT / 法遵訪談 | 治理需求表 | IT / 法遵 | 權限表、審核規則 | `[ ]` |

## 4. L1-L5 IPOE 控制表

IPOE = Input / Process / Output / Evidence。

| 成熟度 | Input | Process | Output | Evidence | Owner | 驗收標準 | 狀態 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L1 Chat AI | `[文件、Email、問卷、低敏感資料]` | `[OpenWebUI、Prompt 訓練、使用規範]` | `[Prompt、AI 使用規範、入口流程]` | `[截圖、規範文件、練習成果]` | `[HR / IT / 顧問]` | `[種子人員可完成基本任務]` | `[ ]` |
| L2 Skill AI | `[SOP、模板、資深經驗、範例]` | `[Skill 設計、模板化、版本管理]` | `[Skill Library、3-5 個 Skill]` | `[Skill 文件、版本、測試輸出]` | `[部門 Owner]` | `[非原作者可使用 Skill]` | `[ ]` |
| L3 Workflow AI | `[Gmail、Sheets、Notion、CRM、API、ERP]` | `[n8n 串接、Trigger、AI 分類、人工審核、Log]` | `[Workflow PoC、摘要、任務、通知]` | `[Workflow JSON、Execution Log、測試案例]` | `[IT / 流程 Owner]` | `[測試案例成功且有審核]` | `[ ]` |
| L4 Auto Agentic AI | `[Skill、Workflow、任務、文件、Wiki、schema、權限]` | `[Hermes Agent orient、ingest、query、update、briefing、工具呼叫、人工 Gate]` | `[Agent 任務卡、Wiki pages、briefing、回報、追蹤清單]` | `[Log、SQLite 查詢、source page、工具呼叫紀錄、人工審核紀錄]` | `[部門 Owner / IT]` | `[Agent 輸出可追溯、可審核、可維運]` | `[ ]` |
| L5 Agentic Team AI | `[跨部門任務、角色、資料源]` | `[ClawTeam 多 Agent 分工、整合、審核]` | `[整合報告、改善提案、Roadmap]` | `[各 Agent 輸出、整合紀錄、主管審核]` | `[管理 Sponsor]` | `[有角色分工、人工 Gate、ROI]` | `[ ]` |

## 5. L1-L5 詳細控制表

### 5.1 L1 Chat AI 控制表

| 控制項 | 填寫內容 | Evidence | 是否完成 |
| --- | --- | --- | --- |
| AI 入口 | `[OpenWebUI / 核准工具]` | 工具截圖、網址、帳號清單 | `[ ]` |
| 使用對象 | `[種子人員 / 部門]` | 名單、簽到表 | `[ ]` |
| 可輸入資料 | `[資料類型]` | 資料分級表 | `[ ]` |
| 禁止輸入資料 | `[資料類型]` | AI 使用規範 | `[ ]` |
| Prompt 範本 | `[範本清單]` | Prompt Library | `[ ]` |
| 課程練習 | `[練習題]` | 學員輸出 | `[ ]` |
| L1 Gate | `[通過 / 未通過]` | Gate 1 驗收紀錄 | `[ ]` |

### 5.2 L2 Skill AI 控制表

| 控制項 | 填寫內容 | Evidence | 是否完成 |
| --- | --- | --- | --- |
| Skill 名稱 | `[Skill]` | Skill 文件 | `[ ]` |
| Skill Owner | `[人員 / 部門]` | Owner 名單 | `[ ]` |
| Input 定義 | `[資料 / 文件 / 範例]` | Skill 模板 | `[ ]` |
| Process 定義 | `[步驟]` | Skill 模板 | `[ ]` |
| Output 定義 | `[格式]` | 輸出樣本 | `[ ]` |
| 限制條件 | `[不可做事項]` | Skill 模板 | `[ ]` |
| 測試結果 | `[結果]` | 測試輸入輸出 | `[ ]` |
| L2 Gate | `[通過 / 未通過]` | Gate 2 驗收紀錄 | `[ ]` |

### 5.3 L3 Workflow AI 控制表

| 控制項 | 填寫內容 | Evidence | 是否完成 |
| --- | --- | --- | --- |
| Workflow 名稱 | `[名稱]` | n8n Workflow | `[ ]` |
| Trigger | `[Email / Webhook / 排程 / 表單]` | Node 設定截圖 | `[ ]` |
| 串接系統 | `[Gmail / Sheets / Notion / CRM / API / ERP]` | 系統串接清單 | `[ ]` |
| Credential | `[權限範圍]` | Credential 清單 | `[ ]` |
| AI 處理節點 | `[分類 / 摘要 / 草稿 / 判斷]` | Node 設定 | `[ ]` |
| 人工審核節點 | `[審核人 / 條件]` | 審核紀錄 | `[ ]` |
| Log | `[紀錄內容]` | Execution Log | `[ ]` |
| 錯誤處理 | `[通知 / 重試 / fallback]` | 測試紀錄 | `[ ]` |
| L3 Gate | `[通過 / 未通過]` | Gate 3 驗收紀錄 | `[ ]` |

### 5.4 L4 Hermes Agent 控制表

| 控制項 | 填寫內容 | Evidence | 是否完成 |
| --- | --- | --- | --- |
| Agent 名稱 | `[名稱]` | Agent 任務卡 | `[ ]` |
| Agent 目標 | `[目標]` | Agent 任務卡 | `[ ]` |
| Purpose | `[Agent 為什麼存在]` | `purpose.md` | `[ ]` |
| Schema | `[知識欄位與規則]` | `SCHEMA.md` | `[ ]` |
| Wiki 結構 | `[INBOX / queue / watchlist / tasks / wiki]` | Wiki 檔案清單 | `[ ]` |
| 可呼叫 Skill | `[Skill 清單]` | 工具清單 | `[ ]` |
| 可呼叫 Workflow | `[Workflow 清單]` | 工具清單 | `[ ]` |
| Ingest 測試 | `[文件 / SOP / FAQ]` | source page、log、index | `[ ]` |
| Query 測試 | `[查詢題目]` | query record、引用來源 | `[ ]` |
| Update 測試 | `[回寫內容]` | update diff、審核紀錄 | `[ ]` |
| Briefing | `[morning / weekly]` | briefing 報告 | `[ ]` |
| Discovery / Watchlist | `[關鍵字]` | watchlist、queue | `[ ]` |
| 可存取資料 | `[資料範圍]` | 權限表 | `[ ]` |
| 禁止事項 | `[不可做事項]` | 權限表 | `[ ]` |
| 回報格式 | `[格式]` | 輸出樣本 | `[ ]` |
| 人工接手 | `[條件與負責人]` | 接手紀錄 | `[ ]` |
| L4 Gate | `[4A / 4B / 4C / 4D / 4E]` | Gate 4A-4E 驗收紀錄 | `[ ]` |

### 5.5 L5 ClawTeam 控制表

| 控制項 | 填寫內容 | Evidence | 是否完成 |
| --- | --- | --- | --- |
| Team 任務 | `[跨部門任務]` | 任務說明 | `[ ]` |
| Agent 角色 | `[角色清單]` | 角色卡 | `[ ]` |
| 任務分派 | `[分派規則]` | 任務分派表 | `[ ]` |
| 各 Agent Input | `[資料源]` | Input 清單 | `[ ]` |
| 各 Agent Output | `[輸出]` | 輸出樣本 | `[ ]` |
| 整合 Agent | `[角色]` | 整合報告 | `[ ]` |
| Reviewer / Critic | `[審核角色]` | 審核紀錄 | `[ ]` |
| 人工 Gate | `[審核人]` | 簽核紀錄 | `[ ]` |
| L5 Gate | `[通過 / 未通過]` | Gate 5 驗收紀錄 | `[ ]` |

## 6. Evidence 控制表

| Evidence 類型 | 對應成熟度 | 必備程度 | 範例 | 存放位置 | Owner | 狀態 |
| --- | --- | --- | --- | --- | --- | --- |
| 問卷原始資料 | L1-L5 | 必備 | Google Form / Sheets | `[URL / 路徑]` | 顧問 | `[ ]` |
| 成熟度評分表 | L1-L5 | 必備 | L1-L5 分數 | `[URL / 路徑]` | 顧問 | `[ ]` |
| AI 使用規範 | L1 | 必備 | 可用 / 禁用資料 | `[URL / 路徑]` | IT / 顧問 | `[ ]` |
| Prompt Library | L1 | 建議 | 常用 Prompt | `[URL / 路徑]` | 部門 | `[ ]` |
| Skill Library | L2 | 必備 | 3-5 個 Skill | `[URL / 路徑]` | 部門 Owner | `[ ]` |
| Workflow JSON | L3 | 必備 | n8n Export | `[URL / 路徑]` | IT | `[ ]` |
| Execution Log | L3 | 必備 | n8n 執行紀錄 | `[URL / 路徑]` | IT | `[ ]` |
| 人工審核紀錄 | L3-L5 | 必備 | 審核表 / 簽核 | `[URL / 路徑]` | 部門 Owner | `[ ]` |
| Agent 任務卡 | L4 | 必備 | Hermes Agent 任務卡 | `[URL / 路徑]` | 顧問 / 部門 | `[ ]` |
| Hermes Wiki | L4 | 必備 | purpose、schema、INBOX、queue、watchlist、tasks | `[URL / 路徑]` | IT / 部門 | `[ ]` |
| Ingest / Query / Update 紀錄 | L4 | 必備 | source page、query record、update diff | `[URL / 路徑]` | 顧問 / IT | `[ ]` |
| Briefing 範本 | L4 | 建議 | morning / weekly briefing | `[URL / 路徑]` | 部門 Owner | `[ ]` |
| Agent 執行紀錄 | L4 | 必備 | 工具呼叫紀錄、Log、SQLite 查詢 | `[URL / 路徑]` | IT | `[ ]` |
| Agent Team 角色卡 | L5 | 必備 | ClawTeam 角色卡 | `[URL / 路徑]` | 顧問 | `[ ]` |
| ROI 追蹤表 | L3-L5 | 必備 | 工時 / 錯誤率 / 回應速度 | `[URL / 路徑]` | 管理 Sponsor | `[ ]` |

## 7. Stage Gate 控制表

| Gate | 對應成熟度 | 必備 Deliverables | 通過標準 | 審核人 | 結果 | 備註 |
| --- | --- | --- | --- | --- | --- | --- |
| Gate 1 | L1 | AI 入口、使用規範、Prompt 範本 | 種子人員可完成基本 AI 任務且知道資料邊界 | HR / IT / 顧問 | `[Pass / Fail]` | `[備註]` |
| Gate 2 | L2 | Skill Library、Skill Owner、測試輸出 | 非原作者可使用 Skill 產出可接受結果 | 部門主管 / 顧問 | `[Pass / Fail]` | `[備註]` |
| Gate 3 | L3 | n8n Workflow、Log、人工審核 | Workflow 可跑測試案例，且有錯誤處理 | IT / 流程 Owner | `[Pass / Fail]` | `[備註]` |
| Gate 4 | L4 | Hermes Agent 任務卡、L4 IPOE、Wiki、權限表、工具清單、Log、briefing | Agent 可完成 ingest/query/update，能呼叫 Skill / Workflow，輸出可追溯、可審核、可維運 | 部門主管 / IT | `[Pass / Fail]` | `[備註]` |
| Gate 5 | L5 | ClawTeam 角色卡、任務分派、整合報告 | 多 Agent 有分工、整合、Reviewer 與人工 Gate | 管理 Sponsor | `[Pass / Fail]` | `[備註]` |

## 8. 風險與治理控制表

| 風險類型 | 說明 | 影響等級 | 對應控制 | Evidence | Owner | 狀態 |
| --- | --- | --- | --- | --- | --- | --- |
| 資料外流 | 敏感資料輸入未核准 AI | 高 | 資料分級、禁用清單、受控入口 | AI 使用規範 | IT / 法遵 | `[ ]` |
| 錯誤輸出 | AI 回答錯誤被直接使用 | 中高 | 人工審核、來源引用、信心標記 | 審核紀錄 | 部門 Owner | `[ ]` |
| 權限誤用 | Agent 查詢或修改不該碰的資料 | 高 | 權限表、最小權限、Log | 權限表、Log | IT | `[ ]` |
| 流程失敗 | Workflow 中斷無人知道 | 中 | 錯誤通知、重試、fallback | Execution Log | IT | `[ ]` |
| 責任不清 | AI 輸出誰審核不明 | 中 | Owner / Gate / 簽核 | RACI、審核表 | 管理 Sponsor | `[ ]` |
| ROI 不明 | 無法證明導入效益 | 中 | KPI、前後測、Dashboard | ROI 追蹤表 | 顧問 / 部門 | `[ ]` |

## 9. Deliverables 驗收控制表

| Deliverable | 對應階段 | 必備 | 驗收條件 | 審核人 | 狀態 |
| --- | --- | --- | --- | --- | --- |
| AI 成熟度問卷結果 | 診斷 | 是 | 問卷完成且可計分 | 顧問 | `[ ]` |
| 公司屬性調查表 | 診斷 | 是 | 產業、系統、資料、部署模式明確 | 顧問 / 客戶窗口 | `[ ]` |
| As-Is Process Map | Stage 1 | 是 | 部門確認流程正確 | 部門 Owner | `[ ]` |
| 成熟度評估報告 | Stage 2 | 是 | L1-L5 判定與證據完整 | 管理 Sponsor | `[ ]` |
| 場景優先級矩陣 | Stage 3-4 | 是 | Impact x Effort 明確 | 管理 Sponsor | `[ ]` |
| Executive Problem Statement | Stage 5 | 是 | 核心問題一句話可被管理層認同 | 管理 Sponsor | `[ ]` |
| Stage Gate Criteria | Stage 6 | 是 | 每階段驗收標準明確 | 顧問 / 客戶窗口 | `[ ]` |
| To-Be Operating Model | Stage 7 | 是 | L1-L5 目標架構完整 | 管理 Sponsor / IT | `[ ]` |
| Transformation Roadmap | Stage 8 | 是 | 30 / 60 / 90 天任務清楚 | 管理 Sponsor | `[ ]` |
| ROI 追蹤矩陣 | Stage 8 | 是 | KPI、量測方式、Owner 明確 | 管理 Sponsor | `[ ]` |
| 後續 SOW 建議 | Stage 8 | 否 | 可轉成報價或導入專案 | 業務 / 顧問 | `[ ]` |

## 10. 案例完成檢查

| 檢查項 | 是否完成 |
| --- | --- |
| 已完成問卷診斷 | `[ ]` |
| 已完成公司屬性與部署模式判斷 | `[ ]` |
| 已完成 As-Is 流程盤點 | `[ ]` |
| 已完成 L1-L5 IPOE 控制表 | `[ ]` |
| 已完成 Evidence 控制表 | `[ ]` |
| 已完成 Stage Gate 控制表 | `[ ]` |
| 已完成風險與治理控制表 | `[ ]` |
| 已完成 Deliverables 驗收控制表 | `[ ]` |
| 已完成 30 / 60 / 90 天 Roadmap | `[ ]` |
| 已完成 ROI 追蹤矩陣 | `[ ]` |
