# 06 Delivery — Lieferungsabnahme & Engagement-Operations

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Zweck dieses Verzeichnisses

Dieses Verzeichnis hat zwei Schichten, die zusammen eines lösen: **wie man Beratungseinsätze professionell und skalierbar zu einem „Geschäft" macht und „liefert".**

- **Lieferungsabnahme-Schicht**: definiert was dieses Programm an den Kunden liefert, wie abgenommen wird, welche Evidence Vollendung beweist.
- **Engagement-Operations-Schicht**: definiert den gesamten Engagement Lifecycle (Sales → Delivery → Support), Rollen-SOPs, Geschäftsdokumenten-Vorlagen, Operations-Checklisten, Pricing & Risk Management.

`01`-`03` sind „was der Berater tut" (Methodik); `05` ist „wie man den Kunden zum Kaufen bringt" (Pre-Sales); dieses Verzeichnis ist „**nach der Unterschrift, wie man das ganze Mandat als Geschäft komplett, sauber und wiederholbar durchführt**". Das Problem: **eine Beratungsfirma mit nur Methodik aber ohne Operations-Framework wird durch Scope Creep zermalmt, hat Handover-Brüche, Sicherheitsvorfälle, kann nicht skalieren.**

Wer nutzt: Projektmanager, Berater, Sales (Closer), Technical Lead, Client-Side Owner.

## 2. Position in der Methodik

| Achse | Mapping |
| --- | --- |
| Drei-Phasen-Service-Flow | **Deliver** + Operations-Rahmen, der alle drei Phasen in „Geschäft" verpackt |
| Achtstufige Beratungsstruktur | Entspricht der **Lieferung und Abnahme** der acht Stufen; Engagement Lifecycle ist die „kommerzielle Hülle" der acht Stufen |
| **3-Phasen-Vertragsmodell (Beratungs-Closed-Loop)** | **Phase A Diagnose 2W → Phase B Strategie 4W → Phase C Implementierung 24M + vierteljährliche Radar-Review** — die Delivery-Phase des Engagement Lifecycle IST die Phase-A→B→C-Schleife |
| L1-L5-Reifegrad | Lieferpaket-Abnahme deckt Deliverables aller L1-L5-Stufen ab |
| Engagement Lifecycle | **Dieses Verzeichnis IST der Körper des Engagement Lifecycle (Sales → Delivery → Support)** |

> 🔁 **Engagement Lifecycle ↔ Beratungs-Closed-Loop**: die „Delivery-Phase" dieses Verzeichnisses ist **kein 6-Wochen-Marathon**, sondern die in [`../03_Consulting_Report/README.md`](../03_Consulting_Report/README.md) §4 und [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 beschriebene **Schleife**: Phase A Zwischenbericht signiert → Gate A → Phase B vollständiger Bericht → Gate B → Phase C 24 Monate Implementierung + **vierteljährliche Radar-Review** (Falsifikationsmechanismus der wissenschaftlichen Verwaltung). Die Support-Phase entspricht Retainer / Maintenance nach Phase C.

## 3. Ziele & Nutzen

| Ziel | Nutzen |
| --- | --- |
| Klares Lieferpaket und Abnahmekriterien | Kunde und Berater sind sich einig „ist es fertig", kein Streit |
| Vollständiger Engagement Lifecycle | Von Lead bis Closeout hat SOP, nicht persönliche Handwerkskunst |
| Rollen-SOPs | Skalierbar (nicht eine Person macht alles), Handover ohne Bruch |
| Geschäftsdokumenten-Vorlagen | SOW/Vertrag/Rechnung/Change Order fertig, nicht jedes Mal neu |
| Operations-Checklisten | pre-project/security/QA/handover/offboarding nichts vergessen |
| Pricing- und Risk-Framework | Scope Creep frisst nicht die Marge auf, wissen wann „nein" sagen |

**Wenn dieses Verzeichnis übersprungen wird**: Methodik stark, aber Geschäft skaliert nicht — Scope Creep, umsonst gearbeitet, Handover-Bruch, Sicherheitsvorfall, Schlüsselperson-Abhängigkeit, uneinbringliche Forderungen.

## 4. Workflow & Logik

