# AI 導入專案 WBS 範本

版本：v1.0  
適用範圍：企業 AI 轉型成熟度診斷、L1-L5 課程導入、PoC 建置、Agent / Workflow 導入與後續擴散  
建議放置路徑：`07_Project_Management/AI_PROJECT_WBS_TEMPLATE.md`

---

## 1. 文件目的

本文件提供一套可重複使用的 **AI 導入專案 WBS（Work Breakdown Structure，工作分解結構）範本**，協助顧問、企業主管、IT 團隊與流程 Owner，將 AI 導入從「課程、工具或概念」轉換成可規劃、可分工、可追蹤、可驗收的專案。

AI 導入專案常見問題不是沒有工具，而是：

- 目標不清楚：不知道這次導入到底要改善什麼。
- 範圍不清楚：課程、PoC、系統串接、治理責任混在一起。
- 責任不清楚：主管、IT、流程 Owner、顧問、使用者的分工不明。
- 驗收不清楚：只有上完課或做完 Demo，沒有 evidence 與 Stage Gate。
- 效益不清楚：無法回答時間節省、錯誤率改善、採用率與 ROI。

因此，本 WBS 範本的核心目標是：

> 將 AI 成熟度診斷、L1-L5 能力建置、PoC 實作、治理設計、效益追蹤與後續擴散，拆解成可執行的專案工作包。

---

## 2. 使用方式

本 WBS 可依專案規模裁剪使用：

| 專案型態 | 建議使用範圍 |
|---|---|
| AI 課程型專案 | 使用 WBS 1、2、3、4、8 |
| AI 成熟度診斷專案 | 使用 WBS 1、2、7、8 |
| L3 Workflow PoC 專案 | 使用 WBS 1、2、4、5、6、7、8 |
| L4 Agent PoC 專案 | 使用 WBS 1、2、4、5、6、7、8、9 |
| 企業 AI 轉型導入專案 | 使用完整 WBS 1-10 |

建議顧問使用方式：

1. 先用 AI 成熟度問卷判斷客戶目前位於 L1-L5 哪一階段。
2. 再用本 WBS 選擇適合的工作包。
3. 依客戶產業、部署模式、系統成熟度與風險要求調整工作項目。
4. 每個工作包都要定義交付物、Evidence、Owner 與驗收標準。
5. 專案結束時，將 WBS 完成狀態納入顧問診斷報告。

---

## 3. WBS 總覽

| WBS 編號 | 工作包 | 主要目的 | 主要交付物 |
|---|---|---|---|
| 1.0 | 專案啟動與治理 | 建立專案目標、範圍、角色與治理節奏 | 專案章程、RACI、會議節奏、風險初表 |
| 2.0 | AI 成熟度診斷 | 掌握企業現況、成熟度、缺口與導入優先順序 | 問卷結果、成熟度分數、缺口分析、課程比例 |
| 3.0 | L1 Chat AI 能力建置 | 建立受控 AI 使用入口與基礎 Prompt 能力 | AI 使用規範、Prompt Library、帳號與權限表 |
| 4.0 | L2 Skill AI 能力建置 | 將個人經驗沉澱成可複用 Skill | Skill Library、SOP、Checklist、模板 |
| 5.0 | L3 Workflow AI PoC | 串接系統與流程，完成可驗證自動化 PoC | n8n Workflow、Execution Log、資料表、錯誤處理 |
| 6.0 | L4 Agent PoC | 建立可追溯、可審核、可持續運行的 Agent 任務 | Agent 任務卡、Wiki、Briefing、Gate 4A-4E |
| 7.0 | KPI / ROI 與數據追蹤 | 建立效益衡量模型與儀表板需求 | KPI 字典、Baseline、ROI 試算、Dashboard Spec |
| 8.0 | 交付驗收與 Stage Gate | 確認每一階段成果可被驗證 | Evidence Matrix、Gate Review、驗收紀錄 |
| 9.0 | 上線準備與維運設計 | 建立 Owner、Runbook、權限與維運流程 | 上線檢核表、Runbook、維運責任表 |
| 10.0 | 擴散與 Roadmap | 規劃 30/60/90 天與下一波導入 | Roadmap、Use Case Portfolio、擴散計畫 |

---

## 4. 詳細 WBS

