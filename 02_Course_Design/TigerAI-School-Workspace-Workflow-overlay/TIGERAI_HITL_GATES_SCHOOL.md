# Tiger AI 校園 HITL Gate 設計 / Tiger AI School HITL Gate Design

> 🌐 中英雙語 / Bilingual inline
> HITL = Human-in-the-Loop（人類在迴圈內審核）

## 0. 為什麼校園 HITL 規格比一般企業嚴 / Why school HITL is stricter than enterprise

| 因素 / Factor | 學校特殊性 / School specificity |
|---|---|
| **對象多為未成年** | 學生資料受個資法 / 兒少法雙重保護 |
| **家長期待高** | 家長對 AI 介入學校事務的容忍度低 |
| **政府監管嚴** | 教育部 / 縣市教育局有具體規範 |
| **錯誤後果重** | 一封錯誤的家長通知可能引發退費 / 投訴 / 媒體報導 |
| **教師接受度差異大** | 同一校內教師對 AI 的態度從「擁抱」到「拒絕」都有 |

**核心原則：在學校，HITL 從來不是「為了保險」，而是「為了讓 AI 真的能上線」。沒 HITL = 沒辦法上線。**
**Core principle: in schools, HITL is not "for insurance" — it's "what enables AI to launch at all." No HITL = no launch.**

---

## 1. 四大類 HITL Gate / Four HITL Gate Categories

### 1.1 公文簽核 HITL / Document Routing HITL

**情境：** 校內公文走 AI 自動路由（如教師請假單、活動申請、物資請購）
**Scenario:** School internal docs auto-routed via AI

**HITL 設計：**

| 階段 / Stage | AI 做 | 人做 |
|---|---|---|
| 收件 / Intake | AI 檢查必填欄位 + 格式 | — |
| 路由 / Routing | AI 自動找下一個簽核者 | — |
| 簽核 / Approval | — | **每一站簽核者必須親點「同意 / 退回 / 修改」**，AI 不可代簽 |
| 通知 / Notification | AI 起草通知文字 | 主任最後審 1 句並按送出 |
| 歸檔 / Archive | AI 自動歸到正確資料夾 | — |

**紅線（任 1 觸發 = 立刻人審）：**
- 申請金額 > NT$5,000
- 涉及多個處室
- 申請人是新進教師（< 1 學期）
- 申請類別是「特別」/「緊急」/「機密」

### 1.2 學生資料處理 HITL / Student Data Processing HITL

**情境：** AI 處理學生作業、評量、輔導紀錄、出缺勤
**Scenario:** AI processing student assignments, assessments, counseling, attendance

**HITL 設計：**

| 階段 | AI 做 | 人做 |
|---|---|---|
| 上傳資料 | AI 自動去識別化（替換姓名為「學生 A」） | 教師確認去識別化結果 |
| 評語草擬 | AI 給每位學生個別化評語草稿 | **每份評語必須教師親自審 + 微調 + 送出** |
| 輔導建議 | AI 從資料中找趨勢、給建議 | **建議只給輔導教師參考，不對學生 / 家長直接呈現** |
| 統計報告 | AI 出班級層級統計 | 教師審後送主任 |

**絕對紅線（任 1 觸發 = AI 立刻停止、人接手）：**
- 學生資料含「自殺 / 自傷 / 受虐 / 家庭問題」關鍵字 → **AI 不處理，直接 alert 輔導室主任**
- 學生有特教 / 身障身份 → AI 處理但**評語必須特教老師審**
- AI 評語 confidence < 0.7 → 不出草稿，直接交白卷給老師寫

### 1.3 對外公告 HITL / Outbound Public Announcements HITL

**情境：** AI 草擬校網公告、家長通知信、學校 FB 貼文、媒體新聞稿
**Scenario:** AI drafting school website notices, parent emails, FB posts, press releases

**HITL 設計：**

| 階段 | AI 做 | 人做 |
|---|---|---|
| 草擬 | AI 出多版草稿（正式版 / 友善版 / 簡短版）| 行政組長選一版 |
| 校稿 | AI 文法檢查 + 政治正確檢查 | **教務 / 學務主任親自審** |
| 多語版本 | AI 出英 / 越 / 印 / 泰版（如校內有外籍家長） | 各語版需該語言能力者審 |
| 送出 | — | **必須校長 / 教務主任親自按「發布」** |

**絕對紅線（任 1 觸發 = 校長親簽）：**
- 涉及學生個人事件（霸凌、意外、表揚個人）
- 涉及學校危機（停課、緊急疏散、財務問題）
- 涉及政治 / 宗教 / 性別議題
- 對媒體 / 議員 / 主管機關發送

> **任何家長通知不可由 AI 直接發送。**`Code.gs` 裡所有 `MailApp.sendEmail()` 都應該被 wrapping 在 HITL approval flow 內。
> **No parent communication may be auto-sent by AI.** All `MailApp.sendEmail()` calls in `Code.gs` should be wrapped in HITL approval flow.

### 1.4 家長通知 HITL / Parent Notification HITL

**情境：** 個別學生狀況通知家長（如成績、出缺勤、輔導、特殊事件）
**Scenario:** Per-student notification to parents (grades, attendance, counseling, special events)

**HITL 設計：**

