# 90 References — Reference Materials & Third-Party Citations

> 🌐 中文版本 / Chinese version: [README.md](README.md)

## 1. Purpose of This Directory

This directory is the methodology's **evidence base and citation-governance center**. `00`-`06` are "methods and tools"; this directory answers: **"What is the basis for these methods? What content cites third parties? Is the licensing compliant?"**

The problem it solves: **an open-source methodology that draws heavily on third-party material faces two risks if its "basis" and "citation licensing" are not managed clearly — (1) users do not know the methodology's foundation, and (2) it may infringe third-party copyright/licensing.** This directory centralizes: original reference materials (PDFs, methodology diagrams), third-party video learning notes, and a **citation & license notice file for every cited third-party project**.

Who uses this directory: consultants (checking the methodology's basis), reviewers (checking license compliance), legal counsel (confirming citations are clean), and anyone redistributing/commercializing this methodology.

## 2. Position in the Methodology

| Axis | Mapping |
| --- | --- |
| Three-phase service flow | **Across the whole flow** — underpins the basis and citations of `00`-`06` |
| Eight-stage consulting structure | Does not map to a single stage; it is the evidence layer of the whole methodology |
| License governance | This repo uses Apache 2.0; this directory manages the license compliance of all third-party citations |

## 3. Goals & Benefits

| Goal | Benefit |
| --- | --- |
| Centralize original reference materials | The methodology's basis is traceable |
| Every third-party citation has its own `*_REFERENCE.md` | License compliance is transparent and auditable by legal / reviewers |
| Unified citation principles | Rewrite-don't-fork, explicit attribution, dual notes in both the file and the reference doc |
| Video learning notes separated from original sources | Clearly marks "derivative notes" vs. "original-content copyright" |

**If you skip this directory**: the methodology has no traceable basis, third-party citations are scattered and unauditable, and redistribution risks licensing infringement.

## 4. Citation Principles & Usage Logic

When this methodology cites third-party material, it always follows these principles (i.e., "Plan A"):

1. **Independent rewrite — do not fork, do not reproduce source code** — after referencing its structure and concepts, rewrite in this methodology's language.
2. **Explicit attribution** — note the original author and license both in the header of the citing file and in this directory's `*_REFERENCE.md` (dual notes).
3. **Generalize to this methodology's context** — convert domain-specific content into the L1-L5 AI transformation consulting context.
4. **Do not touch the unlicensed** — third-party projects without a LICENSE are not integrated (they can only be cited as external example URLs).

**Usage logic**: to check "what a given file in a given directory cites" → look at that file's header "citation note" → go to the corresponding `*_REFERENCE.md` in this directory for the full license explanation.

## 5. File Descriptions

### Original reference materials and diagrams

| File | Purpose |
| --- | --- |
| `@AI-MD-PUBIC.pdf` | The public-version handbook of the AI transformation maturity model. |
| `MD-Map.png` | The AI maturity map, used for the maturity overview in the root README. |
| `Metholodgy.png` | The eight-stage enterprise-management-consulting transformation guide, used for the methodology overview in the root README. |

### Third-party video learning notes (derivative notes; original video copyright belongs to the original creators)

| File | Purpose |
| --- | --- |
| `OPENWEBUI_VIDEO_LEARNING_NOTES.md` | Learning notes on the OpenWebUI public playlist and its mapping to the L1 course. |
| `TIGERAI_VIDEO_LEARNING_NOTES.md` | Learning notes on the TigerAI channel videos, focused on n8n / the L3 course. |

### Third-party project citation & license notices

| File | Cited project / License | Corresponding directory |
| --- | --- | --- |
| `CLAWTEAM_REFERENCE.md` | HKUDS/ClawTeam (MIT) | L5 course platform (`02`) |
| `AGENCY_AGENTS_REFERENCE.md` | msitarzewski/agency-agents (MIT) | L2 agent-persona library (`02`) |
| `N8N_SKILL_PACK_REFERENCE.md` | MorrisLu-Taipei/TigerAI-n8n-Skill-Pack (mixed license) | Second half of the L3 course (`02`) |
| `CONSULTANT_FRAMEWORKS_REFERENCE.md` | yoichiojima-2/consultant (MIT) | Classic consulting frameworks library (`03`) |
| `MCKINSEY_SKILLS_REFERENCE.md` | Kafurtan/mckinsey-consultant-skills (MIT) | Report production workflow (`03`) |
| `WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md` | Mirza Iqbal / next8n.com (MIT) | Engagement-operations layer (`06`) |
| `AWESOME_LLM_APPS_REFERENCE.md` | Shubhamsaboo/awesome-llm-apps (Apache-2.0) | LLM application case index (`04`) |
| `AI_ENGINEERING_HUB_REFERENCE.md` | patchy631/ai-engineering-hub (MIT) | LLM application case index (`04`) |

### `*_EN.md`

The English-version siblings of some files.

## 6. Attribution

The content in this directory originally created by Tiger AI Morris Lu 盧業興 is licensed under the Apache License 2.0 of the root [`LICENSE`](../LICENSE) and may be freely used, modified, adapted, and commercialized. When redistributing, preserve the author attribution in [`NOTICE`](../NOTICE):

```text
Original Author: Tiger AI Morris Lu 盧業興
Role: n8n Taipei Ambassador / PhD Student, Graduate Institute of Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australia
```

Third-party platform names, trademarks, videos, external projects, and cited content remain the property of their respective rights holders. This repo only performs learning notes, citation, organization, and course-design reference on third-party material; it does not reproduce or fork source code. The license and citation scope of each third party is detailed in the corresponding `*_REFERENCE.md` in the table above.

## 7. Mapping to Other Directories

| Directory | Relationship to this directory |
| --- | --- |
| `00_Overview` | The methodology diagrams in the storyline (Metholodgy.png / MD-Map.png) come from here |
| `02_Course_Design` | Third-party citations for the L1/L2/L3/L5 courses (OpenWebUI notes, agency-agents, n8n-Skill-Pack, ClawTeam) |
| `03_Consulting_Report` | Third-party citations for the frameworks library and report workflow (consultant, mckinsey-skills) |
| `04_Scenarios` | Third-party citations for the LLM application case index (awesome-llm-apps, ai-engineering-hub) |
| `06_Delivery` | Third-party citation for the engagement-operations layer (Mirza Iqbal framework) |

## 8. Common Usage Scenarios

- **A reviewer checks license compliance**: read the citation table in §5 and cross-check each `*_REFERENCE.md`.
- **A consultant checks the methodology's basis**: the basis of the eight-stage methodology is in `@AI-MD-PUBIC.pdf` and `Metholodgy.png`.
- **Redistributing/commercializing this methodology**: first read the §6 attribution requirements and the root `NOTICE`.
- **Evaluating new third-party material**: follow the §4 citation principles — first confirm there is a license, then rewrite independently, then create a `*_REFERENCE.md`.
