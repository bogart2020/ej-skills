---
name: compare
description: Compare any two or more options head-to-head across weighted categories with category winners, calibrated ties, and an overall winner. Use when evaluating products or services side by side, weighing places, cities, or neighborhoods, comparing people, job candidates, athletes, or historical figures, or choosing between technologies, architectures, companies, careers, or policies.
license: MIT
---

# Compare

Compare any options head-to-head: settle priorities and dealbreakers, build **4 to 7 weighted MECE categories**, score **one category at a time** with calibrated **ties**, and deliver one **overall winner** with the conditions that would change it.

## Environment adaptation

- **Chat** (Claude Desktop, web): check history, memory, and attached files for priorities and constraints.
- **Code and CLI**: when the comparison concerns the active project, read relevant workspace files (`package.json`, architecture docs, notes) before asking. Use Python or shell for exact math. For **3 or more options**, dispatch parallel verification subagents when supported, briefing each with the user's country and currency.

## Plain-language output

The bolded and table terms are your working vocabulary. Everything the user sees is everyday language:

- Print the **user-facing label** from the table below wherever an internal term would appear.
- Show math as labeled plain arithmetic ("\$1,850/month rent + \$400 taxes = \$2,250/month"), never formulas or symbols, even if the user asks for formulas or LaTeX (a typesetting format for math); offer formulas only in a separate appendix if they insist.
- **Money**: never silently default to US dollars. Lead every amount, in tables and prose, with the user's currency; after a converted one, add the original and one dated rate looked up this session ("₱16,800 (US\$299 at ₱56.20 per US\$1, 25 Oct 2026)"), or flag amounts approximate if no rate is current. If a source's currency is unclear, never print a bare \$; write "currency unconfirmed" next to the amount.
- Keep step and method names internal: describe the work by what it does (*"scoring battery life for both phones before moving on"*).
- Explain any unavoidable technical term (a benchmark name, a stat like WAR) in a short clause the first time it appears.

| Internal term | User-facing label |
| :--- | :--- |
| Knockout / Veto ($v_j$) | Dealbreaker |
| Category weight ($w_j$) | How much it matters (%) |
| Weighted Composite Score ($U$) | Overall score (out of 10) |
| Category Win-Loss-Tie Record | Categories won |
| Normalized evidence | Like-for-like evidence |
| Non-alignable differentiators | What only one option has |
| Even Swap | The core trade-off, in plain units |
| TCO / RPP / Z-score / GeoMean | Total cost over N years / cost-of-living-adjusted pay / era-adjusted stats / average across benchmarks |

## Interview rounds

Interview the user in rounds before the full research. Before the first round, run only quick checks that the options exist, are available, and fit a price range.

1. Ask at least one round on every run. Skip only when the user says "just answer", "no questions", or equivalent; then state the default priorities and weights in one line at the top of the report.
2. The **frontier** is every open question whose prerequisites are settled. Ask the whole frontier in one round, number each question, give your recommended answer, and word it so "yes" accepts the recommendation. When no safe default exists (currency with no cue, options not yet named), write `➡️ No default: please tell me`. Then stop and wait.
3. Find facts yourself. Ask only for decisions, preferences, and facts only the user knows. Never ask about anything the user already stated; turn what you only inferred into a quick confirmation.
4. Recompute the frontier after each answer. A question that depends on another open question (a budget depends on the currency) belongs to a later round.
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

## Reference pointers

- **Before Steps 2 and 3**, read the matching domain section of [`references/entity-playbooks.md`](references/entity-playbooks.md) for its canonical categories, weights, like-for-like formulas, and tie thresholds: products and services, places, job candidates and providers, athletes and historical figures, technologies, or companies, careers, policies, and creative works.
- **Before Step 7**, read [`references/report-format.md`](references/report-format.md) for the five report sections.

## Comparison sequence

Run these seven steps in order.

### Step 1: Frame the options, interview the user, and screen dealbreakers

