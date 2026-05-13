# AI 轉型成熟度顧問方案 TODO / WBS

更新日期：2026-05-13

## 0. 目標

把「AI 成熟度 L1-L5」、「課程模組」、「簡易問卷診斷」與「八階段顧問方法論」整合成一套可銷售、可交付、可複製的企業 AI 轉型方案。

## 1. WBS 總覽

| WBS | 工作項目 | 優先級 | 狀態 | 主要產出 |
| --- | --- | --- | --- | --- |
| 1 | 方案故事與定位 | P0 | Done | 故事版規劃、角色價值主張、銷售話術 |
| 2 | L1-L5 成熟度模型細化 | P0 | Done | 評分標準、能力矩陣、缺口分類 |
| 3 | 簡易問卷診斷 | P0 | Done | 10 題、25 題、50 題問卷 |
| 4 | 課程模組與比例配置 | P0 | Done | L1-L5 課綱、比例推薦規則 |
| 5 | 公司屬性與部署模式調查 | P0 | In Progress | 雲 AI / Hybrid / 全地端判斷、產業適配 |
| 6 | 情境故事庫 | P0 | Done | 管理層與部門情境故事 |
| 7 | 八階段顧問診斷工具 | P1 | In Progress | 訪談問題、盤點表、分析表 |
| 8 | AI 轉型診斷報告模板 | P1 | In Progress | Markdown 報告模板已完成 |
| 9 | 系統串接與 PoC 場景 | P1 | Todo | Gmail、Sheets、Notion、CRM、API、ERP PoC 細稿 |
| 10 | 範例客戶完整案例 | P1 | In Progress | 製造業與醫院案例已完成，其他案例待補 |
| 11 | 對外銷售素材 | P2 | In Progress | 話術完成，One-pager 與簡報待做 |

## 2. 已完成文件

- [x] `README.md`
- [x] `00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`
- [x] `00_Overview/TODO_WBS.md`
- [x] `01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`
- [x] `01_Assessment/AI_MATURITY_SCORING_MODEL.md`
- [x] `02_Course_Design/COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md`
- [x] `02_Course_Design/COURSE_MODULE_MATRIX.md`
- [x] `02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`
- [x] `03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`
- [x] `04_Scenarios/CUSTOMER_SCENARIO_LIBRARY.md`
- [x] `04_Scenarios/CASE_CONTROL_TABLES.md`
- [x] `04_Scenarios/CASE_WRITING_STANDARD.md`
- [x] `04_Scenarios/SAMPLE_CLIENT_CASE_MANUFACTURING.md`
- [x] `04_Scenarios/SAMPLE_CLIENT_CASE_HOSPITAL.md`
- [x] `05_Sales/SALES_VALUE_PROPOSITION.md`

## 3. 已完成項目

### 3.1 方案故事與定位

- [x] 定義這不是單純課程，而是 AI 轉型顧問方案。
- [x] 定義三段式路徑：問卷診斷、課程建置、顧問報告。
- [x] 定義 L1-L5 與工具對應。
- [x] 將 Gmail、Sheets、Notion、CRM、API、ERP 納入 L3 Workflow AI 串接範圍。
- [x] 補 CEO / COO / CIO / IT / HR / 部門主管價值主張。
- [x] 補 30 秒、3 分鐘、10 分鐘銷售話術。
- [x] 方案名稱暫定：企業 AI 轉型成熟度診斷與導入方案。
- [x] L4 工具名稱統一：Hermes Agent。
- [x] ClawTeam 對外中文：AI Agent Team 協作平台。

### 3.2 L1-L5 成熟度模型

