# OpenWebUI 影片學習紀錄與應用摘要

版本：v1.0  
作者：Morris  
整理目的：將 OpenWebUI playlist 轉成 L1 企業啟用課的學習紀錄、摘要與未來應用地圖。  
原始 Playlist：`https://www.youtube.com/watch?v=oXJ4L1G8kaI&list=PL_rTgQnnMXsXAsEiid-tWhaj03SsP4U5Z`

---

## 1. 使用方式

這份文件不是逐字稿，而是課程設計用的學習紀錄。每支影片都被對應到：

1. 影片主題。
2. 學習摘要。
3. 未來在 TigerAI L1-L5 方法論中的應用。
4. 課程優先級。

優先級定義：

| 優先級 | 說明 |
|---|---|
| P0 | L1 企業啟用必看，直接影響帳號、登入、使用、權限、資料安全 |
| P1 | Admin / IT 必看，影響部署、模型、維運、權限、更新 |
| P2 | 功能選修，依客戶需求加入 |
| P3 | 靈感案例，可用於展示或後續 L2/L3/L4 延伸 |

---

## 2. 對 L1 課程的總結論

OpenWebUI 不應只被包裝成「免費 ChatGPT 替代品」。在企業導入時，它的核心價值是：

> 讓公司用一個受控入口管理 AI 使用，每位員工有自己的帳號與聊天區域，Admin 能管理角色、群組、權限、模型、工具與資料邊界。

因此，L1 課程的主軸應該是：

1. 每人登入，不共用帳號。
2. 每人有自己的聊天歷史、資料夾、Prompt 與個人設定。
3. Admin 能管理使用者、角色、群組、權限與模型可見性。
4. IT 能決定本地模型、雲端 API、Hybrid 模式與維運更新策略。
5. HR / 管理者能建立 AI 使用規範與資料輸入邊界。
6. L1 的輸出要銜接 L2：把高頻 Prompt 與工作情境整理成 Skill 候選。

---

## 3. 影片學習摘要與未來應用

