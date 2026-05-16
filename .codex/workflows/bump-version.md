# /bump-version

> 註解：Codex 原生創舉 - 語意化版本控制與發布說明 (Semantic Versioning & Changelog)
> 用途：將「活書」視為真正的軟體產品，每次的方法論修補與升級都由 AI 自動進行版控與發布說明。

## 步驟 1：讀取變更差異 (Diff Analysis)
- 分析最近一次 `/methodology-test` 或 `/academic-upgrade` 對專案核心文件造成的實質變動。

## 步驟 2：決定版號 (SemVer)
- 若為修補錯字或小型證據斷鏈：升級 Patch (例如 v2.0.0 -> v2.0.1)
- 若為新增分析框架或 L1-L5 定義微調：升級 Minor (例如 v2.0.0 -> v2.1.0)
- 若為八階段結構性翻新：升級 Major (例如 v2.0.0 -> v3.0.0)

## 步驟 3：撰寫 CHANGELOG.md 與 README.md 更新
- 使用「高階商業顧問」的嚴謹語氣自動撰寫 Release Note。
- 說明本次更新對企業導入流程的實際影響與價值。
- 自動更新 `README.md` 中的版本號與發布日期。
