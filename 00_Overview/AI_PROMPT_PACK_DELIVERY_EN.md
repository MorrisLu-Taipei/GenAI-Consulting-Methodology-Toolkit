# Book II AI Prompt Pack (Consulting Engagement Delivery)

> 🌐 Language: [繁體中文](AI_PROMPT_PACK_DELIVERY.md) ｜ **English**
> Counterpart to Book I's [`11_AI_Prompt_Pack.md`](https://github.com/MorrisLu-Taipei/consultant-thinking-framework/blob/main/11_AI_Prompt_Pack.md). Book I's pack trains *judgment*; this pack drives that judgment through each stage of *delivery*.
> Shared discipline: **separate signal from inference, never fabricate, mark the unverified as "to confirm", process client data only with approved AI / private endpoints.**

---

## How to use
Paste client data / interview notes into each prompt's `{{ }}`, or trigger via the `consulting-delivery-coach` skill. Every prompt asks the AI to **cite the evidence source** and **state the basis for the L-level**.

---

### 1. Client profile → preliminary L-level
```
You are an AI-transformation diagnostic consultant. From the client background below, give a preliminary L1-L5 maturity judgment.
Rule: tie every judgment to specific evidence in the background; mark dimensions with insufficient evidence as "to diagnose" — do not guess.
Output: preliminary L-level + the 3 most important follow-up questions.
Client background: {{paste}}
```

### 2. Interview notes → Phase A diagnostic summary
```
Turn the interview transcript below into a Phase A diagnostic summary.
Structure: (1) client's exact words (facts) (2) real pain (surface → root) (3) the current job-to-be-done (4) the diagonal (competitor blind spot × client future need × our entry) (5) evidence gaps (mark "to confirm").
Do not add anything not in the transcript.
Transcript: {{paste}}
```

### 3. Diagnosis → course-design recommendation
```
From the L-level diagnosis below, recommend an L1-L5 course path.
Rule: first decide whether the client lacks capability / process / governance / tooling, then design the course; explain the ordering.
Output: course path + target output per stage + risks.
Diagnosis: {{paste}}
```

### 4. Diagnosis → consulting-report outline
```
Turn the diagnosis below into an eight-stage consulting-report outline.
Must include: Executive Problem Statement (written from the diagonal), Roadmap, Risk Register, Stage Gate Criteria.
Cite an evidence source for each conclusion; do not state anything as a conclusion without evidence.
Diagnosis: {{paste}}
```

### 5. Roadmap → delivery checklist
```
Turn the Roadmap below into an acceptance-ready delivery checklist.
Rule: each item needs an "acceptance criterion" (what counts as successful delivery) + "is this delivering capability or a tool". Flag tool-only items.
Roadmap: {{paste}}
```

### 6. Project status → risks and next step
```
You are a project reviewer. From the project status below, list risks and the next step.
Focus: scope creep, whether a Gate should fire, final-payment risk, whether the client's structure actually improved.
Output: Top 3 risks + recommended next step + whether to enter the next Phase.
Status: {{paste}}
```

---

## Safety & honesty reminder
- Process client data only with **company-approved AI or a private endpoint**; never paste into public services.
- A human consultant reviews all AI output; **anything marked "to confirm" must not be delivered as a conclusion**.
- Anonymize external cases ("Company ABC" / "City X"). This pack is a tool, not final legal / financial / security advice.
