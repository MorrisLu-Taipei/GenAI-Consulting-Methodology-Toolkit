# 06 Delivery — Aceptación de Entrega & Operaciones de Engagement

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Propósito de Este Directorio

Este directorio tiene dos niveles que juntos resuelven una cosa: **cómo transformar un mandato de consultoría profesional y escalablemente en «negocio» y «entregarlo».**

- **Capa aceptación de entrega**: define qué entrega este programa al cliente, cómo se acepta, qué evidence prueba la finalización.
- **Capa operaciones de engagement**: define todo el ciclo de engagement (Sales → Delivery → Support), SOP de roles, plantillas de documentos comerciales, checklists operacionales, gestión pricing y riesgo.

`01`-`03` son «lo que hace el consultor» (metodología); `05` es «cómo hacer que el cliente quiera» (pre-venta); este directorio es «**tras firma, cómo ejecutar todo el mandato como un negocio: completo, limpio, repetible**». El problema: **una firma de consultoría con solo metodología sin framework operacional será aplastada por scope creep, tendrá rupturas de handover, incidentes de seguridad, no podrá escalar.**

Quién lo usa: gerentes de proyecto, consultores, Sales (Closer), Technical Lead, Owner lado cliente.

## 2. Posición en la Metodología

| Eje | Mapeo |
| --- | --- |
| Flujo de servicio 3 fases | **Deliver** + marco operacional que envuelve las 3 fases en «negocio» |
| Estructura de consultoría 8 etapas | Corresponde a la **entrega y aceptación** de las 8 etapas; engagement lifecycle es la «cáscara comercial» de las 8 etapas |
| **Modelo de contrato 3 fases (bucle cerrado de consultoría)** | **Phase A Diagnóstico 2W → Phase B Estrategia 4W → Phase C Implementación 24M + revisión radar trimestral** — la fase Delivery del ciclo ES el bucle Phase A→B→C |
| Madurez L1-L5 | Aceptación del paquete de entrega cubre entregables de todos los niveles L1-L5 |
| Engagement Lifecycle | **Este directorio ES el cuerpo del ciclo de engagement (Sales → Delivery → Support)** |

