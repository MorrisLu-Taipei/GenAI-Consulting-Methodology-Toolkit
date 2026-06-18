# 一篇 Advanced RAG 論文是怎麼由人類與 AI 共同完成的

> 文件版本：v1.1.1  
> 日期：2026-06-06  
> Owner：MORRIS LU / YEH HSING LU, TigerAI Founder  
> 文件類型：情境故事 / SOP companion  
> 案例來源：`C:\Tools\@@@@@@Antigravity\TigerAI-投稿\RAG-Paper-2026`

---

## 序幕：論文不是從 AI 的提示詞開始

Morris 並不是先對 AI 說：「幫我寫一篇 RAG 論文。」

事情的起點，是他在做 Advanced RAG 產品時反覆遇到一個現實問題：

> 企業把勞動法規、HR 手冊、SOP、產品規格書放進一般 RAG，系統雖然能回答問題，卻常常找錯段落。固定長度切分會把條文切斷，扁平關鍵字會把不同層次的概念混在一起，而神經網路 reranker 又增加 GPU、模型與維護成本。

這一段只能由 Morris 提出。

AI 沒有服務過 TigerAI 的客戶，不知道企業導入時真正在哪裡卡住，也不知道哪些問題值得 TigerAI 花半年研究。AI 可以閱讀文件、整理問題，但它不能替 Morris 決定「這是不是一個值得研究的真實問題」。

這就是第一條邊界：

> **研究問題源自人類面對真實世界的觀察；AI 可以幫忙把觀察變成可研究的問題，但不能反過來製造研究需求。**

---

## 第一幕：從產品想法變成研究問題

Morris 把初步想法交給 AI：

- 文件應依條、款、項或文件結構切分，而不是固定 512 tokens。
- 關鍵字應區分 L1、L2、L3 語意層次。
- 查詢與 chunk 應在同一層比對。
- reranking 不一定要再部署一個模型。
- 不是所有問題都要走 RAG，一般對話可以直接交給 LLM。

AI 的工作不是說「這太創新了」，而是把想法拆成可被否證的候選研究問題：

- **RQ1：** 規則驅動切分是否比固定切分改善結構化文件的檢索品質？
- **RQ2：** L1/L2/L3 同層比對是否降低廣義關鍵字造成的錯誤召回？
- **RQ3：** 零模型加權重排能否在不使用 neural reranker 的條件下，維持可接受的檢索品質與較低部署成本？
- **RQ4：** 以階層關鍵字作為 RAG / direct LLM 路由訊號，是否能降低無關檢索與虛假引用？

AI 還提出十幾個聽起來很厲害的題目，例如「建立全新的領域語意本體」或「取代傳統 Hybrid RAG」。

Morris 沒有全部接受。他問：

1. 我們目前的產品真的做到這些事了嗎？
2. 哪些功能可以獨立測量？
3. 一篇論文的實驗規模能支持幾個主張？
4. 哪些只是產品語言，不是學術貢獻？

最後由 Morris 決定研究範圍。

這不代表創新只能由人類單獨想出來。Morris 會刻意要求 AI 進行**創新性的文獻搜尋**，不只搜尋「RAG chunking」這種直接關鍵字，也跨到：

- hierarchical classification
- ontology-guided retrieval
- faceted search
- metadata filtering
- legal information retrieval
- edge inference
- query routing
- information granularity alignment

AI 可以透過跨領域搜尋，發現原本沒有被 Morris 放在一起思考的理論、方法與技術組合。例如，AI 可能發現「同層比對」與資訊檢索中的 faceted search、taxonomy-aware retrieval 或 ontology alignment 有相似思想，進而幫助 TigerAI：

- 找到可以借用的理論語言。
- 避免把既有概念誤認為全新發明。
- 發現現有研究尚未處理的組合方式。
- 將產品機制轉化成更清楚的研究假設。
- 提出 Morris 原先沒有想到的實驗或比較基線。

因此 AI 不只是文獻整理員，也可以是**創新探索者與跨領域連結者**。但 AI 搜尋後提出的是「創新候選」，不是已成立的學術貢獻。

真正宣布貢獻之前，仍要完成三個步驟：

1. AI 提出跨領域連結、研究缺口與創新候選。
2. 人類查閱原始文獻，確認相似處、差異與搜尋範圍。
3. Morris 判斷該創新是否符合真實產品、能否實驗驗證，以及是否值得由作者正式主張。

> **AI 可以協助發現創新；人類負責驗證創新、選擇創新，並對創新主張負責。**

**本階段分工：**

