# 八階段顧問診斷工具表 / Eight-Stage Consulting Toolkit Templates

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

本檔提供八階段顧問方法論的 **可直接使用工具表**：訪談題庫、盤點表、矩陣、worksheet、checklist。每個 Stage 對應 1-4 個工具。顧問可直接複製到 Notion / Google Docs / Word 開始用。

This document provides ready-to-use **toolkit templates** for the eight-stage consulting methodology: interview question banks, inventories, matrices, worksheets, and checklists. Each stage maps to 1-4 tools. Consultants can copy directly into Notion / Google Docs / Word.

---

## Stage 1：現況掌握 / Current-State Discovery

### Tool 1.1 訪談問題庫 / Interview Question Bank (40 問)

#### A. 主管層 (CEO / COO / CIO) — 12 問

1. 您對 AI 在公司的「最理想未來樣貌」是什麼？/ What is your ideal future state of AI in the company?
2. 您過去 12 個月看到哪些 AI 成功與失敗案例？
3. 公司目前最大的營運痛點是什麼？AI 能不能幫上？
4. 您最擔心 AI 帶來什麼風險？(資安、合規、員工抗拒、ROI 不明)
5. 您願意每年投入多少預算在 AI 轉型？
6. 公司有 AI 推動的負責人嗎？(若無，誰可以承擔？)
7. 您覺得我們已經是 L1-L5 的哪一級？為什麼？
8. 您希望 12 個月後達到哪一級？
9. 哪個部門最先導入 AI 對公司影響最大？
10. 您有打算自建 AI 團隊還是依賴外部顧問？
11. 公司董事會 / 母公司對 AI 投資態度？
12. 您最想從這次顧問專案得到什麼具體成果？

#### B. 部門主管層 — 14 問

13. 部門目前的關鍵 KPI 與痛點？
14. 員工每天有多少時間花在重複性工作？
15. 哪些工作是「換誰來做都一樣」可以 AI 化？
16. 哪些工作極度仰賴特定資深員工？
17. 部門目前用了哪些 SaaS 工具？整合狀況？
18. 員工是否私下使用 ChatGPT / Claude？頻率？資料邊界？
19. 您部門的「黃金 SOP」有哪些？是否已書面化？
20. 跨部門協作最大障礙是什麼？
21. 您希望 AI 解放您的哪一段時間？
22. 您部門員工對 AI 的態度？(熱衷 / 中性 / 抗拒)
23. 部門新人 onboarding 多久？AI 能加速嗎？
24. 部門決策慢在哪？資料找不到還是溝通慢？
25. 過去 90 天有哪些值得記錄的 AI 嘗試？
26. 您部門有沒有「我希望可以自動化但一直沒空做」的願望清單？

#### C. 操作員 / 一線員工 — 14 問

27. 您每天最重複的 5 件工作是什麼？
28. 您每天會打開哪幾個系統 / 工具？
29. 哪些資料您找了很久都找不到？
30. 您會私下用 AI 工具嗎？用哪一個？做什麼？
31. 您覺得 AI 哪些地方幫上忙、哪些幫不上？
32. 寫報告 / email / 提案時 AI 能加速多少？
33. 您怕 AI 取代您的工作嗎？(若怕，怕哪部分)
34. 您希望主管別再叫您做哪些事？
35. 上次出錯的原因？AI 能避免嗎？
36. 您覺得自己的「核心專業」AI 應該不能取代的是？
37. 同事用 AI 哪些地方做得比您好？
38. 您願意花多少時間學 AI？
39. 哪些事情您「人工做反而比 AI 做更快」？
40. 給 AI 一個願望，您希望它幫您解決什麼？

> **使用方式**：訪談每場 60-90 分鐘；主管 12 題、部門 14 題、操作員 6-8 題（精選）。錄音 + 摘要 + 編碼。

---

### Tool 1.2 AI Usage Inventory / AI 使用盤點表

