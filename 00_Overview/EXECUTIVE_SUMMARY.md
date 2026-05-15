# 執行摘要：5 分鐘看懂這套方法論（10 分鐘掌握全貌）

> 🌐 English: [EXECUTIVE_SUMMARY_EN.md](EXECUTIVE_SUMMARY_EN.md)
>
> **5 分鐘版**：讀 §1 「一頁懂」 + §2 「核心模型」 就夠。
> **10 分鐘版**：再加 §3-§7（活書、理論、課程、顧問、交付物、共讀、下一步）。
> 想深入再點開各區塊指向的檔案。

---

## 1. 一頁懂：它解決什麼

很多企業導入 AI 是「**直接跳工具**」 —— 買 ChatGPT、試 n8n、想做 Agent。結果：員工不會用、流程沒接上、資料沒治理、PoC 無法驗收、高層不知道公司 AI 到底成熟到哪。

這套方法論把「**零散的 AI 使用**」變成「**可複製、可治理、可衡量、可擴大的組織能力**」 —— 用一套**問卷 + 課程 + 顧問**的閉環，從**個人會用 AI** 一路走到**企業擁有 AI 團隊**。

| 元素 | 一句話 |
|---|---|
| **診斷工具** | 10 / 25 / 50 題問卷 → L1-L5 客觀落點 + 六大構面缺口 |
| **教育路徑** | 5 級課程（OpenWebUI / Antigravity / n8n / Hermes / ClawTeam）+ BARS 評分校準 |
| **顧問結構** | 8 階段（Awareness → Acceptance Test）+ 3 階段合約（A 診斷 / B 策略 / C 落地）|
| **學術根基** | 7 大理論支柱（Rosemann / Cohen & Levinthal / Teece / Real Options / 等）|
| **承載媒介** | **AI-Native Living Book** —— 真正「活」的方法論，可直接用 AI IDE 共讀 |

---

## 2. 核心模型：L1-L5 兩條軸

L1-L5 不是「五個工具」，是**兩條軸**接起來的成熟度路徑：

| 軸 | 範圍 | 主控者 | 層級 | 工具 |
|---|---|---|---|---|
| **規模軸** | L1 → L2 → L3 | **人**用 AI、**人**監督 AI | 個人 → 部門 → 跨部門/全公司 | OpenWebUI / Antigravity / n8n |
| **AI 自主軸** | L4 → L5 | **AI** 自主營運，人退為**治理者** | AI 個體 → AI 團隊 | Hermes Agent / ClawTeam |

**關鍵分界 = L3 → L4**：從「人驅動工作」跨到「AI 驅動工作」。即使到 L4-L5，**治理框架仍由人建立、人保有監督權**；AI 自主的是「營運執行」，不是「治理決策」。

➜ 完整故事：[`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0

---

## 3. AI-Native Living Book —— 為什麼這本書「活」起來

這份方法論不是 PDF / PPT / SOP，**它是一本真正『活』的書**：

| 世代 | 形式 | 限制 |
|---|---|---|
| 第 1 代 印刷書 | 紙本 | **靜止** —— 只能讀，不會回應 |
| 第 2 代 互動書 | 網頁 / Wiki | **介面活了，內容沒活** —— 仍不會主動建議 |
| **第 3 代 AI-Native Book**（本 repo）| Markdown + AI IDE | **真正活起來** —— 讓你問、幫你答、陪你想，依你公司情境跑診斷、寫報告、做模擬 |

**操作模型**：`git clone` → 用 AI IDE（Antigravity / Claude Code / Codex）打開 → AI 自動讀完整本書 → 把自己定位成**這套方法論的共讀導師** → 你直接對話、提問、套用。

➜ 完整論述：[`AI_NATIVE_LIVING_BOOK.md`](AI_NATIVE_LIVING_BOOK.md)

### 三個 AI 引擎，各自擅長不同的事

| 引擎 | 角色 | 它最擅長的事 | 工作流 |
|---|---|---|---|
| 🟦 **Antigravity** | 前線顧問 | 跟客戶對話、跑問卷、產報告草稿 | `/diagnose`、`/generate-report` |
| 🟪 **Codex CLI** | 方法論稽核員 | 跨檔測試、紅隊演練、版控、修補 | `/evidence-audit`、`/red-team-review`、`/bump-version` 等 10 個 |
| 🟨 **Claude Code** | 跨檔思考夥伴 | 深度綜合、多視角辯論、模擬、客戶分叉 | `/simulate-engagement`、`/devil-pair-debate`、`/methodology-fork` 等 10 個 |

➜ 三引擎共筆自述：[`../07_AI_Contributions/`](../07_AI_Contributions/) ｜ 安裝指南：根 [`../README.md`](../README.md) §🚀

---

## 4. 學術理論基礎：7 大理論支柱

不是憑感覺寫出來的方法論。每個關鍵設計**都對應一個經典理論**，學術審稿、監管、董事會質疑「理論依據是什麼」時的標準答案：

| # | 理論 | 創立者 | 在本方法論的角色 |
|---|---|---|---|
| 1 | **Capability Maturity** | Rosemann (QUT) / CMMI | L1-L5 五層成熟度的學派根基 |
| 2 | **Absorptive Capacity** | Cohen & Levinthal (1990) | 解釋為什麼有些公司導入 AI 永遠停在 L1 —— 缺 prior knowledge |
| 3 | **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | Stage 7 To-Be 設計：哪些任務該到 L4、哪些該停在 L2 |
| 4 | **Dynamic Capabilities** | Teece (1997, 2007) | sense / seize / transform —— 為什麼 AI 治理是「能力」不是「制度」 |
| 5 | **Sociotechnical Systems & Trust in AI** | Bostrom (1977) / Dietvorst (2015) / Glikson (2020) | 為什麼 L4-L5 必須保留 HITL —— 人不會盲信純自動 AI |
| 6 | **Real Options Theory** | Dixit & Pindyck (1994) / McGrath (1997) | 為什麼 Phase 1 看似 NPV ≈ 0 仍值得投 —— 買的是未來擴張的選擇權 |
| 7 | **Executable Knowledge Artifact** | Knuth (1984) Literate Programming + 當代延伸 | 為什麼這份方法論是 Markdown + AI IDE 共讀，而不是 PDF |

➜ 完整理論論述（含引用）：[`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](ACADEMIC_THEORETICAL_FOUNDATIONS.md)
➜ 失敗模式（理論預測哪些情境會失敗）：[`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md)
➜ Pilot Study 設計（18-24 個月實證計畫）：[`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md)

