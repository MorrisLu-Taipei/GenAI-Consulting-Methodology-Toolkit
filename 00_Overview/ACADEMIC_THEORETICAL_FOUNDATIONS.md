# 學術理論基礎：Tiger AI 方法論的七大理論支柱

> 🌐 English version: [ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md)
>
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技

更新日期：2026-05-16

---

> **本文目的**：把 Tiger AI 方法論散落在各檔案中的學術理論依據**統一收斂到一份權威文件**。任何學者 / 監管者 / 嚴肅顧問質詢「這套方法論的理論依據是什麼」時，本文是唯一答案。
>
> **核心主張**：Tiger AI 方法論不只是顧問實務歸納，而是**七大理論的工程化整合**。

---

## 1. 理論地圖總覽

| 理論 | 創立者 / 經典文獻 | 解決的核心問題 | Tiger AI 對應位置 |
| --- | --- | --- | --- |
| **Capability Maturity & BPM Maturity** | Paulk et al. (1993) CMMI; Rosemann & de Bruin (2005) BPM Maturity | 組織能力如何被結構化評分？ | L1-L5 + Stage 2 評分 |
| **Absorptive Capacity** | Cohen & Levinthal (1990) | 為什麼組織「**接收**」新能力的能力差很多？ | Tool 6.3 組織吸收力評估 |
| **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | 哪些任務適合 / 不適合 AI？ | Stage 7 To-Be Design（不是每部門都該 L5）|
| **Dynamic Capabilities** | Teece, Pisano & Shuen (1997); Teece (2007) | 組織如何「**快速適應外部變化**」？ | Stage 7 + Stage 8（從靜態流程自動化到動態能力）|
| **Sociotechnical Systems & Trust in AI** | Bostrom & Heinen (1977); Dietvorst et al. (2015); Glikson & Woolley (2020) | 人機協作為何困難？演算法厭惡 / 過度依賴 | Stage 8 Change Management + 人機協作 HITL |
| **Real Options Theory** | Dixit & Pindyck (1994); McGrath (1997) | 高度不確定性下，如何評估 AI 戰略投資？ | Stage 8 §13 Value Tracking + ROI |
| **AI-Native Living Book / Executable Knowledge Artifact** | Knuth (1984) Literate Programming; Anderson et al. (1995) ITS; 本作者 (2026) | 方法論本身可被 AI 執行 | AGENTS.md + AI_NATIVE_LIVING_BOOK |

---

## 2. Capability Maturity 與 BPM Maturity

### 2.1 理論概要

- **CMMI（Capability Maturity Model Integration）**：Paulk et al. (1993) 起源於 SEI（軟體工程研究所），定義組織能力 5 級（Initial / Repeatable / Defined / Managed / Optimizing）。
- **BPM Maturity Model**：Rosemann & de Bruin (2005, QUT) 把成熟度概念延伸到 Business Process Management，加入「**Process Awareness / Alignment / Methods / IT / People / Culture**」六大 enabler。

### 2.2 對 Tiger AI 的貢獻

- **L1-L5 兩條軸**繼承 BPM Maturity 的「Process Awareness → Optimization」演化邏輯，但加入 GenAI 時代必要的「**規模軸 + AI 自主軸**」雙軸結構
- **0-4 量尺**與 BARS 行為錨點源自此學派
- **Stage Gate Criteria** = CMMI 的「Process Areas」+ 階段驗收

### 2.3 對應檔案

- [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 兩條軸的故事
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL.md) L1-L5 定義
- [`../01_Assessment/BARS_RUBRICS.md`](../01_Assessment/BARS_RUBRICS.md) 行為錨點

### 2.4 引用

- Paulk, M., et al. (1993). *Capability Maturity Model for Software, Version 1.1*. SEI/CMU.
- Rosemann, M., & de Bruin, T. (2005). Towards a Business Process Management Maturity Model. *ECIS 2005 Proceedings*.
- Rosemann, M., zur Muehlen, M. (Eds.) (2009). *Business Process Management Maturity Models*.

---

## 3. Absorptive Capacity（吸收能力）

### 3.1 理論概要

- **Cohen & Levinthal (1990)** 在 *Administrative Science Quarterly* 提出：組織「**識別、吸收、應用新外部知識的能力**」決定其創新能力。
- 核心要素：**Prior Knowledge（先備知識）+ Internal Knowledge Flow（內部知識流動機制）**。
- Zahra & George (2002) 進一步拆成 4 維度：Acquisition / Assimilation / Transformation / Exploitation。

