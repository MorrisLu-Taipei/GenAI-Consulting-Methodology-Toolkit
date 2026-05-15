# Pilot Study Protocol: Empirical Validation Research Plan for Tiger AI Methodology

> 🌐 中文版本 / Chinese version: [PILOT_STUDY_PROTOCOL.md](PILOT_STUDY_PROTOCOL.md)
>
> Apache License 2.0 · Author: Morris Lu · Tiger AI

Last updated: 2026-05-16
Version: v1.0 Research Design Protocol (pre-registration ready)

---

> **Purpose**: Evolve Tiger AI methodology from a "well-designed consulting framework" into a "researchable model." This protocol defines an 18-24 month, 5-10 enterprise empirical pilot study, **subjecting the methodology to external falsification rather than self-validation alone**.
>
> This is a **research design document** ready for IRB submission / academic pre-registration / government research grant applications.

---

## 1. Background & Motivation

### 1.1 Why Empirical Research

Current evidence strength of Tiger AI methodology:

| Element | Evidence Level (Tool 8.9) | Status |
| --- | --- | --- |
| 8-stage flow design | L2 documentary argument | Complete (Rosemann BPM + industry framework integration) |
| 6 constructs × 0-4 scale | L2 expert consensus | Complete (**no psychometric validation**) |
| 7-case library | L2 anonymized composite | Complete (**not real longitudinal data**) |
| Self-qualification (Tool 2.5) | L1 self-report | Complete (**self-referential, not externally validated**) |
| Inter-rater consistency | — | **Not done** |
| Longitudinal KPI response to methodology | — | **Not done** |

**Conclusion**: The methodology is mature in "internal consistency + logical closure" but has not been empirically tested for "external reproducibility + predictive validity." This pilot study addresses both.

### 1.2 Research Questions

**RQ1 — Inter-rater Reliability**: Can different consultants using the same method score the same company consistently?

- **H1**: Cohen's κ ≥ 0.60 (substantial agreement)

**RQ2 — Internal Consistency**: How internally consistent are the 6 constructs?

- **H2**: Cronbach's α ≥ 0.70 per construct

**RQ3 — Construct Validity**: Do the 6 constructs cleanly emerge in factor analysis?

- **H3a**: EFA extracts 5-6 factors; each item loads ≥ 0.5 on its assigned factor
- **H3b**: CFA 6-factor model fit: CFI ≥ 0.90, TLI ≥ 0.90, RMSEA ≤ 0.08

**RQ4 — Predictive Validity**: Can T0 scores predict T+12 month business KPI improvement?

- **H4**: Controlling for baseline KPI and company size, Tiger AI maturity score positively predicts +12m KPI improvement (β ≥ 0.30, p < 0.05)

**RQ5 — Longitudinal Pattern**: Do enterprises completing Phase C 24 months show "rounder" radars?

- **H5**: T0 vs T24 radar area (6-construct sum) increases significantly, and each construct's growth follows Tool 6.1 decomposition (foundation → optimization → excellence)

---

## 2. Study Design

### 2.1 Design Type

- **Mixed-methods longitudinal study**
- **Convergent parallel design**: quantitative (scale scoring, KPIs) + qualitative (semi-structured interviews, case studies) simultaneously
- **Pre-registered** (public hypotheses, sampling, analysis plan; avoiding p-hacking)

### 2.2 Sample

| Item | Specification |
| --- | --- |
| **Target sample N** | 5-10 enterprises (pilot stage; main study N=200+ for CFA) |
| **Industry diversity** | ≥ 3 industries (≥ 1 each of mfg, services, public sector) |
| **Company size** | 100-5000 employees |
| **AI starting point** | L0-L2 (already L3+ excluded due to limited intervention space) |
| **Commitment duration** | 18 months (research collaboration agreement) |
| **Incentive** | Free / discounted consulting + co-publication opportunity + case anonymization control |

### 2.3 Recruitment Strategy

1. Via n8n Taipei Ambassador community, NTUST Intelligent Manufacturing, QUT alumni
2. Public solicitation + Apache 2.0 open repo as trust signal
3. Signed research collaboration agreement (data use, anonymization, exit mechanism)

### 2.4 Ethics / IRB

- Apply for NTUST or QUT IRB approval
- Informed consent: all participants in writing
- Sensitive data handling: PII / business secret grading; double-blind data isolation
- Right to withdraw: any enterprise may exit at any time; collected data returned or destroyed

---

## 3. Double-Blind Scoring Design

### 3.1 Purpose

Validate **inter-rater reliability** of Tiger AI scoring model.

### 3.2 Design

