# 經典顧問框架庫 / Consulting Frameworks Library

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **引用備註 / Attribution:** 本框架庫之框架清單與分類，參考並改寫自 [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant)（MIT License）。本檔在其基礎上，**重新以本方法論的語言改寫，並對應到我方八階段顧問結構與 L1-L5 成熟度模型**。引用與授權說明見 [`../90_References/CONSULTANT_FRAMEWORKS_REFERENCE.md`](../90_References/CONSULTANT_FRAMEWORKS_REFERENCE.md)。
> The framework list and taxonomy in this library are referenced from and rewritten based on [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant) (MIT License), re-expressed in this methodology's language and mapped onto our eight-stage consulting structure and L1-L5 maturity model.

---

## 1. 這份框架庫怎麼用 / How to Use This Library

本方法論的核心是 **八階段顧問結構**（見 [`CONSULTING_TOOLKIT_TEMPLATES.md`](CONSULTING_TOOLKIT_TEMPLATES.md)）。八階段是「流程骨架」，而本框架庫是「每一階段裡可以拿來用的分析工具」。

This methodology's core is the **eight-stage consulting structure** (see `CONSULTING_TOOLKIT_TEMPLATES.md`). The eight stages are the "process skeleton"; this library is the set of "analytical tools you can pull into each stage."

> 八階段告訴你「現在該做什麼」；框架庫告訴你「這一步可以用哪個工具把它做好」。
> The eight stages tell you *what to do now*; the framework library tells you *which tool can do that step well*.

**使用原則：**

1. **先定位階段，再選框架** — 不要為了用框架而用框架。
2. **框架是組合的，不是單用的** — 多數商業問題需要 2-4 個框架交叉。
3. **答案先行（Answer-First）** — 先給初步假設答案（Day-1 Answer），再用框架驗證或推翻。
4. **MECE 是底層紀律** — 任何拆解都要「互斥、窮盡」。

---

## 2. 框架選擇器 / Framework Selector

當客戶 / 學員用自然語言描述問題時，用這張表快速路由到該用的框架組合：

| 客戶說 / "I need to…" | 建議框架組合 | 對應階段 |
| --- | --- | --- |
| 「我有個複雜問題不知從何下手」 | McKinsey 7-Step + MECE + Issue Tree | Stage 1, 4 |
| 「我要把這件事講清楚 / 寫成報告」 | Pyramid Principle + SCQ + Storyboarding | Stage 5 |
| 「為什麼利潤在下滑？」 | Profitability Framework + Issue Tree + 5 Whys | Stage 4 |
| 「我要評估要不要進這個市場」 | Market Entry + Market Sizing + Porter's 5 Forces | Stage 3 |
| 「我要做整體策略規劃」 | PESTEL → Porter's 5 Forces → 3C → SWOT → Issue Tree | Stage 2, 3 |
| 「我要評估一樁併購 / 投資」 | M&A Framework + Due Diligence + NPV / IRR | Stage 3, 8 |
| 「我要找出流程哪裡出問題」 | 5 Whys + Fishbone + Value Stream Mapping | Stage 1, 4 |
| 「我要排優先順序」 | 80/20 (Pareto) + Impact×Effort + MECE | Stage 4 |
| 「我要規劃這個轉型專案」 | WBS + RACI + Kotter + OKR | Stage 6 |
| 「我要證明這個投資值得做」 | ROI + NPV + IRR + Payback + Break-even | Stage 8 |
| 「我要設計新的商業 / 服務模式」 | Business Model Canvas + Design Thinking + Customer Journey | Stage 7 |
| 「我要說服組織接受改變」 | Kotter 8 Steps + ADKAR + Stakeholder Map | Stage 6 |
| 「我要分析我們的競爭定位」 | Porter's 5 Forces + SWOT + Value Chain + Core Competency | Stage 3 |
| 「我要訂價」 | Pricing Framework + Value-Based Pricing + Break-even | Stage 7 |
| 「我要追蹤導入成效」 | Balanced Scorecard + OKR + KPI Tree | Stage 8 |

