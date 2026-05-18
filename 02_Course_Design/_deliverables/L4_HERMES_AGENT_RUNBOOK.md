# L4 Hermes Agent Runbook

> 對應課程 / Course: [L4_HERMES_AGENT_COURSE_PLAN.md](../L4_HERMES_AGENT_COURSE_PLAN.md) §3.4 + §12 Deliverables
> 版本 / Version: 範本 v1.0（部門 Agent Owner + IT 共填）/ Template v1.0 (filled by Agent Owner + IT)
> 授權 / License: Apache 2.0

## 0. Runbook 定位 / Purpose

Hermes Agent **上線後維運必備**——故障時誰 on-call、要看什麼 dashboard、怎麼處理、怎麼決定要不要 escalate。
**Post-launch operations essentials** — who's on-call during incidents, which dashboard, how to handle, when to escalate.

---

## 1. Agent 基本資料 / Agent Info

| 欄位 / Field | 內容 / Content |
|---|---|
| Agent 名稱 / Name | `[填入 / fill in]` |
| 部門 / Department | `[填入 / fill in]` |
| 上線日 / Launch date | `[填入 / fill in]` |
| 當前版本 / Current version | `[填入 / fill in]` |
| Owner（人）/ Owner | `[填入 + 緊急聯絡 / fill in + emergency contact]` |
| Backup Owner | `[填入 / fill in]` |

---

## 2. 服務時段 / Service Hours

| 模式 / Mode | 時段 / Time | 響應 SLA / Response SLA |
|---|---|---|
| Office hours | 工作日 9:00-18:00 / Workdays 9-18 | 30 min |
| After hours | 工作日 18:00-9:00 / Workdays 18-9 | 4 hr |
| Weekend | 週末 / Weekend | 8 hr |
| Emergency | 任何時間 P0 / P0 anytime | 15 min |

---

## 3. 日常維運 SOP / Daily Operations SOP

### 3.1 每日早晨檢查（5 分鐘）/ Daily morning check (5 min)

| # | 動作 / Action | 預期 / Expected |
|---|---|---|
| 1 | 看 Daily Briefing email / Read Daily Briefing email | 有寄達 + 摘要清楚 / Received + summary clear |
| 2 | 看夜間 ingest log / Check overnight ingest log | success rate ≥ 95% |
| 3 | 看 task tracking 未處理項 / Check task tracking unhandled | < 5 items |
| 4 | 看 Gate queue / Check Gate queue | 無 SLA 過期 / No SLA breach |

任 1 項異常 → 走 §4 故障處理 / Any anomaly → §4 incident handling.

### 3.2 每週 review（30 分鐘）/ Weekly review (30 min)

| # | 動作 / Action |
|---|---|
| 1 | 看 KPI dashboard / Review KPI dashboard |
| 2 | 看本週新加知識頁 sample / Sample new KB pages |
| 3 | 看 Reject 累積 / Review rejection trends |
| 4 | 看 LLM cost / Review LLM cost |
| 5 | 更新 Task Tracking File 上週 issue / Update Task Tracking with last week's issues |

### 3.3 每月 review（1 小時）/ Monthly review (1 hr)

- 跑 lint 全庫 / Run full-KB lint
- 跑失敗模式 review / Run failure mode review
- 跟 owner / 部門主管 review KPI / Review KPI with owner / dept lead
- 決定是否升版 / Decide version upgrade

---

## 4. 故障處理 / Incident Handling

### 4.1 P 等級定義 / P-level definitions

| 等級 / Level | 條件 / Condition | 響應 / Response |
|---|---|---|
| **P0** | Agent 完全無回應 / Agent fully unresponsive | 15 min |
| **P0** | 資料外洩疑慮 / Data leak suspicion | 15 min + 法務 / + legal |
| **P1** | KPI 跌破 50% / KPI drops below 50% | 1 hr |
| **P1** | 連續 ≥ 3 個 ingest 失敗 / ≥ 3 consecutive ingest failures | 1 hr |
| **P2** | 單一 query 異常 / Single query anomaly | 4 hr |
| **P3** | 改善建議 / Improvement suggestion | 下個 sprint / Next sprint |

