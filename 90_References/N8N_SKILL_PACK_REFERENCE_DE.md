# TigerAI-n8n-Skill-Pack Zitations- & Lizenzhinweis

> 🌐 Sprache: [繁體中文](N8N_SKILL_PACK_REFERENCE.md) ｜ [English](N8N_SKILL_PACK_REFERENCE_EN.md) ｜ Deutsch ｜ [Français](N8N_SKILL_PACK_REFERENCE_FR.md) ｜ [Español](N8N_SKILL_PACK_REFERENCE_ES.md) ｜ [日本語](N8N_SKILL_PACK_REFERENCE_JA.md) ｜ [한국어](N8N_SKILL_PACK_REFERENCE_KR.md)

Die zweite Hälfte des **L3 Workflow Automation**-Kurses in dieser Methodik zitiert **TigerAI-n8n-Skill-Pack** als Lehrplattform für „n8n-Workflows aus natürlicher Sprache mit Antigravity generieren". Dieses Dokument hält die Upstream-Quelle, Lizenzbedingungen, Zitations-Leitlinien und Nutzungsumfang fest.

---

## 1. Upstream-Projekt

| Feld | Wert |
| --- | --- |
| **Projekt** | TigerAI-n8n-Skill-Pack |
| **Maintainer** | Morris Lu (盧業興) — n8n Taipei Ambassador |
| **GitHub URL** | <https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack> |
| **Lizenz** | Gemischt: Skills / Cookbook / Specs sind **TigerAI Proprietary**; `skills/_vendor/` ist **MIT** (von czlonkowski/n8n-skills); `reference-workflows/` ist **MIT** (von Zie619/n8n-workflows, Secrets bereinigt) |
| **Umfang** | 13 Skills (7 Vendor + 6 Custom), 8 Cookbook-Rezepte, 2.061 Reference Workflows, DSL v1.2 Spec, 3 Flagship-Beispiele |
| **Unterstützte Tools** | Antigravity (native agentic Orchestration), Claude Code (CLI / VS Code), n8n (2.10.3+), beliebiger AI-Assistent (via Cookbook Few-Shot Prompting) |

> **Hinweis:** dies ist das eigene Projekt des Methodik-Autors Morris Lu; es gibt kein Drittanbieter-Lizenz-Hindernis zur Zitation, aber die MIT-Quellen unter `_vendor/` und `reference-workflows/` müssen weiterhin ihre Copyright-Hinweise behalten (siehe Upstream `THIRD_PARTY_NOTICES.md`).

## 2. Was ist TigerAI-n8n-Skill-Pack

Es ermöglicht Nutzern, Enterprise-grade n8n-Workflows aus **natürlich-sprachlichen Beschreibungen** zu generieren statt manueller Node-Konfiguration. Das System transformiert „Sticky-Note"-Plain-Language-Intent in komplettes, dokumentiertes Workflow-JSON, bereit für Deployment.

### Drei-Schichten-Struktur

`Gelbe Sticky-Note Intent` + `Blaue Sticky-Note Notizen` + `Workflow Nodes` — der Nutzer schreibt Intent → AI generiert das Drei-Schichten-JSON → Deployment via n8n API.

### Drei Nutzungsmodi

1. **Cookbook Copy** — aus den 8 vorgebauten Recipe-Templates auswählen
2. **Q&A-Modus** — AI führt den Nutzer durch Requirements Gathering
3. **Example Finder** — ähnliche Implementierungen unter den 2.061 Reference Workflows entdecken

### Installation

`bash install.sh` (Unix) oder `install.ps1` (Windows).

## 3. Warum es in die L3 zweite Hälfte gehört

Der L3-Kurs ist nach dem Prinzip „Konzepte zuerst, Generierung danach" in Hälften aufgeteilt:

- **L3 erste Hälfte** (§5.1 Foundation + §5.2 Builder): Lerner **bauen handarbeitlich** Trigger / Node / AI / Human Gate / Error Handling und verstehen Workflow-Struktur und Governance.
- **L3 zweite Hälfte** (§5.5): auf dieser Grundlage Antigravity + TigerAI-n8n-Skill-Pack nutzen, um Workflow-JSON direkt aus natürlich-sprachlichem Intent zu generieren, und lernen, das generierte Ergebnis zu **reviewen**.

> **Kernprinzip: das Skill Pack ist ein Accelerator, kein Ersatz für Verständnis.** Ohne handarbeitlich Workflows in der ersten Hälfte zu bauen, können Lerner nicht beurteilen, ob generierte Ergebnisse korrekt, sicher oder wartbar sind.

Entsprechender Kurs: [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) §1.1, §5.5.

## 4. Lizenz-Zusammenfassung

| Teil | Lizenz | Verpflichtung |
| --- | --- | --- |
| `skills/` (custom), `cookbook/`, `spec/` | TigerAI Proprietary | Lizenziert vom Autor Morris Lu; kein Hindernis zur Nutzung innerhalb dieser Methodik; Zustimmung des Autors für externe Weiterverbreitung einholen |
| `skills/_vendor/` | MIT (czlonkowski/n8n-skills) | MIT Copyright-Hinweis beibehalten |
| `reference-workflows/` | MIT (Zie619/n8n-workflows) | MIT Copyright-Hinweis beibehalten; Secrets sind bereinigt, aber selbst verifizieren |

> ⚠️ **Wichtig**
> Dieses Repo verbreitet TigerAI-n8n-Skill-Pack-Source **nicht weiter**. Wir **zitieren und lehren** seine Struktur und Nutzung nur im L3-Kurs und weisen Lerner an, **upstream selbst zu installieren**. Workflows, die Lerner mit dem Skill Pack generieren, gehören dem Unternehmen.

## 5. Umfang der Zitation

| Umfang | Behandlung |
| --- | --- |
| **Als Lehrplattform** | Die primäre Implementierungsplattform für die L3 zweite Hälfte (§5.5) |
| **Source / Skills** | **Nicht reproduziert, nicht geforkt**; Lerner installieren selbst via `install.sh` / `install.ps1` |
| **reference-workflows** | Zitiert für die „Example Finder"-Lektion; Lerner müssen bestätigen, dass keine residualen Secrets / internen Endpoints vorhanden sind |
| **Generierter Output** | Generierte Workflow-JSON ist ein Enterprise-Asset; muss Gates 3A-3G passieren, um als Enterprise-grade PoC zu zählen |

## 6. Zitationsformat für Lerner

> Built with TigerAI-n8n-Skill-Pack by Morris Lu — <https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack>

## 7. Disclaimer

TigerAI-n8n-Skill-Pack ist das eigene Projekt des Methodik-Autors Morris Lu. Falls seine Skills, Cookbook, DSL Spec oder Installation in neueren Versionen ändert, siehe das [Upstream-Repository](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack) und seine `THIRD_PARTY_NOTICES.md`. AI-generierte Workflows müssen immer Human Review und Gate 3 Acceptance durchlaufen — Generierung ist nicht Acceptance.
