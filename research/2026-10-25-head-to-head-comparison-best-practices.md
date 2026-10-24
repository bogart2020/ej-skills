# Head-to-Head & Side-by-Side Comparison Skill Best Practices: Primary-Source Synthesis

**Date:** 2026-10-25  
**Repository:** `ej-skills`  
**Scope:** Multi-Criteria Decision Analysis (MCDA) and outranking theory, cognitive psychology of comparative judgment, LLM-as-a-judge debiasing, domain-universal entity normalization (places, people, software/architectures, companies, careers, policies, creative works, and products), mathematics of category ties and aggregation paradoxes, and cross-platform AI skill design.

---

## Executive Summary

When a human asks an AI assistant to compare two or more entities—whether *"Austin vs. Denver for a remote software engineer"*, *"PostgreSQL vs. DynamoDB for an event ledger"*, *"Job Offer A vs. Job Offer B"*, *"Nikola Jokić vs. Hakeem Olajuwon"*, *"Nuclear vs. Utility-Scale Solar + Storage"*, or *"MacBook Air vs. ThinkPad X1 Carbon"*—default LLM behavior fails in five predictable ways:

1. **The Spec-Table Trap (Alignability Bias):** The model compares only easily tabulated numbers that happen to share a column label while ignoring qualitative, structural, or unique non-alignable differentiators (Gentner & Markman, 1994, 1997; Zhang & Markman, 1998).
2. **Distinction Bias & False Micro-Wins:** Placed side-by-side in Joint Evaluation, the model awards a category win over a 2% difference that lies inside measurement noise or below the human Just Noticeable Difference (JND) in real-world Separate Evaluation (Hsee, 1996; Hsee & Zhang, 2004, 2010), rather than calling a calibrated **Category Tie** using formal indifference thresholds (Roy, 1968, 1991; Brans & Vincke, 1985).
3. **Unweighted Category-Count Fallacies:** The model either declares an overall winner by counting raw category wins (allowing 4 minor category wins to beat 2 mission-critical category wins) or falls victim to **Simpson's Paradox** (Simpson, 1951) and benchmark-ratio arithmetic-mean distortion (Fleming & Wallace, 1986).
4. **LLM Pairwise Judging Biases:** Unstructured LLM comparisons suffer from **Position Bias** (favoring whichever contender is named first), **Verbosity/Documentation-Density Bias**, and **Halo Error** (Thorndike, 1920; Zheng et al., 2023; Wang et al., 2023).
5. **Evasive Fence-Sitting:** To avoid taking a rigorous analytical stand, default responses end with *"Both are excellent choices depending on what you value!"* without computing weighted utilities, naming category winners/ties, declaring an overall verdict, or stating the exact numerical threshold that would flip the winner.

Building a rigorous, domain-universal **Head-to-Head Comparison Skill** requires synthesizing five primary research traditions:

1. **Multi-Criteria Decision Analysis (MCDA) & Outranking Methods:** Thomas Saaty's **Analytic Hierarchy Process (AHP)** (1977, 1990) and its rank-reversal fixes (Belton & Gear, 1983; Dyer, 1990); Hwang & Yoon's **TOPSIS** (1981) for geometric distance to positive- and negative-ideal solutions; Bernard Roy's **ELECTRE** (1968, 1991) and Brans & Vincke's **PROMETHEE** (1985) for **indifference ($q$), strict preference ($p$), and non-compensatory veto ($v$) thresholds**; and Hammond, Keeney, & Raiffa's **Even Swaps** (1998) for commensurable trade-offs.
2. **Cognitive Science of Comparative Judgment & LLM Judge Debiasing:** Dedre Gentner & Arthur Markman's **Structural Alignment Theory** (1994, 1997) to surface non-alignable differences; Christopher Hsee's **General Evaluability Theory** (1996, 1999, 2010) to neutralize **Distinction Bias**; Huber, Payne, & Puto's **Decoy Effect** (1982), Simonson's **Compromise Effect** (1989), and Pratkanis & Farquhar's **Phantom Alternatives** (1992); and **Thurstone / Bradley-Terry / Glicko** paired-comparison theory (1927, 1952, 1999) combined with **MT-Bench / Chatbot Arena** protocols (Zheng et al., 2023; Wang et al., 2023) to enforce order-swap invariance and blinded per-criterion scoring.
3. **Domain-Universal Normalization Frameworks (Beyond Products):** Purchasing Power Parity (PPP) / BEA Regional Price Parities (RPP) and **EIU / OECD / Mercer** frameworks for **Places**; **Schmidt & Hunter** (1998), **Sackett et al.** (2022), **BARS** (Smith & Kendall, 1963), **Gould's *Full House* Era-Adjusted Z-Scores** (1996), and **WAR / JAWS** for **People**; **ISO/IEC 25010:2023**, **SEI ATAM** (Kazman et al., 2000), and **Geometric Mean Benchmark Aggregation** (Fleming & Wallace, 1986) for **Software & Architectures**; and **Balanced Scorecard** (Kaplan & Norton, 1992) plus **Bardach & Patashnik's Policy Outcomes Matrix** for **Companies, Careers, Policies, and Creative Works**.
4. **Mathematics of MECE Criteria, Indifference Zones (Ties), and Verdict Aggregation:** Preferential independence (Keeney & Raiffa, 1976) to prevent double-counting correlated categories; formal indifference zones ($|g_j(A) - g_j(B)| \le q_j$) to justify **Category Ties**; and dual accounting that reconciles the **Category Win-Loss-Tie Tally** with **Weighted Utility ($U$) + Veto Checks**.
5. **Skill Architecture & Clean Boundary with `should-i-buy`:** Separating horizontal multi-entity comparison (`compare` / `head-to-head`) from vertical capital-allocation gating (`should-i-buy`).

---

## 1. Multi-Criteria Decision Analysis (MCDA) & Toe-to-Toe Comparison Frameworks

### 1.1 Analytic Hierarchy Process (AHP), Pairwise Matrices & Rank Reversal (Saaty, 1977, 1990; Belton & Gear, 1983; Dyer, 1990)

When comparing entities across multiple competing criteria, decision-makers struggle to assign globally consistent weights to 6–8 criteria simultaneously, but can reliably judge the relative importance of **two criteria at a time**.

