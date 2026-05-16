# 04 Scenarios — シナリオ、ケース & ケースインデックス

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

> ⚠️ **重要な学術誠実性声明 / Important Academic Integrity Disclaimer**
>
> **本ディレクトリの 7 個の SAMPLE_CLIENT_CASE_*.md ケース（Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education）と名指しされた主人公（例：`00_Overview/CLIENT_JOURNEY_STORY.md` の Ming）は、すべて AI 生成の架空ケースであり、実際の顧客データではありません。**
>
> - **用途**：教育デモ、方法論説明、Stage 1-8 ツール表応用練習
> - **制限**：すべての数字（時間、ROI、人月、予算、KPI）は例示のみ、**対外宣伝、契約上の約束、学術的実証エビデンスとして使用してはならない**
> - **エビデンスレベル**：[`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 8.9 に従い、本ディレクトリのケースは **L0（AI-Simulated Teaching Case）**、L1 自己評価問卷より低い
> - **実際の longitudinal ケース** は [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) の 18-24 ヶ月実証研究完了後のみ置き換え

## 1. 本ディレクトリの位置づけ

本ディレクトリは方法論全体の**素材ライブラリとエビデンスライブラリ**です。`01`-`03`、`05`、`06` は「方法とプロセス」；本ディレクトリは「**方法論の実装に実シナリオ、ケース、選択可能ケースを提供**」。

解決する課題：**AI 導入の最大障害は「やり方が分からない」ではなく、「何ができるか、他者がどうやっているか、導入後どうなるか分からない」。** 本ディレクトリは 4 種類の素材を提供：(1) 役割/部門別の**シナリオストーリー**（顧客の「自己投影」）、(2) ケースの**書き方標準と制御表**（コンサルが一貫ケース書く）、(3) 7 業界の**完全デモケース**（問卷から Roadmap まで）、(4) 150+ 実 LLM 応用の**ケースインデックス**（L レベルと部門の 2 軸で即座検索）。

本ディレクトリを使う人：コンサル（Discovery でシナリオ・ケースインデックスで PoC 選定）、Sales（ケースで価値裏付け）、講師（ケースをデモ題に）、顧客（完全ケースで「導入後どうなる」理解）。

## 2. 方法論における位置

| 軸 | 対応 |
| --- | --- |
| 3 段階サービスフロー | **全工程横断** — Discovery でシナリオ使用、Build でケースを題に、Deliver でケース裏付け |
| 8 段階コンサル構造 | 主に **Stage 1 As-Is Snapshot（現状シナリオ）、Stage 3 Best Practice Integration（業界ベスト実践ベンチマーク）** をサポート |
| L1-L5 成熟度 | ケースインデックスが各ケースを L レベルにマッピング |
| Engagement Lifecycle | Sales（Discovery 自己投影）+ Build（デモ題） |

## 3. 目標 & 効果

| 目標 | 効果 |
| --- | --- |
| 役割/部門別シナリオストーリー提供 | 顧客が「自己投影」可能、Discovery がより速く焦点 |
| ケース書き方標準と制御表 | コンサルが構造一貫・検証可能ケース作成 |
| 7 業界完全デモケース | 顧客が「導入後の全景」を見る；新人コンサルにテンプレ |
| 150+ LLM 応用インデックス（2 軸検索） | 顧客/コンサルが「L レベル」または「部門」で即座検索 |
| クロスレベル期待管理 | 顧客が L5 ケース指したら、インデックスで「あなたは L2、先に補う必要」と指摘 |

**本ディレクトリ飛ばすと**：顧客が「何ができるか」概念なし、PoC 選定が当てずっぽう、ケース品質不揃い、クロスレベル期待管理不可。

## 4. ワークフロー & ロジック

```text
Discovery 段階
   → CUSTOMER_SCENARIO_LIBRARY（役割別シナリオ、顧客自己投影）
   → LLM_APPS_CASE_INDEX（L レベル + 部門で「顧客に響く」ケース選択）
   → 選定ケース → PoC 候補

講座 / 提案段階
   → SAMPLE_CLIENT_CASE_*（同業界完全ケースを顧客に見せる）
   → LLM_APPS_CASE_INDEX（クラスデモ題、練習題）

コンサルが新ケース執筆時
   → CASE_WRITING_STANDARD（書き方標準）
   → CASE_CONTROL_TABLES（制御表、コピー記入）
```

| ステップ | 誰 | いつ | 入力 | 出力 |
| --- | --- | --- | --- | --- |
| 顧客自己投影 | コンサル | Discovery | シナリオストーリーライブラリ | 顧客が認める痛点 |
| PoC 候補選定 | コンサル | 診断後 | L レベル + 部門 → インデックス | PoC 候補リスト |
| 完全ケース顧客提示 | Sales / コンサル | 提案 | 同業界 sample case | 顧客が全景理解 |
| 新ケース執筆 | コンサル | プロジェクト終了後 | 書き方標準 + 制御表 | 新 sample case |

> ロジック：シナリオストーリーは「**共感誘発**」（顧客が「そう、まさにそれ」と言う）；ケースインデックスは「**素材即選**」（L レベル/部門で即座検索）；完全デモケースは「**全景提示**」（問卷から Roadmap）；書き方標準は「**一貫性保証**」（新ケース品質安定）。

## 5. ファイル説明

### シナリオと標準

| ファイル | 用途 |
| --- | --- |
| `CUSTOMER_SCENARIO_LIBRARY.md` | 役割/部門別シナリオストーリー：CEO、COO、IT、HR と Sales、Customer Service、Marketing、Operations、Finance、HR、IT 部門；各ストーリーに Before、Trigger、AI Flow、Systems、Output、KPI 含む。 |
| `CASE_WRITING_STANDARD.md` | ケース書き方標準、L1-L5 の Input / Process / Output / Evidence と検証可能納品物の書き方を規定。 |
| `CASE_CONTROL_TABLES.md` | ケース制御表、評価活動、L1-L5 IPOE、Evidence、Stage Gate、リスクガバナンス、Deliverables 検収をコピペ可能。 |
| `INDUSTRY_SCENARIOS.md` | 5 業界推奨シナリオ（小売/教育/物流/ソフトウェア/プロフェッショナルサービス）、業界別：紹介、L1-L5 ベースライン、Top-10 シナリオ、リスクガバナンス、30 日 Quick Win、Anti-Patterns。 |

### 完全デモケース（顧客はすべてコードネーム）

| ファイル | ケース |
| --- | --- |
| `SAMPLE_CLIENT_CASE_MANUFACTURING.md` | R&D 製造業完全ケース |
| `SAMPLE_CLIENT_CASE_HOSPITAL.md` | 病院 / 医療機関（高感度データ、フルオンプレ、人手レビュー） |
| `SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md` | マーケティング代理店（コードネーム：代理店 M） |
| `SAMPLE_CLIENT_CASE_B2B_SALES.md` | B2B 工業機器ディーラー（コードネーム：工業機器 B）、RFP・CRM ガバナンス・L5 Pre-RFP Team フォーカス |
| `SAMPLE_CLIENT_CASE_FINANCIAL.md` | 金融業界（コードネーム：地方銀行 F）、フルオンプレ、二重レビュー |
| `SAMPLE_CLIENT_CASE_GOVERNMENT.md` | 政府機関（コードネーム：市デジタル局 G）、フルオンプレ、三重レビュー |
| `SAMPLE_CLIENT_CASE_EDUCATION.md` | 教育機関（コードネーム：テクノロジー大学 E）、Hybrid、学術倫理 |

> 各ケースは完全フロー：問卷結果 → L レベル判定 → 講座比率 → クラス内産出 → 8 段階分析 → 診断レポート要約 → 30/60/90 Roadmap → ROI → リスクガバナンス。

### L5 実装とケースインデックス

| ファイル | 用途 |
| --- | --- |
| `CLAWTEAM_WALKTHROUGH.md` | ClawTeam（HKUDS, MIT）で部門横断 Agent Team 完全 walkthrough（製造業 QA Team）、環境設定、タスクチェーン、Human Gate、Gate 5 マッピング含む。 |
| `LLM_APPS_CASE_INDEX.md` | **LLM 応用ケースインデックス（マルチソース）**。150+ 実 LLM app、**2 つの検索軸**：① L1-L5 / 講座別 ② 企業部門/プロセス別（エンジニアリング/財務/人事/営業/マーケティング/R&D/オペレーション/カスタマーサービス/法務/データ/デザイン/経営層）。ソース：awesome-llm-apps（Apache-2.0）、ai-engineering-hub（MIT）。 |

### `*_EN.md`

一部ファイルの英語版 sibling。

## 6. 他ディレクトリへの対応

| ディレクトリ | 本ディレクトリとの関係 | データフロー |
| --- | --- | --- |
| `01_Assessment` | 診断の L レベルがどのケースを選ぶか決定 | `01` L レベル → `04` ケースフィルタ |
| `02_Course_Design` | ケース/PoC インデックスはクラスデモ・練習題のソース | `04` ケース ↔ `02` 講座題 |
| `03_Consulting_Report` | 8 段階 Stage 3 業界ベスト実践ベンチマークでケース引用 | `04` ケース → `03` Stage 3 |
| `05_Sales` | 完全ケースとシナリオは Sales 素材の裏付け | `04` ケース → `05` 裏付け |
| `00_Overview` | シナリオストーリーはストーリーの素材 | `04` ↔ `00` |
| `90_References` | ケースインデックスの第三者引用（awesome-llm-apps / ai-engineering-hub） | `90` 引用 → `04` |

## 7. 共通使用シナリオ

- **Discovery 自己投影**：`CUSTOMER_SCENARIO_LIBRARY.md` を顧客役割に対応、「どのストーリーが似ている？」と質問。
- **PoC 選定**：L レベル診断後、`LLM_APPS_CASE_INDEX.md` §3 で L レベル別、または §4 で部門別、顧客に響く 3-5 個選択。
- **提案裏付け**：製造業顧客に `SAMPLE_CLIENT_CASE_MANUFACTURING.md` 見せ、完全導入全景を提示。
- **クロスレベル期待管理**：顧客が L5 ケース指摘 → インデックスでその L レベルと前提講座を指摘。
- **新ケース執筆**：プロジェクト終了後 `CASE_WRITING_STANDARD.md` + `CASE_CONTROL_TABLES.md` で新 sample case として執筆。

---

## ⭐ Cross-Topic Quick References：5 つの核心テーマ、どこで見つけるか

方法論全体には全ディレクトリを貫く 5 つの主動脈があります。本ディレクトリがそれぞれにどう接続するか：

| Cross-Topic | 主要位置 | 本ディレクトリがどう接続するか |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 3 エンジン共読** | Root [`README_JA.md`](../README_JA.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | ケースは Claude Code Tier 2 ワークフローで実行可能：`/simulate-engagement` で完全 6 週コンサル案件シミュレーション、`/parallel-perspectives` で 6 ステークホルダー視点、`/devil-pair-debate` で価値観前提議論 |
| 🎓 **学術基盤（7 大支柱）** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | ケースの ROI 論述は **Real Options** に対応（なぜ Phase 1 NPV ≈ 0 でも投資価値あり）；To-Be Design は **Task-Technology Fit** に対応（どのタスクが L4 へ、どれが L2 に留まるか） |
| 📚 **L1-L5 講座教育** | [`../02_Course_Design/`](../02_Course_Design/) | LLM Apps Case Index は L レベル分類、直接 PoC として選択可能；`POC_SCENARIO_SPECS.md` + `N8N_WORKFLOW_TEMPLATES.md` でケースを L3 クラスハンズオン題に変換 |
| 🔁 **コンサル方案 / 8 段階 + Phase A→B→C クローズドループ** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **ケースは Phase A Discovery の「自己投影」素材**（顧客が「そう、まさにそれ」と言う）；業界ベスト実践が Stage 3 にマッピング；7 つの完全 sample case が Phase B レポートの雛形 |
| 📖 **参考資料 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | LLM Apps Case Index ソース：`Shubhamsaboo/awesome-llm-apps`（Apache-2.0）+ `patchy631/ai-engineering-hub`（MIT）、完全 appreciation cards は [`../90_References/README.md`](../90_References/README.md) §2.4 参照；ClawTeam Walkthrough は `HKUDS/ClawTeam`（MIT）から |
