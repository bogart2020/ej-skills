# Camera RAW Systems & Style Replication Playbooks

Specialized camera sensor color-science neutralization rules, file-format headroom bounds, look-archetype recipes, and Lightroom Mobile Free-tier global workarounds referenced in [`SKILL.md`](../SKILL.md).

## Contents

1. Camera RAW sensor baselines (1B batch culling, 1C cross-sensor emulation)
2. 5-zone tonal and 8-band color decomposition
3. Look archetypes (A to J)
4. Free-tier fallbacks

## 1. Camera RAW sensor baselines & input profile neutralization

Every camera manufacturer encodes a distinct `ColorMatrix1/2`, `ForwardMatrix1/2`, `BaselineExposure`, and default `ProfileToneCurve` inside its RAW files (Adobe DNG Specification v1.7.1.0). Applying the exact same Lightroom Mobile slider values to a Sony `.ARW`, a Canon `.CR3`, an iPhone `.DNG` (Apple ProRAW), and a baked `.JPEG` produces visibly different results. Before transferring the reference look from Photo 2, neutralize Photo 1's sensor baseline:

| Camera System / File Format | Native Sensor & Color Matrix Characteristics in LR Mobile | Pre-Grade Neutralization Adjustment |
| :--- | :--- | :--- |
| **Sony Alpha (`ARW`)** *(A7 III / A7 IV / A7R V / A7C II / ZV-E1 / A6700)* | Older Bionz X sensors (A7 III, A6400) exhibit a slight green-yellow cast in shadows and cooler magenta-shifted highlights on *Adobe Color*, with a steep default shadow drop. Newer Bionz XR bodies (A7 IV, A7R V, A7C II) have cleaner skin tones but still render foliage cooler/greener than Canon. | Start on **Adobe Standard** or **Adobe Neutral** (or **Camera Standard** if available). For older Bionz X bodies, add **Tint `+4 to +8` (toward Magenta)**, shift **Color Mix -> Orange Hue `-3 to -6`** (warmer skin), and **Yellow Hue `-8 to -12`** before applying the reference grade. |
| **Canon EOS (`CR2` / `CR3`)** *(R5 / R6 II / R8 / R50 / 5D IV)* | Strong red-orange skin-tone bias and punchier default midtone contrast; reds and oranges saturate rapidly when increasing Contrast or Vibrance, and highlights roll off warmly. | Start on **Adobe Neutral** (for soft/film looks) or **Adobe Standard**. Pull **Color Mix -> Red Hue `+4 to +8`**, **Orange Saturation `-6 to -12`**, and **Shadows `+10 to +18`** to prevent skin from turning overly tangerine when adding warm reference grading. |
| **Nikon Z / F (`NEF`)** *(Z8 / Z9 / Z6 III / Zf / D850)* | Neutral-to-warm yellow-green rendering with high linear shadow dynamic range (ISO-invariant Sony-fabricated sensors with Nikon color matrices) and slightly cooler blues. | Start on **Adobe Standard** or **Camera Flat / Neutral**. Shift **Yellow Hue `+5 to +10`** if foliage looks too chartreuse, and use **Blacks** rather than heavy **Contrast** to set the shadow floor. |
| **Fujifilm X / GFX (`RAF`)** *(X100VI / X-T5 / X-Pro3 / X-S20 / GFX100 II)* | X-Trans CFA demosaicing has high color fidelity and film-like blue/green separation. If the user shot with an in-camera Film Simulation, LR Mobile defaults to *Adobe Color* unless switched to **Camera Matching**. | In **Profiles -> Browse -> Camera Matching**, pick the closest Fujifilm base (**Camera Classic Chrome** for documentary/muted looks, **Camera Classic Neg.** for high-contrast street, **Camera Nostalgic Neg.** for warm amber highlights, **Camera Astia/Provia** for clean portraits). In **Detail**, keep Sharpening **Detail $\le 25$** and **Masking $\ge 40$** to avoid X-Trans "worm" artifacts. |
| **Leica / Panasonic Lumix / OM System / Ricoh GR (`DNG` / `RW2` / `ORF`)** | Native DNG cameras (Leica Q3/M11, Ricoh GR III/IIIx) embed vendor profiles with high micro-contrast and deep shadow falloff; Ricoh GR DNGs often underexpose highlights by `-0.3 to -0.7 EV` to protect sky detail. | Check `BaselineExposure` headroom first: lift **Exposure `+0.25 to +0.50 EV`** and **Shadows `+15 to +25`** on Ricoh GR / Leica DNGs before matching midtone luminance to Photo 2. |
| **Apple ProRAW (`DNG`)** *(iPhone 12 Pro through iPhone 16 Pro / Max)* | **Critical computational RAW behavior**: Apple ProRAW is an already-demosaiced, multi-frame merged 12-bit/16-bit linear DNG carrying an embedded **`ProfileGainTableMap`** (semantic local tone mapping that brightens faces, compresses skies, and sharpens edges). Leaving the **Apple ProRAW** profile at `100%` fights film curves and causes HDR haloing when pulling Highlights down. | 1. Open **Profiles -> Apple ProRAW** and drag the **Profile Amount slider down to `30%-55%`** (or switch Profile to **Adobe Color / Adobe Neutral**) to flatten Apple's baked Smart HDR local tone map.<br>2. Set **Detail -> Sharpening Amount to `0-15`** (ProRAW already has baked multi-frame edge sharpening).<br>3. Compensate for mobile highlight clipping by using the **Point Curve White Point `(100%, 92%-96%)`** rather than pushing the `Highlights` slider to `-100` (which creates gray plastic skin/skies on ProRAW). |
| **Samsung Expert RAW / Google Pixel RAW (`DNG`)** | Multi-frame computational DNGs with aggressive shadow noise reduction and vivid blue/green saturation matrices; highlights clip abruptly if over-exposed at capture. | Switch Profile from the default embedded profile to **Adobe Standard** or **Adobe Neutral** to remove excessive cyan-sky and neon-green boosts; reduce **Vibrance `-8 to -15`** before applying the target look. |
| **8-bit Baked JPEG / HEIC / PNG** *(Camera JPEG, downloaded image, or phone non-RAW)* | Gamma-encoded 8-bit ($256$ levels per channel) with white balance, tone curve, and sharpening permanently baked in; clipped `255` whites and `0` blacks contain zero recoverable detail. **Temp** slider is relative (`-100 to +100`) instead of Kelvin (`2000K-50000K`). | 1. Report **Temp** on the **`-100 to +100` relative scale** (never Kelvin).<br>2. Keep global **Temp / Tint within `±30`**, **Highlights / Shadows within `±65`**, and **HSL Luminance within `±40`** to prevent 8-bit banding and posterization.<br>3. Use the **Tone Curve** and **Color Grading wheels** (which operate smoothly across 8-bit luma ranges) to reshape contrast and color casts instead of extreme White Balance or Dehaze sliders. |


