# 05 Sales — Material de Venta Externo

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Propósito de Este Directorio

Este directorio es la primera pieza para **convertir la metodología en negocio**: **material de venta externo**.

`01`-`03` son la metodología de consultoría misma (muy fuerte, pero «fuerte» no se convierte sola en mandatos); el problema que resuelve este directorio: **antes de que el prospecto entre al diagnóstico — ¿cómo Sales lo hace «querer comprar»?** Este directorio proporciona todo, desde DM one-pager, tres longitudes de outline de deck, especificaciones visuales, hasta 20 FAQ ventas — para que Sales tenga material listo, coherente, profesional en todas las etapas de Lead Gen, propuesta, gestión de objeciones.

Corresponde a la **fase Sales** del ciclo de engagement: lleva un lead frío a «listo para llenar el cuestionario y entrar al diagnóstico».

Quién lo usa: Sales (Lead Gen / Sales Rep / Closer), consultores (briefing metodología al C-level), diseñadores (producen visuales reales según especificación).

## 2. Posición en la Metodología

| Eje | Mapeo |
| --- | --- |
| Flujo de servicio 3 fases | **«Pre-venta» antes del diagnóstico** — lleva al cliente al punto de entrar al diagnóstico |
| Estructura de consultoría 8 etapas | No corresponde a ninguna de las 8 etapas (las 8 etapas son tras firma) |
| Madurez L1-L5 | Material de venta usa el modelo L1-L5 como argumento |
| Engagement Lifecycle | **Sales — Lead Qualification / Discovery / Proposal** |

## 3. Objetivos & Beneficios

| Objetivo | Beneficio |
| --- | --- |
| Material externo coherente y profesional | Diferentes Sales hablan la metodología de forma uniforme, marca pro |
| Tres longitudes de deck para diferentes contextos | C-level 10 páginas, estándar 20 páginas, metodología 30 páginas, cada uno adaptado |
| 20 FAQ ventas | Sales tiene respuestas estándar a objeciones, no improvisa |
| Especificaciones visuales | Diseñadores tienen brief claro, assets visuales coherentes |
| One-pager DM | Primer contacto con cliente da ya un entregable pro |

**Si se salta este directorio**: cada Sales hace sus propias slides, discursos inconsistentes, objeciones improvisadas, primera impresión de la metodología dispersa.

## 4. Flujo & Lógica

```text
Lead Gen
   → ONE_PAGER_OUTLINE (DM one-pager, entregable primer contacto)
Primera reunión formal
   → EXECUTIVE_DECK_OUTLINE (10 páginas C-level, urgencia + credibilidad metodología)
Propuesta profunda
   → STANDARD_SALES_DECK_OUTLINE (20 páginas, para jefe de departamento/IT/RR.HH.)
   → CONSULTING_METHODOLOGY_DECK_OUTLINE (30 páginas, profundidad metodo, para CIO/jefe estrategia/académicos)
Gestión de objeciones (continuo)
   → SALES_FAQ (20 Q&A estándar)
Producir visuales reales
   → VISUAL_ASSETS_SPEC (diseñador produce PNG/SVG/archivos print según spec)
```

| Paso | Quién | Cuándo | Input | Output |
| --- | --- | --- | --- | --- |
| Enviar DM one-pager | Sales (Lead Gen) | Lead Gen | one-pager | Cognición cliente inicial |
| Briefing C-level | Sales / consultor | Primera reunión | deck 10 páginas | Cliente listo para discusión profunda |
| Propuesta profunda | Closer | Fase propuesta | deck 20/30 páginas | Cliente listo a firmar SOW |
| Tratar objeciones | Sales / Closer | Continuo | SALES_FAQ | Dudas del cliente eliminadas |
| Producir visuales | Diseñador | Fase de producción | VISUAL_ASSETS_SPEC | Archivos visuales reales |

> Lógica: material **de superficial a profundo** — one-pager (despertar interés) → 10 páginas (crear urgencia) → 20/30 páginas (convicción profunda) → FAQ (eliminar dudas). Cada uno apunta al mismo próximo paso: «llenar cuestionario 10 ítems, entrar al diagnóstico `01_Assessment`».

## 5. Descripciones de Archivos

### `SALES_VALUE_PROPOSITION.md`

Propuestas de valor por rol y scripts de venta. Para los dolores de CEO / COO / CIO / IT / RR.HH. / jefe de departamento, propuestas de valor correspondientes, más scripts 30 segundos / 3 minutos / 10 minutos y objeciones comunes.

### `SALES_FAQ.md`

20 FAQ ventas externas. Preguntas más hechas (diferencia con Big-4, estructura de precios, timeline, customización, cloud/on-prem, seguridad, ROI, IP, elección modelo AI, gestión de fallo…), 2-4 frases de respuesta estándar cada una, zh+en paralelas.

### `ONE_PAGER_OUTLINE.md`

Script de contenido y brief de layout para PDF / impreso one-pager (aprox. 600 palabras). Incluye Hero tagline, tres dolores, flujo 3 fases, mapa L1-L5, entregables verificables, aplicabilidad 3 sectores, ROI proof point, CTA, más sugerencias layout/colores/tipo para diseñador.

### `EXECUTIVE_DECK_OUTLINE.md`

