# AI Governance 對齊：Tiger AI 方法論 vs 國際 AI 治理框架

> 🌐 English version: [AI_GOVERNANCE_ALIGNMENT_EN.md](AI_GOVERNANCE_ALIGNMENT_EN.md)
>
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技

更新日期：2026-05-16

---

> **本文回答**：Tiger AI 方法論跟國際 AI 治理框架（NIST AI RMF / EU AI Act / ISO/IEC 42001 / OECD AI Principles / 台灣 AI 基本法 / Singapore Model AI Governance）有什麼對應關係？董事會 / 法遵 / 監管者需要看到我們在每個框架的具體落點。
>
> 已對齊 BPM / 顧問框架 / AI 成熟度框架見 [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md)；**本文專注 AI Governance 維度**，特別針對 L4-L5 自主 AI 的制度可信度。

---

## 1. 為什麼 L4-L5 需要正式 AI Governance 對齊

L4 Autonomous Agent + L5 Multi-Agent Organization = AI 不在人類即時監督下執行業務動作。

董事會 / 監管者必問三題：

1. **誰擔責任**？AI 出事誰負法律 / 道德責任？
2. **怎麼預警**？高風險決策有什麼觸發人類介入的機制？
3. **怎麼稽核**？事後第三方能否獨立驗證 AI 行為合規？

這三題的答案必須對應到**國際公認治理框架**，才能在董事會、法遵、監管層面被接受。

---

## 2. 八階段 × 主流 AI Governance 框架對應總表

| 治理框架 | 來源 / 性質 | Tiger AI 方法論在哪幾個 Stage 對應 |
| --- | --- | --- |
| **NIST AI RMF (AI Risk Management Framework)** | 美國 NIST，2023 / 自願但廣泛採用 | Govern→Stage 8；Map→Stage 1-2；Measure→Stage 4 + 8；Manage→Stage 6-8 |
| **EU AI Act** | 歐盟，2024 通過 / 強制法規 | High-risk AI 對應 L4-L5；治理透明 → Stage 8 Audit；HITL → 全 Stage |
| **ISO/IEC 42001:2023 AI Management System** | 國際標準組織，2023 / 可認證 | AI 政策 → Stage 8；風險評估 → Stage 4 + 8；持續改善 → Phase C 季度 |
| **ISO/IEC 23894:2023 AI Risk Management** | 國際標準組織 / 風險聚焦 | Risk Register → Stage 8 |
| **OECD AI Principles** | OECD 加成員國 / 政策原則 | 5 大原則 → 對應 Tool 7.2 人機協作、Tool 8.8 Ethics |
| **台灣 AI 基本法（草案）** | 台灣立法院，審議中 | 對應台灣高合規行業客戶（金融 / 醫療 / 政府） |
| **Singapore Model AI Governance Framework** | 新加坡 IMDA / 自願 | 4 大支柱 → 對應 Stage 7 To-Be + Stage 8 |
| **US AI Bill of Rights** | 美國白宮 / 政策聲明 | 5 大保護 → 對應 Tool 8.8 Ethics + 客戶資料保護 |

---

## 3. NIST AI RMF（最重要的全球參考框架）

NIST AI RMF 是目前**最被企業實際採用**的 AI 治理框架。4 大核心 functions：

### 3.1 Govern（治理）

**NIST 要求**：建立組織級的 AI 政策、角色、責任、文化。

**Tiger AI 對應**：

- Stage 8 §12.1 RACI 矩陣（含 AI 議題的責任分配）
- Stage 8 Tool 8.8 AI Ethics Checklist 15 項（員工規範、IP、智財、偏見、incident response）
- 4 層架構 Layer 1 Governance（AI Policy / Ethics / Compliance / Risk Committee / Audit Owner）
- Tool 3.6 客戶 Ideal Practice 三方簽名 = 公司治理層級的書面承諾

### 3.2 Map（盤點）

**NIST 要求**：盤點 AI 系統的上下文、風險、利害關係人。

**Tiger AI 對應**：

- Stage 1 As-Is：訪談、Systems Inventory、AI Usage Inventory、Swimlane（全部都是 Map）
- Tool 2.2 Reference Model Mapping Worksheet
- Tool 2.6 Component Map + Tool 2.7 4 層架構

### 3.3 Measure（衡量）

**NIST 要求**：量化 AI 系統的性能、影響、風險。

**Tiger AI 對應**：

- Stage 2 雷達 0-4 評分
- Stage 4 Impact × Effort 矩陣
- Stage 8 Tool 8.5 價值追蹤矩陣（5 維度：時間 / 品質 / 規模 / 風險 / 資產）
- Tool 8.9 Evidence Hierarchy（L1-L5 證據強度）
- 季度 Gate C 雷達回頭核對

### 3.4 Manage（管理）

**NIST 要求**：執行風險緩解、監控、持續改善。

**Tiger AI 對應**：

