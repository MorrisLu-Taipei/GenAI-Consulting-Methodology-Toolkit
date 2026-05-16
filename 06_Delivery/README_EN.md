# 06 Delivery — Delivery Acceptance & Engagement Operations

> 🌐 中文版本 / Chinese version: [README.md](README.md)

## 1. Purpose of This Directory

This directory has two layers, which together solve one thing: **how to professionally and scalably "turn a consulting engagement into a business" and "deliver it."**

- **Delivery & acceptance layer**: defines what this program delivers to the client, how it is accepted, and which evidence proves completion.
- **Engagement operations layer**: defines the entire engagement lifecycle (Sales → Delivery → Support), role SOPs, business document templates, operations checklists, and pricing & risk management.

`01`-`03` are "what the consultant does" (the methodology); `05` is "how to make the client want to buy" (pre-sales); this directory is "**after signing, how to run the whole engagement as a business — completely, cleanly, and repeatably.**" The problem it solves: **a consulting firm with only a methodology and no operations framework will be dragged down by scope creep, suffer handoff gaps, have security incidents, and be unable to scale.**

Who uses this directory: project managers, consultants, sales (Closers), technical leads, client-side Owners.

## 2. Position in the Methodology

| Axis | Mapping |
| --- | --- |
| Three-phase service flow | **Deliver** + the operations wrapper that packages all three phases into a "business" |
| Eight-stage consulting structure | Maps to the **delivery and acceptance** of the eight stages; the engagement lifecycle is the "commercial shell" of the eight stages |
| **3-phase contract model (consulting closed-loop)** | **Phase A Diagnosis 2W → Phase B Strategy 4W → Phase C Implementation 24M + quarterly radar review** — the Delivery part of the engagement lifecycle IS the Phase A→B→C closed-loop |
| L1-L5 maturity | The delivery package and acceptance cover the deliverables of each level L1-L5 (the scale axis L1-L3 = implemented & verified; the AI-autonomy axis L4-L5 = framework + guidance) |
| Engagement lifecycle | **This directory IS the body of the engagement lifecycle (Sales → Delivery → Support)** |

