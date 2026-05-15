# 方法論的科學邏輯：為什麼這份報告經得起辯論

> 🌐 English version: [METHODOLOGY_SCIENTIFIC_LOGIC_EN.md](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md)
>
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技

更新日期：2026-05-15

---

> **本文回答的問題**：為什麼這套方法論這樣設計？為什麼是 8 階段而不是 5 個或 12 個？為什麼資料要這樣流？為什麼案例要寫成 Benchmark 格式？**最終回答的問題是**：客戶 / 董事會 / 監管機構在追問時，這份顧問報告憑什麼站得住腳？
>
> **核心主張**：這套方法論不是顧問經驗的整理，而是一套**科學管理的邏輯閉環** —— 每一步都符合可觀察、可量化、可重複、可證偽、可審核的科學方法五條件。

---

## 1. 為什麼顧問報告需要「科學辯論能力」

傳統顧問報告失敗的場景：

| 場景 | 客戶質疑 | 顧問常見回答 | 為什麼失敗 |
| --- | --- | --- | --- |
| 董事會質詢 | 「你怎麼知道我們公司在 L2？」 | 「依照我們訪談的判斷...」 | 主觀判斷不可驗證 |
| 內稽追問 | 「為什麼先做客服而不是業務？」 | 「我們經驗上...」 | 經驗不可被審核 |
| 監管檢查 | 「萬一 AI 出事誰負責？」 | 「我們有規範...」 | 規範若無 Audit 鏈不算數 |
| 換顧問 | 「上一家說我們在 L3，你說 L2，誰對？」 | 「我們方法不同」 | 方法論不可重複 = 不科學 |

**Tiger AI 方法論的設計目標**：讓上述每個追問都有**可驗證的數字 + 可審核的證據 + 可重複的步驟**作答。

---

## 2. 科學方法的 5 條件 vs 本方法論的對應

| 科學條件 | 定義 | 本方法論如何符合 |
| --- | --- | --- |
| **1. 可觀察 (Observable)** | 結論建立在可被他人看到的證據上 | Stage 1 訪談錄音 + 系統盤點表 + As-Is Swimlane 畫面標註；每筆都有時間戳與來源 |
| **2. 可量化 (Quantifiable)** | 結論可被換算為數字而非形容詞 | Stage 2 雷達 0-4 分；Stage 4 Impact×Effort 計分；Stage 5 80/20 影響面積數字；Stage 8 價值追蹤 5 維度 |
| **3. 可重複 (Reproducible)** | 不同顧問用同樣方法應得相近結論 | 三套 Reference Model（APQC / SCOR / Tiger AI L1-L5）是公開標準；40 題訪談題庫；MECE 分類紀律 |
| **4. 可證偽 (Falsifiable)** | 結論有明確可被否證的條件 | Stage 6 Stage Gate Criteria 明列「達成 / 未達成」；驗收清單每項有觀察條件；目標未達 = 假設被否證 |
| **5. 可審核 (Auditable)** | 過程可被第三方獨立查核 | Stage 8 Audit Log（LLM 呼叫、權限變更、Skill 部署、Reviewer 簽核全鏈），保存週期定義 |

> **這 5 條件不是裝飾**。任何顧問結論若無法回應這 5 條件，就不算科學管理，只是經驗分享。

---

## 3. 八階段為什麼必須是這 8 個（不是 5 個、不是 12 個）

從科學方法反推：要做出一份可辯論的 AI 轉型報告，**必須走完 5 個推理動作**，且每個動作之間有嚴格的資料依賴關係：

| 推理動作 | 對應 Stage | 沒做這步會發生什麼 |
| --- | --- | --- |
| **A. 觀察現況** | Stage 1 As-Is | 沒有客觀現狀基準，所有後續結論都是猜的 |
| **B. 套國際座標** | Stage 2 Reference Model | 沒有外部座標，「我們做得不夠好」是顧問主觀說法 |
| **C. 客戶自己展開 Ideal Practice** | Stage 3 Best Practice | 沒有客戶簽名的目標，差距會被客戶否認 |
| **D. 量化差距** | Stage 4 Gap Analysis | 沒有結構化差距，無法排優先順序 |
| **E. 收斂核心問題** | Stage 5 Problem Definition | 沒有 80/20，會「全部都重要」 = 全部都做不完 |
| **F. 設定可達目標** | Stage 6 Phased Goals | 沒有階段拆解，會試圖一次到位 = 失敗 |
| **G. 設計藍圖** | Stage 7 To-Be Design | 沒有 To-Be 圖，Roadmap 落不到組織與系統 |
| **H. 執行與治理** | Stage 8 Implementation | 沒有變革管理 + 價值追蹤 + Audit，藍圖是廢紙 |

