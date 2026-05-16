# 01 Assessment — AI 成熟度診斷

## 一、本目錄定位

本目錄是三段式服務流程的**第一段：診斷（Diagnose）**。它要解決一個顧問接案最根本的問題：**「企業說自己『有在用 AI』，但到底在哪一級？缺什麼？該從哪裡補？」**

如果沒有客觀診斷，顧問只能憑客戶的主觀描述配課程 —— 結果往往是跳級（客戶連 L1 全員使用都沒有就想做 L4 Agent）、或配錯重點（明明缺治理卻一直加工具）。本目錄用三種長度的問卷 + 評分模型 + 公司屬性調查，把「模糊的感覺」變成**客觀、可量化、可比較的 L1-L5 分數與六大構面缺口圖**。

使用本目錄的人：業務（用 10 題版做開發期篩選）、顧問（用 25/50 題版做課前與訪談前盤點）、IT/AI Champion（填公司屬性問卷）。

## 二、在方法論中的位置

| 軸 | 對應 |
| --- | --- |
| 三段式服務流程 | **診斷（Diagnose）** —— 第一段 |
| 八階段顧問結構 | **Stage 1 現況掌握**（診斷結果是 Stage 1 的核心輸入）|
| L1-L5 成熟度 | 本目錄就是「**判定客戶落在哪一級**」的工具 |
| 接案生命週期 | **Sales — Lead Qualification（10 題版）/ Discovery（25/50 題版）** |

## 三、目標與效益

| 目標 | 效益 |
| --- | --- |
| 用客觀分數取代主觀臆測 | 顧問配課程有依據，不憑感覺 |
| 找出六大構面缺口（工具/知識/流程/整合/Agent/治理 ROI）| 知道客戶「強在哪、弱在哪」 |
| 直接推導三項建議 | 課程比例 + 部署模式 + PoC 場景，一次到位 |
| 三種問卷長度對應三個銷售階段 | 業務開發、課前、訪談前各有適用工具 |
| 可自動化 | 問卷→計分→報告全程自動，顧問只做解讀 |

**若跳過本目錄**：課程比例靠猜、客戶期待無法管理（指著 L5 案例說「我要這個」卻不知自己在 L2）、顧問報告沒有客觀起點。

## 四、使用流程與邏輯

```text
10 題快速問卷（業務開發期，3 分鐘）
   → 判定 Lead 合格 + 初步 L 級落點
25 題問卷（課前，8 分鐘，由客戶主管填）
   → 六大構面分數 + 雷達圖
50 題問卷（顧問訪談前，20 分鐘，由 IT/AI Champion 填）
   → 完整盤點 + 開放問答
公司屬性問卷（35 題）
   → JSON Profile Bundle（系統 / 風險 / 部署偏好 / 預算）
        ↓ 合併
   自動計分 → L1-L5 等級 + 六構面雷達
        ↓ 推導
   ① 建議課程比例  ② 建議部署模式  ③ 建議 PoC 場景
```

| 步驟 | 誰 | 何時 | 輸入 | 輸出 |
| --- | --- | --- | --- | --- |
| 10 題快篩 | 業務 | Lead 開發期 | 潛在客戶 | 合格判定 + 初步 L 級 |
| 25 題課前診斷 | 客戶主管群 | L1 開課前 1 週 | 25 題問卷 | 六構面分數 |
| 50 題完整盤點 | 客戶 IT / AI Champion | 顧問訪談前 | 50 題 + 公司屬性問卷 | 完整 Profile Bundle |
| 自動計分 | 系統（Sheets/Notion/n8n）| 問卷提交後 | 問卷答案 | L 級 + 雷達 + 三項建議 |
| 解讀 | 顧問 | 收到自動報告後 | 自動報告 | 客製化提案方向 |

> 邏輯：問卷只是**輸入**；真正的產出是「**L 級 + 六構面缺口 + 三項建議**」。這三項分別餵給 —— 課程比例 → `02_Course_Design`；部署模式 → `03` 的 To-Be Design；PoC 場景 → `04_Scenarios` 的案例索引。診斷不是終點，是把後面三個目錄「點亮」的開關。

## 五、檔案說明

### `AI_MATURITY_QUESTIONNAIRE.md`

10 / 25 / 50 題三種長度的 AI 成熟度問卷本體。10 題版供業務快速判定；25 題版每個構面 4-5 題、供課前；50 題版加上部署模式與系統盤點、供顧問訪談前。三版共用 0-4 分量尺與六大構面架構。

### `AI_MATURITY_SCORING_MODEL.md`

評分邏輯與判定規則。包含：六大構面（工具使用、知識沉澱、流程標準化、系統整合、Agent 應用、治理 ROI）的計分方式、總分對應 L1-L5 的門檻、**主成熟度 vs 局部成熟度**的判斷（為何某部門可局部 L4 但整體 L2）、部署模式與課程比例的推薦規則。

### `AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`

