# L1 OpenWebUI 企業啟用課程規劃

版本：v1.0  
作者：Morris  
適用層級：L1 Controlled AI Access  
參考影片清單：DigitalBrainBase OpenWebUI playlist  
`https://www.youtube.com/watch?v=oXJ4L1G8kaI&list=PL_rTgQnnMXsXAsEiid-tWhaj03SsP4U5Z`

---

## 1. L1 重新定位

L1 不是教員工「如何用 AI 聊天」而已。企業真正需要的是一個受控的 AI 入口：

> 每位員工可以用自己的帳號登入 OpenWebUI，擁有自己的聊天區域、歷史紀錄與個人設定；管理者可以管理帳號、角色、群組、模型、權限、功能與資料使用邊界。

所以 L1 課程要同時服務兩種人：

| 對象 | 需要學會什麼 |
|---|---|
| 一般使用者 | 登入、選模型、開新聊天、管理自己的聊天、上傳允許資料、使用 Prompt 完成工作 |
| Admin / IT / HR | 建立或審核帳號、設定角色、群組、預設權限、模型可見性、文件上傳、Web Search、API Key、分享與資料規範 |

L1 的完成標準不是「大家都會問問題」，而是「公司可以安全、可管理、可擴充地讓員工開始使用 AI」。

---

## 2. 企業必備能力

| 能力 | 企業要求 | 驗收方式 |
|---|---|---|
| 帳號登入 | 每位員工用自己的帳號登入，不共用帳號 | 測試帳號清單、登入截圖 |
| 個人聊天區域 | 每位使用者有自己的聊天歷史、資料夾、個人 Prompt 與設定 | 使用者個別操作展示 |
| 角色管理 | 至少分 Admin、User、Pending；新帳號需審核或受控開通 | Admin Panel 設定截圖 |
| 群組管理 | 依部門或種子團隊建立群組 | Groups 設定表 |
| 權限控管 | 控制文件上傳、Web Search、Image、Tools、API Keys、分享、刪除、匯出 | Permissions 檢查表 |
| 模型控管 | 不同群組可使用不同模型或模型預設 | Model access 表 |
| 資料邊界 | 定義可輸入、不可輸入、需人工確認資料 | AI 使用規範 |
| 使用紀錄與治理 | 管理者知道如何檢查設定、公告規範、處理帳號與權限問題 | L1 Admin Runbook |

備註：OpenWebUI 官方文件說明其 RBAC 以 Roles、Permissions、Groups 三層組成，且權限採 additive model；因此企業應採最小權限原則，先收斂 Global Defaults，再透過 Groups 開放進階功能。

官方文件參考：

- Roles：`https://docs.openwebui.com/features/rbac/roles/`
- Permissions：`https://docs.openwebui.com/features/rbac/permissions/`
- Groups：`https://docs.openwebui.com/features/rbac/groups/`

---

## 3. 課程目標

完成 L1 課程後，客戶應能：

1. 說明 OpenWebUI 在企業 AI 成熟度 L1 的角色。
2. 完成 OpenWebUI 登入與基本聊天操作。
3. 建立個人聊天區域：新聊天、歷史、資料夾、Prompt、檔案。
4. 使用 Prompt 完成 Email、會議紀錄、摘要、報告草稿等高頻工作。
5. 使用文件上傳或 Knowledge 完成低敏感文件問答。
6. 理解模型選擇、參數、幻覺與人工確認。
7. Admin 能管理帳號、角色、群組、權限、模型與功能。
8. IT / HR 能建立 AI 使用規範、資料分級與 Gate 1 驗收表。
9. 產出 L2 Skill 候選清單。

---

## 4. 課前條件

| 項目 | 最低要求 |
|---|---|
| OpenWebUI 環境 | 已有測試環境或課堂 demo 環境 |
| 帳號 | 每位學員有自己的測試帳號；Admin 有管理帳號 |
| 模型 | 至少 1 個可用模型；可選本地 Ollama 或 API 模型 |
| 測試資料 | 低敏感文件、會議紀錄、Email、FAQ、SOP |
| 權限草案 | 是否允許文件上傳、Web Search、分享、API Key、工具使用 |
| 公司規範 | 若無既有 AI 政策，課堂建立第一版 |

---

## 5. L1 OpenWebUI IPOE

| 類別 | 定義 |
|---|---|
| Input | 使用者帳號、部門低敏感資料、Prompt、文件、模型、群組、權限設定、AI 使用規範 |
| Process | 登入、開新聊天、模型選擇、Prompt 實作、文件問答、聊天整理、Admin 帳號審核、角色/群組/權限設定、資料案例判斷 |
| Output | 個人聊天紀錄、Prompt Library、低敏感文件摘要、AI 使用規範、帳號/群組/權限表、高頻工作清單、L2 Skill 候選 |
| Evidence | 登入截圖、個人聊天截圖、Admin Panel 截圖、Groups/Permissions 設定、Prompt 作業、資料案例判斷表、Gate 1 驗收紀錄 |