1. **Draft 2 to 5 finalists**: compare all of 2 to 5 named options. With only 1 named (*"Postgres vs. the best alternatives"*), add the top 1 to 2 archetype rivals. With 6 or more, run a fast **Elimination by Aspects** pass down to 3 or 4 finalists, recording why each was cut.
2. **Interview** on what flips weights or knockouts: the decision and who it serves; the finalist set; dealbreakers (eligibility, budget ceiling, compatibility, a compliance floor); the top 2 to 3 priorities; when prices matter, the user's country and currency (confirm any guess from cues like ₱; with none, ask without suggesting one); and for canonical debates (historical figures, sports eras, general technology or policy), the era or rules, the yardstick (peak vs. career, today vs. then), and what "better" means.
3. **Screen**: mark options that fail a dealbreaker `Disqualified (Knockout)`; strip asymmetrically dominated decoy tiers and flag unavailable phantom options so they do not distort scoring.

**Completion criterion**: The user has confirmed 2 to 5 available finalists, their dealbreakers, top priorities, and (when prices matter) their country and currency (or opted out, with default weights stated), and every knocked-out or decoy option is identified.

### Step 2: Build categories, weights, and tie thresholds

1. Define **4 to 7 MECE categories** covering every dimension that separates the options in real outcomes. **Merge collinear criteria** (rent, taxes, groceries for cities) into one category with sub-metrics so nothing counts twice.
2. Assign **weights $w_j$ summing to 100%**, anchored to the user's priorities or the playbook's canonical weights. When the user lists priorities without ranking them, give them equal shares of 70% and split the other 30% equally across the remaining categories.
3. Per category, set the **indifference threshold $q_j$** (gap that is noise, a `Tie`), the **strict preference threshold $p_j$** (gap that is a decisive win), and any **veto $v_j$** for catastrophic failure.

**Completion criterion**: 4 to 7 non-overlapping categories carry weights summing to 100% and explicit $q_j$, $p_j$, and $v_j$ thresholds.

### Step 3: Gather symmetric evidence and normalize it

1. **Query parity**: for each option, run one capability query and one limitation query (`"<option>" benchmark OR failure OR limitation OR criticism`); a combined query for several options does not count.
2. **Normalize** to like-for-like units per the playbook, and split pooled averages by subgroup when sample mix differs, to avoid **Simpson's Paradox**.

**Completion criterion**: Every option has session-verified primary or independent evidence for every category, normalized to identical units and subgroup baselines.

### Step 4: Score one category at a time and call winners or ties

Score each category across all options before moving to the next, so an early win never creates a halo.

1. **Day-to-day check**: ask *"Six months from now, using this option alone, will this difference be felt in daily life, performance, or budget?"* Side-by-side charts inflate tiny gaps. For people and canonical debates, ask whether the gap would change an informed fan's or expert's ranking.
2. **Score 0.0 to 10.0** against objective domain anchors, never relative to the column, so adding or removing an option cannot flip the others' order.
3. **Call the category**: `Winner: [Option] (Decisive)` when $|\Delta g_j| \ge p_j$ with a clear real-world advantage; `Winner: [Option] (Narrow Edge)` when $q_j < |\Delta g_j| < p_j$ with a verifiable but modest or partly offset margin; `Tie` when any of:
   1. **Practical indifference** ($|\Delta g_j| \le q_j$): below the noticeable difference, such as under 3% real cost or under 5% benchmark.
   2. **Measurement overlap**: source variance or conflicting primary measurements exceed the gap.
   3. **Sub-criterion wash**: each option wins an equally weighted sub-dimension inside the category.
   4. **No session evidence**: any option lacks evidence checked in this session for this category. Score them equal, say it was not verified, and never award a win on general knowledge.

   With 3 or more options, call each category by the gap between its top two scores and name a single winner or `Tie`. A gap that fails the day-to-day check is a `Tie`, whatever its size on paper.

