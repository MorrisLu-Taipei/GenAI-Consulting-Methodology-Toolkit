# 8-Stufen Consulting-Flow: Vollständige Szenario-Story und Closed-Loop-Design

> 🌐 Sprache: [繁體中文](EIGHT_STAGE_FLOW_STORY.md) ｜ [English](EIGHT_STAGE_FLOW_STORY_EN.md) ｜ Deutsch ｜ [Français](EIGHT_STAGE_FLOW_STORY_FR.md) ｜ [Español](EIGHT_STAGE_FLOW_STORY_ES.md) ｜ [日本語](EIGHT_STAGE_FLOW_STORY_JA.md) ｜ [한국어](EIGHT_STAGE_FLOW_STORY_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Letzte Aktualisierung: 2026-05-15

---

> **Was dies ist**: Die 8-Stufen-Consulting-Methodik geschrieben als vollständige, reproduzierbare, debattierbare Closed-Loop-Story. Von der Fragebogen-Intake bis zum Implementation Plan, jeder Schritt hat klare Trigger, Deliverables, Unterschriften und Lock-In-Beziehungen mit dem nächsten Schritt.
>
> **Was dies nicht ist**: keine 6-Wochen lineare Marathon-Erzählung. Sondern **ein 3-Phasen-Vertragsmodell + Mid-Engagement Client Signature + Quarterly Loopback** vollständiger wissenschaftlicher Management-Prozess.

---

## 0. Verbesserungen gegenüber einem linearen Walk-Through (3 bessere Design-Entscheidungen)

Eine typische Nutzer-Intuition:
> Fragebogen + AI As-Is Assessment → vergleichen mit RM → Maturity + Cases Benchmarking → scoren → Kunden Report zeigen → Kunde wählt Ideal Practice → analysieren was benötigt → TO-BE Empfehlungen → Consulting Report → Implementation Plan

**Die Richtung ist richtig**. Tiger AI baut 3 Verbesserungen darauf:

| # | Verbesserung | Warum stärker |
| --- | --- | --- |
| **1** | **Drei Vertragsphasen** (Phase A Diagnostic / Phase B Strategy / Phase C Implementation), kein 6-Wochen-Marathon | Kunde committed niedrig-Risiko zuerst zu Phase A, entscheidet über B / C basierend auf Ergebnissen; Berater vermeidet Über-Committment |
| **2** | **Ende von Phase A: ein Mid-Engagement Assessment Report wird als Deliverable unterzeichnet** vor Launch der Phase B Ideal Practice Workshop | Kunde wird zuerst durch Radar leere Zellen geschockt, dann wählt Ideal — vermeidet Fantasie; Mid-Report ist auch ein standalone Deliverable |
| **3** | **Jedes Quartal, das Reference Model Radar erneut besuchen** (geht nach Eintritt in Phase C Implementation weiter) | Nicht „erledigt ist gut" sondern **„ist die Struktur tatsächlich runder geworden?"** — das ist der wissenschaftliche Closed-Loop-Falsifikations-Mechanismus |

> **Warum stärker als ein linearer 6-Wochen-Marathon**: linear zwingt Kunde, 6 Wochen + 24 Monate auf einmal zu committen — psychologische Barriere zu hoch; 3 Phasen teilen Entscheidungen, reduzieren Risiko, erhöhen Akzeptanz.

---

## 1. Drei-Phasen-Vertragsmodell Überblick

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  Phase A: Diagnostic           Phase B: Strategy           Phase C:        ║
║                                                            Implementation  ║
║  ─────────────                ─────────────              ─────────────     ║
║  2 Wochen · NT$ 800K          4 Wochen · NT$ 2M          24 Monate · NT$ 7M║
║                                                                             ║
║  Stage 1 + 2 + 3 Materialien Stage 3 Ideal Practice      Stage 7 + 8        ║
║                                + Stage 4 + 5                                ║
║                                                            (Quarterly       ║
║                                                            Radar Revisit)  ║
║                                                                             ║
║  Deliverable:                Deliverable:                Deliverable:      ║
║  Mid-Engagement              Voller Diagnostic Report    Transformation    ║
║  Assessment Report           + Ideal Practice            Roadmap +         ║
║  (Kunden-Receipts)           Definition (3-Parteien-     Change Mgmt +     ║
║                              Unterschrift)               Value Tracking +  ║
║                                                          Quarterly Logs    ║
╚═══════════════════════════════════════════════════════════════════════════╝
                ↑                       ↑                       ↑
            Gate A                  Gate B                   Gate C
        Kunde entscheidet,      Kunde entscheidet,       Kunde entscheidet jedes
        zu B fortzufahren       zu C fortzufahren        Quartal fortzufahren
```

**Wissenschaftliche Signifikanz**: jedes Gate ist „ein Exit-Punkt, an dem der Kunde aussteigen kann" — der Berater **designt das nur mit Vertrauen**, dass das vorherige Phase-Deliverable **gut genug ist, dass der Kunde fortfahren will**.

---

## 2. Der Protagonist: Client M

> ⚠️ **„Client M / MingChang Packaging" ist ein AI-generiertes fiktives Unternehmen**, KEIN realer Kunde. Alle Scale-, KPI-, Budget- und Timeline-Zahlen sind **nur illustrativ**, für Methodik-Lehrzwecke. Siehe [`../04_Scenarios/README_EN.md`](../04_Scenarios/README_EN.md) für vollständigen akademischen Integritäts-Disclaimer.

- **Industrie**: Halbleiter Packaging & Testing (FATP)
- **Scale**: 700 Mitarbeiter, NT$ 1,2 Mrd Jahresumsatz
- **Trigger**: Drei direkte Wettbewerber deployten AI Quality Inspection und Complaint Agents; Customer A's Quarterly Orders sanken 18%
- **Pain Points**: Complaint Response 5 Tage (Branche 1 Tag); Proposal Turnaround 4 Tage (Branche 1,5 Tage); Defekt-Rate 3,2% (Branche 1,8%)
- **Beschränkungen**: Budget-Cap NT$ 8M; Prozessdaten on-prem; IT 2 FTE, kein Wachstum
- **Rollen**: CEO (Sponsor), COO, IT Director (potenzieller AI Champion), QC Head, Sales Head, CS Head, HR, Compliance

---

## 3. Phase A: Diagnostic (2 Wochen, NT$ 800K)

### Trigger

M Unternehmens CEO erhält Tiger AI Outreach Email + sieht das Open-Source-Methodik-Repo auf GitHub; Sekretär scheduled 30-Min Intro.

### Pre-Engagement: 10-Fragen Quick Survey (nächste Woche gesendet)

CEO selbst-füllt die 10-Fragen-Version von [`01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) (5 Min).

