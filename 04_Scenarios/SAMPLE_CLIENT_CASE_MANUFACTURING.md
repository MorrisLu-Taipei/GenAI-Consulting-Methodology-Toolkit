# 範例客戶完整案例：研發製造業

更新日期：2026-05-13

## 1. 案例定位

本案例用來示範「企業 AI 轉型成熟度診斷與導入方案」如何從問卷、課程，到顧問診斷報告形成完整交付。

案例產業：研發製造業  
公司規模：約 500 人  
主要部門：業務、客服、研發、製造、品保、營運、財務、IT  
主要系統：Gmail、Google Sheets、Notion、CRM、ERP、QMS、內部 API、檔案伺服器  
建議部署：Hybrid，核心資料留地端，低敏感工作可使用雲 AI

## 1.1 案例交付邏輯

本案例不是單純描述「可以做什麼」，而是示範一個完整顧問交付流程：

1. 現況資料蒐集：收集系統清單、部門流程、AI 使用現況、資料敏感度。
2. 問卷診斷：完成 10 題快速診斷與 25 題課前診斷。
3. 訪談評估：訪談管理層、客服、營運、品保、IT。
4. As-Is 流程盤點：繪製客訴處理與 ERP 異常訂單流程。
5. L1-L5 能力評估：逐級定義 input、process、output、evidence。
6. 課程與工作坊：依成熟度配置 L1-L4 課程。
7. PoC 設計：選定「客訴信件 + CRM + ERP + QMS」為第一個 PoC。
8. 顧問診斷報告：產出 Roadmap、ROI、治理與後續 SOW。

每一階段都必須留下可驗證 deliverables，避免只停留在口頭建議。

## 2. 客戶故事

這家公司已經有不少員工開始使用 AI。業務會用 AI 寫信，研發會用 AI 摘要文件，客服會用 AI 草擬回覆，但所有成果都停在個人電腦與聊天紀錄裡。

管理層的困惑是：

- 大家都說 AI 好用，但公司看不到整體 ROI。
- ERP、CRM、QMS 裡有很多資料，但 AI 沒有真正串進流程。
- 客訴、異常訂單、品質問題仍靠人工查資料與整理報告。
- IT 擔心資料外流，所以不敢讓核心資料直接上雲。
- 新人學習 SOP、品質規範與客戶規格很慢。

因此本案的重點不是先導入最炫的 Agent，而是先建立可治理的 AI 使用入口、部門 Skill、n8n Workflow，再逐步導入 Hermes Agent。

## 3. 問卷填答摘要

### 3.1 10 題快速診斷結果

| 題號 | 構面 | 分數 | 觀察 |
| --- | --- | ---: | --- |
| Q1 | AI 工具入口 | 2 | 員工各自用雲端 AI，尚未有統一入口 |
| Q2 | AI 使用頻率 | 3 | 業務、研發、客服已有穩定個人使用 |
| Q3 | Prompt / SOP / Skill | 1 | 有零星 Prompt，沒有部門 Skill Library |
| Q4 | 新人套用 Skill | 1 | 新人仍靠資深同仁口頭教 |
| Q5 | 系統串接 | 1 | 尚未用 n8n 串 ERP / CRM / QMS |
| Q6 | 自動流程 | 1 | 有少量排程報表，但 AI 未進流程 |
| Q7 | Agent 任務 | 0 | 尚未有 Hermes Agent |
| Q8 | 多 Agent 協作 | 0 | 尚未有 ClawTeam 場景 |
| Q9 | 治理與紀錄 | 2 | IT 有資安意識，但缺 AI 使用紀錄 |
| Q10 | ROI 指標 | 1 | 管理層想看 ROI，但尚未定義 KPI |

總分：12 / 40  
快速判定：L1，局部具備 L2 萌芽  
主要缺口：Skill 沉澱、Workflow 串接、治理與 ROI

### 3.2 25 題課前診斷摘要

