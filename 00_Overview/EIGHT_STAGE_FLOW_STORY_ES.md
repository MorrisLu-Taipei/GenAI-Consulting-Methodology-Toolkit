# Flow consultoría 8-etapas: Historia de escenario completa y diseño de ciclo cerrado

> 🌐 Idioma: [繁體中文](EIGHT_STAGE_FLOW_STORY.md) ｜ [English](EIGHT_STAGE_FLOW_STORY_EN.md) ｜ [Deutsch](EIGHT_STAGE_FLOW_STORY_DE.md) ｜ [Français](EIGHT_STAGE_FLOW_STORY_FR.md) ｜ Español ｜ [日本語](EIGHT_STAGE_FLOW_STORY_JA.md) ｜ [한국어](EIGHT_STAGE_FLOW_STORY_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Última actualización: 2026-05-15

---

> **Lo que es esto**: La metodología consultoría de 8 etapas escrita como historia de ciclo cerrado completa, reproducible, debatible. Del intake del cuestionario al plan de implementación, cada paso tiene triggers claros, deliverables, firmas y relaciones de lock-in con el paso siguiente.
>
> **Lo que no es**: no es una narrativa marathon lineal de 6 semanas. Más bien **un modelo de contrato 3-fases + firma de cliente mid-engagement + loopback trimestral** proceso completo de management científico.

---

## 0. Mejoras sobre un walk-through lineal (3 mejores decisiones de diseño)

Intuición típica del usuario:
> Cuestionario + AI As-Is assessment → comparar a RM → maturity + casos benchmarking → score → mostrar reporte al cliente → cliente elige Ideal Practice → analizar qué se necesita → recomendaciones TO-BE → reporte consultoría → plan de implementación

**La dirección es correcta**. Tiger AI construye 3 mejoras sobre esto:

| # | Mejora | Por qué más fuerte |
| --- | --- | --- |
| **1** | **Tres fases de contrato** (Phase A Diagnostic / Phase B Strategy / Phase C Implementation), no marathon de 6 semanas | Cliente se compromete bajo-riesgo primero a Phase A, decide sobre B / C basado en resultados; consultor evita over-committing |
| **2** | **Fin de Phase A: un Mid-Engagement Assessment Report se firma como deliverable** antes de lanzar workshop Phase B Ideal Practice | Cliente impactado por celdas vacías del radar primero, luego elige Ideal — evita fantasía; mid-report es también deliverable standalone |
| **3** | **Cada trimestre, revisar el radar Reference Model** (continúa tras entrar Phase C Implementation) | No "hecho está bien" sino **"¿la estructura se volvió realmente más redonda?"** — este es el mecanismo de falsificación ciclo cerrado científico |

> **Por qué más fuerte que marathon lineal de 6 semanas**: lineal fuerza al cliente a comprometerse 6 semanas + 24 meses de una vez — barrera psicológica demasiado alta; 3 fases dividen decisiones, reducen riesgo, aumentan acceptance.

---

## 1. Vista general modelo contrato tres-fases

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  Phase A: Diagnostic           Phase B: Strategy           Phase C:        ║
║                                                            Implementation  ║
║  ─────────────                ─────────────              ─────────────     ║
║  2 semanas · NT$ 800K         4 semanas · NT$ 2M         24 meses · NT$ 7M║
║                                                                             ║
║  Stage 1 + 2 + 3 materiales  Stage 3 Ideal Practice      Stage 7 + 8        ║
║                                + Stage 4 + 5                                ║
║                                                            (radar revisit  ║
║                                                            trimestral)    ║
║                                                                             ║
║  Deliverable:                Deliverable:                Deliverable:      ║
║  Reporte mid-engagement      Reporte diagnóstico completo Transformation  ║
║  de assessment               + Ideal Practice            Roadmap +         ║
║  (client receipts)           definición (3-partes sign)  Change Mgmt +     ║
║                                                          Value Tracking +  ║
║                                                          Logs trimestrales║
╚═══════════════════════════════════════════════════════════════════════════╝
                ↑                       ↑                       ↑
            Gate A                  Gate B                   Gate C
        Cliente decide          Cliente decide           Cliente decide cada
        proceder a B            proceder a C             trimestre continuar
```

**Significado científico**: cada Gate es "un punto de salida donde el cliente puede bajarse" — el consultor **diseña esto solo con confianza** de que el deliverable de la fase previa es **lo suficientemente bueno para que el cliente quiera continuar**.

---

## 2. El protagonista: Client M

> ⚠️ **"Client M / MingChang Packaging" es empresa ficticia generada por IA**, NO cliente real. Todos los números scale, KPI, presupuesto y timeline son **solo ilustrativos**, para propósitos didácticos de metodología. Ver [`../04_Scenarios/README_EN.md`](../04_Scenarios/README_EN.md) para disclaimer completo de integridad académica.

- **Industria**: Packaging y testing de semiconductores (FATP)
- **Scale**: 700 empleados, NT$ 1.2B revenue anual
- **Trigger**: Tres competidores directos desplegaron inspección calidad IA y complaint Agents; órdenes trimestrales Cliente A cayeron 18%
- **Pain points**: Complaint response 5 días (industria 1 día); turnaround propuesta 4 días (industria 1.5 días); tasa defectos 3.2% (industria 1.8%)
- **Restricciones**: Tope presupuesto NT$ 8M; data process on-prem; IT 2 FTE, sin crecimiento
- **Roles**: CEO (Sponsor), COO, IT Director (AI Champion potencial), QC Head, Sales Head, CS Head, HR, Compliance

---

## 3. Phase A: Diagnostic (2 semanas, NT$ 800K)

### Trigger

CEO de M Company recibe email outreach Tiger AI + ve repo de metodología open-source en GitHub; secretario agenda intro de 30 min.

### Pre-Engagement: Quick Survey 10-preguntas (enviada semana siguiente)

CEO auto-completa la versión 10-preguntas de [`01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) (5 min).

