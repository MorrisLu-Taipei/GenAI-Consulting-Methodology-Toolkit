# 學術投稿工作流使用手冊 / Publishing Workflow Manual

> 🎯 **這份手冊教你**：怎麼用本 toolkit 的工作流，把一篇論文從**草稿**一路帶到**投稿 / deposit / 審稿回覆**。
> 中心是三個投稿工作流（`/claim-audit`、`/hype-scrub`、`/reviewer-response`），並把它們放進完整的「草稿→發表」管線。
> 📝 本檔以中文為主；EN 版列 TODO。
> 🎭 想看「跟著一個人走一遍」的敘事版？見 [`PUBLISHING_WORKFLOW_SCENARIO.md`](PUBLISHING_WORKFLOW_SCENARIO.md)（研究者 R 從草稿到被接受的全程）。

---

## 0. 給誰用 / 用在哪

| 你是 | 你會用到 |
|---|---|
| 要投 preprint / 期刊 / 會議的作者 | 全部 |
| 要稽核別人稿件的 reviewer / 共同作者 | `/claim-audit`、`/hype-scrub` |
| 收到審稿意見要回覆 | `/reviewer-response` |

**對象稿件**：`09_Research_Paper/` 內的 preprint，或任何要投出去的學術文字。

> ⚠️ 共同原則：**所有工作流產出都是「草稿」，不是定稿。** 最終由人類作者負責、署名、送出。

---

## 1. 全景圖：草稿 → 發表管線

```
[1] 寫作 / 草稿
      │
      ▼
[2] 內容審查（看「對不對、夠不夠硬」）
      ├─ /red-team-review     ← 找最致命的攻擊點（Codex）
      ├─ /evidence-audit      ← 顧問報告主張↔證據（Codex）
      └─ /devil-pair-debate   ← 價值觀盲點、對立辯論（Claude）
      │
      ▼
[3] 投稿前打磨（看「能不能投、像不像話」）★本手冊重點
      ├─ /claim-audit         ← 學術主張稽核、overclaim（Codex）
      └─ /hype-scrub          ← 投稿用語、hype 詞清理（Codex）
      │
      ▼
[4] 凍結 + 發表（PDF → DOI → 投稿）
      ├─ 渲染 PDF（pandoc，見 Makefile / REPRODUCIBILITY.md）
      ├─ GitHub Release（tag）→ 觸發 Zenodo DOI
      └─ SSRN deposit
      │
      ▼
[5] 審稿回覆（收到 reviewer 意見後）
      └─ /reviewer-response   ← 逐點回覆信草稿 + 改動清單（Codex）
      │
      └──→ 改完回到 [3] 再跑一次 claim-audit + hype-scrub，確認沒引入新問題
```

> 記憶法：**[2] 看內容硬不硬、[3] 看話講得像不像話、[5] 回覆審稿。** 跑完 [5] 一定回 [3] 收尾。

---

## 2. 工具速查表

| 工作流 | 階段 | 引擎 | 一句話 | 檔案 |
|---|---|---|---|---|
| `/red-team-review` | [2] | Codex | 找最致命的攻擊點 | `.codex/workflows/red-team-review.md` |
| `/evidence-audit` | [2] | Codex | **顧問報告**主張↔證據 | `.codex/workflows/evidence-audit.md` |
| `/devil-pair-debate` | [2] | Claude | 雙方對立辯論 + 法官 | `.claude/workflows/devil-pair-debate.md` |
| **`/claim-audit`** | **[3]** | Codex | **學術稿件**主張稽核、overclaim | `.codex/workflows/claim-audit.md` |
| **`/hype-scrub`** | **[3]** | Codex | hype 詞 / 投稿用語清理 | `.codex/workflows/hype-scrub.md` |
| **`/reviewer-response`** | **[5]** | Codex | 審稿意見→逐點回覆草稿 | `.codex/workflows/reviewer-response.md` |

> ⚠️ 易混淆：**`/evidence-audit` 是稽核「顧問報告」、`/claim-audit` 是稽核「學術論文」。** 投論文用後者。

---

## 3. 怎麼啟動（兩個引擎都能用，零安裝）

這三個工具**同時**做成兩種格式（內容同步）。看你在哪個引擎：

| 引擎 | 形式 | 怎麼叫 | 安裝 |
|---|---|---|---|
| **Claude Code** | 原生 Skill（`.claude/skills/claim-audit/SKILL.md`）| 打 `/claim-audit`（自動發現，也可能被 Claude 自動觸發）| ❌ 零安裝，丟檔即生效 |
| **Codex** | workflow（`.codex/workflows/claim-audit.md`）| `/claim-audit` 或「請依 .codex/workflows/claim-audit.md 執行」| ❌ 零安裝 |

> **沒有「安裝程序」。** 專案內的 skill / workflow 都是「放進目錄就生效」——不必改 `settings.json`、不必重開。
> 唯一需要「安裝」的，是把它打包成 plugin 給**別人** `/plugin install`（本 repo 目前不做）。

接著**貼上要處理的內容，或給檔案路徑**，例如：

```text
/claim-audit
請稽核 09_Research_Paper/2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md 的 §9 評估章節
```

> 工具若資訊不足會**先問你**（例如 reviewer-response 會要你貼審稿意見全文）。
> Claude Code skill 清單見 [`../.claude/skills/README.md`](../.claude/skills/README.md)。

---

## 4. 三個投稿工作流：詳細用法

### 4.1 `/claim-audit` —— 學術主張稽核

