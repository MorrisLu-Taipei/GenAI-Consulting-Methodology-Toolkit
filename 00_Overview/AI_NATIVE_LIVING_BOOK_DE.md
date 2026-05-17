# AI-Native Living Book: Methodik als Executable Knowledge Artifact

> 🌐 Sprache: [繁體中文](AI_NATIVE_LIVING_BOOK.md) ｜ [English](AI_NATIVE_LIVING_BOOK_EN.md) ｜ Deutsch ｜ [Français](AI_NATIVE_LIVING_BOOK_FR.md) ｜ [Español](AI_NATIVE_LIVING_BOOK_ES.md) ｜ [日本語](AI_NATIVE_LIVING_BOOK_JA.md) ｜ [한국어](AI_NATIVE_LIVING_BOOK_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Letzte Aktualisierung: 2026-05-16

---

> **Was dieses Dokument beantwortet**: Das distinktivste Feature dieser Methodik ist nicht ihr Inhalt — es ist ihr **Trägermedium**. Traditionelle Consulting-Methodiken sind PDFs / PPTs / SOPs (statische Dokumente); dieses Repo ist ein **Knowledge-System, lesbar, erklärbar, abfragbar und anwendbar durch AI-IDEs**. Nutzer „lesen keine Dokumente" — sie **konversieren mit der Methodik**. Dieses Dokument schreibt diese Charakteristik formal in die Positionierung der Methodik und adressiert ihre akademische Klassifikation + Risk Controls.

---

## 1. Ein-Satz-Positionierung / Tagline

> Dieses Repository ist nicht nur ein Methodik-Toolkit, sondern ein **AI-native Living Book**: wenn in einer AI-IDE geöffnet, verwandeln seine eingebetteten Agent-Anweisungen ([`AGENTS.md`](../AGENTS.md) und [`CLAUDE.md`](../CLAUDE.md)) die statische Methodik in einen **interaktiven Co-Reading-Tutor und Consulting-Assistenten**.

---

## 2. Warum dies eine neue Form von Methodik ist

### 2.1 Traditionelle Methodik vs. AI-Native Living Book

| Dimension | Traditionell (PDF / PPT / SOP) | AI-Native Living Book (dieses Repo) |
| --- | --- | --- |
| **Medium** | Statische Dokumente, Slide Decks, Word | Markdown + AI-IDE Instruction-Dateien (AGENTS.md / CLAUDE.md) |
| **Nutzer-Interaktion** | Einweg-Lesen | Zweiweg-Konversation (Q&A, Anwendung, Generierung) |
| **Onboarding-Barriere** | Hoch (muss 100+ Seiten lesen) | Niedrig (AI auto-liest, wird Co-Reading-Tutor) |
| **Wie anwenden** | Berater übersetzt für Kunden | Kunde fragt AI direkt, auf ihre Firma anzuwenden |
| **Kann angefochten werden** | Nein (Dokumente antworten nicht) | Ja (AI beantwortet jede Frage in Echtzeit) |
| **Kann neu geschrieben werden** | Berater muss editieren | Kunde forkt + AI assistiert mit Consistency Checking |
| **Versionskontrolle** | Meist keine | Volle Git-History (inkl. AGENTS.md Änderungen) |
| **Akademische Zitation** | PDF zitieren | GitHub Commit Hash + reproduzierbare Execution-Umgebung zitieren |

### 2.2 Akademische Klassifikationen

Diese Methodik kann kategorisiert werden als eine (oder mehrere) von:

| Name | Betontes Property | Ursprung / Analog |
| --- | --- | --- |
| **Executable Knowledge Artifact** | Wissen, das ausgeführt werden kann; nicht nur beschrieben, sondern anwendbar | Jupyter Notebooks, Computational Essays |
| **AI-Mediated Methodology** | AI als Vermittler zwischen Nutzer und Methodik | Intelligent Tutoring Systems (ITS) |
| **Interactive Consulting Playbook** | Interaktives Consulting-Operations-Manual | Game Playbooks, Decision-Tree Wizards |
| **Living Book with Embedded Tutor Agent** | Living Book + eingebetteter Tutor Agent | Hypertext, Knowledge Graphs |

Tiger AI adoptiert **AI-Native Living Book** als primären Begriff, weil es **gleichzeitig erfasst** „Living Book" (Inhalt entwickelt sich) + „AI-Native" (für AI designt) + „Co-Reading-Tutor" (eingebettete Tutor-Persönlichkeit).

---

## 3. Drei Schichten: Repo als Buch / Agent als Tutor / Methodik als Executable Artifact

### 3.1 Schicht 1: Repo als Buch

Die Repo-Struktur folgt Buch-Konventionen:

| Buch-Element | Repo-Mapping |
| --- | --- |
| Cover / Ein-Satz-Position | Root [`README_EN.md`](../README_EN.md) + dieses Doc §1 |
| Vorwort / Executive Summary | [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) |
| Story-Kapitel | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) Mings Story |
| Hauptmethodik | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 |
| Implementierungs-Kapitel | `01_Assessment` / `02_Course_Design` / `03_Consulting_Report` |
| Case-Anthologie | `04_Scenarios/` 7 Benchmark-grade Cases |
| Sales Support | `05_Sales/` |
| Delivery SOP | `06_Delivery/` |
| Akademisches Argument | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) |
| Alignment-Map | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) |
| Failure Modes (Counter-Cases) | [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) |
| Forschungsdesign | [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) |
| Referenzen | Referenzen jeder Datei + `90_References/` |

