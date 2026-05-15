# 八階段顧問流程：完整情境故事與閉環設計

> 🌐 English version: [EIGHT_STAGE_FLOW_STORY_EN.md](EIGHT_STAGE_FLOW_STORY_EN.md)
>
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技

更新日期：2026-05-15

---

> **本文是什麼**：把八階段顧問方法論寫成一個完整、可重複、可被辯論的閉環故事。從問卷接觸到實施計畫，每一步都有明確的觸發、產出、簽署、與下一步的鎖死關係。
>
> **本文不是什麼**：不是 6 週 marathon 直線敘事。而是**三階段合約模型 + 中期客戶簽署 + 季度回頭核對閉環** 的完整科學管理流程。

---

## 0. 對使用者原始流程的改進建議（3 個更好的設計）

使用者原始流程：
> 問卷 + AI As-Is 實地評估 → 比對 RM 缺什麼 → 拿成熟度 + 業界案例 benchmarking → 評分 → 給客戶看評估報告 → 客戶挑 Ideal Practice → 分析還要做什麼 → TO-BE 建議 → 顧問報告 → Implementation plan

**這是對的方向**。Tiger AI 在此基礎上補 3 個改進：

| # | 改進 | 為什麼這樣設計更強 |
| --- | --- | --- |
| **改進 1** | **拆成 3 階段合約**（Phase A 診斷 / Phase B 策略 / Phase C 落地），不是一個 6 週 marathon | 客戶可低風險先簽 Phase A，看結果決定要不要簽 B、C；顧問也避免一次承諾過多 |
| **改進 2** | **Phase A 結束時，中期評估報告先簽署成 Deliverable**，再啟動 Phase B Ideal Practice 共創 | 客戶被雷達空格震撼後才挑 Ideal，避免空想；中期報告本身也是可單獨交付的成品 |
| **改進 3** | **每季回頭核對 Reference Model 雷達**（從 Phase C 進入 Implementation 後持續）| 不是「做完就好」，而是**結構真的變圓了嗎** —— 這是科學閉環的反證機制 |

> **為什麼比直線 6 週 marathon 強**：直線流程客戶要一次決定 6 週 + 24 個月 commitment，心理門檻太高；3 階段合約讓決策分批、降低風險、提高接受度。

---

## 1. 三階段合約模型總覽

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  Phase A：診斷                Phase B：策略              Phase C：落地     ║
║  Diagnostic                    Strategy                    Implementation   ║
║  ─────────────                ─────────────              ─────────────     ║
║  2 週 · NT$ 80 萬             4 週 · NT$ 200 萬          24 個月 · NT$ 700 萬║
║                                                                             ║
║  Stage 1 + 2 + 3 素材         Stage 3 Ideal Practice     Stage 7 + 8 落地 ║
║                                + Stage 4 + 5                                ║
║                                                            （每季回頭核對   ║
║                                                              Stage 2 雷達）║
║                                                                             ║
║  Deliverable：                Deliverable：               Deliverable：    ║
║  中期評估報告                  完整顧問診斷報告            轉型路徑圖 +     ║
║  （客戶簽收）                  + Ideal Practice 定義表    變革管理 +       ║
║                                （三方簽名）                價值追蹤 +       ║
║                                                            季度回顧紀錄    ║
╚═══════════════════════════════════════════════════════════════════════════╝
                ↑                       ↑                       ↑
            Gate A                   Gate B                  Gate C
        客戶決定要不要         客戶決定要不要              客戶決定每季
        進 Phase B             進 Phase C                  要不要繼續
