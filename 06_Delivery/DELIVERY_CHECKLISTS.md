# 交付營運檢查清單 / Delivery Operations Checklists

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **引用備註 / Attribution:** 本檢查清單之分類（pre-project / security / QA / handover / offboarding），參考並改寫自 **Mirza Iqbal**（next8n.com）之 *Workflow Automation Delivery Framework*（MIT License），已重新以本方法論語言改寫並對應 L1-L5 AI 轉型顧問情境。引用見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)。

---

## 0. 與 Stage Gate 的差異 / vs. Stage Gates

| | Stage Gate（方法論閘）| 本檔檢查清單（營運閘）|
| --- | --- | --- |
| 把關什麼 | L1-L5 課程 / 診斷的「能力是否到位」 | 接案交付的「營運是否做對」|
| 範例 | Gate 3：n8n Workflow 能跑、有 Log | Security checklist：機敏資料有沒有 redact |
| 文件 | `01_Assessment` 的 Evidence Matrix | **本檔** |

兩者並行：Stage Gate 確認「做出來的東西對」，營運清單確認「交付這件事做對」。

---

## 1. Pre-Project Checklist（專案啟動前）

### 1.1 銷售交接

- [ ] SOW 已簽，範圍內 / 外明確
- [ ] 付款里程碑與條件確認
- [ ] Discovery Notes 與問卷結果已交接給 PM
- [ ] 7 Pillars 已與客戶對齊

### 1.2 團隊與資源

- [ ] PM、Technical Lead、Developer 已指派
- [ ] 客戶端 AI Champion / Owner 已指派
- [ ] Kickoff 會議已排，議程與與會者確認

### 1.3 環境與存取

- [ ] 部署模式確認（雲 / Hybrid / 全地端）
- [ ] 客戶系統存取權限到位（OpenWebUI / n8n / API / 資料源）
- [ ] 平台 / API / 模型帳號就緒（客戶自持、客戶付費）
- [ ] 開發 / 測試 sandbox 環境就緒

### 1.4 資料與治理

- [ ] 可訓練 / 測試的範例資料已備（去識別化）
- [ ] 不可碰資料、機敏邊界已定義
- [ ] 人工審核點、輸出責任人已定義

---

## 2. Security Checklist（資安檢核）

> 對應 7 Pillars 第 3 條「資安優先」。每個交付前必過。

### 2.1 帳號與權限

- [ ] 每人獨立帳號，無共用
- [ ] 權限矩陣已設定（最小權限原則）
- [ ] Admin 權限限定特定人員
- [ ] SSO（如有）已啟用

### 2.2 資料邊界

- [ ] 機敏資料 / PII 不進外部 LLM（或已 redact）
- [ ] 模型供應商之資料保留政策已審
- [ ] 高敏感情境採 Hybrid / 全地端，已確認資料不出本地
- [ ] DLP（如客戶有）已涵蓋 AI 流程

### 2.3 稽核與紀錄

- [ ] 所有 LLM 呼叫寫入 Audit Log
- [ ] Audit Log 保存期限符合客戶法遵要求
- [ ] 權限變更有紀錄
- [ ] Credential / API Key 存於密鑰管理，未進 git

### 2.4 上線前

- [ ] 資安檢核報告已產出並經 Technical Lead 簽核
- [ ] 客戶 IT / 資安（如有）已知會並同意

---

## 3. QA / Testing Checklist（測試檢核）

> 對應 7 Pillars 第 4 條「徹底測試」。

### 3.1 功能測試

- [ ] 每個 Skill / Workflow / Agent 用「正常案例」測過
- [ ] 用「異常案例」測過（錯誤輸入、缺資料、邊界值）
- [ ] 串接的系統（Gmail / Sheets / CRM / ERP…）回應正確
- [ ] AI 輸出品質抽樣檢查（分類正確率、摘要忠實度）

### 3.2 錯誤處理

- [ ] Error handling / retry / fallback 已測
- [ ] 失敗會通知、不會靜默
- [ ] DLQ（死信佇列）機制可運作

### 3.3 人工 Gate

- [ ] 高風險動作有人工審核節點
- [ ] AI 只產草稿、不自動送出的部分已確認

### 3.4 證據

- [ ] Execution Log 完整
- [ ] 每個交付物可追溯到來源與判斷依據
- [ ] 測試紀錄已歸檔

---

## 4. Handover Checklist（交接檢核）

> 對應 7 Pillars 第 6 條「乾淨交接」。

### 4.1 交付物

- [ ] 所有 SOW 範圍內交付物已完成並驗收
- [ ] 交付物清單對照 `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` 逐項確認
- [ ] Handover Document 已填寫（見 `BUSINESS_DOCUMENT_TEMPLATES.md`）

### 4.2 系統與帳號

- [ ] 帳號 / 權限移交給客戶 Admin
- [ ] 平台 / API / 模型設定移交（客戶自持）
- [ ] 顧問方臨時存取權限已移除

### 4.3 文件與知識轉移

- [ ] Runbook、維運文件齊全且非原作者可讀
- [ ] 教育訓練 / walkthrough 已完成
- [ ] 客戶端確認可自行維運

### 4.4 收尾

- [ ] 已知限制與後續建議已書面告知
- [ ] 客戶簽署 Handover 確認
- [ ] 最終發票里程碑觸發

---

## 5. Offboarding Checklist（結案 / 退場檢核）

> 對應接案生命週期 Support — Exit 階段。

### 5.1 合約收尾

- [ ] 合約 / Retainer 到期或終止確認
- [ ] 所有發票結清
- [ ] 結案報告（如約定）已交付

### 5.2 資產與權限

- [ ] 顧問方所有存取權限已移除
- [ ] 共用帳號 / 臨時憑證已停用
- [ ] 客戶資料：顧問方端的副本依約定刪除或封存

### 5.3 知識封存

- [ ] 專案文件封存（雙方各留一份）
- [ ] Lessons learned 內部記錄（顧問方）
- [ ] 失敗模式清單更新（如有事故）

### 5.4 關係維護

- [ ] 結案滿意度回饋已蒐集
- [ ] 後續支援 / 續約選項已告知
- [ ] 推薦 / 案例使用授權（如客戶同意）已確認

---

## 引用 / Citation

本檢查清單之 5 大分類，參考並改寫自 Mirza Iqbal（next8n.com）之 *Workflow Automation Delivery Framework*（MIT License），已 generalize 為 L1-L5 AI 轉型顧問情境。完整引用見 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)。
