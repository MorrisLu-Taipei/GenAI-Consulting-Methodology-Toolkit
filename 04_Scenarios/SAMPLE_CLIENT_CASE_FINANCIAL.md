# 範例客戶案例：金融業 / Sample Client Case: Financial Services

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **本案例為示範用途，客戶以代號 "區域銀行 F" 表示（非真實公司名）。內容綜合自多家真實金融客戶之挑戰與解法，數字為示範值。**
> Sample case for illustration. Client referred to by the code "Regional Bank F" (not a real company name).

---

## 0. Benchmark-grade Summary（Tool 3.5 九欄位）

> **此案例符合 Tool 3.5 Cases-as-Benchmarks 紀律** ── 客戶可拿此表 30 分鐘自助算差距。

| # | 必填欄位 | 本案例 |
| --- | --- | --- |
| 1 | 產業 + 規模 | 金融（區域銀行），約 2,500 人 |
| 2 | 起點 L-level + 證據 | L1 部分 + APQC 13.0 Compliance = 3（金融業合規高） |
| 3 | 終點 L-level + 證據 | L3 + APQC 4.0 + 13.0 = 3 |
| 4 | 跨越期間 | 18 個月 |
| 5 | 跨越的 RM Category | APQC 4.0 Deliver、APQC 13.0 Compliance、Tiger AI L1-L3 |
| 6 | 每階段投入 | 估 NT$ 800-1,200 萬 / 40-60 人月 |
| 7 | Key wins（可量化） | KYC 文件摘要 Workflow、客服分流 Agent、ROI ~358% |
| 8 | Key failures（踩過的雷） | 若法遵審核流程未先打通、若地端 LLM 效能評估不足 |
| 9 | 適用條件 | ≥ 500 人區域 / 民營銀行、Hybrid 受限、預算 NT$ 800 萬+ |

**部署模式 / 代號**：全地端（金融監管要求） ／ 代號 區域銀行 F


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
| 客戶代號 / Client code | 區域銀行 F / Regional Bank F（區域型商業銀行，匿名） |
| 產業 | 區域型商業銀行（消金 + 企金 + 財管） |
| 員工 | 2,500 人（分行 1,600 / 總行 700 / IT 200） |
| 分行數 | 68 |
| 起始 L 級 | L1（總行 IT 局部 L2） |
| 預算 | NT$ 2,400 萬（18 個月） |
| 監管 | 金管會、個資法、洗錢防制法、ISO 27001 |
| 主要痛點 | (1) KYC / 徵審文件處理慢 (2) 客服分流靠人工 (3) 法遵檢核覆蓋不足 (4) 分行知識落差大 |

## 2. 顧問接觸與診斷

### 2.1 10 題快速問卷結果

均分 **0.9 → L1**。工具使用 Q1=2（員工私下用），治理 Q6=1、風險 Q10=2（金融業相對有 IT 紀律但 AI 治理空白）。

### 2.2 25 題六構面

| 構面 | 均分 |
| --- | ---: |
| 工具使用 | 1.8 |
| 知識沉澱 | 1.0 |
| 流程標準化 | 2.2（金融 SOP 文化強） |
| 系統整合 | 1.5 |
| Agent 應用 | 0.3 |
| 治理 ROI | 1.6 |

**洞察**：流程標準化分數高（SOP 文化），但工具與 Agent 低。金融業導入特性 — 治理門檻高、但一旦過關擴散快。

### 2.3 公司屬性 Bundle 重點

```json
{
  "profile": {"industry":"financial","headcount_bucket":"1000-5000"},
  "systems": {"core_banking":"自建主機","crm":"自建","erp":"SAP","wiki":["SharePoint"],"kyc":"第三方"},
  "risk": {"sensitive_data":["PII","財務","徵信","交易"],"regulations":["金管會","個資法","洗錢防制法","ISO 27001"],"llm_retention_acceptance":"拒絕"},
  "deployment": {"preference":"全地端","gpu_capacity":"H100 級","local_llm_plan":"是"},
  "course": {"l1_headcount":2500,"seed_team_headcount":40,"objectives":["治理建立","流程自動化"]},
  "budget": {"annual_bucket":"10M+","kickoff":"3-6個月"}
}
```

## 3. 課程比例建議

| Level | 比例 | 重點 |
| ---: | ---: | --- |
| L1 | 40% | 全員啟用 + **治理優先**；地端 OpenWebUI；金融資料紅線；模型可見性嚴管 |
| L2 | 25% | 徵審 / 法遵 / 客服 Skill；強制 Reviewer |
| L3 | 25% | KYC 文件摘要、客服分流、法遵檢核 Workflow |
| L4 | 8% | 法遵助理 Agent（高度受控） |
| L5 | 2% | 暫不導入，僅概念說明 |

理由：金融業治理門檻最高，L1 須佔 40%（地端部署 + 權限 + Audit + 法遵教育）。L5 在監管未明前不導入。

## 4. 課中產出資產

### L1 OpenWebUI (8 週，分批)

