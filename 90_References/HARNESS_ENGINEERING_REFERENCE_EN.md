# Harness Engineering — Citation & Mapping Notice

> 🌐 Language: English ｜ [繁體中文](HARNESS_ENGINEERING_REFERENCE.md) ｜ Deutsch (TBD) ｜ Français (TBD) ｜ Español (TBD) ｜ 日本語 (TBD) ｜ 한국어 (TBD)

On top of "platform selection," the **L5 (Agent Team)** layer of this methodology adds a conceptual frame for *why* an Agent Team can reliably deliver — **Harness Engineering**. This document records the concept's origin, its six-layer model, how it maps onto our existing L5 / HITL Gates / Stage Gates / eight-stage process, and points to the complete worked case [`ai-news-channel`](../02_Course_Design/ai-news-channel/) inside this toolkit.

---

## 1. The Core Thesis

> "What determines whether AI can reliably deliver results is not the model itself, but **the system wrapped around the model**." — Harness Engineering

A "harness" is the tack that lets a powerful but unruly horse pull a cart steadily. Applied to AI: the model is the horse; the **harness is the set of constraints, tools, loops, and checks that make its output stable**. Harness Engineering asserts a counter-intuitive ordering:

> **Design the system first, then pick the models.**

This is exactly this methodology's standing position: the L1→L5 jump has never come from "a bigger model," but from "**placing the model inside an increasingly rigorous frame**." Harness Engineering gives that intuition a teachable, assessable name and structure.

---

## 2. The Six Harness Layers

Sourced from [`ai-news-channel/README.md`](../02_Course_Design/ai-news-channel/README.md) §"The 6 Harness Layers," adopted here as the **core conceptual skeleton of L5**:

| # | Layer | One-line definition | Implementation in [`ai-news-channel`] |
| --- | --- | --- | --- |
| 1 | **Loop** | A fixed work order, never skipped | The Fixed Loop in `CLAUDE.md`: PM→CTO→Researcher→Developer→Designer→Supervisor→PM Approve→Publish |
| 2 | **Tools** | Each agent gets only the tool scope it needs | The `tools:` frontmatter in `.claude/agents/*.md` (e.g., CTO has only `Read, Write, Glob`; Supervisor has `Bash`) |
| 3 | **Context** | All agents read the same "constitution" first | Every agent's "On Every Invocation" step 1 reads `CLAUDE.md` + `constitution/` |
| 4 | **Persistence** | Outputs & decisions are durably stored, never lost | `knowledge-base/` (deliverables / decisions / topic-archive) + `project-state.md` |
| 5 | **Verification** | A machine + human check before anything ships | The `Supervisor` agent + `verify_build.sh` (7 hard checks) + Definition of Done |
| 6 | **Constraints** | Each role's CAN / CANNOT, in black and white | The CAN / CANNOT tables in `constitution/ai-member-boundaries.md` + Context Isolation Rules |

> Mnemonic: Loop = *sequence*, Tools = *reach*, Context = *shared ground*, Persistence = *memory*, Verification = *gatekeeping*, Constraints = *boundaries*.

---

## 3. Mapping onto Existing Methodology Constructs

Harness Engineering is not a foreign import; it **consolidates discipline already scattered across this methodology into six nameable layers**:

| Harness layer | Existing construct | Source |
| --- | --- | --- |
| **Loop** | Stage ordering of the eight-stage process; the L5 Fixed Loop / dependency chains (`--blocked-by`) | `00_Overview` eight-stage; `L5_CLAWTEAM_COURSE_PLAN` §6.4 |
| **Tools** | The L1-L5 "capability = model + the tools that layer is authorized to use" two-axis view | `AI_TRANSFORMATION_STORY_AND_STRUCTURE` §3.0 |
| **Context** | The "AI-readable living book" / long-context co-reading; client scenario → theory anchoring | `CLAUDE.md` (Claude Code role); `ACADEMIC_THEORETICAL_FOUNDATIONS` |
| **Persistence** | Durable, versioned, citable deliverables (the Git→GitHub→DOI publishing cycle) | research paper §8.2.2 publishing cycle |
| **Verification** | **HITL Gates** + **Stage Gates** (human gatekeeping at each stage) | Gate design across the methodology; Bible AI governance HITL Gates |
| **Constraints** | The "constraints" field of role cards; Reviewer/Human Gate; red-line design | `L5_CLAWTEAM_COURSE_PLAN` §6.2 role cards; governance red lines |

