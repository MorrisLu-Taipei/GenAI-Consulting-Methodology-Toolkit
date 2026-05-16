# 00 Overview — プログラム概要 & エントリーポイント

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 本ディレクトリの位置づけ

本ディレクトリは **AI Consulting Methodology Toolkit** 全体の**唯一のエントリーポイント**です。「ツール」や「成果物」は置かず、2 つだけを置きます：**方法論のストーリー** と **方法論のステータス**。

本リポジトリに初めて触れる人 — コンサルタントが方法論を学ぶ、顧客が購入評価する、新人がオンボーディングする、レビュアーが監査する — 誰もがここから始めるべきです。まずここで「方法論とは何か、なぜこう設計されているか、現在どこまで進んでいるか」の全体像を構築し、それから機能ディレクトリ `01`-`06` へ進む。木を見て森を見ずにならないように。

本ディレクトリが解決する問題：**明確なエントリーとステータスがなければ、ユーザーは迷い、誤用し、何が完了で何が進行中か分からなくなる。**

## 2. 方法論における位置

| 軸 | 対応 |
| --- | --- |
| 3 段階サービスフロー | 単一段階に対応せず；「Diagnose → Build → Deliver」3 段階の**俯瞰地図** |
| 8 段階コンサル構造 | 単一段階に対応せず；8 段階の**全体像** |
| L1-L5 成熟度 | 単一レベルに対応せず；L1-L5 の**全体像** |
| Engagement Lifecycle | 単一フェーズに対応せず；全ライフサイクルの**起点説明** |

> 論理的位置づけ：`00_Overview` は「**何・なぜ**」に答える；`01`-`06` は「**どう**」に答える；`90_References` は「**根拠と引用**」に答える。

## 3. 目標 & 効果

| 目標 | 効果 |
| --- | --- |
| 新規読者に 5-10 分で方法論の骨格を理解させる | オンボーディング短縮；誤用減少 |
| 価値訴求を顧客の言葉で語る | Sales がストーリーを直接 30 分の顧客ブリーフィングに使用可能 |
| 権威ある専案ステータスファイルを維持 | 誰でも「現在の進捗、次のステップ」を確認可能 — 口頭引継ぎ不要 |
| `01`-`06` と `90` の関係を繋ぐ | ユーザーが各ディレクトリの役割と順序を把握 |

**本ディレクトリを飛ばすと**：ユーザーは機能ディレクトリに直接飛び込み、「なぜこのディレクトリが存在するか、他とどう繋がるか」を理解しない — 結果：ツールが孤立利用され、方法論が散らばったファイルの山になる。

## 4. ワークフロー & ロジック

```text
新規読者 / 顧客
   → AI_TRANSFORMATION_STORY_AND_STRUCTURE.md を読む（なぜ + どう動く + 何を生む）
   → 「L1-L5 + 8 段階 + 3 段階フロー」の全体メンタルモデル構築
   → 01_Assessment へ進み実際の診断開始

コンサル / 同僚 / レビュアー
   → TODO_WBS.md を読む（プロジェクト状況、変更履歴、次のラウンド候補、作業ログ）
   → 状況把握してから動く
```

| ステップ | 誰 | いつ | 入力 | 出力 |
| --- | --- | --- | --- | --- |
| ストーリーを読む | コンサル / 顧客 / 新人 | リポ初接触時 | なし | 方法論の全体理解 |
| 顧客にブリーフィング | Sales / コンサル | プリエンゲージメント初会議 | ストーリー | 顧客が診断に進む準備完了 |
| プロジェクト状況確認 | コンサル / 同僚 / レビュアー | 引継 / レビュー前 | なし | 現状 + 次のステップ |
| ステータス更新 | 担当コンサル / AI | 各バッチ完了後 | 完了作業 | 更新済 `TODO_WBS.md` |

> ロジック：ストーリーは「外向け」（顧客 + 新人向け）；`TODO_WBS.md` は「内向け」（実行者向け）。外 + 内で完全なエントリーを構成。

## 5. ファイル説明

### `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`

