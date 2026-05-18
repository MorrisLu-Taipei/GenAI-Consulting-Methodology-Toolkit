# L3 Data Tables Schema 範例 / L3 Data Tables Schema Example

> 對應課程 / Course: [L3_N8N_TIGERAI_COURSE_PLAN.md](../L3_N8N_TIGERAI_COURSE_PLAN.md) §2.4 + §5.2 Builder + §5.3 Advanced
> 版本 / Version: 範本 v1.0（學員 / 講師參考用）/ Template v1.0 (reference for learner / instructor)
> 授權 / License: Apache 2.0

## 0. 為什麼 n8n Workflow 需要 Data Tables / Why Data Tables for n8n

無狀態 workflow（每次 trigger 重新跑）會踩 4 個雷：/ Stateless workflows (re-running each trigger) hit 4 traps:

1. **重複處理同一筆資料 / Duplicate processing** — 比如同一封 Email 被分類 2 次
2. **失敗無重試紀錄 / No retry record** — 失敗一次後無法知道該不該重來
3. **流程跨多步驟無共享狀態 / No cross-step state** — Step A 的結果 Step C 拿不到
4. **無法事後審計 / No post-hoc audit** — 客戶問「上週這 3 筆怎麼處理的」答不出來

Data Tables（n8n 內建 schema-based DB）解決這 4 個問題。/ Data Tables (n8n's built-in schema-based DB) solves all 4.

---

## 1. 標準 schema：5 必備欄 / Standard schema: 5 required fields

```yaml
table_name: workflow_state
fields:
  - id: string (primary key, auto-generated)
  - status: enum [pending, in_progress, approved, sent, failed, retry]
  - timestamp: datetime (created)
  - updated_at: datetime (auto on update)
  - error_log: text (nullable; populated on failure)
```

> **規則 / Rules：** 任何含 Human Gate / Error Handling 的 workflow，**state table 至少要有這 5 欄**。/ Any workflow with Human Gate / Error Handling **must have at least these 5 fields**.

---

## 2. 範例 schema：客戶詢價自動化 / Example: Customer Quote Automation

```yaml
table_name: quote_requests
description: 客戶 email 詢價 → AI 拆 spec → 出報價草稿 → 業務審 → 寄出
description_en: Customer email RFQ → AI extracts spec → drafts quote → sales reviews → sends

fields:
  # 5 必備 / Required
  - id: string (primary key)
  - status: enum [received, parsing, drafted, reviewing, approved, sent, failed]
  - timestamp: datetime (created)
  - updated_at: datetime (auto)
  - error_log: text (nullable)

  # Trigger 來源 / Trigger source
  - source_email_id: string (Gmail message ID)
  - source_email_from: string
  - source_email_subject: string
  - source_email_received_at: datetime

  # AI 處理結果 / AI processing result
  - extracted_specs: json
    # {product: "...", quantity: int, deadline: "...", special_requirements: "..."}
  - extraction_confidence: float (0-1)

  # 報價草稿 / Quote draft
  - draft_quote_amount: decimal
  - draft_quote_pdf_url: string
  - draft_generated_at: datetime

  # Human Gate
  - reviewer_id: string (nullable until reviewed)
  - reviewer_decision: enum [pending, approved, modified, rejected]
  - reviewer_comments: text (nullable)
  - reviewed_at: datetime (nullable)

  # 寄出 / Send
  - final_quote_amount: decimal (nullable; same as draft if approved as-is)
  - sent_to: string (email; nullable until sent)
  - sent_at: datetime (nullable)

  # 重試 / Retry
  - retry_count: int (default 0)
  - last_retry_at: datetime (nullable)
```

---

## 3. 範例 schema：客服 Email 自動分類 / Example: Customer Service Email Classification

```yaml
table_name: customer_service_emails
fields:
  - id: string (PK)
  - status: enum [received, classified, routed, answered_auto, answered_human, escalated]
  - timestamp: datetime
  - updated_at: datetime
  - error_log: text (nullable)

  - source_email_id: string
  - source_email_from: string
  - source_email_text: text

  - ai_category: enum [billing, technical, refund, general, complaint, abuse]
  - ai_priority: enum [P0_urgent, P1_high, P2_normal, P3_low]
  - ai_confidence: float
  - ai_suggested_response: text (nullable)

  - routed_to: string (email / Slack channel)
  - routed_at: datetime
  - escalated: boolean (default false)
  - escalation_reason: text (nullable)

  - resolution_time_hours: float (nullable; computed on close)
  - customer_satisfaction: int (1-5; nullable; from follow-up survey)
```

---

## 4. 設計規則 / Design Rules

### 4.1 命名 / Naming

| 項 / Item | 規則 / Rule |
|---|---|
| table_name | snake_case，複數 / snake_case, plural |
| field_name | snake_case |
| enum values | snake_case, lowercase |
| boolean | prefix with `is_` or `has_` |
| timestamp | suffix with `_at`（如 `created_at`）/ suffix `_at` |

### 4.2 欄位類型對應 / Field-type mapping

| 概念 / Concept | n8n Data Tables type |
|---|---|
| 文字（短）/ Short text | string |
| 文字（長）/ Long text | text |
| 數字（整數）/ Integer | integer |
| 數字（金額）/ Money | decimal |
| 日期時間 / Datetime | datetime |
| 布林 / Boolean | boolean |
| 結構化資料 / Structured | json |
| 列舉 / Enumeration | enum (with allowed values list) |

### 4.3 索引建議 / Index recommendations

- `status` 欄位幾乎必加 index（filter 用）/ `status` field almost always indexed
- `source_*` 欄位（外部 ID）加 unique constraint 防重複 / `source_*` fields (external IDs) add unique constraint
- `timestamp` / `updated_at` 加 index（排序用）/ index for sorting

### 4.4 何時切多張表 / When to split tables

- 單表 > 30 欄 → 考慮拆 / Single table > 30 fields → consider split
- 一對多關係（如 1 quote → N attachments）→ 拆 / One-to-many → split
- 不同生命週期（如 quote 是月為單位 vs log 是天為單位）→ 拆 / Different lifecycles → split

---

## 5. 學員任務 / Learner Task

1. 從 [`POC_SCENARIO_SPECS.md`](../POC_SCENARIO_SPECS.md) 選 1 個 PoC / Pick 1 PoC from POC_SCENARIO_SPECS
2. 用本範例格式設計 schema / Design schema using this template
3. 在 n8n Data Tables 建好 / Create in n8n Data Tables
4. 跑 workflow 寫入 ≥ 5 筆 / Run workflow to write ≥ 5 records
5. 用 `status` filter 驗證資料正確分流 / Verify routing by `status` filter
