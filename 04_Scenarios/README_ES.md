# 04 Scenarios — Escenarios, Casos & Índice de Casos

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

> ⚠️ **Declaración importante de integridad académica / Important Academic Integrity Disclaimer**
>
> **Todos los 7 SAMPLE_CLIENT_CASE_*.md en este directorio (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education) y todos los personajes principales nombrados (p. ej., «Ming» en `00_Overview/CLIENT_JOURNEY_STORY.md`) son casos ficticios generados por IA, NO datos de clientes reales.**
>
> - **Uso**: demostración pedagógica, explicación metodológica, ejercicios de aplicación de los tableros Stage 1-8
> - **Límites**: todos los números (tiempo, ROI, person-month, presupuesto, KPI) son ejemplos ilustrativos, **NO deben usarse para marketing externo, compromisos contractuales o evidencia empírica académica**
> - **Nivel de evidence**: según [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 8.9, los casos de este directorio son **L0 (AI-Simulated Teaching Case)**, inferior al cuestionario de autoevaluación L1
> - **Casos longitudinales reales** se reemplazarán solo tras el estudio empírico 18-24 meses de [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md)

## 1. Propósito de Este Directorio

Este directorio es la **biblioteca de material y evidence** de toda la metodología. `01`-`03`, `05`, `06` son «método y proceso»; este directorio es «**proporcionar escenarios, casos y casos seleccionables reales para la implementación**».

El problema que resuelve: **el mayor obstáculo en la adopción IA no es «no sabemos hacer», es «no sabemos qué es posible, cómo lo hacen otros, cómo se verá después».** Este directorio proporciona cuatro tipos de material: (1) **Historias de escenarios** por rol/departamento (para que clientes se «reconozcan»), (2) **Estándares de escritura de casos y tablas de control** (casos coherentes), (3) **Casos demo completos para 7 sectores** (del cuestionario a la Roadmap), (4) **Índice de 150+ aplicaciones LLM reales** (búsqueda rápida por L-level y departamento).

Quién lo usa: consultores (escenarios Discovery, índice de casos para PoC), Sales (casos para justificar valor), instructores (casos como temas demo), clientes (casos completos para entender «cómo se ve después»).

## 2. Posición en la Metodología

| Eje | Mapeo |
| --- | --- |
| Flujo de servicio 3 fases | **Toda la duración** — Discovery usa escenarios, Build usa casos como temas, Deliver usa casos para justificar |
| Estructura de consultoría 8 etapas | Soporta principalmente **Stage 1 As-Is Snapshot (escenarios actuales), Stage 3 Best Practice Integration (benchmark industria)** |
| Madurez L1-L5 | Índice de casos mapea cada caso a un L-level |
| Engagement Lifecycle | Sales (Discovery reconocimiento) + Build (temas demo) |

## 3. Objetivos & Beneficios

| Objetivo | Beneficio |
| --- | --- |
| Proporcionar historias de escenarios por rol/departamento | Clientes pueden «reconocerse», Discovery enfoca más rápido |
| Estándares de escritura de casos y tablas de control | Consultores escriben casos estructuralmente coherentes y verificables |
| 7 casos demo completos por sector | Clientes ven el «cuadro completo de implementación»; nuevos consultores tienen modelos |
| Índice 150+ aplicaciones LLM (búsqueda doble eje) | Clientes/consultores pueden buscar por «L-level» o «departamento» al instante |
| Gestión de expectativa cross-level | Cuando cliente señala caso L5, con el índice señalarle «usted está en L2, debe ponerse al día antes» |

**Si se salta este directorio**: cliente no tiene idea «de qué es posible», selección PoC a ciegas, calidad de casos inconsistente, sin gestión de expectativa cross-level.

## 4. Flujo & Lógica

```text
Fase Discovery
   → CUSTOMER_SCENARIO_LIBRARY (escenarios por rol, reconocimiento cliente)
   → LLM_APPS_CASE_INDEX (por L-level + departamento, seleccionar casos «relevantes para cliente»)
   → Casos seleccionados → candidatos PoC

Fase curso / propuesta
   → SAMPLE_CLIENT_CASE_* (mostrar casos completos del mismo sector al cliente)
   → LLM_APPS_CASE_INDEX (temas demo, ejercicios en clase)

Consultor escribe nuevo caso
   → CASE_WRITING_STANDARD (estándar de escritura)
   → CASE_CONTROL_TABLES (tabla de control, copiar-pegar y llenar)
```

| Paso | Quién | Cuándo | Input | Output |
| --- | --- | --- | --- | --- |
| Reconocimiento cliente | Consultor | Discovery | Biblioteca de escenarios | Dolor reconocido por cliente |
| Seleccionar candidatos PoC | Consultor | Tras diagnóstico | L-level + departamento → índice | Lista de candidatos PoC |
| Mostrar casos completos al cliente | Sales / consultor | Propuesta | Sample case del mismo sector | Cliente entiende cuadro completo |
| Escribir nuevos casos | Consultor | Tras fin de proyecto | Estándar + tabla de control | Nuevo sample case |

> Lógica: las historias de escenarios son «**provocar resonancia**» (cliente dice «sí, así somos»); el índice de casos es «**selección rápida**» (por L-level/departamento búsqueda al instante); casos demo completos muestran «**cuadro completo**» (del cuestionario a Roadmap); estándares de escritura «**aseguran coherencia**» (calidad estable de nuevos casos).

## 5. Descripciones de Archivos

### Escenarios y Estándares

| Archivo | Uso |
| --- | --- |
| `CUSTOMER_SCENARIO_LIBRARY.md` | Historias por rol/departamento: CEO, COO, IT, RR.HH., Sales, Customer Service, Marketing, Operations, Finance, RR.HH., IT; cada historia contiene Before, Trigger, AI Flow, Systems, Output, KPI. |
| `CASE_WRITING_STANDARD.md` | Estándar de escritura, rige la escritura de L1-L5 Input / Process / Output / Evidence y entregables verificables. |
| `CASE_CONTROL_TABLES.md` | Tablas de control de casos, copiar-pegar para actividades de evaluación, L1-L5 IPOE, Evidence, Stage Gate, gobernanza riesgo, aceptación entregables. |
| `INDUSTRY_SCENARIOS.md` | Escenarios recomendados 5 sectores (Retail/Education/Logística/Software/Servicios profesionales), por sector: intro, baseline L1-L5, Top-10 escenarios, gobernanza riesgo, Quick Win 30 días, Anti-Patterns. |

### Casos Demo Completos (clientes con codenames)

| Archivo | Caso |
| --- | --- |
| `SAMPLE_CLIENT_CASE_MANUFACTURING.md` | Industria R&D-fabricación caso completo |
| `SAMPLE_CLIENT_CASE_HOSPITAL.md` | Hospital / institución médica (datos muy sensibles, full on-prem, revisión humana) |
| `SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md` | Agencia marketing (codename: Agencia M) |
| `SAMPLE_CLIENT_CASE_B2B_SALES.md` | Distribuidor equipo industrial B2B (codename: Equipo B), foco RFP, gobernanza CRM, L5 Pre-RFP Team |
| `SAMPLE_CLIENT_CASE_FINANCIAL.md` | Industria financiera (codename: Banco regional F), full on-prem, doble revisión |
| `SAMPLE_CLIENT_CASE_GOVERNMENT.md` | Agencia gubernamental (codename: Oficina digital de la ciudad G), full on-prem, triple revisión |
| `SAMPLE_CLIENT_CASE_EDUCATION.md` | Institución educativa (codename: Universidad tech E), Hybrid, ética académica |

> Cada caso sigue el flow completo: resultado cuestionario → juicio L-level → ratio de cursos → output en clase → análisis 8 etapas → resumen del informe de diagnóstico → Roadmap 30/60/90 → ROI → gobernanza riesgo.

### Implementación L5 e Índice de Casos

| Archivo | Uso |
| --- | --- |
| `CLAWTEAM_WALKTHROUGH.md` | Walkthrough completo de Agent Team inter-departamental con ClawTeam (HKUDS, MIT) (Manufacturing QA Team), incl. setup environment, cadena de tareas, Human Gate, mapeo Gate 5. |
| `LLM_APPS_CASE_INDEX.md` | **Índice de aplicaciones LLM (multi-fuentes)**. 150+ apps LLM reales, **dos ejes de búsqueda**: ① por L1-L5 / curso ② por departamento/proceso empresarial (Engineering/Finance/RR.HH./Sales/Marketing/R&D/Operations/Customer Service/Legal/Data/Design/Management). Fuentes: awesome-llm-apps (Apache-2.0), ai-engineering-hub (MIT). |

### `*_EN.md`

Versiones inglesas sibling de algunos archivos.

## 6. Mapeo a Otros Directorios

| Directorio | Relación con este directorio | Flujo de datos |
| --- | --- | --- |
| `01_Assessment` | L-level del diagnóstico determina qué casos seleccionar | `01` L-level → `04` filtro casos |
| `02_Course_Design` | Casos/índice PoC son fuente para demos y ejercicios en clase | `04` casos ↔ `02` temas curso |
| `03_Consulting_Report` | Stage 3 benchmark Best Practice industrial cita casos | `04` casos → `03` Stage 3 |
| `05_Sales` | Casos y escenarios completos son justificación del material Sales | `04` casos → `05` justificación |
| `00_Overview` | Historias de escenarios son material para la historia | `04` ↔ `00` |
| `90_References` | Citas de terceros para índice de casos (awesome-llm-apps / ai-engineering-hub) | `90` cita → `04` |

## 7. Escenarios de Uso Comunes

- **Reconocimiento Discovery**: tomar `CUSTOMER_SCENARIO_LIBRARY.md` correspondiente al rol del cliente, preguntar «¿qué historia se le parece?».
- **Seleccionar PoC**: tras diagnóstico L-level, en `LLM_APPS_CASE_INDEX.md` §3 por L-level o §4 por departamento, elegir 3-5 relevantes para el cliente.
- **Justificación propuesta**: mostrar `SAMPLE_CLIENT_CASE_MANUFACTURING.md` al cliente manufacturing, demostrar el cuadro de implementación completo.
- **Gestión de expectativa cross-level**: cliente señala caso L5 → con el índice señalarle su L-level y cursos prerrequisitos.
- **Escribir nuevo caso**: tras fin de proyecto, seguir `CASE_WRITING_STANDARD.md` + `CASE_CONTROL_TABLES.md` para escribirlo como nuevo sample case.

---

## ⭐ Cross-Topic Quick References: 5 Temas Centrales, Dónde Encontrar

Toda la metodología tiene 5 arterias principales atravesando todos los directorios. Cómo este directorio se conecta a cada una:

| Cross-Topic | Lugar principal | Cómo este directorio se conecta |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lectura tres motores** | Root [`README_ES.md`](../README_ES.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | Los casos pueden ejecutarse con workflows Tier 2 de Claude Code: `/simulate-engagement` simula mandato completo 6 semanas, `/parallel-perspectives` 6 vistas stakeholders, `/devil-pair-debate` debate los supuestos de valor |
| 🎓 **Fundamento académico (7 pilares)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | La argumentación ROI de los casos corresponde a **Real Options** (por qué Phase 1 con NPV ≈ 0 vale la inversión); el To-Be Design corresponde a **Task-Technology Fit** (qué tareas deben llegar a L4, cuáles deben quedarse en L2) |
| 📚 **Educación L1-L5** | [`../02_Course_Design/`](../02_Course_Design/) | LLM Apps Case Index clasificado por L-level, seleccionable directamente como PoC; `POC_SCENARIO_SPECS.md` + `N8N_WORKFLOW_TEMPLATES.md` transforman casos en temas hands-on de clase L3 |
| 🔁 **Consultoría / 8 etapas + Closed-Loop Phase A→B→C** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Los casos son el «material de reconocimiento» de Phase A Discovery** (hacer que cliente diga «sí, así somos»); benchmark Best Practice industrial mapeado a Stage 3; los 7 sample cases completos son los modelos del informe Phase B |
| 📖 **Referencias / agradecimientos** | [`../90_References/`](../90_References/) §2 agradecimientos | Fuentes de LLM Apps Case Index: `Shubhamsaboo/awesome-llm-apps` (Apache-2.0) + `patchy631/ai-engineering-hub` (MIT), appreciation cards completas en [`../90_References/README.md`](../90_References/README.md) §2.4; ClawTeam Walkthrough de `HKUDS/ClawTeam` (MIT) |
