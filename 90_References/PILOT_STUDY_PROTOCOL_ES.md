# Pilot Study Protocol: Plan de investigación de validación empírica para la metodología Tiger AI

> 🌐 Idioma: [繁體中文](PILOT_STUDY_PROTOCOL.md) ｜ [English](PILOT_STUDY_PROTOCOL_EN.md) ｜ [Deutsch](PILOT_STUDY_PROTOCOL_DE.md) ｜ [Français](PILOT_STUDY_PROTOCOL_FR.md) ｜ Español ｜ [日本語](PILOT_STUDY_PROTOCOL_JA.md) ｜ [한국어](PILOT_STUDY_PROTOCOL_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Última actualización: 2026-05-16
Versión: v1.0 Research Design Protocol (pre-registration ready)

---

> **Propósito**: Evolucionar la metodología Tiger AI de un "framework de consultoría bien diseñado" a un "modelo investigable". Este protocolo define un estudio piloto empírico de 18-24 meses, con 5-10 empresas, **sometiendo la metodología a falsificación externa en lugar de solo auto-validación**.
>
> Este es un **documento de diseño de investigación** listo para sumisión IRB / pre-registration académica / aplicaciones a subvenciones gubernamentales de investigación.

---

## 1. Antecedentes & Motivación

### 1.1 Por qué investigación empírica

Fuerza de evidence actual de la metodología Tiger AI:

| Elemento | Evidence Level (Tool 8.9) | Estado |
| --- | --- | --- |
| Diseño del flow de 8 etapas | L2 argumento documental | Completo (Rosemann BPM + integración de frameworks industriales) |
| 6 constructs × escala 0-4 | L2 consenso de expertos | Completo (**sin validación psicométrica**) |
| Biblioteca de 7 casos | L2 composite anonimizado | Completo (**no datos longitudinales reales**) |
| Self-qualification (Tool 2.5) | L1 self-report | Completo (**auto-referencial, no validado externamente**) |
| Inter-rater consistency | — | **No hecho** |
| Respuesta KPI longitudinal a la metodología | — | **No hecha** |

**Conclusión**: La metodología es madura en "cohesión interna + cierre lógico" pero no ha sido probada empíricamente por "reproducibilidad externa + validez predictiva". Este estudio piloto aborda ambos.

### 1.2 Preguntas de investigación

**RQ1 — Inter-rater Reliability**: ¿Pueden diferentes consultores usando el mismo método scorear la misma empresa de manera consistente?

- **H1**: Cohen's κ ≥ 0.60 (substantial agreement)

**RQ2 — Cohesión interna**: ¿Qué tan internamente cohesivos son los 6 constructs?

- **H2**: Cronbach's α ≥ 0.70 por construct

**RQ3 — Validez de construct**: ¿Emergen los 6 constructs limpiamente en análisis factorial?

- **H3a**: EFA extrae 5-6 factores; cada item carga ≥ 0.5 en su factor asignado
- **H3b**: CFA modelo 6-factores fit: CFI ≥ 0.90, TLI ≥ 0.90, RMSEA ≤ 0.08

**RQ4 — Validez predictiva**: ¿Pueden los scores T0 predecir mejora KPI business a T+12 meses?

- **H4**: Controlando por KPI baseline y tamaño de empresa, el score de madurez Tiger AI predice positivamente mejora KPI a +12m (β ≥ 0.30, p < 0.05)

**RQ5 — Patrón longitudinal**: ¿Las empresas completando Phase C 24 meses muestran radares "más redondos"?

- **H5**: T0 vs T24 área de radar (suma 6-construct) aumenta significativamente, y el crecimiento de cada construct sigue la descomposición Tool 6.1 (foundation → optimization → excellence)

---

## 2. Diseño del estudio

### 2.1 Tipo de diseño

- **Estudio longitudinal mixed-methods**
- **Convergent parallel design**: cuantitativo (scale scoring, KPIs) + cualitativo (entrevistas semi-estructuradas, case studies) simultáneamente
- **Pre-registered** (hipótesis públicas, sampling, plan de análisis; evitando p-hacking)

### 2.2 Sample

| Item | Especificación |
| --- | --- |
| **Sample N objetivo** | 5-10 empresas (etapa piloto; main study N=200+ para CFA) |
| **Diversidad de industria** | ≥ 3 industrias (≥ 1 cada una de mfg, servicios, sector público) |
| **Tamaño de empresa** | 100-5000 empleados |
| **Punto de partida IA** | L0-L2 (ya L3+ excluido por espacio de intervención limitado) |
| **Duración de commitment** | 18 meses (acuerdo de colaboración de investigación) |
| **Incentivo** | Consultoría gratuita / descontada + oportunidad de co-publicación + control de anonimización de casos |

### 2.3 Estrategia de reclutamiento

1. Vía comunidad n8n Taipei Ambassador, redes de clientes empresariales, instituciones partner académicas (partners específicos divulgados tras firma MOU)
2. Solicitación pública + repo Apache 2.0 abierto como señal de confianza
3. Acuerdo de colaboración de investigación firmado (uso de datos, anonimización, mecanismo de exit)

### 2.4 Ética / IRB

- Aplicar para aprobación IRB de institución partner académica (partner divulgado tras firma MOU)
- Consentimiento informado: todos participantes por escrito
- Manejo de datos sensibles: grading PII / secreto de negocio; aislamiento de datos double-blind
- Derecho a retirar: cualquier empresa puede salir en cualquier momento; datos recolectados devueltos o destruidos

---

## 3. Diseño de scoring double-blind

### 3.1 Propósito

Validar **inter-rater reliability** del modelo de scoring Tiger AI.

### 3.2 Diseño

```
Fase de scoring T0 (por empresa):
  ↓
  Consultor A completa independientemente:
    • Entrevistas (Tool 1.1 40-Q bank)
    • Inventory + Swimlane (Tools 1.2-1.4)
    • Reference Model Mapping (Tool 2.2)
    • 6-construct 0-4 scoring (Tool 2.3)
    • Juicio primario de madurez (L1-L5)
  ↓
  Consultor B completa independientemente (misma empresa, blinded a A):
    • Repetir todas acciones anteriores
  ↓
  Analista de investigación (neutral) compara A vs B:
    • Gap de score 6-construct (weighted kappa)
    • Agreement de juicio primario de madurez (unweighted kappa)
    • Overlap de identificación de gap (overlap tabla M/B/R)
```

### 3.3 Estadísticas de consistencia

| Métrica | Tool | Interpretación |
| --- | --- | --- |
| **Cohen's κ (unweighted)** | κ = (Po - Pe) / (1 - Pe) | < 0.20 slight; 0.21-0.40 fair; 0.41-0.60 moderate; 0.61-0.80 substantial; > 0.80 almost perfect |
| **Weighted κ (linear / quadratic)** | Para escala ordinal (0-4) | Como arriba, pero más estricto en "1 punto off" vs "4 puntos off" |
| **ICC (Intraclass Correlation)** | Modelo mixto two-way | < 0.5 poor; 0.5-0.75 moderate; 0.75-0.9 good; > 0.9 excellent |
| **Bland-Altman plot** | Visualizar gap de score | Detectar bias sistemático |

---

## 4. Tracking longitudinal de KPI

### 4.1 Timepoints de medición de KPI

| Timepoint | Nombre | Medición |
| --- | --- | --- |
| **T0** | Baseline | Después Phase A, antes Phase B |
| **T+6m** | Fin Phase 1 | L1 Gate Acceptance |
| **T+12m** | Medio Phase 2 | L2/L3 Gate |
| **T+18m** | Fin Phase 2 | L3 completo |
| **T+24m** | Fin Phase 3 | L4/L5 Gate |

### 4.2 5 dimensiones KPI (por Tool 8.5 Value Tracking)

| Dimensión | KPIs ejemplo |
| --- | --- |
| **Time** | Complaint response, proposal turnaround, month-end close, decision cycle |
| **Quality** | Tasa de defecto, tasa de error, complaint count, rework rate |
| **Scale** | Throughput, beneficiaries, automated task count |
| **Risk** | Missed case rate, compliance violations, sensitive-data leakage |
| **Assets** | Skill count, Wiki entries, Agent task count, training completion |

### 4.3 Calidad de datos KPI (por Tool 8.9 Evidence Hierarchy)

- **L3 obligatorio**: Todos los KPIs time / scale de system logs (n8n / Audit Log / ERP)
- **L4 recomendado**: Sample-verificado por internal audit / external accountants
- **L1-L2 suplementario**: Employee NPS / interview summaries

---

## 5. Cualitativo: Entrevistas semi-estructuradas

### 5.1 Timepoints de entrevista

Por empresa: T0, T+6m, T+12m, T+18m, T+24m — 1 ronda cada uno (por entrevistado).

### 5.2 Entrevistados

- CEO / Sponsor
- AI Champion
- IT Lead
- ≥ 2 Department Heads
- ≥ 3 Front-line Users

### 5.3 Preguntas de entrevista (extracto)

1. ¿Cuál es el cambio IA más impactful de los últimos 6 meses?
2. ¿Qué cambios IA esperados no ocurrieron? ¿Por qué?
3. ¿Ha cambiado la actitud del personal / departamento hacia IA?
4. ¿Recomendaría / no recomendaría esta metodología a pares?
5. ¿Qué Stage / Tool fue más útil? ¿Menos?
6. Cross-time: mirando atrás al Ideal Practice firmado hace 12 meses, ¿algún arrepentimiento?

### 5.4 Análisis cualitativo

- Transcripción verbatim + coding (NVivo / Atlas.ti)
- Reliability dual-coder ≥ 80%
- Análisis temático para extraer patterns / counter-examples

---

## 6. Plan de análisis estadístico

### 6.1 Estadísticas descriptivas

- Distribución de score por construct (mean, SD, median, IQR)
- Visualización radar chart T0 vs T24
- Matriz de correlación 6-construct (check de multicolinealidad)

### 6.2 Reliability & Validity

| Análisis | Tool | Mapea a hipótesis |
| --- | --- | --- |
| Cronbach's α | SPSS / R `psych::alpha()` | H2 |
| EFA + Bartlett's + KMO | SPSS / R `psych::fa()` | H3a |
| CFA + fit indices | Mplus / R `lavaan::cfa()` | H3b (**N ≥ 200 requerido**) |
| Cohen's κ | R `irr::kappa2()` | H1 |
| ICC | R `irr::icc()` | H1 |

### 6.3 Estadísticas inferenciales

| Análisis | Hipótesis | Tool |
| --- | --- | --- |
| Paired t-test (T0 vs T24) | H5 aumento área de radar | R `t.test(paired=TRUE)` |
| Mixed-effects model | H4 validez predictiva | R `lme4::lmer()` |
| ANCOVA | Controlar KPI baseline + size | R `aov()` |
| Análisis de sensibilidad | Contra missing data + dropout | R `mice` multiple imputation |

### 6.4 Significancia & Ajuste

- α = 0.05 test principal
- Bonferroni correction para multiple comparisons
- Reporting de effect size: Cohen's d, η², partial η²

---

## 7. Timeline & Milestones

```
Mes 0:     Finalizar diseño + sumisión IRB
Mes 1-3:   Reclutar 5-10 empresas + firmar acuerdo de investigación
Mes 4:     Entrenar Consultor A/B (SOP double-blind)
Mes 5-6:   Scoring double-blind T0 + medición KPI Baseline
Mes 6-12:  Intervención Phase 1 + scoring T+6m + entrevistas
Mes 12-18: Intervención Phase 2 + T+12m + T+18m
Mes 18-24: Intervención Phase 3 + scoring final T+24m + entrevistas
Mes 24-27: Análisis + reporte de investigación + sumisión journal
Mes 27-30: Revisiones + sumisión
```

---

## 8. Estimación de presupuesto

| Item | Est. (NT$) |
| --- | --- |
| Tiempo de consultor (A + B 80-120 hrs cada uno por empresa) | 6-9M |
| Personal de investigación (comparación de scoring neutral + análisis cualitativo) | 1.5-2.5M |
| Herramientas KPI system-log + transcripción de entrevista | 0.5-1M |
| IRB / legal / consultor estadístico | 0.5-1M |
| Herramientas open-source + cloud data store | 0.3-0.5M |
| Contingencia (15%) | 1.3-2M |
| **Total** | **NT$ 10.1-16M** |

⚠️ A cambio de consultoría gratuita, 5-10 empresas se comprometen a 18 meses de colecta de datos → labor de consultor offsetable por "equivalent consulting service", **outlay cash real reducible a NT$ 4-7M**.

---

## 9. Estrategia de publicación

### 9.1 Outputs esperados

| Output | Journal / Plataforma | Timing est. |
| --- | --- | --- |
| **Pre-registration** | OSF | Mes 0 |
| **Protocol paper** | BMJ Open / Pilot and Feasibility Studies | Mes 3 |
| **Methodology paper** | MIS Quarterly / Information Systems Research / Journal of Business Research | Mes 27 |
| **Industry white paper** | Bilingüe, público Apache 2.0 | Mes 27 |
| **Case studies (anonimizados)** | HBR-style cases | Mes 30 |
| **Practitioner guide** | Actualizar toolkit + agregar evidence empírica | Mes 30 |

### 9.2 Commitment Open Science

- Todos los datos de investigación (de-identificados) públicos en OSF
- Scripts estadísticos R / Python en GitHub
- Identidad de entrevistado confidencial; resultados agregados totalmente transparentes

---

## 10. Riesgos & Mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
| --- | --- | --- | --- |
| Withdrawal de empresa a medio camino (dropout) | Med | High | Over-reclutar 12; análisis intention-to-treat |
| Bias / leakage Consultor A/B | Low | High | Entrenamiento SOP + audits + double-blind estricto + diferentes oficinas |
| KPI system log inaccesible | Med | Med | T0 IT confirma disponibilidad de log; indicadores sustitutos si no |
| Retraso de revisión IRB | Med | Med | Sumisión IRB Mes 0 concurrente con reclutamiento |
| N insuficiente para CFA | High | Med | EFA en piloto; CFA espera main study N=200+ |
| Shortfall de presupuesto | Med | High | Aplicar grants gubernamentales (NSTC / MOE etc.) / grants partner académicos; cost-sharing multi-empresa |

---

## 11. Stopping Rules

Terminación temprana con disclosure completo si:

- ≥ 50% empresas se retiran
- Inter-rater κ < 0.40 (metodología incoherente → scale necesita rediseño)
- IRB revocado
- Issues éticos serios (data leak, participant harm)

**Estudios terminados temprano deben aún publicar todos los datos recolectados** (evitando publication bias).

---

## 12. Contribuciones esperadas

| Contribución | Audiencia | Forma |
| --- | --- | --- |
| **Teoría**: primer modelo de madurez de adopción GenAI empíricamente validado | Academia (IS / BPM / Strategy) | Paper peer-reviewed |
| **Método**: Cases-as-Benchmarks + protocolo de workshop Client Ideal Practice | Industria de consultoría | Toolkit open-source (Apache 2.0) |
| **Política**: evidence empírica para alignment AI Governance | Regulatorios (Taiwan AI Basic Act / NIST / EU) | White paper + audiencias legislativas |
| **Industria**: 5-10 casos reales longitudinales de empresa | Clientes pares | Casos reales (reemplazando composites) |
| **Educación**: integrar en curricula partners académicos | Estudiantes | Materiales de curso |

---

## 13. Documentos relacionados

| Documento | Relación |
| --- | --- |
| [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) §3.1-3.3 | Definiciones de constructs de scale; este estudio valida |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Por qué la metodología necesita validación empírica |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | Failure modes conocidos → mitigación construida en este estudio |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9 | Base Evidence Hierarchy para grading de evidence KPI |

---

## 14. Referencias

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297-334.
- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- Streiner, D. L., Norman, G. R., & Cairney, J. (2015). *Health measurement scales: A practical guide to their development and use* (5th ed.). Oxford University Press.
- Hair, J. F., et al. (2019). *Multivariate Data Analysis* (8th ed.). Cengage.
- Creswell, J. W. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). SAGE.
- Open Science Framework: <https://osf.io/>

---

Licencia & Citación

Este documento es Apache License 2.0; puede usarse, modificarse, comercializarse, siempre que se preserve la atribución [`../NOTICE`](../NOTICE). Otros equipos de investigación pueden **adoptar, modificar, replicar libremente** este diseño, siempre que sigan los mismos commitments de pre-registration y open-science.
