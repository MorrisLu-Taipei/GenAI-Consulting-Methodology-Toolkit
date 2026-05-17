# 90 References — 參考資料、依據與致敬名單

> 🌐 語言：繁體中文 ｜ [English](README_EN.md) ｜ [Deutsch](README_DE.md) ｜ [Français](README_FR.md) ｜ [Español](README_ES.md) ｜ [日本語](README_JA.md) ｜ [한국어](README_KR.md)

## 一、本目錄定位

本目錄是整套方法論的**依據庫、引用治理中心、與致敬名單**。`00`-`07` 是「方法與工具」；本目錄回答三件事：

1. **這些方法的依據是什麼？**（PDF 原稿、方法論圖、影片學習筆記）
2. **哪些內容引用了第三方？授權合不合規？**（每個被引用的專案都有獨立 `*_REFERENCE.md`）
3. **我們站在哪些開源前輩的肩膀上？**（致敬名單）

使用本目錄的人：顧問、reviewer、法務、再散布者、**想找上游專案的學員與愛好者**。

---

## 二、致敬名單：我們站在誰的肩膀上

依使用層次分四類：**核心平台 / 顧問框架類 / Agent 與 Skill 類 / 案例索引類**。每一張「致敬卡」都附**上游 URL + 我們在哪裡引用 + 完整 _REFERENCE.md 連結**。

### 2.1 核心平台（L1-L5 的執行底座）

這些不是「被引用的素材」，而是 **L1-L5 課程直接運行其上的平台**。沒有它們，這套方法論落不了地。

#### 🎯 [`open-webui/open-webui`](https://github.com/open-webui/open-webui)（開源，授權見上游 LICENSE）

- **是什麼**：開源、可自架（self-hosted）的企業級 AI 對話介面。支援多種 LLM provider（OpenAI / Anthropic / Ollama / OpenRouter / Azure 等）、帳號 / 群組 / 角色 / 權限、個人聊天區、模型控管、Pipelines、Function Calling、知識庫、RAG、影像、音訊、檔案上傳。
- **為什麼欣賞**：少數把「**企業內部 AI 對話入口**」整套做成「**一鍵可裝、純地端、權限分層、可審計**」的開源方案。讓企業在試 LLM 時不必把資料丟給 SaaS，這是地端部署、製造業 / 醫療 / 政府等高敏感資料企業的關鍵。社群活躍、版本演化快。
- **我們在哪裡用**：**L1 Controlled AI Access 的核心平台** —— [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) 完整課綱（每人登入、個人聊天區、Admin Panel、帳號 / 角色 / 群組 / 權限、模型控管、資料規範）；影片學習筆記在 [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md)。

#### 🎯 [`n8n-io/n8n`](https://github.com/n8n-io/n8n)（Sustainable Use License，授權見上游 LICENSE.md）

- **是什麼**：開源的工作流程自動化平台。視覺化編輯器、1000+ integrations（Gmail、Sheets、Notion、Slack、CRM、API、ERP、資料庫、Webhook、自家函式庫等）、Sub-workflow Library、Data Tables、執行紀錄、錯誤處理、排程觸發、AI / LangChain 節點。支援 self-host 與 cloud。
- **為什麼欣賞**：跨系統自動化的「**樂高積木**」—— 顧問可在 1-2 天內串出 PoC 給客戶看效果；社群活躍、模板豐富、商業模式健康。**可自架是企業導入的關鍵**（資料不外流）。Tiger AI 作者是 n8n Taipei 大使，社群第一手經驗。
- **我們在哪裡用**：**L3 Workflow Automation 的核心引擎** —— [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) 完整課綱；35 個可實作 PoC 規格在 [`../02_Course_Design/POC_SCENARIO_SPECS.md`](../02_Course_Design/POC_SCENARIO_SPECS.md)；30 個 workflow JSON 骨架在 [`../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md`](../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md)；影片學習筆記在 [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md)。

#### 🎯 [`nousresearch/hermes-agent`](https://github.com/nousresearch/hermes-agent)（Nous Research，授權見上游 LICENSE）

