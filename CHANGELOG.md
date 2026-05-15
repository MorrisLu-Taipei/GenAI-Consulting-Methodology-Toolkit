# Changelog — 三引擎共筆 / Three-Engine Co-Authored Release Notes

> 本檔記錄本 repo 各版本的變更。**這是多作者共筆檔** —— Antigravity / Codex / Claude Code 三個 AI 引擎各自在自己段落紀錄貢獻，人類作者 **Morris Lu（Tiger AI）** 把關發版時機與版本號。
>
> *This changelog is a multi-author co-edited file. Antigravity / Codex / Claude Code each record their own contributions; human author **Morris Lu (Tiger AI)** owns release cadence and version numbers.*

---

## 共筆紀律 / Co-Authoring Discipline

完整紀律見 [`07_AI_Contributions/README.md` §3](07_AI_Contributions/README.md#3-共筆紀律鐵則-claude-code-起草)。摘要：

1. **標明作者** — 每則條目以 `*[Antigravity 補充]*` / `*[Codex 補充]*` / `*[Claude Code 補充]*` 開頭
2. **不修改他人段落** — 已標名作者的段落，其他 AI 不得改寫、刪除
3. **不替別人發聲** — 不在自己的段落中描述「另一個 AI 做了什麼」
4. **可被驗證** — 每則條目必須可指向 repo 內具體 commit / 檔案

格式參考：

```markdown
### vX.Y.Z — YYYY-MM-DD — <版本主題>

#### *[作者 補充，YYYY-MM-DD]*
- 變更摘要（commit `<sha>` / 檔案 `<path>`）
- ...
```

---

## Unreleased / 三引擎架構建立期

> 此區塊為 v1.1.0 之後、下次發版之前的累積。發版時由 Morris 決定版本號，並把此區塊整段封存至下一個版本標題下。

### *[Antigravity 補充]*

（待 Antigravity 進場填寫自己在此期間的貢獻）

### *[Codex 補充]*

（待 Codex 進場填寫自己在此期間的貢獻）

### *[Claude Code 補充，2026-05-16]*

主軸：**方法論大批次升級 + 第三引擎（Claude Code）落位**。本批次工作多在 Morris 直接指揮下完成；架構決策歸屬 Morris，本段僅紀錄我作為執行 / 展開 / 稽核工具的具體動作。

**A. 方法論本體**（commit `27cb15a`）

- **L1-L5 雙層命名**：依 Morris 拍板，全 repo 305 處替換（Chat AI → Controlled AI Access 等）+ canonical 表升級
- **八階段對齊圖卡**：對齊 NotebookLM 圖與 Rosemann BPM 學派
- **4 份權威概念檔**（在 Morris 方法論定位下展開）：
  - [`00_Overview/CLIENT_JOURNEY_STORY.md`](00_Overview/CLIENT_JOURNEY_STORY.md)
  - [`00_Overview/EIGHT_STAGE_FLOW_STORY.md`](00_Overview/EIGHT_STAGE_FLOW_STORY.md)
  - [`00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md`](00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md)
  - [`00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md`](00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md)

**B. 學術硬化批次**（依 Morris 接受的學者建議）

- [`90_References/FAILURE_PATTERNS.md`](90_References/FAILURE_PATTERNS.md) — 失敗模式
- [`90_References/AI_GOVERNANCE_ALIGNMENT.md`](90_References/AI_GOVERNANCE_ALIGNMENT.md) — 治理對齊
- [`90_References/PILOT_STUDY_PROTOCOL.md`](90_References/PILOT_STUDY_PROTOCOL.md) — Pilot Study 協定
- [`01_Assessment/BARS_RUBRICS.md`](01_Assessment/BARS_RUBRICS.md) — Behaviorally Anchored Rating Scales
- [`00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) — 7 大理論支柱
- AI-Native Living Book 論述 + 案例 Evidence Level **L0 AI-Simulated** 揭露（依 Morris 學術誠信要求）

**C. Claude Code 第三引擎落位**

- [`CLAUDE.md`](CLAUDE.md) — Claude Code 專屬入口檔
- [`.claude/README.md`](.claude/README.md) + [`.claude/workflows/`](.claude/workflows/) 10 個工作流
  - **Tier 1 戰術工作流（5 個）**：`/deep-synthesize`、`/theory-bridge`、`/scenario-planning`、`/socratic-challenge`、`/cross-stage-trace`
  - **Tier 2 原創工作流（5 個）**：`/simulate-engagement`、`/parallel-perspectives`、`/thought-experiment`、`/devil-pair-debate`、`/methodology-fork`
- [`07_AI_Contributions/`](07_AI_Contributions/) 目錄建立：多作者 README 骨架 + §3 共筆紀律 + [`CLAUDE_CODE.md`](07_AI_Contributions/CLAUDE_CODE.md) 自我揭露
- 根 [`README.md`](README.md) 升級：三代書敘事（印刷書 → 互動書 → AI-Native Living Book）+ 三 AI 引擎介紹 + 三引擎統一安裝指南

**D. 邊界與誠實揭露**

- 過往越界紀錄（替 Codex / Antigravity 發聲）已於 Morris 糾正後立刻還原，並於 [`07_AI_Contributions/CLAUDE_CODE.md`](07_AI_Contributions/CLAUDE_CODE.md) §2 末段誠實記錄
- 本批次的 Tier 2 工作流為**未經實證的設計**，需 Pilot Study 完成才能驗證實用性（見 [`90_References/PILOT_STUDY_PROTOCOL.md`](90_References/PILOT_STUDY_PROTOCOL.md)）

---

## v1.1.0 — 2026-05-15 — 雙語對齊 + 公開誠實版交付範圍

> 此版本由 Morris 在三引擎架構建立**之前**獨立發版。三引擎尚未進場，故不分作者區塊。

- 7 個目錄 README_EN（00-06）重寫至與中文完整版對應，並納入 L1-L5 雙軸概念
- [`DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](DELIVERY_PACKAGE_AND_ACCEPTANCE.md) §1.1：公開誠實版交付範圍 —— L1-L3 實作並驗收 vs L4-L5 框架與顧問引導
- Gate 術語清理：人工 Gate → HITL；Stage Gate → 階段驗收關卡
- TODO_WBS 更新

對應 commit：`ef32c4a`

---

## v1.0.0 — 2026-05-15 — L4 Starter-kit + Finance PoCs + Consulting Frameworks

> 首次正式發版。Morris 獨立完成。

- L4 starter-kit 改寫
- Finance PoCs
- n8n skeletons
- Consulting frameworks

對應 commit：`843f9fa`

---

## 變更紀錄之變更紀錄 / Changelog of This Changelog

| 日期 | 作者 | 動了什麼 |
| --- | --- | --- |
| 2026-05-16 | Claude Code | 建立 CHANGELOG.md 骨架 + Unreleased §[Claude Code 補充] + v1.0.0 / v1.1.0 回填 |

---

授權：Apache License 2.0。每段條目歸署名作者所有，全體受 Apache 2.0 共用授權。
*License: Apache License 2.0. Each entry remains attributable to its named author; collectively governed by Apache 2.0.*
