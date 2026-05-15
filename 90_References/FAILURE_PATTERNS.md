# 失敗模式與反例：什麼時候 Tiger AI 方法論不該用 / 會失敗

> 🌐 English version: [FAILURE_PATTERNS_EN.md](FAILURE_PATTERNS_EN.md)
>
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技

更新日期：2026-05-16

---

> **本文目的**：方法論若只談成功，就是銷售文件。學術 / 監管 / 嚴肅客戶會問：「**什麼時候會失敗？什麼條件不該用？跳級會出什麼事？**」本文公開記錄已知的失敗模式 (failure patterns) 與反案例 (counter-cases)，作為方法論可被批評、可被改進的硬證據。

---

## 1. 為什麼方法論必須公開失敗模式

| 對象 | 為什麼需要看到失敗 |
| --- | --- |
| **學術審稿** | 只有成功例 = selection bias → 不能發表 |
| **監管機構** | 風險評估必須含失敗模式 + 預警條件 → 否則拒絕通過 |
| **嚴肅客戶** | 「**告訴我什麼時候你會失敗**」是真正信任顧問的問題 |
| **顧問自己** | 失敗模式 = 機構記憶 = 避免重蹈覆轍 |

> 一份**只談成功的方法論**比一份**承認失敗的方法論**更不可信。

---

## 2. 跳級失敗（Skipping Levels Failure）

### 2.1 跳過 L1 → 直奔 L4 Agent

**症狀**：

- 公司沒做過 L1 全員 Chat AI 採用，老闆看了一個 Agent demo 就想做 L4 客服 Agent
- 工程師 3 人花 3 個月做了一個 Hermes-like Agent
- Agent 上線後：客服員工不敢用、品保不簽核、IT 不知道 audit log 怎麼接、法遵說「這風險誰擔」

**根因**：

- 員工沒有經過 L1 階段建立**對 AI 的個人信任**（自己試過才相信）
- 沒有 L2 Skill Library → Agent 沒「公司寫過的判斷邏輯」可以引用
- 沒有 L3 Workflow → Agent 沒有「跨系統的合法管道」執行任務
- 沒有 L1-L3 治理打底 → Agent 上線就是合規 black box

**典型結局**：6 個月後 Agent 停用、IT 副理被問責、AI 預算被砍。

