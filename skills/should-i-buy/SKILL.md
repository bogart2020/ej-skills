---
name: should-i-buy
description: Evaluate buying and financial decisions across any category to deliver a calibrated verdict. Use when deciding whether to buy, upgrade, repair, or skip an item, comparing options or subscriptions, or weighing buying against renting, leasing, or building.
argument-hint: "[item, comparison, subscription, or financial commitment]"
license: MIT
---

# Should I Buy

Evaluate any purchase or financial commitment by establishing shared context on the **5 verdict-flipping variables**, benchmarking against **non-purchase baselines**, auditing real-world **failure modes**, computing full-lifecycle **Total Cost of Ownership (TCO)** and **50%-deflated utilization**, debiasing cognitive traps, and delivering a single calibrated **verdict** with explicit **reversal conditions**.

## Environment adaptation

Adapt tool use and memory discovery to the active runtime:

- **Chat environment** (Claude Desktop, web chat): inspect conversation history, project instructions, built-in memory, and any attached files for existing buyer context. Run web searches for independent lab tests, historical street prices, resale values, and long-term owner failure reports. When the user wants to persist their preferences or decision log, output a copyable Markdown snippet following [`references/buyer-profile-template.md`](references/buyer-profile-template.md).
- **Code and CLI environment** (Claude Code, Codex, Antigravity, Gemini CLI, Cursor, Windsurf): check whether `.agents/buyer-profile.md` or `~/.agents/buyer-profile.md` exists and read it before asking questions. Use Python or shell (`python3 -c ...`) for exact TCO, APR, Net Present Value (NPV), and break-even calculations. When comparing **3 or more candidate products** in a harness that supports subagents, dispatch parallel verification subagents so raw search pages stay out of the main context window; handle 1 or 2 items inline.

## Progressive disclosure pointers

- **Category playbooks**: Before running Step 3, read the matching section in [`references/category-playbooks.md`](references/category-playbooks.md):

| Purchase domain | What `references/category-playbooks.md` provides |
| :--- | :--- |
| **Consumer tech, appliances, and gear** | Spec/teardown verification, repairability checks, generation-curve pricing, Diderot accessory audits |
| **Subscriptions, digital services, and courses** | 1- and 3-year compounding cost, active-hour utilization, cancellation friction, open-source/one-time replacements |
| **Vehicles, real estate, and financed assets** | Full LCCA/TCO with APR, insurance, maintenance schedules, depreciation curves, and liquidity stress tests |
| **B2B, SaaS, and productive business assets** | ROI, payback period, NPV, Build vs. Buy (including 15% to 25% annual engineering maintenance), and exit/lock-in cost |
| **Health, supplements, and credence goods** | Human RCT verification, effect-size checks, third-party lab certifications (USP, NSF, NIOSH, UL), placebo stripping |
| **Experiences, travel, and time-saving services** | Cost per net hour saved, hedonic durability, cancellation/weather risk, and opportunity cost framing |

- **Persistent buyer profile**: When creating or updating `.agents/buyer-profile.md` or `~/.agents/buyer-profile.md` in Step 6, read [`references/buyer-profile-template.md`](references/buyer-profile-template.md).

## Proportional rigor

Scale verification and financial math to the commitment's 3-year cash outflow:

- **Everyday tier** (under \$100 one-time and non-recurring): compute street price, 50%-deflated Cost-Per-Use (`CPU`), top failure mode, and compare against `Keep Current` or a proven budget benchmark in a concise report.
- **Standard tier** (\$100 to \$2,500 one-time, or any recurring subscription): run the full 7-bucket TCO calculation, resale value lookup, 50%-deflated `CPU` / Cost-Per-Hour (`CPH`), independent lab and 1-to-3 star failure audit, Diderot spiral check, and 12-month premortem.
- **High-stakes tier** (over \$2,500, financed purchases, vehicles, real estate, or B2B commitments): run full discounted life-cycle cost analysis (LCCA), financing APR and monthly liquidity stress tests, break-even utilization (`N*`) against renting/leasing/building, and explicit opportunity-cost modeling against debt payoff or compounded investment.

## Decision sequence

Run these six steps in order.

### Step 1: Load buyer context and gate on verdict-flipping variables

