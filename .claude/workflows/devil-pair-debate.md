# /devil-pair-debate

> Claude Code-Native — 雙 Claude 真實辯論 (Two-Claude Adversarial Debate)
> 用途：對方法論的某個前提 / 章節 / 決策，讓 Claude **同時持有兩個對立位置**辯論 3-5 回合，再由第三個 Claude 綜合。暴露的不是 bug，是**價值觀預設**。
>
> 為什麼只有 Claude Code 能做：Codex `/red-team-review` 是**單向攻擊**；這個是**雙向真實辯論**，需要在同一 context window 內讓兩個 persona 真誠地對立，不取巧。

## 步驟 1：選定辯論議題

請使用者指定要辯論什麼。建議是**方法論的價值觀預設**而不是 bug：

### 適合本工作流的議題

- 「Tool 3.6 客戶 Ideal Practice 三方簽署 = paternalism？」
- 「BARS 行為錨點是不是 algorithmic discrimination 的當代版？」
- 「L4-L5 自主 AI 是不是把員工從『執行者』降格為『監督機器人的人』？」
- 「強推 8 階段流程是不是顧問業的 colonial knowledge transfer？」
- 「Real Options 邏輯是不是合理化短期看不出 ROI 的浪費？」
- 「『AI-Native Living Book』是不是把方法論商品化的包裝術？」

### 不適合的議題（請改用其他工作流）

- 「Tool 6.3 是不是漏了哪個維度」→ 用 Codex `/consistency-review`
- 「報告寫得太樂觀」→ 用 Codex `/red-team-review`
- 「客戶 M 該不該做 L4」→ 用 `/parallel-perspectives`

## 步驟 2：分配 3 個 Claude persona

整場辯論明確切換：

| Persona | 立場 | 任務 |
| --- | --- | --- |
| **Claude-A（傳教士）** | 為方法論辯護 | 真誠相信 8 階段 / L1-L5 / BARS 的價值，給出最強論證 |
| **Claude-B（批評者）** | 攻擊方法論前提 | 真誠質疑，引用批判理論、組織政治、權力分析 |
| **Claude-C（法官）** | 不取邊 | 最後綜合，標出真正的 tension 與可能的 reconciliation |

**鐵則**：A 和 B **不能取巧**。A 不能寫稻草人攻擊讓 B 容易反駁；B 不能虛無主義說「全部都是建構」。**兩邊都必須在自己最強的位置**。

## 步驟 3：辯論 3 回合

每回合格式：

```text
### Round N

[Claude-A 傳教士]
論點：...
證據：[檔案 §章節]
為什麼這論點站得住：...

[Claude-B 批評者]
回應 A 的論點：...
但更深的問題是：...
引用：[Foucault / Bourdieu / Habermas / Goffman / Scott / 等批判學派]
證據：...
```

**回合間漸進**：

- Round 1：表面交鋒
- Round 2：B 找出 A 的價值觀預設；A 必須承認或反駁
- Round 3：A 找出 B 的虛無主義漏洞；B 必須承認或建設性回應

## 步驟 4：Claude-C 法官綜合

```text
[Claude-C 法官]

## 真正的 tension（不是表面歧見）
A 和 B 在以下根本問題上對立：...

## 雙方都對的部分
- A 對的：...
- B 對的：...

## 雙方都避開的盲點
- 兩邊都沒提到：...

## 可能的 reconciliation
1. 結構性方案：...
2. 程序性方案：...
3. 接受 tension 共存（無法 reconcile，但可治理）

## 對方法論的具體 patch 建議
- 章節 X 加上：...
- 章節 Y 改為：...
- 新增章節：「方法論的價值觀預設與限制」
- 新增警語：[具體文字]
```

## 步驟 5：產出**辯論成果**給方法論

```text
## 議題：[XXX]

## 結論（3 種可能）
### A. 強 reconciliation：A 和 B 的對立可以解決
方法 → ...

### B. 弱 reconciliation：可以治理但無法解決
方法 → 顯式承認，加警語

### C. 不可調和：方法論必須選邊
方法 → 公開立場，承擔後果

## 給方法論的具體變動建議
- [檔案 X §Y] 修改：...
- 新增的限制聲明：...
- 配合的 governance 機制：...

## 給 Codex `/methodology-patch` 的 input
（讓 Codex 把上述建議變成 markdown patch）
```

## 紀律

- **A 和 B 都要真誠**：禁止稻草人攻擊、禁止虛無主義
- **引用真實批判理論**：B 必須引用 Foucault / Bourdieu / Habermas / Scott / Goffman / Said 等真實學派，不能編
- **不取笑**：批判性辯論不是嘲諷，每一句都要有重量
- **法官不要溫吞**：Claude-C 必須明確指出**真正的 tension 在哪**，不能寫「兩邊都有道理」這種廢話
- **產出可被使用**：辯論結尾必須給方法論具體的 patch 建議，不能停在純理論

## 典型應用場景

- 方法論發表前：跑 1-2 個自我辯論，主動暴露盲點寫進「Limitations」章節
- 學術投稿前：reviewer 會質疑的角度先在內部辯論一次
- 監管文件提交前：主動處理批判性質疑（提升可信度）
- 顧問內部訓練：訓練顧問**自己**思考方法論的價值觀預設
- 對接 Codex `/academic-upgrade`：辯論結果 → 章節 patch