**Takeaway: Harness Engineering is the *conceptual lens* for L5; HITL/Stage Gates are the concrete instantiation of its Verification + Constraints layers in a consulting setting.** They are two vocabularies for one discipline.

---

## 4. The L5 Triad: Platform + Lens + Worked Case

L5 teaching now rests on three complementary pieces, none dispensable:

| Role | What it is | What it teaches | File |
| --- | --- | --- | --- |
| **Platform** | ClawTeam (CLI orchestration framework) | Mechanics: how spawn / task / inbox / board / gate work | [`L5_CLAWTEAM_COURSE_PLAN_EN.md`](../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN_EN.md), [`CLAWTEAM_REFERENCE_EN.md`](CLAWTEAM_REFERENCE_EN.md) |
| **Lens** | Harness Engineering (six-layer model) | Concept: why an Agent Team can reliably deliver | This file |
| **Worked case** | `ai-news-channel` (a readable, runnable complete project) | Demonstration: what the six layers + governance look like, how to stand one up | [`ai-news-channel/TIGERAI_L5_CASE_NOTES.md`](../02_Course_Design/ai-news-channel/TIGERAI_L5_CASE_NOTES.md) |

> Suggested flow: give the mental model with the **six-layer lens** → open the **worked case** to see each layer concretely → then go hands-on with the **platform** to run your own team.

---

## 5. Source References

The Harness Engineering frame in `ai-news-channel` cites the following public sources (all 2025-2026 first-hand industry discussions):

1. Mitchell Hashimoto, *"My AI Adoption Journey"* (2026/02)
2. OpenAI, *"Harness Engineering: Leveraging Codex in an Agent-First World"* (2026/02)
3. Birgitta Böckeler / Martin Fowler, *"Harness Engineering"* @ martinfowler.com (2026/02)
4. Anthropic, *"Effective Harnesses for Long-Running Agents"* (2025/11)
5. Aakash Gupta, *"2025 Was Agents. 2026 Is Agent Harnesses."* @ Medium

> Citation discipline: when our materials cite the six layers and terminology, we note Harness Engineering as an industry-consensus frame (not any single author's proprietary IP), with `ai-news-channel` as our own original "localized worked example."

---

## 6. Alignment with Taiwan's AI Talent Guide

The *AI Industry Talent Accreditation Guidelines (May 2026)* list **Harness Engineering** as one of the emerging capability domains. Our alignment points:

- The L5 course's **six Harness layers + the `ai-news-channel` worked case** can serve as an **assessable teaching unit + hands-on assignment** for the "Harness Engineering" competency.
- When mapping to the guide's capability descriptors, write them in this methodology's **Bloom-format LOs** ([Verb]+[Content]+[Context]) so capability is measurable (see [`ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md`](../02_Course_Design/ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md) §4).

> TODO: a clause-by-clause capability mapping against the guide PDF is logged in `TODO_WBS` as a deferred item (batched with the broader Talent-Guide integration).

---

## 7. License & Authorship Notice

| Field | Value |
| --- | --- |
| **`ai-news-channel` Author** | Morris Lu · Tiger AI — **original work within this toolkit** |
| **Upstream** | No external fork, no third-party LICENSE file — a self-authored L5 teaching case |
| **License** | Follows the toolkit (code Apache 2.0 / docs CC BY 4.0) |
| **The term "Harness Engineering"** | Industry-consensus frame, cited per academic convention (§5); no claim of ownership over the term |

> Unlike ClawTeam (HKUDS, MIT, external upstream): `ai-news-channel` does **not** require NOTICE / upstream-copyright handling, because it is a self-authored original case inside this toolkit.

---

**Version:** v0.1 (2026-05-22)
**Author:** Morris Lu · Tiger AI
**Related:** [`ai-news-channel/TIGERAI_L5_CASE_NOTES.md`](../02_Course_Design/ai-news-channel/TIGERAI_L5_CASE_NOTES.md), [`L5_CLAWTEAM_COURSE_PLAN_EN.md`](../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN_EN.md), [`CLAWTEAM_REFERENCE_EN.md`](CLAWTEAM_REFERENCE_EN.md)
