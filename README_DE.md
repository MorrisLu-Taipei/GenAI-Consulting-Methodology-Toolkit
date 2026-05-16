# GenAI Consulting Methodology Toolkit

Sprache: [繁體中文](README.md) | [English](README_EN.md) | [ภาษาไทย](README_TH.md) | Deutsch | [Français](README_FR.md) | [Español](README_ES.md) | [日本語](README_JA.md) | [한국어](README_KR.md)

Toolkit für die Reifegradbewertung und Implementierungsmethodik der KI-Transformation in Unternehmen (Enterprise AI Transformation Maturity Assessment & Implementation Methodology Toolkit).

Originalautor: **Tiger AI Morris Lu 盧業興**  
Rolle: **n8n Taipei Ambassador / Doktorand am Institut für Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australien**

Lizenzhinweis: Dieses Projekt steht unter der **[Apache License 2.0](LICENSE)**. Es darf frei genutzt, kopiert, modifiziert, weiterverteilt und kommerziell verwendet werden. Bei Weiterverteilung sind der Apache-2.0-Lizenztext und die Urhebernennung in [`NOTICE`](NOTICE) beizubehalten.

> **Nur 5 Minuten Zeit?** Beginnen Sie mit [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) — die gesamte Methodik auf einer Seite.

---

## 🌟 Dies ist nicht nur ein Buch, es ist ein AI-Native Living Book — ein wirklich „lebendiges" Buch

Bücher haben sich Generation für Generation weiterentwickelt. Jede Generation hat ein Problem gelöst, aber eine Lücke hinterlassen — **keines war jemals wirklich „lebendig"**:

- **Generation 1 — Gedruckte Bücher**: bewahren Wissen und geben es an die nächste Leserin weiter. Doch sie **können nur gelesen werden, sie antworten nicht**, können Ihre Fragen nicht beantworten und wissen nicht, wie Ihr Unternehmen aussieht — sie sind **stilles Papier**.
- **Generation 2 — Interaktive Bücher**: nach dem Umzug ins Web und in Wikis kann man sie durchsuchen, verlinken und kommentieren. Sie bieten gegenüber gedruckten Büchern **„Interaktion"**, aber sie **schlagen Ihnen nichts proaktiv vor** und analysieren erst recht nichts für Sie — sie bleiben passiv: die Oberfläche lebt, der Inhalt nicht.
- **Generation 3 — AI-Native Books (dieses Repo) — ein wirklich „lebendiges" Buch**: die Methodik ist in Markdown geschrieben und wird mit einer AI-IDE geöffnet — die KI liest das gesamte Buch automatisch, **lässt Sie fragen, antwortet für Sie, denkt mit Ihnen** und **gibt maßgeschneiderte Empfehlungen für die tatsächliche Situation Ihres Unternehmens, führt Diagnosen durch, erstellt Berichtsentwürfe, simuliert Szenarien**. Das Buch selbst reagiert, erweitert sich und lässt neue Kapitel mit Ihren Fragen wachsen.

Mit anderen Worten: gedruckte Bücher übertragen Wissen, interaktive Bücher machen es durchsuchbar, **AI-Native Books lassen „das Buch" zum ersten Mal wirklich lebendig werden — es wird zu einem Partner, der mit Ihnen denkt**. Die endgültige Entscheidung trifft weiterhin der Mensch, aber Sie stehen einer statischen Methodik nicht mehr allein gegenüber.

> *Three generations of books: printed (read-only, dead) → interactive (search & link, still passive) → **AI-native (truly alive — advises, analyzes, simulates, and grows with your questions)**. Open with an AI IDE; AI becomes your reading partner, consulting assistant, and auditor.*

### 🔱 Drei AI-Engines mit unterschiedlichen Spezialisierungen

Derselbe Inhalt zeigt **völlig unterschiedliche Persönlichkeiten**, je nachdem, welche AI-IDE Sie wählen:

| Engine | Rolle | Worin sie am besten ist |
| --- | --- | --- |
| 🟦 **Antigravity** | Frontlinien-Berater | Mit Kunden sprechen, Fragebögen durchführen, Berichtsentwürfe erstellen |
| 🟪 **Codex CLI** | Methodik-Auditor | Dateiübergreifende Tests, Red-Team-Übungen, Versionskontrolle, defekte Links reparieren |
| 🟨 **Claude Code** | Dateiübergreifender Denkpartner | Tiefensynthese, Debatten aus mehreren Perspektiven, Simulationen, kundenspezifische Forks |

Die drei Engines ersetzen einander nicht, sondern **teilen sich die Arbeit**: morgens mit Antigravity Kundentermine, nachmittags mit Codex Berichtsentwürfe auditieren, abends mit Claude Code Szenarien simulieren. Jeder Arbeitsbereich ist eigenständig (`.agent/` / `.codex/` / `.claude/`) und stört die anderen nicht.

