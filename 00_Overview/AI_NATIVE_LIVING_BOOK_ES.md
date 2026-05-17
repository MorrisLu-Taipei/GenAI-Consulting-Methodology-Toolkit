# AI-Native Living Book: Metodología como Executable Knowledge Artifact

> 🌐 Idioma: [繁體中文](AI_NATIVE_LIVING_BOOK.md) ｜ [English](AI_NATIVE_LIVING_BOOK_EN.md) ｜ [Deutsch](AI_NATIVE_LIVING_BOOK_DE.md) ｜ [Français](AI_NATIVE_LIVING_BOOK_FR.md) ｜ Español ｜ [日本語](AI_NATIVE_LIVING_BOOK_JA.md) ｜ [한국어](AI_NATIVE_LIVING_BOOK_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Última actualización: 2026-05-16

---

> **Lo que esto responde**: La característica más distintiva de esta metodología no es su contenido — es su **medio portador**. Las metodologías de consultoría tradicionales son PDFs / PPTs / SOPs (documentos estáticos); este repo es un **sistema de conocimiento legible, explicable, consultable y aplicable por AI IDEs**. Los usuarios no "leen documentos" — **conversan con la metodología**. Este documento escribe formalmente esta característica en el posicionamiento de la metodología y aborda su clasificación académica + controles de riesgo.

---

## 1. Posicionamiento / Tagline de una frase

> Este repositorio no es solo un toolkit de metodología, sino un **AI-native living book**: cuando se abre en un AI IDE, sus instrucciones de agent embebidas ([`AGENTS.md`](../AGENTS.md) y [`CLAUDE.md`](../CLAUDE.md)) convierten la metodología estática en un **tutor de co-lectura interactivo y asistente de consultoría**.

---

## 2. Por qué esta es una nueva forma de metodología

### 2.1 Metodología tradicional vs. AI-Native Living Book

| Dimensión | Tradicional (PDF / PPT / SOP) | AI-Native Living Book (este repo) |
| --- | --- | --- |
| **Medio** | Documentos estáticos, slide decks, Word | Markdown + archivos de instrucción AI IDE (AGENTS.md / CLAUDE.md) |
| **Interacción usuario** | Lectura unidireccional | Conversación bidireccional (Q&R, aplicación, generación) |
| **Barrera de onboarding** | Alta (debe leer 100+ páginas) | Baja (AI auto-lee, se vuelve tutor de co-lectura) |
| **Cómo aplicar** | Consultor traduce para cliente | Cliente pide directamente a AI aplicar a su empresa |
| **Puede ser desafiado** | No (documentos no responden) | Sí (AI responde cualquier pregunta en tiempo-real) |
| **Puede ser reescrito** | Consultor debe editar | Cliente forkea + AI asiste con consistency checking |
| **Control de versión** | Usualmente ninguno | Historial Git completo (incluye cambios AGENTS.md) |
| **Citación académica** | Citar PDF | Citar hash de commit GitHub + entorno de ejecución reproducible |

### 2.2 Clasificaciones académicas

Esta metodología puede categorizarse como una (o más) de:

| Nombre | Propiedad enfatizada | Origen / Análogo |
| --- | --- | --- |
| **Executable Knowledge Artifact** | Conocimiento que puede ejecutarse; no solo descrito, sino aplicable | Jupyter Notebooks, computational essays |
| **AI-Mediated Methodology** | AI como intermediario entre usuario y metodología | Intelligent Tutoring Systems (ITS) |
| **Interactive Consulting Playbook** | Manual de operaciones de consultoría interactivo | Game playbooks, decision-tree wizards |
| **Living Book with Embedded Tutor Agent** | Living book + tutor agent embebido | Hypertext, knowledge graphs |

Tiger AI adopta **AI-native living book** como término primario porque **captura simultáneamente** "living book" (contenido evoluciona) + "AI-native" (diseñado para AI) + "co-reading tutor" (personalidad de tutor embebida).

---

## 3. Tres capas: Repo como Libro / Agent como Tutor / Metodología como Executable Artifact

### 3.1 Capa 1: Repo como Libro

La estructura del repo sigue convenciones de libro:

| Elemento de libro | Mapping repo |
| --- | --- |
| Portada / posición de una frase | Root [`README_EN.md`](../README_EN.md) + este doc §1 |
| Prefacio / executive summary | [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) |
| Capítulo de historia | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) historia de Ming |
| Metodología principal | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 |
| Capítulos de implementación | `01_Assessment` / `02_Course_Design` / `03_Consulting_Report` |
| Antología de casos | `04_Scenarios/` 7 casos Benchmark-grade |
| Soporte sales | `05_Sales/` |
| Delivery SOP | `06_Delivery/` |
| Argumento académico | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) |
| Mapa de alignment | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) |
| Failure modes (counter-cases) | [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) |
| Diseño de investigación | [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) |
| Referencias | Referencias de cada archivo + `90_References/` |

