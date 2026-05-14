# n8n Workflow 範本與匯入指南 / n8n Workflow Templates & Import Guide

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>

本檔把 [`POC_SCENARIO_SPECS.md`](POC_SCENARIO_SPECS.md) 中的 PoC 整理成可匯入 n8n 的 workflow 範本骨架（JSON skeleton），以及在課堂上分享、版本控制、備份的標準流程。

Turns the PoCs from [`POC_SCENARIO_SPECS.md`](POC_SCENARIO_SPECS.md) into importable n8n workflow skeletons (JSON) plus the standard process for sharing, version-controlling, and backing them up in class.

---

## 1. 為什麼要範本化 / Why Templatize

| 沒有範本 | 有範本 |
| --- | --- |
| 每位學員從零拉節點 | 匯入骨架，專注在 prompt 與 mapping |
| Workflow 散落各人帳號 | 集中在 Sub-workflow Library |
| 無版本控制 | GitHub backup + 版本號 |
| 課後無法複製 | 企業可重複部署 |

---

## 2. n8n 範本匯出 / 匯入流程 / Export & Import

### 2.1 匯出 / Export

```
n8n UI → 開啟 workflow → 右上 ⋯ 選單 → Download
→ 得到 {workflow-name}.json
```

或用 n8n CLI（self-host）：

```bash
n8n export:workflow --id=<workflow-id> --output=./templates/
n8n export:workflow --all --output=./templates/    # 全部匯出
```

### 2.2 匯入 / Import

```
n8n UI → Workflows → Import from File → 選 .json
```

或 CLI：

```bash
n8n import:workflow --input=./templates/G-1-email-triage.json
```

### 2.3 匯入後必做 / Post-import checklist

- [ ] 重新綁定 Credentials（匯出的 JSON **不含** 金鑰）
- [ ] 確認 Webhook URL（匯入後會變新的）
- [ ] 確認 Schedule trigger 時區
- [ ] 測試 LLM 節點 provider 設定
- [ ] 啟用 Error Workflow 連結

---

## 3. 範本命名與版本規範 / Naming & Versioning

```
templates/
├── G-1-email-triage.v1.json          # PoC ID + 名稱 + 版本
├── G-2-sales-email-summary.v1.json
├── S-1-questionnaire-scoring.v2.json
├── ...
└── _sub/                              # Sub-workflow library
    ├── sub-redact-pii.v1.json
    ├── sub-llm-call-router.v1.json
    └── sub-audit-log.v1.json
```

| 規則 | 說明 |
| --- | --- |
| 檔名 | `{PoC-ID}-{slug}.v{n}.json` |
| 版本 | 每次 breaking change +1；非破壞性改 patch note |
| Sub-workflow | 放 `_sub/`，前綴 `sub-` |
| Commit | 每個 workflow 改動獨立 commit |

---

## 4. 範本骨架 / Workflow Skeletons

> 以下為 **教學用骨架**，節點結構正確但 credentials / 實際 prompt 需學員填入。
> Teaching skeletons — node structure is correct; credentials and actual prompts to be filled by learners.

### 4.1 G-1 客服信件分流 / Email Triage（骨架）

```json
{
  "name": "G-1 Email Triage",
  "nodes": [
    { "name": "Gmail Trigger", "type": "n8n-nodes-base.gmailTrigger",
      "parameters": { "event": "messageReceived", "filters": {} } },
    { "name": "Extract Fields", "type": "n8n-nodes-base.set",
      "parameters": { "fields": ["from", "subject", "bodyPlain"] } },
    { "name": "Classify (LLM)", "type": "n8n-nodes-base.openAi",
      "parameters": {
        "resource": "chat",
        "systemPrompt": "<分類定義 + SLA；輸出 JSON {category,priority,summary,suggested_action}>",
        "userPrompt": "={{ $json.subject }}\\n\\n{{ $json.bodyPlain }}" } },
    { "name": "IF P0", "type": "n8n-nodes-base.if",
      "parameters": { "condition": "={{ $json.priority === 'P0' }}" } },
    { "name": "Gmail Label", "type": "n8n-nodes-base.gmail",
      "parameters": { "operation": "addLabels" } },
    { "name": "Slack Alert", "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#cs-p0" } },
    { "name": "Audit Log", "type": "n8n-nodes-base.googleSheets",
      "parameters": { "operation": "append", "sheet": "aid_audit" } }
  ],
  "connections": {
    "Gmail Trigger": { "main": [[{ "node": "Extract Fields" }]] },
    "Extract Fields": { "main": [[{ "node": "Classify (LLM)" }]] },
    "Classify (LLM)": { "main": [[{ "node": "IF P0" }]] },
    "IF P0": { "main": [
      [{ "node": "Slack Alert" }, { "node": "Gmail Label" }],
      [{ "node": "Gmail Label" }]
    ] },
    "Gmail Label": { "main": [[{ "node": "Audit Log" }]] },
    "Slack Alert": { "main": [[{ "node": "Audit Log" }]] }
  }
}
```

