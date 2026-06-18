# 一篇 AI-Native eBook 論文，如何由 Morris 與 AI 共同研究、投稿與發表

> 文件版本：v1.0.0  
> 日期：2026-06-07  
> Owner：MORRIS LU / YEH HSING LU, TigerAI Founder  
> 文件類型：人類 + AI 共同研究與論文寫作第三情境故事  
> 研究案例：`2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md`  
> 方法論基礎：`AI_NATIVE_RESEARCH_HUMAN_AI_BOUNDARY_SOP_ZH.md`  

---

## Stage 0：這篇論文不是從題目開始，而是從一個已經做出來的製品開始

前兩個情境故事處理的是「題目如何形成」與「技術 / 理論研究如何被 AI 協助」。

第三個情境不同。

`2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md` 的起點不是一句抽象題目，而是一個已經存在的製品：

> **GenAI Consulting Methodology Toolkit**

這個 Toolkit 已經包含：

- 354 份 Markdown 文件。
- 7 種語言。
- 22 個 AI-IDE workflow。
- 三個 AI IDE 家族的工作流空間。
- Git commit 歷史。
- GitHub release。
- Zenodo DOI。
- 可重現性 manifest。

因此，Morris 這次面對的研究問題不是：

> 我想研究什麼？

而是：

> 我已經做出一個大型 AI-native 方法論製品，這能不能被整理成一篇設計科學研究論文？如果可以，研究貢獻到底是工具本身、方法論內容，還是「AI-Native eBook production」這種新的生產範式？

AI 在這裡的第一個任務，不是幫 Morris 發想題目，而是幫他把「已完成的實作」轉成「可被學術界理解的研究對象」。

---

## Stage 1：先查文獻與資料庫，判斷研究題目是否正確

Morris 一開始擁有太多素材：

- AI 轉型成熟度模型。
- 八階段顧問方法論。
- 多語言文件。
- AI workflows。
- Git / GitHub / Zenodo release。
- AI-Native Living Book 概念。
- 讀者可以用 AI IDE 反向詢問方法論。

如果全部寫進一篇論文，會失焦。

所以 AI 的第一個任務不是幫忙寫，而是幫 Morris 查：

> 這到底是一個什麼研究題目？它是電子書研究、AI 寫作研究、HCI 研究、資訊系統研究、設計科學研究，還是方法論工程研究？

### 1.1 AI 應該搜尋哪些資料庫

這篇論文不能只靠 arXiv，也不能只靠 Google 搜尋。

AI 必須分層搜尋：

| 搜尋層 | 建議來源 | 目的 |
| --- | --- | --- |
| 前沿與 working paper | arXiv、SSRN | 找 AI writing、AI IDE、active publication、scholarly infrastructure 的最新討論 |
| 跨領域引用網路 | OpenAlex、Semantic Scholar、Google Scholar | 找相鄰概念、引用鏈、相似作者與跨領域關鍵詞 |
| DOI 與正式書目查核 | Crossref | 核對題名、作者、年份、出版來源與 DOI |
| 資訊系統與管理 | AIS eLibrary、Emerald、SpringerLink、ScienceDirect | 找 DSR、methodology engineering、maturity model、IS artifact 文獻 |
| HCI 與人機互動 | ACM Digital Library、CHI / CSCW proceedings | 找 human-AI collaboration、AI-assisted writing、reader interaction、IDE-as-medium |
| 工程與電腦科學 | IEEE Xplore、ACM、arXiv cs.* | 找 AI IDE、software engineering、literate programming、workflow、provenance |
| 系統性回顧與期刊盤點 | Scopus、Web of Science | 做正式 literature review、期刊適配與 citation network 分析 |

若學校沒有 Scopus / Web of Science 授權，AI 可以先用 OpenAlex、Semantic Scholar、Google Scholar 與 Crossref 建立初步地圖，再由人類透過學校圖書館補正式檢索。

### 1.2 AI 應該搜尋哪些關鍵詞

第一組：AI 原生電子書與可互動出版

