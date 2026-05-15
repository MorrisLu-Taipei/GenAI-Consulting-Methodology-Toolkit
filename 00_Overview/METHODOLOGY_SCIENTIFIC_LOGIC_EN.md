# Methodology's Scientific Logic: Why This Report Withstands Debate

> 🌐 中文版本 / Chinese version: [METHODOLOGY_SCIENTIFIC_LOGIC.md](METHODOLOGY_SCIENTIFIC_LOGIC.md)
>
> Apache License 2.0 · Author: Morris Lu · Tiger AI

Last updated: 2026-05-15

---

> **What this document answers**: Why is this methodology designed this way? Why 8 stages, not 5 or 12? Why does data flow this way? Why must cases be Benchmark-grade? **Ultimately**: when clients / boards / regulators challenge it, on what basis does this consulting report stand?
>
> **Core claim**: This methodology is not a collection of consulting experience but a **closed-loop scientific management logic** — every step meets the five conditions of scientific method: observable, quantifiable, reproducible, falsifiable, auditable.

---

## 1. Why Consulting Reports Need "Scientific Argumentative Power"

Common failure scenarios:

| Scenario | Client challenge | Typical consultant answer | Why it fails |
| --- | --- | --- | --- |
| Board questioning | "How do you know we're at L2?" | "Based on our interviews..." | Subjective; unverifiable |
| Internal audit | "Why customer service before sales?" | "In our experience..." | Experience is unauditable |
| Regulatory check | "Who's accountable if AI fails?" | "We have policies..." | Policies without audit chains don't count |
| Switching consultants | "The previous firm said L3; you say L2 — who's right?" | "Different methods" | Non-reproducible = not scientific |

**Tiger AI's design goal**: every such question has a **verifiable number + auditable evidence + reproducible procedure** as answer.

---

## 2. Five Conditions of Scientific Method vs. This Methodology

| Scientific Condition | Definition | How methodology meets it |
| --- | --- | --- |
| **1. Observable** | Conclusions rest on evidence others can see | Stage 1 recordings + system inventory + As-Is Swimlanes; every item timestamped with source |
| **2. Quantifiable** | Conclusions reducible to numbers, not adjectives | Stage 2 radar 0-4 scoring; Stage 4 Impact×Effort scoring; Stage 5 80/20 impact-surface numbers; Stage 8 value tracking 5 dimensions |
| **3. Reproducible** | Different consultants using same method get similar conclusions | Three Reference Models (APQC / SCOR / Tiger AI L1-L5) are public standards; 40-question interview bank; MECE discipline |
| **4. Falsifiable** | Conclusions have explicit refutation conditions | Stage 6 Stage Gate Criteria explicitly list pass/fail; checklists have observable conditions; target missed = hypothesis disproved |
| **5. Auditable** | Process can be independently verified by third parties | Stage 8 Audit Log (LLM calls, permission changes, Skill deploys, Reviewer sign-offs full chain), retention defined |

> **These five conditions are not decorations**. Any consultant conclusion that cannot respond to these five is not scientific management — only experience-sharing.

---

## 3. Why Exactly 8 Stages (Not 5, Not 12)

Reasoning back from scientific method: a defensible AI transformation report **must walk through 5 reasoning actions**, with strict data dependencies between them:

| Reasoning action | Maps to Stage | Skipping causes |
| --- | --- | --- |
| **A. Observe current state** | Stage 1 As-Is | No objective baseline → everything afterward is guessing |
| **B. Apply international coordinates** | Stage 2 Reference Model | No external coordinates → "we're not good enough" is consultant opinion |
| **C. Client expands their own Ideal Practice** | Stage 3 Best Practice | No client-signed target → client can deny the gap |
| **D. Quantify gap** | Stage 4 Gap Analysis | No structured gap → cannot prioritize |
| **E. Converge core problem** | Stage 5 Problem Definition | No 80/20 → "everything is important" = nothing gets done |
| **F. Set absorbable targets** | Stage 6 Phased Goals | No phase decomposition → attempt one-shot perfection = failure |
| **G. Design blueprint** | Stage 7 To-Be Design | No To-Be diagram → Roadmap won't land on org and systems |
| **H. Execute & govern** | Stage 8 Implementation | No change mgmt + value tracking + Audit → blueprint is wallpaper |

**Why exactly 8**: every reasoning action is inseparable; **skipping any one leaves a challenge unanswered**.

- Skip Stage 2 → "What's your standard?" has no answer
- Skip Stage 4 → "Why this before that?" has no answer
- Skip Stage 6 → "Why 9 months not 3?" has no answer
- Skip Stage 8 → "How do you prove it improved?" has no answer

> 5 stages is too coarse (omits Reference Model, Phased Goals, Change Mgmt); 12 stages is too fine (redundant sub-steps). **8 is "the minimum complete debatable reasoning chain."**

---

## 4. Why Data Flows This Way (Scientific reason for each arrow)

