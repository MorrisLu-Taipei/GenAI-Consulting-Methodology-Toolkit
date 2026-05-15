# AI 轉型成熟度顧問方案：故事、目錄與章節規劃

更新日期：2026-05-13

## 1. 方案定位

這套方案不是單純賣 AI 課程，也不是單純賣工具導入。

真正的定位是：

> 幫企業把零散的 AI 使用，轉成可複製、可治理、可衡量、可擴大的組織能力。

企業通常已經開始使用 ChatGPT、Claude、Gemini 或其他 AI 工具，但多數仍停在個人自行嘗試。員工覺得好用，主管卻看不到組織效益；有人做出成果，卻無法複製給團隊；流程仍在人工搬資料、複製貼上、寄信、填表、更新系統。

我們的策略是用一條清楚的顧問路徑把企業帶起來：

1. 用簡易問卷診斷企業目前 AI 成熟度。
2. 依診斷結果配置 L1-L5 課程比例。
3. 課後透過八階段顧問方法論，產出 AI 轉型診斷報告。
4. 報告中提出可執行的 Skill、Workflow、Agent、Agent Team Roadmap。

## 2. 客戶看得懂的情境故事

### 2.1 故事主角

假設客戶是一家 300 人的製造或服務型企業。

公司有業務、客服、營運、財務、IT、人資與管理部門。每個部門都開始聽到 AI，但使用狀態很不一致：

- 業務同仁用 ChatGPT 寫拜訪信與簡報。
- 客服主管想整理 FAQ，但資料散落在 Gmail、CRM、Notion 和 Excel。
- 營運主管想知道每天異常訂單，但 ERP 匯出的資料需要人工整理。
- 老闆想推 AI，但只聽到零散案例，無法判斷公司到底走到哪裡。
- IT 擔心資安、權限、資料外流與系統串接維護成本。

這時候如果直接賣工具，客戶容易聽不懂價值；如果只上課，課後也很容易回到原本流程。

所以我們要講的是一個轉型故事：

> 先知道公司現在在哪裡，再補足員工與部門能力，最後把真正有價值的場景整理成可落地的 AI 轉型路線圖。

### 2.2 Before：企業導入 AI 前的典型狀態

企業一開始通常不是「完全沒有 AI」，而是「AI 已經散落在各處」。

常見狀態：

- 有人很會用 AI，但方法留在個人電腦或聊天紀錄裡。
- 部門內沒有共同 Prompt、SOP、模板與知識庫。
- 客戶資料在 CRM，任務在 Notion，表格在 Google Sheets，信件在 Gmail，訂單在 ERP，資料彼此不連通。
- 管理層問 AI 的 ROI，現場只能回答「好像有變快」。
- IT 沒有辦法判斷哪些場景可以自動化，哪些場景應該先治理。

這代表企業並不是缺一個 AI 工具，而是缺一張「成熟度地圖」與一套「轉型方法」。

### 2.3 Future：上課前先讓客戶看見的未來

客戶通常不是因為想學工具才買課，客戶是因為想看見公司未來可以變成什麼樣子。L1-L5 課程開場不能只講 OpenWebUI、Antigravity、n8n、Hermes Agent、ClawTeam，而要先講一個上完課後的工作日。

想像三個月後，這家公司星期一早上的運作方式已經改變：

1. 業務同仁打開 OpenWebUI，用自己的帳號進入個人聊天區。AI 已經知道公司允許哪些資料、禁止哪些資料，也知道部門常用的輸出格式。業務不再從空白頁開始寫信，而是用公司核准的 Prompt 產出客戶拜訪信、會議摘要與提案初稿。
2. 行銷主管把過去只有自己會寫的產品文案方法，整理成 Skill。新人只要輸入產品資料、客群、語氣與通路，就能產出符合部門風格的初稿。主管審的是品質，不再每次重教流程。
3. 客服主管收到客訴信時，n8n 自動從 Gmail 讀取內容，查 CRM 的客戶等級與歷史紀錄，更新 Google Sheets 狀態，建立 Notion 追蹤任務，再產生主管摘要。人仍然做判斷，但不再人工搬資料。
4. 營運主管每天早上收到 Hermes Agent briefing。Agent 已讀取 ERP 異常訂單、客服紀錄、前一天會議紀錄與 Wiki 知識，整理出三個需要追蹤的問題，並標示哪些步驟需要 HITL（Human-in-the-Loop，人類在迴圈內審核）才能繼續。
5. 管理層要規劃新產品上市時，ClawTeam 編組市場 Agent、產品 Agent、客服 Agent、財務 Agent 與營運 Agent。每個 Agent 有角色、任務與交付物，最後產出一份可追溯來源與責任的整合報告。

這個未來想像要放在課程開始前，因為它能把 L1-L5 從工具清單變成客戶聽得懂的能力演進：

| 等級 | 軸 | 上完課後具備的能力 | 客戶能想像的情境 |
| --- | --- | --- | --- |
| L1 | 規模軸·個人 | 每位員工能在受控入口安全使用 AI | 員工有自己的 AI 工作區，不再共用帳號或任意丟資料 |
| L2 | 規模軸·部門 | 高手方法以部門職責為單位被整理成可複用 Skill | 新人也能沿用部門標準方法產出穩定成果 |
| L3 | 規模軸·跨部門 / 全公司 | AI 能串接跨部門 Skill 與系統並執行流程 | email、Sheets、Notes、CRM、API、ERP 開始連成全公司工作流 |
| L4 | AI 自主軸·超級助理 | 全自動 AI Agent 能用記憶、工具、Workflow 與自動排程 | 每天自動產生 briefing、追蹤清單、證據與待 HITL 人類審核事項 |
| L5 | AI 自主軸·AI 團隊 | 多個專業 Agent 形成職能分工團隊 | 新產品、品質、醫療服務或客戶經營可由 AI 團隊協作前置分析 |

因此，課程銷售時要先講未來情境，再講 L1-L5；先講客戶會得到的工作能力，再講工具；先講可驗證交付物，再講技術細節。

### 2.4 Transformation：我們帶客戶走的三段旅程

#### 第一段：問卷診斷

先用簡易問卷快速掌握企業目前在哪一級：

