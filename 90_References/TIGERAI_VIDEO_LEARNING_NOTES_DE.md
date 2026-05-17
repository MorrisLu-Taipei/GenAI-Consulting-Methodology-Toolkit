# TigerAI Channel Video Lernnotizen und L3-Anwendungs-Zusammenfassung

> 🌐 Sprache: [繁體中文](TIGERAI_VIDEO_LEARNING_NOTES.md) ｜ [English](TIGERAI_VIDEO_LEARNING_NOTES_EN.md) ｜ Deutsch ｜ [Français](TIGERAI_VIDEO_LEARNING_NOTES_FR.md) ｜ [Español](TIGERAI_VIDEO_LEARNING_NOTES_ES.md) ｜ [日本語](TIGERAI_VIDEO_LEARNING_NOTES_JA.md) ｜ [한국어](TIGERAI_VIDEO_LEARNING_NOTES_KR.md)

Version: v1.0
Autor: Morris Lu (盧業興) · Tiger AI 虎智科技
Channel: 虎智科技 TigerAI
Original Channel: `https://www.youtube.com/@%E8%99%8E%E6%99%BA%E7%A7%91%E6%8A%80TigerAI`

---

## 1. Wie man dieses Dokument verwendet

Dieses Dokument organisiert Videos vom TigerAI-Channel, die für L1-L4 Kursdesign verwendet werden können, mit besonderem Fokus auf n8n und L3 Workflow Automation.

Organisations-Ansatz:

1. Lern-Zusammenfassungen basierend auf dem öffentlich verfügbaren Video-Catalog und Titeln aufbauen.
2. Videos auf L1 / L2 / L3 / L4 Kursnutzungen mappen.
3. Die n8n-Videos in L3 Kursmodule und eine PoC-Roadmap organisieren.
4. Die OpenGenie-Videos in einen Adoption-Thread organisieren, der Enterprise Governance, Accounts, Permissions, Modelle, Prompts, Channels, n8n-Integration, RAG/Vision und Feedback-Systeme abdeckt.

Priorität:

| Priorität | Beschreibung |
|---|---|
| P0 | Must-Watch für den L3 n8n Core-Kurs |
| P1 | Wichtiger unterstützender Inhalt für L1 / L2 / L3 / L4 |
| P2 | Industrie- oder Abteilungs-spezifischer Wahl-Case |
| P3 | Demo oder Inspirations-Case |

---

## 2. Gesamtschlussfolgerung für den L3-Kurs

Die TigerAI n8n-Videos sind nicht einfach Tool-Tutorials; sie sind eine komplette Enterprise Process Automation Case Library. Die L3 Training-Logik, die sie offenbaren, sollte sein:

> Aufnehmen, wo die L2-produzierte Skill / Workflow Blueprint aufhört, und n8n verwenden, um sie in einen Prozess-PoC zu verwandeln, der ausführbar, verifizierbar, gesichert, betreibbar und plattformübergreifend integrierbar ist.

Daher sollte der L3-Kurs betonen:

1. Trigger: Webhook, Schedule, Gmail, LINE, Facebook, YouTube, GCS / API Event.
2. Data Handling: Data Tables, Sheets, BigQuery, CRM / ERP / API-Daten.
3. AI Processing: Gemini, Bilder, Audio, Video, Dokumente, Copywriting, Zusammenfassung, Klassifikation.
4. Platform Integration: LINE, Facebook, YouTube, soziale Plattformen, Gmail, GitHub.
5. Reuse: Sub-Workflow Modularisierung.
6. Governance: Credentials, Execution Log, GitHub Backup, Human Review, Error Handling.
7. L4 Readiness: Hermes Agent in die Lage versetzen, n8n Workflows in Zukunft aufzurufen.

---

## 3. OpenGenie Enterprise Governance Video-Zusammenfassungen