```text
Engagement Lifecycle (ENGAGEMENT_LIFECYCLE):
  Sales (Lead → Discovery → Proposal → Contract)
     → BUSINESS_DOCUMENT_TEMPLATES nutzen (Vorschlag, SOW)
     → PRICING_AND_RISK nutzen (Pricing, Risk Register)
  Delivery (Kickoff → Build → Test → Security → Handover)
     → DELIVERY_CHECKLISTS nutzen (pre-project / security / QA / handover)
     → DELIVERY_PACKAGE_AND_ACCEPTANCE nutzen (Lieferpaket-Abnahme)
     → DELIVERY_ROLE_SOPS nutzen (wer für welche Phase verantwortlich)
  Support (Retainer → Maintenance → Offboarding)
     → DELIVERY_CHECKLISTS nutzen (offboarding)
Durchgängig: 7 Pillars als Grundprinzip
```

| Schritt | Wer | Wann | Input | Output |
| --- | --- | --- | --- | --- |
| Lifecycle laufen | PM | Gesamtes Mandat | `ENGAGEMENT_LIFECYCLE` | Phasen-Vorrücken |
| Geschäftsdokumente erstellen | Closer / PM | Sales / bei Änderung | `BUSINESS_DOCUMENT_TEMPLATES` | Vorschlag / SOW / Change Order |
| Pricing und Risk | Closer / PM | Proposal / Kickoff | `PRICING_AND_RISK` | Angebot + Risk Register |
| Checklisten laufen | PM / Technical Lead | Jede Lieferphase | `DELIVERY_CHECKLISTS` | Jede Phase bestanden |
| Lieferungsabnahme | PM + Kunde | Handover | `DELIVERY_PACKAGE_AND_ACCEPTANCE` | Kundenunterschrift |
| Rollenverteilung | Gesamtes Team | Durchgängig | `DELIVERY_ROLE_SOPS` | Klare Verantwortung und Handover |

> Logik: `ENGAGEMENT_LIFECYCLE` ist der Hauptstrang (Lebenszyklus); die anderen 5 sind Werkzeuge für die Phasen — Dokumentenvorlagen, Pricing & Risk, Checklisten, Rollen-SOPs, Lieferungsabnahme. **7 Pillars** (Kunde besitzt, Kunde zahlt, Security first, gründlich testen, vollständige Dokumentation, sauberer Handover, klarer Scope) durchziehen alles.

## 5. Dateibeschreibungen

### Lieferungsabnahme-Schicht

| Datei | Zweck |
| --- | --- |
| `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` | Lieferpaket-Liste und item-by-item Abnahmetabelle für KI-Reifegrad-Diagnose, L1-L5-Kurse, L4 Hermes Agent, 8-stufiger Beraterbericht. |

### Engagement-Operations-Schicht (adaptiert von Mirza Iqbal / next8n.com Workflow Automation Delivery Framework, MIT, generalized für L1-L5 KI-Transformations-Kontext; Zitat siehe `../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`)

| Datei | Zweck |
| --- | --- |
| `ENGAGEMENT_LIFECYCLE.md` | 3-Phasen-Lebenszyklus (Sales → Delivery → Support), Sub-Phasen und Outputs jeder Phase, 7 Pillars, Lifecycle × 8 Stufen Cross-Reference, Pre-Engagement-Checkliste. |
| `DELIVERY_ROLE_SOPS.md` | 7 Lieferrollen-SOPs (Lead Gen / Sales Rep / Closer / PM / Technical Lead / Developer / Client), je Rolle: Verantwortung, Key-Deliverables, Handover-Punkte, Kollaborationspartner, zugehörige Lifecycle-Phase, plus Rolle × Lifecycle-Matrix und Handover-Golden-Rule. |
| `BUSINESS_DOCUMENT_TEMPLATES.md` | 8 Geschäftsdokumenten-Vorlagen: Vorschlag, SOW, MSA-Outline, Change Order, Rechnung, Handover-Dokument, Maintenance-Vertrag, kritische E-Mails. **Mit Haftungsausschluss — Vorlagen-Skelette sind keine Rechtsdokumente, müssen rechtlich geprüft werden.** |
| `DELIVERY_CHECKLISTS.md` | 5 Operations-Checklisten: pre-project, security, QA, handover, offboarding; Unterschied zu Methodik-Stage-Gate. |
| `PRICING_AND_RISK.md` | Zwei Trennprinzipien des Pricing, 4 Pricing-Modelle, gestufte Produktlinien, häufige Mandatsrisiken und Mitigation, wann „nein" sagen, Incident-Behandlungsprozess. |

