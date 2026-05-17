# ClawTeam Zitations- & Lizenzhinweis

> 🌐 Sprache: [繁體中文](CLAWTEAM_REFERENCE.md) ｜ [English](CLAWTEAM_REFERENCE_EN.md) ｜ Deutsch ｜ [Français](CLAWTEAM_REFERENCE_FR.md) ｜ [Español](CLAWTEAM_REFERENCE_ES.md) ｜ [日本語](CLAWTEAM_REFERENCE_JA.md) ｜ [한국어](CLAWTEAM_REFERENCE_KR.md)

Der **L5 Multi-Agent Organization**-Kurs in dieser Methodik übernimmt **ClawTeam** als Implementierungsplattform. Dieses Dokument hält die Upstream-Quelle, Lizenzbedingungen, Zitations-Leitlinien und den Umfang unserer Nutzung fest.

---

## 1. Upstream-Projekt

| Feld | Wert |
| --- | --- |
| **Projekt** | ClawTeam |
| **Tagline** | The Evolution of AI Agents: Solo 🤖 → Swarm 🦞🤖🤖🤖 |
| **Maintainer** | HKUDS (HKU Data Science Lab / 香港大學資料科學實驗室) |
| **GitHub URL** | <https://github.com/HKUDS/ClawTeam> |
| **Lizenz** | **MIT License** |
| **Version zum Zeitpunkt des Schreibens** | v0.2 — v0.3 (Stabilization → Multi-User + Web UI) |
| **Sprache** | Python 3.10+ |
| **Abhängigkeiten** | `tmux`, `git`, jeder CLI Agent (Claude Code / Codex / nanobot / OpenClaw usw.) |

## 2. Was ist ClawTeam

ClawTeam ist ein **CLI-Framework für Multi-Agent Self-Organizing Teams**: ein Mensch gibt ein High-Level-Ziel aus, und das Agent Team zerlegt, delegiert, kollaboriert und mergt autonom. Es ist kein SDK, sondern ein Set von CLI-Befehlen + Shared Filesystem + git-worktree Isolation + Messaging-Schicht — **jeder CLI Agent (Claude Code, Codex, Gemini, …) kann von ihm orchestriert werden**.

### Core-Architektur

| Schicht | Inhalt |
| --- | --- |
| **Team Management** | Ein Pool von Agents, die Workspace & Task Queue teilen |
| **Workspace Isolation** | Jeder Agent läuft in seinem eigenen git worktree & Branch — keine Konflikte |
| **Task Tracking** | Kanban-Style mit Dependency Chains und Auto-Unblocking |
| **Inter-Agent Messaging** | Point-to-Point Inboxes + Broadcasts |
| **Transport-Schicht** | File-based als Default; optional P2P (ZeroMQ); Redis auf Roadmap |
| **Storage** | Alles JSON in `~/.clawteam/`; keine Datenbank, kein zentraler Server |

### Core CLI Command Kategorien

| Kategorie | Schlüssel-Befehle |
| --- | --- |
| **Team** | `clawteam team spawn-team`, `status`, `snapshot`, `restore` |
| **Task** | `clawteam task create`, `update`, `list`, `wait` (inkl. `--blocked-by`) |
| **Inbox** | `clawteam inbox send`, `broadcast`, `receive`, `peek` |
| **Board** | `clawteam board show`, `live`, `attach`, `gource`, `serve` |
| **Profile** | `clawteam profile wizard`, `test`, `doctor`, `generate-profile` |
| **Context** | `clawteam context inject`, `conflicts`, `log` |
| **Spawn** | `clawteam spawn [backend] [command] --profile ...` |

### Drei Reference-Szenarien vom Upstream

1. **AutoResearch (8 Agents auf H100)** — 8 Exploration-Agents designten autonom 2.430+ Experimente; val_bpb verbessert 1,044 → 0,977 (+6,4%).
2. **Full-Stack Software Engineering (5 Agents)** — Architect, Backend (OAuth2 + DB), Frontend (React), Test/QA — parallele Branches auto-merged.
3. **AI Hedge Fund (7 Agents)** — Portfolio Manager + Value/Growth/Technical/Fundamentals/Sentiment Analysts + Risk Manager — Signale konvergieren durch die Messaging-Schicht.

### Roadmap-Zusammenfassung