```
Stage 1 ──────────► Stage 2 ──────────► Stage 3 ──────────► Stage 4
As-Is              Reference Model     Best Practice         Gap
observed reality    international       client's Ideal       objective gap
                    coordinates         Practice (signed)
                                                              │
                                                              ▼
Stage 8 ◄────────── Stage 7 ◄────────── Stage 6 ◄────────── Stage 5
Implementation      To-Be Design       Phased Goals          Problem
landing + change    future blueprint    absorbable steps      core convergence
                                                              
        ↑                                                     ↓
        └─── Quarterly: revisit Stage 2 radar (closed-loop verification) ───┘
```

#### Why each arrow is causally necessary

| Arrow | Why this direction | Reversing causes |
| --- | --- | --- |
| **Stage 1 → 2** | Must have "reality" before something to compare against "standard" | Reversed: cherry-pick evidence to fit standard |
| **Stage 2 → 3** | Must confirm "structure complete" before discussing "client's Ideal" | Reversed: Ideal skips structural gaps |
| **Stage 3 → 4** | Must have **client-signed Ideal Practice** before computing "Gap = (client Ideal − client As-Is)" | Without client signature, gap = consultant opinion, refutable |
| **Stage 4 → 5** | Must have "all gaps" before 80/20 convergence to "core problem" | Without 4, problem definition = guessing |
| **Stage 5 → 6** | Must lock "core problem" before setting "targets" | Without 5, targets scatter |
| **Stage 6 → 7** | Must have "phased targets" before designing "blueprint" | Without 6, blueprint attempts one-shot |
| **Stage 7 → 8** | Must have "blueprint" before "execution" | Without 7, execution is blind |
| **Stage 8 ↑ Stage 2 (quarterly)** | After execution, revisit "is standard radar rounder?" | Without loopback, PoCs done but structure unverified |

> **This is the scientific meaning of "closed loop"**: not "done is good" but "results can be retroactively verified / falsified."

---

## 5. Why Reference Model Is 4 Layers (Not 3, Not 5)

Derived from maturity's "**abstraction × volatility**" axis (see [`CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 2.7):

| Abstraction | Volatility | Layer | Why it cannot be merged or omitted |
| --- | --- | --- | --- |
| Most abstract | Years | **L1 Governance** | Strategy and policy can't mix with processes (volatility differs 10×) |
| Abstract | Quarters-Years | **L2 Business** | Business functions can't mix with data services |
| Medium | Months-Quarters | **L3 Information** | Data services can't mix with hardware/networks |
| Most concrete | Weeks-Months | **L4 Technical** | Hardware mixed into Business layer locks in tech choices |

**3 layers insufficient**: usually drops L3 Information → data services squeezed into L2 or L4 → loss of focus.
**5 layers excessive**: the extra layer is usually a sub-layer of L2 or L3 → violates MECE.

> **The Dragon1 school insists on 4 layers** for this scientific reason. Tiger AI Enterprise AI Reference Model strictly follows it.

---

## 6. Why Cases Must Be Benchmark-grade (Not Narrative)

Science requires "**reproducibility**" — the same case read by different consultants / clients should yield similar "gap estimates."

