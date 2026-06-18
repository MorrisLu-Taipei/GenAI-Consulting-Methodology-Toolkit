# 一篇 AI 轉型成熟度理論論文，如何由 Morris 與 AI 共同研究完成

> 文件版本：v1.1.0  
> 日期：2026-06-07  
> Owner：MORRIS LU / YEH HSING LU, TigerAI Founder  
> 文件類型：人類 + AI 共同研究與論文寫作第二情境故事  
> 研究案例：Tiger AI L1-L5 Generative AI Adoption Maturity Model  
> 方法論基礎：`AI_NATIVE_RESEARCH_HUMAN_AI_BOUNDARY_SOP_ZH.md`  

---

## Stage 0：Morris 提出題目，AI 先幫他判斷值不值得研究

這個故事的研究主題是：

> **企業導入生成式 AI 時，能否用一套 L1-L5 成熟度模型，說明企業如何從個人使用，發展到部門知識資產化、跨部門流程自動化、單一自主 Agent，以及多 Agent 組織？**

這個題目來自 Morris 自己的研究與工作經歷。

- 碩士階段，他師從 Michael Rosemann 教授，接觸成熟度模型、BPM 與方法論發展的研究思想。
- 在資訊外商工作期間，他累積顧問方法論的實踐心得，理解企業能力不能只靠工具清單描述，而要有階段、證據、Owner 與驗收標準。
- 進入博士班後，他開始思考：生成式 AI、AI IDE、Workflow 與 Agent 出現後，傳統數位成熟度模型是否足以描述新的企業轉型路徑？

這個問題只能由 Morris 提出。

AI 沒有他的研究訓練，也沒有他的顧問工作經驗。AI 可以幫忙比較理論、找文獻、攻擊模型與整理證據，但不能替他捏造一個研究動機。

這就是案例的起點：

> **人類從自身經驗提出可能值得研究的問題；AI 透過大量對談、追問、文獻搜尋與可行性查核，協助判斷它能否變成真正可研究的題目。**

---

## Stage 1：研究所最難的不是寫論文，而是找到能研究的題目

多數研究生一開始沒有足夠研究經驗。

他們常常只有一個模糊直覺：

- 我覺得這件事很重要。
- 我在工作或產業裡看過這個問題。
- 我想研究某個工具、方法或現象。
- 我覺得現有說法好像沒有講清楚。

但這還不是研究題目。

研究題目必須經過一連串轉換：

```text
自身經驗
→ 問題直覺
→ AI 對談釐清
→ 候選研究問題
→ 文獻搜尋
→ 撞題與缺口查核
→ 方法與資料可行性分析
→ 投稿社群與期刊適配
→ 可研究題目
```

Morris 的起點不是「我已經有一篇前置研究」，而是：

> 我有成熟度模型、BPM 與顧問方法論的學習與實務經驗；我觀察到生成式 AI 讓企業轉型能力出現新型態，但我還需要 AI 協助我判斷：這個想法到底有沒有研究價值？是否已經被別人做過？能不能形成一篇學術論文？

因此，AI 的第一個角色不是寫作者，而是**研究題目引導者**。

AI 要陪 Morris 反覆問：

- 你真正想研究的是工具、組織能力、流程變化，還是成熟度模型？
- 你的經驗裡哪一部分是個人觀察，哪一部分能變成可研究現象？
- 這個題目屬於資訊系統、BPM、管理、教育，還是 AI governance？
- 既有研究如果已經有 AI maturity model，你還剩下什麼差異？
- 如果差異只是名稱不同，這題目就不成立。
- 如果差異能被文獻與資料支持，才有機會成為研究。

這就是人類 + AI 共同研究方法論的第一步：

> **不是請 AI 直接寫論文，而是請 AI 幫研究者把直覺變成可以被搜尋、被反駁、被驗證的研究問題。**

---

## Stage 2：Morris 先寫 Research Brief，不先叫 AI 寫論文

Morris 不會從這句提示詞開始：

> 幫我寫一篇企業 AI 成熟度模型論文。

他要先完成 `RESEARCH_BRIEF.md`，說清楚：

### 研究現象

企業已經開始使用 ChatGPT、Claude、Gemini、OpenWebUI、n8n 與各種 Agent，但「有使用 AI」無法回答：

- 能力只存在少數個人，還是已成為部門資產？
- AI 只是聊天工具，還是已進入跨部門流程？
- Agent 是展示 Demo，還是有任務、權限、記憶、Log 與人工審核？
- 多 Agent 是多開幾個視窗，還是真正形成可治理的職能分工？

### 初步理論想法

Morris 提出兩條軸：

1. **規模軸 L1-L3：** 個人使用 → 部門知識資產化 → 跨部門 / 全公司流程。
2. **AI 自主軸 L4-L5：** 單一自主 Agent → 多 Agent 組織。

### 初步研究缺口

既有成熟度模型可能能描述數位能力、流程能力或 AI adoption，但未必能清楚區隔：

- 組織擴散的範圍。
- AI 執行工作的自主程度。
- 每一級應具備的 Evidence 與 Stage Gate。
- L3 流程自動化到 L4 自主 Agent 的關鍵分界。

這些都只是初步想法，不是已成立的研究貢獻。

---

## Stage 3：AI 先做研究價值與撞題查核

Morris 有研究動機，不代表題目一定具有學術價值。