1. **Check existing buyer context**: inspect `.agents/buyer-profile.md` or `~/.agents/buyer-profile.md` (when file tools exist) or platform memory and prior turns for currency, tax region, financial guardrails, owned ecosystem/gear, active subscriptions, and past purchase lessons.
2. **Separate fundamental from means objectives**: identify the underlying job to be done (**fundamental objective**, such as sleeping through street noise or cutting meal-prep time) separately from the specific commercial SKU (**means objective**).
3. **Audit the 5 verdict-flipping variables**:
   - **Fundamental objective**: the concrete problem to solve and why it matters now.
   - **Current baseline**: what the user currently owns, uses, or does today (`Status Quo`), and its exact pain point.
   - **Utilization and horizon**: realistic usage frequency (uses per week/month or hours per day) and expected holding period $T$.
   - **Financial mode and guardrails**: paying cash from discretionary funds versus credit/financing/BNPL, budget ceiling, and any high-APR debt or emergency-fund constraints.
   - **Hard knockout constraints**: non-negotiable dealbreakers (physical dimensions, OS/ecosystem compatibility, battery platform, safety, offline capability, local warranty/repairability).
4. **Adaptive Context Gate**: when any of the 5 verdict-flipping variables is missing or ambiguous (and the user has not requested an immediate one-shot verdict), pause and ask **2 to 4 concise, high-information-gain questions** before rendering a verdict. Repeat in a follow-up round only when an answer exposes a new dependency until shared understanding is reached.

**Completion criterion**: All 5 verdict-flipping variables are bounded via existing buyer context or user confirmation, or the user explicitly requested an immediate verdict with stated assumptions.

### Step 2: Benchmark non-purchase baselines and prune by knockouts

1. **Generate mandatory baselines**: include the applicable non-purchase and low-capital baselines in the comparison set alongside the target item:
   - `Keep Current / Do Nothing`: continue with the existing setup at \$0 incremental spend.
   - `Repair / Optimize Existing`: replace a degraded part, battery, or consumable, or tune current workflows.
   - `Delay / Wait`: defer for a cooling-off window (72 hours for everyday items, 30 days for major discretionary spend) or until a confirmed release/discount cycle.
   - `Rent / Borrow / Trial`: satisfy temporary or uncertain demand without ownership depreciation.
   - `Used / Refurbished / Previous-Gen`: capture 85% to 95% of functional utility after the steepest retail depreciation drop.
2. **Apply Elimination by Aspects (EBA)**: test every candidate against the hard knockout constraints from Step 1 first. Disqualify any option that fails a non-negotiable constraint regardless of its scores on secondary features.

**Completion criterion**: Surviving candidates are paired with the strongest non-purchase baseline and low-capital alternative, and every disqualified option names the exact knockout constraint it failed.

### Step 3: Verify attributes and audit failure modes

Consult [`references/category-playbooks.md`](references/category-playbooks.md) for the item's category, then route product claims by information-economic class:

1. **Search attributes** (specs, dimensions, ports, licensing tiers, warranty/return terms): verify against Tier 1 manufacturer documentation, spec sheets, regulatory filings, or contract terms.
2. **Experience attributes** (real-world build quality, ergonomics, noise, battery longevity, software stability): verify via independent instrumental testers (such as RTINGS, Wirecutter, Consumer Reports, Project Farm, Notebookcheck) and 6-to-24 month owner reports.
3. **Credence attributes** (health outcomes, supplement efficacy, safety ratings, security guarantees): verify against peer-reviewed human randomized controlled trials (RCTs) or primary regulatory/lab certifications (USP, NSF, NIOSH, UL, SOC 2).
4. **Adversarial failure-mode search**: run targeted queries (`"<product>" problem OR failure OR "after a year" OR recall OR warranty denied OR teardown`) to identify:
   - Recurring 1-to-3 star failure clusters and average time-to-failure.
   - Silent component downgrades, review hijacking (old reviews attached to a new SKU), mandatory cloud accounts, or proprietary consumable lock-in.

**Completion criterion**: Every critical Search, Experience, and Credence claim on surviving candidates is checked against primary or independent test sources, and top real-world failure modes and lock-in risks are documented with session-verified links.

### Step 4: Compute TCO, unit utilization, and opportunity cost

Compute lifecycle numbers over holding horizon $T$ (in years or months), scaled to the Proportional Rigor tier:

