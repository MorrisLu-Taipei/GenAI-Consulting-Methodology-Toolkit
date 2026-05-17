# Akademische theoretische Grundlagen: Die sieben theoretischen Säulen der Tiger AI Methodik

> 🌐 Sprache: [繁體中文](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [English](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) ｜ Deutsch ｜ [Français](ACADEMIC_THEORETICAL_FOUNDATIONS_FR.md) ｜ [Español](ACADEMIC_THEORETICAL_FOUNDATIONS_ES.md) ｜ [日本語](ACADEMIC_THEORETICAL_FOUNDATIONS_JA.md) ｜ [한국어](ACADEMIC_THEORETICAL_FOUNDATIONS_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Letzte Aktualisierung: 2026-05-16

---

> **Zweck**: Die in Dateien verstreuten akademischen theoretischen Grundlagen der Tiger AI Methodik in **ein autoritatives Dokument** konsolidieren. Wenn irgendein Wissenschaftler / Regulator / ernsthafter Berater fragt „was ist die theoretische Basis", ist dieses Dokument die Antwort.
>
> **Kernanspruch**: Tiger AI Methodik ist nicht bloß Consulting-Praxis, sondern eine **engineered Integration von sieben Theorien**.

---

## 1. Theorie-Map Überblick

| Theorie | Begründer / Klassische Referenz | Gelöstes Kernproblem | Tiger AI Mapping |
| --- | --- | --- | --- |
| **Capability Maturity & BPM Maturity** | Paulk et al. (1993) CMMI; Rosemann & de Bruin (2005) | Wie strukturiert organisatorische Capability scoren? | L1-L5 + Stage 2 Scoring |
| **Absorptive Capacity** | Cohen & Levinthal (1990) | Warum unterscheiden sich Organisationen so stark beim **Absorbieren** neuer Capability? | Tool 6.3 Organizational Absorption Assessment |
| **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | Welche Aufgaben passen / passen nicht zu AI? | Stage 7 To-Be Design (nicht jede Abteilung sollte L5 erreichen) |
| **Dynamic Capabilities** | Teece et al. (1997); Teece (2007) | Wie passt sich eine Organisation **schnell an externe Änderung an**? | Stage 7 + Stage 8 (von statischer Automatisierung zu dynamischer Capability) |
| **Sociotechnical Systems & Trust in AI** | Bostrom & Heinen (1977); Dietvorst et al. (2015); Glikson & Woolley (2020) | Warum ist Human-AI-Kollaboration schwer? Algorithm Aversion / Complacency | Stage 8 Change Management + HITL |
| **Real Options Theory** | Dixit & Pindyck (1994); McGrath (1997) | Wie hoch-unsichere AI-Strategie-Investition bewerten? | Stage 8 §13 Value Tracking + ROI |
| **AI-Native Living Book / Executable Knowledge Artifact** | Knuth (1984); Anderson et al. (1995); dieser Autor (2026) | Kann die Methodik selbst von AI ausführbar sein? | AGENTS.md + AI_NATIVE_LIVING_BOOK |

---

## 2. Capability Maturity & BPM Maturity

### 2.1 Theorie-Zusammenfassung

- **CMMI**: Paulk et al. (1993) am SEI definierten 5-Level organisatorische Capability (Initial / Repeatable / Defined / Managed / Optimizing)
- **BPM Maturity Model**: Rosemann & de Bruin (2005, QUT) erweiterten Maturity auf Business Process Management, hinzufügend 6 Enabler: Process Awareness / Alignment / Methods / IT / People / Culture

### 2.2 Beitrag zu Tiger AI

- **L1-L5 zwei Achsen** erben BPM Maturity's „Process Awareness → Optimization" Logik, hinzufügend GenAI-Ära-essentielle „**Scale-Achse + AI-Autonomie-Achse**" Doppelstruktur
- **0-4 Skala + BARS Behavioral Anchors** stammen aus dieser Schule
- **Stage Gate Criteria** = CMMI's „Process Areas" + Phase Acceptance

### 2.3 Gemappte Dateien

- [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §3.0 Zwei-Achsen-Story
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) L1-L5 Definitionen
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) Behavioral Anchors

---

## 3. Absorptive Capacity

### 3.1 Theorie-Zusammenfassung

- **Cohen & Levinthal (1990)** in *Administrative Science Quarterly*: die „**Fähigkeit einer Organisation, externes Wissen zu identifizieren, zu assimilieren und anzuwenden**" bestimmt ihre Innovations-Capacity
- Kernelemente: **Prior Knowledge + Internal Knowledge Flow**
- Zahra & George (2002) teilen weiter in 4 Dimensionen: Acquisition / Assimilation / Transformation / Exploitation

### 3.2 Beitrag zu Tiger AI

- Erklärt, warum **dieselbe AI-Opportunity völlig unterschiedliche Ergebnisse** über Unternehmen yieldet — der Unterschied ist Absorptive Capacity
- Tool 6.3 Organizational Absorption Assessment mappt direkt auf diese Theorie
- Verstärkt „**warum Levels nicht übersprungen werden können**": L1-L3 überspringen → unzureichende Absorptive Capacity → L4-L5 wird scheitern (siehe [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) §2)

### 3.3 Spezifische Erweiterung zu Tool 6.3

Original Tool 6.3 6 Dimensionen (Budget / Champion / IT FTE / Governance / Literacy / Change Capacity) **fügen 2 neue Dimensionen hinzu**:

| Neue Dimension | Assessment-Fragen | Score |
| --- | --- | --- |
| **Prior Knowledge** | Hat Unternehmen: (a) vergangene BPM / Lean / Six Sigma Erfahrung? (b) irgendwelche vergangenen AI / ML / RPA Versuche? (c) interne Software-Dev-Capability? | 0-4 |
| **Internal Knowledge Flow** | Zwischen Abteilungen: (a) routinemäßige Cross-Dept-Reviews? (b) geteilte Document-Platform? (c) internes Mentor- / Instructor-System? | 0-4 |

→ High Prior Knowledge + High Knowledge Flow Unternehmen können aggressiveres Phase 1/2/3 handhaben; umgekehrt müssen Timelines verlängert werden.

### 3.4 Referenzen

- Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128-152.
- Zahra, S. A., & George, G. (2002). Absorptive capacity: A review, reconceptualization, and extension. *Academy of Management Review*, 27(2), 185-203.

---

## 4. Task-Technology Fit (TTF)

### 4.1 Theorie-Zusammenfassung

- **Goodhue & Thompson (1995)** in *MIS Quarterly*: der Grad, zu dem Technologie Performance verbessert, hängt vom **„Task Demand ↔ Tech Capability"** Fit ab
- Task-Klassifikation: **Routine (repetitive, vorhersagbar) vs Non-Routine (urteilsschwer, kreativ)**

### 4.2 Beitrag zu Tiger AI

**Nicht jede Abteilung sollte L5 erreichen**. Bestimme den angemessenen L-Level-Endpunkt jeder Abteilung durch Task-Charakteristiken:

| Task-Typ | Angemessener Endpunkt | Begründung |
| --- | --- | --- |
| Highly Routine (CS FAQ, Rechnungs-Klassifikation) | L3-L4 | Hoher AI-Fit; niedriger HITL-Kost |
| Medium Routine + partielles Judgment (Sales-Angebote, Monatsende-Anomalien) | L2-L3 + HITL | AI entwirft + Mensch bestätigt; balanciert Effizienz und Risiko |
| Highly Non-Routine (M&A Evaluation, strategische Entscheidungen) | L1-L2 (persönlicher Assistent) | AI assistiert, Menschen führen; L4-L5 zu pushen schadet Urteilsqualität |
| Highly Compliance-Sensitive (Legal, medizinische Diagnose) | L2-L3 + strong HITL | Regulatorisches Risiko zu hoch; L4-L5 ungeeignet |

### 4.3 Gemappte Dateien / Tools

- Stage 7 Tool 7.2 Human-AI Collaboration → TTF Matrix entscheidet AI-Involvement pro Prozess
- Hinzufügen **TTF Assessment Worksheet** zu Tool 6.3 → TTF pro Abteilung scoren, Ideal L-Level bestimmen

### 4.4 Referenzen

- Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. *MIS Quarterly*, 19(2), 213-236.
- Zigurs, I., & Buckland, B. K. (1998). A theory of task/technology fit and group support systems effectiveness. *MIS Quarterly*, 22(3), 313-334.

---

## 5. Dynamic Capabilities

### 5.1 Theorie-Zusammenfassung

- **Teece, Pisano & Shuen (1997)** in *Strategic Management Journal*: Wettbewerbsvorteil stammt vom „**Integrieren, Aufbauen, Rekonfigurieren interner und externer Ressourcen**"
- **Teece (2007)** zerlegt in drei Micro-Foundations:
  1. **Sensing**: Opportunities und Threats identifizieren
  2. **Seizing**: Entscheidung und Ressourcenallokation
  3. **Transforming**: organisatorische Rekonfiguration, um Opportunities zu nutzen

### 5.2 Beitrag zu Tiger AI

**Von statischer Automatisierung → dynamische adaptive Capability**. Tiger AI macht nicht nur bestehende APQC-Prozesse AI-isiert, sondern **baut Kunden neue Capability auf, sich kontinuierlich an externe Änderung anzupassen**:

| Dynamic Capability | Tiger AI Mapping |
| --- | --- |
| **Sensing** | L3 Workflow + L4 Agent monitoren kontinuierlich Markt- / Kunden- / Prozess-Signale |
| **Seizing** | Phase 1/2/3 Dekomposition = Konvertierung gesensed Signale in konkrete Investment-Entscheidungen |
| **Transforming** | L5 Multi-Agent Organization + Quarterly Gate C Radar = kontinuierliche Org-Rekonfiguration |

### 5.3 Spezifische Erweiterung zu Stage 7

Hinzufügen **Dynamic Capability Worksheet** zu Stage 7 To-Be Design:

```
Per Teece (2007) drei Micro-Foundations, jedes To-Be Design muss beantworten:

1. Sensing: Welches externe Signal hilft dieses AI-Design dem Unternehmen zu "sensen"?
   Z.B. Complaint Agent monitort Kunden-Zufriedenheits-Trends
2. Seizing: Wie schnell kann das Unternehmen "seizen", wenn Signale erscheinen?
   Z.B. Quick Win Complaint Response 5d → 1d komprimiert Kunden-Verlust-Fenster
3. Transforming: Wie ermöglicht dieses AI organisatorische "Self-Reconfiguration"?
   Z.B. L5 ClawTeam cross-dept = Org hängt nicht mehr von spezifischem Senior-Personal ab
```

→ Ein To-Be, das diese 3 nicht beantwortet, ist nur „Status Quo automatisieren", keine echte Transformation.

### 5.4 Referenzen

- Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal*, 18(7), 509-533.
- Teece, D. J. (2007). Explicating dynamic capabilities. *Strategic Management Journal*, 28(13), 1319-1350.

---

## 6. Sociotechnical Systems & Trust in AI

### 6.1 Theorie-Zusammenfassung

- **Sociotechnical Systems Theory** (Bostrom & Heinen, 1977): organisatorische Performance = Joint Output von **Social System + Technical System**; keines kann allein optimiert werden
- **Algorithm Aversion**: Dietvorst, Simmons & Massey (2015) in *JEP*: Menschen **bevorzugen schlechteres menschliches Urteil gegenüber Algorithmen, nachdem sie den Algorithmus erren sahen**, selbst wenn sie wissen, dass der Algorithmus genauer ist
- **Automation Complacency**: Parasuraman & Manzey (2010): Über-Vertrauen in Automation verursacht Vigilanz-Verlust, führt zu größeren Incidents
- **Trust in AI**: Glikson & Woolley (2020) integrieren kognitives + emotionales Trust

### 6.2 Beitrag zu Tiger AI

Die wahre Challenge der Human-AI-Kollaboration ist nicht nur „Angst vor Ersatz", sondern auch:

1. **Algorithm Aversion**: nach AI's erstem Fehler lehnt das Personal es kollektiv ab → häufig nach L3-L4 Launch
2. **Automation Complacency**: Personal stoppt mit Reviewen → HITL scheitert → größere Incidents
3. **Accountability-Ambiguität**: wer ist verantwortlich, wenn AI erret? Personal fürchtet Schuld → psychologische Sicherheits-Gap
4. **Professional Identity Reshaping**: von „Doer" zu „Reviewer" → kognitive Last und Sense of Achievement verschieben sich

### 6.3 Erweiterung zu Stage 8 Change Management

Hinzufügen 2 neuer Resistance-Typen zu Tool 8.2:

| Resistance-Typ | Typisches Signal | Handhabung |
| --- | --- | --- |
| **Algorithm Aversion** | Kollektive Ablehnung nach einem AI-Fehler | Transparenz über Fehlerraten (Mensch vs AI) + graduelle Trust-Building (mit Low-Risk-Szenarien beginnen) |
| **Automation Complacency** | Personal genehmigt ohne zu reviewen | Verpflichtende Random Sampling im Reviewer Workflow + Re-Training nach detektierten Fehlern |

### 6.4 Erweiterung zu HITL Design (Tool 7.2)

Hinzufügen **Psychologische Sicherheit und Accountability-Spalten**:

| Prozess | HITL Node | **Accountability Statement** | **Psychologische Sicherheit** |
| --- | --- | --- | --- |
| CS Reply | 100% Human Review vor Senden | AI Draft Responsibility = AI Champion; finale Reply Responsibility = CS-Personal | Personal hat Recht „abzulehnen ohne Review wenn AI falsch ist" ohne Schuld |
| Process Root Cause | 100% Human Review vor Action | AI Hypothesis Responsibility = Agent Developer; Action Responsibility = Process Manager | Manager hat formales SOP zu „AI-Vorschlag abzulehnen" |

### 6.5 Referenzen

- Bostrom, R. P., & Heinen, J. S. (1977). MIS problems and failures: A socio-technical perspective. *MIS Quarterly*, 1(3), 17-32.
- Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion. *JEP: General*, 144(1), 114-126.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3), 381-410.
- Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence. *Academy of Management Annals*, 14(2), 627-660.
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *ASQ*, 44(2), 350-383.

