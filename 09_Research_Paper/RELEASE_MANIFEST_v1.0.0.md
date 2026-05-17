# Release Manifest -- v1.0.0

**Frozen at commit:** `7da82d78aa120258e150a9ce0d9fff60a58f62d7` (short: `7da82d7`)
**Date frozen:** 2026-05-18
**Released as:** (pending GitHub tag `v1.0.0` -- this file will be referenced by `RELEASE_NOTES_v1.0.0.md`)
**License:** Apache License 2.0
**Purpose:** Snapshot of all quantitative properties of the artifact at the moment of release, so that subsequent commits cannot retroactively invalidate cited numbers.

This file is the **source of truth** for every numeric claim made in `2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md` v1.0 and in `RELEASE_NOTES_v1.0.0.md`. The reproducibility commands that regenerate these numbers live in `REPRODUCIBILITY.md`.

---

## 1. Repository state

| Property | Value |
| --- | --- |
| Commit SHA (full) | `7da82d78aa120258e150a9ce0d9fff60a58f62d7` |
| Commit SHA (short) | `7da82d7` |
| Commit date | 2026-05-18 |
| Branch | `main` |
| Repository URL | <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit> |
| License | Apache License 2.0 |
| Working-directory subroot | `Deliverable/10_Cosultanting/` |

---

## 2. Document counts (frozen)

| Metric | Value |
| --- | --- |
| Total markdown files in subroot | **352** |
| Substantive source documents (zh primary; excludes `_EN`/`_DE`/`_FR`/`_ES`/`_JA`/`_KR`/`_TH` siblings) | **118** |
| Translation siblings: total | **234** |
| Translation siblings: `_EN` | 78 |
| Translation siblings: `_DE` | 31 |
| Translation siblings: `_FR` | 31 |
| Translation siblings: `_ES` | 31 |
| Translation siblings: `_JA` | 31 |
| Translation siblings: `_KR` | 31 |
| Translation siblings: `_TH` | 1 |

Sum-check: 118 + 234 = **352** -- matches total. The `_EN` count exceeds other languages because earlier release waves completed `_EN` siblings for many files that have not yet received DE/FR/ES/JA/KR translations.

---

## 3. Specialized AI-IDE workflow counts (frozen)

| IDE family | Workflow count | Directory |
| --- | --- | --- |
| Claude Code | **10** | `.claude/workflows/` |
| OpenAI Codex CLI | **10** | `.codex/workflows/` |
| Google Antigravity | **2** | `.antigravity/workflows/` |
| **Total** | **22** | three directories |

### 3.1 Claude Code workflows enumerated

`cross-stage-trace.md`, `deep-synthesize.md`, `devil-pair-debate.md`, `methodology-fork.md`, `parallel-perspectives.md`, `scenario-planning.md`, `simulate-engagement.md`, `socratic-challenge.md`, `theory-bridge.md`, `thought-experiment.md`

### 3.2 Codex workflows enumerated

`academic-upgrade.md`, `bump-version.md`, `consistency-review.md`, `diagnose.md`, `evidence-audit.md`, `generate-report.md`, `generate-traceability.md`, `harvest-insights.md`, `methodology-test.md`, `red-team-review.md`

### 3.3 Antigravity workflows enumerated

`diagnose.md`, `generate-report.md`

---

## 4. Git history snapshot (frozen)

| Metric | Value |
| --- | --- |
| Total commits to `main` at `7da82d7` | **94** |
| First commit date | (see `git log --reverse --format='%ad' --date=short \| head -1`) |
| Most recent commit message | "Add 09_Research_Paper: AI-Native eBook preprint + CITATION.cff + v1.0.0 release notes" |
| Commits with `Co-Authored-By: Claude` trailer | (run `git log --grep='Co-Authored-By: Claude' \| wc -l` to verify) |

---

## 5. Methodology substance (qualitative -- frozen)

These are structural properties of the methodology itself, not file counts. They do not change between commits except by explicit revision.

