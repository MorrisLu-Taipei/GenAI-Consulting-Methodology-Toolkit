# AI Consulting Methodology Toolkit

企業 AI 轉型成熟度診斷與導入方法論工具包。

作者：Morris

這個 repo 整理一套可用於企業顧問交付的 AI 轉型方法：先用問卷診斷企業目前 AI 成熟度，再依 L1-L5 配置課程與導入路徑，課中產出可驗收資產，最後用八階段顧問方法產出診斷報告、Roadmap、ROI 與治理建議。

## 方法論總覽

![企業管理顧問方法論：八階段轉型指南](90_References/Metholodgy.png)

## 核心流程

```text
AI 成熟度問卷
→ 公司屬性與部署模式調查
→ L1-L5 課程與能力建置
→ L4 Hermes Agent PoC 與 evidence
→ 情境案例與 Stage Gate
→ 八階段顧問診斷
→ AI 轉型診斷報告與 Roadmap
```

## L1-L5 成熟度模型

| 等級 | 名稱 | 工具 / 平台 | 核心定位 |
| --- | --- | --- | --- |
| L1 | Chat AI | OpenWebUI | 企業內部 AI 對話入口，讓員工開始安全使用 AI |
| L2 | Skill AI | Antigravity / Claude Code / Codex | 將個人經驗、提示詞、文件與工作方法整理成可複用 Skill |
| L3 | Workflow AI | n8n | 串接 Gmail、Sheets、Notion、CRM、API、ERP 等系統，讓 AI 進入流程 |
| L4 | Auto Agentic AI | Hermes Agent | 以 Wiki 記憶、Skill、Workflow、工具、排程與人工 Gate 組成可驗證的知識型 Agent 作業系統 |
| L5 | Agentic Team AI | ClawTeam | AI Agent Team 協作平台，多個專業 Agent 協同完成企業級任務 |

## 目錄結構

| 目錄 | 用途 |
| --- | --- |
| [`00_Overview`](00_Overview/) | 方案總論、故事線、WBS |
| [`01_Assessment`](01_Assessment/) | AI 成熟度問卷與評分模型 |
| [`02_Course_Design`](02_Course_Design/) | L1-L5 完整課程規劃、L4 Hermes Agent 深度課程、公司屬性、部署模式 |
| [`03_Consulting_Report`](03_Consulting_Report/) | AI 轉型診斷報告模板 |
| [`04_Scenarios`](04_Scenarios/) | 客戶情境、案例控制表、製造業與醫院案例 |
| [`05_Sales`](05_Sales/) | 對外價值主張、銷售話術與 FAQ |
| [`06_Delivery`](06_Delivery/) | 交付包與驗收標準 |
| [`90_References`](90_References/) | 原始 PDF 與方法論圖片 |

## 建議閱讀順序

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md)
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md)
4. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
5. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md)
6. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md)
7. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)
8. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)

## 可驗證交付物

- AI 成熟度問卷與評分結果
- 公司屬性與部署模式調查
- L1-L5 課程完成證據
- Skill Library
- n8n Workflow PoC 與 Execution Log
- Hermes Agent 任務卡、Wiki、ingest/query/update 紀錄、briefing 與 Gate 4A-4E
- ClawTeam Agent Team 角色卡
- Stage Gate 驗收紀錄
- AI 轉型診斷報告
- 30 / 60 / 90 天 Roadmap

## 參考資料

- [`90_References/@AI-MD-PUBIC.pdf`](90_References/@AI-MD-PUBIC.pdf)
- [`90_References/Metholodgy.png`](90_References/Metholodgy.png)

