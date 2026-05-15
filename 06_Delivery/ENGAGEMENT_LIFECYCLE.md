# 顧問接案生命週期 / Consulting Engagement Lifecycle

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **引用備註 / Attribution:** 本接案生命週期、7 Pillars、Sales→Delivery→Support 三階段架構，參考並改寫自 **Mirza Iqbal**（next8n.com）之 *Workflow Automation Delivery Framework*（MIT License）。本檔在其基礎上**重新以本方法論語言改寫，並從「n8n 自動化交付」generalize 為「L1-L5 AI 轉型顧問交付」**，對應八階段顧問結構。引用與授權說明見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)。
> The engagement lifecycle, 7 Pillars, and Sales→Delivery→Support three-phase structure are referenced from and rewritten based on **Mirza Iqbal**'s (next8n.com) *Workflow Automation Delivery Framework* (MIT License), re-expressed in this methodology's language and generalized from "n8n automation delivery" to "L1-L5 AI transformation consulting delivery."

---

## 1. 兩個正交的軸 / Two Orthogonal Axes

本方法論先前的核心是 **八階段顧問結構**（診斷方法論）。但「怎麼診斷」不等於「怎麼把一個顧問案當成生意跑完」。本檔補上後者。

| 軸 | 是什麼 | 文件 |
| --- | --- | --- |
| **方法論軸**（縱向）| 怎麼診斷、怎麼教、怎麼產出報告 | 八階段、L1-L5、`CONSULTING_TOOLKIT_TEMPLATES.md` |
| **生命週期軸**（橫向）| 怎麼找案、簽約、交付、收尾、續約 | **本檔** |

> 八階段是「顧問做什麼」；接案生命週期是「公司怎麼把這件事變成可重複的生意」。兩軸同時跑。

---

## 2. 三階段接案生命週期 / The Three-Phase Engagement Lifecycle

### Phase 1：Sales（銷售）

| 階段 | 內容 | 產出 | 對應本方法論 |
| --- | --- | --- | --- |
| Lead Qualification | 判斷潛在客戶是否合格（規模、預算、痛點、決策權）| 合格 / 不合格判定 | 10 題快速問卷（`01_Assessment`）|
| Discovery | 深入了解客戶現況、系統、目標 | Discovery Notes | 八階段 Stage 1；25/50 題問卷 |
| Proposal | 提出方案、範圍、時程、報價 | 提案書 + SOW 草稿 | `05_Sales` deck outlines；`BUSINESS_DOCUMENT_TEMPLATES.md` |
| Contract | 簽約、確認範圍與付款 | 已簽 SOW / 合約 | `BUSINESS_DOCUMENT_TEMPLATES.md` |

### Phase 2：Delivery（交付）

| 階段 | 內容 | 產出 | 對應本方法論 |
| --- | --- | --- | --- |
| Kickoff | 啟動會議、確認團隊、環境、資料、權限 | Kickoff 紀錄 + 環境就緒 | `DELIVERY_CHECKLISTS.md` pre-project |
| Build | 執行八階段診斷 + L1-L5 課程 + PoC 建置 | 各階段交付物（Prompt/Skill/Workflow/Agent）| 八階段、`02_Course_Design` |
| Test | 驗證 PoC、Workflow、Agent 可運作 | 測試紀錄 | `DELIVERY_CHECKLISTS.md` QA |
| Security Audit | 資安檢核：權限、資料邊界、Audit Log | 資安檢核報告 | `DELIVERY_CHECKLISTS.md` security；Stage Gate 治理 |
| Handover | 交付包、文件、Runbook、知識轉移 | Handover Document | `DELIVERY_PACKAGE_AND_ACCEPTANCE.md`；`BUSINESS_DOCUMENT_TEMPLATES.md` |

### Phase 3：Support（支援）

| 階段 | 內容 | 產出 | 對應本方法論 |
| --- | --- | --- | --- |
| Retainer Setup | 設定後續維運合約、SLA、聯絡窗口 | Retainer 合約 | `BUSINESS_DOCUMENT_TEMPLATES.md` |
| Ongoing Maintenance | 定期維護、監控、優化、新需求 | 維護紀錄、變更單 | `DELIVERY_CHECKLISTS.md`；Change Order |
| Exit / Offboarding | 合約結束、資產移交、帳號清理、知識封存 | Offboarding 紀錄 | `DELIVERY_CHECKLISTS.md` offboarding |

