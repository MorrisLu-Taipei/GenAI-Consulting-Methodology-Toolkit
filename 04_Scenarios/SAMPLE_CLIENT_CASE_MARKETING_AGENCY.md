# 範例客戶案例：行銷服務業 / Sample Client Case: Marketing Agency

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>
>
> **本案例為示範用途，客戶以代號 "代理商 M" 表示（非真實公司名）。內容綜合自多家真實客戶之挑戰與解法，數字為示範值。**
> Sample case for illustration. Client referred to by the code "Agency M" (not a real company name) — synthesized from multiple real engagements; numbers illustrative.

---

## 1. 客戶背景 / Client Profile

| 欄位 | 內容 |
| --- | --- |
| 客戶代號 / Client code | 代理商 M / Agency M（數位行銷代理商，匿名） |
| 產業 | 數位行銷代理商 (Performance + Content + Social) |
| 員工 | 120 人 |
| 客戶數 | 27 個品牌客戶 (FMCG / 餐飲 / 美妝 / 醫美) |
| 年營收 | NT$ 3.2 億 |
| 部門結構 | Strategy 8 / Account 24 / Creative 32 / Media-Buy 18 / Data 12 / Production 18 / Admin 8 |
| 起始 L 級 | L1 (邊緣) |
| 啟動時間 | 2026 Q1 |
| 預算 | NT$ 480 萬 (12 個月) |
| 主要痛點 | 三快三慢：客戶要快、內容慢；報表多、洞察慢；提案急、深度慢 |

## 2. 顧問接觸與診斷 / Engagement Onboarding & Diagnostic

### 2.1 10 題快速問卷結果

| Q | 題目 | 評分 (0-4) |
| ---: | --- | ---: |
| Q1 | 員工每天用 AI 工具 | 3 |
| Q2 | Prompt / 經驗有集中整理 | 1 |
| Q3 | 有「好的 AI 使用」定義 | 1 |
| Q4 | AI 串企業系統 | 1 |
| Q5 | 有可重複呼叫 Skill / Workflow | 1 |
| Q6 | AI 使用規範 + Audit | 0 |
| Q7 | AI 有可量化成果 | 1 |
| Q8 | 有清楚下一步 (非靠廠商) | 2 |
| Q9 | 主管定期 review | 1 |
| Q10 | AI 風險防護 | 0 |
| **均分** |  | **1.1 → L1** |

**洞察**：員工個人使用率高 (Q1=3) 但治理為零 (Q6=0, Q10=0)。典型 **影子 IT** 階段，極高機敏外流風險（品牌客戶資料）。

### 2.2 25 題版六構面分數

| 構面 | 均分 | Bar |
| --- | ---: | --- |
| 工具使用 | 2.8 | ▓▓▓▓▓▓░░░░ |
| 知識沉澱 | 0.9 | ▓▓░░░░░░░░ |
| 流程標準化 | 1.2 | ▓▓▓░░░░░░░ |
| 系統整合 | 1.0 | ▓▓░░░░░░░░ |
| Agent 應用 | 0.5 | ▓░░░░░░░░░ |
| 治理 ROI | 0.4 | ▓░░░░░░░░░ |

整體 L1，工具使用偏 L2。**局部成熟度落差大** — 員工會用但組織無能力。

### 2.3 公司屬性 Bundle 重點

```json
{
  "profile": { "industry": "marketing_agency", "headcount_bucket": "50-300", "markets": ["TW"] },
  "systems": { "wiki": ["Notion"], "crm": "HubSpot", "asana": true, "figma": true, "media_buy": ["GA4","Meta Ads","Google Ads"] },
  "risk": { "sensitive_data": ["品牌機密","客戶 PII"], "regulations": ["個資法"], "llm_retention_acceptance": "30d" },
  "deployment": { "preference": "Hybrid", "vendor_acceptance": ["OpenAI","Anthropic","Google"] },
  "course": { "l1_headcount": 120, "seed_team_headcount": 14, "objectives": ["流程自動化","Agent 建置"] },
  "budget": { "annual_bucket": "2M-10M", "kickoff": "1-3個月", "first_poc": "1-3月" }
}
```

