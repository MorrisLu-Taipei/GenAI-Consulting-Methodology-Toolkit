# 公司屬性問卷 / Company Profile Questionnaire

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

把 `02_Course_Design/COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md` 內容轉成 35 題可填寫問卷，輸出 **Company Profile Bundle (JSON)** 與成熟度問卷 (`AI_MATURITY_QUESTIONNAIRE.md`) 結果合併供顧問使用。

Converts `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md` into a 35-question fillable form. Output is a **Company Profile Bundle (JSON)** which joins with the maturity questionnaire result (by `submission_id`) for consultant use.

---

## Form Intro

> 共 35 題、約 12 分鐘。本問卷協助我們了解貴公司屬性、系統現況、部署偏好。
> 與 AI 成熟度問卷搭配，可產生客製化的 L1-L5 課程比例建議與部署模式建議。
> 請由 IT 主管或 AI Champion 填寫；若部分題目不確定，可選「不確定」。
>
> 35 questions, ~12 minutes. Helps us understand your company profile, system landscape, and deployment preferences.
> Combined with the maturity questionnaire, produces a customized L1-L5 course-mix and deployment-mode recommendation.
> Recommended completer: IT manager or AI Champion. "Unsure" is acceptable.

---

## Section P：公司基本資料 / Profile (5 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| P1 | 公司名稱 / Company name | short text | - |
| P2 | 員工人數 / Headcount | radio | <50 / 50-300 / 300-1000 / 1000-5000 / 5000+ |
| P3 | 年營收區間 / Annual revenue | radio | <NT$1億 / 1-10億 / 10-50億 / 50億+ / 不揭露 |
| P4 | 主要產業 / Primary industry | radio | manufacturing / hospital / retail / financial / gov / education / logistics / software / pro-services / other |
| P5 | 主要市場 / Primary market | multi-select | TW / Greater China / SEA / Japan / Europe / Americas / other |

---

## Section S：系統現況 / Systems Inventory (10 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| S1 | 主要 email 平台 | radio | Gmail Workspace / Microsoft 365 / 其他 |
| S2 | 主要文件 / Wiki 平台 | multi-select | Notion / Confluence / Google Drive / SharePoint / 自建 |
| S3 | 主要 CRM | radio | Salesforce / HubSpot / Zoho / Dynamics / 自建 / 無 |
| S4 | 主要 ERP | radio | SAP / Oracle / SAP B1 / Dynamics / Workday / 鼎新 / 自建 / 無 |
| S5 | 主要 HR 系統 | radio | Workday / SAP SuccessFactors / 1111 / 104 / Notion / 自建 |
| S6 | 主要客服系統 | radio | Zendesk / Freshdesk / Intercom / 自建 / 無 |
| S7 | 主要分析 / BI 平台 | multi-select | Looker / Tableau / Power BI / Metabase / 自建 / 無 |
| S8 | 公司是否有自建 API gateway | radio | 有 / 部分 / 無 |
| S9 | 公司是否有 SSO (OIDC / SAML) | radio | 有 / 規劃中 / 無 |
| S10 | 公司是否使用 GitHub / GitLab | radio | 有 enterprise / 有 SaaS / 無 |

> Skip logic: P4 = "manufacturing" → 額外題 S-Mfg-1 (是否有 MES) / S-Mfg-2 (是否有 SPC) / S-Mfg-3 (是否有 WMS)
> P4 = "hospital" → S-Hsp-1 (HIS / EMR / LIS / PACS yes/no per system)

---

## Section R：資料屬性與風險 / Data & Risk (5 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| R1 | 機敏資料種類 (multi-select) | multi | PII / 病歷 / 財務 / 合約 / 商業機密 / 工業設計 / 國防 / 無 |
| R2 | 是否受法規監管 | multi | EU GDPR / 個資法 / HIPAA / SOX / ISO 27001 / 金管會 / 衛福部 / 軍規 / 無 |
| R3 | 過去 24 個月是否發生資安事件 | radio | 有 (重大) / 有 (輕微) / 無 / 不便揭露 |
| R4 | 公司是否已導入 DLP | radio | 有 / 部分 / 無 |
| R5 | 對 LLM 廠商資料保留之態度 | radio | 拒絕 / 30 天可接受 / 90 天可接受 / 無所謂 |

---

## Section D：部署模式偏好 / Deployment Preference (5 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| D1 | 整體 AI 部署偏好 | radio | 雲 AI 為主 / Hybrid / 全地端 |
| D2 | 是否已有 GPU 機房 | radio | A100/H100 級 / 4090/L40 級 / 無 / 不確定 |
| D3 | 是否願意使用 OpenAI / Anthropic / Google API | multi | OpenAI / Anthropic / Google / Azure OpenAI / Mistral / 不願 |
| D4 | 是否計畫 12 個月內導入地端 LLM | radio | 是 / 評估中 / 否 |
| D5 | 對 Llama / Qwen / DeepSeek 等開源模型接受度 | radio | 高 / 中 / 低 |

---

