# consultant Frameworks — 引用 & ライセンス通知

> 🌐 言語：[繁體中文](CONSULTANT_FRAMEWORKS_REFERENCE.md) ｜ [English](CONSULTANT_FRAMEWORKS_REFERENCE_EN.md) ｜ [Deutsch](CONSULTANT_FRAMEWORKS_REFERENCE_DE.md) ｜ [Français](CONSULTANT_FRAMEWORKS_REFERENCE_FR.md) ｜ [Español](CONSULTANT_FRAMEWORKS_REFERENCE_ES.md) ｜ 日本語 ｜ [한국어](CONSULTANT_FRAMEWORKS_REFERENCE_KR.md)

本方法論の [`03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) のフレームワークリストと分類は **yoichiojima-2/consultant** に基づいて参照および書き直し。本ドキュメントは上流ソース、ライセンス条件、引用ガイダンス、適応範囲を記録。

---

## 1. 上流プロジェクト

| フィールド | 値 |
| --- | --- |
| **プロジェクト** | consultant |
| **メンテナー** | @yoichiojima-2 |
| **GitHub URL** | <https://github.com/yoichiojima-2/consultant> |
| **ライセンス** | **MIT License** |
| **形式** | Claude Code プラグイン（`/plugin marketplace add` 経由でインストール）|
| **コンテンツ** | 7 カテゴリにわたる 50+ 古典的コンサルティングフレームワーク（McKinsey / BCG / Bain / Accenture）、markdown skill としてパッケージ化 |

## 2. consultant とは

consultant は **Claude Code プラグイン**、50+ 古典的経営コンサルティングフレームワーク（MECE、Pyramid Principle、Porter's 5 Forces、SWOT、BCG Matrix、PESTEL、5 Whys、Fishbone、Business Model Canvas、WBS、RACI、Kotter、OKR、NPV/IRR、Lean、Six Sigma 等）を markdown skill にパッケージ化。

### 構造的特徴

- **7 カテゴリ分類**：problem solving / strategy analysis / case frameworks / business design / project & change / financial analysis / operations。
- **トリガー認識**：自然言語の「私は…が必要」文をフレームワーク組み合わせへルーティング。
- **フレームワーク組み合わせ**：事前構築されたマルチフレームワークチェーン（例：PESTEL → 5 Forces → 3C → SWOT → Issue Tree）。
- **フレームワークごとの標準構造**：起源 / コアコンセプト / ステップ / 適用方法 / 実例 / よくある落とし穴。

## 3. 何を適応し引用したか

| 範囲 | 取り扱い |
| --- | --- |
| **フレームワークリストと 7 カテゴリ分類** | 分類を参照、本方法論の言語で書き直し |
| **「フレームワークセレクター」概念**（自然言語 → フレームワーク） | トリガー認識パターンを本方法論シナリオに整合するセレクターへ適応 |
| **「フレームワーク組み合わせチェーン」概念** | 組み合わせチェーンパターンを適応、本方法論の 8 段階にマップ |
| **フレームワークごとの展開フォーマット** | フレームワークごとの構造を参照、「maps-to-stage」列を追加 |
| **古典的フレームワーク自体**（MECE、Porter's 5 Forces 等） | パブリックドメイン経営知識、consultant に専有でない |
| **オリジナルの markdown skill ファイル** | **再現せず、フォークもしない**；本方法論は独立した書き直し |

## 4. ライセンスサマリー

consultant は **MIT License** でリリース、プロプライエタリ製品の一部として含むことを含め、自由な使用、修正、再配布、商用使用を許可；唯一の条件はソース再配布時に MIT 著作権表示とライセンステキストを保持すること。

本方法論は consultant のソースコードを**再配布しない** — consultant のフレームワークリストとデザインパターンを参照後、独立して `CONSULTING_FRAMEWORKS_LIBRARY.md` を書き直した。書き直されたファイルは本 repo の Apache 2.0 下；それでも、オリジナル著者の貢献への敬意として、そのファイルとここに**引用ソースを明示的に記載**。

## 5. 学習者向け引用フォーマット

> consultant by @yoichiojima-2 から適応されたフレームワークライブラリ — <https://github.com/yoichiojima-2/consultant>（MIT License）

## 6. 免責事項

本方法論における consultant の引用、適応、8 段階マッピングは方法論著者（Morris Lu / Tiger AI 虎智科技）の解釈を表し、@yoichiojima-2 の公式立場を表さない。古典的コンサルティングフレームワークの定義と適用については、各フレームワークのオリジナル学術 / 産業ソースを参照。consultant のフレームワークリストまたは構造が新バージョンで変更される場合、[上流リポジトリ](https://github.com/yoichiojima-2/consultant) を参照。
