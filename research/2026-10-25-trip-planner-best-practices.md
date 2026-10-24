# Travel & Itinerary Planning Skill Best Practices: Primary-Source Synthesis

**Date:** 2026-10-25  
**Repository:** `ej-skills`  
**Scope:** Spatio-temporal constraint modeling and operations research for itineraries, multimodal door-to-door transit math and connection risk engineering, cognitive load and circadian physiology, consular/border and environmental hard gates, information economics of anti-tourist-trap vetting and hospitality drip pricing, conversational preference elicitation, and cross-platform AI skill design.

---

## Executive Summary

When a human asks an AI assistant *"Plan a 7-day trip to Japan"*, *"Review my Italy itinerary"*, or *"Should I stay in Shinjuku or Asakusa?"*, default LLM behavior suffers from **brochure hallucination**, **teleportation scheduling**, and **tourist-trap recitation**: the model packs 5–6 geographically scattered attractions into a single day, quotes idealized in-vehicle transit times while ignoring access/security/transfer buffers, schedules museums on their weekly closing days, recommends SEO-inflated tourist traps, and omits border entry gates or misconnection risks.

Empirical evaluations of language agents on realistic travel benchmarks confirm that unconstrained LLM itinerary generation is systematically broken. On the **ICML 2024 TravelPlanner benchmark** (Xie et al., 2024), across 1,225 multi-constraint travel planning queries with access to search and database tools, baseline **GPT-3.5-Turbo and GPT-4 achieved a 0.6% final pass rate**, and **GPT-4-Turbo reached only 4.4%**—failing predominantly due to ignored opening hours/time windows, spatial oscillation, hallucinated transit legs, budget overruns, and dropped hard constraints.

Building a rigorous, stress-tested **Travel & Itinerary Planning Skill (`trip-planner`)**—capable of planning or auditing everything from a weekend city break or multi-country rail itinerary to a family road trip, high-altitude trek, or complex international trip—requires synthesizing six primary research traditions:

1. **Spatio-Temporal Constraint Modeling & Operations Research:** Torsten Hägerstrand's **Time-Geography** and **Space-Time Prism** (1970) (Capability, Coupling, and Authority constraints); the **Tourist Trip Design Problem (TTDP)** and **Team Orienteering Problem with Time Windows (TOPTW)** (Vansteenwegen & Van Oudheusden, 2007; Vansteenwegen et al., 2011; Gavalas et al., 2014); and structural guardrails against the failure modes documented in **TravelPlanner** (Xie et al., 2024).
2. **Door-to-Door Transit Math, Buffer Sizing & Connection Risk Engineering:** Full multimodal **Door-to-Door ($T_{\text{D2D}}$) decomposition** and **Perceived Travel Time / Transfer Penalty multipliers** from the Transportation Research Board's **TCRP Report 165** (2013) and Mark Wardman (2001, 2004); **Planning Fallacy** debiasing via outside-view buffer sizing (Kahneman & Tversky, 1979; Buehler, Griffin, & Ross, 1994); and aviation/rail connection protection under **IATA Resolution 765 Minimum Connecting Time (MCT)**, **EU Regulation (EC) No 261/2004**, and the **US DOT Automatic Refund Rule (14 CFR Part 260, 2024)**.
3. **Cognitive Load, Museum/Walking Fatigue, Circadian Physiology & Daily Pacing:** Barbara Fredrickson & Daniel Kahneman's **Peak-End Rule & Duration Neglect** (1993) and Kemp, Burt, & Furneaux's (2008) empirical validation on vacations; **Museum Fatigue** and **Directed Attention Fatigue** (Gilman, 1916; Melton, 1935; Bitgood, 2009) paired with Stephen Kaplan's **Attention Restoration Theory (ART)** (1995) to enforce a strict **1 Anchor Activity + 1 Flexible Option per half-day** cap; and **circadian resynchronization math** (Waterhouse et al., 2007, *The Lancet*; CDC Yellow Book).
4. **Logistics & Entry Gate (Authority, Calendar & Environmental Constraints):** Hard-knockout pre-trip checks grounded in **IATA Timatic**, **Schengen Borders Code Regulation (EU) 2016/399 Article 6** (the dual 10-year issue date + 3-month post-departure rule), passport blank-page and 6-month rules, **ESTA / ETIAS / e-Visa** lead times, **1949 Geneva vs. 1968 Vienna IDP Conventions**, **WHO International Health Regulations (IHR)** & strict national medication import prohibitions, **CDC Yellow Book high-altitude acclimatization thresholds ($>2,500\text{ m}$)**, and local holiday/strike/weekly closure matrices.
5. **Information Economics of Anti-Tourist-Trap Vetting & Hospitality Comparison:** Dean MacCannell's **"Staged Authenticity"** (1973) and George Akerlof's **"Market for Lemons"** (1970) applied to zero-repeat-customer tourist zones; promotional review distortion (Mayzlin, Dover, & Chevalier, 2014; **FTC 16 CFR Part 255 & Part 465**) defeated by cross-checking native regional culinary/local directories; and **True Location-Adjusted Nightly Cost** incorporating **drip pricing** defenses (**FTC 16 CFR Part 464**, 2024/2025; Santana, Dallas, & Morwitz, 2020).
6. **Interactive Context Elicitation, Premortem Stress-Testing & Calibrated Readiness Verdicts:** High-information-gain preference elicitation on verdict-flipping travel variables (Pu & Chen, 2008, 2012), Gary Klein's **Project Premortem** (2007) applied to travel failure modes, an optional persistent traveler profile (`.agents/traveler-profile.md`), and a 6-level **Itinerary Readiness Verdict Taxonomy**.

---

## 1. Spatio-Temporal Constraint Modeling & Operations Research for Itineraries

### 1.1 Hägerstrand's Time-Geography & The Space-Time Prism (Hägerstrand, 1970)

Most travel planning failures begin by treating a destination as an unordered wishlist of attractions rather than a continuous trajectory through space and time. Regional scientist Torsten Hägerstrand (1970) established **Time-Geography**, proving that human movement in physical space is governed by an indivisible **Space-Time Path** bounded by a **Space-Time Prism**.