```
T0 Scoring Phase (per enterprise):
  ↓
  Consultant A independently completes:
    • Interviews (Tool 1.1 40-Q bank)
    • Inventory + Swimlane (Tools 1.2-1.4)
    • Reference Model Mapping (Tool 2.2)
    • 6-construct 0-4 scoring (Tool 2.3)
    • Primary maturity judgment (L1-L5)
  ↓
  Consultant B independently completes (same enterprise, blinded to A):
    • Repeat all above actions
  ↓
  Research analyst (neutral) compares A vs B:
    • 6-construct score gap (weighted kappa)
    • Primary maturity judgment agreement (unweighted kappa)
    • Gap identification overlap (M/B/R table overlap)
```

### 3.3 Consistency Statistics

| Metric | Tool | Interpretation |
| --- | --- | --- |
| **Cohen's κ (unweighted)** | κ = (Po - Pe) / (1 - Pe) | < 0.20 slight; 0.21-0.40 fair; 0.41-0.60 moderate; 0.61-0.80 substantial; > 0.80 almost perfect |
| **Weighted κ (linear / quadratic)** | For ordinal scale (0-4) | Same as above, but stricter on "1 point off" vs "4 points off" |
| **ICC (Intraclass Correlation)** | Two-way mixed model | < 0.5 poor; 0.5-0.75 moderate; 0.75-0.9 good; > 0.9 excellent |
| **Bland-Altman plot** | Visualize score gap | Detect systematic bias |

---

## 4. Longitudinal KPI Tracking

### 4.1 KPI Measurement Timepoints

| Timepoint | Name | Measurement |
| --- | --- | --- |
| **T0** | Baseline | After Phase A, before Phase B |
| **T+6m** | Phase 1 end | L1 Gate acceptance |
| **T+12m** | Mid Phase 2 | L2/L3 Gate |
| **T+18m** | Phase 2 end | L3 complete |
| **T+24m** | Phase 3 end | L4/L5 Gate |

### 4.2 5 KPI Dimensions (per Tool 8.5 Value Tracking)

| Dimension | Example KPIs |
| --- | --- |
| **Time** | Complaint response, proposal turnaround, month-end close, decision cycle |
| **Quality** | Defect rate, error rate, complaint count, rework rate |
| **Scale** | Throughput, beneficiaries, automated task count |
| **Risk** | Missed case rate, compliance violations, sensitive-data leakage |
| **Assets** | Skill count, Wiki entries, Agent task count, training completion |

### 4.3 KPI Data Quality (per Tool 8.9 Evidence Hierarchy)

- **L3 mandatory**: All time / scale KPIs from system logs (n8n / Audit Log / ERP)
- **L4 recommended**: Sample-verified by internal audit / external accountants
- **L1-L2 supplementary**: Employee NPS / interview summaries

---

## 5. Qualitative: Semi-Structured Interviews

### 5.1 Interview Timepoints

Per enterprise: T0, T+6m, T+12m, T+18m, T+24m — 1 round each (per interviewee).

### 5.2 Interviewees

- CEO / Sponsor
- AI Champion
- IT Lead
- ≥ 2 Department Heads
- ≥ 3 Front-line Users

### 5.3 Interview Questions (Excerpt)

1. What's the most impactful AI change in the past 6 months?
2. Which expected AI changes didn't happen? Why?
3. Has staff / department attitude toward AI shifted?
4. Would you recommend / not recommend this methodology to peers?
5. Which Stage / Tool was most useful? Least?
6. Cross-time: looking back at the Ideal Practice signed 12 months ago, any regrets?

### 5.4 Qualitative Analysis

- Verbatim transcription + coding (NVivo / Atlas.ti)
- Dual-coder reliability ≥ 80%
- Thematic analysis to extract patterns / counter-examples

---

## 6. Statistical Analysis Plan

### 6.1 Descriptive Statistics

- Score distribution per construct (mean, SD, median, IQR)
- Radar chart T0 vs T24 visualization
- 6-construct correlation matrix (multicollinearity check)

### 6.2 Reliability & Validity

| Analysis | Tool | Maps to Hypothesis |
| --- | --- | --- |
| Cronbach's α | SPSS / R `psych::alpha()` | H2 |
| EFA + Bartlett's + KMO | SPSS / R `psych::fa()` | H3a |
| CFA + fit indices | Mplus / R `lavaan::cfa()` | H3b (**N ≥ 200 required**) |
| Cohen's κ | R `irr::kappa2()` | H1 |
| ICC | R `irr::icc()` | H1 |

### 6.3 Inferential Statistics

| Analysis | Hypothesis | Tool |
| --- | --- | --- |
| Paired t-test (T0 vs T24) | H5 radar area increase | R `t.test(paired=TRUE)` |
| Mixed-effects model | H4 predictive validity | R `lme4::lmer()` |
| ANCOVA | Control baseline KPI + size | R `aov()` |
| Sensitivity analysis | Against missing data + dropout | R `mice` multiple imputation |

### 6.4 Significance & Adjustment

- α = 0.05 main test
- Bonferroni correction for multiple comparisons
- Effect size reporting: Cohen's d, η², partial η²

---

