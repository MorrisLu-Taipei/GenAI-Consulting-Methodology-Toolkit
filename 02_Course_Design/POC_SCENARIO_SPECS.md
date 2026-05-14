# PoC 場景細稿 / PoC Scenario Specifications

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

本檔提供 L3 Workflow AI 與 L4 Hermes Agent 課程之 **可實作 PoC 場景庫**。6 大系統共 30 個 PoC，每個可在 1-3 個工作天完成，具完整輸入輸出、AI step、KPI 與 n8n 節點序列。

This document provides an **implementable PoC scenario library** for the L3 Workflow AI and L4 Hermes Agent courses. 30 PoCs across 6 systems; each completable in 1-3 work days, with full input/output, AI steps, KPIs, and n8n node sequences.

---

## PoC 模板格式 / PoC Template

```
### PoC ID — Title
- Business outcome：1 句話業務結果
- Trigger：觸發來源
- Input：輸入資料 / 事件 / 來源
- AI step：LLM 動作 + prompt 設計重點
- Systems touched：涉及系統
- Output：輸出去向
- Acceptance criteria：3 個驗收條件
- KPI / 量化指標
- Estimated effort：人天
- L-level：L3 / L4
- Sample n8n node sequence：5-10 個節點
```

---

## 1. Gmail PoCs (4)

### G-1 — 客服信件分類與優先級判定 / Customer-Service Email Triage

- Business outcome：客服信件自動分類為「投訴 / 詢問 / 報修 / 其他」並標 P0-P3 優先級
- Trigger：Gmail 收到新信（Webhook / IMAP / Gmail API push）
- Input：寄件人、主旨、內文、附件
- AI step：Claude / GPT-4 prompt — system prompt 含分類定義與企業 SLA；user prompt 為信件全文；輸出 JSON `{category, priority, summary, suggested_action}`
- Systems touched：Gmail、Sheets (Log)
- Output：自動加 Gmail Label + 分派到對應信箱 + Slack 通知 P0
- Acceptance criteria：分類正確率 ≥ 90%、漏接率 ≤ 5%、P0 5 分鐘內通知
- KPI：客服首次回應時間 ↓ 50%、漏接 ↓ 70%
- Effort：1 人天
- L-level：L3
- n8n nodes：Gmail Trigger → Set (extract) → OpenAI Chat → IF (P0) → Gmail Label / Move + Slack + Sheets Append

### G-2 — 業務信件摘要與行動清單 / Sales Email Summary & Action List

- Business outcome：業務每天 7am 收到一封「過去 24h 客戶信摘要 + 必須行動清單」
- Trigger：Schedule (Cron 7am)
- Input：過去 24h Gmail label="customer" 的信
- AI step：彙整 → 每信 2 行摘要 + 標識「客戶問題 / 報價 / 抱怨 / 機會」+ 萃取行動項
- Systems touched：Gmail、Notion (Action DB)
- Output：Email 給該業務 + 寫入 Notion Action DB
- Acceptance：摘要與原信意圖一致 ≥ 95%、行動項可被直接執行
- KPI：業務每日 review 時間 90 min → 20 min
- Effort：1.5 人天
- L-level：L3
- n8n nodes：Schedule → Gmail (search 24h) → Loop Over → OpenAI Chat → Merge → Format Email → Gmail Send + Notion Create

### G-3 — 主管每日重要信件摘要 / Executive Daily Digest

- Business outcome：主管不被 200+ 封信淹沒；每日早上一封 1 頁 digest
- Trigger：Schedule 8am
- Input：主管所有 inbox 過去 24h
- AI step：依重要性過濾 (CC、寄件人 seniority、關鍵字、客戶名單)；產出「Top 5 必讀 + Top 10 可瀏覽 + 一段建議行動」
- Systems touched：Gmail
- Output：HTML email
- Acceptance：主管覺得 Top 5 都對；每週調整 prompt
- KPI：主管 inbox 處理時間 ↓ 60%
- Effort：1 人天
- L-level：L3
- n8n nodes：Schedule → Gmail (search) → Function (rank) → OpenAI → Format HTML → Gmail Send

