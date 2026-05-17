# Pilot Study Protocol：Tiger AI 方法論の実証検証研究計画

> 🌐 言語：[繁體中文](PILOT_STUDY_PROTOCOL.md) ｜ [English](PILOT_STUDY_PROTOCOL_EN.md) ｜ [Deutsch](PILOT_STUDY_PROTOCOL_DE.md) ｜ [Français](PILOT_STUDY_PROTOCOL_FR.md) ｜ [Español](PILOT_STUDY_PROTOCOL_ES.md) ｜ 日本語 ｜ [한국어](PILOT_STUDY_PROTOCOL_KR.md)
>
> Apache License 2.0 · 著者：Morris Lu · Tiger AI

最終更新：2026-05-16
バージョン：v1.0 Research Design Protocol（pre-registration ready）

---

> **目的**：Tiger AI 方法論を「よく設計されたコンサルティングフレームワーク」から「研究可能なモデル」へ進化させる。本プロトコルは 18-24 ヶ月、5-10 企業の実証パイロット研究を定義、**方法論を自己検証だけでなく外部反証にさらす**。
>
> これは IRB 提出 / 学術 pre-registration / 政府研究助成申請の準備ができた**研究設計ドキュメント**。

---

## 1. 背景 & 動機

### 1.1 なぜ実証研究

Tiger AI 方法論の現在のエビデンス強度：

| 要素 | Evidence Level（Tool 8.9）| ステータス |
| --- | --- | --- |
| 8 段階フロー設計 | L2 文書的論証 | 完了（Rosemann BPM + 業界フレームワーク統合）|
| 6 構成概念 × 0-4 スケール | L2 専門家コンセンサス | 完了（**心理測定検証なし**）|
| 7 ケースライブラリ | L2 匿名化合成 | 完了（**実縦断データなし**）|
| Self-Qualification（Tool 2.5）| L1 Self-Report | 完了（**自己参照、外部検証なし**）|
| Inter-Rater Consistency | — | **未実施** |
| 縦断 KPI 方法論への応答 | — | **未実施** |

**結論**：方法論は「内部一貫性 + 論理的閉鎖性」で成熟しているが、「外部再現性 + 予測妥当性」については実証的にテストされていない。本パイロット研究は両方に対処。

### 1.2 研究質問

**RQ1 — Inter-Rater Reliability**：異なるコンサルタントが同じ方法を使って同じ会社を一貫してスコアできるか？

- **H1**：Cohen's κ ≥ 0.60（substantial agreement）

**RQ2 — 内部一貫性**：6 構成概念はどれくらい内部一貫的か？

- **H2**：Cronbach's α ≥ 0.70 構成概念ごと

**RQ3 — 構成概念妥当性**：6 構成概念は因子分析できれいに浮かび上がるか？

- **H3a**：EFA が 5-6 因子を抽出；各項目が割り当てられた因子に ≥ 0.5 でロード
- **H3b**：CFA 6 因子モデルフィット：CFI ≥ 0.90、TLI ≥ 0.90、RMSEA ≤ 0.08

**RQ4 — 予測妥当性**：T0 スコアは T+12 ヶ月のビジネス KPI 向上を予測できるか？

- **H4**：ベースライン KPI と企業サイズをコントロールしつつ、Tiger AI maturity スコアは +12m KPI 向上を正に予測（β ≥ 0.30、p < 0.05）

**RQ5 — 縦断パターン**：Phase C 24 ヶ月を完了する企業は「より丸い」レーダーを示すか？

- **H5**：T0 vs T24 レーダー面積（6 構成概念合計）が有意に増加、各構成概念の成長は Tool 6.1 分解（foundation → optimization → excellence）に従う

---

## 2. 研究設計

### 2.1 設計タイプ

- **混合方法縦断研究**
- **Convergent Parallel Design**：定量（スケールスコアリング、KPI）+ 定性（半構造化インタビュー、ケーススタディ）同時
- **Pre-Registered**（公的仮説、サンプリング、分析計画；p-hacking 回避）

### 2.2 サンプル

