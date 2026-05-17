# 90 References — Material de referencia, fuentes y reconocimientos

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Propósito de este directorio

Este directorio es la **biblioteca de referencias, centro de gobernanza de citas y lista de reconocimientos** de toda la metodología. Los directorios `00`-`07` cubren "el método y las herramientas"; este directorio responde tres preguntas:

1. **¿En qué se basan estos métodos?** (PDF original, diagramas de metodología, notas de aprendizaje en video)
2. **¿Qué contenido cita a terceros? ¿Las licencias son conformes?** (cada proyecto citado tiene su propio `*_REFERENCE.md`)
3. **¿Sobre los hombros de quién estamos?** (lista de reconocimientos)

Audiencia: consultores, revisores, equipos legales, redistribuidores, **aprendices y entusiastas que buscan los proyectos upstream**.

---

## 2. Reconocimientos: sobre qué hombros nos apoyamos

Organizados por nivel de uso en cuatro categorías: **Plataformas Core / Frameworks de consultoría / Agent & Skill / Índice de casos**. Cada "tarjeta de agradecimiento" contiene **URL upstream + dónde lo citamos + enlace al `_REFERENCE.md` completo**.

### 2.1 Plataformas Core (la base de runtime para L1-L5)

Estas no son "material citado" — son **las plataformas sobre las que corren los cursos L1-L5**. Sin ellas, esta metodología no puede aterrizar.

#### 🎯 [`open-webui/open-webui`](https://github.com/open-webui/open-webui) (open-source, licencia: ver LICENSE upstream)

- **Qué es**: interfaz de chat IA empresarial open-source y auto-hospedable. Soporta múltiples proveedores LLM (OpenAI / Anthropic / Ollama / OpenRouter / Azure, etc.), cuentas / grupos / roles / permisos, espacios de chat personales, control de modelos, pipelines, function calling, bases de conocimiento, RAG, carga de imagen/audio/archivo.
- **Por qué lo apreciamos**: una de las pocas soluciones open-source que hace que "**el punto de entrada de chat IA interno de la empresa**" sea "**instalable con un clic, completamente on-prem, con permisos por niveles, auditable**". Permite a las empresas probar LLMs sin enviar datos a SaaS — crítico para despliegues on-prem en manufactura / salud / gobierno. Comunidad activa, evolución rápida de versiones.
- **Dónde lo usamos**: **la plataforma core de L1 Controlled AI Access** — plan de curso completo en [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md); notas de video en [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md).

#### 🎯 [`n8n-io/n8n`](https://github.com/n8n-io/n8n) (Sustainable Use License, ver LICENSE.md upstream)

- **Qué es**: plataforma de automatización de workflows open-source. Editor visual, 1000+ integraciones (Gmail, Sheets, Notion, Slack, CRM, API, ERP, bases de datos, webhooks, nodos personalizados), librería de sub-workflows, data tables, logs de ejecución, manejo de errores, triggers programados, nodos AI / LangChain. Soporta self-host y cloud.
- **Por qué lo apreciamos**: los "**bloques LEGO**" de la automatización inter-sistemas — los consultores pueden ensamblar un PoC en 1-2 días para demos de cliente. Comunidad activa, plantillas ricas, modelo de negocio saludable. **El self-hosting es crítico para la adopción empresarial** (los datos quedan internos). El autor de la metodología también es n8n Taipei Ambassador.
- **Dónde lo usamos**: **el motor core de L3 Workflow Automation** — plan de curso completo en [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md); 35 specs de PoC implementables en [`../02_Course_Design/POC_SCENARIO_SPECS.md`](../02_Course_Design/POC_SCENARIO_SPECS.md); 30 esqueletos JSON de workflow en [`../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md`](../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md); notas de video en [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md).

#### 🎯 [`nousresearch/hermes-agent`](https://github.com/nousresearch/hermes-agent) (Nous Research, ver LICENSE upstream)

- **Qué es**: implementación de referencia open-source de Nous Research para un **Knowledge-grade Autonomous Agent** — **Wiki-Capability-Map-Memory + ingest / query / update en tres pasos para Knowledge-Compounding + tareas programadas + Gate 4A-4E + HITL Human Review**. Objetivo de diseño: un "super-asistente IA agent totalmente autónomo" verificable.
- **Por qué lo apreciamos**: integra "**Autonomous Agent + Knowledge Management**" en un design pattern verificable — los **"Siete principios de diseño para Knowledge-grade Agents"** (light-day-heavy-night / Knowledge-Compounding-Loop / P1>P2 / Write-Read-Same-Source / Tool-vs-LLM-Division / Failure-driven Learning / Why-not-just-RAG) ofrecen un framework de aprendizaje completo para L4 Agent Design.
- **Dónde lo usamos**: **la columna vertebral del diseño del curso L4 Autonomous Agent** — [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) §2 explica los siete principios. **Límite**: el curso **solo toma conceptos y design patterns — sin reproducción de código fuente, sin fork**.

