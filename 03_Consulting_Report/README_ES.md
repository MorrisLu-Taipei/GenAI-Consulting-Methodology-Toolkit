# 03 Consulting Report — Diagnóstico & Informe de Consultoría (Bucle Cerrado de Consultoría)

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Propósito de Este Directorio

Este directorio es la **tercera fase del flujo de servicio 3 fases: Deliver**, y también el **núcleo de la práctica de consultoría** de toda la metodología.

El diagnóstico (`01`) da scores objetivos, el Build (`02`) hace crecer la capacidad del cliente — pero lo que un mandato de consultoría finalmente entrega al cliente es un **informe de diagnóstico estructurado, basado en evidence, con Roadmap y adoptable por decisores**. Este directorio provee todo lo necesario para producir ese informe: **tablas de herramientas de la estructura de consultoría 8 etapas, biblioteca de frameworks clásicos, workflow de producción de informe, plantilla de informe**.

> 🔁 **Este directorio NO es un «maratón lineal de 6 semanas», es el «bucle cerrado de consultoría»**. Diseño completo del bucle ver [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md):
> **Contrato 3 fases** (Phase A Diagnóstico 2W + Phase B Estrategia 4W + Phase C Implementación 24M) + **Informe intermedio** + **Revisión radar trimestral** (mecanismo de falsación de la gestión científica).
> El punto del bucle no es «terminado cuando entregado» — sino «**¿la estructura se volvió realmente más redonda?**» — auto-falsación continua contra el radar Reference Model de Stage 2.

El problema que resuelve: **sin metodología, el diagnóstico del consultor es artesanía personal basada en experiencia — no escalable, no replicable por nuevos consultores, calidad inestable.** Este directorio transforma «cómo un consultor hace un diagnóstico» en bucle cerrado estándar, enseñable, replicable y aceptable.

Quién lo usa: consultores, consultores senior, nuevos consultores (onboarding), gerentes de proyecto.

## 2. Posición en la Metodología

| Eje | Mapeo |
| --- | --- |
| Flujo de servicio 3 fases | **Deliver** — tercera fase |
| Estructura de consultoría 8 etapas | **Este directorio ES las herramientas y el cuerpo del informe de las 8 etapas (Stage 1-8)** |
| **Modelo de contrato 3 fases** | **Phase A Diagnóstico 2W → Phase B Estrategia 4W → Phase C Implementación 24M + revisión radar trimestral** (bucle cerrado de consultoría) |
| Madurez L1-L5 | El informe cita el nivel L y observaciones de curso del cliente |
| Engagement Lifecycle | **Delivery — Handover** (el informe es la entrega central de Phase B; Phase C produce continuamente records de revisión radar) |

