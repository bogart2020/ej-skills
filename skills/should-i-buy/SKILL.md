---
name: should-i-buy
description: Evaluate buying and financial decisions across any category to deliver a calibrated verdict. Use when deciding whether to buy, upgrade, repair, or skip an item, comparing options or subscriptions, or weighing buying against renting, leasing, or building.
license: MIT
---

# Should I Buy

Evaluate any purchase or financial commitment against **not buying**, real-world **failure modes**, full **Total Cost of Ownership (TCO)**, and **50%-deflated usage**, then deliver one calibrated **verdict** with the conditions that would change it.

## Environment adaptation

- **Chat** (Claude Desktop, web): check history, project instructions, memory, and attachments for buyer context. Search for independent lab tests, price history, resale values, and long-term owner failure reports. To save preferences or a decision log, output a copyable snippet following [`references/buyer-profile-template.md`](references/buyer-profile-template.md).
- **Code and CLI** (Claude Code, Codex, Antigravity, Gemini CLI, Cursor, Windsurf): read `.agents/buyer-profile.md` or `~/.agents/buyer-profile.md` before asking questions. Use Python or shell for exact TCO, APR, NPV, and break-even math. For **3 or more candidate products**, dispatch parallel verification subagents when the harness supports them; handle 1 or 2 inline.

## Plain-language output

The bolded terms and formulas in this skill (TCO, CPU, CPH, $V_{\text{salvage}}$, $N^*$, EBA, Diderot spiral, premortem, Action/Inaction Regret, fundamental vs. means objective) are your working vocabulary. Everything the user sees speaks everyday language a non-specialist understands on first read:

- Print the **user-facing label** from the table below wherever an internal term would appear.
- Show math as labeled plain arithmetic ("\$1,200 up front + \$15/month for 3 years - \$300 resale = \$1,440 total"), never formulas or symbols.
- Keep step, tier, and section names internal: describe the work by what it does (*"checking owner complaints after a year of use"*).
- Explain any unavoidable technical term (APR, a lab certification) in a short clause the first time it appears.

| Internal term | User-facing label |
| :--- | :--- |
| Fundamental objective | Your real goal |
| Knockout constraint / EBA | Dealbreaker |
| $\text{TCO}(T)$ | Total cost over N years (after resale) |
| 50%-deflated $\text{CPU}$ / $\text{CPH}$ | Cost per use / per hour, even if you use it half as much as you expect |
| $V_{\text{salvage}}$ | Resale value |
| Break-even $N^*$ | Uses needed before buying beats renting |
| Non-purchase baseline | Not buying (keep, repair, wait, or rent) |
| Diderot spiral | Add-ons you'll likely end up buying |
| Opportunity cost | What else this money could do |
| 12-month premortem / Action vs. Inaction Regret | If you regret this in a year, here's the likely reason / regret of buying vs. regret of skipping |

## Interview rounds

Interview the user in rounds before researching, so the verdict fits their real situation.

1. Ask at least one round on every run. Skip only when the user says "just answer", "no questions", or equivalent; then state your assumptions in one line at the top of the report.
2. The **frontier** is every open question whose prerequisites are settled. Ask the whole frontier in one round, number each question, give your recommended answer, and word it so "yes" accepts the recommendation. Then stop and wait.
3. Find facts yourself (web search, attachments, buyer profile, history, memory). Ask only for decisions, preferences, and facts only the user knows; turn already-answered questions into quick confirmations.
4. Recompute the frontier after each answer. A question that depends on another open question belongs to a later round.
5. When the frontier is empty, summarize the settled answers in 2 to 4 bullets and ask "Ready for me to start?" Begin once the user confirms.

Format every round like so:

```
❓ **Q1** - **<short title>**: <question in everyday words, with options when useful>

➡️ <your recommended answer>

---

❓ **Q2** - **<short title>**: <question in everyday words, with options when useful>

➡️ <your recommended answer>
```

## Reference pointers

