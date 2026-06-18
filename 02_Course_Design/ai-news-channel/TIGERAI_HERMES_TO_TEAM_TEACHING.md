# 從 Hermes Agent 到 Agent Team：用 ai-news-channel 教 L4→L5

> 🧭 **這份檔案的用途**
> 把 `ai-news-channel`（L5 完整實例）接回 **L4 Hermes Agent** 課程，讓學員看懂一件事：
> **L5 團隊不是「六個新東西」，而是「六個被治理好的 Hermes Agent，被一層 harness 串起來」。**
> 對應 [`L4_HERMES_AGENT_COURSE_PLAN.md`](../L4_HERMES_AGENT_COURSE_PLAN.md) §15「L4 到 L5 的銜接條件」與 [`TIGERAI_L5_CASE_NOTES.md`](TIGERAI_L5_CASE_NOTES.md)。
>
> ⚠️ 本檔是外掛教學層，**不改動 `ai-news-channel/` 任何原始檔**。
> 📝 本檔依使用者要求以中文為主；EN 版列為延伸 TODO。
> 🔒 情境故事為**虛構教學案例**，公司／人名一律用 ABC 公司／城市 X 式佔位符（依 [`CASE_WRITING_STANDARD.md`](../../04_Scenarios/CASE_WRITING_STANDARD.md)）。

本檔分三部分，是一條完整的教學弧：

- **Part A（#1）**——把這個案例補成「Hermes Agent 可以使用的教學」：每個 AI 成員怎麼當成一個 L4 Hermes Agent 來設計。
- **Part B（#2）**——設定一個情境故事：一家虛構公司為什麼需要這個 Agent Team。
- **Part C（#3）**——使用情境故事：帶這個團隊把那一天的任務從頭跑到尾。

---

# Part A —— 每個成員都是一個 Hermes Agent

## A.1 核心觀念：L5 是「拆開的 Hermes」

回顧 L4：一個 **Hermes Agent** 在**單一領域**裡，自己跑完七條流程——
`ingest（吃資料）→ query（查）→ update（回寫）→ lint（檢查）→ 簡報 → 探勘 → 知識圖整合`，
全部由一份 **目的檔（mission.md）** 與 **Gate 4** 治理。

L5 做的事，是把這七條流程**拆給多個專精 Agent**，再用 **harness 六層**把它們重新串成一個可治理的團隊：

| | L4 單一 Hermes Agent | L5 Agent Team（ai-news-channel） |
|---|---|---|
| 流程 | 七條流程**集中在一個** Agent | 七條流程**拆給六個** Agent |
| 治理 | 一份 `mission.md` + Gate 4 | 六份迷你目的檔 + 一部憲法（`CLAUDE.md`）+ Supervisor Gate |
| 知識庫 | Agent 自己的 Knowledge Base | 共用 `knowledge-base/`（多 Agent 寫、Librarian 維護） |
| 風險 | 一個 Agent 出錯 | **拆開反而更安全**——每個 Agent 權限更窄、被別的 Agent 把關 |

> 教學金句：**L5 不是把多個不穩定 Agent 放在一起，而是讓已經可治理的 L4 Agent 進入團隊協作。**（L4 課 §15）
> 所以——**先會做一個乾淨的 Hermes Agent（L4 Gate 4 過關），才有資格組 Agent Team（L5）。**

## A.2 七條 Hermes 流程 → 拆給哪個成員

| Hermes 流程（L4 §3.7）| 在 ai-news-channel 由誰負責 | 對應檔 |
|---|---|---|
| **ingest（吃資料）** | Researcher（抓新聞、查證來源） | `.claude/agents/researcher.md` |
| **探勘（discovery）** | Researcher（找趨勢、新來源） | 同上 |
| **query（查）** | CTO（查 topic-archive 避免重複）、Developer（查 findings） | `cto.md` / `developer.md` |
| **update（回寫）** | Librarian（把當日產出歸檔回 knowledge-base） | `librarian` / scripts |
| **lint（一致性檢查）** | Supervisor（5 項產出齊不齊、規格對不對） | `supervisor.md` + `verify_build.sh` |
| **簡報（產出）** | Developer（長文 + 社群 + 電子報）、Designer（圖卡） | `developer.md` / `designer.md` |
| **知識圖整合** | Librarian（topic-archive、project-state 跨日串接） | `constitution/project-state.md` |