**Completion criterion**: Every category is scored across all options with normalized evidence, the day-to-day check, a 0.0 to 10.0 score each, and a `Decisive`, `Narrow Edge`, or `Tie` call.

### Step 5: Audit what only one option has, and debias

1. **Non-alignable differences**: list the high-impact unique capabilities, ecosystem locks, or one-sided risks per option and fold them into the trade-off.
2. **Even Swap**: state the net gap between the top two in natural units (*"A over B trades \$X/year for Z"*).
3. **Order-swap check**: mentally reverse the order the options were named; if any `Narrow Edge` or the overall call would flip, re-anchor it to the math or make it a `Tie`.

**Completion criterion**: High-impact unique traits are documented, the core trade-off is a concrete Even Swap, and every call survives the order-swap check.

### Step 6: Build the scoreboard

1. Count the Winner column of the scoreboard to build each option's record (`Decisive`, `Narrow Edge`, ties), and print it as the `Categories won` row.
2. Compute the weighted score $U(x_i) = \sum_j w_j s_{ij}$ out of 10.
3. Check for any veto. When the weighted winner took fewer categories than the runner-up, note why for the report: category count never overrides weighted score (two decisive 35% wins beat three narrow 10% wins).
4. Assign exactly one row of the **Overall verdict table**. The report prints that row's **Show the user** text once and never mixes in another row's wording.

**Completion criterion**: Every option has a win-loss-tie record and a weighted score, vetoes are identified, any category-count vs. score gap is reconciled, one overall verdict is assigned, and the printed record matches the scoreboard's Winner column exactly.

### Step 7: Write the report in plain language

Write the five sections in `references/report-format.md`.

**Completion criterion**: All five sections are present (section 4 with both parts), the verdict line is one overall verdict label with nothing added and a gap that matches that row's rule, any gap between categories won and overall score is explained, every category and the overall matchup has a result, sources are session-verified, the conditions that would change the winner are exact, and every internal term is replaced by its user-facing label. A last scan finds no foreign amount alone or first, even in prices quoted from news or stores.

## Verdict tables

| Category verdict | Show the user | When |
| :--- | :--- | :--- |
| **`Winner: [Option] (Decisive)`** | `[Option] wins clearly` | See Step 4. |
| **`Winner: [Option] (Narrow Edge)`** | `[Option] has a slight edge` | See Step 4. |
| **`Tie`** | `Tie` | See Step 4. |

| Overall verdict | Show the user | When |
| :--- | :--- | :--- |
| **`Overall Winner: [Option] (Decisive)`** | `Clear winner: [Option]` | Passes every knockout, leads by $\Delta U \ge 0.8$ (of 10), and stays first when any one weight moves 10 points. |
| **`Overall Winner: [Option] (On Points / Narrow Edge)`** | `Narrow winner: [Option]` | Passes every knockout and wins on weighted score ($0.25 < \Delta U < 0.8$), whether or not it lost any categories. |
| **`Overall Winner: [Option] (Default) / Split by Profile`** | `Best for most people: [Option] (but it depends on you)` | Gap over 0.25 but the winner flips for a common user profile. Name the default winner up front, and show the split (`Best if you [A]: X` vs. `Best if you [B]: Y`). |
| **`Overall Tie (Dead Heat)`** | `Too close to call` | Always when $\lvert\Delta U\rvert \le 0.25$, whatever the category wins; always add a one-step tiebreaker as a single if-then rule that names an option ("If you mostly fast-charge, pick B; otherwise A"). |
| **`Disqualified / Pivot to [Option Z]`** | `None of these fit: consider [Option Z]` | Every option fails a veto, or all are dominated by an outside benchmark Z. |

## Guardrails

1. **Session-verified evidence only**: cite only URLs, benchmarks, filings, and datasets retrieved in this session (or provided by the user), with source name and date or version. A search-result summary supports a claim only when labeled "from search summary"; scores that decide a win need a fetched page.
