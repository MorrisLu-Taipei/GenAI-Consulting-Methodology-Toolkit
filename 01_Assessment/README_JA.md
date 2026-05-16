# 01 Assessment — AI 成熟度診断

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 本ディレクトリの位置づけ

本ディレクトリは 3 段階サービスフローの**第 1 段階：診断 (Diagnose)** です。コンサル業務の最も根本的な問題を解決します：**「企業は『AI を使っている』と言うが、実際どのレベル？何が足りない？どこから補うべき？」**

客観的な診断がなければ、コンサルは顧客の主観的記述だけで講座を組み立てるしかない — 結果はしばしばレベル飛び越し（L1 全員利用すらないのに L4 Agent をやりたがる）や、優先度の誤り（ガバナンスが欠けているのにツールを足し続ける）。本ディレクトリは 3 種類の長さの問卷 + スコアリングモデル + 企業属性調査で「曖昧な感覚」を **客観的・定量的・比較可能な L1-L5 スコアと 6 次元ギャップレーダー** に変換します。

本ディレクトリを使う人：Sales（10 問版でリード開発期スクリーニング）、コンサル（25/50 問版で講前・面談前棚卸し）、IT/AI Champion（企業属性問卷）。

## 2. 方法論における位置

| 軸 | 対応 |
| --- | --- |
| 3 段階サービスフロー | **診断 (Diagnose)** — 第 1 段階 |
| 8 段階コンサル構造 | **Stage 1 現状把握**（診断結果は Stage 1 の核心入力） |
| L1-L5 成熟度 | 本ディレクトリは「**顧客がどのレベルか判定**」するツール |
| Engagement Lifecycle | **Sales — Lead Qualification (10 問) / Discovery (25/50 問)** |

## 3. 目標 & 効果

| 目標 | 効果 |
| --- | --- |
| 主観的推測を客観的スコアで置換 | コンサルが講座構成に根拠を持つ、感覚ではない |
| 6 次元のギャップ発見（ツール/ナレッジ/プロセス/統合/Agent/ガバナンス-ROI） | 顧客がどこで強い・弱いか把握 |
| 直接 3 つの推奨を導出 | 講座比率 + デプロイ方式 + PoC シナリオ、一度に完成 |
| 3 種類の問卷長さで 3 つの営業段階対応 | リード開発、講前、面談前 — それぞれ適切なツール |
| 自動化可能 | 問卷→スコアリング→レポート全自動、コンサルは解釈のみ |

**本ディレクトリを飛ばすと**：講座比率は当てずっぽう、顧客期待値管理不能（L5 ケースを指して「これが欲しい」と言うが自分が L2 と知らない）、コンサルレポートに客観的起点なし。

## 4. ワークフロー & ロジック

```text
10 問クイック問卷（リード開発期、3 分）
   → リード適格判定 + 初期 L レベル位置
25 問問卷（講前、8 分、顧客マネージャー記入）
   → 6 次元スコア + レーダー図
50 問問卷（コンサル面談前、20 分、IT/AI Champion）
   → 完全棚卸し + オープン質問
企業属性問卷（35 問）
   → JSON Profile Bundle（システム / リスク / デプロイ嗜好 / 予算）
        ↓ Merge
   自動スコアリング → L1-L5 レベル + 6 次元レーダー
        ↓ 導出
   ① 推奨講座比率  ② 推奨デプロイ方式  ③ 推奨 PoC シナリオ
```

| ステップ | 誰 | いつ | 入力 | 出力 |
| --- | --- | --- | --- | --- |
| 10 問クイックスクリーン | Sales | リード開発期 | 潜在顧客 | 適格判定 + 初期 L レベル |
| 25 問講前診断 | 顧客マネージャー群 | L1 開講 1 週前 | 25 問問卷 | 6 次元スコア |
| 50 問完全棚卸し | 顧客 IT / AI Champion | コンサル面談前 | 50 問 + 企業属性問卷 | 完全 Profile Bundle |
| 自動スコアリング | システム (Sheets/Notion/n8n) | 問卷提出後 | 問卷回答 | L レベル + レーダー + 3 推奨 |
| 解釈 | コンサル | 自動レポート受領後 | 自動レポート | カスタマイズ提案方向 |

> ロジック：問卷は単なる**入力**；本当の出力は「**L レベル + 6 次元ギャップ + 3 推奨**」。この 3 つはそれぞれ — 講座比率 → `02_Course_Design`；デプロイ方式 → `03` の To-Be Design；PoC シナリオ → `04_Scenarios` のケースインデックス、に流れる。診断は終点ではなく、後続 3 ディレクトリを「点灯」するスイッチ。

## 5. ファイル説明

### `AI_MATURITY_QUESTIONNAIRE.md`

10 / 25 / 50 問 3 種類の AI 成熟度問卷本体。10 問版は Sales クイック判定用；25 問版は各次元 4-5 問、講前用；50 問版にデプロイ方式とシステム棚卸し追加、コンサル面談前用。3 版共通：0-4 点尺度と 6 次元アーキテクチャ。

### `AI_MATURITY_SCORING_MODEL.md`

スコアリングロジックと判定ルール。含む：6 次元（ツール使用、ナレッジ沈殿、プロセス標準化、システム統合、Agent 応用、ガバナンス-ROI）のスコア計算、総合点が L1-L5 に対応する閾値、**主成熟度 vs 局所成熟度**の判断（なぜある部門が局所 L4 で全体 L2 か）、デプロイ方式と講座比率の推奨ルール。

