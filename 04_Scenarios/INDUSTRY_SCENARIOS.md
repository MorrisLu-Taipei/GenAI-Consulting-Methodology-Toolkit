# 產業推薦場景 / Industry Recommended Scenarios

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

本檔涵蓋 5 個產業之推薦 AI 場景：零售、教育、物流、軟體、專業服務。每個產業含產業簡介、L1-L5 成熟度基線、Top 10 推薦場景、風險與治理、30 天 quick win、anti-patterns。

5 industries: retail, education, logistics, software, professional services. Each section covers industry intro, L1-L5 maturity baseline, Top 10 recommended scenarios, risk & governance, 30-day quick win, and anti-patterns.

---

## 1. 零售 / Retail

### 1.1 產業簡介

零售涵蓋實體連鎖、電商、D2C 品牌。關鍵流程：商品 / 訂單 / 庫存 / 通路 / 會員 / 行銷。受個資法、消保法、金管會 (信用卡) 規範。

Retail spans brick-and-mortar chains, e-commerce, and D2C brands. Key processes: products / orders / inventory / channels / loyalty / marketing. Regulated by personal data protection law, consumer protection law, and FSC for credit-card flows.

**台灣零售 AI 成熟度基線（2026）**：多數企業在 **L1-L2 之間**。少數連鎖品牌已有 L3 PoC（社群輿情、商品文案）。L4-L5 為先驅者。
Most retail enterprises in Taiwan sit between **L1 and L2**. Some chain brands have L3 PoCs (social listening, product copy). L4-L5 are pioneers.

### 1.2 Top 10 推薦場景 / Top 10 Recommended Scenarios

| # | 場景 | 部門 | L | 描述 | 系統 / 資料 | ROI 槓桿 | 複雜度 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| R1 | 店員 AI 助手 (商品 / 庫存查詢) | 門市 | L3 | 店員手機 app 對話查商品、庫存、價格 | POS / WMS / 商品 DB | 時間 | 中 |
| R2 | 商品文案大量生成 | 商品 / 行銷 | L2 | 從商品規格自動產出多語版商品描述 | PIM / Sheets | 時間 + 質量 | 低 |
| R3 | 動態定價建議 | 商品 / 定價 | L4 | 結合競品、庫存、季節給定價區間 | 競品爬蟲 / 庫存 / POS | 營收 | 高 |
| R4 | 退換貨分流與摘要 | 客服 | L3 | 客戶退換貨原因分類、優先處理 | Email / 客服系統 | 時間 + NPS | 中 |
| R5 | 會員忠誠度互動 | 會員 / 行銷 | L3 | 個人化推薦、生日 / 紀念日訊息 | CRM / 訂單 | 營收 | 中 |
| R6 | 補貨建議 (跨店 / 跨倉) | 營運 | L4 | 依銷售速度與安全水位建議補貨 | WMS / POS | 缺料下降 | 高 |
| R7 | 客流分析 (實體店) | 營運 | L4 | 攝影機 + AI 算客流、停留、轉換 | 攝影機 / POS | 營運決策 | 高 |
| R8 | 社群輿情監測 | 行銷 / PR | L3 | FB / IG / Threads / Dcard 品牌提及監測 + sentiment | 社群 API | 風險預警 | 中 |
| R9 | 線上線下庫存同步 | 營運 / IT | L3 | 統一視圖避免超賣 / 缺貨 | OMS / WMS / E-commerce | 營收 + 客滿意 | 中 |
| R10 | 客戶 360 視圖 | 行銷 / 業務 | L4 | 整合線上線下會員資料 + AI 摘要 | CDP / CRM / POS | 營收 + LTV | 高 |

### 1.3 風險與治理

- **個資與支付**：會員資料、信用卡 token 必須 redact 後再進 LLM
- **品牌一致性**：AI 生成文案需 Brand Guidelines reviewer
- **庫存決策**：補貨建議需有人工 Gate，避免 AI 跑量過頭
- **動態定價**：避免歧視性定價（依族群差別待遇）

### 1.4 30 天 Quick Win

> **R2 商品文案 + R8 社群輿情**：兩個低風險、立即見效，員工感受度高。
> R2 (product copy) + R8 (social listening): low-risk, immediate impact, high adoption.

### 1.5 Anti-Patterns

- ❌ 跳過 L1 直接做動態定價（沒有店員 / 商品同事的 trust）
- ❌ AI chatbot 取代客服一線（高敏感互動沒 fallback）
- ❌ 未經 Brand Guidelines 審核就把 AI 文案上架

---

## 2. 教育 / Education

### 2.1 產業簡介

涵蓋 K-12、高等教育、企業培訓、EdTech。受個資法 (學生資料)、教育部規範、智財權 (教材) 影響。