| # | 影片 | 學習摘要 | 未來應用 | 優先級 |
|---:|---|---|---|---|
| 1 | [Open WebUI: The Free, Private ChatGPT Alternative](https://www.youtube.com/watch?v=oXJ4L1G8kaI) | OpenWebUI 的定位、價值與基本使用情境。 | L1 開場，用來說明為什麼企業需要自己的 AI 入口。 | P0 |
| 2 | [How to Install OpenWebUI](https://www.youtube.com/watch?v=d6Su3Nmv7-8) | 安裝 OpenWebUI 的基礎流程。 | IT 課前準備、PoC 環境建立、部署檢查表。 | P1 |
| 3 | [Local AI Model Requirements](https://www.youtube.com/watch?v=CYBu9dTVWC4) | 本地模型所需 CPU、RAM、GPU 概念。 | 雲 AI / Hybrid / 全地端部署評估，幫客戶判斷硬體門檻。 | P1 |
| 4 | [Exploring the OpenWebUI Admin Panel](https://www.youtube.com/watch?v=4pIzLtUhJLM) | Admin Panel 功能總覽與管理入口。 | L1 Admin 課必看，對應帳號、模型、功能、設定管理。 | P0 |
| 5 | [Exploring Open WebUI: Features, Models, & Tools](https://www.youtube.com/watch?v=CDiVq3mPZc8) | OpenWebUI 功能、模型與工具概覽。 | L1 全員導覽，讓學員知道可用功能與邊界。 | P0 |
| 6 | [How to Chat with Your Own Documents](https://www.youtube.com/watch?v=lqKapMX2GAI) | 使用自己的文件做聊天與問答。 | L1 文件摘要與低敏感文件問答；高敏感資料需另設規範。 | P0 |
| 7 | [How to Add Real-Time Web Search](https://www.youtube.com/watch?v=_KoifHHJhNY) | 加入即時 Web Search。 | 研究、業務、行銷情境；企業需設定來源引用與權限。 | P2 |
| 8 | [How to Add GPT-4 to OpenWebUI](https://www.youtube.com/watch?v=ZUc50fcWO2E) | 串接 OpenAI API / GPT-4 類模型。 | Admin / IT 設定雲端模型 provider；可用於 Hybrid 架構。 | P1 |
| 9 | [How to Use Community Tools](https://www.youtube.com/watch?v=juAbnns5Ohg) | 使用社群工具擴充能力。 | L2/L3 前置；企業需先做安全審查與工具白名單。 | P2 |
| 10 | [Text-to-Speech with ElevenLabs API](https://www.youtube.com/watch?v=LzlzXQzBUcg) | 串接 TTS 與語音輸出。 | 客服、教育、訓練教材選修；非 L1 核心。 | P2 |
| 11 | [How to Create Custom AI Models](https://www.youtube.com/watch?v=Fd_1zePgCLE) | 建立客製化模型設定或模型角色。 | 部門預設模型、角色化助理；可銜接 L2 Skill。 | P2 |
| 12 | [AI Images with OpenWebUI & DALL-E 3](https://www.youtube.com/watch?v=3rg8Tdyn_RA) | 圖像生成能力。 | 行銷設計選修；需注意版權、品牌與審核。 | P2 |
| 13 | [LLAVA Multimodal / GPT-4 Image Analysis](https://www.youtube.com/watch?v=yZkmolyV0Zk) | 使用多模態模型分析圖片。 | 品管、醫療、文件影像初步探索；高風險場景需人工審核。 | P2 |
| 14 | [AI Clone](https://www.youtube.com/watch?v=dXaFbHw5-m8) | 個人化 AI clone 概念展示。 | 展示靈感；企業導入需特別處理隱私與肖像/聲音授權。 | P3 |
| 15 | [Functions to Build Websites & Apps](https://www.youtube.com/watch?v=KbkfaapAvpE) | 使用 Functions 擴充應用能力。 | L2/L3 延伸：把聊天能力轉成可執行工具或 app prototype。 | P2 |
| 16 | [Reduce AI Hallucinations with Advanced Parameters](https://www.youtube.com/watch?v=OWsFsnnrMdE) | 使用進階參數降低幻覺風險。 | L1 必看，用於資料可信度、人工確認、模型參數教育。 | P0 |
| 17 | [Choosing the Right Ollama Model](https://www.youtube.com/watch?v=KIc1lRmehyY) | 選擇合適的本地 Ollama 模型。 | IT / Admin 模型管理與地端部署評估。 | P1 |
| 18 | [Mobile Access with Ngrok](https://www.youtube.com/watch?v=DFtI1m957XM) | 用 Ngrok 遠端或手機存取 OpenWebUI。 | 選修；企業需注意資安、VPN、暴露面與存取控制。 | P2 |
| 19 | [Choosing the Best Language Model](https://www.youtube.com/watch?v=-yhChXlYjbQ) | 不同語言模型選型方法。 | 管理模型清單與部門適用模型，銜接模型評估表。 | P1 |
| 20 | [Vision LLMs for Local Inference](https://www.youtube.com/watch?v=VDLNtKbfewQ) | 本地視覺模型比較。 | 品管、影像文件、醫療影像探索；屬進階選修。 | P2 |
| 21 | [AI Recruiter Meets AI Clone](https://www.youtube.com/watch?v=649qtKjbnk4) | 招募與 AI clone 的展示情境。 | HR 案例靈感，可轉成 L2 招募 Skill 或 L3 招募流程。 | P3 |
| 22 | [Groq Cloud & OpenWebUI](https://www.youtube.com/watch?v=Ukft9qfb67o) | 串接 Groq Cloud 等雲端模型。 | IT / Admin 建立多模型 provider 策略。 | P1 |
| 23 | [Docker & Watchtower](https://www.youtube.com/watch?v=W0Yh_HsMkOQ) | Docker 容器自動更新與維運。 | IT 維運必看，對應 OpenWebUI 更新與服務穩定性。 | P1 |
| 24 | [OpenWebUI Pipelines](https://www.youtube.com/watch?v=DFlSd6GrMIk) | Pipelines 自訂工作流能力。 | L3 預告；未來可與 n8n、API、資料處理流程銜接。 | P2 |
| 25 | [Set Up User Roles for Secure Collaboration](https://www.youtube.com/watch?v=xlE782FrW_s) | 設定使用者角色與安全協作。 | L1 Admin 必看，對應企業每人帳號、角色、群組、權限。 | P0 |
| 26 | [Writing Better Prompts](https://www.youtube.com/watch?v=FYTir7cor1c) | 寫出更好的 Prompt。 | L1 全員必看，對應 Prompt Library 與 L2 Skill 候選。 | P0 |
| 27 | [Arena Model](https://www.youtube.com/watch?v=PU7B5FHalrg) | 模型比較與表現測試。 | Admin / 種子人員用來做模型評估與採購判斷。 | P1 |
| 28 | [Run Text-to-Speech Locally](https://www.youtube.com/watch?v=lwk0QGLou9Y) | 本地 TTS。 | 高隱私語音需求選修；非 L1 核心。 | P2 |
| 29 | [OpenWebUI Memory Explained](https://www.youtube.com/watch?v=a0H2w5z_uk4) | Memory / 個人化記憶概念。 | 可作為個人化能力介紹；企業需先處理隱私、刪除與資料留存政策。 | P2 |
| 30 | [Quantization](https://www.youtube.com/watch?v=7J-AKL2TAD0) | 模型量化與效能改善。 | IT 選修，協助地端部署與成本控制。 | P2 |
| 31 | [AI-Powered Recruiter Bot](https://www.youtube.com/watch?v=XPeZGo6McLc) | 招募 Bot 建置案例。 | HR / L2 / L3 案例：職缺分析、履歷摘要、面試問題草稿。 | P3 |
| 32 | [Open WebUI v0.4 Updates](https://www.youtube.com/watch?v=qESVuLFHYqI) | 版本更新與新功能。 | IT / Admin 維持版本意識；建立更新檢查 SOP。 | P1 |
| 33 | [Anthropic Claude Models in OpenWebUI](https://www.youtube.com/watch?v=1jahR-BA6Ts) | 串接 Claude 模型。 | Admin / IT 設定多 provider；適合 Hybrid 模型策略。 | P1 |
| 34 | [Public Access to OpenWebUI Chatbots](https://www.youtube.com/watch?v=0pyHYhzqdRQ) | 公開 Chatbot 存取。 | 高風險功能；企業需嚴格控管，適合外部客服 PoC 前討論。 | P2 |
| 35 | [Tools, Functions & Pipelines Deep Dive](https://www.youtube.com/watch?v=wRkAko8yphs) | Tools、Functions、Pipelines 深度說明。 | L2/L3 預告，讓 OpenWebUI 從聊天入口走向工具與流程。 | P2 |
| 36 | [Online? Offline? Both?](https://www.youtube.com/watch?v=W9czUS3trMU) | 線上、離線、混合模式討論。 | L1 部署模式討論必看，對應雲 AI / Hybrid / 全地端。 | P0 |

---

## 4. 推薦觀看路線

### 4.1 全員 L1 使用者

建議觀看：

1. #1 OpenWebUI 定位。
2. #5 功能、模型與工具總覽。
3. #6 文件聊天。
4. #16 降低幻覺與進階參數。
5. #26 Prompt 寫作。
6. #36 線上 / 離線 / 混合模式。

目的：讓員工能安全登入、建立自己的聊天區、完成日常任務並知道資料邊界。

### 4.2 Admin / IT

建議觀看：

1. #2 安裝。
2. #3 本地模型硬體需求。
3. #4 Admin Panel。
4. #8 OpenAI API。
5. #17 Ollama 模型。
6. #19 模型選型。
7. #22 Groq Cloud。
8. #23 Docker / Watchtower。
9. #25 User Roles。
10. #32 版本更新。
11. #33 Claude 模型。

目的：讓 IT 能建立、維運、管理與治理 OpenWebUI。

### 4.3 L2 / L3 延伸

建議觀看：

1. #9 Community Tools。
2. #11 Custom AI Models。
3. #15 Functions。
4. #24 Pipelines。
5. #35 Tools / Functions / Pipelines Deep Dive。

目的：把 OpenWebUI 從 L1 Chat 入口銜接到 L2 Skill 與 L3 Workflow。

### 4.4 產業選修

| 產業 / 部門 | 建議影片 |
|---|---|
| HR | #21、#31 |
| 行銷 / 設計 | #12 |
| 客服 / 教育訓練 | #10、#28 |
| 品管 / 醫療 / 影像文件 | #13、#20 |
| 高隱私企業 | #3、#17、#23、#30、#36 |

---

## 5. 對課程與交付的應用

### 5.1 L1 課程應用

必須轉成以下課程交付：

- OpenWebUI 使用者操作手冊。
- OpenWebUI Admin Runbook。
- 帳號 / 群組 / 權限 / 模型可見性設定表。
- AI 使用規範。
- Prompt Library v1。
- Gate 1 驗收表。

### 5.2 L2 課程應用

可以把以下影片轉成 Skill 候選：

- #26 Prompt 寫作 → Prompt Skill。
- #6 文件聊天 → 文件摘要 Skill。
- #11 Custom AI Models → 部門角色模型 Skill。
- #15 Functions → 工具化 Skill。
- #35 Tools / Functions / Pipelines → L2-to-L3 Bridge。

### 5.3 L3 課程應用

可以把以下影片轉成 Workflow 候選：

- #7 Web Search → 市場研究 Workflow。
- #24 Pipelines → 自訂處理流程。
- #35 Tools / Functions / Pipelines → OpenWebUI + n8n 流程銜接。
- #34 Public Chatbots → 外部客服 Bot PoC，但需嚴格權限與審核。

---

## 6. 企業導入注意事項

1. 不可共用帳號，否則無法做到個人聊天區、責任歸屬與權限治理。
2. 新使用者預設不應直接給進階功能，建議由 Admin 審核。
3. File Upload、Web Search、Tools、Functions、Pipelines、Public Share 都應視為進階功能。
4. 每個部門應有自己的群組與模型可見性策略。
5. 高敏感產業應先確認雲 AI / Hybrid / 全地端部署模式。
6. Memory 與個人化能力需要隱私、刪除、資料留存政策。
7. 公開 Chatbot 或外部存取不應在 L1 大規模開放，需另開 PoC。
8. 每次版本更新都要更新 Admin Runbook 與使用規範。