---

## 2.5 三階段合約模型 / The Three-Phase Contract Model（Delivery 內部）

> §2 的 **Sales → Delivery → Support** 是**生意層的生命週期**。本節的 **Phase A / B / C** 是**合約層的拆解** —— 把整個 Delivery 拆成三份可獨立簽約的合約，**每份合約結束都是客戶可下車的退場點**。完整論述見 [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md)。

### 為什麼拆成 3 階段合約

傳統顧問接案常見問題：

- 一次簽 6 個月 + 後續 24 個月，**客戶心理門檻高**，常常猶豫不簽
- 顧問提案被砍價（因為客戶覺得「整套都買承擔不起」）
- 顧問做完後客戶覺得「我不知道我買到什麼」

3 階段合約解法：

- **Phase A 診斷** — 風險低、價格低、結果具體 → 容易簽
- **Phase A 結尾有「中期評估報告」做 Deliverable** → 客戶看到具體價值才決定要不要簽 B
- **Phase B 策略** — 客戶簽完 A 已被雷達震撼，95% 會簽 B
- **Phase C 落地** — Phase B 客戶**自己簽了 Ideal Practice 定義表**，95% 會簽 C 執行

### 三階段合約對照表

| 合約階段 | 時程 | 金額（示例 700 人客戶） | 涵蓋八階段 | 退場點 (Gate) | 主要 Deliverable |
| --- | --- | --- | --- | --- | --- |
| **Phase A 診斷** | 2 週 | NT$ 80 萬 | Stage 1 + 2 + Stage 3 素材準備 | **Gate A**：客戶看完中期報告，決定是否進 B | 中期評估報告（10-15 頁，客戶簽收）|
| **Phase B 策略** | 4 週 | NT$ 200 萬 | Stage 3 Ideal Practice 共創 + Stage 4 + 5 + 6 + 7 | **Gate B**：客戶看完完整顧問報告，決定是否進 C | 完整顧問報告（14 章 30-50 頁）+ Ideal Practice 定義表（**三方簽名**）|
| **Phase C 落地** | 24 個月 | NT$ 700 萬 | Stage 8 + 季度雷達回頭核對 | **Gate C 每季**：客戶決定是否續推進 / 調整 / 暫停 | Transformation Roadmap + 變革管理 + 價值追蹤 + 季度回顧紀錄 |

### Phase A / B / C 各階段的「中止退場機制」

- **Gate A 退場**：客戶看完中期報告，不簽 B → 顧問仍交付一份有價值的評估報告，客戶可自行接手或找下一家顧問。**這就是顧問**敢設計 Gate 的原因 —— 中期報告本身就是可獨立交付的成品**。
- **Gate B 退場**：客戶簽了 Ideal Practice 但不簽 C → 顧問交付完整報告 + Ideal Practice 定義表，客戶可自行找執行夥伴。
- **Gate C 退場**（每季）：客戶決定暫停 / 中止 → 已完成的 Phase（含階段驗收）保留，未來可續做。

### 跟生意層 Sales→Delivery→Support 的對應

```text
Sales（生意層）        Delivery（生意層）              Support（生意層）
─────────────         ──────────────────              ──────────────────
Lead Qualification    Phase A 診斷 (2W, 80 萬)        Retainer Setup
Discovery       ─────►  ↓ Gate A                      Maintenance (每季)
Proposal               Phase B 策略 (4W, 200 萬)       Exit / Offboarding
Contract                ↓ Gate B
                       Phase C 落地 (24M, 700 萬)
                        ↓ Gate C 每季
```

> **3 階段合約模型住在 Delivery 階段裡面**，但每個 Gate 都可能觸發新一輪 Sales（續簽下一階段）或進入 Support（季度維運）。

### 對 Sales 團隊的 implication

- 不再賣「24 個月 980 萬」整套 → 賣「**2 週 80 萬先做診斷**」，門檻低 10×
- Sales 第一通電話的目標 = **賣出 Phase A**，不是賣出整套
- Phase A 結尾的中期報告 review 會議 = **轉化 Phase B 的關鍵時刻**
- Phase B 結尾的 Ideal Practice 簽署 = **轉化 Phase C 的關鍵時刻**

