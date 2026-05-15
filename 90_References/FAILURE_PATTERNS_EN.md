# Failure Patterns & Counter-Cases: When Tiger AI Methodology Should Not Be Applied / Will Fail

> 🌐 中文版本 / Chinese version: [FAILURE_PATTERNS.md](FAILURE_PATTERNS.md)
>
> Apache License 2.0 · Author: Morris Lu · Tiger AI

Last updated: 2026-05-16

---

> **Purpose**: A methodology that only discusses success is sales material. Academic / regulatory / serious clients ask: "**When does it fail? When should it not be applied? What goes wrong if levels are skipped?**" This document publicly records known failure patterns and counter-cases as hard evidence of methodology critiquability and improvability.

---

## 1. Why a Methodology Must Publish Failure Modes

| Audience | Why they need to see failures |
| --- | --- |
| **Academic reviewers** | Only-success cases = selection bias → unpublishable |
| **Regulators** | Risk assessment must include failure modes + early-warning conditions |
| **Serious clients** | "**Tell me when you fail**" is the real trust question |
| **Consultants** | Failure modes = institutional memory = avoid repetition |

> A methodology that **only discusses success** is less trustworthy than one that **admits failure**.

---

## 2. Level-Skipping Failures

### 2.1 Skip L1 → Jump to L4 Agent

**Symptoms**: No company-wide L1 adoption. Boss sees an Agent demo and wants a customer-service Agent. 3 engineers build an Agent in 3 months. Once live: CS staff afraid to use it, QC won't sign off, IT doesn't know how to wire audit logs, Compliance asks "who bears the risk."

**Root cause**: Staff haven't built **personal trust** through L1; no L2 Skill Library → Agent lacks "company-written judgment logic"; no L3 Workflow → Agent has no legal pipes to act on systems; no L1-L3 governance foundation → Agent goes live as compliance black box.

**Typical ending**: Agent decommissioned in 6 months; IT Deputy gets blamed; AI budget cut.

### 2.2 Skip L2 → Build L3 Workflow Directly

**Symptoms**: IT watches n8n tutorials → builds Gmail → CRM → Slack chains. Month 1: works. Staff complain "outputs are off-tone / not citing our SOPs". Engineers tune prompts, but **each Workflow has 10 prompts scattered across n8n nodes — no Owner, no version, no docs**.

**Root cause**: No L2 Skill Library as "company-written prompts + judgment + data" → L3 becomes "IT engineer's personal prompt playground."

**Typical ending**: Workflow quality drifts over time; 3 months later business unit asks to revert; IT loses trust.

### 2.3 Going L3 / L4 Without HITL

**Symptoms**: Workflow auto-sends customer emails, auto-creates invoices, auto-places orders. Month 1: 70% efficiency gain. Month 2: LLM hallucination → wrong-priced quote to a tier-A customer → NT$ 3M contract lost.

**Root cause**: All AI has ~0.5-3% hallucination rate. **No HITL = sooner or later hits a zero-tolerance scenario**.

**Typical ending**: C-suite bans AI; AI Champion penalized; methodology labeled "unreliable."

### 2.4 Rushing L5 ClawTeam Before L4 Stabilizes

**Symptoms**: Boss sees multi-agent demo, wants Sales + CS + QC cross-dept Agent Team. Not a single Agent has passed Stage Gate 4A-4E, but 3 Agents are chained. Evidence trail breaks across Agents → no one can trace decisions.

**Root cause**: Single Agent ungoverned → multi-Agent must lose control (no one can pin down which Agent caused which issue).

**Typical ending**: Project dissolves in 6 months; falls back to single Agents; half a year wasted.

---

## 3. Organizational Misfit Failures

### 3.1 No AI Champion (executive driver)

**Precondition**: Every Phase needs at least one Champion who can "coordinate cross-dept, decide, report to Sponsor."

