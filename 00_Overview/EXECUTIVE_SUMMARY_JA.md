# エグゼクティブサマリー：方法論全体を 5 分で（全体像は 10 分で）

> 🌐 中文 / Chinese: [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) ｜ English: [EXECUTIVE_SUMMARY_EN.md](EXECUTIVE_SUMMARY_EN.md)
>
> **5 分版**: §1「1 ページで」+ §2「コアモデル」を読めば十分。
> **10 分版**: §3-§7（生きている本、理論、講座、コンサル、納品、共読、次のステップ）を追加。
> リンクされたファイルは深く知りたいときだけクリック。

---

## 1. 1 ページで：解決する課題

多くの企業が AI 導入で「**いきなりツールに飛びつく**」 — ChatGPT を買い、n8n を試し、Agent を作りたがる。結果：社員が使えない、プロセスがつながらない、データがガバナンスされていない、PoC が検収されない、最終的に経営陣も AI の成熟度を把握できない。

本方法論は「**散在する AI 利用**」を「**再現可能、ガバナンス可能、測定可能、スケール可能な組織能力**」に変えます — **アンケート + 講座 + コンサル**の閉ループで、**個人が AI を使う**段階から**企業が AI チームを保有する**段階まで導きます。

| 要素 | 一言で |
|---|---|
| **診断ツール** | 10 / 25 / 50 問のアンケート → 客観的な L1-L5 ポジション + 6 次元のギャップ |
| **教育パス** | 5 階層の講座（OpenWebUI / Antigravity / n8n / Hermes / ClawTeam）+ BARS スコアキャリブレーション |
| **コンサル構造** | 8 段階（Awareness → Acceptance Test）+ 3 段階契約（A 診断 / B 戦略 / C 導入） |
| **学術基盤** | 7 大理論支柱（Rosemann / Cohen & Levinthal / Teece / Real Options / 等） |
| **担体メディア** | **AI-Native Living Book** — 本当に*生きている*方法論、AI IDE で直接共読可能 |

---

## 2. コアモデル：L1-L5 の 2 軸

L1-L5 は「5 つのツール」ではなく、**2 軸**で結ばれた成熟度の経路:

| 軸 | 範囲 | ドライバ | 階層 | ツール |
|---|---|---|---|---|
| **スケール軸** | L1 → L2 → L3 | **人間**が AI を使い、**人間**が AI を監督 | 個人 → 部門 → 部門横断 / 全社 | OpenWebUI / Antigravity / n8n |
| **AI 自律軸** | L4 → L5 | **AI** が自律稼働；人間は**ガバナー**に後退 | AI エンティティ → AI チーム | Hermes Agent / ClawTeam |

**重要な分水嶺 = L3 → L4**：「人間が仕事を駆動」から「AI が仕事を駆動」へ。L4-L5 でも、**ガバナンスフレームは依然として人間が構築し、人間が監督を保持** — AI が自律するのは「業務執行」であって「ガバナンス意思決定」ではない。

➜ 完全なストーリー：[`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0

---

## 3. AI-Native Living Book — なぜこの本は*生きている*のか

本方法論は PDF / PPT / SOP ではない — **本当に*生きている*本**:

| 世代 | 形態 | 限界 |
|---|---|---|
| 第 1 世代 — 印刷書 | 紙 | **静止** — 読むことしかできず、応答しない |
| 第 2 世代 — インタラクティブブック | Web / Wiki | **インターフェイスは生きてもコンテンツは生きていない** — 自発的に提案しない |
| **第 3 世代 — AI-Native Book**（本リポジトリ）| Markdown + AI IDE | **本当に生きている** — あなたが問い、答え、共に考え、企業の状況に応じて診断 / レポート草稿 / シミュレーションを実行 |

**操作モデル**：`git clone` → AI IDE（Antigravity / Claude Code / Codex）で開く → AI が本全体を自動で読む → 本方法論の**共読チューター**として位置づけ → 直接対話、質問、適用。

➜ 完全な議論：[`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md)

### 3 つの AI エンジン、それぞれ専門が違う

| エンジン | 役割 | 最も得意なこと | ワークフロー |
|---|---|---|---|
| 🟦 **Antigravity** | 最前線コンサル | 顧客との会話、アンケート実行、レポート草稿 | `/diagnose`, `/generate-report` |
| 🟪 **Codex CLI** | 方法論監査員 | クロスファイルテスト、レッドチームレビュー、バージョン管理、修復 | `/evidence-audit`, `/red-team-review`, `/bump-version` ほか 7 件 |
| 🟨 **Claude Code** | クロスファイル思考のパートナー | 深層統合、多視点ディベート、シミュレーション、顧客向け Fork | `/simulate-engagement`, `/devil-pair-debate`, `/methodology-fork` ほか 7 件 |

➜ 三エンジン自己記述：[`../07_AI_Contributions/`](../07_AI_Contributions/) ｜ セットアップガイド：root [`../README_JA.md`](../README_JA.md) §🚀

---

