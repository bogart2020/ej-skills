---
name: compare
description: Compare any two or more options head-to-head across weighted categories with category winners, calibrated ties, and an overall winner. Use when evaluating products or services side by side, weighing places, cities, or neighborhoods, comparing people, job candidates, athletes, or historical figures, or choosing between technologies, architectures, companies, careers, or policies.
argument-hint: "[contender A vs contender B (vs C...), or 1 item to benchmark against top rivals]"
license: MIT
---

# Compare

Run a rigorous toe-to-toe comparison across any entity class by interviewing the user, framing the **contenders** and **knockout constraints**, constructing **4 to 7 weighted MECE categories**, normalizing domain evidence symmetrically, scoring **horizontally one category at a time** with calibrated **indifference thresholds (`Tie`)**, auditing **non-alignable differentiators**, and delivering a **dual-accounting scoreboard** with an unambiguous **overall winner** and **crossover conditions**.

## Environment adaptation

Adapt tool use and context discovery to the active runtime:

- **Chat environment** (Claude Desktop, web chat): inspect conversation history, project instructions, built-in memory, and attached files for user priorities and constraints. Use web search to retrieve symmetric primary and independent data for every contender.
- **Code and CLI environment** (Claude Code, Codex, Antigravity, Gemini CLI, Cursor, Windsurf): inspect relevant local workspace files (such as `package.json`, architecture docs, or user notes) when the comparison relates to the active project before asking questions. Use Python or shell (`python3 -c ...`) for exact weighted-score, geometric-mean, purchasing-power, Total Cost of Ownership (TCO), and Z-score calculations. When comparing **3 or more contenders** in a harness that supports subagents, dispatch parallel verification subagents so raw search pages stay out of the main context window; handle 2 contenders inline.

## Plain-language output

The bolded terms and formulas in this skill (MECE, weights $w_j$, thresholds $q_j$ / $p_j$ / $v_j$, $U$, Even Swap, non-alignable differences, Z-scores, TCO, RPP, BARS, GeoMean) are your working vocabulary. Everything the user sees, including interview questions and the report, speaks everyday language a non-specialist understands on first read:

- Print the **user-facing label** from the table below wherever an internal term would appear.
- Show math as labeled plain arithmetic ("\$1,850/month rent + \$400 taxes = \$2,250/month") rather than formulas or symbols.
- Keep step and method names from this skill internal: describe the work by what it does (*"scoring battery life for both phones before moving on"*, not *"Step 4 horizontal scoring with Ideal-Mode AHP"*).
- When a technical term is unavoidable (a benchmark name, a stat like WAR), explain it in a short clause the first time it appears.

| Internal term | User-facing label |
| :--- | :--- |
| Contender | Option |
| Knockout / Veto ($v_j$) | Dealbreaker |
| Category weight ($w_j$) | How much it matters (%) |
| Weighted Composite Score ($U$) | Overall score (out of 10) |
| Category Win-Loss-Tie Record | Categories won |
| Separate-Evaluation Reality Check | Will you notice it day to day? |
| Normalized evidence | Like-for-like evidence |
| Non-alignable differentiators | What only one option has |
| Even Swap | The core trade-off, in plain units |
| Crossover thresholds | What would change the winner |
| TCO / RPP / Z-score / GeoMean | Total cost over N years / cost-of-living-adjusted pay / era-adjusted stats / average across benchmarks |

## Interview rounds

Interview the user in rounds before researching, so the comparison is weighted for their situation rather than a generic one.

1. Ask at least one round on every run. Skip the interview only when the user explicitly says "just answer", "no questions", or equivalent; then state the default priorities and weights in one line at the top of the report.
2. The **frontier** is every open question whose prerequisites are already settled. Ask the whole frontier in one round, number each question, give your recommended answer, and word each question so "yes" accepts your recommendation. Then stop and wait for the user's answers.
3. Find facts yourself (web search, attached files, workspace files, conversation history, memory). Ask the user only for decisions, preferences, and facts only they know. When existing context already answers a question, turn it into a quick confirmation with that answer as your recommendation.
4. Each answer can open new questions: recompute the frontier and ask the next round. A question that depends on another question still open in this round belongs to a later round.
5. When the frontier is empty, summarize the settled answers in 2 to 4 bullets and ask "Ready for me to start?" Begin research once the user confirms.

