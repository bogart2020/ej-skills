# Lightroom Mobile Recipe Output Format

Exact panel fields, value ranges, and report layout for Steps 4 to 6 of [`SKILL.md`](../SKILL.md). Read it before writing any recipe or Pass 2 delta table.

## Contents

1. Light panel and Tone Curves (Step 4)
2. Color, Color Mix, Color Grading, Effects, Detail, and Masks (Step 5)
3. Report layout (Step 6)
4. Visual 4x4 Tone Curve template
5. Direct Python grading, exhibition borders, and `.xmp` preset export

## 1. Light panel and Tone Curves (Step 4)

Account for pipeline interaction: `Exposure`, `Highlights`, `Shadows`, `Whites`, and `Blacks` feed into the `Tone Curve`.

- **Light sliders**: **Exposure** (to `0.05 EV` precision, e.g., `-0.35 EV` or `+0.40 EV`), **Contrast**, **Highlights**, **Shadows**, **Whites**, and **Blacks** (each `-100 to +100`).
- **Avoid double-counting**: when the **Point Curve** lifts the black point `(0%, 7%)` and compresses the white ceiling `(100%, 92%)`, use the `Blacks` and `Whites` sliders to set the pre-curve dynamic range so the two tools work together rather than canceling each other out. With a lifted curve black point, keep `Blacks` between `-10` and `0`.
- **Tone Curves in dual format**: Lightroom Mobile displays the Point Curve on a **4x4 grid** with grid lines at **`0%`, `25%`, `50%`, `75%`, and `100%`**. In every recipe, render:
  1. **Visual ASCII/Unicode 4x4 grid plots** for the **Master RGB Curve** (and the **Red**, **Green**, and **Blue** channel curves whenever per-channel curves are used), marking the diagonal neutral baseline (`·` or `╱`) and the plotted curve path and control points (`●`) aligned to the grid lines. Use the template in section 4.
  2. **Anchor point coordinate tables** listing each point left to right with its **Zone Name**, **Grid Position `(Input %, Output %)`**, **8-Bit Value `(0-255, 0-255)`**, and a **plain-language thumb-drag landmark** (where to tap on the grid lines and how far to drag).
  3. **Parametric Curve sliders** (`Shadows`, `Darks`, `Lights`, `Highlights` from `-100 to +100`, plus the 3 region split sliders at `25 / 50 / 75`) whenever they add smooth shoulder/toe control or the user prefers sliders over dragging points.

## 2. Color, Color Mix, Color Grading, Effects, Detail, and Masks (Step 5)

Give the remaining panels in Lightroom Mobile's left-to-right toolbar order:

1. **Color & White Balance**: **Temp** in **Kelvin (`2000K-50000K`)** plus how much warmer/cooler than As-Shot when Photo 1 is **RAW / ProRAW / DNG**, or on the relative **`-100 to +100`** scale when Photo 1 is **JPEG / HEIC**. Then **Tint** (`-150 to +150`), **Vibrance** and **Saturation** (`-100 to +100`). Set Temp/Tint only from neutral grey, white, or black objects; sky and foliage go to Color Mix. When a neutral object reads the same in both photos (each channel within about 3%, or 8 levels out of 255), write `Temp: As Shot` and `Tint: 0` with no Kelvin offset. When the file's As Shot Kelvin cannot be read (chat previews), give Temp as "As Shot plus or minus N K".
2. **Color Mix (HSL, all 8 bands) and Point Color**: an 8-row table for **Red**, **Orange**, **Yellow**, **Green**, **Aqua**, **Blue**, **Purple**, and **Magenta** with **Hue**, **Saturation**, and **Luminance** (`-100 to +100`) plus what each change does to Photo 1 (such as *"Orange: Hue `-3`, Sat `-8`, Lum `+10` -> warms and brightens skin tones to match Photo 2"*). On **Premium**, when a narrow swatch needs surgical tuning (a neon sign or garment without touching skin), add **Point Color** (`Hue Shift`, `Sat Shift`, `Lum Shift`, `Range`).
3. **Color Grading (3-way wheels + Global + Blending & Balance)**: **Hue (`0° to 360°`)**, **Saturation (`0 to 100`)**, and **Luminance (`-100 to +100`)** for **Shadows**, **Midtones**, **Highlights**, and **Global** (each hue follows that zone's measured cast: warm, with red above blue, means `30°` to `60°`; cool means `195°` to `225°`), plus **Blending (`0 to 100`)** and **Balance (`-100 to +100`)**. Remind the user to tap and hold the small **eye or slider icon / expand arrow** on the wheel to type exact `Hue` and `Saturation` numbers instead of guessing on the circle.
4. **Effects**: **Texture**, **Clarity**, **Dehaze**, **Vignette** (`Amount`, `Midpoint`, `Feather`, `Roundness`, `Highlights`), and **Grain** (`Amount`, `Size`, `Roughness`).
5. **Detail & Optics**: **Sharpening** (`Amount`, `Radius`, `Detail`, `Masking`), **Noise Reduction (Luminance)**, **Color Noise Reduction**, **Remove Chromatic Aberration (`ON`)**, and **Enable Lens Corrections (`ON`)**, calibrated to Photo 1's sensor (Sharpening `0-15` on Apple ProRAW; Detail $\le 25$ and Masking $\ge 40$ on Fujifilm X-Trans).
6. **Crop & Geometry (Maestro Composition Gate)**: **Aspect Ratio** (`Original`, `4:5`, `3:2`, or `16:9`), **Straighten / Rotate** (`-X.X°` to `+X.X°` to eliminate any `0.5°-3.0°` unintentional horizon/vertical tilt), **Vertical Upright** (`-25 to +25` for wide-angle keystoning), and **Edge-Patrol Trim** (`2%-8%` inward crop when needed to remove border amputations, utility poles, or bright edge leaks).
7. **Local Masks**: when lighting geometry, subject pop, sky density, or foreground vignette differs, give numbered masks (`Mask 1: Select Subject`, `Mask 2: Select Sky`, `Mask 3: Linear Gradient from bottom`, `Mask 4: Inverted Radial Gradient`) with exact placement and local Light/Color/Effects sliders. Every mask slider, Temp and Tint included, runs `-100 to +100` (never Kelvin), even on RAW files. On **Free** (or alongside Premium masks), add the Free-tier global workaround from the camera playbook's Free-tier table. When lighting, subject separation, sky, and foreground already match, write `Masks: None` and skip the mask cards.

## 3. Report layout (Step 6)

Five sections, plus an optional sixth profile-save prompt:

1. **Match Verdict, Fidelity Estimate & Look Breakdown**:
   - **Verdict**: one label from the verdict table in `SKILL.md`.
   - **Estimated fidelity** after the first recipe (for example, **`96%-98% Match`** with the included masks) and the 3 defining traits of Photo 2's edit (such as *"1. Lifted matte black floor at 7% with rolled-off 93% highlights; 2. Desaturated emerald-shifted greens (`Hue +28, Sat -55`); 3. Cool slate-blue shadow tint (`212°`) paired with warm golden highlights (`44°`)"*).
   - **Your setup summary**: one line confirming Photo 1's camera/format, starting Profile, and Lightroom Mobile tier.
2. **Step-by-step recipe (left-to-right toolbar order)**:
   1. **Profile**: Profile name and Profile Amount (`0-200%`).
   2. **Light**: `Exposure`, `Contrast`, `Highlights`, `Shadows`, `Whites`, `Blacks`.
   3. **Tone Curve**: grid plot(s), coordinate table (`Zone | Grid (In %, Out %) | 8-Bit (0-255) | Where to Drag on Your Phone`), and Parametric sliders with split points.
   4. **Color & 8-band Color Mix**: `Temp`, `Tint`, `Vibrance`, `Saturation`, then the `Red` to `Magenta` table (`Hue`, `Saturation`, `Luminance`, `Visual Effect`).
   5. **Color Grading wheels**: `Shadows`, `Midtones`, `Highlights`, `Global` (`Hue 0°-360°`, `Saturation 0-100`, `Luminance -100 to +100`), plus `Blending` and `Balance`.
   6. **Effects, Detail, Optics & Crop/Geometry**: `Texture`, `Clarity`, `Dehaze`, `Vignette`, `Grain`, `Sharpening`, `Noise Reduction`, `Optics`, and `Crop / Rotate / Upright` (from the Maestro Composition check).
   7. **Local Masks (or Free-tier global equivalent)**: numbered mask cards with placement and exact slider values.
3. **Maestro Composition & Calibration QA Scorecard**: a concise verification table reporting the pass/fix status of:
   - **Composition & Edge Patrol**: horizon/vertical alignment (`±0.3°`), 5% border scan (any edge crop applied), and figure-ground luminance separation ($\Delta L \ge 20\%$).
   - **Colorimetric & Pixel Accuracy**: highlight clipping ($Y \ge 254 \le 0.5\%$), shadow/matte floor integrity, single-channel gamut headroom, CIE LAB skin-tone hue ($h_{ab} \in [32^\circ, 54^\circ]$), `0` histogram comb gaps, and uncontaminated border purity.
   - **Preset (`.xmp`) Calibration & 3-Lighting Stress-Test**: ACR `ProcessVersion="15.4"` schema compliance, portability hygiene (`Exposure2012` omitted, `WhiteBalance="As Shot"`), and pass status across High-Key Daylight, Golden-Hour Skin, and Low-Key Twilight stress tests.
4. **Screenshot check**: a 3-bullet checklist:
   1. Apply the recipe, then take a **screenshot of the edited Photo 1** (ideally with the **Lightroom Mobile histogram** visible, or a clean export).
   2. Send the screenshot back in this chat.
   3. The 2 to 3 sliders most sensitive to Photo 1's exposure (such as `Temp`, `Exposure`, or `Orange Luminance`), so the user knows what the screenshot check will fine-tune.
5. **Save as a reusable preset & Creator Disclaimer**:
   - `Three-dot menu (...) at top right -> Create Preset -> Name it and check all modified panels except Exposure and local Subject/Sky masks if applying across different photos`, noting that `Exposure` and `Temp/Tint` are the 2 sliders to tweak on future photos.
   - **Creator Note & Disclaimer (Mandatory on recipe cards & exports):** Never use clinical, medical, or infomercial buzzwords ("magic pill", "instant one-click fix"). Use authentic photography creator language:
     > **CREATOR NOTE: NOT A ONE-CLICK PRESET**  
     > *Every scene has unique lighting and color temperature. Use these numbers as a clean starting baseline, then fine-tune Exposure & Temp to match your shot, and dial Luminance Noise Reduction for your camera sensor & ISO.*
   - **No Film Simulation or Film Stock Name-Dropping:** Never label, title, or name presets, cards, or exports after actual film simulations or commercial film stocks (e.g., "Classic Neg", "Kodak Gold", "Classic Chrome", "Portra 400") unless the user explicitly requests to include them. Default to descriptive visual character or scene/hardware labels (e.g., "Warm Golden Baseline", "Muted Heritage Tones", "Downtown Street Grade").
6. **Save your camera & editor profile (when applicable)**: if the session established the user's camera/phone, default RAW/JPEG format, or Lightroom Mobile tier, ask in one line whether to save it in the photo profile.

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

## 5. Direct Python grading, exhibition borders, and `.xmp` preset export

When running in a local code environment and the user asks to see the graded photos, add clean borders, or receive a ready-to-import Lightroom preset file:

### A. Orientation-safe Python grading & border pipeline

1. **Always transpose EXIF orientation first**: open with `ImageOps.exif_transpose(Image.open(path)).convert('RGB')` so portrait smartphone/camera RAWs (`Orientation=6`) are never rendered sideways.
2. **Apply anti-clinical de-sharpening & optical halation (when emulating X100VI / soft film)**:
   - Blend a low-pass softened copy (`GaussianBlur(radius=0.7)`, `alpha=0.35`) to strip baked ProRAW/digital edge halos.
   - Extract highlights (`L > 0.70`), blur with `GaussianBlur(radius=4.5)`, and add `15%-20%` bloom back onto the image.
3. **Apply Color Chrome compression, per-channel RGB Tone Curves, and multi-scale grain**:
   - Attenuate high-saturation pixels by `1 - clip(S * 0.22, 0, 0.22)` and deep blue skies by `0.86-0.88`.
   - Map `R`, `G`, `B` arrays through `np.interp` using the recipe's normalized curve points.
   - Add dual-octave grain (`65%` fine `σ=0.010` + `35%` 2x bilinear-upscaled coarse `σ=0.016`) weighted by a midtone luminance mask `clip(1.1 - (L - 0.25)^2 * 1.8, 0.1, 1.0)`.
4. **Add clean white exhibition borders**:
   - Pad with `ImageOps.expand(img, border=int(min(w, h) * 0.038), fill=(255, 255, 255))` (`3.5%-4.5%` of the shorter edge) and save at `quality=95-96`.

### C. Lightroom Mobile UI Slider Simulation Card (`1080 x 1350 px`)

When exporting a recipe as a social carousel slide or standalone utility card (Slide N), render a dedicated **Lightroom Mobile UI Slider Card**:
1. **Dark UI Canvas:** `1080 x 1350 px` canvas in `#16171A` (charcoal dark mode).
2. **Header Area:** Small `ADOBE LIGHTROOM MOBILE` badge (`20pt bold`, `#2680EB`), descriptive mood/hardware title (e.g. `WARM GOLDEN STREET BASELINE`, 36pt bold `#FFFFFF`, strictly omitting commercial stock names per `MEM-10`), and in-camera baseline pill (`#222429` container, 19pt bold `#B0B5C0`).
3. **Grouped Edit Tabs:** Clean panel pills for `LIGHT`, `COLOR`, and `EFFECTS & DETAIL` (`#23252B` rounded tabs with section accent colors).
4. **Visual Slider Rows:**
   - Parameter label on left (`24pt bold`, `#FFFFFF`, flush left).
   - Horizontal slider track: `#2E3038`, width 6px, from X=340 to X=860. Bipolar sliders include a subtle center zero notch (`#484B55`).
   - Active slider fill: signature Lightroom electric cyan/blue (`#2680EB`, or warm amber `#E5943B` for Temp, purple `#9B51E0` for Tint) extending from 0 to current value.
   - Circular slider knob / thumb: `radius=11px` (`#FFFFFF` circle with dark outline).
   - Exact numerical readout on right: `24pt bold` (`#FFFFFF` or matching active fill), flush right at X=1020.
5. **Mobile Readability Rule:** Because smartphone screens compress 1080px to ~68mm width, all parameter labels and values must never drop below `24pt` (optimal `24pt` to `28pt`), guaranteeing instant mobile legibility without zooming.
6. **Amber Creator Note Banner (`MEM-07`):** Rounded container (`#241B0E` fill, `#D48806` outline) displaying:
   `CREATOR NOTE: NOT A ONE-CLICK PRESET`
   `Every scene has unique lighting and color temperature. Use these numbers as a clean starting baseline, then fine-tune Exposure & Temp to match your shot, and dial Luminance NR for your camera ISO.`
7. **Footer CTA:** Episodic series subtitle and social follow handle (`20pt`, `#8E8E93`).

### B. Calibrated, portable Adobe Lightroom `.xmp` preset schema (`ProcessVersion="15.4"`)

Write a `.xmp` file alongside the graded exports using the exact slider values from Steps 4 and 5, adhering to the **Maestro Calibration Preset Portability Rules** (`references/maestro-critique-and-qa-gate.md` Pillar 3):
- Omit `crs:Exposure2012` and crop/geometry tags so the preset adapts cleanly across any photo.
- Keep `crs:WhiteBalance="As Shot"` with `crs:IncrementalTemperature` / `crs:IncrementalTint` (never write small integers like `crs:Temperature="+5"` into the Kelvin tag).
- Include `<crs:Name><rdf:Alt>`, `<crs:Group><rdf:Alt>`, 32-hex `crs:UUID`, `crs:ProcessVersion="15.4"`, `crs:HasSettings="True"`, all 8 HSL bands, 3-Way Color Grading (`SplitToning*` + `ColorGrade*`), Camera Calibration, and all 4 `ToneCurvePV2012*` sequences (`PV2012`, `Red`, `Green`, `Blue`):

```xml
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 7.0-c000 1.000000, 0000/00/00-00:00:00">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"
    crs:PresetType="Normal"
    crs:Cluster=""
    crs:UUID="A100F5004C8F494CE49E570000000001"
    crs:SupportsAmount="True"
    crs:SupportsColor="True"
    crs:SupportsMonochrome="True"
    crs:SupportsHighDynamicRange="True"
    crs:SupportsNormalDynamicRange="True"
    crs:SupportsSceneReferred="True"
    crs:SupportsOutputReferred="True"
    crs:CameraModelRestriction=""
    crs:Copyright=""
    crs:ContactInfo=""
    crs:Version="15.4"
    crs:ProcessVersion="15.4"
    crs:WhiteBalance="As Shot"
    crs:IncrementalTemperature="+5"
    crs:IncrementalTint="+2"
    crs:Contrast2012="-8"
    crs:Highlights2012="-30"
    crs:Shadows2012="+22"
    crs:Whites2012="+8"
    crs:Blacks2012="-8"
    crs:Texture="-4"
    crs:Clarity2012="-16"
    crs:Dehaze="+4"
    crs:Vibrance="+4"
    crs:Saturation="-5"
    crs:ParametricShadows="0"
    crs:ParametricDarks="0"
    crs:ParametricLights="0"
    crs:ParametricHighlights="0"
    crs:ParametricShadowSplit="25"
    crs:ParametricMidtoneSplit="50"
    crs:ParametricHighlightSplit="75"
    crs:Sharpness="12"
    crs:SharpenRadius="+0.8"
    crs:SharpenDetail="15"
    crs:SharpenEdgeMasking="75"
    crs:LuminanceSmoothing="10"
    crs:ColorNoiseReduction="25"
    crs:HueAdjustmentRed="+4"
    crs:HueAdjustmentOrange="-2"
    crs:HueAdjustmentYellow="-14"
    crs:HueAdjustmentGreen="+26"
    crs:HueAdjustmentAqua="-8"
    crs:HueAdjustmentBlue="-12"
    crs:HueAdjustmentPurple="0"
    crs:HueAdjustmentMagenta="0"
    crs:SaturationAdjustmentRed="+6"
    crs:SaturationAdjustmentOrange="+6"
    crs:SaturationAdjustmentYellow="-8"
    crs:SaturationAdjustmentGreen="-26"
    crs:SaturationAdjustmentAqua="-12"
    crs:SaturationAdjustmentBlue="-16"
    crs:SaturationAdjustmentPurple="-10"
    crs:SaturationAdjustmentMagenta="-5"
    crs:LuminanceAdjustmentRed="-12"
    crs:LuminanceAdjustmentOrange="-6"
    crs:LuminanceAdjustmentYellow="-4"
    crs:LuminanceAdjustmentGreen="-4"
    crs:LuminanceAdjustmentAqua="0"
    crs:LuminanceAdjustmentBlue="-22"
    crs:LuminanceAdjustmentPurple="0"
    crs:LuminanceAdjustmentMagenta="0"
    crs:SplitToningShadowHue="215"
    crs:SplitToningShadowSaturation="8"
    crs:ColorGradeShadowLum="0"
    crs:SplitToningHighlightHue="46"
    crs:SplitToningHighlightSaturation="14"
    crs:ColorGradeHighlightLum="0"
    crs:ColorGradeMidtoneHue="38"
    crs:ColorGradeMidtoneSat="4"
    crs:ColorGradeMidtoneLum="0"
    crs:ColorGradeGlobalHue="0"
    crs:ColorGradeGlobalSat="0"
    crs:ColorGradeGlobalLum="0"
    crs:ColorGradeBlending="50"
    crs:SplitToningBalance="0"
    crs:PostCropVignetteAmount="-12"
    crs:PostCropVignetteMidpoint="45"
    crs:PostCropVignetteFeather="75"
    crs:PostCropVignetteRoundness="0"
    crs:PostCropVignetteStyle="1"
    crs:PostCropVignetteHighlightContrast="25"
    crs:GrainAmount="38"
    crs:GrainSize="45"
    crs:GrainFrequency="60"
    crs:ShadowTint="0"
    crs:RedHue="+4"
    crs:RedSaturation="+4"
    crs:GreenHue="+12"
    crs:GreenSaturation="-8"
    crs:BlueHue="-12"
    crs:BlueSaturation="+12"
    crs:ToneCurveName2012="Custom"
    crs:HasSettings="True">
   <crs:Name>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">Fuji X100VI Soft Portra (EJ Afterglow)</rdf:li>
    </rdf:Alt>
   </crs:Name>
   <crs:Group>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">EJ Afterglow Film Lab</rdf:li>
    </rdf:Alt>
   </crs:Group>
   <crs:ToneCurvePV2012>
    <rdf:Seq>
     <rdf:li>0, 14</rdf:li>
     <rdf:li>58, 54</rdf:li>
     <rdf:li>128, 128</rdf:li>
     <rdf:li>198, 202</rdf:li>
     <rdf:li>255, 240</rdf:li>
    </rdf:Seq>
   </crs:ToneCurvePV2012>
   <crs:ToneCurvePV2012Red>
    <rdf:Seq>
     <rdf:li>0, 0</rdf:li>
     <rdf:li>255, 255</rdf:li>
    </rdf:Seq>
   </crs:ToneCurvePV2012Red>
   <crs:ToneCurvePV2012Green>
    <rdf:Seq>
     <rdf:li>0, 0</rdf:li>
     <rdf:li>255, 255</rdf:li>
    </rdf:Seq>
   </crs:ToneCurvePV2012Green>
   <crs:ToneCurvePV2012Blue>
    <rdf:Seq>
     <rdf:li>0, 0</rdf:li>
     <rdf:li>128, 124</rdf:li>
     <rdf:li>255, 246</rdf:li>
    </rdf:Seq>
   </crs:ToneCurvePV2012Blue>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
```
