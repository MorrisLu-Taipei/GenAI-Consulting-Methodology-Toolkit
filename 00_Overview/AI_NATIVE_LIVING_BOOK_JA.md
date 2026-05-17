# AI-Native Living Book：方法論を Executable Knowledge Artifact として

> 🌐 言語：[繁體中文](AI_NATIVE_LIVING_BOOK.md) ｜ [English](AI_NATIVE_LIVING_BOOK_EN.md) ｜ [Deutsch](AI_NATIVE_LIVING_BOOK_DE.md) ｜ [Français](AI_NATIVE_LIVING_BOOK_FR.md) ｜ [Español](AI_NATIVE_LIVING_BOOK_ES.md) ｜ 日本語 ｜ [한국어](AI_NATIVE_LIVING_BOOK_KR.md)
>
> Apache License 2.0 · 著者：Morris Lu · Tiger AI

最終更新：2026-05-16

---

> **本ドキュメントが答えるもの**：本方法論の最も特徴的な特徴は内容ではなく — その**運搬媒体**。伝統的コンサルティング方法論は PDF / PPT / SOP（静的ドキュメント）；本 repo は **AI IDE が読取可能、説明可能、クエリ可能、適用可能なナレッジシステム**。ユーザーは「ドキュメントを読む」のではなく — **方法論と会話する**。本ドキュメントはこの特性を方法論の位置づけに正式に書き込み、その学術的分類 + リスクコントロールに対処。

---

## 1. 一文位置づけ / タグライン

> 本リポジトリは方法論ツールキットだけでなく、**AI-native living book**：AI IDE で開かれた時、その埋め込みエージェント指示（[`AGENTS.md`](../AGENTS.md) と [`CLAUDE.md`](../CLAUDE.md)）が静的方法論を**対話型共読チューターとコンサルティングアシスタント**へ変換。

---

## 2. なぜこれが新しい形式の方法論か

### 2.1 伝統的方法論 vs. AI-Native Living Book

| 次元 | 伝統的（PDF / PPT / SOP）| AI-Native Living Book（本 repo）|
| --- | --- | --- |
| **媒体** | 静的ドキュメント、スライドデッキ、Word | Markdown + AI IDE 指示ファイル（AGENTS.md / CLAUDE.md）|
| **ユーザー対話** | 一方向読み取り | 双方向会話（Q&A、適用、生成）|
| **オンボーディング障壁** | 高（100+ ページを読む必要）| 低（AI が自動読み取り、共読チューターになる）|
| **適用方法** | コンサルタントが顧客のために翻訳 | 顧客が AI に直接、彼らの会社に適用を依頼 |
| **挑戦可能か** | いいえ（ドキュメントは答えない）| はい（AI がリアルタイムで任意の質問に答える）|
| **書き直し可能か** | コンサルタントが編集必要 | 顧客が fork + AI が一貫性チェックを支援 |
| **バージョン管理** | 通常なし | 完全な Git 履歴（AGENTS.md 変更含む）|
| **学術引用** | PDF 引用 | GitHub commit hash + 再現可能実行環境を引用 |

### 2.2 学術的分類

本方法論は以下のうち 1 つ（または複数）として分類可能：

| 名前 | 強調プロパティ | 起源 / アナログ |
| --- | --- | --- |
| **Executable Knowledge Artifact** | 実行可能な知識；単に記述ではなく、適用可能 | Jupyter Notebooks、computational essays |
| **AI-Mediated Methodology** | ユーザーと方法論の間の媒介としての AI | Intelligent Tutoring Systems（ITS）|
| **Interactive Consulting Playbook** | 対話型コンサルティング運用マニュアル | Game playbooks、decision-tree wizards |
| **Living Book with Embedded Tutor Agent** | Living book + 埋め込みチューターエージェント | Hypertext、knowledge graphs |

Tiger AI は **AI-native living book** を主要用語として採用、なぜなら「living book」（コンテンツ進化）+「AI-native」（AI 向け設計）+「co-reading tutor」（埋め込みチューター人格）を**同時に捕捉**するから。

