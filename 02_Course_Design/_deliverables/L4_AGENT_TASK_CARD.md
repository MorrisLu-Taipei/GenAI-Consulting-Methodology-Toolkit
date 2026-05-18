# L4 Hermes Agent 任務卡範本 / L4 Hermes Agent Task Card Template

> 對應課程 / Course: [L4_HERMES_AGENT_COURSE_PLAN.md](../L4_HERMES_AGENT_COURSE_PLAN.md) §3.4 + §7.1 Section 6 Workshop
> 版本 / Version: 範本 v1.0（學員 + 部門主管共同填）/ Template v1.0 (filled jointly by learner + dept manager)
> 授權 / License: Apache 2.0

---

## Task Card / 任務卡

| 欄位 / Field | 內容 / Content |
|---|---|
| **Agent 名稱 / Agent name** | `[例：QC-Knowledge-Agent / e.g., QC-Knowledge-Agent]` |
| **部門 / Department** | `[填入 / fill in]` |
| **Owner（人）/ Owner (human)** | `[填入姓名 + email / fill in name + email]` |
| **建立日期 / Created** | `[YYYY-MM-DD]` |
| **版本 / Version** | v0.1 |
| **狀態 / Status** | Draft / In Pilot / Production |

---

## 1. Mission（任務） / Mission

**一句話描述這個 Agent 解決什麼工作 / One-sentence description of what work this Agent solves：**

`[例：累積品保部門 QC SOP、不良品案例、製程改善知識，回答跨班別跨產線的「之前怎麼處理」問題]`
`[e.g., Accumulate QC dept knowledge across SOPs, defect cases, process improvements; answer "how was this handled before" across shifts and lines]`

---

## 2. 任務邊界 / Task Boundaries

### 2.1 允許的輸入 / Allowed inputs

- ✅ `[例：QC 日 / 週 / 月報 / e.g., QC daily/weekly/monthly reports]`
- ✅ `[例：物料規格表 / e.g., Material specifications]`
- ✅ `[例：製程 SOP / e.g., Process SOPs]`
- ✅ `[例：不良品分析報告 / e.g., Defect analysis reports]`

### 2.2 禁止的輸入 / Forbidden inputs

- ❌ `[例：人事 / 組織資料 / e.g., HR / org data]`
- ❌ `[例：財務數據 / e.g., Financial data]`
- ❌ `[例：客戶 PII / e.g., Customer PII]`
- ❌ `[例：跨部門資料（行銷 / HR）/ e.g., Cross-dept data]`

### 2.3 處理範圍 / Processing scope

- ✅ `[例：摘要、結構化、跨檔關聯 / e.g., Summarize, structure, cross-link]`
- ❌ `[例：不做主觀判斷、不下結論 / e.g., No subjective judgment, no final calls]`

---

## 3. IPOE

| 類別 / Category | 定義 / Definition |
|---|---|
| **Input** | `[例：PDF / docx QC 報告，每天 5-10 份 / e.g., 5-10 PDF/docx QC reports daily]` |
| **Process** | `[例：1. 來源分析 2. 關鍵字抽取 3. 寫入 knowledge base 4. lint 5. 索引]` |
|             | `[e.g., 1. Source analysis 2. Keyword extraction 3. Write to KB 4. Lint 5. Index]` |
| **Output** | `[例：結構化知識頁（概念/實體/主張）+ 摘要 + 引用來源 / e.g., Structured knowledge pages + summary + citations]` |
| **Evidence** | `[例：每次 ingest 留 log（檔名 + 時間 + 抽取結果 + confidence）/ e.g., Per-ingest log: filename + time + extraction + confidence]` |

---

## 4. Human Gate 設計 / Human Gate Design

### 4.1 觸發條件 / Triggers

| # | 條件 / Condition | Reviewer | SLA |
|---|---|---|---|
| 1 | confidence < 0.7 | QC 主管 / QC Lead | 8 hr |
| 2 | 來源檔含「客戶名稱」/ Source contains "customer name" | 法務 / Legal | 24 hr |
| 3 | 跨 SOP 衝突 / Cross-SOP conflict | QC 主管 / QC Lead | 24 hr |
| 4 | 新增類別到 knowledge base / New category in KB | Owner + 主管 / Owner + lead | 48 hr |

### 4.2 escalation 規則 / Escalation rules

- SLA 超過 2x → 升 1 級 / SLA exceeds 2x → escalate 1 level
- Reject 累積 ≥ 3 次 → 重審 Agent 設計 / ≥ 3 rejections → revisit Agent design

---

## 5. 接入的 L2 Skill + L3 Workflow / Connected L2 Skills + L3 Workflows

| 類型 / Type | 名稱 / Name | 版本 / Version | 用途 / Use |
|---|---|---|---|
| L2 Skill | KeywordExtraction | v1.2 | 從新報告抽關鍵字 |
| L2 Skill | DocClassification | v0.9 | 判斷文件類型 |
| L3 Workflow | DailyReportIngest | v2.0 | 每日 02:00 自動 ingest |
| L3 Workflow | WeeklySummaryEmail | v1.5 | 每週一早寄主管摘要 |

---

## 6. KPI

| 指標 / Metric | 目標 / Target | 量測方式 / Measurement |
|---|---|---|
| Ingest 成功率 / Ingest success rate | ≥ 95% | success / total per day |
| 平均 query 回應時間 / Avg query latency | < 5 sec | p95 query time |
| 知識庫成長 / KB growth | +50 知識頁/月 / +50 pages/month | new pages per month |
| 主管詢問被滿足率 / Manager query satisfaction | ≥ 80% | survey after each query |
| 人工 Gate 通過率 / Human Gate pass rate | 70-90% | passed / total reviews |

> Pass rate < 70% → Agent 太激進 / too aggressive
> Pass rate > 90% → Agent 太保守，gate 失去意義 / too conservative, gate is theater

---

## 7. 風險清單 / Risk Register

| # | 風險 / Risk | 機率 / Prob | 影響 / Impact | 緩解 / Mitigation |
|---|---|---|---|---|
| 1 | Knowledge base 灌入錯誤資料 / KB polluted with wrong data | 中 | 高 | Lint + 人工 sample 抽查 / Lint + sample audit |
| 2 | Agent 自動發布未審內容 / Auto-publish unreviewed | 低 | 極高 | Mission file 明禁 + HITL gate |
| 3 | LLM 成本超支 / LLM cost overrun | 中 | 中 | 月度 cost cap + alert |
| 4 | 跨部門資料誤入 / Cross-dept data leak | 低 | 高 | Forbidden list + auto-reject |

---

## 8. 上線檢查表 / Go-live Checklist

通過 Gate 4A-4E 後才上線 / Live only after passing Gates 4A-4E (見 §10 / see §10):

- [ ] Gate 4A：環境可用 / Environment ready
- [ ] Gate 4B：知識底座可用 / KB ready
- [ ] Gate 4C：Ingest 閉環 / Ingest loop closes
- [ ] Gate 4D：查詢與更新 / Query & update
- [ ] Gate 4E：營運與治理 / Ops & governance

## 9. 簽核 / Sign-off

| 角色 / Role | 簽名 / Signature | 日期 / Date |
|---|---|---|
| Agent Owner | __________ | __________ |
| 部門主管 / Dept Lead | __________ | __________ |
| IT / Platform | __________ | __________ |
| Security / Legal | __________ | __________ |

下次 review / Next review: `[填入 3 個月後 / fill in 3 months ahead]`
