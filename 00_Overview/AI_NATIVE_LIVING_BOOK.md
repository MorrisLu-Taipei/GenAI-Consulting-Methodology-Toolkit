# AI-Native 活書：方法論作為可執行知識物件 (Executable Knowledge Artifact)

> 🌐 English version: [AI_NATIVE_LIVING_BOOK_EN.md](AI_NATIVE_LIVING_BOOK_EN.md)
>
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技

更新日期：2026-05-16

---

> **本文回答**：這套方法論最特別的地方不是內容，而是**承載形式**。傳統顧問方法論是 PDF / PPT / SOP（靜態文件）；本 repo 是**可被 AI IDE 讀取、解釋、問答、套用的知識系統**。使用者不是「讀文件」，而是「**和方法論對話**」。本文將這個特色正式寫入方法論定位，並回應其學術歸類與風險控管。

---

## 1. 一句話定位 / Tagline

**中文**：

> 這不只是一本方法論手冊，而是一本 **AI-native 的活書 (AI-native living book)**：當使用者用 AI IDE 打開 repo，[`AGENTS.md`](../AGENTS.md) 與 [`CLAUDE.md`](../CLAUDE.md) 會把 AI 轉換成**共讀導師 (co-reading tutor)**，帶使用者理解、提問、套用並產出顧問交付物。

**English**:

> This repository is not only a methodology toolkit, but an **AI-native living book**: when opened in an AI IDE, its embedded agent instructions turn the static methodology into an **interactive co-reading tutor and consulting assistant**.

---

## 2. 為什麼這是方法論的全新形式

### 2.1 傳統顧問方法論 vs AI-native 活書

| 維度 | 傳統方法論（PDF / PPT / SOP）| AI-Native Living Book（本 repo）|
| --- | --- | --- |
| **承載形式** | 靜態文件、Slide deck、Word | Markdown + AI IDE 指令檔（AGENTS.md / CLAUDE.md）|
| **使用者互動** | 單向閱讀 | 雙向對話（問答、套用、生成）|
| **入門門檻** | 高（100+ 頁要自己讀完）| 低（AI 自動讀完、變共讀導師）|
| **可被套用的方式** | 靠顧問翻譯給客戶 | 客戶直接請 AI 套到自己公司 |
| **可被反問** | 不行（文件不會回答）| 可以（AI 即時回答任何質詢）|
| **可被改寫** | 需顧問改 | 客戶 fork 後可即時改 + AI 協助一致性檢查 |
| **版本控制** | 通常無 | Git 全程版本（含 AGENTS.md 變更歷史）|
| **學術引用** | 引用 PDF | 引用 GitHub commit hash + 可重現執行環境 |

### 2.2 學術歸類選項

本方法論可被歸類為以下任一（或多重）類型：

| 命名 | 強調的特性 | 出處 / 類比 |
| --- | --- | --- |
| **Executable Knowledge Artifact** | 可被執行的知識；不只是描述，是可被套用的程序 | Notebook (Jupyter), Computational essays |
| **AI-Mediated Methodology** | AI 作為使用者與方法論之間的中介 | Tutoring systems, Intelligent Tutoring Systems (ITS) |
| **Interactive Consulting Playbook** | 互動式顧問操作手冊 | Game playbooks, decision-tree wizards |
| **Living Book with Embedded Tutor Agent** | 活書 + 嵌入式導師代理 | Hypertext, knowledge graphs |

Tiger AI 採用 **AI-native living book** 作為主稱，因為它**同時涵蓋**「活書」（內容會演進）+「AI-native」（為 AI 而生的設計）+「co-reading tutor」（嵌入式導師人格）三層意義。

---

## 3. 三層設計：Repo as Book / Agent as Tutor / Methodology as Executable Artifact

### 3.1 Layer 1：Repo as Book（repo 即一本書）

repo 結構符合「**書**」的體例：

