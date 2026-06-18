# AI 轉型成熟度顧問方案 TODO / WBS

更新日期：2026-05-15（GenAI 改名 + L1-L5 兩條軸精煉 + 目錄 README_EN 同步）

## 0. 目標

把「AI 成熟度 L1-L5」、「課程模組」、「簡易問卷診斷」與「八階段顧問方法論」整合成一套可銷售、可交付、可複製的企業 AI 轉型方案。

## 1. WBS 總覽

| WBS | 工作項目 | 優先級 | 狀態 | 主要產出 |
| --- | --- | --- | --- | --- |
| 1 | 方案故事與定位 | P0 | Done | 故事版規劃、角色價值主張、銷售話術 |
| 2 | L1-L5 成熟度模型細化 | P0 | Done | 評分標準、能力矩陣、缺口分類 |
| 3 | 簡易問卷診斷 | P0 | Done | 10 題、25 題、50 題問卷 |
| 4 | 課程模組與比例配置 | P0 | Done | L1-L5 課綱、比例推薦規則 + L5 ClawTeam |
| 5 | 公司屬性與部署模式調查 | P0 | Done | 雲/Hybrid/地端判斷、產業適配、35 題公司屬性問卷 |
| 6 | 情境故事庫 | P0 | Done | 管理層與部門情境故事 |
| 7 | 八階段顧問診斷工具 | P1 | Done | CONSULTING_TOOLKIT_TEMPLATES.md（8 stages 完整工具表） |
| 8 | AI 轉型診斷報告模板 | P1 | Done | Markdown 報告模板 + 工具表 |
| 9 | 系統串接與 PoC 場景 | P1 | Done | POC_SCENARIO_SPECS.md（6 系統 × 30 PoC） |
| 10 | 範例客戶完整案例 | P1 | Done | 製造業、醫院、行銷服務業、B2B 工業 4 個案例 |
| 11 | 對外銷售素材 | P2 | Done | One-pager / 3 套簡報 / 3 視覺 / FAQ |
| 12 | 問卷自動化（Sheets/Notion/n8n） | P1 | Done | AI_DIAGNOSIS_SHEETS_SCHEMA.md + FILLABLE_QUESTIONNAIRE.md |
| 13 | 產業推薦場景補強 | P2 | Done | INDUSTRY_SCENARIOS.md（零售/教育/物流/軟體/專業服務） |

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
- [x] 補入課前未來想像故事：讓客戶先看懂上完 L1-L5 後具備的能力。
- [x] 將 Gmail、Sheets、Notion、CRM、API、ERP 納入 L3 Workflow Automation 串接範圍。
- [x] 補 CEO / COO / CIO / IT / HR / 部門主管價值主張。
- [x] 補 30 秒、3 分鐘、10 分鐘銷售話術。
- [x] 方案名稱暫定：企業 AI 轉型成熟度診斷與導入方案。
- [x] L4 工具名稱統一：Hermes Agent。
- [x] ClawTeam 對外中文：AI Agent Team 協作平台。

### 3.2 L1-L5 成熟度模型

- [x] L1 Controlled AI Access：OpenWebUI 能力定義、適用對象、完成標準。
- [x] L2 Knowledge Codification：Antigravity / Claude Code / Codex 能力定義、適用對象、完成標準。
- [x] L3 Workflow Automation：n8n 能力定義、適用對象、完成標準。
- [x] L4 Autonomous Agent：Hermes Agent 能力定義、適用對象、完成標準。
- [x] L5 Multi-Agent Organization：ClawTeam 能力定義、適用對象、完成標準。
- [x] 每一級設計 5 個可觀察指標。
- [x] 每個指標設計 0-4 分量尺。
- [x] 定義總分對應成熟度等級。
- [x] 定義主成熟度與局部成熟度判斷方式。
- [x] 定義工具、Skill、Workflow、系統串接、Agent、執行導入與變革治理 缺口。

### 3.3 簡易問卷診斷

- [x] 設計工具使用題目。
- [x] 設計知識沉澱題目。
- [x] 設計流程標準化題目。
- [x] 設計系統整合題目。
- [x] 設計 Agent 應用題目。
- [x] 設計執行導入與變革治理 題目。
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
- [x] 參考 OpenWebUI playlist 補強 L1 企業啟用課：每人登入、個人聊天區、Admin Panel、帳號/角色/群組/權限、模型控管、影片參考地圖。
- [x] L2 Knowledge Codification 課程目標、課綱、練習、產出物、講師備註。
- [x] 參考 Google Antigravity 三套 codelab 補強 L2 工程訓練：Agentic IDE、App Prototype、Unit Test、GCP Serverless Pipeline、Gate 2A-2E。
- [x] 補強 L2 下半堂銜接 L3：Workflow Blueprint、trigger、I/O schema、n8n node map、human gate、log、error handling。
- [x] L3 n8n 課程目標、課綱、練習、產出物、講師備註。
- [x] 參考 TigerAI 頻道補強 L3 深度課程：Gemini、多模態、Sub-workflow、Data Tables、Webhook、LINE/Facebook/YouTube、GitHub 備份、Gate 3A-3G。
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

## 4. 未完成 TODO (Batch 1-3 後已歸零)

### 4.1 可填寫問卷與自動判讀 — Done

- [x] Google Sheets 分數計算表 → `01_Assessment/AI_DIAGNOSIS_SHEETS_SCHEMA.md` §A
- [x] Notion Database 版本 → 同檔 §B
- [x] n8n 自動產生診斷摘要流程 → 同檔 §C
- [x] 將 `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md` 轉成可填寫問卷 → `01_Assessment/COMPANY_PROFILE_QUESTIONNAIRE.md`
- [x] 10 / 25 / 50 題版 fillable form 規格 → `01_Assessment/FILLABLE_QUESTIONNAIRE.md`
- [ ] **未做**：實際的 Google Form 部署（需客戶 GCP / Google Workspace 帳號才能建）— 規格已備齊，可隨時建置

### 4.2 八階段顧問診斷工具細化 — Done

- [x] 全部 12 項目並入 `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`
  - Stage 1 訪談問題 (40)、AI Usage Inventory、Systems Inventory、As-Is Map
  - Stage 2 L1-L5 說明頁 + Vision Worksheet + RACI
  - Stage 3 標竿模板 + 5 stub
  - Stage 4 MBR 表 + Impact×Effort + Prioritization
  - Stage 5 Problem Statement Worksheet + 製造業範例
  - Stage 6 Benchmarking & Phased Goals + Gate 1-5 Checklist + Risk Register
  - Stage 7 Skill/Workflow/Agent Map + 3 種架構 variant
  - Stage 8 Permission Matrix + ROI Matrix + Audit + Ethics

### 4.3 系統串接與 PoC 場景細稿 — Done

- [x] 全部 6 系統 30 PoC → `02_Course_Design/POC_SCENARIO_SPECS.md`
  - Gmail (4)、Sheets (5)、Notion (5)、CRM (5)、API (5)、ERP (6)
  - 每 PoC 含 trigger / input / AI step / systems / output / acceptance / KPI / 人天 / L-level / n8n nodes
  - Selection Guide（依 L-level / 產業 / 敏感度）

### 4.4 範例客戶完整案例 — Done

- [x] 製造業案例（原已完成）
- [x] 醫院案例（原已完成）
- [x] 行銷服務業案例 → `04_Scenarios/SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md`（代號：代理商 M）
- [x] B2B 業務案例 → `04_Scenarios/SAMPLE_CLIENT_CASE_B2B_SALES.md`（代號：工業設備商 B）

### 4.5 對外銷售素材 — Done

