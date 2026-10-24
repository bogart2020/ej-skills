# Category Evaluation Playbooks

Specialized verification, Total Cost of Ownership (TCO), and failure-mode checks for the six purchase domains referenced in [`SKILL.md`](../SKILL.md).

## Consumer tech, appliances, and gear

1. **Separate spec-sheet marketing from sustained performance**:
   - Check independent instrumental benchmarks (such as RTINGS, Wirecutter, Consumer Reports, Notebookcheck, Project Farm, TechPowerUp, ASR) for sustained thermal performance, actual battery life, acoustic noise (dBA), and panel/sensor accuracy rather than burst marketing claims.
2. **Check the generation and depreciation curve**:
   - Compare the target SKU against the **immediately preceding generation** and **manufacturer-certified refurbished** pricing. In laptops, smartphones, cameras, audio gear, and appliances, the prior generation often delivers 90% to 95% of functional utility at a 25% to 45% discount after the first-year retail depreciation drop.
   - Check release-cycle cadence (for example, annual autumn refreshes or trade-show announcements) so the user never pays full retail right before a revision.
3. **Audit repairability, parts availability, and software sunsetting**:
   - Verify whether wear components (batteries, seals, heating elements, ear pads, switches, brushes) are user-replaceable with standard tools or serialized/glued.
   - For smart devices and connected appliances, check whether core functionality works **100% locally offline** if the vendor shuts down its cloud servers or places features behind a post-purchase subscription paywall.
4. **Price the Diderot ecosystem spiral**:
   - Itemize day-one and 6-month accessories: proprietary docks, cables, memory cards, lenses, cases, mounts, replacement filters, or upgraded desk/power infrastructure.

## Subscriptions, digital services, and courses

1. **Convert monthly framing into 1-year and 3-year compounding totals**:
   - Always state the 1-year and 3-year cash outflow alongside the monthly price, including introductory-promo expiration jumps, per-seat minimums, add-on usage tiers, and taxes.
2. **Compute Cost per Active Hour and audit overlap**:
   - Divide monthly/annual cost by realistic **active hours used per month** (deflated by 50% after month 1 when novelty wears off).
   - Check existing user context for overlapping subscriptions (for example, paying for three streaming services or multiple overlapping AI/productivity tools simultaneously) and evaluate a **rotation strategy** (subscribing for 1 month, completing the specific project or catalog, and canceling immediately).
3. **Benchmark against free, open-source, and one-time-license alternatives**:
   - Before approving a recurring subscription, check whether a one-time perpetual license, open-source tool, library card access, or built-in OS utility covers the fundamental objective.
4. **Verify cancellation and data-export friction**:
   - Check whether cancellation is self-serve online or requires phone/chat retention gauntlets, annual lock-in with early termination penalties, or proprietary file formats that trap user data.

## Vehicles, real estate, and financed assets

1. **Run full 7-bucket Life-Cycle Cost Analysis (LCCA)**:
   - Never evaluate a vehicle or property on monthly payment alone. Dealers and lenders stretch loan terms (72 to 84 months on cars) to mask inflated principal and total interest.
   - Compute total 5-year (or holding-horizon $T$) outflow:
     - **Acquisition & closing**: purchase price, sales/transfer tax, registration/title, dealer/origination fees, inspection fees.
     - **Financing**: exact APR, loan term, total cumulative interest paid, and down-payment opportunity cost.
     - **Operating**: insurance quotes for the specific model/zip code, fuel or electricity ($\text{annual miles} / \text{MPG or mi/kWh} \times \text{local rate}$), HOA fees, property taxes, parking/tolls.
     - **Maintenance & consumables**: tires, brakes, scheduled fluid/timing service, out-of-warranty repair reserve (or 1% to 2% of property value per year for home maintenance).
     - **Depreciation & exit**: realistic 5-year residual value ($V_{\text{salvage}}$) minus selling/realtor transaction costs (typically 6% to 10% for real estate).
