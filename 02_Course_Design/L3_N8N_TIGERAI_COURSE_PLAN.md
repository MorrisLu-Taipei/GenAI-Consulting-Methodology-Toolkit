# L3 n8n Workflow AI 課程規劃

版本：v1.1  
作者：Morris  
適用層級：L3 Workflow AI  
參考來源：

- TigerAI YouTube 頻道 n8n / OpenGenie 相關影片  
  頻道：`https://www.youtube.com/@%E8%99%8E%E6%99%BA%E7%A7%91%E6%8A%80TigerAI`
- TigerAI-n8n-Skill-Pack（Morris Lu，TigerAI 自有 + 部分 MIT）：13 個 Skill + 8 cookbook + 2,061 reference workflows，用自然語言生成 n8n workflow JSON，支援 Antigravity + Claude Code + n8n  
  `https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`  
  引用與授權說明見 [`../90_References/N8N_SKILL_PACK_REFERENCE.md`](../90_References/N8N_SKILL_PACK_REFERENCE.md)

---

## 1. L3 重新定位

L3 不是教學員「會拉 n8n node」而已。L3 的真正目標是：

> 從 L2 產出的 Skill / Workflow Blueprint 接手，用 n8n 做出可執行、可驗證、可維運、可備份、可被 L4 Agent 呼叫的企業流程 PoC。

TigerAI 影片呈現的 L3 精神是：

1. 先有 L2 Skill 與 Workflow Blueprint。
2. 用 n8n 把 Trigger、Credential、Data、AI、Platform Action 串起來。
3. 用 Data Tables / Sheets / DB 保存狀態。
4. 用 Sub-workflow 形成可重複使用的流程模組。
5. 用 Execution Log、GitHub 備份、人工 Gate、錯誤處理讓流程可維運。
6. 最後把可用 Workflow 交給 L4 Hermes Agent 呼叫。

### 1.1 L3 課程分上半段與下半段

L3 課程依「先觀念、後生成」原則切成兩段，學員不可跳段：

| 段 | 內容 | 對應課程 | 重點 |
|---|---|---|---|
| **L3 上半段** | n8n / AI workflow 基礎觀念與手動建置 | §5.1 Foundation、§5.2 Builder | 先親手拉過 Trigger / Node / AI / Gate / Log，理解 workflow 的結構與治理 |
| **L3 下半段** | 用 Antigravity (AG) + TigerAI-n8n-Skill-Pack 自然語言生成 workflow | §5.3 Advanced、§5.5 AG + Skill Pack | 在已懂結構的基礎上，用 AI IDE 把自然語言意圖直接生成可部署的 workflow JSON |

> **為什麼先學概念再學 Skill Pack：** TigerAI-n8n-Skill-Pack 能把自然語言「便利貼」直接變成 workflow JSON，但若學員沒先在上半段親手建過 workflow、不懂 Trigger / Credential / Human Gate / Error Handling 的結構，就無法判斷生成結果是否正確、是否安全、是否可維運。**Skill Pack 是加速器，不是替代理解。**

---

## 2. 課程目標

完成 L3 課程後，學員應能：

1. 讀懂 L2 產出的 Workflow Blueprint。
2. 在 n8n 建立 Trigger、Node、Credential、Webhook、Execution。
3. 串接 Gmail、LINE、Facebook、YouTube、Google Sheets、Data Tables、API、CRM、ERP 或其他平台。
4. 使用 Gemini / AI Node 處理文字、圖片、語音、影片、文件。
5. 建立 Sub-workflow，將可重複流程模組化。
6. 建立 Data Tables Schema 或狀態資料表。
7. 設計人工審核 Gate，避免 AI 自動發布高風險內容。
8. 設計錯誤處理、通知、重試、fallback。
9. 將 Workflow 與 Credential 備份到 GitHub 或指定版本庫。
10. 產出可被驗收的 Workflow JSON、Execution Log、測試紀錄與維運 Runbook。

---

## 3. 課前條件

| 項目 | 最低要求 |
|---|---|
| L2 Blueprint | 至少 1 個 Workflow Blueprint，含 trigger、I/O schema、sample payload、human gate |
| n8n 環境 | 可使用 n8n Cloud 或自架環境 |
| 測試帳號 | Gmail、LINE、Facebook、YouTube、Google / Meta / API 測試帳號 |
| Credential | API Key、OAuth、Webhook 權限、測試 token |
| 測試資料 | 去識別化 email、履歷、商品圖、留言、客服問題、查詢資料 |
| 治理規則 | 是否允許自動發文、回覆、外部 API、AI 產圖、影片生成 |
| 備份策略 | GitHub repo 或內部版本庫 |