- **Before Step 3**, read the matching section of [`references/category-playbooks.md`](references/category-playbooks.md): consumer tech and gear (specs, teardowns, repairability, generation pricing, accessories), subscriptions and courses (compounding cost, active hours, cancellation friction), vehicles, real estate, and financed assets (lifecycle cost, APR, depreciation, liquidity stress), B2B and SaaS (ROI, payback, NPV, build vs. buy), health and credence goods (human RCTs, effect sizes, USP/NSF/NIOSH/UL), or experiences and time-saving services (cost per hour saved, cancellation and weather risk).
- **Before Step 4**, read [`references/cost-math.md`](references/cost-math.md) for the TCO, cost-per-use, break-even, and opportunity-cost formulas.
- **Before Step 6**, read [`references/report-format.md`](references/report-format.md) for the report sections.
- **When saving a profile**, read [`references/buyer-profile-template.md`](references/buyer-profile-template.md).

## Proportional rigor

Scale to the commitment's 3-year cash outflow:

- **Everyday** (under \$100, one-time): street price, 50%-deflated cost per use, top failure mode, and a comparison against keeping what the user has or a proven budget pick, in a concise report.
- **Standard** (\$100 to \$2,500, or any subscription): full TCO, resale, deflated cost per use or hour, independent tests and 1-to-3 star failure audit, add-on check, and 12-month premortem.
- **High stakes** (over \$2,500, financed, vehicles, real estate, B2B): add discounted lifecycle cost, APR and monthly liquidity stress tests, break-even uses against renting, leasing, or building, and explicit opportunity cost against debt payoff or investing.

## Decision sequence

Run these six steps in order.

### Step 1: Load buyer context and interview the user

1. Check the buyer profile, memory, and prior turns for currency, tax region, financial guardrails, owned gear and ecosystem, active subscriptions, and past purchase lessons.
2. Separate the **fundamental objective** (the job to be done, such as sleeping through street noise) from the **means objective** (the specific product).
3. Settle the **5 verdict-flipping variables**:
   - **Fundamental objective**: the problem to solve and why now.
   - **Current baseline**: what the user owns, uses, or does today, and its exact pain point.
   - **Usage and horizon**: realistic frequency (uses per week or hours per day) and holding period $T$.
   - **Payment and guardrails**: cash vs. credit, financing, or BNPL; budget ceiling; any high-APR debt or emergency-fund limits.
   - **Dealbreakers**: physical size, OS or ecosystem fit, battery platform, safety, offline use, local warranty or repairability.
4. Run **Interview rounds** on these in everyday words (*"How often will you realistically use it?"*); context-answered variables become quick confirmations.

**Completion criterion**: The user has confirmed all 5 variables (or opted out, with assumptions stated).

### Step 2: Add the not-buying options and apply dealbreakers

1. Put the applicable baselines next to the target item: `Keep Current / Do Nothing` (\$0 extra), `Repair / Optimize Existing` (part, battery, consumable, or workflow fix), `Delay / Wait` (72 hours for everyday items, 30 days for major spend, or until a confirmed release or sale), `Rent / Borrow / Trial` (for temporary or uncertain need), and `Used / Refurbished / Previous-Gen` (85% to 95% of the utility after the steepest depreciation).
2. Apply **Elimination by Aspects**: test every option against the dealbreakers first and drop any that fails, whatever its other scores.

**Completion criterion**: Surviving options sit next to the strongest not-buying and low-cost alternative, and every dropped option names the dealbreaker it failed.

### Step 3: Verify claims and audit failure modes

Route each claim by type:

1. **Search attributes** (specs, dimensions, ports, license tiers, warranty and return terms): manufacturer documentation, spec sheets, filings, or contract terms.
2. **Experience attributes** (build, ergonomics, noise, battery life, software stability): independent instrumented testers (RTINGS, Wirecutter, Consumer Reports, Project Farm, Notebookcheck) and 6-to-24-month owner reports.
3. **Credence attributes** (health outcomes, supplement efficacy, safety, security): peer-reviewed human RCTs or primary lab and regulatory certifications (USP, NSF, NIOSH, UL, SOC 2).
4. **Failure search** (`"<product>" problem OR failure OR "after a year" OR recall OR warranty denied OR teardown`): recurring 1-to-3 star failure clusters and time to failure, silent component downgrades, review hijacking (old reviews on a new model), mandatory cloud accounts, and consumable lock-in.

