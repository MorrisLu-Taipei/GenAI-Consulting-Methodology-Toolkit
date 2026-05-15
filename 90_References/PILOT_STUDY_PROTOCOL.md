# Pilot Study Protocol：Tiger AI 方法論的實證驗證研究計畫

> 🌐 English version: [PILOT_STUDY_PROTOCOL_EN.md](PILOT_STUDY_PROTOCOL_EN.md)
>
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技

更新日期：2026-05-16
版本：v1.0 研究設計協議（pre-registration ready）

---

> **本文目的**：把 Tiger AI 方法論從「漂亮的顧問框架 (well-designed methodology)」進化到「可被學術研究的模型 (researchable model)」。本協議定義一份 18-24 個月、5-10 家企業的實證 pilot study，**讓方法論被外部反證、而非僅自證**。
>
> 本文是**研究設計文件 (research protocol)**，可直接提交 IRB / 學術期刊 pre-registration / 政府研究補助申請。

---

## 1. 研究背景與動機 / Background & Motivation

### 1.1 為什麼需要實證研究

Tiger AI 方法論目前的證據強度：

| 元素 | 證據等級 (Tool 8.9) | 狀態 |
| --- | --- | --- |
| 八階段流程設計 | L2 文件論證 | 已完成（Rosemann BPM 學派 + 業界框架整合）|
| 6 構面 × 0-4 量尺 | L2 專家共識 | 已完成（**未做信效度驗證**）|
| 7 案例庫 | L2 匿名合成 | 已完成（**非真實 longitudinal 資料**）|
| 方法論自評合格 (Tool 2.5) | L1 自評 | 已完成（**self-referential, 非外部驗證**）|
| 跨顧問評分一致性 | — | **未做** |
| 縱貫 KPI 對方法論的回應 | — | **未做** |

**結論**：方法論在「**內部一致性 + 邏輯閉環**」已成熟，但「**外部可重複性 + 預測效度**」尚未實證。本 pilot study 補上這兩塊。

### 1.2 研究問題 (Research Questions)

**RQ1** ── **Inter-rater Reliability**：不同顧問用同套方法評同一家公司，能得到一致的成熟度評分嗎？

- **H1**：Cohen's κ ≥ 0.60（substantial agreement）

**RQ2** ── **Internal Consistency**：6 構面量表的內部一致性如何？

- **H2**：每個 construct 的 Cronbach's α ≥ 0.70

**RQ3** ── **Construct Validity**：6 構面在因素分析中是否清晰浮現？

- **H3a**：EFA 主成分分析提取 5-6 個因子，每題在歸屬因子上負荷 ≥ 0.5
- **H3b**：CFA 6 因子模型 fit 指標 CFI ≥ 0.90, TLI ≥ 0.90, RMSEA ≤ 0.08

**RQ4** ── **Predictive Validity**：T0 評分能否預測 T+12 個月的業務 KPI 改善？

- **H4**：控制基期 KPI 與企業規模後，Tiger AI maturity score 與 +12m KPI 改善幅度顯著正相關（β ≥ 0.30, p < 0.05）

**RQ5** ── **Longitudinal Pattern**：跑完 24 個月 Phase C 的企業，雷達圖是否真的變「圓」？

- **H5**：T0 vs T24 的雷達面積（6 構面總和）顯著增加，且每個構面的提升符合 Tool 6.1 預設拆解路徑（基礎 → 優化 → 卓越）

---

## 2. 研究設計 / Study Design

### 2.1 設計類型

- **Mixed-methods longitudinal study**
- **Convergent parallel design**：量化（量表評分、KPI）+ 質化（半結構訪談、案例研究）同時進行
- **Pre-registered**（公開研究假設、抽樣方法、分析計畫，避免 p-hacking）

### 2.2 樣本

| 項目 | 規範 |
| --- | --- |
| **目標樣本量 N** | 5-10 家企業（pilot 階段；後續主研究 N=200+ 才能做 CFA）|
| **產業多元性** | 至少 3 個產業（製造、服務、公部門各 ≥ 1 家）|
| **公司規模** | 100-5000 員工 |
| **AI 起點** | L0-L2（已 L3+ 的企業排除，因介入空間小）|
| **承諾參與時長** | 18 個月（簽研究合作協議）|
| **誘因** | 免費 / 折扣顧問服務 + 共同 publication 機會 + 案例匿名披露主導權 |