### 4.2 S-1 問卷自動計分 / Questionnaire Scoring（骨架）

```json
{
  "name": "S-1 Questionnaire Scoring",
  "nodes": [
    { "name": "Form Webhook", "type": "n8n-nodes-base.webhook",
      "parameters": { "path": "diagnostic/submit", "httpMethod": "POST" } },
    { "name": "Validate", "type": "n8n-nodes-base.set",
      "parameters": { "note": "檢查必填、預設 language=zh-TW" } },
    { "name": "Idempotency Check", "type": "n8n-nodes-base.n8n",
      "parameters": { "note": "Data Table lookup by submission_id" } },
    { "name": "Score (Function)", "type": "n8n-nodes-base.function",
      "parameters": { "note": "六構面平均 + overall + level，邏輯見 AI_DIAGNOSIS_SHEETS_SCHEMA.md" } },
    { "name": "Generate Narrative (LLM)", "type": "n8n-nodes-base.openAi",
      "parameters": { "resource": "chat", "systemPrompt": "<等級對應 prompt 模板>" } },
    { "name": "Sheets Append", "type": "n8n-nodes-base.googleSheets",
      "parameters": { "operation": "append" } },
    { "name": "Email Report", "type": "n8n-nodes-base.gmail",
      "parameters": { "operation": "send" } }
  ],
  "connections": {
    "Form Webhook": { "main": [[{ "node": "Validate" }]] },
    "Validate": { "main": [[{ "node": "Idempotency Check" }]] },
    "Idempotency Check": { "main": [[{ "node": "Score (Function)" }]] },
    "Score (Function)": { "main": [[{ "node": "Generate Narrative (LLM)" }]] },
    "Generate Narrative (LLM)": { "main": [[{ "node": "Sheets Append" }]] },
    "Sheets Append": { "main": [[{ "node": "Email Report" }]] }
  }
}
```

### 4.3 Sub-workflow：PII Redaction（骨架）

```json
{
  "name": "sub-redact-pii",
  "nodes": [
    { "name": "Sub Trigger", "type": "n8n-nodes-base.executeWorkflowTrigger" },
    { "name": "Regex Redact", "type": "n8n-nodes-base.function",
      "parameters": { "note": "身分證 / 電話 / email / 信用卡 regex 遮蔽" } },
    { "name": "Return", "type": "n8n-nodes-base.set",
      "parameters": { "fields": ["redactedText"] } }
  ],
  "connections": {
    "Sub Trigger": { "main": [[{ "node": "Regex Redact" }]] },
    "Regex Redact": { "main": [[{ "node": "Return" }]] }
  }
}
```

> **用途**：所有要送雲 LLM 的文字，先過 `sub-redact-pii`。Hybrid / 高敏感部署的必備 sub-workflow。

### 4.4 Error Workflow：統一錯誤處理（骨架）

```json
{
  "name": "_error-handler",
  "nodes": [
    { "name": "Error Trigger", "type": "n8n-nodes-base.errorTrigger" },
    { "name": "Format Error", "type": "n8n-nodes-base.set" },
    { "name": "LLM Root Cause", "type": "n8n-nodes-base.openAi",
      "parameters": { "note": "摘要失敗原因（讀 error stack）" } },
    { "name": "Slack Alert", "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#n8n-errors" } },
    { "name": "DLQ Append", "type": "n8n-nodes-base.googleSheets",
      "parameters": { "operation": "append", "sheet": "aid_errors" } }
  ],
  "connections": {
    "Error Trigger": { "main": [[{ "node": "Format Error" }]] },
    "Format Error": { "main": [[{ "node": "LLM Root Cause" }]] },
    "LLM Root Cause": { "main": [[{ "node": "Slack Alert" }, { "node": "DLQ Append" }]] }
  }
}
```

> 在每個 production workflow 的 Settings → Error Workflow 指定此 `_error-handler`。

---

## 4.5 其餘 28 個 PoC 骨架 / The Remaining 28 PoC Skeletons

> 以下骨架對應 [`POC_SCENARIO_SPECS.md`](POC_SCENARIO_SPECS.md) 的 30 個 PoC（G-1、S-1 已於 §4.1、§4.2 給出完整版）。為節省篇幅，以下採精簡骨架格式：`name` + `nodes`（節點名稱與類型）+ `connections`（節點串接順序）。credentials、實際 prompt、參數仍須學員填入；機敏情境須前置 `sub-redact-pii`、接上 `_error-handler`。
>
> These skeletons map to the 30 PoCs in `POC_SCENARIO_SPECS.md` (G-1 and S-1 already given in full in §4.1, §4.2). For brevity, a compact skeleton format is used below: `name` + `nodes` (node names and types) + `connections` (wiring order). Credentials, actual prompts, and parameters must still be filled in by learners; sensitive scenarios must prepend `sub-redact-pii` and wire up `_error-handler`.

