# 02 Course Design — L1-L5 Kursgestaltung

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Zweck dieses Verzeichnisses

Dieses Verzeichnis ist die **zweite Phase: Build (Build)** des Drei-Phasen-Service-Flows. Die Diagnose (`01`) sagt Ihnen „auf welcher Stufe der Kunde ist und was fehlt"; dieses Verzeichnis enthält die **tatsächlichen Kurse, die die Lücke schließen**.

Das Problem, das es löst: **KI-Transformation gelingt nicht allein durch Werkzeugkauf oder Vorträge — das Unternehmen muss L1-L5 Stufe für Stufe durchlaufen und abnehmbare Assets produzieren.** Dieses Verzeichnis bietet für jede Stufe L1 bis L5 vollständige Curricula: Kursziele, Zielgruppe, Vorbedingungen, Inhalt, Lab-Aufgaben, Hausaufgaben, Abschlussstandards und Stage Gate. Jede Stufe produziert **abnehmbare Deliverables** (L1 Prompt Library, L2 Skill, L3 Workflow, L4 Agent, L5 Agent Team) — nicht „nach Vorlesung vergessen".

Wer nutzt: Dozenten, AI Champions, IT, Lernende aller Stufen.

## 2. Position in der Methodik

| Achse | Mapping |
| --- | --- |
| Drei-Phasen-Service-Flow | **Build** — zweite Phase |
| Achtstufige Beratungsstruktur | **Stufe 7 To-Be Design** (Kurse sind die tatsächliche Lösungs-Implementierung) |
| L1-L5-Reifegrad | Dieses Verzeichnis ist der Körper der Kurse, die „**den Kunden von seiner aktuellen Stufe zur nächsten heben**"; spannt L1-L5 **zwei Achsen** auf |
| Engagement Lifecycle | **Delivery — Build** |

