---
name: should-i-buy
description: Evaluate buying and financial decisions across any category to deliver a calibrated verdict. Use when deciding whether to buy, upgrade, repair, or skip an item, comparing options or subscriptions, or weighing buying against renting, leasing, or building.
license: MIT
---

# Should I Buy

Evaluate any purchase or financial commitment against **not buying**, real-world **failure modes**, full **Total Cost of Ownership (TCO)**, and **50%-deflated usage**, then deliver one calibrated **verdict** with the conditions that would change it. If the request is not a decision about buying, paying for, or keeping something, set this skill aside and answer normally.

## Environment adaptation

- **Chat** (Claude Desktop, web): check history, memory, and attachments for buyer context. To save preferences, output a copyable snippet following [`references/buyer-profile-template.md`](references/buyer-profile-template.md).
- **Code and CLI**: read `.agents/buyer-profile.md` or `~/.agents/buyer-profile.md` before asking questions. Use Python or shell for exact math. For **3 or more candidate products**, dispatch parallel verification subagents when supported, briefing each with the user's country and currency.

## Plain-language output

The bolded and table terms are your working vocabulary. Everything the user sees is everyday language:

- Print the **user-facing label** from the table below wherever an internal term would appear.
- Show math as labeled plain arithmetic ("\$1,200 up front + \$540 in fees - \$300 resale = \$1,440 total"), never formulas or symbols: write "divided by" and "times" in words, with no ÷, ×, or / between numbers.
- **Money**: never silently default to US dollars. Lead every amount, in tables and prose, with the user's currency; after a converted one, add the original and one dated rate looked up this session ("₱16,800 (US\$299 at ₱56.20 per US\$1, 25 Oct 2026)"), or flag amounts approximate if no rate is current. Prefer local sellers' prices to converted ones.
- Keep step, tier, and section names internal: describe the work by what it does (*"checking owner complaints after a year of use"*).
- Explain any unavoidable technical term (APR, a lab certification) in a short clause on first use.

| Internal term | User-facing label |
| :--- | :--- |
| Fundamental objective | Your real goal |
| Knockout constraint / EBA | Dealbreaker |
| $\text{TCO}(T)$ | Total cost over N years (after resale) |
| 50%-deflated $\text{CPU}$ / $\text{CPH}$ | Cost per use / per hour, even if you use it half as much as you expect |
| $V_{\text{salvage}}$ | Resale value |
| Break-even $N^*$ | Uses needed before buying beats renting |
| Diderot spiral | Add-ons you'll likely end up buying |
| Opportunity cost | What else this money could do |
| 12-month premortem / Action vs. Inaction Regret | If you regret this in a year, here's the likely reason / regret of buying vs. regret of skipping |

## Interview rounds

1. Ask at least one round on every run. Skip only when the user says "just answer", "no questions", or equivalent; then state your assumptions, including the currency, in one line at the top of the report. If they also ask you to skip research, say what you could not check and still show the cost table.
2. The **frontier** is every open question whose prerequisites are settled. Ask the whole frontier in one round, number each question, give your recommended answer, and word it so "yes" accepts the recommendation (with no safe default, such as the country, write `➡️ No default: please tell me`). Then stop and wait.
3. Find facts yourself. Ask only for decisions, preferences, and facts only the user knows. Never ask about anything the user already stated; turn what you only inferred into a quick confirmation.
4. Recompute the frontier after each answer. A question that depends on another open question (a budget depends on the currency) belongs to a later round.
5. "Yes", "idk", or a skipped question accepts your recommendation. When the user hands you the choice ("you decide", "whatever you think"), adopt your recommendations for every open question, list them as assumptions, and start without another round. A written answer replaces your recommendation: carry the user's exact words into the analysis, and never describe your own suggestion as something the user said.
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

- **Before Step 3**, read the matching category section of [`references/category-playbooks.md`](references/category-playbooks.md).
- **Before Step 4**, read [`references/cost-math.md`](references/cost-math.md) for the formulas.
- **Before Step 6**, read [`references/report-format.md`](references/report-format.md) for the report sections.
- **When saving a profile**, read [`references/buyer-profile-template.md`](references/buyer-profile-template.md).

## Proportional rigor

Scale to the commitment's 3-year cash outflow (in US dollars; convert to the user's currency):

- **Everyday** (under \$100, one-time): street price, 50%-deflated cost per use, top failure mode, and a comparison against keeping what the user has or a proven budget pick. Skip the full report layout: answer in at most 200 words (verdict, bottom line, cost per use, comparison, top risk, next step) with 1 or 2 source links.
- **Standard** (\$100 to \$2,500, or any subscription): full TCO, resale, deflated cost per use or hour, independent tests and 1-to-3 star failure audit, add-on check, and 12-month premortem.
- **High stakes** (over \$2,500, financed, vehicles, real estate, B2B): add discounted lifecycle cost, APR and monthly cash stress tests, break-even against renting, leasing, or building, and opportunity cost against debt payoff or investing.

## Decision sequence

Run these six steps in order.

### Step 1: Load buyer context and interview the user

1. Check the buyer profile, memory, prior turns, and cues (₱, a city, a store; with none, ask without suggesting one) for country and currency, guardrails, owned gear, subscriptions, and past purchase lessons.
2. Settle the **5 verdict-flipping variables**:
   - **Fundamental objective**: the job to be done, not the product, and why now.
   - **Current baseline**: what the user owns, uses, or does today, and its exact pain point.
   - **Usage and horizon**: realistic frequency (uses per week or hours per day) and holding period $T$.
   - **Payment and guardrails**: cash vs. credit, financing, or BNPL; budget ceiling; any high-APR debt or emergency-fund limits. Keep the payment method the user chose in every section, including any profile offer; if their plan cannot be confirmed, say so and price it as they described next to cash.
   - **Dealbreakers**: size, ecosystem or battery platform fit, safety, local warranty or repairability.