---

## 7. Real Options Theory

### 7.1 Theorie-Zusammenfassung

- **Dixit & Pindyck (1994)** in *Investment Under Uncertainty*: hoch-unsicherer Investment-Wert = sofortiger Ausführungswert + **„Future Optionality" Wert**
- **McGrath (1997)** auf Strategie angewendet: „**Today's Investment Preserves the Right to Expand in the Future**"
- Kontert NPV-Unterschätzung unter Unsicherheit: NPV nimmt Gewissheit an, aber Manager-Flexibilität hat hohen Wert unter Unsicherheit

### 7.2 Beitrag zu Tiger AI

L4-L5 hoch-unsichere AI-Investition wird **notwendigerweise durch traditionelles NPV / IRR unterschätzt** (weil 18-24-Monats-Cash-Flows unsicher sind). Real Options bietet bessere Framing:

| Investment | NPV-Sicht (unterschätzt) | Real Options-Sicht (gerechtfertigt) |
| --- | --- | --- |
| Phase 1 Foundation (NT$ 2,8M) | Cash Flow unklar → NPV ≈ 0 | Kauf der „**Option, L4-L5 in Zukunft zu niedrigeren Kosten schnell zu expandieren**", weit mehr wert als NT$ 2,8M |
| L1 unternehmensweites Chat AI | Kurzfristige ROI unklar | Mitarbeiter-AI-Literacy = **Foundational Asset für alle zukünftigen AI-Anwendungen** |
| L2 Skill Library | ROI unsichtbar | Knowledge Codification = Option des Unternehmens, „**mehrere AI-Anwendungen gleichzeitig in Zukunft einzustöpseln**" |
| L4 Hermes Agent Pilot | Ist ein Agent es wert? | Pilot = L4 lernen = Option zu L5 ClawTeam |