Format every round like so:

```
❓ **Q1** - **<short title>**: <question in everyday words, with options when useful>

➡️ <your recommended answer>

---

❓ **Q2** - **<short title>**: <question in everyday words, with options when useful>

➡️ <your recommended answer>
```

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

Run these seven steps in order.

### Step 1: Frame contenders, interview the user, and screen knockouts

1. **Draft the contender set ($2$ to $5$ finalists)**:
   - **2 to 5 contenders named**: compare all named contenders head-to-head in a unified matrix.
   - **Only 1 contender named** (for example, *"Compare Postgres against the best alternatives"*): select the top 1 to 2 archetype competitors in that domain so the matchup is a genuine toe-to-toe test.
   - **6 or more contenders named**: run a fast **Elimination by Aspects (EBA)** knockout pass first to narrow the field to the **top 3 to 4 finalists** for deep category scoring, recording the exact reason each eliminated option was cut.
2. **Interview the user**: run **Interview rounds** on the questions that flip category weights or knockouts:
   - **Decision and purpose**: what the choice is for and who it serves (relocating a family, a specific workload, a gift, settling a debate).
   - **Contender set**: confirm the drafted finalists, the archetype rivals you picked for a 1-contender request, or the shortlist left after the EBA pass.
   - **Dealbreakers**: non-negotiables such as legal/visa eligibility, hard budget ceiling, OS/platform compatibility, or a latency/compliance floor.
   - **Top priorities**: the 2 to 3 things that matter most, which anchor the category weights in Step 2.
   - **Lens for general or canonical matchups** (historical figures, sports eras, general technology or policy debates): which era or rules, which yardstick (peak vs. whole career, today vs. at the time), and what "better" means to the user.
3. **Screen knockouts, decoys, and phantoms** using the interview answers:
   - **Knockouts**: test each contender against the user's dealbreakers. Flag any failing option as `Disqualified (Knockout)`.
   - **Asymmetric decoys and phantoms**: strip asymmetrically dominated decoy tiers (middle pricing tiers engineered to push buyers toward a target tier) and flag unavailable phantom options so they do not distort category scoring.

**Completion criterion**: The user has confirmed the finalist set of 2 to 5 available contenders, their dealbreakers, and top priorities (or explicitly opted out of questions, with default weights stated), and any knockout-disqualified or decoy options are identified.

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

### Step 6: Aggregate the dual-accounting scoreboard

Compute the final results before writing anything for the user:

1. **Category Win-Loss-Tie Record**: tally total category wins for each contender (breaking down `Decisive` vs. `Narrow Edge` wins) and total `Ties`.
2. **Weighted Composite Score ($U$)**: compute each contender's weighted score out of $10.0$ (or $100$):
   $$U(x_i) = \sum_{j=1}^{m} w_j s_{ij}$$
3. **Reconciliation & Veto Check**: check whether any contender triggered a non-compensatory **Veto ($v_j$)**. Whenever the **Overall Winner** on weighted score ($U$) won fewer raw categories than the runner-up (for example, winning 2 high-weight categories decisively vs. losing 3 low-weight categories narrowly), note the reconciliation for the report.
4. **Overall verdict**: assign one entry from the **Overall verdict taxonomy** below.

**Completion criterion**: Every contender has a Win-Loss-Tie record and a weighted score $U$, any veto is identified, any category-count vs. $U$ divergence is reconciled, and one overall verdict is assigned.

### Step 7: Render the comparison report in plain language

Render the Comparison Report inline in the plain language set by **Plain-language output**, using five sections:

1. **Verdict & Bottom Line**
   - **Verdict**: the user-facing label of the overall verdict from Step 6 (see the **Show the user** column in the taxonomy below).
   - **Scorecard**: each option's categories won (clear wins, slight edges, ties) next to its overall score out of 10.
   - **Bottom line**: 2 to 3 decisive sentences on why the winner won (or why it is too close to call). When the winner took fewer categories than the runner-up, explain in one plain sentence that it won the categories that matter most to the user.
2. **Head-to-Head Scoreboard**
   - A single Markdown table with columns: `Category (how much it matters %)` | `Option A (score / 10)` | `Option B (score / 10)` | `[Option C...]` | `Winner`.
   - Bottom rows: **Categories won** and **Overall score (out of 10)**.
