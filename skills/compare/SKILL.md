---
name: compare
description: Compare any two or more options head-to-head across weighted categories with category winners, calibrated ties, and an overall winner. Use when evaluating products or services side by side, weighing places, cities, or neighborhoods, comparing people, job candidates, athletes, or historical figures, or choosing between technologies, architectures, companies, careers, or policies.
argument-hint: "[contender A vs contender B (vs C...), or 1 item to benchmark against top rivals]"
license: MIT
---

# Compare

Run a rigorous toe-to-toe comparison across any entity class by framing the **contenders** and **knockout constraints**, constructing **4 to 7 weighted MECE categories**, normalizing domain evidence symmetrically, scoring **horizontally one category at a time** with calibrated **indifference thresholds (`Tie`)**, auditing **non-alignable differentiators**, and delivering a **dual-accounting scoreboard** with an unambiguous **overall winner** and **crossover conditions**.

## Environment adaptation

Adapt tool use and context discovery to the active runtime:

- **Chat environment** (Claude Desktop, web chat): inspect conversation history, project instructions, built-in memory, and attached files for user priorities and constraints. Use web search to retrieve symmetric primary and independent data for every contender.
- **Code and CLI environment** (Claude Code, Codex, Antigravity, Gemini CLI, Cursor, Windsurf): inspect relevant local workspace files (such as `package.json`, architecture docs, or user notes) when the comparison relates to the active project before asking questions. Use Python or shell (`python3 -c ...`) for exact weighted-score, geometric-mean, purchasing-power, Total Cost of Ownership (TCO), and Z-score calculations. When comparing **3 or more contenders** in a harness that supports subagents, dispatch parallel verification subagents so raw search pages stay out of the main context window; handle 2 contenders inline.

## Progressive disclosure pointers

Before running Step 2 and Step 3, read the matching section in [`references/entity-playbooks.md`](references/entity-playbooks.md):

| Entity domain | What `references/entity-playbooks.md` provides |
| :--- | :--- |
| **Products, hardware, appliances, and services** | 7-bucket TCO normalization, independent lab benchmarks, 1-to-3 star failure clusters, resale value |
| **Places: cities, neighborhoods, countries, and venues** | BEA RPP / World Bank PPP and tax-adjusted real disposable surplus, neighborhood safety/transit, comfortable outdoor climate days |
| **People: job candidates, leaders, and service providers** | Schmidt & Hunter validity hierarchy, Behaviorally Anchored Rating Scales (BARS), work-sample evidence vs. pedigree Halo |
| **People: athletes, public/historical figures, and creators** | Gould *Full House* era-adjusted Z-scores ($Z_{\text{era}}$), talent-pool depth, WAR replacement baseline, JAWS 50/50 peak vs. longevity |
| **Technologies, software, libraries, models, and architectures** | ISO/IEC 25010:2023 quality dimensions, SEI ATAM scenario tradeoff points, Fleming & Wallace geometric mean for benchmark ratios |
| **Companies, careers/job offers, policies, and creative works** | Balanced Scorecard and moat analysis, RPP/risk-adjusted compensation and effective hourly rate, Bardach policy matrix, craft vs. audience fit |

## Comparison sequence

Run these six steps in order.

### Step 1: Frame contenders, screen knockouts, and gate on context

1. **Establish the contender set ($2$ to $5$ finalists)**:
   - **2 to 5 contenders named**: compare all named contenders head-to-head in a unified matrix.
   - **Only 1 contender named** (for example, *"Compare Postgres against the best alternatives"*): select the top 1 to 2 archetype competitors in that domain so the matchup is a genuine toe-to-toe test.
   - **6 or more contenders named**: run a fast **Elimination by Aspects (EBA)** knockout pass first to narrow the field to the **top 3 to 4 finalists** for deep category scoring, recording the exact reason each eliminated option was cut.
2. **Screen knockouts, decoys, and phantoms**:
   - **Knockouts**: test each contender against non-negotiable user dealbreakers (legal/visa eligibility, hard budget ceiling, OS/platform compatibility, latency/compliance floor). Flag any failing option as `Disqualified (Knockout)`.
   - **Asymmetric decoys and phantoms**: strip asymmetrically dominated decoy tiers (middle pricing tiers engineered to push buyers toward a target tier) and flag unavailable phantom options so they do not distort category scoring.
