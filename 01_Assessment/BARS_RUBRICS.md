# BARS 行為錨定評分量表：六大構面 × 0-4 分

> 🌐 English version: [BARS_RUBRICS_EN.md](BARS_RUBRICS_EN.md)
>
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技

更新日期：2026-05-16

---

> **本文目的**：把 6 構面 × 0-4 分的量表從「抽象級別」升級為**行為錨定評分量表 (Behaviorally Anchored Rating Scales, BARS)**，讓任何顧問評同一家公司都能得到**接近一致**的分數（提升 inter-rater reliability）。
>
> **學術依據**：BARS 源自 Smith & Kendall (1963)，是組織行為與績效評估領域提升評分一致性的標準方法。每個分數有具體可觀察的行為描述，避免主觀「感覺評分」。
>
> **應用**：本表是 [`AI_MATURITY_SCORING_MODEL.md`](AI_MATURITY_SCORING_MODEL.md) §3.1 Construct Definition 的執行細則，也是 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) Inter-rater Reliability 驗證的依據。

---

## 1. 使用紀律

| 紀律 | 說明 |
| --- | --- |
| **依行為描述評分，不依印象** | 看到具體行為「有 / 無」就打分，不憑感覺 |
| **不能在兩級之間** | 0/1/2/3/4 五個整數值，不接受 0.5 / 1.5 |
| **以**最低未滿足**等級為實際分數** | 例：3 分要求 (a) (b) (c) (d) 都有，缺 (d) 就只給 2 分 |
| **證據必須對應 Tool 8.9 Evidence Level** | 高分（3-4）必須有 L3+ 系統 log 或 L4+ 第三方稽核 |
| **跨評分者爭議解法** | 找第三評分者；若 3 人皆不同，回頭看「最低未滿足等級」紀律 |

---

## 2. 構面 A：工具使用 / Tool Usage

| 分數 | 行為錨點 (Behavioral Anchor) | 必要證據 (Required Evidence) |
| --- | --- | --- |
| **0** | 公司**無**統一 AI 工具入口；員工**無**公司 AI 帳號；無使用紀錄；可能有員工私下用 ChatGPT 但無治理 | L1 訪談 + 影子 IT 觀察（無公司帳號名單） |
| **1** | 有零星員工自費使用 AI；**部分主管**有公司帳號（≤ 20% 員工）；**無使用規範**或規範未簽署 | L2 IT 帳號清單 + AI 使用情況訪談 |
| **2** | 有公司 AI 工具入口；**部分部門**（≥ 1 個）已開通帳號（20-60% 員工）；**有簡易使用規範文件**（未必簽署）；有零星 Prompt 紀錄 | L2 帳號清單 + 使用規範文件 |
| **3** | **全員**或**大多數部門**（≥ 60%）開通帳號；**AI 使用規範已簽署**（≥ 90% 簽署率）；**Prompt Library 上線**（≥ 30 條入庫，有 Owner）；**月度活躍使用 ≥ 50% 員工**；**影子 IT 比例 ≤ 10%** | L3 OpenWebUI / API Gateway audit log + Prompt Library Git |
| **4** | L3 全部條件達成 + **跨部門複用率 ≥ 50%**（同 Prompt 被 ≥ 2 部門使用）+ **權限矩陣完整**（角色 × 資源 × 動作矩陣）+ **每年至少 1 次員工教育稽核完成**+ **第三方稽核通過**或 ISO/IEC 42001 認證 ready | L4 第三方稽核報告 + Audit Log |

---

## 3. 構面 B：知識沉澱 / Knowledge Codification

| 分數 | 行為錨點 | 必要證據 |
| --- | --- | --- |
| **0** | 完全**無** Skill Library / Wiki / SOP；個人經驗散在私人筆記、Slack DM、口耳相傳 | L1 訪談 + 系統盤點（無 Wiki 系統） |
| **1** | 個別員工有自己的「**個人 Prompt 集**」（散在筆記）；無 Owner / 無版本 / 無法被別人找到 | L2 訪談 + 抽樣員工筆記 |
| **2** | **單一部門**（≥ 1 個）有部門 Skill 集（≥ 5 條）；**有 Owner**但**版本治理不完整**；**他部門無法直接複用** | L2 部門 Wiki / SharePoint |
| **3** | **跨部門 Skill Library 上線**；**每 Skill 有 Owner + 版本 + IPOE 文件**；**Git commit history 可追溯**；**每月新增 ≥ 10 條**；**跨部門引用發生**（同 Skill 被 ≥ 2 部門引用） | L3 Git commit log + Wiki access log |
| **4** | L3 全部條件 + **每月新增 ≥ 20 條** + **新人 onboarding 時 Skill Library 使用率 ≥ 80%** + **Skill 自動引用機制**（Workflow / Agent 自動拉 Skill 不需人工指定）+ **退役員工 Skill 不流失**（離職前 SOP 強制 review） | L3-L4 Wiki 引用 log + 新人訪談 |