- 2,500 帳號分 6 梯次上線（先總行後分行）
- **全地端部署**：H100 機房 + Llama 70B + 地端 Embedding，零雲端 LLM 呼叫
- AI 使用規範 v1（金管會對標）：客戶資料 / 徵信 / 交易資料絕對不可進任何外部服務
- 模型可見性：分行櫃員只能用「客服 FAQ」模型；徵審只能用「文件摘要」模型；總行 IT 全權
- Prompt Library 45 條（皆經法遵預審）
- Audit Log：所有 LLM 呼叫即時寫入，3 年保存

### L2 Knowledge Codification (8 週)

12 個 Skill（每個經法遵 + 資安雙審）：

| # | Skill | Owner | 備註 |
| --- | --- | --- | --- |
| 1 | KYC 文件重點摘要 | 徵審 | 不外送、地端 |
| 2 | 徵信報告草擬輔助 | 企金 | Reviewer 強制 |
| 3 | 客訴信件分類 | 客服 | - |
| 4 | 法遵法規變更摘要 | 法遵 | 政府網站 RAG |
| 5 | 分行 SOP 問答 | 全分行 | RAG over SharePoint |
| 6 | 理財商品說明白話化 | 財管 | 不得構成投資建議 |
| 7 | 內部稽核底稿草擬 | 內稽 | - |
| 8 | 客戶 360 摘要（內部用） | 分行主管 | 嚴格權限 |
| 9 | 洗錢防制案件初篩說明 | 法遵 | 僅輔助、人工決策 |
| 10 | 新人 onboarding Q&A | HR | - |
| 11 | 會議紀錄與行動項 | 總行各處 | - |
| 12 | 信用卡客訴回覆草稿 | 卡部 | Reviewer 強制 |

### L3 n8n Workflow (10 週)

5 個 Workflow PoC（皆地端 n8n、地端 LLM）：

1. **KYC 文件摘要 Pipeline** — 文件上傳 → OCR → Skill #1 → 徵審人員 review queue
2. **客服信件分流** — 內部信箱 → Skill #3 → 分派 + 優先級
3. **法規變更監測** — Schedule → 金管會 / 政府網站 → Skill #4 → 法遵 Slack
4. **分行知識問答** — 分行員工問 → RAG over SharePoint → 答 + 來源
5. **內稽底稿輔助** — 稽核項目 → 歷史底稿 RAG → Skill #7 → 稽核員 review

### L4 Hermes Agent (6 週)

**法遵助理 Agent**（極度受控）：
- Wiki：法規庫、內規、歷史裁罰案例、FAQ
- Skills：#4, #9
- 任務卡：法遵人員查詢「某情境是否合規」→ Agent 給「相關法規 + 內規 + 類似案例 + 不確定處標註」
- **Reviewer：法遵主管強制簽核每一筆**
- Evidence：100% 來源追溯
- Gate 4A-4E + 額外 Gate 4F（法遵長簽署）

### L5 ClawTeam

本階段**不導入**。僅在課程中概念說明，待金管會 AI 監理規範明朗後再評估。

## 5. 八階段顧問分析

### Stage 1 現況掌握
- 訪談：總經理、法遵長、資訊長、徵審處長、客服處長、3 分行經理、內稽
- 痛點密度：KYC / 徵審（企金 100%）、客服分流（消金 90%）、法遵覆蓋（法遵 100%）

### Stage 2 標準模型引入
- 總經理願景：18 個月內 KYC 處理時間減半、法遵檢核覆蓋率 100%、不發生 AI 相關裁罰
- Sponsor = 資訊長 + 法遵長（雙 sponsor，金融業特性）

### Stage 3 產業最佳實務對標
- 國際：星展 / 匯豐 AI lab（規模差距大）；台灣：少數金控在 PoC
- 採全地端自建，對標金管會「金融業運用 AI 指引」

### Stage 4 差距分析

Missing/Broken/Redundant：
- **Missing**：AI 治理框架、Skill Library、地端 LLM 基礎建設、Audit 機制
- **Broken**：KYC 文件人工逐頁讀（每件 40-60 min）
- **Redundant**：68 分行各自的 SOP 問答方式（無統一知識庫）

Impact × Effort：
- Quick Win：分行知識問答（L3-W4）；客服分流（L3-W2）
- Big Bet：KYC Pipeline（L3-W1，需 OCR + 地端 LLM）
- Avoid：消費者直接面對的 AI chatbot（監管風險高，當前不做）

### Stage 5 結論與核心問題定義

```
CONTEXT: 金管會 2025 發布金融業 AI 指引；同業已啟動 AI PoC。區域銀行 F KYC 處理速度落後同業，
         企金客戶抱怨開戶 / 徵審慢；法遵人力不足覆蓋率僅 70%。
TENSION: 流程 SOP 成熟 (L2) 但無 AI 工具；2,500 員工知識落差大。
COI: 不行動 18 個月：(1) 企金客戶流失預估 NT$ 8,000 萬 (2) 法遵覆蓋不足之裁罰風險。
DESIRED: 18 個月達 L4；KYC 處理 -50%；法遵覆蓋 100%；零 AI 相關裁罰。
CONSTRAINT: 預算 2,400 萬；全地端、零雲端 LLM；每個 AI 應用須法遵 + 資安雙審；分批導入。
```