- L1：員工各自使用 Chat AI。
- L2：部門開始沉澱 Skill、SOP、Prompt、範本。
- L3：開始用 n8n 串接系統與流程。
- L4：開始使用具備 Wiki 記憶、工具呼叫、排程、證據與 HITL 人類審核的 Hermes Agent。
- L5：多個 Agent 形成團隊，協同完成企業級流程。

問卷的目的不是做學術評量，而是讓老闆、主管與 IT 對現況有共同語言。

#### 第二段：課程能力建置

課程不是固定菜單，而是依診斷結果配置比例。

例如：

- 客戶目前幾乎都在 L1，則課程要多放在 OpenWebUI、AI 使用規範、Prompt、資料安全與部門 Skill 化。
- 客戶已有部門模板與 SOP，則課程要往 n8n Workflow 與系統串接前進。
- 客戶已經有自動化基礎，則可加入 Hermes Agent 的知識工作閉環，再進一步評估 ClawTeam 的 Agentic AI 團隊課程。

課程的目標不是只教會工具操作，而是讓客戶在課程中產出自己的工作資產：

- Prompt Library
- Skill 清單
- SOP 與模板
- Workflow PoC
- Hermes Agent 任務範例
- AI Team 協作情境

課程設計還必須參考每一級的需求清單與公司屬性。也就是說，L1-L5 不是固定教案，而是成熟度架構；實際教什麼、用什麼案例、做到多深，要看客戶的產業、資料敏感度、IT 能力、既有系統與部署模式。

例如同樣是 L3 n8n：

- 行銷服務業可能優先串 Gmail、Sheets、Notion、CRM，快速做客戶提案與活動報告。
- 研發製造業可能優先串 ERP、內部 API、資料庫、品質文件與異常訂單流程。
- 高敏感資料企業可能先做 Hybrid 或全地端，並加上人工審核、權限控管與稽核紀錄。

#### 第三段：顧問診斷報告

課後不是結束，而是進入顧問診斷。

我們用八階段方法論整理：

1. 企業現況。
2. AI 成熟度等級。
3. 流程與資料缺口。
4. 高價值場景。
5. 優先導入順序。
6. 三階段 Roadmap。
7. ROI 與治理建議。
8. 後續導入計畫。

最後交付一份管理層看得懂、部門主管能認同、IT 能評估、團隊能執行的 AI 轉型診斷報告。

### 2.5 After：客戶應該感受到的改變

完成第一輪服務後，客戶應該能回答以下問題：

- 我們公司目前 AI 成熟度在哪一級？
- 哪些部門已經具備 AI 化基礎？
- 哪些流程最適合先自動化？
- 哪些資料與系統需要串接？
- 下一季應該先做 L2 Skill、L3 Workflow、L4 Agent，還是 L5 Agent Team？
- 推動 AI 後，要用哪些 KPI 追蹤成效？

這就是從「大家各自試 AI」走到「公司有 AI 轉型路線圖」。

## 3. L1-L5 成熟度與課程模組

### 3.0 L1-L5 的兩條軸：從一個人的工具，到公司自己的數位人力

> 企業的 AI 成熟度，不是「學會幾個工具」，而是走過**兩條軸**：先讓 AI 滲透整個組織，再讓組織長出自己的 AI 人力。

#### 第一幕：規模軸 —— AI 從「一個人的工具」長成「全公司的神經」（L1 → L2 → L3）

阿哲是一位業務。

- **L1・個人**：阿哲自己學會用 AI 寫客戶拜訪信。很好用——但只有他會，方法鎖在他腦袋裡。AI 的能力範圍 ＝ 一個人。
- **L2・部門**：業務部把「怎麼寫好一封拜訪信」整理成一個 Skill，新人第一天就能用。AI 的能力範圍，從阿哲擴散到整個部門。
- **L3・跨部門 / 全公司**：業務部、客服部、財務部的 Skill 被 n8n 串起來，接上 CRM、ERP、email。一封客訴信進來，AI 自動跨部門查資料、更新、通知。AI 的能力範圍，變成整間公司。

這一幕從頭到尾，**方向盤在人手上**。阿哲、主管、IT 決定 AI 做什麼、做到哪——AI 再強，都是「人在開的車」。這條軸的進步，是**滲透範圍**：一個人 → 一個部門 → 一整間公司。

#### 第二幕：AI 自主軸 —— 公司養出了「不在編制內的員工」（L4 → L5）

當全公司的流程都接起來了（L3 把地基打好），公司可以做一件以前做不到的事：**讓 AI 自己上工。**

- **L4・AI 超級助理**：公司多了一個會自己上工的 AI 個體。它有自己的職責地圖、自己的工具、自己的排程。主管早上進辦公室，桌上已經有它整理好的 briefing 和三個要追蹤的問題。主管的角色，從「使用 AI」變成「管理一個 AI 部屬」。
- **L5・AI 團隊**：不只一個。市場 AI、產品 AI、財務 AI、客服 AI……多個有專長的 AI 組成一支團隊，自己分工、自己協作，完成「新產品上市分析」這種跨部門大任務。主管的角色再升一級——從「管一個 AI」變成「治理一支 AI 部隊」。

這一幕，**方向盤在 AI 手上**。但人沒有消失——**人退到更高的位置**：定義職責、設定規則、驗收成果，保留 HITL（Human-in-the-Loop，人類在迴圈內審核）與階段驗收關卡。**AI 愈自主，人就愈像「治理者」，而不是被取代的「操作員」。**

#### 那條最重要的線：L3 → L4

整個模型只有**一條真正的分界**，就在 L3 和 L4 之間：

| | L1 → L3（規模軸）| L4 → L5（AI 自主軸）|
| --- | --- | --- |
| 你問的問題 | 「我能**用** AI 做到多**廣**？」 | 「我的 AI 能**自己**做多少？」 |
| 方向盤在誰手上 | 人 | AI（人退為治理者）|
| AI 的身分 | 公司的**工具** | 公司的**數位人力** |
| 怎麼長大 | 個人 → 部門 → 全公司 | 一個助理 → 一支團隊 |

而且這條線**沒有捷徑**：L4 一定要站在 L3 打好的地基上——沒有全公司串好的流程，AI 根本沒有東西可以「自己跑」。

> L1-L3，你把 AI 教會、教廣；L4-L5，你把 AI 養成、交棒。走完兩條軸，公司不只是「會用 AI」，而是「擁有 AI 人力」——而你，從操作員變成治理者。

