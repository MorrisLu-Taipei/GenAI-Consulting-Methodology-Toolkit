> 🌐 中文版本 / Chinese version: [L4_HERMES_AGENT_COURSE_PLAN.md](L4_HERMES_AGENT_COURSE_PLAN.md)

# L4 Hermes Agent Complete Course Plan

Version: v1.1
Author: Morris Lu (盧業興) · Tiger AI 虎智科技
Applicable Level: L4 Autonomous Agent
Reference material: internal implementation experience with a knowledge-type Agent architecture (Hermes Agent)

> Note: the concepts in this course are drawn from internal implementation experience with a knowledge-type Agent and are used for teaching purposes only. The course teaches **only methodology and design principles** — it does not include internal source code, tool scripts, configuration details, or proprietary implementations. When going to production, students should design the implementation according to their own environment.

---

## 1. Repositioning L4

L4 is not just "letting AI run tasks on its own." In this methodology, the positioning of the L4 Hermes Agent is:

> Upgrade L1 Chat, L2 Skill, and L3 Workflow into a continuously running knowledge-type Agent operating system.

The Hermes Agent is not a single prompt, nor a bot that only triggers APIs. It should have:

1. **Persistent task memory:** a Markdown knowledge base as the source of truth.
2. **Queryable indexing:** an index database (a derived cache rebuildable from Markdown) as the query-acceleration layer.
3. **Composable skills:** capability composed of "1 orchestrator skill + several specialist skills."
4. **A verifiable tool chain:** deterministic tools handle the "bookkeeping" work of writing, indexing, validation, extraction, caching, deletion protection, and logging.
5. **A schedulable work rhythm:** nightly digestion, morning briefing, periodic discovery, evening preview, and weekly knowledge-graph synthesis form a stable operating rhythm.
6. **Governable human-AI collaboration:** high-risk actions keep a human Gate; all output must have evidence, logs, sources, and review records.

Therefore, the focus of the L4 course is not to convince students that Agents are impressive, but to teach the enterprise how to put an Agent into a controllable process so it stably produces verifiable work outcomes every day.

---

## 2. The Seven Design Principles of an L4 Knowledge-Type Agent

These seven principles are the conceptual core of the L4 course. If students learn only tool operations without understanding these principles, the Agents they build will stop at "a demo that runs" and never become "an organizational capability that grows."

### 2.1 Light by Day, Heavy by Night

The Agent's work rhythm should be time-divided:

- **By day:** do only lightweight, real-time things — collect files, answer questions, record tasks. Do not interrupt the user.
- **By night:** do the heavy, batch things — digest the data collected during the day, write to the knowledge base, build cross-references, rebuild the knowledge graph.

This keeps the Agent "quiet" while the user is working, and "growing itself" after hours.

### 2.2 The Compounding-Knowledge Closed Loop

The value of a knowledge-type Agent comes from a **closed loop of self-growth**, not from one-off processing:

```text
Ingest data → Extract keyword candidates → Human selects → Add to watchlist
   ↑                                                            ↓
Ingest again  ←  Into the task queue  ←  Auto-discover external sources  ←
```

Every ingest makes the next ingest smarter. If any link of the loop breaks (e.g., forgetting to extract keywords), the knowledge base stops growing.

### 2.3 Human-Submitted Tasks Always Outrank Auto-Discovery

Tasks have two sources with different priorities:

- **P1 — Human-submitted:** what the user actively submits — **must be cleared the same night.**
- **P2 — Auto-discovered:** what the Agent finds on its own from external sources — queued after P1.

The Agent cannot defer the user's assigned tasks just because "it found a bunch of interesting things." Human needs always come first.

### 2.4 Read and Write from the Same Source

A query's answer can be chosen to "write back" into the knowledge base. As a result:

> The act of asking a question is itself growing the knowledge base.

The next time someone asks a similar question, they can retrieve the previously organized answer. Reading and writing share the same knowledge source — they are not two separate systems.

### 2.5 Tools Do Bookkeeping, the LLM Does Judgment — Don't Swap Roles

A clear division of labor:

| Role | Responsible for | Why |
|---|---|---|
| **Deterministic tools** | Writing files, indexing, SQL upsert, format validation, multi-format extraction, log appending | These must be 100% accurate and repeatable — the LLM should not "guess" them |
| **LLM / Agent** | Reading, analysis, judgment, cross-data reasoning, synthesizing answers | These require understanding and judgment that tools cannot do |

Swapping the two roles causes incidents — having the LLM compute a hash or write to a database produces errors, while having a tool judge "is this paper important" is simply not possible.

### 2.6 Failure-Mode-Driven Learning

Record **real incidents** and use them as teaching material for the Agent and the team:

> "2026-XX-XX: the Agent wrote without orienting first, creating duplicate pages and no log" → Fix: always orient before any write (read the purpose, structure, index, and current state).

Every failure mode maps to a "never repeat" rule. The L4 course teaches students to build their own "failure-mode list."

### 2.7 Why Not Just RAG

L4 should make students understand the difference between a "knowledge-type Agent" and "pure RAG":

| Approach | Problem |
|---|---|
| **Pure RAG** | Every query re-reads the original documents — cost rises linearly with data volume, knowledge does **not** compound |
| **Note-taking software** | Requires a person to organize it manually — the person becomes the bottleneck |
| **Knowledge-type Agent (L4)** | The Agent "digests" data at night into structured knowledge pages and a knowledge graph; queries traverse the index and graph, and knowledge **compounds** |

L4 does not oppose RAG — it makes RAG one retrieval stage within the "knowledge-type Agent," not the whole thing.

---

## 3. Course Objectives

After completing the L4 course, students should be able to:

1. Explain the differences between the Hermes Agent and L1 Chat, L2 Skill, and L3 Workflow.
2. Explain the seven design principles in Section 2 and use them to review their own Agent design.
3. Design the use scenario, task boundaries, input sources, and human Gate of a department-level Hermes Agent.
4. Build the Hermes Agent's knowledge-operations structure: purpose file, domain-structure file, inbox, task queue, watchlist, task-tracking file, knowledge base, index cache.
5. Define what input the L4 Agent consumes, what process it runs, what output it produces, and what evidence is used to verify it.
6. Design the workflows for ingest, query, update, lint, briefing, discovery, and knowledge-graph synthesis.
7. Plug L2 Skills and L3 Workflows into the Hermes Agent's task chain.
8. Build the Agent operations Runbook, permission table, evidence table, Stage Gate, and go-live checklist.
9. Judge which tasks are suitable for L4 and which must remain at L1-L3 or be deferred to L5.

---

## 4. Audience

| Audience | Course Focus |
|---|---|
| Department managers | What management problems the Agent can solve, how to accept outcomes, how to set Gates |
| IT / systems department | Deployment, permissions, data paths, tools, scheduling, logs, indexing, and operations |
| Process Owners | Which work can be handed to the Agent to prepare, organize, remind, and track |
| Knowledge workers | How to turn documents, data, research, meetings, and tasks into a knowledge base the Agent can accumulate over time |
| Consultants / PMs | How to use L4 as a PoC or adoption plan after the AI transformation diagnostic |

---

## 5. Prerequisites

| Item | Minimum Requirement |
|---|---|
| L1 | An OpenWebUI or equivalent Chat AI entry point already in place |
| L2 | At least 1-3 reusable Skills or prompt SOPs |
| L3 | At least 1 callable n8n Workflow or API process |
| Data | Sample documents, SOPs, FAQs, reports, research data, or client cases available for training |
| Governance | Untouchable data, human review points, and output owners already defined |
| Technical | Cloud, Hybrid, or fully on-prem deployment mode confirmed |

---

## 6. L4 Input / Process / Output / Evidence

| Category | Definition |
|---|---|
| Input | Client tasks, department documents, PDFs, SOPs, FAQs, research data, API responses, n8n Workflow results, L2 Skills, purpose file, domain-structure file, watchlist, task queue, permission table |
| Process | Orient-first, bootstrap, ingest, source analysis, keyword extraction, index update, query, update, lint, autonomous discovery, briefing, knowledge-graph synthesis, human review |
| Output | Knowledge-base pages, source analyses, concept/entity/claim pages, query answers, daily briefings, pending-review watchlist, task-tracking list, Agent execution records, improvement recommendations, go-live report |
| Evidence | Environment health-check results, skill installation list, configuration files, knowledge-base files, logs, index query results, queue/watchlist/task files, briefing emails, n8n execution records, human review records, Gate sign-offs |