顧客指向のストーリーと章構造。技術文書ではなく**ナラティブ** — 「企業がなぜ AI トランスフォーメーションを必要とするか、方法論がどう段階的に動くか、各段階が何を検収可能に生成するか」を顧客が分かる一貫したストーリーとして語る。含む：ソリューション位置づけ、3 段階パス、L1-L5 ↔ ツール対応、未来想像、役割別価値訴求（CEO/COO/CIO/IT/HR/部門長）、§6 完全 8 段階定義 + 6 週シナリオ。初回顧客会議で直接使用可能。

### `EXECUTIVE_SUMMARY.md`

方法論全体を 5 分で 1 ページに圧縮。詳細を見る時間のない経営陣向け。

### `CLIENT_JOURNEY_STORY.md` 🆕

**Ming の物語** — CEO / 取締役 / 家族が 20 分で方法論を理解するシナリオストーリー。半導体パッケージング 700 人企業の 24 ヶ月トランスフォーメーション — ツール表ゼロ、専門用語ゼロ。対外コミュニケーション、初回顧客接触、新人面接で使用可能。

### `EIGHT_STAGE_FLOW_STORY.md` 🆕

**権威ある 8 段階フロー物語**：3 段階契約モデル（Phase A 診断 2W + Phase B 戦略 4W + Phase C 導入 24M）+ 中間評価レポート + 四半期レーダー回顧の完全なクローズドループ。コンサル内部研修の必読書。

### `METHODOLOGY_SCIENTIFIC_LOGIC.md` 🆕

**方法論の科学的議論耐性**：科学的方法の 5 条件（観察可能、定量化可能、再現可能、反証可能、監査可能）で 8 段階がなぜ顧客 / 取締役会 / 規制当局の質問に耐えるかを検証。学術投稿、政策ロビー活動、取締役会レビューに必須。

### `INDUSTRY_FRAMEWORK_ALIGNMENT.md` 🆕

**業界フレームワークとの整合地図**：8 段階 vs McKinsey / BCG / Bain / Deloitte / Accenture / PwC；4 層アーキテクチャ vs TOGAF / Zachman / Dragon1；L1-L5 vs Gartner / MIT / Forrester AI Maturity。「うちの既存方法論と競合する？」という顧客質問への回答。

### `AI_NATIVE_LIVING_BOOK.md` 🆕

**方法論の運搬媒体に関する革新論述**：本方法論を **AI-native living book**（AI IDE で直接実行可能な知識システム）として位置づけ、単なる PDF / PPT ではない。含む：学術分類（executable knowledge artifact、AI-mediated methodology、interactive consulting playbook）、3 層設計（Repo as Book / Agent as Tutor / Methodology as Executable Artifact）、4 大リスク管理原則（AI ≠ コンサル、evidence 必要、AGENTS.md バージョン管理、AI 出力明示）。学術投稿 / 方法論差別化に必須。

### `ACADEMIC_THEORETICAL_FOUNDATIONS.md` 🆕

**7 大理論支柱の統一論述**：Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Task-Technology Fit (Goodhue & Thompson 1995) + Dynamic Capabilities (Teece 1997/2007) + Sociotechnical Systems & Trust in AI (Bostrom 1977/Dietvorst 2015/Glikson 2020) + Real Options (Dixit & Pindyck 1994/McGrath 1997) + Executable Knowledge Artifact (Knuth 1984)。各理論：要約 + 創立者 + Tiger AI への貢献 + 対応位置 + 引用。学術 / 規制 / 取締役会が「理論的根拠は？」と問うときの唯一の答え。

### `../01_Assessment/BARS_RUBRICS.md` 🆕（学術硬化）

**Behaviorally Anchored Rating Scales**：6 次元 × 0-4 点の**行動アンカー表**（Smith & Kendall 1963 に基づく）。各スコアに具体的な観察可能行動があり、**コンサルの主観評価を回避**、inter-rater reliability を向上。Pilot Study Cohen's κ ≥ 0.60 目標に対応。2 人のコンサルが同じ企業に近いスコアを付けられる中核メカニズム。

### `TODO_WBS.md`

