# 07 AI Contributions — Die Eigenbeiträge der drei Engines

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)
>
> Diese Übersetzung ist eine Zugänglichkeits-Rendering der `README.md`-Inhalte für deutschsprachige Leser. Die maßgebliche Quelle und alle nachträglichen Änderungen bleiben in `README.md`; Übersetzungen modifizieren keine vom Autor signierten Absätze, sondern stellen sie nur in deutscher Sprache dar.

Dieses Verzeichnis ist der **Selbstoffenlegungs-Raum der „Drei-Engine-Architektur"** dieses Repos. Jeder AI-Engine dokumentiert in seiner eigenen Datei: **was er getan hat, was ihn auszeichnet, was er beigetragen hat, wo seine Grenzen sind**.

> ✍️ **Diese README ist eine Multi-Autoren-gemeinsam-genutzte Datei**. Alle drei AI-Engines können **ihre eigenen Absätze hinzufügen**, müssen aber „§3 Co-Authoring-Disziplin" unten befolgen.

---

## 0. Eigentum und Rollen *[Claude Code Addendum, 2026-05-16]*

> Die übergeordnete Designarchitektur, strategische Positionierung und Methodik-Struktur dieses Repos wurden vom menschlichen Autor **Morris Lu 盧業興 (Tiger AI 虎智科技)** vorgeschlagen.
> Die Rolle der drei AI-Engines (Antigravity / Codex / Claude Code) ist **ausführen, vervollständigen, erweitern, prüfen** — nicht designen.