| Morris | AI |
| --- | --- |
| 提出產業痛點與產品機制 | 將想法拆成候選 RQ 與可測變項 |
| 決定研究價值與範圍 | 執行跨領域、相鄰概念與反向文獻搜尋 |
| 核准最終 RQ | 提出創新候選、理論連結、研究缺口與新 baseline |
| 對正式貢獻主張負責 | 不得把尚未查證的候選直接宣稱為 novelty 或「首次」 |

---

## 插曲：三個 AI IDE 不是三個聊天視窗

Morris 不把 Antigravity、Claude Code 與 Codex 同時叫來寫三份摘要，再挑一份最好看的。

三個工具在研究流程中有不同職責：

| 工具 | 主要角色 | Advanced RAG 案例中的工作 |
| --- | --- | --- |
| **Antigravity** | 多代理探索與早期診斷 | 同時從 IR researcher、RAG engineer、企業使用者、法規專家與 reviewer 視角找問題 |
| **Claude Code** | 長上下文綜合、理論連結與論證結構 | 跨讀 preprint、研究計畫、文獻矩陣與實驗紀錄，形成 RQ、related work、論證與審稿回覆 |
| **Codex** | 工程實作、可重現性、證據與一致性稽核 | 讀取 `eval/` 程式、修正評估管線、執行測試、建立 traceability、阻止無證據主張進稿 |

它們透過檔案交棒，不靠記憶交棒。

每一個 AI 都只能讀取前一階段已留下的研究產物，再把輸出寫到指定區域。人類則在 Gate 文件中決定接受、修改或拒絕。

---

## 操作場景一：先建立研究工作區

TigerAI Methodology repository 是**研究方法與 Skills 控制庫**：

```text
C:\Tools\@@@@@@Antigravity\TigerAI-Methodology
└── Deliverable\10_Consulting\
    ├── .claude\skills\
    ├── .claude\workflows\
    ├── .codex\workflows\
    ├── .antigravity\workflows\
    └── 09_Research_Paper\
```

Advanced RAG 論文則是**個別研究專案工作區**：

```text
C:\Tools\@@@@@@Antigravity\TigerAI-投稿\RAG-Paper-2026
```

此路徑是本案例實際存在的研究工作區，不是示意路徑。

兩者不應混成同一包。方法論庫管理共用規則，論文工作區保存這篇論文的資料、程式、結果與稿件。

Morris 先要求 Codex 在 `RAG-Paper-2026` 建立以下目錄。實際建立前由人類確認，不覆蓋原有 `eval/` 與 preprint：

```text
RAG-Paper-2026/
├── 00_GOVERNANCE/
│   ├── RESEARCH_BRIEF.md
│   ├── HUMAN_AI_BOUNDARY.md
│   ├── AI_USE_LOG.md
│   └── DECISION_LOG.md
├── 01_PROTOCOL/
│   ├── RESEARCH_QUESTIONS.md
│   ├── EXPERIMENT_PROTOCOL.md
│   ├── BASELINE_CONTROL_MATRIX.md
│   └── CHANGE_CONTROL.md
├── 02_LITERATURE/
│   ├── SEARCH_STRATEGY.md
│   ├── SEARCH_LOG.md
│   ├── LITERATURE_MATRIX.md
│   ├── INNOVATION_CANDIDATES.md
│   └── REJECTED_REFERENCES.md
├── 03_DATA/
│   ├── RAW_READ_ONLY/
│   ├── GOLD_DATASET/
│   ├── ANNOTATION_GUIDE.md
│   └── DATASET_VALIDATION_LOG.md
├── 04_ANALYSIS/
│   ├── runs/
│   ├── figures/
│   ├── ERROR_ANALYSIS.md
│   └── ANALYSIS_DECISION_LOG.md
├── 05_MANUSCRIPT/
│   ├── OUTLINE.md
│   ├── CLAIM_EVIDENCE_MATRIX.md
│   ├── preprint_ZH.md
│   └── preprint_EN.md
├── 06_REVIEW/
│   ├── RED_TEAM_FINDINGS.md
│   ├── CLAIM_AUDIT.md
│   ├── HYPE_SCRUB.md
│   └── REVIEWER_RESPONSE.md
├── 07_RELEASE/
│   ├── SUBMISSION_CHECKLIST.md
│   ├── RELEASE_MANIFEST.md
│   └── REPRODUCIBILITY.md
└── eval/
```

上述 `.md` 檔案是目標研究治理結構，將由後續核准的模板或各研究階段逐步建立；下面的 PowerShell 腳本只建立尚不存在的目錄，不會一次產生所有文件。

若使用 PowerShell，建立空目錄可以由 Codex 提出並執行類似命令：

