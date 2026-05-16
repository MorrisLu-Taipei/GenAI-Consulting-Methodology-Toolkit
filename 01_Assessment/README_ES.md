# 01 Assessment — Diagnóstico de Madurez IA

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Propósito de Este Directorio

Este directorio es la **primera fase: Diagnóstico (Diagnose)** del flujo de servicio de 3 fases. Resuelve uno de los problemas más fundamentales del trabajo de consultor: **«La empresa dice que 'usa IA', pero ¿en qué nivel exactamente? ¿Qué le falta? ¿Por dónde empezar?»**

Sin diagnóstico objetivo, los consultores solo pueden componer cursos a partir de descripciones subjetivas del cliente — resultado frecuente: saltos de nivel (el cliente ni siquiera tiene uso L1 generalizado pero quiere hacer un Agent L4) o prioridades equivocadas (falta gobernanza pero se siguen agregando herramientas). Este directorio transforma con tres longitudes de cuestionario + modelo de scoring + encuesta de perfil empresarial las «impresiones difusas» en **puntuaciones L1-L5 objetivas, cuantificables, comparables, y diagramas radar de brechas en seis dimensiones**.

Quién usa este directorio: Sales (versión 10 ítems para calificación lead), consultores (versiones 25/50 ítems para inventario pre-curso y pre-entrevista), IT/AI Champion (cuestionario perfil empresarial).

## 2. Posición en la Metodología

| Eje | Mapeo |
| --- | --- |
| Flujo de servicio 3 fases | **Diagnóstico** — primera fase |
| Estructura de consultoría 8 etapas | **Etapa 1 Captura del existente** (resultado del diagnóstico es input central de Etapa 1) |
| Madurez L1-L5 | Este directorio es la herramienta para «**determinar en qué nivel está el cliente**» |
| Engagement Lifecycle | **Sales — Lead Qualification (10 ítems) / Discovery (25/50 ítems)** |

## 3. Objetivos & Beneficios

| Objetivo | Beneficio |
| --- | --- |
| Reemplazar conjetura subjetiva por scores objetivos | El consultor tiene base para componer cursos, no solo intuición |
| Encontrar brechas en seis dimensiones (herramientas/conocimiento/proceso/integración/Agent/gobernanza-ROI) | Saber dónde el cliente es fuerte / débil |
| Derivar directamente tres recomendaciones | Ratio de cursos + modo de despliegue + escenario PoC en un paso |
| Tres longitudes de cuestionario para tres fases comerciales | Desarrollo lead, pre-curso, pre-entrevista — cada cual su herramienta |
| Automatizable | Cuestionario → scoring → informe totalmente automático, el consultor solo interpreta |

**Si se salta este directorio**: ratio de cursos adivinado, expectativas del cliente no manejables (señala un caso L5 «quiero eso» sin saber que está en L2), informe de consultoría sin punto de partida objetivo.

## 4. Flujo & Lógica

```text
Cuestionario rápido 10 ítems (desarrollo lead, 3 min)
   → Calificación lead + posición L inicial
Cuestionario 25 ítems (pre-curso, 8 min, llenado por managers del cliente)
   → Scores seis dimensiones + diagrama radar
Cuestionario 50 ítems (pre-entrevista consultor, 20 min, IT/AI Champion)
   → Inventario completo + preguntas abiertas
Cuestionario perfil empresarial (35 ítems)
   → JSON Profile Bundle (sistema / riesgo / preferencia despliegue / presupuesto)
        ↓ Merge
   Auto-scoring → nivel L1-L5 + radar seis dimensiones
        ↓ Derivación
   ① Ratio de cursos recomendado  ② Modo de despliegue recomendado  ③ Escenario PoC recomendado
```

| Paso | Quién | Cuándo | Input | Output |
| --- | --- | --- | --- | --- |
| Quickscreen 10 ítems | Sales | Desarrollo lead | Prospecto | Calificación + nivel L inicial |
| Diagnóstico pre-curso 25 ítems | Grupo de managers cliente | 1 semana antes del L1 | Cuestionario 25 ítems | Scores seis dimensiones |
| Inventario completo 50 ítems | IT/AI Champion cliente | Antes entrevista consultor | 50 ítems + perfil empresarial | Profile Bundle completo |
| Auto-scoring | Sistema (Sheets/Notion/n8n) | Tras submission | Respuestas | Nivel L + radar + 3 recomendaciones |
| Interpretación | Consultor | Tras informe auto | Informe auto | Dirección de propuesta personalizada |

> Lógica: el cuestionario es solo **input**; el verdadero output es «**nivel L + brechas seis dimensiones + 3 recomendaciones**». Estos tres alimentan — ratio de cursos → `02_Course_Design`; modo de despliegue → To-Be Design de `03`; escenario PoC → índice de casos de `04_Scenarios`. El diagnóstico no es el fin, es el interruptor que «enciende» los tres directorios siguientes.

## 5. Descripciones de Archivos

### `AI_MATURITY_QUESTIONNAIRE.md`

Cuestionario de madurez IA en tres longitudes 10 / 25 / 50 ítems. Versión 10 ítems para evaluación rápida comercial; versión 25 ítems 4-5 preguntas por dimensión para pre-curso; versión 50 ítems más modo de despliegue e inventario sistema para pre-entrevista. Las tres versiones comparten la escala 0-4 y la arquitectura seis dimensiones.

### `AI_MATURITY_SCORING_MODEL.md`

