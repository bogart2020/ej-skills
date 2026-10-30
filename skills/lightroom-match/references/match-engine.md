# Match Engine Loop

Build a preset from a set of reference photos (a folder, or a web page the user named), apply it to the user's photos, and loop until the look matches. The engine is `lrmatch.py` in the `scripts` folder next to `SKILL.md`; run it by that path. It needs Python 3 with `numpy` and `pillow`; `rawpy` adds camera RAW decoding, and macOS `sips` covers files `rawpy` cannot open. Run every command with `python3 -I`, and keep all files in one work folder.

The engine renders an approximation of Lightroom, so its previews guide the recipe. Lightroom's own render is the final word, through the screenshot check.

## 1. Collect the references

1. Use a folder the user gave, or run `fetch <url> --out refs/` on a page the user named (up to 30 images; sources go to `refs/SOURCES.txt`).
2. Run `sheet refs/ --out refs_sheet.jpg` and view it. Pick 4 to 8 frames that carry the look **and share the subject type of the user's photos** (foliage with foliage, street with street, portraits with portraits). Drop logos, product shots, and frames with a clearly different grade.
3. Keep reference images in the work folder only. They are for measurement: never ship, republish, or upload them.

**Done when**: 4 to 8 chosen reference frames share the user's subject type, and each dropped frame has a one-line reason.

## 2. Measure the look

Run `measure <chosen refs> --out target.json`. It records the look's fingerprint: 9 tone percentiles and the highlight fade to white, the color cast on near-neutral areas (shadows, midtones, highlights), colorfulness per tone range, hue, saturation, and brightness of every Color Mix band present, local contrast, fine texture, softness (their ratio), grain, and corner darkening. Raw local contrast and texture follow how busy the scene is (ferns read as punchy); read crispness from softness, where a higher value means negative Clarity and Texture glow. It also scores the references against their own set: that mean is **100% character match**, because a user photo can only be as close to the look as the reference photos are to each other.

**Done when**: `target.json` exists and you can state the look's signature in one plain sentence per item: black floor, highlight color, midtone tint, band colors, colorfulness by tone, crispness (local contrast and texture), grain, and vignette.

## 3. Plan the preset

Write `plan.json` by hand from the signature and the closest playbook archetype: Light sliders, Temp/Tint offsets, Color Mix for the bands that carry the look, Color Grading (`grade_shadows`, `grade_midtones`, `grade_highlights` as `[hue, sat]`), Clarity and Texture in the direction the crispness numbers point, Dehaze, Vignette, Grain. Omitted keys stay at 0. Per-photo anchors (Exposure from `target_p50`, black floor `black_p1`, white balance `wb_target`) come from the target automatically; they stand for the Exposure, Blacks, and Temp/Tint the user sets per photo.

Group the user's photos before fitting: write one line per photo naming its subject (person, landscape, architecture, interior) and light (sun, overcast, backlit, artificial). A photo where a person is the main subject, or a backlit or artificially lit frame, goes in its own group. Fit one preset per group.

**Done when**: every signature item maps to at least one planned setting, and the photos are grouped.

## 4. Fit, grade, and check (the loop)

1. `loop --target target.json --photos <group photos> --start plan.json --out preset.json` runs the loop itself: score every photo in parallel, nudge the setting tied to each signature measure that is off on average, fine-tune around the nudged plan, and repeat until the mean character match reaches 95% with every photo passing, or 6 loops ran (`preset_loop_log.json` records each loop). `fit` is the single-pass version. When the crops or the user fix a setting's direction (for example negative Clarity for a soft look), pass `--hold clarity:-40:-10` so the loop stays inside that range.
   Before the loop, set aside 4 to 6 photos of the same group by rule (not by look) as a held-out check, and grade them with the final preset afterwards; report their result next to the tuned set's.
2. `grade <group photos> --preset preset.json --target target.json --out graded/ --refs <chosen refs>`. Read `graded/qa.json` (per photo `character_match_pct`, `numbers_pass`, `clipped_pct`, the 3 largest gaps) and each `graded/<photo>_report.txt`, which lists every fingerprint measure, look vs yours, worst first, with the slider it points to.
3. View `graded/board.jpg` (graded photos above, references below). Judge the character with your eyes: color of skies and highlights, foliage, black depth, overall brightness, skin. Then crop branches or edges against sky at full size in one graded photo and one reference, and compare edge softness and glow; when the numbers and the crops disagree, the crops win and the plan changes.
4. Check every Color Mix band the references contain (the `hue`, `saturation`, `brightness` rows in each report): state look vs yours per band, and steer only bands present in at least 2 references.
5. When numbers or eyes fail, change `plan.json` along the named gap (for example, a sky warmer than the references: cooler highlight grading), then return to step 1. When the fitter drifts back toward a look the crops reject, grade straight from the hand-tuned plan instead.

Call a photo matched only when `numbers_pass` is true, even when its percentage reads 100% (the percentage is capped).

**Done when** every photo in the group shows `numbers_pass: true` (95%+ character match, no signature gap over 2 tolerances, highlights clipped 0.5% or less) **and** the board passes the visual check, or 6 loops ran. After 6 loops, report the remaining gaps in plain words, pick the matching verdict (usually `Lighting or Time-of-Day Mismatch` when the scenes differ), and suggest source frames closer to the references.

## 5. Ship

Ship only what passed step 4, or what the user accepted with its named gaps.

1. Run `xmp --preset preset.json --name "<descriptive name>" --out <name>.xmp`. Name it descriptively, never after a person. Lightroom Mobile imports `.xmp` presets from the Presets panel menu (Import Presets); unzip archives first.
2. Deliver the graded JPEGs, the before/after sheets, the `.xmp`, and the Lightroom Mobile recipe (from `preset.json`, laid out per `recipe-output-format.md`). List the per-photo Exposure, Blacks, and Temp/Tint the engine used, since the preset leaves those to each photo.
3. Report each photo's character match as a labeled number ("Character match: 96%, where 100% means as close as the reference photos are to each other").

**Done when**: the user has the files and recipe, every number shown is labeled in plain words, and the report ends with the screenshot-check prompt.

## Plain-language labels

| Engine term | Say to the user |
| :--- | :--- |
| `character_match_pct` | Character match (100% = as close as the reference photos are to each other) |
| `numbers_pass` | Passed the measured checks |
| `target.json` / signature | The look's measured fingerprint |
| `wb_target`, `black_p1`, `target_p50` | Per-photo white balance, black level, and brightness |
| Board | Side-by-side check against the reference photos |
