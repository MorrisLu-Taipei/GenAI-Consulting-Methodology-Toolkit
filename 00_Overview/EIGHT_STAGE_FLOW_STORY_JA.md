# 8 段階コンサルティングフロー：完全シナリオストーリーとクローズドループ設計

> 🌐 言語：[繁體中文](EIGHT_STAGE_FLOW_STORY.md) ｜ [English](EIGHT_STAGE_FLOW_STORY_EN.md) ｜ [Deutsch](EIGHT_STAGE_FLOW_STORY_DE.md) ｜ [Français](EIGHT_STAGE_FLOW_STORY_FR.md) ｜ [Español](EIGHT_STAGE_FLOW_STORY_ES.md) ｜ 日本語 ｜ [한국어](EIGHT_STAGE_FLOW_STORY_KR.md)
>
> Apache License 2.0 · 著者：Morris Lu · Tiger AI

最終更新：2026-05-15

---

> **これは何か**：8 段階コンサルティング方法論を完全、再現可能、議論可能なクローズドループストーリーとして書いたもの。アンケート受付から実装計画まで、各ステップに明確なトリガー、デリバラブル、署名、次ステップとのロックイン関係がある。
>
> **これは何でないか**：6 週間の線形マラソンナラティブではない。むしろ **3 フェーズ契約モデル + 中間エンゲージメント顧客署名 + 四半期ループバック**の完全科学的管理プロセス。

---

## 0. 線形ウォークスルーに対する改善（3 つのより良い設計選択）

典型的なユーザー直観：
> アンケート + AI As-Is 評価 → RM と比較 → 成熟度 + ケースベンチマーキング → スコア → クライアントレポート表示 → クライアントが Ideal Practice 選択 → 必要なものを分析 → TO-BE 推奨 → コンサルレポート → 実装計画

**方向は正しい**。Tiger AI はこれに 3 つの改善を構築：

| # | 改善 | なぜより強いか |
| --- | --- | --- |
| **1** | **3 つの契約フェーズ**（Phase A Diagnostic / Phase B Strategy / Phase C Implementation）、6 週マラソンではない | クライアントが最初に低リスクで Phase A にコミット、結果に基づいて B / C を決定；コンサルタントは過剰コミットを回避 |
| **2** | **Phase A 終了：中間エンゲージメント評価レポートがデリバラブルとして署名される** Phase B Ideal Practice ワークショップ開始前 | クライアントは最初にレーダー空セルで衝撃を受け、その後 Ideal を選択 — ファンタジー回避；中間レポートも独立デリバラブル |
| **3** | **四半期ごとに Reference Model レーダーを再訪**（Phase C Implementation に入った後も継続） | 「完了したから良い」ではなく **「構造は実際により丸くなったか？」** — これが科学的クローズドループ反証メカニズム |

> **なぜ 6 週線形マラソンより強いか**：線形はクライアントに 6 週 + 24 ヶ月を一度にコミットさせる — 心理的障壁が高すぎ；3 フェーズは決定を分割し、リスクを減らし、受け入れを増やす。

---

## 1. 3 フェーズ契約モデル概観

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  Phase A: Diagnostic           Phase B: Strategy           Phase C:        ║
║                                                            Implementation  ║
║  ─────────────                ─────────────              ─────────────     ║
║  2 週 · NT$ 80 万             4 週 · NT$ 200 万          24 ヶ月 · NT$ 700 万║
║                                                                             ║
║  Stage 1 + 2 + 3 資料        Stage 3 Ideal Practice      Stage 7 + 8        ║
║                                + Stage 4 + 5                                ║
║                                                            （四半期         ║
║                                                            レーダー再訪）   ║
║                                                                             ║
║  デリバラブル：              デリバラブル：              デリバラブル：     ║
║  中間エンゲージメント        完全診断レポート            Transformation     ║
║  評価レポート                + Ideal Practice            Roadmap +          ║
║  （クライアント受領）        定義（3 者署名）            Change Mgmt +      ║
║                                                          Value Tracking +   ║
║                                                          四半期ログ        ║
╚═══════════════════════════════════════════════════════════════════════════╝
                ↑                       ↑                       ↑
            Gate A                  Gate B                   Gate C
        クライアントが B へ      クライアントが C へ        クライアントが各
        進む決定                 進む決定                   四半期継続を決定
