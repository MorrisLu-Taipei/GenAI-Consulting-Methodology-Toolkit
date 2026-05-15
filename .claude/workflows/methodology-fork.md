# /methodology-fork

> Claude Code-Native — 客戶特化分叉 (Client-Specific Methodology Fork)
> 用途：把標準方法論**分叉**為某客戶的客製版。每個 Tool、每個 Stage、每個門檻**全部依該客戶限制重寫**，獨立存活、不污染標準。把方法論從「一份標準」進化為「**標準 + N 個衍生**」。
>
> 為什麼只有 Claude Code 能做：1M context 一次裝下整個方法論 + 對單一客戶 deep customize + 跨檔同步改寫 + 維持衍生版內部一致性。

## 步驟 1：定義 fork 範圍

請使用者提供（缺一不可）：

```text
- 客戶名稱（會作為 fork 識別碼，例：fork-mingchang）
- 產業 / 規模 / 起點 L 級
- 不可動限制（預算 / 合規 / 部署 / IT FTE）
- 客戶 Ideal Practice 定義表（若已有 Phase B 成果）
- 客戶獨有的痛點 / 業務模式（如：半導體封測廠 vs 區域銀行差異）
- 簽 fork 的負責人（必須有人 own）
```

## 步驟 2：規劃 fork 目錄結構

不污染標準方法論。產出獨立的 fork 目錄：

```text
forks/
└── fork-[客戶識別碼]/
    ├── README.md                    # fork 元資料（誰簽、為何、與標準的差異摘要）
    ├── DIVERGENCE.md                # 與標準方法論的所有差異點清單
    ├── 01_Assessment/
    │   ├── AI_MATURITY_QUESTIONNAIRE_[客戶].md   # 客製化問卷
    │   ├── BARS_RUBRICS_[客戶].md                # 客製化 BARS 行為錨點
    │   └── ...
    ├── 03_Consulting_Report/
    │   ├── CONSULTING_REPORT_TEMPLATE_[客戶].md  # 客製化報告模板
    │   ├── CONSULTING_TOOLKIT_TEMPLATES_[客戶].md
    │   └── ...
    └── ...
```

**鐵則**：fork 目錄完全獨立，**不能改標準方法論的任何檔案**。

## 步驟 3：跨檔客製化（依客戶限制）

對標準方法論的每個關鍵檔案，產出客戶版：

### 範例：fork-mingchang（製造業 700 人 + 預算 800 萬 + 製程地端）

| 標準檔案 | 客戶 fork 版本的差異 |
| --- | --- |
| `AI_MATURITY_QUESTIONNAIRE.md` 10 題 | 加 5 題製造業專屬（製程資料分級、不良率 KPI、客訴根因系統）|
| `BARS_RUBRICS.md` 構面 C 流程自動化 | 3 分門檻加入「製程資料在地端」「跨產線 SOP 統一」|
| `CONSULTING_TOOLKIT_TEMPLATES.md` Tool 2.1 RM 選用 | 強制必選 SCOR + APQC + Tiger AI L1-L5；移除 ITIL / CMMI / eTOM 等不適用的選項 |
| Tool 6.3 組織吸收力 | 預算上限改 800 萬；IT FTE 上限 2；加「製程地端維運成本」維度 |
| Tool 6.2 Stage Gate Criteria | L3 Gate 加「製程異常通報自動化 ≤ 1hr」；L4 Gate 加「品保 Reviewer 雙簽機制」|
| `CONSULTING_REPORT_TEMPLATE.md` §4 RM | 雷達只畫 SCOR + Tiger AI（移除其他 RM）|
| `04_Scenarios/SAMPLE_CLIENT_CASE_MANUFACTURING.md` | 替換為**真實的明強封測案例**（若有 NDA）或保持 AI-simulated 但標明為「基於 fork-mingchang 量身打造的範例」|
| `06_Delivery/ENGAGEMENT_LIFECYCLE.md` 3 階段合約 | Phase A 2 週 NT$ 80 萬、Phase B 4 週 NT$ 200 萬、Phase C 24 月 NT$ 700 萬（具體數字鎖定）|