```powershell
# eval/ 已存在且包含評估程式，本初始化腳本不移動或改寫它。
$folders = @(
  "00_GOVERNANCE", "01_PROTOCOL", "02_LITERATURE",
  "03_DATA\RAW_READ_ONLY", "03_DATA\GOLD_DATASET",
  "04_ANALYSIS\runs", "04_ANALYSIS\figures",
  "05_MANUSCRIPT", "06_REVIEW", "07_RELEASE"
)
$folders | ForEach-Object {
  if (Test-Path -LiteralPath $_) {
    Write-Host "[reused] $_"
  } else {
    New-Item -ItemType Directory -Path $_ | Out-Null
    Write-Host "[created] $_"
  }
}
```

這種寫法不會以 `-Force` 默默掩蓋既有目錄，而是明確列出哪些目錄為新建、哪些沿用。若既有目錄內容與預期不符，Codex 應先回報差異，由 Morris 決定是否繼續。

但建立目錄只是準備工作。Codex 不得自行移動、刪除或改寫原始資料；`RAW_READ_ONLY` 一旦凍結，正式實驗期間只能新增版本，不能偷偷修改舊版本。

接著初始化或確認 Git：

```powershell
git status
git add 00_GOVERNANCE 01_PROTOCOL 02_LITERATURE
git commit -m "chore: initialize Advanced RAG research workspace"
```

Git commit 不是行政工作，而是研究 provenance。每次 protocol freeze、dataset freeze、正式 run 與 submission candidate 都應有可識別的 commit 或 tag。

---

## 操作場景二：Antigravity 先把問題打開

### 為什麼先用 Antigravity

研究剛開始時，問題通常不是資料太少，而是 Morris 腦中同時有產品、客戶、工程與商業經驗。這時太早讓單一 AI 寫 Introduction，容易把第一個說法固定成論文框架。

Antigravity 適合先做多代理診斷。

Morris 在 `RAG-Paper-2026` 開啟 Antigravity，要求它參考：

- `preprint_ZH.md`
- `paper_submission_plan.md`
- `eval/`
- `00_GOVERNANCE/RESEARCH_BRIEF.md`
- TigerAI Methodology 的 `.antigravity/workflows/diagnose.md`

使用情境可以寫成：

```text
/diagnose

主題：TigerAI Advanced RAG 是否能形成可驗證的研究貢獻。

請平行模擬五個角色：
1. Information Retrieval researcher
2. RAG system engineer
3. Enterprise on-premise buyer
4. Traditional Chinese legal-domain evaluator
5. Skeptical peer reviewer

每個角色回答：
- 真正問題是什麼？
- 哪些產品功能可轉成研究假設？
- 哪些主張目前沒有證據？
- 最可能的替代解釋是什麼？
- 需要什麼 baseline、dataset 與 ablation？

只輸出候選診斷，不修改論文。
```

Antigravity 把多代理結果寫成：

```text
00_GOVERNANCE/ANTIGRAVITY_DIAGNOSIS_001.md
```

它可能提出彼此衝突的觀點：

- IR researcher 認為 novelty 不在 L1/L2/L3，而在 granularity-aware metadata retrieval。
- 工程師認為真正價值是不用 neural reranker。
- 企業買家在意的是斷網、GPU 成本與可維護性。
- 法規 evaluator 質疑 gold answer 的版本與法律效力。
- reviewer 認為四個 contribution 太多，應拆成兩篇。

Morris 不要求 Antigravity 自己投票決定。他在 `DECISION_LOG.md` 記錄：

```text
Decision D-001
- 採納：將 C1-C3 留在主研究。
- 暫緩：C4 routing 改列探索性研究，除非能建立獨立測試集。
- 拒絕：不以「完全取代 BM25」作為主張。
- 理由：目前可取得的證據與實驗時間不足以支持更大範圍。
```

### Antigravity 的邊界

- 可以同時產生多種觀點。
- 可以發現衝突與盲點。
- 不負責決定哪個觀點是真的。
- 不直接修改正式 preprint。
- 所有輸出先標記 `AI-Candidate`。

---

## 操作場景三：Claude Code 做創新性文獻搜尋與理論綜合

### 第一次 Claude Code session：建立搜尋策略

Claude Code 讀取 Antigravity 診斷、研究問題與現有參考文獻。Morris 要求它使用 `theory-bridge` 與 `deep-synthesize` 的思路，把 Advanced RAG 與相鄰學術概念連起來。

```text
/theory-bridge

請將 Advanced RAG 的四個候選機制：
1. rule-driven chunking
2. L1/L2/L3 tier-matched retrieval
3. zero-model reranking
4. keyword-aware query routing

映射到相鄰研究領域。不要只搜尋 RAG 關鍵字。
至少探索 ontology-guided retrieval、faceted search、
hierarchical classification、information granularity、
rule induction、legal IR、edge inference、query routing。

輸出：
- 概念橋接表
- 建議搜尋式
- 可能相似研究
- 可能反駁 novelty 的研究
- 可形成的新 baseline

不得把任何候選文獻直接列入正式 References。
```

