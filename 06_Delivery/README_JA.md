# 06 Delivery — 納品検収 & 案件オペレーション

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 本ディレクトリの位置づけ

本ディレクトリは 2 つの層を持ち、合わせて 1 つを解決：**コンサル案件をプロフェッショナルにスケーラブルに「ビジネスにして」「納品する」方法。**

- **納品検収層**：本方案が顧客に何を納品するか、どう検収するか、どの evidence で完了を証明するか定義。
- **案件オペレーション層**：案件ライフサイクル全体（Sales → Delivery → Support）、ロール SOP、商業文書テンプレ、運用チェックリスト、価格設定とリスク管理を定義。

`01`-`03` は「コンサルが何をするか」（方法論）；`05` は「顧客にどう買いたくさせるか」（プリセールス）；本ディレクトリは「**契約後、案件全体をビジネスとして完走、クリーン、再現可能に実行**」。問題：**方法論だけで運用フレームワークがないコンサル会社はスコープクリープに潰され、ハンドオーバー断絶、セキュリティ事故、スケール不可。**

本ディレクトリを使う人：PM、コンサル、Sales（Closer）、Technical Lead、顧客側 Owner。

## 2. 方法論における位置

| 軸 | 対応 |
| --- | --- |
| 3 段階サービスフロー | **Deliver** + 3 段階を「ビジネス」運用フレームに包む |
| 8 段階コンサル構造 | 8 段階の**納品と検収**に対応；案件ライフサイクルは 8 段階の「商業殻」 |
| **3 段階契約モデル（コンサルクローズドループ）** | **Phase A 診断 2W → Phase B 戦略 4W → Phase C 導入 24M + 四半期レーダー回顧** — 案件ライフサイクルの Delivery 段は Phase A→B→C のクローズドループ |
| L1-L5 成熟度 | 納品パッケージ検収が L1-L5 各レベルの納品物カバー |
| Engagement Lifecycle | **本ディレクトリは案件ライフサイクル（Sales → Delivery → Support）本体** |

