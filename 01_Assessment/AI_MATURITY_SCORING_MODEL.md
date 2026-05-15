# AI 成熟度評分模型

更新日期：2026-05-13

## 1. 評分目的

本評分模型用來將企業 AI 現況轉換成可溝通、可比較、可導入的成熟度結果。

評分不是為了貼標籤，而是為了回答四個問題：

1. 企業目前主要落在哪個成熟度等級？
2. 哪些能力已經具備，哪些能力仍是缺口？
3. 課程比例應該如何配置？
4. 顧問診斷報告應該優先處理哪些議題？

## 2. L1-L5 成熟度定義

L1-L5 是**兩條軸**：**規模軸（L1-L3）** —— 個人 → 部門 → 跨部門 / 全公司，人監督 AI；**AI 自主軸（L4-L5）** —— AI 超級助理 → AI 團隊，AI 營運自主、人退為治理者（仍保有監督權）。關鍵分界在 L3 → L4。完整故事見 [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0。

> **命名說明（v2.0 雙層命名）**：L1-L5 採**能力導向命名**（capability-oriented naming）。各級的「Tiger AI Reference Implementation」欄為 Tiger AI 採用的**示例工具**，非定義 —— 同樣的能力可用其他工具實現（如 L1 可用 OpenWebUI / LibreChat / 自建 chat gateway 等）。這保留了學術上的 vendor-neutral 立場 + 實務上的具體可實作性。

| 等級 | 能力名稱 (Capability Name) | 早期短稱 (legacy) | Tiger AI Reference Implementation | 軸 | 成熟度定義 | 完成標準 |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | **Controlled AI Access** 受控 AI 入口 | `Chat AI` (deprecated) | OpenWebUI | 規模軸·個人 | 員工能透過受控入口使用 AI，提升個人效率 | 有統一入口、基本使用規範、常用 Prompt、個人效率案例 |
| L2 | **Knowledge Codification** 知識資產化 | `Skill AI` (deprecated) | Antigravity / Claude Code / Codex | 規模軸·部門 | 以部門職責為單位，個人經驗被整理成部門可複用 Skill | 有 Skill Library、SOP、模板、Checklist、部門共用範例 |
| L3 | **Workflow Automation** 流程自動化 | `Workflow AI` (deprecated) | n8n | 規模軸·跨部門 / 全公司 | 串接跨部門 Skill 與系統，AI 進入全公司流程執行任務 | 有 Gmail、Sheets、Notion、CRM、API、ERP 等流程 PoC 或上線流程 |
| L4 | **Autonomous Agent** 自主代理 | `Auto Agentic AI` (deprecated) | Hermes Agent | AI 自主軸·超級助理 | 全自動 AI Agent 能以 Wiki 記憶為底座，呼叫 Skill/Workflow，進行 ingest、query、update、briefing 並留下 evidence | 有 Agent 任務卡、L4 IPOE、Wiki/schema、工具清單、權限邊界、Log、HITL 人類審核與驗收關卡 4A-4E |
| L5 | **Multi-Agent Organization** 多代理組織 | `Agentic Team AI` (deprecated) | ClawTeam | AI 自主軸·AI 團隊 | 多個專業 Agent 形成職能分工，協同完成跨部門企業級任務 | 有 Agent Team 角色分工、任務分派、整合輸出、品質檢查與治理 |

> 術語：本評分模型的 **Stage Gate ＝ 階段驗收關卡**、**HITL ＝ Human-in-the-Loop（人類在迴圈內審核）**。

## 3. 六大評估構面

| 構面 | 說明 | 主要對應成熟度 |
| --- | --- | --- |
| A. 工具使用 | 員工是否穩定、安全、有效使用 AI 工具 | L1 |
| B. 知識沉澱 | 是否將 Prompt、SOP、模板、經驗整理成可複用資產 | L2 |
| C. 流程自動化 | 是否把 AI 接進實際流程並減少人工重工 | L3 |
| D. 系統整合 | 是否能串接 Gmail、Sheets、Notion、CRM、API、ERP、DB | L3 |
| E. Agent 應用 | 是否有可拆解任務、呼叫工具、累積記憶、產生 briefing、執行回報且可追溯的 Agent | L4-L5 |
| F. 執行導入與變革治理 | 是否有權限、稽核、資料分級、KPI 與 ROI 追蹤 | L1-L5 |

## 3.1 Construct Definition Table（學術級量表規範）

> **目的**：把 6 大構面從「顧問口語描述」升級為**研究級量表 (psychometric scale) 規範**。每構面明確：定義、觀察指標、排除項、測量題目、證據來源（對應 [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 8.9 Evidence Hierarchy）。
>
> 這份表是後續 §3.2 信效度驗證（Cronbach's α / EFA / CFA / inter-rater reliability）的基礎。

### A. 工具使用 / Tool Usage

| 項目 | 內容 |
| --- | --- |
| **Definition / 定義** | 員工是否能透過受控入口、穩定、安全、有效地使用 AI 工具完成日常工作；公司是否有可追溯的使用紀錄與規範 |
| **Observable Indicators / 觀察指標** | (a) 全員 AI 帳號開通率 (b) AI 使用規範簽署率 (c) 月度活躍使用比例 (d) Prompt Library 條數 (e) 影子 IT（私人帳號）比例 |
| **Exclusions / 排除項** | **不包含**：員工是否「會使用 AI」的主觀感受、員工是否「想用 AI」的態度問卷（這屬於 readiness，見 §3.3）|
| **Measurement Items / 測量題目** | 10 題版 Q1-Q2、25 題版 Q1-Q5、50 題版 Q1-Q10（詳見 [`AI_MATURITY_QUESTIONNAIRE.md`](AI_MATURITY_QUESTIONNAIRE.md)）|
| **Evidence Sources / 證據來源** | L1 自評問卷 + L2 IT 提供之帳號清單 + **L3 OpenWebUI / API Gateway audit log（建議）** |

### B. 知識沉澱 / Knowledge Codification

| 項目 | 內容 |
| --- | --- |
| **Definition** | 個人經驗、Prompt、SOP、判斷邏輯，是否被系統化整理成「**可被別人重用**」的部門 / 公司資產 |
| **Observable Indicators** | (a) Skill Library 條數 (b) 每 Skill 是否有 Owner / 版本 / IPOE 文件 (c) Skill 被跨部門引用次數 (d) 新人 onboarding 時 Skill 使用率 |
| **Exclusions** | **不包含**：散落各處的「個人筆記」（無版本、無 Owner、無法被找到 ≠ 知識沉澱）|
| **Measurement Items** | 10 題 Q3、25 題 Q6-Q10、50 題 Q11-Q20 |
| **Evidence Sources** | L1 自評 + L2 Skill Library 文件 + **L3 Git commit history + Wiki 引用 log** |

### C. 流程自動化 / Process Automation

| 項目 | 內容 |
| --- | --- |
| **Definition** | AI 是否被接進實際業務流程（不僅是 demo），自動執行任務、降低人工重工，且**有 HITL 節點與 evidence trail** |
| **Observable Indicators** | (a) 上線 Workflow 數量 (b) Workflow 月執行次數 (c) Workflow uptime (d) HITL 節點覆蓋率 (e) 每 Workflow 是否有 Owner |
| **Exclusions** | **不包含**：RPA / Zapier 純規則自動化（無 AI 推理）、demo 階段未上線的 PoC |
| **Measurement Items** | 10 題 Q4-Q5、25 題 Q11-Q15、50 題 Q21-Q30 |
| **Evidence Sources** | L2 Workflow 設計文件 + **L3 n8n / orchestrator 執行 log + L5 流程 KPI 追蹤** |

### D. 系統整合 / System Integration

| 項目 | 內容 |
| --- | --- |
| **Definition** | AI 是否能與企業核心系統（Gmail / Sheets / Notion / CRM / API / ERP / DB）雙向、安全、可稽核地串接 |
| **Observable Indicators** | (a) 系統間整合點數量 (b) API 授權治理完整度 (c) 機敏資料 redact 覆蓋率 (d) 串接錯誤率 |
| **Exclusions** | **不包含**：人工 export / import 的「假整合」、無 API 授權管理的私接 |
| **Measurement Items** | 10 題 Q6-Q7、25 題 Q16-Q18、50 題 Q31-Q35 |
| **Evidence Sources** | L2 系統地圖 + **L3 API Gateway audit log + DLP alert log** |

### E. Agent 應用 / Agent Application

| 項目 | 內容 |
| --- | --- |
| **Definition** | 是否有可**拆解任務、呼叫工具、累積記憶、產生 briefing、執行回報、可追溯**的 AI Agent，並通過 HITL 與階段驗收 |
| **Observable Indicators** | (a) 上線 Agent 數量 (b) Agent 月任務數 (c) Reviewer 通過率 (d) Wiki 記憶條目數 (e) Agent 通過 4A-4E 階段驗收 |
| **Exclusions** | **不包含**：單次 chat session（無 Wiki 記憶 ≠ Agent）、demo Agent（未通過驗收 ≠ governed Agent）|
| **Measurement Items** | 10 題 Q8、25 題 Q19-Q22、50 題 Q36-Q43 |
| **Evidence Sources** | L2 Agent 設計文件 + **L3 Agent task log + Reviewer log + L5 Agent ROI 縱貫追蹤** |

### F. 執行導入與變革治理 / Implementation Governance

| 項目 | 內容 |
| --- | --- |
| **Definition** | 是否有**權限矩陣、Audit Log、資料分級、ROI 追蹤、變革管理、AI Ethics 檢核**等完整治理機制（對應 Stage 8）|
| **Observable Indicators** | (a) Permission Matrix 覆蓋率 (b) Audit Log 保存期 (c) Reviewer Workflow 啟用率 (d) 價值追蹤 5 維度上線 (e) Ethics Checklist 通過項數 |
| **Exclusions** | **不包含**：只有 AI Policy 文件但無實作（policy ≠ governance）|
| **Measurement Items** | 10 題 Q9-Q10、25 題 Q23-Q25、50 題 Q44-Q50 |
| **Evidence Sources** | L2 治理文件 + **L3 Audit Log + L4 第三方稽核報告 + L5 KPI 縱貫追蹤** |

> **學術紀律**：本 §3.1 表格是後續做信效度驗證的前提。任何問卷題目都應對應到此表的某個 construct 的 Measurement Items；任何分數變化都應對應到 Evidence Sources。

## 3.2 信效度驗證計畫（未來執行）

> 本評分模型的下一階段研究工作。需要實際樣本資料（至少 N=200 企業 / 500 受訪者）才能完成。詳見 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md)。

| 驗證項目 | 方法 | 目標值 | 狀態 |
| --- | --- | --- | --- |
| **內部一致性 Internal Consistency** | Cronbach's α（每構面內各題項相關係數）| α ≥ 0.70 acceptable, ≥ 0.80 good | 待執行 |
| **探索性因素分析 EFA** | 主成分分析；Varimax rotation；KMO ≥ 0.6, Bartlett p < 0.05 | 6 構面提取乾淨、構面間負荷 < 0.4 | 待執行 |
| **驗證性因素分析 CFA** | 結構方程模型；fit indices: CFI ≥ 0.90, TLI ≥ 0.90, RMSEA ≤ 0.08 | 6 因子模型 fit 顯著優於 1 因子 | 待執行 |
| **評分者間信度 Inter-rater Reliability** | Cohen's κ（兩位獨立顧問評分同一公司）| κ ≥ 0.60 substantial, ≥ 0.80 almost perfect | 待執行 |
| **效標關聯效度 Criterion Validity** | 評分與外部 KPI（如 AI ROI / 員工 NPS / 客訴回應）的相關 | r ≥ 0.30 | 待執行 |
| **預測效度 Predictive Validity** | T0 評分對 T+12 個月 KPI 改善的預測力 | β 顯著 (p < 0.05) | 待縱貫研究 |

⚠️ **目前狀態**：本評分模型為**專家共識版** (expert-consensus version)，0-4 量尺、區段門檻、構面劃分皆基於 Rosemann BPM 學派 + Tiger AI 實務歸納。**尚未完成上述心理計量驗證**。在學術發表時應標明本量表為 "expert-consensus, pending psychometric validation"。

## 3.3 區分：成熟度 (Maturity) 與準備度 (Readiness)

> **重要**：原 6 構面中混有「**output 側成熟度**」與「**input 側準備度 / 限制條件**」。為提高量表精準度，本版本明確區分：

### 成熟度（Maturity）── 你已經建立什麼

「**做出來的成果**」，反映組織已投入並產出的 AI 能力資產。

| 構面 | 例 |
| --- | --- |
| A. 工具使用 | 已上線的帳號 / 已寫的 Prompt |
| B. 知識沉澱 | 已建立的 Skill Library |
| C. 流程自動化 | 已上線的 Workflow |
| E. Agent 應用 | 已通過驗收的 Agent |
| F. 治理 | 已實作的 Audit / Permission |

### 準備度 / 限制條件（Readiness / Constraints）── 什麼讓你能 / 不能往前走

「**還沒做但會影響後續導入的條件**」，不算入 Maturity Score，但會影響 Phased Goals 設計（Tool 6.3 組織吸收力評估）。

| 構面 | 例 |
| --- | --- |
| IT FTE / 預算 | 影響 Phase 1-3 的人力與資源 |
| 資料敏感度 | 影響部署模式選擇（雲 / Hybrid / 地端）|
| 雲端政策 | 法規 / 母公司限制 |
| 變革容量 | 同時可推進的專案數 |
| 領導承諾 | Sponsor / Champion 是否就位 |
| 監管壓力 | 行業合規負擔 |

### 報告中如何呈現

報告同時產出**兩張雷達**：

- **Radar A**：AI Maturity Score（六構面 0-4 分）—— 量「已做的」
- **Radar B**：AI Readiness / Constraint Profile（七維 0-4 分）—— 量「環境條件」

> Stage 6 Phased Goals 設計時：Maturity 雷達告訴你「**該往哪走**」；Readiness 雷達告訴你「**走得多快**」。兩張缺一不可。

## 4. 單題分數量尺

所有問卷題目採 0-4 分。

| 分數 | 判斷標準 |
| --- | --- |
| 0 | 完全沒有，或不知道是否存在 |
| 1 | 有零星個人使用，但沒有標準或制度 |
| 2 | 部門內有初步做法，但尚未穩定複製 |
| 3 | 已有標準流程、共用資產或可重複執行做法 |
| 4 | 已制度化、可治理、可衡量，且能跨部門擴散 |

## 5. 成熟度判定方式

### 5.1 主成熟度

主成熟度採「最高穩定等級」判定。

一個等級被視為穩定，需要同時滿足：

- 該等級對應構面平均分數達 3 分以上。
- 前一等級能力不得低於 2.5 分。
- 執行導入與變革治理 構面不得低於 2 分。

### 5.2 局部成熟度

如果某個部門或場景已經達到更高等級，但公司整體尚未達標，標記為局部成熟度。

範例：

- 公司整體是 L2。
- 客服部門已有 n8n 串接 Gmail、CRM、Sheets 的 PoC。
- 可標記為「整體 L2，客服局部 L3」。

### 5.3 建議分數區間

| 總分區間 | 初步判定 |
| --- | --- |
| 0-20 | L0-L1：尚未形成穩定 AI 使用 |
| 21-40 | L1：個人 AI 使用階段 |
| 41-60 | L2：部門 Skill 化階段 |
| 61-78 | L3：Workflow 自動化階段 |
| 79-92 | L4：Agentic AI 初步運作 |
| 93-100 | L5：Agent Team 協作階段 |

註：總分只是初判，最終仍需參考主成熟度、局部成熟度與治理分數。

## 6. L1-L5 可觀察指標

### L1 Controlled AI Access

| 指標 | 觀察重點 |
| --- | --- |
| 統一入口 | 是否有 OpenWebUI 或企業核准的 AI 入口 |
| 使用頻率 | 員工是否每週穩定使用 AI 處理工作 |
| Prompt 能力 | 是否能寫出有效提問與輸出要求 |
| 使用規範 | 是否知道哪些資料不可輸入 AI |
| 個人效益 | 是否能提出時間節省或品質提升案例 |

### L2 Knowledge Codification

| 指標 | 觀察重點 |
| --- | --- |
| Skill 清單 | 是否有部門常用 Skill 名單 |
| 知識沉澱 | 是否把 Prompt、SOP、模板、案例整理成資產 |
| 共用機制 | 是否有 Notion、Git、文件庫或內部平台管理 |
| 新人上手 | 新人是否能直接套用 Skill 完成工作 |
| 品質一致 | 是否降低個人差異造成的品質落差 |

### L3 Workflow Automation

| 指標 | 觀察重點 |
| --- | --- |
| 流程盤點 | 是否知道哪些流程可被自動化 |
| 系統串接 | 是否串接 Gmail、Sheets、Notion、CRM、API、ERP |
| 自動觸發 | 是否有 Trigger、Webhook 或排程 |
| 人工審核 | 是否在關鍵節點保留人工確認 |
| 維運紀錄 | 是否有 Log、錯誤通知與重試機制 |

### L4 Autonomous Agent

| 指標 | 觀察重點 |
| --- | --- |
| 任務拆解 | Agent 是否能將目標拆成步驟 |
| 知識記憶 | 是否有 `purpose.md`、`SCHEMA.md`、Wiki、index、log |
| Ingest 閉環 | 是否能吃進文件、分析、寫回 Wiki 並更新索引 |
| Query / Update | 是否能用證據回答並保留回寫紀錄 |
| Briefing / Discovery | 是否能依 watchlist、queue、tasks 產生週期性 briefing |
| 工具調用 | Agent 是否能呼叫 Skill 與 Workflow |
| 權限邊界 | Agent 可做與不可做的事是否清楚 |
| 回報機制 | Agent 是否能回報結果、異常、下一步與 evidence |
| 人機協作 | 人是否能審核、修正、接手 Agent 任務 |

### L5 Multi-Agent Organization

| 指標 | 觀察重點 |
| --- | --- |
| 角色分工 | 是否有市場、產品、客服、財務等 Agent 角色 |
| 任務分派 | 是否能把企業級任務拆給多 Agent 協作 |
| 輸出整合 | 是否有整合 Agent 結果的角色或流程 |
| 品質檢查 | 是否有 Critic、Reviewer 或 HITL 人類審核 |
| 經營價值 | 是否支援跨部門決策、營運或創新任務 |

## 7. 部署模式評分

部署模式不等於成熟度，但會影響課程與導入路線。

| 構面 | 雲 AI 傾向 | Hybrid 傾向 | 全地端傾向 |
| --- | --- | --- | --- |
| 資料敏感度 | 低 | 中 | 高 |
| 雲端政策 | 可使用公有雲 | 部分可上雲 | 核心資料不得上雲 |
| IT 能力 | 弱 | 中 | 強 |
| 預算 | 低 | 中 | 高 |
| 系統型態 | SaaS 為主 | SaaS + 內部系統 | ERP/MES/DB/內網為主 |
| 法規要求 | 低 | 中 | 高 |

### 建議判斷

- 雲 AI：快速啟動，適合低敏感資料與行銷服務場景。
- Hybrid：多數企業首選，兼顧成本、能力、資料安全與落地速度。
- 全地端：適合高敏感資料、研發製造、金融、醫療、政府與強稽核場景。

## 8. 課程比例推薦邏輯

### 8.1 依成熟度推薦

| 初判成熟度 | L1 | L2 | L3 | L4 | L5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| L0-L1 | 40% | 35% | 20% | 5% | 0% |
| L1 | 30% | 35% | 25% | 10% | 0% |
| L2 | 15% | 30% | 40% | 10% | 5% |
| L3 | 5% | 20% | 35% | 30% | 10% |
| L4 | 5% | 15% | 25% | 30% | 25% |
| L5 | 0% | 10% | 20% | 30% | 40% |

### 8.2 依部署模式調整

- 雲 AI：增加 L1、L2 比例，L3 以 SaaS 串接為主。
- Hybrid：增加 L3 比例，強化資料分級、API、Credential 與人工審核。
- 全地端：增加治理、系統整合與 L3/L4 深度，案例偏 ERP、DB、內網、RAG。

### 8.3 依產業調整

- 研發製造業：增加 L2、L3、治理與內部系統案例。
- 行銷服務業：增加 L1、L2、L3 快速 PoC 與內容產出案例。
- 高敏感產業：增加資料分級、權限、稽核、人工審核與全地端架構。

## 9. 缺口分類

| 缺口類型 | 說明 | 常見補強方式 |
| --- | --- | --- |
| 工具缺口 | 沒有統一 AI 入口或授權工具 | L1 課程、OpenWebUI、使用規範 |
| Skill 缺口 | 個人經驗沒有沉澱 | L2 Skill Workshop、模板與知識庫 |
| Workflow 缺口 | 流程仍靠人工搬資料 | L3 n8n PoC、系統串接 |
| 系統串接缺口 | Gmail、Sheets、Notion、CRM、API、ERP 未整合 | API 盤點、Credential、資料路由 |
| Agent 缺口 | 沒有可自主執行任務的 AI | L4 Hermes Agent 任務設計 |
| Agent Team 缺口 | 跨部門任務無法多 Agent 協作 | L5 ClawTeam 情境設計 |
| 治理缺口 | 權限、稽核、ROI 不清楚 | 治理表、階段驗收關卡（Stage Gate）、KPI |