## Section C：課程對象與目標 / Course Audience (5 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| C1 | 預計參與 L1 課程人數 | number | - |
| C2 | 預計種子團隊 (L2-L4 進階) 人數 | number | - |
| C3 | 主要課程目的 (top 2) | multi (max 2) | 全員啟用 / 流程自動化 / Agent 建置 / Agent Team / 治理建立 |
| C4 | 期望課程節奏 | radio | 集中營 (連續) / 週次 (每週半天) / 月次 (每月一天) |
| C5 | 是否需要 Train-the-Trainer | radio | 是 / 評估中 / 否 |

---

## Section B：預算與時程 / Budget & Timeline (5 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| B1 | 12 個月預算區間 | radio | <100K / 100-500K / 500K-2M / 2M-10M / 10M+ NT$ |
| B2 | 期望啟動時間 | radio | 1 個月內 / 1-3 個月 / 3-6 個月 / > 6 個月 |
| B3 | 期望完成首個 PoC 時間 | radio | < 1 月 / 1-3 月 / 3-6 月 / > 6 月 |
| B4 | 內部專案 owner | radio | 已有 / 規劃中 / 需顧問協助指認 |
| B5 | 對「整套導入」vs「單點 PoC」偏好 | radio | 整套 / 先單點再擴展 / 不確定 |

---

## Output: Company Profile Bundle (JSON)

填寫完成後，自動組成下列 JSON，與成熟度問卷之 `submission_id` 對應：

```json
{
  "submission_id": "0f4a-8bd1-...",
  "filled_at": "2026-05-14T10:23:00Z",
  "profile": {
    "company": "Acme Corp",
    "headcount_bucket": "300-1000",
    "revenue_bucket": "10-50億",
    "industry": "manufacturing",
    "markets": ["TW", "SEA"]
  },
  "systems": {
    "email": "Microsoft 365",
    "wiki": ["Confluence", "SharePoint"],
    "crm": "Salesforce",
    "erp": "SAP",
    "hr": "Workday",
    "support": "Zendesk",
    "analytics": ["Power BI"],
    "api_gateway": "partial",
    "sso": "yes",
    "git": "GitHub Enterprise",
    "industry_specific": {
      "mes": true,
      "spc": true,
      "wms": false
    }
  },
  "risk": {
    "sensitive_data": ["PII", "工業設計"],
    "regulations": ["個資法", "ISO 27001"],
    "incidents_24m": "minor",
    "dlp": "partial",
    "llm_retention_acceptance": "30d"
  },
  "deployment": {
    "preference": "Hybrid",
    "gpu_capacity": "L40 級",
    "vendor_acceptance": ["Azure OpenAI", "Mistral"],
    "local_llm_plan": "evaluating",
    "open_source_acceptance": "中"
  },
  "course": {
    "l1_headcount": 320,
    "seed_team_headcount": 12,
    "objectives": ["流程自動化", "Agent 建置"],
    "cadence": "週次",
    "train_the_trainer": "evaluating"
  },
  "budget": {
    "annual_bucket": "2M-10M",
    "kickoff": "1-3 個月",
    "first_poc": "1-3 月",
    "owner_status": "已有",
    "scope_preference": "先單點再擴展"
  }
}
```

---

## 推導規則 / Derivation Rules

由 Bundle 自動推導三項建議：

### 1. 部署模式建議 / Deployment Recommendation

```
if risk.regulations contains ["HIPAA","軍規","金管會"] OR sensitive_data contains ["病歷","國防"]:
    → 全地端
elif risk.regulations contains ["個資法","SOX"] AND llm_retention_acceptance != "無所謂":
    → Hybrid
else:
    → 雲 AI 為主
```

### 2. 課程比例調整 / Course Ratio Adjustment

成熟度問卷得 level 後，依 profile 微調：
- 若 industry 為 "manufacturing" / "hospital" / "financial" → L1 比例 +10%（治理優先）
- 若 course.objectives 含 "Agent 建置" → L4 比例 +10%
- 若 course.objectives 含 "Agent Team" → L5 比例 +10%
- 若 budget.bucket = "<100K" → L4-L5 比例移到 L1-L3

### 3. PoC 場景建議 / PoC Scenario Suggestion

依 systems 對應 `POC_SCENARIO_SPECS.md`：
- 若 crm 有 → 推薦 C-1, C-2, C-3
- 若 erp 有 → 推薦 E-1, E-2, E-5
- 若 wiki 含 Notion → 推薦 N-1, N-2, N-5
- 若 industry = "hospital" → 病患服務 + 病歷摘要組合

---

## 串接到顧問流程 / Integration with Consulting Flow

| Output | 串到 |
| --- | --- |
| `profile.industry` + `profile.headcount` | Stage 3 Best Practice Integration 標竿選擇 |
| `systems` | Stage 1.3 Systems Inventory 預填 |
| `risk` | Stage 8 治理 / 法遵建議 |
| `deployment` | Stage 7 To-Be Design variant 選擇 |
| `course` | Stage 6 Benchmarking & Phased Goals 課程排程 |
| `budget` | Stage 6 Benchmarking & Phased Goals 階段切分 |

完整自動化 schema：`AI_DIAGNOSIS_SHEETS_SCHEMA.md`。
