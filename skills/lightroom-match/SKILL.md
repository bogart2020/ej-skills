---
name: lightroom-match
description: Replicate a reference photo's color grade, tone curve, and look onto a source or RAW photo in Adobe Lightroom Mobile at 95% to 100% fidelity, reverse-engineer any photo's edit into exact Lightroom Mobile sliders, visual curves, and masks, or fine-tune an in-progress Lightroom Mobile edit from a screenshot.
license: MIT
---

# Lightroom Match

Copy the look of **Photo 2 (reference)** onto **Photo 1 (source)** in **Lightroom Mobile** at **95% to 100% fidelity**, with exact numbers for every panel in toolbar order and a **Pass 2 screenshot loop**.

## Environment adaptation

- **Chat** (Claude Desktop, mobile, web): check attached photos, history, and memory for camera and app context. With a code sandbox, measure the photos directly; otherwise run the visual 5-zone and 8-band audit. To save a camera baseline, output a copyable snippet following [`references/photo-profile-template.md`](references/photo-profile-template.md).
- **Code and CLI**: read `.agents/photo-profile.md` or `~/.agents/photo-profile.md` before asking questions. When image files are local, use Python (`PIL` / `numpy`) for EXIF, exact luminance percentiles, and per-zone casts before computing slider deltas. If `PIL` is missing, decode the image with the standard library (`zlib` for PNG) or macOS `sips`; never fall back to visual estimates while the file is readable.

## Plain-language output

The bolded terms are your working vocabulary. Everything the user sees is everyday language a phone photo editor understands:

- Print the **user-facing label** from the table below wherever an internal term would appear.
- Show adjustments as labeled numbers and thumb-drag directions ("drag the bottom-left Black Point straight up about a quarter of the first grid box to `(0%, 6%)`"), never color-science equations.
- Keep step, tier, gate, and pass names (Pass 1, Pass 2) internal: describe the work by what it does (*"matching how your Sony RAW file handles skin tones and greens"*).
- When an app term is unavoidable (**ProRAW Profile Amount**, **Point Curve**, **Color Mix**, **Luminance Mask**), say where to tap it the first time it appears.

| Internal term | User-facing label |
| :--- | :--- |
| Recipe-flipping variables | Your camera, file type, and Lightroom Mobile setup |
| Photo 1 (Source) / Photo 2 (Reference) | Your photo to edit (Photo 1) / The look you want to copy (Photo 2) |
| Camera RAW sensor baseline / `ColorMatrix` | How your camera or phone naturally renders colors |
| `ProfileGainTableMap` (Apple ProRAW) | Apple's built-in Smart HDR tone processing (the ProRAW Profile slider) |
| 5-Zone Tonal Decomposition | How dark the blacks, shadows, midtones, highlights, and whites are |
| Lifted black point / rolled-off white point | Matte film fade in the blacks / soft, creamy highlights |
| 8-Band Chromatic Decomposition (HSL) | Individual color shifts (Hue, Saturation, Luminance in Color Mix) |
| 3-Way Color Grading | Shadow, Midtone, and Highlight color wheels |
| Scene & Lighting Physics Gate | Whether the lighting in both photos matches (and what local masks fix) |
| Pass 2 Delta Calibration | Screenshot check to dial in the final 1% to 5% |

## Interview rounds

1. Ask at least one round on every run. Skip only when the user says "just answer", "no questions", or equivalent; then state your file-format, camera, and Lightroom Mobile tier assumptions in one line at the top. When the tier is unknown, assume Free and say so.
2. The **frontier** is every open question whose prerequisites are settled. Ask the whole frontier in one round, number each question, give your recommended answer, and word it so "yes" accepts the recommendation. Then stop and wait.
3. Check the images, EXIF, photo profile, and history first; never ask for a fact you can see or the user already stated. When context only suggests an answer, turn it into a quick confirmation.
4. Recompute the frontier after each answer. A question that depends on another open question belongs to a later round.
5. "Yes", "idk", or a skipped question accepts your recommendation. When the user hands you the choice ("you decide", "whatever you think"), adopt your recommendations for every open question, list them as assumptions, and start without another round.
6. When the frontier is empty, summarize the setup in 2 to 4 bullets and ask "Ready for me to generate your Lightroom Mobile recipe?" Start once the user confirms.

Copy this format exactly, keeping the ❓ and ➡️ markers and the `---` line between questions:

```
❓ **Q1** - **<short title>**: <question in everyday words, with options when useful>

➡️ <your recommended answer>

---

❓ **Q2** - **<short title>**: <question in everyday words, with options when useful>

➡️ <your recommended answer>
```

## Reference pointers

- **Before Step 2**, read [`references/camera-raw-and-style-playbooks.md`](references/camera-raw-and-style-playbooks.md) for Photo 1's camera baseline and pre-offsets, the starting Profile list, percentile formulas, look archetypes, and the Free-tier workaround table.
- **Before Steps 4 to 6 and in Pass 2 mode**, read [`references/recipe-output-format.md`](references/recipe-output-format.md) for every panel's fields and value ranges, the report layout, and the 4x4 Tone Curve template.
- **When saving a profile** in Step 6, read [`references/photo-profile-template.md`](references/photo-profile-template.md).

## Modes

- **No photos and no named look**: ask which they want: copy a photo's look, turn one photo into a preset, or a named film look.
- **Full two-photo replication** (Photo 1 + Photo 2): run all 6 steps and deliver the full recipe plus the Pass 2 prompt.
- **Pass 2 screenshot calibration** (user sends their edited Photo 1): compare it (and any visible histogram) against Photo 2, isolate the remaining 1% to 10% gap in exposure, white balance, skin-tone orange luminance, shadow tint, or black-point fade, and output a **Pass 2 Fine-Tuning Delta Table** (`Slider | Current Value -> New Value | Why`). If the first message says Photo 1 is already edited, use this table when its current values are known (screenshot or stated); otherwise build a full recipe from `Reset`.
- **Single-reference reverse-engineering** (only Photo 2): ask which camera and file format the preset is for, decompose Photo 2's edit, and build a reusable preset for that camera.
- **Named look, no photo** (a film stock or style such as Portra or teal and orange): use the playbook's matching look archetype as Photo 2, settle only camera, file format, and tier, and label the result a starting preset, with no verdict label or fidelity percentage.

## Replication sequence

Run these six steps in order.

### Step 1: Verify the photos, load the gear profile, and interview the user

1. Read the photo profile or history for camera, file format, and tier. Confirm the photos your mode needs are attached and which is which; if one is missing or ambiguous, make that the first question.
2. Settle the **5 recipe-flipping variables**:
   - **Photo mapping and clean slate**: which image is Photo 1 and Photo 2, and whether Photo 1 is unedited (`Reset`) or already has a preset or profile.
   - **Camera and file format in Lightroom Mobile**: exact body or phone, and whether the file is camera RAW, computational phone RAW (Apple ProRAW, Samsung Expert RAW), or 8-bit JPEG / HEIC. Chat previews strip RAW headers, and `Temp` is Kelvin for RAW but `-100 to +100` for JPEG/HEIC.
   - **Tier**: **Premium** (Masking and Point Color) or **Free** (global sliders, Tone Curve, Color Mix, Color Grading only).
   - **Priority look anchors**: what in Photo 2 matters most (skin warmth, matte blacks, muted greens), and whether to keep Photo 1's time-of-day feel or fully adopt Photo 2's cast.
   - **Screen check**: True Tone, Night Shift, or Eye Comfort Shield turned off while editing, so screen warmth does not skew Pass 2.
3. Run **Interview rounds** on every unsettled variable, flagging any lighting or exposure mismatch you can already see.

**Completion criterion**: Both photos are present and unambiguously identified, and the user has confirmed all 5 variables (or opted out, with assumptions stated at the top).

### Step 2: Check lighting feasibility and neutralize the camera baseline

1. **Separate transferable grade from capture physics**: compare light direction and hardness, clipped channels, palette presence (foliage or sky Photo 1 lacks), and depth of field. Decide whether global sliders reach 95% or whether local masks (or Free-tier workarounds) are needed.
2. **Pick Photo 1's starting Profile and pre-offsets** from the playbook for its exact camera and file format.

**Completion criterion**: Photo 1's starting Profile and sensor pre-offsets are chosen for its camera and format, and every lighting difference is mapped to a specific local mask or Free-tier workaround.

### Step 3: Measure the 5 tonal zones and 8 color bands

1. **Tonal zones**:
   - **Black Point** (`0%–10%`): pure blacks (`0%`) or lifted matte fade (`4%–12%`).
   - **Shadows** (`10%–30%`): openness and dark contrast.
   - **Midtones & Skin** (`30%–70%`): exposure and skin luminance (`55%–68%` natural radiant, `42%–54%` moody low-key).
   - **Highlights** (`70%–90%`): sky and bright background.
   - **White Point** (`90%–100%`): crisp full whites (`98%–100%`) or creamy film highlights pulled to `86%–95%`.