---

## 7. Full Course Versions

### 7.1 L4 Foundation: 3 Hours

Goal: Help managers and the seed team understand the value, limits, and acceptance methods of the Hermes Agent.

| Time | Topic | Content | Output |
|---|---|---|---|
| 30 min | L4 positioning | Agent vs. Chat vs. Skill vs. Workflow | L4 consensus diagram |
| 40 min | Seven design principles | Section 2's seven principles: light-by-day/heavy-by-night, compounding knowledge, P1>P2, read-write same source, tool/LLM division, failure modes, why not just RAG | Design-principle checklist |
| 40 min | Hermes architecture | Knowledge base, index cache, skill composition, tool chain, structural contract, policy | Hermes architecture diagram |
| 40 min | Enterprise scenarios | R&D, manufacturing, hospital, customer service, legal, marketing cases | L4 scenario candidate list |
| 30 min | IPOE and Stage Gate | Input / Process / Output / Evidence, Gates 4A-4E, and human review | L4 IPOE table, Gate table |
| 40 min | Workshop | Rewrite a department task into a Hermes Agent task | Agent task card draft |

### 7.2 L4 Builder: 1 Day

Goal: Build a runnable Hermes Agent PoC.

| Time | Topic | Content | Output |
|---|---|---|---|
| 60 min | Environment health check | Environment health check, gateway, model, permission and path confirmation | Environment check record |
| 60 min | Skill installation | Install the orchestrator skill and specialist skills | Skill installation list |
| 60 min | Configuration initialization | Configure knowledge-base path, language, indexing, notification recipient, discovery time window | Agent configuration file |
| 90 min | Bootstrap the knowledge base | Build the knowledge base, domain-structure file, purpose file, index cache | Initial knowledge base |
| 90 min | Ingest practice | Import a PDF / SOP / FAQ and produce a source analysis | Source page and log |
| 60 min | Query / read-write same source | Answer questions with citations, write the query result back into the knowledge base | Query record |
| 60 min | L2/L3 integration | Invoke Skills and n8n Workflows to form the Agent task chain | Agent test run |
| 60 min | Gate 4 acceptance | Check evidence, permissions, logs, human review | Gate 4A-4C record |

### 7.3 L4 Operator: 2 Days

Goal: Turn the Hermes Agent from a PoC into operable department work.

| Time | Topic | Content | Output |
|---|---|---|---|
| 90 min | Orient-first SOP | Before each Agent work session, read the domain structure, structural contract, purpose file, inbox, index, and log | Agent startup SOP |
| 90 min | Update mode | Let the Agent modify existing knowledge pages, preserving diff, reason, and log | Update record |
| 90 min | Lint / schema | Check frontmatter, cross-refs, missing fields, broken links | Lint report |
| 90 min | Autonomous discovery | Configure the watchlist, collect metadata from external sources without ingesting directly (enforcing P1>P2) | P2 queue |
| 90 min | Briefing rhythm | Produce morning briefing, evening preview, periodic ping (enforcing light-by-day/heavy-by-night) | Briefing report |
| 90 min | Knowledge-graph synthesis | Find concept relationships, contradictions, gaps, and next-step tasks | Graph insight |
| 90 min | Scheduling / Runbook | Nightly digestion, morning briefing, discovery ping, weekly lint | Operations schedule |
| 90 min | Failure-mode drill | Build the department's own failure-mode list and corresponding rules | Failure-mode list |
| 90 min | Governance | Permissions, data grading, human Gate, fallback, incident handling | L4 governance table |
| 90 min | Demo day + Roadmap | Each team demos a complete Hermes Agent closed loop, and plans L4-to-L5 | Demo, acceptance, Roadmap |

---

## 8. Skill Composition: Orchestrator Skill + Specialist Skills

