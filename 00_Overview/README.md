# 00 Overview — 方案總論與入口

## 一、本目錄定位

本目錄是整套 **AI 顧問方法論工具包**的**唯一入口**。它不放任何「工具」或「交付物」，只放兩件事：**方法論的故事**，以及**方法論的狀態**。

任何人第一次接觸這個 repo —— 顧問要學會這套方法、客戶要評估要不要買、新進同事要 onboard、reviewer 要審查 —— 都應該從這裡開始。先在這裡建立「這套方法論是什麼、為什麼這樣設計、現在做到哪」的整體脈絡，再進到 `01`-`06` 的功能目錄，才不會見樹不見林。

本目錄要解決的問題是：**一個方法論若沒有清楚的入口與狀態，使用者會迷路、會誤用、會不知道哪些已完成哪些還在進行。**

## 二、在方法論中的位置

| 軸 | 對應 |
| --- | --- |
| 三段式服務流程 | 不對應單一段；是「診斷 → 建置 → 交付」三段的**鳥瞰地圖** |
| 八階段顧問結構 | 不對應單一階段；是八階段的**總覽** |
| L1-L5 成熟度 | 不對應單一級；是 L1-L5 的**總覽** |
| 接案生命週期 | 不對應單一階段；是整個生命週期的**起點說明** |

> 邏輯定位：`00_Overview` 回答「**是什麼、為什麼**」；`01`-`06` 回答「**怎麼做**」；`90_References` 回答「**依據與引用**」。

## 三、目標與效益

| 目標 | 效益 |
| --- | --- |
| 讓新讀者 5-10 分鐘理解方法論骨架 | 縮短 onboarding；減少誤用 |
| 用客戶語言講方法論的價值主張 | 業務可直接拿故事線對客戶簡介 |
| 維護一份權威的專案狀態文件 | 任何人都能查「現在做到哪、下一步是什麼」，不靠口頭交接 |
| 串起 `01`-`06` 與 `90` 的關係 | 使用者知道每個目錄的角色與先後順序 |

**若跳過本目錄**：使用者會直接跳進功能目錄，不理解「為什麼這個目錄存在、它跟其他目錄怎麼接」，導致工具被孤立使用、方法論變成一堆散落的檔案。

## 四、使用流程與邏輯

```text
新讀者 / 客戶
   → 讀 AI_TRANSFORMATION_STORY_AND_STRUCTURE.md（為什麼 + 怎麼運作 + 產出什麼）
   → 建立「L1-L5 + 八階段 + 三段式流程」的整體心智圖
   → 轉進 01_Assessment 開始實際的診斷

顧問 / 同事 / reviewer
   → 讀 TODO_WBS.md（專案做到哪、變更紀錄、下一輪候選、工作日誌）
   → 掌握現況後再動手
```

| 步驟 | 誰 | 何時 | 輸入 | 輸出 |
| --- | --- | --- | --- | --- |
| 讀故事線 | 顧問 / 客戶 / 新人 | 第一次接觸 repo | 無 | 對方法論的整體理解 |
| 對客戶簡介 | 業務 / 顧問 | 接案前第一次會談 | 故事線 | 客戶願意進入診斷 |
| 查專案狀態 | 顧問 / 同事 / reviewer | 接手 / 審查前 | 無 | 知道現況與下一步 |
| 更新狀態 | 負責的顧問 / AI | 每完成一個批次 | 完成的工作 | 更新後的 `TODO_WBS.md` |

> 邏輯：故事線是「對外」的（給客戶與新人建立認知）；`TODO_WBS.md` 是「對內」的（給執行者掌握現況）。兩者一外一內，構成完整入口。

## 五、檔案說明

### `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`

客戶導向的方案故事與章節架構。它不是技術文件，而是**敘事** —— 把「企業為什麼需要 AI 轉型、這套方法怎麼一步步運作、每一步會產出什麼可驗收的東西」講成一個連貫、客戶聽得懂的故事。包含：方案定位、三段式路徑、L1-L5 與工具對應、課前未來想像、各角色（CEO/COO/CIO/IT/HR/部門主管）的價值主張、§6 完整八階段定義 + 6 週情境演練。業務與顧問在第一次客戶會談時直接用它。

### `EXECUTIVE_SUMMARY.md`

5 分鐘看懂整套方法論的一頁濃縮。給沒空看細節的主管。

### `CLIENT_JOURNEY_STORY.md` 🆕

**阿明的故事** —— 一個讓 CEO / 董事 / 家人 20 分鐘看懂方法論的場景故事。以製造業 700 人封測廠 24 個月轉型為主線，零工具表、零黑話。對外宣傳、客戶第一次接觸、面試新員工都可以用。

### `EIGHT_STAGE_FLOW_STORY.md` 🆕

**權威八階段流程故事**：3 階段合約模型（Phase A 診斷 2W + Phase B 策略 4W + Phase C 落地 24M）+ 中期評估報告 + 季度雷達回看的完整閉環。顧問內部訓練必讀。

### `METHODOLOGY_SCIENTIFIC_LOGIC.md` 🆕

**方法論的科學辯論能力**：用科學方法的 5 條件（可觀察、可量化、可重複、可證偽、可審核）逐步驗證八階段為什麼經得起客戶 / 董事會 / 監管者質詢。學術投稿、政策遊說、董事會 review 必讀。

### `INDUSTRY_FRAMEWORK_ALIGNMENT.md` 🆕

**跟業界框架對齊地圖**：八階段 vs McKinsey / BCG / Bain / Deloitte / Accenture / PwC；4 層架構 vs TOGAF / Zachman / Dragon1；L1-L5 vs Gartner / MIT / Forrester AI Maturity。客戶問「跟我們現有方法論衝突嗎」時就拿這份。