## 1.0 專案啟動與治理

### 1.1 定義專案背景與商業目標

| 欄位 | 內容 |
|---|---|
| 工作說明 | 釐清企業推動 AI 的背景、痛點、目標與管理層期待。 |
| 主要活動 | 訪談 Sponsor、確認策略目標、定義專案成功樣貌。 |
| 交付物 | AI 導入專案章程草案。 |
| Evidence | 啟動會議紀錄、Sponsor 訪談摘要、確認後的專案目標。 |
| Owner | Sponsor / 顧問 PM |
| 驗收標準 | 管理層能用 3-5 句話說明本專案為何要做、要改善什麼。 |

### 1.2 定義專案範圍與非範圍

| 欄位 | 內容 |
|---|---|
| 工作說明 | 明確界定本次 AI 導入涵蓋哪些部門、流程、系統、課程與 PoC。 |
| 主要活動 | 定義 In Scope / Out of Scope、列出不處理項目、確認限制條件。 |
| 交付物 | Scope Statement。 |
| Evidence | 範圍確認表、會議簽核紀錄。 |
| Owner | 顧問 PM / 客戶 PM |
| 驗收標準 | 專案團隊對本次不做什麼有共同認知。 |

### 1.3 建立專案角色與 RACI

| 欄位 | 內容 |
|---|---|
| 工作說明 | 定義 Sponsor、PM、IT Owner、流程 Owner、資料 Owner、顧問、使用者代表的責任。 |
| 主要活動 | 建立 RACI 表、確認決策權與簽核權。 |
| 交付物 | AI 導入 RACI Matrix。 |
| Evidence | 角色名單、責任矩陣、簽核流程。 |
| Owner | 顧問 PM / 客戶 PM |
| 驗收標準 | 每個關鍵工作包都有唯一負責人與明確決策者。 |

### 1.4 設定專案會議節奏

| 欄位 | 內容 |
|---|---|
| 工作說明 | 設定專案週會、技術會議、風險會議、Stage Gate Review 與主管報告節奏。 |
| 主要活動 | 安排會議頻率、議程模板、紀錄格式與追蹤方式。 |
| 交付物 | Meeting Cadence Plan。 |
| Evidence | 會議排程、會議紀錄模板、Action Item Tracker。 |
| Owner | 客戶 PM / 顧問 PM |
| 驗收標準 | 所有專案問題都有固定回報與決策機制。 |

### 1.5 建立初始風險登錄表

| 欄位 | 內容 |
|---|---|
| 工作說明 | 盤點 AI 導入的初始風險，包括資料、技術、使用、治理、商業與維運風險。 |
| 主要活動 | 建立 Risk Register、評估機率與影響、指定風險 Owner。 |
| 交付物 | AI Project Risk Register。 |
| Evidence | 風險清單、風險等級、對應措施。 |
| Owner | 顧問 PM / IT Owner / 流程 Owner |
| 驗收標準 | 高風險項目有明確處理策略與負責人。 |

---

## 2.0 AI 成熟度診斷

### 2.1 選擇診斷版本

| 欄位 | 內容 |
|---|---|
| 工作說明 | 依專案階段選擇 10 題快速診斷、25 題課前診斷或 50 題顧問深度診斷。 |
| 主要活動 | 確認診斷目的、受訪對象與填答方式。 |
| 交付物 | 診斷計畫。 |
| Evidence | 問卷版本、填答名單、填答時程。 |
| Owner | 顧問 / 客戶 PM |
| 驗收標準 | 問卷版本與受訪對象符合本次專案目的。 |

### 2.2 蒐集問卷與訪談資料

| 欄位 | 內容 |
|---|---|
| 工作說明 | 蒐集管理層、IT、部門主管與使用者的 AI 使用現況。 |
| 主要活動 | 發送問卷、進行訪談、蒐集現有文件與流程資料。 |
| 交付物 | 問卷原始資料、訪談摘要。 |
| Evidence | 問卷回覆、訪談紀錄、資料來源清單。 |
| Owner | 顧問 / 部門窗口 |
| 驗收標準 | 關鍵部門與決策角色皆有輸入資料。 |

### 2.3 計算成熟度分數

