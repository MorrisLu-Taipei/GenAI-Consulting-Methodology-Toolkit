# GenAI Consulting Methodology Toolkit

語言選單：繁體中文 | [English](README_EN.md) | [ภาษาไทย](README_TH.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [日本語](README_JA.md) | [한국어](README_KR.md)

企業 AI 轉型成熟度診斷與導入方法論工具包。

原作者：**Tiger AI Morris Lu 盧業興**  
身份備註：**n8n Taipei 大使 / 臺灣科技大學 智慧製造所博士生 / QUT 澳洲昆士蘭科技大學 資工碩士**

授權摘要：本專案採用 **[Apache License 2.0](LICENSE)**。可自由使用、複製、修改、再散布與商業化；再散布時請保留 Apache 2.0 授權文字與 [`NOTICE`](NOTICE) 中的作者署名。

> **只有 5 分鐘？** 先讀 [`00_Overview/EXECUTIVE_SUMMARY.md`](00_Overview/EXECUTIVE_SUMMARY.md) —— 一頁看懂這套方法論。

---

## 🌟 這不是一本書，是 AI-Native Living Book ── 一本真實「活」的書

書本一路演化過來，每一代都解決了一個問題，但也留下一個缺口 —— **一直都不是「活」的**：

- **第 1 代　印刷書**：把知識保留下來、傳給下一個讀者。但它**只能被讀，不會回應**，不能回答你的問題，也不知道你公司長什麼樣 —— 是一份**靜止的紙**。
- **第 2 代　互動書**：搬上網頁與 Wiki 之後，可以搜尋、跳轉、留言。比印刷書多了「**互動**」，但仍然**不會主動建議**你什麼，更不會替你分析、產出新東西 —— 還是被動的，只是介面活了，內容沒活。
- **第 3 代　AI-Native Book（本 repo）── 真正「活」起來的書**：用 Markdown 寫成方法論本體，再用 AI IDE 打開 ── AI 自動讀完整本書，**讓你問、幫你答、陪你想**，並且**依你公司的真實情境給出客製化建議、跑診斷、寫報告草稿、做模擬演練**。書本身會回應、會延伸、會跟著你的問題長出新的章節。

換句話說：印刷書傳承知識、互動書方便查找，**AI-Native Book 第一次讓「書」真正活起來 —— 變成可以陪你一起想事情的夥伴**。最終決策仍然由人類做，但你不再是一個人面對一份靜態的方法論。

> *Three generations of books: printed (read-only, dead) → interactive (search & link, still passive) → **AI-native (truly alive — advises, analyzes, simulates, and grows with your questions)**. Open with an AI IDE; AI becomes your reading partner, consulting assistant, and auditor.*

### 🔱 三個 AI 引擎，各自擅長不同的事

同一份內容，依您選擇的 AI IDE 顯現**完全不同的人格**：

| 引擎 | 角色 | 它最擅長的事 |
| --- | --- | --- |
| 🟦 **Antigravity** | 前線顧問 | 跟客戶對話、跑問卷、產報告草稿 |
| 🟪 **Codex CLI** | 方法論稽核員 | 跨檔測試、紅隊演練、版本控管、修補斷鏈 |
| 🟨 **Claude Code** | 跨檔思考夥伴 | 深度綜合、多視角辯論、模擬演練、客戶分叉 |

三個引擎不互相取代，而是**分工合作**：上午用 Antigravity 跟客戶開會，下午用 Codex 稽核報告草稿，晚上用 Claude Code 跑情境模擬。各自的工作流空間獨立（`.agent/` / `.codex/` / `.claude/`），互不干擾。

每個引擎的詳細自述見 [`07_AI_Contributions/`](07_AI_Contributions/)；安裝步驟見下方[三 AI 引擎安裝與啟動指南](#-三-ai-引擎安裝與啟動指南--three-ai-engines-setup-guide)。

### 對不同身分的讀者，這代表什麼

- **CEO / 高管**：把這個 repo 丟給 ChatGPT / Claude / Gemini，10 分鐘問答就能得到「我公司在哪一級？該先做什麼？」的初步判斷。
- **顧問 / 學員**：用 AI IDE 打開，能跑完整套對話式顧問體驗 ── 從診斷、報告、到 24 個月落地 Roadmap。
- **學者 / 研究者**：可以直接跑 `/devil-pair-debate`、`/thought-experiment` 來辯論方法論的價值觀預設，背後有 7 大理論支柱與 28 篇 classics 可引用。
- **監管 / 法遵**：跑 `/evidence-audit`、`/generate-traceability` 取得可審計的證據鏈，並對齊 NIST AI RMF / EU AI Act / ISO 42001。

> ⚠️ **誠實揭露**：方法論的整體架構由 **Morris Lu（人類）** 設計，三個 AI 引擎只是執行、完善、稽核工具。詳見 [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0。書中所有案例為 AI 模擬教學用途，**非真實客戶資料**。

---

## 這套方法在解決什麼

很多企業導入 AI 時會直接跳工具：今天買 ChatGPT，明天試 n8n，下週又想做 Agent。結果常見問題是員工不會用、流程沒有接上、資料沒有治理、PoC 無法驗收，最後高層也不知道 AI 到底成熟到哪一層。

這個工具包的策略是：先用簡易問卷診斷企業目前的 AI 成熟度，再依照 L1-L5 設計課程比例與導入路徑。課程不是單純上完就結束，而是在每一層都留下可驗證交付物，最後再用 AI 轉型診斷顧問手法的八階段流程，產出完整顧問診斷報告、Roadmap、ROI 與治理建議。

## 上課前的未來想像

客戶在決定是否上 L1-L5 課程前，最需要先看見一個未來畫面：不是「我們要學五個工具」，而是「公司上完課後，日常工作會怎麼改變」。

故事主線是**規模一層一層擴大、最後從『人用 AI』長出『AI 自己幹活』**：**個人 → 部門 → 跨部門/全公司 → AI 超級助理（個體）→ AI 團隊**。想像三個月後的星期一早上：

- **L1 Controlled AI Access ─ 規模軸·個人**：**每位員工各自一個人**用自己的帳號登入 OpenWebUI，有自己的聊天區、歷史紀錄與部門權限。業務寫客戶信、HR 整理訓練摘要、主管產出會議重點，都從同一個受控 AI 入口開始 —— **單位是「個人」**，AI 在每個人身邊。
- **L2 Knowledge Codification ─ 規模軸·部門**：**單位升級為「部門」**。資深同仁不再只是自己很會做，而是以**部門職責為邊界**，把文案、報告、客服回覆、SOP 判讀、程式開發方法整理成可複用 Skill。新人與部門內其他人沿用同一套方法，**部門整體**產出品質開始一致。
- **L3 Workflow Automation ─ 規模軸·跨部門 / 全公司**：**單位再升級為「跨部門、全公司」**。n8n 把各部門的 Skill 與系統（Gmail、Sheets、Notion、CRM、API、ERP）串起來，一封客訴信進來能**穿越業務、客服、CRM、主管多個部門**自動處理 —— 系統查 CRM、更新表單、建立任務、產生主管摘要，人只負責判斷與批准。AI 開始進入**全公司流程**。
- **L4 Autonomous Agent ─ AI 自主軸·超級助理（AI 個體）**：**從「人類部隊」之外，多長出一個 AI 實體**。Hermes Agent 每天讀取任務、文件、Workflow 結果與 Wiki 記憶，產生 briefing、追蹤清單與需要 HITL（Human-in-the-Loop，人類在迴圈內審核）的決策點。企業開始擁有**可驗證的知識型 AI 個體**，像多請了一個全自動超級助理。
- **L5 Multi-Agent Organization ─ AI 自主軸·AI 團隊**：**多個 L4 個體再編成一支「AI 團隊」**。ClawTeam 把市場、產品、客服、財務、營運等專業 Agent 組成職能分工，協作完成新產品上市、品質改善、病患服務改善或客戶經營任務 —— 企業同時擁有「**人類團隊 + AI 團隊**」兩支隊伍。

這個故事要放在課程開始前講。客戶先看懂「規模如何一層一層擴大、AI 如何從工具長成數位人力」，再回頭理解為什麼需要問卷診斷、為什麼課程要分 L1-L5、為什麼每一層都要有 deliverables、evidence 與階段驗收關卡（Stage Gate）。

> ⚠️ 更詳細的兩軸解釋（為什麼 L3 → L4 是關鍵分界、為什麼治理始終由人保有）見下方 [§L1-L5 的兩條軸](#l1-l5-的兩條軸)。

## AI 成熟度地圖

![AI 成熟度地圖](90_References/MD-Map.png)

## 方法論總覽

![企業管理顧問方法論：八階段轉型指南](90_References/Metholodgy.png)

## 核心故事線

```text
AI 成熟度問卷
→ 公司屬性、產業情境、部署模式調查
→ L1-L5 課程比例設計
→ L1 OpenWebUI 企業帳號與個人聊天區啟用
→ L2 Antigravity / Claude Code / Codex Skill 化訓練
→ L3 n8n 串接 Gmail、Sheets、Notion、CRM、API、ERP 等系統
→ L4 Hermes Agent 形成可驗證的自動 Agent 作業
→ L5 ClawTeam 形成 Agentic Team 協作
→ 情境案例、Evidence、階段驗收關卡（Stage Gate）
→ 八階段 AI 轉型顧問診斷
→ AI 轉型診斷報告、Roadmap、ROI、治理建議
```

## L1-L5 成熟度模型

| 等級 | 名稱 | 工具 / 平台 | 軸 | 企業定位 |
| --- | --- | --- | --- | --- |
| L1 | Controlled AI Access | OpenWebUI | 規模軸·個人 | 建立企業內部 AI 對話入口，讓每位員工有自己的帳號、AI 聊天區與權限邊界 |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | 規模軸·部門 | 以部門職責為單位，將個人知識、提示詞、文件與工作方法整理成可重複使用的 Skill |
| L3 | Workflow Automation | n8n | 規模軸·跨部門 / 全公司 | 串接跨部門 Skill 並連接 email、Sheets、Notes、CRM、API、ERP 等系統，讓 AI 進入全公司自動化流程 |
| L4 | Autonomous Agent | Hermes Agent | AI 自主軸·超級助理 | 以 Wiki 職能地圖、AI 工具、Workflow、自動排程、自主學習組成可驗證的全自動 AI Agent 超級助理 |
| L5 | Multi-Agent Organization | ClawTeam | AI 自主軸·AI 團隊 | 讓多個專業 Agent 形成職能分工，協同完成跨部門、跨流程的企業任務 AI 團隊 |

### L1-L5 的兩條軸

L1-L5 不是「五個工具」，而是**兩條軸**接起來的成熟度路徑：

- **L1 → L2 → L3：規模軸（人類使用 / 監督 AI）。** 這三層是「人在迴圈內、人用 AI、人監督 AI」的階段，沿著組織規模逐層放大 —— **L1 個人**（每位員工各自用 AI）→ **L2 部門**（以部門職責為單位把個人知識封裝成可複用 Skill）→ **L3 跨部門 / 全公司**（把跨部門 Skill 串起來、接上系統，AI 進入全公司自動化流程）。
- **L4 → L5：AI 自主軸（AI 完全自主，不需人類即時監督）。** 這兩層是企業在人類部隊之外「額外長出來」的 AI 實體 —— **L4 AI 超級助理**（全自動 AI Agent 個體）→ **L5 AI 團隊**（多個專業 Agent 職能分工協作）。

> 關鍵分界：**L1-L3 是「人類輔助 / 監督 AI」，AI 是工具；L4-L5 是「AI 自主運作」，AI 是企業額外的數位人力。** 導入順序上，L1-L3 先把人與組織帶起來，L4-L5 才在穩固的基礎上長出自主 AI。
>
> 即使到了 L4-L5，**治理框架仍由人建立、人保有監督權** —— AI 自主的是「營運執行」，不是「治理決策」。每一層都保留 HITL（Human-in-the-Loop，人類在迴圈內審核）與階段驗收關卡，AI 愈自主，人的角色就愈往「治理者」升級，而不是被取代。

## 每一層如何驗收

| 等級 | Input | Process | Output | Evidence | 階段驗收關卡（Stage Gate）|
| --- | --- | --- | --- | --- | --- |
| L1 | 員工角色、常見任務、AI 使用痛點、權限需求 | 建置 OpenWebUI、帳號 / 群組 / 權限、個人聊天區、Prompt 基礎訓練 | 企業 AI 對話入口、Prompt 清單、使用情境清單 | 帳號表、權限表、登入紀錄、個人聊天區截圖、Prompt 範例 | 是否能安全登入、分權、留下可追蹤使用紀錄 |
| L2 | L1 高頻 Prompt、文件、SOP、個人工作方法 | 用 Antigravity / Claude Code / Codex 將知識封裝成 Skill 與可重用 artifacts | Skill Library、Agentic artifacts、Workflow Blueprint | Skill 文件、測試案例、版本紀錄、輸出範例 | Skill 是否可被他人重複使用並穩定產出 |
| L3 | L2 Skill、流程藍圖、系統清單、API / CRM / ERP / Sheet 權限 | 用 n8n 建立自動化流程、資料表、Execution Log、錯誤處理 | Workflow PoC、Sub-workflow Library、Data Tables、L4 Workflow Contract | n8n workflow、執行紀錄、失敗重跑紀錄、系統串接截圖 | Workflow 是否能在真實資料與真實系統中穩定執行 |
| L4 | L3 Workflow、L2 Skill、企業 Wiki、任務規則、HITL 人類審核點 | 用 Hermes Agent 建立任務卡、Wiki ingest/query/update、排程、工具調用與驗收關卡 4A-4E | 可驗證 Agent、Briefing、任務處理紀錄、驗收關卡簽核 | Agent log、Wiki 版本、任務卡、briefing、人類批准紀錄 | Agent 是否能在受控邊界內自動完成任務並留下 evidence |
| L5 | 多個 L4 Agent、跨部門任務、角色責任、治理規則 | 用 ClawTeam 編組 Agentic Team，定義角色、協作規則、交接與監督方式 | Agent Team、角色卡、協作流程、跨部門成果 | Team run log、角色卡、交接紀錄、成果文件、治理紀錄 | Agent Team 是否能穩定協作並產出可追責成果 |

## 課程設計原則

課程比例由客戶的成熟度、產業、部署模式與目標情境決定。不是每家公司都要一次上滿 L1-L5，而是先找出最能產生交付成果的一層，往上銜接。

| 調查面向 | 用途 |
| --- | --- |
| 公司屬性 | 判斷是研發製造業、行銷服務業、醫療院所、內部營運單位或其他類型 |
| 部署模式 | 判斷走雲 AI、Hybrid 雲地混合，或全地端部署 |
| 系統現況 | 盤點 Gmail、Sheets、Notion、CRM、API、ERP、資料庫與內部系統 |
| 流程成熟度 | 判斷是否已有 SOP、流程 owner、資料欄位與例外處理 |
| 風險要求 | 評估資安、隱私、醫療 / 製造 / 財務合規與人工簽核需求 |

## 目錄結構

| 目錄 | 用途 |
| --- | --- |
| [`00_Overview`](00_Overview/) | 方案總論、故事線、WBS |
| [`01_Assessment`](01_Assessment/) | AI 成熟度問卷、評分模型、交付物與驗證矩陣 |
| [`02_Course_Design`](02_Course_Design/) | L1-L5 課程規劃、公司屬性、部署模式、課程模組矩陣 |
| [`03_Consulting_Report`](03_Consulting_Report/) | AI 轉型診斷報告模板 |
| [`04_Scenarios`](04_Scenarios/) | 客戶情境、控制表、製造業案例、醫院案例 |
| [`05_Sales`](05_Sales/) | 對外價值主張、銷售話術與 FAQ |
| [`06_Delivery`](06_Delivery/) | 交付包與驗收標準 |
| [`90_References`](90_References/) | 原始 PDF、方法論圖片、影片學習紀錄與引用資料 |

## 想看故事的 5 種人，從這 5 份開始

| 您是 | 從這份開始 |
| --- | --- |
| **CEO / 老闆 / 家人** ── 想 20 分鐘看懂這套方法論做什麼 | [`00_Overview/CLIENT_JOURNEY_STORY.md`](00_Overview/CLIENT_JOURNEY_STORY.md) — 阿明的故事 |
| **顧問 / 學員** ── 想知道八階段怎麼跑、合約怎麼分 | [`00_Overview/EIGHT_STAGE_FLOW_STORY.md`](00_Overview/EIGHT_STAGE_FLOW_STORY.md) — 完整流程 |
| **董事會 / 監管者 / 學術** ── 想知道為什麼這方法論經得起辯論 | [`00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md`](00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md) — 科學論證 |
| **大企業 IT / 跳槽顧問** ── 想知道跟 McKinsey/BCG/TOGAF/Gartner 怎麼對齊 | [`00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md`](00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md) — 對齊地圖 |
| **趕時間的主管** ── 只有 5 分鐘 | [`00_Overview/EXECUTIVE_SUMMARY.md`](00_Overview/EXECUTIVE_SUMMARY.md) — 執行摘要 |
| **方法論研究者 / AI Pedagogy 學者** ── 為什麼這是新型態方法論 | [`00_Overview/AI_NATIVE_LIVING_BOOK.md`](00_Overview/AI_NATIVE_LIVING_BOOK.md) — AI-Native Living Book 設計 |
| **學者 / 監管 / 董事會** ── 7 大理論支柱（Rosemann / Cohen & Levinthal / Teece / Real Options 等）| [`00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) — 學術理論基礎 |
| **顧問 / 評分校準** ── 0-4 分要怎麼客觀評，避免主觀 | [`01_Assessment/BARS_RUBRICS.md`](01_Assessment/BARS_RUBRICS.md) — BARS 行為錨點 |

## 建議閱讀順序

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md)
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md)
4. [`01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)
5. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
6. [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md)
7. [`02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md)
8. [`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md)
9. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md)
10. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md)
11. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)
12. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)

