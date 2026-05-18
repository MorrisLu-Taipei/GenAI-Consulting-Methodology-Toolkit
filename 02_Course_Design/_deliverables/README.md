# L1-L5 課程 Deliverables / Course Deliverables

> 對應課程 / Maps to: 各 L1-L5 課程的 §3.4 Reference materials 清單 / §3.4 Reference materials list of each L1-L5 course
> 版本 / Version: v1.0（2026-05-18）
> 授權 / License: Apache 2.0

## 用途 / Purpose

本資料夾收錄 L1-L5 課程的 **填空式範本檔案**（templates）。每份檔案：
This folder contains **fillable templates** for L1-L5 courses. Each file:

- 中英雙語並陳 / bilingual zh + EN
- 含 `[填入 / fill in]` 等待客戶 / 學員填入 / contains `[fill in]` placeholders for client / learner
- 可由 [`09_Research_Paper/Makefile`](../../09_Research_Paper/Makefile) 同樣 pipeline 渲染成 PDF（依需要）/ can be rendered to PDF via the same pandoc pipeline as `09_Research_Paper/Makefile`

---

## 檔案清單 / File List

### L1 OpenWebUI（5 個 / 5 files）

| 檔案 / File | 用途 / Use |
|---|---|
| [`L1_USER_OPERATION_MANUAL.md`](L1_USER_OPERATION_MANUAL.md) | 使用者操作手冊：login SOP + 模型選擇決策樹 + 檔案上傳 checklist + 資料邊界 10 案例 / User manual |
| [`L1_ADMIN_RUNBOOK.md`](L1_ADMIN_RUNBOOK.md) | Admin Runbook：帳號 / 角色 / 群組 / 權限 / 模型 / 功能完整設定 + Gate 1 驗收 |
| [`L1_AI_USAGE_POLICY_TEMPLATE.md`](L1_AI_USAGE_POLICY_TEMPLATE.md) | AI 使用規範範本 1 頁 / 1-page AI usage policy template |
| [`L1_DATA_BOUNDARY_QUIZ.md`](L1_DATA_BOUNDARY_QUIZ.md) | 資料邊界 10 題判斷題庫（含答案解析）/ 10-question data boundary quiz |
| [`L1_PROMPT_LIBRARY_STARTER.md`](L1_PROMPT_LIBRARY_STARTER.md) | Prompt Library 啟動包：5 個範例 Prompt + 5 個個人擴充欄 / 5 starter prompts + 5 expansion slots |

### L2 Antigravity（3 個 / 3 files）

| 檔案 / File | 用途 / Use |
|---|---|
| [`L2_ANTIGRAVITY_OPERATION_POLICY.md`](L2_ANTIGRAVITY_OPERATION_POLICY.md) | 操作政策表：Terminal / Review / JS 三本柱 + Safe Mode 條件 |
| [`L2_FLASK_SKELETON.md`](L2_FLASK_SKELETON.md) | Flask app 骨架（12 個檔案結構 + 各檔內容 + pytest + Dockerfile） |
| [`L2_WALKTHROUGH_ARTIFACT_EXAMPLE.md`](L2_WALKTHROUGH_ARTIFACT_EXAMPLE.md) | Walkthrough artifact 6 欄範例 + 自審 / Reviewer checklist |

### L3 n8n（2 個 / 2 files）

| 檔案 / File | 用途 / Use |
|---|---|
| [`L3_DATA_TABLES_SCHEMA_EXAMPLE.md`](L3_DATA_TABLES_SCHEMA_EXAMPLE.md) | Data Tables schema：5 必備欄 + 2 個完整範例（客戶詢價 / 客服分類） |
| [`L3_SUBWORKFLOW_DESIGN_CHECKLIST.md`](L3_SUBWORKFLOW_DESIGN_CHECKLIST.md) | Sub-workflow 8 點設計 checklist + 範例 + 反例 |

### L4 Hermes Agent（2 個 / 2 files）

| 檔案 / File | 用途 / Use |
|---|---|
| [`L4_AGENT_TASK_CARD.md`](L4_AGENT_TASK_CARD.md) | Agent 任務卡：Mission / 邊界 / IPOE / Human Gate / KPI / 風險 / Gate 4 |
| [`L4_HERMES_AGENT_RUNBOOK.md`](L4_HERMES_AGENT_RUNBOOK.md) | 上線後維運 Runbook：日常 SOP / 故障處理 / Rollback / 升版 / Post-mortem |

### L5 ClawTeam

L5 deliverable 範本（Agent 角色卡、整合報告、Human Gate 設計、CLI 速查卡）已 **內嵌於** [`L5_CLAWTEAM_COURSE_PLAN.md`](../L5_CLAWTEAM_COURSE_PLAN.md) 內，不另抽檔。
L5 deliverables (Agent role card, integration report, Human Gate design, CLI cheat sheet) are **embedded** in `L5_CLAWTEAM_COURSE_PLAN.md` and not extracted to standalone files.

---

## 渲染成 PDF / Render to PDF

```bash
# 用 09_Research_Paper 的 pandoc pipeline，假設已裝 pandoc + MiKTeX
# Using the pandoc pipeline from 09_Research_Paper, assuming pandoc + MiKTeX installed

cd 02_Course_Design/_deliverables
pandoc L1_USER_OPERATION_MANUAL.md \
  -o L1_USER_OPERATION_MANUAL.pdf \
  --pdf-engine=xelatex \
  --include-in-header=../../09_Research_Paper/_preamble.tex \
  --variable=mainfont="Times New Roman" \
  --variable=monofont="Consolas" \
  --variable=geometry:margin=0.9in \
  --toc \
  --number-sections
```

---

## 客戶交付建議 / Client Delivery Guidance

| 場景 / Scenario | 給什麼 / Deliver what |
|---|---|
| 全員上線 / All-hands launch | L1_USER_OPERATION_MANUAL + L1_AI_USAGE_POLICY |
| IT 部門 setup / IT setup | L1_ADMIN_RUNBOOK + L2_ANTIGRAVITY_OPERATION_POLICY |
| 種子團隊培訓 / Seed team training | 全部 / All |
| 學員 hands-on / Learner hands-on | L1_PROMPT_LIBRARY_STARTER + L2_FLASK_SKELETON + L3_DATA_TABLES_SCHEMA |
| Agent owner 上線 / Agent owner go-live | L4_AGENT_TASK_CARD + L4_HERMES_AGENT_RUNBOOK |
| 跨部門 Agent Team / Cross-functional Agent Team | L5_CLAWTEAM_COURSE_PLAN（內嵌範本 / embedded templates） |

---

## 客製化指引 / Customization Guide

1. **不要直接交付給客戶用** —— 這些是「範本」不是「成品」。/ Don't deliver directly — these are templates not finished products.
2. **客製順序：** 客戶名稱 / 部門 / 工具版本 / 數字 / 範例情境換成客戶自家的 / Customize: company name / dept / tool versions / numbers / scenarios.
3. **法務審：** AI 使用規範、Runbook、任務卡上線前都應該被客戶法務看過 / Legal review: usage policy, Runbook, task cards should all pass client's legal review before launch.
4. **版本管理：** 客戶填完後存到客戶 repo，標版本 v1.0 開始 / Versioning: after client fills in, store in client repo at v1.0.
