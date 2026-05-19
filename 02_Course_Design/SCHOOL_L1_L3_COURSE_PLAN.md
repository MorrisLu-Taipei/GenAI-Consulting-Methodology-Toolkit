# K-12 學校 L1-L3 AI 導入課程規劃 / K-12 School L1-L3 AI Adoption Course Plan

> 🌐 中英雙語 / Bilingual inline
>
> 版本 / Version：v1.0（2026-05-20）
> 作者 / Author：Morris Lu (盧業興)
> 適用層級 / Applicable level：L1 → L3（cross-level for K-12 schools）
> 對位案例 / Reference case：[`04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL_K12.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL_K12.md)
> 對位 overlay：[`TigerAI-School-Workspace-Workflow-overlay/`](TigerAI-School-Workspace-Workflow-overlay/)
> 對位上游：[mihozip/google-workspace-admin-project-workflow](https://github.com/mihozip/google-workspace-admin-project-workflow)（MIT）
> 對位方法論：[`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](ONLINE_COURSE_DESIGN_METHODOLOGY.md)

## 1. 課程定位 / Positioning

本課程是 Tiger AI Methodology 在 **K-12 學校場景**的跨級（L1-L3）導入規劃。它**不是** L1_OPENWEBUI / L2_ANTIGRAVITY / L3_N8N 三個分離課程的學校版替代品，而是**把它們整合成適合學校節奏的 9 個月導入課**。

This course is Tiger AI Methodology's cross-level (L1-L3) adoption plan for **K-12 schools**. It is **not** a school-version replacement for the separate L1_OPENWEBUI / L2_ANTIGRAVITY / L3_N8N courses, but rather **integrates them into a 9-month school-paced adoption course**.

### 為什麼 K-12 需要跨級整合課 / Why K-12 needs cross-level integration

| 因素 | 說明 |
|---|---|
| **學年節奏** | 學校以「學期」為單位，3 個課程拆開教需要 1.5-2 學年；整合課 9 個月 = 1 學期 + 1 暑假 |
| **教師時間有限** | 教師上課 + 改作業 + 行政 + 輔導，無法同時上 3 個分離課程 |
| **行政與教師需共同進度** | L1 全員 → L2 種子 → L3 行政是有先後依賴的，不可平行 |
| **校長需要單一窗口** | 一個總體課程 + 一個總體預算，校長才好決策 |

---

## 2. 校園必備能力 / Required Capabilities (Stage Gates)

每個 L 階段結束有 1 個 Stage Gate（詳見 [overlay/TIGERAI_STAGE_GATES_SCHOOL.md](TigerAI-School-Workspace-Workflow-overlay/TIGERAI_STAGE_GATES_SCHOOL.md)）。

| 能力 / Capability | L 級 | 完成標準 |
|---|---|---|
| 教師個人 AI 使用 | L1 | ≥ 95% 教師有帳號 + Prompt Library v1 |
| 學科 NotebookLM 教材庫 | L2 | ≥ 5 學科有 NotebookLM + 種子教師持續分享 |
| 行政流程自動化 | L3 | ≥ 2 個 use case 上線 + HITL Gate 觸發過 + 行政組長獨立維運 |
| 治理規範 + 規範簽署 | L1-L3 全程 | AI 使用規範通過校務會議 + 全員簽署 |

---

## 3. 課程目標 / Learning Objectives