```

**設計的科學意義**：每個 Gate 都是「客戶可下車的退場點」 —— 顧問**有信心**才敢這樣設計，因為前一階段的 deliverable 必須**好到客戶想繼續**。

---

## 2. 主角介紹：客戶 M 公司

> ⚠️ **「客戶 M / 明強封測」為 AI 模擬產生的虛構公司**，並非真實客戶。所有規模、KPI、預算、時程數字皆為**示例**，僅供方法論教學用。詳見 [`../04_Scenarios/README.md`](../04_Scenarios/README.md) 學術誠信聲明。

- **產業**：半導體封測（FATP）
- **規模**：700 人，年營收 NT$ 12 億
- **觸發事件**：三家直接競爭對手導入 AI 質檢與客訴 Agent，客戶 A 季訂單下降 18%
- **痛點**：客訴回應 5 天（業界 1 天）、業務提案 4 天（業界 1.5 天）、不良率 3.2%（業界 1.8%）
- **限制**：預算上限 NT$ 800 萬、製程資料須地端、IT 2 FTE 不可再增
- **角色**：CEO（Sponsor）、COO、IT 副理（潛在 AI Champion）、品保長、業務長、客服長、HR、法遵

---

## 3. Phase A：診斷（2 週，NT$ 80 萬）

### 觸發

M 公司 CEO 收到 Tiger AI 的 outreach email + 看到 GitHub 開源方法論 repo，請祕書約 30 分鐘 intro。

### Pre-Engagement：10 題快速問卷（隔週寄）

CEO 自己填 [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) 的 10 題版（5 分鐘）。

**自動評分結果**：

```
六維雷達：
  工具使用    1 / 4 （部分主管私下用 ChatGPT）
  知識沉澱    0 / 4 （無 Wiki、無 SOP）
  流程自動化  1 / 4 （財務 1 個 Power Automate）
  系統整合    2 / 4 （ERP/CRM 各自孤島）
  Agent 應用  0 / 4 （無）
  治理 ROI    1 / 4 （無 AI 政策）