The capability of the L4 Hermes Agent is not one big prompt, but a composition of "1 orchestrator skill + several specialist skills." The course teaches students to understand this composition pattern, not to memorize specific skill names.

| Skill type | Course positioning | What students should master |
|---|---|---|
| **Orchestrator skill (knowledge-base management)** | The coordination hub of the Hermes Agent | bootstrap, ingest, query, update, lint, knowledge-graph synthesis, schema evolution — the orchestrator skill handles "orchestration" and delegates work to specialist skills |
| **Source-analysis skill** | Rigorous source analysis | Turn PDFs, articles, reports, regulations, and videos one by one into structured analyses |
| **Keyword-extraction skill** | Knowledge expansion | Extract keyword candidates from new data for human approve / reject (the key link of the closed loop) |
| **Autonomous-discovery skill** | Autonomous discovery | Find metadata from external sources based on the watchlist, add to the queue, but do not ingest directly |
| **Briefing-generation skill** | Operating rhythm | Produce morning briefing, evening preview, periodic ping, weekly knowledge-graph digest |

> **Skill composition principle:** the orchestrator skill is responsible only for "orchestration and decisions," and specialist skills are responsible only for "a single area of expertise." Adding a capability means "adding a specialist skill," not "making the orchestrator skill fatter." This keeps Agent capability extensible, reviewable, and replaceable.

---

## 9. L4 Stage Gate Controls

| Gate | Check Question | Required Evidence | Verdict |
|---|---|---|---|
| Gate 4A: Environment operational | Are Hermes, the model, the gateway, and permissions usable? | Environment health-check result, model list, gateway status | Pass / Fail |
| Gate 4B: Knowledge base operational | Are the knowledge base, domain structure, purpose, and index established? | Domain-structure file, purpose file, index cache, initialization log | Pass / Fail |
| Gate 4C: Ingest loop operational | Can the Agent consume documents, analyze, write, index, log, and extract keywords? | Source page, concept/entity/claim pages, log, index query, keyword candidates | Pass / Fail |
| Gate 4D: Query and update operational | Can the Agent answer with evidence, write back results, and keep records? | Query record, update diff, cited sources, human review records | Pass / Fail |
| Gate 4E: Operations and governance operational | Are there scheduling, briefings, watchlist, queue, human Gate, and failure-mode list? | Schedule configuration, briefings, queue, watchlist, permission table, failure-mode list, Gate sign-offs | Pass / Fail |

If Gates 4A-4C do not pass, do not proceed to department go-live. If Gates 4D-4E do not pass, you may run a demo but cannot claim it is an operable L4 Agent.

---

## 10. L4 Control Sheet

| Control | Fields | Description |
|---|---|---|
| Agent task card | Role, task, user, data sources, prohibitions, human Gate | Defines what the Agent can and cannot do |
| Input Register | Documents, APIs, Workflows, Skills, data level, Owner | Confirms the data the Agent consumes is usable and authorized |
| Process Map | Orient, ingest, query, update, briefing, discovery, lint | Confirms each step has an SOP |
| Output Register | Knowledge pages, reports, summaries, reminders, tasks, updates | Confirms the output is usable by the business |
| Evidence Register | Logs, index, citations, execution records, review records | Confirms outcomes are verifiable |
| Risk Register | Hallucination, wrong citations, data leakage, over-automation, unauthorized modification | Confirms risks are controlled |
| Failure-mode list | Incident description, root cause, corresponding rule | Enforces the "failure-mode-driven learning" principle |
| Stage Gate | 4A-4E | Confirms whether to proceed to the next stage |

---

## 11. Classroom Exercises

### Exercise 1: L4 Task Decomposition

Rewrite "weekly consolidation of complaints and improvement suggestions" into a Hermes Agent task.

Required:

- Who is the user?
- Which things does the Agent do by day, and which by night? (enforcing principle 2.1)
- Which documents, systems, and Workflows does it need to consume?
- Which actions may only produce a draft and not be auto-sent?
- What evidence does the manager use to accept it?

### Exercise 2: Build the Purpose and Domain Structure

For a department Agent, build:

- The purpose file (why this Agent exists — the relevance filter)
- The domain-structure file (source types, concept types, prohibitions, domain red flags)

