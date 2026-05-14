# mckinsey-consultant-skills 引用與授權說明 / mckinsey-consultant-skills Citation & License Notice

> 🌐 English version: [MCKINSEY_SKILLS_REFERENCE_EN.md](MCKINSEY_SKILLS_REFERENCE_EN.md)

本方法論的 [`03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) 之生產工作流，參考並改寫自 **Kafurtan/mckinsey-consultant-skills**。本檔詳列原始來源、授權條款、引用方式與改寫範圍。

The production workflow in this methodology's [`03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) is referenced from and rewritten based on **Kafurtan/mckinsey-consultant-skills**. This document records the upstream source, license terms, citation guidance, and scope of adaptation.

---

## 1. 原始專案 / Upstream Project

| 項目 / Field | 內容 / Value |
| --- | --- |
| **專案名稱 / Project** | mckinsey-consultant-skills（V3.1） |
| **作者 / Maintainer** | @Kafurtan |
| **GitHub URL** | <https://github.com/Kafurtan/mckinsey-consultant-skills> |
| **授權 / License** | **MIT License** |
| **形式 / Form** | AI agent skill（`SKILL.md` + `references/`） |
| **內容 / Content** | 把「業務問題 → McKinsey 風格簡報」自動化的 8 步工作流，90-110 分鐘端到端 |

## 2. mckinsey-consultant-skills 是什麼 / What is mckinsey-consultant-skills

它把 McKinsey Problem Solving 方法論系統化為一條 **8 步工作流**，讓 AI 助手能把業務問題轉成專業簡報（PPT + Excel 證據軌）。

It systematizes McKinsey's Problem Solving methodology into an **8-step workflow** that lets an AI assistant turn a business problem into a professional presentation (PPT + Excel evidence trail).

### 結構特色 / Structural Features

- **8 步工作流**：定義邊界 → Issue Tree + 假設 → Dummy Pages + 設計規格 → 逐頁迭代生產 → PPT + Excel → 選配 Word 報告 → 迭代修訂。
- **Dummy Page**：先做線框規格再研究，避免無方向蒐集資料、支援跨對話接續。
- **Dependency awareness**：頁面標註依賴狀態，決定生產順序（執行摘要最後做）。
- **7 個頁面版型**：標題+單圖 / 雙欄 / 2×2 矩陣 / 表格 / 瀑布圖 / 時間軸 / 洞察摘要。
- **Excel 證據軌**：每頁原始資料 + URL + 清理過程。
- **Progressive disclosure**：參考檔只在需要的步驟載入、用完釋放，省 ~70% context。
- `references/`：methodology.md、layouts.md、design-specs.md、examples.md、troubleshooting.md。

## 3. 我們改寫並引用了什麼 / What We Adapted and Cited

| 範圍 / Scope | 處理方式 / Treatment |
| --- | --- |
| **8 步生產工作流** | 參考其流程，重新以本方法論語言改寫，對應到八階段顧問結構 / Referenced the workflow, rewritten in this methodology's language, mapped to the eight-stage structure |
| **Dummy Page 概念** | 借鑑「先骨架後填充」紀律，重做成本方法論的 deck outline 逐頁規格化 / Adapted the "skeleton-first" discipline into per-page specs for our deck outlines |
| **Dependency awareness** | 借鑑頁面依賴管理概念 / Adapted the page-dependency concept |
| **7 個頁面版型** | 參考其版型清單，重新改寫並補強 `VISUAL_ASSETS_SPEC.md` / Referenced the layout list, rewritten to extend `VISUAL_ASSETS_SPEC.md` |
| **Excel 證據軌、progressive disclosure** | 借鑑概念，對應到本方法論的 Evidence 紀律與 AI IDE context 管理 / Adapted the concepts, mapped to our Evidence discipline and AI-IDE context management |
| **McKinsey Problem Solving、MECE、Pyramid Principle** | 為公開領域之管理知識，非本專案專屬 / Public-domain management knowledge, not proprietary to this project |
| **原始 `SKILL.md` 與 `references/` 檔** | **未重製、未 fork**；本方法論為獨立改寫 / **Not reproduced, not forked**; this methodology is an independent rewrite |

## 4. 授權條款摘要 / License Summary

mckinsey-consultant-skills 採用 **MIT License**。MIT 允許自由使用、修改、再散布、商業使用，並可作為閉源產品的一部分；**唯一條件**是再散布原始碼時保留 MIT 著作權聲明與授權文字。

本方法論**未重新散布**其原始碼，而是參考其工作流與設計模式後**獨立改寫**為 `REPORT_PRODUCTION_WORKFLOW.md`。改寫後之檔案採本 repo 的 Apache 2.0 授權；但我們仍於該檔與本檔中明確**備註引用來源**，以示尊重原作者貢獻。

mckinsey-consultant-skills is released under the **MIT License**, which permits free use, modification, redistribution, and commercial use, including as part of a proprietary product; **the only condition** is preserving the MIT copyright notice and license text when redistributing the source.

This methodology does **not redistribute** its source code — it independently rewrote `REPORT_PRODUCTION_WORKFLOW.md` after referencing the workflow and design patterns. The rewritten file is licensed under this repo's Apache 2.0; nevertheless, we explicitly **note the citation source** in that file and here, in respect of the original author's contribution.

## 5. 學員引用建議格式 / Citation Format for Learners

> Production workflow adapted from mckinsey-consultant-skills by @Kafurtan — <https://github.com/Kafurtan/mckinsey-consultant-skills> (MIT License)
> 生產工作流改寫自 @Kafurtan 之 mckinsey-consultant-skills — <https://github.com/Kafurtan/mckinsey-consultant-skills> (MIT 授權)

## 6. 免責聲明 / Disclaimer

本方法論中對 mckinsey-consultant-skills 之引用、改寫、與八階段對應，皆為本方法論作者（Morris Lu / Tiger AI 虎智科技）的詮釋，不代表 @Kafurtan 之官方立場。「McKinsey」為 McKinsey & Company 之商標，本方法論與 McKinsey & Company 無任何隸屬或背書關係；相關方法論名稱僅作為公開領域管理知識之指稱。若 mckinsey-consultant-skills 之工作流或結構有版本變動，請以 [上游 repo](https://github.com/Kafurtan/mckinsey-consultant-skills) 之最新版本為準。

Any citation, adaptation, or eight-stage mapping of mckinsey-consultant-skills in this methodology represents the interpretation of the methodology author (Morris Lu / Tiger AI 虎智科技) and does not represent the official position of @Kafurtan. "McKinsey" is a trademark of McKinsey & Company; this methodology has no affiliation with or endorsement from McKinsey & Company, and related methodology names are used only as references to public-domain management knowledge. If mckinsey-consultant-skills' workflow or structure changes in newer versions, refer to the [upstream repository](https://github.com/Kafurtan/mckinsey-consultant-skills).
