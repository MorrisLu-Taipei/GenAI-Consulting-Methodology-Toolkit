# 90 References — 参考資料、出典と謝辞

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 本ディレクトリの目的

本ディレクトリは方法論全体の**「参考文献ライブラリ、引用ガバナンスセンター、謝辞リスト」**。`00`-`07` は「方法とツール」をカバー；本ディレクトリは 3 つに答える：

1. **これらの方法は何に基づくか？**（オリジナル PDF、方法論図、動画学習ノート）
2. **どの内容が第三者を引用するか？ライセンスはコンプライアンスか？**（引用される各プロジェクトは自身の `*_REFERENCE.md` を持つ）
3. **私たちは誰の肩の上に立つか？**（謝辞リスト）

対象：コンサルタント、レビュアー、法務、再配布者、**上流プロジェクトを探す学習者と愛好家**。

---

## 2. 謝辞：私たちが立つ肩

使用レベルで 4 カテゴリに整理：**Core プラットフォーム / コンサルティングフレームワーク / Agent & Skill / Case-Index**。各「Appreciation Card」は **上流 URL + どこで引用するか + 完全な `_REFERENCE.md` へのリンク** を含む。

### 2.1 Core プラットフォーム（L1-L5 のランタイム基盤）

これらは「引用される資料」ではなく — **L1-L5 コースが走るプラットフォーム**。これらなしでは本方法論は着地できない。

#### 🎯 [`open-webui/open-webui`](https://github.com/open-webui/open-webui)（オープンソース、ライセンスは上流 LICENSE 参照）

- **何か**：オープンソース、セルフホスト可能なエンタープライズ AI チャットインターフェース。複数 LLM プロバイダー（OpenAI / Anthropic / Ollama / OpenRouter / Azure 等）、アカウント / グループ / 役割 / 権限、個人チャットワークスペース、モデル制御、Pipelines、Function Calling、ナレッジベース、RAG、画像/音声/ファイルアップロードをサポート。
- **なぜ評価するか**：「**社内 AI チャットエントリポイント**」を「**ワンクリックインストール、フルオンプレ、権限階層化、監査可能**」にする数少ないオープンソースソリューションの一つ。データを SaaS に送らずに LLM を試せる — 製造 / 医療 / 政府のオンプレ展開に critical。アクティブなコミュニティ、迅速なバージョン進化。
- **どこで使うか**：**L1 Controlled AI Access の Core プラットフォーム** — [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) 完全コース計画；動画学習ノートは [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md)。

#### 🎯 [`n8n-io/n8n`](https://github.com/n8n-io/n8n)（Sustainable Use License、上流 LICENSE.md 参照）

- **何か**：オープンソースのワークフロー自動化プラットフォーム。ビジュアルエディタ、1000+ 統合（Gmail、Sheets、Notion、Slack、CRM、API、ERP、データベース、Webhook、カスタムノード）、サブワークフローライブラリ、Data Tables、Execution Logs、エラーハンドリング、スケジュールトリガー、AI / LangChain ノード。Self-Host と Cloud をサポート。
- **なぜ評価するか**：クロスシステム自動化の「**レゴブロック**」 — コンサルタントは 1-2 日で顧客デモ用の PoC を組み立てられる。アクティブなコミュニティ、豊富なテンプレート、健全なビジネスモデル。**Self-Hosting はエンタープライズ採用に critical**（データは内部に残る）。方法論著者は n8n Taipei Ambassador でもある。
- **どこで使うか**：**L3 Workflow Automation の Core エンジン** — [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) 完全コース計画；35 個の実装可能 PoC 仕様 [`../02_Course_Design/POC_SCENARIO_SPECS.md`](../02_Course_Design/POC_SCENARIO_SPECS.md)；30 個のワークフロー JSON スケルトン [`../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md`](../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md)；動画ノートは [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md)。

#### 🎯 [`nousresearch/hermes-agent`](https://github.com/nousresearch/hermes-agent)（Nous Research、上流 LICENSE 参照）

