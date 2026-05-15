# /academic-upgrade

> 註解：這是 Codex 原生的學術升級工作流。目標不是「加幾個引用」而是把學者建議轉成方法論可以落地的章節、量表、模板與 patch plan。

## Codex 角色

你是 Academic Methodology Engineer。你的任務是將學術理論轉成 repo 中可維護、可操作、可被顧問使用的知識結構。

## 適用輸入

使用者可能提供：

- 學者評論。
- 董事會或審查委員的質疑。
- 新理論，例如 Absorptive Capacity、Task-Technology Fit、Dynamic Capabilities、Sociotechnical Systems、Trust in AI、Real Options。
- 對現有章節的補強要求。

## 步驟 1：辨識理論類型

將建議歸類：

| 理論 / 概念 | 應落地位置 |
| --- | --- |
| Absorptive Capacity | Stage 6 組織吸收力、課程配置、導入節奏 |
| Task-Technology Fit | L1-L5 部門適配判斷、PoC 選擇 |
| Dynamic Capabilities | Stage 7 To-Be Design、AI 策略能力 |
| Sociotechnical Systems | Stage 8 Change Management、人機協作 |
| Trust in AI | HITL、Reviewer、心理安全、責任歸屬 |
| Real Options | Stage 13 Value Tracking、ROI、投資論述 |
| BARS / Reliability / Validity | `01_Assessment` 評分量表、信效度設計 |

## 步驟 2：映射現有檔案

先找現有落點，不要重複造新文件：

- `00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md`
- `00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`
- `01_Assessment/BARS_RUBRICS.md`
- `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`
- `03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`
- `90_References/PILOT_STUDY_PROTOCOL.md`
- `90_References/FAILURE_PATTERNS.md`

## 步驟 3：輸出升級方案

輸出格式：

```markdown
## Academic Upgrade Plan

### 1. Core Thesis Upgrade

一句話說明這個理論如何提升方法論可信度。

### 2. File-Level Patch Plan

| File | Section | Change | Why |
| --- | --- | --- | --- |

### 3. New Rubrics / Tools Needed

| Tool | Purpose | Owner |
| --- | --- | --- |

### 4. Risks

- 避免理論堆疊而不可操作：
- 避免引用不精確：
- 避免與現有 L1-L5 術語衝突：

### 5. Suggested Text Blocks

提供可直接放入 repo 的短段落草稿。
```

## 步驟 4：若使用者要求，直接修補

若使用者明確要求「幫我加進去」或「直接修改 repo」，Codex 應：

1. 先檢查相關文件。
2. 用最小可行修改補入內容。
3. 避免破壞既有 Antigravity / Claude / AGENTS 設計。
4. 在 final answer 中列出修改檔案。

## 注意事項

- 不要把學術理論變成裝飾引用。
- 每個理論都要連到具體工具、量表、模板或顧問動作。
- 若不確定引用細節，明確標示需要後續 bibliographic verification。