### G-4 — 自動回覆草稿 (FAQ + 客服) / Auto-Reply Draft

- Business outcome：客服收信後 30 秒內看到「建議回覆草稿」於 Gmail draft
- Trigger：Gmail Webhook
- Input：客戶問題
- AI step：RAG over FAQ Notion DB → 草稿；標 `[AI Draft - 請審核]`
- Systems touched：Gmail、Notion FAQ
- Output：Gmail Draft
- Acceptance：草稿可直接發送率 ≥ 60%；不可發送案例不傷害 trust
- KPI：客服平均處理時間 ↓ 40%
- Effort：2 人天
- L-level：L3 / L4 (升級為 Agent 後可學習修正)
- n8n nodes：Gmail Trigger → Notion Search (RAG) → OpenAI Chat → Gmail Create Draft

---

## 2. Google Sheets PoCs (5)

### S-1 — 問卷結果寫入與自動計分 / Questionnaire Ingestion & Auto-Scoring

- Business outcome：填問卷 → 24 hr 內看到分數 + 客製建議
- Trigger：Google Form Submit
- Input：問卷答案
- AI step：Apps Script / Function 計分 + LLM 寫個人化建議段落
- Systems touched：Form、Sheets、Gmail
- Output：Sheet update + email
- Acceptance：分數正確、email 1 hr 內寄出
- KPI：填表後到顧問接觸時差 7d → 1d
- Effort：1 人天
- L-level：L3
- n8n nodes：Webhook (Form) → Set → Function (score) → OpenAI Chat → Sheets Append → Gmail

### S-2 — KPI 月度自動更新 / Monthly KPI Auto-Refresh

- Business outcome：月初自動拉各部門 KPI、彙整成主管儀表板
- Trigger：Schedule 1st of month 6am
- Input：各部門 Sheet / API
- AI step：彙整 + 異常識別 + 文字解讀
- Systems touched：Sheets、各部門資料源
- Output：主儀表板 + Email digest
- Acceptance：每個 KPI 有來源 + 異常標註
- KPI：月報製作時間 16 hr → 30 min
- Effort：2 人天
- L-level：L3
- n8n nodes：Schedule → HTTP (各源) → Function → Sheets Update → OpenAI → Email

### S-3 — Workflow 執行紀錄與失敗監控 / Workflow Execution Log & Failure Monitoring

- Business outcome：n8n 全部 Workflow 的執行記錄寫入 Sheet；失敗即時 Slack 告警
- Trigger：n8n 全域 Workflow End
- Input：execution metadata
- AI step：失敗時 LLM 摘要 root cause（讀 stack + 上次成功對比）
- Systems touched：n8n、Sheets、Slack
- Output：Sheet log + Slack alert
- Acceptance：所有 workflow 都被記錄；失敗 30 秒內告警
- KPI：MTTR (mean time to recover) ↓ 70%
- Effort：1 人天
- L-level：L3
- n8n nodes：Error Trigger → Set → OpenAI Chat → Slack + Sheets

### S-4 — 客戶名單去重與分類 / Customer List Dedup & Classification

- Business outcome：3 個來源客戶名單合併、去重、分類
- Trigger：Manual or Webhook
- Input：3 個 Sheet/CSV
- AI step：LLM 處理 fuzzy 匹配（名稱差異、英中對照）+ 分類
- Systems touched：Sheets
- Output：合併後 Sheet
- Acceptance：去重正確率 ≥ 98%
- KPI：人工去重 8 hr → 30 min
- Effort：1.5 人天
- L-level：L3
- n8n nodes：Manual Trigger → Sheets (3 sources) → Merge → Function (initial dedup) → OpenAI (fuzzy) → Sheets Output

### S-5 — 預算與支出差異分析 / Budget vs Spend Variance

