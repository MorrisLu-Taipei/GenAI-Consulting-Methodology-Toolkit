# AI 轉型診斷報告模板 / AI Transformation Diagnostic Report Template

更新日期：2026-05-15（八階段對齊圖卡 / Aligned to canonical eight-stage methodology）

> 本模板對齊**企業管理顧問方法論：八階段轉型指南**（Rosemann BPM 學派 + Tiger AI L1-L5）。每章節對應 [`CONSULTING_TOOLKIT_TEMPLATES.md`](CONSULTING_TOOLKIT_TEMPLATES.md) 的對應 Stage 工具。

---

## 封面 / Cover

報告名稱：企業 AI 轉型成熟度診斷報告
客戶名稱：`[客戶公司]`
診斷期間：`[YYYY/MM/DD - YYYY/MM/DD]`
顧問團隊：虎智科技 Tiger AI
方法論：GenAI Consulting Methodology Toolkit · Eight-Stage Transformation Guide
版本：v2.0（八階段對齊版）

---

## 1. Executive Summary / 執行摘要

### 1.1 核心結論

`[用 3-5 點寫給老闆看的結論。避免技術細節，聚焦：標準缺口、卓越距離、核心問題、階段路徑、變革風險。]`

範例：

- 依 APQC PCF + Tiger AI L1-L5 雙座標，公司在「知識管理 (APQC 11.x)」與「Workflow 自動化 (Tiger AI L3)」呈現結構性缺口。
- 對照產業卓越案例，公司客服回應、報價產出、知識沉澱距標竿尚有 3-5 倍效率落差。
- 核心問題不是工具不足，而是「**沒有知識資產化的角色、工具與誘因**」—— 80% 的差距均源於此。
- 建議分三階段（基礎穩固 6m / 效能優化 6m / 標竿卓越 12m）推進，避免一次到位失敗。
- 部署模式建議 Hybrid，低敏感任務走雲、核心 ERP 與客戶資料留在受控環境。

### 1.2 成熟度與標準缺口總覽

| 項目 | 結果 |
| --- | --- |
| 採用 Reference Model | `[APQC PCF / SCOR / eTOM / ITIL]` + Tiger AI L1-L5 |
| 標準完整度（產業 RM） | `[X / 4，含 N 個 Missing Category]` |
| AI 採用成熟度（Tiger AI） | `[L1 / L2 / L3 / L4 / L5]` |
| 局部成熟度 | `[例如客服 L3、行銷 L2]` |
| 與產業標竿距離 | `[3-5 倍效率落差 / 接近]` |
| 建議部署模式 | `[雲 AI / Hybrid / 全地端]` |
| 優先導入部門 | `[部門]` |
| 優先 PoC | `[場景]` |
| 建議課程比例 | `[L1 x%、L2 x%、L3 x%、L4 x%、L5 x%]` |

---

## 2. 診斷方法 / Methodology

本報告依**八階段顧問方法論**（Rosemann BPM 學派 + Tiger AI L1-L5）產出：

| Stage | 名稱 | 本報告對應章節 |
| --- | --- | --- |
| 1 | As-Is Snapshot 現況掌握 | §3 |
| 2 | Reference Model Alignment 標準模型引入 | §4 |
| 3 | Best Practice Integration 產業最佳實務對標 | §5 |
| 4 | Gap Analysis 差距分析 | §6 |
| 5 | Problem Definition 結論與核心問題定義 | §7 |
| 6 | Benchmarking & Phased Goals 多階段目標設定 | §8 |
| 7 | To-Be Design 未來藍圖設計 | §9 |
| 8 | Implementation & Change 執行導入與變革治理 | §10-§13 |

### 2.1 資料來源

1. AI 成熟度問卷（10 / 25 / 50 題版）。
2. 主管、部門、操作員三層訪談（題庫 40 題）。
3. AI Usage Inventory + Systems Inventory。
4. As-Is Process Map（Swimlane）。
5. Reference Model Mapping Worksheet（APQC / SCOR / Tiger AI L1-L5）。
6. 產業最佳實務檔案（≥ 3 個對標案例）。