**為什麼正好是 8 個**：每個推理動作都不可被合併或省略，**省略任一步就會有一個質詢無法回答**。例如：

- 省略 Stage 2 → 「你的標準是什麼？」無解
- 省略 Stage 4 → 「為什麼先做這個不做那個？」無解
- 省略 Stage 6 → 「為什麼是 9 個月不是 3 個月？」無解
- 省略 Stage 8 → 「怎麼證明變好了？」無解

> 5 個階段太粗（漏掉 Reference Model、Phased Goals、Change Mgmt）；12 個階段太細（出現重複的子步驟）。**8 個是「可被辯論的最小完整推理鏈」**。

---

## 4. 為什麼資料要這樣流（每條箭頭的科學原因）

```
Stage 1 ──────────► Stage 2 ──────────► Stage 3 ──────────► Stage 4
As-Is              Reference Model      Best Practice        Gap
觀察到的現實        套國際標準座標        定義具體卓越          客觀差距盤點
                                                              │
                                                              ▼
Stage 8 ◄────────── Stage 7 ◄────────── Stage 6 ◄────────── Stage 5
Implementation      To-Be Design        Phased Goals         Problem
落地 + 變革         未來藍圖             階段拆解              收斂核心問題
                                                              
        ↑                                                     ↓
        └─── 每季回頭核對 Stage 2 雷達（閉環驗證）────────────┘
```

#### 每條箭頭的因果必然性

| 箭頭 | 為什麼必須這個方向 | 反向會怎樣 |
| --- | --- | --- |
| **Stage 1 → 2** | 必須先有「現實」才有東西可被「標準」對照 | 若顛倒：先套標準再看現實，會 cherry-pick 證據 |
| **Stage 2 → 3** | 必須先確定「結構完整」才談「客戶 Ideal Practice」 | 若顛倒：先談 Ideal 會跳過結構缺口 |
| **Stage 3 → 4** | 必須先讓**客戶自己簽署 Ideal Practice 定義表**，才能算「客戶 Ideal − 客戶 As-Is = Gap」 | 沒有 3 的客戶簽名，差距就是顧問主觀說，客戶可推翻 |
| **Stage 4 → 5** | 必須先有「全部差距」才能 80/20 收斂出「核心問題」 | 沒有 4，問題定義變成「拍腦袋」 |
| **Stage 5 → 6** | 必須先鎖定「核心問題」才設定「目標」 | 沒有 5，目標會散 |
| **Stage 6 → 7** | 必須先有「階段目標」才設計「藍圖」 | 沒有 6，藍圖會嘗試一次到位 |
| **Stage 7 → 8** | 必須先有「藍圖」才談「執行」 | 沒有 7，執行變盲動 |
| **Stage 8 ↑ Stage 2（季度閉環）** | 執行後必須回頭看「標準雷達是否變圓」 | 沒有閉環，PoC 做完無法證明結構真的變好 |

> **這就是「閉環」的科學意義**：不是「做完就好」，而是「結果可被回頭驗證 / 反證」。

---

## 5. 為什麼 Reference Model 是 4 層架構（不是 3 層、不是 5 層）