| 構面 | 平均分數 | 判斷 |
| --- | ---: | --- |
| 工具使用 | 2.6 | 個人使用已成形，但缺統一入口 |
| 知識沉澱 | 1.4 | SOP 與 Prompt 未 Skill 化 |
| 流程自動化 | 1.2 | 流程仍人工搬資料 |
| 系統整合 | 1.4 | ERP / CRM / QMS 尚未納入 AI 流程 |
| Agent 應用 | 0.4 | 尚未具備 Agent 基礎 |
| 治理與 ROI | 1.8 | 有資安意識，但缺制度化管理 |

初判成熟度：整體 L1，部分部門接近 L2  
建議目標：90 天內達成 L2 穩定化，並完成 1 個 L3 Workflow PoC

## 4. 公司屬性與部署模式判斷

### 4.1 公司屬性

| 項目 | 判斷 |
| --- | --- |
| 產業 | 研發製造業 |
| 資料敏感度 | 高，包含客戶規格、BOM、品質紀錄、訂單與出貨資料 |
| 系統封閉度 | 中高，ERP、QMS、內部 API 需 IT 協助 |
| IT 能力 | 中，有 IT 團隊但資源有限 |
| 雲端政策 | 一般資料可上雲，核心資料不可直接上雲 |
| 導入風險 | 資料權限、錯誤決策、流程維運、跨部門責任 |

### 4.2 建議部署模式

建議採 Hybrid。

理由：

- OpenWebUI 可作為受控 AI 入口。
- 一般文件摘要、訓練與文案可使用雲 AI。
- ERP、QMS、客戶規格、品質資料留在受控環境。
- n8n 可作為流程橋接層，透過權限控管串接內部 API。
- Hermes Agent 初期只做分析、整理與提醒，不直接改 ERP 核心資料。

## 5. 建議課程比例

| 模組 | 比例 | 原因 |
| --- | ---: | --- |
| L1 OpenWebUI | 25% | 建立統一入口、使用規範與資料安全觀念 |
| L2 Skill AI | 35% | 製造業知識多，需先沉澱 SOP、品質、客訴、異常分析 Skill |
| L3 n8n Workflow AI | 30% | 優先完成 ERP / CRM / QMS / Sheets 的 PoC |
| L4 Hermes Agent | 10% | 先設計營運或客服 Agent 任務卡 |
| L5 ClawTeam | 0% | 尚未具備多 Agent 團隊基礎，先列入後續 Roadmap |

課程產品包建議：二日導入營 + 顧問診斷專案

## 6. 課程中應產出的工作資產

### 6.1 L1 產出

- AI 使用規範草案。
- OpenWebUI 使用流程。
- 業務、客服、研發、品保常用 Prompt。

### 6.2 L2 產出

優先建立 5 個 Skill：

1. 客訴摘要 Skill。
2. 8D / 5Why 問題分析 Skill。
3. ERP 異常訂單分析 Skill。
4. SOP / WI 文件摘要 Skill。
5. 客戶規格差異整理 Skill。

### 6.3 L3 產出

優先完成 1 個 PoC：

> 客訴信件與 ERP 訂單狀態整合 Workflow

流程：

1. Gmail 收到客訴信。
2. AI 判斷客訴類型、客戶、產品與急迫性。
3. CRM 查客戶等級與歷史案件。
4. ERP 查訂單、出貨與庫存狀態。
5. QMS 查相關品質紀錄。
6. Notion 建立案件任務。
7. Sheets 記錄處理狀態。
8. 產出客服回覆草稿與主管摘要。

### 6.4 L4 產出

Hermes Agent 任務卡：

名稱：客服案件整理 Agent  
目標：收到客訴後，自動整理客戶背景、訂單狀態、品質紀錄與回覆草稿。  
可用工具：客訴摘要 Skill、8D / 5Why Skill、n8n 客訴 Workflow、CRM 查詢、ERP 查詢、QMS 查詢。  
限制：不得直接修改 ERP / QMS 正式資料；所有對外回覆需人工確認。  
輸出：案件摘要、建議回覆、待追蹤清單、風險提醒。

## 7. 八階段顧問診斷分析