- Business outcome：每月底自動產出「實際 vs 預算」差異 + AI 解讀
- Trigger：Schedule 月底
- Input：預算 Sheet + ERP 支出
- AI step：差異 > 10% 自動列出原因（依歷史資料）
- Systems touched：Sheets、SAP/Oracle ERP
- Output：報告 + Email
- Acceptance：差異列表完整、AI 解讀合理
- KPI：CFO review 時間 ↓ 50%
- Effort：2 人天
- L-level：L3
- n8n nodes：Schedule → SAP API + Sheets → Merge → Function (compare) → OpenAI → Format → Email

---

## 3. Notion PoCs (5)

### N-1 — 會議錄音轉摘要與行動項 / Meeting Transcript → Summary + Action Items

- Business outcome：會議錄音 → 5 分鐘內 Notion 有摘要 + actions
- Trigger：Notion Page Webhook (上傳 audio file)
- Input：m4a / mp3
- AI step：Whisper 轉文字 → Claude/GPT 摘要 + 提取 action item (含 owner, due)
- Systems touched：Notion、Whisper API
- Output：Notion 子頁 (Meeting Notes + Actions DB rows)
- Acceptance：action item 含 owner 比例 ≥ 80%
- KPI：會議後 follow-up 時間 90 min → 5 min
- Effort：2 人天
- L-level：L3 / L4
- n8n nodes：Notion Trigger → HTTP (Whisper) → OpenAI Chat → Function (parse actions) → Notion Update + Notion Create (Actions DB)

### N-2 — 顧問診斷資料庫設計 / Consulting Diagnostic Database

- Business outcome：每位客戶有完整 Notion workspace：profile、interview notes、scoring、roadmap、actions
- Trigger：n8n Webhook (新客戶)
- Input：客戶基本資料
- AI step：依範本產生客製化結構 + 預填初步 hypothesis
- Systems touched：Notion
- Output：Notion 結構化頁面
- Acceptance：所有必要區塊到位、relation 設定正確
- KPI：新客戶 onboarding 4 hr → 15 min
- Effort：1.5 人天
- L-level：L3
- n8n nodes：Webhook → OpenAI Chat (生成 outline) → Loop → Notion Create (per page) → Notion Update (relations)

### N-3 — Skill Library 範本與版本控制 / Skill Library Template & Versioning

- Business outcome：每個 Skill 在 Notion 有 IPOE、Owner、版本、test cases
- Trigger：Manual (新 Skill 建立)
- Input：Skill 名稱 + 簡述
- AI step：依 Skill 簡述產出 IPOE 草稿、test case 範例
- Systems touched：Notion、GitHub (備份)
- Output：Notion page + GitHub markdown
- Acceptance：每個 Skill 有 IPOE + ≥ 3 test cases + Owner
- KPI：Skill 上架時間 60 min → 10 min
- Effort：1.5 人天
- L-level：L3 / L4
- n8n nodes：Webhook → OpenAI Chat → Notion Create → GitHub Create File

### N-4 — 任務自動分派 / Auto Task Assignment

- Business outcome：從 Sheets / Webhook 進來的任務自動建立 Notion task + 指派 owner + 通知
- Trigger：Sheets Append 或 Webhook
- Input：task description, deadline, dept
- AI step：LLM 依描述判斷最佳 owner（從 dept skill matrix）+ 拆解子任務
- Systems touched：Sheets / Notion / Slack
- Output：Notion task DB rows + Slack DM
- Acceptance：分派正確率 ≥ 90%
- KPI：任務指派時間 ↓ 70%
- Effort：2 人天
- L-level：L3
- n8n nodes：Trigger → Notion Search (skill matrix) → OpenAI → Notion Create + Slack DM

### N-5 — 內部 RAG 問答 / Internal Q&A over Notion

