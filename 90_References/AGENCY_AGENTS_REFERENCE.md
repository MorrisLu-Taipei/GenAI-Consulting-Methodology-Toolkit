# agency-agents 引用與授權說明 / agency-agents Citation & License Notice

> 🌐 English version: [AGENCY_AGENTS_REFERENCE_EN.md](AGENCY_AGENTS_REFERENCE_EN.md)

本方法論的 **L2 Skill AI**（特別是 L2-B Agentic Developer 線）下半段，引用 **agency-agents** 作為「現成 agent persona 庫」之教學素材。本檔詳列原始來源、授權條款、引用方式與使用範圍。

The **L2 Skill AI** course of this methodology (specifically the L2-B Agentic Developer track) cites **agency-agents** as teaching material for the "ready-made agent persona library" module. This document records the upstream source, license terms, citation guidance, and scope of use.

---

## 1. 原始專案 / Upstream Project

| 項目 / Field | 內容 / Value |
| --- | --- |
| **專案名稱 / Project** | agency-agents |
| **作者 / Maintainer** | @msitarzewski（社群維護 / community-maintained） |
| **GitHub URL** | <https://github.com/msitarzewski/agency-agents> |
| **授權 / License** | **MIT License** |
| **內容規模 / Scale** | 144+ 個 agent persona，分 12 大類（divisions） |
| **支援工具 / Tools** | Claude Code、GitHub Copilot、Cursor、Aider、Windsurf、OpenCode、Antigravity、Gemini CLI、OpenClaw、Qwen Code、Kimi Code |

## 2. agency-agents 是什麼 / What is agency-agents

agency-agents 是一個 **AI agent persona 定義集合**：每個 agent 是一份 markdown，內含身份特質、核心使命、技術規格、工作流程與可衡量的成功指標。它不是泛用的 prompt 模板，而是一組「可部署的虛擬專家」。

agency-agents is a **collection of AI agent persona definitions**: each agent is a markdown file containing identity traits, core mission, technical specifications, workflow processes, and measurable success criteria. It is not a set of generic prompt templates but a roster of "deployable virtual specialists."

### 12 大類 / 12 Divisions

`engineering`（25+ agents：Frontend Developer、Backend Architect、Security Engineer…）、`design`、`marketing`、`sales`、`product`、`project-management`、`testing`、`support`、`finance`、`game-development`、`academic`、`specialized`、`spatial-computing`。

### 安裝 / Installation

透過 `./scripts/install.sh` 安裝，會自動偵測已安裝的 AI 工具並平行處理。
Installed via `./scripts/install.sh`, which auto-detects installed AI tools and processes them in parallel.

## 3. 為什麼放在 L2 / Why It Belongs in L2

L2 Skill AI 的核心是「把工作經驗封裝成可複用 Skill」。L2-B Agentic Developer 線的下半段要教一個關鍵觀念：**不是每個 Skill 都要從零寫。** agency-agents 提供 144+ 個成熟 agent persona，可作為 Skill 建置的起點 — 學員學會挑選、客製、納入企業 Skill Library，而非重造輪子。

The core of L2 Skill AI is "packaging work experience into reusable Skills." The second half of the L2-B Agentic Developer track teaches a key idea: **not every Skill needs to be built from scratch.** agency-agents provides 144+ mature agent personas as a starting point — learners select, customize, and incorporate them into the enterprise Skill Library rather than reinventing the wheel.

對應課程：[`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6。
Corresponding course: `../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md` §7.6.

## 4. 授權條款摘要 / License Summary

agency-agents 採用 **MIT License**。MIT 允許您自由使用、修改、再散布、商業使用，並可作為閉源產品的一部分；**唯一條件**是再散布時保留原始 MIT 著作權聲明與授權文字。MIT 不強制要求對使用者顯示署名（但原作者表示 appreciated）。

agency-agents is released under the **MIT License**. MIT permits free use, modification, redistribution, and commercial use, including as part of a proprietary product; **the only condition** is that redistribution must preserve the original MIT copyright notice and license text. MIT does not strictly require visible attribution to end users (though the author notes it is appreciated).

> ⚠️ **重要 / Important**
> 本 repo **不重新散布** agency-agents 的原始碼。我們僅在 L2 課程中**教學引用**其結構與用法，並引導學員**自行從 GitHub 安裝**。學員客製化後的 agent persona 屬企業所有，但建議於 Skill 文件中標註原始來源（agency-agents + 版本）。
> This repo does **not redistribute** agency-agents source. We only **cite and teach** its structure and usage in the L2 course and direct learners to **install upstream** themselves. Agent personas customized by learners belong to the enterprise, but it is recommended to note the original source (agency-agents + version) in the Skill documentation.

## 5. 在本方法論的引用範圍 / Scope of Citation

| 範圍 / Scope | 處理方式 / Treatment |
| --- | --- |
| **作為教學素材** / As teaching material | 在 L2-B 下半段作為「現成 agent 庫」案例；教安裝、瀏覽、挑選、客製 / Used as the "ready-made agent library" case in the L2-B second half; teaches install, browse, select, customize |
| **程式碼 / persona 檔** / Source / persona files | **未重製、未 fork**；學員自行 `./scripts/install.sh` / **Not reproduced, not forked**; learners install themselves |
| **客製化產出** / Customized output | 學員客製後的 persona = 企業 Skill Library 條目，建議標註來源 / Customized personas become enterprise Skill Library entries; source attribution recommended |

## 6. 學員引用建議格式 / Citation Format for Learners

> Based on agency-agents by @msitarzewski — <https://github.com/msitarzewski/agency-agents> (MIT License)
> 基於 @msitarzewski 之 agency-agents — <https://github.com/msitarzewski/agency-agents> (MIT 授權)

## 7. 免責聲明 / Disclaimer

本方法論中對 agency-agents 之任何描述、應用、客製化建議，皆為本方法論作者（Morris Lu / Tiger AI 虎智科技）的學習詮釋，不代表 @msitarzewski 或 agency-agents 社群之官方立場。若 agency-agents 之結構、安裝方式、agent 分類有版本變動，請以 [上游 repo](https://github.com/msitarzewski/agency-agents) 之最新版本為準。

Any description, application, or customization guidance for agency-agents in this methodology represents the interpretation of the methodology author (Morris Lu / Tiger AI 虎智科技) and does not represent the official position of @msitarzewski or the agency-agents community. If agency-agents' structure, installation, or agent taxonomy changes in newer versions, refer to the [upstream repository](https://github.com/msitarzewski/agency-agents).
