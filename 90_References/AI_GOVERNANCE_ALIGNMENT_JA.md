# AI Governance Alignment：Tiger AI 方法論 vs 国際 AI Governance フレームワーク

> 🌐 言語：[繁體中文](AI_GOVERNANCE_ALIGNMENT.md) ｜ [English](AI_GOVERNANCE_ALIGNMENT_EN.md) ｜ [Deutsch](AI_GOVERNANCE_ALIGNMENT_DE.md) ｜ [Français](AI_GOVERNANCE_ALIGNMENT_FR.md) ｜ [Español](AI_GOVERNANCE_ALIGNMENT_ES.md) ｜ 日本語 ｜ [한국어](AI_GOVERNANCE_ALIGNMENT_KR.md)
>
> Apache License 2.0 · 著者：Morris Lu · Tiger AI

最終更新：2026-05-16

---

> **本ドキュメントが答えるもの**：Tiger AI 方法論はどう国際 AI Governance フレームワーク（NIST AI RMF / EU AI Act / ISO/IEC 42001 / OECD AI Principles / Taiwan AI Basic Act / Singapore Model AI Governance）にマップするか？取締役会 / コンプライアンス / 規制当局は各フレームワークで具体的な着地点を必要とする。
>
> BPM / コンサルティング / AI-Maturity アライメントは [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) に。**本ドキュメントは AI Governance にフォーカス**、特に L4-L5 制度的信頼性。

---

## 1. なぜ L4-L5 に正式な AI Governance Alignment が必要か

L4 Autonomous Agent + L5 Multi-Agent Organization = AI がリアルタイム人間スーパービジョンなしでビジネスアクションを実行。

取締役会 / 規制当局は 3 つの必須質問を問う：

1. **誰が責任を負うか**？AI が失敗した時、誰が法的 / 倫理的に責任を負うか？
2. **どんな Early-Warning メカニズム**？高リスク決定に対し、何が人間介入をトリガーするか？
3. **どう監査されるか**？第三者が独立して AI 行動を検証できるか？

回答は取締役会、コンプライアンス、規制当局に受け入れられるよう、**国際的に認知されたガバナンスフレームワーク**にマップしなければならない。

---

## 2. 8 段階 × メインストリーム AI Governance フレームワーク

| ガバナンスフレームワーク | ソース / 性質 | カバーされる Tiger AI 段階 |
| --- | --- | --- |
| **NIST AI RMF** | US NIST、2023 / 任意だが広く採用 | Govern→Stage 8；Map→Stage 1-2；Measure→Stage 4+8；Manage→Stage 6-8 |
| **EU AI Act** | EU、2024 / 強制規制 | High-risk AI は L4-L5 にマップ；透明性→Stage 8 Audit；HITL→全段階 |
| **ISO/IEC 42001:2023 AI Management System** | ISO、2023 / 認証可能 | AI policy→Stage 8；risk→Stage 4+8；継続的改善→Phase C |
| **ISO/IEC 23894:2023 AI Risk Management** | ISO / リスクフォーカス | Risk Register→Stage 8 |
| **OECD AI Principles** | OECD+加盟国 / ポリシー原則 | 5 原則 → Tool 7.2 + 8.8 |
| **Taiwan AI Basic Act（草案）** | Taiwan 立法院、審議中 | Taiwan ハイコンプライアンス顧客にマップ |
| **Singapore Model AI Governance Framework** | IMDA / 任意 | 4 pillars → Stage 7 To-Be + Stage 8 |
| **US AI Bill of Rights** | ホワイトハウス / ポリシーステートメント | 5 保護 → Tool 8.8 Ethics + 顧客データ保護 |

---

## 3. NIST AI RMF（最重要グローバルリファレンス）

NIST AI RMF は**最も広く採用された** AI Governance フレームワーク。4 つのコア機能：

### 3.1 Govern

**NIST が要求**：org-level AI policy、役割、責任、文化。

**Tiger AI**：Stage 8 §12.1 RACI マトリクス；Tool 8.8 AI Ethics チェックリスト 15 項目；4 層アーキテクチャ Layer 1 Governance（Policy / Ethics / Compliance / Risk Committee / Audit Owner）；Tool 3.6 顧客 3 者署名 = corporate-level 書面コミットメント。

### 3.2 Map

**NIST が要求**：AI システムコンテキスト、リスク、ステークホルダーのインベントリ。

**Tiger AI**：Stage 1 As-Is（インタビュー、Systems Inventory、AI Usage Inventory、Swimlane）；Tool 2.2 RM Mapping；Tool 2.6 + 2.7 Component Map + 4 層。

### 3.3 Measure

**NIST が要求**：AI システムパフォーマンス、インパクト、リスクを定量化。

**Tiger AI**：Stage 2 レーダー 0-4 スコアリング；Stage 4 Impact × Effort；Stage 8 Tool 8.5 Value Tracking Matrix（5 次元）；Tool 8.9 Evidence Hierarchy（L1-L5 evidence strength）；四半期 Gate C レーダー再訪。

### 3.4 Manage

**NIST が要求**：リスク緩和、モニタリング、継続的改善。