2. **Color**: for each Color Mix band (`Red`, `Orange`, `Yellow`, `Green`, `Aqua`, `Blue`, `Purple`, `Magenta`), the hue shift, saturation, and luminance. Judge Temp, Tint, and grading casts only from neutral objects (white, grey, black), never from sky or foliage, which Color Mix handles. If neutral objects match in both photos, keep Temp and Tint at As Shot and put the cast in Color Grading, setting each wheel's hue from that zone's measured cast (a warm highlight shift means a Highlights hue of 30° to 60°).

**Completion criterion**: All 5 zones, all 8 bands, and the shadow/midtone/highlight casts are stated as explicit deltas from Photo 1's current state to Photo 2's target.

### Step 4: Build the Light panel and Tone Curves

Translate the tonal deltas into exact **Light** sliders and **Tone Curves** using the fields in `references/recipe-output-format.md` section 1. Set `Blacks` and `Whites` to the pre-curve range so they work with the curve's black and white points instead of canceling them; with a lifted curve black point, keep Blacks between -10 and 0.

**Completion criterion**: Every Light slider has an exact value, and the Tone Curve has a 4x4 grid plot plus a coordinate table (`(In %, Out %)` and `(0–255, 0–255)`) with thumb-drag landmarks for Master RGB and every active R, G, B curve.

### Step 5: Set Color, Color Mix, Color Grading, Effects, Detail, and Masks

Fill every remaining panel in left-to-right toolbar order using `references/recipe-output-format.md` section 2. For lighting gaps, give numbered local masks on Premium, and the playbook's Free-tier workaround on Free (or alongside masks).

**Completion criterion**: Color, all 8 Color Mix bands, Color Grading (`0°–360°` Hue, `0–100` Sat), Effects, Detail, Optics, and Masks or Free-tier workarounds (or `Masks: None` when the light already matches) all carry exact numbers, with zero "adjust to taste".

### Step 6: Deliver the verdict and the Pass 2 loop

Pick one label from the **Verdict table**, print it word for word, and render the report in plain language using the layout in `references/recipe-output-format.md` section 3.

**Completion criterion**: The report gives one verdict (named-look mode: no verdict), every section of the layout with exact numbers, and the screenshot-check prompt, with every internal term replaced by its user-facing label.

## Verdict table

| Verdict | When to assign |
| :--- | :--- |
| **`95%–100% Exact Lock`** | RAW/ProRAW (or well-exposed JPEG/HEIC) with lighting compatible with Photo 2; global tools reach 95%+ as measured from the actual file, or a screenshot check confirmed it. |
| **`95%+ Match With Local Masks`** | Global tools reach about 85% to 90%; 1 to 4 local masks close the lighting or separation gap to 95%+. Use only when Step 2 names a specific lighting or separation gap that global sliders cannot close; when both photos share the same light, masks are `None`. |
| **`Screenshot Check Needed for 95%+ Lock`** | The first recipe reaches about 90% to 94%; mixed light, heavy shadow compression, or an unverified base profile makes a screenshot check the way to the last 2% to 6%. Always use this label when slider values come from a preview or a visual estimate instead of the actual file. |
| **`85%–94% Close Approximation (Free-Tier / JPEG Ceiling)`** | Free tier without masks for a strongly directional reference, or a clipped 8-bit JPEG that would band if pushed; give the workaround. |
| **`Lighting or Time-of-Day Mismatch`** | Incompatible capture light (harsh noon vs. blue-hour neon); deliver the closest mood translation and say what light difference remains. |
| **`Missing or Unclear Reference/Source`** | A needed photo is missing, or both are identical or ambiguous; stop and ask before any sliders. |

## Guardrails

1. **No blind presets**: never output a preset before confirming (or, after an opt-out, stating as assumptions) which photo is which, Photo 1's camera and file format, and the Lightroom Mobile tier.
2. **Delta math, not static presets**: compute every slider as the bridge from Photo 1 to Photo 2. A warm golden-hour reference needs `+1,200K` Temp from cool shade but `-400K` from warm tungsten.
3. **Exact numbers only**: every panel states values (`Exposure -0.35 EV`, `Orange Hue -4, Sat -10, Lum +12`), plus a one-line note on what a screenshot check would tweak.