---

## 4. L3 n8n IPOE

| 類別 | 定義 |
|---|---|
| Input | L2 Workflow Blueprint、trigger event、sample payload、API credential、測試資料、AI prompt、資料表 schema、人工審核規則 |
| Process | 建立 workflow、設定 trigger、讀寫資料、呼叫 AI、格式轉換、串接平台、人工審核、錯誤處理、execution log、備份 |
| Output | n8n Workflow JSON、Data Tables、平台回覆、通知、報表、發文草稿、客服草稿、HR 篩選結果、備份 repo、維運文件 |
| Evidence | Execution Log、測試 payload、輸出截圖、Data Tables / Sheets 紀錄、GitHub backup commit、審核紀錄、錯誤測試紀錄 |

---

## 5. 課程版本

### 5.1 L3 Foundation：3 小時

目標：建立 n8n 基礎與 L2-to-L3 接手能力。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 30 分 | L3 定位 | 從 L2 Blueprint 到 n8n Workflow | L3 共識 |
| 45 分 | n8n 基礎 | Trigger、Node、Credential、Webhook、Execution | 基礎流程 |
| 45 分 | Blueprint 轉換 | trigger、I/O schema、sample payload、node map | 轉換表 |
| 45 分 | AI Node / Gemini | 文字、圖片、文件的 AI 處理 | AI node demo |
| 45 分 | Gate / Log | 人工審核、Execution Log、失敗測試 | Gate / Log 表 |

### 5.2 L3 Builder：1 天

目標：完成一個可驗證的 n8n Workflow PoC。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 60 分 | Trigger 實作 | Webhook、Gmail、LINE、Facebook 或排程 | Trigger node |
| 60 分 | Data handling | Set、Code、Merge、Data Tables、Sheets | Data schema |
| 90 分 | AI processing | Gemini / AI 分類、摘要、草稿、多模態分析 | AI step |
| 90 分 | Platform action | LINE 回覆、Gmail 通知、Facebook 回覆、Sheets / CRM 寫入 | 系統輸出 |
| 60 分 | Human Gate | 發文、回覆、履歷篩選、客服草稿的人工審核 | 審核節點 |
| 60 分 | Error / retry | 錯誤通知、重試、fallback | 錯誤測試 |
| 90 分 | Demo / Review | 用 2 筆正常與 1 筆錯誤 payload 測試 | Execution Log |

### 5.3 L3 Advanced：1 天

目標：補齊企業維運、模組化與治理。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 90 分 | Sub-workflow | 將 AI 分類、通知、審核、寫入資料表模組化 | Sub-workflow library |
| 75 分 | Data Tables | 客服狀態、FAQ、黑白名單、互動紀錄 | Data Tables schema |
| 75 分 | GitHub backup | Workflow / Credential 備份策略 | Backup SOP |
| 60 分 | Credential governance | API Key、OAuth、權限、環境變數 | Credential matrix |
| 60 分 | Monitoring | Execution Log、失敗通知、手動重跑 | 維運表 |
| 90 分 | L4 readiness | 將 workflow 包成 Hermes Agent 可呼叫任務 | Workflow contract |

### 5.4 L3 Enterprise Lab：2 天

目標：使用客戶自己的場景完成一個可交付 PoC。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| Day 1 AM | Use case selection | 從 L2 Blueprint 選一個流程 | PoC Brief |
| Day 1 PM | Build | Trigger、AI、Data、Platform Action | Workflow PoC |
| Day 2 AM | Governance | Human Gate、Log、Error、Backup、Credential | 維運與治理 |
| Day 2 PM | Acceptance | Demo、Execution Log、文件、L4 contract | Gate 3 驗收 |

### 5.5 L3 下半段核心：AG + TigerAI-n8n-Skill-Pack：1 天