**Auto-scored Result**:

```
6-Dimensionen Radar:
  Tool Usage              1 / 4 (einige Execs nutzen ChatGPT privat)
  Knowledge Sedimentation 0 / 4 (kein Wiki, keine SOP)
  Process Automation      1 / 4 (Finance 1 Power Automate Flow)
  System Integration      2 / 4 (ERP/CRM in Silos)
  Agent Application       0 / 4 (keine)
  Governance & ROI        1 / 4 (keine AI Policy)
Total: 5 / 24 → preliminary L1
```

CEO sieht das Radar → **erster Schock** → stimmt zu, Phase A Vertrag zu unterzeichnen.

### Phase A Flow (Woche 1-2)

#### Woche 1 ── Stage 1 As-Is Snapshot: Zuhören, Beobachten, kein Kommentar

| Tag | Aktion | Tool | Output |
| --- | --- | --- | --- |
| Tag 1-2 | Exec Interviews (CEO/COO/CIO × 60 Min) + Dept Head Interviews (QC/Sales/CS/IT/HR × 90 Min) | Tool 1.1 (40-Q Bank) | Aufnahmen + Summaries |
| Tag 3 | Operator Interviews (Line/Sales/CS × 3 each × 30 Min) | Tool 1.1 Section C | Summaries |
| Tag 4 | AI Usage Inventory + Systems Inventory | Tool 1.2 + 1.3 | Shadow IT Risk Map + System Map |
| Tag 5 | Walkthrough von 3 Key Processes + Swimlanes zeichnen | Tool 1.4 | 3 As-Is Process Maps |

