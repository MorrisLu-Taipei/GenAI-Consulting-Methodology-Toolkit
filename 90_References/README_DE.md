# 90 References — Referenzmaterial, Quellen & Acknowledgments

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. Zweck dieses Verzeichnisses

Dieses Verzeichnis ist die **Referenzbibliothek, Citation-Governance-Zentrum und Acknowledgments-Liste** der gesamten Methodik. `00`-`07` sind „Methode und Werkzeuge"; dieses Verzeichnis beantwortet drei Dinge:

1. **Worauf basieren diese Methoden?** (Original-PDF, Methodik-Diagramme, Video-Lernnotizen)
2. **Welcher Inhalt zitiert Dritte? Sind die Lizenzen compliant?** (jedes zitierte Projekt hat eigene `*_REFERENCE.md`)
3. **Auf welchen Schultern stehen wir?** (Acknowledgments-Liste)

Wer nutzt: Berater, Reviewer, Rechtsabteilung, Redistributoren, **Lernende und Enthusiasten, die die Upstream-Projekte suchen**.

---

## 2. Acknowledgments: auf wessen Schultern wir stehen

Organisiert nach Nutzungsebene in vier Kategorien: **Core-Plattformen / Consulting-Framework-Klasse / Agent & Skill-Klasse / Case-Index-Klasse**. Jede „Appreciation Card" enthält **Upstream-URL + wo wir es zitieren + Link zur vollständigen _REFERENCE.md**.

### 2.1 Core-Plattformen (die Runtime-Basis für L1-L5)

Diese sind nicht „zitiertes Material" — sie sind **die Plattformen, auf denen L1-L5-Kurse laufen**. Ohne sie kann diese Methodik nicht landen.

#### 🎯 [`open-webui/open-webui`](https://github.com/open-webui/open-webui) (Open-Source, Lizenz siehe Upstream LICENSE)

- **Was es ist**: Open-Source, selbst-hostbares Enterprise-AI-Chat-Interface. Unterstützt mehrere LLM-Provider (OpenAI / Anthropic / Ollama / OpenRouter / Azure usw.), Konten / Gruppen / Rollen / Permissions, persönliche Chat-Workspaces, Modellsteuerung, Pipelines, Function Calling, Wissensbasen, RAG, Bild/Audio/Datei-Upload.
- **Warum wir es schätzen**: einer der wenigen Open-Source-Lösungen, die „**den unternehmensinternen AI-Chat-Eingangspunkt**" zu „**ein-Klick-installierbar, vollständig on-prem, permissions-tiered, auditierbar**" macht. Lässt Unternehmen LLMs ausprobieren, ohne Daten an SaaS zu senden — kritisch für on-prem-Deployment in Manufacturing / Healthcare / Government. Aktive Community, schnelle Versionsevolution.
- **Wo wir es nutzen**: **die Core-Plattform von L1 Controlled AI Access** — [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) vollständiger Kursplan; Video-Lernnotizen in [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md).

#### 🎯 [`n8n-io/n8n`](https://github.com/n8n-io/n8n) (Sustainable Use License, Lizenz siehe Upstream LICENSE.md)

- **Was es ist**: Open-Source Workflow-Automatisierungsplattform. Visueller Editor, 1000+ Integrationen (Gmail, Sheets, Notion, Slack, CRM, API, ERP, Datenbanken, Webhooks, eigene Knoten), Sub-Workflow Library, Data Tables, Execution Logs, Fehlerbehandlung, geplante Trigger, AI / LangChain Knoten. Unterstützt Self-Host und Cloud.
- **Warum wir es schätzen**: die „**LEGO-Bausteine**" der Cross-System-Automatisierung — Berater können in 1-2 Tagen ein PoC für Kundendemos zusammenstellen. Aktive Community, reichhaltige Vorlagen, gesundes Geschäftsmodell. **Self-Hosting ist kritisch für Enterprise-Adoption** (Daten bleiben intern). Der Autor der Methodik ist auch n8n Taipei Ambassador.
- **Wo wir es nutzen**: **der Core-Engine von L3 Workflow Automation** — [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) vollständiger Kursplan; 35 implementierbare PoC-Specs in [`../02_Course_Design/POC_SCENARIO_SPECS.md`](../02_Course_Design/POC_SCENARIO_SPECS.md); 30 Workflow-JSON-Skelette in [`../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md`](../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md); Video-Lernnotizen in [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md).