**Starting Profile for Photo 1 (Step 2):**

- **Apple ProRAW (`.DNG`)**: keep **Apple ProRAW** selected and lower **Profile Amount to `30%-55%`** (or switch to **Adobe Neutral / Adobe Color**) so Apple's baked `ProfileGainTableMap` Smart HDR tone map does not fight the reference Tone Curve.
- **Sony (`ARW`) / Canon (`CR3`) / Nikon (`NEF`) / Leica & Ricoh (`DNG`)**: **Adobe Neutral** (low-contrast film/matte references), **Adobe Standard** (balanced natural grades), **Adobe Color** (punchy vibrant references), or **Adobe Monochrome** (B&W), plus the brand pre-offsets in the table above.
- **Fujifilm (`RAF`)**: the closest **Camera Matching** profile (**Camera Classic Chrome**, **Camera Classic Neg.**, **Camera Nostalgic Neg.**, **Camera Astia**, or **Camera Acros**) when available on RAW, or **Adobe Standard** with matching HSL offsets.
- **8-bit JPEG / HEIC**: White Balance `Temp` uses the relative **`-100 to +100`** scale; keep global sliders within the anti-banding limits in the table above. Adobe Raw profiles (Adobe Neutral, Standard, Color) are not offered for JPEG/HEIC; start from the Color profile (or Monochrome for black and white) or a creative profile.

### 1B. Batch RAW Culling & 5-Slot Carousel Sequencing Gate

When the user supplies a folder or Google Drive batch of RAW/DNG files and asks to select and grade the best shots:

1. **Extract EXIF & Orient Previews First**:
   - **Google Drive folder links**: download into a workspace subfolder with `gdown --folder "<url>"`. When `gdown` is missing or `pip` refuses a system install (`externally-managed-environment`), create a virtual environment (`python3 -m venv <dir>/venv`, then `<dir>/venv/bin/pip install gdown pillow numpy rawpy`) and run the download in the background; large folders take minutes, so start culling local files meanwhile. If Drive returns HTTP `302` to `accounts.google.com/ServiceLogin` or `401 Unauthorized`, ask the user to either switch the folder's **General access** from **Restricted** to **Anyone with the link (Viewer)** and click **Done**, or drag the RAW/DNG files directly into the local workspace folder.
   - Inspect `make`, `model`, `pixelWidth`, `pixelHeight`, and EXIF Orientation tag (`0x0112`) via `sips -g all` or Python `PIL`.
   - **Verify the real file type** from the first bytes, never the extension: `head -c 4 <path> | xxd -p` gives `ffd8...` for JPEG and `4d4d002a` or `49492a00` for a TIFF-based RAW/DNG (the `file` command can mislead, since JPEG EXIF blocks also mention TIFF). Shared folders often hold JPEGs renamed `.DNG`; those take the 8-bit JPEG rules. If a true RAW still fails in `rawpy`, convert it with macOS `sips -s format jpeg -s formatOptions 100 -Z 3000 <in> --out <out.jpg>` and label previews from it as estimates.
   - Always run `ImageOps.exif_transpose()` when generating preview thumbnails (`1200px` max edge) or graded exports so portrait-oriented smartphone/camera RAWs (`Orientation=6`) are evaluated right-side up.
2. **Apply Culling Knockout Criteria**:
   - **Drop test/filler frames**: flat, underexposed indoor surfaces or accidental shutter presses with no clear subject.
   - **Drop awkward edge/background intersections**: tight crops where window muntins, poles, or frames slice unnaturally through a subject's head or halo.
   - **Drop dead negative space**: backlit silhouettes where the background sky or wall has zero tonal gradient or story context.
   - **Drop redundant duplicates**: when two frames cover the same landmark or subject, keep the frame with stronger typographic punch, cleaner leading lines, or higher native resolution (such as a `48MP` `8064×6048` ProRAW main-sensor capture over a `12MP` crop).
3. **Assign Surviving Frames to the 5-Slot Carousel Blueprint**:
   - **Slide 01: Hero Hook (Thumb-Stopper)**: Wide environmental establishing frame with the strongest leading lines, architectural symmetry, or warm/cool color contrast.
   - **Slide 02: Dynamic Action & Night Mood**: High-contrast street scene, vibrant neon signage, or pedestrian motion blur that shifts energy from Slide 01.
   - **Slide 03: Intimate Texture / Detail Study**: Tight organic material study (woven lantern, stone texture, warm tungsten filament against twilight).
   - **Slide 04: Cultural / Location Anchor**: Heritage landmark, glowing archway typography, or sense-of-place frame.
   - **Slide 05: Scale & Atmospheric Climax**: Vertical architectural perspective, expansive cloud/sky texture, or emotional closing frame.

### 1C. Cross-Sensor & Optical System Emulation (Mimicking Target Sensors on Bayer / ProRAW)

When the user wants a Bayer mirrorless sensor (Sony, Canon, Nikon) or computational phone RAW (iPhone 16 Pro Apple ProRAW) to mimic a **target camera sensor and lens architecture**, most notably the **Fujifilm X100VI (40.2MP APS-C X-Trans CMOS 5 HR BSI sensor + X-Processor 5 + Fujinon 23mm f/2 Mark II lens)** with an organic, *"not too sharp"* rendering, translate all four hardware pillars:

| Target Hardware Pillar | Physical Sensor / Lens Behavior | Lightroom Mobile Slider Translation | Direct Python Render Translation |
| :--- | :--- | :--- | :--- |
| **1. Anti-Clinical Edge De-Sharpening (*"Not Too Sharp"*)** | The 40.2MP X-Trans 5 HR (`3.04µm` pitch) paired with Fujifilm recipes uses in-camera `Sharpness -2` to avoid digital edge ringing, whereas Apple ProRAW bakes multi-frame Smart HDR sharpening (`ProfileGainTableMap`) that looks crunchy. | Lower **Profile Amount to `30%-50%`**; set **Detail -> Sharpening Amount `10-15`**, **Radius `0.8`**, **Detail `15`**, and **Edge Masking `70-80`** (zero sharpening on skin, skies, and flat walls); set **Effects -> Texture `-4 to -8`**. | Blend the source image with a micro-softened low-pass layer (`GaussianBlur(radius=0.7)`, `alpha=0.35`) *before* applying tone curves to strip computational edge halos. |
| **2. Fujinon 23mm f/2 & In-Camera Negative Clarity (`-2 to -3`) Halation** | Wide-open spherical aberration on the 23mm f/2 lens (often paired with a 1/8 Black Pro-Mist or CineBloom filter) plus Fuji's negative Clarity creates a dreamy highlight bloom around neon signs, lamps, and bright skies without losing core focus. | Set **Effects -> Clarity `-14 to -18`** paired with **Dehaze `+4`** (so black levels stay anchored while midtones/highlights soften). On Premium, add a **Radial Mask** over practical lights (`Texture -20, Clarity -20, Dehaze -15`). | Extract highlights (`L > 0.70`), blur with `GaussianBlur(radius=4.5)`, and screen/add `15%-20%` highlight bloom back onto the de-edged base. |
| **3. X-Processor 5 Color Chrome Effect (`CCE` & `Color Chrome FX Blue`)** | Standard Bayer matrices clip high-saturation channels into flat pastels. Fuji's 64-bit X-Processor 5 compresses luminance in deeply saturated reds, ambers, and skies so colors look dense and velvety, while shifting skies toward Classic Chrome cyan-teal. | In **Color Mix (HSL)**, pull **Luminance down on saturated bands**: **Red Lum `-10 to -15`**, **Orange Lum `-4 to -8`**, **Yellow Lum `-4 to -8`**, and **Blue Lum `-18 to -25`** (Color Chrome Blue); shift **Blue Hue `-10 to -15`**. (In LR Desktop/`.xmp`, also set **Calibration -> Blue Primary Hue `-12`, Sat `+15`**.) | Compute per-pixel HSV saturation `S = (max - min) / max` and attenuate RGB luminance by `1 - clip(S * 0.22, 0, 0.22)`; attenuate blue channel by `0.86-0.88` where `B > R * 1.08`, and add `+0.025` green into sky pixels (`B > R` and `B > 0.25`). |
| **4. 6x6 Aperiodic Multi-Scale Grain Clumping** | Unlike uniform 2x2 Bayer pixel noise, the pseudo-random 6x6 X-Trans CFA produces organic silver-halide grain clusters that are pronounced in midtones and shadows but roll off cleanly in bright highlights. | Set **Effects -> Grain Amount `35-40`**, **Size `45-55`**, **Roughness `60-65`**. | Combine `65%` fine Gaussian noise (`σ=0.010`) with `35%` 2x bilinear-upscaled coarse noise (`σ=0.016`), multiplied by a midtone luminance mask `clip(1.1 - (L - 0.25)^2 * 1.8, 0.1, 1.0)`. |

---

## 2. Quantitative 5-zone tonal & 8-band chromatic decomposition

When code execution (`python3` with `PIL` / `numpy`) is available in the active environment and the image files are accessible on disk, inspect the source and reference images quantitatively before writing slider values:

1. **Compute luminance percentiles** ($L = 0.2126 R + 0.7152 G + 0.0722 B$ in sRGB):
   - **Black Floor ($P_1, P_5$)**: If Reference $P_1 > 12/255$ ($>5\%$), the reference has a **lifted matte black point** `(0%, 5%-12%)` on the Master RGB Point Curve.
   - **Shadow Density ($P_{10}, P_{25}$)**: Maps to **Shadows** slider and Point Curve `(25%, Y%)` anchor.
   - **Midtone / Skin Anchor ($P_{50}$)**: Maps to **Exposure ($\text{EV}$)** and Point Curve `(50%, Y%)` anchor. Each $\pm 1.00\text{ EV}$ shift corresponds to roughly a $2\times$ linear luminance factor ($\approx \pm 20\text{ to }25\%$ in midtone sRGB code value).
   - **Highlight Shoulder ($P_{75}, P_{90}$)**: Maps to **Highlights** slider and Point Curve `(75%, Y%)` anchor.
   - **White Ceiling ($P_{95}, P_{99}$)**: If Reference $P_{99} < 242/255$ ($<95\%$), the reference has **compressed/rolled-off creamy whites** `(100%, 88%-95%)` on the Master RGB Point Curve.
2. **Compute per-zone chromaticity cast ($\Delta R, \Delta G, \Delta B$ in Shadows, Midtones, Highlights)**:
   - Compare mean $(R - G)$ and $(B - \frac{R+G}{2})$ separately across dark pixels ($L \in [5\%, 30\%]$), midtones ($L \in [30\%, 70\%]$), and bright pixels ($L \in [70\%, 95\%]$).
   - Translate shadow and highlight RGB offsets into **Color Grading wheel Hue ($0^\circ\text{-}360^\circ$) and Saturation ($0\text{-}100$)**:
     - $0^\circ$ = Red | $30^\circ$ = Warm Orange | $45^\circ\text{-}55^\circ$ = Golden Amber/Yellow | $120^\circ$ = Green | $180^\circ\text{-}195^\circ$ = Cyan/Teal | $210^\circ\text{-}225^\circ$ = Cool Steel Blue | $240^\circ$ = Deep Blue | $300^\circ\text{-}330^\circ$ = Magenta/Rose.

---

## 3. Canonical style & look archetypes in Lightroom Mobile

Use these calibrated signatures to anchor specific photographic looks when Photo 2 exhibits one of these classic aesthetics, adjusting every number to Photo 1's actual starting histogram:

### A. Warm Analog Film (Kodak Portra 400 / Fuji Pro 400H Aesthetic)
- **Tonal Signature**: Soft lifted blacks `(0%, 5%-8%)`, gentle shadow lift `(25%, 28%-32%)`, slightly compressed creamy highlights `(100%, 93%-96%)`, negative Contrast (`-10 to -20`), positive Shadows (`+20 to +40`), negative Highlights (`-25 to -50`).
- **Per-Channel RGB Curves**: Subtle warm S-curve in **Red** (pull darks down `-2%`, lift upper midtones `+2%`), gentle lift in **Green** midtones (`+1% to +2%`), and inverse tilt in **Blue** (lift deep shadows `(0%, 3%)`, pull highlights down `(100%, 95%)` for creamy warm skies/highlights).
- **HSL Color Mix**:
  - **Orange**: Hue `-4 to +4`, Sat `-5 to -12`, Lum `+6 to +15` (luminous, natural skin).
  - **Yellow**: Hue `-15 to -25` (shift toward warm gold), Sat `-15 to -30`, Lum `+5 to +10`.
  - **Green**: Hue `+15 to +35` (toward emerald/cyan-green, away from neon yellow-green), Sat `-30 to -55`, Lum `-10 to +5`.
  - **Aqua / Blue**: Blue Hue `-10 to -22` (toward cyan/teal sky), Sat `-15 to -30`, Lum `-5 to -18`.
- **Effects**: Texture `-5 to -12`, Clarity `-5 to -10`, Dehaze `-3 to +5`, Grain Amount `15-24`, Size `25-30`, Roughness `50-60`.