**Ende Woche 1**: Berater sagt Kunde „jetzt wissen wir, was Ihr Unternehmen tut." **Kein Kommentar, keine Empfehlung.**

#### Woche 2 ── Stage 2 Reference Model Alignment + Stage 3 Material Prep

| Tag | Aktion | Tool | Output |
| --- | --- | --- | --- |
| Tag 6 | Reference Model wählen: SCOR + APQC + Tiger AI L1-L5 | Tool 2.1 | RM Selection Rationale |
| Tag 7-8 | Mapping Worksheet: As-Is in RM-Zellen lokalisieren | Tool 2.2 | Mapping-Tabelle |
| Tag 9 | Standard Capability Gap Checkliste + Dual Radar | Tool 2.3 + 2.4 | Zwei Radare (APQC + Tiger AI) |
| Tag 10 | Benchmark Case Prep (Halbleiter aus 5 Stubs + 2 Same-Industry Cases wählen) | Tool 3.1 + 3.3 | 3 Best-Practice Profile |

> **Phase A Disziplin**: Tag 10 Berater **läuft NOCH NICHT Ideal Practice Workshop**. Nur Materialien — verwendet in nächster Phase.

### Phase A Deliverable: Mid-Engagement Assessment Report (Kunden-Receipts)

**Tag 11-12 Report schreiben → Tag 13-14 Client Review → Tag 14 Closeout Meeting**

Mid-Engagement Report (10-15 Seiten):

1. **Executive Summary**: „Per internationaler Standards zeigt Ihr Unternehmen strukturelle Gaps in SCOR Make/Deliver, APQC 11.x Knowledge, Tiger AI L1-L3."
2. **As-Is Snapshot**: Interview-Summaries + System Map + 3 Swimlanes
3. **Reference Model Mapping**: Standard Capability Gap Checkliste
4. **Dual Radar**: APQC + Tiger AI L1-L5 (gestrichelt = Benchmark, durchgezogen = Unternehmen)
5. **Industry Best Practice Materialien**: 3 Same-Industry Benchmark Profile (nur Materialien — **noch keine Schlussfolgerungen gezogen**)
6. **Empfehlung nächste Phase**: Phase B Ideal Practice Workshop (halber Tag) + Stage 4-5 Analyse

### Gate A: Kunde entscheidet, ob zu Phase B fortgefahren wird

**Was passiert beim Closeout Meeting**:

- CEO sieht Radar: „Ich dachte, wir machen okay — unter dem Standard sind diese Zellen 0?" → **zweiter Schock**
- COO blättert durch Swimlanes: „Unser Complaint-Prozess hat wirklich diese Löcher..." → Pain Points konkretisiert
- IT Director sieht Shadow IT monatliche Ausgaben: „Privates ChatGPT verbrennt NT$ 24.000 mit Daten leakend..." → Risiko konkretisiert

**90% der Kunden unterzeichnen Phase B**. Weil:

- Radar-Gaps sind nicht berater-gesagt — internationaler Standard gesagt → **objektiv**
- Pain ist in Mitarbeiter-Interview-Aufnahmen → **verifizierbar**
- Same-Industry-Firmen haben es schon gemacht → **erreichbar**

> **Phase A's Design-Ziel IST dieser Schock**: Kunde **sieht den Gap selbst**, nicht vom Berater gesagt.

---

## 4. Phase B: Strategy (4 Wochen, NT$ 2M)

### Woche 3 ── Stage 3 Ideal Practice Co-Creation Workshop (halber Tag)

