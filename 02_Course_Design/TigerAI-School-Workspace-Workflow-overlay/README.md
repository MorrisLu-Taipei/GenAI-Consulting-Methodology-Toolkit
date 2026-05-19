# TigerAI School Workspace Workflow — Overlay 說明

> 🌐 繁體中文（本檔內含 EN section）/ This file is bilingual; English sections inline.

## 0. 這個資料夾是什麼 / What this folder is

本資料夾是 **Tiger AI 對 [mihozip/google-workspace-admin-project-workflow](https://github.com/mihozip/google-workspace-admin-project-workflow) 的方法論延伸（overlay）**。它**不複製**原 repo 任何檔案，只**新增** Tiger AI L1-L3 方法論層 + 校園情境的 Stage Gate / HITL Gate 設計 + 獨立 release 紀錄。

This folder is **Tiger AI's methodology overlay on top of [mihozip/google-workspace-admin-project-workflow](https://github.com/mihozip/google-workspace-admin-project-workflow)**. It **does not duplicate** any of the original repo's files. It **only adds** the Tiger AI L1-L3 methodology layer + school-context Stage Gate / HITL Gate design + an independent release log.

### 為什麼用 overlay 不直接 fork 然後改 / Why overlay not in-place fork

| 原因 / Reason | 說明 / Explanation |
|---|---|
| **法律乾淨 / Legal clean** | 原 repo 為 **MIT**；本 toolkit 為 **Apache 2.0**；兩者相容但混合會讓衍生作品授權變複雜。Overlay 模式讓兩個專案的授權邊界永遠清楚。/ Original repo is MIT; this toolkit is Apache 2.0. Compatible but mixing makes derivative-work licensing complex. Overlay keeps both projects' license boundaries clean. |
| **可同步上游 / Upstream sync** | 原作者未來更新 → 使用者直接 `git pull upstream main` 拿到，overlay 不會擋路。/ When upstream updates, users `git pull upstream main` cleanly without overlay blocking. |
| **獨立 release 流程 / Independent release flow** | Tiger AI overlay 自己有 CHANGELOG + RELEASE 流程，不污染原作者的版本史。/ Tiger AI overlay has its own CHANGELOG + RELEASE, doesn't pollute original's version history. |
| **可分發給多客戶 / Distributable per client** | Overlay 可以被多個學校 / 縣市 fork 後客製，原作者貢獻持續被尊重。/ Overlay can be forked per school / county for customization while preserving original attribution. |

---

## 1. 原作者署名（MIT 授權必須保留）/ Original Attribution (MIT-required)

| 欄位 / Field | 內容 / Value |
|---|---|
| **原專案 / Original project** | google-workspace-admin-project-workflow |
| **原作者 / Original author** | mihozip ([GitHub](https://github.com/mihozip)) |
| **原 URL / Original URL** | <https://github.com/mihozip/google-workspace-admin-project-workflow> |
| **授權 / License** | **MIT License** |
| **參考於 / Referenced on** | 2026-05-20 |

> 完整 MIT 授權條款與權利保留聲明，見同資料夾 [`NOTICE.md`](NOTICE.md)。
> Full MIT license terms and rights notice: see [`NOTICE.md`](NOTICE.md) in this folder.

---

## 2. Tiger AI overlay 增加了什麼 / What Tiger AI Overlay Adds

| 檔案 / File | 內容 / Content |
|---|---|
| [`NOTICE.md`](NOTICE.md) | 雙重署名（原作者 mihozip + Tiger AI 貢獻） / Dual attribution (mihozip + Tiger AI) |
| [`INSTRUCTIONS_FOR_FORK.md`](INSTRUCTIONS_FOR_FORK.md) | 學校 / 顧問如何把 overlay 套進自己的 fork / How schools / consultants apply overlay to their fork |
| [`TIGERAI_METHODOLOGY_LAYER.md`](TIGERAI_METHODOLOGY_LAYER.md) | Tiger AI L1-L5 方法論與本 repo 的對位關係 / Tiger AI L1-L5 mapping to this repo |
| [`TIGERAI_SCHOOL_L1_L3_GUIDE.md`](TIGERAI_SCHOOL_L1_L3_GUIDE.md) | 校園情境下 L1 / L2 / L3 的具體實作對應 / School-context L1 / L2 / L3 concrete implementations |
| [`TIGERAI_STAGE_GATES_SCHOOL.md`](TIGERAI_STAGE_GATES_SCHOOL.md) | 校長 / 教務主任 / 學年主任的 Stage Gate 驗收設計 / Stage Gate acceptance design |
| [`TIGERAI_HITL_GATES_SCHOOL.md`](TIGERAI_HITL_GATES_SCHOOL.md) | 校園工作流的 HITL Gate 範本（公文 / 學生資料 / 對外公告 / 家長通知）/ School HITL Gate patterns |
| [`CHANGELOG.md`](CHANGELOG.md) | Tiger AI overlay 獨立版本紀錄 / Tiger AI overlay's independent version log |
| [`RELEASE_v0.1.0.md`](RELEASE_v0.1.0.md) | 第一版 release notes / First release notes |

**所有 Tiger AI 新增檔案以 Apache 2.0 授權發布。** 原 repo 檔案維持 MIT。
**All Tiger AI added files are released under Apache 2.0.** Original repo files remain MIT.

---

## 3. 適用對象 / Audience

| 對象 / Audience | 該讀什麼 / Read what |
|---|---|
| **學校 IT / 教務主任** | `INSTRUCTIONS_FOR_FORK.md` → `TIGERAI_SCHOOL_L1_L3_GUIDE.md` |
| **校長 / 副校長** | `TIGERAI_STAGE_GATES_SCHOOL.md`（看驗收標準） |
| **教師（一般使用者）** | 原 repo 的 `basic-lesson/` + `advanced-lesson/` 資料夾 + 本 overlay 的 L1 段 |
| **顧問 / AI Champion** | 全部 |

---

## 4. 跟 Tiger AI Methodology Toolkit 主體的關係 / Relation to Main Toolkit

本 overlay 是 [Tiger AI Methodology Toolkit](https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit) 在「教育界 L1-L3 案例」維度的具體實作分支。讀完本 overlay，建議回主 toolkit 看：

- `02_Course_Design/ONLINE_COURSE_DESIGN_METHODOLOGY.md` 線上課程設計品質 SOP
- `00_Overview/SME_LITE_PATH.md` 中小組織（含學校）的壓縮顧問流程
- `04_Scenarios/SAMPLE_CLIENT_CASE_*.md` 其他產業 case study 對照

This overlay is a domain-specific implementation branch of [Tiger AI Methodology Toolkit](https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit) for the education sector L1-L3 use case. After this overlay, recommended further reading in the main toolkit:

- `02_Course_Design/ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md` Online course design quality SOP
- `00_Overview/SME_LITE_PATH_EN.md` Compressed consulting flow for SME / schools
- `04_Scenarios/SAMPLE_CLIENT_CASE_*.md` Cross-industry case studies

---

**版本 / Version：** Tiger AI overlay v0.1.0（2026-05-20）
**授權 / License：** Apache License 2.0（Tiger AI additions only；原 repo 維持 MIT）
**作者 / Author：** Tiger AI Morris Lu 盧業興
