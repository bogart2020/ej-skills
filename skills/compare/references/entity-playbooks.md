# Entity Comparison Playbooks

Domain-specific MECE category templates, normalization formulas, and indifference thresholds ($q_j \implies \texttt{Tie}$) for the six entity domains referenced in [`SKILL.md`](../SKILL.md).

## Products, hardware, appliances, and services

1. **Recommended MECE Categories & Default Weights**:
   - **Core Functional Performance & Sustained Output (30%)**: independent lab measurements under realistic sustained load (rather than burst marketing specs).
   - **Total Cost of Ownership (TCO) & Resale Value (25%)**: full lifecycle cost over holding horizon $T$ ($C_{\text{acquisition}} + C_{\text{operating}}(T) + C_{\text{maintenance}}(T) + C_{\text{exit}} - V_{\text{salvage}}(T)$).
   - **Reliability, Build Quality & Repairability (20%)**: 6-to-24 month owner failure rates, 1-to-3 star failure clusters, teardown/iFixit repairability, and parts availability.
   - **Ergonomics, Daily Experience & Noise/Footprint (15%)**: physical comfort, UI/workflow friction, acoustic output (dBA), and portability/space fit.
   - **Ecosystem Compatibility, Warranty & Offline Autonomy (10%)**: open standards vs. proprietary consumables/cloud lock-in, return policy, and warranty support.
2. **Normalization & Tie Thresholds ($q_j$)**:
   - Declare a **`Tie`** on **TCO** when net lifecycle cost over $T$ differs by less than **3% to 5%**.
   - Declare a **`Tie`** on **Performance or Battery/Efficiency** when independent test differences fall below **5%** (or below the human Just Noticeable Difference in separate daily use).
   - Check for **silent revision downgrades** and **Diderot add-on spirals** (mandatory docks, proprietary filters, subscriptions) and fold them directly into the TCO category.

## Places: cities, neighborhoods, countries, and venues

1. **Recommended MECE Categories & Default Weights** (synthesizing EIU Global Liveability, OECD Better Life Index, and Mercer Quality of Living):
   - **Real Purchasing Power & Tax/Housing Surplus (25%)**: Purchasing Power Parity (PPP) or U.S. BEA Regional Price Parity (RPP) and tax-adjusted real disposable surplus.
   - **Career Depth, Local Economy & Income Trajectory (20%)**: density of relevant employers, local compensation bands, and career resilience if switching jobs locally.
   - **Mobility, Walkability & Door-to-Door Time Tax (15%)**: Walk/Transit/Bike scores, rush-hour commute times, and airport connectivity at the specific neighborhood tier.
   - **Safety, Healthcare & Civic Stability (15%)**: tract/neighborhood-level violent and property crime rates, hospital quality/access, and infrastructure reliability.
   - **Climate Comfort & Environmental Quality (15%)**: number of comfortable outdoor days per year (highs $55^\circ\text{F}$ to $82^\circ\text{F}$ with low dew point), sunshine hours, air quality ($\text{PM}_{2.5}$ / AQI), and natural hazard risk.
   - **Culture, Education & Social Fit (10%)**: schools/universities, third places, culinary/arts density, and proximity to family/support networks.
2. **Mandatory Normalization Formulas & Tie Thresholds ($q_j$)**:
   - **Never compare nominal salaries or raw price indices in isolation.** Compute **Annual Real Discretionary Surplus ($S_{\text{real}}$)**:
     $$S_{\text{real}, i} = \frac{Y_{\text{gross}, i} - T_{\text{fed+state+local}, i} - C_{\text{equivalent housing}, i} - C_{\text{transport+childcare}, i}}{\text{RPP}_i / 100}$$
   - Anchor all metrics to the **specific neighborhood tier** the user would actually live in rather than city-wide averages (avoiding the ecological fallacy).
   - Declare a **`Tie`** on **Purchasing Power** when $S_{\text{real}}$ differs by less than **3%**, on **Commute/Mobility** when door-to-door transit differs by less than **4 minutes each way**, and on **Climate** when comfortable outdoor days per year differ by fewer than **10 days**.

