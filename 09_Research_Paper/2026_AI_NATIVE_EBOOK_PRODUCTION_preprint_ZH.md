# AI 原生電子書生產：多 IDE 編排作為方法論工程基礎設施

**設計科學研究**

> 🌐 Languages: [English (source)](2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md) ｜ 繁體中文（本檔）

---

**作者：** Morris Lu（盧業興）
**單位：** Tiger AI（獨立研究）
**ORCID：** 待註冊（將於正式 Zenodo 發布前填入）
**聯絡：** tiger.ai.tw@gmail.com
**版本：** 1.0（工作草稿；**尚未正式 deposit**）
**日期：** 2026-05-18
**授權：** Apache License 2.0
**Artifact DOI：** 待 Zenodo 發布（將於 GitHub `v1.0.0` tag 觸發 webhook 後自動鑄造）
**Preprint DOI：** 待 Zenodo 發布
**Repository：** <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
**可重現性 manifest：** `09_Research_Paper/REPRODUCIBILITY.md`
**Release manifest（凍結版）：** `09_Research_Paper/RELEASE_MANIFEST_v1.0.0.md`（對應 commit `7da82d7`）
**建議引用格式（發布後）：** Lu, M. (2026). *AI-Native eBook Production: Multi-IDE Orchestration as Methodology Engineering Infrastructure*. Working paper. Zenodo. DOI: [發布後填入].

> **狀態說明。** 本文件為待正式發布的工作草稿。所有 DOI 欄位刻意標記為「待發布（pending）」；本草稿不得以虛構的 DOI 形式被引用。GitHub `v1.0.0` tag 觸發 Zenodo webhook 後，數分鐘內 concept DOI 與 version DOI 將取代「pending」標記。

> **譯註。** 本中文版為英文原稿之翻譯。技術術語（如 DSR、LLM、AI IDE、workflow 名稱、commit hash、檔案路徑）刻意保留原文，便於跨語對照與檢索；其他敘述與 section heading 翻譯為中文。如中英文出現歧義，以英文原稿為準。

---

## 摘要

傳統方法論的發展仰賴以年計的單作者循環，產出讀者被動消費的靜態文件。本文以設計科學研究方法探討一種新範式——**AI 原生電子書生產（AI-Native eBook production）**：方法論製品透過多 IDE 協作環境（Claude Code、Cursor、Antigravity、Codex）共同創作、以 Git 進行版本控制、附帶持久識別符（DOI）出版，並以讀者—IDE 互動方式消費，取代線性閱讀。我們以 *GenAI Consulting Methodology Toolkit*（Apache 2.0；n = 354 份 markdown 文件；7 種語言；橫跨三個 IDE 家族的 22 個專門化 AI-IDE workflow）作為此範式的實作。該製品展現四項傳統單一工具寫作無法達成的特性：(1) 跨語言強制執行的同步多語一致性；(2) 多引擎對抗式審查（例如 `/devil-pair-debate`、`/red-team-review`）；(3) 讀者可查詢的執行能力——生產該製品的同一 IDE 可被讀者用 `/socratic-challenge`、`/deep-synthesize` 等 workflow 反向詢問；(4) 透過 Git 歷史加宣告式 workflow 檔案達成的可加密重現衍生鏈。我們依 Hevner 設計科學七大準則進行評估，並與傳統方法論發展循環（McKinsey 7-Step、Rosemann BPM 發展）量化對比。我們討論此範式對方法論工程、HCI 中「IDE 即媒介」命題、以及 LLM 時代「active」學術出版未來的意涵。

**關鍵字：** 設計科學研究；AI IDE；方法論工程；多代理協作；可執行文件；可重現方法論；AI 原生；literate programming；顧問框架

---

## 1. 緒論

### 1.1 動機

方法論工程——對顧問框架、成熟度模型、流程參考架構進行有紀律的構建、驗證與傳播——歷史上一直是緩慢的、單一作者的工藝活動。經典範例如 Capability Maturity Model [Paulk et al. 1993]、Business Process Management Maturity Model [Rosemann & de Bruin 2005]、Process Classification Framework [APQC 2024]，每一項都需要小型專家團隊耗時數年完成，以靜態文件（PDF、期刊論文）形式發布，讀者以根本上被動的方式消費：閱讀，然後嘗試應用。

此工藝模式衍生三項結構性低效：

1. **循環延遲（Cycle latency）。** 新方法論落後其主題領域 3 至 7 年。當一份經同儕審查的 AI 成熟度框架終於問世，AI 主題本身早已經歷兩次典範轉移。
2. **單作者偏見（Single-author bias）。** 即使優秀的方法論也繼承其主要作者的盲點。對抗式審查只在同儕審查階段發生，往往在偏見被烘焙進製品結構之後才發生。
3. **讀者被動性（Reader passivity）。** 以靜態 PDF 形式消費的方法論需要大量人類翻譯勞動才能應用到特定組織。方法論本身無法回答關於自己的問題。

與此同時，一種新的生產環境已經出現：**AI 整合開發環境（AI IDEs）**，例如 Claude Code [Anthropic 2025]、Cursor [Anysphere 2024]、Google Antigravity [Google 2025]、OpenAI Codex CLI [OpenAI 2024]。這些工具將大型語言模型（LLM）推理與檔案系統、版本控制、shell 指令原語融合，使其不再僅是程式編輯器，而成為通用的**認知基礎設施（cognitive infrastructure）**。

### 1.2 研究問題

本文探討 AI IDE 在刻意編排下，是否能作為新類別方法論製品的生產環境——我們將這類製品稱為 **AI 原生電子書（AI-Native eBook）**。具體而言：

- **RQ1。** 多 IDE 編排在方法論生產中啟用了哪些單一工具寫作無法達成的特性？
- **RQ2。** 讀者—IDE 互動如何改變方法論製品的消費方式？需要哪些設計支援？
- **RQ3。** 哪些設計原則應規範 AI 原生電子書工程？這些原則與已確立的方法論發展指南如何比較？

### 1.3 貢獻

本文做出四項貢獻：