總分：5 / 24 → 初判 L1
```

CEO 看到雷達圖 → **第一次震撼** → 同意簽 Phase A 診斷合約。

### Phase A 流程（Week 1-2）

#### Week 1 ── Stage 1 As-Is Snapshot：先聽、先看、不評論

| Day | 動作 | 對應工具 | 產出 |
| --- | --- | --- | --- |
| Day 1-2 | 高管訪談（CEO/COO/CIO 各 60 分）+ 部門長訪談（品保/業務/客服/IT/HR 各 90 分）| Tool 1.1 訪談題庫 40 題 | 訪談錄音 + 摘要 |
| Day 3 | 操作員訪談（產線/業務/客服各 3 位 × 30 分）| Tool 1.1 C 段 | 訪談摘要 |
| Day 4 | AI Usage Inventory + Systems Inventory | Tool 1.2 + 1.3 | 影子 IT 風險地圖 + 系統地圖 |
| Day 5 | 3 條關鍵 process 的 walkthrough + 畫 Swimlane | Tool 1.4 | 3 張 As-Is Process Map |

**Week 1 結尾**：顧問跟客戶說「現在我們知道你公司在做什麼了」。**不評論、不建議**。

#### Week 2 ── Stage 2 Reference Model Alignment + Stage 3 素材準備

| Day | 動作 | 對應工具 | 產出 |
| --- | --- | --- | --- |
| Day 6 | 選 Reference Model：SCOR + APQC + Tiger AI L1-L5 | Tool 2.1 | RM 選用理由文件 |
| Day 7-8 | Mapping Worksheet：把 As-Is 落點到 RM 格子 | Tool 2.2 | Mapping 結果表 |
| Day 9 | 標準能力缺口檢核 + 雙雷達圖 | Tool 2.3 + 2.4 | 兩張雷達（APQC + Tiger AI） |
| Day 10 | 對標案例準備（從 5 個 Benchmark Stub 挑出半導體業 + 另找 2 家同業） | Tool 3.1 + 3.3 | 3 份 Best-Practice Profile |

> **Phase A 紀律**：Day 10 顧問**還不做 Ideal Practice 共創**。先把素材備齊，下一階段才用。

### Phase A Deliverable：中期評估報告（客戶簽收）

**Day 11-12 寫報告 → Day 13-14 客戶 review → Day 14 結案會議**

中期評估報告（10-15 頁）章節：

1. **執行摘要**：「依國際標準，您公司目前在 SCOR Make/Deliver、APQC 11.x Knowledge、Tiger AI L1-L3 這 3 個 Category 呈現結構性缺口」
2. **As-Is Snapshot**：訪談摘要 + 系統地圖 + 3 張 Swimlane
3. **Reference Model Mapping**：標準能力缺口檢核表
4. **雙雷達圖**：APQC + Tiger AI L1-L5（虛線=產業標竿、實線=本公司）
5. **產業最佳實務素材**：3 家同業案例 Benchmark Profile（先列素材，**不下結論**）
6. **下一階段建議**：Phase B Ideal Practice 共創 Workshop（半天）+ Stage 4-5 分析

### Gate A：客戶決定要不要進 Phase B

**結案會議發生什麼**：

- CEO 看到雷達圖：「我以為我們不算差，原來在標準下我們這幾格是 0 分？」 → **第二次震撼**
- COO 翻到 Swimlane：「客訴流程真的這麼破洞...」 → 痛點具體化
- IT 副理看到影子 IT 月支出：「私人 ChatGPT 月燒 24,000 元而且資料在飛...」 → 風險具象化

**90% 客戶會簽 Phase B**。因為：

- 雷達空格不是顧問說，是國際標準說 → **客觀**
- 痛點是訪談錄音裡員工說的 → **可驗證**
- 同業已經做到的 → **可達**

> **Phase A 設計目的就是這個震撼**：客戶**自己看到差距**，而不是顧問告訴他差距。

---

## 4. Phase B：策略（4 週，NT$ 200 萬）

### Week 3 ── Stage 3 Ideal Practice 共創 Workshop（半天）

**Day 15 上午** ─ Tool 3.6 共創 Workshop

| Step | 動作 | 時間 | 產出 |
| --- | --- | --- | --- |
| 1. 素材展示 | 顧問**只展示、不推薦** Tool 3.1/3.3/3.4/2.7 4 層架構圖 | 30 min | 共識素材 |
| 2. 獨立投票 | 每人**獨立**在便利貼寫「12 個月後想成為什麼」 | 45 min | N 張便利貼 |
| 3. 集體共識 | 貼到 4 層架構圖，找共識/分歧 | 60 min | v1 Ideal Practice 草稿 |
| 4. Reality check | 顧問首次主動介入用 Tool 6.3 反問可行性 | 45 min | v2 Ideal Practice |
| 5. 寫定義表 | 把 v2 落定為「Ideal Practice 定義表」| 30 min | 簽署版定義表 |
| 6. **三方簽名** | CEO + Sponsor + AI Champion | 15 min | 公開可審核文件 |

**M 公司簽出的 Ideal Practice 定義表（節錄）**：

| # | 能力 | RM Category | 12 個月後想到的程度 | 證據條件 |
| --- | --- | --- | --- | --- |
| 1 | 客訴回應 | APQC 4.4 + Tiger AI L3 | 90% 1hr 分流 + 24hr 人工回 | n8n + Reviewer 簽核率 ≥ 95% |
| 2 | 知識沉澱 | APQC 11.x + Tiger AI L2 | 每月 ≥ 20 條 Skill 入庫 | Skill Library Git + Owner + IPOE |
| 3 | 製程根因 | SCOR Make + Tiger AI L4 | 異常 → 假設 ≤ 1hr | Hermes Agent + 5 任務 Reviewer 通過 |

> **這張表就是整個顧問案的 anchor**。後續 Stage 4-8 全部基於這張表計算，客戶無法否認自己當初簽的目標。

### Week 3-4 ── Stage 4 Gap Analysis + Stage 5 Problem Definition

#### Stage 4：差距 = (客戶 Ideal − 客戶 As-Is)

| Day | 動作 | 對應工具 | 產出 |
| --- | --- | --- | --- |
| Day 16-17 | M/B/R 三類分 + Impact × Effort | Tool 4.1 + 4.2 | 差距矩陣 |
| Day 18 | Prioritization Worksheet | Tool 4.3 | 優先級排序 |

**M 公司差距矩陣（節錄）**：

- 🔴 Missing: 知識管理（M 公司：0；Ideal：每月 20 條）→ Impact 5、Effort 2
- 🟡 Broken: 報價系統（M 公司：人工 copy-paste；Ideal：4hr 出報價）→ Impact 5、Effort 4
- 🔴 Missing: AI 治理（M 公司：無；Ideal：完整 Audit + ROI）→ Impact 4、Effort 1
- 🔵 Redundant: 工單三套（M 公司：Notion + Trello + Email；Ideal：統一）→ Impact 3、Effort 1

#### Stage 5：80/20 收斂找真因

| Day | 動作 | 對應工具 | 產出 |
| --- | --- | --- | --- |
| Day 19 | 80/20 收斂 + 5 Whys | Tool 5.1 + 5.2 | 核心病灶清單 |
| Day 20-21 | Executive Problem Statement | Tool 5.3 + 5.4 | 一句話定義核心問題 |

**M 公司 Executive Problem Statement**：

> M 公司沒有「知識資產化」的角色、工具與誘因，80% 的差距（客訴慢/報價慢/知識無沉澱/製程慢）都源於同樣的事重複做、無人沉澱、無人重用。

### Week 4 ── Stage 6 Phased Goals + Stage 7 To-Be Design

#### Stage 6：把 Ideal 拆成組織吃得下的台階

| Day | 動作 | 對應工具 | 產出 |
| --- | --- | --- | --- |
| Day 22 | 終極 Ideal → Phase 1/2/3 拆解 | Tool 6.1 | 拆解表 |
| Day 23 | 組織吸收力評估（6 維度） | Tool 6.3 | 吸收力評分 |
| Day 24 | Stage Gate Criteria | Tool 6.2 | L1-L5 各 Gate 驗收清單 |

> **M 公司吸收力評估發現 IT 只有 2 FTE，Phase 2 需要 0.5 加人**。決定：拉長 Phase 2 由 6 月 → 9 月。**這個調整來自客戶自己看資料，不是顧問建議**。

#### Stage 7：每 Phase 一張 To-Be Operating Model

| Day | 動作 | 對應工具 | 產出 |
| --- | --- | --- | --- |
| Day 25-26 | 分階段 To-Be Operating Model（3 張）| Tool 7.1 | 3 張 To-Be 圖 |
| Day 27 | 人機協作架構 + HITL 節點 | Tool 7.2 | 每 process 的人機分工 |
| Day 28 | Skill/Workflow/Agent Map + 整合架構 | Tool 7.3-7.6 | 3 張地圖 + 部署模式（Variant B Hybrid） |

### Phase B Deliverable：完整顧問診斷報告 + Ideal Practice 定義表

**Day 29-30 寫報告 → Day 31-32 客戶 review → Day 32 結案會議**

完整顧問診斷報告（30-50 頁）章節：依 [`CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md) 14 章結構：

