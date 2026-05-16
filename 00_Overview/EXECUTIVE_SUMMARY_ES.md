# Resumen Ejecutivo: Toda la Metodología en 5 Minutos (10 Minutos para la Vista Completa)

> 🌐 中文 / Chinese: [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) ｜ English: [EXECUTIVE_SUMMARY_EN.md](EXECUTIVE_SUMMARY_EN.md)
>
> **Versión 5 minutos**: lea §1 «En una página» + §2 «Modelo central» — es suficiente.
> **Versión 10 minutos**: añada §3-§7 (libro vivo, teoría, cursos, consultoría, entregables, co-lectura, próximos pasos).
> Haga clic en los archivos enlazados solo cuando quiera profundizar.

---

## 1. En Una Página: Lo que Resuelve

Muchas empresas adoptan IA «**saltando directamente a las herramientas**» — comprar ChatGPT, probar n8n, querer construir Agents. El resultado: los empleados no saben usarla, los procesos no están conectados, los datos no están gobernados, los PoC no pueden aceptarse, y la dirección no tiene idea de qué nivel de madurez está realmente la IA de la empresa.

Esta metodología convierte el «**uso disperso de IA**» en una «**capacidad organizacional reproducible, gobernable, medible y escalable**» — usando un bucle cerrado de **cuestionario + cursos + consultoría** para llevar a una empresa desde **individuos que usan IA** hasta **la empresa que posee un equipo IA**.

| Elemento | En una frase |
|---|---|
| **Herramienta de diagnóstico** | Cuestionario de 10 / 25 / 50 ítems → posición L1-L5 objetiva + brechas en seis dimensiones |
| **Ruta de educación** | Cursos en 5 niveles (OpenWebUI / Antigravity / n8n / Hermes / ClawTeam) + calibrado BARS |
| **Estructura de consultoría** | 8 etapas (Awareness → Acceptance Test) + contrato en 3 fases (A Diagnóstico / B Estrategia / C Implementación) |
| **Fundamento académico** | 7 pilares teóricos (Rosemann / Cohen & Levinthal / Teece / Real Options / etc.) |
| **Medio portador** | **AI-Native Living Book** — una metodología realmente *viva*, co-legible directamente con un AI IDE |

---

## 2. Modelo Central: Los Dos Ejes de L1-L5

L1-L5 no son «cinco herramientas» — es un camino de madurez conectado por **dos ejes**:

| Eje | Rango | Conductor | Capas | Herramientas |
|---|---|---|---|---|
| **Eje de escala** | L1 → L2 → L3 | **Humanos** usan IA, **humanos** supervisan IA | individuo → departamento → entre departamentos / toda la empresa | OpenWebUI / Antigravity / n8n |
| **Eje de autonomía IA** | L4 → L5 | **IA** funciona en autonomía; humanos retroceden a **gobernador** | entidad IA → equipo IA | Hermes Agent / ClawTeam |

**Frontera crítica = L3 → L4**: cruzar de «los humanos dirigen el trabajo» a «la IA dirige el trabajo». Incluso en L4-L5, **el marco de gobernanza sigue siendo construido por humanos, quienes conservan la supervisión** — lo que la IA hace en autonomía es «ejecución operativa», no «decisión de gobernanza».