## 4. 学術基盤：7 大理論支柱

本方法論はその場しのぎではない。各キー設計は**古典理論にマッピング** — 学者、規制当局、取締役会が「理論的根拠は？」と問うときの標準回答:

| # | 理論 | 創立者 | 本方法論での役割 |
|---|---|---|---|
| 1 | **Capability Maturity** | Rosemann (QUT) / CMMI | L1-L5 成熟度の学派的基盤 |
| 2 | **Absorptive Capacity** | Cohen & Levinthal (1990) | 一部企業が L1 で止まる理由を説明 — 事前知識の欠如 |
| 3 | **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | Stage 7 To-Be 設計：どのタスクが L4 に到達すべきか、どれが L2 に留まるべきか |
| 4 | **Dynamic Capabilities** | Teece (1997, 2007) | sense / seize / transform — AI ガバナンスが「能力」であって「ポリシー」ではない理由 |
| 5 | **Sociotechnical Systems & Trust in AI** | Bostrom (1977) / Dietvorst (2015) / Glikson (2020) | L4-L5 で HITL を保持しなければならない理由 — 人間は純自律 AI を盲信しない |
| 6 | **Real Options Theory** | Dixit & Pindyck (1994) / McGrath (1997) | Phase 1 で NPV ≈ 0 でも投資価値がある理由 — 拡張オプションを買っている |
| 7 | **Executable Knowledge Artifact** | Knuth (1984) Literate Programming + 現代的拡張 | 本方法論が PDF でなく Markdown + AI IDE 共読である理由 |

➜ 完全な理論議論（引用付き）：[`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md)
➜ 失敗パターン（理論が失敗を予測する場所）：[`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md)
➜ パイロットスタディ設計（18-24 ヶ月の実証計画）：[`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md)

---

## 5. 教育：L1-L5 完全カリキュラム

各レベルには**独自の教材 + 検証可能な納品物 + Stage Gate 検収**:

| レベル | 名称 | ツール | 講座計画 |
|---|---|---|---|
| L1 | Controlled AI Access | OpenWebUI | [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) |
| L3 | Workflow Automation | n8n + Tiger AI Skill Pack | [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) |
| L4 | Autonomous Agent | Hermes Agent + Wiki | [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) |
| L5 | Multi-Agent Organization | ClawTeam | （L5 は [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md) に含む） |

**設計原則**：顧客は L1-L5 をすべて一度に受講する必要はない。アンケートを使って**最も即座に納品可能な成果を生み出せる階層**を見つけ、上に積み上げる。講座のミックスは企業属性、業界、デプロイ方式（クラウド / ハイブリッド / オンプレ）、リスク要件で決定。

➜ 完全な講座パッケージ：[`../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
➜ スコアキャリブレーション（主観を避ける）：[`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) BARS

---

## 6. コンサルティング：8 段階 + 3 段階契約モデル

### 6.1 8 つの段階

| # | 段階 | 主要アクション |
|---|---|---|
| 1 | **Awareness** | AI 認識と顧客ビジョンを確立 |
| 2 | **Reference Model** | 顧客を Ideal Practice レーダー署名に導く |
| 3 | **Discovery** | As-Is 現状、Shadow IT、システム棚卸しを収集 |
| 4 | **Gap Analysis** | Ideal Practice vs As-Is を比較；高影響ギャップを特定 |
| 5 | **Stakeholder Mapping** | Sponsor、AI Champion、HR、Compliance を特定 |
| 6 | **Diagnosis** | クロスレイヤー分析（7 大理論支柱への固定を含む） |
| 7 | **To-Be Design** | TTF / Real Options を使って段階的なロードマップを設計 |
| 8 | **Acceptance Test** | Stage Gate sign-off + 四半期レーダーレビュー |

### 6.2 3 段階契約

| Phase | 期間 | 主要納品物 |
|---|---|---|
| **Phase A — 診断** | 2 週間 | 中間診断レポート + 署名済み Ideal Practice |
| **Phase B — 戦略** | 4 週間 | 完全 14 章コンサルレポート + 24 ヶ月ロードマップ + ROI + ガバナンス提言 |
| **Phase C — 導入** | 24 ヶ月 | 段階的導入 + 四半期レーダーレビュー + 継続的進化 |

➜ 完全な 8 段階ストーリー（対話例付き）：[`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md)
➜ コンサルレポートテンプレート：[`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)
➜ コンサルツールキットテンプレート：[`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md)
➜ 納品パッケージ & 検収：[`../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)

---

## 7. 検証可能な納品物：各レベルが残すもの

各レベルの「講座」は講義が終わって終わりではなく — 監査可能な evidence を残す:

| レベル | 主要納品物 | Evidence |
|---|---|---|
| L1 | 個人チャットエリア、Prompt Library | アカウント表、権限表、ログイン log、Prompt サンプル |
| L2 | Skill Library、Agentic artifacts | Skill 文書、テストケース、バージョン履歴、出力サンプル |
| L3 | n8n Workflow PoC、Sub-workflow Library、Data Tables | 実行 log、再試行 log、システム接続スクリーンショット |
| L4 | 検証可能 Agent、Briefing、task card | Agent log、Wiki バージョン、HITL sign-off log |
| L5 | Agent Team 役割カード、協働フロー、部門横断成果 | Team run log、引継ぎ log、ガバナンス log |
| **コンサルレベル** | 14 章診断レポート、30/60/90 日ロードマップ、ROI、ガバナンス提言 | Stage Gate sign-off log、四半期レーダーレビュー |

➜ 完全な納品物 + evidence マトリクス：[`../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)

---

## 8. この本の使い方（役割別 5 つの入口）

| あなたは | ここから始める（20 分 → 1 時間）|
|---|---|
| **CEO / オーナー / 方法論を把握したい家族** | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) — Ming の物語 |
| **コンサルタント / 受講者** | [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) — 完全 8 段階フロー |
| **取締役会 / 規制 / 学術** | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — 科学的論証 |
| **エンタープライズ IT / 他社からの転職コンサル** | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — McKinsey/BCG/TOGAF/Gartner との整合 |
| **方法論研究者 / AI Pedagogy 学者** | [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) — なぜ新形態の方法論か |

