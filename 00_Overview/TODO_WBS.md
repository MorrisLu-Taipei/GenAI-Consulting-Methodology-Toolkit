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
- [x] 參考 OpenWebUI playlist 補強 L1 企業啟用課：每人登入、個人聊天區、Admin Panel、帳號/角色/群組/權限、模型控管、影片參考地圖。
- [x] L2 Skill AI 課程目標、課綱、練習、產出物、講師備註。
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
  - Stage 6 Roadmap + Gate 1-5 Checklist + Risk Register
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
| Git：已 push | …（截至 `db42c15`）；2026-05-15 大批次：8 目錄 README 改寫、改名 GenAI、問卷白話化、14 個 `_EN` sibling、L1-L5 兩條軸精煉（截至 `2604a37`） |
| Git：本地待 push | 7 目錄 README_EN 同步 + DELIVERY_PACKAGE L1-L3/L4-L5 交付範圍 + Gate 術語清理 + 本次 TODO 更新 |
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

- Repo 授權 / 署名整備：CC BY 4.0 → Apache 2.0、新增 `NOTICE`、中英雙語署名、致謝 Prof. Michael Rosemann (QUT)、作者學歷補 QUT 資工碩士。
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
- **身份署名加 QUT**：NOTICE / README / 90_References / 銷售簡報全部加註「QUT 澳洲昆士蘭科技大學 資工碩士」。
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