> 🔁 **案件ライフサイクル ↔ コンサルクローズドループ**：本ディレクトリの「Delivery 段」は **6 週マラソンではなく**、[`../03_Consulting_Report/README.md`](../03_Consulting_Report/README.md) §4 と [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 が描く**クローズドループ**：Phase A 中間レポート署名 → Gate A → Phase B 完全レポート → Gate B → Phase C 24 ヶ月実装 + **四半期レーダー回顧**（科学管理の反証メカニズム）。Support 段は Phase C 後の Retainer / Maintenance に対応。

## 3. 目標 & 効果

| 目標 | 効果 |
| --- | --- |
| 明確な納品パッケージと検収基準 | 顧客とコンサル「終わったか」で合意、争いなし |
| 完全な案件ライフサイクル | リードから結案まで SOP、個人手芸に頼らない |
| ロール SOP | スケール可能（一人ですべてではない）、ハンドオーバー断絶なし |
| 商業文書テンプレ | SOW/契約/請求書/変更指令書既製、毎回書き直しなし |
| 運用チェックリスト | pre-project/security/QA/handover/offboarding 漏れなし |
| 価格設定とリスクフレームワーク | スコープクリープでマージン食われない、いつ「ノー」と言うか分かる |

**本ディレクトリ飛ばすと**：方法論強くてもビジネス大きくならない — スコープクリープ、徒労、ハンドオーバー断絶、セキュリティ事故、キーパーソン依存、貸倒。

## 4. ワークフロー & ロジック

```text
案件ライフサイクル（ENGAGEMENT_LIFECYCLE）：
  Sales（Lead → Discovery → Proposal → Contract）
     → BUSINESS_DOCUMENT_TEMPLATES 使用（提案、SOW）
     → PRICING_AND_RISK 使用（価格設定、リスク登録）
  Delivery（Kickoff → Build → Test → Security → Handover）
     → DELIVERY_CHECKLISTS 使用（pre-project / security / QA / handover）
     → DELIVERY_PACKAGE_AND_ACCEPTANCE 使用（パッケージ検収）
     → DELIVERY_ROLE_SOPS 使用（誰がどの段階責任）
  Support（Retainer → Maintenance → Offboarding）
     → DELIVERY_CHECKLISTS 使用（offboarding）
全工程：7 Pillars を基本原則として
```

| ステップ | 誰 | いつ | 入力 | 出力 |
| --- | --- | --- | --- | --- |
| ライフサイクル実行 | PM | 案件全工程 | `ENGAGEMENT_LIFECYCLE` | 各段階推進 |
| 商業文書作成 | Closer / PM | Sales / 変更時 | `BUSINESS_DOCUMENT_TEMPLATES` | 提案 / SOW / 変更指令書 |
| 価格設定とリスク評価 | Closer / PM | Proposal / Kickoff | `PRICING_AND_RISK` | 見積 + Risk Register |
| チェックリスト実行 | PM / Technical Lead | 各納品段階 | `DELIVERY_CHECKLISTS` | 各段階チェック通過 |
| 納品検収 | PM + 顧客 | Handover | `DELIVERY_PACKAGE_AND_ACCEPTANCE` | 顧客サインオフ |
| ロール分担 | チーム全体 | 全工程 | `DELIVERY_ROLE_SOPS` | 明確な責任とハンドオーバー |

> ロジック：`ENGAGEMENT_LIFECYCLE` は主幹（ライフサイクル）；他 5 つは主幹各段階のツール — 文書テンプレ、価格リスク、チェックリスト、ロール SOP、納品検収。**7 Pillars**（顧客所有、顧客支払、セキュリティ最優先、徹底テスト、完全文書、クリーンハンドオーバー、明確スコープ）が全工程貫通。

## 5. ファイル説明

### 納品検収層

| ファイル | 用途 |
| --- | --- |
| `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` | AI 成熟度診断、L1-L5 講座、L4 Hermes Agent、8 段階コンサル診断レポートの納品パッケージリストと項目別検収表。 |

### 案件オペレーション層（Mirza Iqbal / next8n.com の Workflow Automation Delivery Framework から adapt、MIT、L1-L5 AI トランスフォーメーション文脈に generalized；引用は `../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md` 参照）

| ファイル | 用途 |
| --- | --- |
| `ENGAGEMENT_LIFECYCLE.md` | 3 段階ライフサイクル（Sales → Delivery → Support）、各段階のサブ段階と産出、7 Pillars、ライフサイクル × 8 段階クロスリファレンス、プリエンゲージメントチェックリスト。 |
| `DELIVERY_ROLE_SOPS.md` | 7 つの納品ロール SOP（Lead Gen / Sales Rep / Closer / PM / Technical Lead / Developer / Client）、各ロール：責任、キー納品物、ハンドオーバー点、協働相手、ライフサイクル段階、ロール × ライフサイクルマトリクスとハンドオーバー黄金ルール追加。 |
| `BUSINESS_DOCUMENT_TEMPLATES.md` | 8 種商業文書テンプレ：提案、SOW、MSA アウトライン、変更指令書、請求書、ハンドオーバー文書、保守契約、重要 email。**法的免責付き — テンプレ骨格は法律文書ではない、法務レビュー必要。** |
| `DELIVERY_CHECKLISTS.md` | 5 つの運用チェックリスト：pre-project、security、QA、handover、offboarding；方法論 Stage Gate との違い説明。 |
| `PRICING_AND_RISK.md` | 価格設定の 2 つの分離原則、4 つの価格モデル、段階的プロダクトライン、案件一般的リスクと緩和、いつ「ノー」と言うか、インシデント処理プロセス。 |

### `*_EN.md`

一部ファイルの英語版 sibling。

## 6. 他ディレクトリへの対応

| ディレクトリ | 本ディレクトリとの関係 | データフロー |
| --- | --- | --- |
| `01_Assessment` | 診断はライフサイクルの Sales 段に対応 | `01` ↔ `06` Sales |
| `02_Course_Design` | クラス内産出物が納品パッケージ検収に | `02` 産出 → `06` 検収 |
| `03_Consulting_Report` | コンサルレポートは納品パッケージのコア納品物 | `03` レポート → `06` 検収 |
| `05_Sales` | デックの見積/プラン分けがライフサイクルと価格設定に対応 | `05` デック ↔ `06` 価格 |
| `00_Overview` | 案件ライフサイクルはストーリーをビジネスに変える外枠 | `00` ストーリー → `06` 運用 |
| `90_References` | 案件オペレーション層の第三者引用（Mirza Iqbal フレームワーク） | `90` 引用 → `06` |

## 7. 共通使用シナリオ

- **新案件受領**：PM が `ENGAGEMENT_LIFECYCLE.md` の「開始前チェックリスト」で準備確認、`DELIVERY_ROLE_SOPS.md` でロール割り当て。
- **契約直前**：Closer が `BUSINESS_DOCUMENT_TEMPLATES.md` の SOW テンプレ（スコープ内外明記）使用、`PRICING_AND_RISK.md` で価格設定。
- **各納品段階**：`DELIVERY_CHECKLISTS.md` と照合し pre-project / security / QA / handover チェックリスト実行。
- **顧客への納品**：`DELIVERY_PACKAGE_AND_ACCEPTANCE.md` で項目別検収 + `BUSINESS_DOCUMENT_TEMPLATES.md` のハンドオーバー文書。
- **顧客が要件追加し続ける**：`PRICING_AND_RISK.md` のスコープクリープ緩和 + `BUSINESS_DOCUMENT_TEMPLATES.md` の変更指令書。
- **結案**：`DELIVERY_CHECKLISTS.md` の offboarding チェックリスト実行。

---

## ⭐ Cross-Topic Quick References：5 つの核心テーマ、どこで見つけるか

方法論全体には全ディレクトリを貫く 5 つの主動脈があります。本ディレクトリがそれぞれにどう接続するか：

| Cross-Topic | 主要位置 | 本ディレクトリがどう接続するか |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 3 エンジン共読** | Root [`README_JA.md`](../README_JA.md) §🌟 ｜ [`AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | 案件中に 3 エンジン分担動員可能：Antigravity が顧客会議 / Codex が SOW とレポート草稿監査 / Claude Code が Phase B シミュレーションと多視点レビュー |
| 🎓 **学術基盤（7 大支柱）** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | 7 Pillars の「セキュリティ最優先 / HITL」は Sociotechnical Systems & Trust（Bostrom / Dietvorst / Glikson）に対応；スコープクリープ / レベル飛び越し失敗は Real Options + Absorptive Capacity 失敗パターンに対応 |
| 📚 **L1-L5 講座教育** | [`../02_Course_Design/`](../02_Course_Design/) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md) | 納品パッケージ検収が L1-L5 各レベルの検収可能納品物カバー；クラス内産出物が [`DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](DELIVERY_PACKAGE_AND_ACCEPTANCE.md) で項目別検収 |
| 🔁 **コンサル方案 / 8 段階 + Phase A→B→C クローズドループ** | [`EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **本ディレクトリはコンサルクローズドループの「商業殻」** — 案件ライフサイクル Sales→Delivery→Support が Phase A→B→C + 四半期レーダー回顧に対応 |
| 📖 **参考資料 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | 案件オペレーション層が Mirza Iqbal / next8n.com の Workflow Delivery Framework（MIT）引用、詳細は [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) |
