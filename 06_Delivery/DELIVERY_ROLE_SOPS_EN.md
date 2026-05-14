# Delivery Role SOPs

> 🌐 中文版本 / Chinese version: [DELIVERY_ROLE_SOPS.md](DELIVERY_ROLE_SOPS.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **Attribution:** The 7-role structure of these role SOPs is referenced from and rewritten based on **Mirza Iqbal**'s (next8n.com) *Workflow Automation Delivery Framework* (MIT License), re-expressed in this methodology's language and mapped to the AI transformation consulting context. See [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md).

---

## 0. Why Role SOPs

Without clear role division, a consulting firm runs into: one person doing everything (not scalable), handoff gaps, unclear accountability, and clients not knowing the right contact. This document defines 7 delivery roles, each with: **responsibilities, key deliverables, handoff points, collaborators, and the lifecycle phase it belongs to.**

For the engagement lifecycle mapping, see [`ENGAGEMENT_LIFECYCLE.md`](ENGAGEMENT_LIFECYCLE.md). A small team may have one person wear multiple hats, but a role's "responsibilities" cannot be skipped.

---

## 1. Lead Generation

| Item | Content |
| --- | --- |
| **Lifecycle phase** | Sales — Lead Qualification |
| **Core responsibility** | Find prospects; use the 10-item quick questionnaire for an initial qualification check (size, budget, pain points, decision authority) |
| **Key deliverables** | Qualified-lead list + preliminary questionnaire results |
| **Handoff point** | Qualified lead → handed to Sales Rep; with questionnaire results and a preliminary L1-L5 position |
| **Collaborators** | Sales Rep |
| **Must not do** | Do not promise scope, pricing, or timeline to the client — that is the Closer's job |

## 2. Sales Rep

| Item | Content |
| --- | --- |
| **Lifecycle phase** | Sales — Discovery |
| **Core responsibility** | Run Discovery with qualified leads: understand current state, systems, goals, pain points in depth; arrange the 25/50-item questionnaire |
| **Key deliverables** | Discovery Notes + complete questionnaire results + preliminary solution direction |
| **Handoff point** | Discovery complete → handed to Closer for the proposal; handed to PM for resource estimation |
| **Collaborators** | Lead Gen, Closer, PM |
| **Must not do** | Do not sign contracts or make technical commitments — technical feasibility must first be checked with the Technical Lead |

## 3. Closer

| Item | Content |
| --- | --- |
| **Lifecycle phase** | Sales — Proposal, Contract |
| **Core responsibility** | Produce the proposal, set scope, price, handle objections, sign |
| **Key deliverables** | Proposal, SOW, signed contract |
| **Handoff point** | Contract signed → handed to PM to start Delivery; with the SOW (in/out of scope) and payment terms |
| **Collaborators** | Sales Rep, PM, (when needed) Technical Lead |
| **Must not do** | Do not verbally add scope outside the SOW; any scope change goes through a Change Order |

## 4. Project Manager

| Item | Content |
| --- | --- |
| **Lifecycle phase** | Throughout Delivery, into Support |
| **Core responsibility** | Kickoff meeting, scheduling, resource coordination, progress tracking, Stage Gate gatekeeping, client communication contact |
| **Key deliverables** | Kickoff notes, project schedule, Stage Gate acceptance records, Handover Document |
| **Handoff point** | Only move to the next stage after each Stage Gate is confirmed; Handover complete → handed to Support |
| **Collaborators** | Closer, Technical Lead, Developer, Client |
| **Must not do** | Do not skip Stage Gates; do not claim delivery complete without acceptance |

## 5. Technical Lead / AI Platform Owner

| Item | Content |
| --- | --- |
| **Lifecycle phase** | Delivery — Build, Test, Security Audit |
| **Core responsibility** | Technical solution architecture (cloud/Hybrid/on-prem), L1-L5 platform selection, security review, technical risk judgment, Developer guidance |
| **Key deliverables** | Solution architecture, security audit report, L4 Workflow Contract, technical risk list |
| **Handoff point** | Architecture confirmed → Developer starts building; security review passed → PM enters Handover |
| **Collaborators** | PM, Developer, Client IT |
| **Must not do** | Do not let anything go live without passing the security review; do not bypass the 7 Pillars' "Security First" |

## 6. Developer / AI Engineer

| Item | Content |
| --- | --- |
| **Lifecycle phase** | Delivery — Build, Test |
| **Core responsibility** | The actual build — L1 account setup, L2 Skills, L3 n8n Workflows, L4 Hermes Agent, L5 ClawTeam; write tests and documentation |
| **Key deliverables** | Skills / Workflows / Agents, test records, Runbook, GitHub backup |
| **Handoff point** | Build + test complete → Technical Lead review → PM acceptance |
| **Collaborators** | Technical Lead, PM |
| **Must not do** | Do not deliver anything untested, undocumented, or without evidence; do not change SOW scope unilaterally |

## 7. Client (Client-Side Role)

| Item | Content |
| --- | --- |
| **Lifecycle phase** | Throughout |
| **Core responsibility** | Provide current-state data, system access, time for key-personnel interviews, sign-off at each Stage Gate, receipt and acceptance at Handover |
| **Key deliverables** | Signed SOW / Gate acceptances / Handover confirmation; designate an internal AI Champion and Owner |
| **Handoff point** | The client's AI Champion takes over operations in the Support phase |
| **Collaborators** | PM (primary contact), Technical Lead |
| **Client must know** | Per the 7 Pillars: the client hosts systems and data, the client pays platform costs, and scope changes require client confirmation |

---

## 8. Role × Lifecycle Matrix

| Role | Sales | Delivery | Support |
| --- | :---: | :---: | :---: |
| Lead Generation | ● | | |
| Sales Rep | ● | | |
| Closer | ● | | |
| Project Manager | ○ | ● | ○ |
| Technical Lead | ○ | ● | ○ |
| Developer | | ● | ○ |
| Client | ● | ● | ● |

(● Primary owner　○ Participant)

---

## 9. Handoff Golden Rules

1. **Every handoff carries documentation** — Lead→Sales carries questionnaire results; Sales→Closer carries Discovery Notes; Closer→PM carries the SOW; Delivery→Support carries the Handover Document.
2. **A handoff is not a dump** — the handing-off party must confirm the receiving party understands before the handoff counts as complete.
3. **The client always has a single primary contact** — in the Delivery phase that is the PM; do not let the client be contacted by multiple people at once and get confused.
4. **When one person wears multiple hats in a small team, the responsibility list cannot be skipped** — wearing a hat does not mean omitting that role's check items.

---

## Citation

The 7-role structure of these role SOPs is referenced from and rewritten based on Mirza Iqbal's (next8n.com) *Workflow Automation Delivery Framework* (MIT License), generalized to the AI transformation consulting context. See [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) for the full citation.