3. **Adaptive Context Gate**:
   - **Personal or workload-specific decisions** (such as choosing a city to relocate to, picking between job offers, or selecting a database for a specific system): if 1 to 3 high-leverage variables that flip category weights or knockouts are missing (and the user has not asked for an immediate comparison), ask **2 to 3 concise, high-information-gain questions** and wait for confirmation.
   - **General or canonical matchups** (such as historical/sports comparisons, general technology/policy matchups, or when the user requests an immediate answer): proceed immediately without asking questions by stating the default evaluation profile and category weights upfront.

**Completion criterion**: A clean finalist set of 2 to 5 available contenders is locked, any knockout-disqualified or decoy options are identified, and the evaluation profile is bounded via user confirmation or explicit default assumptions.

### Step 2: Construct MECE categories, weights, and tie thresholds

Consult [`references/entity-playbooks.md`](references/entity-playbooks.md) for the entity domain and build the evaluation rubric:

1. **Generate 4 to 7 Mutually Exclusive, Collectively Exhaustive (MECE) categories**:
   - Cover every fundamental dimension that separates the contenders in real-world outcomes.
   - **Collinearity merge check (anti-double-counting)**: verify that no two categories measure the same underlying trait. Where two candidate criteria move together (for example, *"Rent"*, *"Taxes"*, and *"Groceries"* for cities, or *"Throughput"* and *"Ingestion Speed"* for databases), merge them into a single category with sub-metrics so that dimension is counted once.
2. **Assign explicit Category Weights ($w_j$) summing to $100\%$**:
   - Anchor weights ($\sum_{j=1}^{m} w_j = 100\%$) to the user's stated priorities from Step 1, or to the canonical domain weights in [`references/entity-playbooks.md`](references/entity-playbooks.md).
3. **Define Indifference ($q_j$), Strict Preference ($p_j$), and Veto ($v_j$) thresholds**:
   - For each category, establish what gap constitutes practical noise (**Indifference Threshold $q_j \implies \texttt{Tie}$**), what gap constitutes an unmistakable advantage (**Strict Preference Threshold $p_j \implies \texttt{Decisive Win}$**), and whether a catastrophic failure triggers a **Non-Compensatory Veto ($v_j$)**.

**Completion criterion**: 4 to 7 non-overlapping MECE categories are defined with explicit percentage weights summing to 100% and clear indifference ($q_j$), preference ($p_j$), and veto ($v_j$) thresholds.

### Step 3: Retrieve symmetric evidence and normalize to domain baselines

Gather primary and independent evidence with equal rigor across every contender:

1. **Symmetric query parity**: run parallel positive-capability and adversarial-limitation queries (`"<contender>" benchmark OR failure OR limitation OR criticism`) for *every* contender so marketing volume or documentation density never masquerades as quality.
2. **Normalize metrics to commensurate units**:
   - Convert raw numbers into comparable baselines following [`references/entity-playbooks.md`](references/entity-playbooks.md): **BEA RPP / World Bank PPP and tax-adjusted real disposable surplus** for places; **Era-Adjusted Z-Scores ($Z_{\text{era}}$), WAR, and JAWS** for athletes and historical figures; **BARS behavioral anchors** for job candidates; **Geometric Mean ($\text{GeoMean}$) of normalized ratios** for multi-workload benchmarks; and **full-lifecycle TCO** for products and services.
   - Disaggregate pooled averages by workload or subgroup whenever sample mix differs across contenders to prevent **Simpson's Paradox**.

**Completion criterion**: Every contender has session-verified primary or independent evidence across all categories, normalized to identical units and subgroup baselines.

### Step 4: Score horizontally category-by-category and call winners or ties

Evaluate **one category at a time horizontally across all contenders** before moving to the next category (preventing Thorndike Halo carryover from Category 1 into Categories 2 through $m$):

1. **Apply the Separate-Evaluation Reality Check (Distinction Bias filter)**:
   - Side-by-side joint evaluation magnifies tiny continuous differences. For each category, ask: *"Six months from now, when experiencing Contender A alone without Contender B sitting next to it on a chart, will this difference actually be felt in daily life, performance, or budget?"*
2. **Assign domain-anchored scores ($0.0$ to $10.0$)**:
   - Score each contender on a $0.0$ to $10.0$ scale anchored to objective domain standards (**Ideal-Mode AHP** normalization) rather than dividing by the column sum, ensuring that adding or removing a third contender never reverses the pairwise rank of the original two.
