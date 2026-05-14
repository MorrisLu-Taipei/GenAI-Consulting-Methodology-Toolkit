# 可填寫問卷規格 / Fillable Questionnaire Specifications

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

把 `AI_MATURITY_QUESTIONNAIRE.md` 內的 10/25/50 題版本，改成可在 Google Form / Tally / Notion Form 直接渲染的 form spec。Schema 同步至 `AI_DIAGNOSIS_SHEETS_SCHEMA.md`。

Renders the 10/25/50-question versions of `AI_MATURITY_QUESTIONNAIRE.md` as form specs for Google Form / Tally / Notion Form. Schema aligns with `AI_DIAGNOSIS_SHEETS_SCHEMA.md`.

---

## 0. 白話化原則（給填答者的設計準則）

填這份表單的多半是**非技術背景的部門主管**，所以表單渲染時務必遵守：

1. **每一題都要帶「說明文字 / help text」**——用白話講清楚這題在問什麼，附一個情境舉例。Google Form 用「題目說明」、Tally 用「question description」、Notion Form 用 hint。
2. **表單開頭放「名詞小辭典」連結或摺疊區塊**——直接引用 `AI_MATURITY_QUESTIONNAIRE.md` §1.2 的 24 個術語白話解釋（OpenWebUI、n8n、Skill、Agent、API、CRM/ERP/MES/PLM/QMS、Hybrid、Stage Gate…）。
3. **開頭加「給填答者的話」**：不需懂技術名詞、不確定就往低分打、這是健檢不是考試。
4. 技術縮寫第一次出現時，在 help text 內就地解釋，不要假設填答者懂。

---

## 共通設定 / Common Settings

| 欄位 | 內容 |
| --- | --- |
| 表單語言 / Language | 預設中文，提供 EN 版開關 |
| 答題量尺 / Scale | 0-4（0=完全沒有，4=已制度化並有 Gate）|
| 說明文字 / Help text | **每題必附**白話 help text（見 §0 原則）|
| 名詞小辭典 / Glossary | 表單開頭引用 `AI_MATURITY_QUESTIONNAIRE.md` §1.2 |
| 必填欄位 | 全題必填；空值不計分 |
| 提交收件 / On-submit | Google Sheets `Raw Responses` + n8n webhook |
| 隱私 / Privacy | 不蒐集 IP；email 加密儲存 |
| Branding | Tiger AI logo + Apache 2.0 footer |

---

## A. 10 題版（業務開發快速診斷）/ 10-Question Version (Quick Diagnostic for Sales)

### Form intro

> 10 題、約 3 分鐘。協助您快速看出企業 AI 成熟度落點 (L1-L5)。每題下面都有白話說明，**不需要懂技術名詞**；不確定就往低分打。填寫後 24 hr 內收到客製化解讀。
> 10 questions, ~3 minutes. Quickly see your enterprise AI maturity level. Every question has a plain-language note — **no technical knowledge needed**; when unsure, score lower. Custom report delivered within 24 hours.

### Page 1：基本資料 / Profile (4 questions)

- P1 公司名稱 / Company name — short text
- P2 您的角色 / Your role — radio: CEO / COO / CIO·IT / Dept head / Other
- P3 公司規模 / Size — radio: <50 / 50-300 / 300-1000 / 1000+
- P4 產業 / Industry — radio: manufacturing / hospital / retail / financial / gov / software / pro-services / other

### Page 2：六大構面 (10 questions, each scale 0-4)

