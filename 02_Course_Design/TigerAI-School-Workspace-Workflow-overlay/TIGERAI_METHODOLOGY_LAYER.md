# Tiger AI Methodology Layer — 對 google-workspace-admin-project-workflow 的延伸

> 🌐 中英雙語 / Bilingual inline
> 對應原 repo / Maps to: <https://github.com/mihozip/google-workspace-admin-project-workflow> (MIT)

## 1. 為什麼要疊一層方法論 / Why add a methodology layer

原 repo 是 **可實作的代碼與教材**（Apps Script + Workspace + NotebookLM + Gemini 整套，含 basic / advanced lesson）。它解決了「**怎麼做**」（how）的問題。

但學校 / 縣市要實際導入時，還需要回答這 4 個問題：

1. **WHO**（誰來推） —— 是 IT、教務、AI Champion，還是校長？
2. **WHEN**（何時推） —— L1 全員、L2 部門、L3 跨部門順序怎麼排？
3. **HOW MUCH**（投入多少） —— 顧問費、人時、AI 成本？
4. **HOW TO VERIFY**（怎麼驗收） —— 每階段做完誰簽？AI 出錯怎麼回滾？

這些問題不在原 repo 範疇，是 **Tiger AI Methodology 的工作**。

The original repo provides **implementable code and educational materials** (full Apps Script + Workspace + NotebookLM + Gemini stack with basic/advanced lessons). It answers **how**.

But schools / districts deploying it need to additionally answer:

1. **WHO** drives it — IT / academic affairs / AI Champion / principal?
2. **WHEN** to roll out — L1 all-hands → L2 dept → L3 cross-dept?
3. **HOW MUCH** to invest — consulting fees / person-hours / AI cost?
4. **HOW TO VERIFY** — who signs off each phase? What's the rollback when AI errs?

These questions are out of scope for the original repo — they are **the Tiger AI Methodology's job**.

---

## 2. 對位到 Tiger AI L1-L5 / Mapping to Tiger AI L1-L5

| Tiger AI L 級 | 學校場景 / School scenario | 本 repo 怎麼用 / How this repo fits | 推不推 / Push or not |
|---|---|---|---|
| **L1** Personal Chat | 教師個人使用 AI 寫教案 / 翻譯 / 摘要 / Email 家長 | 原 repo basic-lesson 適用；補充 OpenWebUI / Gemini 個人使用 | ✅ 全校都應走 |
| **L2** Skill / Knowledge Capture | 各科教師整理「教學 Prompt 庫」+ NotebookLM 教材索引 | 原 repo advanced-lesson 適用；用 NotebookLM 建學科知識庫 | ✅ 每科至少 1 個種子教師 |
| **L3** Workflow Automation | 行政流程自動化（公文簽核 / 活動申請 / 物資請購 / 家長通知）| **原 repo 核心價值在這層** —— Apps Script + Workspace 完整 admin workflow | ✅ 教務處 / 學務處 / 總務處 都該走 |
| **L4** Autonomous Agent | 知識型 Agent（如累積學校 SOP、案例庫的 Hermes Agent） | 原 repo 不到 L4；但 NotebookLM 可作為 L4 知識底座的入門 | ⚠️ 大型私校 / 完全中學等可考慮；中小學暫無必要 |
| **L5** Multi-Agent | Agent Team 跨處室協作 | 原 repo 不適用 | ❌ 學校不需要 |

> 核心判斷：**本 repo 對學校最大的價值在 L3**（行政自動化），這是 Tiger AI Methodology 在教育界的「主戰場」。L4-L5 多數學校用不到。
> Core judgment: this repo's main value for schools is at **L3 (admin automation)** — the main battlefield of Tiger AI Methodology in education. Most schools don't need L4-L5.

---

## 3. 對位到三段式服務流程 / Mapping to Three-Phase Service Flow

Tiger AI 的三段式 = **Diagnostic（診斷）→ Strategy（戰略）→ Build（建置）**

| 階段 / Phase | 學校場景對應 / School equivalent | Output |
|---|---|---|
| **Diagnostic** | 訪談校長 + IT + 3 位教師 + 1 位行政組長；評估目前 AI 成熟度 | 1 頁學校 AI 成熟度卡 |
| **Strategy** | 選定 1-2 個首要痛點（例：每週 5 小時的活動簽核流程 / 每月 10 小時的家長通知整理） | 90 天 roadmap |
| **Build** | 依 L1 → L2 → L3 順序展開；L1 全校教師訓練 / L2 種子科教師深耕 / L3 行政組長導入 admin workflow | 上線的 AI 工具 + 培訓完成證明 |

**對應的 SOP 文件：** 主 toolkit 的 [`00_Overview/SME_LITE_PATH.md`](../../00_Overview/SME_LITE_PATH.md)（學校通常落在 SME 50-300 人區間）

---

## 4. 對位到八階段顧問流程 / Mapping to Eight-Stage Flow

