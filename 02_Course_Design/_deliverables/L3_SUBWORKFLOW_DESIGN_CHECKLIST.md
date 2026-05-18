# L3 Sub-workflow 設計 Checklist / L3 Sub-workflow Design Checklist

> 對應課程 / Course: [L3_N8N_TIGERAI_COURSE_PLAN.md](../L3_N8N_TIGERAI_COURSE_PLAN.md) §2.4 + §5.3 Advanced
> 版本 / Version: 範本 v1.0（學員 / reviewer 用）/ Template v1.0 (learner / reviewer use)
> 授權 / License: Apache 2.0

## 0. 什麼時候要切 Sub-workflow / When to split a Sub-workflow

切 sub-workflow 的 4 個 trigger / 4 triggers to split:

1. **重複出現** —— 同邏輯被 3 個以上 workflow 用到 / **Repeated** — same logic used in 3+ workflows
2. **節點數爆炸** —— 主 workflow > 30 nodes 視覺難讀 / **Node bloat** — main workflow > 30 nodes hard to read
3. **獨立業務責任** —— 「分類」「通知」「審核」「寫資料表」這類獨立工作 / **Independent responsibility** — classify / notify / review / write
4. **不同 SLA** —— 主流程要 5 秒內回，子流程可以慢慢處理 / **Different SLA** — main needs 5s response, sub can be async

---

## 1. Sub-workflow 設計 8 點 Checklist

### Layer A — 介面契約 / Interface contract

- [ ] **明確的 input schema** —— 列出每個欄位、型別、必填、預設值
       Clear input schema — fields, types, required, defaults
- [ ] **明確的 output schema** —— 同上
       Clear output schema — same
- [ ] **錯誤回傳格式** —— 失敗時返回什麼結構（status / message / retry_after）
       Error return shape — what's returned on failure

### Layer B — 獨立性 / Independence

- [ ] **無外部 state 依賴** —— Sub-workflow 不假設主流程留下任何 state
       No external state dependency — sub doesn't assume main left anything
- [ ] **冪等性** —— 同樣 input 跑 N 次得到同樣結果 / Idempotency — same input N times = same output

### Layer C — 治理 / Governance

- [ ] **獨立的 credential 範圍** —— 只用自己需要的，不繼承全 workflow 的
       Independent credential scope — only what's needed, not inherited
- [ ] **獨立的 log 寫入** —— 子流程的 log 可單獨被 query
       Independent log writes — sub-flow log can be queried alone
- [ ] **版本標記** —— 每個 sub-workflow 標 `vX.Y` 版本，更新走 deprecation policy
       Version tag — every sub-workflow tagged `vX.Y`, updates follow deprecation

---

## 2. 範例：「客戶分類」Sub-workflow / Example: "Customer Classification" Sub-workflow

### Input

```json
{
  "email_text": "string (required)",
  "customer_id": "string (optional, for context lookup)",
  "language_hint": "string (optional, default 'zh-TW')"
}
```

### Output

```json
{
  "status": "success | error",
  "category": "billing | technical | refund | general | complaint | abuse",
  "priority": "P0 | P1 | P2 | P3",
  "confidence": 0.85,
  "reasoning": "short text explaining classification",
  "error_message": "(only when status=error)"
}
```

### Error returns

- `status: "error"` + `error_message: "input_too_short"` if `email_text.length < 10`
- `status: "error"` + `error_message: "ai_unavailable"` if downstream LLM failed 3 times

### Independence check

- ✅ 不依賴主流程設過的環境變數 / No reliance on main-workflow env vars
- ✅ 跑 100 次同樣 input → 結果相同（confidence ±0.05 容差）/ 100 same-input runs → same result (±0.05 tolerance)

### Governance

- credential: 只有 `LLM_API_KEY`，沒有其他 / Only `LLM_API_KEY`, nothing else
- log: 寫到 `subworkflow_classification_log` 表，欄位 `id / input_hash / output / latency_ms / timestamp`
- 版本: `v1.2`；上次更新 2026-04-15；deprecation: v1.x 支援到 2027-04-15

---

## 3. Sub-workflow library 規劃 / Sub-workflow library planning

| Sub-workflow 類型 / Type | 典型範例 / Typical examples | 建議重用度 / Suggested reuse |
|---|---|---|
| AI 分類 / AI classification | Email 分類、Lead 評分、文件類型判斷 | 高 / High |
| AI 摘要 / AI summary | 會議摘要、長文摘要、報告摘要 | 高 / High |
| 通知 / Notification | Slack / LINE / Email / SMS 通知 | 高 / High |
| 人工審核 Gate / Human Gate | Approve / Reject + 註記 | 高 / High |
| 資料表寫入 / Data table write | 任 1 table 的 standard insert | 中 / Medium |
| 外部 API 呼叫 / External API call | CRM / ERP / 自家系統 | 中 / Medium |
| 錯誤處理 / Error handling | Retry / Fallback / 降級 | 高 / High |
| 驗證 / Validation | Schema check、PII detection | 中 / Medium |

> **目標：** 1 個成熟的 n8n 部門有 **5-10 個高重用 sub-workflow**，主 workflow 變得像「組裝積木」。/ **Goal:** Mature n8n team has 5-10 high-reuse sub-workflows; main workflows feel like "assembling Lego."

---

## 4. 反例：什麼不該切 sub-workflow / Anti-patterns

| 情境 / Scenario | 為什麼不該切 / Why not |
|---|---|
| 只被 1 個 workflow 用 / Used by only 1 workflow | 沒有 reuse 價值，徒增複雜度 / No reuse value, adds complexity |
| 邏輯 < 3 個節點 / Logic < 3 nodes | 切了反而難讀 / Splitting makes it harder to read |
| 需要主流程的 dynamic state / Needs main flow's dynamic state | 違反獨立性原則 / Violates independence |
| 跨 SLA 要求差異不明 / SLA difference unclear | 增加 async 複雜度沒收益 / Adds async complexity for no gain |

---

## 5. Reviewer Checklist

審查同學的 sub-workflow 設計時 / When reviewing peer's sub-workflow design:

- [ ] 8 點 checklist 全綠 / 8-point checklist all green
- [ ] 至少 1 個其他 workflow 真的接到它 / At least 1 other workflow actually plugs in
- [ ] Error 路徑有測 / Error path tested
- [ ] 版本與更新策略寫了 / Version + update policy documented
- [ ] 不踩 §4 的 4 個反例 / Doesn't hit the 4 anti-patterns in §4