```

**科学的意義**：各 Gate は「クライアントが降りられる出口点」 — コンサルタントは前フェーズデリバラブルが**クライアントが継続したいほど十分に良い**という**自信があるからこそ**これを設計。

---

## 2. 主人公：Client M

> ⚠️ **「Client M / MingChang Packaging」 は AI 生成架空企業**、実顧客ではない。すべてのスケール、KPI、予算、タイムライン数字は**説明用のみ**、方法論教育目的。完全な学術誠実性免責事項は [`../04_Scenarios/README_EN.md`](../04_Scenarios/README_EN.md) を参照。

- **業界**：半導体パッケージング & テスティング（FATP）
- **規模**：700 名従業員、NT$ 12 億年間売上
- **トリガー**：3 つの直接競合が AI 品質検査と Complaint Agent を展開；顧客 A の四半期受注 18% 減少
- **痛点**：Complaint response 5 日（業界 1 日）；Proposal turnaround 4 日（業界 1.5 日）；不良率 3.2%（業界 1.8%）
- **制約**：予算上限 NT$ 800 万；プロセスデータオンプレ；IT 2 FTE、成長なし
- **役割**：CEO（Sponsor）、COO、IT Director（潜在的 AI Champion）、QC Head、Sales Head、CS Head、HR、Compliance

---

## 3. Phase A: Diagnostic（2 週、NT$ 80 万）

### トリガー

M Company の CEO が Tiger AI アウトリーチメール受信 + GitHub でオープンソース方法論 repo を見る；秘書が 30 分イントロをスケジュール。

### Pre-Engagement: 10 問クイックサーベイ（翌週送信）

CEO が [`01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) の 10 問版を自己記入（5 分）。

**自動スコア結果**：

```
6 次元レーダー：
  ツール使用              1 / 4（一部 exec が ChatGPT 私的使用）
  ナレッジ沈殿            0 / 4（Wiki なし、SOP なし）
  プロセス自動化          1 / 4（Finance 1 Power Automate フロー）
  システム統合            2 / 4（ERP/CRM サイロ化）
  Agent 適用              0 / 4（なし）
  Governance & ROI        1 / 4（AI ポリシーなし）
合計：5 / 24 → 予備 L1
```

CEO がレーダーを見る → **最初の衝撃** → Phase A 契約署名に同意。

### Phase A フロー（週 1-2）

#### 週 1 ── Stage 1 As-Is Snapshot：聴く、観察、コメントなし

| 日 | アクション | Tool | 出力 |
| --- | --- | --- | --- |
| 日 1-2 | Exec インタビュー（CEO/COO/CIO × 60 分）+ Dept Head インタビュー（QC/Sales/CS/IT/HR × 90 分）| Tool 1.1（40 問バンク）| 録音 + サマリー |
| 日 3 | オペレーターインタビュー（Line/Sales/CS × 各 3 × 30 分）| Tool 1.1 Section C | サマリー |
| 日 4 | AI Usage Inventory + Systems Inventory | Tool 1.2 + 1.3 | Shadow IT リスクマップ + システムマップ |
| 日 5 | 3 つのキープロセスのウォークスルー + Swimlanes 描画 | Tool 1.4 | 3 As-Is プロセスマップ |

**週 1 終了**：コンサルタントがクライアントに「今、貴社が何をしているか分かりました」と告げる。**コメントなし、推奨なし。**

#### 週 2 ── Stage 2 Reference Model Alignment + Stage 3 資料準備

| 日 | アクション | Tool | 出力 |
| --- | --- | --- | --- |
| 日 6 | Reference Model 選択：SCOR + APQC + Tiger AI L1-L5 | Tool 2.1 | RM 選択理由 |
| 日 7-8 | マッピングワークシート：RM セルに As-Is を配置 | Tool 2.2 | マッピングテーブル |
| 日 9 | Standard Capability Gap チェックリスト + デュアルレーダー | Tool 2.3 + 2.4 | 2 つのレーダー（APQC + Tiger AI）|
| 日 10 | ベンチマークケース準備（5 stubs から半導体 + 2 同業界ケース選択）| Tool 3.1 + 3.3 | 3 つの Best-Practice Profile |

