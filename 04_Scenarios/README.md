# 04 Scenarios — 情境、案例與案例索引

> 🌐 語言：繁體中文 ｜ [English](README_EN.md) ｜ [Deutsch](README_DE.md) ｜ [Français](README_FR.md) ｜ [Español](README_ES.md) ｜ [日本語](README_JA.md) ｜ [한국어](README_KR.md)

> ⚠️ **重要學術誠信聲明 / Important Academic Integrity Disclaimer**
>
> **本目錄中所有 7 個 SAMPLE_CLIENT_CASE_*.md 案例（製造業、醫院、行銷、B2B、金融、政府、教育）以及任何具名的故事主角（如 `00_Overview/CLIENT_JOURNEY_STORY.md` 阿明的故事），皆為 AI 模擬產生的虛構案例，並非真實客戶資料。**
>
> - **用途**：教學示範、方法論講解、Stage 1-8 工具表套用練習
> - **限制**：所有數字（時間、ROI、人月、預算、KPI）僅為示例，**不可作為對外宣傳、合約承諾、學術 empirical evidence**
> - **證據等級**：依 [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 8.9，本目錄案例屬 **L0（AI-Simulated Teaching Case）**，低於 L1 自評問卷
> - **真實 longitudinal cases** 需透過 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) 18-24 個月實證研究完成後才會替換
>
> ⚠️ **Important**: All 7 sample cases in this directory and any named story protagonists (e.g., "Ming" in `CLIENT_JOURNEY_STORY.md`) are **AI-generated fictional cases**, not real client data. Numbers are illustrative; must NOT be used as marketing, contractual commitments, or academic empirical evidence. Real cases will replace these after the 18-24 month pilot study.

## 一、本目錄定位

本目錄是整套方法論的**素材庫與證據庫**。`01`-`03`、`05`、`06` 是「方法與流程」；本目錄是「**讓方法落地時有真實的情境、案例、案例可挑**」。

它要解決的問題是：**企業導入 AI 時最大的卡點，不是「不會做」，而是「不知道可以做什麼、別人怎麼做、做了會長什麼樣」。** 本目錄提供四種素材：(1) 各角色/部門的**情境故事**（讓客戶「對號入座」）、(2) 案例的**書寫標準與控制表**（讓顧問寫出一致的案例）、(3) 7 個產業的**完整示範案例**（從問卷到 Roadmap 的完整走一遍）、(4) 150+ 個真實 LLM 應用的**案例索引表**（依 L 級與部門兩軸快速查詢）。

使用本目錄的人：顧問（Discovery 時拿情境讓客戶對號入座、用案例索引挑 PoC）、業務（用案例佐證價值）、課程講師（用案例當示範題）、客戶（看完整案例理解「導入後長什麼樣」）。

## 二、在方法論中的位置

| 軸 | 對應 |
| --- | --- |
| 三段式服務流程 | **跨全程** —— Discovery 用情境、Build 用案例當題目、Deliver 用案例佐證 |
| 八階段顧問結構 | 主要支援 **Stage 1 As-Is Snapshot（現況情境）、Stage 3 Best Practice Integration（產業最佳實務對標）** |
| L1-L5 成熟度 | 案例索引表把每個案例對應到 L 級 |
| 接案生命週期 | Sales（Discovery 對號入座）+ Build（示範題）|

## 三、目標與效益

| 目標 | 效益 |
| --- | --- |
| 提供各角色/部門情境故事 | 客戶能「對號入座」，Discovery 更快聚焦 |
| 案例書寫標準與控制表 | 顧問寫出結構一致、可驗證的案例 |
| 7 個產業完整示範案例 | 客戶看得到「導入後的全貌」；新顧問有範本 |
| 150+ LLM 應用案例索引（雙軸查詢）| 客戶/顧問依「L 級」或「部門」秒查可做的事 |
| 跨級期待管理 | 客戶指著 L5 案例時，用索引指出「你在 L2，要先補」 |

**若跳過本目錄**：客戶對「能做什麼」沒概念、PoC 選題憑空想、顧問案例品質不一、無法管理跨級期待。

## 四、使用流程與邏輯