### 4.5.1 Gmail PoCs（G-2 ~ G-4）

```json
{ "name": "G-2 Sales Email Summary",
  "nodes": [
    {"name":"Schedule","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"Gmail Search 24h","type":"n8n-nodes-base.gmail"},
    {"name":"Loop Over","type":"n8n-nodes-base.splitInBatches"},
    {"name":"Summarize (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Merge","type":"n8n-nodes-base.merge"},
    {"name":"Format Email","type":"n8n-nodes-base.set"},
    {"name":"Gmail Send","type":"n8n-nodes-base.gmail"},
    {"name":"Notion Create","type":"n8n-nodes-base.notion"}
  ],
  "connections": {
    "Schedule":{"main":[[{"node":"Gmail Search 24h"}]]},
    "Gmail Search 24h":{"main":[[{"node":"Loop Over"}]]},
    "Loop Over":{"main":[[{"node":"Summarize (LLM)"}]]},
    "Summarize (LLM)":{"main":[[{"node":"Merge"}]]},
    "Merge":{"main":[[{"node":"Format Email"}]]},
    "Format Email":{"main":[[{"node":"Gmail Send"},{"node":"Notion Create"}]]}
  }
}
```

```json
{ "name": "G-3 Executive Daily Digest",
  "nodes": [
    {"name":"Schedule 8am","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"Gmail Search","type":"n8n-nodes-base.gmail"},
    {"name":"Rank (Function)","type":"n8n-nodes-base.function"},
    {"name":"Digest (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Format HTML","type":"n8n-nodes-base.set"},
    {"name":"Gmail Send","type":"n8n-nodes-base.gmail"}
  ],
  "connections": {
    "Schedule 8am":{"main":[[{"node":"Gmail Search"}]]},
    "Gmail Search":{"main":[[{"node":"Rank (Function)"}]]},
    "Rank (Function)":{"main":[[{"node":"Digest (LLM)"}]]},
    "Digest (LLM)":{"main":[[{"node":"Format HTML"}]]},
    "Format HTML":{"main":[[{"node":"Gmail Send"}]]}
  }
}
```

```json
{ "name": "G-4 Auto-Reply Draft",
  "nodes": [
    {"name":"Gmail Trigger","type":"n8n-nodes-base.gmailTrigger"},
    {"name":"Notion Search (RAG)","type":"n8n-nodes-base.notion"},
    {"name":"Draft (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Gmail Create Draft","type":"n8n-nodes-base.gmail"}
  ],
  "connections": {
    "Gmail Trigger":{"main":[[{"node":"Notion Search (RAG)"}]]},
    "Notion Search (RAG)":{"main":[[{"node":"Draft (LLM)"}]]},
    "Draft (LLM)":{"main":[[{"node":"Gmail Create Draft"}]]}
  }
}
```

### 4.5.2 Google Sheets PoCs（S-2 ~ S-5）

```json
{ "name": "S-2 Monthly KPI Auto-Refresh",
  "nodes": [
    {"name":"Schedule 1st 6am","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"HTTP Sources","type":"n8n-nodes-base.httpRequest"},
    {"name":"Consolidate (Function)","type":"n8n-nodes-base.function"},
    {"name":"Sheets Update","type":"n8n-nodes-base.googleSheets"},
    {"name":"Interpret (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Email","type":"n8n-nodes-base.gmail"}
  ],
  "connections": {
    "Schedule 1st 6am":{"main":[[{"node":"HTTP Sources"}]]},
    "HTTP Sources":{"main":[[{"node":"Consolidate (Function)"}]]},
    "Consolidate (Function)":{"main":[[{"node":"Sheets Update"}]]},
    "Sheets Update":{"main":[[{"node":"Interpret (LLM)"}]]},
    "Interpret (LLM)":{"main":[[{"node":"Email"}]]}
  }
}
```

```json
{ "name": "S-3 Workflow Execution Log & Failure Monitor",
  "nodes": [
    {"name":"Error Trigger","type":"n8n-nodes-base.errorTrigger"},
    {"name":"Set","type":"n8n-nodes-base.set"},
    {"name":"Root Cause (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Slack","type":"n8n-nodes-base.slack"},
    {"name":"Sheets","type":"n8n-nodes-base.googleSheets"}
  ],
  "connections": {
    "Error Trigger":{"main":[[{"node":"Set"}]]},
    "Set":{"main":[[{"node":"Root Cause (LLM)"}]]},
    "Root Cause (LLM)":{"main":[[{"node":"Slack"},{"node":"Sheets"}]]}
  }
}
```

