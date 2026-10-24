# Destination & Mode Playbooks

Specialized verification, transit math, physiological pacing, and anti-tourist-trap rules for the six travel domains referenced in [`SKILL.md`](../SKILL.md).

## 1. Native anti-tourist-trap and culinary vetting

1. **Apply the 3-Block Repeat-Local Rule (Akerlof & MacCannell defense)**:
   - Venues directly facing Tier 1 monuments, cruise terminals, or major transit hubs operate in a **zero-repeat-customer equilibrium**: 99% of diners are one-time visitors, allowing high-margin, low-quality operators ("lemons") to outbid local kitchens for prime tourist frontage.
   - Route meals and coffee stops **3 to 6 blocks away** into residential or office backstreets where restaurants depend on repeat local patronage.
2. **Cross-check against native regional platforms and curated directories**:
   - Filter out English-only SEO listicles, paid influencer roundups, and viral social-media queue traps by checking native-language platforms and independent local guides:

| Region / Country | Primary Native & Independent Vetting Sources | Score Calibration & Local Signals |
| :--- | :--- | :--- |
| **Japan** | **Tabelog (`tabelog.com`)**, *Tabelog Hyakumeiten* (Top 100 by category), *Michelin Bib Gourmand* | Tabelog weights experienced local critics heavily: **$3.50+$ is top ~3% exceptional**; **$3.20\text{ to }3.49$ is a strong neighborhood favorite**; **$3.70+$ requires advance reservations**. A 4.8 rating on English Google Maps in Shinjuku, Shibuya, or Kyoto with 90% tourist reviews is frequently an incentivized-review tourist trap. |
| **Italy** | **Slow Food *Osterie d'Italia***, **Gambero Rosso** (*Tre Forchette*, *Tre Gamberi*, *Tre Spicchi*), *Michelin Bib Gourmand* | Favor seasonal regional *osterie* and *trattorie* with short printed daily menus over spots with multilingual laminated photo boards or street barkers. |
| **France** | **Le Fooding**, **Gault & Millau**, *Michelin Bib Gourmand*, municipal covered markets (*Marchés couverts*) | Look for the legal ***"Fait Maison"*** symbol and short daily slate (*ardoise*) menus that change with market supply; verify lunch service windows (typically 12:00 PM to 2:00 PM strict cutoff). |
| **Spain & Portugal** | **Guía Repsol (*Soles Repsol* & *Soletes*)**, *Macarfi Guide* (Madrid, Barcelona, Basque Country), *Michelin Bib Gourmand* | Repsol ***Soletes*** specifically index authentic neighborhood *tascas*, *tabernas*, *marisquerías*, and *pintxo* bars favored by locals at everyday prices. Account for late Spanish dining windows (lunch 1:30 PM to 3:30 PM; dinner 8:30 PM to 10:30 PM). |
| **South Korea** | **Naver Map**, **KakaoMap**, **Blue Ribbon Survey**, **CatchTable** | Google Maps lacks full walking/driving routing in South Korea due to geospatial export rules and skews heavily toward foreign visitors. Verify ratings, local review volume, and operating hours on **Naver Map** or **KakaoMap**, and check **Blue Ribbon Survey** for vetted local kitchens. |
| **China, Taiwan & HK** | **Dianping (*Dazhong Dianping* / Black Pearl Guide)**, **OpenRice** (Hong Kong), *Michelin Bib Gourmand* | Cross-check local rating distributions and recent unedited dish photos on Dianping or OpenRice; use **AMap (Gaode)** or **Baidu Maps** for accurate mainland China transit times. |
| **Americas, UK & Global** | **Michelin *Bib Gourmand***, **James Beard Foundation** (US), **Good Food Guide** (UK), **Eater 38** (city heatmaps), destination-specific local forums | Require convergence between curated local food journalism and recent resident discussion rather than affiliate-driven "Top 10" travel blogs. |

3. **Disqualify structural tourist-trap red flags**:
   - Reject or flag venues exhibiting: (a) street touts/barkers standing outside with menus, (b) 6-language laminated picture menus with 80+ unrelated dishes (such as pizza, sushi, burger, and paella from one kitchen), (c) table placards offering a free shot, dessert, or discount in exchange for an immediate 5-star Google review, or (d) 90-minute viral queues driven by a single recent social video with weak native ratings.

## 2. Urban and multi-city rail itineraries

1. **Run rail-pass break-even math against point-to-point tickets**:
   - Never recommend a national or regional rail pass (such as the nationwide JR Pass in Japan, Swiss Travel Pass, or Eurail) by default. Following major fare adjustments (such as the 2023 JR Pass price increase of ~65% to 70%), point-to-point tickets or regional passes (such as JR West Kansai-Hiroshima Pass or Swiss Half Fare Card) frequently beat nationwide passes by 30% to 50%.
   - Sum the exact point-to-point fares for the planned legs and recommend a pass only when $\sum F_{\text{point-to-point}} > P_{\text{pass}}$ (or when the pass unlocks specific convenience value that the user prioritizes).