| 階段 | AI 做 | 人做 |
|---|---|---|
| 識別需通知對象 | AI 從資料 query 出該通知的學生清單 | 導師確認名單 |
| 起草通知文字 | AI 出個別化內容（含學生姓名、具體事件）| **導師必須逐封親自審** |
| 發送通道 | AI 建議用 Line / Email / 紙本 | 導師選 |
| 送出 | — | **必須導師親自按「送出」**；AI 不可批次 auto-send |
| 追蹤回覆 | AI 整理家長回覆 + 標 sentiment | 導師看後決定如何回 |

**絕對紅線：**
- 任何敏感事件（霸凌、意外、自傷風險、學業問題） → **必須電話 + 紙本，不可純線上 AI 通知**
- 家長已表示「不接收 AI 通知」→ 該家長加入黑名單，AI 永不處理該家長帳號
- 重大事件 → **校長 / 學務主任面對面，不發任何文字通知**

---

## 2. HITL Gate 在 Apps Script 程式碼層的實作 / HITL implementation in Apps Script

對應原 repo `src/Code.gs` 的修改建議（**在 fork 上修改，不動原 repo**）：

```javascript
// 範例：在 sendEmail 前必加 HITL approval
function sendParentNotification(toParent, content) {
  // ❌ 不可直接發 / Don't do this:
  // MailApp.sendEmail(toParent, "Notification", content);

  // ✅ 必經 HITL approval / Required HITL flow:
  const approvalRecord = createApprovalRequest({
    type: 'parent_notification',
    to: toParent,
    contentDraft: content,
    reviewerRole: 'classroom_teacher',
    slaHours: 24,
    requireHumanClick: true
  });

  // 不直接發信，等 reviewer 在 UI 上按「同意送出」
  // Don't send; wait for reviewer to click "Approve & Send" in UI
  return approvalRecord.id;
}
```

完整實作架構：

```text
教師 / 行政組長 / AI Agent
        │
        ▼
   填寫表單 (Google Form)
        │
        ▼
   AI 草擬 / 路由 (Apps Script)
        │
        ▼
   寫入 Pending Approval Queue
   (Google Sheet 或 Firestore)
        │
        ▼
   通知 reviewer
   (Email / Slack / LINE)
        │
        ▼
   Reviewer 在 Dashboard 看內容
   點「同意 / 退回 / 修改」
        │
        ▼
   只有「同意」才觸發實際 sendEmail()
```

---

## 3. HITL 設計檢核表 / HITL Design Checklist

每個 L3 use case 上線前，**逐項核對**：

Before each L3 use case launches, **check every item**:

- [ ] 對外輸出（家長 / 學生 / 媒體 / 主管機關）**100% 須人工點「送出」**
- [ ] 對內輸出（教師 / 主任）**至少有 1 個 reviewer 簽核**
- [ ] 涉及金額 / 政策變動 / 對外公告 → **校長或副校長必須簽核**
- [ ] 涉及學生敏感資料 → **AI 自動 escalate 不自行處理**
- [ ] 所有 HITL approval **保留 ≥ 1 年 log**（供日後審計 / 法律訴訟）
- [ ] Reviewer 看不到 AI 原始 prompt → **改造 UI 讓 reviewer 看「最終文字」而非「Prompt 對話」**
- [ ] HITL SLA 超過 2x → **自動 escalate** 給更高層級
- [ ] 有 emergency override 但**只校長可開**

---

## 4. 常見錯誤 / Common Mistakes

| 錯誤 / Mistake | 後果 / Consequence | 修法 / Fix |
|---|---|---|
| HITL 只設給「對外」沒設給「對內」 | 教師看到 AI 草擬的「對學生評語」會不爽 | 加教師 HITL |
| HITL approve 後沒留紀錄 | 出事查不到誰簽 | log 必須留 ≥ 1 年 |
| AI 出錯但 HITL 沒辦法 reject | reviewer 變橡皮圖章 | UI 加「退回 + 改」按鈕 |
| HITL SLA 太長 | 流程變慢，比手動還慢 | SLA 設 24 hr，超過自動 escalate |
| Reviewer 是「AI Champion」一個人 | 此人請假 = 全校 AI 流程停擺 | 至少 2 人 backup |
| 教師 / 主任不知道「我是 reviewer」 | 通知漏看 = SLA 過 | 上線前演練 1 次 |

---

## 5. 法律與規範對位 / Legal & Regulatory Mapping

| 規範 / Regulation | 對 HITL 的要求 / HITL requirement |
|---|---|
| **個人資料保護法**（台灣） | 學生 / 家長 / 教師 PII 處理需個資長 / 校長同意；AI 自動處理需明確告知當事人 |
| **兒童及少年福利與權益保障法** | 對未成年的處理特別謹慎，敏感事件不可純 AI 通知 |
| **教育部 AI 應用倫理規範**（如有） | 各縣市可能有自己的規範，上線前查 |
| **個資法第 8 條** | 蒐集 PII 時應明確告知用途；AI 處理算「特定目的外利用」需另取得同意 |
| **歐盟 GDPR**（若收外籍學生 / 家長）| 自動化決策需提供 opt-out + 人工申訴管道 |
| **美國 FERPA**（若有美籍學生）| 教育紀錄不得未授權揭露；AI 處理也算揭露 |

> 不確定時：**保守一點。** 學校不該成為 AI 法律邊界的測試場。
> When uncertain: **be conservative.** Schools should not be the test ground for AI legal boundaries.

---

**Version:** v0.1.0 (2026-05-20)
**License:** Apache 2.0