1. **範式描述：** AI 原生電子書生產的範式，並與先前類別（AI 輔助寫作、literate programming、可執行文件）區隔。
2. **實作製品：** *GenAI Consulting Methodology Toolkit*，已準備好以 Apache 2.0 授權與待發布的 Zenodo DOI 釋出，既是一份可用的方法論，也是該範式的實證示範。
3. **設計科學評估：** 依 Hevner 等人 [2004] 的七大準則對製品進行評估，並對傳統方法論發展循環做量化對比。
4. **可重用基礎設施：** 22 個 AI-IDE workflow 規格、三個 IDE 設定目錄、與一份 `CITATION.cff` provenance 檔，其他研究者可 fork 並改編。

本文其餘安排如下：第 2 節將本工作定位於相關文獻；第 3 節描述實作製品；第 4 至 8 節闡述 AI 原生電子書生產的五項區辨特性；第 9 節呈現設計科學評估；第 10 節討論意涵。

---

## 2. 相關工作

### 2.1 方法論工程與設計科學研究

方法論的系統性建構已透過**設計科學研究（DSR）** 範式予以形式化 [Hevner et al. 2004; Peffers et al. 2007]。Hevner 的七大準則——問題相關性、設計即製品、設計評估、研究貢獻、研究嚴謹度、設計即搜尋過程、研究傳播——提供 IT 製品（包含方法論）作為學術貢獻接受評估的標準視角。

在 DSR 範疇內，方法論發展是一類被認可的製品 [March & Smith 1995]。其下知名子類別包含**成熟度模型發展**，de Bruin 等人 [2005] 與 Becker 等人 [2009] 為其闡明程序標準。本工作以 DSR 為主要評估視角（第 9 節），同時引入一項**二階（second-order）** 設計科學貢獻：研究中的製品不僅是一份方法論，更是**一份關於如何在 LLM 時代建構方法論的方法論**。

### 2.2 Literate Programming 與可執行文件

Knuth [1984] 的 **literate programming** 引入了「程式與其文件應共存於單一製品中、程式可從文件衍生」的觀念。Jupyter notebooks [Kluyver et al. 2016] 將此推廣至計算科學，讓散文、程式碼、輸出可交織。

近期 **observable notebooks** [Bostock 2017] 與**反應式文件（reactive documents）**[Victor 2011, 2014] 進一步推進：文件本身可互動，讀者操作參數並觀察重新計算的輸出。AI 原生電子書沿第三個軸線延展此軌跡：不只是**互動**文件，而是**可查詢（queryable）**文件——讀者的問題由製作該文件的同一 AI 基礎設施回答。

### 2.3 AI 輔助寫作

近年的文獻探討 LLM 輔助學術與專業寫作 [Mirowski et al. 2023; Lee et al. 2022; Long et al. 2024]。主流框架是**增強（augmentation）**：單一人類作者搭配單一 AI 助手，研究問題聚焦於創作控制、署名歸屬、AI 共同作者的感知。

我們主張此框架已不足。當生產從聊天介面移到**具有檔案系統存取權的 AI IDE** 之後，相關分析單位不再是「人—AI 二元組」，而是**多 IDE 編排（multi-IDE orchestration）**——多個專門化 AI 引擎各自貢獻獨特能力，透過檔案系統與版本控制原語協調。據我們所知，這種編排模式尚未在方法論工程脈絡中被系統性研究。

### 2.4 IDE 即媒介

Engelbart [1962] 關於**增強人類心智（augmenting human intellect）**的論文預示，計算介面不只是加速既有任務，而是**重構**人類認知工作。Victor [2014] 關於**思考的媒介（media for thought）**的工作主張，程式設計環境本身塑造可被便宜地思考的思想。

AI IDE 是此命題在前所未有規模上的全新實例化。我們延伸 Engelbart 與 Victor 的框架，主張 AI IDE 不只是**思考程式碼**的媒介，也是**思考任何可以版本化純文字表達的事物**的媒介——包含方法論、書籍、合約、課綱。

### 2.5 落差

據我們所知，先前並無工作探討：

- 將**多個專門化 AI IDE 以刻意編排方式**作為方法論生產環境的使用方式；
- 將**主動的、讀者可查詢的方法論**以持久識別符發布為學術製品；
- 使此類製品在形式學術意義上可重現的**衍生鏈（provenance chain）**（Git + workflow 檔案 + DOI）。

本文填補此落差。

---

## 3. 製品：GenAI Consulting Methodology Toolkit

### 3.1 範疇

實作製品為 **GenAI Consulting Methodology Toolkit**（以下簡稱 *Toolkit*），以 Apache License 2.0 發布。下列數值屬性**凍結於 commit `7da82d7`（2026-05-18）**，可依 `09_Research_Paper/REPRODUCIBILITY.md` 中的指令獨立驗證：

| 屬性 | 數值 | 驗證指令（見 REPRODUCIBILITY.md）|
| --- | --- | --- |
| Markdown 文件總數 | 354 | `find . -name "*.md" -not -path "./.git/*" \| wc -l` |
| 實質源文件數（排除 `_EN`/`_DE`/`_FR`/`_ES`/`_JA`/`_KR`/`_TH` 翻譯姊妹檔）| 120 | 見 REPRODUCIBILITY.md §3 |
| 翻譯姊妹檔總數（`_EN`/`_DE`/`_FR`/`_ES`/`_JA`/`_KR`/`_TH`）| 234（78/31/31/31/31/31/1）| 見 REPRODUCIBILITY.md §3 |
| 專門化 AI-IDE workflow 數 | 22（Claude Code 10、Codex 10、Antigravity 2）| `ls .claude/workflows/*.md .codex/workflows/*.md .antigravity/workflows/*.md \| wc -l` |
| 八階段方法論的階段數 | 8 | （定性；見 `00_Overview/EIGHT_STAGE_FLOW_STORY.md`）|
| 成熟度模型的層級數 | 5（L1 Chat -> L5 Agent Team）| （定性）|
| 業界案例研究（Benchmark-grade 格式）| 7 | `ls 04_Scenarios/SAMPLE_CLIENT_CASE_*.md \| wc -l` |
| Git commit 數 | 94 | `git rev-list --count HEAD` |
| 具實質涵蓋的源語言 | 7（繁體中文、English、Deutsch、Français、Español、日本語、한국어；部分泰文）| 見 REPRODUCIBILITY.md §3 |
| Repository URL | `https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit` | — |
| 授權 | Apache License 2.0（附 `NOTICE` 署名要求）| `cat LICENSE` |