1. **Total Cost of Ownership ($\text{TCO}(T)$)**:
   $$\text{TCO}(T) = C_{\text{acquisition}} + C_{\text{onboarding}} + C_{\text{financing}} + C_{\text{operating}}(T) + C_{\text{maintenance}}(T) + C_{\text{exit}} - V_{\text{salvage}}(T)$$
   - $C_{\text{acquisition}}$: street price + sales/VAT tax + shipping/customs + mandatory day-one accessories.
   - $C_{\text{onboarding}}$: installation, setup, migration, or learning-curve cost.
   - $C_{\text{financing}}$: total interest and fees paid over any loan, credit, or BNPL term.
   - $C_{\text{operating}}(T)$: electricity/fuel, consumables (filters, ink, pods, blades), insurance, and recurring subscriptions over $T$.
   - $C_{\text{maintenance}}(T)$: scheduled servicing, battery replacements, and expected out-of-warranty repairs.
   - $C_{\text{exit}} - V_{\text{salvage}}(T)$: realistic resale or trade-in value at $T$ from completed secondary-market sales minus marketplace selling fees (typically 10% to 15%) or termination penalties.
2. **Deflated Unit Utilization ($\text{CPU}$ and $\text{CPH}$)**:
   - Compute Cost-Per-Use ($\text{TCO}(T) / \text{total uses}$) or Cost-Per-Hour ($\text{TCO}(T) / \text{total active hours}$) at both stated usage and **50% deflated usage** ($0.5 \times \text{stated usage}$) to guard against optimism bias.
3. **Break-Even Utilization ($N^*$) and Time-Value Equivalence**:
   - When a rent, lease, or pay-per-use option exists at cost $R$ per use and ownership has variable cost $v$ per use, compute break-even uses:
     $$N^* = \frac{C_{\text{acquisition}} + C_{\text{onboarding}} + C_{\text{financing}} + C_{\text{exit}} - V_{\text{salvage}}(T)}{R - v}$$
   - When the purchase saves time, compute **Cost per Net Hour Saved** ($\Delta \text{TCO}(T) / \Delta H_{\text{net saved}}$, subtracting setup, cleaning, and maintenance time) and compare against the user's net hourly rate.
4. **Explicit Opportunity Cost**:
   - Frame $\text{TCO}(T)$ against concrete competing uses of the same funds: paying off high-APR debt (20% to 29% guaranteed return), preserving emergency-fund liquidity, compounding at a conservative real return over $T$ and 10 years, or funding a higher-priority goal.

**Completion criterion**: $\text{TCO}(T)$, 50%-deflated $\text{CPU}$/$\text{CPH}$, applicable break-even ($N^*$) or cost-per-hour-saved figures, and explicit opportunity cost are calculated with verified numbers.

### Step 5: Debias and run a 12-month premortem

Stress-test the purchase against four behavioral traps:

1. **Zero-Anchor / Full-Price Test (Transaction vs. Acquisition Utility)**: strip fake MSRP markdowns, bundle illusions, and "pennies-a-day" framing. Check 90-to-365 day street price history and verify whether the item is worth its current price based purely on utility if no discount badge existed.
2. **Sunk Cost Reset**: set all prior money, time, or ecosystem spend to $C_{\text{sunk}} = 0$. Compare only prospective incremental costs and utility from today forward.
3. **Diderot Spiral Audit**: itemize complementary purchases triggered within 6 months of buying the primary item (mounts, cases, adapters, upgraded cables, furniture, storage, higher subscription tiers) and include probable add-ons in the real budget impact.
4. **12-Month Purchase Premortem**: assume 12 months have passed and the buyer regrets this decision. State the 2 to 3 most likely failure causes (hedonic adaptation after 2 weeks, lower-than-expected usage, ergonomic/workflow friction, hidden recurring cost, or cash-flow strain) and weigh **Action Regret** (buying and regretting, adjusted for return policy and resale liquidity) against **Inaction Regret** (skipping and wishing you had bought).

**Completion criterion**: Fake discount anchors are stripped, Diderot add-on costs are priced in, and the 12-month premortem failure causes and reversibility are evaluated.

### Step 6: Render the calibrated verdict and reversal conditions

Assign one categorical label from the **Verdict taxonomy** below and render the Decision Report inline using four sections (plus an optional fifth memory prompt when new durable context was learned):

1. **Verdict Summary**:
   - **Verdict**: `[Buy | Buy With Conditions / Wait | Buy Alternative Instead | Rent / Borrow / Trial First | Keep Current / Repair | Do Not Buy]`
   - **Bottom Line**: 2 to 3 decisive sentences stating the verdict, the primary financial and functional reason, the net $\text{TCO}(T)$, and the 50%-deflated $\text{CPU}$ or $\text{CPH}$.
