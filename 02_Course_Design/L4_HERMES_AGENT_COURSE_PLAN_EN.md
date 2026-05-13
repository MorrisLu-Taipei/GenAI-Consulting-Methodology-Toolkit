> 🌐 中文版本 / Chinese version: [L4_HERMES_AGENT_COURSE_PLAN.md](L4_HERMES_AGENT_COURSE_PLAN.md)

# L4 Hermes Agent Complete Course Plan

Version: v1.0
Author: Morris Lu (盧業興) · Tiger AI 虎智科技
Applicable Level: L4 Auto Agentic AI
Reference Materials: Hermes `llm-wiki/starter-kit-v2`

---

## 1. Repositioning L4

L4 is not simply "letting the AI run tasks on its own." Within this methodology, the L4 Hermes Agent is positioned as:

> Upgrading L1 Chat, L2 Skill, and L3 Workflow into a sustainable, knowledge-driven Agent operating system.

A Hermes Agent is not a single prompt, nor a bot that merely triggers APIs. It must possess:

1. Sustainable task memory: Markdown Wiki as the source of knowledge truth.
2. Queryable indexing capability: SQLite / FTS as the derived index and query cache.
3. Composable skills: skills such as `llm-wiki-manager`, `source-analysis-zh`, `keyword-extraction-zh`, `autonomous-discovery`, and `briefing-generator` form Agent capabilities.
4. Verifiable tool chains: deterministic tools handle writing, indexing, validation, extraction, caching, delete protection, and logging.
5. Schedulable cadence: nightly ingest, morning briefing, discovery ping, evening preview, and weekly graph synthesis establish a stable operational rhythm.
6. Governable human-AI collaboration: high-risk actions retain a human gate; all outputs require evidence, logs, sources, and review records.

Therefore, the focus of the L4 course is not to convince students that Agents are powerful, but to teach the enterprise how to place an Agent inside a controlled process so it produces verifiable work output every day.

---

## 2. Course Objectives

After completing the L4 course, students should be able to:

1. Explain the differences between Hermes Agent and L1 Chat, L2 Skill, and L3 Workflow.
2. Design the use scenario, task boundaries, input sources, and human gates for a department-level Hermes Agent.
3. Build the Hermes Agent knowledge-operations structure: `purpose.md`, `SCHEMA.md`, `INBOX.md`, `queue.md`, `watchlist.md`, `tasks.md`, `wiki/`, `.index.db`.
4. Define what input the L4 Agent consumes, what process it executes, what output it produces, and which evidence is used for verification.
5. Design the operational flow for ingest, query, update, lint, briefing, discovery, and graph synthesis.
6. Plug L2 Skills and L3 Workflows into the Hermes Agent task chain.
7. Build the Agent operations Runbook, permission sheet, evidence sheet, Stage Gate, and go-live checklist.
8. Judge which tasks are suitable for L4, and which tasks must remain at L1-L3 or be deferred to L5.

---

## 3. Target Audience

| Audience | Course Focus |
|---|---|
| Department heads | Which management problems the Agent can solve, how to accept outputs, how to set Gates |
| IT / system departments | Deployment, permissions, data paths, tools, scheduling, logs, indexing, and operations |
| Process owners | Which work can be delegated to the Agent for preparation, organization, reminding, and tracking |
| Knowledge workers | How to turn documents, data, research, meetings, and tasks into a Wiki the Agent can continuously accumulate |
| Consultants / PMs | How to use L4 as the PoC or rollout plan after an AI transformation diagnosis |

---

## 4. Prerequisites

| Item | Minimum Requirement |
|---|---|
| L1 | OpenWebUI or equivalent Chat AI entry point already in place |
| L2 | At least 1-3 reusable Skills or Prompt SOPs |
| L3 | At least 1 callable n8n Workflow or API flow |
| Data | Sample documents, SOPs, FAQs, reports, research data, or client cases for training |
| Governance | Untouchable data, human review points, and output owners already defined |
| Technology | Cloud, Hybrid, or fully on-premise deployment mode confirmed |

---

## 5. L4 Input / Process / Output / Evidence

| Category | Definition |
|---|---|
| Input | Client tasks, departmental documents, PDFs, SOPs, FAQs, research, API responses, n8n Workflow results, L2 Skills, `purpose.md`, `SCHEMA.md`, `watchlist.md`, `queue.md`, permission sheet |
| Process | Orient-first, bootstrap, ingest, source analysis, keyword extraction, index upsert, query, update, lint, autonomous discovery, briefing, graph synthesis, human review |
| Output | Wiki pages, source analysis, concept/entity/claim pages, query answers, daily briefings, pending watchlist, task tracking lists, Agent execution logs, improvement suggestions, go-live report |
| Evidence | `hermes doctor` results, skill installation list, configuration files, Wiki files, logs, SQLite queries, queue/watchlist/tasks, briefing email, n8n execution logs, human review records, Gate sign-off |

---

## 6. Full Course Versions

### 6.1 L4 Foundation: 3 Hours

Goal: Help managers and seed teams understand the value, limits, and acceptance criteria of a Hermes Agent.