- [x] One-pager → `05_Sales/ONE_PAGER_OUTLINE.md`
- [x] 三段式服務流程圖規格 → `05_Sales/VISUAL_ASSETS_SPEC.md` §1
- [x] L1-L5 成熟度圖規格 → 同檔 §2
- [x] 交付物清單視覺化 → 同檔 §3
- [x] 10 頁高階主管簡報 → `05_Sales/EXECUTIVE_DECK_OUTLINE.md`
- [x] 20 頁標準銷售簡報 → `05_Sales/STANDARD_SALES_DECK_OUTLINE.md`
- [x] 30 頁顧問方法論簡報 → `05_Sales/CONSULTING_METHODOLOGY_DECK_OUTLINE.md`
- [x] 銷售 FAQ 20 題 → `05_Sales/SALES_FAQ.md`
- [ ] **未做**：實際 Adobe Illustrator / Figma 視覺檔（規格已備齊，需設計師執行）
- [ ] **未做**：實際 PowerPoint / Keynote 檔（outline 已備齊，需設計師執行）

### 4.6 其他產業補強 — Done

- [x] 零售 / 教育 / 物流 / 軟體 / 專業服務 → `04_Scenarios/INDUSTRY_SCENARIOS.md`
  - 每產業：簡介、L1-L5 基線、Top 10 推薦場景、風險治理、30 天 Quick Win、Anti-Patterns

## 5. 下一輪建議優先順序（Batch 4+ 候選）

依重要度：

1. **EN 版本補齊**：本次 Batch 1-3 新增的 13 份檔案皆中文 inline 中英；若 reviewer 認為需嚴格 `_EN.md` sibling，可派代理產生。
2. **實際 Google Form / Tally 部署**：拿 `FILLABLE_QUESTIONNAIRE.md` 之 spec 建置上線。
3. **n8n template export**：把 `POC_SCENARIO_SPECS.md` 內的 PoC 寫成可分享之 n8n JSON template。
4. **設計師交付**：把 `VISUAL_ASSETS_SPEC.md` / 3 套 deck outline 真的做成 PNG / SVG / pptx。
5. ~~**更多客戶案例**：金融、政府、教育~~ → Done（`SAMPLE_CLIENT_CASE_FINANCIAL.md` / `_GOVERNMENT.md` / `_EDUCATION.md`，Batch 4）
6. **L4 Hermes Agent 完整 starter-kit 整理**（若採用）。
7. **L5 ClawTeam 實作 walk-through**：跑通一個跨部門 Agent Team 完整 demo，記錄為 `04_Scenarios/CLAWTEAM_WALKTHROUGH.md`。

---

## 6. 變更紀錄 / Change Log（給 reviewer）

### Batch 1 — commit `8795bfc` ✅ 已 push

| 檔案 | 內容 |
| --- | --- |
| `05_Sales/ONE_PAGER_OUTLINE.md` | 一頁式銷售素材內容稿 + 版型 brief |
| `05_Sales/EXECUTIVE_DECK_OUTLINE.md` | 10 頁高階主管簡報大綱 |
| `05_Sales/STANDARD_SALES_DECK_OUTLINE.md` | 20 頁標準銷售簡報大綱 |
| `05_Sales/CONSULTING_METHODOLOGY_DECK_OUTLINE.md` | 30 頁顧問方法論簡報大綱 |
| `05_Sales/VISUAL_ASSETS_SPEC.md` | 3 視覺素材 ASCII 規格 + 設計師 brief |
| `05_Sales/SALES_FAQ.md` | 20 題對外銷售 FAQ |
| `01_Assessment/AI_DIAGNOSIS_SHEETS_SCHEMA.md` | Google Sheets / Notion / n8n 自動診斷 schema |
| `01_Assessment/FILLABLE_QUESTIONNAIRE.md` | 10/25/50 題可填寫問卷規格 |

### Batch 2+3 — commit `42df8cd` ⏳ 本地，未 push

| 檔案 | 內容 |
| --- | --- |
| `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md` | 八階段顧問工具表（訪談題庫、盤點表、矩陣、worksheet、checklist、6 週排程） |
| `02_Course_Design/POC_SCENARIO_SPECS.md` | 6 系統 30 個 PoC 細稿 + Selection Guide |
| `01_Assessment/COMPANY_PROFILE_QUESTIONNAIRE.md` | 35 題公司屬性問卷 + JSON Bundle + 推導規則 |
| `04_Scenarios/INDUSTRY_SCENARIOS.md` | 零售/教育/物流/軟體/專業服務 5 產業 Top 10 場景 |
| `04_Scenarios/SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md` | 行銷代理商完整案例（代號：代理商 M） |
| `04_Scenarios/SAMPLE_CLIENT_CASE_B2B_SALES.md` | B2B 工業完整案例（代號：工業設備商 B） |
| `00_Overview/TODO_WBS.md` | WBS 重整、TODO 4.1-4.6 對帳 |

### Batch 4 — commit `778bb03` ⏳ 本地，未 push

| 檔案 | 內容 |
| --- | --- |
| `04_Scenarios/SAMPLE_CLIENT_CASE_FINANCIAL.md` | 金融業完整案例（代號：區域銀行 F，2,500 人，全地端、雙審、ROI ~358%） |
| `04_Scenarios/SAMPLE_CLIENT_CASE_GOVERNMENT.md` | 某市政府數位局（22 局處、800 人先導、三審、24 個月） |
| `04_Scenarios/SAMPLE_CLIENT_CASE_EDUCATION.md` | 教育機構完整案例（代號：科技大學 E，600 教職員/8,000 學生、Hybrid、學術倫理） |
| `00_Overview/TODO_WBS.md` | §5 item 5 標記 Done |

## 7. 目前狀態總覽 / Current Status