K-12, higher education, corporate training, EdTech. Regulated by personal data law (student records), Ministry of Education rules, and IP (course materials).

**台灣教育 AI 成熟度基線**：L1。少數大學與 EdTech 在 L2-L3。家長與學生對 AI 接受度逐漸提高，但教師抗拒仍強。
Baseline at L1; a few universities and EdTechs at L2-L3. Parent / student acceptance rising, but teacher resistance still notable.

### 2.2 Top 10 推薦場景

| # | 場景 | 對象 | L | 描述 | 系統 / 資料 | ROI 槓桿 | 複雜度 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| E1 | 教師備課草稿 (lesson plan) | 教師 | L2 | 依課綱 + 班級資料草擬教案 | Sheets / 課綱 DB | 時間 | 低 |
| E2 | 學生作業回饋 (formative) | 教師 | L3 | 學生作業 → AI 摘要重點與弱點 | LMS | 時間 + 質量 | 中 |
| E3 | 家長溝通信草擬 | 教師 / 行政 | L2 | 期中報告、突發事件、家長會通知草稿 | Email / 學生 DB | 時間 | 低 |
| E4 | 招生 Q&A (chatbot) | 招生 | L3 | 24/7 招生諮詢，問題自動分流給人工 | 網站 / FAQ | 招生轉換 | 中 |
| E5 | 課程搜尋與推薦 (RAG) | 學生 / 大學 | L4 | 學生問「我想學 X」AI 給課程組合 | 課程 DB | 學生滿意 | 中 |
| E6 | AI 內容檢核 (plagiarism + AI-text) | 教師 | L3 | 學生作業檢測 AI 比例 + 抄襲 | LMS / 第三方 API | 學術誠信 | 中 |
| E7 | 無障礙 (TTS / 翻譯 / 字幕) | 教師 / 學生 | L2 | 課程錄影自動字幕、翻譯、文字朗讀 | LMS | 包容性 | 低 |
| E8 | 評分 rubric 助手 | 教師 | L3 | AI 依 rubric 給初評，教師確認 | LMS | 時間 | 中 |
| E9 | 校友 / 系友互動 | 行政 | L3 | 系友資料更新、活動推薦 | CRM | 募款 + 凝聚 | 中 |
| E10 | 評鑑 / 認證資料整理 | 行政 / 系所 | L4 | 系所評鑑文件自動匯整、佐證連結 | Notion / Drive | 時間 + 質量 | 高 |

### 2.3 風險與治理

- **學生個資**：未成年資料須加強保護；GDPR-K
- **AI 內容檢核**：誤判風險高，需有申訴機制
- **教師專業權威**：AI 不可取代教學決策，需人工最終確認
- **教材智財權**：明確區分教師、學校、AI 廠商之教材所有權

### 2.4 30 天 Quick Win

> **E1 教案草稿 + E3 家長信草擬**：教師工作量最重的兩件，立即減負。
> E1 (lesson plan drafts) + E3 (parent comms): the two heaviest tasks; immediate teacher relief.

### 2.5 Anti-Patterns

- ❌ AI 直接給學生答案而非引導
- ❌ AI 評分未經教師確認就下成績
- ❌ 把 AI 招生 chatbot 當成「永遠不需要人工」

---

## 3. 物流 / Logistics

### 3.1 產業簡介

3PL、貨運、最後一哩、倉儲。關鍵流程：訂單 / 揀貨 / 路由 / 出貨 / 異常處理。受海關、運輸法規影響。

3PL, freight forwarding, last-mile delivery, warehousing. Key processes: orders / picking / routing / shipping / exception handling. Regulated by customs and transportation rules.

**台灣物流 AI 成熟度基線**：L1-L2。少數大型 3PL 在 L3 (路線優化、異常告警)。
Baseline L1-L2; a few large 3PLs at L3 (route optimization, exception alerts).

### 3.2 Top 10 推薦場景