- [x] L1 Chat AI：OpenWebUI 能力定義、適用對象、完成標準。
- [x] L2 Skill AI：Antigravity / Claude Code / Codex 能力定義、適用對象、完成標準。
- [x] L3 Workflow AI：n8n 能力定義、適用對象、完成標準。
- [x] L4 Auto Agentic AI：Hermes Agent 能力定義、適用對象、完成標準。
- [x] L5 Agentic Team AI：ClawTeam 能力定義、適用對象、完成標準。
- [x] 每一級設計 5 個可觀察指標。
- [x] 每個指標設計 0-4 分量尺。
- [x] 定義總分對應成熟度等級。
- [x] 定義主成熟度與局部成熟度判斷方式。
- [x] 定義工具、Skill、Workflow、系統串接、Agent、治理與 ROI 缺口。

### 3.3 簡易問卷診斷

- [x] 設計工具使用題目。
- [x] 設計知識沉澱題目。
- [x] 設計流程標準化題目。
- [x] 設計系統整合題目。
- [x] 設計 Agent 應用題目。
- [x] 設計治理與 ROI 題目。
- [x] 10 題版：業務開發快速診斷用。
- [x] 25 題版：課前診斷用。
- [x] 50 題版：顧問訪談前完整盤點用。
- [x] 成熟度等級判定。
- [x] 六大構面雷達圖欄位。
- [x] 建議課程比例。
- [x] 建議優先導入場景。
- [x] 建議顧問診斷焦點。

### 3.4 課程模組與比例配置

- [x] L1 OpenWebUI 課程目標、課綱、練習、產出物、講師備註。
- [x] L2 Skill AI 課程目標、課綱、練習、產出物、講師備註。
- [x] 參考 Google Antigravity 三套 codelab 補強 L2 工程訓練：Agentic IDE、App Prototype、Unit Test、GCP Serverless Pipeline、Gate 2A-2E。
- [x] 補強 L2 下半堂銜接 L3：Workflow Blueprint、trigger、I/O schema、n8n node map、human gate、log、error handling。
- [x] L3 n8n 課程目標、課綱、練習、產出物、講師備註。
- [x] L4 Hermes Agent 課程目標、課綱、練習、產出物、講師備註。
- [x] 參考 Hermes `starter-kit-v2` 補強 L4 深度課程：Wiki 記憶、五個 skills、ingest/query/update、briefing/discovery、Gate 4A-4E。
- [x] L5 ClawTeam 課程目標、課綱、練習、產出物、講師備註。
- [x] 依成熟度推薦課程比例。
- [x] 依產業、主管目標、系統整合成熟度、部署模式調整比例。
- [x] 建立半日體驗課、一日工作坊、二日導入營、顧問診斷專案。

### 3.5 公司屬性與部署模式

- [x] 建立 L1-L5 需求清單。
- [x] 補入各級課程重點與產出物。
- [x] 定義基本公司資料調查項目。
- [x] 定義資料與風險屬性。
- [x] 定義主要系統盤點項目。
- [x] 定義雲 AI、Hybrid、全地端適用條件、優缺點與課程備註。
- [x] 建立部署模式評分表。
- [x] 建立部署模式建議文字模板。
- [x] 補入研發製造業、行銷服務業、金融、醫療、政府等高敏感單位備註。

### 3.6 情境故事庫

- [x] CEO：想知道 AI 投資是否能帶來 ROI。
- [x] COO：想降低流程重工與跨部門溝通成本。
- [x] CIO / IT：想掌握權限、資安、系統串接與維運。
- [x] HR：想做 AI 訓練、能力盤點與新人上手。
- [x] 業務：客戶開發、拜訪摘要、提案產生、CRM 更新。
- [x] 客服：Gmail 客訴分類、CRM 查詢、FAQ 產生、案件追蹤。
- [x] 行銷：市場分析、文案產生、活動規劃、成效報告。
- [x] 營運：ERP 異常訂單分析、庫存追蹤、流程改善。
- [x] 財務：費用分類、月結差異分析、預算彙整。
- [x] 人資：履歷摘要、教育訓練、內部知識庫。
- [x] IT：API 串接、權限治理、系統監控、流程維護。
- [x] 每個故事包含 Before、Trigger、AI Flow、Systems、Output、KPI。

### 3.7 診斷報告模板

