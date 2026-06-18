# 📰 AI News Channel — Daily Auto Post

> "Design the system first, then pick the models." — Harness Engineering

A fully automated AI news channel using **Harness Engineering** principles.
1 human PM + 6 AI team members produce and publish daily AI news content across platforms.

---

## The Team

| Member | Model | Role |
|---|---|---|
| 🧠 CTO | Claude Opus | Editorial architecture & daily brief |
| 👨‍💻 Developer | Claude Sonnet | Content generation & publishing |
| 🔬 Researcher | Gemini Pro | News gathering & source verification |
| 🎨 Designer | Gemini Vision | Image prompts & visual QA |
| 📚 Librarian | Claude Haiku | Knowledge base & archiving |
| ✅ Supervisor | Claude Sonnet | QA verification & delivery gate |

---

## Daily Output (automated)

| Format | Platform | Spec |
|---|---|---|
| Long-form article | Medium / Substack | 800–1200 words |
| Short post | Twitter/X | ≤280 chars |
| Professional post | LinkedIn | ≤1300 chars |
| Casual post | Threads | ≤500 chars |
| Image card | Instagram / header | 1080×1080 / 2500×1686px |
| Newsletter | Email digest | Subject + 3 insights + CTA |

---

## The Fixed Loop

```
PM Brief → CTO → Researcher → Developer → Designer → Supervisor → PM Approve → Publish
```

Nothing skips a step. Nothing ships without Supervisor PASS.

---

## Setup

### 1. Clone and configure
```bash
git clone <repo>
cd ai-news-channel
cp .env.example .env
# Fill in your API keys in .env
```

### 2. Test API connections
```bash
source .env  # or: export $(cat .env | xargs)

python3 .claude/scripts/call_gemini.py --test
```

### 3. Run your first cycle (dry run)
Start Claude Code in this directory:
```bash
claude
```

Then brief the PM agent:
```
Write today's brief to working-notes/pm-brief.md, then invoke the cto agent
```

### 4. Verify outputs
```bash
bash .claude/scripts/verify_build.sh --date $(date +%Y-%m-%d)
```

### 5. Publish (after Supervisor PASS)
```bash
bash .claude/scripts/run_daily.sh --publish --date $(date +%Y-%m-%d)
```

---

## Repository Structure

```
ai-news-channel/
├── CLAUDE.md                        # Constitution — all agents read this first
├── constitution/
│   ├── project-state.md             # Current pipeline status
│   ├── skill-stack.md               # Models & APIs in use
│   ├── ai-member-boundaries.md      # Who does what
│   └── pending-tasks.md             # Task queue
├── .claude/
│   ├── agents/                      # Agent definition files
│   │   ├── cto.md
│   │   ├── developer.md
│   │   ├── researcher.md
│   │   ├── designer.md
│   │   ├── supervisor.md
│   │   └── librarian.md
│   ├── scripts/                     # API wrappers & publish scripts
│   │   ├── call_gemini.py
│   │   ├── call_gemini_vision.py
│   │   ├── publish_medium.py
│   │   ├── publish_twitter.py
│   │   ├── send_newsletter.py
│   │   ├── verify_build.sh
│   │   └── run_daily.sh
│   └── settings.json
├── knowledge-base/
│   ├── decisions/                   # CTO architectural decisions
│   ├── task-instructions/           # PM briefs archive
│   ├── deliverables/                # Daily content outputs
│   │   └── YYYY-MM-DD/
│   │       ├── article.md
│   │       ├── social-posts.md
│   │       ├── image-prompt.md
│   │       └── newsletter.md
│   └── project-docs/
│       └── topic-archive.md         # Prevents topic repetition
├── working-notes/                   # Inter-agent communication (reset each cycle)
│   ├── pm-brief.md
│   ├── cto-analysis.md
│   ├── researcher-findings.md
│   ├── developer-summary.md
│   ├── designer-output.md
│   └── supervisor-report.md
├── .env.example
├── .gitignore
└── README.md
```

---

## The 6 Harness Layers

| Layer | Implementation |
|---|---|
| **Loop** | Fixed agent order — never skip steps |
| **Tools** | Each agent has scoped tool permissions |
| **Context** | CLAUDE.md constitution read first by all agents |
| **Persistence** | All outputs saved to `knowledge-base/` |
| **Verification** | Supervisor + `verify_build.sh` before publish |
| **Constraints** | `ai-member-boundaries.md` — clear role limits |

---

## References

1. Mitchell Hashimoto, "My AI Adoption Journey" (2026/02)
2. OpenAI, "Harness Engineering: Leveraging Codex in an Agent-First World" (2026/02)
3. Birgitta Böckeler / Martin Fowler, "Harness Engineering" @ martinfowler.com (2026/02)
4. Anthropic, "Effective Harnesses for Long-Running Agents" (2025/11)
5. Aakash Gupta, "2025 Was Agents. 2026 Is Agent Harnesses." @ Medium