他需要 AI 先協助回答：

1. 這個問題是否已經被別人研究？
2. 既有模型已經做到哪裡？
3. Morris 的模型與既有研究真正差在哪裡？
4. 這個差異能不能被驗證？
5. 所需專家、企業樣本、問卷與資料能不能取得？
6. 做完後可能投到哪些研究社群與期刊？

AI 在這個階段不是替 Morris 證明題目很新，而是執行一份：

> **Research Value and Feasibility Scan**

### AI 應該去哪裡搜尋

不能只搜尋 arXiv，也不能只看 Google 第一頁。

| 搜尋層 | 建議來源 | 在本研究中的用途 |
| --- | --- | --- |
| 快速前沿掃描 | [arXiv](https://arxiv.org/)、SSRN | 找最新概念、working paper 與尚未正式出版的撞題研究；必須標記為未必經同儕審查 |
| 跨學科探索 | [OpenAlex](https://openalex.org/)、[Semantic Scholar](https://www.semanticscholar.org/) | 擴展關鍵字、找相似論文、追蹤引用網路與相關作者 |
| DOI 與書目查核 | [Crossref](https://www.crossref.org/) | 核對題名、作者、年份、期刊、DOI 與正式出版版本 |
| 資訊系統研究 | [AIS eLibrary](https://aisel.aisnet.org/) | 搜尋 ICIS、ECIS、PACIS、MCIS 等 IS 研究與企業 AI adoption 文獻 |
| 資訊科技與 HCI | [ACM Digital Library](https://dl.acm.org/) | 搜尋 Human-AI collaboration、agent、socio-technical system 與組織使用研究 |
| 工程與 AI 系統 | [IEEE Xplore](https://ieeexplore.ieee.org/) | 搜尋 AI system maturity、autonomy、governance、workflow 與 multi-agent 研究 |
| 商管與完整系統性檢索 | Scopus、Web of Science | 正式 systematic review、citation analysis、期刊篩選與可重複檢索；通常需學校授權 |
| 出版商原文 | SpringerLink、Emerald Insight、ScienceDirect、Wiley、SAGE | 閱讀正式期刊版本、方法、限制與附錄，不能只依搜尋摘要判斷 |

arXiv 的角色是「前沿雷達」，不是「品質認證」。

AI 若在 arXiv 找到相關 preprint，還要繼續查：

- 是否已有期刊或會議正式版本？
- 版本之間有沒有重大修改？
- 是否真的通過同儕審查？
- 正式引用應使用哪一個 DOI？

### AI 應該搜尋哪些概念

第一輪直接搜尋：

```text
"generative AI maturity model" organization
"AI capability maturity model" enterprise
"artificial intelligence maturity model" adoption
"GenAI adoption framework" enterprise
"agentic AI maturity model" organization
```

第二輪搜尋理論與方法：

```text
"maturity model development" design science
"business process maturity model" validation
"digital maturity" organizational capability
"AI readiness" versus "AI maturity"
"maturity model" inter-rater reliability
```

第三輪搜尋 Morris 模型最可能的差異：

```text
"workflow automation" "autonomous agent" maturity
"human AI collaboration" maturity organization
"multi-agent organization" enterprise
"AI autonomy" organizational maturity
"stage gate" "AI maturity model"
"evidence-based" maturity assessment AI
```

第四輪必須做反向搜尋：

```text
limitations of AI maturity models
non-linear maturity model AI adoption
critique of maturity models digital transformation
AI maturity does not improve performance
organizational AI capability pathways
```

### AI 初步找到什麼

快速查核已經顯示，這不是一片空白：

- 2021 年已有針對 AI-driven platform enterprise 的五級成熟度架構。
- 2021 年已有工業 AI / smart manufacturing 成熟度模型。
- 2023 年已有 responsible AI maturity 的 socio-technical 文獻回顧。
- 2024 年 *Information Systems Frontiers* 已刊出 AI Capability Maturity Model，使用文獻、專家與三個組織案例發展及驗證模型。
- 2025 至 2026 年又出現 Human-Centered AI、SME AI maturity、國際標準導向 AI maturity，以及 GenAI adoption framework 等研究。

本輪初查至少要把以下研究放入候選文獻矩陣：

- [Understanding Artificial Intelligence Diffusion through an AI Capability Maturity Model](https://link.springer.com/article/10.1007/s10796-024-10528-4)
- [A sociotechnical perspective for responsible AI maturity models](https://www.sciencedirect.com/science/article/pii/S266709682300040X)
- [Establishment of a maturity model to assess the development of industrial AI in smart manufacturing](https://doi.org/10.1108/JEIM-10-2020-0397)
- [Developing an Artificial Intelligence Maturity Model for Auditing](https://aisel.aisnet.org/ecis2021_rp/133/)
- [Understanding Data & Analytics Maturity: A Systematic Review of Maturity Model Composition](https://link.springer.com/article/10.1007/s41471-024-00205-2)
- [Artificial Intelligence Maturity in Small and Medium-Sized Enterprises](https://arxiv.org/abs/2603.08728)

這份清單只是 seed set，不是完整 systematic review。AI 必須再做 backward search、forward search、作者追蹤與替代關鍵字搜尋。

因此 AI 應該回報：

> **「企業 AI 成熟度模型」本身不構成 novelty。研究價值必須建立在更精確的理論差異與驗證設計上。**

### 目前可能成立的研究差異

以下只能先列為 `Innovation Candidates`：

1. **GenAI 工作能力的兩條軸**
   - L1-L3 描述能力從個人、部門擴大到跨部門流程。
   - L4-L5 描述 AI 從受控工具轉向自主 Agent 與多 Agent 組織。

2. **L3 Workflow 與 L4 Autonomous Agent 的明確分界**
   - 不以工具品牌區分，而以任務拆解、記憶、工具調用、自主排程、Evidence 與 HITL 邊界區分。

3. **Evidence-gated maturity**
   - 每一級不只描述能力，還要求 Definition of Done、Deliverables、Evidence、Owner、Fail Condition 與 Stage Gate。

4. **整體成熟度與局部成熟度並存**
   - 企業整體可能是 L2，但特定客服流程局部達到 L3 或 L4，避免把企業硬塞進單一線性級別。

5. **Maturity 與 Readiness 分離**
   - 已建立的能力才算 maturity；預算、IT 人力、資料敏感度與領導支持是 readiness / constraints。

這些差異是否真的新，仍要經過系統性文獻回顧與專家審查。

### Research Value Gate

Morris 在進入正式研究前，至少要取得一份包含以下內容的可行性報告：

- 主要既有模型比較表。
- 最接近的 10-20 篇核心研究。
- 本模型與既有模型的重疊、差異與衝突。
- 每個 innovation candidate 的支持與反證。
- 可取得的專家、企業案例與問卷樣本。
- 需要的研究倫理與資料處理。
- 預估可完成的研究設計。
- 候選投稿社群與期刊。
- Go / Narrow / Pivot / Stop 建議。

如果最後發現既有模型已完整涵蓋相同概念，正確結果不是硬寫 novelty，而是縮小題目、改變研究問題，甚至停止研究。

---

## Stage 4：AI 把通過價值查核的想法拆成候選研究問題

Morris 把 Research Brief 交給 AI，要求它不要急著證明模型正確，而是先把想法拆成可被推翻的問題。

AI 可能提出：

- **RQ1：** 規模軸與 AI 自主軸，是否能比單一路徑更清楚地區分企業生成式 AI 能力？
- **RQ2：** L1-L5 各級需要哪些可觀察能力、交付物、Evidence 與 Stage Gate？
- **RQ3：** 這套模型與既有 AI adoption、digital maturity、BPM maturity 及 agent maturity 模型有何重疊與差異？
- **RQ4：** 不同評分者使用相同 rubric 評估企業時，是否能得到一致結果？
- **RQ5：** 成熟度分數是否與外部營運指標、AI 使用成果或治理能力相關？

AI 也可能提出過大的候選主張：

- 這是第一個 Generative AI maturity model。
- 所有企業都必須依 L1 到 L5 順序發展。
- 到達 L5 的企業一定有更高績效。
- L4-L5 將取代人類組織。

Morris 必須拒絕這些沒有證據或過度普遍化的說法。

### RQ Freeze 的人類責任

AI 可以提出 RQ 候選，但 Morris 要決定：

- 哪些問題符合他的真實研究意圖？
- 哪些問題能取得資料？
- 哪些問題需要質性案例？
- 哪些問題需要問卷與統計驗證？
- 一篇論文能合理回答多少問題？

只有 Morris 核准後，RQ 才能進入 `RESEARCH_QUESTIONS.md`。

---

## 操作 Stage 1：建立成熟度論文研究工作區

Paper #2 不應只散落在聊天紀錄裡。

Morris 先要求 Codex 建立或確認研究結構：

```text
09_Research_Paper/
└── AI_MATURITY_PAPER/
    ├── 00_GOVERNANCE/
    │   ├── RESEARCH_BRIEF.md
    │   ├── HUMAN_AI_BOUNDARY.md
    │   ├── AI_USE_LOG.md
    │   └── DECISION_LOG.md
    ├── 01_PROTOCOL/
    │   ├── RESEARCH_QUESTIONS.md
    │   ├── MODEL_DEVELOPMENT_PROTOCOL.md
    │   ├── VALIDATION_PROTOCOL.md
    │   └── CHANGE_CONTROL.md
    ├── 02_LITERATURE/
    │   ├── SEARCH_STRATEGY.md
    │   ├── SEARCH_LOG.md
    │   ├── LITERATURE_MATRIX.md
    │   ├── THEORY_BRIDGES.md
    │   └── REJECTED_REFERENCES.md
    ├── 03_MODEL/
    │   ├── CONSTRUCT_DEFINITIONS.md
    │   ├── LEVEL_DEFINITIONS.md
    │   ├── BARS_RUBRICS.md
    │   └── MODEL_CHANGE_LOG.md
    ├── 04_VALIDATION/
    │   ├── EXPERT_REVIEW/
    │   ├── CASE_STUDIES/
    │   ├── SURVEY/
    │   └── ANALYSIS/
    ├── 05_MANUSCRIPT/
    │   ├── OUTLINE.md
    │   ├── CLAIM_EVIDENCE_MATRIX.md
    │   ├── preprint_ZH.md
    │   └── preprint_EN.md
    ├── 06_REVIEW/
    │   ├── RED_TEAM_FINDINGS.md
    │   ├── CLAIM_AUDIT.md
    │   └── REVIEWER_RESPONSE.md
    └── 07_RELEASE/
        ├── SUBMISSION_CHECKLIST.md
        └── RELEASE_MANIFEST.md
```

這些目錄不是形式工作。

它們把「理論怎麼形成」「哪些內容已驗證」「誰做了什麼決定」分開保存，避免 AI 草稿、顧問經驗與實證結果混成一團。

---

## Stage 5：正式文獻回顧不是替模型找支持，而是找誰能推翻它

Morris 會請 AI 做兩種搜尋。

### 第一種：驗證性搜尋

確認研究需要的理論基礎：

- Maturity model development。
- Business Process Management maturity。
- Design Science Research。
- Digital maturity。
- AI adoption maturity。
- Organizational capability。
- Absorptive capacity。
- Dynamic capabilities。
- Human-AI collaboration。
- Agent autonomy 與 multi-agent organization。

### 第二種：創新性與反向搜尋

AI 要跨領域搜尋：

- 是否已有模型使用「組織規模 × AI 自主性」兩條軸？
- 是否已有成熟度模型把 Workflow 與 Agent 分開？
- 是否已有模型要求每一級具備 Evidence、Owner 與 Stage Gate？
- 是否有研究認為成熟度不一定是線性階梯？
- 是否有企業可以局部 L4、但整體仍是 L2？
- 是否有研究指出高成熟度不必然帶來高績效？

AI 的責任不是替 Morris 證明他是對的，而是盡可能找到：

- 相同概念。
- 更早的研究。
- 替代理論。
- 反例。
- 會削弱 novelty 的文獻。

### 三個 AI IDE 的分工

| 工具 | 在成熟度論文中的角色 |
| --- | --- |
| **Antigravity** | 平行派出 maturity model、BPM、organization、AI adoption、agent governance 等探索角色 |
| **Claude Code** | 長上下文閱讀 Paper #1、Toolkit、文獻矩陣與模型版本，建立理論橋接與 Related Work |
| **Codex** | 核對 DOI、引用、檔案一致性、表格定義、版本差異與 Claim-Evidence traceability |

### Authenticity Gate

每一篇核心文獻都必須：

1. 能在正式來源查得。
2. 核對題名、作者、年份與 DOI。
3. 由人類閱讀支撐核心主張的原文。
4. 記錄它真正支持與不支持的內容。
5. 查核失敗時放入 `REJECTED_REFERENCES.md`。

AI 找到的文獻只是 `AI-Candidate`，不是正式 References。

---

## Stage 6：把顧問經驗轉成 Construct，而不是直接當作學術真理

Morris 已經有 L1-L5 的實務想法：

| Level | 初步能力概念 |
| --- | --- |
| L1 | Controlled AI Access |
| L2 | Knowledge Codification |
| L3 | Workflow Automation |
| L4 | Autonomous Agent |
| L5 | Multi-Agent Organization |

但顧問經驗不能直接等同學術驗證。

AI 可以協助 Morris 逐級追問：

- 這一級的 Definition 是什麼？
- Observable Indicators 是什麼？
- 哪些現象不算這一級？
- 要用哪些問卷題目測量？
- 需要哪些客觀 Evidence？
- 哪一級與哪一級最容易混淆？
- 哪些能力是成熟度，哪些只是 Readiness 或限制條件？

例如：

> 員工想使用 AI，是 readiness；公司已有受控入口、使用規範與使用紀錄，才是 maturity。

又例如：

> 公司做過一次 n8n Demo，不等於 L3；必須有真實流程、系統串接、Log、錯誤處理、Owner 與人工審核。

AI 可以幫忙整理 Construct Definition Table，但每一項定義都要由 Morris 與後續專家審查。

---

## 操作 Stage 2：讓 AI 模擬不同學派攻擊模型

Morris 可以使用多 AI 進行對抗式審查。

### BPM 研究者

可能會問：

> 你的模型如何對應既有 maturity model development procedure？為什麼是五級？

### 組織理論研究者

可能會問：

> 企業能力真的線性發展嗎？局部成熟與組織整體成熟如何區分？

### AI 工程師

可能會問：

> L4 Agent 與 L3 Workflow 的客觀分界是什麼？只是工具品牌不同嗎？

### 統計研究者

可能會問：

> 量表是否有信度、效度與評分者一致性？

### 企業主管

可能會問：

> 成熟度升高是否真的帶來營運價值？還是只增加治理成本？

AI 的工作是把這些反駁提早帶進研究。

Morris 的工作是決定：

- 修改模型。
- 補文獻。
- 補實驗。
- 降低主張。
- 將問題誠實列為限制。

Red-team 不是為了替論文找漂亮答案，而是避免模型只剩作者自己相信。

---

## Stage 7：研究設計由人決定，AI 協助找漏洞

目前的 L1-L5 模型屬於：

> **Expert-consensus version，尚待 psychometric 與 empirical validation。**

因此成熟度論文不能直接宣稱模型已經被證明有效。

Morris 必須設計驗證路線，可能包含：

### 1. 專家內容效度

- 邀請 BPM、AI、組織、顧問與企業實務專家。
- 檢查 Level、Construct、題目與 Evidence 是否合理。
- 記錄專家分歧與模型修改。

### 2. 案例研究

- 追蹤不同產業企業的 AI 導入。
- 觀察模型能否解釋真實能力差異。
- 檢查局部成熟度、跳級與退化情況。

### 3. 評分者間信度

- 兩位顧問獨立評估同一企業。
- 比較是否能得到相近判定。
- 找出 rubric 模糊的位置。

### 4. 問卷信效度

- 蒐集足夠樣本後進行內部一致性、EFA、CFA。
- 檢查六大構面是否真的能被資料支持。
- 不因統計結果不漂亮就偷偷改掉原始假設。

### 5. 外部效度與縱貫研究

- 檢查成熟度與時間、品質、風險、知識資產或 AI ROI 的關聯。
- 追蹤企業是否真的依預期路徑發展。

AI 可以：

- 比較研究設計。
- 草擬問卷與訪談題目。
- 模擬 reviewer。
- 檢查變項與資料格式。
- 執行統計程式。
- 整理質性編碼候選。

但 AI 不可以：

- 代替專家填答。
- 產生虛構企業樣本。
- 把模擬資料當成實證結果。
- 自行刪除不支持模型的案例。
- 決定最終理論解釋。

### Protocol Freeze

正式收集資料前，Morris 要凍結：

- RQ。
- Construct definitions。
- 納入排除標準。
- 問卷版本。
- 訪談流程。
- 主要分析方法。
- 主要評估指標。

之後若修改，必須留下 Change Control，而不是讓 AI 邊分析邊改規則。

---

## 操作 Stage 3：AI 如何幫研究生把「我覺得」變成「可研究」

這一幕對研究生最重要。

Morris 一開始可能只對 AI 說：

> 我熟悉成熟度模型，也有外商顧問經驗。現在 GenAI、n8n、AI Agent 很快進入企業，我覺得企業 AI 轉型應該要有一套新的成熟度模型。

AI 不應該回答：

> 這是一個很棒的題目，我幫你寫。

正確的 AI 對談方式是連續追問：

### 1. 釐清研究對象

- 你要研究企業使用 AI 的成熟度，還是 AI 工具本身的成熟度？
- 你要研究生成式 AI adoption，還是 broader AI capability？
- 你要研究模型發展，還是模型驗證？
- 你要研究中小企業、大企業、製造業，還是不限定產業？

### 2. 釐清理論基礎

- 你的模型與 Rosemann / de Bruin 的 maturity model development 有何關係？
- 它與 BPM maturity、digital maturity、AI readiness、AI capability maturity 有何差別？
- 你說的 L1-L5 是順序階梯、能力集合，還是兩條軸？
- 你如何處理局部成熟度與整體成熟度？

### 3. 釐清研究價值

- 如果 2024 已有 AI Capability Maturity Model，你的新模型還剩下什麼？
- 你的貢獻是新的 Level、Construct、Evidence Gate、評分量表，還是實務導入流程？
- 你的模型是否能解釋 GenAI、Workflow、Agent、Multi-Agent 這些新現象？
- 這些現象是否已有文獻處理？

### 4. 釐清資料可行性

- 你能找到幾位專家做 content validity？
- 你能取得幾家企業案例？
- 你能讓兩位顧問獨立評分同一企業嗎？
- 你能收集問卷樣本做 reliability 與 factor analysis 嗎？
- 若不能，第一篇論文是否應先定位為 conceptual / design science / model development？

### 5. 釐清投稿可能性

- 這題比較像 BPM、Information Systems、Management、HCI，還是 AI governance？
- 哪些期刊接受 maturity model development？
- 哪些期刊要求強實證，不適合早期模型論文？
- 哪些 conference 適合先投 research-in-progress？

這些對談會讓研究者慢慢看見：

> 原本一句「我想做 AI 成熟度模型」，其實可以分成十幾種完全不同的研究。

AI 的價值，是幫研究者把模糊方向拆開，再用文獻與方法逐一檢查。

---

## Stage 8：AI 寫初稿之前，先建立 Claim-Evidence Matrix

Morris 不先叫 AI 把所有內容寫成漂亮論文。

他先建立：

| Claim | 需要的 Evidence | 目前狀態 | 可否進正式稿 |
| --- | --- | --- | --- |
| 企業 GenAI 能力包含規模與自主兩條軸 | 文獻比較 + 理論論證 + 專家審查 | 待驗證 | 只能寫成 proposed model |
| L3 到 L4 是重要分界 | Construct 定義 + 案例證據 + 專家審查 | 部分理論支持 | 降級表述 |
| 五級模型可被穩定評分 | Inter-rater data | 尚未執行 | 不可宣稱 |
| 六大構面具有信效度 | EFA / CFA / reliability | 尚未執行 | 不可宣稱 |
| 高成熟度改善企業績效 | 縱貫 KPI / 外部效度 | 尚未執行 | 不可宣稱因果 |
| Toolkit 已形成可查詢方法論製品 | Paper #1、Git、Workflow、DOI | 已有來源 | 可引用但須限定範圍 |

只有 Claim-Evidence Matrix 通過後，AI 才能依核准大綱撰寫草稿。

尚未完成的內容必須使用：

- proposed。
- hypothesized。
- expert-consensus。
- pending validation。
- future empirical study。

不能使用：

- proven。
- validated。
- universally applicable。
- first-ever。
- guarantees performance。

---

## 操作 Stage 4：三個 AI 如何共同寫，但不共同署名

### Antigravity：發散

Morris 可以要求多個角色同時提出：

- 替代理論。
- 反例。
- 不同產業情境。
- 可能的 construct overlap。
- 可能推翻模型的案例。

輸出先進入候選區。

### Claude Code：綜合

Claude Code 跨讀：

- Paper #1。
- 成熟度問卷。
- 評分模型。
- Evidence matrix。
- BARS rubrics。
- 文獻矩陣。
- 專家審查紀錄。

再依核准大綱產生 Related Work、Model Development 與 Discussion 草稿。

### Codex：驗證

Codex 檢查：

- 每個引用是否存在。
- Level 名稱是否跨檔一致。
- 數字是否能由來源重建。
- 未驗證結果是否被寫成事實。
- 表格、圖、問卷與稿件是否使用相同版本。
- Claim 是否能追溯到 Evidence。

### Morris：核准

Morris 逐段判斷：

- 這是我的研究意圖嗎？
- 這項理論連結成立嗎？
- 這段話超過證據了嗎？
- 哪些內容我能在口試或審稿時親自辯護？
- 哪些內容應刪除或列為限制？

AI 可以留下貢獻紀錄，但不能列為人類共同作者。

---

## Stage 9：Reviewer Red-Team 專門攻擊最脆弱的地方

正式投稿前，Morris 要求 AI 不再幫忙「寫得更好」，而是試著讓論文失敗。

Reviewer Red-Team 應集中攻擊：

1. 五級是否為作者主觀切分？
2. 兩條軸是否真的正交？
3. 模型是否過度依賴特定工具品牌？
4. L4 Agent 是否只是較複雜的 L3 Workflow？
5. 企業是否真的需要依序升級？
6. 局部成熟度如何處理？
7. Readiness 與 Maturity 是否混在一起？
8. Expert-consensus 是否被誤寫成 validated scale？
9. 問卷門檻是否缺乏心理計量證據？
10. 顧問商業利益是否造成 confirmation bias？

每個問題都進入 `RED_TEAM_FINDINGS.md`。

Morris 再決定：

- 補文獻。
- 修改 construct。
- 增加研究。
- 降低主張。
- 揭露利益衝突。
- 保留為 limitation。

### Revision Sign-off

AI 不能自行宣布問題已解決。

每個 finding 必須由 Morris 標記：

- Accepted and revised。
- Partially accepted。
- Rejected with rationale。
- Requires future study。

---

## Stage 10：投稿可行性不能等到論文寫完才分析

AI 在研究價值查核完成後，就應建立第一版 `VENUE_MATRIX.md`。

期刊不是依名氣排序，而是依論文最後的貢獻類型選擇。

| 候選 venue | 適合的論文版本 | 投稿前最低條件 | 初步判斷 |
| --- | --- | --- | --- |
| **Business Process Management Journal** | 強調成熟度模型發展、流程能力、Stage Gate 與 BPM 理論 | 完整模型發展程序、專家審查、案例驗證、與 BPM maturity 文獻清楚對話 | **高度適配**，尤其符合 Morris 的 BPM 與 Rosemann 學術脈絡 |
| **Journal of Enterprise Information Management** | 強調企業資訊管理、導入路徑與顧問實務價值 | 理論貢獻不能只停在工具清單，需有多企業案例與管理意涵 | **務實且適配** |
| **Information Systems Frontiers** | 強調新興 IS、AI capability 與組織擴散 | 必須正面比較該刊既有 AICMM，提出清楚差異並完成較強實證 | **主題適配但撞題壓力高** |
| **International Journal of Information Management** | 強調高影響力的 socio-technical、治理與組織理論 | 需要強理論、跨組織或跨國資料、嚴謹量表驗證與廣泛管理意涵 | **Stretch target** |
| **Information & Management** | 強調 IS 理論、採用、組織能力與可驗證結果 | 需要成熟理論模型、扎實量化或多方法實證，而非純 conceptual framework | **Stretch target** |
| **ECIS / PACIS / ICIS** | 先發表 model development、early validation 或 research-in-progress | 清楚研究問題、初步文獻、模型與第一輪專家 / 案例證據 | **適合先取得 IS 社群回饋** |
| **DESRIST** | 將成熟度模型視為 Design Science artifact | 明確 problem relevance、design cycle、evaluation 與 contribution | **適合方法論製品版本** |

### 目前最務實的投稿路徑

1. 先完成系統性文獻回顧與最接近模型比較。
2. 完成專家內容效度與第一輪模型修訂。
3. 以 ECIS、PACIS 或 DESRIST 的 research-in-progress / conference paper 取得回饋。
4. 加入 3-5 個企業案例與 inter-rater reliability。
5. 再依最後論文重心選 BPMJ、JEIM 或 Information Systems Frontiers。
6. 若後續完成大樣本 EFA / CFA、跨產業或跨國驗證，再考慮 IJIM 或 Information & Management。

這只是截至 2026-06-07 的初步 venue fit。正式投稿前，AI 必須重新查各 venue 官方：

- Aims and Scope。
- Article type。
- 最新已刊論文。
- 字數與格式。
- Preprint policy。
- AI use disclosure。
- Research ethics。
- 當期 special issue。

期刊政策會改變，不能把今天的查核當成永久規則。

### Feasibility Gate

目前的初步判斷是：

> **研究可行，但必須 Narrow。**

不建議研究：

> 我提出一個全新的企業 AI 成熟度模型。

較可行的研究定位是：

> 我提出並初步驗證一套面向生成式 AI 工作能力的 evidence-gated maturity model，區分組織擴散規模與 AI 自主性，並探討 Workflow 到 Agent 的能力分界。

若無法取得企業案例與評分者資料，可以先寫：

- Conceptual / design paper。
- Systematic literature review。
- Model development protocol。

但不能假裝完成 empirical validation。

---

## Stage 11：何時可以先公開 Preprint

若成熟度論文尚未完成企業樣本與量表驗證，仍可以公開理論或研究設計 preprint，但必須誠實命名。

可以寫：

> 本文提出一套 expert-consensus 的企業生成式 AI 採用成熟度模型，並說明其理論基礎、construct、評分規則與待執行驗證計畫。

不能寫：

> 本研究已證明 L1-L5 能準確衡量企業 AI 成熟度。

Preprint 應清楚揭露：

- 哪些部分是設計製品。
- 哪些部分來自顧問經驗。
- 哪些部分已完成文獻支持。
- 哪些部分已經專家審查。
- 哪些統計與案例研究尚未執行。
- 下一版本要補哪些資料。

Zenodo DOI 可以凍結這個研究階段，但 DOI 只證明版本已公開，不證明理論已通過同儕審查。

---

## Stage 12：真正的 Human Release

在 Human Release 之前，Morris 要先決定公開與投稿路線。

這裡要分清楚三件事：

1. **Zenodo DOI**：用來凍結某一個研究版本，讓 working paper、protocol、dataset、code 或 release package 可以被引用。
2. **arXiv / SSRN preprint**：用來讓研究社群提早看見、引用與回饋，但不是同儕審查通過。
3. **國際期刊 / 會議**：才是正式 peer review 的學術發表路徑。

DOI 不等於論文已被接受；arXiv ID 也不等於研究已驗證。它們是公開、版本、可引用與回饋機制。

### DOI 註冊流程：先用 Zenodo 凍結可引用版本

Zenodo 適合先做「研究階段凍結」：

```text
Research Brief / Working Paper / Protocol / Dataset / Code
→ 建立 Zenodo draft
→ Reserve DOI
→ 把 DOI 寫回稿件與 metadata
→ 上傳 PDF / Markdown / release manifest / reproducibility package
→ Publish
→ 取得 version DOI + concept DOI
```

流程重點：

- 若只是準備階段，可先在 Zenodo draft 中 **Reserve DOI**，把 DOI 寫進 PDF 與 `RELEASE_MANIFEST.md` 後再 publish。
- 第一次 publish 後，Zenodo 會建立一個指向特定版本的 **version DOI**，以及一個指向整組版本的 **concept DOI**。
- 引用某個已使用的研究版本時，優先引用 version DOI。
- 若要引用一個會持續更新的研究計畫或方法論製品，可以引用 concept DOI。
- 新增實驗數據、案例、量表驗證或大幅修改稿件時，不覆蓋舊版，而是建立新版本。

建議版本策略：

| 版本 | 狀態 | 是否適合 DOI | 說明 |
| --- | --- | --- | --- |
| v0.1 | Research idea / brief | 可選 | 題目仍在探索，通常內部保存即可 |
| v0.2 | Literature scan + feasibility report | 可選 | 若要公開徵求回饋，可上 Zenodo |
| v0.3 | Model development protocol | 適合 | 研究設計與驗證計畫已可引用 |
| v0.5 | Expert-consensus working paper | 適合 | 可公開模型、construct、rubric 與限制 |
| v0.8 | Case / pilot validation preprint | 適合 | 已有初步資料，可投 conference / arXiv |
| v1.0 | Journal submission candidate | 適合 | 投稿前凍結版本與 reproducibility package |
| v1.1+ | Revision / accepted manuscript | 適合 | 回覆審稿或補實驗後建立新版本 |

### arXiv 路線：用於英文 preprint，不是 DOI 替代品

arXiv 通常適合在英文稿達到可被外部讀者理解時使用。

```text
English preprint
→ 確認 arXiv category
→ 確認是否需要 endorsement
→ 準備 TeX / PDF
→ 填 title、abstract、authors、categories、comments
→ 上傳並等待 moderation
→ 取得 arXiv ID
→ 後續用 replacement 更新版本
→ 期刊接受後補 journal reference / DOI
```

對本成熟度理論論文而言，arXiv 可以作為：

- 早期理論模型 preprint。
- model development protocol。
- expert-consensus working paper。
- case / pilot validation 版本。

但 arXiv 不會替研究補上同儕審查，也不會自動證明模型有效。若後續期刊接受，arXiv metadata 可以補上正式 journal reference 與 journal DOI。

投稿 arXiv 前要檢查：

- 類別是否適合，例如 `cs.CY`、`cs.HC`、`cs.AI`、`cs.SE` 或其他更合適分類。
- 論文是否屬於 arXiv 接受的 topical and refereeable scientific contribution。
- 是否需要 endorsement。
- 是否有中英文版本問題；正式 arXiv 版本建議使用英文 canonical 稿。
- 是否與目標期刊 preprint policy 相容。

### SSRN 路線：管理、IS 與商管讀者曝光

若論文偏管理、資訊系統、顧問方法論與企業導入，SSRN 也可同步考慮。

SSRN 的優點是：

- 較接近管理、商管、社會科學與 IS 讀者。
- 適合作為 working paper 流通。
- 可增加學術圈與實務圈曝光。

但要注意：

- SSRN 與 Zenodo / arXiv 的 DOI 與版本關係要清楚。
- 若多平台公開，稿件 metadata 要一致。
- 期刊投稿時要主動揭露 preprint / working paper 版本。

### 國際期刊路線：依研究成熟度分階段

這篇研究不應一開始就以最高等級期刊為唯一目標。

更務實的路線是：

#### Phase A：題目與文獻可行性

輸出：

- Research Brief。
- Research Value and Feasibility Scan。
- Literature Matrix。
- Venue Matrix。
- Go / Narrow / Pivot / Stop decision。

目的：

- 確定題目不是只靠個人直覺。
- 找到最接近的既有研究。
- 確認研究差異與可行性。

#### Phase B：模型發展與理論定位

輸出：

- Construct definitions。
- L1-L5 level definitions。
- Readiness / Maturity distinction。
- BARS rubric。
- Evidence / Owner / Stage Gate matrix。
- Expert review protocol。

適合目標：

- DESRIST research-in-progress。
- ECIS / PACIS / ICIS early-stage track。
- Zenodo / SSRN working paper。

#### Phase C：初步驗證

輸出：

- 專家內容效度。
- 3-5 個企業案例。
- Inter-rater reliability。
- 第一版修訂模型。

適合目標：

- Business Process Management Journal。
- Journal of Enterprise Information Management。
- Information Systems Frontiers。
- ECIS / PACIS full paper。

#### Phase D：強驗證與國際期刊

輸出：

- 大樣本問卷。
- Internal consistency。
- EFA / CFA。
- Criterion validity。
- Predictive / longitudinal validation。
- 跨產業或跨國樣本。

適合目標：

- International Journal of Information Management。
- Information & Management。
- MISQ / ISR 等頂級期刊通常需要更強理論與資料，不應作為第一階段目標。

### 推薦研究路線圖

```text
2026 Q2-Q3
  題目釐清、文獻搜尋、撞題查核、Research Brief、Venue Matrix

2026 Q3-Q4
  Construct definitions、rubric、expert review protocol、Zenodo v0.3 DOI

2026 Q4-2027 Q1
  專家審查、模型修訂、3-5 個案例設計、SSRN / arXiv working paper

2027 Q1-Q2
  pilot case study、inter-rater reliability、conference submission

2027 Q3-Q4
  journal submission to BPMJ / JEIM / IS Frontiers

2028+
  大樣本量表驗證、跨產業 / 跨國研究、挑戰 IJIM / I&M
```

### 投稿前的硬性 Gate

任何公開或投稿前，Morris 都要確認：

- AI 使用已揭露。
- 研究資料、訪談或企業案例有倫理與同意處理。
- 沒有一稿多投。
- preprint / DOI / repository / manuscript 版本一致。
- 每個核心 Claim 都有 Evidence。
- 未驗證的模型效果沒有被寫成已證明。
- 所有引用已由正式來源查核。
- 作者能親自解釋並承擔所有核心主張。

---

投稿前，Morris 必須能親自回答：

- 為什麼要研究這個模型？
- 為什麼是兩條軸？
- 為什麼是五級？
- 每一級如何觀察？
- 既有文獻與本模型有何不同？
- 哪些內容已驗證？
- 哪些仍是候選理論？
- 資料如何取得與分析？
- 模型在哪些情況不適用？
- TigerAI 的商業角色可能造成哪些偏誤？

如果其中一個核心主張只能回答：

> 因為 AI 幫我寫成這樣。

那一段就不能投稿。

只有人類作者完成全文通讀、引用核對、資料核對、利益衝突揭露、版本凍結與簽核後，才能執行：

> **Human Release**

---

## 一頁看懂：成熟度理論論文的人類 / AI 分工

| 研究環節 | Morris 負責 | AI 協助 | Gate |
| --- | --- | --- | --- |
| 選題 | 研究動機、經驗與價值 | 拆解候選問題、找反例 | RQ Freeze |
| 文獻 | 閱讀原文、判斷理論位置 | 驗證性、創新性、反向搜尋 | Authenticity Gate |
| 模型 | 決定兩軸、Level 與 Construct | 比較替代模型、找重疊與漏洞 | Model Freeze |
| 方法 | 決定案例、樣本、問卷與分析 | 模擬 reviewer、檢查設計 | Protocol Freeze |
| 資料 | 確保真實、合法與可追溯 | 格式、缺漏與分析程式 | Human Validation |
| 分析 | 解讀結果與替代解釋 | 統計、編碼候選、重現檢查 | Result Verification |
| 寫作 | 決定主張、論證與限制 | 大綱、草稿、重組與潤稿 | Author Approval |
| 審查 | 決定如何回應批評 | Red-team、claim audit、hype scrub | Revision Sign-off |
| 發表 | 署名、投稿與公開責任 | Metadata、版本與格式檢查 | Human Release |

---

## 最後一句話

> **成熟度理論案例示範：研究者先提出來自學術背景與顧問實踐的問題，再由 AI 協助查核研究價值、搜尋全球文獻、找出撞題與反證、分析研究與投稿可行性；最後經由 construct、驗證設計、證據 Gate 與多 AI 對抗審查，逐步轉成一篇可被學術界反駁與驗證的理論論文。**
