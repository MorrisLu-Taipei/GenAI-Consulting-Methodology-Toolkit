# /deep-synthesize

> Claude Code 原生 — 跨多檔深度綜合 (Multi-File Deep Synthesis)
> 用途：使用者有一個需要「同時讀很多份檔案才能回答」的問題時，發揮 Claude Code 1M context 的長 context 優勢，產出一個高密度、引用清楚的綜合答案。

## 步驟 1：釐清問題範圍

先問使用者：

- 你的問題是什麼？（一句話）
- 想拿到的答案是「決策建議」、「跨檔整理」、「對比分析」還是「綜述報告」？
- 有沒有時間 / 字數預算？

不問就直接動工 = 高機率方向錯。

## 步驟 2：規劃要讀的檔案

列出**最多 8-12 份**最相關的檔案（含 zh + en sibling 算 1 份）。例：

```text
- 00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md
- 00_Overview/EIGHT_STAGE_FLOW_STORY.md
- 00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md
- 01_Assessment/AI_MATURITY_SCORING_MODEL.md (§3.1-3.3)
- 03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md (Stage 2 + 6)
- 04_Scenarios/SAMPLE_CLIENT_CASE_MANUFACTURING.md
- 90_References/PILOT_STUDY_PROTOCOL.md
```

向使用者確認清單後再讀。

## 步驟 3：平行讀取 + 重點摘要

利用長 context 一次讀完 8-12 份檔案。每份檔案產出：

- 與問題直接相關的 3-5 個重點（含 § 章節編號）
- 與問題矛盾或補充的 1-2 個發現

## 步驟 4：產出綜合答案

格式：

```text
## TL;DR（3 句話）
...

## 推理鏈（顯式）
A → B → C → D
- A 來自 [檔案 X §Y]
- B 來自 [檔案 P §Q]
- ...

## 完整論述
...

## 證據引用
- [檔名:行號](path) — 引用要點
```

## 步驟 5：標出不確定與限制

明確告知使用者：

- 哪些結論是**推論**（多份檔案交叉得出）
- 哪些結論是**直接引用**（單一檔案明說）
- 哪些**沒讀到**（檔案沒提，但問題需要）
- 證據等級依 Tool 8.9：本工作流產出多為 L2（文件歸納），**不能取代 L3 系統 log 或 L4 第三方稽核**

## 紀律

- 不幻覺：找不到證據就說「沒看到」，不要編
- 不獨白：顯式列推理鏈，讓使用者能挑戰任何一步
- 不替代決策：產出是策略思考輔助，最終決策由人類