### 3.2 對 Tiger AI 的貢獻

- 解釋為什麼**同樣的 AI 機會，不同企業導入結果天差地別** —— 差別在 absorptive capacity
- Tool 6.3 組織吸收力評估直接對應此理論
- 強化「**為什麼不能跳級**」：跳過 L1-L3 → absorptive capacity 不足 → L4-L5 必然失敗（見 [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) §2）

### 3.3 對 Tool 6.3 的具體強化

原 Tool 6.3 6 維度（預算 / Champion / IT FTE / 治理 / 素養 / 變革容量）**加入 2 個新維度**：

| 新維度 | 評估問題 | 評分 |
| --- | --- | --- |
| **Prior Knowledge（先備知識）** | 公司是否有：(a) 過去 BPM / Lean / Six Sigma 經驗 (b) 過去任何 AI / ML / RPA 嘗試 (c) 軟體開發內部能力 | 0-4 分 |
| **Internal Knowledge Flow（知識流動）** | 部門之間是否有：(a) 跨部門 review 例行 (b) 共享文件平台 (c) 內部 mentor / 講師制度 | 0-4 分 |

→ 高 Prior Knowledge + 高 Knowledge Flow 的公司可承擔更激進 Phase 1/2/3；反之必須拉長時程。

### 3.4 引用

- Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128-152.
- Zahra, S. A., & George, G. (2002). Absorptive capacity: A review, reconceptualization, and extension. *Academy of Management Review*, 27(2), 185-203.

---

## 4. Task-Technology Fit (TTF)

### 4.1 理論概要

- **Goodhue & Thompson (1995)** 在 *MIS Quarterly* 提出：科技帶來績效的程度，取決於「**任務需求 ↔ 科技能力**」的契合度。
- 任務特性二分：**Routine（重複性、可預測）vs Non-routine（高度判斷、創造性）**

### 4.2 對 Tiger AI 的貢獻

**不是每個部門都該走到 L5**。依任務特性決定該部門的合適 L 級終點：

| 任務特性 | 合適終點 | 理由 |
| --- | --- | --- |
| 高度 Routine（如客服 FAQ、發票分類）| L3-L4 | AI 適配度高、HITL 成本低 |
| 中度 Routine + 部分判斷（如業務提案、月結異常）| L2-L3 + HITL | AI 草稿 + 人工確認，平衡效率與風險 |
| 高度 Non-routine（如 M&A 評估、策略決策）| L1-L2（個人助理）| AI 是輔助，人類主導；強推 L4-L5 反而傷害判斷品質 |
| 高度合規敏感（如法律、醫療診斷）| L2-L3 + 強 HITL | 法規風險過高，不適合 L4-L5 |

### 4.3 對應檔案 / 工具

- Stage 7 Tool 7.2 人機協作架構 → 用 TTF 矩陣決定每 process 的 AI 介入程度
- 新增 **TTF Assessment Worksheet** 至 Tool 6.3 → 每部門打 TTF 分數，決定該部門的 Ideal L 級

### 4.4 引用

- Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. *MIS Quarterly*, 19(2), 213-236.
- Zigurs, I., & Buckland, B. K. (1998). A theory of task/technology fit and group support systems effectiveness. *MIS Quarterly*, 22(3), 313-334.

---

## 5. Dynamic Capabilities（動態能力）

### 5.1 理論概要

- **Teece, Pisano & Shuen (1997)** 在 *Strategic Management Journal* 提出：企業競爭優勢源自「**整合、建構、重構內外資源的能力**」。
- **Teece (2007)** 進一步拆成三組微基礎：
  1. **Sensing**（感知）：辨識機會與威脅
  2. **Seizing**（捕捉）：決策與資源配置
  3. **Transforming**（重構）：組織重組以利用機會

### 5.2 對 Tiger AI 的貢獻

**從靜態流程自動化 → 動態適應能力**。Tiger AI 不只是把現有 APQC 流程 AI 化，而是**幫客戶建立持續適應外部變化的新能力**：

| 動態能力 | Tiger AI 對應 |
| --- | --- |
| **Sensing** | L3 Workflow + L4 Agent 持續監測市場 / 客戶 / 製程訊號（如競品價格、客訴趨勢、產品瑕疵）|
| **Seizing** | Phase 1/2/3 階段拆解 = 把 Sensing 來的訊號轉成具體投資決策 |
| **Transforming** | L5 Multi-Agent Organization + 季度 Gate C 雷達回顧 = 組織持續重構 |

