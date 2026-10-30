#!/usr/bin/env python3
"""Reference-match engine for lightroom-match.

Commands (run with `python3 -I lrmatch.py <command> --help`):
  fetch    download reference images from a web page the user named
  sheet    contact sheet of a folder, to pick the frames that carry the look
  measure  measure the look of reference images into a JSON target
  fit      tune one shared preset so the source photos match the target
  grade    apply a preset to photos, write previews and before/after sheets
  xmp      write a Lightroom .xmp preset from a preset JSON

Needs numpy and pillow; rawpy is optional (camera RAW decode).
Rendering approximates Lightroom sliders; it is a preview, not Lightroom.
"""
import argparse, html, io, json, math, os, re, subprocess, urllib.parse, urllib.request, uuid

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

BANDS = {"red": 0, "orange": 30, "yellow": 60, "green": 120, "aqua": 180, "blue": 225, "purple": 270, "magenta": 315}
WIDTH = {"red": 30, "orange": 30, "yellow": 35, "green": 55, "aqua": 45, "blue": 45, "purple": 40, "magenta": 40}

DEFAULT = {
    "exposure": "auto", "target_p50": 145, "contrast": 0, "highlights": 0, "shadows": 0, "whites": 0, "blacks": 0,
    "temp": 0, "tint": 0, "vibrance": 0, "saturation": 0,
    "curve": [[0, 0], [255, 255]],
    "hsl": {b: [0, 0, 0] for b in BANDS},
    "grade_shadows": [0, 0], "grade_midtones": [0, 0], "grade_highlights": [0, 0], "balance": 0,
    "clarity": 0, "texture": 0, "grain": 0, "dehaze": 0, "vignette": 0,
    "ev_max": None,  # cap for auto Exposure; None = +0.6 when the sky would clip, else +1.5
    "black_p1": None,
    "wb_target": None,  # per-photo white balance: neutral midtones land at [blue-red, green-magenta] like the references
}

# Parameters `fit` may move: search step and hard bounds (Lightroom slider units).
# `fit` also keeps each value within WINDOW of the planned start, so it fine-tunes the plan instead of inventing a new look.
WINDOW = {"grade_shadows.0": 40, "grade_highlights.0": 40, "grade_shadows.1": 10, "grade_highlights.1": 10,
          "grade_midtones.0": 60, "grade_midtones.1": 10, "grain": 25, "vignette": 30,
          "target_p50": 15, "clarity": 15}
FIT_SPACE = {
    "contrast": (10, -60, 60), "highlights": (15, -100, 100), "shadows": (15, -100, 100),
    "whites": (10, -60, 60), "blacks": (15, -100, 60), "temp": (6, -40, 40), "tint": (6, -40, 40),
    "vibrance": (10, -60, 60), "saturation": (10, -80, 60),
    "hsl.orange.0": (8, -40, 40), "hsl.orange.1": (12, -60, 60), "hsl.orange.2": (10, -40, 40),
    "hsl.yellow.0": (10, -60, 60), "hsl.yellow.1": (15, -80, 80), "hsl.yellow.2": (10, -40, 40),
    "hsl.green.0": (10, -60, 60), "hsl.green.1": (15, -90, 60), "hsl.green.2": (10, -40, 40),
    "hsl.blue.0": (8, -40, 40), "hsl.blue.1": (12, -70, 50), "hsl.blue.2": (10, -40, 40),
    "grade_shadows.0": (30, 0, 359), "grade_shadows.1": (6, 0, 40),
    "grade_highlights.0": (30, 0, 359), "grade_highlights.1": (6, 0, 40),
    "clarity": (8, -40, 40), "dehaze": (8, -30, 60), "target_p50": (10, 90, 175),
    "hsl.red.0": (8, -40, 40), "hsl.red.1": (12, -60, 60), "hsl.red.2": (10, -40, 40),
    "hsl.aqua.1": (12, -70, 50), "hsl.aqua.2": (10, -40, 40),
    "grade_midtones.0": (30, 0, 359), "grade_midtones.1": (5, 0, 30), "balance": (15, -60, 60),
    "texture": (8, -50, 40), "vignette": (8, -50, 20), "grain": (6, 0, 40),
}

RAW_EXT = {".arw", ".cr2", ".cr3", ".nef", ".raf", ".rw2", ".orf", ".dng", ".pef", ".srw"}


# ---------- loading ----------

def sniff(path):
    with open(path, "rb") as f:
        head = f.read(12)
    if head[:2] == b"\xff\xd8":
        return "jpeg"  # includes JPEGs renamed .DNG
    if head[4:12] in (b"ftypheic", b"ftypheix", b"ftypmif1"):
        return "heic"
    if os.path.splitext(path)[1].lower() in RAW_EXT:
        return "raw"
    return "other"


def load(path, max_edge=1600):
    """Return (float RGB array 0..1 in display sRGB, decode note). Orientation is applied."""
    kind = sniff(path)
    if kind == "raw":
        try:
            import rawpy
            with rawpy.imread(path) as r:
                rgb = r.postprocess(use_camera_wb=True, half_size=True, output_bps=8)
            im, note = Image.fromarray(rgb), "rawpy (camera white balance)"
        except Exception as e:  # unsupported RAW variant or rawpy missing
            im, note = _sips(path), f"sips fallback ({type(e).__name__}); estimate"
    elif kind == "heic":
        im, note = _sips(path), "sips (HEIC)"
    else:
        im, note = ImageOps.exif_transpose(Image.open(path)).convert("RGB"), f"{kind} (8-bit, baked)"
    im.thumbnail((max_edge, max_edge))
    return np.asarray(im).astype(np.float32) / 255.0, note


