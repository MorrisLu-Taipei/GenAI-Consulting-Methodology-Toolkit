# consultant Frameworks — Zitations- & Lizenzhinweis

> 🌐 Sprache: [繁體中文](CONSULTANT_FRAMEWORKS_REFERENCE.md) ｜ [English](CONSULTANT_FRAMEWORKS_REFERENCE_EN.md) ｜ Deutsch ｜ [Français](CONSULTANT_FRAMEWORKS_REFERENCE_FR.md) ｜ [Español](CONSULTANT_FRAMEWORKS_REFERENCE_ES.md) ｜ [日本語](CONSULTANT_FRAMEWORKS_REFERENCE_JA.md) ｜ [한국어](CONSULTANT_FRAMEWORKS_REFERENCE_KR.md)

Die Framework-Liste und Taxonomie im [`03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) dieser Methodik werden basierend auf **yoichiojima-2/consultant** referenziert und neu geschrieben. Dieses Dokument hält die Upstream-Quelle, Lizenzbedingungen, Zitations-Leitlinien und Anpassungsumfang fest.

---

## 1. Upstream-Projekt

| Feld | Wert |
| --- | --- |
| **Projekt** | consultant |
| **Maintainer** | @yoichiojima-2 |
| **GitHub URL** | <https://github.com/yoichiojima-2/consultant> |
| **Lizenz** | **MIT License** |
| **Form** | Claude Code Plugin (installiert via `/plugin marketplace add`) |
| **Inhalt** | 50+ klassische Consulting-Frameworks (McKinsey / BCG / Bain / Accenture) über 7 Kategorien, verpackt als Markdown-Skill |

## 2. Was consultant ist

consultant ist ein **Claude Code Plugin**, das 50+ klassische Management-Consulting-Frameworks (MECE, Pyramid Principle, Porter's 5 Forces, SWOT, BCG Matrix, PESTEL, 5 Whys, Fishbone, Business Model Canvas, WBS, RACI, Kotter, OKR, NPV/IRR, Lean, Six Sigma usw.) in einen Markdown-Skill verpackt.

### Strukturelle Features

- **7-Kategorien-Taxonomie**: problem solving / strategy analysis / case frameworks / business design / project & change / financial analysis / operations.
- **Trigger Recognition**: routet natürliche „Ich brauche…"-Sätze zu einer Framework-Kombination.
- **Framework-Kombinationen**: vorgebaute Multi-Framework-Chains (z.B. PESTEL → 5 Forces → 3C → SWOT → Issue Tree).
- **Standardstruktur pro Framework**: Ursprung / Kernkonzept / Schritte / wie anwenden / reales Beispiel / häufige Fallstricke.

## 3. Was wir adaptiert und zitiert haben

| Umfang | Behandlung |
| --- | --- |
| **Framework-Liste und 7-Kategorien-Taxonomie** | Taxonomie referenziert, in der Sprache dieser Methodik neu geschrieben |
| **Das „Framework Selector"-Konzept** (natürliche Sprache → Framework) | Trigger-Recognition-Pattern in einen Selector adaptiert, der mit den Szenarien dieser Methodik abgestimmt ist |
| **Das „Framework Combination Chains"-Konzept** | Combination-Chains-Pattern adaptiert, auf die acht Stufen dieser Methodik gemappt |
| **Per-Framework Expansion-Format** | Per-Framework-Struktur referenziert, eine „maps-to-stage"-Spalte hinzugefügt |
| **Die klassischen Frameworks selbst** (MECE, Porter's 5 Forces usw.) | Public-Domain-Management-Wissen, nicht proprietär zu consultant |
| **Die originalen Markdown-Skill-Dateien** | **Nicht reproduziert, nicht geforkt**; diese Methodik ist eine unabhängige Neufassung |

## 4. Lizenz-Zusammenfassung

consultant wird unter der **MIT License** veröffentlicht, die freie Nutzung, Modifikation, Weiterverbreitung und kommerzielle Nutzung erlaubt, einschließlich als Teil eines proprietären Produkts; die einzige Bedingung ist die Beibehaltung des MIT Copyright-Hinweises und Lizenztextes beim Weiterverbreiten der Source.

Diese Methodik **verbreitet** den Source Code von consultant **nicht weiter** — sie hat `CONSULTING_FRAMEWORKS_LIBRARY.md` unabhängig neu geschrieben, nachdem sie die Framework-Liste und Design-Patterns von consultant referenziert hat. Die neu geschriebene Datei steht unter Apache 2.0 dieses Repos; nichtsdestotrotz **vermerken wir die Zitationsquelle** in dieser Datei und hier explizit, in Anerkennung des Beitrags des Originalautors.

## 5. Zitationsformat für Lerner

> Framework-Bibliothek adaptiert von consultant von @yoichiojima-2 — <https://github.com/yoichiojima-2/consultant> (MIT License)

## 6. Disclaimer

Jede Zitation, Anpassung oder Acht-Stufen-Mapping von consultant in dieser Methodik repräsentiert die Interpretation des Methodik-Autors (Morris Lu / Tiger AI 虎智科技) und repräsentiert nicht die offizielle Position von @yoichiojima-2. Für die Definitionen und Anwendung klassischer Consulting-Frameworks siehe die originale akademische / industrielle Quelle jedes Frameworks. Falls die Framework-Liste oder Struktur von consultant in neueren Versionen ändert, siehe das [Upstream-Repository](https://github.com/yoichiojima-2/consultant).
