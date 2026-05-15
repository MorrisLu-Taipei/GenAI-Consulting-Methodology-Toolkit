# 範例客戶案例：教育機構 / Sample Client Case: Education Institution

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **本案例為示範用途，客戶以代號 "科技大學 E" 表示（非真實機構名）。內容綜合自多個真實教育客戶之挑戰與解法，數字為示範值。**
> Sample case for illustration. Client referred to by the code "University E" (not a real institution name).

---

## 0. Benchmark-grade Summary（Tool 3.5 九欄位）

> **此案例符合 Tool 3.5 Cases-as-Benchmarks 紀律** ── 客戶可拿此表 30 分鐘自助算差距。

| # | 必填欄位 | 本案例 |
| --- | --- | --- |
| 1 | 產業 + 規模 | 教育（科技大學），600 教職員 / 8,000 學生 |
| 2 | 起點 L-level + 證據 | L1 部分 + APQC 11.x = 2（學術知識本就豐厚） |
| 3 | 終點 L-level + 證據 | L3 + APQC 11.x = 3 |
| 4 | 跨越期間 | 12 個月 |
| 5 | 跨越的 RM Category | APQC 11.0 Knowledge、Tiger AI L1-L3 |
| 6 | 每階段投入 | 估 NT$ 400-600 萬 / 20-25 人月 |
| 7 | Key wins（可量化） | 教師備課 -40%、招生 FAQ、學術倫理檢核 Workflow |
| 8 | Key failures（踩過的雷） | 若忽略學術倫理紅線、若教師抗拒 AI 評分 |
| 9 | 適用條件 | 5,000+ 學生規模、有 IT 中心、能處理 FERPA / 個資法 |

**部署模式 / 代號**：Hybrid（學術倫理 + 校務資料地端） ／ 代號 科技大學 E


**Evidence Level**：🔵 **L0 — AI-Simulated Teaching Case**（AI 模擬教學案例，在 Tool 8.9 Evidence Hierarchy 之下）

> ⚠️ **本案例由 AI 模擬產生，並非真實客戶資料**。
>
> - **目的**：作為教學示範、方法論講解、Stage 1-8 工具表套用練習用
> - **來源**：AI 依據產業常識 + 方法論架構合成出符合 Tool 3.5 九欄位 Benchmark-grade 格式的虛構案例
> - **所有數字**（時間 / ROI / 投入人月 / 預算 / KPI）**僅為示例**，**不可**作為：
>   - 對外客戶宣傳依據
>   - 顧問合約 ROI 承諾
>   - 學術引用之 empirical evidence
>   - 對任何單一真實公司的對比結論
>
> 證據等級依 Tool 8.9 Evidence Hierarchy：L1 自評 · L2 文件 · L3 系統 log · L4 第三方稽核 · L5 縱貫 KPI ── **本案例屬 L0（pre-evidence）**，低於 L1。
>
> **真實 longitudinal 案例**需透過 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) 18-24 個月實證研究完成後才會替換。在此之前，請以**AI 模擬教學案例**對待本檔內容。

