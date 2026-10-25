---
name: fact-check
description: Deep-research and verify factual accuracy against primary sources. Use when investigating whether a topic, claim, or rumour is true, auditing a document, draft, file, or URL for factual errors and citation entailment, or stress-testing a prior statement in the conversation.
license: MIT
---

# Fact Check

Verify claims by splitting the target into **atomic claims**, testing each with primary-source and **falsification queries**, and tracing every report back to its **Tier 1 source**.

## Environment adaptation

- **Chat** (Claude Desktop, web): verify with web search, URL fetching, and any attached documents or images, inline.
- **Code and CLI**: combine web search with local inspection (`grep`, file reads, `git log`), shell or Python for quantitative checks, and test runs. For **4 or more claims** or a broad topic, dispatch parallel verification subagents when the harness supports them; handle 1 to 3 inline.

## Plain-language output

The bolded terms in this skill (atomic claims, Tier 1 to Tier 4, falsification, citogenesis, entailment) are your working vocabulary. Everything the user sees, including interview questions and the report, speaks everyday language a non-specialist understands on first read:

- Print the **user-facing label** from the table below wherever an internal term would appear.
- Keep step, tier, and section names from this skill internal: describe the work by what it does (*"checking the original study"*, not *"Step 4: trace to Tier 1"*).
- When a technical term is unavoidable (a study type, a filing name), explain it in a short clause the first time it appears.

| Internal term | User-facing label |
| :--- | :--- |
| Atomic claim | Claim |
| Citogenesis | Many outlets repeating one unchecked source |
| Tier 1 source | Original source (the official document, dataset, study, or recording itself) |
| Tier 2 source | Trusted secondhand source (a reputable fact-checker, newsroom, or review that cites the original) |
| Tier 3 / Tier 4 source | Lead only / Unreliable source |
| Falsification query | Search for counter-evidence |
| Citation entailment | The quote that proves it |

## Interview rounds

Interview the user in rounds before researching, so the check answers the question they actually care about.

1. Ask at least one round on every run. Skip only when the user says "just answer", "no questions", or equivalent; then state your assumptions in one line at the top of the report.
2. The **frontier** is every open question whose prerequisites are settled. Ask the whole frontier in one round, number each question, give your recommended answer, and word it so "yes" accepts the recommendation. Then stop and wait.
3. Find facts yourself (web search, the attached document, history, memory). Ask only for decisions, preferences, and facts only the user knows. Never ask about anything the user already stated; turn what you only inferred into a quick confirmation.
4. Recompute the frontier after each answer. A question that depends on another open question belongs to a later round.
5. "Yes", "idk", or a skipped question accepts your recommendation. When the user hands you the choice ("you decide", "whatever you think"), adopt your recommendations for every open question, list them as assumptions, and start without another round.
6. When the frontier is empty, summarize the settled answers in 2 to 4 bullets and ask "Ready for me to start?" Begin once the user confirms.

Copy this format exactly, keeping the ❓ and ➡️ markers and the `---` line between questions:

```
❓ **Q1** - **<short title>**: <question in everyday words, with options when useful>

➡️ <your recommended answer>

---

❓ **Q2** - **<short title>**: <question in everyday words, with options when useful>

➡️ <your recommended answer>
```

## Domain playbooks

**Before Step 3**, when a claim falls in one of these domains, read its section of [`references/domain-playbooks.md`](references/domain-playbooks.md): software, APIs, and benchmarks; science, medicine, and papers; economics, finance, and statistics; or quotes, history, and viral media.

## Verification sequence

Run these six steps in order.

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

### Step 2: Interview the user on scope and purpose

Run **Interview rounds** on these verdict-shaping questions, showing the numbered claim list from Step 1 in plain wording so the user can react to it:

- **Scope**: which claims to check (all of them, or the ones that matter most to the user).
- **Meaning**: which interpretation the user means wherever Step 1 found an ambiguous claim.
- **Time and place frame**: "true as of when, and where" for claims that vary by date, version, or country.
- **Purpose and depth**: what the user will do with the answer (settle a debate, share a post, publish a piece, make a health or money decision), which sets how deep to dig and how to frame the report.

**Completion criterion**: The user has confirmed the settled scope, meaning, time frame, and purpose (or explicitly opted out of questions, with assumptions stated), and the atomic claim list reflects their answers.

### Step 3: Triangulate and falsify

Route each atomic claim to the tool that owns its ground truth:

