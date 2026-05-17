# Notas de aprendizaje de video OpenWebUI y resumen de aplicación

> 🌐 Idioma: [繁體中文](OPENWEBUI_VIDEO_LEARNING_NOTES.md) ｜ [English](OPENWEBUI_VIDEO_LEARNING_NOTES_EN.md) ｜ [Deutsch](OPENWEBUI_VIDEO_LEARNING_NOTES_DE.md) ｜ [Français](OPENWEBUI_VIDEO_LEARNING_NOTES_FR.md) ｜ Español ｜ [日本語](OPENWEBUI_VIDEO_LEARNING_NOTES_JA.md) ｜ [한국어](OPENWEBUI_VIDEO_LEARNING_NOTES_KR.md)

Versión: v1.0
Notas por: Morris Lu (盧業興) · Tiger AI 虎智科技
Propósito: Convertir la playlist pública OpenWebUI en notas de aprendizaje, resúmenes y un mapa de aplicación futura para el curso de onboarding empresarial L1.

## 原始影片版權聲明 / Third-Party Video Credits

> **本文件為第三方公開影片的學習筆記，並非影片本身。所有影片內容與版權皆歸原始創作者所有，本文件僅作為學習與課程設計用途引用其公開連結。**
>
> **Este documento contiene notas de estudio derivadas de videos de terceros disponibles públicamente. NO es una transcripción o reproducción. Todo el contenido de video y copyrights permanecen con los creadores originales; los enlaces se citan aquí únicamente para referencia educativa y de diseño de curso.**

- **原始 Playlist / Playlist original**: <https://www.youtube.com/watch?v=oXJ4L1G8kaI&list=PL_rTgQnnMXsXAsEiid-tWhaj03SsP4U5Z>
- Enlace original y título de cada video citados individualmente en las tablas a continuación; por favor referirse a la fuente original para contenido autoritativo.

Si usted es titular de derechos y desea actualizar la atribución o solicitar la eliminación de cualquier cita, por favor abra un issue en este repositorio.

---

## 1. Cómo usar este documento

Este documento no es una transcripción; es un registro de aprendizaje para diseño de curso. Cada video se mapea a:

1. El tema del video.
2. Un resumen de aprendizaje.
3. Su aplicación futura dentro de la metodología TigerAI L1-L5.
4. Una prioridad de curso.

Definiciones de prioridad:

| Prioridad | Descripción |
|---|---|
| P0 | Must-watch para enablement empresarial L1; afecta directamente cuentas, login, uso, permisos y seguridad de datos |
| P1 | Must-watch para Admin / IT; afecta despliegue, modelos, operations, permisos y updates |
| P2 | Funcionalidad opcional; incluida según necesidades del cliente |
| P3 | Caso inspiracional; usable para demos o como extensión L2/L3/L4 follow-on |

---

## 2. Conclusión general para el curso L1

OpenWebUI no debe simplemente empaquetarse como "alternativa gratuita a ChatGPT". Durante la adopción empresarial, su valor core es:

> Un entry point controlado a través del cual la empresa gestiona el uso IA. Cada empleado tiene su propia cuenta y zona de chat, y el Admin puede gestionar roles, grupos, permisos, modelos, herramientas y fronteras de datos.

Por lo tanto, el hilo principal del curso L1 debe ser:

1. Cada persona se loguea individualmente; sin cuentas compartidas.
2. Cada persona tiene su propio historial de chat, carpetas, Prompts y settings personales.
3. El Admin puede gestionar users, roles, grupos, permisos y visibilidad de modelos.
4. IT puede decidir sobre modelos locales, APIs cloud, modo Hybrid y estrategias de update operacional.
5. HR / management puede establecer guidelines de uso IA y fronteras de entrada de datos.
6. El output L1 debe puentear hacia L2: organizar Prompts de alta-frecuencia y escenarios de trabajo en candidatos Skill.

---

## 3. Resúmenes de aprendizaje de video y aplicaciones futuras

