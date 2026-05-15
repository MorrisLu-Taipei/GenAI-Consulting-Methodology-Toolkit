# Academic Theoretical Foundations: Tiger AI Methodology's Seven Theoretical Pillars

> 🌐 中文版本 / Chinese version: [ACADEMIC_THEORETICAL_FOUNDATIONS.md](ACADEMIC_THEORETICAL_FOUNDATIONS.md)
>
> Apache License 2.0 · Author: Morris Lu · Tiger AI

Last updated: 2026-05-16

---

> **Purpose**: Consolidate Tiger AI methodology's academic theoretical foundations scattered across files into **one authoritative document**. When any scholar / regulator / serious consultant asks "what's the theoretical basis", this document is the answer.
>
> **Core claim**: Tiger AI methodology is not merely consulting practice but a **engineered integration of seven theories**.

---

## 1. Theory Map Overview

| Theory | Founder / Classic Reference | Core Problem Solved | Tiger AI Mapping |
| --- | --- | --- | --- |
| **Capability Maturity & BPM Maturity** | Paulk et al. (1993) CMMI; Rosemann & de Bruin (2005) | How to structurally score organizational capability? | L1-L5 + Stage 2 scoring |
| **Absorptive Capacity** | Cohen & Levinthal (1990) | Why do organizations differ so much in **absorbing** new capability? | Tool 6.3 Organizational Absorption Assessment |
| **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | Which tasks suit / don't suit AI? | Stage 7 To-Be Design (not every dept should reach L5) |
| **Dynamic Capabilities** | Teece et al. (1997); Teece (2007) | How does an organization **rapidly adapt to external change**? | Stage 7 + Stage 8 (from static automation to dynamic capability) |
| **Sociotechnical Systems & Trust in AI** | Bostrom & Heinen (1977); Dietvorst et al. (2015); Glikson & Woolley (2020) | Why is human-AI collaboration hard? Algorithm aversion / complacency | Stage 8 Change Management + HITL |
| **Real Options Theory** | Dixit & Pindyck (1994); McGrath (1997) | How to value high-uncertainty AI strategic investment? | Stage 8 §13 Value Tracking + ROI |
| **AI-Native Living Book / Executable Knowledge Artifact** | Knuth (1984); Anderson et al. (1995); this author (2026) | Can the methodology itself be executable by AI? | AGENTS.md + AI_NATIVE_LIVING_BOOK |

---

## 2. Capability Maturity & BPM Maturity

### 2.1 Theory Summary

- **CMMI**: Paulk et al. (1993) at SEI defined 5-level organizational capability (Initial / Repeatable / Defined / Managed / Optimizing)
- **BPM Maturity Model**: Rosemann & de Bruin (2005, QUT) extended maturity to Business Process Management, adding 6 enablers: Process Awareness / Alignment / Methods / IT / People / Culture

### 2.2 Contribution to Tiger AI

- **L1-L5 two axes** inherit BPM Maturity's "Process Awareness → Optimization" logic, adding GenAI-era essential "**Scale axis + AI Autonomy axis**" dual structure
- **0-4 scale + BARS behavioral anchors** stem from this school
- **Stage Gate Criteria** = CMMI's "Process Areas" + phase acceptance

### 2.3 Mapped Files

- [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §3.0 two-axis story
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) L1-L5 definitions
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) Behavioral anchors

---

## 3. Absorptive Capacity

### 3.1 Theory Summary

- **Cohen & Levinthal (1990)** in *Administrative Science Quarterly*: an organization's "**ability to identify, assimilate, and apply external knowledge**" determines its innovation capacity
- Core elements: **Prior Knowledge + Internal Knowledge Flow**
- Zahra & George (2002) further split into 4 dimensions: Acquisition / Assimilation / Transformation / Exploitation

### 3.2 Contribution to Tiger AI

- Explains why **the same AI opportunity yields wildly different results** across companies — the difference is absorptive capacity
- Tool 6.3 Organizational Absorption Assessment directly maps to this theory
- Reinforces "**why levels cannot be skipped**": skipping L1-L3 → insufficient absorptive capacity → L4-L5 will fail (see [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) §2)

### 3.3 Specific Enhancement to Tool 6.3

Original Tool 6.3 6 dimensions (Budget / Champion / IT FTE / Governance / Literacy / Change capacity) **add 2 new dimensions**:

| New Dimension | Assessment Questions | Score |
| --- | --- | --- |
| **Prior Knowledge** | Does company have: (a) past BPM / Lean / Six Sigma experience? (b) any past AI / ML / RPA attempts? (c) internal software dev capability? | 0-4 |
| **Internal Knowledge Flow** | Between depts: (a) routine cross-dept reviews? (b) shared document platform? (c) internal mentor / instructor system? | 0-4 |

→ High Prior Knowledge + High Knowledge Flow companies can handle more aggressive Phase 1/2/3; conversely, must extend timelines.

### 3.4 References

- Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128-152.
- Zahra, S. A., & George, G. (2002). Absorptive capacity: A review, reconceptualization, and extension. *Academy of Management Review*, 27(2), 185-203.

---

## 4. Task-Technology Fit (TTF)

### 4.1 Theory Summary

- **Goodhue & Thompson (1995)** in *MIS Quarterly*: the degree to which technology improves performance depends on the **"task demand ↔ tech capability"** fit
- Task classification: **Routine (repetitive, predictable) vs Non-routine (judgment-heavy, creative)**

### 4.2 Contribution to Tiger AI

**Not every department should reach L5**. Determine each dept's appropriate L-level endpoint by task characteristics:

| Task Type | Appropriate Endpoint | Rationale |
| --- | --- | --- |
| Highly Routine (CS FAQ, invoice classification) | L3-L4 | High AI fit; low HITL cost |
| Medium Routine + partial judgment (sales proposals, month-end anomalies) | L2-L3 + HITL | AI drafts + human confirms; balances efficiency and risk |
| Highly Non-routine (M&A evaluation, strategic decisions) | L1-L2 (personal assistant) | AI assists, humans lead; pushing L4-L5 harms judgment quality |
| Highly compliance-sensitive (legal, medical diagnosis) | L2-L3 + strong HITL | Regulatory risk too high; L4-L5 unsuitable |

### 4.3 Mapped Files / Tools

- Stage 7 Tool 7.2 Human-AI Collaboration → TTF matrix decides AI involvement per process
- Add **TTF Assessment Worksheet** to Tool 6.3 → score TTF per dept, determine Ideal L-level

### 4.4 References

- Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. *MIS Quarterly*, 19(2), 213-236.
- Zigurs, I., & Buckland, B. K. (1998). A theory of task/technology fit and group support systems effectiveness. *MIS Quarterly*, 22(3), 313-334.

---

## 5. Dynamic Capabilities

### 5.1 Theory Summary

- **Teece, Pisano & Shuen (1997)** in *Strategic Management Journal*: competitive advantage stems from "**integrating, building, reconfiguring internal and external resources**"
- **Teece (2007)** breaks down into three micro-foundations:
  1. **Sensing**: identifying opportunities and threats
  2. **Seizing**: decision and resource allocation
  3. **Transforming**: organizational reconfiguration to leverage opportunities

### 5.2 Contribution to Tiger AI

**From static automation → dynamic adaptive capability**. Tiger AI doesn't just AI-ify existing APQC processes but **builds clients' new capability to continually adapt to external change**:

| Dynamic Capability | Tiger AI Mapping |
| --- | --- |
| **Sensing** | L3 Workflow + L4 Agent continuously monitor market / customer / process signals |
| **Seizing** | Phase 1/2/3 decomposition = converting sensed signals to concrete investment decisions |
| **Transforming** | L5 Multi-Agent Organization + quarterly Gate C radar = continuous org reconfiguration |

### 5.3 Specific Enhancement to Stage 7

Add **Dynamic Capability Worksheet** to Stage 7 To-Be Design:

```
Per Teece (2007) three micro-foundations, each To-Be design must answer:

1. Sensing: What external signal does this AI design help the company "sense"?
   E.g., complaint Agent monitors customer satisfaction trends
2. Seizing: How fast can the company "seize" when signals appear?
   E.g., Quick Win complaint response 5d → 1d compresses customer-loss window
3. Transforming: How does this AI enable organizational "self-reconfiguration"?
   E.g., L5 ClawTeam cross-dept = org no longer depends on specific senior staff
```

→ A To-Be that doesn't answer these 3 is just "automating status quo," not real transformation.

### 5.4 References

- Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal*, 18(7), 509-533.
- Teece, D. J. (2007). Explicating dynamic capabilities. *Strategic Management Journal*, 28(13), 1319-1350.

