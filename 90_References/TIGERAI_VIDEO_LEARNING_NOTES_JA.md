# TigerAI チャンネル動画学習ノートと L3 適用サマリー

> 🌐 言語：[繁體中文](TIGERAI_VIDEO_LEARNING_NOTES.md) ｜ [English](TIGERAI_VIDEO_LEARNING_NOTES_EN.md) ｜ [Deutsch](TIGERAI_VIDEO_LEARNING_NOTES_DE.md) ｜ [Français](TIGERAI_VIDEO_LEARNING_NOTES_FR.md) ｜ [Español](TIGERAI_VIDEO_LEARNING_NOTES_ES.md) ｜ 日本語 ｜ [한국어](TIGERAI_VIDEO_LEARNING_NOTES_KR.md)

バージョン：v1.0
著者：Morris Lu（盧業興）· Tiger AI 虎智科技
チャンネル：虎智科技 TigerAI
オリジナルチャンネル：`https://www.youtube.com/@%E8%99%8E%E6%99%BA%E7%A7%91%E6%8A%80TigerAI`

---

## 1. 本ドキュメントの使い方

本ドキュメントは L1-L4 コース設計に使用可能な TigerAI チャンネル動画を整理、特に n8n と L3 Workflow Automation にフォーカス。

整理アプローチ：

1. 公的に利用可能な動画カタログとタイトルに基づいて学習サマリーを構築。
2. 動画を L1 / L2 / L3 / L4 コース使用へマップ。
3. n8n 動画を L3 コースモジュールと PoC ロードマップへ整理。
4. OpenGenie 動画をエンタープライズガバナンス、アカウント、権限、モデル、Prompts、Channels、n8n 統合、RAG/Vision、フィードバックシステムをカバーする採用スレッドへ整理。

優先度：

| 優先度 | 説明 |
|---|---|
| P0 | L3 n8n コアコース必須 |
| P1 | L1 / L2 / L3 / L4 の重要サポートコンテンツ |
| P2 | 業界 / 部門固有の選択ケース |
| P3 | デモまたはインスピレーションケース |

---

## 2. L3 コース全体結論

TigerAI n8n 動画は単なるツールチュートリアルではなく、完全なエンタープライズプロセス自動化ケースライブラリ。明らかにする L3 トレーニングロジックは：

> L2 が生成した Skill / Workflow Blueprint が終わったところを引き継ぎ、n8n を使って実行可能、検証可能、バックアップ可能、運用可能、プラットフォーム横断統合可能なプロセス PoC に変換。

したがって L3 コースは強調すべき：

1. Trigger：Webhook、スケジュール、Gmail、LINE、Facebook、YouTube、GCS / API イベント。
2. Data Handling：Data Tables、Sheets、BigQuery、CRM / ERP / API データ。
3. AI Processing：Gemini、画像、音声、動画、ドキュメント、コピーライティング、要約、分類。
4. Platform Integration：LINE、Facebook、YouTube、ソーシャルプラットフォーム、Gmail、GitHub。
5. Reuse：Sub-workflow モジュール化。
6. Governance：Credentials、Execution Log、GitHub バックアップ、human review、error handling。
7. L4 Readiness：Hermes Agent が将来 n8n Workflows を呼び出し可能にする。

---

## 3. OpenGenie Enterprise Governance 動画サマリー