2. **TCO, Utilization & Baseline Comparison**:
   - Present a side-by-side Markdown table comparing the **Target Item**, the **Best Competing Alternative** (or Used/Refurbished tier), and the **Strongest Non-Purchase Baseline** (`Keep Current / Repair` or `Rent / Trial`) across: Upfront Cost, Hidden/Recurring Costs, Net Resale Value ($V_{\text{salvage}}$), Net $\text{TCO}(T)$, 50%-Deflated $\text{CPU}$/$\text{CPH}$, and Primary Trade-off.
3. **Verification, Failure Modes & Behavioral Audit**:
   - **Evidence & Failure Modes**: what independent testing and 1-to-3 star long-term owner reports show, with session-verified links and publication dates.
   - **Diderot & Opportunity Cost Check**: itemized secondary add-on costs and what else $\text{TCO}(T)$ buys or earns.
   - **12-Month Premortem**: the likeliest regret scenario and how easily the decision can be reversed (return policy, restocking fees, resale liquidity).
4. **Reversal Conditions & Action Plan**:
   - **What would flip this verdict**: state exact, falsifiable numerical or contextual thresholds that would change the verdict (for example, *"Flips from `Do Not Buy` to `Buy` if street price drops below \$X or verified usage exceeds Y uses/month"*).
   - **Next steps**: if buying or trialing, state the target price ceiling, recommended buying channel/tier, and a return-window stress-test checklist; if skipping or waiting, state the exact price alert or trigger condition to set.
5. **Buyer Profile Update (when applicable)**:
   - If the session revealed new durable buyer context (currency, budget guardrails, hourly time valuation, owned gear/subscriptions) or a final purchase decision, ask in one line whether to save it to `.agents/buyer-profile.md` / `~/.agents/buyer-profile.md` (following [`references/buyer-profile-template.md`](references/buyer-profile-template.md)).

**Completion criterion**: The report delivers a single unambiguous verdict from the 6-level taxonomy, a side-by-side TCO and utilization table against the non-purchase baseline, session-verified sources, and explicit numerical reversal conditions.

---

## Reference rules

### Verdict taxonomy

| Verdict | When to assign |
| :--- | :--- |
| **`Buy`** | Passes all hard knockouts, delivers positive net utility over the `Keep Current` and `Rent` baselines even at 50%-deflated usage, exhibits no disqualifying failure modes, and fits cash/liquidity guardrails at current street price. |
| **`Buy With Conditions / Wait`** | Sound match for the fundamental objective, but currently overpriced relative to street history, awaiting an imminent product refresh, or requires a specific prerequisite (such as clearing a 30-day cooling-off window, selling an existing item first, or hitting a target sale price $\le \$X$). |
| **`Buy Alternative Instead`** | The fundamental objective warrants a purchase, but the target SKU is dominated on TCO, reliability, or utility by a competing model, a previous-generation/refurbished tier, or an open-source/one-time-purchase alternative. |
| **`Rent / Borrow / Trial First`** | Projected usage falls below the break-even threshold ($N_{\text{projected}} < N^*$), or high preference uncertainty makes a low-cost rental, borrow, or time-boxed trial superior before committing capital. |
| **`Keep Current / Repair`** | The existing setup (or a low-cost repair, battery swap, consumable upgrade, or workflow change) satisfies 80%+ of the fundamental objective at a fraction of the replacement TCO. |
| **`Do Not Buy`** | Fails a hard knockout constraint, suffers from severe reliability or lock-in defects, relies on high-APR financing or emergency savings for a discretionary want, or delivers negative net utility relative to keeping the cash. |

### Financial & verification guardrails

1. **Liquidity and APR guardrail**: Financing a depreciating consumer good with revolving credit card debt, fee-bearing BNPL, or deferred-interest promos (where missing the payoff date retroactively charges 25% to 30% APR from day one) triggers `Do Not Buy` or `Buy With Conditions / Wait` unless the item is strictly required for livelihood or health/safety.
2. **Session-verified prices and sources only**: Cite only URLs, prices, and test data retrieved and inspected during the current session (or explicitly provided by the user). State the source name and date on every citation.
3. **Anti-sycophancy rule**: Treat user enthusiasm (*"I really want X, convince me"* or *"I already decided on X, just checking"*) as a signal to increase scrutiny on the 50%-deflated utilization test, Diderot spiral, and 12-month premortem rather than validating the impulse.