## 3. 課程比例建議 / Recommended Course Mix

| Level | 比例 | 重點 |
| ---: | ---: | --- |
| L1 | 35% | 全員 OpenWebUI、AI 使用規範、Brand Safety、品牌 / 客戶資料邊界 |
| L2 | 35% | Creative / Account / Media-Buy Skill Library；Antigravity 用於 ETL 與 Reporting |
| L3 | 20% | 報表自動化、社群輿情 Workflow、客戶月報 Pipeline |
| L4 | 8% | 客戶 Onboarding Briefing Agent |
| L5 | 2% | 跨職能 Agent Team（活動上線：Strategy + Copy + Design + Media-Buy + Report + Reviewer） |

理由：L1 治理 zero 必須先補；L2 Skill 是行銷代理商最大槓桿（內容大量再利用）；L3 接 GA4 / Ads / Meta API；L4-L5 為後期。

## 4. 課中產出資產 / In-Class Artifacts

### L1 OpenWebUI (4 週)

- 120 帳號開通 + 群組（Strategy / Account / Creative / Media / Data / Prod / Admin）+ 角色矩陣
- AI 使用規範 v1（含「不可對 LLM 提供客戶未公開素材」紅線）
- Brand Safety Prompt 模板 27 套（每客戶一套）
- Prompt Library 36 條（簡報草稿、活動命名、社群文案、報告 narrative...）
- 模型可見性：品牌客戶機敏 → 走 Azure OpenAI；公開素材 → 雲端 OpenAI

### L2 Skill AI (6 週)

13 個上線 Skill：

| # | Skill | Owner | L-target |
| --- | --- | --- | --- |
| 1 | 品牌 Tone-of-Voice 寫作 (per client) | Creative Lead | L2 |
| 2 | 社群短文 (FB / IG / Threads / X) batch | Social Manager | L2 |
| 3 | 廣告素材 brief→hook 提案 | Copy Lead | L2 |
| 4 | 月度 GA4 + Meta + Google Ads 報表 narrative | Data Lead | L2 |
| 5 | 客戶活動 Recap 草擬 | Account Lead | L2 |
| 6 | KOL 名單研究與接洽信草擬 | PR Lead | L2 |
| 7 | 內部會議錄音 → 行動清單 | Account Lead | L2 |
| 8 | 客戶報告封面 / 結構草稿 | Account Lead | L2 |
| 9 | 競品 Social Listening 摘要 | Strategy Lead | L2 |
| 10 | 提案草稿 (RFP 回覆) | Strategy Lead | L2 |
| 11 | 拍攝 brief 結構化 | Production Lead | L2 |
| 12 | Asana task ↔ Notion 雙向轉換 | Ops | L2 |
| 13 | 內部新人 onboarding Q&A (RAG over Notion) | HR | L2 |

每個 Skill 有 IPOE + ≥ 3 test cases + Owner + 版本（GitHub backup）。

### L3 n8n Workflow (6 週)

5 個 Workflow PoC：

1. **客戶月報自動 Pipeline** — Schedule → GA4/Ads API → Sheets → Skill #4 → Notion 月報草稿 → Account review → 發送
2. **社群輿情 Workflow** — Schedule 4 hr → 社群搜尋 API → Skill #9 → Slack 通知 Strategy
3. **新客戶 RFP 進線分類** — Gmail Trigger → OpenAI Chat → 分派給對應 Strategy + Notion task
4. **拍攝 brief → 製作 task 拆解** — Notion Trigger → Skill #11 → Asana batch create
5. **每週客戶 Pulse Check** — Schedule → HubSpot + GA4 → AI digest → 客戶 Slack channel

每 Workflow 含 Sub-workflow、Data Tables、GitHub Backup、Error DLQ。

### L4 Hermes Agent (4 週)