### `*_EN.md`

Englische Sibling-Versionen einiger Dateien.

## 6. Mapping zu anderen Verzeichnissen

| Verzeichnis | Beziehung zu diesem Verzeichnis | Datenfluss |
| --- | --- | --- |
| `01_Assessment` | Diagnose entspricht der Sales-Phase des Lifecycles | `01` ↔ `06` Sales |
| `02_Course_Design` | In-Class-Outputs gehen in Lieferpaket-Abnahme | `02` Output → `06` Abnahme |
| `03_Consulting_Report` | Beraterbericht ist Kernlieferung des Lieferpakets | `03` Bericht → `06` Abnahme |
| `05_Sales` | Deck-Preise/Pakete entsprechen Lifecycle und Pricing | `05` Deck ↔ `06` Pricing |
| `00_Overview` | Engagement Lifecycle ist der Rahmen, der die Story in Geschäft verwandelt | `00` Story → `06` Operations |
| `90_References` | Drittanbieter-Zitat für Operations-Schicht (Mirza Iqbal Framework) | `90` Zitat → `06` |

## 7. Häufige Nutzungsszenarien

- **Neues Mandat angenommen**: PM nutzt „Pre-Engagement-Checkliste" in `ENGAGEMENT_LIFECYCLE.md` für Bereitschaftsprüfung, `DELIVERY_ROLE_SOPS.md` für Rollenzuweisung.
- **Vor Unterschrift**: Closer nutzt SOW-Vorlage in `BUSINESS_DOCUMENT_TEMPLATES.md` (in/out of scope klar geschrieben), `PRICING_AND_RISK.md` für Pricing.
- **Jede Lieferphase**: Gegen `DELIVERY_CHECKLISTS.md` pre-project / security / QA / handover Checklisten laufen.
- **Lieferung an Kunden**: `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` für item-by-item Abnahme + Handover-Dokument in `BUSINESS_DOCUMENT_TEMPLATES.md`.
- **Kunde fügt ständig Anforderungen hinzu**: Scope-Creep-Mitigation in `PRICING_AND_RISK.md` + Change Order in `BUSINESS_DOCUMENT_TEMPLATES.md`.
- **Closeout**: Offboarding-Checkliste in `DELIVERY_CHECKLISTS.md` laufen.

---

## ⭐ Cross-Topic Quick References: 5 Kernthemen, wo zu finden

Die ganze Methodik hat 5 Hauptarterien durch alle Verzeichnisse. So bezieht sich dieses Verzeichnis auf jede:

| Cross-Topic | Hauptort | Wie dieses Verzeichnis anbindet |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + Drei-Engine-Co-Lesen** | Root [`README_DE.md`](../README_DE.md) §🌟 ｜ [`AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | Während des Mandats können die drei Engines verteilt eingesetzt werden: Antigravity für Kundenmeetings / Codex für SOW- und Berichtsentwurfs-Audit / Claude Code für Phase-B-Simulation und Mehrperspektiven-Review |
| 🎓 **Akademische Grundlage (7 Säulen)** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | „Security first / HITL" der 7 Pillars entspricht Sociotechnical Systems & Trust (Bostrom / Dietvorst / Glikson); Scope Creep / Niveau-Sprung-Versagen entspricht Real Options + Absorptive Capacity Failure Patterns |
| 📚 **L1-L5 Kursbildung** | [`../02_Course_Design/`](../02_Course_Design/) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md) | Lieferpaket-Abnahme deckt verifizierbare Deliverables aller L1-L5-Stufen ab; In-Class-Outputs gehen in [`DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](DELIVERY_PACKAGE_AND_ACCEPTANCE.md) für item-by-item Abnahme |
| 🔁 **Beratung / 8 Stufen + Phase A→B→C Closed-Loop** | [`EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **Dieses Verzeichnis IST die „kommerzielle Hülle" des Beratungs-Closed-Loop** — Engagement Lifecycle Sales→Delivery→Support entspricht Phase A→B→C + vierteljährliches Radar-Review |
| 📖 **References / Acknowledgments** | [`../90_References/`](../90_References/) §2 Acknowledgments | Operations-Schicht zitiert Mirza Iqbal / next8n.com Workflow Delivery Framework (MIT), Details in [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) |