```json
{ "name": "S-4 Customer List Dedup & Classification",
  "nodes": [
    {"name":"Manual Trigger","type":"n8n-nodes-base.manualTrigger"},
    {"name":"Sheets Source A/B/C","type":"n8n-nodes-base.googleSheets"},
    {"name":"Merge","type":"n8n-nodes-base.merge"},
    {"name":"Initial Dedup (Function)","type":"n8n-nodes-base.function"},
    {"name":"Fuzzy Match (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Sheets Output","type":"n8n-nodes-base.googleSheets"}
  ],
  "connections": {
    "Manual Trigger":{"main":[[{"node":"Sheets Source A/B/C"}]]},
    "Sheets Source A/B/C":{"main":[[{"node":"Merge"}]]},
    "Merge":{"main":[[{"node":"Initial Dedup (Function)"}]]},
    "Initial Dedup (Function)":{"main":[[{"node":"Fuzzy Match (LLM)"}]]},
    "Fuzzy Match (LLM)":{"main":[[{"node":"Sheets Output"}]]}
  }
}
```

```json
{ "name": "S-5 Budget vs Spend Variance",
  "nodes": [
    {"name":"Schedule Month-End","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"SAP API","type":"n8n-nodes-base.httpRequest"},
    {"name":"Sheets Budget","type":"n8n-nodes-base.googleSheets"},
    {"name":"Merge","type":"n8n-nodes-base.merge"},
    {"name":"Compare (Function)","type":"n8n-nodes-base.function"},
    {"name":"Explain (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Format","type":"n8n-nodes-base.set"},
    {"name":"Email","type":"n8n-nodes-base.gmail"}
  ],
  "connections": {
    "Schedule Month-End":{"main":[[{"node":"SAP API"},{"node":"Sheets Budget"}]]},
    "SAP API":{"main":[[{"node":"Merge"}]]},
    "Sheets Budget":{"main":[[{"node":"Merge"}]]},
    "Merge":{"main":[[{"node":"Compare (Function)"}]]},
    "Compare (Function)":{"main":[[{"node":"Explain (LLM)"}]]},
    "Explain (LLM)":{"main":[[{"node":"Format"}]]},
    "Format":{"main":[[{"node":"Email"}]]}
  }
}
```

### 4.5.3 Notion PoCs（N-1 ~ N-5）

```json
{ "name": "N-1 Meeting Transcript to Actions",
  "nodes": [
    {"name":"Notion Trigger","type":"n8n-nodes-base.notionTrigger"},
    {"name":"Whisper (HTTP)","type":"n8n-nodes-base.httpRequest"},
    {"name":"Summarize (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Parse Actions (Function)","type":"n8n-nodes-base.function"},
    {"name":"Notion Update","type":"n8n-nodes-base.notion"},
    {"name":"Notion Create Actions","type":"n8n-nodes-base.notion"}
  ],
  "connections": {
    "Notion Trigger":{"main":[[{"node":"Whisper (HTTP)"}]]},
    "Whisper (HTTP)":{"main":[[{"node":"Summarize (LLM)"}]]},
    "Summarize (LLM)":{"main":[[{"node":"Parse Actions (Function)"}]]},
    "Parse Actions (Function)":{"main":[[{"node":"Notion Update"},{"node":"Notion Create Actions"}]]}
  }
}
```

```json
{ "name": "N-2 Consulting Diagnostic Database",
  "nodes": [
    {"name":"Webhook","type":"n8n-nodes-base.webhook"},
    {"name":"Generate Outline (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Loop","type":"n8n-nodes-base.splitInBatches"},
    {"name":"Notion Create Page","type":"n8n-nodes-base.notion"},
    {"name":"Notion Update Relations","type":"n8n-nodes-base.notion"}
  ],
  "connections": {
    "Webhook":{"main":[[{"node":"Generate Outline (LLM)"}]]},
    "Generate Outline (LLM)":{"main":[[{"node":"Loop"}]]},
    "Loop":{"main":[[{"node":"Notion Create Page"}]]},
    "Notion Create Page":{"main":[[{"node":"Notion Update Relations"}]]}
  }
}
```

```json
{ "name": "N-3 Skill Library Template & Versioning",
  "nodes": [
    {"name":"Webhook","type":"n8n-nodes-base.webhook"},
    {"name":"Generate IPOE (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Notion Create","type":"n8n-nodes-base.notion"},
    {"name":"GitHub Create File","type":"n8n-nodes-base.github"}
  ],
  "connections": {
    "Webhook":{"main":[[{"node":"Generate IPOE (LLM)"}]]},
    "Generate IPOE (LLM)":{"main":[[{"node":"Notion Create"}]]},
    "Notion Create":{"main":[[{"node":"GitHub Create File"}]]}
  }
}
```