### 2.2 使用模型 / Models Used

#### Tiger AI L1-L5（AI 採用軸）

- L1 Controlled AI Access：OpenWebUI。
- L2 Knowledge Codification：Antigravity / Claude Code / Codex。
- L3 Workflow Automation：n8n。
- L4 Autonomous Agent：Hermes Agent。
- L5 Multi-Agent Organization：ClawTeam。

#### 產業 Reference Model（業務結構軸）

- 通用：APQC PCF（13 Categories、1,000+ process）
- 製造 / 供應鏈：SCOR（Plan / Source / Make / Deliver / Return / Enable）
- 電信 / SaaS：eTOM
- IT 服務：ITIL
- 軟體研發：CMMI

> 詳見 [`CONSULTING_TOOLKIT_TEMPLATES.md`](CONSULTING_TOOLKIT_TEMPLATES.md) Tool 2.1 Reference Model 選用指引。

### 2.3 評估構面（六維雷達）

| 構面 | 分數 | 觀察摘要 |
| --- | ---: | --- |
| 工具使用 | `[0-4]` | `[摘要]` |
| 知識沉澱 | `[0-4]` | `[摘要]` |
| 流程自動化 | `[0-4]` | `[摘要]` |
| 系統整合 | `[0-4]` | `[摘要]` |
| Agent 應用 | `[0-4]` | `[摘要]` |
| 治理與 ROI | `[0-4]` | `[摘要]` |

---

## 3. As-Is Snapshot / 現況掌握（Stage 1）

### 3.1 主要訪談發現

| 受訪層級 | 場次 | 關鍵發現 |
| --- | ---: | --- |
| 高層 (CEO/COO/CIO) | `[N]` | `[3-5 點]` |
| 部門主管 | `[N]` | `[3-5 點]` |
| 一線員工 | `[N]` | `[3-5 點]` |

### 3.2 系統盤點摘要

| 系統 | 用途 | API 可用？ | 雲/地端 | 整合潛力 |
| --- | --- | --- | --- | --- |
| Gmail / Email | `[用途]` | `[✓/✗]` | `[雲/地]` | `[高/中/低]` |
| Sheets / Excel | `[用途]` | `[✓/✗]` | `[雲/地]` | `[高/中/低]` |
| CRM | `[用途]` | `[✓/✗]` | `[雲/地]` | `[高/中/低]` |
| ERP | `[用途]` | `[✓/✗]` | `[雲/地]` | `[高/中/低]` |
| Notion / Wiki | `[用途]` | `[✓/✗]` | `[雲/地]` | `[高/中/低]` |
| ... | ... | ... | ... | ... |

### 3.3 影子 IT 風險

`[列出未經許可的 AI 工具使用、私人帳號處理公司資料、月支出總額]`

### 3.4 As-Is Process Maps

附錄 A 提供 ≥ 3 張關鍵流程的 swimlane（含痛點密度標註）。

---

## 4. Reference Model Alignment / 標準模型引入（Stage 2）

> **本章回答**：依國際標準框架，公司營運結構是否完整？哪些 Category 是「標準應有但公司沒有」？

### 4.1 採用 Reference Model

- **產業 Reference Model**：`[APQC PCF / SCOR / eTOM / ITIL]`
- **AI 採用 Reference Model**：Tiger AI L1-L5

### 4.2 Reference Model Mapping 結果

| 標準分類 | 標準應有能力 | 公司現況 | 差距類型 |
| --- | --- | --- | --- |
| `[APQC 4.0 Deliver]` | `[訂單、出貨、客服]` | `[完整/部分/無]` | `[OK / 部分 / Missing]` |
| `[APQC 11.0 Knowledge]` | `[知識管理、Skill Library]` | `[完整/部分/無]` | `[OK / 部分 / Missing]` |
| `[Tiger AI L1]` | `[全員 Chat AI 入口]` | `[完整/部分/無]` | `[OK / 部分 / Missing]` |
| `[Tiger AI L3]` | `[Workflow 自動化]` | `[完整/部分/無]` | `[OK / 部分 / Missing]` |
| ... | ... | ... | ... |

### 4.3 標準完整度雷達