### 7.3 Real Options Valuation (vereinfacht Black-Scholes)

Für L4-L5 Investments, schätzen via:

```
Option Value = max(0, future_payoff - exercise_cost)

Wobei:
  future_payoff = Umsatz aus Ausübung der Option (z.B. Expandieren zu L5)
  exercise_cost = Kost bei Ausübung (z.B. Phase 3 Investment)
  volatility (σ) = Markt- / Tech-Unsicherheit
  time-to-expiration = Opportunity-Window
```

⚠️ Keine Notwendigkeit für exaktes Black-Scholes; **Narrativ-Level-Argument genügt, um CFO zu überzeugen**, „kurzfristig unsichtbare ROI aber langfristig wertvolle" Investition zu rechtfertigen.

### 7.4 Erweiterung zu Stage 8 §13 Value Tracking

Original 5 Dimensionen (Time / Quality / Scale / Risk / Assets), **6. Dimension hinzufügen**:

| Dimension | Inhalt |
| --- | --- |
| **Strategic Options** | Welches „**Future Exercise Right**" hat dieses Investment bewahrt? Z.B. L1 Foundation → kann L4 in Zukunft schnell expandieren; L2 Skill Library → kann jeden zukünftigen Agent einstecken; L3 Workflow → kann jedes neue System integrieren |