## People: job candidates, leaders, and service providers

1. **Recommended MECE Categories & Default Weights** (grounded in Schmidt & Hunter, 1998; Sackett et al., 2022; and Smith & Kendall, 1963 Behaviorally Anchored Rating Scales):
   - **Demonstrated Role Execution & Work Sample Quality (35%)**: verified output on work samples, technical/domain assessments, or past deliverables under comparable constraints.
   - **Problem-Solving Depth & Decision Judgment (25%)**: ability to diagnose ambiguous trade-offs, architectural or strategic reasoning, and post-mortem learning from failures.
   - **Scope Ownership, Leadership & Collaboration (20%)**: cross-functional execution, mentoring, communication clarity, and reliability under pressure.
   - **Ramp Velocity, Trajectory & Contextual Fit (20%)**: speed of adaptation to the target stage/scale (for example, 0-to-1 startup vs. regulated enterprise) and compensation/start-date alignment.
2. **Mandatory BARS Normalization & Debiasing Rules**:
   - **Anchor every score to Behaviorally Anchored Rating Scales (BARS)**: map concrete behavioral evidence (shipped systems, measurable outcomes, code/portfolio artifacts) to explicit level anchors ($1\text{–}5$ or $1\text{–}10$) rather than scoring on pedigree Halo (*"worked at Famous Company"*) or raw years of tenure.
   - **Declare a `Tie`** on any competency where both candidates meet the same behavioral level anchor and differences rest on unverified self-reporting or resume polish.

## People: athletes, public/historical figures, and creators

1. **Recommended MECE Categories & Default Weights** (grounded in Stephen Jay Gould's *Full House*, 1996, and Jay Jaffe's JAWS methodology):
   - **Era-Adjusted Peak Dominance (30%)**: best 3-to-7 year prime ceiling measured against contemporary peer distribution.
   - **Career Longevity & Cumulative Value Over Replacement (25%)**: sustained elite production across full career span (WAR or domain equivalent above a replacement baseline).
   - **High-Leverage, Postseason, or Crisis Execution (20%)**: performance when stakes, defensive scheming, or historical opposition are highest, adjusted for supporting cast and resources.
   - **Versatility, Two-Way / Multi-Domain Impact & Scalability (15%)**: adaptability across systems, rules, or teammates without diminishing returns.
   - **Structural Influence, Accolades & Cultural/Historical Footprint (10%)**: MVPs/honors, championship equity, and lasting changes to how the field operates.
2. **Mandatory Cross-Era Normalization Formulas**:
   - **Era-Adjusted Z-Score ($Z_{\text{era}}$)**: never compare raw counting stats across eras with different pace, rule sets, or baselines. Compute relative dominance over contemporary peers:
     $$Z_{i, \text{era}} = \frac{X_i - \mu_{\text{era}}}{\sigma_{\text{era}}}$$
     Pair $Z_{\text{era}}$ with an explicit adjustment for **competitive talent-pool depth** (size, global integration, and professionalization of the pool in each era).
   - **JAWS Peak-vs-Longevity Balance**: evaluate Peak Ceiling and Career Cumulative Value in separate categories so neither a short-peak comet nor a long-career compiler wins by default without weighing both halves of $\text{JAWS} = \frac{1}{2}(\text{Career Value} + \text{Peak Value})$.

## Technologies, software, libraries, models, and architectures

1. **Recommended MECE Categories & Default Weights** (synthesizing ISO/IEC 25010:2023 SQuaRE and SEI ATAM, Kazman et al., 2000):
   - **Workload Performance & Resource Efficiency (25%)**: tail latency ($p_{95}/p_{99}$), throughput, token/compute cost, and memory/CPU footprint on representative workloads.
   - **Reliability, Consistency & Operational Resilience (20%)**: fault tolerance, recovery time objective (RTO/RPO), correctness guarantees, and production stability at scale.
   - **Developer Experience (DX), Maintainability & Velocity (20%)**: API ergonomics, type safety, debugging/observability tooling, testability, and onboarding speed.
   - **Ecosystem Maturity, Interoperability & Community (15%)**: library ecosystem, active maintenance cadence, documentation accuracy, and hiring pool depth.
   - **Security, Licensing, Total Cost & Exit Portability (20%)**: license openness, cloud/vendor lock-in, migration exit cost ($C_{\text{exit}}$), and day-2 operational staffing burden.