---

## 3. 3 層：Repo as Book / Agent as Tutor / Methodology as Executable Artifact

### 3.1 Layer 1：Repo as Book

Repo 構造は本の慣例に従う：

| 本要素 | Repo マッピング |
| --- | --- |
| カバー / 一文位置 | Root [`README_EN.md`](../README_EN.md) + 本 doc §1 |
| 序文 / executive summary | [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) |
| ストーリー章 | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) 明のストーリー |
| メイン方法論 | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 |
| 実装章 | `01_Assessment` / `02_Course_Design` / `03_Consulting_Report` |
| ケースアンソロジー | `04_Scenarios/` 7 Benchmark-grade ケース |
| Sales サポート | `05_Sales/` |
| Delivery SOP | `06_Delivery/` |
| 学術論証 | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) |
| アライメントマップ | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) |
| Failure modes（counter-cases）| [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) |
| 研究設計 | [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) |
| 参考文献 | 各ファイルの参考文献 + `90_References/` |

> **重要点**：この「本」は**完全** — 顧客 / コンサルタント / 学者 / 規制者がそれぞれ関連章を見つけられる。

### 3.2 Layer 2：Agent as Tutor（AGENTS.md は「チューター人格」）

[`AGENTS.md`](../AGENTS.md) と [`CLAUDE.md`](../CLAUDE.md) は補足ノートではなく、**AI の役割、境界、ガイダンスを repo に埋め込み**。AI IDE（Claude Code / Cursor / Antigravity / Codex など）はこれらファイルを自動読み取り、**「本方法論の共読チューター」**として位置づける。

#### AGENTS.md で定義された「チューター人格」