- **何か**：Nous Research のオープンソース **Knowledge-grade Autonomous Agent** リファレンス実装 — **Wiki-Capability-Map-Memory + ingest / query / update 三段階 Knowledge-Compounding + スケジュールタスク + Gate 4A-4E + HITL Human Review**。設計目標：検証可能な「完全自律 AI Agent スーパーアシスタント」。
- **なぜ評価するか**：「**Autonomous Agent + Knowledge Management**」を検証可能な design pattern に統合 — **「Knowledge-grade Agents の七つの設計原則」**（light-day-heavy-night / Knowledge-Compounding-Loop / P1>P2 / Write-Read-Same-Source / Tool-vs-LLM-Division / Failure-driven Learning / Why-not-just-RAG）は L4 Agent Design に完全な学習フレームワークを提供。
- **どこで使うか**：**L4 Autonomous Agent コースの設計バックボーン** — [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) §2 が七つの原則を説明。**境界**：コースは**コンセプトと design pattern のみ取り — ソースコード再現せず、フォークしない**。

#### 🎯 [`HKUDS/ClawTeam`](https://github.com/HKUDS/ClawTeam)（HKUDS、MIT）

- **何か**：HKU Data Science Lab（HKUDS）のオープンソース **Multi-Agent Collaboration Framework**。五層アーキテクチャ（Team / Workspace / Task / Inbox / Transport）、分離された Agent ワークスペース用 git worktree；CLI-driven；3 つのリファレンスシナリオ。
- **なぜ評価するか**：「Multi-Agent Team Collaboration」をデモスケールから「**実ワークフロー監査可能コラボレーション**」へ押し上げる — 各 Agent は自身の worktree、自身の Inbox、自身の Transport を持つ。チャット風の toy demo ではなく、実組織分業に近い。学術背景（HKUDS）+ MIT ライセンス。
- **どこで使うか**：**L5 Multi-Agent Organization の実装プラットフォーム** — [`../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md`](../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md) 完全コース計画；Manufacturing QA Team Walkthrough は [`../04_Scenarios/CLAWTEAM_WALKTHROUGH.md`](../04_Scenarios/CLAWTEAM_WALKTHROUGH.md)。
- **完全引用**：[`CLAWTEAM_REFERENCE.md`](CLAWTEAM_REFERENCE.md)

### 2.2 コンサルティングフレームワーク（03_Consulting_Report に影響）

#### 🎯 [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant)（MIT）

- **何か**：古典的コンサルティング分析フレームワーク（MECE、Pyramid Principle、Issue Tree、Porter's 5 Forces、SWOT、BCG Matrix、5 Whys、Fishbone、Business Model Canvas、WBS/RACI、NPV/IRR、Lean/Six Sigma 等 — 50+ フレームワーク）のプログラマティックな整理
- **なぜ評価するか**：散在するコンサルフレームワークを**構造化、引用可能、組み合わせ可能なライブラリ**へ変換 — もう一つの PPT コレクションではない
- **どこで使うか**：[`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) — 7 カテゴリ + フレームワークセレクタ + 8 段階へのマッピングに適応
- **完全引用**：[`CONSULTANT_FRAMEWORKS_REFERENCE.md`](CONSULTANT_FRAMEWORKS_REFERENCE.md)

#### 🎯 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills)（MIT）

- **何か**：McKinsey 等トップコンサルタントの「**問題 → レポート / Deck**」生産工芸を実行可能な 8 ステップワークフローへ変換
- **なぜ評価するか**：「Dummy Page → Dependency Management → 7 Page Layouts → Progressive Disclosure → Troubleshooting」の全セットを最初に教えられる SOP に書き下した — 「シニアコンサルタントだけが持つ暗黙の工芸」の代わりに
- **どこで使うか**：[`../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) — 8 ステップコンサルレポートワークフロー + §9 Troubleshooting Playbook に適応
- **完全引用**：[`MCKINSEY_SKILLS_REFERENCE.md`](MCKINSEY_SKILLS_REFERENCE.md)

#### 🎯 **Mirza Iqbal（[next8n.com](https://next8n.com)） — Workflow Delivery Framework**（MIT）

