# AI-Native Living Book: Methodology as Executable Knowledge Artifact

> 🌐 中文版本 / Chinese version: [AI_NATIVE_LIVING_BOOK.md](AI_NATIVE_LIVING_BOOK.md)
>
> Apache License 2.0 · Author: Morris Lu · Tiger AI

Last updated: 2026-05-16

---

> **What this answers**: The most distinctive feature of this methodology isn't its content — it's its **carrying medium**. Traditional consulting methodologies are PDFs / PPTs / SOPs (static documents); this repo is a **knowledge system readable, explainable, queryable, and applicable by AI IDEs**. Users don't "read documents" — they **converse with the methodology**. This document formally writes this characteristic into the methodology's positioning and addresses its academic classification + risk controls.

---

## 1. One-Sentence Positioning / Tagline

> This repository is not only a methodology toolkit, but an **AI-native living book**: when opened in an AI IDE, its embedded agent instructions ([`AGENTS.md`](../AGENTS.md) and [`CLAUDE.md`](../CLAUDE.md)) turn the static methodology into an **interactive co-reading tutor and consulting assistant**.

---

## 2. Why This Is a New Form of Methodology

### 2.1 Traditional Methodology vs. AI-Native Living Book

| Dimension | Traditional (PDF / PPT / SOP) | AI-Native Living Book (this repo) |
| --- | --- | --- |
| **Medium** | Static documents, slide decks, Word | Markdown + AI IDE instruction files (AGENTS.md / CLAUDE.md) |
| **User interaction** | One-way reading | Two-way conversation (Q&A, application, generation) |
| **Onboarding barrier** | High (must read 100+ pages) | Low (AI auto-reads, becomes co-reading tutor) |
| **How to apply** | Consultant translates for client | Client directly asks AI to apply to their company |
| **Can be challenged** | No (documents don't answer) | Yes (AI answers any question in real-time) |
| **Can be rewritten** | Consultant must edit | Client forks + AI assists consistency checking |
| **Version control** | Usually none | Full Git history (including AGENTS.md changes) |
| **Academic citation** | Cite PDF | Cite GitHub commit hash + reproducible execution environment |

### 2.2 Academic Classifications

This methodology can be categorized as one (or more) of:

| Name | Emphasized Property | Origin / Analog |
| --- | --- | --- |
| **Executable Knowledge Artifact** | Knowledge that can be executed; not just described, but applicable | Jupyter Notebooks, computational essays |
| **AI-Mediated Methodology** | AI as intermediary between user and methodology | Intelligent Tutoring Systems (ITS) |
| **Interactive Consulting Playbook** | Interactive consulting operations manual | Game playbooks, decision-tree wizards |
| **Living Book with Embedded Tutor Agent** | Living book + embedded tutor agent | Hypertext, knowledge graphs |

Tiger AI adopts **AI-native living book** as the primary term because it **simultaneously captures** "living book" (content evolves) + "AI-native" (designed for AI) + "co-reading tutor" (embedded tutor personality).

---

## 3. Three Layers: Repo as Book / Agent as Tutor / Methodology as Executable Artifact

### 3.1 Layer 1: Repo as Book

The repo structure follows book conventions:

| Book Element | Repo Mapping |
| --- | --- |
| Cover / one-sentence position | Root [`README_EN.md`](../README_EN.md) + this doc §1 |
| Preface / executive summary | [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) |
| Story chapter | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) Ming's story |
| Main methodology | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 |
| Implementation chapters | `01_Assessment` / `02_Course_Design` / `03_Consulting_Report` |
| Case anthology | `04_Scenarios/` 7 Benchmark-grade cases |
| Sales support | `05_Sales/` |
| Delivery SOP | `06_Delivery/` |
| Academic argument | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) |
| Alignment map | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) |
| Failure modes (counter-cases) | [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) |
| Research design | [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) |
| References | Each file's References + `90_References/` |

> **Key point**: This "book" is **complete** — clients / consultants / academics / regulators can each find their relevant chapter.

### 3.2 Layer 2: Agent as Tutor (AGENTS.md is the "Tutor Personality")

[`AGENTS.md`](../AGENTS.md) and [`CLAUDE.md`](../CLAUDE.md) are not supplementary notes but **embed the AI's role, boundaries, and guidance into the repo**. AI IDEs (Claude Code / Cursor / Antigravity / Codex etc.) auto-read these files and position themselves as **"co-reading tutors for this methodology"**.