### 3.2 方法論實質內容（簡述）

Toolkit 的實質方法論——不在本文範圍內，但完整記錄於 repository——包含：

- **八階段閉環顧問流程**（Stage 1 As-Is -> Stage 2 Reference Model -> Stage 3 Best Practice/Ideal Practice -> Stage 4 Gap Analysis -> Stage 5 Problem Definition -> Stage 6 Phased Goals -> Stage 7 To-Be Design -> Stage 8 Implementation），以季度性的 Stage 2 雷達回環作為可證偽機制；
- **Tiger AI L1-L5 GenAI 採用成熟度模型**，組織於兩條正交軸上（規模軸 L1-L3、AI 自主軸 L4-L5），依 Tool 2.5 成熟度模型資格計分卡自評通過 10 條件中的 9 條；
- **四層企業 AI Reference Model**（L1 Governance / L2 Business / L3 Information / L4 Technical），由「抽象 × 揮發性」軸線推導而出；
- **三階段契約模型**（Phase A Diagnostic / Phase B Strategy / Phase C Implementation），具有明確的 Gate A/B/C 退出點；
- **工具箱範本庫**（40 題訪談題庫、計分量規、Stage Gate 條件、Risk Register、Audit Log 規範、AI Ethics 檢核表）。

L1-L5 成熟度模型將作為獨立的學術貢獻於另一篇論文中呈現 [Lu, in preparation]。本文聚焦於建構整個 Toolkit 所用的**生產範式**。

### 3.3 此製品在本文中為何有趣

就本文目的而言，Toolkit 的實質方法論被視為**代表性負載（representative payload）**。新穎貢獻在於回答以下問題：*既然需要生產出此規模的製品（354 份文件，7 種語言，8 階段方法論，5 級成熟度模型，7 個案例研究），使用了何種生產環境？該環境提供了哪些傳統環境無法提供的特性？*

第 4 至 8 節從五個維度回答此問題。

---

## 4. 多 IDE 生產架構

Toolkit 透過刻意編排**三個專門化 AI IDE 家族**進行生產，各自貢獻獨特能力。編排方式編碼於三個 repository 目錄中：

```
10_Consulting/
├── .claude/         (Claude Code -- 1M context、跨檔綜合)
│   ├── README.md
│   └── workflows/   (10 個專門化 workflow)
├── .codex/          (OpenAI Codex CLI -- 工程嚴謹度、稽核)
│   └── workflows/   (10 個專門化 workflow)
└── .antigravity/    (Google Antigravity -- 多代理並行)
    └── workflows/   (2 個專門化 workflow)
```

### 4.1 依認知任務的專門化分工

不同生產任務適合不同 IDE 引擎。Toolkit 的設計讓每個引擎處理其最擅長的認知任務：

| 認知任務 | 偏好的 IDE | 原因 | 代表性 workflow |
| --- | --- | --- | --- |
| 跨檔深度綜合 | Claude Code（Opus 4.7，1M-token context）| 對整個 repository 單次推理 | `/deep-synthesize` |
| 對抗式辯論 | Claude Code（多代理 spawn）| 可生成獨立的專門化 sub-agent | `/devil-pair-debate` |
| 長時程反事實壓測 | Claude Code | 在假設體制變動下持續推理 | `/thought-experiment` |
| 工程一致性稽核 | Codex CLI | 嚴格守則，結構檢查低幻覺 | `/consistency-review` |
| Provenance / traceability 生成 | Codex CLI | 機械式擷取，低創造性容忍 | `/generate-traceability` |
| 多代理並行報告草擬 | Antigravity | 原生並行代理派發 | `/generate-report` |
| 診斷訪談模擬 | Antigravity、Claude Code | 多角色並行角色扮演 | `/diagnose`、`/simulate-engagement` |

完整列舉見附錄 A。

### 4.2 為何不使用單一 IDE

自然的反問：用單一 IDE 生產 Toolkit 不是更簡單嗎？由生產歷史得出的實證答案是**不**。三項生產挑戰驅使了多 IDE 選擇：

1. **Context window 異質。** Claude Code 的 1M-token context 讓「整個 repository 的綜合」對跨檔工作（`/deep-synthesize`、`/cross-stage-trace`）成為可行；其他 IDE 較短的 context 無法維持 354 份檔案間的一致性。
2. **對抗分離需要獨立代理。** 單一 LLM session 內的「自我辯論」是退化的——相同參數傾向收斂。為 `/devil-pair-debate` spawn 全新 Claude sub-agent，或為 `/red-team-review` 交替使用 Claude（提案者）與 Codex（稽核者），可產生真正獨立的批判。
3. **工程嚴謹度與綜合的偏誤方向不同。** 長 context 綜合引擎（依我們經驗）對敘事一致性有輕微偏好，偶爾會「平滑掉」真實的不一致。Codex 較嚴格、較保守的風格被用作矯正：`/consistency-review` 反覆標示出 Claude 已敘事跳過的結構違規。

### 4.3 編排作為宣告式規格

關鍵的方法論行動是：**編排本身即為版本化製品**。`.claude/workflows/`、`.codex/workflows/`、`.antigravity/workflows/` 目錄包含 markdown 規格，任何使用者可閱讀、fork、修改、呼叫。這使生產環境具可重現性：擁有相同 IDE 帳號的第三方可對相同的 repository 狀態重播 workflow，並觀察到類似的輸出。

我們主張這是 AI 原生電子書生產區別於 ad-hoc AI 輔助寫作的關鍵特性：**製作該製品的食譜本身是製品的一部分**，被版本化且可被引用。

---

## 5. 讀者作為查詢者的互動模型

### 5.1 超越被動閱讀

傳統方法論消費遵循線性模式：讀者（顧問、主管、研究生）打開文件、循序閱讀、嘗試心理上將其翻譯到自己的脈絡。翻譯勞動巨大且大半隱形；這正是許多優秀方法論失望感的來源。

