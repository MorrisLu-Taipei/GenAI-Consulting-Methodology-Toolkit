# Harness Engineering 引用與對應說明 / Harness Engineering Citation & Mapping Notice

> 🌐 語言：繁體中文 ｜ [English](HARNESS_ENGINEERING_REFERENCE_EN.md) ｜ Deutsch（待補）｜ Français（待補）｜ Español（待補）｜ 日本語（待補）｜ 한국어（待補）

本方法論的 **L5（Agent Team）** 在「平台選型」之上，補一層「**為什麼 Agent Team 能可靠交付**」的概念框架——**Harness Engineering（馬具工程 / 框架工程）**。本檔記錄這個概念的來源、六層模型，以及它如何對應到本方法論既有的 L5、HITL Gate、Stage Gate 與八階段流程；並指向 toolkit 內的完整實作案例 [`ai-news-channel`](../02_Course_Design/ai-news-channel/)。

On top of "platform selection," the **L5 (Agent Team)** layer of this methodology adds a conceptual frame for *why* an Agent Team can reliably deliver — **Harness Engineering**. This document records the concept's origin, its six-layer model, how it maps onto our existing L5 / HITL Gates / Stage Gates / eight-stage process, and points to the complete worked case [`ai-news-channel`](../02_Course_Design/ai-news-channel/) inside this toolkit.

---

## 1. 核心命題 / The Core Thesis

> 「決定 AI 能不能可靠交付的，不是模型本身，而是**包在模型外面的那套系統**。」
> "What determines whether AI can reliably deliver results is not the model itself, but **the system wrapped around the model**." — Harness Engineering

「Harness」原指馬具——讓一匹力量強大但難以駕馭的馬，能穩定地拉動車輛。套用到 AI：模型是馬，**harness（框架）是讓它穩定產出的那組約束、工具、迴圈與檢核**。Harness Engineering 主張一個反直覺的順序：

A "harness" is the tack that lets a powerful but unruly horse pull a cart steadily. Applied to AI: the model is the horse; the **harness is the set of constraints, tools, loops, and checks that make its output stable**. Harness Engineering asserts a counter-intuitive ordering:

> **先設計系統，再挑模型。**（Design the system first, then pick the models.）

這正是本方法論一貫的立場：L1→L5 的躍升，靠的從來不是「換更大的模型」，而是「**把模型放進愈來愈嚴謹的框架**」。Harness Engineering 給了這個直覺一個可教、可驗收的名字與結構。

This is exactly this methodology's standing position: the L1→L5 jump has never come from "a bigger model," but from "**placing the model inside an increasingly rigorous frame**." Harness Engineering gives that intuition a teachable, assessable name and structure.

---

## 2. 六層 Harness 模型 / The Six Harness Layers

源出 [`ai-news-channel/README.md`](../02_Course_Design/ai-news-channel/README.md) §"The 6 Harness Layers"，本方法論將其定為 **L5 的核心概念骨架**：

| # | 層 / Layer | 一句話定義 / One-line definition | 在 [`ai-news-channel`] 的實作 / Implementation in the case |
| --- | --- | --- | --- |
| 1 | **Loop（迴圈）** | 固定的工作順序，永不跳步 / A fixed work order, never skipped | `CLAUDE.md` 的 Fixed Loop：PM→CTO→Researcher→Developer→Designer→Supervisor→PM Approve→Publish |
| 2 | **Tools（工具）** | 每個 Agent 只拿到該拿的權限 / Each agent gets only the tool scope it needs | `.claude/agents/*.md` frontmatter 的 `tools:`（如 CTO 只有 `Read, Write, Glob`；Supervisor 有 `Bash`）|
| 3 | **Context（脈絡）** | 所有 Agent 先讀同一份「憲法」 / All agents read the same "constitution" first | 每個 agent「On Every Invocation」第一步都讀 `CLAUDE.md` + `constitution/` |
| 4 | **Persistence（持久化）** | 產出與決策永久落地，不丟失 / Outputs & decisions are durably stored, never lost | `knowledge-base/`（deliverables / decisions / topic-archive）+ `project-state.md` |
| 5 | **Verification（驗證）** | 上線前一定過一道機器 + 人的檢核 / A machine + human check before anything ships | `Supervisor` agent + `verify_build.sh`（7 項硬檢核）+ Definition of Done |
| 6 | **Constraints（約束）** | 每個角色的能 / 不能，白紙黑字 | `constitution/ai-member-boundaries.md` 的 CAN / CANNOT 表 + Context Isolation Rules |

