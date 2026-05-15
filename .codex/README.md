# Codex Workflows

> 註解：這個目錄存放 Codex 使用者可召喚的對話式工作流。它讓本 repo 從「AI-native 活書」進一步變成 Codex 可操作的「對話式顧問應用程式」。

## 使用方式

在 Codex 對話中輸入：

```text
/diagnose
```

或：

```text
請依 .codex/workflows/diagnose.md 執行
```

即可啟動互動式 AI 成熟度診斷。

診斷完成後輸入：

```text
/generate-report
```

或：

```text
請依 .codex/workflows/generate-report.md 執行
```

即可將對話內容整理成顧問診斷報告草稿。

## 工作流清單

| 工作流 | 檔案 | 用途 |
| --- | --- | --- |
| `/diagnose` | [`workflows/diagnose.md`](workflows/diagnose.md) | 透過互動式提問完成 L1-L5 成熟度初判 |
| `/generate-report` | [`workflows/generate-report.md`](workflows/generate-report.md) | 將診斷對話轉成顧問報告 Markdown 草稿 |
| `/evidence-audit` | [`workflows/evidence-audit.md`](workflows/evidence-audit.md) | 檢查報告主張是否能回指到 evidence，標出 unsupported claims |
| `/academic-upgrade` | [`workflows/academic-upgrade.md`](workflows/academic-upgrade.md) | 把學者建議轉成章節補強、模板修補與 repo patch plan |
| `/consistency-review` | [`workflows/consistency-review.md`](workflows/consistency-review.md) | 跨文件審查 L1-L5、Stage Gate、HITL、Evidence 與交付邏輯一致性 |

## Codex 行為要求

- 每次工作流啟動時，先讀取對應 Markdown。
- 若資訊不足，先問使用者，不要自行補完。
- 所有評分與報告章節都要能回指到 repo 內的問卷、評分模型、BARS 或顧問模板。
- 報告草稿不是正式交付，需由人類顧問 / 客戶 Owner / Sponsor 審核。

## Codex 與其他 AI IDE 的差異

Antigravity 工作流偏向「互動式顧問體驗」。Codex 工作流額外強調「可維護、可審查、可修補」：

- 能對 repo 進行跨文件一致性審查。
- 能把理論建議轉成具體 Markdown patch。
- 能檢查顧問報告是否有 evidence chain。
- 能協助檢查這本活書的版本化知識結構，但不取代 Claude 的主維護角色。
- 能作為後續方法論 CI/CD 工作流的承載目錄，但新增工作流應由實際作者各自提交與署名。