> 一句話：**Researcher 是 Hermes 的「ingest 引擎」、Librarian 是 Hermes 的「知識庫主控技能」、Supervisor 是 Hermes 的「lint + Gate」。** 把 L4 學的東西，原封不動對位過來。

## A.3 給成員寫「迷你目的檔」（沿用 L4 §3.6 mission.md 格式）

L4 教過：每個 Hermes Agent 啟動先讀一份 `mission.md`（Allowed / Forbidden / Output style / Decision boundary）。
在 L5，**每個成員都該有自己的迷你目的檔**——這正是 `.claude/agents/*.md` 的 frontmatter + Hard Constraints 在做的事。下面把它「翻譯回」L4 學員熟悉的 mission.md 格式。

### 範例 1：Researcher Agent（= Hermes 的 ingest + 探勘）

```markdown
# Mission（相關性過濾用）
本 Agent 服務 AI 新聞頻道，負責蒐集當日 AI 產業新聞、查證來源，產出 findings 給 Developer。
不寫文章、不做設計、不發布。

## Allowed input types
- AI 產業新聞（官方部落格、論文、可信媒體）
- 趨勢訊號（GitHub trending、研究機構發布）

## Forbidden input types
- 未經查證的單一來源爆料（最少 3 個獨立來源才採用）
- 設計／視覺任務（→ 交給 Designer）
- 與 Designer 共用上下文（Context Isolation：兩者不得互相餵 context）

## Output style
- findings 寫進 working-notes/researcher-findings.md
- 每則新聞附 ≥ 1 來源 URL，整篇 ≥ 3 個獨立來源

## Decision boundary
- 來源 < 3 或可信度存疑 → 標註「待查證」，不下結論
- 不替 CTO 決定編輯角度（那是 CTO 的事）
```

### 範例 2：Librarian Agent（= Hermes 的知識庫主控技能 + update + lint）

```markdown
# Mission
本 Agent 是團隊的知識庫管家：每個 cycle 結束把產出歸檔、更新 project-state、維護 topic-archive 避免重複。

## Allowed
- 讀寫 knowledge-base/、constitution/project-state.md、topic-archive.md
- 歸檔 deliverables/<日期>/

## Forbidden
- 寫內容、做編輯決策、發布（只做帳務性歸檔——對應 L4 §2.5「工具做帳務、LLM 做判讀」）

## Decision boundary
- 主題與過去 7 天重複 → 在 topic-archive 標記，回報 CTO
```

### 範例 3：Supervisor Agent（= Hermes 的 lint + Gate）

```markdown
# Mission
本 Agent 是發布前最後一道關。驗證 5 項產出齊全、合規格、對得上 CTO 驗收標準。不修內容，只 PASS / FAIL。

## Decision boundary（硬規則，對應原始 supervisor.md）
- 任一交付物缺 → 一律 FAIL
- 文章字數不在 800-1200 → FAIL
- 來源 < 3 → FAIL
- FAIL → 寫修正指示給 Developer，最多 2 輪；2 輪還 FAIL → 升 PM
```

> 其餘三個成員（CTO / Developer / Designer）的迷你目的檔，留作 **課堂作業**（見 Part C §C.6 活動）。
> 對位練習：把每個成員的 `.claude/agents/xxx.md` 翻寫成 L4 的 `mission.md` 格式，學員就會發現——**L5 的 agent 定義檔，就是 L4 mission.md 的多 Agent 版。**

## A.4 從「一個 Hermes」到「一個團隊」要補的三件事

學員若已會做單一 Hermes Agent，升 L5 只要再補三件（這也是 harness 六層裡 L4 還沒強調的部分）：