> 詳細案例細節見下方各章節。本表為 [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 3.5 規範的標準摘要。

---


## 1. 客戶背景 / Client Profile

| 欄位 | 內容 |
| --- | --- |
| 機構代號 / Client code | 科技大學 E / University E（私立科技大學，匿名） |
| 性質 | 私立科技大學 |
| 規模 | 教職員 600 人（教師 380 / 行政 220）、學生 8,000 人 |
| 起始 L 級 | L1 |
| 預算 | NT$ 600 萬（18 個月） |
| 規範 | 個資法（學生資料）、教育部規範、學術倫理 |
| 主要痛點 | (1) 教師備課 / 批改負擔重 (2) 招生諮詢重複問答多 (3) 系所評鑑文件整理耗時 (4) 行政流程紙本多 |

## 2. 顧問接觸與診斷

### 2.1 10 題快速問卷結果

均分 **1.0 → L1**。工具使用 Q1=2（教師個人用 ChatGPT），治理 Q6=0、流程 Q3=1。

### 2.2 25 題六構面

| 構面 | 均分 |
| --- | ---: |
| 工具使用 | 2.4（教師接受度高） |
| 知識沉澱 | 1.2 |
| 流程標準化 | 1.5 |
| 系統整合 | 0.8 |
| Agent 應用 | 0.4 |
| 治理 ROI | 0.6 |

**洞察**：教師個人使用率高（接受度好），但組織無治理、無沉澱。教育機構導入特性 — 教師抗拒與支持兩極，需以「減負」破冰；學生個資保護是紅線。

### 2.3 公司屬性 Bundle 重點

```json
{
  "profile": {"industry":"education","headcount_bucket":"300-1000"},
  "systems": {"lms":"Moodle","wiki":["Google Drive"],"sis":"自建學籍系統","email":"Google Workspace for Education"},
  "risk": {"sensitive_data":["學生PII","成績","健康"],"regulations":["個資法","教育部規範","學術倫理"],"llm_retention_acceptance":"30天可接受"},
  "deployment": {"preference":"Hybrid","gpu_capacity":"4090級","local_llm_plan":"評估中"},
  "course": {"l1_headcount":600,"seed_team_headcount":20,"objectives":["全員啟用","流程自動化"]},
  "budget": {"annual_bucket":"500K-2M","kickoff":"1-3個月"}
}
```

## 3. 課程比例建議

| Level | 比例 | 重點 |
| ---: | ---: | --- |
| L1 | 35% | 全員啟用；教師 + 行政分軌；學生個資紅線；學術倫理規範 |
| L2 | 30% | 教師教學 Skill + 行政 Skill |
| L3 | 25% | 招生 FAQ、評鑑文件、行政流程 Workflow |
| L4 | 8% | 課程搜尋推薦 Agent |
| L5 | 2% | 概念說明 |

理由：教師接受度高，L1 可較快；重點在 L2 教學 Skill（最大減負槓桿）+ L3 行政自動化。

## 4. 課中產出資產

### L1 OpenWebUI (6 週)

- 600 教職員帳號（教師軌 / 行政軌分課程）
- **Hybrid 部署**：公開教學資料走雲；學生個資 / 成績走地端（4090 機）
- AI 使用規範：學生個資絕對不可進雲 LLM；學術倫理（AI 輔助 vs AI 代寫之界線）
- Prompt Library 32 條（教學設計、行政公文、招生回覆）
- 學生端另有獨立規範（學生使用 AI 之學術誠信指引）

### L2 Knowledge Codification (8 週)

12 個 Skill：

| # | Skill | Owner |
| --- | --- | --- |
| 1 | 教案 / 課程大綱草擬 | 教師 |
| 2 | 作業回饋摘要（formative） | 教師 |
| 3 | 評量題目產生（含 rubric） | 教師 |
| 4 | 投影片大綱與講稿草擬 | 教師 |
| 5 | 課程錄影自動字幕 + 摘要 | 教學發展中心 |
| 6 | 招生 FAQ 回覆草稿 | 招生組 |
| 7 | 家長 / 學生溝通信草擬 | 導師 / 行政 |
| 8 | 系所評鑑文件匯整 | 系所助理 |
| 9 | 行政公文草擬 | 行政各處 |
| 10 | 會議紀錄與決議追蹤 | 秘書室 |
| 11 | 學生輔導紀錄結構化 | 學務 / 諮輔（嚴格權限） |
| 12 | 研究計畫摘要與格式檢查 | 研發處 |

### L3 n8n Workflow (6 週)

4 個 Workflow PoC：

1. **招生 FAQ 自動回覆** — 招生信箱 / 表單 → Skill #6 → 招生組 review → 發送
2. **評鑑文件匯整 Pipeline** — 評鑑項目 → RAG over Drive → Skill #8 → 系所助理 review
3. **課程錄影處理** — 錄影上傳 → Whisper → Skill #5 → Moodle 字幕 + 摘要
4. **行政公文流程** — 公文進線 → Skill #9 → 承辦 review

### L4 Hermes Agent (4 週)

**課程搜尋推薦 Agent**：
- Wiki：全校課程資料、選課規則、學程地圖、職涯對應
- Skills：課程搜尋、學程說明
- 任務卡：學生問「我想往 X 方向發展該選什麼課」→ Agent 給課程組合 + 學程路徑 + 理由
- Reviewer：教務處 / 系主任
- Gate 4A-4E 通過
- **學生個資不進此 Agent**（僅課程資料）

### L5 ClawTeam

僅概念說明。

## 5. 八階段顧問分析

### Stage 1 現況掌握
- 訪談：校長、教務長、學務長、3 系主任、教學發展中心、招生組、資訊中心
- 痛點密度：備課 / 批改（教師 95%）、招生問答（招生組 100%）、評鑑（系所 90%）

### Stage 2 標準模型引入
- 校長願景：18 個月內教師行政負擔 -30%、招生諮詢回應 < 1 天、評鑑文件準備時間減半
- Sponsor = 教務長 + 資訊中心主任

### Stage 3 產業最佳實務對標
- 國際：ASU（亞利桑那州立）AI 應用、可汗學院 Khanmigo（願景參考）
- 採 Hybrid，對標個資法 + 學術倫理規範

### Stage 4 差距分析

Missing/Broken/Redundant：
- **Missing**：AI 治理規範、學術倫理 AI 指引、Skill Library、學生個資邊界
- **Broken**：評鑑文件每次重新人工整理（系所每次評鑑 200+ 工時）
- **Redundant**：招生問答 60% 為重複問題；各系所各自的課程介紹

Impact × Effort：
- Quick Win：招生 FAQ（L3-W1）；教案草擬 Skill（L2-#1）
- Big Bet：評鑑文件 Pipeline（L3-W2）
- Avoid：AI 直接批改給成績（學術風險高，僅輔助）

### Stage 5 結論與核心問題定義

```
CONTEXT: 少子化下招生競爭激烈；教育部評鑑頻繁；教師流失率上升（行政負擔為主因之一）。
TENSION: 教師個人 AI 接受度高 (L1+) 但組織零治理零沉澱；學生個資保護壓力大。
COI: 不行動 18 個月：(1) 教師流失加劇 (2) 招生轉換落後同校 (3) 評鑑準備持續耗損系所人力。
DESIRED: 18 個月達 L3-L4；教師行政負擔 -30%；招生回應 < 1 天；評鑑準備 -50%。
CONSTRAINT: 預算 600 萬；學生個資走地端；學術倫理界線明確；教師抗拒需處理。
```

### Stage 6 標竿對照與多階段目標設定

| Phase | 月 | 主要交付 | Gate | KPI |
| --- | --- | --- | --- | --- |
| 1 | 1-3 | L1 全員 + 治理 + 學術倫理指引 | Gate 1 | 教師週使用 ≥ 60% |
| 2 | 4-9 | L2 12 Skills | Gate 2 | Skill Library ≥ 12 |
| 3 | 10-14 | L3 4 Workflows | Gate 3 | 招生回應 < 1 天 |
| 4 | 15-18 | L4 課程推薦 Agent | Gate 4 | 學生使用率 ≥ 30% |

### Stage 7 未來藍圖設計

- **Variant B Hybrid**：
  - 公開教學資料 → 雲（Claude / Gemini for Education）
  - 學生個資 / 成績 / 輔導紀錄 → 地端（4090 + Llama 8B/70B）
- Moodle LMS 串接；Google Workspace 串接

### Stage 8 執行導入與變革治理

- Permission：教師 / 行政 / 諮輔 / 資訊 分層；學生資料嚴格 ACL
- 學術倫理：教師端「AI 輔助」指引 + 學生端「學術誠信」指引
- Audit：所有 LLM call 1 年；學生資料相關 3 年
- ROI Tracker：教師行政時間、招生回應時間、評鑑準備工時、Skill 使用率

## 6. 診斷報告摘要

> **核心發現**：科技大學 E 教師個人 AI 接受度高（L1+）但組織零治理零沉澱。教育機構導入特性 — 以「教師減負」破冰最有效，學生個資是不可踩的紅線。建議 18 個月達 L3-L4。
>
> **預期 ROI**：18 個月可量化效益 NT$ 2,400 萬，ROI ≈ 300%。

## 7. 30/60/90 天 Roadmap

### 30 天
- L1 OpenWebUI 600 帳號（教師軌先行）
- AI 使用規範 + 學術倫理指引草案
- 4090 地端機建置（學生個資用）

### 60 天
- L1 行政軌上線
- 學術倫理指引校務會議通過
- 5 個 quick-win Skill 上架（#1 #3 #6 #9 #10）

### 90 天
- Skill Library 達 12
- 招生 FAQ Workflow 上線（招生旺季前）
- Gate 1 + Gate 2 通過

## 8. ROI 預估

| Initiative | Baseline | 18 月 Target | NT$ 影響 |
| --- | --- | --- | --- |
| 教師行政 / 備課時間 | 高 | -30% | NT$ 1,000 萬/年（等效人力） |
| 招生諮詢回應 | 2-3 天 | < 1 天 | NT$ 600 萬/年（轉換提升） |
| 評鑑文件準備 | 200+ 工時/系所 | -50% | NT$ 480 萬/年 |
| 行政公文處理 | 慢 | -35% | NT$ 320 萬/年 |
| 教師流失防護 | - | - | NT$ 600 萬（招募 + 銜接成本） |
| **小計** |  |  | **NT$ 3,000 萬** |
| **扣除投資** |  |  | **-600 萬** |
| **淨效益** |  |  | **NT$ 2,400 萬/年** |

## 9. 風險與治理

| 風險 | 機率 | 影響 | 緩解 |
| --- | --- | --- | --- |
| 學生個資外流雲 LLM | 中 | 致命 | 學生資料走地端；redact；Audit |
| AI 代寫破壞學術誠信 | 高 | 高 | 學生端學術誠信指引 + AI 內容檢核 + 教師教育 |
| AI 批改誤判給錯成績 | 中 | 高 | AI 僅 formative 輔助；成績一律教師確認 |
| 教師兩極抗拒 | 高 | 中 | 以減負破冰；種子教師示範；不強制 |
| 評鑑文件 AI 內容被質疑 | 中 | 中 | 系所助理 review；來源追溯 |

## 10. 結果摘要

18 個月後：
- 從 L1 推進至 L3-L4
- 教師行政負擔 -30%；招生回應 < 1 天；評鑑準備 -50%
- 學術倫理指引成為校務常設規範
- 課程推薦 Agent 學生使用率達 35%
- 教學發展中心轉型為「AI 教學支援中心」

引用：完整 PoC `02_Course_Design/POC_SCENARIO_SPECS.md`；產業 `INDUSTRY_SCENARIOS.md`（教育段）；顧問工具 `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`。