本リポの**権威あるステータスファイル**、「現在どこまで進んでいるか」の唯一の信頼できる情報源。含む：WBS 全体像（項目 × 優先度 × 状態）、完了ファイルリスト、完了項目詳細、未完了 TODO、次回ラウンド推奨、**変更履歴（バッチ毎 + commit hash）**、現在のステータス全体像、**日次作業ログ**。コンサル引継、レビュアー監査、AI 継続作業前に必ず読む。各バッチ完了後に更新。

### `*_EN.md`

上記ファイルの英語版 sibling、中国語版と内容対応。

## 6. 他ディレクトリへの対応

| ディレクトリ | 本ディレクトリとの関係 | データフロー |
| --- | --- | --- |
| `01_Assessment` | ストーリーの「診断」段階がここで実現 | `00` ストーリー → `01` 診断ツール |
| `02_Course_Design` | ストーリーの「Build」段階がここで実現 | `00` ストーリー → `02` 講座 |
| `03_Consulting_Report` | ストーリーの「Deliver」段階がここで実現 | `00` ストーリー → `03` コンサルレポート |
| `04_Scenarios` | ストーリーの顧客シナリオ・ケース素材を提供 | `04` ケース ↔ `00` ストーリー |
| `05_Sales` | ストーリーを販売可能素材へ変換 | `00` ストーリー → `05` 販売素材 |
| `06_Delivery` | 方法論を納品・運営可能なビジネスへ変換 | `00` ストーリー → `06` 納品 & 運営 |
| `90_References` | 方法論の原典 + 第三者引用ライセンス | `90` 根拠 → `00`-`06` 支援 |

## 7. 共通使用シナリオ

- **Sales が顧客招待**：`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md` の 3 段階パスと価値訴求で 30 分方法論ブリーフィング。
- **新コンサルのオンボーディング**：まずストーリー読了で認識構築 → `TODO_WBS.md` で現状把握 → §6 データフロー順に各ディレクトリ学習。
- **レビュアー監査**：`TODO_WBS.md` の変更履歴と作業ログを直接読み、git log と比較。
- **AI が作業継続**：`TODO_WBS.md` の「次回ラウンド候補」と「作業ログ」を読み、どこから再開か把握。

---

## ⭐ Cross-Topic Quick References：5 つの核心テーマ、どこで見つけるか

方法論全体には全ディレクトリを貫く 5 つの主動脈があります。本ディレクトリがそれぞれにどう接続するか：

| Cross-Topic | 主要位置 | 本ディレクトリがどう接続するか |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 3 エンジン共読** | Root [`README_JA.md`](../README_JA.md) §🌟 ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | **本ディレクトリは AI-Native Living Book の「ストーリー入口」そのもの** — [`AI_NATIVE_LIVING_BOOK.md`](AI_NATIVE_LIVING_BOOK.md) が完全議論；4 つの権威概念ファイル（CLIENT_JOURNEY / EIGHT_STAGE_FLOW / METHODOLOGY_SCIENTIFIC_LOGIC / INDUSTRY_FRAMEWORK_ALIGNMENT）がすべてここにある |
| 🎓 **学術基盤（7 大支柱）** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **7 大理論支柱の統一論述が本ディレクトリにある**：Rosemann / Cohen & Levinthal / TTF / Teece / Sociotechnical Trust / Real Options / Knuth |
| 📚 **L1-L5 講座教育** | [`../02_Course_Design/`](../02_Course_Design/) | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 が **L1-L5 2 軸**（スケール軸 + AI 自律軸）の権威ある物語入口 |
| 🔁 **コンサルティング / 8 段階 + Phase A→B→C クローズドループ** | [`EIGHT_STAGE_FLOW_STORY.md`](EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **コンサルクローズドループ物語が本ディレクトリにある** — `EIGHT_STAGE_FLOW_STORY` §6 に完全クローズドループ図（Phase A 2W + Phase B 4W + Phase C 24M + 四半期レーダー回顧） |
| 📖 **参考資料 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | 本ディレクトリの物語は `90_References` のすべての素材を根拠として使用（PDF / 図 / ビデオノート / 学術理論引用） |