### Stage 1：As-Is Snapshot 現況掌握

觀察：

- AI 使用停在個人效率。
- ERP、CRM、QMS 資料豐富，但流程未串接。
- 客訴與異常分析高度依賴資深員工。

輸出：

- AI 使用盤點。
- 客訴處理 As-Is Process Map。
- 系統與資料源盤點。

### Stage 2：Reference Model Alignment 標準模型引入

判定：

- 整體 L1。
- 客服、研發、業務具備 L2 潛力。
- 尚未達 L3，因缺 n8n Workflow 與系統串接。

輸出：

- L1-L5 成熟度評估表。
- 部門成熟度比較。

### Stage 3：Best Practice Integration 最佳實務對標

製造業優先 AI 場景：

- 客訴分析。
- ERP 異常訂單。
- 品質問題 8D / 5Why。
- SOP / WI 查詢。
- 研發文件摘要。

### Stage 4：Gap Analysis 差距分析

| 類型 | 發現 | 影響 |
| --- | --- | --- |
| Missing | 缺 Skill Library | 好方法無法複製 |
| Missing | 缺 n8n Workflow | AI 未進入流程 |
| Broken | 客訴需人工查 CRM / ERP / QMS | 回應慢、易漏資料 |
| Redundant | 主管週報人工整理 | 花時間且格式不一致 |
| Missing | 缺 ROI 指標 | 管理層難決策 |

### Stage 5：Problem Definition 核心問題定義

Executive Problem Statement：

> 公司已具備個人 AI 使用基礎，但缺少部門 Skill 沉澱、跨系統 Workflow 與治理機制，導致 AI 成果無法複製、客訴與異常處理仍高度依賴人工，管理層也無法衡量 AI 投資回報。

### Stage 6：Benchmarking and Phased Goals 階段目標

90 天目標：

- 建立 OpenWebUI 使用規範。
- 完成 5 個 L2 Skill。
- 完成 1 個 L3 客訴 Workflow PoC。
- 建立客服案件整理 Hermes Agent 任務卡。
- 定義 5 個 ROI 指標。

### Stage 7：To-Be Design 未來藍圖

To-Be 架構：

- L1：OpenWebUI 作為受控 AI 入口。
- L2：Notion / Git / 文件庫作為 Skill Library。
- L3：n8n 串接 Gmail、CRM、ERP、QMS、Sheets、Notion。
- L4：Hermes Agent 呼叫 Skill 與 Workflow。
- L5：第二階段再規劃 ClawTeam，例如「品質改善 Agent Team」。

### Stage 8：Implementation and Change 導入與變革治理

治理建議：

- 設定 AI 使用規範。
- 設定資料分級。
- ERP / QMS 僅允許查詢，不允許 Agent 直接修改。
- 所有客戶對外回覆需人工確認。
- n8n 執行需保留 Log。
- 每月回顧 ROI 與流程改善。

## 8. 三階段 Roadmap

### Phase 1：0-30 天，AI 基礎與 Skill 化

任務：

- 啟用 OpenWebUI 或統一 AI 入口。
- 完成 AI 使用規範。
- 建立 5 個部門 Skill。
- 完成客訴 As-Is 流程盤點。

驗收：

- 20 位種子人員完成訓練。
- 5 個 Skill 可被部門使用。
- 每個 Skill 有 Owner 與版本。

### Phase 2：31-60 天，n8n Workflow PoC

任務：

- 串接 Gmail、CRM、ERP、QMS、Sheets、Notion。
- 建立客訴 Workflow PoC。
- 加入人工審核節點。
- 建立 Log 與錯誤通知。

驗收：

- 客訴案件可自動分類。
- 可產生客戶背景、訂單狀態、品質紀錄摘要。
- 回覆草稿需人工確認後送出。

### Phase 3：61-90 天，Hermes Agent 與治理

任務：

- 建立客服案件整理 Hermes Agent。
- 讓 Agent 呼叫 L2 Skill 與 L3 Workflow。
- 建立 ROI Dashboard。
- 評估第二波 PoC：ERP 異常訂單分析。

