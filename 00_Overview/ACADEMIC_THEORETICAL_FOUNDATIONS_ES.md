# Fundaciones teóricas académicas: Los siete pilares teóricos de la metodología Tiger AI

> 🌐 Idioma: [繁體中文](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [English](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) ｜ [Deutsch](ACADEMIC_THEORETICAL_FOUNDATIONS_DE.md) ｜ [Français](ACADEMIC_THEORETICAL_FOUNDATIONS_FR.md) ｜ Español ｜ [日本語](ACADEMIC_THEORETICAL_FOUNDATIONS_JA.md) ｜ [한국어](ACADEMIC_THEORETICAL_FOUNDATIONS_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Última actualización: 2026-05-16

---

> **Propósito**: Consolidar las fundaciones teóricas académicas de la metodología Tiger AI dispersas en archivos en **un documento autoritativo**. Cuando cualquier académico / regulatorio / consultor serio pregunta "cuál es la base teórica", este documento es la respuesta.
>
> **Afirmación core**: La metodología Tiger AI no es meramente práctica de consultoría sino una **integración ingenieril de siete teorías**.

---

## 1. Vista general del mapa teórico

| Teoría | Fundador / Referencia clásica | Problema core resuelto | Mapping Tiger AI |
| --- | --- | --- | --- |
| **Capability Maturity & BPM Maturity** | Paulk et al. (1993) CMMI; Rosemann & de Bruin (2005) | ¿Cómo scorear estructuralmente la capacidad organizacional? | L1-L5 + scoring Stage 2 |
| **Absorptive Capacity** | Cohen & Levinthal (1990) | ¿Por qué las organizaciones difieren tanto en **absorber** nueva capacidad? | Tool 6.3 Organizational Absorption Assessment |
| **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | ¿Qué tareas se adaptan / no se adaptan a IA? | Stage 7 To-Be Design (no todo dept debe alcanzar L5) |
| **Dynamic Capabilities** | Teece et al. (1997); Teece (2007) | ¿Cómo se **adapta rápidamente una organización al cambio externo**? | Stage 7 + Stage 8 (de automatización estática a capacidad dinámica) |
| **Sociotechnical Systems & Trust in AI** | Bostrom & Heinen (1977); Dietvorst et al. (2015); Glikson & Woolley (2020) | ¿Por qué la colaboración humano-IA es difícil? Algorithm aversion / complacency | Stage 8 Change Management + HITL |
| **Real Options Theory** | Dixit & Pindyck (1994); McGrath (1997) | ¿Cómo valorar inversión estratégica IA de alta incertidumbre? | Stage 8 §13 Value Tracking + ROI |
| **AI-Native Living Book / Executable Knowledge Artifact** | Knuth (1984); Anderson et al. (1995); este autor (2026) | ¿Puede la metodología misma ser ejecutable por IA? | AGENTS.md + AI_NATIVE_LIVING_BOOK |

---

## 2. Capability Maturity & BPM Maturity

### 2.1 Resumen de teoría

- **CMMI**: Paulk et al. (1993) en SEI definieron capacidad organizacional de 5 niveles (Initial / Repeatable / Defined / Managed / Optimizing)
- **BPM Maturity Model**: Rosemann & de Bruin (2005, QUT) extendieron madurez a Business Process Management, añadiendo 6 enablers: Process Awareness / Alignment / Methods / IT / People / Culture

### 2.2 Contribución a Tiger AI

- **L1-L5 dos ejes** heredan la lógica "Process Awareness → Optimization" de BPM Maturity, añadiendo la doble estructura esencial de era GenAI "**eje scale + eje AI Autonomy**"
- **Escala 0-4 + anclas conductuales BARS** derivan de esta escuela
- **Stage Gate Criteria** = "Process Areas" de CMMI + acceptance de fase

### 2.3 Archivos mapeados

- [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §3.0 historia dos-ejes
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) definiciones L1-L5
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) anclas conductuales

---

## 3. Absorptive Capacity

### 3.1 Resumen de teoría

- **Cohen & Levinthal (1990)** en *Administrative Science Quarterly*: la "**capacidad de una organización para identificar, asimilar y aplicar conocimiento externo**" determina su capacidad de innovación
- Elementos core: **Prior Knowledge + Internal Knowledge Flow**
- Zahra & George (2002) dividen más en 4 dimensiones: Acquisition / Assimilation / Transformation / Exploitation

### 3.2 Contribución a Tiger AI

- Explica por qué **la misma oportunidad IA yielda resultados radicalmente diferentes** entre empresas — la diferencia es absorptive capacity
- Tool 6.3 Organizational Absorption Assessment mapea directamente a esta teoría
- Refuerza "**por qué los niveles no pueden saltarse**": saltar L1-L3 → absorptive capacity insuficiente → L4-L5 fallará (ver [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) §2)

### 3.3 Mejora específica a Tool 6.3

Original Tool 6.3 6 dimensiones (Budget / Champion / IT FTE / Governance / Literacy / Change capacity) **añaden 2 nuevas dimensiones**:

| Nueva dimensión | Preguntas de assessment | Score |
| --- | --- | --- |
| **Prior Knowledge** | ¿La empresa tiene: (a) experiencia pasada BPM / Lean / Six Sigma? (b) intentos pasados IA / ML / RPA? (c) capacidad dev software interna? | 0-4 |
| **Internal Knowledge Flow** | Entre departamentos: (a) reviews inter-dept rutinarios? (b) plataforma de documentos compartida? (c) sistema mentor / instructor interno? | 0-4 |

→ Empresas High Prior Knowledge + High Knowledge Flow pueden manejar Phase 1/2/3 más agresivas; inversamente, deben extender timelines.

### 3.4 Referencias

- Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128-152.
- Zahra, S. A., & George, G. (2002). Absorptive capacity: A review, reconceptualization, and extension. *Academy of Management Review*, 27(2), 185-203.

---

## 4. Task-Technology Fit (TTF)

### 4.1 Resumen de teoría

- **Goodhue & Thompson (1995)** en *MIS Quarterly*: el grado en que la tecnología mejora la performance depende del fit **"demanda de tarea ↔ capacidad tech"**
- Clasificación de tarea: **Routine (repetitiva, predecible) vs Non-routine (judgment-heavy, creativa)**

### 4.2 Contribución a Tiger AI

**No todo departamento debe alcanzar L5**. Determinar el endpoint L-level apropiado de cada dept por características de tarea:

| Tipo de tarea | Endpoint apropiado | Rationale |
| --- | --- | --- |
| Highly Routine (CS FAQ, clasificación de factura) | L3-L4 | Alto fit IA; bajo costo HITL |
| Medium Routine + juicio parcial (propuestas de ventas, anomalías de fin de mes) | L2-L3 + HITL | IA borronea + humano confirma; balancea eficiencia y riesgo |
| Highly Non-routine (evaluación M&A, decisiones estratégicas) | L1-L2 (asistente personal) | IA asiste, humanos lideran; empujar L4-L5 daña calidad de juicio |
| Highly compliance-sensitive (legal, diagnóstico médico) | L2-L3 + strong HITL | Riesgo regulatorio demasiado alto; L4-L5 inapropiado |

### 4.3 Archivos / Tools mapeados

- Stage 7 Tool 7.2 Human-AI Collaboration → matriz TTF decide involvement IA por proceso
- Añadir **TTF Assessment Worksheet** a Tool 6.3 → scorear TTF por dept, determinar L-level Ideal

### 4.4 Referencias

- Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. *MIS Quarterly*, 19(2), 213-236.
- Zigurs, I., & Buckland, B. K. (1998). A theory of task/technology fit and group support systems effectiveness. *MIS Quarterly*, 22(3), 313-334.

---

## 5. Dynamic Capabilities

### 5.1 Resumen de teoría

- **Teece, Pisano & Shuen (1997)** en *Strategic Management Journal*: la ventaja competitiva proviene de "**integrar, construir, reconfigurar recursos internos y externos**"
- **Teece (2007)** descompone en tres micro-foundations:
  1. **Sensing**: identificar oportunidades y amenazas
  2. **Seizing**: decisión y asignación de recursos
  3. **Transforming**: reconfiguración organizacional para aprovechar oportunidades

### 5.2 Contribución a Tiger AI

**De automatización estática → capacidad adaptativa dinámica**. Tiger AI no solo IA-iza procesos APQC existentes sino **construye a clientes la nueva capacidad de adaptarse continuamente al cambio externo**:

| Dynamic Capability | Mapping Tiger AI |
| --- | --- |
| **Sensing** | L3 Workflow + L4 Agent monitorean continuamente señales mercado / cliente / proceso |
| **Seizing** | Descomposición Phase 1/2/3 = conversión de señales sensadas en decisiones de inversión concretas |
| **Transforming** | L5 Multi-Agent Organization + radar trimestral Gate C = reconfiguración org continua |

### 5.3 Mejora específica a Stage 7

Añadir **Dynamic Capability Worksheet** a Stage 7 To-Be Design:

```
Por Teece (2007) tres micro-foundations, cada To-Be design debe responder:

1. Sensing: ¿Qué señal externa ayuda este diseño IA a la empresa a "sense"?
   Ej. complaint Agent monitorea tendencias satisfacción cliente
2. Seizing: ¿Qué tan rápido puede la empresa "seize" cuando aparecen señales?
   Ej. Quick Win complaint response 5d → 1d comprime ventana de pérdida cliente
3. Transforming: ¿Cómo este IA permite "self-reconfiguration" organizacional?
   Ej. L5 ClawTeam inter-dept = org ya no depende de personal senior específico
```

→ Un To-Be que no responde estos 3 es solo "automatizar status quo", no transformación real.

### 5.4 Referencias

- Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal*, 18(7), 509-533.
- Teece, D. J. (2007). Explicating dynamic capabilities. *Strategic Management Journal*, 28(13), 1319-1350.

---

## 6. Sociotechnical Systems & Trust in AI

### 6.1 Resumen de teoría

- **Sociotechnical Systems Theory** (Bostrom & Heinen, 1977): performance organizacional = output joint de **sistema social + sistema técnico**; no puede optimizarse uno solo
- **Algorithm Aversion**: Dietvorst, Simmons & Massey (2015) en *JEP*: la gente **prefiere juicio humano peor sobre algoritmos después de ver al algoritmo errar**, incluso sabiendo que el algoritmo es más preciso
- **Automation Complacency**: Parasuraman & Manzey (2010): sobre-confianza en automation causa pérdida de vigilancia, llevando a incidentes mayores
- **Trust in AI**: Glikson & Woolley (2020) integran trust cognitivo + emocional

### 6.2 Contribución a Tiger AI

El verdadero challenge de la colaboración humano-IA no es solo "miedo a reemplazo", sino también:

1. **Algorithm Aversion**: después del primer error IA, personal colectivamente lo rechaza → común tras lanzamiento L3-L4
2. **Automation Complacency**: personal deja de revisar → HITL falla → incidentes mayores
3. **Ambigüedad de accountability**: ¿quién es responsable cuando IA erra? Personal teme culpa → gap de seguridad psicológica
4. **Reshape de identidad profesional**: de "Doer" a "Reviewer" → carga cognitiva y sentido de logro se desplazan

### 6.3 Mejora a Stage 8 Change Management

Añadir 2 nuevos tipos de resistencia a Tool 8.2:

| Tipo de resistencia | Señal típica | Handling |
| --- | --- | --- |
| **Algorithm Aversion** | Rechazo colectivo después de un error IA | Transparencia sobre tasas de error (humano vs IA) + trust-building gradual (comenzar con escenarios low-risk) |
| **Automation Complacency** | Personal aprueba sin revisar | Random sampling obligatorio en Reviewer Workflow + re-entrenamiento después de errores detectados |

### 6.4 Mejora a HITL Design (Tool 7.2)

Añadir **columnas seguridad psicológica y accountability**:

| Proceso | HITL Node | **Accountability Statement** | **Seguridad psicológica** |
| --- | --- | --- | --- |
| CS reply | 100% revisión humana antes de envío | Responsabilidad IA draft = AI Champion; responsabilidad reply final = personal CS | Personal tiene derecho a "rechazar sin revisión si IA es incorrecto" sin culpa |
| Process root cause | 100% revisión humana antes de acción | Responsabilidad hipótesis IA = desarrollador Agent; responsabilidad acción = manager de proceso | Manager tiene SOP formal para "rechazar sugerencia IA" |

### 6.5 Referencias

- Bostrom, R. P., & Heinen, J. S. (1977). MIS problems and failures: A socio-technical perspective. *MIS Quarterly*, 1(3), 17-32.
- Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion. *JEP: General*, 144(1), 114-126.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3), 381-410.
- Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence. *Academy of Management Annals*, 14(2), 627-660.
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *ASQ*, 44(2), 350-383.

