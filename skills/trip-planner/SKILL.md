---
name: trip-planner
description: Plan stress-tested trips and day-by-day itineraries, audit draft itineraries for logistics, pacing, and closure traps, or compare flights, routes, hotels, and base neighborhoods on door-to-door time and true nightly cost.
argument-hint: "[destination, dates/duration, draft itinerary, or flight/hotel/neighborhood comparison]"
license: MIT
---

# Trip Planner

Build or audit any travel itinerary by interviewing the user on the **5 verdict-flipping variables**, clearing the **Logistics and Entry Knockout Gate**, clustering stops around bases scored by **True Location-Adjusted Nightly Cost ($C_{\text{night, true}}$)**, computing realistic **Door-to-Door Transit ($T_{\text{D2D}}$)** and connection buffers, enforcing **1 Fixed Anchor + 1 Flexible Option per half-day** with native **anti-tourist-trap vetting**, running a **Travel Premortem**, and delivering a calibrated **readiness verdict** with explicit **reversal conditions**.

## Environment adaptation

Adapt tool use and memory discovery to the active runtime:

- **Chat environment** (Claude Desktop, web chat): inspect conversation history, project instructions, built-in memory, and any attached bookings or screenshots for traveler context. Run web searches to verify consular entry rules, operating hours, weekly closure days, live transit durations, and local dining directories. When the user wants to save their traveler preferences or trip post-mortem, output a copyable Markdown snippet following [`references/traveler-profile-template.md`](references/traveler-profile-template.md).
- **Code and CLI environment** (Claude Code, Codex, Antigravity, Gemini CLI, Cursor, Windsurf): check whether `.agents/traveler-profile.md` or `~/.agents/traveler-profile.md` exists and read it before asking questions. Use Python or shell (`python3 -c ...`) for exact $T_{\text{D2D}}$ time budgets, $C_{\text{night, true}}$ comparisons, rail-pass break-even math, and currency conversions. When auditing or planning across **3 or more cities, candidate base neighborhoods, or multi-week legs** in a harness that supports subagents, dispatch parallel verification subagents so raw search pages stay out of the main context window; handle 1 or 2 cities inline.

## Plain-language output

The bolded terms and formulas in this skill ($C_{\text{night, true}}$, $T_{\text{D2D}}$, Hotel Change Tax, Fixed Anchor, Space-Time Prism, Single-PNR, MCT, IRROPs, premortem, Peak-End Rule) are your working vocabulary. Everything the user sees, including interview questions and the report, speaks everyday language a non-specialist understands on first read:

- Print the **user-facing label** from the table below wherever an internal term would appear.
- Show math as labeled plain arithmetic ("\$180 room + \$25 resort fee + \$12 city tax + \$20 taxis = \$237 a night") rather than formulas or symbols.
- Keep step, tier, and gate names from this skill internal: describe the work by what it does (*"checking your passport dates for Europe"*, not *"Step 2 Logistics and Entry Knockout Gate"*).
- When a technical term is unavoidable (ETIAS, an IDP), explain it in a short clause the first time it appears.

| Internal term | User-facing label |
| :--- | :--- |
| Verdict-flipping variables | The basics of your trip |
| Logistics and Entry Knockout Gate | Before-you-go checks (passport, visa, permits, health, weather, holidays) |
| $C_{\text{night, true}}$ / True Location-Adjusted Nightly Cost | Real cost per night (with fees, taxes, and getting around) |
| $T_{\text{D2D}}$ / Door-to-Door Transit | Door-to-door travel time |
| Hotel Change Tax | Time lost changing hotels |
| 1 Fixed Anchor + 1 Flexible Option | One main plan + one optional extra |
| Space-Time Prism | Fits between your fixed plans |
| Single-PNR / Self-Transfer | One booking (the airline rebooks you) / Separate tickets (a missed connection is on you) |
| MCT | The airport's minimum connection time |
| IRROPs | Delays and cancellations |
| Travel Premortem / If/Then Fallback Triggers | What could go wrong / Plan B |
| 3-Block Rule / native vetting | Eat a few blocks away from the big sights / local review sites |
| Peak-End Rule / circadian resynchronization | Save the best for unhurried moments / jet-lag recovery |

