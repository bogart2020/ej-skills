---
name: fact-check
description: Deep-research and verify factual accuracy against primary sources. Use when investigating whether a topic, claim, or rumour is true, auditing a document, draft, file, or URL for factual errors and citation entailment, or stress-testing a prior statement in the conversation.
argument-hint: "[topic, claim, file, or URL]"
license: MIT
---

# Fact Check

Verify claims by decomposing them into **atomic claims**, testing each with paired primary-source and **falsification queries**, and tracing every secondary report back to its **Tier 1 primary source**.

## Environment adaptation

Adapt tool use to the active runtime:

- **Chat environment** (Claude Desktop, web chat): verify claims using web search, URL fetching, and any attached documents or images. Run the verification sequence inline.
- **Code and CLI environment** (Claude Code, Codex, Antigravity, Gemini CLI, Cursor): combine web search with local codebase inspection (`grep`, file reads, `git log`), shell/Python execution for quantitative checks, and test runs. When auditing **4 or more atomic claims** or investigating a broad topic in a harness that supports subagents, dispatch parallel verification subagents so raw search pages stay out of the main context window; handle 1 to 3 claims inline.

## Domain playbooks

When a claim falls into one of the specialized domains below, read [`references/domain-playbooks.md`](references/domain-playbooks.md) before running Step 2:

| Claim domain | What `references/domain-playbooks.md` provides |
| :--- | :--- |
| **Software, APIs, and benchmarks** | Version-pinned docs lookup, changelog/release-note tracing, benchmark methodology auditing |
| **Science, medicine, and academic papers** | DOI/arXiv verification, study hierarchy, sample-size and p-hacking checks, retraction checks |
| **Economics, finance, and statistics** | Denominator/base-rate checks, inflation/seasonality adjustments, regulatory filing (`10-K`/`8-K`) tracing |
| **Quotes, history, and viral media** | Earliest-appearance tracing, misattribution traps, context-stripping checks |

## Verification sequence

Run these five steps in order.

### Step 1: Decompose and decontextualize

Identify which input branch applies:

1. **Topic or question**: surface the core factual propositions and common misconceptions circulating on the topic.
2. **Document, file, or URL**: extract every checkworthy, falsifiable proposition in the text (skipping pure opinion and boilerplate).
3. **Prior conversation turn (self-audit)**: treat the target statement as untrusted input and extract every factual claim it made.

Rewrite the extracted propositions into a numbered list of **atomic claims**:

- Split compound sentences so each atomic claim tests a single fact (a true clause must never mask a false sibling clause).
- **Decontextualize** each claim: replace pronouns (`it`, `they`, `this study`), relative dates (`last year`, `recently`), and shorthand with explicit canonical entity names and concrete dates or versions.
- Preserve causal links (`X caused Y`) and essential qualifiers (`in browsers without WebGPU`, `up to 20%`). Where a sentence is irreducibly ambiguous, list both interpretations explicitly.

**Completion criterion**: Every checkworthy proposition in the target is listed as a numbered, self-contained atomic claim carrying its explicit entity names and temporal anchor.

### Step 2: Triangulate and falsify

Route each atomic claim to the tool that owns its ground truth:

- **Codebase or local repository claims**: inspect the source files, git history, or run the test/command directly.
- **Mathematical, percentage, or statistical claims**: compute the exact figures in Python or shell (`python3 -c ...`) when a code tool is available, or write out the explicit arithmetic step by step.
- **World, documentation, or literature claims**: run **paired search queries** for every claim:
  1. **Neutral primary-source query**: strip adjectives and presuppositions (`"Bun vs Node.js HTTP throughput methodology"` rather than `"Why Bun is 4x faster than Node.js"`), targeting official documentation, specs, filings, or primary datasets.
  2. **Popperian falsification query**: actively search for counter-evidence, errata, deprecations, retractions, or methodological critiques (`"<topic or claim>" errata OR deprecated OR criticism OR limitation OR retraction`).
  3. **Temporal anchor**: include the relevant year, date, or version number in queries for time-sensitive facts.

**Completion criterion**: Every atomic claim from Step 1 has been tested by both a primary-source retrieval pass and an explicit falsification pass (or direct local tool execution for code and math).

### Step 3: Read laterally and trace to Tier 1

Defeat **citogenesis** (circular reporting where multiple secondary blogs or news outlets repeat the same unsourced claim):

- **Trace to the root node**: five articles citing the same press release, blog post, or unnamed study count as a single unverified thread. Follow hyperlinks, footnotes, DOIs, and named studies backward until you inspect the **Tier 1 primary source** directly.
- **Read laterally**: when a claim rests on an unfamiliar domain, organization, benchmark author, or study, run an external search about the source itself (`"<source or author>" funding OR reputation OR criticism OR conflict of interest`) rather than reading the page's self-authored "About" section.
- Grade every source against the **Source hierarchy** below. Use Tier 3 sources (Wikipedia, Stack Overflow, engineering blogs, press releases) strictly as discovery indices to locate Tier 1 footnotes.

**Completion criterion**: Every atomic claim's evidence chain terminates at a verified **Tier 1** primary source, or explicitly records why Tier 1 is inaccessible and documents independent **Tier 2** corroboration.