- Business outcome：員工在 Slack 問問題，Bot 從 Notion 全公司知識庫回答
- Trigger：Slack message (DM 或 mention)
- Input：自然語言問題
- AI step：Embedding 比對 → 取 Top-5 chunks → Claude / GPT 回答 + 來源連結
- Systems touched：Slack、Notion、Vector DB (Pinecone / Qdrant / Chroma)
- Output：Slack reply with sources
- Acceptance：答案有來源連結 100%、答對率 ≥ 85%
- KPI：HR / IT 重複問答 ↓ 60%
- Effort：3 人天 (含 embedding pipeline)
- L-level：L4 (近 Agent 邊界)
- n8n nodes：Slack Trigger → HTTP (embedding query) → HTTP (vector search) → OpenAI Chat → Slack Reply

---

## 4. CRM PoCs (5) — 以 HubSpot / Salesforce 為例

### C-1 — 對話查詢客戶資料 / Conversational Customer Lookup

- Business outcome：業務在 Slack/Teams 問「客戶 X 上次互動是什麼」立即得答
- Trigger：Slack mention bot
- Input：客戶名稱（fuzzy）
- AI step：Fuzzy match → CRM API → 摘要回覆
- Systems touched：Slack、CRM
- Output：Slack reply
- Acceptance：fuzzy match 正確 ≥ 95%、回覆 < 10 秒
- KPI：業務查資料時間 ↓ 90%
- Effort：1.5 人天
- L-level：L3
- n8n nodes：Slack Trigger → CRM Search → OpenAI (summary) → Slack Reply

### C-2 — 商機摘要與下一步建議 / Opportunity Summary & Next-Step

- Business outcome：每週日晚自動產出 Top 20 商機 brief + 推薦下一步
- Trigger：Schedule Sun 8pm
- Input：CRM Pipeline > NT$ 100K 案件
- AI step：摘要 stage、過往互動、產業 context、推薦下一步
- Systems touched：CRM、Email、Notion
- Output：每位 AE 收 email + Notion 子頁
- Acceptance：建議下一步可被執行率 ≥ 70%
- KPI：每週 1-on-1 review 時間 ↓ 50%
- Effort：2 人天
- L-level：L3 / L4
- n8n nodes：Schedule → CRM API → Loop → OpenAI Chat → Format → Email + Notion

### C-3 — 拜訪後互動紀錄自動更新 / Post-Visit Note Auto-Update

- Business outcome：業務口述拜訪重點 (Slack voice / 文字) → 自動寫入 CRM
- Trigger：Slack DM to bot
- Input：voice / text
- AI step：Whisper + 結構化萃取 (誰、何時、聊什麼、下一步) → CRM update
- Systems touched：Slack、CRM、Whisper
- Output：CRM activity record
- Acceptance：欄位填寫率 ≥ 90%
- KPI：CRM 更新率 ↑ 60%
- Effort：2 人天
- L-level：L3 / L4
- n8n nodes：Slack Trigger → Whisper → OpenAI (extract) → CRM Update

### C-4 — 客訴案件追蹤與升級警示 / Complaint Tracking & Escalation

- Business outcome：客訴未在 SLA 內回應自動 escalate
- Trigger：Schedule 每 30 min + CRM Webhook
- Input：客訴 case
- AI step：判斷案件 sentiment、預估時間敏感度、escalate to who
- Systems touched：CRM、Slack
- Output：Slack alert + CRM 標記
- Acceptance：SLA 違規率 ↓ 80%
- KPI：客訴升級時間 ↓ 70%
- Effort：1.5 人天
- L-level：L3
- n8n nodes：CRM Webhook + Schedule → Function (SLA check) → OpenAI (sentiment) → Slack + CRM Update

### C-5 — 客戶健康分數計算 / Customer Health Score

- Business outcome：每週為每個客戶算 churn risk score，Top 10 risk 通知 CSM
- Trigger：Schedule 週一 9am
- Input：CRM 互動 + Product usage + 帳單
- AI step：Function 算分 + LLM 寫 narrative why-it-changed
- Systems touched：CRM、Product DB、Billing
- Output：CRM score field + Slack alert
- Acceptance：分數可解釋、Top 10 觸發實際介入
- KPI：年 churn 率 ↓ 15%
- Effort：3 人天
- L-level：L4
- n8n nodes：Schedule → CRM + DB + Billing → Merge → Function → OpenAI → CRM Update + Slack