> **Phase A 規律**：日 10 コンサルタントは **まだ Ideal Practice ワークショップを実行しない**。資料のみ — 次フェーズで使用。

### Phase A デリバラブル：中間エンゲージメント評価レポート（クライアント受領）

**日 11-12 レポート執筆 → 日 13-14 クライアントレビュー → 日 14 closeout meeting**

中間エンゲージメントレポート（10-15 ページ）：

1. **Executive Summary**：「国際標準別、貴社は SCOR Make/Deliver、APQC 11.x Knowledge、Tiger AI L1-L3 に構造的ギャップを示す」
2. **As-Is Snapshot**：インタビューサマリー + システムマップ + 3 Swimlane
3. **Reference Model Mapping**：Standard Capability Gap チェックリスト
4. **デュアルレーダー**：APQC + Tiger AI L1-L5（点線 = ベンチマーク、実線 = 会社）
5. **業界 Best Practice 資料**：3 同業界 Benchmark Profile（資料のみ — **まだ結論なし**）
6. **次フェーズ推奨**：Phase B Ideal Practice Workshop（半日）+ Stage 4-5 分析

### Gate A：クライアントが Phase B へ進むか決定

**closeout meeting で起こること**：

- CEO がレーダーを見る：「うまくやっていると思っていた — 標準下でこれらのセルは 0？」 → **2 番目の衝撃**
- COO が Swimlanes をめくる：「我々の Complaint プロセスは本当にこれらの穴がある...」 → 痛点が具体化
- IT Director が shadow IT 月次支出を見る：「私的 ChatGPT が NT$ 24,000 を燃やし、データが漏れている...」 → リスクが具体化

**90% の顧客が Phase B に署名**。なぜなら：

- レーダーギャップはコンサルタント言ではない — 国際標準言 → **客観的**
- 痛みは従業員インタビュー録音にある → **検証可能**
- 同業界企業が既にやった → **達成可能**

> **Phase A の設計目標はこの衝撃そのもの**：クライアントが**自分でギャップを見る**、コンサルタントに言われるのではない。

---

## 4. Phase B: Strategy（4 週、NT$ 200 万）

### 週 3 ── Stage 3 Ideal Practice 共創ワークショップ（半日）

**日 15 朝** ─ Tool 3.6 共創ワークショップ

| ステップ | アクション | 時間 | 出力 |
| --- | --- | --- | --- |
| 1. 資料表示 | コンサルタントは Tool 3.1/3.3/3.4/2.7 4 層アーキテクチャを**表示のみ、推奨しない** | 30 分 | 共有資料 |
| 2. 独立投票 | 各人が**独立して**付箋に「12 ヶ月で我々が何になりたいか」を書く | 45 分 | N 枚の付箋 |
| 3. 集団コンセンサス | 4 層アーキテクチャに貼る、コンセンサス / 相違を見つける | 60 分 | v1 Ideal Practice ドラフト |
| 4. Reality check | コンサルタントが初めて介入、Tool 6.3 を使って実現可能性に挑戦 | 45 分 | v2 Ideal Practice |
| 5. 定義テーブル | v2 を「Ideal Practice Definition Table」として書く | 30 分 | 署名版定義テーブル |
| 6. **3 者署名** | CEO + Sponsor + AI Champion | 15 分 | 公的、監査可能ドキュメント |

**M Company の署名済み Ideal Practice Definition Table（抜粋）**：

| # | Capability | RM Category | 12 ヶ月ターゲット | エビデンス基準 |
| --- | --- | --- | --- | --- |
| 1 | Complaint response | APQC 4.4 + Tiger AI L3 | 90% が 1 時間内 + 24 時間人間返信 | n8n + Reviewer サインオフ率 ≥ 95% |
| 2 | ナレッジ沈殿 | APQC 11.x + Tiger AI L2 | ≥ 20 Skills 月間追加 | Skill Library Git + Owner + IPOE |
| 3 | Process root cause | SCOR Make + Tiger AI L4 | 異常 → 仮説 ≤ 1 時間 | Hermes Agent + 5 タスク Reviewer pass |

> **このテーブルは全エンゲージメントのアンカー**。すべての後続 Stage 4-8 計算はこれに基づく；クライアントは自分の署名済みターゲットを否定できない。