### A2. Classic Chrome Portra Hybrid (Fujifilm X100VI / X-Trans Classic Chrome + Kodak Portra 400)
- **Tonal Signature (DR400% Rolloff)**: Lifted matte shadow floor `(0%, 5.5%-6.5% / 8-bit 14-16)`, slightly dipped shadow toe `(23%, 21% / 58, 54)`, anchored midtones `(50%, 50% / 128, 128)`, gentle upper-mid lift `(78%, 79%-80% / 198, 202-204)`, and rolled-off creamy white ceiling `(100%, 94%-96% / 255, 240-244)`. **Blue Curve** pulls highlights slightly down `(50%, 48.5% / 128, 124)` and `(100%, 96.5%-97% / 255, 246-248)` for golden highlight warmth.
- **Light Sliders**: Exposure `0.00 to +0.25 EV`, Contrast `-5 to -8`, Highlights `-25 to -30`, Shadows `+22 to +25`, Whites `+8 to +12`, Blacks `-8 to -10`.
- **Color & HSL Color Mix**:
  - **White Balance**: Warm shift (`Temp +5 to +6` or `+300K to +450K` warmer than As Shot, `Tint +2 to +3`), Vibrance `+4 to +5`, Saturation `-4 to -5`.
  - **Red**: Hue `+4`, Sat `+6`, Lum `+2` (`-12` when X-Trans Color Chrome Effect is active).
  - **Orange (Skin & Warm Practicals)**: Hue `-2`, Sat `+6 to +8`, Lum `+10` (`-6` with Color Chrome compression).
  - **Yellow**: Hue `-14` (pushes sickly greenish-yellow toward warm amber gold), Sat `-8`, Lum `+6` (`-4` with CCE).
  - **Green (Foliage)**: Hue `+26` (shifts digital neon green toward nostalgic film olive), Sat `-26 to -28`, Lum `-4`.
  - **Aqua**: Hue `-8`, Sat `-12`, Lum `0`.
  - **Blue (Sky & Twilight Shadows)**: Hue `-10 to -12` (Classic Chrome cyan shift), Sat `-16 to -18`, Lum `-6` (`-22` with Color Chrome FX Blue).
- **Color Grading**: Highlights Hue `46°-48°` (Warm Kodak Cream), Sat `14%`; Shadows Hue `215°` (Balanced Slate-Teal), Sat `8%`; Balance `0`.
- **Effects & Detail (Clean vs. X100VI Soft Variant)**:
  - *Standard Portra*: Texture `+10`, Clarity `-8`, Dehaze `+4`, Grain Amount `28`, Size `30`, Roughness `50`, Sharpening `30` (Masking `35`).
  - *X100VI Soft Organic ("Not Too Sharp")*: Texture `-4`, Clarity `-16`, Dehaze `+4`, Grain Amount `38`, Size `45`, Roughness `60`, Sharpening `12` (`Radius 0.8, Detail 15, Masking 75`).

### B. Moody Dark / Desaturated Forest, Street & Automotive
- **Tonal Signature**: Deep crushed midtones with a matte black floor: RGB Curve `(0%, 7%-11%)`, dipped shadow anchor `(25%, 18%-22%)`, controlled midtones `(50%, 44%-48%)`, muted white ceiling `(100%, 86%-92%)`. Exposure `-0.30 to -0.70 EV`, Highlights `-40 to -75`, Shadows `+15 to +35`, Whites `-20 to -45`, Blacks `-15 to -35`.
- **HSL Color Mix**:
  - Desaturate **Yellow (`-50 to -80`)**, **Green (`-60 to -90`)**, **Aqua (`-40 to -70`)**, **Blue (`-45 to -75`)**, **Purple/Magenta (`-60 to -85`)**, while keeping **Red** and **Orange** selectively intact (`Sat -10 to +10`, `Lum +4 to +12`) so skin or tail-lights/warm practicals pop against the monochrome-leaning environment.
- **Color Grading**: Shadows Hue `205°-225°` (Cool Slate/Teal), Sat `10-18`, Lum `-10 to -20`; Midtones Hue `35°-45°` (Warm Bronze), Sat `6-12`; Highlights Hue `40°-55°` (Muted Warm Cream), Sat `8-15`; Blending `60-75`, Balance `-15 to -30`.
- **Local Masking**: **Subject Mask** (`Exposure +0.25 to +0.45 EV`, `Clarity +10`) + **Inverted Radial Gradient** or **Linear Gradient** on foreground (`Exposure -0.40 to -0.80 EV`, `Dehaze +10`).

### C. Bright, Airy & Editorial Clean (Wedding, Lifestyle, Interior)
- **Tonal Signature**: High-key luminance with open shadows and luminous skin: Exposure `+0.35 to +0.85 EV`, Contrast `-15 to -30`, Highlights `-30 to -55`, Shadows `+35 to +65`, Whites `+15 to +30`, Blacks `+15 to +35`. RGB Curve lifts `(0%, 3%-5%)`, `(25%, 30%-35%)`, `(50%, 56%-60%)`, `(75%, 80%-83%)`, `(100%, 98%-100%)`.
- **HSL Color Mix**:
  - **Orange**: Hue `+2 to +6`, Sat `-10 to -18`, Lum `+12 to +22` (bright porcelain/editorial skin).
  - **Yellow & Green**: Yellow Sat `-35 to -55`, Lum `+15 to +25`; Green Hue `+10 to +25`, Sat `-45 to -70`, Lum `+15 to +30` (light sage foliage).
  - **Blue**: Hue `-8 to -15`, Sat `-20 to -35`, Lum `+10 to +25` (pastel airy sky).

### D. Cinema Teal & Orange / Night Neon / Cyberpunk
- **Tonal Signature**: Strong S-curve contrast (`(0%, 4%)`, `(25%, 19%)`, `(50%, 50%)`, `(75%, 82%)`, `(100%, 97%)`), Highlights `-35 to -60` (recovering neon sign bloom), Blacks `-10 to -25`.
- **Color & HSL**: Cooler White Balance (`Temp 3600K-4400K` or `-15 to -30`, `Tint +8 to +22`). Shift **Red Hue `+15 to +30`** (toward orange), **Yellow Hue `-25 to -45`** (toward orange), **Green Hue `+60 to +90`** (toward teal), **Blue Hue `-20 to -35`** (toward cyan/electric blue), **Purple/Magenta Sat `+15 to +35`**.
- **Color Grading**: Shadows Hue `195°-215°` (Deep Teal/Cyan), Sat `22-38`; Highlights Hue `28°-42°` (Warm Amber/Orange), Sat `20-35`; Blending `45-60`.
- **Effects**: Clarity `-10 to -20` combined with Dehaze `-10 to -18` (or a Radial Mask around light sources with `Dehaze -25`, `Texture -20`) to replicate **optical halation / bloom filter (CineBloom / Black Pro-Mist)** glow.