---

## 5. API PoCs (5)

### A-1 — 內部 API webhook 訂閱 / Internal Webhook Subscriber

- Business outcome：訂閱內部事件 (新客戶、訂單、異常) 後自動處理
- Trigger：Webhook
- Input：JSON event payload
- AI step：分類事件、決策路由
- Systems touched：n8n、各內部 service
- Output：分流到對應 workflow
- Acceptance：所有事件都有 audit log
- KPI：內部事件處理延遲 ↓ 80%
- Effort：1 人天
- L-level：L3
- n8n nodes：Webhook → Switch → 分流到子 workflow

### A-2 — 外部 API 整合 / External API Integration

- Business outcome：業務需要查天氣 / 物流 / 地圖 / 公司資料時統一介面
- Trigger：Slack mention 或 chatbot
- Input：自然語言
- AI step：判斷需要哪個 API、組合回答
- Systems touched：多家外部 API
- Output：Slack reply
- Acceptance：API 切換正確、回答整合
- KPI：員工自助查詢率 ↑
- Effort：2 人天
- L-level：L3 / L4
- n8n nodes：Slack Trigger → OpenAI (intent) → Switch → HTTP (對應 API) → OpenAI (format) → Slack

### A-3 — 錯誤重試與 Idempotency

- Business outcome：API 不穩定不會 corrupt 資料
- Trigger：n8n Workflow 內部
- Input：API call
- AI step：N/A (純邏輯)
- Systems touched：External API、Data Table (idempotency key)
- Output：成功 or 死信佇列
- Acceptance：idempotency key 重複呼叫不重複處理
- KPI：重複資料 ↓ 100%
- Effort：1 人天
- L-level：L3
- n8n nodes：Function (gen key) → Data Table Lookup (skip if exists) → HTTP with retry → On Error → Data Table (DLQ)

### A-4 — Rate-Limit 處理與排程 / Rate-Limit & Scheduling

- Business outcome：避免被 API 廠商封鎖
- Trigger：Schedule + Queue
- Input：待處理 batch
- AI step：N/A
- Systems touched：External API
- Output：批次完成
- Acceptance：每秒 ≤ rate limit；overflow 進 queue
- KPI：API 失敗率 ↓
- Effort：1.5 人天
- L-level：L3
- n8n nodes：Trigger → Loop with Wait → HTTP → If 429 → Wait + Retry

### A-5 — 多 API 結果整合 / Multi-API Aggregation

- Business outcome：一個查詢調用 3+ API 後彙整
- Trigger：Webhook / Slack
- Input：query
- AI step：分散查詢 → 結果整合 → 回答
- Systems touched：3+ API
- Output：合併結果
- Acceptance：整合無遺漏
- KPI：查詢完成時間 ↓ 60%
- Effort：2 人天
- L-level：L3
- n8n nodes：Trigger → Split In Batches → HTTP (parallel) → Merge → OpenAI (synthesize) → Reply

---

## 6. ERP PoCs (6) — 以 SAP B1 / Oracle / 通用 ERP 為例

### E-1 — 訂單狀態查詢 / Order Status Lookup

- Business outcome：業務 / 客服在 Slack 問訂單即時得答
- Trigger：Slack mention
- Input：訂單號 or 客戶名
- AI step：Fuzzy lookup → format
- Systems touched：Slack、ERP
- Output：Slack reply
- Acceptance：< 5 秒回應
- KPI：客服查單時間 ↓ 90%
- Effort：1.5 人天
- L-level：L3
- n8n nodes：Slack Trigger → ERP API → OpenAI (format) → Slack Reply

### E-2 — 庫存異常告警 / Inventory Anomaly Alert