**Resultado auto-scored**:

```
Radar 6-dimensiones:
  Uso herramientas         1 / 4 (algunos execs usan ChatGPT privado)
  Sedimentación conocim.   0 / 4 (sin Wiki, sin SOP)
  Automatización process   1 / 4 (Finance 1 flow Power Automate)
  Integración sistema      2 / 4 (ERP/CRM en silos)
  Aplicación Agent         0 / 4 (ninguna)
  Governance & ROI         1 / 4 (sin AI policy)
Total: 5 / 24 → L1 preliminar
```

CEO ve el radar → **primer shock** → acepta firmar contrato Phase A.

### Flow Phase A (Semana 1-2)

#### Semana 1 ── Stage 1 As-Is Snapshot: Escuchar, Observar, Sin Comentario

| Día | Acción | Tool | Output |
| --- | --- | --- | --- |
| Día 1-2 | Entrevistas exec (CEO/COO/CIO × 60 min) + entrevistas dept head (QC/Sales/CS/IT/HR × 90 min) | Tool 1.1 (40-Q bank) | Grabaciones + resúmenes |
| Día 3 | Entrevistas operadores (Line/Sales/CS × 3 cada uno × 30 min) | Tool 1.1 Section C | Resúmenes |
| Día 4 | AI Usage Inventory + Systems Inventory | Tool 1.2 + 1.3 | Shadow IT risk map + system map |
| Día 5 | Walkthrough de 3 key processes + dibujar Swimlanes | Tool 1.4 | 3 As-Is Process Maps |

**Fin Semana 1**: Consultor dice al cliente "ahora sabemos qué hace su empresa." **Sin comentario, sin recomendación.**

#### Semana 2 ── Stage 2 Reference Model Alignment + Stage 3 Material Prep

| Día | Acción | Tool | Output |
| --- | --- | --- | --- |
| Día 6 | Elegir Reference Model: SCOR + APQC + Tiger AI L1-L5 | Tool 2.1 | RM selection rationale |
| Día 7-8 | Mapping Worksheet: localizar As-Is en celdas RM | Tool 2.2 | Tabla mapping |
| Día 9 | Standard Capability Gap Checklist + dual radar | Tool 2.3 + 2.4 | Dos radares (APQC + Tiger AI) |
| Día 10 | Prep caso benchmark (elegir semiconductor de 5 stubs + 2 casos misma industria) | Tool 3.1 + 3.3 | 3 Best-Practice Profiles |

