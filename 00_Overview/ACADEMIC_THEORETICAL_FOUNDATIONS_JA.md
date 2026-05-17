# 学術理論基盤：Tiger AI 方法論の七つの理論的柱

> 🌐 言語：[繁體中文](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [English](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) ｜ [Deutsch](ACADEMIC_THEORETICAL_FOUNDATIONS_DE.md) ｜ [Français](ACADEMIC_THEORETICAL_FOUNDATIONS_FR.md) ｜ [Español](ACADEMIC_THEORETICAL_FOUNDATIONS_ES.md) ｜ 日本語 ｜ [한국어](ACADEMIC_THEORETICAL_FOUNDATIONS_KR.md)
>
> Apache License 2.0 · 著者：Morris Lu · Tiger AI

最終更新：2026-05-16

---

> **目的**：ファイルに散在する Tiger AI 方法論の学術的理論基盤を**1 つの権威ある文書**に統合。いかなる学者 / 規制者 / 真剣なコンサルタントが「理論的基盤は何か」と問うても、本ドキュメントが答え。
>
> **核心主張**：Tiger AI 方法論は単にコンサルティング実践ではなく、**7 つの理論のエンジニアリング統合**。

---

## 1. 理論マップ概観

| 理論 | 創始者 / 古典参考文献 | 解決された核心問題 | Tiger AI マッピング |
| --- | --- | --- | --- |
| **Capability Maturity & BPM Maturity** | Paulk et al.（1993）CMMI；Rosemann & de Bruin（2005） | 組織能力をどう構造化してスコアするか？ | L1-L5 + Stage 2 スコアリング |
| **Absorptive Capacity** | Cohen & Levinthal（1990） | 組織が新しい能力を**吸収**することで大きく異なるのはなぜか？ | Tool 6.3 Organizational Absorption Assessment |
| **Task-Technology Fit（TTF）** | Goodhue & Thompson（1995） | どのタスクが AI に合う / 合わないか？ | Stage 7 To-Be Design（全部門が L5 に到達すべきではない）|
| **Dynamic Capabilities** | Teece et al.（1997）；Teece（2007） | 組織はどう**外部変化に素早く適応するか**？ | Stage 7 + Stage 8（静的自動化から動的能力へ）|
| **Sociotechnical Systems & Trust in AI** | Bostrom & Heinen（1977）；Dietvorst et al.（2015）；Glikson & Woolley（2020） | 人間-AI 協働はなぜ難しいか？Algorithm aversion / complacency | Stage 8 Change Management + HITL |
| **Real Options Theory** | Dixit & Pindyck（1994）；McGrath（1997） | 高不確実性 AI 戦略投資をどう評価するか？ | Stage 8 §13 Value Tracking + ROI |
| **AI-Native Living Book / Executable Knowledge Artifact** | Knuth（1984）；Anderson et al.（1995）；本著者（2026） | 方法論自体が AI によって実行可能か？ | AGENTS.md + AI_NATIVE_LIVING_BOOK |

---

## 2. Capability Maturity & BPM Maturity

### 2.1 理論サマリー

- **CMMI**：Paulk et al.（1993）が SEI で 5 レベル組織能力（Initial / Repeatable / Defined / Managed / Optimizing）を定義
- **BPM Maturity Model**：Rosemann & de Bruin（2005、QUT）が Maturity を Business Process Management へ拡張、6 イネーブラーを追加：Process Awareness / Alignment / Methods / IT / People / Culture

### 2.2 Tiger AI への貢献

- **L1-L5 二軸**は BPM Maturity の「Process Awareness → Optimization」論理を継承、GenAI 時代必須の「**スケール軸 + AI 自律軸**」二重構造を追加
- **0-4 スケール + BARS 行動アンカー**はこの学派から
- **Stage Gate Criteria** = CMMI の「Process Areas」 + フェーズ受入

### 2.3 マッピングされたファイル

- [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §3.0 二軸ストーリー
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) L1-L5 定義
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) 行動アンカー

