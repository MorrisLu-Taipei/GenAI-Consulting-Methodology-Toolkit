# 02 Course Design — Diseño de Cursos L1-L5

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Propósito de Este Directorio

Este directorio es la **segunda fase: Build (Build)** del flujo de servicio de 3 fases. El diagnóstico (`01`) le dice «en qué nivel está el cliente, qué le falta»; este directorio contiene **los cursos concretos que cierran la brecha**.

El problema que resuelve: **la transformación IA no se logra solo comprando herramientas o asistiendo a conferencias — la empresa debe atravesar L1-L5 nivel por nivel y producir activos aceptables.** Este directorio proporciona para cada nivel L1 a L5 currículos completos: objetivos de curso, audiencia, prerrequisitos, contenido, ejercicios, deberes, estándares de finalización, Stage Gate. Cada nivel produce **entregables aceptables** (L1 Prompt Library, L2 Skill, L3 Workflow, L4 Agent, L5 Agent Team) — no «olvidado tras el curso».

Quién lo usa: instructores, AI Champions, IT, aprendices de todos los niveles.

## 2. Posición en la Metodología

| Eje | Mapeo |
| --- | --- |
| Flujo de servicio 3 fases | **Build** — segunda fase |
| Estructura de consultoría 8 etapas | **Etapa 7 To-Be Design** (los cursos son la implementación concreta de la solución) |
| Madurez L1-L5 | Este directorio es el cuerpo de cursos que «**llevan al cliente de su nivel actual al siguiente**»; cubre L1-L5 **dos ejes** |
| Engagement Lifecycle | **Delivery — Build** |