- **Narrative case**: "Company X did AI quality inspection and succeeded" → not reproducible (every reader interprets differently)
- **Benchmark-grade case**: 9 mandatory fields (industry + scale + start L + end L + duration + investment + Wins + Failures + applicability) → **reproducible** (any reader's gap/time/budget estimate falls in similar range)

See Tool 3.5 Cases-as-Benchmarks.

> **This is why all 7 Tiger AI cases follow the same 9-field template** — not for visual consistency but for the scientific condition of **reproducibility**.

---

## 7. The Report's "Scientific Argumentative Power" Checklist

When clients / boards / regulators ask the following questions, this methodology has specific answer locations:

| Challenge | Answer location | Evidence |
| --- | --- | --- |
| "How do you know we're at L2?" | §3 As-Is + §4 RM Mapping | Interview recordings, system inventory, RM radar 0-4 |
| "Why APQC / Tiger AI L1-L5?" | §4.1 + Tool 2.5 | 10-condition qualification scorecard |
| "How far are we from our ideal?" | §5 + §6.1 | **Client-signed Ideal Practice definition table** + case Benchmark; Gap = (your signed Ideal − your As-Is), both ends are your statements |
| "Why customer service before sales?" | §6.2 + §6.3 | Impact × Effort matrix + Prioritization Score |
| "Why is the core problem 'knowledge asset-ization'?" | §7 | 80/20 impact-surface numbers + 5 Whys chain |
| "Why 9 months not 3?" | §8 + Tool 6.3 | Phased decomposition + Organizational Absorption (6 dimensions) + benchmark case duration |
| "What if the PoC fails?" | §13.2 | Risk Register + Triggers + Mitigation Owners |
| "How do you prove it improved?" | §13.1 + quarterly radar review | Value Tracking 5 dimensions + Stage 2 radar before/after |
| "Who's accountable if AI fails?" | §12.1 + Tool 8.8 | RACI + AI Ethics Checklist + Audit Log full chain |
| "Can your methodology be reproduced?" | Whole methodology | Apache 2.0 + GitHub + Tool 2.5 self-qualification 9/10 |
| "Last consultant said L3, you say L2 — who's right?" | §3 scoring evidence | Public 0-4 scale + every score has observable evidence → **third-party verifiable** |
| "Why exactly 8 stages?" | This document §3 | "Minimum complete debatable reasoning chain" argument |

> **The report becomes a debatable document**: the client doesn't "trust the consultant's authority" but "follows the evidence chain to reach the same conclusion themselves." That is scientific management.

---

## 8. Comparison with Mainstream Consulting Methodologies

| Methodology | Strength | Missing (from scientific completeness lens) |
| --- | --- | --- |
| **McKinsey Issue Tree + Pyramid** | Rigorous logical reasoning, strong narrative | No Reference Model (no coordinates); no Phased Goals (no phase decomposition) |
| **BCG Digital Maturity** | Clear 5-stage maturity | No quantified Best Practice (excellence described by consultant); no organizational absorption assessment |
| **Gartner AI Maturity** | Industry-recognized | No As-Is interview discipline; no reproducible case Benchmarks |
| **MIT AI Capability** | Academically rigorous | Lacks Implementation & Change landing tools |
| **Tiger AI (this methodology)** | **8-stage complete reasoning chain + 4-layer Reference Model + Cases-as-Benchmarks closed loop** | New (launched 2025, accumulating cases) |

> **Not saying other methodologies are bad** — saying they each have strengths but **incomplete closed loops**. Tiger AI's design goal is to complete that loop so the report has **evidence for every sentence from front cover to last page**.

---

## 9. Academic and Regulatory Citation Worthiness

Why this methodology can be validated, cited, improved by academic communities:

1. **Public**: Apache 2.0, GitHub repo, bilingual zh/en
2. **Self-qualifiable**: Tool 2.5 self-evaluation, 9 of 10 conditions met
3. **Theoretical roots transparent**: Rosemann BPM Maturity school (QUT) + CMMI + APQC + Dragon1 EA each cited
4. **Cross-industry validated**: Manufacturing / Hospital / Marketing / B2B / Financial / Government / Education — 7 industry cases (validates portability)
5. **Falsifiable**: every Stage Gate Criteria has refutation conditions
6. **Critiquable**: this document and Tool 2.5 both explicitly note "new, recognition accumulating"

> **The gold standard of academic citation is "can someone else apply this method to a different problem and get similar conclusions?"** — Tiger AI methodology answers Yes, because all steps, tools, and scoring criteria are public.

---

## 10. Operational Discipline for Consultants

When you write this report, every paragraph must answer:

```
What is the evidence for this statement?           ← Observable
How was this number computed?                       ← Quantifiable
Would another consultant get the same?              ← Reproducible
If this is wrong, what would I see?                 ← Falsifiable
Who has signed off on this process?                 ← Auditable
```

**Answer all 5 → that paragraph is scientific management**.
**Any unanswerable → that paragraph is personal opinion; supplement evidence or delete.**

---

## 11. Promise to Clients

This methodology promises:

1. **Every conclusion has numbered evidence** — Appendices A-G fully traceable
2. **Every number has a computation formula** — no "based on consultant judgment"
3. **Every recommendation has Stage Gate Criteria** — you can verify
4. **Every risk has Trigger + Owner + Mitigation** — you can manage
5. **Every case is Benchmark-grade** — you can self-compute the gap
6. **Every phase end revisits Reference Model radar** — you see structure actually getting rounder

**If any paragraph feels like "consultant authority decides," point it out. We'll add evidence, revise the formula, or delete it.**

---

## 12. Closing: This Methodology Itself Is a Reference Model

A final self-referential observation:

- This methodology applies Tool 2.5's 10 conditions to **self-evaluate**: 9 of 10 met (condition 6 "broad industry recognition" still accumulating)
- This methodology applies Tool 2.6's 5 derivation questions to **self-inventory components**: 8 stages + 4 layers + 5 tracking dimensions all present
- This methodology applies Tool 2.7's 4-layer architecture to **self-organize**: Governance (this doc) + Business (Stages 1-8) + Information (toolkit + cases) + Technical (GitHub repo + AGENTS.md + CLAUDE.md)
- This methodology applies Tool 3.5's Cases-as-Benchmarks to **self-prove reproducibility**: 7 industry cases all follow the 9-field template

> **This is the closed loop of scientific management**: a methodology not only analyzes others, but **can analyze itself with its own tools** — in academia called "self-referential consistency," the hallmark of rigorous theory.

---

## References

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- APQC (2024). *Process Classification Framework Version 7.3*.
- CMMI Institute (2018). *CMMI for Development V2.0*.
- Dragon1 (n.d.). *Enterprise Architecture Reference Model*. <https://www.dragon1.com/reference-models/enterprise-architecture-reference-model>
- Pyramid Principle: Minto, B. (2009). *The Pyramid Principle*.
- 80/20: Koch, R. (1997). *The 80/20 Principle*.
- 5 Whys: Ohno, T. (1988). *Toyota Production System*.
- Change Management: Kotter, J. (1996). *Leading Change*. Prosci ADKAR.

---

License & Citation

This document is Apache License 2.0; may be used, modified, commercialized, provided the [`../NOTICE`](../NOTICE) attribution is preserved.