| 欄位 | 內容 |
|---|---|
| 工作說明 | 依六大構面計算成熟度分數，判斷主成熟度與局部成熟度。 |
| 主要活動 | 計算 L1-L5、工具使用、知識沉澱、流程自動化、系統整合、Agent 應用、治理與 ROI 分數。 |
| 交付物 | AI 成熟度評分表。 |
| Evidence | 計算表、雷達圖、分數說明。 |
| Owner | 顧問 / 數據分析負責人 |
| 驗收標準 | 分數可回溯到原始問卷與訪談證據。 |

### 2.4 產出缺口分析

| 欄位 | 內容 |
|---|---|
| 工作說明 | 分析企業目前能力與目標能力之間的差距。 |
| 主要活動 | 分類工具缺口、Skill 缺口、Workflow 缺口、系統串接缺口、Agent 缺口、治理缺口。 |
| 交付物 | Gap Analysis。 |
| Evidence | 缺口矩陣、部門成熟度表、訪談佐證。 |
| Owner | 顧問 |
| 驗收標準 | 客戶主管認同主要缺口與優先順序。 |

### 2.5 建議課程比例與 PoC 方向

| 欄位 | 內容 |
|---|---|
| 工作說明 | 依成熟度、部署模式、產業情境與風險要求，建議 L1-L5 課程比例與第一波 PoC。 |
| 主要活動 | 對應課程模組、選擇 PoC 候選場景、確認優先導入部門。 |
| 交付物 | 課程比例建議、PoC 候選清單。 |
| Evidence | 課程配置表、Use Case 初選表。 |
| Owner | 顧問 PM / Sponsor |
| 驗收標準 | 管理層同意第一波課程方向與 PoC 範圍。 |

---

## 3.0 L1 Chat AI 能力建置

### 3.1 建立 AI 使用入口與帳號規劃

| 欄位 | 內容 |
|---|---|
| 工作說明 | 規劃企業 AI 使用入口，例如 OpenWebUI 或其他核准工具。 |
| 主要活動 | 帳號規劃、群組規劃、權限邊界、使用政策。 |
| 交付物 | 帳號 / 群組 / 權限表。 |
| Evidence | 帳號表、登入截圖、權限設定截圖。 |
| Owner | IT Owner |
| 驗收標準 | 使用者能以指定帳號安全登入並使用受控 AI 入口。 |

### 3.2 建立 AI 使用規範

| 欄位 | 內容 |
|---|---|
| 工作說明 | 定義哪些資料可輸入 AI、哪些資料不得輸入 AI，以及高風險任務處理規則。 |
| 主要活動 | 資料分類、使用情境規範、禁止事項、人工審核原則。 |
| 交付物 | AI 使用規範。 |
| Evidence | 規範文件、宣導紀錄、學員確認紀錄。 |
| Owner | IT Owner / 法務或資安 / 顧問 |
| 驗收標準 | 使用者能說明至少三類不得輸入 AI 的資料。 |

### 3.3 建立 Prompt Library

| 欄位 | 內容 |
|---|---|
| 工作說明 | 整理部門常用工作情境，建立可重複使用的 Prompt。 |
| 主要活動 | 收集高頻任務、設計 Prompt 模板、測試輸出品質。 |
| 交付物 | Prompt Library。 |
| Evidence | Prompt 文件、測試輸出、部門使用回饋。 |
| Owner | 部門 Owner / 顧問 |
| 驗收標準 | 每個優先部門至少完成 3-5 個高頻 Prompt。 |

### 3.4 完成 L1 課堂實作與驗收

| 欄位 | 內容 |
|---|---|
| 工作說明 | 透過課程與實作確認使用者具備基本 AI 對話能力。 |
| 主要活動 | 摘要、改寫、分類、報告初稿、Email 草稿等練習。 |
| 交付物 | L1 課堂作業。 |
| Evidence | 學員作業、範例輸出、課後回饋。 |
| Owner | 講師 / 顧問 |
| 驗收標準 | 學員能針對自己的工作產出可用 AI 初稿。 |

---

## 4.0 L2 Skill AI 能力建置

### 4.1 盤點高頻工作與資深經驗