Outline deck C-level 10 páginas. Objetivo CEO/COO/CIO/CTO. Cada página: título, mensaje clave, contenido, sugerencia visual, notas orador. Cubre visión, urgencia, metodología, L1-L5, story arc, ROI, gobernanza, diferenciación competitiva, precio, siguientes pasos.

### `STANDARD_SALES_DECK_OUTLINE.md`

Outline deck estándar 20 páginas. Objetivo jefes de departamento, PM, IT Lead, RR.HH., AI Champion. Más amplio que 10 páginas, incluye teasers de cursos por nivel, escenarios PoC, Stage Gate, paquete de entrega, inicio 3 fases.

### `CONSULTING_METHODOLOGY_DECK_OUTLINE.md`

Outline deck metodología 30 páginas. Objetivo CIO, jefe estrategia, grandes oficinas de transformación digital, académicos. Profundidad metodología — 8 etapas, encadenamiento L1-L5, modelo de scoring, extractos de casos, gobernanza, raíces académicas (Prof. Michael Rosemann, QUT).

### `VISUAL_ASSETS_SPEC.md`

Spec ASCII y brief diseñador para 3 assets visuales externos: diagrama flujo servicio 3 fases, mapa madurez L1-L5, visual lista entregables verificables. Cada uno con spec ASCII, alternativas de layout, requisitos color/tipo/tamaño/accesibilidad.

### `*_EN.md`

Versiones inglesas sibling de los archivos anteriores.

## 6. Mapeo a Otros Directorios

| Directorio | Relación con este directorio | Flujo de datos |
| --- | --- | --- |
| `00_Overview` | Esqueleto historia del material de venta viene de la historia | `00` historia → `05` material |
| `01_Assessment` | Todo material de venta apunta a «llenar cuestionario → diagnóstico» | `05` → drive hacia `01` |
| `02_Course_Design` | Teasers de cursos en los decks vienen del diseño de cursos | `02` cursos → `05` teaser |
| `03_Consulting_Report` | Deck metodología 30 páginas cita las 8 etapas y frameworks | `03` metodología → `05` deck |
| `04_Scenarios` | Material de venta usa casos y escenarios completos para justificar valor | `04` casos → `05` justificación |
| `06_Delivery` | Precios/paquetes del deck corresponden al ciclo y pricing | `06` pricing ↔ `05` deck |

## 7. Escenarios de Uso Comunes

- **Lead Gen**: Sales envía DM one-pager hecho desde `ONE_PAGER_OUTLINE.md`.
- **Primera reunión**: usar `EXECUTIVE_DECK_OUTLINE.md` para briefing 15-20 min C-level, terminar con «llenar cuestionario 10 ítems».
- **Propuesta profunda**: según objetivo elegir 20 páginas (jefe de departamento) o 30 páginas (CIO/jefe estrategia).
- **Cliente dice «demasiado caro / ya tenemos ChatGPT / ¿los datos están seguros?»**: abrir `SALES_FAQ.md` para respuesta estándar.
- **Hacer visuales**: dar `VISUAL_ASSETS_SPEC.md` al diseñador para producir archivos reales.

---

## ⭐ Cross-Topic Quick References: 5 Temas Centrales, Dónde Encontrar

Toda la metodología tiene 5 arterias principales atravesando todos los directorios. Cómo este directorio se conecta a cada una:

| Cross-Topic | Lugar principal | Cómo este directorio se conecta |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lectura tres motores** | Root [`README_ES.md`](../README_ES.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | **AI-Native Living Book + tres motores es un nuevo argumento de venta** — tras adopción, cliente tiene «metodología + compañero AI de co-lectura»; el deck 30 páginas puede pitchear la diferenciación de la división de los tres motores (frontline Antigravity / audit Codex / estrategia Claude Code) |
| 🎓 **Fundamento académico (7 pilares)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **El deck 30 páginas cita Prof. Rosemann (QUT) + 7 pilares teóricos** como diferenciación (para académicos, CIO, consejo); `SALES_FAQ.md` usa los 7 pilares como base para «diferencia con Big-4 / McKinsey» |
| 📚 **Educación L1-L5** | [`../02_Course_Design/`](../02_Course_Design/) | **El deck 20 páginas contiene teasers de cursos por nivel** (camino L1-L5, escenarios PoC, Stage Gate); ONE_PAGER contiene mapa L1-L5; decks citan ratio de cursos y currículos profundos de `02` |
| 🔁 **Consultoría / 8 etapas + Closed-Loop Phase A→B→C** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Todo material de venta dirige a «llenar cuestionario → iniciar Phase A»**; deck 20/30 páginas contiene modelo de contrato 3 fases (Phase A 2W + Phase B 4W + Phase C 24M) + revisión radar trimestral; EXECUTIVE_DECK contiene story arc 8 etapas |
| 📖 **Referencias / agradecimientos** | [`../90_References/`](../90_References/) §2 agradecimientos | **Los decks Sales son mayormente self-authored** (sin citas de terceros); `SALES_FAQ.md` cita los 7 pilares como base; agradecimientos citan Prof. Rosemann (QUT); si cliente pregunta «por qué estas herramientas», apuntar a las appreciation cards de 90_References §2 |
