# Tiger AI 方法論と業界フレームワークのアライメント

> 🌐 言語：[繁體中文](INDUSTRY_FRAMEWORK_ALIGNMENT.md) ｜ [English](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) ｜ [Deutsch](INDUSTRY_FRAMEWORK_ALIGNMENT_DE.md) ｜ [Français](INDUSTRY_FRAMEWORK_ALIGNMENT_FR.md) ｜ [Español](INDUSTRY_FRAMEWORK_ALIGNMENT_ES.md) ｜ 日本語 ｜ [한국어](INDUSTRY_FRAMEWORK_ALIGNMENT_KR.md)
>
> Apache License 2.0 · 著者：Morris Lu · Tiger AI

最終更新：2026-05-15

---

> **この文書が答えるもの**：Tiger AI 方法論はメインストリームコンサルティングファーム（McKinsey / BCG / Bain / Deloitte / Accenture / PwC）、学術学派（Rosemann BPM / CMMI / APQC / SCOR / TOGAF / Dragon1）、AI 成熟度フレームワーク（Gartner / MIT / MMC / Forrester）とどう関連するか？何を重複、補完、革新するか？
>
> **コアスタンス**：Tiger AI は車輪を再発明するのではなく、**メインストリームツールを統合し、業界クローズドループを補完し、GenAI 時代のエッセンシャルを追加する**。引用されたすべてのフレームワークは [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md) に詳述；本文書はファーム間でマッピング。

---

## 1. なぜこのアライメントが重要か

| オーディエンス | 得るもの |
| --- | --- |
| 大企業 IT/CIO | 「この方法論は既存の TOGAF / ITIL / APQC と互換」 |
| 他ファームのコンサルタント | 「BCG/Deloitte 出身 — どのツールを使い続けるか、どれが Tiger AI 特有かが分かる」 |
| 学術レビュアー | 「Tiger AI は周縁科学ではない — Rosemann/CMMI/APQC 学派の肩の上に立つ」 |
| 規制当局 | 「引用された標準は国際的に認められている；AI ガバナンスは既存 GRC フレームワークにマップ」 |
| クライアント幹部 | 「我々が支払うのは業界ベスト + GenAI 時代の補完、単一ファーム独自の方法ではない」 |

---

## 2. 8 ステージ vs. メインストリームコンサルティングファーム

### 2.1 クロスファームアライメントテーブル

| ステージ | Tiger AI | McKinsey | BCG | Bain | Deloitte | Accenture | PwC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1 As-Is Snapshot** | 40-Q インタビュー + Inventory + Swimlane | 7-Step Step 1: Define Problem | Diagnostic Survey | Customer / Process Diagnostics | Business Architecture Discovery | Living Business Diagnostic | Value Creation Diagnostic |
| **2 Reference Model** | APQC + Tiger AI L1-L5 + 4 層 | （稀にしか行われない）| Capability Maturity Map | （非コア）| TOGAF Capability Assessment | Industry Reference Architecture | Capability Framework |
| **3 Best Practice → Ideal** | Benchmark + Ideal Practice Workshop | Best Practice Research | Strategic Position vs Industry | NPS / Customer Loyalty | Industry Pulse | Industry Benchmarking | Industry Outlook |
| **4 Gap Analysis** | M/B/R + Impact×Effort | Issue Tree + MECE | Importance-Performance Map | Pareto + Lean | Capability Gap Heatmap | Maturity Gap Analysis | Gap Map |
| **5 Problem Definition** | 80/20 + 5 Whys + EPS | Day-1 + SCQ + Pyramid | Strategic Diagnosis | Bain Question Pyramid | Hypothesis-Driven | Outcome-Driven | Issue-Tree Synthesis |
| **6 Phased Goals** | Phased + Absorption | Workplan + Critical Path | Phased Transformation | Bain Way Multi-phase | Imagine-Deliver-Run | Wave Planning | Transformation Wave |
| **7 To-Be Design** | Phased To-Be + Human-AI | To-Be Operating Model | Operating Model Design | Bain Way (Org) | Target Operating Model | Future-State Blueprint | Future Operating Model |
| **8 Implementation & Change** | Roadmap + Change + Value Tracking | Influence Model + 7S | Smart Simplicity | Bain Results Delivery | Diamond Performance | Wired for Change | Project Delivery |

### 2.2 各ファームが何を貢献するか

- **McKinsey** MECE / Pyramid / Issue Tree は **Tiger AI Stage 4-5 ツールのソース**（Frameworks Library に収録）
- **BCG** Capability Maturity 思考は **Tiger AI Stage 2 RM スコアリングを啓発**
- **Bain** Customer / Process Diagnostics は **Tiger AI Stage 1 インタビューバンクを補完**
- **Deloitte** Imagine-Deliver-Run は **Tiger AI Stage 6 3 フェーズと高度に一致**
- **Accenture** Wave Planning は **Tiger AI Phase 1/2/3 と一致**
- **PwC** Value Creation Diagnostic は **Tiger AI Stage 8 value tracking にマップ**

