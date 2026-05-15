# /generate-report

> 註解：這是 Antigravity 專屬的報告產出工作流。利用先前對話中取得的診斷資訊，自動填入顧問報告模板中，發揮 AI IDE 的產能。

## 步驟 1：讀取模板與確認資訊
- **目標**：載入報告模板並盤點所需資訊。
- **動作**：
  - 使用 `view_file` 工具讀取 `03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md` (或對應的中文版)。
  - 盤點先前的對話歷史，檢查是否已具備足夠的資訊 (如客戶名稱、問題痛點、成熟度級別等)。
  - 若資訊不足，簡短詢問使用者補充。**等待使用者回答。**

## 步驟 2：產出報告草稿 (Artifact)
- **目標**：撰寫並結構化輸出報告。
- **動作**：
  - 將收集到的所有客製化資訊，精準填入報告模板對應的章節（例如：1. Executive Summary, 6. Gap Analysis, 7. Executive Problem Statement）。
  - 將完成的報告使用 Markdown Artifact 的格式產出給使用者。
  - 加上註解說明：提醒使用者重點審查「§5.4 Ideal Practice Definition Table (三方簽署版)」以及「§13.2 Risk Register」，這些是落地的關鍵環節。
