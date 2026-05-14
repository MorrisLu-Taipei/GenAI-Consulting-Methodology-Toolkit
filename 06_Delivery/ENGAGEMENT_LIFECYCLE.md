# 顧問接案生命週期 / Consulting Engagement Lifecycle

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>
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
                    │    Stage 6 路徑圖                    │
                    │    Stage 7 解決方案（L1-L5 課程+PoC） │
                    │  Test / Security Audit               │
                    │    Stage 8 治理與 ROI                │
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