```text
Discovery 階段
   → CUSTOMER_SCENARIO_LIBRARY（各角色情境，讓客戶對號入座）
   → LLM_APPS_CASE_INDEX（依客戶 L 級 + 部門，挑出「客戶有感」的案例）
   → 挑出的案例 → PoC 候選

課程 / 提案階段
   → SAMPLE_CLIENT_CASE_*（給客戶看同產業的完整案例）
   → LLM_APPS_CASE_INDEX（課堂示範題、練習題）

顧問寫新案例時
   → CASE_WRITING_STANDARD（書寫標準）
   → CASE_CONTROL_TABLES（控制表，直接複製填寫）
```

| 步驟 | 誰 | 何時 | 輸入 | 輸出 |
| --- | --- | --- | --- | --- |
| 客戶對號入座 | 顧問 | Discovery | 情境故事庫 | 客戶認領的痛點 |
| 挑 PoC 候選 | 顧問 | 診斷後 | L 級 + 部門 → 案例索引 | PoC 候選清單 |
| 給客戶看完整案例 | 業務 / 顧問 | 提案 | 同產業 sample case | 客戶理解全貌 |
| 寫新案例 | 顧問 | 專案結束後 | 書寫標準 + 控制表 | 新的 sample case |

> 邏輯：情境故事是「**引發共鳴**」（客戶說「對，我就是這樣」）；案例索引是「**快速選材**」（依 L 級/部門秒查）；完整示範案例是「**展示全貌**」（從問卷到 Roadmap）；書寫標準是「**確保一致**」（新案例品質穩定）。

## 五、檔案說明

### 情境與標準

| 檔案 | 用途 |
| --- | --- |
| `CUSTOMER_SCENARIO_LIBRARY.md` | 各角色/部門情境故事：CEO、COO、IT、HR 與業務、客服、行銷、營運、財務、人資、IT 部門；每個故事含 Before、Trigger、AI Flow、Systems、Output、KPI。 |
| `CASE_WRITING_STANDARD.md` | 案例書寫標準，規定 L1-L5 的 Input / Process / Output / Evidence 與可驗證交付物的寫法。 |
| `CASE_CONTROL_TABLES.md` | 案例控制表，可直接複製填寫評估活動、L1-L5 IPOE、Evidence、Stage Gate、風險治理、Deliverables 驗收。 |
| `INDUSTRY_SCENARIOS.md` | 零售/教育/物流/軟體/專業服務 5 產業推薦場景，每產業含簡介、L1-L5 基線、Top 10 場景、風險治理、30 天 Quick Win、Anti-Patterns。 |

### 完整示範案例（客戶皆以代號表示）

| 檔案 | 案例 |
| --- | --- |
| `SAMPLE_CLIENT_CASE_MANUFACTURING.md` | 研發製造業完整案例 |
| `SAMPLE_CLIENT_CASE_HOSPITAL.md` | 醫院 / 醫療機構（高敏感資料、全地端、人工審核）|
| `SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md` | 行銷代理商（代號：代理商 M）|
| `SAMPLE_CLIENT_CASE_B2B_SALES.md` | B2B 工業設備商（代號：工業設備商 B），聚焦 RFP、CRM 治理、L5 Pre-RFP Team |
| `SAMPLE_CLIENT_CASE_FINANCIAL.md` | 金融業（代號：區域銀行 F），全地端、雙審 |
| `SAMPLE_CLIENT_CASE_GOVERNMENT.md` | 政府機關（代號：市政府數位局 G），全地端、三審 |
| `SAMPLE_CLIENT_CASE_EDUCATION.md` | 教育機構（代號：科技大學 E），Hybrid、學術倫理 |

> 每個案例都走完整流程：問卷結果 → L 級判定 → 課程比例 → 課中產出 → 八階段分析 → 診斷報告摘要 → 30/60/90 Roadmap → ROI → 風險治理。

### L5 實作與案例索引

