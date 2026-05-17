# Notas de aprendizaje de video canal TigerAI y resumen de aplicación L3

> 🌐 Idioma: [繁體中文](TIGERAI_VIDEO_LEARNING_NOTES.md) ｜ [English](TIGERAI_VIDEO_LEARNING_NOTES_EN.md) ｜ [Deutsch](TIGERAI_VIDEO_LEARNING_NOTES_DE.md) ｜ [Français](TIGERAI_VIDEO_LEARNING_NOTES_FR.md) ｜ Español ｜ [日本語](TIGERAI_VIDEO_LEARNING_NOTES_JA.md) ｜ [한국어](TIGERAI_VIDEO_LEARNING_NOTES_KR.md)

Versión: v1.0
Autor: Morris Lu (盧業興) · Tiger AI 虎智科技
Canal: 虎智科技 TigerAI
Canal original: `https://www.youtube.com/@%E8%99%8E%E6%99%BA%E7%A7%91%E6%8A%80TigerAI`

---

## 1. Cómo usar este documento

Este documento organiza videos del canal TigerAI que pueden usarse para diseño de cursos L1-L4, con enfoque particular en n8n y L3 Workflow Automation.

Enfoque de organización:

1. Construir resúmenes de aprendizaje basados en catálogo de videos públicamente disponible y títulos.
2. Mapear videos a usos de cursos L1 / L2 / L3 / L4.
3. Organizar los videos n8n en módulos de curso L3 y una roadmap PoC.
4. Organizar los videos OpenGenie en un thread de adopción cubriendo gobernanza empresarial, cuentas, permisos, modelos, Prompts, Channels, integración n8n, RAG/Vision y sistemas de feedback.

Prioridad:

| Prioridad | Descripción |
|---|---|
| P0 | Must-watch para el curso core L3 n8n |
| P1 | Contenido de soporte importante para L1 / L2 / L3 / L4 |
| P2 | Caso electivo específico de industria o departamento |
| P3 | Caso demo o inspiracional |

---

## 2. Conclusión general para el curso L3

Los videos TigerAI n8n no son simplemente tutoriales de herramienta; son una biblioteca de casos completa de automatización de procesos empresariales. La lógica de entrenamiento L3 que revelan debe ser:

> Retomar donde el Skill / Workflow Blueprint producido en L2 termina, y usar n8n para convertirlo en un PoC de proceso que sea ejecutable, verificable, respaldado, operable e integrable inter-plataformas.

Por lo tanto el curso L3 debe enfatizar:

1. Trigger: Webhook, schedule, Gmail, LINE, Facebook, YouTube, GCS / API event.
2. Data Handling: Data Tables, Sheets, BigQuery, CRM / ERP / API data.
3. AI Processing: Gemini, imágenes, audio, video, documentos, copywriting, resumen, clasificación.
4. Platform Integration: LINE, Facebook, YouTube, plataformas sociales, Gmail, GitHub.
5. Reuse: Modularización Sub-workflow.
6. Governance: Credentials, Execution Log, GitHub backup, human review, error handling.
7. L4 Readiness: Permitir a Hermes Agent llamar Workflows n8n en el futuro.

---

## 3. Resúmenes de video OpenGenie Enterprise Governance

