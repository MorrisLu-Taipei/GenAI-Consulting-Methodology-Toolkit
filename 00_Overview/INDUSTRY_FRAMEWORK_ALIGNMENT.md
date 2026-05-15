# Tiger AI 方法論與業界框架對齊圖

> 🌐 English version: [INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md)
>
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技

更新日期：2026-05-15

---

> **本文回答**：Tiger AI 方法論跟主流顧問公司（McKinsey / BCG / Bain / Deloitte / Accenture / PwC）、學派（Rosemann BPM / CMMI / APQC / SCOR / TOGAF / Dragon1）、AI 成熟度框架（Gartner / MIT / MMC / Forrester）有什麼對應關係？我們重複了什麼、補完了什麼、創新了什麼？
>
> **核心立場**：Tiger AI 不是另起爐灶，而是**整合主流工具、補完業界閉環、加入新時代 GenAI 必要元素**。所有引用的框架都已在 [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) 詳列；本文做的是「跨家對齊」。

---

## 1. 為什麼需要這份對齊

| 受眾 | 看完此文得到 |
| --- | --- |
| 大型企業 IT/CIO | 「原來這套方法論跟我們已採用的 TOGAF / ITIL / APQC 是相容的」 |
| 顧問業界跳槽者 | 「我從 BCG/Deloitte 來，看完知道哪些工具直接沿用、哪些有 Tiger AI 特色」 |
| 學術審稿 | 「Tiger AI 不是民科，是站在 Rosemann/CMMI/APQC 學派肩膀上」 |
| 監管者 | 「方法論引用的標準都是國際公認的，AI 治理符合既有 GRC 框架」 |
| 客戶高層 | 「我們花的錢買的是業界精華 + AI 時代必要補件，不是任何一家的私有方法」 |

---

## 2. 八階段 vs 主流顧問公司方法論對齊

### 2.1 跨家對齊總表

| Stage | Tiger AI | McKinsey | BCG | Bain | Deloitte | Accenture | PwC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1 As-Is Snapshot** | 40 題訪談 + Inventory + Swimlane | 7-Step Step 1: Define Problem | Diagnostic Survey | Customer / Process Diagnostics | Business Architecture Discovery | Living Business Diagnostic | Value Creation Diagnostic |
| **2 Reference Model** | APQC + Tiger AI L1-L5 + 4 層架構 | (極少做)| Capability Maturity Map | (非核心) | TOGAF Capability Assessment | Industry Reference Architecture | Capability Framework |
| **3 Best Practice → Ideal** | Benchmark + Ideal Practice 共創 | Best Practice Research | Strategic Position vs Industry | NPS / Customer Loyalty Benchmarks | Industry Pulse | Industry Benchmarking | Industry Outlook |
| **4 Gap Analysis** | M/B/R + Impact×Effort | Issue Tree + MECE | Importance-Performance Map | Pareto + Lean | Capability Gap Heatmap | Maturity Gap Analysis | Gap Map |
| **5 Problem Definition** | 80/20 + 5 Whys + EPS | Day-1 Answer + SCQ + Pyramid Principle | Strategic Diagnosis | Bain Question Pyramid | Hypothesis-Driven Approach | Outcome-Driven Definition | Issue-Tree Synthesis |
| **6 Phased Goals** | Phased Decomposition + Absorption | Workplan + Critical Path | Phased Transformation | Bain Way (Multi-phase) | Imagine-Deliver-Run | Wave Planning | Transformation Wave |
| **7 To-Be Design** | Phased To-Be + 人機協作 + HITL | To-Be Operating Model | Operating Model Design | Bain Way (Org Design) | Target Operating Model | Future-State Blueprint | Future Operating Model |
| **8 Implementation & Change** | Roadmap + 變革 + 價值追蹤 | McKinsey Influence Model + 7S | Smart Simplicity | Bain Results Delivery | Diamond Performance | Wired for Change | Project Delivery Framework |

### 2.2 各家強項對 Tiger AI 的補充意義