### 週 3-4 ── Stage 4 Gap Analysis + Stage 5 Problem Definition

#### Stage 4：Gap = （Client Ideal − Client As-Is）

| 日 | アクション | Tool | 出力 |
| --- | --- | --- | --- |
| 日 16-17 | M/B/R 分類 + Impact × Effort | Tool 4.1 + 4.2 | Gap matrix |
| 日 18 | Prioritization Worksheet | Tool 4.3 | 優先順位ランキング |

#### Stage 5：80/20 収束で Root Cause へ

| 日 | アクション | Tool | 出力 |
| --- | --- | --- | --- |
| 日 19 | 80/20 収束 + 5 Whys | Tool 5.1 + 5.2 | Core lesion リスト |
| 日 20-21 | Executive Problem Statement | Tool 5.3 + 5.4 | 一文定義 |

**M Company の Executive Problem Statement**：

> M Company には「ナレッジ資産化」の役割、ツール、インセンティブが欠けている。80% のギャップ（遅い Complaint / 遅い Quote / ナレッジ沈殿なし / 遅い Root Cause）は「同じことを反復し、誰も沈殿せず、誰も再利用しない」から来る。

### 週 4 ── Stage 6 Phased Goals + Stage 7 To-Be Design

#### Stage 6：Ideal を吸収可能ステップに分解

| 日 | アクション | Tool | 出力 |
| --- | --- | --- | --- |
| 日 22 | Ultimate Ideal → Phase 1/2/3 分解 | Tool 6.1 | 分解テーブル |
| 日 23 | 組織吸収評価（6 次元）| Tool 6.3 | 吸収スコア |
| 日 24 | Stage Gate Criteria | Tool 6.2 | L1-L5 Gate チェックリスト |

> **M Company の吸収評価は IT に 2 FTE しかないと発見；Phase 2 は +0.5 必要**。決定：Phase 2 を 6 → 9 ヶ月に延長。**この調整はクライアントが自分でデータを見て出した、コンサルタント推奨ではない**。

#### Stage 7：Phase ごとに 1 つの To-Be Operating Model

| 日 | アクション | Tool | 出力 |
| --- | --- | --- | --- |
| 日 25-26 | Phased To-Be Operating Models（3 図）| Tool 7.1 | 3 図 |
| 日 27 | Human-AI Collaboration + HITL ノード | Tool 7.2 | プロセスごとの分割 |
| 日 28 | Skill/Workflow/Agent Map + Integration Architecture | Tool 7.3-7.6 | 3 マップ + Variant B Hybrid |

### Phase B デリバラブル：完全診断レポート + Ideal Practice Definition Table

**日 29-30 レポート執筆 → 日 31-32 クライアントレビュー → 日 32 closeout meeting**

