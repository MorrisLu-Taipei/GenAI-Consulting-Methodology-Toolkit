# AI Governance Alignment: Metodología Tiger AI vs frameworks internacionales de AI Governance

> 🌐 Idioma: [繁體中文](AI_GOVERNANCE_ALIGNMENT.md) ｜ [English](AI_GOVERNANCE_ALIGNMENT_EN.md) ｜ [Deutsch](AI_GOVERNANCE_ALIGNMENT_DE.md) ｜ [Français](AI_GOVERNANCE_ALIGNMENT_FR.md) ｜ Español ｜ [日本語](AI_GOVERNANCE_ALIGNMENT_JA.md) ｜ [한국어](AI_GOVERNANCE_ALIGNMENT_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Última actualización: 2026-05-16

---

> **Lo que esto responde**: ¿Cómo se mapea la metodología Tiger AI a los frameworks internacionales de AI Governance (NIST AI RMF / EU AI Act / ISO/IEC 42001 / OECD AI Principles / Taiwan AI Basic Act / Singapore Model AI Governance)? Boards / compliance / regulatorios necesitan puntos de aterrizaje específicos en cada framework.
>
> BPM / consultoría / AI-maturity alignments están en [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md). **Este doc se enfoca en AI Governance**, especialmente credibilidad institucional L4-L5.

---

## 1. Por qué L4-L5 necesita AI Governance Alignment formal

L4 Autonomous Agent + L5 Multi-Agent Organization = IA ejecutando acciones de negocio sin supervisión humana en tiempo real.

Boards / regulatorios hacen tres preguntas obligatorias:

1. **¿Quién carga la responsabilidad**? ¿Quién es legal / éticamente responsable cuando la IA falla?
2. **¿Qué mecanismo de early-warning**? ¿Qué dispara intervención humana para decisiones de alto riesgo?
3. **¿Cómo se audita**? ¿Pueden terceros verificar independientemente el comportamiento de IA?

Las respuestas deben mapearse a **frameworks de gobernanza reconocidos internacionalmente** para ser aceptables a boards, compliance, regulatorios.

---

## 2. Ocho etapas × Frameworks AI Governance mainstream

| Framework de Gobernanza | Fuente / Naturaleza | Etapas Tiger AI cubiertas |
| --- | --- | --- |
| **NIST AI RMF** | US NIST, 2023 / voluntario pero ampliamente adoptado | Govern→Stage 8; Map→Stage 1-2; Measure→Stage 4+8; Manage→Stage 6-8 |
| **EU AI Act** | EU, 2024 / regulación obligatoria | High-risk AI mapea a L4-L5; transparencia→Stage 8 Audit; HITL→todas etapas |
| **ISO/IEC 42001:2023 AI Management System** | ISO, 2023 / certificable | AI policy→Stage 8; risk→Stage 4+8; mejora continua→Phase C |
| **ISO/IEC 23894:2023 AI Risk Management** | ISO / foco de riesgo | Risk Register→Stage 8 |
| **OECD AI Principles** | OECD+miembros / principios de política | 5 principios → Tool 7.2 + 8.8 |
| **Taiwan AI Basic Act (borrador)** | Taiwan Legislative Yuan, en review | Mapea a clientes Taiwan high-compliance |
| **Singapore Model AI Governance Framework** | IMDA / voluntario | 4 pillars → Stage 7 To-Be + Stage 8 |
| **US AI Bill of Rights** | Casa Blanca / declaración de política | 5 protecciones → Tool 8.8 Ethics + protección datos cliente |

---

## 3. NIST AI RMF (Referencia global más importante)

NIST AI RMF es el framework AI Governance **más ampliamente adoptado**. 4 funciones core:

### 3.1 Govern

**NIST requiere**: AI policy nivel-org, roles, responsabilidades, cultura.

**Tiger AI**: Stage 8 §12.1 matriz RACI; Tool 8.8 AI Ethics Checklist 15 items; arquitectura 4-capas Layer 1 Governance (Policy / Ethics / Compliance / Risk Committee / Audit Owner); Tool 3.6 firma cliente 3-partes = commitment escrito nivel-corporate.

### 3.2 Map

**NIST requiere**: inventario de contexto del sistema IA, riesgos, stakeholders.

**Tiger AI**: Stage 1 As-Is (entrevistas, Systems Inventory, AI Usage Inventory, Swimlane); Tool 2.2 RM Mapping; Tool 2.6 + 2.7 Component Map + 4-capas.

### 3.3 Measure

**NIST requiere**: cuantificar performance, impacto, riesgo del sistema IA.

**Tiger AI**: Stage 2 radar 0-4 scoring; Stage 4 Impact × Effort; Stage 8 Tool 8.5 Value Tracking Matrix (5 dimensiones); Tool 8.9 Evidence Hierarchy (L1-L5 evidence strength); revisit radar trimestral Gate C.

### 3.4 Manage

**NIST requiere**: risk mitigation, monitoring, mejora continua.

**Tiger AI**: Stage 6 Phased Goals + Stage Gate Criteria; Stage 7 Human-AI Collaboration + HITL nodes; Stage 8 Tool 8.6 Risk Register; Tool 8.7 Audit Log; Phase C 24-meses revisión trimestral.

> **General**: NIST AI RMF 4 funciones aterrizan completamente en Tiger AI 8 etapas, **produciendo documentos NIST compliance directamente**.

---

## 4. EU AI Act (Regulación obligatoria)

EU AI Act clasifica IA en 4 tiers de riesgo: Unacceptable / High-risk / Limited / Minimal.

### 4.1 Mapping de clasificación de riesgo

| EU AI Act Tier | Tiger AI L-level | Gobernanza requerida |
| --- | --- | --- |
| **Unacceptable** (social scoring, real-time biometric ID, etc.) | ❌ Tiger AI **rehúsa asistir** | — |
| **High-risk** (HR, credit, medical, education, judicial, infraestructura crítica) | Principalmente escenarios L4-L5 | Risk assessment obligatorio + transparencia + human oversight + post-market monitoring |
| **Limited** (chatbots, deepfake) | Principalmente escenarios L1-L3 | Obligaciones de transparencia (marcar "AI-generated") |
| **Minimal** (spam filtering, etc.) | Principalmente escenarios L1-L2 | Obligaciones generales |

### 4.2 High-Risk AI Article Alignment

| EU AI Act Artículo | Mapping Tiger AI |
| --- | --- |
| **Art. 9 Risk Management System** | Stage 8 Tool 8.6 Risk Register |
| **Art. 10 Data Governance** | Tool 8.7 Audit Log + Tool 8.4 Permission Matrix |
| **Art. 11 Technical Documentation** | Reporte consultoría 14-secciones completo + docs arquitectura 4-capas |
| **Art. 12 Record-Keeping (logs)** | Tool 8.7 Audit Log 7 event types |
| **Art. 13 Transparency** | Tool 8.8 "AI-generated marking" + firma pública Ideal Practice |
| **Art. 14 Human Oversight** | Tool 7.2 Human-AI Collaboration + HITL nodes + Reviewer Workflow |
| **Art. 15 Accuracy, Robustness, Cybersecurity** | Stage 8 Tool 8.5 Value Tracking (dim calidad) + Audit Log + Security |
| **Art. 17 Post-Market Monitoring** | Phase C trimestral Gate C + revisit radar Stage 2 + value tracking 5-dim longitudinal |
| **Art. 26 Quality Management System** | Alignment ISO/IEC 42001 (ver §5) |
| **Art. 72 Serious Incident Reporting** | Tool 8.8 Ethics §11 "AI system incident response" |

> **Clientes con operaciones EU**: deliverables de la metodología Tiger AI (reporte 14-secciones completo + governance docs) sirven como paquete de evidencia compliance EU AI Act.

---

## 5. ISO/IEC 42001:2023 AI Management System

ISO 42001 es el primer estándar AI management system **certificable por terceros**. La estructura refleja ISO 9001 / 27001.

### 5.1 Mapping de sección ISO 42001

| ISO 42001 Sección | Mapping Tiger AI |
| --- | --- |
| **4. Context of the Organization** | Stage 1 As-Is + Stage 2 Reference Model |
| **5. Leadership** | Definición rol Sponsor + AI Champion (RACI) + firma AI Policy |
| **6. Planning** | Stage 5 Problem Definition + Stage 6 Phased Goals + Tool 6.3 Absorption |
| **7. Support** | Change Management Playbook + plan de entrenamiento + planificación de recursos |
| **8. Operation** | Stage 7 To-Be Operating Model + Human-AI Collaboration + HITL |
| **9. Performance Evaluation** | Tool 8.5 Value Tracking Matrix + Tool 8.7 Audit Log + radar trimestral Gate C |
| **10. Improvement** | Phase C revisión trimestral + acumulación Cases-as-Benchmarks |
| **Annex A Controls** | Tool 8.4 Permission + Tool 8.6 Risk + Tool 8.7 Audit + Tool 8.8 Ethics |

> **Meta**: Las empresas persiguiendo certificación ISO/IEC 42001 pueden usar deliverables Tiger AI como documentación management-system. Tiger AI **cubre completamente todas las secciones ISO 42001**.

---

## 6. OECD AI Principles (5 principios)

OECD AI Principles son ampliamente adoptados por G20, APEC.

| OECD Principio | Mapping Tiger AI |
| --- | --- |
| **1. Inclusive growth, sustainable development and well-being** | Stage 8 Tool 8.5 Value Tracking incluye "employee experience"; Change Management incluye "upgradear roles, no reemplazar" |
| **2. Human-centered values and fairness** | Tool 8.8 Ethics §9 bias / discrimination assessment; Tool 7.2 HITL obligatorio |
| **3. Transparency and explainability** | Tool 8.7 Audit Log + Tool 8.8 §7 "AI-generated marking" + full evidence trail |
| **4. Robustness, security and safety** | Stage 8 Risk Register + Tool 8.4 Permission + modo de despliegue (Hybrid / On-Prem 3 opciones) |
| **5. Accountability** | Matriz RACI + "**firma 3-partes Ideal Practice firmada por cliente**" + Reviewer sign-off |

---

## 7. Taiwan AI Basic Act (Borrador)

Taiwan Legislative Yuan AI Basic Act en review (al 2026/05). La metodología Tiger AI **se alinea con las provisiones principales**:

| Highlight del borrador | Mapping Tiger AI |
| --- | --- |
| **Productos/servicios IA necesitan risk grading** | Identificación Stage 1-2 + arquitectura 4-capas + Tool 8.6 Risk Register |
| **Protección PII sobre training de modelo** | Tool 8.8 §2 PII no enviado al LLM / redacted; despliegue por defecto on-prem para alta-sensibilidad |
| **Transparencia y explicabilidad de algoritmo** | Tool 8.7 Audit Log + 8.8 §7 marcado IA |
| **Protección de derechos del usuario** | Tool 8.8 §5 los empleados tienen derecho a saber que el trabajo es procesado por IA |
| **Accountability del operador** | RACI + Tool 8.8 §8 atribución IP |
| **Autoridad regulatoria gubernamental** | Tool 8.7 Audit Log retention soporta auditoría gubernamental |

⚠️ Taiwan AI Basic Act aún no aprobado. Este alignment se actualizará con el texto final.

---

## 8. Singapore Model AI Governance Framework

Singapore IMDA framework voluntario, 4 pillars:

| Singapore Pillar | Mapping Tiger AI |
| --- | --- |
| **1. Internal Governance Structures** | Layer 1 Governance + RACI |
| **2. Determining Level of Human Involvement** | Tool 7.2 Human-AI Collaboration (HITL nodes) |
| **3. Operations Management** | Tool 8.4-8.7 set completo (Permission / Value / Risk / Audit) |
| **4. Stakeholder Interaction & Communication** | Tool 8.2 Change Management Playbook + Stakeholder Map |

---

## 9. Map de deliverables regulatorios / compliance

Cuando los clientes enfrentan regulatorio / compliance / auditoría interna, qué deliverables Tiger AI pueden ser entregados directamente:

| Necesidad regulatoria | Deliverable Tiger AI directo |
| --- | --- |
| AI risk assessment | Stage 4 Gap + Tool 8.6 Risk Register |
| AI policy | Tool 8.8 Ethics Checklist 15 items + AI Policy doc |
| Audit evidence package | Tool 8.7 Audit Log + logs trimestral Gate C + Stage 2 radar before/after |
| Prep audit 3a parte | Reporte 14-secciones completo + arquitectura 4-capas + 4 docs autoritativos |
| ROI / substanciación de beneficio | Tool 8.5 Value Tracking 5 dimensiones + KPI longitudinal |
| Flow de respuesta a incidente | Tool 8.8 §12 + triggers Tool 8.6 Risk Register |
| Records de entrenamiento empleado | Records de entrenamiento Change Management + Tool 8.8 §14 |

---

## 10. Recomendaciones de certificación / labeling

Basado en madurez de la metodología, los clientes Tiger AI pueden considerar:

| Certificación | Aplica a | Timeline est. |
| --- | --- | --- |
| **ISO/IEC 42001 AI Management System** | Clientes L3+ (con gobernanza completa) | 6-12 meses |
| **ISO/IEC 27001 ISMS** | Todos clientes (baseline seguridad) | 6-12 meses |
| **SOC 2 Type II** | Clientes US / servicio multinacional | 6-12 meses |
| **EU AI Act CE Marking** (High-risk) | Operaciones EU + sistemas IA High-risk | 12-24 meses |

> Los deliverables Tiger AI sirven como **base del 90% de la documentación de certificación**. La certificación real requiere auditoría de tercero.

---

## 11. Documentos relacionados

| Documento | Relación |
| --- | --- |
| [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | Se alinea con firmas consultoría / BPM / AI maturity frameworks; este doc añade AI Governance |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Por qué la metodología resiste el debate |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | Failure modes & counter-cases de la metodología |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Stage 8 | Toolkit gobernanza completo |

---

## 12. Referencias

- NIST (2023). *AI Risk Management Framework (AI RMF 1.0)*.
- European Commission (2024). *Regulation on Artificial Intelligence (EU AI Act)*.
- ISO/IEC (2023). *ISO/IEC 42001:2023 — AI Management System*.
- ISO/IEC (2023). *ISO/IEC 23894:2023 — AI Risk Management*.
- OECD (2019, updated 2024). *OECD AI Principles*.
- The White House (2022). *Blueprint for an AI Bill of Rights*.
- Singapore IMDA (2020). *Model AI Governance Framework, 2nd Edition*.
- 立法院 (en review). *Taiwan Artificial Intelligence Basic Act Draft*.

---

Licencia & Citación

Este documento es Apache License 2.0; puede usarse, modificarse, comercializarse, siempre que se preserve la atribución [`../NOTICE`](../NOTICE).
