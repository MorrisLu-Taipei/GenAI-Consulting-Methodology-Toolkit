# 00 Overview — Programmübersicht & Einstiegspunkt

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Zweck dieses Verzeichnisses

Dieses Verzeichnis ist der **einzige Einstiegspunkt** des gesamten **AI Consulting Methodology Toolkits**. Es enthält keine „Werkzeuge" oder „Deliverables", sondern nur zwei Dinge: **die Geschichte der Methodik** und **den Status der Methodik**.

Jeder, der diesem Repo zum ersten Mal begegnet — Berater, die die Methodik lernen, Kunden, die eine Kaufentscheidung treffen, neue Kollegen im Onboarding, Reviewer, die prüfen — sollte hier beginnen. Bauen Sie hier zuerst das Gesamtverständnis auf („was ist die Methodik, warum ist sie so gestaltet, wo stehen wir") und gehen Sie dann in die Funktionsverzeichnisse `01`-`06`, damit Sie den Wald vor lauter Bäumen nicht aus dem Blick verlieren.

Das Problem, das dieses Verzeichnis löst: **Ohne einen klaren Einstieg und Status verlieren sich Nutzer, missbrauchen die Methodik und wissen nicht, was fertig ist und was noch in Arbeit ist.**

## 2. Position in der Methodik

| Achse | Mapping |
| --- | --- |
| Drei-Phasen-Service-Flow | Entspricht keinem einzelnen Schritt; eine **Vogelperspektive** auf „Diagnose → Build → Deliver" |
| Achtstufige Beratungsstruktur | Entspricht keiner einzelnen Stufe; eine **Übersicht** der acht Stufen |
| L1-L5-Reifegrad | Entspricht keiner einzelnen Stufe; eine **Übersicht** über L1-L5 |
| Engagement Lifecycle | Entspricht keiner einzelnen Phase; eine **Startpunkt-Erklärung** des gesamten Lebenszyklus |

> Logische Positionierung: `00_Overview` beantwortet „**was und warum**"; `01`-`06` beantwortet „**wie**"; `90_References` beantwortet „**Grundlage und Zitate**".

## 3. Ziele & Nutzen

| Ziel | Nutzen |
| --- | --- |
| Neuen Lesern in 5-10 Min das Methodik-Skelett vermitteln | Onboarding verkürzen; Fehlnutzung reduzieren |
| Wertversprechen in Kundensprache erzählen | Sales kann die Story direkt für 30-Min-Kundenintro nutzen |
| Eine maßgebliche Projektstatus-Datei pflegen | Jeder kann nachschauen „wo wir gerade stehen, was als Nächstes kommt" — keine mündliche Übergabe nötig |
| Beziehung zwischen `01`-`06` und `90` verbinden | Nutzer kennen Rolle und Reihenfolge jedes Verzeichnisses |

**Wenn dieses Verzeichnis übersprungen wird**: Nutzer springen direkt in die Funktionsverzeichnisse, ohne zu verstehen, „warum dieses Verzeichnis existiert oder wie es mit anderen verbunden ist", und Werkzeuge werden isoliert genutzt; die Methodik wird zu einem Haufen verstreuter Dateien.

## 4. Workflow & Logik

```text
Neue Leser / Kunden
   → AI_TRANSFORMATION_STORY_AND_STRUCTURE.md lesen (warum + wie + was wird produziert)
   → Mentales Gesamtmodell „L1-L5 + 8 Stufen + 3-Phasen-Flow" aufbauen
   → Weiter nach 01_Assessment für die eigentliche Diagnose

Berater / Kollegen / Reviewer
   → TODO_WBS.md lesen (Projektstand, Änderungslog, nächste Kandidaten, Arbeitslog)
   → Status verstehen, dann handeln
```

| Schritt | Wer | Wann | Input | Output |
| --- | --- | --- | --- | --- |
| Story lesen | Berater / Kunde / Neuling | Erster Repo-Kontakt | keiner | Gesamtverständnis der Methodik |
| Kunde briefen | Sales / Berater | Erstes Pre-Engagement-Meeting | Story | Kunde bereit für Diagnose |
| Projektstatus prüfen | Berater / Kollege / Reviewer | Vor Übernahme / Review | keiner | Aktuelles Bild + nächster Schritt |
| Status aktualisieren | Verantwortlicher Berater / AI | Nach jedem Batch | Fertige Arbeit | Aktualisierte `TODO_WBS.md` |

> Logik: Die Story ist „nach außen" (für Kunden + Neulinge); `TODO_WBS.md` ist „nach innen" (für Ausführende, um den Stand zu kennen). Außen + innen bilden den vollständigen Einstieg.

## 5. Dateibeschreibungen

### `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`

Kundenorientierte Story und Kapitelstruktur. Keine technische Dokumentation, sondern **Narrativ** — erzählt „warum Unternehmen KI-Transformation brauchen, wie die Methodik Schritt für Schritt funktioniert, was jeder Schritt akzeptierbar produziert" als eine zusammenhängende Geschichte, die der Kunde versteht. Enthält: Lösungspositionierung, 3-Phasen-Pfad, L1-L5 ↔ Werkzeug-Mapping, Zukunftsvorstellung, Wertversprechen je Rolle (CEO/COO/CIO/IT/HR/Abteilungsleiter), §6 vollständige 8-Stufen-Definition + 6-Wochen-Szenario. Direkt nutzbar in der ersten Kundenbesprechung.

### `EXECUTIVE_SUMMARY.md`

Die gesamte Methodik in 5 Minuten auf einer Seite. Für Führungskräfte ohne Zeit für Details.

### `CLIENT_JOURNEY_STORY.md` 🆕

**Mings Geschichte** — eine Szenario-Story, mit der CEO / Vorstand / Familie die Methodik in 20 Minuten verstehen. Eine Fertigung mit 700 Mitarbeitern in 24 Monaten Transformation — null Werkzeugtabellen, null Jargon. Nutzbar für externe Kommunikation, ersten Kundenkontakt, Einstellung neuer Mitarbeiter.

### `EIGHT_STAGE_FLOW_STORY.md` 🆕

**Maßgebliche 8-Stufen-Story**: 3-Phasen-Vertragsmodell (Phase A Diagnose 2W + Phase B Strategie 4W + Phase C Implementierung 24M) + Zwischenbericht + vierteljährliche Radar-Review als vollständige geschlossene Schleife. Pflichtlektüre für Berater-Internschulung.

### `METHODOLOGY_SCIENTIFIC_LOGIC.md` 🆕

**Wissenschaftliche Debattierfähigkeit der Methodik**: Validiert mit den 5 Kriterien wissenschaftlicher Methode (beobachtbar, quantifizierbar, wiederholbar, falsifizierbar, auditierbar), warum die 8 Stufen Kunden / Vorstand / Regulator-Hinterfragung standhalten. Pflicht für akademische Einreichung, Politik-Lobbying, Vorstands-Review.

### `INDUSTRY_FRAMEWORK_ALIGNMENT.md` 🆕

**Alignment-Karte mit Branchen-Frameworks**: 8 Stufen vs McKinsey / BCG / Bain / Deloitte / Accenture / PwC; 4-Schichten-Architektur vs TOGAF / Zachman / Dragon1; L1-L5 vs Gartner / MIT / Forrester AI Maturity. Antwort auf die Kundenfrage „Steht das im Konflikt zu unserer bestehenden Methodik?"

### `AI_NATIVE_LIVING_BOOK.md` 🆕

**Innovations-Diskussion zum Trägermedium der Methodik**: Positioniert diese Methodik als **AI-native living book** (ein Wissenssystem, das von AI-IDEs direkt ausgeführt werden kann), nicht nur PDF / PPT. Enthält akademische Einordnung (executable knowledge artifact, AI-mediated methodology, interactive consulting playbook), 3-Schichten-Design (Repo as Book / Agent as Tutor / Methodology as Executable Artifact), 4 Risikokontroll-Prinzipien (AI ≠ Berater, Evidence erforderlich, AGENTS.md versionskontrolliert, AI-Output ausgewiesen). Pflicht für akademische Einreichung / Methodik-Differenzierung.

### `ACADEMIC_THEORETICAL_FOUNDATIONS.md` 🆕

**Unified Statement der 7 theoretischen Säulen**: Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Task-Technology Fit (Goodhue & Thompson 1995) + Dynamic Capabilities (Teece 1997/2007) + Sociotechnical Systems & Trust in AI (Bostrom 1977/Dietvorst 2015/Glikson 2020) + Real Options (Dixit & Pindyck 1994/McGrath 1997) + Executable Knowledge Artifact (Knuth 1984). Pro Theorie: Summary + Begründer + Beitrag zu Tiger AI + Mapping-Position + Zitate. Die einzige Antwort, wenn Akademie / Regulator / Vorstand fragen „was ist die theoretische Basis".

### `../01_Assessment/BARS_RUBRICS.md` 🆕 (akademisch gehärtet)

**Behaviorally Anchored Rating Scales**: 6 Dimensionen × 0-4 Punkte **Verhaltensanker-Tabellen** (nach Smith & Kendall 1963). Jeder Score hat konkretes beobachtbares Verhalten, **vermeidet subjektive Beraterbewertung**, erhöht inter-rater reliability. Mit Pilot-Studie-Ziel Cohen's κ ≥ 0.60 abgestimmt. Der Kernmechanismus, mit dem zwei Berater zu nahezu identischen Scores für dieselbe Firma kommen.

### `TODO_WBS.md`

Die **maßgebliche Status-Datei** dieses Repos, die einzige glaubwürdige Quelle für „wo wir gerade stehen". Enthält: WBS-Überblick (Items × Priorität × Status), Liste fertiger Dateien, Detail fertiger Items, offene TODOs, Empfehlung für nächste Runde, **Änderungslog (pro Batch + Commit-Hash)**, aktueller Statusüberblick, **tägliches Arbeitslog**. Vor jeder Berater-Übernahme, Reviewer-Prüfung oder AI-Fortsetzung zuerst lesen. Nach jedem Batch wieder aktualisieren.

### `*_EN.md`

Englische Sibling-Versionen der obigen Dateien, inhaltsgleich mit den chinesischen Versionen.

## 6. Mapping zu anderen Verzeichnissen

| Verzeichnis | Beziehung zu diesem Verzeichnis | Datenfluss |
| --- | --- | --- |
| `01_Assessment` | Die „Diagnose"-Phase der Story wird hier umgesetzt | `00` Story → `01` Diagnose-Werkzeuge |
| `02_Course_Design` | Die „Build"-Phase der Story wird hier umgesetzt | `00` Story → `02` Kurse |
| `03_Consulting_Report` | Die „Deliver"-Phase der Story wird hier umgesetzt | `00` Story → `03` Beraterbericht |
| `04_Scenarios` | Liefert Kundenszenarien und Cases für die Story | `04` Cases ↔ `00` Story |
| `05_Sales` | Wandelt die Story in verkaufsfähiges Material | `00` Story → `05` Sales-Material |
| `06_Delivery` | Macht die Methodik zu liefer- und betreibbarem Geschäft | `00` Story → `06` Lieferung & Betrieb |
| `90_References` | Originalgrundlage der Methodik + Lizenzierung externer Zitate | `90` Grundlage → stützt `00`-`06` |

## 7. Häufige Nutzungsszenarien

- **Sales lädt Kunden ein**: nutzt den 3-Phasen-Pfad und das Wertversprechen aus `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md` für ein 30-Min-Methodik-Briefing.
- **Onboarding eines neuen Beraters**: zuerst Story lesen für Verständnis → dann `TODO_WBS.md` für aktuellen Stand → dann Verzeichnisse gemäß §6 Datenfluss nacheinander lernen.
- **Reviewer prüft**: liest Änderungslog und Arbeitslog in `TODO_WBS.md` direkt, vergleicht mit git log.
- **AI setzt Arbeit fort**: liest „nächste Kandidaten" und „Arbeitslog" in `TODO_WBS.md`, weiß, wo weitermachen.

---

## ⭐ Cross-Topic Quick References: 5 Kernthemen, wo zu finden

Die ganze Methodik hat 5 Hauptarterien durch alle Verzeichnisse. So bezieht sich dieses Verzeichnis auf jede:

| Cross-Topic | Hauptort | Wie dieses Verzeichnis anbindet |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + Drei-Engine-Co-Lesen** | Root [`README_DE.md`](../README_DE.md) §🌟 ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | **Dieses Verzeichnis IST der „Story-Einstiegspunkt" des AI-Native Living Books** — [`AI_NATIVE_LIVING_BOOK.md`](AI_NATIVE_LIVING_BOOK.md) ist die volle Diskussion; die 4 maßgeblichen Konzept-Dateien (CLIENT_JOURNEY / EIGHT_STAGE_FLOW / METHODOLOGY_SCIENTIFIC_LOGIC / INDUSTRY_FRAMEWORK_ALIGNMENT) liegen alle hier |
| 🎓 **Akademische Grundlage (7 Säulen)** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **Die Unified Discussion der 7 theoretischen Säulen liegt in diesem Verzeichnis**: Rosemann / Cohen & Levinthal / TTF / Teece / Sociotechnical Trust / Real Options / Knuth |
| 📚 **L1-L5 Kursbildung** | [`../02_Course_Design/`](../02_Course_Design/) | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 ist der maßgebliche Narrativ-Einstieg für **L1-L5 als zwei Achsen** (Skalen-Achse + AI-Autonomie-Achse) |
| 🔁 **Beratung / 8 Stufen + Phase A→B→C Closed-Loop** | [`EIGHT_STAGE_FLOW_STORY.md`](EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Die Beratungs-Closed-Loop-Story lebt in diesem Verzeichnis** — `EIGHT_STAGE_FLOW_STORY` §6 hat das vollständige Closed-Loop-Diagramm (Phase A 2W + Phase B 4W + Phase C 24M + vierteljährliche Radar-Review) |
| 📖 **References / Acknowledgments** | [`../90_References/`](../90_References/) §2 Acknowledgments | Die Stories in diesem Verzeichnis nutzen das gesamte Material von `90_References` als Grundlage (PDF / Diagramme / Video-Notizen / Theorie-Zitate) |