| 檔案 | 用途 |
| --- | --- |
| `CLAWTEAM_WALKTHROUGH.md` | 以 ClawTeam（HKUDS, MIT）跑通跨部門 Agent Team 的完整 walkthrough（製造業 QA Team），含環境設定、任務鏈、Human Gate、Gate 5 對應。 |
| `LLM_APPS_CASE_INDEX.md` | **LLM 應用案例索引表（多來源）**。150+ 個真實 LLM app，**兩個查詢軸**：①依 L1-L5 / 課程 ②依企業部門/流程（工程/財務/人事/業務/行銷/研發/營運/客服/法務/資料/設計/管理層）。來源：awesome-llm-apps（Apache-2.0）、ai-engineering-hub（MIT）。|

### `*_EN.md`

部分檔案的英文版 sibling。

## 六、與其他目錄的對應

| 目錄 | 與本目錄的關係 | 資料流 |
| --- | --- | --- |
| `01_Assessment` | 診斷的 L 級決定從案例索引挑哪些 | `01` L 級 → `04` 案例篩選 |
| `02_Course_Design` | 案例/PoC 索引是課堂示範題與練習題來源 | `04` 案例 ↔ `02` 課程題目 |
| `03_Consulting_Report` | 八階段 Stage 3 產業最佳實務對標引用案例 | `04` 案例 → `03` Stage 3 |
| `05_Sales` | 完整案例與情境是銷售素材的佐證 | `04` 案例 → `05` 銷售佐證 |
| `00_Overview` | 情境故事是故事線的素材 | `04` ↔ `00` |
| `90_References` | 案例索引的第三方引用（awesome-llm-apps / ai-engineering-hub）| `90` 引用 → `04` |

## 七、常見用法情境

- **Discovery 對號入座**：拿 `CUSTOMER_SCENARIO_LIBRARY.md` 對應客戶角色，問「哪個故事像你？」。
- **挑 PoC**：診斷出 L 級後，到 `LLM_APPS_CASE_INDEX.md` §3 依 L 級、或 §4 依部門，挑 3-5 個客戶有感的。
- **提案佐證**：給製造業客戶看 `SAMPLE_CLIENT_CASE_MANUFACTURING.md`，展示完整導入全貌。
- **跨級期待管理**：客戶指 L5 案例 → 用索引指出其 L 級與所需的前置課程。
- **寫新案例**：專案結束後依 `CASE_WRITING_STANDARD.md` + `CASE_CONTROL_TABLES.md` 把它寫成新的 sample case。

---

## ⭐ 跨主題對照：5 個核心主題去哪查

整本方法論有 5 條主動脈，貫穿所有目錄。本目錄與它們的關聯如下：

| 跨主題 | 主檔案位置 | 本目錄如何接 |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 三引擎共讀** | 根 [`README.md`](../README.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | 案例可用 Claude Code Tier 2 工作流跑：`/simulate-engagement` 模擬完整 6 週顧問案、`/parallel-perspectives` 6 利害關係人視角、`/devil-pair-debate` 辯論案例的價值觀預設 |
| 🎓 **成熟理論（7 大支柱）** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | 案例的 ROI 論述對應 **Real Options**（為何 Phase 1 看似 NPV ≈ 0 仍值得投）；案例的 To-Be 設計對應 **Task-Technology Fit**（哪些任務該到 L4、哪些該停在 L2）|
| 📚 **L1-L5 課程教育** | [`../02_Course_Design/`](../02_Course_Design/) | LLM Apps Case Index 依 L 級分類，可直接挑為 PoC；`POC_SCENARIO_SPECS.md` + `N8N_WORKFLOW_TEMPLATES.md` 把案例變成 L3 課堂實作題 |
| 🔁 **顧問方案 / 8 階段 + Phase A→B→C 閉環** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **案例是 Phase A Discovery 的「對號入座」素材**（讓客戶說「對，我就是這樣」）；產業 Best Practice 對標到八階段 Stage 3；7 個完整 sample case 是 Phase B 顧問報告的範本 |
| 📖 **參考資料 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | LLM Apps Case Index 來源：`Shubhamsaboo/awesome-llm-apps`（Apache-2.0）+ `patchy631/ai-engineering-hub`（MIT），完整致敬卡見 [`../90_References/README.md`](../90_References/README.md) §2.4；ClawTeam Walkthrough 來自 `HKUDS/ClawTeam`（MIT）|