> 本節以 [`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](ONLINE_COURSE_DESIGN_METHODOLOGY.md) §4 的 Bloom 公式撰寫。

### 3.1 給 CLP 用的 4 條主 LO / 4 primary LOs for the CLP

完成 K-12 L1-L3 課程後，學員能夠：

By the end of the K-12 L1-L3 course, learners can:

1. **應用** AI 工具完成日常教學工作（教案 / Email / 翻譯 / 評語），**產出** 個人 Prompt Library ≥ 5 個。（Apply）
   **Apply** AI tools to daily teaching tasks (lesson plans / Email / translation / comments), **producing** a personal Prompt Library of ≥ 5 prompts. (Apply)

2. **建構** 學科 NotebookLM 教材庫（≥ 10 份文件 + ≥ 5 個學科 Prompt），**示範** 跨班 / 跨年級分享。（Create）
   **Build** a subject NotebookLM library (≥ 10 documents + ≥ 5 subject-specific prompts), **demonstrating** cross-class / cross-grade sharing. (Create)

3. **設計** 校園行政流程的 AI 自動化（公文 / 活動 / 請購 / 家長通知），**部署** ≥ 2 個 use case 並含完整 HITL Gate。（Create + Apply）
   **Design** AI automation for school admin workflows (doc routing / events / procurement / parent notifications), **deploying** ≥ 2 use cases with full HITL Gates. (Create + Apply)

4. **評估** 校園 AI 導入的 ROI 與 Stage Gate 達成度，**產出** 對校長 + 家長代表的成果報告 + 下階段建議。（Evaluate）
   **Evaluate** the ROI and Stage Gate achievement of school AI adoption, **producing** a results report for principal + parent representative + next-phase recommendations. (Evaluate)

### 3.2 細部能力清單 / Detailed capability list

| 主 LO / Primary LO | 對應細部能力 / Supporting capabilities |
| --- | --- |
| LO1（個人 AI）| 登入 / 模型選擇 / 5 要素 Prompt / 資料邊界判斷 / 個人 Prompt Library |
| LO2（學科 NotebookLM）| NotebookLM 建置 / 教材上傳 / 學科 Prompt 設計 / 跨班分享機制 |
| LO3（行政自動化）| Apps Script 基礎 / Workspace 整合 / HITL Gate 設計 / 4 個 use case 實作 |
| LO4（評估與報告）| KPI 設計 / Stage Gate 自評 / 對校長簡報 / 家長代表溝通 |

### 3.3 互動學習設計 / Interactive Learning Design

**Engagement activity（開頭 10 分鐘必須有）：**

> **校長 + 主任先 hands-on**。讓全校教師看到「校長都做了，我也可以」。Top-down 示範比任何訓練投影片有用。
> **Principal + deans go hands-on first**. Let teachers see "if the principal can, so can I." Top-down demo beats any training slides.

**Formative gates（章節結尾的快速自我檢核）：**

| 章節 | Formative 檢核 | 時長 |
|---|---|---|
| L1 訓練結尾 | 學員當場用 Prompt 完成 1 個今天工作 | 10 分鐘 |
| L2 訓練結尾 | 學員打開 NotebookLM 問 1 個自己課程問題 | 10 分鐘 |
| L3 訓練結尾 | 學員看 Apps Script 流程圖，找出 HITL Gate | 10 分鐘 |
| 治理章節結尾 | 10 案例資料邊界 Quiz（90% 通過才算合格） | 15 分鐘 |

**Summative gate（全課程結尾）：對應 Gate 1 + Gate 2 + Gate 3（見 §9）+ 1 份校長對家長代表的成果報告。**

### 3.4 Reference materials 清單 / Reference materials

| 類型 | 檔名 / 位置 | 狀態 |
|---|---|---|
| L1-L3 校園實作指南 | [overlay/TIGERAI_SCHOOL_L1_L3_GUIDE.md](TigerAI-School-Workspace-Workflow-overlay/TIGERAI_SCHOOL_L1_L3_GUIDE.md) | ☑ 已加 |
| Stage Gate 完整設計 | [overlay/TIGERAI_STAGE_GATES_SCHOOL.md](TigerAI-School-Workspace-Workflow-overlay/TIGERAI_STAGE_GATES_SCHOOL.md) | ☑ 已加 |
| HITL Gate 完整設計 | [overlay/TIGERAI_HITL_GATES_SCHOOL.md](TigerAI-School-Workspace-Workflow-overlay/TIGERAI_HITL_GATES_SCHOOL.md) | ☑ 已加 |
| AI 使用規範範本 | [_deliverables/L1_AI_USAGE_POLICY_TEMPLATE.md](_deliverables/L1_AI_USAGE_POLICY_TEMPLATE.md) | ☑ 已加（通用版）|
| 教師 Prompt Library 啟動包 | [_deliverables/L1_PROMPT_LIBRARY_STARTER.md](_deliverables/L1_PROMPT_LIBRARY_STARTER.md) | ☑ 已加（通用版）|
| 資料邊界判斷 Quiz | [_deliverables/L1_DATA_BOUNDARY_QUIZ.md](_deliverables/L1_DATA_BOUNDARY_QUIZ.md) | ☑ 已加（通用版）|
| Admin Runbook | [_deliverables/L1_ADMIN_RUNBOOK.md](_deliverables/L1_ADMIN_RUNBOOK.md) | ☑ 已加（通用版，校內 IT 用） |
| 校園版 Prompt Library | 待補（針對教師工作場景的 ≥ 10 個 Prompt） | ☐ 待補 |
| 校園版資料邊界案例 | 待補（針對學生資料、家長通訊的 10 案例 Quiz） | ☐ 待補 |
| L3 Apps Script 實作 | [mihozip 原 repo](https://github.com/mihozip/google-workspace-admin-project-workflow)（MIT） | ☑ 上游已有 |
| 上游 basic-lesson + advanced-lesson 教材 | mihozip 原 repo `basic-lesson/` + `advanced-lesson/` | ☑ 上游已有 |

---

## 4. 課前條件 / Prerequisites

| 項目 | 最低要求 |
|---|---|
| **校長 / 主任承諾** | 校長書面承諾每月撥 ≥ 2 小時親自參與 |
| **IT 中心** | 至少 1 人有基本 Google Workspace 管理權限 |
| **Workspace** | 已使用 Google Workspace for Education ≥ 6 個月 |
| **預算** | NT$ 50-150 萬（依規模） |
| **家長代表** | PTA 已存在或可組成 |
| **教師意願** | 教師代表大會通過「願意試行 AI 導入」 |
| **法務 / 個資審查** | 校內或委外法律顧問可在上線前審 AI 使用規範 |
| **網路 / 設備** | 全校教師有可用設備（個人或公用）+ 校內 Wi-Fi 穩定 |

---

## 5. K-12 學校 L1-L3 IPOE

| 類別 | 定義 |
|---|---|
| **Input** | 教師工作經驗、學校公文格式、家長通訊範本、學科教材、學生作業（去識別化）、行政流程 SOP、AI 使用規範、Google Workspace 帳號、Apps Script 程式碼（取自上游 repo） |
| **Process** | 全員 L1 訓練 → 種子科 L2 訓練 → 行政 L3 訓練 → Stage Gate 驗收（×3） → HITL Gate 設計 + 上線 + 維運 |
| **Output** | 個人 Prompt Library v1 / 學科 NotebookLM × N / 行政 use case × 2-4 / AI 使用規範 / Gate 1-3 驗收紀錄 / 對校長對家長代表的成果報告 |
| **Evidence** | 帳號清單、Prompt Library 截圖、NotebookLM 連結、執行 Log、Apps Script commit 紀錄、HITL approval 紀錄、KPI 對比表、Stage Gate 簽署表 |

---

## 6. 課程版本 / Course Versions

### 6.0 Lecture Map（Foundation 版本完整切細）

對應 [`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](ONLINE_COURSE_DESIGN_METHODOLOGY.md) §5.3 的講座切細原則。