**Tag 15 morgens** ─ Tool 3.6 Co-Creation Workshop

| Schritt | Aktion | Zeit | Output |
| --- | --- | --- | --- |
| 1. Material Display | Berater **zeigt nur, empfiehlt nicht** Tool 3.1/3.3/3.4/2.7 4-Schichten-Architektur | 30 Min | Shared Materialien |
| 2. Independent Voting | Jede Person **unabhängig** schreibt auf Sticky Notes „was ich will, dass wir in 12 Monaten werden" | 45 Min | N Sticky Notes |
| 3. Collective Consensus | Auf 4-Schichten-Architektur posten, Konsens / Divergenz finden | 60 Min | v1 Ideal Practice Draft |
| 4. Reality Check | Berater interveniert zuerst, nutzt Tool 6.3 zur Challenge Feasibility | 45 Min | v2 Ideal Practice |
| 5. Define Table | v2 als „Ideal Practice Definition Table" schreiben | 30 Min | Signierte Version Definition Table |
| 6. **3-Parteien-Unterschrift** | CEO + Sponsor + AI Champion | 15 Min | Öffentliches, auditierbares Dokument |

**M Unternehmens signierte Ideal Practice Definition Table (Auszug)**:

| # | Capability | RM Category | 12-Monats-Target | Evidence Criteria |
| --- | --- | --- | --- | --- |
| 1 | Complaint Response | APQC 4.4 + Tiger AI L3 | 90% in 1 Std + 24 Std Human Reply | n8n + Reviewer Sign-off Rate ≥ 95% |
| 2 | Knowledge Sedimentation | APQC 11.x + Tiger AI L2 | ≥ 20 Skills monatlich hinzugefügt | Skill Library Git + Owner + IPOE |
| 3 | Process Root Cause | SCOR Make + Tiger AI L4 | Anomaly → Hypothese ≤ 1 Std | Hermes Agent + 5 Tasks Reviewer Pass |

> **Diese Table ist der Anker des gesamten Engagements**. Alle nachfolgenden Stage 4-8 Berechnungen basieren darauf; Kunde kann seine eigenen signierten Targets nicht verleugnen.

### Woche 3-4 ── Stage 4 Gap Analysis + Stage 5 Problem Definition

#### Stage 4: Gap = (Client Ideal − Client As-Is)

| Tag | Aktion | Tool | Output |
| --- | --- | --- | --- |
| Tag 16-17 | M/B/R Klassifikation + Impact × Effort | Tool 4.1 + 4.2 | Gap Matrix |
| Tag 18 | Prioritization Worksheet | Tool 4.3 | Priorität-Ranking |

#### Stage 5: 80/20 Convergence zur Root Cause

| Tag | Aktion | Tool | Output |
| --- | --- | --- | --- |
| Tag 19 | 80/20 Convergence + 5 Whys | Tool 5.1 + 5.2 | Core Lesion Liste |
| Tag 20-21 | Executive Problem Statement | Tool 5.3 + 5.4 | Ein-Satz-Definition |

**M Unternehmens Executive Problem Statement**:

> M Unternehmen fehlt die Rolle, das Tool und der Anreiz für „Knowledge Asset-Isierung." 80% der Gaps (langsame Complaints / langsame Quotes / keine Knowledge Sedimentation / langsame Root Cause) stammen aus „dieselbe Sache wiederholt gemacht, niemand sedimentiert, niemand wiederverwendet."

### Woche 4 ── Stage 6 Phased Goals + Stage 7 To-Be Design

#### Stage 6: Ideal in absorbierbare Schritte zerlegen

| Tag | Aktion | Tool | Output |
| --- | --- | --- | --- |
| Tag 22 | Ultimate Ideal → Phase 1/2/3 Dekomposition | Tool 6.1 | Dekompositions-Tabelle |
| Tag 23 | Organizational Absorption Assessment (6 Dimensionen) | Tool 6.3 | Absorption Score |
| Tag 24 | Stage Gate Criteria | Tool 6.2 | L1-L5 Gate Checklisten |