### 2.3 招募策略

1. 透過 n8n Taipei 大使社群、台科大智慧製造所、QUT 校友網
2. 公開徵求書 + Apache 2.0 開源 repo 作為信任佐證
3. 簽署研究合作協議（含資料使用、匿名化、退場機制）

### 2.4 倫理審查 / IRB

- 申請台科大或 QUT 倫理審查委員會 IRB approval
- 知情同意 (informed consent)：所有受訪者書面同意
- 機敏資料處理：個資 / 商業機密分級；雙盲評分階段資料隔離
- 退場權：任何企業隨時可退出，已收集資料予以歸還或銷毀

---

## 3. 雙盲評分設計 / Double-Blind Scoring Design

### 3.1 目的

驗證 Tiger AI 評分模型的 **inter-rater reliability**（評分者間一致性）。

### 3.2 設計

```
T0 評分階段（每家企業）：
  ↓
  Consultant A 獨立完成：
    • 訪談（依 Tool 1.1 40 題題庫）
    • Inventory + Swimlane（Tool 1.2-1.4）
    • Reference Model Mapping（Tool 2.2）
    • 6 構面 0-4 評分（依 Tool 2.3）
    • 主成熟度判定（L1-L5）
  ↓
  Consultant B 獨立完成（同一家企業，互不知對方結論）：
    • 重複以上所有動作
  ↓
  研究員（中立角色）比對 A 與 B 的：
    • 6 構面分數差距（kappa weighted）
    • 主成熟度判定一致性（unweighted kappa）
    • 缺口識別重疊度（M/B/R 表的 overlap）
```

### 3.3 一致性檢定統計

| 指標 | 公式 / 工具 | 解讀 |
| --- | --- | --- |
| **Cohen's κ (unweighted)** | κ = (Po - Pe) / (1 - Pe) | < 0.20 slight; 0.21-0.40 fair; 0.41-0.60 moderate; 0.61-0.80 substantial; > 0.80 almost perfect |
| **Weighted κ (linear / quadratic)** | 適用於有序量表（0-4）| 同上，但對「差 1 分」比「差 4 分」更嚴格 |
| **ICC (Intraclass Correlation Coefficient)** | 雙因子混合模型 | < 0.5 poor; 0.5-0.75 moderate; 0.75-0.9 good; > 0.9 excellent |
| **Bland-Altman plot** | 視覺化分數差距 | 檢視系統性偏誤 |

---

## 4. 縱貫 KPI 追蹤 / Longitudinal KPI Tracking

### 4.1 KPI 量測時點

| 時點 | 名稱 | 量測內容 |
| --- | --- | --- |
| **T0** | Baseline | 跑完 Phase A 後、Phase B 啟動前 |
| **T+6m** | Phase 1 結束 | L1 Gate 驗收 |
| **T+12m** | Phase 2 中段 | L2/L3 Gate |
| **T+18m** | Phase 2 結束 | L3 完成 |
| **T+24m** | Phase 3 結束 | L4/L5 Gate |

### 4.2 KPI 五大維度（對應 Tool 8.5 價值追蹤矩陣）

| 維度 | 具體 KPI 例 |
| --- | --- |
| **時間** | 客訴回應時間、提案產出時間、月結時間、決策週期 |
| **品質** | 不良率、錯誤率、客戶投訴次數、重工率 |
| **規模** | 處理量、受惠人數、自動化任務次數 |
| **風險** | 漏案率、合規違規次數、機敏外流事件 |
| **資產** | Skill 條數、Wiki 條目數、Agent 任務數、訓練完成率 |

### 4.3 KPI 資料品質要求（依 Tool 8.9 Evidence Hierarchy）

- **L3 必要**：所有時間 / 規模 KPI 來自系統 log（n8n / Audit Log / ERP）
- **L4 建議**：抽樣由內稽 / 外部會計師驗證
- **L1-L2 補充**：員工 NPS / 訪談摘要

---

## 5. 質化研究：半結構訪談 / Qualitative: Semi-Structured Interviews

### 5.1 訪談時點