Toolkit 顛覆此模式。生產該方法論的同一個 Claude Code、Cursor 或 Codex 環境，可被讀者用來**詢問**方法論。10 個 Claude Code workflow 中有一個子集專為讀者使用而設計：

- **`/socratic-challenge`**——方法論向讀者提出探問式問題，迫使讀者用方法論的詞彙說出自己組織的真實狀況；
- **`/theory-bridge`**——讀者描述具體情境，workflow 將其對應到方法論引用的七大學術支柱；
- **`/scenario-planning`**——給定讀者的限制條件，workflow 產出三條對比路線圖加上明確 trade-off；
- **`/cross-stage-trace`**——讀者在某一階段提出一個改動，workflow 追蹤其在 stages 4 至 8 的下游影響。

### 5.2 上手機制

實務問題隨之而來：讀者的 AI IDE 如何**理解**方法論到足以支援這些 workflow？答案是 repository 附帶兩份專為 AI 攝取設計的上手檔：

- **`AGENTS.md`**——200 行規格，向任何 AI 代理簡述方法論的結構、關鍵檔案、詞彙、紀律邊界。是任何 AI 工具的主要進入點。
- **`CLAUDE.md`**——Claude Code 專屬擴充，啟動 workflow 庫並闡明 Claude 的角色為「具跨檔綜合能力的戰略推理夥伴」。

這些檔案讓全新的 LLM session 在數秒內從通用助手轉變為「方法論識讀的對話夥伴」。經驗上這是質性差異：在 repository 根目錄打開 Claude Code session 並自動攝取 `CLAUDE.md`，第一輪即可回答相當深度的方法論問題；同一模型若無 context，只會產出通用的 AI 顧問陳腔濫調。

### 5.3 對作者—讀者關係的意涵

古典作者—讀者關係不對稱：作者廣播，讀者接收。AI 原生電子書引入第三方——讀者的 AI IDE——雙向中介此關係。讀者仍無法直接詢問作者（Morris Lu），但可以詢問一個由作者公開素材塑造、以方法論為基礎的 AI。

這引發關於作者意圖、方法論在讀者群中的漂移、以及「方法論可轉移性（transferability）」如何適當評估等有趣問題。我們於第 10 節回到這些問題。

---

## 6. 多語言一致性作為湧現特性

### 6.1 一致性挑戰

Toolkit 以七種語言發布。多語方法論的天真做法——以 A 語言寫，然後翻譯至 B 到 G 語言——累積兩項複合問題：

1. **漂移（Drift）。** 源語言的更新無法一致地傳播至譯本。
2. **不對稱權威（Asymmetric authority）。** 譯本語言的讀者遇到的術語與範例往往以源文化校準，且通常不可見。

Toolkit 的生產透過我們所稱的**同步多語一致性（simultaneous multilingual coherence）** 同時處理兩個問題：源更新與譯本更新被視為單一協調的 commit；跨語一致性由**自動化掃描強制執行**。例如，專案記憶系統紀錄如下紀律規則：

> *真實姓名移除：* `新竹` -> `City X`、`Hsinchu` -> `City X`、`신주` -> `City X`。必須在同一 commit 中跨 7 種語言檔案套用。

Commit `1dcc569`（46 個檔案修改，2026-05-17）即為此紀律的示範：一個語意變動（為避免法律風險而移除台灣真實地名與機構名）在單一 atomic commit 中傳播到 `CLIENT_JOURNEY_STORY` 的全部 7 種語言、`MANUFACTURING_CONSULTING_STORY`（zh）、加上 14 個相關檔案。

### 6.2 為何單作者生產無法達成

人類作者無法在涉及 354 份檔案、數十萬字的文件量上同時維持 7 種語言的流暢度與一致性。即使一支專業譯者團隊，也無法在多 IDE 生產所支援的時間軸上保證跨語言的語意變動 atomic 傳播（前述 commit 完成於約 45 分鐘的單一操作者 session 內）。

我們將此性質描繪為**湧現特性（emergent property）**：同步多語一致性不是生產環境中任一單一代理具備的功能，而是「LLM 流暢生成 + Git atomic commits + `/consistency-review` 式掃描 workflow」三者組合的結果。任何單一人類或單一 AI 引擎都無法產出；整體生產環境可以。

### 6.3 實證稽核

完整的跨語言涵蓋稽核（透過 `09_Research_Paper/REPRODUCIBILITY.md` §3.2 的單行 Python 腳本生成）顯示，在 120 份實質源文件（即非 IDE-meta 檔案）中：

- 31 份（26%）在五種非源目標語言（DE/FR/ES/JA/KR；通常 EN 也存在）皆完整；
- 48 份（40%）有部分姊妹檔涵蓋（DE/FR/ES/JA/KR 中的 1 至 4 種，加上多數有 EN）；
- 41 份（34%）尚無翻譯姊妹檔（低優先內部任務日誌、輔助檔案、近期新增等待首輪翻譯的文件）。

對於這個規模的單作者專案，唯有透過所述的生產範式才可能達成。

---

## 7. 對抗式品質保證

### 7.1 單次審查問題

慣例方法論審查為單次、人類進行：作者寫，同儕審查者讀一次，回應意見，製品出版。此模式留下三種未被涵蓋的失敗模式：

- **價值觀盲點（Value-system blind spots）**——審查者與作者間共享的盲點（同領域的每個人都共享相同文化預設）；
- **內部不一致（Internal inconsistencies）**——跨檔案數量超出任何單一審查者閱讀範圍的不一致；
- **反事實脆弱性（Counterfactual fragility）**——方法論在可信情境下運作，但在體制變動（如監管改變）下崩潰。

### 7.2 用 workflow 編碼的對抗式審查

Toolkit 透過對應的 workflow 處理上述每一項：

