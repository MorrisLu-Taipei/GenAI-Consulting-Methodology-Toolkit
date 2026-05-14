# 顧問報告/簡報生產工作流 / Consulting Report & Deck Production Workflow

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>
>
> **引用備註 / Attribution:** 本工作流之 8 步生產流程、Dummy Page、依賴管理、7 頁面版型、progressive disclosure 等概念，參考並改寫自 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills)（MIT License）。本檔在其基礎上**重新以本方法論語言改寫，並對應到八階段顧問結構、`CONSULTING_REPORT_TEMPLATE.md` 與 3 套 deck outline**。引用與授權說明見 [`../90_References/MCKINSEY_SKILLS_REFERENCE.md`](../90_References/MCKINSEY_SKILLS_REFERENCE.md)。
> The 8-step production workflow, Dummy Page, dependency awareness, 7 page layouts, and progressive-disclosure concepts in this document are referenced from and rewritten based on [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills) (MIT License), re-expressed in this methodology's language and mapped onto our eight-stage consulting structure.

---

## 1. 這份工作流怎麼用 / How to Use This Workflow

本方法論已有：

- **八階段顧問結構** — 「怎麼診斷」（[`CONSULTING_TOOLKIT_TEMPLATES.md`](CONSULTING_TOOLKIT_TEMPLATES.md)）
- **診斷報告模板** — 「報告長什麼樣」（[`CONSULTING_REPORT_TEMPLATE.md`](CONSULTING_REPORT_TEMPLATE.md)）
- **3 套 deck outline** — 「簡報講什麼」（[`../05_Sales/`](../05_Sales/)）
- **經典框架庫** — 「用哪些分析工具」（[`CONSULTING_FRAMEWORKS_LIBRARY.md`](CONSULTING_FRAMEWORKS_LIBRARY.md)）

但少了一塊：**「怎麼高效率把八階段的診斷結果，生產成一份可交付的報告/簡報」**。本工作流補上這塊。

This methodology already has the eight-stage structure ("how to diagnose"), the report template ("what the report looks like"), 3 deck outlines ("what the deck says"), and the frameworks library ("which analytical tools"). What was missing: **how to efficiently turn the eight-stage diagnostic output into a deliverable report/deck.** This workflow fills that gap.

> 八階段產出「診斷內容」；本工作流把診斷內容**生產**成客戶手上的交付物。
> The eight stages produce the "diagnostic content"; this workflow *produces* that content into the deliverable in the client's hands.

**核心原則 / Core principles：**

1. **假設驅動** — 先立假設，再找證據，不亂蒐集資料。
2. **先骨架、後填充**（Dummy Page）— 先設計每一頁的線框，再去研究與製作。
3. **逐頁迭代** — 一次處理一頁，不要一次展開全部（避免 context 爆炸、避免無方向研究）。
4. **依賴管理** — 有些頁面要等其他頁面完成才能做（如執行摘要最後做）。
5. **證據軌** — 每頁的原始資料、來源 URL、清理過程都留下，對應本方法論的 Evidence 紀律。
6. **Progressive disclosure** — 用 AI IDE 製作時，參考檔只在需要的步驟載入、用完釋放，省 context。

---

## 2. 八步生產工作流 / The 8-Step Production Workflow

> 總時程約 90-150 分鐘（依報告規模），對應到八階段診斷**之後**或**並行**的「交付物生產」階段。

### 階段 A：問題拆解 / Problem Decomposition（20-30 分）

**Step 1 — 定義問題邊界 / Define Problem Boundaries**
- 輸入：客戶的業務問題、八階段 Stage 1-2 的現況與願景
- 做什麼：釐清範圍內 / 範圍外、定義成功指標
- 產出：有明確邊界的問題陳述
- 對應框架：SCQ（情境-衝突-問題）
- 對應八階段：Stage 1 現況掌握、Stage 5 高階問題定義
- 不載入任何參考檔，純對話

**Step 2-3 — Issue Tree + 假設 / Issue Tree + Hypotheses**
- 輸入：問題陳述
- 做什麼：用 Issue Tree 把問題拆成 MECE 的子問題；形成 5-10 個**可驗證**的假設；對每個假設做 5-10 次定向查證
- 產出：問題拆解樹 + 排序過的假設清單（附證據）
- 對應框架：MECE、Issue Tree、Hypothesis-Driven（見框架庫 §4.1）
- 對應八階段：Stage 4 差距分析

> **假設樹 / Hypothesis Tree**：一組「為什麼會有這個問題、哪些槓桿能改變它」的假設。例如「成長停滯，可能因為 (a) 獲客成本上升 (b) 流失加速 (c) 市場飽和」。每個假設後來會變成報告的一個章節或一頁。

### 階段 B：設計藍圖 / Design Blueprint（30-40 分）

