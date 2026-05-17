# ClawTeam 引用 & ライセンス通知

> 🌐 言語：[繁體中文](CLAWTEAM_REFERENCE.md) ｜ [English](CLAWTEAM_REFERENCE_EN.md) ｜ [Deutsch](CLAWTEAM_REFERENCE_DE.md) ｜ [Français](CLAWTEAM_REFERENCE_FR.md) ｜ [Español](CLAWTEAM_REFERENCE_ES.md) ｜ 日本語 ｜ [한국어](CLAWTEAM_REFERENCE_KR.md)

本方法論の **L5 Multi-Agent Organization** コースは **ClawTeam** を実装プラットフォームとして採用。本ドキュメントは上流ソース、ライセンス条件、引用ガイダンス、我々の使用範囲を記録。

---

## 1. 上流プロジェクト

| フィールド | 値 |
| --- | --- |
| **プロジェクト** | ClawTeam |
| **タグライン** | The Evolution of AI Agents: Solo 🤖 → Swarm 🦞🤖🤖🤖 |
| **メンテナー** | HKUDS（HKU Data Science Lab / 香港大學資料科學實驗室）|
| **GitHub URL** | <https://github.com/HKUDS/ClawTeam> |
| **ライセンス** | **MIT License** |
| **執筆時点バージョン** | v0.2 — v0.3（Stabilization → Multi-User + Web UI）|
| **言語** | Python 3.10+ |
| **依存関係** | `tmux`、`git`、任意の CLI Agent（Claude Code / Codex / nanobot / OpenClaw 等）|

## 2. ClawTeam とは

ClawTeam は **マルチエージェント自己組織化チーム用 CLI フレームワーク**：人間が 1 つのハイレベルゴールを発し、Agent Team が自律的に分解、委任、協力、マージ。SDK ではなく、CLI コマンドセット + 共有ファイルシステム + git-worktree 分離 + メッセージング層 — **任意の CLI Agent（Claude Code、Codex、Gemini、…）がそれによってオーケストレーション可能**。

### コアアーキテクチャ

| 層 | コンテンツ |
| --- | --- |
| **Team Management** | ワークスペース & タスクキューを共有する Agents プール |
| **Workspace Isolation** | 各 Agent が独自の git worktree & ブランチで実行 — 競合なし |
| **Task Tracking** | 依存関係チェーンと auto-unblocking 付き Kanban スタイル |
| **Inter-Agent Messaging** | Point-to-Point Inboxes + ブロードキャスト |
| **Transport 層** | デフォルトファイルベース；オプション P2P（ZeroMQ）；Redis はロードマップ |
| **Storage** | 全 JSON が `~/.clawteam/` に；データベースなし、中央サーバーなし |

### コア CLI コマンドカテゴリ

| カテゴリ | キーコマンド |
| --- | --- |
| **Team** | `clawteam team spawn-team`、`status`、`snapshot`、`restore` |
| **Task** | `clawteam task create`、`update`、`list`、`wait`（`--blocked-by` 含む）|
| **Inbox** | `clawteam inbox send`、`broadcast`、`receive`、`peek` |
| **Board** | `clawteam board show`、`live`、`attach`、`gource`、`serve` |
| **Profile** | `clawteam profile wizard`、`test`、`doctor`、`generate-profile` |
| **Context** | `clawteam context inject`、`conflicts`、`log` |
| **Spawn** | `clawteam spawn [backend] [command] --profile ...` |

### 上流からの 3 リファレンスシナリオ

1. **AutoResearch（H100 上の 8 Agents）** — 8 探索 Agents が自律的に 2,430+ 実験を設計；val_bpb が 1.044 → 0.977（+6.4%）向上。
2. **Full-Stack Software Engineering（5 Agents）** — Architect、Backend（OAuth2 + DB）、Frontend（React）、Test/QA — 並列ブランチが自動マージ。
3. **AI Hedge Fund（7 Agents）** — Portfolio Manager + Value/Growth/Technical/Fundamentals/Sentiment Analysts + Risk Manager — シグナルがメッセージング層を通じて収束。

