# Maestro Critique & Calibration QA Gate: Primary-Source Research & Reference Specification

Primary-source specification for Step 6 of [`SKILL.md`](../SKILL.md): the mandatory pre-ship **Maestro Critique & Calibration QA Gate** covering (1) curatorial composition and crop/geometry critique, (2) colorimetric pixel and skin-tone QA, and (3) Adobe Camera Raw `.xmp` preset schema validation and 3-lighting stress-testing.

## Citations & Primary Sources

1. **Adobe XMP & Camera Raw Settings (`xmlns:crs`)**:
   - *Adobe XMP Specification Part 2: Additional Properties: Camera Raw Settings (`http://ns.adobe.com/camera-raw-settings/1.0/`)*, Adobe Inc.
   - *Adobe Camera Raw & Lightroom Classic Process Version 5 (`ProcessVersion="11.0"` / `"15.4"`) `.xmp` Preset Schema*.
   - *ExifTool `XMP-crs` Tag Table*, Phil Harvey (`https://exiftool.org/TagNames/XMP.html#crs`).
2. **Colorimetry, Skin-Tone Vectorscope & Spatial Image Quality**:
   - *IEC 61966-2-1:1999 (sRGB) & ITU-R BT.709 Relative Luminance ($Y = 0.2126 R + 0.7152 G + 0.0722 B$)*.
   - *CIE 1976 ($L^*a^*b^*$) Uniform Color Space & CIEDE2000 ($\Delta E_{00}$)*, Commission Internationale de l'Éclairage.
   - *SMPTE Vectorscope I-Line Skin-Tone Engineering Guideline ($123^\circ$ YIQ phase / CIE LAB hue angle $h_{ab} \in [32^\circ, 54^\circ]$)*.
   - *ISO 12233:2023 Photography: Electronic still picture imaging: Resolution and spatial frequency responses (Oversharpening halo / edge overshoot modulation)*.
3. **Master Curatorial & Contact-Sheet Critique Standards**:
   - *Magnum Contact Sheets*, ed. Kristen Lubben (Thames & Hudson): perimeter edge discipline, stride separation, and multi-plane hierarchy.
   - *Alex Webb & Rebecca Norris Webb, On Street Photography and the Poetic Image* (Aperture): figure-ground separation in high-contrast shadow, multi-plane layering without subject collisions.
   - *Henri Cartier-Bresson, The Mind's Eye* (Aperture): geometric rigor, vertical/horizon alignment, and decisive stride geometry.
   - *Saul Leiter, Early Color* (Steidl) & *Fan Ho, Hong Kong Yesterday* (Modernbook): foreground framing proportions (`20%-45%`) and luminance-guided eye flow.

---

## Pillar 1: Maestro Compositional & Geometric Critique (Every Photo Edit)

Before finalizing any single-photo edit or batch cull, run this 4-point visual audit and apply (or prescribe) exact **Crop & Geometry** corrections:

| Audit Dimension | What to Inspect | Quantitative / Visual Pass Criterion | Action When Triggered |
| :--- | :--- | :--- | :--- |
| **1. Edge Patrol (`5%` Perimeter Scan) & Coordinate-Grid Pre-Crop Audit** | Before cropping to `4:5` (vertical) or `5:4` (horizontal), render a fractional `0.05..0.95` coordinate grid (`x, y`) on the candidate preview to locate exact spire/flagpole/subject bounds, and scan the outermost `5%` border strip along Top, Bottom, Left, and Right for: (a) **bright edge leaks** (cut-off bright sky/car/sign or right-edge pillar gap pulling the eye out), (b) **border amputations** (severed tourist heads/caps at the bottom edge, half-sliced bystanders, plaques, traffic cones, or utility/cell towers entering the margin), (c) **kissing tangents**, and (d) **internal lens-flare dots** on dark surfaces. | Outer `5%` perimeter contains zero severed heads/limbs, zero clipped plaques/cones, zero non-sky bright edge leaks where $L_{\text{edge}, P_{95}} > L_{\text{center}, P_{95}} + 25$, and all architectural spires/flags have clean sky breathing room. | **Crop inward using exact fractional coordinates** (locking inner photo and outer canvas to `4:5` or `5:4`), spot-heal internal lens-flare dots from adjacent shadow texture, and/or add **Post-Crop Vignette (`-14 to -28`, Feather `75-85`)** before mounting on exhibition borders. |
| **2. Horizon & Vertical Geometry (`0.5°-3.0°` Tilt Ban)** | Measure dominant horizon lines and central architectural verticals. A tilt between **`0.5° and 3.0°`** always reads as an accidental crooked shutter press, never an intentional Dutch angle (`> 8°`). | Horizon and central vertical lines sit within **`±0.3°`** of true level/plumb, and wide-angle (`23mm-28mm`) vertical keystoning is balanced. | Prescribe or apply exact **Rotate (`-X.X°` to `+X.X°`)** and **Geometry -> Vertical Upright (`-20 to +20`)** before adding exhibition borders. |
| **3. Figure-Ground Squint Test (`Low-Pass Separation`)** | Evaluate a blurred (`GaussianBlur(radius=12)`) or `150px` thumbnail view: does the primary subject (`Figure`) separate in `<200ms` from the background (`Ground`)? | Subject-to-background luminance delta $\Delta L \ge 20\%$ (or distinct warm/cool chromatic isolation) with zero dark-on-dark camouflage mergers. | Add a **Subject / Radial Mask** (`Exposure +0.25 to +0.45 EV`, `Clarity +10`) paired with background luminance suppression in **Color Mix**, or drop the frame in batch culling. |
| **4. Gesture, Stride & Foreground Proportions** | Check pedestrian stride (open inverted-"V" stride vs. static merged legs), multi-subject pocket separation (heads in separate depth pockets), and foreground obstructions (must frame `20%-45%` of the canvas without slicing the subject's eyes). | Clean subject gesture and balanced visual weight across the rule-of-thirds or golden-triangle diagonals. | Pick the superior burst frame, or re-anchor the focal subject onto the upper/lower third intersection via an intentional aspect-ratio crop. |

---

## Pillar 2: Colorimetric & Pixel QA Gate (Every Graded Image & Recipe)

When code execution is available, run this automated pixel audit on every graded output before delivery. When operating in chat-only mode, verify these bounds against the recipe math and histogram:

| QA Check | Formula / Metric | Pass Bound | Auto-Correction When Red |
| :--- | :--- | :--- | :--- |
| **1. Specular Highlight Clipping & White Ceiling** | Relative luminance $Y = 0.2126R + 0.7152G + 0.0722B \in [0, 255]$. Check ratio of pixels at $Y \ge 254$, and check $P_{99.9}$ against the recipe's Point Curve white ceiling $Y_{\text{max}}$. | `Clipped_Hi` ($Y \ge 254$) $\le 0.5\%$ of image pixels; if recipe rolls off whites to $Y_{\text{max}} \le 245$, then $P_{99.9} \le Y_{\text{max}} + 3$ (`0.0%` at `255`). For cool or airy looks, bright pixels ($Y \ge 178$) also hold $\bar{B} - \bar{R} \ge +3$ (cool) and $\bar{R} - \bar{G} \le +2$ (no pink clouds). | Pull `Whites` down by `-8 to -15`, lower Point Curve `(100%, Y%)` anchor, or apply soft shoulder compression above `L = 0.80`; when a large sky area is clipped, lower Exposure first. For pink highlights, move Tint back toward green by `3 to 5` and cool Temp instead. |
| **2. Shadow Toe & Matte Floor Integrity** | Check ratio of pixels at $Y \le 1$, $P_5$ shadow texture density, and minimum luminance $P_{0.1}$ against the Point Curve black floor $Y_{\text{min}}$. | For slide/high-contrast looks: $Y \le 2$ under `3.0%` and $P_5 \ge 6$. For lifted matte looks ($Y_{\text{min}} \ge 10$): **$0.0\%$ of image pixels** below $Y_{\text{min}} - 2$. | Ensure Point Curve black floor is applied **after** any contrast/dehaze step, or raise `Blacks` to `-5..0` so pre-curve blacks do not starve the curve toe. When rendering, set or stretch the black floor on luminance only (scale RGB by $L_{new}/L$); a per-channel offset turns near-black windows and doorways saturated blue or red. |
| **3. Single-Channel Gamut Clipping** | Midtone channel saturation clipping: pixels with $Y \in [25, 240]$ where $\max(R,G,B) = 255$ (high clip) or $\min(R,G,B) = 0$ (zero floor clip, e.g., Blue hitting `0` in warm skin/foliage). | High single-channel clip $< 0.3\%$; Zero single-channel gamut floor $< 1.0\%$. | Enable **Color Chrome luminance compression** (`Red/Orange/Blue Lum -8 to -22`), reduce channel Saturation by `-6 to -12`, or lift Blue curve `(0%, 2%-3%)`. |
| **4. Skin-Tone Vectorscope I-Line / CIE LAB Gate** | Convert midtone skin candidate pixels ($L^* \in [42, 78]$, warm dominant $R > G > B$) to CIE $L^*a^*b^*$. Measure hue angle $h_{ab} = \text{atan2}(b^*, a^*)$, ratio $b^*/a^*$, and chroma $C^*_{ab} = \sqrt{(a^*)^2 + (b^*)^2}$. | $h_{ab} \in [32^\circ, 54^\circ]$, ratio $b^*/a^* \in [0.85, 1.45]$, and chroma $C^*_{ab} \le 42$ (no nuclear orange, magenta sunburn, or greenish jaundice). | If $C^*_{ab} > 42$: lower `Orange Sat -8`. If $b^*/a^* < 0.75$ (magenta): shift `Orange Hue +4`, `Tint -5`. If $b^*/a^* > 1.60$ (yellow/green): shift `Orange Hue -4`, `Color Grading Balance +15`. |
| **5. 8-Bit Histogram Comb (Posterization) Check** | Compute 256-bin luminance histogram $H[k]$ on the image interior (excluding borders). Count empty interior bins ($H[k]=0$ where $H[k-1]>0$ and $H[k+1]>0$) across $[P_5, P_{95}]$. | **`0` interior comb gaps** across $[P_5, P_{95}]$; dynamic spread $P_{95} - P_5 \ge 115$. | Perform all grading math in 32-bit float (`np.float32`) and apply subtle Gaussian dithering / film grain before quantizing to `uint8`. |
| **6. Spatial Halo, Orientation & Border Purity (Including `4:5` / `5:4` Poetic Borders)** | Check EXIF tag `0x0112`, inspect high-contrast roofline edges for bright overshoot halos, and verify top/left/right border RGB values (`#FFFFFF` or `#FCFBF8`). When rendering `4:5` (`1600×2000`) or `5:4` (`2000×1600`) prints with bottom-border poetic typography (e.g., minimalist modern poetry style in `Baskerville Italic` `#706258` + `Baskerville Regular` `#2E2824`), verify both the inner image and outer canvas match exact `4:5` (`0.800`) or `5:4` (`1.250`) proportions. | Pixels upright (`Orientation=1`), zero white edge halos, and top/left/right exhibition borders applied **last** (after vignette & grain) with mean RGB delta $< 1.5$ from `#FCFBF8` (`252, 251, 248`) and balanced bottom poetic margin (`220px` on `4:5`, `176px` on `5:4`). | Transpose EXIF first (`ImageOps.exif_transpose()`), blend low-pass de-sharpening before curves, and compose the `#FCFBF8` gallery border + `Baskerville` typography as the final pipeline step after grading. |

---

## Pillar 3: Calibration Preset (`.xmp`) Schema & 3-Lighting Stress-Test Gate

Every exported `.xmp` preset must pass both **Static Schema Validation** and **Dynamic 3-Lighting Stress-Testing** before shipping:

### 3.1 Mandatory `.xmp` Schema & Portability Checklist

1. **Modern ACR Engine Headers**:
   - `crs:PresetType="Normal"`
   - `crs:UUID="<32-HEX-CHARS>"` (valid uppercase hex UUID, never arbitrary words with hyphens beyond standard UUID structure)
   - `crs:ProcessVersion="15.4"` (or `"11.0"`) and `crs:Version="15.4"`
   - `crs:HasSettings="True"` and `crs:SupportsAmount="True"`
   - `crs:SupportsColor="True"`, `crs:SupportsMonochrome="True"`, `crs:SupportsHighDynamicRange="True"`, `crs:SupportsNormalDynamicRange="True"`, `crs:SupportsSceneReferred="True"`, `crs:SupportsOutputReferred="True"`
2. **Required RDF Child Elements & XML Escaping**:
   - `<crs:Name><rdf:Alt><rdf:li xml:lang="x-default">Preset Name</rdf:li></rdf:Alt></crs:Name>` (always XML-escape special characters such as `&` -> `&amp;` in `B&amp;W` so `ElementTree` and Lightroom XML parsers never fail on invalid tokens).
   - `<crs:Group><rdf:Alt><rdf:li xml:lang="x-default">Preset Group</rdf:li></rdf:Alt></crs:Group>`
   - All 4 Point Curve sequences (`<crs:ToneCurvePV2012>`, `<crs:ToneCurvePV2012Red>`, `<crs:ToneCurvePV2012Green>`, `<crs:ToneCurvePV2012Blue>`) present whenever `crs:ToneCurveName2012="Custom"`, with strictly increasing $X \in [0, 255]$.
3. **Portability Hygiene (Zero Scene Contamination)**:
   - **No baked `crs:Exposure2012`**: omit `crs:Exposure2012` from universal look presets so the preset adapts to each photo's native exposure.
   - **No invalid Kelvin `crs:Temperature="+5"`**: omit `crs:Temperature` and set `crs:WhiteBalance="As Shot"` (or use `crs:IncrementalTemperature` / `crs:IncrementalTint` within `-15..+15` plus Color Grading wheels and RGB curves for warmth).
   - **No baked Crop / Upright / Spot Heal tags**: omit `crs:HasCrop`, `crs:Crop*`, `crs:Perspective*`, and coordinate-bound masks.
   - **Complete 8-Band HSL + 3-Way Color Grading + Calibration reset**: explicitly write all 8 HSL bands (`Red` through `Magenta`), all 3-Way Color Grading tags (`SplitToning*` + `ColorGradeMidtone*` + `ColorGradeShadowLum` + `ColorGradeHighlightLum` + `ColorGradeBlending`), and Camera Calibration (`ShadowTint`, `Red/Green/BlueHue`, `Red/Green/BlueSaturation`) so applying the preset never inherits stale values from a prior edit.

### 3.2 Dynamic 3-Lighting Stress-Test (Bulletproof Preset Calibration)

Before declaring a preset calibrated, simulate applying its exact Tone Curves, HSL matrix, and 3-Way Color Grading across three canonical synthetic/real test distributions:
1. **Stress Scenario A: High-Key Daylight Sky & Architecture**: verify skies shift cleanly without cyan/purple posterization and highlights roll off below `248/255`.
2. **Stress Scenario B: Golden-Hour Warm Portrait / Street Skin**: verify skin stays within CIE LAB $h_{ab} \in [32^\circ, 54^\circ]$ and $C^*_{ab} \le 42$ without orange/red channel clipping.
3. **Stress Scenario C: Low-Key Twilight / Underexposed Street Shadow**: verify the shadow toe ($P_5$ and $P_{10}$) preserves detail without crushing into solid black blobs or introducing toxic blue/green shadow noise.
