# consultant 框架庫引用與授權說明 / consultant Frameworks Citation & License Notice

> 🌐 English version: [CONSULTANT_FRAMEWORKS_REFERENCE_EN.md](CONSULTANT_FRAMEWORKS_REFERENCE_EN.md)

本方法論的 [`03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) 之框架清單與分類，參考並改寫自 **yoichiojima-2/consultant**。本檔詳列原始來源、授權條款、引用方式與改寫範圍。

The framework list and taxonomy in this methodology's [`03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) are referenced from and rewritten based on **yoichiojima-2/consultant**. This document records the upstream source, license terms, citation guidance, and scope of adaptation.

---

## 1. 原始專案 / Upstream Project

| 項目 / Field | 內容 / Value |
| --- | --- |
| **專案名稱 / Project** | consultant |
| **作者 / Maintainer** | @yoichiojima-2 |
| **GitHub URL** | <https://github.com/yoichiojima-2/consultant> |
| **授權 / License** | **MIT License** |
| **形式 / Form** | Claude Code plugin（透過 `/plugin marketplace add` 安裝） |
| **內容 / Content** | 50+ 個經典顧問框架（McKinsey / BCG / Bain / Accenture），分 7 大類，以 markdown skill 形式封裝 |

## 2. consultant 是什麼 / What is consultant

consultant 是一個 **Claude Code plugin**，把 50+ 個經典管理顧問框架（MECE、Pyramid Principle、Porter's 5 Forces、SWOT、BCG Matrix、PESTEL、5 Whys、Fishbone、Business Model Canvas、WBS、RACI、Kotter、OKR、NPV/IRR、Lean、Six Sigma 等）整理成 markdown skill。

consultant is a **Claude Code plugin** that packages 50+ classic management-consulting frameworks (MECE, Pyramid Principle, Porter's 5 Forces, SWOT, BCG Matrix, PESTEL, 5 Whys, Fishbone, Business Model Canvas, WBS, RACI, Kotter, OKR, NPV/IRR, Lean, Six Sigma, etc.) into a markdown skill.

### 結構特色 / Structural Features

- **7 大類分類**：問題解決 / 策略分析 / 案例框架 / 商業設計 / 專案與變革 / 財務分析 / 營運。
- **Trigger recognition**：以「I need to…」自然語言句子路由到框架組合。
- **Framework combinations**：預建多框架鏈（如 PESTEL → 5 Forces → 3C → SWOT → Issue Tree）。
- **每個框架的標準結構**：起源 / 核心概念 / 步驟 / 套用方式 / 真實範例 / common pitfalls。

## 3. 我們改寫並引用了什麼 / What We Adapted and Cited

| 範圍 / Scope | 處理方式 / Treatment |
| --- | --- |
| **框架清單與 7 大分類** | 參考其分類，重新以本方法論語言改寫 / Referenced the taxonomy, rewritten in this methodology's language |
| **「框架選擇器」概念**（自然語言 → 框架） | 借鑑 trigger-recognition 模式，重做成對應本方法論情境的選擇器 / Adapted the trigger-recognition pattern into a selector aligned with our scenarios |
| **「框架組合鏈」概念** | 借鑑 combination-chains 模式，對應到本方法論八階段 / Adapted the combination-chains pattern, mapped to our eight stages |
| **框架文件展開格式** | 參考其 per-framework 結構，加上「對應階段」一欄 / Referenced its per-framework structure, added a "maps-to-stage" column |
| **經典框架本身**（MECE、Porter's 5 Forces 等） | 為公開領域之管理知識，非 consultant 專屬 / Public-domain management knowledge, not proprietary to consultant |
| **原始 markdown skill 檔** | **未重製、未 fork**；本方法論為獨立改寫 / **Not reproduced, not forked**; this methodology is an independent rewrite |

## 4. 授權條款摘要 / License Summary

consultant 採用 **MIT License**。MIT 允許自由使用、修改、再散布、商業使用，並可作為閉源產品的一部分；**唯一條件**是再散布原始碼時保留 MIT 著作權聲明與授權文字。

本方法論**未重新散布** consultant 的原始碼，而是參考其框架清單與設計模式後**獨立改寫**為 `CONSULTING_FRAMEWORKS_LIBRARY.md`。改寫後之檔案採本 repo 的 Apache 2.0 授權；但我們仍於該檔與本檔中明確**備註引用來源**，以示尊重原作者貢獻。

consultant is released under the **MIT License**, which permits free use, modification, redistribution, and commercial use, including as part of a proprietary product; **the only condition** is preserving the MIT copyright notice and license text when redistributing the source.

This methodology does **not redistribute** consultant's source code — it independently rewrote `CONSULTING_FRAMEWORKS_LIBRARY.md` after referencing consultant's framework list and design patterns. The rewritten file is licensed under this repo's Apache 2.0; nevertheless, we explicitly **note the citation source** in that file and here, in respect of the original author's contribution.

## 5. 學員引用建議格式 / Citation Format for Learners

> Framework library adapted from consultant by @yoichiojima-2 — <https://github.com/yoichiojima-2/consultant> (MIT License)
> 框架庫改寫自 @yoichiojima-2 之 consultant — <https://github.com/yoichiojima-2/consultant> (MIT 授權)

## 6. 免責聲明 / Disclaimer

本方法論中對 consultant 之引用、改寫、與八階段對應，皆為本方法論作者（Morris Lu / Tiger AI 虎智科技）的詮釋，不代表 @yoichiojima-2 之官方立場。經典顧問框架之定義與應用，請以各框架原始學術 / 業界出處為準。若 consultant 之框架清單或結構有版本變動，請以 [上游 repo](https://github.com/yoichiojima-2/consultant) 之最新版本為準。

Any citation, adaptation, or eight-stage mapping of consultant in this methodology represents the interpretation of the methodology author (Morris Lu / Tiger AI 虎智科技) and does not represent the official position of @yoichiojima-2. For the definitions and application of classic consulting frameworks, refer to each framework's original academic / industry source. If consultant's framework list or structure changes in newer versions, refer to the [upstream repository](https://github.com/yoichiojima-2/consultant).