- **`/devil-pair-debate`**——Claude-A 為方法論主張辯護；Claude-B 從 Foucauldian 或 Bourdieusian 批判理論立場反駁；Claude-C 法官綜合。輸出暴露的不是 bug，而是**價值觀偏見**。例如針對 Tiger AI L1-L5 模型本身執行此 workflow，浮現出「AI 自主性是值得追求的軌跡」這個文化偶然性主張——目前已明確記於方法論的討論中。
- **`/consistency-review`**（Codex）——掃描整個 repository 的跨檔不一致（術語漂移、數值主張矛盾、損壞的交叉引用）。例如此 workflow 標示出角色職稱（具體為 `IT 副理`）與角色責任所暗示的階級不一致（解決方案：commit `1dcc569` 將該角色升級為 `IT 協理`，橫跨 17 個檔案）。
- **`/thought-experiment`**——執行反事實壓測：「若 EU AI Act 將 L4 部署刑罪化，方法論是否仍能運作？若 LLM 成本下降 1000 倍，什麼變得過時？」這些產出明確的**脆弱性地圖（fragility maps）**，是慣例審查無法生成的。
- **`/red-team-review`**（Codex 對 Claude 輸出）——使用不同 IDE 引擎稽核主要作者引擎的輸出。功能上類似於在多輪間切換同儕審查者，但具備確定性的跨引擎獨立性，而非審查者池的政治。

### 7.3 意涵：方法論硬度 vs. 審查者池規模

傳統同儕審查的硬度隨審查者數量線性增加，且受限於審查者注意力與共享盲點。AI 原生對抗式審查依 workflow 設計工作量（一次性）與運算成本（變動）擴展，並暴露人類審查者結構上無法暴露的結構盲點。兩者不互相取代；應串聯執行。但 AI 原生層改變了方法論品質的**地板（floor）**：通過 `/devil-pair-debate` 與 `/red-team-review` 的主張在類別上比僅通過人類審查的主張更難擊倒。

---

## 8. 可重現性與 Provenance

### 8.1 「AI Slop」問題

對 LLM 生成內容的常見批評是**不可證偽的 provenance**：讀者無法判斷哪些主張來自人類推理、哪些來自 LLM 補完、哪些既非前者也非後者（即幻覺）。此批評對方法論製品尤為尖銳，因為其權威性源自理論血緣與經驗基礎。

### 8.2 Toolkit 的 Provenance Chain

Toolkit 透過四層 provenance chain 處理此問題：

1. **Git 歷史**——每次改動皆有時間戳並可歸屬於 commit。截至撰文時的 94 個 commit 編碼了製品的完整衍生歷史。
2. **AI 署名紀律**——具實質 AI 協助的 commit 帶有 `Co-Authored-By:` trailer（例如 `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`）。混合署名的 commit 對這份混合性誠實。
3. **Workflow 檔案作為衍生食譜**——`.claude/workflows/`、`.codex/workflows/`、`.antigravity/workflows/` 目錄歸檔所用的精確 prompt 與程序。第三方可重播。
4. **持久識別符**——待發布的 Zenodo DOI（concept DOI + 每個 release 的 version DOI）將在 `v1.0.0` tag 發布後，為學術引用提供不可變的 handle。

### 8.3 引用紀律

Toolkit 在**內容層級**進一步強制引用紀律。所有理論主張在 `00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md` 中追溯至具體外部來源（Rosemann BPM Maturity、CMMI、APQC PCF、SCOR、TOGAF、Dragon1 EA 等）。源自 Toolkit 自身設計選擇的內部主張則被標示為內部主張，並依 Tool 2.5 的十條件計分卡自評。

此紀律處理我們認為對 AI 輔助方法論生產最深層的反對：**AI 增強的作者無法抗拒「生成聽起來合理的理論」**而非引用實際來源的誘惑。Toolkit 的紀律——編碼於 `AGENTS.md` 並由 `/evidence-audit`（Codex）強制——讓此類生成可見且可被切除。

### 8.4 形式意義上的可重現性

具備以下三項條件的讀者：

- 公開 repository 的存取權；
- Claude Code / Codex / Antigravity（或相容 AI IDE）的帳號；
- 已發布的 workflow 檔案；

原則上可從相當早期的 commit 起重新衍生方法論，觀察相同的 workflow 是否產出收斂或發散的輸出。在前 LLM 時代方法論製品（如 1990 年代的 CMMI 發展）並不具備這種**可重現性**——因為生產環境本身被發布了。

---

## 9. 評估

### 9.1 Hevner 設計科學七大準則

我們依 Hevner 等人 [2004] 的標準準則評估 AI 原生電子書範式。

| # | 準則 | 自評 | 證據 |
| --- | --- | --- | --- |
| 1 | 設計即製品 | [x] | 實作 Toolkit 為可行、完整製品（Apache 2.0、354 個檔案、待發布 Zenodo DOI）。|
| 2 | 問題相關性 | [x] | 方法論工程危機（循環延遲、單作者偏見、讀者被動性）已記錄且結構性內在。|
| 3 | 設計評估 | [!] 部分達成 | 對自有十條件計分卡自評（9/10）。對比傳統方法論循環的評估為定性（§9.2）。經驗讀者採用研究延至後續工作。|
| 4 | 研究貢獻 | [x] | 範式描述、實作製品、評估框架、可重用基礎設施——四項獨立貢獻。|
| 5 | 研究嚴謹度 | [x] | 理論視角（DSR）、評估標準（Hevner）、比較方法（循環時間與涵蓋度指標）皆明確。|
| 6 | 設計即搜尋過程 | [x] | 93 個 Git commit 記錄設計空間的反覆搜尋。|
| 7 | 研究傳播 | [x] | 兩種受眾：實務工作者（整個 repository、多語言）與學術界（本 preprint、待發布的 Zenodo DOI）。|

唯一的部分通過（準則 3）是誠實的：經驗讀者採用研究目前不在範疇內。我們於第 10 節描繪經驗研究議程。

### 9.2 比較循環分析

我們將 AI 原生電子書生產與三個參考點比較：McKinsey 7-Step 問題解決方法論的發展（如 [Rasiel 1999] 所載）；Rosemann 的 BPM Maturity Model 發展 [Rosemann & de Bruin 2005; de Bruin & Rosemann 2007]；以及一個代表性的 GenAI 成熟度框架（Gartner AI Maturity Model，2019-2024 多次改版）。