> 🔁 **Engagement lifecycle ↔ consulting closed-loop**: the "Delivery" phase here is **not a 6-week marathon** — it is the **closed-loop** described in [`../03_Consulting_Report/README_EN.md`](../03_Consulting_Report/README_EN.md) §4 and [`../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) §6: Phase A mid-term assessment signed → Gate A → Phase B full report → Gate B → Phase C 24-month implementation + **quarterly radar review** (the falsification mechanism of scientific management). The Support phase corresponds to Retainer / Maintenance after Phase C.

## 3. Goals & Benefits

| Goal | Benefit |
| --- | --- |
| A clear delivery package and acceptance criteria | The client and consultant agree on "is it done," no dispute |
| A complete engagement lifecycle | There is an SOP from lead to closeout, not personal craft |
| Role SOPs | Scalable (not one person doing everything), no handoff gaps |
| Business document templates | SOW/contract/invoice/change order ready-made, not rewritten each time |
| Operations checklists | Pre-project/security/QA/handover/offboarding — nothing missed |
| Pricing and risk framework | Not eaten by scope creep; knowing when to say "no" |

**If you skip this directory**: the methodology is strong but the business can't scale — scope creep, unpaid work, handoff gaps, security incidents, key-person dependency, bad debt.

## 4. Usage Flow & Logic

```text
Engagement lifecycle (ENGAGEMENT_LIFECYCLE):
  Sales (Lead → Discovery → Proposal → Contract)
     → use BUSINESS_DOCUMENT_TEMPLATES (proposal, SOW)
     → use PRICING_AND_RISK (pricing, risk register)
  Delivery (Kickoff → Build → Test → Security → Handover)
     → use DELIVERY_CHECKLISTS (pre-project / security / QA / handover)
     → use DELIVERY_PACKAGE_AND_ACCEPTANCE (delivery-package acceptance)
     → use DELIVERY_ROLE_SOPS (who owns which segment)
  Support (Retainer → Maintenance → Offboarding)
     → use DELIVERY_CHECKLISTS (offboarding)
Throughout: the 7 Pillars are the baseline principles
```

| Step | Who | When | Input | Output |
| --- | --- | --- | --- | --- |
| Run the lifecycle | PM | Throughout the engagement | `ENGAGEMENT_LIFECYCLE` | Each phase advanced |
| Produce business documents | Closer / PM | Sales / on change | `BUSINESS_DOCUMENT_TEMPLATES` | Proposal / SOW / change order |
| Price and assess risk | Closer / PM | Proposal / Kickoff | `PRICING_AND_RISK` | Quote + risk register |
| Run the checklists | PM / Technical Lead | Each delivery phase | `DELIVERY_CHECKLISTS` | Each phase's checks passed |
| Delivery acceptance | PM + client | Handover | `DELIVERY_PACKAGE_AND_ACCEPTANCE` | Client sign-off |
| Role division | Whole team | Throughout | `DELIVERY_ROLE_SOPS` | Clear responsibility and handoffs |

> Logic: `ENGAGEMENT_LIFECYCLE` is the trunk (the lifecycle); the other 5 files are the tools for each phase of the trunk — document templates, pricing & risk, checklists, role SOPs, delivery acceptance. The **7 Pillars** (client hosts, client pays, security first, test thoroughly, document fully, clean handover, clear scope) run throughout.

## 5. File Descriptions

### Delivery & acceptance layer

| File | Purpose |
| --- | --- |
| `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` | The delivery-package list and item-by-item acceptance table for the AI maturity diagnosis, L1-L5 courses, L4 Hermes Agent, and the eight-stage consulting diagnostic report. Its §1.1 states the public-honest delivery scope: L1-L3 is implemented & verified delivery; L4-L5 is framework + consulting guidance, client-built. |

### Engagement operations layer (adapted from Mirza Iqbal / next8n.com's Workflow Automation Delivery Framework, MIT, generalized to the L1-L5 AI transformation consulting context; citation in `../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`)

| File | Purpose |
| --- | --- |
| `ENGAGEMENT_LIFECYCLE.md` | The three-phase engagement lifecycle (Sales → Delivery → Support), each phase's sub-phases and outputs, the 7 Pillars, the lifecycle × eight-stage mapping, and the pre-engagement checklist for starting every project. |
| `DELIVERY_ROLE_SOPS.md` | SOPs for 7 delivery roles (Lead Gen / Sales Rep / Closer / PM / Technical Lead / Developer / Client) — each role's responsibilities, key deliverables, handoff points, collaborators, and lifecycle phase — plus the role × lifecycle matrix and the handoff golden rules. |
| `BUSINESS_DOCUMENT_TEMPLATES.md` | 8 business document templates: proposal, SOW, MSA outline, change order, invoice, handover document, retainer agreement, key emails. **With a legal disclaimer — the template skeletons are not legal documents and must be reviewed by legal counsel.** |
| `DELIVERY_CHECKLISTS.md` | 5 operations checklists: pre-project, security, QA, handover, offboarding; with an explanation of the difference from the methodology's Stage Gates. |
| `PRICING_AND_RISK.md` | The two separation principles of pricing, 4 pricing models, the tiered product line, common engagement risks and mitigations, when to say "no," and the incident-response process. |

### `*_EN.md`

The English-version siblings of the files above.

## 6. Mapping to Other Directories

| Directory | Relationship to this directory | Data flow |
| --- | --- | --- |
| `01_Assessment` | Diagnosis maps to the Sales phase of the engagement lifecycle | `01` ↔ `06` Sales |
| `02_Course_Design` | In-class outputs go into the delivery-package acceptance | `02` output → `06` acceptance |
| `03_Consulting_Report` | The consulting report is the core deliverable of the delivery package | `03` report → `06` acceptance |
| `05_Sales` | The deck's pricing/tiering maps to the engagement lifecycle and pricing | `05` deck ↔ `06` pricing |
| `00_Overview` | The engagement lifecycle is the wrapper that turns the storyline into a business | `00` story → `06` operations |
| `90_References` | Third-party citation for the engagement operations layer (Mirza Iqbal framework) | `90` citation → `06` |

## 7. Common Usage Scenarios

- **A new engagement comes in**: the PM uses the "pre-engagement checklist" in `ENGAGEMENT_LIFECYCLE.md` to confirm readiness, and `DELIVERY_ROLE_SOPS.md` to assign roles.
- **About to sign**: the Closer uses the SOW template in `BUSINESS_DOCUMENT_TEMPLATES.md` (in/out of scope spelled out), and `PRICING_AND_RISK.md` to price.
- **Each delivery phase**: run the pre-project / security / QA / handover checklists against `DELIVERY_CHECKLISTS.md`.
- **Delivering to the client**: use `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` for item-by-item acceptance + the handover document in `BUSINESS_DOCUMENT_TEMPLATES.md`.
- **Client keeps adding requirements**: use the scope-creep mitigation in `PRICING_AND_RISK.md` + the change order in `BUSINESS_DOCUMENT_TEMPLATES.md`.
- **Closeout**: run the offboarding checklist in `DELIVERY_CHECKLISTS.md`.

---

## ⭐ Cross-Topic Quick References: 5 Core Themes, Where to Find Them

The whole methodology has 5 main arteries running through every directory. How this directory connects to each:

| Cross-Topic | Primary location | How this directory connects |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + three-engine co-reading** | Root [`README_EN.md`](../README_EN.md) §🌟 ｜ [`AI_NATIVE_LIVING_BOOK_EN.md`](../00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | Engagements can mobilize the three engines: Antigravity for client meetings / Codex for SOW & report-draft audit / Claude Code for Phase B simulation and multi-perspective review |
| 🎓 **Academic foundation (7 pillars)** | [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | The "security-first / HITL" of the 7 Pillars maps to Sociotechnical Systems & Trust (Bostrom / Dietvorst / Glikson); scope creep / level-jumping failures map to Real Options + Absorptive Capacity failure patterns |
| 📚 **L1-L5 course education** | [`../02_Course_Design/`](../02_Course_Design/) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md) | The delivery package and acceptance cover verifiable deliverables of every L1-L5 level; in-class outputs flow into [`DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](DELIVERY_PACKAGE_AND_ACCEPTANCE.md) for item-by-item acceptance |
| 🔁 **Consulting / 8 stages + Phase A→B→C closed-loop** | [`EIGHT_STAGE_FLOW_STORY_EN.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **This directory IS the "commercial shell" of the consulting closed-loop** — engagement lifecycle Sales→Delivery→Support corresponds to Phase A→B→C + quarterly radar review |
| 📖 **References / acknowledgments** | [`../90_References/`](../90_References/) §2 acknowledgments | The engagement-operations layer cites Mirza Iqbal / next8n.com's Workflow Delivery Framework (MIT); see [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE_EN.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE_EN.md) |