**Tiger AI**：Stage 6 Phased Goals + Stage Gate Criteria；Stage 7 Human-AI Collaboration + HITL ノード；Stage 8 Tool 8.6 Risk Register；Tool 8.7 Audit Log；Phase C 24 ヶ月四半期レビュー。

> **総合**：NIST AI RMF 4 機能は Tiger AI 8 段階に完全に着地、**NIST コンプライアンスドキュメントを直接生成**。

---

## 4. EU AI Act（強制規制）

EU AI Act は AI を 4 つのリスク tier に分類：Unacceptable / High-risk / Limited / Minimal。

### 4.1 リスク分類マッピング

| EU AI Act Tier | Tiger AI L-level | 必要なガバナンス |
| --- | --- | --- |
| **Unacceptable**（social scoring、real-time biometric ID 等）| ❌ Tiger AI **支援を拒否** | — |
| **High-risk**（HR、credit、medical、education、judicial、critical infrastructure）| 主に L4-L5 シナリオ | 強制リスクアセスメント + 透明性 + human oversight + post-market monitoring |
| **Limited**（chatbots、deepfake）| 主に L1-L3 シナリオ | 透明性義務（「AI-generated」マーク）|
| **Minimal**（spam filtering 等）| 主に L1-L2 シナリオ | 一般義務 |

### 4.2 High-Risk AI Article Alignment

| EU AI Act Article | Tiger AI Mapping |
| --- | --- |
| **Art. 9 Risk Management System** | Stage 8 Tool 8.6 Risk Register |
| **Art. 10 Data Governance** | Tool 8.7 Audit Log + Tool 8.4 Permission Matrix |
| **Art. 11 Technical Documentation** | 完全 14 セクションコンサルレポート + 4 層アーキテクチャドキュメント |
| **Art. 12 Record-Keeping（logs）** | Tool 8.7 Audit Log 7 event types |
| **Art. 13 Transparency** | Tool 8.8「AI-generated マーキング」 + 公的 Ideal Practice 署名 |
| **Art. 14 Human Oversight** | Tool 7.2 Human-AI Collaboration + HITL ノード + Reviewer Workflow |
| **Art. 15 Accuracy, Robustness, Cybersecurity** | Stage 8 Tool 8.5 Value Tracking（quality dim）+ Audit Log + Security |
| **Art. 17 Post-Market Monitoring** | Phase C 四半期 Gate C + Stage 2 レーダー再訪 + 5 次元 value tracking 縦断 |
| **Art. 26 Quality Management System** | ISO/IEC 42001 アライメント（§5 参照）|
| **Art. 72 Serious Incident Reporting** | Tool 8.8 Ethics §11「AI system incident response」|

> **EU 業務を持つ顧客**：Tiger AI 方法論デリバラブル（完全 14 セクションレポート + ガバナンスドキュメント）は EU AI Act コンプライアンスエビデンスパッケージとして機能。

---

## 5. ISO/IEC 42001:2023 AI Management System

ISO 42001 は最初の**第三者認証可能な** AI management system 標準。構造は ISO 9001 / 27001 を反映。

### 5.1 ISO 42001 セクションマッピング

| ISO 42001 Section | Tiger AI Mapping |
| --- | --- |
| **4. Context of the Organization** | Stage 1 As-Is + Stage 2 Reference Model |
| **5. Leadership** | Sponsor + AI Champion 役割定義（RACI）+ AI Policy 署名 |
| **6. Planning** | Stage 5 Problem Definition + Stage 6 Phased Goals + Tool 6.3 Absorption |
| **7. Support** | Change Management Playbook + トレーニング計画 + リソース計画 |
| **8. Operation** | Stage 7 To-Be Operating Model + Human-AI Collaboration + HITL |
| **9. Performance Evaluation** | Tool 8.5 Value Tracking Matrix + Tool 8.7 Audit Log + 四半期 Gate C レーダー |
| **10. Improvement** | Phase C 四半期レビュー + Cases-as-Benchmarks 蓄積 |
| **Annex A Controls** | Tool 8.4 Permission + Tool 8.6 Risk + Tool 8.7 Audit + Tool 8.8 Ethics |

> **目標**：ISO/IEC 42001 認証を追求する企業は Tiger AI デリバラブルを management-system ドキュメンテーションとして使用可能。Tiger AI は **ISO 42001 全セクションを完全カバー**。

---

## 6. OECD AI Principles（5 原則）

OECD AI Principles は G20、APEC により広く採用。

| OECD 原則 | Tiger AI Mapping |
| --- | --- |
| **1. Inclusive growth, sustainable development and well-being** | Stage 8 Tool 8.5 Value Tracking が「employee experience」を含む；Change Management が「役割アップグレード、置換ではない」を含む |
| **2. Human-centered values and fairness** | Tool 8.8 Ethics §9 bias / discrimination assessment；Tool 7.2 HITL 必須 |
| **3. Transparency and explainability** | Tool 8.7 Audit Log + Tool 8.8 §7「AI-generated マーキング」 + 完全 evidence trail |
| **4. Robustness, security and safety** | Stage 8 Risk Register + Tool 8.4 Permission + デプロイメントモード（Hybrid / On-Prem 3 オプション）|
| **5. Accountability** | RACI マトリクス + 「**顧客署名済み Ideal Practice 3 者署名**」 + Reviewer sign-off |

