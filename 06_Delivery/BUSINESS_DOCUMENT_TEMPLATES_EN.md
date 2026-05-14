# Business Document Templates

> 🌐 中文版本 / Chinese version: [BUSINESS_DOCUMENT_TEMPLATES.md](BUSINESS_DOCUMENT_TEMPLATES.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **Attribution:** This list and structure of business document templates is referenced from and rewritten based on **Mirza Iqbal**'s (next8n.com) *Workflow Automation Delivery Framework* (MIT License), re-expressed in this methodology's language and mapped to the AI transformation consulting context. See [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md).
>
> ⚠️ **Legal disclaimer**: This document is a **template skeleton**, not a legal document. Actual contracts and SOWs must be reviewed by your company's legal counsel / lawyer before use.

---

## 0. Document Index

| Document | When to use | Lifecycle phase |
| --- | --- | --- |
| Proposal | After a lead passes Discovery | Sales |
| Statement of Work / SOW | Proposal accepted, preparing to sign | Sales |
| Master Service Agreement / MSA outline | The master contract for long-term cooperation | Sales |
| Change Order | When the SOW scope needs adjustment | Delivery / Support |
| Invoice | Per payment milestone | Throughout |
| Handover Document | End of Delivery | Delivery |
| Retainer Agreement | Entering Support | Support |
| Key email templates | Communication at each phase | Throughout |

---

## 1. Proposal Template

```text
[Proposal] [Client Name] AI Transformation Consulting Plan

1. Background and pain points
   - 2-4 key pain points consolidated from Discovery

2. Recommended plan
   - AI maturity position: L[X]
   - Recommended three-phase path: Diagnose → L1-L5 courses → consulting report
   - Recommended course ratio: L1 __% / L2 __% / L3 __% / L4 __% / L5 __%

3. Scope
   - In scope: [list]
   - Out of scope: [list — very important, to avoid future disputes]

4. Timeline
   - Diagnose [X] weeks / Build [X] weeks / Deliver [X] weeks

5. Deliverables
   - [Map to DELIVERY_PACKAGE_AND_ACCEPTANCE.md]

6. Investment / Pricing
   - Consulting fee: NT$ ______
   - Platform / API / model costs (borne by client, listed transparently): NT$ ______
   - Payment milestones: signing __% / mid-term __% / acceptance __%

7. Team and roles
   - PM, Technical Lead, Developer (see DELIVERY_ROLE_SOPS.md)

8. Next step
   - Confirm proposal → sign SOW → Kickoff
```

---

## 2. Statement of Work (SOW) Template

```text
[Statement of Work — SOW]

Project name: ______
Client: ______          Consultant: Tiger AI 虎智科技
SOW number: ______      Date: ______

1. Project objectives
   [Quantifiable objectives, mapped to the problem framing from Discovery]

2. In Scope
   - [Explicitly list each deliverable]

3. Out of Scope
   - [Explicitly list what is not included, to avoid scope creep]

4. Deliverables and acceptance criteria
   | Deliverable | Acceptance criteria | Stage Gate |
   |-------------|---------------------|-----------|

5. Timeline and milestones
   | Milestone | Date | Payment % |
   |-----------|------|-----------|

6. Responsibilities of both parties
   - Consultant: [list]
   - Client: provide data / system access / key-personnel time / sign-off at each Gate (see 7 Pillars)

7. Assumptions and prerequisites
   - [e.g., the client already has an OpenWebUI environment / the client's IT can dedicate 2 FTE]

8. Change management
   - Any scope change requires a written Change Order from both parties; no verbal additions

9. Fees and payment
   - Consulting fee, third-party costs (borne by client), payment terms

10. Intellectual property
    - In-class outputs (Prompt/Skill/Workflow/Agent) belong to the client
    - The methodology itself is Tiger AI's Apache 2.0 open-source asset

11. Signatures
    Client: ____________  Consultant: ____________  Date: ______
```

---

## 3. Master Service Agreement (MSA) Outline

For long-term / multi-project cooperation, first sign an MSA (master contract); afterward each project signs only a SOW. The MSA should cover:

- Both parties' legal entities and contact information
- Overall service scope (details in each SOW)
- Confidentiality clause (NDA)
- Intellectual property ownership principles
- Data protection and security responsibilities (mapped to the 7 Pillars' Security First)
- Limitation of liability and disclaimers
- General payment and invoicing rules
- Termination clauses and Offboarding agreements
- Governing law and dispute resolution
- Which prevails when the MSA and a SOW conflict

---

## 4. Change Order Template

```text
[Change Order]

Related SOW: ______      Change Order number: ______      Date: ______

1. Change content
   [Describe what is to be added / modified / removed]

2. Reason for change
   [New client requirement / assumption did not hold / scope clarification]

3. Impact on scope
   - Original scope: ______
   - Scope after change: ______

4. Impact on timeline
   - Add / reduce [X] weeks

5. Impact on cost
   - Add / reduce NT$ ______

6. Signatures
   Client: ____________  Consultant: ____________  Date: ______
```

---

## 5. Invoice Template

```text
[Invoice]

Invoice number: ______      Date: ______      Due date: ______
Issued by: Tiger AI 虎智科技
Billed to: [Client]

Related SOW / milestone: ______

| Item | Description | Amount |
|------|-------------|--------|
| Consulting fee (milestone __) | | NT$ ______ |
| Third-party cost advance (if any) | | NT$ ______ |
| Subtotal | | NT$ ______ |
| Tax | | NT$ ______ |
| Total | | NT$ ______ |

Payment method: ______
Notes: overdue payment terms ______
```

---

## 6. Handover Document Template

```text
[Handover Document]

Project: ______      Handover date: ______
Delivering party: Tiger AI      Receiving party: [Client AI Champion / Owner]

1. Deliverable list and locations
   | Deliverable | Location / link | Description |

2. Systems and accounts
   - Account list, permission matrix, who is Admin
   - Platform / API / model configuration (client-hosted)

3. Runbook and operations
   - Scheduling, monitoring, error handling, fallback, incident contacts

4. Knowledge transfer records
   - Completed training / walkthroughs
   - Confirmation that the client can operate it independently

5. Known limitations and follow-up recommendations
   - [list]
   - Possible future L4/L5 expansions

6. Acceptance
   - Confirm item by item against DELIVERY_PACKAGE_AND_ACCEPTANCE.md
   Client sign-off: ____________  Date: ______
```

---

## 7. Retainer Agreement Outline

When entering the Support phase:

- Service scope: monitoring / maintenance / minor optimization / consulting hours
- SLA: response time, resolution time, service hours
- Billing method: monthly fee / hour pack / hybrid
- Handling of out-of-scope work: via Change Order or billed separately
- Contact point and escalation path
- Contract period and renewal / termination

---

## 8. Key Email Templates

| Occasion | Key points |
| --- | --- |
| Discovery invitation | Explain the meeting purpose, duration, what the client should prepare |
| Sending the proposal | Summarize 3 key points + a clear next step (do not just attach a file) |
| Kickoff notice | Time, attendees, agenda, what the client should prepare in advance |
| Stage Gate acceptance request | List this stage's deliverables + the specific items for the client to confirm |
| Change Order notice | Explain why the change is needed + its impact on scope/timeline/cost |
| Handover notice | Deliverable list + knowledge-transfer arrangements + acceptance method |
| Offboarding notice | Asset transfer, account cleanup timeline, follow-up support options |

---

## Citation

This list and structure of business document templates is referenced from and rewritten based on Mirza Iqbal's (next8n.com) *Workflow Automation Delivery Framework* (MIT License), generalized to the AI transformation consulting context. See [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) for the full citation.