---

## 3. 框架 × 八階段對應總表 / Framework × Eight-Stage Mapping

| 八階段 | 主要可套用框架 |
| --- | --- |
| **Stage 1 現況掌握** | 5 Whys、Fishbone、Issue Tree、McKinsey 7-Step、Value Chain |
| **Stage 2 願景對齊** | McKinsey 7S、Ansoff Matrix、Blue Ocean、Scenario Planning、OKR |
| **Stage 3 產業標竿** | Porter's 5 Forces、PESTEL、3C、SWOT、BCG Matrix、Core Competency |
| **Stage 4 差距分析** | MECE、Issue Tree、80/20 (Pareto)、Hypothesis-Driven、Profitability Framework、Impact×Effort |
| **Stage 5 高階問題定義** | Pyramid Principle、SCQ、Day-1 Answer、MECE |
| **Stage 6 路徑圖與 Stage Gate** | WBS、RACI、Gantt、Kotter 8 Steps、ADKAR、OKR、Stakeholder Map |
| **Stage 7 解決方案架構** | Business Model Canvas、Design Thinking、Customer Journey、Jobs-to-be-Done、Pricing、Lean、Six Sigma |
| **Stage 8 治理與 ROI** | ROI、NPV、IRR、Payback、Break-even、Sensitivity Analysis、Balanced Scorecard、PDCA |

---

## 4. 框架庫（依七大類）/ The Library (by 7 Categories)

> 每個框架：**名稱** ｜ 一句話用途 ｜ 何時用 ｜ 對應我方階段。
> 詳細步驟、範例與 common pitfalls，建議顧問依此清單再展開為各自的 worksheet（格式參考 §6）。

### 4.1 問題解決 / Problem-Solving

| 框架 | 一句話用途 | 何時用 | 階段 |
| --- | --- | --- | --- |
| **MECE**（互斥窮盡） | 把問題拆成不重疊、無遺漏的子項 | 任何拆解的底層紀律 | 1,4,5 |
| **Pyramid Principle**（金字塔原理） | 結論先行、由上而下組織論述 | 寫報告、做簡報、定問題 | 5 |
| **Issue Tree**（議題樹） | 把大問題逐層拆成可驗證的小問題 | 問題結構化 | 1,4 |
| **McKinsey 7-Step** | 定義→結構→排序→分析→建議→溝通→實施 的標準流程 | 複雜問題的整體流程 | 1-6 |
| **SCQ**（情境-衝突-問題） | 用 Situation-Complication-Question 框定問題 | 問題定義、報告開場 | 5 |
| **Hypothesis-Driven**（假設驅動） | 先立假設再找證據，不亂蒐集資料 | 分析效率 | 4 |
| **80/20（Pareto）** | 找出貢獻 80% 結果的 20% 關鍵因素 | 排優先順序 | 4 |
| **Day-1 Answer**（首日答案） | 一開始就給初步假設答案，再驗證 | 答案先行 | 5 |

### 4.2 策略分析 / Strategic Analysis

