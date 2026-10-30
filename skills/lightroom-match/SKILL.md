---
name: lightroom-match
description: Replicate a reference photo's color grade, tone curve, and look onto a source or RAW photo in Adobe Lightroom Mobile at 95% to 100% fidelity, cull and grade batches of RAW/DNG photos (with optional borders and .xmp presets), emulate camera sensors and film recipes (such as Fujifilm X100VI), reverse-engineer any photo's edit into exact Lightroom Mobile sliders, curves, and masks, build a preset from a folder or web page of reference photos, or fine-tune an in-progress edit from a screenshot.
license: MIT
---

# Lightroom Match

Copy the look of **Photo 2 (reference)**, or a target camera or film recipe, onto **Photo 1 (source or RAW batch)** in **Lightroom Mobile** at **95% to 100% fidelity**, with exact numbers for every panel.

## Environment adaptation

- **Chat** (Claude Desktop, mobile, web): check photos, history, and memory for camera context. With a code sandbox, measure the photos; otherwise audit them visually. To save a camera baseline, output a snippet following [`references/photo-profile-template.md`](references/photo-profile-template.md).
- **Code and CLI**: read `.agents/photo-profile.md` or `~/.agents/photo-profile.md` before asking questions. When files are local, use Python (`PIL` / `numpy`) or macOS `sips` for EXIF, luminance percentiles, and per-zone casts before computing deltas.

## Plain-language output

The bolded terms are your working vocabulary. Everything the user sees is everyday language a phone photo editor understands:

- Print the **user-facing label** from the table below wherever an internal term would appear.
- Show adjustments as labeled numbers and drag directions ("drag the bottom-left Black Point up to `(0%, 6%)`"), never color-science equations.
- Keep step, gate, and pass names internal: describe the work by what it does.
- When an app term is unavoidable (**Point Curve**, **Color Mix**, **Luminance Mask**), say where to tap it the first time it appears.

| Internal term | User-facing label |
| :--- | :--- |
| Recipe-flipping variables | Your camera, file type, and Lightroom Mobile setup |
| Photo 1 / Photo 2 | Your photo to edit (Photo 1) / The look you want to copy (Photo 2) |
| Sensor baseline | How your camera or phone naturally renders colors |
| Cross-sensor emulation | Matching how another camera renders color, grain, and glow |
| Batch culling | Picking your strongest shots and dropping weak ones |
| 5-zone / 8-band decomposition | How dark each tone range is / Color shifts in Color Mix |
| QA gate | Final check of crop, horizon, edges, colors, and the preset file |
| Pass 2 Delta Calibration | Screenshot check to dial in the final 1% to 5% |

## Interview rounds

1. Ask at least one round on every run. Skip only when the user says "just answer", "no questions", or equivalent, or in a direct batch run where EXIF and the named look settle the prerequisites; then state your file-format, camera, and tier assumptions in one line at the top. When the tier is unknown, assume Free and say so.
2. The **frontier** is every open question whose prerequisites are settled. Ask the whole frontier in one round, number each question, give your recommended answer, and word it so "yes" accepts the recommendation. Then stop and wait.
3. Check the images, EXIF, photo profile, and history first; never ask for a fact you can see or the user already stated. When context only suggests an answer, turn it into a quick confirmation.
4. Recompute the frontier after each answer. A question that depends on another open question belongs to a later round.
5. "Yes", "idk", or a skipped question accepts your recommendation. When the user says "you decide", adopt your recommendations as listed assumptions and start.
6. When the frontier is empty, summarize the setup in 2 to 4 bullets and ask "Ready for me to generate your Lightroom Mobile recipe?" Start once the user confirms.

Copy this format exactly, with the ❓ and ➡️ markers and a `---` line between questions:

```
❓ **Q1** - **<short title>**: <question in everyday words, with options when useful>

➡️ <your recommended answer>

---

❓ **Q2** - **<short title>**: <question in everyday words, with options when useful>

➡️ <your recommended answer>
```

## Reference pointers

