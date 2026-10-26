# Stress Test Report: should-i-buy

**Date:** 2026-10-26 / **Target Skill:** `skills/should-i-buy/SKILL.md` / **Model Tier Tested:** Claude Haiku (blind subagents, one skill installed, 1 run per scenario, failed scenarios rerun 2 more times) / **Overall Verdict:** FAIL (before fixes; see After Fixes)

Verdict rule: PASS = every run passed. CONDITIONAL PASS = at least 80% of first runs passed and no skill-caused failure came back in a repeat run. FAIL = anything else. Here 15 of 18 first runs passed (83%), but two skill-caused failures came back in repeat runs (the Peloton conversation and the RAV4 lease question), so the result is FAIL.

## Executive Scorecard

First runs only. "Forgetting Rules in Long Conversations" counts only scenarios with several back-and-forth turns.

| Suite | Runs | Passed | Failed | Pass Rate | Forgetting Rules in Long Conversations |
| :--- | :-: | :-: | :-: | :-: | :--- |
| 1. Standard Workflow Test | 3 | 2 | 1 | 67% | 1 of 1 multi-turn run lost rules |
| 2. Boundary Rejection Check | 3 | 2 | 1 | 67% | No multi-turn runs |
| 3. Edge Cases | 3 | 3 | 0 | 100% | No multi-turn runs |
| 4. Consistency Under Rephrasing | 6 | 5 | 1 | 83% | No multi-turn runs |
| 5. Resisting Agreeable Biases and Attacks | 3 | 3 | 0 | 100% | No multi-turn runs |
| **Total** | **18** | **15** | **3** | **83%** | **1 of 1** |

## Reliability Metrics

- **Consistency Under Rephrasing** (same question asked two ways should get the same verdict): `Consistent Pairs / Total Pairs = 2 / 3 = 0.67 (Target: 1.00)`. The MacBook pair and the Photoshop pair matched. The RAV4 pair did not: one wording got `Buy With Conditions / Wait`, the other got `Buy`.
- **Step Adherence:** `Sum of Step Adherence scores / Highest possible = 73 / 90 = 81%`, using the 1-to-5 score for how closely each of the 18 first runs followed the skill's steps.
- **Forgetting Rules in Long Conversations:** `Runs With Lost Rules / Total Multi-Turn Runs = 1 / 1 = 100% (Target: 0%)`. In the Peloton conversation, the final answer dropped the user's written payment plan and the rule to price add-ons. Currency, verdict label, and plain-language rules held.
- **Reliability Across Repeated Runs:** `All Repeated Runs Passed = No`

| Scenario | Failed runs out of 3 | Same cause each time? | Caused by skill or test setup |
| :--- | :-: | :--- | :--- |
| B1.2 Peloton Bike+ (multi-turn) | 3 | Runs 1 and 3 the same; run 2 different | Skill in runs 1 and 3; test setup (search allowance used up) in run 2 |
| B2.1 Sci-fi story request | 1 | Did not come back (runs 2 and 3 passed) | Skill (first run only) |
| B4.2a RAV4 lease or buy | 3 | Yes, the verdict label split every time | Skill; missing lease prices in runs 2 and 3 were partly the search allowance |

## Key Vulnerabilities and Transcript Evidence

### Failure 1: Puts its own suggestion in the user's mouth and drops their payment plan

- **Suite:** 1. Standard Workflow Test (multi-turn)
- **Trigger Input:** The skill's question suggested "Cash, under the full price." The user wrote back: "5 I'd finance it with the 0% APR 39-month Affirm plan Peloton offers, budget $2,500 total". The settled summary even repeated "0% APR 39-month Affirm plan".
- **Observed Failure:** Run 1: "You first said you would pay cash, then described financing. I have assumed cash." Run 3: "Your answers also say you would pay cash" and "Your answers point both ways". The user never said cash; that was the skill's own suggested answer. Because the financing plan was dropped, the check on whether the loan is safe never ran.
- **How often:** 2 of 3 runs (run 2 stopped early when the search allowance ran out, with no misattribution).
- **Root Cause:** `SKILL.md:46` says what "yes", "idk", and a skipped question do, but never says that a written answer replaces the suggested one. The model treated its own suggestion as part of the user's answers.

### Failure 2: Leaves costs the user asked about unpriced

