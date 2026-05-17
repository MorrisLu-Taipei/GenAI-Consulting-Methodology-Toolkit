# consultant Frameworks — Aviso de cita & licencia

> 🌐 Idioma: [繁體中文](CONSULTANT_FRAMEWORKS_REFERENCE.md) ｜ [English](CONSULTANT_FRAMEWORKS_REFERENCE_EN.md) ｜ [Deutsch](CONSULTANT_FRAMEWORKS_REFERENCE_DE.md) ｜ [Français](CONSULTANT_FRAMEWORKS_REFERENCE_FR.md) ｜ Español ｜ [日本語](CONSULTANT_FRAMEWORKS_REFERENCE_JA.md) ｜ [한국어](CONSULTANT_FRAMEWORKS_REFERENCE_KR.md)

La lista de frameworks y taxonomía en el [`03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) de esta metodología son referenciadas y reescritas basándose en **yoichiojima-2/consultant**. Este documento registra la fuente upstream, términos de licencia, guía de citación y scope de adaptación.

---

## 1. Proyecto upstream

| Campo | Valor |
| --- | --- |
| **Proyecto** | consultant |
| **Mantenedor** | @yoichiojima-2 |
| **URL GitHub** | <https://github.com/yoichiojima-2/consultant> |
| **Licencia** | **MIT License** |
| **Forma** | Plugin Claude Code (instalado vía `/plugin marketplace add`) |
| **Contenido** | 50+ frameworks clásicos de consultoría (McKinsey / BCG / Bain / Accenture) en 7 categorías, empaquetados como skill markdown |

## 2. Qué es consultant

consultant es un **plugin Claude Code** que empaqueta 50+ frameworks clásicos de consultoría de management (MECE, Pyramid Principle, Porter's 5 Forces, SWOT, BCG Matrix, PESTEL, 5 Whys, Fishbone, Business Model Canvas, WBS, RACI, Kotter, OKR, NPV/IRR, Lean, Six Sigma, etc.) en un skill markdown.

### Características estructurales

- **Taxonomía de 7 categorías**: problem solving / strategy analysis / case frameworks / business design / project & change / financial analysis / operations.
- **Reconocimiento de trigger**: rutea frases en lenguaje natural "necesito…" a una combinación de frameworks.
- **Combinaciones de frameworks**: cadenas multi-framework pre-construidas (ej. PESTEL → 5 Forces → 3C → SWOT → Issue Tree).
- **Estructura estándar por framework**: origen / concepto core / pasos / cómo aplicar / ejemplo real / trampas comunes.

## 3. Qué adaptamos y citamos

| Scope | Tratamiento |
| --- | --- |
| **Lista de frameworks y taxonomía de 7 categorías** | Taxonomía referenciada, reescrita en el lenguaje de esta metodología |
| **El concepto "framework selector"** (lenguaje natural → framework) | Pattern de reconocimiento de trigger adaptado a un selector alineado con los escenarios de esta metodología |
| **El concepto "framework combination chains"** | Pattern de cadenas de combinación adaptado, mapeado a las ocho etapas de esta metodología |
| **Formato de expansión por framework** | Estructura por framework referenciada, añadida una columna "maps-to-stage" |
| **Los frameworks clásicos mismos** (MECE, Porter's 5 Forces, etc.) | Conocimiento de management de dominio público, no propietario a consultant |
| **Los archivos skill markdown originales** | **No reproducidos, no forkeados**; esta metodología es una reescritura independiente |

## 4. Resumen de licencia

consultant se publica bajo **MIT License**, que permite uso libre, modificación, redistribución y uso comercial, incluyendo como parte de un producto propietario; la única condición es preservar el aviso de copyright MIT y texto de licencia al redistribuir la fuente.

Esta metodología **no redistribuye** el código fuente de consultant — reescribió `CONSULTING_FRAMEWORKS_LIBRARY.md` independientemente después de referenciar la lista de frameworks y design patterns de consultant. El archivo reescrito está bajo Apache 2.0 de este repo; sin embargo, **notamos explícitamente la fuente de citación** en ese archivo y aquí, en respeto a la contribución del autor original.

## 5. Formato de citación para aprendices

> Biblioteca de frameworks adaptada de consultant por @yoichiojima-2 — <https://github.com/yoichiojima-2/consultant> (MIT License)

## 6. Disclaimer

Cualquier cita, adaptación o mapping de ocho etapas de consultant en esta metodología representa la interpretación del autor de la metodología (Morris Lu / Tiger AI 虎智科技) y no representa la posición oficial de @yoichiojima-2. Para las definiciones y aplicación de frameworks clásicos de consultoría, referir a la fuente académica / industrial original de cada framework. Si la lista de frameworks o estructura de consultant cambia en versiones más recientes, referir al [repositorio upstream](https://github.com/yoichiojima-2/consultant).
