# AI 轉型成熟度顧問方案交付包與驗收標準

版本：v1.0  
作者：Morris

---

## 1. 交付定位

本方案可以交付，不應只被包裝成「上課」。完整交付應該是：

> 先用問卷快速診斷 AI 成熟度，再依 L1-L5 配置課程與工作坊，課中產出可用資產，課後用八階段顧問手法形成 AI 轉型診斷報告，並用 evidence 與 Stage Gate 驗收。

客戶買到的不是工具介紹，而是一套可以被主管、IT、流程 Owner、顧問共同驗證的 AI 轉型落地包。

---

## 2. 交付總覽

| 交付階段 | 對客戶的說法 | 主要交付物 | 驗收方式 |
|---|---|---|---|
| D1 診斷 | 先知道公司目前在哪一級 | 問卷、成熟度分數、缺口分析、課程比例建議 | 診斷簡報與主管確認 |
| D2 課程設計 | 不是固定課表，而是依成熟度配課 | L1-L5 課程表、公司屬性調查、部署模式建議 | 課前會議簽核 |
| D3 課程實作 | 上課中產出自己的資產 | Prompt、Skill、Workflow、Agent 任務卡、控制表 | 課堂展示與作業 |
| D4 L4 Hermes Agent PoC | 做出可追溯的 Agent 閉環 | Wiki、schema、ingest/query/update、briefing、Gate 4A-4E | Demo、Log、Evidence |
| D5 顧問診斷 | 課後形成正式轉型報告 | 八階段診斷報告、Roadmap、ROI、風險治理 | 顧問報告會議 |
| D6 後續導入 | 從 PoC 進入上線與擴散 | 90 天導入計畫、Owner、KPI、維運 Runbook | 專案啟動會 |

---

## 3. D1 成熟度診斷交付包

### 3.1 交付內容

- AI 成熟度問卷：10 題快速版 / 25 題標準版 / 50 題完整版。
- L1-L5 成熟度初判。
- 六大構面分數：工具使用、知識沉澱、流程自動化、系統整合、Agent 應用、治理與 ROI。
- 公司屬性調查：產業、部門、資料敏感度、IT 能力、決策流程。
- 部署模式建議：雲 AI、Hybrid、全地端。
- 課程比例建議：L1/L2/L3/L4/L5 各佔比。

### 3.2 Evidence

| Evidence | 說明 |
|---|---|
| 問卷原始回覆 | 可回溯每個分數來源 |
| 成熟度雷達圖 | 顯示六大構面缺口 |
| 課程比例表 | 將診斷結果轉成上課安排 |
| 管理層確認紀錄 | 確認診斷假設沒有偏離現場 |

### 3.3 驗收標準

- 客戶能理解自己目前位於 L1-L5 哪一級。
- 客戶能說出三個最重要缺口。
- 客戶同意第一波課程比例與 PoC 範圍。

---

## 4. D2 L1-L5 課程交付包

| Level | 課程交付物 | Evidence | Gate |
|---|---|---|---|
| L1 OpenWebUI | AI 使用規範、Prompt Library、部門案例 | Prompt 範本、課堂作業、使用規範 | Gate 1 |
| L2 Skill AI | Skill Library、SOP、Checklist、模板、Antigravity app prototype / test / docs / GCP PoC | Skill 文件、測試紀錄、Owner 清單、Agent artifact、部署驗證紀錄 | Gate 2 |
| L3 n8n Workflow | Workflow PoC、串接需求、Execution Log | n8n JSON、API 權限、執行紀錄 | Gate 3 |
| L4 Hermes Agent | Agent 任務卡、Wiki、L4 IPOE、briefing、Gate 4A-4E | Log、SQLite 查詢、source page、briefing、人工審核 | Gate 4 |
| L5 ClawTeam | Agent Team 角色卡、任務分工、整合報告模板 | Agent 輸出、Reviewer 紀錄、整合報告 | Gate 5 |

---

## 5. D3-L2 Antigravity 工程訓練可交付內容

Antigravity 三套 codelab 可作為 L2 工程訓練，不只交付練習截圖，而要交付可被重用的 engineering skill。