1. Executive Summary
2. Methodology
3. As-Is Snapshot（接 Phase A）
4. Reference Model Alignment（接 Phase A）
5. **Best Practice Integration + Ideal Practice 定義表（三方簽名版）**
6. Gap Analysis
7. Executive Problem Statement
8. Benchmarking & Phased Goals
9. To-Be Design
10-13. （Phase C 內容暫列骨架）

### Gate B：客戶決定要不要進 Phase C

**95% 客戶會簽 Phase C**。因為：

- Ideal Practice 是**他們自己簽的** → 無法否認
- Gap 是減法算出來的 → **可被驗證**
- Phase 1/2/3 拆解符合組織吸收力 → **可達**

---

## 5. Phase C：落地（24 個月，NT$ 700 萬）

### Stage 8 Implementation & Change

**首月（Month 1）**

| Day | 動作 | 對應工具 | 產出 |
| --- | --- | --- | --- |
| Day 33 | Transformation Roadmap（24 個月 6 季）| Tool 8.1 | Roadmap |
| Day 34 | 變革管理計畫 + 抗拒處理 Playbook | Tool 8.2 | 變革計畫 |
| Day 35 | RACI + Permission Matrix + Audit Log | Tool 8.3 + 8.4 + 8.7 | 治理文件 |
| Day 36 | 價值追蹤矩陣（5 維度）| Tool 8.5 | 追蹤儀表板規格 |
| Day 37 | Risk Register（含案例 Failures 轉換）| Tool 8.6 | 風險登錄表 |
| Day 38 | AI Ethics Checklist | Tool 8.8 | Ethics 簽署版 |
| Day 39 | SOW + Phase 1 啟動會議 | — | Phase 1 啟動 |

### Phase 1（Month 1-6）：基礎穩固期

- L1 全員 OpenWebUI 上線
- 5 個核心 Skill 上架
- AI 政策簽署率 > 90%
- Prompt Library ≥ 30 條

**Month 6 結尾 → L1 Gate 驗收 + 回頭核對 Stage 2 雷達**：

