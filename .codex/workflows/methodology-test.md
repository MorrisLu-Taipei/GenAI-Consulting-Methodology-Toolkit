# /test-methodology

> 註解：Codex 原生創舉 - 方法論的單元測試 (Methodology CI/CD)
> 用途：當更新了框架庫或修改了階段定義後，確保方法論在不同情境下的邏輯一致性，避免出現死胡同。

## 步驟 1：載入極端測試情境 (Edge Case Injection)
- 模擬三種極端客戶情境：
  1. 無 IT 人員的傳統製造業 (資源極缺)
  2. 高度監管的醫療院所 (合規極嚴)
  3. 全雲端的純軟體新創 (極度敏捷)

## 步驟 2：執行壓力測試 (Stress Test)
- 將最新的 `SKILL.md` 與 `CONSULTING_FRAMEWORKS_LIBRARY.md` 套用至上述情境。
- 檢查 L1-L5 的升級路徑是否出現：邏輯斷層、無法達成的 Evidence 要求、或是矛盾的 Gate Criteria。

## 步驟 3：產出測試報告與修補建議 (Test Report & Patch Plan)
- 若有衝突，立刻列出 "Failed Cases" 並給出具體的修補建議 (Methodology Patch Loop)。
