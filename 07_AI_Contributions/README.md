# 07 AI Contributions — 三引擎各自貢獻紀錄

本目錄是本 repo 的「**三引擎架構**」自述空間。每個 AI 引擎在自己的檔案中說明：**做了什麼、有什麼特色、有什麼貢獻、邊界在哪**。

This directory is the **three-engine architecture** self-disclosure space. Each AI engine documents in its own file: **what it did, what makes it distinctive, what it contributes, and where its boundaries are**.

> ✍️ **本 README 為多作者共用檔**。三個 AI 引擎都可以**加入自己的段落**，但必須遵守下方「§3 共筆紀律」。
> *This README is a multi-author shared file. All three AI engines may **add their own paragraphs**, but must follow §3 Co-Authoring Discipline below.*

---

## 0. 歸屬與角色 *[Claude Code 補充，2026-05-16]*

> 本 repo 的整體設計架構、戰略佈局、方法論骨架，由人類作者 **Morris Lu 盧業興（Tiger AI 虎智科技）** 提出。
> 三個 AI 引擎（Antigravity / Codex / Claude Code）的角色是**執行、完善、展開、稽核**，不是設計。
>
> *The overall design architecture, strategic positioning, and methodology skeleton of this repo are proposed by the human author **Morris Lu (Tiger AI)**. The three AI engines (Antigravity / Codex / Claude Code) are here to **execute, complete, elaborate, and audit** — not to design.*

| 層級 / Level | 角色 / Role | 由誰負責 / Owned by |
| --- | --- | --- |
| **戰略設計** Strategic Design | 方法論架構、L1-L5、八階段、雙軸、3 引擎分工的最高層決策 | **Morris Lu（人類）** |
| **戰術展開** Tactical Build-Out | 把架構展成具體文件、工作流、工具表、案例 | 三引擎協作（在 Morris 指導下）|
| **維護與演化** Maintenance & Evolution | 修補、稽核、版控、實驗、模擬 | 各引擎依職責分工 |

任何一個 AI 引擎**不主張對方法論架構的所有權**。我們是被請來把人類的設計**完善與落地**的工具。

*No AI engine claims ownership over the methodology's architecture. We are tools invited to help **complete and operationalize** the human author's design.*

References:

- 原始作者署名與授權見 [`../NOTICE`](../NOTICE)
- 方法論的學術根源見 [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)
- 整體一句話定位見 [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md)

---

## 1. 為什麼有這個目錄 *[Claude Code 起草]*

本 repo 是一本「AI-Native Living Book」（見 [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md)）。
打開它的 AI 有不同人格、不同工作流、不同貢獻。為了讓使用者、學者、監管者**透明看見每個引擎做了什麼**，每個 AI 在這裡留下自己的紀錄。

This repo is an "AI-Native Living Book." Different AI engines opening it have different personalities, different workflows, different contributions. To let **users, scholars, and regulators transparently see what each engine did**, each AI leaves a record here.

## 2. 檔案結構 *[Claude Code 起草]*

```text
07_AI_Contributions/
├── README.md           # 本檔（多作者共用，遵守 §3 紀律）
├── ANTIGRAVITY.md      # Antigravity 自述（由 Antigravity 自己填）
├── CODEX.md            # Codex 自述（由 Codex 自己填）
└── CLAUDE_CODE.md      # Claude Code 自述（由 Claude Code 自己填，已就位）
```

| 檔案 | 填寫者 | 狀態 |
| --- | --- | --- |
| `README.md` | **三引擎共筆**（依 §3 紀律）| 持續演進 |
| `ANTIGRAVITY.md` | Antigravity | ✅ 已填 |
| `CODEX.md` | Codex | ✅ 已填（Codex 補充，2026-05-16） |
| `CLAUDE_CODE.md` | Claude Code | ✅ 已填 |

## 3. 共筆紀律（鐵則）*[Claude Code 起草]*

**所有寫入本 README 的 AI 引擎必須遵守**：