### E. High-Contrast Monochrome / Classic B&W Film (Ilford HP5 / Kodak Tri-X / Ricoh GR Hi-Contrast B&W)
- **Profile**: Switch to **B&W -> Adobe Monochrome** or **B&W 01 / Camera Acros**.
- **B&W Color Mix (Luminance Channel Weights)**: Instead of HSL, adjust the 8 **B&W Mix** sliders to control how original scene colors map to gray tones:
  - **Orange `+15 to +30`** and **Red `+10 to +20`** (brighten skin tones and blemishes).
  - **Blue `-35 to -65`** and **Aqua `-25 to -45`** (dramatic dark skies, replicating a physical Red/Orange contrast filter).
  - **Green `-15 to +20`** and **Yellow `+15 to +35`** (separate foliage from shadows).
- **Tone Curve & Grain**: Classic film toe and shoulder (`(0%, 5%)`, `(20%, 14%)`, `(50%, 52%)`, `(80%, 86%)`, `(100%, 96%)`, or for **Ricoh GR Hi-Contrast B&W**, crush the toe to `(0%, 1.5%)`, `(28%, 18%)`, `(72%, 78%)`, `(100%, 98.5%)` with Vignette `-25`), Grain Amount `25-38`, Size `30-40`, Roughness `55-65`.

### F. Ricoh GR III / GR IIIx "Positive Film" (Royal Supra / Street Slide Aesthetic)
- **Tonal Signature (Highlight-Weighted Slide Contrast)**: Deep, ink-rich blacks `(0%, 2.5% / 8-bit 6)`, steep punchy shadow toe `(22%, 18% / 56, 46)`, crisp midtone separation `(50%, 48% / 128, 122)`, and rolled slide-film shoulder `(75%, 76% / 191, 194)`, `(100%, 96% / 255, 245)`. **Blue Curve** lifts deep shadows slightly `(0%, 3.2% / 0, 8)` for a cool indigo shadow undertone and pulls highlights to `(100%, 94% / 255, 240)` for warm cream highlights.
- **Light Sliders**: Exposure `-0.15 to -0.35 EV` (emulating Ricoh Highlight-Weighted Metering), Contrast `+12 to +18`, Highlights `-30 to -45`, Shadows `-12 to -20`, Whites `+10 to +15`, Blacks `-15 to -25`.
- **HSL Color Mix (Slide Film Separation)**:
  - **Red**: Hue `-4`, Sat `+18`, Lum `-10` (signature Ricoh GR punchy carmine-red street pop).
  - **Orange**: Hue `-4`, Sat `+10`, Lum `+4` (rich golden-amber skin and warm street lamps).
  - **Yellow**: Hue `-10`, Sat `+6`, Lum `+4`.
  - **Green**: Hue `+18`, Sat `-35`, Lum `-18` (deep, dark forest/urban foliage that steps back into shadow).
  - **Aqua**: Hue `-6`, Sat `-15`, Lum `-10`.
  - **Blue**: Hue `+2 to -4`, Sat `+10`, Lum `-22` (signature deep Cobalt / Prussian blue slide sky).
- **Color Grading & Effects**: Shadows Hue `225°` (Cool Indigo), Sat `10%`; Highlights Hue `44°` (Warm Cream), Sat `12%`; Texture `+8`, Clarity `+6`, Vignette `-18` (Midpoint `40`, Feather `80`, emulating GR 18.3mm/28mm wide-open corner falloff), Grain Amount `22`, Size `25`, Roughness `50`.

### G. Classic Cuban Negative (Fujifilm `Classic Neg.` base)
- **In-Camera Fujifilm Recipe Blueprint**: `Classic Neg.` (Fujicolor Superia consumer negative matrix), `DR400%` (`ISO 500` floor), `WB: Auto (Shift R: +4, B: -5)`, `Highlight Tone: -2`, `Shadow Tone: +1`, `Color: +4`, `Color Chrome Effect: Strong`, `Color Chrome FX Blue: Strong`, `Clarity: -4`, `Sharpness: 0`, `High ISO NR: -4`, `Grain: Strong, Large`.
- **Tonal & RGB Curve Signature (Superia Emulsion Crossover)**:
  - **Master RGB**: `(0%, 5.5% / 0, 14) -> (22%, 17% / 56, 43) -> (50%, 49% / 128, 125) -> (75%, 73% / 191, 186) -> (100%, 93% / 255, 237)` (lifted matte floor, steep `Shadow +1` toe, creamy `DR400 + Highlight -2` shoulder).
  - **Red Curve**: `(0, 0) -> (61, 52) -> (133, 138) -> (204, 210) -> (255, 252)` (pulls Red down in shadows for cyan-teal crossover and lifts midtones/highlights for `R: +4` copper warmth).
  - **Green Curve**: `(0, 3) -> (64, 62) -> (128, 125) -> (255, 250)`.
  - **Blue Curve**: `(0, 6) -> (64, 62) -> (128, 119) -> (191, 180) -> (255, 233)` (cool teal shadow floor + strong `B: -5` golden-amber midtone and postcard-cream highlight shift).
- **Light & White Balance**: `Contrast +10`, `Highlights -38`, `Shadows -10`, `Whites +6`, `Blacks -8`; `WhiteBalance="As Shot"`, `IncrementalTemperature +14`, `IncrementalTint +8`, `Vibrance +24`, `Saturation +6`.
- **8-Band HSL (`Color: +4` + `Color Chrome Strong` + `FX Blue Strong`)**:
  - **Red**: Hue `+6`, Sat `+18`, Lum `-16` (dense, velvety terracotta/vermilion reds via Color Chrome Strong luminance compression).
  - **Orange**: Hue `-4`, Sat `+12`, Lum `-6` (toasted copper-bronze skin & sunlit colonial walls).
  - **Yellow**: Hue `-18`, Sat `+10`, Lum `-8` (warm Cuban ochre / marigold).
  - **Green**: Hue `+28`, Sat `-34`, Lum `-14` (muted dark olive-emerald foliage).
  - **Aqua**: Hue `-12`, Sat `+8`, Lum `-12`.
  - **Blue**: Hue `-16`, Sat `+10`, Lum `-24` (nostalgic deep cyan-teal sky via Color Chrome FX Blue Strong).
  - **Purple / Magenta**: Purple Hue `-10`, Sat `-20`, Lum `-10`; Magenta Hue `-8`, Sat `-16`, Lum `-8`.
- **3-Way Color Grading, Effects & Calibration**:
  - **Color Grading**: Shadows Hue `196°` (Cyan-Teal), Sat `12`, Lum `-4`; Midtones Hue `34°` (Warm Copper), Sat `10`; Highlights Hue `44°` (Cuban Gold), Sat `16`; Blending `58`, Balance `+12`.
  - **Effects**: `Texture -6`, `Clarity -22` (`Clarity: -4` halation diffusion), `Dehaze +6`, `Grain Amount 42`, `Size 52`, `Roughness 62` (`Grain: Strong, Large`), `Vignette -14` (`Midpoint 42`, `Feather 78`, `Highlights 25`).
  - **Calibration**: `Shadow Tint -6`, `Red Hue +6 / Sat +8`, `Green Hue +18 / Sat -10`, `Blue Hue -14 / Sat +16`.