**Failure**: CEO signs Phase A but doesn't designate a Champion → dept heads pass blame during interviews → As-Is incomplete → Phase A quality poor → client doesn't sign Phase B.

**Tiger AI refusal**: If no Champion is in place before Phase B, **consultant should refuse to sign** or require Champion appointment first.

### 3.2 IT Capacity Insufficient for L3+

**Precondition**: L3 Workflow + L4 Agent need 0.5-2 IT FTE for ongoing maintenance.

**Failure**: Company has 1 IT person already maxed on ERP / network / Helpdesk. 5 Workflows go live → no one maintains them → 50% fail in 6 months → staff revert to manual.

**Tiger AI refusal**: If Tool 6.3 Organizational Absorption "IT FTE" < Phase 2 minimum (0.5 FTE dedicated), **strongly advise client to add IT first**.

### 3.3 Insufficient Compliance/Regulation (Sensitive Industries)

**Precondition**: Financial / Healthcare / Government / Legal have strong compliance requirements.

**Failure**: Hospital deploys CS AI without HIPAA / PIPA / patient-rights review → audited 3 months in by Health Ministry → AI pulled, fined, on the news → not only AI plan fails but entire IT governance questioned.

**Tiger AI refusal**: Sensitive industries without dedicated compliance officer / lawyer review → **Phase A end report must mark "compliance unverified → suspend Phase B"**.

### 3.4 Executive Turnover Breaks 24-Month Roadmap

**Precondition**: Phase C 24 months needs stable Sponsor support.

**Failure**: Phase A signed by CEO; CEO departs at Month 9 of Phase C → new CEO disagrees → Phase C frozen → NT$ 9.8M invested, partial outputs (L1-L3) retained but L4-L5 abandoned.

**Tiger AI mitigation**: Phase C quarterly Gate C exit mechanism = even if Sponsor changes, each quarter is independently re-evaluable, not sunk-cost-all-lost.

---

## 4. Known Methodology Limitations

### 4.1 Scoring Model Lacks Psychometric Validation

**Status**: 6 constructs × 0-4 scale and L1-L5 boundaries are **expert consensus**, **not yet validated** via Cronbach's α / EFA / CFA / inter-rater reliability.

**Potential issues**:

- Two consultants scoring the same company may yield L2 vs L3
- "50-60 = L2 boundary vs 41-60 = L2" lacks empirical basis
- Constructs may have collinearity; actual factor count may differ

**Tiger AI response**: Report explicitly marks "expert-consensus version, pending psychometric validation"; `PILOT_STUDY_PROTOCOL.md` plans empirical research; academic submissions should lower claim strength to "a proposed framework."

### 4.2 Case Library Evidence Level

**Status**: 7 cases are **anonymized composites** with Evidence Level 2 (per Tool 8.9).

**Potential issues**: Clients may ask "are these numbers real or fabricated?" ROI ~358%, defect rate 3.2 → 2.0% **cannot be used as contractual commitments for any single client**.

**Tiger AI response**: Each case header marks Evidence Level and Composite nature; SOW uses client's own baseline, not case numbers; gradually replace with real L3-L5 longitudinal cases.

### 4.3 Tiger AI L1-L5 Recognition Still New

**Status**: Tool 2.5 self-qualification 9/10; Condition 6 (broad industry recognition) is △ partial.

**Potential issues**: Initial contacts ask "APQC, SCOR are internationally recognized — by what authority Tiger AI L1-L5?" Academic citations haven't reached critical mass.

**Tiger AI response**: Open-source (Apache 2.0 + GitHub); proactively engage with ISO/IEC working groups / IEEE AI Maturity standards discussions; build joint research with QUT, NTUST.

---

## 5. Consultant-Level Anti-Patterns (Internal Failures)

### 5.1 Skip Phase A → Sign Phase B-C Directly

