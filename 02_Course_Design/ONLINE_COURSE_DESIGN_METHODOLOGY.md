# 線上課程設計方法論 / Online Course Design Methodology

> 🌐 語言：繁體中文（本檔） ｜ [English](ONLINE_COURSE_DESIGN_METHODOLOGY_EN.md)

## 一、本文件定位

本文件是 Tiger AI 所有 **L1-L5 線上課程**的**共通設計標準**。它不是替任何特定平台（Udemy / Coursera / Hahow / 自有 LMS）寫的，而是把學術界公認的學習科學原則 + 主流付費課程平台共通要求，整理成一套**內部設計 SOP**。

所有 L1-L5 課程在上架（或重新編修）前，必須以本文件的 **Tier 1 必要門檻 + 設計檢核表（§9）** 自我審查；上架到任何外部平台時，再依該平台 specific 規格做 micro-adjust。

本文件涵蓋：

- 學習設計三大理論基礎（§2）
- 線上課程的 4 大組成與 3 層門檻（§3-§6）
- 學習目標寫法（§4）
- 章節 / 講座設計準則（§5）
- 互動學習活動類型對照（§7）
- 影音與環境規格（§8）
- 課程自我 audit checklist（§9）
- L1-L5 既有課程的 audit 套用流程（§10）

---

## 二、學習設計三大理論基礎

任何「結構良好」的線上課程都建立在這三條原則之上。違反任一條，課程都會出現「學員看完卻學不會」的失敗模式。

### 2.1 Backward Design（反向設計）

**先定義學員學完後要能做什麼，再倒推教什麼、怎麼教、怎麼驗收。**

順序：

```text
1. 定學習目標（Learning Objectives, LO）
        ↓
2. 設計驗收方式（Assessment / 練習活動）
        ↓
3. 選擇教材與教學方法（Lecture / Demo / Reading）
```

不是「我會什麼就教什麼」，而是「學員要會什麼，我才設計什麼」。

> 來源：Wiggins, G., & McTighe, J. (1998). *Understanding by Design.* ASCD.

### 2.2 Constructive Alignment（建構式對齊）

**學習目標、教學活動、驗收方式**三者必須**互相對齊**。

例：

| 學習目標 | 對齊的教學活動 | 對齊的驗收方式 |
|---|---|---|
| 「能套用 L1-L5 模型診斷自己公司」 | Demo + 學員操作 + 自評範例 | Assignment：交一份自診斷報告 |
| ❌「了解 L1-L5 模型」（動詞太模糊） | Reading + Quiz on definitions | Quiz：填空背名詞 |

第二列是反例 —— 動詞「了解」不可驗收，所以驗收只能退化成背名詞，學員「會考試但不會用」。

> 來源：Biggs, J. (1996). Enhancing teaching through constructive alignment. *Higher Education*, 32(3).

### 2.3 Bloom's Taxonomy（布魯姆認知層級）

設計學習目標時，**先決定要學員達到哪一層認知**，再選對應動詞。

| 認知層級 | 動詞範例 | 適用情境 |
|---|---|---|
| **Remember** 記憶 | 列出、定義、辨識、命名 | 名詞、術語、流程步驟 |
| **Understand** 理解 | 解釋、描述、區分、比較 | 概念、理論、原理 |
| **Apply** 應用 | 套用、計算、執行、操作 | 工具、流程、模板 |
| **Analyze** 分析 | 拆解、比較、推論、診斷 | 案例、決策、流程 |
| **Evaluate** 評估 | 評估、判斷、選擇、辯護 | 方案、策略、品質 |
| **Create** 創作 | 設計、生成、合成、建構 | 產出、原創方案 |

**學員花的錢 vs. 願意達到的層級**通常呈正相關：免費 / 低價課常停在 Remember-Understand；企業內訓 / 顧問課必須衝到 Apply 以上。