- Stage 6 Phased Goals + Stage Gate Criteria
- Stage 7 人機協作架構 + HITL 節點明確化
- Stage 8 Tool 8.6 Risk Register（trigger + owner + mitigation）
- Stage 8 Tool 8.7 Audit Log（保存期 + reviewer）
- Phase C 24 個月季度 review

> **整體對應**：NIST AI RMF 的 4 functions 完整落點在 Tiger AI 8 階段，**可直接出 NIST 對應文件給監管者**。

---

## 4. EU AI Act（強制法規）

EU AI Act 將 AI 系統分為 4 風險等級：Unacceptable / High-risk / Limited / Minimal。

### 4.1 風險分類對應

| EU AI Act 等級 | Tiger AI L 級對應 | 治理要求 |
| --- | --- | --- |
| **Unacceptable**（社會評分、即時生物辨識等）| ❌ Tiger AI **拒絕協助** | — |
| **High-risk**（HR / 信用 / 醫療 / 教育 / 司法 / 關鍵基礎設施）| 多在 L4-L5 場景 | 強制風險評估 + transparency + human oversight + post-market monitoring |
| **Limited**（聊天機器人、deepfake）| 多在 L1-L3 場景 | 透明度義務（標明「AI 生成」）|
| **Minimal**（垃圾郵件過濾等）| 多在 L1-L2 場景 | 一般義務 |

### 4.2 High-risk AI 系統的 Article 對應

| EU AI Act Article | Tiger AI 對應 |
| --- | --- |
| **Art. 9 Risk Management System** | Stage 8 Tool 8.6 Risk Register（持續更新）|
| **Art. 10 Data Governance** | Tool 8.7 Audit Log + Tool 8.4 Permission Matrix |
| **Art. 11 Technical Documentation** | 完整 14 章顧問報告 + 4 層架構文件 |
| **Art. 12 Record-Keeping (logs)** | Tool 8.7 Audit Log 7 類事件 |
| **Art. 13 Transparency** | Tool 8.8 「AI 產出明示」+ 客戶 Ideal Practice 公開簽署 |
| **Art. 14 Human Oversight** | Tool 7.2 人機協作架構 + HITL 節點 + Reviewer Workflow |
| **Art. 15 Accuracy, Robustness, Cybersecurity** | Stage 8 Tool 8.5 價值追蹤（品質維度）+ Audit Log + Security |
| **Art. 17 Post-Market Monitoring** | Phase C 季度 Gate C + Stage 2 雷達回頭 + 5 維度價值追蹤縱貫 |
| **Art. 26 Quality Management System** | ISO/IEC 42001 對應（見 §5）|
| **Art. 72 Serious Incident Reporting** | Tool 8.8 Ethics §11「AI 系統 incident response 流程」 |

> **客戶在歐盟有業務時**：Tiger AI 方法論的交付物（完整 14 章報告 + 治理文件）可作為 EU AI Act 合規證據包。

---

## 5. ISO/IEC 42001:2023 AI Management System

ISO 42001 是首個**可被第三方認證**的 AI 管理系統標準。結構仿 ISO 9001 / 27001。

### 5.1 ISO 42001 結構對應

| ISO 42001 章節 | Tiger AI 對應 |
| --- | --- |
| **4. Context of the Organization** | Stage 1 As-Is + Stage 2 Reference Model |
| **5. Leadership** | Sponsor + AI Champion 角色定義（RACI）+ AI Policy 簽署 |
| **6. Planning** | Stage 5 Problem Definition + Stage 6 Phased Goals + Tool 6.3 吸收力 |
| **7. Support** | 變革管理 Playbook + 訓練計畫 + 資源規劃 |
| **8. Operation** | Stage 7 To-Be Operating Model + 人機協作 + HITL |
| **9. Performance Evaluation** | Tool 8.5 價值追蹤矩陣 + Tool 8.7 Audit Log + 季度 Gate C 雷達 |
| **10. Improvement** | Phase C 季度 review + Cases-as-Benchmarks 案例累積 |
| **Annex A Controls** | Tool 8.4 Permission + Tool 8.6 Risk + Tool 8.7 Audit + Tool 8.8 Ethics |

> **目標**：希望 ISO/IEC 42001 認證的企業，可拿 Tiger AI 方法論的交付物作為 management system 文件包。我們的方法論**完整覆蓋 ISO 42001 全部章節**。

---

## 6. OECD AI Principles（5 大原則）

OECD AI Principles 是 G20、APEC 廣泛採用的政策原則。

| OECD 原則 | Tiger AI 對應 |
| --- | --- |
| **1. Inclusive growth, sustainable development and well-being** | Stage 8 Tool 8.5 價值追蹤含「員工體驗」維度；變革管理含「升級角色非取代」 |
| **2. Human-centered values and fairness** | Tool 8.8 Ethics §9 偏見 / 歧視風險評估；Tool 7.2 HITL 必須存在 |
| **3. Transparency and explainability** | Tool 8.7 Audit Log + Tool 8.8 §7「AI 產出明示」+ 完整 evidence trail |
| **4. Robustness, security and safety** | Stage 8 Risk Register + Tool 8.4 Permission + 部署模式（Hybrid / On-Prem 三選一）|
| **5. Accountability** | RACI 矩陣 + 「**客戶簽署 Ideal Practice 三方簽名**」+ Reviewer 簽核機制 |

