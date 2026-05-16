# 04 Scenarios — Szenarien, Cases & Case Index

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

> ⚠️ **Wichtiger Hinweis zur wissenschaftlichen Integrität / Important Academic Integrity Disclaimer**
>
> **Alle 7 SAMPLE_CLIENT_CASE_*.md Cases in diesem Verzeichnis (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education) und alle namentlich genannten Hauptfiguren (z. B. „Ming" in `00_Overview/CLIENT_JOURNEY_STORY.md`) sind KI-generierte fiktive Cases, KEINE echten Kundendaten.**
>
> - **Zweck**: Lehrdemonstration, Methodik-Erläuterung, Übung der Stage-1-8-Werkzeugtabellen
> - **Begrenzung**: Alle Zahlen (Zeit, ROI, Personenmonate, Budget, KPI) sind nur Beispiele, **dürfen NICHT für externes Marketing, vertragliche Zusagen oder akademische empirische Belege verwendet werden**
> - **Evidence-Stufe**: gemäß [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 8.9 sind die Cases in diesem Verzeichnis **L0 (AI-Simulated Teaching Case)**, niedriger als L1-Selbstbewertungsfragebogen
> - **Echte longitudinale Cases** werden erst nach Abschluss der 18-24-monatigen empirischen Studie gemäß [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) ersetzt

## 1. Zweck dieses Verzeichnisses

Dieses Verzeichnis ist die **Materialbibliothek und Evidence-Bibliothek** der gesamten Methodik. `01`-`03`, `05`, `06` sind „Methode und Prozess"; dieses Verzeichnis ist „**reale Szenarien, Cases und auswählbare Cases für die Methodik-Implementierung bereitstellen**".

Das Problem: **Das größte Hindernis bei der KI-Einführung ist nicht „wir wissen nicht wie", sondern „wir wissen nicht, was möglich ist, wie andere es machen, wie es danach aussieht".** Dieses Verzeichnis bietet vier Arten von Material: (1) **Szenario-Stories** für jede Rolle/Abteilung (damit Kunden sich „wiedererkennen"), (2) **Case-Schreibstandards und Kontrolltabellen** (für konsistente Cases), (3) **Vollständige Demo-Cases für 7 Branchen** (vom Fragebogen bis Roadmap), (4) **150+ realer LLM-Anwendungs-Case-Index** (schnelle Abfrage nach L-Stufe und Abteilung).

Wer nutzt: Berater (Discovery-Szenarien, Case-Index für PoC-Auswahl), Sales (Cases zur Wertbestätigung), Dozenten (Cases als Demo-Themen), Kunden (vollständige Cases verstehen „wie es nach der Einführung aussieht").

## 2. Position in der Methodik

| Achse | Mapping |
| --- | --- |
| Drei-Phasen-Service-Flow | **Durchgängig** — Discovery nutzt Szenarien, Build nutzt Cases als Themen, Deliver nutzt Cases zur Bestätigung |
| Achtstufige Beratungsstruktur | Unterstützt hauptsächlich **Stage 1 As-Is Snapshot (aktuelle Szenarien), Stage 3 Best Practice Integration (Branchenstandards-Benchmarking)** |
| L1-L5-Reifegrad | Case-Index mappt jeden Case zu einer L-Stufe |
| Engagement Lifecycle | Sales (Discovery Wiedererkennung) + Build (Demo-Themen) |

## 3. Ziele & Nutzen

| Ziel | Nutzen |
| --- | --- |
| Szenario-Stories je Rolle/Abteilung bereitstellen | Kunden können sich „wiedererkennen", Discovery fokussiert schneller |
| Case-Schreibstandards und Kontrolltabellen | Berater schreiben strukturkonsistente, verifizierbare Cases |
| 7 vollständige Branchen-Demo-Cases | Kunden sehen die „komplette Implementierungs-Vista"; neue Berater haben Vorlagen |
| 150+ LLM-Anwendungs-Case-Index (Dual-Achsen-Abfrage) | Kunden/Berater können nach „L-Stufe" oder „Abteilung" sofort nachschlagen |
| Cross-Level-Erwartungsmanagement | Wenn Kunde auf L5-Case zeigt, mit Index ausweisen „Sie sind L2, müssen zuerst aufholen" |

**Wenn dieses Verzeichnis übersprungen wird**: Kunde hat keine Vorstellung „was möglich ist", PoC-Auswahl aus dem Nichts, inkonsistente Case-Qualität, kein Cross-Level-Erwartungsmanagement.

## 4. Workflow & Logik

```text
Discovery-Phase
   → CUSTOMER_SCENARIO_LIBRARY (Szenarien je Rolle, Kunden wiedererkennen)
   → LLM_APPS_CASE_INDEX (nach L-Stufe + Abteilung „kundenrelevante" Cases auswählen)
   → Ausgewählte Cases → PoC-Kandidaten

Kurs / Vorschlag-Phase
   → SAMPLE_CLIENT_CASE_* (vollständige Branchen-Cases zeigen)
   → LLM_APPS_CASE_INDEX (Klassen-Demo, Übungsaufgaben)

Berater schreibt neuen Case
   → CASE_WRITING_STANDARD (Schreibstandard)
   → CASE_CONTROL_TABLES (Kontrolltabelle, direkt kopieren und ausfüllen)
```

| Schritt | Wer | Wann | Input | Output |
| --- | --- | --- | --- | --- |
| Kunden-Wiedererkennung | Berater | Discovery | Szenario-Story-Bibliothek | Vom Kunden bekanntes Schmerz |
| PoC-Kandidaten auswählen | Berater | Nach Diagnose | L-Stufe + Abteilung → Case-Index | PoC-Kandidatenliste |
| Vollständige Cases für Kunden | Sales / Berater | Vorschlag | Same-Industry Sample Case | Kunde versteht Gesamtbild |
| Neue Cases schreiben | Berater | Nach Projektende | Schreibstandard + Kontrolltabelle | Neuer Sample Case |

> Logik: Szenario-Stories sind „**Resonanz auslösen**" (Kunde sagt „ja, so ist es bei uns"); Case-Index ist „**Schnellauswahl**" (nach L-Stufe/Abteilung sofort nachschlagen); vollständige Demo-Cases zeigen „**Gesamtbild**" (vom Fragebogen bis Roadmap); Schreibstandards „**Konsistenz sichern**" (neue Cases stabil in Qualität).

## 5. Dateibeschreibungen

### Szenarien und Standards

| Datei | Zweck |
| --- | --- |
| `CUSTOMER_SCENARIO_LIBRARY.md` | Szenario-Stories je Rolle/Abteilung: CEO, COO, IT, HR, Sales, Customer Service, Marketing, Operations, Finance, HR, IT; jede Story enthält Before, Trigger, AI Flow, Systems, Output, KPI. |
| `CASE_WRITING_STANDARD.md` | Case-Schreibstandard, regelt Schreibweise von L1-L5 Input / Process / Output / Evidence und verifizierbarer Deliverables. |
| `CASE_CONTROL_TABLES.md` | Case-Kontrolltabellen, direkt kopier- und ausfüllbar für Bewertungsaktivitäten, L1-L5 IPOE, Evidence, Stage Gate, Risk Governance, Deliverables-Abnahme. |
| `INDUSTRY_SCENARIOS.md` | 5 Branchen empfohlene Szenarien (Retail/Education/Logistics/Software/Professional Services), je Branche: Einführung, L1-L5-Baseline, Top-10-Szenarien, Risk Governance, 30-Tage Quick Win, Anti-Patterns. |

### Vollständige Demo-Cases (Kunden mit Codenamen)

| Datei | Case |
| --- | --- |
| `SAMPLE_CLIENT_CASE_MANUFACTURING.md` | F&E-Fertigungsindustrie vollständiger Case |
| `SAMPLE_CLIENT_CASE_HOSPITAL.md` | Krankenhaus / Medizinische Einrichtung (hoch-sensible Daten, vollständig On-Prem, menschliche Prüfung) |
| `SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md` | Marketingagentur (Codename: Agentur M) |
| `SAMPLE_CLIENT_CASE_B2B_SALES.md` | B2B-Industriegerätehändler (Codename: Industriegeräte B), Fokus RFP, CRM-Governance, L5 Pre-RFP Team |
| `SAMPLE_CLIENT_CASE_FINANCIAL.md` | Finanzindustrie (Codename: Regionalbank F), vollständig On-Prem, Doppelprüfung |
| `SAMPLE_CLIENT_CASE_GOVERNMENT.md` | Regierungsbehörde (Codename: Stadtdigitalbüro G), vollständig On-Prem, Dreifachprüfung |
| `SAMPLE_CLIENT_CASE_EDUCATION.md` | Bildungseinrichtung (Codename: Tech-Universität E), Hybrid, akademische Ethik |

> Jeder Case durchläuft den vollständigen Flow: Fragebogenergebnis → L-Stufen-Beurteilung → Kursverhältnis → In-Class-Output → 8-Stufen-Analyse → Diagnosebericht-Zusammenfassung → 30/60/90 Roadmap → ROI → Risk Governance.

### L5-Implementierung und Case-Index

| Datei | Zweck |
| --- | --- |
| `CLAWTEAM_WALKTHROUGH.md` | Mit ClawTeam (HKUDS, MIT) komplettes Walkthrough für abteilungsübergreifendes Agent Team (Manufacturing QA Team), inkl. Environment-Setup, Aufgabenkette, Human Gate, Gate-5-Mapping. |
| `LLM_APPS_CASE_INDEX.md` | **LLM-Anwendungs-Case-Index (Multi-Quelle)**. 150+ reale LLM-Apps, **zwei Abfrageachsen**: ① nach L1-L5 / Kurs ② nach Unternehmensabteilung/Prozess (Engineering/Finance/HR/Sales/Marketing/R&D/Operations/Customer Service/Legal/Data/Design/Management). Quellen: awesome-llm-apps (Apache-2.0), ai-engineering-hub (MIT). |

### `*_EN.md`

Englische Sibling-Versionen einiger Dateien.

## 6. Mapping zu anderen Verzeichnissen

| Verzeichnis | Beziehung zu diesem Verzeichnis | Datenfluss |
| --- | --- | --- |
| `01_Assessment` | L-Stufe der Diagnose bestimmt welche Cases auszuwählen | `01` L-Stufe → `04` Case-Filter |
| `02_Course_Design` | Cases/PoC-Index sind Quelle für Klassen-Demo und Übungsaufgaben | `04` Cases ↔ `02` Kursthemen |
| `03_Consulting_Report` | Stage 3 Branchen-Best-Practice-Benchmarking zitiert Cases | `04` Cases → `03` Stage 3 |
| `05_Sales` | Vollständige Cases und Szenarien sind Wert-Bestätigung für Sales-Material | `04` Cases → `05` Sales-Bestätigung |
| `00_Overview` | Szenario-Stories sind Material für die Story | `04` ↔ `00` |
| `90_References` | Drittanbieter-Zitate für Case-Index (awesome-llm-apps / ai-engineering-hub) | `90` Zitat → `04` |

## 7. Häufige Nutzungsszenarien

- **Discovery Wiedererkennung**: `CUSTOMER_SCENARIO_LIBRARY.md` mit Kundenrolle abgleichen, fragen „welche Story ist wie Sie?".
- **PoC auswählen**: Nach L-Stufen-Diagnose, in `LLM_APPS_CASE_INDEX.md` §3 nach L-Stufe oder §4 nach Abteilung, 3-5 kundenrelevante auswählen.
- **Vorschlag-Bestätigung**: Manufacturing-Kunden `SAMPLE_CLIENT_CASE_MANUFACTURING.md` zeigen, vollständiges Implementierungsbild demonstrieren.
- **Cross-Level-Erwartung**: Kunde zeigt auf L5-Case → mit Index seine L-Stufe und Voraussetzungs-Kurse ausweisen.
- **Neuen Case schreiben**: Nach Projektende mit `CASE_WRITING_STANDARD.md` + `CASE_CONTROL_TABLES.md` als neuen Sample Case schreiben.

---

## ⭐ Cross-Topic Quick References: 5 Kernthemen, wo zu finden

Die ganze Methodik hat 5 Hauptarterien durch alle Verzeichnisse. So bezieht sich dieses Verzeichnis auf jede:

| Cross-Topic | Hauptort | Wie dieses Verzeichnis anbindet |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + Drei-Engine-Co-Lesen** | Root [`README_DE.md`](../README_DE.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | Cases können mit Claude Code Tier-2-Workflows ausgeführt werden: `/simulate-engagement` simuliert vollen 6-Wochen-Beratungseinsatz, `/parallel-perspectives` 6 Stakeholder-Perspektiven, `/devil-pair-debate` debattiert Wertannahmen der Cases |
| 🎓 **Akademische Grundlage (7 Säulen)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | ROI-Argumentation der Cases entspricht **Real Options** (warum Phase 1 mit scheinbar NPV ≈ 0 trotzdem lohnt); To-Be-Design der Cases entspricht **Task-Technology Fit** (welche Aufgaben L4 erreichen, welche bei L2 bleiben) |
| 📚 **L1-L5 Kursbildung** | [`../02_Course_Design/`](../02_Course_Design/) | LLM Apps Case Index nach L-Stufe klassifiziert, direkt als PoC wählbar; `POC_SCENARIO_SPECS.md` + `N8N_WORKFLOW_TEMPLATES.md` verwandeln Cases in L3-Klassen-Hands-on-Themen |
| 🔁 **Beratung / 8 Stufen + Phase A→B→C Closed-Loop** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Cases sind Phase-A-Discovery-„Wiedererkennungsmaterial"** (damit Kunde sagt „ja, so ist es bei uns"); Branchen-Best-Practice gemappt auf Stage 3; die 7 vollständigen Sample Cases sind Vorlagen für den Phase-B-Bericht |
| 📖 **References / Acknowledgments** | [`../90_References/`](../90_References/) §2 Acknowledgments | LLM Apps Case Index Quellen: `Shubhamsaboo/awesome-llm-apps` (Apache-2.0) + `patchy631/ai-engineering-hub` (MIT), volle Appreciation Cards in [`../90_References/README.md`](../90_References/README.md) §2.4; ClawTeam Walkthrough von `HKUDS/ClawTeam` (MIT) |
