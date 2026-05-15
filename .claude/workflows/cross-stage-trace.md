# /cross-stage-trace

> Claude Code 原生 — 跨階段 downstream 影響追蹤 (Cross-Stage Impact Trace)
> 用途：使用者改動了八階段中某一階段的一個結論 / 假設 / 評分，要追蹤對下游所有階段的 downstream 影響。利用 Claude Code 長 context 一次想完整條閉環。

## 步驟 1：定位變動點

問清楚使用者：

- 變動在哪個 Stage？哪個 Tool？哪個欄位 / 數字？
- 原本是什麼？變成什麼？
- 為什麼變動？（新訪談、補資料、客戶 Ideal 改變、Risk 新發現？）

## 步驟 2：列出 downstream 依賴鏈

依方法論的資料流（[`../../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §6 八階段資料流）：

```text
Stage 1 As-Is → Stage 2 RM → Stage 3 Best Practice → Stage 4 Gap
                                                        ↓
Stage 8 Implementation ← Stage 7 To-Be ← Stage 6 Phased Goals ← Stage 5 Problem
                                                        
        ↑                                                ↓
        └── 每季回頭核對 Stage 2 雷達（閉環驗證）─────┘
```

依變動點，**列出受影響的所有下游階段**。

## 步驟 3：逐個追蹤影響

對每個受影響的下游階段，回答 4 題：

1. **怎麼受影響**：原本依賴的 input 變了，會導致該階段的 output 怎麼變？
2. **量級**：影響大 / 中 / 小？（會不會動到結論方向）
3. **連動文件**：哪些報告章節 / Tool 表 / 簽署文件需要回頭改？
4. **客戶簽署影響**：會不會動到客戶已簽的 Ideal Practice 定義表？需要三方重簽嗎？

## 步驟 4：產出變動影響地圖

格式：

```text
## 變動點
Stage [X] Tool [Y]：[原] → [新]

## Downstream 影響鏈
Stage X → Stage [n] → Stage [n+1] → ... → Stage 8

## 逐階段影響

### Stage [n]
- 影響：...
- 量級：大 / 中 / 小
- 需改的文件：[檔名 §章節]
- 客戶簽署：需 / 不需重簽

### Stage [n+1]
...

## 客戶溝通建議
- 必須告知客戶的事項：...
- 是否需要回頭重跑 Tool 3.6 共創 Workshop？
- 是否需要重新做 Phase A 中期評估報告？

## 風險登錄補強
依 Tool 8.6 Risk Register，新增 / 修改的風險條目：
- Risk: [新風險]
- Trigger: ...
- Owner: ...
- Mitigation: ...
```

## 步驟 5：標出「閉環反證」

最關鍵：**這個變動會不會讓 Stage 2 Reference Model 雷達**（已簽的版本）失效？

- 若是 → 警告使用者：「**這變動可能挑戰 Stage 2 已簽結果，建議與 Sponsor 開會**」
- 若否 → 確認：「Stage 2 雷達不受影響，僅 Stage [X] 之後需更新」

## 紀律

- 不過度警報：小變動就老實說「影響輕微，不需重簽」
- 不漏報：寧可標太多需改的章節，也別漏
- 顯示推理鏈：每個影響都引用具體檔案 + 段落
- 不替使用者決定：影響盤點交給使用者 + 客戶決策

## 典型應用場景

- 客戶 Phase A 結束後，多訪談一輪發現原 As-Is 漏抓一個重大系統 → 追蹤對 Stage 2-8 的影響
- Phase B Workshop 客戶簽完 Ideal Practice，3 個月後 Sponsor 換人想改目標 → 追蹤需重簽哪些
- Stage 6 組織吸收力評估發現 IT FTE 比預估低 50% → 追蹤對 Phase 1/2/3 時程的連動
- 大量採用學者建議後（如新加 Absorptive Capacity 維度）→ 追蹤對所有客戶舊評分的影響