| 項目 | 仕様 |
| --- | --- |
| **ターゲットサンプル N** | 5-10 企業（パイロットステージ；メインスタディ N=200+ CFA 用）|
| **業界多様性** | ≥ 3 業界（製造、サービス、公共セクター ≥ 1 ずつ）|
| **企業規模** | 100-5000 従業員 |
| **AI 出発点** | L0-L2（既に L3+ は介入空間限定により除外）|
| **コミットメント期間** | 18 ヶ月（研究協力協定）|
| **インセンティブ** | 無料 / 割引コンサルティング + 共同出版機会 + ケース匿名化コントロール |

### 2.3 リクルート戦略

1. n8n Taipei Ambassador コミュニティ、企業顧客ネットワーク、学術パートナー機関経由（具体的パートナーは MOU 締結後に開示）
2. 公的勧誘 + Apache 2.0 オープン repo を信頼シグナルとして
3. 署名済み研究協力協定（データ使用、匿名化、Exit メカニズム）

### 2.4 倫理 / IRB

- 学術パートナー機関 IRB 承認に申請（パートナーは MOU 締結後に開示）
- インフォームドコンセント：全参加者を書面で
- センシティブデータ取り扱い：PII / ビジネス機密グレーディング；ダブルブラインドデータ分離
- 撤回権：いかなる企業もいつでも退出可能；収集データ返却または破棄

---

## 3. ダブルブラインドスコアリング設計

### 3.1 目的

Tiger AI スコアリングモデルの **Inter-Rater Reliability** を検証。

### 3.2 設計

```
T0 スコアリングフェーズ（企業ごと）：
  ↓
  コンサルタント A が独立して完了：
    • インタビュー（Tool 1.1 40-Q バンク）
    • Inventory + Swimlane（Tools 1.2-1.4）
    • Reference Model Mapping（Tool 2.2）
    • 6 構成概念 0-4 スコアリング（Tool 2.3）
    • 主要 maturity 判定（L1-L5）
  ↓
  コンサルタント B が独立して完了（同じ企業、A に対してブラインド）：
    • 上記全アクションを繰り返し
  ↓
  研究アナリスト（中立）が A vs B を比較：
    • 6 構成概念スコアギャップ（weighted kappa）
    • 主要 maturity 判定一致（unweighted kappa）
    • ギャップ識別オーバーラップ（M/B/R テーブルオーバーラップ）
```

### 3.3 一貫性統計

| メトリクス | ツール | 解釈 |
| --- | --- | --- |
| **Cohen's κ（unweighted）** | κ = (Po - Pe) / (1 - Pe) | < 0.20 slight；0.21-0.40 fair；0.41-0.60 moderate；0.61-0.80 substantial；> 0.80 almost perfect |
| **Weighted κ（linear / quadratic）** | 順序スケール（0-4）用 | 上記同様、しかし「1 ポイント off」 vs 「4 ポイント off」 でより厳格 |
| **ICC（Intraclass Correlation）** | Two-way Mixed Model | < 0.5 poor；0.5-0.75 moderate；0.75-0.9 good；> 0.9 excellent |
| **Bland-Altman プロット** | スコアギャップを可視化 | システマティックバイアスを検出 |

---

## 4. 縦断 KPI トラッキング

### 4.1 KPI 測定時点

| 時点 | 名前 | 測定 |
| --- | --- | --- |
| **T0** | Baseline | Phase A 後、Phase B 前 |
| **T+6m** | Phase 1 終了 | L1 Gate Acceptance |
| **T+12m** | Mid Phase 2 | L2/L3 Gate |
| **T+18m** | Phase 2 終了 | L3 完了 |
| **T+24m** | Phase 3 終了 | L4/L5 Gate |

### 4.2 5 KPI 次元（Tool 8.5 Value Tracking 別）

| 次元 | KPI 例 |
| --- | --- |
| **Time** | Complaint response、proposal turnaround、month-end close、decision cycle |
| **Quality** | 不良率、エラー率、Complaint count、rework rate |
| **Scale** | Throughput、beneficiaries、automated task count |
| **Risk** | Missed case rate、compliance violations、sensitive-data leakage |
| **Assets** | Skill count、Wiki entries、Agent task count、training completion |

### 4.3 KPI データ品質（Tool 8.9 Evidence Hierarchy 別）