| 欄位 | 內容 |
|---|---|
| 工作說明 | 找出最適合 Skill 化的高頻任務、知識工作與資深員工經驗。 |
| 主要活動 | 部門訪談、任務盤點、SOP 蒐集、案例整理。 |
| 交付物 | Skill 候選清單。 |
| Evidence | 訪談紀錄、任務清單、現有 SOP。 |
| Owner | 部門 Owner / 顧問 |
| 驗收標準 | 每個優先部門至少找出 3 個 Skill 候選任務。 |

### 4.2 建立 Skill 標準模板

| 欄位 | 內容 |
|---|---|
| 工作說明 | 定義 Skill 文件應包含的欄位與品質標準。 |
| 主要活動 | 設計 Skill 名稱、用途、輸入、處理步驟、輸出格式、範例、限制、測試案例。 |
| 交付物 | Skill Template。 |
| Evidence | Skill 樣板、範例 Skill。 |
| Owner | 顧問 |
| 驗收標準 | 非原作者能依模板重複建立 Skill。 |

### 4.3 建立 Skill Library

| 欄位 | 內容 |
|---|---|
| 工作說明 | 將部門 Skill 集中管理，形成可重複使用的知識資產。 |
| 主要活動 | 建立文件庫、分類、Owner、版本、測試紀錄。 |
| 交付物 | Skill Library。 |
| Evidence | Skill 文件、版本紀錄、Owner 清單。 |
| Owner | 部門 Owner / 知識管理 Owner |
| 驗收標準 | 使用者能查找、使用並回饋 Skill。 |

### 4.4 測試 Skill 可重複使用性

| 欄位 | 內容 |
|---|---|
| 工作說明 | 驗證 Skill 是否能被不同人使用並產出穩定品質。 |
| 主要活動 | 測試案例設計、多人測試、輸出品質比較、修正 Skill。 |
| 交付物 | Skill 測試紀錄。 |
| Evidence | 測試輸入、測試輸出、修正紀錄。 |
| Owner | 顧問 / 部門 Reviewer |
| 驗收標準 | 至少 2 位非原作者能使用 Skill 產出可接受成果。 |

---

## 5.0 L3 Workflow AI PoC

### 5.1 選定 Workflow PoC 場景

| 欄位 | 內容 |
|---|---|
| 工作說明 | 從高價值 AI 場景清單中選出第一波 Workflow PoC。 |
| 主要活動 | 評估 Impact、Effort、Data Readiness、Risk、Owner。 |
| 交付物 | PoC 場景選定表。 |
| Evidence | Use Case 評分表、主管確認紀錄。 |
| Owner | Sponsor / 流程 Owner / 顧問 PM |
| 驗收標準 | PoC 具備明確商業價值、流程 Owner 與可用資料。 |

### 5.2 繪製 As-Is / To-Be 流程

| 欄位 | 內容 |
|---|---|
| 工作說明 | 釐清目前流程與導入 AI Workflow 後的目標流程。 |
| 主要活動 | 流程訪談、流程圖繪製、人工重工點分析、例外處理盤點。 |
| 交付物 | As-Is / To-Be 流程圖。 |
| Evidence | 流程圖、訪談紀錄、重工點清單。 |
| Owner | 流程 Owner / 顧問 |
| 驗收標準 | 現場人員確認流程描述符合實際作業。 |

### 5.3 定義資料與系統串接需求

| 欄位 | 內容 |
|---|---|
| 工作說明 | 盤點 Workflow 需要讀取、寫入、通知與觸發的系統。 |
| 主要活動 | 確認 Gmail、Sheets、Notion、CRM、ERP、API、DB、Webhook、Credential。 |
| 交付物 | Integration Requirement。 |
| Evidence | 系統清單、欄位清單、API 文件、Credential 檢核表。 |
| Owner | IT Owner / 顧問技術負責人 |
| 驗收標準 | PoC 所需資料來源與權限可被取得或模擬。 |

### 5.4 建立 n8n Workflow PoC

| 欄位 | 內容 |
|---|---|
| 工作說明 | 建立可執行的 n8n Workflow，完成觸發、資料處理、AI 判斷、寫入與通知。 |
| 主要活動 | 建立 Trigger、Node、AI Node、資料轉換、錯誤處理、人工審核節點。 |
| 交付物 | n8n Workflow JSON。 |
| Evidence | Workflow 截圖、JSON 匯出、測試紀錄。 |
| Owner | 顧問技術負責人 / IT Owner |
| 驗收標準 | Workflow 能以測試資料完整跑通一次。 |