每家企業：T0、T+6m、T+12m、T+18m、T+24m 各 1 次（每位受訪者）。

### 5.2 受訪者

- CEO / Sponsor
- AI Champion
- IT Lead
- 至少 2 位部門長
- 至少 3 位一線使用者

### 5.3 訪談題目（節錄）

1. 過去 6 個月最有感的 AI 改變是什麼？
2. 哪些原本期待的 AI 改變沒實現？為什麼？
3. 員工 / 部門對 AI 的態度有變化嗎？
4. 你會如何向同業推薦 / 不推薦這套方法論？
5. 哪一個 Stage / Tool 對你最有用？哪一個沒用？
6. 跨期：你回頭看 12 個月前的 Ideal Practice 簽署，後不後悔？

### 5.4 質化分析

- 逐字稿轉錄 + 編碼（NVivo / Atlas.ti）
- 雙編碼者編碼一致性 ≥ 80%（inter-coder reliability）
- 主題分析 (thematic analysis) 萃取共同模式 / 反例

---

## 6. 統計分析計畫 / Statistical Analysis Plan

### 6.1 描述性統計

- 各構面分數分布（mean, SD, median, IQR）
- 雷達圖 T0 vs T24 視覺化
- 6 構面相關矩陣（檢視多重共線性）

### 6.2 信度與效度

| 分析 | 工具 | 假設對應 |
| --- | --- | --- |
| Cronbach's α | SPSS / R `psych::alpha()` | H2 |
| EFA + Bartlett's + KMO | SPSS / R `psych::fa()` | H3a |
| CFA + fit indices | Mplus / R `lavaan::cfa()` | H3b（**N ≥ 200 才做**）|
| Cohen's κ | R `irr::kappa2()` | H1 |
| ICC | R `irr::icc()` | H1 |

### 6.3 推論統計

| 分析 | 假設 | 工具 |
| --- | --- | --- |
| Paired t-test (T0 vs T24) | H5 雷達面積增加 | R `t.test(paired=TRUE)` |
| Mixed-effects model | H4 預測效度 | R `lme4::lmer()` |
| ANCOVA | 控制基期 KPI 與規模 | R `aov()` |
| Sensitivity analysis | 對抗 missing data + dropout | R `mice` 多重插補 |

### 6.4 顯著水準與調整

- α = 0.05 為主檢定
- Bonferroni 校正多重比較
- effect size 報告：Cohen's d、η²、partial η²

---

## 7. 時程與里程碑 / Timeline & Milestones

```
Month 0:    研究設計 finalize + IRB 申請
Month 1-3:  招募 5-10 家企業 + 簽研究合作協議
Month 4:    Consultant A/B 培訓（雙盲評分 SOP）
Month 5-6:  T0 雙盲評分 + Baseline KPI 量測
Month 6-12: Phase 1 介入 + T+6m 評分與訪談
Month 12-18: Phase 2 介入 + T+12m + T+18m
Month 18-24: Phase 3 介入 + T+24m 終期評分與訪談
Month 24-27: 資料分析 + 撰寫研究報告 + 期刊投稿
Month 27-30: revise + submission
```

---

## 8. 預算估算 / Budget Estimate

| 項目 | 估算 (NT$) |
| --- | --- |
| 顧問人力（Consultant A + B 各家 80-120 小時）| 600-900 萬 |
| 研究員（中立評分比對 + 質化分析）| 150-250 萬 |
| KPI 系統 log 蒐集工具 + 訪談轉錄 | 50-100 萬 |
| IRB / 法務 / 統計顧問 | 50-100 萬 |
| 開源工具與雲端資料庫 | 30-50 萬 |
| 預備金 (15%) | 130-200 萬 |
| **總計** | **NT$ 1,010-1,600 萬** |

⚠️ 為換取免費顧問服務，5-10 家企業承諾配合 18 個月資料蒐集 → 顧問人力成本可由「等值顧問服務」抵充，**實際現金支出可降至 NT$ 400-700 萬**。

---

## 9. 出版策略 / Publication Strategy

### 9.1 預期產出

