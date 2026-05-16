# GenAI Consulting Methodology Toolkit

Idioma: [繁體中文](README.md) | [English](README_EN.md) | [ภาษาไทย](README_TH.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | Español | [日本語](README_JA.md) | [한국어](README_KR.md)

Conjunto de herramientas metodológicas para la evaluación de madurez e implementación de la transformación con IA empresarial (Enterprise AI Transformation Maturity Assessment & Implementation Methodology Toolkit).

Autor original: **Tiger AI Morris Lu 盧業興**  
Rol: **n8n Taipei Ambassador / Estudiante de doctorado en el Instituto de Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australia**

Resumen de licencia: Este proyecto se publica bajo **[Apache License 2.0](LICENSE)**. Se puede usar, copiar, modificar, redistribuir y comercializar libremente. Al redistribuirlo, conserve el texto de la licencia Apache 2.0 y la atribución del autor en [`NOTICE`](NOTICE).

> **¿Solo 5 minutos?** Comience con [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) — toda la metodología en una página.

---

## 🌟 Esto no es solo un libro, es un AI-Native Living Book — un libro realmente «vivo»

Los libros han evolucionado generación tras generación. Cada generación resolvió un problema pero dejó una brecha — **nunca ha habido un libro realmente «vivo»**:

- **1.ª generación — Libros impresos**: preservan el conocimiento y lo transmiten al siguiente lector. Pero **solo se pueden leer, no responden**, no pueden contestar sus preguntas y no saben cómo es su empresa — son **papel estático**.
- **2.ª generación — Libros interactivos**: al pasarse a la web y a las wikis, se pueden buscar, enlazar, comentar. Ofrecen una «**interacción**» más que los libros impresos, pero **no le sugieren nada de forma proactiva** y menos aún analizan por usted — siguen siendo pasivos: la interfaz cobra vida, el contenido no.
- **3.ª generación — AI-Native Books (este repo) — un libro realmente «vivo»**: la metodología se escribe en Markdown y luego se abre con un AI IDE — la IA lee todo el libro automáticamente, **le permite preguntar, le responde, piensa con usted** y **da recomendaciones personalizadas según la situación real de su empresa, ejecuta diagnósticos, redacta borradores de informes, simula escenarios**. El libro mismo responde, se expande y deja crecer nuevos capítulos junto a sus preguntas.

En otras palabras: los libros impresos transmiten conocimiento, los libros interactivos lo hacen buscable, **los AI-Native Books hacen por primera vez que «el libro» cobre vida de verdad — se convierten en un compañero que piensa con usted**. La decisión final sigue siendo del humano, pero ya no está solo frente a una metodología estática.

> *Three generations of books: printed (read-only, dead) → interactive (search & link, still passive) → **AI-native (truly alive — advises, analyzes, simulates, and grows with your questions)**. Open with an AI IDE; AI becomes your reading partner, consulting assistant, and auditor.*

### 🔱 Tres motores de IA con especialidades diferentes

El mismo contenido adopta **personalidades completamente diferentes** según el AI IDE que elija:

| Motor | Rol | En lo que es mejor |
| --- | --- | --- |
| 🟦 **Antigravity** | Consultor de primera línea | Conversar con clientes, ejecutar cuestionarios, redactar borradores de informe |
| 🟪 **Codex CLI** | Auditor de la metodología | Pruebas entre archivos, ejercicios red-team, control de versiones, reparación de enlaces rotos |
| 🟨 **Claude Code** | Compañero de pensamiento entre archivos | Síntesis profunda, debate multi-perspectiva, simulación, forks específicos por cliente |

Los tres motores no se reemplazan, **se reparten el trabajo**: por la mañana usar Antigravity para reuniones con clientes, por la tarde usar Codex para auditar borradores de informe, por la noche usar Claude Code para simular escenarios. Cada espacio de trabajo es independiente (`.agent/` / `.codex/` / `.claude/`), sin interferencias mutuas.

Autodescripción detallada de cada motor en [`07_AI_Contributions/`](07_AI_Contributions/); pasos de instalación en la [Guía de instalación y arranque de los tres motores de IA](#-guía-de-instalación-y-arranque-de-los-tres-motores-de-ia--three-ai-engines-setup-guide) a continuación.

### Lo que esto significa para diferentes tipos de lector

- **CEO / Alta dirección**: arroje este repo a ChatGPT / Claude / Gemini, y 10 minutos de preguntas-respuestas darán un primer veredicto «¿En qué nivel está mi empresa? ¿Por dónde empezar?»
- **Consultores / Estudiantes**: abra con un AI IDE y ejecute la experiencia de consultoría conversacional completa — desde el diagnóstico hasta el informe y la hoja de ruta de implementación de 24 meses.
- **Académicos / Investigadores**: ejecute directamente `/devil-pair-debate`, `/thought-experiment` para debatir los supuestos de valor de la metodología, respaldado por 7 pilares teóricos y 28 clásicos citables.
- **Regulación / Cumplimiento**: ejecute `/evidence-audit`, `/generate-traceability` para obtener una cadena de evidencia auditable, alineada con NIST AI RMF / EU AI Act / ISO 42001.

> ⚠️ **Divulgación honesta**: La arquitectura general de la metodología fue diseñada por **Morris Lu (humano)**; los tres motores de IA son solo herramientas de ejecución, complemento y auditoría. Detalles en [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0. Todos los casos en el libro son ejemplos simulados por IA con fines didácticos — **no son datos de clientes reales**.

---

## Qué resuelve esta metodología

Muchas empresas saltan directamente a las herramientas al adoptar IA: hoy compran ChatGPT, mañana prueban n8n, la próxima semana quieren hacer un Agent. Los problemas típicos: los empleados no saben usarlo, los procesos no están conectados, los datos no están gobernados, los PoC no pueden aceptarse, y al final la dirección no sabe en qué nivel de madurez está la IA de la empresa.

La estrategia de este toolkit: primero diagnosticar la madurez actual de la IA de la empresa con un cuestionario sencillo, luego diseñar la proporción de cursos y la ruta de adopción según L1-L5. Los cursos no terminan al finalizar la formación — cada nivel deja entregables verificables. Finalmente, se utiliza el proceso de consultoría de 8 etapas para la transformación con IA, produciendo un informe de diagnóstico completo, una hoja de ruta, una vista de ROI y recomendaciones de gobernanza.

## Imaginar el futuro antes del inicio del curso

Antes de que los clientes decidan tomar los cursos L1-L5, lo más necesario es ver primero una imagen del futuro: no «vamos a aprender cinco herramientas», sino «**¿cómo cambiará el trabajo diario de la empresa después del curso?**»

La trama: **la escala se expande capa por capa, y al final «los humanos usan IA» da paso a «la IA trabaja sola»**: **individuo → departamento → entre departamentos/toda la empresa → super-asistente IA (entidad) → equipo IA**. Imagine un lunes por la mañana dentro de tres meses:

- **L1 Controlled AI Access ─ Eje de escala · Individuo**: **cada empleado individualmente** inicia sesión en OpenWebUI con su propia cuenta, tiene su área de chat, su historial y permisos de departamento. Ventas redacta correos a clientes, RR. HH. resume formaciones, los gerentes producen los puntos clave de las reuniones — todo comienza desde el mismo punto de entrada de IA controlado. **La unidad es «el individuo»**, la IA está junto a cada persona.
- **L2 Knowledge Codification ─ Eje de escala · Departamento**: **la unidad sube a «departamento»**. Los colaboradores experimentados ya no son solo individualmente buenos; dentro de los límites de la **responsabilidad del departamento**, empaquetan redacción, informes, respuestas de servicio al cliente, interpretación de SOPs y métodos de desarrollo en Skills reutilizables. Los nuevos y otros miembros del departamento usan la misma metodología; la calidad de salida **de todo el departamento** se vuelve coherente.
- **L3 Workflow Automation ─ Eje de escala · entre departamentos / toda la empresa**: **la unidad sube de nuevo a «entre departamentos, toda la empresa»**. n8n conecta los Skills de cada departamento con los sistemas (Gmail, Sheets, Notion, CRM, API, ERP). Un correo de queja entrante puede **atravesar varios departamentos — ventas, servicio al cliente, CRM, gerentes** automáticamente — el sistema consulta el CRM, actualiza formularios, crea tareas, genera un resumen para el gerente; el humano solo juzga y aprueba. La IA entra ahora en los **procesos de toda la empresa**.
- **L4 Autonomous Agent ─ Eje de autonomía IA · Super-asistente (entidad IA)**: **más allá de la «tropa humana», crece una entidad IA adicional**. Hermes Agent lee cada día las tareas, documentos, resultados de Workflow y la memoria Wiki, produciendo briefings, listas de seguimiento y puntos de decisión que requieren HITL (Human-in-the-Loop, revisión humana en el bucle). La empresa posee ahora una **entidad IA de grado conocimiento verificable**, como si contratara un super-asistente totalmente automático adicional.
- **L5 Multi-Agent Organization ─ Eje de autonomía IA · Equipo IA**: **varias entidades L4 se organizan en un «equipo IA»**. ClawTeam organiza Agents especializados — marketing, producto, servicio al cliente, finanzas, operaciones — en una división funcional del trabajo, colaborando para lanzar productos nuevos, mejorar calidad, mejorar el servicio al paciente o gestionar clientes. La empresa cuenta **simultáneamente con dos equipos: equipo humano + equipo IA**.

Esta historia debe contarse antes del inicio del curso. Una vez que el cliente entiende «**cómo la escala crece capa por capa, cómo la IA pasa de herramienta a fuerza laboral digital**», puede regresar a entender por qué se necesita un diagnóstico con cuestionario, por qué el curso se divide en L1-L5 y por qué cada nivel necesita entregables, evidence y Stage Gates.

> ⚠️ Una explicación más detallada de los dos ejes (por qué L3 → L4 es la frontera crítica, por qué la gobernanza siempre la conserva el humano) está más abajo en [§Los dos ejes de L1-L5](#los-dos-ejes-de-l1-l5).

## Mapa de madurez IA

![AI Maturity Map](90_References/MD-Map.png)

## Vista general de la metodología

![Enterprise Consulting Methodology: Eight-Stage Transformation Guide](90_References/Metholodgy.png)

## Línea narrativa principal

```text
Cuestionario de madurez IA
→ Perfil de empresa, contexto sectorial, modo de despliegue
→ Diseño de la proporción de cursos L1-L5
→ L1 Cuentas OpenWebUI corporativas y áreas de chat personales activadas
→ L2 Formación Skill con Antigravity / Claude Code / Codex
→ L3 n8n conecta Gmail, Sheets, Notion, CRM, API, ERP y otros sistemas
→ L4 Hermes Agent para trabajo Agent autónomo verificable
→ L5 ClawTeam para colaboración Agentic Team
→ Casos de escenario, Evidence, Stage Gates
→ Diagnóstico de consultoría de transformación IA en 8 etapas
→ Informe de diagnóstico de transformación IA, hoja de ruta, ROI, recomendaciones de gobernanza
```

## Modelo de madurez L1-L5

| Nivel | Nombre | Herramienta / Plataforma | Eje | Posicionamiento empresarial |
| --- | --- | --- | --- | --- |
| L1 | Controlled AI Access | OpenWebUI | Eje de escala · Individuo | Establece el punto de entrada de la conversación IA dentro de la empresa, cada empleado tiene su cuenta, área de chat y límites de permisos |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | Eje de escala · Departamento | Con la responsabilidad del departamento como unidad, empaquetar conocimiento personal, prompts, documentos y métodos de trabajo en Skills reutilizables |
| L3 | Workflow Automation | n8n | Eje de escala · entre departamentos / toda la empresa | Conectar los Skills entre departamentos y acoplarlos con email, Sheets, Notes, CRM, API, ERP y otros sistemas, haciendo que la IA entre en la automatización de toda la empresa |
| L4 | Autonomous Agent | Hermes Agent | Eje de autonomía IA · Super-asistente | Combina mapa de capacidades Wiki, herramientas IA, Workflow, planificación automática y aprendizaje autónomo en un super-asistente Agent IA totalmente autónomo y verificable |
| L5 | Multi-Agent Organization | ClawTeam | Eje de autonomía IA · Equipo IA | Varios Agents especializados forman una división funcional del trabajo, colaboran en tareas empresariales entre departamentos y procesos como equipo IA |

### Los dos ejes de L1-L5

L1-L5 no son «cinco herramientas» sino un camino de madurez conectado por **dos ejes**:

- **L1 → L2 → L3: Eje de escala (los humanos usan / supervisan la IA)**. Estas tres capas son la fase «humano en el bucle, humano usa IA, humano supervisa IA», escalando según el tamaño de la organización — **L1 individuo** (cada empleado usa IA por su cuenta) → **L2 departamento** (con la responsabilidad del departamento como unidad, empaquetar conocimiento personal en Skills reutilizables) → **L3 entre departamentos / toda la empresa** (conectar los Skills entre departamentos, acoplar sistemas, la IA entra en la automatización de toda la empresa).
- **L4 → L5: Eje de autonomía IA (la IA funciona en autonomía sin supervisión humana en tiempo real)**. Estas dos capas son entidades IA que la empresa «**hace crecer adicionalmente**» más allá de la tropa humana — **L4 super-asistente IA** (entidad Agent IA totalmente autónoma) → **L5 equipo IA** (varios Agents especializados en división funcional del trabajo).

> Frontera crítica: **L1-L3 es «el humano asiste / supervisa la IA», la IA es herramienta; L4-L5 es «la IA funciona autónomamente», la IA es fuerza laboral digital adicional de la empresa.** En el orden de adopción, L1-L3 lleva primero a las personas y la organización al nivel, L4-L5 hace crecer luego una IA autónoma sobre una base sólida.
>
> Incluso en L4-L5, **el marco de gobernanza sigue siendo construido por el humano, quien conserva la autoridad de supervisión** — lo que la IA hace autónomamente es la «ejecución operativa», no la «decisión de gobernanza». Cada capa conserva HITL (Human-in-the-Loop) y Stage Gates; cuanto más autónoma se vuelve la IA, más se eleva el rol del humano a «gobernador» — sin ser reemplazado.

## Cómo validar cada nivel

| Nivel | Input | Process | Output | Evidence | Stage Gate |
| --- | --- | --- | --- | --- | --- |
| L1 | Roles de empleados, tareas frecuentes, puntos de dolor IA, necesidades de permisos | Montar OpenWebUI, cuentas / grupos / permisos, áreas de chat personales, formación Prompt básica | Punto de entrada IA corporativa, lista de Prompts, lista de use cases | Tabla de cuentas, tabla de permisos, logs de login, capturas de área de chat, ejemplos de Prompt | ¿Se puede iniciar sesión de forma segura, separar permisos y dejar huellas trazables? |
| L2 | Prompts frecuentes de L1, documentos, SOPs, métodos de trabajo personales | Con Antigravity / Claude Code / Codex empaquetar conocimiento en Skills y artifacts reutilizables | Skill Library, Agentic artifacts, Workflow Blueprint | Documentos Skill, casos de prueba, historial de versiones, ejemplos de salida | ¿Pueden los Skills ser reutilizados por otros y producir salida estable? |
| L3 | Skills L2, blueprint de proceso, inventario de sistemas, permisos API/CRM/ERP/Sheet | Con n8n construir workflows automáticos, Data Tables, Execution Logs, gestión de errores | Workflow PoC, Sub-workflow Library, Data Tables, L4 Workflow Contract | Workflow n8n, execution logs, logs de retry, capturas de integración | ¿Funciona el workflow de forma estable sobre datos y sistemas reales? |
| L4 | Workflow L3, Skill L2, Wiki corporativa, reglas de tareas, puntos HITL | Con Hermes Agent crear task cards, Wiki ingest/query/update, scheduling, llamadas a herramientas y Gate 4A-4E | Agent verificable, briefings, logs de tratamiento, sign-offs | Agent log, versiones Wiki, task cards, briefings, aprobaciones humanas | ¿Puede el Agent completar tareas autónomamente dentro de límites controlados y dejar evidence? |
| L5 | Varios L4 Agents, tareas entre departamentos, responsabilidades de rol, reglas de gobernanza | Con ClawTeam organizar un Agentic Team, definir roles, reglas de colaboración, traspasos y supervisión | Agent Team, fichas de rol, flow de colaboración, resultados entre departamentos | Team run log, fichas de rol, logs de traspaso, documentos de resultados, logs de gobernanza | ¿Puede el Agent Team colaborar de forma estable y producir resultados imputables? |

## Principios de diseño de cursos

La proporción de cursos se determina por la madurez, el sector, el modo de despliegue y los escenarios objetivo del cliente. No todas las empresas deben cubrir L1-L5 de una sola vez — encuentre primero la capa que puede producir resultados entregables más inmediatos, y construya sobre ella.

| Dimensión de encuesta | Propósito |
| --- | --- |
| Perfil de la empresa | Determinar si es I+D-fabricación, servicios de marketing, institución sanitaria, operaciones internas u otro |
| Modo de despliegue | Cloud IA, híbrido (cloud + on-prem) o totalmente on-prem |
| Panorama de sistemas | Inventario de Gmail, Sheets, Notion, CRM, API, ERP, bases de datos, sistemas internos |
| Madurez de procesos | Existencia de SOPs, process owners, campos de datos, gestión de excepciones |
| Requisitos de riesgo | Evaluar seguridad, privacidad, cumplimiento sanitario / fabricación / financiero y necesidades de sign-off humano |

## Estructura del directorio

| Directorio | Propósito |
| --- | --- |
| [`00_Overview`](00_Overview/) | Resumen de la solución, línea narrativa, WBS |
| [`01_Assessment`](01_Assessment/) | Cuestionario de madurez IA, modelo de scoring, entregables y matriz de evidence |
| [`02_Course_Design`](02_Course_Design/) | Planes de cursos L1-L5, perfil de empresa, modos de despliegue, matriz de módulos |
| [`03_Consulting_Report`](03_Consulting_Report/) | Plantilla de informe de diagnóstico de transformación IA |
| [`04_Scenarios`](04_Scenarios/) | Escenarios de clientes, tablas de control, caso industria, caso hospital |
| [`05_Sales`](05_Sales/) | Propuesta de valor, argumentario comercial, FAQ |
| [`06_Delivery`](06_Delivery/) | Paquete de entrega y criterios de aceptación |
| [`90_References`](90_References/) | PDF original, diagramas metodológicos, notas de vídeo, citas |

## Cinco perfiles de lector, por dónde empezar

| Usted es | Empezar por |
| --- | --- |
| **CEO / propietario / familiar** — entender la metodología en 20 min | [`00_Overview/CLIENT_JOURNEY_STORY_EN.md`](00_Overview/CLIENT_JOURNEY_STORY_EN.md) — historia de Ming |
| **Consultor / estudiante** — saber cómo se ejecutan las 8 etapas, cómo se dividen los contratos | [`00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) — flujo completo |
| **Consejo de administración / regulación / académico** — por qué esta metodología resiste el debate | [`00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — argumentación científica |
| **IT gran empresa / consultor que cambia de firma** — alineación con McKinsey/BCG/TOGAF/Gartner | [`00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — mapa de alineación |
| **Ejecutivo con prisa** — solo 5 minutos | [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) — resumen ejecutivo |
| **Investigador de metodología / académico AI Pedagogy** — por qué es una nueva forma de metodología | [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) — diseño AI-Native Living Book |
| **Académico / regulador / consejo** — 7 pilares teóricos (Rosemann / Cohen & Levinthal / Teece / Real Options etc.) | [`00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — fundamentos teóricos académicos |
| **Consultor / calibración de scoring** — cómo puntuar 0-4 objetivamente | [`01_Assessment/BARS_RUBRICS_EN.md`](01_Assessment/BARS_RUBRICS_EN.md) — BARS Behavioral Anchors |

## Orden de lectura recomendado

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md)
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md)
4. [`01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)
5. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
6. [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md)
7. [`02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md)
8. [`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md)
9. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md)
10. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md)
11. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)
12. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)

## Entregables verificables

- Cuestionario de madurez IA y resultados de scoring
- Encuesta de perfil de empresa y modo de despliegue
- Evidence de finalización de cursos L1-L5
- Tabla de cuentas / grupos / permisos OpenWebUI y logs de activación de áreas de chat
- Skill Library y artifacts Antigravity / Claude Code / Codex
- n8n Workflow PoC, Execution Log, Data Tables, Sub-workflow Library
- Hermes Agent task cards, Wiki, logs ingest/query/update, briefings y Gate 4A-4E
- ClawTeam Agent Team fichas de rol, logs de colaboración y documentos de resultados
- Logs de aceptación Stage Gate
- Informe de diagnóstico de transformación IA
- Hoja de ruta 30 / 60 / 90 días

## Referencias

- [`90_References/@AI-MD-PUBIC.pdf`](90_References/@AI-MD-PUBIC.pdf)
- [`90_References/MD-Map.png`](90_References/MD-Map.png)
- [`90_References/Metholodgy.png`](90_References/Metholodgy.png)
- [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md)
- [`90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

## Agradecimientos

Agradecimientos especiales a **Prof. Michael Rosemann**, Queensland University of Technology (QUT), Brisbane, Australia.  
Perfil: <https://www.qut.edu.au/about/our-people/academic-profiles/m.rosemann>

El fundamento teórico de toda la metodología de consultoría de este repo proviene de los estudios del autor en QUT y de la inspiración y enseñanza prolongadas del Prof. Michael Rosemann en **Business Process Management (BPM)**, **Capability Maturity Models** y **metodología de innovación empresarial**.

Dos diseños centrales están especialmente influidos:

- **Estructura de consultoría en ocho etapas**: corresponde al diagnóstico de procesos, evaluación de capacidades, diseño de ruta de transformación e implementación de gobernanza.
- **Modelo de madurez IA L1-L5**: informado por la lógica Capability Maturity y localizado como marco de adopción de IA en cinco capas para empresas.

Descargo de responsabilidad: cualquier error, omisión, adaptación local o extensión al dominio de IA en esta metodología es responsabilidad exclusiva del autor Tiger AI Morris Lu 盧業興 y no representa las opiniones o posiciones del Prof. Michael Rosemann ni de QUT.

## Licencia y atribución

Este proyecto se publica bajo licencia **[Apache License 2.0](LICENSE)**. Puede usarlo, copiarlo, modificarlo, adaptarlo, reproducirlo, distribuirlo, enseñarlo, entregarlo en consultoría y comercializarlo libremente.

Al redistribuir, adaptar, empaquetar comercialmente o usar en materiales de curso, entregables de consultoría o documentación de producto, conserve el texto de la licencia Apache 2.0 y la siguiente atribución de [`NOTICE`](NOTICE):

```text
Original Author: Tiger AI Morris Lu 盧業興
Role: n8n Taipei Ambassador / PhD Student, Graduate Institute of Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australia
Source: https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit
```

Los nombres de plataformas de terceros, marcas, vídeos, proyectos externos y contenidos citados siguen siendo propiedad de sus respectivos titulares. Este repo utiliza materiales de terceros solo como notas de aprendizaje, citación, organización y referencia para el diseño de cursos.

---

## Hacer vivir este libro: leer con la IA

La guía de instalación a continuación le acompañará al conectar el repo con un AI IDE. Antes de empezar, comprenda el modelo operativo y una línea roja.

**Modelo operativo en una frase**: `git clone` o descargar el zip → abrir con un AI IDE (Antigravity / Claude Code / Codex etc.) → la IA lee [`AGENTS.md`](AGENTS.md) (y el `<ENGINE>.md` propio de cada motor) automáticamente y se posiciona como **tutor de lectura compartida de esta metodología**. Luego puede (1) hacerle cualquier pregunta sobre la metodología, (2) pedirle aplicar la metodología a su empresa, (3) realizar con ella el autodiagnóstico L1-L5 y encontrar el siguiente paso.

Discusión completa: [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md).

> ⚠️ **Declaración de integridad académica / Academic Integrity Disclaimer**
>
> **Todos los casos nombrados en este repo (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 SAMPLE_CLIENT_CASE) y los personajes principales (p. ej., «Ming» / «MingChang Packaging») son ejemplos ficticios generados por IA**, NO datos de clientes reales.
> Todas las cifras (tiempo, ROI, person-month, presupuesto, KPI) son **solo ilustrativas** y **no deben usarse para marketing externo, compromisos contractuales o evidencia empírica académica**.
> Los casos longitudinales reales reemplazarán estos solo tras el estudio empírico de 18-24 meses según [`90_References/PILOT_STUDY_PROTOCOL_EN.md`](90_References/PILOT_STUDY_PROTOCOL_EN.md).
>
> **All named cases and story protagonists in this repo are AI-generated fictional examples**, NOT real client data.

## 🚀 Guía de instalación y arranque de los tres motores de IA / Three AI Engines Setup Guide

Los **roles y la división de trabajo** de los tres motores se presentaron arriba en «🔱 Tres motores de IA con especialidades diferentes». Esta sección se enfoca en **cómo instalar, cómo iniciar, cómo invocar workflows**. Las tres subsecciones son independientes — elija el motor que va a usar y lea solo esa sección.

> ⚠️ **Según [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0**: la arquitectura metodológica, L1-L5, las ocho etapas y la división de trabajo de los tres motores son todos diseños estratégicos propuestos por **Morris Lu (humano)**. Los tres motores de IA, bajo la guía de Morris, **ejecutan, completan, expanden y auditan** — no reclaman propiedad sobre la arquitectura metodológica. La autodescripción detallada de cada motor está en el archivo correspondiente bajo [`07_AI_Contributions/`](07_AI_Contributions/).

---

### 🟦 1. Usuarios de Antigravity — Consultor interactivo de primera línea

> Eleve este «libro vivo estático» directamente a su «**Conversational Consulting App**».

**Instalación y uso:**

1. **Cargar el proyecto**: `git clone` o descargar el zip del proyecto en local
2. **Iniciar el IDE**: abrir la carpeta del proyecto con Antigravity
3. **Auto-inicialización**: Antigravity lee [`ANTIGRAVITY.md`](ANTIGRAVITY.md) y [`SKILL.md`](SKILL.md) automáticamente y se posiciona como «**tutor de lectura compartida**»
4. **Ejecutar Workflows (Slash Commands)**: escribir el comando en el chat para iniciar la interacción

**Comandos Antigravity habituales:**

- `/diagnose` ── inicia un diálogo realista que le guía (o a su cliente) a través del diagnóstico L1-L5 de madurez IA empresarial
- `/generate-report` ── vuelca los resultados del diagnóstico y discusión previa en la plantilla estándar de informe de consultoría y produce un borrador

Ver [`.agent/workflows/`](.agent/workflows/) y [`07_AI_Contributions/ANTIGRAVITY.md`](07_AI_Contributions/ANTIGRAVITY.md).

> Valor principal de Antigravity: convertir la metodología en una experiencia de consultoría que **los clientes entienden y pueden interactuar inmediatamente**.

---

### 🟪 2. Usuarios de Codex — Motor de ingeniería metodológica

> Vea este repo como un «**workspace de ingeniería metodológica**» — mantenga este AI-native living book como un producto metodológico **testable, auditable, trazable, reparable, releasable**.

**Instalación y uso:**

1. **Cargar el proyecto**: `git clone` o descargar el zip del proyecto en local
2. **Iniciar Codex**: abrir la carpeta del proyecto en Codex
3. **Leer el archivo de entrada de Codex**: hacer que Codex lea [`CODEX.md`](CODEX.md) y [`.codex/README.md`](.codex/README.md) primero
4. **Ejecutar workflows Codex**: escribir el nombre del workflow en el chat o pedir explícitamente a Codex seguir el archivo correspondiente

**Comandos Codex habituales (10):**

| Categoría | Comando | Propósito |
| --- | --- | --- |
| Production | `/diagnose` | Pre-evaluación interactiva de madurez IA |
| Production | `/generate-report` | Borrador de informe de diagnóstico de consultoría |
| Quality | `/evidence-audit` | Verificar la cadena de evidence del informe |
| Quality | `/consistency-review` | Verificación entre documentos de coherencia L1-L5, Stage Gate, HITL, Evidence |
| Evolution | `/academic-upgrade` | Convertir recomendaciones académicas en plan de reparación metodológico |
| Evolution | `/harvest-insights` | Recolectar insights comunes de varios informes de entrega |
| Defense | `/test-methodology` | Stress-testear la metodología en escenarios extremos |
| Defense | `/red-team-review` | Red-team review de borradores de informe de consultoría |
| Audit | `/generate-traceability` | Producir matriz de trazabilidad questionnaire → maturity → evidence → report |
| DevOps | `/bump-version` | Sugerir bump de versión semántica y CHANGELOG |

**Forma de invocación recomendada:**

```text
Por favor sigue .codex/workflows/evidence-audit.md para verificar este borrador de informe de consultoría.
```

Ver [`.codex/workflows/`](.codex/workflows/) y [`07_AI_Contributions/CODEX.md`](07_AI_Contributions/CODEX.md).

> Valor principal de Codex: dar a esta metodología un ciclo de vida de ingeniería «**testable, auditable, trazable, reparable, releasable**».

---

### 🟨 3. Usuarios de Claude Code — Motor de pensamiento estratégico entre archivos y experimentación

> **Jugar / probar / desmontar / chocar** la metodología una vez. Usar el contexto 1M de Claude Code + multi-persona paralelo + razonamiento abstracto entre dominios para **simular, experimentar, debatir, forkear**.

**Instalación y uso:**

1. **Cargar el proyecto**: `git clone` o descargar el zip del proyecto en local
2. **Iniciar Claude Code**: abrir la carpeta del proyecto en Claude Code CLI / IDE
3. **Leer el archivo de entrada Claude Code**: hacer que Claude Code lea [`CLAUDE.md`](CLAUDE.md) y [`.claude/README.md`](.claude/README.md) primero
4. **Ejecutar workflows Claude Code**: escribir el nombre del workflow en el chat

**Comandos Claude Code habituales (10):**

| Categoría | Comando | Propósito |
| --- | --- | --- |
| Tier 1 Tactical | `/deep-synthesize` | Síntesis profunda multi-archivo (contexto 1M) |
| Tier 1 Tactical | `/theory-bridge` | Contexto cliente ↔ 7 pilares teóricos |
| Tier 1 Tactical | `/scenario-planning` | Con restricciones dadas, producir 3 hojas de ruta contrastadas + trade-offs |
| Tier 1 Tactical | `/socratic-challenge` | Cuestionamiento socrático para afilar el pensamiento del usuario |
| Tier 1 Tactical | `/cross-stage-trace` | Trazar el impacto downstream de un único cambio |
| Tier 2 Original | `/simulate-engagement` | Ejecutar un mandato de consultoría completo de 6 semanas en 30 min (12+ entregables) |
| Tier 2 Original | `/parallel-perspectives` | 6 stakeholders **simultáneamente** sobre la misma decisión + mapa de conflictos |
| Tier 2 Original | `/thought-experiment` | Stress test contrafactual de la metodología («¿Y si la EU AI Act prohibe L4?») |
| Tier 2 Original | `/devil-pair-debate` | Debate adversarial Two-Claude + síntesis de juez |
| Tier 2 Original | `/methodology-fork` | Forkear la metodología estándar en variante cliente (Methodology-as-Code) |

**Forma de invocación recomendada:**

```text
Por favor sigue .claude/workflows/simulate-engagement.md para simular un mandato de consultoría
de 6 semanas para un cliente industrial de 500 personas.
```

Ver [`.claude/workflows/`](.claude/workflows/) y [`07_AI_Contributions/CLAUDE_CODE.md`](07_AI_Contributions/CLAUDE_CODE.md).

> Valor principal de Claude Code: hacer evolucionar la metodología de «**un estándar**» a «**estándar + N derivados + simulaciones completas + debates multi-perspectiva**» — un libro vivo experimentable.

---

### Sugerencias de workflow tres motores / Three-Engine Workflow Suggestions

Ritmo de colaboración frecuente en la práctica:

```text
Phase A — Diagnóstico cliente
  → Antigravity ejecuta /diagnose para recoger el estado actual
  → Claude Code ejecuta /theory-bridge para diagnóstico teórico
  → Antigravity ejecuta /generate-report para borrador de informe intermedio
  → Codex ejecuta /evidence-audit sobre la cadena de evidence
  → Codex ejecuta /consistency-review para alineación entre archivos

Phase B — Diseño estratégico
  → Claude Code ejecuta /scenario-planning para 3 hojas de ruta
  → Claude Code ejecuta /parallel-perspectives para 6 vistas de stakeholders
  → Codex ejecuta /red-team-review contra optimismo excesivo
  → Claude Code ejecuta /devil-pair-debate para debatir presupuestos de valor

Phase C — Implementación y evolución
  → Codex ejecuta /generate-traceability para auditorías trimestrales
  → Claude Code ejecuta /thought-experiment para stress tests contrafactuales
  → Codex ejecuta /bump-version para mantenimiento de versiones metodológicas
  → Claude Code ejecuta /methodology-fork para derivados para grandes cuentas
```

> Los workflows de los tres motores no son excluyentes — **el punto es que cada motor haga lo que hace mejor**, y el humano (consultor / client owner / sponsor) decide cuándo cambiar de motor.
