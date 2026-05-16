# 03 Consulting Report — コンサル診断 & レポート（コンサルクローズドループ）

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 本ディレクトリの位置づけ

本ディレクトリは 3 段階サービスフローの**第 3 段階：Deliver**、そして方法論全体の**コンサル実践のコア**です。

診断 (`01`) は客観的スコア提供、Build (`02`) は顧客能力育成 — しかしコンサル案件が最終的に顧客に手渡すのは、**構造化され、エビデンスベース、Roadmap 付き、意思決定層に採用可能な診断レポート**。本ディレクトリはそのレポート作成に必要なすべてを提供：**8 段階コンサル構造のツール表、古典コンサルフレームワーク庫、レポート生産ワークフロー、レポートテンプレート**。

> 🔁 **本ディレクトリは「6 週マラソン線形プロセス」ではなく、「コンサルクローズドループ」**。完全クローズドループ設計は [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) 参照：
> **3 段階契約**（Phase A 診断 2W + Phase B 戦略 4W + Phase C 導入 24M）+ **中間評価レポート** + **四半期レーダー回顧**（科学管理の反証メカニズム）。
> ループの要点は「完了したら終わり」ではなく、「**構造は実際に丸くなったか？**」 — Stage 2 Reference Model レーダーに対する継続的自己反証。

解決する課題：**方法論なしでは、コンサル診断は経験ベースの個人手芸 — スケール不可、新人コンサル再現不可、品質不安定。** 本ディレクトリは「コンサルがどう診断するか」を、教えられる・再現可能・検収可能な標準クローズドループに変換。

本ディレクトリを使う人：コンサル、シニアコンサル、新人コンサル（オンボーディング）、PM。

## 2. 方法論における位置

| 軸 | 対応 |
| --- | --- |
| 3 段階サービスフロー | **Deliver** — 第 3 段階 |
| 8 段階コンサル構造 | **本ディレクトリは 8 段階（Stage 1-8）のツールとレポート本体そのもの** |
| **3 段階契約モデル** | **Phase A 診断 2W → Phase B 戦略 4W → Phase C 導入 24M + 四半期レーダー回顧**（コンサルクローズドループ） |
| L1-L5 成熟度 | レポートで顧客の L レベルと講座観察を引用 |
| Engagement Lifecycle | **Delivery — Handover**（レポートは Phase B のコア納品；Phase C で四半期レーダー回顧記録を継続産出） |