### 5.5 建立 Log、錯誤處理與重試機制

| 欄位 | 內容 |
|---|---|
| 工作說明 | 確保 Workflow 執行過程可追蹤、可除錯、可重跑。 |
| 主要活動 | 設計 Execution Log、錯誤通知、重試流程、人工接手方式。 |
| 交付物 | Log Schema、Error Handling Design。 |
| Evidence | 執行紀錄、失敗測試、重跑紀錄。 |
| Owner | IT Owner / 顧問技術負責人 |
| 驗收標準 | 至少完成一個失敗情境測試並留下紀錄。 |

---

## 6.0 L4 Agent PoC

### 6.1 定義 Agent 任務卡

| 欄位 | 內容 |
|---|---|
| 工作說明 | 明確定義 Agent 的角色、任務、資料來源、可用工具、限制與人工 Gate。 |
| 主要活動 | 撰寫 Agent 任務卡、確認任務邊界、定義不可執行事項。 |
| 交付物 | Agent Task Card。 |
| Evidence | 任務卡、主管確認紀錄、IT 確認紀錄。 |
| Owner | 部門 Owner / 顧問 |
| 驗收標準 | Agent 的目標、權限與限制能被主管與 IT 理解並接受。 |

### 6.2 建立 Agent 知識底座

| 欄位 | 內容 |
|---|---|
| 工作說明 | 建立 Agent 可讀取的 Wiki、schema、INBOX、queue、watchlist、tasks 等基礎資料。 |
| 主要活動 | 建立 `purpose.md`、`SCHEMA.md`、任務清單、資料來源清單、初始知識文件。 |
| 交付物 | Agent Wiki。 |
| Evidence | Wiki 檔案、版本紀錄、資料來源表。 |
| Owner | 知識 Owner / 顧問 |
| 驗收標準 | Agent 啟動前能讀取任務目的、資料結構與限制條件。 |

### 6.3 執行 Ingest / Query / Update 測試

| 欄位 | 內容 |
|---|---|
| 工作說明 | 測試 Agent 是否能匯入資料、查詢資料、回答問題、更新知識。 |
| 主要活動 | 匯入文件、建立索引、執行查詢、測試回寫、保留引用來源。 |
| 交付物 | Ingest / Query / Update 測試紀錄。 |
| Evidence | Source page、Log、回答結果、Diff、審核紀錄。 |
| Owner | 顧問技術負責人 / 部門 Reviewer |
| 驗收標準 | 至少完成 3 個可追溯查詢與 1 個受控更新測試。 |

### 6.4 建立 Briefing 與人工 Gate

| 欄位 | 內容 |
|---|---|
| 工作說明 | 設計 Agent 定期回報格式，以及高風險動作前的人工審核機制。 |
| 主要活動 | 建立 morning briefing、weekly briefing、Gate 4A-4E 表。 |
| 交付物 | Briefing Template、Gate 4A-4E Checklist。 |
| Evidence | Briefing 範例、審核紀錄、人工批准紀錄。 |
| Owner | 部門 Owner / 顧問 |
| 驗收標準 | 主管能依 briefing 做出下一步決策，且高風險動作不會繞過人工 Gate。 |

---

## 7.0 KPI / ROI 與數據追蹤

### 7.1 定義 Baseline

| 欄位 | 內容 |
|---|---|
| 工作說明 | 在 AI 導入前建立現況基準值，作為後續效益比較依據。 |
| 主要活動 | 蒐集目前處理時間、錯誤率、處理量、等待時間、重工率、成本。 |
| 交付物 | Baseline Measurement Sheet。 |
| Evidence | 原始數據、抽樣紀錄、計算方式。 |
| Owner | 數據分析負責人 / 流程 Owner |
| 驗收標準 | 每個 PoC 至少有 1-3 個可量測基準指標。 |

### 7.2 建立 KPI 字典

| 欄位 | 內容 |
|---|---|
| 工作說明 | 定義 AI 導入後要追蹤的效益與治理指標。 |
| 主要活動 | 定義 KPI 名稱、公式、資料來源、更新頻率、Owner、目標值。 |
| 交付物 | AI KPI Dictionary。 |
| Evidence | KPI 表、公式說明、資料來源。 |
| Owner | 數據分析負責人 / Sponsor |
| 驗收標準 | 每個 KPI 都有明確公式、資料來源與負責人。 |