> Dos ejes ortogonales: **L1-L5 es la «vertical capacidad» (`02` responsable); las 8 etapas son la «horizontal diagnóstico» (este directorio responsable).** Los dos ejes se cruzan para entregar verificable.
>
> **L1-L5 es en sí mismo dos ejes** (eje de escala L1-L3 + eje de autonomía IA L4-L5); véase [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0.

## 3. Objetivos & Beneficios

| Objetivo | Beneficio |
| --- | --- |
| Cada etapa tiene tablas de herramientas directamente usables | El consultor no debe rehacer diseño; nuevos consultores operativos rápido |
| Biblioteca clásica mapeada a las 8 etapas | Cada etapa sabe «qué framework de análisis usar» |
| Workflow de producción de informe | «Problema → informe/deck entregable» tiene SOP, no artesanía |
| Estructura de informe fijada | Calidad de entrega estable; decisor entiende |
| Metodología de consultoría enseñable y replicable | Equipo de consultores escala |

**Si se salta este directorio**: cada consultor diagnostica a su manera, calidad de informe inconsistente, nuevos consultores no pueden replicar, el diagnóstico degenera en «artesanía personal del senior».

## 4. Flujo & Lógica (Contrato 3 Fases + Bucle Cerrado Trimestral)

```text
01 resultado diagnóstico + 02 observaciones de curso
   ↓
┌─ Phase A Diagnóstico (2 semanas) ──────────────────────┐
│  Stage 1-4 primera mitad de las 8 etapas: Awareness /  │
│  Reference Model / Discovery / Gap Analysis            │
│  → Usar herramientas CONSULTING_TOOLKIT_TEMPLATES.md   │
│  → Informe intermedio → firmado por el cliente         │
└────────────────────────────────────────────────────────┘
   ↓ Gate A — el cliente decide continuar Phase B
┌─ Phase B Estrategia (4 semanas) ───────────────────────┐
│  Stage 5-8 segunda mitad: Stakeholder / Diagnosis /    │
│  To-Be Design / Acceptance Test                        │
│  → Producción 8 pasos REPORT_PRODUCTION_WORKFLOW.md    │
│  → Informe completo 14 capítulos + Roadmap 24M + ROI + │
│     recomendaciones de gobernanza                       │
│  → Llenado en estructura CONSULTING_REPORT_TEMPLATE.md │
└────────────────────────────────────────────────────────┘
   ↓ Gate B — el cliente firma el SOW Phase C
┌─ Phase C Implementación (24 meses) ─ fase feedback ────┐
│  Implementación por fases + **Gate C trimestral:       │
│  re-verificar radar Stage 2**                          │
│  → ¿La estructura se volvió realmente más redonda?     │
│     Si no → regresar a la Stage correspondiente,       │
│     ajustar Roadmap                                     │
│  → Outputs trimestrales: records de revisión radar +   │
│     notas de corrección Roadmap                        │
└────────────────────────────────────────────────────────┘
```

| Fase | Duración | Etapas | Herramientas principales | Entregables principales |
| --- | --- | --- | --- | --- |
| **Phase A Diagnóstico** | 2 semanas | Stage 1-4 | TOOLKIT primera mitad + selector FRAMEWORKS | **Informe intermedio** + radar Reference Model firmado |
| **Phase B Estrategia** | 4 semanas | Stage 5-8 | TOOLKIT segunda mitad + REPORT_PRODUCTION_WORKFLOW + REPORT_TEMPLATE | **Informe completo 14 capítulos** + Roadmap + ROI + gobernanza |
| **Phase C Implementación** | 24 meses | Revisión trimestral de Stage 2 | Herramienta de revisión radar trimestral TOOLKIT + Risk Register | **Records de revisión radar trimestral** + correcciones Roadmap |

> Lógica: `CONSULTING_TOOLKIT_TEMPLATES` es «las herramientas de diagnóstico + la herramienta de revisión trimestral»; `CONSULTING_FRAMEWORKS_LIBRARY` es «qué framework de análisis en cada paso»; `REPORT_PRODUCTION_WORKFLOW` es «cómo transformar eficientemente el diagnóstico en entregable»; `CONSULTING_REPORT_TEMPLATE` es «cómo se ve el informe final». Juntos = **metodología completa de bucle cerrado de consultoría** (no maratón lineal).

> 📖 Script completo de diálogo 8 etapas + story de bucle cerrado: [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) (incl. conclusión «por qué el bucle cerrado es ciencia»).

## 5. Descripciones de Archivos

### `CONSULTING_REPORT_TEMPLATE.md`

Plantilla Markdown del informe de diagnóstico de transformación IA (v2.0 alineado 8 etapas). 14 capítulos fijos: portada, Executive Summary (incl. visión brechas estándar), método de diagnóstico, As-Is Snapshot, Reference Model Alignment (doble coordenada APQC + Tiger AI), Best Practice Integration (perfil de excelencia), Gap Analysis, Executive Problem Statement, Phased Goals, To-Be Design, Implementation Roadmap, Change Management Plan, Governance Design, Value Tracking & Risk Register, recomendaciones SOW.

### `CONSULTING_TOOLKIT_TEMPLATES.md`

**Tablas de herramientas directamente usables** del diagnóstico de consultoría 8 etapas (v2.0 image-aligned). Cada etapa mapea a 1-5 herramientas: banco entrevista 40 preguntas, inventario AI/sistema, swimlane As-Is, **selección Reference Model (APQC/SCOR/eTOM/ITIL/CMMI) + Mapping Worksheet + Standard Gap Checklist + doble radar**, Best-Practice Profile + perfil de excelencia, Missing/Broken/Redundant (**no evaluación de riesgo**), Impact×Effort, **convergencia 80/20 + 5 Whys**, Problem Statement, **Ultimate Benchmark → Phased Goals + evaluación absorción organizacional**, **Phased To-Be Operating Model + Human-AI Collaboration (HITL)**, Skill/Workflow/Agent Map, Transformation Roadmap, **Change Management Playbook (incl. gestión resistencia)**, RACI, permisos, **Value Tracking Matrix (Tiempo/Calidad/Escala/Riesgo/Assets 5 dimensiones)**, Risk Register, Audit, Ethics, **planning estándar Phase A 2W + Phase B 4W + herramienta revisión radar trimestral Phase C** (bucle cerrado de consultoría). Listo para copiar-pegar.

### `CONSULTING_FRAMEWORKS_LIBRARY.md`

Biblioteca de frameworks de consultoría clásicos. 50+ frameworks de la industria (MECE, Pyramid Principle, Issue Tree, Porter's 5 Forces, SWOT, BCG Matrix, 5 Whys, Fishbone, Business Model Canvas, WBS/RACI, NPV/IRR, Lean/Six Sigma, etc.) en 7 categorías. Incluye un «selector de framework» (lenguaje natural → combinación de frameworks), «cadenas de combinación», cada framework mapeado a las 8 etapas, y §4.8 profundización sobre MECE / Issue Tree / formación de hipótesis. Adaptado de yoichiojima-2/consultant (MIT).

### `REPORT_PRODUCTION_WORKFLOW.md`

Workflow de producción de 8 pasos para «problema → informe/deck entregable». Incluye Dummy Page (esqueleto primero, llenar después), gestión de dependencias, 7 layouts de página, pista de evidence Excel, divulgación progresiva, §9 troubleshooting playbook (7 problemas comunes + correcciones). Adaptado de Kafurtan/mckinsey-consultant-skills (MIT).

### `*_EN.md`

Versiones inglesas sibling de los archivos anteriores.

## 6. Mapeo a Otros Directorios

| Directorio | Relación con este directorio | Flujo de datos |
| --- | --- | --- |
| `01_Assessment` | Scores y radar del diagnóstico son input central de Stage 1 | `01` scores → `03` informe |
| `02_Course_Design` | Output y observaciones en clase son material para el capítulo «observaciones de curso» | `02` observaciones → `03` informe |
| `00_Overview` | El informe es la fase «Deliver» de la historia | `00` historia → `03` realización |
| `04_Scenarios` | Stage 3 benchmark Best Practice industrial cita casos | `04` casos → `03` Stage 3 |
| `06_Delivery` | El informe es la entrega central del paquete; mapea al Handover | `03` informe → `06` aceptación entrega |
| `90_References` | Citas de terceros para la biblioteca de frameworks y workflow informe (consultant / mckinsey-skills) | `90` cita → `03` |

## 7. Escenarios de Uso Comunes (por fase de bucle cerrado)

- **Onboarding nuevo consultor**: primero leer `CONSULTING_TOOLKIT_TEMPLATES.md` y recorrer todos los samples, luego leer [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) para el script de diálogo, finalmente shadower una entrevista real.
- **Phase A Diagnóstico (2 semanas)**: usar herramientas TOOLKIT Stage 1-4 (entrevista 40 preguntas, inventario AI/sistema, radar Reference Model), producir al final del período **informe intermedio** para firma Sponsor.
- **Phase B Estrategia (4 semanas)**: usar herramientas TOOLKIT Stage 5-8 + `REPORT_PRODUCTION_WORKFLOW.md` producción 8 pasos para transformar diagnóstico en deck, llenar en `CONSULTING_REPORT_TEMPLATE.md`, producir **informe completo 14 capítulos + Roadmap 24M + ROI**.
- **Phase C Implementación (24 meses, fase feedback bucle)**: trimestralmente con la herramienta de revisión radar TOOLKIT, **relanzar el radar Reference Model Stage 2** — comparar contra versión firmada Phase A, ver si «la estructura se volvió realmente más redonda»; si no → regresar a la Stage correspondiente, ajustar Roadmap.
- **Cliente pregunta «¿por qué este framework?»**: usar el selector de framework en `CONSULTING_FRAMEWORKS_LIBRARY.md` para explicar.
- **Cliente pregunta «¿qué pasa después de las 6 semanas?»**: mostrar [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 diagrama completo de bucle cerrado — el punto no son las 6 semanas, es Phase C 24 meses + mecanismo de falsación por revisión radar trimestral.