- Business outcome：庫存低於安全水位 / 過期 / 滯銷自動告警
- Trigger：Schedule 每 6 hr
- Input：庫存報表
- AI step：規則檢查 + LLM 解讀「為什麼異常 + 建議」
- Systems touched：ERP、Slack
- Output：Slack 告警
- Acceptance：告警準確率 ≥ 95%
- KPI：缺料 / 滯銷成本 ↓ 20%
- Effort：2 人天
- L-level：L3
- n8n nodes：Schedule → ERP API → Function (rule) → OpenAI → Slack

### E-3 — 出貨延遲分析 / Shipping Delay Analysis

- Business outcome：每日出貨延遲案件根因分析
- Trigger：Schedule 6pm
- Input：當日 SO + 出貨記錄
- AI step：判斷延遲原因 (備料 / 物流 / 客戶 / 系統)
- Systems touched：ERP、WMS、物流系統
- Output：Email digest 給營運主管
- Acceptance：分類正確 ≥ 85%
- KPI：延遲案件根因識別時間 ↓ 70%
- Effort：2.5 人天
- L-level：L3 / L4
- n8n nodes：Schedule → ERP + WMS + 物流 → Merge → OpenAI → Email

### E-4 — 採購對帳差異分析 / Purchase Reconciliation Diff

- Business outcome：發票與採購單差異 > 5% 自動標記
- Trigger：Schedule 月底 + Webhook
- Input：發票 OCR + PO
- AI step：對帳邏輯 + 差異原因建議
- Systems touched：ERP、OCR
- Output：Sheet + Slack
- Acceptance：差異識別準確率 ≥ 95%
- KPI：對帳人天 ↓ 60%
- Effort：3 人天
- L-level：L3 / L4
- n8n nodes：Schedule → ERP API → OCR → Merge → Function → OpenAI → Sheets

### E-5 — 財務月結異常項摘要 / Month-End Exception Summary

- Business outcome：CFO 月結後 24 hr 內收到異常項摘要
- Trigger：Schedule 月底+1 day
- Input：總帳異動
- AI step：找異常 (跨月、新科目、大金額)、彙整摘要
- Systems touched：ERP、Email
- Output：CFO email + Notion archive
- Acceptance：CFO 認為摘要有用率 ≥ 80%
- KPI：CFO 月結 review 時間 ↓ 50%
- Effort：3 人天
- L-level：L4
- n8n nodes：Schedule → ERP GL Query → Function → OpenAI → Email + Notion

### E-6 — 跨部門 KPI 每日推送 / Daily Cross-Functional KPI Digest

- Business outcome：每天 8am 主管收到跨部門 KPI 一頁式
- Trigger：Schedule 8am
- Input：ERP + CRM + Sheets KPI
- AI step：依角色客製、突顯異動
- Systems touched：ERP、CRM、Sheets、Email
- Output：Email per role
- Acceptance：每位主管覺得有 1 件值得行動的事
- KPI：主管 KPI review 時間 30 min → 5 min
- Effort：2 人天
- L-level：L4
- n8n nodes：Schedule → 多源 → Merge → OpenAI per role → Email

---

## 7. 會計 / 記帳 PoCs (5) — Accounting & Bookkeeping PoCs

> 本節基於**公開的會計內控原則**（憑證原則、借貸平衡、權責發生制、配對原則、職責分離、對帳）獨立撰寫，適合中小企業財會場景。
> 核心紀律：**證據不足不記帳、不臆斷；任何過帳動作一律經人工 Gate**。AI 只做「整理、分類、草稿、標記」，不自動過帳。
>
> This section is independently authored from **public accounting internal-control principles** (the voucher principle, double-entry, accrual basis, the matching principle, segregation of duties, reconciliation), suited to SME finance scenarios.
> Core discipline: **do not record on insufficient evidence and do not make assumptions; every posting action passes a human Gate.** The AI only organizes, classifies, drafts, and flags — it never auto-posts.

### F-1 — 銀行交易自動分類與科目對應 / Bank Transaction Auto-Classification & Account Mapping