---

## 6. 完整課程版本

### 6.1 L1 全員使用課：3 小時

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 20 分 | L1 定位 | 為什麼企業需要統一 AI 入口 | L1 共識 |
| 30 分 | 登入與個人聊天區 | 自己帳號登入、新聊天、歷史、資料夾、個人設定 | 登入與聊天截圖 |
| 30 分 | 模型與聊天操作 | 選模型、重生回答、續寫、匯出、整理聊天 | 操作練習 |
| 45 分 | Prompt 基礎 | 角色、任務、背景、限制、輸出格式 | 個人 Prompt |
| 45 分 | 日常工作實作 | Email、摘要、會議紀錄、主管報告 | 課堂輸出 |
| 30 分 | 資料邊界 | 可輸入 / 不可輸入 / 需人工確認 | 資料案例判斷 |

### 6.2 L1 Admin / IT 管理課：3 小時

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 30 分 | Admin Panel 總覽 | 使用者、模型、連線、功能、文件、公告 | Admin 操作清單 |
| 45 分 | 帳號與登入管理 | Admin / User / Pending、審核流程、預設角色 | 帳號管理表 |
| 45 分 | 群組與權限 | Default Permissions、Groups、部門權限、最小權限 | 權限矩陣 |
| 45 分 | 模型與功能控管 | 模型可見性、Web Search、File Upload、API Keys、Tools | 模型/功能表 |
| 30 分 | 個人區域與分享政策 | 個人聊天、聊天分享、公開資源、匯出規範 | 分享政策 |
| 45 分 | Gate 1 驗收 | 環境、帳號、權限、資料規範、Prompt Library | Gate 1 表 |

### 6.3 L1 企業導入工作坊：1 天

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| AM 1 | 使用者訓練 | 登入、聊天、模型、Prompt、文件 | 個人作業 |
| AM 2 | 部門情境 | Email、會議、摘要、報告、FAQ | 部門 Prompt |
| PM 1 | Admin 設定 | 帳號、角色、群組、權限、模型 | Admin Runbook |
| PM 2 | 治理與銜接 L2 | 資料規範、高頻工作、Skill 候選 | L2 候選清單 |

---

## 7. Admin 控制表

| 控制項 | 建議設定 | Evidence |
|---|---|---|
| 第一位 Admin | 指派 IT 或 AI 管理窗口 | Admin 名單 |
| 使用者開通 | 新使用者預設 Pending 或受控 User | Default role 設定 |
| 個人帳號 | 禁止共用帳號，每人獨立登入 | 帳號清單 |
| 個人聊天區 | 每人各自建立聊天與資料夾 | 使用者截圖 |
| Groups | 依部門、種子團隊、Power Users 建群組 | Groups 表 |
| Default Permissions | 採最小權限，進階功能透過 Groups 開放 | Permission 截圖 |
| File Upload | 先允許低敏感資料；高敏感資料禁止 | 資料分級規範 |
| Web Search | 依部門需求開放，要求引用來源 | 權限表 |
| API Keys | 預設關閉或只給 IT / Power Users | API Key policy |
| Share / Public | 預設限制公開分享 | 分享政策 |
| Models | 依群組開放本地模型或 API 模型 | Model access 表 |
| Announcements | 放置 AI 使用規範與資料提醒 | Banner 截圖 |

---

## 8. 使用者操作標準

每位學員在 L1 結束時必須能完成：

1. 用自己的帳號登入。
2. 建立至少 2 個聊天主題。
3. 將聊天整理到資料夾或命名清楚。
4. 建立 3 個個人常用 Prompt。
5. 用低敏感文件完成摘要或問答。
6. 判斷 10 個資料案例是否可輸入 AI。
7. 知道什麼情況要人工確認，不能直接採用 AI 回答。

---

## 9. 影片參考地圖