#### "Tutor Personality" Defined in AGENTS.md

- **Role**: AI = co-reading tutor + consulting assistant, NOT consultant replacement
- **Scope of answerable questions**: methodology definitions, L1-L5 mapping, Stage tools, case application, report drafts
- **Refusal scope**: final client decisions, bypassing consultant judgment, unverified ROI commitments
- **Response style**: academic rigor + consulting practice + client-comprehensible
- **Citation discipline**: every conclusion tagged with [E:L#] evidence level (per Tool 8.9)
- **Language**: bilingual EN/ZH switching by user

> This design borrows from **LangChain Agent Prompt + Claude Skills**: configuration files that are version-controlled in the repo.

### 3.3 Layer 3: Methodology as Executable Artifact

Users can directly ask AI to **execute the methodology**, not just read it:

#### Typical Interactions

| User asks | AI co-reading tutor executes |
| --- | --- |
| "We're a 700-staff packaging plant; help me run the 10-Q quick survey" | AI runs [`AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) 10-Q version + auto-scores + produces radar |
| "Based on my answers, draft a Phase A mid-engagement report skeleton" | AI generates draft per [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) §3-§5 structure |
| "We're manufacturing; which case is closest to us?" | AI compares to [`SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md) and computes gap |
| "Prep materials for the Stage 3 Client Ideal Practice workshop" | AI generates workshop flow + sticky-note prompts + 4-layer printout per Tool 3.6 |
| "How does this align with McKinsey 7-Step?" | AI maps to [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) §2.1 |
| "Should my Stage 2 radar be rounder after 24 months?" | AI guides user through quarterly Gate C review |

> **This is the meaning of "Methodology as Executable Artifact"** — methodology isn't just described; it's applicable in real-time via AI.

---

## 4. Lowering Methodology Adoption Barriers

### 4.1 Enterprises Fear 100+ Markdown Files

Traditional methodology barriers:

- 100+ pages to read ❌
- Too much terminology ❌
- Don't know what to read first ❌
- Need consultant to translate ❌
- Must write report draft yourself ❌

### 4.2 AI Co-Reading Tutor Answers in Real Time

Once repo + AI IDE is open, users directly ask:

- "**What level is my company at?**" → AI runs 10-Q survey + auto-scores
- "**Which file should I read first?**" → AI recommends reading order by role (CEO / consultant / IT / academic)
- "**How do I apply this to manufacturing?**" → AI cites manufacturing case + flags customization points
- "**Please generate the first-draft diagnostic report**" → AI produces 10-15 page Phase A skeleton
- "**What's the boundary between Stage 4 and Stage 8?**" → AI cites METHODOLOGY_SCIENTIFIC_LOGIC §4

> **This shifts methodology from "expert-only readable" to "non-experts can be guided through it."**

### 4.3 Expected Reduction in Adoption Barrier

Hypotheses validated by PILOT_STUDY_PROTOCOL:

- Traditional PDF methodology: client completion rate < 15%
- **AI-native living book**: client "conversation rate" > 70% (AI proactively guides)
- Mid-sized enterprise (100-500 staff) adoption cycle: from "3-month evaluation needed" → "Phase A within 2 weeks"

---

## 5. Risk Controls

⚠️ Because AI interprets the methodology, **AI co-reading tutor must NOT do** the following:

### 5.1 Tutor Boundaries

| Can | Cannot |
| --- | --- |
| Explain methodology content | ❌ Replace formal consultant judgment |
| Run surveys, auto-score, produce radars | ❌ Promise specific ROI numbers to clients |
| Cite cases to compute gaps | ❌ Sign Ideal Practice Definition Table (requires 3-party human signature) |
| Generate report drafts | ❌ Replace client owner / consultant final review |
| Guide Stage Gate self-assessment | ❌ Replace third-party audit |
| Apply 80/20 / 5 Whys / Issue Tree in real-time | ❌ Replace longitudinal KPI real data |

### 5.2 4 Risk Control Principles

1. **AI co-reading tutor ≠ consultant**: all report drafts require **human consultant or client owner review** before external use
2. **Important diagnoses require evidence**: per [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9, major conclusions need L3+ (system log) support
3. **AGENTS.md version control**: avoid inconsistent interpretation across AI IDEs — commit every AGENTS.md change to Git and record in CHANGELOG
4. **AI-generated marking**: per Tool 8.8 §7, all AI-generated content must be marked "AI-generated"

### 5.3 Failure Scenarios

If the AI co-reading tutor is misused (documented in [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md)):

- AI errs and client takes it at face value → wrong report
- AI gives unverified ROI numbers → client signs SOW based on false hope
- Different AI IDEs interpret AGENTS.md differently → inconsistent conclusions

**Mitigations**:

- AGENTS.md explicitly mandates "**Don't predict ROI without baseline data**"
- Every report paragraph requires [E:L#] evidence-level tag
- Encourage clients to cross-validate critical conclusions with ≥ 2 AI IDEs

---

## 6. Academic Contribution

### 6.1 Contributions to IS / Consulting Methodology

| Contribution | Innovation |
| --- | --- |
| **Methodology medium innovation** | First consulting methodology built as Markdown + agent config directly executable by AI IDEs |
| **AI-mediated knowledge transfer** | Using AI as "knowledge translator" lowers methodology adoption barriers |
| **Open-source consulting framework** | Apache 2.0, can be forked / adapted by other consultants, academically reproducible |
| **Embedded tutor agent design pattern** | AGENTS.md / CLAUDE.md pattern can be borrowed by other open-source repos |

### 6.2 Connection to AI Pedagogy / ITS

- 1980s ITS research studied "how AI teaches" → this methodology is a new case of "**how AI helps adults learn professional methodologies**"
- Application of Vygotsky's ZPD (Zone of Proximal Development): AI co-reading tutor dynamically adjusts prompt depth

### 6.3 Future Research

- Cross-IDE consistency of AGENTS.md interpretation (Claude Code / Cursor / Antigravity / Codex / Windsurf)
- Longitudinal tracking of AI co-reading tutor's effect on methodology adoption rate (per PILOT_STUDY_PROTOCOL design)
- Cross-language (EN / ZH / JA / KO) methodology adoptability research

---

## 7. How It Combines with Other Documents

### 7.1 Statement in Different Locations

| Location | Main message |
| --- | --- |
| Root [`README.md`](../README.md) | One-sentence positioning (ZH §1) |
| Root [`README_EN.md`](../README_EN.md) | One-sentence positioning (EN §1) |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) | "Living Book" section |
| [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) | "How to Read This Book" section |
| [`AGENTS.md`](../AGENTS.md) | Concrete tutor personality config (in repo root) |
| Sales decks | 1 slide highlighting "AI-native living book" differentiation |
| Academic submissions | Whole chapter as methodology contribution |

### 7.2 Relationship to 4 Other Authoritative Concept Docs

| Document | Question it answers |
| --- | --- |
| [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) | "What does the user experience?" |
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | "How does the methodology run?" |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | "Why does the methodology withstand debate?" |
| [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | "How does it align with industry frameworks?" |
| **`AI_NATIVE_LIVING_BOOK_EN.md` (this doc)** | **"Why is the methodology's medium new?"** |

5 authoritative docs form a complete methodology argument: **experience + process + science + alignment + form innovation**.

---

## 8. References

- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors: Lessons learned. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.
- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Pérez, F., & Granger, B. E. (2007). IPython: A system for interactive scientific computing. *Computing in Science & Engineering*, 9(3), 21-29.
- Anthropic (2024). *Claude Code documentation*: <https://docs.anthropic.com/claude/docs/claude-code>
- OpenAI (2024). *Codex / Codex CLI*.
- Cursor (n.d.). *Cursor IDE documentation*.

---

## 9. Closing: The Next Phase of Methodology

Evolution of consulting methodologies:

```
1990s: Paper consulting reports
   ↓
2000s: PowerPoint decks
   ↓
2010s: SharePoint / Confluence wikis
   ↓
2020s: GitHub-hosted methodology + open source
   ↓
2025s: AI-Native Living Book (this methodology)
```

**What's next?** Possibly **multi-agent consulting team auto-running full Phase A** (AI consultant + AI reviewer + AI client simulator, 3-Agent collaboration) — applying L5 Multi-Agent Organization to "the methodology itself."

**But**: per §5.1, AI is always tool and tutor, never replacement. Human consultant judgment, client owner decision-making, third-party audit — these **human governance layers** are the final guarantees of methodology credibility.

---

License & Citation

This document is Apache License 2.0; may be used, modified, commercialized, provided the [`../NOTICE`](../NOTICE) attribution is preserved.