完全診断レポート（30-50 ページ）、[`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) 14 セクション構造別。

### Gate B：クライアントが Phase C へ進むか決定

**95% の顧客が Phase C に署名**。なぜなら：

- Ideal Practice は**彼らに署名された** → 否定不可能
- Gap は減算で計算 → **検証可能**
- Phase 1/2/3 は組織吸収にフィット → **達成可能**

---

## 5. Phase C: Implementation（24 ヶ月、NT$ 700 万）

### Stage 8 Implementation & Change

**最初の月（月 1）**

| 日 | アクション | Tool | 出力 |
| --- | --- | --- | --- |
| 日 33 | Transformation Roadmap（24 ヶ月 / 6 四半期）| Tool 8.1 | Roadmap |
| 日 34 | Change Management Plan + resistance Playbook | Tool 8.2 | Change plan |
| 日 35 | RACI + Permission Matrix + Audit Log | Tool 8.3 + 8.4 + 8.7 | ガバナンスドキュメント |
| 日 36 | Value Tracking Matrix（5 次元）| Tool 8.5 | Dashboard spec |
| 日 37 | Risk Register（case Failures を組み込む）| Tool 8.6 | Risk log |
| 日 38 | AI Ethics チェックリスト | Tool 8.8 | 署名済み ethics |
| 日 39 | SOW + Phase 1 kickoff | — | Phase 1 開始 |

### Phase 1（月 1-6）：Foundation

- L1 全社 OpenWebUI ライブ
- 5 つの core Skills 公開
- AI ポリシー > 90% 署名
- Prompt Library ≥ 30 エントリ

**月 6 終了 → L1 Gate acceptance + Stage 2 レーダー再訪**：

```
APQC 11.x Knowledge:  0 → 2（Skill library 開始）
Tiger AI L1:          0 → 4（完全 OpenWebUI + 92% policy 署名）
Tiger AI L2:          0 → 2（5 Skills）
```

> レーダーが**本当により丸い**。クライアントが涙ぐむ：「だからこれが科学的管理。」

### Phase 2（月 6-15）：Optimization

- L2 Skill Library ≥ 15 エントリ
- L3 n8n Workflow ≥ 3 ライブ
- HITL ノードが完全に配置

**月 15 終了 → L2/L3 Gate + レーダー再訪**：

```
APQC 4.0 Deliver: 1 → 3（complaint response 5 日 → 1 日）✓ Ideal 達成
APQC 11.x:        2 → 3（ナレッジ沈殿安定）✓ Ideal 達成
Tiger AI L3:      0 → 2（n8n PoC ライブ）
```

### Phase 3（月 15-24）：Excellence

- L4 Hermes Agent が 4A-4E を通過
- L5 ClawTeam cross-dept 1 つの成功リハーサル

**月 24 終了 → L4/L5 Gate + 最終レーダー**：

```
SCOR Make + Tiger AI L4: 0 → 3（Hermes Agent 通過）✓ Ideal 達成
Tiger AI L5:             0 → 2（ClawTeam cross-dept リハーサル）
```

### Gate C 四半期：クライアントは各四半期決定可能

各四半期は必須：

1. Quarter Gate acceptance（Tool 6.2 チェックリスト別）
2. Stage 2 レーダー再訪（改善を定量化）
3. Value tracking matrix 5 次元レビュー
4. クライアントが次四半期を進めるか、調整するか、一時停止するか決定

> 24 ヶ月後：M Company complaint response 1 日、不良率 2.0%、顧客 churn ゼロ、Stage 2 レーダーが**ギザギザ線からほぼ丸い形へ変化**。

---

## 6. 完全クローズドループ図

```
                          ┌──────────────────┐
                    ┌────►│ Phase A Diag 2W   │
                    │     │ Stage 1 + 2 + 3   │
                    │     │   資料準備        │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ 中間 Report       │ ← Phase A デリバラブル
                    │     │ （クライアント受領）│
                    │     └────────┬─────────┘
                    │              │
                    │           Gate A
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase B Strat 4W  │
                    │     │ Stage 3 Ideal     │
                    │     │ + Stage 4 + 5     │
                    │     │ + Stage 6 + 7     │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ 完全 Report       │ ← Phase B デリバラブル
                    │     │ + Ideal Practice  │
                    │     │ （3 者署名）      │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate B
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase C Impl 24M  │
                    │     │ Stage 8           │
                    │     │ Transformation +  │
                    │     │ Change + Value    │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase 1/2/3       │
                    │     │ Stage Gate accept │
                    │     └────────┬─────────┘
                    │              │
                    │     四半期 Gate C
                    │              │
                    │     ┌────────▼─────────┐
                    └─────┤ Stage 2 Radar    │
                          │ 再訪（より丸い？）│
                          └──────────────────┘
                                  
                          このフィードバックラインは
                          科学的クローズドループの
                          コア反証メカニズム
```

---

## 7. なぜこのフローがクライアント議論に耐えるか

すべての可能な challenge について、応答場所：

| Challenge | 場所 | エビデンス |
| --- | --- | --- |
| 「L1 だとなぜ分かる？」 | Phase A mid-report §2 レーダー | 10-Q サーベイ + 録音 + system inventory |
| 「なぜこれらのセルが 0？」 | Phase A §3 RM Mapping | APQC / Tiger AI 公的標準 |
| 「誰がターゲットを設定？」 | Phase B §5 Ideal Practice テーブル | **クライアント自身が署名、3 者署名** |
| 「なぜギャップが大きい？」 | Phase B §6 Gap Analysis | Gap = （あなたの署名 Ideal − あなたの As-Is）公式 |
| 「なぜカスタマーサービスがセールスより先？」 | Phase B §6.2 | Impact × Effort matrix |
| 「なぜ 24 ヶ月？」 | Phase B §8 + Tool 6.3 | Case Benchmark + Organizational Absorption |
| 「うまくいかなかったら？」 | Phase C §13 Risk Register | Trigger + Owner + Mitigation |
| 「改善したとどう証明？」 | 四半期 Gate C | Stage 2 レーダー + Value Tracking 5 次元 |
| 「前のコンサルは L3、あなたは L2 — 誰が正しい？」 | 公的 0-4 スケール + エビデンス | 第三者が独立検証可能 |

---

## 8. ユーザーオリジナルフローへのマッピング

| ユーザーステップ | Phase | Stage | 改善 |
| --- | --- | --- | --- |
| 1. アンケート + AI As-Is | Phase A W1 | Stage 1 | + 10-Q クイックスクリーンを pre-engagement として |
| 2. RM と比較 | Phase A W2 | Stage 2 | 4 層アーキテクチャ + デュアルレーダー |
| 3. 成熟度 + ケースベンチマーキング → スコア | Phase A 終 W2 | Stage 3 資料 | ケースは Benchmark-grade（9 フィールド）でなければならない |
| 4. **クライアントが評価レポートを見る** | **Phase A デリバラブル** | — | **新規：中間レポートを独立デリバラブル + クライアント受領として** |
| 5. クライアントが Ideal Practice 選択 | Phase B W3 | Stage 3 Tool 3.6 | **クライアント署名、コンサル処方ではない** |
| 6. 必要なものを分析 | Phase B W3-W4 | Stage 4 + 5 | Gap = Ideal − As-Is、80/20 収束 |
| 7. TO-BE 推奨 | Phase B W4 | Stage 6 + 7 | Phased + 組織吸収評価 |
| 8. コンサルレポート | Phase B デリバラブル | — | 14 セクション完全レポート + 署名済み Ideal Practice |
| 9. 実装計画 | Phase C kickoff | Stage 8 | Change Mgmt + Value Tracking + Audit |
| **（欠落）** | **四半期再訪** | — | **新規：各四半期 Stage 2 レーダー再訪（科学的クローズドループ）** |

---

## 9. 他ドキュメントとの関係

| ドキュメント | 本ドキュメントとの関係 |
| --- | --- |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 | 8 段階定義とデータフローを提供；本 doc は完全プロセスナラティブ |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | 「なぜそう設計」科学的論証を提供；本 doc は「実際にどう走るか」 |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | Per-Stage ツールテーブルを提供 |
| [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) | Phase B デリバラブル 14 セクション構造を提供 |
| [`../04_Scenarios/`](../04_Scenarios/) | Phase A 用 Benchmark-grade ケースを提供 |
| [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) | エンゲージメント / 価格 / デリバリー SOP を提供 |

---

## 10. クロージング：なぜクローズドループは科学か

このフローは**線形マラソンではなく**、**フィードバック付きクローズドループ**：

- **各 Gate は出口点** → コンサルタントはこう設計する**自信がある**（前のデリバラブルがクライアント継続意思を引き出すほど十分良い必要）
- **各デリバラブルにクライアント署名** → 後続推論を否定できない
- **各四半期 Stage 2 レーダー再訪** → 構造が実際により丸くなる = 成功、「PoC 完了 = 成功」ではない

**それが科学的管理**：

- 客観的な出発点（国際標準 + クライアント署名）
- 検証可能なプロセス（すべての Stage Gate Criteria）
- 反証可能な終点（デュアルレーダー before/after + Value Tracking 5 次元）

もし誰かが「Tiger AI 方法論は機能しない」と言うなら、彼らは**挑戦**しなければならない：

- APQC PCF は間違いか？
- Rosemann BPM 学派は間違いか？
- クライアント自身が署名した Ideal Practice はカウントされないか？
- 我々の四半期レーダーループバックはカウントされないか？

**難しい。** だからこそクローズドループ設計に投資した。

---

ライセンス & 引用

本ドキュメントは Apache License 2.0；[`../NOTICE`](../NOTICE) 帰属が保持されることを条件に、使用、修正、商業化可能。