## 7. Timeline & Milestones

```
Month 0:    Finalize design + IRB submission
Month 1-3:  Recruit 5-10 enterprises + sign research agreement
Month 4:    Train Consultant A/B (double-blind SOP)
Month 5-6:  T0 double-blind scoring + Baseline KPI measurement
Month 6-12: Phase 1 intervention + T+6m scoring + interviews
Month 12-18: Phase 2 intervention + T+12m + T+18m
Month 18-24: Phase 3 intervention + T+24m final scoring + interviews
Month 24-27: Analysis + research report + journal submission
Month 27-30: Revisions + submission
```

---

## 8. Budget Estimate

| Item | Est. (NT$) |
| --- | --- |
| Consultant time (A + B 80-120 hrs each per company) | 6-9M |
| Research staff (neutral scoring comparison + qualitative analysis) | 1.5-2.5M |
| KPI system-log tools + interview transcription | 0.5-1M |
| IRB / legal / statistical consultant | 0.5-1M |
| Open-source tools + cloud data store | 0.3-0.5M |
| Contingency (15%) | 1.3-2M |
| **Total** | **NT$ 10.1-16M** |

⚠️ In exchange for free consulting, 5-10 enterprises commit to 18 months of data collection → consultant labor offsetable by "equivalent consulting service", **actual cash outlay reducible to NT$ 4-7M**.

---

## 9. Publication Strategy

### 9.1 Expected Outputs

| Output | Journal / Platform | Est. Timing |
| --- | --- | --- |
| **Pre-registration** | OSF | Month 0 |
| **Protocol paper** | BMJ Open / Pilot and Feasibility Studies | Month 3 |
| **Methodology paper** | MIS Quarterly / Information Systems Research / Journal of Business Research | Month 27 |
| **Industry white paper** | Bilingual, public Apache 2.0 | Month 27 |
| **Case studies (anonymized)** | HBR-style cases | Month 30 |
| **Practitioner guide** | Update toolkit + add empirical evidence | Month 30 |

### 9.2 Open Science Commitment

- All research data (de-identified) public on OSF
- Statistical R / Python scripts on GitHub
- Interviewee identity confidential; aggregate results fully transparent

---

## 10. Risks & Mitigation

| Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- |
| Enterprise mid-withdrawal (dropout) | Med | High | Over-recruit 12; intention-to-treat analysis |
| Consultant A/B bias / leakage | Low | High | SOP training + audits + strict double-blind + different offices |
| KPI system log inaccessible | Med | Med | T0 IT confirms log availability; substitute indicators if not |
| IRB review delay | Med | Med | Month 0 IRB submission concurrent with recruitment |
| Insufficient N for CFA | High | Med | EFA at pilot; CFA awaits main study N=200+ |
| Budget shortfall | Med | High | Apply NSTC / MOE / QUT grants; multi-enterprise cost-sharing |

---

## 11. Stopping Rules

Early termination with full disclosure if:

- ≥ 50% enterprises withdraw
- Inter-rater κ < 0.40 (methodology inconsistent → scale needs redesign)
- IRB revoked
- Serious ethics issues (data leak, participant harm)

**Early-terminated studies must still publish all collected data** (avoiding publication bias).

---

## 12. Expected Contributions

| Contribution | Audience | Form |
| --- | --- | --- |
| **Theory**: first empirically validated GenAI adoption maturity model | Academia (IS / BPM / Strategy) | Peer-reviewed paper |
| **Method**: Cases-as-Benchmarks + Client Ideal Practice workshop protocol | Consulting industry | Open-source toolkit (Apache 2.0) |
| **Policy**: empirical evidence for AI Governance alignment | Regulators (Taiwan AI Basic Act / NIST / EU) | White paper + legislative hearings |
| **Industry**: 5-10 enterprise real longitudinal cases | Peer clients | Real cases (replacing composites) |
| **Education**: integrate into NTUST / QUT curricula | Students | Course materials |

---

## 13. Related Documents

| Document | Relationship |
| --- | --- |
| [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) §3.1-3.3 | Scale construct definitions; this study validates |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Why methodology needs empirical validation |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | Known failure modes → mitigation built into this study |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9 | Evidence Hierarchy basis for KPI evidence grading |

---

## 14. References

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297-334.
- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- Streiner, D. L., Norman, G. R., & Cairney, J. (2015). *Health measurement scales: A practical guide to their development and use* (5th ed.). Oxford University Press.
- Hair, J. F., et al. (2019). *Multivariate Data Analysis* (8th ed.). Cengage.
- Creswell, J. W. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). SAGE.
- Open Science Framework: <https://osf.io/>

---

License & Citation

This document is Apache License 2.0; may be used, modified, commercialized, provided the [`../NOTICE`](../NOTICE) attribution is preserved. Other research teams may **freely adopt, modify, replicate** this design, provided they follow the same pre-registration and open-science commitments.