```text
"AI-native ebook"
"interactive ebook" "artificial intelligence"
"active publication" "LLM"
"queryable document" "large language model"
"AI-native book" methodology
```

第二組：AI 輔助寫作與人機共同作者

```text
"AI-assisted writing" academic writing
"LLM-assisted writing" scholarly writing
"human-AI co-writing"
"AI writing tools" authorship attribution
```

第三組：可執行文件與知識製品

```text
"literate programming" knowledge artifact
"executable documents" scholarly communication
"computational notebook" reproducibility
"Jupyter notebook" scholarly publishing
"reactive documents" Bret Victor
```

第四組：AI IDE 與多工具編排

```text
"AI IDE" knowledge work
"multi-agent" writing workflow
"LLM orchestration" document production
"Git" "DOI" "provenance" scholarly artifact
"workflow" "research artifact" "reproducibility"
```

第五組：設計科學與方法論工程

```text
"design science research" artifact evaluation
"methodology engineering"
"methodology development" "design science"
"maturity model development" de Bruin Rosemann
"professional knowledge artifact" "information systems"
```

### 1.3 AI 要把文獻討論整理成「研究題目正確性判斷」

搜尋後，AI 不能只列 bibliography。

它要產出一份 `TOPIC_FIT_AND_LITERATURE_POSITIONING.md`，至少回答：

| 問題 | 判斷方式 |
| --- | --- |
| 這題是否已經有人做過？ | 比較 AI writing、interactive documents、executable documents、AI IDE、DSR artifact 文獻 |
| 研究對象應該是什麼？ | 判斷重心是 eBook production、methodology engineering、reader interaction，還是 AI-assisted writing |
| 本文不能主張什麼？ | 不能主張第一個 AI 寫作、第一個互動書、第一個可執行文件 |
| 本文可能主張什麼？ | 多 AI IDE + Git + workflow + DOI + reader-queryable methodology artifact 的組合 |
| 哪些文獻是核心理論？ | Hevner / Peffers DSR、Knuth、Jupyter、Victor、Engelbart、AI writing studies |
| 哪些只是相鄰實務？ | AI research skills、AI IDE workflows、open-source tooling |
| 最適合的學術社群是誰？ | DSR / IS、HCI、scholarly communication、knowledge management |

AI 初步應該幫 Morris 得出一個較精準的判斷：

> 這篇論文不是「AI 幫忙寫電子書」；比較正確的題目是「AI IDE 作為方法論工程與 AI-native professional eBook 生產的基礎設施」。  
>  
> 它的研究價值不在於發明電子書，也不在於證明 AI 能寫作，而在於說明：當專業知識製品被放進 Git、workflow、AI IDE 與 DOI 形成的環境中，電子書開始具有可查詢、可審查、可重現與可演化的特性。

### 1.4 題目正確性 Gate

Stage 1 結束前，Morris 必須做一個決定：

| 選項 | 何時採用 |
| --- | --- |
| **Go** | 文獻顯示組合式缺口成立，且 artifact 有足夠證據支撐 |
| **Narrow** | 題目太大，需收斂到 methodology engineering 或 reader-queryable professional eBook |
| **Pivot** | 發現 eBook 不是正確主題，應改成 AI IDE-based methodology engineering |
| **Stop** | 既有文獻已完整涵蓋，且 artifact 沒有足夠差異 |

在目前這篇論文中，最合理的判斷是：

> **Narrow + Go。**

也就是：

- 不寫成「AI 改變所有電子書出版」。
- 不寫成「AI 協助寫書」。
- 不寫成「第一本 AI-native book」。
- 而是收斂為：

> **以 GenAI Consulting Methodology Toolkit 作為 demanding case，研究多 AI IDE 編排如何讓 professional eBook / methodology artifact 具備可查詢、可審查、可重現與可演化的特性。**

因此 Morris 先要求 AI 協助拆解：