3. Run **Interview rounds** on these in everyday words (*"How often will you realistically use it?"*).

**Completion criterion**: The user has confirmed their country and currency and all 5 variables (or opted out, with assumptions stated).

### Step 2: Add the not-buying options and apply dealbreakers

1. Put the applicable baselines next to the target item: `Keep Current / Do Nothing` (\$0 extra), `Repair / Optimize Existing`, `Delay / Wait` (72 hours for everyday items, 30 days for major spend, or until a confirmed release or sale), `Rent / Borrow / Trial`, and `Used / Refurbished / Previous-Gen` (85% to 95% of the utility after the steepest depreciation). Price any rival the user names (lease, rent, build, another model) from searched offers; if none is local, use the nearest published regional offer and label it.
2. Apply **Elimination by Aspects**: test every option against the dealbreakers first and drop any that fails, whatever its other scores.

**Completion criterion**: Surviving options sit next to the strongest not-buying and low-cost alternative, and every dropped option names the dealbreaker it failed.

### Step 3: Verify claims and audit failure modes

Route each claim by type:

1. **Search attributes** (specs, warranty and return terms): manufacturer documentation, spec sheets, or contract terms.
2. **Experience attributes** (build, noise, battery life, stability): independent instrumented testers and 6-to-24-month owner reports.
3. **Credence attributes** (health, safety, security): peer-reviewed human trials or lab and regulatory certifications (USP, NSF, UL, SOC 2).
4. **Failure search** (`"<product>" problem OR failure OR "after a year" OR recall OR warranty denied OR teardown`): recurring 1-to-3 star failure clusters, time to failure, review hijacking, and lock-in.

**Completion criterion**: Every critical claim on surviving options is checked against primary or independent test sources, and the top failure modes and lock-in risks are documented with session-verified links.

### Step 4: Compute total cost, cost per use, and opportunity cost

Using `references/cost-math.md`, scaled to the rigor tier: TCO over $T$ net of realistic resale, cost per use or per hour at both stated and **50% of stated usage**, break-even uses against any rent or pay-per-use option, and the opportunity cost of the same money.

**Completion criterion**: Every metric above appears in the report in the user's currency, including cost per use at stated and half usage and what else this money could do; resale comes from a searched listing or is labeled an estimate.

### Step 5: Debias and run a 12-month premortem

1. **Full-price test**: strip fake markdowns and "pennies a day" framing; check 90-to-365-day price history.
2. **Sunk-cost reset**: count prior spend as zero; compare only costs and value from today forward.
3. **Add-on audit (Diderot spiral)**: price the accessories or higher subscription tiers likely within 6 months.
4. **Premortem**: assume the buyer regrets this in 12 months; name the 2 to 3 likeliest causes (novelty fading, lower usage, hidden recurring cost, cash strain), and weigh regret of buying (adjusted for returns and resale) against regret of skipping.

**Completion criterion**: The report states what the price history showed (or that none was found), add-on costs are priced in (a searched typical price labeled as an estimate when no exact one exists; "not priced" does not count), and the premortem causes and reversibility are evaluated.

### Step 6: Deliver the verdict

Pick one label from the **Verdict table**, print it word for word, and write the report in plain language using `references/report-format.md`.

**Completion criterion**: The report gives one verdict, a side-by-side cost table against the best not-buying option, session-verified sources, and exact conditions that would change the verdict, with every internal term replaced by its user-facing label. A last scan finds no foreign amount alone or first, even in prices quoted from news or stores.

## Verdict table

| Verdict | When to assign |
| :--- | :--- |
| **`Buy`** | Passes every dealbreaker, beats keeping and renting even at 50% usage, shows no disqualifying failure mode, and fits cash and liquidity guardrails at street price. |
| **`Buy With Conditions / Wait`** | Right fit, but overpriced against price history, a refresh is imminent, or a prerequisite applies (a 30-day cooling-off, selling an item first, a target price of \$X or less). Use only when the user should not buy today at today's street price; ordinary negotiating and loan-shopping tips stay under `Buy`. |
| **`Buy Alternative Instead`** | A purchase is warranted, but this model loses on TCO, reliability, or value to a competitor, an older or refurbished tier, or a one-time-purchase option. |
| **`Rent / Borrow / Trial First`** | Projected uses fall below break-even ($N_{\text{projected}} < N^*$), or preference uncertainty makes a cheap rental, borrow, or trial the better first step, or leasing beats buying on the side-by-side total over the holding period. |
| **`Keep Current / Repair`** | The current setup, or a cheap repair or workflow change, covers 80%+ of the goal for a fraction of the replacement TCO. |
| **`Do Not Buy`** | Fails a dealbreaker, has severe reliability or lock-in defects, relies on high-APR financing or emergency savings for a want, or is worth less than keeping the cash. |

## Guardrails

1. **Liquidity and APR**: financing a depreciating consumer good on revolving credit, fee-bearing BNPL, or deferred-interest promos means `Do Not Buy` or `Buy With Conditions / Wait`, unless the item is required for livelihood or health and safety.
2. **Session-verified prices and sources only**: cite only URLs, prices, and test data retrieved in this session (or provided by the user), with source name and date. A search snippet counts only when labeled "from a search summary"; prefer an opened page for prices.
3. **No sycophancy**: treat enthusiasm (*"I already decided, just checking"*) as a reason to apply the 50% usage test, add-on audit, and premortem harder, never to validate the impulse.