> 記憶法：**Loop 決定「順序」、Tools 決定「能碰什麼」、Context 決定「共識從哪來」、Persistence 決定「記憶不丟」、Verification 決定「誰把關」、Constraints 決定「不能越界」。**
> Mnemonic: Loop = *sequence*, Tools = *reach*, Context = *shared ground*, Persistence = *memory*, Verification = *gatekeeping*, Constraints = *boundaries*.

---

## 3. 與本方法論既有構件的對應 / Mapping onto Existing Methodology Constructs

Harness Engineering 不是外來的新東西，而是**把本方法論散落各處的紀律，收斂成六個可命名的層**。對應如下：

| Harness 層 | 本方法論既有構件 / Existing construct | 出處 / Source |
| --- | --- | --- |
| **Loop** | 八階段顧問流程的 Stage 順序；L5 課的 Fixed Loop / 任務依賴鏈（`--blocked-by`）| `00_Overview` 八階段；`L5_CLAWTEAM_COURSE_PLAN` §6.4 |
| **Tools** | L1-L5 的「能力 = 模型 + 該層被授權的工具」兩軸觀 | `AI_TRANSFORMATION_STORY_AND_STRUCTURE` §3.0 兩軸模型 |
| **Context** | 「AI 看得懂的活書」/ 長 context 共讀；客戶情境→理論落點 | `CLAUDE.md`（Claude Code 角色）；`ACADEMIC_THEORETICAL_FOUNDATIONS` |
| **Persistence** | 顧問交付物落地、版本化、可引用（Git→GitHub→DOI 出版閉環）| 研究論文 §8.2.2 publishing cycle |
| **Verification** | **HITL Gates** + **Stage Gates**（每階段的人工把關）| 全方法論的 Gate 設計；Bible AI 治理的 HITL Gate |
| **Constraints** | 角色卡的「限制」欄、Reviewer/Human Gate、紅線設計 | `L5_CLAWTEAM_COURSE_PLAN` §6.2 角色卡；治理紅線 |

**結論：Harness Engineering 是 L5 的「概念透鏡」，HITL/Stage Gate 是它的 Verification + Constraints 層在顧問場景的具體化。** 兩者不衝突，是同一套紀律的兩種語言。

**Takeaway: Harness Engineering is the *conceptual lens* for L5; HITL/Stage Gates are the concrete instantiation of its Verification + Constraints layers in a consulting setting.** They are two vocabularies for one discipline.

---

## 4. L5 三件套：平台 + 透鏡 + 實例 / The L5 Triad: Platform + Lens + Worked Case

L5 教學現在由三個互補件組成，缺一不可：

The L5 teaching now rests on three complementary pieces:

| 角色 / Role | 是什麼 / What it is | 教什麼 / What it teaches | 檔案 / File |
| --- | --- | --- | --- |
| **平台 / Platform** | ClawTeam（CLI 編排框架）| 機制：spawn / task / inbox / board / gate 怎麼動 | [`L5_CLAWTEAM_COURSE_PLAN.md`](../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md)、[`CLAWTEAM_REFERENCE.md`](CLAWTEAM_REFERENCE.md) |
| **透鏡 / Lens** | Harness Engineering（六層模型）| 概念：為什麼 Agent Team 能可靠交付 | 本檔 / This file |
| **實例 / Worked case** | `ai-news-channel`（可讀、可跑的完整專案）| 示範：六層 + 治理長什麼樣、怎麼開一個 | [`ai-news-channel/TIGERAI_L5_CASE_NOTES.md`](../02_Course_Design/ai-news-channel/TIGERAI_L5_CASE_NOTES.md) |

> 教學動線建議：先用 **Harness 六層（透鏡）** 給學員心智模型 → 打開 **`ai-news-channel`（實例）** 逐層對照「原來六層長這樣」→ 再用 **ClawTeam（平台）** 動手把自己的 Team 跑起來。
> Suggested flow: give the mental model with the **six-layer lens** → open the **worked case** to see each layer concretely → then go hands-on with the **platform** to run your own team.

---

