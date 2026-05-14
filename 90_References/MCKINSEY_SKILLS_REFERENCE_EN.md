# mckinsey-consultant-skills — Citation & License Notice

> 🌐 中文版本 / Chinese version: [MCKINSEY_SKILLS_REFERENCE.md](MCKINSEY_SKILLS_REFERENCE.md)

The production workflow in this methodology's [`03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) is referenced from and rewritten based on **Kafurtan/mckinsey-consultant-skills**. This document records the upstream source, license terms, citation guidance, and scope of adaptation.

---

## 1. Upstream Project

| Field | Value |
| --- | --- |
| **Project** | mckinsey-consultant-skills (V3.1) |
| **Maintainer** | @Kafurtan |
| **GitHub URL** | <https://github.com/Kafurtan/mckinsey-consultant-skills> |
| **License** | **MIT License** |
| **Form** | AI agent skill (`SKILL.md` + `references/`) |
| **Content** | An 8-step workflow that automates "business problem → McKinsey-style presentation," end-to-end in 90-110 minutes |

## 2. What mckinsey-consultant-skills Is

It systematizes McKinsey's Problem Solving methodology into an **8-step workflow** that lets an AI assistant turn a business problem into a professional presentation (PPT + Excel evidence trail).

### Structural Features

- **8-step workflow**: define boundaries → Issue Tree + hypotheses → Dummy Pages + design specs → page-by-page iterative production → PPT + Excel → optional Word report → iterative revision.
- **Dummy Page**: build the wireframe spec before research, to avoid aimless data collection and to support resuming across conversations.
- **Dependency awareness**: pages are tagged with dependency status, determining production order (the executive summary is done last).
- **7 page layouts**: title + single chart / two-column / 2×2 matrix / table / waterfall chart / timeline / insight summary.
- **Excel evidence trail**: per-page raw data + URL + cleaning process.
- **Progressive disclosure**: reference files are loaded only at the steps that need them and released afterward, saving ~70% context.
- `references/`: methodology.md, layouts.md, design-specs.md, examples.md, troubleshooting.md.

## 3. What We Adapted and Cited

| Scope | Treatment |
| --- | --- |
| **The 8-step production workflow** | Referenced the workflow, rewritten in this methodology's language, mapped to the eight-stage consulting structure |
| **The Dummy Page concept** | Adapted the "skeleton-first, fill-in-later" discipline into per-page specs for this methodology's deck outlines |
| **Dependency awareness** | Adapted the page-dependency-management concept |
| **The 7 page layouts** | Referenced the layout list, rewritten to extend `VISUAL_ASSETS_SPEC.md` |
| **Excel evidence trail, progressive disclosure** | Adapted the concepts, mapped to this methodology's Evidence discipline and AI-IDE context management |
| **McKinsey Problem Solving, MECE, Pyramid Principle** | Public-domain management knowledge, not proprietary to this project |
| **The original `SKILL.md` and `references/` files** | **Not reproduced, not forked**; this methodology is an independent rewrite |

## 4. License Summary

mckinsey-consultant-skills is released under the **MIT License**, which permits free use, modification, redistribution, and commercial use, including as part of a proprietary product; the only condition is preserving the MIT copyright notice and license text when redistributing the source.

This methodology does **not redistribute** its source code — it independently rewrote `REPORT_PRODUCTION_WORKFLOW.md` after referencing the workflow and design patterns. The rewritten file is licensed under this repo's Apache 2.0; nevertheless, we explicitly **note the citation source** in that file and here, in respect of the original author's contribution.

## 5. Citation Format for Learners

> Production workflow adapted from mckinsey-consultant-skills by @Kafurtan — <https://github.com/Kafurtan/mckinsey-consultant-skills> (MIT License)

## 6. Disclaimer

Any citation, adaptation, or eight-stage mapping of mckinsey-consultant-skills in this methodology represents the interpretation of the methodology author (Morris Lu / Tiger AI 虎智科技) and does not represent the official position of @Kafurtan. "McKinsey" is a trademark of McKinsey & Company; this methodology has no affiliation with or endorsement from McKinsey & Company, and related methodology names are used only as references to public-domain management knowledge. If mckinsey-consultant-skills' workflow or structure changes in newer versions, refer to the [upstream repository](https://github.com/Kafurtan/mckinsey-consultant-skills).
