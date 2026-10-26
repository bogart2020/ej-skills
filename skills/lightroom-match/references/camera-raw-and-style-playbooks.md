# Camera RAW Systems & Style Replication Playbooks

Specialized camera sensor color-science neutralization rules, file-format headroom bounds, look-archetype recipes, and Lightroom Mobile Free-tier global workarounds referenced in [`SKILL.md`](../SKILL.md).

## 1. Camera RAW sensor baselines & input profile neutralization

Every camera manufacturer encodes a distinct `ColorMatrix1/2`, `ForwardMatrix1/2`, `BaselineExposure`, and default `ProfileToneCurve` inside its RAW files (Adobe DNG Specification v1.7.1.0). Applying the exact same Lightroom Mobile slider values to a Sony `.ARW`, a Canon `.CR3`, an iPhone `.DNG` (Apple ProRAW), and a baked `.JPEG` produces visibly different results. Before transferring the reference look from Photo 2, neutralize Photo 1's sensor baseline:

| Camera System / File Format | Native Sensor & Color Matrix Characteristics in LR Mobile | Pre-Grade Neutralization Adjustment |
| :--- | :--- | :--- |
| **Sony Alpha (`ARW`)** *(A7 III / A7 IV / A7R V / A7C II / ZV-E1 / A6700)* | Older Bionz X sensors (A7 III, A6400) exhibit a slight green-yellow cast in shadows and cooler magenta-shifted highlights on *Adobe Color*, with a steep default shadow drop. Newer Bionz XR bodies (A7 IV, A7R V, A7C II) have cleaner skin tones but still render foliage cooler/greener than Canon. | Start on **Adobe Standard** or **Adobe Neutral** (or **Camera Standard** if available). For older Bionz X bodies, add **Tint `+4 to +8` (toward Magenta)**, shift **Color Mix -> Orange Hue `-3 to -6`** (warmer skin), and **Yellow Hue `-8 to -12`** before applying the reference grade. |
| **Canon EOS (`CR2` / `CR3`)** *(R5 / R6 II / R8 / R50 / 5D IV)* | Strong red-orange skin-tone bias and punchier default midtone contrast; reds and oranges saturate rapidly when increasing Contrast or Vibrance, and highlights roll off warmly. | Start on **Adobe Neutral** (for soft/film looks) or **Adobe Standard**. Pull **Color Mix -> Red Hue `+4 to +8`**, **Orange Saturation `-6 to -12`**, and **Shadows `+10 to +18`** to prevent skin from turning overly tangerine when adding warm reference grading. |
| **Nikon Z / F (`NEF`)** *(Z8 / Z9 / Z6 III / Zf / D850)* | Neutral-to-warm yellow-green rendering with high linear shadow dynamic range (ISO-invariant Sony-fabricated sensors with Nikon color matrices) and slightly cooler blues. | Start on **Adobe Standard** or **Camera Flat / Neutral**. Shift **Yellow Hue `+5 to +10`** if foliage looks too chartreuse, and use **Blacks** rather than heavy **Contrast** to set the shadow floor. |
| **Fujifilm X / GFX (`RAF`)** *(X100VI / X-T5 / X-Pro3 / X-S20 / GFX100 II)* | X-Trans CFA demosaicing has high color fidelity and film-like blue/green separation. If the user shot with an in-camera Film Simulation, LR Mobile defaults to *Adobe Color* unless switched to **Camera Matching**. | In **Profiles -> Browse -> Camera Matching**, pick the closest Fujifilm base (**Camera Classic Chrome** for documentary/muted looks, **Camera Classic Neg.** for high-contrast street, **Camera Nostalgic Neg.** for warm amber highlights, **Camera Astia/Provia** for clean portraits). In **Detail**, keep Sharpening **Detail $\le 25$** and **Masking $\ge 40$** to avoid X-Trans "worm" artifacts. |
| **Leica / Panasonic Lumix / OM System / Ricoh GR (`DNG` / `RW2` / `ORF`)** | Native DNG cameras (Leica Q3/M11, Ricoh GR III/IIIx) embed vendor profiles with high micro-contrast and deep shadow falloff; Ricoh GR DNGs often underexpose highlights by `-0.3 to -0.7 EV` to protect sky detail. | Check `BaselineExposure` headroom first: lift **Exposure `+0.25 to +0.50 EV`** and **Shadows `+15 to +25`** on Ricoh GR / Leica DNGs before matching midtone luminance to Photo 2. |
| **Apple ProRAW (`DNG`)** *(iPhone 12 Pro through iPhone 16 Pro / Max)* | **Critical computational RAW behavior**: Apple ProRAW is an already-demosaiced, multi-frame merged 12-bit/16-bit linear DNG carrying an embedded **`ProfileGainTableMap`** (semantic local tone mapping that brightens faces, compresses skies, and sharpens edges). Leaving the **Apple ProRAW** profile at `100%` fights film curves and causes HDR haloing when pulling Highlights down. | 1. Open **Profiles -> Apple ProRAW** and drag the **Profile Amount slider down to `30%–55%`** (or switch Profile to **Adobe Color / Adobe Neutral**) to flatten Apple's baked Smart HDR local tone map.<br>2. Set **Detail -> Sharpening Amount to `0–15`** (ProRAW already has baked multi-frame edge sharpening).<br>3. Compensate for mobile highlight clipping by using the **Point Curve White Point `(100%, 92%–96%)`** rather than pushing the `Highlights` slider to `-100` (which creates gray plastic skin/skies on ProRAW). |
| **Samsung Expert RAW / Google Pixel RAW (`DNG`)** | Multi-frame computational DNGs with aggressive shadow noise reduction and vivid blue/green saturation matrices; highlights clip abruptly if over-exposed at capture. | Switch Profile from the default embedded profile to **Adobe Standard** or **Adobe Neutral** to remove excessive cyan-sky and neon-green boosts; reduce **Vibrance `-8 to -15`** before applying the target look. |
| **8-bit Baked JPEG / HEIC / PNG** *(Camera JPEG, downloaded image, or phone non-RAW)* | Gamma-encoded 8-bit ($256$ levels per channel) with white balance, tone curve, and sharpening permanently baked in; clipped `255` whites and `0` blacks contain zero recoverable detail. **Temp** slider is relative (`-100 to +100`) instead of Kelvin (`2000K–50000K`). | 1. Report **Temp** on the **`-100 to +100` relative scale** (never Kelvin).<br>2. Keep global **Temp / Tint within `±30`**, **Highlights / Shadows within `±65`**, and **HSL Luminance within `±40`** to prevent 8-bit banding and posterization.<br>3. Use the **Tone Curve** and **Color Grading wheels** (which operate smoothly across 8-bit luma ranges) to reshape contrast and color casts instead of extreme White Balance or Dehaze sliders. |