| # | Video | Resumen de aprendizaje | Aplicación futura | Prioridad |
|---:|---|---|---|---|
| 1 | [Open WebUI: The Free, Private ChatGPT Alternative](https://www.youtube.com/watch?v=oXJ4L1G8kaI) | Posicionamiento, valor y escenarios de uso básico de OpenWebUI. | Sesión de apertura L1, usada para explicar por qué la empresa necesita su propio entry point IA. | P0 |
| 2 | [How to Install OpenWebUI](https://www.youtube.com/watch?v=d6Su3Nmv7-8) | Flow de instalación fundacional para OpenWebUI. | Preparación pre-curso IT, setup de ambiente PoC, checklist de despliegue. | P1 |
| 3 | [Local AI Model Requirements](https://www.youtube.com/watch?v=CYBu9dTVWC4) | Conceptos de CPU, RAM y GPU requeridos para modelos locales. | Evaluación de despliegue Cloud AI / Hybrid / completamente on-premise; ayuda a clientes a juzgar umbrales hardware. | P1 |
| 4 | [Exploring the OpenWebUI Admin Panel](https://www.youtube.com/watch?v=4pIzLtUhJLM) | Vista general de funcionalidades del Admin Panel y entry points de gestión. | Must-watch para el curso L1 Admin; cubre gestión de cuenta, modelo, funcionalidad y settings. | P0 |
| 5 | [Exploring Open WebUI: Features, Models, & Tools](https://www.youtube.com/watch?v=CDiVq3mPZc8) | Vista general de funcionalidades, modelos y herramientas OpenWebUI. | Tour L1 all-hands, para que los trainees entiendan funcionalidades y fronteras disponibles. | P0 |
| 6 | [How to Chat with Your Own Documents](https://www.youtube.com/watch?v=lqKapMX2GAI) | Usar documentos propios para chat y Q&R. | Resumen de documento L1 y Q&R de documento low-sensitivity; datos altamente sensibles requieren guidelines separadas. | P0 |
| 7 | [How to Add Real-Time Web Search](https://www.youtube.com/watch?v=_KoifHHJhNY) | Añadir Web Search en tiempo real. | Escenarios research, sales y marketing; la empresa debe fijar reglas de citación de fuente y permisos. | P2 |
| 8 | [How to Add GPT-4 to OpenWebUI](https://www.youtube.com/watch?v=ZUc50fcWO2E) | Integrar modelos clase OpenAI API / GPT-4. | Setup cloud model provider Admin / IT; usable en arquitectura Hybrid. | P1 |
| 9 | [How to Use Community Tools](https://www.youtube.com/watch?v=juAbnns5Ohg) | Extender capabilities con community tools. | Precursor a L2/L3; la empresa debe primero hacer security review y whitelisting de herramientas. | P2 |
| 10 | [Text-to-Speech with ElevenLabs API](https://www.youtube.com/watch?v=LzlzXQzBUcg) | Integrar TTS y output audio. | Opcional para customer service, educación y materiales de training; no L1 core. | P2 |
| 11 | [How to Create Custom AI Models](https://www.youtube.com/watch?v=Fd_1zePgCLE) | Crear settings de modelo customizados o personas de modelo. | Modelos default departamentales, asistentes persona-based; puentea hacia L2 Skills. | P2 |
| 12 | [AI Images with OpenWebUI & DALL-E 3](https://www.youtube.com/watch?v=3rg8Tdyn_RA) | Capability de generación de imagen. | Opcional para marketing y diseño; requiere atención a copyright, brand y review. | P2 |
| 13 | [LLAVA Multimodal / GPT-4 Image Analysis](https://www.youtube.com/watch?v=yZkmolyV0Zk) | Usar modelos multimodales para analizar imágenes. | Exploración preliminar para QC, healthcare y document imaging; escenarios high-risk requieren human review. | P2 |
| 14 | [AI Clone](https://www.youtube.com/watch?v=dXaFbHw5-m8) | Demo de un AI clone personalizado. | Demo inspiracional; adopción empresarial requiere handling especial de privacy y licensing de likeness/voice. | P3 |
| 15 | [Functions to Build Websites & Apps](https://www.youtube.com/watch?v=KbkfaapAvpE) | Extender capability de aplicación con Functions. | Extensión L2/L3: convertir capability chat en herramientas ejecutables o prototipos de app. | P2 |
| 16 | [Reduce AI Hallucinations with Advanced Parameters](https://www.youtube.com/watch?v=OWsFsnnrMdE) | Usar advanced parameters para reducir riesgo de alucinación. | Must-watch para L1; usado para data trustworthiness, verificación humana y educación de parámetros de modelo. | P0 |
| 17 | [Choosing the Right Ollama Model](https://www.youtube.com/watch?v=KIc1lRmehyY) | Elegir el modelo Ollama local correcto. | Gestión de modelo IT / Admin y evaluación de despliegue on-premise. | P1 |
| 18 | [Mobile Access with Ngrok](https://www.youtube.com/watch?v=DFtI1m957XM) | Acceso remote o mobile a OpenWebUI vía Ngrok. | Opcional; la empresa debe considerar seguridad, VPN, exposure surface y access control. | P2 |
| 19 | [Choosing the Best Language Model](https://www.youtube.com/watch?v=-yhChXlYjbQ) | Métodos para seleccionar entre diferentes modelos de lenguaje. | Gestionar catálogo de modelos y modelos apropiados al departamento; puentea a model evaluation sheet. | P1 |
| 20 | [Vision LLMs for Local Inference](https://www.youtube.com/watch?v=VDLNtKbfewQ) | Comparación de modelos vision locales. | Exploración para QC, documentos imagen e imágenes médicas; contenido opcional avanzado. | P2 |
| 21 | [AI Recruiter Meets AI Clone](https://www.youtube.com/watch?v=649qtKjbnk4) | Escenario demo de reclutamiento con AI clone. | Caso inspiracional HR; convertible en Skill de reclutamiento L2 o workflow de reclutamiento L3. | P3 |
| 22 | [Groq Cloud & OpenWebUI](https://www.youtube.com/watch?v=Ukft9qfb67o) | Integrar modelos cloud como Groq Cloud. | Estrategia multi-model provider IT / Admin. | P1 |
| 23 | [Docker & Watchtower](https://www.youtube.com/watch?v=W0Yh_HsMkOQ) | Auto-updates y operations de container Docker. | Must-watch para operations IT; cubre updates OpenWebUI y estabilidad de servicio. | P1 |
| 24 | [OpenWebUI Pipelines](https://www.youtube.com/watch?v=DFlSd6GrMIk) | Capability workflow Custom Pipelines. | Preview L3; puede puentear después a n8n, APIs y pipelines de procesamiento de datos. | P2 |
| 25 | [Set Up User Roles for Secure Collaboration](https://www.youtube.com/watch?v=xlE782FrW_s) | Set up user roles y colaboración segura. | Must-watch para L1 Admin; cubre cuentas per-person, roles, grupos y permisos. | P0 |
| 26 | [Writing Better Prompts](https://www.youtube.com/watch?v=FYTir7cor1c) | Escribir mejores Prompts. | Must-watch para todo L1; puentea a Prompt Library y candidatos Skill L2. | P0 |
| 27 | [Arena Model](https://www.youtube.com/watch?v=PU7B5FHalrg) | Comparación de modelo y testing de performance. | Usado por Admin / seed users para evaluación de modelo y decisiones de procurement. | P1 |
| 28 | [Run Text-to-Speech Locally](https://www.youtube.com/watch?v=lwk0QGLou9Y) | TTS local. | Opcional para necesidades de voz high-privacy; no L1 core. | P2 |
| 29 | [OpenWebUI Memory Explained](https://www.youtube.com/watch?v=a0H2w5z_uk4) | Conceptos de memory y personalización. | Puede servir como introducción a capability de personalización; la empresa debe abordar privacy, deletion y data retention policy. | P2 |
| 30 | [Quantization](https://www.youtube.com/watch?v=7J-AKL2TAD0) | Quantization de modelo y mejora de performance. | Opcional para IT; soporta despliegue on-premise y control de costo. | P2 |
| 31 | [AI-Powered Recruiter Bot](https://www.youtube.com/watch?v=XPeZGo6McLc) | Construir un recruiter bot. | Caso HR / L2 / L3: análisis de puesto, resumen de CV, drafting de preguntas de entrevista. | P3 |
| 32 | [Open WebUI v0.4 Updates](https://www.youtube.com/watch?v=qESVuLFHYqI) | Updates de versión y nuevas funcionalidades. | Awareness de versión IT / Admin; establecer un SOP de check de update. | P1 |
| 33 | [Anthropic Claude Models in OpenWebUI](https://www.youtube.com/watch?v=1jahR-BA6Ts) | Integrar modelos Claude. | Setup multi-provider Admin / IT; apto para estrategia de modelo Hybrid. | P1 |
| 34 | [Public Access to OpenWebUI Chatbots](https://www.youtube.com/watch?v=0pyHYhzqdRQ) | Acceso Public Chatbot. | Funcionalidad high-risk; la empresa debe gobernar estrictamente. Apto para discusión pre-PoC sobre customer service externo. | P2 |
| 35 | [Tools, Functions & Pipelines Deep Dive](https://www.youtube.com/watch?v=wRkAko8yphs) | Deep dive en Tools, Functions y Pipelines. | Preview L2/L3; lleva OpenWebUI de un entry point chat a herramientas y workflows. | P2 |
| 36 | [Online? Offline? Both?](https://www.youtube.com/watch?v=W9czUS3trMU) | Discusión de modos online, offline y hybrid. | Must-watch para discusión de modo de despliegue L1; cubre cloud AI / Hybrid / completamente on-premise. | P0 |

---

## 4. Rutas de visualización recomendadas

### 4.1 Todos los usuarios L1

Visualización recomendada:

1. #1 Posicionamiento OpenWebUI.
2. #5 Vista general funcionalidades, modelos y herramientas.
3. #6 Chat documentos.
4. #16 Reducir alucinaciones y advanced parameters.
5. #26 Escritura de Prompt.
6. #36 Modos online / offline / hybrid.

Propósito: Habilitar a empleados loguearse seguramente, construir su propia zona de chat, completar tareas diarias y entender fronteras de datos.

### 4.2 Admin / IT

Visualización recomendada:

1. #2 Instalación.
2. #3 Requerimientos hardware modelo local.
3. #4 Admin Panel.
4. #8 OpenAI API.
5. #17 Modelos Ollama.
6. #19 Selección de modelo.
7. #22 Groq Cloud.
8. #23 Docker / Watchtower.
9. #25 User Roles.
10. #32 Updates de versión.
11. #33 Modelos Claude.

Propósito: Habilitar a IT construir, operar, gestionar y gobernar OpenWebUI.

### 4.3 Extensiones L2 / L3

Visualización recomendada:

1. #9 Community Tools.
2. #11 Custom AI Models.
3. #15 Functions.
4. #24 Pipelines.
5. #35 Tools / Functions / Pipelines Deep Dive.

Propósito: Puentear OpenWebUI de un entry point Chat L1 a Skills L2 y Workflows L3.

### 4.4 Industria / Departamento Electivos

| Industria / Departamento | Videos recomendados |
|---|---|
| HR | #21, #31 |
| Marketing / Diseño | #12 |
| Customer Service / Educación y Training | #10, #28 |
| QC / Healthcare / Documentos Imagen | #13, #20 |
| Empresas High-Privacy | #3, #17, #23, #30, #36 |

---

## 5. Aplicación a cursos y entrega

### 5.1 Aplicación al curso L1

Debe convertirse en los siguientes deliverables de curso:

- Manual de operaciones de usuario OpenWebUI.
- Runbook Admin OpenWebUI.
- Sheet de configuración de cuenta / grupo / permiso / visibilidad de modelo.
- Guidelines de uso IA.
- Prompt Library v1.
- Sheet de acceptance Gate 1.

### 5.2 Aplicación al curso L2

Los siguientes videos pueden convertirse en candidatos Skill:

- #26 Escritura de Prompt → Skill Prompt.
- #6 Chat documentos → Skill resumen de documento.
- #11 Custom AI Models → Skill modelo persona departamental.
- #15 Functions → Skill tool-ificado.
- #35 Tools / Functions / Pipelines → Bridge L2-a-L3.

### 5.3 Aplicación al curso L3

Los siguientes videos pueden convertirse en candidatos Workflow:

- #7 Web Search → Workflow market research.
- #24 Pipelines → flow de procesamiento custom.
- #35 Tools / Functions / Pipelines → puenteo flow OpenWebUI + n8n.
- #34 Public Chatbots → PoC bot customer service externo, pero requiere permisos estrictos y review.

---

## 6. Notas de adopción empresarial

1. Las cuentas no deben compartirse; de lo contrario zonas de chat per-person, accountability y governance de permisos son imposibles.
2. Los nuevos usuarios no deben obtener funcionalidades avanzadas por defecto; review Admin es recomendada.
3. File Upload, Web Search, Tools, Functions, Pipelines y Public Share deben todos tratarse como funcionalidades avanzadas.
4. Cada departamento debe tener su propio grupo y estrategia de visibilidad de modelo.
5. Las industrias altamente sensibles deben primero determinar modo de despliegue cloud AI / Hybrid / completamente on-premise.
6. Capabilities memory y personalización requieren políticas de privacy, deletion y data retention.
7. Public Chatbots o acceso externo no deben abrirse ampliamente en L1; un PoC separado es requerido.
8. Cada update de versión debe refrescar el Admin Runbook y usage guidelines.