驗收:

- Agent 可完成案件摘要與追蹤清單。
- 管理層可看到每週 KPI。
- 形成下一階段 SOW。

## 9. ROI 指標

| KPI | 現況 | 90 天目標 |
| --- | --- | --- |
| 客訴初步整理時間 | 30-60 分鐘 / 件 | 降至 10-15 分鐘 / 件 |
| 查詢 CRM / ERP / QMS 次數 | 人工多系統查詢 | 由 Workflow 自動彙整 |
| 客服回覆草稿產出 | 人工撰寫 | AI 產生草稿，人工確認 |
| 客訴週報製作 | 2-4 小時 / 週 | 降至 30 分鐘內 |
| Skill 產出 | 無正式 Skill | 5 個可用 Skill |
| 流程 PoC | 無 | 1 個 L3 PoC |

## 10. 最終顧問報告摘要

本案例的建議結論：

- 目前成熟度：整體 L1，局部 L2。
- 目標成熟度：90 天內達到 L2 穩定，完成 L3 PoC。
- 建議部署：Hybrid。
- 優先場景：客訴信件與 ERP / CRM / QMS 整合。
- 建議課程：二日導入營 + 顧問診斷專案。
- 後續導入：客服案件整理 Hermes Agent，第二波擴展到 ERP 異常訂單分析。

## 11. L1-L5 Input / Process / Output / Evidence

### 11.1 L1 Chat AI：OpenWebUI

| 項目 | 定義 |
| --- | --- |
| Input | 員工日常文件、Email、會議紀錄、SOP、非敏感產品資料、AI 使用現況問卷 |
| Process | 建立受控 AI 入口，訓練 Prompt 基礎，定義可輸入與不可輸入資料，建立個人效率場景 |
| Output | 個人常用 Prompt、AI 使用規範、OpenWebUI 使用流程、部門常見任務範例 |
| Evidence | OpenWebUI 截圖、帳號清單、Prompt 範本、使用規範文件、課程簽到與練習成果 |
| 驗收標準 | 種子人員能用 OpenWebUI 完成摘要、改寫、Email 草稿與主管摘要；不得輸入核心機密資料 |

### 11.2 L2 Skill AI：Antigravity / Claude Code / Codex

| 項目 | 定義 |
| --- | --- |
| Input | 資深員工經驗、客訴 SOP、8D / 5Why 範本、ERP 異常處理規則、品質文件、客戶規格摘要 |
| Process | 將個人經驗轉為 Skill，定義 Skill 目標、輸入、步驟、輸出格式、限制與驗收條件 |
| Output | 客訴摘要 Skill、8D / 5Why Skill、ERP 異常訂單分析 Skill、SOP 摘要 Skill、客戶規格差異 Skill |
| Evidence | Skill Library、Skill 模板、版本紀錄、範例輸入輸出、部門 Owner 名單 |
| 驗收標準 | 至少 5 個 Skill 可被非原作者使用，且輸出格式一致；每個 Skill 有 Owner 與更新紀錄 |

### 11.3 L3 Workflow AI：n8n

| 項目 | 定義 |
| --- | --- |
| Input | Gmail 客訴信、CRM 客戶資料、ERP 訂單 / 出貨 / 庫存資料、QMS 品質紀錄、Sheets 追蹤表、Notion 任務庫 |
| Process | 用 n8n 建立 Trigger、資料查詢、AI 分類、Skill 呼叫、人工審核、寫入紀錄、通知與錯誤處理 |
| Output | 客訴案件分類、客戶背景摘要、訂單狀態摘要、品質紀錄摘要、客服回覆草稿、主管週報 |
| Evidence | n8n Workflow JSON、執行 Log、測試案例、錯誤通知紀錄、人工審核紀錄、資料欄位對照表 |
| 驗收標準 | 至少完成 10 筆測試案件；可自動分類、查詢資料、產生摘要與回覆草稿；對外回覆需人工確認 |

