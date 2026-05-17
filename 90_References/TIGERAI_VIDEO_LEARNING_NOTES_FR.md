# Notes d'apprentissage vidéo chaîne TigerAI et résumé d'application L3

> 🌐 Langue : [繁體中文](TIGERAI_VIDEO_LEARNING_NOTES.md) ｜ [English](TIGERAI_VIDEO_LEARNING_NOTES_EN.md) ｜ [Deutsch](TIGERAI_VIDEO_LEARNING_NOTES_DE.md) ｜ Français ｜ [Español](TIGERAI_VIDEO_LEARNING_NOTES_ES.md) ｜ [日本語](TIGERAI_VIDEO_LEARNING_NOTES_JA.md) ｜ [한국어](TIGERAI_VIDEO_LEARNING_NOTES_KR.md)

Version : v1.0
Auteur : Morris Lu (盧業興) · Tiger AI 虎智科技
Chaîne : 虎智科技 TigerAI
Chaîne originale : `https://www.youtube.com/@%E8%99%8E%E6%99%BA%E7%A7%91%E6%8A%80TigerAI`

---

## 1. Comment utiliser ce document

Ce document organise les vidéos de la chaîne TigerAI qui peuvent être utilisées pour la conception de cours L1-L4, avec un focus particulier sur n8n et L3 Workflow Automation.

Approche d'organisation :

1. Construire des résumés d'apprentissage basés sur le catalogue de vidéos publiquement disponible et les titres.
2. Mapper les vidéos sur des usages de cours L1 / L2 / L3 / L4.
3. Organiser les vidéos n8n en modules de cours L3 et une roadmap PoC.
4. Organiser les vidéos OpenGenie en un thread d'adoption couvrant gouvernance entreprise, comptes, permissions, modèles, Prompts, Channels, intégration n8n, RAG/Vision et systèmes de feedback.

Priorité :

| Priorité | Description |
|---|---|
| P0 | Must-watch pour le cours core L3 n8n |
| P1 | Contenu de support important pour L1 / L2 / L3 / L4 |
| P2 | Cas électif spécifique à l'industrie ou département |
| P3 | Démo ou cas inspirational |

---

## 2. Conclusion globale pour le cours L3

Les vidéos TigerAI n8n ne sont pas simplement des tutoriels d'outil ; ce sont une bibliothèque de cas complète d'automatisation de processus entreprise. La logique de formation L3 qu'elles révèlent devrait être :

> Reprendre là où le Skill / Workflow Blueprint produit en L2 s'arrête, et utiliser n8n pour le transformer en un PoC de processus exécutable, vérifiable, sauvegardé, opérable et intégrable inter-plateformes.

Donc le cours L3 devrait souligner :

1. Trigger : Webhook, schedule, Gmail, LINE, Facebook, YouTube, GCS / API event.
2. Data Handling : Data Tables, Sheets, BigQuery, CRM / ERP / API data.
3. AI Processing : Gemini, images, audio, vidéo, documents, copywriting, résumé, classification.
4. Platform Integration : LINE, Facebook, YouTube, plateformes sociales, Gmail, GitHub.
5. Reuse : Modularisation Sub-workflow.
6. Governance : Credentials, Execution Log, GitHub backup, human review, error handling.
7. L4 Readiness : Permettre à Hermes Agent d'appeler des Workflows n8n dans le futur.

---

## 3. Résumés vidéo OpenGenie Enterprise Governance