- **McKinsey** 的 MECE / Pyramid / Issue Tree **是 Tiger AI Stage 4-5 的工具來源**（已收錄在 Frameworks Library）
- **BCG** 的 Capability Maturity 思維**啟發 Tiger AI Stage 2 的 RM 評分**
- **Bain** 的 Customer / Process Diagnostics **跟 Tiger AI Stage 1 訪談題庫互補**
- **Deloitte** 的 Imagine-Deliver-Run **跟 Tiger AI Stage 6 三段 Phased Goals 高度對齊**
- **Accenture** 的 Wave Planning **跟 Tiger AI Phase 1/2/3 拆解思維一致**
- **PwC** 的 Value Creation Diagnostic **跟 Tiger AI Stage 8 價值追蹤矩陣對應**

> **結論**：八階段沒有一個是 Tiger AI 「發明」的概念。**創新在於：把這些散落各家的工具整合成有資料依賴、有客戶簽署、有閉環反證的完整推理鏈**。

---

## 3. Reference Model 學派對齊

### 3.1 Tiger AI 4 層架構 vs 主要 EA 框架

| 層 | Tiger AI | Dragon1 EA | TOGAF ADM | Zachman | ArchiMate |
| --- | --- | --- | --- | --- | --- |
| **L1 Governance** | AI Governance | Enterprise Governance | (Architecture Vision) | Scope (Contextual) | Motivation + Strategy |
| **L2 Business** | AI Business（L1-L5 在這層）| Business(es) | Business Architecture (B) | Business (Conceptual) | Business Layer |
| **L3 Information** | AI Information | Information Facilities & Systems | Data + Application (C+D) | System (Logical) | Application + Information |
| **L4 Technical** | AI Technical | IT Infrastructure(s) | Technology (E) | Technology (Physical) | Technology + Implementation |

**為什麼這麼對齊**：所有 EA 主流框架都收斂到「**4 個抽象層**」 —— 不是巧合，是「抽象度 × 變動頻率」這個科學軸的必然結果（見 [`METHODOLOGY_SCIENTIFIC_LOGIC.md`](METHODOLOGY_SCIENTIFIC_LOGIC.md) §5）。

### 3.2 Process Reference Model 對齊

| 用途 | Tiger AI 建議 | APQC PCF | SCOR | eTOM | ITIL | CMMI |
| --- | --- | --- | --- | --- | --- | --- |
| **跨產業流程結構** | APQC PCF（首選）| ✓ 13 Cat | — | — | — | — |
| **供應鏈 / 製造** | SCOR | — | ✓ 6 sections | — | — | — |
| **電信 / 訂閱服務** | eTOM | — | — | ✓ 3 levels | — | — |
| **IT 服務管理** | ITIL | — | — | — | ✓ 5 phases | — |
| **軟體研發成熟度** | CMMI | — | — | — | — | ✓ 5 levels |
| **AI 採用成熟度** | **Tiger AI L1-L5（自製，補業界缺）** | — | — | — | — | — |

> **業界既有 RM 沒有 AI 採用維度** —— 這就是 Tiger AI L1-L5 存在的必要性，並用 Tool 2.5 自評合格度 9/10 。

### 3.3 BPM 成熟度學派根源

| 概念 | 來源 | 在 Tiger AI 中的對應 |
| --- | --- | --- |
| Capability Maturity Levels（5 級量尺）| **Rosemann BPM Maturity** (QUT) + CMMI | Stage 2 評分 0-4、Tiger AI L1-L5 |
| Process Excellence Characteristics | Rosemann + APQC | Stage 3 卓越能力特徵 |
| Stage Gates | CMMI + Rosemann | Stage 6 階段驗收關卡 |
| Organizational Absorption | Rosemann（新興研究）| Tool 6.3 組織吸收力評估 |

> **學派致謝**：Prof. Michael Rosemann (QUT) 是本作者學歷指導教授，本方法論的 BPM 學派根源直接源自他的長期啟發與教學。

---

## 4. AI 成熟度框架對齊

### 4.1 主要 AI 成熟度框架對照

