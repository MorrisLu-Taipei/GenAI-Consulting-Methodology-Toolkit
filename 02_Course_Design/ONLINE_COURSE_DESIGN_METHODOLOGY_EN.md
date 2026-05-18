# Online Course Design Methodology

> 🌐 Languages: [繁體中文](ONLINE_COURSE_DESIGN_METHODOLOGY.md) ｜ English (this file)

## 1. Purpose

This document is the **shared design standard** for all Tiger AI L1-L5 online courses. It is not written for any specific platform (Udemy / Coursera / Hahow / internal LMS); rather, it consolidates academic learning-science principles + the common requirements of mainstream paid course platforms into an **internal design SOP**.

Before any L1-L5 course is published (or re-edited), it must pass self-audit against the **Tier 1 mandatory threshold + the design checklist (§9)** in this document. Platform-specific adjustments are made on top of this baseline.

This document covers:

- Three foundational learning-design theories (§2)
- The 4 components and 3 quality tiers of an online course (§3-§6)
- How to write learning objectives (§4)
- Section / lecture design principles (§5)
- Interactive learning activity types (§7)
- Video / audio specifications (§8)
- Course self-audit checklist (§9)
- Audit workflow for existing L1-L5 courses (§10)

---

## 2. Three Foundational Learning-Design Theories

Any well-structured online course rests on these three principles. Violating any one of them produces the "learner watched everything but can't do anything" failure mode.

### 2.1 Backward Design

**First define what the learner must be able to do after the course; then work backward to what to teach, how to teach it, and how to assess it.**

Sequence:

```text
1. Define Learning Objectives (LOs)
        ↓
2. Design assessments / practice activities
        ↓
3. Choose materials and pedagogy (lecture / demo / reading)
```

Not "I'll teach what I know," but "the learner must know X, so I design X."

> Source: Wiggins, G., & McTighe, J. (1998). *Understanding by Design.* ASCD.

### 2.2 Constructive Alignment

**Learning objectives, instructional activities, and assessments** must all align.

Example:

| Learning Objective | Aligned Activity | Aligned Assessment |
|---|---|---|
| "Can apply the L1-L5 model to diagnose own company" | Demo + learner exercise + self-assessment example | Assignment: submit a 1-page self-diagnosis report |
| ❌ "Understand the L1-L5 model" (verb too vague) | Reading + quiz on definitions | Quiz: fill in the blanks |

The second row is the counter-example — the verb "understand" cannot be assessed, so the assessment degrades into rote recall. The learner "passes the quiz but cannot apply."

> Source: Biggs, J. (1996). Enhancing teaching through constructive alignment. *Higher Education*, 32(3).

### 2.3 Bloom's Taxonomy

When writing LOs, **first decide the cognitive level**, then pick the right verb.

| Cognitive Level | Example Verbs | When to Use |
|---|---|---|
| **Remember** | list, define, recognize, name | terminology, facts, procedural steps |
| **Understand** | explain, describe, distinguish, compare | concepts, theories, principles |
| **Apply** | apply, calculate, execute, operate | tools, procedures, templates |
| **Analyze** | decompose, compare, infer, diagnose | cases, decisions, processes |
| **Evaluate** | evaluate, judge, select, defend | proposals, strategies, quality |
| **Create** | design, generate, synthesize, construct | original outputs, novel solutions |

The cognitive level the learner is willing to reach **correlates with what they pay**: free / cheap courses usually stop at Remember-Understand; enterprise training / consulting must drive Apply or higher.