### 7.5 Referenzen

- Dixit, A. K., & Pindyck, R. S. (1994). *Investment Under Uncertainty*. Princeton University Press.
- McGrath, R. G. (1997). A real options logic for initiating technology positioning investments. *Academy of Management Review*, 22(4), 974-996.
- Trigeorgis, L. (1996). *Real Options*. MIT Press.

---

## 8. AI-Native Living Book als Executable Knowledge Artifact

### 8.1 Theorie-Zusammenfassung

- **Literate Programming**: Knuth (1984) argumentierte, Code und Docs sollten in ein einziges „menschlich-lesbares + maschinell-ausführbares" Dokument integriert werden
- **Intelligent Tutoring Systems (ITS)**: Anderson et al. (1995) designten AI als personalisierte Tutoring-Systeme
- **Open Educational Resources (OER) + AI**: zeitgenössischer Trend, der Open Materials mit AI als interaktive Knowledge-Systeme kombiniert

### 8.2 Beitrag zu Tiger AI

Diese Methodik selbst ist ein **praktischer Case** dieser Theorie:

- repo + AGENTS.md = **Executable Knowledge Artifact**
- AI Co-Reading Tutor = **Adaptive ITS** angewendet auf Erwachsenen-Professional-Education
- Kunde, der mit Methodik konversiert = customized OER