def _sips(path):
    out = os.path.join(os.path.dirname(os.path.abspath(path)), "." + os.path.basename(path) + ".sips.jpg")
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "95", "-Z", "3000", path, "--out", out],
                   check=True, capture_output=True)
    return ImageOps.exif_transpose(Image.open(out)).convert("RGB")


# ---------- color helpers ----------

def lum(x):
    return 0.2126 * x[..., 0] + 0.7152 * x[..., 1] + 0.0722 * x[..., 2]


def to_lin(x):
    return np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)


def to_srgb(x):
    x = np.clip(x, 0, None)
    return np.where(x <= 0.0031308, x * 12.92, 1.055 * x ** (1 / 2.4) - 0.055)


def rgb2hsv(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(-1), a.min(-1)
    d = mx - mn + 1e-8
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    s = np.where(mx > 0, (mx - mn) / (mx + 1e-8), 0)
    return h, s, mx


def hsv2rgb(h, s, v):
    h = (h % 360) / 60
    i = np.floor(h).astype(int) % 6
    f = h - np.floor(h)
    p, q, t = v * (1 - s), v * (1 - s * f), v * (1 - s * (1 - f))
    sel = [(v, t, p), (q, v, p), (p, v, t), (p, q, v), (t, p, v), (v, p, q)]
    out = np.zeros(h.shape + (3,), np.float32)
    for k in range(6):
        m = i == k
        for c in range(3):
            out[..., c][m] = sel[k][c][m]
    return out


def hue_rgb(hue):
    return hsv2rgb(np.array([hue], np.float32), np.array([1.0], np.float32), np.array([1.0], np.float32))[0] - 0.5


# ---------- render ----------

def _wb_gains(x, br, gm):
    """RGB gains that move near-neutral midtones to the target blue-red and green-magenta offsets (8-bit units)."""
    a = np.clip(x, 0, 1) * 255
    L = lum(a)
    _, s, _ = rgb2hsv(np.clip(x, 0, 1))
    k = (L > 60) & (L < 200) & (s < 0.25)
    if k.sum() < 500:
        return np.ones(3, np.float32)
    r, g, b = (float(a[..., c][k].mean()) for c in range(3))
    m = (r + g + b) / 3
    g2 = m + 2 * gm / 3
    rb = 2 * (m - gm / 3)
    want = np.array([rb / 2 - br / 2, g2, rb / 2 + br / 2])
    return np.clip(want / np.array([r, g, b]), 0.8, 1.25).astype(np.float32)


def render(src, p, ev=None):
    """Apply preset p to src (0..1 sRGB). Returns (image, exposure_used)."""
    q = {**DEFAULT, **p, "hsl": {**DEFAULT["hsl"], **p.get("hsl", {})}}
    lin = to_lin(src)
    t, m = q["temp"] / 100, q["tint"] / 100
    lin = lin * np.array([1 + 0.30 * t, 1 - 0.25 * m, 1 - 0.30 * t], np.float32)
    if ev is None:
        ev = q["exposure"]
        if ev == "auto":
            target = to_lin(np.float32(q["target_p50"] / 255.0))
            med = float(np.median(lum(lin))) + 1e-4
            p99 = float(np.percentile(lum(src), 99))
            cap = q["ev_max"] if q["ev_max"] is not None else (0.6 if p99 > 240 / 255 else 1.5)
            ev = float(np.clip(math.log2(target / med), -0.6, cap))
    lin = lin * 2 ** ev
    x = np.clip(to_srgb(lin), 0, 1.2)
    if q["wb_target"] is not None:
        x = x * _wb_gains(x, *q["wb_target"])

    if q["dehaze"]:  # remove (or add) a soft haze veil estimated from the local dark channel
        veil = np.asarray(Image.fromarray((np.clip(x.min(-1), 0, 1) * 255).astype(np.uint8)).filter(
            ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(max(4, x.shape[1] / 60)))).astype(np.float32) / 255
        k = q["dehaze"] / 100 * 0.8 * veil[..., None]
        x = np.clip((x - k) / np.clip(1 - k, 0.3, 1), 0, 1.2)
    L = lum(x)
    c = q["contrast"] / 100
    nL = 0.45 + (L - 0.45) * (1 + 0.5 * c)
    hw = np.clip((L - 0.5) / 0.5, 0, 1) ** 1.2
    sw = np.clip(1 - L / 0.45, 0, 1) ** 2
    nL = nL + q["highlights"] / 100 * 0.45 * hw * (L - 0.5) + q["shadows"] / 100 * 0.35 * sw * (0.45 - L)
    ww = np.clip((L - 0.70) / 0.30, 0, 1) ** 2
    nL = nL + q["whites"] / 100 * 0.12 * ww
    b = q["blacks"] / 100
    if b < 0:  # deepen the black floor on luminance only (per-channel offsets tint near-black areas)
        bp = -b * 0.14
        nL = np.clip((nL - bp) / (1 - bp), 0, None)
    else:
        nL = nL + b * 0.08 * np.clip(1 - nL / 0.25, 0, 1)
    if q["black_p1"] is not None:
        bp = max(0.0, float(np.percentile(nL, 1)) - q["black_p1"] / 255)
        nL = np.clip((nL - bp) / (1 - bp), 0, None)
    x = x * (np.clip(nL, 0, 1.2) / (L + 1e-6))[..., None]
    x = np.clip(x, 0, 1)

    pts = np.array(q["curve"], np.float32) / 255.0
    L = lum(x)
    cL = np.interp(L, pts[:, 0], pts[:, 1])
    x = np.clip(x * (cL / (L + 1e-6))[..., None], 0, 1)

    h, s, v = rgb2hsv(x)
    dh, ds, dv = np.zeros_like(h), np.zeros_like(h), np.zeros_like(h)
    for band, centre in BANDS.items():
        bh, bs, bl = q["hsl"].get(band, [0, 0, 0])
        if bh == bs == bl == 0:
            continue
        d = np.abs(((h - centre + 180) % 360) - 180)
        w = np.clip(1 - d / WIDTH[band], 0, 1) * np.clip(s * 4, 0, 1)
        dh += w * bh / 100 * 30
        ds += w * bs / 100
        dv += w * bl / 100 * 0.30
    h = h + dh
    s = s * (1 + ds)
    v = v * (1 + dv)
    s = s * (1 + q["vibrance"] / 100 * (1 - s)) * (1 + q["saturation"] / 100)
    s = s * np.clip(v / 0.12, 0.3, 1)  # keep near-black areas neutral (dark brick and foliage keep their color)
    x = hsv2rgb(h, np.clip(s, 0, 1), np.clip(v, 0, 1))

    L = lum(x)
    bal = q["balance"] / 100
    sh_w = np.clip(1 - L / (0.45 + 0.15 * bal), 0, 1)[..., None]
    hi_w = np.clip((L - (0.55 + 0.15 * bal)) / 0.45, 0, 1)[..., None]
    md_w = np.clip(1 - np.abs(L - 0.5) / 0.35, 0, 1)[..., None]
    gsh, gmd, ghi = q["grade_shadows"], q["grade_midtones"], q["grade_highlights"]
    x = (x + sh_w * hue_rgb(gsh[0]) * gsh[1] / 100 * 0.25 + md_w * hue_rgb(gmd[0]) * gmd[1] / 100 * 0.25
         + hi_w * hue_rgb(ghi[0]) * ghi[1] / 100 * 0.25)

    k = -(q["clarity"] / 100) * 1.4
    if k:
        img = Image.fromarray((np.clip(x, 0, 1) * 255).astype(np.uint8))
        blur = np.asarray(img.filter(ImageFilter.GaussianBlur(max(2, x.shape[1] / 160)))).astype(np.float32) / 255
        mid = np.clip(1 - np.abs(L - 0.5) * 2, 0, 1)[..., None]
        x = x - k * mid * (x - blur)
    if q["texture"]:  # fine detail: boost or soften the smallest-scale contrast
        img = Image.fromarray((np.clip(x, 0, 1) * 255).astype(np.uint8))
        fine = np.asarray(img.filter(ImageFilter.GaussianBlur(max(0.8, x.shape[1] / 900)))).astype(np.float32) / 255
        x = x + q["texture"] / 100 * 1.2 * (x - fine)
    if q["vignette"]:
        hh, ww = x.shape[:2]
        yy, xx = np.mgrid[0:hh, 0:ww]
        rr = np.hypot((yy - hh / 2) / (hh / 2), (xx - ww / 2) / (ww / 2)) / math.sqrt(2)
        x = x * (1 + q["vignette"] / 100 * 0.6 * np.clip((rr - 0.35) / 0.65, 0, 1) ** 2)[..., None]
    if q["grain"]:
        rng = np.random.default_rng(7)
        x = x + rng.normal(0, q["grain"] / 100 * 0.05, x.shape[:2]).astype(np.float32)[..., None]
    return np.clip(x, 0, 1), ev


# ---------- measure + score ----------

ANALYSIS_EDGE = 480  # micro metrics (texture, grain, local contrast) are measured at one fixed size

TOL = {"p1": 5, "p5": 6, "p10": 7, "p25": 8, "p50": 10, "p75": 8, "p90": 7, "p95": 6, "p99": 5, "rolloff": 4,
       "sh_br": 4, "sh_g": 4, "mid_br": 5, "mid_g": 4, "hi_br": 4, "hi_g": 3,
       "sat": 0.04, "sat_sh": 0.04, "sat_mid": 0.04, "sat_hi": 0.04,
       "local_contrast": 0.006, "texture": 0.002, "softness": 0.08, "grain": 0.0015, "vignette": 0.05}
for _b in BANDS:
    TOL.update({f"{_b}_h": 6, f"{_b}_s": 0.05, f"{_b}_v": 12})

# Signature metrics carry the look; mid percentiles mostly follow scene content.
WEIGHT = {"p1": 2, "p5": 1, "p10": 1, "p25": 0.5, "p50": 1, "p75": 0.5, "p90": 1, "p95": 1, "p99": 2, "rolloff": 1.5,
          "sh_br": 2, "sh_g": 2, "mid_br": 2, "mid_g": 2, "hi_br": 2, "hi_g": 2,
          "sat": 2, "sat_sh": 1.5, "sat_mid": 1.5, "sat_hi": 1.5,
          "local_contrast": 0.5, "texture": 0.5, "softness": 3, "grain": 1, "vignette": 0.5}
# local_contrast and texture follow scene busyness (ferns read as punchy); their ratio, softness, carries the edit:
# higher = fine detail quiet next to larger shapes (negative Clarity/Texture glow), lower = crunchy.
for _b in BANDS:
    WEIGHT.update({f"{_b}_h": 2, f"{_b}_s": 2, f"{_b}_v": 1.5})

LABEL = {"p1": "darkest blacks", "p5": "deep shadows", "p10": "shadows", "p25": "lower midtones", "p50": "midtones",
         "p75": "upper midtones", "p90": "highlights", "p95": "bright highlights", "p99": "white ceiling",
         "rolloff": "highlight fade to white", "sh_br": "shadow tint (blue vs red)", "sh_g": "shadow tint (green vs magenta)",
         "mid_br": "midtone tint (blue vs red)", "mid_g": "midtone tint (green vs magenta)",
         "hi_br": "highlight tint (blue vs red)", "hi_g": "highlight tint (green vs magenta)",
         "sat": "overall colorfulness", "sat_sh": "colorfulness in shadows", "sat_mid": "colorfulness in midtones",
         "sat_hi": "colorfulness in highlights", "local_contrast": "local contrast (punch)", "texture": "fine texture",
         "grain": "grain / noise", "vignette": "corner darkening",
         "softness": "softness (fine detail vs larger shapes)"}
for _b in BANDS:
    LABEL.update({f"{_b}_h": f"{_b} hue", f"{_b}_s": f"{_b} saturation", f"{_b}_v": f"{_b} brightness"})


def _fixed(x):
    """Resize to ANALYSIS_EDGE on the long side so micro metrics compare across image sizes."""
    h, w = x.shape[:2]
    if max(h, w) == ANALYSIS_EDGE:
        return x
    f = ANALYSIS_EDGE / max(h, w)
    im = Image.fromarray((np.clip(x, 0, 1) * 255).astype(np.uint8)).resize((round(w * f), round(h * f)), Image.LANCZOS)
    return np.asarray(im).astype(np.float32) / 255


def _box(a, k, axis):
    pad = [(0, 0), (0, 0)]
    pad[axis] = (k + 1, k)
    c = np.cumsum(np.pad(a, pad, mode="edge"), axis=axis)
    hi = np.take(c, np.arange(2 * k + 1, c.shape[axis]), axis=axis)
    lo = np.take(c, np.arange(0, c.shape[axis] - 2 * k - 1), axis=axis)
    return (hi - lo) / (2 * k + 1)


def _blur(L, r):
    """Gaussian-like blur of a float array (three box passes)."""
    k = max(1, int(round(r * 0.8)))
    out = L.astype(np.float32)
    for _ in range(3):
        out = _box(_box(out, k, 0), k, 1)
    return out


def stats(x):
    x = _fixed(x)
    a = x * 255
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    L = lum(a)
    out = {f"p{q}": float(np.percentile(L, q)) for q in (1, 5, 10, 25, 50, 75, 90, 95, 99)}
    out["rolloff"] = float(np.percentile(L, 99.7) - out["p95"])
    h, s, v = rgb2hsv(x)
    neutral = s < 0.18  # judge casts on near-neutral pixels so scene content (foliage, sky) does not read as grade
    for name, lo, hi in (("sh", 13, 77), ("mid", 77, 179), ("hi", 179, 243)):
        k = (L >= lo) & (L < hi) & neutral
        if k.sum() > 150:
            r, g, b = R[k].mean(), G[k].mean(), B[k].mean()
            out[f"{name}_br"], out[f"{name}_g"] = float(b - r), float(g - (r + b) / 2)
        z = (L >= lo) & (L < hi) & (v > 0.1)
        if z.sum() > 150:
            out[f"sat_{name}"] = float(s[z].mean())
    out["sat"] = float(s[v > 0.15].mean())
    colored = (s > 0.15) & (v > 0.12)
    for band, centre in BANDS.items():
        d = ((h - centre + 180) % 360) - 180
        k = colored & (np.abs(d) < WIDTH[band] * 0.75)
        out[f"{band}_cov"] = float(k.mean())
        if k.mean() > 0.015:  # band is present in the frame
            out[f"{band}_h"] = float(np.degrees(np.angle(np.exp(1j * np.radians(d[k])).mean())))
            out[f"{band}_s"] = float(s[k].mean())
            out[f"{band}_v"] = float(v[k].mean() * 255)
    Ln = L / 255
    mid = (Ln > 0.15) & (Ln < 0.85)
    out["local_contrast"] = float(np.abs(Ln - _blur(Ln, 8))[mid].mean())
    hp = np.abs(Ln - _blur(Ln, 1.2))
    out["texture"] = float(hp[mid].mean())
    out["softness"] = out["local_contrast"] / max(out["texture"], 1e-4)
    flat = np.abs(Ln - _blur(Ln, 4)) < np.percentile(np.abs(Ln - _blur(Ln, 4)), 25)
    out["grain"] = float(np.median(hp[flat & mid])) if (flat & mid).sum() > 500 else 0.0
    hh, ww = Ln.shape
    yy, xx = np.mgrid[0:hh, 0:ww]
    rr = np.hypot((yy - hh / 2) / (hh / 2), (xx - ww / 2) / (ww / 2))
    centre, corner = Ln[rr < 0.5].mean(), Ln[rr > 1.15].mean()
    out["vignette"] = float(corner / max(centre, 1e-3))
    return out


def build_target(stat_list):
    keys = sorted(set().union(*stat_list))
    tgt = {}
    for k in keys:
        if k.endswith("_cov"):
            continue
        vals = [s[k] for s in stat_list if k in s]
        need = max(2, math.ceil(0.6 * len(stat_list))) if k[:-2] in BANDS else max(1, len(stat_list) // 2)
        if len(vals) >= need:  # a color band steers only when most references contain it
            tgt[k] = {"mean": float(np.mean(vals)), "tol": float(np.clip(np.std(vals), TOL[k], 2 * TOL[k]))}
    return tgt


def score(st, tgt):
    """0..100 closeness. A gap equal to the tolerance scores 90 for that metric."""
    gaps = {}
    for k, t in tgt.items():
        if k[:-2] in BANDS and st.get(k[:-2] + "_cov", 0) < 0.03:
            continue  # band too small in this photo to judge the grade
        if k in st:
            gaps[k] = (st[k] - t["mean"]) / t["tol"]
    if not gaps:
        return 0.0, {}
    vals = [math.exp(-0.105 * g * g) for g in gaps.values()]
    w = [WEIGHT[k] for k in gaps]
    return 100 * float(np.average(vals, weights=w)), gaps


def character(raw, base):
    """Raw score relative to how well the reference photos match their own set (100 = as close as they are)."""
    return min(100.0, 100.0 * raw / max(base, 1e-6))


HINTS = {"p1": "Blacks", "p5": "Blacks", "p10": "Shadows", "p25": "Shadows", "p50": "Exposure / Point Curve midpoint",
         "p75": "Highlights", "p90": "Highlights", "p95": "Whites", "p99": "Whites", "rolloff": "Whites / Point Curve top",
         "sh_br": "Color Grading shadows hue", "sh_g": "Color Grading shadows / Tint", "mid_br": "Temp", "mid_g": "Tint",
         "hi_br": "Color Grading highlights / Temp", "hi_g": "Tint", "sat": "Saturation / Vibrance",
         "sat_sh": "Color Grading shadows saturation", "sat_mid": "Vibrance", "sat_hi": "Color Grading highlights saturation",
         "local_contrast": "Clarity / Dehaze", "texture": "Texture / Sharpening", "grain": "Grain", "vignette": "Vignette",
         "softness": "Texture and Clarity (raise = negative values)"}
for _b in BANDS:
    HINTS.update({f"{_b}_h": f"Color Mix {_b.capitalize()} Hue", f"{_b}_s": f"Color Mix {_b.capitalize()} Saturation",
                  f"{_b}_v": f"Color Mix {_b.capitalize()} Luminance"})


# ---------- commands ----------

def cmd_fetch(a):
    os.makedirs(a.out, exist_ok=True)
    req = urllib.request.Request(a.url, headers={"User-Agent": "Mozilla/5.0"})
    page = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    quote = "[\"']"
    found = re.findall(r"(?:src|data-src|data-image|content|href)=" + quote + r"([^\"']+\.(?:jpe?g|png|webp)[^\"']*)" + quote, page, re.I)
    found += re.findall(r'https://images\.squarespace-cdn\.com/[^"\'\s?]+', page)
    urls, seen = [], set()
    for u in found:
        u = urllib.parse.urljoin(a.url, html.unescape(u)).split("?")[0]
        if u not in seen and not re.search(r"logo|icon|favicon|avatar|sprite", u, re.I):
            seen.add(u)
            urls.append(u)
    kept = []
    for u in urls:
        if len(kept) >= a.max:
            break
        try:
            q = u + ("?format=1500w" if "squarespace-cdn" in u else "")
            data = urllib.request.urlopen(urllib.request.Request(q, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read()
            im = Image.open(io.BytesIO(data)).convert("RGB")
        except Exception:
            continue
        if min(im.size) < 400:
            continue
        name = f"ref{len(kept) + 1:02d}.jpg"
        im.save(os.path.join(a.out, name), quality=92)
        kept.append((name, u))
    with open(os.path.join(a.out, "SOURCES.txt"), "w") as f:
        f.write(f"page: {a.url}\nLocal analysis only. Do not republish or ship these files.\n")
        f.writelines(f"{n}\t{u}\n" for n, u in kept)
    print(f"saved {len(kept)} reference images to {a.out} (sources in SOURCES.txt)")


def cmd_sheet(a):
    files = sorted(f for f in os.listdir(a.folder) if not f.startswith("."))
    tiles = []
    for f in files[: a.max]:
        try:
            x, _ = load(os.path.join(a.folder, f), 300)
        except Exception:
            continue
        im = Image.fromarray((x * 255).astype(np.uint8))
        im.thumbnail((260, 260))
        t = Image.new("RGB", (260, 280), "white")
        t.paste(im)
        ImageDraw.Draw(t).text((2, 266), f, fill="black")
        tiles.append(t)
    cols = 6
    sheet = Image.new("RGB", (260 * cols, 280 * max(1, -(-len(tiles) // cols))), "white")
    for i, t in enumerate(tiles):
        sheet.paste(t, ((i % cols) * 260, (i // cols) * 280))
    sheet.save(a.out, quality=88)
    print(f"contact sheet with {len(tiles)} images: {a.out}")


def cmd_measure(a):
    sts = [stats(load(p, 1000)[0]) for p in a.images]
    tgt = build_target(sts)
    own = [score(s, tgt)[0] for s in sts]
    base = float(np.mean(own))
    with open(a.out, "w") as f:
        json.dump({"images": [os.path.basename(p) for p in a.images], "target": tgt, "reference_score": base}, f, indent=1)
    print(f"target from {len(sts)} images -> {a.out}")
    print(f"reference photos score {min(own):.1f}-{max(own):.1f} against their own set (mean {base:.1f} = 100% character match)")
    for k, t in tgt.items():
        print(f"  {k:8s} {t['mean']:8.2f}  (tolerance {t['tol']:.2f})")


def _get(p, key):
    cur = p
    parts = key.split(".")
    for part in parts[:-1]:
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    last = parts[-1]
    return cur, (int(last) if isinstance(cur, list) else last)


def cmd_fit(a):
    tj = json.load(open(a.target))
    tgt, base = tj["target"], tj.get("reference_score", 100.0)
    srcs = [load(p, ANALYSIS_EDGE)[0] for p in a.sources]
    p = _start_preset(json.load(open(a.start)) if a.start else {}, tgt)

    def one(s, pp):
        out = render(s, pp)[0]
        sc, gaps = score(stats(out), tgt)
        clip = float((lum(out * 255) >= 254).mean() * 100)
        return character(sc, base) - 3 * sum(abs(g) > 2 and WEIGHT[k] >= 2 for k, g in gaps.items()) - 5 * max(0.0, clip - 0.5)

    def total(pp):  # reward the weakest photo too, so one shared preset fits the whole set
        v = [one(s, pp) for s in srcs]
        return 0.5 * float(np.mean(v)) + 0.5 * float(np.min(v))

    plan = {k: _get(p, k)[0][_get(p, k)[1]] for k in FIT_SPACE}
    best = total(p)
    print(f"start character match {best:.1f}%")
    steps = {k: v[0] for k, v in FIT_SPACE.items()}
    for rnd in range(a.rounds):
        improved = False
        for key, (_, lo, hi) in FIT_SPACE.items():
            cont, idx = _get(p, key)
            win = WINDOW.get(key, 20 if key.startswith("hsl.") else 25)
            lo, hi = max(lo, plan[key] - win), min(hi, plan[key] + win)
            old, pick = cont[idx], None
            for sign in (1, -1):  # try both directions, keep the better one
                new = float(np.clip(old + sign * steps[key], lo, hi))
                if key.startswith("grade_") and key.endswith(".0"):
                    new = float(np.clip(old + sign * steps[key], plan[key] - win, plan[key] + win)) % 360
                cont[idx] = new
                sc = total(p)
                if sc > best + 0.05 and (pick is None or sc > pick[1]):
                    pick = (new, sc)
            cont[idx] = old if pick is None else pick[0]
            if pick:
                best, improved = pick[1], True
        print(f"round {rnd + 1}: character match {best:.1f}%")
        if best >= a.goal:
            break
        if not improved:
            steps = {k: v / 2 for k, v in steps.items()}
    _round(p)
    json.dump(p, open(a.out, "w"), indent=1)
    print(f"preset -> {a.out}  character match {best:.1f}% (goal {a.goal}%)")


def _round(p):
    for k in ("contrast", "highlights", "shadows", "whites", "blacks", "temp", "tint", "vibrance", "saturation", "clarity", "texture", "grain", "balance", "target_p50", "dehaze"):
        p[k] = int(round(p[k]))
    p["hsl"] = {b: [int(round(v)) for v in vals] for b, vals in p["hsl"].items()}
    p["grade_shadows"] = [int(round(v)) for v in p["grade_shadows"]]
    p["grade_highlights"] = [int(round(v)) for v in p["grade_highlights"]]
    p["grade_midtones"] = [int(round(v)) for v in p["grade_midtones"]]
    p["vignette"] = int(round(p["vignette"]))


# ---------- loop: fit, score every photo, nudge from the gaps, repeat ----------

# measure -> (setting, effect): effect +1 means raising the setting raises the measure
NUDGE = {"p10": ("shadows", 1), "p25": ("shadows", 1), "p50": ("target_p50", 1), "p75": ("highlights", 1),
         "p90": ("highlights", 1), "p95": ("whites", 1), "p99": ("whites", 1), "mid_br": ("temp", -1),
         "mid_g": ("tint", -1), "sat": ("saturation", 1), "sat_sh": ("vibrance", 1),
         "sat_hi": ("grade_highlights.1", 1), "softness": ("clarity", -1), "texture": ("texture", 1),
         "vignette": ("vignette", 1), "grain": ("grain", 1)}
for _i, _b in enumerate(BANDS):
    NUDGE.update({f"{_b}_h": (f"hsl.{_b}.0", 1), f"{_b}_s": (f"hsl.{_b}.1", 1), f"{_b}_v": (f"hsl.{_b}.2", 1)})

_W = {}


def _init_worker(paths, tgt, base):
    _W.update(srcs=[load(q, ANALYSIS_EDGE)[0] for q in paths], tgt=tgt, base=base)


def _eval_photo(job):
    i, preset = job
    out = render(_W["srcs"][i], json.loads(preset))[0]
    sc, gaps = score(stats(out), _W["tgt"])
    clip = float((lum(out * 255) >= 254).mean() * 100)
    ok = character(sc, _W["base"]) >= 95 and clip <= 0.5 and all(abs(g) <= 2 for k, g in gaps.items() if WEIGHT[k] >= 2)
    return character(sc, _W["base"]), gaps, clip, ok


def _start_preset(start, tgt):  # per-photo anchors come from the target unless the plan set them
    p = json.loads(json.dumps({**DEFAULT, **start, "hsl": {**DEFAULT["hsl"], **start.get("hsl", {})}}))
    if "target_p50" not in start and "p50" in tgt:
        p["target_p50"] = round(tgt["p50"]["mean"])
    if start.get("black_p1") is None and "p1" in tgt:
        p["black_p1"] = round(tgt["p1"]["mean"])
    if start.get("wb_target") is None and "mid_br" in tgt and "mid_g" in tgt:
        p["wb_target"] = [round(tgt["mid_br"]["mean"], 1), round(tgt["mid_g"]["mean"], 1)]
    return p


def cmd_loop(a):
    from concurrent.futures import ProcessPoolExecutor
    tj = json.load(open(a.target))
    tgt, base = tj["target"], tj.get("reference_score", 100.0)
    p = _start_preset(json.load(open(a.start)) if a.start else {}, tgt)
    holds = {h.split(":")[0]: tuple(float(v) for v in h.split(":")[1:]) for h in a.hold}

    def bounds(key):  # a hold keeps a setting inside a range the user or the crops chose
        lo, hi = FIT_SPACE.get(key, (0, -100, 100))[1:]
        return holds.get(key, (lo, hi))

    for key, (lo, hi) in holds.items():
        cont, idx = _get(p, key)
        cont[idx] = float(np.clip(cont[idx], lo, hi))
    n, log = len(a.photos), []
    with ProcessPoolExecutor(max_workers=min(8, os.cpu_count() or 2), initializer=_init_worker,
                             initargs=(a.photos, tgt, base)) as pool:

        def run(pp):
            return list(pool.map(_eval_photo, [(i, json.dumps(pp)) for i in range(n)]))

        def objective(res):
            v = [c - 3 * sum(abs(g) > 2 and WEIGHT[k] >= 2 for k, g in gaps.items()) - 5 * max(0.0, clip - 0.5)
                 for c, gaps, clip, _ in res]
            return 0.5 * float(np.mean(v)) + 0.5 * float(np.min(v))

        for loop in range(1, a.max_loops + 1):
            res = run(p)
            mean_c, passed = float(np.mean([r[0] for r in res])), sum(r[3] for r in res)
            print(f"loop {loop}: mean character match {mean_c:.1f}%, photos passing {passed}/{n}")
            log.append({"loop": loop, "mean_character_match": round(mean_c, 1), "passing": passed})
            if mean_c >= a.goal and passed == n:
                print("done: goal reached")
                break
            # nudge each setting tied to a measure that is off on average (signature measures only)
            moves = {}
            for k, (key, eff) in NUDGE.items():
                g = [r[1][k] for r in res if k in r[1]]
                if len(g) < max(2, n // 3) or WEIGHT.get(k, 0) < 1.5:
                    continue
                gm = float(np.mean(g))
                if abs(gm) > 0.7:
                    step = FIT_SPACE.get(key, (8, -100, 100))[0]
                    moves[key] = moves.get(key, 0.0) - eff * step * float(np.clip(gm / 2, -2, 2))
            for key, d in moves.items():
                cont, idx = _get(p, key)
                lo, hi = bounds(key)
                cont[idx] = float(np.clip(cont[idx] + d, lo, hi))
            if moves:
                print("  nudged: " + ", ".join(f"{k} {d:+.0f}" for k, d in moves.items()))
            # one fine-tune pass around the nudged plan
            best = objective(run(p))
            for key, (step, _, _) in FIT_SPACE.items():
                lo, hi = bounds(key)
                cont, idx = _get(p, key)
                old, pick = cont[idx], None
                for sign in (1, -1):
                    cont[idx] = float(np.clip(old + sign * step / 2, lo, hi))
                    sc = objective(run(p))
                    if sc > best + 0.05 and (pick is None or sc > pick[1]):
                        pick = (cont[idx], sc)
                cont[idx] = old if pick is None else pick[0]
                if pick:
                    best = pick[1]
        else:
            print(f"stopped after {a.max_loops} loops without reaching the goal")
    _round(p)
    json.dump(p, open(a.out, "w"), indent=1)
    json.dump(log, open(os.path.splitext(a.out)[0] + "_loop_log.json", "w"), indent=1)
    print(f"preset -> {a.out}")


def cmd_grade(a):
    p = json.load(open(a.preset))
    tj = json.load(open(a.target)) if a.target else None
    tgt = tj["target"] if tj else None
    os.makedirs(a.out, exist_ok=True)
    rows, tiles = [], []
    for path in a.images:
        src, note = load(path, a.size)
        out, ev = render(src, p)
        name = os.path.splitext(os.path.basename(path))[0]
        Image.fromarray((out * 255).astype(np.uint8)).save(os.path.join(a.out, name + "_graded.jpg"), quality=93)
        bi, ai = Image.fromarray((src * 255).astype(np.uint8)), Image.fromarray((out * 255).astype(np.uint8))
        w, hh = bi.size
        sheet = Image.new("RGB", (w * 2 + 30, hh + 44), "white")
        sheet.paste(bi, (10, 34))
        sheet.paste(ai, (w + 20, 34))
        d = ImageDraw.Draw(sheet)
        d.text((12, 10), "BEFORE", fill="black")
        d.text((w + 22, 10), "AFTER", fill="black")
        sheet.save(os.path.join(a.out, name + "_compare.jpg"), quality=88)
        st = stats(out)
        line = {"photo": name, "decode": note, "exposure_ev": round(ev, 2), "p1": round(st["p1"]), "p50": round(st["p50"]), "p99": round(st["p99"])}
        k = (lum(out * 255) >= 178)
        if k.sum() > 200:
            o = out * 255
            line["hi_blue_minus_red"] = round(float(o[..., 2][k].mean() - o[..., 0][k].mean()), 1)
            line["hi_red_minus_green"] = round(float(o[..., 0][k].mean() - o[..., 1][k].mean()), 1)
        line["clipped_pct"] = round(float((lum(out * 255) >= 254).mean() * 100), 2)
        if tgt:
            sc, gaps = score(st, tgt)
            cm = character(sc, tj.get("reference_score", 100.0))
            line["character_match_pct"] = round(cm, 1)
            worst = sorted(gaps.items(), key=lambda kv: -abs(kv[1]))[:3]
            line["largest_gaps"] = [f"{k} {g:+.1f} tol -> {HINTS[k]}" for k, g in worst if abs(g) > 1]
            line["numbers_pass"] = bool(cm >= a.goal and all(abs(g) <= 2 for k, g in gaps.items() if WEIGHT[k] >= 2) and line["clipped_pct"] <= 0.5)
        tiles.append(ai)
        if tgt:  # full fingerprint comparison, worst first, in plain words
            rep = [f"{name}: character match {line['character_match_pct']}%", f"{'measure':34s} {'look':>9s} {'yours':>9s}  gap  slider"]
            for k, g in sorted(gaps.items(), key=lambda kv: -abs(kv[1]) * WEIGHT[kv[0]]):
                rep.append(f"{LABEL[k]:34s} {tgt[k]['mean']:9.3f} {st[k]:9.3f} {g:+5.1f}  {HINTS[k] if abs(g) > 1 else 'ok'}")
            open(os.path.join(a.out, name + "_report.txt"), "w").write("\n".join(rep) + "\n")
        rows.append(line)
        print(json.dumps(line))
    json.dump(rows, open(os.path.join(a.out, "qa.json"), "w"), indent=1)
    if a.refs:  # side-by-side board for the visual check: graded photos on top, references below
        refs = [Image.open(r).convert("RGB") for r in a.refs[:6]]
        for im in tiles + refs:
            im.thumbnail((420, 420))
        cols = max(len(tiles), len(refs))
        board = Image.new("RGB", (cols * 430 + 10, 2 * 430 + 40), "white")
        d = ImageDraw.Draw(board)
        d.text((10, 4), "YOUR PHOTOS (graded)", fill="black")
        d.text((10, 444), "REFERENCE LOOK", fill="black")
        for i, im in enumerate(tiles):
            board.paste(im, (10 + i * 430, 20))
        for i, im in enumerate(refs):
            board.paste(im, (10 + i * 430, 460))
        board.save(os.path.join(a.out, "board.jpg"), quality=88)
        print(f"visual check board: {os.path.join(a.out, 'board.jpg')}")


def cmd_xmp(a):
    p = {**DEFAULT, **json.load(open(a.preset))}
    hsl = {**DEFAULT["hsl"], **p["hsl"]}
    attrs = {
        "PresetType": "Normal", "UUID": uuid.uuid4().hex.upper(), "SupportsAmount": "True", "SupportsColor": "True",
        "SupportsMonochrome": "False", "SupportsHighDynamicRange": "True", "SupportsNormalDynamicRange": "True",
        "SupportsSceneReferred": "True", "SupportsOutputReferred": "True", "Version": "15.4", "ProcessVersion": "15.4",
        "WhiteBalance": "As Shot", "IncrementalTemperature": p["temp"], "IncrementalTint": p["tint"],
        "Contrast2012": p["contrast"], "Highlights2012": p["highlights"], "Shadows2012": p["shadows"],
        "Whites2012": p["whites"], "Blacks2012": p["blacks"], "Texture": p["texture"], "Clarity2012": p["clarity"],
        "Vibrance": p["vibrance"], "Dehaze": p["dehaze"], "Saturation": p["saturation"],
        "SplitToningShadowHue": p["grade_shadows"][0], "SplitToningShadowSaturation": p["grade_shadows"][1],
        "SplitToningHighlightHue": p["grade_highlights"][0], "SplitToningHighlightSaturation": p["grade_highlights"][1],
        "SplitToningBalance": p["balance"], "ColorGradeMidtoneHue": p["grade_midtones"][0],
        "ColorGradeMidtoneSat": p["grade_midtones"][1], "PostCropVignetteAmount": p["vignette"], "ColorGradeBlending": 50, "GrainAmount": p["grain"],
        "ToneCurveName2012": "Custom", "HasSettings": "True",
    }
    for band, (bh, bs, bl) in hsl.items():
        cap = band.capitalize()
        attrs[f"HueAdjustment{cap}"], attrs[f"SaturationAdjustment{cap}"], attrs[f"LuminanceAdjustment{cap}"] = bh, bs, bl

    def fmt(v):
        return f"+{v}" if isinstance(v, (int, float)) and not isinstance(v, bool) and v > 0 else str(v)

    body = "\n".join(f'    crs:{k}="{fmt(v)}"' for k, v in attrs.items())
    curve = "\n".join(f"     <rdf:li>{int(x)}, {int(y)}</rdf:li>" for x, y in p["curve"])
    flat = "     <rdf:li>0, 0</rdf:li>\n     <rdf:li>255, 255</rdf:li>"
    seqs = "".join(f"   <crs:ToneCurvePV2012{c}>\n    <rdf:Seq>\n{flat}\n    </rdf:Seq>\n   </crs:ToneCurvePV2012{c}>\n" for c in ("Red", "Green", "Blue"))
    xml = f'''<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 7.0-c000 1.000000, 0000/00/00-00:00:00">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"
{body}>
   <crs:Name>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{html.escape(a.name)}</rdf:li>
    </rdf:Alt>
   </crs:Name>
   <crs:Group>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">lightroom-match</rdf:li>
    </rdf:Alt>
   </crs:Group>
   <crs:ToneCurvePV2012>
    <rdf:Seq>
{curve}
    </rdf:Seq>
   </crs:ToneCurvePV2012>
{seqs}  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
'''
    open(a.out, "w").write(xml)
    import xml.dom.minidom
    xml.dom.minidom.parseString(open(a.out).read())  # raises if malformed
    print(f"preset file -> {a.out} (valid XML; Exposure omitted so it adapts per photo)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch"); f.add_argument("url"); f.add_argument("--out", required=True); f.add_argument("--max", type=int, default=30)
    s = sub.add_parser("sheet"); s.add_argument("folder"); s.add_argument("--out", required=True); s.add_argument("--max", type=int, default=60)
    m = sub.add_parser("measure"); m.add_argument("images", nargs="+"); m.add_argument("--out", required=True)
    t = sub.add_parser("fit"); t.add_argument("--target", required=True); t.add_argument("--sources", nargs="+", required=True)
    t.add_argument("--start"); t.add_argument("--out", required=True); t.add_argument("--goal", type=float, default=95); t.add_argument("--rounds", type=int, default=8)
    g = sub.add_parser("grade"); g.add_argument("images", nargs="+"); g.add_argument("--preset", required=True)
    g.add_argument("--target"); g.add_argument("--out", required=True); g.add_argument("--size", type=int, default=1600)
    g.add_argument("--refs", nargs="*"); g.add_argument("--goal", type=float, default=95)
    lp = sub.add_parser("loop"); lp.add_argument("--target", required=True); lp.add_argument("--photos", nargs="+", required=True)
    lp.add_argument("--start"); lp.add_argument("--out", required=True); lp.add_argument("--goal", type=float, default=95)
    lp.add_argument("--max-loops", type=int, default=6)
    lp.add_argument("--hold", nargs="*", default=[], help="setting:min:max, e.g. clarity:-40:-10")
    x = sub.add_parser("xmp"); x.add_argument("--preset", required=True); x.add_argument("--name", required=True); x.add_argument("--out", required=True)
    a = ap.parse_args()
    commands = {"fetch": cmd_fetch, "sheet": cmd_sheet, "measure": cmd_measure, "fit": cmd_fit, "grade": cmd_grade,
                "xmp": cmd_xmp, "loop": cmd_loop}
    run = commands[a.cmd]
    run(a)


if __name__ == "__main__":
    main()
