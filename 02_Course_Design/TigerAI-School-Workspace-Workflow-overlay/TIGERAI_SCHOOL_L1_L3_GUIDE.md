# Tiger AI 校園 L1-L3 實作指南 / Tiger AI School L1-L3 Implementation Guide

> 🌐 中英雙語 / Bilingual inline
> 對位 / Maps to: [TIGERAI_METHODOLOGY_LAYER.md](TIGERAI_METHODOLOGY_LAYER.md) + 原 repo `basic-lesson/` + `advanced-lesson/` + `src/Code.gs`

## 1. 三層導入路徑 / Three-Tier Adoption Path

```text
L1（全員）                L2（種子科 / 部門）           L3（行政組）
教師個人使用 AI           各科教師整理 Skill 庫         行政流程自動化
                                                       (本 repo 核心)
    ↓ 2-4 週                    ↓ 6-8 週                 ↓ 8-12 週
全校 100% 教師有 AI 帳號     每科 ≥ 1 種子教師          公文 / 活動 /
+ Prompt Library v1          + NotebookLM 教材庫         請購 / 家長
                                                          通知自動化
```

```text
L1 (All teachers)        L2 (Seed subject / dept)     L3 (Admin staff)
Personal AI use          Per-subject Skill library    Workflow automation
                                                       (this repo's core)
    ↓ 2-4 weeks                ↓ 6-8 weeks              ↓ 8-12 weeks
100% teachers AI-enabled   ≥ 1 seed teacher per      Doc routing / events /
+ Prompt Library v1        subject + NotebookLM KB   procurement / parent
                                                       notifications auto
```

---

## 2. L1：教師個人使用 AI / L1: Personal AI Use by Teachers

### 2.1 對象 / Audience

全校 100% 教師（含校長、教務主任、各科教師、行政教師）。
All 100% of teaching staff (incl. principal, dept heads, subject teachers, admin teachers).

### 2.2 學什麼 / What to learn

| 能力 / Skill | 範例 / Example |
|---|---|
| 寫教案草稿 / Draft lesson plan | 用 1 句話描述教學目標 → AI 出 45 分鐘教案 |
| 翻譯與摘要 / Translate & summarize | 把英文期刊 paper 翻成 5 點重點給教師參考 |
| Email 家長 / Email parents | 從 1 句話事件 → 出完整委婉 + 同理表達 email |
| 學生作業評語 / Student assignment comments | 給作業內容 + 評分 rubric → AI 出個別化評語草稿 |
| 行政公文起草 / Admin doc draft | 給目的 → AI 出符合公文格式的草稿 |

### 2.3 工具棧 / Tool stack

| 學校類型 / School type | 推薦工具 / Recommended |
|---|---|
| **小型補習班 / cram school** | 個人 Gemini / ChatGPT 帳號 + 培訓 |
| **公立 K-12** | Workspace for Education + Gemini for Workspace（學校付月費） |
| **私立 K-12** | OpenWebUI 自架 + 雲端 API（成本可控） + Gemini |
| **完全中學 / 大型私校** | OpenWebUI 自架 + 多 LLM provider + 地端 Ollama 處理機敏 |

### 2.4 對應原 repo / Maps to original repo

- **`basic-lesson/`** —— 入門教材，全員上課用
- **`gemini_notebooklm_workspace_teacher_workflow_handout_Advanced.html`** —— 進階教師參考

### 2.5 完成標準 / Completion Criteria

- [ ] 全校 100% 教師有自己 AI 帳號（不共用）
- [ ] 每位教師有個人 Prompt Library ≥ 5 個
- [ ] 教師資料邊界判斷 10 案例 quiz ≥ 90% 正確
- [ ] AI 使用規範已公告並簽署

對應主 toolkit deliverable：[`L1_USER_OPERATION_MANUAL.md`](../_deliverables/L1_USER_OPERATION_MANUAL.md) + [`L1_AI_USAGE_POLICY_TEMPLATE.md`](../_deliverables/L1_AI_USAGE_POLICY_TEMPLATE.md)

---

## 3. L2：種子科 Skill 庫 + NotebookLM / L2: Seed Subject Skill Library + NotebookLM

### 3.1 對象 / Audience

