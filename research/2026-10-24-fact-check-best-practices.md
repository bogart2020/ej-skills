# Deep Research & Fact-Checking Skill Best Practices: Primary-Source Synthesis

**Date:** 2026-10-24  
**Repository:** `ej-skills`  
**Scope:** Journalistic fact-checking standards, LLM/agentic fact-verification pipelines, and cross-platform AI skill/plugin packaging specifications.

---

## Executive Summary

Building a high-precision **Fact-Checking & Deep-Research Skill** for coding and research agents requires combining two bodies of work that rarely talk to each other:

1. **Human Journalistic & Information-Literacy Standards** — the **IFCN Code of Principles**, the Stanford History Education Group (**SHEG**) empirical research on **lateral reading**, Mike Caulfield's **SIFT** methodology, and **Schema.org `ClaimReview`** structured data.
2. **Automated LLM Factuality Pipelines** — atomic claim extraction and decontextualization (**FActScore**, **Google DeepMind SAFE**, **Microsoft Claimify**, **FacTool**), Popperian **falsification search query formulation**, **anti-citogenesis** primary-source tracing, multi-class epistemic verdict taxonomies (**FEVER**, **AVeriTeC**), and strict **citation entailment hygiene** (**ALCE**).

Finally, to ship cleanly across **Claude Code, Claude Desktop, OpenAI Codex, GitHub Copilot CLI/VS Code, Google Antigravity (AGY), Gemini CLI, Cursor, and Windsurf**, the repository should follow a unified flat `skills/<skill-name>/SKILL.md` architecture paired with both `.claude-plugin/` manifests and a root Antigravity `plugin.json`.

---

## 1. Journalistic & Human Fact-Checking Standards

### 1.1 IFCN Code of Principles (Poynter Institute)