### `AI_NATIVE_LIVING_BOOK.md` 🆕

**方法論承載形式的創新論述**：把這套方法論定位為 **AI-native living book**（可被 AI IDE 直接執行的知識系統），不只是 PDF / PPT。包含學術歸類（executable knowledge artifact、AI-mediated methodology、interactive consulting playbook）、3 層設計（Repo as Book / Agent as Tutor / Methodology as Executable Artifact）、4 大風險控管原則（AI ≠ 顧問、需 evidence、AGENTS.md 版本控管、AI 產出明示）。學術投稿 / 方法論差異化必讀。

### `ACADEMIC_THEORETICAL_FOUNDATIONS.md` 🆕

**7 大理論支柱統一論述**：Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Task-Technology Fit (Goodhue & Thompson 1995) + Dynamic Capabilities (Teece 1997/2007) + Sociotechnical Systems & Trust in AI (Bostrom 1977/Dietvorst 2015/Glikson 2020) + Real Options (Dixit & Pindyck 1994/McGrath 1997) + Executable Knowledge Artifact (Knuth 1984)。每個理論：summary + 創立者 + 對 Tiger AI 的貢獻 + 對應位置 + 引用。學術審稿 / 監管 / 高階董事會質詢「理論依據是什麼」時的唯一答案。

### `../01_Assessment/BARS_RUBRICS.md` 🆕（學術硬化）

**Behaviorally Anchored Rating Scales**：6 構面 × 0-4 分的**行為錨點表**（依 Smith & Kendall 1963）。每個分數有具體可觀察的行為，**避免顧問主觀評分**，提升 inter-rater reliability。對應 Pilot Study Cohen's κ ≥ 0.60 目標。讓兩位顧問評同公司能得相近分數的核心機制。

### `TODO_WBS.md`

本 repo 的**權威狀態文件**，是唯一可信的「現在做到哪」來源。內容包含：WBS 總覽（工作項目 × 優先級 × 狀態）、已完成文件清單、已完成項目明細、未完成 TODO、下一輪建議優先順序、**變更紀錄（每批次 + commit hash）**、目前狀態總覽、**每日工作日誌**。顧問接手、reviewer 審查、AI 繼續工作前，都應先讀這份。任何批次工作完成後，也應回來更新它。

### `*_EN.md`

上述檔案的英文版 sibling，內容與中文版對應。

## 六、與其他目錄的對應

| 目錄 | 與本目錄的關係 | 資料流 |
| --- | --- | --- |
| `01_Assessment` | 故事線的「診斷」段在此落實 | `00` 故事 → `01` 診斷工具 |
| `02_Course_Design` | 故事線的「建置」段在此落實 | `00` 故事 → `02` 課程 |
| `03_Consulting_Report` | 故事線的「交付」段在此落實 | `00` 故事 → `03` 顧問報告 |
| `04_Scenarios` | 提供故事線中的客戶情境與案例素材 | `04` 案例 ↔ `00` 故事 |
| `05_Sales` | 把故事線變成可銷售的素材 | `00` 故事 → `05` 銷售素材 |
| `06_Delivery` | 把方法論變成可交付、可營運的生意 | `00` 故事 → `06` 交付與營運 |
| `90_References` | 方法論的原始依據與第三方引用授權 | `90` 依據 → 支撐 `00`-`06` |

## 七、常見用法情境

- **業務要約客戶**：拿 `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md` 的三段式路徑與價值主張，做 30 分鐘方法論簡介。
- **新顧問 onboard**：先讀故事線建立認知 → 讀 `TODO_WBS.md` 掌握現況 → 再依 §六的資料流逐目錄學習。
- **reviewer 審查**：直接看 `TODO_WBS.md` 的變更紀錄與工作日誌，對照 git log。
- **AI 接續工作**：讀 `TODO_WBS.md` 的「下一輪候選」與「工作日誌」，知道從哪裡繼續。

---

## ⭐ 跨主題對照：5 個核心主題去哪查

整本方法論有 5 條主動脈，貫穿所有目錄。本目錄與它們的關聯如下：

| 跨主題 | 主檔案位置 | 本目錄如何接 |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 三引擎共讀** | 根 [`README.md`](../README.md) §🌟 ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | **本目錄就是 AI-Native Living Book 的「故事入口」** —— [`AI_NATIVE_LIVING_BOOK.md`](AI_NATIVE_LIVING_BOOK.md) 完整論述；4 份權威概念檔（CLIENT_JOURNEY / EIGHT_STAGE_FLOW / METHODOLOGY_SCIENTIFIC_LOGIC / INDUSTRY_FRAMEWORK_ALIGNMENT）都在這 |
| 🎓 **成熟理論（7 大支柱）** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **7 大理論支柱統一論述就放在本目錄**：Rosemann / Cohen & Levinthal / TTF / Teece / Sociotechnical Trust / Real Options / Knuth |
| 📚 **L1-L5 課程教育** | [`../02_Course_Design/`](../02_Course_Design/) | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 是 **L1-L5 兩條軸**（規模軸 + AI 自主軸）的權威故事入口 |
| 🔁 **顧問方案 / 8 階段 + Phase A→B→C 閉環** | [`EIGHT_STAGE_FLOW_STORY.md`](EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **顧問閉環故事就放在本目錄** —— `EIGHT_STAGE_FLOW_STORY.md` §6 完整閉環圖（Phase A 2W + Phase B 4W + Phase C 24M + 季度雷達回看）|
| 📖 **參考資料 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | 本目錄的故事使用 `90_References` 的所有素材作依據（PDF / 圖 / 影片筆記 / 學術理論引用） |
