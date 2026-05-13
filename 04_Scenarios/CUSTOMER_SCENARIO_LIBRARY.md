# 客戶情境故事庫

更新日期：2026-05-13

## 1. 使用目的

客戶需要透過故事理解 AI 成熟度，而不是只聽工具名稱。

每個故事採同一格式：

- Before：現在怎麼做，有什麼痛點。
- Trigger：什麼事件啟動 AI 流程。
- AI Flow：OpenWebUI、Skill、n8n、Hermes Agent、ClawTeam 如何介入。
- Systems：串接哪些系統。
- Output：產出什麼。
- KPI：如何衡量價值。

## 2. 管理層故事

### 2.1 CEO：我想知道 AI 投資有沒有 ROI

Before：公司各部門都說在用 AI，但 CEO 只聽到零散案例，無法判斷投資效益。

Trigger：CEO 要求管理團隊在季度會議前提出 AI 導入現況與下一步。

AI Flow：

1. 用成熟度問卷取得各部門 L1-L5 現況。
2. 用 n8n 收集問卷結果並寫入 Sheets。
3. Hermes Agent 整理各部門成熟度、缺口與建議。
4. 顧問用八階段方法產出 AI 轉型診斷報告。

Systems：Google Forms、Sheets、Notion、CRM、ERP、n8n。

Output：AI 成熟度雷達圖、三階段 Roadmap、ROI 追蹤矩陣。

KPI：可量化場景數、預估節省工時、PoC 完成數、Stage Gate 達成率。

### 2.2 COO：我想降低流程重工

Before：跨部門流程依賴人工複製貼上，資料散在 Gmail、Sheets、CRM、ERP。

Trigger：每週營運會議前，需要彙整訂單、客訴、出貨、庫存與異常。

AI Flow：

1. L2 建立「營運異常分析 Skill」。
2. n8n 定期從 ERP、CRM、Sheets 取得資料。
3. AI 依 Skill 分類異常原因。
4. Hermes Agent 產出主管摘要與追蹤清單。

Systems：ERP、CRM、Google Sheets、Email、n8n。

Output：營運異常週報、責任部門清單、改善建議。

KPI：週報製作時間、異常回應時間、重複輸入次數、漏追蹤案件數。

### 2.3 CIO / IT：我想管得住 AI

Before：員工各自使用雲端 AI，IT 不清楚資料流向、權限與風險。

Trigger：公司準備導入 OpenWebUI、n8n 與 Agent，需要 IT 設定治理原則。

AI Flow：

1. L1 建立受控 AI 入口。
2. L3 建立 n8n Credential 與權限管理。
3. L4 設定 Agent 可呼叫工具與不可碰資料。
4. 顧問報告建立治理矩陣。

Systems：OpenWebUI、n8n、SSO、API、DB、ERP。

Output：AI 使用規範、權限表、Log 需求、部署模式建議。

KPI：未授權 AI 使用下降、流程 Log 完整度、權限例外數、資安事件數。

### 2.4 HR：我想讓 AI 訓練真的落地

Before：員工上完 AI 課很興奮，但一個月後回到原本工作方式。

Trigger：HR 要規劃 AI 訓練與部門種子人員制度。

AI Flow：

1. 課前用 25 題問卷分組。
2. 課中產出每個部門的 Prompt、Skill、Workflow 候選清單。
3. 課後用 Notion 建立 Skill Library。
4. Hermes Agent 每週提醒部門更新實作成果。

Systems：Google Forms、Sheets、Notion、OpenWebUI、n8n。

Output：訓練分組、學習成果、部門 Skill Library、課後追蹤表。

KPI：參訓人數、Skill 產出數、實際採用率、新人上手時間。

## 3. 部門故事

### 3.1 業務：客戶拜訪準備與 CRM 更新

Before：業務拜訪前要查客戶資料、整理歷史互動、寫提案摘要，拜訪後還要回填 CRM。

Trigger：CRM 中新增一場客戶拜訪行程。

AI Flow：

1. n8n 從 CRM 取得客戶資料與商機狀態。
2. 從 Gmail 找近期往來信件摘要。
3. 使用 L2「拜訪準備 Skill」整理客戶背景、痛點、建議話題。
4. Hermes Agent 產出拜訪準備包。
5. 會後自動產出 CRM 更新草稿。

Systems：CRM、Gmail、Google Calendar、Sheets、n8n。

Output：拜訪摘要、提問清單、提案方向、CRM 更新草稿。

KPI：拜訪準備時間、CRM 更新率、提案產出速度、商機推進率。

### 3.2 客服：Gmail 客訴分類與案件追蹤

Before：客服每天人工看信、分類、查 CRM、查 ERP 訂單，再建立追蹤任務。

Trigger：Gmail 收到客訴或服務信件。

AI Flow：

