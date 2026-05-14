# Delivery Operations Checklists

> 🌐 中文版本 / Chinese version: [DELIVERY_CHECKLISTS.md](DELIVERY_CHECKLISTS.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **Attribution:** The classification of these checklists (pre-project / security / QA / handover / offboarding) is referenced from and rewritten based on **Mirza Iqbal**'s (next8n.com) *Workflow Automation Delivery Framework* (MIT License), re-expressed in this methodology's language and mapped to the L1-L5 AI transformation consulting context. See [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md).

---

## 0. vs. Stage Gates

| | Stage Gate (methodology gate) | This document's checklists (operations gate) |
| --- | --- | --- |
| What it gates | Whether the "capability is in place" for L1-L5 courses / diagnosis | Whether the "operations are done right" for engagement delivery |
| Example | Gate 3: the n8n Workflow runs and has a Log | Security checklist: whether sensitive data is redacted |
| Document | The Evidence Matrix in `01_Assessment` | **This document** |

The two run in parallel: Stage Gates confirm "what was built is correct," operations checklists confirm "the act of delivering was done right."

---

## 1. Pre-Project Checklist

### 1.1 Sales handoff

- [ ] The SOW is signed; in / out of scope is explicit
- [ ] Payment milestones and terms confirmed
- [ ] Discovery Notes and questionnaire results handed off to the PM
- [ ] The 7 Pillars are aligned with the client

### 1.2 Team and resources

- [ ] PM, Technical Lead, Developer assigned
- [ ] The client's AI Champion / Owner assigned
- [ ] Kickoff meeting scheduled; agenda and attendees confirmed

### 1.3 Environment and access

- [ ] Deployment mode confirmed (cloud / Hybrid / fully on-premises)
- [ ] Client system access permissions in place (OpenWebUI / n8n / API / data sources)
- [ ] Platform / API / model accounts ready (client-hosted, client-paid)
- [ ] Development / test sandbox environment ready

### 1.4 Data and governance

- [ ] Sample data for training / testing prepared (de-identified)
- [ ] Off-limits data and sensitive boundaries defined
- [ ] Human review points and output owners defined

---

## 2. Security Checklist

> Maps to the 7 Pillars' principle 3, "Security First." Must pass before every delivery.

### 2.1 Accounts and permissions

- [ ] Each person has an individual account; no sharing
- [ ] Permission matrix configured (least-privilege principle)
- [ ] Admin permissions restricted to specific personnel
- [ ] SSO (if any) enabled

### 2.2 Data boundaries

- [ ] Sensitive data / PII does not enter external LLMs (or is redacted)
- [ ] The model provider's data retention policy has been reviewed
- [ ] Highly sensitive scenarios use Hybrid / fully on-premises; confirmed that data does not leave local
- [ ] DLP (if the client has it) covers the AI workflows

### 2.3 Auditing and logging

- [ ] All LLM calls are written to an Audit Log
- [ ] Audit Log retention period meets the client's compliance requirements
- [ ] Permission changes are logged
- [ ] Credentials / API Keys are stored in secret management, not in git

### 2.4 Before go-live

- [ ] The security audit report is produced and signed off by the Technical Lead
- [ ] Client IT / security (if any) has been informed and agrees

---

## 3. QA / Testing Checklist

> Maps to the 7 Pillars' principle 4, "Test Thoroughly."

### 3.1 Functional testing

- [ ] Every Skill / Workflow / Agent has been tested with "normal cases"
- [ ] Tested with "abnormal cases" (wrong input, missing data, boundary values)
- [ ] Integrated systems (Gmail / Sheets / CRM / ERP…) respond correctly
- [ ] AI output quality spot-checked (classification accuracy, summary faithfulness)

### 3.2 Error handling

- [ ] Error handling / retry / fallback tested
- [ ] Failures notify; they do not fail silently
- [ ] The DLQ (dead-letter queue) mechanism works

### 3.3 Human Gate

- [ ] High-risk actions have a human review node
- [ ] The parts where AI only produces drafts and does not auto-send have been confirmed

### 3.4 Evidence

- [ ] The Execution Log is complete
- [ ] Every deliverable is traceable to its source and reasoning basis
- [ ] Test records are archived

---

## 4. Handover Checklist

> Maps to the 7 Pillars' principle 6, "Clean Handover."

### 4.1 Deliverables

- [ ] All in-scope SOW deliverables are complete and accepted
- [ ] The deliverable list is confirmed item by item against `DELIVERY_PACKAGE_AND_ACCEPTANCE.md`
- [ ] The Handover Document is filled out (see `BUSINESS_DOCUMENT_TEMPLATES.md`)

### 4.2 Systems and accounts

- [ ] Accounts / permissions transferred to the client Admin
- [ ] Platform / API / model configuration transferred (client-hosted)
- [ ] The consultant's temporary access permissions removed

### 4.3 Documentation and knowledge transfer

- [ ] Runbook and operations documents are complete and readable by someone other than the author
- [ ] Training / walkthroughs completed
- [ ] The client confirms it can operate independently

### 4.4 Wrap-up

- [ ] Known limitations and follow-up recommendations communicated in writing
- [ ] The client signs the Handover confirmation
- [ ] The final invoice milestone is triggered

---

## 5. Offboarding Checklist

> Maps to the engagement lifecycle's Support — Exit phase.

### 5.1 Contract wrap-up

- [ ] Contract / Retainer expiration or termination confirmed
- [ ] All invoices settled
- [ ] Closing report (if agreed) delivered

### 5.2 Assets and permissions

- [ ] All of the consultant's access permissions removed
- [ ] Shared accounts / temporary credentials disabled
- [ ] Client data: the consultant-side copy is deleted or archived per agreement

### 5.3 Knowledge archival

- [ ] Project documents archived (both parties keep a copy)
- [ ] Lessons learned recorded internally (consultant side)
- [ ] Failure-mode list updated (if any incidents occurred)

### 5.4 Relationship maintenance

- [ ] Closing satisfaction feedback collected
- [ ] Follow-up support / renewal options communicated
- [ ] Referral / case-study usage authorization (if the client agrees) confirmed

---

## Citation

The 5 checklist categories are referenced from and rewritten based on Mirza Iqbal's (next8n.com) *Workflow Automation Delivery Framework* (MIT License), generalized to the L1-L5 AI transformation consulting context. See [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) for the full citation.
