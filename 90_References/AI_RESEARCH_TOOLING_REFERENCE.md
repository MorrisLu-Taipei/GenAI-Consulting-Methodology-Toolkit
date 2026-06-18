# AI 研究工具參考：WenyuChiou 的 ai-research-skills 與 research-hub

> 🌐 語言：繁體中文（本檔）｜ English（待補 TODO）
> 🎯 **這份檔回答一個問題：以後 Tiger AI 要發表論文，可以從 WenyuChiou 的兩個開源專案「參考／借用」什麼？**
> 對應論文 [`09_Research_Paper/`](../09_Research_Paper/) 的發表實務；兩個 repo 已在 preprint §2.3 / §10.4 / References §C 作為 Tier-3「獨立收斂」佐證引用。

---

## 0. 兩個 repo 是什麼（一句話 + 授權）

| Repo | 一句話 | 授權 | 成熟度 |
|---|---|---|---|
| **[ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | 15 個 Claude Code **skills**：文獻分流、研究設計、稿件修訂（含 claim 稽核 / 禁用詞偵測 / 審稿回覆）、Zotero、Codex/Gemini 委派 | **MIT** | agentskills.io 規範、catalog 索引 |
| **[research-hub](https://github.com/WenyuChiou/research-hub)** | 串 Zotero + Obsidian + NotebookLM 的**本地優先工作管線**（找論文、查證真偽、聚類、產 brief）；MCP server + CLI + REST + Web | **MIT** | v0.95、82 releases、479 commits、Python 3.10+ |

> 同一作者（GitHub handle `WenyuChiou`）。兩者互補：**skills 是「能力清單」、research-hub 是「天天用的產線」。**

---

## 1. 可參考的「發表實務元件」（最該借的——直接強化我們的發表管線）

我們發表論文的痛點是：**幻覺引用、投稿用語膨脹、審稿回覆耗時、文獻回顧從零開始**。這四件，他兩個 repo 都有對應的可借元件：

| 我們的痛點 | 可借元件 | 來源 | 怎麼用在 Tiger AI |
|---|---|---|---|
| 幻覺 / 假引用 | **authenticity gate**：無法對外部來源查證的引用→隔離 + 記錄拒絕原因 | research-hub | 把這個**紀律**寫進我們既有的 `/evidence-audit` workflow（不是裝它，是學它的「擋下並記錄理由」機制）|
| 投稿用語膨脹（hype words）| **banned-word / claim auditing** skill | ai-research-skills | 新增一個 `/claim-audit` 或 `/hype-scrub` workflow，投稿前掃描「revolutionary / seamless / cutting-edge」這類詞 + 標出無證據主張 |
| 審稿回覆耗時 | **reviewer-response generation** skill | ai-research-skills | 新增 `/reviewer-response` workflow：吃審稿意見 → 產出逐點回覆草稿（人改）|
| 文獻回顧從零開始 | **literature triage** skill + research-hub 的 discover→cluster→brief | 兩者 | Paper #2 / #3 的文獻回顧管線（見 [`09_Research_Paper/PAPER2_LITREVIEW_PIPELINE.md`](../09_Research_Paper/PAPER2_LITREVIEW_PIPELINE.md)）|

> ⭐ **最高價值借用：authenticity gate 的紀律。** 我們論文的核心論點就是「provenance 紀律是 AI slop 與 AI 原生學術的分界」（§10.4）。把「擋下無法查證的引用並記錄理由」變成我們發表 SOP 的硬步驟，是**言行合一**——我們主張的東西，自己要先做到。

---

## 2. 可參考的「設計立場 / 理念」（佐證我們、也提醒我們）

| 立場 | 他怎麼做 | 為什麼對我們重要 |
|---|---|---|
| **非 RAG / 不要 opaque RAG box** | research-hub 明講「不把文獻庫變成不透明 RAG 黑盒」 | **獨立呼應我們一貫的反 RAG 立場**（L4 課 §2.7、Bible AI 討論）。可在論文 / 演講引為「不只我們這樣想」|
| **能力 = 可組合 skills，而非單一巨型 prompt** | ai-research-skills 把研究方法拆成 15 個 schema 描述的 skill | 直接呼應我們論文 §10.2「first-class workflow specifications」的呼籲；可研究他的 schema 當我們 workflow 規格化的參考 |
| **多引擎委派** | Codex / Gemini delegation skills | 呼應我們的多 IDE 編排（Claude + Codex + Antigravity）|
| **catalog 即索引、skill 各居其 repo** | ai-research-skills 用 catalog 當索引、不做 monorepo | 我們若要把 22 個 workflows 對外發布成可重用單元，這是一種打包模式參考 |

---

## 3. 可參考的「具體工具」（裝來用，不一定併進 repo）

| 工具 | 用途 | 對哪篇論文有用 | 我方動作 |
|---|---|---|---|
| **research-hub**（MCP/CLI）| 文獻發現（arXiv / Semantic Scholar / Crossref）+ 真偽查核 + 聚類 + brief | **Paper #2**（L1-L5 實證成熟度模型，需正式文獻回顧）幫助最大 | 自行安裝；接入步驟見 `PAPER2_LITREVIEW_PIPELINE.md` |
| **ai-research-skills** 的 manuscript skill | 投稿前 claim 稽核 + 用語清理 + 審稿回覆 | **每一篇**（含現在這篇往 peer review 推進）| 可裝來用，或仿其邏輯做自己的 workflow |

---

## 4. 採用 vs 引用 vs 略過：決策表

| 元件 | 決策 | 理由 |
|---|---|---|
| authenticity-gate 紀律 | **採用（學機制）** | 言行合一；強化 `/evidence-audit` |
| claim-audit / hype-scrub / reviewer-response | **採用（做成自己的 workflow）** | 投稿剛需；用我們現有引擎即可 |
| 兩個 repo 當相關工作 | **已引用** | preprint §2.3 / §10.4 / References §C（Tier-3 獨立收斂）|
| research-hub 當文獻管線 | **使用（外部工具）** | Paper #2 lit review；不必併進 repo |
| 整包 fork 進我們 repo | **略過** | 沒必要；增加維護負擔 + 授權混合風險 |

---

## 5. 授權與 attribution 機制（重要——若把他的東西「併進」我們 repo）

兩個 repo 都是 **MIT**；我們 toolkit 是 **Apache 2.0（程式）/ CC BY 4.0（文件）**。三種情境分清楚：

1. **只引用（cite）**：沒問題，照學術慣例（已做，見 References §C）。
2. **學機制、自己重寫**（如把 authenticity-gate 的「擋下+記錄理由」邏輯寫成我們自己的 workflow，不複製其程式碼）：**沒有授權義務**，但禮貌上在 workflow 檔註明「concept inspired by research-hub (MIT)」。
3. **直接複製他的程式碼 / skill 檔進我們 repo**：**必須**保留 MIT 著作權聲明 + 在 `NOTICE` 加 attribution，比照我們對 ClawTeam（[`CLAWTEAM_REFERENCE.md`](CLAWTEAM_REFERENCE.md)）與學校 overlay 的做法。MIT 與 Apache 2.0 相容，但**不可移除原始 MIT 條款**。

> 建議：優先走情境 2（學機制、自己重寫）。乾淨、無授權混合、又能客製成我們的風格。

---

## 6. 別重造輪子：我們已經有的對照

| 他的元件 | 我們已有的對應 | 結論 |
|---|---|---|
| 對抗式 / 紅隊審查 | `/devil-pair-debate`、`/red-team-review` | 我們已有，不必借 |
| 證據稽核 | `/evidence-audit` | 已有；可借 research-hub 的「記錄拒絕理由」強化 |
| 跨檔綜合 | `/deep-synthesize` | 已有 |
| claim 稽核 / hype 清理 / 審稿回覆 | **無** | ← **這是缺口，值得新增** |
| 文獻發現 + 真偽查核管線 | **無**（我們偏重自製方法論，文獻回顧較弱）| ← **Paper #2 之前要補** |

---

## 7. 結論：三句話

1. **最該借的不是工具，是紀律**——authenticity gate 的「擋下無法查證的引用並記錄理由」，讓我們論文主張的 provenance 紀律言行合一。
2. **最該補的缺口**——claim-audit / hype-scrub / reviewer-response 三個投稿 workflow（我們現在沒有），用現有引擎自己做。
3. **最該裝的工具**——Paper #2 文獻回顧時用 research-hub 當管線。

---

**版本：** v0.1（2026-05-23）
**作者：** Morris Lu（盧業興）· Tiger AI 虎智科技
**授權：** 隨本 toolkit（程式 Apache 2.0 / 文件 CC BY 4.0）
**相關：** [`09_Research_Paper/PAPER2_LITREVIEW_PIPELINE.md`](../09_Research_Paper/PAPER2_LITREVIEW_PIPELINE.md)、[`09_Research_Paper/CLAIM_AUDIT_2026-05-23.md`](../09_Research_Paper/CLAIM_AUDIT_2026-05-23.md)、preprint §2.3 / §10.4