> 🔁 **Ciclo de engagement ↔ bucle cerrado de consultoría**: la «fase Delivery» de este directorio **no es maratón 6 semanas** sino el **bucle cerrado** descrito en [`../03_Consulting_Report/README.md`](../03_Consulting_Report/README.md) §4 y [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6: informe intermedio Phase A firmado → Gate A → informe completo Phase B → Gate B → implementación 24 meses Phase C + **revisión radar trimestral** (mecanismo de falsación de la gestión científica). La fase Support corresponde a Retainer / Maintenance tras Phase C.

## 3. Objetivos & Beneficios

| Objetivo | Beneficio |
| --- | --- |
| Paquete de entrega y criterios de aceptación claros | Cliente y consultor de acuerdo sobre «está terminado», sin disputa |
| Ciclo de engagement completo | De lead a closeout tiene SOP, no artesanía personal |
| SOP de roles | Escalable (no una persona hace todo), handover sin ruptura |
| Plantillas de documentos comerciales | SOW/contrato/factura/change order listos, no reescritos cada vez |
| Checklists operacionales | pre-project/security/QA/handover/offboarding nada olvidado |
| Framework pricing y riesgo | Scope creep no come la margen, saber cuándo decir «no» |

**Si se salta este directorio**: metodología fuerte pero negocio no escala — scope creep, trabajo en vano, ruptura handover, incidente seguridad, dependencia persona clave, cuentas incobrables.

## 4. Flujo & Lógica

```text
Ciclo de engagement (ENGAGEMENT_LIFECYCLE):
  Sales (Lead → Discovery → Proposal → Contract)
     → Usar BUSINESS_DOCUMENT_TEMPLATES (propuesta, SOW)
     → Usar PRICING_AND_RISK (pricing, risk register)
  Delivery (Kickoff → Build → Test → Security → Handover)
     → Usar DELIVERY_CHECKLISTS (pre-project / security / QA / handover)
     → Usar DELIVERY_PACKAGE_AND_ACCEPTANCE (aceptación paquete)
     → Usar DELIVERY_ROLE_SOPS (quién responsable de qué fase)
  Support (Retainer → Maintenance → Offboarding)
     → Usar DELIVERY_CHECKLISTS (offboarding)
Continuo: 7 Pillars como principio base
```

| Paso | Quién | Cuándo | Input | Output |
| --- | --- | --- | --- | --- |
| Ejecutar ciclo | PM | Mandato completo | `ENGAGEMENT_LIFECYCLE` | Avance de fases |
| Producir documentos comerciales | Closer / PM | Sales / al cambiar | `BUSINESS_DOCUMENT_TEMPLATES` | Propuesta / SOW / Change Order |
| Pricing y evaluación riesgo | Closer / PM | Proposal / Kickoff | `PRICING_AND_RISK` | Cotización + Risk Register |
| Ejecutar checklists | PM / Technical Lead | Cada fase entrega | `DELIVERY_CHECKLISTS` | Cada fase pasada |
| Aceptación entrega | PM + cliente | Handover | `DELIVERY_PACKAGE_AND_ACCEPTANCE` | Firma cliente |
| División de roles | Todo el equipo | Continuo | `DELIVERY_ROLE_SOPS` | Responsabilidad clara y handover |

> Lógica: `ENGAGEMENT_LIFECYCLE` es el tronco (lifecycle); los otros 5 son herramientas para fases — plantillas, pricing & riesgo, checklists, SOP roles, aceptación. **7 Pillars** (cliente posee, cliente paga, seguridad primero, probar a fondo, documentación completa, handover limpio, scope claro) atraviesan todo.

## 5. Descripciones de Archivos

### Capa Aceptación de Entrega

| Archivo | Uso |
| --- | --- |
| `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` | Lista de entrega y tabla de aceptación item-by-item para diagnóstico madurez IA, cursos L1-L5, L4 Hermes Agent, informe de diagnóstico de consultoría 8 etapas. |

### Capa Operaciones de Engagement (adaptado de Mirza Iqbal / next8n.com Workflow Automation Delivery Framework, MIT, generalized para contexto L1-L5 transformación IA; cita ver `../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`)

| Archivo | Uso |
| --- | --- |
| `ENGAGEMENT_LIFECYCLE.md` | Ciclo 3 fases (Sales → Delivery → Support), sub-fases y outputs de cada fase, 7 Pillars, ciclo × 8 etapas cross-referencia, checklist pre-engagement. |
| `DELIVERY_ROLE_SOPS.md` | 7 SOP de roles entrega (Lead Gen / Sales Rep / Closer / PM / Technical Lead / Developer / Client), cada rol: responsabilidad, entregables clave, puntos handover, compañeros colaboración, fase ciclo, más matriz rol × ciclo y regla de oro handover. |
| `BUSINESS_DOCUMENT_TEMPLATES.md` | 8 plantillas documentos comerciales: propuesta, SOW, MSA outline, change order, factura, documento handover, contrato mantenimiento, e-mails críticos. **Con disclaimer legal — esqueletos no son documentos jurídicos, deben ser revisados por jurista.** |
| `DELIVERY_CHECKLISTS.md` | 5 checklists operacionales: pre-project, security, QA, handover, offboarding; diferencia con Stage Gate metodológico. |
| `PRICING_AND_RISK.md` | Dos principios de separación del pricing, 4 modelos de pricing, línea productos por niveles, riesgos comunes de mandato y mitigación, cuándo decir «no», proceso de gestión de incidente. |

### `*_EN.md`

Versiones inglesas sibling de algunos archivos.

## 6. Mapeo a Otros Directorios

| Directorio | Relación con este directorio | Flujo de datos |
| --- | --- | --- |
| `01_Assessment` | Diagnóstico corresponde a fase Sales del ciclo | `01` ↔ `06` Sales |
| `02_Course_Design` | Output en clase entra a aceptación paquete | `02` output → `06` aceptación |
| `03_Consulting_Report` | Informe de consultoría es entrega central del paquete | `03` informe → `06` aceptación |
| `05_Sales` | Precios/paquetes del deck corresponden al ciclo y pricing | `05` deck ↔ `06` pricing |
| `00_Overview` | Ciclo de engagement es el marco que transforma la historia en negocio | `00` historia → `06` operaciones |
| `90_References` | Cita tercera para capa operaciones (framework Mirza Iqbal) | `90` cita → `06` |

## 7. Escenarios de Uso Comunes

- **Nuevo mandato recibido**: PM usa la «checklist pre-engagement» de `ENGAGEMENT_LIFECYCLE.md` para verificar preparación, `DELIVERY_ROLE_SOPS.md` para asignar roles.
- **A punto de firmar**: Closer usa la plantilla SOW de `BUSINESS_DOCUMENT_TEMPLATES.md` (in/out of scope claramente escritos), `PRICING_AND_RISK.md` para pricing.
- **Cada fase de entrega**: ejecutar checklists pre-project / security / QA / handover contra `DELIVERY_CHECKLISTS.md`.
- **Entrega al cliente**: usar `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` para aceptación item-by-item + documento handover de `BUSINESS_DOCUMENT_TEMPLATES.md`.
- **Cliente añade sin cesar requisitos**: usar mitigación scope creep de `PRICING_AND_RISK.md` + change order de `BUSINESS_DOCUMENT_TEMPLATES.md`.
- **Closeout**: ejecutar checklist offboarding de `DELIVERY_CHECKLISTS.md`.

---

## ⭐ Cross-Topic Quick References: 5 Temas Centrales, Dónde Encontrar

Toda la metodología tiene 5 arterias principales atravesando todos los directorios. Cómo este directorio se conecta a cada una:

| Cross-Topic | Lugar principal | Cómo este directorio se conecta |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + co-lectura tres motores** | Root [`README_ES.md`](../README_ES.md) §🌟 ｜ [`AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | Durante el mandato los tres motores pueden movilizarse en división del trabajo: Antigravity para reuniones cliente / Codex para audit SOW y borradores de informe / Claude Code para simulación Phase B y review multi-perspectivas |
| 🎓 **Fundamento académico (7 pilares)** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | «Seguridad primero / HITL» de los 7 Pillars corresponde a Sociotechnical Systems & Trust (Bostrom / Dietvorst / Glikson); scope creep / fallos de salto de nivel corresponden a failure patterns Real Options + Absorptive Capacity |
| 📚 **Educación L1-L5** | [`../02_Course_Design/`](../02_Course_Design/) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md) | Aceptación paquete cubre entregables verificables de todos L1-L5; output en clase entra en [`DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](DELIVERY_PACKAGE_AND_ACCEPTANCE.md) para aceptación item-by-item |
| 🔁 **Consultoría / 8 etapas + Closed-Loop Phase A→B→C** | [`EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Este directorio ES la «cáscara comercial» del bucle cerrado de consultoría** — ciclo Sales→Delivery→Support corresponde a Phase A→B→C + revisión radar trimestral |
| 📖 **Referencias / agradecimientos** | [`../90_References/`](../90_References/) §2 agradecimientos | Capa operaciones cita Mirza Iqbal / next8n.com Workflow Delivery Framework (MIT), detalles en [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) |