- **Editorial 4:5 / 5:4 Exhibition Border & Poetic Caption Option**: When the user requests `4:5` (vertical) or `5:4` (horizontal) framing with poetic on-screen text in the bottom white border (such as minimalist poetry or fine-art book plate style), crop the inner image to fit inside a `4:5` (`1600x2000`) or `5:4` (`2000x1600`) warm museum paper canvas (`#FCFBF8`) with balanced top/left/right margins (`4.2%`) and a weighted bottom gallery margin (`11%-13%`) that houses centered literary serif verse in warm charcoal ink (`#2C2623`).

### H. Airy Washed-Green Fine Art Landscape
- **Visual Character**: Minimalist, airy fine art outdoor aesthetic. Highlights and skies are clean, cool-neutral daylight with zero yellow or sepia cast (`Highlight Blue > Red`). Foliage is muted into soft sage and olive green, while sand, stone, and terracotta retain warm presence. Midtones are bright and luminous (`P50 ~ 130-165`), while deep shadow crevices stay crisp and anchored (`P1 ~ 5-20`). Micro-contrast has a dreamlike diffusion from negative clarity, balanced by sharp optical edges.
- **The 5-Step Workflow**:
  1. **Apply Preset**: Save this section's Color Mix, Tone Curve, Split Toning, and Camera Calibration values as a preset and apply it. Base profile is **Adobe Standard** on RAW or **Color** on JPEG.
  2. **Adjust Strength of Preset**: Set the Preset Amount slider to `65%-75%` (enabled by `crs:SupportsAmount="True"`). This scales Camera Calibration, extreme HSL saturation swings, and per-channel RGB curves so the look suits direct sunlight without overpowering colors into sepia.
  3. **Adjust White Balance**: Cool the White Balance (`Temp -6 to -12`, `Tint +1 to +3` toward magenta) so clouds, sea spray, and open skies stay clean daylight pastel blue (`Highlight Blue > Red`), eliminating warm yellow tints from highlights.
  4. **Adjust Exposures**: Set Exposure from the source's own median: `EV = log2(target / source)` in linear light, aiming for output `P50 ~ 130-165` and capped to `-0.60 to +0.60 EV` when the source `P99 > 240` (bright sky that would clip), otherwise up to `+1.50 EV`. An already bright, hazy frame needs a negative value; a backlit frame with bright sky hits the `+0.60` cap and leans on Shadows. Pull Highlights (`-45 to -65`) and Whites (`-20 to -35`) to recover cloud and water textures. Raise Shadows (`+45 to +60`) to open backlit foliage. Keep Blacks (`-20 to -28`) negative to anchor shadow contrast.
     - **Cast and ceiling checks**: Sony Bionz X's Tint offset plus this look's magenta pull can turn clouds pink. Keep bright pixels (`L > 70%`) at `mean B - mean R >= +3` and `mean R - mean G <= +2`; when pink, return Tint toward `+2` and cool Temp instead. Keep `P99 <= 250` with visible cloud texture; when the sky clips, lower Exposure before adding more negative Highlights. On backlit skin, the Orange boost reads red: hold Orange Sat at `+6` or less and run the skin-tone check.
  5. **Add Negative Clarity**: Set Clarity to `-10 to -16` to create soft atmospheric glow and halation across midtones. Keep Texture at `-2` and Sharpening at `40` (Radius `1.0`, Masking `15-25`) so fine details stay crisp.
- **Tone Curve & Per-Channel RGB Curves**:
  - **Master Tone Curve**: `(0, 0) -> (66, 63) -> (164, 179) -> (255, 255)`
  - **Red Channel Curve**: `(0, 0) -> (43, 14) -> (84, 58) -> (123, 125) -> (184, 198) -> (255, 255)`
  - **Green Channel Curve**: `(0, 0) -> (40, 14) -> (83, 59) -> (123, 126) -> (172, 185) -> (255, 255)`
  - **Blue Channel Curve**: `(0, 0) -> (39, 13) -> (87, 65) -> (123, 124) -> (183, 199) -> (255, 255)`
  - **Parametric Curve**: Shadows `-20`, Darks `+30`, Lights `-50`, Highlights `0` (Splits `25 / 50 / 75`).
- **8-Band HSL Color Mix**:
  - **Red**: Hue `-7`, Sat `+4`, Lum `-2`
  - **Orange**: Hue `-22`, Sat `+22`, Lum `+13` (warm earth, terracotta, sandstone)
  - **Yellow**: Hue `-30`, Sat `+94`, Lum `+14` (warm grass highlights and autumn leaves)
  - **Green**: Hue `+17`, Sat `-74`, Lum `-10` (signature Washed Green foliage shifted toward cool sage/emerald and desaturated)
  - **Aqua**: Hue `-1`, Sat `-5`, Lum `0`
  - **Blue**: Hue `-8`, Sat `-19`, Lum `0` (muted, clean daylight sky)
  - **Purple / Magenta**: Purple Sat `+13`, Lum `-10`; Magenta Sat `-3`, Lum `-44`.
- **Global Presence, Split Toning & Calibration**:
  - **Basic Presence**: Vibrance `+5`, Saturation `-27` (global desaturation balanced by the steep RGB S-curves and Orange/Yellow saturation boosts).
  - **Split Toning**: Shadow Hue `52` (warm olive), Shadow Sat `20`, Highlight Sat `0` (zero split-tone color cast in highlights), Balance `+40` (pushes color only into deep shadow crevices).
  - **Camera Calibration**: Red Hue `+46`, Red Sat `+5`, Green Hue `+50`, Green Sat `-25`, Blue Hue `-10`, Blue Sat `-10`.
  - **Effects & Detail**: Grain Amount `15`, Size `30`, Frequency `35`; Post-Crop Vignette `-5` (Midpoint `50`, Feather `50`); Sharpening `40`, Color Noise Reduction `25`.

