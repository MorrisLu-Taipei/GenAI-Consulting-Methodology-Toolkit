# AI Consulting Methodology Toolkit

> 企業 AI 轉型成熟度診斷與導入方法論工具包
> Enterprise AI Transformation Maturity Assessment & Implementation Methodology Toolkit

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

**作者 / Author：** Morris Lu （盧業興）· Tiger AI 虎智科技
**身份 / Roles：** n8n Taipei 大使 · 國立臺灣科技大學 智慧製造科技研究所 博士生 · QUT 昆士蘭科技大學 資工碩士
**Roles (EN):** n8n Taipei Ambassador · PhD Student, Graduate Institute of Intelligent Manufacturing Tech, NTUST · Master of Information Technology (M.IT), Queensland University of Technology (QUT)

![AI 成熟度地圖 / AI Maturity Map](90_References/MD-Map.png)

這個 repo 整理一套可用於企業顧問交付的 AI 轉型方法：先用問卷診斷企業目前 AI 成熟度，再依 L1-L5 配置課程與導入路徑，課中產出可驗收資產，最後用八階段顧問方法產出診斷報告、Roadmap、ROI 與治理建議。

This repository organizes an enterprise AI transformation methodology suitable for consulting delivery: it begins with a maturity questionnaire, then maps L1-L5 courses and adoption paths, produces verifiable in-class artifacts, and concludes with an eight-stage consulting method that yields the diagnostic report, roadmap, ROI, and governance recommendations.

## 授權 / License

本專案採用 **[Apache License 2.0](LICENSE)** 授權，您可以自由地 **使用、修改、再散布與商業利用**。Apache 2.0 是業界廣泛使用的開源授權，並包含 **patent grant**（防專利訴訟）。

This work is licensed under the **[Apache License 2.0](LICENSE)** — a widely-adopted open-source license that includes a **patent grant**. You are free to **use, modify, redistribute, and commercialize** the contents.

**唯一條件：必須保留 [`NOTICE`](NOTICE) 檔案中的署名（Apache 2.0 §4(d) 要求）。**
**Single condition: you must preserve the attribution notices in the [`NOTICE`](NOTICE) file (required by Apache 2.0 §4(d)).**

詳細署名指引請見 [NOTICE.md](NOTICE.md)。
For human-readable attribution guidance, see [NOTICE.md](NOTICE.md).

## 方法論總覽 / Methodology Overview

![企業管理顧問方法論：八階段轉型指南 / Consulting Methodology: Eight-Stage Transformation Guide](90_References/Metholodgy.png)

## 核心流程 / Core Process

```text
AI 成熟度問卷                                    /  AI Maturity Questionnaire
→ 公司屬性與部署模式調查                          /  → Company profile & deployment-mode survey
→ L1-L5 課程與能力建置                            /  → L1-L5 courses & capability building
→ L1 OpenWebUI 企業帳號與個人聊天區啟用             /  → L1 OpenWebUI enterprise accounts & personal chat workspaces
→ L2 Antigravity Agentic Developer Skill         /  → L2 Antigravity Agentic Developer Skill
→ L3 n8n 企業流程自動化 PoC                       /  → L3 n8n enterprise workflow automation PoC
→ L4 Hermes Agent PoC 與 evidence                /  → L4 Hermes Agent PoC & evidence
→ 情境案例與 Stage Gate                           /  → Scenario cases & Stage Gate
→ 八階段顧問診斷                                  /  → Eight-stage consulting diagnostic
→ AI 轉型診斷報告與 Roadmap                       /  → AI transformation diagnostic report & Roadmap
```

## L1-L5 成熟度模型 / Maturity Model

> **層層銜接：上一層的「產出」就是下一層的「輸入」。**
> **Each layer feeds the next — the *output* of one level becomes the *input* of the level above it.**

### 流程圖 / Flow

```text
                                              ┌───────────────────────────────────────┐
L5  Agentic Team AI    ◀── 多個 L4 Agent ─── │  ClawTeam：Agent Team 完成企業級任務   │
        ▲                                     └───────────────────────────────────────┘
        │ 多個專業 Agent 上架
        │ multiple specialist Agents onboarded
L4  Auto Agentic AI    ◀── L3 Workflow + L2 Skill + Wiki + Gate ──▶  Hermes Agent
        ▲
        │ Workflow 成為 Agent 可呼叫的工具
        │ Workflows become Agent-callable tools
L3  Workflow AI        ◀── L2 Skill + 企業系統 (Gmail/CRM/ERP) ──▶  n8n
        ▲
        │ Skill Library 成為流程的動作積木
        │ Skill Library becomes workflow building blocks
L2  Skill AI           ◀── L1 高頻 Prompt + 工作經驗 ──▶  Antigravity / Claude Code / Codex
        ▲
        │ 員工沉澱出高頻 Prompt 與情境
        │ Employees surface high-freq prompts & scenarios
L1  Chat AI            ◀── 企業全員開始安全使用 AI ──▶  OpenWebUI
        △ (起點 / starting point)
```

