# GenAI Consulting Methodology Toolkit

語言選單：繁體中文 | [English](README_EN.md)

企業 AI 轉型成熟度診斷與導入方法論工具包。

原作者：**Tiger AI Morris Lu 盧業興**  
身份備註：**n8n Taipei 大使 / 臺灣科技大學 智慧製造所博士生 / QUT 澳洲昆士蘭科技大學 資工碩士**

授權摘要：本專案採用 **[Apache License 2.0](LICENSE)**。可自由使用、複製、修改、再散布與商業化；再散布時請保留 Apache 2.0 授權文字與 [`NOTICE`](NOTICE) 中的作者署名。

## 這套方法在解決什麼

很多企業導入 AI 時會直接跳工具：今天買 ChatGPT，明天試 n8n，下週又想做 Agent。結果常見問題是員工不會用、流程沒有接上、資料沒有治理、PoC 無法驗收，最後高層也不知道 AI 到底成熟到哪一層。

這個工具包的策略是：先用簡易問卷診斷企業目前的 AI 成熟度，再依照 L1-L5 設計課程比例與導入路徑。課程不是單純上完就結束，而是在每一層都留下可驗證交付物，最後再用 AI 轉型診斷顧問手法的八階段流程，產出完整顧問診斷報告、Roadmap、ROI 與治理建議。

## 上課前的未來想像

客戶在決定是否上 L1-L5 課程前，最需要先看見一個未來畫面：不是「我們要學五個工具」，而是「公司上完課後，日常工作會怎麼改變」。

想像三個月後的星期一早上：

- **L1 Chat AI**：每位員工用自己的帳號登入 OpenWebUI，有自己的聊天區、歷史紀錄與部門權限。業務寫客戶信、HR 整理訓練摘要、主管產出會議重點，都從同一個受控 AI 入口開始。
- **L2 Skill AI**：資深同仁不再只是自己很會做，而是把文案、報告、客服回覆、SOP 判讀、程式開發方法整理成 Skill。新人與其他部門可以沿用同一套方法，產出品質開始一致。
- **L3 Workflow AI**：n8n 開始串接 Gmail、Sheets、Notion、CRM、API、ERP。客訴信進來後，系統可以查 CRM、更新表單、建立任務、產生主管摘要，人只負責判斷與批准。
- **L4 Auto Agentic AI**：Hermes Agent 每天讀取任務、文件、Workflow 結果與 Wiki 記憶，產生 briefing、追蹤清單與需要人工 Gate 的決策點。企業開始擁有可驗證的知識型 Agent。
- **L5 Agentic Team AI**：ClawTeam 將市場、產品、客服、財務、營運等專業 Agent 編成團隊，協作完成新產品上市、品質改善、病患服務改善或客戶經營任務。

這個故事要放在課程開始前講。客戶先看懂未來工作情境，再回頭理解為什麼需要問卷診斷、為什麼課程要分 L1-L5、為什麼每一層都要有 deliverables、evidence 與 Stage Gate。

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
→ 情境案例、Evidence、Stage Gate 驗收
→ 八階段 AI 轉型顧問診斷
→ AI 轉型診斷報告、Roadmap、ROI、治理建議
```

## L1-L5 成熟度模型

| 等級 | 名稱 | 工具 / 平台 | 企業定位 |
| --- | --- | --- | --- |
| L1 | Chat AI | OpenWebUI | 建立企業內部 AI 對話入口，讓每位員工有自己的帳號、聊天區與權限邊界 |
| L2 | Skill AI | Antigravity / Claude Code / Codex | 將個人知識、提示詞、文件與工作方法整理成可重複使用的 Skill |
| L3 | Workflow AI | n8n | 串接 Gmail、Sheets、Notion、CRM、API、ERP 等系統，讓 AI 進入真實流程 |
| L4 | Auto Agentic AI | Hermes Agent | 以 Wiki 記憶、工具、Workflow、排程與人工 Gate 組成可驗證的自動 Agent |
| L5 | Agentic Team AI | ClawTeam | 讓多個專業 Agent 形成團隊，協同完成跨部門、跨流程的企業任務 |

## 每一層如何驗收

| 等級 | Input | Process | Output | Evidence | Stage Gate |
| --- | --- | --- | --- | --- | --- |
| L1 | 員工角色、常見任務、AI 使用痛點、權限需求 | 建置 OpenWebUI、帳號 / 群組 / 權限、個人聊天區、Prompt 基礎訓練 | 企業 AI 對話入口、Prompt 清單、使用情境清單 | 帳號表、權限表、登入紀錄、個人聊天區截圖、Prompt 範例 | 是否能安全登入、分權、留下可追蹤使用紀錄 |
| L2 | L1 高頻 Prompt、文件、SOP、個人工作方法 | 用 Antigravity / Claude Code / Codex 將知識封裝成 Skill 與可重用 artifacts | Skill Library、Agentic artifacts、Workflow Blueprint | Skill 文件、測試案例、版本紀錄、輸出範例 | Skill 是否可被他人重複使用並穩定產出 |
| L3 | L2 Skill、流程藍圖、系統清單、API / CRM / ERP / Sheet 權限 | 用 n8n 建立自動化流程、資料表、Execution Log、錯誤處理 | Workflow PoC、Sub-workflow Library、Data Tables、L4 Workflow Contract | n8n workflow、執行紀錄、失敗重跑紀錄、系統串接截圖 | Workflow 是否能在真實資料與真實系統中穩定執行 |
| L4 | L3 Workflow、L2 Skill、企業 Wiki、任務規則、人工 Gate | 用 Hermes Agent 建立任務卡、Wiki ingest/query/update、排程、工具調用與 Gate 4A-4E | 可驗證 Agent、Briefing、任務處理紀錄、Gate 簽核 | Agent log、Wiki 版本、任務卡、briefing、人工批准紀錄 | Agent 是否能在受控邊界內自動完成任務並留下 evidence |
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