> **Disciplina Phase A**: Día 10 consultor **NO corre AÚN workshop Ideal Practice**. Solo materiales — usados próxima fase.

### Phase A Deliverable: Mid-Engagement Assessment Report (client receipts)

**Día 11-12 escribir reporte → Día 13-14 client review → Día 14 closeout meeting**

Reporte mid-engagement (10-15 páginas):

1. **Executive Summary**: "Por estándares internacionales, su empresa muestra gaps estructurales en SCOR Make/Deliver, APQC 11.x Knowledge, Tiger AI L1-L3."
2. **As-Is Snapshot**: resúmenes entrevistas + system map + 3 Swimlanes
3. **Reference Model Mapping**: Standard Capability Gap Checklist
4. **Dual radar**: APQC + Tiger AI L1-L5 (punteado = benchmark, sólido = empresa)
5. **Materiales Industry Best Practice**: 3 Benchmark Profiles misma industria (solo materiales — **aún sin conclusiones**)
6. **Recomendación próxima fase**: Phase B Ideal Practice Workshop (medio día) + análisis Stage 4-5

### Gate A: Cliente Decide Si Proceder a Phase B

**Lo que pasa en closeout meeting**:

- CEO ve radar: "Pensé que íbamos bien — bajo el estándar estas celdas son 0?" → **segundo shock**
- COO hojea Swimlanes: "Nuestro proceso de complaint realmente tiene estos huecos..." → pain points concretizados
- IT Director ve gasto mensual shadow IT: "ChatGPT privado quemando NT$ 24,000 con data leaking..." → riesgo concretizado

**90% de clientes firman Phase B**. Porque:

- Gaps radar no son dichos-por-consultor — dichos por estándar internacional → **objetivo**
- Pain está en grabaciones entrevistas empleados → **verificable**
- Firmas misma industria ya lo hicieron → **alcanzable**

> **La meta de diseño de Phase A ES este shock**: cliente **ve el gap él mismo**, no dicho por consultor.

---

## 4. Phase B: Strategy (4 semanas, NT$ 2M)

### Semana 3 ── Stage 3 Ideal Practice Co-Creation Workshop (medio día)

**Día 15 mañana** ─ Tool 3.6 Co-Creation Workshop

| Paso | Acción | Tiempo | Output |
| --- | --- | --- | --- |
| 1. Material display | Consultor **solo muestra, no recomienda** Tool 3.1/3.3/3.4/2.7 arquitectura 4-capas | 30 min | Materiales compartidos |
| 2. Voting independiente | Cada persona **independientemente** escribe en sticky notes "qué quiero que seamos en 12 meses" | 45 min | N sticky notes |
| 3. Consenso colectivo | Postear en arquitectura 4-capas, encontrar consenso / divergencia | 60 min | Draft v1 Ideal Practice |
| 4. Reality check | Consultor interviene primero, usando Tool 6.3 para challenge feasibility | 45 min | v2 Ideal Practice |
| 5. Define table | Escribir v2 como "Ideal Practice Definition Table" | 30 min | Definition table versión-firmada |
| 6. **Firma 3-partes** | CEO + Sponsor + AI Champion | 15 min | Documento público, auditable |

**Ideal Practice Definition Table firmada de M Company (extracto)**:

| # | Capability | RM Category | Target 12-meses | Criterios evidence |
| --- | --- | --- | --- | --- |
| 1 | Complaint response | APQC 4.4 + Tiger AI L3 | 90% en 1hr + 24hr human reply | n8n + tasa Reviewer sign-off ≥ 95% |
| 2 | Sedimentación conocimiento | APQC 11.x + Tiger AI L2 | ≥ 20 Skills añadidos mensual | Skill Library Git + Owner + IPOE |
| 3 | Process root cause | SCOR Make + Tiger AI L4 | Anomalía → hipótesis ≤ 1hr | Hermes Agent + 5 tasks Reviewer pass |

> **Esta tabla es el ancla de todo el engagement**. Todos los cálculos Stage 4-8 subsecuentes están basados en ella; cliente no puede negar sus propios targets firmados.