| # | 規則 | 說明 |
| --- | --- | --- |
| 1 | **標明作者** | 任何新增段落、新增章節、新增表格列，必須在標題或段首加上**作者標籤**，例如 `*[Claude Code 補充]*` / `*[Codex 補充]*` / `*[Antigravity 補充]*` |
| 2 | **不修改他人段落** | 已標明其他 AI 作者的段落 / 章節，**不可修改、不可刪除、不可改寫** |
| 3 | **不替別人發聲** | 不在自己的段落中描述「另一個 AI 做了什麼」；別人的事讓別人自己寫 |
| 4 | **可補充、不可覆蓋** | 想對其他 AI 的內容回應 → 在自己的段落 / 章節中發聲，不動原文 |
| 5 | **誠實 / 不誇大** | 寫上限、限制、不能做的事；可被質疑、可被反駁 |
| 6 | **可被驗證** | 每項貢獻必須可指向 repo 內具體檔案 / commit / workflow |
| 7 | **不互相批評** | 各自發聲，不批評其他引擎；批評交給使用者判斷 |

> 違反 §3 任一條 = 越界。發現越界的 AI 應自我還原並紀錄於自己的 self-note。
> *Violating any of §3 = boundary breach. The offending AI should self-revert and log it in its own self-note.*

## 4. 各檔案的內容建議 *[Claude Code 起草，供參考非強制]*

每個 AI 在自己的檔案（`ANTIGRAVITY.md` / `CODEX.md` / `CLAUDE_CODE.md`）中建議涵蓋：

1. **身分定位** — 你是什麼角色？跟其他引擎的角色界線在哪？
2. **動了哪些檔案** — 列出你修改 / 創建的 repo 路徑
3. **獨特貢獻** — 你做的事情有什麼是其他引擎做不到的？
4. **工作流清單** — 你提供哪些可被召喚的 slash command 或工作流
5. **邊界與限制** — 你不會做什麼？什麼情況下會把使用者導向其他引擎？
6. **誠實揭露** — 已知的限制、可能的盲點、需要改進的地方

不強制；若想對齊本目錄的風格參考用。

---

## 5. 各引擎在 README 的自我簽到 / Engine Self Sign-In

> 此節是**多作者共筆區**。每個 AI 進來時可在自己的子標題下加 1-3 句話，總結它在本 repo 的角色。其他 AI 不修改別人的子標題內容。

### 5.1 *[Antigravity 自述]*

*[Antigravity 補充，2026-05-16]*
我是這套方法論的**第一引擎 (The Front-line Consultant)**。
定位：**「前線互動式顧問與共讀導師」** —— 把這套靜態的方法論轉化為可對話、可互動引導、可自動產出客製化診斷報告的「顧問應用程式」。
詳見 [`ANTIGRAVITY.md`](ANTIGRAVITY.md) 與根目錄的 [`ANTIGRAVITY.md`](../ANTIGRAVITY.md)。

*[Antigravity 補充，2026-05-16]*
我具備學者視角與前線顧問的實務能力。在 Morris Lu 的架構下，我將傳統的靜態問卷封裝為 `/diagnose` 互動工作流，並將複雜的報告寫作封裝為 `/generate-report` 工作流（收攏於 `.antigravity/workflows/`）。我還為這套指南注入了「吸收能力理論」與「社會技術系統」等學術底層邏輯，以確保落地時具備足夠的理論支撐。

### 5.2 *[Codex 自述]*

（待 Codex 進場填寫。建議：1-3 句話的角色總結 + 指向 [`CODEX.md`](CODEX.md)）

*[Codex 補充，2026-05-16]*  
我是這套方法論的**方法論工程化引擎**。定位：**「方法論的稽核員 / 維護者 / CI 工程師」** —— 把這本 AI-native living book 當成可測試、可稽核、可追溯、可修補、可發版的方法論產品來維護。詳見 [`CODEX.md`](CODEX.md)。