| # | 部門 / Dept | 目前 AI 工具 | 頻率 | 使用人數 | 是否經許可 | 機敏資料風險 | 月支出 | 備註 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Marketing | ChatGPT Plus (個人帳號) | Daily | 8 | ❌ | High (品牌資料) | NT$24,000 | 私人信用卡 |
| 2 | Sales | Copilot for Office | Weekly | 15 | ✓ | Medium | NT$45,000 | 公司採購 |
| 3 | IT | Claude.ai (自己用) | Daily | 3 | ❌ | Medium (程式碼) | NT$9,000 | 私人帳號 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

> **產出**：影子 IT 風險地圖 + 採購整合機會。

---

### Tool 1.3 Systems Inventory / 系統盤點表

| 系統名稱 | 廠商 / 版本 | 部門擁有者 | 使用人數 | 整合點 (in/out) | 資料敏感度 | API 可用？ | 雲/地端 | 備註 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gmail Workspace | Google | IT | 全公司 250 | OAuth API | Medium | ✓ | 雲 | 已啟 SSO |
| Salesforce | SF Sales Cloud Pro | Sales | 35 | REST + Webhook | High (PII) | ✓ | 雲 | 12 月到期 |
| SAP B1 | 9.3 | Finance | 18 | DI API + ODBC | High | ✓ | 地端 | 老舊客製多 |
| Notion | Plus | All | 80 | API + Webhook | Medium | ✓ | 雲 | 部門自管 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

> **產出**：系統地圖 + L3 Workflow PoC 候選清單。

---

### Tool 1.4 As-Is Process Map (Swimlane Template)

```
Process: 客戶詢價到出貨 / Quote-to-Ship
========================================
Actor / 角色   | Step / 步驟         | System / 系統 | Input         | Output        | Pain
---------------|--------------------|---------------|---------------|---------------|-------
客戶 Customer  | 寄詢價信           | Email         | 需求描述       | 詢價郵件       | -
業務 Sales     | 收信判斷           | Gmail         | 詢價郵件       | 內部分派       | 漏接 30%
業務 Sales     | 查 ERP 庫存價格    | SAP B1        | 料號           | 庫存價格表     | 慢 + 出錯
業務 Sales     | 寫報價單           | Word + Sheet  | 庫存價格       | 報價單草稿     | 重複
業務主管 Lead  | 審核報價           | Email         | 報價單         | 簽核 / 退回    | 等
業務 Sales     | 寄報價             | Gmail + PDF   | 簽核版         | 報價郵件       | -
客戶 Customer  | 確認下單           | Email         | 報價           | PO            | -
業務 Sales     | 開單 (SO)          | SAP B1        | PO             | SO 編號        | 重 key
倉儲 WMS Op    | 出貨備貨           | WMS           | SO             | 揀貨單         | 對單錯
出貨 Shipping  | 列印貨運單         | 物流系統        | 揀貨單         | 託運單         | -
========================================
總時間 / Total: 平均 4-7 個工作天
痛點 / Pain summary: 漏接、重 key、找價格慢、簽核等
AI 化建議 / AI candidates: L3 Gmail 分類、L3 SAP 報價自動草稿、L4 Agent 簽核摘要
```

> **產出**：每個 process 一張 swimlane；標註痛點密度（每 step 0-3 點）；交給 Stage 4 做 Impact × Effort。

---

## Stage 2：願景對齊 / Vision Alignment

### Tool 2.1 L1-L5 能力說明手冊 (handout for clients)

| Level | 在實務中看起來像 | 客戶常說的話 | 常見誤解需澄清 |
| --- | --- | --- | --- |
| L1 Chat AI | 全員有公司帳號、會用、有規範 | 「我們有買 ChatGPT」 | 買 ChatGPT ≠ 全員會用、≠ 有治理 |
| L2 Skill AI | Skill Library + 版本控制 | 「我有寫 Prompt 庫」 | Prompt 庫 ≠ 可被別人重用 |
| L3 Workflow AI | n8n PoC 在跑 + 串到系統 | 「我們有自動化」 | RPA / Zapier ≠ AI Workflow |
| L4 Auto Agentic AI | Agent 通過 Gate + 有 Wiki | 「我們在用 Agent」 | Demo Agent ≠ 受控 Agent |
| L5 Agentic Team AI | 多 Agent 完成跨部門任務 | 「我們在做 AI 團隊」 | Chatbot 群 ≠ Agent Team |

