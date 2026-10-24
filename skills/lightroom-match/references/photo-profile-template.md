# Photo & Editor Profile Template & Maintenance Rules

Reference for reading, creating, and updating an optional persistent photo and Lightroom Mobile profile so [`lightroom-match`](../SKILL.md) remembers the user's camera system, RAW format, Lightroom Mobile subscription tier, and saved look recipes across sessions without re-asking settled questions.

## Discovery order

1. **Project-scoped profile**: `.agents/photo-profile.md` in the current workspace (useful for client shoots, specific travel albums, or brand style folders).
2. **User-global profile**: `~/.agents/photo-profile.md` (default home for personal camera gear and Lightroom Mobile preferences across CLI and IDE agents).
3. **Chat environment fallback**: in Claude Desktop or web chat where local dotfiles are unavailable, read built-in platform memory or project instructions, and offer a copyable Markdown block when the user asks to save their photo profile.

## Maintenance rules

1. **Zero-config by default**: Never block a Lightroom Mobile replication because no profile file exists. Gather only the context needed for the current photo pair via Step 1.
2. **Opt-in writes only**: Create or update `.agents/photo-profile.md` or `~/.agents/photo-profile.md` only after delivering the Lightroom Mobile recipe and confirming the user wants to save their camera baseline or custom preset log entry.
3. **Keep entries compact, durable, and privacy-safe**: Store only durable facts that affect future Lightroom Mobile recipes (camera body/phone model, default file format in LR Mobile, Lightroom Mobile Free vs. Premium tier, preferred base profiles, skin-tone or grain preferences, and past calibrated preset recipes). Never store private GPS coordinates, personal faces/identifiers, or cloud account credentials.

## Recommended schema (`photo-profile.md`)

```markdown
# Photo & Lightroom Mobile Profile

## Primary Camera Bodies & Sensor Systems
- **Main Camera / Phone**: [e.g., Sony A7 IV / Fujifilm X-T5 / Canon R6 II / iPhone 16 Pro]
- **Default File Format in LR Mobile**: [e.g., Uncompressed/Compressed RAW (.ARW / .RAF / .CR3) / Apple ProRAW (.DNG) / 8-bit HEIC or JPEG]
- **Common Lenses & Focal Lengths**: [e.g., 35mm f/1.4 GM, 24-70mm f/2.8, iPhone 24mm 1x main camera]
- **Sensor Calibration Notes**: [e.g., Sony A7 IV needs +3 to +6 Magenta Tint offset in shade; iPhone ProRAW needs Profile Amount reduced to 40–50% before grading]

## Lightroom Mobile Setup
- **Subscription Tier**: [e.g., Lightroom Mobile Premium (Masking, Point Color, Cloud RAW unlocked) / Lightroom Mobile Free (Global sliders, Tone Curve, HSL Color Mix, Color Grading only)]
- **Device Screen & True Tone**: [e.g., iPhone OLED with True Tone & Night Shift OFF during editing]
- **Preferred Base Profile**: [e.g., Adobe Color / Adobe Neutral / Camera Classic Chrome / Apple ProRAW at 45%]

## Style & Skin-Tone Guardrails
- **Skin-Tone Preference**: [e.g., Natural warm golden skin (Orange Hue -2 to +4, Sat -8 to -4, Lum +5 to +12); avoid overly orange or magenta skin casts]
- **Grain & Texture Baseline**: [e.g., Subtle 35mm film grain (Grain 12–18, Size 25, Roughness 50) vs. clean zero-grain digital look]
- **Black Point Preference**: [e.g., Slight matte film fade (RGB Black Point lifted to 4–7%) vs. deep true blacks (0%)]

## Saved Reference Look & Preset Log
| Date | Look / Preset Name | Source Camera & Format | Key Signature (Curve + HSL + Grading) | Final Calibrated Notes (Pass 2 Delta) |
| :--- | :--- | :--- | :--- | :--- |
| YYYY-MM-DD | [e.g., Portra 400 Warm Street] | [Sony ARW / iPhone ProRAW] | [Adobe Neutral; RGB lifted black (0%, 6%); Green Hue +25, Sat -45; Shadows 215° Sat 12, Highlights 42° Sat 16] | [Needed -12 Highlights and +4 Orange Lum on Pass 2 to hit 98% match] |
```
