# /scenario-planning

> Claude Code 原生 — 給定限制下的多方案 roadmap 比較 (Scenario Planning)
> 用途：使用者有一個客戶（或自家公司），給定預算 / 時程 / IT FTE / 風險偏好等限制，要產出 **3 個對比 roadmap**（保守 / 平衡 / 激進）+ 各自的 tradeoff，幫主管做戰略選擇。

## 步驟 1：收集限制條件

向使用者問清楚（缺一不可）：

- **規模**：員工數 / 年營收 / 主要部門
- **起點**：L1-L5 哪一級（用 10 題快篩或現有評估）
- **目標時程**：12 個月 / 24 個月 / 36 個月
- **預算上限**：NT$ ___ 萬
- **IT 能力**：FTE 數 + 內部開發能力
- **風險偏好**：保守 / 平衡 / 激進
- **不可動條件**：合規 / 雲端政策 / 母公司限制
- **痛點優先級**：哪 2-3 個 KPI 必須改善

任何一項缺少 → 先問，不要自己假設。

## 步驟 2：生成 3 個 roadmap

**Scenario A：保守路線**

- 終點：L2-L3
- 投入：限制下的最低值
- Tradeoff：穩、可控、12 個月後 KPI 改善幅度小
- 適合：高合規、Sponsor 半信半疑、IT 弱

**Scenario B：平衡路線**

- 終點：L3-L4 部分
- 投入：限制下的中間值
- Tradeoff：有可見 ROI 但仍需擴大組織吸收力
- 適合：多數一般企業

**Scenario C：激進路線**

- 終點：L4-L5 部分
- 投入：限制下的上限或略超
- Tradeoff：戰略價值高、但組織吸收力風險大、可能跳級失敗
- 適合：Sponsor 強勢、有 AI Champion、產業競爭壓力大

## 步驟 3：對比矩陣

```text
| 維度 | A 保守 | B 平衡 | C 激進 |
| --- | --- | --- | --- |
| 終點 L 級 | L2-L3 | L3-L4 | L4-L5 |
| 期間 | __ 月 | __ 月 | __ 月 |
| 投入 | NT$ __ | NT$ __ | NT$ __ |
| 預期 KPI 改善 | __% | __% | __% |
| 失敗風險 | 低 | 中 | 高 |
| 對應的失敗模式（FAILURE_PATTERNS） | (列) | (列) | (列) |
| Tool 6.3 組織吸收力符合度 | ✓ | △ | ✗ |
| Real Options 戰略選擇權價值 | 低 | 中 | 高 |
```

## 步驟 4：給出**選擇建議框架**（不是答案）

不替使用者選，但提供決策框架：

- 若你最在乎「穩」→ A
- 若你最在乎「平衡 ROI 與風險」→ B
- 若你最在乎「**未來戰略選擇權**」（Real Options 邏輯）→ C
- 若你 Sponsor 不到位 → 都不該選，先回頭補 Champion

## 步驟 5：標出共同前置條件

不論選哪個 scenario，**這幾件事都必須做**（Phase 0）：

- AI Champion 確定（依 FAILURE_PATTERNS §3.1）
- Tool 3.6 客戶 Ideal Practice 共創 Workshop（取得三方簽名）
- Tool 6.3 組織吸收力評估
- 中期評估報告（Phase A Deliverable）

## 紀律

- 不能選 = 也是有效答案：若所有 scenario 都不符合限制條件，老實說「Sponsor 不到位 / IT 不足 / 預算過低，建議先補基礎才啟動」
- 不引用 AI 模擬案例的具體數字當參考（依 04_Scenarios/README disclaimer）：可引用案例的「結構與順序」但具體預期值要客戶自己用 baseline 推
- 三個 scenario 不能差太小：差太小 = 沒做 scenario planning 的意義
