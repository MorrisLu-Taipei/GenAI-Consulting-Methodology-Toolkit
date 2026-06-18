# Claim Audit — AI-Native eBook Production preprint（2026-05-23）

> 仿 [ai-research-skills](https://github.com/WenyuChiou/ai-research-skills) 的 manuscript skill 邏輯（claim auditing / banned-word / 投稿用語），用本專案現有引擎對 preprint 跑一輪稽核。
> 稽核對象：[`2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md`](2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md)（EN canonical）+ ZH companion。
> **這是審稿者視角的清單，不是自動改稿。** 每項給「發現 → 嚴重度 → 建議」，由作者決定是否採納。

---

## ✅ 套用狀態（2026-05-23，同日套用）

使用者核可後，已對 EN + ZH preprint **實際套用**第 1、2、3 項。`/hype-scrub` + `/claim-audit` 重跑一遍時**多抓到 2 項原稿漏列**（見 §7 Bonus）。第 5、5b 項為「下次 deposit 決策」，保留未動。

| 項 | 狀態 |
|---|---|
| §1 pending/staged DOI → 實際 DOI | ✅ 已套用（EN+ZH，含 §8.2 漏網點）|
| §2 §E 計數重數 | ✅ 已套用（32 total = Tier1 11 / Tier2 5 / Tier3 16，含計數規則 + Tier-3 表補滿 16 列）|
| §3 unprecedented / cryptographically | ✅ 已套用（EN+ZH）+ §7 Bonus 的 ZH「顛覆→翻轉」|
| §5 兩 commit 澄清 | ✅ 已套用（§3.1 加 7da82d7=數值凍結 / 5361c7b=發布觸發 的角色說明，EN+ZH）|
| §5b 工作流計數定義 | ✅ 已套用（§3.1 加「workflow 計數範圍」note：22 = 方法論生產 workflow，投稿/meta workflow 排除，HEAD 仍為 22；Appendix A 同步，EN+ZH）|

---

## 0. 總體判斷

**這篇論文的引用與主張紀律已經相當好**——有 §9.4「本論文不主張之事」、tiered citation（Tier 1/2/3）、§9.2 比較表逐欄 footnote 並標 approximate、大量 hedging（"in our observation" / "to our knowledge" / "we cannot rule out"）。下列為**殘餘**項目，多屬中低嚴重度，主要是「部署後資訊變舊」與「一處既存計數不一致」。

---

## 1. 事實性：deposit 後的「pending / staged」字眼已過時（中嚴重度）

論文多處仍寫成「尚未 deposit」的狀態，但 Zenodo DOI 其實**已 mint**（front-matter 已列 concept/version DOI）。

| 位置 | 現在寫法 | 問題 | 建議 |
|---|---|---|---|
| §1.3 貢獻 #2 | "staged for release under Apache 2.0 with a **pending** Zenodo DOI" | DOI 已發 | 改 "released under Apache 2.0 with Zenodo DOI [10.5281/zenodo.20261680]" |
| §9.1 Hevner 表 #1 | "Apache 2.0, 354 files, **pending Zenodo DOI**" | 同上 | 補上實際 DOI |
| §9.1 Hevner 表 #7 | "**pending** Zenodo DOI" | 同上 | 同上 |

> 影響：審稿者若對照 front-matter（已有 DOI）與內文（pending），會覺得稿件未同步。屬「部署後沒回頭改」的常見問題。

---

## 2. 內部一致性：References §E 計數不符（中嚴重度，**既存問題**）

- §E 摘要原寫「27 references total（Tier 3: 11）」，但 Tier-3 表格**原本就列了 13 列**（2 列落差，疑似把兩筆政府著作權 FAQ 或 Lu in-prep 排除在計數外）。
- 本次修訂新增 2 筆 Chiou（Tier-3），我**維持原本的 +2 偏移**：摘要改 29（Tier 3: 13），表格現為 15 列。**落差仍是 2 列，未擴大。**

**建議：** 下次 deposit 前重數一次，讓「摘要數字 = 表格列數」完全一致（決定 Lu in-prep 與兩筆 copyright FAQ 是否計入），並在 audit note 說明計數規則。

---

## 3. 投稿用語（hype words）：少數可再收斂（低嚴重度）

論文整體很克制，僅幾處：

| 位置 | 字眼 | 建議 |
|---|---|---|
| §2.4 | "a fresh instantiation of this thesis at **unprecedented** scale" | "unprecedented" 是審稿常被點的 hype 詞；改 "at a new scale"（與全文他處用法一致）|
| Abstract | "**cryptographically** reproducible derivation through Git history" | Git 是 content-addressed（SHA），技術上可辯護，但 "cryptographically" 易被讀成 overclaim；建議 "content-addressed (Git-based) reproducible derivation" 或加一句腳註說明指 SHA 內容定址 |

> 其餘如 "living artifact"、"cognitive workbench" 屬已定義的術語，保留。

---

## 4. 主張範圍：已良好（無行動，記錄佐證）

下列原本就處理得當，列出供放心：
- n=354 / 7 語 / 22 workflows / 94 commits → 全數指向 `REPRODUCIBILITY.md`，可重現。✅
- §9.2 比較表非-Toolkit 欄位明確標 "approximate / not independently reproducible"。✅
- §4.0 GitHub 段主動承認 wikis / Jupyter Books / GitBook 在相鄰領域有類似效果，主張 bounded。✅
- §9.4 明列「非 peer-reviewed / 非實證驗證 / 非 AI 作者」三不主張。✅

---

## 5. 小一致性：兩個 commit hash 並存（低嚴重度）

- §3.1 數字凍結於 commit `7da82d7`；front-matter 發布 tag 為 `5361c7b`（v3.0.1）。
- 兩者角色不同（數字凍結點 vs 發布 tag），但審稿者可能困惑。

**建議：** §3.1 加半句註明「數字凍結 commit 與發布 tag 為不同 commit，前者是 metric 凍結點，後者是 Zenodo 觸發點」。

---

## 5b. 工作流計數：live repo 已與凍結值分歧（低嚴重度，需下版處理）

2026-05-23 新增 3 個 Codex 投稿工作流（`/claim-audit`、`/hype-scrub`、`/reviewer-response`）。

- 論文 §3.1 / Appendix A 凍結值：**22（10 Claude Code / 10 Codex / 2 Antigravity）@ commit `7da82d7`** —— 此陳述**仍為真**（明確標 frozen-at-commit）。
- 但 `REPRODUCIBILITY.md` 若在 HEAD 重數，現為 **25（10 / 13 / 2）**。

**建議（擇一，下次 deposit 處理）：**
- (a) 下版重新凍結於新 commit，數字更新為 25；或
- (b) 把論文計數定義為「**方法論生產工作流**」，明確排除投稿 / meta 工作流（claim-audit 等），並在 §3.1 加半句定義。

> 傾向 (b)：這 3 個是「生產論文」用的 meta 工作流，與「生產 eBook 方法論內容」的 22 個本質不同。

## 7. Bonus：重跑 /hype-scrub + /claim-audit 多抓到的（原稿漏列）

實際用新做的 workflow 全文掃描，比原始人工稽核多抓到 2 處：

1. **第 4 個 "pending DOI" 點（§8.2 持久識別符）** —— 原 audit §1 只列了 §1.3 + §9.1 兩處（共 3 個），全文 grep 發現 §8.2 還有一個「the pending Zenodo DOI ... will provide ... after the v1.0.0 tag is released」。已一併改為已發布事實。
2. **ZH「顛覆此模式」（§5.1）** —— EN 原文是 "inverts this"（翻轉），ZH 卻譯成「顛覆」（disrupt，hype 連帶）。已對齊為「翻轉此模式」。

> 這正是 `/hype-scrub`、`/claim-audit` 作為**全文掃描** workflow 的價值：人工讀重點章節會漏，工具掃全文不會。

## 6. 行動清單（給作者勾選）

- [x] §1.3 + §9.1 + **§8.2**（共 4 處）把 "pending / staged" 改成已發 DOI ✅ 2026-05-23
- [x] §E 重數，摘要數字 = 表格列數，註明計數規則 ✅（32 = 11/5/16）
- [x] §2.4 "unprecedented" → "new"；Abstract "cryptographically" → "content-addressed" ✅
- [x] ZH §5.1「顛覆」→「翻轉」對齊 EN "inverts" ✅（§7 Bonus）
- [x] EN 改完同步 ZH（preprint_ZH.md）✅
- [x] §3.1 加一句澄清兩個 commit 的角色 ✅ 2026-05-23
- [x] 工作流計數定義：採「方法論生產 workflow = 22」口徑，投稿/meta workflow 排除（§3.1 note + Appendix A，EN+ZH）✅ 2026-05-23

> **全部 audit 項目已 close。** 餘下僅 REPRODUCIBILITY.md §3.3 的驗證指令若要在 HEAD 重跑、且要回傳 22，需加一行排除 `.codex/workflows/{claim-audit,hype-scrub,reviewer-response}.md`；惟論文已明定數字凍結於 `7da82d7`（該 commit 當下即 22），故非必要，列為 optional。

> 註：第 1、2 項屬「部署後同步」與「透明度表」，是投 peer review 前**最該先修**的兩項；第 3-5 項是錦上添花。

---

**稽核者：** Claude（Opus）· 受 Morris Lu 委託
**方法：** 對 abstract / §1 / §2 / §3.1 / §4.0 / §9 / §10 / §11 / References 全讀後人工標註（非全文逐行）
**日期：** 2026-05-23
**授權：** 隨本 toolkit