### Exercise 3: Ingest a Piece of Data and Complete the Loop

Input a PDF, SOP, FAQ, or report, and produce:

- Source analysis
- Source page
- Keyword candidates (the key link of the loop — do not skip)
- Log
- Index query result

### Exercise 4: Generate a Briefing

Based on the inbox, task queue, watchlist, and task-tracking file, produce a manager-readable morning briefing.

### Exercise 5: Build a Failure-Mode List

Per principle 2.6, each team writes 3 Agent failure modes their department might encounter, and defines a "never repeat" rule for each.

### Exercise 6: Design Gate 4

Each team designs its own Gate 4A-4E verdict table and explains which missing evidence means it cannot go live.

---

## 12. L4 Deliverables

| Deliverable | Description | Acceptance Method |
|---|---|---|
| L4 Hermes Agent task card | Defines role, task, boundaries, tools, human Gate | Department manager sign-off |
| Seven-design-principle checklist | Review your own Agent design using the Section 2 principles | Consultant review |
| L4 IPOE table | Defines input, process, output, evidence | Consultant and IT review |
| Hermes Agent architecture diagram | Explains the relationship between knowledge base, index, skill composition, tools, scheduling, OpenWebUI / n8n | Classroom presentation |
| Initial knowledge base | Build the purpose, domain structure, inbox, queue, watchlist, task file | Files and screenshots |
| Ingest test record | Import at least 1 real or sample document and complete the loop | Source page, log, index, keyword candidates |
| Query / Update test record | Complete at least 3 traceable queries and 1 write-back | Query record, update diff |
| Briefing template | Morning briefing or weekly briefing | Report sample |
| Failure-mode list | The department's own failure modes and corresponding rules | Owner sign-off |
| L4 Stage Gate table | Gates 4A-4E | Sign-off records |
| Operations Runbook | Scheduling, monitoring, fallback, human review, incident handling | IT / Owner acceptance |

---

## 13. Industry Adjustments

| Industry | Recommended L4 Entry Point | Special Notes |
|---|---|---|
| R&D manufacturing | Technical-document knowledge base, complaint summaries, anomaly-cause consolidation, ERP anomaly report drafts | Do not directly modify ERP core data; first do recommendations and tracking |
| Marketing services | Proposal asset library, competitor monitoring, campaign briefings, client weekly-report drafts | External discovery can be adopted faster, but source reliability must be tagged |
| Hospital / healthcare | In-hospital SOP lookup, customer-service FAQ drafts, quality-incident summaries, research-literature briefings | Do not make diagnosis or treatment recommendations; high-risk content must be human-reviewed |
| Legal / financial | Regulation tracking, case summaries, risk alerts, investment-research data consolidation | Strengthen citations, versioning, review, data retention, and compliance |
| Internal management | Meeting notes, task tracking, policy Q&A, cross-department progress briefings | Clear data permissions and accountability |

---

## 14. Deployment Mode Adjustments

| Mode | L4 Course Adjustment |
|---|---|
| Cloud AI | Quickly demonstrate the Agent closed loop; suitable for PoCs, knowledge organization, non-sensitive documents |
| Hybrid | Documents and indexes can stay internal while the model or some APIs go to the cloud; suitable for most enterprise adoption |
| Fully on-prem | Strengthen the model, gateway, internal data, permissions, logs, backup, audit, and operations; the course needs more technical hands-on time |

---

## 15. Conditions for the L4-to-L5 Transition

Only when L4 already has the following capabilities is it advisable to enter L5 ClawTeam:

1. At least 1 Hermes Agent has passed Gates 4A-4E.
2. The Agent's input, process, output, and evidence are all traceable.
3. There is a stable knowledge-base memory, log, index, and briefing rhythm.
4. All seven design principles are in place (especially the compounding-knowledge closed loop and the failure-mode list).
5. There are at least 2 reusable L2 Skills.
6. There is at least 1 stable L3 Workflow.
7. High-risk decisions have a human Gate and an accountable Owner.

L5 is not about putting multiple unstable Agents together — it is about letting an already-governable L4 Agent enter team collaboration.
