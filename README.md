# AI Consulting Methodology Toolkit

> 企業 AI 轉型成熟度診斷與導入方法論工具包
> Enterprise AI Transformation Maturity Assessment & Implementation Methodology Toolkit

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

**作者 / Author：** Morris Lu （盧業興）· Tiger AI 虎智科技
**身份 / Roles：** n8n Taipei 大使 · 國立臺灣科技大學 智慧製造科技研究所 博士生
**Roles (EN):** n8n Taipei Ambassador · PhD Student, Graduate Institute of Intelligent Manufacturing Tech, NTUST

![AI 成熟度地圖 / AI Maturity Map](90_References/MD-Map.png)

這個 repo 整理一套可用於企業顧問交付的 AI 轉型方法：先用問卷診斷企業目前 AI 成熟度，再依 L1-L5 配置課程與導入路徑，課中產出可驗收資產，最後用八階段顧問方法產出診斷報告、Roadmap、ROI 與治理建議。

This repository organizes an enterprise AI transformation methodology suitable for consulting delivery: it begins with a maturity questionnaire, then maps L1-L5 courses and adoption paths, produces verifiable in-class artifacts, and concludes with an eight-stage consulting method that yields the diagnostic report, roadmap, ROI, and governance recommendations.

## 授權 / License

本專案採用 **[CC BY 4.0](LICENSE)** 授權，您可以自由地 **使用、修改、再散布與商業利用**，唯一條件是 **必須註明原作者**（詳見 [NOTICE.md](NOTICE.md)）。

This work is licensed under **[CC BY 4.0](LICENSE)**. You are free to **use, modify, redistribute, and commercialize** the contents under the **single condition that the original author is credited** (see [NOTICE.md](NOTICE.md)).

## 方法論總覽

![企業管理顧問方法論：八階段轉型指南](90_References/Metholodgy.png)

## 核心流程

```text
AI 成熟度問卷
→ 公司屬性與部署模式調查
→ L1-L5 課程與能力建置
→ L1 OpenWebUI 企業帳號與個人聊天區啟用
→ L2 Antigravity Agentic Developer Skill
→ L3 n8n 企業流程自動化 PoC
→ L4 Hermes Agent PoC 與 evidence
→ 情境案例與 Stage Gate
→ 八階段顧問診斷
→ AI 轉型診斷報告與 Roadmap
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

## 目錄結構

| 目錄 | 用途 |
| --- | --- |
| [`00_Overview`](00_Overview/) | 方案總論、故事線、WBS |
| [`01_Assessment`](01_Assessment/) | AI 成熟度問卷與評分模型 |
| [`02_Course_Design`](02_Course_Design/) | L1-L5 完整課程規劃、L1 OpenWebUI 企業啟用、L2 Antigravity 工程訓練、L3 n8n 企業流程自動化、L4 Hermes Agent 深度課程、公司屬性、部署模式 |
| [`03_Consulting_Report`](03_Consulting_Report/) | AI 轉型診斷報告模板 |
| [`04_Scenarios`](04_Scenarios/) | 客戶情境、案例控制表、製造業與醫院案例 |
| [`05_Sales`](05_Sales/) | 對外價值主張、銷售話術與 FAQ |
| [`06_Delivery`](06_Delivery/) | 交付包與驗收標準 |
| [`90_References`](90_References/) | 原始 PDF 與方法論圖片 |

## 建議閱讀順序

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md)
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md)
4. [`01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)
5. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
6. [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md)
7. [`02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md)
8. [`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md)
9. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md)
10. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md)
11. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)
12. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)

## 可驗證交付物

- AI 成熟度問卷與評分結果
- 公司屬性與部署模式調查
- L1-L5 課程完成證據
- OpenWebUI 帳號 / 群組 / 權限表與每人個人聊天區啟用紀錄
- Skill Library 與 Antigravity Agentic Developer artifacts
- n8n Workflow PoC 與 Execution Log
- Sub-workflow Library、Data Tables Schema、GitHub Backup SOP、L4 Workflow Contract
- Hermes Agent 任務卡、Wiki、ingest/query/update 紀錄、briefing 與 Gate 4A-4E
- ClawTeam Agent Team 角色卡
- Stage Gate 驗收紀錄
- AI 轉型診斷報告
- 30 / 60 / 90 天 Roadmap

## 參考資料 / References

- [`90_References/@AI-MD-PUBIC.pdf`](90_References/@AI-MD-PUBIC.pdf)
- [`90_References/Metholodgy.png`](90_References/Metholodgy.png)
- [`90_References/MD-Map.png`](90_References/MD-Map.png)
- [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md)
- [`90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

### 第三方內容 / Third-Party Content

本專案中 [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) 為對 **OpenWebUI 公開 YouTube playlist** 的學習筆記。所有影片內容與版權皆歸原始創作者所有，本檔僅引用其公開連結作為學習與課程設計用途。

The file [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) contains study notes derived from the **OpenWebUI public YouTube playlist**. All video content and copyrights remain with the original creators; links are cited solely for educational and course-design reference.

---

## 署名要求 / Attribution Requirement

使用、修改或商業利用本專案內容時，請於合理可見位置保留以下署名：

When using, modifying, or commercializing this work, please preserve the following attribution in a reasonably visible location:

> **原作者 / Author:** Morris Lu (盧業興) · Tiger AI 虎智科技 / Tiger AI Co., Ltd.
> **身份 / Roles:** n8n Taipei 大使 / n8n Taipei Ambassador · 國立臺灣科技大學 智慧製造科技研究所 博士生 / PhD Student, Graduate Institute of Intelligent Manufacturing Tech, NTUST
> **來源 / Source:** <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>

完整授權條款請見 [LICENSE](LICENSE)，完整署名規範請見 [NOTICE.md](NOTICE.md)。
Full license terms: see [LICENSE](LICENSE). Full attribution guidance: see [NOTICE.md](NOTICE.md).