> Principio central 1: **L1-L5 encadenado — el output del nivel inferior es input del siguiente.** Sin uso L1 generalizado, no hay Skills para L2; sin Skills L2, los Workflows L3 son tubos vacíos; sin Workflows L3, el Agent L4 no tiene herramientas; sin Agents L4, el equipo L5 no tiene miembros. **Sin saltos de nivel.**
>
> Principio central 2: **L1-L5 son dos ejes** — eje de escala (L1 individuo → L2 departamento → L3 entre departamentos / toda la empresa, humano supervisa IA) y eje de autonomía IA (L4 super-asistente → L5 equipo IA, IA autónoma, humano retrocede a gobernador). Frontera crítica en L3 → L4. Véase [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0. Terminología: **Stage Gate = puerta de aceptación por etapa**, **HITL = Human-in-the-Loop (humano en el bucle de review)**.

## 3. Objetivos & Beneficios

| Objetivo | Beneficio |
| --- | --- |
| Cada nivel tiene currículo completo y entregable | El instructor puede enseñar directo, sin rehacer diseño |
| La producción en clase deja activos aceptables | Los resultados se convierten en capacidad organizacional, no «olvidado tras el curso» |
| Cada nivel tiene Stage Gate | Sin avance sin pasar, evita saltos fallidos |
| Ratio de cursos configurado según scores de diagnóstico | Recursos del cliente concentrados en brechas, no desperdiciados |
| L3/L4 con biblioteca de escenarios PoC + esqueletos n8n | Ejercicios prácticos con temas y templates listos, no desde cero |

**Si se salta este directorio**: el cliente compra herramientas sin capacidad, los PoCs se quedan eternamente en demo, la IA no escala.

## 4. Flujo & Lógica

```text
01_Assessment diagnóstico → nivel L + recomendación de ratio
   ↓
COURSE_REQUIREMENTS_AND_COMPANY_PROFILE (confirmar prerrequisitos, perfil, modo despliegue)
   ↓
COURSE_MODULE_MATRIX (ver outline L1-L5 y configuración de ratios)
   ↓
L1_L5_COMPLETE_COURSE_PLAN (currículo global) + currículos profundos por nivel:
   L1 OPENWEBUI → L2 ANTIGRAVITY → L3 N8N → L4 HERMES → L5 CLAWTEAM
   ↓ por nivel
   Clase → ejercicios (con POC_SCENARIO_SPECS / N8N_WORKFLOW_TEMPLATES como temas)
   → Producir activos aceptables → pasar Stage Gate → luego siguiente nivel
```

| Paso | Quién | Cuándo | Input | Output |
| --- | --- | --- | --- | --- |
| Confirmar prerrequisitos | Consultor + IT cliente | Antes del curso | Resultado diagnóstico, perfil | Checklist pre-curso pasada |
| Configurar ratio | Consultor | Antes del curso | Nivel L + recomendación | Configuración horaria L1-L5 |
| Clase (por nivel) | Instructor | Fase build | Currículos profundos | Resultados aprendices |
| Ejercicios | Aprendices | En clase cada nivel | Escenario PoC / esqueleto n8n | Prompt/Skill/Workflow/Agent/Team |
| Aceptación Stage Gate | Consultor + manager cliente | Tras cada nivel | Output en clase | Gate pasado → siguiente nivel |

> Lógica: los cursos no son «enseñar uso de herramienta» sino «construir capacidad organizacional verificable a lo largo de la madurez». Cada nivel sigue la estructura «primera mitad producir, segunda mitad conectar al siguiente».

## 5. Descripciones de Archivos

### `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md`

Lista de requisitos de cursos L1-L5 y encuesta de perfil empresarial. Define para cada nivel prerrequisitos, datos básicos, atributos de datos y riesgo, inventario sistema, condiciones de elegibilidad y notas de curso para tres modos de despliegue (cloud IA / híbrido / on-prem completo). Usado antes del curso para confirmar «¿está listo el cliente?».

### `COURSE_MODULE_MATRIX.md`

Matriz de módulos de cursos L1-L5. Una tabla muestra para cada nivel: objetivos, ejercicios, output deberes, packaging (medio día experiencia / taller de un día / bootcamp dos días / proyecto consultoría) y reglas de recomendación de ratio según madurez.

### `L1_L5_COMPLETE_COURSE_PLAN.md`

Planificación completa L1-L5. Por nivel: objetivos, contenido, ejercicios, deberes, estándar de finalización y resumen Stage Gate. Currículos profundos por nivel en los cinco archivos siguientes.

### `L1_OPENWEBUI_COURSE_PLAN.md`

Currículo profundo L1 Controlled AI Access. Referencia playlist pública OpenWebUI, incluye login por persona, espacio chat personal, Admin Panel, cuentas/roles/grupos/permisos, control de modelos, normas de datos, mapa de referencia vídeo.

### `L2_ANTIGRAVITY_COURSE_PLAN.md`

Currículo profundo L2 Knowledge Codification. Referencia tres codelabs Google Antigravity, incluye Agentic IDE, App Prototype, Unit Test, GCP Serverless Pipeline, Gate 2A-2E. **§7.6** incluye módulo «usar biblioteca Agent existente (agency-agents)». Segunda mitad: Bridge L2→L3.

### `L3_N8N_TIGERAI_COURSE_PLAN.md`

Currículo profundo L3 Workflow Automation. **§1.1** divide L3 en primera mitad (concepto n8n y construcción manual) y segunda mitad (AG + TigerAI-n8n-Skill-Pack generación en lenguaje natural, **§5.5**). Referencia vídeos canal TigerAI n8n / OpenGenie, incluye Gemini, multimodal, Sub-workflow, Data Tables, Webhook, GitHub Backup, Gate 3A-3G.

### `L4_HERMES_AGENT_COURSE_PLAN.md`

Currículo profundo L4 Autonomous Agent. **§2** «siete principios de diseño de Agent knowledge-grade» (día ligero / noche pesada, bucle de capitalización conocimiento, P1>P2, escritura-lectura-misma-fuente, división herramientas/LLM, aprendizaje impulsado por failure-mode, por qué no solo RAG). Incluye combinación master + skills especializados, memoria Wiki, ingest/query/update, Gate 4A-4E. **Este curso solo toma conceptos, no código interno.**

### `L5_CLAWTEAM_COURSE_PLAN.md`

Currículo profundo L5 Multi-Agent Organization. Sobre la base de HKUDS/ClawTeam (MIT) como plataforma de implementación, incluye arquitectura cinco capas Team/Workspace/Task/Inbox/Transport, git worktree, CLI hands-on, tres escenarios localizados, Gate 5.

### `POC_SCENARIO_SPECS.md`

Biblioteca de escenarios PoC para cursos L3/L4. 7 categorías en total 35 PoCs implementables (Gmail / Sheets / Notion / CRM / API / ERP + contabilidad), cada uno con trigger, input, AI step, systems, output, acceptance, KPI, person-day, secuencia node n8n. Elegir directamente los temas de ejercicio aquí.

### `N8N_WORKFLOW_TEMPLATES.md`

Organizar los PoCs en esqueletos workflow n8n importables (JSON). Incluye 30 esqueletos PoC, flow export/import, especificación de nombrado de versión, SOP GitHub Backup, flow de uso en clase.

### `*_EN.md`

Versiones inglesas sibling de los archivos anteriores.

## 6. Mapeo a Otros Directorios

| Directorio | Relación con este directorio | Flujo de datos |
| --- | --- | --- |
| `01_Assessment` | Nivel L + ratio de cursos del diagnóstico determina la configuración | `01` ratio → `02` configuración |
| `00_Overview` | Los cursos son la fase «Build» de la historia | `00` historia → `02` realización |
| `03_Consulting_Report` | Output y observaciones en clase alimentan el informe 8 etapas | `02` output → `03` informe |
| `04_Scenarios` | Temas de demo desde el índice de casos; PoCs pueden volverse casos | `04` casos ↔ `02` temas de curso |
| `06_Delivery` | Cursos corresponden a Delivery — Build del ciclo; entregables hacia aceptación | `02` output → `06` aceptación |
| `90_References` | Citas de terceros por nivel (OpenWebUI / Antigravity / n8n-Skill-Pack / ClawTeam / agency-agents) | `90` cita → `02` |

## 7. Escenarios de Uso Comunes

- **Configurar ratio de cursos**: tomar el ratio del diagnóstico → usar `COURSE_MODULE_MATRIX.md` para configurar horas → abrir el currículo profundo correspondiente.
- **Dar curso L3**: usar primera mitad de `L3_N8N_TIGERAI_COURSE_PLAN.md` para concepto, segunda mitad para AG+Skill Pack; temas de ejercicio desde `POC_SCENARIO_SPECS.md`, esqueletos importados desde `N8N_WORKFLOW_TEMPLATES.md`.
- **Aprendices buscan temas**: según departamento y nivel L, elegir desde `POC_SCENARIO_SPECS.md` o `04_Scenarios/LLM_APPS_CASE_INDEX.md`.
- **Aceptación**: tras cada nivel, pasar Stage Gate contra `01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`.

---

## ⭐ Cross-Topic Quick References: 5 Temas Centrales, Dónde Encontrar

Toda la metodología tiene 5 arterias principales atravesando todos los directorios. Cómo este directorio se conecta a cada una:

| Cross-Topic | Lugar principal | Cómo este directorio se conecta |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lectura tres motores** | Root [`README_ES.md`](../README_ES.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | **L2 Knowledge Codification enseña directamente los tres motores** — Antigravity / Codex / Claude Code son las herramientas de los aprendices L2; en clase, los tres motores pueden movilizarse para demos, encapsulación Skill, pruebas entre archivos |
| 🎓 **Fundamento académico (7 pilares)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **Arquitectura 5 capas L1-L5 según Capability Maturity (Rosemann/CMMI)**; regla anti-salto según Absorptive Capacity (Cohen & Levinthal 1990); siete principios diseño L4 Hermes según Sociotechnical & Knowledge Compounding |
| 📚 **Educación L1-L5** | [`../02_Course_Design/`](este directorio) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](L1_L5_COMPLETE_COURSE_PLAN.md) | **Este directorio ES el cuerpo de la educación L1-L5** — 5 currículos profundos independientes (L1 OPENWEBUI / L2 ANTIGRAVITY / L3 N8N / L4 HERMES / L5 CLAWTEAM) + COURSE_MODULE_MATRIX configuración ratio + POC_SCENARIO_SPECS 35 temas hands-on |
| 🔁 **Consultoría / 8 etapas + Closed-Loop Phase A→B→C** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Output en clase alimenta informe Phase B** (se convierte en el capítulo «observaciones de curso» de los 14 capítulos) + seguimiento radar trimestral Phase C; cada Stage Gate corresponde a Gates A/B/C del closed-loop |
| 📖 **Referencias / agradecimientos** | [`../90_References/`](../90_References/) §2 agradecimientos | **L1 → OpenWebUI** ｜ **L2 → Antigravity / Codex / Claude Code + agency-agents** ｜ **L3 → n8n + TigerAI-n8n-Skill-Pack** ｜ **L4 → nousresearch/hermes-agent** ｜ **L5 → HKUDS/ClawTeam**. Appreciation cards completas en [`../90_References/README.md`](../90_References/README.md) §2.1-2.3 |
