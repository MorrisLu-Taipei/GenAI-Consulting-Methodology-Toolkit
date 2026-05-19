# 範例客戶案例：K-12 完全中學 / Sample Client Case: K-12 Through-school

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **本案例為示範用途。** 客戶以代號「**完全中學 K**」表示（非真實機構名）。內容綜合自多個真實 K-12 客戶 + [`mihozip/google-workspace-admin-project-workflow`](https://github.com/mihozip/google-workspace-admin-project-workflow)（MIT）的實作能力，數字為示範值。
> Sample case for illustration. Client referred to as "Through-school K" (anonymized). Synthesized from real K-12 client patterns + the implementation capability of `mihozip/google-workspace-admin-project-workflow` (MIT). All numbers are illustrative.
>
> **Evidence Level：** 🔵 **L0 — AI-Simulated Teaching Case**（依 Tool 8.9 Evidence Hierarchy）

---

## 0. Benchmark-grade Summary（Tool 3.5 九欄位）

| # | 必填欄位 / Field | 本案例 / This case |
| --- | --- | --- |
| 1 | 產業 + 規模 | 教育（私立完全中學），200 教職員 / 1,500 學生 |
| 2 | 起點 L-level + 證據 | L0.5（教師個人有用 ChatGPT、無治理） |
| 3 | 終點 L-level + 證據 | L3（行政流程自動化上線） |
| 4 | 跨越期間 | 9 個月 |
| 5 | 跨越的 RM Category | Tiger AI L1-L3、SME Lite Path 4 階段 |
| 6 | 每階段投入 | NT$ 80 萬 / 12 人月（外部顧問）+ 校內 5 人核心團隊 50% 時數 |
| 7 | Key wins（可量化）| 公文簽核 3 天 → 4 小時；家長通知撰寫 3h → 30min；教師滿意度 6.2 → 8.1 |
| 8 | Key failures（踩過的雷） | 第 4 個月 AI 通知家長被罵；補上 HITL Gate 後解決 |
| 9 | 適用條件 | 50-500 教職員私立 / 公立 K-12；已用 Google Workspace；校長親自支持 |

**部署模式 / 代號：** Hybrid（雲端 Workspace + 地端 OpenWebUI for 學生敏感資料） ／ 代號 **完全中學 K**

---

## 1. 客戶背景 / Client Profile

| 欄位 | 內容 |
| --- | --- |
| 機構代號 | 完全中學 K（私立，國中部 + 高中部一貫） |
| 規模 | 教職員 200 人（教師 150 / 行政 50）、學生 1,500 人、班級 50 班 |
| 起始狀態 | L0.5 —— 30% 教師私下用 ChatGPT；無校內治理；無共用工具；行政全紙本 |
| 預算 | NT$ 80 萬（9 個月） |
| 規範 | 個資法 / 兒少法 / 教育部 AI 應用倫理規範 / 私校法 |
| 主要痛點 | (1) 公文紙本走 3 天 (2) 家長通知撰寫費時 (3) 教師備課負擔重 (4) 招生諮詢重複問答多 |

## 2. 顧問接觸 + 診斷（Phase A，3 天）

### 2.1 25 題自評問卷結果

教師組（n=120）+ 行政組（n=40）+ 校長與主任（n=10）= 170 份。

| 構面 | 均分 / 5 |
|---|---|
| 工具使用 | 1.8（30% 教師私下用，但無共用） |
| 知識沉澱 | 0.8 |
| 流程標準化 | 1.4 |
| 系統整合 | 0.6 |
| Agent 應用 | 0.2 |
| 治理 ROI | 0.5 |

**整體 L = L0.5**

### 2.2 訪談關鍵發現

- 教師對 AI **接受度高**（70% 表示想多學）；行政對 AI **疑慮高**（怕被取代）
- 校長**強烈支持**且願意親自示範（關鍵成功因素）
- IT 中心**只 1 人**，無能力獨立部署 LLM；需仰賴顧問或雲端
- 既有 Google Workspace for Education 已用 3 年，全員熟悉

### 2.3 同業對標（3 個 case）

| 對標案例 | L 級 | 工具 | 啟發 |
|---|---|---|---|
| 同類私立完全中學 A | L1.5 | OpenWebUI + Gemini | 全員教師訓練 8 週可達 L1 |
| 同類私立小學 B | L3 | Workspace + Apps Script | L3 主要 ROI 來自家長通知自動化 |
| 鄰縣公立國中 C | L2 | NotebookLM | 種子科教師 6 個月可建學科 NotebookLM |

> 對標素材改寫自 [`mihozip/google-workspace-admin-project-workflow`](https://github.com/mihozip/google-workspace-admin-project-workflow) 的 admin workflow 設計（MIT）。
> Benchmark material adapted from `mihozip/google-workspace-admin-project-workflow` (MIT).

---

## 3. CEO（校長）拍板：選定主痛點（Phase B Stage 5）

**選定：** 「**公文簽核 + 家長通知**」雙痛點（兩者人工成本最高 + 影響家長端感受最深）

**理由：**
- ROI 量化最容易（時間成本可算）
- 不直接涉及教學內容（教師抗拒風險低）
- 失敗也不會立刻爆社群（公文是內部 + 家長通知有 HITL 把關）

**候補：**
- 候補 1：招生諮詢 AI 助手
- 候補 2：教師備課輔助

---

## 4. 90 天 Roadmap（Phase B Stage 6-7）

### Sprint 1（M1：L1 全員 AI 啟用）

- W1：校長 + 主任先 hands-on（top-down 示範）
- W2-3：全校教師 L1 基本訓練（3 小時 × 4 場）+ 每人個人 AI 帳號
- W4：Gate 1 驗收（≥ 95% 教師有帳號 + 5 個個人 Prompt）

**KPI 中期：** 教師活躍使用率 ≥ 60%

### Sprint 2（M2：L3 公文 PoC）

- W5：用 [`mihozip` repo](https://github.com/mihozip/google-workspace-admin-project-workflow) 的 Apps Script 建第一版公文簽核
- W6-7：5 種公文類型試行（請假 / 活動申請 / 物資請購 / 出差 / 補班補課）
- W8：M2 月會 + 行政組長 demo

**KPI 中期：** 公文簽核時間從 3 天 → 1 天

### Sprint 3（M3：L3 家長通知 PoC）

- W9-10：家長通知 workflow + HITL Gate（**對外不可自動發**）
- W11：3 種通知類型試行（停課 / 活動 / 親師會）
- W12：M3 月會 + 校長 + 家長代表 demo + Gate 3 驗收

**KPI 終期：**
- 公文簽核時間 3 天 → 4 小時（87% reduction）
- 家長通知撰寫時間 3 hr → 30 min（83% reduction）
- 0 起 AI 對家長端誤發事件
- 行政組長能獨立維運

---

## 5. Phase C 實施 + 持續調整（M4-M9）

### M4（關鍵踩雷月）

**事件：** 某次活動延期通知，AI 草擬版本被導師按「送出」前未仔細看，發出去含錯字 + 時間錯誤。家長群組炸開。

**處理（24 小時內）：**
1. 校長親自 LINE 道歉 + 紙本道歉信
2. 暫停所有 AI 家長通知 1 週
3. Post-mortem：發現 HITL 設計太鬆（導師按送出沒看到 diff）
4. 補強：UI 強制顯示「AI 草擬內容」+ 「你要送出的最終版」對比 + 必須打勾確認 5 個項目才能送出

**結果：** 重新上線後**再無類似事件**。家長群組對「人工確認 + AI 加速」逐漸接受。

### M5-M6

- 補完物資請購 + 活動申請 use case
- 開始 L2 種子科教師訓練（3 個學科：國文 / 英文 / 自然）
- 教師 NotebookLM 建置開始

### M7-M9

- L2 種子科持續深耕
- L3 行政 4 個 use case 全上線
- 顧問逐漸退場，行政組長 + AI Champion 接手維運
- 月會頻率從每月 → 每季

---

## 6. Key Wins / 量化成果

| 指標 | 起始值 | 9 個月後 |
|---|---|---|
| 公文簽核時間（5 種公文平均） | 3 天 | 4 小時 |
| 家長通知撰寫（單份） | 3 小時 | 30 分鐘 |
| 教師 AI 使用率 | 30%（私下） | 85%（公開） |
| 教師工作滿意度（1-10） | 6.2 | 8.1 |
| 行政人員工作滿意度 | 5.8 | 7.5 |
| AI 對家長端誤發事件 | N/A | 1 次（M4，已修） |
| 家長對學校溝通滿意度（PTA 問卷） | 7.2 | 8.4 |

## 7. Key Failures / 踩過的雷

1. **M4 家長通知誤發** —— HITL UI 設計不足，導師按送出沒看清
2. **L2 種子教師找不到第 4-5 科** —— 體育 + 藝能科教師對 AI 興趣低，最終只有 3 科達 L2
3. **顧問退場太快** —— 顧問 M7 退場後，M8 出 1 次 Apps Script 小 bug 沒人會修，等 1 週才補。後續顧問加 4 週 backup support

## 8. 適用條件 / Applicability

| 條件 | 必要 / 加分 |
|---|---|
| 50-500 教職員私立 / 公立 K-12 | 必要 |
| 已用 Google Workspace for Education | 必要（用其他系統需大改） |
| **校長親自支持並示範** | **必要** |
| 至少 1 個 IT 中心人員（不必精通） | 必要 |
| 教師對 AI 整體偏正面 | 加分 |
| 有家長代表 / PTA 機制 | 加分 |
| 預算 NT$ 50-150 萬 | 必要 |

**不適用：**
- 校長對 AI 有強烈疑慮 → 先做半天 awareness session 再決定
- 教師工會強烈反對 AI 介入 → 先協商再啟動
- 全紙本文化 / IT 基礎為零 → 先補基礎再來

---

## 9. 對主 toolkit 與 overlay 的引用對照

| 用了什麼 | 出處 |
|---|---|
| SME Lite Path 4 階段壓縮 | [`00_Overview/SME_LITE_PATH.md`](../00_Overview/SME_LITE_PATH.md) |
| L1 教師訓練 deliverable | [`02_Course_Design/_deliverables/L1_*.md`](../02_Course_Design/_deliverables/) |
| L1-L3 校園實作指南 | [`02_Course_Design/TigerAI-School-Workspace-Workflow-overlay/TIGERAI_SCHOOL_L1_L3_GUIDE.md`](../02_Course_Design/TigerAI-School-Workspace-Workflow-overlay/TIGERAI_SCHOOL_L1_L3_GUIDE.md) |
| Stage Gate 設計 | [overlay/TIGERAI_STAGE_GATES_SCHOOL.md](../02_Course_Design/TigerAI-School-Workspace-Workflow-overlay/TIGERAI_STAGE_GATES_SCHOOL.md) |
| HITL Gate 設計 | [overlay/TIGERAI_HITL_GATES_SCHOOL.md](../02_Course_Design/TigerAI-School-Workspace-Workflow-overlay/TIGERAI_HITL_GATES_SCHOOL.md) |
| L3 Apps Script 實作 | [mihozip/google-workspace-admin-project-workflow](https://github.com/mihozip/google-workspace-admin-project-workflow)（MIT）|

---

## 10. Open Questions / 待研究議題

- L4 「校史 Hermes Agent」對中型完全中學是否有 ROI？目前判斷否，但需 1-2 個 case 驗證
- 同樣方法套用到**公立**學校時，採購流程 + 行政決策權限差異會如何影響時程？預估 +50% 時間
- 多校（縣市層級）統一導入時，是否需要中央 vs 校本位的不同 overlay？

---

**版本：** v1.0（2026-05-20）
**作者：** Tiger AI Morris Lu 盧業興
**授權：** Apache License 2.0