### 7.3 建立 ROI 試算模型

| 欄位 | 內容 |
|---|---|
| 工作說明 | 將時間節省、成本降低、品質改善、營收機會轉換成可溝通的效益估算。 |
| 主要活動 | 建立節省工時計算、成本換算、投入成本、回收期與敏感度分析。 |
| 交付物 | ROI Calculation Template。 |
| Evidence | ROI 試算表、假設條件、資料來源。 |
| Owner | 顧問 / 數據分析負責人 |
| 驗收標準 | 管理層能理解 ROI 假設、限制與可能效益範圍。 |

### 7.4 設計 Dashboard 規格

| 欄位 | 內容 |
|---|---|
| 工作說明 | 定義 AI 轉型儀表板頁面、指標、資料表、更新頻率與使用者。 |
| 主要活動 | 設計成熟度總覽、Use Case Portfolio、專案進度、效益追蹤、治理監控。 |
| 交付物 | Dashboard Design Spec。 |
| Evidence | 指標清單、資料模型、Mockup。 |
| Owner | 數據分析負責人 / 顧問 |
| 驗收標準 | Dashboard 規格足以交由 BI 工程師或資料人員製作。 |

---

## 8.0 交付驗收與 Stage Gate

### 8.1 建立 Evidence Matrix

| 欄位 | 內容 |
|---|---|
| 工作說明 | 將每一項交付物與可驗證證據對應起來。 |
| 主要活動 | 列出交付物、Evidence、檔案位置、Owner、驗收日期。 |
| 交付物 | Evidence Matrix。 |
| Evidence | 文件連結、截圖、Log、測試紀錄。 |
| Owner | 顧問 PM / 客戶 PM |
| 驗收標準 | 每一項重要成果都有可回溯證據。 |

### 8.2 執行 Gate Review

| 欄位 | 內容 |
|---|---|
| 工作說明 | 依 L1-L5 對應 Gate 檢查成果是否達到下一階段條件。 |
| 主要活動 | Gate 1-5 檢核、Pass / Conditional Pass / Fail 判定、改善項目追蹤。 |
| 交付物 | Gate Review Record。 |
| Evidence | Gate Checklist、會議紀錄、改善清單。 |
| Owner | Sponsor / 顧問 PM / IT Owner |
| 驗收標準 | 未通過 Gate 的項目不得直接進入上線或擴散。 |

### 8.3 完成正式驗收

| 欄位 | 內容 |
|---|---|
| 工作說明 | 彙整所有交付物、Evidence、缺口、風險與後續建議，完成正式驗收。 |
| 主要活動 | 驗收會議、交付包確認、未結項目確認、簽核。 |
| 交付物 | Acceptance Record。 |
| Evidence | 簽核紀錄、會議紀錄、交付清單。 |
| Owner | Sponsor / 客戶 PM / 顧問 PM |
| 驗收標準 | 客戶確認交付內容、未結項目與下一步安排。 |

---

## 9.0 上線準備與維運設計

### 9.1 建立上線檢核表

| 欄位 | 內容 |
|---|---|
| 工作說明 | 確認 PoC 或 Workflow / Agent 進入正式使用前的必要條件。 |
| 主要活動 | 權限、資料、Log、錯誤處理、人工接手、資安、備份、回復機制檢核。 |
| 交付物 | Go-Live Checklist。 |
| Evidence | 檢核紀錄、權限設定、測試結果。 |
| Owner | IT Owner / 顧問技術負責人 |
| 驗收標準 | 高風險項目完成處理後才能上線。 |

### 9.2 建立維運 Runbook

| 欄位 | 內容 |
|---|---|
| 工作說明 | 設計上線後日常維護、異常處理、版本更新與人工接手流程。 |
| 主要活動 | 建立故障排除步驟、聯絡窗口、升級流程、維護頻率。 |
| 交付物 | Operation Runbook。 |
| Evidence | Runbook 文件、維運責任表。 |
| Owner | IT Owner / 流程 Owner |
| 驗收標準 | 非開發者能依 Runbook 完成基本故障判斷與通報。 |

### 9.3 設定監控與回顧機制