Siehe [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) für volle Diskussion.

### 8.3 Referenzen

- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society*. Harvard University Press.

---

## 9. Wie die 7 Theorien kooperieren: Tiger AI's Integriertes Modell

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   [Capability Maturity]  ────►  L1-L5 strukturiertes Scoring     │
│         │                                                        │
│         ▼                                                        │
│   [Absorptive Capacity] ────►   warum Unternehmen sich beim     │
│         │                       Absorbieren unterscheiden        │
│         ▼                                                        │
│   [Task-Technology Fit] ────►  welche Aufgaben auf welchem L?    │
│         │                                                        │
│         ▼                                                        │
│   [Dynamic Capabilities]────►  L3-L5 nicht nur Automatisierung,  │
│         │                       sondern adaptive Capability bauen │
│         ▼                                                        │
│   [Sociotechnical Trust]────►  reale Human-AI-Kollaborations-    │
│         │                       Challenges (Trust, Accountability)│
│         ▼                                                        │
│   [Real Options]        ────►  Rechtfertigung von L4-L5          │
│         │                       Strategie-Investment unter        │
│         │                       Unsicherheit                     │
│         ▼                                                        │
│   [AI-Native Living Book]──►   Methodik selbst ausführbar        │
│                                                                  │
└────────────────────────────────────────────────────────────────┘

7 Theorien sind keine isolierten Schichten, sondern eine vollständige Kette:
Scoring → Absorption → Matching → Adaptation → Trust → Investment → Execution
```

---

## 10. Akademische Submission-Empfehlungen

Per diese 7 Theorien können mehrere Papers abgeleitet werden:

| Paper-Titel (vorgeschlagen) | Hauptheorie | Ziel-Journal |
| --- | --- | --- |
| A GenAI Adoption Maturity Model: Extending BPM Maturity for the LLM Era | Capability Maturity + AI-Native | MIS Quarterly / Information Systems Research |
| Absorptive Capacity in Enterprise AI Adoption: Empirical Evidence from 7 Industries | Absorptive Capacity | Strategic Management Journal |
| Task-Technology Fit Beyond Routine Work: When Should Departments Adopt L4-L5 Agents? | TTF | Information & Management |
| From Automation to Dynamic Capability: How AI Reshapes Organizational Sensing | Dynamic Capabilities | Strategic Management Journal |
| Algorithm Aversion in Workflow Automation: A Mixed-Methods Study | Sociotechnical / Trust | Organization Science |
| Valuing AI Foundation Investments as Real Options | Real Options | SMJ / California Management Review |
| AI-Native Living Books: Methodology as Executable Knowledge Artifact | AI-Native LB | Communications of the ACM |

---

## 11. Volle Bibliographie

Siehe §3-8 für Per-Theorie-Referenzen und die komplette Bibliographie in der chinesischen Version.

---

Lizenz & Zitation

Dieses Dokument ist Apache License 2.0; darf verwendet, modifiziert, kommerzialisiert werden, vorausgesetzt die [`../NOTICE`](../NOTICE) Attribution wird beibehalten.
