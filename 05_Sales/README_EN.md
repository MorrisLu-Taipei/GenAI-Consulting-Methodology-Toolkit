# 05 Sales — Outbound Sales Material

> 🌐 Language: [繁體中文](README.md) ｜ English ｜ [Deutsch](README_DE.md) ｜ [Français](README_FR.md) ｜ [Español](README_ES.md) ｜ [日本語](README_JA.md) ｜ [한국어](README_KR.md)

## 1. Purpose of This Directory

This directory is the first block of turning the methodology into a **business**: **outbound sales material**.

`01`-`03` are the consulting methodology itself (strong, but "strong" does not turn itself into engagements); this directory solves the problem: **before a prospect has even entered the diagnostic flow, how does sales make them "want to buy"?** This directory provides everything from a one-page DM, three deck outlines of different lengths, visual-asset specs, to a 20-question sales FAQ — so sales has ready-made, consistent, professional material at every stage of lead development, proposal, and objection handling.

It maps to the **Sales phase** of the engagement lifecycle: bringing a cold lead all the way to "willing to fill out the questionnaire, willing to enter diagnosis."

Who uses this directory: sales (Lead Gen / Sales Rep / Closer), consultants (giving a methodology intro to client executives), designers (producing actual visual files per the visual specs).

## 2. Position in the Methodology

| Axis | Mapping |
| --- | --- |
| Three-phase service flow | **The "pre-sales" before diagnosis** — bringing the client to the point of willing to enter diagnosis |
| Eight-stage consulting structure | Does not map to the eight stages (the eight stages are post-contract) |
| L1-L5 maturity | The sales material uses the L1-L5 model as a selling point |
| Engagement lifecycle | **Sales — Lead Qualification / Discovery / Proposal** |

## 3. Goals & Benefits

| Goal | Benefit |
| --- | --- |
| Consistent, professional outbound material | Different salespeople present the methodology consistently; a professional brand |
| Three deck lengths for different occasions | 10-page for executives, 20-page standard, 30-page methodology — each fits its use |
| 20-question sales FAQ | Sales has standard answers to objections instead of improvising |
| Visual-asset specs | Designers have a clear brief and produce consistent visual assets |
| A one-page DM | A professional leave-behind from the very first contact |

**If you skip this directory**: every salesperson makes their own slides, presents the methodology inconsistently, handles objections by improvising, and the client's first impression of the methodology is scattered.

## 4. Usage Flow & Logic

```text
Lead development
   → ONE_PAGER_OUTLINE (one-page DM, the leave-behind for first contact)
First formal meeting
   → EXECUTIVE_DECK_OUTLINE (10-page executive version, builds urgency and methodology credibility)
Deeper proposal
   → STANDARD_SALES_DECK_OUTLINE (20-page, for department heads/IT/HR)
   → CONSULTING_METHODOLOGY_DECK_OUTLINE (30-page, methodology depth, for CIO/strategy chief/academic peers)
Objection handling (throughout)
   → SALES_FAQ (20 standard Q&As)
Produce actual visuals
   → VISUAL_ASSETS_SPEC (designers produce PNG/SVG/print files per the spec)
```

| Step | Who | When | Input | Output |
| --- | --- | --- | --- | --- |
| Send the one-page DM | Sales (Lead Gen) | Lead development | one-pager | Client's initial awareness |
| Executive intro | Sales / consultant | First meeting | 10-page deck | Client willing to talk further |
| Deeper proposal | Closer | Proposal stage | 20/30-page deck | Client willing to sign the SOW |
| Handle objections | Sales / Closer | Throughout | SALES_FAQ | Client's doubts dispelled |
| Produce visuals | Designer | Material production period | VISUAL_ASSETS_SPEC | Actual visual files |

> Logic: material goes **shallow to deep** — one-pager (spark interest) → 10-page (build urgency) → 20/30-page (deeper persuasion) → FAQ (dispel doubts). Each one points to the same next step: "fill out the 10-question questionnaire, enter the `01_Assessment` diagnosis."

## 5. File Descriptions

### `SALES_VALUE_PROPOSITION.md`

Role-based value propositions and sales talking points. Writes a corresponding value proposition for the pain points of CEO / COO / CIO / IT / HR / department heads, and includes 30-second / 3-minute / 10-minute sales pitches plus common objections.

### `SALES_FAQ.md`

20 outbound sales FAQs. The questions clients most often ask (differences from the Big 4, pricing structure, timeline, customization, cloud/on-premises, security, ROI, IP, AI model selection, failure handling…), each with a 2-4 sentence standard answer, in both Chinese and English.

### `ONE_PAGER_OUTLINE.md`

The content draft and layout brief for a one-page PDF / print piece (about 600 words). Includes the Hero tagline, three pain points, the three-phase flow, the L1-L5 map, verifiable deliverables, three industry fits, an ROI proof point, the CTA, and layout/color/font recommendations for the designer.

