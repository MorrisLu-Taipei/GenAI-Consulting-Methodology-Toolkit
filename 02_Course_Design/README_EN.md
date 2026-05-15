# 02 Course Design — L1-L5 Course Design

> 🌐 中文版本 / Chinese version: [README.md](README.md)

## 1. Purpose of This Directory

This directory is the **second phase of the three-phase service flow: Build**. Diagnosis (`01`) tells you "which level the client is at and what is missing"; this directory is **the actual courses that fill those gaps**.

The problem it solves: **AI transformation cannot rely on buying tools or listening to talks alone — the enterprise must move along L1-L5 level by level, producing acceptable assets.** This directory designs a complete syllabus for every level from L1 to L5: course objectives, target audience, pre-class conditions, classroom content, in-class hands-on practice, post-class assignments, completion criteria, and acceptance gates (Stage Gates). Every level produces **acceptable deliverables in class** (L1 Prompt Library, L2 Skill, L3 Workflow, L4 Agent, L5 Agent Team) — not "forgotten after the lecture."

Who uses this directory: course instructors, AI Champions, IT, and the learners at each course level.

## 2. Position in the Methodology

| Axis | Mapping |
| --- | --- |
| Three-phase service flow | **Build** — the second phase |
| Eight-stage consulting structure | **Stage 7 To-Be Design** (courses are the actual build of the solution) |
| L1-L5 maturity | This directory is the course body that "**pushes the client from their current level to the next**"; it spans L1-L5's **two axes** |
| Engagement lifecycle | **Delivery — Build** |

