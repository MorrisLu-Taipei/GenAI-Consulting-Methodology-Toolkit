# AI-Native eBook 論文研究流程：Stage / Gate / 人類與 AI 責任矩陣

> 文件版本：v1.5.0  
> 日期：2026-06-08  
> Owner：MORRIS LU / YEH HSING LU, TigerAI Founder  
> 文件類型：人類 + AI 共同研究與論文寫作責任矩陣  
> 對應故事：`AI_NATIVE_EBOOK_HUMAN_AI_RESEARCH_STORY_ZH.md`  
> 對應論文：`2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md`  

---

## 1. 使用目的

這份表格用來把「AI-Native eBook 論文情境故事」轉成可執行、可稽核的研究 SOP。

本表對齊「寫論文是一個系統化過程」的 4 大階段與 12 個步驟：

| 大階段 | 研究步驟 |
| --- | --- |
| 階段一：研究準備，奠定基礎 | 1. 選題與研究問題；2. 文獻搜尋與閱讀；3. 研究設計與方法；4. 資料收集與整理 |
| 階段二：研究執行，產生內容 | 5. 資料分析與驗證；6. 論文架構與大綱；7. 撰寫初稿 |
| 階段三：寫作與修訂，精煉論述 | 8. 修改與潤稿；9. 引用與參考文獻；10. 圖表與視覺化；11. 投稿與期刊選擇 |
| 階段四：投稿與發表，學術傳播 | 12. 回覆審稿意見 |

表格採用責任矩陣，不使用流程箭頭。

閱讀方式：

| 欄位 | 意義 |
| --- | --- |
| 大階段 | 對應論文寫作的 4 大階段 |
| 階段 | 使用 `Stage01：選題與研究問題` 這種正式階段名稱 |
| 編號 | 使用 `1.1`、`1.2`、`1.3` 這種工作編號 |
| 情境說明 | 說明這一步在 Morris 的 AI-Native eBook 論文情境中為什麼需要做 |
| 階段說明 | 用較容易理解的方式說明這一步的目的 |
| 正式工作 | 研究文件、論文或 SOP 裡正式要完成的工作 |
| 研究人員 | 打 `v` 代表必須由 Morris / 人類研究者負責 |
| AI | 打 `v` 代表可由 AI 協助或執行 |
| Gate / 產出 | 本列完成後要通過的檢查點或留下的文件 |

重要原則：

> **這張表不是在強調文筆或靈感，而是在說明：論文寫作是一套可拆解、可檢查、可由人類與 AI 分工完成的系統化流程。**

---

## 2. Stage / Gate / 人機責任矩陣