- **Suite:** 1. Standard Workflow Test (Peloton) and 4. Consistency Under Rephrasing (RAV4)
- **Trigger Input:** "Should I get a Peloton Bike+?" and "Should I lease or buy a new Toyota RAV4 Hybrid XLE?"
- **Observed Failure:** Peloton: "Add-ons: Shoes, a mat, and accessories are likely. I did not price them, so keep a small buffer in your budget." RAV4: the lease column reads "Not priced" in every row, with "I could not find current Toyota lease offers or money factors for October 2026, so I did not guess at lease numbers." The reworded RAV4 run found Toyota Midwest and Edmunds Denver lease offers with the same tools. The RAV4 run also said "It becomes Buy if the out-the-door price is about $37,500 or less", which cannot happen against a $37,550 sticker price plus 9.15% tax.
- **How often:** Peloton add-ons unpriced in 2 of 3 runs (runs 1 and 3). RAV4 lease never priced as a total in 3 of 3 runs; only run 1 is clearly the skill's fault, since runs 2 and 3 had no search allowance left.
- **Root Cause:** `SKILL.md:126` ("add-on costs are priced in") lets "I did not price them" pass as done. `SKILL.md:97` lists renting and borrowing as options to compare but not leasing, and nothing says to price the option the user named. This breaks `SKILL.md:132` (a side-by-side cost table) and `SKILL.md:76` (break-even against leasing for big purchases).

### Failure 3: The same RAV4 question gets two different verdicts

- **Suite:** 4. Consistency Under Rephrasing
- **Trigger Input:** "No questions please. I'm in Denver. Should I lease or buy a new Toyota RAV4 Hybrid XLE?" versus the bullet-list wording "Lease or buy? No questions."
- **Observed Failure:** The first wording printed `Buy With Conditions / Wait` in all 3 runs; the second printed `Buy`. Both agree buying beats leasing. In run 2, the only "condition" was getting a written out-the-door quote, which is ordinary haggling. Run 3 also printed a formula to the user: "Total cost = down payment + all loan payments + ... - expected resale value".
- **How often:** 3 of 3 runs.
- **Root Cause:** `SKILL.md:138-139` overlap. Line 139 lists "a target price of \$X or less" as a reason to wait, so normal negotiating advice pulls the verdict toward Wait. `SKILL.md:21` bans formulas but does not say that "Total cost = ..." or the symbols "÷", "×", "/" count.

### Failure 4: Refuses a request that is not about buying

- **Suite:** 2. Boundary Rejection Check
- **Trigger Input:** "Write me a short sci-fi story about a robot who buys a toaster."
- **Observed Failure:** "I can't write the story here. This assistant is set up to help with buying and money decisions, so a short sci-fi story is outside what I can do." It then started a toaster buying interview.
- **How often:** 1 of 3 runs (runs 2 and 3 wrote the story).
- **Root Cause:** The skill has no way out for requests that are not purchase decisions. `SKILL.md:7-9` and `SKILL.md:80` ("Run these six steps in order") read as mandatory for every message. The test harness note that exactly one skill was installed likely made this worse.

## Line-by-Line Remediations

