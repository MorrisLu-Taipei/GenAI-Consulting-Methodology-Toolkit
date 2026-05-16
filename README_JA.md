# GenAI Consulting Methodology Toolkit

言語: [繁體中文](README.md) | [English](README_EN.md) | [ภาษาไทย](README_TH.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | 日本語 | [한국어](README_KR.md)

エンタープライズ AI トランスフォーメーション成熟度診断と導入方法論ツールキット（Enterprise AI Transformation Maturity Assessment & Implementation Methodology Toolkit）。

原作者: **Tiger AI Morris Lu 盧業興**  
肩書: **n8n Taipei Ambassador / 国立台湾科技大学 智慧製造研究所 博士課程 / QUT クイーンズランド工科大学（オーストラリア）コンピュータ科学修士**

ライセンス概要: 本プロジェクトは **[Apache License 2.0](LICENSE)** を採用しています。自由に使用・複製・改変・再配布・商用利用が可能です。再配布の際は Apache 2.0 ライセンス文と [`NOTICE`](NOTICE) の作者名を保持してください。

> **5 分しかない方は** まず [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) を読んでください — 1 ページで全方法論を理解できます。

---

## 🌟 これはただの本ではなく、AI-Native Living Book — 本当に「生きている」本

本は世代ごとに進化してきました。各世代が一つの問題を解決し、一つの欠落を残してきました — **どれも本当に「生きている」本ではありませんでした**:

- **第 1 世代 — 印刷書**: 知識を保存し次の読者へ伝えます。しかし**読むことしかできず、返答しません**。あなたの質問に答えられず、あなたの会社がどんな形か知らない — **静止した紙**にすぎません。
- **第 2 世代 — インタラクティブブック**: Web や Wiki に載せられ、検索・リンク・コメントができるようになりました。印刷書より「**インタラクション**」が増えましたが、**自分からあなたに何かを提案することはなく**、まして分析や新しいものの生成もしません — 依然として受動的：インターフェイスは生きたが、コンテンツは生きていない。
- **第 3 世代 — AI-Native Book（本リポジトリ）— 本当に「生きている」本**: Markdown で方法論本体を書き、AI IDE で開く — AI が本全体を自動で読み、**あなたが問い、あなたに答え、あなたと一緒に考える**。さらに**あなたの会社の実情に応じてカスタマイズされた助言を行い、診断を実行し、レポート草案を書き、シミュレーション演習を行います**。本自体が応答し、拡張し、あなたの問いとともに新章を成長させます。

言い換えると：印刷書は知識を伝え、インタラクティブブックは検索を容易にし、**AI-Native Book は史上初めて「本」を本当に生きた存在にし、あなたと一緒に考える相棒になります**。最終決定は依然として人間が下しますが、もう静的な方法論を一人で前にすることはありません。

> *Three generations of books: printed (read-only, dead) → interactive (search & link, still passive) → **AI-native (truly alive — advises, analyzes, simulates, and grows with your questions)**. Open with an AI IDE; AI becomes your reading partner, consulting assistant, and auditor.*

### 🔱 3 つの AI エンジン、それぞれ得意分野が違う

同じ内容でも、選んだ AI IDE によって**まったく異なる人格**を示します:

| エンジン | 役割 | 最も得意なこと |
| --- | --- | --- |
| 🟦 **Antigravity** | 最前線コンサルタント | 顧客との会話、アンケート実行、レポート草案 |
| 🟪 **Codex CLI** | 方法論の監査員 | クロスファイルテスト、レッドチーム演習、バージョン管理、断絶リンクの修復 |
| 🟨 **Claude Code** | クロスファイル思考のパートナー | 深層統合、多視点ディベート、シミュレーション、顧客向け Fork |

3 つのエンジンは互いに置き換えるのではなく、**分業協力**します：午前は Antigravity で顧客と打ち合わせ、午後は Codex でレポート草案を監査、夜は Claude Code でシナリオシミュレーション。各ワークスペースは独立（`.agent/` / `.codex/` / `.claude/`）し、干渉しません。

各エンジンの詳細な自己記述は [`07_AI_Contributions/`](07_AI_Contributions/) を参照。インストール手順は下記の [3 つの AI エンジンのインストールと起動ガイド](#-3-つの-ai-エンジンのインストールと起動ガイド--three-ai-engines-setup-guide) を参照。

### さまざまな読者にとっての意味

- **CEO / 経営層**: このリポジトリを ChatGPT / Claude / Gemini に投げ込み、10 分の Q&A で「我が社はどのレベルにいるのか？まず何をすべきか？」の初期判断が得られます。
- **コンサルタント / 受講者**: AI IDE で開き、診断からレポート、24 ヶ月の導入ロードマップまで完全な対話型コンサルティング体験を実行できます。
- **学者 / 研究者**: `/devil-pair-debate`、`/thought-experiment` を直接実行して方法論の価値観前提を議論できます。背後には 7 大理論支柱と 28 本の引用可能な古典があります。
- **規制 / コンプライアンス**: `/evidence-audit`、`/generate-traceability` を実行し、監査可能な証拠連鎖を取得し、NIST AI RMF / EU AI Act / ISO 42001 と整合させられます。

> ⚠️ **正直な開示**: 方法論の全体アーキテクチャは **Morris Lu（人間）** が設計しました。3 つの AI エンジンは実行・補完・監査のツールにすぎません。詳しくは [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0。本書のすべてのケースは AI シミュレーションによる教育用例であり、**実際の顧客データではありません**。

---

## この方法論が解決する課題

多くの企業が AI 導入時にいきなりツールに飛びつきます — 今日は ChatGPT を買い、明日は n8n を試し、来週は Agent を作りたいと言う。典型的な問題：社員が使えない、プロセスがつながらない、データがガバナンスされていない、PoC が検収されない、最終的に経営陣も AI がどのレベルの成熟度にあるか分からない。

本ツールキットの戦略：まず簡易アンケートで企業の現在の AI 成熟度を診断し、L1-L5 に従って講座比率と導入経路を設計します。講座は受講して終わりではなく、各レベルで検証可能な成果物を残し、最後に AI トランスフォーメーション診断の 8 段階プロセスで、完全な診断レポート・ロードマップ・ROI・ガバナンス提言を生成します。

## 講座開始前の未来想像

顧客が L1-L5 講座を受けるか決める前に、最も必要なのは未来の絵を見ること：「5 つのツールを学ぶ」ではなく、「**講座終了後、会社の日常業務はどう変わるのか？**」。

主軸は **規模が一層ずつ拡大し、最終的に「人間が AI を使う」から「AI が自分で働く」へ育つ**：**個人 → 部門 → 部門横断/全社 → AI スーパーアシスタント（個体）→ AI チーム**。3 ヶ月後の月曜朝を想像してください:

- **L1 Controlled AI Access ─ スケール軸·個人**: **各社員が一人ひとり**自分のアカウントで OpenWebUI にログインし、自分のチャットエリア、履歴、部門権限を持ちます。営業は顧客メールを書き、HR は研修サマリーをまとめ、マネージャーは会議要点を作成 — すべて同じ制御された AI 入口から始まる。**単位は「個人」**、AI が各人のそばにいる。
- **L2 Knowledge Codification ─ スケール軸·部門**: **単位が「部門」へ昇格**。ベテランは個人で上手いだけでなく、**部門責任を境界**として、コピーライティング、レポート、カスタマーサービス回答、SOP 解釈、開発手法を再利用可能な Skill にまとめます。新人や部門内の他メンバーが同じ方法を使い、**部門全体**の出力品質が一貫し始める。
- **L3 Workflow Automation ─ スケール軸·部門横断 / 全社**: **単位がさらに「部門横断、全社」へ昇格**。n8n が各部門の Skill とシステム（Gmail、Sheets、Notion、CRM、API、ERP）を連結。1 通のクレームメールが届くと、**営業・カスタマーサービス・CRM・マネージャーなど複数部門を横断**して自動処理 — システムが CRM を照会し、フォームを更新し、タスクを作成し、マネージャー向け要約を生成、人間は判断と承認のみ。AI が **全社プロセス** に入る。
- **L4 Autonomous Agent ─ AI 自律軸·スーパーアシスタント（AI 個体）**: **「人間部隊」とは別に AI エンティティが追加で育つ**。Hermes Agent が毎日タスク、ドキュメント、Workflow 結果、Wiki 記憶を読み、briefing、追跡リスト、HITL（Human-in-the-Loop、人間がループ内でレビュー）が必要な意思決定点を生成。企業は**検証可能な知識型 AI エンティティ**を持つ、フル自動スーパーアシスタントを一人雇ったような状態。
- **L5 Multi-Agent Organization ─ AI 自律軸·AI チーム**: **複数の L4 個体がさらに「AI チーム」に編成される**。ClawTeam が市場・製品・カスタマーサービス・財務・運営の専門 Agent を機能分業に編成し、新製品ローンチ、品質改善、患者サービス改善、顧客経営タスクを協働。企業は **「人間チーム + AI チーム」の 2 部隊** を同時に持つ。

このストーリーは講座開始前に語るべきです。顧客が「**規模が一層ずつ拡大する仕組み、AI がツールからデジタル人財へ育つ仕組み**」を理解した後、アンケート診断がなぜ必要か、講座を L1-L5 に分ける理由、各レベルに deliverables・evidence・Stage Gate が必要な理由を振り返れます。

> ⚠️ 2 軸のより詳しい説明（なぜ L3 → L4 が分水嶺か、なぜガバナンスは常に人間が保持するか）は [§L1-L5 の 2 つの軸](#l1-l5-の-2-つの軸) を参照。

## AI 成熟度マップ

![AI Maturity Map](90_References/MD-Map.png)

## 方法論の全体像

![Enterprise Consulting Methodology: Eight-Stage Transformation Guide](90_References/Metholodgy.png)

## メインストーリーライン

```text
AI 成熟度アンケート
→ 企業属性・業界状況・デプロイ方式の調査
→ L1-L5 講座比率の設計
→ L1 OpenWebUI 企業アカウントと個人チャットエリアを有効化
→ L2 Antigravity / Claude Code / Codex で Skill 化トレーニング
→ L3 n8n で Gmail, Sheets, Notion, CRM, API, ERP などを連携
→ L4 Hermes Agent で検証可能な自動 Agent 業務
→ L5 ClawTeam で Agentic Team 協働
→ シナリオケース、Evidence、Stage Gate
→ 8 段階 AI トランスフォーメーションコンサル診断
→ AI トランスフォーメーション診断レポート、ロードマップ、ROI、ガバナンス提言
```

## L1-L5 成熟度モデル

| レベル | 名称 | ツール / プラットフォーム | 軸 | 企業ポジショニング |
| --- | --- | --- | --- | --- |
| L1 | Controlled AI Access | OpenWebUI | スケール軸·個人 | 企業内の AI 会話入口を確立し、各社員に専用アカウント・チャットエリア・権限境界を提供 |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | スケール軸·部門 | 部門責任を単位として、個人の知識・プロンプト・文書・作業方法を再利用可能な Skill にまとめる |
| L3 | Workflow Automation | n8n | スケール軸·部門横断 / 全社 | 部門横断 Skill を連結し email, Sheets, Notes, CRM, API, ERP 等のシステムと結合、AI を全社自動化プロセスに導入 |
| L4 | Autonomous Agent | Hermes Agent | AI 自律軸·スーパーアシスタント | Wiki ケーパビリティマップ・AI ツール・Workflow・自動スケジューリング・自律学習を組み合わせ、検証可能なフル自動 AI Agent スーパーアシスタントを構成 |
| L5 | Multi-Agent Organization | ClawTeam | AI 自律軸·AI チーム | 複数の専門 Agent が機能分業し、部門・プロセスを横断する企業タスクを AI チームとして協働遂行 |

### L1-L5 の 2 つの軸

L1-L5 は「5 つのツール」ではなく、**2 つの軸**でつながった成熟度の経路です:

- **L1 → L2 → L3: スケール軸（人間が AI を使う / 監督する）**。この 3 層は「人がループ内、人が AI を使い、人が AI を監督する」フェーズで、組織規模に沿って段階的に拡大 — **L1 個人**（各社員が個別に AI 使用）→ **L2 部門**（部門責任を単位として個人知識を再利用可能 Skill にカプセル化）→ **L3 部門横断 / 全社**（部門横断 Skill を連結しシステムと結合、AI が全社自動化に進入）。
- **L4 → L5: AI 自律軸（AI が完全自律、人間のリアルタイム監督不要）**。この 2 層は企業が人間部隊の外に「**追加で育てた**」AI エンティティ — **L4 AI スーパーアシスタント**（フル自動 AI Agent 個体）→ **L5 AI チーム**（複数の専門 Agent が機能分業協働）。

> 重要な分水嶺: **L1-L3 は「人間が AI を補助 / 監督」、AI はツール；L4-L5 は「AI が自律稼働」、AI は企業の追加デジタル人財。** 導入順序として、L1-L3 でまず人と組織を整え、L4-L5 を強固な基盤の上に自律 AI として成長させる。
>
> L4-L5 においても、**ガバナンスフレームは依然として人間が構築し、人間が監督権を保持** — AI が自律するのは「業務執行」であり、「ガバナンス意思決定」ではない。各層は HITL（Human-in-the-Loop）と Stage Gate を保持し、AI が自律になるほど、人間の役割は「ガバナー」に格上げされ、置き換えられはしない。

## 各レベルの検収方法

| レベル | Input | Process | Output | Evidence | Stage Gate |
| --- | --- | --- | --- | --- | --- |
| L1 | 社員役割、頻出タスク、AI 使用の痛点、権限ニーズ | OpenWebUI 構築、アカウント / グループ / 権限、個人チャットエリア、Prompt 基礎研修 | 企業 AI 会話入口、Prompt リスト、ユースケースリスト | アカウント表、権限表、ログインログ、チャットエリアのスクリーンショット、Prompt サンプル | 安全にログインでき、権限分離でき、追跡可能な使用記録を残せるか |
| L2 | L1 高頻度 Prompt、文書、SOP、個人作業方法 | Antigravity / Claude Code / Codex で知識を Skill と再利用可能 artifact にカプセル化 | Skill Library、Agentic artifacts、Workflow Blueprint | Skill 文書、テストケース、バージョン履歴、出力サンプル | Skill が他者により再利用され安定出力できるか |
| L3 | L2 Skill、プロセスブループリント、システム一覧、API / CRM / ERP / Sheet 権限 | n8n で自動化フロー、Data Table、Execution Log、エラー処理を構築 | Workflow PoC、Sub-workflow Library、Data Tables、L4 Workflow Contract | n8n workflow、execution log、再実行ログ、システム連携スクリーンショット | Workflow が実データ・実システム上で安定稼働するか |
| L4 | L3 Workflow、L2 Skill、企業 Wiki、タスクルール、HITL 人間レビュー点 | Hermes Agent でタスクカード、Wiki ingest/query/update、スケジューリング、ツール呼び出し、Gate 4A-4E を構築 | 検証可能 Agent、Briefing、タスク処理ログ、Gate sign-off | Agent log、Wiki バージョン、タスクカード、briefing、人間承認記録 | Agent が制御境界内で自律的にタスク完了し evidence を残せるか |
| L5 | 複数の L4 Agent、部門横断タスク、役割責任、ガバナンスルール | ClawTeam で Agentic Team を編成、役割・協働ルール・引継ぎ・監督を定義 | Agent Team、役割カード、協働フロー、部門横断成果 | Team run log、役割カード、引継ぎログ、成果文書、ガバナンスログ | Agent Team が安定協働し、追跡可能な成果を生み出せるか |

## 講座設計の原則

講座比率は顧客の成熟度・業界・デプロイ方式・目標シナリオで決まります。すべての企業が一度に L1-L5 を網羅する必要はなく、まず最も即座に成果物を生み出せる層を見つけ、上に積み上げます。

| 調査次元 | 用途 |
| --- | --- |
| 企業属性 | 研究開発製造、マーケティングサービス、医療機関、内部運営、その他のいずれか判定 |
| デプロイ方式 | クラウド AI、ハイブリッド、フルオンプレのいずれか |
| システム現況 | Gmail, Sheets, Notion, CRM, API, ERP, データベース、内部システムの棚卸し |
| プロセス成熟度 | SOP、process owner、データフィールド、例外処理が既にあるか判定 |
| リスク要件 | セキュリティ、プライバシー、医療 / 製造 / 金融コンプライアンス、人間 sign-off ニーズの評価 |

## ディレクトリ構造

| ディレクトリ | 用途 |
| --- | --- |
| [`00_Overview`](00_Overview/) | ソリューション概要、メインストーリー、WBS |
| [`01_Assessment`](01_Assessment/) | AI 成熟度アンケート、スコアリングモデル、成果物と evidence マトリクス |
| [`02_Course_Design`](02_Course_Design/) | L1-L5 講座設計、企業属性、デプロイ方式、講座モジュールマトリクス |
| [`03_Consulting_Report`](03_Consulting_Report/) | AI トランスフォーメーション診断レポート テンプレート |
| [`04_Scenarios`](04_Scenarios/) | 顧客シナリオ、コントロール表、製造業ケース、病院ケース |
| [`05_Sales`](05_Sales/) | バリュープロポジション、営業トーク、FAQ |
| [`06_Delivery`](06_Delivery/) | 納品パッケージと検収基準 |
| [`90_References`](90_References/) | 元 PDF、方法論図、ビデオ学習ノート、引用資料 |

## 5 タイプの読者、まずこの 5 つから

| あなたは | ここから始めましょう |
| --- | --- |
| **CEO / オーナー / 家族** — 20 分で方法論を理解 | [`00_Overview/CLIENT_JOURNEY_STORY_EN.md`](00_Overview/CLIENT_JOURNEY_STORY_EN.md) — Ming の物語 |
| **コンサルタント / 受講者** — 8 段階の運び方、契約の分け方を知りたい | [`00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) — 完全フロー |
| **取締役会 / 規制 / 学術** — なぜこの方法論が議論に耐えるか | [`00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — 科学的論証 |
| **大企業 IT / 他社からの転職コンサル** — McKinsey/BCG/TOGAF/Gartner との整合 | [`00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — 整合マップ |
| **急いでる管理職** — 5 分しかない | [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) — Executive Summary |
| **方法論研究者 / AI Pedagogy 学者** — なぜ新型の方法論か | [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) — AI-Native Living Book 設計 |
| **学者 / 規制 / 取締役会** — 7 大理論支柱（Rosemann / Cohen & Levinthal / Teece / Real Options 等）| [`00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — 学術理論基礎 |
| **コンサルタント / スコアキャリブレーション** — 0-4 点を客観的に評価する方法 | [`01_Assessment/BARS_RUBRICS_EN.md`](01_Assessment/BARS_RUBRICS_EN.md) — BARS 行動アンカー |

## 推奨読書順

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md)
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md)
4. [`01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)
5. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
6. [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md)
7. [`02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md)
8. [`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md)
9. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md)
10. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md)
11. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)
12. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)

## 検証可能な成果物

- AI 成熟度アンケートとスコアリング結果
- 企業属性とデプロイ方式の調査
- L1-L5 講座修了 evidence
- OpenWebUI アカウント / グループ / 権限表、各個人チャットエリアの有効化ログ
- Skill Library と Antigravity / Claude Code / Codex artifacts
- n8n Workflow PoC、Execution Log、Data Tables、Sub-workflow Library
- Hermes Agent タスクカード、Wiki、ingest/query/update ログ、briefing、Gate 4A-4E
- ClawTeam Agent Team 役割カード、協働ログ、成果文書
- Stage Gate 検収記録
- AI トランスフォーメーション診断レポート
- 30 / 60 / 90 日ロードマップ

## 参考資料

- [`90_References/@AI-MD-PUBIC.pdf`](90_References/@AI-MD-PUBIC.pdf)
- [`90_References/MD-Map.png`](90_References/MD-Map.png)
- [`90_References/Metholodgy.png`](90_References/Metholodgy.png)
- [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md)
- [`90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

## 謝辞

特に **Prof. Michael Rosemann** へ感謝します（Queensland University of Technology (QUT), Brisbane, オーストラリア）。  
プロフィール: <https://www.qut.edu.au/about/our-people/academic-profiles/m.rosemann>

本リポジトリのコンサルティング方法論全体の理論的基礎は、著者が QUT で学んだ期間と Prof. Michael Rosemann による **Business Process Management (BPM)**、**Capability Maturity Models**、**企業イノベーション方法論** における長期にわたる啓発と指導から来ています。

特に影響を受けた 2 つのコア設計:

- **8 段階コンサルティング構造**: 企業プロセス診断、能力評価、トランスフォーメーション経路設計、ガバナンス実装に対応。
- **L1-L5 AI 成熟度モデル**: Capability Maturity モデルの階層論理を参照し、企業 AI 導入のための 5 階層フレームワークとしてローカライズ。

免責事項: 本方法論におけるあらゆる誤り、欠落、ローカライゼーション調整、AI 領域への拡張応用は、すべて著者 Tiger AI Morris Lu 盧業興 個人の責任であり、Prof. Michael Rosemann あるいは QUT の見解や立場を代表するものではありません。

## ライセンスと帰属

本プロジェクトは **[Apache License 2.0](LICENSE)** で公開されています。自由に使用・複製・改変・派生・複製・配布・教育・コンサル納品・商用利用が可能です。

再配布、派生、商用パッケージ化、講座資料、コンサル納品文書、製品文書への利用時は、Apache 2.0 ライセンス文と [`NOTICE`](NOTICE) の以下の帰属を保持してください:

```text
Original Author: Tiger AI Morris Lu 盧業興
Role: n8n Taipei Ambassador / PhD Student, Graduate Institute of Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australia
Source: https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit
```

第三者のプラットフォーム名、商標、ビデオ、外部プロジェクト、引用内容は各権利者に帰属します。本リポジトリは第三者データを学習記録、引用、整理、講座設計の参考としてのみ使用しています。

---

## この本を生かす：AI と一緒に読む

下記のインストールガイドはリポジトリを AI IDE に接続する手順を案内します。始める前に、操作モデルとレッドラインを 1 本理解しておきましょう。

**操作モデル一言で**: `git clone` または zip ダウンロード → AI IDE（Antigravity / Claude Code / Codex 等）で開く → AI が [`AGENTS.md`](AGENTS.md)（および各エンジン独自の `<ENGINE>.md`）を自動で読み、自身を **本方法論の共読チューター** として位置づける。その後（1）方法論について何でも質問、（2）方法論をあなたの会社の状況に当てはめてもらう、（3）L1-L5 自己診断を一緒に行い次のステップを見つける、が可能。

完全な議論は [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) を参照。

> ⚠️ **学術誠実性声明 / Academic Integrity Disclaimer**
>
> **本リポジトリ内のすべての具名ケース（Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 個の SAMPLE_CLIENT_CASE）とすべての主人公（例：「Ming」/「MingChang Packaging」）は、AI が生成した架空事例**であり、実際の顧客データではありません。
> すべての数字（時間、ROI、人月、予算、KPI）は **例示のみ** であり、**対外宣伝、契約上の約束、学術的実証エビデンスとして使用してはなりません**。
> 実際の longitudinal ケースは [`90_References/PILOT_STUDY_PROTOCOL_EN.md`](90_References/PILOT_STUDY_PROTOCOL_EN.md) に従う 18-24 ヶ月の実証研究完了後に置き換えられます。
>
> **All named cases and story protagonists in this repo are AI-generated fictional examples**, NOT real client data.

## 🚀 3 つの AI エンジンのインストールと起動ガイド / Three AI Engines Setup Guide

3 つのエンジンの **役割と分業** は上の「🔱 3 つの AI エンジン、それぞれ得意分野が違う」で紹介済みです。このセクションでは **インストール方法、起動方法、ワークフローの呼び出し方** に焦点を当てます。3 つのサブセクションは独立 — 使いたいエンジンを選んでそのセクションだけ読んでください。

> ⚠️ **[`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0 に従い**: 方法論アーキテクチャ、L1-L5、8 段階、3 エンジンの分業など戦略設計はすべて **Morris Lu（人間）** が提案。3 つの AI エンジンは Morris の指導の下で **実行・補完・展開・監査** し、方法論アーキテクチャの所有権を主張しません。各エンジンの詳細な自己記述は [`07_AI_Contributions/`](07_AI_Contributions/) の対応ファイルを参照。

---

### 🟦 1. Antigravity ユーザー — 最前線インタラクティブコンサルタント

> この「静的な生きている本」を直接あなたの「**Conversational Consulting App**」へアップグレード。

**インストールと利用ステップ:**

1. **プロジェクトをロード**: `git clone` または zip をローカルへダウンロード
2. **IDE を起動**: Antigravity でプロジェクトフォルダを開く
3. **自動初期化**: Antigravity が [`ANTIGRAVITY.md`](ANTIGRAVITY.md) と [`SKILL.md`](SKILL.md) を自動で読み、「**共読チューター**」として位置づけ
4. **ワークフロー（Slash Commands）実行**: チャット欄にコマンドを入力してインタラクション開始

**よく使う Antigravity コマンド:**

- `/diagnose` ── リアルな会話を開始し、あなた（または顧客）を L1-L5 企業 AI 成熟度診断へ導く
- `/generate-report` ── 過去の診断と議論結果を標準コンサルレポートテンプレートへ書き込み、草案を生成

詳細は [`.agent/workflows/`](.agent/workflows/) と [`07_AI_Contributions/ANTIGRAVITY.md`](07_AI_Contributions/ANTIGRAVITY.md)。

> Antigravity のコア価値：方法論を**顧客に理解でき、即座にインタラクション可能**なコンサル体験へ変える。

---

### 🟪 2. Codex ユーザー — 方法論エンジニアリングエンジン

> 本リポジトリを「**方法論エンジニアリングワークスペース**」と見なし、この AI-native living book を **テスト可能・監査可能・追跡可能・修復可能・リリース可能** な方法論プロダクトとして維持。

**インストールと利用ステップ:**

1. **プロジェクトをロード**: `git clone` または zip をローカルへダウンロード
2. **Codex を起動**: Codex でプロジェクトフォルダを開く
3. **Codex エントリファイルを読む**: Codex に [`CODEX.md`](CODEX.md) と [`.codex/README.md`](.codex/README.md) を先に読ませる
4. **Codex ワークフロー実行**: チャットでワークフロー名を入力、または対応ファイルに従うよう Codex に明示

**よく使う Codex コマンド（10 個）:**

| カテゴリ | コマンド | 用途 |
| --- | --- | --- |
| Production | `/diagnose` | インタラクティブ AI 成熟度 初期判定 |
| Production | `/generate-report` | コンサル診断レポート草案 |
| Quality | `/evidence-audit` | レポートの evidence chain チェック |
| Quality | `/consistency-review` | 文書横断で L1-L5, Stage Gate, HITL, Evidence の整合性チェック |
| Evolution | `/academic-upgrade` | 学術提言を方法論修復案へ変換 |
| Evolution | `/harvest-insights` | 複数納品レポートから共通 insight を収穫 |
| Defense | `/test-methodology` | 方法論を極端シナリオで stress test |
| Defense | `/red-team-review` | コンサルレポート草案の red-team review |
| Audit | `/generate-traceability` | questionnaire → maturity → evidence → report のトレーサビリティマトリクスを生成 |
| DevOps | `/bump-version` | セマンティックバージョン bump と CHANGELOG 提案 |

**推奨呼び出し方:**

```text
.codex/workflows/evidence-audit.md に従い、このコンサルレポート草案を確認してください。
```

詳細は [`.codex/workflows/`](.codex/workflows/) と [`07_AI_Contributions/CODEX.md`](07_AI_Contributions/CODEX.md)。

> Codex のコア価値：本方法論に「**テスト可能・監査可能・追跡可能・修復可能・リリース可能**」なエンジニアリングライフサイクルを与える。

---

### 🟨 3. Claude Code ユーザー — クロスファイル戦略思考と実験エンジン

> 方法論を **演じる / 試す / 解体する / 衝突させる** 一度。Claude Code の 1M context + マルチペルソナ並行 + 領域横断抽象推論を活用し、**シミュレーション、実験、ディベート、Fork**。

**インストールと利用ステップ:**

1. **プロジェクトをロード**: `git clone` または zip をローカルへダウンロード
2. **Claude Code を起動**: Claude Code CLI / IDE でプロジェクトフォルダを開く
3. **Claude Code エントリファイルを読む**: Claude Code に [`CLAUDE.md`](CLAUDE.md) と [`.claude/README.md`](.claude/README.md) を先に読ませる
4. **Claude Code ワークフロー実行**: チャットでワークフロー名を入力

**よく使う Claude Code コマンド（10 個）:**

| カテゴリ | コマンド | 用途 |
| --- | --- | --- |
| Tier 1 Tactical | `/deep-synthesize` | マルチファイル深層統合（1M context）|
| Tier 1 Tactical | `/theory-bridge` | 顧客状況 ↔ 7 大理論支柱の対応 |
| Tier 1 Tactical | `/scenario-planning` | 制約から 3 つの対比ロードマップ + trade-off を生成 |
| Tier 1 Tactical | `/socratic-challenge` | ソクラテス式の問いで利用者の思考を磨く |
| Tier 1 Tactical | `/cross-stage-trace` | 単一変更の downstream 影響を追跡 |
| Tier 2 Original | `/simulate-engagement` | 30 分で 6 週間コンサル案件を完走（12+ deliverable）|
| Tier 2 Original | `/parallel-perspectives` | 6 ステークホルダー **同時** に同一判断へ意見 + コンフリクトマップ |
| Tier 2 Original | `/thought-experiment` | 方法論の counterfactual stress test（「EU AI Act が L4 を違法にしたら？」）|
| Tier 2 Original | `/devil-pair-debate` | Two-Claude のリアルディベート + 裁判官の総合 |
| Tier 2 Original | `/methodology-fork` | 標準方法論を顧客特化版へ Fork（Methodology-as-Code）|

**推奨呼び出し方:**

```text
.claude/workflows/simulate-engagement.md に従い、500 名規模の製造業顧客向けの
6 週間コンサル案件をシミュレーションしてください。
```

詳細は [`.claude/workflows/`](.claude/workflows/) と [`07_AI_Contributions/CLAUDE_CODE.md`](07_AI_Contributions/CLAUDE_CODE.md)。

> Claude Code のコア価値：方法論を「**標準**」から「**標準 + N 個の派生版 + 完全シミュレーション + 多視点ディベート**」へ進化させる、実験可能な生きている本。

---

### 3 エンジン協働の提案 / Three-Engine Workflow Suggestions

実務で頻出する協働リズム:

```text
Phase A 顧客診断
  → Antigravity が /diagnose で現状を収集
  → Claude Code が /theory-bridge で理論診断を対応
  → Antigravity が /generate-report で中間レポート草案
  → Codex が /evidence-audit で evidence chain を監査
  → Codex が /consistency-review でクロスファイル整合

Phase B 戦略設計
  → Claude Code が /scenario-planning で 3 つのロードマップ
  → Claude Code が /parallel-perspectives で 6 ステークホルダー視点
  → Codex が /red-team-review で過剰楽観を攻撃
  → Claude Code が /devil-pair-debate で価値観前提を議論

Phase C 導入と進化
  → Codex が /generate-traceability で四半期監査
  → Claude Code が /thought-experiment で counterfactual stress test
  → Codex が /bump-version で方法論バージョン管理
  → Claude Code が /methodology-fork で大型顧客向け派生版作成
```

> 3 エンジンのワークフローは排他的ではなく — **要点は各エンジンが最も得意なことをすること**、人間（コンサル / Client Owner / Sponsor）がエンジン切替のタイミングを判断します。
