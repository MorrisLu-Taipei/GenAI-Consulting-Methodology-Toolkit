# TigerAI-n8n-Skill-Pack 引用 & ライセンス通知

> 🌐 言語：[繁體中文](N8N_SKILL_PACK_REFERENCE.md) ｜ [English](N8N_SKILL_PACK_REFERENCE_EN.md) ｜ [Deutsch](N8N_SKILL_PACK_REFERENCE_DE.md) ｜ [Français](N8N_SKILL_PACK_REFERENCE_FR.md) ｜ [Español](N8N_SKILL_PACK_REFERENCE_ES.md) ｜ 日本語 ｜ [한국어](N8N_SKILL_PACK_REFERENCE_KR.md)

本方法論の **L3 Workflow Automation** コース後半は「Antigravity で自然言語から n8n ワークフローを生成する」教育プラットフォームとして **TigerAI-n8n-Skill-Pack** を引用。本ドキュメントは上流ソース、ライセンス条件、引用ガイダンス、使用範囲を記録。

---

## 1. 上流プロジェクト

| フィールド | 値 |
| --- | --- |
| **プロジェクト** | TigerAI-n8n-Skill-Pack |
| **メンテナー** | Morris Lu（盧業興）— n8n Taipei Ambassador |
| **GitHub URL** | <https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack> |
| **ライセンス** | 混合：Skills / Cookbook / Specs は **TigerAI Proprietary**；`skills/_vendor/` は **MIT**（czlonkowski/n8n-skills より）；`reference-workflows/` は **MIT**（Zie619/n8n-workflows より、secrets はスクラブ済み）|
| **規模** | 13 Skills（7 vendor + 6 custom）、8 cookbook レシピ、2,061 reference workflows、DSL v1.2 spec、3 フラッグシップ例 |
| **サポートツール** | Antigravity（ネイティブ agentic オーケストレーション）、Claude Code（CLI / VS Code）、n8n（2.10.3+）、任意の AI アシスタント（cookbook few-shot prompting 経由）|

> **注：** これは方法論著者 Morris Lu 自身のプロジェクト；引用に第三者ライセンス障害なし、しかし `_vendor/` と `reference-workflows/` の MIT ソースは著作権表示を保持しなければならない（上流 `THIRD_PARTY_NOTICES.md` 参照）。

## 2. TigerAI-n8n-Skill-Pack とは

手動 node 設定ではなく**自然言語記述**から企業グレード n8n ワークフローを生成可能にする。システムは「sticky-note」プレーン言語意図を完全、文書化されたデプロイ準備完了 workflow JSON へ変換。

### 3 層構造

`黄色 sticky-note 意図` + `青色 sticky-note ノート` + `workflow nodes` — ユーザーが意図を書く → AI が 3 層 JSON を生成 → n8n API 経由でデプロイ。

### 3 使用モード

1. **Cookbook コピー** — 8 つの事前構築されたレシピテンプレートから選択
2. **Q&A モード** — AI がユーザーを要件収集に導く
3. **Example finder** — 2,061 reference workflows 中で類似実装を発見

### インストール

`bash install.sh`（Unix）または `install.ps1`（Windows）。

## 3. なぜ L3 後半に属するか

L3 コースは「コンセプト先、生成後」原則で半分に分割：

- **L3 前半**（§5.1 Foundation + §5.2 Builder）：学習者は Trigger / Node / AI / Human Gate / Error Handling を**手作りで構築**、ワークフロー構造とガバナンスを理解。
- **L3 後半**（§5.5）：その基盤上で、Antigravity + TigerAI-n8n-Skill-Pack を使って自然言語意図から直接 workflow JSON を生成、生成結果を**レビュー**することを学ぶ。

> **コア原則：Skill Pack はアクセラレーターであり、理解の代替ではない。** 前半で手作りでワークフローを構築せずに、学習者は生成結果が正しい、安全、保守可能かを判断できない。

対応コース：[`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) §1.1、§5.5。

## 4. ライセンスサマリー

| 部分 | ライセンス | 義務 |
| --- | --- | --- |
| `skills/`（custom）、`cookbook/`、`spec/` | TigerAI Proprietary | 著者 Morris Lu によりライセンス；本方法論内での使用に障害なし；外部再配布には著者の同意を取得 |
| `skills/_vendor/` | MIT（czlonkowski/n8n-skills）| MIT 著作権表示を保持 |
| `reference-workflows/` | MIT（Zie619/n8n-workflows）| MIT 著作権表示を保持；secrets はスクラブ済みだが自分でも検証 |

> ⚠️ **重要**
> 本 repo は TigerAI-n8n-Skill-Pack ソースを**再配布しない**。L3 コースでその構造と使用法を**引用と教育**のみ、学習者には**上流から自身でインストール**するよう指示。Skill Pack を使って学習者が生成したワークフローは企業に属する。

## 5. 引用範囲

| 範囲 | 取り扱い |
| --- | --- |
| **教育プラットフォームとして** | L3 後半（§5.5）の主要実装プラットフォーム |
| **ソース / Skills** | **再現せず、フォークもしない**；学習者は `install.sh` / `install.ps1` 経由で自分でインストール |
| **reference-workflows** | 「Example finder」レッスンで引用；学習者は残留 secrets / 内部 endpoint がないことを確認しなければならない |
| **生成出力** | 生成された workflow JSON は企業資産；企業グレード PoC としてカウントされるには Gates 3A-3G を通過しなければならない |

## 6. 学習者向け引用フォーマット

> Built with TigerAI-n8n-Skill-Pack by Morris Lu — <https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack>

## 7. 免責事項

TigerAI-n8n-Skill-Pack は方法論著者 Morris Lu 自身のプロジェクト。Skills、cookbook、DSL spec、インストールが新バージョンで変更される場合、[上流リポジトリ](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack) と `THIRD_PARTY_NOTICES.md` を参照。AI 生成ワークフローは常に人間レビューと Gate 3 Acceptance を経なければならない — 生成は Acceptance ではない。