---

## 7. Real Options Theory

### 7.1 Resumen de teoría

- **Dixit & Pindyck (1994)** en *Investment Under Uncertainty*: valor de inversión altamente incierta = valor de ejecución inmediata + valor de "**future optionality**"
- **McGrath (1997)** aplicado a estrategia: "**la inversión de hoy preserva el derecho a expandir en el futuro**"
- Contrarresta subestimación NPV bajo incertidumbre: NPV asume certeza, pero flexibilidad gerencial tiene alto valor bajo incertidumbre

### 7.2 Contribución a Tiger AI

La inversión IA altamente incierta L4-L5 es **necesariamente subestimada por NPV / IRR tradicional** (porque cash flows 18-24 meses son inciertos). Real Options provee mejor framing:

| Inversión | Vista NPV (subestima) | Vista Real Options (justificada) |
| --- | --- | --- |
| Phase 1 Foundation (NT$ 2.8M) | Cash flow unclear → NPV ≈ 0 | Comprando la "**opción de expandir L4-L5 rápidamente en futuro a costo más bajo**", vale mucho más que NT$ 2.8M |
| L1 Chat AI pan-empresa | ROI corto-plazo unclear | Literacy IA empleados = **activo foundational para todas futuras aplicaciones IA** |
| L2 Skill Library | ROI invisible | Codificación de conocimiento = opción de la empresa de "**enchufar múltiples aplicaciones IA simultáneamente**" en futuro |
| L4 Hermes Agent Pilot | ¿Vale un Agent? | Pilot = aprender L4 = opción a L5 ClawTeam |

