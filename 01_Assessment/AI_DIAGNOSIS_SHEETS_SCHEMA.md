# AI 診斷自動化欄位設計 / AI Diagnosis Automation Schema

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

本檔提供 AI 成熟度診斷在三個平台的實作 schema：Google Sheets、Notion、n8n。讓問卷填答到自動產生診斷摘要可全程自動化。

Implementation schemas for automating the AI maturity diagnostic across three platforms: Google Sheets, Notion, and n8n.

---

## A. Google Sheets 架構 / Google Sheets Schema

### Sheet 1: `Raw Responses`

| 欄 | 名稱 | 類型 | 範例 |
| --- | --- | --- | --- |
| A | timestamp | datetime | 2026-05-14 10:23:00 |
| B | submission_id | string (UUID) | 0f4a-8bd1-... |
| C | respondent_email | email | ceo@acme.com |
| D | company | string | Acme Corp |
| E | industry | enum | manufacturing / hospital / retail / ... |
| F | size_bucket | enum | <50 / 50-300 / 300-1000 / 1000+ |
| G | role | enum | CEO / COO / IT / dept-head / other |
| H-BG | Q1-Q50 | int 0-4 | 各題分數 |
| BH | language | enum | zh-TW / en |

### Sheet 2: `Scoring`

六大構面（Construct）對應題號：

| Construct | 題號範圍 | 公式（以 25 題版為例） |
| --- | --- | --- |
| 工具使用 Tool Usage | Q1-Q4 | `=AVERAGE(Raw!H2:K2)` |
| 知識沉澱 Knowledge | Q5-Q8 | `=AVERAGE(Raw!L2:O2)` |
| 流程標準化 Process | Q9-Q12 | `=AVERAGE(Raw!P2:S2)` |
| 系統整合 Integration | Q13-Q16 | `=AVERAGE(Raw!T2:W2)` |
| Agent 應用 Agent | Q17-Q20 | `=AVERAGE(Raw!X2:AA2)` |
| 治理 ROI Gov+ROI | Q21-Q25 | `=AVERAGE(Raw!AB2:AF2)` |

**整體分數**：`=AVERAGE(B2:G2)` (六構面平均)

**等級判定**：
```
=IF(H2>=3.5,"L5", IF(H2>=2.8,"L4", IF(H2>=2.0,"L3", IF(H2>=1.2,"L2","L1"))))
```

### Sheet 3: `Radar Data`

每個 submission_id × 6 個構面分數，供 Google Sheets 內建雷達圖使用。

### Sheet 4: `Recommendations`

依等級推薦的課程比例（lookup table）：

| Level | L1 % | L2 % | L3 % | L4 % | L5 % | 重點建議 |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| L1 | 50 | 30 | 20 | 0 | 0 | 先打底 L1 全員使用 |
| L2 | 25 | 40 | 25 | 10 | 0 | Skill 化為主 |
| L3 | 15 | 25 | 40 | 15 | 5 | Workflow PoC 為主 |
| L4 | 10 | 15 | 25 | 35 | 15 | Agent 上線 |
| L5 | 5 | 10 | 20 | 30 | 35 | Agent Team 多領域 |

公式範例：`=VLOOKUP(Scoring!I2, RecLookup!A:G, 2, FALSE)`

### Sheet 5: `Cond Format Rules`

- Score ≥ 3.5 綠色
- 2.0 ≤ Score < 3.5 黃色
- Score < 2.0 紅色

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

## B. Notion 資料庫架構 / Notion Database Schema

### 4 個 Database

**1. `AID_Respondents`** — 受測者主檔
- `email` (Title) · `name` · `company` (Relation → Companies DB) · `role` · `submitted_at`

**2. `AID_Responses`** — 每筆問卷答案
- `submission_id` (Title)
- `respondent` (Relation → AID_Respondents)
- 25 / 50 個 number properties (Q1-Q50)
- `language`
- `version` (10 / 25 / 50 題)
- `submitted_at`

**3. `AID_Scoring`** — 計算結果
- `submission_id` (Title; Relation → AID_Responses)
- 6 個 formula properties — 構面平均：
  ```
  Tool Usage = (prop("Q1") + prop("Q2") + prop("Q3") + prop("Q4")) / 4
  ```
- `overall` (Formula: 六構面平均)
- `level` (Formula): 用巢狀 if，邏輯同 Sheets 版

**4. `AID_Recommendations`** — 等級對應推薦
- `level` (Title: L1-L5)
- L1-L5 比例（%）
- `priority_focus` (text)
- `gates` (text)

### 關鍵 View

- `AID_Responses` 表格 View（filter: submitted_at > 7 days ago）
- `AID_Scoring` Gallery View（依 level 群組）
- `AID_Recommendations` Table View（reference 用）

### 範本頁面：「Diagnostic Report」

每個 submission 對應一個自動產生的子頁，模板包含：
- 公司資訊區
- 六構面雷達（用 Embed Mermaid / external chart）
- 等級判定
- 推薦課程比例
- 推薦優先導入場景
- 下一步行動

---

## C. n8n 自動診斷流程 / n8n Auto-Diagnosis Flow

### 節點序列（13 nodes + Error branch）

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

- 在 Step 2 後新增 Data Table lookup：`SELECT * FROM aid_runs WHERE submission_id = $$submission_id`
- 若存在則 short-circuit 回傳已有結果
- 另開 `POST /aid/replay { submission_id }` webhook 用於重新生成（覆寫舊紀錄）

### 構面計分 Function 範例 (Node 3)

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

### 等級對應 Prompt 模板（Node 5a-5e）

每個 level 的 system prompt 內含：
- 該 level 的能力定義
- 常見阻塞點
- 推薦課程比例
- 30/60/90 天 quick win
- 治理檢核要點

讓 LLM 產出 ~600 字客製化 narrative，附在 email/Notion report 中。

### 部署備註

- 部署在客戶 n8n 實例（推薦 self-host）
- 機敏資料：webhook 應啟用 HMAC signature
- LLM 呼叫：若資料敏感請改為 Azure OpenAI / 地端 Llama
- Audit：每筆呼叫寫入 `aid_audit` Data Table，含 timestamp / level / latency / token usage

---

## D. 串接到課程與顧問流程 / Integration with Course & Consulting Flow

| 自動化輸出 | 串到 |
| --- | --- |
| `level` | 課程比例推薦（VLOOKUP / Notion Relation） |
| 構面分數 | 雷達圖 + Stage Gate 起點 |
| `report_url` | 業務追單 + 顧問訪談前讀物 |
| `aid_audit` log | 八階段顧問 Stage 1 訪談資料 |

完整流程：問卷填寫 → 自動計分 → 自動產生報告 → 業務 / 顧問接手 → 訪談 → 客製化提案。
