# 範例客戶案例：B2B 業務 / Sample Client Case: B2B Sales

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **本案例為示範用途，客戶以代號 "工業設備商 B" 表示（非真實公司名）。內容綜合自多家真實 B2B 客戶之挑戰與解法，數字為示範值。**
> Sample case for illustration. Client referred to by the code "Industrial Vendor B" (not a real company name).

---

## 0. Benchmark-grade Summary（Tool 3.5 九欄位）

> **此案例符合 Tool 3.5 Cases-as-Benchmarks 紀律** ── 客戶可拿此表 30 分鐘自助算差距。

| # | 必填欄位 | 本案例 |
| --- | --- | --- |
| 1 | 產業 + 規模 | B2B 工業設備，約 200-400 人 |
| 2 | 起點 L-level + 證據 | L0-L1 + APQC 4.0 Deliver = 1 |
| 3 | 終點 L-level + 證據 | L3 + APQC 4.0 = 3 |
| 4 | 跨越期間 | 9-12 個月 |
| 5 | 跨越的 RM Category | APQC 4.0 Deliver、SCOR Source、Tiger AI L1-L3 |
| 6 | 每階段投入 | 估 NT$ 300-500 萬 / 18-24 人月 |
| 7 | Key wins（可量化） | 商機篩選 -60% 時間、報價 4 天→1 天、跨地理區業務一致性 |
| 8 | Key failures（踩過的雷） | 若 CRM 資料品質不足、若業務 Champion 換人 |
| 9 | 適用條件 | 100-800 人 B2B 設備商、CRM 已就位、有海外業務 |

**部署模式 / 代號**：Hybrid ／ 代號 工業設備商 B


**Evidence Level**：🔵 **L0 — AI-Simulated Teaching Case**（AI 模擬教學案例，在 Tool 8.9 Evidence Hierarchy 之下）

> ⚠️ **本案例由 AI 模擬產生，並非真實客戶資料**。
>
> - **目的**：作為教學示範、方法論講解、Stage 1-8 工具表套用練習用
> - **來源**：AI 依據產業常識 + 方法論架構合成出符合 Tool 3.5 九欄位 Benchmark-grade 格式的虛構案例
> - **所有數字**（時間 / ROI / 投入人月 / 預算 / KPI）**僅為示例**，**不可**作為：
>   - 對外客戶宣傳依據
>   - 顧問合約 ROI 承諾
>   - 學術引用之 empirical evidence
>   - 對任何單一真實公司的對比結論
>
> 證據等級依 Tool 8.9 Evidence Hierarchy：L1 自評 · L2 文件 · L3 系統 log · L4 第三方稽核 · L5 縱貫 KPI ── **本案例屬 L0（pre-evidence）**，低於 L1。
>
> **真實 longitudinal 案例**需透過 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) 18-24 個月實證研究完成後才會替換。在此之前，請以**AI 模擬教學案例**對待本檔內容。