- [x] Markdown 版。
- [x] 封面。
- [x] Executive Summary。
- [x] AI 成熟度診斷結果。
- [x] 課程觀察與能力盤點。
- [x] As-Is 現況流程與系統盤點。
- [x] 高價值 AI 場景清單。
- [x] 差距分析與核心問題。
- [x] To-Be AI Operating Model。
- [x] 三階段 Roadmap。
- [x] ROI 與治理建議。
- [x] 後續導入 SOW 建議。

## 4. 未完成 TODO

### 4.1 可填寫問卷與自動判讀

- [ ] Google Form 版本。
- [ ] Google Sheets 分數計算表。
- [ ] Notion Database 版本。
- [ ] n8n 自動產生診斷摘要流程。
- [ ] 將 `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md` 轉成可填寫問卷。

### 4.2 八階段顧問診斷工具細化

- [ ] Stage 1 現況掌握訪談問題。
- [ ] AI 使用盤點表。
- [ ] 系統盤點表。
- [ ] As-Is Process Map 模板。
- [ ] Stage 2 L1-L5 說明頁。
- [ ] Stage 3 產業標竿案例摘要模板。
- [ ] Stage 4 Missing / Broken / Redundant 表格。
- [ ] Stage 4 Impact x Effort 矩陣。
- [ ] Stage 5 Executive Problem Statement 工作表。
- [ ] Stage 6 Stage Gate 驗收標準。
- [ ] Stage 7 Skill Map / Workflow Map / Agent Map 模板。
- [ ] Stage 8 權限治理表與 ROI 追蹤矩陣。

### 4.3 系統串接與 PoC 場景細稿

- [ ] Gmail PoC：客服信件分類、業務信件摘要、主管每日摘要、回覆草稿。
- [ ] Google Sheets PoC：問卷結果寫入、自動計分、KPI 更新、Workflow 執行紀錄。
- [ ] Notion PoC：會議紀錄、任務建立、Skill Library、顧問診斷資料庫。
- [ ] CRM PoC：客戶資料查詢、商機摘要、互動紀錄更新、客訴案件追蹤。
- [ ] API PoC：內部 API、外部 API、Webhook、錯誤重試與紀錄。
- [ ] ERP PoC：訂單狀態、庫存異常、出貨延遲、財務或採購資料摘要。

### 4.4 範例客戶完整案例

- [x] 製造業案例。
- [x] 醫院 / 醫療機構案例。
- [ ] 行銷服務業案例。
- [ ] B2B 業務案例。
- [x] 問卷填答結果。
- [x] AI 成熟度判定。
- [x] 課程比例建議。
- [x] 課程中產出物。
- [x] 八階段顧問分析。
- [x] 最終診斷報告摘要。
- [x] 三階段 Roadmap。

### 4.5 對外銷售素材

- [x] 交付包與驗收標準文件。
- [ ] One-pager。
- [ ] 三段式服務流程圖。
- [ ] L1-L5 成熟度圖。
- [ ] 交付物清單視覺化。
- [ ] 10 頁高階主管版簡報。
- [ ] 20 頁標準銷售版簡報。
- [ ] 30 頁顧問方法版簡報。

### 4.6 其他產業補強

- [ ] 零售產業推薦場景。
- [ ] 教育產業推薦場景。
- [ ] 物流產業推薦場景。
- [ ] 軟體產業推薦場景。
- [ ] 專業服務產業推薦場景。

## 5. 下一輪建議優先順序

1. 建立 `05_Sales/ONE_PAGER_OUTLINE.md`：對外一頁式銷售素材。
2. 建立 `05_Sales/EXECUTIVE_DECK_OUTLINE.md`：10 頁高階主管版簡報。
3. 建立 `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`：八階段顧問診斷工具表格。
4. 建立 `02_Course_Design/POC_SCENARIO_SPECS.md`：Gmail、Sheets、Notion、CRM、API、ERP PoC 細稿。
5. 建立 `01_Assessment/AI_DIAGNOSIS_SHEETS_SCHEMA.md`：Google Sheets / Notion / n8n 自動診斷欄位設計。
