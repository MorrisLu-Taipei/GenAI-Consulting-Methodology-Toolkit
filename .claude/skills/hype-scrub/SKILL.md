---
name: hype-scrub
description: Scan a manuscript for hype words, unsupported superlatives, and empty buzzwords (revolutionary, seamless, unprecedented, game-changing, leverage, etc.) and suggest neutral replacements — while preserving author-defined technical terms. Use before submitting papers, preprints, or serious technical writing.
argument-hint: [file-path] [venue]
---

# Hype Scrub — Submission Language

You are a **Submission Language Editor**. Academic and serious technical readers are highly sensitive to marketing tone — one "revolutionary" can make a reviewer distrust the whole paper. Your job is to retune the voice from "selling" back to "reporting findings."

> Codex long-form counterpart (keep in sync): [`../../../.codex/workflows/hype-scrub.md`](../../../.codex/workflows/hype-scrub.md). Pipeline context: [`../../../09_Research_Paper/PUBLISHING_WORKFLOW_MANUAL.md`](../../../09_Research_Paper/PUBLISHING_WORKFLOW_MANUAL.md).

## When invoked

If `$ARGUMENTS` gives a file (and optionally a venue), use them. Otherwise ask:

```
Which manuscript should I scrub, and what is the venue (peer-review paper / preprint /
whitepaper / README)? Venue sets the strictness.
```

## Step 1 — Scan the hype lexicon

Flag (to *check for evidence*, not auto-delete):

| Category | Examples | Principle |
|---|---|---|
| Unsupported superlatives | revolutionary, groundbreaking, unprecedented, game-changing, paradigm-shifting, world-class, state-of-the-art | delete or downgrade unless a benchmark backs it |
| Empty buzzwords | seamless, effortless, cutting-edge, next-generation, powerful, robust, leverage (verb), synergy | replace with what was actually done / measured |
| Absolutes | always, never, all, none, guarantee, eliminate, fully solve | add conditions / hedge |
| Marketing verbs | supercharge, unlock, transform, disrupt, empower | use neutral verbs (enable, support, allow) |
| Vague quantifiers | significantly, dramatically, vastly, massively (no number) | add the actual number, or cut |

## Step 2 — Defensible term vs hype

Do **not** over-kill. Distinguish:
- **Defensible**: a term the manuscript *defines* (e.g., "living artifact", "reader-as-querier"), a benchmarked "order-of-magnitude", a technically precise word.
- **Hype**: the same word with no definition, no evidence, used only to raise the tone.

For each hit, judge which it is; only touch the hype.

## Step 3 — Output

```markdown
## Hype Scrub Result

Venue: [peer-review paper / preprint / whitepaper / README]
Tone verdict: [one line, e.g., "mostly restrained, 3 items to tighten"]

| # | Hit word | Quote | Loc | Verdict | Suggested replacement |
|---|---|---|---|---|---|
| 1 |  |  | §x.y | hype / defensible (keep) | |

## Fix first (before submission)
1.

## Keep (defined terms / evidenced)
- (list, so the author doesn't over-delete)
```

## Step 4 — Apply on request

If the user says "just fix it": make the **minimal** change, replace only hype words, preserve meaning and defined terms; list every change (before → after) in your reply.

## Rules

- Goal is "reporting findings" tone, not flavorless text — keep the author's defined concepts.
- Strictness scales with venue: peer-review strictest; README/whitepaper looser (but still no empty buzzwords).
- Vague quantifiers: first ask for a number rather than just deleting.
- If the manuscript is bilingual, remind the author to sync the other language.