- **是什麼**：Nous Research 開源的 **Knowledge-grade Autonomous Agent** 參考實作 —— **Wiki 職能地圖記憶 + ingest / query / update 三段式知識複利 + 排程任務 + Gate 4A-4E 階段驗收 + HITL 人類審核**。設計目標：可被驗證的「全自動 AI Agent 超級助理」。
- **為什麼欣賞**：把「**自主 Agent + 知識管理**」整合成可被驗證的設計範式 —— **「知識型 Agent 七大設計原則」**（白天輕夜間重 / 知識複利閉環 / P1>P2 / 寫讀同源 / 工具與 LLM 分工 / 失敗驅動學習 / 為何不只用 RAG）對 L4 Agent 設計提供完整的學習框架。Nous Research 在開源 LLM 與 Agent 領域的長期貢獻，是社群信任的來源之一。
- **我們在哪裡用**：**L4 Autonomous Agent 課程的設計骨幹** —— [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) §2 完整介紹七大設計原則。**邊界**：本課程**只取概念與設計範式，不重製原始碼、不做 fork**；學員上線時應依自身環境設計實作。

#### 🎯 [`HKUDS/ClawTeam`](https://github.com/HKUDS/ClawTeam)（HKUDS, MIT）

- **是什麼**：香港大學資料科學實驗室（HKUDS）開源的 **Multi-Agent 協作框架**。五層架構（Team / Workspace / Task / Inbox / Transport），使用 git worktree 為每個 agent 提供獨立工作空間，CLI 上機；附三個範例情境（軟體開發 / 研究分析 / 文檔產出）。
- **為什麼欣賞**：把「Multi-Agent 團隊協作」從 demo 規模 push 到「**真實工作流的可審計協作**」—— 每個 agent 有獨立 worktree、有 inbox 通訊、有 transport 機制；不是純 chat-style 的 toy demo，而是接近真實組織分工的設計。學術研究背景（HKUDS）+ MIT 授權，企業可放心參考。
- **我們在哪裡用**：**L5 Multi-Agent Organization 的實作平台** —— [`../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md`](../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md) 完整課綱（5 層架構、git worktree、CLI 上機、三大在地化情境、Gate 5）；製造業 QA Team 跨部門 Agent 協作 walkthrough 在 [`../04_Scenarios/CLAWTEAM_WALKTHROUGH.md`](../04_Scenarios/CLAWTEAM_WALKTHROUGH.md)。
- **完整引用**：[`CLAWTEAM_REFERENCE.md`](CLAWTEAM_REFERENCE.md)

### 2.2 顧問框架類（影響 03_Consulting_Report）

#### 🎯 [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant)（MIT）

- **是什麼**：經典顧問分析框架的程式化整理（MECE、Pyramid Principle、Issue Tree、Porter's 5 Forces、SWOT、BCG Matrix、5 Whys、Fishbone、Business Model Canvas、WBS/RACI、NPV/IRR、Lean/Six Sigma 等 50+ 個）
- **為什麼欣賞**：把散落各家的顧問框架做成**有結構、可被引用、可被組合**的庫，不是又一份 PPT 整理
- **我們在哪裡用**：[`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) —— 改寫成 7 大類 + 框架選擇器 + 對應到八階段
- **完整引用**：[`CONSULTANT_FRAMEWORKS_REFERENCE.md`](CONSULTANT_FRAMEWORKS_REFERENCE.md)

#### 🎯 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills)（MIT）

- **是什麼**：把麥肯錫等頂級顧問的「**問題 → 報告 / 簡報**」生產手藝做成可執行的 8 步工作流
- **為什麼欣賞**：第一個把「Dummy Page → 依賴管理 → 7 個頁面版型 → progressive disclosure → troubleshooting」整套寫成可學的 SOP，不是「資深顧問才會的內隱手藝」
- **我們在哪裡用**：[`../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) —— 改寫成 8 步顧問報告生產流程 + §9 troubleshooting playbook
- **完整引用**：[`MCKINSEY_SKILLS_REFERENCE.md`](MCKINSEY_SKILLS_REFERENCE.md)

#### 🎯 **Mirza Iqbal（[next8n.com](https://next8n.com)）— Workflow Delivery Framework**（MIT）