| 框架 | 一句話用途 | 何時用 | 階段 |
| --- | --- | --- | --- |
| **Porter's 5 Forces** | 分析產業競爭強度（買方、賣方、新進、替代、現有競爭） | 產業吸引力評估 | 3 |
| **SWOT** | 優勢/劣勢/機會/威脅 四象限 | 競爭定位快速盤點 | 3 |
| **PESTEL** | 政治/經濟/社會/技術/環境/法規 宏觀掃描 | 外部環境分析 | 3 |
| **BCG Matrix** | 用市占×成長率把事業分明星/金牛/問號/狗 | 事業組合決策 | 3 |
| **McKinsey 7S** | 7 個 S 的組織一致性檢查 | 組織診斷、願景對齊 | 2 |
| **3C** | Customer / Competitor / Company 三角分析 | 策略起手式 | 3 |
| **Value Chain**（價值鏈） | 拆解企業活動找價值與成本來源 | 競爭優勢來源分析 | 1,3 |
| **Ansoff Matrix** | 既有/新 市場×產品 的成長選項 | 成長策略 | 2 |
| **Core Competency**（核心能力） | 找出難以模仿的關鍵能力 | 競爭優勢定位 | 3 |
| **Blue Ocean**（藍海策略） | 跳出紅海競爭，創造新需求空間 | 願景與差異化 | 2 |
| **Scenario Planning**（情境規劃） | 對多個未來情境做準備 | 不確定環境下的願景 | 2 |

### 4.3 案例框架 / Case Frameworks

| 框架 | 一句話用途 | 何時用 | 階段 |
| --- | --- | --- | --- |
| **Profitability Framework**（獲利框架） | 利潤 = 收入 − 成本，逐層拆 | 「為什麼賺/不賺錢」 | 4 |
| **Market Sizing**（市場規模估算） | 由上而下 / 由下而上估市場大小 | 機會評估、進入決策 | 3 |
| **M&A Framework** | 戰略理由→標的分析→盡職調查→綜效 | 併購評估 | 3,8 |
| **Pricing Framework**（訂價框架） | 成本/競爭/價值 三種訂價邏輯 | 訂價決策 | 7 |
| **Market Entry**（市場進入） | 要不要進、怎麼進、進入模式 | 新市場決策 | 3 |

### 4.4 商業設計 / Business Design

| 框架 | 一句話用途 | 何時用 | 階段 |
| --- | --- | --- | --- |
| **Business Model Canvas** | 9 格畫出商業模式全貌 | 商業/服務模式設計 | 7 |
| **Design Thinking** | 同理→定義→發想→原型→測試 | 以使用者為中心的方案設計 | 7 |
| **Customer Journey**（顧客旅程） | 畫出顧客每個接觸點的體驗 | 服務設計、痛點定位 | 1,7 |
| **Jobs-to-be-Done**（待辦任務理論） | 顧客「雇用」產品來完成什麼任務 | 需求洞察、產品定位 | 7 |

### 4.5 專案與變革 / Project & Change

| 框架 | 一句話用途 | 何時用 | 階段 |
| --- | --- | --- | --- |
| **WBS**（工作分解結構） | 把專案逐層拆成可執行工作包 | 專案規劃 | 6 |
| **RACI** | 釐清每件事的 Responsible/Accountable/Consulted/Informed | 角色權責 | 6 |
| **Gantt Chart**（甘特圖） | 時間軸 × 工作項目的排程視覺化 | 時程管理 | 6 |
| **Kotter 8 Steps** | 變革管理八步驟 | 組織變革推動 | 6 |
| **ADKAR** | Awareness-Desire-Knowledge-Ability-Reinforcement | 個人層級變革 | 6 |
| **OKR** | 目標與關鍵結果 | 目標對齊與追蹤 | 2,6,8 |
| **Balanced Scorecard**（平衡計分卡） | 財務/顧客/流程/學習成長 四構面 | 績效衡量 | 8 |
| **Stakeholder Map**（利害關係人地圖） | 依影響力×關注度定位關係人 | 變革溝通策略 | 6 |

### 4.6 財務分析 / Financial Analysis

| 框架 | 一句話用途 | 何時用 | 階段 |
| --- | --- | --- | --- |
| **ROI**（投資報酬率） | (效益 − 成本) / 成本 | 投資值不值得 | 8 |
| **NPV**（淨現值） | 把未來現金流折現後加總 | 跨期投資決策 | 8 |
| **IRR**（內部報酬率） | 使 NPV = 0 的折現率 | 投資方案比較 | 8 |
| **Payback Period**（回收期） | 多久回本 | 風險與流動性評估 | 8 |
| **Break-even**（損益兩平） | 收入 = 成本 的銷量/價格點 | 訂價、產能決策 | 7,8 |
| **Sensitivity Analysis**（敏感度分析） | 關鍵假設變動對結果的影響 | 風險評估 | 8 |