Launched in 2016 by the **International Fact-Checking Network (IFCN)** at the Poynter Institute, the **Code of Principles** is the global benchmark for professional fact-checking organizations ([IFCN Code of Principles](https://ifcncodeofprinciples.poynter.org/know-more/the-commitments-of-the-code-of-principles); [Poynter IFCN](https://www.poynter.org/ifcn/)).

Three of its five core commitments translate directly into architectural invariants for an AI fact-checking agent:

| IFCN Principle | Human Organization Standard | Agentic Skill Equivalent |
| :--- | :--- | :--- |
| **1. Nonpartisanship and Fairness** | Evaluate all claims using the same evidence standard regardless of speaker; do not cherry-pick claims from one side or advocate policy positions ([IFCN Commitments](https://ifcncodeofprinciples.poynter.org/know-more/the-commitments-of-the-code-of-principles)). | Apply identical decomposition, primary-source requirements, and falsification queries to every claim in a document or user prompt—including the user's own premises and the agent's prior outputs. |
| **2. Transparency of Sources** | Identify and link all sources in enough detail that a reader can independently replicate the verification ([IFCN Commitments](https://ifcncodeofprinciples.poynter.org/know-more/the-commitments-of-the-code-of-principles)). | Provide the exact canonical URL, document title, author/institution, publication/revision date, and a verbatim quote/excerpt for every verified or refuted claim. Never rely on unlinked parametric memory. |
| **4. Transparency of Methodology** | Explain the exact criteria and methodology used to select, research, and rate claims ([IFCN Commitments](https://ifcncodeofprinciples.poynter.org/know-more/the-commitments-of-the-code-of-principles)). | Expose the step-by-step verification trail: the extracted atomic claims, the supporting and falsification search queries executed, the source tier evaluation, and the explicit reasoning behind each verdict label. |
| **5. Open and Honest Corrections** | Publish clear corrections when new evidence emerges or errors are found ([IFCN Commitments](https://ifcncodeofprinciples.poynter.org/know-more/the-commitments-of-the-code-of-principles)). | Explicitly flag when an earlier statement in the conversation, codebase, or draft is contradicted by newly retrieved primary evidence rather than silently smoothing over the discrepancy. |

### 1.2 SHEG "Lateral Reading" vs. Vertical Reading

In a landmark empirical study at the **Stanford History Education Group (SHEG)** (now the Digital Inquiry Group), Sam Wineburg and Sarah McGrew compared how PhD historians, Stanford undergraduates, and professional fact-checkers evaluated unfamiliar digital sources:

- **Primary Source:** Sam Wineburg & Sarah McGrew (2019), *"Lateral Reading and the Nature of Expertise: Reading Less and Learning More When Evaluating Digital Information"*, *Teachers College Record*, Vol. 121, Issue 11, pp. 1–40 ([DOI: 10.1177/016146811912101102](https://doi.org/10.1177/016146811912101102); [Stanford Digital Inquiry Group](https://cor.inquirygroup.org/)).
- **Core Finding:** PhD historians and university students frequently failed to detect front groups and biased advocacy sites because they read **vertically**—staying on the target webpage, inspecting its visual polish, `.org` domain suffix, self-authored "About Us" page, and internal bibliography. Professional fact-checkers did the opposite: within seconds, they left the page (**lateral reading**), opened new search tabs, and queried independent sources to learn *who funded, authored, and critiqued* the site before reading its claims.
- **Implication for AI Agents:** When an AI agent fetches a webpage via a URL or search snippet, it naturally defaults to **vertical reading** (feeding the page's text into context and trusting the page's self-description). A fact-checking skill must mandate **agentic lateral reading**: when encountering an unfamiliar domain, author, benchmark, or organization, the agent must run an external search query about the source itself (`"<domain or author>" reputation OR funding OR criticism OR retraction`) rather than trusting the page's own "About" text.

### 1.3 Mike Caulfield's SIFT Method

Digital literacy researcher **Mike Caulfield** (University of Washington Center for an Informed Public) distilled SHEG's lateral-reading findings into four actionable moves called **SIFT**:

- **Primary Source:** Mike Caulfield (2019), *"SIFT (The Four Moves)"*, Hapgood ([https://hapgood.us/2019/06/19/sift-the-four-moves/](https://hapgood.us/2019/06/19/sift-the-four-moves/)) and *Check, Please! Starter Course* ([ Pressbooks](https://webliteracy.pressbooks.com/chapter/four-strategies/)).
- **The Four Moves Mapped to Agent Execution:**
  1. **S — Stop:** Do not immediately accept a claim or synthesize a single search result into an answer. Separate the *claim* from the *evidence*. Check whether the claim is checkworthy (an objective, falsifiable proposition rather than pure subjective opinion).
  2. **I — Investigate the Source:** Before relying on a retrieved source, identify what kind of source it is (primary specification/data vs. secondary blog/aggregator) and its incentives or biases.
  3. **F — Find Better Coverage:** If the initial source is low-tier (e.g., a social media post, forum thread, content-marketing blog, or secondary news summary), do not stop there—search laterally for consensus across high-trust, independent outlets or domain authorities.
  4. **T — Trace Claims, Quotes, and Media to the Original Context:** Follow hyperlinks, footnotes, DOI numbers, and named studies backward until reaching the **primary source** (the original paper, official API documentation, court filing, dataset, or full transcript). Verify that the primary source actually supports the claim in its original context and was not stripped of caveats.

### 1.4 `schema.org/ClaimReview` Data Structure

The **`ClaimReview`** schema is the open W3C/Schema.org vocabulary used by fact-checkers and major search engines to structure fact-checking assessments:

- **Primary Sources:** Schema.org [`ClaimReview` Specification](https://schema.org/ClaimReview), Schema.org [`Claim` Specification](https://schema.org/Claim), and Google Search Central [Fact Check (`ClaimReview`) Structured Data Documentation](https://developers.google.com/search/docs/appearance/structured-data/factcheck).
- **Key Structural Fields:**
  - `claimReviewed` (`Text`): A concise, neutral restatement of the specific atomic claim being evaluated.
  - `itemReviewed` (`Claim`):
    - `author`: The person, organization, or document making the claim.
    - `datePublished`: When the original claim was made (crucial for temporal verification).
    - `appearance` / `firstAppearance`: Where the claim appears in the input text or external URL.
  - `reviewRating` (`Rating`):
    - `alternateName`: The human-readable categorical verdict (e.g., `Verified`, `Refuted`, `Needs Context`).
    - `ratingValue` / `bestRating` / `worstRating`: Standardized ordinal scale when machine-readable scoring is requested.
  - `author` & `datePublished`: The verifier identity and date of verification (anchoring when sources were checked).

Borrowing `ClaimReview`'s separation between **`itemReviewed` (the claim + its original context/date)** and **`reviewRating` (the verdict + primary evidence)** ensures every fact-check entry in a Markdown report is self-contained and auditable.

---

## 2. LLM & Agentic Fact-Checking Pipelines

Modern NLP and agentic research converge on a multi-stage **"Decompose → Decontextualize → Retrieve (Pro & Contra) → Trace to Primary → Verify"** pipeline.

### 2.1 Atomic Claim Decomposition & Decontextualization

Evaluating a multi-clause sentence or paragraph in a single pass causes LLMs to miss subtle fabrications embedded alongside true statements ("halo effect") or fail to retrieve specific evidence. Four foundational papers define best practices for claim decomposition:

#### A. FActScore (Min et al., EMNLP 2023)
- **Primary Source:** Sewon Min, Kalpesh Krishna, Xinxi Lyu, Mike Lewis, Wen-tau Yih, Pang Wei Koh, Mohit Iyyer, Luke Zettlemoyer, & Hannaneh Hajishirzi (2023), *"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation"*, *Proceedings of EMNLP 2023* ([arXiv:2305.14251](https://arxiv.org/abs/2305.14251); [ACL Anthology: 2023.emnlp-main.741](https://aclanthology.org/2023.emnlp-main.741/); [GitHub: shmsw25/FActScore](https://github.com/shmsw25/FActScore)).
- **Core Mechanism:** Breaks long-form text into **atomic facts**—short sentences that each convey a single piece of information—and evaluates each atomic fact independently against a knowledge source:
  $$\text{FActScore} = \frac{\text{Number of supported atomic facts}}{\text{Total number of atomic facts}}$$
- **Lesson for Skill Design:** A compound sentence like *"React 19, released in December 2024 by Meta, removed `forwardRef` entirely"* contains three distinct atomic claims: (1) React 19 was released by Meta, (2) React 19 was released in December 2024, and (3) React 19 removed `forwardRef` entirely (in reality, React 19 made `ref` a standard prop and deprecated `forwardRef` for future removal, rather than removing it immediately). Without atomic splitting, an agent often marks the whole sentence "True" because the first two clauses match search snippets.

#### B. Google DeepMind SAFE — Search-Augmented Factuality Evaluator (Wei et al., 2024)
- **Primary Source:** Jerry Wei, Chengrun Yang, Xinying Song, Yifeng Lu, Nathan Hu, Jie Huang, Dustin Tran, Daiyi Peng, Ruibo Liu, Da Huang, Cosmo Du, & Quoc V. Le (2024), *"Long-form factuality in large language models"*, Google DeepMind ([arXiv:2403.18802](https://arxiv.org/abs/2403.18802); [GitHub: google-deepmind/long-form-factuality](https://github.com/google-deepmind/long-form-factuality)).
- **Core Mechanism:** SAFE turns an LLM into an open-web fact-checking agent through four explicit steps:
  1. **Split into individual facts:** Prompt the model to break each sentence into independent atomic facts.
  2. **Revise to be self-contained (Decontextualization):** Rewrite each extracted fact so that pronouns (`it`, `they`, `this paper`), relative dates (`last year`), and shorthand references are replaced with explicit canonical entity names from the surrounding paragraph.
  3. **Checkworthiness Filtering:** Classify each atomic fact as *Relevant/Checkworthy* vs. *Irrelevant/Subjective* (filtering out greetings, transitional phrases, or pure tautologies).
  4. **Iterative Multi-Step Google Search:** For each checkworthy fact, run up to $N$ rounds of search query generation, reasoning over prior search results to formulate follow-up queries before rendering a final judgment.
- **Empirical Result:** Across ~16,000 human-annotated facts, SAFE agreed with crowdsourced human annotators 72% of the time, and on a random sample of 100 disagreements, **SAFE was right 76% of the time** while costing >20x less ([arXiv:2403.18802](https://arxiv.org/abs/2403.18802)).

#### C. Microsoft Claimify (Metropolitansky & Larson, 2025)
- **Primary Source:** Dasha Metropolitansky & Jonathan Larson (2025), *"Towards Effective Extraction and Evaluation of Factual Claims"*, Microsoft Research ([arXiv:2502.10855](https://arxiv.org/abs/2502.10855)).
- **Core Mechanism:** Identifies critical failure modes in naive atomic decomposition (e.g., extracting subjective opinions as "facts", losing essential qualifiers like *"might"* or *"in some cases"*, or hallucinating disambiguations). Claimify enforces a strict four-stage extraction pipeline:
  1. **Sentence Splitting & Context Windowing:** Supply surrounding sentences as context for every target sentence.
  2. **Selection:** Isolate sentences that contain at least one verifiable factual proposition; discard purely subjective or speculative sentences.
  3. **Disambiguation:** Resolve linguistic ambiguity (referential pronouns and structural ambiguity) *only* when the surrounding context provides a single unambiguous interpretation; otherwise flag the claim as **ambiguous** rather than guessing.
  4. **Decomposition & Decontextualization:** Extract self-contained factual claims that preserve necessary scope modifiers, hedges, and causal links (so *"X caused Y"* is not flattened into two disconnected claims *"X happened"* and *"Y happened"* without the causal claim *"X caused Y"*).

#### D. FacTool — Tool-Augmented Multi-Domain Verification (Chern et al., 2023)
- **Primary Source:** I-Chun Chern, Steffi Chern, Shiqi Chen, Weizhe Yuan, Kehua Feng, Chunting Zhou, Junxian He, Graham Neubig, & Pengfei Liu (2023), *"FacTool: Factuality Detection in Generative AI — A Tool Augmented Framework for Multi-Task and Multi-Domain Scenarios"* ([arXiv:2307.13528](https://arxiv.org/abs/2307.13528); [GitHub: GAIR-NLP/factool](https://github.com/GAIR-NLP/factool)).
- **Core Mechanism:** Demonstrates that web search alone is insufficient for all factual claims. FacTool routes extracted claims to the **appropriate verification tool by domain**:
  - **General & Current Events Claims:** Web search API (`search_web`).
  - **Code & Repository Claims:** Local codebase search (`grep`, `read_file`), AST/compiler checks, or test execution (`run_command`).
  - **Mathematical / Quantitative Claims:** Python / shell calculator execution (`run_command` with `python3 -c ...`) to verify percentages, growth rates, and arithmetic.
  - **Academic / Scientific Literature Claims:** Academic index queries (DOI lookup, arXiv, Semantic Scholar, Google Scholar) to verify paper existence, author lists, publication years, and actual findings.

### 2.2 Search Query Formulation: Falsification, Neutral Expansion & Temporal Anchoring

When an agent translates an atomic claim directly into a search query, it suffers from **affirmative confirmation bias**: searching `"Does X improve Y"` or `"Why X is faster than Y"` biases search engines toward marketing pages and blog posts that affirm the premise.

To eliminate confirmation bias in retrieval:

1. **Neutral Baseline Queries (Metric/Entity-First):**
   - Strip presuppositions and adjectives from the claim.
   - *Bad (Biased):* `"Why Bun is 4x faster than Node.js"`
   - *Good (Neutral):* `"Bun vs Node.js benchmark throughput latency methodology"`
2. **Primary-Source Targeted Queries:**
   - Target official documentation domains, standards bodies, filings, or primary repositories.
   - Example: `"site:react.dev forwardRef React 19"` or `"arXiv 2403.18802 SAFE Wei"`.
3. **Adversarial / Falsification Queries (Popperian Testing):**
   - Explicitly search for evidence that would *refute, limit, or qualify* the claim:
   - Example: `"<claim topic>" debunked OR retraction OR errata OR criticism OR limitation OR false`.
   - Contrastive retrieval ensures the verifier weighs both supporting and refuting evidence before assigning a verdict.
4. **Temporal Anchoring:**
   - Many claims are true at time $t_1$ and false at time $t_2$. Every search query for time-sensitive facts (versions, laws, market share, pricing, leadership, APIs) must anchor both the **claim's reference date** and the **current date/version**.

### 2.3 Source Hierarchy & Primary-Source Tracing (Anti-Citogenesis)

A critical failure mode in web-based fact-checking is **circular reporting**—popularized by Randall Munroe as **"citogenesis"** (*xkcd* #978, ["Citogenesis"](https://xkcd.com/978/); see also Wikipedia's documentation on [Circular reporting](https://en.wikipedia.org/wiki/Circular_reporting)). In citogenesis, an unsourced claim on a wiki, forum, or AI-generated blog is repeated by several secondary outlets; a naive fact-checker sees 5–10 websites stating the same thing and marks the claim "Verified," mistaking **repetition** for **independent corroboration**.

An AI fact-checking skill must enforce two rules:

1. **Independence Rule (Anti-Citogenesis):** Multiple secondary articles citing the same underlying press release, study, or unnamed rumor count as **one (or zero) primary sources**, never as independent corroboration. Always trace the citation graph back to the root node.
2. **Explicit 4-Tier Source Hierarchy:**

| Tier | Source Category | Examples | Allowed Usage in Fact-Checking |
| :--- | :--- | :--- | :--- |
| **Tier 1: Primary & Authoritative** | Original artifacts that *own* the fact | Official technical docs/specs (RFCs, W3C, MDN), source code & git commit history, peer-reviewed empirical studies, court transcripts, SEC/regulatory filings (`10-K`, `8-K`), official government statistical releases (BLS, Census, WHO), verbatim primary recordings. | **Terminal proof.** Sufficient to verify or refute a claim within its domain. |
| **Tier 2: High-Trust Secondary** | Vetted, accountable synthesis with transparent sourcing | IFCN-signatory fact-checks, established newsrooms of record citing named sources, peer-reviewed systematic reviews/meta-analyses, authoritative textbooks. | **Corroborating proof**, or fallback proof when Tier 1 is inaccessible (must explicitly note whether Tier 1 was directly inspected). |
| **Tier 3: Community & Tertiary** | Useful indices or practitioner reports without editorial auditing | Wikipedia articles, Stack Overflow answers, GitHub issue comments, personal engineering blogs, corporate press releases (for non-self-descriptive claims). | **Discovery only.** Use Wikipedia or blogs to *locate* the Tier 1 footnote/link, then verify the Tier 1 source directly. Corporate blogs are Tier 1 *only* for claims about the company's own product releases/announcements, not for competitor comparisons. |
| **Tier 4: Low-Trust / Disqualified** | Unaccountable, circular, or synthetic content | SEO content farms, AI-generated summary sites, anonymous social media posts, scraped wiki mirrors, unverified marketing copy. | **Never cite as evidence.** If a claim *only* appears in Tier 4 sources, the verdict is `Unverifiable` or `Refuted`. |

### 2.4 Verdict Taxonomy & Epistemic Calibration

Binary (`True` / `False`) fact-checking forces false precision on complex real-world claims:

- **FEVER** (Thorne et al., NAACL 2018, *"FEVER: a Large-scale Dataset for Fact Extraction and VERification"*, [arXiv:1803.05355](https://arxiv.org/abs/1803.05355); [ACL Anthology: N18-1074](https://aclanthology.org/N18-1074/)) established the classic 3-way NLP NLI taxonomy: `SUPPORTED`, `REFUTED`, and `NOT ENOUGH INFO`.
- **AVeriTeC** (Schlichtkrull et al., NeurIPS 2023, *"AVeriTeC: A Dataset for Real-world Claim Verification with Evidence from the Web"*, [arXiv:2305.13117](https://arxiv.org/abs/2305.13117)) showed that open-web claims require a fourth category: **`Conflicting Evidence / Cherry-picking`**, because real-world misinformation frequently uses cherry-picked true numbers stripped of baseline context, or touches areas where reliable sources genuinely conflict.

Combining `FEVER`, `AVeriTeC`, and `ClaimReview` yields a calibrated **6-level Verdict Taxonomy** for an agentic fact-checking skill:

1. **`Verified` (`Supported`)**: Directly entailed by Tier 1 (or corroborated Tier 2) primary evidence with no material omissions.
2. **`Refuted` (`Contradicted`)**: Directly contradicted by authoritative primary evidence, mathematical calculation, or code execution.
3. **`Mixed / Needs Context` (`Cherry-Picked` / `Partially True`)**: Contains a kernel of factual truth (or a literally true statistic) but omits essential caveats, cherry-picks an unrepresentative subset, or combines a true premise with a false sub-clause.
4. **`Outdated` (`Stale / Superseded`)**: Was factually accurate at an earlier date or software version, but is no longer true as of current primary sources.
5. **`Disputed` (`Conflicting Evidence`)**: Credible Tier 1/Tier 2 sources actively disagree (e.g., competing peer-reviewed studies or unresolved methodology disputes), with no settled consensus.
6. **`Unverifiable` (`Insufficient Evidence`)**: No Tier 1 or Tier 2 sources exist to confirm or refute the claim after exhaustive search (preventing the agent from conflating *"absence of evidence"* with *"evidence of absence"*).

> **Epistemic Calibration Guardrail:** Avoid inventing pseudo-quantitative confidence percentages (e.g., `"83% confident"` or `"Truth Score: 74/100"`) for individual claims unless computing an explicit corpus-level FActScore fraction ($\text{Supported} / \text{Total Atomic Claims}$). Instead, state the **categorical verdict** and the **source tier** of the supporting evidence.

### 2.5 Citation Hygiene & Anti-Hallucination Rules

In **ALCE (Automatic LLMs' Citation Evaluation)**, Tianyu Gao, Howard Yen, Jiatong Yu, and Danqi Chen (EMNLP 2023, *"Enabling Large Language Models to Generate Text with Citations"*, [arXiv:2305.14627](https://arxiv.org/abs/2305.14627); [ACL Anthology: 2023.emnlp-main.398](https://aclanthology.org/2023.emnlp-main.398/)) demonstrated that LLMs generating citations frequently suffer from two failures:
1. **Hallucinated / Dead URLs:** Synthesizing plausible-looking URLs or DOIs from parametric memory.
2. **Non-Entailing Citations (Low Citation Precision):** Citing a real URL that discusses the general topic but does *not* actually contain or entail the specific claim made.

To prevent both failures, a fact-checking skill must enforce **Three Citation Hygiene Laws**:
1. **Zero Parametric URLs:** Never emit a URL that was not directly observed in a tool output (`search_web`, `read_file`, etc.) during the current session.
2. **Mandatory Verbatim Excerpt / Quote:** Every citation attached to a verdict must include a short, direct quote or exact figure extracted from the source (or an exact file path + line range `[file.ts](file:///path/to/file.ts#L10-L20)` for local code claims) demonstrating that the source actually entails or refutes the claim.
3. **Provenance Metadata:** Include the source organization/author and publication Date/Version alongside the link so the reader can immediately judge currency and authority.

---

## 3. Cross-Platform AI Skill & Plugin Standards

To make `ej-skills` installable and native across **Claude Code, Claude Desktop, OpenAI Codex, GitHub Copilot CLI & VS Code, Google Antigravity (AGY), Gemini CLI, Cursor, Windsurf, OpenCode, and Amp (`skills.sh`)**, we must align three specifications:
1. The **Agent Skills Open Standard (`agentskills.io`)**
2. The **Claude Code / Codex / Copilot / `skills.sh` conventions** (documented in install-block.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/install-block.md`) and invocation.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/invocation.md`))
3. The **Google Antigravity (AGY) Plugin & Skill specification** (documented in plugin/SKILL.md (`~/.gemini/antigravity/builtin/skills/plugin/SKILL.md`) and agy-customizations/SKILL.md (`~/.gemini/antigravity/builtin/skills/agy-customizations/SKILL.md`))

### 3.1 The `agentskills.io` Open Standard (`SKILL.md`)

- **Primary Source:** Agent Skills Specification ([https://agentskills.io/specification](https://agentskills.io/specification); [https://agentskills.io](https://agentskills.io)).
- **Directory Structure:**
  ```text
  skills/<skill-name>/
  ├── SKILL.md              # Required: YAML frontmatter + Markdown instructions
  ├── agents/
  │   └── openai.yaml       # Recommended: OpenAI Codex UI metadata & invocation policy
  ├── references/           # Optional: Deep reference docs loaded on demand
  ├── scripts/              # Optional: Helper scripts
  └── assets/               # Optional: Templates or static assets
  ```
- **Progressive Disclosure Architecture:**
  1. **Discovery (~100 tokens/skill):** At startup, harnesses load only `name` and `description` from each `SKILL.md` frontmatter.
  2. **Activation:** When triggered (by user `/skill-name` or model auto-invocation), the harness loads the `SKILL.md` body.
  3. **Execution:** Accompanying files in `references/` or `scripts/` are read/executed only when explicitly needed.
- **`SKILL.md` Frontmatter Schema:**

| Field | Required? | Standard / Harness | Constraints & Purpose |
| :--- | :--- | :--- | :--- |
| `name` | **Yes** | `agentskills.io` (All) | Max 64 chars; lowercase `a-z`, `0-9`, and hyphens (`-`). Must match the parent folder name (`skills/<name>/SKILL.md`). |
| `description` | **Yes** | `agentskills.io` (All) | Max 1024 chars. For model-invoked skills, include explicit trigger phrases (*"Use when the user asks to fact-check, verify claims, audit citations..."*). |
| `disable-model-invocation` | Optional | Claude Code | Boolean (`true`/`false`, default `false`). Set to `true` only if the skill should *never* be auto-invoked by the model (invocation.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/invocation.md`)). |
| `user-invocable` | Optional | Claude Code | Boolean (`true`/`false`, default `true`). Controls whether `/skill-name` appears in the user slash-command menu. |
| `argument-hint` | Optional | Claude Code | Short placeholder shown in slash-command autocomplete (e.g., `[file, URL, or claim]`). |
| `license` | Optional | `agentskills.io` | SPDX license identifier (e.g., `MIT`). |
| `compatibility` | Optional | `agentskills.io` | Max 500 chars describing tool/environment requirements (e.g., web search tool access). |
| `metadata` | Optional | `agentskills.io` | Key-value string map (e.g., `author`, `version`). |

### 3.2 Model-Invoked vs. User-Invoked Conventions & `agents/openai.yaml`

Per invocation.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/invocation.md`):

- **Model-Invoked Skills (Recommended for `fact-check`):**
  - Reachable **both** by the human typing `/fact-check` **and** autonomously by the model when the user says *"fact-check this article"*, *"verify the claims in this PR/doc"*, or *"are these citations real?"*.
  - Omit `disable-model-invocation` from `SKILL.md` (or leave default) so the model can reach for it autonomously.
  - Write a rich, model-facing `description` with explicit trigger phrases (`"Use when..."`).
  - Include `skills/<skill-name>/agents/openai.yaml` alongside `SKILL.md` for OpenAI Codex skill-picker support:
    ```yaml
    interface:
      display_name: "Fact Check"
      short_description: "Verify claims against primary sources"
    ```
- **User-Invoked-Only Skills:**
  - If a skill is strictly user-invoked, set `disable-model-invocation: true` in `SKILL.md` **and** `policy.allow_implicit_invocation: false` in `agents/openai.yaml`, keeping both harnesses in sync (invocation.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/invocation.md`)).
- **Inter-Skill Dependencies:**
  - Express dependencies between skills by instructing the agent to `Call the Skill tool with "<skill-name>"`, never via fragile `../other-skill/FILE.md` relative path imports (invocation.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/invocation.md`)).

### 3.3 Unified Multi-Platform Repository Layout for `ej-skills`

A critical insight from install-block.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/install-block.md`) and plugin/SKILL.md (`~/.gemini/antigravity/builtin/skills/plugin/SKILL.md`) is that **a flat `skills/<skill-name>/SKILL.md` directory layout** satisfies *every* major agent ecosystem simultaneously without needing nested bucket workarounds:

1. **Google Antigravity (AGY):** Expects a root `plugin.json` and `skills/<skill>/SKILL.md` (plugin/SKILL.md (`~/.gemini/antigravity/builtin/skills/plugin/SKILL.md`)).
   - *Important AGY Constraint:* Root `plugin.json` must **only** use AGY's supported top-level keys (`name`, `displayName`, `version`, `description`, `logo`, `suggestedPrompts`, `disabled`). Do not put `author` or `homepage` in root `plugin.json`, as AGY's loader discards unknown fields (plugin/SKILL.md (`~/.gemini/antigravity/builtin/skills/plugin/SKILL.md`)).
2. **Claude Code, OpenAI Codex, GitHub Copilot CLI, and VS Code:** Read `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (install-block.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/install-block.md`), .claude-plugin/plugin.json (`~/.gemini/config/vendor/mattpocock-skills/.claude-plugin/plugin.json`), .claude-plugin/marketplace.json (`~/.gemini/config/vendor/mattpocock-skills/.claude-plugin/marketplace.json`)).
   - `.claude-plugin/plugin.json` can include `name`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`, and `"skills": ["./skills/fact-check"]`.
3. **Gemini CLI:** `gemini skills install <repo-url> --path skills` works in a single command when `skills/<name>/SKILL.md` is flat (install-block.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/install-block.md`)).
4. **Cursor, Windsurf, OpenCode, Devin, Amp, Pi (`skills.sh`):** `npx skills@latest add <owner>/ej-skills` or `npx skills@latest add <owner>/ej-skills --skill=fact-check` discovers `skills/<name>/SKILL.md` automatically (install-block.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/install-block.md`)).

#### Recommended Repository Tree for `ej-skills`

```text
ej-skills/
├── .claude-plugin/
│   ├── plugin.json             # Claude Code, Codex, Copilot, VS Code manifest
│   └── marketplace.json        # Self-hosted plugin marketplace index
├── plugin.json                 # Google Antigravity (AGY) root plugin manifest
├── package.json                # Version management & metadata
├── README.md                   # Canonical install blocks + skill catalog
├── research/
│   └── 2026-10-24-fact-check-best-practices.md
└── skills/
    └── fact-check/
        ├── SKILL.md            # Core Agent Skills instructions + YAML frontmatter
        ├── agents/
        │   └── openai.yaml     # OpenAI Codex UI metadata
        └── references/         # Optional deep reference checklists (loaded on demand)
```

---

## 4. Blueprint for the `fact-check` Skill Workflow

Synthesizing the research above, the `fact-check` skill in `ej-skills` should guide the agent through a disciplined **6-Step Verification Protocol**:

1. **Scope & Intake:** Identify the input target (a file/draft in the repo, a URL, a set of claims in chat, or the agent's own prior response) and determine whether the user wants an inline audit, a structured report, or direct edits to fix inaccuracies.
2. **Atomic Decomposition & Decontextualization (Claimify / SAFE / FActScore):**
   - Extract checkworthy, falsifiable propositions (skipping pure opinion or boilerplate).
   - Split compound statements into individual **atomic claims**.
   - **Decontextualize** each claim so it stands alone with explicit entity names, quantities, and temporal anchors (dates/versions).
3. **Triangulated Retrieval & Tool Routing (FacTool + Popperian Falsification):**
   - Route code/repo claims to local file/git/test tools, math/statistical claims to Python/shell calculation, and world/doc claims to web search.
   - For every web-searched claim, execute **at least two complementary query types**: a **primary-source/neutral query** and an **adversarial/falsification query** (hunting for counter-evidence, caveats, deprecations, or retractions).
4. **Lateral Reading & Primary-Source Tracing (SHEG / SIFT / Anti-Citogenesis):**
   - Evaluate sources against the **4-Tier Source Hierarchy**.
   - Never treat secondary blogs, Wikipedia summaries, or multiple outlets repeating the same press release as terminal proof—trace footnotes back to the **Tier 1 primary source** (official docs, source code, peer-reviewed paper, statutory/regulatory filing, or raw dataset).
   - Practice **lateral reading** on unfamiliar domains or authors to detect bias, sponsorship, or predatory publishing.
5. **Epistemic Verdict Assignment (FEVER / AVeriTeC / ClaimReview):**
   - Assign one of the 6 calibrated verdicts to each atomic claim: `Verified`, `Refuted`, `Mixed / Needs Context`, `Outdated`, `Disputed`, or `Unverifiable`.
6. **Citation-Hygienic Reporting (ALCE / IFCN):**
   - Produce a structured Fact-Check Report containing an Executive Summary (overall factual precision tally, e.g., $X/Y$ atomic claims verified), a Claim-by-Claim Verification Table/Cards with **exact URLs, publication dates, source tiers, and verbatim supporting/refuting quotes**, and actionable **Suggested Corrections** for any refuted, outdated, or uncalibrated claims.

---

## References & Primary Sources

1. **IFCN (Poynter Institute):** *The Commitments of the Code of Principles*. [https://ifcncodeofprinciples.poynter.org/know-more/the-commitments-of-the-code-of-principles](https://ifcncodeofprinciples.poynter.org/know-more/the-commitments-of-the-code-of-principles)
2. **Wineburg, S., & McGrew, S. (2019):** *"Lateral Reading and the Nature of Expertise: Reading Less and Learning More When Evaluating Digital Information"*, *Teachers College Record*, 121(11), 1–40. [https://doi.org/10.1177/016146811912101102](https://doi.org/10.1177/016146811912101102)
3. **Caulfield, M. (2019):** *"SIFT (The Four Moves)"*, Hapgood. [https://hapgood.us/2019/06/19/sift-the-four-moves/](https://hapgood.us/2019/06/19/sift-the-four-moves/)
4. **Schema.org & Google Search Central:** *`ClaimReview` Specification* ([https://schema.org/ClaimReview](https://schema.org/ClaimReview)) & *Fact Check (`ClaimReview`) Structured Data* ([https://developers.google.com/search/docs/appearance/structured-data/factcheck](https://developers.google.com/search/docs/appearance/structured-data/factcheck)).
5. **Min, S., et al. (2023):** *"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation"*, *EMNLP 2023*. [https://arxiv.org/abs/2305.14251](https://arxiv.org/abs/2305.14251) | [https://aclanthology.org/2023.emnlp-main.741/](https://aclanthology.org/2023.emnlp-main.741/)
6. **Wei, J., et al. (2024):** *"Long-form factuality in large language models"* (SAFE & LongFact), Google DeepMind. [https://arxiv.org/abs/2403.18802](https://arxiv.org/abs/2403.18802) | [https://github.com/google-deepmind/long-form-factuality](https://github.com/google-deepmind/long-form-factuality)
7. **Metropolitansky, D., & Larson, J. (2025):** *"Towards Effective Extraction and Evaluation of Factual Claims"* (Claimify), Microsoft Research. [https://arxiv.org/abs/2502.10855](https://arxiv.org/abs/2502.10855)
8. **Chern, I., et al. (2023):** *"FacTool: Factuality Detection in Generative AI — A Tool Augmented Framework for Multi-Task and Multi-Domain Scenarios"*. [https://arxiv.org/abs/2307.13528](https://arxiv.org/abs/2307.13528) | [https://github.com/GAIR-NLP/factool](https://github.com/GAIR-NLP/factool)
9. **Thorne, J., et al. (2018):** *"FEVER: a Large-scale Dataset for Fact Extraction and VERification"*, *NAACL-HLT 2018*. [https://arxiv.org/abs/1803.05355](https://arxiv.org/abs/1803.05355) | [https://aclanthology.org/N18-1074/](https://aclanthology.org/N18-1074/)
10. **Schlichtkrull, M., et al. (2023):** *"AVeriTeC: A Dataset for Real-world Claim Verification with Evidence from the Web"*, *NeurIPS 2023*. [https://arxiv.org/abs/2305.13117](https://arxiv.org/abs/2305.13117)
11. **Gao, T., Yen, H., Yu, J., & Chen, D. (2023):** *"Enabling Large Language Models to Generate Text with Citations"* (ALCE), *EMNLP 2023*. [https://arxiv.org/abs/2305.14627](https://arxiv.org/abs/2305.14627) | [https://aclanthology.org/2023.emnlp-main.398/](https://aclanthology.org/2023.emnlp-main.398/)
12. **Munroe, R. (2011):** *"Citogenesis"*, *xkcd* #978 ([https://xkcd.com/978/](https://xkcd.com/978/)) & Wikipedia, *Circular reporting* ([https://en.wikipedia.org/wiki/Circular_reporting](https://en.wikipedia.org/wiki/Circular_reporting)).
13. **Agent Skills Open Standard:** *Specification* ([https://agentskills.io/specification](https://agentskills.io/specification)).
14. **Local Harness & Packaging References:**
    - install-block.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/install-block.md`)
    - invocation.md (`~/.gemini/config/vendor/mattpocock-skills/.agents/invocation.md`)
    - plugin/SKILL.md (`~/.gemini/antigravity/builtin/skills/plugin/SKILL.md`)
    - agy-customizations/SKILL.md (`~/.gemini/antigravity/builtin/skills/agy-customizations/SKILL.md`)
