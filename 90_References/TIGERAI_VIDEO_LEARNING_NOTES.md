# TigerAI 頻道影片學習紀錄與 L3 應用摘要

版本：v1.0  
作者：Morris  
頻道：虎智科技 TigerAI  
原始頻道：`https://www.youtube.com/@%E8%99%8E%E6%99%BA%E7%A7%91%E6%8A%80TigerAI`

---

## 1. 使用方式

這份文件整理 TigerAI 頻道中可用於 L1-L4 課程設計的影片，特別聚焦 n8n 與 L3 Workflow Automation。

整理方式：

1. 依公開可取得的影片清單與標題建立學習摘要。
2. 將影片對應到 L1 / L2 / L3 / L4 課程用途。
3. 將 n8n 影片整理成 L3 上課模組與 PoC 路線。
4. 將 OpenGenie 影片整理成企業治理、帳號、權限、模型、Prompt、Channels、n8n 串接、RAG/Vision 與回饋系統的導入脈絡。

優先級：

| 優先級 | 說明 |
|---|---|
| P0 | L3 n8n 主課必看 |
| P1 | L1 / L2 / L3 / L4 的重要支援內容 |
| P2 | 產業或部門選修案例 |
| P3 | 展示與靈感案例 |

---

## 2. 對 L3 課程的總結論

TigerAI 的 n8n 影片不是單純工具教學，而是一組很完整的企業流程自動化案例庫。它呈現的 L3 訓練邏輯應該是：

> 從 L2 產出的 Skill / Workflow Blueprint 接手，用 n8n 把它變成可執行、可驗證、可備份、可維運、可串平台的流程 PoC。

因此 L3 課程應強調：

1. Trigger：Webhook、排程、Gmail、LINE、Facebook、YouTube、GCS / API event。
2. Data Handling：Data Tables、Sheets、BigQuery、CRM / ERP / API 資料。
3. AI Processing：Gemini、圖片、語音、影片、文件、文案、摘要、分類。
4. Platform Integration：LINE、Facebook、YouTube、社群平台、Gmail、GitHub。
5. Reuse：Sub-workflow 模組化。
6. Governance：Credentials、Execution Log、GitHub 備份、人工審核、錯誤處理。
7. L4 Readiness：讓 Hermes Agent 未來可以呼叫 n8n Workflow。

---

## 3. OpenGenie 企業治理影片摘要

