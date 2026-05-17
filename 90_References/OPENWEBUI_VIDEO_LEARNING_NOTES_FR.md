# Notes d'apprentissage vidéo OpenWebUI et résumé d'application

> 🌐 Langue : [繁體中文](OPENWEBUI_VIDEO_LEARNING_NOTES.md) ｜ [English](OPENWEBUI_VIDEO_LEARNING_NOTES_EN.md) ｜ [Deutsch](OPENWEBUI_VIDEO_LEARNING_NOTES_DE.md) ｜ Français ｜ [Español](OPENWEBUI_VIDEO_LEARNING_NOTES_ES.md) ｜ [日本語](OPENWEBUI_VIDEO_LEARNING_NOTES_JA.md) ｜ [한국어](OPENWEBUI_VIDEO_LEARNING_NOTES_KR.md)

Version : v1.0
Notes par : Morris Lu (盧業興) · Tiger AI 虎智科技
Objectif : Transformer la playlist publique OpenWebUI en notes d'apprentissage, résumés et une carte d'application future pour le cours d'onboarding entreprise L1.

## 原始影片版權聲明 / Third-Party Video Credits

> **本文件為第三方公開影片的學習筆記，並非影片本身。所有影片內容與版權皆歸原始創作者所有，本文件僅作為學習與課程設計用途引用其公開連結。**
>
> **Ce document contient des notes d'étude dérivées de vidéos tierces publiquement disponibles. Ce N'EST PAS un transcript ou une reproduction. Tout le contenu vidéo et les copyrights restent avec les créateurs originaux ; les liens sont cités ici uniquement pour référence éducative et de conception de cours.**

- **原始 Playlist / Playlist originale** : <https://www.youtube.com/watch?v=oXJ4L1G8kaI&list=PL_rTgQnnMXsXAsEiid-tWhaj03SsP4U5Z>
- Lien original et titre de chaque vidéo cités individuellement dans les tableaux ci-dessous ; veuillez vous référer à la source originale pour le contenu autoritaire.

Si vous êtes un titulaire de droits et souhaitez mettre à jour l'attribution ou demander la suppression d'une citation, veuillez ouvrir un issue dans ce repository.

---

## 1. Comment utiliser ce document

Ce document n'est pas un transcript ; c'est un record d'apprentissage pour la conception de cours. Chaque vidéo est mappée à :

1. Le sujet de la vidéo.
2. Un résumé d'apprentissage.
3. Son application future au sein de la méthodologie TigerAI L1-L5.
4. Une priorité de cours.

Définitions de priorité :

| Priorité | Description |
|---|---|
| P0 | Must-watch pour enablement entreprise L1 ; affecte directement comptes, login, usage, permissions et sécurité des données |
| P1 | Must-watch pour Admin / IT ; affecte déploiement, modèles, operations, permissions et updates |
| P2 | Fonctionnalité optionnelle ; incluse selon les besoins client |
| P3 | Cas inspirational ; utilisable pour démos ou comme extension L2/L3/L4 follow-on |

---

## 2. Conclusion globale pour le cours L1

OpenWebUI ne devrait pas être simplement empaqueté comme « alternative gratuite à ChatGPT ». Pendant l'adoption entreprise, sa valeur core est :

> Un entry point contrôlé à travers lequel l'entreprise gère l'usage IA. Chaque employé a son propre compte et zone de chat, et l'Admin peut gérer rôles, groupes, permissions, modèles, outils et frontières de données.

Donc, le fil principal du cours L1 devrait être :

1. Chaque personne se logue individuellement ; pas de comptes partagés.
2. Chaque personne a sa propre history de chat, dossiers, Prompts et settings personnels.
3. L'Admin peut gérer users, rôles, groupes, permissions et visibilité des modèles.
4. IT peut décider sur modèles locaux, APIs cloud, mode Hybrid et stratégies d'update opérationnel.
5. HR / management peut établir des guidelines d'usage IA et frontières d'entrée de données.
6. L'output L1 doit overlapper en L2 : organiser les Prompts haute-fréquence et scénarios de travail en candidats Skill.

---

## 3. Résumés d'apprentissage vidéo et applications futures