`[插入兩張雷達圖：產業 RM Categories + Tiger AI L1-L5；雙線 = 公司現況 vs 標準完整度]`

### 4.4 結構性缺口清單

| 缺口 | 對應 Reference Model | 嚴重度 1-5 |
| --- | --- | --- |
| `[缺口 1]` | `[Category]` | `[N]` |
| `[缺口 2]` | `[Category]` | `[N]` |
| ... | ... | ... |

> **紀律**：本章只回答「結構是否完整」，不回答「為什麼」（§7）、「該做什麼」（§8-§9）。

---

## 5. Best Practice Integration / 產業最佳實務對標（Stage 3）

> **本章回答**：產業 Best Practice 是**素材**；客戶 Ideal Practice 才是**目標**。本章把產業領先模式作為輸入，協助客戶**自己展開出他想成為的樣子**，並以三方簽名形式鎖住目標。
>
> ⚠️ **關鍵設計**：§5.4 Ideal Practice 定義表 = **整個顧問案的 anchor**。後續 §6-§13 的所有推理都基於此表。客戶簽署後**無法否認自己當初挑的目標**。

### 5.1 對標案例摘要

| 對標公司 | 產業 | 規模 | L 級起點→現況 | 月數 | 借鏡重點 |
| --- | --- | --- | --- | --- | --- |
| `[公司 A]` | `[產業]` | `[人數]` | `[Lx → Ly]` | `[N]` | `[3 點]` |
| `[公司 B]` | `[產業]` | `[人數]` | `[Lx → Ly]` | `[N]` | `[3 點]` |
| `[公司 C]` | `[產業]` | `[人數]` | `[Lx → Ly]` | `[N]` | `[3 點]` |

### 5.2 卓越能力特徵（本公司對標版）

| 能力領域 | 卓越特徵（具體可量化） | 領先案例佐證 | 本公司 vs 卓越距離 |
| --- | --- | --- | --- |
| 客服回應 | `[90% 客訴 1hr 分流 + 24hr 回覆]` | `[公司 A]` | `[5 days vs 1 day]` |
| 報價產出 | `[詢價 → 報價 ≤ 4hr]` | `[公司 B]` | `[4 days vs 4hr]` |
| 知識沉澱 | `[每月 ≥ 30 條 Skill 入庫]` | `[公司 C]` | `[0 vs 30/月]` |
| ... | ... | ... | ... |

### 5.3 L1-L5 卓越在本公司應該長什麼樣

| Level | 對本公司而言的「卓越」 |
| --- | --- |
| L1 Controlled AI Access | `[依公司規模具體化]` |
| L2 Knowledge Codification | `[依公司部門結構具體化]` |
| L3 Workflow Automation | `[依公司系統地圖具體化]` |
| L4 Autonomous Agent | `[依公司業務模式具體化]` |
| L5 Multi-Agent Organization | `[依公司跨部門協作模式具體化]` |

### 5.4 客戶 Ideal Practice 定義表（**三方簽署版**）

> 本表在 Tool 3.6 共創 Workshop 結尾產出，由 CEO + Sponsor + AI Champion 三方簽名。**這是整個顧問案的 anchor**。

| # | 能力領域 | 對應 RM Category（Stage 2）| 客戶 Ideal Practice<br/>（具體可量化）| 12 個月後目標 L 級 | 證據條件（達成的觀察標準）| 對應 Stage 4 算 Gap |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `[客訴回應]` | `[APQC 4.4 + Tiger AI L3]` | `[90% 1hr 分流 + 24hr 人工回]` | `[L3 = 3]` | `[n8n + Reviewer 簽核率 ≥ 95%]` | `[Gap = 5 天 → 1 天]` |
| 2 | `[知識沉澱]` | `[APQC 11.x + Tiger AI L2]` | `[每月 ≥ 20 條 Skill 入庫]` | `[L2 = 3]` | `[Git + Owner + IPOE]` | `[Gap = 0 → 20/月]` |
| 3 | `[製程根因]` | `[SCOR Make + Tiger AI L4]` | `[異常→假設 ≤ 1hr]` | `[L4 = 2]` | `[Hermes Agent + 5 任務 Reviewer 通過]` | `[Gap = 3 天 → 1hr]` |
| ... | ... | ... | ... | ... | ... | ... |

