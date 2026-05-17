# mckinsey-consultant-skills — 引用 & ライセンス通知

> 🌐 言語：[繁體中文](MCKINSEY_SKILLS_REFERENCE.md) ｜ [English](MCKINSEY_SKILLS_REFERENCE_EN.md) ｜ [Deutsch](MCKINSEY_SKILLS_REFERENCE_DE.md) ｜ [Français](MCKINSEY_SKILLS_REFERENCE_FR.md) ｜ [Español](MCKINSEY_SKILLS_REFERENCE_ES.md) ｜ 日本語 ｜ [한국어](MCKINSEY_SKILLS_REFERENCE_KR.md)

本方法論の [`03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) のプロダクションワークフローは **Kafurtan/mckinsey-consultant-skills** に基づいて参照および書き直し。本ドキュメントは上流ソース、ライセンス条件、引用ガイダンス、適応範囲を記録。

---

## 1. 上流プロジェクト

| フィールド | 値 |
| --- | --- |
| **プロジェクト** | mckinsey-consultant-skills（V3.1）|
| **メンテナー** | @Kafurtan |
| **GitHub URL** | <https://github.com/Kafurtan/mckinsey-consultant-skills> |
| **ライセンス** | **MIT License** |
| **形式** | AI agent skill（`SKILL.md` + `references/`）|
| **コンテンツ** | 「ビジネス問題 → McKinsey スタイルプレゼン」を自動化する 8 ステップワークフロー、エンドツーエンドで 90-110 分 |

## 2. mckinsey-consultant-skills とは

McKinsey の Problem Solving 方法論を **8 ステップワークフロー** にシステム化、AI アシスタントがビジネス問題をプロフェッショナルなプレゼンテーション（PPT + Excel evidence trail）へ変換できるようにする。

### 構造的特徴

- **8 ステップワークフロー**：境界定義 → Issue Tree + 仮説 → Dummy Pages + デザイン仕様 → ページごとの反復生産 → PPT + Excel → オプションの Word レポート → 反復改訂。
- **Dummy Page**：リサーチ前に wireframe 仕様を構築、無目的なデータ収集を避け、会話間のレジュームをサポート。
- **依存関係認識**：ページに依存関係ステータスをタグ付け、生産順序を決定（executive summary は最後）。
- **7 ページレイアウト**：タイトル + シングルチャート / 2 カラム / 2×2 マトリクス / テーブル / waterfall chart / タイムライン / インサイトサマリー。
- **Excel evidence trail**：ページごとの raw data + URL + クリーニングプロセス。
- **Progressive disclosure**：reference ファイルは必要なステップでのみロード、その後リリース、~70% コンテキスト節約。
- `references/`：methodology.md、layouts.md、design-specs.md、examples.md、troubleshooting.md。

## 3. 何を適応し引用したか

| 範囲 | 取り扱い |
| --- | --- |
| **8 ステッププロダクションワークフロー** | ワークフロー参照、本方法論の言語で書き直し、8 段階コンサルティング構造にマップ |
| **Dummy Page 概念** | 「skeleton-first, fill-in-later」規律を本方法論デッキアウトラインのページごと仕様に適応 |
| **依存関係認識** | ページ依存管理概念を適応 |
| **7 ページレイアウト** | レイアウトリスト参照、`VISUAL_ASSETS_SPEC.md` 拡張のため書き直し |
| **Excel evidence trail、progressive disclosure** | 概念を適応、本方法論の Evidence 規律と AI-IDE Context Management にマップ |
| **McKinsey Problem Solving、MECE、Pyramid Principle** | パブリックドメイン経営知識、本プロジェクトに専有でない |
| **オリジナルの `SKILL.md` と `references/` ファイル** | **再現せず、フォークもしない**；本方法論は独立した書き直し |

## 4. ライセンスサマリー

mckinsey-consultant-skills は **MIT License** でリリース、プロプライエタリ製品の一部として含むことを含め、自由な使用、修正、再配布、商用使用を許可；唯一の条件はソース再配布時に MIT 著作権表示とライセンステキストを保持すること。

本方法論はソースコードを**再配布しない** — ワークフローとデザインパターンを参照後、独立して `REPORT_PRODUCTION_WORKFLOW.md` を書き直した。書き直されたファイルは本 repo の Apache 2.0 下；それでも、オリジナル著者の貢献への敬意として、そのファイルとここに**引用ソースを明示的に記載**。

## 5. 学習者向け引用フォーマット

> mckinsey-consultant-skills by @Kafurtan から適応されたプロダクションワークフロー — <https://github.com/Kafurtan/mckinsey-consultant-skills>（MIT License）

## 6. 免責事項

本方法論における mckinsey-consultant-skills の引用、適応、8 段階マッピングは方法論著者（Morris Lu / Tiger AI 虎智科技）の解釈を表し、@Kafurtan の公式立場を表さない。「McKinsey」 は McKinsey & Company の商標；本方法論は McKinsey & Company と関連や承認はなく、関連する方法論名はパブリックドメイン経営知識への参照としてのみ使用。mckinsey-consultant-skills のワークフローまたは構造が新バージョンで変更される場合、[上流リポジトリ](https://github.com/Kafurtan/mckinsey-consultant-skills) を参照。