| # | Vidéo | Résumé d'apprentissage | Application future | Priorité |
|---:|---|---|---|---|
| 1 | [Open WebUI: The Free, Private ChatGPT Alternative](https://www.youtube.com/watch?v=oXJ4L1G8kaI) | Positionnement, valeur et scénarios d'usage de base d'OpenWebUI. | Session d'ouverture L1, utilisée pour expliquer pourquoi l'entreprise a besoin de son propre entry point IA. | P0 |
| 2 | [How to Install OpenWebUI](https://www.youtube.com/watch?v=d6Su3Nmv7-8) | Flow d'installation fondamental pour OpenWebUI. | Préparation pré-cours IT, setup d'environnement PoC, checklist de déploiement. | P1 |
| 3 | [Local AI Model Requirements](https://www.youtube.com/watch?v=CYBu9dTVWC4) | Concepts de CPU, RAM et GPU requis pour modèles locaux. | Évaluation de déploiement Cloud AI / Hybrid / entièrement on-premise ; aide les clients à juger les seuils hardware. | P1 |
| 4 | [Exploring the OpenWebUI Admin Panel](https://www.youtube.com/watch?v=4pIzLtUhJLM) | Vue d'ensemble des fonctionnalités Admin Panel et entry points de management. | Must-watch pour le cours L1 Admin ; couvre management de compte, modèle, fonctionnalité et settings. | P0 |
| 5 | [Exploring Open WebUI: Features, Models, & Tools](https://www.youtube.com/watch?v=CDiVq3mPZc8) | Vue d'ensemble des fonctionnalités, modèles et outils OpenWebUI. | Tour L1 all-hands, pour que les stagiaires comprennent les fonctionnalités et frontières disponibles. | P0 |
| 6 | [How to Chat with Your Own Documents](https://www.youtube.com/watch?v=lqKapMX2GAI) | Utiliser ses propres documents pour chat et Q&R. | Résumé de document L1 et Q&R de document low-sensitivity ; données hautement sensibles nécessitent des guidelines séparées. | P0 |
| 7 | [How to Add Real-Time Web Search](https://www.youtube.com/watch?v=_KoifHHJhNY) | Ajouter Web Search temps-réel. | Scénarios research, sales et marketing ; l'entreprise doit fixer règles de citation de source et permissions. | P2 |
| 8 | [How to Add GPT-4 to OpenWebUI](https://www.youtube.com/watch?v=ZUc50fcWO2E) | Intégrer modèles classe OpenAI API / GPT-4. | Setup cloud model provider Admin / IT ; utilisable en architecture Hybrid. | P1 |
| 9 | [How to Use Community Tools](https://www.youtube.com/watch?v=juAbnns5Ohg) | Étendre les capabilities avec community tools. | Précurseur à L2/L3 ; l'entreprise doit d'abord faire security review et whitelisting d'outils. | P2 |
| 10 | [Text-to-Speech with ElevenLabs API](https://www.youtube.com/watch?v=LzlzXQzBUcg) | Intégrer TTS et output audio. | Optionnel pour customer service, éducation et matériaux de formation ; pas L1 core. | P2 |
| 11 | [How to Create Custom AI Models](https://www.youtube.com/watch?v=Fd_1zePgCLE) | Créer settings de modèle customisés ou personas de modèle. | Modèles default départementaux, assistants persona-based ; overlapper en L2 Skills. | P2 |
| 12 | [AI Images with OpenWebUI & DALL-E 3](https://www.youtube.com/watch?v=3rg8Tdyn_RA) | Capability de génération d'image. | Optionnel pour marketing et design ; requiert attention à copyright, brand et review. | P2 |
| 13 | [LLAVA Multimodal / GPT-4 Image Analysis](https://www.youtube.com/watch?v=yZkmolyV0Zk) | Utiliser modèles multimodaux pour analyser images. | Exploration préliminaire pour QC, healthcare et document imaging ; scénarios high-risk nécessitent human review. | P2 |
| 14 | [AI Clone](https://www.youtube.com/watch?v=dXaFbHw5-m8) | Démo d'un AI clone personnalisé. | Démo inspirational ; adoption entreprise requiert handling spécial de privacy et licensing likeness/voice. | P3 |
| 15 | [Functions to Build Websites & Apps](https://www.youtube.com/watch?v=KbkfaapAvpE) | Étendre capability d'application avec Functions. | Extension L2/L3 : transformer capability chat en outils exécutables ou prototypes d'app. | P2 |
| 16 | [Reduce AI Hallucinations with Advanced Parameters](https://www.youtube.com/watch?v=OWsFsnnrMdE) | Utiliser advanced parameters pour réduire risque d'hallucination. | Must-watch pour L1 ; utilisé pour data trustworthiness, vérification humaine et éducation aux paramètres de modèle. | P0 |
| 17 | [Choosing the Right Ollama Model](https://www.youtube.com/watch?v=KIc1lRmehyY) | Choisir le bon modèle Ollama local. | Management de modèle IT / Admin et évaluation de déploiement on-premise. | P1 |
| 18 | [Mobile Access with Ngrok](https://www.youtube.com/watch?v=DFtI1m957XM) | Accès remote ou mobile à OpenWebUI via Ngrok. | Optionnel ; l'entreprise doit considérer sécurité, VPN, exposure surface et access control. | P2 |
| 19 | [Choosing the Best Language Model](https://www.youtube.com/watch?v=-yhChXlYjbQ) | Méthodes pour sélectionner parmi différents modèles de langage. | Gérer catalogue de modèles et modèles département-appropriés ; overlapper à model evaluation sheet. | P1 |
| 20 | [Vision LLMs for Local Inference](https://www.youtube.com/watch?v=VDLNtKbfewQ) | Comparaison de modèles vision locaux. | Exploration pour QC, documents image et imagerie médicale ; contenu optionnel avancé. | P2 |
| 21 | [AI Recruiter Meets AI Clone](https://www.youtube.com/watch?v=649qtKjbnk4) | Scénario démo de recrutement avec AI clone. | Cas inspirational HR ; convertible en Skill de recrutement L2 ou workflow de recrutement L3. | P3 |
| 22 | [Groq Cloud & OpenWebUI](https://www.youtube.com/watch?v=Ukft9qfb67o) | Intégrer modèles cloud comme Groq Cloud. | Stratégie multi-model provider IT / Admin. | P1 |
| 23 | [Docker & Watchtower](https://www.youtube.com/watch?v=W0Yh_HsMkOQ) | Auto-updates et operations de container Docker. | Must-watch pour operations IT ; couvre updates OpenWebUI et stabilité de service. | P1 |
| 24 | [OpenWebUI Pipelines](https://www.youtube.com/watch?v=DFlSd6GrMIk) | Capability workflow Custom Pipelines. | Preview L3 ; peut overlapper plus tard à n8n, APIs et pipelines de traitement de données. | P2 |
| 25 | [Set Up User Roles for Secure Collaboration](https://www.youtube.com/watch?v=xlE782FrW_s) | Set up user roles et collaboration sécurisée. | Must-watch pour L1 Admin ; couvre comptes per-person, rôles, groupes et permissions. | P0 |
| 26 | [Writing Better Prompts](https://www.youtube.com/watch?v=FYTir7cor1c) | Écrire de meilleurs Prompts. | Must-watch pour tout L1 ; overlapper à Prompt Library et candidats Skill L2. | P0 |
| 27 | [Arena Model](https://www.youtube.com/watch?v=PU7B5FHalrg) | Comparaison de modèle et test de performance. | Utilisé par Admin / seed users pour évaluation de modèle et décisions de procurement. | P1 |
| 28 | [Run Text-to-Speech Locally](https://www.youtube.com/watch?v=lwk0QGLou9Y) | TTS local. | Optionnel pour besoins voix high-privacy ; pas L1 core. | P2 |
| 29 | [OpenWebUI Memory Explained](https://www.youtube.com/watch?v=a0H2w5z_uk4) | Concepts de mémoire et personnalisation. | Peut servir d'introduction capability personnalisation ; l'entreprise doit adresser privacy, deletion et data retention policy. | P2 |
| 30 | [Quantization](https://www.youtube.com/watch?v=7J-AKL2TAD0) | Quantization de modèle et amélioration de performance. | Optionnel pour IT ; supporte déploiement on-premise et contrôle de coût. | P2 |
| 31 | [AI-Powered Recruiter Bot](https://www.youtube.com/watch?v=XPeZGo6McLc) | Construire un recruiter bot. | Cas HR / L2 / L3 : analyse de poste, résumé de CV, drafting de questions d'interview. | P3 |
| 32 | [Open WebUI v0.4 Updates](https://www.youtube.com/watch?v=qESVuLFHYqI) | Updates de version et nouvelles fonctionnalités. | Awareness de version IT / Admin ; établir un SOP de check d'update. | P1 |
| 33 | [Anthropic Claude Models in OpenWebUI](https://www.youtube.com/watch?v=1jahR-BA6Ts) | Intégrer modèles Claude. | Setup multi-provider Admin / IT ; convient à stratégie de modèle Hybrid. | P1 |
| 34 | [Public Access to OpenWebUI Chatbots](https://www.youtube.com/watch?v=0pyHYhzqdRQ) | Accès Public Chatbot. | Fonctionnalité high-risk ; l'entreprise doit gouverner strictement. Convient à discussion pré-PoC sur customer service externe. | P2 |
| 35 | [Tools, Functions & Pipelines Deep Dive](https://www.youtube.com/watch?v=wRkAko8yphs) | Deep dive en Tools, Functions et Pipelines. | Preview L2/L3 ; prend OpenWebUI d'un entry point chat vers outils et workflows. | P2 |
| 36 | [Online? Offline? Both?](https://www.youtube.com/watch?v=W9czUS3trMU) | Discussion de modes online, offline et hybrid. | Must-watch pour discussion de mode de déploiement L1 ; couvre cloud AI / Hybrid / entièrement on-premise. | P0 |

---

## 4. Parcours de visionnage recommandés

### 4.1 Tous les utilisateurs L1

Visionnage recommandé :

1. #1 Positionnement OpenWebUI.
2. #5 Vue d'ensemble fonctionnalités, modèles et outils.
3. #6 Chat documents.
4. #16 Réduire hallucinations et advanced parameters.
5. #26 Écriture de Prompt.
6. #36 Modes online / offline / hybrid.

Objectif : Permettre aux employés de se loguer en sécurité, construire leur propre zone de chat, compléter les tâches quotidiennes et comprendre les frontières de données.

### 4.2 Admin / IT

Visionnage recommandé :

1. #2 Installation.
2. #3 Exigences hardware modèle local.
3. #4 Admin Panel.
4. #8 OpenAI API.
5. #17 Modèles Ollama.
6. #19 Sélection de modèle.
7. #22 Groq Cloud.
8. #23 Docker / Watchtower.
9. #25 User Roles.
10. #32 Updates de version.
11. #33 Modèles Claude.

Objectif : Permettre à IT de construire, opérer, gérer et gouverner OpenWebUI.

### 4.3 Extensions L2 / L3

Visionnage recommandé :

1. #9 Community Tools.
2. #11 Custom AI Models.
3. #15 Functions.
4. #24 Pipelines.
5. #35 Tools / Functions / Pipelines Deep Dive.

Objectif : Overlapper OpenWebUI d'un entry point Chat L1 en Skills L2 et Workflows L3.

### 4.4 Industrie / Département Électifs

| Industrie / Département | Vidéos recommandées |
|---|---|
| HR | #21, #31 |
| Marketing / Design | #12 |
| Customer Service / Éducation et Formation | #10, #28 |
| QC / Healthcare / Documents Image | #13, #20 |
| Entreprises High-Privacy | #3, #17, #23, #30, #36 |

---

## 5. Application aux cours et livraison

### 5.1 Application au cours L1

Doit être transformé en les deliverables de cours suivants :

- Manuel d'opérations utilisateur OpenWebUI.
- Runbook Admin OpenWebUI.
- Sheet de configuration compte / groupe / permission / visibilité de modèle.
- Guidelines d'usage IA.
- Prompt Library v1.
- Sheet d'acceptance Gate 1.

### 5.2 Application au cours L2

Les vidéos suivantes peuvent être transformées en candidats Skill :

- #26 Écriture de Prompt → Skill Prompt.
- #6 Chat documents → Skill résumé de document.
- #11 Custom AI Models → Skill modèle persona départemental.
- #15 Functions → Skill outillé.
- #35 Tools / Functions / Pipelines → Bridge L2-vers-L3.

### 5.3 Application au cours L3

Les vidéos suivantes peuvent être transformées en candidats Workflow :

- #7 Web Search → Workflow market research.
- #24 Pipelines → flow de traitement custom.
- #35 Tools / Functions / Pipelines → bridge flow OpenWebUI + n8n.
- #34 Public Chatbots → PoC bot customer service externe, mais nécessite permissions strictes et review.

---

## 6. Notes d'adoption entreprise

1. Les comptes ne doivent pas être partagés ; sinon zones de chat per-person, accountability et governance de permission sont impossibles.
2. Les nouveaux utilisateurs ne devraient pas avoir de fonctionnalités avancées par défaut ; review Admin est recommandée.
3. File Upload, Web Search, Tools, Functions, Pipelines et Public Share devraient tous être traités comme fonctionnalités avancées.
4. Chaque département devrait avoir son propre groupe et stratégie de visibilité de modèle.
5. Les industries hautement sensibles doivent d'abord déterminer mode de déploiement cloud AI / Hybrid / entièrement on-premise.
6. Capabilities memory et personnalisation requièrent politiques de privacy, deletion et data retention.
7. Public Chatbots ou accès externe ne devraient pas être ouverts largement à L1 ; un PoC séparé est requis.
8. Chaque update de version devrait rafraîchir l'Admin Runbook et usage guidelines.