> 引用：[`MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack)。完整引用與授權說明見 [`../90_References/N8N_SKILL_PACK_REFERENCE.md`](../90_References/N8N_SKILL_PACK_REFERENCE.md)。
>
> **先修條件：必須先完成 L3 上半段（§5.1 Foundation + §5.2 Builder）**，學員須已親手建過至少 1 個含 Trigger / AI / Human Gate / Error Handling 的 workflow。

目標：在已理解 n8n workflow 結構的基礎上，用 Antigravity（AG）+ TigerAI-n8n-Skill-Pack 把自然語言意圖直接生成可部署、可驗收的 workflow JSON，並學會審查生成結果。

| 時間 | 主題 | 內容 | 產出 |
|---|---|---|---|
| 45 分 | Skill Pack 觀念 | 三層結構（黃色便利貼意圖 + 藍色便利貼註記 + workflow nodes）、DSL v1.2、13 Skills / 8 cookbook / 2,061 reference workflows | Skill Pack 結構筆記 |
| 30 分 | 安裝與設定 | `install.sh` / `install.ps1`、AG 與 Claude Code 整合、n8n 2.10.3+ | 安裝紀錄 |
| 60 分 | Cookbook 模式 | 從 8 個 cookbook recipe 挑模板、用自然語言改寫意圖 | 第 1 個生成 workflow |
| 75 分 | Q&A 生成模式 | AI 引導需求蒐集 → 三層 JSON 生成 → 對照 L2 Workflow Blueprint | 第 2 個生成 workflow |
| 60 分 | 生成結果審查 | 用上半段學到的結構知識檢查：Trigger 對不對？Credential / Human Gate / Error Handling 有沒有？是否可維運？ | 生成結果審查表 |
| 45 分 | Example finder | 從 2,061 reference workflows 找相似實作、比對與借鑑 | 參考實作對照 |
| 45 分 | 部署與驗收 | 透過 n8n API 部署、跑 Execution Log、對齊 Gate 3 | Execution Log + Gate 3 對照 |

#### 5.5.1 治理與紅線

- TigerAI-n8n-Skill-Pack 之 `skills/_vendor/` 與 `reference-workflows/` 為 **MIT**；其餘 Skill / Cookbook / Spec 為 **TigerAI 自有**。引用與再散布請依 [`../90_References/N8N_SKILL_PACK_REFERENCE.md`](../90_References/N8N_SKILL_PACK_REFERENCE.md)。
- **生成不等於驗收**：AI 生成的 workflow 一律須經學員依上半段知識審查，並走 Gate 3A-3G，未過不得宣稱企業級 PoC。
- 機敏資料情境：生成的 workflow 若含 LLM 節點，須改指地端 / Azure OpenAI 隔離 tenant，並前置 redaction。
- reference workflows 已洗去 secrets，但仍須確認沒有殘留的內部端點 / 帳號才可作為範本。

#### 5.5.2 §5.5 Deliverables

- TigerAI-n8n-Skill-Pack 安裝紀錄。
- 至少 2 個用 AG + Skill Pack 生成的 workflow JSON（cookbook 模式 1 個、Q&A 模式 1 個）。
- 生成結果審查表（對照上半段的結構知識）。
- reference workflow 參考實作對照。
- 部署 Execution Log + Gate 3 對照表。

---

## 6. TigerAI 影片對應課程模組

| 課程模組 | 參考影片 | 課程用途 |
|---|---|---|
| L3 入口 | OpenGenie 單元 7：n8n 串接與自動化工作流 | 說明 OpenGenie / OpenWebUI 如何與 n8n 串接 |
| AI Node | n8n 27：Gemini 圖片、語音、影片、文件分析 | AI 多模態處理 |
| Sub-workflow | n8n 28：Sub-workflow 模組化 | 建立可重複流程模板 |
| 查詢 Bot | n8n 29：高鐵時刻查詢機器人 | LINE + API 查詢 |
| HR 流程 | n8n 30：自動履歷篩選 | Gmail + Gemini + LINE 通知 |
| 行銷流程 | n8n 31、32、38、39 | 圖片、文案、關鍵字、影片、社群發布 |
| 社群互動 | n8n 33 | YouTube 留言自動回覆 |
| 維運治理 | n8n 34：GitHub 備份 | Workflow / Credential 備份 |
| 客服流程 | n8n 35、36、37 | Facebook Webhook、Data Tables、圖片與訊息回覆 |
| 管理回饋 | OpenGenie 單元 10 | 監督、回饋、品質改善 |

---

## 7. PoC 案例包

### 7.1 客服自動化 PoC

參考影片：n8n 35、36、37。

流程：

`Facebook / LINE / Email 進件 → Webhook → Data Tables 查 FAQ / 狀態 → AI 產生回覆草稿 → 人工 Gate → 回覆 / 通知 → Log`

交付：

- Webhook Trigger。
- Data Tables Schema。
- AI 回覆 Prompt。
- Human Gate。
- Execution Log。
- 客服主管驗收表。

### 7.2 HR 履歷篩選 PoC

參考影片：n8n 30。

流程：

`Gmail 收履歷 → 附件 / 內文抽取 → Gemini 篩選 → 分數與摘要 → LINE / Email 通知 → Sheets / DB 記錄`

交付：

- 履歷資料 schema。
- 評分規則。
- AI 篩選 Prompt。
- 通知節點。
- 人工審核節點。

### 7.3 行銷自動化 PoC

參考影片：n8n 31、32、33、38、39。

流程：

`商品 / 主題輸入 → AI 找關鍵字 / 圖片 / 文案 / 影片 → 生成草稿 → 人工審核 → 多平台排程發布 → 成效記錄`

交付：

- Content Brief。
- Keyword / image / copy pipeline。
- 發文草稿。
- 人工審核 Gate。
- 多平台發布紀錄。

### 7.4 即時查詢 Bot PoC

參考影片：n8n 29。

流程：

`LINE 問題 → Webhook → API 查詢 → AI 格式化回答 → LINE 回覆 → Log`

交付：

- Webhook URL。
- API query spec。
- 回覆格式。
- 錯誤 fallback。

---

## 8. L3 控制表

| 控制項 | 必填內容 | Evidence |
|---|---|---|
| Workflow 名稱 | `[名稱]` | Workflow Blueprint |
| Business Owner | `[部門 / 人]` | Owner 表 |
| Trigger | `[Webhook / Gmail / LINE / FB / Schedule / API]` | Trigger 測試 |
| Input Schema | `[欄位 / 型別 / 範例]` | Sample payload |
| Credential | `[API Key / OAuth / Token]` | Credential matrix |
| Data Store | `[Data Tables / Sheets / DB / BigQuery]` | Schema / 寫入紀錄 |
| AI Step | `[Gemini / LLM / Prompt]` | AI input/output |
| Platform Action | `[回覆 / 發文 / 寫入 / 通知]` | 輸出截圖 |
| Human Gate | `[審核條件 / 審核人]` | 審核紀錄 |
| Error Handling | `[重試 / 通知 / fallback]` | 失敗測試 |
| Backup | `[GitHub / Repo / 匯出 JSON]` | Backup commit |
| Execution Log | `[成功 / 失敗 / 重跑]` | n8n log |
| L4 Contract | `[Hermes 可呼叫方式]` | Workflow contract |

---

## 9. Stage Gate 3

| Gate | 檢查問題 | 必備 Evidence | 判定 |
|---|---|---|---|
| Gate 3A：Blueprint 可用 | L2 Blueprint 是否完整？ | Trigger、I/O schema、sample payload | Pass / Fail |
| Gate 3B：Workflow 可跑 | n8n Workflow 是否能處理正常 payload？ | Execution Log | Pass / Fail |
| Gate 3C：系統串接可用 | 是否至少串接 2 個系統或平台？ | Node 設定、輸出截圖 | Pass / Fail |
| Gate 3D：AI 處理可驗證 | AI 分類、摘要、草稿或多模態處理是否可檢查？ | AI input/output、測試案例 | Pass / Fail |
| Gate 3E：Human Gate 可用 | 高風險動作是否有人工審核？ | 審核紀錄 | Pass / Fail |
| Gate 3F：維運可用 | 是否有 Log、Error、Retry、Backup？ | 失敗測試、GitHub backup | Pass / Fail |
| Gate 3G：L4 可接 | Hermes Agent 是否能呼叫或引用此 Workflow？ | Workflow contract | Pass / Fail |

未通過 Gate 3F 時，只能算 Demo，不能算企業級 PoC。未通過 Gate 3G 時，可以進行 L3 上線，但不能宣稱已準備好進入 L4。

---

## 10. L3 Deliverables

- n8n Workflow Blueprint。
- n8n Workflow JSON。
- Sub-workflow Library。
- Credential / API / Webhook 權限表。
- Data Tables / Sheets / DB Schema。
- Sample Payload：2 筆正常、1 筆錯誤。
- Execution Log。
- Human Gate 設計。
- Error Handling / Retry / Fallback 設計。
- GitHub Backup / 版本管理 SOP。
- L4 Hermes Agent Workflow Contract。