### 4.7 營運 / Operations

| 框架 | 一句話用途 | 何時用 | 階段 |
| --- | --- | --- | --- |
| **Lean**（精實） | 消除浪費、只留增值活動 | 流程改善 | 7 |
| **Six Sigma**（六標準差） | 用 DMAIC 降低變異與缺陷 | 品質改善 | 7 |
| **5 Whys**（五個為什麼） | 連問五次「為什麼」挖到根因 | 根因分析 | 1,4 |
| **Fishbone / Ishikawa**（魚骨圖） | 從多個面向（人機料法環）找原因 | 根因結構化 | 1,4 |
| **PDCA** | Plan-Do-Check-Act 持續改善循環 | 改善的迭代節奏 | 8 |
| **Pareto Analysis**（柏拉圖分析） | 用圖找出少數關鍵問題 | 問題排序 | 4 |
| **Value Stream Mapping**（價值流圖） | 畫出端到端流程的時間與浪費 | 流程診斷 | 1,7 |

---

## 4.8 重點框架深化：MECE / Issue Tree / 假設形成 / Deep-Dive: MECE, Issue Tree, Hypothesis Formation

> §4 的表格每個框架只有一句話。本節把三個**最常用、最容易做錯**的框架展開成操作規則。
> 深化內容參考自 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills) 之 `methodology.md`（MIT），已重新以本方法論語言改寫。

### 4.8.1 MECE 操作規則

| 規則 | 說明 |
| --- | --- |
| **每一層都要互斥窮盡** | 同一層的子項不重疊（互斥）、合起來涵蓋全部（窮盡）；不能有重複或遺漏的分類 |
| **依邏輯拆，不依直覺拆** | 用商業邏輯、資料結構或既有框架來拆，不要憑感覺隨意分組 |
| **初期 2-3 層就好** | 一開始拆 2-3 層 MECE 即可；要不要再往下鑽，依研究需要決定 |
| **驗證方法** | 拆完問自己：有沒有哪個情況兩個分類都算得進去？（不互斥）有沒有哪個情況哪個分類都不算？（不窮盡）|

### 4.8.2 Issue Tree 建構規則

| 規則 | 說明 |
| --- | --- |
| **用商業邏輯公式拆** | 優先用可量化的商業公式當拆解骨架。例：`市場規模 = 用戶數 × 滲透率 × 付費率 × 單價`；`利潤 = 收入 − 成本`；每個因子再往下拆 |
| **多維度拆解** | 可用的切法：客戶類型（B2B / B2C / C2C）、時間軸（歷史 / 現況 / 預測）、競爭比較（同業標竿 / 區域差異）|
| **拆到「可被快速查證」為止** | 拆解的終點，是拆到「能用一次快速資料查證就能驗的」顆粒度，不要拆過頭也不要拆不夠 |
| **每個葉節點都要可回答** | Issue Tree 的每個末端子問題，都必須是「找得到資料就能回答」的問題 |

### 4.8.3 假設形成規則 / Hypothesis Formation

| 步驟 | 說明 |
| --- | --- |
| **1. 初步推理** | 先用產業經驗與常識做「初步判斷」，形成方向 |
| **2. 快速查證** | 做 5-10 次快速搜尋取得框架資訊，**不是**做完整研究 — 只是驗證方向對不對 |
| **3. 形成假設** | 把判斷寫成「高機率的判斷 + 明確的驗證路徑」 |
| **關鍵屬性** | 假設必須是**可驗證的** — 要能指出「哪些資料可以證明或推翻它」。不可驗證的不是假設，是猜測 |

