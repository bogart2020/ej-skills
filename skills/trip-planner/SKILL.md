---
name: trip-planner
description: Plan stress-tested trips and day-by-day itineraries, audit draft itineraries for logistics, pacing, and closure traps, or compare flights, routes, hotels, and base neighborhoods on door-to-door time and true nightly cost.
license: MIT
---

# Trip Planner

Build or audit any itinerary and deliver one **readiness verdict** with the conditions that would change it.

## Environment adaptation

- **Chat** (Claude Desktop, web): check history, project instructions, memory, and attached bookings or screenshots for traveler context. To save preferences, output a copyable snippet following [`references/traveler-profile-template.md`](references/traveler-profile-template.md).
- **Code and CLI**: read `.agents/traveler-profile.md` or `~/.agents/traveler-profile.md` before asking questions. Use Python or shell for exact door-to-door budgets, true nightly cost, rail-pass break-even, and currency math. For **3 or more cities, candidate bases, or multi-week legs**, dispatch parallel verification subagents when the harness supports them, briefing each with the user's country and currency; handle 1 or 2 cities inline.

## Plain-language output

The bolded terms, formulas, and table's internal terms in this skill are your working vocabulary. Everything the user sees speaks everyday language a non-specialist understands on first read:

- Print the **user-facing label** from the table below wherever an internal term would appear.
- Show math as labeled plain arithmetic ("\$180 room + \$37 fees and taxes + \$20 taxis = \$237 a night"), never formulas or symbols.
- **Money**: never silently default to US dollars. Lead every cost, in tables and prose, with the user's currency and add the original in local currency when it differs ("₱2,850 (¥7,500)"). State one dated rate per currency from this session (or flag amounts approximate if none is current), and total budgets in the user's currency.
- Keep step, tier, and gate names internal: describe the work by what it does (*"checking your passport dates for Europe"*).
- Explain any unavoidable technical term (ETIAS, an IDP) in a short clause the first time it appears.

| Internal term | User-facing label |
| :--- | :--- |
| Verdict-flipping variables | The basics of your trip |
| True Location-Adjusted Nightly Cost | Real cost per night (with fees, taxes, and getting around) |
| Door-to-Door Transit | Door-to-door travel time |
| Hotel Change Tax | Time lost changing hotels |
| 1 Fixed Anchor + 1 Flexible Option | One main plan + one optional extra |
| Space-Time Prism | Fits between your fixed plans |
| Single-PNR / Self-Transfer | One booking (the airline rebooks you) / Separate tickets (a missed connection is on you) |
| MCT | The airport's minimum connection time |
| Travel Premortem / If/Then Fallback Triggers | What could go wrong / Plan B |
| 3-Block Rule / native vetting | Eat a few blocks away from the big sights / local review sites |
| Peak-End Rule / circadian resynchronization | Save the best for unhurried moments / jet-lag recovery |

## Interview rounds

Interview the user in rounds before researching, so the plan fits their real trip.

1. Ask at least one round on every run. Skip only when the user says "just answer", "no questions", or equivalent; then state your assumptions in one line at the top of the report.
2. The **frontier** is every open question whose prerequisites are settled. Ask the whole frontier in one round, number each question, give your recommended answer, and word it so "yes" accepts the recommendation. Then stop and wait.
3. Find facts yourself (web search, bookings, traveler profile, history, memory). Ask only for decisions, preferences, and facts only the user knows. Never ask about anything the user already stated; turn what you only inferred into a quick confirmation.
4. Recompute the frontier after each answer. A question that depends on another open question belongs to a later round.
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

- **Before each of Steps 2 to 5**, read the matching section of [`references/planning-rules.md`](references/planning-rules.md) for exact entry rules, cost and transit formulas, buffers, and pacing thresholds.
- **When the trip matches a domain below**, read that section of [`references/destination-and-mode-playbooks.md`](references/destination-and-mode-playbooks.md): native food and activity vetting, urban and multi-city rail, road trips and ferries, high altitude and extreme climates, family and accessible travel, or complex air routing and self-transfers.
- **Before Step 6**, read [`references/report-format.md`](references/report-format.md) for the report sections.
- **When saving a profile**, read [`references/traveler-profile-template.md`](references/traveler-profile-template.md).

## Proportional rigor

- **Short hop** (1 to 3 nights, one domestic or regional base, no visa or jet lag): verify weekday hours and holidays, cluster by walkable neighborhood, apply the half-day cap, and vet dining locally in a concise plan.
- **Standard** (4 to 10 nights, 1 to 3 bases, or international short/medium haul): run all 6 steps.
- **Complex expedition** (10+ nights, multi-country, 5+ time zones, separate-ticket connections, altitude above 2,500 m, or multi-generational/accessibility needs): add jet-lag scheduling for Days 1 to 3, graded altitude profiles, connection-failure planning, luggage forwarding, and a 90/60/30/7-day booking timeline.

## Planning and audit sequence

Run these six steps in order.

### Step 1: Load traveler context and interview the user

1. Check the traveler profile, memory, prior turns, and cues (₱, a home airport; with none, ask without suggesting one) for passport nationality and validity, home country and currency, home hub, walking ceiling, luggage style, dietary/medical rules, and past trip lessons.
2. Settle the **5 verdict-flipping variables**:
   - **Dates and anchors**: exact dates or season, nights on the ground, and inbound/outbound times.
   - **Party, mobility, and luggage**: who is traveling (solo, couple, stroller, seniors), realistic daily walking, carry-on vs. heavy checked bags.
   - **Budget and transit style**: nightly or total ceiling in their home currency, public transit vs. car or private transfers, preferred neighborhood pace.
   - **Peaks and anti-goals**: the top 2 to 3 experiences, and explicit dislikes (crowded checklist museums, pre-9:00 AM starts, 1-night hotel hops).
   - **Entry, medical, and dietary knockouts**: passport nationality and issue/expiry dates, severe allergies or dietary laws, altitude or heat sensitivity.