> 2 つの直交軸：**L1-L5 は「能力縦軸」（`02` 担当）；8 段階は「診断横軸」（本ディレクトリ担当）。** 2 軸が交差して検証可能な納品物。
>
> **L1-L5 自体が 2 軸**（スケール軸 L1-L3 + AI 自律軸 L4-L5）；[`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 参照。

## 3. 目標 & 効果

| 目標 | 効果 |
| --- | --- |
| 8 段階各ステップに直接使えるツール表 | コンサルがツール設計やり直し不要；新人コンサル即戦力 |
| 古典フレームワーク庫が 8 段階にマッピング | 各ステップで「どの分析フレームワーク使うか」分かる |
| レポート生産ワークフロー | 「課題 → 納品レポート/プレゼン」に SOP、手芸ではない |
| レポート構造固定 | 納品品質安定；意思決定層が理解できる |
| コンサル方法論が教育・再現可能 | コンサルチームスケール可能 |

**本ディレクトリ飛ばすと**：各コンサルが独自方法、レポート品質不揃い、新人再現不可、診断が「シニアの個人手芸」に堕落。

## 4. ワークフロー & ロジック（3 段階契約 + 四半期クローズドループ）

```text
01 診断結果 + 02 講座観察
   ↓
┌─ Phase A 診断（2 週間）─────────────────────────────────┐
│  Stage 1-4 8 段階前半：Awareness / Reference Model /   │
│  Discovery / Gap Analysis                              │
│  → CONSULTING_TOOLKIT_TEMPLATES.md ツール使用          │
│  → 中間評価レポート → 顧客署名                          │
└────────────────────────────────────────────────────────┘
   ↓ Gate A 顧客が Phase B 継続判断
┌─ Phase B 戦略（4 週間）─────────────────────────────────┐
│  Stage 5-8 8 段階後半：Stakeholder / Diagnosis /       │
│  To-Be Design / Acceptance Test                        │
│  → REPORT_PRODUCTION_WORKFLOW.md 8 ステップ生産        │
│  → 完全 14 章診断レポート + 24M Roadmap + ROI +        │
│     ガバナンス提言                                      │
│  → CONSULTING_REPORT_TEMPLATE.md 固定構造に記入        │
└────────────────────────────────────────────────────────┘
   ↓ Gate B 顧客が Phase C SOW 署名
┌─ Phase C 導入（24 ヶ月）─ クローズドループ反饋段 ──────┐
│  段階実装 + **四半期 Gate C：Stage 2 レーダー再点検**  │
│  → 構造は実際に丸くなったか？丸くなっていない →        │
│     対応 Stage に戻って Roadmap 修正                   │
│  → 四半期産出：レーダー回顧記録 + Roadmap 校正記録     │
└────────────────────────────────────────────────────────┘
```

| Phase | 期間 | 対応 8 段階 | 主要ツール | 主納品 |
| --- | --- | --- | --- | --- |
| **Phase A 診断** | 2 週間 | Stage 1-4 | TOOLKIT 前半 + FRAMEWORKS セレクター | **中間評価レポート** + Reference Model レーダー署名 |
| **Phase B 戦略** | 4 週間 | Stage 5-8 | TOOLKIT 後半 + REPORT_PRODUCTION_WORKFLOW + REPORT_TEMPLATE | **完全 14 章診断レポート** + Roadmap + ROI + ガバナンス |
| **Phase C 導入** | 24 ヶ月 | Stage 2 四半期レビュー | TOOLKIT 四半期レーダー回顧ツール + Risk Register | **四半期レーダー回顧記録** + Roadmap 校正 |

> ロジック：`CONSULTING_TOOLKIT_TEMPLATES` は「診断のツール + 四半期回顧ツール」；`CONSULTING_FRAMEWORKS_LIBRARY` は「各ステップでどの分析フレームワーク」；`REPORT_PRODUCTION_WORKFLOW` は「診断を効率的に納品物へ変換」；`CONSULTING_REPORT_TEMPLATE` は「最終レポートはどんな形」。4 つ合わせて = **完全なコンサルクローズドループ方法論**（線形マラソンではない）。

> 📖 完全 8 段階対話脚本 + クローズドループストーリー：[`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md)（「なぜクローズドループは科学か」結語含む）。

## 5. ファイル説明

### `CONSULTING_REPORT_TEMPLATE.md`

AI トランスフォーメーション診断レポートの Markdown テンプレート（v2.0 8 段階整合版）。14 章固定構造：カバー、Executive Summary（標準ギャップ概要含む）、診断手法、As-Is Snapshot、Reference Model Alignment（APQC + Tiger AI 双座標）、Best Practice Integration（卓越能力プロファイル）、Gap Analysis、Executive Problem Statement、Phased Goals、To-Be Design、Implementation Roadmap、Change Management Plan、Governance Design、Value Tracking & Risk Register、SOW 提言。

### `CONSULTING_TOOLKIT_TEMPLATES.md`

8 段階コンサル診断の**直接使用可能ツール表**（v2.0 イメージアライン版）。各段階に 1-5 ツール対応：40 問インタビューバンク、AI/システム棚卸し、As-Is スイムレーン、**Reference Model 選定（APQC/SCOR/eTOM/ITIL/CMMI）+ Mapping Worksheet + 標準ギャップチェック + 双レーダー**、Best-Practice Profile + 卓越能力プロファイル、Missing/Broken/Redundant（**リスク評価ではない**）、Impact×Effort、**80/20 収束 + 5 Whys**、Problem Statement、**究極ベンチマーク → Phased Goals + 組織吸収力評価**、**段階別 To-Be Operating Model + Human-AI Collaboration (HITL)**、Skill/Workflow/Agent Map、Transformation Roadmap、**Change Management Playbook（抵抗対処含む）**、RACI、権限、**Value Tracking Matrix（時間/品質/規模/リスク/資産 5 次元）**、Risk Register、Audit、Ethics、**Phase A 2W + Phase B 4W 標準スケジュール + Phase C 四半期レーダー回顧ツール**（コンサルクローズドループ）。コピペで使用可能。

