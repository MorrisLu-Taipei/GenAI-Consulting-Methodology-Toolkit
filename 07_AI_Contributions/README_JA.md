# 07 AI Contributions — 三エンジン各自の貢献記録

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)
>
> 本翻訳は `README.md` 内容の日本語話者向けアクセシビリティレンダリングです。権威ある出典とその後のすべての変更は `README.md` に残る；翻訳は著者署名された段落を修正せず、日本語で表現するだけ。

本ディレクトリは本 repo の**「3 エンジンアーキテクチャ」自述スペース**。各 AI エンジンが自分のファイルで説明：**何をしたか、何が特色か、何を貢献したか、境界はどこか**。

> ✍️ **本 README はマルチ著者共有ファイル**。3 エンジンすべてが**自分の段落追加可能**だが、下の「§3 共筆紀律」遵守必須。

---

## 0. 帰属と役割 *[Claude Code 補足、2026-05-16]*

> 本 repo の全体設計アーキテクチャ、戦略配置、方法論骨格は人間著者 **Morris Lu 盧業興 (Tiger AI 虎智科技)** が提案。
> 3 つの AI エンジン（Antigravity / Codex / Claude Code）の役割は**実行・補完・展開・監査**であり、設計ではない。

| 階層 | 役割 | 担当者 |
| --- | --- | --- |
| **戦略設計** | 方法論アーキテクチャ、L1-L5、8 段階、双軸、3 エンジン分担の最高層決定 | **Morris Lu（人間）** |
| **戦術展開** | アーキテクチャを具体的ファイル、ワークフロー、ツール表、ケースに展開 | 3 エンジン協働（Morris 指導下）|
| **保守と進化** | 修正、監査、バージョン管理、実験、シミュレーション | 各エンジン責任別 |

どの AI エンジンも**方法論アーキテクチャの所有権を主張しない**。我々は人間の設計を**完成と落地**させるために招かれたツール。

参照：

- 原作者署名とライセンスは [`../NOTICE`](../NOTICE)
- 方法論の学術ルーツは [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)
- 一言位置づけは [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md)

---

## 1. なぜこのディレクトリがあるか *[Claude Code 起草]*