| Book Element | repo 對應 |
| --- | --- |
| 封面 / 一句話定位 | 根 [`README.md`](../README.md) + 本檔 §1 一句話定位 |
| 序言 / 執行摘要 | [`EXECUTIVE_SUMMARY.md`](EXECUTIVE_SUMMARY.md) |
| 故事章節 | [`CLIENT_JOURNEY_STORY.md`](CLIENT_JOURNEY_STORY.md) 阿明的故事 |
| 方法論主體 | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §6 八階段 |
| 實作章節 | `01_Assessment` / `02_Course_Design` / `03_Consulting_Report` |
| 案例集 | `04_Scenarios/` 7 個 Benchmark-grade 案例 |
| 銷售輔助 | `05_Sales/` |
| 接案 SOP | `06_Delivery/` |
| 學術論證 | [`METHODOLOGY_SCIENTIFIC_LOGIC.md`](METHODOLOGY_SCIENTIFIC_LOGIC.md) |
| 對齊地圖 | [`INDUSTRY_FRAMEWORK_ALIGNMENT.md`](INDUSTRY_FRAMEWORK_ALIGNMENT.md) |
| 失敗模式（反例） | [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) |
| 研究設計 | [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) |
| 引用文獻 | 每檔末 References + `90_References/` |

> **重點**：這份「書」**完整**到客戶 / 顧問 / 學者 / 監管者都能各自找到自己要的章節。

### 3.2 Layer 2：Agent as Tutor（AGENTS.md 即「導師人格」）

[`AGENTS.md`](../AGENTS.md) 與 [`CLAUDE.md`](../CLAUDE.md) 不是補充說明，而是把 **AI 的角色、邊界、引導方式寫進 repo**。AI IDE（Claude Code / Cursor / Antigravity / Codex 等）會自動讀取這兩份檔案，把自己定位為「**這套方法論的共讀導師**」。

#### AGENTS.md 內含的「導師人設」

