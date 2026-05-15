# /theory-bridge

> Claude Code 原生 — 客戶情境 ↔ 學術理論對應 (Theory Bridge)
> 用途：使用者帶來一個客戶真實情境（如「客戶花了 NT$ 500 萬但 L3 PoC 全失敗」），把它對應到 7 大理論支柱中**最能解釋這個現象的 1-2 個理論**，並產出可採用的 intervention。

## 步驟 1：聽完情境，不打斷

請使用者完整描述客戶情境，至少含：

- 公司規模 / 產業 / 起點 L 級
- 發生了什麼（症狀）
- 客戶 / 顧問認為原因是什麼（**他們的假設**）
- 已嘗試過什麼（**避免重複建議**）

不夠就追問。

## 步驟 2：對應 7 大理論

依 [`../../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) 的 7 大理論支柱，找最能解釋此情境的 1-2 個：

| 理論 | 適用症狀 |
| --- | --- |
| **Capability Maturity** (Rosemann/CMMI) | 跳級失敗、評分主觀爭議 |
| **Absorptive Capacity** (Cohen & Levinthal 1990) | 同樣 AI 機會，不同公司導入結果天差地別 |
| **Task-Technology Fit** (Goodhue & Thompson 1995) | 強推 L4-L5 到 Non-routine 部門失敗 |
| **Dynamic Capabilities** (Teece 1997) | 只做自動化、沒建立適應能力 |
| **Sociotechnical Systems + Trust in AI** | 演算法厭惡 / 過度依賴 / 心理安全 / 責任模糊 |
| **Real Options** (Dixit & Pindyck 1994) | L4-L5 投資被 NPV 否決，但戰略上應該做 |
| **AI-Native Living Book / Executable Knowledge Artifact** | 方法論本身的承載形式問題 |

## 步驟 3：給出「理論診斷 + intervention」

格式：

```text
## 理論診斷
- 主因（**最能解釋**）：[理論 X]
- 次因：[理論 Y]
- 引用學術依據：[Author, Year]

## 為什麼是這個理論
1. 症狀 A 對應理論的核心命題 ...
2. 症狀 B 對應 ...
3. 客戶的假設「___」與此理論的解釋不一致（這是關鍵切入點）

## 可採用的 intervention
- 短期（30 天內）：...
- 中期（3-6 個月）：...
- 長期（12-24 個月）：...

## 對應到方法論的具體工具
- Tool X.Y（在哪個檔案）
- BARS 行為錨點哪一格
- Stage Gate Criteria 補哪幾項
```

## 步驟 4：標明證據強度

- 理論是 L2 文件依據（學術 classic）
- 對客戶的具體 intervention 是 L0-L1（沒看到客戶 ground truth，僅供討論起點）
- 真要落地必須回頭跑問卷 / 訪談（升到 L1-L2）

## 紀律

- 不亂套理論：能對應就對應，不能就老實說「7 大理論都不能完整解釋」
- 不替代資料：理論只是 lens，不是答案；最終診斷需經 Phase A 流程
- 引用要可被驗證：每個理論引用對應到 ACADEMIC_THEORETICAL_FOUNDATIONS 的章節