| 項目 | 狀態 |
| --- | --- |
| WBS §1-§13（P0/P1/P2） | ✅ 全部 Done |
| TODO §4.1-§4.6 | ✅ 全部 Done（2 項標 "未做" 為需外部資源：Google Form 部署、設計師視覺檔） |
| 案例庫產業數 | 7（製造/醫院/行銷/B2B/金融/政府/教育） |
| 八階段方法論版本 | **v2.0 對齊 NotebookLM 圖卡 + Rosemann BPM 學派**（2026-05-15）|
| Stage 2 工具表 | ✅ Tool 2.1-2.7（含 Reference Model 條件檢核 + 元件圖 + 4 層架構，仿 Dragon1）|
| Stage 3 工具表 | ✅ Tool 3.1-3.6（含 Cases-as-Benchmarks + 客戶 Ideal Practice 共創 Workshop） |
| 新增 4 份權威概念檔 | ✅ `CLIENT_JOURNEY_STORY`（阿明的故事）+ `EIGHT_STAGE_FLOW_STORY`（完整流程）+ `METHODOLOGY_SCIENTIFIC_LOGIC`（科學論證）+ `INDUSTRY_FRAMEWORK_ALIGNMENT`（業界對齊）；中英雙語俱全 |
| 報告模板 v2.0 | ✅ §5.4 Ideal Practice 簽署頁加入 |
| 接案 SOP v2.0 | ✅ ENGAGEMENT_LIFECYCLE §2.5 3 階段合約模型加入 |
| Git：已 push | …（截至 `2604a37`）|
| Git：本地待 push | **2026-05-15 大批次**：Stage 工具表升級 Tool 2.5-2.7 + 3.5-3.6（中英）+ 4 份新權威檔（中英 = 8 檔）+ 報告模板 §5.4 + ENGAGEMENT_LIFECYCLE §2.5（中英）+ Stage 名稱對齊圖卡 50 檔 + 各 README 索引更新 |
| Git：本地待 push（續）| **2026-05-16 補完**：EXECUTIVE_DECK 加 CEO 60 秒 elevator pitch（中英）+ STANDARD_SALES_DECK Slide 18b/18c 加 4 份權威檔 + 3 階段合約模型（中英）+ CONSULTING_METHODOLOGY_DECK Part C2/C3/C4 加 Tool 2.5-2.7 + 3.5-3.6 + 閉環圖（中英）+ 7 案例（中英 = 14 檔）加 Tool 3.5 Benchmark-grade Summary block |
| Git：本地待 push（v3 學術硬化批次）| **2026-05-16 V3 學術版**：9 大學術建議全做完 ── Wave 1: 案例 Evidence Level 標籤（14 檔）+ Tool 8.9 Evidence Hierarchy + AI_MATURITY_SCORING_MODEL §3.1 Construct Definition + §3.2 信效度驗證計畫 + §3.3 Maturity vs Readiness 拆分；Wave 2: FAILURE_PATTERNS（中英）+ AI_GOVERNANCE_ALIGNMENT（中英，含 NIST AI RMF / EU AI Act / ISO 42001 / OECD / 台灣 AI 基本法）；Wave 3: PILOT_STUDY_PROTOCOL 18-24 個月實證研究設計（中英）；Wave 4: L1-L5 全 repo 雙層命名（Chat AI → Controlled AI Access 等，305 處替換 + canonical 表升級）；額外：AI_NATIVE_LIVING_BOOK 方法論承載形式論述（中英） |
| Git：本地待 push（v3 學術硬化 V2 批次）| **2026-05-16 V3 V2 學術理論加冕**：5 大理論建議全做完 ── BARS_RUBRICS（中英，6 構面 × 0-4 分行為錨點 + 校準練習 SOP）+ ACADEMIC_THEORETICAL_FOUNDATIONS（中英，7 大理論支柱 + 創立者引用 + 7 篇 paper 投稿建議）+ Tool 6.3 加 Absorptive Capacity（Prior Knowledge + Internal Knowledge Flow 2 維）+ TTF Assessment + Tool 7.2 加責任歸屬 / 心理安全欄位 + Tool 7.2-Extension Dynamic Capability Worksheet（Sensing/Seizing/Transforming）+ Tool 8.2 加演算法厭惡 / 過度依賴 2 抗拒類型 + Tool 8.5 加第 6 維度 Strategic Options（Real Options）+ 各 README 索引更新 |
| Git：本地待 push（v3 學術誠信批次）| **2026-05-16 V3 學術誠信加固**：14 案例 Evidence Level 從 🟡 L2 Anonymized Composite **改為 🔵 L0 AI-Simulated Teaching Case**（明確聲明所有案例皆 AI 模擬產生，非真實客戶資料）+ 阿明的故事 / 客戶 M / MingChang 全部加 AI-fabricated 聲明 + 04_Scenarios/README 加 banner + 根 README（中英）加 disclaimer + 兩份銷售 deck 加 disclaimer + AI_TRANSFORMATION_STORY §6.1 + EIGHT_STAGE_FLOW_STORY §2 + Tool 3.5 M 公司範本（中英）全部加 AI-Simulated 標註 |
| 專案名稱 | **GenAI Consulting Methodology Toolkit**（2026-05-15 由 `AI Consulting…` 改名）|

## 8. 下一輪候選

| # | 項目 | 狀態 |
| --- | --- | --- |
| 1 | ~~EN `_EN.md` sibling 補齊（Batch 1-5 新檔）~~ | ✅ Done（19 個 `_EN.md`，commits `f0dc604`~`611f779`） |
| 2 | Google Form / Tally 實際部署 | ❌ 需客戶 Google 帳號 |
| 3 | ~~n8n template JSON export~~ | ✅ Done（`N8N_WORKFLOW_TEMPLATES.md`，4 骨架 + 匯入/備份 SOP；其餘 26 PoC 骨架本輪補齊中） |
| 4 | 設計師交付（pptx / Figma / PNG） | ❌ 需設計師 |
| 5 | ~~更多客戶案例（金融/政府/教育）~~ | ✅ Done（Batch 4） |
| 6 | ~~L4 Hermes Agent starter-kit 整理~~ | ✅ Done（`L4_HERMES_AGENT_COURSE_PLAN.md` 改版：抽象化具體名稱 + 新增七大設計原則；僅取概念，不含程式碼） |
| 7 | ~~L5 ClawTeam 實作 walkthrough~~ | ✅ Done（`04_Scenarios/CLAWTEAM_WALKTHROUGH.md`） |
| 8 | ~~agency-agents 進 L2、TigerAI-n8n-Skill-Pack 進 L3~~ | ✅ Done（commit `db42c15`：L2 §7.6、L3 §1.1+§5.5、2 個 reference 檔） |

## 9. 工作日誌 / Session Log

### 2026-05-14

#### 完成 / Done

- Repo 授權 / 署名整備：CC BY 4.0 → Apache 2.0、新增 `NOTICE`、中英雙語署名、致謝 Prof. Michael Rosemann (QUT)、作者學歷補海外資工碩士。（2026-05-18 後再校：個人 bio 還原為「n8n Taipei 大使 / NTUST 智慧製造博士生 / QUT 資工碩士」全名；affiliation 維持 `Tiger AI (Independent Research)` —— bio 是個人事實揭露 ≠ 機構掛名，後者才需要書面同意。）
- L5 ClawTeam 引用整備：新增 `90_References/CLAWTEAM_REFERENCE.md` 與 `02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md`，引用 HKUDS/ClawTeam (MIT)。
- 全 repo .md 中英雙語化（29 個 `_EN.md` sibling）。
- TODO §4.1-§4.6 全數完成，共新增 17 份方法論交付檔，分 4 個 batch：
  - Batch 1 (`8795bfc`, 已 push)：銷售素材 6 + 問卷自動化 2。
  - Batch 2+3 (`42df8cd`, 本地)：顧問工具表、PoC 規格、公司屬性問卷、產業場景、行銷+B2B 案例。
  - Batch 4 (`778bb03`, 本地)：金融 / 政府 / 教育 案例。
  - TODO 紀錄 (`2616d1d`, 本地)。

#### 狀態 / Status

- 本地有 3 個 commit 未 push（`42df8cd` / `778bb03` / `2616d1d`），等使用者與另一位 reviewer AI 看過後再 push。
- 規則：使用者要求所有 push 前先列表給他看過。

#### 下一步 / Next

- 等 review → 決定是否 push 本地 commit。
- 後續候選見 §8（EN siblings 補齊 / Hermes starter-kit）。

#### 後續追加（同日）/ Same-day follow-ups

- 客戶名稱匿名化（commit `ec3bd54`）：5 個案例的化名全改成代號 M/B/F/E/G。
- Batch 5（commit `0ae048f`）：`04_Scenarios/CLAWTEAM_WALKTHROUGH.md` + `02_Course_Design/N8N_WORKFLOW_TEMPLATES.md`。
- 各資料夾 README 索引更新（commit `1b73551`）。

### 2026-05-15

#### 完成 / Done

- **EN siblings 全套補齊**：Batch 1-5 新增的 19 個檔案全部產出 `_EN.md`（commits `f0dc604` / `bc3f4ec` / `1f3d9a5` / `45565f7` / `611f779`）。
- **GitHub About 設定**：description、homepage（LinkedIn）、15 個 topics，透過 GitHub API 寫入。
- **agency-agents 進 L2、TigerAI-n8n-Skill-Pack 進 L3**（commit `db42c15`）：
  - L2 新增 §7.6「L2-B 下半段擴充：善用現成 Agent 庫」，保留原 §7 L2→L3 Bridge。
  - L3 新增 §1.1（上半段概念 / 下半段 AG+Skill Pack 生成）與 §5.5。
  - 新增 `90_References/AGENCY_AGENTS_REFERENCE.md`、`N8N_SKILL_PACK_REFERENCE.md`。
- **L4 Hermes starter-kit 整理**：依使用者指示，starter-kit-v2 為內部不公開資料，課程**只取概念、不含程式碼**。
  - `L4_HERMES_AGENT_COURSE_PLAN.md` 改版：5 個 skill 名稱、檔案結構、CLI 指令全部抽象化（選項 1）。
  - 新增 §2「L4 知識型 Agent 的七大設計原則」：白天輕夜間重、知識複利閉環、P1>P2、寫讀同源、工具/LLM 分工、失敗模式驅動學習、為何不只用 RAG。
