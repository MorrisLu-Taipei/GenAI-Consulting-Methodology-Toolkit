# ClawTeam Aviso de cita & licencia

> 🌐 Idioma: [繁體中文](CLAWTEAM_REFERENCE.md) ｜ [English](CLAWTEAM_REFERENCE_EN.md) ｜ [Deutsch](CLAWTEAM_REFERENCE_DE.md) ｜ [Français](CLAWTEAM_REFERENCE_FR.md) ｜ Español ｜ [日本語](CLAWTEAM_REFERENCE_JA.md) ｜ [한국어](CLAWTEAM_REFERENCE_KR.md)

El curso **L5 Multi-Agent Organization** en esta metodología adopta **ClawTeam** como su plataforma de implementación. Este documento registra la fuente upstream, términos de licencia, guía de citación y el scope de nuestro uso.

---

## 1. Proyecto upstream

| Campo | Valor |
| --- | --- |
| **Proyecto** | ClawTeam |
| **Tagline** | The Evolution of AI Agents: Solo 🤖 → Swarm 🦞🤖🤖🤖 |
| **Mantenedor** | HKUDS (HKU Data Science Lab / 香港大學資料科學實驗室) |
| **URL GitHub** | <https://github.com/HKUDS/ClawTeam> |
| **Licencia** | **MIT License** |
| **Versión al momento de escribir** | v0.2 — v0.3 (Stabilization → Multi-User + Web UI) |
| **Lenguaje** | Python 3.10+ |
| **Dependencias** | `tmux`, `git`, cualquier agent CLI (Claude Code / Codex / nanobot / OpenClaw, etc.) |

## 2. Qué es ClawTeam

ClawTeam es un **framework CLI para equipos multi-agent auto-organizantes**: un humano emite un objetivo de alto nivel, y el Agent Team descompone, delega, colabora y merge autónomamente. No es un SDK sino un conjunto de comandos CLI + un filesystem compartido + aislamiento git-worktree + una capa de messaging — **cualquier agent CLI (Claude Code, Codex, Gemini, …) puede ser orquestado por él**.

### Arquitectura core

| Capa | Contenido |
| --- | --- |
| **Team Management** | Un pool de Agents compartiendo workspace & task queue |
| **Workspace Isolation** | Cada Agent corre en su propio git worktree & branch — sin conflictos |
| **Task Tracking** | Estilo Kanban con cadenas de dependencias y auto-unblocking |
| **Inter-Agent Messaging** | Inboxes punto-a-punto + broadcasts |
| **Capa de transporte** | Basada en archivos por defecto; P2P opcional (ZeroMQ); Redis en roadmap |
| **Storage** | Todo JSON en `~/.clawteam/`; sin base de datos, sin servidor central |

### Categorías de comandos CLI core

| Categoría | Comandos clave |
| --- | --- |
| **Team** | `clawteam team spawn-team`, `status`, `snapshot`, `restore` |
| **Task** | `clawteam task create`, `update`, `list`, `wait` (incl. `--blocked-by`) |
| **Inbox** | `clawteam inbox send`, `broadcast`, `receive`, `peek` |
| **Board** | `clawteam board show`, `live`, `attach`, `gource`, `serve` |
| **Profile** | `clawteam profile wizard`, `test`, `doctor`, `generate-profile` |
| **Context** | `clawteam context inject`, `conflicts`, `log` |
| **Spawn** | `clawteam spawn [backend] [command] --profile ...` |

### Tres escenarios de referencia desde upstream

1. **AutoResearch (8 Agents en H100)** — 8 Agents de exploración autónomamente diseñaron 2,430+ experimentos; val_bpb mejorado 1.044 → 0.977 (+6.4%).
2. **Full-Stack Software Engineering (5 Agents)** — Architect, Backend (OAuth2 + DB), Frontend (React), Test/QA — branches paralelas auto-mergeadas.
3. **AI Hedge Fund (7 Agents)** — Portfolio Manager + Value/Growth/Technical/Fundamentals/Sentiment Analysts + Risk Manager — señales convergen a través de la capa de messaging.