接著：

```text
/deep-synthesize

讀取：
- 02_LITERATURE/SEARCH_LOG.md
- 02_LITERATURE/LITERATURE_MATRIX.md
- 02_LITERATURE/INNOVATION_CANDIDATES.md
- 00_GOVERNANCE/ANTIGRAVITY_DIAGNOSIS_001.md

請形成三種可能的論文定位：
A. chunking 方法論論文
B. granularity-aware retrieval 論文
C. edge-deployable RAG system 論文

比較各定位需要的證據、風險與適合 venue。
```

Claude Code 的價值在於跨很多文件做長上下文綜合，但它不能因為讀了很多檔案，就自動取得學術判定權。

Morris 對每一筆創新候選標記：

```text
Candidate IC-003
- AI proposal：L1/L2/L3 可重新定義為 granularity-aware retrieval。
- Source status：待查證。
- Human decision：有潛力，進入原文閱讀。
- Required evidence：至少查核 faceted search、ontology retrieval、
  hierarchical IR 與 metadata filtering 文獻。
```

### Claude Skills 如何使用

目前方法論庫中的 Claude Code Skills 包含：

- `/claim-audit`
- `/hype-scrub`
- `/reviewer-response`

Skills 與一般 prompt 不同：Skill 是可重複使用的工作規格，定義輸入、步驟、輸出與禁止事項。

如果 Claude Code 以 `Deliverable/10_Consulting` 為專案根目錄開啟，這些 Skills 可從 `.claude/skills/` 被發現。若在獨立的 `RAG-Paper-2026` 開啟，應採其中一種治理方式：

1. 將經核准版本的 Skill 複製到該專案 `.claude/skills/`，並記錄來源版本。
2. 明確要求 Claude 讀取方法論庫中指定的 `SKILL.md` 後執行。
3. 將共用 Skills 發布為受版本管理的 plugin，再由研究專案安裝固定版本。
4. 將通用 Skill 放在使用者層級 `~/.claude/skills/`，供多個研究專案共同使用；release manifest 仍須記錄 Skill 名稱、內容版本或來源 commit，避免使用者層級內容更新後無法重現。

不得口頭說「用最新版 Skill」卻不記錄版本。研究 release 應在 manifest 中寫明使用的 Skill 路徑與 commit。

另外，`/claim-audit`、`/hype-scrub`、`/reviewer-response` 位於 `.claude/skills/`，屬 Claude Code 可原生發現的 Skills；`/theory-bridge`、`/deep-synthesize` 等則位於 `.claude/workflows/`，是本 repository 保存的 workflow 規格。後者若未被目前工具自動註冊為 slash command，使用者應明確要求 Claude 讀取對應的 `.md` 後執行，而不是假設兩者具有完全相同的發現與觸發機制。

---

## 操作場景四：Codex 把研究設計變成可執行實驗

Claude Code 完成理論定位後，Codex 接手工程與證據。

Codex 先讀：

- `01_PROTOCOL/EXPERIMENT_PROTOCOL.md`
- `01_PROTOCOL/BASELINE_CONTROL_MATRIX.md`
- `03_DATA/ANNOTATION_GUIDE.md`
- `eval/chunkers.py`
- `eval/retrievers.py`
- `eval/dataset.py`
- `eval/metrics.py`
- `eval/judge.py`
- `eval/run_eval.py`

### 先診斷，不急著改程式

```text
請依 .codex/workflows/diagnose.md 診斷 eval/。

重點：
- B1-B5 是否只改變預定變項？
- 是否有 dataset leakage？
- metric 實作是否符合定義？
- LLM-as-judge 是否可重現？
- random seed、model version、top-k 是否固定？
- results.csv 是否足以追溯每一題與每一 baseline？

先輸出 06_REVIEW/EVAL_DIAGNOSIS.md，不修改程式。
```

Morris 看完診斷，批准修改範圍後，Codex 才能：

- 補固定參數。
- 增加 run manifest。
- 保存每題 retrieved chunk IDs。
- 讓失敗 API call 不會被誤記成 0 分。
- 增加人工抽查輸出。
- 加入測試，確認 metrics 計算。

### 建立主張與證據追溯

Codex 使用 `generate-traceability` workflow，把論文主張接到實際證據：

```text
請依 .codex/workflows/generate-traceability.md 建立：
05_MANUSCRIPT/CLAIM_EVIDENCE_MATRIX.md

每列包含：
- Claim ID
- 論文主張
- 所需證據
- 實際來源檔
- run ID / commit
- 目前狀態
- 人類核准者
```