## Interview rounds

Interview the user in rounds before researching, so the plan fits their real trip rather than a generic traveler.

1. Ask at least one round on every run. Skip the interview only when the user explicitly says "just answer", "no questions", or equivalent; then state your assumptions in one line at the top of the report.
2. The **frontier** is every open question whose prerequisites are already settled. Ask the whole frontier in one round, number each question, give your recommended answer, and word each question so "yes" accepts your recommendation. Then stop and wait for the user's answers.
3. Find facts yourself (web search, attached bookings, traveler profile, conversation history, memory). Ask the user only for decisions, preferences, and facts only they know. When existing context already answers a question, turn it into a quick confirmation with that answer as your recommendation.
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

- **Destination and mode playbooks**: Before running Steps 2 through 5, read the matching sections in [`references/destination-and-mode-playbooks.md`](references/destination-and-mode-playbooks.md):

| Trip archetype or domain | What `references/destination-and-mode-playbooks.md` provides |
| :--- | :--- |
| **Native anti-tourist-trap and culinary vetting** | Regional local directories (Tabelog, Slow Food, Le Fooding, Guía Repsol, Naver/KakaoMap, Dianping, Bib Gourmand), rating calibration, and 3-Block Rule checks |
| **Urban and multi-city rail itineraries** | Rail-pass break-even math, luggage forwarding (*Takkyubin* / SBB), station labyrinth buffers, Monday/Tuesday museum closure checks, 30-to-90-day ticket lotteries |
| **Road trips, rental vehicles, and island ferries** | 1949 Geneva vs. 1968 Vienna IDP rules, ZTL/congestion camera traps, CDW/LDW coverage, overnight parking costs, and ferry misconnection buffers |
| **High-altitude, trekking, and extreme climates** | CDC Yellow Book $>2,500\text{ m}$ graded ascent and *climb high, sleep low* rules, heatwave/wet-bulb midday siesta blocks, and seasonal pass/monsoon shutdowns |
| **Family, multi-generational, and accessible travel** | Step-free station routing, cobblestone/stair walk multipliers ($w_{\text{walk}} = 3.0\text{ to }4.0\times$), nap-window anchoring, and split-party flexible blocks |
| **Complex air routing and self-transfers** | Single-PNR ($\ge 1.5\times \text{MCT}$) vs. separate-ticket overnight/4-to-6 hour buffers, cruise/event positioning rules, and EC 261 / US DOT 14 CFR Part 260 rights |

- **Persistent traveler profile**: When creating or updating `.agents/traveler-profile.md` or `~/.agents/traveler-profile.md` in Step 6, read [`references/traveler-profile-template.md`](references/traveler-profile-template.md).

## Proportional rigor

Scale verification depth and quantitative math to the trip's complexity:

- **Short-hop tier** (1 to 3 nights, single domestic or regional base, no border visa or jet lag): verify day-of-week opening hours and local holidays, cluster stops by walkable neighborhood, apply the `1 Fixed Anchor + 1 Flexible Option` half-day cap, and vet dining via local sources in a concise plan.
- **Standard multi-day tier** (4 to 10 nights, 1 to 3 bases, or international short/medium-haul): run the full 6-step sequence including the Consular and Entry Gate, True Location-Adjusted Nightly Cost ($C_{\text{night, true}}$), Door-to-Door transit math ($T_{\text{D2D}}$) with the Hotel Change Tax, native anti-tourist-trap vetting, and If/Then weather and low-energy pivots.
- **Complex expedition tier** (10+ nights, multi-country, long-haul crossing $\ge 5$ time zones, separate-ticket connections, high altitude $>2,500\text{ m}$, or multi-generational/accessibility constraints): add circadian resynchronization scheduling on Days 1 to 3, graded altitude acclimatization profiles, connection failure and IRROPs engineering, luggage-forwarding logistics, and a phased 90/60/30/7-day Booking Action Timeline.

## Planning and audit sequence

Run these six steps in order.

### Step 1: Load traveler context and interview the user

