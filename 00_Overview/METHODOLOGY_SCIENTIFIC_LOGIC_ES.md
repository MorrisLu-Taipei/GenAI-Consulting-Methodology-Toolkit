# Lógica científica de la metodología: Por qué este reporte resiste el debate

> 🌐 Idioma: [繁體中文](METHODOLOGY_SCIENTIFIC_LOGIC.md) ｜ [English](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) ｜ [Deutsch](METHODOLOGY_SCIENTIFIC_LOGIC_DE.md) ｜ [Français](METHODOLOGY_SCIENTIFIC_LOGIC_FR.md) ｜ Español ｜ [日本語](METHODOLOGY_SCIENTIFIC_LOGIC_JA.md) ｜ [한국어](METHODOLOGY_SCIENTIFIC_LOGIC_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Última actualización: 2026-05-15

---

> **Qué responde este documento**: ¿Por qué esta metodología está diseñada así? ¿Por qué 8 etapas, no 5 o 12? ¿Por qué los datos fluyen así? ¿Por qué los cases deben ser Benchmark-grade? **Finalmente**: cuando clientes / consejos / reguladores la desafían, ¿sobre qué base se sostiene este reporte de consultoría?
>
> **Afirmación central**: Esta metodología no es una colección de experiencia de consultoría sino una **lógica de management científico en closed loop** — cada paso satisface las cinco condiciones del método científico: observable, cuantificable, reproducible, falsable, auditable.

---

## 1. Por qué los reportes de consultoría necesitan «poder argumentativo científico»

Escenarios comunes de fracaso:

| Escenario | Desafío del cliente | Respuesta típica del consultor | Por qué falla |
| --- | --- | --- | --- |
| Cuestionamiento del consejo | «¿Cómo saben que estamos en L2?» | «Basado en nuestras entrevistas...» | Subjetivo; no verificable |
| Auditoría interna | «¿Por qué servicio al cliente antes que ventas?» | «Según nuestra experiencia...» | La experiencia es no auditable |
| Verificación regulatoria | «¿Quién es responsable si la IA falla?» | «Tenemos políticas...» | Políticas sin cadenas de auditoría no cuentan |
| Cambio de consultores | «La firma anterior dijo L3; ustedes dicen L2 — ¿quién tiene razón?» | «Métodos diferentes» | No reproducible = no científico |

**Objetivo de diseño de Tiger AI**: cada pregunta así tiene un **número verificable + evidencia auditable + procedimiento reproducible** como respuesta.

---

## 2. Cinco condiciones del método científico vs. esta metodología

| Condición científica | Definición | Cómo la metodología la cumple |
| --- | --- | --- |
| **1. Observable** | Conclusiones reposan en evidencia que otros pueden ver | Grabaciones Stage 1 + inventario de sistemas + As-Is Swimlanes; cada ítem con timestamp y fuente |
| **2. Cuantificable** | Conclusiones reducibles a números, no adjetivos | Scoring radar Stage 2 0-4; scoring Impact×Effort Stage 4; números de impact-surface 80/20 Stage 5; value tracking Stage 8 5 dimensiones |
| **3. Reproducible** | Diferentes consultores usando el mismo método obtienen conclusiones similares | Tres Reference Models (APQC / SCOR / Tiger AI L1-L5) son estándares públicos; banco de entrevistas 40 preguntas; disciplina MECE |
| **4. Falsable** | Conclusiones tienen condiciones de refutación explícitas | Stage 6 Stage Gate Criteria listan explícitamente pass/fail; checklists tienen condiciones observables; meta fallida = hipótesis refutada |
| **5. Auditable** | Proceso puede ser verificado independientemente por terceros | Stage 8 Audit Log (llamadas LLM, cambios de permisos, deploys Skill, sign-offs Reviewer cadena completa), retención definida |

> **Estas cinco condiciones no son decoraciones**. Cualquier conclusión de consultor que no pueda responder a estas cinco no es management científico — solo intercambio de experiencia.

---

## 3. Por qué exactamente 8 etapas (no 5, no 12)

Razonando hacia atrás desde el método científico: un reporte de transformación IA defendible **debe caminar a través de 5 acciones de razonamiento**, con dependencias de datos estrictas entre ellas:

| Acción de razonamiento | Mapea a Stage | Saltar causa |
| --- | --- | --- |
| **A. Observar estado actual** | Stage 1 As-Is | Sin baseline objetiva → todo lo después es adivinanza |
| **B. Aplicar coordenadas internacionales** | Stage 2 Reference Model | Sin coordenadas externas → «no somos suficientemente buenos» es opinión del consultor |
| **C. Cliente expande su propia Ideal Practice** | Stage 3 Best Practice | Sin meta firmada por cliente → cliente puede negar el gap |
| **D. Cuantificar gap** | Stage 4 Gap Analysis | Sin gap estructurado → no puede priorizar |
| **E. Converger problema central** | Stage 5 Problem Definition | Sin 80/20 → «todo es importante» = nada se hace |
| **F. Fijar metas absorbibles** | Stage 6 Phased Goals | Sin descomposición de fases → intento de perfección one-shot = fracaso |
| **G. Diseñar blueprint** | Stage 7 To-Be Design | Sin diagrama To-Be → Roadmap no aterrizará en org y sistemas |
| **H. Ejecutar & gobernar** | Stage 8 Implementation | Sin change mgmt + value tracking + Audit → blueprint es papel tapiz |

**Por qué exactamente 8**: cada acción de razonamiento es inseparable; **saltar una deja un desafío sin respuesta**.

- Saltar Stage 2 → «¿Cuál es tu estándar?» sin respuesta
- Saltar Stage 4 → «¿Por qué esto antes que aquello?» sin respuesta
- Saltar Stage 6 → «¿Por qué 9 meses no 3?» sin respuesta
- Saltar Stage 8 → «¿Cómo pruebas que mejoró?» sin respuesta

> 5 etapas es demasiado grueso (omite Reference Model, Phased Goals, Change Mgmt); 12 etapas es demasiado fino (sub-pasos redundantes). **8 es «la cadena de razonamiento debatible completa mínima.»**

---

## 4. Por qué los datos fluyen así (Razón científica para cada flecha)

```
Stage 1 ──────────► Stage 2 ──────────► Stage 3 ──────────► Stage 4
As-Is              Reference Model     Best Practice         Gap
realidad observada  coordenadas         Ideal del cliente     gap objetivo
                    internacionales     Practice (firmada)
                                                              │
                                                              ▼
Stage 8 ◄────────── Stage 7 ◄────────── Stage 6 ◄────────── Stage 5
Implementation      To-Be Design       Phased Goals          Problem
landing + change    blueprint futuro    pasos absorbibles     convergencia central
                                                              
        ↑                                                     ↓
        └─── Trimestralmente: revisitar Stage 2 radar (verificación closed-loop) ───┘
```

#### Por qué cada flecha es causalmente necesaria

| Flecha | Por qué esta dirección | Invertir causa |
| --- | --- | --- |
| **Stage 1 → 2** | Debe tener «realidad» antes de comparar contra «estándar» | Invertido: cherry-pick evidencia para encajar al estándar |
| **Stage 2 → 3** | Debe confirmar «estructura completa» antes de discutir «Ideal del cliente» | Invertido: Ideal salta gaps estructurales |
| **Stage 3 → 4** | Debe tener **Ideal Practice firmada por cliente** antes de calcular «Gap = (Ideal cliente − As-Is cliente)» | Sin firma del cliente, gap = opinión del consultor, refutable |
| **Stage 4 → 5** | Debe tener «todos los gaps» antes de convergencia 80/20 a «problema central» | Sin 4, definición de problema = adivinanza |
| **Stage 5 → 6** | Debe bloquear «problema central» antes de fijar «metas» | Sin 5, metas dispersan |
| **Stage 6 → 7** | Debe tener «metas faseadas» antes de diseñar «blueprint» | Sin 6, blueprint intenta one-shot |
| **Stage 7 → 8** | Debe tener «blueprint» antes de «ejecución» | Sin 7, ejecución es ciega |
| **Stage 8 ↑ Stage 2 (trimestral)** | Después de ejecución, revisitar «¿radar estándar más redondo?» | Sin loopback, PoCs hechos pero estructura no verificada |

> **Este es el significado científico de «closed loop»**: no «hecho es bueno» sino «resultados pueden ser verificados / falseados retroactivamente.»

---

## 5. Por qué Reference Model es 4 capas (no 3, no 5)

Derivado del eje «**abstracción × volatilidad**» de la madurez (ver [`CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 2.7):

| Abstracción | Volatilidad | Capa | Por qué no puede fusionarse u omitirse |
| --- | --- | --- | --- |
| Más abstracto | Años | **L1 Governance** | Estrategia y política no pueden mezclar con procesos (volatilidad difiere 10×) |
| Abstracto | Trimestres-Años | **L2 Business** | Funciones business no pueden mezclar con servicios de datos |
| Medio | Meses-Trimestres | **L3 Information** | Servicios de datos no pueden mezclar con hardware/redes |
| Más concreto | Semanas-Meses | **L4 Technical** | Hardware mezclado en capa Business bloquea decisiones tech |

**3 capas insuficiente**: usualmente descarta L3 Information → servicios de datos comprimidos en L2 o L4 → pérdida de foco.
**5 capas excesivo**: la capa extra es usualmente una sub-capa de L2 o L3 → viola MECE.

> **La escuela Dragon1 insiste en 4 capas** por esta razón científica. Tiger AI Enterprise AI Reference Model la sigue estrictamente.

---

## 6. Por qué los cases deben ser Benchmark-grade (no narrativos)

La ciencia requiere «**reproducibilidad**» — el mismo case leído por diferentes consultores / clientes debería rendir «estimaciones de gap» similares.

- **Case narrativo**: «Empresa X hizo inspección calidad IA y tuvo éxito» → no reproducible (cada lector interpreta diferente)
- **Case Benchmark-grade**: 9 campos obligatorios (industria + escala + L inicial + L final + duración + inversión + Wins + Failures + aplicabilidad) → **reproducible** (estimación gap/tiempo/presupuesto de cualquier lector cae en rango similar)

Ver Tool 3.5 Cases-as-Benchmarks.

> **Por esto todos los 7 cases Tiger AI siguen la misma plantilla 9 campos** — no por consistencia visual sino por la condición científica de **reproducibilidad**.

---

## 7. Checklist de «poder argumentativo científico» del reporte

Cuando clientes / consejos / reguladores hacen las siguientes preguntas, esta metodología tiene ubicaciones de respuesta específicas:

| Desafío | Ubicación respuesta | Evidencia |
| --- | --- | --- |
| «¿Cómo saben que estamos en L2?» | §3 As-Is + §4 RM Mapping | Grabaciones de entrevista, inventario de sistemas, radar RM 0-4 |
| «¿Por qué APQC / Tiger AI L1-L5?» | §4.1 + Tool 2.5 | Scorecard de calificación 10 condiciones |
| «¿Qué tan lejos estamos de nuestro ideal?» | §5 + §6.1 | **Tabla de definición Ideal Practice firmada por cliente** + Benchmark de case; Gap = (tu Ideal firmado − tu As-Is), ambos extremos son tus afirmaciones |
| «¿Por qué servicio al cliente antes que ventas?» | §6.2 + §6.3 | Matriz Impact × Effort + Score de Priorización |
| «¿Por qué el problema central es ‹asset-ización del conocimiento›?» | §7 | Números de impact-surface 80/20 + cadena 5 Whys |
| «¿Por qué 9 meses no 3?» | §8 + Tool 6.3 | Descomposición faseada + Organizational Absorption (6 dimensiones) + duración de case benchmark |
| «¿Y si el PoC falla?» | §13.2 | Risk Register + Triggers + Mitigation Owners |
| «¿Cómo pruebas que mejoró?» | §13.1 + revisión radar trimestral | Value Tracking 5 dimensiones + Stage 2 radar before/after |
| «¿Quién es responsable si la IA falla?» | §12.1 + Tool 8.8 | RACI + AI Ethics Checklist + Audit Log cadena completa |
| «¿Puede su metodología ser reproducida?» | Metodología entera | Apache 2.0 + GitHub + Tool 2.5 auto-calificación 9/10 |
| «El último consultor dijo L3, ustedes dicen L2 — ¿quién tiene razón?» | §3 evidencia de scoring | Escala 0-4 pública + cada score tiene evidencia observable → **verificable por terceros** |
| «¿Por qué exactamente 8 etapas?» | Este documento §3 | Argumento «cadena de razonamiento debatible completa mínima» |

> **El reporte se vuelve un documento debatible**: el cliente no «confía en la autoridad del consultor» sino «sigue la cadena de evidencia para alcanzar la misma conclusión él mismo.» Eso es management científico.

---

## 8. Comparación con metodologías de consultoría mainstream

| Metodología | Fortaleza | Falta (bajo lente de completitud científica) |
| --- | --- | --- |
| **McKinsey Issue Tree + Pyramid** | Razonamiento lógico riguroso, narrativa fuerte | Sin Reference Model (sin coordenadas); sin Phased Goals (sin descomposición de fases) |
| **BCG Digital Maturity** | Madurez 5 etapas clara | Sin Best Practice cuantificado (excelencia descrita por consultor); sin evaluación de absorción organizacional |
| **Gartner AI Maturity** | Reconocido en la industria | Sin disciplina de entrevista As-Is; sin benchmarks de case reproducibles |
| **MIT AI Capability** | Académicamente riguroso | Carece herramientas de landing Implementation & Change |
| **Tiger AI (esta metodología)** | **Cadena de razonamiento 8 etapas completa + Reference Model 4 capas + closed loop Cases-as-Benchmarks** | Nuevo (lanzado 2025, cases acumulando) |

> **No dice que otras metodologías son malas** — dice que cada una tiene fortalezas pero **closed loops incompletos**. El objetivo de diseño de Tiger AI es completar ese loop para que el reporte tenga **evidencia para cada oración desde la portada hasta la última página**.

---

## 9. Mérito de citación académica y regulatoria

Por qué esta metodología puede ser validada, citada, mejorada por comunidades académicas:

1. **Pública**: Apache 2.0, repo GitHub, bilingüe zh/en
2. **Auto-calificable**: Tool 2.5 auto-evaluación, 9 de 10 condiciones cumplidas
3. **Raíces teóricas transparentes**: escuela Rosemann BPM Maturity (QUT) + CMMI + APQC + Dragon1 EA cada uno citado
4. **Validado inter-industrias**: Manufactura / Hospital / Marketing / B2B / Financiero / Gobierno / Educación — 7 cases industriales (valida portabilidad)
5. **Falsable**: cada Stage Gate Criteria tiene condiciones de refutación
6. **Criticable**: este documento y Tool 2.5 ambos notan explícitamente «nuevo, reconocimiento acumulando»

> **El gold standard de la citación académica es «¿puede alguien más aplicar este método a un problema diferente y obtener conclusiones similares?»** — la metodología Tiger AI responde Sí, porque todos los pasos, herramientas y criterios de scoring son públicos.

---

## 10. Disciplina operacional para consultores

Cuando escribes este reporte, cada párrafo debe responder:

```
¿Cuál es la evidencia para esta afirmación?         ← Observable
¿Cómo se calculó este número?                        ← Cuantificable
¿Otro consultor obtendría lo mismo?                  ← Reproducible
Si esto es incorrecto, ¿qué vería?                   ← Falsable
¿Quién ha firmado este proceso?                      ← Auditable
```

**Responder los 5 → ese párrafo es management científico**.
**Cualquier insrespondible → ese párrafo es opinión personal; suplementar evidencia o eliminar.**

---

## 11. Promesa a los clientes

Esta metodología promete:

1. **Cada conclusión tiene evidencia numerada** — Apéndices A-G completamente rastreables
2. **Cada número tiene fórmula de cálculo** — sin «basado en juicio del consultor»
3. **Cada recomendación tiene Stage Gate Criteria** — puedes verificar
4. **Cada riesgo tiene Trigger + Owner + Mitigation** — puedes gestionar
5. **Cada case es Benchmark-grade** — puedes auto-calcular el gap
6. **Cada fin de fase revisita el radar Reference Model** — ves la estructura volviéndose realmente más redonda

**Si algún párrafo se siente como «autoridad del consultor decide», señálalo. Añadiremos evidencia, revisaremos la fórmula, o eliminaremos.**

---

## 12. Cierre: Esta metodología en sí misma es un Reference Model

Una observación auto-referencial final:

- Esta metodología aplica las 10 condiciones de Tool 2.5 para **auto-evaluar**: 9 de 10 cumplidas (condición 6 «reconocimiento industrial amplio» todavía acumulando)
- Esta metodología aplica las 5 preguntas de derivación de Tool 2.6 para **auto-inventariar componentes**: 8 etapas + 4 capas + 5 dimensiones de tracking todas presentes
- Esta metodología aplica la arquitectura 4 capas de Tool 2.7 para **auto-organizarse**: Governance (este doc) + Business (Stages 1-8) + Information (toolkit + cases) + Technical (repo GitHub + AGENTS.md + CLAUDE.md)
- Esta metodología aplica Cases-as-Benchmarks de Tool 3.5 para **auto-probar reproducibilidad**: 7 cases industriales todos siguen la plantilla 9 campos

> **Esto es el closed loop del management científico**: una metodología no solo analiza otros, sino **puede analizarse a sí misma con sus propias herramientas** — en academia llamada «consistencia auto-referencial», la marca de la teoría rigurosa.

---

## Referencias

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- APQC (2024). *Process Classification Framework Version 7.3*.
- CMMI Institute (2018). *CMMI for Development V2.0*.
- Dragon1 (n.d.). *Enterprise Architecture Reference Model*. <https://www.dragon1.com/reference-models/enterprise-architecture-reference-model>
- Pyramid Principle: Minto, B. (2009). *The Pyramid Principle*.
- 80/20: Koch, R. (1997). *The 80/20 Principle*.
- 5 Whys: Ohno, T. (1988). *Toyota Production System*.
- Change Management: Kotter, J. (1996). *Leading Change*. Prosci ADKAR.

---

Licencia & Citación

Este documento está bajo Apache License 2.0; puede ser usado, modificado, comercializado, siempre que la atribución [`../NOTICE`](../NOTICE) sea preservada.
