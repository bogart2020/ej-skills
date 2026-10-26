# Stress Test Report: trip-planner

**Date:** 2026-10-26 / **Target Skill:** `skills/trip-planner/SKILL.md` / **Model Tier Tested:** Claude Haiku (blind subagents, one skill installed, 1 run per scenario, failed scenarios rerun 2 more times) / **Overall Verdict:** FAIL (before fixes; see After Fixes)

Verdict rule: PASS = every run passed. CONDITIONAL PASS = at least 80% of first runs passed and no skill-caused failure came back in a repeat run. FAIL = anything else. This skill passed 14 of 18 first runs (78%, below 80%), and skill-caused failures came back in repeat runs for 3 of the 4 failed scenarios, so it fails on both counts. None of the 4 failures was caused only by the test setup.

## Executive Scorecard

First runs only. "Forgetting Rules in Long Conversations" asks whether a multi-turn run dropped a rule it followed earlier in the same conversation.

| Suite | Runs | Passed | Failed | Pass Rate | Forgetting Rules in Long Conversations |
| :--- | :-: | :-: | :-: | :-: | :--- |
| 1. Standard Workflow Test | 3 | 1 | 2 | 33% | No (1 multi-turn run, no rules lost) |
| 2. Boundary Rejection Check | 3 | 3 | 0 | 100% | Not tested (single-turn only) |
| 3. Edge Cases | 3 | 3 | 0 | 100% | Not tested (single-turn only) |
| 4. Consistency Under Rephrasing | 6 | 4 | 2 | 67% | Not tested (single-turn only) |
| 5. Resisting Agreeable Biases and Attacks | 3 | 3 | 0 | 100% | Not tested (single-turn only) |
| **Total** | **18** | **14** | **4** | **78%** | **No** |

## Reliability Metrics

- Consistency Under Rephrasing: `Consistent Pairs / Total Pairs = 2 / 3 = 0.67 (Target: 1.00)`
  - The Lisbon pair (T4.1a and T4.1b) gave different verdicts: `Ready to Book` and `Viable With Adjustments`. The Barcelona pair and the Tokyo pair matched. In the repeat runs, all four Lisbon reruns gave `Viable With Adjustments` with the same central base, so 5 of 6 Lisbon runs agree on the label and 6 of 6 on the base.
- Step Adherence: `Sum of Step Adherence scores / Highest possible = 75 / 90 = 83%`, which uses the 1-to-5 score for how closely each of the 18 first runs followed the skill's steps.
- Forgetting Rules in Long Conversations: `Runs With Lost Rules / Total Multi-Turn Runs = 0 / 1 = 0% (Target: 0%)`
  - The only multi-turn run (T1.2) kept the verdict wording, the passport math, and the question format in its last turn. What it left out, single-turn runs left out too, so this was not caused by the long conversation.
- Reliability Across Repeated Runs: `All Repeated Runs Passed = No`

| Scenario | Failed runs out of 3 | Same cause each time? | Caused by skill or test setup |
| :--- | :-: | :--- | :--- |
| T1.2 Rome and Florence, multi-turn | 3 | No: run 1 skipped the half-day backup plans; runs 2 and 3 stopped the report after the passport blocker | Skill |
| T1.3 Paris to Bruges audit | 3 | Partly: the share of waking hours spent in transit was missing every time; the other faults varied | Skill |
| T4.1a Lisbon, version a | 1 | Only run 1 failed | Skill |
| T4.1b Lisbon, version b | 2 | Yes: both failed runs sent the traveler to a funicular that has been closed since 2025 | Skill |

## Key Vulnerabilities and Transcript Evidence

### Failure 1: Sends the traveler to a closed attraction, trusting third-party pages

- **Suite:** 4. Consistency Under Rephrasing (T4.1b); also 1. Standard Workflow Test (T1.3, run 1)
- **Trigger Input:** "Lisbon, May 12-15 2027, solo. Hate early mornings, love viewpoints + food. ... Just plan, no qs." and the Paris audit ("Day 1 (Mon Jun 7, 2027): ... Versailles 14:00")
- **Observed Failure:** T4.1b: "Morning, main plan: ride the Elevador da Glória funicular ... The first run is around 7:15 on weekdays". The funicular has been out of service since the 3 Sept 2025 derailment, with a replacement planned for 2029. The source was a third-party guide (lisbonlisboaportugal.com), not the operator, Carris. Rerun 2: "*Optional extra:* ride the Glória funicular." T1.3 run 1: "Versailles: conflicting listings on whether it closes Mondays, so check the official site." Versailles does close on Mondays, and the skill's own reference files say so.
- **How often:** T4.1b 2 of 3 runs; T1.3 1 of 3 runs (the Versailles miss).
- **Root Cause:** The verified-facts rule (Guardrail 1, `SKILL.md:144`) asks for current hours but accepts any web page. Nothing requires the venue's or operator's own site for a planned stop, nothing asks whether the place is operating at all, and there is no rule for what to do when sources disagree on a closure day.