- **過時檔案同步**：L2/L3/L4 的 `_EN.md` 更新、2 個新 reference 補 `_EN.md`、本 TODO_WBS 更新。
- **N8N_WORKFLOW_TEMPLATES.md**：補齊其餘 26 個 n8n PoC 骨架。

#### Git 規則更新

- 使用者於 2026-05-15 進一步指示：「沒有說要 commit」→ 之後**只寫檔，不 commit、不 push，除非明確要求**。

#### 狀態 / Status

- 截至 commit `db42c15` 已 push。
- 本輪（L4 整理 + EN 同步 + TODO 更新 + 26 PoC 骨架）尚未 commit，等使用者指示。

#### 後續大批次（同日）/ Same-day major batch

- **8 個目錄 README 全面改寫**（commit `43ffa09`）：統一結構（定位 / 方法論位置 / 目標效益 / 使用流程 / 檔案說明 / 目錄對應 / 常見情境）。
- **新增 06_Delivery 接案營運層**（commit `43ffa09`）：ENGAGEMENT_LIFECYCLE、DELIVERY_ROLE_SOPS、BUSINESS_DOCUMENT_TEMPLATES、DELIVERY_CHECKLISTS、PRICING_AND_RISK（改寫自 Mirza Iqbal / next8n.com，MIT）+ `90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`。
- **新增 04_Scenarios/LLM_APPS_CASE_INDEX.md**（commit `43ffa09`）：150+ LLM 應用案例，雙軸查詢（L1-L5 / 部門）；+ awesome-llm-apps、ai-engineering-hub 兩個 reference 檔。
- **身份署名補學歷**：NOTICE / README / 90_References / 銷售簡報全部加註「海外資工碩士」（2026-05-17 因法務風險先抽象化為「PhD student / M.IT overseas」；2026-05-18 再還原為「NTUST 智慧製造博士生 / QUT 資工碩士」實名 —— 釐清個人 bio（personal disclosure，可放）vs 機構 affiliation（需書面同意）的差異；CITATION.cff / 論文 Affiliation 欄位仍維持 `Tiger AI (Independent Research)`）。
- **專案改名**（commit `25ecc4e`）：`AI Consulting Methodology Toolkit` → `GenAI Consulting Methodology Toolkit`（GenAI＝LLM-based，與傳統深度學習數理 AI 區隔）；全 repo 50 檔的名稱與 GitHub URL 一併更新（org 統一 MorrisLu-Taipei、slug 改 GenAI-）；git remote URL 已更新。
- **問卷白話化**（commit `25ecc4e` / `b26899f`）：`AI_MATURITY_QUESTIONNAIRE`(.md/_EN) 新增「給填答者的話」+「名詞小辭典」（24 術語）+ 10 題加 0/2/4 情境錨點 + 25/50 題加白話舉例；`FILLABLE_QUESTIONNAIRE`(.md/_EN) 加每題 help text 原則。
- **補齊 14 個缺漏 `_EN` sibling**（commit `b26899f`）：06_Delivery x5、90_References reference x5、CONSULTING_FRAMEWORKS_LIBRARY_EN、REPORT_PRODUCTION_WORKFLOW_EN、LLM_APPS_CASE_INDEX_EN、90_References/README_EN。
- **L1-L5 兩條軸概念精煉**（commit `2604a37`）：L1-L5 重新定位為兩條軸 —— 規模軸（L1 個人 → L2 部門 → L3 跨部門 / 全公司，人監督 AI）+ AI 自主軸（L4 AI 超級助理 → L5 AI 團隊，AI 營運自主、人退為治理者）；關鍵分界 L3→L4；強調 L4-L5 治理仍由人建立、人保有監督權。新增「兩條軸故事」至 `00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE`（中英）。
- **Gate 術語白話化**：人工 Gate → HITL（Human-in-the-Loop，人類在迴圈內審核）；Stage Gate → 階段驗收關卡。貫徹至定義型檔案（根 README、故事、L1_L5_COMPLETE、02 README、SCORING_MODEL、DELIVERABLES_AND_EVIDENCE_MATRIX，皆含 `_EN`）。
- **7 個目錄 README_EN 同步**：00-06 的 README_EN 全部重寫至與中文完整版對應，並納入兩條軸概念。
- **公開誠實版交付範圍**：`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE`(.md/_EN) §1.1 —— L1-L3 實作並驗收的交付 vs L4-L5 框架與顧問引導。

#### 下一步 / Next（2026-05-15 大批次後）

- 一致性已掃描（名稱 / URL / Gate 術語乾淨）。
- 待 commit & push 本批次（7 目錄 README_EN + DELIVERY_PACKAGE + Gate 清理 + 本 TODO 更新），並切 GitHub Release。

---

### 2026-05-18 —— 學術 deposit 日 + L1-L5 audit cycle 完成

#### 完成 / Done（10 commits, +6300 lines）

**學術 deposit pipeline 建置：**

| Commit | 內容 |
| --- | --- |
| `f864e01` | Bio 還原（NTUST + QUT）跨 12 檔 |
| `002762b` | Paper DOI cross-link + LaTeX PDF render pipeline + Citation Status Table 3-tier 重整 |
| `950adff` | ZH preprint parity fix（同 EN 的 table-shorten + Korean replace + emoji removal） |

**外部成果：**

- **Zenodo v1.0**（先 deposit）：concept DOI `10.5281/zenodo.20261850`、version DOI `10.5281/zenodo.20261851`（只 .md）
- **Zenodo v2.0**（同日升版）：version DOI `10.5281/zenodo.20264772`（加 3 個 PDF：EN preprint / ZH preprint / AI_Comments）
- Author name "Lu, YEH HSING" → "Lu, Yeh-Hsing"（同步在 Zenodo 編輯）

**方法論大批次（兩個 P0 新檔）：**

| Commit | 內容 |
| --- | --- |
| `0efd56f` | `02_Course_Design/ONLINE_COURSE_DESIGN_METHODOLOGY`（zh+EN）— 跨課程學習設計品質 SOP；Backward Design + Constructive Alignment + Bloom's Taxonomy + Cognitive Load + Mager + Mayer 等學術錨點 + 30 點 audit checklist + 4 大組件 / 3 層門檻。`00_Overview/SME_LITE_PATH`（zh+EN）— 中小企業 4 階段壓縮版 + SOHO 2 階段精簡版 + 6 個升級觸發條件 + 銷售腳本回應「你方法太重」+ 2 個 worked example。 |

**L1-L5 audit + 編修（P0 → P1 → P2 三輪）：**

| Commit | 階段 | 內容 |
| --- | --- | --- |
| `434eb9e` | P0 | L1-L5 Bloom-format LO 重寫（10 檔：5 zh + 5 EN）。原narrative「能...」目標 → 4 條主 LO + 細部能力清單 |
| `49cb86f` | P1 + Zenodo v2 cross-link | L1-L5 §3.3 互動學習設計（engagement / formative / summative）+ §3.4 reference materials + L4 §3.5 Skill JSON + §3.6 mission.md + L5 角色卡 + 整合報告範本（10 檔 zh+EN）+ 5 檔 v2 DOI cross-link |
| `1253dfd` | P2 batch 1 | L1 §6.0 完整 ~50 lecture map（zh+EN）+ L4 §3.7 Hermes Agent ASCII 架構圖（zh+EN）+ L5 ClawTeam CLI 速查卡（zh+EN） |
| `be7c39b` | P2 batch 2 | L2/L3/L4/L5 Foundation lecture maps（8 檔 zh+EN，~190 lectures）；Builder/Advanced/Operator/Enterprise-Lab 留 stub |
| `a8af67c` | P2 batch 3 | 12 個 standalone deliverable templates 在 `02_Course_Design/_deliverables/`（L1×5 + L2×3 + L3×2 + L4×2）+ index README + L1-L4 §3.4 cross-link 由 ☐ → ☑ |