從成熟度的「**抽象度 × 變動頻率**」推導（詳見 [`CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 2.7）：

| 抽象度 | 變動頻率 | 對應層 | 為什麼不能合併或省略 |
| --- | --- | --- | --- |
| 最抽象 | 年 | **L1 Governance** | 戰略與政策不能跟流程混（變動頻率差 10×）|
| 抽象 | 季-年 | **L2 Business** | 業務職能不能跟資料服務混（職能變動慢於服務）|
| 中 | 月-季 | **L3 Information** | 資料服務不能跟硬體網路混（服務抽象、硬體具象）|
| 最具象 | 週-月 | **L4 Technical** | 硬體網路若混入業務層會被綁死技術選型 |

**3 層不夠**：通常少了 L3 Information，會把資料服務硬塞進 L2 或 L4 → 失焦。
**5 層太多**：通常多切的那層其實是 L2 或 L3 的子層 → 違反 MECE 原則。

> **Dragon1 學派堅持 4 層**就是這個科學原因。Tiger AI Enterprise AI Reference Model 嚴格遵守。

---

## 6. 為什麼案例要寫成 Benchmark-grade（不是敘事故事）

科學要求「**可重複**」 —— 同一個案例給不同顧問 / 不同客戶讀，應該得出相近的「差距估算」。

- **敘事故事**：「某公司做了 AI 質檢，成功了」→ 不可重複（每個讀者解讀不同）
- **Benchmark-grade 案例**：9 必填欄位（產業 + 規模 + 起點 L + 終點 L + 期間 + 投入 + Wins + Failures + 適用條件）→ **可重複**（任何讀者算出來的差距、時間、預算都會落在相近範圍）

詳見 Tool 3.5 Cases-as-Benchmarks。

> **這就是為什麼 Tiger AI 的 7 個案例都用同一個 9 欄位範本** —— 不是為了一致性的美感，是為了**可重複性**這個科學條件。

---

## 7. 顧問報告的「科學辯論能力」清單

當客戶 / 董事會 / 監管機構問下列問題，本方法論的具體回答位置：

| 質詢 | 在報告哪裡可以回答 | 用什麼證據 |
| --- | --- | --- |
| 「你怎麼知道我們在 L2？」 | §3 As-Is + §4 RM Mapping | 訪談錄音、系統盤點、Reference Model 雷達 0-4 分 |
| 「為什麼選 APQC / Tiger AI L1-L5？」 | §4.1 + Tool 2.5 | 10 條件合格度評分表 |
| 「你怎麼算出我們距理想多遠？」 | §5 + §6.1 | **客戶自己簽的 Ideal Practice 定義表** + 案例 Benchmark；Gap = (你簽的 Ideal − 你的 As-Is)，分子分母都是你說的 |
| 「為什麼先做客服不做業務？」 | §6.2 + §6.3 | Impact × Effort 矩陣 + Prioritization Score |
| 「為什麼核心問題是『知識資產化』？」 | §7 | 80/20 影響面積數字 + 5 Whys 推導鏈 |
| 「為什麼是 9 個月不是 3 個月？」 | §8 + Tool 6.3 | Phased Goals 拆解 + 組織吸收力評估（6 維度）+ 對標案例期間 |
| 「萬一 PoC 失敗怎麼辦？」 | §13.2 | Risk Register + 觸發條件 + Mitigation Owner |
| 「怎麼證明做完後真的變好了？」 | §13.1 + 每季雷達回顧 | 價值追蹤矩陣 5 維度 + Stage 2 雷達前後對比 |
| 「AI 出事誰負責？」 | §12.1 + Tool 8.8 | RACI 矩陣 + AI Ethics Checklist + Audit Log 全鏈 |
| 「你的方法論能不能被別人複製？」 | 整份方法論 | Apache 2.0 + GitHub + Tool 2.5 自評合格度 9/10 |
| 「上一家顧問說我們在 L3，你說 L2，誰對？」 | §3 評分證據 | 公開的 0-4 分量尺 + 每分必有觀察證據 → **可被獨立第三方驗證** |
| 「為什麼這 8 階段不是 5 個或 12 個？」 | 本文 §3 | 「可被辯論的最小完整推理鏈」論證 |

> **報告變成可辯論的文件**：客戶不是「相信顧問的權威」，而是「順著證據鏈自己也能推到同一個結論」。這才是科學管理。

---

## 8. 跟其他主流顧問方法論的對比

| 方法論 | 強項 | 缺什麼（從科學完整性看）|
| --- | --- | --- |
| **McKinsey Issue Tree + Pyramid** | 邏輯推理嚴密、敘事強 | 沒 Reference Model（缺座標）、沒 Phased Goals（缺階段拆解） |
| **BCG Digital Maturity** | 5 階段成熟度清楚 | 沒 Best Practice 量化（卓越靠顧問描述）、沒組織吸收力評估 |
| **Gartner AI Maturity** | 業界認可 | 沒 As-Is 訪談紀律、沒可重複的案例 Benchmark |
| **MIT AI Capability** | 學術嚴謹 | 缺 Implementation & Change 落地工具 |
| **Tiger AI（本方法論）** | **8 階段完整推理鏈 + 4 層 Reference Model + Cases-as-Benchmarks 閉環** | 新興（2025 啟動，案例累積中）|

> **不是說其他方法論不好** —— 是說它們各有強項但**閉環不完整**。Tiger AI 的設計目標就是補完這個閉環，讓報告**從首頁到尾頁每一句話都有上一句話的證據**。

---

## 9. 對學術界與監管者的可被引用性

本方法論能被學術社群驗證、引用、改進的原因：

1. **公開**：Apache 2.0、GitHub repo、bilingual zh/en
2. **可被合格度自評**：用 Tool 2.5 自評，10 條件達成 9 條
3. **理論根源透明**：Rosemann BPM Maturity 學派（QUT）+ CMMI + APQC + Dragon1 EA 各自註明引用
4. **跨產業驗證**：製造 / 醫院 / 行銷 / B2B / 金融 / 政府 / 教育 7 個產業案例（驗證可移植性）
5. **可被反證**：每個 Stage Gate Criteria 都有可被否證的觀察條件
6. **可被批評**：本文與 Tool 2.5 都明寫「新興、認可度累積中」的不足

> **學術引用的金標準**是「**這個方法可以被別人套到別的問題上得到相近結論嗎？**」—— Tiger AI 方法論的答案是 Yes，因為所有步驟、工具、評分標準都已公開。

---

## 10. 給顧問的實務口訣

當你寫這份報告，每一段都要能回答：

```
我這段話的證據是什麼？             ← 可觀察
我這段話的數字怎麼算的？           ← 可量化
換一個顧問用同方法會得到一樣的嗎？ ← 可重複
如果這段話錯了，我會看到什麼？     ← 可證偽
這段話的過程被誰簽過？             ← 可審核
```

**5 個問題都能答 → 這段就是科學管理**。
**有任何一題答不出 → 那段就是個人意見，要麼補證據要麼刪除**。

---

## 11. 給客戶的承諾

本方法論承諾：

1. **每一個結論都有編號的證據** —— 報告附錄 A-G 全部證據可追溯
2. **每一個數字都有計算公式** —— 沒有「依顧問判斷」這種句子
3. **每一個建議都對應 Stage Gate Criteria** —— 你能驗收
4. **每一個風險都有 Trigger + Owner + Mitigation** —— 你能管理
5. **每一個案例都是 Benchmark-grade** —— 你能自己算差距
6. **每一個階段結束都回頭核對 Reference Model 雷達** —— 你能看到結構真的變圓

**如果你覺得任何一段是「顧問權威說了算」，請指出來。我們會補證據、改算法、或刪掉那段話。**

---

## 12. 結語：這套方法論本身就是個 Reference Model

最後一個自指的觀察：

- 本方法論用 Tool 2.5 的 10 條件**自評合格度**：9 條達成（缺第 6 條「廣泛產業認可」尚在累積）
- 本方法論用 Tool 2.6 的 5 推導提問**自我盤點 component**：8 階段 + 4 層 + 5 維追蹤俱全
- 本方法論用 Tool 2.7 的 4 層架構**自我組織**：Governance（本文）+ Business（Stage 1-8）+ Information（工具表 + 案例）+ Technical（GitHub repo + AGENTS.md + CLAUDE.md）
- 本方法論用 Tool 3.5 的 Cases-as-Benchmarks**自證可被複製**：7 產業案例都按 9 欄位寫

> **這就是科學管理的閉環**：方法論不只用來分析別人，**方法論能用自己的工具分析自己** —— 這在學術界叫做 "self-referential consistency"，是嚴謹理論的標誌。

---

## 參考文獻 / References

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- APQC (2024). *Process Classification Framework Version 7.3*.
- CMMI Institute (2018). *CMMI for Development V2.0*.
- Dragon1 (n.d.). *Enterprise Architecture Reference Model*. <https://www.dragon1.com/reference-models/enterprise-architecture-reference-model>
- Pyramid Principle: Minto, B. (2009). *The Pyramid Principle*.
- 80/20: Koch, R. (1997). *The 80/20 Principle*.
- 5 Whys: Ohno, T. (1988). *Toyota Production System*.
- Change Management: Kotter, J. (1996). *Leading Change*. Prosci ADKAR.

---

授權與引用 / License & Citation

本文為 Apache License 2.0；可使用、修改、商業利用，唯需保留 [`../NOTICE`](../NOTICE) 檔之署名。