2. **Run liquidity and cash-flow stress tests**:
   - Check whether total monthly carrying costs leave adequate emergency-fund runway and whether the asset becomes underwater (loan balance exceeding net resale value) during years 1 to 3.
3. **Check model-year failure clusters and recalls**:
   - Query NHTSA recalls/complaints, long-term reliability indices, and owner forums for transmission, engine, battery degradation, rust, or structural issues specific to that exact model year and trim.

## B2B, SaaS, and productive business assets

1. **Model Net Present Value (NPV), Payback Period, and ROI**:
   - Quantify expected cash inflows or hard cost savings ($\Delta \text{Revenue} + \Delta \text{Labor Saved} - \Delta \text{Operating Cost}$) over horizon $T$.
   - Discount optimistic productivity or revenue gains by 50% when computing the conservative **Payback Period** (in months) and **NPV**.
2. **Run a realistic Build vs. Buy comparison**:
   - When weighing commercial SaaS/infrastructure against building in-house, price both:
     - **Buy TCO**: base platform fee + per-seat/MAU/ingestion overage scaling at $2\times$ and $5\times$ growth + integration engineering hours + contract renewal price hikes.
     - **Build TCO**: initial engineering build hours $\times$ fully loaded hourly engineering cost + **15% to 25% of initial build cost per year** for ongoing maintenance, security patching, on-call incidents, and compliance.
   - If the capability is non-core undifferentiated plumbing and commercial TCO is below the fully loaded build + maintenance cost, favor `Buy` (or open-source self-hosting); if vendor lock-in or usage-based pricing explodes at scale, price the migration exit cost ($C_{\text{exit}}$) upfront.
3. **Audit security, compliance, and exit portability**:
   - Verify SOC 2 / ISO 27001 / GDPR compliance, SLA uptime credits, API rate limits, and bulk data export formats before signing multi-year commitments.

## Health, supplements, and credence goods

1. **Demand human Randomized Controlled Trials (RCTs) and meta-analyses**:
   - Testimonials, influencer sponsorships, "clinically proven" marketing badges without linked papers, *in vitro* petri-dish assays, and rodent studies do not establish human efficacy.
   - Search peer-reviewed systematic reviews and human RCTs for the **exact active ingredient, dosage, and bioavailable form**. Check absolute effect size (not just relative percentage change) and sample size ($n$).
2. **Verify independent third-party purity and safety certifications**:
   - Because supplements and wellness devices often lack pre-market regulatory approval, require independent batch certification (**USP Verified**, **NSF Certified for Sport**, **ConsumerLab**, **UL**, **NIOSH**, or **FDA 510(k) clearance** for medical devices) to rule out heavy-metal contamination, under-dosing, or adulteration.
3. **Compare against foundational lifestyle or generic baselines**:
   - Benchmark proprietary blends or wellness gadgets against generic single-ingredient equivalents (for example, generic USP creatine monohydrate or caffeine versus a \$75/month proprietary powder) and zero-cost behavioral baselines (sleep, resistance training, whole foods).

## Experiences, travel, and time-saving services

1. **Evaluate Time-Saving Purchases via Cost per Net Hour Saved**:
   - Empirical research (Whillans et al., 2017, *PNAS*) shows that buying time out of unpleasant chores reliably increases well-being when affordable.
   - Compute $\text{Cost per Net Hour Saved} = \Delta \text{Cost} / (\text{Gross Hours Saved} - \text{Coordination/Setup/Cleanup Hours})$. Compare against the buyer's after-tax hourly wage or valued leisure rate.
2. **Audit total trip or event TCO beyond headline fare**:
   - For travel, tickets, and experiences, sum headline fare + mandatory resort/service/ticketing fees + baggage/seat fees + ground transit + lodging taxes + meals + pet/childcare + unpaid PTO cost.
3. **Verify refundability and tail-risk protection**:
   - Check cancellation windows, change penalties, weather/illness disruption risk, and whether existing credit-card travel protection or refundable booking tiers cover downside risk better than third-party add-on insurance.