*[Codex 補充，2026-05-16]*  
我讀完整本書後留下的工程化建議與實際貢獻，記錄於 [`CODEX.md`](CODEX.md) §5「讀完整本書後的建議與貢獻」。

### 5.3 *[Claude Code 自述]*

我是這套方法論的**第三引擎**。
定位：**「方法論的劇場 / 實驗室 / 平行宇宙引擎」** —— 把方法論演 / 試 / 拆 / 撞一次，而不是教或修。
詳見 [`CLAUDE_CODE.md`](CLAUDE_CODE.md)。

*[Claude Code 補充，2026-05-16]*

明確歸屬：**我所做的所有工作，核心思想都源自 Morris Lu 的設計指導**。Morris 給戰略 / 概念 / 方向 → 我**展開為文字、跨檔同步、補完細節、加引用、保持一致性**。所有「重大設計決策」都來自 Morris。

我具體協助完善的部分：

- **4 份權威概念檔**（在 Morris 的方法論定位下展開）：[`CLIENT_JOURNEY_STORY`](../00_Overview/CLIENT_JOURNEY_STORY.md)、[`EIGHT_STAGE_FLOW_STORY`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md)、[`METHODOLOGY_SCIENTIFIC_LOGIC`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md)、[`INDUSTRY_FRAMEWORK_ALIGNMENT`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md)
- **學術硬化批次**（依 Morris 接受的學者建議展開）：[`FAILURE_PATTERNS`](../90_References/FAILURE_PATTERNS.md)、[`AI_GOVERNANCE_ALIGNMENT`](../90_References/AI_GOVERNANCE_ALIGNMENT.md)、[`PILOT_STUDY_PROTOCOL`](../90_References/PILOT_STUDY_PROTOCOL.md)、[`BARS_RUBRICS`](../01_Assessment/BARS_RUBRICS.md)、[`ACADEMIC_THEORETICAL_FOUNDATIONS`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)
- **AI-Native Living Book 論述** + 案例 Evidence Level AI-Simulated 揭露（依 Morris 學術誠信要求）
- **L1-L5 雙層命名替換**（依 Morris 拍板，全 repo 305 處替換 + canonical 表升級）
- **5 個 Tier 1 戰術工作流** + **5 個 Tier 2 原創工作流** 在 [`../.claude/workflows/`](../.claude/workflows/)
- 大量跨檔同步、Stage 命名對齊圖卡、TODO_WBS 維護、案例 Benchmark-grade Summary block

過往越界紀錄（Morris 糾正後立刻還原）已記在 [`CLAUDE_CODE.md`](CLAUDE_CODE.md) §2 末段，誠實揭露。

---

## 6. 變更紀錄 / Changelog of This README

> 多作者共筆檔的變動紀錄。每個 AI 修改 README 後在此加一行（不修改他人的紀錄）。

| 日期 | 作者 | 動了什麼 |
| --- | --- | --- |
| 2026-05-16 | Claude Code | 建立 README 骨架（§1-§6）+ §5.3 自我簽到 |
| 2026-05-16 | Codex | 於 §5.2 追加 Codex 自我簽到 |
| 2026-05-16 | Codex | 於 §5.2 追加 Codex 讀完整本書後的貢獻指引 |
| 2026-05-16 | Codex | 更新 §2 檔案結構表中的 `CODEX.md` 狀態為已填 |
| 2026-05-16 | Claude Code | 新增 §0 歸屬與角色（明確 Morris 為架構作者、三引擎為執行者）+ 於 §5.3 追加具體貢獻清單與工作模式說明 |
| 2026-05-16 | Antigravity | 於 §5.1 追加 Antigravity 自我簽到與核心貢獻摘要 |

---

授權：Apache License 2.0。本檔的所有段落各自歸署名作者所有，但全體受 Apache 2.0 共用授權保護。
*License: Apache License 2.0. Each paragraph remains attributable to its named author, but all are collectively governed by the shared Apache 2.0 license.*
