# 02 Course Design — L1-L5 課程設計

## 一、本目錄定位

本目錄是三段式服務流程的**第二段：建置（Build）**。診斷（`01`）告訴你「客戶在哪一級、缺什麼」；本目錄就是**把缺口補起來的實際課程**。

它要解決的問題是：**AI 轉型不能只靠買工具或聽演講 —— 必須讓企業沿著 L1-L5 一級一級、產出可驗收的資產。** 本目錄為 L1 到 L5 每一級都設計了完整課綱：課程目標、適合對象、課前條件、上課內容、課堂實作、課後作業、完成標準、階段驗收關卡（Stage Gate）。每一級課中都產出**可驗收的交付物**（L1 Prompt Library、L2 Skill、L3 Workflow、L4 Agent、L5 Agent Team），不是聽完就忘。

使用本目錄的人：課程講師、AI Champion、IT、各級課程的學員。

## 二、在方法論中的位置

| 軸 | 對應 |
| --- | --- |
| 三段式服務流程 | **建置（Build）** —— 第二段 |
| 八階段顧問結構 | **Stage 7 解決方案架構**（課程是解決方案的實際建置）|
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

L1 Chat AI 深度課綱。參考 OpenWebUI 公開 playlist，含每人登入、個人聊天區、Admin Panel、帳號/角色/群組/權限、模型控管、資料規範、影片參考地圖。

### `L2_ANTIGRAVITY_COURSE_PLAN.md`

L2 Skill AI 深度課綱。參考 Google Antigravity 三套 codelab，含 Agentic IDE、App Prototype、Unit Test、GCP Serverless Pipeline、Gate 2A-2E。**§7.6** 含「善用現成 Agent 庫（agency-agents）」模組。下半堂為 L2→L3 Bridge。

### `L3_N8N_TIGERAI_COURSE_PLAN.md`

L3 Workflow AI 深度課綱。**§1.1** 把 L3 切成上半段（n8n 概念與手動建置）與下半段（AG + TigerAI-n8n-Skill-Pack 自然語言生成，**§5.5**）。參考 TigerAI 頻道 n8n / OpenGenie 影片，含 Gemini、多模態、Sub-workflow、Data Tables、Webhook、GitHub 備份、Gate 3A-3G。

### `L4_HERMES_AGENT_COURSE_PLAN.md`

L4 Auto Agentic AI 深度課綱。**§2** 為「知識型 Agent 七大設計原則」（白天輕夜間重、知識複利閉環、P1>P2、寫讀同源、工具/LLM 分工、失敗模式驅動學習、為何不只用 RAG）。含主控+專業技能組合、Wiki 記憶、ingest/query/update、Gate 4A-4E。**本課程只取概念，不含內部程式碼。**

### `L5_CLAWTEAM_COURSE_PLAN.md`

L5 Agentic Team AI 深度課綱。以 HKUDS/ClawTeam（MIT）為實作平台，含 Team/Workspace/Task/Inbox/Transport 五層架構、git worktree、CLI 上機、三大在地化情境、Gate 5。

### `POC_SCENARIO_SPECS.md`

L3/L4 課程的 PoC 場景庫。7 大類共 35 個可實作 PoC（Gmail / Sheets / Notion / CRM / API / ERP + 會計記帳），每個含 trigger、輸入、AI step、systems、輸出、驗收、KPI、人天、n8n 節點序列。課堂實作直接從這裡挑題目。

### `N8N_WORKFLOW_TEMPLATES.md`

把 PoC 整理成可匯入 n8n 的 workflow 骨架（JSON）。含 30 個 PoC 骨架、匯出/匯入流程、命名版本規範、GitHub Backup SOP、課堂使用流程。

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