### Semana 3-4 ── Stage 4 Gap Analysis + Stage 5 Problem Definition

#### Stage 4: Gap = (Client Ideal − Client As-Is)

| Día | Acción | Tool | Output |
| --- | --- | --- | --- |
| Día 16-17 | Clasificación M/B/R + Impact × Effort | Tool 4.1 + 4.2 | Gap matrix |
| Día 18 | Prioritization Worksheet | Tool 4.3 | Ranking prioridad |

#### Stage 5: Convergencia 80/20 a Root Cause

| Día | Acción | Tool | Output |
| --- | --- | --- | --- |
| Día 19 | Convergencia 80/20 + 5 Whys | Tool 5.1 + 5.2 | Lista core lesion |
| Día 20-21 | Executive Problem Statement | Tool 5.3 + 5.4 | Definición una-frase |

**Executive Problem Statement de M Company**:

> M Company carece del rol, herramienta e incentivo para "knowledge asset-ización." 80% de gaps (complaints lentos / quotes lentos / sin sedimentación conocimiento / root cause lento) provienen de "lo mismo hecho repetidamente, nadie sedimenta, nadie reutiliza."

### Semana 4 ── Stage 6 Phased Goals + Stage 7 To-Be Design

#### Stage 6: Descomponer Ideal en pasos absorbibles

| Día | Acción | Tool | Output |
| --- | --- | --- | --- |
| Día 22 | Ultimate Ideal → descomposición Phase 1/2/3 | Tool 6.1 | Tabla descomposición |
| Día 23 | Evaluación absorción organizacional (6 dimensiones) | Tool 6.3 | Absorption score |
| Día 24 | Stage Gate Criteria | Tool 6.2 | Checklists L1-L5 Gate |

> **El assessment absorción de M Company encuentra que IT solo tiene 2 FTE; Phase 2 necesita +0.5**. Decisión: extender Phase 2 de 6 → 9 meses. **Este ajuste viene del cliente mirando los datos él mismo, no de recomendación consultor**.

#### Stage 7: Un To-Be Operating Model por Phase

| Día | Acción | Tool | Output |
| --- | --- | --- | --- |
| Día 25-26 | Phased To-Be Operating Models (3 diagramas) | Tool 7.1 | 3 diagramas |
| Día 27 | Human-AI Collaboration + HITL nodes | Tool 7.2 | Split por-proceso |
| Día 28 | Skill/Workflow/Agent Map + Integration Architecture | Tool 7.3-7.6 | 3 maps + Variant B Hybrid |

### Phase B Deliverable: Reporte diagnóstico completo + Ideal Practice Definition Table

**Día 29-30 escribir reporte → Día 31-32 client review → Día 32 closeout meeting**

Reporte diagnóstico completo (30-50 páginas) por estructura 14-secciones [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md).

### Gate B: Cliente Decide Si Proceder a Phase C

**95% de clientes firman Phase C**. Porque:

- Ideal Practice fue **firmada por ellos** → innegable
- Gap se calcula por sustracción → **verificable**
- Phase 1/2/3 ajusta absorción organizacional → **alcanzable**

---

## 5. Phase C: Implementation (24 meses, NT$ 7M)

### Stage 8 Implementation & Change

**Primer mes (Mes 1)**

| Día | Acción | Tool | Output |
| --- | --- | --- | --- |
| Día 33 | Transformation Roadmap (24 mo / 6 trimestres) | Tool 8.1 | Roadmap |
| Día 34 | Change Management Plan + resistance Playbook | Tool 8.2 | Change plan |
| Día 35 | RACI + Permission Matrix + Audit Log | Tool 8.3 + 8.4 + 8.7 | Docs gobernanza |
| Día 36 | Value Tracking Matrix (5 dimensiones) | Tool 8.5 | Dashboard spec |
| Día 37 | Risk Register (incorporando case Failures) | Tool 8.6 | Risk log |
| Día 38 | AI Ethics Checklist | Tool 8.8 | Signed ethics |
| Día 39 | SOW + Phase 1 kickoff | — | Phase 1 lanzada |

### Phase 1 (Meses 1-6): Foundation

