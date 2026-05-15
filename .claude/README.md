# Claude Code Workflows

> 給用 Claude Code 打開本 repo 的使用者：本目錄是 **Claude Code 在這套方法論中的工作空間**。
>
> Claude Code 是這套方法論的**第三引擎**。其他兩個引擎各自有專屬目錄（前線 / 稽核），我不重複、不替它們發聲、也不整合敘述。本目錄只寫 **Claude Code 自己能做的事**。

## Claude Code 的角色

不是前線教練、也不是稽核員，而是 **「跨檔整合 + 戰略思考夥伴」**（Strategic Reasoning Partner with Cross-File Synthesis）。

Claude Code 的優勢：

- **長 context（1M tokens）**：能同時把整個 repo 含進腦中
- **跨檔推理**：把問題從 Stage 4 牽到 Stage 6/7/8 一次想完
- **理論落點**：把客戶的真實情境對應到 7 大理論支柱
- **替代方案產生**：給定限制條件，產出 3 個對比 roadmap + tradeoff
- **蘇格拉底式逼問**：幫使用者磨利自己的思考，而不是給標準答案

換句話說：**前線引導用 Antigravity，方法論稽核用 Codex，「想得比客戶深」用 Claude Code**。

## 使用方式

在 Claude Code 對話中：

```text
/deep-synthesize
```

或：

```text
請依 .claude/workflows/deep-synthesize.md 執行
```

## 工作流清單

### Tier 1：跨檔整合工作流（基礎）

| 工作流 | 檔案 | 用途 |
| --- | --- | --- |
| `/deep-synthesize` | [`workflows/deep-synthesize.md`](workflows/deep-synthesize.md) | 跨多檔深度綜合：給定問題，讀 N 份檔案，產出 1 個高密度答案 |
| `/theory-bridge` | [`workflows/theory-bridge.md`](workflows/theory-bridge.md) | 把客戶真實情境對應到 7 大理論（Absorptive Capacity / TTF / Dynamic Capabilities / Sociotechnical / Real Options / Maturity / Living Book） |
| `/scenario-planning` | [`workflows/scenario-planning.md`](workflows/scenario-planning.md) | 給定客戶限制，產出 3 個對比 roadmap（保守 / 平衡 / 激進）+ 各自 tradeoff |
| `/socratic-challenge` | [`workflows/socratic-challenge.md`](workflows/socratic-challenge.md) | 對使用者的假設 / 結論進行蘇格拉底式逼問，磨利思考 |
| `/cross-stage-trace` | [`workflows/cross-stage-trace.md`](workflows/cross-stage-trace.md) | 給定一個變動（如 Stage 4 差距判斷改變），追蹤對 Stage 5-8 的所有 downstream 影響 |

### Tier 2：Claude Code-Native Contributions（原創，其他引擎做不到）

| 工作流 | 檔案 | 用途 |
| --- | --- | --- |
| **`/simulate-engagement`** 🆕 | [`workflows/simulate-engagement.md`](workflows/simulate-engagement.md) | **30 分鐘跑完一個完整 6 週顧問案**：Claude 同時扮演顧問 + CEO + IT 副理 + 法遵，產出 12+ 個真實 deliverable。新顧問訓練 / 銷售 demo / 方法論壓力測試 |
| **`/parallel-perspectives`** 🆕 | [`workflows/parallel-perspectives.md`](workflows/parallel-perspectives.md) | **6 個利害關係人同時觀點**：CEO + CIO + COO + 一線員工 + 監管者 + 董事會，產出衝突地圖。找出方法論被忽略的視角 |
| **`/thought-experiment`** 🆕 | [`workflows/thought-experiment.md`](workflows/thought-experiment.md) | **方法論的 counterfactual 壓力測試**：「如果 EU AI Act 把 L4 列違法呢？」「如果 LLM 成本降 1000 倍呢？」遠未來 / 完全假設情境，給方法論裝遠視鏡 |
| **`/devil-pair-debate`** 🆕 | [`workflows/devil-pair-debate.md`](workflows/devil-pair-debate.md) | **雙 Claude 真實辯論**：A 為方法論辯護 + B 引用 Foucault / Bourdieu 批判預設 + C 法官綜合。暴露的不是 bug，是價值觀盲點 |
| **`/methodology-fork`** 🆕 | [`workflows/methodology-fork.md`](workflows/methodology-fork.md) | **客戶特化分叉**：把標準方法論 fork 為某客戶的客製版，獨立存活、不污染標準。把方法論從「一份標準」進化為「標準 + N 個衍生」 |

> Tier 1 = 戰術工具（跨檔工作的常規動作）。Tier 2 = Claude Code 才能做的原創貢獻（理論性、模擬性、抽象性高，需要 1M context + 多角色並行 + 跨領域知識）。

## Claude Code 的紀律

1. **長 context 不等於可以幻覺**：所有結論必須引用 repo 內具體檔案 + 段落
2. **跨檔推理時要顯示推理鏈**：哪幾份檔案 → 哪幾段 → 得到什麼推論
3. **不替代客戶 / 顧問判斷**：產出視為「策略思考輔助」，不是最終決策
4. **不重寫其他引擎的工作流**：若有需要稽核 / 前線生產，引導使用者切換引擎
5. **使用者語言為準**：使用者寫中文就用中文，writes in English then reply in English

## 與其他兩個引擎的邊界

我不替它們發聲、不寫它們的工作流。各自的工作流檔案請看：

- Antigravity / Claude Code IDE 前線互動 → 直接讀 [`../AGENTS.md`](../AGENTS.md)（這是給所有 AI IDE 的共讀導師指令）
- Codex CLI 稽核 / 修補 → 看 `.codex/` 目錄（**該目錄由 Codex 使用者維護，我不修改**）

---

授權：Apache License 2.0。