#### 🎯 [`nousresearch/hermes-agent`](https://github.com/nousresearch/hermes-agent) (Nous Research, Lizenz siehe Upstream LICENSE)

- **Was es ist**: Nous Research's Open-Source **Knowledge-grade Autonomous Agent** Reference-Implementierung — **Wiki-Capability-Map-Memory + ingest / query / update Drei-Schritt-Knowledge-Compounding + scheduled Tasks + Gate 4A-4E + HITL Human Review**. Designziel: ein verifizierbarer „vollautonomer AI Agent Super-Assistant".
- **Warum wir es schätzen**: integriert „**Autonomous Agent + Knowledge Management**" in ein verifizierbares Design-Pattern — die **„Sieben Designprinzipien für Knowledge-grade Agents"** (light-day-heavy-night / Knowledge-Compounding-Loop / P1>P2 / Write-Read-Same-Source / Tool-vs-LLM-Division / Failure-driven Learning / Why-not-just-RAG) bieten einen vollständigen Lernframework für L4 Agent Design.
- **Wo wir es nutzen**: **das Design-Rückgrat des L4 Autonomous Agent Kurses** — [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) §2 erklärt die sieben Prinzipien. **Grenze**: der Kurs **nimmt nur Konzepte und Design-Patterns — keine Source-Code-Reproduktion, kein Fork**.

#### 🎯 [`HKUDS/ClawTeam`](https://github.com/HKUDS/ClawTeam) (HKUDS, MIT)

- **Was es ist**: Open-Source **Multi-Agent Collaboration Framework** vom HKU Data Science Lab (HKUDS). Fünf-Schichten-Architektur (Team / Workspace / Task / Inbox / Transport), git worktree für isolierte Agent-Workspaces; CLI-driven; drei Reference-Szenarien.
- **Warum wir es schätzen**: pusht „Multi-Agent Team Collaboration" von Demo-Skala zu „**Real-Workflow auditable Collaboration**" — jeder Agent hat eigenen Worktree, eigene Inbox, eigenes Transport. Kein chat-style Toy-Demo, sondern näher an realer Organisations-Arbeitsteilung. Akademischer Hintergrund (HKUDS) + MIT-Lizenz.
- **Wo wir es nutzen**: **die Implementierungsplattform für L5 Multi-Agent Organization** — [`../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md`](../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md) vollständiger Kursplan; Manufacturing QA Team Walkthrough in [`../04_Scenarios/CLAWTEAM_WALKTHROUGH.md`](../04_Scenarios/CLAWTEAM_WALKTHROUGH.md).
- **Vollständige Zitation**: [`CLAWTEAM_REFERENCE.md`](CLAWTEAM_REFERENCE.md)

### 2.2 Consulting Framework Klasse (beeinflusst 03_Consulting_Report)

#### 🎯 [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant) (MIT)