### 7.3 Real Options Valuation (Black-Scholes simplificado)

Para inversiones L4-L5, estimar vía:

```
Option Value = max(0, future_payoff - exercise_cost)

Donde:
  future_payoff = ingreso de ejercer opción (ej. expandir a L5)
  exercise_cost = costo al ejercer (ej. Phase 3 inversión)
  volatility (σ) = incertidumbre mercado / tech
  time-to-expiration = ventana de oportunidad
```

⚠️ No necesidad de Black-Scholes exacto; **argumento nivel narrativo es suficiente para convencer CFO** de justificar inversión "ROI corto-plazo invisible pero largo-plazo valiosa".

### 7.4 Mejora a Stage 8 §13 Value Tracking

Original 5 dimensiones (Time / Quality / Scale / Risk / Assets), **añadir 6ª dimensión**:

| Dimensión | Contenido |
| --- | --- |
| **Strategic Options** | ¿Qué "**future exercise right**" preservó esta inversión? Ej. L1 foundation → puede expandir L4 rápido en futuro; L2 Skill Library → puede enchufar cualquier futuro Agent; L3 Workflow → puede integrar cualquier nuevo sistema |

### 7.5 Referencias

- Dixit, A. K., & Pindyck, R. S. (1994). *Investment Under Uncertainty*. Princeton University Press.
- McGrath, R. G. (1997). A real options logic for initiating technology positioning investments. *Academy of Management Review*, 22(4), 974-996.
- Trigeorgis, L. (1996). *Real Options*. MIT Press.