- Business outcome：銀行對帳單交易自動分類並對應到會計科目草稿，人工確認後才入帳
- Trigger：銀行對帳單上傳（CSV / API）
- Input：交易日期、金額、對手方、摘要、帳戶
- AI step：依交易特徵分類（收入 / 費用 / 轉帳 / 借還款 …）+ 建議會計科目；**信心不足者標記「待釐清」不給科目**；對手方若為第三方支付別名（街口、LINE Pay）須標記「需穿透實際商戶」
- Systems touched：銀行 API / Sheets、會計系統（僅讀）
- Output：分類後交易表 + 科目建議 + 「待釐清」清單
- Acceptance criteria：分類正確率 ≥ 90%；「待釐清」項目零誤入帳；別名對手方 100% 被標記
- KPI / 量化指標：記帳前置整理時間 ↓ 60%
- Estimated effort：2 人天
- L-level：L3
- Sample n8n node sequence：Webhook/Manual → Set (parse) → OpenAI Chat (classify) → IF (信心不足) → Sheets (待釐清 / 已分類兩表)

### F-2 — 發票與付款配對 / Invoice–Payment Matching

- Business outcome：應收/應付發票與銀行付款自動配對，**不只比金額**
- Trigger：Schedule（每日）或發票 / 付款進件 Webhook
- Input：發票（號碼、日期、對手方、金額、品項）、付款（日期、金額、對手方、摘要）
- AI step：多欄位比對 — 金額 + 期間 + 對手方身分 + 業務類型 + 單據鏈；**金額相符但其他欄位不符者不配對，列入例外**
- Systems touched：會計系統、Sheets / Data Tables
- Output：已配對清單、部分配對（待人工確認）、未配對例外
- Acceptance criteria：配對正確率 ≥ 95%；無「僅金額相符」之錯誤配對
- KPI：對帳人工工時 ↓ 50%
- Estimated effort：2.5 人天
- L-level：L3
- Sample n8n node sequence：Schedule → 發票源 + 付款源 → Merge → Function (multi-field match) → Switch (配對/部分/例外) → Sheets

### F-3 — 傳票草稿生成與覆核佇列 / Voucher Draft Generation & Review Queue

- Business outcome：從已分類交易產生借貸傳票**草稿**，進覆核佇列等人工核准
- Trigger：F-1 / F-2 完成後
- Input：已分類交易、科目對應、配對結果
- AI step：產生借貸分錄草稿（檢查借貸平衡）+ 附上判斷依據與來源憑證連結；標記「草稿 — 待覆核」
- Systems touched：會計系統（僅寫入「草稿」狀態）、Sheets
- Output：傳票草稿 + 覆核佇列 + 每筆的證據連結
- Acceptance criteria：借貸 100% 平衡；每筆草稿可追溯到原始憑證；**無任何草稿被自動過帳**
- KPI：傳票製作時間 ↓ 55%
- Estimated effort：3 人天
- L-level：L3 / L4
- Sample n8n node sequence：Trigger → Function (借貸分錄 + 平衡檢查) → 會計系統 (draft only) → Sheets (覆核佇列) → Slack (通知會計覆核)

### F-4 — 月結異常與跨期調整偵測 / Month-End Exception & Cross-Period Adjustment Detection

- Business outcome：月結前自動掃出異常分錄與應計 / 預付 / 跨期項目
- Trigger：Schedule（月底前 3 天）
- Input：當月總帳異動、前期比較、待攤 / 預收 / 應計清單
- AI step：找異常（新科目、異常大額、跨月、重複）+ 依權責發生制標記應做的跨期調整；產出「會計師覆核清單」
- Systems touched：會計系統（僅讀）、Email / Notion
- Output：月結異常清單 + 跨期調整建議清單（皆待人工確認）
- Acceptance criteria：異常偵測召回率 ≥ 90%；跨期建議皆附依據；**不自動產生調整分錄**
- KPI：月結覆核時間 ↓ 40%
- Estimated effort：3 人天
- L-level：L4
- Sample n8n node sequence：Schedule → 會計系統 Query → Function (異常規則 + 跨期判斷) → OpenAI (解讀) → Notion (覆核清單) → Email (會計主管)

