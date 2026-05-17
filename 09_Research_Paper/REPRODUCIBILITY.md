# Reproducibility Manifest

**Companion to:** `2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md`
**Frozen at commit:** `7da82d7` (date 2026-05-18)
**License:** Apache License 2.0

---

## Purpose

This document enables any third party to (a) verify every quantitative claim made in the preprint at the exact commit above, (b) re-render the PDF, and (c) re-derive a substantial subset of the methodology using the published AI-IDE workflows. It is the operational counterpart to the preprint's reproducibility claims (see preprint Section 8).

If a number reported in the preprint does not match the output of the commands below at the stated commit, the discrepancy is a bug; please file an Issue on the repository.

---

## 1. Clone the artifact

```bash
git clone https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit.git
cd GenAI-Consulting-Methodology-Toolkit
git checkout 7da82d7
```

> **Primary working directory.** Start Claude Code, Codex, shell commands, and reproducibility checks from the public repository root. The local staging folder name is not part of the published path because its contents are uploaded as the repository root.

---

## 2. Software prerequisites

| Tool | Purpose | Tested version |
| --- | --- | --- |
| `git` | Repository access, history queries | 2.40+ |
| `find`, `wc`, `grep`, `sort`, `uniq` | File enumeration and counts | POSIX (any) |
| `pandoc` | PDF rendering of the preprint | 3.0+ |
| `python` (3.10+) | Optional helper scripts | CPython 3.10+ |
| An AI IDE: Claude Code, OpenAI Codex CLI, Google Antigravity, or compatible | Workflow replay (Section 7 below) | as available at time of replay |

PowerShell users on Windows may substitute `Get-ChildItem` and `Measure-Object` for `find` and `wc`. We provide POSIX commands below for the lowest common denominator.

---

## 3. Verifying preprint Section 3.1 numbers (artifact scope)

Run these exact commands from the repository root after `git checkout 7da82d7`.

### 3.1 Total markdown documents

```bash
find . -name "*.md" -not -path "./.git/*" | wc -l
```

**Expected output:** `354`

### 3.2 Substantive source documents (i.e., excluding translation siblings)

```bash
find . -name "*.md" -not -path "./.git/*" \
  -not -name "*_EN.md" -not -name "*_DE.md" -not -name "*_FR.md" \
  -not -name "*_ES.md" -not -name "*_JA.md" -not -name "*_KR.md" \
  -not -name "*_TH.md" | wc -l
```

**Expected output:** `120`

### 3.3 Translation siblings by language

```bash
for lang in EN DE FR ES JA KR TH; do
  count=$(find . -name "*_${lang}.md" -not -path "./.git/*" | wc -l)
  printf "%s: %d\n" "$lang" "$count"
done
```

**Expected output:**

```text
EN: 78
DE: 31
FR: 31
ES: 31
JA: 31
KR: 31
TH: 1
```

Total translations: 234. Substantive source files: 120. Total markdown: 354.

### 3.4 Specialized AI-IDE workflows

```bash
echo "Claude:     $(ls .claude/workflows/*.md     2>/dev/null | wc -l)"
echo "Codex:      $(ls .codex/workflows/*.md      2>/dev/null | wc -l)"
echo "Antigravity:$(ls .antigravity/workflows/*.md 2>/dev/null | wc -l)"
echo "Total:      $(ls .claude/workflows/*.md .codex/workflows/*.md .antigravity/workflows/*.md 2>/dev/null | wc -l)"
```

**Expected output:**

```text
Claude:     10
Codex:      10
Antigravity:2
Total:      22
```

### 3.5 Git commits and authorship

```bash
git rev-list --count HEAD
# Expected: 94 at commit 7da82d7

git log --format='%H %s' | head -5
# Lists most recent 5 commits, ending at 7da82d7 if this is HEAD
```

### 3.6 Industry case studies (Benchmark-grade)

```bash
ls 04_Scenarios/SAMPLE_CLIENT_CASE_*.md | grep -v '_EN\|_DE\|_FR\|_ES\|_JA\|_KR\|_TH' | wc -l
```

**Expected output:** `7`

---

## 4. Verifying preprint claims about provenance and AI attribution

### 4.1 Commits with explicit AI co-authorship

```bash
git log --all --grep='Co-Authored-By: Claude' --format='%H %ad %s' --date=short | wc -l
```

This counts commits that explicitly credit Claude (any model version) as co-author. The number should be > 0 and increase with each subsequent release.

### 4.2 Latest workflow inventory dump

```bash
{
  echo "## .claude/workflows/"
  ls -1 .claude/workflows/*.md | xargs -n1 basename
  echo
  echo "## .codex/workflows/"
  ls -1 .codex/workflows/*.md | xargs -n1 basename
  echo
  echo "## .antigravity/workflows/"
  ls -1 .antigravity/workflows/*.md | xargs -n1 basename
} > workflow_inventory.txt

cat workflow_inventory.txt
```