> Source: Anderson, L. W., & Krathwohl, D. R. (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman. (Revision of Bloom 1956.)

---

## 3. The 4 Components of an Online Course

Every online course has 4 components. **Each has 3 quality tiers:**

- **Tier 1 Mandatory**: cannot launch without these (most platforms enforce)
- **Tier 2 Quality**: primary determinants of learning effectiveness and ratings
- **Tier 3 Bonus**: increase enrollment, ratings, platform visibility

| Component | Contents | Detail |
|---|---|---|
| **A. Course Landing Page** | LOs, prerequisites, target audience, description | §4 |
| **B. Course Structure** | section / lecture hierarchy; intro / middle / end | §5 |
| **C. Video & Environment** | resolution, audio, lighting, background | §8 |
| **D. Interactive Learning** | quiz / assignment / practice test / supplement | §7 |

---

## 4. Learning Objectives

### 4.1 Formula

**[Bloom verb] + [content] + [context / condition]**

Examples:

| LO | Why it works |
|---|---|
| ✅ **Apply** the L1-L5 maturity model to **diagnose** your own company's current AI state, **producing** a 1-page self-assessment report | Apply level, assessable (artifact), contextual |
| ✅ **Identify** the 3 Stage Gates of Phase A / B / C, **judging** when to Stop / Go / Pivot | Analyze level, assessable (decision), contextual |
| ❌ Understand the AI maturity model | Vague verb, unassessable |
| ❌ Learn all AI tools from scratch to mastery | Overpromise, unmeasurable, no context |

### 4.2 Quantity and Specs

| Item | Spec |
|---|---|
| **LOs displayed on CLP** | **At least 4** (most platforms enforce) |
| **Per-LO length** | ≤ 160 chars (reader fatigue) |
| **Whole-course LO count** | One per section; 4-10 total depending on length |
| **Cognitive distribution** | Intro courses may stay below Apply; advanced courses must have Analyze or higher |

### 4.3 Three Pitfalls

1. **Keyword stuffing**: cramming all buzzwords into LOs blurs focus
2. **Overpromising**: "from zero to expert" / "master all AI" are obvious red flags
3. **Vague verbs**: "understand" / "know" / "be familiar with" are unassessable; learners cannot self-confirm

---

## 5. Course Structure

### 5.1 Three-Act Structure

```text
┌─────────────────────────────────────────┐
│  Introduction                           │
│  Total ≤ 10 minutes                     │
│  ├─ Intro lecture (≤ 4 min)             │
│  │    self-intro + why you + value       │
│  ├─ Course outline & LO preview         │
│  └─ Engagement activity (within first   │
│     few lectures)                       │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Instructional Sections                 │
│  Each section = 1 LO                    │
│  ├─ Section 1                           │
│  │   ├─ Section intro (state the LO)    │
│  │   ├─ Content lectures × N            │
│  │   ├─ Section recap                   │
│  │   ├─ ≥ 1 practice / assessment       │
│  │   └─ Reference materials             │
│  ├─ Section 2 ...                       │
│  └─ Section N ...                       │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Conclusion                             │
│  ├─ Recap lecture: key takeaways +      │
│  │   congratulations                    │
│  ├─ Next steps: where to go next        │
│  └─ Bonus lecture (optional)            │
└─────────────────────────────────────────┘
```

### 5.2 Section Design

| Rule | Value |
|---|---|
| LOs per section | **1 LO** |
| Min lectures per section | **≥ 3 lectures + 1 practice/assessment** |
| Section structure | intro → content → recap |
| Inter-section dependency | each section builds on the prior (progressive construction) |

### 5.3 Lecture Design

| Rule | Value |
|---|---|
| Concepts per lecture | **1 concept** |
| Lecture length (typical) | **3-6 min optimal** (2-7 min acceptable) |
| Lecture length (technical / complex) | up to 8-12 min |
| Lecture types | rotate among talking head / screencast / slides / visuals |
| Titles | clear, searchable; learner knows what's inside from the title |

**Why short lectures beat long lectures:**

- Cognitive Load Theory (Sweller 1988): single-session uptake caps around 20 minutes
- Enterprise learners (especially managers) learn in scattered time slots; **short lectures make resuming easy**
- Modular lectures are reusable / cross-linkable

### 5.4 Length Thresholds

| Item | Value |
|---|---|
| Min lecture count | **≥ 5 lectures** (platform floor) |
| Min total video duration | **≥ 30 minutes** (platform floor) |
| Recommended (intro / short) | 30 minutes – 2 hours |
| Recommended (medium) | 5-10 hours |
| Recommended (flagship) | 20+ hours |
| Intro proportion | ≤ 10% |
| Conclusion proportion | ≤ 5% |
| Middle content proportion | ≥ 85% |

---

## 6. Quality Red Lines

If any one of the following is violated, the course **must not launch**:

1. ❌ Fewer than 5 lectures or total runtime under 30 minutes
2. ❌ No learning objectives, or fewer than 4
3. ❌ LO verbs unassessable (understand / know / be familiar with)
4. ❌ Video resolution below 720p
5. ❌ Audio echo, noise, or channel desync
6. ❌ Promotional / off-topic / distracting content
7. ❌ Plagiarized course content (must have own design, examples, explanations)
8. ❌ Sections without LO alignment or without practice activity
9. ❌ Learner cannot self-confirm they learned (no assessment / no checklist)

---

## 7. Interactive Learning Activity Types

> Not strictly required, but empirically: **more interactivity → higher ratings → better sales.**

| Type | Use | Design Notes |
|---|---|---|
| **Quiz** | Check concept understanding within sections | Multiple choice, instant answer + explanation; not for memorization detail |
| **Practice Test** | Simulate certification-style exams | Timed, covers all domains, post-test score report + study recommendations |
| **Coding Exercise** | Auto-graded code practice | Provide starter code, clear spec, automatic test cases |
| **Assignment** | Open-ended task + self/peer review | Provide rubric / checklist for self-assessment; best for Apply or higher LOs |
| **Supplemental** | PDF / template / worksheet | Learner downloads and uses; lowest cost, highest ROI |

### 7.1 Formative vs Summative

| Type | Position | Use |
|---|---|---|
| **Formative** | within sections / after lectures | Learner self-checks understanding; can re-watch if wrong |
| **Summative** | end of course | Assess whole-course LO achievement |

Include **both**: formative at the end of each section, summative at the end of the course.

### 7.2 Five Requirements

Every interactive activity must satisfy:

1. **Clearly explained**: dual text + video describing purpose, expected output, required materials
2. **Time-estimated**: give a time estimate (learners take longer than you do)
3. **Well-resourced**: provide templates, examples, starter code
4. **Feedback-enabled**: provide self-assessment checklist / rubric; encourage peer feedback where appropriate
5. **Real-world contextualized**: tasks must map to real situations, not abstract exercises

---

## 8. Video & Environment Specs

### 8.1 Spec Thresholds

| Item | Min | Recommended |
|---|---|---|
| Video resolution | **720p** | 1080p (4K unnecessary; large files strain streaming) |
| Bitrate | 5 Mbps | 10 Mbps |
| Audio channels | L/R stereo | same |
| Audio sample rate | 44.1 kHz | 48 kHz |
| Audio-video sync | ✅ required | same |
| No echo, no background noise | ✅ required | same |

### 8.2 Recording Environment

| Item | Lowest cost | Recommended upgrade |
|---|---|---|
| **Camera** | smartphone 1080p (rear) | 1080p+ webcam / DSLR |
| **Microphone** | any external mic (15-30 cm from mouth) | dynamic mic (SM58 / Maono PD200X) |
| **Lighting** | natural light + overhead off | three-point lighting (front 2 + back 1) |
| **Background** | clean, uncluttered | uniform background paper / ironed solid-color sheet |
| **Noise control** | turn off AC fan, record during quiet hours | acoustic foam + rug + thick curtain |

### 8.3 Lecture Type Mix

Per lecture, rotate among these types to avoid viewer fatigue:

- **TH (Talking Head)**: instructor on camera; builds trust and emotional connection
- **S (Screencast)**: screen recording; demonstrates actual operation
- **Slides**: for structural content
- **Whiteboard / Visual**: hand-drawn or animated; explains abstract concepts

**Reference mix**: TH 30% / Screencast 40% / Slides 20% / Visual 10%.

---

## 9. Course Design Audit Checklist

Before launch / re-edit, self-audit against these 30 items.

### 9.1 Course Landing Page (CLP)

- [ ] At least 4 LOs, each ≤ 160 chars
- [ ] LO verbs at Bloom Apply or higher (intro courses may relax)
- [ ] LOs assessable (no "understand / know" verbs)
- [ ] Prerequisites clearly listed; lower the bar proactively if none
- [ ] Target audience description clear (seniority / role / problem)
- [ ] Course description covers: problem solved + what they can do + why you

### 9.2 Course Structure

- [ ] Total lectures ≥ 5
- [ ] Total video time ≥ 30 min
- [ ] Intro ≤ 10 min, including ≤ 4 min intro lecture
- [ ] One engagement activity in intro region
- [ ] Each section maps to 1 LO
- [ ] Each section has ≥ 3 lectures + ≥ 1 practice/assessment
- [ ] Each section has intro + content + recap
- [ ] Conclusion has recap + next-steps lecture

### 9.3 Lecture Design

- [ ] Each lecture covers 1 concept
- [ ] Each lecture 3-6 min (complex topics ≤ 12 min)
- [ ] Lecture titles clear, searchable
- [ ] Lecture types rotate (TH / S / Slides / Visual)

### 9.4 Interactive Learning

- [ ] At least Quiz or Assignment
- [ ] Both formative and summative assessment included
- [ ] Every activity has instruction + time estimate + template + self-check
- [ ] Tasks contextualized to real situations

### 9.5 Video Specs

- [ ] Resolution ≥ 720p
- [ ] Audio stereo, synced, noise-free
- [ ] Background clean
- [ ] Lighting not too dark

### 9.6 Completeness

- [ ] Reference materials (PDF / template / checklist) prepared
- [ ] No promotional / off-topic content

---

## 10. Audit Workflow for Existing L1-L5 Courses

Tiger AI has 5 existing course plans (`L1_OPENWEBUI_COURSE_PLAN.md` ~ `L5_CLAWTEAM_COURSE_PLAN.md`). The workflow for applying this methodology to each:

### Step 1: Run §9 checklist

For each course, produce an audit gap report:

```markdown
# L?_xxx_COURSE_PLAN — Audit Report

## ✅ Conforming
- ...

## ⚠️ Gaps (need editing)
- Gap 1: [item] / [recommended fix]
- Gap 2: ...

## 🔧 Editing workload estimate
- Text additions: X spots
- New sections: X
- New LOs: X
```

### Step 2: Prioritize fixes

- **P0**: missing LOs, no practice activity, wrong section structure → must fix
- **P1**: oversized lectures, missing reference materials → should fix
- **P2**: monotonous lecture types, missing section intros → bonus

### Step 3: Batch edit

Edit by priority; commit per batch.

### Step 4: Final audit before launch

Confirm all of §9 ✅ before submitting to any platform.

---

## 11. Relation to Existing Methodology

| Existing file | Relation to this file |
|---|---|
| `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md` | Client side: who and what to teach |
| `COURSE_MODULE_MATRIX.md` | Content side: module-to-L1-L5 mapping |
| `L1_..._COURSE_PLAN.md` ~ `L5_..._COURSE_PLAN.md` | Per-level content body |
| **This file** | **Cross-course design quality SOP** |
| `L1_L5_COMPLETE_COURSE_PLAN.md` | L1-L5 master blueprint |

This file does not replace any existing course; it is the **shared design-quality baseline** across all of them.

---

## 12. References

- Wiggins, G., & McTighe, J. (1998). *Understanding by Design.* ASCD.
- Biggs, J. (1996). Enhancing teaching through constructive alignment. *Higher Education*, 32(3), 347-364.
- Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.* Longman.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257-285.
- Mager, R. F. (1962). *Preparing Instructional Objectives.* Fearon Publishers.
- Mayer, R. E. (2009). *Multimedia Learning* (2nd ed.). Cambridge University Press.

---

**Version:** v1.0
**Date:** 2026-05-18
**Author:** Tiger AI Morris Lu 盧業興
**License:** Apache License 2.0 (consistent with the toolkit)