| 框架 | 級別 | Tiger AI L1-L5 對應 |
| --- | --- | --- |
| **Gartner AI Maturity Model** | Awareness / Active / Operational / Systemic / Transformational | L1 / L1+L2 / L3 / L4 / L5 |
| **MIT Sloan AI Capability** | Experimenters / Investigators / Pioneers / Empowerment | L1-L2 / L2-L3 / L3-L4 / L5 |
| **McKinsey AI Quotient (AIQ)** | (連續量尺，4 個 driver) | 對應 Tiger AI 六大構面 |
| **Capgemini DELTA Maturity** | Data / Enterprise / Leadership / Targets / Analysts | 對應 Tiger AI 治理 + 部署軸 |
| **Forrester AI Pulse Index** | (3 個 ring：People / Process / Tech) | 對應 Tiger AI 4 層架構 |
| **Tiger AI L1-L5** | L1 Chat / L2 Skill / L3 Workflow / L4 Auto Agent / L5 Agent Team | （**規模軸 L1-L3 + AI 自主軸 L4-L5 兩條軸**）|

### 4.2 Tiger AI L1-L5 對主流 AI 框架的補充

| 補充點 | 為什麼業界沒有 | Tiger AI 怎麼補 |
| --- | --- | --- |
| **明確的工具對應** | Gartner / MIT 抽象描述各級，無工具落點 | L1=OpenWebUI、L2=Antigravity、L3=n8n、L4=Hermes、L5=ClawTeam |
| **規模軸 vs 自主軸分離** | 業界混在一起，導致 L4-L5 描述模糊 | 規模軸（人主導）vs 自主軸（AI 主導），關鍵分界 L3→L4 |
| **GenAI 特定（非傳統 ML）** | 多數框架還停在傳統 ML / 預測模型 | 完全聚焦 LLM / Agent / Workflow 範式 |
| **可驗證的階段驗收** | 業界框架多為 self-assessment 量表 | 每級有 Stage Gate Criteria 可被獨立驗證 |
| **跨 RM 雙座標** | 業界框架單軸 | Tiger AI 跟產業 RM（APQC/SCOR）正交，給雙雷達 |

---

## 5. 經典分析工具對齊（已收在 Frameworks Library）

### 5.1 戰略分析工具

| 工具 | 來源 | 在 Tiger AI 中的對應 Stage |
| --- | --- | --- |
| Porter's 5 Forces | Harvard / Porter (1979) | Stage 3 Industry Position |
| PESTEL | Aguilar (1967) | Stage 3 macro context |
| BCG Growth-Share Matrix | BCG (1970s) | Stage 3 portfolio strategy |
| SWOT | Stanford (1960s) | Stage 3 + Stage 4 |
| Blue Ocean Strategy | INSEAD / Kim & Mauborgne | Stage 7 future positioning |
| Wardley Map | Simon Wardley | Stage 6 + 7 evolution path |

### 5.2 問題分析工具

| 工具 | 來源 | 在 Tiger AI 中的對應 Stage |
| --- | --- | --- |
| MECE | McKinsey (Minto) | Stage 2 + 4 紀律 |
| Issue Tree / Logic Tree | McKinsey | Stage 4 + 5 |
| Pyramid Principle | Minto (1985) | Stage 5 報告寫作 |
| SCQ (Situation-Complication-Question) | Minto | Stage 5 Problem Statement |
| 5 Whys | Toyota / Ohno | Stage 5 根因 |
| Fishbone (Ishikawa) | Kaoru Ishikawa | Stage 4 + 5 根因分類 |
| Hypothesis-Driven | McKinsey | Stage 1-5 全程 |
| 80/20 (Pareto) | Pareto / Juran | Stage 5 收斂 |

### 5.3 變革管理工具

| 工具 | 來源 | 在 Tiger AI 中的對應 Stage |
| --- | --- | --- |
| Kotter 8 Steps | Harvard / Kotter (1996) | Stage 8 變革管理 |
| ADKAR | Prosci / Hiatt | Stage 8 個人變革 |
| Stakeholder Map | Mendelow | Stage 8 利害關係人 |
| RACI | (源頭多家) | Stage 8 角色分工 |
| McKinsey Influence Model | McKinsey | Stage 8 抗拒處理 |
| 7S Framework | McKinsey | Stage 2 + 8 內部一致性 |