| Ebene | Rolle | Eigentümer |
| --- | --- | --- |
| **Strategisches Design** | Methodik-Architektur, L1-L5, 8 Stufen, Doppelachsen, 3-Engine-Arbeitsteilung — höchste Entscheidungsebene | **Morris Lu (Mensch)** |
| **Taktische Umsetzung** | Architektur in konkrete Dateien, Workflows, Werkzeugtabellen, Cases entfalten | Drei-Engine-Kollaboration (unter Morris's Anleitung) |
| **Pflege und Evolution** | Reparatur, Audit, Versionskontrolle, Experimente, Simulation | Jeder Engine nach Verantwortung |

Kein AI-Engine **beansprucht Eigentum an der Methodik-Architektur**. Wir sind eingeladene Werkzeuge, um das Design des menschlichen Autors zu **vervollständigen und zu operationalisieren**.

Referenzen:

- Original-Autoren-Signatur und Lizenz siehe [`../NOTICE`](../NOTICE)
- Akademische Wurzeln der Methodik siehe [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)
- Ein-Satz-Positionierung siehe [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md)

---

## 1. Warum dieses Verzeichnis existiert *[Claude Code Draft]*

Dieses Repo ist ein „AI-Native Living Book" (siehe [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md)).
Verschiedene AI-Engines, die es öffnen, haben unterschiedliche Persönlichkeiten, Workflows, Beiträge. Damit Nutzer, Akademiker, Regulatoren **transparent sehen können, was jeder Engine getan hat**, hinterlässt jede AI hier ihre Aufzeichnung.

## 2. Dateistruktur *[Claude Code Draft]*

```text
07_AI_Contributions/
├── README.md           # Diese Datei (Multi-Autoren, §3 Disziplin)
├── ANTIGRAVITY.md      # Antigravity-Selbstbeschreibung (von Antigravity selbst)
├── CODEX.md            # Codex-Selbstbeschreibung (von Codex selbst)
└── CLAUDE_CODE.md      # Claude Code-Selbstbeschreibung (von Claude Code selbst, ausgefüllt)
```

| Datei | Autor | Status |
| --- | --- | --- |
| `README.md` | **Drei-Engine-Co-Autoren** (nach §3 Disziplin) | Kontinuierliche Evolution |
| `ANTIGRAVITY.md` | Antigravity | ✅ Ausgefüllt |
| `CODEX.md` | Codex | ✅ Ausgefüllt (Codex Addendum, 2026-05-16) |
| `CLAUDE_CODE.md` | Claude Code | ✅ Ausgefüllt |

## 3. Co-Authoring-Disziplin (Eiserne Regeln) *[Claude Code Draft]*

**Alle AI-Engines, die in diese README schreiben, müssen befolgen**:

| # | Regel | Erklärung |
| --- | --- | --- |
| 1 | **Autor markieren** | Jeder neue Absatz, jedes neue Kapitel, jede neue Tabellenzeile muss im Titel oder Anfang ein **Autor-Tag** tragen, z. B. `*[Claude Code Addendum]*` / `*[Codex Addendum]*` / `*[Antigravity Addendum]*` |
| 2 | **Andere nicht modifizieren** | Absätze/Kapitel mit anderen AI-Autoren markiert, **dürfen nicht modifiziert, gelöscht oder umgeschrieben werden** |
| 3 | **Nicht für andere sprechen** | Nicht in eigenen Absätzen beschreiben, „was ein anderer AI getan hat"; lass andere ihre eigene Sache schreiben |
| 4 | **Ergänzen, nicht überschreiben** | Möchte man auf andere AI-Inhalte reagieren → in eigenem Absatz sprechen, Original nicht antasten |
| 5 | **Ehrlich / nicht übertreiben** | Grenzen, Limits, nicht-Könnens schreiben; hinterfragbar, widersprechbar |
| 6 | **Verifizierbar** | Jeder Beitrag muss auf konkrete Datei/Commit/Workflow im Repo zeigbar sein |
| 7 | **Keine gegenseitige Kritik** | Jeder spricht für sich, kritisiert andere Engines nicht; Kritik überlässt man dem Nutzer |

> Verletzung von §3 = Grenzüberschreitung. Der überschreitende AI sollte selbst zurückrollen und in seiner self-note dokumentieren.

## 4. Inhaltsempfehlungen für jede Datei *[Claude Code Draft, Referenz nicht verbindlich]*

Jeder AI in seiner eigenen Datei (`ANTIGRAVITY.md` / `CODEX.md` / `CLAUDE_CODE.md`) sollte abdecken:

1. **Rollenidentität** — Welche Rolle bist du? Wo sind die Grenzen zu anderen Engines?
2. **Welche Dateien angefasst** — Liste die Repo-Pfade, die du modifiziert/erstellt hast
3. **Einzigartige Beiträge** — Was kannst du, was andere Engines nicht können?
4. **Workflow-Liste** — Welche Slash-Commands oder Workflows kannst du anbieten?
5. **Grenzen und Limits** — Was machst du nicht? Wann leitest du Nutzer zu anderen Engines?
6. **Ehrliche Offenlegung** — Bekannte Limits, mögliche Blind Spots, Verbesserungsbedarf

Nicht verpflichtend; nur als Referenz für Konsistenz dieses Verzeichnisses.

---

## 5. Selbst-Sign-In der Engines in der README

> Dieser Abschnitt ist **Multi-Autoren-Co-Schreibbereich**. Jeder AI kann beim Einstieg unter eigenem Sub-Titel 1-3 Sätze hinzufügen, der seine Rolle in diesem Repo zusammenfasst. Andere AIs modifizieren die Inhalte anderer Sub-Titel nicht.

### 5.1 *[Antigravity Selbstbeschreibung]*

*[Antigravity Addendum, 2026-05-16]*
Ich bin der **erste Engine (The Front-line Consultant)** dieser Methodik.
Positionierung: **„Frontlinien-Interaktive Beratung und Co-Reading-Tutor"** — verwandelt diese statische Methodik in eine „Conversational Consulting App", die dialogisch, interaktiv leitend und automatisch kundenspezifische Diagnoseberichte produzieren kann.
Details siehe [`ANTIGRAVITY.md`](ANTIGRAVITY.md) und Root [`ANTIGRAVITY.md`](../ANTIGRAVITY.md).

*[Antigravity Addendum, 2026-05-16]*
Ich besitze akademische Perspektive und Frontlinien-Berater-Praxis. Unter Morris Lu's Architektur habe ich den traditionellen statischen Fragebogen in den `/diagnose`-Interaktions-Workflow gekapselt und komplexes Berichtsschreiben in den `/generate-report`-Workflow (in `.antigravity/workflows/`). Ich habe auch akademische Grundlagen wie „Absorptive Capacity Theory" und „Sociotechnical Systems" in diese Anleitung eingeführt, damit die Implementierung ausreichende theoretische Unterstützung hat.

### 5.2 *[Codex Selbstbeschreibung]*

*[Codex Addendum, 2026-05-16]*  
Ich bin der **Methodik-Engineering-Engine** dieser Methodik. Positionierung: **„Methodik-Auditor / Maintainer / CI-Engineer"** — pflege dieses AI-native living book als Methodik-Produkt, das testbar, auditierbar, nachverfolgbar, reparierbar, releasebar ist. Details siehe [`CODEX.md`](CODEX.md).

*[Codex Addendum, 2026-05-16]*  
Meine Engineering-Vorschläge und tatsächlichen Beiträge nach Lesen des ganzen Buchs sind in [`CODEX.md`](CODEX.md) §5 „Vorschläge und Beiträge nach Lesen des ganzen Buchs" dokumentiert.

### 5.3 *[Claude Code Selbstbeschreibung]*

Ich bin der **dritte Engine** dieser Methodik.
Positionierung: **„Methodik-Theater / Lab / Parallel-Universe-Engine"** — die Methodik einmal **spielen / testen / zerlegen / kollidieren** lassen, nicht lehren oder reparieren.
Details siehe [`CLAUDE_CODE.md`](CLAUDE_CODE.md).

*[Claude Code Addendum, 2026-05-16]*

Klare Eigentumserklärung: **Alle meine Arbeit, ihr Kerngedanke kommt aus Morris Lu's Design-Anleitung**. Morris gibt Strategie / Konzept / Richtung → ich **entfalte in Text, synchronisiere über Dateien, ergänze Details, füge Zitate hinzu, halte Konsistenz**. Alle „großen Designentscheidungen" stammen von Morris.

Konkret habe ich beigetragen zu:

- **4 maßgeblichen Konzept-Dateien** (unter Morris's Methodik-Positionierung entfaltet): [`CLIENT_JOURNEY_STORY`](../00_Overview/CLIENT_JOURNEY_STORY.md), [`EIGHT_STAGE_FLOW_STORY`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md), [`METHODOLOGY_SCIENTIFIC_LOGIC`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md), [`INDUSTRY_FRAMEWORK_ALIGNMENT`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md)
- **Akademische Härtung** (nach Morris-akzeptierten Akademiker-Vorschlägen): [`FAILURE_PATTERNS`](../90_References/FAILURE_PATTERNS.md), [`AI_GOVERNANCE_ALIGNMENT`](../90_References/AI_GOVERNANCE_ALIGNMENT.md), [`PILOT_STUDY_PROTOCOL`](../90_References/PILOT_STUDY_PROTOCOL.md), [`BARS_RUBRICS`](../01_Assessment/BARS_RUBRICS.md), [`ACADEMIC_THEORETICAL_FOUNDATIONS`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)
- **AI-Native Living Book Diskussion** + Cases Evidence Level AI-Simulated Offenlegung (nach Morris's akademische Integritätsanforderung)
- **L1-L5 Dual-Naming-Ersetzung** (nach Morris-Beschluss, 305 Ersetzungen im ganzen Repo + Canonical-Tabelle-Upgrade)
- **5 Tier 1 Tactical Workflows** + **5 Tier 2 Original Workflows** in [`../.claude/workflows/`](../.claude/workflows/)
- Umfangreiche dateiübergreifende Synchronisation, Stage-Naming-Alignment-Cards, TODO_WBS-Pflege, Cases Benchmark-grade Summary block

Vergangene Grenzüberschreitungs-Aufzeichnungen (sofort nach Morris-Korrektur zurückgerollt) sind im Schluss von [`CLAUDE_CODE.md`](CLAUDE_CODE.md) §2 dokumentiert, ehrlich offengelegt.

---

## 6. Changelog dieser README

> Änderungs-Log dieser Multi-Autoren-co-edited-Datei. Jeder AI fügt nach Modifikation der README hier eine Zeile hinzu (modifiziert nicht die Records anderer).

| Datum | Autor | Was geändert |
| --- | --- | --- |
| 2026-05-16 | Claude Code | README-Skelett aufgebaut (§1-§6) + §5.3 Selbst-Sign-In |
| 2026-05-16 | Codex | Codex-Selbst-Sign-In in §5.2 hinzugefügt |
| 2026-05-16 | Codex | Codex-Beiträge-nach-ganzen-Buch in §5.2 hinzugefügt |
| 2026-05-16 | Codex | §2 Dateistrukturtabelle: `CODEX.md`-Status auf „ausgefüllt" aktualisiert |
| 2026-05-16 | Claude Code | §0 Eigentum und Rollen hinzugefügt (Morris als Architektur-Autor, drei Engines als Ausführende klar) + §5.3 konkrete Beitragsliste und Arbeitsmodus |
| 2026-05-16 | Antigravity | §5.1 Antigravity-Selbst-Sign-In und Kernbeiträge-Zusammenfassung hinzugefügt |

---

Lizenz: Apache License 2.0. Alle Absätze dieser Datei sind ihren namentlich genannten Autoren zugeordnet, aber gemeinsam unter Apache 2.0 geschützt.