| # | 場景 | 部門 | L | 描述 | 系統 / 資料 | ROI 槓桿 | 複雜度 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| L1-1 | 出貨異常分流 | 客服 / 營運 | L3 | 異常案件 (延誤 / 破損 / 失蹤) 自動分類 | TMS / 工單 | 時間 + NPS | 中 |
| L2-1 | 海關文件草擬 | 報關 | L3 | 從訂單自動產出報關文件草稿 | ERP / 海關規則 | 時間 + 準確 | 中 |
| L3-1 | 路線異常解讀 | 營運 | L4 | 路線偏離 / 延遲 → AI 解釋原因 + 建議 | GPS / TMS | 營運決策 | 高 |
| L4-1 | 司機 app FAQ 助手 | 司機 / IT | L3 | 司機問 app 操作 / SOP / 異常處理 | LMS / 知識庫 | 時間 | 中 |
| L5-1 | 倉儲 SOP 檢索 | 倉管 | L3 | 倉管問 SOP / 安全 / 規則即得答 | Wiki | 時間 + 安全 | 中 |
| L6-1 | 客戶 ETA chatbot | 客服 | L3 | 客戶查貨況自動回覆 + 預測 ETA | TMS / WMS | 客服減負 | 中 |
| L7-1 | 賠償 / 索賠處理 | 客服 / 法務 | L3 | 索賠案件分類、證據檢核、賠償計算 | 工單 / 保險 | 時間 + 準確 | 中 |
| L8-1 | 營運 KPI 每日 digest | 營運主管 | L3 | 每日 8am 主管收到關鍵 KPI 與異常 | TMS / WMS | 主管時間 | 中 |
| L9-1 | 合作夥伴外展 | 業務 / 採購 | L3 | 自動產生招商信、合約初稿 | CRM | 業務時間 | 中 |
| L10-1 | 法規更新追蹤 | 法務 / 海關 | L4 | 各國海關 / 運輸法規變更摘要 | 政府網站 RAG | 風險預警 | 高 |

### 3.3 風險與治理

- **司機隱私**：GPS / 行為資料須限制存取
- **海關 / 法規**：AI 草擬之文件須法務確認，避免誤填造成罰款
- **客戶 ETA 預測**：明示為預測非保證，避免承諾過度

### 3.4 30 天 Quick Win

> **L1-1 異常分流 + L8-1 KPI digest**：營運主管最有感。

### 3.5 Anti-Patterns

- ❌ AI 路線推薦未經調度員確認直接下發
- ❌ 索賠 AI 自動結案不通知人工

---

## 4. 軟體 / Software (B2B SaaS, ISV)

### 4.1 產業簡介

SaaS、地端 ISV、專業服務部門。關鍵流程：產品 / 客戶 / 工程 / 客服 / 業務。本身就是 AI 早期採用者，員工抗拒最低。

SaaS, on-prem ISV, professional services arms. Key processes: product / customers / engineering / support / sales. Themselves early AI adopters with the lowest employee resistance.

**台灣軟體業 AI 成熟度基線**：L2-L3。多數有 Copilot / Cursor / Claude Code 實際使用。L4 Agent 逐漸普及。
Baseline L2-L3; widespread use of Copilot / Cursor / Claude Code. L4 Agents increasingly common.

### 4.2 Top 10 推薦場景

| # | 場景 | 部門 | L | 描述 | 系統 / 資料 | ROI 槓桿 | 複雜度 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| SW1 | 客服工單分類與草稿 | 客服 / CS | L3 | Zendesk / Intercom 工單分類 + 回覆草稿 | 客服系統 | 時間 + FCR | 中 |
| SW2 | 文件自動生成 (from code) | 工程 | L2 | 程式碼註解 + API spec 自動產出 docs | GitHub / Notion | 時間 | 中 |
| SW3 | Release notes 草擬 | PM / 工程 | L2 | 從 commit / PR 自動產 release notes | GitHub | 時間 | 低 |
| SW4 | 客戶流失風險 (churn) 評分 | CS / Product | L4 | 結合 product usage + ticket + 帳單算 churn | 自有資料 | 營收 + LTV | 高 |
| SW5 | CSM 客戶 brief | CS | L4 | CSM 開會前自動 brief：上次互動、開放工單、合約 | CRM / 工單 | 客戶質量 | 高 |
| SW6 | QA 自動 test case 生成 | QA / 工程 | L3 | 從 user story 產出 test case | Jira / TestRail | 質量 + 時間 | 中 |
| SW7 | On-call shift 摘要 | SRE / 工程 | L3 | 每班結束 AI 摘要 incident、決策、todo | PagerDuty / Slack | 知識傳承 | 中 |
| SW8 | 客戶 onboarding plan 生成 | CS | L3 | 依客戶 profile 自動產 onboarding 計畫 | CRM | 時間 + 客戶 NPS | 中 |
| SW9 | Code review 助手 | 工程 | L4 | PR comments 自動建議；不取代 reviewer | GitHub | 質量 + 時間 | 中 |
| SW10 | 合作夥伴 enablement Q&A | 業務 / 通路 | L3 | Partner 問產品功能即得答 (RAG) | Notion / Wiki | Partner 自助 | 中 |

### 4.3 風險與治理

- **客戶資料**：SaaS 多租戶資料須隔離；不同 tenant 不可混用
- **程式碼**：機敏程式碼避免送雲 LLM；可使用 self-host
- **客戶承諾**：AI chatbot 不可給承諾性回答 (SLA / 退費)
- **資安**：AI 生成程式碼仍須通過 SAST / DAST

### 4.4 30 天 Quick Win

> **SW2 文件 + SW3 Release notes**：工程立即減負，無風險。

### 4.5 Anti-Patterns

