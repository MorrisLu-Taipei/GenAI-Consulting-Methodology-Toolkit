# L1 資料邊界判斷題庫 / L1 Data Boundary Quiz Bank

> 對應課程 / Course: [L1_OPENWEBUI_COURSE_PLAN.md](../L1_OPENWEBUI_COURSE_PLAN.md) §3.3 Formative gate + §6.1 Section 6
> 版本 / Version: 範本 v1.0（10 題；客戶可加自家情境）/ Template v1.0 (10 questions; clients can add own scenarios)
> 授權 / License: Apache 2.0

## 使用方式 / How to use

- 每題 4 選 1 / Each question is multiple-choice (1 of 4)
- 滿分 10 分 / 10 points total
- ≥ 9 / 10 才算通過 Formative gate / ≥ 9 / 10 to pass formative gate
- 答錯題目要 **看完原因後重答** / Wrong answers require **review and retake**

---

## Q1：客戶 A 的訂單金額 / Customer A's order amount

A. 可貼到雲端 AI / OK to paste to cloud AI
B. 可貼到地端 AI / OK to paste to on-prem AI
C. **只能去識別化後** 才能用任一 AI / **Must de-identify** before any AI
D. 任何狀況都不可用 AI / Never use AI in any condition

<details><summary>答案 / Answer</summary>

**C.** 客戶 PII（含訂單金額）算敏感。可去識別化（改成「客戶 X 訂單 50 萬」）後用 AI 分析趨勢。/ Customer PII (incl. order amounts) is sensitive. After de-identification ("Customer X order 500K"), AI analysis is OK.
</details>

---

## Q2：自己寫到一半的 LinkedIn 貼文要 AI 校稿 / Own draft LinkedIn post for AI proofreading

A. 不可，社群文都不能給 AI / No, no social posts to AI
B. **可，這是對外公開內容** / OK, this is public content
C. 要 HITL 才能用 AI / Requires HITL
D. 只能用地端 AI / Only on-prem AI

<details><summary>答案 / Answer</summary>

**B.** 你自己寫的對外內容 + 還沒發布 + 沒含他人 PII → 安全範圍。/ Own outbound content + not yet published + no PII of others → safe range.
</details>

---

## Q3：信用卡號要做格式整理 / Credit card numbers for formatting

A. 可，AI 只是處理格式 / OK, AI just formats
B. **絕對不可** / Absolutely no
C. 用地端 AI 就好 / On-prem AI fine
D. 去掉中間 8 碼再貼 / Mask middle 8 digits

<details><summary>答案 / Answer</summary>

**B.** PCI DSS 規範下，完整信用卡號不得貼到任何非合規工具（含地端 AI）。/ Under PCI DSS, full card numbers cannot be pasted to any non-compliant tool (incl. on-prem AI).
</details>

---

## Q4：去年公開的年報摘要 / Last year's published annual report summary

A. **可，公開資料** / OK, public data
B. 不可，公司內部資料 / No, internal data
C. 要 HITL / Requires HITL
D. 只能用地端 / On-prem only

<details><summary>答案 / Answer</summary>

**A.** 已公開的年報是公開資料。/ Published annual reports are public.
</details>

---

## Q5：同事的離職原因（人資紀錄）/ Colleague's resignation reason (HR record)

A. 可，內部資料 / OK, internal
B. 去名字後可 / OK after removing name
C. **絕對不可** / Absolutely no
D. 用地端 AI 就好 / On-prem fine

<details><summary>答案 / Answer</summary>

**C.** 員工 PII + 敏感人事紀錄 + 你無權限存取 → 不可。/ Employee PII + sensitive HR + you have no access → no.
</details>

---

## Q6：競品的公開定價（網站抓的）/ Competitor's public pricing (scraped from website)

A. **可，公開資料** / OK, public
B. 不可，有 NDA 風險 / No, NDA risk
C. 要 HITL / Requires HITL
D. 用地端 AI 才安全 / On-prem only

<details><summary>答案 / Answer</summary>

**A.** 公開網站抓的定價 = 公開資料。但若是客戶在 NDA 下給你的 → 走 NDA 規範。/ Publicly scraped pricing = public. But if obtained under NDA → follow NDA terms.
</details>

---

## Q7：會議錄音轉文字後要摘要 / Meeting transcript for summarization

A. 可，AI 只看文字 / OK, AI just sees text
B. 不可，有他人聲音 / No, contains others' voices
C. **看內容**：若含客戶 PII 或機敏資料 → 不可；否則可 / **Depends on content**: if PII / sensitive → no; else OK
D. 一律用地端 / Always on-prem

<details><summary>答案 / Answer</summary>

**C.** 會議 transcript 內容差異大。需檢查含不含 PII / 機密 / NDA 內容。/ Meeting transcripts vary widely. Check for PII / confidential / NDA content.
</details>

---

## Q8：把 AI 寫的 marketing 文案直接 post / Direct-post AI-written marketing copy

A. 可，AI 寫得很好 / OK, AI writes well
B. **不可，必須人工確認** / No, requires human review
C. 同事看一眼就可 post / Colleague glance is enough
D. 只 post 100 字以下的 / Only short posts

<details><summary>答案 / Answer</summary>

**B.** 對外發布 AI 產出 = HITL 必要。/ External publishing of AI output = HITL required.
</details>

---

## Q9：員工內訓投影片要重做 / Internal training slides for redesign

A. **可，內部低敏感** / OK, internal low-sensitivity
B. 不可，公司資料 / No, company data
C. 要 HITL / Requires HITL
D. 只能用地端 / On-prem only

<details><summary>答案 / Answer</summary>

**A.** 內訓材料通常低敏感。但若含人評紀錄、薪酬資訊等敏感內容 → 升級到 HITL。/ Internal training usually low-sensitivity. Upgrade to HITL if contains evaluation / compensation data.
</details>

---

## Q10：客戶說「我們在用 SAP」要 AI 整理 / Client mentions "We use SAP", asking AI to organize info

A. **可，這是業界資訊不是 NDA** / OK, this is industry info not NDA
B. 不可，提到客戶名 / No, mentions client name
C. 一定要去客戶名 / Must remove client name
D. 只能用地端 / On-prem only

<details><summary>答案 / Answer</summary>

**A.** 客戶提到使用通用商業軟體不算 NDA 內容。但若客戶的 **使用方式 / 客製 / 整合架構** 屬於 NDA 範圍 → 不可揭露細節。/ Mentioning use of mainstream commercial software is not NDA. But the client's **specific usage / customization / integration** under NDA → don't disclose.
</details>

---

## Quiz 結果 / Quiz Results

| 學員姓名 / Learner | 答對題數 / Correct | 通過 / Pass | 重答題目 / Retake | 日期 / Date |
|---|---|---|---|---|
| | / 10 | ☐ | | |

> 講師可加 10 題自家產業情境題作為 Part 2。/ Instructor can add 10 industry-specific cases as Part 2.