> **結論**：8 ステージのいずれも Tiger AI の「発明」ではない。**革新は、これら分散したツールをデータ依存、クライアント署名、クローズドループ反証を持つ完全な推論チェーンに統合することにある**。

---

## 3. Reference Model 学派アライメント

### 3.1 Tiger AI 4 層 vs. 主要 EA フレームワーク

| 層 | Tiger AI | Dragon1 EA | TOGAF ADM | Zachman | ArchiMate |
| --- | --- | --- | --- | --- | --- |
| **L1 Governance** | AI Governance | Enterprise Governance | (Architecture Vision) | Scope | Motivation + Strategy |
| **L2 Business** | AI Business（L1-L5 はここ）| Business(es) | Business Architecture (B) | Business | Business Layer |
| **L3 Information** | AI Information | Information Facilities & Systems | Data + Application (C+D) | System | Application + Information |
| **L4 Technical** | AI Technical | IT Infrastructure(s) | Technology (E) | Technology | Technology + Implementation |

**なぜこのアライメント**：すべてのメインストリーム EA フレームワークは「**4 抽象層**」に収束する — 偶然ではなく、「抽象 × 揮発性」科学的軸の必然的結果（[`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) §5 参照）。

### 3.2 Process Reference Model アライメント

| ユースケース | Tiger AI 推奨 | APQC PCF | SCOR | eTOM | ITIL | CMMI |
| --- | --- | --- | --- | --- | --- | --- |
| **業界横断プロセス** | APQC PCF（デフォルト）| ✓ 13 Cat | — | — | — | — |
| **サプライチェーン / 製造** | SCOR | — | ✓ 6 セクション | — | — | — |
| **テレコム / サブスクリプション** | eTOM | — | — | ✓ 3 レベル | — | — |
| **IT サービス管理** | ITIL | — | — | — | ✓ 5 フェーズ | — |
| **ソフトウェア成熟度** | CMMI | — | — | — | — | ✓ 5 レベル |
| **AI 採用成熟度** | **Tiger AI L1-L5（DIY、業界ギャップを埋める）** | — | — | — | — | — |

> **既存の業界 RM は AI 採用をカバーしていない** — したがって Tiger AI L1-L5 の必要性、Tool 2.5 スコア 9/10 で自己認定。

### 3.3 BPM Maturity 学派ルーツ

| 概念 | ソース | Tiger AI マッピング |
| --- | --- | --- |
| Capability Maturity Levels（5 階層スケール）| **Rosemann BPM Maturity**（QUT）+ CMMI | Stage 2 0-4 スコアリング、Tiger AI L1-L5 |
| Process Excellence Characteristics | Rosemann + APQC | Stage 3 Excellence Capability Profile |
| Stage Gates | CMMI + Rosemann | Stage 6 acceptance gates |
| Organizational Absorption | Rosemann（新興研究）| Tool 6.3 Absorption Assessment |

> **謝辞**：Prof. Michael Rosemann（QUT）は著者の修士アドバイザー；本方法論の BPM 学派ルーツは彼の長期メンターシップから直接来ている。

---

## 4. AI 成熟度フレームワークアライメント

### 4.1 主要 AI 成熟度フレームワークマッピング

| フレームワーク | レベル | Tiger AI L1-L5 マッピング |
| --- | --- | --- |
| **Gartner AI Maturity Model** | Awareness / Active / Operational / Systemic / Transformational | L1 / L1+L2 / L3 / L4 / L5 |
| **MIT Sloan AI Capability** | Experimenters / Investigators / Pioneers / Empowerment | L1-L2 / L2-L3 / L3-L4 / L5 |
| **McKinsey AI Quotient (AIQ)** | （連続スケール、4 ドライバー）| Tiger AI 6 次元レーダーにマップ |
| **Capgemini DELTA Maturity** | Data / Enterprise / Leadership / Targets / Analysts | ガバナンス + デプロイ軸にマップ |
| **Forrester AI Pulse Index** | （3 リング：People / Process / Tech）| Tiger AI 4 層アーキテクチャにマップ |
| **Tiger AI L1-L5** | L1 Chat / L2 Skill / L3 Workflow / L4 Auto Agent / L5 Agent Team | （**スケール軸 L1-L3 + AI 自律軸 L4-L5**）|

### 4.2 Tiger AI L1-L5 のメインストリームへの追加

| 追加 | なぜ業界に欠けているか | Tiger AI が埋める |
| --- | --- | --- |
| **明示的ツールマッピング** | Gartner/MIT はレベルを抽象的に記述、ツールランディングなし | L1=OpenWebUI、L2=Antigravity、L3=n8n、L4=Hermes、L5=ClawTeam |
| **スケール軸と自律軸の分離** | 業界はそれらを混合、L4-L5 を曖昧にする | スケール（人間主導）vs 自律（AI 主導）、重要境界 L3→L4 |
| **GenAI 特化（伝統的 ML ではなく）** | ほとんどのフレームワークは伝統的 ML / 予測モデルに留まる | LLM / Agent / Workflow パラダイムに完全集中 |
| **検証可能なステージアクセプタンス** | 業界フレームワークは主に自己評価スケール | 各レベルに Stage Gate Criteria、独立検証可能 |
| **クロス RM デュアル座標** | 業界フレームワークは単軸 | Tiger AI は業界 RM（APQC/SCOR）に直交、デュアルレーダー |

---

## 5. クラシック分析ツールアライメント

[`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md) に詳述。サマリー：