> **M Unternehmens Absorption Assessment findet, IT hat nur 2 FTE; Phase 2 braucht +0,5**. Entscheidung: Phase 2 von 6 → 9 Monate verlängern. **Diese Anpassung kommt vom Kunden, der die Daten selbst betrachtet, nicht von Berater-Empfehlung**.

#### Stage 7: Ein To-Be Operating Model pro Phase

| Tag | Aktion | Tool | Output |
| --- | --- | --- | --- |
| Tag 25-26 | Phased To-Be Operating Models (3 Diagramme) | Tool 7.1 | 3 Diagramme |
| Tag 27 | Human-AI Collaboration + HITL Nodes | Tool 7.2 | Per-Prozess Split |
| Tag 28 | Skill/Workflow/Agent Map + Integration Architecture | Tool 7.3-7.6 | 3 Maps + Variant B Hybrid |

### Phase B Deliverable: Voller Diagnostic Report + Ideal Practice Definition Table

**Tag 29-30 Report schreiben → Tag 31-32 Client Review → Tag 32 Closeout Meeting**

Voller Diagnostic Report (30-50 Seiten) per [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) 14-Sektionen-Struktur.

### Gate B: Kunde entscheidet, ob zu Phase C fortgefahren wird

**95% der Kunden unterzeichnen Phase C**. Weil:

- Ideal Practice wurde **von ihnen unterzeichnet** → unverleugbar
- Gap wird durch Subtraktion berechnet → **verifizierbar**
- Phase 1/2/3 passt zu organisatorischer Absorption → **erreichbar**

---

## 5. Phase C: Implementation (24 Monate, NT$ 7M)

### Stage 8 Implementation & Change

**Erster Monat (Monat 1)**

| Tag | Aktion | Tool | Output |
| --- | --- | --- | --- |
| Tag 33 | Transformation Roadmap (24 Mo / 6 Quartale) | Tool 8.1 | Roadmap |
| Tag 34 | Change Management Plan + Resistance Playbook | Tool 8.2 | Change Plan |
| Tag 35 | RACI + Permission Matrix + Audit Log | Tool 8.3 + 8.4 + 8.7 | Governance Docs |
| Tag 36 | Value Tracking Matrix (5 Dimensionen) | Tool 8.5 | Dashboard Spec |
| Tag 37 | Risk Register (Case Failures inkorporierend) | Tool 8.6 | Risk Log |
| Tag 38 | AI Ethics Checkliste | Tool 8.8 | Signed Ethics |
| Tag 39 | SOW + Phase 1 Kickoff | — | Phase 1 launched |

### Phase 1 (Monate 1-6): Foundation

- L1 unternehmensweites OpenWebUI live
- 5 Core Skills veröffentlicht
- AI Policy signiert von > 90%
- Prompt Library ≥ 30 Einträge

**Ende Monat 6 → L1 Gate Acceptance + Stage 2 Radar erneut besuchen**:

```
APQC 11.x Knowledge:  0 → 2 (Skill Library startend)
Tiger AI L1:          0 → 4 (volles OpenWebUI + 92% Policy signiert)
Tiger AI L2:          0 → 2 (5 Skills)
```

> Das Radar **ist wirklich runder**. Kunde wird emotional: „So ist das also wissenschaftliches Management."

### Phase 2 (Monate 6-15): Optimization

- L2 Skill Library ≥ 15 Einträge
- L3 n8n Workflow ≥ 3 live
- HITL Nodes vollständig in Place

**Ende Monat 15 → L2/L3 Gate + Radar Revisit**:

```
APQC 4.0 Deliver: 1 → 3 (Complaint Response 5 Tage → 1 Tag) ✓ Ideal erreicht
APQC 11.x:        2 → 3 (Knowledge Sedimentation stabil) ✓ Ideal erreicht
Tiger AI L3:      0 → 2 (n8n PoC live)
```

### Phase 3 (Monate 15-24): Excellence