- L1 OpenWebUI pan-empresa live
- 5 Skills core publicados
- AI policy firmada por > 90%
- Prompt Library ≥ 30 entradas

**Fin Mes 6 → L1 Gate acceptance + revisit Stage 2 radar**:

```
APQC 11.x Knowledge:  0 → 2 (Skill library iniciando)
Tiger AI L1:          0 → 4 (OpenWebUI completo + 92% policy firmada)
Tiger AI L2:          0 → 2 (5 Skills)
```

> El radar **realmente es más redondo**. Cliente se emociona: "Entonces esto es management científico."

### Phase 2 (Meses 6-15): Optimization

- L2 Skill Library ≥ 15 entradas
- L3 n8n Workflow ≥ 3 live
- HITL nodes plenamente en lugar

**Fin Mes 15 → L2/L3 Gate + radar revisit**:

```
APQC 4.0 Deliver: 1 → 3 (complaint response 5 días → 1 día) ✓ Ideal alcanzado
APQC 11.x:        2 → 3 (sedimentación conocimiento estable) ✓ Ideal alcanzado
Tiger AI L3:      0 → 2 (n8n PoC live)
```

### Phase 3 (Meses 15-24): Excellence

- L4 Hermes Agent pasa 4A-4E
- L5 ClawTeam cross-dept 1 ensayo exitoso

**Fin Mes 24 → L4/L5 Gate + radar final**:

```
SCOR Make + Tiger AI L4: 0 → 3 (Hermes Agent pasa) ✓ Ideal alcanzado
Tiger AI L5:             0 → 2 (ClawTeam cross-dept ensayo)
```

### Gate C Trimestral: Cliente Puede Decidir Cada Trimestre

Cada trimestre debe:

1. Quarter Gate acceptance (por Tool 6.2 checklist)
2. Revisit Stage 2 radar (cuantificar mejora)
3. Value tracking matrix review 5-dimensiones
4. Cliente decide si avanzar, ajustar o pausar próximo trimestre

> Tras 24 meses: M Company complaint response 1 día, tasa defectos 2.0%, churn cliente cero, Stage 2 radar **cambia de línea zigzagueante a casi redondo**.

---

## 6. Diagrama completo de ciclo cerrado

```
                          ┌──────────────────┐
                    ┌────►│ Phase A Diag 2W   │
                    │     │ Stage 1 + 2 + 3   │
                    │     │   prep materiales │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Mid Report        │ ← Phase A Deliverable
                    │     │ (client receipts) │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate A
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase B Strat 4W  │
                    │     │ Stage 3 Ideal     │
                    │     │ + Stage 4 + 5     │
                    │     │ + Stage 6 + 7     │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Reporte completo  │ ← Phase B Deliverable
                    │     │ + Ideal Practice  │
                    │     │ (sign 3-partes)   │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate B
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase C Impl 24M  │
                    │     │ Stage 8           │
                    │     │ Transformation +  │
                    │     │ Change + Value    │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase 1/2/3       │
                    │     │ Stage Gate accept │
                    │     └────────┬─────────┘
                    │              │
                    │     Gate C trimestral
                    │              │
                    │     ┌────────▼─────────┐
                    └─────┤ Revisit Stage 2 │
                          │ Radar (más rondo?)│
                          └──────────────────┘
                                  
                          Esta línea de feedback
                          es el mecanismo core
                          de falsificación del
                          ciclo cerrado científico
```

---

## 7. Por qué este flow resiste debate cliente

Para cada challenge posible, la ubicación de respuesta:

