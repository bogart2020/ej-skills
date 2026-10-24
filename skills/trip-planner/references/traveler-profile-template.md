# Traveler Profile Template & Maintenance Rules

Reference for reading, creating, and updating an optional persistent traveler profile so [`trip-planner`](../SKILL.md) remembers the user's baseline travel constraints across sessions without re-asking settled questions.

## Discovery order

1. **Project-scoped profile**: `.agents/traveler-profile.md` in the current workspace (useful for shared family trips, team offsites, or specific expedition folders).
2. **User-global profile**: `~/.agents/traveler-profile.md` (default home for personal travel preferences across CLI and IDE agents).
3. **Chat environment fallback**: in Claude Desktop or web chat where local dotfiles are unavailable, read built-in platform memory or project instructions, and offer a copyable Markdown block when the user asks to save their traveler profile.

## Maintenance rules

1. **Zero-config by default**: Never block trip planning or an itinerary audit because no profile file exists. Gather only the context needed for the current trip via Step 1.
2. **Opt-in writes only**: Create or update `.agents/traveler-profile.md` or `~/.agents/traveler-profile.md` only after delivering the readiness verdict and confirming the user wants to save the newly established preferences or trip post-mortem entry.
3. **Keep entries compact, durable, and privacy-safe**: Store only durable facts that affect future routing, entry gates, pacing, and accommodation choices (passport nationality, validity year/month, trusted traveler programs, IDP status, home airport/station, walking ceiling, circadian style, dietary/medical rules, and past trip lessons). Never store full passport numbers, KTN/Redress numbers, PNR confirmation codes, credit card numbers, or exact home street addresses.

## Recommended schema (`traveler-profile.md`)

```markdown
# Traveler Profile

## Passports, Entry & Driving Eligibility
- **Passport Nationality**: [e.g., US / UK / PH / Dual]
- **Passport Issue & Expiry (YYYY-MM)**: Issued [YYYY-MM], Expires [YYYY-MM] (used for Schengen 10-year/3-month and 6-month validity checks)
- **Active Multi-Year Authorizations / Visas**: [e.g., US ESTA valid to YYYY-MM, UK ETA, Japan e-Visa, Schengen multi-entry]
- **Trusted Traveler Programs**: [e.g., Global Entry / TSA PreCheck / NEXUS / APEC Business Travel Card]
- **Driving & IDP Baseline**: [Home license country; comfortable with manual/automatic, left/right-hand traffic; active 1949 or 1968 IDP expiry]

## Home Hub & Transit Preferences
- **Home Airport & Rail Hub**: [e.g., SFO / MNL / LHR]
- **Luggage Baseline**: [e.g., Carry-on + personal item only / 1 checked spinner + daypack]
- **Transit Mode Preferences**: [e.g., High-speed rail > short-haul flights under 4 hrs; avoid overnight buses; motion-sickness sensitivity on rough ferries/winding roads]
- **Loyalty & Card Protections**: [e.g., Primary rental CDW via Chase Sapphire Reserve; Star Alliance Gold / Oneworld Emerald]

## Pacing, Mobility & Circadian Style
- **Circadian Chronotype**: [e.g., Morning lark (happy with 07:30 starts) vs. Night owl (no fixed anchors before 10:00)]
- **Daily Walking & Elevation Ceiling**: [e.g., Comfortable up to 12–15 km/day (18,000 steps); avoid steep unshaded climbs or heavy stair hauling]
- **Base Hop Tolerance**: [e.g., Minimum 3 nights per hotel base; happy to use luggage forwarding for 1-night ryokan/alpine stops]
- **Hard Anti-Goals**: [e.g., No 60+ minute viral food queues; no back-to-back art museums; no unprotected self-transfers]

## Dietary, Medical & Sleep Guardrails
- **Dietary Rules & Allergies**: [e.g., Severe peanut/shellfish allergy (carry translated chef cards); vegetarian; halal; gluten-free]
- **Environmental & Physiological Limits**: [e.g., Needs air conditioning for sleep above 22C; quiet high-floor room away from street bars; high-altitude AMS sensitivity above 2,500m]
- **Medication Import Notes**: [e.g., Carries prescription inhaler / stimulant requiring advance customs check for Japan/UAE]

## Past Trip Post-Mortem Log
| Date | Destination & Duration | Verdict / Structure Used | What Worked Best (Peaks) | What Failed / Lesson for Next Trip |
| :--- | :--- | :--- | :--- | :--- |
| YYYY-MM | [e.g., Kyoto & Tokyo, 9 nights] | 2 bases + *Takkyubin* to Hakone | [07:00 Fushimi Inari walk; Tabelog 3.5+ neighborhood izakayas] | [2 museums in 1 day caused burnout; keep Day 1 arrival completely unscheduled] |
```