---

## 9. リファレンス クイックインデックス

### 9.1 学術理論 & 失敗モード

- [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — 7 大理論支柱の完全議論
- [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) — 14 個の失敗モード（理論予測）
- [`../90_References/AI_GOVERNANCE_ALIGNMENT.md`](../90_References/AI_GOVERNANCE_ALIGNMENT.md) — NIST AI RMF / EU AI Act / ISO 42001 との整合
- [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) — 18-24 ヶ月実証研究設計

### 9.2 教育 & 評価

- [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) — 10/25/50 問アンケート（平易な言葉）
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL.md) — スコアリングモデル
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) — BARS スコアキャリブレーション（主観を避ける）
- [`../02_Course_Design/`](../02_Course_Design/) — 完全な L1-L5 講座計画

### 9.3 コンサル納品

- [`../03_Consulting_Report/`](../03_Consulting_Report/) — コンサルレポート + ツールキットテンプレート
- [`../04_Scenarios/`](../04_Scenarios/) — 7 業界シナリオ（製造 / 病院 / マーケティング / B2B / 金融 / 政府 / 教育）
- [`../05_Sales/`](../05_Sales/) — 営業トーキングポイント + FAQ
- [`../06_Delivery/`](../06_Delivery/) — 納品パッケージ + 検収基準 + Engagement Lifecycle

### 9.4 三エンジン自己開示

- [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) — 三エンジン共筆 README + §3 共筆紀律
- [`../07_AI_Contributions/ANTIGRAVITY.md`](../07_AI_Contributions/ANTIGRAVITY.md) ｜ [`CODEX.md`](../07_AI_Contributions/CODEX.md) ｜ [`CLAUDE_CODE.md`](../07_AI_Contributions/CLAUDE_CODE.md)
- [`../CHANGELOG.md`](../CHANGELOG.md) — 三エンジン共筆 changelog

### 9.5 ソース資料

- [`../90_References/@AI-MD-PUBIC.pdf`](../90_References/@AI-MD-PUBIC.pdf) — 元の PDF 方法論
- [`../90_References/MD-Map.png`](../90_References/MD-Map.png) — AI Maturity Map
- [`../90_References/Metholodgy.png`](../90_References/Metholodgy.png) — 8 段階トランスフォーメーションガイド図
- [`../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) — ビデオ学習ノート
- [`../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

---

## 10. 次のステップ：3 つの推奨パス

| あなたのニーズ | 推奨される次のステップ |
|---|---|
| **全体メンタルモデルを構築** | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)（§3.0 2 軸完全ストーリーを含む） |
| **自社がどのレベルか知る** | [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) の 10 問クイック診断 |
| **AI と直接共読** | AI IDE でこのリポジトリを開く → 最初に root [`../README_JA.md`](../README_JA.md) §🚀 3 つの AI エンジンセットアップガイドを読み、エンジンを 1 つ起動 |

---

> ⚠️ **学術誠実性声明**：本リポジトリの具名ケース（Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 個の SAMPLE_CLIENT_CASE ファイル）と主人公（例：「Ming」「MingChang Packaging」）はすべて **AI 生成の架空事例** であり、実際の顧客データではありません。すべての数字（時間、ROI、人月、予算、KPI）は **例示のみ** であり、**対外宣伝、契約上の約束、学術的実証エビデンスとして使用してはなりません**。実際の longitudinal ケースは [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) に記載の 18-24 ヶ月実証研究完了後にのみ置き換えられます。
>
> **アーキテクチャ帰属**：本リポジトリの方法論アーキテクチャは人間の著者 **Morris Lu (Tiger AI)** が設計。3 つの AI エンジン（Antigravity / Codex / Claude Code）は**実行・補完・展開・監査**のツールです。[`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0 参照。
