# agency-agents 引用 & ライセンス通知

> 🌐 言語：[繁體中文](AGENCY_AGENTS_REFERENCE.md) ｜ [English](AGENCY_AGENTS_REFERENCE_EN.md) ｜ [Deutsch](AGENCY_AGENTS_REFERENCE_DE.md) ｜ [Français](AGENCY_AGENTS_REFERENCE_FR.md) ｜ [Español](AGENCY_AGENTS_REFERENCE_ES.md) ｜ 日本語 ｜ [한국어](AGENCY_AGENTS_REFERENCE_KR.md)

本方法論の **L2 Knowledge Codification** コース後半（特に L2-B Agentic Developer トラック）は、「既製の Agent ペルソナライブラリ」モジュールの教材として **agency-agents** を引用。本ドキュメントは上流ソース、ライセンス条件、引用ガイダンス、使用範囲を記録。

---

## 1. 上流プロジェクト

| フィールド | 値 |
| --- | --- |
| **プロジェクト** | agency-agents |
| **メンテナー** | @msitarzewski（コミュニティメンテナンス）|
| **GitHub URL** | <https://github.com/msitarzewski/agency-agents> |
| **ライセンス** | **MIT License** |
| **規模** | 12 部門にわたる 144+ Agent ペルソナ |
| **サポートツール** | Claude Code, GitHub Copilot, Cursor, Aider, Windsurf, OpenCode, Antigravity, Gemini CLI, OpenClaw, Qwen Code, Kimi Code |

## 2. agency-agents とは

agency-agents は **AI Agent ペルソナ定義のコレクション**：各 Agent は ID 特性、コアミッション、技術仕様、ワークフロープロセス、測定可能な成功基準を含む markdown ファイル。一般的なプロンプトテンプレートのセットではなく、「デプロイ可能な仮想スペシャリスト」のロスター。

### 12 部門

`engineering`（25+ Agent：Frontend Developer、Backend Architect、Security Engineer…）、`design`、`marketing`、`sales`、`product`、`project-management`、`testing`、`support`、`finance`、`game-development`、`academic`、`specialized`、`spatial-computing`。

### インストール

`./scripts/install.sh` 経由でインストール、インストール済み AI ツールを自動検出して並列処理。

## 3. なぜ L2 に属するか

L2 Knowledge Codification の核心は「仕事経験を再利用可能な Skills へパッケージ化」。L2-B Agentic Developer トラック後半は重要なアイデアを教える：**すべての Skill がゼロから構築される必要はない**。agency-agents は出発点として 144+ 成熟した Agent ペルソナを提供 — 学習者は車輪を再発明する代わりに、選択、カスタマイズし、企業 Skill Library に組み込む。

対応コース：[`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6。

## 4. ライセンスサマリー

agency-agents は **MIT License** でリリース。MIT は自由な使用、修正、再配布、商用使用を許可、プロプライエタリ製品の一部としてを含む；**唯一の条件**は再配布時にオリジナルの MIT 著作権表示とライセンステキストを保持しなければならない。MIT はエンドユーザーへの可視帰属を厳格に要求しない（ただし著者は感謝されると注記）。

> ⚠️ **重要**
> 本 repo は agency-agents ソースを**再配布しない**。L2 コースでその構造と使用法を**引用と教育**のみ、学習者には**上流から自身でインストール**するよう指示。学習者がカスタマイズした Agent ペルソナは企業に属するが、Skill ドキュメントにオリジナルソース（agency-agents + バージョン）を記載することを推奨。

## 5. 引用範囲

| 範囲 | 取り扱い |
| --- | --- |
| **教材として** | L2-B 後半の「既製 Agent ライブラリ」ケースとして使用；インストール、ブラウズ、選択、カスタマイズを教える |
| **ソース / ペルソナファイル** | **再現せず、フォークもしない**；学習者は `./scripts/install.sh` 経由で自分でインストール |
| **カスタマイズ出力** | カスタマイズされたペルソナは企業 Skill Library エントリになる；ソース帰属推奨 |

## 6. 学習者向け引用フォーマット

> agency-agents by @msitarzewski に基づく — <https://github.com/msitarzewski/agency-agents>（MIT License）

## 7. 免責事項

本方法論における agency-agents の記述、適用、カスタマイズガイダンスは方法論著者（Morris Lu / Tiger AI 虎智科技）の解釈を表し、@msitarzewski または agency-agents コミュニティの公式立場を表さない。agency-agents の構造、インストール、Agent 分類が新バージョンで変更される場合、[上流リポジトリ](https://github.com/msitarzewski/agency-agents) を参照。