```json
{ "name": "N-4 Auto Task Assignment",
  "nodes": [
    {"name":"Trigger (Sheets/Webhook)","type":"n8n-nodes-base.webhook"},
    {"name":"Notion Search Skill Matrix","type":"n8n-nodes-base.notion"},
    {"name":"Assign (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Notion Create Task","type":"n8n-nodes-base.notion"},
    {"name":"Slack DM","type":"n8n-nodes-base.slack"}
  ],
  "connections": {
    "Trigger (Sheets/Webhook)":{"main":[[{"node":"Notion Search Skill Matrix"}]]},
    "Notion Search Skill Matrix":{"main":[[{"node":"Assign (LLM)"}]]},
    "Assign (LLM)":{"main":[[{"node":"Notion Create Task"},{"node":"Slack DM"}]]}
  }
}
```

```json
{ "name": "N-5 Internal Q&A over Notion (RAG)",
  "nodes": [
    {"name":"Slack Trigger","type":"n8n-nodes-base.slackTrigger"},
    {"name":"Embedding Query (HTTP)","type":"n8n-nodes-base.httpRequest"},
    {"name":"Vector Search (HTTP)","type":"n8n-nodes-base.httpRequest"},
    {"name":"Answer (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Slack Reply","type":"n8n-nodes-base.slack"}
  ],
  "connections": {
    "Slack Trigger":{"main":[[{"node":"Embedding Query (HTTP)"}]]},
    "Embedding Query (HTTP)":{"main":[[{"node":"Vector Search (HTTP)"}]]},
    "Vector Search (HTTP)":{"main":[[{"node":"Answer (LLM)"}]]},
    "Answer (LLM)":{"main":[[{"node":"Slack Reply"}]]}
  }
}
```

### 4.5.4 CRM PoCs（C-1 ~ C-5）

```json
{ "name": "C-1 Conversational Customer Lookup",
  "nodes": [
    {"name":"Slack Trigger","type":"n8n-nodes-base.slackTrigger"},
    {"name":"CRM Search","type":"n8n-nodes-base.httpRequest"},
    {"name":"Summary (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Slack Reply","type":"n8n-nodes-base.slack"}
  ],
  "connections": {
    "Slack Trigger":{"main":[[{"node":"CRM Search"}]]},
    "CRM Search":{"main":[[{"node":"Summary (LLM)"}]]},
    "Summary (LLM)":{"main":[[{"node":"Slack Reply"}]]}
  }
}
```

```json
{ "name": "C-2 Opportunity Summary & Next-Step",
  "nodes": [
    {"name":"Schedule Sun 8pm","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"CRM API","type":"n8n-nodes-base.httpRequest"},
    {"name":"Loop","type":"n8n-nodes-base.splitInBatches"},
    {"name":"Brief (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Format","type":"n8n-nodes-base.set"},
    {"name":"Email","type":"n8n-nodes-base.gmail"},
    {"name":"Notion Create","type":"n8n-nodes-base.notion"}
  ],
  "connections": {
    "Schedule Sun 8pm":{"main":[[{"node":"CRM API"}]]},
    "CRM API":{"main":[[{"node":"Loop"}]]},
    "Loop":{"main":[[{"node":"Brief (LLM)"}]]},
    "Brief (LLM)":{"main":[[{"node":"Format"}]]},
    "Format":{"main":[[{"node":"Email"},{"node":"Notion Create"}]]}
  }
}
```

```json
{ "name": "C-3 Post-Visit Note Auto-Update",
  "nodes": [
    {"name":"Slack Trigger","type":"n8n-nodes-base.slackTrigger"},
    {"name":"Whisper (HTTP)","type":"n8n-nodes-base.httpRequest"},
    {"name":"Extract (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"CRM Update","type":"n8n-nodes-base.httpRequest"}
  ],
  "connections": {
    "Slack Trigger":{"main":[[{"node":"Whisper (HTTP)"}]]},
    "Whisper (HTTP)":{"main":[[{"node":"Extract (LLM)"}]]},
    "Extract (LLM)":{"main":[[{"node":"CRM Update"}]]}
  }
}
```

```json
{ "name": "C-4 Complaint Tracking & Escalation",
  "nodes": [
    {"name":"CRM Webhook","type":"n8n-nodes-base.webhook"},
    {"name":"Schedule 30min","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"SLA Check (Function)","type":"n8n-nodes-base.function"},
    {"name":"Sentiment (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Slack","type":"n8n-nodes-base.slack"},
    {"name":"CRM Update","type":"n8n-nodes-base.httpRequest"}
  ],
  "connections": {
    "CRM Webhook":{"main":[[{"node":"SLA Check (Function)"}]]},
    "Schedule 30min":{"main":[[{"node":"SLA Check (Function)"}]]},
    "SLA Check (Function)":{"main":[[{"node":"Sentiment (LLM)"}]]},
    "Sentiment (LLM)":{"main":[[{"node":"Slack"},{"node":"CRM Update"}]]}
  }
}
```