| 維度 | McKinsey 7-Step（標準）[a] | Rosemann BPM-MM（學術）[b] | Gartner AI-MM（業界）[c] | Toolkit（AI 原生）[d] |
| --- | --- | --- | --- | --- |
| 首次公開發布到 v1.0 | ~ 5 年 | ~ 3 年（PhD 週期）| 每次改版 ~ 18 個月 | **~ 6 個月** |
| v1.0 時源語言數 | 1 | 1 | 1（EN），部分後續本地化 | **7 同步** |
| v1.0 時實質文件數 | ~ 30（書）| ~ 6（論文 + 補充材料）| ~ 5（研究筆記）| **120** |
| 專門化 workflow 數 | 0 | 0 | 0 | **22** |
| 生產 provenance | 回憶錄／訪談 | 致謝段落 | 編輯團隊名單 | **完整 Git + workflow 檔案 + DOI** |
| 讀者可查詢性 | 無（靜態文字）| 無 | 無 | **22 個讀者可呼叫的 workflow** |
| 授權 | 專有 | 學術／Elsevier | 專有（付費牆）| **Apache 2.0（開放）** |

**比較表的腳註：**

**[a] McKinsey 7-Step。** 數值估計來自 Rasiel [1999] 的記載，該書記錄該方法自 1990 年代初期累積到正式出版。循環時間估計指 McKinsey 內部發展 7-step 公式的時間；文件數指 Rasiel 該書（~ 200 頁）作為主要公開製品。實質上更豐富的衍生書籍（如 Friga 2009）在首次釋出後才出現。

**[b] Rosemann BPM Maturity Model。** 數值估計來自 de Bruin 博士論文循環 [de Bruin & Rosemann 2005, 2007; de Bruin 2009]。循環時間估計對應產出標準模型的博士工作；文件數計入 v1.0 時期的公開論文（ECIS 2005、BPTrends 2005、Delphi 論文 2007），不包含後續衍生工作。

**[c] Gartner AI Maturity Model。** 數值估計來自 Gartner 已發布的研究筆記改版節奏（2019、2021、2023、2024 為實質改版；間隔年份僅有小幅更新）。循環時間估計指改版節奏，非首次發布。文件數指每次改版的研究筆記包。

**[d] Toolkit（本論文）。** 所有數字凍結於 commit `7da82d7`（2026-05-18），可依 `09_Research_Paper/REPRODUCIBILITY.md` 中的指令重現。

非 Toolkit 欄位的數值仍為來自公開來源的近似值；歡迎修正，將透過 repository Issues 接受勘誤。**定性**模式則穩固：AI 原生生產產出比比較者多一個數量級的文件、同時支援多語、且具備比較者結構上欠缺的 provenance 與讀者可查詢性。我們指出此比較是**生產範式**之間的比較，而非方法論本身實質優劣的比較。

### 9.3 限制

我們列舉三項誠實的限制：

- **幻覺風險。** 儘管有引用紀律與 `/evidence-audit`，殘存的幻覺主張可能仍存在。歡迎讀者透過 repository Issues 標示。
- **IDE 存取不對稱。** 無 Claude Code、Cursor 或同類工具的讀者無法完整運用「讀者作為查詢者」的模式。這以經濟資源層級化存取，這是我們共同的擔憂。
- **永續性。** Toolkit 的生產速率取決於對當代 LLM 的持續可負擔存取。明顯的價格上漲或能力下降將改變計算。

### 9.4 本論文不主張之事

我們明確指出本論文**不**做的三項主張：

- **不主張「已經同儕審查」。** 在 Zenodo 發布只授予持久識別符，非同儕審查。本 preprint 是為社群回饋而提供的；經同儕審查的版本是下一步。
- **不主張「已透過經驗案例研究驗證」。** Toolkit 的實質方法論（L1-L5、八階段流程）已被謹慎**建構**，但尚未透過縱貫式客戶交付經**驗證**。此驗證是另一條研究線目前正在規格設計階段的明確主題（見 repository 中 `90_References/PILOT_STUDY_PROTOCOL.md`）。
- **不主張「AI 為作者」。** 生產環境是 AI 原生，但作者責任——以及對錯誤的問責——由人類作者承擔。共同作者 trailer 承認 AI 對特定 commit 的貢獻，並不轉移作者身份。

### 9.5 計畫驗證實驗（預註冊）

為了讓本文從「立場與製品」貢獻向研究級評估推進，我們**預註冊（pre-register）** 一項小樣本讀者採用研究，將於 v1.0.0 發布後進行。下列協議現在即提供，讓審稿者在結果出現前評估方法適切性；最終結果將於 v2.0 修訂中呈現。

**假設。**

- **H1（時間）：** 使用讀者作為查詢者 workflow（`/socratic-challenge`、`/theory-bridge`、`/deep-synthesize`）回答方法論理解問題的讀者，每題所需時間將少於使用相同方法論靜態 PDF 形式的讀者。
- **H2（正確性）：** 讀者作為查詢者的答案在正確性上將相對 PDF 閱讀答案非劣（non-inferior），正確性以與方法論作者預先撰寫的評分量規一致性衡量。
- **H3（應用準備度）：** 讀者作為查詢者的參與者在 10 分鐘的後問卷應用草稿任務中，將產出比 PDF 參與者更具體、更組織專屬的應用草稿。

**設計。** 受試者內交叉（within-subject crossover），n = 6 位參與者（兩種背景各 3 位：有經驗的管理顧問；對顧問框架不熟悉的資深 IT 專業人員）。每位參與者完成兩個 session，間隔 ≥ 7 日，順序對抗平衡：Session A 使用 AI-IDE 讀者作為查詢者模型；Session B 使用相同內容的 PDF 渲染版本。每個 session 呈現相同 8 題理解題（每 session 內容隨機不同）與相同的 10 分鐘應用草稿任務。

**測量。**

- 每題作答時間（連續，自動記錄）；
- 答案正確性（5 點量規，由獨立評分者盲分）；
- 應用草稿涵蓋度（引用的方法論元素計數；品質由同一盲評分者 1-5 評分）；
- 自陳認知負荷（NASA-TLX 簡式）；
- 自陳偏好（實驗後 Likert）。