### ロードマップサマリー

- **v0.3** — Config システム、Multi-User（`CLAWTEAM_USER`）、Web UI ダッシュボード、SSHFS / クラウドベースのクロスマシン共有
- **v0.4** — Redis transport（クロスマシンメッセージング）
- **v0.5** — 共有 state 層（NFS または Redis）；`RedisTeamStore` / `RedisTaskStore`
- **v0.6** — アイデンティティ、権限、ネームスペース、トークン認証（分散チーム）
- **v1.0** — 完全な Web UI、リアルタイム WebSocket、マルチチーム概観

---

## 3. ライセンスサマリー

ClawTeam は **MIT License** でリリース。MIT は以下を許可：

- 自由に使用、修正、再配布
- 商用使用
- プロプライエタリ製品の一部として含む

**唯一の条件**：再配布時に、オリジナルの **MIT 著作権表示** と **MIT License テキスト** を保持しなければならない。

> ⚠️ **重要**
> 本 repo は ClawTeam ソースコードを**再配布しない**。L5 コースでそのアーキテクチャ、CLI、デザイン原則を**引用と教育**のみ、学習者には**上流から自身でインストール**するよう指示（`pip install clawteam`）。コース派生（例：フォーク、配布、カスタマイズ）が ClawTeam コードを再配布する場合、オリジナル MIT ライセンス表示を含まなければならない。

---

## 4. 本方法論における引用範囲

| 範囲 | 取り扱い |
| --- | --- |
| **アーキテクチャ & デザインコンセプト** | L5 の**主要教育プラットフォーム**として使用；シラバスがその Team / Workspace / Task / Inbox / Transport アーキテクチャを記述 |
| **CLI コマンド** | L5 ハンズオンセッション中に**直接**使用 |
| **3 リファレンスシナリオ** | **インスピレーション**として使用；本方法論は製造、病院、小売エンタープライズシナリオへローカライズ |
| **ソースコード** | **再現せず、フォークもしない**；学習者は上流から `pip install` |
| **ブランド / ロゴ** | コースと本ドキュメントで「ClawTeam」の名前で引用；ロゴ再現なし |

## 5. 学習者向け引用フォーマット

スライド、レポート、PoC、または派生作品で ClawTeam を引用する際、以下のフォーマット使用：

**APA スタイル：**

> HKUDS. (2026). *ClawTeam: Agent Swarm Intelligence* (Version 0.2-0.3) [Computer software]. GitHub. https://github.com/HKUDS/ClawTeam

**短縮形：**

> Built on ClawTeam by HKUDS — <https://github.com/HKUDS/ClawTeam>（MIT License）

**学術引用：**

> ClawTeam [Software]. HKUDS, 2026. Available at: https://github.com/HKUDS/ClawTeam. MIT License.

## 6. 謝辞

**HKUDS（HKU Data Science Lab）** が ClawTeam をオープンソース化したことに感謝、これは企業マルチエージェントコラボレーションを研究プロジェクトから教えられる、学べる、デプロイ可能なエンジニアリングプラクティスへ昇華させた。本方法論の L5 コース設計はそのアーキテクチャに深く情報を得て、台湾と中国語圏での企業採用にローカライズされている。

---

## 7. 免責事項

- 本方法論における ClawTeam の記述、適用、またはローカル適応は方法論著者（Morris Lu / Tiger AI 虎智科技）の解釈を表し、HKUDS または ClawTeam メンテナーの公式立場を**表さない**。
- ClawTeam の API、コマンド、またはアーキテクチャが新バージョンで変更される場合、権威ある現在の状態については [上流リポジトリ](https://github.com/HKUDS/ClawTeam) を参照。
- 方法論著者は上流 ClawTeam の変更に合わせて本ドキュメントを更新する権利を留保。
