# /simulate-engagement

> Claude Code-Native — 30 分鐘跑完一個完整 6 週顧問案 (Engagement Simulator)
> 用途：把整個 Phase A → B → C 顧問流程**壓縮模擬**成 30 分鐘對話，產出 12+ 個真實 deliverable。用於新顧問訓練、銷售 demo、方法論壓力測試。
>
> 為什麼只有 Claude Code 能做：1M context 一次裝下整個方法論 + 同時扮演 4-6 個角色 + 跨檔生出完整交付物。

## 步驟 1：建立模擬客戶（5 分鐘）

請使用者描述假想客戶。若提供不足，用以下範本問：

```text
- 產業 / 規模 / 員工數 / 年營收
- 觸發事件（為什麼今天想做 AI 轉型）
- 主要痛點 3 個
- 不可動限制（預算上限、合規、地端政策）
- Sponsor 是誰、Champion 候選
```

若使用者只給「製造業 500 人」，立刻**自動補完合理參數**（並標明這些是合成的，可被覆寫）。

## 步驟 2：分配 Claude 角色（持續整場）

整場模擬中，Claude **同時扮演** 4 個角色：

| 角色 | 講話風格 | 任務 |
| --- | --- | --- |
| **顧問張** | 專業、結構化、引用 Tool 編號 | 主導訪談、產出 deliverable |
| **客戶 CEO** | 急迫、商業導向、會問 ROI | 對顧問問尖銳問題 |
| **IT 副理** | 務實、保守、擔心吃不消 | 對顧問挑可行性 |
| **內稽 / 法遵** | 嚴謹、合規導向 | 在 Phase B 結尾做品管挑戰 |

**用標籤明確區分**：「[顧問張] ...」「[CEO] ...」「[IT 副理] ...」「[法遵] ...」

## 步驟 3：Phase A 診斷（10 分鐘 = 模擬 2 週）

依 [`00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../../00_Overview/EIGHT_STAGE_FLOW_STORY.md) Phase A 流程，跑完整 Stage 1 + Stage 2 + Stage 3 素材：

| 模擬時間 | 真實對應 | 產出 deliverable |
| --- | --- | --- |
| 1 分鐘 | Week 1 訪談 | 訪談摘要（從 Tool 1.1 40 題挑 10 題模擬問答）|
| 2 分鐘 | Week 1 末 | AI Usage Inventory（虛構但合理）+ Systems Inventory + 1 張 Swimlane |
| 3 分鐘 | Week 2 Day 6-9 | Reference Model Mapping（APQC + Tiger AI L1-L5）+ 雙雷達 |
| 3 分鐘 | Week 2 Day 10 | 從 [`../../04_Scenarios/`](../../04_Scenarios/) 挑 3 個對標案例的 Best-Practice Profile |
| 1 分鐘 | Week 2 末 | **產出中期評估報告大綱**（10-15 頁，依 §1-§6 結構）|

**Gate A 模擬**：[CEO] 看完雷達 → [Claude] 模擬震撼反應 + 決定是否簽 Phase B。

## 步驟 4：Phase B 策略（10 分鐘 = 模擬 4 週）

依 EIGHT_STAGE_FLOW_STORY Phase B：

| 模擬時間 | 真實對應 | 產出 deliverable |
| --- | --- | --- |
| 3 分鐘 | Week 3 Tool 3.6 Workshop | **完整 6 步驟模擬**：素材展示 → 獨立投票（4 個角色各寫 3 張便利貼）→ 集體共識 → Reality check → **Ideal Practice 定義表（三方簽名版）**|
| 2 分鐘 | Week 3-4 | Gap Matrix + 80/20 收斂 + EPS（Executive Problem Statement）|
| 2 分鐘 | Week 4 | Phased Goals + 組織吸收力評估 + Stage Gate Criteria |
| 3 分鐘 | Week 4 末 | **產出完整 14 章顧問報告大綱** |

**Gate B 模擬**：[法遵] 跳出來挑戰報告（依 [`../../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](../../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md) §11-§13 治理段）。

## 步驟 5：Phase C 落地（5 分鐘 = 模擬 24 個月）

時間軸跳躍，每 5 個月 1 分鐘：

- Month 6：L1 Gate 驗收 + 雷達回看（標出哪幾格從 0 升到 2-3）
- Month 12：L2/L3 Gate
- Month 18：第一個 Quick Win 出來，CEO 反應
- Month 24：L4/L5 Gate + 最終雷達 + 完整 Transformation Roadmap 回顧

## 步驟 6：模擬結束輸出（5 分鐘）

產出**模擬包**（一份 markdown 含所有 deliverable 連結）：

```text
## 模擬客戶：[名稱]
## 模擬完成日：[今天]
## ⚠️ 本模擬全部由 AI 產生，所有數字僅為示範用

### Phase A Deliverables
- 中期評估報告大綱（嵌入）
- 雙雷達圖文字版

### Phase B Deliverables  
- Ideal Practice 定義表（三方簽名模擬）
- 完整 14 章報告大綱

### Phase C Deliverables
- 24 個月 Roadmap
- Stage Gate 驗收清單
- 雷達演變（T0 / T6 / T12 / T18 / T24）

### 4 個角色的「亮點台詞」
[CEO] 「...」
[IT 副理] 「...」
[法遵] 「...」
[顧問張] 「...」

### 這次模擬暴露的 3 個方法論弱點
1. ...
2. ...
3. ...
```

## 紀律

- **明示是模擬**：每個 deliverable 都標 `⚠️ Simulated`，引用 Tool 8.9 Evidence Level **L0**（依 [`../../04_Scenarios/README.md`](../../04_Scenarios/README.md)）
- **不假裝真實**：4 個角色的反應由 Claude 編，不能聲稱「客戶會這樣想」
- **暴露方法論弱點**：每次模擬結尾必須寫 3 個「這次模擬暴露的問題」 → 回饋給 Codex `/harvest-insights` 或 `/methodology-test`
- **30 分鐘上限**：超時就停，與其面面俱到不如完整跑一遍
- **可選擇深度**：使用者要 30 分鐘速跑 / 2 小時詳細 / 1 天逐 step 都可，由 Claude 動態調整

## 典型應用場景

- **新顧問訓練**：跑 3 次不同產業，學會方法論流程
- **銷售 demo**：給潛在客戶看「跑你公司會長什麼樣」
- **方法論壓力測試**：在邊界客戶（如 3000 人銀行 / 20 人 startup）跑一次，看哪裡崩
- **學術 case generation**：給 Pilot Study 預演用