### Resumen de roadmap

- **v0.3** — Sistema de config, Multi-User (`CLAWTEAM_USER`), dashboard Web UI, SSHFS / compartir cross-machine basado en cloud
- **v0.4** — Transporte Redis (messaging cross-machine)
- **v0.5** — Capa de estado compartido (NFS o Redis); `RedisTeamStore` / `RedisTaskStore`
- **v0.6** — Identity, permisos, namespacing, token auth (equipos distribuidos)
- **v1.0** — Web UI completa, WebSocket en tiempo real, vista general multi-team

---

## 3. Resumen de licencia

ClawTeam se publica bajo **MIT License**. MIT te permite:

- Usar, modificar y redistribuir libremente
- Usar comercialmente
- Incluir como parte de un producto propietario

**La única condición**: al redistribuir, debes preservar el **aviso de copyright MIT** original y el **texto de la License MIT**.

> ⚠️ **Importante**
> Este repo **no redistribuye** el código fuente de ClawTeam. Solo **citamos y enseñamos** su arquitectura, CLI y principios de diseño en el curso L5 y dirigimos a los aprendices a **instalar upstream** ellos mismos (`pip install clawteam`). Si cualquier derivado del curso (ej. un fork, distribución, o customización) redistribuye código ClawTeam, debe incluir el aviso de licencia MIT original.

---

## 4. Scope de citación en esta metodología

| Scope | Tratamiento |
| --- | --- |
| **Arquitectura & conceptos de diseño** | Usado como la **plataforma didáctica primaria** para L5; el syllabus describe su arquitectura Team / Workspace / Task / Inbox / Transport |
| **Comandos CLI** | Usados **directamente** durante las sesiones hands-on de L5 |
| **Tres escenarios de referencia** | Usados como **inspiración**; esta metodología los localiza en escenarios empresariales de manufactura, hospital y retail |
| **Código fuente** | **No reproducido, no forkeado**; los aprendices `pip install` desde upstream |
| **Brand / Logo** | Citado por nombre "ClawTeam" en el curso y este doc; sin reproducción de logo |

## 5. Formato de citación para aprendices

Al citar ClawTeam en slides, reportes, PoCs o trabajos derivados, usar el siguiente formato:

**Estilo APA:**

> HKUDS. (2026). *ClawTeam: Agent Swarm Intelligence* (Version 0.2-0.3) [Computer software]. GitHub. https://github.com/HKUDS/ClawTeam

**Forma corta:**

> Built on ClawTeam by HKUDS — <https://github.com/HKUDS/ClawTeam> (MIT License)

**Citación académica:**

> ClawTeam [Software]. HKUDS, 2026. Available at: https://github.com/HKUDS/ClawTeam. MIT License.

## 6. Reconocimientos

Agradecemos a **HKUDS (HKU Data Science Lab)** por hacer open-source ClawTeam, que ha elevado la colaboración multi-agent empresarial de un proyecto de investigación a una práctica de engineering enseñable, aprendible y desplegable. El diseño del curso L5 en esta metodología está profundamente informado por su arquitectura y localizado para adopción empresarial en Taiwán y el mundo de habla china.

---

## 7. Disclaimer

- Cualquier descripción, aplicación o adaptación local de ClawTeam en esta metodología representa la interpretación del autor de la metodología (Morris Lu / Tiger AI 虎智科技) y **no** representa la posición oficial de HKUDS o los mantenedores de ClawTeam.
- Si la API, comandos o arquitectura de ClawTeam cambian en versiones más recientes, referir al [repositorio upstream](https://github.com/HKUDS/ClawTeam) para el estado autorizado actual.
- El autor de la metodología se reserva el derecho de actualizar este documento en línea con los cambios upstream de ClawTeam.
