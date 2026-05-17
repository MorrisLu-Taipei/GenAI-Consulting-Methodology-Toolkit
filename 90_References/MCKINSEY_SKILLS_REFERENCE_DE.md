# mckinsey-consultant-skills — Zitations- & Lizenzhinweis

> 🌐 Sprache: [繁體中文](MCKINSEY_SKILLS_REFERENCE.md) ｜ [English](MCKINSEY_SKILLS_REFERENCE_EN.md) ｜ Deutsch ｜ [Français](MCKINSEY_SKILLS_REFERENCE_FR.md) ｜ [Español](MCKINSEY_SKILLS_REFERENCE_ES.md) ｜ [日本語](MCKINSEY_SKILLS_REFERENCE_JA.md) ｜ [한국어](MCKINSEY_SKILLS_REFERENCE_KR.md)

Der Production-Workflow im [`03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) dieser Methodik wird basierend auf **Kafurtan/mckinsey-consultant-skills** referenziert und neu geschrieben. Dieses Dokument hält die Upstream-Quelle, Lizenzbedingungen, Zitations-Leitlinien und Anpassungsumfang fest.

---

## 1. Upstream-Projekt

| Feld | Wert |
| --- | --- |
| **Projekt** | mckinsey-consultant-skills (V3.1) |
| **Maintainer** | @Kafurtan |
| **GitHub URL** | <https://github.com/Kafurtan/mckinsey-consultant-skills> |
| **Lizenz** | **MIT License** |
| **Form** | AI Agent Skill (`SKILL.md` + `references/`) |
| **Inhalt** | Ein 8-Schritt-Workflow, der „Business-Problem → McKinsey-Style-Präsentation" automatisiert, end-to-end in 90-110 Minuten |

## 2. Was mckinsey-consultant-skills ist

Er systematisiert McKinsey's Problem Solving Methodologie in einen **8-Schritt-Workflow**, der einem AI-Assistenten erlaubt, ein Business-Problem in eine professionelle Präsentation (PPT + Excel Evidence Trail) zu verwandeln.

### Strukturelle Features

- **8-Schritt-Workflow**: Grenzen definieren → Issue Tree + Hypothesen → Dummy Pages + Design Specs → seitenweise iterative Produktion → PPT + Excel → optionaler Word-Bericht → iterative Revision.
- **Dummy Page**: vor der Recherche die Wireframe-Spec bauen, um ziellose Datensammlung zu vermeiden und Wiederaufnahme über Konversationen zu unterstützen.
- **Dependency Awareness**: Seiten werden mit Dependency-Status getaggt, was die Produktionsreihenfolge bestimmt (die Executive Summary wird zuletzt gemacht).
- **7 Page Layouts**: Titel + Single Chart / Two-Column / 2×2 Matrix / Tabelle / Waterfall Chart / Timeline / Insight Summary.
- **Excel Evidence Trail**: pro Seite Raw Data + URL + Cleaning Process.
- **Progressive Disclosure**: Reference-Dateien werden nur in den Schritten geladen, die sie brauchen, und danach freigegeben, ~70% Context-Ersparnis.
- `references/`: methodology.md, layouts.md, design-specs.md, examples.md, troubleshooting.md.

## 3. Was wir adaptiert und zitiert haben

| Umfang | Behandlung |
| --- | --- |
| **Der 8-Schritt Production-Workflow** | Workflow referenziert, in der Sprache dieser Methodik neu geschrieben, auf die Acht-Stufen-Consulting-Struktur gemappt |
| **Das Dummy Page Konzept** | „Skeleton-first, fill-in-later"-Disziplin in per-Page-Specs für die Deck-Outlines dieser Methodik adaptiert |
| **Dependency Awareness** | Page-Dependency-Management-Konzept adaptiert |
| **Die 7 Page Layouts** | Layout-Liste referenziert, neu geschrieben, um `VISUAL_ASSETS_SPEC.md` zu erweitern |
| **Excel Evidence Trail, Progressive Disclosure** | Konzepte adaptiert, auf die Evidence-Disziplin dieser Methodik und AI-IDE Context Management gemappt |
| **McKinsey Problem Solving, MECE, Pyramid Principle** | Public-Domain-Management-Wissen, nicht proprietär zu diesem Projekt |
| **Die originalen `SKILL.md` und `references/` Dateien** | **Nicht reproduziert, nicht geforkt**; diese Methodik ist eine unabhängige Neufassung |

## 4. Lizenz-Zusammenfassung

mckinsey-consultant-skills wird unter der **MIT License** veröffentlicht, die freie Nutzung, Modifikation, Weiterverbreitung und kommerzielle Nutzung erlaubt, einschließlich als Teil eines proprietären Produkts; die einzige Bedingung ist die Beibehaltung des MIT Copyright-Hinweises und Lizenztextes beim Weiterverbreiten der Source.

Diese Methodik **verbreitet** seinen Source Code **nicht weiter** — sie hat `REPORT_PRODUCTION_WORKFLOW.md` unabhängig neu geschrieben, nachdem sie den Workflow und die Design Patterns referenziert hat. Die neu geschriebene Datei steht unter Apache 2.0 dieses Repos; nichtsdestotrotz **vermerken wir die Zitationsquelle** in dieser Datei und hier explizit, in Anerkennung des Beitrags des Originalautors.

## 5. Zitationsformat für Lerner

> Production-Workflow adaptiert von mckinsey-consultant-skills von @Kafurtan — <https://github.com/Kafurtan/mckinsey-consultant-skills> (MIT License)

## 6. Disclaimer

Jede Zitation, Anpassung oder Acht-Stufen-Mapping von mckinsey-consultant-skills in dieser Methodik repräsentiert die Interpretation des Methodik-Autors (Morris Lu / Tiger AI 虎智科技) und repräsentiert nicht die offizielle Position von @Kafurtan. „McKinsey" ist eine Marke von McKinsey & Company; diese Methodik hat keine Verbindung oder Befürwortung von McKinsey & Company, und verwandte Methodologie-Namen werden nur als Referenzen zu Public-Domain-Management-Wissen verwendet. Falls der Workflow oder die Struktur von mckinsey-consultant-skills in neueren Versionen ändert, siehe das [Upstream-Repository](https://github.com/Kafurtan/mckinsey-consultant-skills).
