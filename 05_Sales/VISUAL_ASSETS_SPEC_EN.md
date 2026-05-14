# Visual Assets Specification

> 🌐 中文版本 / Chinese version: [VISUAL_ASSETS_SPEC.md](VISUAL_ASSETS_SPEC.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>

ASCII/Markdown specs and designer briefs for 3 external visual assets — ready to hand to a designer for high-res production (SVG / PNG / print).

---

## Asset 1: Three-Step Service Flow

### ASCII spec

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ 1. Diagnose  │ ──▶ │ 2. Build     │ ──▶ │ 3. Deliver   │
├──────────────┤     ├──────────────┤     ├──────────────┤
│ 10/25/50-q   │     │ L1-L5 courses│     │ Eight-stage  │
│ company-     │     │ in-class     │     │   report     │
│ profile      │     │ assets:      │     │ 30/60/90     │
│ survey       │     │ Prompt/Skill │     │   Roadmap    │
│ → L1-L5 score│     │ Workflow/    │     │ ROI +        │
│              │     │ Agent/Team   │     │ governance   │
└──────────────┘     └──────────────┘     └──────────────┘
   2-4 weeks            4-8 weeks            2-4 weeks
```

### Three layout alternatives

1. **Linear** — left to right, arrows emphasize flow (ASCII above)
2. **Circular** — three segments around a circle, emphasizing repeatable iteration (good for repeat customers)
3. **Pyramid** — diagnose at the base, build in the middle, deliver at the top, emphasizing layered convergence

### Designer brief

- **Size:** 1920×1080 (PNG) + SVG vector
- **Palette:**
  - Diagnose: indigo #1B3A6B
  - Build: teal-green #2D8B7C
  - Deliver: gold #D4A017
- **Typography:** Noto Sans TC Bold (zh) / Inter Bold (EN); title 32pt, body 16pt
- **Icons:** Stage 1 magnifying glass / Stage 2 gear / Stage 3 trophy
- **Animated version (optional):** MP4 30 sec, three segments lighting up in sequence

---

## Asset 2: L1-L5 Maturity Map

### ASCII spec (vertical pyramid version)

```
                  ╔════════════════════════════════╗
                  ║   L5  Agentic Team AI           ║
                  ║   Tool: ClawTeam                ║
                  ║   Multiple specialist Agents    ║
                  ╚════════════════════════════════╝
                              ▲
                  ┌────────────────────────┐
                  │ L4  Auto Agentic AI    │
                  │ Tool: Hermes Agent     │
                  │ Wiki+Skill+Workflow+   │
                  │ Gate = verifiable Agent│
                  └────────────────────────┘
                              ▲
              ┌─────────────────────────────────┐
              │ L3  Workflow AI                  │
              │ Tool: n8n                       │
              │ Skill + enterprise systems =     │
              │ Workflow                        │
              └─────────────────────────────────┘
                              ▲
          ┌──────────────────────────────────────────┐
          │ L2  Skill AI                              │
          │ Tool: Antigravity / Claude Code / Codex   │
          │ Personal know-how → reusable Skill        │
          └──────────────────────────────────────────┘
                              ▲
      ┌────────────────────────────────────────────────────┐
      │ L1  Chat AI                                         │
      │ Tool: OpenWebUI                                     │
      │ Org-wide safe AI usage                              │
      └────────────────────────────────────────────────────┘
```

### Card content (per level)

| Field | Content |
| --- | --- |
| Level | L1 / L2 / L3 / L4 / L5 |
| Name | Chat / Skill / Workflow / Auto Agentic / Agentic Team AI |
| Tool | OpenWebUI / Antigravity / n8n / Hermes / ClawTeam |
| Capability | One-line positioning |
| Output | What this layer hands off to the next |
| Who Uses It | Everyone / core users / process designers / IT+AI Champion / management |

### Three layout alternatives

1. **Vertical Pyramid** — ASCII above, emphasizing bottom-up stacking
2. **Horizontal Layers** — five blocks left to right, each layer color-banded
3. **Radial** — core methodology at center, five layers radiating outward

### Designer brief

- **Size:** 1920×1200 + A3 print
- **Color gradient:** L1 light blue → L5 deep gold, each layer deeper
- **Arrow text (between layers):** state each layer's "output = next layer's input"
  - L1 → L2: high-frequency prompts + scenarios
  - L2 → L3: Skill Library
  - L3 → L4: Workflows + Sub-workflows
  - L4 → L5: controlled Agents + Wiki
- **Footer:** "Each layer's output is the next layer's input."
- **Optional interactive HTML:** hover shows the full course link

---

## Asset 3: Verifiable Deliverables Visual

### ASCII spec

```
┌─ Diagnose ────────────────────────────────────────┐
│ ✓ AI maturity questionnaire & scoring results      │
│ ✓ Company profile & deployment-mode survey         │
│ ✓ As-Is Process Map & Systems Inventory           │
│ ─── [Gate 1 ✓] ────────────────────────────       │
└──────────────────────────────────────────────────┘

┌─ Build ───────────────────────────────────────────┐
│ ✓ L1 OpenWebUI accounts / groups / permissions     │
│ ✓ Prompt Library + personal-chat activation logs   │
│ ✓ L2 Skill Library (3-5 Skills) + Antigravity      │
│ ✓ L3 n8n Workflow PoC (3 workflows)               │
│ ✓ Sub-workflow Library + Data Tables Schema        │
│ ✓ GitHub Backup SOP + L4 Workflow Contract         │
│ ✓ L4 Hermes Agent + Wiki + Gate 4A-4E              │
│ ✓ L5 ClawTeam Agent Team Role Cards                │
│ ─── [Gate 2 / 3 / 4 / 5 ✓] ────────────────       │
└──────────────────────────────────────────────────┘

┌─ Deliver ─────────────────────────────────────────┐
│ ✓ Eight-stage consulting diagnostic report         │
│ ✓ 30/60/90-day Roadmap                            │
│ ✓ ROI tracking matrix + governance recommendations │
│ ✓ Stage Gate sign-off records                      │
│ ✓ SOW continuation recommendations                  │
└──────────────────────────────────────────────────┘
```

### Designer brief

- **Size:** 1920×1200 + A4 portrait print
- **Palette:** three distinct color blocks (Diagnose blue / Build green / Deliver gold)
- **Item prefix ✓:** green check icon (Lucide CheckCircle)
- **Gate markers:** circular "Stage Gate" stamp icons between sections
- **Optional interactive version:** click each item to expand a real example file (links to GitHub)

---

## Overall Production Notes

- **File naming:** `tigerai-visual-{asset}-{version}.{ext}`
- **Version control:** all Adobe Illustrator / Figma source files uploaded to `assets/source/`
- **Copyright notice:** add "© 2026 Tiger AI · Apache 2.0 · attribution required" at the bottom of each visual
- **Multilingual versions:** produce a Chinese version + an English version + a bilingual version of each visual
- **Accessibility:** contrast ratio ≥ AA; provide SVG alt text; color must not be the sole carrier of information (distinguish by shape too)