**對標案例**：[`../04_Scenarios/SAMPLE_CLIENT_CASE_HOSPITAL.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_HOSPITAL.md) Key failures 第 1 條（早期忽略護理 frontline 抗拒，後補 L1 課）。

### 2.2 跳過 L2 → 直接做 L3 Workflow

**症狀**：

- IT 看了 n8n 教學 → 開始接 Gmail → CRM → Slack 一連串 workflow
- 跑一個月，員工說「workflow 產出的內容不對 / 不符公司語氣 / 沒有引用我們的 SOP」
- 工程師回去微調 Prompt，但**每個 Workflow 有 10 個 Prompt 散在 n8n node 裡，無 Owner、無版本、無文件**

**根因**：沒有 L2 Skill Library 作為「公司寫過的 prompt + 判斷邏輯 + 數據」，L3 Workflow 變成「IT 工程師個人 prompt 練習場」。

**典型結局**：Workflow 越跑品質越漂移；3 個月後業務部門要求 IT 改回手動；IT 失去信任。

### 2.3 沒有 HITL 設計就上 L3 / L4

**症狀**：

- Workflow 自動寄客戶 email、自動產發票、自動下訂單
- 第一個月很順、效率提升 70%
- 第二個月 LLM 幻覺：發了一封價格錯誤的 quote 給 A 級客戶；損失合約 NT$ 300 萬

**根因**：所有 AI 系統都會有 ~0.5-3% 幻覺率。**沒有 HITL = 早晚會擊中 0% 容錯的場景**。

**典型結局**：高層全面禁用 AI、AI Champion 被處分、整套方法論被貼上「不可靠」標籤。

### 2.4 急著做 L5 ClawTeam 但 L4 還沒穩

**症狀**：

- 老闆看到 multi-agent demo，要求做「業務 + 客服 + 品保跨部門 Agent Team」
- 一個 Agent 都還沒通過 Stage Gate 4A-4E 驗收，就把 3 個 Agent 串起來
- 跨 Agent 任務的 evidence trail 中斷 → 沒人能追溯「為什麼決策是這樣」

**根因**：單 Agent 都沒治理好，多 Agent 必然失控（誰也說不清是哪個 Agent 的問題）。

**典型結局**：6 個月後解體，回到單 Agent 各自運作，但已浪費大半年。

---

## 3. 組織條件不適配的失敗模式

### 3.1 沒有 AI Champion（高管推手）

**前提**：每個 Phase 都需要至少一位「能跨部門協調、可決策、可向 Sponsor 回報」的 Champion。

**失敗症狀**：CEO 簽了 Phase A 但沒指派 Champion → 訪談時部門長互相推託 → As-Is 拼湊不完整 → Phase A 報告 quality 差 → 客戶不簽 Phase B。

**Tiger AI 拒絕條件**：若 Phase B 啟動前無 Champion 確定就位，**顧問應拒絕簽約**或要求先補 Champion。

### 3.2 IT 能力不足無法支撐 L3+

**前提**：L3 Workflow + L4 Agent 需要 IT 0.5-2 FTE 持續維護。

**失敗症狀**：

- 公司 IT 1 人，已被 ERP / 網路 / Helpdesk 操滿
- 上線 5 個 Workflow 後，沒人維護 / 沒人修 / 沒人更新
- 6 個月後 50% Workflow 失效，員工回到手動

**Tiger AI 拒絕條件**：若 Tool 6.3 組織吸收力評估中「IT FTE」維度 < Phase 2 最低需求（0.5 FTE 專責），**應強烈建議客戶先補 IT 才啟動**，不要硬簽。

### 3.3 法遵 / 合規嚴重不足（敏感行業）

**前提**：金融、醫療、政府、法律業有強合規要求。

**失敗症狀**：

- 醫院做客服 AI 沒先過 HIPAA / 個資法 / 病人權益審查
- 上線 3 個月被衛福部稽核 → 撤下 AI、罰款、新聞登版
- 不只 AI 計畫失敗，整體 IT 治理被質疑

**Tiger AI 拒絕條件**：高合規行業若無法遵專員 / 律師審查，**Phase A 結尾報告必須明確標示「合規未過 → 暫停 Phase B」**。

### 3.4 高層更迭打斷 24 個月 Roadmap

**前提**：Phase C 24 個月需要 Sponsor 長期穩定支持。

**失敗症狀**：

- Phase A 由 CEO 簽，但 CEO 在 Phase C Month 9 離職
- 新 CEO 不認同前任的 AI 方向 → Phase C 凍結
- 已投資 NT$ 980 萬 → 部分產出（L1-L3）保留，但 L4-L5 整個放棄

**Tiger AI 緩解設計**：Phase C 季度 Gate C 退場機制 = 即使 Sponsor 換人，每季都可重新評估，不會 sunk cost 全失。

---

## 4. 方法論本身的已知限制

### 4.1 評分模型未經心理計量驗證

**現況**：6 構面 × 0-4 量尺、L1-L5 區段門檻**由專家共識訂定**，**尚未做 Cronbach's α / EFA / CFA / inter-rater reliability**。

**潛在問題**：

- 兩位顧問評同一公司可能得出 L2 vs L3 不同結論
- 50-60 分 = L2 邊界 vs 41-60 = L2 的劃分缺實證
- 構面間可能有共線性（高相關），實際因子數可能 < 6

**Tiger AI 應對**：

- 報告中明確標示「expert-consensus version, pending psychometric validation」
- 已寫 `PILOT_STUDY_PROTOCOL.md` 規劃實證研究
- 在學術投稿時應降低 claim 強度為「a proposed framework」而非「validated instrument」

### 4.2 案例庫的證據等級

**現況**：7 個案例為**匿名合成案例 (Anonymized Composite)**，Evidence Level 為 L2（依據 Tool 8.9）。

**潛在問題**：

- 客戶可能質疑：「這數字是真的嗎？還是你拼湊的？」
- ROI ~358%、不良率 3.2 → 2.0% 等具體數字**不能作為任何單一客戶的合約承諾**

**Tiger AI 應對**：

- 每案例頂部明確標示 Evidence Level 與 Anonymized Composite 屬性
- 簽 SOW 時客戶自己的 baseline 為準，不引用案例數字
- 累積 L3-L5 證據後逐步替換為真實 longitudinal cases

### 4.3 GenAI 採用 Reference Model 認可度尚新

**現況**：Tiger AI L1-L5 在 Tool 2.5 自評 9/10，**條件 6（廣泛產業認可度）為 △ 部分**。

**潛在問題**：

- 業界初期接觸者會問：「APQC、SCOR 是國際公認，Tiger AI L1-L5 憑什麼？」
- 學術引用尚未累積到 critical mass

**Tiger AI 應對**：

- 開源（Apache 2.0 + GitHub）
- 主動申請 ISO/IEC 工作組 / IEEE AI Maturity 標準討論
- 跟 QUT、NTUST 等學校建立 joint research

---

## 5. 顧問執行層面的反模式（顧問自身的失敗）

### 5.1 跳過 Phase A 直接簽 Phase B-C

**症狀**：銷售壓力大，跳過 Phase A 診斷 → 直接簽 6 個月顧問案

**結果**：沒有客戶簽過的 As-Is / Reference Model / Ideal Practice → Stage 4 之後客戶可隨時否認「這不是我要的」→ 顧問被動。

**紀律**：**絕對不能跳過 Phase A**。Phase A 是後續一切的 anchor。

### 5.2 自己訂客戶的 Ideal Practice

**症狀**：顧問為了「快」，自己擬一份 Ideal Practice 草稿給客戶簽

**結果**：客戶覺得不是自己想的 → 後續逐項挑戰 → 整套推理鏈崩塌。

**紀律**：**必須跑 Tool 3.6 共創 Workshop 6 步驟**。獨立投票、集體共識、Reality check、寫定義表、三方簽名 —— 一步都不能省。

### 5.3 報告全靠 L1 自評，沒有 L3+ 證據

**症狀**：寫報告趕時間，所有結論都來自客戶問卷自評

**結果**：客戶內稽 / 母公司審計時被質疑「依據不足」→ 全案被退回。

**紀律**：依 Tool 8.9 Evidence Hierarchy，**任何重要結論必須有 L3+（系統 log）支撐**。報告每段明示 `[E:L#]`。

### 5.4 把 Stage 4 風險寫進 Gap Analysis

**症狀**：Gap Analysis 章節摻雜「這個風險高、不建議做」的主觀判斷

**結果**：Stage 4 變成 subjective → 客戶可挑「為什麼你認為這風險高」→ 整章被改。

**紀律**：**Stage 4 = 客觀差距盤點，不是風險評估**。風險屬於 Stage 8 Risk Register。

### 5.5 每季 Gate C 沒回頭看 Stage 2 雷達

**症狀**：執行階段忙於 PoC，每季只交進度，沒回頭核對 Stage 2 Reference Model 雷達

**結果**：做了一堆 PoC 但結構完整度沒改善 → 24 個月後客戶問「我們真的進步了嗎」無法回答。

**紀律**：**季度 Gate C 必做雷達回頭比對**。沒做 = 顧問失職。

---

## 6. 拒絕簽約的硬條件清單

Tiger AI **應該拒絕**簽 Phase C（落地）的條件（即使客戶想簽）：

- [ ] **未通過 Phase A + B** → 沒有客戶簽署的 Ideal Practice → 拒絕簽 Phase C
- [ ] **無 AI Champion 確定就位** → 拒絕簽 Phase C
- [ ] **IT FTE 不足以支撐目標 Phase** → 強烈建議延後 + 補 IT 才簽
- [ ] **高合規行業無法遵專員 / 律師 review** → 拒絕簽 Phase C
- [ ] **Sponsor 不到位（CEO 沒明確支持）** → 拒絕簽 Phase C
- [ ] **客戶想跳級（如：跳過 L1-L3 直接做 L4-L5）** → 拒絕，至少要求補 Phase 1 基礎
- [ ] **預算不足以撐完當階段** → 拒絕，建議客戶縮小範圍

---

## 7. 失敗時的退場機制（Customer Exit Protocol）

若 Phase A / B / C 任一階段失敗，Tiger AI 承諾：

1. **Phase A 失敗**：客戶仍保留中期評估報告（10-15 頁）+ 訪談摘要 + 雷達圖 → **可自行接手或找下一家顧問**
2. **Phase B 失敗**：完整顧問報告 + Ideal Practice 定義表（簽署版）保留 → **可帶到其他顧問繼續**
3. **Phase C 中途失敗（每季 Gate C 評估後客戶決定停）**：已完成的 Phase（含 Stage Gate 驗收）保留 + 治理文件保留 + 程式碼 / Skill / Workflow 全部移交客戶（顧問**不持有任何客戶資產**）
4. **顧問不質押客戶資產**：對應 [`../06_Delivery/ENGAGEMENT_LIFECYCLE.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE.md) 7 Pillars 第 1 條「客戶自持」

---

## 8. 如何使用本文件

| 角色 | 怎麼用 |
| --- | --- |
| **顧問內部訓練** | onboarding 必讀；每季團隊 review 一次「我們上一季踩到哪些失敗模式」 |
| **客戶簽約前** | 顧問主動讓客戶看本文 → 客戶會更信任「這顧問不只賣成功，也誠實談失敗」 |
| **學術審稿** | 引用本文作為「方法論的可批評性 / falsifiability」證據 |
| **監管 / 投標文件** | 附本文作為風險評估與緩解策略 |

> **誠實談失敗 = 最高層級的銷售技巧**。客戶買的不是「保證成功」，而是「失敗時我們知道怎麼辦」。

---

授權與引用 / License & Citation

本文為 Apache License 2.0；可使用、修改、商業利用，唯需保留 [`../NOTICE`](../NOTICE) 檔之署名。