- L4 Hermes Agent besteht 4A-4E
- L5 ClawTeam Cross-Dept 1 erfolgreiche Rehearsal

**Ende Monat 24 → L4/L5 Gate + Final Radar**:

```
SCOR Make + Tiger AI L4: 0 → 3 (Hermes Agent besteht) ✓ Ideal erreicht
Tiger AI L5:             0 → 2 (ClawTeam Cross-Dept Rehearsal)
```

### Gate C Quarterly: Kunde kann jedes Quartal entscheiden

Jedes Quartal muss:

1. Quarter Gate Acceptance (per Tool 6.2 Checkliste)
2. Stage 2 Radar erneut besuchen (Verbesserung quantifizieren)
3. Value Tracking Matrix 5-Dimensionen Review
4. Kunde entscheidet, ob nächstes Quartal voranschreiten, anpassen oder pausieren

> Nach 24 Monaten: M Unternehmen Complaint Response 1 Tag, Defekt-Rate 2,0%, Customer Churn null, Stage 2 Radar **ändert sich von zackiger Linie zu nahezu rund**.

---

## 6. Vollständiges Closed-Loop-Diagramm

```
                          ┌──────────────────┐
                    ┌────►│ Phase A Diag 2W   │
                    │     │ Stage 1 + 2 + 3   │
                    │     │   Material Prep   │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Mid Report        │ ← Phase A Deliverable
                    │     │ (Kunden-Receipts) │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate A
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase B Strat 4W  │
                    │     │ Stage 3 Ideal     │
                    │     │ + Stage 4 + 5     │
                    │     │ + Stage 6 + 7     │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Voller Report     │ ← Phase B Deliverable
                    │     │ + Ideal Practice  │
                    │     │ (3-Parteien-Sign) │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate B
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase C Impl 24M  │
                    │     │ Stage 8           │
                    │     │ Transformation +  │
                    │     │ Change + Value    │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase 1/2/3       │
                    │     │ Stage Gate accept │
                    │     └────────┬─────────┘
                    │              │
                    │     Quarterly Gate C
                    │              │
                    │     ┌────────▼─────────┐
                    └─────┤ Stage 2 Radar    │
                          │ erneut besuchen  │
                          │ (runder?)        │
                          └──────────────────┘
                                  
                          Diese Feedback-Linie ist
                          der Core-Falsifikations-
                          Mechanismus des
                          wissenschaftlichen Closed Loop
```

---

## 7. Warum dieser Flow Client-Debate standhält

Für jede mögliche Challenge die Response-Location:

| Challenge | Location | Evidence |
| --- | --- | --- |
| „Woher wissen Sie, dass wir bei L1 sind?" | Phase A Mid-Report §2 Radar | 10-Q Survey + Aufnahmen + System Inventory |
| „Warum sind diese Zellen 0?" | Phase A §3 RM Mapping | APQC / Tiger AI öffentliche Standards |
| „Wer hat das Target gesetzt?" | Phase B §5 Ideal Practice Table | **Kunde selbst signiert, 3-Parteien-Unterschrift** |
| „Warum ist der Gap so groß?" | Phase B §6 Gap Analysis | Gap = (Ihr signiertes Ideal − Ihr As-Is) Formel |
| „Warum Customer Service vor Sales?" | Phase B §6.2 | Impact × Effort Matrix |
| „Warum 24 Monate?" | Phase B §8 + Tool 6.3 | Case Benchmark + Organizational Absorption |
| „Was wenn es nicht funktioniert?" | Phase C §13 Risk Register | Trigger + Owner + Mitigation |
| „Wie beweisen Sie, dass es verbessert hat?" | Quarterly Gate C | Stage 2 Radar + Value Tracking 5 Dimensionen |
| „Letzter Berater sagte L3, Sie sagen L2 — wer hat Recht?" | Public 0-4 Skala + Evidence | Jeder Dritte kann unabhängig verifizieren |

---

## 8. Mapping auf Nutzers Original-Flow

