# Tiger AI L5 教學案例導讀：ai-news-channel / L5 Teaching-Case Guide

> 🧭 **這份檔案的用途 / What this file is for**
> 這是把 `ai-news-channel` 接進《GenAI Consulting Methodology Toolkit》的「導讀層」。`ai-news-channel` 本身是一個**可讀、可跑的完整 L5（Agent Team）專案**；本檔說明它在方法論裡的定位、怎麼當教材用、每個檔案對應哪一個 **Harness 六層** 與哪一個 **L5 教學構件**。
> This is the "reader's guide" that wires `ai-news-channel` into the *GenAI Consulting Methodology Toolkit*. The project itself is a **readable, runnable, complete L5 (Agent Team) project**; this file explains its place in the methodology, how to teach with it, and how each file maps to a **Harness layer** and an **L5 teaching construct**.
>
> ⚠️ **不要改動本資料夾的原始檔。** 本檔是「外掛導讀」，原專案（`README.md` / `CLAUDE.md` / `constitution/` / `.claude/`）保持原樣，作為學員閱讀的「真實成品」。
> ⚠️ **Do not modify the original files in this folder.** This guide is an *overlay*; the original project stays intact as the "real artifact" students read.

---

## 1. 它在方法論裡是什麼 / Where it sits in the methodology

| 問題 / Question | 答案 / Answer |
| --- | --- |
| 屬於哪一層？ / Which maturity layer? | **L5 — Agent Team（多 Agent 自組成團隊）** |
| 它教的核心概念？ / Core concept? | **Harness Engineering 六層模型** — 見 [`90_References/HARNESS_ENGINEERING_REFERENCE.md`](../../90_References/HARNESS_ENGINEERING_REFERENCE.md) |
| 和 ClawTeam 課的關係？ / Relation to the ClawTeam course? | ClawTeam 是**平台**（CLI 機制）；本案是**完整實例**（憲法 + 治理長什麼樣）。見三件套：[`L5_CLAWTEAM_COURSE_PLAN.md`](../L5_CLAWTEAM_COURSE_PLAN.md) §4.5 |
| 授權 / License | 本 toolkit 原創作品，隨 toolkit（程式 Apache 2.0 / 文件 CC BY 4.0）；**無外部上游、無需 NOTICE** |

> 一句話：**ClawTeam 教「怎麼讓 Agent 們動起來」，本案教「一個動得起來、又管得住的 Agent Team 長什麼樣」。**
> In one line: **ClawTeam teaches *how to make agents move*; this case teaches *what a moving — yet governed — Agent Team actually looks like*.**

---

## 2. 一頁看懂這個 Team / The team at a glance

1 位人類 PM + 6 個 AI 成員，跑一條**固定迴圈**，每天自動產出 1 篇長文 + 3 則社群貼文 + 1 張圖卡 + 1 封電子報：

```
PM 設定當日 brief
  → CTO（編輯架構 / 出題，不寫內容）
    → Researcher（找新聞、查證來源）
      → Developer（產生內容、排版）
        → Designer（圖卡 prompt）
          → Supervisor（驗證 5 項產出，PASS 才放行）
            → PM（最終核准）→ Publish
```

**鐵律：不跳步、Supervisor 不 PASS 不出貨。** 這正是 L5 與 L4（單一 Agent）最大的差異——**分工 + 把關**。

---

## 3. 檔案 → Harness 六層 → L5 構件 對照表 / File → Harness Layer → L5 Construct

這是本案最值得帶學員逐格走查的一張表。**打開左欄的檔案，對照它落在哪一層、對應方法論裡哪個構件。**

| Harness 層 | 在本案打開哪個檔 / Open this file | 對應 L5 教學構件 / Maps to L5 construct |
| --- | --- | --- |
| **1. Loop** | `CLAUDE.md` → "The Fixed Loop"；`README.md` → "The Fixed Loop" | 任務依賴鏈 / `--blocked-by`（[`L5_CLAWTEAM_COURSE_PLAN`](../L5_CLAWTEAM_COURSE_PLAN.md) §6.4）|
| **2. Tools** | `.claude/agents/cto.md` 等 frontmatter 的 `tools:`（CTO=`Read,Write,Glob`；Supervisor 加 `Bash`）| 角色卡的「Primary Skill(s)」欄（§1 角色卡範本）|
| **3. Context** | 每個 agent「On Every Invocation」第一步讀 `CLAUDE.md`+`constitution/`；`constitution/skill-stack.md` | 「AI 看得懂的活書」共讀；IPOE 的 Input 來源 |
| **4. Persistence** | `knowledge-base/`（deliverables / decisions / project-docs/topic-archive.md）+ `constitution/project-state.md` | Stage Gate 的交付物落地；整合報告留存 |
| **5. Verification** | `.claude/agents/supervisor.md` + `.claude/scripts/verify_build.sh`（7 項硬檢核）+ `CLAUDE.md` 的 Definition of Done | **HITL Gate / Stage Gate 5**；整合報告範本（§1）|
| **6. Constraints** | `constitution/ai-member-boundaries.md`（每角色 CAN/CANNOT + Context Isolation Rules）| 角色卡的「限制」欄；Reviewer / Human Gate 設計 |