1. **Loop（迴圈）**——固定誰先誰後（`CLAUDE.md` The Fixed Loop）。單一 Hermes 不需要，多 Agent 一定要。
2. **Context Isolation（脈絡隔離）**——Researcher 與 Designer 不共用 context（`ai-member-boundaries.md`）。單一 Hermes 沒有這問題。
3. **跨 Agent 的 Gate**——單一 Hermes 的 Gate 4 在 Agent 內部；L5 把關搬到一個獨立的 Supervisor + PM（Verification 層）。

---

# Part B —— 情境故事設定（虛構教學案例）

> 依 [`CASE_WRITING_STANDARD.md`](../../04_Scenarios/CASE_WRITING_STANDARD.md)：寫清楚產業、規模、部門、系統、痛點，並說明**為什麼是 L5**。

## B.1 公司背景

| 欄位 | 內容 |
|---|---|
| 公司 | **ABC 公司**（虛構）|
| 產業 | B2B SaaS（企業流程自動化軟體）|
| 規模 | 約 200 人，總部在城市 X |
| 部門 | 行銷部（含內容行銷組 3 人）|
| 現有系統 | 官網部落格（Medium 風格 CMS）、企業社群帳號（X / LinkedIn / Threads）、電子報平台、Notion 內容行事曆 |
| 部署模式 | 雲為主（內容皆為公開素材，無機敏資料）|

## B.2 痛點（為什麼需要 Agent Team）

ABC 公司想用「**每天一篇 AI 產業洞察**」建立思想領導地位，替主產品帶來 inbound leads。但內容行銷組只有 3 個人：

- **產能跟不上**：要「每天」跨 4 個平台（長文 + X + LinkedIn + Threads + 電子報 + 圖卡）穩定產出，3 個人做不到。
- **品質不穩**：趕稿時來源沒查證、字數忽長忽短、社群貼文超字數、圖卡規格錯。
- **主題會撞**：常不小心寫到上週寫過的題目。
- **知識不累積**：寫完就散在各處，沒人歸檔，明年又從零開始。

## B.3 為什麼不是 L1-L4，而是 L5？

| 層級 | 為什麼不夠 |
|---|---|
| L1 Chat | 個人問答，無法每天穩定跨平台產出 |
| L2 Skill | 有「寫貼文」Skill 也只是片段，無法串成一條每日產線 |
| L3 Workflow | n8n 能自動發布，但**不會自己想題目、查證、把關品質** |
| L4 單一 Hermes | 一個 Agent 同時要研究 + 寫作 + 設計 + 把關，**權限太大、職責不分、出錯沒人擋** |
| **L5 Agent Team** ✅ | **分工 + 互相把關**：Researcher 查證、CTO 出題、Developer 寫、Designer 出圖、Supervisor 把關、PM 核准。這正是 ai-news-channel 的設計。 |

> 升級觸發條件（對照 L4 §15）：ABC 公司已有 L1-L4 基礎（內容行銷組會用 Chat、有幾個寫作 Skill、有 n8n 發布 Workflow），且高風險動作（對外發布）需要人工 Gate——**完全符合進 L5 的條件。**

## B.4 角色設定（職稱依方法論規範）

| 角色 | 職稱 | 在 Agent Team 的位置 |
|---|---|---|
| 專案發起人（AI 導入 sponsor）| **行銷副總**（CXO 級 = 副總＋）| 不在每日 loop 內，季度看 ROI |
| 人類 PM（每日 loop 的人）| **內容行銷經理** | 下 daily brief、最後核准發布（PM Approve）|
| IT 支援（部署 / 串接）| **資訊協理**（IT Director）| 只在建置期，串接 CMS / 社群 API |
| 6 個 AI 成員 | —— | CTO / Researcher / Developer / Designer / Supervisor / Librarian |

## B.5 問卷與成熟度判定（摘要）

| 項目 | 判定 |
|---|---|
| 目前成熟度 | L3（有 Chat、有 Skill、有發布 Workflow，但無自主團隊）|
| 目標成熟度 | L5（內容產線交給 Agent Team，人只下題 + 核准）|
| 課程比例建議 | L4 補強 20%（先讓每個成員是乾淨 Hermes）+ L5 主體 80% |
| 部署 | 雲（公開內容，無機敏）|