### 5.3 對 Stage 7 的具體強化

在 Stage 7 To-Be Design 增補 **Dynamic Capability Worksheet**：

```
依 Teece (2007) 三組微基礎，每個 To-Be 設計要回答：

1. Sensing：這個 AI 設計幫公司「**感知**」什麼外部訊號？
   例：客訴 Agent 監測客戶滿意度趨勢
2. Seizing：當訊號出現，公司能「**捕捉**」多快？
   例：Quick Win 客訴回應 5 天→1 天 = 把客戶流失機會壓縮到最小
3. Transforming：這套 AI 如何讓組織「**自我重構**」？
   例：L5 ClawTeam 跨部門 Agent 協作 = 組織不再依賴特定資深員工
```

→ 不答這 3 題的 To-Be 只是「自動化現狀」，不是真正的轉型。

### 5.4 引用

- Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal*, 18(7), 509-533.
- Teece, D. J. (2007). Explicating dynamic capabilities: The nature and microfoundations of (sustainable) enterprise performance. *Strategic Management Journal*, 28(13), 1319-1350.

---

## 6. Sociotechnical Systems & Trust in AI

### 6.1 理論概要

- **Sociotechnical Systems Theory**（Bostrom & Heinen, 1977）：組織績效是**社會系統 + 技術系統**的聯合產出，不可單獨優化任一邊
- **演算法厭惡 (Algorithmic Aversion)**：Dietvorst, Simmons & Massey (2015) 在 *Journal of Experimental Psychology* 證實：人即使知道演算法更準確，看到演算法犯錯後**寧可用較差的人類判斷**
- **演算法過度依賴 (Automation Complacency)**：Parasuraman & Manzey (2010) 證實：人對自動化過度信任會喪失警覺，反致更大事故
- **Trust in AI**：Glikson & Woolley (2020) 整合 cognitive + emotional trust 兩維度

### 6.2 對 Tiger AI 的貢獻

人機協作真正的挑戰不只是「**怕被取代**」，更是：

1. **演算法厭惡**：AI 第一次出錯後，員工集體拒用 → L3-L4 上線後常見
2. **演算法過度依賴**：員工放棄審核 → HITL 失效 → 出事規模放大
3. **責任歸屬模糊**：AI 出錯算誰的？員工怕擔責 → 心理安全感缺
4. **職業認同重塑**：從「執行者 Doer」變「審查者 Reviewer」 → 認知負荷與成就感變化

### 6.3 對 Stage 8 Change Management 的強化

原 Tool 8.2 抗拒處理 4 類型，**加上 2 個新類型**：

| 抗拒類型 | 典型訊號 | 處理 |
| --- | --- | --- |
| **演算法厭惡** | AI 一次出錯後集體拒用 | 透明化錯誤率（人 vs AI 對比）+ 漸進信任建立（先低風險場景） |
| **演算法過度依賴** | 員工不審核就 approve | Reviewer Workflow 強制隨機抽樣 + 錯誤偵測後重新教育 |

### 6.4 對 HITL 設計的強化（Tool 7.2）

新增**心理安全與責任歸屬欄位**：

| Process | HITL 節點 | **責任歸屬聲明** | **心理安全保障** |
| --- | --- | --- | --- |
| 客訴回覆 | 寄出前 100% 人審 | AI 草稿責任 = AI Champion；最終回覆責任 = 客服員工 | 員工有權「我覺得 AI 答錯，可以不審核直接退」不被責難 |
| 製程根因 | 對策前 100% 人審 | AI 假設責任 = Agent 開發者；採用對策責任 = 製程主管 | 主管有「拒絕採用 AI 建議」的正式 SOP |

### 6.5 引用

- Bostrom, R. P., & Heinen, J. S. (1977). MIS problems and failures: A socio-technical perspective. *MIS Quarterly*, 1(3), 17-32.
- Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. *Journal of Experimental Psychology: General*, 144(1), 114-126.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3), 381-410.
- Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence: Review of empirical research. *Academy of Management Annals*, 14(2), 627-660.
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *Administrative Science Quarterly*, 44(2), 350-383.

---

## 7. Real Options Theory（實質選擇權）

### 7.1 理論概要

