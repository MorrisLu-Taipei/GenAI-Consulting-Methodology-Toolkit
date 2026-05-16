# 03 Consulting Report — Beratungsdiagnose & Bericht (Beratungs-Closed-Loop)

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Zweck dieses Verzeichnisses

Dieses Verzeichnis ist die **dritte Phase des Drei-Phasen-Service-Flows: Deliver**, und auch der **Kern der Beratungspraxis** der gesamten Methodik.

Diagnose (`01`) liefert objektive Scores, Build (`02`) lässt die Kundenfähigkeit wachsen — aber was ein Beratungseinsatz letztlich an den Kunden übergibt, ist ein **Diagnosebericht, der strukturiert, evidenzbasiert, mit Roadmap und vom Entscheidungsträger annehmbar ist**. Dieses Verzeichnis bietet alles, was zur Erstellung dieses Berichts nötig ist: **Werkzeugtabellen der achtstufigen Beratungsstruktur, klassische Beratungsframework-Bibliothek, Berichtserzeugungs-Workflow und Berichtsvorlage**.

> 🔁 **Dieses Verzeichnis ist KEIN „6-Wochen-Linear-Marathon", sondern der „Beratungs-Closed-Loop"**. Volles Closed-Loop-Design siehe [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md):
> **3-Phasen-Vertrag** (Phase A Diagnose 2W + Phase B Strategie 4W + Phase C Implementierung 24M) + **Zwischen-Diagnose-Bericht** + **vierteljährliche Radar-Review** (Falsifikationsmechanismus der wissenschaftlichen Verwaltung).
> Der Punkt des Loops ist nicht „fertig wenn geliefert" — sondern „**ist die Struktur tatsächlich runder geworden?**" — kontinuierliche Selbst-Falsifikation gegen das Stage-2-Reference-Model-Radar.

Das Problem, das es löst: **Ohne Methodik ist die Beraterdiagnose persönliche Handwerkskunst auf Erfahrungsbasis — nicht skalierbar, nicht von neuen Beratern reproduzierbar, instabile Qualität.** Dieses Verzeichnis verwandelt „wie ein Berater diagnostiziert" in einen Standard-Closed-Loop, der lehrbar, replizierbar und abnehmbar ist.

Wer nutzt: Berater, Senior-Berater, neue Berater (Onboarding), Projektmanager.

## 2. Position in der Methodik

| Achse | Mapping |
| --- | --- |
| Drei-Phasen-Service-Flow | **Deliver** — dritte Phase |
| Achtstufige Beratungsstruktur | **Dieses Verzeichnis IST die Werkzeuge und der Berichtskörper der acht Stufen (Stage 1-8)** |
| **3-Phasen-Vertragsmodell** | **Phase A Diagnose 2W → Phase B Strategie 4W → Phase C Implementierung 24M + vierteljährliche Radar-Review** (Beratungs-Closed-Loop) |
| L1-L5-Reifegrad | Der Bericht zitiert L-Stufe und Kursbeobachtungen des Kunden |
| Engagement Lifecycle | **Delivery — Handover** (Bericht ist Kernlieferung von Phase B; Phase C produziert kontinuierlich vierteljährliche Radar-Review-Records) |

