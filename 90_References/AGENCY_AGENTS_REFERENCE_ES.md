# agency-agents Aviso de cita & licencia

> 🌐 Idioma: [繁體中文](AGENCY_AGENTS_REFERENCE.md) ｜ [English](AGENCY_AGENTS_REFERENCE_EN.md) ｜ [Deutsch](AGENCY_AGENTS_REFERENCE_DE.md) ｜ [Français](AGENCY_AGENTS_REFERENCE_FR.md) ｜ Español ｜ [日本語](AGENCY_AGENTS_REFERENCE_JA.md) ｜ [한국어](AGENCY_AGENTS_REFERENCE_KR.md)

La segunda mitad del curso **L2 Knowledge Codification** en esta metodología (específicamente la pista L2-B Agentic Developer) cita **agency-agents** como material didáctico para el módulo "biblioteca de personas de agent listas para usar". Este documento registra la fuente upstream, términos de licencia, guía de citación y scope de uso.

---

## 1. Proyecto upstream

| Campo | Valor |
| --- | --- |
| **Proyecto** | agency-agents |
| **Mantenedor** | @msitarzewski (mantenido por la comunidad) |
| **URL GitHub** | <https://github.com/msitarzewski/agency-agents> |
| **Licencia** | **MIT License** |
| **Escala** | 144+ personas de agent en 12 divisiones |
| **Herramientas soportadas** | Claude Code, GitHub Copilot, Cursor, Aider, Windsurf, OpenCode, Antigravity, Gemini CLI, OpenClaw, Qwen Code, Kimi Code |

## 2. Qué es agency-agents

agency-agents es una **colección de definiciones de personas de AI agent**: cada agent es un archivo markdown que contiene rasgos de identidad, misión core, especificaciones técnicas, procesos de workflow y criterios de éxito medibles. No es un conjunto de templates de prompt genéricos sino un roster de "especialistas virtuales desplegables".

### 12 divisiones

`engineering` (25+ agents: Frontend Developer, Backend Architect, Security Engineer…), `design`, `marketing`, `sales`, `product`, `project-management`, `testing`, `support`, `finance`, `game-development`, `academic`, `specialized`, `spatial-computing`.

### Instalación

Instalado vía `./scripts/install.sh`, que auto-detecta herramientas IA instaladas y las procesa en paralelo.

## 3. Por qué pertenece a L2

El core de L2 Knowledge Codification es "empaquetar experiencia de trabajo en Skills reutilizables." La segunda mitad de la pista L2-B Agentic Developer enseña una idea clave: **no todo Skill necesita construirse desde cero.** agency-agents proporciona 144+ personas de agent maduras como punto de partida — los aprendices seleccionan, customizan e incorporan en la Skill Library de la empresa en lugar de reinventar la rueda.

Curso correspondiente: [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6.

## 4. Resumen de licencia

agency-agents se publica bajo la **MIT License**. MIT permite uso libre, modificación, redistribución y uso comercial, incluyendo como parte de un producto propietario; **la única condición** es que la redistribución debe preservar el aviso de copyright MIT y texto de licencia originales. MIT no requiere estrictamente atribución visible a usuarios finales (aunque el autor nota que es apreciada).

> ⚠️ **Importante**
> Este repo **no redistribuye** la fuente de agency-agents. Solo **citamos y enseñamos** su estructura y uso en el curso L2 y dirigimos a los aprendices a **instalar upstream** ellos mismos. Las personas de agent customizadas por los aprendices pertenecen a la empresa, pero se recomienda notar la fuente original (agency-agents + versión) en la documentación de Skill.

## 5. Scope de citación

| Scope | Tratamiento |
| --- | --- |
| **Como material didáctico** | Usado como caso "biblioteca de agents lista para usar" en la segunda mitad de L2-B; enseña instalar, navegar, seleccionar, customizar |
| **Fuente / archivos de persona** | **No reproducidos, no forkeados**; los aprendices instalan ellos mismos vía `./scripts/install.sh` |
| **Output customizado** | Las personas customizadas se vuelven entradas de la Skill Library de la empresa; atribución de fuente recomendada |

## 6. Formato de citación para aprendices

> Basado en agency-agents por @msitarzewski — <https://github.com/msitarzewski/agency-agents> (MIT License)

## 7. Disclaimer

Cualquier descripción, aplicación o guía de customización para agency-agents en esta metodología representa la interpretación del autor de la metodología (Morris Lu / Tiger AI 虎智科技) y no representa la posición oficial de @msitarzewski o la comunidad agency-agents. Si la estructura, instalación o taxonomía de agent de agency-agents cambia en versiones más recientes, referir al [repositorio upstream](https://github.com/msitarzewski/agency-agents).