```json
{ "name": "C-5 Customer Health Score",
  "nodes": [
    {"name":"Schedule Mon 9am","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"CRM API","type":"n8n-nodes-base.httpRequest"},
    {"name":"Product DB","type":"n8n-nodes-base.httpRequest"},
    {"name":"Billing","type":"n8n-nodes-base.httpRequest"},
    {"name":"Merge","type":"n8n-nodes-base.merge"},
    {"name":"Score (Function)","type":"n8n-nodes-base.function"},
    {"name":"Narrative (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"CRM Update","type":"n8n-nodes-base.httpRequest"},
    {"name":"Slack","type":"n8n-nodes-base.slack"}
  ],
  "connections": {
    "Schedule Mon 9am":{"main":[[{"node":"CRM API"},{"node":"Product DB"},{"node":"Billing"}]]},
    "CRM API":{"main":[[{"node":"Merge"}]]},
    "Product DB":{"main":[[{"node":"Merge"}]]},
    "Billing":{"main":[[{"node":"Merge"}]]},
    "Merge":{"main":[[{"node":"Score (Function)"}]]},
    "Score (Function)":{"main":[[{"node":"Narrative (LLM)"}]]},
    "Narrative (LLM)":{"main":[[{"node":"CRM Update"},{"node":"Slack"}]]}
  }
}
```

### 4.5.5 API PoCs（A-1 ~ A-5）

```json
{ "name": "A-1 Internal Webhook Subscriber",
  "nodes": [
    {"name":"Webhook","type":"n8n-nodes-base.webhook"},
    {"name":"Switch","type":"n8n-nodes-base.switch"},
    {"name":"Sub-workflow A","type":"n8n-nodes-base.executeWorkflow"},
    {"name":"Sub-workflow B","type":"n8n-nodes-base.executeWorkflow"},
    {"name":"Audit Log","type":"n8n-nodes-base.googleSheets"}
  ],
  "connections": {
    "Webhook":{"main":[[{"node":"Switch"}]]},
    "Switch":{"main":[[{"node":"Sub-workflow A"}],[{"node":"Sub-workflow B"}]]},
    "Sub-workflow A":{"main":[[{"node":"Audit Log"}]]},
    "Sub-workflow B":{"main":[[{"node":"Audit Log"}]]}
  }
}
```

```json
{ "name": "A-2 External API Integration",
  "nodes": [
    {"name":"Slack Trigger","type":"n8n-nodes-base.slackTrigger"},
    {"name":"Intent (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Switch","type":"n8n-nodes-base.switch"},
    {"name":"HTTP API","type":"n8n-nodes-base.httpRequest"},
    {"name":"Format (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Slack Reply","type":"n8n-nodes-base.slack"}
  ],
  "connections": {
    "Slack Trigger":{"main":[[{"node":"Intent (LLM)"}]]},
    "Intent (LLM)":{"main":[[{"node":"Switch"}]]},
    "Switch":{"main":[[{"node":"HTTP API"}]]},
    "HTTP API":{"main":[[{"node":"Format (LLM)"}]]},
    "Format (LLM)":{"main":[[{"node":"Slack Reply"}]]}
  }
}
```

```json
{ "name": "A-3 Retry & Idempotency",
  "nodes": [
    {"name":"Gen Key (Function)","type":"n8n-nodes-base.function"},
    {"name":"Data Table Lookup","type":"n8n-nodes-base.n8n"},
    {"name":"HTTP with Retry","type":"n8n-nodes-base.httpRequest"},
    {"name":"DLQ (Data Table)","type":"n8n-nodes-base.n8n"}
  ],
  "connections": {
    "Gen Key (Function)":{"main":[[{"node":"Data Table Lookup"}]]},
    "Data Table Lookup":{"main":[[{"node":"HTTP with Retry"}]]},
    "HTTP with Retry":{"main":[[{"node":"DLQ (Data Table)"}]]}
  }
}
```

```json
{ "name": "A-4 Rate-Limit Handling & Scheduling",
  "nodes": [
    {"name":"Trigger","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"Loop with Wait","type":"n8n-nodes-base.splitInBatches"},
    {"name":"HTTP","type":"n8n-nodes-base.httpRequest"},
    {"name":"If 429","type":"n8n-nodes-base.if"},
    {"name":"Wait + Retry","type":"n8n-nodes-base.wait"}
  ],
  "connections": {
    "Trigger":{"main":[[{"node":"Loop with Wait"}]]},
    "Loop with Wait":{"main":[[{"node":"HTTP"}]]},
    "HTTP":{"main":[[{"node":"If 429"}]]},
    "If 429":{"main":[[{"node":"Wait + Retry"}],[]]},
    "Wait + Retry":{"main":[[{"node":"HTTP"}]]}
  }
}
```