### Stage 6 標竿對照與多階段目標設定

| Phase | 月 | 主要交付 | Gate | KPI |
| --- | --- | --- | --- | --- |
| 1 | 1-3 | 地端基礎建設 + AI 治理框架 | 前置 Gate | H100 機房就緒、治理框架法遵簽署 |
| 2 | 4-7 | L1 全員（6 梯次） | Gate 1 | 員工週使用 ≥ 70% |
| 3 | 8-11 | L2 12 Skills | Gate 2 | Skill Library ≥ 12，全經雙審 |
| 4 | 12-15 | L3 5 Workflows | Gate 3 | KYC 處理 -50% |
| 5 | 16-18 | L4 法遵助理 Agent | Gate 4 + 4F | 法遵覆蓋 100% |

### Stage 7 未來藍圖設計

- **Variant C 全地端**：
  - OpenWebUI Local + n8n Local + Hermes Local
  - Llama 70B + bge-m3 embedding（H100 ×4）
  - Qdrant 向量庫（地端）
  - 零雲端 LLM 呼叫，符合金管會指引

### Stage 8 執行導入與變革治理

- Permission：櫃員 / 徵審 / 法遵 / 內稽 / IT 五層；模型級 + 資料級雙重 ACL
- Audit：所有 LLM call 3 年；法遵相關永久
- 法遵雙審流程：每個 Skill / Workflow / Agent 上線前法遵 + 資安會簽
- ROI Tracker：KYC 時間、法遵覆蓋率、客服分流準確、分行知識問答使用率

## 6. 診斷報告摘要

> **核心發現**：區域銀行 F 流程 SOP 成熟（L2）但 AI 工具與治理空白（L1）。金融業特性 — 導入門檻高（須全地端 + 雙審），但一旦框架建立擴散快。建議 18 個月推進至 L4，重點在治理框架先行。
>
> **預期 ROI**：18 個月可量化效益 NT$ 1.1 億，ROI ≈ 358%。

## 7. 30/60/90 天 Roadmap

### 30 天
- 地端 H100 機房規劃 + 採購啟動
- AI 治理框架草案（法遵 + 資安 + IT 三方）
- L1 課程教材在地化（金融場景）

### 60 天
- H100 機房就緒、Llama 70B 部署測試
- AI 治理框架法遵長簽署
- L1 第 1 梯次（總行 200 人）上線
- 前置 Gate 通過

### 90 天
- L1 第 2-3 梯次（總行剩餘 + 首批分行）
- 3 個 quick-win Skill 雙審通過
- Gate 1 啟動評估

## 8. ROI 預估

| Initiative | Baseline | 18 月 Target | NT$ 影響 |
| --- | --- | --- | --- |
| KYC / 徵審文件處理 | 40-60 min/件 | 20 min | NT$ 3,200 萬/年（徵審人力釋出） |
| 法遵覆蓋率 | 70% | 100% | NT$ 4,000 萬（裁罰風險防護） |
| 客服分流 | 人工 | AI 輔助 | NT$ 1,800 萬/年 |
| 分行知識落差 | 高 | 統一知識庫 | NT$ 1,200 萬/年（錯誤 + 訓練成本） |
| 企金客戶流失防護 | - | - | NT$ 8,000 萬（一次性風險） |
| **小計（年化 + 風險）** |  |  | **NT$ 1.82 億** |
| **扣除投資** |  |  | **-2,400 萬** |
| **淨效益** |  |  | **NT$ 1.58 億** |

## 9. 風險與治理

| 風險 | 機率 | 影響 | 緩解 |
| --- | --- | --- | --- |
| 客戶 / 交易資料外流 | 低（地端） | 致命 | 全地端、零雲端、Audit、DLP |
| AI 構成投資建議違規 | 中 | 致命 | 理財 Skill 嚴格限制；Reviewer；法遵審 |
| 法遵助理 Agent 誤判 | 中 | 高 | 100% 人工簽核；Agent 僅輔助 |
| 金管會監理變化 | 中 | 高 | 法遵持續追蹤；L5 暫緩 |
| 分行員工抗拒 | 中 | 中 | 分梯次；分行經理帶頭；不裁員承諾 |
| 地端 LLM 效能不足 | 中 | 中 | H100 ×4；必要時升級；非即時場景優先 |

## 10. 結果摘要

18 個月後：
- 從 L1 推進至 L4（法遵助理 Agent 上線）
- KYC 處理時間減半；法遵覆蓋 100%
- 零 AI 相關裁罰
- 全地端架構成為同業參訪標竿
- 資訊長 + 法遵長共同主導之「AI 治理委員會」常設化

引用：完整 PoC `02_Course_Design/POC_SCENARIO_SPECS.md`；產業 `INDUSTRY_SCENARIOS.md`；顧問工具 `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`。