➜ Historia completa: [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0

---

## 3. AI-Native Living Book — Por qué Este Libro está *Vivo*

Esta metodología no es un PDF / PPT / SOP — **es un libro realmente *vivo***:

| Generación | Forma | Limitación |
|---|---|---|
| Gen 1 — Libros impresos | Papel | **Estático** — solo puede leerse, no responde |
| Gen 2 — Libros interactivos | Web / Wiki | **Interfaz viva, contenido no** — sigue sin sugerir nada proactivamente |
| **Gen 3 — AI-Native Books** (este repo) | Markdown + AI IDE | **Realmente vivo** — le deja preguntar, le responde, piensa con usted, ejecuta diagnósticos / redacta informes / simula escenarios según la situación de su empresa |

**Modelo operativo**: `git clone` → abrir con un AI IDE (Antigravity / Claude Code / Codex) → la IA lee todo el libro automáticamente → se posiciona como **tutor de co-lectura** para esta metodología → usted conversa, pregunta y aplica directamente.

➜ Discusión completa: [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md)

### Tres Motores IA, Cada Uno Especializado Diferente

| Motor | Rol | En lo que es mejor | Workflows |
|---|---|---|---|
| 🟦 **Antigravity** | Consultor de primera línea | Dialogar con clientes, ejecutar cuestionarios, redactar informes | `/diagnose`, `/generate-report` |
| 🟪 **Codex CLI** | Auditor de la metodología | Pruebas entre archivos, red-team review, control de versiones, reparación | `/evidence-audit`, `/red-team-review`, `/bump-version` y 7 más |
| 🟨 **Claude Code** | Compañero de pensamiento entre archivos | Síntesis profunda, debate multi-perspectiva, simulación, forks de cliente | `/simulate-engagement`, `/devil-pair-debate`, `/methodology-fork` y 7 más |

➜ Autodescripción de los tres motores: [`../07_AI_Contributions/`](../07_AI_Contributions/) ｜ Guía de instalación: root [`../README_ES.md`](../README_ES.md) §🚀

---

## 4. Fundamento Académico: 7 Pilares Teóricos

Esta metodología no es ad-hoc. Cada diseño clave **remite a una teoría clásica** — la respuesta estándar cuando académicos, reguladores o consejos preguntan «¿cuál es la base teórica?»:

| # | Teoría | Fundador | Rol en esta metodología |
|---|---|---|---|
| 1 | **Capability Maturity** | Rosemann (QUT) / CMMI | El fundamento escolar para la madurez L1-L5 |
| 2 | **Absorptive Capacity** | Cohen & Levinthal (1990) | Explica por qué algunas empresas se atascan en L1 — les falta conocimiento previo |
| 3 | **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | Diseño To-Be Etapa 7: qué tareas deben llegar a L4, cuáles deben quedarse en L2 |
| 4 | **Dynamic Capabilities** | Teece (1997, 2007) | sense / seize / transform — por qué la gobernanza IA es una «capacidad», no una «policy» |
| 5 | **Sociotechnical Systems & Trust in AI** | Bostrom (1977) / Dietvorst (2015) / Glikson (2020) | Por qué L4-L5 deben mantener HITL — los humanos no confían ciegamente en IA pura |
| 6 | **Real Options Theory** | Dixit & Pindyck (1994) / McGrath (1997) | Por qué Phase 1 con NPV ≈ 0 vale la pena invertir — compra la opción de expandir |
| 7 | **Executable Knowledge Artifact** | Knuth (1984) Literate Programming + extensiones modernas | Por qué esta metodología es Markdown + co-lectura AI IDE en vez de PDF |

➜ Discusión teórica completa (con citas): [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md)
➜ Patrones de fallo (donde la teoría predice fallo): [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md)
➜ Diseño de Pilot Study (estudio empírico 18-24 meses): [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md)

---

## 5. Educación: El Currículum L1-L5 Completo

Cada nivel tiene su **propio material de curso + entregables verificables + aceptación Stage Gate**:

| Nivel | Nombre | Herramienta | Plan de curso |
|---|---|---|---|
| L1 | Controlled AI Access | OpenWebUI | [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) |
| L3 | Workflow Automation | n8n + Tiger AI Skill Pack | [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) |
| L4 | Autonomous Agent | Hermes Agent + Wiki | [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) |
| L5 | Multi-Agent Organization | ClawTeam | (L5 incluido en [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)) |

**Principio de diseño**: los clientes no tienen que hacer todo L1-L5 de una vez. Use el cuestionario para encontrar **la capa que produce los entregables más inmediatos**, luego construya hacia arriba. El mix de cursos se determina por perfil de empresa, sector, modo de despliegue (cloud / híbrido / on-prem) y requisitos de riesgo.

➜ Paquete de cursos completo: [`../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
➜ Calibrado de scoring (evitar subjetividad): [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) BARS

---

## 6. Consultoría: 8 Etapas + Modelo de Contrato 3 Fases

### 6.1 Las Ocho Etapas

| # | Etapa | Acción principal |
|---|---|---|
| 1 | **Awareness** | Establecer conciencia IA y visión del cliente |
| 2 | **Reference Model** | Guiar al cliente a firmar el radar Ideal Practice |
| 3 | **Discovery** | Recoger estado As-Is, Shadow IT, inventario de sistemas |
| 4 | **Gap Analysis** | Comparar Ideal Practice vs As-Is; identificar brechas de alto impacto |
| 5 | **Stakeholder Mapping** | Identificar Sponsor, AI Champion, RR. HH., Compliance |
| 6 | **Diagnosis** | Análisis entre capas (incl. anclaje en los 7 pilares teóricos) |
| 7 | **To-Be Design** | Usar TTF / Real Options para diseñar una hoja de ruta por niveles |
| 8 | **Acceptance Test** | Sign-off Stage Gate + revisión trimestral del radar |

### 6.2 Contrato en Tres Fases

| Fase | Duración | Entregable principal |
|---|---|---|
| **Phase A — Diagnóstico** | 2 semanas | Informe de diagnóstico intermedio + Ideal Practice firmado |
| **Phase B — Estrategia** | 4 semanas | Informe de consultoría completo de 14 capítulos + Roadmap 24 meses + ROI + recomendaciones de gobernanza |
| **Phase C — Implementación** | 24 meses | Implementación por fases + revisión trimestral del radar + evolución continua |

➜ Historia completa de 8 etapas (con ejemplos de diálogo): [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md)
➜ Plantilla de informe de consultoría: [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)
➜ Plantillas de toolkit de consultoría: [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md)
➜ Paquete de entrega & aceptación: [`../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)

---

## 7. Entregables Verificables: Lo que Cada Nivel Deja

El «curso» de cada nivel no termina cuando acaba la conferencia — deja evidence auditable:

| Nivel | Entregables principales | Evidence |
|---|---|---|
| L1 | Área de chat personal, Prompt Library | Tabla de cuentas, tabla de permisos, logs de login, ejemplos de Prompt |
| L2 | Skill Library, artifacts Agentic | Documentos Skill, casos de prueba, historial de versiones, ejemplos de salida |
| L3 | n8n Workflow PoC, Sub-workflow Library, Data Tables | Execution logs, logs de retry, capturas de integración de sistemas |
| L4 | Agent verificable, briefings, task cards | Agent log, versiones Wiki, records de sign-off HITL |
| L5 | Fichas de rol Agent Team, flow de colaboración, resultados entre departamentos | Team run log, records de traspaso, records de gobernanza |
| **Nivel consultoría** | Informe de diagnóstico de 14 capítulos, Roadmap 30/60/90 días, ROI, recomendaciones de gobernanza | Records sign-off Stage Gate, revisión trimestral del radar |

➜ Entregables completos + matriz evidence: [`../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)

---

## 8. Cómo Usar Este Libro (5 Rutas de Entrada por Rol)

| Usted es | Empezar aquí (20 min → 1 hora) |
|---|---|
| **CEO / propietario / familiar que quiere captar la metodología** | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) — historia de Ming |
| **Consultor / aprendiz** | [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) — flow completo 8 etapas |
| **Consejo / regulador / académico** | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — argumentación científica |
| **IT empresa / consultor de otra firma** | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — alineación con McKinsey/BCG/TOGAF/Gartner |
| **Investigador de metodología / académico AI Pedagogy** | [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) — por qué es una nueva forma de metodología |

---

## 9. Índice Rápido de Referencias

### 9.1 Teoría Académica & Modos de Fallo

- [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — discusión completa de los 7 pilares teóricos
- [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) — 14 modos de fallo (predichos por la teoría)
- [`../90_References/AI_GOVERNANCE_ALIGNMENT.md`](../90_References/AI_GOVERNANCE_ALIGNMENT.md) — alineación con NIST AI RMF / EU AI Act / ISO 42001
- [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) — diseño de estudio empírico 18-24 meses

### 9.2 Educación & Evaluación

- [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) — cuestionario 10/25/50 ítems (plain-language)
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL.md) — modelo de scoring
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) — calibrado BARS (evitar subjetividad)
- [`../02_Course_Design/`](../02_Course_Design/) — planes de cursos L1-L5 completos

### 9.3 Entrega de Consultoría

- [`../03_Consulting_Report/`](../03_Consulting_Report/) — informe de consultoría + plantillas de toolkit
- [`../04_Scenarios/`](../04_Scenarios/) — 7 escenarios sectoriales (fabricación / hospital / marketing / B2B / financiero / gobierno / educación)
- [`../05_Sales/`](../05_Sales/) — argumentario de ventas + FAQ
- [`../06_Delivery/`](../06_Delivery/) — paquete de entrega + criterios de aceptación + Engagement Lifecycle

### 9.4 Autodivulgación de los Tres Motores

- [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) — README co-editado por los tres motores + §3 disciplina de co-redacción
- [`../07_AI_Contributions/ANTIGRAVITY.md`](../07_AI_Contributions/ANTIGRAVITY.md) ｜ [`CODEX.md`](../07_AI_Contributions/CODEX.md) ｜ [`CLAUDE_CODE.md`](../07_AI_Contributions/CLAUDE_CODE.md)
- [`../CHANGELOG.md`](../CHANGELOG.md) — changelog co-editado por los tres motores

### 9.5 Material Fuente

- [`../90_References/@AI-MD-PUBIC.pdf`](../90_References/@AI-MD-PUBIC.pdf) — PDF original de la metodología
- [`../90_References/MD-Map.png`](../90_References/MD-Map.png) — AI Maturity Map
- [`../90_References/Metholodgy.png`](../90_References/Metholodgy.png) — diagrama Eight-Stage Transformation Guide
- [`../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) — notas de aprendizaje en vídeo
- [`../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

---

## 10. Próximos Pasos: 3 Rutas Sugeridas

| Su necesidad | Próximo paso recomendado |
|---|---|
| **Construir el modelo mental global** | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) (incl. §3.0, la historia completa de los dos ejes) |
| **Descubrir en qué nivel está su empresa** | El diagnóstico rápido de 10 ítems en [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) |
| **Leer este libro directamente con IA** | Abrir este repo con un AI IDE → leer primero root [`../README_ES.md`](../README_ES.md) §🚀 Guía de instalación de los tres motores y elegir un motor para iniciar |

---

> ⚠️ **Declaración de integridad académica**: Todos los casos nombrados en este repo (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 archivos SAMPLE_CLIENT_CASE) y todos los personajes principales (p. ej., «Ming» y «MingChang Packaging») son **ejemplos ficticios generados por IA**, NO datos de clientes reales. Todas las cifras (tiempo, ROI, person-month, presupuesto, KPI) son **solo ilustrativas** y **NO deben usarse para marketing externo, compromisos contractuales o evidencia empírica académica**. Los casos longitudinales reales reemplazarán estos solo tras el estudio empírico de 18-24 meses descrito en [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md).
>
> **Propiedad de la arquitectura**: La arquitectura de la metodología en este repo está diseñada por el autor humano **Morris Lu (Tiger AI)**. Los tres motores IA (Antigravity / Codex / Claude Code) son herramientas que **ejecutan, completan, expanden y auditan**. Véase [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0.