### 3.0.1 采購 AI，不是買系統：L4-L5 的心態轉換

到了 L4-L5，企業要做的最大轉換不是技術，是**心態**。

老闆習慣用「買系統」的方式看 AI：評估功能清單、比較授權價格、算軟體 ROI。但 L4-L5 的 AI 不是一套軟體 —— 它具備**推理、自主、會用工具**三件事，功能上它做的就是一個知識工作者在做的事。所以正確的心態是**「采購 AI」**：像招募、上工、管理、治理一個人才，而不是像買一套軟體。

| 買系統的心態 | 采購 AI 的心態 |
| --- | --- |
| 評估功能清單、座位數、授權年費 | 評估它接走多少工作量、放大多少產能 |
| 算「軟體 ROI」 | 算「人力 ROI」—— ROI 沒有不見，是換了一把尺 |
| 安裝、上線、結束 | 定義職責、上工、績效檢視、持續治理 |
| 人被工具取代 | 人升級成治理者，多了一個要被治理的數位人力 |

> **範圍**：這個心態只適用 **L4-L5（AI 自主軸）**。L1-L3 你本來就是在買工具、買設備、買系統 —— 那是合理且可驗證的。「采購 AI」講的是 AI 跨過 L3→L4、變成自主數位人力之後，老闆的心態要跟著換。
> **它是管理姿態的類比，不是說「AI 就是人」** —— 正因為 AI ≠ 人，它才需要人建立的治理框架與 HITL，而那正是顧問服務的核心。

### 3.1 L1 Controlled AI Access：OpenWebUI

#### 定位

OpenWebUI 是企業內部 AI 對話入口。

L1 的重點是讓員工安全、穩定、有效地開始使用 AI，處理日常知識工作。

#### 典型情境

業務同仁要寫客戶拜訪信、會議摘要、提案初稿。以前要花 1 小時整理，現在透過 OpenWebUI 可以在 15 分鐘內產出初稿，再由人修正。

#### 客戶會聽懂的價值

- 員工開始節省個人工作時間。
- 公司可以建立統一 AI 入口。
- 比較容易管理模型、權限與使用規範。
- 建立後續 Skill 化與 Workflow 化的共同基礎。

#### 課程內容

- OpenWebUI 基本操作。
- AI 對話與 Prompt 基礎。
- 摘要、改寫、翻譯、分類、腦力激盪。
- 企業 AI 使用規範。
- 不適合丟給 AI 的資料與任務。

#### 課程產出物

- 個人高頻工作 Prompt。
- 部門 AI 使用注意事項。
- 常見職能情境範例。

### 3.2 L2 Knowledge Codification：Antigravity / Claude Code / Codex

#### 定位

L2 的重點是把個人經驗變成部門能力。

Antigravity、Claude Code、Codex 不是只拿來寫程式，而是作為「Skill 建置工具」：把一位高手的工作方法整理成可重複使用的規格、提示詞、文件、模板與操作流程。

#### 典型情境

行銷主管原本很會寫產品文案，但每次新人加入都要重新教。透過 L2 Knowledge Codification，可以把文案產生流程整理成「文案產生 Skill」：

- 目標客群。
- 語氣風格。
- 禁用語。
- 產品賣點。
- 範例文案。
- 輸出格式。

新人只要呼叫 Skill，就能產出接近部門標準的內容。

#### 客戶會聽懂的價值

- 不再只依靠個人英雄。
- 好的方法可以被複製。
- 新人訓練時間縮短。
- 部門品質更一致。
- 知識開始沉澱為公司資產。

#### 課程內容

- Skill 的定義與範例。
- 如何把個人經驗寫成 Skill。
- 如何整理 Prompt、SOP、Checklist、Template。
- 如何用 Antigravity / Claude Code / Codex 協助產出文件與規格。
- 部門 Skill Library 的維護方法。

#### 課程產出物

- 部門 Skill 清單。
- 3-5 個高頻 Skill 範例。
- Skill 標準模板。
- Skill 維護與版本控管建議。

### 3.3 L3 Workflow Automation：n8n

#### 定位

L3 的重點是讓 AI 不只是回答問題，而是進入流程、串接系統、完成任務。

n8n 是 Workflow AI 的核心，用來連接 Gmail、Google Sheets、Notion、CRM、API、ERP 等系統。

#### 典型情境

客服主管每天要看 Gmail 客訴信、到 CRM 查客戶資料、把狀態更新到 Google Sheets，再在 Notion 寫週報。這些工作很耗時間，也容易漏資料。

透過 n8n 可以設計 Workflow：

1. Gmail 收到客訴信。
2. AI 判斷客訴類型與急迫性。
3. 到 CRM 查客戶等級與歷史紀錄。
4. 到 ERP 查訂單或出貨狀態。
5. 將整理結果寫入 Google Sheets。
6. 在 Notion 自動建立處理任務。
7. 發 Email 或 Slack 通知負責人。
8. 週五自動彙整客服週報。

#### 客戶會聽懂的價值

- 減少重複性人工搬資料。
- 降低漏單、漏信、漏更新。
- 讓資料流、任務流、決策流接在一起。
- AI 開始替公司做事，而不是只跟人聊天。

#### 系統串接範圍

- Gmail：信件收取、分類、摘要、回覆草稿。
- Google Sheets：資料紀錄、名單維護、報表更新。
- Notion：任務管理、知識庫、會議紀錄。
- CRM：客戶資料、商機、互動紀錄、服務紀錄。
- API：內外部系統資料交換。
- ERP：訂單、庫存、出貨、採購、財務資料。
- Database：PostgreSQL、MySQL、向量資料庫等。
- 通訊工具：Slack、Teams、LINE、Telegram。

#### 課程內容

- n8n 基本概念。
- Trigger、Node、Credential、Webhook。
- Gmail / Sheets / Notion 串接。
- API 串接與資料轉換。
- ERP / CRM 串接規劃。
- AI Node 與 RAG 節點應用。
- 錯誤處理與人工審核節點。

#### 課程產出物

- 1-2 個部門 Workflow PoC。
- Workflow 場景盤點表。
- 系統串接需求清單。
- 自動化風險與權限檢核表。

### 3.4 L4 Autonomous Agent：Hermes Agent