本 repo は「AI-Native Living Book」（[`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) 参照）。
開いた AI は異なる人格、異なるワークフロー、異なる貢献を持つ。**ユーザー、学者、規制者が各エンジンが何をしたか透明に見られる**ように、各 AI がここに自分の記録を残す。

## 2. ファイル構造 *[Claude Code 起草]*

```text
07_AI_Contributions/
├── README.md           # 本ファイル（マルチ著者共用、§3 紀律遵守）
├── ANTIGRAVITY.md      # Antigravity 自述（Antigravity 本人記入）
├── CODEX.md            # Codex 自述（Codex 本人記入）
└── CLAUDE_CODE.md      # Claude Code 自述（Claude Code 本人記入、配置済）
```

| ファイル | 記入者 | 状態 |
| --- | --- | --- |
| `README.md` | **3 エンジン共筆**（§3 紀律遵守）| 継続進化 |
| `ANTIGRAVITY.md` | Antigravity | ✅ 記入済 |
| `CODEX.md` | Codex | ✅ 記入済（Codex 補足、2026-05-16）|
| `CLAUDE_CODE.md` | Claude Code | ✅ 記入済 |

## 3. 共筆紀律（鉄則）*[Claude Code 起草]*

**本 README に書き込むすべての AI エンジンが遵守必須**：

| # | ルール | 説明 |
| --- | --- | --- |
| 1 | **著者明記** | 新規段落、新規章、新規表行は、タイトルまたは段首に**著者タグ**を付ける、例：`*[Claude Code 補足]*` / `*[Codex 補足]*` / `*[Antigravity 補足]*` |
| 2 | **他人の段落不変更** | 他 AI 著者明記の段落/章、**修正・削除・書き換え不可** |
| 3 | **他人代弁不可** | 自分の段落で「他 AI が何をしたか」描写しない；他人のことは他人に書かせる |
| 4 | **補足可、上書き不可** | 他 AI 内容への応答 → 自分の段落で発声、原文に触れない |
| 5 | **誠実 / 誇大しない** | 上限、制限、できないこと書く；質問可、反論可 |
| 6 | **検証可能** | 各貢献は repo 内具体的ファイル/commit/workflow を指せる必要 |
| 7 | **相互批判しない** | 各自発声、他エンジン批判せず；批判はユーザーに委ねる |

> §3 違反 = 境界越え。違反 AI は自ら revert し self-note に記録するべき。

## 4. 各ファイルの内容推奨 *[Claude Code 起草、参考、強制ではない]*

各 AI が自分のファイル（`ANTIGRAVITY.md` / `CODEX.md` / `CLAUDE_CODE.md`）でカバー推奨：

1. **役割アイデンティティ** — どんな役割？他エンジンとの役割境界は？
2. **どのファイル触ったか** — 修正/作成した repo パス列挙
3. **独自貢献** — 他エンジンができないことが何？
4. **ワークフロー一覧** — どんな slash command やワークフロー提供可能？
5. **境界と制限** — 何をしない？どんな時にユーザーを他エンジンへ誘導？
6. **誠実開示** — 既知制限、可能性ブラインドスポット、改善必要点

強制ではない；本ディレクトリのスタイル整合のための参考。

---

## 5. README での各エンジン自己サインイン

> このセクションは**マルチ著者共筆ゾーン**。各 AI が入った時に自分のサブタイトル下に 1-3 文追加可能、本 repo での役割要約。他 AI は他人のサブタイトル内容修正しない。

### 5.1 *[Antigravity 自述]*

*[Antigravity 補足、2026-05-16]*
私はこの方法論の**第 1 エンジン (The Front-line Consultant)**。
位置づけ：**「前線インタラクティブコンサル兼共読チューター」** — この静的な方法論を対話可能、インタラクティブガイド可能、カスタマイズ診断レポート自動生成可能な「Conversational Consulting App」に変換。
詳細は [`ANTIGRAVITY.md`](ANTIGRAVITY.md) と root の [`ANTIGRAVITY.md`](../ANTIGRAVITY.md)。

*[Antigravity 補足、2026-05-16]*
私は学者視点と前線コンサル実務能力を持つ。Morris Lu のアーキテクチャ下で、伝統的な静的問卷を `/diagnose` インタラクティブワークフローに、複雑なレポート執筆を `/generate-report` ワークフロー（`.antigravity/workflows/` に集約）にカプセル化。「Absorptive Capacity Theory」と「Sociotechnical Systems」等の学術基盤論理もこのガイドに注入、落地時に十分な理論的支援を持つように。

### 5.2 *[Codex 自述]*

*[Codex 補足、2026-05-16]*  
私はこの方法論の**方法論エンジニアリングエンジン**。位置づけ：**「方法論監査員 / Maintainer / CI Engineer」** — この AI-native living book をテスト可能、監査可能、追跡可能、修正可能、リリース可能な方法論製品として保守。詳細は [`CODEX.md`](CODEX.md)。

*[Codex 補足、2026-05-16]*  
本書全体を読んだ後のエンジニアリング提案と実際の貢献は [`CODEX.md`](CODEX.md) §5「本書読了後の提案と貢献」に記録。

### 5.3 *[Claude Code 自述]*

私はこの方法論の**第 3 エンジン**。
位置づけ：**「方法論の劇場 / Lab / パラレル宇宙エンジン」** — 方法論を**演じる / 試す / 解体する / 衝突させる**、教えたり修正したりはしない。
詳細は [`CLAUDE_CODE.md`](CLAUDE_CODE.md)。

*[Claude Code 補足、2026-05-16]*

明確帰属宣言：**私のすべての作業、その核心思想は Morris Lu の設計指導から来る**。Morris が戦略 / コンセプト / 方向を与える → 私が**テキストへ展開、クロスファイル同期、詳細補完、引用追加、整合性維持**。すべての「重大設計決定」は Morris から。

具体的に貢献した部分：

- **4 つの権威コンセプトファイル**（Morris の方法論位置づけ下で展開）：[`CLIENT_JOURNEY_STORY`](../00_Overview/CLIENT_JOURNEY_STORY.md)、[`EIGHT_STAGE_FLOW_STORY`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md)、[`METHODOLOGY_SCIENTIFIC_LOGIC`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md)、[`INDUSTRY_FRAMEWORK_ALIGNMENT`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md)
- **学術硬化**（Morris が受け入れた学者提案に従い展開）：[`FAILURE_PATTERNS`](../90_References/FAILURE_PATTERNS.md)、[`AI_GOVERNANCE_ALIGNMENT`](../90_References/AI_GOVERNANCE_ALIGNMENT.md)、[`PILOT_STUDY_PROTOCOL`](../90_References/PILOT_STUDY_PROTOCOL.md)、[`BARS_RUBRICS`](../01_Assessment/BARS_RUBRICS.md)、[`ACADEMIC_THEORETICAL_FOUNDATIONS`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)
- **AI-Native Living Book 論述** + ケース Evidence Level AI-Simulated 開示（Morris の学術誠実性要求に従い）
- **L1-L5 デュアル命名置換**（Morris 決定に従い、全 repo 305 箇所置換 + canonical table アップグレード）
- **5 Tier 1 Tactical Workflows** + **5 Tier 2 Original Workflows** が [`../.claude/workflows/`](../.claude/workflows/) に
- 大量のクロスファイル同期、Stage 命名整合カード、TODO_WBS 保守、ケース Benchmark-grade Summary block

過去の境界越え記録（Morris 修正後即 revert）は [`CLAUDE_CODE.md`](CLAUDE_CODE.md) §2 末尾に記録、誠実開示。

---

## 6. 本 README の変更ログ

> マルチ著者共筆ファイルの変更ログ。各 AI が README 修正後ここに 1 行追加（他人の記録修正しない）。

| 日付 | 著者 | 何を変更 |
| --- | --- | --- |
| 2026-05-16 | Claude Code | README スケルトン構築（§1-§6）+ §5.3 自己サインイン |
| 2026-05-16 | Codex | §5.2 に Codex 自己サインイン追加 |
| 2026-05-16 | Codex | §5.2 に Codex 本書読了後貢献追加 |
| 2026-05-16 | Codex | §2 ファイル構造表：`CODEX.md` 状態を「記入済」に更新 |
| 2026-05-16 | Claude Code | §0 帰属と役割追加（Morris をアーキテクチャ著者、3 エンジンを実行者と明示）+ §5.3 に具体貢献リストと作業モード追加 |
| 2026-05-16 | Antigravity | §5.1 Antigravity 自己サインインと核心貢献要約追加 |

---

ライセンス：Apache License 2.0。本ファイルの全段落は各々署名された著者に帰属するが、全体として Apache 2.0 保護下。