- **何か**：n8n デリバリーコンサルティングの**運用 SOP** — 完全な Discovery → Sprint → Handover ライフサイクル、価格表、顧客コミュニケーションテンプレート
- **なぜ評価するか**：**デリバリー作業の運用 SOP**（技術 SOP だけでなく）をオープンソース化した数少ない一つ — コンサル業界がめったに語らない運用面を埋める
- **どこで使うか**：[`../06_Delivery/`](../06_Delivery/) — Engagement Lifecycle、Role SOPs、Business Document Templates は全てこれにインスパイア
- **完全引用**：[`WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)
- **入手経路**：<https://github.com/MorrisLu-Taipei/AI-Workflow-Delivery-Framework>（README が Mirza Iqbal をオリジナル著者として記載）

### 2.3 Agent & Skill（02_Course_Design に影響）

#### 🎯 [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents)（MIT）

- **何か**：12 部門の Agent ペルソナライブラリ（Marketing、Sales、Customer Service、HR、Finance、R&D 等） — そのまま使える
- **なぜ評価するか**：「Agent ペルソナ設計」を再利用可能なライブラリにし、チームがゼロから System Prompt を書く手間を省く
- **どこで使うか**：[`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6「既存 Agent ライブラリ使用」モジュール
- **完全引用**：[`AGENCY_AGENTS_REFERENCE.md`](AGENCY_AGENTS_REFERENCE.md)

#### 🎯 [`MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack)（混合ライセンス）

- **何か**：n8n Skill 三層構造（Workflow Library + Cookbook + DSL Spec）、AI 生成 Workflow Skill Pack 付き
- **なぜここに**：これは方法論著者 Morris Lu 自身のプロジェクトだが、**引用規律を示す**ためにここに記載 — 自身のプロジェクトでもライセンスと第三者ソース（`_vendor/` MIT）が同じ標準で文書化されている
- **どこで使うか**：[`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) 後半
- **完全引用**：[`N8N_SKILL_PACK_REFERENCE.md`](N8N_SKILL_PACK_REFERENCE.md)

### 2.4 Case-Index（04_Scenarios に影響）

#### 🎯 [`Shubhamsaboo/awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps)（Apache-2.0）

- **何か**：150+ 実 LLM アプリケーションケース（Agent / RAG / Fine-Tuning / Multimodal 等）のキュレーションリスト、コミュニティ保守
- **なぜ評価するか**：高いキュレーション品質、明確な分類、継続更新；コンサルタントが顧客に「**他社はこのシナリオでこう実装している**」と言う時の最速リファレンス
- **どこで使うか**：[`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index — Dual-Axis Index（L1-L5 × エンタープライズ部門）にマップ；**マッピングは我々のもの**、オリジナルケースリストは Shubham Saboo とコミュニティ貢献者の著作権
- **完全引用**：[`AWESOME_LLM_APPS_REFERENCE.md`](AWESOME_LLM_APPS_REFERENCE.md)

#### 🎯 [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub)（MIT）

- **何か**：93+ AI エンジニアリング教育プロジェクト（RAG から Multi-Agent まで実行可能実装）
- **なぜ評価するか**：各プロジェクトに **コード + 教育動画** が付属、学習者は直接始められる；awesome-llm-apps の「キュレーションケース」を「ハンズオン実装」面で補完
- **どこで使うか**：[`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index 第二ソース — L2-L4 コース実行可能デモにマップ
- **完全引用**：[`AI_ENGINEERING_HUB_REFERENCE.md`](AI_ENGINEERING_HUB_REFERENCE.md)

---

## 3. オリジナル参考資料 & 図（自製または Public Domain）

| ファイル | 目的 |
| --- | --- |
| [`@AI-MD-PUBIC.pdf`](@AI-MD-PUBIC.pdf) | AI Transformation Maturity Model パブリック版マニュアル（オリジナル PDF 方法論ドラフト） |
| [`MD-Map.png`](MD-Map.png) | AI Maturity Map、ルート README で使用 |
| [`Metholodgy.png`](Metholodgy.png) | Enterprise Consulting Eight-Stage Transformation Guide、ルート README で使用 |

## 4. 学術基盤 & Failure Patterns（完全オリジナル、Tiger AI + 三 AI エンジンが執筆）

| ファイル | 目的 |
| --- | --- |
| [`FAILURE_PATTERNS.md`](FAILURE_PATTERNS.md) | 14 Failure Patterns（理論予測 + 実ケース + 対応修正） |
| [`AI_GOVERNANCE_ALIGNMENT.md`](AI_GOVERNANCE_ALIGNMENT.md) | NIST AI RMF / EU AI Act / ISO 42001 とのアライメント |
| [`PILOT_STUDY_PROTOCOL.md`](PILOT_STUDY_PROTOCOL.md) | 18-24 ヶ月実証研究設計（Pilot Study） |

学術理論自体（7 つの柱）は [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)。

## 5. 動画学習ノート（派生ノート；オリジナル動画著作権は制作者に帰属）

| ファイル | 目的 |
| --- | --- |
| [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md) | OpenWebUI 公式プレイリストからの学習ノート、L1 コース適用にマップ |
| [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md) | TigerAI チャンネルからの学習ノート、n8n / L3 コース適用に焦点 |

---

## 6. 引用規律（将来の貢献者のための鉄則）

本 repo で第三者資料を引用するには、**全て以下の「Approach A」原則に従う**：

| # | 原則 | どうやって |
|---|---|---|
| 1 | **独立適応 — フォークせず、ソースコード再現せず** | 構造とコンセプトを参照し、本方法論の声で書き直す |
| 2 | **明示帰属、二重記載** | (a) 引用ファイルのヘッダーノート；(b) 本ディレクトリの standalone `*_REFERENCE.md` |
| 3 | **方法論シナリオへ一般化** | 領域固有内容を L1-L5 AI トランスフォーメーションコンサルティングコンテキストへ変換 |
| 4 | **ライセンスなし = 統合なし** | LICENSE のない第三者プロジェクトは統合しない（外部例示 URL としてのみ引用） |
| 5 | **寛大な評価** | 引用ファイルで**何が良いか明示**、「下記ソース参照」だけではない |
| 6 | **失敗に正直** | 引用ツールが不適合と判明したら、`FAILURE_PATTERNS.md` に正直に書く — 成功談だけではない |

**使用ロジック**：「ディレクトリ Y のファイル X が何を引用したか」を見つける → そのファイルのヘッダーを読む → 本ディレクトリの対応する `*_REFERENCE.md` へジャンプして完全ライセンスノートを参照。

---

## 7. クロスディレクトリマッピング

| ディレクトリ | 本ディレクトリとの関係 |
| --- | --- |
| [`../00_Overview/`](../00_Overview/) | 方法論図（Metholodgy.png / MD-Map.png）はここから；7 理論柱の議論は `00` に住む |
| [`../02_Course_Design/`](../02_Course_Design/) | L1/L2/L3/L5 コースの第三者引用（OpenWebUI ノート、agency-agents、n8n-Skill-Pack、ClawTeam） |
| [`../03_Consulting_Report/`](../03_Consulting_Report/) | フレームワークライブラリとレポートワークフローの第三者引用（consultant、mckinsey-skills） |
| [`../04_Scenarios/`](../04_Scenarios/) | LLM アプリケーション Case Index の第三者引用（awesome-llm-apps、ai-engineering-hub） |
| [`../06_Delivery/`](../06_Delivery/) | デリバリー運用層の第三者引用（Mirza Iqbal フレームワーク） |
| [`../07_AI_Contributions/`](../07_AI_Contributions/) | 3 AI エンジン自身も「謝辞対象」 — Antigravity / Codex CLI / Claude Code |

---

## 8. 一般的な使用シナリオ

- **あるファイルがなぜそう書かれているか疑問**：ファイルヘッダーを読む → 本ディレクトリの `*_REFERENCE.md` にマップ
- **本方法論を再配布 / 商用化**：§6 引用規律 + [`NOTICE`](../NOTICE) 帰属要件を読む
- **新規オープンソースプロジェクトをオンボード** → §6 の 6 原則に従う：ライセンス確認 → 独立適応 → `*_REFERENCE.md` 作成 → 本 README §2 謝辞へ追加
- **上流コミュニティへの関与、インタラクト / 評価**：各 Appreciation Card の GitHub URL をクリックして Star、Follow、Issue 開設、PR 送信
- **学習者が repo 内容を自身のペーパー / Deck で引用**：§6 に従い、本方法論を引用する際はオリジナル著者帰属を保持（[`../NOTICE`](../NOTICE)）；第三者資料を引用する際は対応する `*_REFERENCE.md` の学習者引用形式に従う

---

## 9. 謝辞

本ディレクトリにリストされた全上流著者とコミュニティは**本方法論が立つ肩**。誤解、不適切引用、オリジナル目標からの逸脱はいかなるものも方法論著者 **Tiger AI Morris Lu 盧業興** の単独責任 — 上流著者やコミュニティのものではない。

あなたが上流著者で本 repo の引用が不適切、修正が必要、強化されるべきと感じたら — Issue を開くか Morris Lu に連絡してください、すぐに対応します。

> **アーキテクチャ所有権**：本 repo の方法論アーキテクチャは人間著者 **Morris Lu（Tiger AI）** が提案。3 AI エンジン（Antigravity / Codex / Claude Code）は**実行、補完、拡張、監査**するツール。[`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0 参照。
