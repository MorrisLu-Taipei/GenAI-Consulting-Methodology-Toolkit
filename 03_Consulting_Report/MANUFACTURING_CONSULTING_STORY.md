# 製造業顧問實戰故事：一家封測廠走過 8 步顧問手法

> 🌐 語言：繁體中文 ｜ English: [MANUFACTURING_CONSULTING_STORY_EN.md](MANUFACTURING_CONSULTING_STORY_EN.md)（待補）
>
> Apache License 2.0 · 作者：Morris Lu · Tiger AI 虎智科技

最後更新：2026-05-17

---

> ⚠️ **重要學術誠信免責聲明**
>
> **「明昌封裝（MingChang Packaging）」是 AI 生成的虛構公司**，NOT 真實案例。本故事是教學素材，幫助非技術讀者快速理解 8 步顧問手法。所有數字（公司規模、KPI、預算、時程、客戶 A 訂單下降百分比）僅供說明。
>
> - 依 [`CONSULTING_TOOLKIT_TEMPLATES.md`](CONSULTING_TOOLKIT_TEMPLATES.md) Tool 8.9，這是 **L0 AI-Simulated 教學案例**（L1 以下）
> - 真實縱貫研究案例需等 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) 18-24 個月實證研究完成後才會存在
> - 本故事**不得**用於「我們有真實客戶這樣做過」的對外行銷

---

## 0. 為什麼需要這份故事

**問題**：`03_Consulting_Report/` 目錄裡是 Templates（範本）、Workflow（生產流程）、Toolkit（工具表）、Frameworks Library（框架庫）。這些文件對顧問有用 — 但客戶看了會問：

> 「這些範本和工具是怎麼串成一場顧問案？我（製造業老闆）要花 NT$ 9.8M、6 週 + 24 個月，到底會經歷什麼？最後拿到什麼？」

**這份故事就是答案**。

用一家虛構的製造業（明昌封裝，半導體封測廠）作為主角，把 8 步顧問手法從頭到尾走一遍，**讓客戶在簽約前就清楚知道每一步會發生什麼、自己要做什麼、會拿到什麼**。

---

## 1. 主角設定：明昌封裝

| 項目 | 內容 |
| --- | --- |
| **產業** | 半導體封裝測試（FATP）|
| **規模** | 700 名員工，年營收 NT$ 12 億 |
| **位置** | 新竹科學園區 |
| **核心客戶** | 大客戶 A（佔營收 35%）|
| **觸發事件** | 客戶 A 採購總監寄信：「下季訂單將砍 18%。原因：投訴回應 5 天太慢、提案週轉 4 天落後、不良率 3.2% 高於同業 1.8%。」|
| **管理層痛點** | CEO 老明（55 歲，創辦人）夜不能寐：3 家直接競爭對手都已部署 AI 品檢與投訴 Agent，我們連公司用 ChatGPT 帳號都沒有 |
| **IT 現況** | IT 副理 1 人主管，2 名 IT FTE，ERP（鼎新）+ MES（自製）+ CRM（無）|
| **AI 現況** | 員工私下用 ChatGPT，月燒 NT$ 24,000 在個人信用卡，data 流向不明 |
| **預算** | 24 個月內可投入 NT$ 8M |

**老明的核心問題**：「我們到底落後在哪裡？要怎麼追？追到什麼程度？多少時間？多少錢？」

---

## 2. 故事架構：3 Phase × 8 Stage

```
Phase A 診斷（2 週 / NT$ 80 萬）
├─ Stage 1 As-Is Snapshot
├─ Stage 2 Reference Model Alignment
└─ Stage 3 Best Practice Integration（資料準備）

Phase B 戰略（4 週 / NT$ 200 萬）
├─ Stage 3 完成 Ideal Practice 共創（客戶簽署）
├─ Stage 4 Gap Analysis
├─ Stage 5 Problem Definition
├─ Stage 6 Benchmarking + Phased Goals
└─ Stage 7 To-Be Design

Phase C 實施（24 個月 / NT$ 700 萬）
└─ Stage 8 Implementation & Change
   ├─ Phase 1 Foundation（0-6 月）
   ├─ Phase 2 Optimization（6-15 月）
   └─ Phase 3 Excellence（15-24 月）
```

---

## 3. Phase A：診斷 2 週（Stage 1 + 2 + 3 資料）

### 第 1 天：簽約 + Day 0 Kickoff

**早上 9:00**，Tiger AI 顧問張顧問與老明、IT 副理林副理坐在明昌會議室。

**張顧問拿出兩份文件**：
1. Phase A 合約：2 週，NT$ 80 萬，交付物：**中期評估報告**
2. Phase B / C 意願書：「先做完 Phase A，看完報告再決定要不要簽。」

老明點頭。**這是他人生第一次有顧問說「先看再決定」。**

### Stage 1 As-Is Snapshot：聽，看，不評論（第 1 週）

#### Day 1-2：經營層深訪

| 對象 | 時長 | 工具 | 重點問題 |
| --- | --- | --- | --- |
| CEO 老明 | 60 分鐘 | Tool 1.1 40-Q 訪談題庫 §A | 「公司 3 年最大隱憂？AI 是機會還威脅？」|
| COO 王經理 | 60 分鐘 | 同上 | 「跨部門協作最大瓶頸在哪？」|
| IT 副理林 | 60 分鐘 | 同上 | 「IT 預算、人力、現有系統？」|