#### 定位

L4 的重點是讓 AI 從「一次性回答」升級為「可持續運行的知識工作代理」。它不只理解任務、拆解步驟、呼叫工具與回報結果，還要能留下記憶、索引、證據、排程與人工審核紀錄。

Hermes Agent 是 L4 的標準平台。它把 L1 Chat、L2 Skill、L3 Workflow 整合成一個知識型 Agent 作業系統：

1. Markdown Wiki 作為知識真相來源。
2. SQLite / FTS 作為查詢索引與衍生快取。
3. 五個核心 skills 負責管理、來源分析、關鍵字抽取、自主發現與 briefing。
4. deterministic tools 負責寫入、索引、驗證、抽取、快取與 log。
5. 排程負責 nightly ingest、morning briefing、discovery ping、evening preview、weekly graph synthesis。
6. HITL（Human-in-the-Loop，人類在迴圈內審核）負責高風險更新、關鍵字核准、schema 變更、刪除與上線判斷。

#### 典型情境

營運經理對 AI 助理說：

> 幫我整理這週異常訂單，找出前三大原因，產出主管會議報告，並列出需要追蹤的客戶。

Hermes Agent 會：

1. 先讀取部門 `purpose.md`、`SCHEMA.md`、`INBOX.md`、`queue.md`、`watchlist.md` 與近期 log。
2. 呼叫 ERP 查詢異常訂單。
3. 呼叫 CRM 查詢客戶資料。
4. 呼叫 Google Sheets 整理分析表。
5. 呼叫 L2 的「異常分析 Skill」。
6. 呼叫 L3 的報告產生 Workflow。
7. 將分析過程、引用來源、待追蹤任務與主管摘要寫回 Wiki。
8. 在 briefing 中提醒主管哪些項目需要人工確認。

#### 客戶會聽懂的價值

- 同仁不用知道每個系統怎麼操作。
- AI 可以幫忙拆解與執行跨系統任務。
- 管理者可以更快取得決策資料。
- AI 從工具變成可累積知識、可追溯證據、可排程運作的工作代理人。
- Agent 不只是做一次任務，而是每天持續整理、提醒、更新與產生 briefing。

#### 課程內容

- Agentic AI 基本觀念與 L4 / L5 邊界。
- Hermes Agent 架構：Wiki、SQLite、skills、tools、runtime schema、policy。
- Orient-first SOP：Agent 開工前先讀 schema、purpose、INBOX、index 與 log。
- Ingest / query / update / lint / graph-synthesis。
- source analysis、keyword extraction、autonomous discovery、briefing-generator。
- 如何設計 Agent 可用的 Skill 與 n8n Workflow。
- HITL 人類審核、權限、Log、fallback 與階段驗收關卡（Stage Gate）。

#### 課程產出物

- 1 個部門 Hermes Agent 任務範例。
- L4 IPOE 表。
- Agent 任務說明書。
- 初始 Wiki：`purpose.md`、`SCHEMA.md`、INBOX、queue、watchlist、tasks。
- Agent 可用工具清單。
- Ingest / query / update 測試紀錄。
- Briefing 範本。
- 驗收關卡 4A-4E 驗收表。
- Agent 風險、權限與維運 Runbook。

### 3.5 L5 Multi-Agent Organization：ClawTeam

#### 定位

L5 的重點是多個專業 Agent 協作，形成 AI 團隊，完成單一 Agent 難以完成的企業級任務。

ClawTeam 是 Agentic Team AI 的落地平台。

#### 典型情境

老闆說：

> 我們想開發一個新產品，幫我整理市場機會、競品、產品定位、行銷策略、客服準備與財務預估。

ClawTeam 可以啟動多個 Agent：

- 市場分析 Agent：分析市場趨勢、客群、競品。
- 產品規劃 Agent：整理產品需求、功能優先順序。
- 行銷策略 Agent：提出通路、訊息、活動規劃。
- 客服支援 Agent：準備 FAQ、服務流程、知識庫。
- 財務分析 Agent：估算成本、收益、預算與 ROI。
- 專案整合 Agent：整合所有輸出，形成專案計畫。

#### 客戶會聽懂的價值

- 不是一個人加一個 AI，而是一個部門加一個 AI 團隊。
- 跨部門複雜任務可以更快形成初稿。
- 管理層可以用 AI Team 做決策前置作業。
- 企業開始具備自動化營運與創新能力。

#### 課程內容

- Multi-Agent 協作觀念。
- Agent 角色設計。
- 任務分派與整合。
- 角色衝突與品質檢查。
- Agent Team 的輸出格式。
- 企業級任務的治理與監督。

#### 課程產出物

- 一個 Agent Team 情境設計。
- Agent 角色卡。
- 多 Agent 協作流程圖。
- Agent Team 輸出範例。

## 4. 簡易問卷診斷設計

### 4.1 問卷目的

問卷要讓客戶在 10-15 分鐘內理解：

- 公司目前 AI 成熟度在哪裡。
- 哪些能力已經有基礎。
- 哪些缺口阻礙下一階段。
- 課程應該如何配置比例。
- 後續顧問診斷要聚焦哪些議題。

### 4.2 問卷構面

問卷建議分成六個構面：

| 構面 | 要判斷的事 |
| --- | --- |
| 工具使用 | 員工是否已經穩定使用 AI 工具 |
| 知識沉澱 | 是否有 Prompt、SOP、模板、Skill Library |
| 流程自動化 | 是否已經有系統串接、自動化流程 |
| 系統整合 | Gmail、Sheets、Notion、CRM、API、ERP 是否能被流程調用 |
| Agent 應用 | 是否有可自主執行任務的 AI Agent |
| 執行導入與變革治理 | 是否有權限、資安、成效指標與管理制度 |

### 4.3 診斷輸出

問卷完成後輸出：

- 目前成熟度等級：L1-L5。
- 主要缺口：例如知識未沉澱、流程未串接、Agent 缺治理。
- 建議課程比例：例如 L1 20%、L2 30%、L3 30%、L4 15%、L5 5%。
- 建議優先場景：例如客服信件自動分類、業務提案產生、ERP 異常訂單分析。
- 後續顧問診斷焦點：例如流程盤點、資料權限、ROI 指標。

## 5. 課程比例配置邏輯

### 5.1 配置原則

