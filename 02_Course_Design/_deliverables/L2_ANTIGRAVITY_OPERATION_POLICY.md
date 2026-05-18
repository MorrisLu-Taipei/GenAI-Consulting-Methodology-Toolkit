# L2 Antigravity 操作政策表 / L2 Antigravity Operation Policy Table

> 對應課程 / Course: [L2_ANTIGRAVITY_COURSE_PLAN.md](../L2_ANTIGRAVITY_COURSE_PLAN.md) §3.4 + §6.1 Section 4
> 版本 / Version: 範本 v1.0（IT / Engineering Lead 填空）/ Template v1.0 (fillable by IT / Engineering Lead)
> 授權 / License: Apache 2.0

## 0. 政策定位 / Purpose

Antigravity 是 **Agentic IDE** —— Agent 能自主跑 terminal 指令、執行 JS、產生 code、開瀏覽器。**沒有治理 = Agent 失控**。本政策表是 IT 必填的 3 本柱設定。
Antigravity is an **Agentic IDE** — Agents can autonomously run terminal commands, execute JS, generate code, and drive the browser. **No governance = runaway Agent.** This policy table is the 3 mandatory governance pillars for IT.

---

## 1. 三本柱政策 / The Three Pillars

### 1.1 終端機執行政策 / Terminal Execution Policy

| 動作類型 / Action type | 預設政策 / Default | 何時改 / Adjust when |
|---|---|---|
| `ls / cat / grep / find` 等 read-only | **Allow** | 永遠允許 / Always allow |
| `mkdir / touch / cp` 等 file creation | **Allow** | workspace 內 / Within workspace |
| `git status / git diff / git log` | **Allow** | 永遠允許 / Always allow |
| `git commit / git push` | **Review** | 不 push 受保護分支 / Don't push protected branches |
| `npm install / pip install` | **Review** | 確認 package 來源 / Verify package origin |
| `rm -rf / sudo / chmod 777` | **Block** | 高破壞性 / High-destruction |
| 對外網路請求 / Outbound HTTP | **Review** | 確認 URL / Verify URL |
| Production 部署指令 / Production deploy | **Block** | 必須走 CI/CD 流程 / Must go through CI/CD |

**公司客製 / Company customization：**

| 動作 / Action | 公司政策 / Company policy |
|---|---|
| `[填入指令 / fill in command]` | Allow / Review / Block |
| `[填入指令 / fill in command]` | Allow / Review / Block |

### 1.2 Review Policy

| 觸發條件 / Trigger | Reviewer | SLA |
|---|---|---|
| Agent 修改 `production/` 目錄 / Agent modifies `production/` | Tech Lead | 4 hr |
| Agent 新增 dependency / Agent adds dependency | Tech Lead + Security | 24 hr |
| Agent 觸碰 `*.env / credentials.*` | Security 必審 / Security mandatory | 8 hr |
| Agent 跨檔案 ≥ 5 個改動 / Agent cross-file changes ≥ 5 | Tech Lead | 8 hr |
| Agent 想 push 到 main / Agent wants to push to main | Tech Lead | 24 hr |

**公司客製 / Company customization：**

| 觸發 / Trigger | Reviewer | SLA |
|---|---|---|
| `[填入 / fill in]` | `[填入 / fill in]` | `[填入 / fill in]` |

### 1.3 JavaScript 執行政策 / JavaScript Execution Policy

> Antigravity Browser 可以執行 JS。最大風險：XSS / 資料外洩 / cookie 偷竊。/ Antigravity Browser can execute JS. Top risks: XSS / data leak / cookie theft.

| 動作 / Action | 預設 / Default |
|---|---|
| 讀取頁面 DOM / Read page DOM | **Allow** |
| 填表 / Fill form | **Allow** |
| 點擊按鈕 / Click button | **Allow** |
| 觸發頁面內 AJAX / Trigger in-page AJAX | **Review** |
| 修改 localStorage / cookie | **Block** |
| 注入 third-party JS / Inject third-party JS | **Block** |
| 對 internal company URL 操作 / Operate on internal company URLs | **Block 或專案授權 / Block or per-project authorization** |

---

## 2. Safe Mode 啟動條件 / Safe Mode Triggers

啟動 Safe Mode 時：所有 terminal / JS / file-write 動作都走 Review，**等同對 Agent 上手銬**。
When Safe Mode is on: all terminal / JS / file-write actions go through Review — effectively handcuffing the Agent.

**何時必須啟動 / When mandatory：**

- [ ] 新 Agent / 新 task 第一次跑 / New Agent / new task first run
- [ ] 接觸 production code 時 / When touching production code
- [ ] 接觸 customer data 時 / When touching customer data
- [ ] 跨工作天的長 task / Long-running task spanning days
- [ ] 新 dependency 安裝後第一次跑 / First run after new dependency install

---

## 3. 治理截圖清單 / Governance Evidence Screenshots

Gate 2 驗收要求以下截圖 / Gate 2 acceptance requires the following screenshots：

- [ ] Terminal Execution Policy 設定畫面 / Terminal policy config screen
- [ ] Review Policy 觸發條件清單 / Review trigger list
- [ ] JavaScript Execution Policy 設定 / JS policy config
- [ ] Safe Mode 開關狀態 / Safe Mode toggle state
- [ ] Audit Log 範例（任 1 個 Agent 1 天的 log）/ Audit log sample (any 1 Agent for 1 day)
- [ ] 1 個 Review 通過 + 1 個 Review 拒絕的範例 / 1 approved + 1 rejected review example

---

## 4. 簽署 / Sign-off

| 角色 / Role | 簽名 / Signature | 日期 / Date |
|---|---|---|
| IT 主管 / IT Lead | __________ | __________ |
| Security Owner | __________ | __________ |
| Tech Lead | __________ | __________ |

下次 review / Next review: `[填入 / fill in，建議季度 / suggest quarterly]`
