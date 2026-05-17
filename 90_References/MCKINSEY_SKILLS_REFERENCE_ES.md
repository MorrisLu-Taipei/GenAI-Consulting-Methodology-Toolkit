# mckinsey-consultant-skills — Aviso de cita & licencia

> 🌐 Idioma: [繁體中文](MCKINSEY_SKILLS_REFERENCE.md) ｜ [English](MCKINSEY_SKILLS_REFERENCE_EN.md) ｜ [Deutsch](MCKINSEY_SKILLS_REFERENCE_DE.md) ｜ [Français](MCKINSEY_SKILLS_REFERENCE_FR.md) ｜ Español ｜ [日本語](MCKINSEY_SKILLS_REFERENCE_JA.md) ｜ [한국어](MCKINSEY_SKILLS_REFERENCE_KR.md)

El workflow de producción en el [`03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) de esta metodología es referenciado y reescrito basándose en **Kafurtan/mckinsey-consultant-skills**. Este documento registra la fuente upstream, términos de licencia, guía de citación y scope de adaptación.

---

## 1. Proyecto upstream

| Campo | Valor |
| --- | --- |
| **Proyecto** | mckinsey-consultant-skills (V3.1) |
| **Mantenedor** | @Kafurtan |
| **URL GitHub** | <https://github.com/Kafurtan/mckinsey-consultant-skills> |
| **Licencia** | **MIT License** |
| **Forma** | AI agent skill (`SKILL.md` + `references/`) |
| **Contenido** | Un workflow de 8 pasos que automatiza "problema de negocio → presentación estilo McKinsey", end-to-end en 90-110 minutos |

## 2. Qué es mckinsey-consultant-skills

Sistematiza la metodología de Problem Solving de McKinsey en un **workflow de 8 pasos** que permite a un asistente IA convertir un problema de negocio en una presentación profesional (PPT + Excel evidence trail).

### Características estructurales

- **Workflow de 8 pasos**: definir fronteras → Issue Tree + hipótesis → Dummy Pages + design specs → producción iterativa página por página → PPT + Excel → reporte Word opcional → revisión iterativa.
- **Dummy Page**: construir la spec wireframe antes de la investigación, para evitar recolección de datos sin propósito y soportar reanudar entre conversaciones.
- **Consciencia de dependencias**: las páginas se etiquetan con estado de dependencia, determinando orden de producción (el executive summary se hace al último).
- **7 layouts de página**: título + chart único / dos columnas / matriz 2×2 / tabla / waterfall chart / timeline / resumen de insight.
- **Excel evidence trail**: por página raw data + URL + proceso de limpieza.
- **Progressive disclosure**: los archivos de referencia solo se cargan en los pasos que los necesitan y se liberan después, ahorrando ~70% de contexto.
- `references/`: methodology.md, layouts.md, design-specs.md, examples.md, troubleshooting.md.

## 3. Qué adaptamos y citamos

| Scope | Tratamiento |
| --- | --- |
| **El workflow de producción de 8 pasos** | Workflow referenciado, reescrito en el lenguaje de esta metodología, mapeado a la estructura de consultoría de ocho etapas |
| **El concepto Dummy Page** | Disciplina "skeleton-first, fill-in-later" adaptada en specs por página para los outlines de deck de esta metodología |
| **Consciencia de dependencias** | Concepto de gestión de dependencias de página adaptado |
| **Los 7 layouts de página** | Lista de layouts referenciada, reescrita para extender `VISUAL_ASSETS_SPEC.md` |
| **Excel evidence trail, progressive disclosure** | Conceptos adaptados, mapeados a la disciplina Evidence de esta metodología y gestión de contexto AI-IDE |
| **McKinsey Problem Solving, MECE, Pyramid Principle** | Conocimiento de management de dominio público, no propietario a este proyecto |
| **Los archivos `SKILL.md` y `references/` originales** | **No reproducidos, no forkeados**; esta metodología es una reescritura independiente |

## 4. Resumen de licencia

mckinsey-consultant-skills se publica bajo **MIT License**, que permite uso libre, modificación, redistribución y uso comercial, incluyendo como parte de un producto propietario; la única condición es preservar el aviso de copyright MIT y texto de licencia al redistribuir la fuente.

Esta metodología **no redistribuye** su código fuente — reescribió `REPORT_PRODUCTION_WORKFLOW.md` independientemente después de referenciar el workflow y design patterns. El archivo reescrito está bajo Apache 2.0 de este repo; sin embargo, **notamos explícitamente la fuente de citación** en ese archivo y aquí, en respeto a la contribución del autor original.

## 5. Formato de citación para aprendices

> Workflow de producción adaptado de mckinsey-consultant-skills por @Kafurtan — <https://github.com/Kafurtan/mckinsey-consultant-skills> (MIT License)

## 6. Disclaimer

Cualquier cita, adaptación o mapping de ocho etapas de mckinsey-consultant-skills en esta metodología representa la interpretación del autor de la metodología (Morris Lu / Tiger AI 虎智科技) y no representa la posición oficial de @Kafurtan. "McKinsey" es una marca de McKinsey & Company; esta metodología no tiene afiliación o endoso de McKinsey & Company, y los nombres de metodología relacionados se usan solo como referencias a conocimiento de management de dominio público. Si el workflow o estructura de mckinsey-consultant-skills cambia en versiones más recientes, referir al [repositorio upstream](https://github.com/Kafurtan/mckinsey-consultant-skills).