### Failure 2: An overpacked plan is not measured, so the verdict and the alternative go soft

- **Suite:** 1. Standard Workflow Test (T1.3)
- **Trigger Input:** "Audit my plan, no questions please." (4 stops, 3 nights, 3 hotel changes, Paris to Amsterdam to Brussels to Bruges)
- **Observed Failure:** No run gave the share of waking hours spent in transit. Run 1 offered a path to `Ready to Book` that kept all 3 hotel moves: "Switches to `Ready to Book` once Versailles hours are confirmed, Eiffel Tower hours are confirmed, and the Bruges to airport train is set to leave before 11:00". Rerun 2 gave the wrong verdict: "The overall shape works" (`Viable With Adjustments`), then "Moves to **Cut Stops / Slow Down** if you add a fourth city" when the plan already had four stops. Rerun 3 got the verdict right but offered only one clause as the shorter plan ("cut the route to two cities"), with no plan and no trade-offs.
- **How often:** 3 of 3 runs.
- **Root Cause:** The "too many cities" row of the verdict table (`SKILL.md:137`) and the no-flattery pacing rule (Guardrail 3, `SKILL.md:146`, "when a draft is overpacked") give no number that marks a plan as overpacked. Guardrail 3 wants the transit numbers "first", but the bottom-line slot in `references/report-format.md:10` has no place for them. `references/report-format.md:28` does not require that each condition for a better verdict removes the reason for the current one.

### Failure 3: The report stops after a passport blocker