Detaillierte Selbstbeschreibungen jedes Engines siehe [`07_AI_Contributions/`](07_AI_Contributions/); Installationsschritte siehe [Installations- und Startanleitung der drei AI-Engines](#-installations--und-startanleitung-der-drei-ai-engines--three-ai-engines-setup-guide) weiter unten.

### Was das für verschiedene Leserrollen bedeutet

- **CEO / Top-Management**: werfen Sie dieses Repo in ChatGPT / Claude / Gemini, und 10 Minuten Frage-Antwort liefern eine erste Einschätzung „Auf welcher Stufe steht mein Unternehmen? Was sollte ich zuerst tun?"
- **Berater / Lernende**: mit einer AI-IDE öffnen und das vollständige konversationelle Beratungserlebnis durchlaufen — von der Diagnose über den Bericht bis zur 24-monatigen Implementierungs-Roadmap.
- **Forscher / Wissenschaftler**: führen Sie direkt `/devil-pair-debate` und `/thought-experiment` aus, um die Wertannahmen der Methodik zu debattieren, gestützt auf 7 theoretische Säulen und 28 zitierbare Klassiker.
- **Regulierung / Compliance**: `/evidence-audit` und `/generate-traceability` für eine auditierbare Beweiskette, abgeglichen mit NIST AI RMF / EU AI Act / ISO 42001.

> ⚠️ **Ehrliche Offenlegung**: Die Gesamtarchitektur der Methodik wurde von **Morris Lu (Mensch)** entworfen; die drei AI-Engines sind lediglich Werkzeuge zur Ausführung, Vervollständigung und Prüfung. Details siehe [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0. Alle Fallstudien im Buch sind KI-generierte Lehrbeispiele — **keine echten Kundendaten**.

---

## Welches Problem löst diese Methodik

Viele Unternehmen springen bei der KI-Einführung direkt zu den Werkzeugen: heute ChatGPT kaufen, morgen n8n testen, nächste Woche einen Agent bauen. Typische Probleme: Mitarbeiter wissen nicht, wie sie es nutzen sollen, Prozesse sind nicht verbunden, Daten nicht governanced, PoCs werden nicht abgenommen, und am Ende weiß die Führung nicht, auf welcher Reifestufe die Unternehmens-KI tatsächlich steht.

Die Strategie dieses Toolkits: zuerst mit einem einfachen Fragebogen den aktuellen KI-Reifegrad des Unternehmens diagnostizieren, dann gemäß L1-L5 das Kursverhältnis und den Adoptionspfad gestalten. Kurse enden nicht einfach nach der Teilnahme — auf jeder Stufe entstehen verifizierbare Deliverables. Schließlich wird ein achtstufiger Beratungsprozess für die KI-Transformation eingesetzt, um einen vollständigen Diagnosebericht, eine Roadmap, ROI-Sicht und Governance-Empfehlungen zu erstellen.

## Zukunftsvorstellung vor Kursbeginn

Bevor Kunden über die L1-L5-Kurse entscheiden, müssen sie zuerst ein Zukunftsbild sehen: nicht „wir lernen fünf Werkzeuge", sondern „**wie wird sich der Arbeitsalltag nach dem Kurs verändern?**"

Die Handlung: **Der Maßstab erweitert sich Schicht für Schicht, und schließlich wächst aus „Menschen nutzen KI" das „KI arbeitet selbst"**: **Individuum → Abteilung → abteilungsübergreifend/unternehmensweit → AI-Super-Assistent (Einheit) → AI-Team**. Stellen Sie sich einen Montagmorgen in drei Monaten vor:

- **L1 Controlled AI Access ─ Skalen-Achse · Individuum**: **Jeder Mitarbeiter einzeln** loggt sich mit seinem eigenen Konto in OpenWebUI ein, hat seinen eigenen Chatbereich, seine Historie und Abteilungsberechtigungen. Vertrieb schreibt Kunden-E-Mails, HR fasst Schulungen zusammen, Führungskräfte erstellen Meeting-Highlights — alles startet vom selben kontrollierten KI-Eingangspunkt. **Die Einheit ist „das Individuum"**, KI steht neben jeder Person.
- **L2 Knowledge Codification ─ Skalen-Achse · Abteilung**: **Die Einheit steigt zur „Abteilung" auf**. Erfahrene Mitarbeiter sind nicht mehr nur individuell gut, sondern verpacken — **innerhalb der Abteilungsverantwortung** — Texte, Berichte, Kundenservice-Antworten, SOP-Auswertungen und Entwicklungsmethoden in wiederverwendbare Skills. Neueinsteiger und andere in der Abteilung nutzen dieselbe Methodik; die Output-Qualität **der gesamten Abteilung** wird konsistent.
- **L3 Workflow Automation ─ Skalen-Achse · abteilungsübergreifend / unternehmensweit**: **Die Einheit steigt erneut auf „abteilungsübergreifend, unternehmensweit"**. n8n verbindet die Skills jeder Abteilung mit Systemen (Gmail, Sheets, Notion, CRM, API, ERP). Eine eingehende Kundenbeschwerde **durchläuft mehrere Abteilungen — Vertrieb, Kundenservice, CRM, Management** automatisch — das System fragt das CRM ab, aktualisiert Formulare, erstellt Aufgaben, generiert Management-Zusammenfassungen, der Mensch entscheidet und genehmigt nur. KI betritt nun die **unternehmensweiten Prozesse**.
- **L4 Autonomous Agent ─ AI-Autonomie-Achse · Super-Assistent (AI-Einheit)**: **Über die „menschliche Mannschaft" hinaus wächst eine zusätzliche AI-Einheit**. Hermes Agent liest täglich Aufgaben, Dokumente, Workflow-Ergebnisse und Wiki-Speicher, erzeugt Briefings, Verfolgungslisten und Entscheidungspunkte, die HITL (Human-in-the-Loop, Mensch im Überprüfungsschleifen) benötigen. Das Unternehmen verfügt nun über eine **verifizierbare wissensbasierte AI-Einheit**, wie ein zusätzlich eingestellter vollautomatischer Super-Assistent.
- **L5 Multi-Agent Organization ─ AI-Autonomie-Achse · AI-Team**: **Mehrere L4-Einheiten werden zu einem „AI-Team" zusammengestellt**. ClawTeam organisiert spezialisierte Agents — Markt, Produkt, Kundenservice, Finanzen, Operations — als funktionale Arbeitsteilung, die zusammenarbeitet, um Produkteinführungen, Qualitätsverbesserungen, Patientendienst-Verbesserungen oder Kundenpflegeaufgaben zu erledigen. Das Unternehmen verfügt nun **gleichzeitig über zwei Mannschaften: ein menschliches Team + ein AI-Team**.

Diese Geschichte sollte vor Kursbeginn erzählt werden. Sobald der Kunde versteht „**wie der Maßstab Schicht für Schicht wächst und wie KI sich vom Werkzeug zur digitalen Arbeitskraft entwickelt**", kann er zurückkehren, um zu verstehen, warum eine Fragebogen-Diagnose nötig ist, warum der Kurs in L1-L5 geteilt wird und warum jede Stufe Deliverables, Evidence und Stage Gates braucht.

> ⚠️ Eine ausführlichere Erklärung der zwei Achsen (warum L3 → L4 die kritische Grenze ist, warum die Governance immer beim Menschen bleibt) finden Sie weiter unten unter [§Die zwei Achsen von L1-L5](#die-zwei-achsen-von-l1-l5).

## KI-Reifegradkarte

![AI Maturity Map](90_References/MD-Map.png)

## Methodik-Überblick

![Enterprise Consulting Methodology: Eight-Stage Transformation Guide](90_References/Metholodgy.png)

## Haupthandlungsstrang

```text
KI-Reifegrad-Fragebogen
→ Unternehmensprofil, Branchenkontext, Deployment-Modus erheben
→ L1-L5-Kursverhältnis entwerfen
→ L1 OpenWebUI Unternehmenskonten und persönliche Chatbereiche aktivieren
→ L2 Skill-Training mit Antigravity / Claude Code / Codex
→ L3 n8n verbindet Gmail, Sheets, Notion, CRM, API, ERP und weitere Systeme
→ L4 Hermes Agent für verifizierbare autonome Agent-Arbeit
→ L5 ClawTeam für Agentic-Team-Zusammenarbeit
→ Szenario-Cases, Evidence, Stage Gates
→ Achtstufige KI-Transformations-Beratungsdiagnose
→ KI-Transformations-Diagnosebericht, Roadmap, ROI, Governance-Empfehlungen
```

## L1-L5 Reifegradmodell

| Stufe | Name | Werkzeug / Plattform | Achse | Unternehmenspositionierung |
| --- | --- | --- | --- | --- |
| L1 | Controlled AI Access | OpenWebUI | Skalen-Achse · Individuum | Etabliert den unternehmensinternen KI-Chat-Eingangspunkt, jeder Mitarbeiter erhält ein eigenes Konto, einen Chatbereich und Berechtigungsgrenzen |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | Skalen-Achse · Abteilung | Mit Abteilungsverantwortung als Einheit werden persönliches Wissen, Prompts, Dokumente und Arbeitsmethoden in wiederverwendbare Skills verpackt |
| L3 | Workflow Automation | n8n | Skalen-Achse · abteilungsübergreifend / unternehmensweit | Verbindet abteilungsübergreifende Skills und koppelt E-Mail, Sheets, Notes, CRM, API, ERP und weitere Systeme, damit KI in unternehmensweite Automatisierungsprozesse eintritt |
| L4 | Autonomous Agent | Hermes Agent | AI-Autonomie-Achse · Super-Assistent | Kombiniert Wiki-Kompetenzkarte, AI-Tools, Workflow, automatische Planung und autonomes Lernen zu einem verifizierbaren vollautonomen AI-Agent-Super-Assistenten |
| L5 | Multi-Agent Organization | ClawTeam | AI-Autonomie-Achse · AI-Team | Mehrere spezialisierte Agents bilden eine funktionale Arbeitsteilung, arbeiten zusammen an abteilungs- und prozessübergreifenden Unternehmensaufgaben als AI-Team |

### Die zwei Achsen von L1-L5

L1-L5 sind nicht „fünf Werkzeuge", sondern ein Reifegrad-Pfad, der durch **zwei Achsen** verbunden ist:

- **L1 → L2 → L3: Skalen-Achse (Menschen nutzen / überwachen KI)**. Diese drei Schichten sind die Phase „Mensch im Loop, Mensch nutzt KI, Mensch überwacht KI" und skalieren entlang der Organisationsgröße — **L1 Individuum** (jeder Mitarbeiter nutzt KI für sich) → **L2 Abteilung** (mit Abteilungsverantwortung als Einheit persönliches Wissen in wiederverwendbare Skills verpacken) → **L3 abteilungsübergreifend / unternehmensweit** (abteilungsübergreifende Skills verbinden, Systeme koppeln, KI tritt in unternehmensweite Automatisierung ein).
- **L4 → L5: AI-Autonomie-Achse (KI läuft autonom, ohne Echtzeit-Überwachung)**. Diese zwei Schichten sind AI-Einheiten, die das Unternehmen „**zusätzlich zur menschlichen Mannschaft wachsen lässt**" — **L4 AI-Super-Assistent** (vollautonome AI-Agent-Einheit) → **L5 AI-Team** (mehrere spezialisierte Agents in funktionaler Arbeitsteilung).

> Kritische Grenze: **L1-L3 ist „Mensch unterstützt / überwacht KI", KI ist Werkzeug; L4-L5 ist „KI läuft autonom", KI ist zusätzliche digitale Arbeitskraft des Unternehmens.** In der Einführungsreihenfolge bringen L1-L3 zuerst Menschen und Organisation auf den richtigen Stand, L4-L5 wächst dann auf einer soliden Basis.
>
> Selbst bei L4-L5 **wird der Governance-Rahmen weiterhin vom Menschen aufgebaut, der Mensch behält die Aufsicht** — was die KI autonom macht, ist die „operative Ausführung", nicht die „Governance-Entscheidung". Jede Schicht behält HITL (Human-in-the-Loop) und Stage Gates bei; je autonomer die KI wird, desto mehr wird die Rolle des Menschen zum „Governor" aufgewertet — nicht ersetzt.

## Wie jede Stufe abgenommen wird

| Stufe | Input | Process | Output | Evidence | Stage Gate |
| --- | --- | --- | --- | --- | --- |
| L1 | Mitarbeiterrollen, häufige Aufgaben, KI-Schmerzpunkte, Berechtigungsbedarf | OpenWebUI einrichten, Konten / Gruppen / Berechtigungen, persönliche Chatbereiche, Prompt-Grundlagen-Training | Unternehmens-KI-Eingang, Prompt-Liste, Use-Case-Liste | Kontotabelle, Berechtigungstabelle, Login-Logs, Chatbereich-Screenshots, Prompt-Beispiele | Können sicher angemeldet, getrennt berechtigt und nachvollziehbare Nutzung erfasst werden? |
| L2 | Häufige L1-Prompts, Dokumente, SOPs, persönliche Arbeitsmethoden | Mit Antigravity / Claude Code / Codex Wissen in Skills und wiederverwendbare Artifacts verpacken | Skill Library, Agentic Artifacts, Workflow Blueprint | Skill-Dokumente, Testfälle, Versionshistorie, Output-Beispiele | Können Skills von anderen wiederverwendet werden und stabilen Output liefern? |
| L3 | L2-Skills, Prozess-Blueprints, Systeminventar, API/CRM/ERP/Sheet-Berechtigungen | Mit n8n Automatisierungs-Workflows, Data Tables, Execution Logs, Fehlerbehandlung aufbauen | Workflow PoC, Sub-Workflow Library, Data Tables, L4 Workflow Contract | n8n-Workflow, Execution Log, Retry-Logs, Systemintegrations-Screenshots | Läuft der Workflow stabil mit echten Daten und Systemen? |
| L4 | L3-Workflow, L2-Skill, Unternehmens-Wiki, Aufgabenregeln, HITL-Prüfpunkte | Mit Hermes Agent Aufgabenkarten, Wiki ingest/query/update, Scheduling, Tool-Aufrufe und Gate 4A-4E erstellen | Verifizierbarer Agent, Briefings, Aufgabenverarbeitungslogs, Gate-Sign-offs | Agent Log, Wiki-Versionen, Aufgabenkarten, Briefings, menschliche Genehmigungslogs | Kann der Agent innerhalb kontrollierter Grenzen autonom Aufgaben erledigen und Evidence hinterlassen? |
| L5 | Mehrere L4-Agents, abteilungsübergreifende Aufgaben, Rollenverantwortung, Governance-Regeln | Mit ClawTeam ein Agentic Team formieren, Rollen, Kollaborationsregeln, Übergaben und Aufsicht definieren | Agent Team, Rollenkarten, Kollaborationsflow, abteilungsübergreifende Ergebnisse | Team Run Log, Rollenkarten, Übergabelogs, Ergebnisdokumente, Governance-Logs | Kann das Agent Team stabil zusammenarbeiten und nachverfolgbare Ergebnisse liefern? |

## Prinzipien des Kursdesigns

Das Kursverhältnis wird durch Reifegrad, Branche, Deployment-Modus und Zielszenarien des Kunden bestimmt. Nicht jedes Unternehmen muss L1-L5 in einem Durchgang absolvieren — finden Sie zuerst die Schicht, die den unmittelbarsten lieferbaren Output erzeugt, und bauen Sie darauf auf.

| Erhebungsdimension | Zweck |
| --- | --- |
| Unternehmensprofil | Beurteilen, ob es sich um F&E-Fertigung, Marketing-Dienstleistung, Gesundheitseinrichtung, interne Operations oder eine andere Kategorie handelt |
| Deployment-Modus | Cloud-KI, Hybrid (Cloud + On-Prem) oder vollständig On-Prem |
| Systemlandschaft | Inventarisierung von Gmail, Sheets, Notion, CRM, API, ERP, Datenbanken, internen Systemen |
| Prozessreife | Vorhandensein von SOPs, Process Owners, Datenfeldern, Ausnahmebehandlung beurteilen |
| Risikoanforderungen | Sicherheit, Datenschutz, Compliance in Gesundheit / Fertigung / Finanzen und menschliche Sign-off-Bedürfnisse bewerten |

## Verzeichnisstruktur

| Verzeichnis | Zweck |
| --- | --- |
| [`00_Overview`](00_Overview/) | Lösungsüberblick, Haupthandlung, WBS |
| [`01_Assessment`](01_Assessment/) | KI-Reifegrad-Fragebogen, Scoring-Modell, Deliverables und Evidence-Matrix |
| [`02_Course_Design`](02_Course_Design/) | L1-L5-Kursplanung, Unternehmensprofil, Deployment-Modi, Kursmodul-Matrix |
| [`03_Consulting_Report`](03_Consulting_Report/) | KI-Transformations-Diagnose-Berichtsvorlage |
| [`04_Scenarios`](04_Scenarios/) | Kundenszenarien, Kontrolltabellen, Fertigungs-Case, Krankenhaus-Case |
| [`05_Sales`](05_Sales/) | Wertversprechen, Verkaufsgesprächspunkte, FAQ |
| [`06_Delivery`](06_Delivery/) | Delivery-Paket und Abnahmekriterien |
| [`90_References`](90_References/) | Original-PDF, Methodik-Diagramme, Video-Lernnotizen, Zitate |

## Lesergruppen: Mit welcher der 5 Dateien beginnen?

| Sie sind | Beginnen Sie mit |
| --- | --- |
| **CEO / Eigentümer / Familienmitglied** — die Methodik in 20 Minuten verstehen | [`00_Overview/CLIENT_JOURNEY_STORY_EN.md`](00_Overview/CLIENT_JOURNEY_STORY_EN.md) — Mings Geschichte |
| **Berater / Lernender** — wissen, wie die 8 Stufen ablaufen, wie Verträge geteilt werden | [`00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) — vollständiger Ablauf |
| **Vorstand / Regulierung / Wissenschaft** — warum diese Methodik einer Debatte standhält | [`00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — wissenschaftliche Argumentation |
| **Enterprise-IT / Berater anderer Firma** — Abgleich mit McKinsey/BCG/TOGAF/Gartner | [`00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — Alignment-Karte |
| **Eilige Führungskraft** — nur 5 Minuten | [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) — Executive Summary |
| **Methodik-Forscher / AI-Pedagogy-Akademiker** — warum dies eine neue Form der Methodik ist | [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) — AI-Native Living Book Design |
| **Akademiker / Regulierung / Vorstand** — 7 theoretische Säulen (Rosemann / Cohen & Levinthal / Teece / Real Options usw.) | [`00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — akademische theoretische Grundlagen |
| **Berater / Scoring-Kalibrierung** — wie 0-4 Punkte objektiv vergeben, Subjektivität vermeiden | [`01_Assessment/BARS_RUBRICS_EN.md`](01_Assessment/BARS_RUBRICS_EN.md) — BARS Behavioral Anchors |

## Empfohlene Lesereihenfolge

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md)
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md)
4. [`01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)
5. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
6. [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md)
7. [`02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md)
8. [`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md)
9. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md)
10. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md)
11. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)
12. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)

## Verifizierbare Deliverables

- KI-Reifegrad-Fragebogen und Scoring-Ergebnisse
- Unternehmensprofil- und Deployment-Modus-Erhebung
- L1-L5-Kursabschluss-Evidence
- OpenWebUI Konto- / Gruppen- / Berechtigungstabelle und persönliche Chatbereich-Aktivierungslogs
- Skill Library und Antigravity / Claude Code / Codex Artifacts
- n8n Workflow PoC, Execution Log, Data Tables, Sub-Workflow Library
- Hermes Agent Aufgabenkarten, Wiki, ingest/query/update-Logs, Briefings und Gate 4A-4E
- ClawTeam Agent Team Rollenkarten, Kollaborationslogs und Ergebnisdokumente
- Stage-Gate-Abnahmeprotokolle
- KI-Transformations-Diagnosebericht
- 30 / 60 / 90-Tage-Roadmap

## Referenzen

- [`90_References/@AI-MD-PUBIC.pdf`](90_References/@AI-MD-PUBIC.pdf)
- [`90_References/MD-Map.png`](90_References/MD-Map.png)
- [`90_References/Metholodgy.png`](90_References/Metholodgy.png)
- [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md)
- [`90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

## Danksagung

Besonderer Dank gilt **Prof. Michael Rosemann**, Queensland University of Technology (QUT), Brisbane, Australien.  
Profil: <https://www.qut.edu.au/about/our-people/academic-profiles/m.rosemann>

Die theoretische Grundlage der gesamten Beratungsmethodik dieses Repos stammt aus dem Studium des Autors an der QUT und der langjährigen Inspiration und Lehre von Prof. Michael Rosemann in **Business Process Management (BPM)**, **Capability Maturity Models** und **Methodik für Unternehmensinnovation**.

Zwei Kerngestaltungen sind besonders beeinflusst:

- **Achtstufige Beratungsstruktur**: entspricht Prozessdiagnose, Fähigkeitsbewertung, Transformationspfaddesign und Governance-Implementierung.
- **L1-L5 KI-Reifegradmodell**: angelehnt an die Capability-Maturity-Logik und für den fünfschichtigen Adoptionsrahmen von KI in Unternehmen lokalisiert.

Haftungsausschluss: Alle Fehler, Auslassungen, lokalen Anpassungen oder KI-Domain-Erweiterungen in dieser Methodik liegen in der alleinigen Verantwortung des Autors Tiger AI Morris Lu 盧業興 und repräsentieren nicht die Ansichten oder Positionen von Prof. Michael Rosemann oder der QUT.

## Lizenz und Urhebernennung

Dieses Projekt steht unter der **[Apache License 2.0](LICENSE)**-Lizenz. Sie dürfen es frei nutzen, kopieren, modifizieren, bearbeiten, reproduzieren, verbreiten, lehren, in Beratung liefern und kommerziell verwenden.

Bei Weiterverteilung, Bearbeitung, kommerzieller Verpackung, Verwendung in Schulungsmaterialien, Beratungsdokumenten oder Produktdokumentation bewahren Sie bitte den Apache-2.0-Lizenztext und die folgende Urhebernennung aus [`NOTICE`](NOTICE) auf:

```text
Original Author: Tiger AI Morris Lu 盧業興
Role: n8n Taipei Ambassador / PhD Student, Graduate Institute of Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australia
Source: https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit
```

Drittanbieter-Plattformnamen, Marken, Videos, externe Projekte und zitierte Inhalte bleiben Eigentum der jeweiligen Rechteinhaber. Dieses Repo nutzt Drittanbieter-Material ausschließlich als Lernnotizen, Zitate, Organisation und Referenz für Kursdesign.

---

## Dieses Buch zum Leben erwecken: gemeinsam mit der KI lesen

Die folgende Setup-Anleitung führt Sie durch die Verbindung des Repos mit einer AI-IDE. Bevor Sie loslegen, verstehen Sie das Bedienmodell und eine rote Linie.

**Bedienmodell in einem Satz**: `git clone` oder ZIP herunterladen → mit einer AI-IDE (Antigravity / Claude Code / Codex usw.) öffnen → die KI liest [`AGENTS.md`](AGENTS.md) (und den eigenen `<ENGINE>.md` jedes Engines) automatisch und positioniert sich als **Co-Reading-Tutor dieser Methodik**. Anschließend können Sie (1) jede Frage zur Methodik stellen, (2) die Methodik auf Ihr Unternehmen anwenden lassen, (3) gemeinsam die L1-L5-Selbstdiagnose durchführen und den nächsten Schritt finden.

Vollständige Diskussion: [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md).

> ⚠️ **Hinweis zur wissenschaftlichen Integrität / Academic Integrity Disclaimer**
>
> **Alle in diesem Repo namentlich genannten Fallstudien (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 SAMPLE_CLIENT_CASE) und Hauptfiguren (z. B. „Ming" / „MingChang Packaging") sind KI-generierte fiktive Beispiele**, KEINE echten Kundendaten.
> Alle Zahlen (Zeit, ROI, Personenmonate, Budget, KPI) sind **nur illustrativ** und **dürfen nicht für externes Marketing, vertragliche Zusagen oder akademische empirische Belege verwendet werden**.
> Echte longitudinale Cases werden erst nach Abschluss der 18-24-monatigen empirischen Studie gemäß [`90_References/PILOT_STUDY_PROTOCOL_EN.md`](90_References/PILOT_STUDY_PROTOCOL_EN.md) ersetzt.
>
> **All named cases and story protagonists in this repo are AI-generated fictional examples**, NOT real client data.

## 🚀 Installations- und Startanleitung der drei AI-Engines / Three AI Engines Setup Guide

Die **Rollen und Arbeitsteilung** der drei Engines wurden bereits oben unter „🔱 Drei AI-Engines mit unterschiedlichen Spezialisierungen" vorgestellt. Dieser Abschnitt konzentriert sich auf **wie installieren, wie starten, wie Workflows aufrufen**. Die drei Unterabschnitte sind eigenständig — wählen Sie den Engine, den Sie nutzen wollen, und lesen Sie nur diesen.

> ⚠️ **Gemäß [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0**: Die Methodik-Architektur, L1-L5, die acht Stufen und die Arbeitsteilung der drei Engines sind allesamt strategische Entwürfe, die von **Morris Lu (Mensch)** vorgeschlagen wurden. Die drei AI-Engines unter der Anleitung von Morris **führen aus, vervollständigen, erweitern und prüfen** — sie beanspruchen kein Eigentum an der Methodik-Architektur. Die detaillierte Selbstbeschreibung jedes Engines befindet sich in der entsprechenden Datei unter [`07_AI_Contributions/`](07_AI_Contributions/).

---

### 🟦 1. Antigravity-Nutzer — Interaktiver Frontlinien-Berater

> Veredeln Sie dieses „statische lebendige Buch" direkt zu Ihrer „**Conversational Consulting App**".

**Installation und Nutzung:**

1. **Projekt laden**: `git clone` oder ZIP des Projekts lokal herunterladen
2. **IDE starten**: Projektordner mit Antigravity öffnen
3. **Auto-Initialisierung**: Antigravity liest [`ANTIGRAVITY.md`](ANTIGRAVITY.md) und [`SKILL.md`](SKILL.md) automatisch und positioniert sich als „**Co-Reading-Tutor**"
4. **Workflows ausführen (Slash Commands)**: Befehl im Chat eingeben, um die Interaktion zu starten

**Häufige Antigravity-Befehle:**

- `/diagnose` ── startet einen realistischen Dialog und führt Sie (oder Ihren Kunden) durch die L1-L5-Unternehmens-KI-Reifegrad-Diagnose
- `/generate-report` ── überführt frühere Diagnose- und Diskussionsergebnisse in die Standard-Beraterberichtsvorlage und erstellt einen Entwurf

Siehe [`.agent/workflows/`](.agent/workflows/) und [`07_AI_Contributions/ANTIGRAVITY.md`](07_AI_Contributions/ANTIGRAVITY.md).

> Antigravity-Kernwert: Die Methodik in ein Beratungserlebnis verwandeln, das **Kunden verstehen und sofort interaktiv erleben können**.

---

### 🟪 2. Codex-Nutzer — Methodik-Engineering-Engine

> Betrachten Sie dieses Repo als „**Methodik-Engineering-Workspace**" — pflegen Sie dieses AI-native living book als Methodik-Produkt, das **testbar, auditierbar, nachverfolgbar, reparierbar, releasebar** ist.

**Installation und Nutzung:**

1. **Projekt laden**: `git clone` oder ZIP des Projekts lokal herunterladen
2. **Codex starten**: Projektordner in Codex öffnen
3. **Codex-Eingangsdatei lesen**: Codex zuerst [`CODEX.md`](CODEX.md) und [`.codex/README.md`](.codex/README.md) lesen lassen
4. **Codex-Workflows ausführen**: Workflow-Name im Chat eingeben oder Codex explizit auffordern, die entsprechende Datei auszuführen

**Häufige Codex-Befehle (10):**

| Kategorie | Befehl | Zweck |
| --- | --- | --- |
| Production | `/diagnose` | Interaktive KI-Reifegrad-Vorabbeurteilung |
| Production | `/generate-report` | Entwurf des Beratungs-Diagnoseberichts |
| Quality | `/evidence-audit` | Evidence-Kette des Berichts prüfen |
| Quality | `/consistency-review` | Dokumentübergreifende Konsistenz von L1-L5, Stage Gate, HITL, Evidence prüfen |
| Evolution | `/academic-upgrade` | Akademische Empfehlungen in Methodik-Reparaturplan umsetzen |
| Evolution | `/harvest-insights` | Gemeinsame Insights aus mehreren Lieferberichten extrahieren |
| Defense | `/test-methodology` | Methodik unter Extremszenarien stress-testen |
| Defense | `/red-team-review` | Red-Team-Review von Beraterbericht-Entwürfen |
| Audit | `/generate-traceability` | Traceability-Matrix questionnaire → maturity → evidence → report erzeugen |
| DevOps | `/bump-version` | Semantische Versionsnummer und CHANGELOG vorschlagen |

**Empfohlene Aufrufweise:**

```text
Bitte folge .codex/workflows/evidence-audit.md, um diesen Beraterberichtsentwurf zu prüfen.
```

Siehe [`.codex/workflows/`](.codex/workflows/) und [`07_AI_Contributions/CODEX.md`](07_AI_Contributions/CODEX.md).

> Codex-Kernwert: Der Methodik einen „**testbaren, auditierbaren, nachverfolgbaren, reparierbaren, releasebaren**" Engineering-Lebenszyklus geben.

---

### 🟨 3. Claude Code-Nutzer — Engine für dateiübergreifendes strategisches Denken und Experimente

> **Spielen / testen / zerlegen / kollidieren** Sie die Methodik einmal. Nutzen Sie Claude Codes 1M-Kontext + parallele Multi-Persona + domänenübergreifende abstrakte Argumentation zum **Simulieren, Experimentieren, Debattieren, Forken**.

**Installation und Nutzung:**

1. **Projekt laden**: `git clone` oder ZIP des Projekts lokal herunterladen
2. **Claude Code starten**: Projektordner in Claude Code CLI / IDE öffnen
3. **Claude Code-Eingangsdatei lesen**: Claude Code zuerst [`CLAUDE.md`](CLAUDE.md) und [`.claude/README.md`](.claude/README.md) lesen lassen
4. **Claude Code-Workflows ausführen**: Workflow-Name im Chat eingeben

**Häufige Claude Code-Befehle (10):**

| Kategorie | Befehl | Zweck |
| --- | --- | --- |
| Tier 1 Tactical | `/deep-synthesize` | Mehrdatei-Tiefensynthese (1M-Kontext) |
| Tier 1 Tactical | `/theory-bridge` | Kundenkontext ↔ 7 theoretische Säulen abbilden |
| Tier 1 Tactical | `/scenario-planning` | Mit gegebenen Einschränkungen 3 kontrastierende Roadmaps + Trade-offs erzeugen |
| Tier 1 Tactical | `/socratic-challenge` | Sokratisches Nachfragen, um das Denken des Nutzers zu schärfen |
| Tier 1 Tactical | `/cross-stage-trace` | Downstream-Wirkung einer einzelnen Änderung nachverfolgen |
| Tier 2 Original | `/simulate-engagement` | Vollständigen 6-wöchigen Beratungseinsatz in 30 Minuten durchspielen (12+ Deliverables) |
| Tier 2 Original | `/parallel-perspectives` | 6 Stakeholder **gleichzeitig** zur selben Entscheidung + Konfliktkarte |
| Tier 2 Original | `/thought-experiment` | Counterfactual Stress Test der Methodik („Was, wenn der EU AI Act L4 verbietet?") |
| Tier 2 Original | `/devil-pair-debate` | Zwei-Claude-Adversarial-Debate + Richter-Synthese |
| Tier 2 Original | `/methodology-fork` | Standardmethodik in einen kundenspezifischen Fork überführen (Methodology-as-Code) |

**Empfohlene Aufrufweise:**

```text
Bitte folge .claude/workflows/simulate-engagement.md, um einen 6-wöchigen Beratungseinsatz
für einen Fertigungskunden mit 500 Mitarbeitern zu simulieren.
```

Siehe [`.claude/workflows/`](.claude/workflows/) und [`07_AI_Contributions/CLAUDE_CODE.md`](07_AI_Contributions/CLAUDE_CODE.md).

> Claude Code-Kernwert: Die Methodik von „**einer Standardversion**" zu „**Standard + N Derivate + vollständige Simulationen + Mehrperspektivendebatten**" weiterentwickeln — ein experimentierbares lebendiges Buch.

---

### Empfehlungen für Drei-Engine-Workflow / Three-Engine Workflow Suggestions

Häufiger Kollaborationsrhythmus in der Praxis:

```text
Phase A — Kundendiagnose
  → Antigravity läuft /diagnose, sammelt den Ist-Zustand
  → Claude Code läuft /theory-bridge für theoretische Diagnose
  → Antigravity läuft /generate-report für einen Zwischenberichtsentwurf
  → Codex läuft /evidence-audit für die Evidence-Kette
  → Codex läuft /consistency-review für dateiübergreifenden Abgleich

Phase B — Strategiedesign
  → Claude Code läuft /scenario-planning für 3 Roadmaps
  → Claude Code läuft /parallel-perspectives für 6-Stakeholder-Sichten
  → Codex läuft /red-team-review gegen Überoptimismus
  → Claude Code läuft /devil-pair-debate für Wertannahmen-Debatte

Phase C — Umsetzung und Evolution
  → Codex läuft /generate-traceability für quartalsweise Audits
  → Claude Code läuft /thought-experiment für Counterfactual-Stress-Tests
  → Codex läuft /bump-version für Methodik-Versionspflege
  → Claude Code läuft /methodology-fork für Derivate für Großkunden
```

> Die Workflows der drei Engines sind nicht exklusiv — **der Punkt ist, dass jeder Engine das tut, was er am besten kann**, und der Mensch (Berater / Client Owner / Sponsor) entscheidet, wann gewechselt wird.