**Starting Profile for Photo 1 (Step 2):**

- **Apple ProRAW (`.DNG`)**: keep **Apple ProRAW** selected and lower **Profile Amount to `30%–55%`** (or switch to **Adobe Neutral / Adobe Color**) so Apple's baked `ProfileGainTableMap` Smart HDR tone map does not fight the reference Tone Curve.
- **Sony (`ARW`) / Canon (`CR3`) / Nikon (`NEF`) / Leica & Ricoh (`DNG`)**: **Adobe Neutral** (low-contrast film/matte references), **Adobe Standard** (balanced natural grades), **Adobe Color** (punchy vibrant references), or **Adobe Monochrome** (B&W), plus the brand pre-offsets in the table above.
- **Fujifilm (`RAF`)**: the closest **Camera Matching** profile (**Camera Classic Chrome**, **Camera Classic Neg.**, **Camera Nostalgic Neg.**, **Camera Astia**, or **Camera Acros**) when available on RAW, or **Adobe Standard** with matching HSL offsets.
- **8-bit JPEG / HEIC**: White Balance `Temp` uses the relative **`-100 to +100`** scale; keep global sliders within the anti-banding limits in the table above. Adobe Raw profiles (Adobe Neutral, Standard, Color) are not offered for JPEG/HEIC; start from the Color profile (or Monochrome for black and white) or a creative profile.

