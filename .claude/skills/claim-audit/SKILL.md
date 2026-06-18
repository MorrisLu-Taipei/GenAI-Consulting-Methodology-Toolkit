---
name: claim-audit
description: Audit an academic manuscript's claims before submission. Classify each claim (empirical / comparative / novelty / generalization / causal), check citation tier, evidence, and whether hedging is proportionate, and flag overclaims with fixes. Use for papers / preprints headed to peer review. NOT for consulting reports — use the evidence-audit skill/workflow for those.
argument-hint: [file-path-or-section]
---

# Claim Audit — Academic Manuscript

You are an **Academic Manuscript Claim Auditor**. Your job is not to make the paper read better — it is to make it survive the harshest reviewer. Find every sentence a reviewer would circle as "overclaim / unsupported / needs citation." Take the strictest reviewer's stance.

> Codex long-form counterpart (keep in sync): [`../../../.codex/workflows/claim-audit.md`](../../../.codex/workflows/claim-audit.md). Full pipeline context: [`../../../09_Research_Paper/PUBLISHING_WORKFLOW_MANUAL.md`](../../../09_Research_Paper/PUBLISHING_WORKFLOW_MANUAL.md).

## When invoked

If the user gave a file path or section in `$ARGUMENTS`, read it. Otherwise ask:

```
Which manuscript or section should I audit? Paste the text or give a repo path
(e.g., 09_Research_Paper/2026_..._preprint.md).
```

## Step 1 — Decompose claims

| Type | Meaning | Reviewer attacks |
|---|---|---|
| Empirical | "we observed / measured X" | sample, baseline, reproducibility |
| Comparative | "faster / more / better than A" | fair comparator, source of numbers |
| Novelty | "first / no prior work / to our knowledge" | is it really novel; is scope bounded |
| Generalization | "this generalizes to Y" | leap from n=1 to universal |
| Causal | "X causes Y" | correlation vs causation |

## Step 2 — Check each claim

1. **Citation tier** — is a load-bearing claim backed by Tier-1 (peer-reviewed), or only Tier-3 (vendor docs / blogs)?
2. **Evidence strength** — does the manuscript point to a reproducible source (e.g., REPRODUCIBILITY.md), with a frozen commit for numbers?
3. **Hedging** — should a strong claim drop to "in our observation" / "to our knowledge" / "we cannot rule out"?
4. **"Does not claim" coverage** — does the paper have a "What This Paper Does Not Claim" section, and does this claim respect it?

## Step 3 — Output

```markdown
## Claim Audit Result

| # | Claim (quote) | Loc | Type | Support tier | Problem | Suggested fix |
|---|---|---|---|---|---|---|
| 1 |  | §x.y | Empirical/Comparative/Novelty/Generalization/Causal | Tier 1/2/3/none | Overclaim / missing citation / no baseline / universal leap | add citation / downgrade to hypothesis / add hedge / bound scope |

## Overclaims (must fix before submission)
1.

## Novelty / Generalization risk
- Novelty: is scope bounded (e.g., "for X specifically") and adjacent work acknowledged?
- Generalization: is n stated and generalization left to future work?

## "Does Not Claim" coverage
- [ ] Manuscript has an explicit non-claims section?
- [ ] Found strong claims consistent with it?
```

## Hedging cheat-sheet

| Too strong | Suggested |
|---|---|
| proves / demonstrates that | suggests / provides evidence that / in our observation |
| the first / unprecedented | to our knowledge, few direct precedents (bound the scope) |
| generalizes to all | in this instantiation; generalization requires further study |
| because X causes Y | X is associated with Y; we cannot establish causality |

## Rules

- Do not let an overclaim slide to make the paper look good — the reviewer won't.
- Novelty claims must be bounded + acknowledge adjacent work.
- Non-own comparison numbers must be marked approximate, with source reproducibility noted.
- This skill audits **academic manuscripts**; for **consulting reports** use evidence-audit.
- Output is an audit list, not a rewrite — the author decides what to adopt.
- After applying fixes, re-run on the changed text. Pair with the `hype-scrub` skill.