#### Workshop 共識來源

- ☑ Step 1 素材展示（產業 Best Practice + 4 層架構）
- ☑ Step 2 獨立投票（避免高管定錨）
- ☑ Step 3 集體共識化
- ☑ Step 4 組織吸收力 Reality Check（依 §8.3）
- ☑ Step 5 寫成上表

#### 三方簽署 / Three-Party Signature

| 簽署人 | 角色 | 姓名 | 簽署 | 日期 |
| --- | --- | --- | --- | --- |
| Sponsor | `[CEO / 董事長 / 總經理]` | `[___________]` | _____________ | YYYY/MM/DD |
| AI Champion | `[負責推動的高管]` | `[___________]` | _____________ | YYYY/MM/DD |
| 顧問代表 | `[Tiger AI 首席顧問]` | `[___________]` | _____________ | YYYY/MM/DD |

> **本表簽署後生效**。後續任何修改須**三方共同重簽**並版本控制（v1 / v2 ...）。每次修改記錄變更原因，作為 §8 Risk Register 的 trigger 來源。

---

## 6. Gap Analysis / 差距分析（Stage 4）

> **本章回答**：對比 Stage 2 標準 + Stage 3 卓越，公司差什麼？差多少？
>
> ⚠️ **紀律**：本章是**客觀差距盤點**，**不是風險評估**。風險屬於 §13 的 Risk Register。

### 6.1 Missing / Broken / Redundant 表

| 領域 | 類型 (M/B/R) | 描述 | 對應 Reference Model | 對應卓越特徵 | 嚴重 1-5 | 擁有者 |
| --- | --- | --- | --- | --- | --- | --- |
| `[領域]` | `[M/B/R]` | `[描述]` | `[Category]` | `[卓越特徵]` | `[N]` | `[Owner]` |
| ... | ... | ... | ... | ... | ... | ... |

### 6.2 Impact × Effort 矩陣

| 場景 | Impact (1-5) | Effort (1-5) | Strategic Fit (1-5) | Score = (I × SF) / E | 排名 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `[場景 1]` | `[N]` | `[N]` | `[N]` | `[N]` | `[N]` |
| `[場景 2]` | `[N]` | `[N]` | `[N]` | `[N]` | `[N]` |
| ... | ... | ... | ... | ... | ... |

### 6.3 差距分布觀察

`[依 M/B/R 三類分布、依部門分布、依 Reference Model Category 分布的觀察]`

---

## 7. Executive Problem Statement / 結論與核心問題定義（Stage 5）

> **本章回答**：用 80/20 原則收斂，公司「真正要解決」的核心問題是什麼？

### 7.1 80/20 收斂結果

`[從 §6 一堆差距中，找出影響面積最大的 3-5 個核心病灶，再追 5 Whys 找真因]`

### 7.2 高階問題定義聲明

```
CONTEXT / 情境
[過去 12 個月發生了什麼讓 AI 變成優先議題？]

TENSION / 張力
[目前的「現實」與「期望」差距是什麼？引用 §5 卓越特徵具體量化。]

COST OF INACTION / 不行動的代價
[不做 AI 12 個月後會發生什麼？金額？]

DESIRED FUTURE / 期望未來
[12 個月後成功長什麼樣？三個可量化指標，對齊 §5 卓越特徵。]

CONSTRAINTS / 限制條件
[預算？人力？合規？時程？哪些選項已被排除？]
```

### 7.3 核心問題（一句話）

> `[一句話定義核心問題。範例：公司目前 AI 使用已具備個人效率基礎，但缺少部門 Skill 沉澱、跨系統 Workflow 與治理機制，導致 AI 成果難以複製、難以衡量，也難以支撐管理層決策。]`

### 7.4 真因清單

- `[根因 1]`
- `[根因 2]`
- `[根因 3]`

---

## 8. Benchmarking & Phased Goals / 標竿對照與多階段目標設定（Stage 6）