**訪談紀錄**：張顧問**全程錄音**（已徵得受訪者書面同意），不打斷、不評論、不下推論。**每段錄音由 AI 自動轉成逐字稿，當天寄回受訪者確認**。

#### Day 3：部門長 + 一線員工深訪

| 對象 | 時長 | 工具 | 為什麼必要 |
| --- | --- | --- | --- |
| QC 部長 × 1 | 90 分鐘 | Tool 1.1 §B | 不良率 3.2% 的根本流程在哪 |
| Sales 部長 × 1 | 90 分鐘 | 同上 | 提案週轉 4 天的真實時間都花在哪 |
| CS 部長 × 1 | 90 分鐘 | 同上 | 投訴 5 天回應的卡點在哪 |
| 線長老陳 × 1 | 30 分鐘 | Tool 1.1 §C | 25 年現場經驗，知道真實流程怎麼跑 |
| 業務 Sophie × 1 | 30 分鐘 | 同上 | 一線視角的真實提案流程 |
| CS 客服 Jenny × 1 | 30 分鐘 | 同上 | 一線視角的真實投訴流程 |

**老陳訪談的關鍵 5 分鐘**：

> 張顧問：「老陳，你每天最重複的 5 件事是？」
> 老陳：「品檢、報工、異常通報、領料、交班。」
> 張顧問：「這 5 件事，有哪幾項是寫下來的 SOP？」
> 老陳：「異常通報有 SOP，但跟我實際做的不太一樣。其他 4 項沒有，靠經驗。」
> 張顧問：「萬一你退休，誰會這 5 件事？」
> 老陳沉默 30 秒，說：「沒人。」

**這 5 分鐘為什麼重要**：明昌的「知識資產化」缺口，不是顧問推論出來的 — 是線長親口說的。**錄音可作為 Stage 5 Root Cause 的 Evidence Level L1 證據**。

#### Day 4：AI 使用盤點 + 系統盤點

張顧問與林副理一起列出**所有員工用過的 AI 工具**（包括私下）：

| 工具 | 部門 | 月支出 | 付款方式 | 資料邊界 |
| --- | --- | --- | --- | --- |
| ChatGPT Plus | 業務 × 5 | $100/月 | 個人信用卡 | 不明（客戶資料可能流出）|
| Claude Pro | 行銷 × 2 | $40/月 | 個人信用卡 | 不明 |
| Gemini Advanced | IT × 1 | $20/月 | 個人信用卡 | 不明 |
| Notion AI | QC × 3 | $30/月 | 個人信用卡 | 不明 |
| Microsoft Copilot | 行政 × 4 | $120/月 | 公司刷卡 | 已簽 NDA |
| **總計** | | **NT$ 約 42,000/月** | 大部分在個人卡 | **資料邊界不明 = Shadow IT 風險** |

**林副理當場臉色發白**：「我們從來不知道有這麼多人在用 AI。」

#### Day 5：3 條真實流程 Swimlane

張顧問與部門長一起，用便利貼在牆上重建 3 條最關鍵流程：

1. **RFQ → 出貨**（客戶詢價到貨物送達）
2. **投訴處理**（客戶投訴到正式回覆）
3. **製程異常通報**（產線發現異常到部門主管確認）

每一步都標上**痛點密度點（0-3）**：

```
「投訴處理」流程（簡化版）：

客戶寄信進 Gmail   → ●●● 痛（每天 15-30 封，業務漏看率 ~12%）
業務轉發 CS         → ●● 痛（轉發 + 翻譯前因後果，平均 30 分鐘）
CS 查 ERP 訂單史    → ●●● 痛（ERP 介面慢，平均 45 分鐘）
CS 查 QC 不良紀錄   → ●●● 痛（要走實體去 QC 拿紙本，平均 60 分鐘）
CS 寫回覆草稿       → ●● 痛（一封需 30-60 分鐘）
主管審核           → ● 痛（主管常出差，等待 1-3 天）
寄回客戶           → ✓
......
合計：平均 5 個工作天
業界 1 流：1 個工作天
```

**老明看了痛點圖**：「原來我們的『5 天』不是均值 — 是糟糕案例 1 週，好案例 3 天，全都人力撐著。」

**Week 1 末，張顧問在客戶面前說：「現在我們知道貴公司在做什麼了。」不評論，不推論。**

---

### Stage 2 Reference Model Alignment：國際標準對照（第 2 週）

#### Day 6：選 3 套國際參考模型

張顧問拿出**3 套標準**（Tool 2.1）：

1. **APQC PCF**（美國生產力與品質中心，13 大流程分類）
2. **SCOR**（供應鏈協會，Plan / Source / Make / Deliver / Return / Enable）
3. **Tiger AI L1-L5**（GenAI 採用成熟度）

「為什麼用 3 套？因為每套都覆蓋一部分。APQC 看流程結構、SCOR 看製造供應鏈、Tiger AI L1-L5 看 AI 成熟度。**3 套疊起來才看得出全貌**。」

#### Day 7-8：Mapping Worksheet