| Property | Value at v1.0.0 |
| --- | --- |
| Eight-stage flow stages | 8 (Stage 1 As-Is, Stage 2 Reference Model, Stage 3 Best Practice / Ideal Practice, Stage 4 Gap Analysis, Stage 5 Problem Definition, Stage 6 Phased Goals, Stage 7 To-Be Design, Stage 8 Implementation & Change) |
| Maturity model levels | 5 (L1 Chat, L2 Skill, L3 Workflow, L4 Auto Agent, L5 Agent Team) |
| Maturity model axes | 2 (scale axis L1-L3; AI-autonomy axis L4-L5) |
| Enterprise AI Reference Model layers | 4 (L1 Governance, L2 Business, L3 Information, L4 Technical) |
| Contract phases | 3 (Phase A Diagnostic 2 weeks; Phase B Strategy 4 weeks; Phase C Implementation 24 months) |
| Phase gates | 3 (Gate A, Gate B, Gate C; Gate C runs quarterly) |
| Benchmark-grade case studies | 7 (Manufacturing, Hospital, Marketing Agency, B2B Sales, Financial, Government, Education) |
| Case Benchmark format fields | 9 (industry, scale, start L, end L, duration, investment, Wins, Failures, applicability) |
| Source language with substantive coverage | 7 (zh source + EN/DE/FR/ES/JA/KR; partial TH) |

---

## 6. External citations and theoretical lineage (frozen at v1.0.0)

The following external academic sources are explicitly cited in the methodology and constitute its theoretical lineage. The list is closed at v1.0.0; new sources added in v1.1+ will appear in a corresponding `RELEASE_MANIFEST_v1.1.0.md`.

- Rosemann, M., & de Bruin, T. (2005). BPM Maturity Model.
- de Bruin, T., & Rosemann, M. (2007). Delphi technique for BPM capability areas.
- Paulk et al. (1993). Capability Maturity Model for Software, CMU/SEI.
- CMMI Institute (2018). CMMI for Development V2.0.
- APQC (2024). Process Classification Framework Version 7.3.
- APICS / ASCM. SCOR Reference Model.
- TM Forum. eTOM Business Process Framework.
- ISACA. COBIT / ITIL Framework.
- The Open Group. TOGAF Standard 9.2.
- Zachman, J. Zachman Framework.
- Dragon1. Enterprise Architecture Reference Model.
- Minto, B. (2009). The Pyramid Principle.
- Rasiel, E. (1999). The McKinsey Way.
- Bain & Company. Bain Way / Results Delivery.
- Iansiti, M., & Lakhani, K. (2020). Competing in the Age of AI.
- Kotter, J. (1996). Leading Change.
- Hiatt, J. (2006). ADKAR. Prosci.
- Mendelow, A. (1991). Stakeholder Mapping.
- Gartner. AI Maturity Model (multiple revisions 2019-2024).
- Davenport, T., & Mittal, N. (2022). All-in on AI.
- Brynjolfsson, E., & McAfee, A. (2014). The Second Machine Age.
- Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in IS research. MIS Quarterly.
- Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). DSR methodology for IS research. JMIS.
- Becker, J., Knackstedt, R., & Pöppelbuß, J. (2009). Developing maturity models for IT management. BISE.

---

## 7. AI engines used in producing v1.0.0 (frozen)

| Engine | Vendor | Use |
| --- | --- | --- |
| Claude Opus 4.6 | Anthropic | Early-cycle drafting and synthesis |
| Claude Opus 4.7 (1M context) | Anthropic | Cross-file synthesis, adversarial debate, multilingual translation |
| OpenAI Codex CLI | OpenAI | Engineering review, consistency audit |
| Google Antigravity | Google | Parallel multi-agent workflows |

AI co-authorship at the commit level is recorded via `Co-Authored-By:` trailers in the Git history. AI contribution at the file or sentence level is **not** machine-traceable in v1.0.0 -- a known limitation noted in the preprint Section 10.2 ("Provenance as a built-in feature" as a direction for IDE designers).

---

## 8. What will change in v1.1.0 (forward declaration)

The following numeric properties are expected to increase between v1.0.0 and v1.1.0:

| Property | v1.0.0 | v1.1.0 (planned) |
| --- | --- | --- |
| Translation siblings (non-_EN) | 31 each for DE/FR/ES/JA/KR | ~ 60 each (completion of 01_Assessment, 03_Consulting_Report, 05_Sales) |
| Total markdown documents | 352 | ~ 500 |
| Git commits | 94 | (incremental) |
| Workflows | 22 | unchanged |
| Substantive source documents | 118 | unchanged (no new zh source planned) |

If you cite Toolkit numbers in your work, **always pin to a manifest file** (either this v1.0.0 manifest or a successor) rather than to live HEAD, so your citation remains verifiable even as the artifact evolves.

---

## 9. Verification

To independently verify every number in this manifest, follow `REPRODUCIBILITY.md` Sections 1, 2, and 3. If any command in `REPRODUCIBILITY.md` produces a number that does not match the corresponding value here at commit `7da82d7`, please file an Issue.
