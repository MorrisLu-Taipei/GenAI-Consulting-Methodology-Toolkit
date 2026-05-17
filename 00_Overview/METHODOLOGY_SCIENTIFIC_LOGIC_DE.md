# Wissenschaftliche Logik der Methodik: Warum dieser Report Debatten standhält

> 🌐 Sprache: [繁體中文](METHODOLOGY_SCIENTIFIC_LOGIC.md) ｜ [English](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) ｜ Deutsch ｜ [Français](METHODOLOGY_SCIENTIFIC_LOGIC_FR.md) ｜ [Español](METHODOLOGY_SCIENTIFIC_LOGIC_ES.md) ｜ [日本語](METHODOLOGY_SCIENTIFIC_LOGIC_JA.md) ｜ [한국어](METHODOLOGY_SCIENTIFIC_LOGIC_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Letzte Aktualisierung: 2026-05-15

---

> **Was dieses Dokument beantwortet**: Warum ist diese Methodik so entworfen? Warum 8 Stufen, nicht 5 oder 12? Warum fließen Daten so? Warum müssen Cases Benchmark-Grade sein? **Letztlich**: Wenn Klienten / Boards / Regulatoren sie herausfordern, worauf basiert dieser Beratungsreport?
>
> **Kernbehauptung**: Diese Methodik ist keine Sammlung von Beratungserfahrung, sondern eine **wissenschaftliche Management-Closed-Loop-Logik** — jeder Schritt erfüllt die fünf Bedingungen der wissenschaftlichen Methode: beobachtbar, quantifizierbar, reproduzierbar, falsifizierbar, auditierbar.

---

## 1. Warum Beratungsreports „wissenschaftliche Argumentationskraft" brauchen

Häufige Versagensszenarien:

| Szenario | Klient-Herausforderung | Typische Berater-Antwort | Warum es scheitert |
| --- | --- | --- | --- |
| Board-Befragung | „Wie wissen Sie, dass wir auf L2 sind?" | „Basierend auf unseren Interviews..." | Subjektiv; nicht verifizierbar |
| Interne Revision | „Warum Kundenservice vor Vertrieb?" | „Aus unserer Erfahrung..." | Erfahrung ist nicht auditierbar |
| Regulatorische Prüfung | „Wer ist verantwortlich, wenn KI versagt?" | „Wir haben Richtlinien..." | Richtlinien ohne Audit-Ketten zählen nicht |
| Berater wechseln | „Die vorherige Firma sagte L3; Sie sagen L2 — wer hat recht?" | „Verschiedene Methoden" | Nicht reproduzierbar = nicht wissenschaftlich |

**Tiger AIs Designziel**: Jede solche Frage hat eine **verifizierbare Zahl + auditierbare Evidenz + reproduzierbare Prozedur** als Antwort.

---

## 2. Fünf Bedingungen der wissenschaftlichen Methode vs. diese Methodik

| Wissenschaftliche Bedingung | Definition | Wie die Methodik sie erfüllt |
| --- | --- | --- |
| **1. Beobachtbar** | Schlussfolgerungen ruhen auf Evidenz, die andere sehen können | Stage 1 Aufnahmen + System-Inventar + As-Is Swimlanes; jedes Item mit Zeitstempel und Quelle |
| **2. Quantifizierbar** | Schlussfolgerungen reduzierbar auf Zahlen, nicht Adjektive | Stage 2 Radar 0-4 Scoring; Stage 4 Impact×Effort Scoring; Stage 5 80/20 Impact-Surface-Zahlen; Stage 8 Value Tracking 5 Dimensionen |
| **3. Reproduzierbar** | Verschiedene Berater mit gleicher Methode erreichen ähnliche Schlüsse | Drei Reference Models (APQC / SCOR / Tiger AI L1-L5) sind öffentliche Standards; 40-Fragen-Interview-Bank; MECE-Disziplin |
| **4. Falsifizierbar** | Schlussfolgerungen haben explizite Widerlegungsbedingungen | Stage 6 Stage Gate Criteria listen explizit pass/fail; Checklisten haben beobachtbare Bedingungen; verfehltes Ziel = Hypothese widerlegt |
| **5. Auditierbar** | Prozess kann unabhängig von Dritten verifiziert werden | Stage 8 Audit Log (LLM-Calls, Berechtigungsänderungen, Skill-Deploys, Reviewer-Sign-offs vollständige Kette), Aufbewahrung definiert |

> **Diese fünf Bedingungen sind keine Dekorationen**. Jede Berater-Schlussfolgerung, die auf diese fünf nicht reagieren kann, ist kein wissenschaftliches Management — nur Erfahrungsaustausch.

---

## 3. Warum genau 8 Stufen (nicht 5, nicht 12)

Zurück gefolgert aus wissenschaftlicher Methode: ein verteidigbarer KI-Transformations-Report **muss durch 5 Argumentationsaktionen gehen**, mit strikten Datenabhängigkeiten zwischen ihnen:

| Argumentationsaktion | Mappt auf Stage | Auslassung verursacht |
| --- | --- | --- |
| **A. Aktuellen Zustand beobachten** | Stage 1 As-Is | Keine objektive Baseline → alles danach ist Raten |
| **B. Internationale Koordinaten anwenden** | Stage 2 Reference Model | Keine externen Koordinaten → „wir sind nicht gut genug" ist Berater-Meinung |
| **C. Klient erweitert eigene Ideal Practice** | Stage 3 Best Practice | Kein klient-signiertes Ziel → Klient kann Gap leugnen |
| **D. Gap quantifizieren** | Stage 4 Gap Analysis | Kein strukturierter Gap → kann nicht priorisieren |
| **E. Kernproblem konvergieren** | Stage 5 Problem Definition | Kein 80/20 → „alles ist wichtig" = nichts wird erledigt |
| **F. Absorbierbare Ziele setzen** | Stage 6 Phased Goals | Keine Phasen-Zerlegung → einmaliger Perfektionsversuch = Versagen |
| **G. Blueprint entwerfen** | Stage 7 To-Be Design | Kein To-Be-Diagramm → Roadmap landet nicht auf Org und Systemen |
| **H. Ausführen & steuern** | Stage 8 Implementation | Kein Change Mgmt + Value Tracking + Audit → Blueprint ist Wandschmuck |

**Warum genau 8**: jede Argumentationsaktion ist untrennbar; **Auslassung einer lässt eine Herausforderung unbeantwortet**.

- Stage 2 auslassen → „Was ist Ihr Standard?" hat keine Antwort
- Stage 4 auslassen → „Warum dies vor jenem?" hat keine Antwort
- Stage 6 auslassen → „Warum 9 Monate nicht 3?" hat keine Antwort
- Stage 8 auslassen → „Wie beweisen Sie Verbesserung?" hat keine Antwort

> 5 Stufen ist zu grob (lässt Reference Model, Phased Goals, Change Mgmt aus); 12 Stufen ist zu fein (redundante Unterschritte). **8 ist „die minimal vollständige debattierbare Argumentationskette."**

---

## 4. Warum Daten so fließen (Wissenschaftlicher Grund für jeden Pfeil)

```
Stage 1 ──────────► Stage 2 ──────────► Stage 3 ──────────► Stage 4
As-Is              Reference Model     Best Practice         Gap
beobachtete         internationale      Klient Ideal          objektiver Gap
Realität            Koordinaten         Practice (signiert)
                                                              │
                                                              ▼
Stage 8 ◄────────── Stage 7 ◄────────── Stage 6 ◄────────── Stage 5
Implementation      To-Be Design       Phased Goals          Problem
Landing + Change    Zukunftsblueprint   absorbierbare         Kernkonvergenz
                                        Schritte
                                                              
        ↑                                                     ↓
        └─── Quartalsweise: Stage 2 Radar erneut besuchen (Closed-Loop-Verifikation) ───┘
```

#### Warum jeder Pfeil kausal notwendig ist

| Pfeil | Warum diese Richtung | Umkehrung verursacht |
| --- | --- | --- |
| **Stage 1 → 2** | Muss „Realität" haben, bevor mit „Standard" verglichen wird | Umgekehrt: Cherry-Pick-Evidenz, um zum Standard zu passen |
| **Stage 2 → 3** | Muss „Struktur vollständig" bestätigen, bevor „Klient Ideal" diskutiert wird | Umgekehrt: Ideal überspringt strukturelle Gaps |
| **Stage 3 → 4** | Muss **klient-signierte Ideal Practice** haben, bevor „Gap = (Klient Ideal − Klient As-Is)" berechnet wird | Ohne Klient-Unterschrift = Berater-Meinung, widerlegbar |
| **Stage 4 → 5** | Muss „alle Gaps" haben, bevor 80/20-Konvergenz zu „Kernproblem" | Ohne 4 = Problem-Definition raten |
| **Stage 5 → 6** | Muss „Kernproblem" sperren, bevor „Ziele" gesetzt werden | Ohne 5, Ziele zerstreuen |
| **Stage 6 → 7** | Muss „phasierte Ziele" haben, bevor „Blueprint" entworfen wird | Ohne 6, Blueprint versucht einmaligen Wurf |
| **Stage 7 → 8** | Muss „Blueprint" haben, bevor „Ausführung" | Ohne 7, Ausführung ist blind |
| **Stage 8 ↑ Stage 2 (quartalsweise)** | Nach Ausführung, „ist Standard-Radar runder?" erneut besuchen | Ohne Loopback, PoCs erledigt aber Struktur unverifiziert |

> **Das ist die wissenschaftliche Bedeutung von „Closed Loop"**: nicht „erledigt ist gut", sondern „Ergebnisse können rückwirkend verifiziert / falsifiziert werden."

---

## 5. Warum Reference Model 4 Schichten ist (nicht 3, nicht 5)

Abgeleitet aus Maturitys „**Abstraktion × Volatilität**" Achse (siehe [`CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 2.7):

| Abstraktion | Volatilität | Schicht | Warum kann nicht zusammengelegt oder ausgelassen werden |
| --- | --- | --- | --- |
| Am abstraktesten | Jahre | **L1 Governance** | Strategie und Richtlinien können nicht mit Prozessen mischen (Volatilität unterscheidet sich 10×) |
| Abstrakt | Quartale-Jahre | **L2 Business** | Geschäftsfunktionen können nicht mit Daten-Services mischen |
| Mittel | Monate-Quartale | **L3 Information** | Daten-Services können nicht mit Hardware/Netzwerken mischen |
| Am konkretesten | Wochen-Monate | **L4 Technical** | Hardware in Business-Schicht gemischt sperrt Tech-Entscheidungen |

**3 Schichten unzureichend**: lässt normalerweise L3 Information fallen → Daten-Services gequetscht in L2 oder L4 → Fokusverlust.
**5 Schichten exzessiv**: die zusätzliche Schicht ist normalerweise eine Unterschicht von L2 oder L3 → verletzt MECE.

> **Die Dragon1-Schule besteht aus diesem wissenschaftlichen Grund auf 4 Schichten**. Tiger AI Enterprise AI Reference Model folgt ihm strikt.

---

## 6. Warum Cases Benchmark-Grade sein müssen (nicht narrativ)

Wissenschaft erfordert „**Reproduzierbarkeit**" — derselbe Case gelesen von verschiedenen Beratern / Klienten sollte ähnliche „Gap-Schätzungen" liefern.

- **Narrativer Case**: „Firma X machte KI-Qualitätsprüfung und war erfolgreich" → nicht reproduzierbar (jeder Leser interpretiert anders)
- **Benchmark-Grade Case**: 9 obligatorische Felder (Industrie + Skala + Start L + End L + Dauer + Investment + Wins + Failures + Anwendbarkeit) → **reproduzierbar** (jeder Leser's Gap/Zeit/Budget-Schätzung fällt in ähnliche Bandbreite)

Siehe Tool 3.5 Cases-as-Benchmarks.

> **Deshalb folgen alle 7 Tiger AI Cases derselben 9-Felder-Vorlage** — nicht für visuelle Konsistenz, sondern für die wissenschaftliche Bedingung der **Reproduzierbarkeit**.

---

## 7. Die „wissenschaftliche Argumentationskraft" Checkliste des Reports

Wenn Klienten / Boards / Regulatoren folgende Fragen stellen, hat diese Methodik spezifische Antwortstellen:

| Herausforderung | Antwortstelle | Evidenz |
| --- | --- | --- |
| „Wie wissen Sie, dass wir auf L2 sind?" | §3 As-Is + §4 RM Mapping | Interview-Aufnahmen, System-Inventar, RM-Radar 0-4 |
| „Warum APQC / Tiger AI L1-L5?" | §4.1 + Tool 2.5 | 10-Bedingungen-Qualifikations-Scorecard |
| „Wie weit sind wir von unserem Ideal?" | §5 + §6.1 | **Klient-signierte Ideal Practice Definitionstabelle** + Case Benchmark; Gap = (Ihr signiertes Ideal − Ihr As-Is), beide Enden sind Ihre Aussagen |
| „Warum Kundenservice vor Vertrieb?" | §6.2 + §6.3 | Impact × Effort Matrix + Prioritization Score |
| „Warum ist das Kernproblem ‚Wissens-Asset-Bildung'?" | §7 | 80/20 Impact-Surface-Zahlen + 5 Whys-Kette |
| „Warum 9 Monate nicht 3?" | §8 + Tool 6.3 | Phased Zerlegung + Organizational Absorption (6 Dimensionen) + Benchmark-Case-Dauer |
| „Was, wenn der PoC versagt?" | §13.2 | Risk Register + Triggers + Mitigation Owners |
| „Wie beweisen Sie Verbesserung?" | §13.1 + quartalsweise Radar-Review | Value Tracking 5 Dimensionen + Stage 2 Radar before/after |
| „Wer ist verantwortlich, wenn KI versagt?" | §12.1 + Tool 8.8 | RACI + AI Ethics Checklist + Audit Log vollständige Kette |
| „Kann Ihre Methodik reproduziert werden?" | Gesamte Methodik | Apache 2.0 + GitHub + Tool 2.5 Selbstqualifikation 9/10 |
| „Letzter Berater sagte L3, Sie sagen L2 — wer hat recht?" | §3 Scoring-Evidenz | Öffentliche 0-4 Skala + jeder Score hat beobachtbare Evidenz → **drittpartei-verifizierbar** |
| „Warum genau 8 Stufen?" | Dieses Dokument §3 | „Minimal vollständige debattierbare Argumentationskette" Argument |

> **Der Report wird ein debattierbares Dokument**: der Klient „vertraut nicht der Berater-Autorität", sondern „folgt der Evidenzkette, um selbst dieselbe Schlussfolgerung zu erreichen." Das ist wissenschaftliches Management.

---

## 8. Vergleich mit Mainstream-Beratungsmethodiken

| Methodik | Stärke | Fehlt (aus Linse wissenschaftlicher Vollständigkeit) |
| --- | --- | --- |
| **McKinsey Issue Tree + Pyramid** | Rigorose logische Argumentation, starke Narrative | Kein Reference Model (keine Koordinaten); keine Phased Goals (keine Phasen-Zerlegung) |
| **BCG Digital Maturity** | Klare 5-Stufen-Maturity | Kein quantifiziertes Best Practice (Exzellenz vom Berater beschrieben); keine organisatorische Absorptions-Bewertung |
| **Gartner AI Maturity** | Branchenanerkannt | Keine As-Is Interview-Disziplin; keine reproduzierbaren Case-Benchmarks |
| **MIT AI Capability** | Akademisch rigoros | Fehlt Implementation & Change Landing-Tools |
| **Tiger AI (diese Methodik)** | **8-Stufen vollständige Argumentationskette + 4-Schichten Reference Model + Cases-as-Benchmarks Closed Loop** | Neu (gestartet 2025, Cases akkumulieren) |

> **Wir sagen nicht, dass andere Methodiken schlecht sind** — wir sagen, sie haben jeweils Stärken, aber **unvollständige Closed Loops**. Tiger AIs Designziel ist, diesen Loop zu vervollständigen, damit der Report **Evidenz für jeden Satz vom Cover bis zur letzten Seite** hat.

---

## 9. Würdigkeit für akademische und regulatorische Zitation

Warum diese Methodik von akademischen Communities validiert, zitiert, verbessert werden kann:

1. **Öffentlich**: Apache 2.0, GitHub Repo, zweisprachig zh/en
2. **Selbst-qualifizierbar**: Tool 2.5 Selbst-Evaluation, 9 von 10 Bedingungen erfüllt
3. **Theoretische Wurzeln transparent**: Rosemann BPM Maturity Schule (QUT) + CMMI + APQC + Dragon1 EA je zitiert
4. **Branchenübergreifend validiert**: Fertigung / Krankenhaus / Marketing / B2B / Financial / Government / Education — 7 Branchen-Cases (validiert Portabilität)
5. **Falsifizierbar**: jede Stage Gate Criteria hat Widerlegungsbedingungen
6. **Kritisierbar**: dieses Dokument und Tool 2.5 vermerken beide explizit „neu, Anerkennung akkumuliert"

> **Der Gold-Standard akademischer Zitation ist „kann jemand anders diese Methode auf ein anderes Problem anwenden und ähnliche Schlüsse erreichen?"** — Tiger AI Methodik antwortet Ja, weil alle Schritte, Tools und Scoring-Kriterien öffentlich sind.

---

## 10. Operative Disziplin für Berater

Wenn Sie diesen Report schreiben, muss jeder Absatz beantworten:

```
Was ist die Evidenz für diese Aussage?              ← Beobachtbar
Wie wurde diese Zahl berechnet?                      ← Quantifizierbar
Würde ein anderer Berater dasselbe erreichen?        ← Reproduzierbar
Wenn dies falsch ist, was würde ich sehen?           ← Falsifizierbar
Wer hat diesen Prozess abgesegnet?                   ← Auditierbar
```

**Alle 5 beantworten → dieser Absatz ist wissenschaftliches Management**.
**Jede unbeantwortbar → dieser Absatz ist persönliche Meinung; Evidenz ergänzen oder löschen.**

---

## 11. Versprechen an Klienten

Diese Methodik verspricht:

1. **Jede Schlussfolgerung hat nummerierte Evidenz** — Appendices A-G vollständig nachverfolgbar
2. **Jede Zahl hat eine Berechnungsformel** — kein „basierend auf Berater-Urteil"
3. **Jede Empfehlung hat Stage Gate Criteria** — Sie können verifizieren
4. **Jedes Risiko hat Trigger + Owner + Mitigation** — Sie können managen
5. **Jeder Case ist Benchmark-Grade** — Sie können den Gap selbst berechnen
6. **Jedes Phasenende besucht das Reference Model Radar erneut** — Sie sehen die Struktur tatsächlich runder werden

**Wenn ein Absatz sich anfühlt wie „Berater-Autorität entscheidet", weisen Sie darauf hin. Wir fügen Evidenz hinzu, überarbeiten die Formel oder löschen sie.**

---

## 12. Schluss: Diese Methodik ist selbst ein Reference Model

Eine letzte selbstreferenzielle Beobachtung:

- Diese Methodik wendet Tool 2.5's 10 Bedingungen zur **Selbst-Evaluation** an: 9 von 10 erfüllt (Bedingung 6 „breite Branchenanerkennung" akkumuliert noch)
- Diese Methodik wendet Tool 2.6's 5 Ableitungsfragen zum **Selbst-Inventar von Komponenten** an: 8 Stufen + 4 Schichten + 5 Tracking-Dimensionen alle vorhanden
- Diese Methodik wendet Tool 2.7's 4-Schichten-Architektur zur **Selbst-Organisation** an: Governance (dieses Dokument) + Business (Stages 1-8) + Information (Toolkit + Cases) + Technical (GitHub Repo + AGENTS.md + CLAUDE.md)
- Diese Methodik wendet Tool 3.5's Cases-as-Benchmarks an, um **Reproduzierbarkeit selbst zu beweisen**: 7 Branchen-Cases folgen alle der 9-Felder-Vorlage

> **Das ist der Closed Loop wissenschaftlichen Managements**: eine Methodik analysiert nicht nur andere, sondern **kann sich selbst mit ihren eigenen Tools analysieren** — in der Akademie genannt „selbstreferenzielle Konsistenz", das Markenzeichen rigoroser Theorie.

---

## Referenzen

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- APQC (2024). *Process Classification Framework Version 7.3*.
- CMMI Institute (2018). *CMMI for Development V2.0*.
- Dragon1 (n.d.). *Enterprise Architecture Reference Model*. <https://www.dragon1.com/reference-models/enterprise-architecture-reference-model>
- Pyramid Principle: Minto, B. (2009). *The Pyramid Principle*.
- 80/20: Koch, R. (1997). *The 80/20 Principle*.
- 5 Whys: Ohno, T. (1988). *Toyota Production System*.
- Change Management: Kotter, J. (1996). *Leading Change*. Prosci ADKAR.

---

Lizenz & Zitation

Dieses Dokument ist Apache License 2.0; darf verwendet, modifiziert, kommerzialisiert werden, sofern die [`../NOTICE`](../NOTICE) Attribution erhalten bleibt.