```
APQC 11.x Knowledge：0 → 2 （Skill 入庫起步）
Tiger AI L1：          0 → 4 （全員 OpenWebUI + 規範 92%）
Tiger AI L2：          0 → 2 （5 條 Skill）
```

> 雷達**真的更圓了**。客戶看了想哭：「原來這就是科學管理。」

### Phase 2（Month 6-15）：效能優化期

- L2 Skill Library ≥ 15 條
- L3 n8n Workflow 上線 ≥ 3 個
- HITL 節點全部就位

**Month 15 結尾 → L2/L3 Gate + 雷達回看**：

```
APQC 4.0 Deliver：1 → 3 （客訴回應 5 天 → 1 天）✓ Ideal 達成
APQC 11.x：       2 → 3 （知識沉澱穩定）✓ Ideal 達成
Tiger AI L3：     0 → 2 （n8n PoC 上線）
```

### Phase 3（Month 15-24）：標竿卓越期

- L4 Hermes Agent 通過 4A-4E
- L5 ClawTeam 跨部門 1 次成功演練

**Month 24 結尾 → L4/L5 Gate + 雷達最終核對**：

```
SCOR Make + Tiger AI L4：0 → 3 （Hermes Agent 通過）✓ Ideal 達成
Tiger AI L5：             0 → 2 （ClawTeam 跨部門演練）
```

### Gate C 季度：每季客戶可決定要不要繼續

每季結尾**必做**：

1. 該季 Gate 驗收（依 Tool 6.2 清單）
2. 回頭核對 Stage 2 雷達（量化進步幅度）
3. 價值追蹤矩陣 5 維度 review
4. 客戶決定下一季要繼續推進、調整、或暫停

> 24 個月後，M 公司客訴回應 1 天、不良率 2.0%、流失客戶歸零、Stage 2 雷達**從一條凹凸線變成接近圓**。

---

## 6. 完整閉環圖：八階段 + 三階段合約 + 季度回顧

```
                          ┌──────────────────┐
                    ┌────►│ Phase A 診斷 2W   │
                    │     │ Stage 1 + 2 + 3   │
                    │     │   素材準備        │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ 中期評估報告      │ ← Phase A Deliverable
                    │     │ （客戶簽收）      │
                    │     └────────┬─────────┘
                    │              │
                    │            Gate A
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase B 策略 4W   │
                    │     │ Stage 3 Ideal     │
                    │     │ + Stage 4 + 5     │
                    │     │ + Stage 6 + 7     │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ 完整顧問報告      │ ← Phase B Deliverable
                    │     │ + Ideal Practice  │
                    │     │   定義表（簽名） │
                    │     └────────┬─────────┘
                    │              │
                    │            Gate B
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase C 落地 24M  │
                    │     │ Stage 8           │
                    │     │ Transformation +  │
                    │     │ 變革 + 價值追蹤   │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase 1/2/3       │
                    │     │ Stage Gate 驗收   │
                    │     └────────┬─────────┘
                    │              │
                    │      每季 Gate C
                    │              │
                    │     ┌────────▼─────────┐
                    └─────┤ 回頭核對         │
                          │ Stage 2 雷達      │
                          │ （結構是否更圓） │
                          └──────────────────┘
                                  
                          這條回饋線就是
                          「科學管理閉環」
                          的核心反證機制
```

---

## 7. 為什麼這個流程經得起客戶辯論

對每個可能的質詢，本流程的回應位置：

| 質詢 | 回應位置 | 證據 |
| --- | --- | --- |
| 「你怎麼知道我們在 L1？」 | Phase A 中期報告 §2 雷達 | 10 題問卷 + 訪談錄音 + 系統盤點 |
| 「為什麼這幾格是 0 分？」 | Phase A §3 RM Mapping | APQC / Tiger AI 公開標準 |
| 「目標誰訂的？」 | Phase B §5 Ideal Practice 定義表 | **客戶自己簽的，三方簽名** |
| 「為什麼差距這麼大？」 | Phase B §6 Gap Analysis | Gap = (你簽的 Ideal − 你的 As-Is) 算式 |
| 「為什麼先做客服不做業務？」 | Phase B §6.2 | Impact × Effort 矩陣 |
| 「為什麼 24 個月？」 | Phase B §8 + Tool 6.3 | 案例 Benchmark + 組織吸收力評估 |
| 「萬一做不到怎麼辦？」 | Phase C §13 Risk Register | Trigger + Owner + Mitigation |
| 「怎麼證明變好了？」 | 每季 Gate C 回頭核對 | Stage 2 雷達 + 價值追蹤 5 維度 |
| 「下家顧問說我們在 L3，你說 L2，誰對？」 | 公開的 0-4 量尺 + 證據 | 任何第三方可獨立驗證 |

