# Buying-Decision & Purchase-Evaluation Skill Best Practices: Primary-Source Synthesis

**Date:** 2026-10-24  
**Repository:** `ej-skills`  
**Scope:** Multi-Criteria Decision Analysis (MCDA), Total Cost of Ownership (TCO) and life-cycle economics, behavioral economics debiasing, information economics of product verification, conversational preference elicitation, and cross-platform AI skill design.

---

## Executive Summary

When a human asks an AI assistant *"Should I buy X?"*, *"Is X worth it?"*, or *"Which Y should I get?"*, default LLM behavior suffers from **sycophantic affirmation** and **spec-sheet recitation**: the model summarizes marketing copy, lists generic pros and cons, and hedges with *"It depends on your needs and budget."*

Building a rigorous, domain-universal **Buying-Decision & Purchase-Evaluation Skill**—capable of evaluating everything from a \$15 kitchen tool, a \$20/month SaaS subscription, or a \$2,500 laptop to a \$45,000 vehicle, enterprise B2B software, or residential real estate—requires synthesizing five primary research traditions:

1. **Decision Analysis & Multi-Criteria Decision Analysis (MCDA):** Ralph Keeney's **Value-Focused Thinking** (1992) and Hammond, Keeney, & Raiffa's **PrOACT** framework (1999) to separate fundamental objectives from specific products; Amos Tversky's **Elimination by Aspects (EBA)** (1972) for non-compensatory dealbreaker pruning; and **Multi-Attribute Utility Theory (MAUT) / SMART** (Keeney & Raiffa, 1976; Edwards, 1977) for weighted trade-offs against the **Status Quo / Do Nothing / Repair / Rent** baseline.
2. **Total Cost & Utilization Economics:** Gartner's **Total Cost of Ownership (TCO)** (Kirwin, 1987), **NIST Handbook 135 Life-Cycle Cost Analysis (LCCA)** (Kneifel & Webb, 2025), and **ISO 15686-5** to surface hidden operating, financing, consumables, switching, and depreciation costs; **Cost-Per-Use (CPU)** and **Break-Even Utilization** modeling; **Time-Value Equivalence** (Whillans et al., 2017); and explicit **Opportunity Cost** & **Liquidity Guardrails** (Frederick et al., 2009; Spiller, 2011; CFPB BNPL reports, 2022–2025).
3. **Behavioral Economics & Cognitive Debiasing:** Richard Thaler's **Mental Accounting** (1985, 1999) to sever **Acquisition Utility** from **Transaction Utility** (fake MSRP markdowns); Hal Arkes & Catherine Blumer's **Sunk Cost** debiasing (1985); Dunn, Gilbert, & Wilson's **Hedonic Adaptation** principles (2011); David Laibson's **Hyperbolic Discounting** (1997); Grant McCracken's **Diderot Effect** (1988) for secondary purchase spirals; and Gary Klein's **Project Premortem** (2007) paired with **Regret Theory** (Bell, 1982; Loomes & Sugden, 1982).
4. **Information Economics & Product Verification:** Phillip Nelson's (1970) and Darby & Karni's (1973) taxonomy of **Search, Experience, and Credence Attributes**, paired with the **FTC Endorsement Guides (16 CFR Part 255)** and **FTC Consumer Review Rule (16 CFR Part 465)**, to route verification toward independent lab testing, long-term failure distributions, and primary regulatory evidence.
5. **Conversational Preference Elicitation & Calibrated Verdicts:** Pu & Chen's (2008, 2012) research on **critiquing and high-information-gain elicitation** to gather missing context with minimal friction before rendering a non-hedging verdict backed by explicit **reversal conditions**.

---

## 1. Decision Science & Multi-Criteria Decision Analysis (MCDA)

### 1.1 Value-Focused Thinking vs. Alternative-Focused Thinking (Keeney, 1992; Hammond, Keeney, & Raiffa, 1999)

Most buyers fall into what Ralph L. Keeney calls **Alternative-Focused Thinking**: they start with a narrow set of pre-packaged commercial products (e.g., *"Should I buy the Sony WH-1000XM5 or Bose QuietComfort Ultra?"*) and try to pick one before clarifying the underlying problem.