- **v0.3** — Config-System, Multi-User (`CLAWTEAM_USER`), Web UI Dashboard, SSHFS / cloud-based Cross-Machine Sharing
- **v0.4** — Redis Transport (cross-machine Messaging)
- **v0.5** — Shared State Layer (NFS oder Redis); `RedisTeamStore` / `RedisTaskStore`
- **v0.6** — Identity, Permissions, Namespacing, Token Auth (verteilte Teams)
- **v1.0** — Volle Web UI, Real-time WebSocket, Multi-Team-Übersicht

---

## 3. Lizenz-Zusammenfassung

ClawTeam wird unter der **MIT License** veröffentlicht. MIT erlaubt Ihnen:

- Frei nutzen, modifizieren und weiterverbreiten
- Kommerziell nutzen
- Als Teil eines proprietären Produkts einbinden

**Die einzige Bedingung**: beim Weiterverbreiten müssen Sie den originalen **MIT Copyright-Hinweis** und **MIT License-Text** beibehalten.

> ⚠️ **Wichtig**
> Dieses Repo verbreitet ClawTeam-Source-Code **nicht weiter**. Wir **zitieren und lehren** seine Architektur, CLI und Design-Prinzipien nur im L5-Kurs und weisen Lerner an, **upstream selbst zu installieren** (`pip install clawteam`). Falls irgendein Kurs-Derivat (z.B. ein Fork, eine Distribution oder Anpassung) ClawTeam-Code weiterverbreitet, muss es den originalen MIT-Lizenzhinweis enthalten.

---

## 4. Umfang der Zitation in dieser Methodik

| Umfang | Behandlung |
| --- | --- |
| **Architektur & Design-Konzepte** | Verwendet als **primäre Lehrplattform** für L5; der Lehrplan beschreibt seine Team / Workspace / Task / Inbox / Transport-Architektur |
| **CLI-Befehle** | **Direkt** während L5 Hands-on Sessions verwendet |
| **Drei Reference-Szenarien** | Als **Inspiration** verwendet; diese Methodik lokalisiert sie in Manufacturing, Hospital und Retail Enterprise-Szenarien |
| **Source Code** | **Nicht reproduziert, nicht geforkt**; Lerner `pip install` vom Upstream |
| **Brand / Logo** | Zitiert namentlich „ClawTeam" im Kurs und diesem Dokument; keine Logo-Reproduktion |

## 5. Zitationsformat für Lerner

Beim Zitieren von ClawTeam in Slides, Berichten, PoCs oder abgeleiteten Werken folgendes Format verwenden:

**APA-Style:**

> HKUDS. (2026). *ClawTeam: Agent Swarm Intelligence* (Version 0.2-0.3) [Computer software]. GitHub. https://github.com/HKUDS/ClawTeam

**Kurzform:**

> Built on ClawTeam by HKUDS — <https://github.com/HKUDS/ClawTeam> (MIT License)

**Akademische Zitation:**

> ClawTeam [Software]. HKUDS, 2026. Available at: https://github.com/HKUDS/ClawTeam. MIT License.

## 6. Danksagungen

Wir danken **HKUDS (HKU Data Science Lab)** für das Open-Sourcing von ClawTeam, das Enterprise Multi-Agent Collaboration von einem Forschungsprojekt zu einer lehrbaren, lernbaren und deploybaren Engineering Practice gehoben hat. Das L5-Kurs-Design in dieser Methodik ist tief von seiner Architektur informiert und für Enterprise-Adoption in Taiwan und der chinesisch-sprachigen Welt lokalisiert.

---

## 7. Disclaimer

- Jede Beschreibung, Anwendung oder lokale Anpassung von ClawTeam in dieser Methodik repräsentiert die Interpretation des Methodik-Autors (Morris Lu / Tiger AI 虎智科技) und repräsentiert **nicht** die offizielle Position von HKUDS oder den ClawTeam-Maintainern.
- Falls ClawTeams API, Befehle oder Architektur in neueren Versionen ändern, siehe das [Upstream-Repository](https://github.com/HKUDS/ClawTeam) für den autoritativen aktuellen Stand.
- Der Methodik-Autor behält sich das Recht vor, dieses Dokument im Einklang mit Upstream-ClawTeam-Änderungen zu aktualisieren.