> **Schlüsselpunkt**: Dieses „Buch" ist **vollständig** — Kunden / Berater / Akademiker / Regulatoren können jeweils ihr relevantes Kapitel finden.

### 3.2 Schicht 2: Agent als Tutor (AGENTS.md ist die „Tutor-Persönlichkeit")

[`AGENTS.md`](../AGENTS.md) und [`CLAUDE.md`](../CLAUDE.md) sind keine supplementären Notizen, sondern **betten die Rolle, Grenzen und Anleitung der AI in das Repo ein**. AI-IDEs (Claude Code / Cursor / Antigravity / Codex etc.) auto-lesen diese Dateien und positionieren sich als **„Co-Reading-Tutoren für diese Methodik"**.

#### „Tutor-Persönlichkeit" definiert in AGENTS.md

- **Rolle**: AI = Co-Reading-Tutor + Consulting-Assistent, NICHT Berater-Ersatz
- **Scope beantwortbarer Fragen**: Methodik-Definitionen, L1-L5 Mapping, Stage Tools, Case-Anwendung, Report-Drafts
- **Refusal Scope**: finale Kundenentscheidungen, Berater-Urteil umgehen, unverified ROI-Commitments
- **Antwort-Stil**: akademische Strenge + Consulting-Praxis + kunden-verständlich
- **Zitations-Disziplin**: jede Schlussfolgerung mit [E:L#] Evidence Level (per Tool 8.9) getaggt
- **Sprache**: bilinguales EN/ZH Switching durch Nutzer

> Dieses Design borgt von **LangChain Agent Prompt + Claude Skills**: Konfigurationsdateien, die im Repo versioniert werden.

### 3.3 Schicht 3: Methodik als Executable Artifact

Nutzer können AI direkt bitten, die Methodik **auszuführen**, nicht nur zu lesen:

#### Typische Interaktionen

| Nutzer fragt | AI Co-Reading-Tutor führt aus |
| --- | --- |
| „Wir sind eine 700-Mitarbeiter Verpackungsfabrik; hilf mir, die 10-Q Quick Survey zu laufen" | AI läuft [`AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) 10-Q Version + Auto-Scores + produziert Radar |
| „Basierend auf meinen Antworten, entwirf eine Phase A Mid-Engagement Report Skelett" | AI generiert Draft per [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) §3-§5 Struktur |
| „Wir sind Manufacturing; welcher Case ist uns am nächsten?" | AI vergleicht mit [`SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md) und berechnet Gap |
| „Bereite Materialien für den Stage 3 Client Ideal Practice Workshop vor" | AI generiert Workshop-Flow + Sticky-Note Prompts + 4-Schichten-Printout per Tool 3.6 |
| „Wie alignt das mit McKinsey 7-Step?" | AI mappt auf [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) §2.1 |
| „Sollte mein Stage 2 Radar nach 24 Monaten runder sein?" | AI führt Nutzer durch Quarterly Gate C Review |

> **Das ist die Bedeutung von „Methodik als Executable Artifact"** — Methodik wird nicht nur beschrieben; sie ist in Echtzeit via AI anwendbar.

---

## 4. Methodik-Adoption-Barrieren senken

### 4.1 Unternehmen fürchten 100+ Markdown-Dateien

Traditionelle Methodik-Barrieren:

- 100+ Seiten zu lesen ❌
- Zu viel Terminologie ❌
- Wissen nicht, was zuerst zu lesen ❌
- Brauchen Berater zur Übersetzung ❌
- Müssen Report-Draft selbst schreiben ❌

### 4.2 AI Co-Reading-Tutor antwortet in Echtzeit

Sobald Repo + AI-IDE geöffnet, fragen Nutzer direkt:

- „**Auf welchem Level ist meine Firma?**" → AI läuft 10-Q Survey + Auto-Scores
- „**Welche Datei sollte ich zuerst lesen?**" → AI empfiehlt Lese-Reihenfolge nach Rolle (CEO / Berater / IT / Akademiker)
- „**Wie wende ich das auf Manufacturing an?**" → AI zitiert Manufacturing-Case + flaggt Anpassungspunkte
- „**Bitte generiere den First-Draft Diagnostic Report**" → AI produziert 10-15 Seiten Phase A Skelett
- „**Was ist die Grenze zwischen Stage 4 und Stage 8?**" → AI zitiert METHODOLOGY_SCIENTIFIC_LOGIC §4

> **Das verschiebt Methodik von „nur-Experten-lesbar" zu „Nicht-Experten können durchgeführt werden."**

### 4.3 Erwartete Reduktion der Adoption-Barriere

Hypothesen, validiert durch PILOT_STUDY_PROTOCOL:

- Traditionelle PDF-Methodik: Client Completion Rate < 15%
- **AI-Native Living Book**: Client „Conversation Rate" > 70% (AI führt proaktiv)
- Mittelständische Enterprise (100-500 Mitarbeiter) Adoption-Zyklus: von „3-Monats-Evaluation nötig" → „Phase A innerhalb von 2 Wochen"

---

## 5. Risk Controls

⚠️ Weil AI die Methodik interpretiert, **darf AI Co-Reading-Tutor NICHT** das Folgende tun:

### 5.1 Tutor-Grenzen

| Kann | Kann nicht |
| --- | --- |
| Methodik-Inhalt erklären | ❌ Formales Berater-Urteil ersetzen |
| Surveys laufen, auto-scoren, Radare produzieren | ❌ Spezifische ROI-Zahlen Kunden versprechen |
| Cases zitieren, um Gaps zu berechnen | ❌ Ideal Practice Definition Table unterzeichnen (erfordert 3-Parteien-Menschen-Unterschrift) |
| Report-Drafts generieren | ❌ Client Owner / Berater Final Review ersetzen |
| Stage Gate Self-Assessment führen | ❌ Drittparteien-Audit ersetzen |
| 80/20 / 5 Whys / Issue Tree in Echtzeit anwenden | ❌ Longitudinale KPI-Real-Daten ersetzen |

### 5.2 4 Risk Control Prinzipien

1. **AI Co-Reading-Tutor ≠ Berater**: alle Report-Drafts erfordern **menschlichen Berater oder Client Owner Review** vor externer Nutzung
2. **Wichtige Diagnosen erfordern Evidence**: per [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9, Hauptkonklusionen brauchen L3+ (System Log) Support
3. **AGENTS.md Versionskontrolle**: vermeide inkonsistente Interpretation über AI-IDEs hinweg — commite jede AGENTS.md Änderung zu Git und zeichne im CHANGELOG auf
4. **AI-Generated Marking**: per Tool 8.8 §7, aller AI-generierter Content muss als „AI-generated" markiert werden

### 5.3 Failure-Szenarien

Falls der AI Co-Reading-Tutor missbraucht wird (dokumentiert in [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md)):

- AI erret und Kunde nimmt es bare Münze → falscher Report
- AI gibt unverified ROI-Zahlen → Kunde unterzeichnet SOW basierend auf falscher Hoffnung
- Verschiedene AI-IDEs interpretieren AGENTS.md unterschiedlich → inkonsistente Schlussfolgerungen

**Mitigations**:

- AGENTS.md mandatet explizit „**Don't predict ROI without baseline data**"
- Jeder Report-Absatz erfordert [E:L#] Evidence-Level-Tag
- Kunden ermutigen, kritische Schlussfolgerungen mit ≥ 2 AI-IDEs cross-zu-validieren

---

## 6. Akademischer Beitrag

### 6.1 Beiträge zu IS / Consulting-Methodik

| Beitrag | Innovation |
| --- | --- |
| **Methodik-Medium-Innovation** | Erste Consulting-Methodik gebaut als Markdown + Agent Config direkt ausführbar durch AI-IDEs |
| **AI-Mediated Knowledge Transfer** | AI als „Knowledge-Translator" zu verwenden senkt Methodik-Adoption-Barrieren |
| **Open-Source Consulting Framework** | Apache 2.0, kann von anderen Beratern geforkt / adaptiert werden, akademisch reproduzierbar |
| **Embedded Tutor Agent Design Pattern** | AGENTS.md / CLAUDE.md Pattern kann von anderen Open-Source-Repos geborgt werden |

### 6.2 Verbindung zu AI Pedagogy / ITS

- 1980er ITS-Forschung studierte „wie AI lehrt" → diese Methodik ist ein neuer Case von „**wie AI Erwachsenen hilft, professionelle Methodiken zu lernen**"
- Anwendung von Vygotsky's ZPD (Zone of Proximal Development): AI Co-Reading-Tutor passt dynamisch Prompt-Tiefe an

### 6.3 Zukünftige Forschung

- Cross-IDE Consistency der AGENTS.md-Interpretation (Claude Code / Cursor / Antigravity / Codex / Windsurf)
- Longitudinales Tracking des Effekts des AI Co-Reading-Tutors auf Methodik-Adoption-Rate (per PILOT_STUDY_PROTOCOL Design)
- Cross-Language (EN / ZH / JA / KO) Methodik-Adoptability-Forschung

---

## 7. Wie es mit anderen Dokumenten kombiniert

### 7.1 Statement in verschiedenen Lokationen

| Lokation | Hauptbotschaft |
| --- | --- |
| Root [`README.md`](../README.md) | Ein-Satz-Positionierung (ZH §1) |
| Root [`README_EN.md`](../README_EN.md) | Ein-Satz-Positionierung (EN §1) |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) | „Living Book" Sektion |
| [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) | „How to Read This Book" Sektion |
| [`AGENTS.md`](../AGENTS.md) | Konkrete Tutor-Persönlichkeits-Config (im Repo Root) |
| Sales Decks | 1 Slide hebt „AI-Native Living Book" Differenzierung hervor |
| Akademische Submissions | Ganzes Kapitel als Methodik-Beitrag |

### 7.2 Beziehung zu 4 anderen autoritativen Konzept-Docs

| Dokument | Frage, die es beantwortet |
| --- | --- |
| [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) | „Was erlebt der Nutzer?" |
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | „Wie läuft die Methodik?" |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | „Warum hält die Methodik der Debatte stand?" |
| [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | „Wie alignt sie mit Branchen-Frameworks?" |
| **`AI_NATIVE_LIVING_BOOK_EN.md` (dieses Doc)** | **„Warum ist das Medium der Methodik neu?"** |

5 autoritative Docs bilden ein vollständiges Methodik-Argument: **Erfahrung + Prozess + Wissenschaft + Alignment + Form-Innovation**.

---

## 8. Referenzen

- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors: Lessons learned. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.
- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Pérez, F., & Granger, B. E. (2007). IPython: A system for interactive scientific computing. *Computing in Science & Engineering*, 9(3), 21-29.
- Anthropic (2024). *Claude Code documentation*: <https://docs.anthropic.com/claude/docs/claude-code>
- OpenAI (2024). *Codex / Codex CLI*.
- Cursor (n.d.). *Cursor IDE documentation*.

---

## 9. Abschluss: Die nächste Phase der Methodik

Evolution von Consulting-Methodiken:

```
1990s: Paper Consulting Reports
   ↓
2000s: PowerPoint Decks
   ↓
2010s: SharePoint / Confluence Wikis
   ↓
2020s: GitHub-hosted Methodology + Open Source
   ↓
2025s: AI-Native Living Book (diese Methodik)
```

**Was kommt als Nächstes?** Möglicherweise **Multi-Agent Consulting Team Auto-Running Full Phase A** (AI Berater + AI Reviewer + AI Client Simulator, 3-Agent Collaboration) — L5 Multi-Agent Organization auf „die Methodik selbst" anwenden.

**Aber**: per §5.1, AI ist immer Tool und Tutor, nie Ersatz. Menschliches Berater-Urteil, Client Owner Decision-Making, Drittparteien-Audit — diese **menschlichen Governance-Schichten** sind die finalen Garantien der Methodik-Glaubwürdigkeit.

---

Lizenz & Zitation

Dieses Dokument ist Apache License 2.0; darf verwendet, modifiziert, kommerzialisiert werden, vorausgesetzt die [`../NOTICE`](../NOTICE) Attribution wird beibehalten.