### F-5 — 對帳差異分析與根因標記 / Reconciliation Difference Analysis & Root-Cause Flagging

- Business outcome：銀行 / 廠商 / 內部帳對帳差異自動分析並標記根因類型
- Trigger：Schedule 或對帳啟動 Webhook
- Input：兩方帳務資料（銀行 vs 帳冊 / 廠商對帳單 vs 應付）
- AI step：找出差異項，分類根因（時間差 / 漏記 / 重複 / 金額誤植 / 手續費 / 待釐清）；無法判斷者一律標「待釐清」
- Systems touched：會計系統、銀行 / 廠商資料、Sheets
- Output：對帳差異表 + 根因分類 + 待釐清清單
- Acceptance criteria：根因分類正確率 ≥ 85%；待釐清項目不被臆測歸類
- KPI：對帳差異處理時間 ↓ 50%
- Estimated effort：2.5 人天
- L-level：L3
- Sample n8n node sequence：Trigger → 兩方資料源 → Merge → Function (diff) → OpenAI (根因分類) → Sheets (差異表 + 待釐清)

> **會計 PoC 共通治理紅線：**
> 1. AI 永遠只產「草稿 / 建議 / 標記」，**過帳、調整、結帳一律人工 Gate**。
> 2. 證據不足 → 進「待釐清」，不臆測、不自動入帳。
> 3. 對手方別名（第三方支付）必須穿透到實際商戶才可入帳。
> 4. 配對不可只靠金額，須多欄位驗證。
> 5. 機敏財務資料情境建議 Hybrid / 全地端部署，LLM 節點前置 redaction。
> 6. 全程證據軌：每筆草稿 / 建議都可追溯到原始憑證與判斷依據。

---

## Selection Guide / PoC 選擇指南

### 依客戶 L-level 推薦 PoC

| 客戶起點 | 建議優先 PoC | 為什麼 |
| --- | --- | --- |
| L1 → L2 | G-1, G-4, S-1 | 員工每天感受到、低風險、立即見效 |
| L2 → L3 | S-2, S-3, N-1, C-1, A-1 | 開始系統整合、看 ROI |
| L3 → L4 | C-2, C-5, N-5, E-5, E-6 | 複雜度高、需 Wiki 與 Reviewer |
| L4 → L5 | 跨 PoC 組合 (e.g., E-3 + C-4 + N-1 → ClawTeam) | 多 Agent 串接 |

### 依產業推薦

| 產業 | Top 3 PoC |
| --- | --- |
| Manufacturing | E-2, E-3, S-2 |
| Hospital | N-5, G-1, C-4 (病患服務 case) |
| Retail | C-2, C-5, S-2 |
| B2B SaaS | C-2, C-5, A-2 |
| Pro Services | N-1, N-3, N-5 |

### 依資料敏感度

| 敏感度 | 建議部署 | PoC 改寫 |
| --- | --- | --- |
| 低 | 雲端 OpenAI / Claude | 全部 PoC |
| 中 | Hybrid (LLM redact 後再送) | 加 redaction step |
| 高 | 全地端 Llama 70B | 改 OpenAI Chat → Local LLM HTTP |

---

## 共通要求 / Cross-Cutting Requirements

每個 PoC 不論細節，都必須：

- 有 audit log (寫入 `aid_audit` Data Table)
- 有 error handling (Error Trigger → DLQ)
- 有 idempotency key (避免重複)
- 有 GitHub backup workflow (定期匯出)
- 有 Reviewer / Human Gate (重大決策)
- 上線前通過 Stage Gate 3 (L3) 或 4 (L4)

完整 schema：見 `01_Assessment/AI_DIAGNOSIS_SHEETS_SCHEMA.md`、`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`。