| Time | Topic | Content | Output |
|---|---|---|---|
| 30 min | L4 positioning | Agent vs. Chat vs. Skill vs. Workflow | L4 consensus diagram |
| 40 min | Hermes architecture | Wiki, SQLite, skills, tools, runtime schema, policy | Hermes architecture diagram |
| 40 min | Enterprise scenarios | R&D, manufacturing, hospital, customer service, legal, marketing cases | L4 scenario candidate list |
| 40 min | IPOE | Input / Process / Output / Evidence | L4 IPOE sheet |
| 30 min | Stage Gate | Gates 4A-4E and human review | L4 Gate sheet |
| 40 min | Workshop | Rewrite one departmental task as a Hermes Agent task | Agent task card draft |

### 6.2 L4 Builder: 1 Day

Goal: Build a runnable Hermes Agent PoC.

| Time | Topic | Content | Output |
|---|---|---|---|
| 60 min | Environment health check | `hermes doctor`, gateway, model, permissions, and paths | Environment check record |
| 60 min | Skill installation | Install 5 core skills | Skill installation list |
| 60 min | Config migrate | Configure wiki path, language, embedding, email, lookback | Hermes config |
| 90 min | Bootstrap wiki | Create `wiki/`, `SCHEMA.md`, `purpose.md`, `.index.db` | Initial Wiki |
| 90 min | Ingest practice | Import a PDF / SOP / FAQ and produce source analysis | Source page and Log |
| 60 min | Query / file-back | Answer questions with citations; write query results back to the Wiki | Query record |
| 60 min | L2/L3 integration | Invoke Skills and n8n Workflows to form Agent task chains | Agent test run |
| 60 min | Gate 4 acceptance | Check evidence, permissions, logs, and human review | Gate 4A-4C records |

### 6.3 L4 Operator: 2 Days

Goal: Move Hermes Agent from PoC to a maintainable departmental operation.

| Time | Topic | Content | Output |
|---|---|---|---|
| 90 min | Orient-first SOP | Before each Agent session, read schema, runtime, purpose, INBOX, index, log | Agent start-of-shift SOP |
| 90 min | Update mode | Let the Agent edit existing Wiki pages while preserving diff, rationale, and log | Update records |
| 90 min | Lint / schema | Check frontmatter, cross-refs, missing fields, broken links | Lint report |
| 90 min | Discovery | Configure the watchlist to collect metadata from external sources without direct ingest | P2 queue |
| 90 min | Briefing | Produce morning briefing, evening preview, and 2h ping | Briefing report |
| 90 min | Graph synthesis | Find concept relations, contradictions, gaps, and next-step tasks | Graph insight |
| 90 min | Cron / Runbook | Nightly ingest, morning briefing, discovery ping, weekly lint | Operations schedule |
| 90 min | Governance | Permissions, data classification, human Gate, fallback, incident handling | L4 governance sheet |
| 90 min | Demo day | Each team demonstrates a full Hermes Agent loop | Demo and acceptance |
| 90 min | Roadmap | Bridge L4 to the prerequisites of L5 ClawTeam | L4-to-L5 Roadmap |

---

## 7. How the Five Core Skills Enter the Course

| Skill | Course Positioning | What Students Must Master |
|---|---|---|
| `llm-wiki-manager` | The master skill of the Hermes Agent | Bootstrap, ingest, query, update, lint, graph-synthesis, schema-evolve |
| `source-analysis-zh` | Rigorous source analysis skill | Convert PDFs, articles, reports, regulations, and videos into a 10-section analysis |
| `keyword-extraction-zh` | Knowledge expansion skill | Extract keyword candidates from new material for human approve / reject |
| `autonomous-discovery` | Autonomous discovery skill | Search external sources based on the watchlist for metadata; add to queue without direct ingest |
| `briefing-generator` | Operational cadence skill | Produce morning briefing, evening preview, 2h ping, weekly graph digest |

---

## 8. L4 Stage Gate Controls

| Gate | Check Question | Required Evidence | Verdict |
|---|---|---|---|
| Gate 4A: Environment operational | Are Hermes, the model, the gateway, and permissions usable? | `hermes doctor`, model list, gateway status | Pass / Fail |
| Gate 4B: Knowledge base operational | Are the Wiki, schema, purpose, and index in place? | `SCHEMA.md`, `purpose.md`, `.index.db`, initialization log | Pass / Fail |
| Gate 4C: Ingest loop operational | Can the Agent consume documents, analyze, write, index, and log? | Source page, concept/entity/claim, log, SQLite query | Pass / Fail |
| Gate 4D: Query and update operational | Can the Agent answer with evidence, write results back, and keep records? | Query record, update diff, source citation, human review record | Pass / Fail |
| Gate 4E: Operations and governance operational | Are scheduling, briefing, watchlist, queue, and human Gate in place? | Cron settings, briefing, queue, watchlist, permission sheet, Gate sign-off | Pass / Fail |