> 詳細案例細節見下方各章節。本表為 [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 3.5 規範的標準摘要。

---


## 1. 客戶背景 / Client Profile

| 欄位 | 內容 |
| --- | --- |
| 客戶代號 / Client code | 工業設備商 B / Industrial Vendor B（工業自動化設備 + 軟體，匿名） |
| 產業 | 工業自動化設備 + 軟體 (PLC / SCADA / 解決方案銷售) |
| 員工 | 380 人 (Sales + Engineering + Support) |
| 業務團隊 | 60 (含 SDR 12 + AE 32 + SE 8 + Sales Ops 8) |
| 客戶 | 240 個現役企業客戶 (製造、能源、半導體、食品) |
| 年營收 | NT$ 12 億 |
| 平均單筆 deal | NT$ 380 萬 |
| 平均 sales cycle | **9-14 個月** |
| 起始 L 級 | L2 (局部 L3) |
| 預算 | NT$ 720 萬 (12 個月) |
| 主要痛點 | (1) Sales cycle 過長 (2) CRM 資料碎裂 (3) RFP 回覆耗時 14 天 (4) SDR→AE 交接斷層 |

## 2. 顧問接觸與診斷

### 2.1 10 題快速問卷結果

| Q | 評分 |
| ---: | ---: |
| Q1 工具使用 | 3 |
| Q2 知識沉澱 | 2 |
| Q3 流程標準化 | 2 |
| Q4 系統整合 | 2 |
| Q5 Agent 應用 | 1 |
| Q6 治理 + Audit | 2 |
| Q7 ROI 可量化 | 2 |
| Q8 下一步清楚 | 3 |
| Q9 主管 review | 2 |
| Q10 風險防護 | 2 |
| **均分 2.1 → L2-L3 邊緣** |  |

### 2.2 25 題六構面

| 構面 | 均分 |
| --- | ---: |
| 工具使用 | 3.0 |
| 知識沉澱 | 2.1 |
| 流程標準化 | 1.8 |
| 系統整合 | 2.0 |
| Agent 應用 | 0.8 |
| 治理 ROI | 2.0 |

**洞察**：工具普及但 Agent 為零；知識沉澱集中在資深 AE 個人腦中（流失風險高）。

### 2.3 公司屬性 Bundle 重點

```json
{
  "profile": {"industry":"b2b_industrial","headcount_bucket":"300-1000"},
  "systems": {"crm":"Salesforce","erp":"SAP","support":"Zendesk","cpq":"Salesforce CPQ","wiki":["Confluence"]},
  "risk": {"sensitive_data":["客戶廠房資料","RFP","定價"],"regulations":["個資法"],"llm_retention_acceptance":"拒絕"},
  "deployment": {"preference":"Hybrid","gpu_capacity":"L40 級","local_llm_plan":"是"},
  "course": {"l1_headcount":380,"seed_team_headcount":18,"objectives":["流程自動化","Agent 建置"]},
  "budget": {"annual_bucket":"2M-10M","first_poc":"<1月"}
}
```

## 3. 課程比例建議

| Level | 比例 | 重點 |
| ---: | ---: | --- |
| L1 | 20% | 補齊規範與權限；強調定價 / RFP 紅線 |
| L2 | 25% | RFP / Demo / 技術文件 Skill |
| L3 | 30% | CRM-to-Slack alert、Lead scoring、Deal stage automation、Forecast aggregator |
| L4 | 20% | Account Briefing Hermes Agent |
| L5 | 5% | Pre-RFP Response ClawTeam |

理由：起點 L2-L3 → 重點補 Skill 沉澱 + 自動化系統整合 + Agent。RFP 是業務金雞母，最高槓桿。

## 4. 課中產出資產

### L1 OpenWebUI (3 週)

- 380 帳號 + 群組（Sales / Eng / Support / Admin）
- AI 使用規範：客戶資料邊界（廠房配置 / RFP 內容禁外送雲 LLM）
- Prompt Library 28 條（拜訪前 brief、後送 follow-up、Demo intro、競品比較）

### L2 Knowledge Codification (6 週)

15 個 Skill：

| # | Skill | Owner |
| --- | --- | --- |
| 1 | 拜訪前 Account brief (自動整合 CRM / news / 公開資訊) | AE |
| 2 | 拜訪後 follow-up email | AE |
| 3 | RFP 段落草擬（技術 / 商務 / 服務） | SE / Sales |
| 4 | Demo 開場與情境串接 | SE |
| 5 | 競品功能對比表 | Product Marketing |
| 6 | 客戶 ROI 試算 worksheet 草擬 | Sales |
| 7 | 報價 narrative + 替代方案 | Sales |
| 8 | Legal/MSA 常見條款 Q&A | Legal |
| 9 | 既有客戶健康摘要 | CSM |
| 10 | Onboarding playbook（依產業） | CSM |
| 11 | 技術文件 → 客戶常見問題 FAQ | SE |
| 12 | 客戶月度 QBR 草擬 | AE / CSM |
| 13 | Forecast call narrative | Sales Manager |
| 14 | 對 SDR 之 lead qualification rubric | SDR Lead |
| 15 | Account map 視覺化（決策者、影響者、技術評估者） | AE / SE |

### L3 n8n Workflow (8 週)

7 個 Workflow PoC：

1. **Lead scoring + 自動分派** — Form/HubSpot inbound → enrichment API → Skill #14 → Salesforce assignment + Slack DM
2. **CRM → Slack alert** — Salesforce Webhook → 重大階段變更 / 大金額 → Slack with brief
3. **Deal stage 自動化** — 階段移動觸發 follow-up email、task、template 預設
4. **Weekly forecast aggregator** — Schedule Sun 9pm → Salesforce → Skill #13 → Sales Manager email
5. **客戶健康分數** — Schedule daily → Salesforce + Zendesk + product usage → Skill #9 → field update + alert
6. **RFP 進線自動分類** — Email Trigger → OpenAI → Notion task + AE assign
7. **競品價格爬蟲 + 摘要** — Schedule weekly → web scrape → Skill #5 → Confluence

### L4 Hermes Agent — Account Briefing (4 週)

**Sales Account Briefing Agent**：
- Wiki：客戶 history（過去互動 / 合約 / 訴訟 / 主管異動 / 公開新聞）
- Skills 引用：#1, #5, #9, #15
- Workflows 引用：CRM alert、客戶健康
- 任務卡：每個 AE 拜訪前 1 hr 自動產出 brief
- Reviewer：AE 簽收（拒絕 / 修改 / 接受）
- Evidence：每筆 brief 來源完整追溯
- Gate 4A-4E 通過

### L5 ClawTeam — Pre-RFP Response Team (2 週演練)

基於 HKUDS/ClawTeam (MIT)，組成 6 個 Agent：

| Agent 角色 | 任務 |
| --- | --- |
| **Solution Architect Agent** | 從 RFP 萃取技術需求、對應產品方案 |
| **Pricing Agent** | 依產品 mix 與客戶 segment 給定價區間 |
| **Legal Agent** | 比對 MSA、找出客戶 RFP 條款風險點 |
| **Reference Agent** | 從 CRM 找類似客戶 case study |
| **Reviewer Agent** | Brand safety + 商務一致性 |
| **Coordinator (Human Gate)** | Sales Director |

實際情境：某半導體大客戶 RFP，過去 14 天回覆縮至 5 天，且涵蓋面更完整。

## 5. 八階段顧問分析

### Stage 1 現況掌握
- 訪談：CSO、3 Sales Manager、2 Account Director、SE Lead、CRM Admin、Legal
- 痛點密度：RFP 回覆（90%）、Forecast 不準（60%）、SDR→AE 交接斷層（45%）

### Stage 2 標準模型引入
- CSO 願景：18 個月內 sales cycle 9-14 月 → 6-9 月；RFP 14 天 → 5 天；win rate 22%→32%
- Stakeholder：CSO = Sponsor；Sales Ops Lead = AI Champion

### Stage 3 產業最佳實務對標
- B2B Industrial：Salesforce Einstein、Gong、Outreach AI（功能參考但不直接導）
- 採自建（Hybrid）以保護 RFP / 定價機敏

### Stage 4 差距分析

Missing/Broken/Redundant：
- **Missing**：Account brief 自動化、RFP Library、Lead scoring 模型、Forecast narrative
- **Broken**：CRM 資料品質 35% 欄位空白；SDR→AE 交接靠 email
- **Redundant**：3 套 follow-up email 模板（每 Team 自製）

Impact × Effort：
- Quick Win：Account brief Skill（L2-W2）；CRM Slack alert（L3-W1）
- Big Bet：Pre-RFP ClawTeam（L5，第 11-12 月）
- Avoid：自建 LLM-based forecasting 預測模型（資料不足）

### Stage 5 結論與核心問題定義

```
CONTEXT: 過去 12 個月競爭對手 Siemens / Rockwell 加大數位內容 RFP 回覆速度；我方 RFP 14 天平均
         流失 3 場 NT$ 2,800 萬大案。資深 AE 之一即將退休，知識斷層風險高。
TENSION: 工具普及但組織能力 (L2) 沉澱不夠；資深 AE 個人知識難複製。
COI: 不行動 12 個月：(1) NT$ 6,000 萬 RFP 流失預估 (2) 資深 AE 退休後新人 ramp-up 12+ 月。
DESIRED: 12 個月達 L4；RFP 5 天；Forecast 準度 ±10%；新人 ramp-up 3 個月。
CONSTRAINT: 預算 720 萬；RFP / 定價資料不可送雲 LLM；CRM 必須先資料治理。
```

### Stage 6 標竿對照與多階段目標設定

| Phase | 月 | 主要交付 | Gate | KPI |
| --- | --- | --- | --- | --- |
| 1 | 1-2 | L1 + 規範 + CRM 資料清理 | Gate 1 ✓ | CRM 必填率 ≥ 90% |
| 2 | 3-4 | L2 15 Skills | Gate 2 ✓ | RFP 草擬 14d → 8d |
| 3 | 5-7 | L3 7 Workflows | Gate 3 ✓ | Lead 分派 < 5 min |
| 4 | 8-10 | L4 Account Briefing Agent | Gate 4 ✓ | 拜訪 brief 採用率 ≥ 80% |
| 5 | 11-12 | L5 Pre-RFP ClawTeam | Gate 5 ✓ | RFP 14d → 5d |

### Stage 7 未來藍圖設計

- **Hybrid 部署**：
  - 公開資料 / 公開 news → 雲 (Anthropic Claude)
  - 客戶 history / RFP / 定價 → 地端 Llama 70B (L40 GPU)
- **CRM**：Salesforce Webhook → n8n self-host
- **Wiki**：Confluence → embedding → Qdrant vector DB（地端）

### Stage 8 執行導入與變革治理

- Permission：Sales / SE / Manager / Director 四層；CRM 欄位級 ACL
- Audit Log：所有 LLM call 1 年保存；RFP 相關 3 年
- ROI Tracker：sales cycle、RFP 天數、win rate、forecast accuracy、AE ramp-up

## 6. 診斷報告摘要

> **核心發現**：工業設備商 B 於 L2-L3 邊緣，工具使用普及但組織知識沉澱不足，資深員工流失風險即將觸發。建議 12 個月推進至 L4（Account Briefing Agent + Pre-RFP Team），同步補強 CRM 資料治理。
>
> **預期 ROI**：12 個月可量化效益 NT$ 4,400 萬，ROI ≈ 511%。

## 7. 30/60/90 天 Roadmap

### 30 天
- L1 OpenWebUI 380 帳號 + 規範
- CRM 資料治理 sprint：必填欄位策略、歷史資料清理
- 啟動 Skill #1 拜訪前 brief（quick win）
- Gate 1 通過

### 60 天
- Skill Library 15 個完成
- RFP Library 結構化（過去 RFP 拆段、tag）
- Workflow PoC #1, #2 上線
- Gate 2 通過
- RFP 草擬 14 天 → 10 天

### 90 天
- 7 個 Workflow 全上線
- Forecast aggregator 第一次完整運作
- Account Briefing Agent 規劃 + Wiki 建構啟動
- Gate 3 通過
- Lead 分派時間 < 5 min；CRM 必填 ≥ 90%

## 8. ROI 預估

| Initiative | Baseline | 12 月 Target | NT$ 影響 |
| --- | --- | --- | --- |
| RFP 回覆天數 | 14 天 | 5 天 | NT$ 600 萬（AE/SE 釋出） |
| RFP 流失 (因慢) | 3 場/年 | 0 場 | NT$ 2,800 萬 |
| Forecast 準度 | ±25% | ±10% | NT$ 400 萬（庫存 + 計畫） |
| Account brief 採用 | 25% | 80% | NT$ 600 萬（多 12 場拜訪/AE/年） |
| AE ramp-up | 12 月 | 6 月 | NT$ 500 萬（新人 4 位/年） |
| Forecast call 工時 | 4 hr/週 × 8 管理者 | 1 hr | NT$ 250 萬 |
| **小計** |  |  | **NT$ 5,150 萬** |
| **扣除投資** |  |  | **-720 萬** |
| **淨效益** |  |  | **NT$ 4,430 萬 / 年** |

## 9. 風險與治理

| 風險 | 機率 | 影響 | 緩解 |
| --- | --- | --- | --- |
| RFP / 定價外流雲 LLM | 高 | 致命 | 地端 Llama；DLP；Audit log；員工教育 |
| AI 對技術規格產生幻覺 | 高 | 高 | SE 強制 review；Hermes evidence 機制 |
| CRM 資料品質低 → AI 輸出垃圾 | 高 | 高 | 第 1 月專案：CRM 清理 sprint |
| AE 不採用 Account brief | 中 | 中 | Champion AE 帶頭；brief 內嵌 deal 自動更新 |
| Forecast Agent 偏離真實 | 中 | 高 | Human Gate；保留人工 override |

## 10. 結果摘要

12 個月後：
- 從 L2 推進至 L4（Pre-RFP ClawTeam 在試）
- RFP 14 天 → 5 天；win rate 22% → 30% (向 32% 進)
- Forecast 準度 ±25% → ±12%
- 1 位資深 AE 退休後新人 ramp-up 6 個月（原 12 個月）
- CSO 升等為集團 CDO；Sales Ops Lead 成 AI Practice Lead

引用：完整 PoC `02_Course_Design/POC_SCENARIO_SPECS.md`；產業 `INDUSTRY_SCENARIOS.md`；顧問工具 `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`；ClawTeam 引用 `90_References/CLAWTEAM_REFERENCE.md`。