| 候選研究對象 | 可能論文類型 | 是否放在本篇 |
| --- | --- | --- |
| L1-L5 成熟度模型本身 | Maturity model paper | 否，留給後續 Paper #2 |
| 八階段顧問方法論 | Consulting methodology paper | 否，可作 artifact substance |
| Toolkit 作為整體 artifact | Design science artifact paper | 是 |
| 多 IDE 生產模式 | AI-native production paradigm | 是 |
| 讀者用 AI IDE 詢問文件 | Reader-as-querier interaction | 是 |
| Git + Workflow + DOI provenance | Reproducible scholarly artifact | 是 |

AI 的作用是幫 Morris 發現：

> 本篇論文真正的研究對象不是「企業 AI 轉型方法論內容」，而是「AI IDE 如何成為方法論工程與 AI-native eBook 生產的基礎設施」。

這一步非常關鍵。

因為如果研究對象不收斂，論文會變成產品介紹，而不是學術研究。

---

## Stage 2：把實作經驗轉成 Research Questions

Morris 先說出自己的直覺：

> 我以前用傳統方式寫方法論，很慢、容易偏見、難以跨語言維護，也很難讓讀者真正互動。後來我用 Claude Code、Codex、Antigravity、Git、Workflow、DOI，把整套方法論做成 AI-Native Living Book。這是不是一種新的電子書生產方式？

AI 不應直接回答「是」。

AI 要把直覺拆成可研究問題：

- **RQ1：** 多 IDE 編排在電子書生產中，啟用了哪些單一工具寫作無法達成的特性？
- **RQ2：** 讀者與 AI IDE 的互動如何改變專業電子書的消費方式？需要哪些設計支援？
- **RQ3：** AI-Native eBook engineering 應有哪些設計原則？與既有方法論發展指南如何比較？

這三個 RQ 是從實作經驗中抽出來的。

但 Morris 要決定它們是否：

- 能由現有 artifact 支撐。
- 能由 Git / workflow / DOI 證據追溯。
- 能和既有文獻對話。
- 不會誇大為「所有電子書都應該這樣做」。

這就是 RQ Freeze。

---

## Stage 3：AI 協助定位文獻，不把實作誤當 novelty

這篇論文容易犯的錯，是把「我做出來了」誤寫成「學術上沒有人想過」。

因此 AI 必須先幫 Morris 搜尋相鄰領域：

- Design Science Research。
- Methodology engineering。
- Maturity model development。
- Literate programming。
- Executable documents。
- Jupyter notebooks。
- Observable / reactive documents。
- AI-assisted writing。
- Human-AI collaboration。
- IDE-as-medium。
- Open-source knowledge artifacts。
- Git / DOI / provenance in scholarly communication。

AI 應該提出一個誠實定位：

> 這篇論文不是第一個談 AI 寫作，也不是第一個談可執行文件；它的可能貢獻在於把多 AI IDE、Git、workflow、reader-queryable interaction 與 DOI provenance 組合到 professional eBook / methodology engineering 這個 demanding case。

### Literature Gate

每個文獻來源都要分級：

| 層級 | 例子 | 用途 |
| --- | --- | --- |
| Tier 1 | Hevner DSR、Peffers DSR、Knuth literate programming | 核心理論基礎 |
| Tier 2 | Jupyter、observable notebooks、reactive documents、AI writing studies | 相鄰研究 |
| Tier 3 | AI research skills、research tooling、AI IDE practitioner artifacts | 顯示實務趨勢，但不能當核心學術證據 |

AI 可以協助找文獻，但不能把 practitioner artifacts 寫成同儕審查證據。

---

## Stage 4：把 Toolkit 轉成 Design Science Artifact

Morris 不是只描述「我做了一個 repo」。

他要把 Toolkit 對齊 Design Science Research。

AI 協助將 artifact 描述成：

- 問題：傳統專業電子書週期慢、單作者偏見、讀者被動。
- 製品：GenAI Consulting Methodology Toolkit。
- 形式：AI-native eBook / methodology engineering artifact。
- 組成：Markdown 文件、AI IDE workflows、Git history、release manifest、DOI。
- 評估：依 Hevner 七大準則。
- 貢獻：AI-Native eBook production paradigm。