#### 🎯 [`HKUDS/ClawTeam`](https://github.com/HKUDS/ClawTeam) (HKUDS, MIT)

- **Qué es**: **framework open-source de Colaboración Multi-Agente** del HKU Data Science Lab (HKUDS). Arquitectura de cinco capas (Team / Workspace / Task / Inbox / Transport), git worktree para workspaces de Agent aislados; CLI-driven; tres escenarios de referencia.
- **Por qué lo apreciamos**: empuja "Multi-Agent Team Collaboration" de escala demo a "**colaboración auditable en workflow real**" — cada agente tiene su propio worktree, su propio inbox, su propio transport. No es un toy-demo estilo chat, sino más cercano a la división real de trabajo organizacional. Fondo académico (HKUDS) + licencia MIT.
- **Dónde lo usamos**: **la plataforma de implementación para L5 Multi-Agent Organization** — plan de curso completo en [`../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md`](../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md); walkthrough Manufacturing QA Team en [`../04_Scenarios/CLAWTEAM_WALKTHROUGH.md`](../04_Scenarios/CLAWTEAM_WALKTHROUGH.md).
- **Cita completa**: [`CLAWTEAM_REFERENCE.md`](CLAWTEAM_REFERENCE.md)

### 2.2 Frameworks de consultoría (influye en 03_Consulting_Report)

#### 🎯 [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant) (MIT)