> 講座類型代碼：**TH** Talking Head / **S** Screencast / **SL** Slides / **PR** Practice / **EN** Engagement / **RC** Recap

#### §6.1 校園 AI 半日體驗營（4 小時 = ~50 lectures × 平均 4.8 min）

| Section | 時長 | Lectures | Focus |
|---|---|---|---|
| Intro | 30 min | 5 lectures (含 Engagement) | 為什麼學校需要 AI；4 條主 LO 預告；校長 5 分鐘 demo |
| L1 速覽 | 60 min | 12 lectures | 個人 AI 使用 + Prompt 5 要素 + 5 個範例 |
| 資料邊界 | 30 min | 8 lectures | 學生資料 / 家長通訊紅線 + 10 案例 Quiz |
| L2 / L3 預告 | 60 min | 12 lectures | 學科 NotebookLM 展示 + 行政自動化 demo（用 mihozip repo）|
| 治理討論 | 30 min | 8 lectures | AI 使用規範 + Stage Gate + HITL Gate 概念 |
| Conclusion | 30 min | 5 lectures | 收尾 + 下一步路徑（要不要走完整 9 個月）|

#### §6.2 校園 AI 完整 9 個月導入課（外部顧問帶 + 校內團隊）

| Phase | 期間 | 主要活動 | 對應 Gate |
|---|---|---|---|
| Phase A 診斷 | M0（3 天） | 訪談 + 25 題自評 + 對標 3 case + 校長拍板主痛點 | — |
| Phase B 戰略 | M0-M1（2 週） | 90 天 roadmap + PoC 規格 + HITL 設計 + Gate 通過條件定義 | — |
| **L1 全員啟用** | M1-M2 | 校長 + 主任先學 → 全校 4 場 3 小時訓練 → 個人 Prompt Library | **Gate 1** |
| **L3 公文 PoC** | M2-M3 | 用 mihozip repo 的 Apps Script 建第一個 use case → 上線 → 月驗收 | （Gate 3 部分） |
| **L3 家長通知 PoC** | M3-M4 | HITL Gate 設計 → workflow 建置 → 試行 + post-mortem | （Gate 3 部分） |
| **L2 種子科啟動** | M5-M6 | 3-5 科教師訓練 → NotebookLM 建置 → 跨班分享機制 | **Gate 2** |
| **L3 補完 use case** | M6-M7 | 活動 / 請購 use case 上線 | **Gate 3** |
| **持續調整** | M7-M9 | 教師 Q&A / 行政維運 / 顧問退場 / KPI review | — |