1. **Check existing traveler context**: inspect `.agents/traveler-profile.md` or `~/.agents/traveler-profile.md` (when file tools exist) or platform memory and prior turns for passport nationality and validity, home hub, mobility/walking ceiling, luggage style, dietary/medical rules, and past trip post-mortems.
2. **Audit the 5 verdict-flipping variables**:
   - **Dates, duration, and arrival/departure anchors**: exact dates or season, nights on the ground, and inbound/outbound flight or train timestamps (which bound Day 1, the Final Day, weather, and holiday closures).
   - **Party composition, mobility, and luggage**: who is traveling (solo, couple, young children with stroller, seniors), realistic daily walking ceiling (km or steps), and carry-on versus heavy checked luggage.
   - **Budget tier and transit/base style**: nightly or total trip budget ceiling, public transit versus rental car or private transfers, and preferred base neighborhood pace.
   - **Peak priorities and hard anti-goals**: top 2 to 3 peak experiences to optimize for, alongside explicit anti-goals (such as skipping crowded checklist museums, avoiding pre-9:00 AM starts, or banning 1-night hotel hops).
   - **Authority, medical, and dietary knockouts**: passport nationality and issue/expiry dates for international trips, severe allergies or dietary laws, and high-altitude or heat sensitivities.
3. **Interview the user**: run **Interview rounds** on the 5 verdict-flipping variables, phrased in everyday words (for example, *"How much walking per day feels comfortable?"* rather than *"mobility ceiling"*). Variables already answered by traveler context become quick confirmations. Raise any date, visa, or safety warning you can already see in the first round.

**Completion criterion**: The user has confirmed all 5 verdict-flipping variables (or explicitly opted out of questions, with assumptions stated).

### Step 2: Clear the logistics, authority, and environmental knockout gate

Consult [`references/destination-and-mode-playbooks.md`](references/destination-and-mode-playbooks.md) and test the trip against hard regulatory, calendar, and physiological constraints:

1. **Passport and border entry rules**:
   - For **Schengen Area** trips, verify the dual rule under **Regulation (EU) 2016/399 Article 6(1)(a)**: the passport must be **(a) issued within the previous 10 years** on the date of entry AND **(b) valid for at least 3 months after the planned departure date**.
   - For all other international destinations, verify minimum passport validity (typically **6 months beyond entry/departure**), required blank visa pages (2 to 4 pages), and mandatory pre-departure digital authorizations or visas (**US ESTA**, **UK ETA**, **EU ETIAS**, **Canada eTA**, **Australia ETA**, **Korea K-ETA**, **India e-Visa**, or consular visas) with official government domains and lead times.