---

## 4. 構面 C：流程自動化 / Process Automation

| 分數 | 行為錨點 | 必要證據 |
| --- | --- | --- |
| **0** | **所有流程皆人工執行**；無自動化工具；無 log；無 Workflow 概念 | L1 訪談 + 系統盤點 |
| **1** | 個人或單一部門用**腳本 / Excel 巨集 / Power Automate** 處理局部任務；**無 AI 推理**；**無 HITL 節點**；無正式 Owner | L2 抽樣腳本 |
| **2** | **有少數 Workflow**（≥ 1 個含 AI 步驟）但**不穩定 uptime < 95%**；**無正式 Owner 或 log**；**Demo 階段，未真正進入業務流程** | L2 Workflow 設計文件 |
| **3** | **跨系統 Workflow ≥ 3 個上線**（含 trigger / log / HITL 節點）；**每 Workflow 有 Owner**；**uptime ≥ 95%**；**錯誤處理 + 重試機制就位**；**月執行量 ≥ 100 次** | L3 n8n / orchestrator 執行 log |
| **4** | L3 全部條件 + **Workflow ≥ 10 個** + **版本控管 (Git)** + **KPI 追蹤縱貫資料**（≥ 6 個月）+ **跨部門擴散使用** + **錯誤率 < 1%** + **Reviewer 簽核率 ≥ 95%** | L3-L5 系統 log + 縱貫 KPI |

---

## 5. 構面 D：系統整合 / System Integration

| 分數 | 行為錨點 | 必要證據 |
| --- | --- | --- |
| **0** | 各系統（Gmail / Sheets / CRM / ERP）**完全孤島**；所有資料**人工 export / import** | L1 訪談 + 系統地圖 |
| **1** | **個別系統間有手動整合**（如 IT 寫 cron job 跑 CSV 搬資料）；**無 API 授權治理**；**機敏資料無 redact** | L2 系統盤點 + 抽樣 |
| **2** | **少數系統有 API 整合**（≥ 2 個系統互通）；**API 授權靠個人帳號**；**有簡易 redact 規則但未涵蓋所有系統** | L2 整合文件 + DLP 抽樣 |
| **3** | **核心系統皆有 API 治理**（≥ 5 個系統互通，OAuth / SSO）；**API Gateway 上線**（rate limit + auth log）；**機敏資料 redact 覆蓋率 ≥ 80%**；**串接錯誤率 < 5%** | L3 API Gateway audit log + DLP alert log |
| **4** | L3 全部條件 + **redact 覆蓋率 100%** + **零信任架構 (Zero Trust)** + **第三方安全稽核通過**（SOC 2 / ISO 27001）+ **資料分級 (Data Classification) 完整** | L4 第三方稽核報告 |

---

## 6. 構面 E：Agent 應用 / Agent Application

| 分數 | 行為錨點 | 必要證據 |
| --- | --- | --- |
| **0** | **無任何 AI Agent 概念**；可能有 chatbot 但**無 Wiki 記憶 / 無多步推理 / 無工具呼叫** | L1 訪談 |
| **1** | **有 Agent demo**（≤ 5 個任務）但**未進入業務流程**；**無 Reviewer 機制**；**無持久 Wiki 記憶** | L2 Agent demo 文件 |
| **2** | **有 1 個 Agent 上線**（執行單一場景，如 FAQ 回覆）；**有 HITL Reviewer**；**有 task log**；**月任務 ≥ 20 次**；**未通過 Stage Gate 4A-4E 全部驗收** | L3 Agent task log + Reviewer log |
| **3** | **≥ 1 個 Agent 通過 4A-4E 全驗收**；**Wiki ingest/query/update 都跑通**；**月任務 ≥ 100 次**；**Reviewer 通過率 ≥ 85%**；**Evidence trail 完整**（input → process → output → log） | L3 Agent log + Wiki audit |
| **4** | L3 全部條件 + **≥ 2 個 Agent 上線** + **跨 Agent 任務串接** + **L5 ClawTeam 跨部門演練成功 ≥ 1 次** + **Reviewer 通過率 ≥ 95%** + **Agent ROI 縱貫追蹤** | L3-L5 系統 log + 縱貫 KPI |

