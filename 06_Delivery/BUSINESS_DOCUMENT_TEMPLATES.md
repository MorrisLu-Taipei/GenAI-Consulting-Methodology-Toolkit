# 商業文件範本 / Business Document Templates

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **引用備註 / Attribution:** 本商業文件範本清單與結構，參考並改寫自 **Mirza Iqbal**（next8n.com）之 *Workflow Automation Delivery Framework*（MIT License），已重新以本方法論語言改寫並對應 AI 轉型顧問情境。引用見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)。
>
> ⚠️ **法律免責**：本檔為**範本骨架**，非法律文件。實際合約、SOW 在使用前務必經貴公司法務 / 律師審閱。

---

## 0. 文件清單 / Document Index

| 文件 | 何時用 | 生命週期階段 |
| --- | --- | --- |
| 提案書 / Proposal | Lead 通過 Discovery 後 | Sales |
| 工作範圍書 / SOW | 提案被接受、準備簽約 | Sales |
| 主服務合約 / MSA 大綱 | 長期合作的母約 | Sales |
| 變更單 / Change Order | SOW 範圍要調整時 | Delivery / Support |
| 發票 / Invoice | 依付款里程碑 | 全程 |
| 交接文件 / Handover Document | Delivery 結束 | Delivery |
| 維運合約 / Retainer Agreement | 進入 Support | Support |
| 關鍵 email 範本 | 各階段溝通 | 全程 |

---

## 1. 提案書 / Proposal Template

```text
【提案書】[客戶名] AI 轉型顧問方案

1. 背景與痛點
   - 從 Discovery 整理出的 2-4 個關鍵痛點

2. 建議方案
   - AI 成熟度落點：L[X]
   - 建議三段式路徑：診斷 → L1-L5 課程 → 顧問報告
   - 課程比例建議：L1 __% / L2 __% / L3 __% / L4 __% / L5 __%

3. 範圍 / Scope
   - 範圍內：[列出]
   - 範圍外：[列出 — 很重要，避免日後爭議]

4. 時程
   - 診斷 [X] 週 / 建置 [X] 週 / 交付 [X] 週

5. 交付物
   - [對照 DELIVERY_PACKAGE_AND_ACCEPTANCE.md]

6. 投資 / Pricing
   - 顧問費：NT$ ______
   - 平台 / API / 模型費用（客戶承擔，透明列出）：NT$ ______
   - 付款里程碑：簽約 __% / 期中 __% / 驗收 __%

7. 團隊與角色
   - PM、Technical Lead、Developer（見 DELIVERY_ROLE_SOPS.md）

8. 下一步
   - 確認提案 → 簽 SOW → Kickoff
```

---

## 2. 工作範圍書 / Scope of Work (SOW) Template

```text
【工作範圍書 SOW】

專案名稱：______
客戶：______          顧問方：Tiger AI 虎智科技
SOW 編號：______      日期：______

1. 專案目標
   [可量化的目標，對應 Discovery 的問題定義]

2. 範圍內 / In Scope
   - [明確列出每一項交付]

3. 範圍外 / Out of Scope
   - [明確列出不包含的，避免 scope creep]

4. 交付物與驗收標準
   | 交付物 | 驗收標準 | Stage Gate |
   |--------|----------|-----------|

5. 時程與里程碑
   | 里程碑 | 日期 | 付款 % |
   |--------|------|--------|

6. 雙方責任
   - 顧問方：[列出]
   - 客戶方：提供資料/系統存取/關鍵人員時間/各 Gate 簽核（見 7 Pillars）

7. 假設與前提
   - [例：客戶已有 OpenWebUI 環境 / 客戶 IT 可配合 2 FTE]

8. 變更管理
   - 任何範圍變動須經雙方書面 Change Order，不口頭加項

9. 費用與付款
   - 顧問費、第三方費用（客戶承擔）、付款條件

10. 智財權
    - 課中產出（Prompt/Skill/Workflow/Agent）歸客戶
    - 方法論本身為 Tiger AI 之 Apache 2.0 開源資產

11. 簽署
    客戶：____________  顧問方：____________  日期：______
```

---

