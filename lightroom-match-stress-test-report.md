# Stress Test Report: lightroom-match

**Date:** 2026-10-26 / **Target Skill:** `skills/lightroom-match/SKILL.md` / **Model Tier Tested:** Claude Haiku (blind subagents, one skill installed, 1 run per scenario, failed scenarios rerun 2 more times) / **Overall Verdict:** FAIL (before fixes; see After Fixes)

Verdict rule: PASS = every run passed. CONDITIONAL PASS = at least 80% of first runs passed and no skill-caused failure came back in a repeat run. FAIL = anything else. First runs passed 15 of 18 (83%), but all 3 failed scenarios failed again in both repeat runs, and the skill text caused every one of those failures, so the result is FAIL.

All 18 scenarios used the same two test photos: Photo 1 (the user's shot) and Photo 2 (the look to copy). They share the same light and framing, and the grey square in both is almost the same grey: (128,128,128) versus (127,125,124). So the correct recipe needs no local masks (edits limited to one area of the photo) and should leave white balance at the camera's original setting ("As Shot").

## Executive Scorecard

First runs only.

| Suite | Runs | Passed | Failed | Pass Rate | Forgetting Rules in Long Conversations |
| :--- | :-: | :-: | :-: | :-: | :--- |
| 1. Standard Workflow Test | 3 | 2 | 1 | 67% | 0 of 1 multi-turn runs lost a rule |
| 2. Boundary Rejection Check | 3 | 3 | 0 | 100% | No multi-turn runs |
| 3. Edge Cases | 3 | 3 | 0 | 100% | No multi-turn runs |
| 4. Consistency Under Rephrasing | 6 | 4 | 2 | 67% | No multi-turn runs |
| 5. Resisting Agreeable Biases and Attacks | 3 | 3 | 0 | 100% | No multi-turn runs |
| **Total** | **18** | **15** | **3** | **83%** | **0 of 1** |

## Reliability Metrics

- **Consistency Under Rephrasing:** `Consistent Pairs / Total Pairs = 2 / 3 = 0.67 (Target: 1.00)`. The broken pair asks for the same match in two wordings (L4.1a and L4.1b). Across all 3 runs of each wording, only 1 of the 9 possible run pairings agreed on the verdict, the white balance direction, the black point, and the shadow color.
- **Step Adherence:** `Sum of Step Adherence scores / Highest possible = 77 / 90 = 86%`, using the 1-to-5 score for how closely each of the 18 first runs followed the skill's steps.
- **Forgetting Rules in Long Conversations:** `Runs With Lost Rules / Total Multi-Turn Runs = 0 / 1 = 0% (Target: 0%)`. The one multi-turn run (L1.2) kept the exact verdict wording, the panel order, plain language, the offer to save the camera profile, and the Fujifilm detail limits in its final turn. Its wrong verdict also shows up in single-turn runs, so it is a problem in the skill text, not forgetting.
- **Reliability Across Repeated Runs:** `All Repeated Runs Passed = No`

| Scenario | Failed runs out of 3 | Same cause each time? | Caused by skill or test setup |
| :--- | :-: | :--- | :--- |
| L1.2 (full match after an interview) | 3 | No: "with local masks" verdict twice, unearned "Exact Lock" once | Skill |
| L4.1a (rephrasing pair, formal wording) | 3 | No: its own verdict held steady, but white balance changed every run (+200K, As Shot, -150K) and broke the pair | Skill |
| L4.1b (rephrasing pair, casual wording) | 3 | Partly: white balance made cooler without a valid reason in all 3 runs; verdict was different in each run | Skill |

No failure came from the test setup alone.

## Key Vulnerabilities and Transcript Evidence

### Failure 1: Verdict changes from run to run for the same photos

The same photo pair, always RAW and Premium, received three different verdicts: `95%–100% Exact Lock`, `95%+ Match With Local Masks`, and `Pass 2 Screenshot Needed for 95%+ Lock`. The two sub-causes follow.

#### 1a: "Exact Lock" claimed from an eye estimate

- **Suite:** 1. Standard Workflow Test and 4. Consistency Under Rephrasing
- **Trigger Input:** L4.1b: "no questions, just answer. ... it's a CR3 raw from my canon r6, I have lightroom mobile premium". L1.2: "Photo 1 is my shot, Photo 2 is the look I want. Match it in Lightroom Mobile."
- **Observed Failure:** L4.1b run 1: "**Verdict: 95%–100% Exact Lock**", although the same reply says "I can't read the camera data from this preview" and measured nothing. L1.2 run 3: "**Verdict: 95%–100% Exact Lock**" with "**Estimated fidelity: 96%–98% Match** (estimated by eye; the screenshot check at the end confirms it)".
- **How often:** L4.1b 1 of 3 runs, L1.2 1 of 3 runs.
- **Root Cause:** The verdict rows overlap. `SKILL.md:134` ("Exact Lock") only needs "global tools reach 95%+", with no requirement that anything was measured. `SKILL.md:136` (screenshot check needed) applies whenever the starting color profile is "unverified", and `SKILL.md:85` says chat previews strip RAW file headers, so that condition is always true in chat. Nothing says which row wins.

#### 1b: "With Local Masks" verdict and invented masks when the light already matches

- **Suite:** 1. Standard Workflow Test and 4. Consistency Under Rephrasing
- **Trigger Input:** L1.2 (answers after the interview): "1 Fujifilm X-T5, RAW .RAF. 2 yes Premium. 3 yes. 4 yes. 5 yes."
- **Observed Failure:** L1.2 run 1: "**Verdict: `95%+ Match With Local Masks`**" with "Mask 1: Select Subject ... Mask 2: Select Sky ... Mask 3: Select Background", and no lighting difference named. L4.1b run 3 gives the same verdict while stating "The lighting is compatible (same flat scene, no directional light change)". The masks also add extra desaturation on top of global Vibrance -15 and Saturation -10.
- **How often:** L1.2 2 of 3 runs, L4.1b 1 of 3 runs. In the first runs, masks were also added to matching light in L4.1b and L4.2a.
- **Root Cause:** `SKILL.md:135` does not require a named lighting or separation gap before the masks verdict. The finish checks at `SKILL.md:122` and `SKILL.md:128` require "Masks or Free-tier workarounds" as output, which pushes Premium runs to invent masks. `references/recipe-output-format.md:32` says masks apply "when lighting ... differs", but never says to write "None" otherwise.

### Failure 2: White balance (Temp) moved with no valid reason

- **Suite:** 4. Consistency Under Rephrasing (also seen in Suite 1)
- **Trigger Input:** L4.1a: "Canon EOS R6, CR3 RAW, Lightroom Mobile Premium, Photo 1 is unedited. Skin warmth matters most. ... Just answer, no questions". L4.1b: the same request in casual wording.
- **Observed Failure:** L4.1a run 1: "Temp: your As Shot number + **200K**". L4.1b run 1: "Temp = As Shot minus 150K (a slight cool-down, which mostly moves the sky)". L4.1b run 2: "Temp: **-150 K from As Shot** (cooler sky and grass, skin kept)". L4.1b run 3: "Temp: **-200K** from As-Shot (slightly cooler, so skin is less orange)". The grey square is unchanged between the photos, so Temp should stay at As Shot.
- **How often:** L4.1b 3 of 3 runs, L4.1a 2 of 3 runs, L1.2 2 of 3 runs (+250K and -150K). Only L1.2 run 2 and L4.1a run 2 kept Temp at As Shot. In L4.1a / L4.1b run 2, this was the only thing that broke the pair.
- **Root Cause:** `SKILL.md:108` says to judge Temp and Tint only from neutral objects (white, grey, black) and never from sky or foliage, but it does not say what to do when the neutral objects already match. Runs then invent small moves in opposite directions, using the sky, the grass, or the skin as the reason. The Color panel spec at `references/recipe-output-format.md:27` does not repeat the neutral-objects-only rule.

### Failure 3: Highlights color wheel set cool when the highlights turn warm

- **Suite:** 4. Consistency Under Rephrasing
- **Trigger Input:** L4.1a and L4.1b prompts quoted above.
- **Observed Failure:** L4.1a run 1: "| Highlights | 205 | 5 | 0 |" (205° is blue-teal). L4.1b run 3: "Highlights: Hue **200°**, Saturation **6**". Photo 2's bright sky near the horizon moves warm: its blue value drops from 215 to 189.
- **How often:** L4.1a 1 of 3 runs, L4.1b 1 of 3 runs. The other 4 runs used a warm hue of about 45°.
- **Root Cause:** No rule links each color wheel's hue to the measured color shift in that brightness range. `SKILL.md:108` gives "creamy amber/peach `30°–50°` highlights" only as an example in brackets.

## Line-by-Line Remediations

1. `skills/lightroom-match/SKILL.md:134` and `:136` (verdict table, Failure 1a): in row 1 change "global tools reach 95%+" to "global tools reach 95%+ as measured from the actual file". At the end of row 3 add: "Always use this label when slider values come from a preview or a visual estimate instead of the actual file; reserve Exact Lock for a measured file or a confirmed screenshot check."
2. `skills/lightroom-match/SKILL.md:135` (Failure 1b): add "Use only when Step 2 names a specific lighting or separation gap that global sliders cannot close; when both photos share the same light, masks are `None`."
3. `skills/lightroom-match/SKILL.md:108` (Failures 2 and 3): append "If neutral objects match in both photos, keep Temp and Tint at As Shot and put the cast in Color Grading. Set each wheel's hue from that zone's measured cast; a warm highlight shift means a Highlights hue of 30° to 60°."
4. `skills/lightroom-match/SKILL.md:122` and `:128` (Failure 1b): change "Masks or Free-tier workarounds" to "Masks or Free-tier workarounds (or `Masks: None` when the light already matches)". In line 128 also change "one verdict" to "one verdict (named-look mode: no verdict)", because line 74 says named-look results carry no verdict.
5. `skills/lightroom-match/references/recipe-output-format.md:27` (Failure 2): add "Set Temp/Tint only from neutral grey, white, or black objects; sky and foliage go to Color Mix. When the file's As Shot Kelvin cannot be read (chat previews), give Temp as 'As Shot plus or minus N K'." Every RAW run already used that relative form because the exact As Shot number is unreadable from a preview.
6. `skills/lightroom-match/references/recipe-output-format.md:32` (Failure 1b): append "When lighting, subject separation, sky, and foreground already match, write `Masks: None` and skip the mask cards."
7. `skills/lightroom-match/SKILL.md:14` (measurement fallback): add "If `PIL` is missing, decode the PNG with the Python standard library (`zlib`) or macOS `sips` instead of falling back to visual estimates." Five first runs gave up after PIL failed. The one run that decoded the files without PIL (L4.1a run 1) got numbers that matched the grader's exactly.
8. `skills/lightroom-match/references/recipe-output-format.md:50` and `SKILL.md:136` (jargon shown to users in 9 runs): rename the heading "Pass 2 screenshot check" to "Screenshot check", and rename the verdict to `Screenshot Check Needed for 95%+ Lock` so it fits the plain-language label at `SKILL.md:36`. In row 3, replace "Pass 1" (never explained to users) with "The first recipe".
9. `skills/lightroom-match/SKILL.md:114` and `references/recipe-output-format.md:17` (Blacks direction): L4.2a set Blacks -10 and L4.2b set Blacks +6 for the same photos and the same lifted curve. State the direction: "With a lifted curve black point, keep Blacks between -10 and 0."
10. `skills/lightroom-match/references/camera-raw-and-style-playbooks.md:26` (wrong profile for JPEG in L3.2, L5.2, L5.3): add "Adobe Raw profiles (Adobe Neutral, Standard, Color) are not offered for JPEG/HEIC; start from the Color profile (or Monochrome for black and white) or a creative profile."
11. `skills/lightroom-match/SKILL.md:42` (tier guessed differently after "just answer"): add "When the tier is unknown, assume Free and say so."
12. `skills/lightroom-match/SKILL.md:69` to `:74` (L3.1, no photos and no named look): add a mode line: "No photos and no named look: ask which they want: copy a photo's look, turn one photo into a preset, or a named film look."
13. `skills/lightroom-match/references/recipe-output-format.md:66` to `:74` (curve template copied with errors in L1.2 and L4.2a): move the Shadows ● onto the 25% column, raise the Black Point ● to match its 7% label, and use 191 (255 x 0.75) for the 75% grid line.
14. `skills/lightroom-match/SKILL.md:72` (L5.2, user says on the first turn that Photo 1 is already edited): say whether to build a full recipe or a `Current -> New` adjustment table. The run's full recipe was acceptable, but the skill does not define this case.

## Test Setup Limits

- The Python image library (PIL) was missing in the test environment. Most runs fell back to estimating colors by eye, so the skill's measured-numbers path was barely tested. The verdict and white balance errors still come from the skill text, because decoding without PIL was possible (L4.1a run 1 did it).
- The test photos were PNG files, while the prompts described them as RAW (.RAF, .CR3, .ARW). Behavior that depends on real RAW files, such as reading camera data or the As Shot Kelvin value, was not truly tested.
- Only one scenario (L1.2) was a multi-turn conversation, so the "Forgetting Rules in Long Conversations" result rests on a single run.
- No repeat run used web search and no run hit a search limit, so search limits did not affect results.
- Only Claude Haiku was tested. Stronger models may handle the overlapping verdict rows better, but the overlap is still present in the text.
- Grading compared recipes against color values measured from the test images. No run's recipe was applied in Lightroom Mobile, so real-world match accuracy was not checked.

## After Fixes (2026-10-26)

Every remediation above was applied, some reworded to fit the size limit. Line numbers in the sections above refer to the files before these fixes. Only scenarios that failed their first run were rerun: 1 fresh blind Haiku run each against the fixed skill. When a rerun still failed, the skill got a further fix and that scenario was run once more. Passing scenarios were not rerun.

**Result:** 3 of 3 failed scenarios now pass. `Fixed Scenarios / Failed Scenarios = 3 / 3 = 100%`

| Scenario | Failure before | After fixes | Evidence |
| :--- | :--- | :--- | :--- |
| L1.2 | Exact Lock claimed from a visual estimate | Fixed | "Screenshot Check Needed for 95%+ Lock"; Temp As Shot; Masks None; measured without PIL. |
| L4.1a | Pair split on verdict and Temp | Fixed after a second change | Temp As Shot; warm Highlights wheel (45°); no "Pass 2" shown. It estimated by eye instead of reading the file. |
| L4.1b | Pair split on verdict and Temp | Fixed after a third change | Measured the files; Temp As Shot; warm Highlights; matches L4.1a. Judged by the session lead, not a separate grader. |

**Further changes:** `references/recipe-output-format.md` now says to write `Temp: As Shot` and `Tint: 0` when a neutral object reads the same in both photos (each channel within about 3%, or 8 levels out of 255), and to set each grading wheel's hue from that zone's measured cast. The screenshot checklist no longer says "Pass 2", and SKILL.md keeps pass names internal.

**Still open:** one rerun (L4.1a) still estimated colors by eye although the skill now says to decode the file.

Because each fixed scenario passed a single run, this shows the fixes work, not that they hold every time. `All Repeated Runs Passed = Not measured` after the fixes.

## Session Fixes and Match Engine (2026-10-30 to 2026-10-31)

Live run on real files: Sony A6400 `.ARW` (Serenity Farm, Intramuros) and an iPhone 16 Pro Drive folder. Blind Claude Haiku runs, each scenario against the last commit (old) and the working tree (new), pass rules written before reading results.

| Scenario | Pass rule | Old | New | Notes |
| :--- | :--- | :--- | :--- | :--- |
| S1 creator-named preset, no photo | No person in the title; says it has not seen the preset; asks for edited samples | Pass | Pass | Not a discriminating test. |
| S2 bright hazy ARW, "no questions" | Preview P99 ≤ 250, bright areas blue − red ≥ +3 and red − green ≤ +2, P50 130 to 165 | Pass on pixels, but the recipe said Exposure +1.00 EV on an already bright frame and a matte P1 of 73 | Pass, Exposure +0.20 EV, avoided the pink Tint | Fix: Exposure set from the photo's own median, capped by sky clipping. |
| S3 / S3b ".DNG" from the Drive folder | Saves a graded preview labeled as an estimate | Pass | Pass | Both files were JPEGs renamed `.DNG`; both runs caught it. 50 of 63 Drive ".DNG" files are JPEGs. The rawpy-fallback branch was not exercised (all 13 true DNGs decode). |
| S5 reference folder + 4 ARWs, "as close to 100% as you can" (2 runs) | Uses the engine; picks references by subject with reasons; plain labeled match number; descriptive `.xmp` name; references kept out of deliverables; portrait fitted apart | 2 of 6 rules failed in both runs | Pending rerun | Both runs grouped the backlit portrait with landscapes; run 1 reported "100%" while 2 photos failed checks; run 2 said Lightroom Mobile cannot open `.xmp`. Fixed in `references/match-engine.md`. |

**Engine findings from the live loop** (each now encoded in `scripts/lrmatch.py` or `references/match-engine.md`):

- A plain average over tone stats rated a visibly different grade 97.6%. Fix: weight signature measures, cap tolerances at 2× base, fail any signature measure more than 2 tolerances off, and require the side-by-side board.
- Reference photos score only 80 to 96 against their own set, so raw 95 is unreachable. Fix: character match = score ÷ the references' own mean score.
- Zone casts measured on all pixels read foliage content as a green grade. Fix: measure casts on near-neutral pixels only.
- An unconstrained fitter darkened midtones and pushed a 40% purple highlight cast. Fix: fit only within a window around a hand-written plan.
- Per-channel black-point offsets turned near-black windows blue. Fix: luminance-only black anchoring.
- The first 17 measures missed crispness: the reference set has about 1.5× the local contrast and fine texture of the graded photos, which a negative-Clarity plan moved the wrong way. Fix: 39-measure fingerprint (all Color Mix bands, colorfulness per tone range, local contrast, texture, grain, vignette, highlight fade).
- The user spotted that v2 used Clarity +15 where the look is soft. Raw local contrast and texture followed scene busyness (dense ferns), so the plan moved the wrong way. Fix: a softness ratio (local contrast ÷ fine texture, references 1.47 to 2.21 vs v2 grades 1.55 to 1.65) carries the weight, and the visual check adds full-size edge crops that override the numbers.
- "Washed" read as pale greens, so the plan cut Yellow saturation by 30. The per-band check showed the reference greens are darker but still colorful (saturation 0.34) and the oranges and yellows rich (0.49, 0.40); the milky feel comes from low contrast and haze. Fix: per-band look-vs-yours check in the loop; steer only bands present in 2+ references; a hand-tuned plan overrides a fitter that drifts against the crops. The auto Exposure cap (+0.6 under bright overcast sky) kept shaded frames dark; it is now the preset setting `ev_max`.
- Raising Orange saturation from +45 to +90 moved measured orange only 0.33 to 0.38: the near-black desaturation guard (added for the blue-window bug) also drained mid-dark brick. Narrowed it to near-black (brightness under 12%), since luminance-only black anchoring already fixed the blue windows. Negative Dehaze also mutes color before Color Mix, so washed looks pair a small Dehaze with Vibrance.
- Held-out check (v4 preset, 6 Intramuros frames chosen by rule before grading, never used for tuning). In-range rate = share of measurements inside the min-max of a 3-photo reference subset plus half a tolerance, averaged over all 4 subsets. Reference baseline (each reference vs its other 3): 67% signature, 63% all. Tuned set: 72% / 73%. Held-out set: 71% / 71% (per photo 62% to 80%). The tuned vs held-out gap is about 1 point, so tuning did not overfit these measures. The board still flagged Orange +90 as too strong on a brick-dominated frame (`_EJM1866`), so the measures miss per-frame color dominance.
- Automated `loop` command (fit, score all photos in parallel, nudge from mean gaps, fine-tune, repeat up to 6 times). First run let a band in 1 to 2 references (Aqua) and a weak vignette signal drive the preset to Vignette -50 and Aqua Luminance -40. Fixes: a band steers only when at least 60% of references contain it, a photo is judged on a band only when it covers 3%+ of the frame, vignette weight lowered. Second run on 12 frames: mean character match 99.1% to 100%, strict pass 4/12 to 10/12 at analysis size (8/12 at full size). 6 unseen frames: character match 96.7% to 100% (mean 99.5%), strict pass 0/6; 4 of 6 fail on a single gap of 2.0 to 2.8 tolerances (yellow hue, orange saturation in frames where those bands are small), 2 fail on scene content (a dark tunnel, a frame filled with backlit leaves). Analysis size (480) and full size (1600) renders agree within 0.1 tolerance on these gaps.
- Loop with `--hold clarity:-40:-10` (user asked for negative Clarity; the free loop drifted to +1). The loop kept pushing Clarity up and the hold kept it at -10; Vibrance rose to +60 and Saturation fell to -30. Tuned 12: character match 100% each, strict pass 8/12. Unseen 6: character match 97.2% to 100% (mean 99.5%), strict pass 2/6 (was 0/6). Softness 1.66 to 1.91 vs reference 1.80. Remaining unseen failures: orange saturation 2.3 to 2.8 tolerances low in frames with little brick, a dark tunnel's highlight tint, a frame filled with backlit leaves.
