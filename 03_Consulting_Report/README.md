# 03 Consulting Report — 顧問診斷與報告（顧問閉環）

> 🌐 語言：繁體中文 ｜ [English](README_EN.md) ｜ [Deutsch](README_DE.md) ｜ [Français](README_FR.md) ｜ [Español](README_ES.md) ｜ [日本語](README_JA.md) ｜ [한국어](README_KR.md)

## 一、本目錄定位

本目錄是三段式服務流程的**第三段：交付（Deliver）**，也是整套方法論的**顧問方法論核心**。

診斷（`01`）給出客觀分數，建置（`02`）讓客戶長出能力 —— 但顧問案最終要交到客戶手上的，是一份**有結構、有證據、有 Roadmap、可被決策層採用的診斷報告**。本目錄提供做出這份報告所需的一切：**八階段顧問結構的工具表、經典顧問框架庫、報告生產工作流、報告模板**。

> 🔁 **本目錄不是「6 週 marathon 線性流程」，是「顧問閉環」**。完整閉環設計見 [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md)：
> **3 階段合約**（Phase A 診斷 2W + Phase B 策略 4W + Phase C 落地 24M）+ **中期評估報告** + **每季雷達回頭核對**（科學管理的反證機制）。
> 這個閉環的重點不在「做完就好」，而在「**結構真的變圓了嗎**」 —— 持續用 Stage 2 Reference Model 雷達自我反證。

它要解決的問題是：**顧問若沒有方法論，診斷就是憑經驗的個人手藝，無法規模化、無法被新顧問複製、品質不穩。** 本目錄把「顧問怎麼做診斷」變成可教、可複製、可驗收的標準閉環。

使用本目錄的人：顧問、資深顧問、新進顧問（onboarding）、專案經理。

## 二、在方法論中的位置

| 軸 | 對應 |
| --- | --- |
| 三段式服務流程 | **交付（Deliver）** —— 第三段 |
| 八階段顧問結構 | **本目錄就是八階段（Stage 1-8）的工具與報告本體** |
| **3 階段合約模型** | **Phase A 診斷 2W → Phase B 策略 4W → Phase C 落地 24M + 季度雷達回看**（顧問閉環）|
| L1-L5 成熟度 | 報告中會引用客戶的 L 級與課程觀察 |
| 接案生命週期 | **Delivery — Handover**（報告是 Phase B 的核心交付物；Phase C 持續產出季度雷達回看記錄）|

