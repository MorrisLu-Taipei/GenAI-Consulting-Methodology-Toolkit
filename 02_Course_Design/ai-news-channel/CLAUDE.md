# 🏛️ Project Constitution — AI News Channel Daily Auto Post

> "What determines whether AI can reliably deliver results is not the model itself,
> but the system wrapped around the model." — Harness Engineering

---

## Project Overview

**Mission:** Fully automated daily AI news channel — research, write, design, and publish
AI-related news content across social platforms every day, with zero manual effort after setup.

**Output targets:**
- 1× long-form article (Medium / Substack)
- 3× short posts (Twitter/X, LinkedIn, Threads)
- 1× image card (for Instagram / Pinterest)
- 1× newsletter digest (email)

→ See current state: `constitution/project-state.md`
→ See pending tasks: `constitution/pending-tasks.md`

---

## My Team: 1 Human (PM) + 6 AI Members

| Member | Powered by | Responsibility |
|---|---|---|
| CTO | Claude (claude.ai) | Content strategy, editorial architecture |
| Developer | Claude Code | Automation scripts, publishing pipelines |
| Researcher | Gemini Pro | Daily AI news gathering, source verification |
| Designer | gpt-image-2 | Image cards, visual formatting, thumbnail checks |
| Librarian | Scripts + NotebookLM | Knowledge base, topic archive, trend tracking |
| Supervisor | Claude Code | QA, format checks, publish verification |

---

## The Fixed Loop (NEVER skip steps)

```
PM sets daily topic/brief
    → CTO (editorial plan & content structure)
        → Researcher (gather news, sources, data)
            → Developer (generate content, format posts)
                → Designer (create image card)
                    → Supervisor (verify all outputs)
                        → PM (final approve & publish)
```

Every task goes through this loop. No shortcuts. No skipped steps.

---

## Constraints (Hard Rules)

- **CTO** does NOT write content — designs the structure and brief only
- **Developer** does NOT publish directly — must pass Supervisor first
- **Researcher** and **Designer** run on separate Gemini instances — no shared context
- **Supervisor** does NOT approve incomplete deliverable sets (all 5 outputs required)
- **Librarian** archives after every completed cycle — knowledge never lost
- All outputs saved to `knowledge-base/deliverables/<YYYY-MM-DD>/` before task is done

---

## Definition of Done

A daily post cycle is NOT complete until:
- [ ] Long-form article saved to `knowledge-base/deliverables/<date>/article.md`
- [ ] Short posts saved to `knowledge-base/deliverables/<date>/social-posts.md`
- [ ] Image card saved to `knowledge-base/deliverables/<date>/image-card.png` (or prompt)
- [ ] Newsletter digest saved to `knowledge-base/deliverables/<date>/newsletter.md`
- [ ] Supervisor report written to `working-notes/supervisor-report.md` with PASS
- [ ] Librarian updated `constitution/project-state.md` and topic archive
- [ ] PM confirmed acceptance

---

## Content Guidelines

- **Tone:** Clear, insightful, non-hype — respect reader intelligence
- **Length:** Article 800–1200 words; social posts under platform limits
- **Sources:** Minimum 3 verified sources per article; no single-source stories
- **Image spec:** 2500×1686px for article header; 1080×1080px for social card
- **Language:** English (default); Traditional Chinese variant on request