---

## 8. AI-Native Living Book como Executable Knowledge Artifact

### 8.1 Resumen de teoría

- **Literate Programming**: Knuth (1984) argumentó que código y docs deben integrarse en un solo documento "humano-legible + máquina-ejecutable"
- **Intelligent Tutoring Systems (ITS)**: Anderson et al. (1995) diseñaron IA como sistemas de tutoring personalizados
- **Open Educational Resources (OER) + IA**: tendencia contemporánea combinando materiales open con IA como sistemas de conocimiento interactivos

### 8.2 Contribución a Tiger AI

Esta metodología misma es un **caso práctico** de esta teoría:

- repo + AGENTS.md = **executable knowledge artifact**
- AI co-reading tutor = **adaptive ITS** aplicado a educación profesional adulta
- Cliente conversando con metodología = OER customizado

Ver [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) para discusión completa.

### 8.3 Referencias

- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society*. Harvard University Press.

---

## 9. Cómo cooperan las 7 teorías: Modelo integrado de Tiger AI

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   [Capability Maturity]  ────►  scoring estructurado L1-L5        │
│         │                                                        │
│         ▼                                                        │
│   [Absorptive Capacity] ────►   por qué empresas difieren en    │
│         │                       absorber                         │
│         ▼                                                        │
│   [Task-Technology Fit] ────►  ¿qué tareas a qué L?              │
│         │                                                        │
│         ▼                                                        │
│   [Dynamic Capabilities]────►  L3-L5 no solo automatización      │
│         │                       sino construcción de capacidad   │
│         │                       adaptativa                       │
│         ▼                                                        │
│   [Sociotechnical Trust]────►  verdaderos challenges de         │
│         │                       colaboración humano-IA           │
│         │                       (trust, accountability)          │
│         ▼                                                        │
│   [Real Options]        ────►  justificar inversión              │
│         │                       estratégica L4-L5 bajo           │
│         │                       incertidumbre                    │
│         ▼                                                        │
│   [AI-Native Living Book]──►   metodología misma ejecutable      │
│                                                                  │
└────────────────────────────────────────────────────────────────┘