課程比例不是客戶隨便選，也不是我們固定賣。

建議邏輯：

- 先依問卷判斷目前成熟度。
- 再看管理層目標：效率、成本、品質、營收、治理。
- 再看系統條件：是否已有 Gmail、Sheets、Notion、CRM、ERP、API。
- 再看公司屬性：產業、資料敏感度、IT 能力、預算、雲端政策。
- 再看部署模式：雲 AI、Hybrid、全地端。
- 最後決定 L1-L5 的課程比例。

### 5.2 公司屬性與部署模式

課程設計前要先調查客戶適合哪種 AI 架構。

#### 雲 AI

最便宜、最快啟動，適合資料敏感度較低、以文案、研究、客服、行銷、一般知識工作為主的企業。課程可強化 L1、L2，L3 先串接 SaaS 工具，例如 Gmail、Sheets、Notion、CRM。

#### Hybrid：雲 + 地端

多數企業最務實的路徑。非敏感任務可走雲端模型，敏感資料、內部系統與核心流程留在地端。課程要強化資料分級、n8n 路由、Credential、API、ERP 串接與人工審核。

#### 全地端

適合研發製造、金融、醫療、政府或高度敏感資料場景。課程要強化 OpenWebUI 私有入口、地端模型、內部 RAG、ERP/API/DB 串接、Log、權限、稽核與變更管理。

### 5.3 產業適配性

#### 研發製造業

常見系統是 ERP、MES、PLM、QMS、內部資料庫與文件系統。AI 場景應放在 SOP 查詢、品質異常、客訴分析、研發文件摘要、ERP 異常訂單與製程知識沉澱。通常建議 Hybrid 或全地端。

#### 行銷服務業

常見系統是 Gmail、Sheets、Notion、CRM、廣告平台與社群工具。AI 場景應放在提案、文案、競品分析、客戶會議摘要、CRM 更新與活動成效報告。通常可從雲 AI 或 Hybrid 快速啟動。

#### 高敏感產業

例如金融、醫療、政府、上市櫃關鍵部門。課程要優先處理資料分級、權限、稽核、人工審核與地端部署，L4/L5 應先定位為決策支援，而不是完全自動決策。

### 5.4 範例配置

#### 情境 A：AI 初學企業

目前狀態：多數員工還沒穩定使用 AI。

建議比例：

- L1 OpenWebUI：40%
- L2 Knowledge Codification：35%
- L3 n8n：20%
- L4 Hermes Agent：5%
- L5 ClawTeam：0%

目標：先建立共同語言與部門 Skill。

#### 情境 B：已有 AI 使用，但缺流程落地

目前狀態：員工會用 AI，但成果散落，流程仍人工。

建議比例：

- L1 OpenWebUI：15%
- L2 Knowledge Codification：30%
- L3 n8n：40%
- L4 Hermes Agent：10%
- L5 ClawTeam：5%

目標：把 Skill 串成 Workflow，優先完成 1-2 個 PoC。

#### 情境 C：已有自動化基礎，想導入 Agent

目前狀態：已有 n8n 或系統整合經驗。

建議比例：

- L1 OpenWebUI：5%
- L2 Knowledge Codification：20%
- L3 n8n：25%
- L4 Hermes Agent：30%
- L5 ClawTeam：20%

目標：從流程自動化升級到 Agent 與 Agent Team。

## 6. 八階段顧問診斷方法

> **核心思維**：以營運模式轉型為中心，透過 80/20 原則精準投放資源，建立可持續進化的能力體系。
>
> **方法論主軸**（Rosemann BPM 學派）：As-Is 真相 → 國際標準座標 → 產業卓越特徵 → 客觀差距 → 核心問題 → 階段可吸收目標 → 多階段藍圖 → 變革落地。

### 6.0 八階段資料流：上一階段的 Output 是下一階段的 Input

```
[Stage 1]                  [Stage 2]                  [Stage 3]
As-Is Snapshot             Reference Model            Best Practice
現況掌握                    標準模型引入                產業最佳實務對標
─────────────              ─────────────              ─────────────
40 題訪談 →                 APQC PCF +                 卓越能力特徵
AI/系統盤點 → ─────────►   Tiger AI L1-L5  ────────►  （可量化的卓越定義）
As-Is Swimlane             雙座標 Mapping              ＋ 5 個產業 Benchmark
                           ▼                          ▼
                           標準能力缺口檢核            「卓越長什麼樣」
                           ＋ 雙雷達圖

[Stage 4]                  [Stage 5]                  [Stage 6]
Gap Analysis               Problem Definition         Phased Goals
差距分析                    核心問題定義                多階段目標設定
─────────────              ─────────────              ─────────────
（Stage 2 + 3 對比         80/20 收斂 +               終極標竿
 Stage 1）                  5 Whys 根因                  ↓ 拆解
Missing / Broken /  ─►     ↓                  ────►  Phase 1 基礎穩固
Redundant 三類分            ▼                          Phase 2 效能優化
Impact × Effort            Executive Problem          Phase 3 標竿卓越
（不作為風險評估）           Statement                  ＋ 組織吸收力評估

[Stage 7]                  [Stage 8]
To-Be Design               Implementation & Change
未來藍圖設計                執行導入與變革治理
─────────────              ─────────────
每 Phase 一張               Transformation Roadmap
To-Be Operating Model      變革管理 Playbook
＋ 人機協作（HITL）─────►  RACI / Permission / Audit
＋ Skill/Workflow/         價值追蹤矩陣（5 維度）
   Agent Map               Risk Register / Ethics

  ◄────────── 每季回頭核對 Stage 2 Reference Model 雷達 ──────────►
  （階段先行、逐步推廣，每階段驗收皆需回頭核對標準完整度）
```

### 6.1 八階段怎麼跑：一個 6 週顧問案的情境演練

> ⚠️ **以下「客戶 M」為 AI 模擬產生的虛構案例**，並非真實客戶。所有公司規模、KPI、預算數字皆為**示例**，僅供方法論教學示範用。詳見 [`../04_Scenarios/README.md`](../04_Scenarios/README.md) 學術誠信聲明。
>
> **客戶 M**（虛構）：半導體封測廠，700 人，CEO 看到三家對手都導入 AI 質檢與客訴 Agent，客戶 A 季訂單下降 18%。簽下 6 週顧問案 + 後續 24 個月 Roadmap。預算上限 NT$ 800 萬，製程資料須地端。