- **Dixit & Pindyck (1994)** 在 *Investment Under Uncertainty* 提出：高度不確定性投資的價值 = 立即執行價值 + **「未來可選擇」的選擇權價值**
- **McGrath (1997)** 應用於戰略投資：「**今天投資是為了**保留**未來可擴張的權利**」
- 對抗 NPV 在不確定性下的低估：NPV 假設未來確定，但高不確定下管理彈性有極高價值

### 7.2 對 Tiger AI 的貢獻

L4-L5 高度不確定 AI 投資，**傳統 NPV / IRR 必然低估**（因為 18-24 個月後具體 cash flow 算不出來）。Real Options 提供更好的論述：

| 投資 | NPV 視角（低估）| Real Options 視角（合理）|
| --- | --- | --- |
| Phase 1 基礎（NT$ 280 萬）| Cash flow 不明 → NPV ≈ 0 | 買「**未來可低成本快速擴張 L4-L5 的選擇權**」，價值遠大於 NT$ 280 萬 |
| L1 全員 Chat AI | 短期 ROI 不明顯 | 員工 AI 素養 = **未來所有 AI 應用的前提資產** |
| L2 Skill Library | 投入產出比看不到 | 知識資產化 = 公司未來「**多家 AI 應用同時 plug-in**」的選擇權 |
| L4 Hermes Agent Pilot | 試做 1 個 Agent 算不算划算？| 試做 = 學會 L4 = 未來 L5 ClawTeam 的選擇權 |

### 7.3 Real Options 估值公式（簡化版 Black-Scholes 應用）

對 L4-L5 投資，可用以下框架估算：

```
Option Value = max(0, future_payoff - exercise_cost)

其中：
  future_payoff = 未來行使選擇權（如擴張到 L5）能帶來的營收
  exercise_cost = 行使時的成本（如 Phase 3 投資）
  volatility (σ) = 市場 / 技術不確定性
  time-to-expiration = 機會窗口期
```

⚠️ 不需要算到 Black-Scholes 精確值；**論述層級足以說服 CFO** 為「短期看不到回報但未來價值高」的投資正名。

### 7.4 對 Stage 8 §13 Value Tracking 的強化

原 §13.1 五維度價值追蹤（時間 / 品質 / 規模 / 風險 / 資產），**加入第 6 維度**：

| 維度 | 內容 |
| --- | --- |
| **戰略選擇權 (Strategic Options)** | 此投資保留了什麼「**未來行使的權利**」？例：L1 基礎 → 未來可快速擴 L4；L2 Skill Library → 未來可串多家 Agent；L3 Workflow → 未來可整合任何新系統 |

### 7.5 引用

- Dixit, A. K., & Pindyck, R. S. (1994). *Investment Under Uncertainty*. Princeton University Press.
- McGrath, R. G. (1997). A real options logic for initiating technology positioning investments. *Academy of Management Review*, 22(4), 974-996.
- Trigeorgis, L. (1996). *Real Options: Managerial Flexibility and Strategy in Resource Allocation*. MIT Press.

---

## 8. AI-Native Living Book as Executable Knowledge Artifact

### 8.1 理論概要

- **Literate Programming**：Knuth (1984) 主張程式碼與文件應整合為「可被人閱讀也可被機器執行」的單一文件
- **Intelligent Tutoring Systems (ITS)**：Anderson, Corbett, Koedinger & Pelletier (1995) 設計 AI 作為個別化導師的系統
- **Open Educational Resources (OER) + AI**：當代趨勢，把開放教材結合 AI 變成可互動知識系統

### 8.2 對 Tiger AI 的貢獻

本方法論本身就是這個理論的**實踐案例**：

- repo + AGENTS.md = **executable knowledge artifact**
- AI 共讀導師 = **適應性 ITS** 應用於成人專業教育
- 客戶與方法論對話 = 客製化 OER

詳見 [`AI_NATIVE_LIVING_BOOK.md`](AI_NATIVE_LIVING_BOOK.md) 完整論述。

### 8.3 引用

- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors: Lessons learned. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

---