- **Primary Sources:**
  - Ralph L. Keeney (1992), *Value-Focused Thinking: A Path to Creative Decisionmaking*, Harvard University Press ([ISBN: 978-0674931978](https://www.hup.harvard.edu/books/9780674931978)).
  - John S. Hammond, Ralph L. Keeney, & Howard Raiffa (1999), *Smart Choices: A Practical Guide to Making Better Decisions*, Harvard Business Review Press ([ISBN: 978-0875848570](https://store.hbr.org/product/smart-choices-a-practical-guide-to-making-better-decisions/8575)).
- **Core Mechanisms:**
  1. **Fundamental Objectives vs. Means Objectives:** By asking *"Why is this objective important?"* repeatedly (the **WITI test**: *Why Is That Important?*), a decision-maker separates **means objectives** (buying a specific gadget, upgrading a subscription tier, buying a second car) from **fundamental objectives** (blocking office noise during deep work, reducing commute stress, preserving liquid savings).
  2. **The PrOACT Sequence:** Hammond, Keeney, and Raiffa structure every consequential choice around five core elements plus uncertainty/risk:
     - **Pr**oblem: Frame the root problem to be solved, not the product being pitched.
     - **O**bjectives: Specify fundamental user criteria (performance, durability, ergonomics, liquidity preservation, flexibility).
     - **A**lternatives: Generate a complete set of alternatives—crucially including **non-purchase baselines**.
     - **C**onsequences: Map how each alternative performs against each objective in a consequences table.
     - **T**rade-offs: Eliminate dominated options and make explicit value trade-offs across remaining contenders.
  3. **Mandatory Non-Purchase Baselines:** In *Value-Focused Thinking*, Keeney shows that restricting the choice set to commercial SKUs biases the outcome toward spending. Every rigorous purchase evaluation must benchmark the target item against five non-purchase or low-capital baselines:
     - **Status Quo / Do Nothing:** Keep using the current solution or skip the category altogether.
     - **Delay / Wait ($t + \Delta t$):** Defer purchase for a cooling-off window (e.g., 72 hours for small items, 30 days for major discretionary purchases) or until a known product/price inflection point.
     - **Repair / Reconfigure / Optimize Existing:** Replace a battery/part, clean/tune existing gear, or adjust workflow at near-zero cost.
     - **Rent / Borrow / Trial / Share:** Satisfy episodic demand without taking on ownership depreciation, storage, and maintenance.
     - **Used / Refurbished / Previous-Generation Tier:** Capture 85–95% of functional utility after the steepest portion of the retail depreciation curve has already been paid by the first owner.

### 1.2 Two-Stage Filtering: Elimination by Aspects (EBA) + Multi-Attribute Utility Theory (MAUT / SMART)

Human buyers and AI agents alike struggle when they try to score 15 attributes across 10 products simultaneously. Decision science resolves this by combining a **non-compensatory first pass** with a **compensatory second pass**:

- **Primary Sources:**
  - Amos Tversky (1972), *"Elimination by aspects: A theory of choice"*, *Psychological Review*, Vol. 79, No. 4, pp. 281–299 ([DOI: 10.1037/h0032955](https://doi.org/10.1037/h0032955)).
  - Ralph L. Keeney & Howard Raiffa (1976), *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*, Wiley / Cambridge University Press ([DOI: 10.1017/CBO9781139174084](https://doi.org/10.1017/CBO9781139174084)).
  - Ward Edwards (1977), *"How to Use Multiattribute Utility Measurement for Social Decisionmaking"*, *IEEE Transactions on Systems, Man, and Cybernetics*, Vol. SMC-7, No. 5, pp. 326–340 ([DOI: 10.1109/TSMC.1977.4309720](https://doi.org/10.1109/TSMC.1977.4309720)).

| Stage | Methodology | Mathematical / Logical Rule | Role in an Agentic Buying Skill |
| :--- | :--- | :--- | :--- |
| **Stage 1: Knockout Pruning** | **Elimination by Aspects (EBA)** (Tversky, 1972) | **Non-compensatory:** An option is immediately disqualified if it fails any hard constraint $c_k$, regardless of how high it scores on other attributes. | Check **dealbreakers first**: hard cash budget ceiling, physical dimensions/compatibility, safety/regulatory compliance, OS/ecosystem compatibility, data privacy requirements, or unacceptable vendor lock-in. |
| **Stage 2: Trade-off Scoring** | **MAUT / SMART** (Keeney & Raiffa, 1976; Edwards, 1977) | **Compensatory:** For surviving candidates $x_i$, overall utility is $U(x_i) = \sum_{j=1}^{m} w_j u_j(x_{ij})$, where $\sum w_j = 1$ and $u_j$ scales attribute performance to $[0, 100]$. | Compare only the 2–4 surviving alternatives (including the best non-purchase baseline) across weighted user criteria, and apply **dominance elimination** (discard any option that is worse or equal on all attributes and strictly worse on at least one). |

---

## 2. Financial & Total Cost Accounting Frameworks

### 2.1 Total Cost of Ownership (TCO) & Life-Cycle Cost Analysis (LCCA)

Retail sticker price ($P_{\text{sticker}}$) is frequently a fraction of the true financial commitment—especially for printers, vehicles, smart-home hardware, espresso machines, SaaS platforms, pets, and real estate.

- **Primary Sources:**
  - Bill Kirwin / Gartner Group (1987), *Total Cost of Ownership (TCO)* methodology for IT asset evaluation ([Gartner Glossary: Total Cost of Ownership](https://www.gartner.com/en/information-technology/glossary/total-cost-of-ownership-tco)).
  - Joshua D. Kneifel & David Webb (2025), *Life-Cycle Costing Manual for the Federal Energy Management Program*, **NIST Handbook 135** (2025 Edition), National Institute of Standards and Technology ([DOI: 10.6028/NIST.HB.135e2025](https://doi.org/10.6028/NIST.HB.135e2025)).
  - **ISO 15686-5:2017**, *Buildings and constructed assets — Service-life planning — Part 5: Life-cycle costing*, International Organization for Standardization ([ISO 15686-5 OBP](https://www.iso.org/obp/ui/#iso:std:iso:15686:-5:ed-2:v1:en)).

Synthesizing NIST Handbook 135, ISO 15686-5, and Gartner TCO yields the **Universal Consumer & Commercial TCO Equation** over a realistic holding horizon $T$ (in years or months) at real discount rate $r$:

$$\text{TCO}(T) = C_{\text{acquisition}} + C_{\text{onboarding}} + \sum_{t=1}^{T} \frac{C_{\text{operating}}(t) + C_{\text{maintenance}}(t) + C_{\text{financing}}(t)}{(1 + r)^t} + \frac{C_{\text{exit}}(T) - V_{\text{salvage}}(T)}{(1 + r)^T}$$

Every purchase evaluation must decompose $\text{TCO}(T)$ into seven auditable buckets:

1. **Acquisition Costs ($C_{\text{acquisition}}$):** Base price + sales/VAT tax + shipping/freight + customs/import duties + mandatory accessories (cables, cases, adapters, mounts) required for day-one operation.
2. **Onboarding & Implementation Costs ($C_{\text{onboarding}}$):** Installation, calibration, data migration, training/learning-curve time, or contractor setup.
3. **Financing & Carrying Costs ($C_{\text{financing}}$):** Total interest paid over the loan term, origination fees, mandatory financing insurance, or lost credit card rewards/cash Discounts.
4. **Recurring Operating & Consumable Costs ($C_{\text{operating}}$):**
   - *Hardware/Appliances/Vehicles:* Electricity/fuel ($\text{kWh} \times \text{rate}$ or $\text{miles}/\text{MPG} \times \text{fuel price}$), proprietary filters, ink/toner, pods/beans, blades, lubricants, insurance premiums, registration/taxes.
   - *Software/SaaS/Smart Devices:* Mandatory cloud subscriptions behind hardware paywalls, per-seat tier jumps, API usage overages, storage fees.
5. **Maintenance, Repair & Downtime Risk ($C_{\text{maintenance}}$):** Scheduled servicing, out-of-warranty failure probability $\times$ repair cost, battery replacement cycles, and cost of downtime.
6. **Switching & Lock-In / Exit Costs ($C_{\text{exit}}$):** Early termination fees, proprietary format export penalties, disposal/decommissioning fees, or realtor/marketplace selling commissions (typically 6–15% on secondary marketplaces like eBay/Reverb/real estate).
7. **Residual / Salvage Value ($V_{\text{salvage}}$):** Realistic net resale or trade-in value at year $T$ based on completed secondary-market listings (not asking prices), minus selling fees and shipping.

### 2.2 Unit Economics of Utilization & Time-Value Equivalence

A \$1,200 ergonomic chair used 2,500 hours/year for 10 years costs **\$0.048/hour**, whereas a \$300 kitchen appliance used 4 times before gathering dust in a cabinet costs **\$75.00/use**.

#### A. Cost-Per-Use (CPU) and Cost-Per-Hour (CPH)
$$\text{CPU} = \frac{\text{TCO}(T)}{u \cdot T}, \qquad \text{CPH} = \frac{\text{TCO}(T)}{h \cdot T}$$
where $u$ is realistic annual uses and $h$ is realistic annual active hours over holding period $T$.

#### B. Break-Even Utilization Threshold ($N^*$) — Buy vs. Rent / Borrow / Pay-Per-Use
When an alternative exists to rent, lease, or pay-per-use at marginal cost $R$ per use (or per day), and buying incurs fixed net ownership cost $F_{\text{net}} = C_{\text{acquisition}} + C_{\text{fixed\_maint}} - V_{\text{salvage}}$ plus variable cost $v$ per use:

$$N^* = \frac{F_{\text{net}}}{R - v}$$

- If projected total uses over the holding horizon $N_{\text{projected}} < N^*$, **Rent / Borrow / Pay-Per-Use** strictly dominates buying financially.
- **Anti-Optimism Deflator:** Consumers systematically overestimate future usage frequency of aspirational goods (fitness equipment, hobby gear, specialized cookware). An advisor should test sensitivity at **50% of the user's optimistic usage estimate** ($0.5 \times N_{\text{projected}}$).

#### C. Time-Value Equivalence (Buying Time vs. Buying Stuff)
- **Primary Source:** Ashley V. Whillans, Elizabeth W. Dunn, Paul Smeets, René Bekkers, & Michael I. Norton (2017), *"Buying time promotes happiness"*, *Proceedings of the National Academy of Sciences (PNAS)*, Vol. 114, No. 32, pp. 8523–8527 ([DOI: 10.1073/pnas.1706541114](https://doi.org/10.1073/pnas.1706541114)).
- **Core Empirical Finding:** Across working adults in the US, Canada, Denmark, and the Netherlands ($N > 6,000$), spending money to **remove unpleasant, time-consuming tasks** (time-saving purchases) reliably reduced time-stress and increased life satisfaction across income brackets, whereas purely material purchases did not.
- **Implied Hourly Wage Test:** For time-saving or productivity purchases, compute the **Cost per Net Hour Saved**:
  $$\text{Cost per Hour Saved} = \frac{\Delta \text{TCO}(T)}{\Delta H_{\text{saved}}(T)}$$
  where $\Delta H_{\text{saved}}(T)$ is gross time saved *minus* setup, maintenance, troubleshooting, and cleaning time. If $\text{Cost per Hour Saved}$ is well below the buyer's after-tax hourly value of time (or billing rate) and liquidity guardrails are met, the purchase has positive time-utility.

### 2.3 Opportunity Cost Neglect, Financing Traps & Liquidity Guardrails

#### A. Opportunity Cost Neglect (Frederick et al., 2009; Spiller, 2011)
- **Primary Sources:**
  - Shane Frederick, Nathan Novemsky, Jing Wang, Ravi Dhar, & Stephen Nowlis (2009), *"Opportunity Cost Neglect"*, *Journal of Consumer Research*, Vol. 36, No. 4, pp. 553–561 ([DOI: 10.1086/599764](https://doi.org/10.1086/599764)).
  - Stephen A. Spiller (2011), *"Opportunity Cost Consideration"*, *Journal of Consumer Research*, Vol. 38, No. 4, pp. 595–610 ([DOI: 10.1086/660045](https://doi.org/10.1086/660045)).
- **Core Empirical Finding:** Frederick et al. (2009) demonstrated that consumers routinely ignore outside uses of money unless those outside alternatives are **explicitly framed in the choice set**. Simply changing a prompt from *"Buy / Do not buy this \$14.99 video"* to *"Buy this \$14.99 video / Keep the \$14.99 for other purchases"* dropped purchase propensity by **20 percentage points** (from 75% to 55%). Spiller (2011) showed that opportunity cost consideration only occurs spontaneously when consumers experience immediate resource constraints or use tightly partitioned budgets.
- **Agentic Design Rule:** An AI buying advisor must **always make opportunity cost explicit** by translating $\text{TCO}(T)$ into concrete competing uses of capital:
  1. **High-Interest Debt Payoff:** Paying down revolving credit card debt at $20\text{–}29\%$ APR provides a guaranteed, tax-free return of $20\text{–}29\%$.
  2. **Emergency Fund / Liquidity Buffer:** How many days/weeks of core living expenses does this purchase consume?
  3. **Compounded Capital Benchmark:** $\text{FV} = \text{TCO} \times (1 + r_{\text{market}})^{10}$ (e.g., at a 7% real return, every \$1,000 spent today is ~\$1,967 of real purchasing power in 10 years, and every \$100/month recurring subscription is ~\$17,300 over 10 years).
  4. **Direct Peer Trade-off:** What other specific item or experience of equal price on the user's wishlist is displaced by buying this?

#### B. Financing Risk, Deferred Interest & Buy Now, Pay Later (BNPL)
- **Primary Sources:**
  - Consumer Financial Protection Bureau (CFPB) (September 2022), *Buy Now, Pay Later: Market trends and consumer impacts* ([CFPB Report](https://www.consumerfinance.gov/data-research/research-reports/buy-now-pay-later-market-trends-and-consumer-impacts/)).
  - CFPB (March 2023), *Consumer Use of Buy Now, Pay Later: Insights from the CFPB Making Ends Meet Survey* ([CFPB Report](https://www.consumerfinance.gov/data-research/research-reports/consumer-use-of-buy-now-pay-later-insights-from-the-cfpb-making-ends-meet-survey/)).
  - CFPB (January 2025), *Consumer Use of Buy Now, Pay Later and Other Unsecured Debt* ([CFPB Report](https://www.consumerfinance.gov/data-research/research-reports/consumer-use-of-buy-now-pay-later-and-other-unsecured-debt/)).
- **Core Empirical Findings:** CFPB data across hundreds of millions of BNPL loans shows that split-pay framing ("4 interest-free payments of \$50") induces **loan stacking** (simultaneous loans across multiple lenders), **overextension**, and higher incidence of overdraft/revolving credit distress. Furthermore, retail **"0% Promotional Financing" (Deferred Interest)** differs fatally from true **0% APR**: if $1.00$ of principal remains unpaid on the promotional expiration date, retroactive interest (often $26.99\text{–}29.99\%$) is charged back to day one on the entire original balance.
- **Liquidity Guardrail Rule:** Any non-essential consumer purchase that requires carrying high-interest debt, stacking BNPL installments to make cash flow work, or dipping into a primary emergency fund triggers an automatic **`Do Not Buy`** (or **`Delay Until Cash-Funded`**) verdict.

### 2.4 Commercial, B2B & Productive Asset Evaluation

When the item is a **productive asset** (a software developer's workstation, contractor tools, B2B SaaS, commercial machinery, or rental property), consumer utility metrics are supplemented by capital-budgeting metrics:

1. **Net Present Value (NPV):**
   $$\text{NPV} = -C_0 + \sum_{t=1}^{T} \frac{\Delta \text{CF}_t}{(1 + k)^t}$$
   where $\Delta \text{CF}_t = (\Delta \text{Revenue}_t + \Delta \text{Cost Savings}_t - \Delta \text{Operating Costs}_t)$ and $k$ is the hurdle rate / cost of capital.
2. **Payback Period:** The time $t^*$ required for cumulative net cash inflows or quantified time savings to recover $C_0$.
3. **Build vs. Buy (for Software / Engineering Teams):** Compare vendor TCO + integration cost + vendor lock-in risk + security/compliance review overhead against internal engineering build cost ($\text{Hours}_{\text{build}} \times \text{Fully Loaded Eng Rate}$) + **ongoing maintenance tax** (typically $15\text{–}25\%$ of initial build effort per year for dependency updates, bug fixes, and on-call support).

---

## 3. Behavioral Economics & Cognitive Debiasing for Buyers

A world-class buying advisor acts as a **cognitive circuit breaker** against six empirically documented behavioral biases that marketers systematically exploit.

### 3.1 Mental Accounting, Transaction Utility & Sunk Costs

- **Primary Sources:**
  - Richard H. Thaler (1985), *"Mental Accounting and Consumer Choice"*, *Marketing Science*, Vol. 4, No. 3, pp. 199–214 ([DOI: 10.1287/mksc.4.3.199](https://doi.org/10.1287/mksc.4.3.199); 2008 reprint [DOI: 10.1287/mksc.1070.0330](https://doi.org/10.1287/mksc.1070.0330)).
  - Richard H. Thaler (1999), *"Mental Accounting Matters"*, *Journal of Behavioral Decision Making*, Vol. 12, No. 3, pp. 183–206 ([DOI: 10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F](https://doi.org/10.1002/(SICI)1099-0771(199909)12:3%3C183::AID-BDM318%3E3.0.CO;2-F)).
  - Hal R. Arkes & Catherine Blumer (1985), *"The psychology of sunk cost"*, *Organizational Behavior and Human Decision Processes*, Vol. 35, No. 1, pp. 124–140 ([DOI: 10.1016/0749-5978(85)90049-4](https://doi.org/10.1016/0749-5978(85)90049-4)).

| Behavioral Mechanism | Primary Theory | How It Traps Buyers | Agent Debiasing Intervention |
| :--- | :--- | :--- | :--- |
| **Transaction Utility vs. Acquisition Utility** | Thaler (1985) defines total utility as $w(z, p, p^*) = v(\bar{p}, -p) + \tilde{v}(-p : -p^*)$, where **Acquisition Utility** $v(\bar{p}, -p)$ is the value of the good $\bar{p}$ relative to price paid $p$, and **Transaction Utility** $\tilde{v}(-p : -p^*)$ is the psychological pleasure of paying $p$ below reference price $p^*$. | Fake MSRP anchors ("Was \$499, Now \$199!"), Prime Day / Black Friday timers, and bundle discounts generate huge positive *transaction utility* ($\tilde{v} \gg 0$) for items with negative *acquisition utility* ($v < 0$). | **The Full-Price / Zero-Anchor Test:** Strip the reference price $p^*$ completely. Ask: *"If this item's permanent everyday price were $p$ (with no sale badge), and you had to compare $p$ against historical street prices (CamelCamelCamel / Keepa / price history), would its standalone functional utility still beat keeping $p$ in cash?"* |
| **Relative Thinking / Pennies-a-Day Framing** | Thaler (1999) / Gourville (1998) | Marketers frame a \$1,095/year recurring expense as "just \$3/day (less than a coffee!)" or hide a \$1,500 trim upgrade inside a \$45,000 auto loan where it feels like a rounding error. | **Horizon Aggregation & Unbundling:** Convert all daily/weekly/monthly prices into **1-year, 3-year, and 5-year cumulative cash outflows**, and evaluate every add-on/trim jump as an independent cash purchase (e.g., *"Would you walk into a store today and hand over \$1,500 cash solely for those upgraded wheels?"*). |
| **Sunk Cost Fallacy** | Arkes & Blumer (1985) | Buyers pour money into an unreliable car, a proprietary smart-home ecosystem, or an enterprise software migration because *"we already spent \$3,000 on it."* | **Zero-Base Forward Evaluation:** Treat all prior expenditures as irrecoverable ($C_{\text{sunk}} = 0$). Compare only **future incremental TCO** of continuing/upgrading the current path vs. **future incremental TCO** (including switching cost) of the alternative. |

### 3.2 Hedonic Adaptation, Hyperbolic Discounting & The Diderot Effect

- **Primary Sources:**
  - Elizabeth W. Dunn, Daniel T. Gilbert, & Timothy D. Wilson (2011), *"If money doesn't make you happy, then you probably aren't spending it right"*, *Journal of Consumer Psychology*, Vol. 21, No. 2, pp. 115–125 ([DOI: 10.1016/j.jcps.2011.02.002](https://doi.org/10.1016/j.jcps.2011.02.002)).
  - David Laibson (1997), *"Golden Eggs and Hyperbolic Discounting"*, *The Quarterly Journal of Economics*, Vol. 112, No. 2, pp. 443–478 ([DOI: 10.1162/003355397555253](https://doi.org/10.1162/003355397555253)).
  - Denis Diderot (1769), *"Regrets on Parting with My Old Dressing Gown"* (*Regrets sur ma vieille robe de chambre*), & Grant McCracken (1988), *Culture and Consumption: New Approaches to the Symbolic Character of Consumer Goods and Activities*, Indiana University Press ([ISBN: 978-0253206282](https://iupress.org/9780253206282/culture-and-consumption/)).

1. **Affective Forecasting Errors & Hedonic Adaptation (Dunn, Gilbert, & Wilson, 2011):**
   - Consumers suffer from **focalism** and **impact bias**: during shopping research, their attention is 100% focused on the marginal difference between Option A and Option B (e.g., a 65-inch vs. 77-inch OLED screen, or titanium vs. aluminum casing). Once purchased, daily attention shifts elsewhere and rapid **hedonic adaptation** flattens the novelty spike within weeks, while ongoing payments or maintenance persist.
2. **Hyperbolic Discounting / Present Bias (Laibson, 1997):**
   - Quasi-hyperbolic discounting ($U_t = u_t + \beta \sum_{\tau=1}^{T-t} \delta^\tau u_{t+\tau}$ with $\beta < 1$) causes immediate acquisition excitement ($u_t$) to disproportionately outweigh future subscription renewals, cleaning chores, storage clutter, and credit bills.
3. **The Diderot Effect (Diderot, 1769; McCracken, 1988):**
   - Anthropologist Grant McCracken coined the **Diderot Effect** after Denis Diderot's 1769 essay, in which acquiring a single scarlet silk dressing gown made his existing desk, chairs, tapestries, and bookshelves look shabby by comparison, triggering a cascade of replacements that drove him into debt.
   - **Diderot Spiral Audit:** Before approving a purchase, the advisor must explicitly list the **secondary complementary purchases** it will trigger:
     - *Espresso machine* $\rightarrow$ burr grinder (\$200–\$500), scale, tamper, filtered water system, specialty beans.
     - *Full-frame camera body* $\rightarrow$ native lenses, faster SD/CFexpress cards, tripod, camera bag, NAS storage, Lightroom subscription.
     - *New monitor/GPU* $\rightarrow$ dock/cables, monitor arm, PSU upgrade, desk upgrade.
     - *Larger home/car* $\rightarrow$ higher property taxes, insurance, heating/cooling, furniture, maintenance.

### 3.3 Prospective Hindsight (Pre-Mortem) & Regret Theory

- **Primary Sources:**
  - Gary Klein (2007), *"Performing a Project Premortem"*, *Harvard Business Review*, Vol. 85, No. 9, pp. 18–19 ([HBR Link](https://hbr.org/2007/09/performing-a-project-premortem); [DOI: 10.1109/EMR.2008.4534313](https://doi.org/10.1109/EMR.2008.4534313)).
  - David E. Bell (1982), *"Regret in Decision Making under Uncertainty"*, *Operations Research*, Vol. 30, No. 5, pp. 961–981 ([DOI: 10.1287/opre.30.5.961](https://doi.org/10.1287/opre.30.5.961)).
  - Graham Loomes & Robert Sugden (1982), *"Regret Theory: An Alternative Theory of Rational Choice Under Uncertainty"*, *The Economic Journal*, Vol. 92, No. 368, pp. 805–824 ([DOI: 10.2307/2232669](https://doi.org/10.2307/2232669)).

- **The Purchase Premortem (Prospective Hindsight):**
  Building on Mitchell, Russo, & Pennington (1989), Gary Klein showed that assuming an outcome has *already failed* increases the identification of concrete failure reasons by **30%** compared to asking *"What could go wrong?"*. Applied to buying decisions, the agent asks:
  > *"Fast-forward 12 months: you bought this item, and you now consider it one of your worst purchases of the year—it sits unused, annoyed you, or you sold it at a loss. Based on real owner failure reports and your workflow, what are the top 3 specific reasons that happened?"*
- **Regret Minimization Across Action vs. Inaction (Bell, 1982; Loomes & Sugden, 1982):**
  Compare **Action Regret** (buying the item and discovering it goes unused, breaks, or strains cash flow) against **Inaction Regret** (waiting or skipping the purchase and missing out on daily utility or a genuine supply window), weighted by **reversibility** (return window, restocking fees, and liquidity/depreciation loss upon resale).

---

## 4. Product Verification, Information Economics & Market Research

### 4.1 Search, Experience, and Credence Attributes (Nelson, 1970; Darby & Karni, 1973)

In information economics, products and their claims are divided into three fundamental classes depending on *when and how* a buyer can verify quality:

- **Primary Sources:**
  - Phillip Nelson (1970), *"Information and Consumer Behavior"*, *Journal of Political Economy*, Vol. 78, No. 2, pp. 311–329 ([DOI: 10.1086/259630](https://doi.org/10.1086/259630)).
  - Michael R. Darby & Edi Karni (1973), *"Free Competition and the Optimal Amount of Fraud"*, *The Journal of Law and Economics*, Vol. 16, No. 1, pp. 67–88 ([DOI: 10.1086/466756](https://doi.org/10.1086/466756)).

An AI buying skill must route its research queries according to the attribute class of the product:

| Attribute Class | Economic Definition | Examples | Mandatory Agent Verification Strategy |
| :--- | :--- | :--- | :--- |
| **1. Search Attributes** (Nelson, 1970) | Properties verifiable **prior to purchase** by direct inspection of specifications or contracts. | Dimensions, weight, port standards (Thunderbolt 4 vs. USB-C 3.2), sensor size, warranty term length, APR, SaaS pricing tier limits, return policy window. | Verify directly against **Tier 1 manufacturer spec sheets, FCC/regulatory filings, user manuals, and explicit contract terms**. Flag spec-sheet omissions (e.g., undisclosed PWM dimming rate, Bluetooth codecs, or fine-print warranty exclusions). |
| **2. Experience Attributes** (Nelson, 1970) | Properties that can only be ascertained **after purchase and prolonged use**. | Build durability after 18 months, cushion sag, thermal throttling under sustained load, software stability, customer support responsiveness, real-world battery degradation, noise/ergonomics. | Manufacturer claims have **zero evidentiary weight** here. Require **independent instrumental lab testing** (e.g., RTINGS, Consumer Reports, Wirecutter, GamersNexus, Notebookcheck, IIHS, Project Farm) plus **long-term owner reports (6–24+ months)** in enthusiast forums, repair communities (iFixit), and reliability surveys. |
| **3. Credence Attributes** (Darby & Karni, 1973) | Properties that the consumer **cannot evaluate even after consumption** without specialized scientific/regulatory testing, creating high incentives for fraud. | Supplements/nootropics, skincare active efficacy, air/water filter micron removal (HEPA/NSF standards), medical/ergonomic health claims, cybersecurity/encryption guarantees, ethical/environmental certifications. | Reject all user testimonials and influencer anecdotes (which reflect placebo effects or sponsorship). Require **peer-reviewed randomized controlled trials (RCTs), Cochrane/systematic reviews, regulatory certifications (FDA, NIOSH, NSF/ANSI, UL, SOC 2 Type II), or independent third-party lab assays (USP, ConsumerLab, Labdoor)**. |

### 4.2 Review Auditing, Regulatory Standards & Failure-Mode Analysis

- **Primary Sources:**
  - U.S. Federal Trade Commission (FTC), **16 CFR Part 255**, *Guides Concerning the Use of Endorsements and Testimonials in Advertising* (revised July 2023) ([eCFR 16 CFR Part 255](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255)).
  - U.S. Federal Trade Commission (FTC), **16 CFR Part 465**, *Trade Regulation Rule on the Use of Consumer Reviews and Testimonials* (effective October 21, 2024) ([eCFR 16 CFR Part 465](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465); [FTC Announcement](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials)).

As documented in the FTC's rulemaking record for **16 CFR Part 465**, retail aggregate star ratings (e.g., "4.7 stars across 12,000 reviews") are routinely distorted by **incentivized Day-1 reviews**, **review hijacking / SKU merging** (attaching old reviews for a USB cable to a newly listed projector), **suppressing negative reviews**, and **affiliate commission bias** (where "Best X of 2026" listicles rank products by Amazon Associates / SaaS affiliate payout rather than testing).

To defeat review manipulation, an AI purchase advisor must enforce a **4-Point Failure-Mode Audit**:

1. **Star-Rating Ignore & 1–3 Star Failure Clustering:** Ignore the overall average star score. Search specifically for **1-star to 3-star reviews and post-warranty threads** (`"<product>" problem OR failure OR broken OR "after a year" OR warranty OR RMA`) to see whether complaints are random shipping defects or a **systematic engineering failure mode** (e.g., hinge cracking, capacitor failure, stick drift, cloud server bricking).
2. **SKU Hijacking & Revision Check:** Verify that reviews correspond to the exact current hardware revision or formulation (checking for silent **"cost-down" component swaps**, such as replacing TLC NAND with QLC NAND in SSDs or changing appliance pump housings from brass to plastic).
3. **Repairability & Right-to-Repair Inspection:** Check iFixit teardown scores, availability of OEM spare parts, whether batteries/wear components are glued or serialized/paired, and whether the product functions offline if the vendor's cloud servers shut down.
4. **Warranty Fine-Print & Return Friction:** Check who pays return shipping, restocking fees, whether warranty coverage requires authorized dealer purchase, and what exclusions void coverage.

---

## 5. Interactive Context Elicitation, Verdict Taxonomy & Optional Persistent Memory

### 5.1 Conversational Preference Elicitation & Information Gain (Pu & Chen, 2008, 2012)

When a user asks *"Should I buy an iPad Pro?"* or *"Which standing desk should I get?"*, rendering an immediate one-shot verdict without knowing their existing devices, budget/liquidity, or actual use case produces generic, low-value advice. Conversely, interrogating the user with a 15-question survey before answering creates unbearable friction.

- **Primary Sources:**
  - Pearl Pu & Li Chen (2008), *"User-Involved Preference Elicitation for Product Search and Recommender Systems"*, *AI Magazine*, Vol. 29, No. 4, pp. 93–103 ([DOI: 10.1609/aimag.v29i4.2200](https://doi.org/10.1609/aimag.v29i4.2200)).
  - Li Chen & Pearl Pu (2012), *"Critiquing-based recommenders: survey and emerging trends"*, *User Modeling and User-Adapted Interaction*, Vol. 22, No. 1–2, pp. 125–150 ([DOI: 10.1007/s11257-011-9111-y](https://doi.org/10.1007/s11257-011-9111-y)).

- **Core Findings & Principles for Agent Design:**
  1. **Decision Accuracy vs. Cognitive Effort Trade-off:** Pu & Chen demonstrate that preference elicitation increases decision accuracy and user confidence *only* when questions target **high-variance, verdict-flipping variables** and require minimal user effort (e.g., structured multiple-choice or 2–4 concise questions).
  2. **The 5 Verdict-Flipping Variables (Missing-Context Gate):** Before locking in a final recommendation, the advisor checks whether five core variables are already known (from the prompt, conversation history, or optional user profile):
     - **Objective / Job-to-be-Done:** What concrete problem or bottleneck is this solving?
     - **Current Baseline / Inventory:** What do you currently use for this, and why is it falling short?
     - **Utilization Frequency & Horizon:** How often will you realistically use it (daily, weekly, 3x/year) and for how long?
     - **Financial Guardrails:** Are you paying cash comfortably within budget, or financing/stretching? What is your ceiling?
     - **Hard Constraints (Knockouts):** Space, OS/ecosystem, portability, noise, or compatibility dealbreakers.
  3. **Proportionate Elicitation Rule:**
     - If critical variables are missing and could flip the verdict, ask **at most 2–4 high-leverage questions** upfront (using structured interactive questions such as `ask_question` when available, or a tight bulleted block), OR provide a **Preliminary Research Snapshot + Conditional Verdict** while asking the 2–3 questions needed to lock in the tailored verdict.
     - Scale elicitation depth to purchase stakes: a \$25 cable needs at most 1 quick compatibility check; a \$2,000 laptop or \$40,000 car warrants a full context lock before final recommendation.

### 5.2 Calibrated 6-Level Purchase Verdict Taxonomy & Reversal Conditions

Just as fact-checking requires a calibrated epistemic taxonomy rather than binary `True/False`, a purchase advisor requires an **actionable, non-hedging 6-level Verdict Taxonomy**:

| Verdict Label | Meaning & Decision Rule | Required Follow-Through in Report |
| :--- | :--- | :--- |
| **`Buy`** | Passes all knockout constraints; high fundamental utility; reasonable TCO/CPU; beats non-purchase baselines and peer competitors; respects liquidity guardrails. | Specify the exact recommended trim/configuration, target street price to pay, and pre-purchase inspection/return-window checklist. |
| **`Buy With Conditions / Wait`** | Strong product fit, *but* currently overpriced relative to price history, awaiting an imminent product refresh, or contingent on verifying one specific constraint (e.g., physical fit or trial). | State the **exact trigger condition** (e.g., *"Buy only if street price drops below \$X"*, *"Wait 6 weeks for next-gen release"*, or *"Buy only from a retailer with a 30-day free return policy to test ergonomics"*). |
| **`Buy Alternative Instead`** | The user's fundamental objective is valid and worth solving, but the specific item asked about is dominated on TCO, reliability, or performance by a competitor or a lower/refurbished tier. | Name the exact superior alternative(s), show the head-to-head TCO and Experience/Search attribute comparison, and explain why it dominates. |
| **`Rent / Borrow / Trial First`** | Projected utilization ($N_{\text{projected}}$) is below the break-even ownership threshold ($N^*$), or hedonic adaptation / workflow fit is highly uncertain. | Show the Break-Even Utilization math ($N^*$) and specify the lowest-friction way to rent, borrow, buy used-and-resell, or run a time-boxed trial. |
| **`Keep Current / Repair`** | The user's existing tool, workflow, or a cheap repair/upgrade (\$20 battery/part/setting change) delivers $\ge 85\%$ of the utility at a fraction of the TCO. | Detail the exact repair, configuration change, or maintenance step to extend the current item's life. |
| **`Do Not Buy`** | Fails knockout criteria, exhibits severe Experience/Credence failure modes, relies on fake Transaction Utility / Diderot spiral, or violates financial/liquidity guardrails. | State plainly why the purchase destroys value, quantify the 1-year and 5-year cash saved by walking away, and name the best alternative use of that capital. |

> **Mandatory Reversal Conditions ("What Would Flip This Verdict?"):** Every evaluation must end by stating the concrete, falsifiable conditions that would change the verdict (e.g., *"This `Do Not Buy` flips to `Buy` only if: (1) your usage exceeds 3 days/week, (2) you buy a certified refurbished unit under \$350 instead of \$699 MSRP, and (3) you have no high-APR debt"*).

### 5.3 Portable User Context & Optional Memory Architecture

Users frequently make recurring purchase evaluations across related domains (tech/home office gear, wardrobe, kitchen, subscriptions, B2B tools). Without persistent context, the user must repeat their currency, country/tax regime, existing hardware ecosystem, and financial rules in every session.

To work seamlessly across **Claude Desktop, Claude Code, OpenAI Codex, GitHub Copilot, Google Antigravity (AGY), Gemini CLI, and Cursor/Windsurf** while remaining **100% optional (zero-config by default)**:

1. **Zero-Config Default:** The skill must work out-of-the-box with zero setup files. If no profile file exists, the agent elicits only the context needed for the current item.
2. **Optional Local Buyer Profile (`buyer-profile.md`):**
   - Before asking questions, the agent checks (if file tools are available) for an optional user context file in standard locations: `.agents/buyer-profile.md` (workspace-level) or `~/.agents/buyer-profile.md` / `~/.claude/buyer-profile.md` (user-level).
   - **Recommended Schema for `buyer-profile.md`:**
     - **Locale & Baseline:** Currency, country/state (for tax, shipping, voltage, and consumer warranty law), and market availability.
     - **Financial Guardrails:** Default opportunity-cost benchmark (e.g., HYSA rate, index return, or debt payoff priority), cooling-off rules by price tier, and net hourly time valuation ($\$/\text{hr}$).
     - **Existing Ecosystem & Inventory:** Owned devices, OS ecosystem, tool battery platforms (e.g., Makita 18V vs. Milwaukee M18), smart-home standard (Matter/HomeKit/Home Assistant), and active subscriptions (to prevent duplicate SaaS/media functionality and Diderot mismatches).
     - **Decision Log & Past Post-Mortems:** Optional table of past purchase verdicts (`Bought`, `Skipped`, `Returned`) and 6-month satisfaction notes so the agent learns which purchases the user actually used vs. regretted.
3. **Opt-In Profile Updates:** After completing an evaluation, if a `buyer-profile.md` exists (or if the user asks to save their preferences/decision), the agent can append the decision entry or newly discovered constraints.

---

## 6. Skill Naming Analysis & Workflow Blueprint

### 6.1 Skill Naming Evaluation Against `writing-for-agents` Principles

Per `writing-for-agents` (`~/.gemini/config/skills/writing-for-agents/SKILL.md`) and `SKILL-MECHANICS.md` (`~/.gemini/config/skills/writing-for-agents/SKILL-MECHANICS.md`):
- A skill name serves as both a **human slash command** (`/skill-name`) and a **model-invoked leading word** in the context pointer.
- The best skill name is short, hyphenated, verb- or question-driven, matches the exact natural-language tokens users type when deliberating a purchase, works across any purchase scale (\$10 to \$500,000), and pairs cleanly with `fact-check` in `ej-skills`.

| Candidate Name | Slash-Command Ergonomics | Pretraining Leading-Word Alignment | Scale Universality (\$10 to \$500k, B2C & B2B) | Evaluation & Trade-offs |
| :--- | :--- | :--- | :--- | :--- |
| **`should-i-buy`** | `/should-i-buy [item]` | **Highest.** Matches the exact verbatim phrase users type into chat and search engines (*"Should I buy X?"*). Immediately primes adversarial evaluation rather than blind shopping fulfillment. | **High.** Natural for gadgets, subscriptions, cars, real estate, and tools alike. | Slightly longer (12 chars, 2 hyphens), but zero ambiguity for both humans and models. |
| **`buy-or-not`** | `/buy-or-not [item]` | **Very High.** Encodes the binary/multi-way decision fork directly in the name; eliminates sycophantic pro-buying bias by giving `"not"` equal weight in the token itself. | **High.** Works well for single-item verdicts and head-to-head comparisons. | Punchy (10 chars), symmetrical with `fact-check` in tone; slightly less conversational than `should-i-buy`. |
| **`worth-it`** | `/worth-it [item]` | **High.** Directly recruits TCO, ROI, and value-for-money priors (*"Is X worth it?"*). | **Very High.** Equally natural for subscriptions, upgrades, repairs, B2B SaaS, and physical goods. | Short (8 chars, 1 hyphen); however, *"Is X worth it?"* is also asked about non-purchases (movies to watch, books to read, careers). |
| **`buy-check`** | `/buy-check [item]` | **Medium-High.** Mirrors `fact-check` in the `ej-skills` suite (`fact-check` + `buy-check`). Connotes a rigorous audit/checklist before spending. | **High.** Clean, audit-oriented framing across consumer and commercial purchases. | Coined compound rather than a pre-existing natural phrase, so the `description` pointer does more triggering work than `should-i-buy`. |
| **`purchase-advisor`** | `/purchase-advisor` | **Medium (Role-noun).** Sounds like an agent persona/role rather than an action or decision gate. | **High.** Covers all categories, including procurement. | Longer (16 chars); role-noun names (`-advisor`, `-assistant`) are weaker leading words than action/decision hooks and tend to prime polite sales-assistant prose. |
| **`verdict`** | `/verdict [item]` | **Medium (Too broad).** Strong leading word for the *final step* of a decision, but not specific to buying. | **Low specificity.** Collides with legal verdicts, code review verdicts, and `fact-check` verdicts. | Better used as an **in-file leading word** inside the skill body rather than the top-level skill name. |

#### Naming Recommendation
- **Top Recommendation for Universal Natural-Language & Slash Ergonomics:** **`should-i-buy`** (or **`buy-or-not`** / **`buy-check`** if a 2-word slug mirroring `fact-check` is preferred).
- Regardless of which slug is chosen as `name`, the `description` frontmatter pointer should front-load all distinct trigger branches:
  1. Single-item purchase evaluation (*"should I buy X"*, *"is X worth it"*, *"talk me into or out of buying X"*)
  2. Multi-option product comparison (*"which X should I get"*, *"X vs Y"*)
  3. Upgrade, repair, subscription, or rent-vs-buy trade-off (*"upgrade from X to Y"*, *"keep or replace"*, *"buy vs rent/lease"*)

### 6.2 Blueprint: 6-Step Buying-Decision Protocol

Synthesizing all five research pillars, the skill should enforce a sequential **6-Step Evaluation Protocol** where every step has a checkable completion criterion:

1. **Frame & Context Gate (Keeney Value-Focused Thinking + Pu & Chen Elicitation):**
   - Separate the **fundamental objective** (the job to be done) from the **means objective** (the specific product).
   - Check optional `buyer-profile.md` (if present) and the user's prompt against the **5 Verdict-Flipping Variables** (Objective, Current Baseline, Utilization Frequency/Horizon, Financial Guardrails, Hard Knockout Constraints).
   - *Completion Criterion:* Either all 5 verdict-flipping variables are bounded, or 2–4 high-leverage questions have been asked to resolve the missing variables before rendering a final verdict.
2. **Baseline & Knockout Pruning (PrOACT + Tversky EBA):**
   - Explicitly include the relevant **Non-Purchase Baselines** (`Do Nothing / Keep Current`, `Repair / Optimize`, `Wait / Delay`, `Rent / Borrow / Trial`, `Used / Refurbished / Previous-Gen`).
   - Apply **Elimination by Aspects (EBA)** to immediately disqualify any option that violates a hard constraint.
   - *Completion Criterion:* Surviving candidates and non-purchase baselines are explicitly listed, and every disqualified option cites the exact knockout constraint it failed.
3. **Attribute-Routed Verification & Failure-Mode Audit (Nelson + Darby & Karni + FTC 16 CFR 465):**
   - Classify key claims into **Search** (verify via Tier 1 specs/manuals/terms), **Experience** (verify via independent lab tests + 6–24 month owner failure reports), and **Credence** (verify via peer-reviewed RCTs or regulatory certifications).
   - Execute adversarial failure-mode queries (`"<item>" problem OR failure OR "after a year" OR warranty OR teardown`) to uncover systematic defects, silent component downgrades, repairability blocks, or subscription lock-in.
   - *Completion Criterion:* Every critical Search, Experience, and Credence attribute has been checked against primary/independent sources, and the top real-world failure modes and warranty/return terms are documented with links.
4. **Full-Lifecycle TCO, Unit Utilization & Opportunity Cost Math (NIST HB 135 + Whillans + Frederick):**
   - Compute **$\text{TCO}(T)$** over holding period $T$: Acquisition (price + tax + shipping + required accessories) + Financing/APR + Operating/Energy/Consumables/Subscriptions + Maintenance/Repairs + Exit/Selling fees $-$ Realistic Resale Value ($V_{\text{salvage}}$).
   - Compute **Cost-Per-Use ($\text{CPU}$)** / **Cost-Per-Hour ($\text{CPH}$)** (stress-tested at 50% of optimistic usage), **Break-Even Utilization ($N^*$)** against renting/pay-per-use, and **Implied Cost per Hour Saved** (for time-saving purchases).
   - State the explicit **Opportunity Cost** (debt payoff, emergency fund impact, compounded capital value, or displaced wishlist items).
   - *Completion Criterion:* A complete $\text{TCO}(T)$ breakdown, utilization unit economics ($\text{CPU}$/$\text{CPH}$/$N^*$), and explicit opportunity-cost comparison are calculated using verified numbers.
5. **Cognitive Debiasing & Pre-Mortem Stress Test (Thaler + McCracken + Klein + Regret Theory):**
   - Run the **Zero-Anchor / Full-Price Test** (stripping fake MSRP discounts / Transaction Utility), **Sunk Cost Reset**, **Diderot Spiral Audit** (listing secondary complementary purchases triggered), and a **12-Month Purchase Premortem** (*"If you regret this in a year, why did it happen?"*).
   - *Completion Criterion:* Cognitive traps, Diderot add-on costs, and top pre-mortem regret scenarios are explicitly evaluated.
6. **Calibrated Verdict & Reversal Conditions:**
   - Assign one of the 6 calibrated verdicts: **`Buy`**, **`Buy With Conditions / Wait`**, **`Buy Alternative Instead`**, **`Rent / Borrow / Trial First`**, **`Keep Current / Repair`**, or **`Do Not Buy`**.
   - State explicit, falsifiable **Reversal Conditions** (*"What would flip this verdict?"*) and, if verdict is `Buy`, provide the target price ceiling and return-window inspection checklist.
   - *Completion Criterion:* The report delivers a single unambiguous verdict label, a comparison matrix against the best alternative and non-purchase baseline, exact citations, and explicit reversal conditions.

---

## References & Primary Sources

1. **Keeney, R. L. (1992):** *Value-Focused Thinking: A Path to Creative Decisionmaking*, Harvard University Press. [https://www.hup.harvard.edu/books/9780674931978](https://www.hup.harvard.edu/books/9780674931978)
2. **Hammond, J. S., Keeney, R. L., & Raiffa, H. (1999):** *Smart Choices: A Practical Guide to Making Better Decisions*, Harvard Business Review Press. [https://store.hbr.org/product/smart-choices-a-practical-guide-to-making-better-decisions/8575](https://store.hbr.org/product/smart-choices-a-practical-guide-to-making-better-decisions/8575)
3. **Tversky, A. (1972):** *"Elimination by aspects: A theory of choice"*, *Psychological Review*, 79(4), 281–299. [https://doi.org/10.1037/h0032955](https://doi.org/10.1037/h0032955)
4. **Keeney, R. L., & Raiffa, H. (1976):** *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*, Wiley / Cambridge University Press. [https://doi.org/10.1017/CBO9781139174084](https://doi.org/10.1017/CBO9781139174084)
5. **Edwards, W. (1977):** *"How to Use Multiattribute Utility Measurement for Social Decisionmaking"*, *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-7(5), 326–340. [https://doi.org/10.1109/TSMC.1977.4309720](https://doi.org/10.1109/TSMC.1977.4309720)
6. **Kneifel, J. D., & Webb, D. (2025):** *Life-Cycle Costing Manual for the Federal Energy Management Program*, **NIST Handbook 135** (2025 Edition), National Institute of Standards and Technology. [https://doi.org/10.6028/NIST.HB.135e2025](https://doi.org/10.6028/NIST.HB.135e2025)
7. **International Organization for Standardization (ISO):** *ISO 15686-5: Buildings and constructed assets — Service-life planning — Part 5: Life-cycle costing*. [https://www.iso.org/obp/ui/#iso:std:iso:15686:-5:ed-2:v1:en](https://www.iso.org/obp/ui/#iso:std:iso:15686:-5:ed-2:v1:en)
8. **Kirwin, B. / Gartner (1987):** *Total Cost of Ownership (TCO)*. [https://www.gartner.com/en/information-technology/glossary/total-cost-of-ownership-tco](https://www.gartner.com/en/information-technology/glossary/total-cost-of-ownership-tco)
9. **Whillans, A. V., Dunn, E. W., Smeets, P., Bekkers, R., & Norton, M. I. (2017):** *"Buying time promotes happiness"*, *Proceedings of the National Academy of Sciences (PNAS)*, 114(32), 8523–8527. [https://doi.org/10.1073/pnas.1706541114](https://doi.org/10.1073/pnas.1706541114)
10. **Frederick, S., Novemsky, N., Wang, J., Dhar, R., & Nowlis, S. (2009):** *"Opportunity Cost Neglect"*, *Journal of Consumer Research*, 36(4), 553–561. [https://doi.org/10.1086/599764](https://doi.org/10.1086/599764)
11. **Spiller, S. A. (2011):** *"Opportunity Cost Consideration"*, *Journal of Consumer Research*, 38(4), 595–610. [https://doi.org/10.1086/660045](https://doi.org/10.1086/660045)
12. **Consumer Financial Protection Bureau (CFPB) (2022, 2023, 2025):** *Buy Now, Pay Later: Market trends and consumer impacts* ([https://www.consumerfinance.gov/data-research/research-reports/buy-now-pay-later-market-trends-and-consumer-impacts/](https://www.consumerfinance.gov/data-research/research-reports/buy-now-pay-later-market-trends-and-consumer-impacts/)) & *Consumer Use of Buy Now, Pay Later and Other Unsecured Debt* ([https://www.consumerfinance.gov/data-research/research-reports/consumer-use-of-buy-now-pay-later-and-other-unsecured-debt/](https://www.consumerfinance.gov/data-research/research-reports/consumer-use-of-buy-now-pay-later-and-other-unsecured-debt/)).
13. **Thaler, R. H. (1985):** *"Mental Accounting and Consumer Choice"*, *Marketing Science*, 4(3), 199–214. [https://doi.org/10.1287/mksc.4.3.199](https://doi.org/10.1287/mksc.4.3.199)
14. **Thaler, R. H. (1999):** *"Mental Accounting Matters"*, *Journal of Behavioral Decision Making*, 12(3), 183–206. [https://doi.org/10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F](https://doi.org/10.1002/(SICI)1099-0771(199909)12:3%3C183::AID-BDM318%3E3.0.CO;2-F)
15. **Arkes, H. R., & Blumer, C. (1985):** *"The psychology of sunk cost"*, *Organizational Behavior and Human Decision Processes*, 35(1), 124–140. [https://doi.org/10.1016/0749-5978(85)90049-4](https://doi.org/10.1016/0749-5978(85)90049-4)
16. **Dunn, E. W., Gilbert, D. T., & Wilson, T. D. (2011):** *"If money doesn't make you happy, then you probably aren't spending it right"*, *Journal of Consumer Psychology*, 21(2), 115–125. [https://doi.org/10.1016/j.jcps.2011.02.002](https://doi.org/10.1016/j.jcps.2011.02.002)
17. **Laibson, D. (1997):** *"Golden Eggs and Hyperbolic Discounting"*, *The Quarterly Journal of Economics*, 112(2), 443–478. [https://doi.org/10.1162/003355397555253](https://doi.org/10.1162/003355397555253)
18. **McCracken, G. (1988):** *Culture and Consumption: New Approaches to the Symbolic Character of Consumer Goods and Activities*, Indiana University Press (coining the **Diderot Effect** from Denis Diderot, 1769, *"Regrets on Parting with My Old Dressing Gown"*). [https://iupress.org/9780253206282/culture-and-consumption/](https://iupress.org/9780253206282/culture-and-consumption/)
19. **Klein, G. (2007):** *"Performing a Project Premortem"*, *Harvard Business Review*, 85(9), 18–19. [https://hbr.org/2007/09/performing-a-project-premortem](https://hbr.org/2007/09/performing-a-project-premortem) | [https://doi.org/10.1109/EMR.2008.4534313](https://doi.org/10.1109/EMR.2008.4534313)
20. **Bell, D. E. (1982):** *"Regret in Decision Making under Uncertainty"*, *Operations Research*, 30(5), 961–981. [https://doi.org/10.1287/opre.30.5.961](https://doi.org/10.1287/opre.30.5.961)
21. **Loomes, G., & Sugden, R. (1982):** *"Regret Theory: An Alternative Theory of Rational Choice Under Uncertainty"*, *The Economic Journal*, 92(368), 805–824. [https://doi.org/10.2307/2232669](https://doi.org/10.2307/2232669)
22. **Nelson, P. (1970):** *"Information and Consumer Behavior"*, *Journal of Political Economy*, 78(2), 311–329. [https://doi.org/10.1086/259630](https://doi.org/10.1086/259630)
23. **Darby, M. R., & Karni, E. (1973):** *"Free Competition and the Optimal Amount of Fraud"*, *The Journal of Law and Economics*, 16(1), 67–88. [https://doi.org/10.1086/466756](https://doi.org/10.1086/466756)
24. **U.S. Federal Trade Commission (FTC):** *Guides Concerning the Use of Endorsements and Testimonials in Advertising* (**16 CFR Part 255**, [https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255)) & *Trade Regulation Rule on the Use of Consumer Reviews and Testimonials* (**16 CFR Part 465**, [https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465)).
25. **Pu, P., & Chen, L. (2008):** *"User-Involved Preference Elicitation for Product Search and Recommender Systems"*, *AI Magazine*, 29(4), 93–103. [https://doi.org/10.1609/aimag.v29i4.2200](https://doi.org/10.1609/aimag.v29i4.2200)
26. **Chen, L., & Pu, P. (2012):** *"Critiquing-based recommenders: survey and emerging trends"*, *User Modeling and User-Adapted Interaction*, 22(1–2), 125–150. [https://doi.org/10.1007/s11257-011-9111-y](https://doi.org/10.1007/s11257-011-9111-y)
