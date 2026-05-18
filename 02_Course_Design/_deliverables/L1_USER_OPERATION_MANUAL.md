# L1 OpenWebUI 使用者操作手冊 / L1 OpenWebUI User Operation Manual

> 對應課程 / Course: [L1_OPENWEBUI_COURSE_PLAN.md](../L1_OPENWEBUI_COURSE_PLAN.md) §10 Deliverables
> 版本 / Version: 範本 v1.0（學員 / 客戶填空式）/ Template v1.0 (fillable by learner / client)
> 授權 / License: Apache 2.0（同 toolkit / same as toolkit）

## 0. 本手冊定位 / Purpose

讓 **不熟 AI 的同事** 在 10 分鐘內能獨立完成「登入 → 開新聊天 → 選模型 → 用 Prompt 完成 1 件工作 → 安全結束」。
Enable **AI-unfamiliar colleagues** to independently complete "login → new chat → select model → complete 1 task with a prompt → safely exit" in 10 minutes.

---

## 1. 登入 SOP / Login SOP

### 步驟 / Steps

| # | 動作 / Action | 預期結果 / Expected |
|---|---|---|
| 1 | 開瀏覽器到 `[公司 OpenWebUI 網址]` / Open browser to `[company OpenWebUI URL]` | 看到登入畫面 / Login screen appears |
| 2 | 輸入公司 email + 密碼（或 SSO）/ Enter company email + password (or SSO) | 進入聊天主畫面 / Enter main chat screen |
| 3 | 確認左上角顯示自己的名字 / Confirm your name in top-left | 已登入自己的帳號 / Logged in as yourself |

### 第一次登入要做的 3 件事 / 3 things on first login

- [ ] 設定個人化（名字、深色、語言）/ Set personalization (name, dark mode, language)
- [ ] 建立第一個資料夾「日常工作」/ Create first folder "Daily Work"
- [ ] 設定 1 個個人 Prompt 「翻譯成中文」/ Add 1 personal Prompt "Translate to Chinese"

### 常見問題 / Common issues

| 問題 / Issue | 解法 / Solution |
|---|---|
| 無法登入 / Cannot log in | 確認帳號是否已被 Admin 開通；聯絡 `[IT 窗口 / IT contact]` |
| 沒看到模型 / No model shown | 檢查群組權限；聯絡 Admin |
| 介面是英文 / UI is English | 右上頭像 → Settings → Language |

---

## 2. 模型選擇決策樹 / Model Selection Decision Tree

```text
你今天的任務是？/ What's today's task?

├─ 寫 Email / 摘要 / 翻譯（純文字、短）/ Email / summary / translation (short text)
│  → 選預設模型 / Use default model
│
├─ 長文章分析 / 多段邏輯（純文字、長）/ Long-text analysis / multi-step logic
│  → 選 large-context 模型（如 Opus / Gemini 1.5 Pro）/ Use large-context model
│
├─ 圖片分析 / OCR / Image analysis / OCR
│  → 選多模態模型（Claude Sonnet / GPT-4o / Gemini）/ Use multimodal model
│
├─ 程式碼 / Code
│  → 選 coding 強的模型（Claude Sonnet / Codex / DeepSeek）/ Use coding-specialized model
│
└─ 機敏資料（PII / 客戶資料）/ Sensitive data (PII / customer data)
   → 一律用本地 Ollama 模型 / Always use local Ollama model；不能用雲端 API / no cloud API
```

> **預設原則：** 不確定時用「公司預設模型」。/ **Default rule:** when in doubt, use "company default model."

---

## 3. 檔案上傳 Checklist / File Upload Checklist

### 上傳前必檢 / Pre-upload checks

- [ ] 檔案 **不含** 公司機密（合約、定價、客戶 PII）/ File **does NOT** contain confidential data (contracts, pricing, customer PII)
- [ ] 檔案 **不含** 個人隱私（同事姓名電話 email）/ File **does NOT** contain personal privacy (colleague names, phones, emails)
- [ ] 檔案 **大小** ≤ 公司設定上限（預設 25MB）/ File **size** ≤ company limit (default 25MB)
- [ ] 檔案 **格式** 為允許清單內：PDF / docx / xlsx / md / csv / txt
- [ ] 檔案 **用完即刪**：使用後從聊天中刪除附件 / File **deleted after use**: remove attachment from chat after done

### 上傳後驗證 / Post-upload verification

1. 在聊天問：「總結這份文件 3 句話」/ Ask "Summarize this in 3 sentences"
2. 確認 AI 回答**只引用文件內容**，沒有掰造 / Confirm AI **only cites the doc**, no hallucination
3. 不確定時請求**引用原文段落**：「請引用第幾頁第幾段」/ When unsure, request citation: "Cite which page, which paragraph"

---

## 4. 資料邊界 10 案例判斷 / 10 Data Boundary Cases

學員必須 **全部判斷正確** 才算通過 Formative gate。/ Learner must answer **all 10 correctly** to pass formative gate.

| # | 情境 / Scenario | 可輸入？ / Inputtable? | 為什麼 / Why |
|---|---|---|---|
| 1 | 公司去年公開的年報 / Company's published annual report from last year | ✅ 可 / Yes | 公開資料 / Public |
| 2 | 同事的離職原因（人資紀錄）/ Colleague's resignation reason (HR record) | ❌ 不可 / No | PII + 敏感 / PII + sensitive |
| 3 | 客戶 A 的訂單金額 / Customer A's order amount | ❌ 不可 / No | 客戶資料 / Customer data |
| 4 | 寫好的 marketing 文案要校稿 / Draft marketing copy for proofreading | ✅ 可 / Yes | 對外用內容 / Outbound content |
| 5 | 信用卡號要做資料整理 / Credit card numbers for data cleanup | ❌ 絕對不可 / Absolutely no | PCI 規範 / PCI regulation |
| 6 | 會議錄音 transcript 要摘要 / Meeting transcript for summary | ⚠️ 需確認 / Requires check | 視內容敏感度 / Depends on content |
| 7 | 公開新聞稿要翻譯 / Public press release for translation | ✅ 可 / Yes | 公開 / Public |
| 8 | 競品價格表（客戶給的）/ Competitor pricing (from client) | ⚠️ 需確認 / Requires check | NDA 範圍 / NDA scope |
| 9 | 員工身分證號 / Employee ID number | ❌ 絕對不可 / Absolutely no | 個資法 / Personal data law |
| 10 | 自己寫到一半的周報 / Own half-written weekly report | ✅ 可 / Yes | 自己的工作 / Own work |

> **判斷流程 / Decision flow：** (1) 含 PII 嗎？/ Contains PII? (2) 是公司機密嗎？/ Is it confidential? (3) 跨 NDA 嗎？/ Cross NDA? → 任一是 = 不可或需 HITL / Any yes = no or HITL required.

---

## 5. 安全結束 / Safe Exit

| # | 動作 / Action |
|---|---|
| 1 | 重要對話**命名 + 釘選**或匯出存檔 / Important chats **named + pinned** or exported |
| 2 | 含機敏資料的聊天**刪除** / Chats containing sensitive data **deleted** |
| 3 | 共用電腦：登出 / Shared computer: log out |
| 4 | 個人電腦：直接關瀏覽器 / Personal computer: just close browser |

---

## 6. 求助管道 / Help Channels

- IT 窗口 / IT contact: `[填入 / fill in]`
- AI Champion: `[填入 / fill in]`
- 公司 AI 規範 / Company AI policy: `[連結 / link]`
- 內部社群 / Internal community: `[Slack / Teams 頻道 / channel]`
