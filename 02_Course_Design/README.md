# 02 Course Design — L1-L5 課程設計

> 🌐 語言：繁體中文 ｜ [English](README_EN.md) ｜ [Deutsch](README_DE.md) ｜ [Français](README_FR.md) ｜ [Español](README_ES.md) ｜ [日本語](README_JA.md) ｜ [한국어](README_KR.md)

## 一、本目錄定位

本目錄是三段式服務流程的**第二段：建置（Build）**。診斷（`01`）告訴你「客戶在哪一級、缺什麼」；本目錄就是**把缺口補起來的實際課程**。

它要解決的問題是：**AI 轉型不能只靠買工具或聽演講 —— 必須讓企業沿著 L1-L5 一級一級、產出可驗收的資產。** 本目錄為 L1 到 L5 每一級都設計了完整課綱：課程目標、適合對象、課前條件、上課內容、課堂實作、課後作業、完成標準、階段驗收關卡（Stage Gate）。每一級課中都產出**可驗收的交付物**（L1 Prompt Library、L2 Skill、L3 Workflow、L4 Agent、L5 Agent Team），不是聽完就忘。

使用本目錄的人：課程講師、AI Champion、IT、各級課程的學員。

## 二、在方法論中的位置

| 軸 | 對應 |
| --- | --- |
| 三段式服務流程 | **建置（Build）** —— 第二段 |
| 八階段顧問結構 | **Stage 7 未來藍圖設計**（課程是解決方案的實際建置）|
| L1-L5 成熟度 | 本目錄就是「**把客戶從現在這級推到下一級**」的課程本體；橫跨 L1-L5 **兩條軸** |
| 接案生命週期 | **Delivery — Build** |