### Tool 2.2 Vision Worksheet (5 prompts)

1. 三年後您希望客戶用一句話形容貴公司的 AI 應用：______
2. 三年後 AI 為您節省 / 創造的具體 NT$ 金額：______
3. 三年後您希望哪個部門最 AI 化？哪個保留人工？______
4. 三年後您希望 AI 治理「至少」做到哪三件事？______
5. 三年後若失敗，您最不希望看到什麼局面？______

### Tool 2.3 Stakeholder Alignment Matrix (RACI)

| 議題 / Topic | 高層 Sponsor | AI Champion | IT | 一線使用者 | 資料 Owner |
| --- | --- | --- | --- | --- | --- |
| 願景設定 | A | R | C | I | I |
| 工具選型 | A | C | R | C | C |
| 帳號 / 權限 | I | C | R | I | A |
| Skill / Workflow 建置 | I | A | R | R | C |
| Audit / 治理 | A | C | R | I | R |
| ROI 衡量 | A | R | C | I | I |

(R=Responsible, A=Accountable, C=Consulted, I=Informed)

---

## Stage 3：產業標竿 / Industry Benchmark

### Tool 3.1 Benchmark Case Summary Template

| 欄位 | 說明 |
| --- | --- |
| Industry | 產業 |
| Company size | 員工數 / 營收 |
| Their L-level start | 開始時 L 級 |
| Their L-level today | 目前 L 級 |
| Time taken | 月數 |
| Key wins | 三個關鍵成果 |
| Key failures | 兩個失敗教訓 |
| Sources | 公開新聞 / 訪談 / 案例 |

### Tool 3.2 五個現成 Benchmark Stub

#### Manufacturing — 半導體封測 700 人
- L1 → L3 in 9 months
- Wins: 製程異常摘要 Agent、SPC 自動分析、客訴根因 Agent Team
- Failures: 早期跳過 L1 全員，靠 IT 一人撐；資料權限沒打底

#### Hospital — 醫學中心 1,200 人
- L1 → L4 in 12 months
- Wins: 病患 onboarding RAG、HIS / EMR 整合 Agent、行政摘要
- Failures: 第一階段忽略護理 frontline 抗拒；後補了 L1 課

#### Retail — 連鎖品牌 800 人
- L1 → L4 in 14 months
- Wins: 商品文案 Skill Library、社群輿情 Workflow、新品上市 Agent Team
- Failures: 早期沒設計 Reviewer，AI 文案誤用品牌字眼

#### Financial Services — 區域銀行 2,500 人
- L1 → L3 in 18 months
- Wins: KYC 文件摘要 Workflow、客服分流 Agent
- Failures: 法遵審核耗時；地端 LLM 效能不足

#### Government — 都市政府 5,000 人
- L1 → L2 in 24 months
- Wins: 公文摘要、市民服務 FAQ
- Failures: 採購程序拖；缺 AI Champion

---

## Stage 4：差距分析 / Gap Analysis

### Tool 4.1 Missing / Broken / Redundant 表

| 領域 / Area | 類型 (M/B/R) | 描述 / Description | 根因 / Root Cause | 嚴重 1-5 | 擁有者 / Owner |
| --- | --- | --- | --- | --- | --- |
| 客服信件分類 | Missing | 完全沒有 AI 分類 | 沒人想到 | 4 | 客服長 |
| 報價系統 | Broken | 業務手動 copy-paste | 系統老舊、無 API | 5 | IT 副理 |
| 工單系統 | Redundant | Notion + Trello + Email 三套 | 各部門自選 | 3 | COO |
| ... | ... | ... | ... | ... | ... |

### Tool 4.2 Impact × Effort 矩陣