> Core principle 1: **L1-L5 connects level by level — each level's output is the next level's input.** Without company-wide L1 usage habits, L2 has no Skills to accumulate; without L2 Skills, L3 Workflows are empty pipes; without L3 Workflows, L4 Agents have no tools; without L4 Agents, L5 Teams have no members. **You cannot skip levels.**
>
> Core principle 2: **L1-L5 is two axes** — the scale axis (L1 individual → L2 department → L3 cross-department / company-wide, humans supervise AI) and the AI-autonomy axis (L4 AI super-assistant → L5 AI team, AI is operationally autonomous while humans step back to governor). The key boundary is L3 → L4. See [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0. Terminology: in this course series, **Stage Gate = acceptance gate**, and **HITL = Human-in-the-Loop**.

## 3. Goals & Benefits

| Goal | Benefit |
| --- | --- |
| Every level has a complete, deliverable syllabus | Instructors can teach directly without redesigning courses |
| In-class production of acceptable assets | Course results become organizational capability, not "forgotten after the lecture" |
| Every level has an acceptance gate (Stage Gate) | No advancing without passing — avoids level-skipping failures |
| Course ratio configured by diagnostic score | Client resources are spent on the gaps, not wasted |
| L3/L4 come with a PoC scenario library + n8n skeletons | Hands-on practice has ready-made topics and templates, not from scratch |

**If you skip this directory**: the client buys tools but has no capability, the PoC stalls forever at "demo," and AI cannot scale.

## 4. Usage Flow & Logic

```text
01_Assessment diagnosis → L-level + recommended course ratio
   ↓
COURSE_REQUIREMENTS_AND_COMPANY_PROFILE (confirm pre-class conditions, company profile, deployment mode)
   ↓
COURSE_MODULE_MATRIX (view the L1-L5 course outlines and ratio configuration)
   ↓
L1_L5_COMPLETE_COURSE_PLAN (master syllabus) + per-level deep syllabi:
   L1 OPENWEBUI → L2 ANTIGRAVITY → L3 N8N → L4 HERMES → L5 CLAWTEAM
   ↓ per level
   Teach → in-class practice (use POC_SCENARIO_SPECS / N8N_WORKFLOW_TEMPLATES as topics)
   → produce acceptable assets → pass the acceptance gate (Stage Gate) → only then advance
```

| Step | Who | When | Input | Output |
| --- | --- | --- | --- | --- |
| Confirm pre-class conditions | Consultant + client IT | Before the course | Diagnostic result, company profile | Pre-class checklist passed |
| Configure the course ratio | Consultant | Before the course | L-level + recommended ratio | L1-L5 hour allocation |
| Teach (level by level) | Instructor | Build phase | Per-level deep syllabi | Learner hands-on results |
| In-class practice | Learners | During each level | PoC scenarios / n8n skeletons | Prompt/Skill/Workflow/Agent/Team |
| Acceptance-gate verification | Consultant + client manager | After each level | In-class deliverables | Gate passed → advance |

> Logic: courses are not "teaching tool operation" but "building verifiable organizational capability along the maturity path." Each level's design follows the "produce in the first half, bridge to the next level in the second half" structure.

## 5. File Descriptions

### `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md`

The L1-L5 course requirements list and company-profile survey. Defines the pre-class conditions for each level, company basic info, data and risk attributes, system inventory, and the applicability conditions and course notes for the three deployment modes (cloud AI / Hybrid / fully on-premises). Use it before the course to confirm "is the client ready."

### `COURSE_MODULE_MATRIX.md`

The L1-L5 course-outline matrix. One table covering each level's course objectives, hands-on exercises, post-class deliverables, course packaging (half-day experience / one-day workshop / two-day rollout bootcamp / consulting diagnostic project), and the maturity-based recommended course-ratio rules.

### `L1_L5_COMPLETE_COURSE_PLAN.md`

The complete L1-L5 master course plan. The master summary of each level's course objectives, classroom content, hands-on practice, post-class assignments, completion criteria, and acceptance gate. The per-level deep syllabi are in the five files below.

### `L1_OPENWEBUI_COURSE_PLAN.md`

The L1 Controlled AI Access deep syllabus. References the OpenWebUI public playlist; covers per-person login, personal chat workspace, Admin Panel, account/role/group/permission, model control, data guidelines, and a video reference map.

### `L2_ANTIGRAVITY_COURSE_PLAN.md`

The L2 Knowledge Codification deep syllabus. References Google Antigravity's three codelabs; covers Agentic IDE, App Prototype, Unit Test, GCP Serverless Pipeline, and Gate 2A-2E. **§7.6** includes the "leveraging a ready-made Agent library (agency-agents)" module. The second half is the L2→L3 Bridge.

### `L3_N8N_TIGERAI_COURSE_PLAN.md`

The L3 Workflow Automation deep syllabus. **§1.1** splits L3 into the first half (n8n concepts and manual building) and the second half (AG + TigerAI-n8n-Skill-Pack natural-language generation, **§5.5**). References the TigerAI channel's n8n / OpenGenie videos; covers Gemini, multimodal, Sub-workflow, Data Tables, Webhook, GitHub backup, and Gate 3A-3G.

### `L4_HERMES_AGENT_COURSE_PLAN.md`

The L4 Autonomous Agent deep syllabus. **§2** is the "seven design principles of a knowledge-grade Agent" (light by day / heavy by night, the knowledge-compounding closed loop, P1>P2, write-read same source, tool/LLM division of labor, failure-mode-driven learning, why not RAG alone). Covers the main-controller + specialist-skill combination, Wiki memory, ingest/query/update, and Gate 4A-4E. **This course teaches concepts only — it does not include internal source code.**

### `L5_CLAWTEAM_COURSE_PLAN.md`

The L5 Multi-Agent Organization deep syllabus. Uses HKUDS/ClawTeam (MIT) as the implementation platform; covers the five-layer Team/Workspace/Task/Inbox/Transport architecture, git worktree, CLI hands-on, three localized scenarios, and Gate 5.

### `POC_SCENARIO_SPECS.md`

The PoC scenario library for the L3/L4 courses. 35 implementable PoCs across 7 categories (Gmail / Sheets / Notion / CRM / API / ERP + accounting bookkeeping); each includes trigger, input, AI step, systems, output, acceptance, KPI, person-days, and n8n node sequence. In-class practice picks topics directly from here.

### `N8N_WORKFLOW_TEMPLATES.md`

Turns the PoCs into n8n-importable workflow skeletons (JSON). Includes 30 PoC skeletons, the export/import flow, naming and versioning conventions, the GitHub Backup SOP, and the classroom usage flow.

### `*_EN.md`

The English-version siblings of the files above.

## 6. Mapping to Other Directories

| Directory | Relationship to this directory | Data flow |
| --- | --- | --- |
| `01_Assessment` | The diagnosis's L-level + course ratio determine the course configuration | `01` course ratio → `02` configuration |
| `00_Overview` | Courses are the "Build" phase of the storyline | `00` story → `02` realization |
| `03_Consulting_Report` | In-class outputs and observations feed into the eight-stage consulting report | `02` in-class output → `03` report |
| `04_Scenarios` | In-class demo topics are picked from the case index; PoCs can become cases | `04` cases ↔ `02` course topics |
| `06_Delivery` | Courses map to Delivery — Build in the engagement lifecycle; deliverables go into the delivery-package acceptance | `02` output → `06` acceptance |
| `90_References` | Third-party citations for each level's course (OpenWebUI / Antigravity / n8n-Skill-Pack / ClawTeam / agency-agents) | `90` citation → `02` |

## 7. Common Usage Scenarios

- **Configure the course**: take the diagnosis's course ratio → use `COURSE_MODULE_MATRIX.md` to allocate hours → open the corresponding deep syllabi.
- **Run the L3 course**: use the first half of `L3_N8N_TIGERAI_COURSE_PLAN.md` to teach concepts, the second half to teach AG+Skill Pack; pick practice topics from `POC_SCENARIO_SPECS.md` and import skeletons from `N8N_WORKFLOW_TEMPLATES.md`.
- **Learners finding practice topics**: by their own department and L-level, pick from `POC_SCENARIO_SPECS.md` or `04_Scenarios/LLM_APPS_CASE_INDEX.md`.
- **Acceptance**: after each level, pass the acceptance gate against `01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`.