| # | 影片標題 | 課程用途 | 建議 |
|---:|---|---|---|
| 1 | Open WebUI: The Free, Private ChatGPT Alternative | L1 開場、價值定位 | 必看 |
| 2 | How to Install OpenWebUI | IT 安裝、環境準備 | IT 必看 |
| 3 | Local AI Model Requirements | 本地模型硬體需求 | IT 必看 |
| 4 | Exploring the OpenWebUI Admin Panel | Admin Panel、企業管理 | Admin 必看 |
| 5 | Exploring Open WebUI: Features, Models, & Tools | 功能總覽、模型與工具概念 | 必看 |
| 6 | Chat with Your Own Documents | 文件上傳、文件問答 | 必看 |
| 7 | Add Real-Time Web Search | Web Search 設定與使用 | 選修 / 權限討論 |
| 8 | Add GPT-4 to Open WebUI | OpenAI API provider 設定 | IT / Admin |
| 9 | Community Tools | 社群工具導入 | 選修，需安全審查 |
| 10 | Text-to-Speech with ElevenLabs | TTS | 選修 |
| 11 | Create Custom AI Models | 模型預設、角色化模型 | Admin / L2 前置 |
| 12 | Generate AI Images with DALL-E 3 | 圖像生成 | 選修 |
| 13 | LLAVA Multimodal / GPT-4 Image Analysis | 多模態圖片分析 | 選修 |
| 14 | AI Clone | 個人化示範 | 靈感，不列核心 |
| 15 | Functions to Build Websites & Apps | Functions 應用 | L2 / L3 預告 |
| 16 | Reduce Hallucinations with Advanced Parameters | 幻覺、參數、人工確認 | 必看 |
| 17 | Choosing the Right Ollama Model | 本地模型選擇 | IT / Admin |
| 18 | Mobile Access with Ngrok | 行動存取、遠端風險 | 選修，需資安審查 |
| 19 | Choosing the Best Language Model | 模型選擇方法 | Admin / 種子人員 |
| 20 | Vision LLMs for Local Inference | 視覺模型評估 | 選修 |
| 21 | AI Recruiter Meets AI Clone | 招募示範 | HR 靈感 |
| 22 | Groq Cloud & OpenWebUI | 雲端模型 provider | IT / Admin |
| 23 | Docker & Watchtower | 維運更新 | IT 必看 |
| 24 | OpenWebUI Pipelines | Pipelines | L3 預告 |
| 25 | User Roles in Open Web UI | 使用者角色與安全協作 | Admin 必看 |
| 26 | Writing Better Prompts | Prompt 基礎 | 全員必看 |
| 27 | Arena Model | 模型測試與比較 | Admin / 評估 |
| 28 | Run Text-to-Speech Locally | 本地 TTS | 選修 |
| 29 | OpenWebUI Memory Explained | Memory / 個人化記憶 | 選修，需隱私討論 |
| 30 | Quantization | 量化與效能 | IT 選修 |
| 31 | AI-Powered Recruiter Bot | 招募 Bot | HR / L2 案例 |
| 32 | Open WebUI v0.4 Updates | 版本更新概念 | IT / Admin |
| 33 | Anthropic Claude Models | Claude provider 設定 | IT / Admin |
| 34 | Public Access to Chatbots | 公開分享 Chatbot | 選修，企業需嚴格控管 |
| 35 | Tools, Functions & Pipelines Deep Dive | 進階擴充 | L2 / L3 預告 |
| 36 | Online? Offline? Both? | 雲端 / 本地 / Hybrid 討論 | 必看 |

---

## 10. L1 Deliverables

| Deliverable | 說明 | 驗收方式 |
|---|---|---|
| OpenWebUI 使用者操作手冊 | 登入、聊天、模型、文件、Prompt、資料邊界 | 使用者能照手冊完成操作 |
| Admin Runbook | 帳號、角色、群組、權限、模型、功能開關 | Admin 能獨立操作 |
| 帳號 / 群組 / 權限表 | 每人帳號、部門群組、功能權限 | IT / HR 簽核 |
| AI 使用規範 | 可輸入、不可輸入、需人工確認 | 管理層確認 |
| Prompt Library v1 | 個人與部門常用 Prompt | 課堂作業 |
| 高頻工作清單 | 可進 L2 Skill 化的工作 | 部門主管確認 |
| Gate 1 驗收表 | 環境、帳號、權限、資料規範、作業 | Pass / Fail |

---

## 11. Gate 1：能否進入 L2

| Gate | 檢查問題 | 必備 Evidence | 判定 |
|---|---|---|---|
| Gate 1A：入口可用 | OpenWebUI 是否可登入、可選模型、可聊天？ | 登入與聊天截圖 | Pass / Fail |
| Gate 1B：帳號可管 | 是否每位學員有自己帳號，Admin 能審核與管理？ | 帳號表、Admin Panel 截圖 | Pass / Fail |
| Gate 1C：個人區域可用 | 使用者是否能建立自己的聊天、歷史、資料夾？ | 使用者操作截圖 | Pass / Fail |
| Gate 1D：權限可控 | 角色、群組、功能、模型、分享是否有設定？ | RBAC / Permission 表 | Pass / Fail |
| Gate 1E：資料規範可用 | 是否有可輸入 / 禁止輸入 / 人工確認規則？ | AI 使用規範 | Pass / Fail |
| Gate 1F：L2 候選清楚 | 是否整理出高頻工作與 Skill 候選？ | 高頻工作清單 | Pass / Fail |

未通過 Gate 1B-1D 時，不建議大規模開放員工使用。未通過 Gate 1E 時，不建議導入文件上傳、Web Search、Tools、Memory 等進階功能。
