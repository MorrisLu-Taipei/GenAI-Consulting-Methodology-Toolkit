# TigerAI-n8n-Skill-Pack Aviso de cita & licencia

> 🌐 Idioma: [繁體中文](N8N_SKILL_PACK_REFERENCE.md) ｜ [English](N8N_SKILL_PACK_REFERENCE_EN.md) ｜ [Deutsch](N8N_SKILL_PACK_REFERENCE_DE.md) ｜ [Français](N8N_SKILL_PACK_REFERENCE_FR.md) ｜ Español ｜ [日本語](N8N_SKILL_PACK_REFERENCE_JA.md) ｜ [한국어](N8N_SKILL_PACK_REFERENCE_KR.md)

La segunda mitad del curso **L3 Workflow Automation** en esta metodología cita **TigerAI-n8n-Skill-Pack** como plataforma didáctica para "generar workflows n8n desde lenguaje natural con Antigravity". Este documento registra la fuente upstream, términos de licencia, guía de citación y scope de uso.

---

## 1. Proyecto upstream

| Campo | Valor |
| --- | --- |
| **Proyecto** | TigerAI-n8n-Skill-Pack |
| **Mantenedor** | Morris Lu (盧業興) — n8n Taipei Ambassador |
| **URL GitHub** | <https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack> |
| **Licencia** | Mixta: Skills / Cookbook / Specs son **TigerAI Proprietary**; `skills/_vendor/` es **MIT** (de czlonkowski/n8n-skills); `reference-workflows/` es **MIT** (de Zie619/n8n-workflows, secrets limpiados) |
| **Escala** | 13 Skills (7 vendor + 6 custom), 8 recetas cookbook, 2,061 reference workflows, spec DSL v1.2, 3 ejemplos insignia |
| **Herramientas soportadas** | Antigravity (orquestación agéntica nativa), Claude Code (CLI / VS Code), n8n (2.10.3+), cualquier asistente IA (vía cookbook few-shot prompting) |

> **Nota:** este es el proyecto propio del autor de la metodología Morris Lu; no hay obstáculo de licencia de terceros para citarlo, pero las fuentes MIT bajo `_vendor/` y `reference-workflows/` deben aún retener sus avisos de copyright (ver `THIRD_PARTY_NOTICES.md` upstream).

## 2. Qué es TigerAI-n8n-Skill-Pack

Permite a los usuarios generar workflows n8n grado empresa desde **descripciones en lenguaje natural** en lugar de configuración manual de nodes. El sistema transforma el intent en lenguaje simple "sticky-note" en JSON de workflow completo, documentado, listo para despliegue.

### Estructura de tres capas

`intent sticky-note amarillo` + `notas sticky-note azul` + `nodes de workflow` — el usuario escribe el intent → la IA genera el JSON de tres capas → despliegue vía la API n8n.

### Tres modos de uso

1. **Copia cookbook** — seleccionar entre los 8 templates de receta pre-construidos
2. **Modo Q&R** — la IA guía al usuario a través de la recolección de requerimientos
3. **Example finder** — descubrir implementaciones similares entre los 2,061 reference workflows

### Instalación

`bash install.sh` (Unix) o `install.ps1` (Windows).

## 3. Por qué pertenece a la segunda mitad de L3

El curso L3 está dividido en mitades sobre el principio "conceptos primero, generación después":

- **L3 primera mitad** (§5.1 Foundation + §5.2 Builder): los aprendices **construyen a mano** Trigger / Node / AI / Human Gate / Error Handling, entendiendo estructura y gobernanza del workflow.
- **L3 segunda mitad** (§5.5): sobre esa fundación, usar Antigravity + TigerAI-n8n-Skill-Pack para generar JSON de workflow directamente desde intent en lenguaje natural, y aprender a **revisar** el resultado generado.

> **Principio core: el Skill Pack es un acelerador, no un sustituto del entendimiento.** Sin construir workflows a mano en la primera mitad, los aprendices no pueden juzgar si los resultados generados son correctos, seguros o mantenibles.

Curso correspondiente: [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) §1.1, §5.5.

## 4. Resumen de licencia

| Parte | Licencia | Obligación |
| --- | --- | --- |
| `skills/` (custom), `cookbook/`, `spec/` | TigerAI Proprietary | Licenciado por el autor Morris Lu; sin obstáculo para uso dentro de esta metodología; obtener consentimiento del autor para redistribución externa |
| `skills/_vendor/` | MIT (czlonkowski/n8n-skills) | Preservar el aviso de copyright MIT |
| `reference-workflows/` | MIT (Zie619/n8n-workflows) | Preservar el aviso de copyright MIT; los secrets están limpiados pero verificar uno mismo |

> ⚠️ **Importante**
> Este repo **no redistribuye** la fuente TigerAI-n8n-Skill-Pack. Solo **citamos y enseñamos** su estructura y uso en el curso L3 y dirigimos a los aprendices a **instalar upstream** ellos mismos. Los workflows generados por aprendices usando el Skill Pack pertenecen a la empresa.

## 5. Scope de citación

| Scope | Tratamiento |
| --- | --- |
| **Como plataforma didáctica** | La plataforma de implementación primaria para la segunda mitad de L3 (§5.5) |
| **Fuente / Skills** | **No reproducidos, no forkeados**; los aprendices instalan ellos mismos vía `install.sh` / `install.ps1` |
| **reference-workflows** | Citados para la lección "Example finder"; los aprendices deben confirmar ausencia de secrets / endpoints internos residuales |
| **Output generado** | El JSON de workflow generado es un activo de la empresa; debe pasar Gates 3A-3G para contar como PoC grado empresa |

## 6. Formato de citación para aprendices

> Built with TigerAI-n8n-Skill-Pack by Morris Lu — <https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack>

## 7. Disclaimer

TigerAI-n8n-Skill-Pack es el proyecto propio del autor de la metodología Morris Lu. Si sus Skills, cookbook, spec DSL o instalación cambian en versiones más recientes, referir al [repositorio upstream](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack) y su `THIRD_PARTY_NOTICES.md`. Los workflows generados por IA deben siempre someterse a revisión humana y Gate 3 Acceptance — la generación no es acceptance.
