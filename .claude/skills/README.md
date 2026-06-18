# Claude Code Skills

> 註解：這個目錄存放 **Claude Code 原生 Skills**（`.claude/skills/<名>/SKILL.md`）。與 [`.claude/workflows/`](../workflows/)（舊式共讀工作流）不同——Skills 會被 Claude Code **自動發現**，可打 `/<名>` 呼叫，也可被 Claude 依 `description` **自動觸發**。

## 零安裝

把 `SKILL.md` 放進 `.claude/skills/<名>/` 就生效——**不必改 `settings.json`、不必重開**，當前 session 即可用。唯一需要「安裝程序」的是打包成 plugin 給別人 `/plugin install`（本 repo 目前不做）。

## Skill 清單

### 學術投稿 Skills（雙引擎：另有 Codex `.codex/workflows/` 對應版，內容同步）

| Skill | 用途 | Codex 對應 |
|---|---|---|
| [`/claim-audit`](claim-audit/SKILL.md) | 稽核**學術稿件**主張、標 overclaim（顧問報告請用 evidence-audit）| [`.codex/workflows/claim-audit.md`](../../.codex/workflows/claim-audit.md) |
| [`/hype-scrub`](hype-scrub/SKILL.md) | 投稿用語清理（hype 詞 / buzzword）、保留已定義術語 | [`.codex/workflows/hype-scrub.md`](../../.codex/workflows/hype-scrub.md) |
| [`/reviewer-response`](reviewer-response/SKILL.md) | 審稿意見→逐點回覆信草稿 + 改動清單 | [`.codex/workflows/reviewer-response.md`](../../.codex/workflows/reviewer-response.md) |

> 完整使用手冊（草稿→投稿→審稿回覆 全管線）：[`../../09_Research_Paper/PUBLISHING_WORKFLOW_MANUAL.md`](../../09_Research_Paper/PUBLISHING_WORKFLOW_MANUAL.md)
> 敘事版（情境故事）：[`../../09_Research_Paper/PUBLISHING_WORKFLOW_SCENARIO.md`](../../09_Research_Paper/PUBLISHING_WORKFLOW_SCENARIO.md)

## 維護紀律

- **雙引擎同步**：每個 skill 都有 Codex workflow 對應版；改一份請同步另一份（兩邊檔頭都有互指 pointer）。
- **產出皆為草稿**：所有 skill 產出由人類作者負責、查證、署名。
- Skill frontmatter 的 `description` 決定 Claude 何時自動觸發；若只想手動 `/呼叫`，可加 `disable-model-invocation: true`。
