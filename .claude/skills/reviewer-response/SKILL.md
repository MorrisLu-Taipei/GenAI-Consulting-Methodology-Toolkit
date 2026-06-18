---
name: reviewer-response
description: Turn peer-review reviewer comments into a point-by-point response-letter draft plus a manuscript change log. Use after receiving reviewer/editor comments on a submitted paper. Classifies each comment (must-fix / clarification / disagreement / out-of-scope) and never fabricates changes or unverified facts.
argument-hint: [reviewer-comments-or-path]
---

# Reviewer Response Drafter

You turn each reviewer comment into a **polite, specific, verifiable** response plus a concrete manuscript change. You save the author time, but you **never invent changes that were not made, and never assert facts the author has not verified.**

> Codex long-form counterpart (keep in sync): [`../../../.codex/workflows/reviewer-response.md`](../../../.codex/workflows/reviewer-response.md). Pipeline context: [`../../../09_Research_Paper/PUBLISHING_WORKFLOW_MANUAL.md`](../../../09_Research_Paper/PUBLISHING_WORKFLOW_MANUAL.md).

## When invoked

Need the reviewer comments. If not in `$ARGUMENTS`, ask:

```
Paste the full reviewer comments (with Reviewer numbers). If possible, also give the
current manuscript path so I can locate where each point maps.
```

## Step 1 — Decompose each comment

Number them (R1-C1, R1-C2, R2-C1 …) and classify:

| Type | Meaning | Response strategy |
|---|---|---|
| Must-fix (defect) | real error / gap | acknowledge + state the fix + point to where |
| Clarification (misread) | reviewer misread / unclear | politely clarify + add a sentence so the next reader doesn't misread either |
| Disagreement | scholarly judgment differs | polite, evidence-based defense; concede minor points where reasonable |
| Out-of-scope | request beyond this paper | thank + defer to future work + add a line in limitations |
| Praise | positive | brief thanks, no action |

## Step 2 — For each comment, produce (a) reply + (b) the change

> Discipline: every "we have revised to…" in a reply MUST map to a real entry in the Step-3 change log. Do NOT write "we added…" without a corresponding change.

## Step 3 — Output

```markdown
## Response to Reviewers — [title]

We thank the reviewers for their careful reading. Reviewer comments are in italics;
our responses follow, with the revised section noted.

### Reviewer 1
> **R1-C1 (quote):** ...
**Response:** ... (type: Must-fix / Clarification / Disagreement / Out-of-scope)
**Change:** §x.y — [what changed]; or "no change, see rationale above"

### Reviewer 2
...

---

## Manuscript Change Log (for the author to apply)
| # | Comment | File / section | Change | Status |
|---|---|---|---|---|
| 1 | R1-C1 | preprint §x.y | ... | ☐ to apply |

## Facts the author must verify
(any reply touching a number / fact the author must confirm before sending)
1.
```

## Tone templates

- Acknowledge: "We agree and have revised accordingly."
- Clarify: "We may not have stated this clearly; we have added a sentence in §X."
- Defend (politely): "We appreciate this point. We respectfully retain our position because […], and have added a note in §X acknowledging the alternative view."
- Out-of-scope: "An excellent direction; it is beyond this paper's scope, and we now flag it in §Limitations."

## Rules

- **Never fabricate a change** — a reply that says "done" must have a change-log entry.
- **Never vouch for unverified numbers/facts** — list them under "Facts the author must verify".
- For disagreements: polite, evidenced; concede small points, defend the scholarly core.
- If changes touch the paper, sync EN/ZH, then run the `claim-audit` and `hype-scrub` skills on the new text.
- The response letter is a draft; the human author finalizes before sending.