## 5. 來源文獻 / Source References

`ai-news-channel` 的 Harness Engineering 框架引用下列公開來源（皆為 2025-2026 業界一手討論）：

The Harness Engineering frame in `ai-news-channel` cites the following public sources (all 2025-2026 first-hand industry discussions):

1. Mitchell Hashimoto, *"My AI Adoption Journey"* (2026/02)
2. OpenAI, *"Harness Engineering: Leveraging Codex in an Agent-First World"* (2026/02)
3. Birgitta Böckeler / Martin Fowler, *"Harness Engineering"* @ martinfowler.com (2026/02)
4. Anthropic, *"Effective Harnesses for Long-Running Agents"* (2025/11)
5. Aakash Gupta, *"2025 Was Agents. 2026 Is Agent Harnesses."* @ Medium

> 引用紀律：本方法論教材在引述上述六層與術語時，註明 Harness Engineering 為業界共識框架（非單一作者專利），並以 `ai-news-channel` 作為我方原創的「在地化完整實例」。
> Citation discipline: when our materials cite the six layers and terminology, we note Harness Engineering as an industry-consensus frame (not any single author's proprietary IP), with `ai-news-channel` as our own original "localized worked example."

---

## 6. 與《AI 產業人才認定指引》的對接 / Alignment with Taiwan's AI Talent Guide

《AI 產業人才認定指引（115 年 5 月）》將 **Harness Engineering** 列為新興能力領域之一。本方法論的對接點：

The *AI Industry Talent Accreditation Guidelines (May 2026)* list **Harness Engineering** as one of the emerging capability domains. Our alignment points:

- L5 課程的 **Harness 六層 + `ai-news-channel` 實例**，可作為「Harness Engineering」職能的**可驗收教學單元 + hands-on 作業**。
- 對應人才能力描述時，建議以本方法論的 **Bloom 格式 LO**（[動詞]+[內容]+[情境]）撰寫，使能力可量測（見 [`ONLINE_COURSE_DESIGN_METHODOLOGY.md`](../02_Course_Design/ONLINE_COURSE_DESIGN_METHODOLOGY.md) §4）。

> 待辦：人才指引 PDF 之逐條能力對照，列為 `TODO_WBS` 延伸項（與 AI 人才指引整合同批處理）。
> TODO: a clause-by-clause capability mapping against the guide PDF is logged in `TODO_WBS` as a deferred item (batched with the broader Talent-Guide integration).

---

## 7. 授權與原創聲明 / License & Authorship Notice

| 項目 / Field | 內容 / Value |
| --- | --- |
| **`ai-news-channel` 作者 / Author** | Morris Lu（盧業興）· Tiger AI 虎智科技 — **本 toolkit 內的原創作品** / original work within this toolkit |
| **與上游關係 / Upstream** | 無外部 fork、無第三方 LICENSE 檔；為本方法論自製之 L5 教學案例 / no external fork, no third-party LICENSE file — a self-authored L5 teaching case |
| **授權 / License** | 隨本 toolkit（程式碼 Apache 2.0 / 文件 CC BY 4.0）/ follows the toolkit (code Apache 2.0 / docs CC BY 4.0) |
| **「Harness Engineering」術語 / Term** | 業界共識框架，本檔依學術引用慣例註明來源（§5），非主張術語所有權 / industry-consensus frame, cited per academic convention (§5), no claim of ownership over the term |

> 與 ClawTeam（HKUDS, MIT, 外部上游）不同：`ai-news-channel` **不需要** NOTICE / 上游著作權保留處理，因為它是本 toolkit 內自製的原創案例。
> Unlike ClawTeam (HKUDS, MIT, external upstream): `ai-news-channel` does **not** require NOTICE / upstream-copyright handling, because it is a self-authored original case inside this toolkit.

---

**版本 / Version：** v0.1（2026-05-22）
**作者 / Author：** Morris Lu（盧業興）· Tiger AI 虎智科技
**相關檔 / Related：** [`ai-news-channel/TIGERAI_L5_CASE_NOTES.md`](../02_Course_Design/ai-news-channel/TIGERAI_L5_CASE_NOTES.md)、[`L5_CLAWTEAM_COURSE_PLAN.md`](../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md)、[`CLAWTEAM_REFERENCE.md`](CLAWTEAM_REFERENCE.md)