## 3. 主服務合約 / MSA 大綱

長期 / 多專案合作時，先簽一份 MSA（母約），之後每個專案只簽 SOW。MSA 應涵蓋：

- 雙方主體、聯絡資訊
- 服務範疇總述（細節在各 SOW）
- 保密條款（NDA）
- 智財權歸屬原則
- 資料保護與資安責任（對應 7 Pillars 資安優先）
- 責任限制與免責
- 付款與發票通則
- 終止條款與 Offboarding 約定
- 準據法與爭議解決
- MSA 與 SOW 衝突時以何者為準

---

## 4. 變更單 / Change Order Template

```text
【變更單 Change Order】

關聯 SOW：______      變更單編號：______      日期：______

1. 變更內容
   [描述要新增 / 修改 / 移除什麼]

2. 變更原因
   [客戶新需求 / 假設不成立 / 範圍澄清]

3. 對範圍的影響
   - 原範圍：______
   - 變更後範圍：______

4. 對時程的影響
   - 增加 / 減少 [X] 週

5. 對費用的影響
   - 增加 / 減少 NT$ ______

6. 簽署
   客戶：____________  顧問方：____________  日期：______
```

---

## 5. 發票 / Invoice Template

```text
【發票 Invoice】

發票編號：______      日期：______      到期日：______
開立方：Tiger AI 虎智科技
收受方：[客戶]

關聯 SOW / 里程碑：______

| 項目 | 說明 | 金額 |
|------|------|------|
| 顧問費（里程碑 __）| | NT$ ______ |
| 第三方費用代墊（如有）| | NT$ ______ |
| 小計 | | NT$ ______ |
| 稅 | | NT$ ______ |
| 總計 | | NT$ ______ |

付款方式：______
備註：逾期付款條款 ______
```

---

## 6. 交接文件 / Handover Document Template

```text
【交接文件 Handover Document】

專案：______      交接日期：______
交付方：Tiger AI      接收方：[客戶 AI Champion / Owner]

1. 交付物清單與位置
   | 交付物 | 位置 / 連結 | 說明 |

2. 系統與帳號
   - 帳號清單、權限矩陣、誰是 Admin
   - 平台 / API / 模型設定（客戶自持）

3. Runbook 與維運
   - 排程、監控、錯誤處理、fallback、事故聯絡

4. 知識轉移紀錄
   - 已完成的教育訓練 / walkthrough
   - 客戶端可自行維運的確認

5. 已知限制與後續建議
   - [列出]
   - 後續可考慮的 L4/L5 擴展

6. 驗收
   - 對照 DELIVERY_PACKAGE_AND_ACCEPTANCE.md 逐項確認
   客戶簽收：____________  日期：______
```

---

## 7. 維運合約 / Retainer Agreement 大綱

進入 Support 階段時：

- 服務範圍：監控 / 維護 / 小幅優化 / 諮詢時數
- SLA：回應時間、處理時間、服務時段
- 計費方式：月費 / 時數包 / 混合
- 超出範圍的處理：走 Change Order 或另計
- 聯絡窗口與升級路徑
- 合約期間與續約 / 終止

---

## 8. 關鍵 Email 範本 / Key Email Templates

| 時機 | 重點 |
| --- | --- |
| Discovery 邀約 | 說明會談目的、時長、需客戶準備什麼 |
| 提案寄送 | 摘要 3 個重點 + 明確下一步（不要只丟附件）|
| Kickoff 通知 | 時間、與會者、議程、客戶需先準備的事 |
| Stage Gate 驗收請求 | 列出本階段交付物 + 請客戶確認的具體項目 |
| 變更單通知 | 說明為何需要變更 + 對範圍/時程/費用的影響 |
| Handover 通知 | 交付物清單 + 知識轉移安排 + 驗收方式 |
| Offboarding 通知 | 資產移交、帳號清理時程、後續支援選項 |

---

## 引用 / Citation

本商業文件範本清單與結構，參考並改寫自 Mirza Iqbal（next8n.com）之 *Workflow Automation Delivery Framework*（MIT License），已 generalize 為 AI 轉型顧問情境。完整引用見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)。
