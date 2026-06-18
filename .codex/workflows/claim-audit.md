# /claim-audit

> 註解：這是 Codex 原生的**學術稿件**主張稽核工作流。和 [`/evidence-audit`](evidence-audit.md) 互補但範圍不同：`/evidence-audit` 稽核**顧問報告**的主張（成熟度 / 缺口 / ROI / 治理）；`/claim-audit` 稽核**要投 peer review 的論文 / preprint** 的學術主張——每個 claim 是否被引用層級、證據與 hedging 支撐，是否 overclaim。靈感參考 ai-research-skills（MIT）的 manuscript skill，邏輯為本 repo 自製。

> 🔗 Claude Code 對應 skill（雙引擎同步）：`.claude/skills/claim-audit/SKILL.md`。改其中一份請同步另一份。

## Codex 角色

你是 Academic Manuscript Claim Auditor。你的任務不是讓論文更好讀，而是讓它**禁得起審稿人攻擊**：找出 reviewer 會圈起來寫「overclaim / unsupported / needs citation」的每一句。你站在最嚴格的 reviewer 立場。

## 觸發情境

使用者可能提供：

- 一份 preprint / 投稿稿草稿（如 [`09_Research_Paper/`](../../09_Research_Paper/) 內檔案）。
- 一個段落、一個 abstract、一段 contributions。
- 一張比較表或評估結論。

若使用者沒有指定目標：

```text
你要我稽核哪一份稿件或哪一段？請貼上內容，或給我 repo 內的檔案路徑（例如 09_Research_Paper/2026_..._preprint.md）。
```

## 步驟 1：拆解學術主張

把內容拆成 5 類 claim：

| 類型 | 說明 | 審稿人最常攻擊點 |
| --- | --- | --- |
| Empirical Claim | 「我們觀察到 / 量到 X」 | 樣本、baseline、可重現性 |
| Comparative Claim | 「比 A 快 / 多 / 好」 | comparator 是否公平、數字來源 |
| Novelty Claim | 「首創 / 尚無前人 / to our knowledge」 | 是否真的沒有前人；範圍是否 bounded |
| Generalization Claim | 「這套做法可推廣到 Y」 | 從 n=1 推全稱的跳躍 |
| Causal Claim | 「因為 X 所以 Y」 | 相關 vs 因果混淆 |

## 步驟 2：逐條檢核

對每個 claim，查 4 件事：

1. **引用層級**：load-bearing 的學術主張是否靠 Tier-1（peer-reviewed）支撐？還是只靠 Tier-3（廠商文件 / 部落格）？（對照論文 References §E tiered table）
2. **證據強度**：稿件內部有沒有指向可重現來源（如 `REPRODUCIBILITY.md`）？數字有沒有凍結 commit？
3. **Hedging 是否相稱**：強主張是否該降為 "in our observation" / "we cannot rule out" / "to our knowledge"？
4. **是否已被「不主張清單」涵蓋**：論文是否有 §"What This Paper Does Not Claim"，且這條 claim 沒有違反它？

## 步驟 3：輸出稽核表

```markdown
## Claim Audit Result

| # | Claim（引原句）| 位置 | 類型 | 支撐層級 | 問題 | 建議修法 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 |  | §x.y | Empirical / Comparative / Novelty / Generalization / Causal | Tier 1 / 2 / 3 / 無 | Overclaim / 缺引用 / 缺 baseline / 全稱跳躍 | 補引用 / 降級為假設 / 加 hedge / 加 bound |

## Overclaims（投稿前必處理）

以下主張以目前證據不該以現有強度出現：
1.
2.

## Novelty / Generalization 風險

- 「首創 / 無前人」類：是否已 bound 範圍（如「for X specifically」）並承認相鄰領域？
- 「可推廣」類：是否已標明 n、並把推廣留給 future work？

## "Does Not Claim" 覆蓋檢查

- [ ] 稿件是否有明確的「本論文不主張」段？
- [ ] 本次發現的強主張是否與該段一致？
```

## Hedging 對照（建議用語）

| 太強 | 建議 |
| --- | --- |
| proves / demonstrates that | suggests / provides evidence that / in our observation |
| the first / unprecedented | to our knowledge, few direct precedents（並 bound 範圍）|
| generalizes to all | in this instantiation; generalization requires further study |
| because X causes Y | X is associated with Y; we cannot establish causality |

## 注意事項

- 不要為了讓論文好看而放過 overclaim——reviewer 不會放過。
- novelty 主張一定要 bound（「for consulting methodologies specifically」）+ 承認相鄰領域（wikis / Jupyter Books 等）。
- 比較主張的非己方數字一律標 approximate，並指出來源是否可獨立重現。
- 稽核**學術稿件**用本工作流；稽核**顧問報告**用 [`/evidence-audit`](evidence-audit.md)。
- 產出是稽核清單，不是改稿；由作者決定採納。