- **役割**：AI = 共読チューター + コンサルティングアシスタント、コンサルタント置換ではない
- **回答可能質問の範囲**：方法論定義、L1-L5 マッピング、Stage ツール、ケース適用、レポートドラフト
- **拒否範囲**：顧客最終決定、コンサルタント判断バイパス、未検証 ROI コミットメント
- **応答スタイル**：学術的厳密性 + コンサル実践 + 顧客理解可能
- **引用規律**：すべての結論に [E:L#] エビデンスレベル（Tool 8.9 別）タグ
- **言語**：ユーザーによる EN/ZH バイリンガル切替

> この設計は **LangChain Agent Prompt + Claude Skills** から借りる：repo でバージョン管理される設定ファイル。

### 3.3 Layer 3：Methodology as Executable Artifact

ユーザーは AI に方法論を**実行**するよう直接依頼可能、読むだけでなく：

#### 典型的対話

| ユーザー質問 | AI 共読チューター実行 |
| --- | --- |
| 「我々は 700 名パッケージング工場；10-Q クイックサーベイ実行を手伝って」 | AI が [`AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) 10-Q 版実行 + 自動スコア + レーダー作成 |
| 「私の回答に基づき、Phase A 中間エンゲージメントレポートスケルトンをドラフト」 | AI が [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) §3-§5 構造別ドラフト生成 |
| 「我々は製造業；どのケースが我々に最も近い？」 | AI が [`SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md) と比較しギャップを計算 |
| 「Stage 3 Client Ideal Practice ワークショップ用資料準備」 | AI が Tool 3.6 別ワークショップフロー + 付箋プロンプト + 4 層プリントアウト生成 |
| 「これは McKinsey 7-Step とどうアラインする？」 | AI が [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) §2.1 にマップ |
| 「私の Stage 2 レーダーは 24 ヶ月後より丸くなるべき？」 | AI がユーザーを四半期 Gate C レビューを通じて導く |

> **これが「Methodology as Executable Artifact」の意味** — 方法論は単に記述されるのではなく；AI を介してリアルタイムで適用可能。

---

## 4. 方法論採用障壁を下げる

### 4.1 企業は 100+ Markdown ファイルを恐れる

伝統的方法論の障壁：

- 100+ ページを読む ❌
- 用語が多すぎ ❌
- 何を最初に読むべきか不明 ❌
- 翻訳のためコンサルタントが必要 ❌
- レポートドラフトを自分で書かなければならない ❌

### 4.2 AI 共読チューターがリアルタイムで応答

repo + AI IDE が開かれると、ユーザーは直接質問：

- 「**私の会社はどのレベル？**」 → AI が 10-Q サーベイ実行 + 自動スコア
- 「**最初にどのファイルを読むべき？**」 → AI が役割別（CEO / コンサルタント / IT / 学者）読み取り順序を推奨
- 「**製造業にどう適用？**」 → AI が製造業ケースを引用 + カスタマイズポイントをフラグ
- 「**診断レポートの初版ドラフトを生成して**」 → AI が 10-15 ページ Phase A スケルトン作成
- 「**Stage 4 と Stage 8 の境界は？**」 → AI が METHODOLOGY_SCIENTIFIC_LOGIC §4 を引用

> **これにより方法論が「専門家のみ読み取り可能」から「非専門家も導かれて通過可能」へシフト。**

### 4.3 採用障壁減少の期待

PILOT_STUDY_PROTOCOL で検証される仮説：

- 伝統的 PDF 方法論：顧客完了率 < 15%
- **AI-native living book**：顧客「会話率」 > 70%（AI が積極的に導く）
- 中規模企業（100-500 名）採用サイクル：「3 ヶ月評価必要」から → 「2 週間以内に Phase A」へ

---

## 5. リスクコントロール

⚠️ AI が方法論を解釈するため、**AI 共読チューターは以下を行ってはならない**：

### 5.1 チューター境界

| 可能 | 不可 |
| --- | --- |
| 方法論コンテンツ説明 | ❌ 正式コンサルタント判断を置換 |
| サーベイ実行、自動スコア、レーダー作成 | ❌ 顧客に特定 ROI 数字を約束 |
| ケース引用しギャップ計算 | ❌ Ideal Practice Definition Table 署名（3 者人間署名必要）|
| レポートドラフト生成 | ❌ 顧客オーナー / コンサルタント最終レビュー置換 |
| Stage Gate 自己評価ガイド | ❌ 第三者監査置換 |
| 80/20 / 5 Whys / Issue Tree をリアルタイムで適用 | ❌ 縦断的 KPI 実データ置換 |

### 5.2 4 つのリスクコントロール原則

1. **AI 共読チューター ≠ コンサルタント**：すべてのレポートドラフトは外部使用前に**人間コンサルタントまたは顧客オーナーレビュー**必要
2. **重要診断はエビデンス必要**：[`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9 別、主要結論は L3+（system log）サポート必要
3. **AGENTS.md バージョン管理**：AI IDE 間で一貫性のない解釈を回避 — すべての AGENTS.md 変更を Git にコミットし CHANGELOG に記録
4. **AI-generated マーキング**：Tool 8.8 §7 別、AI 生成コンテンツはすべて「AI-generated」とマーク必要

### 5.3 失敗シナリオ

AI 共読チューターが誤用される場合（[`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) に文書化）：

- AI が間違い、顧客がそれを額面通りに受け取る → 間違ったレポート
- AI が未検証 ROI 数字を与える → 顧客が偽の希望に基づき SOW 署名
- 異なる AI IDE が AGENTS.md を異なって解釈 → 一貫性のない結論

**緩和**：

- AGENTS.md が明示的に「**Don't predict ROI without baseline data**」を必須化
- 各レポート段落に [E:L#] エビデンスレベルタグ必要
- 顧客に重要な結論を ≥ 2 AI IDE で相互検証することを推奨

---

## 6. 学術的貢献

### 6.1 IS / コンサルティング方法論への貢献

| 貢献 | イノベーション |
| --- | --- |
| **方法論媒体イノベーション** | AI IDE で直接実行可能な Markdown + エージェント設定として構築された最初のコンサルティング方法論 |
| **AI-mediated knowledge transfer** | 「ナレッジトランスレーター」として AI を使用、方法論採用障壁を下げる |
| **オープンソースコンサルティングフレームワーク** | Apache 2.0、他のコンサルタントが fork / 適応可能、学術的に再現可能 |
| **Embedded tutor agent design pattern** | AGENTS.md / CLAUDE.md パターンは他のオープンソース repo が借用可能 |

### 6.2 AI Pedagogy / ITS との接続

- 1980 年代 ITS 研究は「AI がどう教えるか」を研究 → 本方法論は「**AI がどう成人がプロフェッショナル方法論を学ぶことを助けるか**」の新ケース
- Vygotsky の ZPD（Zone of Proximal Development）の適用：AI 共読チューターが動的にプロンプト深度を調整

### 6.3 将来の研究

- AGENTS.md 解釈のクロス IDE 一貫性（Claude Code / Cursor / Antigravity / Codex / Windsurf）
- AI 共読チューターの方法論採用率への効果の縦断的トラッキング（PILOT_STUDY_PROTOCOL 設計別）
- クロス言語（EN / ZH / JA / KO）方法論採用性研究

---

## 7. 他ドキュメントとの結合方法

### 7.1 異なる場所でのステートメント

| 場所 | メインメッセージ |
| --- | --- |
| Root [`README.md`](../README.md) | 一文位置づけ（ZH §1）|
| Root [`README_EN.md`](../README_EN.md) | 一文位置づけ（EN §1）|
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) | 「Living Book」セクション |
| [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) | 「How to Read This Book」セクション |
| [`AGENTS.md`](../AGENTS.md) | 具体的チューター人格設定（repo root で）|
| Sales デッキ | 「AI-native living book」差別化を強調する 1 スライド |
| 学術提出 | 方法論貢献として全章 |

### 7.2 他 4 つの権威的コンセプトドキュメントとの関係

| ドキュメント | 答える質問 |
| --- | --- |
| [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) | 「ユーザーは何を体験するか？」 |
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | 「方法論はどう実行するか？」 |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | 「なぜ方法論が議論に耐えるか？」 |
| [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | 「業界フレームワークとどうアラインするか？」 |
| **`AI_NATIVE_LIVING_BOOK_EN.md`（本 doc）** | **「なぜ方法論の媒体が新しいか？」** |

5 つの権威的ドキュメントが完全な方法論議論を形成：**経験 + プロセス + 科学 + アライメント + 形式イノベーション**。

---

## 8. 参考文献

- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors: Lessons learned. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.
- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Pérez, F., & Granger, B. E. (2007). IPython: A system for interactive scientific computing. *Computing in Science & Engineering*, 9(3), 21-29.
- Anthropic (2024). *Claude Code documentation*：<https://docs.anthropic.com/claude/docs/claude-code>
- OpenAI (2024). *Codex / Codex CLI*.
- Cursor (n.d.). *Cursor IDE documentation*.

---

## 9. クロージング：方法論の次フェーズ

コンサルティング方法論の進化：

```
1990 年代：紙コンサルレポート
   ↓
2000 年代：PowerPoint デッキ
   ↓
2010 年代：SharePoint / Confluence wiki
   ↓
2020 年代：GitHub ホスト方法論 + オープンソース
   ↓
2025 年代：AI-Native Living Book（本方法論）
```

**次は？** 可能性として **マルチエージェントコンサルティングチームが完全 Phase A を自動実行**（AI コンサルタント + AI レビュアー + AI 顧客シミュレーター、3 エージェント協働）— L5 Multi-Agent Organization を「方法論自体」に適用。

**しかし**：§5.1 別、AI は常にツールとチューター、決して置換ではない。人間コンサルタント判断、顧客オーナー意思決定、第三者監査 — これら**人間ガバナンス層**が方法論信頼性の最終保証。

---

ライセンス & 引用

本ドキュメントは Apache License 2.0；[`../NOTICE`](../NOTICE) 帰属が保持されることを条件に、使用、修正、商業化可能。