**Step 4-5 — Dummy Pages + 設計規格 / Dummy Pages + Design Specs**
- 輸入：Step 3 驗證過的假設
- 做什麼：對每個假設，從 §4 的 7 個版型中選一個；指定配色、字級、資訊密度；**標註每頁的依賴狀態**（獨立 / 依賴前面的頁 / 依賴後面的頁或假設樹）；定義每頁的資料來源與 Excel 需求
- 產出：`[專案名]_DummyPages_[日期].md` — 逐頁的版型、視覺層級、依賴關係藍圖
- 對應八階段：Stage 6-7（解決方案與路徑圖的呈現設計）

> **Dummy Page（線框頁）**：不是最終投影片，而是它的「骨架規格」— 版型類型、需要的資料點、圖表類型、視覺元素。先有 Dummy Page 才去研究，避免無方向蒐集資料；也支援「換一個對話接續完成」。

### 階段 C：逐頁迭代生產 / Iterative Page Generation（40-80 分）

**Step 6-7 — 逐頁資料蒐集 → 報告頁 + Excel（每頁一個迴圈）**

對每一頁：
1. **依賴檢查**：確認需要的前置頁面是否已完成；若無，詢問使用者或提供替代方案
2. 第一次迭代時載入 Excel 資料規格
3. 為這一頁的資料需求做 2-5 次查證
4. 在 Excel 記錄原始資料 + URL（A 區），再清理 / 處理（B 區）
5. 產出符合 Dummy 設計的報告頁 — 配色、字型、圖表類型完全對齊
6. 自我檢查 6 項：版型符合、真實資料、設計一致、Excel 完整、URL 有紀錄、視覺層級
7. 暫停詢問使用者：「第 X 頁完成 — 繼續？」
8. 清掉這一頁的查證結果（釋放 context）
9. 進下一頁

- 產出：報告頁 / 投影片 + Excel 工作簿（每頁一個 sheet，含資料軌）
- 對應八階段：Stage 3-8 的內容都在此被「生產」成頁面

**Step 8 — 選配：Word 完整報告 / Optional Word Report**
- 僅在使用者要求時；產出敘事 + 資料表的完整文件
- 對應本方法論：`CONSULTING_REPORT_TEMPLATE.md` 的完整版

**Step 9 — 迭代修訂 / Iterative Refinement**
- 輸入：使用者對配色、清晰度、缺漏資料的回饋
- 做什麼：依 §9 troubleshooting playbook 做常見修正
- 產出：修訂後的頁面
- **典型修訂節奏**：2-4 輪、20-40 分鐘 — 初版生成 → 使用者回饋 → 針對性修正 → 最終潤飾。不要期待一次到位。

---

## 3. Dummy Page 概念 / The Dummy Page Concept

「先骨架、後填充」是本工作流最關鍵的紀律。

| 沒有 Dummy Page | 有 Dummy Page |
| --- | --- |
| 先狂查資料，再硬湊版面 | 先定版面骨架，再針對性查資料 |
| 研究無方向、資料蒐集爆量 | 每頁只查 2-5 筆，精準 |
| 一個對話做不完就斷線 | 骨架在，可換對話接續 |
| 設計不一致 | 全報告版型、配色、字級一致 |

**Dummy Page 規格欄位**：頁碼 / 版型類型（§4 七選一）/ 論點式標題 / 需要的資料點 / 圖表類型 / 資料來源 / 依賴狀態 / Excel 需求。

---

## 4. 7 個頁面版型 / The 7 Page Layout Templates

| # | 版型 | 結構 | 何時用 |
| --- | --- | --- | --- |
| 1 | **標題 + 單圖** | 頂部論點式標題；中部主圖佔 60-70% | 單一資料敘事（折線 / 長條 / 面積圖）|
| 2 | **標題 + 雙欄** | 左右並排：圖表 + 說明文字 | 圖文對照、比較分析 |
| 3 | **標題 + 2×2 矩陣** | 四象限定位（如 BCG 矩陣）| 策略定位 |
| 4 | **標題 + 表格** | 多維度比較表 | 競品功能比較、多選項對照 |
| 5 | **標題 + 瀑布圖** | 逐項拆解成長動因 / 價值變化 | 拆解貢獻、橋接分析 |
| 6 | **標題 + 時間軸** | 橫向時間軸 + 輔助圖 | 歷史進程、發展階段 |
| 7 | **洞察摘要** | 3-5 個編號洞察框 | 章節結論、建議收斂 |

**快速選版型**：趨勢→單圖；比較→雙欄/表格；策略→2×2 矩陣；拆解→瀑布圖；演進→時間軸；結論→洞察摘要。

> 論點式標題（assertion title）：標題本身就是結論，不是「市場分析」而是「市場成長放緩 18%，主因獲客成本上升」。對應 Pyramid Principle（框架庫 §4.1）。

---

## 5. 依賴管理 / Dependency Awareness

頁面有三種依賴狀態，決定生產順序：

| 依賴狀態 | 何時生產 | 範例 |
| --- | --- | --- |
| **獨立** | 立即生產 | 產業背景頁、市場規模頁 |
| **依賴前面的頁** | 等前置頁完成 | 「綜合以上三點」的小結頁 |
| **依賴全部 / 假設樹** | 最後生產 | 執行摘要、整體建議頁 |

> 執行摘要永遠最後做 — 它依賴所有其他頁。先做執行摘要會造成返工與資訊缺口。