- **Qué es**: organización programática de frameworks clásicos de análisis de consultoría (MECE, Pyramid Principle, Issue Tree, Porter's 5 Forces, SWOT, BCG Matrix, 5 Whys, Fishbone, Business Model Canvas, WBS/RACI, NPV/IRR, Lean/Six Sigma, etc. — 50+ frameworks)
- **Por qué lo apreciamos**: transforma frameworks de consultoría dispersos en una **biblioteca estructurada, citable y componible** — no es otra colección de PPT más
- **Dónde lo usamos**: [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) — adaptado en 7 categorías + selector de framework + mapping a 8 etapas
- **Cita completa**: [`CONSULTANT_FRAMEWORKS_REFERENCE.md`](CONSULTANT_FRAMEWORKS_REFERENCE.md)

#### 🎯 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills) (MIT)

- **Qué es**: transforma el oficio de producción "**Problema → Reporte / Deck**" de top consultores como McKinsey en un workflow ejecutable de 8 pasos
- **Por qué lo apreciamos**: el primero en poner por escrito todo el set "Dummy Page → Dependency Management → 7 Page Layouts → Progressive Disclosure → Troubleshooting" en una SOP enseñable — en lugar de "oficio implícito que solo tienen los seniors"
- **Dónde lo usamos**: [`../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) — adaptado en workflow de consulting report de 8 pasos + §9 Troubleshooting Playbook
- **Cita completa**: [`MCKINSEY_SKILLS_REFERENCE.md`](MCKINSEY_SKILLS_REFERENCE.md)

#### 🎯 **Mirza Iqbal ([next8n.com](https://next8n.com)) — Workflow Delivery Framework** (MIT)

- **Qué es**: la **SOP operacional** para consultoría de delivery n8n — ciclo de vida completo Discovery → Sprint → Handover, grillas de precios, plantillas de comunicación con cliente
- **Por qué lo apreciamos**: uno de los pocos en open-sourcing la **SOP operacional del trabajo de delivery** (no solo la SOP técnica) — llena el lado operacional del que la industria de consultoría raramente habla
- **Dónde lo usamos**: [`../06_Delivery/`](../06_Delivery/) — Engagement Lifecycle, Role SOPs, Business Document Templates están todos inspirados en él
- **Cita completa**: [`WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)
- **Obtenido vía**: <https://github.com/MorrisLu-Taipei/AI-Workflow-Delivery-Framework> (el README lista a Mirza Iqbal como autor original)

### 2.3 Agent & Skill (influye en 02_Course_Design)

#### 🎯 [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) (MIT)

- **Qué es**: biblioteca de personas de Agent para 12 divisiones (Marketing, Sales, Customer Service, HR, Finance, R&D, etc.) — listo para usar
- **Por qué lo apreciamos**: hace del "diseño de persona de Agent" una biblioteca reutilizable, ahorrando a los equipos escribir system prompts desde cero
- **Dónde lo usamos**: [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6 módulo "usar bibliotecas de agentes existentes"
- **Cita completa**: [`AGENCY_AGENTS_REFERENCE.md`](AGENCY_AGENTS_REFERENCE.md)

#### 🎯 [`MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack) (licencia mixta)

- **Qué es**: estructura n8n Skill de tres capas (Workflow Library + Cookbook + DSL Spec), con AI-generated Workflow Skill Pack
- **Por qué está aquí**: este es el proyecto propio del autor de la metodología Morris Lu, pero listado aquí para **demostrar la disciplina de citación** — incluso para sus propios proyectos, la licencia y las fuentes de terceros (`_vendor/` MIT) están documentadas con el mismo estándar
- **Dónde lo usamos**: [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) segunda mitad
- **Cita completa**: [`N8N_SKILL_PACK_REFERENCE.md`](N8N_SKILL_PACK_REFERENCE.md)

### 2.4 Índice de casos (influye en 04_Scenarios)

#### 🎯 [`Shubhamsaboo/awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps) (Apache-2.0)

- **Qué es**: lista curada de 150+ casos reales de aplicaciones LLM (Agent / RAG / Fine-Tuning / Multimodal, etc.), mantenida por la comunidad
- **Por qué lo apreciamos**: alta calidad de curación, taxonomía clara, actualización continua; la referencia más rápida cuando un consultor le dice al cliente "**así lo hacen otros con este escenario**"
- **Dónde lo usamos**: [`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index — mapeado al índice dual-axis (L1-L5 × departamento empresarial); **el mapping es nuestro**, la lista original es copyright de Shubham Saboo y los contribuyentes de la comunidad
- **Cita completa**: [`AWESOME_LLM_APPS_REFERENCE.md`](AWESOME_LLM_APPS_REFERENCE.md)

#### 🎯 [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) (MIT)

- **Qué es**: 93+ proyectos pedagógicos de AI Engineering (implementaciones ejecutables, desde RAG hasta Multi-Agent)
- **Por qué lo apreciamos**: cada proyecto viene con **código + video pedagógico**, los aprendices pueden arrancar directo; complementa los "casos curados" de awesome-llm-apps con el lado de "implementación hands-on"
- **Dónde lo usamos**: [`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index segunda fuente — mapeado a demos ejecutables de cursos L2-L4
- **Cita completa**: [`AI_ENGINEERING_HUB_REFERENCE.md`](AI_ENGINEERING_HUB_REFERENCE.md)

---

## 3. Material de referencia original y diagramas (caseros o de dominio público)

| Archivo | Propósito |
| --- | --- |
| [`@AI-MD-PUBIC.pdf`](@AI-MD-PUBIC.pdf) | Manual versión pública del AI Transformation Maturity Model (el PDF original del borrador metodológico) |
| [`MD-Map.png`](MD-Map.png) | AI Maturity Map, usado en el README raíz |
| [`Metholodgy.png`](Metholodgy.png) | Enterprise Consulting Eight-Stage Transformation Guide, usado en el README raíz |

## 4. Fundamento académico y failure patterns (totalmente originales, escritos por Tiger AI + los tres AI engines)

| Archivo | Propósito |
| --- | --- |
| [`FAILURE_PATTERNS.md`](FAILURE_PATTERNS.md) | 14 failure patterns (predicciones teóricas + casos reales + correctivos correspondientes) |
| [`AI_GOVERNANCE_ALIGNMENT.md`](AI_GOVERNANCE_ALIGNMENT.md) | Alineamiento con NIST AI RMF / EU AI Act / ISO 42001 |
| [`PILOT_STUDY_PROTOCOL.md`](PILOT_STUDY_PROTOCOL.md) | Diseño de investigación empírica de 18-24 meses (Pilot Study) |

La teoría académica en sí (los 7 pilares) está en [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md).

## 5. Notas de aprendizaje en video (notas derivadas; copyright del video original a los creadores)

| Archivo | Propósito |
| --- | --- |
| [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md) | Notas de la playlist pública OpenWebUI, mapeadas al uso del curso L1 |
| [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md) | Notas del canal TigerAI, enfocadas en n8n / uso del curso L3 |

---

## 6. Disciplina de citación (las reglas de hierro para futuros contribuyentes)

Para citar cualquier material de terceros en este repo, **todos siguen estos principios "Approach A"**:

| # | Principio | Cómo |
|---|---|---|
| 1 | **Adaptar independientemente — no forkear, no reproducir código fuente** | Referenciar estructura y conceptos, luego reescribir en la voz de esta metodología |
| 2 | **Atribución explícita, doble anotación** | (a) nota de header en el archivo que cita; (b) `*_REFERENCE.md` standalone en este directorio |
| 3 | **Generalizar al escenario metodológico** | Convertir contenido específico de dominio al contexto de consultoría de transformación IA L1-L5 |
| 4 | **Sin licencia = sin integración** | Proyectos de terceros sin LICENSE no se integran (solo citados como URL de ejemplo externo) |
| 5 | **Reconocimiento generoso** | En el archivo de citación, **decir explícitamente qué es bueno**, no solo "ver fuente abajo" |
| 6 | **Honesto sobre los fallos** | Si una herramienta citada resulta inadecuada, escribirlo honestamente en `FAILURE_PATTERNS.md` — no solo success stories |

**Lógica de uso**: para encontrar "qué fue citado por el archivo X en el directorio Y" → leer el header de ese archivo → saltar al `*_REFERENCE.md` correspondiente en este directorio para la nota de licencia completa.

---

## 7. Mapping inter-directorios

| Directorio | Relación con este directorio |
| --- | --- |
| [`../00_Overview/`](../00_Overview/) | Los diagramas metodológicos (Metholodgy.png / MD-Map.png) vienen de aquí; la discusión de los 7 pilares teóricos vive en `00` |
| [`../02_Course_Design/`](../02_Course_Design/) | Citas de terceros para cursos L1/L2/L3/L5 (notas OpenWebUI, agency-agents, n8n-Skill-Pack, ClawTeam) |
| [`../03_Consulting_Report/`](../03_Consulting_Report/) | Citas de terceros para la biblioteca de frameworks y el workflow de reporte (consultant, mckinsey-skills) |
| [`../04_Scenarios/`](../04_Scenarios/) | Citas de terceros para el índice de casos de aplicación LLM (awesome-llm-apps, ai-engineering-hub) |
| [`../06_Delivery/`](../06_Delivery/) | Cita de terceros para la capa de operaciones de delivery (framework de Mirza Iqbal) |
| [`../07_AI_Contributions/`](../07_AI_Contributions/) | Los tres AI engines mismos también son "sujetos de reconocimiento" — Antigravity / Codex CLI / Claude Code |

---

## 8. Escenarios de uso comunes

- **Preguntarse por qué un archivo está escrito de cierta manera**: leer el header del archivo → mapear al `*_REFERENCE.md` en este directorio
- **Redistribuir / comercializar esta metodología**: leer §6 Disciplina de citación + requisitos de atribución en [`NOTICE`](../NOTICE)
- **Onboardear un nuevo proyecto open-source** → seguir los 6 principios de §6: confirmar licencia → adaptar independientemente → crear `*_REFERENCE.md` → agregar a §2 Reconocimientos de este README
- **Engagar a las comunidades upstream, interactuar / reconocer**: hacer clic en la URL de GitHub de cada tarjeta de agradecimiento para star, follow, abrir issue, enviar PR
- **Aprendices citando contenido del repo en sus propios papers / decks**: según §6, al citar esta metodología mantener la atribución del autor original ([`../NOTICE`](../NOTICE)); al citar material de terceros seguir el formato de citación de aprendiz en el `*_REFERENCE.md` correspondiente

---

## 9. Reconocimientos

Todos los autores y comunidades upstream listados en este directorio **son los hombros sobre los que esta metodología se apoya**. Cualquier mala interpretación, cita inapropiada o desviación del objetivo original es responsabilidad exclusiva del autor de la metodología **Tiger AI Morris Lu 盧業興** — no de los autores o comunidades upstream.

Si usted es un autor upstream y siente que una cita en este repo es inapropiada, debe ser corregida o reforzada — por favor abra un issue o contacte a Morris Lu, lo manejaremos de inmediato.

> **Propiedad de la arquitectura**: la arquitectura metodológica de este repo es propuesta por el autor humano **Morris Lu (Tiger AI)**. Los tres AI engines (Antigravity / Codex / Claude Code) son herramientas que **ejecutan, completan, extienden y auditan**. Ver [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0.