---

## 7. 構面 F：執行導入與變革治理 / Implementation Governance

| 分數 | 行為錨點 | 必要證據 |
| --- | --- | --- |
| **0** | **無 AI Policy**；**無權限矩陣**；**無 Audit Log**；**無資料分級**；無 AI Champion / Sponsor 角色 | L1 訪談 |
| **1** | **有口頭 AI 規範**（未書面）；**Sponsor 確定**（CEO / CIO）；**無 Champion**；**權限混亂** | L2 訪談 + Sponsor 確認 |
| **2** | **有 AI Policy 文件**（已書面但簽署率 < 50%）；**AI Champion 兼任**；**部分系統有 Audit Log**；**Risk Register 存在但更新頻率低** | L2 Policy 文件 + Champion 確認 |
| **3** | **Policy 簽署率 ≥ 90%** + **Permission Matrix 完整** + **Audit Log 涵蓋所有 LLM 呼叫**（保存 ≥ 90 天） + **價值追蹤 5 維度上線** + **Ethics Checklist 通過 ≥ 12/15 項** + **季度 Risk Register review** | L3 Audit Log + L4 內稽報告 |
| **4** | L3 全部條件 + **ISO/IEC 42001 / 27001 認證 ready 或已認證** + **EU AI Act 對齊**（若有歐盟業務）+ **第三方稽核年度通過** + **Ethics Checklist 100% 通過** + **AI Incident response 演練 ≥ 1 次/年** | L4 第三方認證 + L5 縱貫稽核 |

---

## 8. 評分一致性檢核 (Inter-Rater Calibration)

### 8.1 雙評分者校準練習

新顧問加入或評分前，**A / B 兩位顧問**各自獨立評同一家「教學模擬」公司，然後比對：

```
Step 1: A 評 → 不告知 B
Step 2: B 評 → 不告知 A
Step 3: 比對 6 構面分數
Step 4: 若任一構面差距 ≥ 2 → 開檢討會（多半是行為錨點理解不一致）
Step 5: 校準後再評下一家
```

**目標**：Cohen's κ ≥ 0.60（substantial agreement）。詳見 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) §3。

### 8.2 常見評分爭議

| 情境 | 處理原則 |
| --- | --- |
| 客戶說「有」但實際看不到證據 | 依「**最低未滿足等級**」打分（即不給高分）|
| 部門有但全公司沒有 | 主成熟度給「整體分」；局部成熟度標註「客服部 L3 / 全公司 L1」 |
| 工具有但治理缺 | 治理是 F 構面；不影響 A-E 構面 |
| 員工會用但企業未開帳號 | A 構面降一級（個人能力 ≠ 企業成熟度）|

---

## 9. BARS 對 Tiger AI 方法論的意義

| 目標 | 達成方式 |
| --- | --- |
| **提升 Inter-rater Reliability** | 用具體行為描述取代主觀判斷 → 不同顧問評分接近一致 |
| **降低客戶質疑** | 客戶看評分依據是「行為清單」而非「顧問印象」→ 不可挑戰 |
| **支撐 Pilot Study Cohen's κ ≥ 0.60** | BARS 是達成此目標的核心機制 |
| **降低新顧問 onboarding 時間** | 看 BARS 表就知道如何評分，不需資深顧問師徒制 |
| **為 ISO/IEC 42001 認證做準備** | 認證機構要看「評估方法的客觀性」，BARS 是業界公認標準 |

---

## 10. 引用文獻 / References

- Smith, P. C., & Kendall, L. M. (1963). Retranslation of expectations: An approach to the construction of unambiguous anchors for rating scales. *Journal of Applied Psychology*, 47(2), 149-155.
- Schwab, D. P., Heneman, H. G., & DeCotiis, T. A. (1975). Behaviorally anchored rating scales: A review of the literature. *Personnel Psychology*, 28(4), 549-562.
- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.

---

授權與引用 / License & Citation

本文為 Apache License 2.0；可使用、修改、商業利用，唯需保留 [`../NOTICE`](../NOTICE) 檔之署名。