| Challenge | Ubicación | Evidence |
| --- | --- | --- |
| "¿Cómo saben que estamos en L1?" | Phase A mid-report §2 radar | Survey 10-Q + grabaciones + system inventory |
| "¿Por qué estas celdas son 0?" | Phase A §3 RM Mapping | Estándares públicos APQC / Tiger AI |
| "¿Quién fijó el target?" | Phase B §5 Ideal Practice table | **Cliente mismo firmó, firma 3-partes** |
| "¿Por qué el gap es tan grande?" | Phase B §6 Gap Analysis | Fórmula Gap = (tu Ideal firmado − tu As-Is) |
| "¿Por qué customer service antes que sales?" | Phase B §6.2 | Matrix Impact × Effort |
| "¿Por qué 24 meses?" | Phase B §8 + Tool 6.3 | Case Benchmark + Organizational Absorption |
| "¿Y si no funciona?" | Phase C §13 Risk Register | Trigger + Owner + Mitigation |
| "¿Cómo prueban que mejoró?" | Quarterly Gate C | Stage 2 radar + Value Tracking 5 dimensiones |
| "Último consultor dijo L3, ustedes dicen L2 — ¿quién tiene razón?" | Escala pública 0-4 + evidence | Cualquier tercero puede verificar independientemente |

---

## 8. Mapping al flow original del usuario

| Paso usuario | Phase | Stage | Mejora |
| --- | --- | --- | --- |
| 1. Cuestionario + AI As-Is | Phase A W1 | Stage 1 | + 10-Q quick screen como pre-engagement |
| 2. Comparar a RM | Phase A W2 | Stage 2 | Arquitectura 4-capas + dual radar |
| 3. Maturity + casos benchmarking → score | Phase A fin W2 | Stage 3 materiales | Casos deben ser Benchmark-grade (9 campos) |
| 4. **Cliente ve reporte assessment** | **Phase A Deliverable** | — | **Nuevo: mid-report como deliverable standalone + client receipt** |
| 5. Cliente elige Ideal Practice | Phase B W3 | Stage 3 Tool 3.6 | **Cliente firma, no consultor prescribe** |
| 6. Analizar qué se necesita | Phase B W3-W4 | Stage 4 + 5 | Gap = Ideal − As-Is, convergencia 80/20 |
| 7. Recomendaciones TO-BE | Phase B W4 | Stage 6 + 7 | Phased + assessment Organizational Absorption |
| 8. Reporte consultoría | Phase B Deliverable | — | Reporte completo 14-secciones + Ideal Practice firmada |
| 9. Plan implementación | Phase C kickoff | Stage 8 | Change Mgmt + Value Tracking + Audit |
| **(falta)** | **Revisit trimestral** | — | **Nuevo: cada trimestre revisit Stage 2 radar (ciclo cerrado científico)** |

---

## 9. Relación a otros documentos

| Documento | Relación a este |
| --- | --- |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 | Provee definiciones 8-stages y flow de datos; este doc es la narrativa completa del proceso |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Provee argumento científico "por qué diseñado así"; este doc es "cómo realmente corre" |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | Provee tablas de herramientas por-stage |
| [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) | Provee estructura 14-secciones del Phase B Deliverable |
| [`../04_Scenarios/`](../04_Scenarios/) | Provee casos Benchmark-grade para Phase A |
| [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) | Provee SOP engagement / pricing / delivery |

---

## 10. Cierre: Por qué el ciclo cerrado es ciencia

Este flow **no es marathon lineal** sino **ciclo cerrado con feedback**:

- **Cada Gate es punto de salida** → consultor **tiene confianza** para diseñar así (el deliverable previo debe ser suficientemente bueno para que cliente quiera continuar)
- **Cada Deliverable tiene firma cliente** → razonamiento subsecuente no puede negarse
- **Cada trimestre revisit Stage 2 radar** → estructura realmente volviéndose más redonda = éxito, no "PoC hecho = éxito"

**Esto es management científico**:

- Punto de partida objetivo (estándar internacional + firma cliente)
- Proceso verificable (cada Stage Gate Criteria)
- Punto final falsificable (dual radar before/after + Value Tracking 5 dimensiones)

Si alguien dice "metodología Tiger AI no funciona", deben **challenge**:

- ¿APQC PCF es incorrecto?
- ¿Escuela Rosemann BPM es incorrecta?
- ¿No cuenta la propia Ideal Practice firmada del cliente?
- ¿No cuenta nuestro loopback radar trimestral?

**Difícil de hacer.** Por eso invertimos en este diseño ciclo cerrado.

---

Licencia & Citación

Este documento es Apache License 2.0; puede usarse, modificarse, comercializarse, siempre que se preserve la atribución [`../NOTICE`](../NOTICE).
