# 06 Delivery — 交付驗收與接案營運

## 一、本目錄定位

本目錄有兩個層次，合起來解決一件事：**怎麼把顧問案專業地、可規模化地「做成生意」並「交付出去」。**

- **交付驗收層**：定義本方案對客戶交付什麼、如何驗收、哪些 evidence 證明已完成。
- **接案營運層**：定義整個接案生命週期（Sales → Delivery → Support）、角色 SOP、商業文件範本、營運檢查清單、定價與風險管理。

`01`-`03` 是「顧問做什麼」（方法論）；`05` 是「怎麼讓客戶想買」（售前）；本目錄是「**簽約之後，怎麼把整個案子當成一門生意跑完、跑乾淨、跑得可重複**」。它要解決的問題是：**一個顧問公司若只有方法論、沒有營運框架，會被範圍蔓延拖垮、會交接斷層、會出資安事故、會無法規模化。**

使用本目錄的人：專案經理、顧問、業務（Closer）、技術主導、客戶端 Owner。

## 二、在方法論中的位置

| 軸 | 對應 |
| --- | --- |
| 三段式服務流程 | **交付（Deliver）** + 把三段都包進「生意」的營運外框 |
| 八階段顧問結構 | 對應八階段的**交付與驗收**；接案生命週期是八階段的「商業外殼」 |
| **3 階段合約模型（顧問閉環）** | **Phase A 診斷 2W → Phase B 策略 4W → Phase C 落地 24M + 季度雷達回看** —— 接案生命週期的 Delivery 段，就是 Phase A→B→C 的閉環 |
| L1-L5 成熟度 | 交付包驗收涵蓋 L1-L5 各級的交付物 |
| 接案生命週期 | **本目錄就是接案生命週期（Sales → Delivery → Support）的本體** |