張顧問把明昌**每一個實際流程與系統**填進 3 套標準的格子裡（Tool 2.2）：

```
APQC 4.0 Deliver（交付）
  └─ 4.4 投訴處理        → 明昌：分散在 Gmail / Excel / 紙本
APQC 11.x Knowledge（知識管理）
  └─ 11.1 知識策略       → 明昌：無
  └─ 11.2 知識文件化     → 明昌：無
SCOR Make（製造）
  └─ M3 異常處理         → 明昌：人力 + 紙本
Tiger AI L1                → 明昌：未部署
Tiger AI L2                → 明昌：無 Skill Library
Tiger AI L3                → 明昌：Power Automate 1 條
Tiger AI L4                → 明昌：無
Tiger AI L5                → 明昌：無
```

#### Day 9：標準能力差距清單 + 雙雷達

張顧問用 Tool 2.3 / 2.4 製作 **2 張雷達圖**：

**雷達 1：APQC 13 大流程完整性（0-4 分）**
```
        知識管理 0  →  ⚠ 空格
       /          \
     IT 治理 1     交付 1
     /              \
   生產 2 ────── 供應鏈 2
     \              /
     財務 3      銷售 2
       \          /
        人資 2  研發 1
        
        平均：1.6 / 4（偏低）
```

**雷達 2：Tiger AI L1-L5 成熟度**
```
        L1 = 0  ⚠
       /        \
     L5 = 0     L2 = 0  ⚠
       \        /
        L4 = 0   L3 = 部分（1 條 Power Automate）
        
        平均：0.2 / 4（極低）
```

**Day 9 末，張顧問把 2 張雷達寄給老明**：「請你今晚回家看，明天我們討論。」

**老明當晚回家，把 2 張雷達放在餐桌上**。
他太太看了問：「你們公司這些格子真的都是 0？」
老明：「我今天才知道。」

#### Day 10：產業 Benchmark 案例準備

張顧問從 [`../04_Scenarios/`](../04_Scenarios/) Case Library 挑出 3 個與明昌相近的案例（**只挑材料，不下結論**）：

| 案例 | 規模 | 期程 | 結果 |
| --- | --- | --- | --- |
| 半導體封裝廠 A | 700 員工 | 9 個月 | 投訴回應 5d → 1d |
| 醫院 X 線部門 | 1,200 員工 | 12 個月 | 報告產出 3d → 2hr |
| 行銷代理商 Z | 800 員工 | 14 個月 | 提案週轉 5d → 1d |

> ⚠️ 所有案例皆標註 **Evidence Level L0 / L1（AI-Simulated 或 Anonymized Composite）**，不可作為合約保證。

---

### Phase A 交付物：中期評估報告（10-15 頁）

**Day 11-12**：張顧問寫報告。**內容刻意「不下結論」**，只呈現事實：

```
中期評估報告目錄：

§1 Executive Summary（1 頁）
   主訊息：「依國際標準，貴公司在 SCOR Make/Deliver、
            APQC 11.x Knowledge、Tiger AI L1-L3 有結構性空格」
            
§2 As-Is Snapshot（3 頁）
   - 18 場訪談摘要（含老陳的「沒人」5 分鐘）
   - 系統盤點表（含 Shadow IT 月支出）
   - 3 條 Swimlane 流程圖（含痛點密度點）

§3 Reference Model Mapping（3 頁）
   - APQC 13 大流程映射表
   - SCOR 6 大區域映射表
   - Tiger AI L1-L5 自評表

§4 雙雷達（2 頁）
   - APQC 雷達（虛線：業界中位數；實線：明昌）
   - Tiger AI L1-L5 雷達（虛線：標準；實線：明昌）

§5 產業 Benchmark 材料（4 頁）
   - 3 個同業 Benchmark Profile
   - ⚠ 標註 Evidence Level
   - 「材料僅供參考，不代表客戶可達成相同數字」

§6 下階段建議（2 頁）
   - Phase B Ideal Practice Workshop（半日）
   - Stage 4 Gap Analysis
   - Stage 5 Problem Definition
```

**Day 13-14：客戶審核 + Closeout 會議**

老明帶著明昌核心幹部 7 人（CEO + COO + IT 副理 + QC / Sales / CS / HR 部長）開會。

**會議流程**：
1. 張顧問播放雷達圖 → 全場沉默 30 秒
2. COO 翻 Swimlane：「我們的投訴流程真的有這些洞……」
3. IT 副理看 Shadow IT 表：「私下 ChatGPT 月燒 4 萬 2，資料邊界不明……」
4. HR 部長看老陳訪談：「他說『沒人』時，我心裡涼了一下。」

**老明轉頭問張顧問**：「下一步呢？」

張顧問：「下一步是 Phase B Strategy，4 週 NT$ 200 萬。我們會做一場 Ideal Practice 共創工作坊，**由你們自己決定 12 個月要達到什麼目標**。我不會告訴你目標 — 你們簽完字後，我再幫你們做 Gap Analysis 跟 To-Be Design。」

**老明當場簽 Phase B 合約**。