---

## 6. Sociotechnical Systems & Trust in AI

### 6.1 Theory Summary

- **Sociotechnical Systems Theory** (Bostrom & Heinen, 1977): organizational performance = joint output of **social system + technical system**; cannot optimize either alone
- **Algorithm Aversion**: Dietvorst, Simmons & Massey (2015) in *JEP*: people **prefer worse human judgment to algorithms after seeing the algorithm err**, even when knowing the algorithm is more accurate
- **Automation Complacency**: Parasuraman & Manzey (2010): over-trust in automation causes loss of vigilance, leading to larger incidents
- **Trust in AI**: Glikson & Woolley (2020) integrate cognitive + emotional trust

### 6.2 Contribution to Tiger AI

The real challenge of human-AI collaboration is not only "fear of replacement," but also:

1. **Algorithm Aversion**: after AI's first error, staff collectively reject it → common after L3-L4 launch
2. **Automation Complacency**: staff stop reviewing → HITL fails → larger incidents
3. **Accountability ambiguity**: who's responsible when AI errs? Staff fear blame → psychological safety gap
4. **Professional identity reshaping**: from "Doer" to "Reviewer" → cognitive load and sense of achievement shift

### 6.3 Enhancement to Stage 8 Change Management

Add 2 new resistance types to Tool 8.2:

| Resistance Type | Typical Signal | Handling |
| --- | --- | --- |
| **Algorithm Aversion** | Collective rejection after one AI error | Transparency on error rates (human vs AI) + gradual trust-building (start with low-risk scenarios) |
| **Automation Complacency** | Staff approve without reviewing | Mandatory random sampling in Reviewer Workflow + re-training after errors detected |

### 6.4 Enhancement to HITL Design (Tool 7.2)

Add **psychological safety and accountability columns**:

| Process | HITL Node | **Accountability Statement** | **Psychological Safety** |
| --- | --- | --- | --- |
| CS reply | 100% human review before send | AI draft responsibility = AI Champion; final reply responsibility = CS staff | Staff have right to "reject without review if AI is wrong" without blame |
| Process root cause | 100% human review before action | AI hypothesis responsibility = Agent developer; action responsibility = process manager | Manager has formal SOP to "reject AI suggestion" |

### 6.5 References

- Bostrom, R. P., & Heinen, J. S. (1977). MIS problems and failures: A socio-technical perspective. *MIS Quarterly*, 1(3), 17-32.
- Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion. *JEP: General*, 144(1), 114-126.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3), 381-410.
- Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence. *Academy of Management Annals*, 14(2), 627-660.
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *ASQ*, 44(2), 350-383.

---

## 7. Real Options Theory

### 7.1 Theory Summary

- **Dixit & Pindyck (1994)** in *Investment Under Uncertainty*: high-uncertainty investment value = immediate execution value + **"future optionality" value**
- **McGrath (1997)** applied to strategy: "**today's investment preserves the right to expand in the future**"
- Counters NPV underestimation under uncertainty: NPV assumes certainty, but managerial flexibility has high value under uncertainty

### 7.2 Contribution to Tiger AI

L4-L5 high-uncertainty AI investment is **necessarily underestimated by traditional NPV / IRR** (because 18-24 month cash flows are uncertain). Real Options provides better framing:

| Investment | NPV View (underestimates) | Real Options View (justified) |
| --- | --- | --- |
| Phase 1 Foundation (NT$ 2.8M) | Cash flow unclear → NPV ≈ 0 | Buying the "**option to rapidly expand L4-L5 in future at lower cost**", worth far more than NT$ 2.8M |
| L1 whole-company Chat AI | Short-term ROI unclear | Employee AI literacy = **foundational asset for all future AI applications** |
| L2 Skill Library | ROI invisible | Knowledge codification = company's option to "**plug in multiple AI applications simultaneously**" in future |
| L4 Hermes Agent Pilot | Is one Agent worth it? | Pilot = learning L4 = option to L5 ClawTeam |

### 7.3 Real Options Valuation (Simplified Black-Scholes)

For L4-L5 investments, estimate via:

```
Option Value = max(0, future_payoff - exercise_cost)

Where:
  future_payoff = revenue from exercising option (e.g., expanding to L5)
  exercise_cost = cost when exercising (e.g., Phase 3 investment)
  volatility (σ) = market / tech uncertainty
  time-to-expiration = opportunity window
```