```
            Low Effort                   High Effort
           ┌──────────────────────┬──────────────────────┐
High       │  ★ Quick Wins        │  Big Bets            │
Impact     │  - Gmail 分類          │  - ERP Agent          │
           │  - Sheet 自動計分      │  - 跨部門 Team         │
           ├──────────────────────┼──────────────────────┤
Low        │  Fill-ins            │  ✗ Avoid              │
Impact     │  - 內部 FAQ          │  - 大客製 chatbot      │
           │  - 簡報模板           │                       │
           └──────────────────────┴──────────────────────┘
```

**置入規則**：
- Impact 計分：直接 NT$ 影響 × 受益人數 × 戰略重要度，得 1-5
- Effort 計分：人天 × 風險 × 系統整合難度，得 1-5
- ≥3 為 High

### Tool 4.3 Prioritization Worksheet

| 候選案 | Impact (1-5) | Effort (1-5) | Strategic Fit (1-5) | Score = (I × SF) / E | 排名 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 客服信件分類 PoC | 4 | 1 | 5 | 20 | 1 |
| 業務提案 Skill | 4 | 2 | 4 | 8 | 4 |
| ERP Agent | 5 | 5 | 5 | 5 | 5 |
| Sheet 自動計分 | 3 | 1 | 3 | 9 | 3 |
| 跨部門 Team | 5 | 4 | 5 | 6.25 | (Big bet 入後段) |

---

## Stage 5：高階問題定義 / Executive Problem Statement

### Tool 5.1 Problem Statement Worksheet (5 sections)

```
1. CONTEXT / 情境
   過去 12 個月發生了什麼讓 AI 變成優先議題？

2. TENSION / 張力
   目前的「現實」與「期望」差距是什麼？具體量化。

3. COST OF INACTION / 不行動的代價
   不做 AI 12 個月後會發生什麼？金額？

4. DESIRED FUTURE / 期望未來
   12 個月後成功長什麼樣？三個可量化指標。

5. CONSTRAINTS / 限制條件
   預算？人力？合規？時程？哪些選項已被排除？
```

### Tool 5.2 Common Pitfalls Checklist (10 anti-patterns)

- [ ] 把 AI 寫成科技議題（應寫成業務議題）
- [ ] 沒有量化「不行動的代價」
- [ ] 把「導 AI」當目標（應該是業務 KPI）
- [ ] 把所有部門都列為高優先（無聚焦）
- [ ] 只談機會、避談風險
- [ ] 用「資安」當擋箭牌阻止任何嘗試
- [ ] 把治理寫成 IT 議題（應全公司議題）
- [ ] 期望時程過短 / 過長
- [ ] 沒有 sponsor / 沒有 champion
- [ ] 沒有失敗退場機制

### Tool 5.3 Sample 完整問題定義（製造業）

```
CONTEXT:
過去 12 個月，三家直接競爭對手導入 AI 質檢與客訴 Agent，公司客戶開始質疑為何
我們交期慢、客訴回應慢。客戶 A 季度訂單下降 18%。

TENSION:
公司目前不良率 3.2%（業界領先 1.8%），客訴平均回應 5 天（業界 2 天），
業務提案產出 4 天（業界 1.5 天）。

COST OF INACTION:
若 12 個月內無顯著改善，預計流失客戶 A、B、C，年營收影響約 NT$ 1.8 億。
另招募 8 位品保與業務的招募成本約 NT$ 1,200 萬。

DESIRED FUTURE:
12 個月後：不良率降至 2.0%、客訴回應 ≤ 1 天、業務提案產出 ≤ 1 天。
建立 1 個製程改善 Agent Team 與 1 個業務 Skill Library。

CONSTRAINTS:
- 預算上限 NT$ 800 萬 (含教育訓練 + 平台 + 顧問)
- 製程資料須地端處理（不能上雲）
- IT 人力 2 FTE 不可再增
- 12 月母公司審計，第一個 Quick Win 須在 6 個月內展現
```

---

## Stage 6：路徑圖與 Stage Gate / Roadmap & Stage-Gate Design