| 欄位 | 內容 |
|---|---|
| 工作說明 | 設定 Workflow / Agent 的執行監控與定期改善機制。 |
| 主要活動 | 設定監控指標、異常通知、每週或每月回顧會。 |
| 交付物 | Monitoring Plan。 |
| Evidence | Log、通知紀錄、改善會議紀錄。 |
| Owner | IT Owner / 流程 Owner |
| 驗收標準 | 異常能被發現、通報、處理與紀錄。 |

---

## 10.0 擴散與 Roadmap

### 10.1 建立 30/60/90 天 Roadmap

| 欄位 | 內容 |
|---|---|
| 工作說明 | 將診斷、課程、PoC 與治理成果轉換成短中期導入計畫。 |
| 主要活動 | 定義 30 天修正、60 天擴大、90 天制度化目標。 |
| 交付物 | 30/60/90 天 Roadmap。 |
| Evidence | Roadmap 文件、主管確認紀錄。 |
| Owner | Sponsor / 顧問 PM |
| 驗收標準 | Roadmap 有明確 Owner、時程、交付物與 KPI。 |

### 10.2 建立 Use Case Portfolio

| 欄位 | 內容 |
|---|---|
| 工作說明 | 彙整所有候選 AI 場景，形成可管理的導入組合。 |
| 主要活動 | 分類 L1-L5、評估優先級、標示狀態、定義下一步。 |
| 交付物 | Use Case Portfolio。 |
| Evidence | 場景清單、評分表、狀態表。 |
| Owner | 顧問 / 客戶 PM |
| 驗收標準 | 管理層能依 Portfolio 決定下一波投資。 |

### 10.3 制定擴散計畫

| 欄位 | 內容 |
|---|---|
| 工作說明 | 將成功 PoC 擴散到其他部門、流程或成熟度階段。 |
| 主要活動 | 定義擴散條件、培訓計畫、Owner 移交、治理制度化。 |
| 交付物 | Scale-out Plan。 |
| Evidence | 擴散清單、訓練計畫、移交紀錄。 |
| Owner | Sponsor / 客戶 PM / 部門 Owner |
| 驗收標準 | 擴散不是複製 Demo，而是包含 Owner、資料、流程、治理與 KPI。 |

---

## 5. WBS 與 L1-L5 對應表

| WBS 工作包 | L1 | L2 | L3 | L4 | L5 | 說明 |
|---|---:|---:|---:|---:|---:|---|
| 1.0 專案啟動與治理 | ✓ | ✓ | ✓ | ✓ | ✓ | 所有 AI 導入都需要治理與責任分工 |
| 2.0 AI 成熟度診斷 | ✓ | ✓ | ✓ | ✓ | ✓ | 用於判斷起點與課程比例 |
| 3.0 L1 Chat AI | ✓ |  |  |  |  | 建立受控 AI 使用入口 |
| 4.0 L2 Skill AI |  | ✓ | ✓ | ✓ | ✓ | Skill 是後續 Workflow / Agent 的能力資產 |
| 5.0 L3 Workflow AI |  |  | ✓ | ✓ | ✓ | Workflow 是 Agent 可呼叫的流程能力 |
| 6.0 L4 Agent PoC |  |  |  | ✓ | ✓ | 建立可追溯的 Agent 作業閉環 |
| 7.0 KPI / ROI | ✓ | ✓ | ✓ | ✓ | ✓ | 將導入成果轉成可衡量指標 |
| 8.0 Stage Gate | ✓ | ✓ | ✓ | ✓ | ✓ | 確保每階段有 evidence 驗收 |
| 9.0 上線維運 |  |  | ✓ | ✓ | ✓ | 適用 Workflow、Agent 與 Agent Team 上線 |
| 10.0 Roadmap 擴散 | ✓ | ✓ | ✓ | ✓ | ✓ | 將 PoC 轉成長期能力建置 |

---

## 6. WBS 與角色責任建議