| Q | 題目 | 構面 | 白話說明文字（help text，渲染在題目下方）|
| --- | --- | --- | --- |
| Q1 | 我們員工普遍每天使用 AI 工具完成工作 | 工具使用 | 不是「有人會用」，而是多數同仁每天都會用 AI 處理工作。0＝幾乎沒人用；4＝跨部門天天用、已成日常。 |
| Q2 | 員工的 Prompt 與經驗有集中整理 | 知識沉澱 | 好用的問法與經驗有沒有集中存放、大家共用，而不是鎖在個人腦袋裡。Prompt＝你給 AI 的指令或問法。 |
| Q3 | 我們有定義「什麼是好的 AI 使用方式」 | 流程標準化 | 公司有沒有講清楚「什麼算是好的、安全的 AI 用法」——哪些能做、哪些不能做。 |
| Q4 | AI 已串接我們至少一個企業系統 (Gmail / Sheets / CRM / ERP) | 系統整合 | AI 有沒有真的接上公司系統自動讀寫資料，而不是只在對話框單獨使用。看不懂 Gmail/Sheets/CRM/ERP 可看表單開頭的名詞小辭典。 |
| Q5 | 我們有可重複呼叫的 AI Skill 或 Workflow | Agent 應用 | 有沒有把常做的任務打包成可重複套用的 Skill，或設定成自動跑的流程 (Workflow)，而不是每次都重做。 |
| Q6 | 我們有 AI 使用規範與 Audit 機制 | 治理 ROI | 用 AI 有沒有「規則＋紀錄」：哪些資料能用、誰能用、AI 做了什麼有沒有留紀錄可稽核。 |
| Q7 | AI 對我們的工作效率有具體可量化成果 | ROI | AI 帶來的效率提升能不能用數字講出來（省多少時間、少多少錯誤），而不是「感覺有用」。 |
| Q8 | 我們有 AI 升級的清楚下一步 (而非靠工具廠商) | 戰略 | 公司知不知道 AI 的下一步要往哪走，而不是廠商賣什麼就用什麼。 |
| Q9 | 主管會定期檢視 AI 導入進度 | 治理 | 主管有沒有定期回頭看 AI 導入的進度與成效，而不是導入後就不管了。 |
| Q10 | 我們對 AI 風險 (資安、合規、幻覺) 有具體防護 | 治理 | 對 AI 的風險——資料外洩、不合規、AI 講錯話 (幻覺)——有沒有具體防護措施，而不是沒想過。 |

### Submit page

> 提交完成。我們將在 24 小時內 email 您的 AI 成熟度初步報告與建議。
> Submitted. Initial maturity report & recommendations will be emailed within 24 hours.

### What happens next

> 1. 自動計分 → 等級判定 (L1-L5)
> 2. 業務聯繫安排 30 分鐘 1-on-1 解讀
> 3. 客製化提案（一日工作坊 / 二日營 / 顧問專案）

---

## B. 25 題版（課前診斷）/ 25-Question Version (Pre-Course Diagnostic)

### Form intro

> 25 題、約 8 分鐘。比 10 題版更深入：每個構面 4-5 題。建議在 L1 課程開課前 1 週由全公司主管填寫。每題附白話說明，名詞看不懂請參考表單開頭的名詞小辭典。
> 25 questions, ~8 minutes. Deeper than 10-Q: 4-5 questions per construct. Recommended to be completed by managers one week before L1 course delivery. Every question has a plain-language note.

> **白話化備註**：本版每題的 help text 直接引用 `AI_MATURITY_QUESTIONNAIRE.md` §3 對應題目的「白話＋例如」一行；渲染時務必帶上，不要只放裸題目。

### Page 1：基本資料 (5)

P1-P4 同上 + P5 您的部門 / Your department

### Pages 2-7：六大構面 × 4-5 題

**Page 2 (工具使用 Tool Usage)** — Q1-Q4
- Q1 員工每週使用 AI 的頻率
- Q2 公司有採購的 AI 工具種類
- Q3 員工是否共用 AI 帳號（負向：得分倒置）
- Q4 員工是否在會議 / 報告中明示「AI 協作」

**Page 3 (知識沉澱 Knowledge Codification)** — Q5-Q8
- Q5 是否有 Prompt Library（共用的提示詞庫）
- Q6 是否有定期匯整 Skill / Workflow
- Q7 經驗豐富員工的 AI know-how 是否被書面化
- Q8 是否有 AI 新人 onboarding 流程

**Page 4 (流程標準化 Process Standardization)** — Q9-Q12
- Q9 是否有 SOP 定義 AI 使用範圍
- Q10 是否有 review 機制（人工 Gate＝人來確認的關卡）
- Q11 高頻使用情境是否變成可重複流程
- Q12 是否有跨部門 AI 流程

**Page 5 (系統整合 System Integration)** — Q13-Q16
- Q13 AI 是否串 Gmail / Outlook
- Q14 AI 是否串 Google Sheets / Notion
- Q15 AI 是否串 CRM (HubSpot / Salesforce)
- Q16 AI 是否串 ERP / 內部 API

**Page 6 (Agent 應用 Agent Application)** — Q17-Q20
- Q17 是否有 Agent 自動執行多步驟任務
- Q18 Agent 是否有 Wiki / 記憶
- Q19 Agent 是否有 Reviewer / Human Gate
- Q20 是否有多 Agent 協作 (Agent Team)

