# Executive Summary: Die gesamte Methodik in 5 Minuten (10 Minuten für das Gesamtbild)

> 🌐 中文 / Chinese: [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) ｜ English: [EXECUTIVE_SUMMARY_EN.md](EXECUTIVE_SUMMARY_EN.md)
>
> **5-Minuten-Version**: Lesen Sie §1 „Auf einer Seite" + §2 „Kernmodell" — das reicht.
> **10-Minuten-Version**: Ergänzen Sie §3-§7 (lebendiges Buch, Theorie, Kurse, Beratung, Lieferung, Co-Lesen, nächste Schritte).
> Klicken Sie nur auf die verlinkten Dateien, wenn Sie tiefer einsteigen wollen.

---

## 1. Auf einer Seite: Was es löst

Viele Unternehmen führen KI ein, indem sie „**direkt zu den Werkzeugen springen**" — ChatGPT kaufen, n8n testen, Agents bauen wollen. Das Ergebnis: Mitarbeiter können es nicht nutzen, Prozesse sind nicht verbunden, Daten sind nicht governanced, PoCs lassen sich nicht abnehmen, und die Führung hat keine Ahnung, wie reif die Unternehmens-KI tatsächlich ist.

Diese Methodik verwandelt „**verstreute KI-Nutzung**" in eine „**reproduzierbare, governance-fähige, messbare, skalierbare organisationale Fähigkeit**" — mit einer geschlossenen Schleife aus **Fragebogen + Kursen + Beratung**, die ein Unternehmen von **Individuen, die KI nutzen** bis zu **einem Unternehmen, das ein KI-Team besitzt** führt.

| Element | In einem Satz |
|---|---|
| **Diagnose-Tool** | 10 / 25 / 50-Punkte-Fragebogen → objektive L1-L5-Position + Lücken auf sechs Dimensionen |
| **Ausbildungspfad** | 5-stufige Kurse (OpenWebUI / Antigravity / n8n / Hermes / ClawTeam) + BARS-Scoring-Kalibrierung |
| **Beratungsstruktur** | 8 Stufen (Awareness → Acceptance Test) + 3-Phasen-Vertrag (A Diagnose / B Strategie / C Implementierung) |
| **Akademische Grundlage** | 7 theoretische Säulen (Rosemann / Cohen & Levinthal / Teece / Real Options / usw.) |
| **Trägermedium** | **AI-Native Living Book** — eine Methodik, die wirklich *lebendig* ist, direkt mit einer AI-IDE co-lesbar |

---

## 2. Kernmodell: Die zwei Achsen von L1-L5

L1-L5 sind nicht „fünf Werkzeuge" — sondern ein Reifegrad-Pfad, der durch **zwei Achsen** verbunden ist:

| Achse | Bereich | Treiber | Schichten | Werkzeuge |
|---|---|---|---|---|
| **Skalen-Achse** | L1 → L2 → L3 | **Menschen** nutzen KI, **Menschen** überwachen KI | Individuum → Abteilung → abteilungsübergreifend / unternehmensweit | OpenWebUI / Antigravity / n8n |
| **AI-Autonomie-Achse** | L4 → L5 | **KI** läuft autonom; Menschen treten als **Governor** zurück | AI-Einheit → AI-Team | Hermes Agent / ClawTeam |

**Kritische Grenze = L3 → L4**: vom „Menschen treiben die Arbeit" zum „KI treibt die Arbeit". Selbst bei L4-L5 wird **der Governance-Rahmen weiterhin von Menschen aufgebaut, Menschen behalten die Aufsicht** — was KI autonom macht, ist „operative Ausführung", nicht „Governance-Entscheidung".