### Tool 6.1 30/60/90 Roadmap Template

| Quarter | Theme | Deliverables | Owner | Stage Gate Criteria | KPI |
| --- | --- | --- | --- | --- | --- |
| 30 days | 診斷 + L1 啟動 | 全員 OpenWebUI 上線、AI 規範、Prompt Library | IT + AI Champion | Gate 1 | 80% 員工每週使用 |
| 60 days | L2 + L3 PoC | 5 個 Skill、3 個 n8n Workflow PoC | AI Champion + 部門 | Gate 2 + 3 | Skill Library 上 ≥3、Workflow uptime 95% |
| 90 days | L4 Pilot | 1 個 Hermes Agent (e.g., 客服 / 業務) | AI Champion + IT | Gate 4 | Agent 完成 5 個任務、Reviewer 通過 |
| 6 months | L4 Scale | 3 個 Agent、跨部門整合 | 部門 Lead | Gate 4 ext. | 每月節省工時 ≥ 200 hr |
| 9-12 months | L5 Pilot | 1 個 ClawTeam (跨部門任務) | Sponsor + AI Champion | Gate 5 | Team 完成 ≥ 1 跨部門任務 |

### Tool 6.2 Stage Gate Acceptance Checklist (Gates 1-5)

#### Gate 1 (L1 完成)
- [ ] OpenWebUI 全員帳號開設完成
- [ ] AI 使用規範文件簽署率 > 90%
- [ ] Prompt Library 收集 ≥ 30 條
- [ ] Admin Panel 權限矩陣設定完成
- [ ] L2 候選 Skill 名單 ≥ 5

#### Gate 2 (L2 完成)
- [ ] Skill Library 上架 ≥ 3 個 Skill
- [ ] 每個 Skill 有 Owner、版本、IPOE 文件
- [ ] Antigravity / Claude Code artifacts 提交
- [ ] Workflow Blueprint 至少 3 個
- [ ] L3 候選 Workflow 名單

#### Gate 3 (L3 完成)
- [ ] n8n Workflow PoC ≥ 3 個上線
- [ ] Sub-workflow Library 結構完成
- [ ] Data Tables Schema 確定
- [ ] GitHub Backup SOP 執行
- [ ] L4 Workflow Contract 與 Hermes 對接規格

#### Gate 4 (L4 完成)
- [ ] Hermes Agent 通過 4A-4E 子 Gate
- [ ] Wiki ingest/query/update 都跑通
- [ ] briefing 模板與實際 brief 案例
- [ ] Evidence 追溯：input → process → output → log
- [ ] L5 Agent Team 候選任務名單

#### Gate 5 (L5 完成)
- [ ] ClawTeam Role Cards 完成
- [ ] Task allocation table 含依賴鏈
- [ ] 1 次跨部門 Agent Team 演練成功
- [ ] Reviewer + Human Gate 設計
- [ ] ROI tracking matrix 啟動

### Tool 6.3 Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner | Trigger |
| --- | --- | --- | --- | --- | --- |
| 員工抗拒 | High | High | L1 全員體驗 + 主管以身作則 | HR + Sponsor | adoption < 50% in 30d |
| 機敏外流 | Medium | Critical | redact policy + audit log + Hybrid 部署 | CIO | DLP alert |
| LLM 幻覺造成決策錯誤 | High | Medium | Reviewer / Human Gate + evidence | AI Champion | 任一決策被推翻 |
| 預算超支 | Medium | Medium | 月度 KPI / ROI 檢視 | CFO | 月支出 > 110% 預算 |
| ... | ... | ... | ... | ... | ... |

---

## Stage 7：解決方案架構 / Solution Architecture

### Tool 7.1 Skill Map Template

| Skill | Owner | Inputs | Outputs | Tools used | L-level | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 客戶提案草稿 | Sales Lead | 客戶資料 + 過往提案 | Word 提案 | Antigravity + Claude | L2 | Live |
| 客訴分類 | CS Lead | Gmail 信件 | 分類 + 優先級 | n8n + Claude | L3 | PoC |
| 月結異常摘要 | Finance | SAP 報表 | 異常表 + 行動 | n8n + GPT-4 | L3 | Build |
| ... | ... | ... | ... | ... | ... | ... |