| 交付物 | 內容 | 驗收標準 |
|---|---|---|
| Antigravity 設定表 | Agent Manager、Editor、Browser、workspace、權限政策 | 學員能完成基本 task 並留下 artifact |
| App Prototype | Flask app、productivity app 或企業內部小工具 | 可本機執行或展示 |
| Unit Test Evidence | 測試檔、測試結果、修正紀錄 | 非原作者能重跑測試 |
| README / Docs | 使用說明、限制、維運方式 | 非原作者能依文件操作 |
| GCP Pipeline PoC | GCS、Pub/Sub、Cloud Run、Gemini、BigQuery | 上傳測試檔後 BigQuery 有處理結果 |
| Deployment Validation | gcloud log、Cloud Run log、BigQuery query、截圖 | IT / 講師可驗證 |
| L2 Engineering Skill | app prototype、test、deployment、validation 的可複用 SOP | 有 Owner、版本、測試紀錄 |

---

## 6. D4 L4 Hermes Agent 可交付內容

L4 Hermes Agent 是最容易被客戶質疑「到底有沒有做出來」的一段，因此必須用 evidence 驗收。

### 6.1 必交付

| 交付物 | 內容 | 驗收標準 |
|---|---|---|
| Hermes Agent 任務卡 | 角色、任務、資料源、工具、限制、人工 Gate | 部門主管與 IT 確認 |
| L4 IPOE 表 | Input / Process / Output / Evidence | 每一項都可指向實際檔案或紀錄 |
| 初始 Wiki | `purpose.md`、`SCHEMA.md`、INBOX、queue、watchlist、tasks | 檔案存在且內容符合任務 |
| Ingest 測試 | 匯入 PDF / SOP / FAQ / 報告 | 有 source page、log、index |
| Query 測試 | 至少 3 個可追溯查詢 | 回答含引用來源 |
| Update 測試 | 至少 1 次回寫或更新 | 有 diff、理由、審核紀錄 |
| Briefing 範本 | morning briefing 或 weekly briefing | 主管能直接閱讀 |
| Gate 4A-4E 表 | 環境、知識底座、ingest、query/update、治理 | 每一 Gate 有 Pass / Fail |
| 維運 Runbook | 排程、Owner、失敗處理、人工接手 | IT / Owner 能接手 |

### 6.2 可選交付

- Autonomous discovery watchlist。
- Weekly graph synthesis 報告。
- OpenWebUI 操作指令卡。
- n8n 觸發 Hermes Agent 的 Workflow。
- 部門 Agent Dashboard。

---

## 7. D5 八階段顧問診斷報告交付包

| 八階段 | 報告章節 | 交付內容 |
|---|---|---|
| 1. 問題定義 | 現況與痛點 | 為什麼客戶需要 AI 轉型 |
| 2. 資料蒐集 | 診斷資料 | 問卷、訪談、系統、流程、文件 |
| 3. 分析診斷 | 成熟度與缺口 | L1-L5 分數、六大構面、瓶頸 |
| 4. 假設驗證 | PoC 與課程成果 | 課堂資產、Workflow、Hermes Agent evidence |
| 5. 方案設計 | Roadmap | 30/60/90 天計畫與角色分工 |
| 6. 執行規劃 | 導入計畫 | Owner、資源、時程、風險 |
| 7. 效益衡量 | KPI / ROI | 節省工時、品質、速度、錯誤率 |
| 8. 制度化 | 治理與擴散 | AI 政策、Stage Gate、維運、下一波案例 |

---

## 8. 交付驗收會議流程

1. 回顧診斷結果：確認原始成熟度與缺口。
2. 回顧課程產出：逐一展示 L1-L5 資產。
3. 展示 L4 Hermes Agent：用真實任務跑一次 input → process → output → evidence。
4. 檢查 Stage Gate：確認哪些已通過、哪些不能進下一階段。
5. 說明顧問報告：提出 Roadmap、KPI、風險、後續導入建議。
6. 決定下一步：上線、擴大 PoC、補課、治理強化或進入 L5。

---

## 9. 客戶看得懂的情境故事

客戶主管看到的不是技術名詞，而是一條很清楚的故事：

> 我們先用問卷知道公司目前只是在零散使用 AI，接著用課程把同仁的 Prompt 變成 Skill，把重複流程變成 n8n Workflow，再把部門文件、FAQ、SOP 與流程輸出交給 Hermes Agent 形成可追溯的知識工作循環。課後我們不是只給講義，而是給成熟度診斷、課程資產、Agent evidence、Stage Gate 與 90 天 Roadmap，讓主管知道下一筆投資要投在哪裡。

這就是本方案可以交付的核心。