---

## 3. Absorptive Capacity

### 3.1 理論サマリー

- **Cohen & Levinthal（1990）** *Administrative Science Quarterly* にて：組織の「**外部知識を識別、同化、適用する能力**」がそのイノベーション能力を決定
- 核要素：**Prior Knowledge + Internal Knowledge Flow**
- Zahra & George（2002）がさらに 4 次元に分割：Acquisition / Assimilation / Transformation / Exploitation

### 3.2 Tiger AI への貢献

- **同じ AI 機会が企業によって極端に異なる結果を yield する**理由を説明 — 違いは absorptive capacity
- Tool 6.3 Organizational Absorption Assessment はこの理論に直接マップ
- 「**なぜレベルをスキップできないか**」を強化：L1-L3 スキップ → absorptive capacity 不足 → L4-L5 は失敗（[`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) §2 参照）

### 3.3 Tool 6.3 への具体的拡張

オリジナル Tool 6.3 6 次元（Budget / Champion / IT FTE / Governance / Literacy / Change capacity）に **2 つの新次元追加**：

| 新次元 | 評価質問 | スコア |
| --- | --- | --- |
| **Prior Knowledge** | 企業に：(a) 過去の BPM / Lean / Six Sigma 経験あり？(b) 過去の AI / ML / RPA 試行あり？(c) 内部ソフトウェア開発能力あり？ | 0-4 |
| **Internal Knowledge Flow** | 部門間：(a) 定期的部門横断レビュー？(b) 共有ドキュメントプラットフォーム？(c) 内部メンター / インストラクターシステム？ | 0-4 |

→ High Prior Knowledge + High Knowledge Flow 企業はより積極的な Phase 1/2/3 を扱える；逆に、タイムラインを延長必要。

### 3.4 参考文献

- Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128-152.
- Zahra, S. A., & George, G. (2002). Absorptive capacity: A review, reconceptualization, and extension. *Academy of Management Review*, 27(2), 185-203.

---

## 4. Task-Technology Fit（TTF）

### 4.1 理論サマリー

- **Goodhue & Thompson（1995）** *MIS Quarterly* にて：技術がパフォーマンスを向上させる度合いは「**タスク需要 ↔ 技術能力**」フィットに依存
- タスク分類：**Routine（反復的、予測可能） vs Non-routine（判断重視、創造的）**

### 4.2 Tiger AI への貢献

**全部門が L5 に到達すべきではない**。タスク特性により各部門の適切な L レベル終点を決定：

| タスクタイプ | 適切な終点 | 根拠 |
| --- | --- | --- |
| Highly Routine（CS FAQ、請求書分類）| L3-L4 | 高 AI フィット；低 HITL コスト |
| Medium Routine + 部分判断（営業提案、月末異常）| L2-L3 + HITL | AI ドラフト + 人間確認；効率とリスクをバランス |
| Highly Non-routine（M&A 評価、戦略決定）| L1-L2（個人アシスタント） | AI 支援、人間がリード；L4-L5 プッシュは判断品質を害する |
| Highly compliance-sensitive（法務、医療診断）| L2-L3 + strong HITL | 規制リスク高すぎ；L4-L5 不適合 |

### 4.3 マッピングされたファイル / Tools

- Stage 7 Tool 7.2 Human-AI Collaboration → TTF マトリクスがプロセスごとの AI 関与を決定
- Tool 6.3 に **TTF Assessment Worksheet 追加** → 部門ごとに TTF スコア、Ideal L レベル決定

### 4.4 参考文献

- Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. *MIS Quarterly*, 19(2), 213-236.
- Zigurs, I., & Buckland, B. K. (1998). A theory of task/technology fit and group support systems effectiveness. *MIS Quarterly*, 22(3), 313-334.

---

## 5. Dynamic Capabilities

### 5.1 理論サマリー

- **Teece, Pisano & Shuen（1997）** *Strategic Management Journal* にて：競争優位は「**内部・外部リソースの統合、構築、再構成**」に由来
- **Teece（2007）** が 3 つのマイクロ基盤に分解：
  1. **Sensing**：機会と脅威の識別
  2. **Seizing**：決定とリソース配分
  3. **Transforming**：機会を活用するための組織再構成

### 5.2 Tiger AI への貢献

**静的自動化から → 動的適応能力**。Tiger AI は既存 APQC プロセスを AI 化するだけでなく、**外部変化に継続的に適応する新能力をクライアントに構築**：

| Dynamic Capability | Tiger AI マッピング |
| --- | --- |
| **Sensing** | L3 Workflow + L4 Agent が市場 / 顧客 / プロセス信号を継続モニター |
| **Seizing** | Phase 1/2/3 分解 = sensed 信号を具体的投資決定へ変換 |
| **Transforming** | L5 Multi-Agent Organization + 四半期 Gate C レーダー = 継続的組織再構成 |

### 5.3 Stage 7 への具体的拡張

Stage 7 To-Be Design に **Dynamic Capability Worksheet 追加**：

```
Teece（2007）3 マイクロ基盤別、各 To-Be 設計は答えなければならない：

1. Sensing：この AI 設計が会社が「sense」するのを助ける外部信号は何？
   例：complaint Agent が顧客満足度トレンドをモニター
2. Seizing：信号が現れた時、会社は何で「seize」できる？
   例：Quick Win complaint response 5d → 1d が顧客損失ウィンドウを圧縮
3. Transforming：この AI が組織「self-reconfiguration」をどう可能にする？
   例：L5 ClawTeam 部門横断 = 組織が特定シニアスタッフに依存しない
```

→ これら 3 つに答えない To-Be はただの「現状を自動化」、真のトランスフォーメーションではない。

### 5.4 参考文献

- Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal*, 18(7), 509-533.
- Teece, D. J. (2007). Explicating dynamic capabilities. *Strategic Management Journal*, 28(13), 1319-1350.

---

## 6. Sociotechnical Systems & Trust in AI

### 6.1 理論サマリー

- **Sociotechnical Systems Theory**（Bostrom & Heinen, 1977）：組織パフォーマンス = **社会システム + 技術システム**のジョイントアウトプット；どちらか単独で最適化できない
- **Algorithm Aversion**：Dietvorst, Simmons & Massey（2015）*JEP* にて：人々は**アルゴリズムが間違うのを見た後、アルゴリズムより劣る人間の判断を好む**、アルゴリズムがより正確と知っていても
- **Automation Complacency**：Parasuraman & Manzey（2010）：自動化への過信が警戒喪失を引き起こし、より大きなインシデントへ導く
- **Trust in AI**：Glikson & Woolley（2020）が認知的 + 感情的トラストを統合

### 6.2 Tiger AI への貢献

人間-AI 協働の真のチャレンジは「置換への恐れ」だけでなく、また：

1. **Algorithm Aversion**：AI の最初のエラー後、スタッフが集団的に拒絶 → L3-L4 ローンチ後によく見られる
2. **Automation Complacency**：スタッフがレビューをやめる → HITL が失敗 → より大きなインシデント
3. **Accountability 曖昧性**：AI が間違った時誰が責任？スタッフが非難を恐れる → 心理的安全性ギャップ
4. **専門アイデンティティ再形成**：「Doer」から「Reviewer」へ → 認知負荷と達成感がシフト

### 6.3 Stage 8 Change Management への拡張

Tool 8.2 に 2 つの新しい抵抗タイプを追加：

| 抵抗タイプ | 典型的信号 | 処理 |
| --- | --- | --- |
| **Algorithm Aversion** | 1 つの AI エラー後の集団拒絶 | エラー率の透明性（人間 vs AI）+ 段階的トラスト構築（低リスクシナリオから開始）|
| **Automation Complacency** | スタッフがレビューせずに承認 | Reviewer Workflow での必須ランダムサンプリング + 検出されたエラー後の再訓練 |

### 6.4 HITL 設計（Tool 7.2）への拡張

**心理的安全性と accountability カラム追加**：

| プロセス | HITL Node | **Accountability Statement** | **心理的安全性** |
| --- | --- | --- | --- |
| CS reply | 送信前 100% 人間レビュー | AI ドラフト責任 = AI Champion；最終返信責任 = CS スタッフ | スタッフは「AI が間違っていればレビューなしで拒否」する権利を持ち、非難なし |
| Process root cause | アクション前 100% 人間レビュー | AI 仮説責任 = Agent 開発者；アクション責任 = プロセスマネージャー | マネージャーは「AI 提案を拒否」する正式 SOP を持つ |

### 6.5 参考文献

- Bostrom, R. P., & Heinen, J. S. (1977). MIS problems and failures: A socio-technical perspective. *MIS Quarterly*, 1(3), 17-32.
- Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion. *JEP: General*, 144(1), 114-126.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3), 381-410.
- Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence. *Academy of Management Annals*, 14(2), 627-660.
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *ASQ*, 44(2), 350-383.

---

## 7. Real Options Theory

### 7.1 理論サマリー

- **Dixit & Pindyck（1994）** *Investment Under Uncertainty* にて：高不確実性投資価値 = 即時実行価値 + 「**将来オプショナリティ**」価値
- **McGrath（1997）** が戦略へ適用：「**今日の投資が将来拡大する権利を保持**」
- 不確実性下の NPV 過小評価に対抗：NPV は確実性を前提とするが、管理柔軟性は不確実性下で高い価値

### 7.2 Tiger AI への貢献

L4-L5 高不確実性 AI 投資は**伝統的 NPV / IRR で必然的に過小評価される**（18-24 ヶ月キャッシュフローが不確実なため）。Real Options がより良いフレーミングを提供：

| 投資 | NPV ビュー（過小評価）| Real Options ビュー（正当化）|
| --- | --- | --- |
| Phase 1 Foundation（NT$ 280 万）| キャッシュフロー不明 → NPV ≈ 0 | 「**将来低コストで L4-L5 を急速に拡大するオプション**」を購入、NT$ 280 万よりはるかに価値 |
| L1 全社 Chat AI | 短期 ROI 不明 | 従業員 AI リテラシー = **将来の全 AI アプリケーションのための基盤資産** |
| L2 Skill Library | ROI 不可視 | ナレッジ codification = 会社の「**将来複数の AI アプリケーションを同時にプラグイン**」するオプション |
| L4 Hermes Agent Pilot | 1 つの Agent が価値あるか？ | Pilot = L4 を学ぶ = L5 ClawTeam へのオプション |

### 7.3 Real Options Valuation（簡略化 Black-Scholes）

L4-L5 投資のため、以下経由で見積もり：

```
Option Value = max(0, future_payoff - exercise_cost)

ここで：
  future_payoff = オプション行使からの収益（例：L5 へ拡大）
  exercise_cost = 行使時のコスト（例：Phase 3 投資）
  volatility（σ）= 市場 / 技術不確実性
  time-to-expiration = 機会ウィンドウ
```

⚠️ 正確な Black-Scholes 不要；**ナラティブレベル議論で「短期 ROI 不可視だが長期価値ある」投資を正当化するため CFO を説得するのに十分**。

### 7.4 Stage 8 §13 Value Tracking への拡張

オリジナル 5 次元（Time / Quality / Scale / Risk / Assets）、**6 番目の次元追加**：

| 次元 | 内容 |
| --- | --- |
| **Strategic Options** | この投資が保持した「**将来行使権**」は何？例：L1 foundation → 将来 L4 を急速に拡大可能；L2 Skill Library → 将来の任意の Agent をプラグイン可能；L3 Workflow → 任意の新システムを統合可能 |

### 7.5 参考文献

- Dixit, A. K., & Pindyck, R. S. (1994). *Investment Under Uncertainty*. Princeton University Press.
- McGrath, R. G. (1997). A real options logic for initiating technology positioning investments. *Academy of Management Review*, 22(4), 974-996.
- Trigeorgis, L. (1996). *Real Options*. MIT Press.

---

## 8. AI-Native Living Book as Executable Knowledge Artifact

### 8.1 理論サマリー

- **Literate Programming**：Knuth（1984）はコードとドキュメントを単一の「人間可読 + 機械実行可能」ドキュメントに統合すべきと主張
- **Intelligent Tutoring Systems（ITS）**：Anderson et al.（1995）が AI を個別チュータリングシステムとして設計
- **Open Educational Resources（OER）+ AI**：オープン教材を AI と組み合わせて対話的ナレッジシステムとする現代的トレンド

### 8.2 Tiger AI への貢献

本方法論自体がこの理論の**実践ケース**：

- repo + AGENTS.md = **実行可能ナレッジアーティファクト**
- AI 共読チューター = 成人プロフェッショナル教育に適用される**適応的 ITS**
- 方法論と対話する顧客 = カスタマイズ OER

完全議論については [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) 参照。

### 8.3 参考文献

- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society*. Harvard University Press.

---

## 9. 7 理論がどう協力するか：Tiger AI の統合モデル

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   [Capability Maturity]  ────►  L1-L5 構造化スコアリング         │
│         │                                                        │
│         ▼                                                        │
│   [Absorptive Capacity] ────►   企業が吸収で異なる理由           │
│         │                                                        │
│         ▼                                                        │
│   [Task-Technology Fit] ────►  どのタスクがどの L で？           │
│         │                                                        │
│         ▼                                                        │
│   [Dynamic Capabilities]────►  L3-L5 は単なる自動化ではなく      │
│         │                       適応能力の構築                   │
│         ▼                                                        │
│   [Sociotechnical Trust]────►  真の人間-AI 協働チャレンジ        │
│         │                       （trust、accountability）        │
│         ▼                                                        │
│   [Real Options]        ────►  不確実性下の L4-L5 戦略投資       │
│         │                       を正当化                         │
│         ▼                                                        │
│   [AI-Native Living Book]──►   方法論自体が実行可能              │
│                                                                  │
└────────────────────────────────────────────────────────────────┘

7 理論は孤立した層ではなく完全なチェーン：
scoring → absorption → matching → adaptation → trust → investment → execution
```

---

## 10. 学術提出推奨事項

これら 7 理論ごとに、複数の論文が派生可能：

| 論文タイトル（提案）| 主要理論 | ターゲットジャーナル |
| --- | --- | --- |
| A GenAI Adoption Maturity Model: Extending BPM Maturity for the LLM Era | Capability Maturity + AI-native | MIS Quarterly / Information Systems Research |
| Absorptive Capacity in Enterprise AI Adoption: Empirical Evidence from 7 Industries | Absorptive Capacity | Strategic Management Journal |
| Task-Technology Fit Beyond Routine Work: When Should Departments Adopt L4-L5 Agents? | TTF | Information & Management |
| From Automation to Dynamic Capability: How AI Reshapes Organizational Sensing | Dynamic Capabilities | Strategic Management Journal |
| Algorithm Aversion in Workflow Automation: A Mixed-Methods Study | Sociotechnical / Trust | Organization Science |
| Valuing AI Foundation Investments as Real Options | Real Options | SMJ / California Management Review |
| AI-Native Living Books: Methodology as Executable Knowledge Artifact | AI-Native LB | Communications of the ACM |

---

## 11. 完全参考文献

§3-8 で理論ごとの参考文献および完全な参考文献は中国語版を参照。

---

ライセンス & 引用

本ドキュメントは Apache License 2.0；[`../NOTICE`](../NOTICE) 帰属が保持されることを条件に、使用、修正、商業化可能。
