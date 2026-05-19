# Tiger AI 校園 Stage Gate 驗收設計 / Tiger AI School Stage Gate Acceptance Design

> 🌐 中英雙語 / Bilingual inline
> 對位 / Maps to: [TIGERAI_SCHOOL_L1_L3_GUIDE.md](TIGERAI_SCHOOL_L1_L3_GUIDE.md) 完成標準節

## 0. 為什麼需要 Stage Gate / Why Stage Gates

學校的 AI 導入失敗模式 90% 是「**做了沒人驗收 → 沒人為品質負責 → 用 1 個月後沒人用**」。Stage Gate 解決這個。
90% of school AI rollout failures stem from "deployed without acceptance → no quality owner → unused after 1 month." Stage Gates solve this.

每個 L 階段結束有 1 個 Stage Gate。**Gate 未通過不能進下一級。**
Each L level ends with a Stage Gate. **No level-skipping without passing the Gate.**

---

## 1. Gate 1 — L1 全員 AI 使用就緒 / Gate 1: L1 All-Hands AI Readiness

### 1.1 通過條件 / Pass criteria

| # | 條件 / Criterion | 證據 / Evidence |
|---|---|---|
| 1 | 全校 ≥ 95% 教師有自己 AI 帳號 | 帳號清單 + 部署截圖 |
| 2 | ≥ 90% 教師完成 L1 基本訓練 | 出席紀錄 + 完課證明 |
| 3 | 每位教師個人 Prompt Library ≥ 5 個 | 隨機抽 10 位教師查看 |
| 4 | 資料邊界判斷 10 案例 Quiz ≥ 90% 正確（教師平均）| Quiz 結果統計 |
| 5 | AI 使用規範已校務會議通過 + 全員簽署 | 校務會議紀錄 + 簽署表 |
| 6 | 至少 3 個科 / 處室回報「我們開始固定用 AI」 | 主任訪談紀錄 |

### 1.2 簽核者 / Sign-off

| 角色 / Role | 簽 / Sign |
|---|---|
| **校長 / Principal** | 最終核可 |
| **教務主任 / Academic Dean** | 教學面驗收 |
| **IT / 資訊組長** | 技術面驗收 |
| **AI Champion**（種子教師代表）| 使用面驗收 |

### 1.3 未過 Gate 1 的常見原因 / Common Gate 1 failures

| 症狀 / Symptom | 根因 / Root cause | 補強方向 / Fix |
|---|---|---|
| 教師反映「不知道怎麼用」 | L1 訓練只放投影片沒做 hands-on | 補半天 workshop |
| 教師抱怨「AI 講錯」 | 沒教資料邊界與幻覺判斷 | 補 1 場 1 小時的資料邊界訓練 |
| 帳號被共用 | IT 沒設定個人帳號 | 補 IT 帳號管理 SOP |
| 校長 / 主任不用 | Top-down 沒身先示範 | 校長 / 主任先補 3 對 1 個別指導 |

> **Gate 1 沒過不能進 L2。** 強推 L2 = 「給沒會走路的人鞋子」。
> **Without Gate 1, no L2.** Pushing L2 = "shoes for someone who can't walk."

---

## 2. Gate 2 — L2 種子科 Skill 庫就緒 / Gate 2: L2 Seed Subject Skills Ready

### 2.1 通過條件 / Pass criteria

| # | 條件 / Criterion | 證據 / Evidence |
|---|---|---|
| 1 | ≥ 5 個科 / 部門各有 1 個 NotebookLM | 各科 NotebookLM 連結清單 |
| 2 | 每個 NotebookLM 已上傳 ≥ 10 份教材 | NotebookLM 文件清單 |
| 3 | 每科 ≥ 5 個學科專用 Prompt 已上架到全校共用 Prompt Library | 共用 Prompt Library 清單 |
| 4 | 種子教師每週分享 1 個成功案例（連續 4 週）| 校內分享會紀錄 |
| 5 | 至少 3 個學科有跨班 / 跨年級分享紀錄 | 教學共備會議紀錄 |
| 6 | 教師整體 AI 使用率 ≥ 70%（透過 OpenWebUI / Workspace log）| 後台統計 |

### 2.2 簽核者 / Sign-off

| 角色 / Role | 簽 / Sign |
|---|---|
| **教務主任 / Academic Dean** | 主要簽核 |
| **教學組長 / Curriculum Head** | 教學品質驗收 |
| **AI Champion** | 種子計畫驗收 |
| **學科召集人 / Subject Head**（≥ 3 位）| 各科認可 |

### 2.3 未過 Gate 2 的常見原因 / Common Gate 2 failures

| 症狀 | 根因 | 補強 |
|---|---|---|
| NotebookLM 蓋好但同事不用 | 種子教師沒帶其他人試用 | 安排「教 1 帶 5」共備 |
| 學科 Prompt 不分享出來 | 沒有共用 Prompt Library 機制 | 建立校內 wiki / Drive 共用區 |
| 種子教師說「沒時間做」 | 校長沒給時數補償 | 給種子教師 2-4 節減課 |
| AI 使用率 < 50% | L1 沒紮實，無法支撐 L2 | 退回 L1 補強 |

---

## 3. Gate 3 — L3 行政流程自動化就緒 / Gate 3: L3 Admin Workflow Ready

### 3.1 通過條件 / Pass criteria