**結構性完成：L1-L5 audit cycle（P0 + P1 + P2）全部結構性 close。剩餘只有 Builder / Advanced / Operator / GCP / Enterprise-Lab 的進階 lecture map stub，等實際錄影前展開。**

#### Lessons Learned

1. **Bio vs Affiliation 是兩件事，需分開處理。** 個人 bio（NTUST 博士生 / QUT 碩士）是個人事實揭露，不需機構同意；機構 affiliation（CITATION.cff `affiliation:` 欄）是 endorsement claim，需書面同意。今日把 NTUST/QUT bio 還原到 NOTICE / READMEs，但 CITATION.cff affiliation 保持 `Tiger AI (Independent Research)`。memory note `feedback_no_real_names.md` 已更新此區分。

2. **Zenodo 的 markdown 預覽不能看，學術 deposit 一定要附 PDF。** v1.0 只丟 .md → 預覽糟、reviewer 看不下去。v1.1（= v2）補上 3 個 LaTeX-rendered PDF 之後立刻變學術級。**Lesson：** 從 deposit 第一刻就附 PDF。

3. **LaTeX PDF rendering 在 Windows 上要繞 8 次彎才乾淨。** 跑了 v1-v8 共 8 個 iteration：MiKTeX 預設不會 auto-install → 加 `--enable-installer`；xeCJK FallBack option 不可靠 → 改用 ucharclasses → 又破壞 longtable → 最後回到 source-level 替換韓文 + 縮短表格內容；inline `\texttt` 不在 `/` `_` 斷行 → seqsplit 失敗 → 直接縮短 source markdown 的 inline code（最務實）。**Lesson：** 工具不行就改 source，不要硬凹 LaTeX。

4. **Lecture map 範圍要先 scope-down 才能交付。** 原本承諾「L1-L5 lecture map」聽起來 1 個 commit，實際算 = 300+ lectures × 平均 4 min × 5 課程 = 大工程。最後 scope 成「每課 Foundation 版本完整切 + 其餘版本 stub」，~290 entries 分 2 個 commit 完成。**Lesson：** 課程 lecture map 切到「primary 版本」就停，Builder / Advanced 等錄影前再展開。

5. **SME Lite Path 是真實 sales objection 驅動的方法論延伸。** 客戶說「你方法太重了我們用不起」→ 才發現八階段假設都是 enterprise。SME（50-300 人）/ SOHO（< 20 人）需要的不是「砍幾個 stage」，而是「每個 cell 工作量降一個數量級但邏輯閉環不缺」。**Lesson：** 方法論 gap 多半從真實對話來，不是 desk research。

6. **"PDF deliverables" 真正的意思是 markdown templates。** 一開始照字面理解要產 PDF，後來想清楚：PDF 是 throwaway render，markdown 才是 source。最終產出 12 個 .md 範本（中英雙語、含 `[填入]` placeholder），加 pandoc 渲染指引；客戶要 PDF 自己跑 pandoc。**Lesson：** 別人說 "PDF" 時，先問「你要可編輯的還是固定的」。

7. **EN propagation 是 2× 工作量。** 每個 zh edit 要對應 EN sibling edit。今日跨 L1-L5 + READMEs 共 8 個語言 README + 多份雙語文件 = 大量 propagation。**Lesson：** 排程要把 propagation 算進去（不是「再加一下英文」）。

8. **Bloom 格式 LO vs 敘述式目標的差別不只是格式美觀，是平台上架硬要求。** Udemy / Coursera / Hahow 都要求 CLP（Course Landing Page）放 4+ 條可驗收 LO。原本 narrative「能..」讀起來 OK 但不可量測，動詞像「了解 / 認識 / 熟悉」會被讀者識破為灌水。Bloom verb（套用 / 分析 / 評估 / 創作）+ 內容 + 情境 = 平台 ready + reviewer 信服。**Lesson：** 課程文件第一個變動就應該是 LO 重寫。

#### 狀態 / Status

- 截至 commit `a8af67c` 全部 push。
- L1-L5 audit cycle 結構性 close。
- Zenodo paper 已是 v2，含 PDF。
- 餘下 P2 加分項（Builder/Advanced/Operator/GCP/Enterprise-Lab lecture maps）標 stub，錄影前再展開。

#### 下一步候選 / Next candidates（2026-05-18 / 2026-05-20 收工後累積）

