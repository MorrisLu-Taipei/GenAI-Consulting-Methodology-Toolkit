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

## 3. 課程目標 / Learning Objectives

> 本節以 [`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](ONLINE_COURSE_DESIGN_METHODOLOGY.md) §4 的 Bloom 公式撰寫：**[動詞] + [內容] + [情境]**，可驗收、可量測。

### 3.1 給 CLP 用的 4 條主 LO（學員選課前看見的承諾）

完成 L1 課程後，學員能夠：

1. **應用** OpenWebUI 的 RBAC 三層架構（Roles / Permissions / Groups），**為自己部門設計** 一份權限矩陣（最小權限 → 群組擴增），**產出** 可審核的 Admin Panel 設定截圖。（Apply）
2. **執行** Email / 會議紀錄 / 摘要 / 報告草稿 4 大高頻工作的 AI 加速流程，**完成** 5 個 Prompt 範本上架到個人 Prompt Library。（Apply）
3. **辨識** AI 輸入資料的 4 個敏感等級（公開 / 內部 / 敏感 / 禁用），**判斷** 何時可貼資料、何時須去識別、何時須人工確認；**產出** 1 頁 AI 使用規範草稿。（Analyze）
4. **產出** L2 Skill 候選清單（≥ 5 個來自實際使用觀察的 Prompt 模式），**驗證** 每個候選具備重複性 + ROI 證據，並按 L2 升級觸發條件排序。（Evaluate）

### 3.2 細部能力清單（章節對應）

每條主 LO 在課中由多個細部能力支撐：

| 主 LO | 對應細部能力 |
| --- | --- |
| LO1（權限） | 完成登入 / 切換模型 / 開新聊天；Admin 能建立帳號、角色、群組；設定模型可見性與功能權限 |
| LO2（高頻工作） | 建立個人聊天區域（資料夾、Prompt、檔案）；使用文件上傳或 Knowledge 做低敏感文件問答；理解模型選擇、參數、幻覺與人工確認 |
| LO3（資料邊界） | 定義可輸入 / 不可輸入 / 須人工確認資料；產出 AI 使用規範與 Gate 1 驗收表 |
| LO4（L2 銜接） | 觀察並記錄 L1 使用模式；對候選做 ROI 評估；交付給 L2 課作為 Skill 候選 |

### 3.3 互動學習設計（Engagement + Formative + Summative）

> 對照 [`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](ONLINE_COURSE_DESIGN_METHODOLOGY.md) §5.1（三幕結構）+ §7（互動類型）+ §9.4（互動 checklist）。

**Engagement activity（開頭 10 分鐘內必須有）：**

> **每人實機登入、開新聊天、選一個模型、用一個 Prompt 完成今天工作中的一件小事**。10 分鐘 hands-on，不講課。目的：把「AI 是抽象概念」變成「AI 就在我面前可以用」的具體體驗。

**Formative gates（章節結尾的快速自我檢核）：**

| 章節 | Formative 檢核 | 時長 |
|---|---|---|
| §6.1 全員使用課每章後 | 1 個 mini-demo：學員當場用 Prompt 完成 1 個高頻工作 | 5 分鐘 |
| §6.2 Admin 課每章後 | 1 個設定截圖比對：學員的 Admin Panel 設定 vs. 標準答案 | 5 分鐘 |
| 資料邊界章節後 | 10 個資料案例判斷題（可輸入 / 須去識別 / 不可輸入） | 10 分鐘 |

**Summative gate（全課程結尾）：**

對應 **Gate 1**（見 §9）。包含 6 個產出：
1. 個人 Prompt Library v1（≥ 5 個 Prompt）
2. 高頻工作完成證據（≥ 3 個 Email / 會議紀錄 / 摘要 / 報告草稿）
3. Admin Panel 設定截圖（角色 + 群組 + 權限 + 模型）
4. AI 使用規範草稿（1 頁）
5. 資料案例判斷表（10 案例 100% 正確）
6. L2 Skill 候選清單（≥ 5 個含 ROI 證據）

### 3.4 Reference materials 清單

對應 [`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](ONLINE_COURSE_DESIGN_METHODOLOGY.md) §9.6（完整性）要求，本課程提供以下可下載素材：

| 類型 | 檔名 / 位置 | 用途 | 狀態 |
|---|---|---|---|
| 使用者操作手冊 | [`_deliverables/L1_USER_OPERATION_MANUAL.md`](_deliverables/L1_USER_OPERATION_MANUAL.md) | login SOP + 模型選擇決策樹 + 檔案上傳 checklist + 資料邊界 10 案例 | ☑ 已加 |
| Admin Runbook | [`_deliverables/L1_ADMIN_RUNBOOK.md`](_deliverables/L1_ADMIN_RUNBOOK.md) | 帳號 / 角色 / 群組 / 權限 / 模型 / 功能完整設定步驟 + Gate 1 驗收 | ☑ 已加 |
| Prompt Library 啟動包 | [`_deliverables/L1_PROMPT_LIBRARY_STARTER.md`](_deliverables/L1_PROMPT_LIBRARY_STARTER.md) | 5 個範例 Prompt + 5 個個人擴充欄 | ☑ 已加 |
| 資料邊界 10 題題庫 | [`_deliverables/L1_DATA_BOUNDARY_QUIZ.md`](_deliverables/L1_DATA_BOUNDARY_QUIZ.md) | 學員 formative quiz（含答案解析） | ☑ 已加 |
| Gate 1 驗收表 | §9（已有 6 項 checklist） | Summative gate 用 | ☑ 已有 |
| AI 使用規範範本 | [`_deliverables/L1_AI_USAGE_POLICY_TEMPLATE.md`](_deliverables/L1_AI_USAGE_POLICY_TEMPLATE.md) | 1 頁公司客製填空 | ☑ 已加 |

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

### 6.0 Lecture Map（依 [`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](ONLINE_COURSE_DESIGN_METHODOLOGY.md) §5.3 切細）

