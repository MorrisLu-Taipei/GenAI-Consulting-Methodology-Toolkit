# 00 Overview — Program Overview & Entry Point

> 🌐 中文版本 / Chinese version: [README.md](README.md)

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

The client-oriented program story and chapter structure. It is not a technical document but a **narrative** — turning "why an enterprise needs AI transformation, how this method works step by step, and what acceptable output each step produces" into a coherent story a client can understand. It includes: program positioning, the three-phase path, L1-L5 and its tool mapping, **the L1-L5 two-axis model and story (§3.0)**, the pre-class future-state imagination, and the value proposition for each role (CEO/COO/CIO/IT/HR/department heads). Sales and consultants use it directly in the first client meeting.

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
