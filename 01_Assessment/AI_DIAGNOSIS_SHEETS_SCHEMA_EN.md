# AI Diagnosis Automation Schema

> 🌐 中文版本 / Chinese version: [AI_DIAGNOSIS_SHEETS_SCHEMA.md](AI_DIAGNOSIS_SHEETS_SCHEMA.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>

Implementation schemas for automating the AI maturity diagnostic across three platforms: Google Sheets, Notion, and n8n. This makes the path from questionnaire submission to auto-generated diagnostic summary fully automatable.

---

## A. Google Sheets Schema

### Sheet 1: `Raw Responses`

| Col | Name | Type | Example |
| --- | --- | --- | --- |
| A | timestamp | datetime | 2026-05-14 10:23:00 |
| B | submission_id | string (UUID) | 0f4a-8bd1-... |
| C | respondent_email | email | ceo@acme.com |
| D | company | string | Acme Corp |
| E | industry | enum | manufacturing / hospital / retail / ... |
| F | size_bucket | enum | <50 / 50-300 / 300-1000 / 1000+ |
| G | role | enum | CEO / COO / IT / dept-head / other |
| H-BG | Q1-Q50 | int 0-4 | per-question score |
| BH | language | enum | zh-TW / en |

### Sheet 2: `Scoring`

The six constructs and their question ranges:

| Construct | Question range | Formula (25-question version example) |
| --- | --- | --- |
| Tool Usage | Q1-Q4 | `=AVERAGE(Raw!H2:K2)` |
| Knowledge Codification | Q5-Q8 | `=AVERAGE(Raw!L2:O2)` |
| Process Standardization | Q9-Q12 | `=AVERAGE(Raw!P2:S2)` |
| System Integration | Q13-Q16 | `=AVERAGE(Raw!T2:W2)` |
| Agent Application | Q17-Q20 | `=AVERAGE(Raw!X2:AA2)` |
| Governance & ROI | Q21-Q25 | `=AVERAGE(Raw!AB2:AF2)` |

**Overall score:** `=AVERAGE(B2:G2)` (average of the six constructs)

**Level determination:**
```
=IF(H2>=3.5,"L5", IF(H2>=2.8,"L4", IF(H2>=2.0,"L3", IF(H2>=1.2,"L2","L1"))))
```

### Sheet 3: `Radar Data`

Per submission_id × the 6 construct scores, for use with the built-in Google Sheets radar chart.

### Sheet 4: `Recommendations`

Course-ratio lookup table driven by level:

| Level | L1 % | L2 % | L3 % | L4 % | L5 % | Key recommendation |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| L1 | 50 | 30 | 20 | 0 | 0 | Build the L1 org-wide foundation first |
| L2 | 25 | 40 | 25 | 10 | 0 | Focus on Skill packaging |
| L3 | 15 | 25 | 40 | 15 | 5 | Focus on Workflow PoCs |
| L4 | 10 | 15 | 25 | 35 | 15 | Bring Agents online |
| L5 | 5 | 10 | 20 | 30 | 35 | Multi-domain Agent Teams |

Formula example: `=VLOOKUP(Scoring!I2, RecLookup!A:G, 2, FALSE)`

### Sheet 5: `Cond Format Rules`

- Score ≥ 3.5 → green
- 2.0 ≤ Score < 3.5 → yellow
- Score < 2.0 → red

### Apps Script outline (Generate Report button)

```javascript
function generateReport() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const submission = ss.getSheetByName('Raw Responses').getRange('A:BH').getValues();
  const scoring = ss.getSheetByName('Scoring').getRange('A:I').getValues();
  // For latest submission_id:
  const latest = submission[submission.length - 1];
  const level = scoring[scoring.length - 1][8]; // Column I = Level
  // Build markdown report:
  let md = `# AI Maturity Diagnostic Report\n`;
  md += `Company: ${latest[3]} · Level: ${level}\n\n`;
  // ... (append per-construct scores, recommendations)
  // Send via Gmail or write to Docs
  DriveApp.createFile(`report-${latest[1]}.md`, md);
  GmailApp.sendEmail(latest[2], 'Your AI Diagnostic', md);
}
```

---

## B. Notion Database Schema

### 4 Databases

**1. `AID_Respondents`** — respondent master
- `email` (Title) · `name` · `company` (Relation → Companies DB) · `role` · `submitted_at`

**2. `AID_Responses`** — each questionnaire submission
- `submission_id` (Title)
- `respondent` (Relation → AID_Respondents)
- 25 / 50 number properties (Q1-Q50)
- `language`
- `version` (10 / 25 / 50 questions)
- `submitted_at`

**3. `AID_Scoring`** — computed results
- `submission_id` (Title; Relation → AID_Responses)
- 6 formula properties — construct averages:
  ```
  Tool Usage = (prop("Q1") + prop("Q2") + prop("Q3") + prop("Q4")) / 4
  ```
- `overall` (Formula: average of the six constructs)
- `level` (Formula): nested if, same logic as the Sheets version

**4. `AID_Recommendations`** — level → recommendation lookup
- `level` (Title: L1-L5)
- L1-L5 ratios (%)
- `priority_focus` (text)
- `gates` (text)

### Key Views

- `AID_Responses` table view (filter: submitted_at > 7 days ago)
- `AID_Scoring` gallery view (grouped by level)
- `AID_Recommendations` table view (for reference)

### Template page: "Diagnostic Report"

Each submission has an auto-generated child page with a template containing:
- Company info section
- Six-construct radar (embed Mermaid / external chart)
- Level determination
- Recommended course ratio
- Recommended priority adoption scenarios
- Next-step actions

---

## C. n8n Auto-Diagnosis Flow

### Node sequence (13 nodes + Error branch)

```
1. Webhook Trigger          /diagnostic/submit  POST { submission_id, answers[], meta }
2. Set                      Validate required fields; default language=zh-TW
3. Function                 Score construct averages + overall + level (JavaScript)
4. Switch (by level)        L1 / L2 / L3 / L4 / L5 → different next branches
5a-5e. OpenAI Chat / Claude Generate narrative summary using level-specific prompt template
6. Merge                    Re-join paths
7. Google Sheets            Append row to `aid_runs` Data Table
8. Notion                   Create page in AID_Responses + AID_Scoring + child Report page
9. Gmail                    Send report to respondent_email + consultant
10. Slack (optional)        #ai-diagnostics notify consultant
11. HTTP Response           Return { ok: true, level, report_url } to webhook caller
12. Error Trigger           catches any failure
13. Function (Error)        Log to `aid_errors` Data Table + notify dev
```

### Idempotency / Replay

- After Step 2, add a Data Table lookup: `SELECT * FROM aid_runs WHERE submission_id = $$submission_id`
- If it exists, short-circuit and return the existing result
- Add a separate `POST /aid/replay { submission_id }` webhook for regeneration (overwrites the old record)

### Construct-scoring Function example (Node 3)

```javascript
const a = $input.item.json.answers; // {Q1: 3, Q2: 2, ...}
const avg = (...keys) => keys.reduce((s, k) => s + (a[k] || 0), 0) / keys.length;

