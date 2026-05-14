# 01 Assessment — AI Maturity Diagnosis

> 🌐 中文版本 / Chinese version: [README.md](README.md)

## 1. Purpose of This Directory

This directory is the **first phase of the three-phase service flow: Diagnose**. It solves the most fundamental problem a consultant faces when taking on an engagement: **"The enterprise says it 'is using AI' — but which level is it actually at? What is missing? Where should it start filling gaps?"**

Without an objective diagnosis, a consultant can only configure courses from the client's subjective description — the result is often skipping levels (the client wants L4 Agents without even having company-wide L1 usage) or misplaced focus (governance is missing, but tools keep getting added). This directory uses three questionnaire lengths + a scoring model + a company-profile survey to turn "a vague feeling" into an **objective, quantifiable, comparable L1-L5 score and a six-dimension gap chart**.

Who uses this directory: sales (the 10-item version for development-stage screening), consultants (the 25/50-item versions for pre-course and pre-interview inventory), IT/AI Champion (fills out the company-profile questionnaire).

## 2. Position in the Methodology

| Axis | Mapping |
| --- | --- |
| Three-phase service flow | **Diagnose** — the first phase |
| Eight-stage consulting structure | **Stage 1 Current-State Grasp** (the diagnostic result is Stage 1's core input) |
| L1-L5 maturity | This directory is the tool that "**determines which level the client is at**" — on the scale axis (L1-L3, human-supervised) and the AI-autonomy axis (L4-L5, AI-autonomous) |
| Engagement lifecycle | **Sales — Lead Qualification (10-item version) / Discovery (25/50-item versions)** |

## 3. Goals & Benefits

| Goal | Benefit |
| --- | --- |
| Replace subjective guesswork with an objective score | Consultants configure courses on a basis, not a hunch |
| Identify the six-dimension gaps (tool / knowledge / process / integration / Agent / governance & ROI) | Know where the client is strong and where weak |
| Directly derive three recommendations | Course ratio + deployment mode + PoC scenarios, all at once |
| Three questionnaire lengths map to three sales stages | Sales development, pre-course, and pre-interview each have a fitting tool |
| Automatable | Questionnaire → scoring → report is fully automated; the consultant only interprets |

**If you skip this directory**: the course ratio is a guess, client expectations cannot be managed (pointing at an L5 case saying "I want this" without knowing they're at L2), and the consulting report has no objective starting point.

## 4. Usage Flow & Logic

```text
10-item quick questionnaire (sales development, 3 min)
   → Qualify the lead + preliminary L-level position
25-item questionnaire (pre-course, 8 min, filled by client managers)
   → Six-dimension scores + radar chart
50-item questionnaire (pre-consulting-interview, 20 min, filled by IT/AI Champion)
   → Full inventory + open questions
Company-profile questionnaire (35 items)
   → JSON Profile Bundle (systems / risk / deployment preference / budget)
        ↓ merge
   Auto-scoring → L1-L5 level + six-dimension radar
        ↓ derive
   (1) recommended course ratio  (2) recommended deployment mode  (3) recommended PoC scenarios
```

| Step | Who | When | Input | Output |
| --- | --- | --- | --- | --- |
| 10-item quick screen | Sales | Lead development stage | A prospect | Qualification + preliminary L-level |
| 25-item pre-course diagnostic | Client's manager group | 1 week before the L1 course | 25-item questionnaire | Six-dimension scores |
| 50-item full inventory | Client IT / AI Champion | Before the consulting interview | 50 items + company-profile questionnaire | Complete Profile Bundle |
| Auto-scoring | The system (Sheets/Notion/n8n) | After questionnaire submission | Questionnaire answers | L-level + radar + three recommendations |
| Interpretation | Consultant | After receiving the auto report | The auto report | Customized proposal direction |

> Logic: the questionnaire is only the **input**; the real output is "**L-level + six-dimension gaps + three recommendations**." These three feed, respectively — course ratio → `02_Course_Design`; deployment mode → `03`'s Solution Architecture; PoC scenarios → `04_Scenarios`'s case index. Diagnosis is not the endpoint — it is the switch that "lights up" the next three directories.

## 5. File Descriptions

### `AI_MATURITY_QUESTIONNAIRE.md`

The AI maturity questionnaire itself, in three lengths: 10 / 25 / 50 items. The 10-item version is for sales to quickly determine; the 25-item version has 4-5 items per dimension, for pre-course; the 50-item version adds deployment mode and system inventory, for pre-consulting-interview. All three share the 0-4 scale and the six-dimension structure. **Rewritten in plain language** with a glossary and 0/2/4 scenario anchors so non-technical respondents can fill it out.

### `AI_MATURITY_SCORING_MODEL.md`

The scoring logic and determination rules. Includes: the scoring method for the six dimensions (tool usage, knowledge consolidation, process standardization, system integration, Agent application, governance & ROI), the total-score thresholds mapping to L1-L5, the **primary maturity vs. local maturity** judgment (why a department can be locally L4 while the company is overall L2), and the recommendation rules for deployment mode and course ratio. Also defines the L1-L5 **two-axis model** (scale axis L1-L3, AI-autonomy axis L4-L5).

### `AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`

The Definition of Done, Deliverables, Evidence, Owner, acceptance gate (Stage Gate), Fail Condition, and Next Level Entry Criteria for each L1-L5 stage. It defines "what 'done' looks like at each level and what evidence proves it" — the basis for acceptance-gate verification.

### `FILLABLE_QUESTIONNAIRE.md`

The rendering spec turning the 10/25/50 items into fillable forms — question types (radio / 0-4 scale / multi-select / short answer), page segmentation, skip logic, the submit page and the "what happens next" page — with rendering hints for the Google Form / Tally / Notion Form platforms. Every question carries plain-language help text.

### `COMPANY_PROFILE_QUESTIONNAIRE.md`

A 35-item company-profile questionnaire in 6 sections (Profile / Systems / Risk / Deployment / Course / Budget). It outputs a JSON Profile Bundle and includes **derivation rules**: from the Bundle, automatically derive the deployment-mode recommendation, course-ratio fine-tuning, and PoC scenario recommendations. It links to the maturity questionnaire via `submission_id`.

### `AI_DIAGNOSIS_SHEETS_SCHEMA.md`

The implementation schema that automates the whole diagnosis. Three platforms: Google Sheets (scoring formulas, conditional formatting, Apps Script), Notion (4 database structures and formulas), n8n (a 13-node automated diagnosis flow with idempotency). It makes questionnaire → scoring → report generation → consultant notification fully automated.

### `*_EN.md`

The English-version siblings of the files above.

## 6. Mapping to Other Directories

| Directory | Relationship to this directory | Data flow |
| --- | --- | --- |
| `00_Overview` | Diagnosis is the first phase of the storyline | `00` story → `01` realization |
| `02_Course_Design` | The diagnosis's "L-level + course ratio" directly determines the course configuration | `01` course ratio → `02` course configuration |
| `03_Consulting_Report` | The diagnostic result is the input to eight-stage Stage 1; the report cites the diagnostic scores and radar | `01` scores → `03` report |
| `04_Scenarios` | After diagnosis, use `LLM_APPS_CASE_INDEX.md` by L-level to pick PoC candidates | `01` L-level → `04` case filtering |
| `06_Delivery` | Diagnosis maps to the Sales phase of the engagement lifecycle | `01` ↔ `06` Sales phase |
| `90_References` | The methodological basis of the scoring model | `90` basis → `01` |

## 7. Common Usage Scenarios

- **Sales development**: a prospect fills out the 10-item version → auto report within 24 hours → sales goes to the meeting with the L-level position in hand.
- **Pre-course preparation**: send the 25-item version to the client's manager group 1 week before the course → the consultant gets the six-dimension radar and adjusts the course ratio.
- **Before the consulting interview**: IT/AI Champion fills out the 50 items + company-profile questionnaire → the consultant receives the complete Profile Bundle as a brief 1 hour before the interview.
- **To scale**: use `AI_DIAGNOSIS_SHEETS_SCHEMA.md` to deploy the automated diagnosis flow in the client's n8n; the consultant only does the final interpretation.