- **Suite:** 1. Standard Workflow Test (T1.2, reruns 2 and 3)
- **Trigger Input:** "1 US passport, issued 2017-03-20, expires 2027-03-15." (Rome and Florence, Dec 10 to 17, 2026; the passport runs out 2 days before the 3-month rule for Europe's border-free area allows)
- **Observed Failure:** Both reruns did the passport math correctly and gave `Do Not Book As Planned`, then stopped: no day-by-day plan, no booking checklist, no conditions that would change the verdict. Rerun 2 ended by asking whether to "start the plan now ... or wait". Its trace says it "Did not read the skill's references/ files". Rerun 3 also showed internal wording to the user: "the EU regulation the trip planner cites".
- **How often:** 2 of 3 runs (run 1 failed for a different reason, see Failure 5).
- **Root Cause:** The `Do Not Book As Planned` row (`SKILL.md:140`, "Hold every booking ... until the blocker clears") and the verdict step (`SKILL.md:127`) read as "stop planning". Nothing says the full report still follows a hard blocker. With web search blocked, Guardrail 1 (`SKILL.md:144`) also pushed the agent to skip the day plan instead of writing it with "not checked" labels.

### Failure 4: `Ready to Book` given while key checks were never done

- **Suite:** 4. Consistency Under Rephrasing (T4.1a)
- **Trigger Input:** "No questions, just plan it: 3 nights in Lisbon, solo, May 12 to 15, 2027."
- **Observed Failure:** "**Verdict: Ready to Book**" next to the rows "Weather | Not checked", ETIAS (the EU's new online travel authorization) as a "Watch item", "I did not search hotels", and "Flight times and fares are not checked." The rephrased twin gave `Viable With Adjustments` for the same trip.
- **How often:** 1 of 3 runs (both reruns gave `Viable With Adjustments` and passed).
- **Root Cause:** `SKILL.md:135` requires that the plan "Clears every entry, altitude, weather, and calendar check" but does not say how an unchecked item counts. `SKILL.md:127` says to grade "the plan as the user gave it", which is unclear when the user gave no draft plan.

### Failure 5: Day plans squeezed to one line, with a same-day train to the flight home

- **Suite:** 1. Standard Workflow Test (T1.2, run 1)
- **Trigger Input:** "Plan 7 nights in Rome and Florence, Dec 10 to Dec 17, 2026. Flying from Chicago."
- **Observed Failure:** "Day 5 ... Uffizi is closed today." has no backup plan; Days 7 and 8 have none either, and most days have no Morning, Afternoon, and Evening split. Day 8: "Morning train back to Termini, then a transfer to the airport. ... Keep the day light." The last night is in Florence while the long-haul flight leaves from Rome the same day.
- **How often:** 1 of 3 runs. The same squeezing (one backup plan per day, no optional extras) also showed up as a minor issue in T4.2b, T5.3, T4.1a, and T3.3.
- **Root Cause:** `references/report-format.md:17` packs 7 required items into one bullet, so a weaker model writes one sentence per day. `SKILL.md:115` says to keep the final 24 hours "in the departure hub" but not what to do when the last night is somewhere else. The separate-tickets rule in `references/planning-rules.md:46` is not tied to train-to-flight days.

## Line-by-Line Remediations

1. `skills/trip-planner/SKILL.md:144` (verified-facts rule): add "For every main plan and optional extra, confirm on the venue's or operator's own site that it is open and operating on that date. If only third-party pages load, label the stop unconfirmed and give a Plan B in the same area. When sources disagree on a closure day, plan as if the place is closed and say so." Addresses Failure 1 (T4.1b, T1.3 run 1) and the third-party sources seen in T1.3, T3.3, T4.1b, and T4.2b.
2. `skills/trip-planner/SKILL.md:137` (`Cut Stops / Slow Down` row): add "Assign when there are more stops than nights minus 1, 2 or more 1-night hotel stays in a row, or more than 35% of waking hours in transit." Addresses Failure 2 (T1.3 rerun 2).
3. `skills/trip-planner/references/report-format.md:10` (bottom line): add "For an overpacked plan, state 'X of about Y waking hours in transit (Z%)' and the total hours lost changing hotels, then name the consolidated alternative and what it gives up." Addresses Failure 2 (transit share missing in all 3 runs; one-clause alternative in rerun 3).
4. `skills/trip-planner/SKILL.md:127` (verdict step): add "After a hard blocker, still write every section of the report for the plan as it would run once the blocker clears, labeling unchecked hours and prices as not checked." Addresses Failure 3 (T1.2 reruns 2 and 3).
5. `skills/trip-planner/SKILL.md:135` (`Ready to Book` row): add "Every before-you-go row must be cleared from a source checked this session; any row marked not checked caps the verdict at `Viable With Adjustments`." At line 127, define "the plan as the user gave it" as "the user's draft, or, when there is none, your plan before revisions". Addresses Failure 4 and the Lisbon pair mismatch.
6. `skills/trip-planner/references/report-format.md:28` (what would change the verdict): add "Each condition must remove the reason for the current verdict." Addresses Failure 2 (T1.3 run 1 and rerun 2) and the same minor issue in T5.1 and T1.2.
7. `skills/trip-planner/references/report-format.md:17` (day layout): replace with "Write Morning, Afternoon, and Evening as three separate lines. Each line gives the main plan with checked hours and last entry, one optional extra, the door-to-door travel leg, where to eat, and ends with 'Plan B: ...' in the same area." Addresses Failure 5 and the minor issue in T4.2b, T5.3, T4.1a, and T3.3.
8. `skills/trip-planner/SKILL.md:115` (final 24 hours): add "If the last night is not in the departure city, move it there, or treat the same-day train to the flight as separate tickets: arrive the evening before or keep 4 to 6 hours of buffer." Addresses Failure 5 (Florence to Rome on flight day).
9. `skills/trip-planner/SKILL.md:22` (money): replace "or flag amounts approximate if none is current" with "If no rate is found this session, still convert at an approximate rate and label it 'approximate, not checked today'; never print a local amount alone." Addresses local-currency-only prices in T1.3, T4.1a, T4.1b, T4.3b, T3.3, and T4.2b, and the US-dollar fallback in T4.3b.
10. `skills/trip-planner/references/planning-rules.md:55` (closure days): this line is wrong. It lists the Prado and Musée Rodin as Tuesday closures, while `references/destination-and-mode-playbooks.md:37` says the Prado is open Tuesdays, and the grader notes Musée Rodin closes Mondays. Change it to "Tuesday closures (Louvre, Centre Pompidou)" and move Musée Rodin to the Monday list.
11. `skills/trip-planner/references/destination-and-mode-playbooks.md:36` and `:37` (closure lists): move "Vatican Museums [Sundays except last Sunday]" and "Reina Sofía [Tuesdays]" out of the Monday list into their own day groups, and move the Kunsthistorisches Museum from the Tuesday list to "Mondays in the off-season". The lists are filed under the wrong days and invite wrong closure calls.
12. `skills/trip-planner/SKILL.md:136` (`Viable With Adjustments` row): add a rule for a plain base comparison: "When the user only asks which base or hotel to pick, grade the recommended base; give `Ready to Book` when every check clears and `Viable With Adjustments` only for a named flaw." Addresses both Tokyo runs (T4.3a and T4.3b), which stretched `Viable With Adjustments` to cover "book early" advice.
13. `skills/trip-planner/SKILL.md:99` (Step 2 completion check): add "If the official page does not load, say so, cite the best dated secondary source, and keep the item as a blocker to re-check before booking." Addresses runs where official sites returned errors and the visa question was left open (T1.1, T3.3, T4.3a, T4.2b).
14. `skills/trip-planner/SKILL.md:105` (Step 3 completion check): add "Compute Real Cost per Night for every recommended base, using a dated price range labeled estimated when no hotel was searched." Addresses missing nightly cost in T4.3a, T4.3b, T4.1a, and T4.1b.
15. `skills/trip-planner/references/planning-rules.md:42` (airport buffers): change "3 hours international" to "3 hours international, 2 hours for flights inside Europe's border-free area". The two Barcelona runs used 2 and 3 hours for the same flight.
16. `skills/trip-planner/SKILL.md:44` (assumptions): change "in one line" to "in up to 3 short bullets". Most runs already wrote more than one line; the rule as written is never followed.

## Test Setup Limits

- **Web search allowance:** most repeat runs used up their search allowance early ("refused: search budget used up"). This explains unchecked hours, exchange rates, and ETIAS status in the reruns. It does not explain the wrong verdicts, the missing report sections, or the closed funicular, so those still count against the skill.
- **Official sites unreachable:** many official pages returned errors (403, 404, a failed address lookup, or a bare page title), for example the EU travel-authorization site in T1.2 rerun 2. Checks that depend on official sources were not fully tested.
- **Only one multi-turn scenario:** the forgetting score (0 of 1) rests on a single conversation, so it says little about long sessions.
- **One first run per scenario:** passing scenarios were not rerun, so a pass may hide a fault that shows up only some of the time.
- **Harness noise:** stray calls to a documents tool in T1.1, T2.3, T3.1, and T3.2 came from the test environment, not the skill, and did not affect the answers.
- **Reference files not always read:** T1.2 rerun 2 says it never opened the skill's reference files. That is a skill-following fault and is counted, but it means the reference-file rules were not exercised in that run.

## After Fixes (2026-10-26)

Every remediation above was applied, some reworded to fit the size limit. Line numbers in the sections above refer to the files before these fixes. Only scenarios that failed their first run were rerun: 1 fresh blind Haiku run each against the fixed skill. When a rerun still failed, the skill got a further fix and that scenario was run once more. Passing scenarios were not rerun.

**Result:** 4 of 4 failed scenarios now pass. `Fixed Scenarios / Failed Scenarios = 4 / 4 = 100%`

| Scenario | Failure before | After fixes | Evidence |
| :--- | :--- | :--- | :--- |
| T1.2 | Stopped after the passport blocker | Fixed | `Do Not Book As Planned`, then every section; the Florence to Rome train moved off flight day. |
| T1.3 | No transit share given | Fixed | "about 20 of about 60 waking hours (roughly a third)"; both closure days caught. |
| T4.1a | Ready to Book with unchecked items | Fixed | `Viable With Adjustments`; the open travel-authorization check caps the verdict. |
| T4.1b | Planned around the closed Glória funicular | Fixed | "this plan does not depend on it"; no day uses it. |

The closure-day lists in both reference files were also corrected (Musée Rodin moved to Mondays, Reina Sofía to Tuesdays, Vatican Museums to Sundays).

**Still open:** the T1.3 transit share was given as "roughly a third" rather than a percentage.

Because each fixed scenario passed a single run, this shows the fixes work, not that they hold every time. `All Repeated Runs Passed = Not measured` after the fixes.