- **L3 必須**：全 Time / Scale KPI を system logs（n8n / Audit Log / ERP）から
- **L4 推奨**：Internal Audit / External Accountants によるサンプル検証
- **L1-L2 補足**：Employee NPS / インタビューサマリー

---

## 5. 定性：半構造化インタビュー

### 5.1 インタビュー時点

企業ごと：T0、T+6m、T+12m、T+18m、T+24m — 各 1 ラウンド（インタビュー対象者ごと）。

### 5.2 インタビュー対象者

- CEO / Sponsor
- AI Champion
- IT Lead
- ≥ 2 Department Heads
- ≥ 3 Front-line Users

### 5.3 インタビュー質問（抜粋）

1. 過去 6 ヶ月で最もインパクトのある AI 変化は何か？
2. 期待された AI 変化のうち、起きなかったものは？なぜ？
3. AI に対するスタッフ / 部門の態度はシフトしたか？
4. このメソドロジーをピアに推奨する / しない？
5. 最も有用な Stage / Tool はどれ？最も有用でないのは？
6. Cross-time：12 ヶ月前に署名された Ideal Practice を振り返り、後悔はあるか？

### 5.4 定性分析

- 逐語転写 + コーディング（NVivo / Atlas.ti）
- Dual-Coder Reliability ≥ 80%
- パターン / カウンター例を抽出するためのテーマ分析

---

## 6. 統計分析計画

### 6.1 記述統計

- 構成概念ごとのスコア分布（mean、SD、median、IQR）
- レーダーチャート T0 vs T24 可視化
- 6 構成概念相関行列（多重共線性チェック）

### 6.2 Reliability & Validity

| 分析 | ツール | 仮説にマップ |
| --- | --- | --- |
| Cronbach's α | SPSS / R `psych::alpha()` | H2 |
| EFA + Bartlett's + KMO | SPSS / R `psych::fa()` | H3a |
| CFA + fit indices | Mplus / R `lavaan::cfa()` | H3b（**N ≥ 200 必要**）|
| Cohen's κ | R `irr::kappa2()` | H1 |
| ICC | R `irr::icc()` | H1 |

### 6.3 推論統計

| 分析 | 仮説 | ツール |
| --- | --- | --- |
| Paired t-test（T0 vs T24）| H5 レーダー面積増加 | R `t.test(paired=TRUE)` |
| Mixed-Effects Model | H4 予測妥当性 | R `lme4::lmer()` |
| ANCOVA | ベースライン KPI + サイズコントロール | R `aov()` |
| 感度分析 | 欠損データ + ドロップアウトに対し | R `mice` Multiple Imputation |

### 6.4 有意性 & 調整

- α = 0.05 メインテスト
- Bonferroni Correction を Multiple Comparisons 用に
- Effect Size レポート：Cohen's d、η²、partial η²

---

## 7. タイムライン & マイルストーン

```
月 0：    設計完成 + IRB 提出
月 1-3：  5-10 企業リクルート + 研究協定署名
月 4：    コンサルタント A/B トレーニング（ダブルブラインド SOP）
月 5-6：  T0 ダブルブラインドスコアリング + Baseline KPI 測定
月 6-12： Phase 1 介入 + T+6m スコアリング + インタビュー
月 12-18：Phase 2 介入 + T+12m + T+18m
月 18-24：Phase 3 介入 + T+24m 最終スコアリング + インタビュー
月 24-27：分析 + 研究レポート + ジャーナル提出
月 27-30：改訂 + 提出
```

---

## 8. 予算見積もり

| 項目 | 見積もり（NT$）|
| --- | --- |
| コンサルタント時間（A + B 80-120 時間ずつ企業ごと）| 6-9M |
| 研究スタッフ（中立スコアリング比較 + 定性分析）| 1.5-2.5M |
| KPI system-log ツール + インタビュー転写 | 0.5-1M |
| IRB / 法務 / 統計コンサルタント | 0.5-1M |
| オープンソースツール + クラウドデータストア | 0.3-0.5M |
| コンティンジェンシー（15%）| 1.3-2M |
| **合計** | **NT$ 10.1-16M** |

⚠️ 無料コンサルティングの交換に、5-10 企業が 18 ヶ月のデータ収集にコミット → コンサルタント労力は「equivalent consulting service」でオフセット可能、**実キャッシュ支出は NT$ 4-7M に削減可能**。

