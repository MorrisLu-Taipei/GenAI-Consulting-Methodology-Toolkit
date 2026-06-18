# CANONICAL TERMS & MAPS — 名詞與流程憲法(單一真實來源)

> 🌐 繁體中文(canonical)｜本檔是**全系列名詞與流程的唯一權威**。任何文件、互動頁、Skill、ebook、i18n 與本檔衝突時,**以本檔為準**,並回頭修正衝突文件。
> 建立:2026-06-18 ｜ 維護者:Morris (Yeh-Hsing) Lu

本系列「內容長得太快」造成四套流程與兩套等級混用。本檔做一次性整理,鎖死定義。

---

## 0. 系列與書的命名(唯一標準)
- **系列(只有一個)**:**AI-Native 顧問方法論系列**(AI-Native Consulting Methodology Series)。
- **書(分兩本)**:
  - **上集 = Book I:顧問思考能力系統**(Consulting Thinking Capability System)→ 顧問怎麼想?位置 `10_Thinking_Framework/`
  - **下集 = Book II:AI 轉型顧問導入方法論**(AI-Transformation Consulting Delivery Methodology)→ 顧問案怎麼跑?位置 `00_Overview/` + `01`–`06`
- **禁止寫法**:❌「Series II」❌「顧問系列 II」❌「Book II (Series II)」。系列只有一個,只有**書**分 I/II。
- **標準引用**:「Book II of the AI-Native Consulting Methodology Series」／「AI-Native 顧問方法論系列・下集」。

## Repo 定位(唯一標準)
本 repo 是**系列總庫(series monorepo)**,同時收錄上集、下集、研究、References 與系列入口。
- `10_Thinking_Framework/` = **上集 Book I**
- `00_Overview/` + `01`–`06` = **下集 Book II**
- `07_AI_Contributions` `09_Research_Paper` `90_References` 與根目錄檔 = **系列外殼/Meta**
> ❌ 不要再說「本 repo = 下集」。

---

## 1. 兩套等級(最易混淆,務必分流)

| 命名空間 | 適用 | 量的是 | 五級 |
|---|---|---|---|
| **C1–C5(Consultant Capability)** | **上集 Book I** | **人**(顧問個人能力) | C1 記錄 Recorder · C2 整理 Organizer · C3 分析 Analyst · C4 規劃 Planner · C5 顧問 Advisor |
| **L1–L5(Enterprise AI Maturity)** | **下集 Book II** | **企業**(AI 成熟度) | L1 Controlled AI Access 受控 AI 入口 · L2 Knowledge Codification 知識資產化 · L3 Workflow Automation 流程自動化 · L4 Autonomous Agent 自主代理 · L5 Multi-Agent Organization 多代理組織 |

**防混淆一句話**:**C 問「人在什麼能力階段?」;L 問「企業在什麼 AI 成熟度階段?」**

**橋接規則**:顧問需達 **C4(規劃)**,才能獨立執行下集的企業 **L1–L5 診斷**;C5 才能獨立帶整案。

> 歷史/研究文件若保留舊版,須標註:「舊版曾以 L1–L5 描述顧問能力;自 vNext 起改用 C1–C5。」
> 下集企業 L1–L5 正式定義權威來源:`01_Assessment/AI_MATURITY_SCORING_MODEL.md`(含雙層命名、證據來源)。

---

## 2. 四張不同的流程圖(不要互相混用)

這四張圖**各有用途、不是同一張**:

### 圖 A — 三段式服務流程(Service Flow,鳥瞰)
**診斷 Diagnose → 建置 Build → 交付 Deliver**。給客戶/新人 5 分鐘理解全貌用。

### 圖 B — 顧問八階段(8 Stages,方法論本體)
權威來源:`00_Overview/EIGHT_STAGE_FLOW_STORY.md`。

| # | Stage(EN) | 中文 |
|---|---|---|
| 1 | As-Is | 現況快照 |
| 2 | Reference Model | 參考模型對齊 |
| 3 | Ideal Practice | 理想實務 |
| 4 | Gap Analysis | 落差分析 |
| 5 | Problem Definition | 問題定義 |
| 6 | Phased Goals | 分階段目標 |
| 7 | To-Be Design | 目標態設計 |
| 8 | Implementation | 落地執行 |