> **Gate A 設計的價值**：90% 客戶在這一刻簽 Phase B。為什麼？因為雷達是國際標準說的（不是顧問說的），痛點是員工自己說的（不是顧問推的），Benchmark 是同業已經做的（不是顧問虛構的）。**Phase A 的設計目標就是「讓客戶自己看到差距」**。

---

## 4. Phase B：戰略 4 週（Stage 3-7）

### Stage 3 Ideal Practice 共創工作坊（Day 15 上午，半日）

**地點**：明昌會議室。會議桌上鋪一張 A2 紙：4 層架構圖（Governance / Business / Information / Technical）。

**參加人**：CEO 老明、COO 王經理、IT 副理林、QC / Sales / CS / HR 4 位部長 — **共 7 人**。

#### 第 1 步：材料展示（30 分鐘）

張顧問拿出 3 個同業案例（Tool 3.1 / 3.3 / 3.4）：
- 半導體封裝 A：投訴 5d → 1d，9 個月
- 醫院 X 部門：報告 3d → 2hr，12 個月
- 行銷代理 Z：提案 5d → 1d，14 個月

**張顧問刻意強調**：「我只是展示材料，**不推薦你們學哪一家**。每家都不同，你們自己挑。」

#### 第 2 步：獨立投票（45 分鐘）

7 人**獨立**寫便利貼 — **「我希望我們公司 12 個月後能做到什麼？」** 規則：

- 每張便利貼必須是 **「動詞 + 量化指標」**（例：「投訴回應 5 天 → 1 天」）
- **不准討論**，靜靜寫 45 分鐘
- 一人可寫多張

#### 第 3 步：集體共識（60 分鐘）

7 人把便利貼貼到 4 層架構牆上。**驚人的事發生了** — 80% 重疊：

| 共識項目 | 寫的人數（含老明）|
| --- | --- |
| 投訴回應 5d → 1d | 7 / 7 ✓ |
| 提案週轉 4d → 1d | 6 / 7 |
| 不良率 3.2% → 2.0% | 5 / 7 |
| 知識沉澱：每月 ≥ 20 個 Skill | 6 / 7（含老明）|
| 製程異常 → 假設 ≤ 1 hr | 4 / 7 |
| 客戶 A 訂單回升 +10% | 5 / 7 |

**張顧問**：「**這就是你們公司的共識**。我什麼都沒說，是你們自己寫的。」

#### 第 4 步：Reality Check（45 分鐘）

張顧問第一次介入，拿出 Tool 6.3 Organizational Absorption：

- 「預算上限 NT$ 8M，能支撐這 6 大目標嗎？」→ 7 人開始算錢
- 「IT 只有 2 FTE，Phase 2 整合 ERP 來得及嗎？」→ 林副理：「來不及，至少要 +0.5」
- 「製程異常 ≤ 1 hr 太激進，3 個月內做不到」→ 5 → 4 hr

**7 人開始砍自己的清單**。最後從 12 項砍到 8 項。

#### 第 5 步：定義表（30 分鐘）

**Ideal Practice Definition Table v1**（共 8 項，節選）：

| # | Capability | RM Mapping | 12 個月目標 | Evidence Criteria |
| --- | --- | --- | --- | --- |
| 1 | 投訴回應 | APQC 4.4 + Tiger AI L3 | 90% 1hr 分類 + 24hr 人工回覆 | n8n Workflow + Reviewer 簽核率 ≥ 95% |
| 2 | 知識沉澱 | APQC 11.x + Tiger AI L2 | 月增 ≥ 20 個 Skill | Skill Library Git + Owner + IPOE |
| 3 | 製程根因 | SCOR Make + Tiger AI L4 | 異常 → 假設 ≤ 1 hr | Hermes Agent + 5 task Reviewer pass |
| 4 | 提案週轉 | APQC 5.0 + Tiger AI L3 | 4d → 1.5d | n8n + Sales Skill |
| ... | | | | |

#### 第 6 步：3 方簽署（15 分鐘）

**3 方簽署**：
- **老明（Sponsor）** ─────────── 簽
- **王 COO（AI Champion）** ─────── 簽
- **林副理（IT Lead）** ─────────── 簽

老明簽完字時，**手在抖**。他跟張顧問說：

> 「我這輩子第一次，目標不是顧問或老婆寫給我，而是**我自己簽**的。」

> **這張定義表是後續所有計算的基石**。Stage 4 Gap、Stage 5 Root Cause、Stage 6 Phased Goals、Stage 7 To-Be、Stage 8 ROI — 全部以這張表為錨。**客戶不能否認自己簽過的目標**。

---

### Stage 4 Gap Analysis：差距 = （Ideal − As-Is）

**Day 16-17**：張顧問做減法。每一項都有具體數字。

| # | Ideal | As-Is | Gap | 分類 |
| --- | --- | --- | --- | --- |
| 1 | 投訴 1d | 投訴 5d | **-4d**（80%）| Broken（系統能力有，流程斷裂）|
| 2 | 月增 20 Skill | 月增 0 | **-20** | Missing（無平台、無角色）|
| 3 | 製程根因 1hr | 平均 8hr | **-7hr**（87%）| Missing（無 Agent 平台）|
| 4 | 提案 1.5d | 提案 4d | **-2.5d** | Redundant（重複拷貝）|

**Day 18**：Impact × Effort 排序（Tool 4.3）：