> **本章回答**：把 §5 卓越拆成「組織可吸收」的 3-4 段台階，每段定義驗收標準。

### 8.1 終極標竿 → 階段性目標拆解

| 能力領域 | 終極標竿（§5 卓越特徵） | Phase 1：基礎穩固期 (0-6m) | Phase 2：效能優化期 (6-12m) | Phase 3：標竿卓越期 (12-24m) |
| --- | --- | --- | --- | --- |
| `[領域 1]` | `[卓越特徵]` | `[Phase 1 目標]` | `[Phase 2 目標]` | `[Phase 3 目標]` |
| `[領域 2]` | `[卓越特徵]` | `[Phase 1 目標]` | `[Phase 2 目標]` | `[Phase 3 目標]` |
| ... | ... | ... | ... | ... |

### 8.2 階段驗收標準（Stage Gate Criteria）

#### Phase 1（基礎穩固期）

- [ ] L1 Gate：`[項目]`
- [ ] HITL 設計確認：`[項目]`
- [ ] `[其他 3-5 項]`

#### Phase 2（效能優化期）

- [ ] L2 Gate：`[項目]`
- [ ] L3 Gate：`[項目]`
- [ ] `[其他 3-5 項]`

#### Phase 3（標竿卓越期）

- [ ] L4 Gate：`[項目]`
- [ ] L5 Gate：`[項目]`
- [ ] `[其他 3-5 項]`

### 8.3 組織吸收力評估

| 維度 | Phase 1 需要 | Phase 2 需要 | Phase 3 需要 | 本公司現況 | 缺口 |
| --- | --- | --- | --- | --- | --- |
| 預算 (年) | `[NT$]` | `[NT$]` | `[NT$]` | `[NT$]` | `[需補]` |
| AI Champion | `[N 位]` | `[N 位]` | `[N 位]` | `[N 位]` | `[需補]` |
| IT FTE | `[N]` | `[N]` | `[N]` | `[N]` | `[需補]` |
| 員工 AI 素養 | `[%]` | `[%]` | `[%]` | `[%]` | `[需補]` |
| 變革容量（同時專案數） | `[N]` | `[N]` | `[N]` | `[N]` | `[需補]` |

> **若吸收力不足**：建議拉長該階段時程，或縮減該階段目標。

---

## 9. To-Be Design / 未來藍圖設計（Stage 7）

> **本章回答**：每個 Phase 的 To-Be Operating Model 長什麼樣？人機怎麼分工？

### 9.1 分階段 To-Be Operating Model

#### Phase 1 To-Be（基礎穩固期）

```
[個人層]   [描述]
[部門層]   [描述]
[流程層]   [描述]
[系統層]   [描述]
[治理層]   [描述]
[人機分工] [%-% 比例]
```

#### Phase 2 To-Be（效能優化期）

```
[同上格式]
```

#### Phase 3 To-Be（標竿卓越期）

```
[同上格式]
```

### 9.2 人機協作架構

| Process | 人的角色 | AI 的角色 | HITL 節點 | 驗收標準 |
| --- | --- | --- | --- | --- |
| `[process 1]` | `[角色]` | `[角色]` | `[節點]` | `[標準]` |
| `[process 2]` | `[角色]` | `[角色]` | `[節點]` | `[標準]` |
| ... | ... | ... | ... | ... |

### 9.3 Skill / Workflow / Agent 地圖

#### Skill Map

| Skill | Owner | Inputs | Outputs | L-level | Status |
| --- | --- | --- | --- | --- | --- |
| `[Skill 1]` | `[Owner]` | `[in]` | `[out]` | `[L]` | `[狀態]` |
| ... | ... | ... | ... | ... | ... |

#### Workflow Map

| Workflow | Trigger | 串接系統 | Output | Owner |
| --- | --- | --- | --- | --- |
| `[Workflow 1]` | `[trigger]` | `[系統]` | `[output]` | `[Owner]` |
| ... | ... | ... | ... | ... |

#### Agent Map