#### Week 1 ── Stage 1 As-Is Snapshot：先聽、先看、不評論

**Day 1-2**：顧問拿 [`CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 1.1 的 40 題題庫進場。CEO/COO/CIO 各 60 分；品保長、業務長、客服長、IT 副理各 90 分；產線、業務、客服各 3 位操作員每位 30 分。**錄音 + 摘要 + 編碼**。

**Day 3-4**：IT 副理協助盤點 Tool 1.2 AI Usage Inventory（影子 IT：行銷部 8 人用個人 ChatGPT 月燒 NT$24,000）+ Tool 1.3 Systems Inventory（SAP B1 地端、Salesforce 雲、Notion 部門自管）。

**Day 5**：和品保 + 業務各跑一場 walkthrough，畫 Tool 1.4 As-Is Swimlane：「客戶詢價到出貨」（4-7 天，漏接 30%）、「客訴回應」（5 天）、「製程異常」（3 天）。每 step 標 0-3 點痛點密度。

**週末交付**：Discovery Report + 3 張 swimlane。**這份報告只描述「現在發生什麼」，不建議任何事**。

> 顧問紀律：Stage 1 絕對不能跳到 Stage 7「我建議導 n8n」。客戶會抗拒。先把現狀講清楚。

#### Week 2 上半 ── Stage 2 Reference Model Alignment：套國際標準座標

**Day 6**：顧問選 **SCOR**（製造業必選）+ **APQC PCF**（通用）+ **Tiger AI L1-L5**（AI 軸）三套 Reference Model。

**Day 7-8**：跑 Tool 2.2 Mapping Worksheet。把 Stage 1 盤點到的 process / 系統 / 角色，落點到三套標準的格子。發現：

- ✅ SCOR Source（採購）成熟。
- ⚠️ SCOR Make / Deliver 部分（人工密集）。
- ❌ APQC 8.x IT Governance：弱。
- ❌ **APQC 11.x Knowledge Management：完全缺**（沒 Wiki、沒 SOP、無人 own）。
- ❌ Tiger AI L1 / L2 / L3：完全缺。

**Day 9**：產出 Tool 2.3 標準能力缺口檢核清單 + Tool 2.4 雙雷達圖（一張 APQC、一張 Tiger AI）。給 CEO 看：「依國際標準，您的營運結構在這幾個 Category 是空的」。

> **管理層第一次震驚**：他們以為公司「該有的都有」，雷達圖一畫，缺口無所遁形。**這是 Rosemann BPM 學派最厲害的一招**：不是顧問主觀說你有問題，是國際標準說你缺。

#### Week 2 下半 ── Stage 3 Best Practice Integration：定義「卓越長什麼樣」

**Day 10-11**：拿出 5 個現成 Benchmark Stub 中的 Manufacturing（半導體封測 700 人，9 個月 L1→L3）+ 另找 2 家半導體業同業案例。跑 Tool 3.1 Best-Practice Profile + Tool 3.2 卓越能力特徵定義表：

| 能力 | 卓越特徵（可量化）| 領先案例佐證 | M 公司距離 |
| --- | --- | --- | --- |
| 客訴回應 | 90% 1hr AI 分流 + 24hr 人工回 | A 公司 | 5 天 vs 1 天 |
| 製程異常 | 異常 → 假設 ≤ 30min | B 公司 | 3 天 vs 30 min |
| 知識沉澱 | 每月 ≥ 30 條 Skill 入庫 | C 公司 | 0 vs 30/月 |

**Day 12**：CEO + 各部門長一起 review。**「卓越不是抽象的，這就是同業已經做到的具體數字」**。

#### Week 3 ── Stage 4 Gap Analysis：把差距盤清楚（不是風險評估）

**Day 13-14**：拿 Stage 2（標準缺口）+ Stage 3（卓越距離）對照 Stage 1（現況），跑 Tool 4.1 Missing/Broken/Redundant 表：

- **Missing**：客服 AI 分類、知識管理、AI 治理 → 對應 APQC 11.x、Tiger AI L1-L3
- **Broken**：報價系統（人工 copy-paste、無 API）、製程異常通報（5 個系統各報各的）
- **Redundant**：工單 Notion+Trello+Email 三套

**Day 15**：跑 Tool 4.2 Impact × Effort + Tool 4.3 Prioritization。客服分類 20 分排第 1，業務提案 Skill 8 分排第 4，ERP Agent 5 分（Big Bet，後段）。

> **顧問紀律**：本週**不寫風險、不寫對策**。風險屬於 Stage 8。Stage 4 只回答「差什麼、差多少、做了影響多大」。

#### Week 4 上半 ── Stage 5 Problem Definition：80/20 找真因

**Day 16**：跑 Tool 5.1 80/20 收斂工作表。把全部 Stage 4 差距列出來，逐條標「影響幾個 process、幾個部門、幾條 KPI」。

發現 4 個高影響差距（A 客服慢 / B 報價慢 / C 知識無沉澱 / D 製程慢）。對 C 跑 **5 Whys**：

```
為什麼沒人寫？   → 寫了沒人用
為什麼沒人用？   → 散在各處找不到
為什麼找不到？   → 沒中央 Wiki
為什麼沒 Wiki？  → 沒人 own + 沒工具 + 沒誘因  ← 真因
```

**Day 17-18**：產出 Executive Problem Statement：

> **M 公司沒有「知識資產化」的角色、工具與誘因，80% 的差距（A/B/C/D）都源於同樣的事重複做、無人沉澱、無人重用。**

CONTEXT / TENSION / COST OF INACTION（流失客戶 A/B/C，年營收 -1.8 億）/ DESIRED FUTURE（不良率 2.0%、客訴 ≤1 天）/ CONSTRAINTS（NT$ 800 萬上限、地端、IT 2 FTE）全部填齊。

**Day 19**：CEO + 高管 review。**這是整個顧問案的轉折點**：客戶從「我們缺工具」→ 認知到「我們缺角色 + 工具 + 誘因的整套組合」。

#### Week 4 下半 ── Stage 6 Benchmarking & Phased Goals：把卓越拆成吃得下的台階

**Day 20-21**：跑 Tool 6.1 終極標竿 → 三階段拆解。把 Stage 3 每條卓越特徵拆成 Phase 1（0-6m 基礎）/ Phase 2（6-12m 優化）/ Phase 3（12-24m 卓越）：

| 能力 | 終極標竿 | Phase 1 | Phase 2 | Phase 3 |
| --- | --- | --- | --- | --- |
| 客訴回應 | 1hr 分流 + 24hr 回 | L1 Controlled AI Access 全員 + Prompt | n8n 分類 + Reviewer | Hermes 草稿 + 根因 |
| 知識沉澱 | 30 條/月 | 5 條核心 Skill | 15 條 + 跨部門 | 30 條 + Wiki 引用 |
| 製程改善 | 異常→假設 ≤30min | 製程 SOP 知識化 | n8n 異常摘要 | Agent Team 多模協作 |

**Day 22-23**：跑 Tool 6.3 組織吸收力評估（6 維度：預算、AI Champion、IT FTE、權限治理、員工 AI 素養、變革容量）。發現 M 公司 Phase 1 吸收力夠，**但 Phase 2 需要再多 0.5 IT FTE**。決策：拉長 Phase 2 由 6 月 → 9 月。

**Day 24**：產出 Tool 6.2 Stage Gate Criteria（L1 Gate / L2 Gate / L3 Gate / L4 Gate / L5 Gate 的驗收清單）。

> **第二次震驚**：客戶本來想「一年到 L4」，看到拆解後接受「24 個月到 L4」是務實的。**避免一次到位失敗 = Stage 6 的價值**。

#### Week 5 ── Stage 7 To-Be Design：每 Phase 一張未來藍圖 + 人機協作架構

**Day 25-26**：依 Phase 1/2/3 各畫一張 To-Be Operating Model（個人層 / 部門層 / 流程層 / 系統層 / 治理層 / 人機分工）。重點是 **每張圖人機分工比例不同**：

```
Phase 1（基礎）：100% 人主導，AI 是個人助理
Phase 2（優化）：70% 人 + 30% Workflow 自動 + HITL
Phase 3（卓越）：50% 人 + 30% Workflow + 20% Agent 自主（含 HITL）
```

**Day 27**：跑 Tool 7.2 人機協作架構。對每個關鍵 process 明確定義「人做什麼、AI 做什麼、HITL 在哪」：

| Process | 人 | AI | HITL | 驗收 |
| --- | --- | --- | --- | --- |
| 客訴回覆 | 審草稿 + 主動關懷 | 分類、優先級、產草稿 | 寄出前 100% 人審 | 直接寄出率 ≥60% |
| 製程根因 | 跨部門協調、決策 | 整資料、產假設 | 對策前 100% 人審 | 根因報告 ≤2 天 |

**Day 28-29**：產出 Skill Map / Workflow Map / Agent Map（先列骨架、Phase 1-3 分批實作）+ Integration Architecture（M 公司選 **Variant B Hybrid**：低敏感雲、製程資料地端 Llama）。

#### Week 6 ── Stage 8 Implementation & Change：把藍圖變成會動的東西

**Day 30**：跑 Tool 8.1 Transformation Roadmap（24 個月 6 季）+ Tool 8.2 變革管理計畫（含 Stakeholder Map、溝通計畫、訓練計畫、抗拒處理 Playbook）。

**Day 31**：對 M 公司 700 人做抗拒預測：

- 怕被取代（產線 ~50 位）→ 1:1 對話、升級為「AI 監督者」角色
- 不會用（年資 20+ 員工 ~30 位）→ 1:1 mentor + 簡化第一個成功經驗
- 不信任（品保高敏感 ~10 位）→ 先給「人審」場景累積信任

**Day 32**：跑 Tool 8.3 RACI、Tool 8.4 Permission Matrix（六種角色 × 五種權限）、Tool 8.5 **價值追蹤矩陣**（5 維度：時間、品質、規模、風險、資產）、Tool 8.6 Risk Register（含階段目標吃不下的風險）、Tool 8.7 Audit Log、Tool 8.8 Ethics 15 項。

**Day 33-35**：把 Stage 1-8 全部產出物編成 14 章診斷報告（依 [`CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md) 結構）+ SOW 提案 + 30-90 days Quick Win 提案。