```
Impact 高 + Effort 低 → 先做：投訴回應（#1）、提案週轉（#4）
Impact 高 + Effort 高 → 中期：製程根因（#3）、知識沉澱（#2）
```

---

### Stage 5 Problem Definition：80/20 收斂到根因

**Day 19**：80/20 + 5 Whys（Tool 5.1 / 5.2）。

```
為什麼投訴 5d？
  └─ 因為 CS 查 ERP + QC 資料要 1.5 hr/件
為什麼 CS 不能直接查？
  └─ 因為沒有跨系統整合
為什麼不整合？
  └─ 因為沒有「自動化串接」的角色（IT 太忙）
為什麼 IT 沒人做？
  └─ 因為自動化沒被視為「Knowledge Asset」，無 Owner、無預算、無 KPI
為什麼沒被視為 Asset？
  └─ 因為公司**沒有「知識資產化」的策略、工具、誘因**

⇒ 根因（Root Cause）：明昌缺乏「知識資產化」的角色、工具、誘因
```

**Day 20-21**：Executive Problem Statement（Tool 5.3 / 5.4）。

**明昌的 Executive Problem Statement**（一句話）：

> **明昌缺乏「知識資產化」的角色、工具、誘因。80% 的 Gap（投訴慢 / 提案慢 / 知識零沉澱 / 根因慢）都來自「同樣的事重複做，沒人沉澱、沒人複用」。**

老明看了這句話，沉默 5 分鐘，說：「**我們不是缺 AI，我們缺的是『讓知識變成資產』這件事**。」

---

### Stage 6 Benchmarking + Phased Goals：把 Ideal 拆成可吸收的步驟

**Day 22**：把 Ideal 拆成 3 個 Phase（Tool 6.1）。

| Phase | 期程 | 目標 | 預算 |
| --- | --- | --- | --- |
| Phase 1 Foundation | 0-6 月 | 全公司 L1 OpenWebUI + 5 個核心 Skill + AI Policy 簽署 ≥ 90% | NT$ 280 萬 |
| Phase 2 Optimization | 6-15 月 | L2 Skill Library ≥ 15 個 + L3 n8n Workflow ≥ 3 條上線 | NT$ 350 萬 |
| Phase 3 Excellence | 15-24 月 | L4 Hermes Agent 通過 4A-4E + L5 ClawTeam 跨部門演練 | NT$ 70 萬 |

**Day 23**：組織吸收評估（Tool 6.3，6 維度）。

| 維度 | 明昌分數（0-4）| 解讀 |
| --- | --- | --- |
| Budget | 3 | 8M 預算夠，但要分 24 個月攤 |
| AI Champion | 4 | 老明 + 王 COO + 林副理 3 人到位 |
| **IT FTE** | **1.5** ⚠️ | **2 名 IT 已 maxed，Phase 2 需要 +0.5 dedicated** |
| Governance | 2 | 缺 AI Policy 與 Audit Log |
| AI Literacy | 2 | 私下用過，但無系統化訓練 |
| Change Capacity | 3 | 老明願意推，但前線可能反彈 |

**關鍵發現**：IT FTE 不足，Phase 2 風險高。

**Day 23 晚，張顧問與老明、林副理**開會：

- 張顧問：「林副理，你 2 名 IT 能多撐 0.5 FTE 嗎？」
- 林副理：「不行，我們連 ERP 維運都來不及。」
- 老明：「那要不要外包？」
- 張顧問：「外包做 PoC 可以，**長期維運最好還是自己人**。建議延長 Phase 2：6 → 9 個月，多 3 個月給 IT 內部消化。」
- 老明：「好，照你建議。但這 3 個月誰決定的？」
- 張顧問：「**你決定的**。我只是提數字給你看。」

**老明簽下 Phase 2 從 6 → 9 個月的決定**。這是他第二次「自己決定」的瞬間。

**Day 24**：Stage Gate Criteria（Tool 6.2）。

每個 Phase 結束時的驗收條件：

```
L1 Gate（Phase 1 末 = Month 6）：
□ OpenWebUI 部署 ≥ 700 帳號
□ AI Policy 簽署率 ≥ 90%
□ 5 個 Core Skill 上線，每個有 Owner + IPOE 文件
□ Prompt Library ≥ 30 條
□ Stage 2 雷達 L1 從 0 → 4

L2/L3 Gate（Phase 2 末 = Month 15）：
□ Skill Library ≥ 15 個
□ n8n Workflow 上線 ≥ 3 條（含 1 條投訴自動分類）
□ Reviewer 簽核率 ≥ 95%
□ APQC 4.4 從 1 → 3

L4/L5 Gate（Phase 3 末 = Month 24）：
□ Hermes Agent 通過 4A-4E
□ ClawTeam 跨部門演練成功 1 次
□ Stage 2 雷達整體面積增加 ≥ 60%
```

---

### Stage 7 To-Be Design：未來藍圖

**Day 25-26**：3 個 Phase 各畫一張 To-Be Operating Model（Tool 7.1）。

**Phase 1 末的 To-Be 簡圖**：

