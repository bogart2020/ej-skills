# Domain Verification Playbooks

Specialized primary-source tracing and falsification checks for the four domain branches referenced in [`SKILL.md`](../SKILL.md).

## Software, APIs, and benchmarks

1. **Pin the version before judging**:
   - An API behavior, flag, or default that changed between versions is `Outdated` when stated as current, or `Mixed / Needs Context` when stated without a version bound.
   - Check the official migration guide, `CHANGELOG.md`, release notes, or source repository tag for the exact version in question.
2. **Distinguish deprecation from removal**:
   - Frameworks frequently mark an API deprecated in major version $N$ and remove it in $N+1$. Verify whether the feature throws an error today or merely emits a warning.
3. **Audit benchmark claims against methodology**:
   - Vendor benchmarks ("Library X is 5x faster than Library Y") are Tier 3 for competitor comparisons until the benchmark harness is inspected.
   - Check the benchmark repository or methodology section for: hardware/OS specs, warmup iterations, caching/memoization asymmetries, payload sizes, concurrency levels, and whether the competitor library was configured idiomatically (e.g., production mode enabled, connection pooling on).
   - If a benchmark holds only on a synthetic micro-task (e.g., cold-start hello-world) while the claim states a universal speedup, grade it `Mixed / Needs Context` and state the exact workload boundary.

## Science, medicine, and academic papers

1. **Verify paper existence and metadata first**:
   - Confirm the exact paper title, author list, publication venue, year, and DOI/arXiv ID via search. Hallucinated citations frequently blend a real author name with a fabricated title and plausible journal.
2. **Check the study hierarchy**:
   - Rank evidence by study design: systematic review and meta-analysis of RCTs > randomized controlled trial (RCT) > prospective cohort study > retrospective observational/case-control > animal or *in vitro* model > preprint / opinion commentary.
   - When a claim states *"scientists proved X works in humans"* based on a mice study, an *in vitro* petri-dish assay, or an unadjusted observational correlation ($n = 24$), grade it `Mixed / Needs Context` or `Refuted` and name the actual study design and sample size ($n$).
3. **Check for retractions, corrections, and failed replications**:
   - Run a targeted falsification query: `"<paper title or DOI>" retraction OR corrigendum OR erratum OR "failed to replicate" OR PubPeer`.
4. **Read the abstract's numbers and limitations, not the press release**:
   - University and journal press releases routinely flatten hedged findings into causal headlines. Extract the actual effect size, confidence interval, $p$-value, and authors' stated limitations directly from the paper.

## Economics, finance, and statistics

1. **Check the denominator and base rate**:
   - A relative change (*"crime/revenue/risk doubled"*, +100%) without the absolute baseline ($0.5\% \to 1.0\%$) is a classic cherry-picking pattern. Always report both the **relative change** and the **absolute baseline**.
2. **Verify unit definitions and adjustments**:
   - Confirm whether financial or macroeconomic series are **nominal vs. inflation-adjusted (real)**, **seasonally adjusted vs. unadjusted**, **mean vs. median**, and **per-capita vs. aggregate**.
   - Comparing nominal values across multi-year periods of high inflation without noting real change earns `Mixed / Needs Context`.
3. **Trace corporate metrics to regulatory filings**:
   - For public companies, trace revenue, headcount, margins, and risk disclosures to primary regulatory filings (`10-K`, `10-Q`, `8-K`, `S-1`, earnings transcripts) rather than secondary news summaries.
   - Distinguish **GAAP** figures from **Non-GAAP / Adjusted** management figures.

## Quotes, history, and viral media

1. **Trace quotes to the earliest dated record**:
   - Famous figures (Einstein, Twain, Churchill, Lincoln, Feynman) attract orphan aphorisms. Search `"<exact quote phrase>" Quote Investigator OR Wikiquote OR earliest` to locate the first dated print or archival appearance.
   - If the earliest documented appearance postdates the speaker's death or originates in a secondary column with no primary citation, grade the attribution `Refuted` or `Unverifiable`.
2. **Check the surrounding paragraph for context stripping**:
   - Retrieve the full paragraph or transcript surrounding a viral quote. If the speaker was summarizing an opponent's position before refuting it, or if an ellipsis (`...`) removed a critical condition, grade the claim `Refuted` or `Mixed / Needs Context` and quote the full original passage.
3. **Verify date, location, and provenance of images or events**:
   - Viral event claims frequently attach genuine photographs or statistics from an earlier year or different country to a current event. Verify the original capture date and location before accepting the framing.