**Completion criterion**: Every critical claim on surviving options is checked against primary or independent test sources, and the top failure modes and lock-in risks are documented with session-verified links.

### Step 4: Compute total cost, cost per use, and opportunity cost

Using `references/cost-math.md`, scaled to the rigor tier: TCO over $T$ net of realistic resale, cost per use or per hour at both stated and **50% of stated usage**, break-even uses against any rent or pay-per-use option, cost per net hour saved for time-saving purchases, and the opportunity cost of the same money.

**Completion criterion**: TCO, 50%-deflated cost per use or hour, any applicable break-even or cost per hour saved, and opportunity cost are calculated from verified numbers.

### Step 5: Debias and run a 12-month premortem

1. **Full-price test**: strip fake MSRP markdowns, bundle illusions, and "pennies a day" framing; check 90-to-365-day price history and ask whether the item is worth its price with no discount badge.
2. **Sunk-cost reset**: count prior money, time, or ecosystem spend as zero; compare only costs and value from today forward.
3. **Add-on audit (Diderot spiral)**: price the mounts, cases, adapters, cables, furniture, storage, or higher subscription tiers likely within 6 months.
4. **Premortem**: assume the buyer regrets this in 12 months; name the 2 to 3 likeliest causes (novelty fading after 2 weeks, lower usage, workflow friction, hidden recurring cost, cash strain), and weigh regret of buying (adjusted for returns and resale) against regret of skipping.

**Completion criterion**: Fake discount anchors are stripped, add-on costs are priced in, and the premortem causes and reversibility are evaluated.

### Step 6: Deliver the verdict

Pick one label from the **Verdict table** and write the report in plain language using `references/report-format.md`.

**Completion criterion**: The report gives one verdict, a side-by-side cost table against the best not-buying option, session-verified sources, and exact conditions that would change the verdict, with every internal term replaced by its user-facing label.

## Verdict table

| Verdict | When to assign |
| :--- | :--- |
| **`Buy`** | Passes every dealbreaker, beats keeping and renting even at 50% usage, shows no disqualifying failure mode, and fits cash and liquidity guardrails at street price. |
| **`Buy With Conditions / Wait`** | Right fit, but overpriced against price history, a refresh is imminent, or a prerequisite applies (a 30-day cooling-off, selling an item first, a target price of \$X or less). |
| **`Buy Alternative Instead`** | A purchase is warranted, but this model loses on TCO, reliability, or value to a competitor, an older or refurbished tier, or an open-source or one-time-purchase option. |
| **`Rent / Borrow / Trial First`** | Projected uses fall below break-even ($N_{\text{projected}} < N^*$), or preference uncertainty makes a cheap rental, borrow, or trial the better first step. |
| **`Keep Current / Repair`** | The current setup, or a cheap repair, battery swap, consumable, or workflow change, covers 80%+ of the goal for a fraction of the replacement TCO. |
| **`Do Not Buy`** | Fails a dealbreaker, has severe reliability or lock-in defects, relies on high-APR financing or emergency savings for a want, or is worth less than keeping the cash. |

## Guardrails

1. **Liquidity and APR**: financing a depreciating consumer good on revolving credit, fee-bearing BNPL, or deferred-interest promos (which can charge 25% to 30% APR back to day one if not paid off in time) means `Do Not Buy` or `Buy With Conditions / Wait`, unless the item is required for livelihood or health and safety.
2. **Session-verified prices and sources only**: cite only URLs, prices, and test data retrieved in this session (or provided by the user), with source name and date.
3. **No sycophancy**: treat enthusiasm (*"I really want X, convince me"*, *"I already decided, just checking"*) as a reason to apply the 50% usage test, add-on audit, and premortem harder, never to validate the impulse.