| # | Video | Lern-Zusammenfassung | Kurs-Anwendung | Priorität |
|---:|---|---|---|---|
| OG-1 | [TigerAI OpenGenie 單元 1：帳號體系與權限佈署](https://www.youtube.com/watch?v=wkgx94TmFE4) | Account-, User- und Permission-Deployment. | L1 OpenWebUI / OpenGenie Enterprise Enablement; deckt Per-Person Accounts und Permission Governance ab. | P1 |
| OG-2 | [單元 2：後端模型 Ollama 管理與安裝](https://www.youtube.com/watch?v=fyK8lIBEdoU) | Back-End Modell-Installation und Management. | L1 IT / Admin Model Management; unterstützt Cloud AI / Hybrid / vollständig on-premise Entscheidungen. | P1 |
| OG-3 | [單元 3：API Key 彈性配置](https://www.youtube.com/watch?v=IdI_pqRjEOU) | API Key und Cloud-Assist Strategie. | L1/L3 IT; managed Model Providers, externe APIs und Permissions. | P1 |
| OG-4 | [單元 4：Prompts 專家設定](https://www.youtube.com/watch?v=CZwXcgtKn0Y) | Expert Prompt Konfiguration. | L1 Prompt Library; L2 Skill-Isierung. | P1 |
| OG-5 | [單元 5：群組與協作權限深度管理](https://www.youtube.com/watch?v=G1MKa10W6K0) | Groups und Collaboration Permissions. | L1 Admin / L3 Prozess-Permission-Design. | P1 |
| OG-6 | [單元 6：Channels 協作與會議摘要](https://www.youtube.com/watch?v=38kkwwRDOpU) | Channels, Collaboration und Meeting Summaries. | L1 Abteilungs-Collaboration, L2 Meeting Summary Skill, L3 Meeting Flow. | P2 |
| OG-7 | [單元 7：n8n 串接與自動化工作流](https://www.youtube.com/watch?v=xX6e0l-TaWg) | OpenGenie und n8n Integration; Automated Workflows. | Core des L3 Hauptkurses, dient als L3 Entry-Video. | P0 |
| OG-8 | [單元 8：多模態進階應用 RAG & Vision](https://www.youtube.com/watch?v=qN_2KSgbjUM) | RAG, Vision und multimodale Anwendungen. | L3 Gemini / multimodaler Flow; Vorläufer zu L4 Hermes Knowledge Work. | P1 |
| OG-9 | [單元 9：綜合應用與分享機制](https://www.youtube.com/watch?v=jQPBSZmYLbg) | Integrierte Anwendungen, Sharing und Collaboration. | L1/L3 Sharing Governance und Demo Showcase. | P2 |
| OG-10 | [單元 10：管理監督與回饋系統](https://www.youtube.com/watch?v=4Lrgg-vdhi8) | Management Supervision und Feedback. | L3 Operations, Feedback, Quality Improvement und Gate 3 Acceptance. | P1 |

---

## 4. Antigravity / L2 Video-Zusammenfassungen

| # | Video | Lern-Zusammenfassung | Kurs-Anwendung | Priorität |
|---:|---|---|---|---|
| AG-1 | [1部曲：AI 全自動寫代碼、測試還幫你錄影](https://www.youtube.com/watch?v=LCO700FzoXg) | Antigravity Foundation; AI schreibt Code, testet, zeichnet Evidence auf. | L2 Antigravity Foundation. | P1 |
| AG-2 | [2部曲：AI 寫 Code 鬼打牆怎麼辦](https://www.youtube.com/watch?v=RRWtnqqQI0E) | Debugging-Mindset; Skill Plugin Extension. | L2 Debug / Skill-Isierung. | P1 |
| AG-3 | [3部曲：開發環境零手動](https://www.youtube.com/watch?v=kHywZFPsju8) | AI installiert Packages und UI. | L2 Engineering Practice. | P1 |
| AG-4 | [4部曲：爬蟲與架站](https://www.youtube.com/watch?v=K4UMhFj9ztE) | Data Scraping und ein customized Web UI. | L2 App Prototyp; L3 kann Data Flows von hier aufnehmen. | P1 |
| AG-5 | [5部曲：Docker 容器化與打包](https://www.youtube.com/watch?v=IILRXP2cMbo) | Docker Containerisierung. | L2 Engineering Deliverable und L3 Deployment Vorläufer. | P1 |
| AG-6 | [6部曲：互動 App 與個人專屬 Skill](https://www.youtube.com/watch?v=q9rNgnqNXlc) | Eine interaktive App und persönlichen Skill bauen. | L2 Skill Library und L2-zu-L3 Bridge. | P1 |

---

## 5. n8n / L3 Video-Zusammenfassungen

| # | Video | Lern-Zusammenfassung | L3 Kurs-Anwendung | Priorität |
|---:|---|---|---|---|
| N27 | [不寫程式也能用 Gemini：n8n 整合 Google Gemini 全攻略](https://www.youtube.com/watch?v=DT5Gx5tMxGs) | n8n verwenden, um Gemini für Bilder, Audio, Video und Dokumente zu integrieren. | L3 AI Node / multimodale Processing Foundation. | P0 |
| N28 | [n8n 進階教學：Sub-workflow 模組化自動化術](https://www.youtube.com/watch?v=hbvHwjrexds) | Wiederverwendbare Sub-Workflows bauen. | Must-Watch für L3 Modularisierung und Prozess-Standardisierung. | P0 |
| N29 | [AI 即時查詢神器：高鐵時刻查詢機器人](https://www.youtube.com/watch?v=T1hzDrIhHSk) | LINE Auto-Reply für Schedule, Fares und Timetable. | Case für Webhook / LINE / API Query Flow. | P0 |
| N30 | [AI 人資革命：自動履歷篩選系統](https://www.youtube.com/watch?v=EgSFZm6hvE8) | n8n + Gemini + Gmail + LINE HR Prozess. | HR-Prozess PoC: Resume Intake, AI Screening, Notifications. | P0 |
| N31 | [史上最強社群自動化](https://www.youtube.com/watch?v=Eb-DwLnNjUk) | Produkt-Bild zu Video, Copywriting, Multi-Platform Marketing. | Marketing-Automatisierungs PoC. | P2 |
| N32 | [AI 自動發文 2.0](https://www.youtube.com/watch?v=hlhByT2m28M) | Video-Generierung, Copywriting, Multi-Platform Publishing. | Social Posting Workflow; erfordert ein Human Review Gate. | P2 |
| N33 | [YouTube AI 留言機器人](https://www.youtube.com/watch?v=3cB4BtGUA9w) | YouTube Auto-Reply Comments und Keyword-Interaktion. | Social-Interaktion und Customer Service Flow. | P2 |
| N34 | [n8n 終極備份術](https://www.youtube.com/watch?v=zrsE4-G6MRY) | Auto-Syncing Workflows + Credentials zu GitHub. | Must-Watch für L3 Operations, Backup und Version Governance. | P0 |
| N35 | [Facebook 聊天機器人實戰](https://www.youtube.com/watch?v=c9VuLN_DasA) | Einen Facebook AI Customer Service Bot mit n8n + Webhook bauen. | Main Case für Customer Service Automation. | P0 |
| N36 | [Data Tables 實戰：Facebook 智能客服](https://www.youtube.com/watch?v=v4plNZNSG08) | n8n Data Tables, Meta-Plattform-Integration, customized AI Replies. | Must-Watch für L3 Data Tables und State Management. | P0 |
| N37 | [AI 客服升級版：FB 粉專自動回圖、回訊息](https://www.youtube.com/watch?v=pEWn2yh1Dkg) | Bild- und Message-Replies für Facebook Customer Service. | Optionaler multimodaler Customer Service. | P2 |
| N38 | [AI 自動行銷機器人](https://www.youtube.com/watch?v=njcKlnhEaUM) | Freepik + DataForSEO: Auto Image Sourcing, Copywriting, Keyword Selection, Posting. | Marketing Content Supply Chain Flow. | P2 |
| N39 | [Sora 2 全自動影片工廠](https://www.youtube.com/watch?v=3NJZ99lY8kU) | n8n + Kie AI: One-Click Video-Generierung und Publishing zu FB, IG, Threads, YouTube. | Advanced Video Factory Case; erfordert Review und Brand Gates. | P3 |

---

## 6. L3 Kursdesign-Implikationen

### 6.1 Wir können nicht nur n8n-Basics lehren

Die TigerAI-Videos zeigen, dass das wirklich Wertvolle in L3 nicht „Nodes ziehen" ist, sondern einen vollständigen Closed Loop im Prozess zu bilden:

`Trigger → Data → AI → System Action → Human Gate → Log → Backup → Reuse`

### 6.2 L3 muss vier Case-Pools haben

| Case Pool | Repräsentative Videos | Geeignete Kunden |
|---|---|---|
| Customer Service Automation | N35, N36, N37 | Services, E-Commerce, Fan Pages, Customer Service Centers |
| HR Automation | N30 | HR, Recruitment, HR Shared Services |
| Marketing Automation | N31, N32, N33, N38, N39 | Marketing, Content, Social, Brand |
| Query / Utility Bot | N29 | Operations, Customer Service, interne Queries |

### 6.3 L3 muss einen Governance-Kurs hinzufügen

Das GitHub Backup in Video N34 ist sehr wichtig und sollte ein erforderlicher Teil von L3 sein, kein Wahlfach. Nachdem Unternehmen n8n adoptieren, ohne Backups, Versionierung, Credential Management, Execution Logs und Error Notifications wird der PoC leicht zu einem nicht wartbaren Spielzeug.

---

## 7. Empfohlene Viewing-Pfade

### 7.1 L3 Core Track

1. OG-7: OpenGenie und n8n Integration.
2. N27: n8n + Gemini multimodal.
3. N28: Sub-Workflows.
4. N34: GitHub Backup.
5. N35: Facebook Webhook Customer Service.
6. N36: Data Tables.

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

## 8. Anwendung auf Delivery

TigerAI-Videos sollten in die folgenden Deliverables verwandelt werden:

- L3 n8n Workflow Blueprint.
- n8n Workflow JSON.
- Credential / API / Webhook Permission Sheet.
- Data Tables Schema.
- Sub-Workflow Library.
- Execution Log und Test Records.
- GitHub Backup und Version Management SOP.
- Human Gate Design.
- Error Handling / Retry / Fallback Design.
- Liste von Workflows, die vom L4 Hermes Agent aufgerufen werden können.