### 5.1 戦略ツール

Porter's 5 Forces (Stage 3)、PESTEL (Stage 3)、BCG Growth-Share (Stage 3)、SWOT (Stage 3/4)、Blue Ocean (Stage 7)、Wardley Map (Stage 6/7)。

### 5.2 問題分析ツール

MECE (Stage 2/4)、Issue Tree (Stage 4/5)、Pyramid Principle (Stage 5)、SCQ (Stage 5)、5 Whys (Stage 5)、Fishbone (Stage 4/5)、Hypothesis-Driven (Stage 1-5)、80/20 (Stage 5)。

### 5.3 Change Management ツール

Kotter 8 Steps (Stage 8)、ADKAR (Stage 8)、Stakeholder Map (Stage 8)、RACI (Stage 8)、Influence Model (Stage 8)、7S (Stage 2/8)。

### 5.4 財務 / ROI ツール

NPV/IRR (Stage 8)、Payback (Stage 8)、Break-Even (Stage 8)、Sensitivity Analysis (Stage 8)、Balanced Scorecard (Stage 8)、OKR (Stage 6/8)。

---

## 6. Tiger AI ユニーク / 革新的要素

ほとんどのツールは業界から来るが、Tiger AI には以下の **ユニークな統合または革新** がある：

| 革新 | なぜ業界に欠けているか | Tiger AI デザイン |
| --- | --- | --- |
| **Tiger AI L1-L5 GenAI Adoption RM** | 業界 RM はまだ IT / 伝統的 ML | LLM/Agent/Workflow 専用に設計された最初の RM、Tool 2.5 10 条件のうち 9/10 を満たす |
| **Client Ideal Practice Co-Creation Workshop** | 業界は Best Practice ベンチマーキングを行うが、稀にしかクライアント署名 Ideal を行わない | Tool 3.6：クライアントが **自分で署名**、後続推論を否定できない |
| **Cases-as-Benchmarks 9 フィールドフォーマット** | 業界ケースはほとんど叙述的、ギャップ計算なし | Tool 3.5：ケースは必須的に 9 フィールドを持つ、クライアントが 30 分で自己計算 |
| **四半期 Stage 2 Radar ループバック** | 業界 Roadmap はほとんど線形、自己反証メカニズムなし | Phase C 毎四半期 Gate C が必須的にレーダーを再訪、構造が実際により丸いことを検証 |
| **3 フェーズ契約モデル + Gate A/B/C 出口** | 業界はほとんど fixed-scope 大型契約 | Phase A diagnostic / Phase B strategy / Phase C implementation、クライアントが決定をフェーズ化 |
| **スケール軸 vs AI 自律軸の直交** | 業界は一軸で混合 | L1-L3 スケール + L4-L5 自律、重要 L3→L4 境界 |
| **4 層 RM × L1-L5 デュアル座標** | 業界は単軸（RM または成熟度のいずれか）| Tiger AI はデュアル軸クロスマッピングを義務付け |
| **プロセスごとの明示的 HITL ノード** | 業界はガバナンスを語るが、稀にしか HITL 位置を指定しない | Tool 7.2 各プロセスに HITL ノード + acceptance criteria が明示的にマーク |

---

## 7. 一般的なクライアント質問：これは我々の方法論と衝突するか？

### 7.1 クライアントが TOGAF / Zachman を使用

**衝突なし**。Tiger AI 4 層は **TOGAF BDAT**（Business/Data/Application/Technology）と直接一致。「我々は貴社の既存 TOGAF アーキテクチャの上に構築し、GenAI 採用次元（L1-L5）と四半期レーダークローズドループを追加します。」と言う。