| # | 影片 | 學習摘要 | 課程應用 | 優先級 |
|---:|---|---|---|---|
| OG-1 | [TigerAI OpenGenie 單元 1：帳號體系與權限佈署](https://www.youtube.com/watch?v=wkgx94TmFE4) | 帳號、使用者與權限部署。 | L1 OpenWebUI / OpenGenie 企業啟用，對應每人帳號與權限治理。 | P1 |
| OG-2 | [單元 2：後端模型 Ollama 管理與安裝](https://www.youtube.com/watch?v=fyK8lIBEdoU) | 後端模型安裝與管理。 | L1 IT / Admin 模型管理，支援雲 AI / Hybrid / 全地端判斷。 | P1 |
| OG-3 | [單元 3：API Key 彈性配置](https://www.youtube.com/watch?v=IdI_pqRjEOU) | API Key 與雲端輔助策略。 | L1/L3 IT，管理模型 provider、外部 API 與權限。 | P1 |
| OG-4 | [單元 4：Prompts 專家設定](https://www.youtube.com/watch?v=CZwXcgtKn0Y) | 專家 Prompt 設定。 | L1 Prompt Library、L2 Skill 化。 | P1 |
| OG-5 | [單元 5：群組與協作權限深度管理](https://www.youtube.com/watch?v=G1MKa10W6K0) | 群組與協作權限。 | L1 Admin / L3 流程權限設計。 | P1 |
| OG-6 | [單元 6：Channels 協作與會議摘要](https://www.youtube.com/watch?v=38kkwwRDOpU) | Channels、協作與會議摘要。 | L1 部門協作、L2 會議摘要 Skill、L3 會議流程。 | P2 |
| OG-7 | [單元 7：n8n 串接與自動化工作流](https://www.youtube.com/watch?v=xX6e0l-TaWg) | OpenGenie 與 n8n 串接、自動化工作流。 | L3 主課核心，作為 L3 入口影片。 | P0 |
| OG-8 | [單元 8：多模態進階應用 RAG & Vision](https://www.youtube.com/watch?v=qN_2KSgbjUM) | RAG、Vision、多模態應用。 | L3 Gemini / 多模態流程，L4 Hermes 知識工作前置。 | P1 |
| OG-9 | [單元 9：綜合應用與分享機制](https://www.youtube.com/watch?v=jQPBSZmYLbg) | 綜合應用、分享與協作。 | L1/L3 分享治理與 Demo 展示。 | P2 |
| OG-10 | [單元 10：管理監督與回饋系統](https://www.youtube.com/watch?v=4Lrgg-vdhi8) | 管理監督與回饋。 | L3 維運、回饋、品質改善與 Gate 3 驗收。 | P1 |

---

## 4. Antigravity / L2 影片摘要

| # | 影片 | 學習摘要 | 課程應用 | 優先級 |
|---:|---|---|---|---|
| AG-1 | [1部曲：AI 全自動寫代碼、測試還幫你錄影](https://www.youtube.com/watch?v=LCO700FzoXg) | Antigravity 基礎入門、AI 寫代碼、測試、錄影 evidence。 | L2 Antigravity Foundation。 | P1 |
| AG-2 | [2部曲：AI 寫 Code 鬼打牆怎麼辦](https://www.youtube.com/watch?v=RRWtnqqQI0E) | 除錯心法、Skill 外掛擴充。 | L2 Debug / Skill 化。 | P1 |
| AG-3 | [3部曲：開發環境零手動](https://www.youtube.com/watch?v=kHywZFPsju8) | AI 安裝套件與 UI。 | L2 工程實作。 | P1 |
| AG-4 | [4部曲：爬蟲與架站](https://www.youtube.com/watch?v=K4UMhFj9ztE) | 資料抓取與客製化網頁 UI。 | L2 App prototype；L3 可接資料流程。 | P1 |
| AG-5 | [5部曲：Docker 容器化與打包](https://www.youtube.com/watch?v=IILRXP2cMbo) | Docker 容器化。 | L2 工程交付與 L3 部署前置。 | P1 |
| AG-6 | [6部曲：互動 App 與個人專屬 Skill](https://www.youtube.com/watch?v=q9rNgnqNXlc) | 建立互動 App 與個人 Skill。 | L2 Skill Library 與 L2-to-L3 Bridge。 | P1 |

---

## 5. n8n / L3 影片摘要

| # | 影片 | 學習摘要 | L3 課程應用 | 優先級 |
|---:|---|---|---|---|
| N27 | [不寫程式也能用 Gemini：n8n 整合 Google Gemini 全攻略](https://www.youtube.com/watch?v=DT5Gx5tMxGs) | 用 n8n 整合 Gemini 處理圖片、語音、影片、文件。 | L3 AI Node / 多模態處理基礎。 | P0 |
| N28 | [n8n 進階教學：Sub-workflow 模組化自動化術](https://www.youtube.com/watch?v=hbvHwjrexds) | 建立可重複使用的 Sub-workflow。 | L3 模組化與流程標準化必看。 | P0 |
| N29 | [AI 即時查詢神器：高鐵時刻查詢機器人](https://www.youtube.com/watch?v=T1hzDrIhHSk) | LINE 自動回覆班次、票價與時刻。 | Webhook / LINE / API 查詢流程案例。 | P0 |
| N30 | [AI 人資革命：自動履歷篩選系統](https://www.youtube.com/watch?v=EgSFZm6hvE8) | n8n + Gemini + Gmail + LINE HR 流程。 | HR 流程 PoC：履歷進件、AI 篩選、通知。 | P0 |
| N31 | [史上最強社群自動化](https://www.youtube.com/watch?v=Eb-DwLnNjUk) | 商品圖轉影片、文案、多平台行銷。 | 行銷自動化 PoC。 | P2 |
| N32 | [AI 自動發文 2.0](https://www.youtube.com/watch?v=hlhByT2m28M) | 影片生成、文案、多平台發布。 | 社群發文 Workflow，需人工審核 Gate。 | P2 |
| N33 | [YouTube AI 留言機器人](https://www.youtube.com/watch?v=3cB4BtGUA9w) | YouTube 留言自動回覆與關鍵字互動。 | 社群互動與客服流程。 | P2 |
| N34 | [n8n 終極備份術](https://www.youtube.com/watch?v=zrsE4-G6MRY) | Workflows + Credentials 自動同步到 GitHub。 | L3 維運、備份、版本治理必看。 | P0 |
| N35 | [Facebook 聊天機器人實戰](https://www.youtube.com/watch?v=c9VuLN_DasA) | n8n + Webhook 打造 Facebook AI 客服。 | 客服自動化主案例。 | P0 |
| N36 | [Data Tables 實戰：Facebook 智能客服](https://www.youtube.com/watch?v=v4plNZNSG08) | n8n Data Tables、Meta 平台整合、自訂 AI 回覆。 | L3 Data Tables 與狀態管理必看。 | P0 |
| N37 | [AI 客服升級版：FB 粉專自動回圖、回訊息](https://www.youtube.com/watch?v=pEWn2yh1Dkg) | 圖片與訊息的 Facebook 客服回覆。 | 多模態客服選修。 | P2 |
| N38 | [AI 自動行銷機器人](https://www.youtube.com/watch?v=njcKlnhEaUM) | Freepik + DataForSEO，自動找圖、寫文案、挑關鍵字、發文。 | 行銷內容供應鏈流程。 | P2 |
| N39 | [Sora 2 全自動影片工廠](https://www.youtube.com/watch?v=3NJZ99lY8kU) | n8n + Kie AI，一鍵生成影片並發布到 FB、IG、Threads、YouTube。 | 進階影片工廠案例；需審核與品牌 Gate。 | P3 |

---

## 6. L3 課程設計啟示

### 6.1 不能只教 n8n 基礎

TigerAI 的影片顯示，L3 真正有價值的不是「拖 node」，而是讓流程形成完整閉環：

`Trigger → Data → AI → System Action → Human Gate → Log → Backup → Reuse`

### 6.2 L3 必須有四個案例池

| 案例池 | 代表影片 | 適合客戶 |
|---|---|---|
| 客服自動化 | N35、N36、N37 | 服務業、電商、粉專、客服中心 |
| HR 自動化 | N30 | HR、招募、人資共享服務 |
| 行銷自動化 | N31、N32、N33、N38、N39 | 行銷、內容、社群、品牌 |
| 查詢 / 工具型 Bot | N29 | 營運、客服、內部查詢 |

### 6.3 L3 必須補治理課

影片 N34 的 GitHub 備份非常重要，應成為 L3 必修，而不是選修。企業導入 n8n 後，如果沒有備份、版本、Credential 管理、Execution Log 與錯誤通知，PoC 很容易變成無法維運的小玩具。

---

## 7. 推薦觀看路線

### 7.1 L3 核心班

1. OG-7：OpenGenie 與 n8n 串接。
2. N27：n8n + Gemini 多模態。
3. N28：Sub-workflow。
4. N34：GitHub 備份。
5. N35：Facebook Webhook 客服。
6. N36：Data Tables。

### 7.2 客服班

1. N35。
2. N36。
3. N37。
4. OG-10。

### 7.3 HR 班

1. N30。
2. OG-4。
3. OG-6。
4. N34。

### 7.4 行銷班

1. N31。
2. N32。
3. N33。
4. N38。
5. N39。

### 7.5 IT / 維運班

1. OG-1。
2. OG-3。
3. OG-5。
4. N28。
5. N34。
6. OG-10。

---

## 8. 對交付的應用

TigerAI 影片應轉成以下交付物：

- L3 n8n Workflow Blueprint。
- n8n Workflow JSON。
- Credential / API / Webhook 權限表。
- Data Tables Schema。
- Sub-workflow Library。
- Execution Log 與測試紀錄。
- GitHub 備份與版本管理 SOP。
- Human Gate 設計。
- Error Handling / Retry / Fallback 設計。
- L4 Hermes Agent 可呼叫 Workflow 清單。

