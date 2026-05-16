# 00 Overview — Resumen del Programa & Punto de Entrada

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Propósito de Este Directorio

Este directorio es el **único punto de entrada** de todo el **AI Consulting Methodology Toolkit**. No contiene «herramientas» ni «entregables», solo dos cosas: **la historia de la metodología** y **el estado de la metodología**.

Cualquiera que se encuentre con este repo por primera vez — consultores aprendiendo el método, clientes evaluando comprarlo, nuevos colegas en onboarding, reviewers auditando — debería comenzar aquí. Construya primero aquí la comprensión global («qué es la metodología, por qué está diseñada así, dónde estamos»), luego entre en los directorios funcionales `01`-`06`, para no perder el bosque por los árboles.

El problema que resuelve este directorio: **sin entrada y estado claros, los usuarios se pierden, hacen mal uso de la metodología, y no saben qué está completo y qué en curso.**

## 2. Posición en la Metodología

| Eje | Mapeo |
| --- | --- |
| Flujo de servicio de 3 fases | No corresponde a una sola fase; un **mapa aéreo** sobre «Diagnose → Build → Deliver» |
| Estructura de consultoría de 8 etapas | No corresponde a una sola etapa; una **vista general** de las 8 etapas |
| Madurez L1-L5 | No corresponde a un solo nivel; una **vista general** de L1-L5 |
| Engagement Lifecycle | No corresponde a una sola fase; una **explicación de punto de partida** de todo el ciclo |

> Posicionamiento lógico: `00_Overview` responde «**qué y por qué**»; `01`-`06` responde «**cómo**»; `90_References` responde «**base y citas**».

## 3. Objetivos & Beneficios

| Objetivo | Beneficio |
| --- | --- |
| Hacer entender el esqueleto metodológico a nuevos lectores en 5-10 min | Acortar onboarding; reducir malos usos |
| Contar la propuesta de valor en lenguaje del cliente | Sales puede tomar directamente la historia para briefing de 30 min |
| Mantener un archivo de estado de proyecto autoritativo | Cualquiera puede consultar «dónde estamos, próximo paso» — sin handoff oral |
| Conectar la relación entre `01`-`06` y `90` | Los usuarios conocen el rol y el orden de cada directorio |

**Si se salta este directorio**: los usuarios saltan directo a los directorios funcionales, sin entender «por qué existe este directorio o cómo conecta con otros» — resultado: herramientas usadas aisladamente, metodología se convierte en un montón de archivos dispersos.

## 4. Flujo & Lógica

```text
Nuevo lector / cliente
   → Leer AI_TRANSFORMATION_STORY_AND_STRUCTURE.md (por qué + cómo funciona + qué produce)
   → Construir el modelo mental global «L1-L5 + 8 etapas + 3 fases»
   → Pasar a 01_Assessment para el diagnóstico real

Consultor / colega / reviewer
   → Leer TODO_WBS.md (estado proyecto, changelog, próximos candidatos, diario de trabajo)
   → Entender la situación antes de actuar
```

| Paso | Quién | Cuándo | Input | Output |
| --- | --- | --- | --- | --- |
| Leer la historia | Consultor / cliente / nuevo | Primer contacto con el repo | ninguno | Comprensión global de la metodología |
| Briefear al cliente | Sales / consultor | Primera reunión pre-engagement | Historia | Cliente listo para diagnóstico |
| Consultar estado del proyecto | Consultor / colega / reviewer | Antes de retomar / revisar | ninguno | Situación actual + próximo paso |
| Actualizar estado | Consultor / AI responsable | Tras cada batch | Trabajo terminado | `TODO_WBS.md` actualizado |

> Lógica: la historia es «hacia fuera» (para clientes + nuevos); `TODO_WBS.md` es «hacia dentro» (para ejecutores). Fuera + dentro forman la entrada completa.

## 5. Descripciones de Archivos

### `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`