- **【Zenodo v3 upload】** —— `09_Research_Paper/_build/` 內 3 個 v3 PDF 已備好（EN 273KB / ZH 983KB / AI_Comments 153KB），等使用者去 zenodo.org/records/20264772 走 "New version" 流程上架。v3 內容變動：abstract reframing（從「方法論發展」→「電子書出版」）+ §8.2.2 出版循環新增 + 短摘要 4 檔。版本號邏輯：v3 = Concept DOI 20261850 的下一版本，會 mint 新 version DOI（預估 20266xxx）。上架後請把新 DOI 傳回，我做 follow-up commit 把 preprint front matter / CITATION.cff / NOTICE 三處 cross-link 更新。
- **【AI 人才指引整合】** —— 把《AI 產業人才認定指引》（經濟部產發署，2026-05/115 年 5 月版）整合進方法論。檔案已收在 `90_References/【電子書下載】AI產業人才認定指引(115年5月).pdf`。要產出：(1) `90_References/AI_TALENT_GUIDE_REFERENCE.md`（+EN）引用說明；(2) `04_Scenarios/AI_TALENT_GUIDE_MAPPING.md`（+EN）Tiger AI L1-L5 vs 三大人才類別（AI 應用 / AI 開發 / AI 研究）對位表；(3) 論文 §1/§3/§10 補對位段（EN + ZH）。**先決條件：** 確認官方下載 URL + 出版單位（封面 / 封底圖檔），確認授權範圍（極可能是「政府資料開放授權條款」≈ CC-BY 4.0）。預估 1 個工作天。
- **【overlay v0.2.0】** —— 把 `TigerAI-School-Workspace-Workflow-overlay/` 從 v0.1.0 推進到 v0.2.0。具體：(1) 補完「活動申請」與「物資請購」HITL 完整範本（v0.1.0 已有「公文簽核」「家長通知」）；(2) 加 Apps Script HITL wrapper 可直接 paste 的程式碼 fragment（不只概念示範）；(3) 為 4 個 L3 use case 各加 ROI 計算範例。預估 1-2 工作天。
- **【overlay 實際 fork + 試行】** —— 在 GitHub 上實際 fork [`mihozip/google-workspace-admin-project-workflow`](https://github.com/mihozip/google-workspace-admin-project-workflow) → 套上 `TigerAI-School-Workspace-Workflow-overlay/` 內所有檔案 → 切 release tag `tigerai-v0.1.0` → 找 1 個學校試行 1 個情境（建議從「跨班物資請購」開始，HITL 嚴格度最低，最安全 PoC）。預估 半天設置 + 學校試行 4-8 週。
- **【SSRN / arXiv 投稿】** —— 用 Zenodo v3 PDF + 短摘要投 SSRN（IS / Information Systems 分類）+ arXiv（cs.HC + cs.SE，需 endorser）。預估 SSRN 2-3 天（含等審），arXiv 1-2 週（含找 endorser）。
- **【Rosemann courtesy email】** —— 寄信給 QUT Rosemann 教授致謝 BPM Maturity 學派 + 附 Zenodo v3 paper DOI。150-200 字英文。預估 30 分鐘。
- **【拍 3 段 IDE demo 影片】** —— 之前提過的腳本：30-45 秒 × 3 段（/simulate-engagement、/devil-pair-debate、reader-as-querier）。HCI 投稿時可加 link 強化證據。預估腳本已備齊，拍攝 + 後製 1 天。
- **【L1 §6.1 實際錄影】** —— 用 [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) §6.0.1 已備好的 ~50 lecture map 實際錄影第 1 套課程。預估 Section 0-1（30 分鐘錄影）半天，全 §6.1（3 小時）3 個工作天。 —— 用 v2 PDF + 拿 SSRN ID
- **arXiv preprint 投稿** —— cs.HC + cs.SE category；需 endorser
- **拍 IDE demo 影片**（3 段：simulate-engagement / devil-pair-debate / reader-as-querier）—— 用 L1 §6.0.1 開頭 5 lectures 當示範
- **實際錄第 1 堂課**（L1 §6.1 Section 0-1 約 30 分鐘）
- **Rosemann 教授 courtesy email** —— 致謝 BPM Maturity 學派 + 附 v2 paper DOI
- **L2/L3/L4/L5 Builder/Advanced/Operator/GCP/Enterprise-Lab 完整 lecture map** —— 對應實際錄影前再展開

---

### 工作階段紀錄：2026-05-22（L5 Harness Engineering 案例融入）

**背景：** `02_Course_Design/ai-news-channel/` 是一個已在 repo 內、但與方法論「斷線」的完整 L5 專案（1 PM + 6 AI 成員、固定迴圈、六層 Harness）。檢查確認：**無外部 LICENSE、無上游 fork、git remote 即本 toolkit → 為本 toolkit 原創作品**，故不需 ClawTeam / school-overlay 那套 NOTICE 上游著作權處理。另確認 "Harness Engineering" 此前**未出現在 repo 任何其他檔**，是真正的新概念（且為《AI 產業人才認定指引》列名領域）。

**整合策略（全部 additive，不改 `ai-news-channel/` 原始檔）：** 確立 **L5 三件套 = ClawTeam（平台）+ Harness Engineering 六層（透鏡）+ ai-news-channel（完整實例）**。

**本階段產出：**

| 檔案 | 內容 |
| --- | --- |
| `90_References/HARNESS_ENGINEERING_REFERENCE.md`（+EN） | 六層模型定義、5 篇來源文獻、六層↔方法論既有構件（八階段/HITL/Stage Gate/兩軸/出版循環）對應、L5 三件套、人才指引對接、原創/授權聲明 |
| `02_Course_Design/ai-news-channel/TIGERAI_L5_CASE_NOTES.md` | 導讀層：定位 + 檔案→六層→L5 構件對照表 + 建議閱讀順序 + 5 個課堂活動（對接 Gate 5）+ 交叉連結。保留原專案的規格漂移當「找出漂移」教材。 |
| `02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md`（+EN） | 新增 §4.5「L5 三件套」+ 六層總表 + 教學動線，交叉連結 reference 與 case notes |

#### Lessons Learned（本階段）

1. **「MIT 授權」的口頭框架要用檔案事實驗證。** 使用者口述 ai-news-channel 是「MIT 授權」教學案例，但實際 `grep` 全資料夾**無任何 LICENSE 檔、無 MIT 字串**（先前 grep `-li` 命中的是 limit/submit/permit 等子字串），git remote 又是本 toolkit 自己。結論：這是**自製原創**，不是外部 MIT 專案。**Lesson：** 授權判定看檔案（LICENSE / NOTICE / remote），不看口頭描述；判錯方向會白做一套上游 NOTICE。

2. **「融入」一個 orphan 專案，關鍵動作是『導讀層』而非改檔。** ai-news-channel 已是完整成品，正確做法是**外掛一份導讀**（檔案→六層→構件對照），把它接上方法論，而**不動原始檔**——原始檔保持成品樣貌，才有教學真實性（甚至刻意保留其規格漂移當教材）。**Lesson：** 整合既有成品時，先問「能不能 additive overlay」，能就別動原檔。

3. **新概念融入要先確認它是不是真的『新』。** 先 `grep -rli "harness"` 全 repo，確認除了 ai-news-channel 外**零命中**，才確定 Harness Engineering 是缺口而非重複。**Lesson：** 加新概念前先全庫搜尋，避免重造或衝突。

#### 延伸 TODO（本階段新增，未做）

- **【Harness reference 補 5 國語言】** —— `HARNESS_ENGINEERING_REFERENCE.md` 目前只有 zh（base）+ EN。`90_References/` 慣例為每份 reference 配 DE/ES/FR/JA/KR 共 7 語言（見 CLAWTEAM_REFERENCE_*）。補齊其餘 5 語言。預估 半天。
- **【ai-news-channel 規格漂移修正評估】** —— 原專案 README（Designer=Gemini Vision / Librarian=Claude Haiku）vs CLAUDE.md（Designer=gpt-image-2 / Librarian=Scripts+NotebookLM）vs skill-stack.md（Gemini 3 Flash）三處不一致。目前**刻意保留**當「找出漂移」教材（CASE_NOTES §5 活動 A）。若日後要把它也當「乾淨可跑範本」散布，需決定是否統一。列待決。
- **【人才指引 × Harness 對位】** —— 與既有「AI 人才指引整合」TODO 同批：把《AI 產業人才認定指引》的「Harness Engineering」職能逐條對到 L5 六層 + ai-news-channel 實例，產出可驗收教學單元對照（Bloom 格式 LO）。

#### 本階段第二批：L4→L5 教學弧（同日，使用者三步指令）

使用者追加三步：#1 把案例補成「Hermes Agent 可用的教學」、#2 設定情境故事、#3 使用情境故事。三步是一條教學弧，合併為一份檔：

| 檔案 | 內容 |
| --- | --- |
| `02_Course_Design/ai-news-channel/TIGERAI_HERMES_TO_TEAM_TEACHING.md` | **Part A**：6 個成員逐一對位回 L4 mission.md（§3.6）/ 七大流程（§3.7）/ Gate；核心論點「L5 = 拆開的 Hermes + harness 重新串起」（引 L4 §15）。**Part B**：虛構情境故事（ABC 公司，B2B SaaS，200 人，內容行銷組產能瓶頸 → 為何是 L5 而非 L1-L4），職稱依規範（行銷副總 = CXO 級、內容行銷經理 = 人類 PM、資訊協理 = IT）。**Part C**：用情境跑一天端到端走查（含 Supervisor FAIL→PASS 真實循環）+ IPOE + Gate 5 + ROI + 4 個課堂活動。 |
| 交叉連結 | `TIGERAI_L5_CASE_NOTES.md` §7 + `L4_HERMES_AGENT_COURSE_PLAN.md` §15 各加一個指向新檔的 pointer（雙向可達）|

**設計決策：** (1) 三步合一檔——因為 #2/#3 的情境是用來示範 #1 建的 Hermes 團隊，拆檔會斷掉敘事。(2) 依使用者「給我中文」以中文為主，EN 版列 TODO。(3) 情境嚴守無真實名稱規範（ABC 公司 / 城市 X）+ 職稱 seniority 規範。(4) 仍 additive，未改 ai-news-channel 原始檔。

**延伸 TODO（本批新增）：** `TIGERAI_HERMES_TO_TEAM_TEACHING.md` 補 EN 版；Part A 其餘 3 個成員（CTO/Developer/Designer）的迷你目的檔目前刻意留作課堂作業，若要當完整範本需補齊。

---

### 工作階段紀錄：2026-05-23（WenyuChiou 研究工具評估 + preprint 強化）

**起因：** 使用者問兩個 repo（[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills) MIT、[WenyuChiou/research-hub](https://github.com/WenyuChiou/research-hub) MIT）對 `09_Research_Paper` 有無幫助，並追問「以後發表論文可以參考他什麼」，指示「全部做」。

**判斷：** 兩種幫助分開——(A) 當寫/改論文的**工具**（manuscript claim-audit、authenticity gate、文獻管線）；(B) 當**可引用的相關工作**（同範式在研究流程領域的獨立收斂）。兩者皆為 practitioner repo（非 peer-reviewed）→ 在論文中定位 Tier-3，佐證「實務趨勢」非理論。

**本階段產出：**

| 檔案 | 內容 |
| --- | --- |
| preprint EN + ZH（§2.3 / §10.4 / References §C / §E）| §2.3 加「practitioner 獨立收斂」段（skills 化 + provenance gate + 非 RAG + 多引擎委派）；§10.4 加 authenticity-gate 佐證段；References §C 新增 Chiou 2026a/b（Tier-3）；§E 表 + 計數同步（EN：27→29、Tier3 11→13）|
| `90_References/AI_RESEARCH_TOOLING_REFERENCE.md` | **回答「可以參考他什麼」**：發表實務元件（claim-audit/hype-scrub/reviewer-response/authenticity-gate）、設計立場、具體工具、採用vs引用vs略過決策表、MIT→Apache attribution 機制、與我們現有 workflows 對照避免重造 |
| `09_Research_Paper/PAPER2_LITREVIEW_PIPELINE.md` | Paper #2 文獻回顧管線：research-hub 五階段（discover→authenticity gate→cluster→brief→export）+ 接回章節 + provenance 言行合一 |
| `09_Research_Paper/CLAIM_AUDIT_2026-05-23.md` | 審稿者視角 claim audit：發現 deposit 後「pending/staged」字眼過時（中）、§E 計數既存不符（中）、少數 hype 詞（低）；附行動清單 |

#### Lessons Learned（本階段）

1. **「有幫助嗎」要拆成「工具」與「可引用」兩種，別混。** 同一個 repo 可以同時是「拿來用的工具」和「論文裡引用的佐證」，但定位完全不同（前者操作面、後者 Tier-3 grey literature）。混在一起講會讓人以為要整包 fork。

2. **發現既存的計數不一致時，preserve offset 而非偷偷重數。** preprint §E 摘要原本 11、表格實際 13（既存 2 列落差）。我新增 2 筆只做 +2，維持落差不擴大，並在 CLAIM_AUDIT 明列請作者下次 deposit 前重數——**不在不確定作者計數規則時擅自「修好」已 deposit 製品的數字**。

3. **最該借的是紀律不是工具。** research-hub 的 authenticity gate（擋下查不到的引用+記錄理由）價值 > 它整套 Zotero/Obsidian 整合，因為它讓我們論文 §10.4 主張的 provenance 紀律「言行合一」。

#### 延伸 TODO（本批新增）

- preprint 下一版必改：§1.3 + §9.1 的 "pending/staged Zenodo DOI" → 實際已發 DOI（見 CLAIM_AUDIT §1）。
- 新增 3 個投稿 workflow（我們目前缺）：`/claim-audit`、`/hype-scrub`、`/reviewer-response`（用現有引擎自製，概念參考 ai-research-skills，MIT）。
- `AI_RESEARCH_TOOLING_REFERENCE.md` 補 EN + 其餘語言（90_References 慣例 7 語）。
- Paper #2 文獻回顧時實際裝 research-hub 跑一次管線。

#### 本階段第二批：3 個投稿工作流（同日）

使用者指示「做」缺的三個投稿工作流。放在 `.codex/workflows/`（Codex = rigor/audit 角色，與既有 `evidence-audit` / `red-team-review` 同家）：

| 工作流 | 用途 | 與既有的區別 |
| --- | --- | --- |
| `.codex/workflows/claim-audit.md` | 稽核**學術稿件**主張（5 類 claim + 引用層級 + hedging + overclaim）| `/evidence-audit` 是稽核**顧問報告**；本工作流是**論文**，明確交叉引用避免混淆 |
| `.codex/workflows/hype-scrub.md` | 投稿用語清理（hype 詞 / 無證據最高級 / buzzword）+ 分辨「可辯護術語 vs 膨脹」 | 新能力，repo 原本沒有 |
| `.codex/workflows/reviewer-response.md` | reviewer 意見→逐點回覆信草稿 + 稿件改動清單；硬規則「不捏造改動、不背書未查證事實」 | 新能力 |

同步更新 `.codex/README.md` 工作流清單（新增「學術投稿工作流」分組）。

**計數影響（已記入 [`CLAIM_AUDIT_2026-05-23.md`](../09_Research_Paper/CLAIM_AUDIT_2026-05-23.md) §5b）：** live repo Codex workflow 由 10→13、總數 22→25。論文 §3.1「22 @ commit 7da82d7」凍結陳述仍為真。下版 deposit 須擇一：重新凍結，或把論文計數定義為「方法論生產工作流」排除投稿/meta 工作流（傾向後者）。

**Lesson：** 新增 workflow 會動到論文凍結的 metric。加之前先想「這會不會讓已 deposit 的數字在 HEAD 重數時對不上」——本次選擇 additive + 在 CLAIM_AUDIT 記下分歧與兩個解法，不回頭改凍結陳述。

#### 本階段第三批：實際套用 CLAIM_AUDIT 修正到 preprint（同日）

使用者「GO」核可後，用新做的 `/claim-audit` + `/hype-scrub` 全文掃描，並把修正**實際套用**到 EN + ZH preprint：

| 修正 | EN | ZH |
| --- | --- | --- |
| pending/staged DOI → 已發布 DOI（§1.3 / §8.2 / §9.1×2，共 **4** 處）| ✅ | ✅ |
| §E 引用計數重數：27（漏列）→ **32 total（Tier1 11 / Tier2 5 / Tier3 16）**，加計數規則、Tier-3 表補滿（拆出第 2 筆 US Copyright）| ✅ | ZH 無 count summary，僅表 |
| Abstract「cryptographically」→「content-addressed」| ✅ | ✅（可加密→內容定址）|
| §2.4「unprecedented scale」→「new scale」| ✅ | ✅（前所未有→新規模）|
| §5.1「顛覆」→「翻轉」對齊 EN "inverts" | —（EN 本就 inverts）| ✅ |

**全文掃描多抓到 2 處原人工稽核漏列**：§8.2 第 4 個 pending-DOI 點、ZH §5.1「顛覆」。已記入 CLAIM_AUDIT §7 Bonus。

**Lesson：** 投稿稿件的 hype/狀態字眼要**全文 grep**，不能只讀重點章節——人工讀 §1/§9 漏了 §8.2 的 pending-DOI 與 ZH 的「顛覆」；做成 `/hype-scrub`、`/claim-audit` workflow 全文掃才補齊。**這也驗證了三個投稿 workflow 的實際價值（第一次用就抓到漏網）。**

**未動（下版 deposit 決策）：** §3.1 兩 commit 澄清、工作流計數分歧（22→25）。 → **已於同日「go」收掉（見下）。**

#### 本階段第四批：收掉 preprint 最後兩項（同日）

| 項 | 處理 |
| --- | --- |
| §3.1 兩個 commit 澄清 | §3.1 凍結句加：`7da82d7` = 數值凍結 commit（論文數字計於此）；`5361c7b`（tag v3.0.1）= 學術 deposit 發布、觸發 Zenodo DOI。前者固定論文數字、後者固定已出版製品。EN+ZH |
| 工作流計數分歧（22 vs 25）| §3.1 表後加「workflow 計數範圍」note：**22 = 方法論生產 workflow**，凍結於 `7da82d7`；投稿/meta workflow（claim-audit / hype-scrub / reviewer-response）作用於「關於製品的論文」非「製品方法論內容」，**刻意排除**，故方法論生產 workflow 計數在 HEAD 仍為 22。Appendix A intro 同步加註。EN+ZH |

**決策口徑：採「定義法」而非「重新凍結 commit」**——把論文的 22 明確定義為「方法論生產 workflow」，投稿 workflow 另成一類。好處：論文數字不必隨每次新增投稿 workflow 變動，且概念上更清楚（生產 eBook 內容 vs 生產關於 eBook 的論文）。

**CLAIM_AUDIT 全部項目 close。** 唯一 optional 殘留：REPRODUCIBILITY.md §3.3 若要在 HEAD 重跑回傳 22，需加排除三個投稿 workflow 的指令；但論文已明定凍結於 `7da82d7`（當下即 22），非必要。

**Lesson：** 「計數分歧」有兩種解法——重新凍結（數字追著現況跑）vs 重新定義（把計數範圍講清楚、現況歸類）。選後者：當新增的東西**本質上屬於不同類別**（meta/投稿 vs 方法論生產）時，定義法比追數字更穩、更不會每次都要回頭改論文。

#### 本階段第五批：投稿工作流使用手冊（同日）

新增 [`09_Research_Paper/PUBLISHING_WORKFLOW_MANUAL.md`](../09_Research_Paper/PUBLISHING_WORKFLOW_MANUAL.md)：把三個投稿工作流放進完整「草稿→發表」管線（[1]寫作 [2]內容審查 [3]投稿前打磨 [4]凍結+發表 [5]審稿回覆），含全景圖、工具速查表、逐工作流詳細用法（何時用/餵什麼/拿到什麼/範例）、投稿前總檢查表、FAQ、本 repo 真實示範。中文為主，EN 列 TODO。交叉連結：09_Research_Paper README Contents + .codex/README 投稿工作流分組。

**注意：** 手冊把易混淆點寫死——`/evidence-audit`=顧問報告、`/claim-audit`=學術論文；跑完 `/reviewer-response` 要回 [3] 再跑 claim-audit + hype-scrub。

#### 本階段第六批：手冊的敘事版（情境故事，同日）

新增 [`09_Research_Paper/PUBLISHING_WORKFLOW_SCENARIO.md`](../09_Research_Paper/PUBLISHING_WORKFLOW_SCENARIO.md)：把手冊改寫成「使用情境故事」——虛構研究者 R（城市 X、C 會議皆化名）從草稿、red-team、claim-audit、hype-scrub、PDF/DOI、收 Major Revision、reviewer-response、回頭再掃、到 Accept 的一週+兩個月全程敘事，每幕含實際 invocation + 範例回傳 + R 怎麼處理，結尾對照回手冊章節。守無真實名稱規範。手冊與故事互補（reference vs narrative），雙向交叉連結 + README Contents 並列。

**Lesson：** 同一套使用方式，「參考手冊（查表）」和「情境故事（跟著走）」服務不同學習風格；本方法論一貫兩者都要（如 L5 case notes + Hermes teaching 也是）。情境故事更能帶出「為什麼這步重要」的情緒（R 冒冷汗、鬆一口氣、感激提醒），是純查表手冊給不了的。

#### 本階段第七批：三個投稿工具做成 Claude Code 原生 Skills（雙引擎，同日）

使用者問「有安裝程序嗎?應該要裝 SKILL 吧」，戳到一個我該講清楚的混淆。先用 claude-code-guide agent 確認當前機制，再給準確答案 + 問方向，使用者選「**兩份都要（Claude Skills + Codex）**」。

**澄清的事實（重要）：**
- 我先前做的三個是本 repo 的 **workflow markdown**（`.codex/workflows/`），**不是** Claude Code SKILL，也不是 WenyuChiou 那種 agentskills.io 可安裝 skill。
- Claude Code 現況：**斜線指令已併進 Skills**；原生 skill = `.claude/skills/<名>/SKILL.md`，**零安裝**（丟檔即自動發現、即時生效，不必改 settings.json）。
- **唯一有「安裝程序」的**是打包成 plugin + marketplace 給別人 `/plugin install`（如 WenyuChiou）。本 repo 不做。

**產出：**

| 檔案 | 內容 |
| --- | --- |
| `.claude/skills/claim-audit/SKILL.md` | Claude Code 原生 skill（frontmatter: name/description/argument-hint），自含程序，互指 Codex 版 |
| `.claude/skills/hype-scrub/SKILL.md` | 同上 |
| `.claude/skills/reviewer-response/SKILL.md` | 同上 |
| `.claude/skills/README.md` | Skills 索引：零安裝說明、雙引擎同步紀律、清單、frontmatter 觸發說明 |
| 3 個 `.codex/workflows/*.md` | 各加「🔗 Claude Code 對應 skill（雙引擎同步）」pointer |
| `PUBLISHING_WORKFLOW_MANUAL.md` §3 | 改寫成「兩個引擎都能用、零安裝」對照表（Claude Code skill vs Codex workflow）|

**雙引擎同步紀律**：每個工具 = 1 個 Claude skill + 1 個 Codex workflow，兩邊檔頭互指 pointer，改一份要同步另一份。

**Lesson：** 「skill」是被濫用的詞——使用者口中的「裝 SKILL」可能指三種不同東西（repo workflow / Claude 原生 skill / 可安裝 plugin）。先確認機制（用 claude-code-guide）再答，避免給錯安裝步驟。關鍵澄清：**專案內 skill 是零安裝的，只有對外散布的 plugin 才有安裝程序。**

**延伸 TODO：** 若日後要對外散布，再做 plugin（`.claude-plugin/plugin.json` + marketplace.json）——目前不做。

#### 本階段第八批：AI-Native eBook 範式升格為獨立 hub（架構決策，同日）

使用者問「要不要為這個獨立開 GitHub、讓它引用 consulting methodology 當實作案例?」。我拆出三件被綁在一起的東西（① 範式/方法論 ② 論文 ③ toolkit 案例），分析後使用者選 **C 範式 hub**。

**架構決策：** 把 ① 範式升格成獨立 repo；toolkit 降為**被引用的參考實作**；論文 DOI 與 toolkit DOI 都**只引用、不搬移**（不動已 mint 的 DOI、不打亂 provenance）。

**產出（在 toolkit repo 之外，`C:\Tools\@@@@@@Antigravity\AI-Native-eBook\`，與本 repo 平行 → 天生獨立 GitHub 專案）：**

```
AI-Native-eBook/
├── README.md          # 門面：三件事拆解圖、DOI 引用、provenance note、quick start
├── METHODOLOGY.md     # 範式本體：六大特性 + 出版閉環 + 實作步驟 + 反 AI-slop 紀律
├── CASE_STUDIES.md    # 案例索引：★toolkit 參考案例 + 聖經/學校(進行中) + 公開邀請 + 範本
├── CITATION.cff       # 引用 paper DOI(preferred) + toolkit DOI(reference)
├── NOTICE / LICENSE   # Apache 2.0(code)/CC BY 4.0(docs)；LICENSE 為 stub 待補全文
├── .gitignore
└── starter-kit/README.md  # 可重用基礎設施索引(投稿手冊/skills/Makefile/CITATION)+抽取計畫
```

**關鍵守則：** (1) 不動 toolkit/paper 已 mint 的 DOI——hub 只 reference。(2) 論文 provenance 證據(Git history、commit 7da82d7)仍在 toolkit repo，README 寫明。(3) 聖經 AI 書、學校案例列為「進行中實例」但標註「公開前需 maintainer 確認」(避免把私案曝光)。(4) 我**不能**建 GitHub 遠端/push——只做本地 scaffold。

**誠實提醒寫進 README/CASE_STUDIES：** 範式 hub 價值隨案例數成長，現成熟案例 n=1，所以老實框成「範式 + 第一個參考實作 + 公開邀請 + 進行中其他案例」。

**使用者待辦（hub 上線前）：** 決定最終 repo 名 → `git init` + 建 GitHub repo + push → LICENSE 補 Apache 2.0 全文 → 上線後回頭在 toolkit 的 09_Research_Paper README 加反向 cross-link → 決定聖經/學校案例是否公開列出。

**Lesson：** 「要不要拆 repo」先別急著動手——先拆清楚「被綁在一起的其實是幾個東西」(範式/論文/案例)，answer 自然浮現。且拆分時 DOI 是紅線：已發布的只引用不搬移，否則打亂譜系與 provenance。