### 4.2 處理步驟 / Handling steps

```text
1. Acknowledge（5 分內回 owner / Reply to owner within 5 min）
2. Investigate（看 Task Tracking + Log + KPI dashboard）
3. Decide：自己處理 / Escalate to IT / Escalate to AI Champion
4. Fix or rollback
5. Verify（5 個 sample query + KPI 恢復）
6. Post-mortem（P0 / P1 必寫；P2 視情況；P3 不必）
```

### 4.3 Rollback SOP

```text
1. 確認 last known good version：__________________
2. 暫停 Agent ingest / 暫停 cron / Pause Agent ingest / cron
3. 還原 knowledge base 到上次 snapshot（命令見 §6）/ Restore KB to snapshot
4. 重啟 Agent 到 last known good version / Restart at LKG
5. 跑 smoke test（5 個 standard query）/ Run smoke test
6. 全綠 → 恢復 ingest / All green → resume ingest
```

---

## 5. 升級與版本管理 / Versioning & Upgrades

### 5.1 何時要升版 / When to upgrade

- 新功能（新 Skill / 新 source / 新 schema）/ New feature
- 安全修補 / Security patch
- 失敗模式累積 ≥ 3 → 系統性改 / Failure modes ≥ 3 → systemic change

### 5.2 升版前必做 / Pre-upgrade checks

- [ ] 在 staging 跑 100 個歷史 query → ≥ 95% 跟 production 一致 / 100 historical queries in staging → ≥ 95% match prod
- [ ] Knowledge base snapshot 已建 / KB snapshot taken
- [ ] Rollback SOP 演練過 / Rollback SOP rehearsed
- [ ] Owner + 主管 signoff / Owner + lead signoff

---

## 6. 常用指令 / Common Commands

```bash
# 健檢 / Health check
hermes status

# 看 ingest log
hermes log --type=ingest --since=24h

# 觸發手動 ingest
hermes ingest --file=path/to/new.pdf

# 跑 lint
hermes lint --full

# Snapshot
hermes kb snapshot --name=before-v1.5-upgrade

# Restore
hermes kb restore --snapshot=before-v1.5-upgrade
```

> 注意：實際指令依您部署的 Hermes 版本而定，請以實際工具文件為準。
> Note: actual commands depend on your Hermes deployment; check the actual tool docs.

---

## 7. 緊急聯絡清單 / Emergency Contacts

| 角色 / Role | 名字 / Name | Phone | Email | Slack |
|---|---|---|---|---|
| Agent Owner | | | | |
| Backup Owner | | | | |
| 部門主管 / Dept Lead | | | | |
| IT On-call | | | | |
| AI Champion | | | | |
| Security On-call | | | | |
| 法務 / Legal | | | | |

---

## 8. Post-mortem 範本 / Post-mortem Template

```markdown
# Incident: [Brief title]
Date: [YYYY-MM-DD HH:MM]
P-level: [P0 / P1 / P2 / P3]
Duration: [X min/hr]

## Summary
[1 paragraph]

## Timeline
- HH:MM Detection
- HH:MM Acknowledgement
- HH:MM Investigation start
- HH:MM Root cause identified
- HH:MM Fix applied
- HH:MM Verified

## Root cause
[What actually broke]

## What worked
- ...

## What didn't
- ...

## Action items
- [ ] [Owner] [Due] [Item]
```

---

## 9. Runbook 維護 / Runbook Maintenance

- 每季 review 1 次 / Quarterly review
- 每次 incident 後 24 小時內更新 / Update within 24 hr after incident
- 重大架構變動立即更新 / Update immediately on major architecture change
- Owner 換人時必更新緊急聯絡清單 / Update emergency contacts on owner change

下次 review / Next review: `[填入 / fill in]`
