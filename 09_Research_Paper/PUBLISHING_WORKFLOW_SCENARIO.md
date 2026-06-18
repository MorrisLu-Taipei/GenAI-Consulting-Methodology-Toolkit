# 投稿工作流：使用情境故事 / Publishing Workflow — A Usage Scenario

> 🎭 這是 [`PUBLISHING_WORKFLOW_MANUAL.md`](PUBLISHING_WORKFLOW_MANUAL.md) 的**敘事版**。手冊是「查表」、本檔是「跟著一個人走一遍」。
> 🔒 **虛構教學案例**：研究者 R、C 會議、城市 X 皆為化名，與真實人事物無關（依 [`../04_Scenarios/CASE_WRITING_STANDARD.md`](../04_Scenarios/CASE_WRITING_STANDARD.md)）。
> 📝 中文為主；EN 版列 TODO。

---

## 主角與處境

**研究者 R**：一位在城市 X 工作的獨立研究者，寫了一篇設計科學論文，想投三週後截稿的 **C 會議**（一個 IS 領域國際會議）。R 一個人作業，沒有共同作者幫忙抓盲點——這正是他最焦慮的地方：**「我自己寫的，自己看不出哪裡會被 reviewer 釘。」**

R 打開本 toolkit，照 [`PUBLISHING_WORKFLOW_MANUAL.md`](PUBLISHING_WORKFLOW_MANUAL.md) 的五階段管線走。以下是他的一週。

---

## 週一上午 ── 階段 [2]：先看「內容硬不硬」

草稿寫完，R 沒有急著潤稿，而是先找最致命的攻擊點。他在 Codex 對話輸入：

```text
/red-team-review
請紅隊我的論文 09_Research_Paper/draft.md，假設你是最嚴格的 reviewer
```

回來一份「最可能被拒的三個理由」。第一條讓 R 冒冷汗：

> 「§9 評估只有自我評分（9/10），沒有外部驗證——reviewer 會質疑這是 self-serving。」

R 想起論文裡其實有 §9.4「本論文不主張之事」和 §9.5 預註冊驗證實驗。他補了一句話，把 reviewer 會問的「那你打算怎麼驗證」**前移到評估章節開頭**，先發制人。

> 💡 階段 [2] 的價值：**在投出去前，先當一次自己的 reviewer。**

---

## 週一下午 ── 階段 [3]：`/claim-audit`，看主張站不站得住

內容補強後，R 要確認「我有沒有講太滿」。他輸入：

```text
/claim-audit
稽核 09_Research_Paper/draft.md，特別是 abstract 和 contributions
```

工作流把他的主張拆成 5 類，逐條查。回來的稽核表裡，兩條被圈起來：

| Claim | 類型 | 問題 | 建議 |
|---|---|---|---|
| 「本範式可推廣到所有專業電子書」 | Generalization | 從 n=1 推全稱 | 降為「in this instantiation；推廣留待 future work」|
| 「首創 reader-as-querier 模式」 | Novelty | 沒 bound、沒承認相鄰領域 | 改「to our knowledge…」+ 承認 wikis / Jupyter Books |

R 看完愣了一下——這兩句他本來覺得「很有力」，但工作流說的對：**reviewer 最愛攻擊的就是這種沒收邊的大話。** 他照建議把「可推廣到所有」改成「在本案例中觀察到；推廣需進一步研究」，把「首創」改成「就我們所知，少有直接前例（針對顧問方法論這一類）」，並補一句承認相鄰領域。

> 💡 `/claim-audit` 不改稿，只給清單。**決定權在 R。** 但這兩條他全採納了。

---

## 週二上午 ── 階段 [3]：`/hype-scrub`，把行銷腔刮掉

主張收好了，接著清用語。R 輸入：

```text
/hype-scrub
場域是 peer-review 論文，全文掃 09_Research_Paper/draft.md
```

回來的命中表，有些他服氣、有些他要保留：

| 命中詞 | 原句 | 判定 | 處理 |
|---|---|---|---|
| seamless | "seamless multi-IDE orchestration" | 膨脹 | → "coordinated"，R 接受 |
| revolutionary | "a revolutionary paradigm" | 膨脹 | → "a new paradigm"，R 接受 |
| living artifact | "a living artifact" | **可辯護（已定義術語）** | 保留 |