If Gates 4A-4C do not pass, do not move to departmental go-live. If Gates 4D-4E do not pass, demos are allowed but you may not claim an operable L4 Agent.

---

## 9. L4 Control Sheet

| Control | Field | Description |
|---|---|---|
| Agent task card | Role, task, user, data sources, prohibitions, human Gate | Defines what the Agent can and cannot do |
| Input Register | Documents, APIs, Workflows, Skills, data classification, Owner | Confirms the data ingested is available and authorized |
| Process Map | Orient, ingest, query, update, briefing, discovery, lint | Confirms every step has an SOP |
| Output Register | Wiki pages, reports, summaries, reminders, tasks, updates | Confirms outputs are usable by the business |
| Evidence Register | Logs, indices, citations, execution logs, review records | Confirms outputs are verifiable |
| Risk Register | Hallucination, wrong citation, data leakage, over-automation, unauthorized modification | Confirms risks are controlled |
| Stage Gate | 4A-4E | Confirms readiness for the next phase |

---

## 10. Classroom Exercises

### Exercise 1: L4 Task Breakdown

Rewrite "weekly compilation of customer complaints and improvement suggestions" as a Hermes Agent task.

Required:

- Who is the user?
- When does the Agent run, daily or weekly?
- Which documents, systems, and Workflows must it consume?
- Which actions may only produce drafts and must not be sent automatically?
- What evidence does the manager use to accept the result?

### Exercise 2: Build Purpose and Schema

For a departmental Agent, build:

- `purpose.md`
- `SCHEMA.md`
- Source types
- Concept types
- Prohibitions
- Domain-specific red flags

### Exercise 3: Ingest a Document

Ingest a PDF, SOP, FAQ, or report and produce:

- Source analysis
- Source page
- Keyword candidates
- Log
- SQLite query results

### Exercise 4: Generate a Briefing

Based on `INBOX.md`, `queue.md`, `watchlist.md`, and `tasks.md`, produce a morning briefing readable by a manager.

### Exercise 5: Design Gate 4

Each team designs its own Gate 4A-4E judgement sheet and explains which missing evidence would prevent go-live.

---

## 11. L4 Deliverables

| Deliverable | Description | Acceptance Method |
|---|---|---|
| L4 Hermes Agent task card | Defines role, task, boundaries, tools, human Gate | Department head sign-off |
| L4 IPOE sheet | Defines input, process, output, evidence | Consultant and IT review |
| Hermes Agent architecture diagram | Explains the relationship between Wiki, SQLite, skills, tools, cron, OpenWebUI / n8n | Classroom presentation |
| Initial Wiki | Creates purpose, schema, INBOX, queue, watchlist, tasks | Files and screenshots |
| Ingest test record | Import at least 1 real or sample document | Source page, log, index |
| Query / Update test record | At least 3 traceable queries and 1 write-back | Query record, update diff |
| Briefing template | Morning briefing or weekly briefing | Sample report |
| L4 Stage Gate sheet | Gates 4A-4E | Sign-off record |
| Operations Runbook | Scheduling, monitoring, fallback, human review, incident handling | IT / Owner acceptance |

---

## 12. Industry Adjustments

| Industry | Recommended L4 Entry Point | Special Notes |
|---|---|---|
| R&D / manufacturing | Technical document Wiki, complaint summaries, abnormality root-cause notes, ERP anomaly report drafts | Do not modify ERP core data directly; start with suggestions and tracking |
| Marketing / services | Proposal asset library, competitor monitoring, event briefings, customer weekly-report drafts | External discovery can be adopted faster, but source credibility must be labelled |
| Hospital / medical | Internal SOP lookup, customer service FAQ drafts, quality-incident summaries, research literature briefings | Do not provide diagnosis or treatment recommendations; high-risk content must be human-reviewed |
| Legal / finance | Regulation tracking, case summaries, risk alerts, research data compilation | Strengthen citation, versioning, review, data retention, and compliance |
| Internal management | Meeting minutes, task tracking, policy Q&A, cross-departmental progress briefings | Clearly define data permissions and accountability |

---

## 13. Deployment Mode Adjustments

| Mode | L4 Course Adjustment |
|---|---|
| Cloud AI | Quick demonstration of the Agent loop; suitable for PoC, knowledge curation, and non-sensitive documents |
| Hybrid | Documents and indices remain on-premise; the model or some APIs use the cloud; suitable for most enterprise rollouts |
| Fully on-premise | Strengthen the model, gateway, intranet data, permissions, logs, backup, audit, and operations; the course must add technical implementation time |

---

## 14. Bridge Conditions from L4 to L5

L5 ClawTeam should only be considered when L4 has all of the following:

1. At least 1 Hermes Agent has passed Gates 4A-4E.
2. The Agent's input, process, output, and evidence are all traceable.
3. A stable Wiki memory, logs, indexing, and briefing cadence are in place.
4. At least 2 reusable L2 Skills exist.
5. At least 1 stable L3 Workflow exists.
6. High-risk decisions have human Gates and accountable Owners.

L5 is not about putting several unstable Agents together; it is about letting governable L4 Agents enter team collaboration.