> 🔁 **接案生命週期 ↔ 顧問閉環**：本目錄的「Delivery 段」**不是 6 週 marathon**，而是 [`../03_Consulting_Report/README.md`](../03_Consulting_Report/README.md) §4 與 [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 描述的**閉環**：Phase A 中期評估報告簽署 → Gate A → Phase B 完整報告 → Gate B → Phase C 24 個月實作 + **每季雷達回看**（科學管理的反證機制）。Support 段則對應 Phase C 之後的 Retainer / Maintenance。

## 三、目標與效益

| 目標 | 效益 |
| --- | --- |
| 明確的交付包與驗收標準 | 客戶與顧問對「做完了沒」有共識，不爭議 |
| 完整的接案生命週期 | 從找案到結案有 SOP，不靠個人手藝 |
| 角色 SOP | 可規模化（不是一個人做所有事）、交接不斷層 |
| 商業文件範本 | SOW/合約/發票/變更單現成，不每次重寫 |
| 營運檢查清單 | pre-project/security/QA/handover/offboarding 不漏項 |
| 定價與風險框架 | 不被範圍蔓延吃掉利潤、知道何時該說「不」 |

**若跳過本目錄**：方法論很強但生意做不大 —— 範圍蔓延、做白工、交接斷層、資安事故、關鍵人員依賴、呆帳。

## 四、使用流程與邏輯

```text
接案生命週期（ENGAGEMENT_LIFECYCLE）：
  Sales（Lead → Discovery → Proposal → Contract）
     → 用 BUSINESS_DOCUMENT_TEMPLATES（提案、SOW）
     → 用 PRICING_AND_RISK（定價、風險登記）
  Delivery（Kickoff → Build → Test → Security → Handover）
     → 用 DELIVERY_CHECKLISTS（pre-project / security / QA / handover）
     → 用 DELIVERY_PACKAGE_AND_ACCEPTANCE（交付包驗收）
     → 用 DELIVERY_ROLE_SOPS（誰負責哪一段）
  Support（Retainer → Maintenance → Offboarding）
     → 用 DELIVERY_CHECKLISTS（offboarding）
全程：7 Pillars 為底線原則
```

| 步驟 | 誰 | 何時 | 輸入 | 輸出 |
| --- | --- | --- | --- | --- |
| 跑生命週期 | PM | 接案全程 | `ENGAGEMENT_LIFECYCLE` | 各階段推進 |
| 出商業文件 | Closer / PM | Sales / 變更時 | `BUSINESS_DOCUMENT_TEMPLATES` | 提案 / SOW / 變更單 |
| 定價與評風險 | Closer / PM | Proposal / Kickoff | `PRICING_AND_RISK` | 報價 + 風險登記表 |
| 跑檢查清單 | PM / Technical Lead | 各交付階段 | `DELIVERY_CHECKLISTS` | 各階段檢查通過 |
| 交付驗收 | PM + 客戶 | Handover | `DELIVERY_PACKAGE_AND_ACCEPTANCE` | 客戶簽收 |
| 角色分工 | 全團隊 | 全程 | `DELIVERY_ROLE_SOPS` | 清楚的責任與交接 |

> 邏輯：`ENGAGEMENT_LIFECYCLE` 是主幹（生命週期）；其他 5 份是主幹各階段的工具 —— 文件範本、定價風險、檢查清單、角色 SOP、交付驗收。**7 Pillars**（客戶自持、客戶付費、資安優先、徹底測試、完整文件、乾淨交接、明確範圍）貫穿全程。

## 五、檔案說明

### 交付驗收層

| 檔案 | 用途 |
| --- | --- |
| `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` | AI 成熟度診斷、L1-L5 課程、L4 Hermes Agent、八階段顧問診斷報告的交付包清單與逐項驗收表。 |

### 接案營運層（改寫自 Mirza Iqbal / next8n.com 之 Workflow Automation Delivery Framework，MIT，已 generalize 為 L1-L5 AI 轉型顧問情境；引用見 `../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`）

| 檔案 | 用途 |
| --- | --- |
| `ENGAGEMENT_LIFECYCLE.md` | 接案三階段生命週期（Sales → Delivery → Support）、每階段的子階段與產出、7 Pillars、生命週期 × 八階段對照、啟動每個專案前的對照表。 |
| `DELIVERY_ROLE_SOPS.md` | 7 個交付角色 SOP（Lead Gen / Sales Rep / Closer / PM / Technical Lead / Developer / Client），每個角色的職責、關鍵交付物、交接點、合作對象、所屬生命週期階段，加角色 × 生命週期矩陣與交接黃金規則。 |
| `BUSINESS_DOCUMENT_TEMPLATES.md` | 8 種商業文件範本：提案、SOW、MSA 大綱、變更單、發票、交接文件、維運合約、關鍵 email。**附法律免責 —— 範本骨架非法律文件，須法務審閱。** |
| `DELIVERY_CHECKLISTS.md` | 5 大營運檢查清單：pre-project、security、QA、handover、offboarding；與方法論 Stage Gate 的差異說明。 |
| `PRICING_AND_RISK.md` | 定價的兩個分離原則、4 種定價模型、階梯式產品線、接案常見風險與緩解、何時該說「不」、事故處理流程。 |

### `*_EN.md`

部分檔案的英文版 sibling。

## 六、與其他目錄的對應

| 目錄 | 與本目錄的關係 | 資料流 |
| --- | --- | --- |
| `01_Assessment` | 診斷對應接案生命週期的 Sales 階段 | `01` ↔ `06` Sales |
| `02_Course_Design` | 課中產出物進交付包驗收 | `02` 產出 → `06` 驗收 |
| `03_Consulting_Report` | 顧問報告是交付包的核心交付物 | `03` 報告 → `06` 驗收 |
| `05_Sales` | 簡報的報價/方案分級對應接案生命週期與定價 | `05` deck ↔ `06` 定價 |
| `00_Overview` | 接案生命週期是把故事線變成生意的外框 | `00` 故事 → `06` 營運 |
| `90_References` | 接案營運層的第三方引用（Mirza Iqbal 框架）| `90` 引用 → `06` |

## 七、常見用法情境

- **接到新案**：PM 用 `ENGAGEMENT_LIFECYCLE.md` 的「啟動前對照表」確認準備就緒，用 `DELIVERY_ROLE_SOPS.md` 指派角色。
- **要簽約**：Closer 用 `BUSINESS_DOCUMENT_TEMPLATES.md` 的 SOW 範本（範圍內/外寫清楚），用 `PRICING_AND_RISK.md` 定價。
- **每個交付階段**：對照 `DELIVERY_CHECKLISTS.md` 跑 pre-project / security / QA / handover 清單。
- **交付給客戶**：用 `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` 逐項驗收 + `BUSINESS_DOCUMENT_TEMPLATES.md` 的交接文件。
- **客戶不斷加需求**：用 `PRICING_AND_RISK.md` 的範圍蔓延緩解 + `BUSINESS_DOCUMENT_TEMPLATES.md` 的變更單。
- **結案**：跑 `DELIVERY_CHECKLISTS.md` 的 offboarding 清單。

---

## ⭐ 跨主題對照：5 個核心主題去哪查

整本方法論有 5 條主動脈，貫穿所有目錄。本目錄與它們的關聯如下：

| 跨主題 | 主檔案位置 | 本目錄如何接 |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 三引擎共讀** | 根 [`README.md`](../README.md) §🌟 ｜ [`AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | 接案中可調動三引擎分工：Antigravity 跑客戶會議 / Codex 稽核 SOW 與報告草稿 / Claude Code 跑 Phase B 模擬與多視角檢視 |
| 🎓 **成熟理論（7 大支柱）** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | 7 Pillars 的「資安優先 / HITL」對應 Sociotechnical Systems & Trust（Bostrom / Dietvorst / Glikson）；範圍蔓延 / 跳級失敗對應 Real Options + Absorptive Capacity 失敗模式 |
| 📚 **L1-L5 課程教育** | [`../02_Course_Design/`](../02_Course_Design/) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md) | 交付包驗收涵蓋 L1-L5 各級的可驗收交付物；課中產出物進入 [`DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](DELIVERY_PACKAGE_AND_ACCEPTANCE.md) 逐項驗收 |
| 🔁 **顧問方案 / 8 階段 + Phase A→B→C 閉環** | [`EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **本目錄就是顧問閉環的「商業外殼」** —— 接案生命週期 Sales→Delivery→Support 對應 Phase A→B→C + 季度雷達回看 |
| 📖 **參考資料 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | 接案營運層引用 Mirza Iqbal / next8n.com 的 Workflow Delivery Framework（MIT），詳見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) |
