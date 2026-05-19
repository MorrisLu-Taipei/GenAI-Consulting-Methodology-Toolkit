# Release Notes — Tiger AI School Workspace Workflow Overlay v0.1.0

> 🌐 中英雙語 / Bilingual inline
> **Release date:** 2026-05-20
> **Version:** v0.1.0 (Initial release)
> **License:** Apache 2.0 (Tiger AI additions) + MIT (upstream original)
> **Author:** Tiger AI Morris Lu 盧業興

---

## 🎯 Why this release / 為什麼有這個版本

Tiger AI Methodology Toolkit 缺一個**教育界 L1-L3 的具體案例 + 實作對位**。同時 [mihozip/google-workspace-admin-project-workflow](https://github.com/mihozip/google-workspace-admin-project-workflow)（MIT）已經提供了**可用的代碼與教材**（Apps Script + Workspace + NotebookLM + Gemini），但**沒有方法論層**告訴學校：誰來推、怎麼排序、怎麼驗收。

The Tiger AI Methodology Toolkit lacked a **concrete L1-L3 case for the education sector**. Meanwhile, [mihozip/google-workspace-admin-project-workflow](https://github.com/mihozip/google-workspace-admin-project-workflow) (MIT) provides **usable code and materials** (Apps Script + Workspace + NotebookLM + Gemini), but has **no methodology layer** answering: who drives it, in what order, how to verify.

**這個 overlay 把這個 gap 補上 —— 不修改原 repo、不掠奪別人成果、不混淆授權。**
**This overlay fills that gap — without modifying the original repo, without appropriating someone else's work, without license confusion.**

---

## ✨ What's in this release / 本版內容

### 8 個 overlay 檔案 / 8 overlay files

| 檔案 / File | 行數 / Lines | 用途 / Purpose |
|---|---|---|
| `README.md` | ~ 100 | 總覽 + attribution |
| `NOTICE.md` | ~ 150 | 雙重授權聲明 + 引用 + 免責 |
| `INSTRUCTIONS_FOR_FORK.md` | ~ 150 | 3 條使用路徑 |
| `TIGERAI_METHODOLOGY_LAYER.md` | ~ 200 | L1-L5 對位 |
| `TIGERAI_SCHOOL_L1_L3_GUIDE.md` | ~ 250 | 3 層實作指南 + 4 個 L3 use case |
| `TIGERAI_STAGE_GATES_SCHOOL.md` | ~ 200 | Gate 1 / 2 / 3 設計 |
| `TIGERAI_HITL_GATES_SCHOOL.md` | ~ 230 | 4 大 HITL 類型 + 程式碼建議 |
| `CHANGELOG.md` | ~ 60 | 獨立版本紀錄 |
| `RELEASE_v0.1.0.md`（本檔 / this file）| ~ 130 | 本版 release notes |

**總計：~ 1,470 行雙語內容。**
**Total: ~1,470 lines of bilingual content.**

---

## 🧭 Key concepts introduced / 引入的關鍵概念

### 1. Tiger AI L1-L5 對位學校場景 / Tiger AI L1-L5 mapping to school

| L | 對位 |
|---|---|
| L1 | 全員教師個人使用 AI（Prompt / Email / 教案）|
| L2 | 種子科教師整理 NotebookLM 教材庫 |
| L3 | **本 repo 核心**：行政流程自動化（公文 / 活動 / 請購 / 家長通知）|
| L4-L5 | **不推給學校**（少數大型完全中學例外）|

### 2. SME Lite Path 對位學校規模 / SME Lite Path × school scale

| 學校規模 | 路線 | 收費 |
|---|---|---|
| < 20 補習班 | SOHO Path | 5-20 萬 |
| 50-300 K-12 | SME Lite Path | 30-150 萬 |
| 500+ 大型 | Enterprise-lite | 120-300 萬 |

### 3. 三層 Stage Gate / Three-tier Stage Gates

- **Gate 1** L1 完成 —— ≥ 95% 教師 AI-enabled + Prompt Library 建立 + 規範通過
- **Gate 2** L2 完成 —— ≥ 5 個學科 NotebookLM + 種子教師持續分享
- **Gate 3** L3 完成 —— ≥ 2 個 use case 上線 + HITL 觸發過 + 行政組長能獨立維運

### 4. 四大 HITL Gate 類型 / Four HITL categories

- **公文簽核** —— 每站親點同意，金額 > 5K 校長簽
- **學生資料** —— 評語必須教師親審，敏感詞觸發 alert
- **對外公告** —— 校長 / 主任親按發布，多語版各語審
- **家長通知** —— 導師逐封親審，敏感事件不可純線上

---

## ⚖️ License compatibility / 授權相容性

**MIT (upstream) + Apache 2.0 (overlay) 在 overlay 模式下相容。** 兩者檔案位於不同資料夾，未交叉合併。

**MIT (upstream) + Apache 2.0 (overlay) are compatible in overlay pattern.** Files reside in separate folders, no cross-merging.

下游使用者若同時使用兩者：
- 原 repo 檔案維持 MIT，須保留原作者聲明
- 本 overlay 檔案維持 Apache 2.0，須保留 NOTICE

Downstream users using both:
- Original repo files remain MIT, preserve original author notice
- Overlay files remain Apache 2.0, preserve NOTICE

---

## 🚀 How to use / 怎麼用

依 `INSTRUCTIONS_FOR_FORK.md` 選 3 條路徑：

Per `INSTRUCTIONS_FOR_FORK.md`, three paths:

| Path | Use case | 行動 |
|---|---|---|
| **A. Production fork + overlay** | 顧問 / 學校要對外發布 | Fork 原 repo + 套 overlay + 重新 release |
| **B. Local trial** | 學校內部試行不公開 | Clone 原 repo + 本地套 overlay |
| **C. Read-only** | 方法論研究 | 只讀 overlay 不動 git |

---

## 🛣️ What's coming next / 下一版預告

### v0.2.0（無 ETA，視客戶需求）

- 補完「活動申請」與「物資請購」HITL 完整範本
- 加 Apps Script HITL wrapper 的可貼上程式碼 fragment
- 補 4 個 L3 use case 的 ROI 計算範例

### v0.3.0

- 加 3 個學校 worked example（匿名化）：
  - 小型私立小學（50 人）
  - 公立國中（200 人）
  - 大型完全中學（800 人）
- 每個含完整 90 天 roadmap + 收費對應 + 實際 KPI

### v0.4.0

- 對位台灣《AI 產業人才認定指引》（115 年 5 月版）
- 教師職能對應到「AI 應用人才」三大類別

### v1.0.0

- 至少 1 個學校實際導入完成
- Lessons learned 沉澱寫入 overlay
- 對應主 toolkit Zenodo DOI 提升到對應版本

---

## 📚 Related deliverables in main toolkit / 主 toolkit 相關 deliverable

本 overlay 跟主 toolkit 的這些檔案搭配閱讀：

Read alongside these main toolkit files:

| 主 toolkit 檔案 / Main toolkit file | 跟 overlay 的關係 |
|---|---|
| `00_Overview/SME_LITE_PATH.md` | 學校屬於 SME，看壓縮路徑 |
| `01_Assessment/AI_MATURITY_QUESTIONNAIRE.md` | 用 25 題版做學校 L 級評估 |
| `02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md` | L1 教師 AI 使用課的詳細課綱 |
| `02_Course_Design/_deliverables/L1_PROMPT_LIBRARY_STARTER.md` | 5 個範例 Prompt（可給教師作起點） |
| `02_Course_Design/_deliverables/L1_DATA_BOUNDARY_QUIZ.md` | 10 案例題（給教師 quiz）|
| `02_Course_Design/_deliverables/L1_AI_USAGE_POLICY_TEMPLATE.md` | 學校 AI 使用規範範本 |
| `04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL.md` | 跟本 overlay 一起 release 的學校案例（位於 04_Scenarios） |

---

## 🙏 Acknowledgments / 致謝

- **mihozip** —— 提供原 repo 與 MIT 授權，讓我們可以站在他的工作之上做方法論延伸
- **Tiger AI Morris Lu 盧業興** —— 本 overlay 作者
- **(待補)** —— 第一個試行學校客戶（如有意願加入，請來信）

---

## 📞 Feedback / 意見回饋

請至 Tiger AI Methodology Toolkit 主 repo 開 Issue：
Please open issues at the Tiger AI Methodology Toolkit main repo:

<https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit/issues>

請**不要**在 mihozip 原 repo 開 overlay 相關 issue（會增加他的維運負擔，且超出他的 repo 範圍）。

Please **do not** open overlay-related issues on mihozip's original repo (would burden his maintenance and is outside his repo's scope).

---

**End of Release v0.1.0**
