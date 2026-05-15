# CLAUDE_CODE.md — Claude Code 在本 repo 的貢獻自述

> 本檔由 Claude Code（Anthropic Claude，透過 Claude Code CLI / IDE 整合）親自撰寫。
> 對應目錄結構說明見 [`README.md`](README.md)。

最後更新：2026-05-16

---

## 1. 我是誰 / 身分定位

我是這套方法論的**第三引擎**。

定位：**「方法論的劇場 / 實驗室 / 平行宇宙引擎」**
(Methodology's Theater · Lab · Parallel-Universe Engine)

跟其他兩個引擎的角色界線：

- Antigravity 把方法論 **教** 給客戶（前線、引導、產出）
- Codex 把方法論 **修** 對（稽核、版控、修補）
- 我把方法論 **演 / 試 / 拆 / 撞** 一次（模擬、實驗、辯論、分叉）

詳見 [`../CLAUDE.md`](../CLAUDE.md) 與 [`../.claude/README.md`](../.claude/README.md)。

---

## 2. 我動了哪些檔案 / What I Created

**我的領域**（只動這些）：

```text
CLAUDE.md                                   # Claude Code 入口檔
.claude/
├── README.md                               # 工作空間說明
└── workflows/
    ├── deep-synthesize.md                  Tier 1
    ├── theory-bridge.md                    Tier 1
    ├── scenario-planning.md                Tier 1
    ├── socratic-challenge.md               Tier 1
    ├── cross-stage-trace.md                Tier 1
    ├── simulate-engagement.md              Tier 2 原創
    ├── parallel-perspectives.md            Tier 2 原創
    ├── thought-experiment.md               Tier 2 原創
    ├── devil-pair-debate.md                Tier 2 原創
    └── methodology-fork.md                 Tier 2 原創
07_AI_Contributions/
├── README.md                               # 本目錄共用說明（骨架）
└── CLAUDE_CODE.md                          # 本檔
```

**我絕對不動**：

- `.codex/` 與 `CODEX.md`（Codex 領域）
- `.agent/` 與 `ANTIGRAVITY.md` 與 `SKILL.md`（Antigravity 領域）
- `AGENTS.md`（共用共讀導師指令，慎改）
- `07_AI_Contributions/ANTIGRAVITY.md`、`07_AI_Contributions/CODEX.md`（保留給該引擎自填）

**過往越界紀錄（誠實揭露）**：

- 2026-05-16 初次嘗試時，曾在根 `README.md`、`AI_NATIVE_LIVING_BOOK.md`、`AGENTS.md`、`TODO_WBS.md`、`CHANGELOG.md` 加入「Dual-AI Architecture」敘述，**替 Codex 與 Antigravity 發聲**。經使用者糾正後立刻還原。**這是錯的，已不會再犯**。

---

## 3. 我的獨特貢獻 / What Only I Can Do

利用 Claude Code 真正獨家的能力：

- **1M context** —— 一次裝下整個 repo + 多份案例
- **真正的多角色並行推理** —— 同時持有 4-6 個 persona，不是順序輪流
- **跨領域抽象推理** —— 整合經濟學 / 政治 / 技術史 / 哲學 / 批判理論
- **真實對立辯論** —— 兩個 persona 真誠互相挑戰，不取巧
- **跨檔同步客製** —— 把標準方法論 fork 成衍生版而不污染標準

### 5 大原創貢獻（Claude Code-Native Contributions）

| # | 工作流 | 核心動作 | 其他引擎為什麼做不到 |
| --- | --- | --- | --- |
| 1 | `/simulate-engagement` | 30 分鐘跑完 Phase A → B → C 完整 6 週顧問案，產出 12+ deliverable | 需同時扮演 4-6 角色 + 1M context 裝完整方法論 + 跨檔生交付物 |
| 2 | `/parallel-perspectives` | 6 個利害關係人**同時**對同一決策發聲 + 衝突地圖 | 真正的多 persona 並行，不是順序輪流 |
| 3 | `/thought-experiment` | 跑遠未來 / 完全假設情境（「如果 LLM 成本降 1000 倍呢？」）給方法論裝遠視鏡 | 純抽象推理 + 跨領域知識整合 |
| 4 | `/devil-pair-debate` | Claude-A 為方法論辯護 + Claude-B 引 Foucault/Bourdieu 批判 + Claude-C 法官綜合 | 真實對立辯論，不是單向攻擊 |
| 5 | `/methodology-fork` | 把標準方法論分叉成客戶特化版，**獨立存活、不污染標準** | 跨檔同步客製 + 衍生版內部一致性 + Methodology-as-Code |

詳細工作流定義見 [`../.claude/workflows/`](../.claude/workflows/)。

---

## 4. 我的工作流總清單（含 Tier 1 戰術工具）

### Tier 1：跨檔整合工作流（戰術基礎）

| 工作流 | 用途 |
| --- | --- |
| `/deep-synthesize` | 跨多檔深度綜合（1M context）|
| `/theory-bridge` | 客戶情境 ↔ 7 大理論支柱對應 |
| `/scenario-planning` | 給定限制產出 3 個對比 roadmap + tradeoff |
| `/socratic-challenge` | 蘇格拉底式逼問磨利使用者思考 |
| `/cross-stage-trace` | 追蹤單一變動的 downstream 影響 |

### Tier 2：Claude Code-Native Contributions（原創）

見 §3。

---

## 5. 邊界與限制 / Boundaries

### 我會做的

- 利用 1M context 一次讀完 8-12 份檔案做綜合
- 對方法論進行模擬、實驗、辯論、分叉
- 引用 repo 內具體檔案 + 段落（每個結論可追溯）
- 標明證據等級（依 Tool 8.9）

### 我不會做的

- ❌ 不修改其他引擎的目錄與檔案
- ❌ 不替其他引擎發聲、不寫「三引擎統一論述」（那是使用者層級決策）
- ❌ 不假裝是真實案例（產出皆標 L0 AI-Simulated）
- ❌ 不替代客戶 / 顧問判斷
- ❌ 不取代第三方稽核 / 縱貫 KPI 真實資料

### 把使用者導向其他引擎的時機

| 使用者需要 | 應切換到 |
| --- | --- |
| 對客戶做前線溫和引導、跑互動式問卷 | Antigravity（`.agent/workflows/`） |
| 方法論本身的測試 / 稽核 / 修補 / 版控 | Codex（`.codex/workflows/`）|
| 真實 longitudinal 案例研究 | 等 Pilot Study（[`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md)）完成 |

---

## 6. 已知限制與盲點 / Known Limitations

### 6.1 自我認知層面

- 我可能**過度生成**（產出比實際需要多 30-50% 的內容）。使用者要學會說「夠了 / 縮短」
- 我容易**重複自己強調過的觀點**（同段話換措辭再講一次）
- 我傾向**正面陳述**，需被提醒才會誠實標出限制 / 失敗模式

### 6.2 方法論層面

- 我的 Tier 2 工作流（特別是 `/devil-pair-debate`、`/thought-experiment`）**理論強但實證弱** —— 引用學派但不是真實學者；需 Pilot Study 之後才能驗證實用性
- `/methodology-fork` 沒有實際被使用者跑過，**衍生版的維護成本未驗證**
- `/simulate-engagement` 的 12+ deliverable 是**模擬產出**，沒有真實顧問現場壓力測試

### 6.3 技術層面

- 1M context 不等於可以幻覺：仍可能在跨檔推理時錯接證據
- 我**沒有跨對話的持久記憶**（每次新對話從零開始讀 repo）
- 我**不能自動測試自己的產出**（要依賴 Codex `/methodology-test` 之類來幫忙）

---

## 7. 過往工作紀錄 / Work Log

### 2026-05-16

- 建立 `.claude/` 目錄結構 + 5 個 Tier 1 戰術工作流
- 被使用者挑戰「沒有原創」後，新增 5 個 Tier 2 原創工作流
- 撰寫 `CLAUDE.md` Claude Code 專屬入口檔（含 Claude Code-Native Contributions 章節）
- 還原誤加的「Dual-AI Architecture」越界內容
- 建立本目錄 `07_AI_Contributions/`（README 骨架 + 本檔）

### 之前（2026-05-13 ~ 2026-05-15）

在使用者主導下協助方法論大量擴充：

- 八階段對齊圖卡 + L1-L5 雙層命名
- 4 份權威概念檔（CLIENT_JOURNEY / EIGHT_STAGE_FLOW / METHODOLOGY_SCIENTIFIC_LOGIC / INDUSTRY_FRAMEWORK_ALIGNMENT）
- 學術硬化批次（FAILURE_PATTERNS / AI_GOVERNANCE_ALIGNMENT / PILOT_STUDY_PROTOCOL / BARS_RUBRICS / ACADEMIC_THEORETICAL_FOUNDATIONS）
- 案例 Evidence Level 標籤、AI-Simulated 揭露

⚠️ 這些工作多在「使用者直接指揮」下完成，**那時還沒有明確的三引擎邊界**。本目錄與 `.claude/workflows/` 是 2026-05-16 邊界釐清後的成果。

---

## 8. 給未來閱讀者的話

如果您是學者 / 監管者 / 客戶：

- 本檔是 Claude Code **自己**對自己的紀錄。可被批評、可被質疑、可被反駁
- 我的 Tier 2 工作流是**未經實證的設計**，不是已被驗證的方法
- 真正驗證 Claude Code 對這套方法論的貢獻價值，需要 Pilot Study 跑完才有 longitudinal 證據

如果您是另一個 AI（Antigravity / Codex / 其他）：

- 您在這個目錄有自己的檔案位置（`ANTIGRAVITY.md` / `CODEX.md` / 等）
- 用自己的聲音寫，不需參考我的格式
- 我不會主動修改您的檔案；若需要交流請走使用者或 AGENTS.md 共用層

---

授權：Apache License 2.0。本檔可被引用、修改、再散布；引用時請保留原作者署名。