### Tool 7.2 Workflow Map Template

| Workflow | Trigger | Steps (n8n) | Systems | Skills called | Output | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| 客服信分類 | Webhook (Gmail) | Webhook → Set → OpenAI Chat → Switch → Gmail Label | Gmail | "客訴分類" | 標籤 + 通知 | CS Lead |
| 客戶月度報告 | Schedule (1st of month) | Schedule → SAP API → Sheet → Claude → Email | SAP, Sheets, Gmail | "月結摘要" | PDF + Email | Finance |
| ... | ... | ... | ... | ... | ... | ... |

### Tool 7.3 Agent Map Template

| Agent | Role | Skills used | Workflows used | Wiki | Reviewer | Gate |
| --- | --- | --- | --- | --- | --- | --- |
| 客服 Triage Agent | 客訴分流與草稿 | 客訴分類, 草稿產生 | 客服信分類 | FAQ + 過往案例 | CS Manager | Gate 4 ✓ |
| 業務 Briefing Agent | 拜訪前 brief | 客戶研究, 商機摘要 | CRM 摘要 | 客戶 history | Sales Lead | Gate 4 ✓ |
| ... | ... | ... | ... | ... | ... | ... |

### Tool 7.4 Integration Architecture (3 variants)

#### Variant A: Cloud-first
```
[OpenWebUI Cloud] → [n8n Cloud] → [Hermes Cloud Agent] → [SaaS APIs]
                                       ↓
                                 [Notion / Sheets / Gmail]
LLM: OpenAI / Claude / Gemini API
適用：低敏感、快速 PoC、預算有限
```

#### Variant B: Hybrid
```
[OpenWebUI On-Prem] → [n8n Self-host] → [Hermes Local Agent]
                            ↓                  ↓
                      [SaaS APIs]      [本地 SQL / ERP]
LLM 路由：低敏感→雲、機敏→地端 Llama
適用：金融、醫療、製造機敏資料
```

#### Variant C: Full On-Prem
```
[OpenWebUI Local] → [n8n Local] → [Hermes Agent Local]
                       ↓                ↓
                 [Local APIs only]  [Local Llama 70B + Embedding]
無雲端 LLM 呼叫
適用：政府、國防、頂級金融
```

---

## Stage 8：治理與 ROI / Governance & ROI

### Tool 8.1 Permission / Governance Matrix

| Role | Resource | Read | Write | Approve | Audit |
| --- | --- | --- | --- | --- | --- |
| 全員 | OpenWebUI 個人區 | ✓ | ✓ | ✗ | self |
| 部門 Lead | 部門 Skill Library | ✓ | ✓ | ✓ | dept |
| AI Champion | 全公司 Workflow | ✓ | ✓ | ✓ (≤ Gate 3) | all |
| IT Admin | 全部 + 模型 + Audit Log | ✓ | ✓ | ✓ (Gate 4-5) | all |
| Sponsor / CIO | 全公司 read + Approve | ✓ | ✗ | ✓ (Gate 5) | all |
| 法遵 / 內稽 | Audit Log only | ✓ | ✗ | ✗ | all |

### Tool 8.2 ROI Tracking Matrix

| Initiative | Baseline | Target | Actual | Period | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 客服信分類 | 5 days resp | 1 day | 1.2 day | Month 3 | CS Lead | 🟡 95% |
| 業務提案 | 4 days | 1 day | 0.8 day | Month 4 | Sales Lead | 🟢 |
| 月結異常摘要 | 3 days | 0.5 day | 0.6 day | Month 5 | Finance | 🟢 |
| Hermes Agent 任務 | n/a | 50 / month | 38 | Month 6 | AI Champion | 🟡 |
| ClawTeam 跨部門 | n/a | 1 / quarter | 0 | Month 9 | Sponsor | 🔴 (delay) |

