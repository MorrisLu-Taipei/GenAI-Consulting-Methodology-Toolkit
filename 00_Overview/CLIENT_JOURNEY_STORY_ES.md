# La historia de Ming: una transformación IA de 24 meses en una fábrica de empaque

> 🌐 Idioma: [繁體中文](CLIENT_JOURNEY_STORY.md) ｜ [English](CLIENT_JOURNEY_STORY_EN.md) ｜ [Deutsch](CLIENT_JOURNEY_STORY_DE.md) ｜ [Français](CLIENT_JOURNEY_STORY_FR.md) ｜ Español ｜ [日本語](CLIENT_JOURNEY_STORY_JA.md) ｜ [한국어](CLIENT_JOURNEY_STORY_KR.md)
>
> Una historia de 20 minutos que te ayuda a entender la metodología de 8 etapas. Sin tablas de herramientas, sin acrónimos, sin jerga de consultor.

Apache License 2.0 · Autor: Morris Lu · Tiger AI

Última actualización: 2026-05-15

---

> ⚠️ **Aviso importante de integridad académica**
>
> **"Ming" y "MingChang Packaging" son personajes ficticios y una empresa ficticia generados por IA, NO reales**. Esta historia es material didáctico diseñado para ayudar a lectores no técnicos a entender rápidamente la metodología de 8 etapas. Todos los números (tamaño de la empresa, KPIs, presupuestos, calendarios, porcentaje de caída de pedidos del Cliente A) son solo ilustrativos.
>
> - Según [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9, este es un **Caso pedagógico L0 simulado por IA** (bajo L1)
> - Los casos longitudinales reales solo existirán después de que se complete el estudio empírico de 18-24 meses en [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md)
> - Esta historia **NO debe** usarse como marketing externo de "tenemos un cliente real que hizo esto"

---

## Conozcan al protagonista

**Ming**, 55, Presidente de MingChang Packaging.
Ubicado en Hsinchu, 700 empleados, packaging y testing de semiconductores, NT$ 1.2B de ingresos anuales.
Su padre fundó la empresa con una sola wire bonder en los años 90; Ming tomó el relevo en 2010 y la hizo crecer hasta convertirla en proveedor de nivel medio del gran Cliente A.
Ming está orgulloso de dos cosas: su hija entró a NTU, y su empresa no ha perdido dinero en 10 años.

Pero a principios de 2025, empezó a perder el sueño.

---

## Capítulo 1 ── "Pensé que no estábamos tan mal"

### Un correo

Enero 2025. El director de compras del Cliente A escribe: "La velocidad de respuesta a quejas y de propuesta de MingChang está muy por detrás de nuestros otros proveedores. Los pedidos del próximo trimestre serán recortados en 18%."

Ming lo lee tres veces.

"5 días de respuesta a quejas es normal en nuestra industria", murmura.

"Hace años solo daban 7 días."

Esa tarde, su secretario encuesta a los pares. **Los líderes de la industria responden a quejas en 1 día. Tasas de defectos 40% más bajas que MingChang.**

Ming busca en línea. Tres competidores directos han desplegado "inspección de calidad IA" y "Agents IA de quejas".

"¿Pueden permitírselo? ¿Podemos nosotros?" Llama a Lin, el VP de IT.

Lin hace una pausa. "Presidente, ni siquiera tenemos una cuenta de ChatGPT empresarial. Los empleados la usan en privado, quemando NT$ 24,000/mes en tarjetas de crédito personales. Los datos probablemente están filtrándose por todos lados."

Ming guarda silencio.

---

### Ese repo en GitHub

Esa noche, Ming sigue en la oficina a las 11 pm.

Prueba una cuenta ChatGPT y pregunta: "¿Cómo hace un manufacturero mediano una transformación IA?"

ChatGPT responde: "Puedes consultar la metodología de consultoría open-source Tiger AI: GenAI Consulting Methodology Toolkit."

Ming hace clic en GitHub y ve un "Executive Summary de 5 minutos."

Después de 5 minutos de lectura, hace algo que nunca ha hecho — **abre un quiz online de 10 preguntas y lo llena él mismo**.

### Las 10 preguntas

Cada pregunta le da tres escenarios en 0/2/4 para elegir:

- ¿Tus empleados usan IA? (0 = ninguno / 2 = ejecutivos personalmente / 4 = toda la empresa con cuentas corporativas)
- ¿Los patrones de uso de IA se sedimentan en templates reutilizables? (0 = no / 2 = algunos ejecutivos guardan los suyos / 4 = la empresa tiene Skill Library)
- ¿Los procesos empresariales tienen automatización inter-sistemas? ...

Ming responde honestamente.

Cuando envía, aparece un **gráfico radar**.

Máximo 24 puntos. MingChang saca 5.

**Dos de los seis ejes están en 0**: "sedimentación de conocimiento" y "aplicación de Agent."

Ming mira fijamente las dos hendiduras hacia adentro por largo rato.

"Pensé que no estábamos tan mal."

---

## Capítulo 2 ── El consultor llega (Phase A Diagnóstico, 2 semanas)

A la mañana siguiente Ming pide a su secretario llamar a Tiger AI.

Firma **Phase A: Diagnóstico, 2 semanas, NT$ 800K**.

Ming pregunta: "¿Cuánto por la transformación completa de 24 meses?"
Consultor Chang dice: "Primero hagamos estas 2 semanas. Después del reporte, decides si firmas la próxima fase."

Ming asiente. **Es la primera vez en su vida que un consultor dice "primero ver, después decidir."**

### Semana 1: hacen preguntas

Consultor Chang llega Día 1 con un **banco de entrevista de 40 preguntas**.

Día 1: CEO, COO, CIO — 60 min cada uno.
Día 2: jefes de departamento (QC, Sales, CS, IT, HR) — 90 min cada uno.
Día 3: primera línea (3 trabajadores de línea, 3 reps de ventas, 3 reps de CS) — 30 min cada uno.

Ming pregunta: "¿Los consultores siempre entrevistan tan largo? Pensé que solo darían recomendaciones."
Chang: "Ni siquiera hemos juzgado si IA es necesaria. **Escuchamos primero**."

Tarde del Día 3, el capataz de línea Old Chen viene a Ming:

"Jefe, ese consultor me preguntó cuáles son mis 5 tareas diarias más repetitivas. Mientras hablaba, me di cuenta — **3 de ellas las he hecho diario por 25 años, nunca escritas**. Cuando me jubile, ¿quién las sabrá?"

Algo se mueve en el pecho de Ming.

### Fin de semana 1: dibujan imágenes

Día 4: Consultor y Lin listan **cada herramienta IA jamás usada en la empresa** (incluidas privadas). 7 herramientas. NT$ 42,000/mes total — **todas en tarjetas personales de empleados**. Fronteras de datos borrosas.

Día 5: tres "**mapas de proceso reales**" (Swimlanes): "RFQ-a-envío," "Respuesta a quejas," "Reporte de anomalías de proceso." Cada paso marcado con puntos de densidad de dolor (0-3).

Ming mira "RFQ-a-envío":

```
Cliente envía RFQ       → 30% perdidos  ●●● dolor
Sales revisa ERP        → lento+errores ●●● dolor
Sales redacta cotización → copia manual ●●  dolor
Manager revisa cotización → espera      ●●  dolor
......
Total: 4-7 días hábiles promedio
Líder de industria: 4 horas
```

Ming: "Pensé que éramos rápidos. Los líderes de la industria están en 4 horas."

### Semana 2: aplican estándares internacionales

Semana 2, Chang hace algo que Ming nunca ha visto a consultores hacer.

Chang saca **tres frameworks de estándares internacionales**:

1. **APQC PCF** — "clasificación de proceso inter-industrias" del American Productivity & Quality Center (13 Categorías)
2. **SCOR** — "modelo de referencia manufacturero" del Supply Chain Council (Plan/Source/Make/Deliver/Return/Enable)
3. **Tiger AI L1-L5** — madurez de adopción GenAI (L1 individual / L2 dept / L3 inter-dept / L4 asistente IA / L5 equipo IA)

Él **mapea cada proceso y sistema real en MingChang a las celdas de estos tres estándares**.

Tarde del Día 8, Chang muestra a Ming **dos gráficos radar**:

- Chart 1: completitud de 13 Categorías APQC
- Chart 2: madurez Tiger AI L1-L5

Ming nota **4 celdas en 0**:

- APQC 11.x Knowledge Management = 0
- APQC 8.x IT Governance = 1
- Tiger AI L1 = 0
- Tiger AI L2 = 0
- Tiger AI L3 = parcial

"**Esto no es opinión del consultor. Estándares internacionales dicen que les faltan estas.**" — Chang.

Ming lleva los radares a casa a su esposa.

Ella dice: "¿Tu empresa realmente no tiene nada en esas celdas?"
Ming: "Lo descubrí solo hoy."

### Fin de semana 2: Reporte de evaluación de mid-engagement

Día 14. Reporte de mid-engagement (10+ páginas) entregado:

- Hallazgos de entrevistas
- Mapa de sistemas + riesgo de Shadow IT
- 3 mapas de proceso reales
- Dos gráficos radar (MingChang vs estándar)
- 3 perfiles de casos de industria (solo materiales, sin conclusiones)

**Sin recomendación sobre "qué hacer."**

Ming presenta este reporte en la junta del directorio.

El directorio ve los radares. 30 segundos de silencio.
Vicepresidente: "¿Realmente tenemos 0 en estas celdas?"
Ming: "Sí."
Vicepresidente: "¿Entonces cómo cruzaron las empresas pares estos ceros?"
Ming: "En la próxima fase el consultor nos mostrará 3 casos pares."

El directorio aprueba inmediatamente **Phase B: Estrategia, 4 semanas, NT$ 2M**.

---

## Capítulo 3 ── Elegimos en qué queremos convertirnos (Phase B Estrategia, 4 semanas)

### Ese workshop crítico de medio día

Semana 3, miércoles 9 am. Sala de conferencias.

CEO Ming, COO, VP IT Lin, jefe QC, jefe Sales, jefe CS, jefe HR — 7 personas.

Chang ha pegado un **diagrama de arquitectura de 4 capas** tamaño A2 (Governance / Business / Information / Technical) en la pared.

**Paso 1 (30 min)**: Chang muestra 3 casos pares — packager de semiconductores 700 personal 9 meses, hospital 1,200 personal 12 meses, agencia de marketing 800 personal 14 meses.

"**Solo estoy mostrando materiales. NO recomiendo** cuál deberían imitar."

**Paso 2 (45 min)**: Cada persona escribe **independientemente** notas adhesivas — "lo que quiero que nuestra empresa haga en 12 meses." Cada nota debe ser "verbo + métrica cuantificada."

Sin discusión. Escritura silenciosa por 45 minutos.

**Paso 3 (60 min)**: Todas las notas pegadas en la pared de arquitectura de 4 capas.

Pasa algo asombroso — 7 personas **independientemente** escribieron notas con **80% de solapamiento**:

- Respuesta a quejas 5 días → 1 día (5 notas)
- Turnaround de propuestas 4 días → 1 día (4 notas)
- Anomalía de proceso → hipótesis ≤ 1 hr (3 notas)
- Sedimentación de conocimiento: ≥ 20 Skills/mes (6 notas, incluyendo Ming)

"**Ese es el consenso de tu empresa**." — Chang.

**Paso 4 (45 min)**: Reality check. Chang interviene por primera vez, saca "Organizational Absorption Assessment" (6 dimensiones).

"Su tope de presupuesto es NT$ 8M por 24 meses. ¿Puede soportar estos 8 objetivos?"
"Su IT tiene 2 FTE; ¿pueden integrar ERP en Q2?"

Las 7 personas comienzan a **recortar su propia lista** — "anomalía de proceso 30 min no es factible, cambiar a 1 hr"; "Skill 30/mes demasiados, cambiar a 20."

Lista final: **8 objetivos claros, alcanzables, cuantificables**.

**Paso 5 (30 min)**: Escribir en la "**Ideal Practice Definition Table**" — cada objetivo tiene: capability correspondiente, estado a 12 meses, criterio de evidence.

**Paso 6 (15 min)**: **Ming, Vicepresidente (Sponsor), VP IT Lin (AI Champion) — firma de tres partes**.

Después de firmar, Ming nota que su mano tiembla.

"**Es la primera vez en mi vida que el objetivo no fue fijado por un consultor. Lo firmé yo mismo**," piensa.

---

### Las próximas 3 semanas: lo que firmas, no puedes negar

Las 3 semanas siguientes, el consultor hace algo simple:

**Fin de Semana 3**: Resta: **Gap = (Tu ideal firmado − Tu estado actual)**. Cada ítem con números específicos.

Ming ya no puede decir "esto no es lo que queremos" — lo firmó.

**Semana 4 temprano**: 80/20 + 5 Whys para encontrar la **causa raíz**.

El resultado deja a Ming atónito:

> 80% de los gaps rastrean a una causa raíz: a MingChang **le falta el rol, la herramienta y el incentivo para "asset-ización de conocimiento."**
>
> Quejas lentas, cotizaciones lentas, procesos lentos, onboarding lento — todo viene de "hacer lo mismo repetidamente, nadie sedimenta, nadie reutiliza."

Ming: "Entonces lo que nos falta no es IA. Nos falta **alguien responsable de hacer que el conocimiento sea capturable, encontrable, reutilizable**?"
Chang: "**IA es solo una herramienta. La causa raíz es diseño organizacional**."

**Semana 4 tarde**: Descomponer el objetivo final en **tres fases**:

- **Phase 1 (0-6 mo) Foundation**: cuentas OpenWebUI a nivel empresa + 5 Skills core
- **Phase 2 (6-15 mo) Optimization**: Skill Library 15 + n8n Workflow 3 en producción
- **Phase 3 (15-24 mo) Excellence**: 1 Hermes Agent + 1 ensayo inter-dept ClawTeam

Evaluación de absorción organizacional encuentra: IT solo tiene 2 FTE; Phase 2 no cabe → extender 6 → 9 meses.

**Esta decisión Ming la tomó él mismo, no por recomendación del consultor**.

### Fin de Phase B: Firmar Phase C

Día 32. **Reporte de consultoría completo de 30+ páginas** entregado:

- Estructura estándar de 14 secciones
- Ideal Practice Definition Table (versión firmada por 3 partes)
- Gap Matrix + ranking de prioridad
- Roadmap de 3 fases + checklists de Stage Gate
- Change Management Plan + Playbook de resistencia
- Matriz Value Tracking de 5 dimensiones
- Risk Register + AI Ethics Checklist

Ming lleva el reporte al directorio.

Vicepresidente hojea 5 minutos, pregunta: "¿Por qué 24 meses?"
Ming abre en §8.3: "Evaluación de absorción organizacional. Yo decidí."
Vicepresidente: "¿Por qué customer service primero?"
Ming abre en §6.2: "Impact 4, Effort 1, Strategic Fit 5, score total 20, #1."

Vicepresidente: "Convencido. Firma."

**Phase C: Implementación, 24 meses, NT$ 7M**.

---

## Capítulo 4 ── 24 meses después (Phase C Implementación)

### Mes 3: Primer quick win

Phase 1 arranca. 3 meses dentro, pasa algo inesperado.

Primer n8n Workflow en producción — auto-clasificación de quejas de cliente + draft IA.

Semana 1: rep CS Sophie lo usa con escepticismo.

Semana 2: encuentra que 60% de drafts IA pueden enviarse directamente; el otro 40% lo edita más rápido que escribir desde cero.

**Tiempo de respuesta a quejas cae de 5 días a 2.5 días**.

Semana 3, Sophie encuentra a Ming: "Presidente, antes editaba correos después de horas. Ahora salgo a las 5 pm. **Puedo recoger a mis hijos a tiempo**."

Ming piensa mucho esa noche.

### Mes 6: L1 Gate Party

Phase 1 termina — aceptación de L1 Gate.

Consultor y empresa verifican juntos:

- ✅ OpenWebUI a nivel empresa: 700 cuentas
- ✅ Política de IA firmada por: 92%
- ✅ Prompt Library: 38 entradas
- ✅ 5 Skills core en producción, todos con Owner + docs IPOE

**Momento crítico**: Chang dibuja el radar Stage 2 **otra vez**, lado a lado con hace 6 meses.

```
Hace 6 meses             6 meses después
       L1=0                  L1=4 ●
   L2=0  L3=parcial       L2=2  L3=parcial ●
                                
   L4=0                    L4=0
   L5=0                    L5=0
   
   APQC 11.x=0           APQC 11.x=2  ●
```

**El radar realmente está más redondo**.

Ming mira los dos gráficos. Sus ojos se humedecen.

"**Es la primera vez en mi vida que veo "nuestra empresa" objetivamente, numéricamente, estructuralmente mejor**."

Esa noche la empresa hace una "L1 Gate Party." Old Chen el capataz habla:

"Antes pensaba que IA tomaría mi trabajo. Ahora la uso para escribir mis logs de trabajo diario. **Mis 25 años de experiencia — por primera vez alguien se interesa lo suficiente para escribirla**."

### Mes 9: Los pedidos del Cliente A regresan

Phase 2 en progreso. Respuesta a quejas 2.5 → 1.5 días. Turnaround de propuesta 4 → 1.5 días.

Fines de noviembre, el director de compras del Cliente A llama: "La respuesta de MingChang es mucho más rápida últimamente. Pedidos del próximo trimestre **+12%**."

Ming le dice a Chang.
Chang sonríe: "¿Todavía usas 'autoridad del consultor' para convencer al directorio?"
Ming: "No. Uso **radar antes/después + dashboard Value Tracking de 5 dimensiones**."

### Mes 15: L2 + L3 Gate

Phase 2 termina.

- Skill Library: 18 entradas (excede los 15 firmados)
- n8n Workflows en producción: 5 (triage CS, propuestas de ventas, anomalías de fin de mes, anomalías de proceso, screening de CV de HR)
- Tasa de sign-off del reviewer: 96%

**APQC 4.0 Deliver: 1 → 3**
**APQC 11.x Knowledge: 2 → 3**

Radar **cambia de línea zigzagueante a casi una elipse**.

### Mes 24: Completo

Phase 3 termina.

- **1 Hermes Agent** pasa 4A-4E (summarizer de anomalías de proceso)
- **1 ensayo inter-dept ClawTeam** (Sales + CS + QC tres-dept Agent colaboración en pedido especial del Cliente A)
- Tasa de defectos: 3.2% → 2.0% (alcanza Ideal Practice Item #5)
- Respuesta a quejas: 5 días → 50 minutos (**vence el objetivo firmado "triage 1hr + humano 24hr"**)

En la reunión de revisión de directorio a los 24 meses, Ming dice:

"Gastamos NT$ 9.8M (80 + 200 + 700). Pero lo más valioso en estos 24 meses no es el dinero ahorrado. Es que **toda la empresa ahora habla el mismo idioma**:

- No discutimos 'qué enfoque es correcto'; discutimos 'qué cambio elevó qué categoría APQC'
- No decimos 'IA está robando empleos'; decimos 'IA nos libera para hacer trabajo más importante'
- No nos apoyamos en el juicio del consultor; nos apoyamos en **nuestros propios objetivos firmados**

**Esto es management científico**. Mi hija en NTU dijo que esto es la escuela Rosemann BPM + management científico de Max Weber aterrizando en la era moderna."

Vicepresidente: "¿Próximo paso?"
Ming: "Quiero open-source lo que aprendimos. **Para que cada manufacturero mediano tenga la misma metodología**."

---

## Epílogo: La metodología misma

24 meses después, dos cosas pasan en MingChang:

**Primero**: Ming se convierte en orador regular de la industria. En cada discurso dice:

> "Antes pensaba que los consultores vienen a decirme 'qué hacer.' Pero los consultores de Tiger AI me hicieron **ver claramente dónde estoy, elegir hacia dónde quiero ir, firmar mi propio commitment**.
> Cada paso posterior **deriva del objetivo que firmé yo mismo**. Ni una sola sección es 'autoridad del consultor dice así.'
> Doy este reporte a mi directorio, mis clientes, mi banco — **nadie puede refutarlo** — porque el inicio son estándares internacionales y el final es mi propia firma."

**Segundo**: Ming dona la historia de transformación de MingChang a la biblioteca de casos open-source de Tiger AI como caso benchmark "Manufacturing packaging 700 personal." **Escrito en formato Benchmark-grade** (los 9 campos obligatorios). Cada manufacturero mediano posterior puede calcular su propio gap contra los números de MingChang.

"**Ese es el ciclo cerrado del management científico**," dice Ming. "No 'terminé y se acabó.' Es 'la gente después de mí puede caminar el mismo camino usando el mismo método.'"

---

## Detrás de la historia — Para lectores que quieren entender la metodología

Esta historia **mapea totalmente** a la metodología de 8 etapas:

| Capítulo de la historia | Mapping metodológico |
| --- | --- |
| Cap 1: auto-quiz 10-Q | Pre-Engagement Quick Screen + Stage 1 punto de partida |
| Cap 2 Semana 1-2: Entrevista + Radar | **Phase A Diagnóstico**: Stage 1 As-Is + Stage 2 Reference Model |
| Cap 2 final: Mid Report | Phase A Deliverable + Gate A |
| Cap 3: Workshop de Co-Creación | **Phase B Estrategia**: Stage 3 Ideal Practice + Tool 3.6 |
| Cap 3 tarde: fórmula de gap | Stage 4 Gap Analysis + Stage 5 80/20 + Stage 6 Phased Goals + Stage 7 To-Be |
| Cap 3 final: reporte completo + 3-firma | Phase B Deliverable + Gate B |
| Cap 4: aterrizaje 24 meses | **Phase C Implementación**: Stage 8 + Revisión trimestral de radar + Value Tracking 5-dim |
| Epílogo: donación de caso | **Ciclo cerrado Cases-as-Benchmarks**: este cliente se convierte en el benchmark del siguiente |

Para lectura más profunda:

- **Argumento científico**: [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — por qué esta metodología resiste el debate
- **Flow completo**: [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) — detalles del modelo de contrato de 3 fases
- **Alineamiento de industria**: [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — vs McKinsey/BCG/Gartner etc.
- **Toolkit**: [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) — detalle de cada herramienta

---

## Versiones para otros roles

- **CEO / Dueño**: Tú eres Ming. Pregunta: "¿He visto evidencia objetiva en 24 meses de que el radar de mi empresa se volvió más redondo?"
- **CIO / Lead IT**: Tú eres Lin. Pregunta: "¿Cuál es mi gasto mensual de Shadow IT? ¿Puedo convertirlo en activos de la empresa?"
- **Consultor**: Tú eres Chang. Pregunta: "¿Estoy dando al cliente 'recomendaciones' o 'ayudándolo a verse claramente a sí mismo'?"
- **Empleado / trabajador Senior**: Tú eres Old Chen. Pregunta: "Mis 25 años de experiencia — ¿desaparecerán el día que me jubile?"
- **Academia / Política**: Esta historia implementa totalmente la escuela Rosemann BPM Maturity + management científico de Weber + ciclo cerrado de adopción GenAI. Open-sourced, reproducible, verificable.

---

Licencia & Citación

Este documento es Apache License 2.0; puede usarse, modificarse, comercializarse, siempre que se preserve la atribución de [`../NOTICE`](../NOTICE).