## 可驗證交付物

- AI 成熟度問卷與評分結果
- 公司屬性與部署模式調查
- L1-L5 課程完成證據
- OpenWebUI 帳號 / 群組 / 權限表與每人個人聊天區啟用紀錄
- Skill Library 與 Antigravity / Claude Code / Codex artifacts
- n8n Workflow PoC、Execution Log、Data Tables、Sub-workflow Library
- Hermes Agent 任務卡、Wiki、ingest/query/update 紀錄、briefing 與 Gate 4A-4E
- ClawTeam Agent Team 角色卡、協作紀錄與成果文件
- Stage Gate 驗收紀錄
- AI 轉型診斷報告
- 30 / 60 / 90 天 Roadmap

## 參考資料

- [`90_References/@AI-MD-PUBIC.pdf`](90_References/@AI-MD-PUBIC.pdf)
- [`90_References/MD-Map.png`](90_References/MD-Map.png)
- [`90_References/Metholodgy.png`](90_References/Metholodgy.png)
- [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md)
- [`90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

## 致謝

特別感謝 **Prof. Michael Rosemann**，Queensland University of Technology (QUT), Brisbane, Australia。  
Profile: <https://www.qut.edu.au/about/our-people/academic-profiles/m.rosemann>

本 repo 整套顧問方法論的學理基礎，來自作者於 QUT 昆士蘭科技大學求學期間，Prof. Michael Rosemann 在 **Business Process Management (BPM)**、**Capability Maturity Models** 與 **企業創新方法論** 上的長期啟發與教導。

其中兩個核心設計特別受到影響：

- **八階段顧問結構**：對應企業流程診斷、能力評估、轉型路徑設計與治理落地。
- **L1-L5 AI 成熟度模型**：參考能力成熟度模型的層級邏輯，並在地化為企業導入 AI 的五層銜接架構。

免責聲明：本方法論中任何錯誤、遺漏、在地化調整或對 AI 領域的延伸應用，皆為作者 Tiger AI Morris Lu 盧業興個人責任，不代表 Prof. Michael Rosemann 或 QUT 之觀點或立場。

## 授權與署名

本專案採用 **[Apache License 2.0](LICENSE)** 授權。您可以自由使用、複製、修改、改作、重製、散布、教學、顧問交付與商業化。

再散布、改作、商業包裝、課程教材、顧問交付文件或產品文件中，請依 Apache 2.0 條款保留授權文字與 [`NOTICE`](NOTICE) 中的以下署名：

```text
原作者：Tiger AI Morris Lu 盧業興
身份：n8n Taipei 大使 / 臺灣科技大學 智慧製造所博士生 / QUT 澳洲昆士蘭科技大學 資工碩士
來源：https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit
```

第三方平台名稱、商標、影片、外部專案與引用內容仍屬於各自權利人。本 repo 對第三方資料僅做學習紀錄、引用、整理與課程設計參考。

---

## 把這本書讀活：和 AI 一起讀

下方的安裝指南會帶你把 repo 接上 AI IDE。在動手之前，先了解這個操作模型 + 一條紅線。

**操作模型一句話**：`git clone` 或下載 zip → 用 AI IDE（Antigravity / Claude Code / Codex 等）打開 → AI 自動讀 [`AGENTS.md`](AGENTS.md)（與各引擎自己的 `<ENGINE>.md`），把自己定位成**這套方法論的共讀導師**。然後你就能（1）問它關於這套方法論的任何問題、（2）請它把方法論套到你公司的情況、（3）跟著它做 L1-L5 自我診斷、找出下一步。

完整論述見 [`00_Overview/AI_NATIVE_LIVING_BOOK.md`](00_Overview/AI_NATIVE_LIVING_BOOK.md)。

> ⚠️ **學術誠信聲明 / Academic Integrity Disclaimer**
>
> **本 repo 中所有具名案例（製造、醫院、行銷、B2B、金融、政府、教育 7 個 SAMPLE_CLIENT_CASE）與所有故事主角（如「阿明」「明強封測」），皆為 AI 模擬產生的虛構案例**。
> 所有數字（時間、ROI、人月、預算、KPI）僅為**示例**，**不可作為對外宣傳、合約承諾、學術 empirical evidence**。
> 真實 longitudinal cases 需透過 [`90_References/PILOT_STUDY_PROTOCOL.md`](90_References/PILOT_STUDY_PROTOCOL.md) 18-24 個月實證研究完成後才會替換。
>
> **All named cases and story protagonists in this repo are AI-generated fictional examples**, NOT real client data. Numbers are illustrative; real cases will replace after the pilot study.

## 🚀 三 AI 引擎安裝與啟動指南 / Three AI Engines Setup Guide

三個引擎的**角色定位與分工**已在頂部「🔱 三個 AI 引擎，各自擅長不同的事」介紹完畢。本節聚焦**怎麼裝、怎麼啟動、怎麼呼叫工作流**。三個區塊獨立可選，挑你要用的引擎讀那一段即可。

> ⚠️ **依 [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0**：方法論架構、L1-L5、八階段、3 引擎分工等戰略設計皆由 **Morris Lu（人類）** 提出。三個 AI 引擎在 Morris 的指導下**執行、完善、展開、稽核**，不主張對方法論架構的所有權。每個引擎的詳細自述見 [`07_AI_Contributions/`](07_AI_Contributions/) 對應檔案。

---

### 🟦 1. Antigravity 使用者 — 前線互動式顧問

> 把這本「靜態的活書」直接升級為您的「**對話式虛擬顧問應用程式 (Conversational Consulting App)**」。

**安裝與使用步驟：**

1. **載入專案**：將本專案 `git clone` 或下載 zip 到本地端
2. **啟動 IDE**：使用 Antigravity 打開本專案資料夾
3. **自動初始化**：Antigravity 自動讀取 [`ANTIGRAVITY.md`](ANTIGRAVITY.md) 與 [`SKILL.md`](SKILL.md)，將自身定位為「**共讀導師**」
4. **執行工作流（Slash Commands）**：在對話框輸入指令啟動互動

**常用 Antigravity 指令：**

- `/diagnose` ── 啟動擬真對話，引導您（或您的客戶）進行 L1-L5 企業 AI 成熟度診斷
- `/generate-report` ── 將先前診斷與討論結果，一鍵寫入標準顧問報告模板並產出草稿

詳見 [`.agent/workflows/`](.agent/workflows/) 與 [`07_AI_Contributions/ANTIGRAVITY.md`](07_AI_Contributions/ANTIGRAVITY.md)。

> Antigravity 的核心價值：把方法論變成**客戶聽得懂、可立即互動**的顧問體驗。

---

### 🟪 2. Codex 使用者 — 方法論工程化引擎

> 把本 repo 視為一套「**方法論工程化工作區**」—— 把這本 AI-native living book 當成**可測試、可稽核、可追溯、可修補、可發版**的方法論產品來維護。

**安裝與使用步驟：**

1. **載入專案**：將本專案 `git clone` 或下載 zip 到本地端
2. **啟動 Codex**：在 Codex 中打開本專案資料夾
3. **讀取 Codex 入口**：先讓 Codex 閱讀 [`CODEX.md`](CODEX.md) 與 [`.codex/README.md`](.codex/README.md)
4. **執行 Codex 工作流**：在對話中輸入工作流名稱，或明確要求 Codex 依對應檔案執行

**常用 Codex 指令（10 個）：**

| 類別 | 指令 | 用途 |
| --- | --- | --- |
| 生產 | `/diagnose` | 互動式 AI 成熟度初判 |
| 生產 | `/generate-report` | 顧問診斷報告草稿 |
| 品管 | `/evidence-audit` | 檢查報告 evidence chain |
| 品管 | `/consistency-review` | 跨文件檢查 L1-L5、Stage Gate、HITL、Evidence 一致性 |
| 演化 | `/academic-upgrade` | 將學術建議轉成方法論修補方案 |
| 演化 | `/harvest-insights` | 從多份交付報告收割共通洞察 |
| 防禦 | `/test-methodology` | 對方法論做極端情境壓力測試 |
| 防禦 | `/red-team-review` | 對顧問報告做紅隊審查 |
| 稽核 | `/generate-traceability` | 產生問卷→成熟度→證據→報告追溯矩陣 |
| DevOps | `/bump-version` | 產出語意化版本與 CHANGELOG 建議 |

**建議呼叫方式：**

```text
請依 .codex/workflows/evidence-audit.md 檢查這份顧問報告草稿。
```

詳見 [`.codex/workflows/`](.codex/workflows/) 與 [`07_AI_Contributions/CODEX.md`](07_AI_Contributions/CODEX.md)。

> Codex 的核心價值：讓這套方法論具備「**可測試、可稽核、可追溯、可修補、可發版**」的工程化生命週期。

---

### 🟨 3. Claude Code 使用者 — 跨檔戰略思考與實驗引擎

> 把方法論**演 / 試 / 拆 / 撞**一次。利用 Claude Code 1M context + 多角色並行 + 跨領域抽象推理，做**模擬、實驗、辯論、分叉**。

**安裝與使用步驟：**

1. **載入專案**：將本專案 `git clone` 或下載 zip 到本地端
2. **啟動 Claude Code**：在 Claude Code CLI / IDE 中打開本專案資料夾
3. **讀取 Claude Code 入口**：先讓 Claude Code 閱讀 [`CLAUDE.md`](CLAUDE.md) 與 [`.claude/README.md`](.claude/README.md)
4. **執行 Claude Code 工作流**：在對話中輸入工作流名稱

**常用 Claude Code 指令（10 個）：**

| 類別 | 指令 | 用途 |
| --- | --- | --- |
| Tier 1 戰術 | `/deep-synthesize` | 跨多檔深度綜合（1M context）|
| Tier 1 戰術 | `/theory-bridge` | 客戶情境 ↔ 7 大理論支柱對應 |
| Tier 1 戰術 | `/scenario-planning` | 給定限制產出 3 個對比 roadmap + tradeoff |
| Tier 1 戰術 | `/socratic-challenge` | 蘇格拉底式逼問磨利使用者思考 |
| Tier 1 戰術 | `/cross-stage-trace` | 追蹤單一變動的 downstream 影響 |
| Tier 2 原創 | `/simulate-engagement` | 30 分鐘跑完完整 6 週顧問案（產出 12+ deliverable）|
| Tier 2 原創 | `/parallel-perspectives` | 6 個利害關係人**同時**對同一決策發聲 + 衝突地圖 |
| Tier 2 原創 | `/thought-experiment` | 方法論的 counterfactual 壓測（「如果 EU AI Act 把 L4 列違法呢？」）|
| Tier 2 原創 | `/devil-pair-debate` | 雙 Claude 真實辯論 + 法官綜合 |
| Tier 2 原創 | `/methodology-fork` | 把標準方法論分叉成客戶特化版（Methodology-as-Code）|

**建議呼叫方式：**

```text
請依 .claude/workflows/simulate-engagement.md 模擬一個 500 人製造業客戶的 6 週顧問案。
```

詳見 [`.claude/workflows/`](.claude/workflows/) 與 [`07_AI_Contributions/CLAUDE_CODE.md`](07_AI_Contributions/CLAUDE_CODE.md)。

> Claude Code 的核心價值：把方法論從「**標準**」進化為「**標準 + N 個衍生版 + 完整模擬 + 多視角辯論**」的可實驗活書。

---

### 三引擎協作建議 / Three-Engine Workflow Suggestions

實務上常見的協作節奏：

```text
Phase A 客戶診斷
  → Antigravity 跑 /diagnose 收集現況
  → Claude Code 跑 /theory-bridge 對應理論診斷
  → Antigravity 跑 /generate-report 產中期報告草稿
  → Codex 跑 /evidence-audit 稽核 evidence chain
  → Codex 跑 /consistency-review 跨檔對齊

Phase B 策略設計
  → Claude Code 跑 /scenario-planning 給 3 個 roadmap
  → Claude Code 跑 /parallel-perspectives 6 利害關係人視角
  → Codex 跑 /red-team-review 紅隊攻擊過度樂觀
  → Claude Code 跑 /devil-pair-debate 辯論價值觀預設

Phase C 落地與演化
  → Codex 跑 /generate-traceability 季度稽核
  → Claude Code 跑 /thought-experiment 抗 counterfactual 壓測
  → Codex 跑 /bump-version 維護方法論版本
  → Claude Code 跑 /methodology-fork 為大客戶建立衍生版
```

> 三個引擎的工作流並非互斥，**重點是各自做自己最擅長的事**，由人類（顧問 / 客戶 owner / Sponsor）決定何時切換引擎。