```
[每位員工] → [OpenWebUI 個人帳號]
                  ↓
       [部門 Skill Library]
       （新人第一天就能用）
                  ↓
       [AI Policy 治理層]
       （資料邊界 / 權限 / 稽核）
```

**Phase 2 末的 To-Be 簡圖**：

```
[Gmail 投訴] → [n8n Trigger]
                  ↓
       [n8n 自動：查 CRM + ERP + QC]
                  ↓
       [AI 生成回覆草稿]
                  ↓
       [CS Reviewer 簽核（HITL）]
                  ↓
       [自動寄回 + Notion 跟進]
```

**Day 27**：Human-AI Collaboration（Tool 7.2）。每個流程都標明：

| 步驟 | 自動化方 | HITL 點 | 簽核責任 |
| --- | --- | --- | --- |
| 投訴分類 | AI | ❌ 不需 | — |
| 草稿生成 | AI | ✅ 需要 | CS Reviewer |
| 寄出客戶 | n8n | ❌ 由 Reviewer 觸發 | — |
| 進入 CRM | n8n | ❌ | — |

**Day 28**：Skill Map / Workflow Map / Agent Map / Integration Architecture（Tool 7.3 - 7.6）。

完整圖太長，重點是**告訴客戶「24 個月後，每個系統如何串成一個整體」**。

---

### Phase B 交付物：完整 30-50 頁顧問報告 + 簽署的 Ideal Practice Table

**Day 29-30**：張顧問與團隊（顧問 A + 顧問 B + 分析師 C）寫完整顧問報告。**參考 [`CONSULTING_REPORT_TEMPLATE.md`](CONSULTING_REPORT_TEMPLATE.md) 14 大章節結構**：

```
§1 封面 + Executive Summary（CEO 1 頁讀完）
§2 公司現況概覽
§3 As-Is Snapshot（Stage 1 整合）
§4 Reference Model 對標（Stage 2 整合）
§5 Ideal Practice Definition Table（3 方簽署原檔）
§6 Gap Analysis Matrix（Stage 4 整合）
§7 Problem Definition + Root Cause（Stage 5 整合）
§8 Phased Goals + Stage Gate（Stage 6 整合）
§9 To-Be Operating Model（Stage 7 整合）
§10 Skill / Workflow / Agent Map
§11 Integration Architecture（4 層架構）
§12 Change Management Plan + Resistance Playbook
§13 ROI Tracking Matrix（5 維度）
§14 Risk Register + AI Ethics Checklist
```

報告**每段都有 Evidence Tag**（Tool 8.9）：

- `[E:L3]` 系統 log 等級（如：n8n Execution Log）
- `[E:L2]` 文件等級（如：客戶簽署文件）
- `[E:L1]` 自報等級（如：訪談錄音）

**Day 31-32：客戶審核 + Closeout 會議**

老明帶 7 人核心幹部 + 副董事長 + 財務長 + 法務長共 10 人來看報告。

**副董事長翻 5 分鐘問**：「為什麼是 24 個月？」
**老明翻到 §8.3**：「IT 吸收力評估。我決定的。」

**財務長問**：「為什麼客戶服務先？不是業務？」
**老明翻到 §6.2**：「Impact 4、Effort 1、Strategic Fit 5，總分 20，第一名。」

**法務長問**：「AI 倫理有沒有處理？」
**老明翻到 §14**：「Tool 8.8 AI Ethics Checklist 15 項，全部簽署。」

**副董事長闔上報告**：「**被說服了。簽 Phase C**。」

> **這就是 Stage 4-7 的價值**：客戶老闆**不是被顧問說服**，而是**能用自己簽過的目標說服自己董事會**。報告每段都有 Evidence Tag，每段都可以被獨立稽核。

---

## 5. Phase C：實施 24 個月（Stage 8）

### Month 1：啟動

**Day 33-39**：張顧問完成 Stage 8 所有治理文件：

- Transformation Roadmap（24 個月 / 6 季）
- Change Management Plan + 阻力 Playbook
- RACI + Permission Matrix + Audit Log
- Value Tracking Matrix（5 維度 Dashboard）
- Risk Register + AI Ethics 簽署

**Day 39**：SOW 簽署 + Phase 1 Kickoff Meeting。

### Phase 1 (Month 1-6) Foundation

進度：
- Month 1：OpenWebUI 部署在公司私有雲（IT 主導）
- Month 2：50 名種子用戶試用 + 收集 Prompt
- Month 3：AI Policy 全公司宣導 + 簽署
- Month 4：5 個 Core Skill 完成（CS / Sales / QC / IT / HR 各 1 個）
- Month 5：全公司 700 帳號開通
- Month 6：**L1 Gate Acceptance**

**Month 3 的小奇蹟**：CS 副理 Sophie 用 Skill 寫投訴回覆，從 60 分鐘縮短到 25 分鐘。她跟老明說：

> 「老闆，我以前下班才能寫完郵件。**現在我可以準時 5 點下班接小孩**。」

老明那天晚上失眠 — 不是因為焦慮，是因為意識到：**這不是省時間，是員工的人生變了**。

#### L1 Gate Acceptance（Month 6 末）

雙雷達對比：