| 八階段 / 8-Stage | 學校情境 / School context |
|---|---|
| **Stage 1 As-Is** | 訪談、觀察、看 1 週實際工作流 / Interview, observe, watch 1 week of actual work |
| **Stage 2 Reference Model** | 給校長看 2-3 個同類學校的 case（去識別化）/ Show 2-3 peer-school cases (anonymized) |
| **Stage 3 Best Practice** | 帶看本 repo 的 admin workflow 圖 / Walk through this repo's admin workflow diagram |
| **Stage 4 Gap Analysis** | 列「現況」vs「理想」的 5 個 gap / List 5 gaps between current and ideal |
| **Stage 5 Problem Definition** | CEO（校長）拍板 1-2 個主痛點 / Principal picks 1-2 primary pains |
| **Stage 6 Phased Goals** | 90 天 KPI（如：活動簽核時間 5h→1h）/ 90-day KPI |
| **Stage 7 To-Be Design** | 用本 repo 的 Apps Script + Workspace 設計新流程 / Design new flow using this repo |
| **Stage 8 Implementation & Change** | 試行 1 個處室 → 滾動全校 / Pilot 1 dept → roll out school-wide |

**對應的 SOP 文件：** 主 toolkit 的 [`00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../../00_Overview/EIGHT_STAGE_FLOW_STORY.md)

---

## 5. 對位到 SME Lite Path（中小組織壓縮版）/ Mapping to SME Lite Path

學校多在 50-300 人區間（私立小學 ~ 50 人；公立國中 ~ 100-200 人；完全中學 ~ 300-500 人），對應主 toolkit 的 **SME Lite Path 4 階段**：

| SME Lite 階段 | 學校情境 |
|---|---|
| **S1. 摸底 + 對標**（半天） | 訪校長 + IT + 1 教師 + 1 行政；對標 3 個同類學校 case |
| **S2. 找痛點**（1 天） | 教師工作坊列 Top 5 痛點 + ROI 評估 → 校長拍板 1 個 |
| **S3. 定 90 天目標**（半天） | PoC 規格：例「活動簽核從 5h → 1h」+ 量化 KPI |
| **S4. 做 + 調**（3 個月） | 用本 repo 的 Apps Script 建第一版 → 週 demo + 雙週調整 + 月驗收 |

**收費對應：** SOHO Path（補習班 / 小型私校 < 20 人）5-20 萬；SME Lite Path（公私立中小學 50-300 人）30-150 萬。
**Pricing:** SOHO Path (cram schools / small private < 20) USD 1.5K-7K; SME Lite Path (public/private K-12, 50-300) USD 10K-50K.

---

## 6. L4-L5 為什麼不推給學校 / Why we DON'T push L4-L5 to schools

| 原因 / Reason | 說明 |
|---|---|
| **學校工作型態不需要自主 Agent** | 行政工作 90% 是規則明確的流程（公文 / 簽核 / 通知），L3 workflow 已足夠 |
| **HITL 永遠是教育界 default** | 對學生 / 家長的所有對外輸出都必須人工確認 —— L4 Agent 「自主執行」對教育界是負分 |
| **資料敏感度** | 學生資料是嚴格 PII，不適合丟給知識型 Agent 自動處理 |
| **預算 / 人力配比** | 學校沒有 L4-L5 級別的 IT 維運能量 |
| **教育部 / 縣市規範** | 多數縣市政府對學校 AI 應用有規範，L4-L5 容易踩線 |

> 例外：大型私立完全中學（500+ 學生 + 完整 IT 組）可以**選擇性**走 L4。例：知識型 Agent 累積「該校歷年招生簡章 / 課程大綱 / 校友訪談」變成內部知識庫。但這是少數，不應 push 給所有學校。
> Exception: large private K-12 schools (500+ students + full IT team) may **selectively** pursue L4. E.g., knowledge Agent that accumulates the school's admission brochures / curriculum / alumni interviews into an internal KB. But this is a minority case, not pushed universally.

---

## 7. 跟主 toolkit 的關係 / Relation to Main Toolkit

本 overlay **不取代** 主 toolkit 的任何文件。它是：

1. 教育界特化的 **應用例（case-based instantiation）**
2. 對於 L1-L3 的具體教育情境補完
3. 跟原 repo 的 implementation 銜接的橋樑

This overlay **does not replace** any document in the main toolkit. It is:

1. An education-sector **case-based instantiation**
2. A concrete education-context completion of L1-L3
3. A bridge to the original repo's implementation

如果你是學校 / 顧問接案，建議閱讀順序：

If you are a school / consultant taking an engagement, recommended reading order:

```
1. 主 toolkit README                           總覽
2. 主 toolkit SME_LITE_PATH.md                 找你的壓縮路徑
3. 本 overlay README                           本案位置
4. 本 overlay TIGERAI_METHODOLOGY_LAYER.md     方法論對位（本檔）
5. 本 overlay TIGERAI_SCHOOL_L1_L3_GUIDE.md   實際操作指南
6. 本 overlay TIGERAI_STAGE_GATES_SCHOOL.md   驗收設計
7. 本 overlay TIGERAI_HITL_GATES_SCHOOL.md    人工審核設計
8. 原 repo basic-lesson / advanced-lesson      實際課堂材料
9. 原 repo src/Code.gs                         技術實作
```

---

**Version:** v0.1.0 (2026-05-20)
**License:** Apache 2.0 (Tiger AI overlay; original repo MIT)
