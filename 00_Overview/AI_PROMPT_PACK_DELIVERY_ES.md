# Libro II AI Prompt Pack (Entrega de proyectos de consultoría)

> 🌐 Idioma: [繁體中文](AI_PROMPT_PACK_DELIVERY.md) ｜ [English](AI_PROMPT_PACK_DELIVERY_EN.md) ｜ **Español**
> Equivalente al [`11_AI_Prompt_Pack.md`](https://github.com/MorrisLu-Taipei/consultant-thinking-framework/blob/main/11_AI_Prompt_Pack.md) del Libro I. El pack del Libro I entrena el *juicio*; este pack lleva ese juicio a través de cada etapa de la *entrega*.
> Disciplina compartida: **separar la señal de la inferencia, nunca inventar, marcar lo no verificado como «por confirmar», procesar los datos del cliente solo con IA aprobada / puntos de conexión privados.**

---

## Cómo usarlo
Pegue los datos del cliente / notas de entrevista en el `{{ }}` de cada prompt, o actívelo mediante la skill `consulting-delivery-coach`. Cada prompt pide a la IA que **cite la fuente de la evidence** y que **indique la base del nivel L**.

---

### 1. Perfil del cliente → nivel L preliminar
```
Eres un consultor de diagnóstico de transformación con IA. A partir del contexto del cliente que figura abajo, da un juicio preliminar de madurez L1-L5.
Regla: vincula cada juicio a una evidence concreta del contexto; marca las dimensiones con evidencia insuficiente como «por diagnosticar» — no adivines.
Salida: nivel L preliminar + las 3 preguntas de seguimiento más importantes.
Contexto del cliente: {{pegar}}
```

### 2. Notas de entrevista → resumen de diagnóstico de la Phase A
```
Convierte la transcripción de la entrevista de abajo en un resumen de diagnóstico de la Phase A.
Estructura: (1) las palabras exactas del cliente (hechos) (2) el dolor real (superficie → raíz) (3) el job-to-be-done actual (4) la diagonal (diagonal) (punto ciego del competidor × necesidad futura del cliente × nuestra entrada) (5) lagunas de evidence (marcar «por confirmar»).
No añadas nada que no esté en la transcripción.
Transcripción: {{pegar}}
```

### 3. Diagnóstico → recomendación de diseño de curso
```
A partir del diagnóstico de nivel L de abajo, recomienda una ruta de cursos L1-L5.
Regla: decide primero si al cliente le falta capacidad / proceso / gobernanza / herramientas, y luego diseña el curso; explica el orden.
Salida: ruta de cursos + producto objetivo por etapa + riesgos.
Diagnóstico: {{pegar}}
```

### 4. Diagnóstico → esquema del informe de consultoría
```
Convierte el diagnóstico de abajo en un esquema de informe de consultoría de ocho etapas.
Debe incluir: Executive Problem Statement (redactado a partir de la diagonal (diagonal)), Roadmap, Risk Register, Stage Gate Criteria.
Cita una fuente de evidence para cada conclusión; no expreses nada como conclusión sin evidence.
Diagnóstico: {{pegar}}
```

### 5. Roadmap → checklist de entrega
```
Convierte la Roadmap de abajo en una checklist de entrega lista para aceptación.
Regla: cada ítem necesita un «criterio de aceptación» (qué cuenta como entrega exitosa) + «si esto entrega capacidad o una herramienta». Señala los ítems que solo entregan herramienta.
Roadmap: {{pegar}}
```

### 6. Estado del proyecto → riesgos y siguiente paso
```
Eres un reviewer del proyecto. A partir del estado del proyecto de abajo, enumera los riesgos y el siguiente paso.
Enfoque: desviación de alcance (scope creep), si debe activarse un Stage Gate, riesgo del pago final, si la estructura del cliente realmente mejoró.
Salida: Top 3 riesgos + siguiente paso recomendado + si debe entrarse en la siguiente Phase A/B/C.
Estado: {{pegar}}
```

---

## Recordatorio de seguridad y honestidad
- Procesa los datos del cliente solo con **IA aprobada por la empresa o un punto de conexión privado**; nunca los pegues en servicios públicos.
- Un consultor humano revisa toda salida de la IA; **lo marcado como «por confirmar» no debe entregarse como conclusión**.
- Anonimiza los casos externos («Company ABC» / «City X»). Este pack es una herramienta, no un dictamen final legal / financiero / de seguridad.