> 核心原則一：**L1-L5 層層銜接，上一層的產出是下一層的輸入。** 沒有 L1 全員使用習慣，L2 沒有 Skill 可累積；沒有 L2 Skill，L3 Workflow 是空管子；沒有 L3 Workflow，L4 Agent 沒工具；沒有 L4 Agent，L5 Team 沒成員。**不可跳級。**
>
> 核心原則二：**L1-L5 是兩條軸** —— 規模軸（L1 個人 → L2 部門 → L3 跨部門 / 全公司，人監督 AI）與 AI 自主軸（L4 AI 超級助理 → L5 AI 團隊，AI 營運自主、人退為治理者）。關鍵分界在 L3 → L4。詳見 [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0。術語：本系列課程的 **Stage Gate ＝ 階段驗收關卡**、**HITL ＝ Human-in-the-Loop（人類在迴圈內審核）**。

## 三、目標與效益

| 目標 | 效益 |
| --- | --- |
| 每一級都有完整、可交付的課綱 | 講師可直接開課，不用重做課程設計 |
| 課中產出可驗收資產 | 課程成果變成組織能力，不是「上完就忘」 |
| 每一級有 Stage Gate | 不通過不放下一級，避免跳級失敗 |
| 課程比例依診斷分數配置 | 客戶資源花在缺口上，不浪費 |
| L3/L4 附 PoC 場景庫 + n8n 骨架 | 實作有現成題目與模板，不從零開始 |

**若跳過本目錄**：客戶買了工具但沒有能力、PoC 永遠停在 demo、AI 無法規模化。

## 四、使用流程與邏輯

```text
01_Assessment 診斷 → L 級 + 課程比例建議
   ↓
COURSE_REQUIREMENTS_AND_COMPANY_PROFILE（確認課前條件、公司屬性、部署模式）
   ↓
COURSE_MODULE_MATRIX（看 L1-L5 課程大綱與比例配置）
   ↓
L1_L5_COMPLETE_COURSE_PLAN（總課綱）+ 各級深度課綱：
   L1 OPENWEBUI → L2 ANTIGRAVITY → L3 N8N → L4 HERMES → L5 CLAWTEAM
   ↓ 每一級
   上課 → 課堂實作（用 POC_SCENARIO_SPECS / N8N_WORKFLOW_TEMPLATES 當題目）
   → 產出可驗收資產 → 過 Stage Gate → 才進下一級
```

| 步驟 | 誰 | 何時 | 輸入 | 輸出 |
| --- | --- | --- | --- | --- |
| 確認課前條件 | 顧問 + 客戶 IT | 開課前 | 診斷結果、公司屬性 | 課前檢查表通過 |
| 配置課程比例 | 顧問 | 開課前 | L 級 + 課程比例建議 | L1-L5 時數配置 |
| 開課（逐級）| 講師 | 建置階段 | 各級深度課綱 | 學員實作成果 |
| 課堂實作 | 學員 | 每級課中 | PoC 場景 / n8n 骨架 | Prompt/Skill/Workflow/Agent/Team |
| Stage Gate 驗收 | 顧問 + 客戶主管 | 每級課後 | 課中產出物 | Gate 通過 → 進下一級 |

> 邏輯：課程不是「教工具操作」，而是「沿著成熟度建立可驗證的組織能力」。每一級的設計都遵循「上半堂產出、下半堂銜接下一級」的結構。

## 五、檔案說明

### `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md`

L1-L5 課程需求清單與公司屬性調查。定義每一級開課的課前條件、公司基本資料、資料與風險屬性、系統盤點、雲 AI / Hybrid / 全地端三種部署模式的適用條件與課程備註。開課前用它確認「客戶準備好了沒」。

### `COURSE_MODULE_MATRIX.md`

L1-L5 課程大綱矩陣。一張表看完每一級的課程目標、實作練習、課後產出物、課程包裝（半日體驗 / 一日工作坊 / 二日導入營 / 顧問診斷專案），以及依成熟度推薦的課程比例規則。

### `L1_L5_COMPLETE_COURSE_PLAN.md`

L1-L5 完整開課總規劃。每一級的課程目標、上課內容、實作、課後作業、完成標準與 Stage Gate 的總綱摘要。各級的深度課綱另見下列五個檔案。

### `L1_OPENWEBUI_COURSE_PLAN.md`

L1 Controlled AI Access 深度課綱。參考 OpenWebUI 公開 playlist，含每人登入、個人聊天區、Admin Panel、帳號/角色/群組/權限、模型控管、資料規範、影片參考地圖。

### `L2_ANTIGRAVITY_COURSE_PLAN.md`

L2 Knowledge Codification 深度課綱。參考 Google Antigravity 三套 codelab，含 Agentic IDE、App Prototype、Unit Test、GCP Serverless Pipeline、Gate 2A-2E。**§7.6** 含「善用現成 Agent 庫（agency-agents）」模組。下半堂為 L2→L3 Bridge。

### `L3_N8N_TIGERAI_COURSE_PLAN.md`

L3 Workflow Automation 深度課綱。**§1.1** 把 L3 切成上半段（n8n 概念與手動建置）與下半段（AG + TigerAI-n8n-Skill-Pack 自然語言生成，**§5.5**）。參考 TigerAI 頻道 n8n / OpenGenie 影片，含 Gemini、多模態、Sub-workflow、Data Tables、Webhook、GitHub 備份、Gate 3A-3G。

### `L4_HERMES_AGENT_COURSE_PLAN.md`

L4 Autonomous Agent 深度課綱。**§2** 為「知識型 Agent 七大設計原則」（白天輕夜間重、知識複利閉環、P1>P2、寫讀同源、工具/LLM 分工、失敗模式驅動學習、為何不只用 RAG）。含主控+專業技能組合、Wiki 記憶、ingest/query/update、Gate 4A-4E。**本課程只取概念，不含內部程式碼。**

### `L5_CLAWTEAM_COURSE_PLAN.md`

L5 Multi-Agent Organization 深度課綱。以 HKUDS/ClawTeam（MIT）為實作平台，含 Team/Workspace/Task/Inbox/Transport 五層架構、git worktree、CLI 上機、三大在地化情境、Gate 5。

### `POC_SCENARIO_SPECS.md`

L3/L4 課程的 PoC 場景庫。7 大類共 35 個可實作 PoC（Gmail / Sheets / Notion / CRM / API / ERP + 會計記帳），每個含 trigger、輸入、AI step、systems、輸出、驗收、KPI、人天、n8n 節點序列。課堂實作直接從這裡挑題目。

### `N8N_WORKFLOW_TEMPLATES.md`

把 PoC 整理成可匯入 n8n 的 workflow 骨架（JSON）。含 30 個 PoC 骨架、匯出/匯入流程、命名版本規範、GitHub Backup SOP、課堂使用流程。

### `ONLINE_COURSE_DESIGN_METHODOLOGY.md`

**跨課程通用的線上課程設計品質 SOP**（v1.0，2026-05-18）。整合學習科學三大基礎（Backward Design / Constructive Alignment / Bloom's Taxonomy）、線上課程 4 大組件（CLP / 結構 / 影音 / 互動）與 3 層品質門檻（必要 / 品質 / 加分）、學習目標寫法公式、30 點 audit checklist。所有 L1-L5 課程上架或重新編修前，**必須以此自我審查**；上架到外部平台時再依該平台規格 micro-adjust。**不替代任何既有課程**，是跨課程設計品質基準。

### `SCHOOL_L1_L3_COURSE_PLAN.md` 🆕

**K-12 學校 L1-L3 跨級整合課程規劃**（v1.0，2026-05-20）。9 個月校園 AI 導入課，把 L1（教師個人 AI）+ L2（學科 NotebookLM）+ L3（行政自動化）整合成一條學年節奏的路徑。含 §6.0 半日體驗營 50-lecture map、§6.2 完整 9 個月 Phase A/B/C 月份分解、§7 L1→L2→L3 三層銜接邏輯、§8 與上游 [mihozip MIT repo](https://github.com/mihozip/google-workspace-admin-project-workflow) 的對位、§11 4 種課程包裝（半日體驗 / 1 日工作坊 / 90 天 PoC / 9 個月完整）。對位 [`SME_LITE_PATH`](../00_Overview/SME_LITE_PATH.md) 教育界實作版。

### `TigerAI-School-Workspace-Workflow-overlay/` 🆕

**對 [`mihozip/google-workspace-admin-project-workflow`](https://github.com/mihozip/google-workspace-admin-project-workflow)（MIT）的 Tiger AI 方法論延伸**（overlay v0.1.0，2026-05-20）。內含 9 份雙語檔案：

- `README.md` + `NOTICE.md` + `INSTRUCTIONS_FOR_FORK.md` —— 法律邊界 + fork 操作指南
- `TIGERAI_METHODOLOGY_LAYER.md` —— L1-L5 對位 + 三段式服務流程 + 八階段 + SME Lite Path
- `TIGERAI_SCHOOL_L1_L3_GUIDE.md` —— 三層實作指南 + 4 個 L3 use case
- `TIGERAI_STAGE_GATES_SCHOOL.md` —— Gate 1/2/3 完整設計（家長代表必簽）
- `TIGERAI_HITL_GATES_SCHOOL.md` —— 4 大 HITL 類型 + 法律規範對位
- `SCHOOL_DAILY_SCENARIOS.md` —— **8 個日常情境逐步走查**（停課 / 戶外教學 / 請假代課 / 跨班請購 / 家長投訴 / 違規通知 / 親師會多語 / 招生 FAQ）
- `CHANGELOG.md` + `RELEASE_v0.1.0.md` —— 獨立 release 流程

**Overlay 模式：** 不修改原 repo，純加值；MIT + Apache 2.0 雙重授權邊界清楚。對位案例 [`../04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL_K12.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL_K12.md)。

### `*_EN.md`

上述檔案的英文版 sibling。

## 六、與其他目錄的對應

| 目錄 | 與本目錄的關係 | 資料流 |
| --- | --- | --- |
| `01_Assessment` | 診斷的 L 級 + 課程比例決定課程配置 | `01` 課程比例 → `02` 配置 |
| `00_Overview` | 課程是故事線的「建置」段 | `00` 故事 → `02` 落實 |
| `03_Consulting_Report` | 課中產出與觀察寫入八階段顧問報告 | `02` 課中產出 → `03` 報告 |
| `04_Scenarios` | 課堂示範題從案例索引挑；PoC 可轉化為案例 | `04` 案例 ↔ `02` 課程題目 |
| `06_Delivery` | 課程對應接案生命週期的 Delivery — Build；交付物進交付包驗收 | `02` 產出 → `06` 驗收 |
| `90_References` | 各級課程的第三方引用（OpenWebUI / Antigravity / n8n-Skill-Pack / ClawTeam / agency-agents）| `90` 引用 → `02` |

## 七、常見用法情境

- **配課程**：拿診斷的課程比例 → 用 `COURSE_MODULE_MATRIX.md` 配時數 → 開對應深度課綱。
- **開 L3 課**：用 `L3_N8N_TIGERAI_COURSE_PLAN.md` 上半段教概念，下半段教 AG+Skill Pack；實作題從 `POC_SCENARIO_SPECS.md` 挑、骨架從 `N8N_WORKFLOW_TEMPLATES.md` 匯入。
- **學員找實作題**：依自己部門與 L 級，從 `POC_SCENARIO_SPECS.md` 或 `04_Scenarios/LLM_APPS_CASE_INDEX.md` 挑。
- **驗收**：每級課後對照 `01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md` 過 Stage Gate。

---

## ⭐ 跨主題對照：5 個核心主題去哪查

整本方法論有 5 條主動脈，貫穿所有目錄。本目錄與它們的關聯如下：

| 跨主題 | 主檔案位置 | 本目錄如何接 |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 三引擎共讀** | 根 [`README.md`](../README.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | **L2 Knowledge Codification 課程直接教三引擎使用** —— Antigravity / Codex / Claude Code 都是 L2 學員的工具；課中可調動三引擎跑 demo + Skill 封裝 + 跨檔測試 |
| 🎓 **成熟理論（7 大支柱）** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **L1-L5 五層架構依 Capability Maturity（Rosemann/CMMI）**；不可跳級的鐵則依 Absorptive Capacity（Cohen & Levinthal 1990）；L4 Hermes 七大設計原則對應 Sociotechnical & Knowledge Compounding |
| 📚 **L1-L5 課程教育** | [`../02_Course_Design/`](本目錄) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](L1_L5_COMPLETE_COURSE_PLAN.md) | **本目錄就是 L1-L5 課程本體** —— 5 個獨立深度課綱（L1 OPENWEBUI / L2 ANTIGRAVITY / L3 N8N / L4 HERMES / L5 CLAWTEAM）+ COURSE_MODULE_MATRIX 比例配置 + POC_SCENARIO_SPECS 35 個實作題 |
| 🔁 **顧問方案 / 8 階段 + Phase A→B→C 閉環** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **課程產出物進 Phase B 報告**（成為 14 章的「課程觀察」章節）+ Phase C 季度雷達追蹤；每級 Stage Gate 對應顧問閉環的 Gate A/B/C |
| 📖 **參考資料 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | **L1 → OpenWebUI** ｜ **L2 → Antigravity / Codex / Claude Code + agency-agents** ｜ **L3 → n8n + TigerAI-n8n-Skill-Pack** ｜ **L4 → nousresearch/hermes-agent** ｜ **L5 → HKUDS/ClawTeam**。完整致敬卡見 [`../90_References/README.md`](../90_References/README.md) §2.1-2.3 |