| 角色 | 主要責任 |
|---|---|
| Sponsor | 決定目標、資源、範圍、優先級與 Stage Gate 是否通過 |
| 客戶 PM | 協調內部資源、追蹤時程、安排會議、管理待辦事項 |
| 顧問 PM | 設計方法論、控管交付品質、主持診斷與驗收 |
| IT Owner | 負責帳號、權限、API、Credential、系統串接、維運與資安 |
| 流程 Owner | 提供現況流程、定義 To-Be 流程、驗證 PoC 是否符合現場 |
| 資料 Owner | 確認資料來源、欄位定義、資料品質、資料使用邊界 |
| 部門 Reviewer | 審查 Prompt、Skill、Workflow、Agent 輸出品質 |
| 使用者代表 | 參與課程、實作測試、提供使用回饋 |

---

## 7. WBS 驗收狀態欄位建議

實際專案管理時，可將本 WBS 轉成 Excel、Google Sheets、Notion Database、Jira 或 GitHub Issue。建議欄位如下：

| 欄位 | 說明 |
|---|---|
| WBS ID | 工作項目編號，例如 5.4 |
| Work Package | 工作包名稱 |
| Task | 具體工作項目 |
| Owner | 負責人 |
| Reviewer | 驗收者 |
| Start Date | 開始日期 |
| Due Date | 預計完成日 |
| Status | Not Started / In Progress / Blocked / Done / Accepted |
| Deliverable | 預期交付物 |
| Evidence Link | 證據連結，例如文件、截圖、Log、測試紀錄 |
| Gate | 對應 Gate 1-5 |
| Risk Level | Low / Medium / High |
| Notes | 備註與待辦 |

---

## 8. 最小可行版 WBS

若客戶預算或時間有限，可以先採用以下最小可行版：

| WBS | 最小交付內容 |
|---|---|
| 1.0 專案啟動 | 專案目標、範圍、Owner、會議節奏 |
| 2.0 診斷 | 10 題或 25 題成熟度診斷 |
| 4.0 Skill | 3 個高頻 Skill |
| 5.0 Workflow | 1 個 n8n PoC |
| 7.0 KPI / ROI | 3 個 Baseline KPI 與簡易 ROI 試算 |
| 8.0 驗收 | Evidence Matrix 與 Gate Review |
| 10.0 Roadmap | 30/60/90 天下一步計畫 |

最小可行版的目的不是一次完成完整 AI 轉型，而是快速證明：

> AI 導入可以被管理、被驗證、被量化，並且能形成下一階段 Roadmap。

---

## 9. 專案完成定義

本 WBS 所定義的 AI 導入專案，不應以「課程結束」或「Demo 完成」作為唯一完成標準。

建議專案完成定義如下：

- 已完成 AI 成熟度診斷，且分數可回溯。
- 已確認 L1-L5 對應能力與主要缺口。
- 已完成至少一個可展示或可執行的 Prompt、Skill、Workflow 或 Agent 成果。
- 已建立 Evidence Matrix，主要交付物皆有證據。
- 已完成 Stage Gate Review，並記錄通過、條件通過或未通過項目。
- 已定義 KPI、Baseline 或 ROI 試算方式。
- 已提出 30/60/90 天 Roadmap。
- 已指定後續 Owner 與維運方式。

---

## 10. 顧問使用提醒

1. 不要把 WBS 當成固定菜單，應依客戶成熟度裁剪。
2. 不要只管理課程時數，要管理交付物與 evidence。
3. 不要只追求 AI Demo，要確認流程 Owner 是否願意接手。
4. 不要只問「能不能自動化」，也要問「資料是否可用、風險是否可控、效益是否可量測」。
5. 不要讓 Agent 直接執行高風險決策，必須設計人工 Gate。
6. 每一項 PoC 都要能回答：節省什麼、改善什麼、誰負責、如何驗收、下一步是什麼。

---

## 11. 延伸搭配文件

建議本文件可搭配以下文件使用：

- `01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`
- `01_Assessment/AI_MATURITY_SCORING_MODEL.md`
- `01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`
- `03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`
- `06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`
- `07_Project_Management/AI_IMPLEMENTATION_PROJECT_CHARTER.md`
- `07_Project_Management/AI_PROJECT_RACI_MATRIX.md`
- `07_Project_Management/AI_PROJECT_RISK_REGISTER.md`
- `08_Data_Analytics/AI_KPI_DICTIONARY.md`
- `08_Data_Analytics/AI_ROI_CALCULATION_TEMPLATE.md`
- `08_Data_Analytics/AI_TRANSFORMATION_DASHBOARD_DESIGN.md`