| Agent | Role | Skills used | Reviewer | 階段驗收 |
| --- | --- | --- | --- | --- |
| `[Agent 1]` | `[Role]` | `[Skills]` | `[Reviewer]` | `[Lx ✓/✗]` |
| ... | ... | ... | ... | ... |

### 9.4 整合架構選擇

建議部署模式：`[Variant A 雲 / B Hybrid / C 全地端]`

理由：

- `[理由 1]`
- `[理由 2]`
- `[理由 3]`

---

## 10. Implementation Roadmap / 轉型路徑圖（Stage 8 §1）

| Quarter | Phase | Theme | Deliverables | Owner | 階段驗收 | KPI |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | Phase 1 | `[主題]` | `[deliverables]` | `[owner]` | `[L1 Gate]` | `[KPI]` |
| Q2 | Phase 1→2 | `[主題]` | `[deliverables]` | `[owner]` | `[L2/L3 Gate]` | `[KPI]` |
| Q3 | Phase 2 | `[主題]` | `[deliverables]` | `[owner]` | `[L4 Gate]` | `[KPI]` |
| Q4 | Phase 2→3 | `[主題]` | `[deliverables]` | `[owner]` | `[L4 ext]` | `[KPI]` |
| Q5-Q6 | Phase 3 | `[主題]` | `[deliverables]` | `[owner]` | `[L5 Gate]` | `[KPI]` |

> **每季結尾必做**：回頭核對 §4 Reference Model 雷達 —— 雷達是否更圓？哪些 Category 還是空？

---

## 11. Change Management Plan / 變革管理計畫（Stage 8 §2）

### 11.1 Stakeholder Map + 溝通計畫

| 維度 | Phase 1 | Phase 2 | Phase 3 |
| --- | --- | --- | --- |
| Stakeholder Map | `[Sponsor、Champion、IT、HR]` | `[+ 部門 Lead]` | `[+ 全公司]` |
| 溝通計畫 | `[月會 + 月報]` | `[雙週站會 + 部門報告]` | `[季度大會]` |
| 訓練計畫 | `[L1 全員 + L2 代表]` | `[L2 部門 + L3 IT]` | `[L4-L5 高階]` |
| 早期採用者 | `[5-10 位]` | `[部門全員]` | `[全公司]` |

### 11.2 抗拒處理 Playbook

| 抗拒類型 | 預期人數 | 處理方式 | Owner |
| --- | --- | --- | --- |
| 怕被取代 | `[N]` | 1:1 對話 + 重新定義角色 | HR |
| 不會用 | `[N]` | 1:1 mentor + 簡化第一個成功經驗 | AI Champion |
| 不信任 | `[N]` | 先給「人審」場景累積信任 | 部門 Lead |
| 怕擔責 | `[N]` | HITL 節點明確 + 究責邊界 | Sponsor |

---

## 12. Governance Design / 治理設計（Stage 8 §3）

### 12.1 RACI

| 議題 | Sponsor | AI Champion | IT | 一線 | 資料 Owner |
| --- | --- | --- | --- | --- | --- |
| 願景 / Roadmap | A | R | C | I | I |
| Reference Model 選用 | A | R | C | I | C |
| 工具選型 | A | C | R | C | C |
| 帳號 / 權限 | I | C | R | I | A |
| Skill / Workflow 建置 | I | A | R | R | C |
| 變革管理 | A | R | C | C | I |
| Audit / 治理 | A | C | R | I | R |
| 價值追蹤 / ROI | A | R | C | I | I |

### 12.2 Permission / Governance Matrix

`[參考 CONSULTING_TOOLKIT_TEMPLATES.md Tool 8.4，依本公司角色填寫]`

### 12.3 Audit Log 規格

`[參考 CONSULTING_TOOLKIT_TEMPLATES.md Tool 8.7，依本公司合規要求填寫]`

### 12.4 AI Ethics & Data Policy

`[依 CONSULTING_TOOLKIT_TEMPLATES.md Tool 8.8 的 15 項清單檢核]`

---

## 13. Value Tracking & Risk Register / 價值追蹤與風險登錄（Stage 8 §4）

### 13.1 價值追蹤矩陣（五大維度）