R 鬆一口氣——他怕工作流把他精心定義的「living artifact」也當垃圾刪掉，結果它**分得出哪些是術語、哪些是膨脹**，只動該動的。

> 💡 `/hype-scrub` 會保留你定義過的概念詞。怕被誤刪是多慮的。

---

## 週四 ── 階段 [4]：凍結 + 發表

打磨完，R 渲染 PDF（pandoc）、開 GitHub Release 打 tag，Zenodo webhook 幾分鐘內 mint 出 DOI，再把 PDF 上傳 SSRN。他特別檢查了一件事——**論文裡所有「pending DOI」的字眼都改成已發布的實際 DOI**（手冊檢查表上的那一項）。

投稿系統按下 submit。R 關上電腦。

---

## 兩個月後 ── 階段 [5]：`/reviewer-response`

C 會議回信：**Major Revision**。三位 reviewer，七條意見。R 深吸一口氣，把意見全文貼進去：

```text
/reviewer-response
以下是 C 會議的三位 reviewer 意見（含編號），目前稿件在 09_Research_Paper/draft.md
[貼上 R1-C1 ... R3-C2 全文]
```

工作流把七條逐一分類、各給回覆 + 對應改動：

> **R2-C1（must-fix）：** 「n=6 樣本太小。」
> **Response（草稿）：** We agree the sample is small. We have (a) reframed the study as exploratory in §9.5, (b) added effect-size reporting alongside p-values, and (c) expanded the limitations.
> **Change:** §9.5 —— 加 exploratory 定位 + effect size 說明。

> **R3-C2（分歧）：** 「這根本不算 design science。」
> **Response（草稿）：** We respectfully retain our position; we evaluate against Hevner's seven guidelines (§9.1) and cite the DSR lineage. We have added a sentence in §2.1 clarifying the second-order DSR contribution.

回覆信末尾有一份 **change log** 和一份 **「需作者確認的事實」清單**——其中一條是「R1 問的那個數字，請作者親自核對 REPRODUCIBILITY.md 再送出」。

R 很感激這條提醒：**工作流沒有替他亂掰數字，而是把不確定的丟回給他查。** 他逐條核對、潤飾語氣，把「we respectfully retain」那段的火力調得更有禮一點。

---

## 收尾 ── 回階段 [3] 再跑一次

改完回覆、也改了稿，R 想起手冊那句話：**「跑完 `/reviewer-response` 要回 [3]。」** 他對新增的文字再跑一次：

```text
/claim-audit 只看這次新增/修改的段落
/hype-scrub 只看這次新增/修改的段落
```

果然——他在回覆 R2 時新寫的一句「this robustly demonstrates…」被 `/hype-scrub` 抓出來（"robustly" + "demonstrates" 都太強）。R 改成「this provides evidence that…」。

**送出 revision。** 三週後：**Accept with minor revisions。**

---

## R 學到的三件事

1. **一個人投稿，也能有「審稿團隊」。** red-team / claim-audit / hype-scrub 各自從不同角度當他的 reviewer，補上了「沒有共同作者」的缺口。
2. **工具是加速器，不是裁判。** 它抓問題、給建議、提醒查證，但每個決定（採不採納、數字對不對）都還是 R 自己負責、自己署名。
3. **回覆審稿後一定要回頭掃一次。** 最容易出包的，就是「為了回覆 reviewer 而新寫、卻沒再檢查」的那幾句。

---

## 這個故事對到手冊哪裡

| 故事場景 | 手冊章節 |
|---|---|
| 週一上午 red-team | [2] 內容審查 |
| 週一下午 claim-audit | [3] + §4.1 |
| 週二 hype-scrub | [3] + §4.2 |
| 週四 PDF/DOI | [4] + §5 檢查表 |
| 兩個月後 reviewer-response | [5] + §4.3 |
| 收尾回頭掃 | §6 FAQ「跑完要回頭」|

---

**版本：** v0.1（2026-05-23）
**作者：** Morris Lu（盧業興）· Tiger AI 虎智科技
**授權：** 隨本 toolkit
**情境聲明：** 研究者 R、C 會議、城市 X 為虛構教學案例。
**相關：** [`PUBLISHING_WORKFLOW_MANUAL.md`](PUBLISHING_WORKFLOW_MANUAL.md)（參考版）