### 7.2 クライアントが ITIL を使用

**衝突なし**。Tiger AI Stage 8 Audit Log / Permission Matrix / Risk Register は ITIL Service Operation に直接接続。「GenAI 特化の LLM コールログ、Reviewer シミュレーション、Skill バージョンガバナンスを補完します。」と言う。

### 7.3 クライアントが CMMI を使用

**衝突なし**。Tiger AI L1-L5 と CMMI 5 レベルは **親族** — 両方とも maturity capability 学派拡張。「CMMI for AI は新興方向；Tiger AI L1-L5 は一つのランディングバージョンです。」と言う。

### 7.4 クライアントが BCG / McKinsey / Bain 内部フレームワークを使用

**衝突なし、相互強化**。Tiger AI はこれらのファームのコアツール（Issue Tree、MECE、Pyramid、Bain Way）を引用。「貴社の戦略コンサルティング方法論を置き換えるのではなく、GenAI 採用クローズドループと 4 層 Reference Model を追加します。」と言う。

### 7.5 クライアントが Gartner / Forrester AI Maturity を使用

**衝突なし、より具体的**。Tiger AI L1-L5 は Gartner の 5 レベルより **より具体的なランディングツール**（L1=OpenWebUI など）を持つ。「Gartner は『Operational AI』と言いますが、我々は『n8n Workflow 3 ライブ + Reviewer サインオフ率 95%』と言います。」と言う。

---

## 8. 学術引用アライメント

各ファイル References に引用。選定：

### 8.1 BPM / Maturity 学派

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT. **（コア理論ルーツ）**
- Paulk, M. et al. (1993). *Capability Maturity Model for Software*. CMU/SEI.
- Curtis, B. et al. (2009). *People CMM*.

### 8.2 Reference Model / Enterprise Architecture

- APQC (2024). *Process Classification Framework Version 7.3*.
- APICS / ASCM. *SCOR Reference Model*.
- TM Forum. *eTOM Business Process Framework*.
- ISACA. *COBIT / ITIL Framework*.
- The Open Group. *TOGAF Standard 9.2*.
- Zachman, J. *Zachman Framework*.
- Dragon1. *Enterprise Architecture Reference Model*.

### 8.3 コンサルティング方法論

- Minto, B. (2009). *The Pyramid Principle*.
- Rasiel, E. (1999). *The McKinsey Way*.
- Bain & Company. *Bain Way / Results Delivery*.
- Iansiti, M., Lakhani, K. (2020). *Competing in the Age of AI*.

### 8.4 Change Management

- Kotter, J. (1996). *Leading Change*.
- Hiatt, J. (2006). *ADKAR*. Prosci.
- Mendelow, A. (1991). *Stakeholder Mapping*.

### 8.5 GenAI 戦略

- Gartner. *AI Maturity Model*.
- Davenport, T., Mittal, N. (2022). *All-in on AI*.
- Brynjolfsson, E., McAfee, A. (2014). *The Second Machine Age*.

---

## 9. クロージング：巨人の肩の上に立つ + 業界クローズドループの補完

Tiger AI 方法論設計哲学：

1. **車輪を再発明しない**：戦略分析（McKinsey）、change mgmt（Kotter）、財務ツール（NPV/IRR）、EA フレームワーク（TOGAF/Dragon1）— 業界のベストを使う
2. **統合 + クローズドループ**：分散したツールをデータ依存、クライアント署名、反証メカニズムを持つ完全な推論チェーンに結ぶ
3. **GenAI ギャップを埋める**：業界フレームワークは LLM/Agent/Workflow 時代に追いついていない → Tiger AI L1-L5 + 4 層 + Cases-as-Benchmarks + HITL デザインがそれを埋める
4. **他者による再現可能**：Apache 2.0 + GitHub + 明確な学術引用 → どのファームの私的資産でもない

> **これが「巨人の肩の上に立つ + 業界クローズドループの補完」の意味** — クライアントが買うのは業界ベスト統合 + GenAI 時代補完、単一ファームの独自方法ではない。

---

## 10. 関連ドキュメント

| ドキュメント | 関係 |
| --- | --- |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) §8 | 本ドキュメント §2 のコンパクトバージョン（vs McKinsey/BCG/Gartner/MIT）|
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | 8 ステージが実際のエンゲージメントでどのように走るか |
| [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md) | 50+ フレームワーク詳述（本ドキュメント = アライメントマップ；そのファイル = フレームワーク辞典）|
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | ステージごとのツールテーブル |

---

ライセンス & 引用

本ドキュメントは Apache License 2.0；[`../NOTICE`](../NOTICE) 帰属が保持されることを条件に、使用、修正、商業化可能。