- **Code or repository claims**: inspect the files, git history, or run the test or command.
- **Math and statistics**: compute exact figures in Python or shell, or write the arithmetic out step by step.
- **World, documentation, or literature claims**: run **paired queries** for every claim:
  1. **Neutral primary-source query**, stripped of presuppositions (`"Bun vs Node.js HTTP throughput methodology"`, not `"Why Bun is 4x faster"`), aimed at official docs, specs, filings, or datasets.
  2. **Falsification query** for counter-evidence (`"<claim>" errata OR deprecated OR criticism OR limitation OR retraction`).
  3. **Temporal anchor**: the year, date, or version in queries for time-sensitive facts.

**Completion criterion**: Every atomic claim in scope has been tested by both a primary-source retrieval pass and an explicit falsification pass (or direct local tool execution for code and math).

### Step 4: Read laterally and trace to Tier 1

Defeat **citogenesis** (circular reporting where multiple secondary blogs or news outlets repeat the same unsourced claim):

- **Trace to the root node**: five articles citing the same press release, blog post, or unnamed study count as a single unverified thread. Follow hyperlinks, footnotes, DOIs, and named studies backward until you inspect the **Tier 1 primary source** directly.
- **Read laterally**: when a claim rests on an unfamiliar domain, organization, benchmark author, or study, run an external search about the source itself (`"<source or author>" funding OR reputation OR criticism OR conflict of interest`) rather than reading the page's self-authored "About" section.
- Grade every source against the **Source hierarchy** below. When a search surfaces Wikipedia or another Tier 3 page, open the reference it footnotes for that fact and cite that; if none opens, cite Britannica or a newsroom of record.

**Completion criterion**: Every atomic claim's evidence chain terminates at a verified **Tier 1** primary source, or explicitly records why Tier 1 is inaccessible and documents independent **Tier 2** corroboration.

### Step 5: Assign calibrated verdicts

Assign each atomic claim one categorical label from the **Verdict taxonomy** below (`Verified`, `Refuted`, `Mixed / Needs Context`, `Outdated`, `Disputed`, or `Unverifiable`), paired with the highest source tier verified (`Tier 1` or `Tier 2`). Never invent confidence percentages.

**Completion criterion**: Every atomic claim in scope carries one categorical verdict and its verified source tier.

### Step 6: Report in plain language

Render the report inline in plain language, in three sections (write a file only when the user asks):

1. **Bottom Line**:
   - **Scorecard**: `X of Y claims hold up`, plus how many came out `Refuted`, `Mixed / Needs Context`, `Outdated`, `Disputed`, or `Unverifiable`.
   - **Summary**: 2 to 3 sentences on what holds up, what fails, and the most important context discovered, framed for the purpose the user gave in Step 2.
2. **Claim by Claim**:
   For each numbered claim:
   - **Claim**: the claim spelled out in full (plus the original quote and its location when checking a text).
   - **Verdict**: the verdict label word for word, then how strong the backing is in plain words: "checked against the original source" or "based on trusted secondhand reporting; the original was not reachable".
   - **Why**: a short explanation of what the source shows, including anything the search for counter-evidence turned up.
   - **Source**: `[Source Title, Author/Org (YYYY-MM-DD or Version)](URL)` followed by **the exact quote that proves it** (or the exact file and line range `[file.ext](file:///path#L10-L20)` for local code).
3. **Suggested Fixes** (include whenever any claim is `Refuted`, `Mixed / Needs Context`, or `Outdated`):
   - Provide exact, ready-to-paste replacement text that fixes the error or adds the missing context.

**Completion criterion**: Every claim in scope appears in Claim by Claim with a session-verified URL, date/version, plain-language source strength, and verbatim excerpt; no proof link is Wikipedia or another Tier 3 page; every flawed claim has a suggested fix; and the report reads cleanly to a non-specialist with every internal term from **Plain-language output** replaced by its user-facing label.

---

## Reference rules

### Source hierarchy

| Tier | Category | Examples | Evidentiary role |
| :--- | :--- | :--- | :--- |
| **Tier 1** | **Primary** | Official specs and docs (RFCs, W3C, vendor docs for their own API), source code and git history, peer-reviewed studies, court transcripts, `10-K`/`8-K` filings, government datasets (BLS, Census, WHO), primary recordings | **Terminal proof** within its domain. |
| **Tier 2** | **High-trust secondary** | IFCN-signatory fact-checks, newsrooms of record citing named sources, systematic reviews and meta-analyses, authoritative textbooks and edited encyclopedias (Britannica) | **Corroboration**, or fallback when Tier 1 is unreachable (say so explicitly). |
| **Tier 3** | **Community** | Wikipedia, Stack Overflow, GitHub issues, personal blogs, press releases | **Discovery only** (see Step 4), never the proof. |
| **Tier 4** | **Unverified / synthetic** | Content farms, AI summary sites, anonymous posts, scraped mirrors, unsourced marketing | **Disqualified**: a claim found only here is `Unverifiable` or `Refuted`. |

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