**客戶 Onboarding Agent** — 新客戶簽約後啟動：
- Wiki：產業、過往合作、品牌風格、輿情、競品
- Skills：上述 #1, #6, #9, #10
- Workflow：月報 Pipeline、社群輿情
- 任務卡：每個新客戶 onboarding 7 天內產出 「客戶 brief 文件 + 首次活動草稿」
- Reviewer：Account Director
- Gate 4A-4E 全通過

### L5 ClawTeam 演練 (2 週)

**新品上市 Agent Team** (基於 HKUDS/ClawTeam MIT)：
- Strategy Agent（市場定位）
- Copy Agent（主視覺文案 / 社群文案）
- Design Brief Agent（給設計師之創意 brief）
- Media-Buy Agent（媒體計畫草擬）
- Report Agent（活動結束週次自動 recap）
- Reviewer Agent（Brand Safety + 法遵）
- 整合：Account Director 為 Human Gate

實際情境：某客戶新品上市，過去 14 天流程縮至 5 天。

## 5. 八階段顧問分析 / Eight-Stage Analysis

### Stage 1 現況掌握
- 訪談：CEO、3 Account Director、Creative Lead、Data Lead、IT 1 人、3 線員工
- 痛點密度集中：客戶報告（90% 部門）、提案 RFP（Strategy）、社群製作（Creative）

### Stage 2 願景對齊
- CEO 願景：18 個月內 27 個品牌客戶 onboarding 縮至 3 天 (現 14 天)；提案 win rate 30%→45%
- Stakeholder RACI 簽妥；CMO 為 Sponsor，Strategy Director 為 AI Champion

### Stage 3 產業標竿
- 國際標竿：WPP / Publicis AI lab（過大）；本地：未明顯 AI 領先者
- Reference architecture 採自建（OpenWebUI + n8n + HubSpot）

### Stage 4 差距分析

Missing/Broken/Redundant：
- **Missing**：Skill Library、Audit Log、Brand Safety Prompt 矩陣、客戶資料邊界規範
- **Broken**：客戶月報製作流程（每客戶 6-8 hr）
- **Redundant**：簡報模板（每位 Account 自己一套）

Impact × Effort：
- Quick Win：客戶月報 Pipeline（L3-W1）
- Big Bet：Onboarding Agent（L4）
- Avoid：自建 chatbot（不在當下優先）

### Stage 5 高階問題定義

```
CONTEXT: 過去 12 個月有 3 家競爭對手宣稱「AI-first agency」，部分客戶詢問我方 AI 策略；
         若無回應預估 6 個月內流失 NT$ 2,400 萬合約。
TENSION: 員工每天用 AI 但組織完全無能力 (L1)；月報製作 6-8 hr 拖累交付。
COI:     不行動 12 個月：(1) NT$ 2,400 萬合約流失 (2) Creative 招募成本 NT$ 600 萬。
DESIRED: 12 個月達 L4；客戶月報 < 2 hr；Onboarding < 3 天；提案 win rate +50%。
CONSTRAINT: 預算 480 萬；CMO 為 Sponsor；不可影響當前交付節奏。
```

### Stage 6 路徑圖

| Phase | 月 | 主要交付 | Stage Gate | KPI |
| --- | --- | --- | --- | --- |
| 1 | 1-2 | L1 OpenWebUI + 規範 | Gate 1 ✓ | 員工週使用率 ≥ 80% |
| 2 | 3-4 | L2 13 Skills | Gate 2 ✓ | Skill Library ≥ 13 |
| 3 | 5-6 | L3 5 Workflows | Gate 3 ✓ | 客戶月報 < 2 hr |
| 4 | 7-9 | L4 Onboarding Agent | Gate 4 ✓ | Onboarding < 3 天 |
| 5 | 10-12 | L5 新品上市 Team | Gate 5 ✓ | 新品上市流程 ≤ 5 天 |

### Stage 7 解決方案架構

- Variant: **Hybrid**
- 雲：OpenAI for 公開素材；Azure OpenAI 隔離 tenant for 客戶機敏
- 本地：n8n self-host on AWS（避免共用節點）
- Notion 為 Wiki + Knowledge Base
- HubSpot 為 CRM；OAuth + Webhook + n8n 串接