Historia y estructura de capítulos orientada al cliente. No es documento técnico sino **narración** — cuenta «por qué las empresas necesitan transformación IA, cómo funciona la metodología paso a paso, qué produce cada paso aceptable» como una historia coherente que el cliente entiende. Incluye: posicionamiento de solución, ruta 3 fases, mapeo L1-L5 ↔ herramientas, imaginación futura, propuestas de valor por rol (CEO/COO/CIO/IT/RR.HH./jefe de departamento), §6 definición completa de 8 etapas + escenario 6 semanas. Usable directamente en primera reunión con cliente.

### `EXECUTIVE_SUMMARY.md`

Toda la metodología en 5 minutos en una página. Para ejecutivos sin tiempo para detalles.

### `CLIENT_JOURNEY_STORY.md` 🆕

**La historia de Ming** — una historia escenario por la que CEO / consejo / familia entienden la metodología en 20 minutos. Industria de empaquetado de semiconductores de 700 personas en 24 meses de transformación — cero tabla de herramientas, cero jerga. Usable para comunicación externa, primer contacto con cliente, entrevista de nuevo colaborador.

### `EIGHT_STAGE_FLOW_STORY.md` 🆕

**Historia de referencia de las 8 etapas**: modelo de contrato 3 fases (Phase A Diagnóstico 2W + Phase B Estrategia 4W + Phase C Implementación 24M) + informe intermedio + revisión radar trimestral como bucle cerrado completo. Lectura obligatoria para la formación interna de consultores.

### `METHODOLOGY_SCIENTIFIC_LOGIC.md` 🆕

**Capacidad de debate científico de la metodología**: valida con los 5 criterios del método científico (observable, cuantificable, reproducible, falsable, auditable) por qué las 8 etapas resisten cuestionamiento de cliente / consejo / regulador. Obligatorio para envío académico, lobby político, review del consejo.

### `INDUSTRY_FRAMEWORK_ALIGNMENT.md` 🆕

**Mapa de alineación con frameworks de industria**: 8 etapas vs McKinsey / BCG / Bain / Deloitte / Accenture / PwC; arquitectura 4 capas vs TOGAF / Zachman / Dragon1; L1-L5 vs Gartner / MIT / Forrester AI Maturity. Respuesta a la pregunta del cliente «¿entra en conflicto con nuestra metodología existente?»

### `AI_NATIVE_LIVING_BOOK.md` 🆕

**Discusión de innovación sobre el medio de la metodología**: posiciona esta metodología como **AI-native living book** (un sistema de conocimiento directamente ejecutable por AI IDE), no solo PDF / PPT. Incluye clasificación académica (executable knowledge artifact, AI-mediated methodology, interactive consulting playbook), diseño 3 capas (Repo as Book / Agent as Tutor / Methodology as Executable Artifact), 4 principios de control de riesgo (AI ≠ consultor, evidence requerida, AGENTS.md versionado, output AI marcado). Obligatorio para envío académico / diferenciación metodológica.

### `ACADEMIC_THEORETICAL_FOUNDATIONS.md` 🆕

**Declaración unificada de los 7 pilares teóricos**: Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Task-Technology Fit (Goodhue & Thompson 1995) + Dynamic Capabilities (Teece 1997/2007) + Sociotechnical Systems & Trust in AI (Bostrom 1977/Dietvorst 2015/Glikson 2020) + Real Options (Dixit & Pindyck 1994/McGrath 1997) + Executable Knowledge Artifact (Knuth 1984). Por teoría: resumen + fundador + contribución a Tiger AI + posición de mapeo + citas. La respuesta única cuando academia / regulador / consejo preguntan «¿cuál es la base teórica?»

### `../01_Assessment/BARS_RUBRICS.md` 🆕 (endurecimiento académico)

**Behaviorally Anchored Rating Scales**: tabla de **anclas de comportamiento** 6 dimensiones × 0-4 puntos (según Smith & Kendall 1963). Cada puntuación tiene comportamiento observable concreto, **evita scoring subjetivo del consultor**, mejora inter-rater reliability. Alineado con objetivo Pilot Study Cohen's κ ≥ 0.60. El mecanismo central para que dos consultores den puntuaciones similares a la misma empresa.

### `TODO_WBS.md`