> Zwei orthogonale Achsen: **L1-L5 ist die „Fähigkeits-Vertikale" (`02` zuständig); die acht Stufen sind die „Diagnose-Horizontale" (dieses Verzeichnis zuständig).** Die zwei Achsen kreuzen sich für verifizierbare Lieferung.
>
> **L1-L5 ist selbst zwei Achsen** (Skalen-Achse L1-L3 + AI-Autonomie-Achse L4-L5); siehe [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0.

## 3. Ziele & Nutzen

| Ziel | Nutzen |
| --- | --- |
| Jeder Schritt der acht Stufen hat direkt nutzbare Werkzeugtabellen | Berater muss Werkzeugdesign nicht neu machen; neue Berater schnell einsatzbereit |
| Klassische Framework-Bibliothek auf acht Stufen gemappt | Jeder Schritt weiß „welches Analyse-Framework nutzen" |
| Berichtserzeugungs-Workflow | „Problem → lieferbarer Bericht/Deck" hat SOP, nicht Handwerk |
| Festgelegte Berichtsstruktur | Stabile Lieferqualität; Entscheidungsträger versteht es |
| Beratungsmethodik lehr- und replizierbar | Beraterteam skaliert |

**Wenn dieses Verzeichnis übersprungen wird**: Jeder Berater diagnostiziert auf eigene Weise, Berichtsqualität inkonsistent, neue Berater können nicht replizieren, Diagnose degradiert zur „persönlichen Handwerkskunst des Senior-Beraters".

## 4. Workflow & Logik (3-Phasen-Vertrag + vierteljährlicher Closed-Loop)

```text
01 Diagnoseergebnis + 02 Kursbeobachtungen
   ↓
┌─ Phase A Diagnose (2 Wochen) ──────────────────────────┐
│  Stage 1-4 erste Hälfte der acht Stufen: Awareness /   │
│  Reference Model / Discovery / Gap Analysis            │
│  → CONSULTING_TOOLKIT_TEMPLATES.md Werkzeuge nutzen    │
│  → Zwischen-Diagnose-Bericht → vom Kunden signiert     │
└────────────────────────────────────────────────────────┘
   ↓ Gate A — Kunde entscheidet über Phase-B-Verlängerung
┌─ Phase B Strategie (4 Wochen) ─────────────────────────┐
│  Stage 5-8 zweite Hälfte: Stakeholder / Diagnosis /    │
│  To-Be Design / Acceptance Test                        │
│  → REPORT_PRODUCTION_WORKFLOW.md 8-Schritt-Produktion  │
│  → Voller 14-Kapitel-Bericht + 24M Roadmap + ROI +    │
│     Governance-Empfehlungen                            │
│  → In CONSULTING_REPORT_TEMPLATE.md-Struktur einfüllen │
└────────────────────────────────────────────────────────┘
   ↓ Gate B — Kunde unterzeichnet Phase-C-SOW
┌─ Phase C Implementierung (24 Monate) ─ Loop-Feedback ──┐
│  Phasenweise Umsetzung + **Vierteljähr. Gate C:        │
│  Stage-2-Radar erneut prüfen**                          │
│  → Ist die Struktur tatsächlich runder? Wenn nicht →   │
│     zurück zur entsprechenden Stage, Roadmap anpassen  │
│  → Vierteljährliche Outputs: Radar-Review-Records +   │
│     Roadmap-Korrektur-Notizen                          │
└────────────────────────────────────────────────────────┘
```

| Phase | Dauer | Stufen | Hauptwerkzeuge | Hauptlieferungen |
| --- | --- | --- | --- | --- |
| **Phase A Diagnose** | 2 Wochen | Stage 1-4 | TOOLKIT erste Hälfte + FRAMEWORKS-Selector | **Zwischen-Diagnose-Bericht** + signiertes Reference-Model-Radar |
| **Phase B Strategie** | 4 Wochen | Stage 5-8 | TOOLKIT zweite Hälfte + REPORT_PRODUCTION_WORKFLOW + REPORT_TEMPLATE | **Voller 14-Kapitel-Bericht** + Roadmap + ROI + Governance |
| **Phase C Implementierung** | 24 Monate | Vierteljährliche Stage-2-Review | TOOLKIT vierteljährliches Radar-Review-Tool + Risk Register | **Vierteljährliche Radar-Review-Records** + Roadmap-Korrekturen |

> Logik: `CONSULTING_TOOLKIT_TEMPLATES` ist „die Werkzeuge zum Diagnostizieren + das vierteljährliche Review-Tool"; `CONSULTING_FRAMEWORKS_LIBRARY` ist „welches Analyse-Framework an jedem Schritt"; `REPORT_PRODUCTION_WORKFLOW` ist „wie die Diagnose effizient in Lieferung verwandeln"; `CONSULTING_REPORT_TEMPLATE` ist „wie der finale Bericht aussieht". Zusammen = **vollständige Beratungs-Closed-Loop-Methodik** (kein linearer Marathon).

> 📖 Volles 8-Stufen-Dialog-Skript + Closed-Loop-Story: [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) (inkl. „Warum der Closed-Loop Wissenschaft ist"-Schluss).

## 5. Dateibeschreibungen

### `CONSULTING_REPORT_TEMPLATE.md`

Markdown-Vorlage für den KI-Transformations-Diagnosebericht (v2.0 acht-stufen-aligned). 14-Kapitel-Festsstruktur: Cover, Executive Summary (inkl. Standard-Lücken-Übersicht), Diagnose-Methode, As-Is Snapshot, Reference Model Alignment (APQC + Tiger AI Doppelkoordinate), Best Practice Integration (Excellence-Profil), Gap Analysis, Executive Problem Statement, Phased Goals, To-Be Design, Implementation Roadmap, Change Management Plan, Governance Design, Value Tracking & Risk Register, SOW-Empfehlungen.

### `CONSULTING_TOOLKIT_TEMPLATES.md`

**Direkt nutzbare Werkzeugtabellen** der achtstufigen Beratungsdiagnose (v2.0 image-aligned). Jede Stufe mappt zu 1-5 Werkzeugen: 40-Frage-Interview-Bank, AI/System-Inventar, As-Is-Swimlane, **Reference-Model-Auswahl (APQC/SCOR/eTOM/ITIL/CMMI) + Mapping Worksheet + Standard-Lücken-Check + Doppel-Radar**, Best-Practice-Profile + Excellence-Profil, Missing/Broken/Redundant (**keine Risikobewertung**), Impact×Effort, **80/20-Konvergenz + 5 Whys**, Problem Statement, **Ultimate Benchmark → Phased Goals + Organisations-Absorptionsbewertung**, **Phased To-Be Operating Model + Human-AI Collaboration (HITL)**, Skill/Workflow/Agent Map, Transformation Roadmap, **Change Management Playbook (inkl. Widerstandsbehandlung)**, RACI, Permissions, **Value Tracking Matrix (Zeit/Qualität/Skala/Risiko/Assets 5 Dimensionen)**, Risk Register, Audit, Ethics, **Phase A 2W + Phase B 4W Standardplan + Phase C vierteljährliches Radar-Review-Tool** (Beratungs-Closed-Loop). Copy-paste-fertig.

### `CONSULTING_FRAMEWORKS_LIBRARY.md`

Klassische Beratungsframework-Bibliothek. 50+ Industrie-Frameworks (MECE, Pyramid Principle, Issue Tree, Porter's 5 Forces, SWOT, BCG Matrix, 5 Whys, Fishbone, Business Model Canvas, WBS/RACI, NPV/IRR, Lean/Six Sigma usw.) in 7 Kategorien. Inkl. „Framework-Selector" (natural language → Framework-Kombination), „Framework-Kombi-Ketten", jedes Framework auf acht Stufen gemappt, und §4.8 Tiefe für MECE / Issue Tree / Hypothesenbildung. Adaptiert von yoichiojima-2/consultant (MIT).

### `REPORT_PRODUCTION_WORKFLOW.md`

8-Schritt-Produktions-Workflow für „Problem → lieferbarer Bericht/Deck". Inkl. Dummy Page (Skelett zuerst, dann füllen), Abhängigkeitsmanagement, 7 Seitenlayouts, Excel-Evidence-Spur, Progressive Disclosure, §9 Troubleshooting Playbook (7 häufige Probleme + Fixes). Adaptiert von Kafurtan/mckinsey-consultant-skills (MIT).

### `*_EN.md`

Englische Sibling-Versionen obiger Dateien.

## 6. Mapping zu anderen Verzeichnissen

| Verzeichnis | Beziehung zu diesem Verzeichnis | Datenfluss |
| --- | --- | --- |
| `01_Assessment` | Diagnose-Scores und Radar sind Kerninput für Stage 1 | `01` Scores → `03` Bericht |
| `02_Course_Design` | In-Class-Output und Beobachtungen sind Material für „Kursbeobachtungen"-Kapitel | `02` Kursbeobachtungen → `03` Bericht |
| `00_Overview` | Bericht ist „Deliver"-Phase der Story | `00` Story → `03` Umsetzung |
| `04_Scenarios` | Stage 3 Industrie-Best-Practice-Benchmarking zitiert Cases | `04` Cases → `03` Stage 3 |
| `06_Delivery` | Bericht ist Kernlieferung des Delivery-Pakets; mappt zu Handover | `03` Bericht → `06` Lieferungs-Abnahme |
| `90_References` | Drittanbieter-Zitate für Framework-Bibliothek und Bericht-Workflow (consultant / mckinsey-skills) | `90` Zitat → `03` |

## 7. Häufige Nutzungsszenarien (nach Closed-Loop-Phase)

- **Neuer Berater Onboarding**: zuerst `CONSULTING_TOOLKIT_TEMPLATES.md` lesen und alle Samples einmal durchgehen, dann [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) Dialog-Skript lesen, zuletzt ein echtes Interview shadowen.
- **Phase A Diagnose (2 Wochen)**: TOOLKIT Stage 1-4 Werkzeuge nutzen (40-Frage-Interview, AI/System-Inventar, Reference-Model-Radar), am Wochenende **Zwischen-Diagnose-Bericht** für Sponsor-Signatur produzieren.
- **Phase B Strategie (4 Wochen)**: TOOLKIT Stage 5-8 Werkzeuge + `REPORT_PRODUCTION_WORKFLOW.md` 8-Schritt-Produktion, Diagnose in Deck verwandeln, in `CONSULTING_REPORT_TEMPLATE.md` einfüllen, **vollen 14-Kapitel-Bericht + 24M Roadmap + ROI** produzieren.
- **Phase C Implementierung (24 Monate, Loop-Feedback-Phase)**: vierteljährlich mit TOOLKIT-Radar-Review-Tool, **Stage-2-Reference-Model-Radar erneut laufen lassen** — gegen Phase-A-signierte Version vergleichen, sehen ob „die Struktur tatsächlich runder geworden ist"; wenn nicht → zurück zur entsprechenden Stage, Roadmap anpassen.
- **Kunde fragt „warum dieses Framework"**: Framework-Selector in `CONSULTING_FRAMEWORKS_LIBRARY.md` nutzen zur Erklärung.
- **Kunde fragt „was passiert nach den 6 Wochen?"**: [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 vollständiges Closed-Loop-Diagramm zeigen — der Punkt sind nicht die 6 Wochen, sondern Phase C 24 Monate + vierteljährliches Radar-Review als Falsifikationsmechanismus.