Lógica de scoring y reglas de decisión. Incluye: scoring de las seis dimensiones (uso herramientas, capitalización conocimiento, estandarización procesos, integración sistemas, aplicación Agent, gobernanza-ROI), umbrales totales correspondientes a L1-L5, **madurez principal vs madurez local** (por qué un departamento puede ser localmente L4 pero globalmente L2), reglas de recomendación del modo de despliegue y ratio de cursos.

### `AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`

Definition of Done, Deliverables, Evidence, Owner, Stage Gate, Fail Condition, Next Level Entry Criteria para cada nivel L1-L5. Define «a qué se parece 'terminado' en cada nivel, qué evidence como prueba» — base de la aceptación Stage Gate.

### `FILLABLE_QUESTIONNAIRE.md`

Especificación de renderizado que transforma 10/25/50 ítems en formularios llenables — tipos de preguntas (radio / escala 0-4 / multi-elección / respuesta corta), segmentación, skip logic, página de submission y página «qué pasará después». Con consejos de renderizado para Google Form / Tally / Notion Form.

### `COMPANY_PROFILE_QUESTIONNAIRE.md`

Cuestionario perfil empresarial 35 ítems, 6 secciones (Profile / Systems / Risk / Deployment / Course / Budget). Output: JSON Profile Bundle, más **reglas de derivación**: del Bundle derivar automáticamente recomendaciones de despliegue, fine-tuning del ratio de cursos, sugerencias PoC. Vinculado al cuestionario de madurez por `submission_id`.

### `AI_DIAGNOSIS_SHEETS_SCHEMA.md`

Schema de implementación para automatizar todo el diagnóstico. Tres plataformas: Google Sheets (fórmulas de scoring, formato condicional, Apps Script), Notion (4 estructuras de database y fórmulas), n8n (flow auto-diagnóstico de 13 nodes, incl. idempotency). Del cuestionario al scoring a la generación de informe y notificación al consultor, todo automático.

### `*_EN.md`

Versiones inglesas sibling de los archivos anteriores.

## 6. Mapeo a Otros Directorios

| Directorio | Relación con este directorio | Flujo de datos |
| --- | --- | --- |
| `00_Overview` | El diagnóstico es la primera fase de la historia | `00` historia → `01` realización |
| `02_Course_Design` | El «nivel L + ratio de cursos» del diagnóstico determina directamente la configuración | `01` ratio → `02` configuración |
| `03_Consulting_Report` | El resultado del diagnóstico es input de Etapa 1; el informe cita los scores y radar | `01` scores → `03` informe |
| `04_Scenarios` | Tras diagnóstico, según nivel L, usar `LLM_APPS_CASE_INDEX.md` para elegir PoCs | `01` nivel L → `04` selección casos |
| `06_Delivery` | El diagnóstico corresponde a la fase Sales del ciclo de engagement | `01` ↔ `06` fase Sales |
| `90_References` | Base metodológica del modelo de scoring | `90` base → `01` |

## 7. Escenarios de Uso Comunes

- **Desarrollo comercial**: prospecto llena la versión 10 ítems → informe auto en 24 h → Sales va al encuentro con el nivel L.
- **Preparación pre-curso**: 1 semana antes del inicio, enviar la versión 25 ítems a managers → el consultor recibe el radar seis dimensiones, ajusta el ratio.
- **Antes entrevista consultor**: IT/AI Champion llena 50 ítems + perfil empresarial → el consultor recibe 1 h antes de la entrevista el Profile Bundle completo como brief.
- **Para escalar**: con `AI_DIAGNOSIS_SHEETS_SCHEMA.md` desplegar el flow auto-diagnóstico en el n8n del cliente, el consultor solo interpreta al final.

---

## ⭐ Cross-Topic Quick References: 5 Temas Centrales, Dónde Encontrar

Toda la metodología tiene 5 arterias principales atravesando todos los directorios. Cómo este directorio se conecta a cada una:

| Cross-Topic | Lugar principal | Cómo este directorio se conecta |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lectura tres motores** | Root [`README_ES.md`](../README_ES.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | El cuestionario puede llenarse interactivamente via Antigravity `/diagnose`; AI_DIAGNOSIS_SHEETS_SCHEMA automatiza el cuestionario (n8n + Google Sheets + Notion); el resultado puede entrar a Codex `/consistency-review` para alineación entre archivos |
| 🎓 **Fundamento académico (7 pilares)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **[`BARS_RUBRICS.md`](BARS_RUBRICS.md) de este directorio corresponde a inter-rater reliability** (Smith & Kendall 1963); las seis dimensiones corresponden a Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Sociotechnical Trust |
| 📚 **Educación L1-L5** | [`../02_Course_Design/`](../02_Course_Design/) | **La determinación del nivel L + radar seis dimensiones + recomendación de ratio** del diagnóstico determina directamente la configuración `02` — es el «prerequisito» de `02` |
| 🔁 **Consultoría / 8 etapas + Closed-Loop Phase A→B→C** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Diagnóstico = input central de Phase A** (Etapa 1 captura del existente + Etapa 2 firma radar Reference Model); la revisión radar trimestral de Phase C ES «**rehacer el diagnóstico**» — ¿la estructura se ha vuelto realmente más redonda? El diagnóstico es a la vez entrada y mecanismo de falsación del bucle |
| 📖 **Referencias / agradecimientos** | [`../90_References/`](../90_References/) §2 agradecimientos | Modelo de scoring referencia BARS (Smith & Kendall 1963) + 7 pilares teóricos; plan empírico 18-24 meses Pilot Study ver [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) (valida el objetivo Cohen's κ ≥ 0.60 del cuestionario) |