2. **Driving permits, health rules, and medication bans**:
   - When vehicle or scooter rental is in scope, verify whether the destination requires a **1949 Geneva Convention IDP** (1-year validity; strictly enforced in Japan, South Korea, Taiwan) or a **1968 Vienna Convention IDP** (3-year validity; continental Europe and others), issued in the traveler's home country before departure.
   - Verify mandatory vaccinations (**WHO IHR Yellow Fever** certificates) and strict national customs bans on common prescriptions (such as Japan's prohibition on amphetamine stimulants/Adderall and pseudoephedrine without advance import clearance, or UAE controlled-medication permits).
3. **High-altitude physiology and seasonal weather extremes**:
   - When sleeping or excursion elevations exceed **$2,500\text{ m}$ ($8,200\text{ ft}$)** (such as Cusco, La Paz, Lhasa, Leh, Quito, or alpine passes), apply **CDC Yellow Book** graded ascent rules: sleep at a lower intermediate elevation first when possible (for example, descending from Cusco Airport at $3,399\text{ m}$ to the Sacred Valley at $2,870\text{ m}$ for Nights 1 to 2), cap sleeping-elevation gains above $3,000\text{ m}$ at **$\le 500\text{ m}/day$** with an extra acclimatization night every $1,000\text{ m}$, and keep the first 24 to 48 hours light.
   - Check travel dates against monsoon, typhoon, hurricane, wildfire-smoke, extreme wet-bulb heat ($>35^\circ\text{C}$), and winter road/ferry closure windows.
4. **Macro-holidays, strikes, and advance-booking bottlenecks**:
   - Check dates against national shutdowns and crowd surges (Golden Week, Obon, and New Year in Japan; Lunar New Year across East/Southeast Asia; Ramadan and Eid; *Ferragosto* in Italy; Sunday commercial closures in DACH/Europe).
   - Flag attractions requiring **30 to 90+ day advance reservations or lotteries** so the user knows immediately whether tickets are still obtainable for their dates.

**Completion criterion**: Every passport, visa/ETA, IDP, health/medication, altitude ($>2,500\text{ m}$), weather, macro-holiday, and 30-to-90-day ticket bottleneck has been verified against primary sources and either cleared or flagged as an immediate blocker with exact remediation steps.

### Step 3: Cluster geography, select bases, and audit true nightly cost

1. **Cluster-first, route-second spatial grouping**:
   - Group candidate Points of Interest (POIs) into contiguous **walkable neighborhood clusters** or single-line transit corridors so each half-day stays inside one geographic zone and eliminates cross-city zig-zagging.
   - Verify state continuity: every day must start at the exact accommodation or hub where the prior night ended.
2. **Minimize the Hotel Change Tax**:
   - Price every base change at **2.5 to 4.5 hours of lost daytime utility** (packing, checkout, station access, line-haul, luggage storage/drop, check-in, unpacking). Convert 1-night hops into **hub-and-spoke day trips** or en-route luggage-forwarded stops whenever door-to-door one-way transit is under 90 minutes.
3. **Compute True Location-Adjusted Nightly Cost ($C_{\text{night, true}}$)**:
   - When comparing hotels, short-term rentals, or base neighborhoods, defeat drip pricing by computing the all-in daily cost:
     $$C_{\text{night, true}} = P_{\text{base}} + F_{\text{resort/dest}} + \frac{F_{\text{cleaning/platform}}}{N_{\text{nights}}} + T_{\text{occupancy/city}} + C_{\text{parking/ZTL}} + \Delta C_{\text{transit/taxi}} + v_{\text{vacation\_hour}} \cdot \Delta T_{\text{commute}}$$
   - Include base rate ($P_{\text{base}}$), mandatory resort/destination fees ($F_{\text{resort/dest}}$), cleaning/OTA fees amortized over $N_{\text{nights}}$, occupancy and per-person municipal tourist taxes ($T_{\text{occupancy/city}}$), overnight parking/ZTL fees ($C_{\text{parking/ZTL}}$), round-trip party transit/late-night taxi fares ($\Delta C_{\text{transit/taxi}}$), and the opportunity cost of daily extra commuting hours ($v_{\text{vacation\_hour}} \cdot \Delta T_{\text{commute}}$) plus the ability to return midday for a 20-minute rest.

**Completion criterion**: Daily stops are grouped into contiguous geographic clusters with unbroken night-to-morning location continuity, 1-night hotel hops are pruned or justified, and base comparisons report $C_{\text{night, true}}$ alongside daily commute time.

### Step 4: Compute door-to-door transit math and engineer connection buffers

1. **Decompose full Door-to-Door elapsed time ($T_{\text{D2D}}$)**:
   - Never schedule using line-haul in-vehicle time ($T_{\text{in-vehicle}}$) alone. Compute:
     $$T_{\text{D2D}} = T_{\text{checkout/pack}} + T_{\text{access}} + T_{\text{terminal/security}} + T_{\text{wait/headway}} + T_{\text{in-vehicle}} + \sum_{k=1}^{K} T_{\text{transfer}, k} + T_{\text{baggage/customs}} + T_{\text{egress}} + T_{\text{checkin/drop}} + T_{\text{buffer}}$$
2. **Apply outside-view friction buffers and transfer penalties**:
   - Add **$+25\%$ to $+35\%$** (minimum **$+15\text{ minutes}$**) to mapping-app urban transit and walking estimates for station labyrinth navigation, ticketing, elevators, and rest stops.
   - Weight out-of-vehicle walking, waiting, and transfers at **$2.0\times$ to $2.5\times$** in-vehicle time (**$3.0\times$ to $4.0\times$** with luggage, strollers, cobblestones, or stairs) plus a **10 to 25 minute equivalent penalty per transfer**. Prefer a slightly longer direct train or bus over a multi-transfer route when carrying bags.
   - Target arrival **20 to 30 minutes before** non-refundable timed-entry cutoffs, and apply **$P_{95}$ terminal arrival buffers** for flights (2 hours domestic, 3 hours international) and high-speed rail (30 to 45 minutes).
3. **Verify Space-Time Prism feasibility**:
   - Between fixed coupling anchors $A$ (ending at $t_1$) and $B$ (starting at $t_2$), include an intermediate stop $k$ with realistic visit dwell time $d_k$ only when:
     $$t_1 + T_{\text{D2D}}(A, k) + d_k + T_{\text{D2D}}(k, B) \le t_2$$
4. **Audit Single-PNR versus Separate-Ticket ("Self-Transfer") connection risk**:
   - **Protected Single-PNR / Interline tickets**: verify that layovers exceed bare legal IATA Minimum Connecting Time (**target $\ge 1.5\times \text{MCT}$**: 90 to 120 minutes domestic, 120 to 180 minutes international/customs) whenever missing the connection would strand the party overnight.
   - **Unprotected Separate Tickets (Self-Transfers)**: flag that a delay on Leg 1 triggers a **100% no-show cancellation** of onward long-haul flights or cruises with zero carrier duty of care. Mandate **arriving the evening before (overnight buffer)** prior to any long-haul flight, cruise embarkation, or wedding/anchor event, or a **minimum 4 to 6 hour buffer** for short-haul self-transfers where rebooking is cheap and frequent.

**Completion criterion**: Every intercity transfer and daily transit leg states its full $T_{\text{D2D}}$ time including outside-view buffers, satisfies the Space-Time Prism inequality, specifies luggage handling, and classifies every flight/rail connection as Protected Single-PNR or Unprotected Self-Transfer with compliant buffer margins.

### Step 5: Enforce cognitive pacing, time windows, and anti-tourist-trap vetting

1. **Cap half-days at 1 Fixed Anchor + 1 Flexible Option**:
   - Divide each day into **Morning**, **Afternoon**, and **Evening** blocks.
   - Schedule at most **1 Fixed/High-Cognitive-Load Anchor** (such as a major museum, historical monument, or timed tour, capped at **90 to 120 minutes** of focused exhibit viewing to prevent museum fatigue) plus **1 Optional/Flexible Low-Load Activity** in the same neighborhood cluster per half-day.
2. **Alternate cognitive modalities (Attention Restoration Theory)**:
   - Pair every High-Directed-Attention stop with a restorative **Soft Fascination** stop (park, waterfront, botanical garden, architectural stroll, neighborhood market, or unhurried café/thermal bath) rather than scheduling two dense museums or archaeological sites back-to-back.
3. **Adjust Days 1 to 2 for circadian directionality and protect the Final 24 Hours**:
   - When crossing $\ge 5$ time zones, pace resynchronization at **$1.0\text{ day per time zone}$ westward** and **$1.5\text{ days per time zone}$ eastward**. Keep Arrival Day free of high-stakes timed tickets or rental-car driving; schedule outdoor daylight exposure and a light neighborhood walk. For **eastward** trips, start Days 1 to 2 anchors at **10:30 AM or later**; for **westward** trips, use natural early waking (7:00 AM to 8:30 AM) for uncrowded outdoor sights and keep evenings early.
   - Apply the **Peak-End Rule**: position the trip's highest-priority experiences as unhurried Peaks, and keep the **Final 24 Hours** in the departure hub city with light packing and zero long-distance transfer stress.
4. **Verify day-of-week operating and last-entry windows**:
   - Annotate every day with its explicit **day of the week** (`Mon`, `Tue`, etc.) and check each POI satisfies $O_{im} \le s_{im} \le L_{im} \le C_{im} - d_i$, accounting for Monday closures (such as Musée d'Orsay, Versailles, Uffizi) versus Tuesday closures (such as the Louvre, Prado, Musée Rodin), seasonal early dusk, and last-entry cutoffs (typically 30 to 60 minutes before closing).
5. **Run anti-tourist-trap vetting**:
   - Apply the **3-Block Repeat-Local Rule**: route dining and shopping **3 to 6 blocks away** from major-landmark perimeters, cruise terminals, and main station plazas into residential or office streets where venues compete for repeat local regulars.
   - Cross-check dining and activity picks against **native regional guides** listed in [`references/destination-and-mode-playbooks.md`](references/destination-and-mode-playbooks.md) (such as Tabelog $\ge 3.20\text{ to }3.50+$ in Japan, Slow Food *Osterie d'Italia* / Gambero Rosso in Italy, Le Fooding / *Fait Maison* in France, Guía Repsol *Soletes* in Spain, Naver/KakaoMap + Blue Ribbon in Korea, Dianping/OpenRice in China/HK/TW, and Michelin *Bib Gourmand*) rather than English-only SEO listicles or viral social media queues.

**Completion criterion**: Every half-day respects the `1 Fixed Anchor + 1 Flexible Option` cap and alternates cognitive load, Days 1 to 2 and the Final 24 Hours follow circadian and Peak-End pacing, every fixed stop lists verified day-of-week hours and last-entry cutoffs, and dining/activity recommendations cite native regional vetting or the 3-Block Rule.

### Step 6: Run the travel premortem and render the calibrated verdict

1. **Execute a 4-point Travel Premortem and Failure Audit**:
   - Assume the trip has concluded and 1 to 2 days went badly wrong. Audit and attach concrete **If/Then Fallback Triggers** for:
     - **Weather pivot**: indoor or shaded swaps in the same geographic cluster if rain, storms, extreme heat ($>35^\circ\text{C}$), or zero visibility strike an outdoor anchor.
     - **Transit or strike pivot**: backup transport mode, last viable return departure time of the evening, and luggage forwarding options.
     - **Queue or lockout pivot**: pre-vetted neighborhood alternative if walk-up lines exceed 45 minutes or a ticket lottery is missed.
     - **Low-energy or sick-day graceful degradation**: confirm that dropping any half-day's Flexible Option leaves all downstream hotel transfers and fixed reservations intact.
   - **Refundability and cancellation audit**: check free-cancellation cutoff dates on hotels/cars, airline fare refundability versus credit expiry, and travel insurance or credit-card coverage for non-refundable anchors.
2. **Assign one calibrated verdict and render the report in plain language**:
   - Select one label from the **Verdict taxonomy** below and present the report inline in the plain language set by **Plain-language output**, using four sections (plus an optional fifth save prompt when new durable context was learned):
     1. **Verdict & Bottom Line**:
        - **Verdict**: `[Ready to Book | Viable With Adjustments | Cut Stops / Slow Down | Reroute / Change Base | Shift Season / Dates | Do Not Book As Planned]`
        - **Bottom line**: 2 to 3 decisive sentences stating the verdict, the main routing or pacing reason, and any blocker or cost surprise.
        - **Before-you-go checks**: a table with the status of passport dates, visa or entry permit, driving permit, health and altitude rules, weather, and holidays or closures.
        - **Where to stay** (when choosing bases, hotels, or routes): a side-by-side table across Room Rate, Required Fees & Taxes, Daily Getting-Around Cost, Daily Commute Time, Real Cost per Night, and Walkability & Feel.
     2. **Day by Day**:
        - Head each day with **Day N (weekday, date) | where you're staying | area of town**.
        - Show **Morning**, **Afternoon**, and **Evening**, each with one main plan (opening hours and last entry checked) plus one optional extra, every travel leg with its door-to-door time (how you get there, ride time, extra buffer, what to do with bags), where to eat nearby, and a one-line Plan B for bad weather or low energy in the same area.
     3. **What Could Go Wrong**:
        - **Connections**: whether each connection is on one booking or separate tickets, the layover against the airport's minimum connection time, and the riskiest points in the trip.
        - **Money at risk**: non-refundable bookings, free-cancellation deadlines, and gaps in insurance or card coverage.
        - **Likeliest problems**: the 2 to 3 likeliest ways this specific trip could go wrong and what the plan already does about each.
     4. **What to Book When, and What Would Change the Verdict**:
        - **Booking checklist**: bookings grouped into `90+ Days Out`, `60 to 30 Days Out`, `14 to 7 Days Out`, and `48 Hours / Walk-Up`, each linked to the official booking site.
        - **What would change the verdict**: exact conditions (for example, *"Switches from `Cut Stops / Slow Down` to `Ready to Book` if you add 3 nights or visit Nara as a day trip from Kyoto instead of moving hotels"*).
     5. **Save for Next Time (when applicable)**:
        - If the session revealed lasting traveler context (passport dates, home airport, daily walking limit, dietary or medical needs, or lessons from this trip), ask in one line whether to save it as the user's traveler profile for future trips (stored per **Environment adaptation**, following [`references/traveler-profile-template.md`](references/traveler-profile-template.md)).

**Completion criterion**: The report delivers a single unambiguous verdict from the 6-level taxonomy, verified before-you-go checks, a day-by-day plan grouped by area with door-to-door travel times and a Plan B per half-day, a booking checklist grouped by lead time, and exact conditions that would change the verdict, and it reads cleanly to a non-specialist with every internal term from **Plain-language output** replaced by its user-facing label.

---

## Reference rules

### Verdict taxonomy

| Verdict | When to assign |
| :--- | :--- |
| **`Ready to Book`** | Clears all consular, altitude, weather, and calendar gates; respects the `1 Fixed Anchor + 1 Flexible Option` half-day cap and Space-Time Prism bounds; uses realistic $T_{\text{D2D}}$ and connection buffers; and contains zero unprotected single-point-of-failure traps. |
| **`Viable With Adjustments`** | Sound destination, dates, and base structure, with 1 to 3 specific pacing, day-of-week closure, ordering, or buffer flaws that are directly corrected in the revised day-by-day schedule. |
| **`Cut Stops / Slow Down`** | Suffers from the **Checklist Maximization Trap** or excessive **Hotel Change Tax** (too many cities for the available nights, $>35\%$ of waking hours spent in transit/transfers, or back-to-back high-fatigue anchors); requires pruning low-yield detours or consolidating into fewer bases. |
| **`Reroute / Change Base`** | Selected neighborhood base, hotel, or transport routing is dominated on **True Location-Adjusted Nightly Cost ($C_{\text{night, true}}$)**, walkability, or connection reliability (such as a peripheral budget lodging trap or an unprotected tight self-transfer). |
| **`Shift Season / Dates`** | Target dates collide with severe monsoon, typhoon, or extreme wet-bulb heat windows, national holiday shutdowns/surges (Golden Week, Lunar New Year, *Ferragosto*), or seasonal road/ferry closures that block the user's primary objectives. |
| **`Do Not Book As Planned`** | Fails a hard **Authority or Physiological Knockout** (passport violates Schengen 10-year/3-month or 6-month rule, insufficient visa/ETA lead time, dangerous unacclimatized ascent $>2,500\text{ m}$, or a mathematically impossible door-to-door connection). |

### Logistics and verification guardrails

1. **Zero-teleportation and session-verified facts**: Never invent direct routes, timetables, opening hours, or prices from parametric memory. Verify current operating windows, weekly closure days, visa/entry rules, and transit durations via session searches, and state the source and date on time-sensitive facts.
2. **Official portals over third-party markups**: For visas, ETAs (ESTA, UK ETA, ETIAS), rail tickets, and monument timed entry (such as Alhambra, Uffizi, Louvre, Ghibli, Recreation.gov), link directly to the **official government or venue portal** rather than third-party reseller or scam markup sites.
3. **Anti-sycophancy pacing rule**: When a user presents an overpacked draft itinerary (*"We only have 5 days so we want to see Tokyo, Kyoto, Osaka, Hiroshima, and Hakone"*), quantify the exact **Hotel Change Tax** and **Door-to-Door Transit share of waking hours** first, assign `Cut Stops / Slow Down`, and show a high-utility consolidated alternative alongside the trade-offs.