---

## 7. Taiwan AI Basic Act（草案）

Taiwan 立法院 AI Basic Act 審議中（2026/05 時点）。Tiger AI 方法論は**主要条項と整合**：

| 草案ハイライト | Tiger AI Mapping |
| --- | --- |
| **AI 製品/サービスにリスクグレーディングが必要** | Stage 1-2 識別 + 4 層アーキテクチャ + Tool 8.6 Risk Register |
| **モデルトレーニング上の PII 保護** | Tool 8.8 §2 PII を LLM に送らない / redacted；高センシティビティはデプロイメントデフォルト on-prem |
| **アルゴリズム透明性と説明可能性** | Tool 8.7 Audit Log + 8.8 §7 AI マーキング |
| **ユーザー権利保護** | Tool 8.8 §5 従業員は仕事が AI 処理されたことを知る権利を持つ |
| **オペレーター Accountability** | RACI + Tool 8.8 §8 IP 帰属 |
| **政府規制権限** | Tool 8.7 Audit Log retention が政府監査をサポート |

⚠️ Taiwan AI Basic Act 未成立。本アライメントは最終テキストで更新。

---

## 8. Singapore Model AI Governance Framework

Singapore IMDA 任意フレームワーク、4 pillars：

| Singapore Pillar | Tiger AI Mapping |
| --- | --- |
| **1. Internal Governance Structures** | Layer 1 Governance + RACI |
| **2. Determining Level of Human Involvement** | Tool 7.2 Human-AI Collaboration（HITL ノード）|
| **3. Operations Management** | Tool 8.4-8.7 完全セット（Permission / Value / Risk / Audit）|
| **4. Stakeholder Interaction & Communication** | Tool 8.2 Change Management Playbook + Stakeholder Map |

---

## 9. 規制 / コンプライアンスデリバラブル Map

顧客が規制 / コンプライアンス / 内部監査に直面する時、どの Tiger AI デリバラブルを直接提出可能か：

| 規制ニーズ | 直接 Tiger AI デリバラブル |
| --- | --- |
| AI リスクアセスメント | Stage 4 Gap + Tool 8.6 Risk Register |
| AI policy | Tool 8.8 Ethics チェックリスト 15 項目 + AI Policy ドキュメント |
| Audit evidence package | Tool 8.7 Audit Log + 四半期 Gate C ログ + Stage 2 レーダー before/after |
| 第三者監査準備 | 完全 14 セクションレポート + 4 層アーキテクチャ + 4 権威ドキュメント |
| ROI / 利益実証 | Tool 8.5 Value Tracking 5 次元 + 縦断 KPI |
| インシデント対応フロー | Tool 8.8 §12 + Tool 8.6 Risk Register トリガー |
| 従業員トレーニング記録 | Change Management トレーニング記録 + Tool 8.8 §14 |

---

## 10. 認証 / Labeling 推奨

方法論成熟度に基づき、Tiger AI 顧客は以下を検討可能：

| 認証 | 対象 | 推定タイムライン |
| --- | --- | --- |
| **ISO/IEC 42001 AI Management System** | L3+ 顧客（完全ガバナンス付）| 6-12 ヶ月 |
| **ISO/IEC 27001 ISMS** | 全顧客（セキュリティベースライン）| 6-12 ヶ月 |
| **SOC 2 Type II** | US / 多国籍サービス顧客 | 6-12 ヶ月 |
| **EU AI Act CE Marking**（High-risk）| EU 業務 + High-risk AI システム | 12-24 ヶ月 |

> Tiger AI デリバラブルは**認証ドキュメンテーションベースの 90%** として機能。実際の認証は第三者監査が必要。

---

## 11. 関連ドキュメント

| ドキュメント | 関係 |
| --- | --- |
| [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | コンサルティングファーム / BPM / AI maturity フレームワークと整合；本ドキュメントは AI Governance を追加 |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | なぜ方法論が議論に耐えるか |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | 方法論 failure modes & counter-cases |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Stage 8 | 完全ガバナンスツールキット |

---

## 12. 参考文献

- NIST (2023). *AI Risk Management Framework (AI RMF 1.0)*.
- European Commission (2024). *Regulation on Artificial Intelligence (EU AI Act)*.
- ISO/IEC (2023). *ISO/IEC 42001:2023 — AI Management System*.
- ISO/IEC (2023). *ISO/IEC 23894:2023 — AI Risk Management*.
- OECD (2019, updated 2024). *OECD AI Principles*.
- The White House (2022). *Blueprint for an AI Bill of Rights*.
- Singapore IMDA (2020). *Model AI Governance Framework, 2nd Edition*.
- 立法院（審議中）. *Taiwan Artificial Intelligence Basic Act Draft*.

---

ライセンス & 引用

本ドキュメントは Apache License 2.0；[`../NOTICE`](../NOTICE) 帰属が保持されることを条件に、使用、修正、商業化可能。