- **是什麼**：n8n 接案顧問的**營運層** SOP —— Discovery → Sprint → Handover 的完整生命週期、價格表、客戶溝通模板
- **為什麼欣賞**：少數把「**接案的營運 SOP**」（不只是技術 SOP）開源出來的人，補完顧問業界鮮少談的營運側
- **我們在哪裡用**：[`../06_Delivery/`](../06_Delivery/) —— Engagement Lifecycle、Role SOPs、Business Document Templates 全部受其啟發
- **完整引用**：[`WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)
- **取得位置**：<https://github.com/MorrisLu-Taipei/AI-Workflow-Delivery-Framework>（README 標示原作者為 Mirza Iqbal）

### 2.3 Agent 與 Skill 類（影響 02_Course_Design）

#### 🎯 [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents)（MIT）

- **是什麼**：12 大類 agent persona 庫（行銷、業務、客服、HR、財務、研發等），即拿即用
- **為什麼欣賞**：把「Agent persona 設計」變成可重複使用的庫，省去每次從頭寫 system prompt
- **我們在哪裡用**：[`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6 「善用現成 Agent 庫」模組
- **完整引用**：[`AGENCY_AGENTS_REFERENCE.md`](AGENCY_AGENTS_REFERENCE.md)

#### 🎯 [`MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack)（混合授權）

- **是什麼**：n8n Skill 三層結構（Workflow Library + Cookbook + DSL Spec），含 AI 生成 workflow 的 Skill Pack
- **為什麼放這裡**：本方法論作者 Morris Lu 自有專案，但仍納入致敬名單以**示範引用紀律** —— 即使是自家專案，授權與第三方來源（`_vendor/` MIT）也照規矩寫
- **我們在哪裡用**：[`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) 下半段
- **完整引用**：[`N8N_SKILL_PACK_REFERENCE.md`](N8N_SKILL_PACK_REFERENCE.md)

### 2.4 案例索引類（影響 04_Scenarios）

#### 🎯 [`Shubhamsaboo/awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps)（Apache-2.0）

- **是什麼**：150+ 個真實 LLM 應用案例的精選清單（agent / RAG / fine-tuning / multimodal 等），社群維護
- **為什麼欣賞**：策展品質高、分類清楚、持續更新；是顧問跟客戶說「**這個情境別人怎麼做**」的最快參考
- **我們在哪裡用**：[`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index —— 把案例對應到 L1-L5 與企業部門的雙軸索引（**對應是我們做的**，原始案例清單版權歸 Shubham Saboo 與社群貢獻者）
- **完整引用**：[`AWESOME_LLM_APPS_REFERENCE.md`](AWESOME_LLM_APPS_REFERENCE.md)

#### 🎯 [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub)（MIT）

- **是什麼**：93+ 個 AI engineering 教學專案（從 RAG 到 multi-agent 的可執行實作）
- **為什麼欣賞**：每個專案都附**程式碼 + 教學影片**，學員可以直接動手；補足 awesome-llm-apps「精選案例」之外的「動手實作」面向
- **我們在哪裡用**：[`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index 第二來源 —— 對應到 L2-L4 課程的可實作 demo
- **完整引用**：[`AI_ENGINEERING_HUB_REFERENCE.md`](AI_ENGINEERING_HUB_REFERENCE.md)

---

## 三、原始參考資料與圖（自製或公開資料）

| 檔案 | 用途 |
| --- | --- |
| [`@AI-MD-PUBIC.pdf`](@AI-MD-PUBIC.pdf) | AI 轉型成熟度模型公開版手冊（原始 PDF 方法論底稿）|
| [`MD-Map.png`](MD-Map.png) | AI 成熟度地圖，用於根目錄 README |
| [`Metholodgy.png`](Metholodgy.png) | 企業管理顧問八階段轉型指南，用於根目錄 README |

## 四、學術依據與失敗模式（純原創，由 Tiger AI + 三 AI 引擎撰寫）

| 檔案 | 用途 |
| --- | --- |
| [`FAILURE_PATTERNS.md`](FAILURE_PATTERNS.md) | 14 個失敗模式（理論預測 + 真實案例 + 對應修正）|
| [`AI_GOVERNANCE_ALIGNMENT.md`](AI_GOVERNANCE_ALIGNMENT.md) | 對齊 NIST AI RMF / EU AI Act / ISO 42001 |
| [`PILOT_STUDY_PROTOCOL.md`](PILOT_STUDY_PROTOCOL.md) | 18-24 個月實證研究計畫（Pilot Study 設計）|

學術理論本體（7 大支柱）見 [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)。

## 五、影片學習筆記（衍生筆記，原始影片版權歸原創作者）

| 檔案 | 用途 |
| --- | --- |
| [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md) | OpenWebUI 公開 playlist 的學習紀錄與 L1 課程應用對照 |
| [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md) | TigerAI 頻道影片學習紀錄，聚焦 n8n / L3 課程應用 |

---

## 六、引用紀律（給未來貢獻者的鐵則）

要在本 repo 引用任何第三方素材，**一律遵守以下「方案 A」原則**：

| # | 原則 | 怎麼做 |
|---|---|---|
| 1 | **獨立改寫，不 fork、不重製原始碼** | 參考結構與概念後，以本方法論的語言重新撰寫 |
| 2 | **明確署名雙重備註** | (a) 引用該素材的檔案 header 加備註；(b) 本目錄建獨立 `*_REFERENCE.md` |
| 3 | **Generalize 到本方法論情境** | 把領域特定內容轉為 L1-L5 AI 轉型顧問情境 |
| 4 | **無授權者不碰** | 沒有 LICENSE 的第三方專案不整合（只能當外部範例引用網址）|
| 5 | **大方致敬** | 在引用檔案中**正面說它好在哪**，不只是「依據如下」一句帶過 |
| 6 | **失敗也誠實** | 如果某個引用的工具不適合，誠實寫在 `FAILURE_PATTERNS.md`，不只報喜 |

**使用邏輯**：要查「某個目錄的某份檔案引用了什麼」→ 看該檔 header 的「引用備註」→ 轉到本目錄對應的 `*_REFERENCE.md` 看完整授權說明。

---

## 七、與其他目錄的對應

| 目錄 | 與本目錄的關係 |
| --- | --- |
| [`../00_Overview/`](../00_Overview/) | 故事線中的方法論圖（Metholodgy.png / MD-Map.png）來自此；7 大理論支柱論述在 `00` |
| [`../02_Course_Design/`](../02_Course_Design/) | L1/L2/L3/L5 課程的第三方引用（OpenWebUI 筆記、agency-agents、n8n-Skill-Pack、ClawTeam）|
| [`../03_Consulting_Report/`](../03_Consulting_Report/) | 框架庫與報告工作流的第三方引用（consultant、mckinsey-skills）|
| [`../04_Scenarios/`](../04_Scenarios/) | LLM 應用案例索引的第三方引用（awesome-llm-apps、ai-engineering-hub）|
| [`../06_Delivery/`](../06_Delivery/) | 接案營運層的第三方引用（Mirza Iqbal 框架）|
| [`../07_AI_Contributions/`](../07_AI_Contributions/) | 三 AI 引擎本身也算「致敬對象」 —— Antigravity / Codex CLI / Claude Code |

---

## 八、常見用法情境

- **想知道某個檔案為什麼這樣寫**：看該檔 header → 對到本目錄的 `*_REFERENCE.md`
- **要再散布 / 商用本方法論**：先讀 §六引用紀律 + 根目錄 [`NOTICE`](../NOTICE) 署名要求
- **找新的開源專案想納入** → 依 §六的 6 條原則：先確認有授權 → 獨立改寫 → 建 `*_REFERENCE.md` → 補進本 README §二 致敬名單
- **想接觸上游社群、想互動 / 致敬**：每張致敬卡的 GitHub URL 直接點進去 star、follow、提 issue、做 PR
- **學員引用本 repo 內容到自己的論文 / 簡報**：依 §六原則 —— 引用本方法論時請保留原作者署名（[`../NOTICE`](../NOTICE)）；引用第三方素材請對到對應 `*_REFERENCE.md` 的學員引用建議格式

---

## 九、致謝

本目錄列出的所有上游作者與社群，**是這套方法論能站立的肩膀**。任何詮釋錯誤、引用不當、應用偏離原意之處，皆為本方法論作者 **Tiger AI Morris Lu 盧業興** 個人責任，與上游作者、社群無關。

如果您是上游作者並認為本 repo 對貴專案的引用有任何不當、需要修正、或希望加強署名 —— 歡迎開 issue 或聯絡 Morris Lu，我們會立刻處理。

> **架構歸屬**：本 repo 整體方法論架構由人類作者 **Morris Lu 盧業興（Tiger AI 虎智科技）** 提出。三個 AI 引擎（Antigravity / Codex / Claude Code）為**執行 / 完善 / 展開 / 稽核**工具。詳見 [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0。