7 teorías no son capas aisladas sino una cadena completa:
scoring → absorption → matching → adaptation → trust → investment → execution
```

---

## 10. Recomendaciones de sumisión académica

Por estas 7 teorías, múltiples papers pueden derivarse:

| Título de paper (sugerido) | Teoría principal | Journal objetivo |
| --- | --- | --- |
| A GenAI Adoption Maturity Model: Extending BPM Maturity for the LLM Era | Capability Maturity + AI-Native | MIS Quarterly / Information Systems Research |
| Absorptive Capacity in Enterprise AI Adoption: Empirical Evidence from 7 Industries | Absorptive Capacity | Strategic Management Journal |
| Task-Technology Fit Beyond Routine Work: When Should Departments Adopt L4-L5 Agents? | TTF | Information & Management |
| From Automation to Dynamic Capability: How AI Reshapes Organizational Sensing | Dynamic Capabilities | Strategic Management Journal |
| Algorithm Aversion in Workflow Automation: A Mixed-Methods Study | Sociotechnical / Trust | Organization Science |
| Valuing AI Foundation Investments as Real Options | Real Options | SMJ / California Management Review |
| AI-Native Living Books: Methodology as Executable Knowledge Artifact | AI-Native LB | Communications of the ACM |

---

## 11. Bibliografía completa

Ver §3-8 para referencias por teoría y la bibliografía completa en la versión china.

---

Licencia & Citación

Este documento es Apache License 2.0; puede usarse, modificarse, comercializarse, siempre que se preserve la atribución [`../NOTICE`](../NOTICE).