---

## 2. Quantitative 5-zone tonal & 8-band chromatic decomposition

When code execution (`python3` with `PIL` / `numpy`) is available in the active environment and the image files are accessible on disk, inspect the source and reference images quantitatively before writing slider values:

1. **Compute luminance percentiles** ($L = 0.2126 R + 0.7152 G + 0.0722 B$ in sRGB):
   - **Black Floor ($P_1, P_5$)**: If Reference $P_1 > 12/255$ ($>5\%$), the reference has a **lifted matte black point** `(0%, 5%–12%)` on the Master RGB Point Curve.
   - **Shadow Density ($P_{10}, P_{25}$)**: Maps to **Shadows** slider and Point Curve `(25%, Y%)` anchor.
   - **Midtone / Skin Anchor ($P_{50}$)**: Maps to **Exposure ($\text{EV}$)** and Point Curve `(50%, Y%)` anchor. Each $\pm 1.00\text{ EV}$ shift corresponds to roughly a $2\times$ linear luminance factor ($\approx \pm 20\text{ to }25\%$ in midtone sRGB code value).
   - **Highlight Shoulder ($P_{75}, P_{90}$)**: Maps to **Highlights** slider and Point Curve `(75%, Y%)` anchor.
   - **White Ceiling ($P_{95}, P_{99}$)**: If Reference $P_{99} < 242/255$ ($<95\%$), the reference has **compressed/rolled-off creamy whites** `(100%, 88%–95%)` on the Master RGB Point Curve.
2. **Compute per-zone chromaticity cast ($\Delta R, \Delta G, \Delta B$ in Shadows, Midtones, Highlights)**:
   - Compare mean $(R - G)$ and $(B - \frac{R+G}{2})$ separately across dark pixels ($L \in [5\%, 30\%]$), midtones ($L \in [30\%, 70\%]$), and bright pixels ($L \in [70\%, 95\%]$).
   - Translate shadow and highlight RGB offsets into **Color Grading wheel Hue ($0^\circ\text{–}360^\circ$) and Saturation ($0\text{–}100$)**:
     - $0^\circ$ = Red | $30^\circ$ = Warm Orange | $45^\circ\text{–}55^\circ$ = Golden Amber/Yellow | $120^\circ$ = Green | $180^\circ\text{–}195^\circ$ = Cyan/Teal | $210^\circ\text{–}225^\circ$ = Cool Steel Blue | $240^\circ$ = Deep Blue | $300^\circ\text{–}330^\circ$ = Magenta/Rose.

---

## 3. Canonical style & look archetypes in Lightroom Mobile

Use these calibrated signatures to anchor specific photographic looks when Photo 2 exhibits one of these classic aesthetics, adjusting every number to Photo 1's actual starting histogram:

### A. Warm Analog Film (Kodak Portra 400 / Fuji Pro 400H Aesthetic)
- **Tonal Signature**: Soft lifted blacks `(0%, 5%–8%)`, gentle shadow lift `(25%, 28%–32%)`, slightly compressed creamy highlights `(100%, 93%–96%)`, negative Contrast (`-10 to -20`), positive Shadows (`+20 to +40`), negative Highlights (`-25 to -50`).
- **Per-Channel RGB Curves**: Subtle warm S-curve in **Red** (pull darks down `-2%`, lift upper midtones `+2%`), gentle lift in **Green** midtones (`+1% to +2%`), and inverse tilt in **Blue** (lift deep shadows `(0%, 3%)`, pull highlights down `(100%, 95%)` for creamy warm skies/highlights).
- **HSL Color Mix**:
  - **Orange**: Hue `-4 to +4`, Sat `-5 to -12`, Lum `+6 to +15` (luminous, natural skin).
  - **Yellow**: Hue `-15 to -25` (shift toward warm gold), Sat `-15 to -30`, Lum `+5 to +10`.
  - **Green**: Hue `+15 to +35` (toward emerald/cyan-green, away from neon yellow-green), Sat `-30 to -55`, Lum `-10 to +5`.
  - **Aqua / Blue**: Blue Hue `-10 to -22` (toward cyan/teal sky), Sat `-15 to -30`, Lum `-5 to -18`.