### `EXECUTIVE_DECK_OUTLINE.md`

A 10-page executive deck outline. Audience: CEO/COO/CIO/CTO. Each page includes a title, key message, content, visual recommendation, and speaker notes. Covers vision, urgency, methodology, L1-L5, the story arc, ROI, governance, competitive differentiation, pricing, and next steps.

### `STANDARD_SALES_DECK_OUTLINE.md`

A 20-page standard sales deck outline. Audience: department heads, PMs, IT Leads, HR, AI Champions. Broader than the 10-page version; includes course teasers for each level, PoC scenarios, Stage Gate, the delivery package, and the three-phase kickoff.

### `CONSULTING_METHODOLOGY_DECK_OUTLINE.md`

A 30-page consulting methodology deck outline. Audience: CIOs, strategy chiefs, large-enterprise digital-transformation offices, academic peers. The methodology-depth version — the eight stages, L1-L5's layered linkage, the scoring model, case excerpts, governance, and the academic roots (Prof. Michael Rosemann, QUT).

### `VISUAL_ASSETS_SPEC.md`

ASCII specs and designer briefs for 3 outbound visual assets: the three-phase service flow diagram, the L1-L5 maturity map, and the verifiable-deliverables list visual. Each includes the ASCII spec, layout alternatives, and color/font/size/accessibility requirements.

### `*_EN.md`

The English-version siblings of the files above.

## 6. Mapping to Other Directories

| Directory | Relationship to this directory | Data flow |
| --- | --- | --- |
| `00_Overview` | The story skeleton of the sales material comes from the storyline | `00` story → `05` material |
| `01_Assessment` | All sales material points to "fill the questionnaire, enter diagnosis" | `05` → drives traffic to `01` |
| `02_Course_Design` | The course teasers in the decks come from the course design | `02` courses → `05` teasers |
| `03_Consulting_Report` | The 30-page methodology deck cites the eight stages and frameworks | `03` methodology → `05` deck |
| `04_Scenarios` | The sales material uses complete cases and scenarios to substantiate value | `04` cases → `05` substantiation |
| `06_Delivery` | The deck's pricing/tiering maps to the engagement lifecycle and pricing | `06` pricing ↔ `05` deck |

## 7. Common Usage Scenarios

- **Lead development**: sales sends a one-page DM made from `ONE_PAGER_OUTLINE.md`.
- **First meeting**: use `EXECUTIVE_DECK_OUTLINE.md` to give executives a 15-20 minute intro, ending by steering toward "fill the 10-question questionnaire."
- **Deeper proposal**: by audience, pick the 20-page (department heads) or 30-page (CIO/strategy chief) version.
- **Client says "too expensive / we already have ChatGPT / is the data secure"**: flip to `SALES_FAQ.md` for the standard answer.
- **Need visuals**: hand `VISUAL_ASSETS_SPEC.md` to a designer to produce the actual files.

---

## ⭐ Cross-Topic Quick References: 5 Core Themes, Where to Find Them

The whole methodology has 5 main arteries running through every directory. How this directory connects to each:

| Cross-Topic | Primary location | How this directory connects |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + three-engine co-reading** | Root [`README_EN.md`](../README_EN.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](../00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | **AI-Native Living Book + three engines is a new-era selling point** — once adopted, the client owns "methodology + an AI co-reading partner"; the 30-page consulting deck can pitch the differentiation of the three-engine division of labor (front-line Antigravity / audit Codex / strategy Claude Code) |
| 🎓 **Academic foundation (7 pillars)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **The 30-page consulting deck cites Prof. Rosemann (QUT) + the 7 theoretical pillars** as differentiation (for academic peers, CIOs, boards); `SALES_FAQ.md` answers "what's different from Big-4 / McKinsey" using the 7 pillars as the basis |
| 📚 **L1-L5 course education** | [`../02_Course_Design/`](../02_Course_Design/) | **The 20-page standard deck contains course teasers for every level** (L1-L5 path, PoC scenarios, Stage Gates); the ONE_PAGER includes the L1-L5 map; the decks reference the course ratios and deep syllabi from `02` |
| 🔁 **Consulting / 8 stages + Phase A→B→C closed-loop** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **All sales material steers toward "fill the questionnaire to start Phase A"**; the 20/30-page decks include the three-phase contract model (Phase A 2W + Phase B 4W + Phase C 24M) + quarterly radar review; the EXECUTIVE_DECK contains the 8-stage story arc |
| 📖 **References / acknowledgments** | [`../90_References/`](../90_References/) §2 acknowledgments | **The sales decks themselves are largely self-authored** (no third-party citations); `SALES_FAQ.md` cites the 7 theoretical pillars; the acknowledgments cite Prof. Rosemann (QUT); when a client asks "why these tools," point them to the appreciation cards in 90_References §2 |