### DSR Gate

論文必須回答：

1. 問題是否重要？
2. 製品是否清楚？
3. 製品是否被評估？
4. 研究貢獻是否明確？
5. 文獻與方法是否嚴謹？
6. 設計過程是否可追溯？
7. 研究是否能傳達給學術與實務讀者？

若只說「這個 repo 很大」，不構成 DSR。

---

## Stage 5：AI 協助建立可驗證的數字與 provenance

這篇論文有一個優勢：很多主張可以回到 repository 查核。

例如：

- Markdown 文件總數。
- 實質源文件數。
- 翻譯姊妹檔數。
- Workflow 數。
- Git commit 數。
- Release tag。
- Zenodo DOI。
- Release manifest。

Codex 的責任是偏工程稽核：

- 讀 `REPRODUCIBILITY.md`。
- 檢查計數命令。
- 核對 commit hash。
- 確認數字來自 frozen commit。
- 避免 HEAD 新增內容污染論文數字。
- 確認 DOI 與 GitHub release 對應。

Morris 的責任是判斷：

- 這些數字是否真的支撐論文主張。
- 哪些只是描述 artifact 規模。
- 哪些能支持 reproducibility。
- 哪些不能拿來證明方法一定有效。

### Evidence Gate

若一句話寫成：

> Toolkit contains 354 markdown documents.

就必須能回到：

- frozen commit。
- counting command。
- reproducibility manifest。

若一句話寫成：

> Multi-IDE orchestration improves eBook quality.

就必須更小心。除非有明確比較設計，否則只能寫成：

> In this observed production process, multi-IDE orchestration enabled properties not achieved in prior single-tool attempts within the same project.

AI 要幫 Morris 降主張，不是幫他加強語氣。

---

## Stage 6：多 AI 分工撰寫，但每個 AI 有不同責任

這篇論文最適合展示多 AI IDE 分工。

| 工具 | 主要責任 | 不該做的事 |
| --- | --- | --- |
| Claude Code | 跨檔綜合、理論橋接、章節敘事 | 不得平滑掉證據缺口 |
| Codex | 結構稽核、數字查核、版本一致性、citation trace | 不得代替 Morris 判斷研究意義 |
| Antigravity | 多角色發散、模擬 reviewer、找反例 | 不得把角色共識當成證據 |

寫作流程：

```text
Morris 定義研究意圖
→ AI 產生候選 RQ
→ Morris 凍結 RQ
→ Claude 建立 outline
→ Codex 建立 evidence / reproducibility checks
→ Antigravity red-team
→ Morris 決定接受 / 修改 / 刪除
→ AI 生成候選草稿
→ Codex 做 claim audit
→ Morris author approval
```

AI 的產出是草稿與檢查，不是最終論文。

---

## Stage 7：Claim-Evidence Matrix 先於潤稿

這篇論文容易被寫得太興奮。

因此 Morris 必須先建立 Claim-Evidence Matrix：

| Claim | Evidence | 狀態 |
| --- | --- | --- |
| Toolkit 是 AI-native eBook demanding case | repo scope、file count、workflow count、release manifest | Source-Verified |
| 多 IDE 編排啟用四項特性 | observed production + workflow examples | Human-Reviewed / Source-Verified |
| Reader-as-querier 改變電子書消費方式 | workflow design + reader interaction model | Proposed / needs user study |
| Git + workflow + DOI 形成 provenance chain | GitHub release、Zenodo DOI、manifest | Source-Verified |
| 這種方法優於所有傳統電子書生產 | 無足夠證據 | 不可進稿 |

這張表會決定哪些句子可以進正式稿。

---

## Stage 8：DOI 註冊與版本治理

這篇論文已經實際走過 DOI 路線。

研究製品與論文要分開管理：

| 物件 | DOI 角色 |
| --- | --- |
| Toolkit software / methodology artifact | Companion software DOI |
| Paper preprint | Paper DOI |
| 每個版本 | Version DOI |
| 持續演化的整組作品 | Concept DOI |