> Kernprinzip 1: **L1-L5 verkettet — der Output der unteren Stufe ist der Input der nächsten.** Ohne L1-Vollnutzung gibt es keine Skills für L2; ohne L2-Skills sind L3-Workflows leere Rohre; ohne L3-Workflows hat L4-Agent kein Werkzeug; ohne L4-Agents hat L5-Team keine Mitglieder. **Kein Niveau-Sprung.**
>
> Kernprinzip 2: **L1-L5 sind zwei Achsen** — Skalen-Achse (L1 Individuum → L2 Abteilung → L3 abteilungsübergreifend / unternehmensweit, Mensch überwacht KI) und AI-Autonomie-Achse (L4 AI-Super-Assistent → L5 AI-Team, KI autonom, Mensch tritt zurück zu Governor). Kritische Grenze bei L3 → L4. Siehe [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0. Terminologie: **Stage Gate = Stufenabnahme-Tor**, **HITL = Human-in-the-Loop (Mensch im Review-Loop)**.

## 3. Ziele & Nutzen

| Ziel | Nutzen |
| --- | --- |
| Jede Stufe hat ein vollständiges, lieferbares Curriculum | Dozent kann direkt unterrichten, ohne Kursdesign neu zu machen |
| In-Class-Produktion liefert abnehmbare Assets | Kursergebnisse werden zur Organisationsfähigkeit, nicht „nach Vorlesung vergessen" |
| Jede Stufe hat Stage Gate | Kein Vorrücken ohne Bestehen, vermeidet gescheiterte Niveau-Sprünge |
| Kursverhältnis nach Diagnose-Scores konfiguriert | Kundenressourcen werden auf Lücken konzentriert, nicht verschwendet |
| L3/L4 mit PoC-Szenario-Bibliothek + n8n-Gerüste | Praktische Übungen haben fertige Aufgaben und Templates, kein Start bei null |

**Wenn dieses Verzeichnis übersprungen wird**: Kunde kauft Werkzeuge aber hat keine Fähigkeit, PoCs bleiben für immer Demos, KI skaliert nicht.

## 4. Workflow & Logik

```text
01_Assessment Diagnose → L-Stufe + Kursverhältnis-Empfehlung
   ↓
COURSE_REQUIREMENTS_AND_COMPANY_PROFILE (Vorbedingungen, Profil, Deployment-Modus prüfen)
   ↓
COURSE_MODULE_MATRIX (L1-L5-Outline und Verhältniskonfiguration ansehen)
   ↓
L1_L5_COMPLETE_COURSE_PLAN (Gesamtcurriculum) + tiefe Curricula je Stufe:
   L1 OPENWEBUI → L2 ANTIGRAVITY → L3 N8N → L4 HERMES → L5 CLAWTEAM
   ↓ pro Stufe
   Unterricht → Lab-Aufgaben (mit POC_SCENARIO_SPECS / N8N_WORKFLOW_TEMPLATES als Themen)
   → Abnehmbare Assets produzieren → Stage Gate passieren → erst dann zur nächsten Stufe
```

| Schritt | Wer | Wann | Input | Output |
| --- | --- | --- | --- | --- |
| Vorbedingungen prüfen | Berater + Kunden-IT | Vor Kursstart | Diagnoseergebnis, Profil | Vor-Kurs-Checkliste bestanden |
| Kursverhältnis konfigurieren | Berater | Vor Kursstart | L-Stufe + Verhältnisempfehlung | L1-L5-Stundenkonfiguration |
| Unterricht (stufenweise) | Dozent | Build-Phase | Tiefe Curricula | Schüler-Ergebnisse |
| Lab-Aufgaben | Lernende | In Class jeder Stufe | PoC-Szenario / n8n-Gerüst | Prompt/Skill/Workflow/Agent/Team |
| Stage-Gate-Abnahme | Berater + Kunden-Manager | Nach jeder Stufe | In-Class-Output | Gate bestanden → nächste Stufe |

> Logik: Kurse sind nicht „Werkzeugbedienung lehren" sondern „verifizierbare Organisationsfähigkeit entlang des Reifegrads aufbauen". Jede Stufe folgt der Struktur „obere Hälfte produzieren, untere Hälfte zur nächsten Stufe anbinden".

## 5. Dateibeschreibungen

### `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md`

L1-L5-Kursanforderungsliste und Unternehmensprofil-Erhebung. Definiert für jede Stufe Vorbedingungen, Stammdaten, Daten- und Risikoattribute, Systeminventar, Eignungskriterien und Kursnotizen für drei Deployment-Modi (Cloud KI / Hybrid / Vollständig On-Prem). Vor Kursstart genutzt, um zu bestätigen „ist der Kunde bereit?".

### `COURSE_MODULE_MATRIX.md`

L1-L5-Kursmodul-Matrix. Eine Tabelle zeigt für jede Stufe: Kursziele, Lab-Übungen, Hausaufgaben-Output, Kurspackaging (Halbtages-Erfahrung / Eintagesworkshop / Zweitages-Bootcamp / Beratungsprojekt) und Verhältnisempfehlungsregeln je Reifegrad.

### `L1_L5_COMPLETE_COURSE_PLAN.md`

L1-L5 komplette Kursplanung. Pro Stufe: Kursziele, Inhalt, Lab, Hausaufgaben, Abschlussstandard und Stage-Gate-Übersicht. Tiefe Curricula einzelner Stufen in den folgenden fünf Dateien.

### `L1_OPENWEBUI_COURSE_PLAN.md`

L1 Controlled AI Access Tief-Curriculum. Referenziert OpenWebUI öffentliche Playlist, enthält Per-Person-Login, persönlichen Chat-Workspace, Admin Panel, Konten/Rollen/Gruppen/Permissions, Modellsteuerung, Datennormen, Video-Referenzkarte.

### `L2_ANTIGRAVITY_COURSE_PLAN.md`

L2 Knowledge Codification Tief-Curriculum. Referenziert Google Antigravity drei Codelabs, enthält Agentic IDE, App Prototype, Unit Test, GCP Serverless Pipeline, Gate 2A-2E. **§7.6** enthält „bestehende Agent-Bibliothek (agency-agents) nutzen" Modul. Zweite Hälfte ist L2→L3 Bridge.

### `L3_N8N_TIGERAI_COURSE_PLAN.md`

L3 Workflow Automation Tief-Curriculum. **§1.1** teilt L3 in obere Hälfte (n8n-Konzept und manueller Aufbau) und untere Hälfte (AG + TigerAI-n8n-Skill-Pack Natural-Language-Generierung, **§5.5**). Referenziert TigerAI-Kanal n8n / OpenGenie Videos, enthält Gemini, multimodal, Sub-workflow, Data Tables, Webhook, GitHub Backup, Gate 3A-3G.

### `L4_HERMES_AGENT_COURSE_PLAN.md`

L4 Autonomous Agent Tief-Curriculum. **§2** sind „sieben Designprinzipien für Knowledge-Grade Agents" (Tag leicht / Nacht schwer, Knowledge-Compounding-Schleife, P1>P2, Schreib-Lese-gleiche-Quelle, Tool/LLM-Aufteilung, Failure-Mode-getriebenes Lernen, warum nicht nur RAG). Enthält Master + Spezial-Skill-Kombination, Wiki-Memory, ingest/query/update, Gate 4A-4E. **Dieser Kurs nimmt nur Konzepte, keinen internen Code.**

### `L5_CLAWTEAM_COURSE_PLAN.md`

L5 Multi-Agent Organization Tief-Curriculum. Auf Basis von HKUDS/ClawTeam (MIT) als Implementierungsplattform, enthält Team/Workspace/Task/Inbox/Transport Fünf-Schicht-Architektur, git worktree, CLI hands-on, drei lokalisierte Szenarien, Gate 5.

### `POC_SCENARIO_SPECS.md`

L3/L4-Kurs PoC-Szenario-Bibliothek. 7 Kategorien insgesamt 35 implementierbare PoCs (Gmail / Sheets / Notion / CRM / API / ERP + Buchhaltung), jeder mit trigger, Input, AI step, systems, Output, Abnahme, KPI, Personentag, n8n-Node-Sequenz. Lab-Aufgaben direkt von hier wählen.

### `N8N_WORKFLOW_TEMPLATES.md`

PoCs als importierbare n8n-Workflow-Gerüste (JSON). Enthält 30 PoC-Gerüste, Export/Import-Flow, Namensversionsspezifikation, GitHub Backup SOP, Kursnutzungs-Flow.

### `*_EN.md`

Englische Sibling-Versionen obiger Dateien.

## 6. Mapping zu anderen Verzeichnissen

| Verzeichnis | Beziehung zu diesem Verzeichnis | Datenfluss |
| --- | --- | --- |
| `01_Assessment` | L-Stufe + Kursverhältnis der Diagnose bestimmt Kurskonfiguration | `01` Verhältnis → `02` Konfiguration |
| `00_Overview` | Kurse sind die „Build"-Phase der Story | `00` Story → `02` Umsetzung |
| `03_Consulting_Report` | In-Class-Output und Beobachtungen fließen in den 8-Stufen-Beratungsbericht | `02` Output → `03` Bericht |
| `04_Scenarios` | Demo-Themen aus dem Case-Index; PoCs können zu Cases werden | `04` Cases ↔ `02` Kursthemen |
| `06_Delivery` | Kurse entsprechen Delivery — Build im Lebenszyklus; Deliverables fließen in Abnahme | `02` Output → `06` Abnahme |
| `90_References` | Drittanbieter-Zitate je Stufe (OpenWebUI / Antigravity / n8n-Skill-Pack / ClawTeam / agency-agents) | `90` Zitat → `02` |

## 7. Häufige Nutzungsszenarien

- **Kursverhältnis konfigurieren**: Diagnose-Verhältnis nehmen → mit `COURSE_MODULE_MATRIX.md` Stunden konfigurieren → entsprechendes Tief-Curriculum öffnen.
- **L3-Kurs durchführen**: erste Hälfte von `L3_N8N_TIGERAI_COURSE_PLAN.md` Konzept lehren, zweite Hälfte AG+Skill Pack; Lab-Aufgaben aus `POC_SCENARIO_SPECS.md`, Gerüste aus `N8N_WORKFLOW_TEMPLATES.md` importieren.
- **Lernende suchen Lab-Aufgaben**: nach Abteilung und L-Stufe aus `POC_SCENARIO_SPECS.md` oder `04_Scenarios/LLM_APPS_CASE_INDEX.md` wählen.
- **Abnahme**: nach jeder Stufe gegen `01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md` Stage Gate passieren.

---

## ⭐ Cross-Topic Quick References: 5 Kernthemen, wo zu finden

Die ganze Methodik hat 5 Hauptarterien durch alle Verzeichnisse. So bezieht sich dieses Verzeichnis auf jede:

| Cross-Topic | Hauptort | Wie dieses Verzeichnis anbindet |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + Drei-Engine-Co-Lesen** | Root [`README_DE.md`](../README_DE.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | **L2 Knowledge Codification lehrt die drei Engines direkt** — Antigravity / Codex / Claude Code sind die Werkzeuge der L2-Lernenden; in Class können die drei Engines für Demos, Skill-Encapsulation, Cross-File-Tests mobilisiert werden |
| 🎓 **Akademische Grundlage (7 Säulen)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **L1-L5 Fünf-Schicht-Architektur folgt Capability Maturity (Rosemann/CMMI)**; die Anti-Sprung-Regel folgt Absorptive Capacity (Cohen & Levinthal 1990); L4 Hermes sieben Designprinzipien folgen Sociotechnical & Knowledge Compounding |
| 📚 **L1-L5 Kursbildung** | [`../02_Course_Design/`](dieses Verzeichnis) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](L1_L5_COMPLETE_COURSE_PLAN.md) | **Dieses Verzeichnis IST der Körper der L1-L5-Kursbildung** — 5 eigenständige Tief-Curricula (L1 OPENWEBUI / L2 ANTIGRAVITY / L3 N8N / L4 HERMES / L5 CLAWTEAM) + COURSE_MODULE_MATRIX Verhältniskonfiguration + POC_SCENARIO_SPECS 35 Hands-on-Themen |
| 🔁 **Beratung / 8 Stufen + Phase A→B→C Closed-Loop** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **In-Class-Output fließt in den Phase-B-Bericht** (wird zum 14-Kapitel „Kursbeobachtungen"-Kapitel) + Phase C vierteljährliches Radar-Tracking; Stage Gate jeder Stufe entspricht Gate A/B/C des Closed-Loop |
| 📖 **References / Acknowledgments** | [`../90_References/`](../90_References/) §2 Acknowledgments | **L1 → OpenWebUI** ｜ **L2 → Antigravity / Codex / Claude Code + agency-agents** ｜ **L3 → n8n + TigerAI-n8n-Skill-Pack** ｜ **L4 → nousresearch/hermes-agent** ｜ **L5 → HKUDS/ClawTeam**. Volle Appreciation Cards in [`../90_References/README.md`](../90_References/README.md) §2.1-2.3 |