每科至少 1 位種子教師（國文 / 英文 / 數學 / 自然 / 社會 / 藝能 / 健體）。
At least 1 seed teacher per subject.

### 3.2 學什麼 / What to learn

| 能力 / Skill | 範例 / Example |
|---|---|
| 建立科目 NotebookLM | 把該科 1 學年的教材、補充資料、學生常見問題上傳成 1 個 notebook |
| 設計學科 Prompt Pack | 國文：詩文翻譯 / 修辭辨識 / 作文評語；數學：題目改編 / 解題步驟生成 |
| 教學設計助理 | 給 1 個單元 → AI 出教學流程 + 學習單 + 課後評量 |
| 教材自動產生 | NotebookLM 跨 5 本參考書 → 自動產出該主題的綜合教材 |

### 3.3 對應原 repo / Maps to original repo

- **`advanced-lesson/`** —— 進階教材，種子教師深耕用
- **`notebooklm_gemini_admin_workflow_agent_v3.html`** —— Agent 互動範例（可改造為各科）

### 3.4 完成標準 / Completion Criteria

- [ ] 每科 ≥ 1 個 NotebookLM 已建好（≥ 10 份文件 input）
- [ ] 每科 ≥ 5 個學科專用 Prompt
- [ ] 種子教師願意每週分享 1 個成功案例給同科同事
- [ ] 至少 3 個學科有「跨班分享」紀錄

對應主 toolkit deliverable：[`L1_PROMPT_LIBRARY_STARTER.md`](../_deliverables/L1_PROMPT_LIBRARY_STARTER.md)（擴充版）

---

## 4. L3：行政流程自動化（本 repo 核心）/ L3: Admin Workflow Automation (this repo's core)

### 4.1 對象 / Audience

教務 / 學務 / 總務 / 輔導四處的行政組長 + 校長 / 教務主任。
Heads of academic affairs / student affairs / general affairs / counseling + principal / academic dean.

### 4.2 4 個主要 use case / 4 primary use cases

#### 4.2.1 公文簽核流程 / Document Routing

**痛點：** 紙本公文跑校長 → 教務主任 → 學年主任 → 任課教師，1 份花 2-3 天。
**Pain:** Paper-based routing principal → academic dean → grade head → teacher takes 2-3 days.

**Tiger AI L3 解法：** 用本 repo 的 Apps Script + Google Forms + Workspace 自動化簽核。觸發條件：上傳公文 → 路由至下個簽核者 + email 通知 → 全部簽完入庫 + 通知行政組長。

**Tiger AI L3 solution:** Use this repo's Apps Script + Forms + Workspace for auto-routing. Triggers: upload doc → route to next approver + email → all approved → archive + notify admin.

**HITL Gate：** 每一站簽核者必須人工點「同意 / 退回」，AI 不代簽。
**HITL Gate:** Every approver must manually click "approve / reject"; AI does not auto-approve.

**對應原 repo：** `admin-project-workflow.png` + `src/Code.gs` 的 form-submission handler。

#### 4.2.2 活動申請與核銷 / Event Application & Reimbursement

**痛點：** 活動申請表手寫 → 教務 → 學務 → 總務 → 會計，4-5 道流程，常有遺漏。
**Pain:** Event request form handwritten → 4-5 stops, prone to omission.

**Tiger AI L3 解法：** Google Form 收申請 → AI 檢查必填欄位 + 預算對照 → 自動路由 → 核銷階段 AI 對照發票 + 預算。

**HITL Gate：** 預算超過 5,000 元的活動，最後一站必須校長親簽。
**HITL Gate:** Events > NT$5,000 require principal's final approval.

#### 4.2.3 物資請購 / Procurement Request

**痛點：** 教師需要教學物資要走紙本流程，從填單到拿到貨平均 2-3 週。
**Pain:** Teacher procurement requests average 2-3 weeks from form to delivery.

**Tiger AI L3 解法：** Google Form 收請購 → AI 對照常用品庫存 + 預算 → 路由 → 通知採購人員 → 到貨通知教師。

**HITL Gate：** 採購人員必須在 PO 前最後確認金額與廠商。
**HITL Gate:** Procurement officer must final-confirm amount and vendor before PO.

#### 4.2.4 家長通知 / Parent Notifications

