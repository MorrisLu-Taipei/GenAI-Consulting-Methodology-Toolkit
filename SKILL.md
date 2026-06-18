---
name: tigerai-consulting-methodology
description: TigerAI P1 顧問方法論與研究交付規範。用於企業 AI 轉型診斷、L1-L5 導入、顧問報告、研究論文從 Zenodo DOI 到 arXiv 與期刊投稿、版本治理，以及生成圖片的本機保存與路徑回報。
---

# TigerAI Consulting Methodology Skill

本目錄包含了**企業 AI 轉型成熟度診斷與導入方法論工具包**。

進行 L1-L5 成熟度說明、客戶教育、主管簡報或非技術溝通時，優先讀取：

- `01_Assessment/AI_MATURITY_SCORING_MODEL.md`
- `01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`

上述文件定義企業情境的正式評分、交付物、Evidence 與 Stage Gate；產品名稱不得被直接視為成熟度等級。

## 📍 專案層級與定位 (Project Tier)
- **Tier**: P1 企業部署框架 (Enterprise Deployment Framework)
- **定位**: 這是 TigerAI 的官方核心顧問方法論，用於指導客戶從 L1 (個人探索) 走向 L5 (多智能體協作)。

## 📚 系列雙教練(上下集分工)
本 repo 是「AI-Native 顧問方法論系列」的**下集(Book II:從顧問判斷到專案交付)**，搭配**上集(Book I:顧問思考能力系統)**。系列總入口見 `SERIES_INDEX.md`。兩集各有一個 AI 教練 skill，依任務切換：

| 任務 | 用哪個 skill | 範圍 |
|---|---|---|
| 練「判斷」：會議改寫、畫對角線、L1-L5 能力評分、主管反問 | **`consulting-thinking-coach`(上集)** | Book I |
| 跑「交付」：成熟度診斷、課程配置、八階段報告、交付驗收、Phase A/B/C Gate、專案風險 | **`consulting-delivery-coach`(下集)** | Book II |