---

## 9. 出版戦略

### 9.1 期待される出力

| 出力 | ジャーナル / プラットフォーム | 推定タイミング |
| --- | --- | --- |
| **Pre-Registration** | OSF | 月 0 |
| **Protocol Paper** | BMJ Open / Pilot and Feasibility Studies | 月 3 |
| **Methodology Paper** | MIS Quarterly / Information Systems Research / Journal of Business Research | 月 27 |
| **Industry White Paper** | バイリンガル、公的 Apache 2.0 | 月 27 |
| **Case Studies（匿名化）** | HBR スタイルケース | 月 30 |
| **Practitioner Guide** | ツールキット更新 + 実証エビデンス追加 | 月 30 |

### 9.2 Open Science コミットメント

- 全研究データ（de-identified）が OSF で公開
- 統計 R / Python スクリプトが GitHub に
- インタビュー対象者ID 機密；集計結果は完全に透明

---

## 10. リスク & 緩和

| リスク | 確率 | インパクト | 緩和 |
| --- | --- | --- | --- |
| 企業途中撤退（ドロップアウト）| Med | High | 12 まで過剰リクルート；Intention-to-Treat 分析 |
| コンサルタント A/B バイアス / リーク | Low | High | SOP トレーニング + 監査 + 厳格ダブルブラインド + 異なるオフィス |
| KPI system log アクセス不可 | Med | Med | T0 IT がログ可用性確認；そうでなければ代替指標 |
| IRB レビュー遅延 | Med | Med | 月 0 IRB 提出をリクルートと並行 |
| CFA に N 不足 | High | Med | パイロットで EFA；CFA はメインスタディ N=200+ を待つ |
| 予算不足 | Med | High | 政府助成（NSTC / MOE 等）/ 学術パートナー助成申請；複数企業コストシェアリング |

---

## 11. Stopping Rules

完全開示付き早期終了は以下の場合：

- ≥ 50% 企業が撤退
- Inter-Rater κ < 0.40（方法論不一致 → スケール再設計必要）
- IRB 取消
- 深刻な倫理問題（データリーク、参加者損害）

**早期終了された研究も収集データを全て出版しなければならない**（出版バイアス回避）。

---

## 12. 期待される貢献

| 貢献 | オーディエンス | 形式 |
| --- | --- | --- |
| **理論**：最初の実証検証済み GenAI 採用 maturity モデル | アカデミア（IS / BPM / Strategy）| ピアレビュー論文 |
| **方法**：Cases-as-Benchmarks + Client Ideal Practice ワークショッププロトコル | コンサルティング業界 | オープンソースツールキット（Apache 2.0）|
| **政策**：AI Governance Alignment の実証エビデンス | 規制当局（Taiwan AI Basic Act / NIST / EU）| ホワイトペーパー + 立法公聴会 |
| **業界**：5-10 企業実縦断ケース | ピアクライアント | 実ケース（合成を置換）|
| **教育**：学術パートナー機関カリキュラムに統合 | 学生 | コース材料 |

---

## 13. 関連ドキュメント

| ドキュメント | 関係 |
| --- | --- |
| [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) §3.1-3.3 | スケール構成概念定義；本研究が検証 |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | なぜ方法論が実証検証を必要とするか |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | 既知の Failure Modes → 緩和が本研究に組み込まれている |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9 | KPI エビデンスグレーディング用 Evidence Hierarchy ベース |

---

## 14. 参考文献

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297-334.
- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- Streiner, D. L., Norman, G. R., & Cairney, J. (2015). *Health measurement scales: A practical guide to their development and use* (5th ed.). Oxford University Press.
- Hair, J. F., et al. (2019). *Multivariate Data Analysis* (8th ed.). Cengage.
- Creswell, J. W. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). SAGE.
- Open Science Framework：<https://osf.io/>

---

ライセンス & 引用

本ドキュメントは Apache License 2.0；[`../NOTICE`](../NOTICE) 帰属が保持されることを条件に、使用、修正、商業化可能。他の研究チームは同じ Pre-Registration と Open-Science コミットメントに従う限り、本設計を**自由に採用、修正、複製**可能。