§6.1 / §6.2 / §6.3 三個課程版本的 hour-block 結構在下方各小節列出。本 §6.0 把 §6.1（最常用的全員課）切細到 **3-6 分鐘 / 講座** 等級，作為錄影的直接腳本。§6.2 與 §6.3 的 lecture map 依同 pattern 在錄影前展開。

#### 6.0.1 §6.1 全員使用課 完整 Lecture Map（~50 lectures × 平均 3.6 min = 180 min / 3 hr）

> 講座類型代碼：**TH** = Talking Head（露臉鏡頭）/ **S** = Screencast（螢幕錄影）/ **SL** = Slides / **VS** = Visual / **PR** = Practice 練習 / **QZ** = Quiz / **EN** = Engagement activity / **RC** = Section Recap。

##### Section 0 — Introduction（≤ 10 min）
| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 0.1 | 歡迎來到 L1 OpenWebUI | TH | 3 | 講師自介；為什麼這套課程值得花 3 小時 |
| 0.2 | 你會學到什麼 | TH+SL | 2 | 4 條主 LO 預告（§3.1）+ 課後你會擁有什麼 |
| 0.3 | **Engagement：用 AI 完成今天一件工作** | EN+S | 5 | 學員當場登入 → 開新聊天 → 選模型 → 提示完成一件實際工作 |

##### Section 1 — L1 定位（20 min）
| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 1.1 | 為什麼企業需要統一 AI 入口 | TH | 4 | 個人版 ChatGPT 的 5 個風險（資安 / 一致性 / 治理 / 成本 / 知識留存）|
| 1.2 | 個人 ChatGPT vs 企業級 AI 的差別 | SL | 4 | 5 維對比表 |
| 1.3 | OpenWebUI 的設計哲學 | SL | 4 | RBAC 三層 + Additive Permissions + Open Source |
| 1.4 | L1-L5 成熟度地圖簡介 | SL+VS | 4 | 兩條軸（規模 + AI 自主）視覺化 |
| 1.5 | 完成 L1 你會擁有什麼 | TH | 4 | 6 個 deliverable 預告（§9）|

##### Section 2 — 登入與個人聊天區（30 min）
| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 2.1 | 第一次登入 | S | 3 | 用自己的帳號；不共用 |
| 2.2 | 介面總覽 | S | 4 | 左側欄 / 上方列 / 設定鈕 |
| 2.3 | 開新聊天 | S | 3 | New Chat 按鈕 + 命名習慣 |
| 2.4 | 聊天歷史 + 資料夾 | S | 4 | 拖曳分類 / 搜尋 / 釘選 |
| 2.5 | 個人 Prompt 設定 | S | 5 | Prompt Library 起步：第一個個人 Prompt |
| 2.6 | 個人化設定 | S | 3 | 名字 / 深色 / 語言 |
| 2.7 | 章節 recap | RC | 3 | 5 個重點復習 + 常見錯誤 |
| 2.8 | **Formative：mini-demo** | PR | 5 | 學員當場完成 1 個 Email Prompt + 截圖 |

##### Section 3 — 模型與聊天操作（30 min）
| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 3.1 | 模型選擇器 | S | 4 | 列表 / 切換 / 預設 |
| 3.2 | 重生回答與對話分支 | S | 4 | Regenerate 用法 |
| 3.3 | 續寫與停止 | S | 3 | Continue / Stop |
| 3.4 | 匯出聊天 | S | 3 | 匯出 JSON / Markdown |
| 3.5 | 整理 / 命名 / 標籤 | S | 4 | 維護自己的聊天庫 |
| 3.6 | 封存與刪除 | S | 3 | Archive vs Delete |
| 3.7 | 章節 recap | RC | 3 | 6 個操作要點 |
| 3.8 | **Formative：mini-demo** | PR | 6 | 學員用同一問題切 3 個模型比較回答 |