- **Effects**: Texture `-5 to -12`, Clarity `-5 to -10`, Dehaze `-3 to +5`, Grain Amount `15–24`, Size `25–30`, Roughness `50–60`.

### B. Moody Dark / Desaturated Forest, Street & Automotive
- **Tonal Signature**: Deep crushed midtones with a matte black floor: RGB Curve `(0%, 7%–11%)`, dipped shadow anchor `(25%, 18%–22%)`, controlled midtones `(50%, 44%–48%)`, muted white ceiling `(100%, 86%–92%)`. Exposure `-0.30 to -0.70 EV`, Highlights `-40 to -75`, Shadows `+15 to +35`, Whites `-20 to -45`, Blacks `-15 to -35`.
- **HSL Color Mix**:
  - Desaturate **Yellow (`-50 to -80`)**, **Green (`-60 to -90`)**, **Aqua (`-40 to -70`)**, **Blue (`-45 to -75`)**, **Purple/Magenta (`-60 to -85`)**, while keeping **Red** and **Orange** selectively intact (`Sat -10 to +10`, `Lum +4 to +12`) so skin or tail-lights/warm practicals pop against the monochrome-leaning environment.
- **Color Grading**: Shadows Hue `205°–225°` (Cool Slate/Teal), Sat `10–18`, Lum `-10 to -20`; Midtones Hue `35°–45°` (Warm Bronze), Sat `6–12`; Highlights Hue `40°–55°` (Muted Warm Cream), Sat `8–15`; Blending `60–75`, Balance `-15 to -30`.
- **Local Masking**: **Subject Mask** (`Exposure +0.25 to +0.45 EV`, `Clarity +10`) + **Inverted Radial Gradient** or **Linear Gradient** on foreground (`Exposure -0.40 to -0.80 EV`, `Dehaze +10`).

### C. Bright, Airy & Editorial Clean (Wedding, Lifestyle, Interior)
- **Tonal Signature**: High-key luminance with open shadows and luminous skin: Exposure `+0.35 to +0.85 EV`, Contrast `-15 to -30`, Highlights `-30 to -55`, Shadows `+35 to +65`, Whites `+15 to +30`, Blacks `+15 to +35`. RGB Curve lifts `(0%, 3%–5%)`, `(25%, 30%–35%)`, `(50%, 56%–60%)`, `(75%, 80%–83%)`, `(100%, 98%–100%)`.
- **HSL Color Mix**:
  - **Orange**: Hue `+2 to +6`, Sat `-10 to -18`, Lum `+12 to +22` (bright porcelain/editorial skin).
  - **Yellow & Green**: Yellow Sat `-35 to -55`, Lum `+15 to +25`; Green Hue `+10 to +25`, Sat `-45 to -70`, Lum `+15 to +30` (light sage foliage).
  - **Blue**: Hue `-8 to -15`, Sat `-20 to -35`, Lum `+10 to +25` (pastel airy sky).