### Step 4: Assign calibrated verdicts

Assign each atomic claim one categorical label from the **Verdict taxonomy** below (`Verified`, `Refuted`, `Mixed / Needs Context`, `Outdated`, `Disputed`, or `Unverifiable`), paired with the highest source tier verified (`Tier 1` or `Tier 2`). Express certainty through the categorical verdict and source tier rather than invented single-claim confidence percentages.

**Completion criterion**: Every atomic claim from Step 1 carries one categorical verdict and its verified source tier.

### Step 5: Report with citation entailment

Render the Fact-Check Report inline using three sections (write to a Markdown file on disk only when the user asks to save a file):

1. **Verdict Summary**:
   - **Precision tally**: `X / Y atomic claims Verified` (plus counts of `Refuted`, `Mixed / Needs Context`, `Outdated`, `Disputed`, `Unverifiable`).
   - **Bottom line**: 2 to 3 sentences synthesizing what holds up, what fails, and the most important context discovered.
2. **Claim-by-Claim Audit**:
   For each numbered atomic claim:
   - **Claim**: The decontextualized atomic claim (and original quote/location if auditing a text).
   - **Verdict**: `[Verified | Refuted | Mixed / Needs Context | Outdated | Disputed | Unverifiable]` (`Tier 1` / `Tier 2`).
   - **Evidence & Analysis**: Concise explanation of what the primary source shows, including any caveats surfaced by the falsification query.
   - **Primary Citation**: `[Source Title, Author/Org (YYYY-MM-DD or Version)](URL)` followed by a **verbatim excerpt** (or exact file and line range `[file.ext](file:///path#L10-L20)` for local code) proving entailment or contradiction.
3. **Drop-in Corrections** (include whenever any claim is `Refuted`, `Mixed / Needs Context`, or `Outdated`):
   - Provide exact, ready-to-paste replacement text that fixes the factual error or supplies the missing baseline context.

**Completion criterion**: Every atomic claim from Step 1 appears in the Claim-by-Claim Audit with a session-verified URL, date/version, source tier, and verbatim excerpt, and every flawed claim has a drop-in correction.

---

## Reference rules

### Source hierarchy

| Tier | Category | Examples | Evidentiary role |
| :--- | :--- | :--- | :--- |
| **Tier 1** | **Primary & authoritative** | Official specs and technical docs (RFCs, W3C, MDN, vendor docs for their own API), source code and git history, peer-reviewed empirical studies, court transcripts, SEC/regulatory filings (`10-K`, `8-K`), official government datasets (BLS, Census, WHO), verbatim primary recordings | **Terminal proof.** Sufficient to verify or refute a claim within its domain. |
| **Tier 2** | **High-trust secondary** | IFCN-signatory fact-checks, established newsrooms of record citing named sources, peer-reviewed systematic reviews and meta-analyses, authoritative textbooks | **Corroborating proof**, or fallback proof when Tier 1 is paywalled or offline (state explicitly that Tier 1 was not directly inspected). |
| **Tier 3** | **Community & tertiary** | Wikipedia articles, Stack Overflow answers, GitHub issue threads, personal engineering blogs, corporate press releases (for competitor comparisons) | **Discovery only.** Use to locate the Tier 1 footnote or link, then verify the Tier 1 source directly. |
| **Tier 4** | **Unverified / synthetic** | SEO content farms, AI-generated summary sites, anonymous social media posts, scraped wiki mirrors, unsourced marketing copy | **Disqualified.** If a claim appears only in Tier 4 sources, mark it `Unverifiable` or `Refuted`. |

### Verdict taxonomy

| Verdict | Definition |
| :--- | :--- |
| **`Verified`** | Directly entailed by Tier 1 (or corroborated Tier 2) evidence with no material omissions. |
| **`Refuted`** | Directly contradicted by authoritative primary evidence, mathematical calculation, or code/test execution. |
| **`Mixed / Needs Context`** | Contains a literally true fact or statistic, but omits essential baseline context, cherry-picks an unrepresentative subset, or pairs a true clause with a false implication. |
| **`Outdated`** | Was accurate at an earlier date or software version, but is superseded by current primary sources. |
| **`Disputed`** | Credible Tier 1 or Tier 2 sources actively disagree (e.g., competing peer-reviewed studies or unresolved methodology disputes) with no settled consensus. |
| **`Unverifiable`** | No Tier 1 or Tier 2 evidence exists to confirm or refute the claim after exhaustive search. Separate *absence of evidence* (`Unverifiable`) from *evidence of absence* (`Refuted`). |

### Citation entailment rules

1. **Session-verified URLs only**: Cite only URLs and file paths retrieved and inspected via tool calls during the current session. Never reconstruct a URL or DOI from memory.
2. **Mandatory verbatim excerpt**: Pair every citation with the exact quote, figure, or table row from the source that entails or contradicts the claim. A page that merely discusses the same topic without proving the specific claim does not qualify as a supporting citation.
3. **Explicit provenance**: State the institution/author and publication date (or software version) on every citation so temporal drift is immediately visible.