3. **Call the Category Verdict (`Decisive Win`, `Narrow Edge`, or `Tie`)**:
   - Assign **`Winner: [Entity] (Decisive)`** when the lead exceeds the strict preference threshold ($|\Delta g_j| \ge p_j$) and produces a clear real-world advantage.
   - Assign **`Winner: [Entity] (Narrow Edge)`** when the lead clears the indifference threshold ($q_j < |\Delta g_j| < p_j$) with a verifiable, meaningful margin that is modest or partially offset by sub-factors.
   - Assign **`Tie`** whenever any of the **Three Tie Conditions** holds:
     1. **Practical Indifference ($|\Delta g_j| \le q_j$)**: the gap falls below the Just Noticeable Difference in separate evaluation (such as a $<3\%$ real cost or salary difference, a $<5\%$ synthetic benchmark delta, or a 2-minute commute gap).
     2. **Epistemic / Measurement Overlap**: source variance, confidence intervals, or conflicting primary measurements exceed the observed gap between contenders.
     3. **Internal Sub-Criterion Wash**: Contender A wins sub-dimension $j_1$ while Contender B wins equally weighted sub-dimension $j_2$ within the same category.

**Completion criterion**: Every category is evaluated horizontally across all contenders with verified normalized metrics, a Separate-Evaluation reality check, a $0.0$ to $10.0$ score per contender, and a calibrated `Winner (Decisive)`, `Winner (Narrow Edge)`, or `Tie` call.

### Step 5: Audit non-alignable differentiators and run order-swap debiasing

1. **Non-Alignable Differentiators Audit**:
   - Standard comparison tables overweight **alignable differences** (metrics that share a column label) and miss **non-alignable differences** (unique capabilities, ecosystem locks, cultural realities, or asymmetric tail risks that exist in one contender with no counterpart slot in the other).
   - Explicitly list the high-impact non-alignable traits for each contender and incorporate them into the trade-off synthesis.
2. **Even-Swap Trade-Off Translation**:
   - Express the net gap between the top two contenders as a concrete **Even Swap** in natural units (for example, *"Choosing Contender A over Contender B trades \$X/year or Y ms of tail latency in exchange for Z"*).
3. **Order-Swap Invariance Check ($f(A, B) \equiv f(B, A)$)**:
   - Mentally reverse the order in which contenders were named in the prompt. If swapping Contender A and Contender B would flip any `Narrow Edge` or overall winner call, re-anchor that call to the objective math or convert an unsupported edge into a `Tie`.

**Completion criterion**: High-impact non-alignable differentiators are documented, the core trade-off between the top contenders is translated into a concrete Even Swap, and all verdicts pass the Order-Swap Invariance check.

### Step 6: Aggregate dual-accounting scoreboard and render the overall verdict

Compute the final results and render the Comparison Report inline using five sections:

1. **Dual-Accounting Aggregation**:
   - **Category Win-Loss-Tie Record**: tally total category wins for each contender (breaking down `Decisive` vs. `Narrow Edge` wins) and total `Ties`.
   - **Weighted Composite Score ($U$)**: compute each contender's weighted score out of $10.0$ (or $100$):
     $$U(x_i) = \sum_{j=1}^{m} w_j s_{ij}$$
   - **Reconciliation & Veto Check**: check whether any contender triggered a non-compensatory **Veto ($v_j$)**. Whenever the **Overall Winner** on weighted score ($U$) won fewer raw categories than the runner-up (for example, winning 2 high-weight categories decisively vs. losing 3 low-weight categories narrowly), explain that mathematical reconciliation explicitly in the summary.