```json
{ "name": "A-5 Multi-API Aggregation",
  "nodes": [
    {"name":"Trigger","type":"n8n-nodes-base.webhook"},
    {"name":"Split In Batches","type":"n8n-nodes-base.splitInBatches"},
    {"name":"HTTP Parallel","type":"n8n-nodes-base.httpRequest"},
    {"name":"Merge","type":"n8n-nodes-base.merge"},
    {"name":"Synthesize (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Reply","type":"n8n-nodes-base.respondToWebhook"}
  ],
  "connections": {
    "Trigger":{"main":[[{"node":"Split In Batches"}]]},
    "Split In Batches":{"main":[[{"node":"HTTP Parallel"}]]},
    "HTTP Parallel":{"main":[[{"node":"Merge"}]]},
    "Merge":{"main":[[{"node":"Synthesize (LLM)"}]]},
    "Synthesize (LLM)":{"main":[[{"node":"Reply"}]]}
  }
}
```

### 4.5.6 ERP PoCs（E-1 ~ E-6）

```json
{ "name": "E-1 Order Status Lookup",
  "nodes": [
    {"name":"Slack Trigger","type":"n8n-nodes-base.slackTrigger"},
    {"name":"ERP API","type":"n8n-nodes-base.httpRequest"},
    {"name":"Format (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Slack Reply","type":"n8n-nodes-base.slack"}
  ],
  "connections": {
    "Slack Trigger":{"main":[[{"node":"ERP API"}]]},
    "ERP API":{"main":[[{"node":"Format (LLM)"}]]},
    "Format (LLM)":{"main":[[{"node":"Slack Reply"}]]}
  }
}
```

```json
{ "name": "E-2 Inventory Anomaly Alert",
  "nodes": [
    {"name":"Schedule 6h","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"ERP API","type":"n8n-nodes-base.httpRequest"},
    {"name":"Rule Check (Function)","type":"n8n-nodes-base.function"},
    {"name":"Interpret (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Slack","type":"n8n-nodes-base.slack"}
  ],
  "connections": {
    "Schedule 6h":{"main":[[{"node":"ERP API"}]]},
    "ERP API":{"main":[[{"node":"Rule Check (Function)"}]]},
    "Rule Check (Function)":{"main":[[{"node":"Interpret (LLM)"}]]},
    "Interpret (LLM)":{"main":[[{"node":"Slack"}]]}
  }
}
```

```json
{ "name": "E-3 Shipping Delay Analysis",
  "nodes": [
    {"name":"Schedule 6pm","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"ERP","type":"n8n-nodes-base.httpRequest"},
    {"name":"WMS","type":"n8n-nodes-base.httpRequest"},
    {"name":"Logistics","type":"n8n-nodes-base.httpRequest"},
    {"name":"Merge","type":"n8n-nodes-base.merge"},
    {"name":"Analyze (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Email","type":"n8n-nodes-base.gmail"}
  ],
  "connections": {
    "Schedule 6pm":{"main":[[{"node":"ERP"},{"node":"WMS"},{"node":"Logistics"}]]},
    "ERP":{"main":[[{"node":"Merge"}]]},
    "WMS":{"main":[[{"node":"Merge"}]]},
    "Logistics":{"main":[[{"node":"Merge"}]]},
    "Merge":{"main":[[{"node":"Analyze (LLM)"}]]},
    "Analyze (LLM)":{"main":[[{"node":"Email"}]]}
  }
}
```

```json
{ "name": "E-4 Purchase Reconciliation Diff",
  "nodes": [
    {"name":"Schedule Month-End","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"ERP API","type":"n8n-nodes-base.httpRequest"},
    {"name":"OCR (HTTP)","type":"n8n-nodes-base.httpRequest"},
    {"name":"Merge","type":"n8n-nodes-base.merge"},
    {"name":"Reconcile (Function)","type":"n8n-nodes-base.function"},
    {"name":"Explain (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Sheets","type":"n8n-nodes-base.googleSheets"}
  ],
  "connections": {
    "Schedule Month-End":{"main":[[{"node":"ERP API"},{"node":"OCR (HTTP)"}]]},
    "ERP API":{"main":[[{"node":"Merge"}]]},
    "OCR (HTTP)":{"main":[[{"node":"Merge"}]]},
    "Merge":{"main":[[{"node":"Reconcile (Function)"}]]},
    "Reconcile (Function)":{"main":[[{"node":"Explain (LLM)"}]]},
    "Explain (LLM)":{"main":[[{"node":"Sheets"}]]}
  }
}
```

```json
{ "name": "E-5 Month-End Exception Summary",
  "nodes": [
    {"name":"Schedule Month-End+1","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"ERP GL Query","type":"n8n-nodes-base.httpRequest"},
    {"name":"Find Exceptions (Function)","type":"n8n-nodes-base.function"},
    {"name":"Summarize (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Email CFO","type":"n8n-nodes-base.gmail"},
    {"name":"Notion Archive","type":"n8n-nodes-base.notion"}
  ],
  "connections": {
    "Schedule Month-End+1":{"main":[[{"node":"ERP GL Query"}]]},
    "ERP GL Query":{"main":[[{"node":"Find Exceptions (Function)"}]]},
    "Find Exceptions (Function)":{"main":[[{"node":"Summarize (LLM)"}]]},
    "Summarize (LLM)":{"main":[[{"node":"Email CFO"},{"node":"Notion Archive"}]]}
  }
}
```

