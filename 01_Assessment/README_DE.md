# 01 Assessment — KI-Reifegrad-Diagnose

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Zweck dieses Verzeichnisses

Dieses Verzeichnis ist die **erste Phase: Diagnose (Diagnose)** des Drei-Phasen-Service-Flows. Es löst eines der grundlegendsten Probleme der Beraterarbeit: **„Das Unternehmen sagt 'wir nutzen KI', aber auf welcher Stufe genau? Was fehlt? Wo soll man ansetzen?"**

Ohne objektive Diagnose können Berater Kurse nur nach subjektiven Kundenbeschreibungen zusammenstellen — das Ergebnis ist oft Niveau-Sprünge (Kunde hat nicht einmal L1-Vollnutzung, will aber L4-Agent) oder falsche Schwerpunkte (es fehlt Governance, aber es werden ständig Werkzeuge hinzugefügt). Dieses Verzeichnis verwandelt mit drei Fragebogen-Längen + Scoring-Modell + Unternehmensprofil-Erhebung „diffuse Eindrücke" in **objektive, quantifizierbare, vergleichbare L1-L5-Scores und Lücken-Radardiagramme auf sechs Dimensionen**.

Wer nutzt dieses Verzeichnis: Sales (10-Punkte-Version für Lead-Qualifizierung), Berater (25/50-Punkte-Version für Vor-Kurs- und Vor-Interview-Inventarisierung), IT/AI Champion (Unternehmensprofil-Fragebogen).

## 2. Position in der Methodik

| Achse | Mapping |
| --- | --- |
| Drei-Phasen-Service-Flow | **Diagnose** — erste Phase |
| Achtstufige Beratungsstruktur | **Stufe 1 Ist-Erfassung** (Diagnoseergebnis ist Kerninput für Stufe 1) |
| L1-L5-Reifegrad | Dieses Verzeichnis ist das Werkzeug zur „**Feststellung, auf welcher Stufe der Kunde ist**" |
| Engagement Lifecycle | **Sales — Lead Qualification (10-Punkte) / Discovery (25/50-Punkte)** |

## 3. Ziele & Nutzen

| Ziel | Nutzen |
| --- | --- |
| Subjektive Vermutung durch objektive Scores ersetzen | Berater hat Grundlage für Kursauswahl, nicht nur Bauchgefühl |
| Lücken auf sechs Dimensionen finden (Werkzeuge/Wissen/Prozess/Integration/Agent/Governance-ROI) | Wissen, wo der Kunde stark / schwach ist |
| Direkt drei Empfehlungen ableiten | Kursverhältnis + Deployment-Modus + PoC-Szenario in einem Schritt |
| Drei Fragebogen-Längen für drei Verkaufsphasen | Lead-Entwicklung, Vor-Kurs, Vor-Interview — je passendes Werkzeug |
| Automatisierbar | Fragebogen → Scoring → Bericht vollautomatisch, Berater interpretiert nur |