3. Run **Interview rounds** on these in everyday words, raising any date, visa, or safety warning you can already see in the first round.

**Completion criterion**: The user has confirmed all 5 variables (or opted out, with assumptions stated).

### Step 2: Clear the entry, health, weather, and calendar gate

Using `references/planning-rules.md` section 1, check passport validity (Schengen 10-year issue and 3-month rule, 6-month rule elsewhere), visas and e-authorizations with lead times, driving permits, vaccination and medication bans, altitude above 2,500 m, weather extremes, holidays and strikes, and attractions that sell out 30 to 90+ days ahead.

**Completion criterion**: Every passport, visa/ETA, IDP, health/medication, altitude, weather, holiday, and advance-ticket item is verified against primary sources and either cleared or flagged as a blocker with exact remediation steps.

### Step 3: Cluster geography, choose bases, and compute true nightly cost

Using `references/planning-rules.md` section 2: group stops into walkable clusters, price every hotel change in lost hours and turn short 1-night hops into day trips, and compare bases on all-in nightly cost including fees, taxes, parking, and getting around.

**Completion criterion**: Stops form contiguous clusters, 1-night hops are pruned or justified, and base comparisons show true nightly cost in the user's currency alongside daily commute time.

### Step 4: Compute door-to-door transit and connection buffers

Using `references/planning-rules.md` section 3: build every leg from door to door (never in-vehicle time alone), add +25% to +35% (minimum 15 minutes) to app estimates, check each optional stop fits between fixed plans, and classify every connection as one booking (at least 1.5x the minimum connection time) or separate tickets (arrive the evening before long-haul or anchor events, or 4 to 6 hours for short-haul).

**Completion criterion**: Every transfer and daily leg states its full door-to-door time with buffers, fits between fixed plans, specifies luggage handling, and classifies each flight/rail connection with a compliant buffer.

### Step 5: Pace each day, check hours, and vet for tourist traps

Using `references/planning-rules.md` section 4: cap each half-day at 1 main plan + 1 optional extra in the same cluster, alternate demanding and restful stops, pace jet lag on Days 1 to 2 and keep the final 24 hours light in the departure hub, label every day with its weekday and check opening hours, weekly closures, and last entry, and vet food and shopping 3 to 6 blocks from landmarks against native regional guides.

**Completion criterion**: Every half-day respects the cap and alternates load, Days 1 to 2 and the final 24 hours follow jet-lag and peak-end pacing, every fixed stop lists verified weekday hours and last entry, and dining picks cite native vetting or the 3-Block Rule.

### Step 6: Run the premortem and deliver the verdict

1. **Premortem**: assume 1 to 2 days went badly wrong and attach an If/Then Plan B for each:
   - **Weather**: indoor or shaded swaps in the same cluster for rain, storms, heat above 35°C, or zero visibility.
   - **Transit or strike**: backup mode, last viable return of the evening, luggage forwarding.
   - **Queue or lockout**: a pre-vetted nearby alternative if lines exceed 45 minutes or a lottery is missed.
   - **Low energy or sick day**: dropping any half-day's optional extra leaves all hotel transfers and fixed bookings intact.
   - **Refunds**: free-cancellation dates, fare refundability vs. credit expiry, and insurance or card coverage for non-refundable anchors.
2. **Verdict and report**: pick one label from the **Verdict table** for the plan as the user gave it (a knockout in it means `Do Not Book As Planned`, even when your revision fixes it), print it word for word, and write the report in plain language using `references/report-format.md`.

**Completion criterion**: The report gives one verdict, verified before-you-go checks, a day-by-day plan by area with door-to-door times and a Plan B per half-day, a booking checklist by lead time, and the exact conditions that would change the verdict, with every internal term replaced by its user-facing label.

## Verdict table

| Verdict | When to assign |
| :--- | :--- |
| **`Ready to Book`** | Clears every entry, altitude, weather, and calendar check; respects the half-day cap and fixed-plan windows; uses realistic door-to-door times and buffers; no unprotected single point of failure. |
| **`Viable With Adjustments`** | Sound destination, dates, and bases, with 1 to 3 pacing, closure-day, ordering, or buffer flaws fixed in the revised plan. |
| **`Cut Stops / Slow Down`** | Too many cities for the nights, more than 35% of waking hours in transit, or back-to-back high-fatigue anchors; prune detours or consolidate bases. |
| **`Reroute / Change Base`** | The chosen base, hotel, or route loses on true nightly cost, walkability, or connection reliability (a remote budget-lodging trap, a tight unprotected self-transfer). |
| **`Shift Season / Dates`** | Dates hit monsoon, typhoon, or extreme heat, holiday shutdowns or surges (Golden Week, Lunar New Year, *Ferragosto*), or seasonal closures that block the main goals. |
| **`Do Not Book As Planned`** | Fails a hard entry or physical knockout: passport fails the Schengen or 6-month rule, too little visa/ETA lead time, unsafe ascent above 2,500 m, or an impossible connection. Hold every booking, timed tickets included, until the blocker clears. |

## Guardrails

1. **Verified facts only**: never invent routes, timetables, hours, or prices from memory. Verify current hours, closure days, entry rules, and transit times in-session, and state the source and date on time-sensitive facts.
2. **Official portals**: link visas, e-authorizations, rail tickets, and timed entry to the official government or venue site, never resellers.
3. **No sycophantic pacing**: when a draft is overpacked, quantify the hotel-change time and transit share of waking hours first, assign `Cut Stops / Slow Down`, and show a consolidated alternative with its trade-offs.