### `CONSULTING_FRAMEWORKS_LIBRARY.md`

古典コンサルフレームワーク庫。50+ 業界フレームワーク（MECE、Pyramid Principle、Issue Tree、Porter's 5 Forces、SWOT、BCG Matrix、5 Whys、Fishbone、Business Model Canvas、WBS/RACI、NPV/IRR、Lean/Six Sigma 等）7 カテゴリ。「フレームワークセレクター」（自然言語 → フレームワーク組合せ）、「フレームワーク組合せチェーン」、各フレームワークの 8 段階マッピング、§4.8 MECE / Issue Tree / 仮説形成深堀り含む。yoichiojima-2/consultant（MIT）から adapt。

### `REPORT_PRODUCTION_WORKFLOW.md`

「課題 → 納品レポート/プレゼン」の 8 ステップ生産ワークフロー。Dummy Page（先に骨格、後で記入）、依存管理、7 種ページレイアウト、Excel エビデンストレース、progressive disclosure、§9 troubleshooting playbook（7 つの一般的問題 + 修正法）含む。Kafurtan/mckinsey-consultant-skills（MIT）から adapt。

### `*_EN.md`

上記ファイルの英語版 sibling。

## 6. 他ディレクトリへの対応

| ディレクトリ | 本ディレクトリとの関係 | データフロー |
| --- | --- | --- |
| `01_Assessment` | 診断スコアとレーダーは 8 段階 Stage 1 のコア入力 | `01` スコア → `03` レポート |
| `02_Course_Design` | クラス内産出と観察は「講座観察」章の素材 | `02` 講座観察 → `03` レポート |
| `00_Overview` | レポートはストーリーの「Deliver」段階 | `00` ストーリー → `03` 実現 |
| `04_Scenarios` | 8 段階 Stage 3 業界 Best Practice ベンチマーキングでケース引用 | `04` ケース → `03` Stage 3 |
| `06_Delivery` | レポートは納品パッケージのコア納品；Handover に対応 | `03` レポート → `06` 納品検収 |
| `90_References` | フレームワーク庫とレポートワークフローの第三者引用（consultant / mckinsey-skills） | `90` 引用 → `03` |

## 7. 共通使用シナリオ（クローズドループフェーズ別）

- **新コンサルオンボーディング**：まず `CONSULTING_TOOLKIT_TEMPLATES.md` で全 sample 通し、次に [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) 対話脚本を読む、最後に実インタビューを shadow。
- **Phase A 診断（2 週間）**：TOOLKIT の Stage 1-4 ツール（40 問インタビュー、AI/システム棚卸し、Reference Model レーダー）使用、週末に**中間評価レポート**を Sponsor 署名のため産出。
- **Phase B 戦略（4 週間）**：TOOLKIT の Stage 5-8 ツール + `REPORT_PRODUCTION_WORKFLOW.md` 8 ステップ生産で診断をデックに変換、`CONSULTING_REPORT_TEMPLATE.md` に記入、**完全 14 章レポート + 24M Roadmap + ROI** 産出。
- **Phase C 導入（24 ヶ月、ループフィードバック段）**：四半期ごとに TOOLKIT のレーダー回顧ツールで、**Stage 2 Reference Model レーダー再実行** — Phase A 署名版と比較、「構造は実際に丸くなったか」を確認；丸くなっていない → 対応 Stage に戻って Roadmap 修正。
- **顧客が「なぜこのフレームワーク？」と質問**：`CONSULTING_FRAMEWORKS_LIBRARY.md` のフレームワークセレクターで説明。
- **顧客が「6 週間後はどうなる？」と質問**：[`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 完全クローズドループ図を見せる — ポイントは 6 週間ではなく、Phase C 24 ヶ月 + 四半期レーダー回顧の反証メカニズム。