---

## 6. Excel 證據軌 / The Excel Evidence Trail

每一頁對應 Excel 一個 sheet，分兩區：

- **A 區 — 原始資料**：每筆資料 + 來源 URL + 擷取時間
- **B 區 — 清理後資料**：處理 / 計算 / 對齊後，用於圖表的資料

這對應本方法論的 **Evidence 紀律**（IPOE 的 E、Stage Gate 的必備 evidence）：報告的每個數字都可追溯到來源。客戶或內稽要查證時，Excel 就是審計軌。

---

## 7. Progressive Disclosure：用 AI IDE 製作時的 context 管理

本工作流原始設計是給 AI 助手（如 Claude Code / Antigravity）執行的。關鍵技巧：

- **參考檔只在需要的步驟載入** — 例如方法論說明檔只在 Step 2-3 載入，用完即釋放。
- **逐頁處理、用完即清** — 每頁只保留 ~5 筆查證結果，做完清掉。
- **效果**：單一對話可處理 20-25 頁而不爆 token。

> 這也是本方法論 L2 / L4 課程的延伸應用：把「顧問報告生產」本身變成一個可被 AI IDE 執行的 Skill / Workflow。

---

## 8. 對應本方法論既有素材 / Mapping to Existing Methodology Assets

| 本工作流的元素 | 對應到 |
| --- | --- |
| Step 1-3 問題拆解 | 八階段 Stage 1、4、5；框架庫 SCQ / MECE / Issue Tree |
| Step 4-5 Dummy Pages | 3 套 deck outline（`05_Sales/*_DECK_OUTLINE.md`）的「逐頁規格」化 |
| Step 6-7 逐頁生產 | `CONSULTING_REPORT_TEMPLATE.md` 各章節的實際填充 |
| 7 頁面版型 | 補強 `05_Sales/VISUAL_ASSETS_SPEC.md`（原本只有 3 個特定視覺）|
| Excel 證據軌 | IPOE 的 Evidence、Stage Gate 必備 evidence |
| 論點式標題 | 框架庫 Pyramid Principle |
| Progressive disclosure | L2 Antigravity / L4 Hermes 課程的 context 管理 |

---

## 9. Troubleshooting Playbook / 報告生產問題排除

> 報告/簡報生產過程中的 7 個常見問題與修法。對應 Step 9 迭代修訂。
> 內容參考自 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills) 之 `troubleshooting.md`（MIT），已重新以本方法論語言改寫。

| # | 問題 / Problem | 徵狀 | 修法 / Fix |
| --- | --- | --- | --- |
| 1 | **深色底文字看不見** | 深藍底的頁首 / 洞察框 / 序號標籤變不可見 | 逐一檢查 shape，深色底一律強制白字（見設計規則「深色底必用白字」）|
| 2 | **元素重疊** | 標題框與內容框疊在一起、圖表被文字蓋住 | 移除所有 shape，系統性重建版面；元素間至少保留 0.2" 間距 |
| 3 | **文字溢出** | 內容超出容器邊界 | 三選一：縮字級（9pt→8pt）/ 容器加高（×1.3）/ 精簡文字 |
| 4 | **圖表標籤顯示不全** | 長條圖的次要標籤消失 | 標籤框高度不足；把標籤框高度加到 0.35" 以容納多行 |
| 5 | **時間軸與圖寬度不一致** | 時間軸與內容圖寬度對不齊 | 設一個統一寬度常數（8.4"），全簡報所有內容元素都用它 |
| 6 | **資訊密度過高** | 單頁塞了 10+ 個重點 | 拆成 2-3 頁，每頁聚焦，提升可讀性（見密度標準）|
| 7 | **形狀樣式違規** | 大文字框用了圓角 | 大文字框只用直角矩形；圓角只給 < 1.5" 的小標籤 |

> **典型修訂節奏**：2-4 輪、20-40 分鐘 — 初版生成 → 使用者回饋 → 針對性修正 → 最終潤飾。

---

## 10. 引用與授權 / Citation & License

本工作流之 8 步流程、Dummy Page、依賴管理、7 頁面版型、progressive disclosure 等概念，參考並改寫自 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills)（MIT License，作者 @Kafurtan）。本檔已重新以本方法論語言改寫，並對應到八階段顧問結構與既有交付素材；McKinsey Problem Solving、MECE、Pyramid Principle 等為公開領域之管理知識。

完整引用與授權說明見 [`../90_References/MCKINSEY_SKILLS_REFERENCE.md`](../90_References/MCKINSEY_SKILLS_REFERENCE.md)。

The 8-step workflow, Dummy Page, dependency awareness, 7 page layouts, and progressive-disclosure concepts in this workflow are referenced from and rewritten based on [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills) (MIT License, by @Kafurtan). This document has been re-expressed in this methodology's language and mapped to the eight-stage consulting structure and existing delivery assets; McKinsey Problem Solving, MECE, and the Pyramid Principle are public-domain management knowledge. Full citation: `../90_References/MCKINSEY_SKILLS_REFERENCE.md`.