- ❌ AI 直接 merge PR (繞過 code review)
- ❌ 客戶 chatbot 給含糊承諾
- ❌ 用客戶資料訓練自家模型而未告知

---

## 5. 專業服務 / Professional Services

### 5.1 產業簡介

法律事務所、會計 / 稅務、管理顧問、設計 / 創意。關鍵流程：客戶開發 / 委任 / 交付 / 計費 / 知識管理。受專業倫理 (律師法、會計師法)、客戶機密影響。

Law firms, accounting / tax, management consulting, design / creative agencies. Key processes: BD / engagement / delivery / billing / knowledge management. Regulated by professional ethics codes and client confidentiality.

**台灣專業服務 AI 成熟度基線**：L1-L2。多數合夥人個人在用 ChatGPT / Claude，但組織化採用低。
Baseline L1-L2. Partners use ChatGPT / Claude individually, but organizational adoption low.

### 5.2 Top 10 推薦場景

| # | 場景 | 對象 | L | 描述 | 系統 / 資料 | ROI 槓桿 | 複雜度 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| PS1 | 客戶 intake 摘要 | 律師 / 顧問 | L3 | 諮詢錄音 → 結構化 intake 文件 | Zoom / Whisper / DMS | 時間 + 質量 | 中 |
| PS2 | 合約條款 Q&A (RAG) | 律師 | L4 | 對自家合約模板問「這條怎麼用」 | DMS / Notion | 時間 + 一致性 | 高 |
| PS3 | 工時記錄自動分類 | 全員 | L3 | calendar + email + chat → 工時分類 | Outlook / Slack | 計費準確 | 中 |
| PS4 | 計費 narrative 草擬 | 律師 / 會計 | L2 | 工時條目自動產出客戶可讀 narrative | 計時系統 | 時間 + 客戶滿意 | 低 |
| PS5 | 利益衝突檢核 (conflict check) | 法務管理 | L3 | 新案件對既有客戶 / 對造做衝突檢核 | 客戶 DB | 風險 + 倫理 | 中 |
| PS6 | 提案 RAG (over past work) | BD / 合夥人 | L4 | 對自家過往提案 / 案例做 RAG，給新提案 | DMS | 業務轉換 | 高 |
| PS7 | 交付物 QA | 律師 / 顧問 | L3 | 對交付物做格式 / 引用 / 拼字 / 邏輯檢查 | Word / Notion | 質量 | 中 |
| PS8 | 客戶 onboarding brief | 合夥人 | L4 | 新客戶 → 自動 brief 公開資訊、產業、過往合作 | News / 公開 DB | 時間 + 客戶印象 | 中 |
| PS9 | 知識管理 Agent | 全員 / KM | L4 | 全所知識庫上 Agent 介面，問答 + 引用 | Wiki / DMS | 知識傳承 | 高 |
| PS10 | BD 外展 | 合夥人 / BD | L3 | 依目標客戶產出個人化開發信 | LinkedIn / CRM | 業務 pipeline | 中 |

### 5.3 風險與治理

- **客戶機密**：法律 / 會計資料極敏感；建議 Hybrid 或全地端
- **專業責任**：AI 草擬之意見書須律師 / 會計師確認；不可直接出
- **利益衝突**：AI 衝突檢核不取代正式檢核流程
- **計費準確**：AI 工時 / 計費草稿須律師確認，避免錯帳

### 5.4 30 天 Quick Win

> **PS4 計費 narrative + PS7 交付物 QA**：低風險、高頻、立即見效。

### 5.5 Anti-Patterns

- ❌ 用雲 LLM 處理客戶機密文件未做 redaction
- ❌ AI 草擬意見書直接出客戶
- ❌ 計費 narrative 未確認直接送客戶

---

## 跨產業共通建議 / Cross-Industry Recommendations

### 從哪裡開始 / Where to Start

不論產業，建議：
1. L1 OpenWebUI 全員啟動（治理優先）
2. 找一個「員工每天感受到」的痛點做 L2-L3 PoC
3. 證明 ROI 後再擴展到 L4 Agent
4. 8-12 個月後評估 L5 Agent Team

### 哪裡要小心 / Where to Be Careful

- **跨級錯誤**：不要 L1 還沒打底就推 L4 Agent
- **無 sponsor**：沒高層 commit 的專案 6 個月內必失敗
- **無 reviewer**：AI 產出必須有人簽核機制
- **無 audit log**：法遵與內稽信任你之前必須先看到 audit log
- **無退場機制**：每階段 Stage Gate 不通過要可以 stop，不要硬上

### 引用 / Cite

詳細場景描述見 `CUSTOMER_SCENARIO_LIBRARY.md`；案例見 `SAMPLE_CLIENT_CASE_*.md`；課程見 `02_Course_Design/`。