### 6.3 校園 AI 1 日工作坊（壓縮版，給已有 L1 基礎的學校）

| Section | 時長 | Focus |
|---|---|---|
| AM1：L2 種子科實作 | 90 min | NotebookLM 建置 + 學科 Prompt |
| AM2：L3 概念 + demo | 90 min | mihozip repo walkthrough |
| PM1：HITL Gate 設計工作坊 | 120 min | 4 大類別實作練習 |
| PM2：Stage Gate 自評 + Roadmap | 90 min | 校長 + 主任拍板 90 天路徑 |

---

## 7. L1 → L2 → L3 三層銜接邏輯 / Tier Transition Logic

```text
L1 全員 AI 啟用 ──────────────────────┐
（教師、行政都會用個人 AI；有規範）       │
                                       │
        ↓ 觸發 L2：教師主動問              │
"我想做學科專用的 AI 怎麼辦"               │
                                       │
L2 種子科 NotebookLM ─────────────────┤
（5+ 科有教材庫；種子教師持續分享）        │
                                       │
        ↓ 觸發 L3：行政主動問              │
"我看老師都這樣用，我們行政呢"              │
                                       │
L3 行政流程自動化 ────────────────────┤
（公文 / 活動 / 請購 / 家長通知 4 use     │
 case 上線；HITL Gate 全部就位）          │
                                       │
        ↓ 學校達成跨級整合                  │
全校 AI 文化建立完成 ◄──────────────────┘
```

**核心紀律：不可跳級。** 沒走完 L1 直接 L3 = 行政自動化跑了但全員不會用，AI 變黑盒子。
**Core discipline: no level-skipping.** Without completing L1, jumping to L3 = admin auto runs but no one understands; AI becomes a black box.

---

## 8. 對位 mihozip 上游 repo / Mapping to mihozip Upstream Repo

| 上游檔案 / Upstream file | 在本課程的用法 / Use in this course |
|---|---|
| `basic-lesson/` | L1 教師全員訓練教材（直接用 + 加 Tiger AI 治理框架）|
| `advanced-lesson/` | L2 種子科教師訓練教材 |
| `src/Code.gs` | L3 行政自動化基底程式碼，學員依自家公文格式微調 |
| `admin-project-workflow.png` | L3 概念說明圖 |
| `admin_ai_workflow_detailed_implementation.html` | L3 實作教材 |
| `docs/install.md` | L3 部署 SOP |
| `docs/workflow.md` | L3 流程設計參考 |
| `docs/privacy.md` | L1-L3 治理章節參考 + Tiger AI HITL Gate 補完 |
| `docs/testing.md` | L3 測試 SOP |
| `docs/troubleshooting.md` | L3 維運 SOP |
| `notebooklm_gemini_admin_workflow_agent_*.html` | L2 進階互動範例 |

> 法律：本課程**引用上游 MIT 授權檔案**，**不複製到本 repo**。學員自行 clone 上游使用。詳見 [overlay NOTICE.md](TigerAI-School-Workspace-Workflow-overlay/NOTICE.md)。
> Legal: this course **references upstream MIT files**, **does not copy to this repo**. Students clone upstream themselves. See [overlay NOTICE.md](TigerAI-School-Workspace-Workflow-overlay/NOTICE.md).

---

## 9. Stage Gates（總覽，詳見 overlay）

| Gate | 時機 | 簽核者 | 主要 evidence |
|---|---|---|---|
| **Gate 1** | M2 結尾（L1 完成）| 校長 + 教務主任 + IT + AI Champion | 教師帳號 + Prompt Library + 規範簽署 + Quiz 通過 |
| **Gate 2** | M6 結尾（L2 完成）| 教務主任 + 教學組長 + 學科召集人 ≥ 3 | NotebookLM ≥ 5 科 + 種子教師分享紀錄 |
| **Gate 3** | M9 結尾（L3 完成）| **校長親簽** + 處室主任 + IT + 法務 + **家長代表** | use case ≥ 2 上線 + KPI 對比 + HITL 觸發紀錄 + 法務審查 |