El **archivo de estado autoritativo** de este repo, la única fuente creíble para «dónde estamos». Contiene: visión WBS (items × prioridad × estado), lista de archivos terminados, detalle de items terminados, TODOs abiertos, recomendación para próxima ronda, **changelog (por batch + hash commit)**, visión de estado actual, **diario diario**. Leer antes de cualquier retoma por consultor, review de reviewer, o continuación AI. Actualizar tras cada batch.

### `*_EN.md`

Versiones inglesas sibling de los archivos anteriores, contenido correspondiente a las versiones chinas.

## 6. Mapeo a Otros Directorios

| Directorio | Relación con este directorio | Flujo de datos |
| --- | --- | --- |
| `01_Assessment` | La fase «Diagnóstico» de la historia se realiza aquí | `00` historia → `01` herramientas de diagnóstico |
| `02_Course_Design` | La fase «Build» de la historia se realiza aquí | `00` historia → `02` cursos |
| `03_Consulting_Report` | La fase «Deliver» de la historia se realiza aquí | `00` historia → `03` informe de consultoría |
| `04_Scenarios` | Proporciona escenarios de cliente y casos para la historia | `04` casos ↔ `00` historia |
| `05_Sales` | Transforma la historia en material vendible | `00` historia → `05` material sales |
| `06_Delivery` | Transforma la metodología en negocio entregable y operable | `00` historia → `06` entrega & operaciones |
| `90_References` | Base original de la metodología + licencias citas terceros | `90` base → soporta `00`-`06` |

## 7. Escenarios de Uso Comunes

- **Sales invita cliente**: usa el camino 3 fases y la propuesta de valor de `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md` para briefing de metodología de 30 min.
- **Onboarding nuevo consultor**: primero leer la historia para comprensión → luego `TODO_WBS.md` para estado actual → luego directorios según flujo de datos §6.
- **Reviewer audita**: lee directamente changelog y diario de `TODO_WBS.md`, compara con git log.
- **AI continúa trabajo**: lee «próximos candidatos» y «diario» en `TODO_WBS.md`, sabe dónde retomar.

---

## ⭐ Cross-Topic Quick References: 5 Temas Centrales, Dónde Encontrar

Toda la metodología tiene 5 arterias principales atravesando todos los directorios. Cómo este directorio se conecta a cada una:

| Cross-Topic | Lugar principal | Cómo este directorio se conecta |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lectura tres motores** | Root [`README_ES.md`](../README_ES.md) §🌟 ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | **Este directorio ES el «punto de entrada historia» del AI-Native Living Book** — [`AI_NATIVE_LIVING_BOOK.md`](AI_NATIVE_LIVING_BOOK.md) es la discusión completa; los 4 archivos concepto de referencia (CLIENT_JOURNEY / EIGHT_STAGE_FLOW / METHODOLOGY_SCIENTIFIC_LOGIC / INDUSTRY_FRAMEWORK_ALIGNMENT) viven todos aquí |
| 🎓 **Fundamento académico (7 pilares)** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **La discusión unificada de los 7 pilares teóricos vive en este directorio**: Rosemann / Cohen & Levinthal / TTF / Teece / Sociotechnical Trust / Real Options / Knuth |
| 📚 **Educación L1-L5** | [`../02_Course_Design/`](../02_Course_Design/) | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 es el punto de entrada narrativo autoritativo para **L1-L5 como dos ejes** (eje de escala + eje de autonomía IA) |
| 🔁 **Consultoría / 8 etapas + Closed-Loop Phase A→B→C** | [`EIGHT_STAGE_FLOW_STORY.md`](EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **La historia del bucle cerrado de consultoría vive en este directorio** — `EIGHT_STAGE_FLOW_STORY` §6 tiene el diagrama completo del bucle (Phase A 2W + Phase B 4W + Phase C 24M + revisión radar trimestral) |
| 📖 **Referencias / agradecimientos** | [`../90_References/`](../90_References/) §2 agradecimientos | Las historias de este directorio usan todo el material de `90_References` como base (PDF / diagramas / notas vídeo / citas teóricas) |
