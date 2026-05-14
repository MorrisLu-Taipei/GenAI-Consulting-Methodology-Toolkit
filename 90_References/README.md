# 90 References — 參考資料與第三方引用

## 一、本目錄定位

本目錄是整套方法論的**依據庫與引用治理中心**。`00`-`06` 是「方法與工具」；本目錄回答：**「這些方法的依據是什麼？哪些內容引用了第三方？授權合不合規？」**

它要解決的問題是：**一個對外開源、且大量參考第三方素材的方法論，若不把「依據」與「引用授權」管理清楚，會有兩個風險 —— (1) 使用者不知道方法論的根據、(2) 踩到第三方著作權/授權。** 本目錄集中放：原始參考資料（PDF、方法論圖）、第三方影片學習筆記、以及每一個被引用的第三方專案的**引用與授權說明檔**。

使用本目錄的人：顧問（查方法論依據）、reviewer（查授權合規）、法務（確認引用是否乾淨）、任何要再散布/商用本方法論的人。

## 二、在方法論中的位置

| 軸 | 對應 |
| --- | --- |
| 三段式服務流程 | **跨全程** —— 支撐 `00`-`06` 的依據與引用 |
| 八階段顧問結構 | 不對應單一階段；是整套方法論的依據層 |
| 授權治理 | 本 repo 採 Apache 2.0；本目錄管理所有第三方引用的授權合規 |

## 三、目標與效益

| 目標 | 效益 |
| --- | --- |
| 集中原始參考資料 | 方法論的依據可追溯 |
| 每個第三方引用都有獨立的 `*_REFERENCE.md` | 授權合規透明、可被法務/reviewer 稽核 |
| 統一引用原則 | 改寫不 fork、明確署名、各檔內 + reference 檔雙重備註 |
| 影片學習筆記與原始來源分離 | 清楚標示「衍生筆記」vs「原始內容版權」 |

**若跳過本目錄**：方法論無依據、第三方引用散落各處無法稽核、再散布時踩授權風險。

## 四、引用原則與使用邏輯

本方法論引用第三方素材時，一律遵守以下原則（即「方案 A」）：

1. **獨立改寫，不 fork、不重製原始碼** —— 參考其結構與概念後，以本方法論的語言重新撰寫。
2. **明確署名** —— 在引用該素材的檔案 header + 本目錄的 `*_REFERENCE.md` 雙重備註原作者與授權。
3. **generalize 到本方法論情境** —— 把領域特定內容轉為 L1-L5 AI 轉型顧問情境。
4. **無授權者不碰** —— 沒有 LICENSE 的第三方專案不整合（只能當外部範例引用網址）。

**使用邏輯**：要查「某個目錄的某份檔案引用了什麼」→ 看該檔 header 的「引用備註」→ 轉到本目錄對應的 `*_REFERENCE.md` 看完整授權說明。

## 五、檔案說明

### 原始參考資料與圖

| 檔案 | 用途 |
| --- | --- |
| `@AI-MD-PUBIC.pdf` | AI 轉型成熟度模型公開版手冊。 |
| `MD-Map.png` | AI 成熟度地圖，用於根目錄 README 的成熟度總覽。 |
| `Metholodgy.png` | 企業管理顧問八階段轉型指南，用於根目錄 README 的方法論總覽。 |

### 第三方影片學習筆記（衍生筆記，原始影片版權歸原創作者）

| 檔案 | 用途 |
| --- | --- |
| `OPENWEBUI_VIDEO_LEARNING_NOTES.md` | OpenWebUI 公開 playlist 的學習紀錄與 L1 課程應用對照。 |
| `TIGERAI_VIDEO_LEARNING_NOTES.md` | TigerAI 頻道影片學習紀錄，聚焦 n8n / L3 課程應用。 |

### 第三方專案引用與授權說明

| 檔案 | 引用對象 / 授權 | 對應目錄 |
| --- | --- | --- |
| `CLAWTEAM_REFERENCE.md` | HKUDS/ClawTeam（MIT）| L5 課程平台（`02`）|
| `AGENCY_AGENTS_REFERENCE.md` | msitarzewski/agency-agents（MIT）| L2 agent persona 庫（`02`）|
| `N8N_SKILL_PACK_REFERENCE.md` | MorrisLu-Taipei/TigerAI-n8n-Skill-Pack（混合授權）| L3 課程下半段（`02`）|
| `CONSULTANT_FRAMEWORKS_REFERENCE.md` | yoichiojima-2/consultant（MIT）| 經典顧問框架庫（`03`）|
| `MCKINSEY_SKILLS_REFERENCE.md` | Kafurtan/mckinsey-consultant-skills（MIT）| 報告生產工作流（`03`）|
| `WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md` | Mirza Iqbal / next8n.com（MIT）| 接案營運層（`06`）|
| `AWESOME_LLM_APPS_REFERENCE.md` | Shubhamsaboo/awesome-llm-apps（Apache-2.0）| LLM 應用案例索引（`04`）|
| `AI_ENGINEERING_HUB_REFERENCE.md` | patchy631/ai-engineering-hub（MIT）| LLM 應用案例索引（`04`）|

### `*_EN.md`

部分檔案的英文版 sibling。

## 六、署名

本目錄中由 Tiger AI Morris Lu 盧業興原創之內容，採用根目錄 [`LICENSE`](../LICENSE) 的 Apache License 2.0，可自由使用、修改、改作與商業化。再散布時請保留 [`NOTICE`](../NOTICE) 中的作者署名：

```text
原作者：Tiger AI Morris Lu 盧業興
身份：n8n Taipei 大使 / 臺灣科技大學 智慧製造所博士生 / QUT 澳洲昆士蘭科技大學 資工碩士
```

第三方平台名稱、商標、影片、外部專案與引用內容仍屬於各自權利人。本 repo 對第三方資料僅做學習紀錄、引用、整理與課程設計參考，未重製或 fork 原始碼。各第三方之授權與引用範圍詳見上表對應的 `*_REFERENCE.md`。

## 七、與其他目錄的對應

| 目錄 | 與本目錄的關係 |
| --- | --- |
| `00_Overview` | 故事線中的方法論圖（Metholodgy.png / MD-Map.png）來自此 |
| `02_Course_Design` | L1/L2/L3/L5 課程的第三方引用（OpenWebUI 筆記、agency-agents、n8n-Skill-Pack、ClawTeam）|
| `03_Consulting_Report` | 框架庫與報告工作流的第三方引用（consultant、mckinsey-skills）|
| `04_Scenarios` | LLM 應用案例索引的第三方引用（awesome-llm-apps、ai-engineering-hub）|
| `06_Delivery` | 接案營運層的第三方引用（Mirza Iqbal 框架）|

## 八、常見用法情境

- **reviewer 查授權合規**：看 §五的引用說明表，逐一對照 `*_REFERENCE.md`。
- **顧問查方法論依據**：八階段方法論的依據見 `@AI-MD-PUBIC.pdf` 與 `Metholodgy.png`。
- **要再散布/商用本方法論**：先讀 §六署名要求與根目錄 `NOTICE`。
- **要評估新的第三方素材**：依 §四引用原則 —— 先確認有授權、再獨立改寫、再建 `*_REFERENCE.md`。