➜ Vollständige Geschichte: [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0

---

## 3. AI-Native Living Book — Warum dieses Buch *lebendig* ist

Diese Methodik ist kein PDF / PPT / SOP — **es ist ein Buch, das wirklich *lebendig* ist**:

| Generation | Form | Begrenzung |
|---|---|---|
| Gen 1 — Gedruckte Bücher | Papier | **Statisch** — können nur gelesen werden, antworten nicht |
| Gen 2 — Interaktive Bücher | Web / Wiki | **Oberfläche lebendig, Inhalt nicht** — schlagen immer noch nichts proaktiv vor |
| **Gen 3 — AI-Native Books** (dieses Repo) | Markdown + AI-IDE | **Wirklich lebendig** — lässt Sie fragen, antwortet für Sie, denkt mit Ihnen, führt Diagnosen durch / erstellt Berichte / simuliert Szenarien basierend auf Ihrer Unternehmenssituation |

**Bedienmodell**: `git clone` → mit einer AI-IDE (Antigravity / Claude Code / Codex) öffnen → KI liest automatisch das gesamte Buch → positioniert sich als **Co-Reading-Tutor** für diese Methodik → Sie unterhalten sich, fragen und wenden direkt an.

➜ Vollständige Diskussion: [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md)

### Drei AI-Engines, jede mit einer anderen Spezialisierung

| Engine | Rolle | Worin sie am besten ist | Workflows |
|---|---|---|---|
| 🟦 **Antigravity** | Frontlinien-Berater | Mit Kunden sprechen, Fragebögen durchführen, Berichte entwerfen | `/diagnose`, `/generate-report` |
| 🟪 **Codex CLI** | Methodik-Auditor | Dateiübergreifende Tests, Red-Team-Review, Versionskontrolle, Reparatur | `/evidence-audit`, `/red-team-review`, `/bump-version` und 7 weitere |
| 🟨 **Claude Code** | Dateiübergreifender Denkpartner | Tiefensynthese, Multi-Perspektiven-Debatte, Simulation, kundenspezifische Forks | `/simulate-engagement`, `/devil-pair-debate`, `/methodology-fork` und 7 weitere |

➜ Drei-Engine-Selbstoffenlegung: [`../07_AI_Contributions/`](../07_AI_Contributions/) ｜ Setup-Anleitung: root [`../README_DE.md`](../README_DE.md) §🚀

---

## 4. Akademische Grundlage: 7 theoretische Säulen

Diese Methodik ist nicht ad-hoc. Jedes Schlüsseldesign **bildet eine klassische Theorie ab** — die Standardantwort, wenn Akademiker, Regulatoren oder Vorstände nach „was ist die theoretische Basis?" fragen:

| # | Theorie | Begründer | Rolle in dieser Methodik |
|---|---|---|---|
| 1 | **Capability Maturity** | Rosemann (QUT) / CMMI | Das schulische Fundament für L1-L5-Reife |
| 2 | **Absorptive Capacity** | Cohen & Levinthal (1990) | Erklärt, warum manche Unternehmen bei L1 stecken bleiben — ihnen fehlt Vorwissen |
| 3 | **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | Stage 7 To-Be-Design: welche Aufgaben sollten L4 erreichen, welche sollten bei L2 bleiben |
| 4 | **Dynamic Capabilities** | Teece (1997, 2007) | sense / seize / transform — warum KI-Governance eine „Fähigkeit" ist, keine „Policy" |
| 5 | **Sociotechnical Systems & Trust in AI** | Bostrom (1977) / Dietvorst (2015) / Glikson (2020) | Warum L4-L5 HITL beibehalten müssen — Menschen vertrauen nicht blind autonomer KI |
| 6 | **Real Options Theory** | Dixit & Pindyck (1994) / McGrath (1997) | Warum Phase 1 mit NPV ≈ 0 trotzdem lohnt — Sie kaufen die Option zur Expansion |
| 7 | **Executable Knowledge Artifact** | Knuth (1984) Literate Programming + moderne Erweiterungen | Warum diese Methodik Markdown + AI-IDE-Co-Lesen ist statt PDF |

➜ Vollständige theoretische Diskussion (mit Zitaten): [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md)
➜ Fehlermuster (wo Theorie Versagen vorhersagt): [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md)
➜ Pilot-Studie-Design (18-24-Monats-Empirie): [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md)

---

## 5. Ausbildung: Das vollständige L1-L5-Curriculum

Jede Stufe hat **eigene Kursmaterialien + verifizierbare Deliverables + Stage-Gate-Abnahme**:

| Stufe | Name | Werkzeug | Kursplan |
|---|---|---|---|
| L1 | Controlled AI Access | OpenWebUI | [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) |
| L3 | Workflow Automation | n8n + Tiger AI Skill Pack | [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) |
| L4 | Autonomous Agent | Hermes Agent + Wiki | [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) |
| L5 | Multi-Agent Organization | ClawTeam | (L5 enthalten in [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)) |

**Designprinzip**: Kunden müssen nicht L1-L5 in einem Durchgang machen. Nutzen Sie den Fragebogen, um **die Schicht zu finden, die die unmittelbarsten Deliverables produziert**, und bauen Sie darauf auf. Der Kursmix wird durch Unternehmensprofil, Branche, Deployment-Modus (Cloud / Hybrid / On-Prem) und Risikoanforderungen bestimmt.

➜ Vollständiges Kurspaket: [`../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
➜ Scoring-Kalibrierung (Subjektivität vermeiden): [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) BARS

---

## 6. Beratung: 8 Stufen + 3-Phasen-Vertragsmodell

### 6.1 Die acht Stufen

| # | Stufe | Hauptaktion |
|---|---|---|
| 1 | **Awareness** | KI-Bewusstsein und Kundenvision aufbauen |
| 2 | **Reference Model** | Kunden zur Unterzeichnung des Ideal-Practice-Radars führen |
| 3 | **Discovery** | As-Is-Stand, Shadow IT, System-Inventar erfassen |
| 4 | **Gap Analysis** | Ideal Practice vs. As-Is vergleichen; High-Impact-Lücken identifizieren |
| 5 | **Stakeholder Mapping** | Sponsor, AI Champion, HR, Compliance identifizieren |
| 6 | **Diagnosis** | Schichtenübergreifende Analyse (inkl. Verankerung an den 7 Säulen) |
| 7 | **To-Be Design** | TTF / Real Options nutzen für eine stufige Roadmap |
| 8 | **Acceptance Test** | Stage-Gate-Sign-off + vierteljährliche Radar-Review |

### 6.2 Drei-Phasen-Vertrag

| Phase | Dauer | Hauptliefergegenstand |
|---|---|---|
| **Phase A — Diagnose** | 2 Wochen | Zwischen-Diagnose-Bericht + signiertes Ideal Practice |
| **Phase B — Strategie** | 4 Wochen | Voller 14-Kapitel-Beratungsbericht + 24-Monats-Roadmap + ROI + Governance-Empfehlungen |
| **Phase C — Implementierung** | 24 Monate | Phasenweise Umsetzung + vierteljährliche Radar-Review + kontinuierliche Evolution |

➜ Vollständige 8-Stufen-Geschichte (mit Dialog-Beispielen): [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md)
➜ Beratungsberichts-Vorlage: [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)
➜ Beratungs-Toolkit-Vorlagen: [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md)
➜ Delivery-Paket & Abnahme: [`../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)

---

## 7. Verifizierbare Deliverables: Was jede Stufe hinterlässt

Jeder „Kurs" endet nicht einfach nach der Vorlesung — er hinterlässt auditierbare Evidence:

| Stufe | Hauptliefergegenstände | Evidence |
|---|---|---|
| L1 | Persönlicher Chat-Workspace, Prompt Library | Kontotabelle, Berechtigungstabelle, Login-Records, Prompt-Beispiele |
| L2 | Skill Library, Agentic Artifacts | Skill-Dokumente, Testfälle, Versionshistorie, Output-Beispiele |
| L3 | n8n Workflow PoC, Sub-Workflow Library, Data Tables | Execution Logs, Retry-Logs, Systemintegrations-Screenshots |
| L4 | Verifizierbarer Agent, Briefings, Task Cards | Agent Log, Wiki-Versionen, HITL-Sign-off-Records |
| L5 | Agent Team Rollenkarten, Kollaborationsflow, abteilungsübergreifende Ergebnisse | Team Run Log, Handover-Records, Governance-Records |
| **Beratungsebene** | 14-Kapitel-Diagnosebericht, 30/60/90-Tage-Roadmap, ROI, Governance-Empfehlungen | Stage-Gate-Sign-off-Records, vierteljährliche Radar-Review |

➜ Vollständige Deliverables + Evidence-Matrix: [`../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)

---

## 8. Wie man dieses Buch nutzt (5 Einstiegspfade nach Rolle)

| Sie sind | Hier anfangen (20 Min → 1 Std) |
|---|---|
| **CEO / Eigentümer / Familie, die die Methodik begreifen wollen** | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) — Mings Geschichte |
| **Berater / Lernende** | [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) — voller 8-Stufen-Ablauf |
| **Vorstand / Regulierer / Akademiker** | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — wissenschaftliche Argumentation |
| **Enterprise-IT / firmenübergreifende Berater** | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — Abgleich mit McKinsey/BCG/TOGAF/Gartner |
| **Methodik-Forscher / AI-Pedagogy-Akademiker** | [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) — warum dies eine neue Form der Methodik ist |

---

## 9. Referenz-Schnellindex

### 9.1 Akademische Theorie & Fehlermodi

- [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — volle Diskussion der 7 theoretischen Säulen
- [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) — 14 Fehlermuster (theorie-prädiziert)
- [`../90_References/AI_GOVERNANCE_ALIGNMENT.md`](../90_References/AI_GOVERNANCE_ALIGNMENT.md) — Abgleich mit NIST AI RMF / EU AI Act / ISO 42001
- [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) — 18-24-Monats-Empirie-Design

### 9.2 Ausbildung & Assessment

- [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) — 10/25/50-Punkte-Fragebogen (plain-language)
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL.md) — Scoring-Modell
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) — BARS-Scoring-Kalibrierung (Subjektivität vermeiden)
- [`../02_Course_Design/`](../02_Course_Design/) — volle L1-L5-Kurspläne

### 9.3 Beratungslieferung

- [`../03_Consulting_Report/`](../03_Consulting_Report/) — Beratungsbericht + Toolkit-Vorlagen
- [`../04_Scenarios/`](../04_Scenarios/) — 7 Branchen-Szenarien (Fertigung / Krankenhaus / Marketing / B2B / Finanzen / Regierung / Bildung)
- [`../05_Sales/`](../05_Sales/) — Verkaufsargumentation + FAQ
- [`../06_Delivery/`](../06_Delivery/) — Delivery-Paket + Abnahmekriterien + Engagement Lifecycle

### 9.4 Drei-Engine-Selbstoffenlegung

- [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) — drei-engine-co-edited README + §3 Co-Authoring-Disziplin
- [`../07_AI_Contributions/ANTIGRAVITY.md`](../07_AI_Contributions/ANTIGRAVITY.md) ｜ [`CODEX.md`](../07_AI_Contributions/CODEX.md) ｜ [`CLAUDE_CODE.md`](../07_AI_Contributions/CLAUDE_CODE.md)
- [`../CHANGELOG.md`](../CHANGELOG.md) — drei-engine-co-edited Changelog

### 9.5 Quellmaterial

- [`../90_References/@AI-MD-PUBIC.pdf`](../90_References/@AI-MD-PUBIC.pdf) — Original-PDF-Methodik
- [`../90_References/MD-Map.png`](../90_References/MD-Map.png) — AI Maturity Map
- [`../90_References/Metholodgy.png`](../90_References/Metholodgy.png) — Acht-Stufen-Transformations-Guide-Diagramm
- [`../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) — Video-Lernnotizen
- [`../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

---

## 10. Nächste Schritte: 3 empfohlene Pfade

| Ihr Bedarf | Empfohlener nächster Schritt |
|---|---|
| **Das Gesamt-Mental-Modell aufbauen** | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) (inkl. §3.0, die volle Zwei-Achsen-Geschichte) |
| **Herausfinden, in welcher Stufe Ihr Unternehmen ist** | Das 10-Punkte-Schnell-Diagnostik in [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) |
| **Dieses Buch direkt mit KI lesen** | Repo mit AI-IDE öffnen → zuerst root [`../README_DE.md`](../README_DE.md) §🚀 Drei AI Engines Setup Guide lesen und einen Engine starten |

---

> ⚠️ **Hinweis zur wissenschaftlichen Integrität**: Alle namentlich genannten Fälle in diesem Repo (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 SAMPLE_CLIENT_CASE-Dateien) und alle Hauptfiguren (z. B. „Ming" und „MingChang Packaging") sind **KI-generierte fiktive Beispiele**, KEINE echten Kundendaten. Alle Zahlen (Zeit, ROI, Personenmonate, Budget, KPI) sind **nur illustrativ** und **dürfen NICHT für externes Marketing, vertragliche Zusagen oder akademische empirische Belege verwendet werden**. Echte longitudinale Cases werden nur nach Abschluss der 18-24-monatigen empirischen Studie gemäß [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) ersetzt.
>
> **Architektur-Eigentum**: Die Methodik-Architektur in diesem Repo wurde vom menschlichen Autor **Morris Lu (Tiger AI)** entworfen. Die drei AI-Engines (Antigravity / Codex / Claude Code) sind Werkzeuge, die **ausführen, vervollständigen, erweitern und prüfen**. Siehe [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0.