例如：

| Claim ID | 主張 | 證據 | 狀態 |
| --- | --- | --- | --- |
| C-RAG-01 | 規則切分改善 P@5 | 正式 run 的 B1/B3/B5 結果 | 待實驗 |
| C-RAG-02 | 同層比對降低誤召回 | B3/B5 錯誤分析 | 待實驗 |
| C-RAG-03 | reranker 為 O(n) | 演算法定義與 benchmark | 部分驗證 |
| C-RAG-04 | 適合 edge deployment | 資源量測與無模型依賴 | 不足 |

只要狀態不是 `Source-Verified`，Codex 在 claim audit 時就必須攔下。

### 正式實驗的 Gate

Morris 簽核 `EXPERIMENT_PROTOCOL.md` 後：

```text
Protocol status: FROZEN
Protocol version: v1.0.0
Dataset version: labor-law-qa-v1.0.0
Approved by: Morris Lu
```

Codex 才執行正式 run。每次輸出放在獨立目錄：

```text
04_ANALYSIS/runs/2026-06-XX_run-001/
├── config.json
├── environment.txt
├── results.csv
├── results_summary.csv
├── retrieved_chunks.jsonl
├── errors.log
└── RUN_MANIFEST.md
```

Codex 可以計算，但結果解讀仍由 Morris 決定並記錄在 `ANALYSIS_DECISION_LOG.md`。

---

## 操作場景五：三個 AI 依序審稿，而不是互相附和

初稿完成後，執行三層審查。

### 第一層：Antigravity 多角色審查

```text
/generate-report

請將 preprint 模擬送給：
- IR reviewer
- applied AI reviewer
- enterprise systems reviewer
- reproducibility reviewer

每位 reviewer 獨立評分：
novelty、method、evidence、reproducibility、clarity。
不得共同協調答案。
```

輸出到：

```text
06_REVIEW/ANTIGRAVITY_REVIEW_ROUND_1.md
```

### 第二層：Claude Code 論證與語言審查

Claude 先用長上下文理解整篇，再執行：

```text
/claim-audit
稽核 05_MANUSCRIPT/preprint_ZH.md。
特別檢查「首次、有效、提升、取代、O(1)、競爭性、
適合 edge、文獻空白」等主張。
```

```text
/hype-scrub
場域是 peer-reviewed research paper。
保留已定義術語，清除沒有證據的最高級與產品宣傳語言。
```

### 第三層：Codex 程式與證據審查

```text
請依 .codex/workflows/red-team-review.md，
交叉檢查 preprint、CLAIM_EVIDENCE_MATRIX、eval/ 與正式 run。

優先回報：
- 稿件數字與 CSV 不一致
- 稿件描述的方法與程式實作不一致
- baseline 不公平
- 引用或 novelty 未驗證
- 缺失測試與不可重現設定
```

再執行 `consistency-review`，確認中英文稿、表格與摘要數字一致。

三層審查的輸出不能自動合併進論文。Morris 透過 revision matrix 逐項裁決：

| Finding | 來源 | 決定 | 實際修改 | 核准 |
| --- | --- | --- | --- | --- |
| F-021 | Codex | 接受 | 降低 O(1) 主張 | Morris |
| F-022 | Claude | 接受 | 移除「首次」 | Morris |
| F-023 | Antigravity | 部分接受 | C4 移至 future work | Morris |

---

## 操作場景六：收到真實審稿意見後

Morris 把 reviewer comments 存成：

```text
06_REVIEW/REVIEWER_COMMENTS_RAW.md
```

Claude Code 使用 `/reviewer-response` Skill：

```text
/reviewer-response

讀取：
- REVIEWER_COMMENTS_RAW.md
- submission version
- current revised version
- revision matrix

產生逐點回覆草稿。
凡是無法從 diff、實驗結果或檔案證明的修改，
一律列入「需作者確認」，不得宣稱已完成。
```

Codex 接著核對 response letter 中每個「已修改」：

- 檔案是否真的改了。
- 頁碼與行號是否正確。
- 新實驗是否真的有 run manifest。
- 新增數字是否能回到 CSV。

最後由 Morris 決定回覆語氣、是否同意 reviewer，以及是否真的送出。

---

## 操作場景七：Release 前的固定順序

正式提交候選版不得由任一 AI 單獨發布。建議順序如下：