The resulting `workflow_inventory.txt` should match Appendix A of the preprint.

---

## 5. Rendering the preprint to PDF

The preprint is authored in Markdown. To produce a PDF identical (modulo platform font rendering) to the version archived on Zenodo:

### 5.1 Pandoc command

```bash
cd 09_Research_Paper

pandoc 2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.md \
  -o 2026_AI_NATIVE_EBOOK_PRODUCTION_preprint.pdf \
  --pdf-engine=xelatex \
  --metadata title="AI-Native eBook Production" \
  --metadata author="Morris Lu" \
  --variable=geometry:margin=1in \
  --variable=fontsize=11pt \
  --variable=linkcolor=blue \
  --variable=urlcolor=blue \
  --highlight-style=tango \
  --toc \
  --toc-depth=3
```

### 5.2 Font requirements for CJK

Some references and acknowledgments contain CJK characters (`繁體中文`, `盧業興`). If `xelatex` reports missing fonts, install:

```bash
# macOS
brew install --cask font-noto-sans-cjk-tc

# Ubuntu / Debian
sudo apt install fonts-noto-cjk

# Windows
# Install Noto Sans CJK TC from https://fonts.google.com/noto and re-run
```

Then add `--variable=mainfont="Noto Sans CJK TC"` to the pandoc command.

### 5.3 Validation

After rendering, the PDF should be approximately 18-22 pages depending on font and margin choice. Critical checks:

- **No `<sup>` HTML tags** rendered as literal text (paper uses `[a]` bracket notation, not HTML);
- **Section 9.2 footnotes** [a], [b], [c], [d] all appear and explain comparison-table claims;
- **All tables render** (some markdown parsers fail on the §4.1 task-IDE table -- verify);
- **No `pending` DOI placeholders** have been replaced with fabricated DOIs.

---

## 6. Cross-checking the comparative analysis (Section 9.2)

The comparison table in Section 9.2 contains approximations for non-Toolkit columns drawn from public sources. Reproducible checks:

- **McKinsey 7-Step.** Look up Rasiel (1999) page count and publication date via the ISBN catalog (ISBN 0-07-053448-0). Compare against the [a] footnote claim.
- **Rosemann BPM-MM.** Verify against the ECIS 2005 proceedings citation and the BPTrends February 2005 article. Both are publicly indexed.
- **Gartner AI-MM.** Gartner research notes are paywalled; the revision-cadence estimate is from public press releases and Gartner conference keynote slides. Where exact dates differ from our estimate, we will update the [c] footnote in v1.1.

We invite contributions to the references and to the comparison table via repository Issues or pull requests.

---

## 7. Replaying a workflow against the artifact

To exercise the reader-as-querier model described in Section 5:

### 7.1 Using Claude Code

```bash
# In an environment with Claude Code installed and authenticated:
cd GenAI-Consulting-Methodology-Toolkit
claude

# Inside Claude Code, run any of the 10 reader workflows:
/socratic-challenge "Apply the L1-L5 maturity model to a 500-person fintech company"
/theory-bridge "Our company is at Stage 4 by McKinsey 7-Step. Where does that map onto Tiger AI's 8-stage flow?"
/deep-synthesize "Trace the data dependencies between Stage 3 Ideal Practice and Stage 6 Phased Goals"
```

### 7.2 Using OpenAI Codex CLI

```bash
codex
# Inside Codex:
/consistency-review
/evidence-audit
/red-team-review "Section 5 of the preprint"
```

### 7.3 Convergence expectations

For substantive structural questions ("What does Stage 4 produce?"), independent replays should converge on substantively equivalent answers. For stylistic or open-ended questions, replays will diverge by design; this is not a bug.

---

## 8. Known limitations of this reproducibility manifest

- **LLM nondeterminism.** Workflow replays use stochastic LLM inference; bit-exact reproduction is not expected for prose outputs. Structural claims should converge.
- **Tool version drift.** Claude Code, Codex CLI, and Antigravity update frequently. Workflows tested at commit `7da82d7` may behave differently under future IDE versions. Pin to the IDE versions noted in Section 2 above where reproducibility is critical.
- **Network access.** Some workflows (notably any using `WebFetch` or `WebSearch`) require network access; replays in offline environments will return incomplete results.
- **Author-time corrections.** If a contradiction emerges between the preprint and a later commit (e.g., document counts shift after v1.1 translations land), the **release-pinned manifest** (`RELEASE_MANIFEST_v1.0.0.md`) takes precedence for the v1.0 publication.

---

## 9. Contacting the author

For corrections, replication results, or errata: `tiger.ai.tw@gmail.com` or via repository Issues at <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit/issues>.

When reporting a reproducibility discrepancy, please include:

- the commit hash you tested against (typically `7da82d7` for v1.0),
- the exact command you ran,
- the output you observed,
- the expected output from this manifest,
- your operating system and tool versions.
