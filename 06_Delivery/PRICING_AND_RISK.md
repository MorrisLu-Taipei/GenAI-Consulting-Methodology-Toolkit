# 定價與風險管理 / Pricing & Risk Management

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>
>
> **引用備註 / Attribution:** 本定價與風險管理之架構，參考並改寫自 **Mirza Iqbal**（next8n.com）之 *Workflow Automation Delivery Framework*（MIT License），已重新以本方法論語言改寫並對應 L1-L5 AI 轉型顧問情境。引用見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)。
>
> ⚠️ 本檔為**定價方法論架構**，非實際報價表。實際金額依市場、規模、客戶個案決定。

---

## A. 定價 / Pricing

### A.1 定價的兩個分離原則 / Two Separation Principles

對應 7 Pillars 第 1、2 條：

1. **顧問費 vs 第三方費用分離** — 顧問費（你的專業）與平台 / API / 模型 / 授權費（客戶自持、客戶付）**分開列**。客戶清楚知道哪些付給你、哪些付給平台。
2. **不墊長期費用** — 第三方訂閱應由客戶自己的帳號付。短期代墊要在發票明列並設上限。

### A.2 四種定價模型 / Four Pricing Models

| 模型 | 適用 | 優點 | 風險 |
| --- | --- | --- | --- |
| **固定價（Fixed）** | 範圍明確的專案（如「一日工作坊」「2 日導入營」）| 客戶好預算、好賣 | 範圍蔓延會吃掉利潤 → 必須有 Change Order |
| **時間與材料（T&M）** | 範圍不確定、探索性 | 不會做白工 | 客戶難預估總額 → 設上限（cap）|
| **價值定價（Value-Based）** | ROI 可量化的案（如「省下 X 工時 / 提升 Y 轉換」）| 利潤最高 | 需要先證明價值、客戶信任門檻高 |
| **維運月費（Retainer）** | Support 階段 | 現金流穩定 | 須明確 SLA 與範圍，否則變無限支援 |

### A.3 階梯式產品線 / Tiered Offerings

對應 `05_Sales` 的方案分級：

| 方案 | 時長 | 定價模型 | 適合 |
| --- | --- | --- | --- |
| 半日體驗 | 4 hr | 固定價 | 決策評估 |
| 一日工作坊 | 8 hr | 固定價 | 5-10 人核心團隊 |
| 二日導入營 | 16 hr | 固定價 | 部門級 + 1 個 PoC |
| 顧問診斷專案 | 6-12 週 | 固定價 / 價值定價 | 全公司 L1-L5 + 八階段報告 |
| 維運 Retainer | 月 | 月費 | Support 階段 |

### A.4 報價時的檢查 / Pricing Checklist

- [ ] 顧問費與第三方費用已分開列
- [ ] 範圍內 / 外已在 SOW 寫明（固定價必備）
- [ ] T&M 有設上限
- [ ] 付款里程碑已定（簽約 / 期中 / 驗收）
- [ ] 第三方費用由客戶帳號付，非顧問長期墊
- [ ] 價值定價案：ROI 假設已與客戶對齊
- [ ] 已預留變更緩衝（Change Order 機制）

---

## B. 風險管理 / Risk Management

### B.1 接案常見風險與緩解 / Common Engagement Risks

| 風險 | 徵狀 | 緩解 |
| --- | --- | --- |
| **範圍蔓延（Scope Creep）** | 客戶不斷「順便加一下」 | SOW 範圍內/外寫死；任何加項走 Change Order |
| **客戶資源不到位** | 訪談排不到、資料給不齊、IT 不配合 | Pre-Project Checklist 先確認；SOW 寫明客戶責任 |
| **資料 / 資安事故** | 機敏資料外流、權限過寬 | Security Checklist 必過；Hybrid / 地端選項；Audit Log |
| **AI 幻覺造成錯誤決策** | AI 輸出被當成事實 | 人工 Gate；evidence 追溯；明示「AI 草稿」|
| **付款延遲 / 呆帳** | 發票過期未付 | 付款里程碑綁交付；期中款未付不進下一階段 |
| **關鍵人員依賴** | 案子綁在某一個顧問身上 | 角色 SOP；文件化；交接黃金規則 |
| **客戶期待落差** | 客戶以為 AI 萬能 | Discovery 階段管理期待；Stage Gate 透明 |
| **技術不可行** | 承諾了做不到的整合 | Sales 階段技術可行性先問 Technical Lead |
| **無 sponsor / champion** | 專案沒人推、6 個月後停擺 | SOW 要求客戶指派 AI Champion 與 Owner |
| **法遵 / 監管變動** | 中途法規改變（金融 / 醫療）| 法遵持續追蹤；高監管產業保守設計 |

### B.2 風險登記表範本 / Risk Register Template

```text
| 風險 | 機率 (高/中/低) | 影響 (高/中/低) | 緩解措施 | 負責人 | 觸發訊號 |
|------|-----------------|------------------|----------|--------|----------|
```

每個專案 Kickoff 時建立，PM 在每個 Stage Gate 檢視更新。

### B.3 何時該說「不」/ When to Decline

顧問公司的健康，來自懂得拒絕。出現以下情況，認真考慮不接 / 不續：

- 客戶不願簽 SOW、不願寫範圍
- 客戶要求顧問長期持有其系統 / 資料（違反 7 Pillars 客戶自持）
- 客戶要求跳過資安檢核或人工 Gate
- 預算與期待嚴重不匹配（要 L4 的成果、給半日的預算）
- 客戶要求顧問為 AI 的自動決策結果負最終責任
- 無 sponsor、無 champion、無預算 owner

### B.4 事故處理 / Incident Response

發生事故（資料、AI 錯誤決策、系統故障）時：

1. **止血** — 先停掉出問題的流程 / Agent
2. **通知** — 依約定時限通知客戶窗口
3. **記錄** — 寫入事故紀錄（時間、影響、根因）
4. **修復** — 修正並重新測試
5. **覆盤** — 更新失敗模式清單（對應 L4 課程「失敗模式驅動學習」）
6. **預防** — 把這個失敗模式變成一條「不可重蹈」規則

---

## 引用 / Citation

本定價與風險管理架構，參考並改寫自 Mirza Iqbal（next8n.com）之 *Workflow Automation Delivery Framework*（MIT License），已 generalize 為 L1-L5 AI 轉型顧問情境。完整引用見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)。
