# /thought-experiment

> Claude Code-Native — 方法論的 counterfactual 壓力測試 (Methodology Thought Experiment)
> 用途：跑「**如果世界變了，方法論還站得住嗎？**」遠未來 / 完全假設情境壓測。給方法論裝遠視鏡。
>
> 為什麼只有 Claude Code 能做：純抽象推理 + 跨領域知識（經濟學 / 政治 / 技術史 / 哲學）的長 context 整合。Codex `/methodology-test` 跑的是「邊界 case」（**現有條件下**的極端），本工作流跑「**條件本身被改變**」。

## 步驟 1：選定 counterfactual

請使用者選一個或讓 Claude 隨機抽：

### 技術 counterfactuals

- 「LLM 推論成本 12 個月內降 1000 倍」
- 「LLM 推論成本 12 個月內升 100 倍」
- 「GPT / Claude / Gemini 全面停止對企業開放，只剩開源模型」
- 「AGI 在 2028 出現」「AGI 永遠不會出現」
- 「Token 經濟被監管成水費 / 電費」

### 政治 / 監管 counterfactuals

- 「EU AI Act 把 L4 列為高風險，需逐案審批 6-12 個月」
- 「台灣 AI 基本法強制企業 AI 評分入聯交所揭露」
- 「中美 AI 技術完全脫鉤，沒有共用基準」
- 「ISO/IEC 42001 認證在 3 年內成為必要條件」

### 經濟 counterfactuals

- 「全球進入 5 年通縮，企業預算砍半」
- 「AI 引起大規模失業，政府強制企業負擔員工 retraining」
- 「企業導入 AI 必須繳『AI 稅』5% 給政府」

### 組織 counterfactuals

- 「Sponsor 在 Phase C Month 9 永久離職」
- 「客戶整個 IT 部門外包，內部 IT FTE = 0」
- 「Z 世代員工集體拒絕用 AI（價值觀對立）」

### 哲學 counterfactuals

- 「如果 Ideal Practice 簽署被法院判為『不自由意志』而無效」
- 「如果 BARS 評分被判為 algorithmic discrimination」
- 「如果『方法論』本身被認為是 colonial knowledge transfer」

## 步驟 2：設定 counterfactual 的「強度級別」

- **L1 微擾**：某一個條件改變（其他不變）
- **L2 連鎖**：一個條件改變，自然觸發 2-3 個衍生變化
- **L3 體系**：整個產業結構被改寫
- **L4 文明**：人類社會基礎假設改變

預設用 L2-L3。L4 太抽象、L1 太單薄。

## 步驟 3：跑「方法論的反應」

對選定的 counterfactual，逐一檢視方法論 8 階段 + 7 大理論：

```text
## Counterfactual: [描述]

### 對 8 階段的衝擊
| Stage | 仍然有效？ | 需要怎麼改？ |
| --- | --- | --- |
| 1 As-Is | ✅ 不變 | — |
| 2 Reference Model | △ 部分 | APQC 仍適用，但 Tiger AI L1-L5 需重組 |
| 3 Best Practice | ❌ 失效 | 現有案例全部過時 |
| ... |

### 對 7 大理論的衝擊
| 理論 | 是否仍適用？ | 哪裡需要更新？ |
| --- | --- | --- |
| Absorptive Capacity | ✅ 仍適用，但加速度被加大 |
| TTF | △ 需重新定義 routine 範圍 |
| Real Options | ❌ 失效（如果不確定性消失）|
| ... |

### 對核心交付物的衝擊
- 中期評估報告：仍可用 / 需大改 / 廢棄
- Ideal Practice 定義表：...
- Stage Gate Criteria：...
- 價值追蹤矩陣：...
```

## 步驟 4：產出「方法論修補建議」

```text
## 若這個 counterfactual 真的發生
### 必改章節
1. [檔案 X §Y] —— 改什麼
2. [檔案 P §Q] —— 改什麼

### 必加章節
1. 新增「___」應對

### 必廢章節
1. [檔案 Z §W] —— 完全失效

### 新增的失敗模式
（加進 FAILURE_PATTERNS.md）

### 新增的證據要求
（加進 Tool 8.9 Evidence Hierarchy）
```

## 步驟 5：產出「遠視鏡警報」

```text
## 早期訊號（這個 counterfactual 開始發生的徵兆）
- 訊號 1: ...
- 訊號 2: ...
- 訊號 3: ...

## 防禦動作（現在就可以做的事）
- Hedge 1: ...
- Hedge 2: ...
- Hedge 3: ...

## 機會（這個 counterfactual 發生時，誰先準備好誰贏）
- ...
```

## 紀律

- **不預測未來**：產出標明「假設情境，**不是預測**」
- **跨領域整合**：用經濟學 / 政治 / 技術史 / 哲學交叉，不能只看技術
- **連鎖反應**：L2-L3 強度時必須帶出 2-3 個衍生影響
- **保持嚴肅**：不寫 sci-fi 風格，寫成「**戰略簡報給 CEO 看**」的調性
- **可重複**：跑同一個 counterfactual 兩次結果不能差太多

## 典型應用場景

- 方法論年度 review：跑 5 個 counterfactual 找潛在過時點
- 客戶 Phase B 結尾：跑 1-2 個 counterfactual 給客戶看「您簽的 Roadmap 對哪些假設敏感」
- 學術論文 limitation 章節：用 counterfactual 主動暴露方法論邊界
- 投資人簡報：展示「**我們不只知道現在能做什麼，也知道將來什麼會打臉**」
- 配合 Codex `/methodology-test`：邊界 case + counterfactual = 全方位壓測