### Tool 8.3 Audit Log Requirements

| Event Type | Captured by | Retention | Reviewer |
| --- | --- | --- | --- |
| LLM call (prompt + response) | n8n / OpenWebUI | 90 days hot, 1 year cold | AI Champion |
| Permission change | OpenWebUI Admin | 3 years | IT Admin + 法遵 |
| Skill / Workflow deploy | GitHub | 永久 | AI Champion |
| Agent task start/end | Hermes log | 1 year | AI Champion |
| Reviewer 簽核 | 系統內 | 永久 | 法遵 |
| Gate 通過記錄 | 顧問 + 客戶 | 永久 | Sponsor + 顧問 |
| 機敏資料 redact 觸發 | DLP | 1 year | 資安 + 法遵 |

### Tool 8.4 AI Ethics & Data Policy Checklist (15 items)

- [ ] 員工 AI 使用規範已書面、已簽署
- [ ] 客戶資料 / PII 不外送 LLM (或經 redact)
- [ ] 模型供應商之資料保留政策已審
- [ ] Audit Log 涵蓋所有 LLM 呼叫
- [ ] 員工有權知道哪些工作被 AI 處理
- [ ] AI 決策有 Human Gate (重大事項)
- [ ] AI 產出內容明示「AI 產生」標記
- [ ] 智財權歸屬已釐清 (員工 / 公司 / AI 廠商)
- [ ] 偏見 / 歧視風險評估 (HR / 客戶決策場景)
- [ ] 兒少 / 醫療 / 法律 等高敏感場景另設規範
- [ ] LLM 幻覺處理 SOP (誰負責檢核)
- [ ] AI 系統 incident response 流程
- [ ] 第三方 AI 工具白名單 / 黑名單
- [ ] 員工教育每年至少 1 次
- [ ] 政府法規追蹤 (EU AI Act, 台灣 AI 基本法, 個資法) by 法遵

---

## Closing：如何使用本工具表 / How to Use This Toolkit

### 6 週標準顧問專案排程 / 6-Week Standard Engagement

| 週 | Stage | 主要工具 | 客戶角色 | 顧問交付 |
| --- | --- | --- | --- | --- |
| W1 | Stage 1 | 1.1 訪談 / 1.2 1.3 盤點 | 主管訪談、IT 提供盤點 | Discovery Report |
| W2 | Stage 1+2 | 1.4 As-Is Map / 2.1 2.2 2.3 | 部門 walkthrough | Vision Workshop Output |
| W3 | Stage 3+4 | 3.1 3.2 標竿 / 4.1 4.2 4.3 | 主管 review | Gap Analysis + Priority |
| W4 | Stage 5+6 | 5.1 5.2 5.3 / 6.1 6.2 6.3 | 主管 + AI Champion | Problem Statement + Roadmap |
| W5 | Stage 7 | 7.1-7.4 | AI Champion + IT | Solution Architecture |
| W6 | Stage 8 + 結案 | 8.1-8.4 | Sponsor + 法遵 | Final Report + Roadmap + Governance |

### 每週交付節奏

- 週一：上週工具 review + 本週 plan
- 週三：客戶訪談 / 工作坊
- 週五：交付草稿 + 客戶 review

### 顧問 onboarding (給新顧問)

1. 先讀 README + AI_TRANSFORMATION_STORY_AND_STRUCTURE
2. 跑過一遍本工具表所有 sample
3. shadow 1 場 Stage 1 訪談、1 場 Stage 5 工作坊
4. 自己跑 1 場 Stage 4 Impact × Effort
5. 通過 Tiger AI 內部 mock review

---

授權與引用 / License & Citation

本工具表為 Apache License 2.0；任何顧問、企業內部、衍生顧問方法論皆可使用、修改、商業利用，唯需保留 [`NOTICE`](../NOTICE) 檔之署名。
This toolkit is Apache License 2.0; consultants, in-house teams, and derivative methodologies may use, modify, and commercialize, provided the [`NOTICE`](../NOTICE) attribution is preserved.
