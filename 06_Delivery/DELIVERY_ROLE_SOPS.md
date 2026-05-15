# 交付角色 SOP / Delivery Role SOPs

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **引用備註 / Attribution:** 本角色 SOP 之 7 角色架構，參考並改寫自 **Mirza Iqbal**（next8n.com）之 *Workflow Automation Delivery Framework*（MIT License），已重新以本方法論語言改寫並對應 AI 轉型顧問情境。引用見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)。

---

## 0. 為什麼要角色 SOP / Why Role SOPs

顧問公司若沒有清楚的角色分工，會出現：一個人做所有事（不可規模化）、交接斷層、責任不清、客戶找不到對的窗口。本檔定義 7 個交付角色，每個角色有：**職責、關鍵交付物、交接點、合作對象、所屬生命週期階段**。

對應接案生命週期見 [`ENGAGEMENT_LIFECYCLE.md`](ENGAGEMENT_LIFECYCLE.md)。小團隊可一人兼多角，但角色「職責」不可省。

---

## 1. Lead Generation（開發）

| 項目 | 內容 |
| --- | --- |
| **生命週期階段** | Sales — Lead Qualification |
| **核心職責** | 找出潛在客戶；用 10 題快速問卷做初步資格判定（規模、預算、痛點、決策權）|
| **關鍵交付物** | 合格 Lead 清單 + 初步問卷結果 |
| **交接點** | 合格 Lead → 交給 Sales Rep；附上問卷結果與初步 L1-L5 落點 |
| **合作對象** | Sales Rep |
| **不可做** | 不對客戶承諾範圍、報價、時程 — 那是 Closer 的事 |

## 2. Sales Rep（業務）

| 項目 | 內容 |
| --- | --- |
| **生命週期階段** | Sales — Discovery |
| **核心職責** | 與合格 Lead 做 Discovery：深入了解現況、系統、目標、痛點；安排 25/50 題問卷 |
| **關鍵交付物** | Discovery Notes + 完整問卷結果 + 初步方案方向 |
| **交接點** | Discovery 完成 → 交給 Closer 出提案；交給 PM 預估資源 |
| **合作對象** | Lead Gen、Closer、PM |
| **不可做** | 不簽約、不做技術承諾 — 技術可行性要先問 Technical Lead |

## 3. Closer（成交）

| 項目 | 內容 |
| --- | --- |
| **生命週期階段** | Sales — Proposal、Contract |
| **核心職責** | 出提案、定範圍、報價、處理反對意見、簽約 |
| **關鍵交付物** | 提案書、SOW、已簽合約 |
| **交接點** | 簽約完成 → 交給 PM 啟動 Delivery；附上 SOW（範圍內/外）與付款條件 |
| **合作對象** | Sales Rep、PM、（必要時）Technical Lead |
| **不可做** | 不在 SOW 外口頭加範圍；任何範圍變動走 Change Order |

## 4. Project Manager（專案經理）

| 項目 | 內容 |
| --- | --- |
| **生命週期階段** | Delivery 全程、Support 銜接 |
| **核心職責** | 啟動會議、排程、資源協調、進度追蹤、Stage Gate 把關、客戶溝通窗口 |
| **關鍵交付物** | Kickoff 紀錄、專案排程、Stage Gate 驗收紀錄、Handover Document |
| **交接點** | 每個 Stage Gate 確認後才進下一階段；Handover 完成 → 交給 Support |
| **合作對象** | Closer、Technical Lead、Developer、Client |
| **不可做** | 不略過 Stage Gate；不在未驗收下宣稱交付完成 |

## 5. Technical Lead / AI 平台負責人（技術主導）

| 項目 | 內容 |
| --- | --- |
| **生命週期階段** | Delivery — Build、Test、Security Audit |
| **核心職責** | 技術方案架構（雲/Hybrid/地端）、L1-L5 平台選型、資安檢核、技術風險判斷、Developer 指導 |
| **關鍵交付物** | 未來藍圖設計、資安檢核報告、L4 Workflow Contract、技術風險清單 |
| **交接點** | 架構確認 → Developer 開始建置；資安檢核通過 → PM 進 Handover |
| **合作對象** | PM、Developer、Client IT |
| **不可做** | 不讓未過資安檢核的東西上線；不繞過 7 Pillars 之「資安優先」 |

## 6. Developer / AI 工程師（建置者）

| 項目 | 內容 |
| --- | --- |
| **生命週期階段** | Delivery — Build、Test |
| **核心職責** | 實際建置 — L1 帳號設定、L2 Skill、L3 n8n Workflow、L4 Hermes Agent、L5 ClawTeam；撰寫測試與文件 |
| **關鍵交付物** | Skill / Workflow / Agent、測試紀錄、Runbook、GitHub backup |
| **交接點** | 建置 + 測試完成 → Technical Lead 審查 → PM 驗收 |
| **合作對象** | Technical Lead、PM |
| **不可做** | 不交付沒測過、沒文件、沒 evidence 的東西；不擅自改 SOW 範圍 |

## 7. Client（客戶端角色）

| 項目 | 內容 |
| --- | --- |
| **生命週期階段** | 全程 |
| **核心職責** | 提供現況資料、系統存取、關鍵人員訪談時間、各 Stage Gate 的簽核、Handover 的接收與驗收 |
| **關鍵交付物** | 簽署的 SOW / Gate 驗收 / Handover 確認；指派內部 AI Champion 與 Owner |
| **交接點** | 客戶 AI Champion 在 Support 階段承接維運 |
| **合作對象** | PM（主要窗口）、Technical Lead |
| **客戶須知** | 依 7 Pillars：系統與資料客戶自持、平台費用客戶付、範圍變動需客戶確認 |

---

## 8. 角色 × 生命週期一覽 / Role × Lifecycle Matrix

| 角色 | Sales | Delivery | Support |
| --- | :---: | :---: | :---: |
| Lead Generation | ● | | |
| Sales Rep | ● | | |
| Closer | ● | | |
| Project Manager | ○ | ● | ○ |
| Technical Lead | ○ | ● | ○ |
| Developer | | ● | ○ |
| Client | ● | ● | ● |

（● 主責　○ 參與）

---

## 9. 交接黃金規則 / Handoff Golden Rules

1. **每次交接都帶文件** — Lead→Sales 帶問卷結果；Sales→Closer 帶 Discovery Notes；Closer→PM 帶 SOW；Delivery→Support 帶 Handover Document。
2. **交接不是丟包** — 交接方要確認接收方理解了再算交接完成。
3. **客戶永遠有單一主要窗口** — Delivery 階段是 PM；不要讓客戶同時被多人聯絡而混亂。
4. **小團隊一人兼多角時，職責清單不可省** — 兼角不等於省略該角色的檢查項。

---

## 引用 / Citation

本角色 SOP 之 7 角色架構參考並改寫自 Mirza Iqbal（next8n.com）之 *Workflow Automation Delivery Framework*（MIT License），已 generalize 為 AI 轉型顧問情境。完整引用見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)。