---

## 7. 台灣 AI 基本法（草案）

台灣立法院審議中的 AI 基本法（截至 2026/05）。Tiger AI 方法論已**對齊主要條文**：

| 草案重點 | Tiger AI 對應 |
| --- | --- |
| **AI 產品 / 服務需做風險分級** | Stage 1-2 識別 + 4 層架構 + Tool 8.6 Risk Register |
| **個資保護優於模型訓練** | Tool 8.8 §2 個資不外送 LLM / 經 redact；部署模式預設 On-Prem 高敏感 |
| **演算法透明度與可解釋性** | Tool 8.7 Audit Log + 8.8 §7 AI 明示標記 |
| **使用者權益保障** | Tool 8.8 §5 員工有權知道哪些工作被 AI 處理 |
| **業者責任歸屬** | RACI + Tool 8.8 §8 智財權歸屬釐清 |
| **政府監管權限** | Tool 8.7 Audit Log 保存期支援政府稽核 |

⚠️ 台灣 AI 基本法尚未通過。本對齊表將隨法案最終版本更新。

---

## 8. Singapore Model AI Governance Framework

新加坡 IMDA 提供的自願性 governance framework，4 大支柱：

| Singapore Pillar | Tiger AI 對應 |
| --- | --- |
| **1. Internal Governance Structures** | Layer 1 Governance + RACI |
| **2. Determining Level of Human Involvement** | Tool 7.2 人機協作架構（HITL 節點）|
| **3. Operations Management** | Tool 8.4-8.7 全套（Permission / Value / Risk / Audit）|
| **4. Stakeholder Interaction & Communication** | Tool 8.2 變革管理 Playbook + Stakeholder Map |

---

## 9. 監管 / 法遵交付物對應表

當客戶面對監管 / 法遵 / 內稽要求，Tiger AI 方法論的哪些交付物可直接提交：

| 監管 / 法遵需求 | 直接提交的 Tiger AI 交付物 |
| --- | --- |
| AI 風險評估 | Stage 4 Gap + Tool 8.6 Risk Register |
| AI 政策 | Tool 8.8 Ethics Checklist 15 項 + AI Policy 文件 |
| Audit 證據包 | Tool 8.7 Audit Log + 季度 Gate C 紀錄 + Stage 2 雷達前後對比 |
| 第三方稽核準備 | 完整 14 章顧問報告 + 4 層架構 + 4 份權威概念檔 |
| ROI / 效益佐證 | Tool 8.5 價值追蹤矩陣 5 維度 + 縱貫 KPI |
| Incident response 流程 | Tool 8.8 §12 + Tool 8.6 Risk Register trigger |
| 員工教育記錄 | 變革管理計畫訓練紀錄 + Tool 8.8 §14 |

---

## 10. 認證 / 標籤建議

依方法論 maturity，Tiger AI 客戶可考慮申請：

| 認證 | 適用 | 預估時程 |
| --- | --- | --- |
| **ISO/IEC 42001 AI Management System** | L3+ 客戶（已有完整治理）| 6-12 個月 |
| **ISO/IEC 27001 ISMS** | 所有客戶（資安基礎）| 6-12 個月 |
| **SOC 2 Type II** | 美國 / 跨國服務客戶 | 6-12 個月 |
| **EU AI Act CE Marking**（High-risk）| 歐盟業務 + High-risk AI 系統 | 12-24 個月 |

> Tiger AI 方法論的交付物可作為**認證準備的 90% 文件基礎**。實際認證需第三方稽核機構。

---

## 11. 相關文件

| 文件 | 與本文關係 |
| --- | --- |
| [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md) | 對齊顧問公司 / BPM / AI 成熟度框架；本文補上 AI Governance 維度 |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md) | 為什麼方法論經得起辯論 |
| [`FAILURE_PATTERNS.md`](FAILURE_PATTERNS.md) | 方法論的失敗模式與反例 |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Stage 8 | 治理工具表完整版 |

---

## 12. 引用文獻 / References

- NIST (2023). *AI Risk Management Framework (AI RMF 1.0)*.
- European Commission (2024). *Regulation on Artificial Intelligence (EU AI Act)*.
- ISO/IEC (2023). *ISO/IEC 42001:2023 — Artificial Intelligence Management System*.
- ISO/IEC (2023). *ISO/IEC 23894:2023 — Artificial Intelligence Risk Management*.
- OECD (2019, updated 2024). *OECD AI Principles*.
- The White House (2022). *Blueprint for an AI Bill of Rights*.
- Singapore IMDA (2020). *Model AI Governance Framework, 2nd Edition*.
- 立法院 (審議中). *人工智慧基本法草案*.

---

授權與引用 / License & Citation

本文為 Apache License 2.0；可使用、修改、商業利用，唯需保留 [`../NOTICE`](../NOTICE) 檔之署名。
