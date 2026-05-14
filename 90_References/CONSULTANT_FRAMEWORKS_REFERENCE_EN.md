# consultant Frameworks — Citation & License Notice

> 🌐 中文版本 / Chinese version: [CONSULTANT_FRAMEWORKS_REFERENCE.md](CONSULTANT_FRAMEWORKS_REFERENCE.md)

The framework list and taxonomy in this methodology's [`03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) are referenced from and rewritten based on **yoichiojima-2/consultant**. This document records the upstream source, license terms, citation guidance, and scope of adaptation.

---

## 1. Upstream Project

| Field | Value |
| --- | --- |
| **Project** | consultant |
| **Maintainer** | @yoichiojima-2 |
| **GitHub URL** | <https://github.com/yoichiojima-2/consultant> |
| **License** | **MIT License** |
| **Form** | Claude Code plugin (installed via `/plugin marketplace add`) |
| **Content** | 50+ classic consulting frameworks (McKinsey / BCG / Bain / Accenture) across 7 categories, packaged as a markdown skill |

## 2. What consultant Is

consultant is a **Claude Code plugin** that packages 50+ classic management-consulting frameworks (MECE, Pyramid Principle, Porter's 5 Forces, SWOT, BCG Matrix, PESTEL, 5 Whys, Fishbone, Business Model Canvas, WBS, RACI, Kotter, OKR, NPV/IRR, Lean, Six Sigma, etc.) into a markdown skill.

### Structural Features

- **7-category taxonomy**: problem solving / strategy analysis / case frameworks / business design / project & change / financial analysis / operations.
- **Trigger recognition**: routes natural-language "I need to…" sentences to a framework combination.
- **Framework combinations**: pre-built multi-framework chains (e.g., PESTEL → 5 Forces → 3C → SWOT → Issue Tree).
- **Standard structure per framework**: origin / core concept / steps / how to apply / real-world example / common pitfalls.

## 3. What We Adapted and Cited

| Scope | Treatment |
| --- | --- |
| **Framework list and 7-category taxonomy** | Referenced the taxonomy, rewritten in this methodology's language |
| **The "framework selector" concept** (natural language → framework) | Adapted the trigger-recognition pattern into a selector aligned with this methodology's scenarios |
| **The "framework combination chains" concept** | Adapted the combination-chains pattern, mapped to this methodology's eight stages |
| **Per-framework expansion format** | Referenced its per-framework structure, added a "maps-to-stage" column |
| **The classic frameworks themselves** (MECE, Porter's 5 Forces, etc.) | Public-domain management knowledge, not proprietary to consultant |
| **The original markdown skill files** | **Not reproduced, not forked**; this methodology is an independent rewrite |

## 4. License Summary

consultant is released under the **MIT License**, which permits free use, modification, redistribution, and commercial use, including as part of a proprietary product; the only condition is preserving the MIT copyright notice and license text when redistributing the source.

This methodology does **not redistribute** consultant's source code — it independently rewrote `CONSULTING_FRAMEWORKS_LIBRARY.md` after referencing consultant's framework list and design patterns. The rewritten file is licensed under this repo's Apache 2.0; nevertheless, we explicitly **note the citation source** in that file and here, in respect of the original author's contribution.

## 5. Citation Format for Learners

> Framework library adapted from consultant by @yoichiojima-2 — <https://github.com/yoichiojima-2/consultant> (MIT License)

## 6. Disclaimer

Any citation, adaptation, or eight-stage mapping of consultant in this methodology represents the interpretation of the methodology author (Morris Lu / Tiger AI 虎智科技) and does not represent the official position of @yoichiojima-2. For the definitions and application of classic consulting frameworks, refer to each framework's original academic / industry source. If consultant's framework list or structure changes in newer versions, refer to the [upstream repository](https://github.com/yoichiojima-2/consultant).