### `AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`

L1-L5 各段階の Definition of Done、Deliverables、Evidence、Owner、Stage Gate、Fail Condition、Next Level Entry Criteria。「各レベル『完了』はどう見えるか、何を evidence として証明するか」を定義 — Stage Gate 検収の根拠。

### `FILLABLE_QUESTIONNAIRE.md`

10/25/50 問を記入可能フォームに変換するレンダー仕様 — 設問タイプ（radio / 0-4 scale / マルチセレクト / 短答）、ページセグメンテーション、skip logic、提出ページと「次に何が起きるか」ページ、Google Form / Tally / Notion Form 3 プラットフォームのレンダーヒント付き。

### `COMPANY_PROFILE_QUESTIONNAIRE.md`

35 問の企業属性問卷、6 セクション（Profile / Systems / Risk / Deployment / Course / Budget）。出力：JSON Profile Bundle、**導出ルール**含む：Bundle から自動でデプロイ方式推奨、講座比率微調整、PoC シナリオ推奨を導出。成熟度問卷と `submission_id` で連結。

### `AI_DIAGNOSIS_SHEETS_SCHEMA.md`

診断全体を自動化する実装スキーマ。3 プラットフォーム：Google Sheets（スコアリング数式、条件付き書式、Apps Script）、Notion（4 つの database 構造と formula）、n8n（13 ノード自動診断フロー、idempotency 含む）。問卷→スコアリング→レポート生成→コンサル通知、全自動。

### `*_EN.md`

上記ファイルの英語版 sibling。

## 6. 他ディレクトリへの対応

| ディレクトリ | 本ディレクトリとの関係 | データフロー |
| --- | --- | --- |
| `00_Overview` | 診断はストーリーの第 1 段階 | `00` ストーリー → `01` 実現 |
| `02_Course_Design` | 診断の「L レベル + 講座比率」が講座配置を直接決定 | `01` 比率 → `02` 配置 |
| `03_Consulting_Report` | 診断結果は 8 段階 Stage 1 の入力；レポートが診断スコアとレーダーを引用 | `01` スコア → `03` レポート |
| `04_Scenarios` | 診断後 L レベルに応じて `LLM_APPS_CASE_INDEX.md` で PoC 候補選定 | `01` L レベル → `04` ケース選定 |
| `06_Delivery` | 診断は engagement lifecycle の Sales 段階に対応 | `01` ↔ `06` Sales 段階 |
| `90_References` | スコアリングモデルの方法論根拠 | `90` 根拠 → `01` |

## 7. 共通使用シナリオ

- **営業開発**：潜在顧客が 10 問版記入 → 24 時間以内に自動レポート → Sales が L レベル位置を持って商談へ。
- **講前準備**：開講 1 週前に 25 問版を顧客マネージャー群へ → コンサルが 6 次元レーダーを得て講座比率調整。
- **コンサル面談前**：IT/AI Champion が 50 問 + 企業属性問卷記入 → コンサルが面談 1 時間前に完全 Profile Bundle をブリーフとして受領。
- **スケール化したい**：`AI_DIAGNOSIS_SHEETS_SCHEMA.md` で顧客 n8n に自動診断フロー deploy、コンサルは最終解釈のみ。

---

## ⭐ Cross-Topic Quick References：5 つの核心テーマ、どこで見つけるか

方法論全体には全ディレクトリを貫く 5 つの主動脈があります。本ディレクトリがそれぞれにどう接続するか：

| Cross-Topic | 主要位置 | 本ディレクトリがどう接続するか |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 3 エンジン共読** | Root [`README_JA.md`](../README_JA.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | 問卷は Antigravity `/diagnose` でインタラクティブに記入可能；AI_DIAGNOSIS_SHEETS_SCHEMA で問卷自動化（n8n + Google Sheets + Notion）；診断結果は Codex `/consistency-review` でクロスファイル整合へ流せる |
| 🎓 **学術基盤（7 大支柱）** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **本ディレクトリの [`BARS_RUBRICS.md`](BARS_RUBRICS.md) が inter-rater reliability に対応**（Smith & Kendall 1963）；6 次元診断は Capability Maturity（Rosemann/CMMI）+ Absorptive Capacity（Cohen & Levinthal 1990）+ Sociotechnical Trust に対応 |
| 📚 **L1-L5 講座教育** | [`../02_Course_Design/`](../02_Course_Design/) | **診断の L レベル判定 + 6 次元レーダー + 講座比率推奨**が `02` の講座配置を直接決定 — `02` の「講前必須」 |
| 🔁 **コンサル方案 / 8 段階 + Phase A→B→C クローズドループ** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **診断 = Phase A の核心入力**（Stage 1 現状把握 + Stage 2 Reference Model レーダー署名）；Phase C 四半期レーダー回顧は「**診断を再実行**」 — 構造は実際に丸くなったか？診断は入口でありクローズドループの反証メカニズムでもある |
| 📖 **参考資料 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | スコアリングモデルは BARS（Smith & Kendall 1963）+ 7 大理論支柱を参照；Pilot Study 18-24 ヶ月実証計画は [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) 参照（問卷の Cohen's κ ≥ 0.60 目標検証） |