| # | Vidéo | Résumé d'apprentissage | Application au cours | Priorité |
|---:|---|---|---|---|
| OG-1 | [TigerAI OpenGenie 單元 1：帳號體系與權限佈署](https://www.youtube.com/watch?v=wkgx94TmFE4) | Déploiement compte, utilisateur et permission. | Enablement entreprise L1 OpenWebUI / OpenGenie ; couvre comptes per-person et gouvernance de permission. | P1 |
| OG-2 | [單元 2：後端模型 Ollama 管理與安裝](https://www.youtube.com/watch?v=fyK8lIBEdoU) | Installation et gestion de modèle back-end. | Gestion de modèle L1 IT / Admin ; supporte décisions cloud AI / Hybrid / entièrement on-premise. | P1 |
| OG-3 | [單元 3：API Key 彈性配置](https://www.youtube.com/watch?v=IdI_pqRjEOU) | API Key et stratégie cloud-assist. | IT L1/L3 ; gère fournisseurs de modèles, APIs externes et permissions. | P1 |
| OG-4 | [單元 4：Prompts 專家設定](https://www.youtube.com/watch?v=CZwXcgtKn0Y) | Configuration Expert Prompt. | Prompt Library L1 ; Skill-isation L2. | P1 |
| OG-5 | [單元 5：群組與協作權限深度管理](https://www.youtube.com/watch?v=G1MKa10W6K0) | Groupes et permissions de collaboration. | L1 Admin / design de permission de processus L3. | P1 |
| OG-6 | [單元 6：Channels 協作與會議摘要](https://www.youtube.com/watch?v=38kkwwRDOpU) | Channels, collaboration et résumés de réunion. | Collaboration départementale L1, Skill de résumé de réunion L2, flow de réunion L3. | P2 |
| OG-7 | [單元 7：n8n 串接與自動化工作流](https://www.youtube.com/watch?v=xX6e0l-TaWg) | Intégration OpenGenie et n8n ; workflows automatisés. | Core du cours principal L3, servant de vidéo d'entrée L3. | P0 |
| OG-8 | [單元 8：多模態進階應用 RAG & Vision](https://www.youtube.com/watch?v=qN_2KSgbjUM) | Applications RAG, Vision et multimodales. | L3 Gemini / flow multimodal ; précurseur au L4 Hermes knowledge work. | P1 |
| OG-9 | [單元 9：綜合應用與分享機制](https://www.youtube.com/watch?v=jQPBSZmYLbg) | Applications intégrées, sharing et collaboration. | Gouvernance de sharing L1/L3 et démo showcase. | P2 |
| OG-10 | [單元 10：管理監督與回饋系統](https://www.youtube.com/watch?v=4Lrgg-vdhi8) | Supervision de gestion et feedback. | Operations L3, feedback, amélioration de qualité et acceptance Gate 3. | P1 |

---

## 4. Résumés vidéo Antigravity / L2

| # | Vidéo | Résumé d'apprentissage | Application au cours | Priorité |
|---:|---|---|---|---|
| AG-1 | [1部曲：AI 全自動寫代碼、測試還幫你錄影](https://www.youtube.com/watch?v=LCO700FzoXg) | Foundation Antigravity ; IA écrit code, teste, enregistre evidence. | L2 Antigravity Foundation. | P1 |
| AG-2 | [2部曲：AI 寫 Code 鬼打牆怎麼辦](https://www.youtube.com/watch?v=RRWtnqqQI0E) | Mindset de debugging ; extension Skill plugin. | L2 Debug / Skill-isation. | P1 |
| AG-3 | [3部曲：開發環境零手動](https://www.youtube.com/watch?v=kHywZFPsju8) | IA installe packages et UI. | Pratique d'engineering L2. | P1 |
| AG-4 | [4部曲：爬蟲與架站](https://www.youtube.com/watch?v=K4UMhFj9ztE) | Data scraping et un Web UI customisé. | Prototype App L2 ; L3 peut reprendre les data flows d'ici. | P1 |
| AG-5 | [5部曲：Docker 容器化與打包](https://www.youtube.com/watch?v=IILRXP2cMbo) | Containerisation Docker. | Deliverable d'engineering L2 et précurseur de déploiement L3. | P1 |
| AG-6 | [6部曲：互動 App 與個人專屬 Skill](https://www.youtube.com/watch?v=q9rNgnqNXlc) | Construire une App interactive et un Skill personnel. | Skill Library L2 et Bridge L2-vers-L3. | P1 |

---

## 5. Résumés vidéo n8n / L3

| # | Vidéo | Résumé d'apprentissage | Application au cours L3 | Priorité |
|---:|---|---|---|---|
| N27 | [不寫程式也能用 Gemini：n8n 整合 Google Gemini 全攻略](https://www.youtube.com/watch?v=DT5Gx5tMxGs) | Utiliser n8n pour intégrer Gemini pour images, audio, vidéo et documents. | Foundation traitement L3 AI Node / multimodal. | P0 |
| N28 | [n8n 進階教學：Sub-workflow 模組化自動化術](https://www.youtube.com/watch?v=hbvHwjrexds) | Construire des Sub-workflows réutilisables. | Must-watch pour modularisation L3 et standardisation de processus. | P0 |
| N29 | [AI 即時查詢神器：高鐵時刻查詢機器人](https://www.youtube.com/watch?v=T1hzDrIhHSk) | LINE auto-reply pour schedule, tarifs et horaires. | Cas pour Webhook / LINE / API query flow. | P0 |
| N30 | [AI 人資革命：自動履歷篩選系統](https://www.youtube.com/watch?v=EgSFZm6hvE8) | Processus HR n8n + Gemini + Gmail + LINE. | PoC processus HR : intake CV, screening IA, notifications. | P0 |
| N31 | [史上最強社群自動化](https://www.youtube.com/watch?v=Eb-DwLnNjUk) | Image produit vers vidéo, copywriting, marketing multi-plateforme. | PoC d'automatisation marketing. | P2 |
| N32 | [AI 自動發文 2.0](https://www.youtube.com/watch?v=hlhByT2m28M) | Génération vidéo, copywriting, publication multi-plateforme. | Workflow social posting ; nécessite un Gate de human review. | P2 |
| N33 | [YouTube AI 留言機器人](https://www.youtube.com/watch?v=3cB4BtGUA9w) | YouTube auto-reply comments et interaction keyword. | Flow d'interaction sociale et customer service. | P2 |
| N34 | [n8n 終極備份術](https://www.youtube.com/watch?v=zrsE4-G6MRY) | Auto-sync Workflows + Credentials vers GitHub. | Must-watch pour operations L3, backup et gouvernance de version. | P0 |
| N35 | [Facebook 聊天機器人實戰](https://www.youtube.com/watch?v=c9VuLN_DasA) | Construire un bot customer service Facebook AI avec n8n + Webhook. | Cas principal pour automatisation customer service. | P0 |
| N36 | [Data Tables 實戰：Facebook 智能客服](https://www.youtube.com/watch?v=v4plNZNSG08) | n8n Data Tables, intégration plateforme Meta, replies AI customisés. | Must-watch pour L3 Data Tables et state management. | P0 |
| N37 | [AI 客服升級版：FB 粉專自動回圖、回訊息](https://www.youtube.com/watch?v=pEWn2yh1Dkg) | Image et message replies pour customer service Facebook. | Customer service multimodal optionnel. | P2 |
| N38 | [AI 自動行銷機器人](https://www.youtube.com/watch?v=njcKlnhEaUM) | Freepik + DataForSEO : auto image sourcing, copywriting, sélection keyword, posting. | Flow supply chain de contenu marketing. | P2 |
| N39 | [Sora 2 全自動影片工廠](https://www.youtube.com/watch?v=3NJZ99lY8kU) | n8n + Kie AI : génération vidéo one-click et publication vers FB, IG, Threads, YouTube. | Cas advanced video factory ; nécessite Gates de review et brand. | P3 |

---

## 6. Implications de conception de cours L3

### 6.1 Nous ne pouvons pas enseigner uniquement les bases n8n

Les vidéos TigerAI montrent que ce qui est vraiment précieux en L3 n'est pas « drag nodes », mais former une boucle fermée complète dans le processus :

`Trigger → Data → AI → System Action → Human Gate → Log → Backup → Reuse`

### 6.2 L3 doit avoir quatre pools de cas

| Pool de cas | Vidéos représentatives | Clients appropriés |
|---|---|---|
| Customer service automation | N35, N36, N37 | Services, e-commerce, fan pages, customer service centers |
| HR automation | N30 | HR, recrutement, HR shared services |
| Marketing automation | N31, N32, N33, N38, N39 | Marketing, contenu, social, brand |
| Bot query / utility | N29 | Operations, customer service, queries internes |

### 6.3 L3 doit ajouter un cours de gouvernance

Le backup GitHub dans la vidéo N34 est très important et devrait être une partie requise de L3, pas un électif. Après que les entreprises adoptent n8n, sans backups, versioning, gestion de credentials, Execution Logs et notifications d'erreur, le PoC devient facilement un jouet non maintenable.

---

## 7. Parcours de visionnage recommandés

### 7.1 L3 Core Track

1. OG-7 : Intégration OpenGenie et n8n.
2. N27 : n8n + Gemini multimodal.
3. N28 : Sub-workflows.
4. N34 : GitHub backup.
5. N35 : Facebook Webhook customer service.
6. N36 : Data Tables.

### 7.2 Customer Service Track

1. N35.
2. N36.
3. N37.
4. OG-10.

### 7.3 HR Track

1. N30.
2. OG-4.
3. OG-6.
4. N34.

### 7.4 Marketing Track

1. N31.
2. N32.
3. N33.
4. N38.
5. N39.

### 7.5 IT / Operations Track

1. OG-1.
2. OG-3.
3. OG-5.
4. N28.
5. N34.
6. OG-10.

---

## 8. Application à la livraison

Les vidéos TigerAI devraient être transformées en les deliverables suivants :

- L3 n8n Workflow Blueprint.
- n8n Workflow JSON.
- Sheet de permission Credential / API / Webhook.
- Data Tables Schema.
- Sub-workflow Library.
- Execution Log et test records.
- SOP GitHub backup et version management.
- Design Human Gate.
- Design Error Handling / Retry / Fallback.
- Liste de Workflows appelables par L4 Hermes Agent.