> 兩個正交軸：**L1-L5 是「能力縱軸」（`02` 負責）；八階段是「診斷橫軸」（本目錄負責）。** 兩軸交叉產出可驗證的交付物。
>
> **L1-L5 本身就是兩條軸**（規模軸 L1-L3 + AI 自主軸 L4-L5），詳見 [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0。

## 三、目標與效益

| 目標 | 效益 |
| --- | --- |
| 八階段每一步都有可直接用的工具表 | 顧問不用重做工具設計；新顧問可快速上手 |
| 經典顧問框架庫對應到八階段 | 每一步知道「該用哪個分析框架」 |
| 報告生產工作流 | 「問題 → 可交付報告/簡報」有 SOP，不是憑手藝 |
| 報告模板結構固定 | 交付品質穩定、客戶決策層看得懂 |
| 顧問方法論可教、可複製 | 顧問團隊可規模化 |

**若跳過本目錄**：每個顧問用自己的方式做診斷、報告品質不一、新顧問無法複製、診斷淪為「資深顧問的個人手藝」。

## 四、使用流程與邏輯（三階段合約 + 季度閉環）

```text
01 診斷結果 + 02 課程觀察
   ↓
┌─ Phase A 診斷（2 週）───────────────────────────────────┐
│  Stage 1-4 八階段前半段：Awareness / Reference Model /  │
│  Discovery / Gap Analysis                                │
│  → 用 CONSULTING_TOOLKIT_TEMPLATES.md 工具表             │
│  → 中期評估報告（Mid-term Diagnosis Report）→ 客戶簽署 │
└──────────────────────────────────────────────────────────┘
   ↓ Gate A 客戶決定是否續約 Phase B
┌─ Phase B 策略（4 週）───────────────────────────────────┐
│  Stage 5-8 八階段後半段：Stakeholder / Diagnosis /     │
│  To-Be Design / Acceptance Test                         │
│  → 用 REPORT_PRODUCTION_WORKFLOW.md 8 步生產流程         │
│  → 完整 14 章診斷報告 + 24M Roadmap + ROI + 治理建議    │
│  → CONSULTING_REPORT_TEMPLATE.md 固定結構填入           │
└──────────────────────────────────────────────────────────┘
   ↓ Gate B 客戶簽署 Phase C SOW
┌─ Phase C 落地（24 個月）─ 顧問閉環的反饋段 ────────────┐
│  分階段實作 + **每季 Gate C：回頭核對 Stage 2 雷達**    │
│  → 結構真的變圓了嗎？沒變圓 → 回到對應 Stage 修正       │
│  → 每季產出：雷達回看記錄 + Roadmap 校正紀錄            │
└──────────────────────────────────────────────────────────┘
```

| 階段 | 期程 | 對應八階段 | 主要工具 | 主交付 |
| --- | --- | --- | --- | --- |
| **Phase A 診斷** | 2 週 | Stage 1-4 | TOOLKIT 前半 + FRAMEWORKS 選擇器 | **中期評估報告** + Reference Model 雷達簽署 |
| **Phase B 策略** | 4 週 | Stage 5-8 | TOOLKIT 後半 + REPORT_PRODUCTION_WORKFLOW + REPORT_TEMPLATE | **完整 14 章診斷報告** + Roadmap + ROI + 治理 |
| **Phase C 落地** | 24 個月 | 季度回頭核對 Stage 2 | TOOLKIT 季度雷達回看工具 + Risk Register | **季度雷達回看記錄** + Roadmap 校正 |

> 邏輯：`CONSULTING_TOOLKIT_TEMPLATES` 是「做診斷的工具 + 季度回看工具」；`CONSULTING_FRAMEWORKS_LIBRARY` 是「每一步該用哪個分析框架」；`REPORT_PRODUCTION_WORKFLOW` 是「怎麼高效把診斷變成交付物」；`CONSULTING_REPORT_TEMPLATE` 是「最終報告長什麼樣」。四者合起來＝**完整的顧問閉環方法論**（不是線性 marathon）。

> 📖 完整 8 階段對話劇本 + 閉環故事：[`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md)（含「為什麼閉環是科學」結語）。

## 五、檔案說明

### `CONSULTING_REPORT_TEMPLATE.md`

AI 轉型診斷報告的 Markdown 模板（v2.0 八階段對齊版）。14 章固定結構：封面、Executive Summary（含標準缺口總覽）、診斷方法、As-Is Snapshot、Reference Model Alignment（APQC + Tiger AI 雙座標）、Best Practice Integration（卓越能力特徵）、Gap Analysis、Executive Problem Statement、Phased Goals、To-Be Design、Implementation Roadmap、Change Management Plan、Governance Design、Value Tracking & Risk Register、SOW 建議。

### `CONSULTING_TOOLKIT_TEMPLATES.md`

八階段顧問診斷的**可直接使用工具表**（v2.0 對齊圖卡版）。每階段對應 1-5 個工具：40 題訪談題庫、AI/系統盤點、As-Is swimlane、**Reference Model 選用指引（APQC/SCOR/eTOM/ITIL/CMMI）+ Mapping Worksheet + 標準缺口檢核 + 雙雷達**、Best-Practice Profile + 卓越能力特徵、Missing/Broken/Redundant 表（**不作為風險評估**）、Impact×Effort、**80/20 收斂 + 5 Whys**、Problem Statement、**終極標竿 → 三階段拆解 + 組織吸收力評估**、**分階段 To-Be Operating Model + 人機協作架構（HITL）**、Skill/Workflow/Agent Map、Transformation Roadmap、**變革管理 Playbook（含抗拒處理）**、RACI、權限、**價值追蹤矩陣（時間/品質/規模/風險/資產 5 維度）**、Risk Register、Audit、Ethics、**Phase A 2W + Phase B 4W 標準排程 + Phase C 季度雷達回看工具**（顧問閉環）。複製即可用。

### `CONSULTING_FRAMEWORKS_LIBRARY.md`

經典顧問框架庫。50+ 個業界框架（MECE、Pyramid Principle、Issue Tree、Porter's 5 Forces、SWOT、BCG Matrix、5 Whys、Fishbone、Business Model Canvas、WBS/RACI、NPV/IRR、Lean/Six Sigma 等），分 7 大類。附「框架選擇器」（自然語言 → 框架組合）、「框架組合鏈」、每個框架對應到八階段、以及 §4.8 對 MECE / Issue Tree / 假設形成的深度操作規則。改寫自 yoichiojima-2/consultant（MIT）。

### `REPORT_PRODUCTION_WORKFLOW.md`

「問題 → 可交付報告/簡報」的 8 步生產工作流。含 Dummy Page（先骨架後填充）、依賴管理、7 個頁面版型、Excel 證據軌、progressive disclosure、§9 troubleshooting playbook（7 個常見問題 + 修法）。改寫自 Kafurtan/mckinsey-consultant-skills（MIT）。

### `*_EN.md`

上述檔案的英文版 sibling。

## 六、與其他目錄的對應

| 目錄 | 與本目錄的關係 | 資料流 |
| --- | --- | --- |
| `01_Assessment` | 診斷分數與雷達是八階段 Stage 1 的核心輸入 | `01` 分數 → `03` 報告 |
| `02_Course_Design` | 課中產出與觀察是報告「課程觀察」章節的素材 | `02` 課程觀察 → `03` 報告 |
| `00_Overview` | 報告是故事線的「交付」段 | `00` 故事 → `03` 落實 |
| `04_Scenarios` | 八階段 Stage 3 產業最佳實務對標引用案例 | `04` 案例 → `03` Stage 3 |
| `06_Delivery` | 報告是交付包的核心交付物；對應 Handover | `03` 報告 → `06` 交付驗收 |
| `90_References` | 框架庫與報告工作流的第三方引用（consultant / mckinsey-skills）| `90` 引用 → `03` |

## 七、常見用法情境（依顧問閉環階段）

- **新顧問 onboard**：先讀 `CONSULTING_TOOLKIT_TEMPLATES.md` 跑過一遍所有 sample，再讀 [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) 的對話劇本，最後 shadow 一場真實訪談。
- **Phase A 診斷（2 週）**：用 TOOLKIT 的 Stage 1-4 工具（40 題訪談、AI/系統盤點、Reference Model 雷達），週末產出**中期評估報告**請 Sponsor 簽署。
- **Phase B 策略（4 週）**：用 TOOLKIT 的 Stage 5-8 工具 + `REPORT_PRODUCTION_WORKFLOW.md` 8 步生產流程把診斷變成簡報，填進 `CONSULTING_REPORT_TEMPLATE.md`，產出**完整 14 章報告 + 24M Roadmap + ROI**。
- **Phase C 落地（24 個月，閉環反饋段）**：每季用 TOOLKIT 的雷達回看工具，**重新跑 Stage 2 Reference Model 雷達** —— 對比 Phase A 簽署版本，看「結構是否真的變圓」；沒變圓 → 回到對應 Stage 修正 Roadmap。
- **客戶問「為什麼用這個框架」**：用 `CONSULTING_FRAMEWORKS_LIBRARY.md` 的框架選擇器說明。
- **客戶問「6 週做完之後呢？」**：給看 [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 完整閉環圖 —— 重點不是 6 週，是 24 個月 Phase C + 季度雷達回看的反證機制。