```
Month 0：                Month 6：
L1 = 0                  L1 = 4 ●（700 帳號 + 92% Policy 簽署）
L2 = 0                  L2 = 2 ●（5 個 Skill 上線）
L3 = 部分               L3 = 部分（無變化，預期）
L4 = 0                  L4 = 0
L5 = 0                  L5 = 0
APQC 11.x = 0           APQC 11.x = 2 ●（Skill 開始累積）
```

**雷達真的變圓了**。老明在 L1 Gate Party 上眼眶濕了：

> 「**這是我這輩子第一次，看見『我的公司』在客觀、量化、結構上變好**。」

線長老陳站起來說：

> 「我以前以為 AI 會搶我的工作。**現在我每天用 AI 寫工作日誌。我 25 年的經驗 — 第一次有人在意到願意把它記下來**。」

### Phase 2 (Month 6-15) Optimization

進度：
- Month 7-9：n8n 平台部署 + 訓練（延長 3 個月為 IT 留消化空間）
- Month 10：第一條投訴自動分類 Workflow 上線
- Month 11-12：sales 提案 Workflow + 月末異常 Workflow
- Month 13-14：QC 異常 Workflow + HR 履歷篩選 Workflow
- Month 15：**L2/L3 Gate Acceptance**

#### L2/L3 Gate Acceptance（Month 15 末）

關鍵 KPI：

| 指標 | Month 0 | Month 15 | 改善 |
| --- | --- | --- | --- |
| 投訴回應時間 | 5 天 | **1.5 天** | -70% |
| 提案週轉時間 | 4 天 | **1.5 天** | -62% |
| Skill Library | 0 | **18 個**（超標 15）| - |
| n8n Workflow | 0 | **5 條**上線 | - |
| Reviewer 簽核率 | - | **96%** | - |
| **APQC 4.0 Deliver** | 1 | **3** | +2 |
| **APQC 11.x** | 2 | **3** | +1 |
| **Tiger AI L3** | 0 | **2** | +2 |

**Month 9**：客戶 A 採購總監主動寄信：「明昌最近回應變快很多，下季訂單**回升 +12%**。」

老明把這封信印出來，貼在會議室牆上。

### Phase 3 (Month 15-24) Excellence

進度：
- Month 16-20：Hermes Agent 開發（製程異常摘要 Agent）
- Month 21：Hermes Agent 通過 4A-4E 驗收
- Month 22-23：ClawTeam 跨部門演練（Sales + CS + QC 3 部門 Agent 協作回應客戶 A 特殊需求）
- Month 24：**L4/L5 Gate Acceptance**

#### L4/L5 Gate Acceptance（Month 24 末）

最終雷達：

```
Month 0：                Month 24：
L1 = 0                  L1 = 4 ●
L2 = 0                  L2 = 3 ●
L3 = 部分               L3 = 3 ●
L4 = 0                  L4 = 3 ●
L5 = 0                  L5 = 2 ●
APQC 11.x = 0           APQC 11.x = 4 ●
SCOR Make = 1           SCOR Make = 3 ●
```

**雷達從鋸齒線變成接近正圓**。

24 個月終端 KPI：

| 指標 | Month 0 | Month 24 | 改善 |
| --- | --- | --- | --- |
| 投訴回應 | 5 天 | **50 分鐘** | -99% |
| 不良率 | 3.2% | **2.0%** | -37% |
| 客戶 A 訂單變化 | -18% | **+22%** | - |
| 員工 AI 使用率 | 0% | **89%** | - |
| Skill Library | 0 | **45 個** | - |
| n8n Workflow | 0 | **12 條** | - |
| Hermes Agent | 0 | **1 個**（通過 4A-4E）| - |

### Gate C 季度回頭看：每季都會做的事

每一季（每 3 個月）必做：

1. **Stage Gate Acceptance**：依 Tool 6.2 checklist 一條條打勾
2. **雷達 Revisit**：把 Stage 2 雷達重畫一次，跟上一季對比
3. **Value Tracking 5 維度**：Time / Quality / Scale / Risk / Assets 5 維度數據對比
4. **客戶決定**：要繼續、要調整、還是要暫停？

> **這就是「科學的閉環」**：不是「PoC 做完就成功」，而是「**結構真的變圓了嗎？**」可以被量化、可以被外部稽核、可以被歷史驗證。

---

## 6. 8 步顧問手法的整體價值

24 個月後，老明在公司年會上致詞：

> 「我們花了 NT$ 980 萬（Phase A 80 + Phase B 200 + Phase C 700）。
>
> 但這 24 個月最有價值的不是省下的錢，而是**整家公司現在說同一套語言**：
>
> - 我們不再爭論『誰的做法對』，而是爭論『哪個改變提升了哪個 APQC 類別』
> - 我們不再說『AI 會搶工作』，而是說『AI 讓我們做更重要的事』
> - 我們不再依賴顧問判斷，而是依賴**自己簽署的目標**
>
> **這就是科學管理**。我女兒在台大資管系說，這是 Rosemann BPM 學派 + Max Weber 的科學管理在現代的落地。」

副董事長問：「下一步呢？」

老明：「我要把我們的轉型故事**捐給 Tiger AI 開源案例庫**。**讓每一家中型製造業都有同一套方法論可以走**。」

---

## 7. 客戶常見問題 Q&A