| Nutzers Schritt | Phase | Stage | Verbesserung |
| --- | --- | --- | --- |
| 1. Fragebogen + AI As-Is | Phase A W1 | Stage 1 | + 10-Q Quick Screen als Pre-Engagement |
| 2. Vergleichen mit RM | Phase A W2 | Stage 2 | 4-Schichten-Architektur + Dual Radar |
| 3. Maturity + Cases Benchmarking → Score | Phase A Ende W2 | Stage 3 Materialien | Cases müssen Benchmark-grade sein (9 Felder) |
| 4. **Kunde sieht Assessment Report** | **Phase A Deliverable** | — | **Neu: Mid-Report als standalone Deliverable + Client Receipt** |
| 5. Kunde wählt Ideal Practice | Phase B W3 | Stage 3 Tool 3.6 | **Kunde signiert, nicht Berater verschreibt** |
| 6. Analysieren was benötigt | Phase B W3-W4 | Stage 4 + 5 | Gap = Ideal − As-Is, 80/20 Convergence |
| 7. TO-BE Empfehlungen | Phase B W4 | Stage 6 + 7 | Phased + Organizational Absorption Assessment |
| 8. Consulting Report | Phase B Deliverable | — | 14-Sektionen Voller Report + signiertes Ideal Practice |
| 9. Implementation Plan | Phase C Kickoff | Stage 8 | Change Mgmt + Value Tracking + Audit |
| **(fehlend)** | **Quarterly Revisit** | — | **Neu: jedes Quartal Stage 2 Radar erneut besuchen (wissenschaftlicher Closed Loop)** |

---

## 9. Beziehung zu anderen Dokumenten

| Dokument | Beziehung zu diesem |
| --- | --- |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 | Bietet 8-Stufen-Definitionen und Datenfluss; dieses Doc ist die volle Process-Narrative |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Bietet „warum so designt" wissenschaftliches Argument; dieses Doc ist „wie es tatsächlich läuft" |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | Bietet Per-Stage Tool-Tabellen |
| [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) | Bietet Phase B Deliverable 14-Sektionen-Struktur |
| [`../04_Scenarios/`](../04_Scenarios/) | Bietet Benchmark-grade Cases für Phase A |
| [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) | Bietet Engagement / Pricing / Delivery SOP |

---

## 10. Abschluss: Warum der Closed Loop Wissenschaft ist

Dieser Flow **ist kein linearer Marathon** sondern **ein Closed Loop mit Feedback**:

- **Jedes Gate ist ein Exit-Punkt** → Berater **hat Vertrauen**, das so zu designen (das vorherige Deliverable muss gut genug sein, dass der Kunde fortfahren will)
- **Jedes Deliverable hat Client Signature** → nachfolgendes Reasoning kann nicht verleugnet werden
- **Jedes Quartal Stage 2 Radar erneut besuchen** → Struktur tatsächlich runder werdend = Erfolg, nicht „PoC gemacht = Erfolg"

**Das ist wissenschaftliches Management**:

- Objektiver Startpunkt (internationaler Standard + Kunden-Unterschrift)
- Verifizierbarer Prozess (jedes Stage Gate Criteria)
- Falsifizierbarer Endpunkt (Dual Radar Before/After + Value Tracking 5 Dimensionen)

Falls irgendjemand sagt „Tiger AI Methodik funktioniert nicht", müssen sie **challengen**:

- Ist APQC PCF falsch?
- Ist Rosemann BPM Schule falsch?
- Zählt nicht das eigene signierte Ideal Practice des Kunden?
- Zählt nicht unser Quarterly Radar Loopback?

**Schwer zu tun.** Deshalb haben wir in dieses Closed-Loop-Design investiert.

---

Lizenz & Zitation

Dieses Dokument ist Apache License 2.0; darf verwendet, modifiziert, kommerzialisiert werden, vorausgesetzt die [`../NOTICE`](../NOTICE) Attribution wird beibehalten.