> 教學金句：**六層不是抽象理論——它們是這個資料夾裡六組你可以「打開來看」的真實檔案。**
> Teaching line: **the six layers aren't abstract theory — they are six sets of files in this folder you can literally open and read.**

---

## 4. 建議閱讀順序（給學員）/ Suggested Reading Order

1. **`README.md`** — 30 秒看懂團隊、迴圈、六層總表。
2. **`CLAUDE.md`** — 這是「憲法」。讀 The Fixed Loop / Constraints / Definition of Done 三節。
3. **`constitution/ai-member-boundaries.md`** — 看 Constraints 層怎麼用 CAN/CANNOT 表落地。
4. **`.claude/agents/cto.md` + `supervisor.md`** — 看一個「不寫內容、只出題」的 Agent 和一個「只把關、不修內容」的 Agent 怎麼被定義（Tools 層 + Verification 層）。
5. **`.claude/scripts/verify_build.sh`** — 看 Verification 層怎麼被寫成一支會 PASS/FAIL 的腳本（7 項檢核）。
6. **`working-notes/` 範例檔** — 看 Agent 之間怎麼用檔案交棒（Context 層的具體載體）。

---

## 5. 課堂活動 / Classroom Exercises（對應 L5 Gate 5）

> 對接 [`L5_CLAWTEAM_COURSE_PLAN.md`](../L5_CLAWTEAM_COURSE_PLAN.md) §7 課後作業與 §10 Gate 5。

| # | 活動 / Exercise | 練到哪一層 / Layer | 產出 / Output |
| --- | --- | --- | --- |
| A | **「找出漂移」**：比對 `README.md`、`CLAUDE.md`、`constitution/skill-stack.md` 三處對 Designer / Librarian 用哪個模型的描述——它們**不一致**。請學員指出，並說明這正是 **Verification 層**要抓的「規格漂移」。 | Verification | 1 頁差異清單 + 修正建議 |
| B | **改寫成自己的 Team**：把「AI 新聞頻道」換成學員自己公司的場景（如「每週競品情報」），重寫 `CLAUDE.md` 的 Team 表 + Fixed Loop + Definition of Done。 | Loop / Constraints | 1 份自製 `CLAUDE.md` |
| C | **補一個 Agent**：替團隊新增一個角色（如「法遵 Agent」），寫出它的 `.claude/agents/xxx.md`（含 `tools:` 與 CAN/CANNOT）。 | Tools / Constraints | 1 份 agent 定義檔 |
| D | **設計一個 Human Gate**：在哪一步該插入人工核准？寫出觸發條件、reviewer、SLA、拒絕後回到哪一步。 | Verification | 1 份 Human Gate 設計 |
| E | **寫驗證腳本**：把活動 B 的 Definition of Done 翻成一支 `verify_build.sh` 風格的檢核清單（可只寫虛擬碼）。 | Verification / Persistence | 1 份檢核腳本草稿 |

> 活動 A 是刻意保留原專案的不一致當教材——**真實專案就是會漂移，能抓出來才是 L5 能力。**（請勿直接修原檔，把差異寫在自己的作業裡。）
> Exercise A deliberately uses the original project's inconsistency as material — **real projects drift; catching it is the L5 skill.** (Don't edit the originals; record the diff in your own submission.)

---

## 6. 為什麼這是好的 L5 教材 / Why this is a strong L5 teaching artifact

- **可讀**：不是 slides，是一個真的能 `git clone` 打開的專案——學員看的是成品，不是示意圖。
- **可跑**：`.claude/scripts/` 有真的 publish / verify 腳本，`run_daily.sh` 串起整條流程。
- **異質模型**：CTO/Developer/Supervisor 用 Claude、Researcher/Designer 用 Gemini——示範「先設計系統、再挑模型」，且**同一個 Team 可以混用不同廠商的模型**。
- **治理完整**：有憲法、有 CAN/CANNOT、有 Definition of Done、有 Supervisor 把關——L5 的重點從來不是「更多 Agent」，而是「**管得住的更多 Agent**」。

---

## 7. 交叉連結 / Cross-links

- **L4→L5 教學弧（Hermes Agent 視角 + 情境故事）**：[`TIGERAI_HERMES_TO_TEAM_TEACHING.md`](TIGERAI_HERMES_TO_TEAM_TEACHING.md)
- 概念透鏡：[`90_References/HARNESS_ENGINEERING_REFERENCE.md`](../../90_References/HARNESS_ENGINEERING_REFERENCE.md)
- 平台課程：[`L5_CLAWTEAM_COURSE_PLAN.md`](../L5_CLAWTEAM_COURSE_PLAN.md)（§4.5 L5 三件套）
- 平台引用：[`90_References/CLAWTEAM_REFERENCE.md`](../../90_References/CLAWTEAM_REFERENCE.md)
- 兩軸成熟度模型：[`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0

---

**版本 / Version：** v0.1（2026-05-22）
**作者 / Author：** Morris Lu（盧業興）· Tiger AI 虎智科技
**授權 / License：** 隨本 toolkit（程式 Apache 2.0 / 文件 CC BY 4.0）