| # | Video | Resumen de aprendizaje | Aplicación al curso | Prioridad |
|---:|---|---|---|---|
| OG-1 | [TigerAI OpenGenie 單元 1：帳號體系與權限佈署](https://www.youtube.com/watch?v=wkgx94TmFE4) | Despliegue de cuenta, usuario y permiso. | Enablement empresarial L1 OpenWebUI / OpenGenie; cubre cuentas per-person y gobernanza de permiso. | P1 |
| OG-2 | [單元 2：後端模型 Ollama 管理與安裝](https://www.youtube.com/watch?v=fyK8lIBEdoU) | Instalación y gestión de modelo back-end. | Gestión de modelo L1 IT / Admin; soporta decisiones cloud AI / Hybrid / completamente on-premise. | P1 |
| OG-3 | [單元 3：API Key 彈性配置](https://www.youtube.com/watch?v=IdI_pqRjEOU) | Estrategia API Key y cloud-assist. | IT L1/L3; gestiona proveedores de modelo, APIs externos y permisos. | P1 |
| OG-4 | [單元 4：Prompts 專家設定](https://www.youtube.com/watch?v=CZwXcgtKn0Y) | Configuración Expert Prompt. | Prompt Library L1; Skill-ización L2. | P1 |
| OG-5 | [單元 5：群組與協作權限深度管理](https://www.youtube.com/watch?v=G1MKa10W6K0) | Grupos y permisos de colaboración. | L1 Admin / diseño de permiso de proceso L3. | P1 |
| OG-6 | [單元 6：Channels 協作與會議摘要](https://www.youtube.com/watch?v=38kkwwRDOpU) | Channels, colaboración y resúmenes de reunión. | Colaboración departamental L1, Skill resumen reunión L2, flow reunión L3. | P2 |
| OG-7 | [單元 7：n8n 串接與自動化工作流](https://www.youtube.com/watch?v=xX6e0l-TaWg) | Integración OpenGenie y n8n; workflows automatizados. | Core del curso principal L3, sirviendo como video de entrada L3. | P0 |
| OG-8 | [單元 8：多模態進階應用 RAG & Vision](https://www.youtube.com/watch?v=qN_2KSgbjUM) | Aplicaciones RAG, Vision y multimodales. | L3 Gemini / flow multimodal; precursor a L4 Hermes knowledge work. | P1 |
| OG-9 | [單元 9：綜合應用與分享機制](https://www.youtube.com/watch?v=jQPBSZmYLbg) | Aplicaciones integradas, sharing y colaboración. | Gobernanza de sharing L1/L3 y demo showcase. | P2 |
| OG-10 | [單元 10：管理監督與回饋系統](https://www.youtube.com/watch?v=4Lrgg-vdhi8) | Supervisión de gestión y feedback. | Operations L3, feedback, mejora de calidad y acceptance Gate 3. | P1 |

---

## 4. Resúmenes de video Antigravity / L2

| # | Video | Resumen de aprendizaje | Aplicación al curso | Prioridad |
|---:|---|---|---|---|
| AG-1 | [1部曲：AI 全自動寫代碼、測試還幫你錄影](https://www.youtube.com/watch?v=LCO700FzoXg) | Fundación Antigravity; IA escribe código, prueba, graba evidence. | L2 Antigravity Foundation. | P1 |
| AG-2 | [2部曲：AI 寫 Code 鬼打牆怎麼辦](https://www.youtube.com/watch?v=RRWtnqqQI0E) | Mindset de debugging; extensión Skill plugin. | L2 Debug / Skill-ización. | P1 |
| AG-3 | [3部曲：開發環境零手動](https://www.youtube.com/watch?v=kHywZFPsju8) | IA instala paquetes y UI. | Práctica de engineering L2. | P1 |
| AG-4 | [4部曲：爬蟲與架站](https://www.youtube.com/watch?v=K4UMhFj9ztE) | Data scraping y un Web UI customizado. | Prototipo App L2; L3 puede retomar data flows desde aquí. | P1 |
| AG-5 | [5部曲：Docker 容器化與打包](https://www.youtube.com/watch?v=IILRXP2cMbo) | Containerización Docker. | Deliverable de engineering L2 y precursor de despliegue L3. | P1 |
| AG-6 | [6部曲：互動 App 與個人專屬 Skill](https://www.youtube.com/watch?v=q9rNgnqNXlc) | Construir un App interactivo y Skill personal. | Skill Library L2 y Bridge L2-a-L3. | P1 |

---

## 5. Resúmenes de video n8n / L3

| # | Video | Resumen de aprendizaje | Aplicación al curso L3 | Prioridad |
|---:|---|---|---|---|
| N27 | [不寫程式也能用 Gemini：n8n 整合 Google Gemini 全攻略](https://www.youtube.com/watch?v=DT5Gx5tMxGs) | Usar n8n para integrar Gemini para imágenes, audio, video y documentos. | Fundación de procesamiento L3 AI Node / multimodal. | P0 |
| N28 | [n8n 進階教學：Sub-workflow 模組化自動化術](https://www.youtube.com/watch?v=hbvHwjrexds) | Construir Sub-workflows reutilizables. | Must-watch para modularización L3 y estandarización de proceso. | P0 |
| N29 | [AI 即時查詢神器：高鐵時刻查詢機器人](https://www.youtube.com/watch?v=T1hzDrIhHSk) | LINE auto-reply para schedule, tarifas y timetable. | Caso para Webhook / LINE / API query flow. | P0 |
| N30 | [AI 人資革命：自動履歷篩選系統](https://www.youtube.com/watch?v=EgSFZm6hvE8) | Proceso HR n8n + Gemini + Gmail + LINE. | PoC proceso HR: intake CV, screening IA, notificaciones. | P0 |
| N31 | [史上最強社群自動化](https://www.youtube.com/watch?v=Eb-DwLnNjUk) | Imagen producto a video, copywriting, marketing multi-plataforma. | PoC automatización marketing. | P2 |
| N32 | [AI 自動發文 2.0](https://www.youtube.com/watch?v=hlhByT2m28M) | Generación video, copywriting, publicación multi-plataforma. | Workflow social posting; requiere un Gate de human review. | P2 |
| N33 | [YouTube AI 留言機器人](https://www.youtube.com/watch?v=3cB4BtGUA9w) | YouTube auto-reply comments e interacción keyword. | Flow de interacción social y customer service. | P2 |
| N34 | [n8n 終極備份術](https://www.youtube.com/watch?v=zrsE4-G6MRY) | Auto-sync Workflows + Credentials a GitHub. | Must-watch para operations L3, backup y gobernanza de versión. | P0 |
| N35 | [Facebook 聊天機器人實戰](https://www.youtube.com/watch?v=c9VuLN_DasA) | Construir un bot customer service Facebook AI con n8n + Webhook. | Caso principal para automatización customer service. | P0 |
| N36 | [Data Tables 實戰：Facebook 智能客服](https://www.youtube.com/watch?v=v4plNZNSG08) | n8n Data Tables, integración plataforma Meta, replies AI customizados. | Must-watch para L3 Data Tables y state management. | P0 |
| N37 | [AI 客服升級版：FB 粉專自動回圖、回訊息](https://www.youtube.com/watch?v=pEWn2yh1Dkg) | Image y message replies para customer service Facebook. | Customer service multimodal opcional. | P2 |
| N38 | [AI 自動行銷機器人](https://www.youtube.com/watch?v=njcKlnhEaUM) | Freepik + DataForSEO: auto image sourcing, copywriting, selección keyword, posting. | Flow supply chain de contenido marketing. | P2 |
| N39 | [Sora 2 全自動影片工廠](https://www.youtube.com/watch?v=3NJZ99lY8kU) | n8n + Kie AI: generación video one-click y publicación a FB, IG, Threads, YouTube. | Caso advanced video factory; requiere Gates de review y brand. | P3 |

---

## 6. Implicaciones de diseño de curso L3

### 6.1 No podemos enseñar solo bases n8n

Los videos TigerAI muestran que lo realmente valioso en L3 no es "drag nodes", sino formar un bucle cerrado completo en el proceso:

`Trigger → Data → AI → System Action → Human Gate → Log → Backup → Reuse`

### 6.2 L3 debe tener cuatro pools de casos

| Pool de casos | Videos representativos | Clientes apropiados |
|---|---|---|
| Customer service automation | N35, N36, N37 | Servicios, e-commerce, fan pages, customer service centers |
| HR automation | N30 | HR, reclutamiento, HR shared services |
| Marketing automation | N31, N32, N33, N38, N39 | Marketing, contenido, social, brand |
| Bot query / utility | N29 | Operations, customer service, queries internas |

### 6.3 L3 debe añadir un curso de gobernanza

El backup GitHub en el video N34 es muy importante y debe ser una parte requerida de L3, no electivo. Después de que las empresas adoptan n8n, sin backups, versioning, gestión de credentials, Execution Logs y notificaciones de error, el PoC fácilmente se vuelve un juguete no mantenible.

---

## 7. Rutas de visualización recomendadas

### 7.1 L3 Core Track

1. OG-7: Integración OpenGenie y n8n.
2. N27: n8n + Gemini multimodal.
3. N28: Sub-workflows.
4. N34: GitHub backup.
5. N35: Facebook Webhook customer service.
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

## 8. Aplicación a entrega

Los videos TigerAI deben convertirse en los siguientes deliverables:

- L3 n8n Workflow Blueprint.
- n8n Workflow JSON.
- Sheet de permiso Credential / API / Webhook.
- Data Tables Schema.
- Sub-workflow Library.
- Execution Log y test records.
- SOP GitHub backup y version management.
- Diseño Human Gate.
- Diseño Error Handling / Retry / Fallback.
- Lista de Workflows llamables por L4 Hermes Agent.
