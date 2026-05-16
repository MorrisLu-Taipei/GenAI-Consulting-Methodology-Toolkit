# 00 Overview — Program Overview & Entry Point

> 🌐 Language: [繁體中文](README.md) ｜ English ｜ [Deutsch](README_DE.md) ｜ [Français](README_FR.md) ｜ [Español](README_ES.md) ｜ [日本語](README_JA.md) ｜ [한국어](README_KR.md)

## 1. Purpose of This Directory

This directory is the **single entry point** to the whole **GenAI consulting methodology toolkit**. It holds no "tools" or "deliverables" — only two things: **the methodology's story**, and **the methodology's status**.

Anyone encountering this repo for the first time — a consultant learning the method, a client evaluating whether to buy, a new colleague onboarding, a reviewer auditing — should start here. Build the overall context of "what this methodology is, why it is designed this way, and how far it has progressed" first, then move into the functional directories `01`-`06`, so you don't miss the forest for the trees.

The problem this directory solves: **a methodology without a clear entry point and status will leave users lost, misusing it, and unsure what is done versus in progress.**

## 2. Position in the Methodology

| Axis | Mapping |
| --- | --- |
| Three-phase service flow | Maps to no single phase; it is the **bird's-eye map** of "Diagnose → Build → Deliver" |
| Eight-stage consulting structure | Maps to no single stage; it is the **overview** of the eight stages |
| L1-L5 maturity | Maps to no single level; it is the **overview** of L1-L5's two axes (scale axis L1-L3, AI-autonomy axis L4-L5) |
| Engagement lifecycle | Maps to no single phase; it is the **starting-point explanation** of the whole lifecycle |

> Logical positioning: `00_Overview` answers "**what and why**"; `01`-`06` answer "**how**"; `90_References` answers "**basis and citation**."

## 3. Goals & Benefits

| Goal | Benefit |
| --- | --- |
| Let a new reader grasp the methodology's skeleton in 5-10 minutes | Shortens onboarding; reduces misuse |
| State the methodology's value proposition in the client's language | Sales can brief clients directly with the storyline |
| Maintain one authoritative project-status document | Anyone can check "where we are now, what's next" without verbal handoff |
| Connect the relationships of `01`-`06` and `90` | Users understand each directory's role and sequence |

**If you skip this directory**: users jump straight into the functional directories without understanding "why this directory exists and how it connects to the others," leaving tools used in isolation and the methodology scattered into a pile of files.

## 4. Usage Flow & Logic

```text
New reader / client
   → Read AI_TRANSFORMATION_STORY_AND_STRUCTURE.md (why + how it works + what it produces)
   → Build the overall mental model of "L1-L5 + eight stages + three-phase flow"
   → Move into 01_Assessment to start the actual diagnosis

Consultant / colleague / reviewer
   → Read TODO_WBS.md (project progress, change log, next-round candidates, work log)
   → Get the current state before acting
```

| Step | Who | When | Input | Output |
| --- | --- | --- | --- | --- |
| Read the storyline | Consultant / client / new hire | First contact with the repo | None | Overall understanding of the methodology |
| Brief the client | Sales / consultant | First pre-engagement meeting | Storyline | Client willing to enter diagnosis |
| Check project status | Consultant / colleague / reviewer | Before taking over / reviewing | None | Knows the current state and next step |
| Update status | The responsible consultant / AI | After completing a batch | The completed work | Updated `TODO_WBS.md` |

> Logic: the storyline is "outward-facing" (builds awareness for clients and new hires); `TODO_WBS.md` is "inward-facing" (gives executors the current state). One outward, one inward, together forming a complete entry point.

## 5. File Descriptions

### `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`

The client-oriented program story and chapter structure. It is not a technical document but a **narrative**. Includes: program positioning, three-phase path, L1-L5 + tool mapping, **L1-L5 two-axis model (§3.0)**, **complete 8-stage definitions + 6-week scenario walkthrough (§6)**, role value propositions. Sales and consultants use it in the first client meeting.

### `EXECUTIVE_SUMMARY_EN.md`

The whole methodology in 5 minutes, one page. For execs without time for details.

### `CLIENT_JOURNEY_STORY_EN.md` 🆕

**Ming's Story** — a 20-minute scenario story for CEOs / boards / families to grasp the methodology. Follows a 700-staff packaging plant's 24-month transformation. No tool tables, no jargon. Use for outreach, first client meetings, new-hire onboarding.

### `EIGHT_STAGE_FLOW_STORY_EN.md` 🆕

**The authoritative 8-stage flow story**: 3-phase contract model (Phase A diagnostic 2W + Phase B strategy 4W + Phase C implementation 24M) + mid-engagement assessment report + quarterly radar revisit. Required reading for consultants.

### `METHODOLOGY_SCIENTIFIC_LOGIC_EN.md` 🆕

**The methodology's scientific argumentative power**: validates the 8 stages against the 5 conditions of scientific method (observable, quantifiable, reproducible, falsifiable, auditable). Required for academic submission, regulatory lobbying, board reviews.

### `INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md` 🆕

**Alignment map with industry frameworks**: 8 stages vs McKinsey / BCG / Bain / Deloitte / Accenture / PwC; 4-layer vs TOGAF / Zachman / Dragon1; L1-L5 vs Gartner / MIT / Forrester AI Maturity. Use when clients ask "does this conflict with our methodology?"