**痛點：** 重大事件（如停課、緊急通知）通知家長要組長手寫 + 一個一個發 Line。
**Pain:** Major events (closures, emergencies) require manual writing + per-parent Line messaging.

**Tiger AI L3 解法：** 行政組長給 1 句話事件描述 → AI 出多語版本（中 / 英 / 越南 / 印尼）+ 條列重點 + 委婉表達 → 教師審查 → 一鍵送家長。

**HITL Gate：** 所有對家長對外輸出**必須**任 1 名教師審查並按「送出」。**任何家長通知不可由 AI 直接發送**。
**HITL Gate:** All outbound parent communications **must** be reviewed by ≥ 1 teacher; **no AI-auto-send to parents under any circumstance**.

### 4.3 對應原 repo / Maps to original repo

- **`src/Code.gs`** —— 完整 Apps Script 實作（form handler / routing / notification）
- **`admin_ai_workflow_detailed_implementation.html`** —— 詳細實作指南
- **`docs/install.md`、`workflow.md`、`form-fields.md`、`testing.md`** —— 部署文件
- **`docs/privacy.md`、`troubleshooting.md`** —— 治理與故障處理

### 4.4 完成標準 / Completion Criteria

- [ ] 至少 2 個 L3 use case 已上線（4 個建議全做完才算「L3 完整」）
- [ ] 每個 use case 有 HITL Gate 設計（見 [`TIGERAI_HITL_GATES_SCHOOL.md`](TIGERAI_HITL_GATES_SCHOOL.md)）
- [ ] 自動化前後的時間 / 錯誤率對比有量測（KPI）
- [ ] 行政組長能獨立維運（不需顧問常駐）

---

## 5. L1 → L2 → L3 升級條件 / Upgrade triggers

| 從 / From | 到 / To | 觸發條件 / Trigger |
|---|---|---|
| L1 | L2 | L1 全校 100% + Prompt Library ≥ 5 / 人 + 至少 3 個科目主動詢問「我想做學科版的 AI」 |
| L2 | L3 | L2 有 ≥ 5 個學科建好 NotebookLM + 行政組長被學科同事的成功案例「逼著」想做行政版 |
| L3 | L4 | （大型私校才考慮）行政組長覺得「每個處室都有 N 個小 PoC，需要一個 Agent 整合知識」 |

> 不可跳級。L1 沒做完直接做 L3 = 全員不會用 AI 但行政流程自動化 → **AI 變成黑盒子，沒人懂、出錯沒人解**。

> No level-skipping. Doing L3 without L1 → AI becomes a black box, nobody understands it, errors have no first responder.

---

## 6. 時程估算 / Timeline Estimate

| 學校規模 / Size | L1 | L2 | L3 | 總計 / Total |
|---|---|---|---|---|
| **補習班 / cram school** (< 20) | 2 週 | 4 週 | 4 週 | **10 週 / 2.5 月** |
| **小型私立 K-12** (50-100) | 4 週 | 6 週 | 8 週 | **18 週 / 4.5 月** |
| **公立 K-12** (100-300) | 6 週 | 8 週 | 12 週 | **26 週 / 6 月** |
| **大型完全中學** (500+) | 8 週 | 12 週 | 16 週 | **36 週 / 9 月** |

> 假設**有顧問帶 + 校內種子團隊 3-5 人配合**。完全 DIY 時程要再 ×1.5。

> Assumes **consultant-led + 3-5 internal seed team members**. Pure DIY add ×1.5.

---

## 7. 收費估算 / Pricing Estimate

對應主 toolkit 的 SME Lite Path：

| 學校規模 / Size | 路線 / Route | 顧問費 / Consulting fee |
|---|---|---|
| 補習班 < 20 | SOHO Path | 5-15 萬 / USD 1.5K-5K |
| 小型私立 50-100 | SME Lite Path | 30-60 萬 / USD 10K-20K |
| 公立 K-12 100-300 | SME Lite Path | 60-120 萬 / USD 20K-40K |
| 大型完全中學 500+ | Enterprise-lite | 120-300 萬 / USD 40K-100K |

工具授權成本另計（Workspace for Education / Gemini for Workspace / OpenWebUI hosting）。

Tool licensing costs separate (Workspace / Gemini / OpenWebUI hosting).

---

**Version:** v0.1.0 (2026-05-20)
**License:** Apache 2.0