⚠️ No need for exact Black-Scholes; **narrative-level argument is enough to convince CFO** to justify "short-term invisible ROI but long-term valuable" investment.

### 7.4 Enhancement to Stage 8 §13 Value Tracking

Original 5 dimensions (Time / Quality / Scale / Risk / Assets), **add 6th dimension**:

| Dimension | Content |
| --- | --- |
| **Strategic Options** | What "**future exercise right**" did this investment preserve? E.g., L1 foundation → can rapidly expand L4 in future; L2 Skill Library → can plug in any future Agent; L3 Workflow → can integrate any new system |

### 7.5 References

- Dixit, A. K., & Pindyck, R. S. (1994). *Investment Under Uncertainty*. Princeton University Press.
- McGrath, R. G. (1997). A real options logic for initiating technology positioning investments. *Academy of Management Review*, 22(4), 974-996.
- Trigeorgis, L. (1996). *Real Options*. MIT Press.

---

## 8. AI-Native Living Book as Executable Knowledge Artifact

### 8.1 Theory Summary

- **Literate Programming**: Knuth (1984) argued code and docs should integrate into a single "human-readable + machine-executable" document
- **Intelligent Tutoring Systems (ITS)**: Anderson et al. (1995) designed AI as personalized tutoring systems
- **Open Educational Resources (OER) + AI**: contemporary trend combining open materials with AI as interactive knowledge systems

### 8.2 Contribution to Tiger AI

This methodology itself is a **practical case** of this theory:

- repo + AGENTS.md = **executable knowledge artifact**
- AI co-reading tutor = **adaptive ITS** applied to adult professional education
- Client conversing with methodology = customized OER

See [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) for full discussion.

### 8.3 References

- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society*. Harvard University Press.

---

## 9. How the 7 Theories Cooperate: Tiger AI's Integrated Model

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   [Capability Maturity]  ────►  L1-L5 structured scoring          │
│         │                                                        │
│         ▼                                                        │
│   [Absorptive Capacity] ────►   why companies differ in absorbing │
│         │                                                        │
│         ▼                                                        │
│   [Task-Technology Fit] ────►  which tasks at which L?            │
│         │                                                        │
│         ▼                                                        │
│   [Dynamic Capabilities]────►  L3-L5 not just automation but     │
│         │                       building adaptive capability     │
│         ▼                                                        │
│   [Sociotechnical Trust]────►  real human-AI collaboration       │
│         │                       challenges (trust, accountability)│
│         ▼                                                        │
│   [Real Options]        ────►  justifying L4-L5 strategic        │
│         │                       investment under uncertainty     │
│         ▼                                                        │
│   [AI-Native Living Book]──►   methodology itself executable     │
│                                                                  │
└────────────────────────────────────────────────────────────────┘

7 theories aren't isolated layers but a complete chain:
scoring → absorption → matching → adaptation → trust → investment → execution
```

---

## 10. Academic Submission Recommendations

Per these 7 theories, multiple papers can be derived:

| Paper Title (suggested) | Main Theory | Target Journal |
| --- | --- | --- |
| A GenAI Adoption Maturity Model: Extending BPM Maturity for the LLM Era | Capability Maturity + AI-native | MIS Quarterly / Information Systems Research |
| Absorptive Capacity in Enterprise AI Adoption: Empirical Evidence from 7 Industries | Absorptive Capacity | Strategic Management Journal |
| Task-Technology Fit Beyond Routine Work: When Should Departments Adopt L4-L5 Agents? | TTF | Information & Management |
| From Automation to Dynamic Capability: How AI Reshapes Organizational Sensing | Dynamic Capabilities | Strategic Management Journal |
| Algorithm Aversion in Workflow Automation: A Mixed-Methods Study | Sociotechnical / Trust | Organization Science |
| Valuing AI Foundation Investments as Real Options | Real Options | SMJ / California Management Review |
| AI-Native Living Books: Methodology as Executable Knowledge Artifact | AI-Native LB | Communications of the ACM |

---

## 11. Full Bibliography

See §3-8 for per-theory references and the complete bibliography in the Chinese version.

---

License & Citation

This document is Apache License 2.0; may be used, modified, commercialized, provided the [`../NOTICE`](../NOTICE) attribution is preserved.