**Symptoms**: Sales pressure → skip Phase A → sign 6-month engagement directly.
**Result**: No client-signed As-Is / RM / Ideal → in Stage 4+ client can deny "this isn't what we want" → consultant on the defensive.
**Discipline**: **Never skip Phase A**. It is the anchor for everything after.

### 5.2 Draft the Client's Ideal Practice for Them

**Symptoms**: Consultant drafts Ideal Practice for client to sign, to save time.
**Result**: Client doesn't feel ownership → later challenges each item → reasoning chain collapses.
**Discipline**: **Must run Tool 3.6 Co-Creation Workshop 6 steps**. Independent voting, collective consensus, reality check, definition table, 3-party signature — no step can be skipped.

### 5.3 Report Based Only on L1 Self-Report

**Symptoms**: Rush writing → all conclusions from client self-questionnaire.
**Result**: Audited by client's internal audit / parent company → "insufficient evidence" → full project returned.
**Discipline**: Per Tool 8.9 Evidence Hierarchy, **any major conclusion needs L3+ (system log) support**. Each paragraph marks `[E:L#]`.

### 5.4 Mixing Risk Into Gap Analysis

**Symptoms**: Stage 4 chapter mixes "this risk is high, not recommended" subjective judgment.
**Result**: Stage 4 becomes subjective → client challenges "why do you think this is risky" → chapter rewritten.
**Discipline**: **Stage 4 = objective gap inventory, NOT risk assessment**. Risk belongs to Stage 8 Risk Register.

### 5.5 Skipping Quarterly Stage 2 Radar Revisit at Gate C

**Symptoms**: During implementation, focused on PoCs, only reports progress each quarter, no radar revisit.
**Result**: PoCs done but structural completeness unchanged → 24 months later "did we actually improve?" unanswerable.
**Discipline**: **Quarterly Gate C must revisit radar**. Not doing so = consultant negligence.

---

## 6. Hard Refusal Conditions

Tiger AI **should refuse** Phase C signing under these conditions (even if client wants it):

- [ ] **Phase A + B not completed** → no signed Ideal Practice → refuse Phase C
- [ ] **No AI Champion confirmed in place** → refuse Phase C
- [ ] **IT FTE insufficient for target Phase** → strongly recommend delay + add IT first
- [ ] **Sensitive industry without compliance officer / lawyer review** → refuse Phase C
- [ ] **Sponsor not in place (no clear CEO support)** → refuse Phase C
- [ ] **Client wants to skip levels (e.g., skip L1-L3 → L4-L5)** → refuse, require Phase 1 foundation
- [ ] **Budget insufficient for current phase** → refuse, advise scope reduction

---

## 7. Customer Exit Protocol

If any Phase A / B / C fails, Tiger AI commits:

1. **Phase A failure**: Client retains mid-engagement report + interview summaries + radar → **can self-execute or hire next consultant**
2. **Phase B failure**: Full report + signed Ideal Practice table preserved → **can transfer to other consultant**
3. **Phase C mid-failure (quarterly Gate C decision to stop)**: Completed Phases preserved + governance docs preserved + code / Skills / Workflows fully transferred to client (consultant **holds no client assets**)
4. **No hostage-taking of client assets**: per [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) 7 Pillars #1 "Client Hosts"

---

## 8. How to Use This Document

| Role | Use |
| --- | --- |
| **Consultant internal training** | Required onboarding reading; quarterly team review "which failure patterns did we hit last quarter" |
| **Pre-signing with client** | Consultant proactively shares this doc → client trusts "this consultant doesn't only sell success, honestly discusses failure" |
| **Academic submissions** | Cite as evidence of methodology criticality / falsifiability |
| **Regulatory / bid documents** | Attach as risk assessment + mitigation evidence |

> **Honestly discussing failure = highest form of sales skill**. Clients buy not "guaranteed success" but "we know what to do when it fails."

---

License & Citation

This document is Apache License 2.0; may be used, modified, commercialized, provided the [`../NOTICE`](../NOTICE) attribution is preserved.
