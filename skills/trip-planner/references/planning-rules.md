# Planning Rules for Steps 2 to 5

Exact thresholds, formulas, and checks behind Steps 2 to 5 of [`SKILL.md`](../SKILL.md). Read the matching section before running each step.

## Contents

1. Entry, permit, health, weather, and calendar gate (Step 2)
2. Geographic clustering and true nightly cost (Step 3)
3. Door-to-door transit math and connection buffers (Step 4)
4. Pacing, opening hours, and anti-tourist-trap vetting (Step 5)

## 1. Entry, permit, health, weather, and calendar gate (Step 2)

1. **Passport and border entry**:
   - **Schengen Area**: verify the dual rule under **Regulation (EU) 2016/399 Article 6(1)(a)**: the passport must be **(a) issued within the previous 10 years** on the date of entry AND **(b) valid for at least 3 months after the planned departure date**.
   - **All other international destinations**: minimum passport validity (typically **6 months beyond entry/departure**), required blank visa pages (2 to 4), and pre-departure authorizations or visas (**US ESTA**, **UK ETA**, **EU ETIAS**, **Canada eTA**, **Australia ETA**, **Korea K-ETA**, **India e-Visa**, or consular visas) with official government domains and lead times.
2. **Driving permits, health rules, and medication bans**:
   - When vehicle or scooter rental is in scope, check whether the destination requires a **1949 Geneva Convention IDP** (1-year validity; strictly enforced in Japan, South Korea, Taiwan) or a **1968 Vienna Convention IDP** (3-year validity; continental Europe and others), issued in the home country before departure.
   - Check mandatory vaccinations (**WHO IHR Yellow Fever** certificates) and national customs bans on common prescriptions (such as Japan's prohibition on amphetamine stimulants/Adderall and pseudoephedrine without advance import clearance, or UAE controlled-medication permits).
3. **High altitude and seasonal extremes**:
   - Above **2,500 m (8,200 ft)** sleeping or excursion elevation (Cusco, La Paz, Lhasa, Leh, Quito, alpine passes), apply **CDC Yellow Book** graded ascent: sleep lower first when possible (for example, Cusco Airport 3,399 m down to the Sacred Valley 2,870 m for Nights 1 to 2), cap sleeping-elevation gains above 3,000 m at **500 m/day or less** with an extra night every 1,000 m, and keep the first 24 to 48 hours light.
   - Check dates against monsoon, typhoon, hurricane, wildfire-smoke, extreme wet-bulb heat (above 35°C), and winter road/ferry closure windows.
4. **Macro-holidays, strikes, and booking bottlenecks**:
   - National shutdowns and crowd surges: Golden Week, Obon, and New Year in Japan; Lunar New Year across East/Southeast Asia; Ramadan and Eid; *Ferragosto* in Italy; Sunday commercial closures in DACH/Europe.
   - Attractions needing **30 to 90+ day advance reservations or lotteries**, so the user knows whether tickets are still obtainable.

## 2. Geographic clustering and true nightly cost (Step 3)

1. **Cluster first, route second**: group Points of Interest into contiguous **walkable neighborhood clusters** or single-line transit corridors so each half-day stays in one zone. Every day starts where the prior night ended.
2. **Hotel Change Tax**: price every base change at **2.5 to 4.5 hours of lost daytime** (packing, checkout, station access, line-haul, luggage, check-in, unpacking). Convert 1-night hops into **hub-and-spoke day trips** or luggage-forwarded stops whenever one-way door-to-door transit is under 90 minutes.
3. **True Location-Adjusted Nightly Cost**, to defeat drip pricing when comparing hotels, rentals, or bases:
   $$C_{\text{night, true}} = P_{\text{base}} + F_{\text{resort/dest}} + \frac{F_{\text{cleaning/platform}}}{N_{\text{nights}}} + T_{\text{occupancy/city}} + C_{\text{parking/ZTL}} + \Delta C_{\text{transit/taxi}} + v_{\text{vacation\_hour}} \cdot \Delta T_{\text{commute}}$$
   Include the base rate, mandatory resort/destination fees, cleaning/OTA fees spread over the nights, occupancy and per-person tourist taxes, overnight parking/ZTL fees, round-trip party transit and late-night taxis, and the value of extra daily commuting time plus the ability to return midday for a 20-minute rest.

## 3. Door-to-door transit math and connection buffers (Step 4)

1. **Full door-to-door time**; never schedule on in-vehicle time alone:
   $$T_{\text{D2D}} = T_{\text{checkout/pack}} + T_{\text{access}} + T_{\text{terminal/security}} + T_{\text{wait/headway}} + T_{\text{in-vehicle}} + \sum_{k=1}^{K} T_{\text{transfer}, k} + T_{\text{baggage/customs}} + T_{\text{egress}} + T_{\text{checkin/drop}} + T_{\text{buffer}}$$
2. **Friction buffers and transfer penalties**:
   - Add **+25% to +35%** (minimum **+15 minutes**) to mapping-app transit and walking estimates for station navigation, ticketing, elevators, and rest stops.
   - Weight walking, waiting, and transfers at **2.0x to 2.5x** in-vehicle time (**3.0x to 4.0x** with luggage, strollers, cobblestones, or stairs) plus a **10 to 25 minute penalty per transfer**. Prefer a slightly longer direct train or bus over a multi-transfer route when carrying bags.
   - Arrive **20 to 30 minutes before** non-refundable timed-entry cutoffs; use **95th-percentile terminal buffers** for flights (2 hours domestic, 3 hours international) and high-speed rail (30 to 45 minutes).
3. **Fits between fixed plans (Space-Time Prism)**: between fixed anchors A (ending at $t_1$) and B (starting at $t_2$), add stop $k$ with dwell time $d_k$ only when $t_1 + T_{\text{D2D}}(A, k) + d_k + T_{\text{D2D}}(k, B) \le t_2$.
4. **One booking vs. separate tickets**:
   - **Protected Single-PNR / interline**: layovers of at least **1.5x the IATA Minimum Connecting Time** (90 to 120 minutes domestic, 120 to 180 minutes international/customs) whenever a miss would strand the party overnight.
   - **Unprotected self-transfers**: a Leg 1 delay triggers a **100% no-show cancellation** of onward flights or cruises with no carrier duty of care. Require **arriving the evening before** any long-haul flight, cruise embarkation, or wedding/anchor event, or a **4 to 6 hour buffer** for short-haul self-transfers where rebooking is cheap and frequent.

## 4. Pacing, opening hours, and anti-tourist-trap vetting (Step 5)

1. **1 Fixed Anchor + 1 Flexible Option per half-day**: split each day into **Morning**, **Afternoon**, and **Evening**. At most one high-load anchor (major museum, monument, or timed tour, capped at **90 to 120 minutes** of focused viewing to prevent museum fatigue) plus one low-load option in the same cluster.
2. **Alternate load (Attention Restoration Theory)**: pair every high-attention stop with a restorative one (park, waterfront, garden, architectural stroll, market, unhurried café or thermal bath), never two dense museums or sites back-to-back.
3. **Jet lag and the final 24 hours**:
   - Crossing **5 or more time zones**: resynchronize at **1.0 day per zone westward** and **1.5 days per zone eastward**. Keep Arrival Day free of high-stakes timed tickets and rental driving; schedule daylight and a light walk. **Eastward**: start Days 1 to 2 anchors at **10:30 AM or later**. **Westward**: use early waking (7:00 to 8:30 AM) for uncrowded outdoor sights and keep evenings early.
   - **Peak-End Rule**: place top priorities as unhurried peaks, and keep the **final 24 hours** in the departure hub with light packing and no long transfers.
4. **Day-of-week hours and last entry**: label every day with its weekday (`Mon`, `Tue`) and check each stop satisfies $O_{im} \le s_{im} \le L_{im} \le C_{im} - d_i$, accounting for Monday closures (Musée d'Orsay, Versailles, Uffizi) versus Tuesday closures (Louvre, Prado, Musée Rodin), early seasonal dusk, and last entry (typically 30 to 60 minutes before closing).
5. **Anti-tourist-trap vetting**:
   - **3-Block Rule**: route dining and shopping **3 to 6 blocks away** from landmark perimeters, cruise terminals, and main station plazas, into streets where venues compete for repeat locals.
   - Cross-check picks against the **native regional guides** in the destination playbook (Tabelog 3.20 to 3.50+ in Japan, Slow Food *Osterie d'Italia* / Gambero Rosso in Italy, Le Fooding / *Fait Maison* in France, Guía Repsol *Soletes* in Spain, Naver/KakaoMap + Blue Ribbon in Korea, Dianping/OpenRice in China/HK/TW, Michelin *Bib Gourmand*) rather than English SEO listicles or viral queues.