2. **Render the 5-Section Comparison Report**:
   - **Section 1: Overall Verdict & Bottom Line**
     - **Overall Verdict**: assign one label from the **Overall Verdict taxonomy** below (`Overall Winner: [Entity] (Decisive)`, `Overall Winner: [Entity] (On Points / Narrow Edge)`, `Overall Winner: [Entity] (Default) / Split by Profile`, `Overall Tie (Dead Heat)`, or `Disqualified / Pivot to [Entity Z]`).
     - **Scorecard Snapshot**: display the **Category Win-Loss-Tie Record** alongside each contender's **Weighted Composite Score ($U$)**.
     - **Bottom Line**: 2 to 3 decisive sentences explaining why the winner took the crown (or why they tied) and reconciling category count with weighted utility.
   - **Section 2: Master Toe-to-Toe Scoreboard Table**
     - Present a single Markdown table with columns: `Category (Weight %)` | `Contender A (Score / 10)` | `Contender B (Score / 10)` | `[Contender C...]` | `Category Winner / Tie`.
     - Include summary bottom rows for **Category Win-Loss-Tie Tally** and **Weighted Overall Score ($U / 10.0$)**.
   - **Section 3: Category-by-Category Breakdown**
     - For each category ($1$ to $m$), show: **Weight ($w_j\%$)**, **Toe-to-Toe Normalized Evidence** (with session-verified citations and dates), **Separate-Evaluation Reality Check**, **Contender Scores ($0.0\text{–}10.0$)**, and **Category Verdict** (`Winner: [Entity] (Decisive)`, `Winner: [Entity] (Narrow Edge)`, or `Tie` with its rationale).
   - **Section 4: Non-Alignable Differentiators & Even-Swap Trade-Off**
     - Detail unique one-sided strengths, structural paradigm differences, or asymmetric risks that sit outside shared table columns, followed by the concrete **Even Swap** between the top contenders.
   - **Section 5: Winner by Scenario & Crossover Conditions**
     - **Winner by User Profile**: concise bullet rules (`Choose [Entity A] if...`, `Choose [Entity B] if...`).
     - **What Flips This Verdict (Crossover Thresholds)**: state exact, falsifiable numerical or contextual thresholds that would cause the runner-up to overtake the overall winner (for example, *"Contender B overtakes Contender A overall if you weight Category X above 40%, if Contender B's price drops below \$Y, or if workload exceeds Z RPS"*).

**Completion criterion**: The report delivers all five sections, reconciles the Category Win-Loss-Tie tally with the Weighted Composite Score ($U$), assigns a calibrated verdict to every category and to the overall matchup, cites session-verified sources, and states exact numerical crossover conditions.

---

## Reference rules

### Category verdict scale

| Category Verdict | Condition & Meaning |
| :--- | :--- |
| **`Winner: [Entity] (Decisive)`** | Margin exceeds the strict preference threshold ($|\Delta g_j| \ge p_j$). Unmistakable, high-confidence advantage in real-world separate evaluation. |
| **`Winner: [Entity] (Narrow Edge)`** | Margin exceeds the indifference threshold ($q_j < |\Delta g_j| < p_j$). Real, verifiable advantage, but modest in magnitude or partially offset by secondary sub-metrics. |
| **`Tie`** | Margin lies inside the indifference threshold ($|\Delta g_j| \le q_j$), falls within measurement/source uncertainty, or washes out across equally important internal sub-criteria. |

### Overall verdict taxonomy

| Overall Verdict | When to assign |
| :--- | :--- |
| **`Overall Winner: [Entity] (Decisive)`** | Passes all knockout/veto checks, leads by a wide weighted margin ($\Delta U \ge 0.8$ on a 10-point scale / $\ge 8.0$ on a 100-point scale), and stays #1 across reasonable weight sensitivity shifts. |
| **`Overall Winner: [Entity] (On Points / Narrow Edge)`** | Passes all knockout/veto checks and wins the weighted composite scorecard ($0.25 < \Delta U < 0.8$ on a 10-point scale) under the active weight profile while ceding specific categories to the runner-up. |
| **`Overall Winner: [Entity] (Default) / Split by Profile`** | Names the **#1 Overall Winner for the primary/default profile** upfront so the verdict never hedges, while highlighting that the contenders split sharply across opposing high-weight axes (`Winner for [Profile A]: Entity X` vs. `Winner for [Profile B]: Entity Y`). |
| **`Overall Tie (Dead Heat)`** | Weighted composite scores fall inside the overall indifference zone ($|\Delta U| \le 0.25$ on a 10-point scale) and category margins cancel out symmetrically. Always pair with a concrete **1-Step Tiebreaker Rule**. |
| **`Disqualified / Pivot to [Entity Z]`** | All compared contenders fail a hard knockout/veto constraint ($v_j$), or all are strictly dominated by a superior external benchmark `[Entity Z]`. |

### Verification & debiasing guardrails

1. **Horizontal scoring before aggregation**: Always score Category $j$ across all contenders before moving to Category $j+1$ so an early category win never creates a Halo effect on later categories.
2. **Category count never overrides weighted utility**: A contender that wins 3 minor 10%-weight categories by a narrow edge loses overall to a contender that wins 2 core 35%-weight categories decisively. Always compute $U = \sum w_j s_{ij}$ and explain any divergence from the raw category win count.
3. **Session-verified evidence only**: Cite only URLs, benchmarks, filings, and datasets retrieved and inspected during the current session (or provided by the user), including source name and date/version.
