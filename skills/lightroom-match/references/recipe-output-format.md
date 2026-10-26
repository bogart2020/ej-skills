# Lightroom Mobile Recipe Output Format

Exact panel fields, value ranges, and report layout for Steps 4 to 6 of [`SKILL.md`](../SKILL.md). Read it before writing any recipe or Pass 2 delta table.

## Contents

1. Light panel and Tone Curves (Step 4)
2. Color, Color Mix, Color Grading, Effects, Detail, and Masks (Step 5)
3. Report layout (Step 6)
4. Visual 4x4 Tone Curve template

## 1. Light panel and Tone Curves (Step 4)

Account for pipeline interaction: `Exposure`, `Highlights`, `Shadows`, `Whites`, and `Blacks` feed into the `Tone Curve`.

- **Light sliders**: **Exposure** (to `0.05 EV` precision, e.g., `-0.35 EV` or `+0.40 EV`), **Contrast**, **Highlights**, **Shadows**, **Whites**, and **Blacks** (each `-100 to +100`).
- **Avoid double-counting**: when the **Point Curve** lifts the black point `(0%, 7%)` and compresses the white ceiling `(100%, 92%)`, use the `Blacks` and `Whites` sliders to set the pre-curve dynamic range so the two tools work together rather than canceling each other out. With a lifted curve black point, keep `Blacks` between `-10` and `0`.
- **Tone Curves in dual format**: Lightroom Mobile displays the Point Curve on a **4x4 grid** with grid lines at **`0%`, `25%`, `50%`, `75%`, and `100%`**. In every recipe, render:
  1. **Visual ASCII/Unicode 4x4 grid plots** for the **Master RGB Curve** (and the **Red**, **Green**, and **Blue** channel curves whenever per-channel curves are used), marking the diagonal neutral baseline (`·` or `╱`) and the plotted curve path and control points (`●`) aligned to the grid lines. Use the template in section 4.
  2. **Anchor point coordinate tables** listing each point left to right with its **Zone Name**, **Grid Position `(Input %, Output %)`**, **8-Bit Value `(0–255, 0–255)`**, and a **plain-language thumb-drag landmark** (where to tap on the grid lines and how far to drag).
  3. **Parametric Curve sliders** (`Shadows`, `Darks`, `Lights`, `Highlights` from `-100 to +100`, plus the 3 region split sliders at `25 / 50 / 75`) whenever they add smooth shoulder/toe control or the user prefers sliders over dragging points.

## 2. Color, Color Mix, Color Grading, Effects, Detail, and Masks (Step 5)

Give the remaining panels in Lightroom Mobile's left-to-right toolbar order:

1. **Color & White Balance**: **Temp** in **Kelvin (`2000K–50000K`)** plus how much warmer/cooler than As-Shot when Photo 1 is **RAW / ProRAW / DNG**, or on the relative **`-100 to +100`** scale when Photo 1 is **JPEG / HEIC**. Then **Tint** (`-150 to +150`), **Vibrance** and **Saturation** (`-100 to +100`). Set Temp/Tint only from neutral grey, white, or black objects; sky and foliage go to Color Mix. When a neutral object reads the same in both photos (each channel within about 3%, or 8 levels out of 255), write `Temp: As Shot` and `Tint: 0` with no Kelvin offset. When the file's As Shot Kelvin cannot be read (chat previews), give Temp as "As Shot plus or minus N K".
2. **Color Mix (HSL, all 8 bands) and Point Color**: an 8-row table for **Red**, **Orange**, **Yellow**, **Green**, **Aqua**, **Blue**, **Purple**, and **Magenta** with **Hue**, **Saturation**, and **Luminance** (`-100 to +100`) plus what each change does to Photo 1 (such as *"Orange: Hue `-3`, Sat `-8`, Lum `+10` -> warms and brightens skin tones to match Photo 2"*). On **Premium**, when a narrow swatch needs surgical tuning (a neon sign or garment without touching skin), add **Point Color** (`Hue Shift`, `Sat Shift`, `Lum Shift`, `Range`).
3. **Color Grading (3-way wheels + Global + Blending & Balance)**: **Hue (`0° to 360°`)**, **Saturation (`0 to 100`)**, and **Luminance (`-100 to +100`)** for **Shadows**, **Midtones**, **Highlights**, and **Global** (each hue follows that zone's measured cast: warm, with red above blue, means `30°` to `60°`; cool means `195°` to `225°`), plus **Blending (`0 to 100`)** and **Balance (`-100 to +100`)**. Remind the user to tap and hold the small **eye or slider icon / expand arrow** on the wheel to type exact `Hue` and `Saturation` numbers instead of guessing on the circle.
4. **Effects**: **Texture**, **Clarity**, **Dehaze**, **Vignette** (`Amount`, `Midpoint`, `Feather`, `Roundness`, `Highlights`), and **Grain** (`Amount`, `Size`, `Roughness`).
5. **Detail & Optics**: **Sharpening** (`Amount`, `Radius`, `Detail`, `Masking`), **Noise Reduction (Luminance)**, **Color Noise Reduction**, **Remove Chromatic Aberration (`ON`)**, and **Enable Lens Corrections (`ON`)**, calibrated to Photo 1's sensor (Sharpening `0–15` on Apple ProRAW; Detail $\le 25$ and Masking $\ge 40$ on Fujifilm X-Trans).
6. **Local Masks**: when lighting geometry, subject pop, sky density, or foreground vignette differs, give numbered masks (`Mask 1: Select Subject`, `Mask 2: Select Sky`, `Mask 3: Linear Gradient from bottom`, `Mask 4: Inverted Radial Gradient`) with exact placement and local Light/Color/Effects sliders. Every mask slider, Temp and Tint included, runs `-100 to +100` (never Kelvin), even on RAW files. On **Free** (or alongside Premium masks), add the Free-tier global workaround from the camera playbook's Free-tier table. When lighting, subject separation, sky, and foreground already match, write `Masks: None` and skip the mask cards.

## 3. Report layout (Step 6)

Five sections, plus an optional sixth profile-save prompt:

1. **Match Verdict, Fidelity Estimate & Look Breakdown**:
   - **Verdict**: one label from the verdict table in `SKILL.md`.
   - **Estimated fidelity** after the first recipe (for example, **`96%–98% Match`** with the included masks) and the 3 defining traits of Photo 2's edit (such as *"1. Lifted matte black floor at 7% with rolled-off 93% highlights; 2. Desaturated emerald-shifted greens (`Hue +28, Sat -55`); 3. Cool slate-blue shadow tint (`212°`) paired with warm golden highlights (`44°`)"*).
   - **Your setup summary**: one line confirming Photo 1's camera/format, starting Profile, and Lightroom Mobile tier.
2. **Step-by-step recipe (left-to-right toolbar order)**:
   1. **Profile**: Profile name and Profile Amount (`0–200%`).
   2. **Light**: `Exposure`, `Contrast`, `Highlights`, `Shadows`, `Whites`, `Blacks`.
   3. **Tone Curve**: grid plot(s), coordinate table (`Zone | Grid (In %, Out %) | 8-Bit (0–255) | Where to Drag on Your Phone`), and Parametric sliders with split points.
   4. **Color & 8-band Color Mix**: `Temp`, `Tint`, `Vibrance`, `Saturation`, then the `Red` to `Magenta` table (`Hue`, `Saturation`, `Luminance`, `Visual Effect`).
   5. **Color Grading wheels**: `Shadows`, `Midtones`, `Highlights`, `Global` (`Hue 0°–360°`, `Saturation 0–100`, `Luminance -100 to +100`), plus `Blending` and `Balance`.
   6. **Effects, Detail & Optics**: `Texture`, `Clarity`, `Dehaze`, `Vignette`, `Grain`, `Sharpening`, `Noise Reduction`, `Optics`.
   7. **Local Masks (or Free-tier global equivalent)**: numbered mask cards with placement and exact slider values.
3. **Screenshot check**: a 3-bullet checklist:
   1. Apply the recipe, then take a **screenshot of the edited Photo 1** (ideally with the **Lightroom Mobile histogram** visible, or a clean export).
   2. Send the screenshot back in this chat.
   3. The 2 to 3 sliders most sensitive to Photo 1's exposure (such as `Temp`, `Exposure`, or `Orange Luminance`), so the user knows what the screenshot check will fine-tune.
4. **Save as a reusable preset**: `Three-dot menu (...) at top right -> Create Preset -> Name it and check all modified panels except Exposure and local Subject/Sky masks if applying across different photos`, and note that `Exposure` and `Temp/Tint` are the 2 sliders to tweak on future photos.
5. **Save your camera & editor profile (when applicable)**: if the session established the user's camera/phone, default RAW/JPEG format, or Lightroom Mobile tier, ask in one line whether to save it in the photo profile.

**Pass 2 mode** replaces sections 2 to 4 with a **Pass 2 Fine-Tuning Delta Table** (`Slider | Current Value -> New Value | Why`).

## 4. Visual 4x4 Tone Curve template

Match Lightroom Mobile's `0%, 25%, 50%, 75%, 100%` grid boxes so the user can match the curve shape on their phone, with the coordinate table below it for exact placement:

```text
Master RGB Point Curve (LR Mobile 4x4 Grid)
Output %
100% +-------+-------+-------+-------+
     |       |       |       |   .   ●  <- White Point rolled off (100%, 93%) for soft, creamy highlights
 75% +-------+-------+-------●-------+  <- Highlights (75%, 76%)
     |       |       |   .   |       |
 50% +-------+-------●-------+-------+  <- Midtones (50%, 50%)
     |       |   .   |       |       |
 25% +-------●-------+-------+-------+  <- Shadows dipped (25%, 20%) for rich shadow contrast
     ●   .   |       |       |       |  <- Black Point lifted (0%, 7%) for matte film fade
  0% +-------+-------+-------+-------+
     0%     25%     50%     75%    100%
                  Input %
(● = Curve control point to place | . = Default diagonal line)
```

| Point # | Zone | Grid `(Input %, Output %)` | 8-Bit `(In, Out)` | Where to Drag on Your Phone in LR Mobile |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Black Point** | `(0%, 7%)` | `(0, 18)` | Tap the bottom-left corner dot `(0%, 0%)` and drag straight up about one-quarter of the first grid box. |
| **2** | **Shadows** | `(25%, 20%)` | `(64, 51)` | Tap on the first vertical grid line (`25%`) and drag slightly below the first horizontal grid line (`25%`). |
| **3** | **Midtones** | `(50%, 50%)` | `(128, 128)` | Tap the exact center intersection `(50%, 50%)` to anchor skin tones and middle gray. |
| **4** | **Highlights** | `(75%, 76%)` | `(191, 194)` | Tap the third vertical/horizontal intersection `(75%, 75%)` and nudge up slightly. |
| **5** | **White Point** | `(100%, 93%)` | `(255, 237)` | Tap the top-right corner dot `(100%, 100%)` and drag straight down about one-quarter of the top box. |