| # | 條件 / Criterion | 證據 / Evidence |
|---|---|---|
| 1 | 至少 2 個 L3 use case 已上線並穩定運作 ≥ 1 個月 | Execution log 統計 |
| 2 | 每個 use case 自動化前後的時間 / 錯誤率對比已量測 | KPI 對比表 |
| 3 | 每個 use case 有完整 HITL Gate 設計 + 至少觸發過 1 次人工審核 | HITL 觸發紀錄 |
| 4 | 行政組長能獨立維運（≥ 1 個月無顧問介入） | 維運日誌 |
| 5 | 故障處理 SOP 已寫 + 真正跑過 1 次 rollback | Rollback drill 紀錄 |
| 6 | 學校 IT 或行政組長有能力修改 Apps Script 的小參數 | 變動 commit 紀錄 |
| 7 | 上線前法務 / 隱私審查已過（特別是涉及學生 / 家長資料的）| 審查紀錄 |

### 3.2 簽核者 / Sign-off

| 角色 / Role | 簽 / Sign |
|---|---|
| **校長 / Principal** | **必須親簽**（涉及對外公文與家長通知） |
| **教務 / 學務 / 總務主任** | 各自業務面驗收 |
| **IT 組長 / IT Lead** | 技術面 + 維運能力 |
| **法務 / 個資保護人員**（若有專任）| 合規面 |
| **家長代表**（PTA 推薦 ≥ 1 位）| 對家長端的影響面 |

> 家長代表簽核**很重要**。L3 涉及對家長端輸出（通知、簽核回傳），沒讓家長代表事先了解 = 上線後家長群組爆炸。

> Parent representative sign-off is **critical**. L3 affects parent-facing outputs; not informing parents in advance = parent group explosion after launch.

### 3.3 未過 Gate 3 的常見原因 / Common Gate 3 failures

| 症狀 | 根因 | 補強 |
|---|---|---|
| 上線後 AI 出錯沒人發現 | HITL Gate 設太鬆，AI 全自動 | 重新檢視 HITL Gate（見 [HITL_GATES_SCHOOL.md](TIGERAI_HITL_GATES_SCHOOL.md)） |
| 上線後一週就靠顧問救火 | 行政組長能力不足 | 顧問下台前再加 4 週手把手帶 |
| 家長抗議「AI 回我？」 | 對家長端輸出沒揭露用 AI | 通知改加上「本訊息經 AI 助理草擬，由 XX 老師審查送出」 |
| 學生資料被 LLM 學走 | 用了雲端 LLM 處理學生 PII | 改用地端 Ollama 處理機敏資料 |
| 上線後流程改了沒人改 Apps Script | 沒交接技術維運能力 | 補 IT 教 Apps Script 基礎課 |

---

## 4. Gate 4 + Gate 5（學校通常不需要） / Gate 4 + 5 (usually unnecessary for schools)

如前述 [`TIGERAI_METHODOLOGY_LAYER.md`](TIGERAI_METHODOLOGY_LAYER.md) §6，學校多數**不應推 L4-L5**。

> 例外：大型私立完全中學想做「校史 Hermes Agent」可考慮 L4 Gate 4A-4E（見主 toolkit `L4_HERMES_AGENT_COURSE_PLAN.md`）。

As stated in §6 of [`TIGERAI_METHODOLOGY_LAYER.md`](TIGERAI_METHODOLOGY_LAYER.md), most schools should **NOT** pursue L4-L5.

Exception: large private K-12 considering "school history Hermes Agent" may use L4 Gate 4A-4E (see main toolkit `L4_HERMES_AGENT_COURSE_PLAN.md`).

---

## 5. Gate 走完後的後續維運 / Post-Gate Operations

| 頻率 / Frequency | 動作 / Action |
|---|---|
| **每月 / Monthly** | 校長 + AI Champion + IT 組長 30 分鐘月會：看 KPI、處理 incident、調整規範 |
| **每季 / Quarterly** | 全體教師回饋 survey + 公布 AI 使用統計 + 公告下季調整 |
| **每學年 / Yearly** | 校務會議 review：Gate 全部 re-audit + 規範更新 + AI 採購 review |
| **緊急 / Ad-hoc** | 出 incident（資料外洩、AI 對外失誤）→ 24 小時內校長 + 法務 review |

---

## 6. Gate 走不下去的退場機制 / Exit mechanism if Gates fail

如果在某個 Gate 卡住超過 3 個月仍過不去：

If stuck at a Gate for > 3 months with no progress:

| 狀況 / Situation | 建議 / Recommendation |
|---|---|
| L1 卡住 | 退一步：先暫停 AI 推動，做組織文化變革 |
| L2 卡住 | 縮小範圍：從「全校 5 科」改成「種子 2 科」深耕 |
| L3 卡住 | 縮小範圍：從「全面行政自動化」改成「單一 use case 做透」 |
| 任何 Gate 卡住 + 校長換人 | **暫停整個方案 + 等新校長表態**，不要硬推 |

**重要原則：學校 AI 導入是長期工程，慢慢來比較快。Gate 過不了不是失敗，是訊號 → 重新評估範圍與節奏。**
**Key principle: school AI adoption is a long-term project; slow is fast. Gate failures are signals, not failures themselves → reassess scope and pace.**

---

**Version:** v0.1.0 (2026-05-20)
**License:** Apache 2.0
