# AI-Native eBook Production: Multi-IDE Orchestration as Methodology Engineering Infrastructure — A Design Science Investigation

---

**Author:** Yeh-Hsing Lu (also known professionally as Morris Lu; Chinese: 盧業興)  
**Affiliations:** Tiger AI (Independent Research); National Kaohsiung University of Science and Technology (NKUST)  
**ORCID:** [0009-0006-5373-0586](https://orcid.org/0009-0006-5373-0586)  
**Contact:** <morrislu@nkust.edu.tw>  
**Version:** 1.0 (release candidate; **not yet deposited**)  
**Date:** 2026-05-18  
**License:** Apache License 2.0  
**Artifact DOI:** pending Zenodo release (will be minted automatically on the first GitHub tag `v1.0.0`)  
**Preprint DOI:** pending Zenodo release  
**Repository:** <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>  
**Reproducibility manifest:** `09_Research_Paper/REPRODUCIBILITY.md`  
**Release manifest (frozen):** `09_Research_Paper/RELEASE_MANIFEST_v1.0.0.md` (will be re-frozen at the v1.0.0 tag commit immediately before deposit)  
**Suggested citation (post-release):** Lu, Y.-H. (2026). *AI-Native eBook Production: Multi-IDE Orchestration as Methodology Engineering Infrastructure*. Working paper. Zenodo. DOI: [to be inserted upon release].

> **Status note.** This document is a working draft staged for first formal release. All DOI fields above are deliberately marked *pending*; this draft must not be cited with a fabricated DOI. The actual concept and version DOIs will replace the *pending* markers within minutes of the GitHub `v1.0.0` tag triggering the Zenodo webhook.

---

## Abstract

Traditional methodology development relies on single-author cycles spanning years, producing static documents that readers consume passively. This paper presents a design science investigation into **AI-Native eBook production** -- a paradigm in which methodology artifacts are co-created through orchestrated multi-IDE environments (Claude Code, Cursor, Antigravity, Codex), version-controlled in Git, published with persistent identifiers (DOI), and consumed through reader-IDE interaction rather than linear reading. We instantiate this paradigm in the *GenAI Consulting Methodology Toolkit* (Apache 2.0; n = 354 documents; 7 languages; 22 specialized AI-IDE workflows across three IDE families). In our observed production of this artifact, we find four properties that we did not achieve in prior single-tool authorship attempts within the same project: (1) simultaneous multilingual coherence enforced cross-language, (2) multi-engine adversarial review (e.g., `/devil-pair-debate`, `/red-team-review`), (3) reader-queryable execution -- the same IDE that produced the artifact can interrogate it through workflows such as `/socratic-challenge` and `/deep-synthesize`, and (4) cryptographically reproducible derivation through Git history plus declarative workflow files. We evaluate against Hevner's seven design science guidelines and contrast quantitatively with traditional methodology development cycles (McKinsey 7-Step, Rosemann BPM development). We discuss implications for methodology engineering, the HCI thesis of IDE-as-medium, and the future of *active* academic publications in the LLM era.

**Keywords:** design science research; AI IDE; methodology engineering; multi-agent collaboration; executable documents; reproducible methodology; AI-native; literate programming; consulting frameworks

---

## 1. Introduction

### 1.1 Motivation

Methodology engineering -- the disciplined construction, validation, and dissemination of consulting frameworks, maturity models, and process reference architectures -- has historically been a slow, single-author craft. Canonical examples such as the Capability Maturity Model [Paulk et al. 1993], the Business Process Management Maturity Model [Rosemann & de Bruin 2005], and the Process Classification Framework [APQC 2024] each required multi-year cycles by small expert teams, were published as static documents (PDFs, journal articles), and consumed by readers in a fundamentally passive mode: read, then attempt application.

Three structural inefficiencies follow from this craft model:

1. **Cycle latency.** New methodologies trail their subject domain by 3-7 years. By the time a peer-reviewed AI maturity framework appears, the AI subject matter has moved through two paradigm shifts.
2. **Single-author bias.** Even excellent methodologies inherit the blind spots of their lead author. Adversarial review happens at peer-review time, often years after the bias has been baked into the artifact's structure.
3. **Reader passivity.** A methodology consumed as a static PDF requires substantial human translation labor to apply to a specific organization. The methodology cannot *answer questions* about itself.

Simultaneously, a new class of production environment has emerged: **AI-integrated development environments (AI IDEs)** such as Claude Code [Anthropic 2025], Cursor [Anysphere 2024], Google Antigravity [Google 2025], and OpenAI Codex CLI [OpenAI 2024]. These tools fuse large language model (LLM) inference with file-system, version-control, and shell-command primitives, making them general-purpose *cognitive infrastructure* rather than mere code editors.

### 1.2 Research Questions

This paper investigates whether AI IDEs, used in deliberate orchestration, can serve as the production environment for a new class of methodology artifact -- what we term the **AI-Native eBook**. Specifically:

- **RQ1.** What properties does multi-IDE orchestration enable in methodology production that single-tool authorship cannot?
- **RQ2.** How does reader-IDE interaction transform the consumption of a methodology artifact, and what design affordances are required?
- **RQ3.** What design principles govern AI-Native eBook engineering, and how do these compare against established methodology development guidelines?

### 1.3 Contributions

We make four contributions:

1. A **paradigm description** of AI-Native eBook production, distinguishing it from prior categories (AI-assisted writing, literate programming, executable documents).
2. An **instantiated artifact** -- the *GenAI Consulting Methodology Toolkit*, staged for release under Apache 2.0 with a pending Zenodo DOI -- that serves as both a working methodology and an empirical demonstration of the paradigm.
3. A **design science evaluation** of the artifact against Hevner et al.'s [2004] seven guidelines, with quantitative comparison against traditional methodology development cycles.
4. **Reusable infrastructure** in the form of 22 AI-IDE workflow specifications, three IDE configuration directories, and a `CITATION.cff` provenance file that other researchers can fork and adapt.

The remainder of this paper is structured as follows. Section 2 positions the work within related literature. Section 3 describes the instantiated artifact. Sections 4-8 elaborate the five distinguishing properties of AI-Native eBook production. Section 9 presents the design science evaluation. Section 10 discusses implications.

---

## 2. Related Work

### 2.1 Methodology Engineering and Design Science Research

The systematic construction of methodologies has been formalized through the **Design Science Research (DSR)** paradigm [Hevner et al. 2004; Peffers et al. 2007]. Hevner's seven guidelines -- problem relevance, design as artifact, design evaluation, research contributions, research rigor, design as search process, and communication of research -- provide the canonical lens through which IT artifacts (including methodologies) are evaluated as scholarly contributions.

Within DSR, methodology development is a recognized class of artifact [March & Smith 1995]. Notable subcategories include **maturity model development**, for which de Bruin et al. [2005] and Becker et al. [2009] articulate procedural standards. The present work uses DSR as its primary evaluation lens (Section 9) while introducing a *second-order* design science contribution: the artifact under study is not only a methodology, but a methodology *about how to construct methodologies in the LLM era*.

### 2.2 Literate Programming and Executable Documents

Knuth's [1984] **literate programming** introduced the idea that a program and its documentation should be co-resident in a single artifact, with the program *derivable from* the document. Jupyter notebooks [Kluyver et al. 2016] generalized this to computational science, allowing prose, code, and outputs to interleave.

More recent work on **observable notebooks** [Bostock 2017] and **reactive documents** [Victor 2011, 2014] pushes further: the document becomes interactive, the reader manipulates parameters and observes recomputed outputs. AI-Native eBooks extend this trajectory along a third axis: not just *interactive* documents but *queryable* documents -- where the reader's questions are answered by the same AI infrastructure that produced the document.

### 2.3 AI-Augmented Writing

A growing literature examines LLM-assisted writing in academic and professional contexts [Mirowski et al. 2023; Lee et al. 2022; Long et al. 2024]. The dominant frame is **augmentation**: a single human author paired with a single AI assistant, with research questions focused on creative control, attribution, and the perception of AI co-authorship.

We argue this frame is now insufficient. Once production moves from chatbot interfaces into **AI IDEs with file-system access**, the relevant unit of analysis is no longer the human-AI dyad but the **multi-IDE orchestration** -- multiple specialized AI engines, each contributing distinct capabilities, coordinated through file-system and version-control primitives. To our knowledge, this orchestration pattern has not been systematically studied in the methodology engineering context.

### 2.4 IDE-as-Medium

Engelbart's [1962] thesis on **augmenting human intellect** anticipated that computational interfaces would not merely speed up existing tasks but *restructure* human cognitive work. Victor's [2014] work on *media for thought* argues that programming environments themselves shape what thoughts can be cheaply thought.

AI IDEs are a fresh instantiation of this thesis at unprecedented scale. We extend Engelbart's and Victor's frame to argue that AI IDEs are not only media for thinking *about code*, but media for thinking *about anything that can be expressed in versioned plain text* -- including methodologies, books, contracts, and curricula.

### 2.5 The Gap

No prior work, to our knowledge, examines:

- the use of **multiple specialized AI IDEs in deliberate orchestration** as a methodology production environment;
- the publication of **active, reader-queryable methodologies** with persistent identifiers as scholarly artifacts;
- the **provenance chain** (Git + workflow files + DOI) that makes such artifacts reproducible in the formal academic sense.

This paper addresses that gap.

---

## 3. The Artifact: GenAI Consulting Methodology Toolkit

### 3.1 Scope

The instantiated artifact is the **GenAI Consulting Methodology Toolkit** (henceforth, *the Toolkit*), released under Apache License 2.0. The numeric properties below are **frozen at commit `7da82d7` (2026-05-18)** and independently verifiable via the commands in `09_Research_Paper/REPRODUCIBILITY.md`:

| Property | Value | Verification command (see REPRODUCIBILITY.md) |
| --- | --- | --- |
| Total markdown documents | 354 | `find . -name "*.md" -not -path "./.git/*" \| wc -l` |
| Substantive source documents (excluding `_EN`/`_DE`/`_FR`/`_ES`/`_JA`/`_KR`/`_TH` siblings) | 120 | see REPRODUCIBILITY.md §3 |
| Translation siblings (`_EN`/`_DE`/`_FR`/`_ES`/`_JA`/`_KR`/`_TH`) | 234 (78/31/31/31/31/31/1) | see REPRODUCIBILITY.md §3 |
| Specialized AI-IDE workflows | 22 (10 Claude Code, 10 Codex, 2 Antigravity) | `ls .claude/workflows/*.md .codex/workflows/*.md .antigravity/workflows/*.md \| wc -l` |
| Eight-stage methodology stages | 8 | (qualitative; see `00_Overview/EIGHT_STAGE_FLOW_STORY.md`) |
| Maturity model levels | 5 (L1 Chat -> L5 Agent Team) | (qualitative) |
| Industry case studies (Benchmark-grade format) | 7 | `ls 04_Scenarios/SAMPLE_CLIENT_CASE_*.md \| wc -l` |
| Git commits | 94 | `git rev-list --count HEAD` |
| Source languages with substantive coverage | 7 (繁體中文, English, Deutsch, Français, Español, 日本語, 한국어; partial Thai) | see REPRODUCIBILITY.md §3 |
| Repository URL | `https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit` | — |
| License | Apache License 2.0 (with `NOTICE` attribution requirements) | `cat LICENSE` |

### 3.2 Methodology Substance (Brief)

The Toolkit's substantive methodology -- out of scope for this paper but documented in the repository -- consists of:

- An **eight-stage closed-loop consulting flow** (Stage 1 As-Is -> Stage 2 Reference Model -> Stage 3 Best Practice/Ideal Practice -> Stage 4 Gap Analysis -> Stage 5 Problem Definition -> Stage 6 Phased Goals -> Stage 7 To-Be Design -> Stage 8 Implementation), with a quarterly Stage 2 radar loopback as the falsification mechanism;
- A **Tiger AI L1-L5 GenAI adoption maturity model**, organized on two orthogonal axes (scale axis L1-L3, AI-autonomy axis L4-L5), self-qualified at 9/10 conditions per Tool 2.5 of the maturity-model qualification scorecard;
- A **four-layer Enterprise AI Reference Model** (L1 Governance / L2 Business / L3 Information / L4 Technical) derived from the abstraction x volatility axis;
- A **three-phase contract model** (Phase A Diagnostic / Phase B Strategy / Phase C Implementation) with explicit Gate A/B/C exit points;
- A library of **toolkit templates** (40-question interview bank, scoring rubrics, Stage Gate criteria, Risk Register, Audit Log specification, AI Ethics checklist).

A separate paper [Lu, in preparation] presents the L1-L5 maturity model as an independent scholarly contribution. The present paper is concerned with the *production paradigm* by which the entire Toolkit was constructed.

### 3.3 What Makes the Artifact Interesting for This Paper

For the purpose of this paper, the Toolkit's substantive methodology is treated as a **representative payload**. The novel contribution lies in the answer to the question: *given that an artifact of this scope (354 documents, 7 languages, 8-stage methodology, 5-level maturity model, 7 case studies) needed to be produced, what production environment was used, and what properties did that environment confer that traditional environments cannot?*

Sections 4 through 8 answer this question along five dimensions.

---

## 4. Multi-IDE Production Architecture

The Toolkit was produced through deliberate orchestration of **three specialized AI IDE families**, each contributing distinct capabilities. The orchestration is encoded in three repository directories:

```text
Repository root/
├── .claude/         (Claude Code -- 1M context, cross-file synthesis)
│   ├── README.md
│   └── workflows/   (10 specialized workflows)
├── .codex/          (OpenAI Codex CLI -- engineering rigor, audit)
│   └── workflows/   (10 specialized workflows)
└── .antigravity/    (Google Antigravity -- parallel multi-agent)
    └── workflows/   (2 specialized workflows)
```

### 4.0 Background Vocabulary: AI IDE, Git, and GitHub

Three terms recur throughout this paper and warrant brief clarification for readers whose background is in management, information systems, HCI, education, or consulting methodology rather than software engineering. Readers already familiar with these constructs may skim this section.

**AI IDE.** By **AI IDE** we do not mean a conventional code editor, nor a standalone chatbot. We mean a working environment that fuses large language model (LLM) inference with a repository, a file system, version control, shell commands, and declarative task specifications. In contrast to a chatbot, an AI IDE does not merely answer questions: within controlled scope, it reads multiple files, compares versions, executes checks, modifies documents according to declared workflows, and writes results back into the repository. This makes an AI IDE a kind of **cognitive workbench**. For authors, it can synthesize across hundreds of files, track cross-file consistency, and run adversarial review. For readers, it can query a methodology, test scenarios against the reader's own organizational context, and trace the downstream implications of a single design change. Claude Code, OpenAI Codex CLI, Google Antigravity, and Cursor are the four AI IDEs discussed in this paper; all four embed LLM inference inside a versioned text workspace. Their significance for our argument lies not in any particular brand, but in their shared property of transforming methodology documents from static text into versioned artifacts that an agent can read, check, recompose, and be queried against. Throughout this paper, claims about "AI IDEs" should be read as referring to this construct -- the AI-embedded versioned workspace -- and not to any single product.

**Git.** Git is a distributed version control system that runs **on the author's local machine**: software that records every change to a set of files as a timestamped, authored, content-addressed unit called a "commit." The chain of commits forms an immutable, replayable history of how the files reached their current state. Branches and tags name particular points in this history (a "release" is typically a named tag, e.g., `v1.0.0`). Critically, Git itself is local and does not require any remote service to function; its role in the eBook lifecycle is **authorial accountability**. For a conventional document, "the document" refers ambiguously to whatever file the reader happens to open. For a Git-versioned artifact, "the document at commit `7da82d7`" is a precise, externally verifiable reference: every paragraph, every table, every workflow specification is traceable to a specific moment and a specific authored decision, whether or not the work is ever published. This is the operational basis for the paper's "full provenance" claim in §1 and §8.

**GitHub.** GitHub is the most widely used public hosting service for Git repositories. It is the layer at which a Git-versioned artifact transitions from private authorial work into a publicly accessible -- and publicly **evolvable** -- scholarly object. In the eBook lifecycle, GitHub serves three distinct functions:

1. **Distribution.** Anyone with internet access can clone the artifact at any prior commit, including any tagged release, without permission from or coordination with the author.
2. **Collaborative evolution surface.** Issues, pull requests, and discussions allow readers not merely to flag errata but to **propose substantive new content** -- for example, a new industry case study, a new workflow specification, an additional language translation, or a corrected scoring rubric. Through the pull-request mechanism, readers' contributions can be reviewed and merged into the canonical artifact, with the contributor's authorship preserved in Git history. This transforms the methodology from a one-to-many broadcast into a many-to-many **living artifact**, a mode of publication for which traditional methodology forms (book, PDF, journal article) do not have a direct equivalent: a book cannot accept reader-submitted chapters; a static PDF cannot incorporate reader corrections; a journal article cannot host a reader's subsequent empirical case study. A GitHub-hosted Git-versioned methodology can do all three.
3. **DOI bridge.** GitHub's release events trigger Zenodo's webhook, which mints a persistent DOI within minutes (see §8.2 and §10.3), turning a GitHub release into a citable, archived scholarly artifact.

Without this Git + GitHub + Zenodo chain, the eBook lifecycle would still be possible in principle, but would lose much of its reproducibility, its public contribution surface, and its citability. References throughout this paper to "the repository," "a commit," "the v1.0.0 release," or "the workflow files" should be read in the standard Git/GitHub sense.

### 4.1 Specialization by Cognitive Task

Different production tasks favor different IDE engines. The Toolkit's design uses each engine for the cognitive task at which it is strongest:

| Cognitive Task | Preferred IDE | Reason | Representative Workflow |
| --- | --- | --- | --- |
| Cross-file deep synthesis | Claude Code (Opus 4.7, 1M-token context) | Single-pass reasoning over the entire repository | `/deep-synthesize` |
| Adversarial debate | Claude Code (multi-agent spawn) | Spawnable specialized sub-agents | `/devil-pair-debate` |
| Long counterfactual stress tests | Claude Code | Sustained reasoning under hypothetical regime change | `/thought-experiment` |
| Engineering consistency audit | Codex CLI | Strict rule-following, low hallucination on structural checks | `/consistency-review` |
| Provenance / traceability generation | Codex CLI | Mechanical extraction with low creativity tolerance | `/generate-traceability` |
| Multi-agent parallel report drafting | Antigravity | Native parallel agent dispatch | `/generate-report` |
| Diagnostic interview simulation | Antigravity, Claude Code | Multi-role concurrent role-play | `/diagnose`, `/simulate-engagement` |

A complete enumeration is provided in Appendix A.

### 4.2 Why Not a Single IDE?

A natural objection: would the Toolkit not have been simpler to produce in a single IDE? Our answer is not that "multi-tool is necessarily superior," but rather that, in this artifact construction, no single IDE in our trial set was able to simultaneously optimize three tasks that stand in tension with one another: whole-repository synthesis, adversarial review, and engineering consistency audit. Multi-IDE orchestration, in this setting, is therefore not decorative tool-stacking but a **task-specialization design**. The three production challenges that drove this design choice were:

1. **Context windows are heterogeneous.** In our production process, shorter-context tools proved well suited to local audit and editing; repository-scale synthesis was carried primarily by Claude Code's long context (`/deep-synthesize`, `/cross-stage-trace`). We make no general claim about other IDEs' capabilities -- only that, within our specific tool-set and workflow, the long-context engine bore the cross-file synthesis load.
2. **Adversarial separation requires viewpoint difference.** A self-debate within a single LLM session is constrained by shared context, shared model preferences, and shared prior framing. Spawning fresh Claude sub-agents for `/devil-pair-debate`, or alternating Claude (as proposer) and Codex (as `/red-team-review` auditor), is not equivalent to human peer review, but did yield greater viewpoint separation than self-review within a single session in our observed comparisons.
3. **Synthesis and audit have differently directed biases.** In this study, long-context synthesis engines were well suited to maintaining narrative coherence and cross-file conceptual integration; the same capability, however, sometimes "narrativized" or smoothed over local inconsistencies. Because Codex tends toward structural checking and rule-following, it was used as a **structural auditor** rather than a primary synthesizer: `/consistency-review` repeatedly flagged naming, dependency, stage-logic, and formatting violations that the primary synthesis pass had let through.

### 4.3 Orchestration as a Declarative Specification

A key methodological move is that **the orchestration is itself a versioned artifact**. The `.claude/workflows/`, `.codex/workflows/`, and `.antigravity/workflows/` directories contain markdown specifications that any user can read, fork, modify, or invoke. This makes the production environment reproducible: a third party with the same IDE accounts can replay the workflows against the same repository state and observe similar outputs.

We argue this is a key property distinguishing AI-Native eBook production from ad-hoc AI-assisted writing: the *recipe for producing the artifact* is itself part of the artifact, version-controlled and citable.

---

## 5. Reader-as-Querier Interaction Model

### 5.1 Beyond Passive Reading

Traditional methodology consumption follows a linear pattern: the reader (a consultant, an executive, a graduate student) opens the document, reads sequentially, and attempts mental translation to their context. The translation labor is enormous and largely invisible; it accounts for much of the disappointment with otherwise excellent methodologies.

The Toolkit inverts this. The same Claude Code, Cursor, or Codex environment that produced the methodology can be used by readers to *interrogate* it. A subset of the 10 Claude Code workflows is designed specifically for reader use:

- **`/socratic-challenge`** -- the methodology asks the reader probing questions about their own organization, forcing them to articulate their actual situation in the methodology's terms;
- **`/theory-bridge`** -- the reader describes a concrete situation, and the workflow maps it onto the seven academic pillars cited by the methodology;
- **`/scenario-planning`** -- given the reader's constraints, the workflow produces three contrasting roadmaps with explicit trade-offs;
- **`/cross-stage-trace`** -- the reader proposes a change at one stage, and the workflow traces its downstream implications through stages 4-8.

### 5.2 The Onboarding Mechanism

A practical question follows: how does a reader's AI IDE come to *understand* the methodology well enough to support these workflows? The answer is that the repository ships with two onboarding files specifically designed for AI ingestion:

- **`AGENTS.md`** -- a 200-line specification that briefs any AI agent on the methodology's structure, key files, vocabulary, and discipline boundaries. It is the common primary entry point for any AI tool.
- **`CLAUDE.md`** / **`CODEX.md`** / **`ANTIGRAVITY.md`** -- IDE-specific extensions that activate their respective workflow libraries. For instance, `ANTIGRAVITY.md` imbues the AI with awareness of its "parallel multi-agent" task dispatch capabilities, while `CLAUDE.md` articulates its role as a "Strategic Reasoning Partner with Cross-File Synthesis."

These files transform a fresh LLM session from a generic assistant into a methodology-literate dialogue partner within seconds. Empirically, the difference is qualitative: an IDE session opened in the repository root, with its specific environment file auto-ingested, can answer methodology questions of substantial depth on the first turn, where the same model with no context produces generic AI consulting truisms.

In other words, the reader-as-querier mode does not consist of "handing the document to an arbitrary chatbot." It depends on repository-bundled orientation files, workflow specifications, and versioned context that, together, constrain a generic LLM session into a methodology-literate querying agent. The reader-as-querier capability is therefore not an inherent property of any one model, but a property of the model **plus** the orientation infrastructure shipped with the repository.

### 5.3 Implications for the Author-Reader Relationship

The classical author-reader relationship is asymmetric: the author broadcasts, the reader receives. AI-Native eBooks introduce a third party -- the reader's AI IDE -- that mediates the relationship in both directions. The reader still cannot literally interrogate the author, but they can interrogate a methodology-grounded AI that the author's published materials have shaped.

This raises interesting questions about authorial intent, methodology drift over reader populations, and the appropriate evaluation of methodology *transferability*. We return to these in Section 10.

---

## 6. Multilingual Coherence as Emergent Property

### 6.1 The Coherence Challenge

The Toolkit is published in seven languages. The naïve approach to multilingual methodology -- write in language A, translate to languages B-G -- accumulates two compounding problems:

1. **Drift.** Updates to the source language are not consistently propagated to translations.
2. **Asymmetric authority.** Readers in translated languages encounter terminology and examples calibrated for the source culture, often invisibly.

The Toolkit's production manages both problems through what we call **simultaneous multilingual coherence**: source updates and translation updates are treated as a single coordinated commit, and cross-language consistency is *enforced by automated sweep*. For example, the project memory system records discipline rules such as:

> *Real-name removal:* `新竹` -> `City X`, `Hsinchu` -> `City X`, `신주` -> `City X`. Must be applied across all 7 language files in the same commit.

Commit `1dcc569` (46 files modified, 2026-05-17) demonstrates this discipline in action: a single semantic change (removing real Taiwan place and institution names for legal risk reasons) was propagated across `CLIENT_JOURNEY_STORY` in all 7 languages, `MANUFACTURING_CONSULTING_STORY` (zh), and 14 related files, in one atomic commit. (Note: The bilingual versions of this preprint itself are maintained in synchronization via this multi-IDE mechanism, serving as a meta-demonstration of this discipline.)

### 6.2 Why This Is Unattainable by Single-Author Production

In our experience producing this artifact, a single human author would struggle to maintain simultaneous fluency and consistency across 7 languages at this document volume (354 files, hundreds of thousands of words). Even a team of professional translators would face substantial coordination overhead in achieving atomic propagation of semantic changes across languages on the timeline that multi-IDE production made possible here (the commit cited above was completed in approximately 45 minutes of one operator's session time). We do not claim these limits are absolute -- merely that, in our observed production setting, the multi-IDE workflow approach lowered the coordination cost meaningfully compared with prior single-tool attempts in the same project.

We characterize this as an **emergent property**: simultaneous multilingual coherence is not a feature any single agent in the production environment possesses, but it arises from the combination of LLM-fluent generation, Git atomic commits, and `/consistency-review`-style sweep workflows. No single human, and no single AI engine, would produce it; the production environment as a whole does.

### 6.3 Empirical Audit

A complete cross-language coverage audit, generated via the one-line Python script in `09_Research_Paper/REPRODUCIBILITY.md` Section 3.2, shows that of 120 substantive (i.e., non-IDE-meta) source documents:

- 31 (26%) are complete across all 5 non-source target languages (DE/FR/ES/JA/KR; EN is typically present as well),
- 48 (40%) have partial sibling coverage (1-4 of DE/FR/ES/JA/KR, with EN present in most cases),
- 41 (34%) have no translation siblings yet (low-priority internal task logs, ancillary files, and recently added documents awaiting their first translation wave).

This is achievable for a single-author project of this scope only through the production paradigm described.

---

## 7. Adversarial Quality Assurance

### 7.1 The Single-Pass Review Problem

Conventional methodology review is single-pass and human: the author writes, peer reviewers read once, comments are addressed, the artifact ships. This pattern leaves three failure modes uncovered:

- **Value-system blind spots** that align across reviewers and author (everyone in the discipline shares the same cultural assumptions);
- **Internal inconsistencies** that span more files than any single reviewer reads;
- **Counterfactual fragility** -- the methodology works in plausible scenarios but collapses under regime change (e.g., regulatory shift).

### 7.2 Workflow-Encoded Adversarial Review

The Toolkit addresses each through a corresponding workflow:

- **`/devil-pair-debate`** -- Claude-A defends a methodology claim; Claude-B argues against it from a Foucauldian or Bourdieusian critical-theory stance; Claude-C judges synthesis. The output exposes not bugs but *value-system biases*. Run, for example, against the Tiger AI L1-L5 model itself, this workflow surfaced an assumption that "AI autonomy is a desirable trajectory" -- a culturally contingent claim now explicitly noted in the methodology's discussion.
- **`/consistency-review`** (Codex) -- sweeps the entire repository for cross-file inconsistencies (terminology drift, contradicting numerical claims, broken cross-references). This workflow flagged, for instance, that role titles (specifically `IT 副理`) were inconsistent with the seniority implied by the character's responsibilities (the resolution, committed as `1dcc569`, upgraded the role to `IT 協理` across 17 files).
- **`/thought-experiment`** -- runs counterfactual stress tests: "If the EU AI Act criminalized L4 deployment, does the methodology still work? If LLM cost dropped 1000x, what becomes obsolete?" These produce explicit *fragility maps* that conventional review cannot generate.
- **`/red-team-review`** (Codex against Claude output) -- uses a different IDE engine to audit the primary author engine's output. Functionally analogous to switching peer reviewers between rounds, but with deterministic cross-engine independence rather than reviewer-pool politics.
- **`/diagnose`** (Antigravity) -- parallel multi-agent role-play. This workflow simultaneously instantiates multiple stakeholders with conflicting interests (e.g., a cost-conscious CFO, a performance-driven CTO, and a compliance-focused legal officer), allowing them to simultaneously stress-test and interrogate a specific stage of the methodology. This parallel adversarial role-play exposes blind spots in the methodology regarding cross-departmental alignment.

### 7.3 Implication: Methodology Hardness vs. Reviewer Pool Size

Traditional peer-review hardness scales linearly with reviewer count and is bottlenecked by reviewer attention and shared blind spots. AI-Native adversarial review scales with workflow design effort (one-time) and compute (variable), and exposes structural blind spots that human reviewers structurally cannot. Neither replaces the other; both should run in series. But the AI-Native layer changes the *floor* of methodology quality -- claims that survive `/devil-pair-debate` and `/red-team-review` are categorically harder than claims that survive only human review.

---

## 8. Reproducibility and Provenance

### 8.1 The "AI Slop" Problem

A common critique of LLM-generated content is unfalsifiable provenance: the reader cannot determine which claims came from human reasoning, which from LLM completion, and which from neither (i.e., hallucination). This critique is particularly acute for methodology artifacts, which derive their authority from theoretical lineage and empirical grounding.

### 8.2 The Toolkit's Provenance Chain

The Toolkit addresses this through a four-layer provenance chain:

1. **Git history** -- every change is timestamped and attributable to a commit. The 94 commits at time of writing encode the artifact's complete derivation history.
2. **AI-attribution discipline** -- commits made with substantive AI assistance carry a `Co-Authored-By:` trailer (e.g., `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`). Mixed-authorship commits are honest about the mixture.
3. **Workflow files as derivation recipes** -- the `.claude/workflows/`, `.codex/workflows/`, and `.antigravity/workflows/` directories archive the exact prompts and procedures used. A third party can replay them.
4. **Persistent identifiers** -- the pending Zenodo DOI (concept DOI + version DOI per release) will provide an immutable handle for academic citation after the `v1.0.0` tag is released.

### 8.3 Citation Discipline

The Toolkit further enforces citation discipline at the *content* level. All theoretical claims are traced to specific external sources in `00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md` (Rosemann BPM Maturity, CMMI, APQC PCF, SCOR, TOGAF, Dragon1 EA, etc.). Internal claims that derive from the Toolkit's own design choices are flagged as such and self-qualified using Tool 2.5's ten-condition scorecard.

This discipline addresses what we believe is the deepest objection to AI-assisted methodology production: that AI-augmented authors cannot resist the temptation to *generate plausible-sounding theory* in place of citing actual sources. The Toolkit's discipline -- encoded in `AGENTS.md` and enforced by `/evidence-audit` (Codex) -- makes such generation visible and excisable.

### 8.4 Reproducibility in the Formal Sense

A reader with:

- access to the public repository,
- accounts on Claude Code / Codex / Antigravity (or compatible AI IDEs),
- and the published workflow files,

can in principle re-derive the methodology from a substantially earlier commit forward, observing whether the same workflows produce convergent or divergent outputs. The artifact is **reproducible** in a sense that pre-LLM methodology artifacts (e.g., 1990s-era CMMI development) were not, because the production environment is itself published.

---

## 9. Evaluation

### 9.1 Hevner's Seven Design Science Guidelines

We evaluate the AI-Native eBook paradigm against the canonical Hevner et al. [2004] guidelines.

| # | Guideline | Self-Assessment | Evidence |
| --- | --- | --- | --- |
| 1 | Design as an artifact | [x] | The instantiated Toolkit is a viable, complete artifact (Apache 2.0, 354 files, pending Zenodo DOI). |
| 2 | Problem relevance | [x] | Methodology engineering crisis (cycle latency, single-author bias, reader passivity) is documented and structurally inherent. |
| 3 | Design evaluation | [!] Partial | Self-evaluation against own ten-condition scorecard (9/10). Comparative evaluation against traditional methodology cycles is qualitative (Section 9.2). Empirical reader-uptake studies are deferred to follow-on work. |
| 4 | Research contributions | [x] | Paradigm description, instantiated artifact, evaluation framework, reusable infrastructure -- four distinct contributions. |
| 5 | Research rigor | [x] | Theoretical lens (DSR), evaluation criteria (Hevner), comparison method (cycle-time and coverage metrics), all explicit. |
| 6 | Design as search process | [x] | 94 Git commits document the iterative search through the design space. |
| 7 | Communication of research | [x] | Two audiences: practitioners (the entire repository, multilingual) and academics (this preprint, pending Zenodo DOI). |

The single partial mark (Guideline 3) is honest: empirical reader-uptake studies are not yet in scope. We outline an empirical research agenda in Section 10.

### 9.2 Comparative Cycle Analysis

We compare AI-Native eBook production against three reference points: McKinsey's 7-Step problem-solving methodology development as documented in [Rasiel 1999]; Rosemann's BPM Maturity Model development [Rosemann & de Bruin 2005; de Bruin & Rosemann 2007]; and a representative GenAI maturity framework (Gartner AI Maturity Model, multiple revisions 2019-2024).

| Dimension | McKinsey 7-Step (canonical) [a] | Rosemann BPM-MM (academic) [b] | Gartner AI-MM (industry) [c] | Toolkit (AI-Native) [d] |
| --- | --- | --- | --- | --- |
| First public release to v1.0 | ~ 5 years | ~ 3 years (PhD-cycle) | ~ 18 months per revision | **~ 6 months** |
| Source language count at v1.0 | 1 | 1 | 1 (EN), some localized later | **7 simultaneously** |
| Substantive documents at v1.0 | ~ 30 (book) | ~ 6 (papers + supplements) | ~ 5 (research notes) | **120** |
| Specialized workflows | 0 | 0 | 0 | **22** |
| Production provenance | Memoir / interviews | Acknowledgments section | Editorial team list | **Full Git + workflow files + DOI** |
| Reader-queryability | None (static text) | None | None | **22 workflows reader-invocable** |
| License | Proprietary | Academic / Elsevier | Proprietary (paywall) | **Apache 2.0 (open)** |

**Footnotes for the comparison table:**

**[a] McKinsey 7-Step.** Estimates derived from Rasiel's [1999] account, which documents the method as accumulating from the early 1990s through formal publication. Cycle-time estimate refers to McKinsey's internal development of the 7-step formulation; document count refers to Rasiel's book (~ 200 pp.) as the primary public artifact. Substantively richer derivative books (e.g., Friga 2009) postdate the initial release.

**[b] Rosemann BPM Maturity Model.** Estimates derived from the de Bruin doctoral cycle [de Bruin & Rosemann 2005, 2007; de Bruin 2009]. Cycle-time estimate corresponds to the PhD work that produced the canonical model; document count counts the v1.0-era public papers (ECIS 2005, BPTrends 2005, Delphi paper 2007), excluding subsequent derivative work.

**[c] Gartner AI Maturity Model.** Estimates derived from Gartner's published research-note revision cadence (2019, 2021, 2023, 2024 substantive revisions; minor updates in interim years). Cycle-time estimate refers to revision cadence, not initial publication. Document count refers to the per-revision research-note bundle.

**[d] Toolkit (this paper).** All numbers frozen at commit `7da82d7` (2026-05-18) and reproducible via the commands in `09_Research_Paper/REPRODUCIBILITY.md`.

Numbers for the non-Toolkit columns remain approximations from publicly available sources; we welcome correction and will accept errata via repository Issues. Subject to those caveats, the *qualitative* pattern we observe is that, in this production setting, AI-Native production yielded considerably more documents (an order of magnitude in our count), across multiple languages simultaneously, with provenance and reader-queryability features that the named comparators do not, to our knowledge, currently offer. We note explicitly that the comparison is between *production paradigms* as exemplified by these reference points, not between the substantive merits of the methodologies themselves, and that we cannot rule out that other comparators (open-source maturity models, community wikis, etc.) might exhibit similar properties.

### 9.3 Limitations

We note three honest limitations:

- **Hallucination risk.** Despite citation discipline and `/evidence-audit`, residual hallucinated claims may exist. Readers are invited to flag them via repository Issues.
- **IDE access asymmetry.** Readers without Claude Code, Cursor, or equivalent cannot fully exercise the reader-as-querier model. This stratifies access by economic resource, a concern we share.
- **Sustainability.** The Toolkit's production rate depends on continued access to current-generation LLMs at sustainable cost. A meaningful price increase or capability decrease would change the calculus.
- **Data Privacy and IP.** Feeding reader-specific organizational contexts (e.g., via `/socratic-challenge`) into IDEs backed by public cloud APIs raises legitimate concerns about corporate data leakage. Enterprise deployment of this paradigm will rely heavily on zero-data-retention API agreements or mature local LLM infrastructure.

### 9.4 What This Paper Does Not Claim

We are explicit about three claims this paper does *not* make:

- **Not "peer-reviewed."** Publication on Zenodo confers a persistent identifier, not peer review. This preprint is offered for community feedback; a peer-reviewed version is the intended next step.
- **Not "validated through empirical case studies."** The Toolkit's substantive methodology (L1-L5, eight-stage flow) has been *constructed* with care but not yet *empirically validated* through longitudinal client engagements. Such validation is the explicit topic of a separate research line currently in protocol design (see `90_References/PILOT_STUDY_PROTOCOL.md` in the repository).
- **Not "AI as author."** The production environment is AI-Native, but authorial responsibility -- and accountability for errors -- rests with the human author. Co-authorship trailers acknowledge AI contribution to specific commits; they do not transfer authorship.

### 9.5 Planned Validation Experiment (Pre-Registration)

To move the present paper from a position-and-artifact contribution toward a research-grade evaluation, we pre-register a small-N reader-uptake study to be conducted following the v1.0.0 release. The protocol below is offered now so reviewers can assess methodological adequacy before results exist; final results will appear in the v2.0 revision.

**Hypotheses.**

- **H1 (Time):** Readers using the reader-as-querier workflows (`/socratic-challenge`, `/theory-bridge`, `/deep-synthesize`) to answer methodology comprehension questions will require less elapsed time per question than readers using the same methodology in static PDF form.
- **H2 (Correctness):** Reader-as-querier answers will exhibit non-inferior accuracy relative to PDF-reading answers, where accuracy is measured by agreement with a rubric pre-authored by the methodology author.
- **H3 (Application-readiness):** Reader-as-querier participants will produce more concrete, organization-specific application sketches in a 10-minute post-questionnaire task than PDF participants.

**Design.** Within-subject crossover, n = 6 participants (3 from each of two backgrounds: experienced management consultant; senior IT professional new to consulting frameworks). Each participant completes two sessions, separated by ≥ 7 days, with order counter-balanced: Session A uses the AI-IDE reader-as-querier model; Session B uses a PDF rendering of the same content. Each session presents the same 8 comprehension questions (different content randomly per session) and the same 10-minute application sketch task.

**Measures.**

- Time-to-answer per question (continuous, logged automatically),
- Answer correctness (5-point rubric, scored blind by an independent rater),
- Application sketch coverage (count of methodology elements referenced; quality rated 1-5 by the same blind rater),
- Self-reported cognitive load (NASA-TLX short form),
- Self-reported preference (post-experiment Likert).

**Statistical plan.** Paired t-tests (or Wilcoxon signed-rank for non-normal distributions) on within-subject differences; Bonferroni correction for the three hypothesis families. The sample (n = 6) is small by survey-study standards but adequate for the within-subject crossover design we use; we report effect sizes alongside p-values and treat the study as exploratory rather than confirmatory at this n.

**Pre-registration.** The full protocol, rubric, questionnaire texts, application-sketch prompts, and statistical plan will be deposited to the OSF (Open Science Framework) registry under a Zenodo-linked DOI before the first participant is recruited. The link will be appended to this section in the v1.1 revision of this preprint.

**Limitations of the planned study.** The within-subject crossover controls for between-participant variability but introduces order effects; counter-balancing addresses this only partially. The sample is convenience-recruited from the author's professional network, which limits generalizability. AI-IDE familiarity is a confound that we control for through a short pre-session training but cannot fully eliminate.

**Why pre-register now, before running the study.** Pre-registration before results exist commits us to the analytic plan and prevents post-hoc fishing. Reviewers of this preprint should treat Section 9.5 as a falsification commitment: if the study is run and the hypotheses are not supported, the v2.0 revision must report null or contrary findings honestly.

---

## 10. Discussion and Implications

### 10.1 For Methodology Engineering

The traditional cost structure of methodology development has been a barrier to entry. In the instantiation reported here, we observed that a single individual, using AI IDEs in the manner described, produced in months an artifact of comparable scope to those that have, in widely cited examples, required institutional teams and years. The implication we draw is not that all methodology engineering will become single-author -- on the contrary, the *evaluation* burden remains substantial and is largely unaffected by the production-side gains we describe. Rather, the *construction* phase has, at least in this one observed setting, become accessible to individuals working alone.

This may have second-order effects on the consulting industry's structure. Methodologies have historically been quasi-proprietary assets of the major firms (the "Bain Way," McKinsey's 7-Step). AI-Native open-source methodologies, released under Apache 2.0 with DOI-citable provenance, compete on a fundamentally different basis. Whether this leads to a *commons* model of methodology (analogous to open-source software) is an empirical question we cannot resolve here, but the production prerequisites are now in place.

### 10.2 For HCI and IDE Design

The Toolkit constitutes evidence for the **IDE-as-medium** thesis at a new scale. Cursor, Claude Code, Antigravity, and Codex were not designed with methodology engineering in mind; their general-purpose design proved sufficient. This suggests three directions for AI IDE designers:

1. **First-class workflow specifications.** The `.claude/workflows/`, `.codex/workflows/` directory conventions are emerging *de facto*. Formal standardization (a `.ide-workflows/` directory? a YAML schema?) would aid portability.
2. **Cross-IDE handoff primitives.** Currently, an author moves between Claude Code and Codex manually. A primitive for "spawn this task in another IDE engine and return the result" would tighten orchestration.
3. **Provenance as a built-in feature.** The Co-Authored-By Git trailer is a workable interim solution but not designed for AI provenance specifically. A standard for AI-attribution at the line level (analogous to `git blame`) would mature the provenance story.

### 10.3 For Academic Publishing

The Zenodo + GitHub release pattern offers an immediately available path to formal scholarly publication for artifacts that do not fit the traditional journal article mold. The path is:

1. Apache 2.0 license + `NOTICE` attribution requirements,
2. GitHub-Zenodo integration for automatic DOI minting per release,
3. `CITATION.cff` for machine-readable citation metadata,
4. SSRN preprint for citation discoverability in the social-sciences and management literatures,
5. Conference / journal submission as a derivative paper.

This stack is not a replacement for peer review, but it removes the cost of *waiting for* peer review to begin accumulating citation evidence and reader engagement.

### 10.4 For the "AI Slop" Concern

Critics of LLM-augmented content production often invoke the term "AI slop" -- content that is fluent, plausible, and substantively unanchored. We share this concern. We argue that the appropriate response is not to abjure AI production but to enforce provenance discipline: Git history, workflow file archival, citation requirements, adversarial review, DOI persistence. The difference between "AI slop" and "AI-Native scholarship" is exactly the discipline. The Toolkit's production is offered as one demonstration of what that discipline can look like in practice.

### 10.5 Empirical Research Agenda

We close with three empirical questions the present paper does not answer, and which we hope to address in follow-on work:

- **Reader-uptake studies.** Does the reader-as-querier model measurably reduce the translation labor between methodology consumption and organizational application?
- **Cross-author replication.** If a different author, with different blind spots, produced a competing AI-Native methodology in the same domain (GenAI adoption), how would the artifacts compare on coverage, internal consistency, and reader uptake?
- **Longitudinal methodology evolution.** Over 24 months, how does the artifact change as LLM capability and IDE features evolve? Does the workflow file approach age gracefully or become obsolete?

---

## 11. Conclusion

AI-Native eBook production, as instantiated in the GenAI Consulting Methodology Toolkit, illustrates a production approach that, in our observation, can meaningfully alter how methodology artifacts are constructed, published, and consumed. The four properties we identified -- multi-IDE orchestration, reader-as-querier interaction, simultaneous multilingual coherence, and provenance discipline -- together appear, in this instantiation, to substantially change the methodology engineering cost structure while improving (or at minimum not weakening) the artifact's auditability. We do not claim these results generalize without further study; the planned validation experiment (§9.5) and the empirical agenda (§10.5) name the kinds of evidence that would warrant a stronger generalization.

The paradigm is not without limitations, and several questions -- particularly around empirical reader uptake and cross-author replication -- remain open. We invite the research community to engage with the artifact, fork it under its Apache 2.0 license, and extend the paradigm to new methodology domains.

The repository, this preprint, the workflow specifications, and the `CITATION.cff` file are all openly available. Citation information is provided in the front matter.

---

## Acknowledgments

The author acknowledges the long-term intellectual influence of Prof. Michael Rosemann (Queensland University of Technology) on the Business Process Management lineage from which the Toolkit's maturity-model approach derives. The methodology is the author's responsibility alone; all errors, omissions, and AI-domain extensions do not represent the views of Prof. Rosemann or QUT.

We acknowledge the AI engines used in producing the Toolkit and this paper: Anthropic Claude (Opus 4.6, 4.7), OpenAI Codex CLI, Google Antigravity. AI contributions to specific commits are recorded via `Co-Authored-By:` trailers in the Git history.

---

## References

> **Citation audit (v1.0).** All references below were independently re-verified against external sources prior to v1.0 release. Four entries were corrected during audit: APQC (2024) → (2022/2024) for accurate publication year; Bostock (2017) corrected from "Observable: A new way to think with code" to "A Better Way to Code" (Medium); Long et al. (2024) corrected from CHI 2024 to DIS 2024 with DOI; Victor (2014) "Seeing Spaces" venue claim softened due to inconsistent secondary sources. Lu (in preparation) is the author's own forthcoming work and cannot be externally verified by design. Errata to other entries are welcomed via repository Issues.

APQC. (2022/2024). *Process Classification Framework, Version 7.3*. APQC. (Version 7.3 was published in 2022 and remains current as of 2024.)

Becker, J., Knackstedt, R., & Pöppelbuß, J. (2009). Developing maturity models for IT management. *Business & Information Systems Engineering*, 1(3), 213-222.

Bostock, M. (2017). *A Better Way to Code*. Medium, April 28, 2017. (The work that became d3.express and subsequently Observable.)

de Bruin, T., & Rosemann, M. (2005). Towards a Business Process Management Maturity Model. In *Proceedings of the 13th European Conference on Information Systems (ECIS 2005)*.

de Bruin, T., & Rosemann, M. (2007). Using the Delphi technique to identify BPM capability areas. In *Proceedings of the 18th Australasian Conference on Information Systems*.

Engelbart, D. C. (1962). *Augmenting Human Intellect: A Conceptual Framework*. Stanford Research Institute, Summary Report AFOSR-3223.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75-105.

Kluyver, T., Ragan-Kelley, B., Pérez, F., et al. (2016). Jupyter Notebooks -- a publishing format for reproducible computational workflows. In *Positioning and Power in Academic Publishing: Players, Agents and Agendas*, IOS Press, 87-90.

Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.

Lee, M., Liang, P., & Yang, Q. (2022). CoAuthor: Designing a human-AI collaborative writing dataset for exploring language model capabilities. In *Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems*.

Long, T., Gero, K. I., & Chilton, L. B. (2024). Not Just Novelty: A Longitudinal Study on Utility and Customization of an AI Workflow. In *Proceedings of the 2024 ACM Designing Interactive Systems Conference (DIS '24)*. DOI: 10.1145/3643834.3661587

Lu, M. (in preparation). *L1-L5: A Generative AI Adoption Maturity Model for Enterprises.*

March, S. T., & Smith, G. F. (1995). Design and natural science research on information technology. *Decision Support Systems*, 15(4), 251-266.

Mirowski, P., Mathewson, K. W., Pittman, J., & Evans, R. (2023). Co-writing screenplays and theatre scripts with language models. In *Proceedings of CHI 2023*.

Paulk, M. C., Curtis, B., Chrissis, M. B., & Weber, C. V. (1993). *Capability Maturity Model for Software, Version 1.1*. Carnegie Mellon University, Software Engineering Institute (CMU/SEI-93-TR-024).

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3), 45-77.

Rasiel, E. M. (1999). *The McKinsey Way*. McGraw-Hill.

Rosemann, M., & de Bruin, T. (2005). Application of a Holistic Model for Determining BPM Maturity. *BPTrends*, February 2005.

Victor, B. (2011). Explorable Explanations. *Personal essay*, <http://worrydream.com/ExplorableExplanations/>.

Victor, B., & Hellman, D. (2014). *Seeing Spaces*. Talk / dynamic poster. (Documented in the Dynamicland archive; original venue attribution varies across secondary sources, so a single venue is not asserted here.)

---

## Appendix A -- Workflow Inventory

The Toolkit's production environment encodes 22 specialized workflows across three IDE families. Each workflow is a markdown specification that the corresponding IDE can read and execute.

### A.1 Claude Code workflows (`.claude/workflows/`)

| Workflow | Purpose | Production use |
| --- | --- | --- |
| `/deep-synthesize` | Multi-file deep synthesis (1M context) | Cross-stage consistency drafting |
| `/theory-bridge` | Map client situation <-> 7 academic pillars | Onboarding new readers |
| `/scenario-planning` | 3 contrasting roadmaps + tradeoffs | Scenario library generation |
| `/socratic-challenge` | Probing questions to sharpen reader thinking | Reader-facing dialogue mode |
| `/cross-stage-trace` | Downstream impact of single change | Change-propagation analysis |
| `/simulate-engagement` | Full 6-week engagement simulation | Sales demo, training material |
| `/parallel-perspectives` | 6-stakeholder concurrent view | Stakeholder map generation |
| `/thought-experiment` | Counterfactual stress testing | Fragility map generation |
| `/devil-pair-debate` | Two Claudes argue, third judges | Value-system bias surfacing |
| `/methodology-fork` | Client-specific methodology fork | Custom-deployment scaffold |

### A.2 Codex workflows (`.codex/workflows/`)

| Workflow | Purpose | Production use |
| --- | --- | --- |
| `/academic-upgrade` | Convert practitioner prose to academic register | This preprint |
| `/bump-version` | Coordinated version bump across files | Release management |
| `/consistency-review` | Cross-file consistency audit | Pre-commit gate |
| `/diagnose` | Engineering diagnostic of a sub-area | Quality triage |
| `/evidence-audit` | Verify every claim has a citation | Hallucination guard |
| `/generate-report` | Mechanical report assembly | Deliverable generation |
| `/generate-traceability` | Build traceability matrix | Provenance support |
| `/harvest-insights` | Distill insights from raw notes | Note -> publication pipeline |
| `/methodology-test` | Apply methodology to a synthetic scenario | Self-validation |
| `/red-team-review` | Adversarial review against author's output | QA gate |

### A.3 Antigravity workflows (`.antigravity/workflows/`)

| Workflow | Purpose | Production use |
| --- | --- | --- |
| `/diagnose` | Multi-agent diagnostic | Parallel role-play interviews |
| `/generate-report` | Multi-agent report drafting | Parallel deliverable production |

---

## Appendix B -- Reproducibility Manifest

To re-derive a substantial subset of the Toolkit from any prior commit:

1. Clone the repository: `git clone https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit.git`
2. Checkout the desired commit: `git checkout <commit-hash>`
3. Open the repository in Claude Code (or compatible AI IDE).
4. Invoke a workflow, e.g., `/deep-synthesize "Re-derive Stage 4 Gap Analysis from Stage 2 and Stage 3"`.
5. Compare the workflow output against the actual Stage 4 documents at that commit.

Convergence is expected for substantive structural content; divergence is expected for stylistic choices and exact phrasing.

---

*End of preprint v1.0. The author welcomes correspondence, errata, and replication attempts at the email and repository above.*