| 產出 | 期刊 / 平台 | 預估時點 |
| --- | --- | --- |
| **Pre-registration** | OSF (Open Science Framework) | Month 0 |
| **Protocol paper** | BMJ Open / Pilot and Feasibility Studies | Month 3 |
| **Methodology paper** | MIS Quarterly / Information Systems Research / Journal of Business Research | Month 27 |
| **Industry white paper** | 中文版 + EN，公開 Apache 2.0 | Month 27 |
| **Case studies (匿名)** | Harvard Business Review 風格 case | Month 30 |
| **Practitioner guide** | 更新本 toolkit + 加入實證證據 | Month 30 |

### 9.2 開放科學承諾

- 所有研究資料（去識別化後）公開於 OSF
- 統計分析 R / Python script 公開於 GitHub
- 受訪者匿名身份保密，但 aggregate 結果完全透明

---

## 10. 風險與緩解 / Risks & Mitigation

| 風險 | 機率 | 影響 | 緩解 |
| --- | --- | --- | --- |
| 企業中途退出 (dropout) | 中 | 高 | 過度招募 (over-recruit) 12 家；分析時用 intention-to-treat |
| Consultant A/B 偏誤 / 互通 | 低 | 高 | SOP 訓練 + 抽查 + 雙盲嚴格執行 + 兩人不同辦公室 |
| KPI 系統 log 取得困難 | 中 | 中 | T0 即與 IT 確認 log 可得性；不可得者改用替代指標 |
| IRB 審查延遲 | 中 | 中 | Month 0 同時送 IRB + 開始招募 |
| 樣本量不足做 CFA | 高 | 中 | pilot 階段先做 EFA；CFA 留待主研究 N=200+ |
| 預算不足 | 中 | 高 | 申請科技部 / NSTC / 教育部 / QUT 補助；多家企業共擔 |

---

## 11. 退場條件 / Stopping Rules

研究若出現以下情況，提前終止並如實揭露：

- ≥ 50% 企業中途退出
- Inter-rater κ < 0.40（方法論不一致 → 量表需重新設計）
- IRB 撤銷
- 出現嚴重倫理問題（資料外洩、受訪者受害）

提前終止的研究**仍須公開所有已收集資料與結果**（避免 publication bias）。

---

## 12. 預期貢獻 / Expected Contributions

| 貢獻 | 對象 | 形式 |
| --- | --- | --- |
| **理論**：首個 GenAI 採用成熟度的實證驗證模型 | 學術界（IS / BPM / Strategy）| Peer-reviewed paper |
| **方法**：Cases-as-Benchmarks + Client Ideal Practice 共創 Workshop 的 protocol | 顧問業 | Open-source toolkit (Apache 2.0) |
| **政策**：AI Governance 對齊的實證證據 | 監管者（台灣 AI 基本法 / NIST / EU）| White paper + 立法院公聽會 |
| **產業**：5-10 家企業的真實 longitudinal cases | 同業客戶 | Real cases (replacing composite) |
| **教育**：研究結果整合進 NTUST / QUT 課程 | 學生 | Course materials |

---

## 13. 相關文件

| 文件 | 與本研究關係 |
| --- | --- |
| [`../01_Assessment/AI_MATURITY_SCORING_MODEL.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL.md) §3.1-3.3 | 量表 construct definition；本研究驗證之 |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md) | 為什麼方法論需要實證 |
| [`FAILURE_PATTERNS.md`](FAILURE_PATTERNS.md) | 已知失敗模式 → 本研究預設 mitigation |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 8.9 | Evidence Hierarchy 為本研究 KPI 證據等級依據 |

---

## 14. 引用文獻 / References

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297-334.
- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- Streiner, D. L., Norman, G. R., & Cairney, J. (2015). *Health measurement scales: A practical guide to their development and use* (5th ed.). Oxford University Press.
- Hair, J. F., et al. (2019). *Multivariate Data Analysis* (8th ed.). Cengage.
- Creswell, J. W. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). SAGE.
- Open Science Framework: <https://osf.io/> (pre-registration platform)

---

授權與引用 / License & Citation

本文為 Apache License 2.0；可使用、修改、商業利用，唯需保留 [`../NOTICE`](../NOTICE) 檔之署名。本研究設計可被其他研究團隊**自由採用、修改、複製**，前提是進行同樣的 pre-registration 與公開開放科學承諾。