- **Was es ist**: programmatische Organisation klassischer Consulting-Analyseframeworks (MECE, Pyramid Principle, Issue Tree, Porter's 5 Forces, SWOT, BCG Matrix, 5 Whys, Fishbone, Business Model Canvas, WBS/RACI, NPV/IRR, Lean/Six Sigma usw. — 50+ Frameworks)
- **Warum wir es schätzen**: verwandelt verstreute Consulting-Frameworks in eine **strukturierte, zitierbare, komponierbare Bibliothek** — keine weitere PPT-Sammlung
- **Wo wir es nutzen**: [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) — adaptiert in 7 Kategorien + Framework-Selector + Mapping auf 8 Stufen
- **Vollständige Zitation**: [`CONSULTANT_FRAMEWORKS_REFERENCE.md`](CONSULTANT_FRAMEWORKS_REFERENCE.md)

#### 🎯 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills) (MIT)

- **Was es ist**: verwandelt das „**Problem → Report / Deck**"-Production-Craft von Top-Consultants wie McKinsey in einen ausführbaren 8-Schritt-Workflow
- **Warum wir es schätzen**: der erste, der das ganze „Dummy Page → Dependency Management → 7 Page Layouts → Progressive Disclosure → Troubleshooting"-Set in eine lehrbare SOP geschrieben hat — anstatt „implizites Handwerk, das nur Senior-Berater haben"
- **Wo wir es nutzen**: [`../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) — adaptiert in 8-Schritt-Consulting-Report-Workflow + §9 Troubleshooting Playbook
- **Vollständige Zitation**: [`MCKINSEY_SKILLS_REFERENCE.md`](MCKINSEY_SKILLS_REFERENCE.md)

#### 🎯 **Mirza Iqbal ([next8n.com](https://next8n.com)) — Workflow Delivery Framework** (MIT)

- **Was es ist**: die **operationelle SOP** für n8n-Delivery-Consultancy — der vollständige Discovery → Sprint → Handover Lifecycle, Preistabellen, Kundenkommunikations-Vorlagen
- **Warum wir es schätzen**: einer der wenigen, die die **operationelle SOP für Delivery-Arbeit** (nicht nur technische SOP) Open-Source gemacht haben — füllt die operationelle Seite, über die die Consulting-Industrie selten spricht
- **Wo wir es nutzen**: [`../06_Delivery/`](../06_Delivery/) — Engagement Lifecycle, Role SOPs, Business Document Templates sind alle davon inspiriert
- **Vollständige Zitation**: [`WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)
- **Bezogen via**: <https://github.com/MorrisLu-Taipei/AI-Workflow-Delivery-Framework> (README schreibt Mirza Iqbal als Originalautor)

### 2.3 Agent & Skill Klasse (beeinflusst 02_Course_Design)

#### 🎯 [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) (MIT)

- **Was es ist**: 12-Divisions-Agent-Persona-Bibliothek (Marketing, Sales, Customer Service, HR, Finance, R&D usw.) — sofort nutzbar
- **Warum wir es schätzen**: macht „Agent-Persona-Design" zu einer wiederverwendbaren Bibliothek, spart Teams das Schreiben von System-Prompts von Grund auf
- **Wo wir es nutzen**: [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6 „bestehende Agent-Bibliothek nutzen" Modul
- **Vollständige Zitation**: [`AGENCY_AGENTS_REFERENCE.md`](AGENCY_AGENTS_REFERENCE.md)

#### 🎯 [`MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack) (gemischte Lizenz)

- **Was es ist**: n8n Skill Drei-Schichten-Struktur (Workflow Library + Cookbook + DSL Spec), mit AI-generiertem Workflow Skill Pack
- **Warum es hier steht**: dies ist das eigene Projekt des Methodik-Autors Morris Lu, wird aber hier gelistet, um die **Zitations-Disziplin zu demonstrieren** — auch für eigene Projekte sind Lizenz und Drittquellen (`_vendor/` MIT) im selben Standard dokumentiert
- **Wo wir es nutzen**: [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) zweite Hälfte
- **Vollständige Zitation**: [`N8N_SKILL_PACK_REFERENCE.md`](N8N_SKILL_PACK_REFERENCE.md)

### 2.4 Case-Index Klasse (beeinflusst 04_Scenarios)

#### 🎯 [`Shubhamsaboo/awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps) (Apache-2.0)

- **Was es ist**: eine kuratierte Liste von 150+ realen LLM-Anwendungs-Cases (Agent / RAG / Fine-Tuning / Multimodal usw.), community-maintained
- **Warum wir es schätzen**: hohe Kurationsqualität, klare Taxonomie, kontinuierlich aktualisiert; die schnellste Referenz, wenn ein Berater dem Kunden sagt „**so machen es andere mit diesem Szenario**"
- **Wo wir es nutzen**: [`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index — gemappt auf Dual-Axis-Index (L1-L5 × Enterprise-Abteilung); **das Mapping ist von uns**, die ursprüngliche Case-Liste ist Copyright von Shubham Saboo und Community-Beitragenden
- **Vollständige Zitation**: [`AWESOME_LLM_APPS_REFERENCE.md`](AWESOME_LLM_APPS_REFERENCE.md)

#### 🎯 [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) (MIT)

- **Was es ist**: 93+ AI-Engineering-Lehrprojekte (ausführbare Implementierungen von RAG bis Multi-Agent)
- **Warum wir es schätzen**: jedes Projekt kommt mit **Code + Lehrvideo**, Lernende können direkt loslegen; ergänzt awesome-llm-apps' „kuratierte Cases" mit der „Hands-on-Implementierung"-Seite
- **Wo wir es nutzen**: [`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index zweite Quelle — gemappt auf L2-L4 Kurs-ausführbare Demos
- **Vollständige Zitation**: [`AI_ENGINEERING_HUB_REFERENCE.md`](AI_ENGINEERING_HUB_REFERENCE.md)

---

## 3. Original-Referenzmaterial & Diagramme (selbst-gemacht oder Public Domain)

| Datei | Zweck |
| --- | --- |
| [`@AI-MD-PUBIC.pdf`](@AI-MD-PUBIC.pdf) | AI Transformation Maturity Model Public-Version-Handbuch (der originale PDF-Methodik-Entwurf) |
| [`MD-Map.png`](MD-Map.png) | AI Maturity Map, im Root-README verwendet |
| [`Metholodgy.png`](Metholodgy.png) | Enterprise Consulting Eight-Stage Transformation Guide, im Root-README verwendet |

## 4. Akademische Grundlage & Failure Patterns (vollständig original, von Tiger AI + drei AI-Engines geschrieben)

| Datei | Zweck |
| --- | --- |
| [`FAILURE_PATTERNS.md`](FAILURE_PATTERNS.md) | 14 Failure Patterns (theorie-prädiziert + reale Cases + entsprechende Fixes) |
| [`AI_GOVERNANCE_ALIGNMENT.md`](AI_GOVERNANCE_ALIGNMENT.md) | Alignment mit NIST AI RMF / EU AI Act / ISO 42001 |
| [`PILOT_STUDY_PROTOCOL.md`](PILOT_STUDY_PROTOCOL.md) | 18-24 Monate empirisches Forschungsdesign (Pilot Study) |

Die akademische Theorie selbst (die 7 Säulen) ist in [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md).

## 5. Video-Lernnotizen (abgeleitete Notizen; Original-Video-Copyright gehört den Erstellern)

| Datei | Zweck |
| --- | --- |
| [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md) | Lernnotizen aus der OpenWebUI Public Playlist, gemappt auf L1-Kursanwendung |
| [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md) | Lernnotizen vom TigerAI Channel, fokussiert auf n8n / L3-Kursanwendung |

---

## 6. Zitations-Disziplin (die eisernen Regeln für zukünftige Beitragende)

Um irgendein Drittanbieter-Material in diesem Repo zu zitieren, **folgen alle diesen „Approach A"-Prinzipien**:

| # | Prinzip | Wie |
|---|---|---|
| 1 | **Unabhängig adaptieren — nicht forken, keinen Source-Code reproduzieren** | Struktur und Konzepte referenzieren, dann in der Stimme dieser Methodik neu schreiben |
| 2 | **Explizite Attribution, doppelt vermerkt** | (a) Header-Note in der Datei, die zitiert; (b) standalone `*_REFERENCE.md` in diesem Verzeichnis |
| 3 | **Generalisieren auf das Methodik-Szenario** | Domänenspezifischen Inhalt in den L1-L5 KI-Transformations-Consulting-Kontext umwandeln |
| 4 | **Keine Lizenz = keine Integration** | Drittanbieter-Projekte ohne LICENSE werden nicht integriert (nur als externe Beispiel-URLs zitiert) |
| 5 | **Großzügige Anerkennung** | In der Zitationsdatei **explizit sagen, was daran gut ist**, nicht nur „siehe Quelle unten" |
| 6 | **Ehrlich über Failure** | Wenn ein zitiertes Tool sich als ungeeignet erweist, ehrlich in `FAILURE_PATTERNS.md` schreiben — nicht nur Erfolgsgeschichten |

**Nutzungslogik**: um „was wurde von Datei X in Verzeichnis Y zitiert" zu finden → den Header dieser Datei lesen → zur entsprechenden `*_REFERENCE.md` in diesem Verzeichnis springen für die vollständige Lizenznote.

---

## 7. Cross-Directory-Mapping

| Verzeichnis | Beziehung zu diesem Verzeichnis |
| --- | --- |
| [`../00_Overview/`](../00_Overview/) | Die Methodik-Diagramme (Metholodgy.png / MD-Map.png) kommen von hier; die Diskussion der 7 theoretischen Säulen lebt in `00` |
| [`../02_Course_Design/`](../02_Course_Design/) | Drittanbieter-Zitate für L1/L2/L3/L5-Kurse (OpenWebUI-Notizen, agency-agents, n8n-Skill-Pack, ClawTeam) |
| [`../03_Consulting_Report/`](../03_Consulting_Report/) | Drittanbieter-Zitate für Framework-Bibliothek und Report-Workflow (consultant, mckinsey-skills) |
| [`../04_Scenarios/`](../04_Scenarios/) | Drittanbieter-Zitate für LLM-Application-Case-Index (awesome-llm-apps, ai-engineering-hub) |
| [`../06_Delivery/`](../06_Delivery/) | Drittanbieter-Zitat für die Delivery-Operations-Schicht (Mirza Iqbal Framework) |
| [`../07_AI_Contributions/`](../07_AI_Contributions/) | Die drei AI-Engines selbst sind auch „Acknowledgment-Subjekte" — Antigravity / Codex CLI / Claude Code |

---

## 8. Häufige Nutzungsszenarien

- **Wundern, warum eine Datei auf eine bestimmte Weise geschrieben ist**: Datei-Header lesen → zur `*_REFERENCE.md` in diesem Verzeichnis mappen
- **Diese Methodik weitergeben / kommerzialisieren**: §6 Zitations-Disziplin + [`NOTICE`](../NOTICE) Attribution-Anforderungen lesen
- **Neues Open-Source-Projekt onboarden** → die 6 Prinzipien in §6 befolgen: Lizenz bestätigen → unabhängig adaptieren → `*_REFERENCE.md` erstellen → zu dieser README §2 Acknowledgments hinzufügen
- **Upstream-Communities engagieren, interagieren / anerkennen**: auf die GitHub-URL jeder Appreciation Card klicken zum Starren, Folgen, Issue öffnen, PR senden
- **Lernende, die Repo-Inhalt in eigene Papers / Decks zitieren**: gemäß §6, beim Zitieren dieser Methodik die Originalautor-Attribution behalten ([`../NOTICE`](../NOTICE)); beim Zitieren von Drittanbieter-Material das Lernende-Zitations-Format in der entsprechenden `*_REFERENCE.md` befolgen

---

## 9. Acknowledgments

Alle in diesem Verzeichnis gelisteten Upstream-Autoren und Communities **sind die Schultern, auf denen diese Methodik steht**. Jede Fehlinterpretation, unangemessene Zitation oder Abweichung vom Originalziel ist die alleinige Verantwortung des Methodik-Autors **Tiger AI Morris Lu 盧業興** — nicht der Upstream-Autoren oder Communities.

Wenn Sie ein Upstream-Autor sind und fühlen, dass eine Zitation in diesem Repo unangemessen ist, korrigiert werden muss oder verstärkt werden sollte — bitte ein Issue öffnen oder Morris Lu kontaktieren, wir werden es sofort behandeln.

> **Architektur-Eigentum**: Die Methodik-Architektur in diesem Repo wird vom menschlichen Autor **Morris Lu (Tiger AI)** vorgeschlagen. Die drei AI-Engines (Antigravity / Codex / Claude Code) sind Werkzeuge, die **ausführen, vervollständigen, erweitern und auditieren**. Siehe [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0.