- **Primary Source:**
  - Torsten Hägerstrand (1970), *"What about people in Regional Science?"*, *Papers of the Regional Science Association*, Vol. 24, No. 1, pp. 6–21 ([DOI: 10.1007/BF01936872](https://doi.org/10.1007/BF01936872) | [Wiley DOI: 10.1111/j.1435-5597.1970.tb01464.x](https://doi.org/10.1111/j.1435-5597.1970.tb01464.x)).

Hägerstrand categorizes all real-world movement restrictions into three non-negotiable constraint classes that an AI trip planner must enforce before scoring any attraction:

| Constraint Class | Hägerstrand's Definition (1970) | Travel & Itinerary Realization | Agentic Enforcement Rule |
| :--- | :--- | :--- | :--- |
| **1. Capability Constraints** | Biological and physical limits of the human body and the maximum speed/reach of available transport modes. | Circadian sleep need (7–8 hrs), meal intervals, daily walking ceiling (km/steps), heat/altitude tolerance, stroller/wheelchair accessibility, and luggage hauling limits. | Never schedule activities during biological recovery windows; bound daily walking distance and stair/elevation load to the lowest-mobility member of the travel party. |
| **2. Coupling Constraints** | Requirements that an individual, tools/tickets, and other people be at the same spatial location $(x,y)$ during the same time interval $[t_a, t_b]$. | Fixed flight/train departure times, timed-entry museum slots, ferry timetables, tour group departure windows, check-in/check-out cutoffs, and dining reservations. | Treat every coupled event as a **fixed spatio-temporal anchor** $(x_i, y_i, [t_{\text{start}}, t_{\text{end}}])$ that truncates the remaining Space-Time Prism for that half-day. |
| **3. Authority Constraints** | Legal, institutional, or proprietor rules controlling who may access a spatial domain and when. | Border visa/passport rules, opening/closing hours, weekly museum closure days, last-entry cutoffs (often 30–60 min before closing), dress codes, ZTL driving zones, and advance-lottery permits. | Verify exact operating hours, seasonal schedules, weekly closure days, and permit/visa requirements before placing any Point of Interest (POI) on a day's schedule. |

#### The Potential Path Area (PPA) & Space-Time Prism Inequality
If a traveler must be at Anchor Location $A$ at time $t_1$ (e.g., hotel checkout or morning train arrival) and at Anchor Location $B$ by time $t_2$ (e.g., timed museum entry or departing flight check-in), an intermediate Point of Interest $k$ with minimum meaningful dwell time $d_k$ is physically feasible **if and only if**:

$$t_1 + T_{\text{D2D}}(A, k) + d_k + T_{\text{D2D}}(k, B) \le t_2$$

When $t_2 - t_1$ shrinks, the **Potential Path Area (PPA)**—the geographic ellipse of reachable stops—collapses. Any stop $k$ violating this inequality is mathematically impossible without cutting dwell time $d_k$ below the threshold of a meaningful visit or missing Anchor $B$.

### 1.2 The Tourist Trip Design Problem (TTDP) & Team Orienteering Problem with Time Windows (TOPTW)

In Operations Research, itinerary construction is formalized as the **Tourist Trip Design Problem (TTDP)**, which generalizes the **Orienteering Problem with Time Windows (OPTW)** and **Team Orienteering Problem with Time Windows (TOPTW)**.

- **Primary Sources:**
  - Pieter Vansteenwegen & Dirk Van Oudheusden (2007), *"The Mobile Tourist Guide: An OR Opportunity"*, *OR Insight*, Vol. 20, No. 3, pp. 21–27 ([DOI: 10.1057/ori.2007.17](https://doi.org/10.1057/ori.2007.17)).
  - Pieter Vansteenwegen, Wouter Souffriau, & Dirk Van Oudheusden (2011), *"The orienteering problem: A survey"*, *European Journal of Operational Research*, Vol. 209, No. 1, pp. 1–10 ([DOI: 10.1016/j.ejor.2010.03.045](https://doi.org/10.1016/j.ejor.2010.03.045)).
  - Damianos Gavalas, Charalampos Konstantopoulos, Konstantinos Mastakas, & Grammati Pantziou (2014), *"A survey on algorithmic approaches for solving tourist trip design problems"*, *Journal of Heuristics*, Vol. 20, No. 3, pp. 291–328 ([DOI: 10.1007/s10732-014-9242-5](https://doi.org/10.1007/s10732-014-9242-5)).

#### Mathematical Formulation of TOPTW for Multi-Day Itineraries
Unlike the Traveling Salesman Problem (TSP)—which assumes the traveler *must* visit every node—the **TOPTW** recognizes that time and energy budgets are strictly finite ($M$ days/half-days, each bounded by time budget $T_{\max, m}$), so the planner must **select a subset of nodes** and **sequence them spatially** to maximize net experiential utility without violating any time window:

$$\max \sum_{m=1}^{M} \sum_{i=2}^{N-1} S_i y_{im} - \lambda \sum_{m=1}^{M} \sum_{i=1}^{N} \sum_{j=1}^{N} C_{\text{generalized}}(i, j) x_{ijm}$$

subject to:
1. **Visit Uniqueness:** $\sum_{m=1}^{M} y_{im} \le 1$ (each POI $i$ is visited at most once, unless it is the home base hotel).
2. **Time-Window Feasibility (Opening & Last-Entry Bounds):** For every visited POI $i$ on day $m$, arrival time $a_{im}$ and service start time $s_{im}$ must satisfy:
   $$O_{im} \le s_{im} \le L_{im} \le C_{im} - d_i$$
   where $[O_{im}, C_{im}]$ is the operating window on day-of-week $m$, $L_{im}$ is the mandatory **last-admission cutoff**, and $d_i$ is the realistic visit duration.
3. **Waiting-Time Absorption:** If the traveler arrives before opening ($a_{im} < O_{im}$), waiting time $w_{im} = O_{im} - a_{im}$ is incurred as dead time.
4. **Daily Time & Budget Ceiling:** Total elapsed time per day (transit + waiting + dwell + meals + buffers) cannot exceed $T_{\max, m}$, and cumulative trip cost cannot exceed hard budget $B_{\max}$.

#### Key Heuristic Insights from TTDP Research (Gavalas et al., 2014)
1. **Spatial Clustering Before Sequencing (Cluster-First, Route-Second):** Grouping candidate POIs into contiguous **walkable neighborhood clusters** (or transit-line corridors) per day eliminates cross-city zig-zagging ("spatial oscillation").
2. **Time-Window Tightness Priority:** Nodes with narrow time windows ($L_{im} - O_{im}$ small, such as a timed palace tour, sunset viewpoint, or morning fish market) must be anchored first; wide-window nodes (parks, neighborhood strolls, shrines open 24/7) fill the flexible slots around them.
3. **Marginal Utility per Hour of Total Commitment:** A POI's value is not its raw score $S_i$, but its **yield ratio**:
   $$\text{Yield}(i) = \frac{S_i}{d_i + \Delta T_{\text{D2D}}(i)}$$
   A "must-see" attraction that requires a 3-hour round-trip detour for a 20-minute photo op has a dismal yield ratio and frequently destroys the rest of the day's prism.

### 1.3 Why Default LLMs Fail on Real-World Travel Planning: The TravelPlanner Benchmark (Xie et al., ICML 2024)

- **Primary Source:**
  - Jian Xie, Kai Zhang, Jiangjie Chen, Tinghui Zhu, Renze Lou, Yuandong Tian, Yanghua Xiao, & Yu Su (2024), *"TravelPlanner: A Benchmark for Real-World Planning with Language Agents"*, *Proceedings of the 41st International Conference on Machine Learning (ICML 2024)*, PMLR Vol. 235, pp. 54590–54613 ([arXiv:2402.01622](https://arxiv.org/abs/2402.01622)).

Xie et al. (2024) evaluated frontier language models across 1,225 travel-planning tasks governed by three constraint tiers: **Environment Constraints** (real availability, prices, schedules), **Commonsense Constraints** (valid spatial continuity, non-overlapping times, reasonable meal/lodging routing, no repeated attractions), and **Hard User Constraints** (budget ceilings, room rules, transport mode restrictions, cuisine/accessibility needs).

| Failure Mode Category | Empirical Observation in *TravelPlanner* (Xie et al., 2024) | Root Cause in Default LLM Generation | Mandatory Skill Countermeasure |
| :--- | :--- | :--- | :--- |
| **Commonsense & Spatial Continuity Failures** | Agents leave the traveler in City A on Night 2 and start Day 3 in City B without a valid connecting transport leg, or route $A \rightarrow C \rightarrow B$ across opposite ends of a metro area. | Next-token generation optimizes for topical similarity rather than geographic coordinates and state transitions. | **Explicit Geographic Clustering & State Continuity Table:** Every day must begin at the exact location where the previous night ended, and POIs within a half-day must share a single geographic cluster. |
| **Hallucinated POIs, Routes & Operating Hours** | Agents invent non-existent direct flights/trains, schedule closed attractions, or assume uniform 9-to-5 opening hours. | Parametric memory blurs seasonal timetables, terminated routes, and Monday/Tuesday museum closures. | **Primary Timetable & Calendar Verification:** Never assume a route or opening window exists; verify day-of-week hours, seasonal closures, and reservation lead times against official sources. |
| **Hard Constraint Forgetting Over Long Horizons** | While agents satisfy individual micro-steps (>70% delivery rate), joint satisfaction of all Commonsense + Hard constraints drops to **0.6% (GPT-4)** and **4.4% (GPT-4-Turbo)**. | Context drift across multi-day generation causes the model to drop budget tallies, mobility limits, or dietary/room rules by Day 4+. | **End-of-Plan Constraint Verification Matrix:** Audit the completed itinerary against an explicit checklist of all Capability, Coupling, Authority, and Budget constraints before output. |

---

## 2. Door-to-Door Transit Math, Buffer Sizing & Connection Risk Engineering

### 2.1 Multimodal Door-to-Door ($T_{\text{D2D}}$) Decomposition & Perceived Travel Time Multipliers

When a traveler or LLM checks a transit app or timetable and sees *"Tokyo to Kyoto: 2 hours 15 minutes on the Nozomi Shinkansen"* or *"London to Paris: 1 hour 15 minutes by flight"*, they are looking solely at **in-vehicle line-haul time ($T_{\text{in-vehicle}}$)**. Scheduling an itinerary around $T_{\text{in-vehicle}}$ guarantees missed connections and chronic exhaustion.

- **Primary Sources:**
  - Transportation Research Board (TRB) / Kittelson & Associates et al. (2013), *Transit Capacity and Quality of Service Manual (TCQSM)*, 3rd Edition, **TCRP Report 165**, Chapter 4: Quality of Service Concepts, Exhibit 4-5 ([DOI: 10.17226/24766](https://doi.org/10.17226/24766); [NAP Record 24766](https://nap.nationalacademies.org/catalog/24766/transit-capacity-and-quality-of-service-manual-third-edition)).
  - Mark Wardman (2004), *"Public transport values of time"*, *Transport Policy*, Vol. 11, No. 4, pp. 363–377 ([DOI: 10.1016/j.tranpol.2004.05.001](https://doi.org/10.1016/j.tranpol.2004.05.001)).
  - Mark Wardman (2001), *"A review of British evidence on time and service quality valuations"*, *Transportation Research Part E: Logistics and Transportation Review*, Vol. 37, Issues 2–3, pp. 107–128 ([DOI: 10.1016/S1366-5545(00)00012-0](https://doi.org/10.1016/S1366-5545(00)00012-0)).

#### A. The Complete Door-to-Door Clock-Time Equation ($T_{\text{D2D}}$)
For any intercity or intracity transit leg, true elapsed clock time from Hotel/Origin Door $A$ to Destination Door $B$ is:

$$T_{\text{D2D}} = T_{\text{checkout/pack}} + T_{\text{access}} + T_{\text{terminal/security}} + T_{\text{wait/headway}} + T_{\text{in-vehicle}} + \sum_{k=1}^{K} T_{\text{transfer}, k} + T_{\text{baggage/customs}} + T_{\text{egress}} + T_{\text{checkin/drop}} + T_{\text{buffer}}$$

- **The "Hotel Change Tax" Rule:** Every hotel change consumes **2.5 to 4.5 hours of prime daytime utility** even when $T_{\text{in-vehicle}}$ is only 60 minutes (packing, checkout, access transit, station buffer, line-haul, egress transit, luggage storage or check-in wait, and unpacking). Therefore, **1-night stays should be strictly minimized** outside of dedicated point-to-point road trips or trekking routes.

#### B. Generalized / Perceived Travel Time ($T_{\text{perceived}}$) & Transfer Penalties
In transport economics (TCRP Report 165 Exhibit 4-5; Wardman, 2001, 2004), passengers do not experience all minutes equally. Out-of-vehicle walking, waiting, and transferring impose **2.0x to 2.5x higher disutility per minute** than seated in-vehicle time, plus a fixed psychological and physical **interchange penalty ($\delta_{\text{transfer}}$)** simply for breaking a journey—which escalates sharply when hauling luggage, navigating stairs, or traveling with children/seniors:

$$T_{\text{perceived}} = T_{\text{in-vehicle}} + w_{\text{walk}} \left(T_{\text{access}} + T_{\text{egress}}\right) + w_{\text{wait}} T_{\text{wait}} + \sum_{k=1}^{K} \left(w_{\text{transfer}} T_{\text{transfer}, k} + \delta_{\text{transfer}}\right)$$

| Trip Component | Empirical Disutility Multiplier (TCRP Report 165 / Wardman, 2004) | Multiplier with Heavy Luggage / Stroller / Mobility Limits | Practical Itinerary Routing Rule |
| :--- | :--- | :--- | :--- |
| **In-Vehicle Time ($T_{\text{in-vehicle}}$)** | **$1.0\times$** (seated baseline; $1.5\times\text{–}2.0\times$ if standing in crowded transit) | **$1.0\times\text{–}1.5\times$** | A 3.5-hour direct high-speed train door-to-door almost always beats a 1-hour flight once airport access, 90–120 min security/boarding, baggage claim, and city-center egress are summed. |
| **Walk Access / Egress ($w_{\text{walk}}$)** | **$2.0\times\text{–}2.2\times$** (U.S./UK empirical range $0.8\text{–}4.4\times$) | **$3.0\times\text{–}4.0\times$** (cobblestones, rain, stairs, heat) | A hotel "15 minutes' walk from the station" up a steep hill or over Venice bridges/Roman cobblestones is a major daily friction tax when carrying bags. |
| **Initial Wait / Headway Time ($w_{\text{wait}}$)** | **$2.1\times$** (range $0.8\text{–}5.1\times$) | **$2.5\times$** | Rural buses, ferries, and regional trains with 60–120 min headways require explicit timetable synchronization, not "show up and go" assumptions. |
| **Transfer Time ($w_{\text{transfer}}$) + Pure Transfer Penalty ($\delta_{\text{transfer}}$)** | **$2.5\times$ per minute** + **10–25 in-vehicle equivalent minutes** per transfer | **$3.5\times$ per minute** + **30–45 equivalent minutes** per transfer | A route that saves 12 minutes of clock time by adding two subway/train transfers with luggage is a **net loss** in generalized travel cost and misconnection reliability. |

### 2.2 The Planning Fallacy & Outside-View Buffer Sizing (Kahneman & Tversky, 1979; Buehler et al., 1994)

- **Primary Sources:**
  - Daniel Kahneman & Amos Tversky (1979), *"Intuitive prediction: Biases and corrective procedures"*, in *TIMS Studies in Management Science*, Vol. 12, pp. 313–327 (reprinted in Kahneman, Slovic, & Tversky, 1982, *Judgment under Uncertainty: Heuristics and Biases*, Cambridge University Press, [DOI: 10.1017/CBO9780511809477.031](https://doi.org/10.1017/CBO9780511809477.031)).
  - Roger Buehler, Dale Griffin, & Michael Ross (1994), *"Exploring the 'planning fallacy': Why people underestimate their task completion times"*, *Journal of Personality and Social Psychology*, Vol. 67, No. 3, pp. 366–381 ([DOI: 10.1037/0022-3514.67.3.366](https://doi.org/10.1037/0022-3514.67.3.366)).

Buehler, Griffin, and Ross (1994) proved that planners adopt an **internal ("inside view") simulation** of future tasks: they mentally simulate the *best-case scenario* where every train platform is found immediately, zero ticket machines reject foreign credit cards, nobody needs a restroom break, and lines do not exist. In empirical trials, fewer than 30% of subjects finished tasks within their self-predicted "realistic" times.

To replace the inside view with **Outside-View Reference Class Forecasting** (Kahneman & Tversky, 1979), an itinerary skill must inject mandatory **Friction Buffers ($T_{\text{buffer}}$)** scaled to the consequence of delay:

1. **Routine Intra-City Transit / Wayfinding Buffer:** Add **$+25\%$ to $+35\%$** (minimum $+15\text{ min}$) onto raw mapping-app walking/transit times in unfamiliar cities (station labyrinth navigation in Shinjuku/Châtelet, ticket gates, elevator searches, rest stops).
2. **Coupled Timed-Entry / Reservation Buffer:** Target arrival at the venue entrance **20–30 minutes before** a non-refundable timed-entry cutoff (e.g., Borghese Gallery, Anne Frank House, Alhambra Nasrid Palaces).
3. **High-Consequence Departure Buffer (Flights, Long-Distance Rail, Ferries):** Target arrival at the departure terminal at the **95th percentile ($P_{95}$) safe window** (2.0 hours domestic air / 3.0 hours international air / 30–45 minutes high-speed rail with security or unfamiliar station layout).

### 2.3 Aviation & Rail Connection Risk Engineering: Single-PNR vs. Self-Transfer

A catastrophic failure mode in DIY and AI-assisted travel planning is treating two separate tickets as a normal "layover."

- **Primary Sources & Regulatory Standards:**
  - **IATA Resolution 765**, *Interline Connecting Time Intervals – Passenger and Checked Baggage*, and **IATA Standard Schedules Information Manual (SSIM) Chapter 8** (governing **Minimum Connecting Time [MCT]** across Global Distribution Systems) ([IATA MCT Overview](https://www.iata.org/en/services/data/timetables/mct/)).
  - **European Union Regulation (EC) No 261/2004** of the European Parliament and of the Council of 11 February 2004 establishing common rules on compensation and assistance to passengers in the event of denied boarding and of cancellation or long delay of flights ([EUR-Lex CELEX: 32004R0261](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0261)).
  - **U.S. Department of Transportation (DOT), 14 CFR Part 260**, *Refunds and Other Consumer Protections* (Final Rule effective June 25, 2024; compliance October 28, 2024) ([eCFR 14 CFR Part 260](https://www.ecfr.gov/current/title-14/chapter-II/subchapter-A/part-260)).
  - **CIV / EU Rail Passenger Rights Regulation (EU) 2021/782** & **AJC (*Agreement on Journey Continuation*) / Railteam "Hop on the Next Available Train" (HOTNAT)** ([EUR-Lex CELEX: 32021R0782](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021R0782)).

| Connection Architecture | Legal & Operational Protection | Baggage & Terminal Flow | Mandatory Agent Buffer & Risk Rule |
| :--- | :--- | :--- | :--- |
| **1. Protected Single-PNR / Interline Ticket** (same booking reference across one airline or alliance/interline partners) | **Protected:** Carrier is contractually obligated to rebook on the next available flight at no cost, provide duty-of-care meals/hotels under **EC 261/2004** (or carrier Conditions of Carriage), and pay statutory compensation (€250–€600 in EU/UK if arrival delay $\ge 3\text{ hrs}$ from non-extraordinary causes) or automatic cash refund if trip is abandoned under **14 CFR Part 260**. | Bags are typically through-checked to final destination (except mandatory first-port-of-entry customs re-check in countries like the US). | **Never book exactly at the bare legal IATA MCT** if a delay on Leg 1 would strand the traveler overnight (e.g., last flight of the day). Require **$\ge 1.5\times \text{MCT}$** ($90\text{–}120\text{ min}$ domestic; $120\text{–}180\text{ min}$ international/customs) when connecting to a once-daily long-haul flight. |
| **2. Unprotected Separate Tickets ("Self-Transfer" / Split-PNR)** (two independent bookings, e.g., low-cost carrier into a long-haul hub, or separate rail + air tickets) | **Zero Protection:** If Leg 1 is delayed or canceled, Carrier 2 treats the passenger as a **No-Show**, cancels the entire outbound and return long-haul itinerary with **100% forfeiture of fare**, and owes zero duty of care or rebooking. | Passenger must exit airside, clear immigration, wait at baggage carousel, clear customs, change terminals landside, re-check bags before the 60-minute bag-drop cutoff, and re-clear security/exit immigration. | **High-Risk Warning:** For any unprotected connection onto a long-haul flight, cross-oceanic cruise departure, or non-refundable anchor event, mandate either **(a) arriving the evening before (overnight buffer)** or **(b) a minimum 4–6 hour buffer** for short-haul self-transfers where rebooking costs are low. |

---

## 3. Cognitive Load, Museum/Walking Fatigue, Circadian Physiology & Daily Pacing

### 3.1 The Peak-End Rule & Duration Neglect in Vacation Evaluation (Fredrickson & Kahneman, 1993; Kemp et al., 2008)

Travelers frequently fall into the **"Checklist Maximization Trap"**: believing that visiting 18 attractions over 6 days yields $2\times$ the happiness of visiting 9 attractions at an unhurried pace. Behavioral decision research proves the exact opposite.

- **Primary Sources:**
  - Barbara L. Fredrickson & Daniel Kahneman (1993), *"Duration neglect in retrospective evaluations of affective episodes"*, *Journal of Personality and Social Psychology*, Vol. 65, No. 1, pp. 45–55 ([DOI: 10.1037/0022-3514.65.1.45](https://doi.org/10.1037/0022-3514.65.1.45)).
  - Simon Kemp, Christopher D. B. Burt, & Laura Furneaux (2008), *"A test of the peak-end rule with extended autobiographical events"*, *Memory & Cognition*, Vol. 36, No. 1, pp. 132–138 ([DOI: 10.3758/MC.36.1.132](https://doi.org/10.3758/MC.36.1.132)).

- **Core Empirical Findings:**
  1. **Remembered Utility vs. Instant Utility:** Fredrickson & Kahneman (1993) demonstrated that retrospective evaluations of affective episodes are governed by the **Peak-End Rule**: global satisfaction is predicted by the average of the **most intense emotional moment (Peak)** and the **final segment of the experience (End)**, while total duration or the sheer count of mediocre intermediate stops exhibits **Duration Neglect**.
  2. **Empirical Validation on Multi-Day Vacations:** Kemp, Burt, & Furneaux (2008) tracked travelers daily during and after multi-day holidays (4 to 14 days). Trip duration had no significant effect on retrospective enjoyment, whereas **peak-day pleasure** and **final-day pleasure** strongly shaped remembered happiness. Crucially, negative troughs (frantic transit rushes, blistered feet, hanger, luggage stress on the final day) disproportionately dragged down the overall evaluation.
  3. **Agentic Pacing Design Rule:**
     - Design around **1–2 unhurried Peak Moments** rather than 6 rushed stops.
     - **Protect the Final 24 Hours (The "End" Guardrail):** Never schedule high-stress cross-country transit, exhausting multi-hour marches, or tight self-transfers on the last day of the trip. Keep the final night located comfortably near the departure hub with a relaxed, high-satisfaction finale.

### 3.2 Museum Fatigue, Directed Attention Fatigue & Attention Restoration Theory (Gilman, 1916; Melton, 1935; Bitgood, 2009; Kaplan, 1995)

Why do travelers who schedule the Louvre in the morning and the Musée d'Orsay in the afternoon end up sitting on a bench staring blankly at their phones by 2:30 PM?

- **Primary Sources:**
  - Benjamin Ives Gilman (1916), *"Museum Fatigue"*, *The Scientific Monthly*, Vol. 2, No. 1, pp. 62–74 ([JSTOR: 6127](https://www.jstor.org/stable/6127)).
  - Arthur W. Melton (1935), *Problems of Installation in Museums of Art*, Publications of the American Association of Museums, New Series, No. 14, Washington, DC ([HathiTrust Record](https://catalog.hathitrust.org/Record/001157268)).
  - Stephen Bitgood (2009), *"Museum Fatigue: A Critical Review"*, *Visitor Studies*, Vol. 12, No. 2, pp. 93–111 ([DOI: 10.1080/10645570903203406](https://doi.org/10.1080/10645570903203406)).
  - Stephen Kaplan (1995), *"The restorative benefits of nature: Toward an integrative framework"*, *Journal of Environmental Psychology*, Vol. 15, No. 3, pp. 169–182 ([DOI: 10.1016/0272-4944(95)90001-2](https://doi.org/10.1016/0272-4944%2895%2990001-2)).

- **Core Empirical Findings:**
  1. **The 90–120 Minute Attention Decay Curve (Melton, 1935; Bitgood, 2009):** Behavioral tracking inside museums shows that visitor stopping frequency and viewing time per exhibit decay exponentially after **60 to 90 minutes** and hit severe **object satiation / cognitive exhaustion** by **120 minutes**, compounded by slow shuffling locomotion ("the museum shuffle"), postural strain (Gilman, 1916), and sensory overload.
  2. **Directed Attention Fatigue vs. Soft Fascination (Kaplan, 1995):** In **Attention Restoration Theory (ART)**, Stephen Kaplan distinguishes between **Directed Attention**—which requires effortful executive control, reading plaques, navigating crowds, and inhibiting distractions, and is a **depletable neurocognitive resource**—and **Restorative Environments** characterized by **"Soft Fascination"** (parks, waterfronts, gardens, scenic cafés, thermal baths, aimless neighborhood strolling) that allow directed attention mechanisms to replenish.
  3. **The "1 Anchor + 1 Flexible Option per Half-Day" Rule:**
     - Divide every day into three blocks: **Morning**, **Afternoon**, and **Evening**.
     - Each half-day block may contain **at most 1 Fixed/High-Cognitive-Load Anchor** (e.g., one major museum, historical monument, or guided tour capped at 90–120 minutes of focused viewing) plus **1 Optional/Flexible Low-Load Activity** in the same spatial cluster.
     - **Modality Alternation Rule:** Never schedule two High-Directed-Attention stops back-to-back (e.g., never pair two art museums or two dense archaeological sites consecutively). Always alternate:
       $$\text{High-Cognitive-Load Anchor (Museum/Monument)} \longrightarrow \text{Restorative / Sensory Stop (Park, Café, Market, Waterfront Walk)}$$

### 3.3 Circadian Physiology & Jet-Lag Directionality Math (Waterhouse et al., 2007; CDC Yellow Book)

- **Primary Sources:**
  - Jim Waterhouse, Thomas Reilly, Greg Atkinson, & Ben Edwards (2007), *"Jet lag: trends and coping strategies"*, *The Lancet*, Vol. 369, Issue 9567, pp. 1117–1129 ([DOI: 10.1016/S0140-6736(07)60529-7](https://doi.org/10.1016/S0140-6736%2807%2960529-7)).
  - U.S. Centers for Disease Control and Prevention (CDC), *CDC Yellow Book: Health Information for International Travel*, Chapter: *Jet Lag Disorder* ([CDC Yellow Book: Jet Lag Disorder](https://www.cdc.gov/yellow-book/hcp/travel-by-air-and-sea/jet-lag-disorder.html)).

- **Core Physiological Asymmetry:**
  Because the endogenous human suprachiasmatic nucleus (SCN) circadian pacemaker has an intrinsic free-running period slightly longer than 24 hours ($\tau \approx 24.2\text{ hours}$), **phase delay (westward travel, lengthening the day)** is physiologically easier than **phase advance (eastward travel, shortening the day)**:
  $$D_{\text{resync}}(\Delta Z) \approx \begin{cases} 1.0 \times |\Delta Z| \text{ days} & \text{for Westward travel (phase delay)} \\ 1.5 \times |\Delta Z| \text{ days} & \text{for Eastward travel (phase advance)} \end{cases}$$
  where $|\Delta Z|$ is the number of time zones crossed (significant when $|\Delta Z| \ge 3$).

- **Mandatory Day-1 / Day-2 Itinerary Pacing Rules for Long-Haul Arrivals ($|\Delta Z| \ge 5$):**
  1. **No High-Cognitive or High-Risk Activities on Arrival Day:** Never schedule a rental-car mountain drive, a dense 3-hour museum tour, or a non-refundable prepaid ticket immediately following an overnight long-haul flight.
  2. **Daylight & Light-Walk Anchoring:** Schedule Arrival Day around luggage drop, outdoor natural light exposure (to entrain the SCN), a gentle neighborhood orientation walk, an early restorative dinner, and local-time sleep.
  3. **Direction-Specific Morning Scheduling:**
     - *Eastward Travel (e.g., Americas $\rightarrow$ Europe, or Europe $\rightarrow$ Japan):* The traveler's biological clock is still at 3:00 AM during local 9:00 AM. **Do not schedule 7:30 AM fixed departures on Days 1–2**; place the primary anchor in the late morning (10:30 AM–11:00 AM) and use strategic morning bright light.
     - *Westward Travel (e.g., Europe $\rightarrow$ Americas, or Asia $\rightarrow$ Europe):* The traveler will naturally wake up early (5:00 AM–6:00 AM local time) and hit a circadian trough at 6:00 PM–7:00 PM. **Leverage early-morning openings (7:00 AM–8:30 AM) on Days 1–3** to beat crowds at major sights, and keep evenings light and early.

---

## 4. Logistics & Entry Gate (Authority, Calendar & Environmental Constraints)

An itinerary that is aesthetically pleasing on paper fails catastrophically if the traveler is denied boarding at the airport, locked out of a closed monument, or hospitalized with acute mountain sickness on Day 2. Every trip evaluation must execute a **Hard-Knockout Logistics & Entry Gate** before finalizing daily plans.

### 4.1 Consular, Border & Regulatory Knockout Gates

- **Primary Sources & Regulatory Frameworks:**
  - **European Union Regulation (EU) 2016/399** (The **Schengen Borders Code**), **Article 6(1)(a)**: Entry conditions for third-country nationals ([EUR-Lex CELEX: 32016R0399](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0399)).
  - **International Air Transport Association (IATA) Timatic** (Travel Information Manual Automatic — the industry database airlines query at check-in to enforce passport, visa, and health entry rules) ([IATA Timatic](https://www.iata.org/en/services/compliance/timatic/)).
  - **United Nations Road Traffic Conventions:** **1949 Geneva Convention on Road Traffic** vs. **1968 Vienna Convention on Road Traffic** (governing International Driving Permit [IDP] formats) ([UNECE Road Traffic Conventions](https://unece.org/transport/international-agreements/conventions-and-agreements)).
  - **World Health Organization (WHO)**, *International Health Regulations (2005)*, 3rd Edition, Annex 6 & Annex 7 (Yellow Fever vaccination certificate validity) ([WHO IHR](https://www.who.int/publications/i/item/9789241580496)).

| Regulatory Gate | Exact Statutory / Operational Rule | Common Traveler Failure Mode | Agent Verification & Warning Protocol |
| :--- | :--- | :--- | :--- |
| **1. Schengen Dual Passport Rule (Reg. EU 2016/399 Art. 6(1)(a))** | Passport must simultaneously be: **(a) issued within the previous 10 years** on the day of entry, AND **(b) valid for at least 3 months after the intended date of departure** from the Schengen Area. | UK/US/Commonwealth travelers whose passports were renewed early and have $>10\text{ years}$ total validity are denied boarding even when the expiry date is 8 months away. | Check both **Issue Date ($<10\text{ yrs}$)** and **Expiry Date ($\ge +3\text{ mos}$ Schengen / $\ge +6\text{ mos}$ for many Asian, Middle Eastern, and South American states)** plus **2–4 blank visa pages**. |
| **2. Electronic Travel Authorizations & Visas** | Mandatory pre-departure digital authorizations even for "visa-exempt" nationals: **US ESTA**, **UK ETA**, **EU ETIAS** (upon rollout), **Canada eTA**, **Australia ETA/eVisitor**, **New Zealand NZeTA**, **Korea K-ETA**, **India e-Visa**. | Assuming visa-free status means "show up with a passport," or applying at the airport when approval takes 72+ hours. | Explicitly list required electronic authorizations, official government portal domains (warning against $5\times$-markup scam sites), and lead-time deadlines. |
| **3. International Driving Permits (IDP: 1949 vs. 1968)** | Countries ratify *either* the **1949 Geneva Convention** (1-year IDP, strictly required by **Japan, South Korea, Taiwan**) *or* the **1968 Vienna Convention** (3-year IDP, used across much of continental Europe, Brazil, etc.), or require a certified local translation (e.g., JAF translation in Japan for select nationalities). | Arriving at a rental counter in Japan or Italy with only a domestic driver's license—or the wrong convention IDP—and being legally barred from picking up the vehicle. | Whenever car, scooter, or kart rental is in scope, verify the exact IDP convention required by the destination country and notes that IDPs **must be issued in the home country prior to departure**. |
| **4. Health Certificates & Strict Medication Import Laws** | **WHO IHR Annex 7** Yellow Fever certificate (valid 10 days after vaccination) for endemic/transit zones; strict national customs bans on common domestic prescriptions (e.g., **Japan's Narcotics and Psychotropics Control Act** banning Adderall/amphetamine stimulants and pseudoephedrine decongestants; **UAE/Singapore** controlled-substance permits). | Bringing standard ADHD medication, codeine, or Sudafed into Japan or the UAE without an advance *Yunyu Kakunin-sho* / Ministry of Health import permit, risking arrest at customs. | Flag mandatory vaccinations and alert travelers carrying prescription stimulants, opioids, inhalers, or high-dose decongestants to check official embassy/ministry import clearance windows (often 2–4 weeks pre-trip). |

### 4.2 High-Altitude Physiology, Seasonal Weather Extremes & Calendar / Closure Matrices

- **Primary Source:**
  - U.S. Centers for Disease Control and Prevention (CDC), *CDC Yellow Book: Health Information for International Travel*, Chapter: *High-Altitude Travel and Altitude Illness* ([CDC Yellow Book: High-Altitude Travel](https://www.cdc.gov/yellow-book/hcp/environmental-hazards-risks/high-altitude-travel-and-altitude-illness.html)).

1. **High-Altitude Acclimatization Guardrails ($>2,500\text{ m} / 8,200\text{ ft}$):**
   - Per CDC Yellow Book wilderness medicine guidelines, Acute Mountain Sickness (AMS), High-Altitude Pulmonary Edema (HAPE), and High-Altitude Cerebral Edema (HACE) risks begin above **$2,500\text{ m}$ ($8,200\text{ ft}$)** and become acute when flying directly from sea level to high-elevation hubs such as **Cusco ($3,399\text{ m}$)**, **La Paz ($3,640\text{ m}$)**, **Lhasa ($3,656\text{ m}$)**, **Leh ($3,500\text{ m}$)**, or **Quito ($2,850\text{ m}$)**.
   - **Graded Ascent & "Climb High, Sleep Low" Rule:**
     - Whenever possible, route travelers to **sleep at a lower intermediate elevation** first (e.g., descending immediately from Cusco Airport at $3,399\text{ m}$ to the **Sacred Valley / Urubamba at $2,870\text{ m}$** for the first 2–3 nights before sleeping in Cusco or trekking).
     - Above $3,000\text{ m}$ ($10,000\text{ ft}$), do not increase **sleeping elevation** by more than **$500\text{ m}$ ($1,600\text{ ft}$) per day**, and insert an **extra acclimatization night (zero net ascent)** every **$1,000\text{ m}$ ($3,300\text{ ft}$)**.
     - Mandate low physical exertion and zero alcohol for the first 24–48 hours at elevation.
2. **Macro-Holiday, Strike & Weekly Closure Matrix:**
   - **Macro-Holiday Shutdowns & Surge Windows:** Check travel dates against national mass-migration and closure periods: **Japan Golden Week** (late April–early May), **Obon** (mid-August), and **Shōgatsu / New Year** (Dec 29–Jan 3); **Lunar New Year / Chunyun** across East and Southeast Asia; **Ramadan & Eid** (daytime dining adjustments and attraction hour shifts); **Italian *Ferragosto*** (mid-August independent restaurant/shop closures); and **European Sunday/Public Holiday commercial shutdowns** (e.g., Germany's *Ladenschlussgesetz*, Switzerland, Austria, Spain).
   - **The Weekly Museum Closure Trap:** In major cultural capitals, state museums do not close on the same day. For example, in Paris, the **Louvre and Musée Rodin close on Tuesdays**, while the **Musée d'Orsay, Palace of Versailles, and Musée de l'Orangerie close on Mondays**. Every day-by-day itinerary must explicitly annotate the **day-of-week** alongside verified opening and last-entry hours.
   - **Advance Booking Horizon Matrix:** Identify high-demand bottlenecks that sell out **30 to 90 days in advance** (e.g., Ghibli Museum / Ghibli Park, Alhambra Nasrid Palaces, Last Supper in Milan, Anne Frank House, Uffizi / Accademia timed slots, US National Park recreation.gov permits, Machu Picchu circuits) and separate them into an explicit **Booking Action Timeline**.

---

## 5. Information Economics of Anti-Tourist-Trap Vetting & Hospitality Comparison

### 5.1 Staged Authenticity & The "Market for Lemons" in Zero-Repeat Tourist Zones (MacCannell, 1973; Akerlof, 1970)

Why is the restaurant directly facing the Trevi Fountain, Times Square, or the Prague Astronomical Clock almost guaranteed to serve overpriced, low-quality food?

- **Primary Sources:**
  - Dean MacCannell (1973), *"Staged Authenticity: Arrangements of Social Space in Tourist Settings"*, *American Journal of Sociology*, Vol. 79, No. 3, pp. 589–603 ([DOI: 10.1086/225585](https://doi.org/10.1086/225585)).
  - George A. Akerlof (1970), *"The Market for 'Lemons': Quality Uncertainty and the Market Mechanism"*, *The Quarterly Journal of Economics*, Vol. 84, No. 3, pp. 488–500 ([DOI: 10.2307/1879431](https://doi.org/10.2307/1879431)).

- **Economic Mechanism:**
  1. **Zero-Repeat-Game Adverse Selection (Akerlof, 1970):** In a residential neighborhood where 80% of customers are locals, a restaurant faces an **infinite-horizon repeated game**: serving mediocre food at inflated prices destroys reputation and leads to bankruptcy. Adjacent to a global tourist monument, 99% of customers play a **one-shot game**: they walk in once based on foot traffic, never return to the city, and cannot observe food quality prior to ordering (**Experience Attribute**). As Akerlof proved, when buyers cannot pre-verify quality and sellers do not depend on repeat patronage, **low-quality "lemons" systematically drive out high-quality operators** because rent is bid up by high-margin tourist extractors.
  2. **Staged Front Regions vs. Back Regions (MacCannell, 1973):** Building on Erving Goffman, sociologist Dean MacCannell showed that tourist zones construct **"staged authenticity"** (costumed touts, multilingual laminated photo menus, pseudo-traditional decor) designed to simulate local culture for outsiders while insulating real local life in residential "back regions."
  3. **The 3-Block / Repeat-Local Rule:** Never dine or shop on the immediate perimeter of a Tier-1 monument or cruise terminal. Walk **3–6 blocks away** into a residential or office street where menus are seasonal, concise, written primarily in the local language, and patronized by local workers or residents.

### 5.2 Defeating Review Manipulation via Native Primary Guides (Mayzlin et al., 2014; FTC 16 CFR Part 255 & 465)

- **Primary Sources:**
  - Dina Mayzlin, Yaniv Dover, & Judith Chevalier (2014), *"Promotional Reviews: An Empirical Investigation of Online Review Manipulation"*, *American Economic Review*, Vol. 104, No. 8, pp. 2421–2455 ([DOI: 10.1257/aer.104.8.2421](https://doi.org/10.1257/aer.104.8.2421)).
  - U.S. Federal Trade Commission (FTC), **16 CFR Part 255**, *Guides Concerning the Use of Endorsements and Testimonials in Advertising* ([eCFR 16 CFR Part 255](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255)), and **16 CFR Part 465**, *Trade Regulation Rule on the Use of Consumer Reviews and Testimonials* ([eCFR 16 CFR Part 465](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465)).

Mayzlin, Dover, and Chevalier (2014) demonstrated empirically that hospitality establishments with higher incentives and lower reputational penalties engage in systematic **promotional review manipulation** (inflating their own 5-star ratings and planting negative reviews on nearby competitors). In travel, this is compounded by **English-language rating inflation** on global tourist platforms (where novice visitors rate a mediocre, friendly tourist trap 4.8 stars because they lack a local calibration baseline) and **viral TikTok/Instagram sponsorship bias**.

To defeat tourist-review distortion, an AI travel planner must cross-check recommendations against **native-language regional platforms and curated independent guides**:

| Region / Country | Primary Native / High-Trust Vetting Sources | Calibration & Interpretation Nuances |
| :--- | :--- | :--- |
| **Japan** | **Tabelog (`tabelog.com`)**, *Michelin Guide / Bib Gourmand*, *Hyakumeiten* (Tabelog Top 100 by category) | **Strict Scale:** Tabelog weights experienced local reviewers heavily. A score of **$3.50+$ is top ~3–5% exceptional**; **$3.20\text{–}3.49$ is a very strong neighborhood spot**; anything $3.70+$ often requires advance reservations. Meanwhile, a 4.7 on English Google Maps in Shinjuku/Kyoto with 90% English reviews is frequently a tourist queue trap. |
| **Italy** | **Slow Food *Osterie d'Italia***, **Gambero Rosso** (*Tre Forchette* / *Tre Gamberi* / *Tre Spicchi*), *Michelin Bib Gourmand* | Prioritize authentic regional *osterie* and *trattorie* vetted by Slow Food over English-language "Top 10 Rome Pasta" blogs. |
| **France** | **Le Fooding**, **Gault & Millau**, *Michelin Bib Gourmand*, local market halls (*Marchés couverts*) | Verify the legal ***"Fait Maison"*** designation and short daily chalkboard (*ardoise*) menus vs. industrial sysco reheating. |
| **Spain & Portugal** | **Guía Repsol (*Soles Repsol* & *Soletes*)**, *Macarfi Guide* (Madrid/Barcelona/Basque Country), *Michelin Bib Gourmand* | Repsol *Soletes* specifically target authentic, affordable local *tascas*, *tabernas*, and *pintxo* bars favored by locals. |
| **South Korea** | **Naver Map**, **KakaoMap**, **Blue Ribbon Survey** (*Korea's Michelin*), **CatchTable** | Google Maps is severely restricted by South Korean geospatial export laws and heavily skewed toward foreign tourists; verify ratings and active local reviews on **Naver/KakaoMap** and **Blue Ribbon Survey**. |
| **China / Taiwan / HK** | **Dianping (*Dazhong Dianping* / Black Pearl Guide)**, **OpenRice** (HK), Taiwanese local night-market/MRT guides, *Bib Gourmand* | Cross-check local review volume and recent photos on Dianping/OpenRice rather than Western OTA summaries. |
| **Global / Americas / UK** | **Michelin *Bib Gourmand*** (high quality at moderate price), **James Beard Foundation** (US), **Good Food Guide** (UK), **Eater 38** (curated local editor heatmaps), local subreddit/forum consensus (`r/JapanTravelTips`, `r/ItalyTravel`, etc.) | Filter out paid PR roundups; require convergence between local food critics and recent uncompensated resident reports. |

### 5.3 True Location-Adjusted Nightly Cost & Drip Pricing Defense (FTC 16 CFR Part 464; Santana et al., 2020)

Travelers routinely book a "cheap" hotel or Airbnb on the suburban periphery—or a "discounted" resort—only to discover at checkout and during the trip that mandatory fees, transit costs, and lost vacation hours made it far more expensive than staying centrally.

- **Primary Sources:**
  - U.S. Federal Trade Commission (FTC), **16 CFR Part 464**, *Trade Regulation Rule on Unfair or Deceptive Fees* (issued December 2024; effective May 12, 2025, targeting mandatory hotel resort, destination, and short-term rental cleaning/service drip fees) ([eCFR 16 CFR Part 464](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-464); [FTC Final Rule Release](https://www.ftc.gov/news-events/news/press-releases/2024/12/federal-trade-commission-announces-bipartisan-rule-banning-junk-fees)).
  - Shelle Santana, Steven K. Dallas, & Vicki G. Morwitz (2020), *"Consumer Reactions to Drip Pricing"*, *Marketing Science*, Vol. 39, No. 1, pp. 188–210 ([DOI: 10.1287/mksc.2019.1207](https://doi.org/10.1287/mksc.2019.1207)).

Santana, Dallas, and Morwitz (2020) demonstrated across six studies that when mandatory surcharges are revealed sequentially (**drip pricing**), consumers anchor on the initial base rate and fail to adjust away from the option even after the final price exceeds a transparent competitor's price—a behavioral distortion caused by psychological sunk time and search-reset aversion.

#### The True Location-Adjusted Nightly Cost Equation ($C_{\text{night, true}}$)
When comparing Accommodation Option $A$ (e.g., central walkable hub) against Option $B$ (e.g., peripheral "budget" hotel or short-term rental), an AI trip planner must compute the **all-in daily cost including transport and time friction**:

$$C_{\text{night, true}} = P_{\text{base}} + F_{\text{resort/dest}} + \frac{F_{\text{cleaning/platform}}}{N_{\text{nights}}} + T_{\text{occupancy/city}} + C_{\text{parking/ZTL}} + \Delta C_{\text{transit/taxi}} + v_{\text{vacation\_hour}} \cdot \Delta T_{\text{commute}}$$

where:
- $P_{\text{base}}$: Advertised nightly room rate.
- $F_{\text{resort/dest}}$: Mandatory daily resort, destination, or amenity fee.
- $F_{\text{cleaning/platform}} / N_{\text{nights}}$: Short-term rental cleaning and OTA service fee amortized over $N_{\text{nights}}$ (which makes 1–2 night Airbnb stays mathematically punitive).
- $T_{\text{occupancy/city}}$: Percentage VAT/occupancy tax plus per-person nightly municipal tourist tax (e.g., €4–€10/person/night in Rome, Paris, Amsterdam, or Kyoto accommodation tax).
- $C_{\text{parking/ZTL}}$: Overnight parking fee (\$40–\$85/night in major cities) and congestion/ZTL zone exposure.
- $\Delta C_{\text{transit/taxi}}$: Round-trip daily transit fares for the whole party plus late-night taxi/rideshare costs when suburban trains stop running.
- $v_{\text{vacation\_hour}} \cdot \Delta T_{\text{commute}}$: The **Vacation Hour Opportunity Cost**. If a peripheral hotel saves \$45/night in cash after transit fares, but adds **90 minutes/day of round-trip commuting** and eliminates the ability to drop off bags or rest midday for 20 minutes, the traveler is selling scarce vacation time at \$30/hour while burning cognitive and physical stamina.

---

## 6. Interactive Context Elicitation, Premortem Stress-Testing, Calibrated Readiness Verdicts & Skill Blueprint

### 6.1 Conversational Preference Elicitation on Verdict-Flipping Travel Variables (Pu & Chen, 2008, 2012)

- **Primary Sources:**
  - Pearl Pu & Li Chen (2008), *"User-Involved Preference Elicitation for Product Search and Recommender Systems"*, *AI Magazine*, Vol. 29, No. 4, pp. 93–103 ([DOI: 10.1609/aimag.v29i4.2200](https://doi.org/10.1609/aimag.v29i4.2200)).
  - Li Chen & Pearl Pu (2012), *"Critiquing-based recommenders: survey and emerging trends"*, *User Modeling and User-Adapted Interaction*, Vol. 22, No. 1–2, pp. 125–150 ([DOI: 10.1007/s11257-011-9111-y](https://doi.org/10.1007/s11257-011-9111-y)).

When a user says *"Plan a 5-day trip to Kyoto and Osaka"*, generating 3,000 words of generic sightseeing before knowing whether they are traveling solo with a backpack or with a toddler and two 75-year-old grandparents in August is useless. Conversely, asking a 12-question intake form before offering any help creates massive friction.

Following Pu & Chen's (2008, 2012) high-information-gain elicitation framework, the advisor checks **5 Verdict-Flipping Travel Variables** before locking in a full itinerary:

1. **Dates, Duration & Origin/Arrival Anchors:** Exact month/dates (or season), number of nights on the ground, and inbound/outbound flight or train timestamps (to bound Day 1, Final Day, jet lag, weather, and holiday closures).
2. **Party Composition, Mobility & Stamina:** Who is traveling (solo, couple, young kids/stroller, seniors), realistic daily walking ceiling, and luggage load.
3. **Budget Tier & Accommodation/Transit Style:** Total or nightly target budget, public transit vs. rental car vs. private transfers, and preferred base neighborhood style.
4. **Core Interests vs. Hard Anti-Goals:** Top 2–3 peak priorities (e.g., specialty food, architecture, hiking, photography) and explicit **anti-goals** (e.g., *"no crowded checklist museums"*, *"no early mornings"*, *"no 1-night hotel hops"*).
5. **Passport / Visa / Dietary / Medical Hard Constraints:** Nationality (if cross-border), severe allergies/dietary laws, or high-altitude/heat sensitivities.

- **Proportionate Elicitation Rule:** If 2+ verdict-flipping variables are missing, ask **at most 2–4 concise, high-leverage questions** (or provide a high-level **Preliminary Routing Skeleton + Critical Warnings** while asking the 2–3 questions needed to build the day-by-day plan).

### 6.2 The Travel Premortem & Contingency Engineering (Klein, 2007)

- **Primary Source:**
  - Gary Klein (2007), *"Performing a Project Premortem"*, *Harvard Business Review*, Vol. 85, No. 9, pp. 18–19 ([HBR Link](https://hbr.org/2007/09/performing-a-project-premortem); [DOI: 10.1109/EMR.2008.4534313](https://doi.org/10.1109/EMR.2008.4534313)).

Before finalizing any itinerary, the agent executes a **Prospective Hindsight (Travel Premortem)** test:
> *"Imagine you have just returned from this trip, and two specific days went completely off the rails—leaving you exhausted, stranded, or deeply disappointed. Looking at the exact connections, weather season, ticket bottlenecks, and pacing in this plan, what caused those failures?"*

Every stress-tested itinerary must attach explicit **If/Then Fallback Triggers** for five high-probability disruptions:
1. **Weather Pivot (Rainout / Heatwave $>35^\circ\text{C}$ / Visibility Zero):** Pre-identify indoor or shaded swaps in the same neighborhood cluster when outdoor anchors are rained out or unsafe in midday heat.
2. **Transit / Strike / Misconnection Fallback:** Specify the backup transport mode, the last viable train/bus departure time of the evening, and luggage forwarding options (e.g., *Takkyubin* in Japan) to decouple passengers from heavy bags.
3. **Ticket / Queue Lockout Pivot:** State what to do if a walk-up line exceeds 45 minutes or an advance lottery is missed.
4. **Low-Energy / Sick-Day Graceful Degradation:** Design every half-day so the **Flexible Option** can be dropped on the spot without breaking any downstream coupling constraint or hotel transfer.

### 6.3 Calibrated 6-Level Itinerary & Decision Verdict Taxonomy

Whether the user asks to **audit an existing itinerary**, **compare destinations/bases**, or **build a new trip plan**, the skill must conclude with an unambiguous, non-hedging verdict from a calibrated 6-level taxonomy:

| Verdict Label | Meaning & Decision Rule | Required Follow-Through in Output |
| :--- | :--- | :--- |
| **`Ready to Book`** | Passes all Consular/Entry, Time-Window, D2D Transit, Connection Buffer, and Cognitive Pacing checks; high Peak-End utility; zero unprotected single-point-of-failure traps. | Provide the chronological **Booking Action Timeline** (what to book 60–90 days out vs. 7 days out vs. walk-up) and day-by-day clustered schedule. |
| **`Viable With Adjustments`** | Strong overall route and destination fit, *but* contains 1–3 fixable pacing, ordering, or buffer flaws (e.g., a museum scheduled on its closed day, back-to-back high-fatigue stops, or a tight connection). | Highlight the exact flaws and present the **corrected day-by-day sequence** with updated D2D buffers. |
| **`Cut Stops / Slow Down`** | Suffers from the **Checklist Maximization Trap** or excessive **Hotel Change Tax** (e.g., 5 cities in 7 days, or 4 anchors in a single day), where transit friction consumes $>35\%$ of waking hours. | Show the **Transit-to-Experience Ratio** math, prune the lowest-yield detours/1-night hops, and present a consolidated **Hub-and-Spoke** alternative. |
| **`Reroute / Change Base`** | Selected neighborhood base, transport mode, or connection architecture is dominated on **True Location-Adjusted Nightly Cost**, safety, or connection reliability (e.g., risky self-transfer or peripheral hotel trap). | Show the head-to-head **True Location-Adjusted Cost & Commute Table** or connection risk comparison, and name the superior base or routing order. |
| **`Shift Season / Dates`** | Requested dates collide with severe monsoon/typhoon/extreme-heat windows, mass national holiday shutdowns (Golden Week, Lunar New Year, Ferragosto), or seasonal road/pass closures. | Detail the exact environmental or calendar impact on the user's goals and specify the optimal alternative date windows (plus survival mitigations if dates are fixed). |
| **`Do Not Book As Planned`** | Violates a hard **Authority or Physiological Knockout** (e.g., passport fails Schengen 10-year/3-month rule, insufficient visa lead time, dangerous unacclimatized altitude jump, or impossible D2D connection). | Flag the exact knockout blocker at the very top of the response and provide the immediate remediation path. |

> **Mandatory Reversal Conditions ("What Would Flip This Verdict?"):** Every trip evaluation or audit must state the concrete conditions that would change the recommendation (e.g., *"This `Cut Stops / Slow Down` verdict on adding Hiroshima as a day trip from Tokyo flips to `Ready to Book` only if you shift the stop to be an en-route break with luggage forwarded between Kyoto and Fukuoka, or extend the trip from 7 to 10 nights"*).

### 6.4 Portable Traveler Context & Optional Memory Architecture (`.agents/traveler-profile.md`)

To prevent users from repeating their passport nationality, home airport, walking pace, dietary rules, and loyalty ecosystems in every session while remaining **100% zero-config by default**:

1. **Zero-Config Default:** Works immediately with zero files required.
2. **Optional Local Traveler Profile (`traveler-profile.md`):**
   - If file reading tools are available, check `.agents/traveler-profile.md` (workspace-level) or `~/.agents/traveler-profile.md` / `~/.claude/traveler-profile.md` (user-level).
   - **Recommended Schema:**
     - **Passports, Residencies & Trusted Traveler Programs:** Nationality, passport issue/expiry dates, existing visas/ETAs, Global Entry / TSA PreCheck / APEC Card, and IDP status.
     - **Home Hub & Transit Preferences:** Home airport/station, preferred cabin/seat rules, motion-sickness sensitivities, and rental-car comfort (manual/automatic, left-hand drive).
     - **Pacing, Mobility & Circadian Style:** Morning lark vs. night owl, realistic daily walking ceiling (e.g., $10\text{ km}$ vs. $20\text{ km}$), mobility/accessibility requirements, and luggage style (carry-on only vs. checked bags).
     - **Dietary, Medical & Sleep Requirements:** Allergies, religious/ethical dietary rules, quiet-room/AC needs, and high-altitude/heat thresholds.
     - **Past Trip Post-Mortems:** Notes on past trips (favorite neighborhoods, pacing lessons learned, hotels/airlines to avoid).

### 6.5 Skill Naming Analysis & 6-Step Protocol Blueprint

#### A. Skill Naming Evaluation Against `writing-for-agents` Principles
Per `writing-for-agents` (`~/.gemini/config/skills/writing-for-agents/SKILL.md`):

| Candidate Name | Slash-Command Ergonomics | Pretraining Leading-Word Alignment | Scope Coverage (New Plans, Audits, Base Comparisons) | Evaluation & Trade-offs |
| :--- | :--- | :--- | :--- | :--- |
| **`trip-planner`** | `/trip-planner [destination/itinerary]` | **Highest.** Universally recognized compound noun/action hook in both human queries and travel-agent benchmarks (*TravelPlanner*). Immediately recruits spatio-temporal routing, transit, and logistics priors. | **Very High.** Covers end-to-end itinerary design, existing itinerary stress-testing, and destination/hotel comparison. | Clear, 12 chars, 1 hyphen; pairs naturally with `fact-check` and `should-i-buy` in `ej-skills`. |
| **`plan-trip`** | `/plan-trip [destination]` | **High.** Verb-first imperative slash command. | **Medium-High.** Slightly narrower for users who already have a draft itinerary and want an *audit* or *stress test*. | Short (9 chars), but less natural when the user is asking *"Is my itinerary too packed?"*. |
| **`itinerary-check`** | `/itinerary-check` | **Medium-High.** Strong audit framing (mirrors `fact-check`). | **Narrower.** Implies an itinerary already exists rather than building one from scratch. | Better treated as a primary trigger branch inside `trip-planner` than the sole top-level name. |

#### B. Blueprint: 6-Step Stress-Tested Trip Planning Protocol

1. **Scope, Context & Hard-Constraint Gate (Hägerstrand + Pu & Chen):**
   - Check optional `traveler-profile.md` (if present) and the user's request against the **5 Verdict-Flipping Variables** (Dates/Duration/Anchors, Party/Mobility/Luggage, Budget/Style, Priorities/Anti-Goals, Passport/Dietary/Medical Constraints).
   - *Completion Criterion:* Either all 5 verdict-flipping variables are bounded, or 2–4 high-leverage questions have been asked (paired with any immediate knockout warnings) before locking in the final day-by-day plan.
2. **Logistics, Authority & Environmental Knockout Gate (Timatic + Schengen Art. 6 + CDC Yellow Book):**
   - Audit passport validity (including the **Schengen 10-year issue date + 3-month post-departure rule** and 6-month rules), visa/ETA/ETIAS lead times, IDP convention requirements (1949 vs. 1968), vaccination/medication import rules, high-altitude acclimatization thresholds ($>2,500\text{ m}$), seasonal weather hazards, and macro-holidays/strikes.
   - *Completion Criterion:* Every regulatory, seasonal, and physiological hard constraint has been verified and passed, or flagged as an immediate blocker with exact remediation steps.
3. **Spatial Clustering, Base Selection & True Nightly Cost Audit (TTDP + FTC 16 CFR 464):**
   - Group candidate POIs into contiguous **walkable geographic clusters** per day, minimize **1-night hotel hops** (accounting for the 2.5–4.5 hr Hotel Change Tax), and evaluate base neighborhoods using **True Location-Adjusted Nightly Cost** ($C_{\text{night, true}}$ including mandatory resort/cleaning/city taxes + transit fares + commute time penalty).
   - *Completion Criterion:* Base accommodations and daily zones are geographically clustered to eliminate cross-city zig-zagging, and hotel/base comparisons show full location-adjusted nightly cost and commute trade-offs.
4. **Door-to-Door Transit Math & Connection Risk Engineering (TCRP Report 165 + IATA Res. 765 + Buehler):**
   - Decompose every intercity and airport/station transfer into full **Door-to-Door time ($T_{\text{D2D}}$)** with outside-view friction buffers ($+25\text{–}35\%$ urban navigation; $P_{95}$ terminal buffers).
   - Distinguish **Single-PNR Protected Connections** ($\ge 1.5\times \text{MCT}$ for critical legs) from **Unprotected Self-Transfers** (requiring overnight arrival or 4–6+ hr buffers).
   - *Completion Criterion:* Every transit leg specifies realistic Door-to-Door elapsed time, luggage handling plan, transfer count, and connection protection status.
5. **Cognitive Pacing, Anti-Tourist-Trap Vetting & Time-Window Sequencing (Peak-End + Kaplan ART + MacCannell):**
   - Cap each half-day (Morning / Afternoon / Evening) at **1 Fixed Anchor + 1 Flexible Option**, alternate **High-Cognitive-Load** stops with **Restorative (Soft Fascination)** stops, adjust Days 1–2 for **Jet-Lag Directionality** ($1.0\text{ d/zone}$ West vs. $1.5\text{ d/zone}$ East), and protect the **Final 24 Hours**.
   - Verify exact **day-of-week opening/closing and last-entry hours** (checking Monday/Tuesday museum closures) and vet dining/activities against **native regional sources** (Tabelog, Slow Food, Le Fooding, Sol Repsol, Naver/Kakao, Bib Gourmand) plus the **3-Block Repeat-Local Rule**.
   - *Completion Criterion:* No half-day exceeds the 1 Anchor + 1 Flexible cap, every fixed stop lists verified day-of-week operating hours, and dining/activity picks cite anti-tourist-trap rationale.
6. **Travel Premortem, Fallback Matrix & Calibrated Readiness Verdict (Klein + Booking Timeline):**
   - Run a **Travel Premortem** across weather, transit/strike, queue/sellout, and low-energy failure modes, attaching concrete **If/Then Pivots** to each day.
   - Assign one of the 6 calibrated verdicts (**`Ready to Book`**, **`Viable With Adjustments`**, **`Cut Stops / Slow Down`**, **`Reroute / Change Base`**, **`Shift Season / Dates`**, or **`Do Not Book As Planned`**), provide a chronological **Advance Booking Action Timeline** (90/60/30/7 days out), and state explicit **Reversal Conditions**.
   - *Completion Criterion:* The output delivers an unambiguous readiness verdict, a complete stress-tested itinerary or audit table, explicit If/Then rain/fatigue pivots, a phased booking checklist, and falsifiable reversal conditions.

---

## References & Primary Sources

1. **Hägerstrand, T. (1970):** *"What about people in Regional Science?"*, *Papers of the Regional Science Association*, 24(1), 6–21. [https://doi.org/10.1007/BF01936872](https://doi.org/10.1007/BF01936872) | [https://doi.org/10.1111/j.1435-5597.1970.tb01464.x](https://doi.org/10.1111/j.1435-5597.1970.tb01464.x)
2. **Vansteenwegen, P., & Van Oudheusden, D. (2007):** *"The Mobile Tourist Guide: An OR Opportunity"*, *OR Insight*, 20(3), 21–27. [https://doi.org/10.1057/ori.2007.17](https://doi.org/10.1057/ori.2007.17)
3. **Vansteenwegen, P., Souffriau, W., & Van Oudheusden, D. (2011):** *"The orienteering problem: A survey"*, *European Journal of Operational Research*, 209(1), 1–10. [https://doi.org/10.1016/j.ejor.2010.03.045](https://doi.org/10.1016/j.ejor.2010.03.045)
4. **Gavalas, D., Konstantopoulos, C., Mastakas, K., & Pantziou, G. (2014):** *"A survey on algorithmic approaches for solving tourist trip design problems"*, *Journal of Heuristics*, 20(3), 291–328. [https://doi.org/10.1007/s10732-014-9242-5](https://doi.org/10.1007/s10732-014-9242-5)
5. **Xie, J., Zhang, K., Chen, J., Zhu, T., Lou, R., Tian, Y., Xiao, Y., & Su, Y. (2024):** *"TravelPlanner: A Benchmark for Real-World Planning with Language Agents"*, *Proceedings of the 41st International Conference on Machine Learning (ICML 2024)*, PMLR 235, 54590–54613. [https://arxiv.org/abs/2402.01622](https://arxiv.org/abs/2402.01622)
6. **Transportation Research Board (TRB) (2013):** *Transit Capacity and Quality of Service Manual (TCQSM)*, 3rd Edition, **TCRP Report 165**, National Academies Press. [https://doi.org/10.17226/24766](https://doi.org/10.17226/24766)
7. **Wardman, M. (2004):** *"Public transport values of time"*, *Transport Policy*, 11(4), 363–377. [https://doi.org/10.1016/j.tranpol.2004.05.001](https://doi.org/10.1016/j.tranpol.2004.05.001)
8. **Wardman, M. (2001):** *"A review of British evidence on time and service quality valuations"*, *Transportation Research Part E: Logistics and Transportation Review*, 37(2–3), 107–128. [https://doi.org/10.1016/S1366-5545(00)00012-0](https://doi.org/10.1016/S1366-5545(00)00012-0)
9. **Kahneman, D., & Tversky, A. (1979):** *"Intuitive prediction: Biases and corrective procedures"*, *TIMS Studies in Management Science*, 12, 313–327 (reprinted in *Judgment under Uncertainty: Heuristics and Biases*, Cambridge University Press, 1982). [https://doi.org/10.1017/CBO9780511809477.031](https://doi.org/10.1017/CBO9780511809477.031)
10. **Buehler, R., Griffin, D., & Ross, M. (1994):** *"Exploring the 'planning fallacy': Why people underestimate their task completion times"*, *Journal of Personality and Social Psychology*, 67(3), 366–381. [https://doi.org/10.1037/0022-3514.67.3.366](https://doi.org/10.1037/0022-3514.67.3.366)
11. **International Air Transport Association (IATA):** *Resolution 765 (Interline Connecting Time Intervals – Passenger and Checked Baggage)* & *Standard Schedules Information Manual (SSIM) Chapter 8: Minimum Connecting Time (MCT)*. [https://www.iata.org/en/services/data/timetables/mct/](https://www.iata.org/en/services/data/timetables/mct/)
12. **European Union:** *Regulation (EC) No 261/2004 establishing common rules on compensation and assistance to passengers in the event of denied boarding and of cancellation or long delay of flights* ([https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0261](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0261)) & *Regulation (EU) 2021/782 on rail passengers' rights and obligations* ([https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021R0782](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021R0782)).
13. **U.S. Department of Transportation (DOT) (2024):** *Refunds and Other Consumer Protections*, **14 CFR Part 260**. [https://www.ecfr.gov/current/title-14/chapter-II/subchapter-A/part-260](https://www.ecfr.gov/current/title-14/chapter-II/subchapter-A/part-260)
14. **Fredrickson, B. L., & Kahneman, D. (1993):** *"Duration neglect in retrospective evaluations of affective episodes"*, *Journal of Personality and Social Psychology*, 65(1), 45–55. [https://doi.org/10.1037/0022-3514.65.1.45](https://doi.org/10.1037/0022-3514.65.1.45)
15. **Kemp, S., Burt, C. D. B., & Furneaux, L. (2008):** *"A test of the peak-end rule with extended autobiographical events"*, *Memory & Cognition*, 36(1), 132–138. [https://doi.org/10.3758/MC.36.1.132](https://doi.org/10.3758/MC.36.1.132)
16. **Gilman, B. I. (1916):** *"Museum Fatigue"*, *The Scientific Monthly*, 2(1), 62–74. [https://www.jstor.org/stable/6127](https://www.jstor.org/stable/6127)
17. **Melton, A. W. (1935):** *Problems of Installation in Museums of Art*, Publications of the American Association of Museums, New Series, No. 14. [https://catalog.hathitrust.org/Record/001157268](https://catalog.hathitrust.org/Record/001157268)
18. **Bitgood, S. (2009):** *"Museum Fatigue: A Critical Review"*, *Visitor Studies*, 12(2), 93–111. [https://doi.org/10.1080/10645570903203406](https://doi.org/10.1080/10645570903203406)
19. **Kaplan, S. (1995):** *"The restorative benefits of nature: Toward an integrative framework"*, *Journal of Environmental Psychology*, 15(3), 169–182. [https://doi.org/10.1016/0272-4944(95)90001-2](https://doi.org/10.1016/0272-4944%2895%2990001-2)
20. **Waterhouse, J., Reilly, T., Atkinson, G., & Edwards, B. (2007):** *"Jet lag: trends and coping strategies"*, *The Lancet*, 369(9567), 1117–1129. [https://doi.org/10.1016/S0140-6736(07)60529-7](https://doi.org/10.1016/S0140-6736%2807%2960529-7)
21. **U.S. Centers for Disease Control and Prevention (CDC):** *CDC Yellow Book: Health Information for International Travel* — *Jet Lag Disorder* ([https://www.cdc.gov/yellow-book/hcp/travel-by-air-and-sea/jet-lag-disorder.html](https://www.cdc.gov/yellow-book/hcp/travel-by-air-and-sea/jet-lag-disorder.html)) & *High-Altitude Travel and Altitude Illness* ([https://www.cdc.gov/yellow-book/hcp/environmental-hazards-risks/high-altitude-travel-and-altitude-illness.html](https://www.cdc.gov/yellow-book/hcp/environmental-hazards-risks/high-altitude-travel-and-altitude-illness.html)).
22. **European Union (2016):** *Regulation (EU) 2016/399 on a Union Code on the rules governing the movement of persons across borders (Schengen Borders Code)*, Article 6(1)(a). [https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0399](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0399)
23. **World Health Organization (WHO) (2005):** *International Health Regulations (IHR)*, 3rd Edition, Annex 6 & Annex 7. [https://www.who.int/publications/i/item/9789241580496](https://www.who.int/publications/i/item/9789241580496)
24. **MacCannell, D. (1973):** *"Staged Authenticity: Arrangements of Social Space in Tourist Settings"*, *American Journal of Sociology*, 79(3), 589–603. [https://doi.org/10.1086/225585](https://doi.org/10.1086/225585)
25. **Akerlof, G. A. (1970):** *"The Market for 'Lemons': Quality Uncertainty and the Market Mechanism"*, *The Quarterly Journal of Economics*, 84(3), 488–500. [https://doi.org/10.2307/1879431](https://doi.org/10.2307/1879431)
26. **Mayzlin, D., Dover, Y., & Chevalier, J. (2014):** *"Promotional Reviews: An Empirical Investigation of Online Review Manipulation"*, *American Economic Review*, 104(8), 2421–2455. [https://doi.org/10.1257/aer.104.8.2421](https://doi.org/10.1257/aer.104.8.2421)
27. **Santana, S., Dallas, S. K., & Morwitz, V. G. (2020):** *"Consumer Reactions to Drip Pricing"*, *Marketing Science*, 39(1), 188–210. [https://doi.org/10.1287/mksc.2019.1207](https://doi.org/10.1287/mksc.2019.1207)
28. **U.S. Federal Trade Commission (FTC):** *Trade Regulation Rule on Unfair or Deceptive Fees* (**16 CFR Part 464**, [https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-464](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-464)), *Guides Concerning the Use of Endorsements and Testimonials in Advertising* (**16 CFR Part 255**, [https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255)), & *Trade Regulation Rule on the Use of Consumer Reviews and Testimonials* (**16 CFR Part 465**, [https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465)).
29. **Pu, P., & Chen, L. (2008):** *"User-Involved Preference Elicitation for Product Search and Recommender Systems"*, *AI Magazine*, 29(4), 93–103. [https://doi.org/10.1609/aimag.v29i4.2200](https://doi.org/10.1609/aimag.v29i4.2200)
30. **Chen, L., & Pu, P. (2012):** *"Critiquing-based recommenders: survey and emerging trends"*, *User Modeling and User-Adapted Interaction*, 22(1–2), 125–150. [https://doi.org/10.1007/s11257-011-9111-y](https://doi.org/10.1007/s11257-011-9111-y)
31. **Klein, G. (2007):** *"Performing a Project Premortem"*, *Harvard Business Review*, 85(9), 18–19. [https://hbr.org/2007/09/performing-a-project-premortem](https://hbr.org/2007/09/performing-a-project-premortem) | [https://doi.org/10.1109/EMR.2008.4534313](https://doi.org/10.1109/EMR.2008.4534313)