Zenodo 的重要性是：

- publish 時建立 DOI。
- 第一版同時有 version DOI 與 concept DOI。
- 新版本有新的 version DOI。
- concept DOI 指向整組版本。

Morris 要確保：

- PDF / Markdown / metadata 內的 DOI 一致。
- GitHub release tag 與 Zenodo deposit 對應。
- `CITATION.cff` 更新。
- README badge 更新。
- Release manifest 記錄版本。

DOI 是可引用與版本凍結，不是同儕審查。

---

## Stage 9：SSRN、arXiv 與期刊路線

這篇論文偏資訊系統、HCI、方法論工程與 scholarly communication。

公開路線可以分三段：

```text
Zenodo DOI
→ SSRN / arXiv preprint
→ conference feedback
→ international journal
```

### SSRN

適合：

- 管理學。
- 資訊系統。
- 顧問方法論。
- working paper 曝光。

### arXiv

適合：

- AI / HCI / CS / scholarly infrastructure 讀者。
- 英文 canonical 稿。
- 可以後續更新版本。

注意：

- arXiv 給 arXiv ID，不是 DOI。
- 期刊接受後可補 journal reference / DOI。
- 版本更新會保留舊版本。
- 投稿前要確認分類是否合適。

### 國際期刊 / 會議

候選方向：

| Venue | 適合角度 |
| --- | --- |
| DESRIST | Design science artifact、methodology engineering |
| ECIS / ICIS / PACIS | Information systems、AI IDE、methodology artifact |
| CHI / CSCW | Reader-as-querier、IDE-as-medium、human-AI knowledge work |
| Information Systems Frontiers | AI capability、information systems innovation |
| International Journal of Information Management | 高層次管理與資訊管理意涵，需要更強資料 |
| Journal of Documentation / scholarly communication venues | AI-native publication、provenance、active documents |

目前最務實的路線：

1. Zenodo DOI 版本維護。
2. SSRN 增加管理 / IS 曝光。
3. arXiv 增加 AI / HCI / CS 曝光。
4. DESRIST 或 ECIS 取得 DSR / IS 社群回饋。
5. 依 reviewer 回饋補 user study 或 replication study。
6. 再投國際期刊。

---

## Stage 10：Reviewer Red-Team 攻擊論文最脆弱處

AI 要模擬 reviewer 問：

1. 這只是個人 repo，不是 generalizable study？
2. 多 IDE 是否只是工具堆疊，而不是理論貢獻？
3. 所謂 reader-queryable 是否真的有使用者研究？
4. 文件數量是否只是規模描述，不能證明品質？
5. AI 參與寫作是否造成 circularity？
6. 這篇論文是否把方法論內容與生產方法混淆？
7. DOI / Git 是否只是出版技術，不是理論貢獻？
8. 與 literate programming、Jupyter、reactive documents 差異是否夠清楚？

Morris 應決定：

- 補文獻。
- 增加 limitation。
- 降低 claim。
- 增加 replication agenda。
- 設計後續 user study。

---

## Stage 11：Human Release

正式公開或投稿前，Morris 要確認：

- 所有數字可由 frozen commit 重建。
- DOI、release tag、manifest、CITATION 一致。
- AI 使用已揭露。
- 沒有把 AI 寫作工具列為人類作者。
- 沒有把 practitioner artifact 寫成 peer-reviewed evidence。
- 沒有把 observed production 寫成普遍因果。
- 每個核心 claim 都有 evidence 或被降級為 proposed。
- 期刊 / 會議 preprint policy 已確認。

只有 Morris 能按下 publish、submit 或 release。

---

## 最後一句話

> **這篇 AI-Native eBook 論文示範的是：當研究者已經做出一個大型 AI-native 方法論製品時，AI 可以協助把製品拆成研究對象、文獻位置、DSR artifact、可查核證據、投稿路線與 reviewer 反駁；但只有人類作者能決定研究意義、降級主張、揭露限制並承擔發表責任。**
