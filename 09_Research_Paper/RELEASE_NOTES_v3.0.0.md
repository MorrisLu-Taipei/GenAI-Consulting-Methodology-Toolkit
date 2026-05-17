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

**Zenodo deposit status:** ✅ deposited (under software tag `v3.0.1`; see below).

- **Concept DOI (all versions):** [10.5281/zenodo.20261680](https://doi.org/10.5281/zenodo.20261680)
- **Version DOI (v3.0.1 = paper v1.0):** [10.5281/zenodo.20261681](https://doi.org/10.5281/zenodo.20261681)
- **Deposit triggered by:** `v3.0.1` GitHub release (the Zenodo-GitHub webhook was not yet enabled when `v3.0.0` was published, so `v3.0.1` was created with identical content to trigger the Zenodo deposit). See `RELEASE_NOTES_v3.0.1.md` content on the [v3.0.1 GitHub release page](https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit/releases/tag/v3.0.1) for full context.

Both DOIs are permanently citable in academic and industry literature.

---

## Full release context

For the complete release notes covering the academic paper (intended for Zenodo deposit, including methodology core, theoretical lineage, what is and is not in this release, repository state metrics, and the roadmap), see:

**📄 [`09_Research_Paper/RELEASE_NOTES_v1.0.0.md`](09_Research_Paper/RELEASE_NOTES_v1.0.0.md)** — the canonical paper-level release notes (paper v1.0).

That file is the authoritative reference for everything the academic deposit contains. The present file (`RELEASE_NOTES_v3.0.0.md`) is a short GitHub-tag-specific cover note that exists only to resolve the software-tag vs paper-version dual numbering.

---

## How to cite

After Zenodo mints the DOIs (typically within minutes of this release going public), the canonical citations will be:

**Concept DOI** (always latest version):

> Lu, Y.-H. (2026). *GenAI Consulting Methodology Toolkit* (Version 1.0; software tag v3.0.1, identical content to v3.0.0) [Software]. Zenodo. <https://doi.org/10.5281/zenodo.20261680> (concept DOI; resolves to latest version).

**Preprint** (in this release):

> Lu, Y.-H. (2026). *AI-Native eBook Production: Multi-IDE Orchestration as Methodology Engineering Infrastructure -- A Design Science Investigation*. Working paper (release candidate v1.0; deposited at software release v3.0.1). Tiger AI. Zenodo. <https://doi.org/10.5281/zenodo.20261680>.

Source URL: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit/blob/v3.0.1/09_Research_Paper/2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md>.

---

## Acknowledgments

The author acknowledges Prof. Michael Rosemann (Queensland University of Technology) for the long-term intellectual influence of the BPM Maturity school on this work's lineage. All errors, omissions, and AI-domain extensions are the author's sole responsibility.

The toolkit and this release were produced using Anthropic Claude (Opus 4.6, 4.7), OpenAI Codex CLI, and Google Antigravity. AI contributions to specific commits are recorded via `Co-Authored-By:` trailers in the Git history. A three-AI-engine self-disclosed evaluation of the preprint is included in `09_Research_Paper/AI_Comments.md` (ZH) and `AI_Comments_EN.md` (EN).