1. n8n 讀取 Gmail 信件。
2. AI 判斷客訴類型、急迫性與情緒。
3. CRM 查客戶等級與歷史案件。
4. ERP 查訂單、出貨或庫存狀態。
5. Notion 建立案件任務。
6. Hermes Agent 產出回覆草稿與追蹤提醒。

Systems：Gmail、CRM、ERP、Notion、Sheets、n8n。

Output：案件分類、回覆草稿、處理任務、客服週報。

KPI：首次回應時間、分類準確率、漏案率、客服工時。

### 3.3 行銷：活動企劃與成效報告

Before：行銷要蒐集競品、寫文案、整理廣告成效、產出週報，資料散在 Sheets、社群平台、CRM。

Trigger：主管要求規劃下月活動。

AI Flow：

1. OpenWebUI 協助市場與競品初稿。
2. L2「活動企劃 Skill」產出活動主題、受眾、文案方向。
3. n8n 從 Sheets 與 CRM 取得名單與成效資料。
4. Hermes Agent 整理活動計畫與預估 KPI。

Systems：Sheets、CRM、Notion、Email、廣告平台 API。

Output：活動企劃書、文案素材、受眾清單、成效報告。

KPI：企劃時間、素材產出量、活動轉換率、報告製作時間。

### 3.4 營運：ERP 異常訂單分析

Before：營運主管每天從 ERP 匯出訂單，再用 Excel 找延遲、缺料、異常狀態。

Trigger：ERP 出現延遲出貨、庫存不足或高價值訂單異常。

AI Flow：

1. n8n 定期取得 ERP 訂單資料。
2. L2「異常訂單分析 Skill」分類異常原因。
3. AI 將結果寫入 Sheets。
4. Hermes Agent 產出主管摘要與責任部門追蹤清單。

Systems：ERP、Sheets、Email、Notion、n8n。

Output：異常訂單清單、原因分類、追蹤任務、主管摘要。

KPI：異常發現時間、人工整理工時、延遲改善率、追蹤完成率。

### 3.5 財務：月結差異分析

Before：財務月結時需要人工比對費用、預算、部門說明與報表差異。

Trigger：每月結帳日或費用資料更新。

AI Flow：

1. n8n 從 ERP 或財務系統取得費用資料。
2. Sheets 整理部門預算與實際費用。
3. L2「差異說明 Skill」產生初步解釋。
4. Hermes Agent 彙整需人工確認的異常項目。

Systems：ERP、Sheets、Email、內部財務系統、n8n。

Output：月結差異摘要、待確認清單、主管報告初稿。

KPI：月結分析時間、人工查核次數、異常項目追蹤率。

### 3.6 人資：新人訓練與知識庫

Before：新人報到後要問很多人，SOP 分散在不同文件與聊天紀錄。

Trigger：新人報到或轉調部門。

AI Flow：

1. L2 建立「新人上手 Skill」。
2. Notion 建立部門知識庫。
3. OpenWebUI 提供新人問答入口。
4. n8n 定期提醒主管補齊缺失文件。

Systems：Notion、OpenWebUI、Sheets、Email、n8n。

Output：新人學習路線、FAQ、SOP 查詢、訓練完成紀錄。

KPI：新人上手時間、重複詢問次數、文件完整度、訓練完成率。

### 3.7 IT：API 串接與流程維運

Before：各部門都想串系統，但需求分散，權限與維運責任不清楚。

Trigger：部門提出 n8n Workflow 或 Agent 串接需求。

AI Flow：

1. IT 使用系統盤點表確認資料源、API、權限。
2. n8n 建立 Credential 與執行 Log。
3. Hermes Agent 監控流程失敗並通知 Owner。
4. 顧問報告整理治理與維運建議。

Systems：n8n、API Gateway、DB、ERP、CRM、Log 系統。

Output：系統串接表、權限矩陣、流程維運規則。

KPI：串接交付時間、流程失敗率、權限例外數、維運工時。

## 4. ClawTeam 高階故事：新產品上市

Before：新產品上市需要市場、產品、行銷、客服、財務多部門協作，通常要開多次會議才有初稿。

Trigger：CEO 下達任務：「三週內提出新產品上市計畫。」

AI Flow：

1. 市場分析 Agent 研究市場與競品。
2. 產品規劃 Agent 整理功能、定位與 Roadmap。
3. 行銷策略 Agent 產出活動與訊息。
4. 客服支援 Agent 準備 FAQ 與服務流程。
5. 財務分析 Agent 估算預算、成本與 ROI。
6. 專案整合 Agent 形成完整計畫草案。
7. 人工 Gate 審核後進入主管會議。

Systems：CRM、Sheets、Notion、ERP、外部資料 API、n8n、ClawTeam。

Output：市場分析、產品規劃、行銷策略、客服準備、財務預估、專案計畫。

KPI：計畫初稿時間、跨部門會議次數、資料完整度、決策速度。