3. **Category by Category**
   - For each category, show: how much it matters (%), the like-for-like evidence (with dated, session-verified sources), whether the user will notice the difference day to day, each option's score out of 10, and the result (clear win, slight edge, or tie) with its reason.
4. **What Only One Option Has, and the Core Trade-off**
   - Unique strengths, structural differences, or one-sided risks that do not fit the table, followed by the core trade-off between the top two options in plain units (for example, *"Choosing A over B costs about \$X more per year and gets you Y"*).
5. **Who Should Pick What, and What Would Change the Winner**
   - **Pick by situation**: concise bullet rules (`Choose [Option A] if...`, `Choose [Option B] if...`).
   - **What would change the winner**: exact numbers or conditions that would make the runner-up come out on top (for example, *"B wins instead if price matters more to you than battery life, if B drops below \$Y, or if you need more than Z users"*).

**Completion criterion**: The report delivers all five sections, explains any gap between categories won and overall score, gives every category and the overall matchup a result, cites session-verified sources, states exact conditions that would change the winner, and reads cleanly to a non-specialist with every internal term from **Plain-language output** replaced by its user-facing label.

---

## Reference rules

### Category verdict scale

| Category Verdict | Show the user | Condition & Meaning |
| :--- | :--- | :--- |
| **`Winner: [Entity] (Decisive)`** | `[Option] wins clearly` | Margin exceeds the strict preference threshold ($|\Delta g_j| \ge p_j$). Unmistakable, high-confidence advantage in real-world separate evaluation. |
| **`Winner: [Entity] (Narrow Edge)`** | `[Option] has a slight edge` | Margin exceeds the indifference threshold ($q_j < |\Delta g_j| < p_j$). Real, verifiable advantage, but modest in magnitude or partially offset by secondary sub-metrics. |
| **`Tie`** | `Tie` | Margin lies inside the indifference threshold ($|\Delta g_j| \le q_j$), falls within measurement/source uncertainty, or washes out across equally important internal sub-criteria. |

### Overall verdict taxonomy

| Overall Verdict | Show the user | When to assign |
| :--- | :--- | :--- |
| **`Overall Winner: [Entity] (Decisive)`** | `Clear winner: [Option]` | Passes all knockout/veto checks, leads by a wide weighted margin ($\Delta U \ge 0.8$ on a 10-point scale / $\ge 8.0$ on a 100-point scale), and stays #1 across reasonable weight sensitivity shifts. |
| **`Overall Winner: [Entity] (On Points / Narrow Edge)`** | `Narrow winner: [Option]` | Passes all knockout/veto checks and wins the weighted composite scorecard ($0.25 < \Delta U < 0.8$ on a 10-point scale) under the active weight profile while ceding specific categories to the runner-up. |
| **`Overall Winner: [Entity] (Default) / Split by Profile`** | `Best for most people: [Option] (but it depends on you)` | Names the **#1 Overall Winner for the primary/default profile** upfront so the verdict never hedges, while highlighting that the contenders split sharply across opposing high-weight axes (`Best if you [Profile A]: Option X` vs. `Best if you [Profile B]: Option Y`). |
| **`Overall Tie (Dead Heat)`** | `Too close to call` | Weighted composite scores fall inside the overall indifference zone ($|\Delta U| \le 0.25$ on a 10-point scale) and category margins cancel out symmetrically. Always pair with a concrete **1-Step Tiebreaker Rule**. |
| **`Disqualified / Pivot to [Entity Z]`** | `None of these fit: consider [Option Z]` | All compared contenders fail a hard knockout/veto constraint ($v_j$), or all are strictly dominated by a superior external benchmark `[Entity Z]`. |

### Verification & debiasing guardrails

1. **Horizontal scoring before aggregation**: Always score Category $j$ across all contenders before moving to Category $j+1$ so an early category win never creates a Halo effect on later categories.
2. **Category count never overrides weighted utility**: A contender that wins 3 minor 10%-weight categories by a narrow edge loses overall to a contender that wins 2 core 35%-weight categories decisively. Always compute $U = \sum w_j s_{ij}$ and explain any divergence from the raw category win count.
3. **Session-verified evidence only**: Cite only URLs, benchmarks, filings, and datasets retrieved and inspected during the current session (or provided by the user), including source name and date/version.