**統計計畫。** 受試者內差異採配對 t 檢定（或 Wilcoxon 符號秩檢定，若分布非常態）；三組假設家族採 Bonferroni 校正。樣本（n = 6）以調查研究標準而言為小，但對於我們使用的受試者內交叉設計為足夠；我們報告效果量與 p 值並列，並將研究視為探索性而非確認性。

**預註冊。** 完整協議、量規、問卷文字、應用草稿題目、統計計畫將於招募第一位參與者前 deposit 至 OSF（Open Science Framework）登錄，並以 Zenodo 連結的 DOI 標示。連結將於本 preprint v1.1 修訂時附於本節。

**計畫研究的限制。** 受試者內交叉設計控制了參與者間變異但引入順序效應；對抗平衡僅部分處理此問題。樣本為作者專業網路便利招募，限制了可推廣性。AI-IDE 熟悉度為一干擾變項，我們透過簡短前 session 訓練控制，但無法完全消除。

**為何在執行研究前就預註冊。** 在結果出現前預註冊承諾分析計畫，避免事後 fishing。本 preprint 的審稿者應將 §9.5 視為**可證偽承諾（falsification commitment）**：若研究執行後假設未獲支持，v2.0 修訂必須誠實報告 null 或反向發現。

---

## 10. 討論與意涵

### 10.1 對方法論工程

方法論發展的傳統成本結構一直是進入門檻。Toolkit 證明：單一個人若有紀律地使用 AI IDE，可在數月內產出過去需要機構團隊與數年才能完成的成果。意涵不是「所有方法論工程都將變成單作者」——恰恰相反，**評估**負擔仍然巨大。但**建構**階段已被民主化。

這可能對顧問業結構產生二階效應。方法論歷史上是大型事務所的準專有資產（Bain Way、McKinsey 7-Step）。AI 原生開源方法論在 Apache 2.0 授權下、附 DOI 可引用 provenance，以根本不同的基礎競爭。是否會導致方法論的**commons** 模式（類比於開源軟體）是我們在此無法解決的經驗問題；但生產的前提條件現在已具備。

### 10.2 對 HCI 與 IDE 設計

Toolkit 在新規模上構成「**IDE 即媒介**」命題的證據。Cursor、Claude Code、Antigravity、Codex 並非為方法論工程設計，其通用設計即足夠。這暗示 AI IDE 設計者三個方向：

1. **First-class 的 workflow 規格。** `.claude/workflows/`、`.codex/workflows/` 目錄慣例正成為 *de facto* 規範。形式標準化（`.ide-workflows/` 目錄？YAML schema？）將有助於可攜性。
2. **跨 IDE handoff 原語。** 目前作者在 Claude Code 與 Codex 之間手動切換。一個「在另一個 IDE 引擎 spawn 此任務並回傳結果」的原語將收緊編排。
3. **Provenance 作為內建功能。** Co-Authored-By 的 Git trailer 是可行的過渡解，但並非專為 AI provenance 設計。一個行級 AI 署名標準（類比於 `git blame`）將使 provenance 故事成熟。

### 10.3 對學術出版

Zenodo + GitHub release 模式提供「不適合傳統期刊論文形式」的製品一條立即可用的正式學術出版路徑。路徑如下：

1. Apache 2.0 授權 + `NOTICE` 署名要求；
2. GitHub-Zenodo 整合自動鑄造每個 release 的 DOI；
3. `CITATION.cff` 用於機器可讀引用元資料；
4. 在 SSRN 發布 preprint 以在社會科學與管理文獻中被發現；
5. 衍生論文投稿會議／期刊。

此 stack 不取代同儕審查，但消除「**等待**同儕審查」的成本，讓引用證據與讀者參與可以提早累積。

### 10.4 對「AI Slop」擔憂

LLM 增強內容生產的批評者常援引「AI slop」——流暢、聽起來合理、實質無錨定的內容。我們共享此擔憂。我們主張適當回應不是揚棄 AI 生產，而是強制執行 provenance 紀律：Git 歷史、workflow 檔案歸檔、引用要求、對抗式審查、DOI 持久性。「AI slop」與「AI 原生學術」的差別正是紀律本身。Toolkit 的生產作為此紀律實務樣貌的一個示範被提供。

### 10.5 經驗研究議程

我們以本論文未回答、希望在後續工作處理的三個經驗問題作結：

- **讀者採用研究。** 讀者作為查詢者模型是否可衡量地減少方法論消費與組織應用之間的翻譯勞動？
- **跨作者複製。** 若不同作者、具不同盲點，在相同領域（GenAI 採用）產出競爭的 AI 原生方法論，製品在涵蓋度、內部一致性、讀者採用上將如何比較？
- **縱貫式方法論演化。** 24 個月內，當 LLM 能力與 IDE 功能演進時，製品如何改變？workflow 檔案手法是否優雅地老化，或變得過時？

---

## 11. 結論

AI 原生電子書生產——以 GenAI Consulting Methodology Toolkit 為例——代表方法論製品如何被建構、出版、消費的有意義轉變。四項區辨特性——多 IDE 編排、讀者作為查詢者互動、同步多語一致性、完整 provenance——共同將方法論工程成本結構改變了一個數量級，同時改善（而非減弱）製品的可稽核性。

此範式並非無限制，且若干問題——特別圍繞經驗讀者採用與跨作者複製——仍未解決。我們邀請研究社群與此製品互動、以 Apache 2.0 授權 fork、並將此範式延伸到新的方法論領域。

Repository、本 preprint、workflow 規格、`CITATION.cff` 檔案皆開放可用。引用資訊位於 front matter。

---

## 致謝

作者感謝 Queensland University of Technology 的 Prof. Michael Rosemann 對 Business Process Management 學派的長期智識影響——Toolkit 的成熟度模型方法即源自此血緣。方法論為作者個人責任；所有錯誤、遺漏、向 AI 領域的延伸應用均不代表 Prof. Rosemann 或 QUT 的觀點。

我們致謝生產 Toolkit 與本論文所使用的 AI 引擎：Anthropic Claude（Opus 4.6、4.7）、OpenAI Codex CLI、Google Antigravity。AI 對特定 commit 的貢獻已透過 Git 歷史中的 `Co-Authored-By:` trailer 記錄。

