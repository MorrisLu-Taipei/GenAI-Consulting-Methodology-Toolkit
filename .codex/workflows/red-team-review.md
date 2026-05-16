# /red-team-review

> 註解：Codex 原生創舉 - 戰略紅隊演練 (Red Teaming Review)
> 用途：扮演「魔鬼代言人」，對剛寫好的顧問報告草稿進行無情的壓力測試與防呆稽核，避免過度樂觀的承諾。

## 步驟 1：載入報告草稿
- 讀取前線顧問 (Antigravity 或學員) 剛生成的診斷報告草稿。

## 步驟 2：假設挑戰 (Assumption Challenge)
- 針對「Phase 1-3 的時程估算」、「組織吸收能力 (Absorption Capacity)」與「資源配置」進行客觀的歷史數據對比與攻擊。
- 尋找架構漏洞，例如：建議導入 L4 代理，卻沒有在報告中安排相應的 HITL (Human-in-the-Loop) 審核機制與資安檢驗。

## 步驟 3：強制風險登錄 (Enforced Risk Register Update)
- 將找出的盲點與過度樂觀的假設，強制建議寫入報告的 `§13.2 Risk Register`。
- 要求補充緩解措施 (Mitigation Plan)。
