# 視覺素材規格 / Visual Assets Specification

> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

本檔提供 3 個對外視覺素材的 ASCII / Markdown 規格與設計師 brief，可交付 designer 製作高解析版本（SVG / PNG / 印刷檔）。

This file provides ASCII/Markdown specs and designer briefs for 3 external visual assets — ready to hand to a designer for high-res production (SVG / PNG / print).

---

## Asset 1：三段式服務流程 / Three-Step Service Flow

### ASCII 規格

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ 1. 診斷       │ ──▶ │ 2. 建置       │ ──▶ │ 3. 交付       │
│   Diagnose   │     │   Build      │     │   Deliver    │
├──────────────┤     ├──────────────┤     ├──────────────┤
│ 10/25/50 題   │     │ L1-L5 課程   │     │ 八階段報告    │
│ 公司屬性問卷  │     │ 課中產出資產 │     │ 30/60/90     │
│ → L1-L5 分數 │     │ Prompt/Skill │     │   Roadmap    │
│              │     │ Workflow/    │     │ ROI + 治理    │
│              │     │ Agent/Team   │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
   2-4 週                 4-8 週              2-4 週
   2-4 weeks             4-8 weeks           2-4 weeks
```

### 三種版型備選 / Three Layout Alternatives

1. **線性 Linear** — 由左到右，箭頭強調流動 (上面 ASCII)
2. **圓形 Circular** — 三段繞圓，強調可重複迭代 (適合 Repeat Customer)
3. **金字塔 Pyramid** — 診斷在底、建置在中、交付在頂，強調逐層收斂

### 設計師 Brief

- **尺寸** / Size: 1920×1080 (PNG) + SVG vector
- **配色** / Palette:
  - 診斷：靛藍 #1B3A6B
  - 建置：青綠 #2D8B7C
  - 交付：金 #D4A017
- **字體** / Typography: 思源黑體 Bold (中) / Inter Bold (EN)；標題 32pt、內文 16pt
- **Icon**：階段 1 用放大鏡 / 階段 2 用齒輪 / 階段 3 用獎盃
- **動畫版** (Optional): MP4 30 sec, 三段依序亮起

---

## Asset 2：L1-L5 成熟度地圖 / L1-L5 Maturity Map

### ASCII 規格 (垂直金字塔版)

```
                  ╔════════════════════════════════╗
                  ║   L5  Agentic Team AI           ║
                  ║   Tool: ClawTeam                ║
                  ║   多個專業 Agent 協作            ║
                  ╚════════════════════════════════╝
                              ▲
                  ┌────────────────────────┐
                  │ L4  Auto Agentic AI    │
                  │ Tool: Hermes Agent     │
                  │ Wiki+Skill+Workflow+   │
                  │ Gate = 可驗證 Agent     │
                  └────────────────────────┘
                              ▲
              ┌─────────────────────────────────┐
              │ L3  Workflow AI                  │
              │ Tool: n8n                       │
              │ Skill + 企業系統 = Workflow      │
              └─────────────────────────────────┘
                              ▲
          ┌──────────────────────────────────────────┐
          │ L2  Skill AI                              │
          │ Tool: Antigravity / Claude Code / Codex   │
          │ 個人經驗 → 可複用 Skill                    │
          └──────────────────────────────────────────┘
                              ▲
      ┌────────────────────────────────────────────────────┐
      │ L1  Chat AI                                         │
      │ Tool: OpenWebUI                                     │
      │ 企業全員安全使用 AI                                  │
      └────────────────────────────────────────────────────┘
```

### 卡片內容（每層 / per level）

| 欄位 / Field | 內容 |
| --- | --- |
| Level | L1 / L2 / L3 / L4 / L5 |
| Name | Chat / Skill / Workflow / Auto Agentic / Agentic Team AI |
| Tool | OpenWebUI / Antigravity / n8n / Hermes / ClawTeam |
| Capability | 一句話定位 |
| Output | 上一層交付給下一層的產出 |
| Who Uses It | 全員 / 核心使用者 / 流程設計者 / IT+AI Champion / 管理層 |

### 三種版型備選 / Three Layout Alternatives

1. **垂直金字塔 Vertical Pyramid** — 上面 ASCII，強調由下而上堆疊
2. **水平層 Horizontal Layers** — 從左到右五個區塊，每層彩條
3. **放射 Radial** — 中心為核心方法論，五層由內而外放射

### 設計師 Brief

- **尺寸**: 1920×1200 + 印刷 A3
- **配色梯度**: L1 淺藍 → L5 深金，每層漸深
- **箭頭文字** (between layers): 寫每層的「產出 = 下一層輸入」
  - L1 → L2: 高頻 Prompt + 情境
  - L2 → L3: Skill Library
  - L3 → L4: Workflow + Sub-workflow
  - L4 → L5: 受控 Agent + Wiki
- **Footer**: 「Each layer's output is the next layer's input.」
- **可附互動 HTML**: hover 顯示完整課程連結

---

## Asset 3：可驗證交付物視覺 / Verifiable Deliverables Visual

### ASCII 規格

```
┌─ Diagnose (診斷) ─────────────────────────────────┐
│ ✓ AI 成熟度問卷 & 評分結果                          │
│ ✓ 公司屬性 & 部署模式調查                          │
│ ✓ As-Is Process Map & Systems Inventory          │
│ ─── [Gate 1 ✓] ────────────────────────────       │
└──────────────────────────────────────────────────┘

┌─ Build (建置) ────────────────────────────────────┐
│ ✓ L1 OpenWebUI 帳號 / 群組 / 權限表                │
│ ✓ Prompt Library + 個人聊天區啟用記錄              │
│ ✓ L2 Skill Library (3-5 Skills) + Antigravity     │
│ ✓ L3 n8n Workflow PoC (3 workflows)              │
│ ✓ Sub-workflow Library + Data Tables Schema       │
│ ✓ GitHub Backup SOP + L4 Workflow Contract        │
│ ✓ L4 Hermes Agent + Wiki + Gate 4A-4E             │
│ ✓ L5 ClawTeam Agent Team Role Cards               │
│ ─── [Gate 2 / 3 / 4 / 5 ✓] ────────────────       │
└──────────────────────────────────────────────────┘

┌─ Deliver (交付) ──────────────────────────────────┐
│ ✓ 八階段顧問診斷報告                                │
│ ✓ 30/60/90 天 Roadmap                            │
│ ✓ ROI 追蹤矩陣 + 治理建議                          │
│ ✓ Stage Gate 驗收紀錄                              │
│ ✓ SOW 後續導入建議                                  │
└──────────────────────────────────────────────────┘
```

### 設計師 Brief

- **尺寸**: 1920×1200 + 印刷 A4 直
- **配色**: 三段不同色塊 (Diagnose 藍 / Build 綠 / Deliver 金)
- **每項前綴 ✓**: 綠色勾勾 icon (Lucide CheckCircle)
- **Gate 標記**: 章節之間放圓形 "Stage Gate" 印章圖示
- **可選互動版**: 點擊每項展開實際範例檔案 (連到 GitHub)

---

## 整體製作備註 / Overall Production Notes

- **檔案命名**：`tigerai-visual-{asset}-{version}.{ext}`
- **版本控管**：所有 Adobe Illustrator / Figma 源檔上傳到 `assets/source/`
- **版權聲明**：每張視覺底部加 "© 2026 Tiger AI · Apache 2.0 · attribution required"
- **多語版本**：每張視覺出中文版 + 英文版 + 中英雙語版 三套
- **無障礙**：對比度 ≥ AA；提供 SVG alt text；顏色不單獨承載資訊（同時用形狀區分）