---

# Part C —— 使用情境故事：跑一天

> 用 ABC 公司情境，帶整個團隊把 **2026-05-22 這天** 從 brief 到發布跑一遍。每一步標出對應的 **Hermes 流程**、**Harness 層** 與 **產出檔**。

## C.1 當日 brief（PM，人類）

> 內容行銷經理在 `working-notes/pm-brief.md` 寫下：
> 「今天主題：**企業導入 AI 助理時最常見的 3 個治理盲點**。角度要務實、給 IT 主管看、避免炒作。」

- **Harness 層**：Loop 起點。**Hermes 對應**：人類提報（L4 §2.3 P1，最高優先）。

## C.2 CTO（編輯架構，不寫內容）

> CTO 先 `query` topic-archive → 確認過去 7 天沒寫過「AI 治理盲點」→ 在 `cto-analysis.md` 產出：
> - 標題 3 選 1、副標、文章結構（Intro → 盲點 1/2/3 → CTA）、目標 900 字
> - 給 Researcher 的研究題目：「找 3 個治理盲點的真實案例 + 數據，≥ 3 獨立來源」
> - 給 Supervisor 的驗收標準

- **Hermes 流程**：query（查 archive）+ orient-first。**Harness 層**：Context（先讀憲法 + archive）。**硬規則**：CTO 不寫內容（Constraints）。

## C.3 Researcher（= Hermes ingest 引擎）

> Researcher 蒐集新聞、查證，在 `researcher-findings.md` 產出 3 個盲點各附 2-3 個獨立來源 URL + 關鍵數據。

- **Hermes 流程**：ingest + 探勘 + 來源分析。**Harness 層**：Tools（只有查找權限）。**Decision boundary**：某盲點只找到 1 個來源 → 標「待查證」，不硬湊。
- **Context Isolation**：Researcher 不把 findings 直接餵給 Designer（兩者隔離）。

## C.4 Developer（簡報產出）

> Developer 讀 `cto-analysis.md` + `researcher-findings.md`，產出 4 件：
> `deliverables/2026-05-22/article.md`（長文）、`social-posts.md`（X / LinkedIn / Threads）、`newsletter.md`（電子報）；
> 並寫 `developer-summary.md` 交棒。

- **Hermes 流程**：簡報（產出）+ query（查 findings）。**Harness 層**：Persistence（全部寫進 `knowledge-base/deliverables/`）。**硬規則**：Developer 不直接發布，要過 Supervisor（Constraints）。

## C.5 Designer + Supervisor（把關）

> Designer 產出圖卡 prompt（2500×1686 + 1080×1080）寫進 `image-prompt.md` + `designer-output.md`。
> Supervisor 跑 `verify_build.sh --date 2026-05-22`：

```
📄 article.md ✅  social-posts.md ✅  image-prompt.md ✅  newsletter.md ✅
📝 字數：1320 字 ❌（超過 1200）
🔗 來源：4 個 ✅
🐦 Twitter：265 字 ✅
🖼️ 2500×1686 ✅  1080×1080 ✅
❌ VERIFICATION: FAIL —— Article word count 1320 outside 800-1200
→ Return to Developer for revision.
```

> Supervisor 把「字數超標」寫進 `supervisor-report.md`，退回 Developer。Developer 砍到 1150 字，第 2 輪 → **PASS**。

- **Hermes 流程**：lint。**Harness 層**：Verification（機器 `verify_build.sh` + 人 Supervisor）。
- **教學點**：這就是 L5 比 L4 安全的地方——**單一 Hermes 不會自己抓自己的字數超標，但團隊有獨立把關者。**

## C.6 PM 核准 + 發布 + 歸檔

> 內容行銷經理看 Supervisor 的 PASS 報告 → 核准 → `run_daily.sh --publish` 發布到各平台。
> Librarian 把 deliverables 歸檔、更新 `project-state.md`、把今天主題寫進 `topic-archive.md`（明天 CTO 才不會撞題）。