### 層層銜接表 / Layer-by-Layer Handoff Table

| 等級 / Level | 名稱 / Name | 工具 / Tool | 由前一層接手 (Input) | 這一層做什麼 (Action) | 交付給下一層 (Output) |
| --- | --- | --- | --- | --- | --- |
| **L1** | **Chat AI** | OpenWebUI | — 起點 / starting point | 建立企業 AI 對話入口，全員安全使用 AI / Establish enterprise AI chat entry; safe AI usage org-wide | 高頻 Prompt 清單、使用情境、Skill 候選名單 / High-freq prompts, use-case inventory, Skill candidates |
| **L2** | **Skill AI** | Antigravity / Claude Code / Codex | L1 的高頻 Prompt 與情境 / L1 prompts & scenarios | 把個人經驗、Prompt、文件、工作方法封裝成可複用 Skill / Package personal know-how into reusable Skills | Skill Library、Agentic artifacts、工作流 Blueprint / Skill Library, Agentic artifacts, Workflow Blueprints |
| **L3** | **Workflow AI** | n8n | L2 的 Skill + 工作流 Blueprint / L2 Skills & Blueprints | 把 Skill 接上企業系統 (Gmail / Sheets / Notion / CRM / ERP / API) 串成可執行 Workflow / Wire Skills into executable workflows across enterprise systems | Workflow PoC、Sub-workflow Library、Data Tables、Execution Log、L4 Workflow Contract / Workflow PoCs, Sub-workflow Library, Data Tables, Execution Log, L4 Workflow Contract |
| **L4** | **Auto Agentic AI** | Hermes Agent | L3 Workflow + L2 Skill / L3 Workflows & L2 Skills | 加上 Wiki 記憶、排程、工具、人工 Gate，組成可驗證的知識型 Agent / Add Wiki memory, schedules, tools, and human Gates to form verifiable knowledge Agents | 任務卡、Wiki ingest/query/update、briefing、Gate 4A-4E 驗收記錄、可重用 Agent / Task cards, Wiki ingest/query/update, briefings, Gate 4A-4E sign-offs, reusable Agents |
| **L5** | **Agentic Team AI** | ClawTeam | L4 的多個專業 Agent / L4 specialist Agent pool | 把多個 L4 Agent 編組成 Agent Team，協同完成企業級任務 / Orchestrate multiple L4 Agents into a collaborative Team for enterprise-grade outcomes | 企業級成果：跨部門自動化、決策支援、可治理的 AI Team / Enterprise-grade outcomes: cross-functional automation, decision support, governed AI Team |

### 為什麼要分這五層 / Why Five Layers

1. **由人到系統 / From people to systems** — L1-L2 重點是「人怎麼用 AI」；L3-L5 重點是「AI 怎麼進入系統與流程」。
   L1-L2 focus on *how people use AI*; L3-L5 focus on *how AI enters systems and processes*.
2. **每一層都有可驗收的交付物 / Every layer has verifiable deliverables** — Stage Gate 在層與層之間，避免跳級導入失敗。
   Stage Gates between layers prevent failed adoption from level-skipping.
3. **上層永遠以下層為基礎 / Upper layers always build on lower layers** — 沒有 L1 的全員使用習慣，L2 的 Skill 無從累積；沒有 L2 的 Skill，L3 的 Workflow 只是無內容的串接；沒有 L3 的 Workflow，L4 Agent 無工具可用；沒有 L4 Agent，L5 Team 無成員。
   Without L1 org-wide adoption, L2 has no Skills to accumulate; without L2 Skills, L3 workflows are empty pipes; without L3 Workflows, L4 Agents have no tools; without L4 Agents, L5 has no team members.

## 目錄結構 / Repository Structure

> 每個資料夾內的 .md 檔案皆有對應的 `*_EN.md` 英文版兄弟檔。
> Every `.md` file under each folder has a sibling `*_EN.md` English version.