> **Punto clave**: Este "libro" es **completo** — clientes / consultores / académicos / regulatorios pueden cada uno encontrar su capítulo relevante.

### 3.2 Capa 2: Agent como Tutor (AGENTS.md es la "personalidad del tutor")

[`AGENTS.md`](../AGENTS.md) y [`CLAUDE.md`](../CLAUDE.md) no son notas suplementarias sino **embeben el rol, fronteras y guía de la AI en el repo**. Las AI IDEs (Claude Code / Cursor / Antigravity / Codex etc.) auto-leen estos archivos y se posicionan como **"tutores de co-lectura para esta metodología"**.

#### "Personalidad del tutor" definida en AGENTS.md

- **Rol**: AI = tutor de co-lectura + asistente consultoría, NO reemplazo de consultor
- **Scope de preguntas respondibles**: definiciones de metodología, mapping L1-L5, herramientas Stage, aplicación de caso, drafts de reporte
- **Scope de rechazo**: decisiones finales de cliente, eludir juicio de consultor, commitments ROI no verificados
- **Estilo de respuesta**: rigor académico + práctica consultoría + comprensible-cliente
- **Disciplina de citación**: cada conclusión etiquetada con nivel evidence [E:L#] (por Tool 8.9)
- **Lenguaje**: switching bilingüe EN/ZH por usuario

> Este diseño toma prestado de **LangChain Agent Prompt + Claude Skills**: archivos de configuración versión-controlados en el repo.

### 3.3 Capa 3: Metodología como Executable Artifact

Los usuarios pueden directamente pedir a AI **ejecutar la metodología**, no solo leerla:

#### Interacciones típicas

| Usuario pregunta | Tutor de co-lectura AI ejecuta |
| --- | --- |
| "Somos planta packaging 700 personal; ayúdame a correr el survey rápido 10-Q" | AI corre [`AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) versión 10-Q + auto-scores + produce radar |
| "Basado en mis respuestas, draftea esqueleto reporte mid-engagement Phase A" | AI genera draft por estructura [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) §3-§5 |
| "Somos manufactura; ¿qué caso es el más cercano a nosotros?" | AI compara con [`SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md) y calcula gap |
| "Prep materiales para el workshop Stage 3 Client Ideal Practice" | AI genera flow workshop + prompts sticky-note + impresión 4-capas por Tool 3.6 |
| "¿Cómo esto alinea con McKinsey 7-Step?" | AI mapea a [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) §2.1 |
| "¿Mi radar Stage 2 debería ser más redondo tras 24 meses?" | AI guía al usuario a través de review Quarterly Gate C |

> **Esto es el significado de "Metodología como Executable Artifact"** — la metodología no solo se describe; es aplicable en tiempo-real vía AI.

---

## 4. Bajando barreras de adopción de metodología

### 4.1 Las empresas temen 100+ archivos Markdown

Barreras de metodología tradicionales:

- 100+ páginas para leer ❌
- Demasiada terminología ❌
- No saben qué leer primero ❌
- Necesitan consultor para traducir ❌
- Deben escribir draft de reporte ellos mismos ❌

### 4.2 Tutor de co-lectura AI responde en tiempo-real

Una vez repo + AI IDE abierto, los usuarios preguntan directamente:

- "**¿Qué nivel es mi empresa?**" → AI corre survey 10-Q + auto-scores
- "**¿Qué archivo debo leer primero?**" → AI recomienda orden de lectura por rol (CEO / consultor / IT / académico)
- "**¿Cómo aplico esto a manufactura?**" → AI cita caso manufactura + flagga puntos de customización
- "**Por favor genera el primer draft del reporte diagnóstico**" → AI produce esqueleto Phase A 10-15 páginas
- "**¿Cuál es la frontera entre Stage 4 y Stage 8?**" → AI cita METHODOLOGY_SCIENTIFIC_LOGIC §4

> **Esto shifta la metodología de "solo-expertos legible" a "no-expertos pueden ser guiados a través."**

### 4.3 Reducción esperada en barrera de adopción

Hipótesis validadas por PILOT_STUDY_PROTOCOL:

- Metodología PDF tradicional: tasa de completion cliente < 15%
- **AI-native living book**: tasa de "conversación" cliente > 70% (AI guía proactivamente)
- Ciclo de adopción empresa mediana (100-500 personal): de "3-meses evaluación necesaria" → "Phase A dentro de 2 semanas"

---

## 5. Controles de riesgo

⚠️ Porque AI interpreta la metodología, **tutor de co-lectura AI NO debe** hacer lo siguiente:

### 5.1 Fronteras del tutor

| Puede | No puede |
| --- | --- |
| Explicar contenido de metodología | ❌ Reemplazar juicio formal de consultor |
| Correr surveys, auto-scorear, producir radares | ❌ Prometer números ROI específicos a clientes |
| Citar casos para calcular gaps | ❌ Firmar Ideal Practice Definition Table (requiere firma humana 3-partes) |
| Generar drafts de reporte | ❌ Reemplazar review final de client owner / consultor |
| Guiar self-assessment Stage Gate | ❌ Reemplazar audit de tercero |
| Aplicar 80/20 / 5 Whys / Issue Tree en tiempo-real | ❌ Reemplazar datos reales KPI longitudinales |

### 5.2 4 principios de control de riesgo

1. **Tutor de co-lectura AI ≠ consultor**: todos drafts de reporte requieren **review consultor humano o client owner** antes de uso externo
2. **Diagnósticos importantes requieren evidence**: por [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9, conclusiones mayores necesitan soporte L3+ (system log)
3. **Control de versión AGENTS.md**: evitar interpretación inconsistente entre AI IDEs — commit cada cambio AGENTS.md a Git y registrar en CHANGELOG
4. **Marcado AI-generated**: por Tool 8.8 §7, todo contenido AI-generated debe marcarse "AI-generated"

### 5.3 Escenarios de fallo

Si el tutor de co-lectura AI es mal usado (documentado en [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md)):

- AI erra y cliente lo toma al pie de la letra → reporte erróneo
- AI da números ROI no verificados → cliente firma SOW basado en falsa esperanza
- Diferentes AI IDEs interpretan AGENTS.md de manera diferente → conclusiones inconsistentes

**Mitigaciones**:

- AGENTS.md mandata explícitamente "**Don't predict ROI without baseline data**"
- Cada párrafo de reporte requiere tag de nivel evidence [E:L#]
- Animar a clientes a cross-validar conclusiones críticas con ≥ 2 AI IDEs

---

## 6. Contribución académica

### 6.1 Contribuciones a IS / metodología consultoría

| Contribución | Innovación |
| --- | --- |
| **Innovación de medio de metodología** | Primera metodología consultoría construida como Markdown + agent config directamente ejecutable por AI IDEs |
| **AI-mediated knowledge transfer** | Usar AI como "traductor de conocimiento" baja barreras de adopción de metodología |
| **Open-source consulting framework** | Apache 2.0, puede ser forkeado / adaptado por otros consultores, académicamente reproducible |
| **Embedded tutor agent design pattern** | Pattern AGENTS.md / CLAUDE.md puede ser tomado prestado por otros repos open-source |

### 6.2 Conexión a AI Pedagogy / ITS

- Investigación ITS de los 1980s estudió "cómo AI enseña" → esta metodología es un nuevo caso de "**cómo AI ayuda a adultos a aprender metodologías profesionales**"
- Aplicación del ZPD de Vygotsky (Zone of Proximal Development): tutor de co-lectura AI ajusta dinámicamente profundidad de prompt

### 6.3 Investigación futura

- Consistencia cross-IDE de interpretación AGENTS.md (Claude Code / Cursor / Antigravity / Codex / Windsurf)
- Tracking longitudinal del efecto del tutor de co-lectura AI en tasa de adopción de metodología (por diseño PILOT_STUDY_PROTOCOL)
- Investigación de adoptabilidad de metodología cross-language (EN / ZH / JA / KO)

---

## 7. Cómo se combina con otros documentos

### 7.1 Statement en diferentes localizaciones

| Localización | Mensaje principal |
| --- | --- |
| Root [`README.md`](../README.md) | Posicionamiento de una frase (ZH §1) |
| Root [`README_EN.md`](../README_EN.md) | Posicionamiento de una frase (EN §1) |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) | Sección "Living Book" |
| [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) | Sección "How to Read This Book" |
| [`AGENTS.md`](../AGENTS.md) | Config concreta de personalidad de tutor (en repo root) |
| Sales decks | 1 slide highlighting diferenciación "AI-native living book" |
| Sumisiones académicas | Capítulo entero como contribución metodológica |

### 7.2 Relación a 4 otros docs autoritativos de concepto

| Documento | Pregunta que responde |
| --- | --- |
| [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) | "¿Qué experimenta el usuario?" |
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | "¿Cómo corre la metodología?" |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | "¿Por qué la metodología resiste el debate?" |
| [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | "¿Cómo se alinea con frameworks de industria?" |
| **`AI_NATIVE_LIVING_BOOK_EN.md` (este doc)** | **"¿Por qué el medio de la metodología es nuevo?"** |

5 docs autoritativos forman un argumento metodológico completo: **experiencia + proceso + ciencia + alignment + innovación de forma**.

---

## 8. Referencias

- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors: Lessons learned. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.
- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Pérez, F., & Granger, B. E. (2007). IPython: A system for interactive scientific computing. *Computing in Science & Engineering*, 9(3), 21-29.
- Anthropic (2024). *Claude Code documentation*: <https://docs.anthropic.com/claude/docs/claude-code>
- OpenAI (2024). *Codex / Codex CLI*.
- Cursor (n.d.). *Cursor IDE documentation*.

---

## 9. Cierre: La próxima fase de metodología

Evolución de metodologías consultoría:

```
1990s: Reportes consultoría papel
   ↓
2000s: Decks PowerPoint
   ↓
2010s: Wikis SharePoint / Confluence
   ↓
2020s: Metodología GitHub-hosted + open source
   ↓
2025s: AI-Native Living Book (esta metodología)
```

**¿Qué sigue?** Posiblemente **equipo consultoría multi-agent auto-running Phase A completa** (AI consultor + AI reviewer + AI client simulator, colaboración 3-Agent) — aplicando L5 Multi-Agent Organization a "la metodología misma".

**Pero**: por §5.1, AI es siempre herramienta y tutor, nunca reemplazo. Juicio de consultor humano, toma de decisión de client owner, audit de tercero — estas **capas de gobernanza humana** son las garantías finales de credibilidad de metodología.

---

Licencia & Citación

Este documento es Apache License 2.0; puede usarse, modificarse, comercializarse, siempre que se preserve la atribución [`../NOTICE`](../NOTICE).
