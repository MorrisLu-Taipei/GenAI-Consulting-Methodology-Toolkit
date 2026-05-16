# /generate-traceability

> 註解：Codex 原生創舉 - 方法論追溯矩陣 (Traceability Matrix) 自動維護
> 用途：確保「問卷題」→「成熟度判定」→「證據要求」→「報告產出」這四者的鐵三角證據鏈完整不斷裂。

## 步驟 1：矩陣映射掃描
- 讀取 `01_Assessment/AI_MATURITY_QUESTIONNAIRE.md` (資料來源)
- 讀取 `01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md` (證據要求)
- 讀取 `03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md` (最終呈現模板)

## 步驟 2：孤兒節點檢查 (Orphan Node Check)
- 標記任何「沒有對應證據的結論」或「沒有納入報告的問卷題」。

## 步驟 3：產出與更新 TRACEABILITY_MATRIX.md
- 自動產出或更新專案根目錄的追溯矩陣文件。
- 對於證據斷鏈的項目標示 `[BROKEN_LINK]`，並觸發 Deliverable Consistency Review 要求修補。