| 目錄 / Folder | 用途 / Purpose |
| --- | --- |
| [`00_Overview`](00_Overview/) | 方案總論、故事線、WBS / Overall narrative, storyline, WBS |
| [`01_Assessment`](01_Assessment/) | AI 成熟度問卷與評分模型 / AI maturity questionnaire and scoring model |
| [`02_Course_Design`](02_Course_Design/) | L1-L5 完整課程規劃、L1 OpenWebUI 企業啟用、L2 Antigravity 工程訓練、L3 n8n 企業流程自動化、L4 Hermes Agent 深度課程、公司屬性、部署模式 / Complete L1-L5 curriculum, L1 OpenWebUI enterprise rollout, L2 Antigravity engineering training, L3 n8n enterprise workflow automation, L4 Hermes Agent deep-dive course, company profiles, deployment modes |
| [`03_Consulting_Report`](03_Consulting_Report/) | AI 轉型診斷報告模板 / AI transformation diagnostic report template |
| [`04_Scenarios`](04_Scenarios/) | 客戶情境、案例控制表、製造業與醫院案例 / Customer scenarios, case control tables, manufacturing & hospital cases |
| [`05_Sales`](05_Sales/) | 對外價值主張、銷售話術與 FAQ / External value proposition, sales talking points, and FAQ |
| [`06_Delivery`](06_Delivery/) | 交付包與驗收標準 / Delivery package and acceptance criteria |
| [`90_References`](90_References/) | 原始 PDF 與方法論圖片 / Source PDFs and methodology diagrams |

## 建議閱讀順序 / Recommended Reading Order

> 中文檔；英文讀者請開啟同名的 `*_EN.md` 兄弟檔。
> Chinese files listed; English readers should open the sibling `*_EN.md` files.

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) ([EN](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md))
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) ([EN](01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md))
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md) ([EN](01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md))
4. [`01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md) ([EN](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX_EN.md))
5. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md) ([EN](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN_EN.md))
6. [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) ([EN](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN_EN.md))
7. [`02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) ([EN](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN_EN.md))
8. [`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) ([EN](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN_EN.md))
9. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) ([EN](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN_EN.md))
10. [`02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md`](02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md) ([EN](02_Course_Design/L5_CLAWTEAM_COURSE_PLAN_EN.md)) — 引用 [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) (MIT)
11. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md) ([EN](04_Scenarios/CASE_CONTROL_TABLES_EN.md))
12. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md) ([EN](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE_EN.md))
13. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md) ([EN](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md))

## 可驗證交付物 / Verifiable Deliverables

- AI 成熟度問卷與評分結果 / AI maturity questionnaire & scoring results
- 公司屬性與部署模式調查 / Company profile & deployment-mode survey
- L1-L5 課程完成證據 / L1-L5 course completion evidence
- OpenWebUI 帳號 / 群組 / 權限表與每人個人聊天區啟用紀錄 / OpenWebUI accounts / groups / permissions matrix and per-user personal-chat-workspace activation records
- Skill Library 與 Antigravity Agentic Developer artifacts / Skill Library and Antigravity Agentic Developer artifacts
- n8n Workflow PoC 與 Execution Log / n8n Workflow PoC and Execution Log
- Sub-workflow Library、Data Tables Schema、GitHub Backup SOP、L4 Workflow Contract / Sub-workflow Library, Data Tables Schema, GitHub Backup SOP, L4 Workflow Contract
- Hermes Agent 任務卡、Wiki、ingest/query/update 紀錄、briefing 與 Gate 4A-4E / Hermes Agent task cards, Wiki, ingest/query/update records, briefings, and Gates 4A-4E
- ClawTeam Agent Team 角色卡 / ClawTeam Agent Team role cards
- Stage Gate 驗收紀錄 / Stage Gate sign-off records
- AI 轉型診斷報告 / AI transformation diagnostic report
- 30 / 60 / 90 天 Roadmap / 30 / 60 / 90-day Roadmap

## 參考資料 / References

- [`90_References/@AI-MD-PUBIC.pdf`](90_References/@AI-MD-PUBIC.pdf)
- [`90_References/Metholodgy.png`](90_References/Metholodgy.png)
- [`90_References/MD-Map.png`](90_References/MD-Map.png)
- [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md)
- [`90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)
- [`90_References/CLAWTEAM_REFERENCE.md`](90_References/CLAWTEAM_REFERENCE.md) — **L5 平台 ClawTeam 引用與 MIT 授權條款 / L5 platform ClawTeam citation & MIT license terms**

### 第三方內容 / Third-Party Content