### 5.4 財務 / ROI 工具

| 工具 | 來源 | 在 Tiger AI 中的對應 Stage |
| --- | --- | --- |
| NPV / IRR | 傳統財務 | Stage 8 投資評估 |
| Payback Period | 傳統財務 | Stage 8 |
| Break-Even Analysis | 傳統財務 | Stage 8 |
| Sensitivity Analysis | 傳統財務 | Stage 8 + Risk Register |
| Balanced Scorecard | Kaplan & Norton (1992) | Stage 8 多維度追蹤 |
| OKR | Intel / Google | Stage 6 + 8 |

---

## 6. Tiger AI 獨有 / 創新元素

雖然絕大多數工具都來自業界既有，Tiger AI 有以下**獨有 / 整合創新**：

| 創新點 | 為什麼業界沒有 | Tiger AI 的設計 |
| --- | --- | --- |
| **Tiger AI L1-L5 GenAI 採用 Reference Model** | 業界 RM 還停在 IT / 傳統 ML | 第一個專門為 LLM/Agent/Workflow 設計的 RM，符合 Tool 2.5 十大條件 9/10 |
| **客戶 Ideal Practice 共創 Workshop** | 業界做 Best Practice 對標，但很少做客戶簽署的 Ideal | Tool 3.6：客戶**自己簽名**的 Ideal，無法否認後續推理 |
| **Cases-as-Benchmarks 9 欄位格式** | 業界案例多為敘事，無法計算差距 | Tool 3.5：案例強制 9 欄位俱全，客戶 30 分鐘自助算差距 |
| **季度回頭核對 Stage 2 雷達閉環** | 業界 Roadmap 多為線性，無自我反證機制 | Phase C 每季 Gate C 必做雷達回看，驗證結構真的變圓 |
| **3 階段合約模型 + Gate A/B/C 退場點** | 業界多為 fixed-scope 大合約 | Phase A 診斷 / Phase B 策略 / Phase C 落地，客戶可分階段決策 |
| **規模軸 vs AI 自主軸正交** | 業界混在一條軸上 | L1-L3 規模 + L4-L5 自主，關鍵分界 L3→L4 |
| **4 層 Reference Model × L1-L5 雙座標** | 業界單軸（要嘛 RM 要嘛 maturity）| Tiger AI 強制雙軸交叉 mapping |
| **HITL 節點明確化到每 Process** | 業界談 governance，少談具體 HITL 在哪 | Tool 7.2 每個 process 明確標 HITL 節點 + 驗收標準 |

---

## 7. 客戶常問：你跟我們現有的方法論衝突嗎？

### 7.1 客戶用 TOGAF / Zachman

**不衝突**。Tiger AI 4 層架構**直接對齊 TOGAF 的 BDAT**（Business/Data/Application/Technology）。可以說：「我們在 TOGAF 既有架構之上，加入 GenAI 採用維度（L1-L5）跟季度雷達閉環。」

### 7.2 客戶用 ITIL

**不衝突**。Tiger AI Stage 8 的 Audit Log / Permission Matrix / Risk Register 跟 ITIL Service Operation 直接對接。可以說：「我們補上 GenAI 特定的 LLM call log、Reviewer simulation、Skill 版本治理。」

### 7.3 客戶用 CMMI

**不衝突**。Tiger AI L1-L5 跟 CMMI 5 級**異曲同工** —— 都是 capability maturity 學派延伸。可以說：「CMMI for AI 是業界正在發展的方向；Tiger AI L1-L5 是其中一個落地版。」

### 7.4 客戶用 BCG / McKinsey / Bain 的內部框架

**不衝突，反而強化**。Tiger AI 引用了這些框架的核心工具（Issue Tree、MECE、Pyramid、Bain Way）。可以說：「我們不取代您的策略諮詢方法論；我們補上 GenAI 採用閉環和 4 層 Reference Model。」

### 7.5 客戶用 Gartner / Forrester AI Maturity

**不衝突，更具體**。Tiger AI L1-L5 比 Gartner 的 5 級**更具落地工具**（L1=OpenWebUI 等）。可以說：「Gartner 講『Operational AI』，我們講『n8n Workflow 3 條上線 + Reviewer 簽核率 95%』。」

