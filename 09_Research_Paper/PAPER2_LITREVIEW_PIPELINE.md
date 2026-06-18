# Paper #2 文獻回顧管線：用 research-hub + ai-research-skills

> 🎯 給 **Paper #2 —— *L1-L5: A Generative AI Adoption Maturity Model for Enterprises***（目標 *Business Process Management Journal*）的文獻回顧用。
> Paper #2 是**實證成熟度模型**論文，需要正式的 related-work（成熟度模型、BPM-MM、CMM、DSR、GenAI 採用），這是我們相對弱的一塊。
> 工具來源：[`90_References/AI_RESEARCH_TOOLING_REFERENCE.md`](../90_References/AI_RESEARCH_TOOLING_REFERENCE.md)。

---

## 0. 為什麼是這條管線

Paper #2 和現在這篇（方法論生產）不同：它要**站在文獻上做實證主張**，審稿者會嚴查 related-work 與引用真偽。我們的痛點：
- 文獻發現靠手動 Google Scholar，容易漏。
- 引用容易出現「LLM 記得但其實不存在」的幻覺條目。

research-hub 正好補這兩點：**發現**（arXiv / Semantic Scholar / Crossref）+ **真偽查核閘**（擋下無法查證的引用、記錄理由）。

---

## 1. 前置安裝（你自己跑一次）

> research-hub 是 MIT、Python 3.10+。以下為**外部工具安裝**，不併進 toolkit repo。

```bash
# 1. 取得
git clone https://github.com/WenyuChiou/research-hub
cd research-hub

# 2. 安裝（依其 README / docs/quickstart）
pip install -e .            # 或其指定方式

# 3. 介面三選一
#   (a) CLI：  research-hub --help
#   (b) MCP：  在 Claude Code / Cursor 設定 MCP server 指向 research-hub
#   (c) REST： 啟動 /api/v1/* 服務
```

MCP 接入 Claude Code 後，就能在 IDE 對話裡直接呼叫它的 search / ingest / brief / ask 操作。

---

## 2. 五階段管線（對應 research-hub 操作）

```
階段 1 發現  ── research-hub discover（arXiv / Semantic Scholar / Crossref）
      ↓        關鍵詞：maturity model / BPM maturity / CMM / DSR / GenAI adoption / AI readiness
階段 2 查核  ── authenticity gate：擋下無法對外部來源查證的條目，記錄拒絕理由
      ↓        ★ 這一步是重點：進到 related-work 的每一條都通過查核
階段 3 聚類  ── cluster：把文獻分主題群（成熟度模型理論 / BPM 學派 / DSR 方法 / GenAI 採用實證）
      ↓
階段 4 摘要  ── brief：每群產 AI 摘要，當 related-work 各小節的初稿骨架
      ↓
階段 5 匯出  ── export 到 Obsidian（frontmatter）/ Zotero（CRUD），保留 DOI 供 CITATION
```

> 對照 ai-research-skills：階段 1-2 可搭其 **literature triage** skill；最後寫稿時用其 **manuscript** skill 做 claim 稽核。

---

## 3. 接回 Paper #2 的章節

| 管線產出 | 餵進 Paper #2 哪裡 |
|---|---|
| 階段 4 各主題群 brief | Related Work 各小節初稿（人改寫，不直接貼）|
| 階段 2 查核通過清單 + DOI | References + CITATION 來源（每條都查證過）|
| 階段 2 拒絕清單 + 理由 | 我們自己的稽核紀錄（言行合一：可附在 reproducibility manifest）|

---

## 4. provenance 紀律（言行合一）

我們現在這篇 preprint §10.4 主張「provenance 紀律是 AI slop 與 AI 原生學術的分界」。Paper #2 要**做到自己說的**：

- [ ] related-work 每一條引用都通過 authenticity gate
- [ ] 保留「被擋下的引用 + 理由」清單，放進 Paper #2 的 reproducibility manifest
- [ ] 不讓任何「LLM 記得但查不到」的條目進 References

> 這正是把 research-hub 的機制，變成我們發表 SOP 的硬步驟（不是裝它就好，是用它的紀律）。

---

## 5. 注意

- research-hub 連 Zotero / Obsidian / NotebookLM；若我們不用 Obsidian，可只用它的 discover + authenticity gate（CLI），匯出 BibTeX 即可。
- 它**不是 RAG 黑盒**——這點與我們反 RAG 立場一致，可放心用於文獻管理（不是拿它當論文知識庫）。
- 工具僅供**文獻回顧階段**；論文實質主張仍由我們自己的方法論與案例支撐。

---

**版本：** v0.1（2026-05-23）
**作者：** Morris Lu（盧業興）· Tiger AI 虎智科技
**授權：** 隨本 toolkit
**相關：** [`90_References/AI_RESEARCH_TOOLING_REFERENCE.md`](../90_References/AI_RESEARCH_TOOLING_REFERENCE.md)、[`README.md`](README.md)（Forthcoming papers）