1. Codex 執行測試、重跑可重現性與 consistency review。
2. Claude Code 執行最後一次 claim audit 與 hype scrub。
3. Antigravity 不再發散新方向，只做獨立角色的最後閱讀。
4. Morris 人工通讀全文、圖表、引用與限制。
5. 凍結 `RELEASE_MANIFEST.md`。
6. 建立 Git tag，例如 `rag-paper-v1.0.0-submission`.
7. 人類登入投稿系統並送出。

`RELEASE_MANIFEST.md` 至少記錄：

- manuscript commit
- dataset version
- experiment run IDs
- model/API versions
- Skills/workflows 路徑與 commit
- AI use log
- 已知限制
- 作者簽核

---

## 三個工具的禁止越界表

| 工具 | 不得做的事 |
| --- | --- |
| Antigravity | 不得以多數代理同意取代證據；不得自動決定研究方向 |
| Claude Code | 不得把長上下文綜合誤當成來源查證；不得虛構引用或結果 |
| Codex | 不得因程式能跑就判定研究設計有效；不得擅改 protocol、gold data 或排除規則 |
| 三者共同 | 不得自行投稿、署名、宣稱實驗完成或替作者承擔責任 |

最理想的接力方式是：

> **Antigravity 打開可能性，Claude Code 建立知識與論證，Codex 把主張鎖到程式與證據，Morris 在每一道 Gate 做決定並承擔責任。**

---

## 第二幕：AI 找文獻，人類確認世界上真的有這些文獻

Morris 要求 AI 進行兩層文獻搜尋。

第一層是**驗證性搜尋**：搜尋 adaptive chunking、hierarchical taxonomy、hybrid retrieval、lightweight reranking、legal RAG 等直接相關研究，確認既有方法與比較基線。

第二層是**創新性搜尋**：刻意離開原本的 RAG 用語，探索 ontology-guided retrieval、faceted search、information granularity、rule induction、edge retrieval、query routing 等相鄰領域，尋找可以重新組合的概念與尚未被連接的研究缺口。

AI 快速建立候選文獻表，也提出新的理論連結與研究設計。這些結果可能真正擴展 Morris 的原始構想，而不只是替既有想法找支持資料。

幾分鐘後，它回報：

> 「目前沒有論文做過 L1/L2/L3 同層比對，因此這是文獻空白。」

這句話不能直接進論文。

「AI 沒找到」不等於「世界上不存在」。搜尋關鍵字可能不完整，論文可能使用 taxonomy-aware retrieval、hierarchical filtering、faceted search 或 ontology-guided retrieval 等不同名稱。

因此 Morris 要求 AI：

1. 列出搜尋資料庫、日期、關鍵字與同義詞。
2. 把每篇候選文獻的 DOI、作者、年份與原始連結列出。
3. 將「支持我們」、「與我們相似」及「可能反駁我們」分開。
4. 把查不到原始來源的條目放進拒絕清單。

接下來，人類閱讀最關鍵的原文，確認論文實際做了什麼。只有完成這一步，才能把：

> 「本文首次將階層概念應用至 RAG 檢索。」

改寫成相稱且可防守的版本，例如：

> 「在本研究截至特定日期所檢索與查證的文獻範圍內，我們尚未發現以同層關鍵字比對結合結構化 metadata filter 的相同設計。」

若後來找到相似研究，論文不是失敗，而是要重新說清楚 TigerAI 方法的差異。

**本階段邊界：**

- AI 可以找候選文獻，不能保證查全。
- AI 可以摘要，但摘要不能代替人類閱讀關鍵原文。
- AI 不得虛構 DOI、作者或研究結果。
- novelty 最終由作者依可重現搜尋紀錄負責。

---

## 第三幕：把產品變成一場公平實驗

現在最大的誘惑，是直接拿 TigerAI Advanced RAG 跟一個很弱的 Naive RAG 比較。這樣很容易得到漂亮數字，卻不能證明是哪個設計產生效果。

AI 提出五個 baseline：

- B1：固定切分、向量檢索。
- B2：固定切分、BM25 加向量。
- B3：規則切分、扁平關鍵字。
- B4：語意切分、同層比對。
- B5：規則切分、同層比對、零模型重排。

Morris 與研究人員必須檢查：

- 各系統是否使用相同文件、embedding model、top-k 與生成模型。
- B3、B4、B5 是否只有預定變項不同。
- TigerAI 系統是否得到 baseline 沒有的額外人工資訊。
- L1/L2/L3 字典是否由測試問題反向調整，造成資料洩漏。
- 加權公式 `L3×3 + L2×2 + L1×1` 是事前固定，還是看過結果後挑出來的。
- 路由 C4 是否有獨立測試集與錯誤類型，而不是只用產品 demo 證明。

AI 可以模擬 reviewer，指出設計漏洞；但最終研究 protocol 必須由人類凍結。