### Stage 8 治理 ROI

- Permission：Creative / Account / Media 各群組可見不同模型；Audit Log 全保 1 年
- ROI Tracker：客戶月報工時、Onboarding 天數、提案 win rate、新品上市天數、員工 NPS

## 6. 診斷報告摘要 / Diagnostic Report Summary

> **核心發現**：代理商 M 之 AI 採用為員工主導（L1+，影子 IT 高），組織能力為零（L0）。建議 12 個月內完成 L1→L4 補強，避免再度落後競爭對手。
>
> **推薦投資**：NT$ 480 萬（教育訓練 NT$ 280 萬 + 平台 NT$ 80 萬 + 顧問 NT$ 120 萬）。
>
> **預期 ROI**：12 個月可量化效益 NT$ 1,800 萬（時間節省 1,200 萬 + 流失合約防護 600 萬），ROI ≈ 275%。

## 7. 30/60/90 天 Roadmap

### 30 天
- L1 OpenWebUI 120 帳號上線
- AI 使用規範 v1 簽署率 ≥ 90%
- Brand Safety Prompt × 27 完成
- 5 個 quick-win Skill 上架 (#1, #2, #4, #7, #12)
- Gate 1 通過

### 60 天
- Skill Library 13 個完成
- 客戶月報 Pipeline Workflow 上線；先試 3 個客戶
- Antigravity artifacts 完成
- Gate 2 通過

### 90 天
- 5 個 Workflow 全上線
- 客戶月報所有 27 個客戶涵蓋
- 客戶月報工時 6-8 hr → 1.5 hr
- Gate 3 通過
- 啟動 L4 Onboarding Agent 規劃

## 8. ROI 預估 / ROI Projection

| Initiative | Baseline | 12 月 Target | NT$ 影響 |
| --- | --- | --- | --- |
| 客戶月報製作工時 | 6-8 hr × 27 客戶 × 12 月 | 1.5 hr | NT$ 540 萬 / 年 |
| Onboarding 天數 | 14 天 | 3 天 | NT$ 360 萬 / 年 (Account 釋出) |
| 新品上市流程 | 14 天 | 5 天 | NT$ 200 萬 / 年 |
| 提案 win rate | 30% | 45% | NT$ 480 萬 / 年 (新業務) |
| Creative 重做率 | 25% | 12% | NT$ 180 萬 / 年 |
| 風險（合約流失防護） | - | - | NT$ 600 萬 |
| **小計** |  |  | **NT$ 2,360 萬** |
| **扣除投資** |  |  | **-480 萬** |
| **淨效益** |  |  | **NT$ 1,880 萬 / 年** |

## 9. 風險與治理 / Risks & Governance

| 風險 | 機率 | 影響 | 緩解 |
| --- | --- | --- | --- |
| 員工把客戶未公開素材送雲 LLM | 高 | 高 | L1 規範 + Brand Safety prompt + Audit log + DLP |
| AI 文案誤用品牌字眼 | 高 | 中 | Brand Safety Skill + Reviewer + 客戶簽核 |
| 客戶機密外流 | 中 | 致命 | Azure OpenAI tenant 隔離；機敏走地端 |
| 員工抗拒（怕被取代） | 中 | 中 | L1 全員體驗；CEO 公開承諾不裁員 |
| 預算超支 | 中 | 中 | 月度 ROI Gate；Stage Gate 不通過暫停 |

## 10. 結果摘要 / Outcome Summary

12 個月後（hypothetical projection）：
- 從 L1 推進到 L4
- 27 個客戶月報全自動化
- Onboarding Agent 已 onboard 12 個新客戶
- 1 個 ClawTeam 完成 3 次新品上市
- CMO 升等為集團 AI Lead；獲新業務 NT$ 4,800 萬

引用：完整 PoC 場景 `02_Course_Design/POC_SCENARIO_SPECS.md`；產業推薦 `INDUSTRY_SCENARIOS.md`；顧問工具 `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`。