> 接力原則:上集把客戶會議變成「判斷 + 對角線」，下集把判斷推進成「可交付、可驗收、可續約」的專案。橋接見 [`22_Bridge_To_Consulting_Delivery.md`](https://github.com/MorrisLu-Taipei/consultant-thinking-framework/blob/main/22_Bridge_To_Consulting_Delivery.md)。

## 🛠️ Antigravity 執行規範
1. **答案先行 (Answer-First)**: 在回答客戶關於策略與診斷的問題時，優先給出清晰的結論，再進行 MECE 的結構化分析。
2. **遵守八階段框架**: 所有顧問建議必須對齊 `CONSULTING_TOOLKIT_TEMPLATES.md` 中定義的八階段 (Stage 1 ~ Stage 8)。
3. **推動 Workflow 互動**: 主動引導使用者使用 `/diagnose` 或是 `/generate-report` 等預設工作流進行互動式諮詢。
4. **報告產出標準**: 產出顧問報告時，必須嚴格遵守 `03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md` 的結構與學理邏輯，切勿隨意省略重要的治理與簽核環節（例如：Risk Register, Stage Gate Criteria）。

## 🖼️ 生成圖片交付規範

使用圖片生成工具建立研究圖、資訊圖、簡報圖或其他視覺素材時，必須遵守以下規定：

1. **必須保存至本機專案**
   - 不得只將圖片留在 Codex、Antigravity 或其他工具的暫存目錄。
   - 生成完成後，必須將圖片複製到目前工作專案內的 `assets/` 目錄。
   - 優先放在對應文件旁的 `assets/`；若沒有明確文件歸屬，放在專案共用的 `assets/generated/`。

2. **必須使用可辨識且版本化的檔名**
   - 檔名至少包含產品或文件名稱、圖片用途與版本號。
   - 建議格式：`{Product_or_Document}_{Purpose}_v{Version}.png`。
   - 不得使用無法辨識用途的隨機雜湊檔名作為正式交付檔。

3. **必須保留原始生成檔**
   - 將正式交付圖複製到專案目錄，不主動刪除工具產生的原始檔。
   - 若後續重新生成，建立新版本檔案；除非使用者明確要求，不覆蓋或刪除舊版。

4. **必須驗證交付結果**
   - 回覆使用者前，確認正式圖片檔案確實存在、檔案大小大於零且版本名稱正確。
   - 圖片若對應特定文件版本，內容與檔名都必須明確標示相同版本。

5. **必須回報完整儲存路徑**
   - 最終回覆必須附上正式圖片的完整本機路徑。
   - 優先提供可點擊的 Markdown 本機檔案連結。
   - 若有多張圖片，逐一列出用途、版本與路徑。

完成條件：

> 圖片已生成、已複製至專案本機目錄、已完成版本化命名、已驗證檔案存在，且已向使用者提供完整儲存路徑，才算完成圖片交付。

## 🧪 AI 原生研究與論文 SOP

處理學術論文、preprint、產業研究、方法論研究或可引用知識製品時，必須先讀取並遵守以下兩份權威文件：

- `09_Research_Paper/AI_NATIVE_RESEARCH_HUMAN_AI_BOUNDARY_SOP_ZH.md`
- `09_Research_Paper/ADVANCED_RAG_HUMAN_AI_RESEARCH_STORY_ZH.md`
- `09_Research_Paper/AI_MATURITY_HUMAN_AI_RESEARCH_STORY_ZH.md`
- `09_Research_Paper/AI_NATIVE_EBOOK_HUMAN_AI_RESEARCH_STORY_ZH.md`
- `09_Research_Paper/AI_NATIVE_EBOOK_STAGE_GATE_HUMAN_AI_TABLE_ZH.md`

第一份定義正式的 12+1 階段、人類／AI 邊界、內容狀態與品質 Gate；第二份示範技術實驗型 Advanced RAG 論文；第三份示範如何以 AI 轉型成熟度理論為題，將研究背景與顧問經驗轉成可反駁、可驗證的理論論文；第四份示範如何把已存在的 AI-Native eBook / Toolkit artifact 轉成 DSR 論文、DOI 版本與後續投稿路線；第五份將 AI-Native eBook 情境轉成 Stage / Gate / 人類與 AI 分工表。若本 Skill 的摘要與上述文件有差異，以較嚴格且版本較新的規則為準。

### 核心責任邊界

人類必須掌握：

- 研究價值、真實問題、研究問題與貢獻範圍。
- 研究倫理、資料合法性、個資、機密與利益衝突。
- 方法、樣本、測量、baseline、排除規則與分析策略的最終選擇。
- 原始資料、金標答案、結果解讀、限制與正式主張。
- 作者資格、作者順序、投稿、審稿回覆與公開責任。

AI 可以協助：

- 驗證性搜尋、創新性搜尋、跨領域連結與反向搜尋。
- 產生候選 RQ、理論橋接、研究缺口、baseline 與反例。
- 整理文獻矩陣、資料格式、候選題、分析程式與圖表草稿。
- 執行實驗、計算指標、建立 traceability 與一致性檢查。
- 撰寫候選草稿、red-team、claim audit、hype scrub 與審稿回覆草稿。

AI 絕對不得：

- 虛構文獻、DOI、作者、頁碼、資料、數字、訪談或實驗結果。
- 把搜尋不到寫成不存在，把候選創新寫成首次或已證明。
- 把 AI 摘要當成已閱讀原文，把相關性寫成因果。
- 擅自修改 protocol、gold data、排除規則或主要評估指標。
- 自行宣布資料已人工驗證、研究倫理已通過或實驗已完成。
- 自行投稿、署名、發布或代替人類作者承擔責任。

核心原則：

> 人類負責研究意圖、真實世界判斷與最終責任；AI 負責擴展搜尋、降低機械負擔、提出反證並加速可追溯的研究迭代。

### 12+1 階段研究生命週期

#### 階段一：研究準備

1. **選題與研究問題**
   - 人類提出真實問題、研究價值、範圍與可證偽性。
   - AI 產生候選 RQ、變項、反例與範圍風險。
   - 產物：`RESEARCH_BRIEF.md`、RQ、非研究範圍。
   - Gate：問題重要、可回答且可取得證據。

2. **文獻搜尋與閱讀**
   - 同時執行驗證性搜尋與創新性搜尋。
   - AI 應跨到相鄰領域、替代術語、反向文獻與可能推翻 novelty 的研究。
   - 人類閱讀關鍵原文，核對作者、年份、DOI、方法與實際結論。
   - 產物：`SEARCH_LOG.md`、`LITERATURE_MATRIX.md`、`INNOVATION_CANDIDATES.md`、`REJECTED_REFERENCES.md`。
   - Gate：核心引用可外部驗證，創新候選已由人類判斷。

3. **研究設計與方法**
   - 人類決定方法、樣本、倫理、baseline、公平性與分析策略。
   - AI 比較方法、模擬 reviewer、尋找 leakage 與設計漏洞。
   - 產物：`EXPERIMENT_PROTOCOL.md`、`BASELINE_CONTROL_MATRIX.md`、分析計畫。
   - Gate：`Protocol Freeze`。

4. **資料收集與整理**
   - 人類確保資料來源、同意、版本、完整性與合法性。
   - AI 只協助去識別化、格式整理、轉錄、缺漏與欄位檢查。
   - 原始資料保存為唯讀版本，不得在正式實驗期間偷偷覆寫。
   - Gate：來源、同意、資料版本與處理紀錄可追溯。

#### 階段二：研究執行

5. **資料分析與驗證**
   - AI 可執行程式、指標、敏感度分析與錯誤整理。
   - 人類決定最終模型、結果意義、替代解釋與異常處理。
   - 保存 config、environment、seed、結果、errors 與 `RUN_MANIFEST.md`。
   - Gate：結果可重跑，負面與不顯著結果未被隱藏。

6. **論文架構與大綱**
   - 人類決定論證順序、核心貢獻與限制。
   - AI 可產生多種大綱與 claim-evidence map。
   - 產物：`OUTLINE.md`、`CLAIM_EVIDENCE_MATRIX.md`。
   - Gate：每個核心主張都有對應證據位置。

7. **撰寫初稿**
   - AI 只能依核准大綱與已存在證據撰寫候選草稿。
   - 尚未完成的結果必須刪除或明確標為 pending，不得填入想像數字。
   - Gate：沒有無來源數字、虛構引用或未驗證的效果宣稱。

#### 階段三：寫作與修訂

8. **修改與潤稿**
   - 執行 red-team、claim audit、hype scrub 與跨章一致性檢查。
   - 人類決定補實驗、降主張、列入限制或有理據地拒絕建議。
   - 產物：`REVISION_LOG.md`、revision matrix。
   - Gate：致命反駁已處理或誠實揭露。

9. **引用與參考文獻**
   - 每條引用必須能在可信原始來源查得。
   - 關鍵主張必須讀原文，不能以 AI 摘要或搜尋片段代替。
   - 不存在、查核失敗或不支持主張的文獻放入拒絕清單。
   - Gate：每條引用可查、每個引述可定位。

10. **圖表與視覺化**
    - 圖表必須可由原始資料與生成程式重建。
    - 不得使用誤導尺度、選擇性區間或與資料不一致的示意圖。
    - 生成圖片另須遵守本 Skill 的本機保存與路徑回報規則。
    - Gate：圖表、caption、原始資料與論文主張一致。

11. **投稿與 venue 選擇**
    - AI 可建立 venue matrix，但不得只依排名或 Impact Factor 推薦。
    - 人類依研究成熟度、讀者、政策、期限、匿名與預印本規則選擇。
    - Gate：venue 適配，政策已由官方網站確認，沒有違規一稿多投。

#### 階段四：投稿與傳播

12. **回覆審稿意見**
    - AI 可拆解意見、產生逐點回覆草稿與 revision matrix。
    - 每個「已修改／已補實驗」都必須由 diff、run manifest 或資料證明。
    - 人類決定接受、部分接受或有理據地不同意。
    - Gate：`Revision Sign-off`。

13. **最終定稿與發表**
    - 作者人工通讀全文、圖表、引用、限制、作者聲明與 metadata。
    - 凍結 commit、tag、dataset、run IDs、Skills/workflows 版本與 release manifest。
    - 只有人類可以登入投稿平台並執行最終送出或 Publish。
    - Gate：`Human Release`。

### 五種內容狀態

研究內容必須依證據成熟度標示：

| 狀態 | 定義 | 可否進正式論文 |
|---|---|---|
| `AI-Candidate` | AI 提出的候選想法、文獻、答案或解釋 | 否 |
| `Human-Reviewed` | 人類已閱讀，但尚未完成外部查證 | 僅限內部草稿 |
| `Source-Verified` | 已由原始來源、原始資料或可重跑分析確認 | 可以 |
| `Author-Approved` | 作者確認論證、用語與責任 | 可以 |
| `Released` | 已凍結 commit/tag/DOI 且可追溯 | 正式公開版本 |

任何內容不得由 `AI-Candidate` 直接跳到 `Released`。

### 三道不可省略的品質閘

1. **Authenticity Gate**
   - 文獻、DOI、作者、數字與外部來源均可查證。
   - AI 找到的內容先進候選區，未查證前不得進 References。

2. **Claim-Evidence Gate**
   - 每個數字、比較、因果、最新、首次、普遍性與效能主張都有相稱證據。
   - 證據不足時必須刪除、降低語氣或標為推論／待驗證設計。

3. **Human Responsibility Gate**
   - 作者能解釋每個核心主張、資料來源、分析方法與研究限制。
   - 無法由人類作者親自辯護的內容不得投稿。

### 多 AI／多 IDE 接力規則

| 工具 | 主要角色 | 禁止越界 |
|---|---|---|
| Antigravity | 多代理探索、早期診斷、獨立 reviewer 視角 | 不得以代理多數決取代證據或決定研究方向 |
| Claude Code | 長上下文綜合、理論橋接、文獻定位、論證與 reviewer response | 不得把長上下文綜合誤當成來源查證 |
| Codex | 工程實作、測試、run manifest、traceability、證據與一致性稽核 | 不得因程式能跑就判定研究設計有效，也不得擅改 protocol 或 gold data |
| 人類作者 | 研究價值、Gate 決策、正式主張、署名與公開責任 | 不得把無法理解或辯護的 AI 內容直接送出 |

標準接力：

> Antigravity 打開可能性 → Claude Code 建立理論與論證 → Codex 將主張鎖到程式與證據 → 人類在每一道 Gate 決策並承擔責任。

同一重大主張至少必須經過：

> `Builder → Critic / Verifier → Human Approval`

多個 AI 透過檔案、版本與 Gate 交棒，不依賴聊天記憶交棒，也不得由單一 AI 自問自答後直接採用。

### 研究工作區與必要紀錄

個別研究專案應至少具備：

```text
Research_Project/
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

所有會影響研究結論、方法或投稿文字的 AI 工作，至少在 `AI_USE_LOG.md` 記錄：

- 日期與人類操作者。
- 工具、模型或 Skill/workflow。
- 輸入資料範圍與任務目的。
- AI 產出檔案或摘要。
- 人類採納、修改或拒絕的決定。
- 外部查證方式。
- 對應 commit、tag 或版本。

聊天紀錄不能作為唯一 provenance。

正式 run 應使用獨立目錄，至少保存：

```text
runs/{date}_{run-id}/
├── config.json
├── environment.txt
├── results.csv
├── results_summary.csv
├── retrieved_chunks.jsonl
├── errors.log
└── RUN_MANIFEST.md
```

Release manifest 至少記錄 manuscript commit、dataset version、run IDs、模型/API 版本、Skill/workflow 路徑與版本、AI use log、已知限制及作者簽核。

### Advanced RAG 案例專用規則

處理 TigerAI Advanced RAG 論文時：

- 產業痛點與研究價值由 Morris Lu 提出並核准。
- C1-C3 為待正式實驗驗證的核心設計。
- C4 在缺乏獨立 in-domain／out-of-domain 測試集與 routing accuracy 前，維持探索性設計。
- B1-B5 必須使用相同文件、embedding model、生成模型與公平的 top-k／參數。
- L1/L2/L3 taxonomy 不得使用正式測試問題反向調整。
- `L3×3 + L2×2 + L1×1` 權重必須事前固定；看過結果後調整需留下 change control。
- 候選題可由 AI 協助產生，gold answer 與 supporting articles 必須由人類對照官方法規簽核。
- 不得在實驗前宣稱提升、競爭性品質、普遍取代 BM25、固定效能複雜度或 edge superiority。
- C4、Open AI Stack、n8n workflow governance 等尚未比較的內容應標為 system design observation 或 future work。
- 中英文稿、PDF、Zenodo metadata、GitHub release 與版本歷史必須一致。

一句話準則：

> 可以讓 AI 幫忙找、整理、比較、計算、寫草稿與挑錯；不能讓 AI 替人類決定研究價值、製造證據、解讀真實世界，或承擔作者責任。

## 📚 研究論文發表流程與 Stage Gate

協助建立、審查或發布研究論文時，必須區分「研究設計預印本」、「完成實驗的正式預印本」與「同儕審查出版物」。取得 DOI 不代表研究已完成，也不代表論文已通過同儕審查。

### Stage 1：研究設計與工作稿

必須完成：

- 明確定義研究問題、研究範圍、待驗證命題與貢獻邊界。
- 完成初步文獻查核，排除不存在、無法驗證或與主張不符的文獻。
- 凍結 baseline、評估指標、消融實驗與資料驗證 protocol。
- 清楚標示尚未完成的實驗、人工驗證與作者名單。
- 不得填寫虛構數據、效果提升比例或未執行的 benchmark。

Gate：

> **Protocol Freeze**：研究方法與結果表結構在觀察正式結果前完成凍結。

### Stage 2：Zenodo 研究設計預印本

可將研究設計工作稿發布至 Zenodo，取得公開時間戳與 DOI，但必須：

- Resource Type 使用 `Publication / Preprint`。
- 狀態明確標示 `Pre-experiment working draft`。
- Description 與 Notes 說明正式實驗與人工資料驗證尚未完成。
- PDF 不得包含 `[X]`、`[Y]`、TODO、TBD 或暗示已有實驗結果的文字。
- 作者、單位、ORCID、授權、版本號與相關軟體 repository 必須一致。
- 軟體 repository 應使用固定 release/tag，並揭露實際公開範圍。
- 先 Reserve DOI 時，可將 DOI 寫回 PDF 後再 Publish。
- 記錄 Concept DOI 與 Version DOI。

Gate：

> **Preprint Release**：作者共同確認內容、授權、未驗證主張與公開責任後，才可 Publish。

### Stage 3：資料集人工驗證

正式論文不得只使用 AI 產生的候選題或候選答案作為金標資料。

必須完成：

- 逐題對照指定版本的官方或可信來源。
- 凍結 question、gold answer、supporting evidence、type 與 difficulty。
- 保存 validation log、爭議紀錄與領域專家裁決。
- 揭露 AI 是否參與候選資料生成。
- 只有完成人工逐題查核後，才可稱為 `human-validated dataset`。

Gate：

> **Human Validation**：領域專家簽核資料集版本與驗證紀錄。

### Stage 4：正式實驗

必須完成：

- 執行所有事前定義的 baseline 與完整系統。
- 執行各核心元件的消融實驗。
- 保存模型、硬體、套件、參數、seed、資料版本與 run manifest。
- 報告失敗 run、例外處理與排除標準。
- 不得故意弱化 baseline 或在看過結果後任意更改主要指標。
- 若調整 protocol，必須留下理由與版本紀錄。

Gate：

> **Reproducible Run**：他人可依公開設定重建相同實驗流程。

### Stage 5：結果驗證與統計分析

正式結果至少應包含：

- 主要 retrieval 與 generation 指標。
- 信賴區間、bootstrap 或適合研究設計的統計比較。
- baseline、完整系統與消融結果。
- latency、資源使用或部署成本宣稱所需的實測環境。
- error analysis、失敗案例與 limitations。
- 結果是否支持、部分支持或否定原始研究命題。

不得只填入漂亮數字而省略變異、失敗案例或不利結果。

Gate：

> **Result Verification**：技術負責人與領域負責人共同確認資料、計算與解讀。

### Stage 6：正式稿與作者確認

必須完成：

- 將摘要、結論與貢獻改寫為由實驗證據支持的版本。
- 移除 working draft、pending experiment 等已不適用敘述。
- 確認每位作者符合實際學術貢獻與責任要求。
- 純執行、行政或工具操作不自動構成作者資格。
- 未達作者資格者應於致謝中具名。
- 揭露生成式 AI 對搜尋、程式、分析或寫作的實際協助範圍。
- 由人類作者核查所有文獻、資料、主張與最終文字。

Gate：

> **Author Approval**：所有作者核准正式稿、作者順序、貢獻聲明與公開責任。

### Stage 7：Zenodo 新版本

實驗完成後，不覆蓋或刪除舊預印本：

- 在原 Zenodo record 建立 `New version`。
- 上傳完成實驗的正式 PDF，例如 `v1.0.0`。
- 更新 Abstract、Description、Notes、Keywords 與版本資訊。
- Concept DOI 持續指向最新版。
- 舊 Version DOI 保持可引用與可追溯。
- 將新舊 DOI 與變更內容寫入 `VERSION_HISTORY.md`。

Gate：

> **Version Integrity**：所有公開版本都可追溯，且每個 DOI 對應固定內容。

### Stage 8：arXiv 投稿

arXiv 是公開預印本平台，不是同儕審查期刊。投稿前必須：

- 完成英文正式稿與適當的 TeX/source package。
- 選擇正確分類，例如 `cs.IR`、`cs.CL` 或實際研究領域。
- 確認帳號 endorsement、技術格式與 moderation 要求。
- 揭露既有 Zenodo preprint，避免被誤認為重複或衝突版本。
- 確認作者、標題、摘要、授權與其他公開版本一致。
- arXiv 接受只代表通過平台技術與內容 moderation，不代表同儕審查錄用。

Gate：

> **arXiv Release**：來源檔可編譯、metadata 一致，且作者同意公開。

### Stage 9：期刊或研討會投稿

每一個 venue 必須個別確認：

- 是否接受已發布於 Zenodo 或 arXiv 的預印本。
- 投稿格式、頁數、匿名規則、資料與程式碼政策。
- 生成式 AI 使用揭露政策。
- 同時投稿、重複出版與版權政策。
- 建議審稿領域、研究範圍與論文類型是否適配。

投稿稿件應依 venue 重新排版，不應直接將 Zenodo PDF 當成所有 venue 的正式稿。

Gate：

> **Submission Approval**：完成 venue policy checklist、作者確認與最終 submission package 檢查。

### Stage 10：審稿、錄用與出版後回填

收到審稿意見後：

- 逐點回覆，不隱藏不利結果或限制。
- 新增實驗時更新 run manifest、資料版本與論文版本。
- 不接受審稿人要求的錯誤引用、誇大主張或不合倫理操作。

正式錄用後：

- 在 arXiv 與 Zenodo 補上 journal/conference reference。
- 補上出版社正式 DOI 與 citation。
- 更新 GitHub README、CITATION、release/tag 與研究頁面。
- 保留 preprint DOI 與出版 DOI 的差異，不將兩者混為同一研究製品。
- 確認出版社允許公開的 manuscript 版本。

Gate：

> **Publication Record Complete**：Zenodo、arXiv、GitHub 與出版社資訊互相連結且版本關係清楚。

### 發表狀態判斷

回答「是否可以發表」時，必須明確說明是哪一種發布：

| 狀態 | 可執行動作 | 不代表 |
|---|---|---|
| 研究設計完成、實驗未完成 | Zenodo working preprint | 已驗證成果、同儕審查 |
| 實驗與人工驗證完成 | Zenodo 新版本、arXiv 正式預印本 | 期刊或研討會錄用 |
| venue 正式接受 | 發布 accepted manuscript、更新引用資訊 | 出版社正式版本已上線 |
| 出版社正式出版 | 回填正式 DOI 與 journal reference | 可任意取代或刪除舊預印本 |

最終原則：

> DOI 提供永久識別與公開時間戳；實驗提供證據；arXiv 提供預印本傳播；期刊或研討會提供同儕審查；出版社 DOI 才對應正式出版紀錄。

## 📂 核心知識庫指標
- **故事與架構總覽**：`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`
- **評估與診斷問卷**：`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`
- **顧問經典框架庫**：`03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`
- **AI 原生研究人類／AI 邊界 SOP**：`09_Research_Paper/AI_NATIVE_RESEARCH_HUMAN_AI_BOUNDARY_SOP_ZH.md`
- **Advanced RAG 人類 × AI 研究故事與操作情境**：`09_Research_Paper/ADVANCED_RAG_HUMAN_AI_RESEARCH_STORY_ZH.md`