凍結後才開始跑正式實驗。若看完結果才更換問題、權重或排除失敗案例，必須留下變更理由，不能假裝一開始就是這樣設計。

---

## 第四幕：50 題資料集究竟是誰做的

目前專案中有 50 題勞動法規問答，分為 factual、inference 與 multi-hop，程式註解稱為「人工標注問答集」。

但在學術上，「檔案裡有 50 題」不等於「已完成可靠的人工標注」。

假設實際流程是：

1. AI 先根據法規產生 80 題候選問題。
2. Morris 刪除太簡單、重複或不符合企業情境的題目。
3. 研究助理依官方法規逐題核對答案與 supporting articles。
4. 第二位標注者獨立檢查其中一部分。
5. 有爭議的題目交由具法規知識的人裁決。
6. 最後凍結 50 題正式測試集。

那麼論文應誠實寫成：

> 「候選題由 AI 輔助產生，經人類依官方法規逐題查證、修訂與核准後形成測試集。」

只有在人類真的逐題驗證並留下紀錄後，才可以說它是 human-validated dataset。若沒有第二位標注者，就不能暗示已做 inter-annotator agreement。

更重要的是，法律問答涉及高風險內容。AI 產生的金標答案可能引用錯誤條文、混入已修法內容，或把法律解釋寫得比法條更確定。這些都必須由人類對照特定版本的官方法規。

**這一幕最清楚的分工是：**

| 工作 | AI | 人類 |
| --- | --- | --- |
| 產生候選題 | 可以 | 審查使用情境 |
| 建議答案與條文 | 只能當候選 | 必須查官方來源 |
| 題型分類 | 可以初分 | 核准標準 |
| 金標答案 | 不得自行定稿 | 人類簽核 |
| 宣稱人工標注 | 不得自行宣稱 | 必須有真實流程與紀錄 |

---

## 第五幕：讓機器跑實驗，但不讓機器替結果說故事

研究 protocol 凍結後，AI 協助工程化評估：

- 建立 B1 到 B5 的索引。
- 對每題執行檢索。
- 計算 P@3、P@5、Recall@5 與 MRR。
- 生成 `results.csv` 與 `results_summary.csv`。
- 保存模型、參數、套件版本、隨機種子與執行時間。

這些是 AI 與程式最擅長的部分：一致、重複、不厭其煩。

但程式輸出一個較高的 P@5，不代表論文已證明 TigerAI 方法比較好。人類還要問：

- 差異有多大？
- 是否在不同題型都成立？
- 是否只是某幾題造成平均數上升？
- 是否有統計或實務意義？
- AnswerScore 使用 LLM-as-judge 時，judge 是否偏好某種回答風格？
- 若更換 embedding model 或字典，結果是否穩定？
- 哪些案例 TigerAI 反而輸給 baseline？

AI 可以列出錯誤案例與可能解釋，但不能自己挑一個對產品最有利的故事。

若結果顯示：

- 規則切分有效；
- 同層比對只在 factual 題有效；
- 零模型重排沒有顯著改善；
- C4 尚未有足夠資料評估；

人類必須照實寫。這時候正確的結論可能不是「四項創新全面成功」，而是：

> 規則切分在本資料集呈現穩定改善；同層比對的效果依查詢類型而異；啟發式重排與查詢路由仍需要更大規模驗證。

負面結果不是產品失敗，而是下一版產品與研究設計的輸入。

---

## 第六幕：AI 可以寫初稿，但不能把空白變成證據

AI 根據核准的大綱開始寫稿。它很快生成一個流暢摘要：

> 「TigerAI RAG 在 Precision@5 提升 28%，MRR 提升 21%。」

如果正式實驗還沒有跑完，這兩個數字就是捏造。

正確做法是保留：

> `Precision@5 提升 [X]%，MRR 提升 [Y]%。`

或在投稿前直接刪除結果句，直到 `results_summary.csv` 已產生、計算方式已核對、人類已批准。

同樣地，下列句子都要經過 Gate：

- 「有效降低誤召回率」需要實驗支持。
- 「O(n)」需要明確定義 n 與實作範圍。
- 「Qdrant payload lookup 為 O(1)」不能只靠直覺，需要依實際索引與官方技術資料精確表述。
- 「廣泛需要」與「未見系統化設計」需要文獻或調查依據。
- 「填補繁體中文文獻空白」需要可重現的文獻搜尋。
- 「達到競爭性檢索品質」必須在結果完成後才可保留。

AI 的初稿一律標記為 `AI-Candidate`。經來源核對後是 `Source-Verified`，經 Morris 通讀並願意在審稿現場親自辯護後，才是 `Author-Approved`。

---

## 第七幕：AI 不只是寫手，也要成為反對者

