# Release Notes -- v1.0.0

**Tag:** `v1.0.0`  
**Date:** 2026-05-18  
**License:** Apache License 2.0  
**Author:** Lu, Yeh-Hsing (盧業興; professionally Morris Lu)  
**Affiliations:** Tiger AI (Independent Research); National Kaohsiung University of Science and Technology (NKUST)  
**ORCID:** [0009-0006-5373-0586](https://orcid.org/0009-0006-5373-0586)  
**Contact:** <morrislu@nkust.edu.tw>

---

## What this release is

First DOI-citable release of the **GenAI Consulting Methodology Toolkit** -- an open-source, multilingual, AI-Native methodology for enterprise GenAI adoption. This release marks the artifact's transition from working draft to a citable, version-pinned scholarly artifact.

When this tag is created on GitHub, Zenodo will automatically mint:

- a **concept DOI** (always resolves to the latest version), and
- a **version DOI** specific to v1.0.0.

Both DOIs become permanently citable in academic and industry literature.

---

## What's included

### Methodology core

- **Eight-stage closed-loop consulting flow** with explicit data dependencies, client signature requirements, and quarterly Stage 2 radar loopback as the falsification mechanism.
- **Tiger AI L1-L5 GenAI adoption maturity model**, organized on two orthogonal axes -- scale axis (L1 Chat -> L2 Skill -> L3 Workflow) and AI-autonomy axis (L4 Auto Agent -> L5 Agent Team) -- with a critical boundary at L3 -> L4. Self-qualified at 9/10 conditions per the Tool 2.5 maturity-model qualification scorecard.
- **Four-layer Enterprise AI Reference Model** (Governance / Business / Information / Technical), derived from the abstraction x volatility axis and aligned with TOGAF BDAT, Dragon1 EA, Zachman, and ArchiMate.
- **Three-phase contract model**: Phase A Diagnostic (2 weeks) -> Gate A -> Phase B Strategy (4 weeks) -> Gate B -> Phase C Implementation (24 months) -> Gate C (quarterly). Each Gate is an explicit client-exit point.
- **Cases-as-Benchmarks** -- seven industry case studies (Manufacturing, Hospital, Marketing Agency, B2B Sales, Financial, Government, Education) all conforming to a nine-field reproducible Benchmark format.
- **Toolkit templates** -- 40-question interview bank, scoring rubrics, gap analysis matrices, Stage Gate criteria, Risk Register, Audit Log specification, AI Ethics checklist, and 14-section Consulting Report template.

### Multilingual documentation

Seven languages of substantive methodology documentation: **繁體中文** (source), **English**, **Deutsch**, **Français**, **Español**, **日本語**, **한국어** (with partial **ภาษาไทย** in entry-point files).

### Multi-IDE production environment

Twenty-two specialized AI-IDE workflow specifications across three IDE families:

- `.claude/workflows/` -- 10 workflows for cross-file synthesis, adversarial debate, scenario planning, and reader-as-querier interaction (`/deep-synthesize`, `/devil-pair-debate`, `/socratic-challenge`, `/thought-experiment`, etc.)
- `.codex/workflows/` -- 10 workflows for engineering rigor, consistency audit, evidence verification, and academic upgrade (`/consistency-review`, `/red-team-review`, `/evidence-audit`, etc.)
- `.antigravity/workflows/` -- 2 workflows for parallel multi-agent diagnosis and report drafting.

### Research paper

`09_Research_Paper/2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md` -- a Markdown preprint, *AI-Native eBook Production: Multi-IDE Orchestration as Methodology Engineering Infrastructure*, intended for parallel Zenodo and SSRN deposit. Rendered page count depends on PDF engine, font, and margin settings; the reproducibility manifest gives the canonical rendering command. This preprint situates the entire toolkit within the design science research tradition and offers it as evidence for a new methodology engineering paradigm.

### Citation infrastructure

- `CITATION.cff` -- GitHub-standard Citation File Format metadata; drives the "Cite this repository" UI on GitHub.
- `NOTICE` and `NOTICE.md` -- Apache 2.0 attribution requirements in both ASCII and rich text.
- `LICENSE` -- Apache License 2.0 full text.

---

## Theoretical foundations

The methodology builds on several established academic schools and industry frameworks. Full attribution is in `00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`. Key lineage:

- **Business Process Management Maturity** -- Rosemann & de Bruin (2005); Process Awareness, Alignment, Methods, IT, People, Culture as six enablers.
- **Capability Maturity Model** -- Paulk et al. (1993); CMMI Institute (2018); the five-level maturity convention.
- **Process Classification Framework** -- APQC (2024); cross-industry process taxonomy used for Stage 2 RM mapping.
- **Supply Chain Operations Reference Model** -- APICS / ASCM SCOR; used as alternate RM for manufacturing engagements.
- **Enterprise Architecture frameworks** -- TOGAF (Open Group), Dragon1, Zachman, ArchiMate; the four-layer abstraction x volatility derivation.
- **Consulting methodologies** -- Minto's Pyramid Principle, Rasiel's McKinsey Way, Bain Results Delivery -- incorporated as analytical tools, not replaced.
- **Change management** -- Kotter's eight steps, Hiatt's ADKAR, Mendelow's stakeholder mapping.

---

## What's **not** in this release

We are explicit about scope to set honest reader expectations:

- **No empirical case-study data.** The methodology has been *constructed* with care but not yet *empirically validated* through completed longitudinal client engagements. A pilot study protocol is included (`90_References/PILOT_STUDY_PROTOCOL.md`) but execution is forthcoming.
- **No peer review yet.** Zenodo DOI publication confers a persistent identifier, not peer review. The preprint will be submitted to peer-reviewed venues (target: ECIS / DESRIST short paper; CHI / CSCW full paper; Business Process Management Journal for the maturity-model line).
- **No proprietary client data.** All examples are AI-generated fictional cases (the "Client M / MingChang Packaging" archetype) with abstract location and ERP labels (`City X`, `XYZ ERP`). Real Taiwan companies, institutions, and place names have been systematically removed.

---

## Repository state at this tag

All numbers below are frozen at commit `7da82d7` and reproducible via the commands in `09_Research_Paper/REPRODUCIBILITY.md`. The authoritative snapshot is `09_Research_Paper/RELEASE_MANIFEST_v1.0.0.md` -- if any value here disagrees with the manifest, **the manifest wins**.

| Metric | Value |
| --- | --- |
| Total markdown documents | 354 |
| Substantive source documents (zh primary, non-translation) | 120 |
| Translation siblings (EN/DE/FR/ES/JA/KR/TH) | 234 (78/31/31/31/31/31/1) |
| Specialized AI-IDE workflows | 22 (10 Claude Code + 10 Codex + 2 Antigravity) |
| Git commits at this tag | 94 |
| Industry case studies (Benchmark-grade) | 7 |
| License | Apache 2.0 (see `LICENSE`, `NOTICE`) |
| Commit SHA (full) | `7da82d78aa120258e150a9ce0d9fff60a58f62d7` |

---

## How to cite

After Zenodo mints the DOIs (typically within minutes of this release going public), the canonical citations will be:

**Concept DOI** (always latest version):

> Lu, M. (2026). *GenAI Consulting Methodology Toolkit* (Version 1.0.0) [Software]. Zenodo. DOI pending Zenodo release (resolvable URL: `https://doi.org/10.5281/zenodo.<ID>` once minted).

**Preprint** (in this release):

> Lu, M. (2026). *AI-Native eBook Production: Multi-IDE Orchestration as Methodology Engineering Infrastructure*. Working paper. Tiger AI. Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit/blob/v1.0.0/09_Research_Paper/2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md>.

(Both will be updated with the Zenodo-issued DOI numbers once the webhook fires.)

---

## Acknowledgments

The author acknowledges Prof. Michael Rosemann (Queensland University of Technology) for the long-term intellectual influence of the BPM Maturity school on this work's lineage. All errors, omissions, and AI-domain extensions are the author's sole responsibility.

The toolkit was produced using Anthropic Claude (Opus 4.6, 4.7), OpenAI Codex CLI, and Google Antigravity. AI contributions to specific commits are recorded via `Co-Authored-By:` trailers in the Git history.

---

## Roadmap (post-v1.0.0)

- **v1.1**: completion of pending translations in 01_Assessment, 03_Consulting_Report, 05_Sales (95+ files).
- **v1.2**: addition of `/methodology-test` self-validation results across all 8 stages.
- **v1.3**: first empirical case-study addendum once pilot engagement completes.
- **v2.0**: post-peer-review revision incorporating reviewer feedback from CHI / CSCW / BPM Journal submissions.

Issue tracker, discussions, and pull requests are open on GitHub.