### Q1：為什麼是 3 個 Phase？不能一次簽 24 個月嗎？

**A**：可以，但**心理門檻太高**。3 個 Phase 讓客戶**用低風險試水溫**，每個 Gate 都是出口。Phase A 80 萬只是 24 個月總預算的 8%，客戶心理上願意「試試看」。

### Q2：為什麼 Phase A 不直接給建議？

**A**：因為**客戶要先看到差距，才會願意接受建議**。如果 Phase A 末就推薦「你應該做 L4」，客戶會反問「你怎麼知道我們需要 L4？」。但如果 Phase A 末只給雷達 + 痛點 + 案例，客戶**自己會問**「下一步該怎麼辦？」 — 那才是顧問該介入的時候。

### Q3：Ideal Practice 為什麼要客戶自己簽？

**A**：因為**簽過的目標不能否認**。如果是顧問寫的目標，客戶在 Stage 4 Gap 出爐時會說「這不是我們要的」。但如果是客戶 7 人**獨立投票 → 集體共識 → 集體 reality check → 3 方簽署**，客戶**不可能否認自己 4 週前剛簽的目標**。

### Q4：為什麼每季要重畫雷達？

**A**：因為**沒有閉環的方法論不是科學**。如果只看「PoC 上線了沒」，那是工程交付；但如果問「**雷達真的變圓了嗎？**」，那才是結構性改善。這也是為什麼這套方法論可以投稿學術期刊 — 因為它**可以被反證**。

### Q5：24 個月後我還需要顧問嗎？

**A**：**不需要**。Phase C 設計目標就是「**24 個月後客戶自主運作**」。所有 Skill / Workflow / Agent / Wiki 都是客戶的資產，**程式碼、Credentials、Audit Log 全部交付**。顧問不持有任何客戶 Asset。

> 真實案例會在 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) 18-24 個月實證研究完成後產生。**目前所有數字都是 AI-Simulated，僅供教學**。

---

## 8. 為什麼這套方法論值 NT$ 980 萬

**Phase A 80 萬**：你拿到「**客觀的差距視覺化** + 員工自己說的痛點 + 同業 Benchmark 材料」。如果你不簽 Phase B，**這份報告也是你的，你可以自己執行**。

**Phase B 200 萬**：你拿到「**3 方簽署的 12 個月目標** + 完整 30-50 頁顧問報告 + 14 章節結構 + 每段都有 Evidence Tag」。如果你不簽 Phase C，**這份報告可以拿去找別家顧問執行**。

**Phase C 700 萬**：24 個月實施。**Quarterly Gate C 每季都可以退場**。你不會被綁定 24 個月，你綁定的是「**每 3 個月一次的選擇權**」。

**總價 980 萬 / 24 個月 = 月均 NT$ 41 萬**。比一個正職顧問的薪資加福利還便宜，但**你拿到的是一整套**：方法論 + 工具庫 + 訓練 + 治理 + 持續驗收 + 雷達閉環。

---

## 9. 與其他文件的關係

| 文件 | 跟本故事的關係 |
| --- | --- |
| [`../00_Overview/CLIENT_JOURNEY_STORY.md`](../00_Overview/CLIENT_JOURNEY_STORY.md) | 阿明 24 個月的個人成長故事（CEO 視角的情感弧）|
| [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) | 3-Phase 契約模型 + 完整流程設計（顧問視角）|
| [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §6 | 8 階段的定義與架構 |
| **本檔（MANUFACTURING_CONSULTING_STORY.md）** | **製造業實戰版：把 8 階段套到一家半導體封測廠的完整故事，每個 Stage 都有日數、工具、輸出** |
| [`CONSULTING_REPORT_TEMPLATE.md`](CONSULTING_REPORT_TEMPLATE.md) | 14 章節報告範本（Phase B 交付物）|
| [`CONSULTING_TOOLKIT_TEMPLATES.md`](CONSULTING_TOOLKIT_TEMPLATES.md) | 完整工具庫（本故事用到的 Tool 1.1 - 8.9 都在這裡）|
| [`REPORT_PRODUCTION_WORKFLOW.md`](REPORT_PRODUCTION_WORKFLOW.md) | 報告 8 步生產工藝（adapted from mckinsey-consultant-skills）|
| [`CONSULTING_FRAMEWORKS_LIBRARY.md`](CONSULTING_FRAMEWORKS_LIBRARY.md) | 50+ 顧問框架庫（本故事用到的 80/20、5 Whys、Issue Tree 都在這裡）|

---

## 10. 結語

如果你是製造業老闆，看完這份故事**你應該能回答**：

- ✅ 我要花多少錢？（NT$ 980 萬 / 24 個月）
- ✅ 我每週會做什麼？（每週日數已標明）
- ✅ 我會拿到什麼？（每個 Phase 的交付物已列）
- ✅ 我什麼時候可以退場？（每季 Gate C）
- ✅ 24 個月後我會變什麼？（最終雷達 + 終端 KPI 已對比）

如果這 5 個問題你都能在這份故事裡找到答案，**那這就是「客戶看得懂的顧問方法論」**。

---

License & Citation

This document is Apache License 2.0; may be used, modified, commercialized, provided the [`../NOTICE`](../NOTICE) attribution is preserved.