### I. Kodak Gold 200 (Warm Sunny Nostalgia)
- **Visual Character**: Iconic consumer daylight color negative aesthetic known from Kodak Gold 200 (Kodak Publication E-7022, edge code `GB-200`). Bathed in rich, warm golden-amber sunlight with butter-cream highlight roll-off and lifted matte film shadows. Sunlit grass and foliage shift toward warm yellow-green and olive (rather than Portra's cool cyan-green). Blue skies shift toward soft, desaturated turquoise and cyan-blue. Skin tones render with radiant golden-peach warmth, backed by distinct organic grain (Print Grain Index 44).
- **Base Profile**: **Adobe Standard** on Bayer RAW (Sony ARW) or **Camera Standard**. Avoid Adobe Color, which over-saturates purple/blue channels.
- **Light & Basic Tone**:
  - **Exposure**: `+0.20 to +0.35 EV` (Kodak Gold thrives when exposed generously, suppressing shadow grain).
  - **Contrast**: `-5 to -10` (keeps digital contrast soft so the analog tone curve controls punch).
  - **Highlights**: `-25 to -35` (recovers highlight texture and rolls off into warm creamy daylight).
  - **Shadows**: `+15 to +25` (opens up dark areas in film shadows).
  - **Whites**: `-10 to -16` (smooth highlight ceiling, prevents harsh specular clipping).
  - **Blacks**: `+14 to +18` (lifts the darkest floor to match unexposed film base fog $D_{\min}$).
- **White Balance & Global Color**:
  - **Temperature**: `+6 to +9` (`+350K to +550K` warmer than As Shot daylight) for rich golden warmth.
  - **Tint**: `+2 to +4` toward magenta (balances scanner green shadow bias).
  - **Vibrance**: `+12 to +15`, **Saturation**: `+2 to +4`.
- **Tone Curve & Per-Channel RGB Curves**:
  - **Master Curve**: `(0, 16) -> (32, 28) -> (64, 58) -> (128, 126) -> (192, 198) -> (235, 238) -> (255, 246)` (lifted matte toe, punchy midtones, soft rolled shoulder).
  - **Red Channel Curve**: `(0, 0) -> (64, 62) -> (128, 130) -> (192, 196) -> (255, 252)` (adds warm midtone glow to skin and sand).
  - **Green Channel Curve**: `(0, 0) -> (64, 64) -> (128, 127) -> (192, 192) -> (255, 253)` (neutral gamma tracking).
  - **Blue Channel Curve**: `(0, 12) -> (64, 60) -> (128, 118) -> (192, 178) -> (255, 236)` (suppresses blue in highlights and midtones for rich golden sunlight, lifts shadow toe).
- **8-Band HSL Color Mix**:
  - **Red**: Hue `-4`, Sat `+12`, Lum `-2` (rich poppy red, natural warmth).
  - **Orange**: Hue `+4`, Sat `+10`, Lum `+8` (radiant golden-peach skin, zero sunburn).
  - **Yellow**: Hue `-14`, Sat `+22`, Lum `+6` (shifts lemon yellow toward sunflower amber).
  - **Green**: Hue `+18`, Sat `-24`, Lum `-6` (shifts digital grass toward warm olive and yellow-green).
  - **Aqua**: Hue `-12`, Sat `-10`, Lum `+4` (warm turquoise coastal water).
  - **Blue**: Hue `-16`, Sat `-18`, Lum `-8` (desaturates harsh digital cobalt, shifts toward cyan-blue).
  - **Purple / Magenta**: Purple Hue `-10`, Sat `-25`, Lum `0`; Magenta Hue `-8`, Sat `-20`, Lum `0`.
- **Color Grading (Split Toning)**:
  - **Shadows**: Hue `210°` (balanced slate-teal), Sat `8`, Lum `+2` (subtle scanner inversion complement).
  - **Midtones**: Hue `42°` (warm honey amber), Sat `10`, Lum `0`.
  - **Highlights**: Hue `48°` (sunlit Kodak cream), Sat `16`, Lum `-2`.
  - **Blending**: `74`, **Balance**: `+12` (biases warmth into upper midtones and highlights).
- **Camera Calibration**:
  - **Shadow Tint**: `+3` (magenta-warm toe).
  - **Red Primary**: Hue `-8`, Sat `+14` (warm skin tone foundation).
  - **Green Primary**: Hue `+24`, Sat `-6` (shifts greens toward warm analog yellow-green).
  - **Blue Primary**: Hue `-12`, Sat `+12` (turquoise sky shift, rich color separation).
- **Effects & Detail**:
  - **Texture**: `-4`, **Clarity**: `-8` (soft analog edge transition, gentle highlight glow).
  - **Dehaze**: `+4` (retains dye density).
  - **Vignette**: `-12` (Midpoint `45`, Feather `60`, Roundness `0`).
  - **Grain**: Amount `32`, Size `30`, Roughness `54` (models Print Grain Index 44 dye cloud clumping).
  - **Sharpening**: Amount `28`, Radius `1.0`, Detail `22`, **Masking `55`** (sharpens structural edges only; leaves skies and skin smooth).

### J. CineStill 800T (Night Tungsten & Red Halation)
- **Visual Character**: CineStill 800T (Kodak Vision3 500T 5219 motion picture emulsion cross-processed in C-41 chemistry with remjet anti-halation carbon backing stripped). Renowned for its moody cinematic night aesthetic, cool slate-cyan/teal ambient shadows (3200K tungsten balance), warm glowing incandescent filaments and sodium streetlights, lifted airy matte shadow toe, gentle highlight compression, organic motion picture grain (RMS granularity 9 to 10), and its signature glowing scarlet-red/orange optical halation around specular light sources.
- **Base Profile**: **Adobe Standard** on Bayer RAW (Sony ARW) or **Camera Standard**. Avoid Adobe Color, which pushes unnatural blue/purple saturation in dark scenes.
- **Light & Basic Tone**:
  - **Exposure**: `+0.25 to +0.45 EV` (CineStill thrives on generous exposure; prevents shadow murk and harsh noise).
  - **Contrast**: `-8 to -12` (gentle digital base contrast; allows S-curve and CD-4 cross-processing contrast to take over).
  - **Highlights**: `-35 to -45` (preserves highlight texture around bright streetlamps and neon signs; smooth analog roll-off).
  - **Shadows**: `+20 to +28` (opens low-key shadows, revealing rich cinematic atmosphere without digital noise clumping).
  - **Whites**: `-14 to -20` (prevents harsh digital clipping in light fixtures).
  - **Blacks**: `+12 to +18` (lifts the deepest black point to match film base fog D-min and lifted cinema toe).
- **White Balance & Global Color**:
  - **Night Street & Tungsten Interior**: Temperature `-18 to -26` (`3200K to 3800K`, or `~ -1200K to -1800K` cooler than standard daylight) to establish the authentic tungsten film look with cool slate-cyan ambient shadows and warm golden light sources. Tint `+8 to +14` toward magenta to counter scanner green cast and balance mercury vapor lights.
  - **Daylight Conversion**: Temperature `-4 to -8` with Wratten 85 orange warming or Tint `+4 to +8`.
  - **Vibrance**: `+14 to +18`, **Saturation**: `-6 to -10` (cinema color density with restrained digital saturation).
- **Tone Curve & Per-Channel RGB Curves**:
  - **Master RGB Curve**: `(0, 14) -> (32, 26) -> (64, 56) -> (128, 126) -> (192, 196) -> (240, 240) -> (255, 248)` (lifted matte toe, smooth midtones, soft rolled highlight shoulder).
  - **Red Channel Curve**: `(0, 0) -> (64, 58) -> (128, 124) -> (192, 196) -> (255, 255)` (subtle red compression in shadows for cool cyan cast; slight boost in specular highlights for halation bloom).
  - **Green Channel Curve**: `(0, 0) -> (64, 62) -> (128, 126) -> (192, 192) -> (255, 252)` (natural cinematic gamma tracking).
  - **Blue Channel Curve**: `(0, 16) -> (64, 72) -> (128, 132) -> (192, 186) -> (255, 240)` (lifts blue in shadows and midtones for atmospheric teal/slate ambient night glow; rolls off in highlights to let warm incandescent streetlights glow golden-orange).
- **8-Band HSL Color Mix**:
  - **Red**: Hue `+6`, Sat `+18`, Lum `-4` (deep scarlet halation and neon sign saturation).
  - **Orange**: Hue `+8`, Sat `+14`, Lum `+6` (warm glowing sodium-vapor streetlights, incandescent bulbs, warm skin tones).
  - **Yellow**: Hue `-12`, Sat `+8`, Lum `+4` (shifts greenish streetlights toward warm amber).
  - **Green**: Hue `+22`, Sat `-35`, Lum `-8` (mutes modern artificial LED greenery, shifting toward muted cinema olive).
  - **Aqua**: Hue `-8`, Sat `+16`, Lum `-4` (rich cinematic teal tones in wet asphalt and ambient night reflections).
  - **Blue**: Hue `+4`, Sat `+8`, Lum `-10` (deep moody midnight sky and cyan-slate shadow architecture).
  - **Purple / Magenta**: Purple Hue `-12`, Sat `-30`, Lum `-6`; Magenta Hue `-16`, Sat `-20`, Lum `0` (cleans up chromatic aberration and harsh purple neon fringes).
- **Color Grading (Split Toning)**:
  - **Shadows**: Hue `196°` (cool slate-cyan/teal), Sat `14`, Lum `+2` (creates signature CineStill cool night shadow tone).
  - **Midtones**: Hue `48°` (subtle warm amber), Sat `6`, Lum `0` (preserves human skin fidelity and street ambiance).
  - **Highlights**: Hue `36°` (warm golden incandescent), Sat `12`, Lum `-2` (soft highlight warmth around light bulbs).
  - **Blending**: `68`, **Balance**: `-16` (biases the slate-cyan color cast deep into ambient shadows while keeping practical highlights clean).
- **Camera Calibration**:
  - **Shadow Tint**: `+8` (magenta shift in deep blacks, countering greenish scanner flare).
  - **Red Primary**: Hue `+12`, Sat `+16` (shifts red toward rich cinema scarlet, enhancing halation punch).
  - **Green Primary**: Hue `+26`, Sat `-8` (shifts greens toward teal-cyan and suppresses digital grass spike).
  - **Blue Primary**: Hue `-18`, Sat `+10` (signature cinema cyan-teal color separation).
- **Effects & Detail**:
  - **Texture**: `-12`, **Clarity**: `-16` (softens harsh modern digital sensor micro-contrast and simulates optical film diffusion).
  - **Dehaze**: `+6` (restores deep film dye density across shadows and midtones).
  - **Vignette**: `-10` (Midpoint `40`, Feather `65`, Roundness `0`).
  - **Grain**: Amount `36`, Size `32`, Roughness `56` (authentic Vision3 500T RMS granularity and dye cloud clumping).
  - **Sharpening**: Amount `32`, Radius `1.0`, Detail `24`, **Masking `60`** (restores edge definition to physical architecture and eyes while keeping the diffused glow smooth).
- **Halation Emulation Technique**:
  - **Premium (Lightroom Mobile Masking)**: Place a **Radial Gradient Mask** centered on practical light sources (streetlamps, neon tubes, car headlights). Set Feather `85 to 95`. Inside the mask: **Exposure `+0.30 to +0.60 EV`**, **Highlights `+20 to +40`**, **Temperature `+30 to +60` (extreme warm amber)**, **Tint `+40 to +75` (intense magenta/scarlet)**, **Clarity `-40 to -70`**, **Dehaze `-25 to -45`**, and **Texture `-20 to -35`**. This produces the exact blooming red/orange halo that characterizes remjet-free film.
  - **Free-Tier Global Workaround**: Use global **Clarity `-16`** and **Texture `-12`** combined with **Calibration Red Primary Hue `+12`, Sat `+16`**, **Color Mix Red Sat `+18`**, and **Detail Masking `60`**. The negative clarity creates optical bloom around all high-contrast specular borders, while the calibration and red saturation ensure that blooming light bleeds with warm scarlet/orange tones rather than cold digital white.

---

## 4. Lightroom Mobile Free-Tier fallbacks (when Masking & Point Color are locked)

If the user is on **Lightroom Mobile Free** (where **Masking** and **Point Color** require a Premium subscription), never leave a gap unaddressed. Provide the exact **Free-Tier Global Workaround** to capture as much of the local lighting effect as possible:

| Premium Local Masking Effect | Lightroom Mobile Free-Tier Global Workaround |
| :--- | :--- |
| **Sky Darkening / Sky Color Shift** *(Sky Mask)* | In **Color Mix (HSL)**, lower **Blue Luminance `-20 to -45`** and **Aqua Luminance `-15 to -35`**, increase **Blue Saturation `+5 to +15`**, and use **Tone Curve -> Parametric Highlights `-15 to -30`** with the Upper Split slider pushed to `75 to 80`. |
| **Subject Skin Brightening / Pop** *(Subject Mask)* | In **Color Mix (HSL)**, raise **Orange Luminance `+10 to +22`** and **Red Luminance `+6 to +14`**, while lowering **Green/Yellow/Blue Luminance `-15 to -35`** so the warm subject separates naturally from cooler/foliage backgrounds. |
| **Directional Edge Burn / Spotlight** *(Radial / Linear Gradient Mask)* | In **Effects -> Vignette**, set **Amount `-20 to -45`**, **Midpoint `25 to 40`** (reaches further toward the center), **Feather `75 to 90`** (invisible ultra-soft transition), **Roundness `-15 to +15`**, and **Highlights `20 to 50`** (preserves bright sky/light sources inside the vignette). |
| **Optical Bloom / Halation Glow on Practical Lights** *(Radial Mask with negative Dehaze)* | Lower global **Texture `-10 to -18`** and **Clarity `-12 to -22`** to create soft highlight bloom, then restore crisp edge definition using **Detail -> Sharpening `+45 to +65`** with **Masking `50 to 70`** (so only high-contrast edges sharpen while highlights stay dreamy). |