### D. Cinema Teal & Orange / Night Neon / Cyberpunk
- **Tonal Signature**: Strong S-curve contrast (`(0%, 4%)`, `(25%, 19%)`, `(50%, 50%)`, `(75%, 82%)`, `(100%, 97%)`), Highlights `-35 to -60` (recovering neon sign bloom), Blacks `-10 to -25`.
- **Color & HSL**: Cooler White Balance (`Temp 3600K–4400K` or `-15 to -30`, `Tint +8 to +22`). Shift **Red Hue `+15 to +30`** (toward orange), **Yellow Hue `-25 to -45`** (toward orange), **Green Hue `+60 to +90`** (toward teal), **Blue Hue `-20 to -35`** (toward cyan/electric blue), **Purple/Magenta Sat `+15 to +35`**.
- **Color Grading**: Shadows Hue `195°–215°` (Deep Teal/Cyan), Sat `22–38`; Highlights Hue `28°–42°` (Warm Amber/Orange), Sat `20–35`; Blending `45–60`.
- **Effects**: Clarity `-10 to -20` combined with Dehaze `-10 to -18` (or a Radial Mask around light sources with `Dehaze -25`, `Texture -20`) to replicate **optical halation / bloom filter (CineBloom / Black Pro-Mist)** glow.

### E. High-Contrast Monochrome / Classic B&W Film (Ilford HP5 / Kodak Tri-X)
- **Profile**: Switch to **B&W -> Adobe Monochrome** or **B&W 01 / Camera Acros**.
- **B&W Color Mix (Luminance Channel Weights)**: Instead of HSL, adjust the 8 **B&W Mix** sliders to control how original scene colors map to gray tones:
  - **Orange `+15 to +30`** and **Red `+10 to +20`** (brighten skin tones and blemishes).
  - **Blue `-35 to -65`** and **Aqua `-25 to -45`** (dramatic dark skies, replicating a physical Red/Orange contrast filter).
  - **Green `-15 to +20`** and **Yellow `+15 to +35`** (separate foliage from shadows).
- **Tone Curve & Grain**: Classic film toe and shoulder (`(0%, 5%)`, `(20%, 14%)`, `(50%, 52%)`, `(80%, 86%)`, `(100%, 96%)`), Grain Amount `25–38`, Size `30–40`, Roughness `55–65`.

---

## 4. Lightroom Mobile Free-Tier fallbacks (when Masking & Point Color are locked)

If the user is on **Lightroom Mobile Free** (where **Masking** and **Point Color** require a Premium subscription), never leave a gap unaddressed. Provide the exact **Free-Tier Global Workaround** to capture as much of the local lighting effect as possible:

| Premium Local Masking Effect | Lightroom Mobile Free-Tier Global Workaround |
| :--- | :--- |
| **Sky Darkening / Sky Color Shift** *(Sky Mask)* | In **Color Mix (HSL)**, lower **Blue Luminance `-20 to -45`** and **Aqua Luminance `-15 to -35`**, increase **Blue Saturation `+5 to +15`**, and use **Tone Curve -> Parametric Highlights `-15 to -30`** with the Upper Split slider pushed to `75–80`. |
| **Subject Skin Brightening / Pop** *(Subject Mask)* | In **Color Mix (HSL)**, raise **Orange Luminance `+10 to +22`** and **Red Luminance `+6 to +14`**, while lowering **Green/Yellow/Blue Luminance `-15 to -35`** so the warm subject separates naturally from cooler/foliage backgrounds. |
| **Directional Edge Burn / Spotlight** *(Radial / Linear Gradient Mask)* | In **Effects -> Vignette**, set **Amount `-20 to -45`**, **Midpoint `25–40`** (reaches further toward the center), **Feather `75–90`** (invisible ultra-soft transition), **Roundness `-15 to +15`**, and **Highlights `20–50`** (preserves bright sky/light sources inside the vignette). |
| **Optical Bloom / Halation Glow on Practical Lights** *(Radial Mask with negative Dehaze)* | Lower global **Texture `-10 to -18`** and **Clarity `-12 to -22`** to create soft highlight bloom, then restore crisp edge definition using **Detail -> Sharpening `+45 to +65`** with **Masking `50–70`** (so only high-contrast edges sharpen while highlights stay dreamy). |