- **角色定位**：AI = 共讀導師 + 顧問助理，不是替代顧問
- **可回答的問題範圍**：方法論定義、L1-L5 對應、Stage 工具、案例套用、報告草稿
- **必須拒絕的範圍**：替客戶做最終決策、繞過顧問判斷、提供未經驗證的 ROI 承諾
- **回答風格**：學術嚴謹 + 顧問實務 + 客戶可懂
- **引用紀律**：每段結論必標 [E:L#] 證據等級（依 Tool 8.9）
- **語言**：中英雙語切換、依使用者語言

> **這個設計借鏡 LangChain Agent Prompt + Claude Skills 的精神**：把「AI 該怎麼回應」寫成 repo 內可被版本控管的設定檔。

### 3.3 Layer 3：Methodology as Executable Artifact（方法論可被執行）

使用者可以直接請 AI **執行方法論**，而不只是「讀方法論」：

#### 典型互動範例

| 使用者問 | AI 共讀導師執行 |
| --- | --- |
| 「我公司 700 人封測廠，幫我快速做 10 題問卷」 | AI 跑 [`AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) 10 題版 + 自動評分 + 產雷達圖 |
| 「依我剛剛回答，幫我寫 Phase A 中期評估報告骨架」 | AI 依 [`CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md) §3-§5 結構生成草稿 |
| 「我們是製造業，跟哪個案例最像？」 | AI 對比 [`SAMPLE_CLIENT_CASE_MANUFACTURING.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_MANUFACTURING.md) 並算差距 |
| 「Stage 3 客戶 Ideal Practice 工作坊，幫我準備材料」 | AI 依 Tool 3.6 6 步驟產出 workshop 流程 + 便利貼題目 + 4 層架構列印版 |
| 「跟 McKinsey 的 7-Step 怎麼對齊？」 | AI 對應 [`INDUSTRY_FRAMEWORK_ALIGNMENT.md`](INDUSTRY_FRAMEWORK_ALIGNMENT.md) §2.1 |
| 「最近 24 個月我的 Stage 2 雷達應該變圓嗎？」 | AI 引導使用者跑季度 Gate C 回顧 |

> **這就是「Methodology as Executable Artifact」的具體意義** —— 方法論不只描述，可被 AI 即時套用。

---

## 4. 降低方法論採用門檻

### 4.1 一般企業看 100+ 份 Markdown 會怕

傳統顧問方法論的採用門檻：

- 100+ 頁要自己讀完 ❌
- 名詞太多看不懂 ❌
- 不知道哪份先看 ❌
- 套到自家公司要靠顧問翻譯 ❌
- 報告草稿要自己寫 ❌

### 4.2 AI 共讀導師可以即時回答的問題

打開 repo + AI IDE 後，使用者直接問：

- 「**我公司現在在哪一級？**」→ AI 跑 10 題問卷 + 自動評分
- 「**我應該先看哪份？**」→ AI 依角色（CEO / 顧問 / IT / 學者）推薦閱讀順序
- 「**這個方法怎麼套到製造業？**」→ AI 引製造業案例 + 提示客製化要點
- 「**請幫我生成第一版診斷報告**」→ AI 依 Phase A 流程產 10-15 頁骨架報告
- 「**Stage 4 vs Stage 8 的分際是什麼？**」→ AI 引用 METHODOLOGY_SCIENTIFIC_LOGIC §4

> **這讓 methodology 從「專家才能讀懂」變成「非專家也能被帶著走」**。

### 4.3 採用門檻降低的數據（預期）

依 PILOT_STUDY_PROTOCOL 假設驗證：

- 傳統 PDF 方法論：客戶讀完率 < 15%
- **AI-native living book**：客戶「對話過」比例 > 70%（因為 AI 主動引導）
- 中型企業（100-500 人）採用週期：從「需要 3 個月評估」→「2 週內可進 Phase A」

---

## 5. 風險控管 (Risk Controls)

⚠️ 因為 AI 會解讀方法論，必須明確界定 **AI 共讀導師不能做什麼**：

### 5.1 AI 共讀導師的邊界

| 可以做 | 不可以做 |
| --- | --- |
| 解釋方法論內容 | ❌ 替代正式顧問判斷 |
| 跑問卷、自動評分、產雷達圖 | ❌ 對客戶承諾具體 ROI 數字 |
| 引用案例算差距 | ❌ 簽署 Ideal Practice 定義表（必須三方人類簽名）|
| 產出報告草稿 | ❌ 取代客戶 owner / 顧問的最終 review |
| 引導 Stage Gate 自評 | ❌ 替代第三方稽核 |
| 對 80% / 5 Whys / Issue Tree 等框架做即時應用 | ❌ 取代縱貫 KPI 追蹤的真實資料 |

### 5.2 4 大風險控管原則

1. **AI 共讀導師 ≠ 顧問**：所有報告草稿須由**人類顧問或客戶 owner 審核**才能對外使用
2. **重要診斷需保留 evidence**：依 [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 8.9 Evidence Hierarchy，重要結論需 L3+ 證據（系統 log）支撐
3. **AGENTS.md 版本控管**：避免不同 AI IDE 解讀不一致 ── 每次 AGENTS.md 修改 commit 上 Git，並於 CHANGELOG 記錄
4. **AI 產出明示**：依 Tool 8.8 §7 「AI 產出內容明示『AI 產生』標記」 ── 客戶看到的所有 AI 生成內容必須標記

### 5.3 失敗情境

若 AI 共讀導師被誤用，可能發生（已記錄於 [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md)）：

- AI 答錯而客戶當真 → 報告錯誤
- AI 給出未經 evidence 的 ROI 數字 → 客戶簽 SOW 後失望
- 不同 AI IDE 對 AGENTS.md 解讀不同 → 結論不一致

**緩解**：

- AGENTS.md 內明確規範「**Don't predict ROI without baseline data**」
- 報告每段強制 [E:L#] 證據等級標籤
- 鼓勵客戶用 ≥ 2 種 AI IDE 交叉驗證關鍵結論

---

## 6. 學術貢獻 / Academic Contribution

### 6.1 對 Information Systems / Consulting Methodology 領域的貢獻

| 貢獻 | 創新點 |
| --- | --- |
| **方法論承載形式創新** | 首次把顧問方法論做成可被 AI IDE 直接執行的 Markdown + agent config 結構 |
| **AI-mediated knowledge transfer** | 用 AI 作為「知識翻譯者」，降低方法論採用門檻 |
| **Open-source consulting framework** | Apache 2.0，可被其他顧問 fork 改寫，學術可重現 |
| **Embedded tutor agent design pattern** | AGENTS.md / CLAUDE.md 模式可被其他開源 repo 借鏡 |

### 6.2 對 AI Pedagogy 與 ITS（Intelligent Tutoring Systems）的銜接

- 1980s ITS 學派研究「AI 如何教」 → 本方法論是「**AI 如何協助大人學會專業方法論**」的新案例
- 對 Vygotsky 的 ZPD（Zone of Proximal Development）的應用：AI 共讀導師動態調整提示深度

### 6.3 未來研究方向

- 不同 AI IDE（Claude Code / Cursor / Antigravity / Codex / Windsurf）對同一份 AGENTS.md 的解讀一致性
- AI 共讀導師對方法論採用率的縱貫追蹤（依 PILOT_STUDY_PROTOCOL 設計）
- 跨語言（中 / 英 / 日 / 韓）的方法論可採用性研究

---

## 7. 怎麼跟其他文件結合

### 7.1 在不同位置如何陳述

| 位置 | 主要訊息 |
| --- | --- |
| 根 [`README.md`](../README.md) | 一句話定位（§1 中文版）|
| 根 [`README_EN.md`](../README_EN.md) | One-sentence positioning (§1 EN) |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) | 「活起來的書」段落 |
| [`EXECUTIVE_SUMMARY.md`](EXECUTIVE_SUMMARY.md) | 「How to Read This Book」段落 |
| [`AGENTS.md`](../AGENTS.md) | 具體導師人格設定（不在本檔，在 repo 根）|
| 銷售簡報 | 1 張 slide 強調「AI-native living book」差異化 |
| 學術投稿 | 整章作為方法論 contribution 之一 |

### 7.2 跟其他 4 份權威概念檔的關係

| 文件 | 解決的問題 |
| --- | --- |
| [`CLIENT_JOURNEY_STORY.md`](CLIENT_JOURNEY_STORY.md) | 「使用者體驗到什麼」 |
| [`EIGHT_STAGE_FLOW_STORY.md`](EIGHT_STAGE_FLOW_STORY.md) | 「方法論怎麼跑」 |
| [`METHODOLOGY_SCIENTIFIC_LOGIC.md`](METHODOLOGY_SCIENTIFIC_LOGIC.md) | 「方法論為什麼經得起辯論」 |
| [`INDUSTRY_FRAMEWORK_ALIGNMENT.md`](INDUSTRY_FRAMEWORK_ALIGNMENT.md) | 「方法論跟業界框架對齊」 |
| **`AI_NATIVE_LIVING_BOOK.md`（本檔）** | **「方法論的承載形式為什麼是新的」** |

5 份權威檔形成完整方法論論述：**體驗 + 流程 + 科學 + 對齊 + 形式創新**。

---

## 8. 引用文獻 / References

- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors: Lessons learned. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.
- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.（將文件與可執行程式碼結合的早期主張）
- Pérez, F., & Granger, B. E. (2007). IPython: A system for interactive scientific computing. *Computing in Science & Engineering*, 9(3), 21-29.（Jupyter 前身）
- Anthropic (2024). *Claude Code documentation*: <https://docs.anthropic.com/claude/docs/claude-code>
- OpenAI (2024). *Codex / Codex CLI*.
- Cursor (n.d.). *Cursor IDE documentation*.

---

## 9. 結語：方法論的下一階段

傳統顧問方法論的進化：

```
1990s: 紙本顧問報告
   ↓
2000s: PowerPoint deck
   ↓
2010s: SharePoint / Confluence Wiki
   ↓
2020s: GitHub-hosted methodology + open source
   ↓
2025s: AI-Native Living Book（本方法論）
```

**下一步是什麼？** 可能是 **multi-agent consulting team 自動跑完整 Phase A**（AI 顧問 + AI Reviewer + AI 客戶 simulator 三 Agent 協作）—— 這就是 L5 Multi-Agent Organization 在「方法論自身」上的應用。

**但是**：依本文 §5.1，AI 永遠是工具與導師，不是替代品。顧問的人類判斷、客戶 owner 的決策、第三方的稽核 ── 這些**人類治理層**才是方法論可信度的最後保證。

---

授權與引用 / License & Citation

本文為 Apache License 2.0；可使用、修改、商業利用，唯需保留 [`../NOTICE`](../NOTICE) 檔之署名。