const constructs = {
  tool: avg('Q1','Q2','Q3','Q4'),
  knowledge: avg('Q5','Q6','Q7','Q8'),
  process: avg('Q9','Q10','Q11','Q12'),
  integration: avg('Q13','Q14','Q15','Q16'),
  agent: avg('Q17','Q18','Q19','Q20'),
  govroi: avg('Q21','Q22','Q23','Q24','Q25'),
};

const overall = Object.values(constructs).reduce((s,v) => s+v, 0) / 6;
const level =
  overall >= 3.5 ? 'L5' :
  overall >= 2.8 ? 'L4' :
  overall >= 2.0 ? 'L3' :
  overall >= 1.2 ? 'L2' : 'L1';

return [{ json: { ...$input.item.json, constructs, overall, level } }];
```

### Level-specific prompt templates (Nodes 5a-5e)

Each level's system prompt contains:
- The capability definition for that level
- Common blockers
- Recommended course ratio
- 30/60/90-day quick wins
- Governance checkpoints

The LLM produces a ~600-word customized narrative, attached to the email / Notion report.

### Deployment notes

- Deploy on the client's n8n instance (self-host recommended)
- Sensitive data: the webhook should enable HMAC signature verification
- LLM calls: for sensitive data, switch to Azure OpenAI / on-prem Llama
- Audit: write every call to an `aid_audit` Data Table — timestamp / level / latency / token usage

---

## D. Integration with the Course & Consulting Flow

| Automation output | Feeds into |
| --- | --- |
| `level` | Course-ratio recommendation (VLOOKUP / Notion Relation) |
| Construct scores | Radar chart + Stage Gate starting point |
| `report_url` | Sales follow-up + pre-consulting-interview reading |
| `aid_audit` log | Eight-stage consulting Stage 1 interview data |

Full flow: questionnaire submission → auto-scoring → auto report generation → sales / consultant takeover → interview → customized proposal.