---

## 5. 課程教育：L1-L5 五級完整課綱

每一級都有**獨立教材 + 可驗收交付物 + 階段驗收關卡（Stage Gate）**：

| 級 | 名稱 | 工具 | 對應課綱 |
|---|---|---|---|
| L1 | Controlled AI Access | OpenWebUI | [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) |
| L3 | Workflow Automation | n8n + Tiger AI Skill Pack | [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) |
| L4 | Autonomous Agent | Hermes Agent + Wiki | [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) |
| L5 | Multi-Agent Organization | ClawTeam | （L5 含於 [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)）|

**設計原則**：客戶不一定要一次上滿 L1-L5。先依問卷診斷找出**最能立即產出交付成果的層**，往上銜接。課程比例由公司屬性、產業、部署模式（雲 / Hybrid / 全地端）、風險要求綜合決定。

➜ 完整課綱組合：[`../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
➜ 評分校準（避免主觀）：[`../01_Assessment/BARS_RUBRICS.md`](../01_Assessment/BARS_RUBRICS.md) BARS 行為錨點

---

## 6. 顧問方案：8 階段 + 3 階段合約模型

### 6.1 八階段流程

| # | 階段 | 主要動作 |
|---|---|---|
| 1 | **Awareness** | 客戶建立 AI 認知與目標願景 |
| 2 | **Reference Model** | 引導客戶簽署 Ideal Practice 雷達 |
| 3 | **Discovery** | 蒐集 As-Is 現況、影子 IT、系統盤點 |
| 4 | **Gap Analysis** | 對比 Ideal Practice vs As-Is，找高影響差距 |
| 5 | **Stakeholder Mapping** | 找 Sponsor、AI Champion、HR、法遵 |
| 6 | **Diagnosis** | 跨層分析（含 7 大理論落點）|
| 7 | **To-Be Design** | 用 TTF / Real Options 設計階梯式 Roadmap |
| 8 | **Acceptance Test** | Stage Gate 驗收 + 季度雷達回看 |

### 6.2 三階段合約

| 階段 | 期程 | 主交付 |
|---|---|---|
| **Phase A 診斷** | 2 週 | 中期診斷報告 + Ideal Practice 簽署表 |
| **Phase B 策略** | 4 週 | 完整 14 章顧問報告 + 24 個月 Roadmap + ROI + 治理建議 |
| **Phase C 落地** | 24 個月 | 階段性實作 + 季度雷達回看 + 持續演化 |

➜ 完整 8 階段故事（含對話範例）：[`EIGHT_STAGE_FLOW_STORY.md`](EIGHT_STAGE_FLOW_STORY.md)
➜ 顧問報告模板：[`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)
➜ 顧問工具包模板：[`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md)
➜ 交付包與驗收：[`../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)

---

## 7. 可驗證交付物：每一級留下什麼

每一級的「課」都不只是上完就忘 —— 都會留下可被第三方稽核的證據：

| 級 | 主要交付物 | Evidence |
|---|---|---|
| L1 | 個人聊天區、Prompt Library | 帳號表、權限表、登入紀錄、Prompt 範例 |
| L2 | Skill Library、Agentic artifacts | Skill 文件、測試案例、版本紀錄、輸出範例 |
| L3 | n8n Workflow PoC、Sub-workflow Library、Data Tables | 執行紀錄、失敗重跑紀錄、系統串接截圖 |
| L4 | 可驗證 Agent、Briefing、任務卡 | Agent log、Wiki 版本、HITL 簽核紀錄 |
| L5 | Agent Team 角色卡、協作流程、跨部門成果 | Team run log、交接紀錄、治理紀錄 |
| **顧問層** | 14 章診斷報告、30/60/90 天 Roadmap、ROI、治理建議 | Stage Gate 驗收紀錄、季度雷達回看 |