第一版完成後，換另一個 AI 扮演最嚴格的 reviewer：

> 「L1/L2/L3 taxonomy 是人工建立還是自動建立？成本是否被忽略？」  
> 「同一資料集同時用來設計字典與測試，是否有 leakage？」  
> 「50 題足以支持跨領域泛化嗎？」  
> 「為什麼不與 neural reranker 比較？」  
> 「C4 是研究貢獻，還是產品 routing rule？」  
> 「LLM-as-judge 是否經過人類校準？」  
> 「法律資料的版本與有效日期是什麼？」

AI 的任務是把論文打痛，不是替作者辯護。

Morris 逐項決定：

- 補實驗。
- 補文獻。
- 降低主張。
- 移到 limitations。
- 暫時拿掉 C4，留待下一篇。
- 保留不同意見並提出理由。

AI 可以提出修法，但不可以在 Morris 不知情的情況下，偷偷把「我們證明」改成另一個仍然無證據的說法。

---

## 第八幕：選擇投稿地點，是研究策略，不是 AI 排名遊戲

AI 可以整理 EMNLP System Demo、ROCLING、TAAI 或期刊的範圍、頁數、審查重點與期限。

但投稿選擇仍由人類決定，因為它涉及：

- 論文目前的證據成熟度。
- 是否偏系統 demo、IR 方法或應用研究。
- 團隊能否在期限前完成資料查證與實驗。
- 是否已經把同一稿件投到其他 venue。
- 產品機密、開源範圍與學術揭露的平衡。

AI 不能因為某期刊 Impact Factor 高，就判定它最適合；也不能保證接受率或投稿日期仍然正確。送出前必須由人類查看 venue 官方網站與投稿規則。

---

## 第九幕：審稿人要求補實驗

審稿人回覆：

> 「目前只用一份勞動法規資料，無法支持 domain-specific documents 的一般化主張。請增加 HR 手冊或產品規格書。」

AI 將意見拆成：

- 核心問題：外部效度不足。
- 可選回應 A：新增兩個領域資料集。
- 可選回應 B：縮小論文主張，只聲稱繁體中文法規文件。
- 可選回應 C：說明資源限制，將跨領域驗證列為未來工作。

Morris 根據時間、資料合法性與研究價值作決定。

若團隊沒有補做實驗，AI 絕對不能生成：

> 「我們已依建議新增 HR 與產品型錄實驗。」

它只能協助寫出真實回覆：

> 「我們同意原稿的一般化語氣超出目前證據，因此已將主張限縮為繁體中文結構化法規文件，並在限制章節明確加入跨領域驗證需求。」

---

## 終幕：誰是作者

最終定稿前，Morris 關掉 AI 對話視窗，獨自從頭讀一次論文。

他必須能回答：

- 為什麼這個問題值得研究？
- 每一個 RQ 是怎麼來的？
- 50 題資料如何產生與驗證？
- baseline 是否公平？
- 每個指標怎麼計算？
- 哪些結果支持哪些主張？
- 哪些地方還不能確定？
- 為什麼選擇這個 venue？
- 若審稿人質疑，自己能不能解釋？

如果其中任何一題只能回答「因為 AI 這樣寫」，論文還不能送出。

AI 可以在 Git 歷史或 AI use log 中被如實記錄，但作者仍是 Morris 與實際做出學術貢獻、願意承擔責任的人類研究者。

---

## 這個案例的最終分工圖

| 研究環節 | 人類主責 | AI 主責 | 最終 Gate |
| --- | --- | --- | --- |
| 產業問題 | 真實觀察、研究價值 | 整理與追問 | Morris 核准問題 |
| 研究問題 | 取捨與可證偽性 | 產生候選 RQ | RQ freeze |
| 文獻 | 讀原文、判斷差異 | 搜尋、聚類、摘要 | authenticity gate |
| 方法 | 公平性、倫理、範圍 | 模擬設計與 reviewer | protocol freeze |
| 資料集 | 法規查證、金標簽核 | 候選題與格式整理 | human validation |
| 實驗 | 決定解讀與限制 | 執行、計算、重現 | result verification |
| 寫作 | 主張、責任、作者聲音 | 草稿、重組、潤稿 | author approval |
| 審查 | 採納或反駁意見 | red-team、逐點整理 | revision sign-off |
| 發表 | 投稿與公開責任 | 格式、版本與 metadata | human release |

---

## 一句話總結

> **Morris 提出 Advanced RAG 為什麼值得研究；AI 幫忙把它變成可搜尋、可實驗、可反駁、可撰寫的研究工程；但只有真實資料、外部來源與人類判斷，能把一份流暢草稿變成一篇可以署名負責的論文。**