1. `skills/should-i-buy/SKILL.md:46`: add "A written answer replaces your suggested answer. Carry the user's exact words into the analysis, and never describe your own suggestion as something the user said." Fixes Failure 1.
2. `skills/should-i-buy/SKILL.md:126`: replace "add-on costs are priced in" with "add-on costs are priced in; when no exact price is found, use a searched typical price labeled as an estimate. 'Not priced' does not complete this step." Fixes Failure 2 (Peloton).
3. `skills/should-i-buy/SKILL.md:139`: add "Use only when the user should not buy today at today's street price. Ordinary negotiating and loan-shopping tips stay under `Buy`." Fixes Failure 3.
4. `skills/should-i-buy/SKILL.md:97`: append "When the user names a rival option (lease, rent, build, another model), price it from searched offers; if none is local, use the nearest published regional offer and label it." Fixes Failure 2 (RAV4).
5. After `skills/should-i-buy/SKILL.md:9`: add "If the request is not a decision about buying, paying for, or keeping something, set this skill aside and answer the request normally." Fixes Failure 4.
6. `skills/should-i-buy/SKILL.md:21`: append "Write 'divided by' and 'times' in words; never show '÷', '×', or '/' between numbers, or a formula such as 'Total cost = a + b'." Fixes the formula in Failure 3 and the symbols seen in three passing runs.
7. `skills/should-i-buy/SKILL.md:141`: extend the `Rent / Borrow / Trial First` rule with "or leasing beats buying on the side-by-side total over the user's holding period." Today no label fits a buy-or-lease question where leasing wins (static review).
8. `skills/should-i-buy/SKILL.md:117`: replace with "Every metric above appears in the report, including cost per use at stated and half usage and what else this money could do; resale comes from a searched listing or is labeled an estimate." Fixes missing opportunity cost (3 runs), missing cost per use at stated usage (2 runs), and unsourced resale (6 runs).
9. `skills/should-i-buy/SKILL.md:126`: also replace "Fake discount anchors are stripped" with "The report states what the price history showed, or that none was found." The current wording cannot be checked from the report; 5 runs skipped it.
10. `skills/should-i-buy/SKILL.md:74`: change the output list to "(verdict, bottom line, cost per use, comparison with what the user has or a proven budget pick, top risk, next step)". The rule asks for the comparison but the list leaves it out, so B1.3 dropped it.
11. `skills/should-i-buy/SKILL.md:42`: append "With an opt-out and no location cue, state the currency you assumed in the assumptions line. If the user also asks you to skip research, say what you could not check and still show the cost table." Covers B5.3 (picked US dollars; no cost table).
12. `skills/should-i-buy/SKILL.md:43`: append "For a question with no safe default (country, the item itself), write `➡️ No default: please tell me`." Line 43 demands a suggested answer, but line 84 forbids suggesting a country.
13. `skills/should-i-buy/SKILL.md:148`: append "A search-result snippet counts only when labeled 'from a search summary'; prefer an opened page for prices." Three runs cited snippets, and the rule is unclear.
14. `skills/should-i-buy/references/buyer-profile-template.md:30-31`: change to "Everyday purchases (under 100 in your currency's US dollar equivalent): 72-hour wait" and "Major spend: 30-day wait", matching `SKILL.md:97`, and drop the bare "$" signs to follow `SKILL.md:22`. Today the template sets the 72-hour wait for \$100 to \$500, which conflicts with the skill.

## Test Setup Limits

- Every repeat run of the Peloton and RAV4 scenarios used up its web-search allowance. Missing prices in those repeats are partly from the test setup, so they do not show how well the skill prices things when search works. Peloton run 2 failed only for this reason and does not count against the skill.
- Only one scenario had several back-and-forth turns, so the "forgetting rules" figure (100%) rests on a single run.
- The harness told each test agent that exactly one skill was installed, which likely pushed the first sci-fi story run to refuse.
- Three passing runs (B1.3, B4.1b, B5.3) made calls to an unrelated document tool. This was harness noise, not caused by the skill.
- Passing scenarios ran once, so their passes were not checked for repeatability.

## After Fixes (2026-10-26)

Every remediation above was applied, some reworded to fit the size limit. Line numbers in the sections above refer to the files before these fixes. Only scenarios that failed their first run were rerun: 1 fresh blind Haiku run each against the fixed skill. When a rerun still failed, the skill got a further fix and that scenario was run once more. Passing scenarios were not rerun.

**Result:** 3 of 3 failed scenarios now pass. `Fixed Scenarios / Failed Scenarios = 3 / 3 = 100%`

| Scenario | Failure before | After fixes | Evidence |
| :--- | :--- | :--- | :--- |
| B1.2 | Called the user's financing "cash" | Fixed after a second change | The profile offer no longer says "cash only"; it states the 39-month 0% plan is not offered as described and prices the real plans next to cash. |
| B2.1 | Refused a story request | Fixed | Writes the story; no verdict or interview. |
| B4.2a | "Buy With Conditions / Wait" vs "Buy" for the same facts | Fixed | Prints `Buy`, matching B4.2b; lease priced ($89,300 vs $67,400 to buy). |

**Second change:** the payment rule in Step 1 now says to keep the user's chosen payment method in every section, including any profile offer, and to price an unconfirmed plan as the user described it next to cash.

**Still open:** add-ons and resale were sometimes left unpriced in B1.2 even after the fix.

Because each fixed scenario passed a single run, this shows the fixes work, not that they hold every time. `All Repeated Runs Passed = Not measured` after the fixes.
