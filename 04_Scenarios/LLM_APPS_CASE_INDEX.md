# LLM 應用案例索引表 / LLM Apps Case Index

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **參考來源 / Reference Sources（多來源索引）:**
> - [`Shubhamsaboo/awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps)（Apache-2.0，Shubham Saboo）— 100+ 可執行 AI Agent / RAG app。引用見 [`../90_References/AWESOME_LLM_APPS_REFERENCE.md`](../90_References/AWESOME_LLM_APPS_REFERENCE.md)。
> - [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub)（MIT，patchy631 / Daily Dose of Data Science）— 93+ 可執行 AI 工程專案，分初/中/進階三級。引用見 [`../90_References/AI_ENGINEERING_HUB_REFERENCE.md`](../90_References/AI_ENGINEERING_HUB_REFERENCE.md)。
>
> 本索引為本方法論原創的 L1-L5 / 課程對應，**不重製任何 app 原始碼**。每列標示其參考來源。

---

## 1. 為什麼有這份索引 / Why This Index

企業導入 Gen AI 時最大的卡點往往不是「不會做」，而是 **「不知道可以做什麼」**。本索引彙整多個高品質開源案例庫（目前 2 個來源、約 130+ 案例），**對應到本方法論的 L1-L5 成熟度模型與課程**，讓顧問與客戶能快速回答：
- 我在 L[X]，有哪些案例適合我？
- 這個案例該放在哪一級課程教？
- 哪些案例現在還不適合我（跨級了）？

> 用法：診斷出客戶 L 級後，從對應 L 級的案例表挑 3-5 個「客戶有感」的，當成 PoC 候選或上課示範。

**索引可持續擴充** — 未來評估新的開源案例庫時，新增「來源」並把案例併入對應 L 級表即可。

---

## 2. 對應邏輯 / Mapping Logic

| 案例類型 | 對應本方法論 | 理由 |
| --- | --- | --- |
| Chat with X、Local ChatGPT、簡單 Starter | **L1 Controlled AI Access** | 與資料對話、單次任務、個人入門 |
| Agent Skills、單一用途封裝能力、OCR/Vision 抽取 | **L2 Knowledge Codification** | 可複用的封裝能力 = Skill |
| RAG 管線、MCP 整合、文件 pipeline、Chat with 系統 | **L3 Workflow Automation** | 檢索管線、工具/系統串接 |
| Advanced Single-Agent、Memory Apps、Agentic/Autonomous RAG | **L4 Autonomous Agent** | 自主多步、記憶、工具鏈、單一 Agent |
| Multi-agent Teams、Multi-Agent 應用 | **L5 Multi-Agent Organization** | 多 Agent 協作 |
| Voice、Optimization、Fine-tuning、Framework 課程、Model 比較、Game-Playing | **跨課程 / 技術支援 / 不對應** | 技術擴充或展示用，非單一 L 級課程 |

「來源」欄：`awesome-llm-apps` = A · `ai-engineering-hub` = H。

---

## 3. L1-L5 案例索引表 / The Index

### 3.1 L1 Controlled AI Access（對應課程：L1 OpenWebUI 企業啟用）

| 案例 / Case | 來源 | 原分類 | 應用情境 / 備註 |
| --- | --- | --- | --- |
| Chat with PDF（GPT & Llama3） | A | Chat with X | 文件問答 — L1 最核心入門 |
| Chat with Research Papers / ArXiv | A | Chat with X | 研究文件問答 |
| Chat with YouTube Videos | A | Chat with X | 影片摘要與問答 |
| Chat with Substack | A | Chat with X | 訂閱內容問答 |
| Chat with GitHub | A | Chat with X | L1 入門體驗；整合面向觸及 L3 |
| Chat with Gmail | A | Chat with X | L1 入門體驗；整合面向觸及 L3 |
| AI Blog to Podcast Agent | A | Starter | 內容轉換 — 單次任務 |
| AI Meme Generator Agent | A | Starter | 趣味示範，破冰用 |
| Gemini Multimodal Agent | A | Starter | 多模態對話入門 |
| Local ChatGPT（DeepSeek / Llama / Gemma 3） | H | Chat Interfaces | 地端 ChatGPT — 對應全地端部署入門 |
| DeepSeek Thinking UI | H | Chat Interfaces | 推理過程可視化的對話介面 |
| Qwen3 Thinking UI | H | Chat Interfaces | 推理過程可視化的對話介面 |

### 3.2 L2 Knowledge Codification（對應課程：L2 Antigravity Agentic Developer）

| 案例 / Case | 來源 | 原分類 | 應用情境 / 備註 |
| --- | --- | --- | --- |
| Academic Researcher | A | Agent Skills | 19 個可複用 Skill — **L2「Skill」概念最佳範本** |
| Code Reviewer | A | Agent Skills | 工程 Skill |
| Content Creator | A | Agent Skills | 行銷 / 內容 Skill |
| Data Analyst | A | Agent Skills | 資料 Skill |
| Debugger | A | Agent Skills | 工程 Skill |
| Decision Helper | A | Agent Skills | 決策輔助 Skill |
| Deep Research | A | Agent Skills | 研究 Skill |
| Editor | A | Agent Skills | 文字編修 Skill |
| Email Drafter | A | Agent Skills | 業務 / 客服 Skill |
| Fact Checker | A | Agent Skills | 查證 Skill |
| Fullstack Developer | A | Agent Skills | 工程 Skill |
| Meeting Notes | A | Agent Skills | 會議紀錄 Skill |
| Project Planner | A | Agent Skills | PM Skill |
| Python Expert | A | Agent Skills | 工程 Skill |
| Sprint Planner | A | Agent Skills | 敏捷 / PM Skill |
| Strategy Advisor | A | Agent Skills | 策略 Skill |
| Technical Writer | A | Agent Skills | 文件 Skill |
| UX Designer | A | Agent Skills | 設計 Skill |
| Visualization Expert | A | Agent Skills | 資料視覺化 Skill |
| Self-Improving Agent Skills | A | Agent Skills | 進階 — Skill 自我改善（L2→L4 邊界）|
| AI Data Analysis Agent | A | Starter | 單一用途封裝能力 |
| AI Music Generator Agent | A | Starter | 創意 Skill |
| Web Scraping AI Agent | A | Starter | 資料擷取 Skill |
| AI Medical Imaging Agent | A | Starter | 領域專業 Skill（醫療，須人工 Gate）|
| AI Travel Agent（Local & Cloud） | A | Starter | 規劃類 Skill |
| LaTeX OCR with Llama | H | OCR & Vision | 文件抽取 Skill |
| Llama OCR | H | OCR & Vision | 文件抽取 Skill |
| Gemma-3 OCR | H | OCR & Vision | 文件抽取 Skill |
| Qwen 2.5 VL OCR | H | OCR & Vision | 視覺文件抽取 Skill |

### 3.3 L3 Workflow Automation（對應課程：L3 n8n + AG/n8n Skill Pack）

| 案例 / Case | 來源 | 原分類 | 應用情境 / 備註 |
| --- | --- | --- | --- |
| Basic RAG Chain | A | RAG | RAG 入門 — L3 檢索管線基礎 |
| AI Blog Search（RAG） | A | RAG | 內容檢索 |
| RAG with Database Routing | A | RAG | 多資料源路由 |
| Hybrid Search RAG（Cloud） | A | RAG | 混合檢索 |
| Local Hybrid Search RAG | A | RAG | 地端混合檢索 |
| Llama 3.1 Local RAG | A | RAG | 地端 RAG（對應 Hybrid/全地端）|
| Deepseek Local RAG Agent | A | RAG | 地端 RAG |
| Local RAG Agent | A | RAG | 地端 RAG |
| RAG Agent with Cohere | A | RAG | 特定 provider RAG |
| Contextual AI RAG Agent | A | RAG | 情境式 RAG |
| Vision RAG | A | RAG | 多模態檢索 |
| RAG-as-a-Service | A | RAG | RAG 服務化 |
| Browser MCP Agent | A | MCP | 工具整合 — 瀏覽器 |
| GitHub MCP Agent | A | MCP | 工具整合 — GitHub |
| Notion MCP Agent | A | MCP | 工具整合 — Notion |
| Multi-MCP Agent Router | A | MCP | 多工具路由 |
| Llama3 Stateful Chat | A | Memory | 有狀態對話（L3→L4 邊界）|
| Simple RAG Workflow | H | RAG | RAG 入門 |
| Document Chat RAG | H | RAG | 文件問答管線 |
| Fastest RAG Stack | H | RAG | 高效 RAG 技術棧 |
| GitHub RAG | H | RAG | 程式碼庫檢索 |
| ModernBERT RAG | H | RAG | embedding 模型實作 |
| Llama 4 RAG | H | RAG | 新模型 RAG |
| Colbert RAG | H | RAG | late-interaction 檢索 |
| GroundX Document Pipeline | H | Infrastructure | 文件處理管線 |
| NotebookLM Clone | H | Infrastructure | 文件問答 / 摘要應用 |
| MindsDB MCP | H | Infrastructure | MCP — 資料庫整合 |
| Graphiti MCP | H | Infrastructure | MCP — 知識圖整合 |
| Pixeltable MCP | H | Infrastructure | MCP — 多模態資料整合 |

### 3.4 L4 Autonomous Agent（對應課程：L4 Hermes Agent）

| 案例 / Case | 來源 | 原分類 | 應用情境 / 備註 |
| --- | --- | --- | --- |
| AI Deep Research Agent | A | Advanced（Single） | 自主深度研究 — L4 核心案例 |
| AI Research Planner & Executor | A | Advanced（Single） | 規劃 + 執行 |
| AI Consultant Agent | A | Advanced（Single） | 顧問型 Agent |
| AI System Architect Agent | A | Advanced（Single） | 架構規劃 Agent |
| AI Movie Production Agent | A | Advanced（Single） | 創意製作 Agent |
| AI Investment Agent | A | Advanced（Single） | 投資分析（須人工 Gate）|
| Earnings Call Analyst Agent | A | Advanced（Single） | 財報分析 |
| AI Health & Fitness Agent | A | Advanced（Single） | 健康規劃（須人工 Gate）|
| AI Fraud Investigation Agent | A | Advanced（Single） | 詐欺調查（高風險，須人工 Gate）|
| AI Journalist Agent | A | Advanced（Single） | 新聞寫作 |
| AI Meeting Agent | A | Advanced（Single） | 會議準備與摘要 |
| Autonomous RAG | A | RAG | 自主檢索（RAG → L4）|
| Agentic RAG with Reasoning | A | RAG | 推理式自主 RAG |
| Agentic RAG with Embedding Gemma | A | RAG | 自主 RAG |
| Gemini Agentic RAG | A | RAG | 自主 RAG |
| Multimodal Agentic RAG | A | RAG | 多模態自主 RAG |
| Corrective RAG（CRAG） | A | RAG | 自我修正檢索 |
| Knowledge Graph RAG with Citations | A | RAG | 知識圖 + 引用（近 L4 知識型 Agent）|
| RAG Failure Diagnostics Clinic | A | RAG | RAG 失敗診斷（對應 L4 失敗模式學習）|
| AI ArXiv Agent with Memory | A | Memory | 有記憶的研究 Agent |
| AI Travel Agent with Memory | A | Memory | 有記憶的規劃 Agent |
| LLM App with Personalized Memory | A | Memory | 個人化記憶 |
| Multi-LLM App with Shared Memory | A | Memory | 共享記憶（L4→L5 邊界）|
| Local ChatGPT Clone with Memory | A | Memory | 地端 + 記憶 |
| xAI Finance Agent | A | Starter | 財務 Agent |
| OpenAI Research Agent | A | Starter | 研究 Agent |
| AutoGen Stock Analyst | H | Agents | 股票分析 Agent |
| YouTube Trend Analysis | H | Agents | 趨勢分析 Agent |
| Brand Monitoring | H | Agents | 品牌監控 Agent |
| Hotel Booking Agent | H | Agents | 訂房 Agent |
| Paralegal Agent | H | Agents | 法務助理 Agent（須人工 Gate）|
| Financial Analyst Agent | H | Agents | 財務分析 Agent |
| Book Writer Flow | H | Agents | 長文寫作 Agent flow |
| Corrective RAG | H | RAG | 自我修正檢索 |
| Trustworthy RAG | H | RAG | 可信度檢索（對應 Evidence 紀律）|

### 3.5 L5 Multi-Agent Organization（對應課程：L5 ClawTeam）

| 案例 / Case | 來源 | 原分類 | 應用情境 / 備註 |
| --- | --- | --- | --- |
| AI Competitor Intelligence Agent Team | A | Multi-agent Teams | 競爭情報團隊 |
| AI Finance Agent Team | A | Multi-agent Teams | 財務分析團隊 |
| AI Game Design Agent Team | A | Multi-agent Teams | 遊戲設計團隊 |
| AG2 Adaptive Research Team | A | Multi-agent Teams | 適應性研究團隊 |
| AI Legal Agent Team（Cloud & Local） | A | Multi-agent Teams | 法務團隊（高敏感，地端選項）|
| AI Recruitment Agent Team | A | Multi-agent Teams | 招募團隊 |
| AI Real Estate Agent Team | A | Multi-agent Teams | 不動產團隊 |
| AI Services Agency（CrewAI） | A | Multi-agent Teams | 服務代理團隊 |
| AI Teaching Agent Team | A | Multi-agent Teams | 教學團隊 |
| Multimodal Coding Agent Team | A | Multi-agent Teams | 多模態開發團隊 |
| Multimodal Design Agent Team | A | Multi-agent Teams | 多模態設計團隊 |
| Multimodal UI/UX Feedback Agent Team | A | Multi-agent Teams | UI/UX 回饋團隊 |
| AI Travel Planner Agent Team | A | Multi-agent Teams | 旅遊規劃團隊 |
| AI VC Due Diligence Agent Team | A | Advanced（Multi） | 創投盡職調查團隊 |
| AI Sales Intelligence Agent Team | A | Advanced（Multi） | 銷售情報團隊 |
| Trust-Gated Multi-Agent Research Team | A | Advanced（Multi） | 信任閘控研究團隊（對應 L5 Human Gate）|
| AI Product Launch Intelligence Agent | A | Advanced（Multi） | 產品上市情報（對應製造/零售案例）|
| AI Financial Coach Agent | A | Advanced（Multi） | 財務教練多 Agent |
| AI Home Renovation Agent | A | Advanced（Multi） | 多 Agent 裝修規劃 |
| DevPulse AI | A | Advanced（Multi） | 多 Agent 訊號情報 |
| AI Self-Evolving Agent | A | Advanced（Multi） | 自我演化（進階）|
| AI News and Podcast Agents | A | Advanced（Multi） | 新聞 + Podcast 多 Agent |
| AI Mental Wellbeing Agent | A | Advanced（Multi） | 身心健康多 Agent（須人工 Gate）|
| Mixture of Agents | A | Starter | 多 Agent 混合 |
| Insurance Claim Live Agent Team | A | Voice | 保險理賠語音團隊 |
| Multi-Agent Deep Researcher | H | Infrastructure | 多 Agent 深度研究團隊 |

### 3.6 跨課程 / 技術支援 / 不對應（Cross-Cutting / Not Course-Mapped）

| 案例 / Case | 來源 | 原分類 | 應用情境 / 備註 |
| --- | --- | --- | --- |
| AI Audio Tour Agent | A | Voice | 語音擴充，可疊在 L3/L4 |
| Customer Support Voice Agent | A | Voice | 客服語音，可疊在 L3/L4 |
| Voice RAG Agent（OpenAI SDK） | A | Voice | 語音 + RAG，疊在 L3 |
| OpenSource Voice Dictation Agent | A | Voice（外部連結）| 語音聽寫工具 |
| Real-time Voice Bot | H | Voice & Audio | 即時語音，可疊在 L3/L4 |
| RAG Voice Agent | H | Voice & Audio | 語音 + RAG |
| Chat with Audios | H | Voice & Audio | 音訊內容問答 |
| Multilingual Meeting Notes Generator | H | Voice & Audio | 多語會議紀錄（可對應 L2 Skill）|
| Toonify Token Optimization | A | Optimization | 跨課程技術支援 — API 成本優化 |
| Headroom Context Optimization | A | Optimization | 跨課程技術支援 — context 縮減 |
| Gemma 3 Fine-tuning | A | Fine-tuning | 進階技術 — 模型客製（對應全地端）|
| Llama 3.2 Fine-tuning | A | Fine-tuning | 進階技術 — 模型客製 |
| DeepSeek Fine-tuning | H | Fine-tuning | 進階技術 — 模型客製 |
| Build Reasoning Model | H | Fine-tuning | 進階技術 — 推理模型訓練 |
| Attention Is All You Need Implementation | H | Fine-tuning | 教學 — Transformer 原理實作 |
| Google ADK Crash Course | A | Framework 課程 | 跨課程 — 框架學習（L4/L5 進階）|
| OpenAI Agents SDK Crash Course | A | Framework 課程 | 跨課程 — 框架學習（L4/L5 進階）|
| Llama 4 vs DeepSeek-R1 | H | Model Comparisons | 跨課程 — 模型選型參考 |
| Qwen3 vs DeepSeek-R1 | H | Model Comparisons | 跨課程 — 模型選型參考 |
| O3 vs Claude Code | H | Model Comparisons | 跨課程 — 工具選型參考 |
| AI 3D Pygame Agent | A | Game-Playing | 不對應企業課程 — 學習 / 展示用 |
| AI Chess Agent | A | Game-Playing | 不對應企業課程 — 學習 / 展示用 |
| AI Tic-Tac-Toe Agent | A | Game-Playing | 不對應企業課程 — 學習 / 展示用 |
| Openwork（Open Browser Automation） | A | Multi-agent（外部連結）| 外部專案，瀏覽器自動化 |

> ai-engineering-hub 共 93+ 專案，分初/中/進階三級；本表收錄其代表性、有明確名稱的專案，未來可持續補入。

---

## 4. 依企業流程 / 部門快速查詢 / Quick Lookup by Enterprise Function

> 同樣的案例，換個軸來查 —— 依**企業部門 / 流程**分組，讓不同部門的人快速看「跟我有關的有哪些」。
> 每列標 L 級（成熟度）與來源（A = awesome-llm-apps、H = ai-engineering-hub）。部門分類為本方法論判斷，部分案例跨多個部門。
> 部門不限於下列 —— 顧問可依客戶實際組織增列。

### 4.1 工程 / IT（Engineering / IT）

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| Code Reviewer / Debugger / Python Expert / Fullstack Developer / Technical Writer | L2 | A |
| AI System Architect Agent | L4 | A |
| Multimodal Coding Agent Team | L5 | A |
| GitHub MCP Agent / Browser MCP Agent | L3 | A |
| Chat with GitHub | L1 | A |
| GitHub RAG / ModernBERT RAG | L3 | H |
| Google ADK / OpenAI Agents SDK Crash Course | 跨課程 | A |
| Build Reasoning Model / Attention Is All You Need 實作 | 跨課程 | H |

### 4.2 財務 / Finance

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| xAI Finance Agent | L4 | A |
| AI Investment Agent / Earnings Call Analyst Agent | L4 | A |
| Financial Analyst Agent / AutoGen Stock Analyst | L4 | H |
| AI Finance Agent Team | L5 | A |
| AI Financial Coach Agent | L5 | A |
| AI VC Due Diligence Agent Team | L5 | A |

### 4.3 人事 / HR

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| AI Recruitment Agent Team（含履歷篩選） | L5 | A |
| Meeting Notes（面談紀錄）| L2 | A |
| Email Drafter（HR 通知信）| L2 | A |
| LLM App with Personalized Memory（新人 onboarding 知識）| L4 | A |

### 4.4 業務 / Sales

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| Email Drafter（業務信草稿）| L2 | A |
| AI Sales Intelligence Agent Team | L5 | A |
| AI Competitor Intelligence Agent Team | L5 | A |
| AI Product Launch Intelligence Agent | L5 | A |
| Brand Monitoring | L4 | H |
| AI Real Estate Agent Team | L5 | A |

### 4.5 行銷 / Marketing

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| Content Creator | L2 | A |
| AI Music Generator / AI Meme Generator | L1-L2 | A |
| AI Blog to Podcast Agent | L1 | A |
| AI News and Podcast Agents | L5 | A |
| AI Movie Production Agent | L4 | A |
| YouTube Trend Analysis | L4 | H |
| Multimodal Design Agent Team / UI/UX Feedback Agent Team | L5 | A |

### 4.6 研發 / R&D

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| Academic Researcher / Deep Research | L2 | A |
| Chat with Research Papers / ArXiv | L1 | A |
| AI Deep Research Agent / AI Research Planner & Executor / OpenAI Research Agent | L4 | A |
| AI ArXiv Agent with Memory | L4 | A |
| AG2 Adaptive Research Team / Trust-Gated Multi-Agent Research Team | L5 | A |
| Multi-Agent Deep Researcher | L5 | H |

### 4.7 營運 / Operations

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| Project Planner / Sprint Planner | L2 | A |
| AI Meeting Agent / Meeting Notes | L2-L4 | A |
| Multilingual Meeting Notes Generator | 跨課程 | H |
| GroundX Document Pipeline / NotebookLM Clone | L3 | H |
| DevPulse AI（訊號情報）| L5 | A |
| AI Services Agency（CrewAI）| L5 | A |
| Hotel Booking Agent | L4 | H |

### 4.8 客服 / Customer Service

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| Customer Support Voice Agent | 語音擴充 | A |
| Real-time Voice Bot / RAG Voice Agent | 語音擴充 | H |
| Insurance Claim Live Agent Team | L5 | A |
| 各類 RAG（FAQ / 知識庫問答）| L3-L4 | A / H |
| Chat with PDF / Substack（內部知識問答）| L1 | A |

### 4.9 法務 / 法遵 / Legal & Compliance

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| AI Legal Agent Team（Cloud & Local）| L5 | A |
| Paralegal Agent | L4 | H |
| AI Fraud Investigation Agent | L4 | A |
| Fact Checker | L2 | A |
| Trustworthy RAG（可信度檢索）| L4 | H |

### 4.10 資料 / 分析 / Data & Analytics

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| Data Analyst / AI Data Analysis Agent / Visualization Expert | L2 | A |
| 各類 RAG（檢索管線）| L3 | A / H |
| Knowledge Graph RAG with Citations | L4 | A |
| Model Comparisons（選型參考）| 跨課程 | H |
| OCR 系列（LaTeX / Llama / Gemma-3 / Qwen VL OCR）| L2 | H |

### 4.11 設計 / 創意 / Design & Creative

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| UX Designer | L2 | A |
| Multimodal Design Agent Team / UI/UX Feedback Agent Team | L5 | A |
| AI Game Design Agent Team | L5 | A |

### 4.12 跨部門 / 管理層 / Cross-Functional & Management

| 案例 | L 級 | 來源 |
| --- | --- | --- |
| Strategy Advisor / Decision Helper | L2 | A |
| AI Consultant Agent | L4 | A |
| Editor | L2 | A |
| LLM Apps with Memory（組織知識記憶）| L4 | A |
| Toonify / Headroom（成本 / context 優化）| 跨課程 | A |

> **非企業部門類**（消費者 / 個人應用情境，列出供參考但非企業導入主軸）：AI Travel Agent、AI Health & Fitness Agent、AI Mental Wellbeing Agent、AI Home Renovation Agent、AI Breakup Recovery Agent、Game-Playing Agents。

---

## 5. 統計摘要 / Summary

| 對應層級 | 案例數（約）| 對應課程 |
| --- | ---: | --- |
| L1 Controlled AI Access | 12 | L1 OpenWebUI 企業啟用 |
| L2 Knowledge Codification | 29 | L2 Antigravity Agentic Developer |
| L3 Workflow Automation | 29 | L3 n8n + AG/n8n Skill Pack |
| L4 Autonomous Agent | 34 | L4 Hermes Agent |
| L5 Multi-Agent Organization | 26 | L5 ClawTeam |
| 跨課程 / 不對應 | 24 | 技術支援 / 展示 |
| **合計（2 來源）** | **約 150+** | — |

> **觀察**：案例分布在 L2、L3、L4 最密集 — 反映業界目前 LLM 應用重心在「封裝能力 → 系統整合 → 自主 Agent」。L5 多 Agent 團隊案例也已成形。RAG 是 L3-L4 的最大宗。

---

## 6. 怎麼把這份索引用進顧問流程 / How to Use in the Consulting Flow

| 顧問場景 | 用法 |
| --- | --- |
| **Discovery 階段** | 給客戶看對應其 L 級的案例表，問「哪些你有感？」— 快速找出 PoC 候選 |
| **L1-L5 課程設計** | 每一級課程可從對應的案例表挑 3-5 個當示範 / 練習題 |
| **跨級期待管理** | 客戶若指著 L5 案例說「我要這個」，用索引指出「你現在 L2，這個要先補 L3-L4」 |
| **PoC 場景庫補充** | 案例可轉化為 `../02_Course_Design/POC_SCENARIO_SPECS.md` 的 PoC 草稿 |
| **模型 / 工具選型** | §3.6 的 Model Comparisons 可作為部署模式與 provider 選型參考 |

> ⚠️ 注意：這些 app 多為**展示 / 起始模板 / 教學專案**，企業導入時仍須套用本方法論的治理（人工 Gate、Evidence、Stage Gate、資安檢核）。索引中標「須人工 Gate」者為高風險領域。

---

## 7. 引用與授權 / Citation & License

本索引表之**對應關係（L1-L5、課程對應、應用情境註記）為本方法論原創**；**案例清單與分類**參考自兩個來源：

- `Shubhamsaboo/awesome-llm-apps`（Apache-2.0）— 見 [`../90_References/AWESOME_LLM_APPS_REFERENCE.md`](../90_References/AWESOME_LLM_APPS_REFERENCE.md)
- `patchy631/ai-engineering-hub`（MIT）— 見 [`../90_References/AI_ENGINEERING_HUB_REFERENCE.md`](../90_References/AI_ENGINEERING_HUB_REFERENCE.md)

本方法論**未重製任何 app 的原始碼**，僅引用案例名稱與分類作為索引。學員若要實作某案例，請自行從對應上游 repo 取得並遵守其授權。

The L1-L5 / course mappings in this index are this methodology's original work; the case lists and categories are referenced from two sources (awesome-llm-apps, Apache-2.0; ai-engineering-hub, MIT). No app source code is reproduced. Full citations: the two `*_REFERENCE.md` files above.