**結案會議**：Sponsor + 高管 + AI Champion + IT + HR + 法遵全到場。客戶**簽下 Phase 1（NT$ 280 萬，6 個月）**，並承諾「**每季結尾回頭看 Stage 2 雷達是否更圓**」。

#### Week 6 之後 ── 階段先行、逐步推廣（每季回頭核對 Reference Model）

```
Q1 結尾：L1 Gate 驗收 → 回看 APQC 雷達 → Tiger AI L1 從 0 → 3
Q2 結尾：L2/L3 Gate    → 回看雷達     → APQC 8.x 從 0 → 2、L3 從 0 → 2
Q3 結尾：L4 Gate       → 回看雷達     → APQC 11.x 從 0 → 3（**知識資產化真因解決**）
...
```

每個季度都重新檢視 Stage 2 標準雷達 —— **這是方法論的閉環設計**：避免做了一堆 PoC 卻沒回頭看「我們的標準完整度是否真的變好了」。

---

### 6.2 各階段定義快查 / Stage Reference

> 完整工具表格與操作指引請見 [`03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md)。本節僅列各階段定位與 Output KPI 快查。

#### Stage 1：As-Is Snapshot 現況掌握

透過訪談與數據盤點資訊流、決策流，識別人工密集與瓶頸節點。**只描述，不評論、不建議**。

輸出：現況評估報告（Assessment Report）、真實營運流程圖（As-Is Process Maps）、AI 使用盤點表、系統盤點表。

#### Stage 2：Reference Model Alignment 標準模型引入

導入國際標準框架（APQC PCF / SCOR / eTOM / ITIL / CMMI）+ Tiger AI L1-L5，建立**業務結構 × AI 採用**雙座標。**用業界公認的標準說話，不靠顧問主觀判斷**。

輸出：標準能力缺口檢核清單、營運結構完整度雷達（產業 RM + Tiger AI 雙圖）。

#### Stage 3：Best Practice Integration 最佳實務對標

識別行業領先模式，把抽象的「卓越」翻譯為本公司**具體可量化**的成熟度特徵與目標。

輸出：產業標竿營運模型圖、卓越能力特徵定義（每條都有量化指標 + 領先案例佐證）。

#### Stage 4：Gap Analysis 差距分析

結構化比對 Stage 1 vs Stage 2 + Stage 3，分類 Missing / Broken / Redundant。**這是客觀盤點，不是風險評估**（風險屬 Stage 8）。

輸出：差距矩陣（Impact × Effort）、優先級排序。

#### Stage 5：Problem Definition 結論與核心問題定義

80/20 收斂 + 5 Whys 根因，鎖定具槓桿效應的核心病灶，區分症狀與真因。

輸出：Executive Problem Statement（一句話 + CONTEXT / TENSION / COST OF INACTION / DESIRED FUTURE / CONSTRAINTS 五段式）。

#### Stage 6：Benchmarking & Phased Goals 標竿對照與多階段目標設定

把 Stage 3 的「終極標竿」拆解為**組織可吸收**的 Phase 1/2/3 階段性目標，並評估組織吸收力。**一次到位 = 失敗**；組織有吸收上限。

輸出：終極標竿 → 階段拆解表、Stage Gate Criteria（L1-L5 各 Gate）、組織吸收力評估（6 維度）。

#### Stage 7：To-Be Design 未來藍圖設計

每個 Phase 各一張 To-Be Operating Model + 明確的**人機協作架構**（哪些人做、哪些 AI 做、HITL 節點在哪）。

輸出：分階段 To-Be Operating Model、未來流程圖、Skill / Workflow / Agent Map、整合架構（Cloud / Hybrid / On-Prem 三選一）。

#### Stage 8：Implementation & Change 執行導入與變革治理

階段先行、逐步推廣。每階段驗收皆需回頭核對 Stage 2 Reference Model 雷達。除執行 Roadmap 外，**變革管理（人）+ 治理（規則）+ 價值追蹤（數據）三件事都要落地**。

輸出：Transformation Roadmap、變革管理計畫（含抗拒處理 Playbook）、RACI、Permission Matrix、價值追蹤矩陣（5 維度）、Risk Register、Audit Log、AI Ethics Checklist。

## 7. 最終交付物：AI 轉型診斷報告目錄

### 7.1 封面

企業名稱、診斷期間、顧問團隊、版本。

### 7.2 Executive Summary

給老闆看的 1-2 頁摘要：

- 目前成熟度。
- 最大問題。
- 最大機會。
- 建議優先導入方向。
- 預期價值。

### 7.3 AI 成熟度診斷結果

- L1-L5 評分。
- 六大構面雷達圖。
- 各部門成熟度差異。
- 主要缺口。

### 7.4 課程觀察與能力盤點

- 課程參與狀況。
- 各部門產出的 Prompt、Skill、Workflow、Agent 情境。
- 員工吸收程度。
- 管理層關注問題。

### 7.5 As-Is 現況流程與系統盤點

- Gmail、Sheets、Notion、CRM、API、ERP 等系統使用情況。
- 資料流。
- 任務流。
- 決策流。
- 人工重工點。

### 7.6 高價值 AI 場景清單

按部門整理：

- 業務。
- 客服。
- 行銷。
- 營運。
- 財務。
- 人資。
- IT。
- 管理層。

每個場景要標註：

- 對應成熟度：L1-L5。
- 需要串接系統。
- 預期效益。
- 導入難度。
- 風險與治理需求。

### 7.7 差距分析與核心問題

- Missing：缺少的能力、資料、流程、角色。
- Broken：目前壞掉或不穩定的流程。
- Redundant：重複、低價值、可自動化的工作。
- 核心問題定義。

### 7.8 To-Be AI Operating Model

- 部門 Skill Library。
- n8n Workflow Center。
- Hermes Agent 任務中心。
- ClawTeam Agent Team 協作模式。
- 權限與審核機制。

### 7.9 三階段 Roadmap

#### Phase 1：AI 基礎與 Skill 化

目標：把個人使用轉為部門能力。

#### Phase 2：Workflow 自動化

目標：串接 Gmail、Sheets、Notion、CRM、API、ERP，完成高價值流程 PoC。

#### Phase 3：Agentic AI 與 AI Team

目標：讓 Hermes Agent 與 ClawTeam 承接跨部門任務。

### 7.10 ROI 與治理建議

- 時間節省。
- 錯誤率下降。
- 回應速度提升。
- 知識沉澱。
- 新人訓練縮短。
- 管理決策品質提升。
- 資料權限與資安控管。

## 8. 對外銷售故事版本

### 8.1 30 秒版本

多數企業現在都已經有人在用 AI，但大多停在個人工具階段。我們會先用問卷診斷企業目前 AI 成熟度，再依照 L1-L5 安排課程比例，最後用八階段顧問方法論產出 AI 轉型診斷報告，讓企業知道現在在哪裡、下一步做什麼、哪些流程可以先自動化。

### 8.2 3 分鐘版本

AI 轉型最常見的問題，不是員工不會用 AI，而是使用太零散。有人會用 ChatGPT，有人會寫 Prompt，有人想串 CRM，有人想自動整理 ERP 報表，但公司沒有共同架構。

我們把 AI 成熟度分成五級：L1 是 OpenWebUI 的 Chat AI，L2 是用 Antigravity、Claude Code、Codex 建立 Skill AI，L3 是用 n8n 串接 Gmail、Sheets、Notion、CRM、API、ERP 的 Workflow AI，L4 是 Hermes Agent，L5 是 ClawTeam 的多 Agent 團隊。

服務流程很簡單：先做問卷診斷，知道企業目前在哪一級；再依照診斷結果上課，課程比例由客戶成熟度與目標決定；最後我們用八階段管理顧問方法論產出診斷報告，包含現況、差距、核心問題、未來藍圖、Roadmap 與 ROI。

所以客戶買到的不是一堂課，而是一條從 AI 學習到企業轉型落地的路。

## 9. 需要後續補齊的內容

後續應優先完成：

- AI 成熟度問卷題目。
- L1-L5 評分邏輯。
- 課程比例推薦規則。
- 顧問診斷報告模板。
- 範例客戶故事。
- 各部門高價值場景庫。
- n8n 串接 Gmail、Sheets、Notion、CRM、API、ERP 的示範 Workflow。

