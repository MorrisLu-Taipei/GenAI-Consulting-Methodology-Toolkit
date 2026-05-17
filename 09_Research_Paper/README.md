# 09_Research_Paper

Research papers, preprints, and academic deposits derived from the GenAI Consulting Methodology Toolkit.

> Languages: 語言：繁體中文（本檔）｜ English coming with first formal release

---

## 目的 / Purpose

本目錄存放可獨立引用的學術 artefact。每份文件都應該：

- 有明確的 working-paper / preprint / submission 版本標示
- 用 Apache 2.0 授權
- 在準備好的時候 deposit 到 Zenodo（取 DOI）+ SSRN（取得學術圈引用曝光）
- 與 repo 主體保持 traceable 關聯（引用具體檔案、commit hash、DOI）

This directory holds independently citable scholarly artefacts derived from the toolkit. Each document carries explicit version status, uses Apache 2.0, will be deposited to Zenodo (for DOI) and SSRN (for academic discoverability), and traces back to specific files / commits / DOIs in the main repository.

---

## 目錄 / Contents

| File | Type | Status | Target venues |
| --- | --- | --- | --- |
| [`2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md`](2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md) | Working paper | v1.0 draft | Zenodo (DOI) -> SSRN -> ECIS / DESRIST -> CHI / CSCW |
| [`RELEASE_NOTES_v1.0.0.md`](RELEASE_NOTES_v1.0.0.md) | Release notes | Ready for v1.0.0 GitHub tag | GitHub Releases (triggers Zenodo DOI) |

---

## 發表流程 / Publication workflow

1. **Draft phase** -- `.md` working draft authored and reviewed in repo (`/red-team-review`, `/evidence-audit`).
2. **PDF rendering** -- convert `.md` to PDF via `pandoc` for SSRN upload and pre-print archives.
3. **GitHub Release** -- tag `v1.0.0` (or per-paper version) with `RELEASE_NOTES_*.md` as the release body.
4. **Zenodo auto-DOI** -- GitHub-Zenodo webhook mints concept DOI + version DOI within minutes.
5. **CITATION.cff update** -- drop the Zenodo DOIs into `../CITATION.cff` so the repo's "Cite this repository" button surfaces them.
6. **SSRN deposit** -- upload PDF separately to SSRN for management-research discoverability; SSRN gives its own paper ID, complementary to Zenodo DOI.
7. **README badges** -- add DOI badge to all 8 main README files (zh + 7 langs).
8. **Conference / journal submission** -- submit extended versions of the working paper to peer-reviewed venues per the venue ladder in `RELEASE_NOTES_v1.0.0.md`.

---

## 未來論文路線圖 / Forthcoming papers

- **Paper #2** -- *L1-L5: A Generative AI Adoption Maturity Model for Enterprises* -- empirical maturity-model paper, requires 3-5 longitudinal case studies (pilot study protocol in `../90_References/PILOT_STUDY_PROTOCOL.md`). Target: Business Process Management Journal.
- **Paper #3** -- *Cases-as-Benchmarks: A Reproducibility Standard for Industry Case Studies* -- methods paper on the 9-field benchmark format. Target: Information Systems Research methods note, or Journal of Information Technology Case and Application Research.

---

## 引用本目錄文件 / How to cite documents here

See [`../CITATION.cff`](../CITATION.cff) and each paper's front-matter `Suggested citation` block. Once Zenodo DOIs are issued, use the DOI as the primary identifier.

---

## 法務 / Legal

所有發表內容都遵守本 repo 的政策：

- 無真實公司、學校、地名 in fictional cases（City X / XYZ ERP / 某大學 標準）
- 學術引用（如 Rosemann at QUT）保留為合法學術慣例
- AI 貢獻記錄在 Git `Co-Authored-By:` trailer，不被掛名為人類共同作者

All publications here follow the repository's policy: no real company / institution / place names in fictional cases (City X / XYZ ERP convention); legitimate academic citations preserved; AI contributions logged via Git `Co-Authored-By:` trailers, never as human co-authors.