> **這就是「3 階段合約 + Gate 退場機制」對銷售的價值** —— 把一個 980 萬的 yes/no 決策，拆成三個 yes/no 決策，每個都更容易說 yes。

---

## 3. 七大支柱 / The 7 Pillars

接案交付的七條核心原則（改寫自原框架，generalize 為 AI 顧問情境）：

| # | 支柱 | 說明 |
| --- | --- | --- |
| 1 | **客戶自持（Client Hosts）** | 系統、資料、帳號運行在客戶自己的環境 / 雲；顧問不長期持有客戶資產。對應本方法論的「全地端 / Hybrid」部署選項。 |
| 2 | **客戶付費（Client Pays）** | 平台、API、模型、授權費用由客戶承擔並透明列出；顧問費與第三方費用分開。 |
| 3 | **資安優先（Security First）** | 每個交付前必過資安檢核：權限、資料邊界、Audit Log、機敏 redact。對應 Stage Gate 的治理檢查。 |
| 4 | **徹底測試（Test Thoroughly）** | PoC / Workflow / Agent 上線前用正常 + 異常案例測過。對應 Stage Gate 3F、4 的 evidence。 |
| 5 | **完整文件（Document Fully）** | 每個交付物有可被非原作者讀懂的文件、Runbook、來源追溯。 |
| 6 | **乾淨交接（Clean Handover）** | Handover 有完整清單、知識轉移、帳號權限移交，客戶能自行維運。 |
| 7 | **明確範圍（Clear Scope）** | SOW 寫清楚範圍內 / 外；範圍變動走 Change Order，不做無償擴張。 |

> 這 7 條是顧問公司「不會被客戶拖垮、不會做白工、不會出資安事故」的底線。每個交付專案開始前，團隊應對照這 7 條。

---

## 4. 生命週期 × 八階段對照 / Lifecycle × Eight-Stage Mapping

```text
Sales ─────────────┬─ Delivery ──────────────────────────┬─ Support ──────────
 Lead Qualify       │  Kickoff                            │  Retainer Setup
 Discovery ─────────┼─ Build:                             │  Maintenance
 Proposal           │    Stage 1 現況掌握                  │  Exit / Offboarding
 Contract           │    Stage 2-3 願景 / 標竿             │
                    │    Stage 4-5 差距 / 問題定義          │
                    │    Stage 6 標竿對照與多階段目標設定                    │
                    │    Stage 7 未來藍圖設計（L1-L5 課程+PoC） │
                    │  Test / Security Audit               │
                    │    Stage 8 執行導入與變革治理                │
                    │  Handover                            │
────────────────────┴─────────────────────────────────────┴────────────────────
```

- **Sales 階段**用 `01_Assessment` 的問卷做 Lead Qualification 與 Discovery。
- **Delivery 階段的 Build** 就是跑完整八階段 + L1-L5 課程。
- **Test / Security Audit / Handover** 對應 Stage Gate 與 `06_Delivery` 的驗收。
- **Support 階段**承接 L4/L5 上線後的持續維運。

---

## 5. 啟動每個專案前的對照 / Pre-Engagement Checklist

任何新顧問案開始前，專案經理應確認：

- [ ] Lead 已通過 Qualification（規模、預算、痛點、決策權）
- [ ] Discovery 已完成，現況與目標清楚
- [ ] SOW 範圍內 / 外已寫明，客戶已簽
- [ ] 7 Pillars 已與客戶對齊（特別是客戶自持、客戶付費、明確範圍）
- [ ] 團隊角色已定（見 [`DELIVERY_ROLE_SOPS.md`](DELIVERY_ROLE_SOPS.md)）
- [ ] 商業文件已備（見 [`BUSINESS_DOCUMENT_TEMPLATES.md`](BUSINESS_DOCUMENT_TEMPLATES.md)）
- [ ] 交付清單已就緒（見 [`DELIVERY_CHECKLISTS.md`](DELIVERY_CHECKLISTS.md)）

---

## 引用 / Citation

本接案生命週期之三階段結構、7 Pillars、角色與文件分類，參考並改寫自 Mirza Iqbal（next8n.com）之 *Workflow Automation Delivery Framework*（MIT License）。本方法論已重新改寫並 generalize 為 AI 轉型顧問情境，未重製、未 fork 原始內容。完整引用見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)。