- **Primary Sources:**
  - Thomas L. Saaty (1977), *"A scaling method for priorities in hierarchical structures"*, *Journal of Mathematical Psychology*, Vol. 15, No. 3, pp. 234–281 ([DOI: 10.1016/0022-2496(77)90033-5](https://doi.org/10.1016/0022-2496(77)90033-5)).
  - Thomas L. Saaty (1990), *"How to make a decision: The Analytic Hierarchy Process"*, *European Journal of Operational Research*, Vol. 48, No. 1, pp. 9–26 ([DOI: 10.1016/0377-2217(90)90057-I](https://doi.org/10.1016/0377-2217(90)90057-I)).
  - Valerie Belton & Tony Gear (1983), *"On a short-coming of Saaty's method of analytic hierarchies"*, *Omega*, Vol. 11, No. 3, pp. 228–230 ([DOI: 10.1016/0305-0483(83)90047-6](https://doi.org/10.1016/0305-0483(83)90047-6)).
  - James S. Dyer (1990), *"Remarks on the Analytic Hierarchy Process"*, *Management Science*, Vol. 36, No. 3, pp. 249–258 ([DOI: 10.1287/mnsc.36.3.249](https://doi.org/10.1287/mnsc.36.3.249)).

- **Core Mathematical Structure:**
  1. **Reciprocal Pairwise Matrix:** For $m$ evaluation categories, construct an $m \times m$ positive reciprocal matrix $A = [a_{jk}]$ where $a_{jk} \in \{1/9, \dots, 1, \dots, 9\}$ represents the relative importance of category $j$ over category $k$, with $a_{jj} = 1$ and $a_{kj} = 1 / a_{jk}$.
  2. **Priority Vector Derivation:** The normalized weight vector $w = (w_1, \dots, w_m)^T$ with $\sum_{j=1}^m w_j = 1$ satisfies the principal eigenvalue problem:
     $$A w = \lambda_{\max} w$$
     (or via the geometric mean of each row, $w_j = \left(\prod_{k=1}^m a_{jk}\right)^{1/m} \Big/ \sum_{i=1}^m \left(\prod_{k=1}^m a_{ik}\right)^{1/m}$, which is invariant to scale inversion).
  3. **Consistency Ratio ($\text{CR}$) Audit:** Because pairwise human or LLM judgments can become intransitive ($A \succ B$, $B \succ C$, $C \succ A$), Saaty defines the Consistency Index ($\text{CI}$) and Consistency Ratio ($\text{CR}$):
     $$\text{CI} = \frac{\lambda_{\max} - m}{m - 1}, \qquad \text{CR} = \frac{\text{CI}}{\text{RI}_m}$$
     where $\text{RI}_m$ is the average random consistency index for dimension $m$. If $\text{CR} > 0.10$, the pairwise judgments are internally inconsistent and must be revised before declaring a winner.
  4. **The Rank Reversal Vulnerability & Ideal-Mode Fix (Belton & Gear, 1983; Dyer, 1990):**
     Belton & Gear (1983) proved that in classical distributive AHP—where candidate scores on criterion $j$ are normalized by dividing by the **column sum** ($\sum_{i=1}^n s_{ij}$)—simply introducing a near-duplicate or irrelevant copy of one option dilutes that criterion's share of priority and can **reverse the rank order** of the original contenders ($A \succ B$ flips to $B \succ A$).
     - **Agentic Guardrail (Ideal-Mode Normalization):** Never normalize contender scores by dividing by the sum of contenders in the choice set. Instead, use **Ideal-Mode AHP** (Belton & Gear, 1983)—dividing by the maximum score or anchoring to fixed domain benchmarks $[x_{j,\min}^{\text{domain}}, x_{j,\max}^{\text{domain}}]$—so adding or removing a third contender cannot algebraically corrupt the pairwise ranking of the first two.

### 1.2 TOPSIS: Geometric Distance to Positive-Ideal and Negative-Ideal Solutions (Hwang & Yoon, 1981)

Linear weighted sums ($U(x_i) = \sum w_j u_j(x_{ij})$) are purely compensatory: an option with an extreme, crippling weakness in one category can still achieve a high arithmetic average if it has extreme outlier scores elsewhere. **TOPSIS** (*Technique for Order Preference by Similarity to Ideal Solution*) resolves this by measuring **Euclidean distance** to both the best possible and worst possible reference vectors.

- **Primary Source:**
  - Ching-Lai Hwang & Kwangsun Yoon (1981), *Multiple Attribute Decision Making: Methods and Applications — A State-of-the-Art Survey*, Lecture Notes in Economics and Mathematical Systems, Vol. 186, Springer-Verlag ([DOI: 10.1007/978-3-642-48318-9](https://doi.org/10.1007/978-3-642-48318-9)).

- **Core Mathematical Equations:**
  Given $n$ contenders $i \in \{1, \dots, n\}$ and $m$ criteria $j \in \{1, \dots, m\}$ with weights $w_j$ ($\sum w_j = 1$):
  1. **Vector Normalization & Weighting:**
     $$r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{k=1}^{n} x_{kj}^2}}, \qquad v_{ij} = w_j r_{ij}$$
  2. **Positive-Ideal ($A^+$) and Negative-Ideal ($A^-$) Reference Points:**
     $$A^+ = (v_1^+, \dots, v_m^+), \qquad A^- = (v_1^-, \dots, v_m^-)$$
     where $v_j^+ = \max_i v_{ij}$ for benefit criteria ($\min_i v_{ij}$ for cost criteria) and $v_j^- = \min_i v_{ij}$ for benefit criteria ($\max_i v_{ij}$ for cost criteria).
  3. **Separation Measures ($L_2$ Euclidean Distance):**
     $$D_i^+ = \sqrt{\sum_{j=1}^{m} (v_{ij} - v_j^+)^2}, \qquad D_i^- = \sqrt{\sum_{j=1}^{m} (v_{ij} - v_j^-)^2}$$
  4. **Relative Closeness Coefficient ($C_i^*$):**
     $$C_i^* = \frac{D_i^-}{D_i^+ + D_i^-} \in [0, 1]$$
     Because squared Euclidean distance penalizes large single-criterion deviations nonlinearly, TOPSIS naturally favors **well-rounded contenders** close to $A^+$ and far from $A^-$ over lopsided contenders.

### 1.3 Outranking Methods (ELECTRE & PROMETHEE): Indifference ($q$), Preference ($p$), and Veto ($v$) Thresholds (Roy, 1968, 1991; Brans & Vincke, 1985)

The single greatest flaw of naive decision matrices is **false precision**: if Laptop A weighs $1.24\text{ kg}$ and Laptop B weighs $1.26\text{ kg}$, or City A has an average commute of $26.2\text{ min}$ vs. City B's $26.8\text{ min}$, an uncalibrated comparator awards a category win to A. The French/European **Outranking School**—founded by **Bernard Roy** (**ELECTRE**) and extended by **Jean-Pierre Brans & Philippe Vincke** (**PROMETHEE**)—solved this by introducing **pseudo-criteria with explicit indifference, preference, and veto thresholds**.

- **Primary Sources:**
  - Bernard Roy (1968), *"Classement et choix en présence de points de vue multiples (la méthode ELECTRE)"*, *Revue Française d'Informatique et de Recherche Opérationnelle (RIRO)*, Vol. 2, No. V1, pp. 57–75 ([DOI: 10.1051/ro/196802V100571](https://doi.org/10.1051/ro/196802V100571)).
  - Bernard Roy (1991), *"The outranking approach and the foundations of ELECTRE methods"*, *Theory and Decision*, Vol. 31, No. 1, pp. 49–73 ([DOI: 10.1007/BF00134132](https://doi.org/10.1007/BF00134132)).
  - Jean-Pierre Brans & Philippe Vincke (1985), *"Note—A Preference Ranking Organisation Method: (The PROMETHEE Method for Multiple Criteria Decision-Making)"*, *Management Science*, Vol. 31, No. 6, pp. 647–656 ([DOI: 10.1287/mnsc.31.6.647](https://doi.org/10.1287/mnsc.31.6.647)).

- **The Three Thresholds Governing Every Category Evaluation:**
  For any criterion $g_j$ (oriented so higher is better) and pair of contenders $(a, b)$ with difference $d_j(a, b) = g_j(a) - g_j(b)$:

| Threshold Symbol | Name | Mathematical Condition | Meaning in a Head-to-Head Comparison Skill |
| :--- | :--- | :--- | :--- |
| **$q_j$** | **Indifference Threshold** | $|g_j(a) - g_j(b)| \le q_j$ | **Mandatory Category Tie (`Tie`).** The gap is smaller than the Just Noticeable Difference (JND), within measurement/sampling noise, or practically inconsequential in lived use. Neither contender receives a category win ($P_j(a, b) = 0$ and $P_j(b, a) = 0$). |
| **$p_j$** | **Strict Preference Threshold** | $g_j(a) - g_j(b) \ge p_j$ | **Decisive Category Win (`Decisive Win`).** Contender $a$ outperforms $b$ by a margin that produces an unmistakable, real-world experiential or financial advantage ($P_j(a, b) = 1$). When $q_j < g_j(a) - g_j(b) < p_j$, $a$ earns a **`Narrow Edge`** with linear preference intensity $P_j(a,b) = \frac{d_j(a,b) - q_j}{p_j - q_j} \in (0, 1)$. |
| **$v_j$** | **Veto Threshold** ($v_j > p_j$) | $g_j(b) - g_j(a) \ge v_j$ | **Non-Compensatory Veto.** Contender $a$'s deficit on criterion $j$ is so severe that $a$ **cannot outrank $b$ overall** ($\text{Discordance } D_j(a, b) = 1 \implies a \not\mathrel{S} b$), even if $a$ wins a majority of minor categories. |

- **PROMETHEE Outranking Flows (for $n \ge 2$ Contenders):**
  Using Brans & Vincke's (1985) pairwise preference index $\pi(a, b) = \sum_{j=1}^m w_j P_j(a, b)$, every contender $a$ in a multi-way matchup has:
  - **Leaving (Positive) Flow $\phi^+(a) = \frac{1}{n-1} \sum_{x \neq a} \pi(a, x)$:** How strongly $a$ dominates all other contenders.
  - **Entering (Negative) Flow $\phi^-(a) = \frac{1}{n-1} \sum_{x \neq a} \pi(x, a)$:** How strongly $a$ is dominated by all other contenders.
  - **Net Outranking Flow $\phi(a) = \phi^+(a) - \phi^-(a) \in [-1, 1]$:** Provides a complete ranking (**PROMETHEE II**), while comparing $\phi^+$ and $\phi^-$ separately (**PROMETHEE I**) identifies **genuine incomparabilities** when one contender has both a high $\phi^+$ (huge strengths) and a high $\phi^-$ (huge weaknesses) compared to a safe generalist.

### 1.4 Non-Compensatory Knockout Pruning (EBA), Pareto Dominance & Even Swaps (Tversky, 1972; Hammond, Keeney, & Raiffa, 1998)

- **Primary Sources:**
  - Amos Tversky (1972), *"Elimination by aspects: A theory of choice"*, *Psychological Review*, Vol. 79, No. 4, pp. 281–299 ([DOI: 10.1037/h0032955](https://doi.org/10.1037/h0032955)).
  - John S. Hammond, Ralph L. Keeney, & Howard Raiffa (1998), *"Even Swaps: A Rational Method for Making Trade-Offs"*, *Harvard Business Review*, Vol. 76, No. 2 (March–April 1998), pp. 137–149 ([HBS Faculty Link](https://www.hbs.edu/faculty/Pages/item.aspx?num=3991); [PubMed: 10177863](https://pubmed.ncbi.nlm.nih.gov/10177863/)).
  - Ralph L. Keeney & Howard Raiffa (1976), *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*, Wiley / Cambridge University Press ([DOI: 10.1017/CBO9781139174084](https://doi.org/10.1017/CBO9781139174084)).

- **Three Structural Simplification Operations Before Scoring:**
  1. **Elimination by Aspects (EBA) (Tversky, 1972):** Before scoring any category, test each contender against the user's non-negotiable **hard constraints** (e.g., visa/legal eligibility for a city or job, maximum latency ceiling for an architecture, dietary/safety rule, budget ceiling). Any contender failing a hard constraint is flagged as **`Disqualified (Knockout)`** upfront.
  2. **Practical Dominance Elimination (Hammond, Keeney, & Raiffa, 1998):**
     - **Strict Pareto Dominance:** If Contender $A$ is at least as good as Contender $B$ on every category ($\forall j,\, g_j(A) \ge g_j(B) - q_j$) and strictly better on at least one ($g_k(A) \ge g_k(B) + p_k$), $B$ is strictly dominated and cannot win under any positive weight vector.
     - **Practical Dominance:** If $A$ beats $B$ on 5 core categories and trails $B$ on only 1 minor category by a trivial margin, $B$ is practically dominated.
  3. **The Even Swaps Method for Qualitative-Quantitative Trade-Offs (Hammond et al., 1998):**
     Abstract 1–10 point scales often obscure what a trade-off means in real life. An **Even Swap** translates category differences into an equivalent adjustment in a natural numeraire (such as dollars, hours per week, or latency milliseconds) that leaves the decision-maker indifferent:
     - *Example (Job Offer A vs. Job Offer B):* Offer A pays \$185k with a 45-minute each-way commute (375 hours/year in traffic); Offer B pays \$170k fully remote. Rather than guessing abstract weights for "Compensation" vs. "Commute", an Even Swap asks: *"Is reclaiming 375 hours of commuting per year (plus ~\$4,500 in after-tax vehicle/transit TCO) worth at least \$10,500 of pre-tax salary (~{\$18–\$20}/hr net)?"* Once swapped into a common unit, the superior contender becomes unmistakable.

---

## 2. Cognitive Science & Behavioral Psychology of Comparative Judgment

### 2.1 Structural Alignment Theory: Alignable vs. Non-Alignable Differences (Gentner & Markman, 1994, 1997; Markman & Medin, 1995; Zhang & Markman, 1998)

Why do both human reviewers and LLMs default to shallow "spec-sheet comparisons"? Cognitive scientists Dedre Gentner, Arthur Markman, Douglas Medin, and Shi Zhang demonstrated that comparison is governed by a **structure-mapping process** that privileges **alignable differences** over **non-alignable differences**.

- **Primary Sources:**
  - Dedre Gentner & Arthur B. Markman (1994), *"Structural Alignment in Comparison: No Difference Without Similarity"*, *Psychological Science*, Vol. 5, No. 3, pp. 152–158 ([DOI: 10.1111/j.1467-9280.1994.tb00652.x](https://doi.org/10.1111/j.1467-9280.1994.tb00652.x)).
  - Dedre Gentner & Arthur B. Markman (1997), *"Structure Mapping in Analogy and Similarity"*, *American Psychologist*, Vol. 52, No. 1, pp. 45–56 ([DOI: 10.1037/0003-066X.52.1.45](https://doi.org/10.1037/0003-066X.52.1.45)).
  - Arthur B. Markman & Douglas L. Medin (1995), *"Similarity and Alignment in Choice"*, *Organizational Behavior and Human Decision Processes*, Vol. 63, No. 2, pp. 117–130 ([DOI: 10.1006/obhd.1995.1067](https://doi.org/10.1006/obhd.1995.1067)).
  - Douglas L. Medin, Robert L. Goldstone, & Arthur B. Markman (1995), *"Comparison and Choice: Relations between Similarity Processes and Decision Processes"*, *Psychonomic Bulletin & Review*, Vol. 2, No. 1, pp. 1–19 ([DOI: 10.3758/BF03214410](https://doi.org/10.3758/BF03214410)).
  - Shi Zhang & Arthur B. Markman (1998), *"Overcoming the Early Entrant Advantage: The Role of Alignable and Nonalignable Differences"*, *Journal of Marketing Research*, Vol. 35, No. 4, pp. 413–426 ([DOI: 10.1177/002224379803500401](https://doi.org/10.1177/002224379803500401)).

- **Core Empirical Findings:**
  1. **Alignable Differences:** Attributes that occupy corresponding slots along a shared dimension (e.g., RAM capacity: $16\text{ GB}$ vs. $32\text{ GB}$; City population: $980\text{k}$ vs. $715\text{k}$; Athlete scoring average: $27.4\text{ ppg}$ vs. $25.1\text{ ppg}$).
  2. **Non-Alignable Differences:** Unique attributes, structural properties, or qualitative realities possessed by one contender that have **no direct counterpart slot** in the other (e.g., a database having native transactional Change Data Capture streams vs. another requiring an external poller; one neighborhood having a walk-to-beach microculture vs. another having a major research university; one job offer exposing the candidate to board-level M&A while the other is a pure IC execution role).
  3. **The Spec-Table Distortion:** Markman & Medin (1995) and Zhang & Markman (1998) proved that because alignable differences are cognitively effortless to place in a table, evaluators **systematically overweight trivial alignable metrics** and **neglect high-impact non-alignable properties** unless explicitly prompted to retrieve and weigh non-alignable features.
- **Agentic Design Rule (Mandatory Non-Alignable Audit):**
  A comparison skill must never stop at a symmetric spec table. It must include a dedicated step and report block for **Non-Alignable & Asymmetric Differentiators**: *"What can Entity A do, enable, or break that has no direct column equivalent in Entity B?"*

### 2.2 General Evaluability Theory: Joint vs. Separate Evaluation & Distinction Bias (Hsee, 1996, 1999; Hsee & Zhang, 2004, 2010)

When humans or AI agents compare options **side-by-side**, they operate in **Joint Evaluation (JE)**. When a human actually lives with the chosen option afterward (living in the chosen city, working at the chosen company, using the chosen tool), they experience it in **Separate Evaluation (SE)**. Christopher K. Hsee and colleagues proved that **JE systematically mispredicts SE satisfaction**.

- **Primary Sources:**
  - Christopher K. Hsee (1996), *"The Evaluability Hypothesis: An Explanation for Preference Reversals between Joint and Separate Evaluations of Alternatives"*, *Organizational Behavior and Human Decision Processes*, Vol. 67, No. 3, pp. 247–257 ([DOI: 10.1006/obhd.1996.0077](https://doi.org/10.1006/obhd.1996.0077)).
  - Christopher K. Hsee, George F. Loewenstein, Sally Blount, & Max H. Bazerman (1999), *"Preference reversals between joint and separate evaluations of options: A review and theoretical analysis"*, *Psychological Bulletin*, Vol. 125, No. 5, pp. 576–590 ([DOI: 10.1037/0033-2909.125.5.576](https://doi.org/10.1037/0033-2909.125.5.576)).
  - Christopher K. Hsee & Jiao Zhang (2004), *"Distinction bias: Misprediction and mischoice due to joint evaluation"*, *Journal of Personality and Social Psychology*, Vol. 86, No. 5, pp. 680–695 ([DOI: 10.1037/0022-3514.86.5.680](https://doi.org/10.1037/0022-3514.86.5.680)).
  - Christopher K. Hsee & Jiao Zhang (2010), *"General Evaluability Theory"*, *Perspectives on Psychological Science*, Vol. 5, No. 4, pp. 343–355 ([DOI: 10.1177/1745691610374586](https://doi.org/10.1177/1745691610374586)).

- **Two Pathologies of Side-by-Side Comparison:**
  1. **The Evaluability Reversal (Hsee, 1996):** In Hsee's classic dictionary study, Dictionary A had 10,000 entries and a pristine cover; Dictionary B had 20,000 entries and a torn cover. In Separate Evaluation (where people don't know if 10,000 entries is good or bad, but immediately feel a torn cover), people paid more for A. In Joint Evaluation, 20,000 vs. 10,000 became instantly evaluable, so people chose B. Conversely, for attributes where the **lived experiential attribute** (e.g., daily team toxicity, seat comfort, neighborhood noise, API ergonomics) is hard to quantify in a side-by-side table while a **minor numerical spec** (e.g., \$3,000 salary delta, 15% synthetic benchmark score, 100 sq ft apartment difference) is easy to compare, Joint Evaluation tricks the decision-maker into sacrificing daily lived well-being for a number on a chart.
  2. **Distinction Bias (Hsee & Zhang, 2004):** Side-by-side comparison magnifies small quantitative differences along a continuous scale. Evaluators comparing two TVs, two sound systems, two apartments, or two camera sensors side-by-side strongly prefer the marginally higher spec and pay a large premium for it—even though in **Separate Evaluation** (once the other option is no longer sitting next to it), human perception adapts immediately and the difference produces **zero measurable difference in experienced utility**.

- **Agentic Design Rule (The Separate-Evaluation Translation Test):**
  Before awarding a category win in a side-by-side table, the agent must apply the **Separate-Evaluation Translation Test**:
  > *"Six months from now, when the user is experiencing Contender A alone (without Contender B sitting next to it on a spec sheet), will this difference actually be felt in daily life, or is it an artifact of Joint-Evaluation Distinction Bias?"*
  If the difference is only noticeable when juxtaposed on a spec sheet, set it inside the **Indifference Threshold ($q_j$)** and score the category as a **`Tie`**.

### 2.3 Choice-Set Context Effects: Decoy, Compromise, and Phantom Alternatives (Huber, Payne, & Puto, 1982; Simonson, 1989; Pratkanis & Farquhar, 1992)

When a head-to-head comparison expands to **3 or more contenders** ($A, B, C, \dots$), the structure of the choice set itself can manipulate the outcome:

- **Primary Sources:**
  - Joel Huber, John W. Payne, & Christopher Puto (1982), *"Adding Asymmetrically Dominated Alternatives: Violations of Regularity and the Similarity Hypothesis"*, *Journal of Consumer Research*, Vol. 9, No. 1, pp. 90–98 ([DOI: 10.1086/208899](https://doi.org/10.1086/208899)).
  - Itamar Simonson (1989), *"Choice Based on Reasons: The Case of Attraction and Compromise Effects"*, *Journal of Consumer Research*, Vol. 16, No. 2, pp. 158–174 ([DOI: 10.1086/209205](https://doi.org/10.1086/209205)).
  - Anthony R. Pratkanis & Peter H. Farquhar (1992), *"A Brief History of Research on Phantom Alternatives: Evidence for Seven Empirical Generalizations About Phantoms"*, *Basic and Applied Social Psychology*, Vol. 13, No. 1, pp. 103–122 ([DOI: 10.1207/s15324834basp1301_9](https://doi.org/10.1207/s15324834basp1301_9)).

| Context Effect | Mechanism | Agentic Countermeasure |
| :--- | :--- | :--- |
| **Asymmetric Dominance / Decoy Effect** (Huber, Payne, & Puto, 1982) | Option $D$ (the decoy) is strictly dominated by Target $A$, but not by Competitor $B$. The presence of $D$ makes $A$ look like a "dominant winner" and inflates $A$'s selection probability, violating Luce's Regularity Axiom. | **Pre-Scoring Dominance Purge:** Identify and strip asymmetrically dominated decoys (e.g., middle pricing tiers designed solely to push buyers to the "Pro" tier, or strawman policy options) before scoring the real contenders. |
| **Compromise Effect** (Simonson, 1989) | Adding an extreme high-end/high-cost option $C$ makes a previously expensive option $B$ appear to be the "sensible middle compromise" between $A$ and $C$. | **Objective-Anchored Scoring:** Anchor utility scales $u_j(\cdot)$ to the user's actual requirements and domain benchmarks, never to the min-max range of whatever extreme items happen to be in the prompt. |
| **Phantom Alternative Effect** (Pratkanis & Farquhar, 1992) | Including an unavailable option (e.g., an out-of-stock GPU at MSRP, a dream apartment that already rented, a candidate who declined the offer, or vaporware) distorts criteria weights and biases selection toward the closest available lookalike. | **Availability & Feasibility Gate:** Verify whether all contenders are actually attainable/available. Flag unavailable contenders as **Phantoms** and exclude them from distorting the active choice set (unless used explicitly as a historical reference benchmark). |

### 2.4 Probabilistic Pairwise Models & Debiasing LLM-as-a-Judge (Thurstone, 1927; Bradley & Terry, 1952; Glickman, 1999; Zheng et al., 2023; Wang et al., 2023)

In mathematical psychology and tournament theory, pairwise comparisons are modeled probabilistically because every observation of performance carries variance. When an LLM acts as the comparative judge, it introduces additional systematic biases that have been rigorously quantified in modern AI evaluation literature.

- **Primary Sources:**
  - Louis L. Thurstone (1927), *"A law of comparative judgment"*, *Psychological Review*, Vol. 34, No. 4, pp. 273–286 ([DOI: 10.1037/h0070288](https://doi.org/10.1037/h0070288)).
  - Ralph Allan Bradley & Milton E. Terry (1952), *"Rank Analysis of Incomplete Block Designs: I. The Method of Paired Comparisons"*, *Biometrika*, Vol. 39, No. 3/4, pp. 324–345 ([DOI: 10.1093/biomet/39.3-4.324](https://doi.org/10.1093/biomet/39.3-4.324)).
  - Mark E. Glickman (1999), *"Parameter estimation in large dynamic paired comparison experiments"*, *Journal of the Royal Statistical Society: Series C (Applied Statistics)*, Vol. 48, No. 3, pp. 377–394 ([DOI: 10.1111/1467-9876.00159](https://doi.org/10.1111/1467-9876.00159)).
  - Edward L. Thorndike (1920), *"A constant error in psychological ratings"*, *Journal of Applied Psychology*, Vol. 4, No. 1, pp. 25–29 ([DOI: 10.1037/h0071663](https://doi.org/10.1037/h0071663)).
  - Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, & Ion Stoica (2023), *"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"*, *NeurIPS 2023 Datasets and Benchmarks* ([arXiv:2306.05685](https://arxiv.org/abs/2306.05685)).
  - Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Qi Liu, Tianyu Liu, & Zhifang Sui (2023), *"Large Language Models are not Fair Evaluators"*, *ACL 2024* ([arXiv:2305.17926](https://arxiv.org/abs/2305.17926)).

- **Core Mathematical & Empirical Foundations:**
  1. **Thurstone's Case V & Bradley-Terry Model (1927, 1952):**
     Every entity $i$ has a latent quality distribution $S_i \sim \mathcal{N}(\mu_i, \sigma_i^2)$. In Thurstone's Law of Comparative Judgment, the standardized difference between $A$ and $B$ is:
     $$z_{AB} = \frac{\mu_A - \mu_B}{\sqrt{\sigma_A^2 + \sigma_B^2 - 2 r_{AB} \sigma_A \sigma_B}}$$
     When $\sigma_A^2 + \sigma_B^2$ (epistemic/measurement variance) is large relative to $|\mu_A - \mu_B|$, $P(A \succ B) = \Phi(z_{AB}) \approx 0.50$. Similarly, in **Glicko** (Glickman, 1999), each contender has both a rating $\mu_i$ and a **Rating Deviation ($RD_i$)** measuring evidence uncertainty: comparing a well-documented contender ($RD_A$ small) against an under-documented contender ($RD_B$ large) requires explicitly flagging the confidence gap rather than assuming the under-documented contender is inferior.
  2. **The Four LLM Comparative Biases (Thorndike, 1920; Zheng et al., 2023; Wang et al., 2023):**
     - **Position / Order Bias:** Wang et al. (2023) proved that simply swapping whether an entity is listed first ("Contender A") vs. second ("Contender B") flips LLM pairwise verdicts in up to 40–60% of close matchups.
     - **Verbosity / Documentation-Volume Bias:** Zheng et al. (2023) demonstrated that LLM judges systematically favor longer, more verbose descriptions or entities with greater marketing/SEO volume on the web.
     - **Halo Effect (Thorndike, 1920):** Originally discovered by Edward Thorndike in 1920 when military officers' global impression of a soldier contaminated their ratings of independent traits (intelligence, physique, leadership, character), LLMs suffer from strong autoregressive Halo bias: if Contender A is evaluated end-to-end before Contender B, or if Contender A wins Category 1, the model unconsciously inflates Contender A's ratings on Categories 2–6.
     - **User-Premise Sycophancy:** If the user asks *"Why is X better than Y?"* or lists their favorite option first, the model biases retrieval and weighting to make X win.

- **Three Mandatory Debiasing Protocols for an Agentic Comparison Skill:**
  1. **Horizontal Criterion-by-Criterion Evaluation (Thorndike Anti-Halo Rule):** Never evaluate all categories of Entity A and then all categories of Entity B. Always evaluate **Category 1 across all contenders simultaneously** using objective rubric anchors, lock the Category 1 verdict, and only then proceed to Category 2.
  2. **Symmetric Retrieval Parity:** Run identical search query structures (both positive capability queries and adversarial failure/criticism queries) for *every* contender so documentation volume or marketing SEO does not masquerade as superiority.
  3. **Order-Swap Invariance Check ($f(A, B) \equiv f(B, A)$):** Before finalizing any `Narrow Edge` or overall verdict, mentally invert the presentation order: *"If Contender B had been listed first in the prompt and Contender A second, would the category winner and overall verdict remain identical based strictly on the verified numbers?"* If swapping order flips the winner, the true verdict is a **`Tie`**.

---

## 3. Methodology for Universal Entity Comparisons (Beyond Products)

A universal head-to-head skill must evaluate **any class of entity** using the canonical primary-source methodology of that domain rather than treating cities, people, software architectures, or policies like retail gadgets.

### 3.1 Comparing Places (Cities, Neighborhoods, Countries, Venues, Campuses)

- **Primary Frameworks & Methodological Sources:**
  - **Economist Intelligence Unit (EIU)**, *Global Liveability Index* methodology—evaluates urban environments across 30+ indicators grouped into 5 weighted categories: **Stability (25%)**, **Healthcare (20%)**, **Culture & Environment (25%)**, **Education (10%)**, and **Infrastructure (20%)**.
  - **OECD**, *Better Life Index* ([oecd.org/betterlifeindex](https://www.oecd.org/en/data/tools/oecd-better-life-index.html))—11 dimensions of material living conditions and quality of life (**Housing, Income, Jobs, Community, Education, Environment, Civic Engagement, Health, Life Satisfaction, Safety, Work-Life Balance**) with user-adjustable weights.
  - **U.S. Bureau of Economic Analysis (BEA)**, *Regional Price Parities (RPPs)* ([bea.gov/data/prices-inflation/regional-price-parities-state-and-metro-area](https://www.bea.gov/data/prices-inflation/regional-price-parities-state-and-metro-area)) & **World Bank International Comparison Program (ICP)**, *Purchasing Power Parities (PPPs)*.
  - **Mercer**, *Quality of Living City Ranking* (39 factors across 10 categories oriented toward relocation and expatriate conditions).

- **Mandatory Normalization Rules for Comparing Places:**
  1. **PPP / RPP & Tax-Adjusted Real Disposable Surplus (Never Compare Nominal Dollars):**
     Earning \$180,000 in San Francisco or Manhattan vs. \$135,000 in Raleigh or Austin cannot be compared via nominal salary or raw price indices alone. Compute **Annual Real Discretionary Surplus ($S_{\text{real}, i}$)**:
     $$S_{\text{real}, i} = \frac{Y_{\text{gross}, i} - T_{\text{fed+state+local}, i} - C_{\text{housing}, i} - C_{\text{transport+childcare}, i}}{\text{RPP}_i / 100}$$
     where $T_{\text{fed+state+local}, i}$ includes federal, state, and municipal income taxes plus property/sales tax incidence, and $C_{\text{housing}, i}$ prices an **equivalent housing standard** (same bedroom count, safety tier, and commute time).
  2. **Tract/Neighborhood-Level Granularity (Avoiding the Ecological Fallacy):**
     City-wide averages hide massive intra-city variance. Always anchor comparisons to the **specific neighborhood tier** the user can afford on their budget, comparing:
     - **Mobility & Door-to-Door Time Tax:** Walk Score / Bike Score / Transit Score, rush-hour commute distribution, and airport connectivity.
     - **Climate Comfort Distribution:** Not "average annual temperature" (which makes a city with $0^\circ\text{F}$ winters and $100^\circ\text{F}$ summers look identical to a $50^\circ\text{F}$ coastal city), but **comfortable outdoor days per year** (e.g., dew point $< 65^\circ\text{F}$ and high between $55^\circ\text{F}$ and $82^\circ\text{F}$), sunshine hours, natural disaster/wildfire/flood risk, and air quality ($\text{PM}_{2.5}$ / AQI).
     - **Safety & Healthcare Access:** Violent and property crime rates per 100,000 at the neighborhood level (distinguishing concentrated vs. dispersed risk) and proximity to Tier-1 hospitals.
     - **Labor Market Depth & Social/Third-Place Fit:** Density of alternative employers in the user's industry (career insurance if laid off without relocating again) and demographic/cultural alignment.

### 3.2 Comparing People (Job Candidates, Leaders, Athletes, Historical Figures, Creators)

#### A. Job Candidates, Executives & Service Providers (Industrial-Organizational Psychology)
- **Primary Sources:**
  - Frank L. Schmidt & John E. Hunter (1998), *"The validity and utility of selection methods in personnel psychology: Practical and theoretical implications of 85 years of research findings"*, *Psychological Bulletin*, Vol. 124, No. 2, pp. 262–274 ([DOI: 10.1037/0033-2909.124.2.262](https://doi.org/10.1037/0033-2909.124.2.262)).
  - Paul R. Sackett, Charlene Zhang, Christopher M. Berry, & Filip Lievens (2022), *"Revisiting meta-analytic estimates of validity in personnel selection: Addressing systematic overcorrection for restriction of range"*, *Journal of Applied Psychology*, Vol. 107, No. 11, pp. 2040–2068 ([DOI: 10.1037/apl0000994](https://doi.org/10.1037/apl0000994)).
  - Patricia Cain Smith & Lorne M. Kendall (1963), *"Retranslation of expectations: An approach to the construction of unambiguous anchors for rating scales"* (**Behaviorally Anchored Rating Scales — BARS**), *Journal of Applied Psychology*, Vol. 47, No. 2, pp. 149–155 ([DOI: 10.1037/h0047060](https://doi.org/10.1037/h0047060)).

- **Core Scientific Rules for Comparing Candidates:**
  1. **Predictive Validity Hierarchy (Schmidt & Hunter, 1998; Sackett et al., 2022):** Across 85+ years of meta-analytic I/O psychology, **work sample tests**, **structured behavioral interviews**, and **verified past performance under comparable scope/constraints** have the highest operational validity, whereas unstructured holistic impressions, years of raw tenure, and prestige pedigree ("worked at Famous Co.") have low incremental validity and high Halo distortion.
  2. **Behaviorally Anchored Rating Scales (BARS) (Smith & Kendall, 1963):** Never score candidates on vague adjectives ("Leadership: 8/10"). Define explicit **behavioral anchors** for each competency (e.g., *Level 1: Executed scoped tasks with supervision; Level 3: Owned end-to-end system delivery across 1–2 teams; Level 5: Redesigned multi-team architecture under ambiguity with measurable business impact*) and map concrete evidence from each candidate's portfolio, work sample, or reference trail to the anchor.

#### B. Athletes, Public Figures, Artists & Cross-Era Historical Matchups
- **Primary Sources:**
  - Stephen Jay Gould (1996), *Full House: The Spread of Excellence from Plato to Darwin*, Harmony Books / Three Rivers Press ([ISBN: 978-0517703946](https://en.wikipedia.org/wiki/Full_House:_The_Spread_of_Excellence_from_Plato_to_Darwin)).
  - Jay Jaffe (2004, 2017), *The Cooperstown Casebook* & the **JAWS (Jaffe WAR Score)** methodology ([Baseball-Reference JAWS](https://www.baseball-reference.com/about/jaws.shtml)).

- **Three Mandatory Normalization Laws for Historical & Sports Comparisons:**
  1. **Era-Adjusted Z-Score Normalization (Gould's *Full House* Principle, 1996):**
     In *Full House*, Stephen Jay Gould proved why raw historical outputs (e.g., a .400 batting average in 1911 vs. .350 in 1995, or raw points/wealth/citations across centuries) cannot be compared at face value: as any competitive domain matures, nutrition, training, tactics, and global talent pool size expand, causing the **system-wide standard deviation ($\sigma_{\text{era}}$) to shrink toward the right wall of human limits**. Therefore, cross-era comparisons must measure **dominance relative to contemporary peer distribution**:
     $$Z_{i, \text{era}} = \frac{X_i - \mu_{\text{era}}}{\sigma_{\text{era}}}$$
     coupled with explicit discussion of **pool-depth expansion** (how large and integrated the competitive pool was in each era).
  2. **Context & Replacement-Level Normalization (WAR Principle):**
     Adjust raw outputs for **environment and opportunity** (pace of play, ballpark/venue effects, team supporting cast, rule regime, resources inherited) and measure value added over a **replacement-level baseline** ($\text{WAR}$), not raw counting volume.
  3. **Peak Ceiling vs. Career Longevity Synthesis (JAWS Principle):**
     Every "Greatest / Who Was Better" comparison collides on **Peak Dominance** (highest 3-to-7 year prime ceiling) vs. **Longevity / Cumulative Compiler Value** (15–20 years of sustained high production). Following Jay Jaffe's **JAWS** formula:
     $$\text{Composite Value} = \frac{1}{2} \left(\text{Career Cumulative Value} + \text{Prime Peak Value}\right)$$
     Always evaluate **Peak Ceiling**, **Career Longevity/Consistency**, and **High-Leverage/Postseason/Crisis Performance** as separate MECE categories before synthesizing the overall verdict.

### 3.3 Comparing Technologies, Software, Libraries, Models & System Architectures

- **Primary Sources:**
  - **ISO/IEC 25010:2023**, *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (2nd Edition, 2023), International Organization for Standardization ([ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html)).
  - Rick Kazman, Mark Klein, & Paul Clements (2000), *ATAM: Method for Architecture Evaluation*, Technical Report **CMU/SEI-2000-TR-004**, Software Engineering Institute, Carnegie Mellon University ([SEI Digital Library](https://insights.sei.cmu.edu/library/atam-method-for-architecture-evaluation/)).
  - Philip J. Fleming & John J. Wallace (1986), *"How not to lie with statistics: The correct way to summarize benchmark results"*, *Communications of the ACM*, Vol. 29, No. 3, pp. 218–221 ([DOI: 10.1145/5666.5673](https://doi.org/10.1145/5666.5673)).

- **Core Scientific Rules for Comparing Software & Architectures:**
  1. **ISO/IEC 25010:2023 Quality Taxonomy:** Select MECE evaluation dimensions from the 9 standardized SQuaRE product quality characteristics tailored to the workload: **Functional Suitability**, **Performance Efficiency** (latency $p_{50}/p_{99}$, throughput, memory/CPU footprint), **Compatibility/Interoperability**, **Interaction Capability / Developer Experience (DX)**, **Reliability** (fault tolerance, recoverability, availability SLA), **Security**, **Maintainability** (modularity, testability, upgrade friction), **Flexibility/Scalability**, and **Safety/Operational Risk** (plus **Ecosystem Maturity & Licensing/Lock-In**).
  2. **ATAM Concrete Quality-Attribute Scenarios & Tradeoff Points (Kazman et al., 2000):**
     In the SEI **Architecture Tradeoff Analysis Method (ATAM)**, vague claims like *"System A is more scalable"* are rejected. Every architectural criterion must be expressed as a concrete **Stimulus $\rightarrow$ Environment $\rightarrow$ Response Measure** scenario (e.g., *"Under 5,000 write RPS with a 200GB working set, maintain $p_{99} < 15\text{ ms}$ during single-node failover"*), and the evaluator must explicitly identify **architectural tradeoff points** where improving one quality attribute (e.g., strict serializable consistency or zero-dependency simplicity) necessarily degrades another (e.g., cross-region write latency or out-of-the-box feature velocity).
  3. **Fleming & Wallace's Law of Benchmark Aggregation (1986):**
     Fleming & Wallace (1986) proved mathematically in *Communications of the ACM* that taking the **arithmetic mean** of normalized benchmark ratios ($r_{k} = t_{B,k} / t_{A,k}$) is **statistically invalid**: simply switching which system is used as the normalization baseline ($A$ vs. $B$) can make the arithmetic mean declare *both* $A$ faster than $B$ and $B$ faster than $A$ on the exact same dataset!
     - **Mandatory Benchmark Rule:** When aggregating relative performance ratios across $K$ benchmarks or workloads, **always use the Geometric Mean**:
       $$\text{GeoMean}\left(\frac{A}{B}\right) = \left(\prod_{k=1}^{K} \frac{y_{A,k}}{y_{B,k}}\right)^{1/K} = \exp\left(\frac{1}{K}\sum_{k=1}^{K} \ln\left(\frac{y_{A,k}}{y_{B,k}}\right)\right)$$
       Because $\text{GeoMean}(A/B) = [\text{GeoMean}(B/A)]^{-1}$, the geometric mean is strictly invariant to the choice of reference baseline. Furthermore, weight workloads by **actual production traffic mix**, never by unweighted synthetic microbenchmarks.

### 3.4 Comparing Companies, Careers / Job Offers, Public Policies & Creative Works

| Entity Class | Primary Methodological Framework | Canonical MECE Comparison Dimensions |
| :--- | :--- | :--- |
| **Companies, Stocks & Business Models** | **Balanced Scorecard** — Robert S. Kaplan & David P. Norton (1992), *"The Balanced Scorecard—Measures That Drive Performance"*, *Harvard Business Review*, Vol. 70, No. 1, pp. 71–79 ([HBR Link](https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2)), paired with Unit Economics & Competitive Moat Analysis. | 1. **Financial & Unit Economics** (Revenue growth, gross/operating margin, ROIC, FCF, LTV:CAC, balance-sheet leverage)<br>2. **Customer & Market Position** (Retention/NRR, switching costs, market share, brand moat)<br>3. **Internal Execution & Product Velocity** (R&D efficiency, operational cadence, supply-chain resilience)<br>4. **Valuation & Risk Asymmetric Downside** (EV/FCF or P/E relative to growth, regulatory/concentration/disruption risk) |
| **Public Policies, Laws & Institutional Proposals** | **Eightfold Path Outcomes Matrix** — Eugene Bardach & Eric M. Patashnik (2023), *A Practical Guide for Policy Analysis: The Eightfold Path to More Effective Problem Solving* (Step 5: *Project the Outcomes*), CQ Press / SAGE. | 1. **Effectiveness** (Magnitude and certainty of solving the target problem)<br>2. **Efficiency & Cost-Effectiveness** (Cost per unit of outcome, fiscal/deadweight impact)<br>3. **Equity & Distributional Incidence** (Who bears the cost vs. who captures the benefit?)<br>4. **Administrative & Technical Feasibility** (Implementation complexity, enforcement capacity)<br>5. **Political/Legal Viability & Second-Order Unintended Consequences** (Goodhart/Cobra effects) |
| **Careers, Job Offers & Educational Paths** | **Risk-Adjusted Total Compensation + Career Capital Utility** (Keeney & Raiffa, 1976; BEA RPP adjustment). | 1. **Risk-Adjusted Real Compensation** (Base + expected bonus + probability-weighted liquid value of equity + benefits, divided by RPP & tax)<br>2. **Effective Hourly Rate & Work-Life Sustainability** (Net comp $\div$ realistic annual work + commute hours; on-call/burnout risk)<br>3. **Career Capital & Learning Velocity** (Skill compounding, mentorship, scope/autonomy)<br>4. **Company/Team Trajectory & Exit Optionality** (Manager quality, runway/stability, resume signaling value) |
| **Creative Works, Media, Courses & Books** | **Structural Craft vs. Audience-Fit Separation**. | 1. **Technical & Structural Execution** (Accuracy, depth, pacing, prose/production craft, pedagogical clarity)<br>2. **Originality & Signal-to-Noise Density** (Insights per hour/page vs. filler)<br>3. **Prerequisite & Audience Alignment** (Beginner vs. specialist fit, tonal/stylistic match, time commitment) |

---

## 4. Designing Fair Category-by-Category Scoring, Ties, and Overall Verdicts

### 4.1 MECE Criteria Generation & Preferential Independence (Avoiding Double-Counting)

- **Primary Source:** Ralph L. Keeney & Howard Raiffa (1976), *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*, Cambridge University Press ([DOI: 10.1017/CBO9781139174084](https://doi.org/10.1017/CBO9781139174084)).

A pervasive flaw in ad-hoc comparison tables is **collinear criterion inflation (double-counting)**: an agent creates 6 categories where 3 of them measure the same underlying property (e.g., comparing two cities on *"Rent Cost"*, *"Home Purchase Affordability"*, and *"Overall Cost of Living"*, or comparing two databases on *"Write Throughput"*, *"Ingestion Speed"*, and *"Scalability"*). This secretly triples the weight of that single dimension and rigs both the category win tally and the overall score.

- **The MECE & Preferential Independence Rule:**
  1. **Mutually Exclusive, Collectively Exhaustive (MECE):** Generate **4 to 7 categories** that partition the decision space cleanly without overlap.
  2. **Collinearity Merge Check:** Before scoring, check every pair of categories $(j, k)$: *"Does changing an entity's underlying physical/economic property automatically move its score in both Category $j$ and Category $k$?"* If yes, **merge them into a single category** with sub-metrics (e.g., merge *"Rent"*, *"Taxes"*, and *"Groceries"* into a single **"Total Cost of Living & Real Purchasing Power"** category) so each independent fundamental objective is counted exactly once.
  3. **Explicit Weights ($w_j$):** Assign explicit percentage weights summing to $100\%$ ($\sum_{j=1}^m w_j = 1.0$) grounded in the user's stated priorities (or domain-standard default weights if evaluating a general matchup).

### 4.2 The Mathematics and Epistemology of Ties (Indifference Zones)

In real-world comparisons, contenders are frequently **statistically or practically indistinguishable** on one or more categories. Forcing a winner in every category violates both measurement theory (Thurstone, 1927; Glickman, 1999) and outranking theory (Roy, 1968, 1991; Brans & Vincke, 1985).

- **Three Formal Conditions That Mandate a Category `Tie`:**

$$\text{Category Verdict}_j(A, B) = \texttt{Tie} \iff \begin{cases} 
1.\ \text{Practical Indifference:} & |g_j(A) - g_j(B)| \le q_j \\[4pt]
2.\ \text{Epistemic / Noise Overlap:} & |\hat{g}_j(A) - \hat{g}_j(B)| < 1.96 \sqrt{\text{SE}_A^2 + \text{SE}_B^2} \\[4pt]
3.\ \text{Internal Sub-Criterion Wash:} & \sum_{s \in j} w_{j,s} \Delta u_{j,s}(A, B) \in [-q_j, +q_j]
\end{cases}$$

1. **Condition 1 — Practical Indifference ($|\Delta g_j| \le q_j$):** The objective gap is smaller than the domain's **Indifference Threshold $q_j$** (Just Noticeable Difference in Separate Evaluation)—for example, a $<3\%$ difference in real TCO or salary, a $<5\%$ difference in synthetic benchmark score that disappears in real workloads, a $40\text{g}$ weight difference on a $15\text{ kg}$ bike, or a $2\text{-minute}$ commute difference.
2. **Condition 2 — Measurement Uncertainty / Epistemic Overlap:** The available evidence has error bars, sample variance, or source disagreement larger than the observed gap between the contenders (e.g., comparing reliability of two newly released products with no 12-month failure data, or comparing crime rates across two neighborhoods whose reporting boundaries differ).
3. **Condition 3 — Symmetric Internal Wash:** Within Category $j$, Contender A clearly wins sub-dimension $j_1$ while Contender B clearly wins equally important sub-dimension $j_2$ (e.g., under *"Healthcare & Wellness"*, City A has better hospital density while City B has markedly cleaner air and lower obesity/mortality rates), resulting in net category parity.

- **Standardized 3-Tier Category Outcome Scale (per Category $j$):**
  To prevent conflating razor-thin edges with blowouts, every category $j$ must be assigned one of three calibrated margin labels:
  - **`Decisive Win: [Entity]`** ($|\Delta g_j| \ge p_j$): Unmistakable, high-confidence advantage that materially changes lived experience, cost, or performance.
  - **`Narrow Edge: [Entity]`** ($q_j < |\Delta g_j| < p_j$): Real, verifiable advantage above the indifference threshold, but modest in magnitude or partially offset by secondary sub-factors.
  - **`Tie (Dead Heat / Wash)`** ($|\Delta g_j| \le q_j$ or epistemic/internal wash): Difference is negligible in separate evaluation, within measurement noise, or internally balanced out.

### 4.3 Aggregation Fallacies, Simpson's Paradox & Reconciling Category Tallies with Overall Verdicts

- **Primary Sources:**
  - Edward H. Simpson (1951), *"The Interpretation of Interaction in Contingency Tables"*, *Journal of the Royal Statistical Society: Series B (Methodological)*, Vol. 13, No. 2, pp. 238–241 ([DOI: 10.1111/j.2517-6161.1951.tb00088.x](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x)).
  - Kenneth J. Arrow (1951), *Social Choice and Individual Values*, Cowles Foundation Monograph No. 12, Wiley ([ISBN: 978-0300179729](https://cowles.yale.edu/publications/cfp/monograph-12)).

When aggregating category-level results into an **Overall Verdict**, three classic mathematical traps arise:

1. **The Raw Category-Count Fallacy (Unweighted Borda / Plurality Trap):**
   Suppose Contender A wins 3 categories by a `Narrow Edge` on low-weight criteria ($w_1 = w_2 = w_3 = 10\%$, margin $+1$ point each on a 10-point scale), while Contender B wins 2 categories by a `Decisive Win` on the two highest-weight criteria ($w_4 = 40\%, w_5 = 30\%$, margin $+4$ points each).
   - **Raw Category Tally:** A leads $3\text{–}2$ in category wins.
   - **Weighted Utility Differential:**
     $$\Delta U(B - A) = (0.40 \times 4 + 0.30 \times 4) - (0.10 \times 1 + 0.10 \times 1 + 0.10 \times 1) = +2.80 - 0.30 = +2.50\text{ points (on a 10-point scale)}$$
     Declaring A the overall winner because it won "3 categories to 2" is a mathematical error.
2. **Non-Compensatory Veto Override (Roy, 1991):**
   Even if Contender A leads in weighted additive utility $\sum w_j u_j$, if A violates a **Veto Threshold ($v_j$)** on a critical dimension (e.g., catastrophic security vulnerability, unaffordable cash-flow burn, or visa impossibility), A cannot be declared the unqualified overall winner.
3. **Simpson's Paradox in Pooled Metrics (Simpson, 1951):**
   An entity can have a higher *pooled* average (e.g., lower overall hospital mortality rate, higher overall batting average, or lower average API latency) while being **worse in every single subgroup** (low-risk vs. high-risk patients, fast-query vs. complex-query workloads) because its sample mix is skewed toward the easy subgroup. Always disaggregate by workload/segment before comparing averages.

- **The Dual-Accounting Aggregation Equation:**
  Every head-to-head comparison must compute and display **both** the **Category Win-Loss-Tie Record** and the **Weighted Composite Score ($U$)**:
  $$U(x_i) = \sum_{j=1}^{m} w_j u_j(x_{ij}) \in [0, 100] \quad (\text{or } [0.0, 10.0])$$
  subject to the non-compensatory veto indicator $\mathbb{I}_{\text{veto}}(x_i) = 0$. When a contender wins fewer raw categories (e.g., 2 wins vs. 3 wins) but wins the **Overall Verdict** due to higher category weights ($w_j$) or larger margin depth (`Decisive Win` vs. `Narrow Edge`), the agent must state this mathematical reconciliation explicitly in the verdict summary.

### 4.4 Calibrated 5-Level Overall Verdict Taxonomy & Reversal Conditions

To eliminate wishy-washy *"It depends"* conclusions while remaining epistemically honest when contenders genuinely split by user archetype or tie, a comparison skill should enforce a **5-Level Overall Verdict Taxonomy**:

| Overall Verdict Label | Mathematical & Decision Rule | Required Output in Report |
| :--- | :--- | :--- |
| **`Clear Overall Winner: [Entity X]`** | Passes all knockouts/vetoes; beats all rivals by a decisive weighted margin ($\Delta U \ge 8.0$ on a 100-point scale or $\ge 0.8$ on a 10-point scale); and remains #1 across reasonable weight sensitivity shifts. | Name `[Entity X]` unconditionally upfront, report the Category Win-Loss-Tie tally + Weighted Score ($U$), and summarize the decisive categories that drove the win. |
| **`Points / Edge Winner: [Entity X]`** | Passes all knockouts/vetoes and leads in weighted utility ($2.5 < \Delta U < 8.0$ on a 100-point scale) under the user's (or domain-default) weight profile, though the runner-up wins specific categories. | Name `[Entity X]` as the overall winner on points, state the exact category trade-off sacrificed, and show how close the runner-up finished. |
| **`Split Verdict (Profile-Dependent)`** | No single option dominates across standard profiles because Contender A wins decisively on High-Weight Axis 1 while Contender B wins decisively on High-Weight Axis 2, flipping the sign of $\Delta U$ across major user archetypes. | State the **Default Pick** (if one profile is more common) **plus explicit if-then winner rules**: *"Winner for [Profile A]: Entity X; Winner for [Profile B]: Entity Y"* with exact numerical criteria. |
| **`Overall Tie (Dead Heat)`** | Weighted utilities lie inside the overall indifference zone ($|\Delta U| \le 2.5$ on a 100-point scale / $\le 0.25$ on a 10-point scale) and category wins/margins cancel out symmetrically. | Declare an explicit **`Overall Tie`**, explain why forcing a winner would rely on Distinction Bias noise, and provide the **1-Step Tiebreaker Rule** (e.g., pick whichever has the lower street price today, shorter commute, or existing team familiarity). |
| **`Disqualified / Pivot to [Entity Z]`** | All compared contenders fail a hard knockout/veto constraint ($v_j$), OR both are strictly dominated by a well-known third benchmark $[Entity Z]$ that solves the user's objective far better. | Explain the exact knockout failure or dominance gap and compare the surviving contender against $[Entity Z]$. |

> **Mandatory Reversal Conditions ("What Flips This Matchup?"):** Every comparison report must conclude with concrete, falsifiable **Crossover Thresholds**—the exact weight shift ($w_j^*$) or metric delta ($\Delta x_j^*$) where the runner-up overtakes the winner:
> $$\text{Crossover Condition: } U(B) > U(A) \iff w_k > w_k^* \quad \text{or} \quad x_{B,k} \ge x_{B,k}^*$$
> *(Example: "Contender B overtakes Contender A overall if: (1) you weight Portability above 35%, (2) Contender B's street price drops below \$1,150, or (3) your query workload exceeds 20% multi-table joins.")*

---

## 5. Skill Naming Analysis, Boundary with `should-i-buy`, & Workflow Blueprint

### 5.1 Skill Naming Evaluation Against `writing-for-agents` Principles

Per `writing-for-agents` (`~/.gemini/config/skills/writing-for-agents/SKILL.md`):
- The skill name acts simultaneously as the **human slash command** (`/skill-name`) and the **model-invoked leading word** in the system prompt discovery list.
- It must be concise, natural to type with arguments (`/compare X vs Y`), universally applicable across **non-shopping and shopping domains alike** (places, people, technologies, companies, careers, policies, creative works, products), and clearly distinct from `should-i-buy`.

| Candidate Name | Slash-Command Ergonomics | Pretraining Leading-Word Alignment | Universal Entity Coverage (Places, People, Tech, Policies, Products) | Boundary Clarity vs. `should-i-buy` |
| :--- | :--- | :--- | :--- | :--- |
| **`compare`** | `/compare [A vs B]` (7 chars, 0 hyphens) | **Highest.** `"compare"` is the #1 canonical verb humans and models use across every domain (*"Compare X and Y"*, *"Compare Austin vs Denver"*, *"Compare Postgres vs Mongo"*). | **100% Universal.** Equally natural for historical figures, cities, software architectures, job offers, public policies, and hardware. | **Very High.** `compare` = horizontal A-vs-B evaluation; `should-i-buy` = vertical financial purchase gate. |
| **`head-to-head`** | `/head-to-head [A vs B]` (12 chars, 2 hyphens) | **Very High.** Immediately primes rigorous toe-to-toe category scoring, round-by-round winners/ties, and a decisive final verdict rather than a passive summary. | **Very High.** Strong for athletes, candidates, products, cities, and technologies; slightly idiomatic for policies/careers. | **High.** Clearly signals a direct matchup between contenders. |
| **`versus`** | `/versus [A vs B]` (6 chars, 0 hyphens) | **High.** Mirrors the universal `"X vs Y"` token present in comparative queries. | **Very High.** Works across sports, history, tech, cities, and products. | **High.** However, `/versus A vs B` repeats `"vs"` in the slash invocation, making `/compare A vs B` cleaner to type. |
| **`side-by-side`** | `/side-by-side [A vs B]` (12 chars, 2 hyphens) | **Medium-High.** Recruits tabular alignment priors, which can inadvertently encourage passive spec-table generation without a decisive winner unless overridden. | **High.** Natural for documents, specs, cities, and plans; less natural for historical figures or athletes. | **High.** Focuses on layout/juxtaposition rather than adjudication. |
| **`matchup`** | `/matchup [A vs B]` (7 chars, 0 hyphens) | **Medium.** Strongly associated with sports, gaming, and combat brackets in pretraining corpora. | **Medium.** Feels unnatural for public policies, job offers, or architectural trade-offs. | **High.** Distinct from buying, but domain-skewed toward sports/games. |
| **`toe-to-toe`** | `/toe-to-toe [A vs B]` (10 chars, 2 hyphens) | **Medium.** Vivid boxing metaphor for direct confrontation, but rarely typed verbatim by users in search or chat prompts. | **Medium.** Idiomatic rather than a direct verb command. | **High.** Best used as descriptive phrasing inside the skill rather than the slash command name. |

#### Naming Recommendation
- **Primary Recommendation:** **`compare`** (with **"Head-to-Head Comparison"** as the display name and in-file framing).
  - `/compare` is 7 characters, zero hyphens, effortless to type as `/compare Postgres vs DynamoDB` or `/compare Tokyo vs London`, matches the exact verb token users speak across every domain, and pairs with `/fact-check` and `/should-i-buy` to form a cohesive 3-skill epistemic & decision suite in `ej-skills`:
    - **`fact-check`**: *Is this claim true?* (Epistemic verification against primary sources)
    - **`should-i-buy`**: *Should I spend money on X at all?* (Vertical capital-allocation, TCO, CPU, and anti-impulse gate)
    - **`compare`**: *Between A, B, and C, how do they stack up category-by-category and which wins overall?* (Horizontal multi-entity MCDA, category winners/ties, and overall verdict across any entity type)

### 5.2 Architectural Boundary & Inter-Skill Routing with `should-i-buy`

| Dimension | `compare` (Horizontal Multi-Entity Matchup) | `should-i-buy` (Vertical Capital & Purchase Gate) |
| :--- | :--- | :--- |
| **Core Question** | *"Between Contender A and Contender B (and C), which wins each category, where do they tie, and which wins overall?"* | *"Should I part with my money for X, or keep cash / repair / rent / wait?"* |
| **Entity Scope** | **Universal:** Places (cities/neighborhoods), People (candidates/athletes/historical figures), Tech/Architectures, Companies, Careers/Job Offers, Policies, Creative Works, and Products. | **Financial & Purchase Commitments:** Physical goods, subscriptions, vehicles, real estate, B2B SaaS, courses, and paid experiences. |
| **Primary Analytical Engine** | MECE category generation, domain normalization (PPP/RPP, era Z-scores, GeoMean benchmarks), PROMETHEE indifference/preference/veto thresholds ($q_j, p_j, v_j$), Non-Alignable audit, Separate-Evaluation translation, Category Win-Loss-Tie tallies, and Weighted Utility ($U$). | Value-Focused Thinking, Non-Purchase Baselines (`Keep Current`, `Repair`, `Rent`, `Wait`), 7-bucket TCO, 50%-deflated CPU/CPH, Break-Even ($N^*$), Opportunity Cost, Diderot Spiral, and 12-Month Premortem. |
| **Cross-Skill Routing Rule** | When comparing purchasable products, `compare` includes a **TCO & Value** category; if the user then asks whether the winning product is worth buying over keeping their current setup or cash, route to `should-i-buy`. | When `should-i-buy` concludes `Buy Alternative Instead` and the user wants a deep category-by-category breakdown of 3+ competing models, route to `compare`. |

### 5.3 Blueprint: 6-Step Universal Head-to-Head Comparison Protocol

Synthesizing all five research traditions, the skill should enforce a sequential **6-Step Comparison Protocol** where every step has a checkable completion criterion:

1. **Frame Contenders, Entity Class & Context Gate (Keeney + Pu & Chen + Pratkanis & Farquhar):**
   - Identify the **Contenders** ($A, B, [C \dots]$), the **Entity Class** (Places, People/Candidates, Athletes/Historical Figures, Tech/Software/Architectures, Companies/Investments, Careers/Job Offers, Policies, Creative Works, or Products/Services), and the **Decision Context / Use Case**.
   - Check for **knockout constraints** (Tversky EBA), **dominated decoys** (Huber et al., 1982), and **unavailable phantoms** (Pratkanis & Farquhar, 1992).
   - **Adaptive Context Gate:** If the comparison outcome depends heavily on 1–3 missing user parameters (e.g., workload scale for databases, income/family size for cities, risk tolerance/role level for job offers) and the user has not asked for an immediate general comparison, ask **2 to 3 concise, high-information-gain questions**; otherwise state explicit default profile assumptions and proceed.
   - *Completion Criterion:* Contenders, entity domain, active use-case profile, and hard knockout constraints are explicitly established.
2. **Generate MECE Categories, Weights & Thresholds (Keeney & Raiffa + Saaty AHP + Roy PROMETHEE):**
   - Construct **4 to 7 Mutually Exclusive, Collectively Exhaustive (MECE) categories** tailored to the entity domain (merging any collinear criteria to prevent double-counting).
   - Assign explicit **Category Weights ($w_j$)** summing to $100\%$ ($\sum w_j = 100\%$).
   - Define the **Indifference Threshold ($q_j$)** (what constitutes a `Tie`), **Strict Preference Threshold ($p_j$)** (what constitutes a `Decisive Win`), and any **Non-Compensatory Veto ($v_j$)** for each category.
   - *Completion Criterion:* 4–7 non-overlapping categories with weights summing to $100\%$ and explicit tie/win thresholds are defined.
3. **Symmetric Primary-Source Verification & Domain Normalization (Wineburg + FacTool + Domain Playbooks):**
   - Execute **symmetric retrieval** across all contenders (never relying on one contender's marketing or asymmetric documentation volume).
   - Apply mandatory **domain normalization**:
     - *Places:* PPP/RPP & tax-adjusted real disposable surplus, neighborhood-level safety/transit, comfortable climate days.
     - *People (Candidates):* BARS evidence mapping against job competencies.
     - *People (Athletes/Historical):* Era-adjusted Z-scores ($Z_{\text{era}}$), replacement-level value (WAR), Peak vs. Longevity (JAWS).
     - *Tech/Architectures:* ISO/IEC 25010 characteristics, ATAM concrete scenarios, and **Geometric Mean** ($\text{GeoMean}$) of normalized benchmark ratios.
     - *Products/Services:* Full-lifecycle TCO, independent instrumental testing (Experience attributes), and 1-to-3 star failure clusters.
   - *Completion Criterion:* Every contender is evaluated using symmetric, session-verified primary/independent evidence normalized to commensurate units.
4. **Horizontal Category-by-Category Evaluation & Indifference-Zone Scoring (Thorndike + Hsee + Brans & Vincke):**
   - Score **one category at a time across all contenders horizontally** (preventing Thorndike Halo carryover).
   - Apply Hsee's **Separate-Evaluation Translation Test** to strip Distinction Bias: if a raw numerical difference would not be noticed or felt 6 months later in separate lived experience ($|\Delta g_j| \le q_j$), declare a **`Tie`**.
   - Assign each category a calibrated verdict: **`Decisive Win: [Entity]`**, **`Narrow Edge: [Entity]`**, or **`Tie (Dead Heat / Wash)`**, plus a $0\text{–}10$ score per contender.
   - *Completion Criterion:* Every category has verified metrics, a Separate-Evaluation reality check, a $0\text{–}10$ score per contender, and an explicit `Decisive Win`, `Narrow Edge`, or `Tie` call.
5. **Non-Alignable Differentiator Audit & Order-Swap Debiasing (Gentner & Markman + Zheng et al. + Wang et al.):**
   - Surface **Non-Alignable Differences** (unique capabilities, structural paradigms, cultural realities, or asymmetric tail risks that do not fit into symmetric spec columns).
   - Run the **Order-Swap Invariance Check** ($f(A, B) \equiv f(B, A)$) and **Even Swap Trade-Off Translation** (Hammond et al., 1998) on the core trade-off between the top two contenders.
   - *Completion Criterion:* Non-alignable differentiators are explicitly analyzed, and order-swap invariance is verified.
6. **Dual-Accounting Aggregation, Overall Verdict & Reversal Conditions:**
   - Compute both the **Category Win-Loss-Tie Tally** (breaking down Decisive vs. Narrow wins) and the **Weighted Composite Score ($U(x_i) = \sum w_j u_j(x_{ij})$ out of 100 or 10.0)**, checking for any non-compensatory **Veto ($v_j$)** violations.
   - Reconcile any divergence between raw category win count and weighted utility.
   - Assign one of the 5 calibrated Overall Verdicts: **`Clear Overall Winner: [Entity]`**, **`Points / Edge Winner: [Entity]`**, **`Split Verdict (Profile-Dependent)`**, **`Overall Tie (Dead Heat)`**, or **`Disqualified / Pivot to [Entity Z]`**.
   - State explicit, falsifiable **Reversal / Crossover Conditions** (*"What would flip this matchup?"*).
   - *Completion Criterion:* The report presents the Overall Verdict, Dual-Accounting Scoreboard (Category Tally + Weighted Score), Category-by-Category Breakdown, Non-Alignable Trade-offs, Winner by User Profile, and exact Crossover Conditions.

---

## References & Primary Sources

1. **Saaty, T. L. (1977):** *"A scaling method for priorities in hierarchical structures"*, *Journal of Mathematical Psychology*, 15(3), 234–281. [https://doi.org/10.1016/0022-2496(77)90033-5](https://doi.org/10.1016/0022-2496(77)90033-5)
2. **Saaty, T. L. (1990):** *"How to make a decision: The Analytic Hierarchy Process"*, *European Journal of Operational Research*, 48(1), 9–26. [https://doi.org/10.1016/0377-2217(90)90057-I](https://doi.org/10.1016/0377-2217(90)90057-I)
3. **Belton, V., & Gear, T. (1983):** *"On a short-coming of Saaty's method of analytic hierarchies"*, *Omega*, 11(3), 228–230. [https://doi.org/10.1016/0305-0483(83)90047-6](https://doi.org/10.1016/0305-0483(83)90047-6)
4. **Dyer, J. S. (1990):** *"Remarks on the Analytic Hierarchy Process"*, *Management Science*, 36(3), 249–258. [https://doi.org/10.1287/mnsc.36.3.249](https://doi.org/10.1287/mnsc.36.3.249)
5. **Hwang, C.-L., & Yoon, K. (1981):** *Multiple Attribute Decision Making: Methods and Applications — A State-of-the-Art Survey*, Lecture Notes in Economics and Mathematical Systems, Vol. 186, Springer-Verlag. [https://doi.org/10.1007/978-3-642-48318-9](https://doi.org/10.1007/978-3-642-48318-9)
6. **Roy, B. (1968):** *"Classement et choix en présence de points de vue multiples (la méthode ELECTRE)"*, *Revue Française d'Informatique et de Recherche Opérationnelle (RIRO)*, 2(V1), 57–75. [https://doi.org/10.1051/ro/196802V100571](https://doi.org/10.1051/ro/196802V100571)
7. **Roy, B. (1991):** *"The outranking approach and the foundations of ELECTRE methods"*, *Theory and Decision*, 31(1), 49–73. [https://doi.org/10.1007/BF00134132](https://doi.org/10.1007/BF00134132)
8. **Brans, J.-P., & Vincke, P. (1985):** *"Note—A Preference Ranking Organisation Method: (The PROMETHEE Method for Multiple Criteria Decision-Making)"*, *Management Science*, 31(6), 647–656. [https://doi.org/10.1287/mnsc.31.6.647](https://doi.org/10.1287/mnsc.31.6.647)
9. **Tversky, A. (1972):** *"Elimination by aspects: A theory of choice"*, *Psychological Review*, 79(4), 281–299. [https://doi.org/10.1037/h0032955](https://doi.org/10.1037/h0032955)
10. **Keeney, R. L., & Raiffa, H. (1976):** *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*, Wiley / Cambridge University Press. [https://doi.org/10.1017/CBO9781139174084](https://doi.org/10.1017/CBO9781139174084)
11. **Hammond, J. S., Keeney, R. L., & Raiffa, H. (1998):** *"Even Swaps: A Rational Method for Making Trade-Offs"*, *Harvard Business Review*, 76(2), 137–149. [https://www.hbs.edu/faculty/Pages/item.aspx?num=3991](https://www.hbs.edu/faculty/Pages/item.aspx?num=3991)
12. **Gentner, D., & Markman, A. B. (1994):** *"Structural Alignment in Comparison: No Difference Without Similarity"*, *Psychological Science*, 5(3), 152–158. [https://doi.org/10.1111/j.1467-9280.1994.tb00652.x](https://doi.org/10.1111/j.1467-9280.1994.tb00652.x)
13. **Gentner, D., & Markman, A. B. (1997):** *"Structure Mapping in Analogy and Similarity"*, *American Psychologist*, 52(1), 45–56. [https://doi.org/10.1037/0003-066X.52.1.45](https://doi.org/10.1037/0003-066X.52.1.45)
14. **Markman, A. B., & Medin, D. L. (1995):** *"Similarity and Alignment in Choice"*, *Organizational Behavior and Human Decision Processes*, 63(2), 117–130. [https://doi.org/10.1006/obhd.1995.1067](https://doi.org/10.1006/obhd.1995.1067)
15. **Medin, D. L., Goldstone, R. L., & Markman, A. B. (1995):** *"Comparison and Choice: Relations between Similarity Processes and Decision Processes"*, *Psychonomic Bulletin & Review*, 2(1), 1–19. [https://doi.org/10.3758/BF03214410](https://doi.org/10.3758/BF03214410)
16. **Zhang, S., & Markman, A. B. (1998):** *"Overcoming the Early Entrant Advantage: The Role of Alignable and Nonalignable Differences"*, *Journal of Marketing Research*, 35(4), 413–426. [https://doi.org/10.1177/002224379803500401](https://doi.org/10.1177/002224379803500401)
17. **Hsee, C. K. (1996):** *"The Evaluability Hypothesis: An Explanation for Preference Reversals between Joint and Separate Evaluations of Alternatives"*, *Organizational Behavior and Human Decision Processes*, 67(3), 247–257. [https://doi.org/10.1006/obhd.1996.0077](https://doi.org/10.1006/obhd.1996.0077)
18. **Hsee, C. K., Loewenstein, G. F., Blount, S., & Bazerman, M. H. (1999):** *"Preference reversals between joint and separate evaluations of options: A review and theoretical analysis"*, *Psychological Bulletin*, 125(5), 576–590. [https://doi.org/10.1037/0033-2909.125.5.576](https://doi.org/10.1037/0033-2909.125.5.576)
19. **Hsee, C. K., & Zhang, J. (2004):** *"Distinction bias: Misprediction and mischoice due to joint evaluation"*, *Journal of Personality and Social Psychology*, 86(5), 680–695. [https://doi.org/10.1037/0022-3514.86.5.680](https://doi.org/10.1037/0022-3514.86.5.680)
20. **Hsee, C. K., & Zhang, J. (2010):** *"General Evaluability Theory"*, *Perspectives on Psychological Science*, 5(4), 343–355. [https://doi.org/10.1177/1745691610374586](https://doi.org/10.1177/1745691610374586)
21. **Huber, J., Payne, J. W., & Puto, C. (1982):** *"Adding Asymmetrically Dominated Alternatives: Violations of Regularity and the Similarity Hypothesis"*, *Journal of Consumer Research*, 9(1), 90–98. [https://doi.org/10.1086/208899](https://doi.org/10.1086/208899)
22. **Simonson, I. (1989):** *"Choice Based on Reasons: The Case of Attraction and Compromise Effects"*, *Journal of Consumer Research*, 16(2), 158–174. [https://doi.org/10.1086/209205](https://doi.org/10.1086/209205)
23. **Pratkanis, A. R., & Farquhar, P. H. (1992):** *"A Brief History of Research on Phantom Alternatives: Evidence for Seven Empirical Generalizations About Phantoms"*, *Basic and Applied Social Psychology*, 13(1), 103–122. [https://doi.org/10.1207/s15324834basp1301_9](https://doi.org/10.1207/s15324834basp1301_9)
24. **Thurstone, L. L. (1927):** *"A law of comparative judgment"*, *Psychological Review*, 34(4), 273–286. [https://doi.org/10.1037/h0070288](https://doi.org/10.1037/h0070288)
25. **Bradley, R. A., & Terry, M. E. (1952):** *"Rank Analysis of Incomplete Block Designs: I. The Method of Paired Comparisons"*, *Biometrika*, 39(3/4), 324–345. [https://doi.org/10.1093/biomet/39.3-4.324](https://doi.org/10.1093/biomet/39.3-4.324)
26. **Glickman, M. E. (1999):** *"Parameter estimation in large dynamic paired comparison experiments"*, *Journal of the Royal Statistical Society: Series C (Applied Statistics)*, 48(3), 377–394. [https://doi.org/10.1111/1467-9876.00159](https://doi.org/10.1111/1467-9876.00159)
27. **Thorndike, E. L. (1920):** *"A constant error in psychological ratings"*, *Journal of Applied Psychology*, 4(1), 25–29. [https://doi.org/10.1037/h0071663](https://doi.org/10.1037/h0071663)
28. **Zheng, L., et al. (2023):** *"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"*, *NeurIPS 2023*. [https://arxiv.org/abs/2306.05685](https://arxiv.org/abs/2306.05685)
29. **Wang, P., et al. (2023):** *"Large Language Models are not Fair Evaluators"*, *ACL 2024*. [https://arxiv.org/abs/2305.17926](https://arxiv.org/abs/2305.17926)
30. **Schmidt, F. L., & Hunter, J. E. (1998):** *"The validity and utility of selection methods in personnel psychology: Practical and theoretical implications of 85 years of research findings"*, *Psychological Bulletin*, 124(2), 262–274. [https://doi.org/10.1037/0033-2909.124.2.262](https://doi.org/10.1037/0033-2909.124.2.262)
31. **Sackett, P. R., Zhang, C., Berry, C. M., & Lievens, F. (2022):** *"Revisiting meta-analytic estimates of validity in personnel selection: Addressing systematic overcorrection for restriction of range"*, *Journal of Applied Psychology*, 107(11), 2040–2068. [https://doi.org/10.1037/apl0000994](https://doi.org/10.1037/apl0000994)
32. **Smith, P. C., & Kendall, L. M. (1963):** *"Retranslation of expectations: An approach to the construction of unambiguous anchors for rating scales"* (BARS), *Journal of Applied Psychology*, 47(2), 149–155. [https://doi.org/10.1037/h0047060](https://doi.org/10.1037/h0047060)
33. **Gould, S. J. (1996):** *Full House: The Spread of Excellence from Plato to Darwin*, Harmony Books.
34. **Jaffe, J. (2004, 2017):** *Jaffe WAR Score System (JAWS)*, Baseball-Reference. [https://www.baseball-reference.com/about/jaws.shtml](https://www.baseball-reference.com/about/jaws.shtml)
35. **ISO/IEC 25010:2023:** *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*. [https://www.iso.org/standard/78176.html](https://www.iso.org/standard/78176.html)
36. **Kazman, R., Klein, M., & Clements, P. (2000):** *ATAM: Method for Architecture Evaluation*, Technical Report CMU/SEI-2000-TR-004, Software Engineering Institute, Carnegie Mellon University. [https://insights.sei.cmu.edu/library/atam-method-for-architecture-evaluation/](https://insights.sei.cmu.edu/library/atam-method-for-architecture-evaluation/)
37. **Fleming, P. J., & Wallace, J. J. (1986):** *"How not to lie with statistics: The correct way to summarize benchmark results"*, *Communications of the ACM*, 29(3), 218–221. [https://doi.org/10.1145/5666.5673](https://doi.org/10.1145/5666.5673)
38. **Kaplan, R. S., & Norton, D. P. (1992):** *"The Balanced Scorecard—Measures That Drive Performance"*, *Harvard Business Review*, 70(1), 71–79. [https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2](https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2)
39. **Bardach, E., & Patashnik, E. M. (2023):** *A Practical Guide for Policy Analysis: The Eightfold Path to More Effective Problem Solving*, CQ Press / SAGE.
40. **OECD Better Life Index & U.S. BEA Regional Price Parities (RPPs):** [https://www.oecd.org/en/data/tools/oecd-better-life-index.html](https://www.oecd.org/en/data/tools/oecd-better-life-index.html) | [https://www.bea.gov/data/prices-inflation/regional-price-parities-state-and-metro-area](https://www.bea.gov/data/prices-inflation/regional-price-parities-state-and-metro-area)
41. **Simpson, E. H. (1951):** *"The Interpretation of Interaction in Contingency Tables"*, *Journal of the Royal Statistical Society: Series B (Methodological)*, 13(2), 238–241. [https://doi.org/10.1111/j.2517-6161.1951.tb00088.x](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x)
42. **Arrow, K. J. (1951):** *Social Choice and Individual Values*, Cowles Foundation Monograph No. 12, Wiley. [https://cowles.yale.edu/publications/cfp/monograph-12](https://cowles.yale.edu/publications/cfp/monograph-12)