**Wenn dieses Verzeichnis übersprungen wird**: Kursverhältnis nach Gefühl, Kundenerwartung unkontrollierbar (zeigt auf L5-Case „ich will das", ohne zu wissen, dass sie selbst L2 sind), Beraterbericht ohne objektiven Startpunkt.

## 4. Workflow & Logik

```text
10-Punkte-Schnellfragebogen (Lead-Entwicklung, 3 Min)
   → Lead-Qualifikation + initiale L-Stufen-Position
25-Punkte-Fragebogen (Vor-Kurs, 8 Min, vom Kunden-Manager ausgefüllt)
   → Sechs-Dimensionen-Scores + Radar-Diagramm
50-Punkte-Fragebogen (Vor-Berater-Interview, 20 Min, IT/AI Champion)
   → Vollständige Inventarisierung + offene Fragen
Unternehmensprofil-Fragebogen (35 Punkte)
   → JSON Profile Bundle (System / Risiko / Deployment-Präferenz / Budget)
        ↓ Merge
   Auto-Scoring → L1-L5-Stufe + Sechs-Dimensionen-Radar
        ↓ Ableitung
   ① Empfohlenes Kursverhältnis  ② Empfohlener Deployment-Modus  ③ Empfohlenes PoC-Szenario
```

| Schritt | Wer | Wann | Input | Output |
| --- | --- | --- | --- | --- |
| 10-Punkte-Quickscreen | Sales | Lead-Entwicklung | Potentieller Kunde | Qualifikation + initiale L-Stufe |
| 25-Punkte Vor-Kurs-Diagnose | Kunden-Manager-Gruppe | 1 Woche vor L1-Kursstart | 25-Punkte-Fragebogen | Sechs-Dimensionen-Scores |
| 50-Punkte vollständige Inventarisierung | Kunden-IT / AI Champion | Vor Berater-Interview | 50 Punkte + Profil-Fragebogen | Vollständiges Profile Bundle |
| Auto-Scoring | System (Sheets/Notion/n8n) | Nach Fragebogen-Einreichung | Fragebogen-Antworten | L-Stufe + Radar + 3 Empfehlungen |
| Interpretation | Berater | Nach Auto-Bericht | Auto-Bericht | Kundenspezifische Vorschlagrichtung |

> Logik: Fragebogen ist nur **Input**; das eigentliche Output ist „**L-Stufe + Sechs-Dimensionen-Lücken + 3 Empfehlungen**". Diese drei werden weitergegeben — Kursverhältnis → `02_Course_Design`; Deployment-Modus → `03` To-Be-Design; PoC-Szenario → `04_Scenarios` Case-Index. Diagnose ist kein Endpunkt, sondern der Schalter, der die nachfolgenden drei Verzeichnisse „einschaltet".

## 5. Dateibeschreibungen

### `AI_MATURITY_QUESTIONNAIRE.md`

KI-Reifegrad-Fragebogen in drei Längen 10 / 25 / 50 Punkte. 10-Punkte-Version für Sales-Schnellbeurteilung; 25-Punkte-Version 4-5 Fragen pro Dimension für Vor-Kurs; 50-Punkte-Version plus Deployment-Modus und Systeminventar für Vor-Berater-Interview. Alle drei Versionen nutzen die 0-4-Punkte-Skala und die Sechs-Dimensionen-Architektur.

### `AI_MATURITY_SCORING_MODEL.md`

Scoring-Logik und Entscheidungsregeln. Enthält: Scoring der sechs Dimensionen (Werkzeugnutzung, Wissensspeicherung, Prozessstandardisierung, Systemintegration, Agent-Anwendung, Governance-ROI), Gesamtpunkt-Schwellen für L1-L5, **Hauptreifegrad vs lokaler Reifegrad** (warum eine Abteilung lokal L4 sein kann, aber gesamt L2), Empfehlungsregeln für Deployment-Modus und Kursverhältnis.

### `AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`

Definition of Done, Deliverables, Evidence, Owner, Stage Gate, Fail Condition, Next Level Entry Criteria für jede Stufe L1-L5. Es definiert „wie 'fertig' auf jeder Stufe aussieht, welche Evidence als Beweis benötigt wird" — die Grundlage der Stage-Gate-Abnahme.

### `FILLABLE_QUESTIONNAIRE.md`

Render-Spezifikation, die 10/25/50 Punkte in ausfüllbare Formulare umsetzt — Fragetypen (radio / 0-4 scale / multi-choice / Kurzantwort), Seitensegmentierung, Skip Logic, Submit-Seite und „Was kommt als Nächstes"-Seite. Inkl. Render-Hinweisen für Google Form / Tally / Notion Form.

### `COMPANY_PROFILE_QUESTIONNAIRE.md`

35-Punkte-Unternehmensprofil-Fragebogen, 6 Sektionen (Profile / Systems / Risk / Deployment / Course / Budget). Output: JSON Profile Bundle, plus **Ableitungsregeln**: aus dem Bundle automatisch Deployment-Empfehlung, Kursverhältnis-Feintuning, PoC-Szenario-Empfehlung ableiten. Mit Reifegrad-Fragebogen über `submission_id` verknüpft.

### `AI_DIAGNOSIS_SHEETS_SCHEMA.md`

Implementierungs-Schema zur Automatisierung der gesamten Diagnose. Drei Plattformen: Google Sheets (Scoring-Formeln, bedingte Formatierung, Apps Script), Notion (4 Database-Strukturen und Formeln), n8n (13-Node Auto-Diagnose-Flow, inkl. Idempotency). Vom Fragebogen über Scoring bis Berichtgenerierung und Berater-Notifizierung alles automatisch.

### `*_EN.md`

Englische Sibling-Versionen obiger Dateien.

## 6. Mapping zu anderen Verzeichnissen

| Verzeichnis | Beziehung zu diesem Verzeichnis | Datenfluss |
| --- | --- | --- |
| `00_Overview` | Diagnose ist die erste Phase der Story | `00` Story → `01` Umsetzung |
| `02_Course_Design` | „L-Stufe + Kursverhältnis" der Diagnose bestimmt direkt die Kurskonfiguration | `01` Kursverhältnis → `02` Kurskonfiguration |
| `03_Consulting_Report` | Diagnoseergebnis ist Input für Stufe 1; Bericht zitiert Diagnose-Scores und Radar | `01` Scores → `03` Bericht |
| `04_Scenarios` | Nach Diagnose anhand L-Stufe aus `LLM_APPS_CASE_INDEX.md` PoC-Kandidaten wählen | `01` L-Stufe → `04` Case-Auswahl |
| `06_Delivery` | Diagnose entspricht der Sales-Phase des Engagement-Lifecycle | `01` ↔ `06` Sales-Phase |
| `90_References` | Methodische Grundlage des Scoring-Modells | `90` Grundlage → `01` |

## 7. Häufige Nutzungsszenarien

- **Sales-Entwicklung**: potentieller Kunde füllt 10-Punkte-Version → Auto-Bericht in 24 Std → Sales geht mit L-Stufe ins Gespräch.
- **Vor-Kurs-Vorbereitung**: 1 Woche vor Kursstart 25-Punkte-Version an Kunden-Manager → Berater bekommt Sechs-Dimensionen-Radar, justiert Kursverhältnis.
- **Vor-Berater-Interview**: IT/AI Champion füllt 50 Punkte + Profil-Fragebogen → Berater erhält 1 Std vor dem Interview komplettes Profile Bundle als Brief.
- **Skalieren**: mit `AI_DIAGNOSIS_SHEETS_SCHEMA.md` Auto-Diagnose-Flow im Kunden-n8n deployen, Berater interpretiert nur final.

---

## ⭐ Cross-Topic Quick References: 5 Kernthemen, wo zu finden

Die ganze Methodik hat 5 Hauptarterien durch alle Verzeichnisse. So bezieht sich dieses Verzeichnis auf jede:

| Cross-Topic | Hauptort | Wie dieses Verzeichnis anbindet |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + Drei-Engine-Co-Lesen** | Root [`README_DE.md`](../README_DE.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | Fragebogen kann interaktiv via Antigravity `/diagnose` ausgefüllt werden; AI_DIAGNOSIS_SHEETS_SCHEMA automatisiert den Fragebogen (n8n + Google Sheets + Notion); Diagnoseergebnis kann an Codex `/consistency-review` für dateiübergreifenden Abgleich fließen |
| 🎓 **Akademische Grundlage (7 Säulen)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **[`BARS_RUBRICS.md`](BARS_RUBRICS.md) in diesem Verzeichnis entspricht inter-rater reliability** (Smith & Kendall 1963); die sechs Diagnose-Dimensionen entsprechen Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Sociotechnical Trust |
| 📚 **L1-L5 Kursbildung** | [`../02_Course_Design/`](../02_Course_Design/) | **L-Stufen-Ermittlung + Sechs-Dimensionen-Radar + Kursverhältnis-Empfehlung** der Diagnose bestimmen direkt die Kurskonfiguration in `02` — sind „Pflichtfeld vor Kursstart" |
| 🔁 **Beratung / 8 Stufen + Phase A→B→C Closed-Loop** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Diagnose = Kerninput für Phase A** (Stufe 1 Ist-Erfassung + Stufe 2 Reference-Model-Radar-Unterschrift); die vierteljährliche Radar-Review in Phase C IST „**erneute Diagnose**" — ist die Struktur tatsächlich runder geworden? Diagnose ist Einstieg und gleichzeitig Falsifikationsmechanismus der Schleife |
| 📖 **References / Acknowledgments** | [`../90_References/`](../90_References/) §2 Acknowledgments | Scoring-Modell referenziert BARS (Smith & Kendall 1963) + 7 theoretische Säulen; Pilot Study 18-24-Monats-Empirie siehe [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) (validiert Fragebogen-Ziel Cohen's κ ≥ 0.60) |