**Page 7 (治理 ROI Governance + ROI)** — Q21-Q25
- Q21 是否定義 AI 使用權限矩陣
- Q22 是否有 Audit Log（使用稽核紀錄）
- Q23 是否定義機敏資料 redact 規則（自動遮蔽敏感欄位）
- Q24 是否有 AI ROI 追蹤 KPI
- Q25 主管是否定期 review AI 成果

### Skip logic

- 若 Q1 ≤ 1（工具使用很低）→ 跳過 Q17-Q20（Agent 題）
- 若 Q15 = 0 且 Q16 = 0 → 跳過 Q12（跨部門流程題）

### Submit + What's next

> 您的報告會於 3 工作天內由顧問解讀後寄出。
> Consultant-reviewed report within 3 working days.

---

## C. 50 題版（顧問訪談前完整盤點）/ 50-Question Version (Full Pre-Interview Inventory)

### Form intro

> 50 題、約 20 分鐘。建議在顧問訪談前由 IT / AI Champion 完成。涵蓋六構面 + 部署模式 + 系統盤點 + 治理。技術題較多，可由 IT 窗口協助；每題仍附白話說明。
> 50 questions, ~20 minutes. Completed by IT / AI Champion before the consulting interview. Covers 6 constructs + deployment mode + systems inventory + governance.

> **白話化備註**：G（部署模式）、H（系統盤點）兩組技術名詞最多，help text 直接引用 `AI_MATURITY_QUESTIONNAIRE.md` §4 對應的「白話與舉例」欄。

### Page Structure

| Page | 範圍 | 題數 |
| --- | --- | --- |
| 1 | Profile + Industry + Size + Deployment preference | 8 |
| 2 | 工具使用（含哪些工具、誰用、頻率）| 7 |
| 3 | 知識沉澱 | 7 |
| 4 | 流程標準化 | 7 |
| 5 | 系統整合（含 12 個系統 yes/no + integration depth）| 8 |
| 6 | Agent 應用 | 6 |
| 7 | 治理 ROI + Audit + Compliance | 7 |
| Submit | | 50 |

### Skip logic

- Q-Profile.industry = "manufacturing" → 額外題：MES / SPC / WMS 系統
- Q-Profile.industry = "hospital" → 額外題：HIS / EMR / LIS / PACS
- Q-deployment = "on-prem" → 額外題：GPU、Llama、機房 capacity

### Bonus 開放問答 / Optional open questions

- O1 您目前最大的 AI 痛點？
- O2 過去 12 個月最成功的 AI 案例？
- O3 過去 12 個月最失敗的 AI 案例？
- O4 對顧問訪談最希望討論的議題？

### Output → 八階段顧問 Stage 1 訪談前 brief

自動把 50 題答案 + 開放回答整理成 markdown，顧問訪談前 1 hr 收到 brief，包含：
- AI Usage Inventory (auto-populated)
- Systems Inventory (auto-populated)
- 推測痛點 (auto from low-score constructs)
- 訪談重點建議

---

## D. 平台 Render 提示 / Platform Rendering Hints

### Google Form
- Profile 用 `Section header` 拆 page
- 0-4 量尺用 `Linear Scale`
- 白話 help text 用每題的「題目說明」欄
- Skip logic 用 "Go to section based on answer"
- 結果寫入 connected Sheet → trigger Apps Script → 寄報告

### Tally
- 更彈性的 logic / 多語切換 / Webhook 內建
- 白話 help text 用 question description；名詞小辭典可用摺疊區塊
- 推薦：n8n webhook node 直接 listen Tally submit

### Notion Form (Beta)
- 直接寫入 Notion Database
- 白話 help text 用 question hint
- 用 Notion Automation 觸發 page 創建
- 適合 Notion-first 客戶

---

## E. 啟用流程 / Onboarding for a Client

1. 顧問建立客戶專屬 Form (copy template)
2. 設定 client logo + email subject
3. 連到客戶 n8n 實例的 webhook
4. 客戶 IT 確認 webhook URL whitelist
5. 業務寄送 form 連結給目標填答者
6. 監看 n8n `aid_runs` Data Table，確認流入正常
7. 客戶填寫完成 → 自動報告 → 顧問解讀 → 1-on-1

完整 schema 與 n8n 流程：見 `AI_DIAGNOSIS_SHEETS_SCHEMA.md`。