- **Before Steps 1 and 2**, read [`references/camera-raw-and-style-playbooks.md`](references/camera-raw-and-style-playbooks.md) for camera baselines, batch culling (Drive downloads, unreadable DNGs), cross-sensor emulation, look archetypes, and Free-tier workarounds.
- **Before Steps 4 to 6, in Pass 2 mode, or when exporting**, read [`references/recipe-output-format.md`](references/recipe-output-format.md) for panel fields, the report layout, the Tone Curve template, and the grading, border, and `.xmp` pipeline.
- **Before Step 6**, read [`references/maestro-critique-and-qa-gate.md`](references/maestro-critique-and-qa-gate.md) for the 3-pillar QA gate (composition, pixel bounds, `.xmp` validation).
- **When saving a profile** in Step 6, read [`references/photo-profile-template.md`](references/photo-profile-template.md).

## Modes

- **No photos and no named look**: ask which they want: copy a look, grade a RAW batch, make a preset from one photo, or build a named look.
- **Full two-photo replication** (Photo 1 + Photo 2): run all 6 steps and deliver the full recipe plus the Pass 2 prompt.
- **Batch RAW culling + grading** (several RAW/DNG files or a Drive folder, plus a reference or named look): cull to the top 4 to 6 frames, deliver the recipe, and (when asked) export bordered graded JPEGs plus a `.xmp` preset.
- **Cross-sensor emulation** (mimic a camera or lens such as the Fujifilm X100VI, or *"not too sharp"*): run all 6 steps with the Step 2 emulation.
- **Pass 2 screenshot calibration** (user sends their edited Photo 1): compare it (and any histogram) against Photo 2, isolate the remaining 1% to 10% gap, and output a **Pass 2 Fine-Tuning Delta Table** (`Slider | Current Value -> New Value | Why`). Use it only when Photo 1's current values are known; otherwise build a full recipe from `Reset`.
- **Single-reference reverse-engineering** (only Photo 2): ask which camera and file format the preset is for, then decompose Photo 2's edit into a reusable preset.
- **Named look, no photo** (a film stock, a style like teal and orange, or a creator's preset): use the closest playbook archetype as Photo 2; settle only camera, file format, and tier; label the result a starting preset, with no verdict or fidelity percentage. For a creator's preset, say you haven't seen it and ask for 1 to 2 photos edited with it or a page of their work.
- **Reference-set match** (a folder or web page of photos in the target look, plus Photo 1 files and code): run the loop in [`references/match-engine.md`](references/match-engine.md).

## Replication sequence

Run these six steps in order.

### Step 1: Read the camera, cull batches, and settle setup variables

1. **EXIF first**: from readable files, extract `make`, `model`, the true file type (RAW or 8-bit JPEG/HEIC, whatever the extension says), and orientation before proposing any sliders.
2. **Batch mode**: view every oriented preview and apply the playbook's **Culling Knockout Criteria**.
3. **Settle the 5 recipe-flipping variables** (from EXIF, profile, or interview):
   - **Photo mapping**: which image is Photo 1 and Photo 2 (or target look), and whether Photo 1 starts from `Reset`.
   - **Camera and file format**: exact body or phone, and camera RAW, phone RAW (ProRAW, Expert RAW), or 8-bit JPEG / HEIC.
   - **Sharpness feel**: clean digital or soft analog (*"not too sharp"*, halation, grain).
   - **Tier**: **Premium** (Masking and Point Color) or **Free** (global sliders, Tone Curve, Color Mix, Color Grading).
   - **Screen check**: True Tone, Night Shift, or Eye Comfort Shield off while editing.
4. Run **Interview rounds** on any variable still unsettled.

**Completion criterion**: Camera metadata is verified, every dropped batch frame has a stated reason, and all 5 variables are confirmed or stated as assumptions.

### Step 2: Neutralize the source baseline and map lighting

1. **Neutralize Photo 1's processing**: pick its starting Profile and pre-offsets from playbook section 1 (for example, **ProRAW Profile Amount `30%-55%`** and **Sharpening `0-15`**).
2. **Target sensor emulation**: when mimicking a camera or a *"not too sharp"* look, apply the playbook's 4-pillar cross-sensor translation.
3. **Separate grade from capture physics**: compare light direction, clipping, palette, and depth of field, and decide whether global sliders reach 95% or masks are needed.

**Completion criterion**: Photo 1's Profile, offsets, and target sharpness are locked, and every lighting difference maps to a mask or Free-tier workaround.

### Step 3: Measure the 5 tonal zones and 8 color bands

1. **Tonal zones**: **Black Point** (`0%-10%`), **Shadows** (`10%-30%`), **Midtones & Skin** (`30%-70%`; skin `55%-68%` radiant, `42%-54%` moody), **Highlights** (`70%-90%`), **White Point** (`90%-100%`).
2. **Color**: find each Color Mix band's hue, saturation, and luminance shift. Judge Temp, Tint, and grading casts only from neutral objects (white, grey, black), never from sky or foliage.

**Completion criterion**: All 5 zones, all 8 bands, and the shadow/midtone/highlight casts are stated as deltas from Photo 1's neutralized baseline.

### Step 4: Build the Light panel and Tone Curves

Translate the tonal deltas into exact **Light** sliders and **Tone Curves** using `references/recipe-output-format.md` section 1. With a lifted curve black point, keep Blacks between `-10` and `0`.

**Completion criterion**: Every Light slider has an exact value, and the Tone Curve has a 4x4 grid plot plus a coordinate table with thumb-drag landmarks for Master RGB and every active R, G, B curve.

### Step 5: Set Color, Color Mix, Color Grading, Effects, Detail, and Masks

Fill every remaining panel in toolbar order using `references/recipe-output-format.md` section 2, with **Effects** and **Detail** matched to Photo 1's sensor and the requested sharpness. For lighting gaps, give numbered masks on Premium and the Free-tier workaround on Free.

**Completion criterion**: Color, all 8 Color Mix bands, Color Grading, Effects, Detail, Optics, and Masks or workarounds (or `Masks: None`) all carry exact numbers, with zero "adjust to taste".

### Step 6: Run the QA gate, then deliver

1. **Pillar 1, composition**: run the reference's edge patrol, horizon and vertical check, and figure-ground test. Build exhibition borders only when the user asks.
2. **Pillar 2, pixels**: check every graded image against the reference's 6 pixel bounds. If any check fails, fix the slider or render math and re-check.
3. **Pillar 3, preset file**: validate every `.xmp` against the reference's schema and portability rules, then stress-test it on the 3 lighting scenarios.
4. **Deliver**: pick one label from the **Verdict table**, print it word for word, and render the report (with the QA scorecard) using `references/recipe-output-format.md` section 3, including the `CREATOR NOTE: NOT A ONE-CLICK PRESET` banner.

**Completion criterion**: Every output photo passes the composition check, every graded image passes all 6 pixel bounds, every `.xmp` passes validation and all 3 stress tests, and the plain-language report ends with the screenshot-check prompt.

## Verdict table

| Verdict | When to assign |
| :--- | :--- |
| **`95%-100% Exact Lock`** | RAW/ProRAW (or well-exposed JPEG/HEIC) with light compatible with Photo 2; global tools reach 95%+ as measured from the actual file, or a screenshot check confirmed it. |
| **`95%+ Match With Local Masks`** | Global tools reach about 85% to 90%, and 1 to 4 masks close a lighting gap that Step 2 named. When both photos share the same light, masks are `None`. |
| **`Screenshot Check Needed for 95%+ Lock`** | The first recipe reaches about 90% to 94% (mixed light, heavy shadow compression, or an unverified profile). Always use this label when values come from a preview or visual estimate instead of the actual file. |
| **`85%-94% Close Approximation (Free-Tier / JPEG Ceiling)`** | Free tier without masks for strongly directional light, or a clipped 8-bit JPEG that would band; give the workaround. |
| **`Lighting or Time-of-Day Mismatch`** | Incompatible light (harsh noon vs. blue-hour neon); deliver the closest mood and name the remaining gap. |
| **`Missing or Unclear Reference/Source`** | A needed photo is missing, or both are identical or ambiguous; stop and ask before any sliders. |

## Guardrails

1. **Delta math, not static presets**: compute every slider as the bridge from Photo 1's neutralized baseline to the target look.
2. **Honor softness requests**: for an analog or *"not too sharp"* look, set `Sharpening` `0-15`, `Masking` `70-80`, and negative `Clarity`/`Texture`; never leave default sharpening (`40`) on.
3. **Exact numbers only**: every panel states values (`Exposure -0.35 EV`), plus a one-line note on what a screenshot check would tweak.
4. **Starting point, not a fix**: every recipe card and export carries `CREATOR NOTE: NOT A ONE-CLICK PRESET`: the values are a baseline that needs Exposure and White Balance matched to the light.
5. **Descriptive names on outputs**: title recipes, cards, and presets descriptively ("Warm Nostalgic Baseline"), never after a person; film stock names ("Portra 400") only on request.
