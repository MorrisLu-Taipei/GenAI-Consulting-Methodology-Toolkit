# Company Profile Questionnaire

> 🌐 中文版本 / Chinese version: [COMPANY_PROFILE_QUESTIONNAIRE.md](COMPANY_PROFILE_QUESTIONNAIRE.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

Converts `02_Course_Design/COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md` into a 35-question fillable form. The output is a **Company Profile Bundle (JSON)** which joins with the maturity questionnaire (`AI_MATURITY_QUESTIONNAIRE.md`) result by `submission_id` for consultant use.

---

## Form Intro

> 35 questions, ~12 minutes. This questionnaire helps us understand your company profile, current systems, and deployment preferences.
> Combined with the AI maturity questionnaire, it produces a customized L1-L5 course-mix recommendation and a deployment-mode recommendation.
> Recommended completer: IT manager or AI Champion. "Unsure" is an acceptable answer for some questions.

---

## Section P: Profile (5 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| P1 | Company name | short text | - |
| P2 | Headcount | radio | <50 / 50-300 / 300-1000 / 1000-5000 / 5000+ |
| P3 | Annual revenue band | radio | <NT$100M / 100M-1B / 1B-5B / 5B+ / undisclosed |
| P4 | Primary industry | radio | manufacturing / hospital / retail / financial / gov / education / logistics / software / pro-services / other |
| P5 | Primary market | multi-select | TW / Greater China / SEA / Japan / Europe / Americas / other |

---

## Section S: Systems Inventory (10 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| S1 | Primary email platform | radio | Gmail Workspace / Microsoft 365 / other |
| S2 | Primary document / Wiki platform | multi-select | Notion / Confluence / Google Drive / SharePoint / self-built |
| S3 | Primary CRM | radio | Salesforce / HubSpot / Zoho / Dynamics / self-built / none |
| S4 | Primary ERP | radio | SAP / Oracle / SAP B1 / Dynamics / Workday / DigiWin / self-built / none |
| S5 | Primary HR system | radio | Workday / SAP SuccessFactors / 1111 / 104 / Notion / self-built |
| S6 | Primary customer-service system | radio | Zendesk / Freshdesk / Intercom / self-built / none |
| S7 | Primary analytics / BI platform | multi-select | Looker / Tableau / Power BI / Metabase / self-built / none |
| S8 | Does the company have a self-built API gateway | radio | yes / partial / no |
| S9 | Does the company have SSO (OIDC / SAML) | radio | yes / planned / no |
| S10 | Does the company use GitHub / GitLab | radio | enterprise / SaaS / no |

> Skip logic: P4 = "manufacturing" → extra questions S-Mfg-1 (MES?) / S-Mfg-2 (SPC?) / S-Mfg-3 (WMS?)
> P4 = "hospital" → S-Hsp-1 (HIS / EMR / LIS / PACS yes/no per system)

---

## Section R: Data & Risk (5 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| R1 | Types of sensitive data (multi-select) | multi | PII / medical records / financial / contracts / trade secrets / industrial design / defense / none |
| R2 | Subject to which regulations | multi | EU GDPR / personal data law / HIPAA / SOX / ISO 27001 / FSC / Ministry of Health / military spec / none |
| R3 | Any security incident in the past 24 months | radio | yes (major) / yes (minor) / no / prefer not to disclose |
| R4 | Has the company deployed DLP | radio | yes / partial / no |
| R5 | Attitude toward LLM-vendor data retention | radio | reject / 30 days acceptable / 90 days acceptable / no concern |

---

## Section D: Deployment Preference (5 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| D1 | Overall AI deployment preference | radio | cloud-AI-first / Hybrid / fully on-prem |
| D2 | Existing GPU machine room | radio | A100/H100 class / 4090/L40 class / none / unsure |
| D3 | Willing to use OpenAI / Anthropic / Google APIs | multi | OpenAI / Anthropic / Google / Azure OpenAI / Mistral / unwilling |
| D4 | Plan to deploy on-prem LLM within 12 months | radio | yes / evaluating / no |
| D5 | Acceptance of open-source models (Llama / Qwen / DeepSeek) | radio | high / medium / low |

---

## Section C: Course Audience (5 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| C1 | Expected L1 course headcount | number | - |
| C2 | Expected seed-team (L2-L4 advanced) headcount | number | - |
| C3 | Primary course objectives (top 2) | multi (max 2) | org-wide enablement / workflow automation / Agent building / Agent Team / governance establishment |
| C4 | Preferred course cadence | radio | bootcamp (consecutive) / weekly (half-day per week) / monthly (one day per month) |
| C5 | Need train-the-trainer | radio | yes / evaluating / no |

---

## Section B: Budget & Timeline (5 questions)

| # | Q | Type | Options |
| --- | --- | --- | --- |
| B1 | 12-month budget band | radio | <100K / 100-500K / 500K-2M / 2M-10M / 10M+ NT$ |
| B2 | Desired kickoff time | radio | within 1 month / 1-3 months / 3-6 months / > 6 months |
| B3 | Desired time to first PoC | radio | < 1 month / 1-3 months / 3-6 months / > 6 months |
| B4 | Internal project owner | radio | already assigned / planned / need consultant help to identify |
| B5 | Preference: "full rollout" vs "single PoC" | radio | full / single PoC first then expand / unsure |

---

## Output: Company Profile Bundle (JSON)

After completion, the following JSON is automatically assembled and matched to the maturity questionnaire's `submission_id`:

```json
{
  "submission_id": "0f4a-8bd1-...",
  "filled_at": "2026-05-14T10:23:00Z",
  "profile": {
    "company": "Acme Corp",
    "headcount_bucket": "300-1000",
    "revenue_bucket": "1B-5B",
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
    "industry_specific": { "mes": true, "spc": true, "wms": false }
  },
  "risk": {
    "sensitive_data": ["PII", "industrial design"],
    "regulations": ["personal data law", "ISO 27001"],
    "incidents_24m": "minor",
    "dlp": "partial",
    "llm_retention_acceptance": "30d"
  },
  "deployment": {
    "preference": "Hybrid",
    "gpu_capacity": "L40 class",
    "vendor_acceptance": ["Azure OpenAI", "Mistral"],
    "local_llm_plan": "evaluating",
    "open_source_acceptance": "medium"
  },
  "course": {
    "l1_headcount": 320,
    "seed_team_headcount": 12,
    "objectives": ["workflow automation", "Agent building"],
    "cadence": "weekly",
    "train_the_trainer": "evaluating"
  },
  "budget": {
    "annual_bucket": "2M-10M",
    "kickoff": "1-3 months",
    "first_poc": "1-3 months",
    "owner_status": "already assigned",
    "scope_preference": "single PoC first then expand"
  }
}
```

---

## Derivation Rules

The Bundle automatically derives three recommendations:

### 1. Deployment Recommendation

```
if risk.regulations contains ["HIPAA","military spec","FSC"] OR sensitive_data contains ["medical records","defense"]:
    → fully on-prem
elif risk.regulations contains ["personal data law","SOX"] AND llm_retention_acceptance != "no concern":
    → Hybrid
else:
    → cloud-AI-first
```

### 2. Course Ratio Adjustment

After the maturity questionnaire produces a level, fine-tune by profile:
- If industry is "manufacturing" / "hospital" / "financial" → L1 ratio +10% (governance priority)
- If course.objectives includes "Agent building" → L4 ratio +10%
- If course.objectives includes "Agent Team" → L5 ratio +10%
- If budget.bucket = "<100K" → shift L4-L5 ratio toward L1-L3

### 3. PoC Scenario Suggestion

Map `systems` to `POC_SCENARIO_SPECS.md`:
- If CRM present → recommend C-1, C-2, C-3
- If ERP present → recommend E-1, E-2, E-5
- If wiki includes Notion → recommend N-1, N-2, N-5
- If industry = "hospital" → patient service + medical-record summary combination

---

## Integration with the Consulting Flow

| Output | Feeds into |
| --- | --- |
| `profile.industry` + `profile.headcount` | Stage 3 Industry Benchmark selection |
| `systems` | Stage 1.3 Systems Inventory pre-fill |
| `risk` | Stage 8 governance / compliance recommendations |
| `deployment` | Stage 7 Solution Architecture variant selection |
| `course` | Stage 6 Roadmap course scheduling |
| `budget` | Stage 6 Roadmap phase division |

Full automation schema: `AI_DIAGNOSIS_SHEETS_SCHEMA.md`.