> ❌ 互動頁舊版寫的「Assessment→Course→Report→Scenarios→Sales→Build→Delivery→Support」**不是八階段**,那是「圖 D 目錄/接案流程」。已修正。

### 圖 C — 三階段合約模型(Contract Phases,賣法/Gate)
權威來源:`00_Overview/EIGHT_STAGE_FLOW_STORY.md` §1。**Phase 的唯一 canonical 定義 = 時長 + 交付物 + Gate**(下表前四欄),這部分兩份權威文件本就一致:

| Phase | 名稱 | 時長(canonical) | 交付物(canonical) | Gate |
|---|---|---|---|---|
| **A** | 診斷 Diagnostic | **2 週** | 中期評估報告(客戶簽收) | Gate A:要不要進 B |
| **B** | 策略 Strategy | **4 週** | 完整顧問診斷報告 + Roadmap + ROI + 治理 | Gate B:要不要進 C |
| **C** | 落地 Implementation | **24 個月** | 轉型路徑圖 + 變革管理 + **每季回核 Stage 2 雷達** | Gate C:每季要不要續 |

> **Phase 含哪些 Stage(已定案)**:**Phase A = Stage 1–3、Phase B = Stage 4–7、Phase C = Stage 8**(每季回核 Stage 2 雷達)。階段名用 §2 圖 B 的甲。

### §2.5 — 八階段命名(已統一為甲,決議定案 2026-06-18)
**唯一八階段 = 甲**(`EIGHT_STAGE_FLOW_STORY.md`,本檔 §2 圖 B):
As-Is → Reference Model → Ideal Practice → Gap Analysis → Problem Definition → Phased Goals → To-Be Design → Implementation。
> 舊的「報告生產子系統」曾用一套不同命名(乙:Awareness/Discovery/Stakeholder/Diagnosis/Acceptance Test),**已停用,全部遷移為甲**。對映:Awareness→As-Is、Discovery→Ideal Practice、Stakeholder→Problem Definition、Diagnosis→Phased Goals、Acceptance Test→Implementation(Reference Model / Gap Analysis / To-Be Design 兩邊同名)。任何文件再出現乙的階段名即為待修。

### 圖 D — 接案生命週期(Engagement Lifecycle,經營)
**Sales → Delivery → Support(季度回看)**。本體在 **`06_Delivery/ENGAGEMENT_LIFECYCLE.md`**(不是 `08_Project_Managements`,後者只放 WBS 模板)。

---

## 3. 授權(唯一標準)
- **全系列(文字 + 軟體)目前一律 Apache License 2.0**,以根目錄 `LICENSE`、`CITATION.cff`、`NOTICE` 為準。
- ❌ 在任何文件/頁面**不要**單方面宣稱「文字 CC BY 4.0」——目前 repo 內**無 CC BY 4.0 授權檔**,宣稱即斷裂。
- 若未來要對「文字」採 CC BY 4.0 雙授權,須先:新增 CC BY 4.0 授權檔 → 明確定義哪些路徑屬「文字」→ 同步更新 README/NOTICE/CITATION。在那之前,**一律 Apache 2.0**。

## 4. 待同步清單(本次憲法整理後的狀態)
- [x] 全系列移除「文字 CC BY 4.0」宣稱,統一 Apache 2.0(§3)。
- [x] 上集所有顧問能力 L1–L5 → C1–C5(§1)。
- [x] 下集互動頁八階段(圖 B)/Phase(時長+交付物)/企業 L1–L5 正式名 對齊(§2、§1)。
- [x] 移除「Series II / 顧問系列 II / Book II (Series II)」寫法,改 Book I/II(§0)。
- [x] repo 定位改「系列總庫」;接案生命週期指向 `06_Delivery/ENGAGEMENT_LIFECYCLE.md`(§Repo 定位、圖 D)。
- [x] 兩個 Skill(thinking/delivery coach)裝進 repo `.claude/skills` 與 `.codex/skills`。
- [x] **八階段命名定案:統一為甲**(2026-06-18 Founder 拍板,§2.5)。Phase→Stage = A:1-3 / B:4-7 / C:8(每季回核 Stage 2)。
- [x] `03_Consulting_Report/`(README 多語 + `CONSULTING_TOOLKIT_TEMPLATES`/`REPORT_PRODUCTION_WORKFLOW`/`REPORT_TEMPLATE`/`FRAMEWORKS_LIBRARY`)八階段名與 Phase 切分遷移為甲。