➜ 完整交付物 + Evidence 矩陣：[`../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)

---

## 8. 怎麼用這本書（依角色 5 條入門路徑）

| 您是 | 從這份開始（20 分鐘 → 1 小時）|
|---|---|
| **CEO / 老闆 / 想懂方法論的家人** | [`CLIENT_JOURNEY_STORY.md`](CLIENT_JOURNEY_STORY.md) — 阿明的故事 |
| **顧問 / 學員** | [`EIGHT_STAGE_FLOW_STORY.md`](EIGHT_STAGE_FLOW_STORY.md) — 完整 8 階段流程 |
| **董事會 / 監管者 / 學術** | [`METHODOLOGY_SCIENTIFIC_LOGIC.md`](METHODOLOGY_SCIENTIFIC_LOGIC.md) — 科學論證 |
| **大企業 IT / 跳槽顧問** | [`INDUSTRY_FRAMEWORK_ALIGNMENT.md`](INDUSTRY_FRAMEWORK_ALIGNMENT.md) — 對齊 McKinsey/BCG/TOGAF/Gartner |
| **方法論研究者 / AI Pedagogy 學者** | [`AI_NATIVE_LIVING_BOOK.md`](AI_NATIVE_LIVING_BOOK.md) — 為什麼這是新型態方法論 |

---

## 9. 參考資料快速指引

### 9.1 學術理論與失敗模式

- [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](ACADEMIC_THEORETICAL_FOUNDATIONS.md) — 7 大理論支柱完整論述
- [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) — 14 個失敗模式（理論預測）
- [`../90_References/AI_GOVERNANCE_ALIGNMENT.md`](../90_References/AI_GOVERNANCE_ALIGNMENT.md) — 對齊 NIST AI RMF / EU AI Act / ISO 42001
- [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) — 18-24 個月實證研究計畫

### 9.2 教學與評估

- [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) — 10/25/50 題問卷（白話版）
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL.md) — 評分模型
- [`../01_Assessment/BARS_RUBRICS.md`](../01_Assessment/BARS_RUBRICS.md) — BARS 評分校準（避免主觀）
- [`../02_Course_Design/`](../02_Course_Design/) — L1-L5 完整課綱

### 9.3 顧問交付

- [`../03_Consulting_Report/`](../03_Consulting_Report/) — 顧問報告 + 工具包模板
- [`../04_Scenarios/`](../04_Scenarios/) — 7 大產業情境案例（製造 / 醫院 / 行銷 / B2B / 金融 / 政府 / 教育）
- [`../05_Sales/`](../05_Sales/) — 銷售話術 + FAQ
- [`../06_Delivery/`](../06_Delivery/) — 交付包 + 驗收標準 + Engagement Lifecycle

### 9.4 三引擎自述

- [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) — 三引擎共筆 README + §3 共筆紀律
- [`../07_AI_Contributions/ANTIGRAVITY.md`](../07_AI_Contributions/ANTIGRAVITY.md) ｜ [`CODEX.md`](../07_AI_Contributions/CODEX.md) ｜ [`CLAUDE_CODE.md`](../07_AI_Contributions/CLAUDE_CODE.md)
- [`../CHANGELOG.md`](../CHANGELOG.md) — 三引擎共筆變更紀錄

### 9.5 原始素材

- [`../90_References/@AI-MD-PUBIC.pdf`](../90_References/@AI-MD-PUBIC.pdf) — 原始 PDF 方法論
- [`../90_References/MD-Map.png`](../90_References/MD-Map.png) — AI 成熟度地圖
- [`../90_References/Metholodgy.png`](../90_References/Metholodgy.png) — 八階段轉型指南圖
- [`../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) — 影片學習紀錄
- [`../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

---

## 10. 下一步：3 條建議路徑

| 你的需求 | 建議下一步 |
|---|---|
| **建立整體心智圖** | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)（含 §3.0 兩條軸完整故事）|
| **想知道你公司在哪一級** | [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) 的 10 題快速診斷 |
| **想直接用 AI 共讀本書** | 用 AI IDE 打開本 repo → 先讀根 [`../README.md`](../README.md) §🚀 三引擎安裝指南，挑一個引擎啟動 |

---

> ⚠️ **學術誠信聲明**：本 repo 中所有具名案例（製造 / 醫院 / 行銷 / B2B / 金融 / 政府 / 教育 7 個 SAMPLE_CLIENT_CASE）與所有故事主角（如「阿明」「明強封測」），皆為 **AI 模擬產生的虛構案例**。所有數字（時間、ROI、人月、預算、KPI）僅為**示例**，**不可作為對外宣傳、合約承諾、學術 empirical evidence**。真實 longitudinal cases 需透過 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) 18-24 個月實證研究完成後才會替換。
>
> **架構歸屬**：本 repo 整體方法論架構由人類作者 **Morris Lu 盧業興（Tiger AI 虎智科技）** 提出。三個 AI 引擎（Antigravity / Codex / Claude Code）為**執行 / 完善 / 展開 / 稽核**工具。詳見 [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0。