本專案中 [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) 為對 **OpenWebUI 公開 YouTube playlist** 的學習筆記。所有影片內容與版權皆歸原始創作者所有，本檔僅引用其公開連結作為學習與課程設計用途。

The file [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) contains study notes derived from the **OpenWebUI public YouTube playlist**. All video content and copyrights remain with the original creators; links are cited solely for educational and course-design reference.

**L5 Agentic Team AI** 課程以 **[HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam)** (MIT License) 作為實作平台。本 repo **未重製、未 fork** ClawTeam 程式碼；僅在 L5 課綱中教學引用其架構、CLI 與設計理念。完整引用條款請見 [`90_References/CLAWTEAM_REFERENCE.md`](90_References/CLAWTEAM_REFERENCE.md)。

The **L5 Agentic Team AI** course uses **[HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam)** (MIT License) as its implementation platform. This repo **does not reproduce or fork** the ClawTeam source; we only cite and teach its architecture, CLI, and design principles in the L5 syllabus. Full citation terms: [`90_References/CLAWTEAM_REFERENCE.md`](90_References/CLAWTEAM_REFERENCE.md).

---

## 致謝 / Acknowledgments

> 🎓 **顧問方法論恩師 / Consulting Methodology Mentor**
> **Prof. Michael Rosemann** — Queensland University of Technology (QUT), Brisbane, Australia
> Profile: <https://www.qut.edu.au/about/our-people/academic-profiles/m.rosemann>

本 repo 整套 **顧問方法論** 的學理基礎，來自作者於 **QUT 昆士蘭科技大學** 求學期間，恩師 **Prof. Michael Rosemann** 的長期啟發與教導。Prof. Rosemann 為國際公認之 **Business Process Management (BPM)**、**Capability Maturity Models** 與 **企業創新方法論** 領域領袖學者，其學術框架直接形塑本方法論的兩大核心：

The **theoretical foundation** of the consulting methodology in this repository comes from the long-term mentorship and teaching of **Prof. Michael Rosemann**, the author's mentor during studies at **Queensland University of Technology (QUT)**. Prof. Rosemann is an internationally recognized leading scholar in **Business Process Management (BPM)**, **Capability Maturity Models**, and **enterprise innovation methodology**, and his academic frameworks directly shape the two pillars of this work:

- **八階段顧問結構** — 對應 Prof. Rosemann 在企業流程診斷、能力評估、轉型路徑設計上的方法學。
  **Eight-stage consulting structure** — informed by Prof. Rosemann's methodology on enterprise process diagnostics, capability assessment, and transformation path design.
- **L1-L5 AI 成熟度模型** — 對應 Prof. Rosemann 的 **BPM Maturity Model** (與 Tonia de Bruin 合著) 的能力成熟度層級設計邏輯，並在地化為企業導入 AI 的五層銜接架構。
  **L1-L5 AI Maturity Model** — informed by the layered capability-maturity logic of Prof. Rosemann's **BPM Maturity Model** (co-authored with Tonia de Bruin), localized into a five-layer adoption framework for enterprise AI.

> ⚠️ **免責聲明 / Disclaimer**
> 本方法論中任何錯誤、遺漏、在地化調整、或對 AI 領域的延伸應用，皆為作者 (Morris Lu / Tiger AI 虎智科技) 個人責任，**不代表** Prof. Rosemann 或 QUT 之觀點或立場。
> Any errors, omissions, local adaptations, or AI-domain extensions in this methodology are **solely** the responsibility of the author (Morris Lu / Tiger AI 虎智科技) and do **not** represent the views or positions of Prof. Rosemann or QUT.

---

## 署名要求 / Attribution Requirement

使用、修改或商業利用本專案內容時，請於合理可見位置保留以下署名：

When using, modifying, or commercializing this work, please preserve the following attribution in a reasonably visible location:

> **原作者 / Author:** Morris Lu (盧業興) · Tiger AI 虎智科技 / Tiger AI Co., Ltd.
> **身份 / Roles:** n8n Taipei 大使 / n8n Taipei Ambassador · 國立臺灣科技大學 智慧製造科技研究所 博士生 / PhD Student, Graduate Institute of Intelligent Manufacturing Tech, NTUST · QUT 昆士蘭科技大學 資工碩士 / Master of Information Technology (M.IT), Queensland University of Technology (QUT)
> **來源 / Source:** <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>

完整授權條款請見 [LICENSE](LICENSE)，完整署名規範請見 [NOTICE.md](NOTICE.md)。
Full license terms: see [LICENSE](LICENSE). Full attribution guidance: see [NOTICE.md](NOTICE.md).
