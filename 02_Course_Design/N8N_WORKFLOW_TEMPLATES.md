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