| 項目 | 內容 |
|---|---|
| **何時用** | 投稿前；改完內容後想確認沒 overclaim |
| **餵什麼** | 整篇稿件，或指定章節（abstract / contributions / evaluation 最該查）|
| **它做什麼** | 把主張拆 5 類（empirical / comparative / novelty / generalization / causal），逐條查「引用層級夠不夠、有沒有 baseline、hedging 相不相稱」|
| **你拿到** | 稽核表（每條 claim + 問題 + 建議修法）+ overclaim 清單 + hedging 對照 |
| **範例** | `/claim-audit` → 「稽核這篇 abstract 的四項貢獻主張」|

> 重點：它**不改稿**，只給清單。你看完決定採納哪些。

### 4.2 `/hype-scrub` —— 投稿用語清理

| 項目 | 內容 |
|---|---|
| **何時用** | 投稿前最後一關；任何要對外的嚴肅文字 |
| **餵什麼** | 整篇稿件 + 告訴它場域（peer-review / preprint / 白皮書 / README，影響嚴格度）|
| **它做什麼** | 全文掃 hype 詞（revolutionary / seamless / unprecedented / 顛覆…）、無證據最高級、空洞 buzzword，並**分辨「可辯護的已定義術語」vs「膨脹」**|
| **你拿到** | 命中表（詞 + 原句 + 判定 + 建議替代）+ 語氣總評 |
| **範例** | `/hype-scrub` → 「場域是 peer-review 論文，掃全文」|

> 重點：會**保留**你定義過的術語（如 living artifact），只動膨脹的字。要它直接改也行（會列出每處前→後）。

### 4.3 `/reviewer-response` —— 審稿回覆

| 項目 | 內容 |
|---|---|
| **何時用** | 收到期刊 / 會議 reviewer 意見後 |
| **餵什麼** | reviewer 意見全文（含 Reviewer 編號）+（最好）目前稿件路徑 |
| **它做什麼** | 每條意見分類（must-fix / 澄清 / 分歧 / 超範圍）→ 產回覆文字 + 對應的稿件改動 |
| **你拿到** | response letter（逐點）+ 稿件改動清單（change log）+「需作者確認的事實」清單 |
| **範例** | 貼上 R1/R2 意見 → 拿到回覆信草稿 |

> 硬規則：**不捏造改動、不替你背書未查證的事實**（會列進「需作者確認」）。送出前由你定稿。

---

## 5. 投稿前總檢查表（照著勾）

```
內容硬度
  [ ] /red-team-review 跑過，致命攻擊點都有回應
  [ ] /devil-pair-debate 跑過（價值觀盲點）

主張與用語
  [ ] /claim-audit 跑過，overclaim 已降級或補證據
  [ ] /hype-scrub 跑過，hype 詞已清
  [ ] 引用分層（Tier 1/2/3）一致、計數正確
  [ ] 有「本論文不主張」段

provenance（言行合一）
  [ ] 每個數字指向 REPRODUCIBILITY.md，凍結 commit 註明
  [ ] 每條引用都查證得到（非 LLM 幻覺）— 文獻可用 research-hub authenticity gate

雙語
  [ ] EN 改完，ZH 同步（反之亦然）

發表機制
  [ ] PDF 渲染 OK（pandoc）
  [ ] GitHub Release tag → Zenodo DOI
  [ ] CITATION.cff 填入 DOI
  [ ] DOI 狀態文字正確（不要還寫 pending）
```

---

## 6. 常見問題

**Q：`/claim-audit` 和 `/evidence-audit` 差在哪？**
A：claim-audit 查**學術論文**的主張；evidence-audit 查**顧問報告**的主張（成熟度 / ROI / 治理）。投論文用 claim-audit。

**Q：工作流會直接改我的稿嗎？**
A：預設**只給清單**。`/hype-scrub`、`/reviewer-response` 你明說「直接幫我改」才會改，且會列出每處改動。改完務必自己看過。

**Q：跑完 `/reviewer-response` 還要做什麼？**
A：回 [3]，對新增/修改的文字再跑一次 `/claim-audit` + `/hype-scrub`，確認沒把 overclaim 或 hype 帶回來。

**Q：文獻回顧（related work）有工具嗎？**
A：有，但那是另一條線——見 [`PAPER2_LITREVIEW_PIPELINE.md`](PAPER2_LITREVIEW_PIPELINE.md)（research-hub 發現+查證+聚類）與 [`../90_References/AI_RESEARCH_TOOLING_REFERENCE.md`](../90_References/AI_RESEARCH_TOOLING_REFERENCE.md)。

**Q：這些工作流自己會不會出錯 / 幻覺？**
A：會。它們是**加速器不是裁判**。所有事實、數字、引用，最終由人類作者查證負責。

---

## 7. 一個真實示範（本 repo 自己跑過）

2026-05-23 我們用 `/claim-audit` + `/hype-scrub` 全文掃本 preprint，**比先前人工稽核多抓到 2 處**（§8.2 漏網的 pending-DOI、ZH「顛覆」誤譯），證明全文掃描的價值。完整紀錄見 [`CLAIM_AUDIT_2026-05-23.md`](CLAIM_AUDIT_2026-05-23.md)。

---

**版本：** v0.1（2026-05-23）
**作者：** Morris Lu（盧業興）· Tiger AI 虎智科技
**授權：** 隨本 toolkit（程式 Apache 2.0 / 文件 CC BY 4.0）
**相關：** [`CLAIM_AUDIT_2026-05-23.md`](CLAIM_AUDIT_2026-05-23.md)、[`PAPER2_LITREVIEW_PIPELINE.md`](PAPER2_LITREVIEW_PIPELINE.md)、[`../.codex/README.md`](../.codex/README.md)、[`README.md`](README.md)