- **Hermes 流程**：update + 知識圖整合。**Harness 層**：Persistence + 人工 Gate（PM Approve）。

## C.7 這一天的 IPOE（對應 CASE_WRITING_STANDARD §3）

| 類別 | 內容 |
|---|---|
| **Input** | PM brief（主題 + 角度）、topic-archive、過去文章風格 |
| **Process** | Fixed Loop：CTO 出題 → Researcher 查證 → Developer 寫 → Designer 出圖 → Supervisor lint → PM 核准 |
| **Output** | 1 長文 + 3 社群貼文 + 1 電子報 + 1 圖卡，全歸檔於 `deliverables/2026-05-22/` |
| **Evidence** | `verify_build.sh` PASS log、`supervisor-report.md`、各 working-notes、發布 URL、topic-archive 更新紀錄 |
| **驗收標準** | 5 項產出齊全 + Supervisor PASS + PM 核准 + 已歸檔 |

## C.8 Gate 5 與 ROI（情境版）

**Gate 5 通過條件**（對照 L5 課 §10）：

- [x] ≥ 1 個完整 Agent Team cycle 跑通（本日已示範）
- [x] 每個 Agent 有角色 / Input / Output / 限制（迷你目的檔，Part A）
- [x] 有整合 + 把關（Supervisor + PM）
- [x] 有 Human Gate（PM Approve）
- [x] 有 ROI 與治理設計（見下表）

**ROI（ABC 公司情境，示意）**：

| 指標 | 導入前（3 人手做）| 導入後（Agent Team + 1 PM 核准）|
|---|---|---|
| 每日跨平台完整產出 | 做不到 / 斷續 | 每日穩定 6 件 |
| 內容組人力投入 | 3 人幾乎全投入 | 1 人每日約 30 分鐘（下題 + 核准）|
| 主題撞題 | 偶發 | topic-archive 自動擋 |
| 來源查證 | 趕稿時略過 | Researcher 硬規則 ≥ 3 來源 |
| 知識累積 | 散落 | 全歸檔、可回溯 |

## C.9 課堂活動（接 Part A，對應 Gate 5）

| # | 活動 | 練到 | 產出 |
|---|---|---|---|
| 1 | 替 CTO / Developer / Designer 補寫迷你目的檔（L4 mission.md 格式）| A.3 | 3 份目的檔 |
| 2 | 把 ABC 公司情境換成自己公司，重寫 `pm-brief.md` + 改 `CLAUDE.md` Team 表 | B + Loop | 自製 brief + 憲法 |
| 3 | 設計一個會讓 Supervisor FAIL 的情況，並寫出修正流程 | Verification | 1 份 FAIL→PASS 走查 |
| 4 | 為 ABC 公司情境填一張 L4 Agent 任務卡（給 Researcher）| A + L4 | [`L4_AGENT_TASK_CARD.md`](../_deliverables/L4_AGENT_TASK_CARD.md) 填寫版 |

---

## 交叉連結

- L4 課程：[`L4_HERMES_AGENT_COURSE_PLAN.md`](../L4_HERMES_AGENT_COURSE_PLAN.md)（§3.6 mission.md、§15 L4→L5 銜接）
- L4 任務卡範本：[`_deliverables/L4_AGENT_TASK_CARD.md`](../_deliverables/L4_AGENT_TASK_CARD.md)
- L5 案例導讀：[`TIGERAI_L5_CASE_NOTES.md`](TIGERAI_L5_CASE_NOTES.md)
- Harness 六層：[`90_References/HARNESS_ENGINEERING_REFERENCE.md`](../../90_References/HARNESS_ENGINEERING_REFERENCE.md)
- 案例撰寫標準：[`04_Scenarios/CASE_WRITING_STANDARD.md`](../../04_Scenarios/CASE_WRITING_STANDARD.md)

---

**版本：** v0.1（2026-05-22）
**作者：** Morris Lu（盧業興）· Tiger AI 虎智科技
**授權：** 隨本 toolkit（程式 Apache 2.0 / 文件 CC BY 4.0）
**情境聲明：** ABC 公司為虛構教學案例，與任何真實公司無關。
