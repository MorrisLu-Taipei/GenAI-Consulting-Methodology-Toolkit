# Tiger AI Methodik-Abgleich mit Branchen-Frameworks

> 🌐 Sprache: [繁體中文](INDUSTRY_FRAMEWORK_ALIGNMENT.md) ｜ [English](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) ｜ Deutsch ｜ [Français](INDUSTRY_FRAMEWORK_ALIGNMENT_FR.md) ｜ [Español](INDUSTRY_FRAMEWORK_ALIGNMENT_ES.md) ｜ [日本語](INDUSTRY_FRAMEWORK_ALIGNMENT_JA.md) ｜ [한국어](INDUSTRY_FRAMEWORK_ALIGNMENT_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Letzte Aktualisierung: 2026-05-15

---

> **Was dieses Dokument beantwortet**: Wie verhält sich die Tiger AI Methodik zu Mainstream-Beratungsfirmen (McKinsey / BCG / Bain / Deloitte / Accenture / PwC), akademischen Schulen (Rosemann BPM / CMMI / APQC / SCOR / TOGAF / Dragon1) und KI-Reifeframeworks (Gartner / MIT / MMC / Forrester)? Was duplizieren, vervollständigen oder erneuern wir?
>
> **Kernhaltung**: Tiger AI erfindet das Rad nicht neu, sondern **integriert Mainstream-Werkzeuge, vervollständigt den Branchen-Closed-Loop und ergänzt um GenAI-Ära-Essenzen**. Alle zitierten Frameworks sind detailliert in [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md); dieses Dokument mappt firmenübergreifend.

---

## 1. Warum dieser Abgleich wichtig ist

| Zielgruppe | Was sie erhalten |
| --- | --- |
| Großunternehmen IT/CIO | „Diese Methodik ist kompatibel mit unserem bestehenden TOGAF / ITIL / APQC" |
| Berater aus anderen Firmen | „Ich komme von BCG/Deloitte — ich sehe, welche Werkzeuge ich weiter nutze und welche Tiger-AI-spezifisch sind" |
| Akademische Reviewer | „Tiger AI ist keine Randwissenschaft — sie steht auf den Schultern der Rosemann/CMMI/APQC-Schulen" |
| Regulatoren | „Zitierte Standards sind international anerkannt; KI-Governance mappt auf bestehende GRC-Frameworks" |
| Klient-Führungskräfte | „Wir zahlen für Branchen-Best + GenAI-Ära-Vervollständigung, nicht für die proprietäre Methode einer einzelnen Firma" |

---

## 2. Acht Stufen vs. Mainstream-Beratungsfirmen

### 2.1 Firmenübergreifende Abgleichtabelle

| Stufe | Tiger AI | McKinsey | BCG | Bain | Deloitte | Accenture | PwC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1 As-Is Snapshot** | 40-Q Interview + Inventory + Swimlane | 7-Step Step 1: Define Problem | Diagnostic Survey | Customer / Process Diagnostics | Business Architecture Discovery | Living Business Diagnostic | Value Creation Diagnostic |
| **2 Reference Model** | APQC + Tiger AI L1-L5 + 4-Schichten | (selten gemacht) | Capability Maturity Map | (nicht-Kern) | TOGAF Capability Assessment | Industry Reference Architecture | Capability Framework |
| **3 Best Practice → Ideal** | Benchmark + Ideal Practice Workshop | Best Practice Research | Strategic Position vs Industry | NPS / Customer Loyalty | Industry Pulse | Industry Benchmarking | Industry Outlook |
| **4 Gap Analysis** | M/B/R + Impact×Effort | Issue Tree + MECE | Importance-Performance Map | Pareto + Lean | Capability Gap Heatmap | Maturity Gap Analysis | Gap Map |
| **5 Problem Definition** | 80/20 + 5 Whys + EPS | Day-1 + SCQ + Pyramid | Strategic Diagnosis | Bain Question Pyramid | Hypothesis-Driven | Outcome-Driven | Issue-Tree Synthesis |
| **6 Phased Goals** | Phased + Absorption | Workplan + Critical Path | Phased Transformation | Bain Way Multi-phase | Imagine-Deliver-Run | Wave Planning | Transformation Wave |
| **7 To-Be Design** | Phased To-Be + Human-AI | To-Be Operating Model | Operating Model Design | Bain Way (Org) | Target Operating Model | Future-State Blueprint | Future Operating Model |
| **8 Implementation & Change** | Roadmap + Change + Value Tracking | Influence Model + 7S | Smart Simplicity | Bain Results Delivery | Diamond Performance | Wired for Change | Project Delivery |

### 2.2 Was jede Firma beiträgt

- **McKinsey** MECE / Pyramid / Issue Tree **sind Quellen für Tiger AI Stage 4-5 Tools** (in der Frameworks Library)
- **BCG** Capability Maturity-Denken **inspiriert Tiger AI Stage 2 RM-Scoring**
- **Bain** Customer / Process Diagnostics **ergänzen die Tiger AI Stage 1 Interview-Bank**
- **Deloitte** Imagine-Deliver-Run **deckt sich stark mit Tiger AI Stage 6 Drei-Phasen**
- **Accenture** Wave Planning **konsistent mit Tiger AI Phase 1/2/3**
- **PwC** Value Creation Diagnostic **mappt auf Tiger AI Stage 8 Value Tracking**

> **Fazit**: Keine der 8 Stufen ist eine Tiger-AI-„Erfindung". **Innovation liegt in der Integration dieser verstreuten Werkzeuge zu einer vollständigen Argumentationskette mit Datenabhängigkeiten, Klient-Unterschriften und Closed-Loop-Falsifikation**.

---

## 3. Reference Model Schul-Abgleich

### 3.1 Tiger AI 4 Schichten vs. Hauptsächliche EA-Frameworks

| Schicht | Tiger AI | Dragon1 EA | TOGAF ADM | Zachman | ArchiMate |
| --- | --- | --- | --- | --- | --- |
| **L1 Governance** | AI Governance | Enterprise Governance | (Architecture Vision) | Scope | Motivation + Strategy |
| **L2 Business** | AI Business (L1-L5 hier) | Business(es) | Business Architecture (B) | Business | Business Layer |
| **L3 Information** | AI Information | Information Facilities & Systems | Data + Application (C+D) | System | Application + Information |
| **L4 Technical** | AI Technical | IT Infrastructure(s) | Technology (E) | Technology | Technology + Implementation |

**Warum dieser Abgleich**: alle Mainstream-EA-Frameworks konvergieren auf „**4 Abstraktionsschichten**" — kein Zufall, sondern ein notwendiges Ergebnis der „Abstraktion × Volatilität" wissenschaftlichen Achse (siehe [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) §5).

### 3.2 Process Reference Model Abgleich

| Anwendungsfall | Tiger AI empfiehlt | APQC PCF | SCOR | eTOM | ITIL | CMMI |
| --- | --- | --- | --- | --- | --- | --- |
| **Branchenübergreifende Prozesse** | APQC PCF (Standard) | ✓ 13 Cat | — | — | — | — |
| **Supply Chain / Fertigung** | SCOR | — | ✓ 6 Sektionen | — | — | — |
| **Telekom / Abonnement** | eTOM | — | — | ✓ 3 Levels | — | — |
| **IT Service Management** | ITIL | — | — | — | ✓ 5 Phasen | — |
| **Software-Reife** | CMMI | — | — | — | — | ✓ 5 Levels |
| **KI-Adoption-Reife** | **Tiger AI L1-L5 (DIY, füllt Branchenlücke)** | — | — | — | — | — |

> **Kein existierendes Branchen-RM deckt KI-Adoption ab** — daher die Notwendigkeit der Tiger AI L1-L5, selbstqualifiziert mit Tool 2.5 Score 9/10.

### 3.3 BPM Maturity Schul-Wurzeln

| Konzept | Quelle | Tiger AI Mapping |
| --- | --- | --- |
| Capability Maturity Levels (5-stufige Skala) | **Rosemann BPM Maturity** (QUT) + CMMI | Stage 2 0-4 Scoring, Tiger AI L1-L5 |
| Process Excellence Characteristics | Rosemann + APQC | Stage 3 Excellence Capability Profile |
| Stage Gates | CMMI + Rosemann | Stage 6 Acceptance Gates |
| Organizational Absorption | Rosemann (neue Forschung) | Tool 6.3 Absorption Assessment |

> **Danksagung**: Prof. Michael Rosemann (QUT) ist der Master-Advisor des Autors; die BPM-Schul-Wurzeln dieser Methodik kommen direkt aus seiner langjährigen Mentorschaft.

---

## 4. KI-Reifeframework-Abgleich

### 4.1 Wichtige KI-Reifeframeworks gemappt

| Framework | Levels | Tiger AI L1-L5 Mapping |
| --- | --- | --- |
| **Gartner AI Maturity Model** | Awareness / Active / Operational / Systemic / Transformational | L1 / L1+L2 / L3 / L4 / L5 |
| **MIT Sloan AI Capability** | Experimenters / Investigators / Pioneers / Empowerment | L1-L2 / L2-L3 / L3-L4 / L5 |
| **McKinsey AI Quotient (AIQ)** | (kontinuierliche Skala, 4 Treiber) | Mappt auf Tiger AI Sechs-Dimensionen-Radar |
| **Capgemini DELTA Maturity** | Data / Enterprise / Leadership / Targets / Analysts | Mappt auf Governance + Deployment-Achse |
| **Forrester AI Pulse Index** | (3 Ringe: People / Process / Tech) | Mappt auf Tiger AI 4-Schichten-Architektur |
| **Tiger AI L1-L5** | L1 Chat / L2 Skill / L3 Workflow / L4 Auto Agent / L5 Agent Team | (**Skalenachse L1-L3 + KI-Autonomieachse L4-L5**) |

### 4.2 Tiger AI L1-L5 Ergänzungen zum Mainstream

| Ergänzung | Warum die Branche es nicht hat | Tiger AI füllt es |
| --- | --- | --- |
| **Explizites Tool-Mapping** | Gartner/MIT beschreiben Levels abstrakt, kein Tool-Landing | L1=OpenWebUI, L2=Antigravity, L3=n8n, L4=Hermes, L5=ClawTeam |
| **Skalenachse von Autonomieachse getrennt** | Branche mischt sie, verwischt L4-L5 | Skala (menschengeführt) vs Autonomie (KI-geführt), kritische Grenze L3→L4 |
| **GenAI-spezifisch (nicht traditionelles ML)** | Die meisten Frameworks stecken bei traditionellem ML / Vorhersagemodellen | Voll fokussiert auf LLM / Agent / Workflow-Paradigma |
| **Verifizierbare Stage Acceptance** | Branchen-Frameworks meist Selbsteinschätzungsskalen | Jedes Level hat Stage Gate Criteria, unabhängig verifizierbar |
| **Cross-RM Dual-Koordinaten** | Branchen-Frameworks einachsig | Tiger AI orthogonal zu Branchen-RM (APQC/SCOR), Dual-Radar |

---

## 5. Abgleich klassischer Analyse-Werkzeuge

Detailliert in [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md). Zusammenfassung:

### 5.1 Strategie-Werkzeuge

Porter's 5 Forces (Stage 3), PESTEL (Stage 3), BCG Growth-Share (Stage 3), SWOT (Stage 3/4), Blue Ocean (Stage 7), Wardley Map (Stage 6/7).

### 5.2 Problemanalyse-Werkzeuge

MECE (Stage 2/4), Issue Tree (Stage 4/5), Pyramid Principle (Stage 5), SCQ (Stage 5), 5 Whys (Stage 5), Fishbone (Stage 4/5), Hypothesis-Driven (Stage 1-5), 80/20 (Stage 5).

### 5.3 Change-Management-Werkzeuge

Kotter 8 Steps (Stage 8), ADKAR (Stage 8), Stakeholder Map (Stage 8), RACI (Stage 8), Influence Model (Stage 8), 7S (Stage 2/8).

### 5.4 Finanz- / ROI-Werkzeuge

NPV/IRR (Stage 8), Payback (Stage 8), Break-Even (Stage 8), Sensitivity Analysis (Stage 8), Balanced Scorecard (Stage 8), OKR (Stage 6/8).

---

## 6. Tiger AI einzigartige / innovative Elemente

Die meisten Tools kommen aus der Branche, aber Tiger AI hat diese **einzigartigen Integrationen oder Innovationen**:

| Innovation | Warum die Branche es nicht hat | Tiger AI Design |
| --- | --- | --- |
| **Tiger AI L1-L5 GenAI Adoption RM** | Branchen-RMs noch bei IT / traditionellem ML | Erstes RM speziell für LLM/Agent/Workflow entworfen, erfüllt Tool 2.5 10 Bedingungen 9/10 |
| **Client Ideal Practice Co-Creation Workshop** | Branche macht Best Practice Benchmarking, aber selten Klient-signiertes Ideal | Tool 3.6: Klient **signiert selbst**, kann spätere Argumentation nicht leugnen |
| **Cases-as-Benchmarks 9-Felder-Format** | Branchencases meist narrativ, keine Gap-Berechnung | Tool 3.5: Cases müssen 9 Felder haben, Klient berechnet Gap in 30 Min selbst |
| **Quartalsweise Stage 2 Radar-Loopback** | Branchen-Roadmaps meist linear, keine Selbst-Falsifizierungsmechanik | Phase C jedes Quartal Gate C muss Radar erneut besuchen, verifizieren dass Struktur tatsächlich runder |
| **3-Phasen-Vertragsmodell + Gate A/B/C Ausstiege** | Branche meist fixed-Scope Großverträge | Phase A Diagnostic / Phase B Strategy / Phase C Implementation, Klient phasiert Entscheidungen |
| **Skalenachse vs KI-Autonomieachse orthogonal** | Branche mischt auf einer Achse | L1-L3 Skala + L4-L5 Autonomie, kritische L3→L4 Grenze |
| **4-Schichten RM × L1-L5 Dual-Koordinaten** | Branche einachsig (entweder RM oder Reife) | Tiger AI verlangt Dual-Achsen-Cross-Mapping |
| **HITL-Knoten explizit pro Prozess** | Branche spricht Governance, spezifiziert selten HITL-Standort | Tool 7.2 jeder Prozess explizit mit HITL-Knoten + Acceptance Criteria markiert |

---

## 7. Häufige Klient-Frage: Steht das im Konflikt mit unserer Methodik?

### 7.1 Klient nutzt TOGAF / Zachman

**Kein Konflikt**. Tiger AI 4 Schichten **deckt sich direkt mit TOGAF BDAT** (Business/Data/Application/Technology). Sage: „Wir bauen auf eurer bestehenden TOGAF-Architektur auf und ergänzen die GenAI-Adoption-Dimension (L1-L5) und den quartalsweisen Radar-Closed-Loop."

### 7.2 Klient nutzt ITIL

**Kein Konflikt**. Tiger AI Stage 8 Audit Log / Permission Matrix / Risk Register verbindet sich direkt mit ITIL Service Operation. Sage: „Wir ergänzen GenAI-spezifische LLM-Call-Logs, Reviewer-Simulation, Skill-Versions-Governance."

### 7.3 Klient nutzt CMMI

**Kein Konflikt**. Tiger AI L1-L5 und CMMI 5 Levels **sind verwandt** — beide Maturity-Capability-Schulerweiterungen. Sage: „CMMI for AI ist eine aufkommende Richtung; Tiger AI L1-L5 ist eine Landing-Version."

### 7.4 Klient nutzt BCG / McKinsey / Bain interne Frameworks

**Kein Konflikt, gegenseitige Verstärkung**. Tiger AI zitiert die Kernwerkzeuge dieser Firmen (Issue Tree, MECE, Pyramid, Bain Way). Sage: „Wir ersetzen nicht eure Strategieberatungsmethodik; wir fügen den GenAI-Adoption-Closed-Loop und das 4-Schichten Reference Model hinzu."

### 7.5 Klient nutzt Gartner / Forrester AI Maturity

**Kein Konflikt, konkreter**. Tiger AI L1-L5 hat **konkretere Landing-Tools** als Gartners 5 Levels (L1=OpenWebUI usw.). Sage: „Gartner sagt ‚Operational AI'; wir sagen ‚n8n Workflow 3 live + Reviewer Sign-off-Rate 95%'."

---

## 8. Akademischer Zitations-Abgleich

Zitate in den jeweiligen Datei-Referenzen. Ausgewählt:

### 8.1 BPM / Maturity Schule

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT. **(Kern-theoretische Wurzel)**
- Paulk, M. et al. (1993). *Capability Maturity Model for Software*. CMU/SEI.
- Curtis, B. et al. (2009). *People CMM*.

### 8.2 Reference Model / Enterprise Architecture

- APQC (2024). *Process Classification Framework Version 7.3*.
- APICS / ASCM. *SCOR Reference Model*.
- TM Forum. *eTOM Business Process Framework*.
- ISACA. *COBIT / ITIL Framework*.
- The Open Group. *TOGAF Standard 9.2*.
- Zachman, J. *Zachman Framework*.
- Dragon1. *Enterprise Architecture Reference Model*.

### 8.3 Beratungsmethodiken

- Minto, B. (2009). *The Pyramid Principle*.
- Rasiel, E. (1999). *The McKinsey Way*.
- Bain & Company. *Bain Way / Results Delivery*.
- Iansiti, M., Lakhani, K. (2020). *Competing in the Age of AI*.

### 8.4 Change Management

- Kotter, J. (1996). *Leading Change*.
- Hiatt, J. (2006). *ADKAR*. Prosci.
- Mendelow, A. (1991). *Stakeholder Mapping*.

### 8.5 GenAI Strategie

- Gartner. *AI Maturity Model*.
- Davenport, T., Mittal, N. (2022). *All-in on AI*.
- Brynjolfsson, E., McAfee, A. (2014). *The Second Machine Age*.

---

## 9. Schluss: Auf den Schultern von Giganten + Vervollständigung des Branchen-Closed-Loops

Tiger AI Methodik-Designphilosophie:

1. **Keine Räder neu erfinden**: Strategieanalyse (McKinsey), Change Mgmt (Kotter), Finanztools (NPV/IRR), EA-Frameworks (TOGAF/Dragon1) — nutze die Besten der Branche
2. **Integration + Closed Loop**: verstreute Werkzeuge zu einer vollständigen Argumentationskette mit Datenabhängigkeiten, Klient-Unterschriften und Falsifizierungsmechanik zusammenbinden
3. **GenAI-Lücken füllen**: Branchen-Frameworks sind nicht mit LLM/Agent/Workflow-Ära nachgekommen → Tiger AI L1-L5 + 4-Schichten + Cases-as-Benchmarks + HITL-Design füllt es
4. **Reproduzierbar durch andere**: Apache 2.0 + GitHub + klare akademische Zitate → kein Privatasset einer Firma

> **Das ist die Bedeutung von „Auf den Schultern von Giganten + Vervollständigung des Branchen-Closed-Loops"** — was Klienten kaufen, ist Branchen-Best-Integration + GenAI-Ära-Vervollständigung, nicht die proprietäre Methode einer einzelnen Firma.

---

## 10. Verwandte Dokumente

| Dokument | Beziehung |
| --- | --- |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) §8 | Kompakte Version dieses Dokuments §2 (vs McKinsey/BCG/Gartner/MIT) |
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | Wie die 8 Stufen tatsächlich in einer realen Engagement laufen |
| [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md) | 50+ Frameworks detailliert (dieses Dokument = Abgleichkarte; jene Datei = Framework-Wörterbuch) |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | Per-Stage Tool-Tabellen |

---

Lizenz & Zitation

Dieses Dokument ist Apache License 2.0; darf verwendet, modifiziert, kommerzialisiert werden, sofern die [`../NOTICE`](../NOTICE) Attribution erhalten bleibt.