### 11.4 L4 Auto Agentic AI：Hermes Agent

| 項目 | 定義 |
| --- | --- |
| Input | 客服案件、客訴摘要 Skill、8D / 5Why Skill、n8n 客訴 Workflow、CRM / ERP / QMS 查詢結果 |
| Process | Hermes Agent 接收任務，拆解為查資料、分類、摘要、風險判斷、建議回覆、追蹤提醒 |
| Output | 案件摘要、處理建議、待追蹤清單、風險標記、主管報告草稿 |
| Evidence | Agent 任務卡、Agent 可用工具清單、權限表、執行紀錄、人工接手紀錄 |
| 驗收標準 | Agent 不直接修改 ERP / QMS；所有建議可追溯資料來源；高風險案件自動標記人工處理 |

### 11.5 L5 Agentic Team AI：ClawTeam

| 項目 | 定義 |
| --- | --- |
| Input | 客訴趨勢、品質異常、ERP 延遲資料、客戶等級、產品線資料、改善專案目標 |
| Process | 多 Agent 分工：品質分析 Agent、營運分析 Agent、客服 Agent、財務 Agent、專案整合 Agent |
| Output | 品質改善提案、客訴根因分析、成本影響估算、跨部門改善 Roadmap |
| Evidence | Agent Team 角色卡、任務分派紀錄、各 Agent 輸出、整合報告、主管審核紀錄 |
| 驗收標準 | L5 不作為第一階段上線目標；需待 L3 Workflow 與 L4 Agent 穩定後，以品質改善專案進行試點 |

## 12. 評估流程與可驗證 Deliverables

| 階段 | 評估活動 | Deliverables | 驗證方式 |
| --- | --- | --- | --- |
| 診斷前 | 收集公司系統、流程、AI 使用現況 | 系統盤點表、AI 使用盤點表 | 由 IT 與部門主管確認 |
| 問卷 | 10 題與 25 題成熟度問卷 | 問卷結果、構面分數、成熟度初判 | 問卷原始資料與計分表 |
| 訪談 | 訪談客服、營運、品保、IT、主管 | 訪談紀錄、痛點清單 | 受訪者確認紀錄 |
| As-Is | 盤點客訴與異常訂單流程 | As-Is Process Map | 部門工作坊確認 |
| L2 | 建立 Skill Library | 5 個 Skill、Owner、版本 | Skill 測試輸入輸出 |
| L3 | 建立 n8n PoC | Workflow JSON、Log、測試資料 | 10 筆測試案件執行成功 |
| L4 | 建立 Hermes Agent 任務卡 | Agent 角色卡、權限表、工具清單 | Agent 測試紀錄與人工審核 |
| 顧問報告 | 八階段診斷與 Roadmap | AI 轉型診斷報告 | 管理層簡報與簽核 |

## 13. Stage Gate 驗收設計

### Gate 1：L1 使用入口與規範

必備證據：

- OpenWebUI 或核准 AI 入口已可使用。
- AI 使用規範已完成。
- 種子人員完成至少 3 個 Prompt 練習。

### Gate 2：L2 Skill Library

必備證據：

- 至少 5 個 Skill。
- 每個 Skill 有用途、輸入、步驟、輸出、限制與 Owner。
- 至少 2 位非原作者能使用 Skill 產出可接受結果。

### Gate 3：L3 Workflow PoC

必備證據：

- n8n Workflow 可執行。
- 可串接 Gmail、CRM、ERP、QMS、Sheets 或 Notion 中至少 3 類系統。
- 有執行 Log、錯誤處理與人工審核節點。

### Gate 4：L4 Hermes Agent

必備證據：

- Agent 任務卡完成。
- Agent 可呼叫至少 1 個 Skill 與 1 個 n8n Workflow。
- Agent 輸出需有資料來源與人工確認機制。

### Gate 5：L5 ClawTeam 準備度

必備證據：

- 已有穩定 L3 Workflow。
- 已有至少 1 個可控 L4 Agent。
- 已定義跨部門任務、Agent 角色與人工 Gate。

