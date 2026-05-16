# 02 Course Design — L1-L5 講座設計

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 本ディレクトリの位置づけ

本ディレクトリは 3 段階サービスフローの**第 2 段階：Build (Build)** です。診断 (`01`) は「顧客がどのレベル、何が不足」を教える；本ディレクトリは**そのギャップを埋める実際の講座**です。

解決する課題：**AI トランスフォーメーションはツール購入や講演だけでは成功しない — 企業は L1-L5 を一段ずつ歩み、検収可能な資産を生み出さなければならない。** 本ディレクトリは L1 から L5 まで各レベルに完全カリキュラムを設計：講座目標、対象、前提条件、内容、ラボ課題、宿題、完了基準、Stage Gate。各レベルで**検収可能な納品物**（L1 Prompt Library、L2 Skill、L3 Workflow、L4 Agent、L5 Agent Team）を生成 — 「講義後に忘れる」ではない。

本ディレクトリを使う人：講師、AI Champion、IT、各レベル受講者。

## 2. 方法論における位置

| 軸 | 対応 |
| --- | --- |
| 3 段階サービスフロー | **Build** — 第 2 段階 |
| 8 段階コンサル構造 | **Stage 7 To-Be Design**（講座はソリューションの実装） |
| L1-L5 成熟度 | 本ディレクトリは「**顧客を現在のレベルから次のレベルに引き上げる**」講座本体；L1-L5 **両軸**にまたがる |
| Engagement Lifecycle | **Delivery — Build** |

