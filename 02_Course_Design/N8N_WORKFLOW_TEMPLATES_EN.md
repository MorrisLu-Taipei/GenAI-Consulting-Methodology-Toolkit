# n8n Workflow Templates & Import Guide

> 🌐 中文版本 / Chinese version: [N8N_WORKFLOW_TEMPLATES.md](N8N_WORKFLOW_TEMPLATES.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

Turns the PoCs from [`POC_SCENARIO_SPECS.md`](POC_SCENARIO_SPECS.md) into importable n8n workflow skeletons (JSON), plus the standard process for sharing, version-controlling, and backing them up in class.

---

## 1. Why Templatize

| Without templates | With templates |
| --- | --- |
| Every learner builds nodes from scratch | Import a skeleton, focus on prompts and mapping |
| Workflows scattered across personal accounts | Centralized in a Sub-workflow Library |
| No version control | GitHub backup + version numbers |
| Cannot be reproduced after class | The enterprise can re-deploy repeatedly |

---

## 2. n8n Template Export & Import

### 2.1 Export

```
n8n UI → open workflow → top-right ⋯ menu → Download
→ produces {workflow-name}.json
```

Or via the n8n CLI (self-host):

```bash
n8n export:workflow --id=<workflow-id> --output=./templates/
n8n export:workflow --all --output=./templates/    # export everything
```

### 2.2 Import

```
n8n UI → Workflows → Import from File → select .json
```

Or CLI:

```bash
n8n import:workflow --input=./templates/G-1-email-triage.json
```

### 2.3 Post-import checklist

- [ ] Re-bind Credentials (the exported JSON does NOT contain keys)
- [ ] Confirm the Webhook URL (it changes on import)
- [ ] Confirm the Schedule trigger time zone
- [ ] Test the LLM node provider settings
- [ ] Wire up the Error Workflow link

---

## 3. Naming & Versioning

```
templates/
├── G-1-email-triage.v1.json          # PoC ID + name + version
├── G-2-sales-email-summary.v1.json
├── S-1-questionnaire-scoring.v2.json
├── ...
└── _sub/                              # Sub-workflow library
    ├── sub-redact-pii.v1.json
    ├── sub-llm-call-router.v1.json
    └── sub-audit-log.v1.json
```

| Rule | Description |
| --- | --- |
| Filename | `{PoC-ID}-{slug}.v{n}.json` |
| Version | +1 on each breaking change; non-breaking changes get a patch note |
| Sub-workflow | placed in `_sub/`, prefixed `sub-` |
| Commit | each workflow change in its own commit |

---

## 4. Workflow Skeletons

> The following are **teaching skeletons** — the node structure is correct, but credentials and actual prompts must be filled in by learners.

### 4.1 G-1 Email Triage (skeleton)

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
        "systemPrompt": "<classification definitions + SLA; output JSON {category,priority,summary,suggested_action}>",
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

### 4.2 S-1 Questionnaire Scoring (skeleton)

```json
{
  "name": "S-1 Questionnaire Scoring",
  "nodes": [
    { "name": "Form Webhook", "type": "n8n-nodes-base.webhook",
      "parameters": { "path": "diagnostic/submit", "httpMethod": "POST" } },
    { "name": "Validate", "type": "n8n-nodes-base.set",
      "parameters": { "note": "check required fields, default language=zh-TW" } },
    { "name": "Idempotency Check", "type": "n8n-nodes-base.n8n",
      "parameters": { "note": "Data Table lookup by submission_id" } },
    { "name": "Score (Function)", "type": "n8n-nodes-base.function",
      "parameters": { "note": "six-construct averages + overall + level; logic in AI_DIAGNOSIS_SHEETS_SCHEMA.md" } },
    { "name": "Generate Narrative (LLM)", "type": "n8n-nodes-base.openAi",
      "parameters": { "resource": "chat", "systemPrompt": "<level-specific prompt template>" } },
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

### 4.3 Sub-workflow: PII Redaction (skeleton)

```json
{
  "name": "sub-redact-pii",
  "nodes": [
    { "name": "Sub Trigger", "type": "n8n-nodes-base.executeWorkflowTrigger" },
    { "name": "Regex Redact", "type": "n8n-nodes-base.function",
      "parameters": { "note": "regex-mask national ID / phone / email / credit card" } },
    { "name": "Return", "type": "n8n-nodes-base.set",
      "parameters": { "fields": ["redactedText"] } }
  ],
  "connections": {
    "Sub Trigger": { "main": [[{ "node": "Regex Redact" }]] },
    "Regex Redact": { "main": [[{ "node": "Return" }]] }
  }
}
```

> **Purpose:** any text being sent to a cloud LLM should pass through `sub-redact-pii` first. An essential sub-workflow for Hybrid / high-sensitivity deployments.

### 4.4 Error Workflow: Unified Error Handling (skeleton)

```json
{
  "name": "_error-handler",
  "nodes": [
    { "name": "Error Trigger", "type": "n8n-nodes-base.errorTrigger" },
    { "name": "Format Error", "type": "n8n-nodes-base.set" },
    { "name": "LLM Root Cause", "type": "n8n-nodes-base.openAi",
      "parameters": { "note": "summarize failure cause (reads error stack)" } },
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

> Set this `_error-handler` as the Error Workflow in each production workflow's Settings → Error Workflow.

---

## 5. GitHub Backup SOP

```bash
# Scheduled daily export (n8n self-host cron or GitHub Action)
n8n export:workflow --all --output=./templates/
git add templates/
git commit -m "n8n backup $(date +%F)"
git push origin main
```

| Rule | Description |
| --- | --- |
| Frequency | daily automated + manual on each major change |
| Scope | workflows + sub-workflows, NOT credentials |
| Secrets | credentials stored in an enterprise key manager (Vault / Secret Manager), never in git |
| Restore | `n8n import:workflow --input=...` to restore from any git version |

---

## 6. Classroom Flow

| Step | Instructor | Learner |
| --- | --- | --- |
| 1 | Publish skeleton templates to the course GitHub | clone repo |
| 2 | Explain the skeleton matching the PoC | import the .json |
| 3 | Demo filling credentials + prompts | follow along |
| 4 | Demo testing + viewing the execution log | test it themselves |
| 5 | Explain the Error Workflow + Audit | wire up `_error-handler` |
| 6 | Stage Gate 3 sign-off | submit an execution-log screenshot |

---

## 7. Mapping to the PoC Specs

The 4 skeletons here map to [`POC_SCENARIO_SPECS.md`](POC_SCENARIO_SPECS.md); the remaining 26 PoC skeletons should be filled in progressively by course instructors following the same pattern, stored in `templates/`:

| Skeleton | PoC | Status |
| --- | --- | --- |
| `G-1-email-triage` | G-1 Email Triage | ✅ in this doc |
| `S-1-questionnaire-scoring` | S-1 Questionnaire Scoring | ✅ in this doc |
| `sub-redact-pii` | (shared across PoCs) | ✅ in this doc |
| `_error-handler` | (shared across PoCs) | ✅ in this doc |
| The other 26, G-2 ~ E-6 | see POC_SCENARIO_SPECS.md | ⏳ filled in progressively by the course |

---

## 8. Notes

- The skeletons are for **teaching** — the node structure is correct but they **cannot go straight to production** — credentials, actual prompts, and testing must be added.
- The exported JSON does **not** contain keys; never commit files containing credentials into git.
- For sensitive-data scenarios: switch the LLM node to on-prem / an Azure OpenAI isolated tenant, and prepend `sub-redact-pii`.
- n8n version differences may change node type names; verify after import.

References: PoC specs in [`POC_SCENARIO_SPECS.md`](POC_SCENARIO_SPECS.md); diagnosis-automation schema in [`../01_Assessment/AI_DIAGNOSIS_SHEETS_SCHEMA.md`](../01_Assessment/AI_DIAGNOSIS_SHEETS_SCHEMA.md).