2. **Decouple luggage from passengers on multi-stop transfers**:
   - In rail-centric destinations (especially Japan and Switzerland), use **luggage forwarding** (such as Yamato *Takkyubin* in Japan or SBB luggage services in Switzerland) to send large bags directly from Hotel $A$ to Hotel $C$ while travelers carry a 1-night daypack to an intermediate stop $B$ (such as Hakone, Nikko, Kanazawa, or Zermatt).
   - Check oversized-baggage rules on high-speed rail (such as the **Shinkansen oversized baggage reservation requirement** for bags with total dimensions $160\text{ cm}$ to $250\text{ cm}$ on Tokaido/Sanyo/Kyushu lines, or Eurostar/TGV/Trenitalia rack limits).
3. **Audit weekly museum closure patterns and timed-entry lotteries**:
   - Cross-check every cultural stop against the city's **Monday vs. Tuesday closure split**:
     - *Monday closures (examples)*: Musée d'Orsay, Palace of Versailles, Musée de l'Orangerie (Paris); Uffizi Gallery, Galleria dell'Accademia, Vatican Museums [Sundays except last Sunday] (Italy); Reina Sofía [Tuesdays], Thyssen-Bornemisza [Mondays partial] (Madrid); most Tokyo national museums (Ueno).
     - *Tuesday closures (examples)*: Musée du Louvre, Centre Pompidou, Musée Rodin (Paris); Museo del Prado (open Tue, closed only major holidays, verify hours), Kunsthistorisches Museum (Vienna, seasonal).
   - Separate **30-to-90-day advance booking bottlenecks** into the Booking Action Timeline with exact release timestamps (for example, Ghibli Museum tickets releasing on the 10th of the preceding month at 10:00 JST, Alhambra Nasrid Palaces 60 to 90 days out, Anne Frank House 6 weeks out on Tuesdays at 10:00 CET, Last Supper in Milan quarterly blocks).

## 3. Road trips, rental vehicles, and island ferries

1. **Verify International Driving Permit (IDP) convention compatibility**:
   - Check whether the destination enforces the **1949 Geneva Convention** (1-year IDP; strictly required by **Japan, South Korea, Taiwan, Thailand, Australia/NZ** if license is not in English) or the **1968 Vienna Convention** (3-year IDP; continental Europe, Brazil, parts of Central Asia), or requires an official local translation (such as a **JAF translation** in Japan for drivers from Switzerland, Germany, France, Belgium, Monaco, or Taiwan).
   - Warn the traveler that an IDP **must be obtained in the issuing country of their driver's license prior to departure**; online "instant digital IDPs" are invalid scams that rental counters reject.