> コア原則 1：**L1-L5 段階接続 — 下位レベルのアウトプットは次レベルの入力。** L1 全員利用なしでは L2 用 Skill 蓄積なし；L2 Skill なしでは L3 Workflow は空管；L3 Workflow なしでは L4 Agent はツールなし；L4 Agent なしでは L5 Team はメンバーなし。**レベル飛び越し禁止。**
>
> コア原則 2：**L1-L5 は 2 軸** — スケール軸（L1 個人 → L2 部門 → L3 部門横断 / 全社、人が AI を監督）と AI 自律軸（L4 AI スーパーアシスタント → L5 AI チーム、AI 自律、人はガバナーに退く）。L3 → L4 が分水嶺。[`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 参照。用語：**Stage Gate = 段階検収関門**、**HITL = Human-in-the-Loop（人間がレビューループ内）**。

## 3. 目標 & 効果

| 目標 | 効果 |
| --- | --- |
| 各レベルに完全で納品可能なカリキュラム | 講師が直接開講可能、設計やり直し不要 |
| クラス内産出が検収可能資産 | 講座成果が組織能力に、「講座後忘却」ではない |
| 各レベルに Stage Gate | パスせず進めない、レベル飛び越し失敗回避 |
| 講座比率を診断スコアで配置 | 顧客リソースをギャップに集中、無駄なし |
| L3/L4 に PoC シナリオ庫 + n8n 骨格 | 実習に既製題と template、ゼロから不要 |

**本ディレクトリ飛ばすと**：顧客がツール買うが能力なし、PoC が永遠に demo 止まり、AI スケール不可。

## 4. ワークフロー & ロジック

```text
01_Assessment 診断 → L レベル + 講座比率推奨
   ↓
COURSE_REQUIREMENTS_AND_COMPANY_PROFILE（前提条件、属性、デプロイ方式確認）
   ↓
COURSE_MODULE_MATRIX（L1-L5 アウトラインと比率配置確認）
   ↓
L1_L5_COMPLETE_COURSE_PLAN（総カリキュラム）+ 各レベル深度カリキュラム：
   L1 OPENWEBUI → L2 ANTIGRAVITY → L3 N8N → L4 HERMES → L5 CLAWTEAM
   ↓ 各レベル
   授業 → ラボ実習（POC_SCENARIO_SPECS / N8N_WORKFLOW_TEMPLATES を題に）
   → 検収可能資産産出 → Stage Gate 通過 → 次レベルへ
```

| ステップ | 誰 | いつ | 入力 | 出力 |
| --- | --- | --- | --- | --- |
| 前提条件確認 | コンサル + 顧客 IT | 開講前 | 診断結果、属性 | 開講前チェックリスト合格 |
| 講座比率配置 | コンサル | 開講前 | L レベル + 比率推奨 | L1-L5 時間配置 |
| 開講（レベル別）| 講師 | Build フェーズ | 各レベル深度カリキュラム | 受講者実習成果 |
| ラボ実習 | 受講者 | 各レベルクラス内 | PoC シナリオ / n8n 骨格 | Prompt/Skill/Workflow/Agent/Team |
| Stage Gate 検収 | コンサル + 顧客マネージャー | 各レベル後 | クラス内産出 | Gate 通過 → 次レベル |

> ロジック：講座は「ツール操作教える」のではなく、「成熟度に沿って検証可能な組織能力を構築」。各レベルは「前半産出、後半次レベルへ接続」構造に従う。

## 5. ファイル説明

### `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md`

L1-L5 講座要件リストと企業属性調査。各レベルの開講前提条件、企業基本データ、データ・リスク属性、システム棚卸し、クラウド AI / Hybrid / フルオンプレ 3 つのデプロイ方式の適用条件と講座注記を定義。開講前に「顧客準備できているか」を確認。

### `COURSE_MODULE_MATRIX.md`

L1-L5 講座モジュールマトリクス。各レベルの目標、ラボ、宿題出力、講座パッケージ（半日体験 / 1 日ワークショップ / 2 日導入合宿 / コンサル診断プロジェクト）、成熟度別比率推奨ルールを一覧表示。

### `L1_L5_COMPLETE_COURSE_PLAN.md`

L1-L5 完全開講総企画。各レベルの目標、内容、ラボ、宿題、完了基準と Stage Gate 総綱要約。各レベル深度カリキュラムは下記 5 ファイル参照。

### `L1_OPENWEBUI_COURSE_PLAN.md`

L1 Controlled AI Access 深度カリキュラム。OpenWebUI 公開 playlist 参照、各人ログイン、個人チャットエリア、Admin Panel、アカウント/役割/グループ/権限、モデル管理、データ規範、ビデオ参考地図含む。

### `L2_ANTIGRAVITY_COURSE_PLAN.md`

L2 Knowledge Codification 深度カリキュラム。Google Antigravity 3 codelab 参照、Agentic IDE、App Prototype、Unit Test、GCP Serverless Pipeline、Gate 2A-2E 含む。**§7.6** に「既存 Agent ライブラリ（agency-agents）活用」モジュール。後半は L2→L3 Bridge。

### `L3_N8N_TIGERAI_COURSE_PLAN.md`

L3 Workflow Automation 深度カリキュラム。**§1.1** で L3 を前半（n8n コンセプトと手動構築）と後半（AG + TigerAI-n8n-Skill-Pack 自然言語生成、**§5.5**）に分割。TigerAI チャンネル n8n / OpenGenie ビデオ参照、Gemini、マルチモーダル、Sub-workflow、Data Tables、Webhook、GitHub Backup、Gate 3A-3G 含む。

### `L4_HERMES_AGENT_COURSE_PLAN.md`

L4 Autonomous Agent 深度カリキュラム。**§2** は「Knowledge-grade Agent 7 大設計原則」（昼軽夜重、知識複利クローズドループ、P1>P2、書読同源、ツール/LLM 分担、Failure-mode 駆動学習、なぜ RAG だけではないか）。マスター + 専門 Skill 組み合わせ、Wiki メモリ、ingest/query/update、Gate 4A-4E 含む。**本講座は概念のみ取得、内部コードは含まない。**

### `L5_CLAWTEAM_COURSE_PLAN.md`

L5 Multi-Agent Organization 深度カリキュラム。HKUDS/ClawTeam（MIT）を実装プラットフォームに、Team/Workspace/Task/Inbox/Transport 5 層アーキテクチャ、git worktree、CLI ハンズオン、3 大ローカライズシナリオ、Gate 5 含む。

### `POC_SCENARIO_SPECS.md`

L3/L4 講座用 PoC シナリオ庫。7 カテゴリ全 35 個の実装可能 PoC（Gmail / Sheets / Notion / CRM / API / ERP + 会計記帳）、各々 trigger、入力、AI step、systems、出力、検収、KPI、人日、n8n ノードシーケンス含む。クラス実習はここから直接題選択。

### `N8N_WORKFLOW_TEMPLATES.md`

PoC を n8n インポート可能 workflow 骨格（JSON）に整理。30 PoC 骨格、エクスポート/インポートフロー、命名バージョン規範、GitHub Backup SOP、クラス使用フロー含む。

### `*_EN.md`

上記ファイルの英語版 sibling。

## 6. 他ディレクトリへの対応

| ディレクトリ | 本ディレクトリとの関係 | データフロー |
| --- | --- | --- |
| `01_Assessment` | 診断の L レベル + 講座比率が講座配置決定 | `01` 比率 → `02` 配置 |
| `00_Overview` | 講座はストーリーの「Build」段階 | `00` ストーリー → `02` 実現 |
| `03_Consulting_Report` | クラス内産出と観察を 8 段階コンサルレポートに記入 | `02` クラス内産出 → `03` レポート |
| `04_Scenarios` | クラスデモ題はケースインデックスから選択；PoC がケースに転化可能 | `04` ケース ↔ `02` 講座題 |
| `06_Delivery` | 講座は engagement lifecycle の Delivery — Build に対応；納品物が納品パッケージ検収へ | `02` 産出 → `06` 検収 |
| `90_References` | 各レベル講座の第三者引用（OpenWebUI / Antigravity / n8n-Skill-Pack / ClawTeam / agency-agents）| `90` 引用 → `02` |

## 7. 共通使用シナリオ

- **講座配置**：診断の講座比率を取る → `COURSE_MODULE_MATRIX.md` で時数配置 → 対応深度カリキュラム開講。
- **L3 開講**：`L3_N8N_TIGERAI_COURSE_PLAN.md` 前半でコンセプト教授、後半で AG+Skill Pack；ラボ題は `POC_SCENARIO_SPECS.md` から、骨格は `N8N_WORKFLOW_TEMPLATES.md` からインポート。
- **受講者がラボ題探す**：自部門と L レベルに応じて `POC_SCENARIO_SPECS.md` または `04_Scenarios/LLM_APPS_CASE_INDEX.md` から選択。
- **検収**：各レベル後に `01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md` と照合し Stage Gate 通過。

---

## ⭐ Cross-Topic Quick References：5 つの核心テーマ、どこで見つけるか

方法論全体には全ディレクトリを貫く 5 つの主動脈があります。本ディレクトリがそれぞれにどう接続するか：

| Cross-Topic | 主要位置 | 本ディレクトリがどう接続するか |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 3 エンジン共読** | Root [`README_JA.md`](../README_JA.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | **L2 Knowledge Codification 講座が 3 エンジンを直接教える** — Antigravity / Codex / Claude Code は L2 受講者のツール；クラス内で 3 エンジン動員し demo + Skill カプセル化 + クロスファイルテスト |
| 🎓 **学術基盤（7 大支柱）** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **L1-L5 5 層アーキテクチャは Capability Maturity（Rosemann/CMMI）に基づく**；レベル飛び越し禁止鉄則は Absorptive Capacity（Cohen & Levinthal 1990）に基づく；L4 Hermes 7 大設計原則は Sociotechnical & Knowledge Compounding に対応 |
| 📚 **L1-L5 講座教育** | [`../02_Course_Design/`](本ディレクトリ) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](L1_L5_COMPLETE_COURSE_PLAN.md) | **本ディレクトリは L1-L5 講座本体** — 5 個独立深度カリキュラム（L1 OPENWEBUI / L2 ANTIGRAVITY / L3 N8N / L4 HERMES / L5 CLAWTEAM）+ COURSE_MODULE_MATRIX 比率配置 + POC_SCENARIO_SPECS 35 実習題 |
| 🔁 **コンサル方案 / 8 段階 + Phase A→B→C クローズドループ** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **クラス内産出が Phase B レポートに入る**（14 章「講座観察」章になる）+ Phase C 四半期レーダー追跡；各レベル Stage Gate がコンサルクローズドループの Gate A/B/C に対応 |
| 📖 **参考資料 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | **L1 → OpenWebUI** ｜ **L2 → Antigravity / Codex / Claude Code + agency-agents** ｜ **L3 → n8n + TigerAI-n8n-Skill-Pack** ｜ **L4 → nousresearch/hermes-agent** ｜ **L5 → HKUDS/ClawTeam**。完全 appreciation cards は [`../90_References/README.md`](../90_References/README.md) §2.1-2.3 参照 |