| 大階段 | 階段 | 編號 | 情境說明 | 階段說明 | 正式工作 | 研究人員 | AI | Gate / 產出 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 階段一：研究準備，奠定基礎 | Stage01：選題與研究問題 | 1.1 | Morris 已經做出 GenAI Consulting Methodology Toolkit，不是從空白題目開始。 | 先確認手上真的有研究素材，不是在空想。 | 確認 Toolkit、Git、workflow、DOI、manifest 等製品是真實完成、可展示、可回溯，不是概念案。 | v |  | Artifact Scope Gate |
| 階段一：研究準備，奠定基礎 | Stage01：選題與研究問題 | 1.2 | Toolkit 很豐富，但論文不能什麼都寫，必須先收斂題目。 | 把實作經驗轉成可以研究的問題。 | 提出初始研究定位：AI IDE、Git、workflow、DOI 如何共同支撐 AI-native professional eBook / methodology artifact。 | v |  | 初始研究定位 |
| 階段一：研究準備，奠定基礎 | Stage01：選題與研究問題 | 1.3 | AI 可以幫忙把同一個想法拆成不同研究問題版本。 | 請 AI 多列幾種研究問題版本，方便比較。 | 產生候選 Research Questions，比較過寬、過窄與可操作版本。 |  | v | RQ 候選清單 |
| 階段一：研究準備，奠定基礎 | Stage01：選題與研究問題 | 1.4 | 題目不能一直漂移，否則後面文獻與證據都會失焦。 | 把研究問題定下來，不要一直改題目。 | 凍結 Research Questions，確認每個 RQ 都能被文獻與 artifact evidence 支撐。 | v |  | `RESEARCH_QUESTIONS.md`、`RQ_DECISION_LOG.md` |
| 階段一：研究準備，奠定基礎 | Stage02：文獻搜尋與閱讀 | 2.1 | 題目是否成立，要先看學術界和 working paper 是否已有相同或相近研究。 | 請 AI 去各大資料庫找相關研究。 | 搜尋 arXiv、SSRN、OpenAlex、Semantic Scholar、Google Scholar、Crossref、AIS eLibrary、ACM DL、IEEE Xplore、Scopus / Web of Science。 |  | v | `SEARCH_LOG.md` |
| 階段一：研究準備，奠定基礎 | Stage02：文獻搜尋與閱讀 | 2.2 | 這題可能落在 AI writing、HCI、DSR、IS 或 scholarly communication，必須先定位。 | 把相關領域整理出來，看這題靠近哪個學術圈。 | 整理 AI writing、interactive documents、executable documents、AI IDE、DSR、methodology engineering 等相鄰文獻。 |  | v | `LITERATURE_CANDIDATES.md` |
| 階段一：研究準備，奠定基礎 | Stage02：文獻搜尋與閱讀 | 2.3 | AI 可以找文獻，但核心文獻是否真的支持本文，必須由人類讀原文。 | 重要文獻不能只看摘要，必須人類讀原文。 | 閱讀核心原文，確認哪些文獻真正支持或挑戰本研究題目。 | v |  | 核心文獻核查紀錄 |
| 階段一：研究準備，奠定基礎 | Stage02：文獻搜尋與閱讀 | 2.4 | 這一步決定論文是否有研究價值，避免把普通實作包裝成學術貢獻。 | 判斷這題是不是值得寫，不能自己騙自己。 | 判斷題目是否已被做過、本文不能主張什麼、本文可以主張什麼、最適合投稿到哪個研究社群。 | v | v | `TOPIC_FIT_AND_LITERATURE_POSITIONING.md` |
| 階段一：研究準備，奠定基礎 | Stage02：文獻搜尋與閱讀 | 2.5 | 假文獻或不支持主張的文獻會直接傷害論文可信度。 | 把查不到或不支持主張的引用剔除。 | 排除不存在、未確認或不支持主張的 citation。 | v | v | `REJECTED_REFERENCES.md` |
| 階段一：研究準備，奠定基礎 | Stage02：文獻搜尋與閱讀 | 2.6 | 如果題目太大或不成立，要及早縮小、轉向或停止。 | 最後決定繼續、縮小、轉向，還是停止。 | 做出題目正確性決策：`Go / Narrow / Pivot / Stop`。 | v |  | Topic Fit Gate |
| 階段一：研究準備，奠定基礎 | Stage03：研究設計與方法 | 3.1 | 這篇要避免像產品介紹，必須把 Toolkit 定位成可研究的 artifact。 | 決定這篇不是產品介紹，而是研究一個設計出來的知識製品。 | 決定 artifact 的核心貢獻：方法論工程、AI-native eBook production、reader-queryable knowledge artifact，或 AI IDE-based professional knowledge production。 | v |  | Artifact framing decision |
| 階段一：研究準備，奠定基礎 | Stage03：研究設計與方法 | 3.2 | DSR 框架能讓審稿人理解這不是普通文件，而是設計、建構與評估的製品。 | 用正式研究框架包裝這個製品。 | 套用 Hevner / Peffers DSR 結構，整理 artifact purpose、context、design principles、evaluation logic。 |  | v | `DSR_ARTIFACT_FRAMING.md` |
| 階段一：研究準備，奠定基礎 | Stage03：研究設計與方法 | 3.3 | 不研究的範圍也要寫清楚，避免審稿人期待錯誤。 | 先說清楚這篇要研究什麼，也說清楚不研究什麼。 | 定義 baseline、研究邊界與不研究範圍。 | v | v | `RESEARCH_SCOPE.md` |
| 階段一：研究準備，奠定基礎 | Stage03：研究設計與方法 | 3.4 | 如果文字太像產品 DM，就要退回重寫。 | 檢查文章是不是還像學術論文，不是業務簡報。 | 檢查研究對象是否清楚是 DSR artifact / methodology artifact，而不是產品行銷文。 | v | v | Artifact Framing Gate |
| 階段一：研究準備，奠定基礎 | Stage04：資料收集與整理 | 4.1 | Toolkit 裡有文件、語言版本、workflow、release 與 DOI，這些都可能成為論文證據。 | 把已有成果全部列出來，知道可以拿什麼當證據。 | 盤點 Toolkit 內容、文件數、語言數、workflow、release、DOI、manifest，整理 artifact inventory。 |  | v | `ARTIFACT_INVENTORY.md` |
| 階段一：研究準備，奠定基礎 | Stage04：資料收集與整理 | 4.2 | 不是所有素材都適合公開，論文必須先區分公開證據與內部資料。 | 先分清楚哪些能公開，哪些不能公開。 | 決定哪些素材可以公開成研究證據，哪些內容因機密或授權限制不能公開。 | v |  | 公開 / 不公開素材清單 |
| 階段一：研究準備，奠定基礎 | Stage04：資料收集與整理 | 4.3 | Toolkit 的規模與版本是論文證據，不能只靠口頭描述。 | 請 AI 把可驗證的數字抓出來。 | 抽取文件數、語言數、workflow 數、版本資訊、manifest 對照、Git release、DOI metadata。 |  | v | `EVIDENCE_MANIFEST.md` |
| 階段一：研究準備，奠定基礎 | Stage04：資料收集與整理 | 4.4 | 每個數字都要能回到來源檔案、版本或 release。 | 建立證據來源表，讓別人能追查。 | 建立 provenance table，對齊數字、來源、版本與可查核位置。 |  | v | `PROVENANCE_TABLE.md` |
| 階段二：研究執行，產生內容 | Stage05：資料分析與驗證 | 5.1 | AI-Native eBook 相關概念可能早有前身，必須尊重既有研究。 | 不能把別人早就做過的事說成自己的創新。 | 比對核心文獻、相鄰研究與本研究 artifact，確認 novelty 邊界。 | v | v | `NOVELTY_RISK_TABLE.md` |
| 階段二：研究執行，產生內容 | Stage05：資料分析與驗證 | 5.2 | 這一步確保論文不是口號，而是有可查核 evidence。 | 所有數字都要能被查到，不能只是口頭說。 | 確認所有數字、版本、release、DOI、workflow 數量都可被查核。 | v | v | Evidence Verification Gate |
| 階段二：研究執行，產生內容 | Stage05：資料分析與驗證 | 5.3 | 潤稿前先查每個主張是否站得住。 | 先做主張與證據對照表，不急著潤稿。 | 建立 claim-evidence matrix，標示 unsupported claim、overclaim、missing citation、weak evidence。 |  | v | `CLAIM_EVIDENCE_MATRIX.md` |
| 階段二：研究執行，產生內容 | Stage05：資料分析與驗證 | 5.4 | 人類要決定哪些話能講，哪些話太滿。 | 決定哪些話可以講，哪些要刪掉或降級。 | 決定哪些主張保留、降級、刪除或改寫。 | v |  | Claim-Evidence Gate |
| 階段二：研究執行，產生內容 | Stage06：論文架構與大綱 | 6.1 | DSR 論文需要把問題、artifact、設計原則、證據與貢獻排成合理順序。 | 先定論文骨架，再開始寫段落。 | 決定最終 DSR 論文架構與 artifact evaluation plan。 | v |  | DSR 架構定稿 |
| 階段二：研究執行，產生內容 | Stage06：論文架構與大綱 | 6.2 | AI 可以協助產生多種大綱，但不能決定最終論證順序。 | 請 AI 提出不同大綱版本，供人類比較。 | 產生 outline candidates、section map、claim order。 |  | v | `OUTLINE_CANDIDATES.md` |
| 階段二：研究執行，產生內容 | Stage06：論文架構與大綱 | 6.3 | 最終大綱要能對應 RQ、文獻、artifact evidence 與 claim-evidence matrix。 | 確認每一章都有存在理由。 | 檢查大綱與 RQ、文獻、證據、貢獻是否一致。 | v | v | `OUTLINE.md` |
| 階段二：研究執行，產生內容 | Stage07：撰寫初稿 | 7.1 | 多個 AI 工具可以協作，但任務必須由人類分派。 | 人類先分派工作，不能讓 AI 自己亂寫整篇。 | 分派 AI 工具任務、設定語氣、決定哪些段落可寫、哪些段落只能整理證據、哪些主張不能擴張。 | v |  | Draft task brief |
| 階段二：研究執行，產生內容 | Stage07：撰寫初稿 | 7.2 | Antigravity 適合做多代理發散與不同角度探索。 | 用 Antigravity 幫忙發散架構。 | Antigravity 協助多代理發散結構。 |  | v | 結構候選 |
| 階段二：研究執行，產生內容 | Stage07：撰寫初稿 | 7.3 | Claude Code 適合處理長脈絡與大篇幅整合。 | 用 Claude Code 幫忙整合長篇脈絡。 | Claude Code 協助長 context 綜合。 |  | v | 綜合草稿 |
| 階段二：研究執行，產生內容 | Stage07：撰寫初稿 | 7.4 | Codex 適合檢查檔案一致性、版本、引用與工程證據。 | 用 Codex 幫忙檢查文件與工程一致性。 | Codex 協助工程嚴謹、檔案一致性、版本檢查與引用格式檢查。 |  | v | 一致性檢查紀錄 |
| 階段二：研究執行，產生內容 | Stage07：撰寫初稿 | 7.5 | AI 寫得順不代表可信，段落仍要對應證據。 | 人類要審 AI 寫出來的段落是否有證據。 | 審查 AI 產出的段落是否都有任務來源與證據對應。 | v |  | Draft Control Gate |
| 階段三：寫作與修訂，精煉論述 | Stage08：修改與潤稿 | 8.1 | 投稿前要先模擬最難纏的審稿意見。 | 請 AI 扮演很挑剔的審稿人。 | 扮演 reviewer 2，找出 novelty 不足、method 不清、evidence 不足、generalizability 過弱、ethics 不清等問題。 |  | v | `REVIEWER_RED_TEAM.md` |
| 階段三：寫作與修訂，精煉論述 | Stage08：修改與潤稿 | 8.2 | AI 可以提出批評，但是否接受要由人類判斷。 | 人類決定哪些批評要接受，哪些要反駁。 | 決定哪些批評要回應、哪些主張要收斂、哪些實驗或證據要補，哪些批評可有理據地拒絕。 | v |  | revision decision |
| 階段三：寫作與修訂，精煉論述 | Stage08：修改與潤稿 | 8.3 | 審稿攻擊要轉成可執行的修訂任務。 | 把所有修改工作整理成清單。 | 建立 revision matrix 與修訂清單。 |  | v | revision matrix |
| 階段三：寫作與修訂，精煉論述 | Stage08：修改與潤稿 | 8.4 | 最後確認弱點已處理，不能只靠修辭硬撐。 | 確認弱點已處理，不靠漂亮文字硬撐。 | 確認主要反駁已處理或誠實揭露，沒有用文字包裝掩蓋證據不足。 | v | v | Revision Sign-off Gate |
| 階段三：寫作與修訂，精煉論述 | Stage09：引用與參考文獻 | 9.1 | 引用錯誤會讓整篇論文失去可信度。 | 每條引用都要能查到原始來源。 | 核對文獻作者、年份、題名、DOI、出版來源與引用格式。 |  | v | reference check |
| 階段三：寫作與修訂，精煉論述 | Stage09：引用與參考文獻 | 9.2 | 核心文獻不能只靠 AI 摘要。 | 關鍵引用由人類讀原文確認。 | 確認關鍵文獻是否真的支持本文主張。 | v |  | citation approval |
| 階段三：寫作與修訂，精煉論述 | Stage09：引用與參考文獻 | 9.3 | 不支持主張的文獻要從正文移除。 | 把有問題的引用移到拒絕清單。 | 更新 `REJECTED_REFERENCES.md` 與 bibliography。 | v | v | Citation Gate |
| 階段三：寫作與修訂，精煉論述 | Stage10：圖表與視覺化 | 10.1 | AI-Native eBook 論文需要圖表說明系統化流程與 artifact 結構。 | 先決定哪些內容值得畫成圖。 | 決定研究流程圖、artifact architecture、claim-evidence map、publication roadmap 等圖表需求。 | v |  | figure plan |
| 階段三：寫作與修訂，精煉論述 | Stage10：圖表與視覺化 | 10.2 | AI 可以協助產生圖表草案，但不能製造不存在的結果。 | 請 AI 協助產生圖表或圖片草稿。 | 協助產生視覺稿、caption、圖表說明與檔案命名。 |  | v | figure draft |
| 階段三：寫作與修訂，精煉論述 | Stage10：圖表與視覺化 | 10.3 | 圖表要和資料、主張、版本一致。 | 檢查圖表有沒有誤導。 | 確認圖表、caption、資料來源與論文主張一致。 | v | v | Figure Gate |
| 階段三：寫作與修訂，精煉論述 | Stage11：投稿與期刊選擇 | 11.1 | DOI 後還要決定學術傳播路線，不是上傳完就結束。 | 決定後續要走 SSRN、arXiv、研討會還是期刊。 | 決定投稿策略、是否先 SSRN / arXiv、是否投 conference 或 journal，以及是否等待補充實驗與 reviewer red-team。 | v |  | Venue strategy decision |
| 階段三：寫作與修訂，精煉論述 | Stage11：投稿與期刊選擇 | 11.2 | 不同 venue 對 DSR、HCI、IS、AI writing 的接受度不同。 | 請 AI 幫忙比較不同期刊和會議適不適合。 | 比較期刊與會議適配度，整理格式要求、預印本政策、投稿風險、審稿週期與時程。 |  | v | `VENUE_STRATEGY.md` |
| 階段三：寫作與修訂，精煉論述 | Stage11：投稿與期刊選擇 | 11.3 | 投稿要符合 venue 政策，避免一稿多投或預印本違規。 | 確認沒有投錯地方，也沒有違反預印本規則。 | 檢查投稿 venue 與論文定位是否一致，且不違反預印本政策。 | v | v | Venue Fit Gate |
| 階段三：寫作與修訂，精煉論述 | Stage11：投稿與期刊選擇 | 11.4 | 預印本公開前，版本、作者、摘要和限制都要先定。 | 決定要不要公開、用哪個版本公開。 | 決定是否公開、版本號、作者資訊、授權、摘要、限制聲明與 DOI metadata。 | v |  | Release decision |
| 階段三：寫作與修訂，精煉論述 | Stage11：投稿與期刊選擇 | 11.5 | DOI 上傳需要 metadata、版本說明與檔案檢查。 | 請 AI 幫忙準備 Zenodo / DOI 上傳資料。 | 產生 Zenodo upload metadata、版本說明、changelog、PDF checklist、公開前檢查表。 |  | v | `ZENODO_UPLOAD_INFO.md` |
| 階段三：寫作與修訂，精煉論述 | Stage11：投稿與期刊選擇 | 11.6 | 正式公開必須由人類執行並承擔責任。 | 由人類執行正式上傳或更新版本。 | 上傳或更新公開版本。 | v |  | Zenodo DOI / release note |
| 階段四：投稿與發表，學術傳播 | Stage12：回覆審稿意見 | 12.1 | 最終版本必須由人類作者負責，不是 AI 送出。 | 最後由人類確認全文與投稿責任。 | 最終確認全文、作者、引用、資料來源、倫理、公開責任與投稿送出。 | v |  | Human Release decision |
| 階段四：投稿與發表，學術傳播 | Stage12：回覆審稿意見 | 12.2 | AI 可以做最後檢查，但不能替人類決定發表。 | 請 AI 做最後格式與檔案檢查。 | 協助最後格式檢查、metadata 檢查、檔案清單檢查、引用一致性檢查。 |  | v | Final checklist |
| 階段四：投稿與發表，學術傳播 | Stage12：回覆審稿意見 | 12.3 | 審稿意見回來後，AI 可以幫忙整理，但不能替人類承諾已修改。 | 把審稿意見拆成逐點回覆。 | 協助拆解 reviewer comments、建立 response matrix 與修訂建議。 |  | v | response matrix |
| 階段四：投稿與發表，學術傳播 | Stage12：回覆審稿意見 | 12.4 | 是否接受審稿意見、補實驗或反駁，要由人類決定。 | 人類決定如何回覆審稿人。 | 決定接受、部分接受或有理據地不同意 reviewer comments。 | v |  | response decision |
| 階段四：投稿與發表，學術傳播 | Stage12：回覆審稿意見 | 12.5 | AI 參與過程可以被揭露，但不能承擔作者責任。 | 確認 AI 不是作者，也不能替人類負責。 | 確認人類作者承擔最終責任，AI 不作為作者責任替代者。 | v |  | Human Release Gate |
| 階段四：投稿與發表，學術傳播 | Stage12：回覆審稿意見 | 12.6 | 所有公開版本與投稿包都要留痕，方便未來追蹤與回覆審稿。 | 保存最後版本與投稿包，留下紀錄。 | 保存最終稿、投稿包、release note、公開版本紀錄。 | v | v | final package |

