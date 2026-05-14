# agency-agents Citation & License Notice

> 🌐 中文版本 / Chinese version: [AGENCY_AGENTS_REFERENCE.md](AGENCY_AGENTS_REFERENCE.md)

The second half of the **L2 Skill AI** course in this methodology (specifically the L2-B Agentic Developer track) cites **agency-agents** as teaching material for the "ready-made agent persona library" module. This document records the upstream source, license terms, citation guidance, and scope of use.

---

## 1. Upstream Project

| Field | Value |
| --- | --- |
| **Project** | agency-agents |
| **Maintainer** | @msitarzewski (community-maintained) |
| **GitHub URL** | <https://github.com/msitarzewski/agency-agents> |
| **License** | **MIT License** |
| **Scale** | 144+ agent personas across 12 divisions |
| **Supported tools** | Claude Code, GitHub Copilot, Cursor, Aider, Windsurf, OpenCode, Antigravity, Gemini CLI, OpenClaw, Qwen Code, Kimi Code |

## 2. What is agency-agents

agency-agents is a **collection of AI agent persona definitions**: each agent is a markdown file containing identity traits, core mission, technical specifications, workflow processes, and measurable success criteria. It is not a set of generic prompt templates but a roster of "deployable virtual specialists."

### 12 Divisions

`engineering` (25+ agents: Frontend Developer, Backend Architect, Security Engineer…), `design`, `marketing`, `sales`, `product`, `project-management`, `testing`, `support`, `finance`, `game-development`, `academic`, `specialized`, `spatial-computing`.

### Installation

Installed via `./scripts/install.sh`, which auto-detects installed AI tools and processes them in parallel.

## 3. Why It Belongs in L2

The core of L2 Skill AI is "packaging work experience into reusable Skills." The second half of the L2-B Agentic Developer track teaches a key idea: **not every Skill needs to be built from scratch.** agency-agents provides 144+ mature agent personas as a starting point — learners select, customize, and incorporate them into the enterprise Skill Library rather than reinventing the wheel.

Corresponding course: [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6.

## 4. License Summary

agency-agents is released under the **MIT License**. MIT permits free use, modification, redistribution, and commercial use, including as part of a proprietary product; **the only condition** is that redistribution must preserve the original MIT copyright notice and license text. MIT does not strictly require visible attribution to end users (though the author notes it is appreciated).

> ⚠️ **Important**
> This repo does **not redistribute** agency-agents source. We only **cite and teach** its structure and usage in the L2 course and direct learners to **install upstream** themselves. Agent personas customized by learners belong to the enterprise, but it is recommended to note the original source (agency-agents + version) in the Skill documentation.

## 5. Scope of Citation

| Scope | Treatment |
| --- | --- |
| **As teaching material** | Used as the "ready-made agent library" case in the L2-B second half; teaches install, browse, select, customize |
| **Source / persona files** | **Not reproduced, not forked**; learners install themselves via `./scripts/install.sh` |
| **Customized output** | Customized personas become enterprise Skill Library entries; source attribution recommended |

## 6. Citation Format for Learners

> Based on agency-agents by @msitarzewski — <https://github.com/msitarzewski/agency-agents> (MIT License)

## 7. Disclaimer

Any description, application, or customization guidance for agency-agents in this methodology represents the interpretation of the methodology author (Morris Lu / Tiger AI 虎智科技) and does not represent the official position of @msitarzewski or the agency-agents community. If agency-agents' structure, installation, or agent taxonomy changes in newer versions, refer to the [upstream repository](https://github.com/msitarzewski/agency-agents).
