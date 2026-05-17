# Failure Patterns & Counter-Cases: Cuándo la metodología Tiger AI no debe aplicarse / fallará

> 🌐 Idioma: [繁體中文](FAILURE_PATTERNS.md) ｜ [English](FAILURE_PATTERNS_EN.md) ｜ [Deutsch](FAILURE_PATTERNS_DE.md) ｜ [Français](FAILURE_PATTERNS_FR.md) ｜ Español ｜ [日本語](FAILURE_PATTERNS_JA.md) ｜ [한국어](FAILURE_PATTERNS_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Última actualización: 2026-05-16

---

> **Propósito**: Una metodología que solo discute éxito es material de venta. Los clientes académicos / regulatorios / serios preguntan: "**¿Cuándo falla? ¿Cuándo no debe aplicarse? ¿Qué sale mal si se saltan niveles?**" Este documento registra públicamente los failure patterns y counter-cases conocidos como evidencia dura de la criticabilidad y mejorabilidad de la metodología.

---

## 1. Por qué una metodología debe publicar failure modes

| Audiencia | Por qué necesitan ver fallos |
| --- | --- |
| **Reviewers académicos** | Casos solo de éxito = selection bias → no publicable |
| **Regulatorios** | La evaluación de riesgo debe incluir failure modes + condiciones de early-warning |
| **Clientes serios** | "**Dime cuándo fallas**" es la verdadera pregunta de confianza |
| **Consultores** | Failure modes = memoria institucional = evitar repetición |

> Una metodología que **solo discute éxito** es menos confiable que una que **admite fallo**.

---

## 2. Fallos por saltar niveles

### 2.1 Saltar L1 → Saltar directo a L4 Agent

**Síntomas**: Sin adopción L1 a nivel de empresa. El jefe ve una demo de Agent y quiere un Agent de servicio al cliente. 3 ingenieros construyen un Agent en 3 meses. Una vez live: personal CS tiene miedo de usarlo, QC no firma, IT no sabe cómo cablear los audit logs, Compliance pregunta "quién carga el riesgo".

**Causa raíz**: El personal no ha construido **confianza personal** a través de L1; sin L2 Skill Library → Agent carece de "lógica de juicio escrita por la empresa"; sin L3 Workflow → Agent no tiene pipes legales para actuar en sistemas; sin fundación de gobernanza L1-L3 → Agent sale live como compliance black box.

**Final típico**: Agent descomisionado en 6 meses; VP IT culpado; presupuesto IA cortado.

### 2.2 Saltar L2 → Construir directamente L3 Workflow

**Síntomas**: IT mira tutoriales n8n → construye cadenas Gmail → CRM → Slack. Mes 1: funciona. Personal se queja "los outputs están off-tone / no citan nuestras SOPs". Los ingenieros tunean prompts, pero **cada Workflow tiene 10 prompts dispersos en nodes n8n — sin Owner, sin versión, sin docs**.

**Causa raíz**: Sin L2 Skill Library como "prompts + juicio + datos escritos por la empresa" → L3 se vuelve "playground prompt personal del ingeniero IT".

**Final típico**: Calidad de Workflow drifta con el tiempo; 3 meses después business unit pide revertir; IT pierde confianza.

### 2.3 Ir a L3 / L4 sin HITL

**Síntomas**: Workflow envía automáticamente correos a clientes, crea automáticamente facturas, coloca automáticamente órdenes. Mes 1: 70% ganancia de eficiencia. Mes 2: alucinación LLM → cotización mal precio enviada a cliente tier-A → contrato NT$ 3M perdido.

**Causa raíz**: Toda IA tiene ~0.5-3% tasa de alucinación. **Sin HITL = tarde o temprano golpea un escenario zero-tolerance**.

**Final típico**: C-suite prohíbe IA; AI Champion penalizado; metodología etiquetada "no confiable".

### 2.4 Apresurar L5 ClawTeam antes de que L4 se estabilice

**Síntomas**: El jefe ve demo multi-agent, quiere Agent Team Sales + CS + QC inter-dept. Ni un solo Agent ha pasado Stage Gate 4A-4E, pero 3 Agents están encadenados. Evidence trail se rompe entre Agents → nadie puede rastrear decisiones.

**Causa raíz**: Single Agent sin gobernar → multi-Agent debe perder control (nadie puede identificar qué Agent causó qué problema).

**Final típico**: Proyecto se disuelve en 6 meses; cae de vuelta a single Agents; medio año desperdiciado.

---

## 3. Fallos de Organizational Misfit

### 3.1 Sin AI Champion (driver ejecutivo)

**Precondición**: Cada Phase necesita al menos un Champion que pueda "coordinar inter-dept, decidir, reportar al Sponsor".

**Fallo**: CEO firma Phase A pero no designa Champion → jefes de dept se pasan la culpa durante entrevistas → As-Is incompleto → calidad Phase A pobre → cliente no firma Phase B.

**Rechazo Tiger AI**: Si no hay Champion en su lugar antes de Phase B, **consultor debe rechazar firmar** o requerir designación de Champion primero.

### 3.2 Capacidad IT insuficiente para L3+

**Precondición**: L3 Workflow + L4 Agent necesitan 0.5-2 IT FTE para mantenimiento continuo.

**Fallo**: Empresa tiene 1 persona IT ya maxed en ERP / red / Helpdesk. 5 Workflows van live → nadie los mantiene → 50% fallan en 6 meses → personal revierte a manual.

**Rechazo Tiger AI**: Si Tool 6.3 Organizational Absorption "IT FTE" < mínimo Phase 2 (0.5 FTE dedicados), **aconsejar fuertemente al cliente agregar IT primero**.

### 3.3 Compliance/Regulación insuficiente (industrias sensibles)

**Precondición**: Financial / Healthcare / Government / Legal tienen fuertes requerimientos de compliance.

**Fallo**: Hospital despliega CS IA sin revisión HIPAA / PIPA / derechos de paciente → auditado 3 meses después por Ministerio de Salud → IA retirada, multada, en las noticias → no solo falla el plan IA sino que toda la gobernanza IT es cuestionada.

**Rechazo Tiger AI**: Industrias sensibles sin Compliance Officer / revisión abogado dedicado → **reporte fin Phase A debe marcar "compliance no verificada → suspender Phase B"**.

### 3.4 Turnover ejecutivo rompe roadmap 24-meses

**Precondición**: Phase C 24 meses necesita soporte Sponsor estable.

**Fallo**: Phase A firmada por CEO; CEO sale en Mes 9 de Phase C → nuevo CEO no está de acuerdo → Phase C congelada → NT$ 9.8M invertidos, outputs parciales (L1-L3) retenidos pero L4-L5 abandonados.

**Mitigación Tiger AI**: Phase C mecanismo exit Quarterly Gate C = aun si Sponsor cambia, cada trimestre es independientemente re-evaluable, no sunk-cost-all-lost.

---

## 4. Limitaciones conocidas de la metodología

### 4.1 Modelo de scoring carece de validación psicométrica

**Estado**: 6 constructs × escala 0-4 y fronteras L1-L5 son **consenso de expertos**, **aún no validados** vía Cronbach's α / EFA / CFA / inter-rater reliability.

**Problemas potenciales**:

- Dos consultores scoring la misma empresa pueden yieldear L2 vs L3
- "50-60 = frontera L2 vs 41-60 = L2" carece de base empírica
- Constructs pueden tener colinealidad; cuenta de factores real puede diferir

**Respuesta Tiger AI**: Reporte explícitamente marca "versión expert-consensus, pendiente validación psicométrica"; `PILOT_STUDY_PROTOCOL.md` planea investigación empírica; submissions académicas deben bajar fuerza de claim a "a proposed framework".

### 4.2 Evidence Level de biblioteca de casos

**Estado**: 7 casos son **composites anonimizados** con Evidence Level 2 (por Tool 8.9).

**Problemas potenciales**: Clientes pueden preguntar "¿estos números son reales o fabricados?" ROI ~358%, tasa defectos 3.2 → 2.0% **no puede usarse como commitments contractuales para ningún cliente único**.

**Respuesta Tiger AI**: Cada header de caso marca Evidence Level y naturaleza Composite; SOW usa baseline propia del cliente, no números de caso; reemplazar gradualmente con casos longitudinales reales L3-L5.

### 4.3 Reconocimiento Tiger AI L1-L5 aún nuevo

**Estado**: Tool 2.5 self-qualification 9/10; Condition 6 (amplio reconocimiento industrial) es △ parcial.

**Problemas potenciales**: Contactos iniciales preguntan "APQC, SCOR son reconocidos internacionalmente — ¿por qué autoridad Tiger AI L1-L5?" Las citaciones académicas no han alcanzado masa crítica.

**Respuesta Tiger AI**: Open-source (Apache 2.0 + GitHub); engagar proactivamente con ISO/IEC working groups / discusiones IEEE AI Maturity standards; construir investigación conjunta con instituciones partner académicas (partners específicos divulgados tras firma MOU).

---

## 5. Anti-Patterns a nivel consultor (fallos internos)

### 5.1 Saltar Phase A → Firmar Phase B-C directamente

**Síntomas**: Presión de venta → saltar Phase A → firmar engagement de 6 meses directamente.
**Resultado**: Sin As-Is / RM / Ideal firmado por cliente → en Stage 4+ cliente puede negar "esto no es lo que queríamos" → consultor a la defensiva.
**Disciplina**: **Nunca saltar Phase A**. Es el ancla para todo lo que sigue.

### 5.2 Redactar el Ideal Practice del cliente por él

**Síntomas**: Consultor redacta Ideal Practice para que cliente firme, para ahorrar tiempo.
**Resultado**: Cliente no siente ownership → después desafía cada item → cadena de razonamiento colapsa.
**Disciplina**: **Debe correr Tool 3.6 Co-Creation Workshop 6 pasos**. Votación independiente, consenso colectivo, reality check, definition table, firma de 3 partes — ningún paso puede saltarse.

### 5.3 Reporte basado solo en L1 Self-Report

**Síntomas**: Escritura apresurada → todas conclusiones del cuestionario de auto-evaluación del cliente.
**Resultado**: Auditado por auditoría interna del cliente / casa matriz → "insufficient evidence" → proyecto completo devuelto.
**Disciplina**: Por Tool 8.9 Evidence Hierarchy, **cualquier conclusión principal necesita soporte L3+ (system log)**. Cada párrafo marca `[E:L#]`.

### 5.4 Mezclar Risk en Gap Analysis

**Síntomas**: Capítulo Stage 4 mezcla "este riesgo es alto, no recomendado" juicio subjetivo.
**Resultado**: Stage 4 se vuelve subjetivo → cliente desafía "por qué piensas que esto es riesgoso" → capítulo reescrito.
**Disciplina**: **Stage 4 = inventario objetivo de gap, NO evaluación de riesgo**. Riesgo pertenece a Stage 8 Risk Register.

### 5.5 Saltar revisit radar Stage 2 trimestral en Gate C

**Síntomas**: Durante implementación, enfocado en PoCs, solo reporta progreso cada trimestre, sin revisit radar.
**Resultado**: PoCs hechas pero completitud estructural sin cambio → 24 meses después "¿realmente mejoramos?" sin responder.
**Disciplina**: **Quarterly Gate C debe revisitar radar**. No hacerlo = negligencia del consultor.

---

## 6. Hard Refusal Conditions

Tiger AI **debe rechazar** firmar Phase C bajo estas condiciones (aun si el cliente lo quiere):

- [ ] **Phase A + B no completadas** → sin Ideal Practice firmado → rechazar Phase C
- [ ] **Sin AI Champion confirmado en su lugar** → rechazar Phase C
- [ ] **IT FTE insuficiente para Phase objetivo** → recomendar fuertemente retraso + agregar IT primero
- [ ] **Industria sensible sin Compliance Officer / revisión abogado** → rechazar Phase C
- [ ] **Sponsor no en su lugar (sin soporte CEO claro)** → rechazar Phase C
- [ ] **Cliente quiere saltar niveles (ej. saltar L1-L3 → L4-L5)** → rechazar, requerir fundación Phase 1
- [ ] **Presupuesto insuficiente para phase actual** → rechazar, aconsejar reducción de scope

---

## 7. Customer Exit Protocol

Si cualquier Phase A / B / C falla, Tiger AI se compromete:

1. **Fallo Phase A**: Cliente retiene mid-engagement report + interview summaries + radar → **puede auto-ejecutar o contratar siguiente consultor**
2. **Fallo Phase B**: Reporte completo + tabla Ideal Practice firmada preservados → **puede transferir a otro consultor**
3. **Fallo Phase C a medio camino (decisión Quarterly Gate C de parar)**: Phases completadas preservadas + docs de gobernanza preservados + código / Skills / Workflows completamente transferidos al cliente (consultor **no retiene activos del cliente**)
4. **Sin toma de rehenes de activos del cliente**: por [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) 7 Pillars #1 "Client Hosts"

---

## 8. Cómo usar este documento

| Rol | Uso |
| --- | --- |
| **Entrenamiento interno consultor** | Lectura obligatoria de onboarding; revisión trimestral de equipo "qué failure patterns golpeamos el trimestre pasado" |
| **Pre-firma con cliente** | Consultor comparte proactivamente este doc → cliente confía "este consultor no solo vende éxito, discute honestamente el fallo" |
| **Submissions académicas** | Citar como evidencia de criticalidad / falsificabilidad de la metodología |
| **Documentos regulatorios / bid** | Adjuntar como evidencia de evaluación de riesgo + mitigación |

> **Discutir honestamente el fallo = forma más alta de skill de venta**. Los clientes no compran "éxito garantizado" sino "sabemos qué hacer cuando falla".

---

Licencia & Citación

Este documento es Apache License 2.0; puede usarse, modificarse, comercializarse, siempre que se preserve la atribución [`../NOTICE`](../NOTICE).