---

## 8. 跟使用者原始流程的對照

| 使用者步驟 | 對應 Phase | 對應 Stage | 改進點 |
| --- | --- | --- | --- |
| 1. 問卷 + AI As-Is 評估 | Phase A W1 | Stage 1 | 加 10 題快篩做為 pre-engagement |
| 2. 比對 RM 缺什麼 | Phase A W2 | Stage 2 | 用 4 層架構 + 雙雷達 |
| 3. 成熟度 + 案例 benchmarking → 評分 | Phase A W2 末 | Stage 3 素材 | 案例必須是 Benchmark-grade（9 欄位） |
| 4. **客戶看評估報告** | **Phase A Deliverable** | — | **新增：中期報告作為獨立 Deliverable + 客戶簽收** |
| 5. 客戶挑 Ideal Practice | Phase B W3 | Stage 3 Tool 3.6 | **客戶自己簽，不是顧問訂** |
| 6. 分析還要做什麼 | Phase B W3-W4 | Stage 4 + 5 | Gap = Ideal − As-Is，80/20 收斂 |
| 7. TO-BE 建議 | Phase B W4 | Stage 6 + 7 | 分階段 + 組織吸收力評估 |
| 8. 顧問報告 | Phase B Deliverable | — | 14 章完整報告 + Ideal Practice 簽名版 |
| 9. Implementation plan | Phase C 啟動 | Stage 8 | 變革管理 + 價值追蹤 + Audit |
| **（缺）** | **季度回顧** | — | **新增：每季回頭核對 Stage 2 雷達（科學閉環）** |

---

## 9. 跟其他文件的關係

| 文件 | 與本文關係 |
| --- | --- |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §6 | 提供八階段的定義與資料流；本文是其完整流程化敘事 |
| [`METHODOLOGY_SCIENTIFIC_LOGIC.md`](METHODOLOGY_SCIENTIFIC_LOGIC.md) | 提供「為什麼這樣設計」的科學論證；本文是「實際怎麼跑」的故事 |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) | 提供每階段的工具表 |
| [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md) | 提供 Phase B Deliverable 的 14 章結構 |
| [`../04_Scenarios/`](../04_Scenarios/) | 提供 Phase A 用的 Benchmark-grade 案例 |
| [`../06_Delivery/ENGAGEMENT_LIFECYCLE.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE.md) | 提供接案 / 計價 / 交付 SOP |

---

## 10. 結語：閉環為什麼是科學

這個流程**不是線性的 marathon**，而是**有反饋的閉環**：

- **每個 Gate 都是客戶可下車的退場點** → 顧問**有信心**才敢這樣設計（前一階段必須好到客戶想繼續）
- **每個 Deliverable 都有客戶簽名** → 後續推理無法被否認
- **每季回頭核對 Stage 2 雷達** → 結構真的變圓才算成功，不是「PoC 做了」就算成功

**這就是科學管理**：

- 起點客觀（國際標準 + 客戶簽名）
- 過程可驗證（每 Stage Gate Criteria）
- 終點可反證（雷達雙圖對比 + 5 維度價值追蹤）

如果哪天有人說「Tiger AI 的方法論不行」，他必須**回去質疑**：

- APQC PCF 不行嗎？
- Rosemann BPM 學派不行嗎？
- 客戶自己簽的 Ideal Practice 不算嗎？
- 我們季度雷達回看那條閉環不算嗎？

**很難**。這就是為什麼我們花這麼多時間設計這套閉環。

---

授權與引用 / License & Citation

本文為 Apache License 2.0；可使用、修改、商業利用，唯需保留 [`../NOTICE`](../NOTICE) 檔之署名。