##### Section 4 — Prompt 基礎（45 min）
| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 4.1 | 好 Prompt 的 5 要素 | SL+VS | 5 | 角色 / 任務 / 背景 / 限制 / 輸出 |
| 4.2 | 範例 1：Email 起稿 | S | 4 | 從 1 句話 → 完整 Email |
| 4.3 | 範例 2：會議紀錄摘要 | S | 4 | 5 點摘要 + Action items |
| 4.4 | 範例 3：主管報告草稿 | S | 4 | 周報 / 月報 |
| 4.5 | 範例 4：FAQ 撰寫 | S | 4 | 客服 / HR 常用 |
| 4.6 | 範例 5：翻譯與校對 | S | 4 | 中英對譯 + 風格選擇 |
| 4.7 | Iterative refinement | TH | 4 | 不滿意怎麼讓它更好 |
| 4.8 | 存到 Prompt Library | S | 4 | 自己的 5 個常用 Prompt |
| 4.9 | 章節 recap | RC | 3 | 5 要素 + 5 範例 + iterative |
| 4.10 | **Formative：寫自己的 5 Prompts** | PR | 9 | 學員當場做 + 互相 review |

##### Section 5 — 日常工作實作（45 min）
| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 5.1 | 場景：英文商務 Email | S | 6 | 含客戶談判 + 同理表達 |
| 5.2 | 場景：30 分鐘會議錄音變 5 點摘要 | S | 6 | 上傳 transcript → 摘要 |
| 5.3 | 場景：客訴回覆 | S | 5 | 同理 + 解決方案 |
| 5.4 | 場景：周報草稿 | S | 5 | 從零碎筆記 → 結構化周報 |
| 5.5 | 場景：簡報大綱 | S | 5 | 客戶提案 / 內部分享 |
| 5.6 | 場景：長文章變 LinkedIn 貼文 | S | 4 | 內容再利用 |
| 5.7 | 場景：競品比較表 | S | 5 | 結構化資料抽取 |
| 5.8 | 章節 recap | RC | 3 | 7 場景 + 部門別應用 |
| 5.9 | **Formative：選 3 個自己場景做** | PR | 6 | 跨部門互助 |

##### Section 6 — 資料邊界（30 min）
| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 6.1 | 3 個資料外洩案例 | SL | 4 | 三星 / Samsung / Air Canada 真實事件改編 |
| 6.2 | 4 個敏感等級 | SL+VS | 5 | 公開 / 內部 / 敏感 / 禁用 視覺化 |
| 6.3 | 判斷流程：3 個問題 | SL+VS | 4 | 流程圖：能不能輸入 |
| 6.4 | 去識別技術簡介 | S | 4 | 替換 PII / 抽象化 |
| 6.5 | 人工確認的時機 | SL | 4 | HITL 必要場景 |
| 6.6 | 章節 recap | RC | 3 | 4 等級 + 3 問題 + 去識別 + HITL |
| 6.7 | **Formative：10 案例 Quiz** | QZ | 6 | 必須 100% 通過 |

##### Section 7 — Conclusion（10 min）
| # | Lecture title | Type | Min | Content / Hook |
| --- | --- | --- | --- | --- |
| 7.1 | 課程回顧 | TH | 3 | 6 個 deliverable 你都有了嗎 |
| 7.2 | 你的 Prompt Library 該長什麼樣 | SL | 3 | 成熟組織的 Prompt Library 範例 |
| 7.3 | L2 銜接預告 | TH | 3 | 把 Prompt 變成 Skill / 把工作變 Workflow |
| 7.4 | 恭喜 + Bonus 資源 | TH | 2 | 結語 + 下一步 |

##### §6.1 lecture type 比例（依 §8.3 建議 TH 30% / S 40% / SL 20% / 其他 10%）

| 類型 | 講座數 | 時間佔比 |
| --- | --- | --- |
| TH（露臉） | 8 | ~ 14% |
| S（螢幕） | 26 | ~ 52% |
| SL（投影片） | 7 | ~ 13% |
| PR / QZ / EN（互動） | 7 | ~ 17% |
| RC（recap） | 6 | ~ 11% |

> ⚠️ Screencast 比例 52% 超過建議的 40% —— 因為 L1 操作密度高，可接受。但實際錄製時，每個 S lecture 前後請穿插 30-60 秒 TH 連接，避免學員看 20 分鐘純螢幕疲勞。

#### 6.0.2 §6.2 Admin / IT 管理課 Lecture Map（stub — 待錄影前展開）

`(同 pattern：6 個 section × 6-8 lectures = ~45 lectures × 平均 4 min = 180 min)`

**Section 結構：** Intro（10 min）→ Admin Panel 總覽 → 帳號登入管理 → 群組權限 → 模型功能控管 → 個人區域分享政策 → Gate 1 驗收 → Conclusion。**展開時參照 §6.0.1 格式。**

#### 6.0.3 §6.3 企業導入工作坊 Lecture Map（stub — 待錄影前展開）

`(1 天 = ~7 小時純講課 = 約 90-100 lectures，但建議切成「上午使用者訓練 + 部門情境」+「下午 Admin 設定 + 治理銜接 L2」兩個半天 mini-course)`

**Section 結構：** AM1 使用者訓練 → AM2 部門情境 → PM1 Admin 設定 → PM2 治理與銜接 L2。**展開時參照 §6.0.1 格式。**

---

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
