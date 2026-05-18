# 公司 AI 使用規範 / Company AI Usage Policy

> 對應課程 / Course: [L1_OPENWEBUI_COURSE_PLAN.md](../L1_OPENWEBUI_COURSE_PLAN.md) §3.4 reference materials
> 版本 / Version: 範本 v1.0（公司填空式 1 頁）/ Template v1.0 (fillable, 1-page)
> 授權 / License: Apache 2.0

---

## 1. 本規範 / This policy

**公司名稱 / Company:** `[填入 / fill in]`
**生效日 / Effective date:** `[填入 / fill in]`
**owner:** `[填入 / fill in，建議 AI Champion / suggest AI Champion]`
**下次 review：** `[填入下個季度 / fill in next quarter]`

---

## 2. 可以做的事 / What's allowed

- ✅ 用 AI 寫 Email / 摘要 / 翻譯 / 報告草稿 / 簡報大綱 / Drafting Email / summary / translation / report / outline
- ✅ 用 AI 校稿、改錯字、改流暢度 / Proofreading
- ✅ 對 **公開資料** 與 **公司內部低敏感資料** 做問答 / Q&A on public + low-sensitivity internal data
- ✅ 用 AI 寫程式 / debug / 註解 / Code / debug / comment
- ✅ 用 AI 學習新主題（不取代你的判斷）/ Learn new topics (not replace your judgment)

## 3. 不可以做的事 / What's NOT allowed

- ❌ 上傳 **客戶 PII**（姓名、身分證、信用卡、地址、電話）/ Upload customer PII
- ❌ 上傳 **員工 PII**（身分證、薪資、人評紀錄、健檢）/ Upload employee PII
- ❌ 上傳 **未公開財務 / 合約 / 定價** / Upload non-public finance / contracts / pricing
- ❌ 直接把 AI 產出 **對外發布**（必須人工確認）/ Publish AI output externally without human review
- ❌ 用個人 ChatGPT / Claude / Gemini 帳號處理 **公司業務** / Use personal accounts for company work
- ❌ 把公司 OpenWebUI 帳號 **共用** 給同事 / Share company account

## 4. 需人工確認（HITL）/ Human-in-the-loop required

- ⚠️ AI 產出對外文案（marketing / PR / 客戶回覆）/ External-facing AI output
- ⚠️ AI 產出含數據的報告 / Reports with numeric data
- ⚠️ AI 寫的 code 部署到 production 前 / Before deploying AI-written code
- ⚠️ AI 翻譯的合約、法律文件 / AI-translated contracts / legal docs

## 5. 機敏資料專屬規則 / Sensitive data rules

| 資料類型 / Data type | 可用工具 / Allowed |
|---|---|
| 客戶 PII | **僅地端模型 / On-prem only**；且需 HITL / + HITL required |
| 員工 PII | **僅 HR Admin** + 地端模型 |
| 財務 / 合約 | **僅授權清單內 + 地端模型** |
| 公司公開資料 | 雲 / 地端皆可 |

## 6. 違規處理 / Violations

| 次數 / Occurrence | 處理 / Action |
|---|---|
| 第 1 次 / 1st | 口頭警告 + 補訓 / Verbal warning + retraining |
| 第 2 次 / 2nd | 書面警告 + 帳號暫停 1 週 / Written warning + 1-week suspension |
| 第 3 次 / 3rd | 依員工守則處理（含解雇可能）/ Per employee handbook (incl. termination) |
| **資料外洩（任 1 次）/ Data breach (any single occurrence)** | **立即帳號停權 + 法務介入 / Immediate suspension + legal review** |

## 7. 求助管道 / Help

- 規範問題 / Policy questions: `[填入 AI Champion / fill in]`
- 帳號問題 / Account issues: `[填入 IT / fill in]`
- 想做但不確定？/ Want to do something but unsure?
  → 寫信給 AI Champion 取得確認 / Email AI Champion for clearance

## 8. 簽署 / Acknowledgment

我已閱讀本規範並同意遵守。/ I have read and agree to comply with this policy.

| 員工姓名 / Employee | 部門 / Dept | 簽名 / Signature | 日期 / Date |
|---|---|---|---|
| | | | |