## 步驟 4：產出 `DIVERGENCE.md`

**完整列出與標準的所有差異**：

```text
# fork-[客戶] 與標準方法論的差異清單

## Stage 1 As-Is
- 訪談題庫加 5 題：[題目]
- Inventory 表加欄位：[欄位]

## Stage 2 Reference Model
- 強制 RM：SCOR + APQC + Tiger AI L1-L5
- 移除選項：ITIL / CMMI / eTOM

## Stage 3 Best Practice
- 對標案例只用：[案例 A]、[案例 B]、[案例 C]
- 排除案例：[案例 X]（不適用）

## Stage 4 Gap Analysis
- M/B/R 分類加產業特化 tag：[製程 / 品保 / 客訴]

## ... 其餘 Stage ...

## 為什麼這樣 fork
- 限制 1: ___ → 導致改動 ___
- 限制 2: ___ → 導致改動 ___

## fork 的維護紀律
- Owner: [人名]
- 升級頻率：依 Phase C 每季 Gate C
- 與標準同步的條件：若標準有 major version 升級，需評估是否回 backport
```

## 步驟 5：產出 fork 的「兼容性報告」

```text
## fork 與標準的兼容性

### 完全相容（標準改動會自動套進 fork）
- Tool 8.7 Audit Log 規格
- Tool 8.9 Evidence Hierarchy
- ...

### 部分相容（標準改動需評估後決定要不要套）
- Tool 6.3 組織吸收力評估
- BARS 行為錨點

### 完全不相容（fork 已自主決定，不接受標準更新）
- Stage 6 Phase 1/2/3 預算上限
- Reference Model 選用清單

### 升級到下個標準版本時的決策樹
若標準 v3.1.0 出來：
- 改 Tool A → fork-mingchang 自動採用
- 改 Tool B → fork-mingchang 評估後決定（誰評估、何時、依據）
- 改 Stage X → fork-mingchang 不採用（已自主）
```

## 步驟 6：給標準方法論的**反饋**

fork 的客製化過程往往會暴露**標準方法論的盲點**。產出反饋清單：

```text
## fork-[客戶] 過程中暴露的標準方法論問題

### 應該回 backport 到標準的改進
1. Tool 2.1 RM 選用清單應加「強制必選」紀律 → 建議回標準
2. BARS 構面 C 3 分門檻太鬆 → 建議標準也收緊
3. ...

### 暴露的標準方法論盲點（不是 bug，是預設）
1. 標準預設客戶有 ≥ 1 IT FTE，但有些 fork 客戶 IT 完全外包
2. 標準預設客戶能跑 6 週 Phase A，但有些 fork 客戶高峰期只有 2 週
3. ...

### 對 Codex `/harvest-insights` 的 input
（fork 累積到 5+ 個後，可請 Codex 跨 fork 找共通模式 → 反向寫回標準）
```

## 紀律

- **fork 完全獨立**：不能修改標準方法論任何檔案
- **每個改動都要有理由**：DIVERGENCE.md 每條都要寫「為什麼改」+ 「依據哪個限制」
- **可追溯回標準**：每個客製檔頂部要標明「fork 自標準 v3.0.0」+ Git commit hash
- **明確 owner**：fork 必須有人 own，沒人 own 就不要 fork
- **時間限定**：fork 預設 24 個月有效（即合約期），到期後評估是 sunset / 升級 / 合併回標準

## 典型應用場景

- **大客戶 Phase B 結尾**：客戶簽完 Ideal Practice，立刻 fork 一份方法論給該客戶
- **產業專屬版**：金融 fork / 醫療 fork / 政府 fork —— 把產業專屬限制鎖在 fork 內
- **學術研究**：研究 5 家不同產業的 fork 差異 → Pilot Study 的具體切入點
- **合作夥伴**：跟撼訊 PowerColor / AMD 合作時 fork 一份硬體優先版
- **配合 Codex `/methodology-test`**：用 fork 跑邊界測試（fork 客戶就是極端 case）
- **長期演化**：5+ 個 fork 累積後，跨 fork pattern 反饋回標準 → 標準愈來愈穩
