# agency-agents Zitations- & Lizenzhinweis

> 🌐 Sprache: [繁體中文](AGENCY_AGENTS_REFERENCE.md) ｜ [English](AGENCY_AGENTS_REFERENCE_EN.md) ｜ Deutsch ｜ [Français](AGENCY_AGENTS_REFERENCE_FR.md) ｜ [Español](AGENCY_AGENTS_REFERENCE_ES.md) ｜ [日本語](AGENCY_AGENTS_REFERENCE_JA.md) ｜ [한국어](AGENCY_AGENTS_REFERENCE_KR.md)

Die zweite Hälfte des **L2 Knowledge Codification**-Kurses in dieser Methodik (speziell der L2-B Agentic Developer Track) zitiert **agency-agents** als Lehrmaterial für das Modul „vorgefertigte Agent-Persona-Bibliothek". Dieses Dokument hält die Upstream-Quelle, Lizenzbedingungen, Zitations-Leitlinien und Nutzungsumfang fest.

---

## 1. Upstream-Projekt

| Feld | Wert |
| --- | --- |
| **Projekt** | agency-agents |
| **Maintainer** | @msitarzewski (community-maintained) |
| **GitHub URL** | <https://github.com/msitarzewski/agency-agents> |
| **Lizenz** | **MIT License** |
| **Umfang** | 144+ Agent-Personas über 12 Divisionen |
| **Unterstützte Tools** | Claude Code, GitHub Copilot, Cursor, Aider, Windsurf, OpenCode, Antigravity, Gemini CLI, OpenClaw, Qwen Code, Kimi Code |

## 2. Was ist agency-agents

agency-agents ist eine **Sammlung von AI Agent Persona-Definitionen**: jeder Agent ist eine Markdown-Datei mit Identitätsmerkmalen, Kernmission, technischen Spezifikationen, Workflow-Prozessen und messbaren Erfolgskriterien. Es ist kein Set generischer Prompt-Templates, sondern eine Liste „deploybarer virtueller Spezialisten".

### 12 Divisionen

`engineering` (25+ Agents: Frontend Developer, Backend Architect, Security Engineer…), `design`, `marketing`, `sales`, `product`, `project-management`, `testing`, `support`, `finance`, `game-development`, `academic`, `specialized`, `spatial-computing`.

### Installation

Installiert via `./scripts/install.sh`, das installierte AI-Tools auto-erkennt und parallel verarbeitet.

## 3. Warum es in L2 gehört

Der Kern von L2 Knowledge Codification ist „Arbeitserfahrung in wiederverwendbare Skills verpacken". Die zweite Hälfte des L2-B Agentic Developer Tracks lehrt eine Schlüsselidee: **nicht jeder Skill muss von Grund auf gebaut werden.** agency-agents bietet 144+ reife Agent-Personas als Startpunkt — Lerner wählen, anpassen und integrieren sie in die Enterprise Skill Library, anstatt das Rad neu zu erfinden.

Entsprechender Kurs: [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6.

## 4. Lizenz-Zusammenfassung

agency-agents wird unter der **MIT License** veröffentlicht. MIT erlaubt freie Nutzung, Modifikation, Weiterverbreitung und kommerzielle Nutzung, einschließlich als Teil eines proprietären Produkts; **die einzige Bedingung** ist, dass die Weiterverbreitung den originalen MIT Copyright-Hinweis und Lizenztext beibehalten muss. MIT erfordert nicht strikt sichtbare Attribution für Endnutzer (obwohl der Autor anmerkt, dass sie geschätzt wird).

> ⚠️ **Wichtig**
> Dieses Repo verbreitet agency-agents-Source **nicht weiter**. Wir **zitieren und lehren** seine Struktur und Nutzung nur im L2-Kurs und weisen Lerner an, **upstream selbst zu installieren**. Von Lernern angepasste Agent-Personas gehören dem Unternehmen, aber es wird empfohlen, die Originalquelle (agency-agents + Version) in der Skill-Dokumentation zu vermerken.

## 5. Umfang der Zitation

| Umfang | Behandlung |
| --- | --- |
| **Als Lehrmaterial** | Verwendet als „vorgefertigte Agent-Library"-Case in der zweiten Hälfte von L2-B; lehrt Installieren, Browsen, Auswählen, Anpassen |
| **Source / Persona-Dateien** | **Nicht reproduziert, nicht geforkt**; Lerner installieren selbst via `./scripts/install.sh` |
| **Angepasster Output** | Angepasste Personas werden Enterprise Skill Library-Einträge; Source-Attribution empfohlen |

## 6. Zitationsformat für Lerner

> Basierend auf agency-agents von @msitarzewski — <https://github.com/msitarzewski/agency-agents> (MIT License)

## 7. Disclaimer

Jede Beschreibung, Anwendung oder Anpassungsanleitung für agency-agents in dieser Methodik repräsentiert die Interpretation des Methodik-Autors (Morris Lu / Tiger AI 虎智科技) und repräsentiert nicht die offizielle Position von @msitarzewski oder der agency-agents-Community. Falls agency-agents' Struktur, Installation oder Agent-Taxonomie in neueren Versionen ändert, siehe das [Upstream-Repository](https://github.com/msitarzewski/agency-agents).