## 9. 7 理論如何協同：Tiger AI 方法論的整合模型

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   [Capability Maturity]  ────►  L1-L5 結構化能力評分              │
│         │                                                        │
│         ▼                                                        │
│   [Absorptive Capacity] ────►   為什麼公司接收能力差很多           │
│         │                                                        │
│         ▼                                                        │
│   [Task-Technology Fit] ────►  哪些任務該 L? 哪些不該              │
│         │                                                        │
│         ▼                                                        │
│   [Dynamic Capabilities]────►  L3-L5 不只自動化，是建立適應能力   │
│         │                                                        │
│         ▼                                                        │
│   [Sociotechnical Trust]────►  人機協作的真實挑戰（信任、責任）   │
│         │                                                        │
│         ▼                                                        │
│   [Real Options]        ────►  L4-L5 高不確定下的投資正名         │
│         │                                                        │
│         ▼                                                        │
│   [AI-Native Living Book]──►   方法論本身可被 AI 執行            │
│                                                                  │
└────────────────────────────────────────────────────────────────┘

7 個理論不是孤立堆疊，而是**從評分 → 接收能力 → 任務匹配 → 動態適應 → 人機信任 → 戰略投資 → 方法論執行**的完整鏈條
```

---

## 10. 學術投稿建議

依本文 7 理論，可拆出多篇學術論文：

| 論文題目（建議）| 主軸理論 | 投稿期刊 |
| --- | --- | --- |
| A GenAI Adoption Maturity Model: Extending BPM Maturity for the LLM Era | Capability Maturity + AI-native | MIS Quarterly / Information Systems Research |
| Absorptive Capacity in Enterprise AI Adoption: Empirical Evidence from 7 Industries | Absorptive Capacity | Strategic Management Journal |
| Task-Technology Fit Beyond Routine Work: When Should Departments Adopt L4-L5 Agents? | TTF | Information & Management |
| From Automation to Dynamic Capability: How AI Reshapes Organizational Sensing | Dynamic Capabilities | Strategic Management Journal |
| Algorithm Aversion in Workflow Automation: A Mixed-Methods Study | Sociotechnical / Trust | Organization Science |
| Valuing AI Foundation Investments as Real Options | Real Options | Strategic Management Journal / California Management Review |
| AI-Native Living Books: Methodology as Executable Knowledge Artifact | AI-Native LB | Communications of the ACM |

---

## 11. 引用文獻完整清單 / Full Bibliography

### 11.1 Maturity Models

- Paulk, M., et al. (1993). *Capability Maturity Model for Software, Version 1.1*. SEI/CMU.
- Rosemann, M., & de Bruin, T. (2005). Towards a Business Process Management Maturity Model. *ECIS 2005 Proceedings*.
- Rosemann, M., zur Muehlen, M. (Eds.) (2009). *Business Process Management Maturity Models*.

### 11.2 Absorptive Capacity

- Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128-152.
- Zahra, S. A., & George, G. (2002). Absorptive capacity: A review, reconceptualization, and extension. *Academy of Management Review*, 27(2), 185-203.

### 11.3 Task-Technology Fit

- Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. *MIS Quarterly*, 19(2), 213-236.
- Zigurs, I., & Buckland, B. K. (1998). A theory of task/technology fit and group support systems effectiveness. *MIS Quarterly*, 22(3), 313-334.

### 11.4 Dynamic Capabilities

- Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal*, 18(7), 509-533.
- Teece, D. J. (2007). Explicating dynamic capabilities. *Strategic Management Journal*, 28(13), 1319-1350.

### 11.5 Sociotechnical Systems & Trust in AI

- Bostrom, R. P., & Heinen, J. S. (1977). MIS problems and failures: A socio-technical perspective. *MIS Quarterly*, 1(3), 17-32.
- Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion. *Journal of Experimental Psychology: General*, 144(1), 114-126.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3), 381-410.
- Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence. *Academy of Management Annals*, 14(2), 627-660.
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *Administrative Science Quarterly*, 44(2), 350-383.

### 11.6 Real Options

- Dixit, A. K., & Pindyck, R. S. (1994). *Investment Under Uncertainty*. Princeton University Press.
- McGrath, R. G. (1997). A real options logic for initiating technology positioning investments. *Academy of Management Review*, 22(4), 974-996.
- Trigeorgis, L. (1996). *Real Options*. MIT Press.

### 11.7 Executable Knowledge / ITS

- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Anderson, J. R., et al. (1995). Cognitive tutors. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society*. Harvard University Press.

### 11.8 Measurement & Methodology

- Smith, P. C., & Kendall, L. M. (1963). Retranslation of expectations: Behaviorally anchored rating scales. *Journal of Applied Psychology*, 47(2), 149-155.
- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297-334.

---

授權與引用 / License & Citation

本文為 Apache License 2.0；可使用、修改、商業利用，唯需保留 [`../NOTICE`](../NOTICE) 檔之署名。