2. **Mandatory Benchmark Normalization & Tie Thresholds ($q_j$)**:
   - **Fleming & Wallace Geometric Mean Law (1986)**: when aggregating relative benchmark ratios ($y_{A,k} / y_{B,k}$) across $K$ workloads, **always compute the Geometric Mean**:
     $$\text{GeoMean}\left(\frac{A}{B}\right) = \left(\prod_{k=1}^{K} \frac{y_{A,k}}{y_{B,k}}\right)^{1/K}$$
     Arithmetic means of normalized benchmark ratios are mathematically invalid because swapping the reference baseline can reverse the winner on identical data.
   - **SEI ATAM Scenario Framing**: evaluate scalability and reliability against concrete **Stimulus $\rightarrow$ Environment $\rightarrow$ Response Measure** scenarios rather than generic claims.
   - **Declare a `Tie`** on **Performance** when workload-weighted $\text{GeoMean}$ differs by less than **5% to 10%** on synthetic benchmarks without producing a measurable production SLA or infrastructure-cost difference.

## Companies, careers/job offers, policies, and creative works

1. **Companies, Stocks & Business Models** (Kaplan & Norton Balanced Scorecard + Moat/Valuation):
   - **Financial & Unit Economics (30%)**: revenue growth, gross/operating margin, ROIC, free cash flow (FCF) conversion, LTV:CAC, and balance-sheet health.
   - **Competitive Moat & Customer Retention (25%)**: switching costs, net dollar retention (NRR), network effects, and market share durability.
   - **Execution Velocity & Leadership Allocation (20%)**: R&D efficiency, capital allocation track record, and supply-chain/operational resilience.
   - **Valuation Multiple & Asymmetric Downside Risk (25%)**: EV/FCF or P/E relative to growth rate, customer concentration, and regulatory/disruption tail risk.
2. **Careers, Job Offers & Educational Paths**:
   - **Risk- and RPP-Adjusted Real Compensation (30%)**: base + expected bonus + probability-weighted liquid value of equity + benefits, adjusted for taxes and local cost of living (RPP).
   - **Effective Hourly Rate & Sustainability (20%)**: real net compensation divided by realistic annual work + commute + on-call hours.
   - **Career Capital, Scope & Learning Velocity (30%)**: skill compounding, mentorship quality, ownership scope, and promotion/title trajectory.
   - **Team Stability, Runway & Exit Optionality (20%)**: manager quality, company financial runway, and downstream resume signaling value.
3. **Public Policies & Institutional Proposals** (Bardach & Patashnik Eightfold Path Outcomes Matrix):
   - **Effectiveness (30%)**: empirical magnitude and certainty of solving the target problem.
   - **Cost-Effectiveness & Fiscal Efficiency (25%)**: cost per unit of outcome and deadweight/macroeconomic impact.
   - **Equity & Distributional Incidence (15%)**: who bears the burdens vs. who captures the benefits across groups.
   - **Administrative & Technical Feasibility (15%)**: implementation complexity and enforcement capacity.
   - **Legal/Political Viability & Second-Order Consequences (15%)**: durability and Goodhart/Cobra incentive risks.
4. **Creative Works, Books, Courses & Media**:
   - **Technical/Artistic Craft & Accuracy (35%)**: structural execution, factual rigor, pacing, and production/prose quality.
   - **Signal-to-Noise Density & Originality (35%)**: actionable or memorable insights per hour/page versus filler.
   - **Audience Fit & Prerequisite Alignment (30%)**: match with the user's current skill level, available time, and goals.