> 來源：Anderson, L. W., & Krathwohl, D. R. (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.（修訂版，原版為 Bloom 1956）

---

## 三、線上課程的 4 大組成

任一門線上課程都由 4 個組件構成。**每個組件都有 3 層門檻**：

- **Tier 1 必要**：缺一不可，否則無法上架（多數平台會擋）
- **Tier 2 品質**：學習效果與評分的主要決定因素
- **Tier 3 加分**：增加銷量、評分、平台曝光

| 組件 | 內容 | 詳見 |
|---|---|---|
| **A. 課程登陸頁** | 學習目標、先決條件、目標學員、課程描述 | §4 |
| **B. 課程結構** | 章節 / 講座階層、開頭 / 中段 / 結尾、長度比例 | §5 |
| **C. 影音與環境** | 解析度、音訊、燈光、背景 | §8 |
| **D. 互動學習** | Quiz / Assignment / Practice Test / Supplement | §7 |

---

## 四、學習目標（Learning Objectives, LO）

### 4.1 公式

**[Bloom 動詞] + [內容] + [情境 / 條件]**

範例：

| LO | 為什麼好 |
|---|---|
| ✅ **套用** L1-L5 成熟度模型 **診斷** 你自己公司的 AI 現況，**產出** 一份 1 頁自評報告 | Apply 層、可驗收（產出物）、有情境 |
| ✅ **辨識** Phase A / B / C 的 3 個 Stage Gate，**判斷** 何時 Stop / Go / Pivot | Analyze 層、可驗收（判斷）、有情境 |
| ❌ 了解 AI 成熟度模型 | 動詞模糊，無法驗收 |
| ❌ 從零開始學會所有 AI 工具 | 過度承諾、無法量測、無情境 |

### 4.2 數量與規格

| 條件 | 規範 |
|---|---|
| **CLP 顯示的 LO 數** | **至少 4 條**（多數平台硬性要求） |
| **單條 LO 長度** | ≤ 160 字（避免讀者疲勞） |
| **整門課 LO 總數** | 每章節對應 1 條，全課 4-10 條視長度而定 |
| **層級分配** | 入門課可全在 Apply 以下；進階課必須有 Analyze 以上 |

### 4.3 三大陷阱

1. **關鍵字塞餵**：把所有 buzzword 都塞進 LO，反而失焦
2. **過度承諾**：「從零變專家」「精通所有 AI」這類學員看了就知道是噱頭
3. **動詞模糊**：「了解」「認識」「熟悉」都不可驗收，學員學完無法自我確認

---

## 五、課程結構

### 5.1 三幕結構（Three-Act Structure）

```text
┌─────────────────────────────────────────┐
│  開頭（Introduction）                    │
│  ≤ 10 分鐘總長                            │
│  ├─ Intro lecture（≤ 4 分鐘）            │
│  │    自我介紹 + 為什麼是你 + 課程價值   │
│  ├─ 課程結構與 LO 預告                   │
│  └─ Engagement activity（頭幾講內必須有）│
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  中段（Instructional Sections）          │
│  每 section 對應 1 個 LO                 │
│  ├─ Section 1                            │
│  │   ├─ 章節介紹（說明本章 LO）          │
│  │   ├─ 內容講座 × N                     │
│  │   ├─ 章節總結                         │
│  │   ├─ ≥ 1 個 練習 / 評量               │
│  │   └─ Reference materials              │
│  ├─ Section 2 ...                        │
│  └─ Section N ...                        │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  結尾（Conclusion）                      │
│  ├─ Recap lecture：重點回顧 + 恭喜       │
│  ├─ Next steps：學完後可以往哪走         │
│  └─ Bonus lecture（選填）                │
└─────────────────────────────────────────┘
```

### 5.2 章節（Section）設計

| 規範 | 數值 |
|---|---|
| 每章節對應 LO 數 | **1 條 LO** |
| 每章節最少講座數 | **≥ 3 講座 + 1 練習/評量** |
| 每章節結構 | 介紹 → 內容 → 總結 |
| 章節之間關係 | 後章節依賴前章節（漸進式建構） |

### 5.3 講座（Lecture）設計

| 規範 | 數值 |
|---|---|
| 單一講座覆蓋概念數 | **1 個概念** |
| 講座長度（一般） | **3-6 分鐘最佳**（2-7 分鐘可接受） |
| 講座長度（技術 / 複雜主題） | 可放寬到 8-12 分鐘 |
| 講座類型 | 露臉鏡頭 / 螢幕錄影 / 投影片 / 視覺素材**輪流出現** |
| 標題 | 清楚、可搜尋；學員從標題就知道講什麼 |

**為什麼短講座優於長講座**：

- 認知負荷研究（Sweller 1988）顯示，學員對單次資訊吸收上限約 20 分鐘
- 企業學員（特別是經理層級以上）多數在零碎時間學習，**短講座方便恢復進度**
- 模組化講座方便日後 reusable / cross-link

### 5.4 比例與長度門檻

| 條件 | 數值 |
|---|---|
| 最低講座總數 | **≥ 5 講座**（平台硬性最低） |
| 最低影片總時長 | **≥ 30 分鐘**（平台硬性最低） |
| 推薦課程長度（入門 / 短篇） | 30 分鐘 – 2 小時 |
| 推薦課程長度（中型） | 5-10 小時 |
| 推薦課程長度（旗艦） | 20 小時+ |
| 開頭佔比 | ≤ 10% |
| 結尾佔比 | ≤ 5% |
| 中段內容佔比 | ≥ 85% |

---

## 六、品質紅線

以下任一條違反，課程不能上架：

1. ❌ **不到 5 個講座** 或 **總時長不到 30 分鐘**
2. ❌ **無學習目標** 或學習目標少於 4 條
3. ❌ **學習目標動詞不可驗收**（了解 / 認識 / 熟悉）
4. ❌ **影音解析度低於 720p**
5. ❌ **音訊有回音、雜音或聲道不同步**
6. ❌ **內容含廣告、推銷無關產品或分心素材**
7. ❌ **重複別人的課程內容**（必須有自己的設計、範例、講解）
8. ❌ **章節無 LO 對應** 或無練習活動
9. ❌ **學員無法驗收自己學會了什麼**（無 assessment / 無 checklist）

---

## 七、互動學習活動類型

> 非絕對必要，但實證上**互動越多、評分越高、銷量越好**。

| 類型 | 用途 | 設計重點 |
|---|---|---|
| **Quiz** | 章節內測驗概念理解 | 多選題、立即給答案 + 解釋；不適合考細節記憶 |
| **Practice Test** | 模擬證照式考試 | 計時、覆蓋所有 domain、題後給 score report + 學習建議 |
| **Coding Exercise** | 程式碼自動評分 | 給 starter code、明確 spec、自動測試案例 |
| **Assignment** | 開放式作業 + 同儕/自評 | 給 rubric / checklist 讓學員自評；最適合 Apply 以上 LO |
| **Supplemental** | PDF / 範本 / Worksheet | 學員下載即用；最低成本最高 ROI |

### 7.1 Formative vs Summative

| 類型 | 位置 | 用途 |
|---|---|---|
| **Formative**（形成性評量） | 章節內 / 講座後 | 學員自我檢查理解；錯了可回頭重看 |
| **Summative**（總結性評量） | 課程結尾 | 驗收整門課 LO 是否達成 |

兩者**都要有**。形成性評量在每章節結尾、總結性評量在全課程結尾。

### 7.2 設計 5 大要件

每個互動活動都要符合：

1. **Clearly explained**：文字 + 影片雙重說明活動目的、期望產出、所需素材
2. **Time-estimated**：給時間估計（學員實際會比你估的久）
3. **Well-resourced**：附範本、範例、starter code
4. **Feedback-enabled**：給自評 checklist / rubric；適當時鼓勵同儕回饋
5. **Real-world contextualized**：題目要對應真實情境，不是抽象練習

---

## 八、影音與環境規格

### 8.1 規格門檻

| 項目 | 最低 | 推薦 |
|---|---|---|
| 影片解析度 | **720p** | 1080p（4K 不必，檔案太大 streaming 反而吃緊） |
| 影片碼率 | 5 Mbps | 10 Mbps |
| 音訊聲道 | L/R 雙聲道 | 同上 |
| 音訊取樣率 | 44.1 kHz | 48 kHz |
| 音訊與影片同步 | ✅ 必要 | 同上 |
| 無回音、無背景雜音 | ✅ 必要 | 同上 |

### 8.2 拍攝環境

| 項目 | 最低成本 | 推薦升級 |
|---|---|---|
| **鏡頭** | 智慧型手機 1080p（後鏡） | 1080p+ Webcam / DSLR |
| **麥克風** | 任何外接 mic（距嘴 15-30 cm） | 動圈麥（SM58 / Maono PD200X） |
| **燈光** | 自然光 + 關頂燈 | Three-point lighting（前 2、後 1） |
| **背景** | 乾淨、無雜物 | 統一色背景紙 / 燙過的純色床單 |
| **噪音控制** | 關冷氣風扇、安靜時段錄 | 吸音棉 + 地毯 + 厚窗簾 |

### 8.3 內容類型混合

每講座建議交替使用以下類型，避免學員視覺疲勞：

- **TH（Talking Head）**：講師露臉，建立信任與情感連結
- **S（Screencast）**：螢幕錄影，示範實際操作
- **Slides**：投影片，傳達結構性內容
- **Whiteboard / Visual**：手繪或動態視覺，解釋抽象概念

**比例參考**：TH 30% / Screencast 40% / Slides 20% / Visual 10%。

---

## 九、課程設計 Audit Checklist

每門課程上架前 / 重新編修前，用以下 30 點 checklist 自我審查。

### 9.1 課程登陸頁（CLP）

- [ ] 至少 4 條學習目標，每條 ≤ 160 字
- [ ] 學習目標動詞屬 Bloom Apply 以上（入門課可放寬）
- [ ] 學習目標可驗收（不出現「了解 / 認識」這類動詞）
- [ ] 先決條件清楚列出；無條件時主動降門檻
- [ ] 目標學員描述明確（年資 / 職務 / 問題）
- [ ] 課程描述包含：解決什麼問題 + 學完能做什麼 + 為什麼是你

### 9.2 課程結構

- [ ] 講座總數 ≥ 5
- [ ] 影片總時長 ≥ 30 分鐘
- [ ] 開頭 ≤ 10 分鐘，含 ≤ 4 分鐘 intro lecture
- [ ] 開頭區有 1 個 engagement activity
- [ ] 每章節對應 1 個 LO
- [ ] 每章節 ≥ 3 講座 + ≥ 1 練習/評量
- [ ] 每章節有介紹 + 內容 + 總結
- [ ] 結尾有 recap + next steps lecture

### 9.3 講座設計

- [ ] 單講座聚焦 1 個概念
- [ ] 單講座長度 3-6 分鐘（複雜主題 ≤ 12 分鐘）
- [ ] 講座標題清楚、可搜尋
- [ ] 講座類型交替（TH / S / Slides / Visual）

### 9.4 互動學習

- [ ] 至少有 Quiz 或 Assignment 之一
- [ ] 互動活動有 formative + summative 兩種
- [ ] 每個互動活動有 instruction + time estimate + 範本 + 自評 checklist
- [ ] 活動題目對應真實情境

### 9.5 影音規格

- [ ] 解析度 ≥ 720p
- [ ] 音訊雙聲道、同步、無雜音
- [ ] 背景乾淨
- [ ] 燈光不過暗

### 9.6 完整性

- [ ] Reference materials（PDF / 範本 / Checklist）已備齊
- [ ] 課程內無廣告或推銷無關產品

---

## 十、套用到 L1-L5 既有課程的 audit 流程

Tiger AI 既有 5 份 L1-L5 課程計畫（`L1_OPENWEBUI_COURSE_PLAN.md` ~ `L5_CLAWTEAM_COURSE_PLAN.md`）。每份套用本方法論的流程：

### Step 1：對照 §9 checklist 跑一次

每課程產出一份 audit gap report，格式：

```markdown
# L?_xxx_COURSE_PLAN — Audit Report

## ✅ 已符合
- ...

## ⚠️ 缺口（需編修）
- 缺口 1：[項目] / [建議補強]
- 缺口 2：...

## 🔧 編修工作量估計
- 文字補強：X 處
- 新增章節：X 個
- 新增 LO：X 條
```

### Step 2：依 gap report 排優先級

- **P0**：缺乏 LO、無練習活動、章節結構不對 → 必修
- **P1**：講座切分過大、缺 Reference materials → 應修
- **P2**：講座類型單一、欠章節介紹 → 加分

### Step 3：批次編修

依優先級批次補強，每批次完成後 commit。

### Step 4：上架前最終 audit

確認 §9 全部 ✅，才送 Udemy / Hahow / 自有 LMS。

---

## 十一、與既有方法論的關係

| 既有檔 | 與本檔的關係 |
|---|---|
| `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md` | 客戶端：搞清楚要教誰、教什麼 |
| `COURSE_MODULE_MATRIX.md` | 課程內容：模組對應 L1-L5 |
| `L1_..._COURSE_PLAN.md` ~ `L5_..._COURSE_PLAN.md` | 每級課程的內容主體 |
| **本檔（ONLINE_COURSE_DESIGN_METHODOLOGY.md）** | **跨課程的設計品質 SOP** |
| `L1_L5_COMPLETE_COURSE_PLAN.md` | L1-L5 整體規劃藍圖 |

本檔不取代任何既有課程；它是**跨課程通用的設計品質基準**。

---

## 十二、參考文獻

- Wiggins, G., & McTighe, J. (1998). *Understanding by Design.* ASCD.
- Biggs, J. (1996). Enhancing teaching through constructive alignment. *Higher Education*, 32(3), 347-364.
- Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.* Longman.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257-285.
- Mager, R. F. (1962). *Preparing Instructional Objectives.* Fearon Publishers.
- Mayer, R. E. (2009). *Multimedia Learning* (2nd ed.). Cambridge University Press.

---

**版本：** v1.0
**日期：** 2026-05-18
**作者：** Tiger AI Morris Lu 盧業興
**授權：** Apache License 2.0（與 toolkit 一致）