| Initiative | 維度 | Baseline | Target | Period | Owner |
| --- | --- | --- | --- | --- | --- |
| `[Init 1]` | 時間 | `[base]` | `[target]` | `[period]` | `[owner]` |
| `[Init 1]` | 品質 | `[base]` | `[target]` | `[period]` | `[owner]` |
| `[Init 1]` | 規模 | `[base]` | `[target]` | `[period]` | `[owner]` |
| `[Init 1]` | 風險 | `[base]` | `[target]` | `[period]` | `[owner]` |
| `[Init 1]` | 資產 | `[base]` | `[target]` | `[period]` | `[owner]` |
| ... | ... | ... | ... | ... | ... |

#### 五大追蹤維度

1. **時間** — 處理時間縮短
2. **品質** — 錯誤率下降、重工減少
3. **規模** — 受惠人數、處理量
4. **風險** — 漏案、合規違規、機敏外流
5. **資產** — Skill 條數、Wiki 條目、Agent 數

### 13.2 Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner | Trigger |
| --- | --- | --- | --- | --- | --- |
| 員工抗拒 | `[H/M/L]` | `[H/M/L]` | `[策略]` | `[Owner]` | `[trigger]` |
| 機敏外流 | `[H/M/L]` | `[H/M/L]` | `[策略]` | `[Owner]` | `[trigger]` |
| LLM 幻覺 | `[H/M/L]` | `[H/M/L]` | `[策略]` | `[Owner]` | `[trigger]` |
| 預算超支 | `[H/M/L]` | `[H/M/L]` | `[策略]` | `[Owner]` | `[trigger]` |
| AI 廠商失聯 | `[H/M/L]` | `[H/M/L]` | `[策略]` | `[Owner]` | `[trigger]` |
| 階段目標吃不下 | `[H/M/L]` | `[H/M/L]` | `[策略]` | `[Owner]` | `[trigger]` |
| ... | ... | ... | ... | ... | ... |

---

## 14. 後續導入 SOW 建議 / Next-Step SOW Proposal

### 14.1 建議工作包

| 工作包 | 內容 | 交付物 | 對應 Phase |
| --- | --- | --- | --- |
| AI 使用入口建置 | OpenWebUI、帳號、模型、規範 | 入口 + 規範 | Phase 1 |
| Skill Library 建置 | 部門 Skill 設計與模板 | Skill Library | Phase 1-2 |
| n8n Workflow PoC | 高價值流程自動化 | Workflow PoC | Phase 2 |
| Hermes Agent 導入 | Agent 任務設計 | Agent 任務卡 + PoC | Phase 2-3 |
| ClawTeam 設計 | 多 Agent 團隊協作 | Agent Team 藍圖 | Phase 3 |
| 變革管理 | 訓練、抗拒處理、慶祝里程碑 | 變革計畫 + 訓練教材 | Phase 1-3 |
| 治理與價值追蹤 | 權限、Log、階段驗收、KPI | 治理 + 價值儀表板 | Phase 1-3 |

### 14.2 建議下一步

1. 確認 §8 三階段拆解與本公司吸收力評估。
2. 選定第一波 PoC 部門與場景。
3. 指定業務 Owner、IT Owner、變革 Owner、Sponsor。
4. 完成系統與資料權限盤點。
5. 啟動 Phase 1 第一個 4 週 PoC。
6. 進行 L1 Gate 驗收 → 回頭核對 §4 Reference Model 雷達 → 調整 Roadmap。

---

## 附錄 / Appendices

- 附錄 A：As-Is Process Maps（≥ 3 張 swimlane）
- 附錄 B：Reference Model 完整 Mapping Worksheet
- 附錄 C：產業最佳實務檔案（≥ 3 個對標案例）
- 附錄 D：訪談紀錄摘要
- 附錄 E：系統盤點完整表
- 附錄 F：成熟度問卷原始作答
- 附錄 G：價值追蹤矩陣 Baseline 量測方法

---

授權與引用 / License & Citation

本模板為 Apache License 2.0；任何顧問、企業內部、衍生顧問方法論皆可使用、修改、商業利用，唯需保留 [`NOTICE`](../NOTICE) 檔之署名。