```json
{ "name": "E-6 Daily Cross-Functional KPI Digest",
  "nodes": [
    {"name":"Schedule 8am","type":"n8n-nodes-base.scheduleTrigger"},
    {"name":"ERP","type":"n8n-nodes-base.httpRequest"},
    {"name":"CRM","type":"n8n-nodes-base.httpRequest"},
    {"name":"Sheets","type":"n8n-nodes-base.googleSheets"},
    {"name":"Merge","type":"n8n-nodes-base.merge"},
    {"name":"Digest per Role (LLM)","type":"n8n-nodes-base.openAi"},
    {"name":"Email","type":"n8n-nodes-base.gmail"}
  ],
  "connections": {
    "Schedule 8am":{"main":[[{"node":"ERP"},{"node":"CRM"},{"node":"Sheets"}]]},
    "ERP":{"main":[[{"node":"Merge"}]]},
    "CRM":{"main":[[{"node":"Merge"}]]},
    "Sheets":{"main":[[{"node":"Merge"}]]},
    "Merge":{"main":[[{"node":"Digest per Role (LLM)"}]]},
    "Digest per Role (LLM)":{"main":[[{"node":"Email"}]]}
  }
}
```

> 以上 28 個骨架 + §4.1-§4.4 的 G-1 / S-1 / sub-redact-pii / _error-handler，涵蓋 `POC_SCENARIO_SPECS.md` 全部 30 個 PoC。每個骨架仍須學員填入 credentials、實際 prompt、節點參數，並依 §2.3 匯入後 checklist 與 §8 注意事項完成上線前準備。

---

## 5. GitHub Backup SOP

```bash
# 每日定時匯出（n8n self-host cron 或 GitHub Action）
n8n export:workflow --all --output=./templates/
git add templates/
git commit -m "n8n backup $(date +%F)"
git push origin main
```

| 規則 | 說明 |
| --- | --- |
| 頻率 | 每日自動 + 每次重大改動手動 |
| 範圍 | workflows + sub-workflows，**不含** credentials |
| Secret | credentials 另存企業密鑰管理（Vault / Secret Manager），絕不進 git |
| 回復 | `n8n import:workflow --input=...` 從 git 任一版本還原 |

---

## 6. 課堂使用流程 / Classroom Flow

| 步驟 | 講師 | 學員 |
| --- | --- | --- |
| 1 | 發布範本骨架到課程 GitHub | clone repo |
| 2 | 講解 PoC 對應的骨架 | 匯入 .json |
| 3 | 示範填 credentials + prompt | 跟著填 |
| 4 | 示範測試 + 看 execution log | 自己測 |
| 5 | 講解 Error Workflow + Audit | 接上 `_error-handler` |
| 6 | Stage Gate 3 驗收 | 提交 execution log 截圖 |

---

## 7. 對應 PoC 清單 / Mapping to PoC Specs

本檔 4 個骨架對應 [`POC_SCENARIO_SPECS.md`](POC_SCENARIO_SPECS.md)；其餘 26 個 PoC 之骨架建議由課程講師依相同模式逐步補齊，存入 `templates/`：

| 骨架 | PoC | 狀態 |
| --- | --- | --- |
| `G-1-email-triage` | G-1 客服信件分流 | ✅ 本檔 |
| `S-1-questionnaire-scoring` | S-1 問卷自動計分 | ✅ 本檔 |
| `sub-redact-pii` | （跨 PoC 共用） | ✅ 本檔 |
| `_error-handler` | （跨 PoC 共用） | ✅ 本檔 |
| G-2 ~ E-6 其餘 26 個 | 見 POC_SCENARIO_SPECS.md | ⏳ 課程逐步補 |

---

## 8. 注意事項 / Notes

- 範本骨架為**教學用**，節點結構正確但 **不可直接上 production** — 須補 credentials、實際 prompt、測試。
- 匯出 JSON **不含金鑰**；切勿把含 credentials 的檔案 commit 進 git。
- 機敏資料情境：LLM 節點改指地端 / Azure OpenAI 隔離 tenant，並前置 `sub-redact-pii`。
- n8n 版本差異可能造成節點 type 名稱不同，匯入後請確認。

引用：PoC 細稿見 [`POC_SCENARIO_SPECS.md`](POC_SCENARIO_SPECS.md)；診斷自動化 schema 見 [`../01_Assessment/AI_DIAGNOSIS_SHEETS_SCHEMA.md`](../01_Assessment/AI_DIAGNOSIS_SHEETS_SCHEMA.md)。