### `AI_NATIVE_LIVING_BOOK_EN.md` 🆕

**Innovation in methodology carrying medium**: positions this methodology as an **AI-native living book** (a knowledge system directly executable by AI IDEs), not just PDF/PPT. Covers academic classifications (executable knowledge artifact, AI-mediated methodology, interactive consulting playbook), 3-layer design (Repo as Book / Agent as Tutor / Methodology as Executable Artifact), and 4 risk-control principles (AI ≠ consultant, evidence required, AGENTS.md versioned, AI-generated marking). Required for academic submissions / methodology differentiation.

### `ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md` 🆕

**7 theoretical pillars unified**: Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Task-Technology Fit (Goodhue & Thompson 1995) + Dynamic Capabilities (Teece 1997/2007) + Sociotechnical Systems & Trust in AI (Bostrom 1977/Dietvorst 2015/Glikson 2020) + Real Options (Dixit & Pindyck 1994/McGrath 1997) + Executable Knowledge Artifact (Knuth 1984). Per theory: summary + founder + contribution to Tiger AI + mapped location + citations. The single source of truth when academia / regulators / board ask "what's the theoretical basis."

### `../01_Assessment/BARS_RUBRICS_EN.md` 🆕 (academic rigor)

**Behaviorally Anchored Rating Scales**: 6 constructs × 0-4 **behavioral anchor table** (per Smith & Kendall 1963). Each score has concrete observable behaviors, **avoiding subjective consultant scoring**, improving inter-rater reliability. Maps to Pilot Study Cohen's κ ≥ 0.60 target. Core mechanism for two consultants scoring the same company consistently.

### `TODO_WBS.md`

This repo's **authoritative status document** — the single trustworthy source of "where we are now." It contains: the WBS overview (work item × priority × status), the completed-files list, completed-item details, outstanding TODOs, next-round recommended priorities, **the change log (per batch + commit hash)**, the current-status overview, and the **daily work log**. Consultants taking over, reviewers auditing, and AI continuing work should all read this first. After any batch of work, come back and update it.

### `*_EN.md`

The English-version siblings of the files above, corresponding to the Chinese versions.

## 6. Mapping to Other Directories

| Directory | Relationship to this directory | Data flow |
| --- | --- | --- |
| `01_Assessment` | The "Diagnose" phase of the storyline is realized here | `00` story → `01` diagnostic tools |
| `02_Course_Design` | The "Build" phase of the storyline is realized here | `00` story → `02` courses |
| `03_Consulting_Report` | The "Deliver" phase of the storyline is realized here | `00` story → `03` consulting report |
| `04_Scenarios` | Provides the client scenarios and case material in the storyline | `04` cases ↔ `00` story |
| `05_Sales` | Turns the storyline into sellable material | `00` story → `05` sales material |
| `06_Delivery` | Turns the methodology into a deliverable, operable business | `00` story → `06` delivery & operations |
| `90_References` | The methodology's original basis and third-party citation licensing | `90` basis → underpins `00`-`06` |

## 7. Common Usage Scenarios

- **Sales inviting a client**: use the three-phase path and value proposition in `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md` for a 30-minute methodology briefing.
- **New consultant onboarding**: read the storyline first to build awareness → read `TODO_WBS.md` for the current state → then learn directory by directory following the data flow in §6.
- **Reviewer auditing**: read the change log and work log in `TODO_WBS.md` directly, cross-checking against the git log.
- **AI continuing work**: read the "next-round candidates" and "work log" in `TODO_WBS.md` to know where to continue.

---

## ⭐ Cross-Topic Quick References: 5 Core Themes, Where to Find Them

The whole methodology has 5 main arteries running through every directory. How this directory connects to each:

| Cross-Topic | Primary location | How this directory connects |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + three-engine co-reading** | Root [`README_EN.md`](../README_EN.md) §🌟 ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | **This directory IS the "story entry point" of the AI-Native Living Book** — [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) is the full discussion; the 4 authoritative concept files (CLIENT_JOURNEY / EIGHT_STAGE_FLOW / METHODOLOGY_SCIENTIFIC_LOGIC / INDUSTRY_FRAMEWORK_ALIGNMENT) all live here |
| 🎓 **Academic foundation (7 pillars)** | [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **The unified discussion of the 7 theoretical pillars lives in this directory**: Rosemann / Cohen & Levinthal / TTF / Teece / Sociotechnical Trust / Real Options / Knuth |
| 📚 **L1-L5 course education** | [`../02_Course_Design/`](../02_Course_Design/) | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 is the authoritative narrative entry point for **L1-L5 as two axes** (scale axis + AI-autonomy axis) |
| 🔁 **Consulting / 8 stages + Phase A→B→C closed-loop** | [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **The consulting closed-loop story lives in this directory** — `EIGHT_STAGE_FLOW_STORY` §6 has the full closed-loop diagram (Phase A 2W + Phase B 4W + Phase C 24M + quarterly radar review) |
| 📖 **References / acknowledgments** | [`../90_References/`](../90_References/) §2 acknowledgments | This directory's stories use all of `90_References` material as their basis (PDF / diagrams / video notes / academic theory citations) |