---

## 8. 學術引用對齊

本方法論引用以下學術 / 業界文獻（在每個對應檔案的 References 已標）：

### 8.1 BPM / 成熟度學派

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT. **（核心理論根源）**
- Rosemann, M., zur Muehlen, M. (Eds.). *Business Process Management Maturity Models*.
- Paulk, M. et al. (1993). *Capability Maturity Model for Software*. CMU/SEI.
- Curtis, B., Hefley, B., Miller, S. (2009). *People CMM*. CMMI Institute.

### 8.2 Reference Model / Enterprise Architecture

- APQC (2024). *Process Classification Framework Version 7.3*.
- APICS (now ASCM). *SCOR Reference Model*.
- TM Forum. *eTOM Business Process Framework*.
- ISACA. *COBIT / ITIL Framework*.
- The Open Group. *TOGAF Standard Version 9.2*.
- Zachman, J. *Zachman Framework for Enterprise Architecture*.
- Dragon1. *Enterprise Architecture Reference Model*. <https://www.dragon1.com/reference-models/enterprise-architecture-reference-model>

### 8.3 顧問方法論

- Minto, B. (2009). *The Pyramid Principle: Logic in Writing and Thinking*.
- Rasiel, E. (1999). *The McKinsey Way*.
- Bain & Company. *Bain Way / Results Delivery*.
- Iansiti, M., Lakhani, K. (2020). *Competing in the Age of AI*. HBR Press.

### 8.4 變革管理

- Kotter, J. (1996). *Leading Change*. HBR Press.
- Hiatt, J. (2006). *ADKAR: A Model for Change in Business, Government and our Community*. Prosci.
- Mendelow, A. (1991). *Stakeholder Mapping*.

### 8.5 GenAI 採用 / AI Strategy

- Gartner. *AI Maturity Model*.
- Davenport, T., Mittal, N. (2022). *All-in on AI: How Smart Companies Win Big with Artificial Intelligence*. HBR Press.
- Brynjolfsson, E., McAfee, A. (2014). *The Second Machine Age*.
- Sweeney, J., Davenport, T. (2018). *AI Maturity Model*. MIT Sloan / Deloitte.

---

## 9. 結語：站在巨人肩膀上 + 補完業界閉環

Tiger AI 方法論的設計哲學：

1. **不重複造輪子**：策略分析（McKinsey）、變革管理（Kotter）、財務工具（NPV/IRR）、EA 框架（TOGAF/Dragon1）—— 用業界既有最好的
2. **整合 + 閉環**：把散落各家的工具串成有資料依賴、有客戶簽署、有反證機制的完整推理鏈
3. **補完 GenAI 缺口**：業界框架還沒跟上 LLM / Agent / Workflow 時代 → Tiger AI L1-L5 + 4 層架構 + Cases-as-Benchmarks + HITL 設計補上
4. **可被他人複製**：Apache 2.0 + GitHub + 學術引用清楚 → 不是任何一家的私有資產

> **這就是「站在巨人肩膀上 + 補完業界閉環」的意義** —— 客戶買的不是任何一家的私有方法，而是業界精華的整合 + GenAI 時代必要補件。

---

## 10. 相關文件

| 文件 | 與本文關係 |
| --- | --- |
| [`METHODOLOGY_SCIENTIFIC_LOGIC.md`](METHODOLOGY_SCIENTIFIC_LOGIC.md) §8 | 包含本文 §2 的精簡版（與 McKinsey/BCG/Gartner/MIT 對照）|
| [`EIGHT_STAGE_FLOW_STORY.md`](EIGHT_STAGE_FLOW_STORY.md) | 八階段在實際顧問流程中如何跑 |
| [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) | 50+ 框架庫詳細收錄（本文做的是「對齊地圖」、Frameworks Library 是「框架辭典」）|
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) | 每階段的具體工具表 |

---

授權與引用 / License & Citation

本文為 Apache License 2.0；可使用、修改、商業利用，唯需保留 [`../NOTICE`](../NOTICE) 檔之署名。
