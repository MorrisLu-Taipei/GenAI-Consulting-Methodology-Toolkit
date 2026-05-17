# Alineación de la metodología Tiger AI con frameworks de la industria

> 🌐 Idioma: [繁體中文](INDUSTRY_FRAMEWORK_ALIGNMENT.md) ｜ [English](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) ｜ [Deutsch](INDUSTRY_FRAMEWORK_ALIGNMENT_DE.md) ｜ [Français](INDUSTRY_FRAMEWORK_ALIGNMENT_FR.md) ｜ Español ｜ [日本語](INDUSTRY_FRAMEWORK_ALIGNMENT_JA.md) ｜ [한국어](INDUSTRY_FRAMEWORK_ALIGNMENT_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Última actualización: 2026-05-15

---

> **Qué responde este documento**: ¿Cómo se relaciona la metodología Tiger AI con las firmas de consultoría mainstream (McKinsey / BCG / Bain / Deloitte / Accenture / PwC), escuelas académicas (Rosemann BPM / CMMI / APQC / SCOR / TOGAF / Dragon1) y frameworks de madurez IA (Gartner / MIT / MMC / Forrester)? ¿Qué duplicamos, completamos o innovamos?
>
> **Postura central**: Tiger AI no reinventa la rueda sino **integra herramientas mainstream, completa el closed loop de la industria, y agrega esenciales de la era GenAI**. Todos los frameworks citados están detallados en [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md); este documento mapea entre firmas.

---

## 1. Por qué importa esta alineación

| Audiencia | Lo que obtiene |
| --- | --- |
| Gran empresa IT/CIO | «Esta metodología es compatible con nuestro TOGAF / ITIL / APQC existente» |
| Consultores de otras firmas | «Vengo de BCG/Deloitte — veo qué herramientas sigo usando y cuáles son específicas de Tiger AI» |
| Revisores académicos | «Tiger AI no es ciencia marginal — se sostiene sobre los hombros de las escuelas Rosemann/CMMI/APQC» |
| Reguladores | «Los estándares citados son internacionalmente reconocidos; la gobernanza IA mapea a los frameworks GRC existentes» |
| Ejecutivos cliente | «Lo que pagamos es lo mejor de la industria + completión de la era GenAI, no el método propietario de una sola firma» |

---

## 2. Ocho etapas vs. firmas de consultoría mainstream

### 2.1 Tabla de alineación inter-firmas

| Etapa | Tiger AI | McKinsey | BCG | Bain | Deloitte | Accenture | PwC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1 As-Is Snapshot** | 40-Q interview + Inventory + Swimlane | 7-Step Step 1: Define Problem | Diagnostic Survey | Customer / Process Diagnostics | Business Architecture Discovery | Living Business Diagnostic | Value Creation Diagnostic |
| **2 Reference Model** | APQC + Tiger AI L1-L5 + 4 capas | (raramente hecho) | Capability Maturity Map | (no-core) | TOGAF Capability Assessment | Industry Reference Architecture | Capability Framework |
| **3 Best Practice → Ideal** | Benchmark + Ideal Practice Workshop | Best Practice Research | Strategic Position vs Industry | NPS / Customer Loyalty | Industry Pulse | Industry Benchmarking | Industry Outlook |
| **4 Gap Analysis** | M/B/R + Impact×Effort | Issue Tree + MECE | Importance-Performance Map | Pareto + Lean | Capability Gap Heatmap | Maturity Gap Analysis | Gap Map |
| **5 Problem Definition** | 80/20 + 5 Whys + EPS | Day-1 + SCQ + Pyramid | Strategic Diagnosis | Bain Question Pyramid | Hypothesis-Driven | Outcome-Driven | Issue-Tree Synthesis |
| **6 Phased Goals** | Phased + Absorption | Workplan + Critical Path | Phased Transformation | Bain Way Multi-phase | Imagine-Deliver-Run | Wave Planning | Transformation Wave |
| **7 To-Be Design** | Phased To-Be + Human-AI | To-Be Operating Model | Operating Model Design | Bain Way (Org) | Target Operating Model | Future-State Blueprint | Future Operating Model |
| **8 Implementation & Change** | Roadmap + Change + Value Tracking | Influence Model + 7S | Smart Simplicity | Bain Results Delivery | Diamond Performance | Wired for Change | Project Delivery |

### 2.2 Lo que cada firma contribuye

- **McKinsey** MECE / Pyramid / Issue Tree **son fuentes para herramientas Tiger AI Stage 4-5** (en Frameworks Library)
- **BCG** pensamiento Capability Maturity **inspira scoring RM Tiger AI Stage 2**
- **Bain** Customer / Process Diagnostics **complementan banco de entrevistas Tiger AI Stage 1**
- **Deloitte** Imagine-Deliver-Run **se alinea fuertemente con tres fases Tiger AI Stage 6**
- **Accenture** Wave Planning **consistente con Tiger AI Phase 1/2/3**
- **PwC** Value Creation Diagnostic **mapea a value tracking Tiger AI Stage 8**

> **Conclusión**: Ninguna de las 8 etapas es una «invención» Tiger AI. **La innovación reside en integrar estas herramientas dispersas en una cadena de razonamiento completa con dependencias de datos, firmas del cliente y falsificación en closed loop**.

---

## 3. Alineación de escuelas Reference Model

### 3.1 Tiger AI 4 capas vs. principales frameworks EA

| Capa | Tiger AI | Dragon1 EA | TOGAF ADM | Zachman | ArchiMate |
| --- | --- | --- | --- | --- | --- |
| **L1 Governance** | AI Governance | Enterprise Governance | (Architecture Vision) | Scope | Motivation + Strategy |
| **L2 Business** | AI Business (L1-L5 aquí) | Business(es) | Business Architecture (B) | Business | Business Layer |
| **L3 Information** | AI Information | Information Facilities & Systems | Data + Application (C+D) | System | Application + Information |
| **L4 Technical** | AI Technical | IT Infrastructure(s) | Technology (E) | Technology | Technology + Implementation |

**Por qué esta alineación**: todos los frameworks EA mainstream convergen en «**4 capas de abstracción**» — no coincidencia sino resultado necesario del eje científico «abstracción × volatilidad» (ver [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) §5).

### 3.2 Alineación Process Reference Model

| Caso de uso | Tiger AI recomienda | APQC PCF | SCOR | eTOM | ITIL | CMMI |
| --- | --- | --- | --- | --- | --- | --- |
| **Procesos inter-industrias** | APQC PCF (default) | ✓ 13 Cat | — | — | — | — |
| **Supply chain / manufactura** | SCOR | — | ✓ 6 secciones | — | — | — |
| **Telecom / suscripción** | eTOM | — | — | ✓ 3 niveles | — | — |
| **IT service mgmt** | ITIL | — | — | — | ✓ 5 fases | — |
| **Madurez software** | CMMI | — | — | — | — | ✓ 5 niveles |
| **Madurez de adopción IA** | **Tiger AI L1-L5 (DIY, llena brecha industria)** | — | — | — | — | — |

> **Ningún RM industrial existente cubre adopción IA** — de ahí la necesidad de Tiger AI L1-L5, auto-calificado en Tool 2.5 score 9/10.

### 3.3 Raíces de la escuela BPM Maturity

| Concepto | Fuente | Mapping Tiger AI |
| --- | --- | --- |
| Capability Maturity Levels (escala 5 niveles) | **Rosemann BPM Maturity** (QUT) + CMMI | Stage 2 0-4 scoring, Tiger AI L1-L5 |
| Process Excellence Characteristics | Rosemann + APQC | Stage 3 Excellence Capability Profile |
| Stage Gates | CMMI + Rosemann | Stage 6 acceptance gates |
| Organizational Absorption | Rosemann (investigación emergente) | Tool 6.3 Absorption Assessment |

> **Agradecimiento**: Prof. Michael Rosemann (QUT) es el advisor de máster del autor; las raíces de la escuela BPM de esta metodología provienen directamente de su mentoría de larga data.

---

## 4. Alineación de frameworks de madurez IA

### 4.1 Principales frameworks de madurez IA mapeados

| Framework | Niveles | Mapping Tiger AI L1-L5 |
| --- | --- | --- |
| **Gartner AI Maturity Model** | Awareness / Active / Operational / Systemic / Transformational | L1 / L1+L2 / L3 / L4 / L5 |
| **MIT Sloan AI Capability** | Experimenters / Investigators / Pioneers / Empowerment | L1-L2 / L2-L3 / L3-L4 / L5 |
| **McKinsey AI Quotient (AIQ)** | (escala continua, 4 drivers) | Mapea al radar seis-dimensiones Tiger AI |
| **Capgemini DELTA Maturity** | Data / Enterprise / Leadership / Targets / Analysts | Mapea al eje gobernanza + deployment |
| **Forrester AI Pulse Index** | (3 anillos: People / Process / Tech) | Mapea a arquitectura 4 capas Tiger AI |
| **Tiger AI L1-L5** | L1 Chat / L2 Skill / L3 Workflow / L4 Auto Agent / L5 Agent Team | (**eje de escala L1-L3 + eje de autonomía IA L4-L5**) |

### 4.2 Aportes de Tiger AI L1-L5 al mainstream

| Aporte | Por qué la industria carece | Tiger AI lo llena |
| --- | --- | --- |
| **Mapping de herramientas explícito** | Gartner/MIT describen niveles abstractamente, sin landing de herramienta | L1=OpenWebUI, L2=Antigravity, L3=n8n, L4=Hermes, L5=ClawTeam |
| **Eje de escala separado del eje de autonomía** | La industria los mezcla, desdibujando L4-L5 | Escala (humano-led) vs Autonomía (IA-led), frontera crítica L3→L4 |
| **Específico GenAI (no ML tradicional)** | La mayoría de frameworks atascados en ML tradicional / modelos predictivos | Plenamente enfocado en paradigma LLM / Agent / Workflow |
| **Acceptance de etapa verificable** | Frameworks industriales mayormente escalas de auto-evaluación | Cada nivel tiene Stage Gate Criteria, independientemente verificable |
| **Coordenadas duales cross-RM** | Frameworks industriales uniaxiales | Tiger AI ortogonal al RM industrial (APQC/SCOR), radar dual |

---

## 5. Alineación de herramientas analíticas clásicas

Detalladas en [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md). Resumen:

### 5.1 Herramientas estrategia

Porter's 5 Forces (Stage 3), PESTEL (Stage 3), BCG Growth-Share (Stage 3), SWOT (Stage 3/4), Blue Ocean (Stage 7), Wardley Map (Stage 6/7).

### 5.2 Herramientas análisis de problemas

MECE (Stage 2/4), Issue Tree (Stage 4/5), Pyramid Principle (Stage 5), SCQ (Stage 5), 5 Whys (Stage 5), Fishbone (Stage 4/5), Hypothesis-Driven (Stage 1-5), 80/20 (Stage 5).

### 5.3 Herramientas change management

Kotter 8 Steps (Stage 8), ADKAR (Stage 8), Stakeholder Map (Stage 8), RACI (Stage 8), Influence Model (Stage 8), 7S (Stage 2/8).

### 5.4 Herramientas financieras / ROI

NPV/IRR (Stage 8), Payback (Stage 8), Break-Even (Stage 8), Sensitivity Analysis (Stage 8), Balanced Scorecard (Stage 8), OKR (Stage 6/8).

---

## 6. Elementos únicos / innovadores de Tiger AI

La mayoría de herramientas vienen de la industria, pero Tiger AI tiene estas **integraciones o innovaciones únicas**:

| Innovación | Por qué la industria carece | Diseño Tiger AI |
| --- | --- | --- |
| **Tiger AI L1-L5 GenAI Adoption RM** | RMs industriales aún en IT / ML tradicional | Primer RM diseñado específicamente para LLM/Agent/Workflow, cumple Tool 2.5 10 condiciones 9/10 |
| **Client Ideal Practice Co-Creation Workshop** | La industria hace Best Practice benchmarking pero raramente Ideal firmado por cliente | Tool 3.6: cliente **firma él mismo**, no puede negar razonamiento posterior |
| **Cases-as-Benchmarks formato 9 campos** | Cases industriales mayormente narrativos, sin cálculo de gap | Tool 3.5: cases obligatoriamente 9 campos, cliente auto-calcula gap en 30 min |
| **Loopback radar Stage 2 trimestral** | Roadmaps industriales mayormente lineales, sin mecanismo de auto-falsificación | Phase C cada trimestre Gate C debe revisitar radar, verificar estructura realmente más redonda |
| **Modelo de contrato 3-Phase + salidas Gate A/B/C** | Industria mayormente grandes contratos fixed-scope | Phase A diagnostic / Phase B strategy / Phase C implementation, cliente fasea decisiones |
| **Eje de escala vs eje de autonomía IA ortogonales** | La industria mezcla en un solo eje | L1-L3 escala + L4-L5 autonomía, frontera crítica L3→L4 |
| **RM 4 capas × L1-L5 coordenadas duales** | Industria uniaxial (RM o madurez) | Tiger AI exige cross-mapping dual-ejes |
| **Nodos HITL explícitos por Process** | La industria habla gobernanza, raramente especifica ubicación HITL | Tool 7.2 cada proceso explícitamente marcado con nodo HITL + criterios de acceptance |

---

## 7. Pregunta cliente común: ¿Entra en conflicto con nuestra metodología?

### 7.1 Cliente usa TOGAF / Zachman

**Sin conflicto**. Tiger AI 4 capas **se alinea directamente con TOGAF BDAT** (Business/Data/Application/Technology). Decir: «Construimos sobre vuestra arquitectura TOGAF existente, añadiendo la dimensión de adopción GenAI (L1-L5) y el closed loop radar trimestral.»

### 7.2 Cliente usa ITIL

**Sin conflicto**. Tiger AI Stage 8 Audit Log / Permission Matrix / Risk Register se conecta directamente a ITIL Service Operation. Decir: «Complementamos con logs de llamadas LLM GenAI-específicos, simulación Reviewer, gobernanza versiones Skill.»

### 7.3 Cliente usa CMMI

**Sin conflicto**. Tiger AI L1-L5 y CMMI 5 niveles **son parientes** — ambos extensiones de escuela maturity capability. Decir: «CMMI for AI es una dirección emergente; Tiger AI L1-L5 es una versión de aterrizaje.»

### 7.4 Cliente usa frameworks internos BCG / McKinsey / Bain

**Sin conflicto, refuerzo mutuo**. Tiger AI cita herramientas centrales de estas firmas (Issue Tree, MECE, Pyramid, Bain Way). Decir: «No reemplazamos vuestra metodología de consultoría estratégica; añadimos el closed loop de adopción GenAI y el Reference Model 4 capas.»

### 7.5 Cliente usa Gartner / Forrester AI Maturity

**Sin conflicto, más concreto**. Tiger AI L1-L5 tiene **herramientas de aterrizaje más concretas** que los 5 niveles de Gartner (L1=OpenWebUI, etc.). Decir: «Gartner dice ‹Operational AI›; nosotros decimos ‹n8n Workflow 3 live + tasa sign-off Reviewer 95%›.»

---

## 8. Alineación de citas académicas

Citas en References de cada archivo respectivo. Selección:

### 8.1 Escuela BPM / Maturity

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT. **(Raíz teórica central)**
- Paulk, M. et al. (1993). *Capability Maturity Model for Software*. CMU/SEI.
- Curtis, B. et al. (2009). *People CMM*.

### 8.2 Reference Model / Enterprise Architecture

- APQC (2024). *Process Classification Framework Version 7.3*.
- APICS / ASCM. *SCOR Reference Model*.
- TM Forum. *eTOM Business Process Framework*.
- ISACA. *COBIT / ITIL Framework*.
- The Open Group. *TOGAF Standard 9.2*.
- Zachman, J. *Zachman Framework*.
- Dragon1. *Enterprise Architecture Reference Model*.

### 8.3 Metodologías de consultoría

- Minto, B. (2009). *The Pyramid Principle*.
- Rasiel, E. (1999). *The McKinsey Way*.
- Bain & Company. *Bain Way / Results Delivery*.
- Iansiti, M., Lakhani, K. (2020). *Competing in the Age of AI*.

### 8.4 Change Management

- Kotter, J. (1996). *Leading Change*.
- Hiatt, J. (2006). *ADKAR*. Prosci.
- Mendelow, A. (1991). *Stakeholder Mapping*.

### 8.5 Estrategia GenAI

- Gartner. *AI Maturity Model*.
- Davenport, T., Mittal, N. (2022). *All-in on AI*.
- Brynjolfsson, E., McAfee, A. (2014). *The Second Machine Age*.

---

## 9. Cierre: Sobre hombros de gigantes + completión del closed loop de la industria

Filosofía de diseño de la metodología Tiger AI:

1. **Sin reinventar ruedas**: análisis estrategia (McKinsey), change mgmt (Kotter), herramientas financieras (NPV/IRR), frameworks EA (TOGAF/Dragon1) — usar lo mejor de la industria
2. **Integración + closed loop**: atar herramientas dispersas en una cadena de razonamiento completa con dependencias de datos, firmas del cliente y mecanismos de falsificación
3. **Llenar brechas GenAI**: frameworks industriales no han alcanzado la era LLM/Agent/Workflow → Tiger AI L1-L5 + 4 capas + Cases-as-Benchmarks + diseño HITL lo llena
4. **Reproducible por otros**: Apache 2.0 + GitHub + citas académicas claras → no activo privado de una firma

> **Este es el significado de «sobre hombros de gigantes + completión del closed loop de la industria»** — lo que los clientes compran es integración de lo mejor de la industria + completión de la era GenAI, no el método propietario de una sola firma.

---

## 10. Documentos relacionados

| Documento | Relación |
| --- | --- |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) §8 | Versión compacta de este documento §2 (vs McKinsey/BCG/Gartner/MIT) |
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | Cómo las 8 etapas realmente corren en un engagement real |
| [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md) | 50+ frameworks detallados (este documento = mapa de alineación; ese archivo = diccionario de frameworks) |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | Tablas de herramientas por etapa |

---

Licencia & Citación

Este documento está bajo Apache License 2.0; puede ser usado, modificado, comercializado, siempre que la atribución [`../NOTICE`](../NOTICE) sea preservada.
