# Release Notes — v3.0.0 (GitHub software tag)

**Tag:** `v3.0.0`
**Date:** 2026-05-18
**License:** Apache License 2.0
**Author:** Lu, Yeh-Hsing (盧業興; professionally Morris Lu)
**Affiliation:** Tiger AI (Independent Research)
**ORCID:** [0009-0006-5373-0586](https://orcid.org/0009-0006-5373-0586)
**Contact:** <yesinlu@gmail.com>

---

## Versioning clarification (please read first)

This release uses **two version numbers** referring to different concepts:

| Version | What it refers to | Where it lives |
| --- | --- | --- |
| **Software tag `v3.0.0`** | The repository's overall release history (incremented from existing `v2.1.0`) | This GitHub tag |
| **Paper version `v1.0`** | The academic preprint's own revision history (release candidate, first formal deposit) | `09_Research_Paper/2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md` |

The existing tags `v1.0.0` / `v1.1.0` / `v1.2.0` / `v2.1.0` cover the pre-academic-paper toolkit lineage and remain in place unchanged. **This `v3.0.0` GitHub release coincides with the first formal academic deposit (Zenodo + SSRN + arXiv pipeline).**

---

## What this release is

This `v3.0.0` software release is the **first formal academic deposit** of the GenAI Consulting Methodology Toolkit, combining the pre-existing toolkit (carried forward from `v2.1.0`) with a new academic publishing layer:

- A 12-page preprint, *AI-Native eBook Production: Multi-IDE Orchestration as Methodology Engineering Infrastructure — A Design Science Investigation* (EN canonical + ZH companion translation)
- Three-AI-engine evaluation panel ([`AI_Comments.md`](09_Research_Paper/AI_Comments.md) / [`AI_Comments_EN.md`](09_Research_Paper/AI_Comments_EN.md)) with Antigravity / Codex / Claude assessments and explicit conflict-of-interest disclosures
- 4-section reference taxonomy (Academic / Books-methods-industry / Product docs / Author in preparation) + Citation Status Table for reviewer transparency
- [`REPRODUCIBILITY.md`](09_Research_Paper/REPRODUCIBILITY.md) — 9-section manifest with verification commands for every numeric claim in the paper
- [`RELEASE_MANIFEST_v1.0.0.md`](09_Research_Paper/RELEASE_MANIFEST_v1.0.0.md) — frozen snapshot of repository state at the academic deposit point
- [`CITATION.cff`](CITATION.cff) — GitHub-standard citation metadata (DOI fields filled in after Zenodo mints them)

When this GitHub tag is published, the Zenodo webhook will mint:

- a **concept DOI** (always resolves to the latest release), and
- a **version DOI** specific to this `v3.0.0` software release / paper `v1.0` deposit.

Both DOIs become permanently citable in academic and industry literature.

---

## Full release context

For the complete release notes covering the academic paper (intended for Zenodo deposit, including methodology core, theoretical lineage, what is and is not in this release, repository state metrics, and the roadmap), see:

**📄 [`09_Research_Paper/RELEASE_NOTES_v1.0.0.md`](09_Research_Paper/RELEASE_NOTES_v1.0.0.md)** — the canonical paper-level release notes (paper v1.0).

That file is the authoritative reference for everything the academic deposit contains. The present file (`RELEASE_NOTES_v3.0.0.md`) is a short GitHub-tag-specific cover note that exists only to resolve the software-tag vs paper-version dual numbering.

---

## How to cite

After Zenodo mints the DOIs (typically within minutes of this release going public), the canonical citations will be:

**Concept DOI** (always latest version):

> Lu, Y.-H. (2026). *GenAI Consulting Methodology Toolkit* (Version 1.0; software tag v3.0.0) [Software]. Zenodo. DOI pending Zenodo release (resolvable URL: `https://doi.org/10.5281/zenodo.<ID>` once minted).

**Preprint** (in this release):

> Lu, Y.-H. (2026). *AI-Native eBook Production: Multi-IDE Orchestration as Methodology Engineering Infrastructure — A Design Science Investigation*. Working paper (release candidate v1.0). Tiger AI. Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit/blob/v3.0.0/09_Research_Paper/2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md>.

(Both will be updated with Zenodo-issued DOI numbers once the webhook fires.)

---

## Acknowledgments

The author acknowledges Prof. Michael Rosemann (Queensland University of Technology) for the long-term intellectual influence of the BPM Maturity school on this work's lineage. All errors, omissions, and AI-domain extensions are the author's sole responsibility.

The toolkit and this release were produced using Anthropic Claude (Opus 4.6, 4.7), OpenAI Codex CLI, and Google Antigravity. AI contributions to specific commits are recorded via `Co-Authored-By:` trailers in the Git history. A three-AI-engine self-disclosed evaluation of the preprint is included in `09_Research_Paper/AI_Comments.md` (ZH) and `AI_Comments_EN.md` (EN).