---

## 3. 判讀規則

| 情況 | 解讀 |
| --- | --- |
| 研究人員欄位有 `v`，AI 欄位空白 | 只能由人類判斷或負責，AI 不應替代 |
| AI 欄位有 `v`，研究人員欄位空白 | AI 可先執行，但結果仍需在後續 Gate 被人類審查 |
| 兩欄都有 `v` | AI 可協助執行或檢查，但人類必須共同確認 |
| Gate / 產出 欄位是 Gate | 代表該列是階段檢查點 |
| Gate / 產出 欄位是檔名 | 代表該列完成後應留下可追溯文件 |

---

## 4. 人類與 AI 的不可混淆邊界

### 4.1 研究人員必須負責

- 研究題目的最終選擇。
- 是否構成研究貢獻。
- 是否公開 DOI。
- 是否投稿 arXiv / SSRN / conference / journal。
- 作者排序與作者責任。
- 研究倫理與資料公開範圍。
- 對 reviewer、讀者與學術社群負責。

### 4.2 AI 可以協助

- 發散候選研究方向。
- 搜尋資料庫與文獻。
- 建立 literature map。
- 整理研究問題候選。
- 草擬段落。
- 建立 claim-evidence matrix。
- 模擬 reviewer red-team。
- 協助格式、metadata、changelog、投稿清單。

### 4.3 AI 不可以做

- 自行宣布 novelty。
- 自行捏造文獻。
- 自行決定研究問題。
- 自行決定實驗結果解讀。
- 自行決定作者名單。
- 自行決定投稿或 DOI 公開。
- 用漂亮文字掩蓋證據不足。

---

## 5. 一句話總結

> **文筆與靈感只是外顯表現；真正的論文寫作是從選題、文獻、方法、資料、分析、架構、撰寫、修訂、引用、圖表、投稿到審稿回覆的一套系統化流程。AI 可以協助每一步，但不能取代人類研究者的判斷與責任。**