---

## 參考文獻

> 本中文版保留英文書目資訊；學術引用應使用英文原始書目以利國際對照。

APQC. (2024). *Process Classification Framework, Version 7.3*. APQC.

Becker, J., Knackstedt, R., & Pöppelbuß, J. (2009). Developing maturity models for IT management. *Business & Information Systems Engineering*, 1(3), 213-222.

Bostock, M. (2017). Observable: A new way to think with code. *Observable Inc. technical note.*

de Bruin, T., & Rosemann, M. (2005). Towards a Business Process Management Maturity Model. In *Proceedings of the 13th European Conference on Information Systems (ECIS 2005)*.

de Bruin, T., & Rosemann, M. (2007). Using the Delphi technique to identify BPM capability areas. In *Proceedings of the 18th Australasian Conference on Information Systems*.

Engelbart, D. C. (1962). *Augmenting Human Intellect: A Conceptual Framework*. Stanford Research Institute, Summary Report AFOSR-3223.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75-105.

Kluyver, T., Ragan-Kelley, B., Pérez, F., et al. (2016). Jupyter Notebooks -- a publishing format for reproducible computational workflows. In *Positioning and Power in Academic Publishing: Players, Agents and Agendas*, IOS Press, 87-90.

Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.

Lee, M., Liang, P., & Yang, Q. (2022). CoAuthor: Designing a human-AI collaborative writing dataset for exploring language model capabilities. In *Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems*.

Long, T., et al. (2024). Not just novelty: A longitudinal study on utility and customization of an AI workflow. In *Proceedings of CHI 2024*.

Lu, M. (in preparation). *L1-L5: A Generative AI Adoption Maturity Model for Enterprises.*

March, S. T., & Smith, G. F. (1995). Design and natural science research on information technology. *Decision Support Systems*, 15(4), 251-266.

Mirowski, P., Mathewson, K. W., Pittman, J., & Evans, R. (2023). Co-writing screenplays and theatre scripts with language models. In *Proceedings of CHI 2023*.

Paulk, M. C., Curtis, B., Chrissis, M. B., & Weber, C. V. (1993). *Capability Maturity Model for Software, Version 1.1*. Carnegie Mellon University, Software Engineering Institute (CMU/SEI-93-TR-024).

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3), 45-77.

Rasiel, E. M. (1999). *The McKinsey Way*. McGraw-Hill.

Rosemann, M., & de Bruin, T. (2005). Application of a Holistic Model for Determining BPM Maturity. *BPTrends*, February 2005.

Victor, B. (2011). Explorable Explanations. *Personal essay*, <http://worrydream.com/ExplorableExplanations/>.

Victor, B. (2014). Seeing Spaces. *Talk delivered at SAP Future of Programming workshop*.

---

## 附錄 A —— Workflow 列表

Toolkit 的生產環境編碼 22 個專門化 workflow，橫跨三個 IDE 家族。每個 workflow 為一份對應 IDE 可閱讀與執行的 markdown 規格。

### A.1 Claude Code workflows（`.claude/workflows/`）

| Workflow | 用途 | 生產用途 |
| --- | --- | --- |
| `/deep-synthesize` | 多檔深度綜合（1M context）| 跨階段一致性草擬 |
| `/theory-bridge` | 映射客戶情境與 7 大學術支柱 | 新讀者上手 |
| `/scenario-planning` | 3 條對比路線圖加 tradeoff | 情境庫生成 |
| `/socratic-challenge` | 探問式問題磨利讀者思考 | 讀者對話模式 |
| `/cross-stage-trace` | 單一變動的下游影響 | 變動傳播分析 |
| `/simulate-engagement` | 完整 6 週顧問案模擬 | 銷售 demo、訓練素材 |
| `/parallel-perspectives` | 6 個利害關係人並行視角 | 利害關係人地圖生成 |
| `/thought-experiment` | 反事實壓測 | 脆弱性地圖生成 |
| `/devil-pair-debate` | 兩個 Claude 對辯，第三方裁判 | 價值觀偏見浮現 |
| `/methodology-fork` | 客戶特化方法論分叉 | 客製部署 scaffold |

### A.2 Codex workflows（`.codex/workflows/`）

| Workflow | 用途 | 生產用途 |
| --- | --- | --- |
| `/academic-upgrade` | 將實務散文轉為學術 register | 本 preprint |
| `/bump-version` | 跨檔案的版本協調升版 | Release 管理 |
| `/consistency-review` | 跨檔一致性稽核 | Pre-commit gate |
| `/diagnose` | 子區域工程診斷 | 品質分類 |
| `/evidence-audit` | 驗證每個主張都有引用 | 幻覺防護 |
| `/generate-report` | 機械式報告組裝 | 交付物生成 |
| `/generate-traceability` | 建立追溯矩陣 | Provenance 支援 |
| `/harvest-insights` | 從原始筆記精煉洞察 | 筆記轉發表 pipeline |
| `/methodology-test` | 將方法論套用到合成情境 | 自我驗證 |
| `/red-team-review` | 對作者輸出進行對抗式審查 | QA gate |

### A.3 Antigravity workflows（`.antigravity/workflows/`）

| Workflow | 用途 | 生產用途 |
| --- | --- | --- |
| `/diagnose` | 多代理診斷 | 並行角色扮演訪談 |
| `/generate-report` | 多代理報告草擬 | 並行交付物生產 |

---

## 附錄 B —— 可重現性 Manifest

從任一較早 commit 重新衍生 Toolkit 的實質子集：

1. Clone repository：`git clone https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit.git`
2. Checkout 指定 commit：`git checkout <commit-hash>`
3. 在 Claude Code（或相容 AI IDE）中打開 repository。
4. 呼叫 workflow，例如：`/deep-synthesize "Re-derive Stage 4 Gap Analysis from Stage 2 and Stage 3"`。
5. 將 workflow 輸出與該 commit 對應的實際 Stage 4 文件比較。

對於實質結構內容預期會收斂；對於風格選擇與精確字句預期會發散。

---

*本 preprint v1.0 中文版結束。作者歡迎來信、勘誤、複製嘗試，聯絡方式見上方 email 與 repository。*