**未過 Gate 不進下一級。** 詳見 [overlay/TIGERAI_STAGE_GATES_SCHOOL.md](TigerAI-School-Workspace-Workflow-overlay/TIGERAI_STAGE_GATES_SCHOOL.md)。

---

## 10. Deliverables

完成 9 個月課程後，學校會擁有：

After the 9-month course, the school will own:

| Deliverable | 說明 |
|---|---|
| 1. 校內 AI 使用規範 v1.0 | 校務會議通過、全員簽署 |
| 2. 個人 Prompt Library | 每位教師 ≥ 5 個 + 全校共用 Prompt Library ≥ 50 個 |
| 3. 學科 NotebookLM ≥ 5 科 | 每科 ≥ 10 份教材 + ≥ 5 個學科 Prompt |
| 4. L3 行政 use case ≥ 2 上線 | 含完整 Apps Script + HITL Gate + Runbook |
| 5. Stage Gate 1/2/3 驗收紀錄 | 簽署表 + KPI 對比 + Post-mortem 紀錄 |
| 6. HITL approval log（≥ 6 個月） | 供日後審計使用 |
| 7. 對家長代表 / PTA 的成果報告 | 1 頁 |
| 8. 對校長的 ROI 計算表 | 含時間 / 滿意度 / 預算對比 |
| 9. 校內 AI Champion 培養計畫 | 種子團隊 5 人接手維運的訓練紀錄 |
| 10. 下一階段建議 | 是否進 L4？是否擴大 L3？是否退場？ |

---

## 11. 課程包裝建議（給銷售 / 課程上架用）/ Course Packaging (for sales / platform listing)

| 課程包 | 時數 | 對象 | 收費 | 對位 SME Lite |
|---|---|---|---|---|
| **校園 AI 半日體驗營** | 4 hr | 全體教師 | 3-8 萬 | 試探客戶 |
| **校園 AI 1 日工作坊** | 8 hr | 教務 + 行政組長 | 8-20 萬 | SOHO Path |
| **校園 AI 90 天 PoC** | 3 個月 | 校長 + 種子團隊 | 30-60 萬 | SME Lite Path（縮減） |
| **校園 AI 完整 9 個月導入** | 9 個月 | 全校 + 種子團隊 + 校長 | 60-150 萬 | SME Lite Path（完整） |

---

## 12. 對應主 toolkit 與其他課程 / Relation to Main Toolkit + Other Courses

| 主 toolkit / 其他課程 | 跟本課程的關係 |
|---|---|
| [`L1_OPENWEBUI_COURSE_PLAN`](L1_OPENWEBUI_COURSE_PLAN.md) | L1 教師訓練可直接引用該課的 §6.1 講座順序 |
| [`L2_ANTIGRAVITY_COURSE_PLAN`](L2_ANTIGRAVITY_COURSE_PLAN.md) | L2 學科 NotebookLM 概念可參考其 Skill 設計章節 |
| [`L3_N8N_TIGERAI_COURSE_PLAN`](L3_N8N_TIGERAI_COURSE_PLAN.md) | 提供另一條 L3 路線（n8n vs Apps Script）—— 視學校既有系統選 |
| [`ONLINE_COURSE_DESIGN_METHODOLOGY`](ONLINE_COURSE_DESIGN_METHODOLOGY.md) | 本課程依此 SOP 撰寫，內含 Bloom LO、互動學習設計、Stage Gate |
| [`../00_Overview/SME_LITE_PATH`](../00_Overview/SME_LITE_PATH.md) | 學校屬 SME，本課程是 SME Lite Path 在教育界的具體實作 |
| [`../04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL_K12`](../04_Scenarios/SAMPLE_CLIENT_CASE_SCHOOL_K12.md) | 跟本課程一起 release 的對位案例 |
| [overlay/](TigerAI-School-Workspace-Workflow-overlay/) | 本課程的方法論依據與 governance 設計來源 |

---

**版本：** v1.0（2026-05-20）
**作者：** Morris Lu (盧業興) · Tiger AI 虎智科技
**授權：** Apache License 2.0
