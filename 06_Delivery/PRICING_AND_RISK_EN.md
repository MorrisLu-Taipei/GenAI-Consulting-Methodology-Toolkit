# Pricing & Risk Management

> 🌐 中文版本 / Chinese version: [PRICING_AND_RISK.md](PRICING_AND_RISK.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **Attribution:** This pricing and risk-management structure is referenced from and rewritten based on **Mirza Iqbal**'s (next8n.com) *Workflow Automation Delivery Framework* (MIT License), re-expressed in this methodology's language and mapped to the L1-L5 AI transformation consulting context. See [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md).
>
> ⚠️ This document is a **pricing methodology framework**, not an actual price list. Actual amounts depend on the market, scale, and individual client case.

---

## A. Pricing

### A.1 Two Separation Principles

Maps to the 7 Pillars' principles 1 and 2:

1. **Consulting fee vs. third-party costs separated** — the consulting fee (your expertise) and platform / API / model / license costs (client-hosted, client-paid) are **listed separately**. The client clearly knows what is paid to you and what is paid to the platform.
2. **Do not advance long-term costs** — third-party subscriptions should be paid from the client's own account. Short-term advances must be itemized on the invoice and capped.

### A.2 Four Pricing Models

| Model | Suitable for | Pros | Risk |
| --- | --- | --- | --- |
| **Fixed price** | Projects with clear scope (e.g., "one-day workshop," "2-day rollout bootcamp") | Easy for the client to budget, easy to sell | Scope creep eats into profit → must have a Change Order |
| **Time & Materials (T&M)** | Uncertain scope, exploratory | No unpaid work | Hard for the client to estimate the total → set a cap |
| **Value-based** | Cases with quantifiable ROI (e.g., "save X labor hours / lift Y conversion") | Highest profit | Requires proving value first; high client trust threshold |
| **Retainer (monthly)** | The Support phase | Stable cash flow | Needs a clear SLA and scope, otherwise it becomes unlimited support |

### A.3 Tiered Offerings

Maps to the `05_Sales` tiered plans:

| Plan | Duration | Pricing model | Suitable for |
| --- | --- | --- | --- |
| Half-day experience | 4 hr | Fixed price | Decision evaluation |
| One-day workshop | 8 hr | Fixed price | A 5-10 person core team |
| Two-day rollout bootcamp | 16 hr | Fixed price | Department level + 1 PoC |
| Consulting diagnostic project | 6-12 weeks | Fixed price / value-based | Company-wide L1-L5 + eight-stage report |
| Maintenance Retainer | Monthly | Monthly fee | The Support phase |

### A.4 Pricing Checklist

- [ ] Consulting fee and third-party costs are listed separately
- [ ] In / out of scope is stated in the SOW (mandatory for fixed price)
- [ ] T&M has a cap set
- [ ] Payment milestones are defined (signing / mid-term / acceptance)
- [ ] Third-party costs are paid from the client's account, not advanced long-term by the consultant
- [ ] Value-based cases: the ROI assumptions are aligned with the client
- [ ] A change buffer is reserved (Change Order mechanism)

---

## B. Risk Management

### B.1 Common Engagement Risks and Mitigations

| Risk | Symptom | Mitigation |
| --- | --- | --- |
| **Scope creep** | The client keeps "just adding one more thing" | Lock in / out of scope in the SOW; any addition goes through a Change Order |
| **Client resources not in place** | Interviews cannot be scheduled, data is incomplete, IT does not cooperate | Confirm via the Pre-Project Checklist first; state client responsibilities in the SOW |
| **Data / security incident** | Sensitive data leaked, permissions too broad | The Security Checklist must pass; Hybrid / on-prem options; Audit Log |
| **AI hallucination causing wrong decisions** | AI output taken as fact | Human Gate; evidence traceability; explicitly mark "AI draft" |
| **Payment delay / bad debt** | Invoices overdue and unpaid | Tie payment milestones to delivery; do not proceed to the next stage if the mid-term payment is unpaid |
| **Key-person dependency** | The project is tied to one specific consultant | Role SOPs; documentation; handoff golden rules |
| **Client expectation gap** | The client thinks AI is omnipotent | Manage expectations in the Discovery phase; keep Stage Gates transparent |
| **Technically infeasible** | An integration that cannot be done was promised | Check technical feasibility with the Technical Lead during the Sales phase |
| **No sponsor / champion** | No one drives the project; it stalls after 6 months | The SOW requires the client to designate an AI Champion and Owner |
| **Compliance / regulatory change** | Regulations change mid-project (finance / healthcare) | Continuously track compliance; design conservatively for highly regulated industries |

### B.2 Risk Register Template

```text
| Risk | Probability (H/M/L) | Impact (H/M/L) | Mitigation | Owner | Trigger signal |
|------|---------------------|----------------|------------|-------|----------------|
```

Created at each project's Kickoff; the PM reviews and updates it at every Stage Gate.

### B.3 When to Decline

A consulting firm's health comes from knowing when to refuse. Seriously consider not taking / not renewing when:

- The client is unwilling to sign a SOW or to write down the scope
- The client demands the consultant hold their systems / data long-term (violates the 7 Pillars' Client Hosts)
- The client demands skipping the security review or the Human Gate
- Budget and expectations are seriously mismatched (wants L4 outcomes for a half-day budget)
- The client demands the consultant bear ultimate responsibility for AI's autonomous decision outcomes
- No sponsor, no champion, no budget owner

### B.4 Incident Response

When an incident occurs (data, AI wrong decision, system failure):

1. **Stop the bleeding** — first shut down the problematic workflow / Agent
2. **Notify** — notify the client contact within the agreed time limit
3. **Record** — write it into the incident log (time, impact, root cause)
4. **Fix** — correct and re-test
5. **Retrospective** — update the failure-mode list (maps to the L4 course's "failure-mode-driven learning")
6. **Prevent** — turn this failure mode into a "do not repeat" rule

---

## Citation

This pricing and risk-management framework is referenced from and rewritten based on Mirza Iqbal's (next8n.com) *Workflow Automation Delivery Framework* (MIT License), generalized to the L1-L5 AI transformation consulting context. See [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) for the full citation.