2. **Audit urban driving traps, ZTL zones, and true vehicle TCO**:
   - In historic European cities (especially Italy's ***Zona a Traffico Limitato* [ZTL]** in Florence, Rome, Pisa, Siena, Bologna, and Milan's Area C/B, or London's Congestion/ULEZ zones), entering a camera-monitored zone without a pre-registered hotel whitelist triggers automatic €80 to €200+ fines per camera pass, billed months later with rental-agency admin fees.
   - Rule: **Pick up rental cars when leaving the major city and drop them off upon entering the next major city**; never rent a car to sit in central city garages at \$40 to \$85/night.
   - Sum full vehicle cost: base rental + mandatory local liability/CDW (such as Italy mandatory CDW/TP or Mexico mandatory third-party liability) + one-way drop fee + highway vignettes/toll transponders (Swiss/Austrian vignette, Portuguese Via Verde, Japanese ETC card rental) + fuel + overnight parking.
3. **Bound daily driving time and ferry connection risk**:
   - Cap scenic road-trip driving at **3 to 4 hours of net wheel time per day** ($T_{\text{in-vehicle}} \le 4\text{ hrs}$) so stops, viewpoint hikes, and meals fit within daylight hours.
   - Avoid night driving on unlit rural, mountain, or wildlife-heavy roads (such as Iceland Ring Road in winter, Scottish single-track roads, Costa Rica rural highways, or Australian outback at dusk/dawn).
   - For **island-hopping ferries** (such as Greek Cyclades high-speed catamarans, Scottish CalMac ferries, or Japanese Seto Inland Sea / Okinawa ferries), account for high-wind cancellations (**Meltemi winds** in the Aegean, typhoon swells in East Asia) by returning to the **mainland departure port city at least the night before (24-hour buffer)** an international flight home.

## 4. High-altitude, trekking, and extreme climates

1. **Enforce CDC Yellow Book high-altitude acclimatization rules ($>2,500\text{ m} / 8,200\text{ ft}$)**:
   - Acute Mountain Sickness (AMS) affects 25% to 50%+ of sea-level travelers who ascend rapidly above $2,500\text{ m}$ ($8,200\text{ ft}$), progressing to life-threatening HAPE or HACE if ignored.
   - **Sleeping elevation governs acclimatization**:
     - When flying into a high-altitude airport such as **Cusco ($3,399\text{ m}$)**, route the traveler immediately down to the **Sacred Valley (Urubamba/Ollantaytambo at $2,790\text{ to }2,870\text{ m}$)** for Nights 1 to 2 before sleeping in Cusco.
     - Above **$3,000\text{ m}$ ($10,000\text{ ft}$)**, increase sleeping elevation by **at most $500\text{ m}$ ($1,600\text{ ft}$) per night**, and schedule a **zero-ascent rest/acclimatization night every $1,000\text{ m}$ ($3,300\text{ ft}$)** of elevation gain.
     - Keep the first 36 to 48 hours at elevation free of strenuous hikes or alcohol, and remind travelers to consult a travel-medicine clinician regarding prophylactic acetazolamide (Diamox) when rapid ascent by flight (such as La Paz at $3,640\text{ m}$ or Leh at $3,500\text{ m}$) is unavoidable.
2. **Schedule around extreme heat, wet-bulb limits, and daylight windows**:
   - When daytime temperatures exceed **$33\text{ to }35^\circ\text{C}$ ($91\text{ to }95^\circ\text{F}$)** or high wet-bulb humidity (such as July/August in Rome, Athens, Seville, Cairo, Kyoto, or Bangkok pre-monsoon), ban unshaded midday archaeological marches between **12:00 PM and 4:00 PM**.
   - Restructure hot-weather days into a **Split-Day (Siesta) Rhythm**:
     - **Early Morning Block (`07:00–11:00`)**: outdoor ruins, hikes, or viewpoints at opening bell.
     - **Midday Heat Block (`11:30–16:30`)**: long shaded lunch, climate-controlled museum/church, or hotel rest/swim.
     - **Late Afternoon & Evening Block (`16:30–22:00`)**: golden-hour neighborhood walk, *passeggiata*, and late dinner.

## 5. Family, multi-generational, and accessible travel

1. **Apply mobility and stroller friction multipliers to $T_{\text{D2D}}$**:
   - Increase the walking and transfer disutility multiplier to **$w_{\text{walk}} = 3.0\text{ to }4.0\times$** and add **30 to 45 equivalent minutes per transfer** when routing strollers, wheelchairs, young children, or travelers with limited knee/hip mobility.
   - Explicitly flag cities or neighborhoods with severe vertical/surface barriers (such as Venice's stepped canal bridges, Positano/Amalfi cliff stairs, Lisbon's Alfama/Bairro Alto steep hills, Santorini caldera steps, or older Paris Métro lines lacking elevators vs. RER/bus network) and specify step-free transit modes (buses, trams, accessible subway lines, or flat neighborhoods).
2. **Anchor around biological rest windows and split-party flexibility**:
   - Select centrally located accommodations so part of the group can return to the hotel in under 15 minutes for a midday nap or rest while higher-energy members take the **Flexible Option**.
   - Cap daily structured sightseeing for young children or seniors at **1 primary morning anchor**, followed by park/playground/café downtime and a low-friction afternoon option.

## 6. Complex air routing, positioning flights, and self-transfers

1. **Separate Single-PNR protected connections from Unprotected Self-Transfers**:
   - **Single-PNR / Interline Connection**: all flights share one booking reference/ticket; the operating carrier owes rebooking and duty of care under **EC 261/2004** (in EU/UK scope) or its Conditions of Carriage. Even on a single PNR, require **$\ge 1.5\times$ IATA Minimum Connecting Time (MCT)** ($90\text{ to }120\text{ min}$ domestic; $120\text{ to }180\text{ min}$ international or US first-port-of-entry customs/bag re-check) when connecting onto a once-daily long-haul flight.
   - **Unprotected Separate Tickets ("Self-Transfer" / Split-PNR)**: booking a separate positioning flight (or non-integrated rail leg) to catch a long-haul flight or cruise carries **zero misconnection protection**. Missing the long-haul check-in/bag-drop cutoff (typically 60 minutes prior to departure) results in a **No-Show cancellation of the entire outbound and return ticket**.
   - **Positioning Rule**: whenever a traveler uses a separate positioning ticket to reach a long-haul international flight, cruise departure, or critical anchor event, recommend **flying/training into the gateway city the evening before (overnight buffer)**. If same-day positioning is unavoidable on short-haul routes, require a **4 to 6+ hour landside buffer** covering deplaning, immigration, baggage claim, terminal change, re-check cutoff, and security.
2. **Audit unbundled "Basic Economy" and LCC fare traps**:
   - When comparing flights on Low-Cost Carriers (Ryanair, EasyJet, Wizz Air, Peach, Jetstar, AirAsia, Spirit, Frontier) or legacy Basic Economy tiers, compute **True Door-to-Door Fare**:
     $$\text{Fare}_{\text{true}} = F_{\text{base}} + F_{\text{carry-on}} + F_{\text{checked bag}} + F_{\text{seat selection}} + F_{\text{airport check-in}} + C_{\text{secondary airport transit}}$$
   - Include the extra time and cost of secondary airports (such as Paris Beauvais `BVA`, London Stansted/Luton `STN`/`LTN`, Tokyo Narita `NRT` vs. Haneda `HND`, or Frankfurt Hahn `HHN`) before declaring an LCC fare cheaper than a main-hub flight or city-center high-speed train.
