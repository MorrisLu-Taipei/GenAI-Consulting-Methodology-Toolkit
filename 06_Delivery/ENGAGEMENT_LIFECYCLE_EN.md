# Consulting Engagement Lifecycle

> 🌐 中文版本 / Chinese version: [ENGAGEMENT_LIFECYCLE.md](ENGAGEMENT_LIFECYCLE.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **Attribution:** This engagement lifecycle, the 7 Pillars, and the Sales→Delivery→Support three-phase structure are referenced from and rewritten based on **Mirza Iqbal**'s (next8n.com) *Workflow Automation Delivery Framework* (MIT License). It has been re-expressed in this methodology's language and **generalized from "n8n automation delivery" to "L1-L5 AI transformation consulting delivery,"** mapped to the eight-stage consulting structure. See [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) for the full citation and license note.

---

## 1. Two Orthogonal Axes

The prior core of this methodology is the **eight-stage consulting structure** (the diagnostic methodology). But "how to diagnose" is not the same as "how to run a consulting engagement as a complete business." This document adds the latter.

| Axis | What it is | Document |
| --- | --- | --- |
| **Methodology axis** (vertical) | How to diagnose, teach, and produce the report | Eight stages, L1-L5, `CONSULTING_TOOLKIT_TEMPLATES.md` |
| **Lifecycle axis** (horizontal) | How to find leads, sign, deliver, close out, renew | **This document** |

> The eight stages are "what the consultant does"; the engagement lifecycle is "how the firm turns this into a repeatable business." Both axes run at the same time.

---

## 2. The Three-Phase Engagement Lifecycle

### Phase 1: Sales

| Stage | Content | Output | Maps to this methodology |
| --- | --- | --- | --- |
| Lead Qualification | Decide whether a prospect is qualified (size, budget, pain points, decision authority) | Qualified / not-qualified determination | 10-item quick questionnaire (`01_Assessment`) |
| Discovery | Understand the client's current state, systems, and goals in depth | Discovery Notes | Eight-stage Stage 1; 25/50-item questionnaire |
| Proposal | Propose the solution, scope, timeline, and pricing | Proposal + draft SOW | `05_Sales` deck outlines; `BUSINESS_DOCUMENT_TEMPLATES.md` |
| Contract | Sign, confirm scope and payment | Signed SOW / contract | `BUSINESS_DOCUMENT_TEMPLATES.md` |

### Phase 2: Delivery

| Stage | Content | Output | Maps to this methodology |
| --- | --- | --- | --- |
| Kickoff | Kickoff meeting; confirm team, environment, data, permissions | Kickoff notes + environment ready | `DELIVERY_CHECKLISTS.md` pre-project |
| Build | Run the eight-stage diagnosis + L1-L5 courses + PoC build | Per-stage deliverables (Prompt/Skill/Workflow/Agent) | Eight stages, `02_Course_Design` |
| Test | Verify that PoCs, Workflows, and Agents work | Test records | `DELIVERY_CHECKLISTS.md` QA |
| Security Audit | Security review: permissions, data boundaries, Audit Log | Security audit report | `DELIVERY_CHECKLISTS.md` security; Stage Gate governance |
| Handover | Delivery package, documents, Runbook, knowledge transfer | Handover Document | `DELIVERY_PACKAGE_AND_ACCEPTANCE.md`; `BUSINESS_DOCUMENT_TEMPLATES.md` |

### Phase 3: Support

| Stage | Content | Output | Maps to this methodology |
| --- | --- | --- | --- |
| Retainer Setup | Set up the ongoing maintenance contract, SLA, and contact point | Retainer agreement | `BUSINESS_DOCUMENT_TEMPLATES.md` |
| Ongoing Maintenance | Periodic maintenance, monitoring, optimization, new requirements | Maintenance records, change orders | `DELIVERY_CHECKLISTS.md`; Change Order |
| Exit / Offboarding | Contract ends, asset transfer, account cleanup, knowledge archival | Offboarding records | `DELIVERY_CHECKLISTS.md` offboarding |

---

## 2.5 The Three-Phase Contract Model (within Delivery)

> §2's **Sales → Delivery → Support** is the **business-layer lifecycle**. This section's **Phase A / B / C** is the **contract-layer split** — breaking Delivery into three separately-signable contracts, **each ending in a "client exit point"**. Full discussion in [`../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md).

### Why Three Contract Phases

Common pain of traditional engagements:

- Single 6-month + 24-month commitment → **high psychological barrier**, client hesitates
- Proposals get bargained down (client feels "the whole bundle is unaffordable")
- After delivery, client says "I don't know what I bought"

Three-phase solution:

- **Phase A Diagnostic** — low risk, low price, concrete result → easy to sign
- **Phase A ends with "Mid-Engagement Assessment Report" as Deliverable** → client sees concrete value before signing B
- **Phase B Strategy** — client already shocked by radar, 95% sign B
- **Phase C Implementation** — client **signed their own Ideal Practice in B**, 95% sign C

### Three-Phase Contract Comparison

| Phase | Duration | Price (700-staff client example) | Stages covered | Exit (Gate) | Main Deliverable |
| --- | --- | --- | --- | --- | --- |
| **Phase A Diagnostic** | 2 weeks | NT$ 800K | Stage 1 + 2 + Stage 3 materials | **Gate A**: client reviews mid report, decides on B | Mid-engagement assessment report (10-15 pp, client receipts) |
| **Phase B Strategy** | 4 weeks | NT$ 2M | Stage 3 Ideal Practice + Stage 4 + 5 + 6 + 7 | **Gate B**: client reviews full report, decides on C | Full consulting report (14-section, 30-50 pp) + Ideal Practice Definition Table (**3-party signed**) |
| **Phase C Implementation** | 24 months | NT$ 7M | Stage 8 + quarterly radar revisit | **Gate C (quarterly)**: client decides to advance / adjust / pause | Transformation Roadmap + Change Mgmt + Value Tracking + quarterly logs |

### Exit Mechanism per Phase

- **Gate A exit**: client reviews mid report but doesn't sign B → consultant has already delivered a valuable assessment report; client can self-execute or hire another consultant. **This is why consultants dare to design Gates — the mid report is a standalone deliverable on its own.**
- **Gate B exit**: client signs Ideal Practice but doesn't sign C → consultant has delivered full report + signed Ideal table; client can find execution partner.
- **Gate C exit (each quarter)**: client decides to pause / stop → completed Phases (with Stage Gate acceptance) preserved, can resume later.

### Mapping to Business-Layer Sales→Delivery→Support

```text
Sales (business)       Delivery (business)              Support (business)
─────────────         ──────────────────              ──────────────────
Lead Qualification    Phase A Diagnostic (2W, 800K)    Retainer Setup
Discovery       ─────►  ↓ Gate A                       Maintenance (quarterly)
Proposal               Phase B Strategy (4W, 2M)       Exit / Offboarding
Contract                ↓ Gate B
                       Phase C Implementation (24M, 7M)
                        ↓ Gate C every quarter
```

> **The 3-phase contract model lives inside the Delivery phase**, but each Gate may trigger new Sales (re-sign next phase) or enter Support (quarterly maintenance).

### Implication for the Sales Team

- No more selling "24 months / NT$ 9.8M" → sell "**2-week diagnostic for NT$ 800K**", 10× lower threshold
- Sales' first call goal = **close Phase A**, not the entire bundle
- Phase A's mid-report review meeting = **conversion moment for Phase B**
- Phase B's Ideal Practice signing = **conversion moment for Phase C**

> **This is the value of "3-phase contracts + Gate exit mechanism" for sales** — convert one NT$ 9.8M yes/no decision into three smaller yes/no decisions, each easier to say yes to.

---

## 3. The 7 Pillars

The seven core principles of engagement delivery (rewritten from the original framework, generalized to the AI consulting context):

| # | Pillar | Description |
| --- | --- | --- |
| 1 | **Client Hosts** | Systems, data, and accounts run in the client's own environment / cloud; the consultant does not hold client assets long-term. Maps to this methodology's "fully on-premises / Hybrid" deployment options. |
| 2 | **Client Pays** | Platform, API, model, and license costs are borne by the client and listed transparently; consulting fees and third-party costs are kept separate. |
| 3 | **Security First** | Every delivery must pass a security review: permissions, data boundaries, Audit Log, sensitive-data redaction. Maps to the Stage Gate governance check. |
| 4 | **Test Thoroughly** | PoCs / Workflows / Agents are tested with normal + abnormal cases before going live. Maps to Stage Gate 3F and 4 evidence. |
| 5 | **Document Fully** | Every deliverable has documentation, a Runbook, and source traceability readable by someone other than the original author. |
| 6 | **Clean Handover** | The handover has a complete checklist, knowledge transfer, and account/permission transfer, so the client can operate it independently. |
| 7 | **Clear Scope** | The SOW clearly states what is in / out of scope; scope changes go through a Change Order — no unpaid expansion. |

> These 7 principles are the baseline that keeps a consulting firm from being dragged down by clients, doing unpaid work, or having security incidents. Before every delivery project starts, the team should review these 7.

---

## 4. Lifecycle × Eight-Stage Mapping

```text
Sales ─────────────┬─ Delivery ──────────────────────────┬─ Support ──────────
 Lead Qualify       │  Kickoff                            │  Retainer Setup
 Discovery ─────────┼─ Build:                             │  Maintenance
 Proposal           │    Stage 1 Current-state grasp      │  Exit / Offboarding
 Contract           │    Stage 2-3 Vision / benchmarking  │
                    │    Stage 4-5 Gap / problem framing  │
                    │    Stage 6 Benchmarking & Phased Goals                  │
                    │    Stage 7 To-Be Design (L1-L5 + PoC)   │
                    │  Test / Security Audit              │
                    │    Stage 8 Implementation & Change         │
                    │  Handover                           │
────────────────────┴─────────────────────────────────────┴────────────────────
```

- The **Sales phase** uses the `01_Assessment` questionnaires for Lead Qualification and Discovery.
- The **Build step in the Delivery phase** is running the full eight stages + L1-L5 courses.
- **Test / Security Audit / Handover** map to the Stage Gates and the acceptance in `06_Delivery`.
- The **Support phase** takes over ongoing maintenance after L4/L5 go live.

---

## 5. Pre-Engagement Checklist

Before any new consulting engagement begins, the project manager should confirm:

- [ ] The lead has passed Qualification (size, budget, pain points, decision authority)
- [ ] Discovery is complete; current state and goals are clear
- [ ] The SOW states what is in / out of scope, and the client has signed
- [ ] The 7 Pillars are aligned with the client (especially Client Hosts, Client Pays, Clear Scope)
- [ ] Team roles are assigned (see [`DELIVERY_ROLE_SOPS.md`](DELIVERY_ROLE_SOPS.md))
- [ ] Business documents are prepared (see [`BUSINESS_DOCUMENT_TEMPLATES.md`](BUSINESS_DOCUMENT_TEMPLATES.md))
- [ ] Delivery checklists are ready (see [`DELIVERY_CHECKLISTS.md`](DELIVERY_CHECKLISTS.md))

---

## Citation

The three-phase structure, 7 Pillars, and role/document classification of this engagement lifecycle are referenced from and rewritten based on Mirza Iqbal's (next8n.com) *Workflow Automation Delivery Framework* (MIT License). This methodology has rewritten and generalized it for the AI transformation consulting context; the original content was not reproduced or forked. See [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) for the full citation.