| # | 動画 | 学習サマリー | コース適用 | 優先度 |
|---:|---|---|---|---|
| OG-1 | [TigerAI OpenGenie 單元 1：帳號體系與權限佈署](https://www.youtube.com/watch?v=wkgx94TmFE4) | アカウント、ユーザー、権限デプロイメント。 | L1 OpenWebUI / OpenGenie エンタープライズイネーブルメント；個人別アカウントと権限ガバナンスをカバー。 | P1 |
| OG-2 | [單元 2：後端模型 Ollama 管理與安裝](https://www.youtube.com/watch?v=fyK8lIBEdoU) | バックエンドモデルインストールと管理。 | L1 IT / Admin モデル管理；クラウド AI / Hybrid / 完全オンプレ決定サポート。 | P1 |
| OG-3 | [單元 3：API Key 彈性配置](https://www.youtube.com/watch?v=IdI_pqRjEOU) | API Key とクラウドアシスト戦略。 | L1/L3 IT；モデルプロバイダー、外部 API、権限管理。 | P1 |
| OG-4 | [單元 4：Prompts 專家設定](https://www.youtube.com/watch?v=CZwXcgtKn0Y) | エキスパート Prompt 設定。 | L1 Prompt Library；L2 Skill 化。 | P1 |
| OG-5 | [單元 5：群組與協作權限深度管理](https://www.youtube.com/watch?v=G1MKa10W6K0) | グループとコラボレーション権限。 | L1 Admin / L3 プロセス権限設計。 | P1 |
| OG-6 | [單元 6：Channels 協作與會議摘要](https://www.youtube.com/watch?v=38kkwwRDOpU) | Channels、コラボレーション、ミーティングサマリー。 | L1 部門コラボレーション、L2 ミーティングサマリー Skill、L3 ミーティングフロー。 | P2 |
| OG-7 | [單元 7：n8n 串接與自動化工作流](https://www.youtube.com/watch?v=xX6e0l-TaWg) | OpenGenie と n8n 統合；自動化ワークフロー。 | L3 メインコースのコア、L3 エントリー動画として機能。 | P0 |
| OG-8 | [單元 8：多模態進階應用 RAG & Vision](https://www.youtube.com/watch?v=qN_2KSgbjUM) | RAG、Vision、マルチモーダルアプリケーション。 | L3 Gemini / マルチモーダルフロー；L4 Hermes 知識ワーク前駆体。 | P1 |
| OG-9 | [單元 9：綜合應用與分享機制](https://www.youtube.com/watch?v=jQPBSZmYLbg) | 統合アプリケーション、共有、コラボレーション。 | L1/L3 共有ガバナンスとデモショーケース。 | P2 |
| OG-10 | [單元 10：管理監督與回饋系統](https://www.youtube.com/watch?v=4Lrgg-vdhi8) | 管理監督とフィードバック。 | L3 運用、フィードバック、品質改善、Gate 3 受入。 | P1 |

---

## 4. Antigravity / L2 動画サマリー

| # | 動画 | 学習サマリー | コース適用 | 優先度 |
|---:|---|---|---|---|
| AG-1 | [1部曲：AI 全自動寫代碼、測試還幫你錄影](https://www.youtube.com/watch?v=LCO700FzoXg) | Antigravity 基盤；AI がコードを書き、テストし、エビデンスを記録。 | L2 Antigravity Foundation。 | P1 |
| AG-2 | [2部曲：AI 寫 Code 鬼打牆怎麼辦](https://www.youtube.com/watch?v=RRWtnqqQI0E) | デバッグマインドセット；Skill プラグイン拡張。 | L2 Debug / Skill 化。 | P1 |
| AG-3 | [3部曲：開發環境零手動](https://www.youtube.com/watch?v=kHywZFPsju8) | AI がパッケージと UI をインストール。 | L2 エンジニアリングプラクティス。 | P1 |
| AG-4 | [4部曲：爬蟲與架站](https://www.youtube.com/watch?v=K4UMhFj9ztE) | データスクレイピングとカスタマイズ Web UI。 | L2 アプリプロトタイプ；L3 はここからデータフローを引き継げる。 | P1 |
| AG-5 | [5部曲：Docker 容器化與打包](https://www.youtube.com/watch?v=IILRXP2cMbo) | Docker コンテナ化。 | L2 エンジニアリングデリバラブルと L3 デプロイメント前駆体。 | P1 |
| AG-6 | [6部曲：互動 App 與個人專屬 Skill](https://www.youtube.com/watch?v=q9rNgnqNXlc) | インタラクティブアプリと個人 Skill 構築。 | L2 Skill Library と L2 から L3 ブリッジ。 | P1 |

---

## 5. n8n / L3 動画サマリー

| # | 動画 | 学習サマリー | L3 コース適用 | 優先度 |
|---:|---|---|---|---|
| N27 | [不寫程式也能用 Gemini：n8n 整合 Google Gemini 全攻略](https://www.youtube.com/watch?v=DT5Gx5tMxGs) | n8n を使って Gemini を画像、音声、動画、ドキュメント用に統合。 | L3 AI Node / マルチモーダル処理基盤。 | P0 |
| N28 | [n8n 進階教學：Sub-workflow 模組化自動化術](https://www.youtube.com/watch?v=hbvHwjrexds) | 再利用可能な Sub-workflows 構築。 | L3 モジュール化とプロセス標準化必須。 | P0 |
| N29 | [AI 即時查詢神器：高鐵時刻查詢機器人](https://www.youtube.com/watch?v=T1hzDrIhHSk) | スケジュール、料金、時刻表用 LINE 自動返信。 | Webhook / LINE / API クエリフロー用ケース。 | P0 |
| N30 | [AI 人資革命：自動履歷篩選系統](https://www.youtube.com/watch?v=EgSFZm6hvE8) | n8n + Gemini + Gmail + LINE HR プロセス。 | HR プロセス PoC：履歴書受付、AI スクリーニング、通知。 | P0 |
| N31 | [史上最強社群自動化](https://www.youtube.com/watch?v=Eb-DwLnNjUk) | 製品画像から動画、コピーライティング、マルチプラットフォームマーケティング。 | マーケティング自動化 PoC。 | P2 |
| N32 | [AI 自動發文 2.0](https://www.youtube.com/watch?v=hlhByT2m28M) | 動画生成、コピーライティング、マルチプラットフォーム公開。 | ソーシャル投稿ワークフロー；human review Gate 必要。 | P2 |
| N33 | [YouTube AI 留言機器人](https://www.youtube.com/watch?v=3cB4BtGUA9w) | YouTube 自動返信コメントとキーワードインタラクション。 | ソーシャルインタラクションとカスタマーサービスフロー。 | P2 |
| N34 | [n8n 終極備份術](https://www.youtube.com/watch?v=zrsE4-G6MRY) | Workflows + Credentials を GitHub へ自動同期。 | L3 運用、バックアップ、バージョンガバナンス必須。 | P0 |
| N35 | [Facebook 聊天機器人實戰](https://www.youtube.com/watch?v=c9VuLN_DasA) | n8n + Webhook で Facebook AI カスタマーサービスボット構築。 | カスタマーサービス自動化メインケース。 | P0 |
| N36 | [Data Tables 實戰：Facebook 智能客服](https://www.youtube.com/watch?v=v4plNZNSG08) | n8n Data Tables、Meta プラットフォーム統合、カスタマイズ AI 返信。 | L3 Data Tables と state 管理必須。 | P0 |
| N37 | [AI 客服升級版：FB 粉專自動回圖、回訊息](https://www.youtube.com/watch?v=pEWn2yh1Dkg) | Facebook カスタマーサービス用画像とメッセージ返信。 | オプション マルチモーダルカスタマーサービス。 | P2 |
| N38 | [AI 自動行銷機器人](https://www.youtube.com/watch?v=njcKlnhEaUM) | Freepik + DataForSEO：自動画像ソーシング、コピーライティング、キーワード選択、投稿。 | マーケティングコンテンツサプライチェーンフロー。 | P2 |
| N39 | [Sora 2 全自動影片工廠](https://www.youtube.com/watch?v=3NJZ99lY8kU) | n8n + Kie AI：ワンクリック動画生成と FB、IG、Threads、YouTube への公開。 | 高度動画工場ケース；review と brand Gates 必要。 | P3 |

---

## 6. L3 コース設計含意

### 6.1 n8n 基礎のみを教えることはできない

TigerAI 動画は L3 で本当に価値あるのは「ノードドラッグ」ではなく、プロセスで完全な閉ループを形成することを示す：

`Trigger → Data → AI → System Action → Human Gate → Log → Backup → Reuse`

### 6.2 L3 は 4 つのケースプール持つ必要

| ケースプール | 代表動画 | 適合顧客 |
|---|---|---|
| カスタマーサービス自動化 | N35、N36、N37 | サービス、e-commerce、ファンページ、カスタマーサービスセンター |
| HR 自動化 | N30 | HR、リクルートメント、HR シェアードサービス |
| マーケティング自動化 | N31、N32、N33、N38、N39 | マーケティング、コンテンツ、ソーシャル、ブランド |
| クエリ / ユーティリティボット | N29 | 運用、カスタマーサービス、内部クエリ |

### 6.3 L3 はガバナンスコースを追加する必要

動画 N34 の GitHub バックアップは非常に重要で、L3 の必須部分であるべき、選択ではなく。企業が n8n を採用後、バックアップ、バージョニング、認証情報管理、Execution Log、エラー通知なしでは、PoC は容易に保守不能なおもちゃになる。

---

## 7. 推奨視聴パス

### 7.1 L3 Core Track

1. OG-7：OpenGenie と n8n 統合。
2. N27：n8n + Gemini マルチモーダル。
3. N28：Sub-workflows。
4. N34：GitHub バックアップ。
5. N35：Facebook Webhook カスタマーサービス。
6. N36：Data Tables。

### 7.2 Customer Service Track

1. N35。
2. N36。
3. N37。
4. OG-10。

### 7.3 HR Track

1. N30。
2. OG-4。
3. OG-6。
4. N34。

### 7.4 Marketing Track

1. N31。
2. N32。
3. N33。
4. N38。
5. N39。

### 7.5 IT / Operations Track

1. OG-1。
2. OG-3。
3. OG-5。
4. N28。
5. N34。
6. OG-10。

---

## 8. デリバリーへの適用

TigerAI 動画は以下のデリバラブルに変換すべき：

- L3 n8n Workflow Blueprint。
- n8n Workflow JSON。
- Credential / API / Webhook 権限シート。
- Data Tables スキーマ。
- Sub-workflow Library。
- Execution Log とテスト記録。
- GitHub バックアップとバージョン管理 SOP。
- Human Gate 設計。
- Error Handling / Retry / Fallback 設計。
- L4 Hermes Agent が呼び出し可能な Workflows のリスト。