L1-L5 每一階段的 Definition of Done、Deliverables、Evidence、Owner、Stage Gate、Fail Condition、Next Level Entry Criteria。它定義「每一級『做完』長什麼樣、要拿什麼 evidence 證明」，是 Stage Gate 驗收的依據。

### `FILLABLE_QUESTIONNAIRE.md`

把 10/25/50 題轉成可填寫表單的渲染規格 —— 題型（radio / 0-4 scale / 多選 / 短答）、頁面分段、skip logic、提交頁與「接下來會發生什麼」頁，並附 Google Form / Tally / Notion Form 三平台的 render 提示。

### `COMPANY_PROFILE_QUESTIONNAIRE.md`

35 題公司屬性問卷，分 6 區（Profile / Systems / Risk / Deployment / Course / Budget）。輸出一份 JSON Profile Bundle，並含**推導規則**：由 Bundle 自動推出部署模式建議、課程比例微調、PoC 場景建議。與成熟度問卷以 `submission_id` 對應。

### `AI_DIAGNOSIS_SHEETS_SCHEMA.md`

把整套診斷自動化的實作 schema。三個平台：Google Sheets（計分公式、條件格式、Apps Script）、Notion（4 個 database 結構與 formula）、n8n（13-node 自動診斷流程，含 idempotency）。讓問卷→計分→產生報告→通知顧問全程自動。

### `*_EN.md`

上述檔案的英文版 sibling。

## 六、與其他目錄的對應

| 目錄 | 與本目錄的關係 | 資料流 |
| --- | --- | --- |
| `00_Overview` | 診斷是故事線的第一段 | `00` 故事 → `01` 落實 |
| `02_Course_Design` | 診斷的「L 級 + 課程比例」直接決定課程配置 | `01` 課程比例 → `02` 課程配置 |
| `03_Consulting_Report` | 診斷結果是八階段 Stage 1 的輸入；報告引用診斷分數與雷達 | `01` 分數 → `03` 報告 |
| `04_Scenarios` | 診斷後依 L 級用 `LLM_APPS_CASE_INDEX.md` 挑 PoC 候選 | `01` L 級 → `04` 案例篩選 |
| `06_Delivery` | 診斷對應接案生命週期的 Sales 階段 | `01` ↔ `06` Sales 階段 |
| `90_References` | 評分模型的方法論依據 | `90` 依據 → `01` |

## 七、常見用法情境

- **業務開發**：潛在客戶填 10 題版 → 24 小時內自動報告 → 業務帶著 L 級落點去談。
- **課前準備**：開課前 1 週發 25 題版給客戶主管群 → 顧問拿到六構面雷達，調整課程比例。
- **顧問訪談前**：IT/AI Champion 填 50 題 + 公司屬性問卷 → 顧問訪談前 1 小時收到完整 Profile Bundle 當 brief。
- **要規模化**：用 `AI_DIAGNOSIS_SHEETS_SCHEMA.md` 在客戶 n8n 部署自動診斷流程，顧問只做最後解讀。

---

## ⭐ 跨主題對照：5 個核心主題去哪查

整本方法論有 5 條主動脈，貫穿所有目錄。本目錄與它們的關聯如下：

| 跨主題 | 主檔案位置 | 本目錄如何接 |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 三引擎共讀** | 根 [`README.md`](../README.md) §🌟 ｜ [`../AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | 問卷可由 Antigravity 跑 `/diagnose` 互動填寫；AI_DIAGNOSIS_SHEETS_SCHEMA 把問卷自動化（n8n + Google Sheets + Notion）；診斷結果可進 Codex 跑 `/consistency-review` 跨檔對齊 |
| 🎓 **成熟理論（7 大支柱）** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **本目錄的 [`BARS_RUBRICS.md`](BARS_RUBRICS.md) 對應 inter-rater reliability**（Smith & Kendall 1963）；診斷六構面對應 Capability Maturity（Rosemann/CMMI）+ Absorptive Capacity（Cohen & Levinthal 1990）+ Sociotechnical Trust |
| 📚 **L1-L5 課程教育** | [`../02_Course_Design/`](../02_Course_Design/) | **診斷的 L 級判定 + 六構面雷達 + 課程比例建議**直接決定 02 的課程配置 —— 是 02 的「課前必填」 |
| 🔁 **顧問方案 / 8 階段 + Phase A→B→C 閉環** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **診斷 = Phase A 的核心輸入**（Stage 1 現況掌握 + Stage 2 Reference Model 雷達簽署）；Phase C 季度雷達回看就是「**重新跑診斷**」—— 結構真的變圓了嗎？診斷既是入口、也是閉環的反證機制 |
| 📖 **參考資料 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | 評分模型參考 BARS（Smith & Kendall 1963）+ 7 大理論支柱；Pilot Study 18-24 月實證計畫見 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md)（驗證問卷的 Cohen's κ ≥ 0.60 目標）|