### 4.8.4 資料蒐集的三層搜尋策略 / 3-Layer Search Strategy

驗證假設、填充 Issue Tree 時，搜尋分三層，由粗到細：

| 層 | 目標 | 範例 |
| --- | --- | --- |
| **Layer 1：框架** | 取得分類、定義 | 市場如何分類、關鍵名詞定義 |
| **Layer 2：核心指標** | 取得量化數據 | 市場規模、成長率、市占龍頭 |
| **Layer 3：細節** | 取得佐證 | 案例、使用者行為、細部數據 |

**交叉驗證要求**：關鍵數據至少 **2-3 個來源** 交叉驗證；優先採用公司財報、權威研究機構、產業出版品。

---

## 5. 框架組合鏈 / Framework Combination Chains

多數商業問題不是單一框架，而是框架鏈。以下是常見組合，可直接套進八階段：

| 情境 | 框架鏈 | 落在哪幾個階段 |
| --- | --- | --- |
| **整體策略規劃** | PESTEL → Porter's 5 Forces → 3C → SWOT → Issue Tree | Stage 2-3 |
| **獲利改善 / 企業轉型** | Profitability Analysis → 5 Whys / Fishbone → Value Chain → Lean / Six Sigma | Stage 4, 7 |
| **併購評估** | 戰略理由 → Market Sizing → Due Diligence → NPV / IRR → Synergies | Stage 3, 8 |
| **新市場進入** | PESTEL → Market Sizing → Porter's 5 Forces → Market Entry → NPV | Stage 3, 8 |
| **轉型專案推動** | Issue Tree → WBS → RACI → Kotter / ADKAR → OKR → Balanced Scorecard | Stage 6, 8 |
| **問題定義到報告** | SCQ → Day-1 Answer → MECE → Issue Tree → Pyramid Principle | Stage 4-5 |

> 本方法論的 **AI 轉型八階段** 本身就是一條「在地化的框架鏈」 — 把上述經典框架在地化、AI 化後串成的標準顧問流程。

---

## 6. 框架文件展開格式 / Per-Framework Expansion Format

顧問若要把某個框架展開成完整 worksheet（給客戶或新顧問用），建議統一格式：

```text
框架名稱（中 / EN）
├─ 起源 / Origin：誰提出、為什麼
├─ 核心概念 / Core Concept：一段話 + 一張示意圖
├─ 步驟 / Steps：編號清單
├─ 套用方式 / Application：怎麼動手做
├─ 真實範例 / Example：一個具體商業情境的拆解
├─ 常見錯誤 / Common Pitfalls：3-5 個 anti-pattern
└─ 對應階段 / Maps to：本方法論八階段的哪幾個
```

此格式參考自 yoichiojima-2/consultant 之框架文件結構，並加上「對應階段」一欄與本方法論對齊。

---

## 7. 引用與授權 / Citation & License

本框架庫之框架清單、分類與「框架選擇器」「框架組合鏈」概念，參考並改寫自 [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant)（MIT License，作者 @yoichiojima-2）。本檔已重新以本方法論語言改寫，並對應到八階段顧問結構；經典顧問框架本身（MECE、Porter's 5 Forces 等）為公開領域之管理知識。

完整引用與授權說明見 [`../90_References/CONSULTANT_FRAMEWORKS_REFERENCE.md`](../90_References/CONSULTANT_FRAMEWORKS_REFERENCE.md)。

The framework list, taxonomy, and the "framework selector" / "combination chains" concepts in this library are referenced from and rewritten based on [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant) (MIT License, by @yoichiojima-2). This document has been re-expressed in this methodology's language and mapped to the eight-stage consulting structure; the classic consulting frameworks themselves (MECE, Porter's 5 Forces, etc.) are public-domain management knowledge. Full citation: `../90_References/CONSULTANT_FRAMEWORKS_REFERENCE.md`.
