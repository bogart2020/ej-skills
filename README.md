# EJ Skills (`ej-skills`)

Personal [Agent Skills](https://agentskills.io) plugin encoding how I research, verify facts, make decisions, and run workflows. Built for universal compatibility across **Claude Desktop**, **Claude Code**, **OpenAI Codex**, **GitHub Copilot**, **Google Antigravity**, **Gemini CLI**, **Cursor**, and **Windsurf**.

---

## Skills

### Model-invoked

Reachable automatically when your prompt matches their trigger conditions, or explicitly via `/skill-name`:

- **[compare](./skills/compare/SKILL.md)**: Compare any two or more options head-to-head across weighted MECE categories (products, places/cities/neighborhoods, job candidates, athletes/historical figures, software/architectures, companies, careers, or policies). Normalizes domain metrics (PPP/RPP real surplus, era-adjusted Z-scores and JAWS, BARS anchors, geometric mean benchmark ratios, and 7-bucket TCO), applies Separate-Evaluation reality checks and PROMETHEE indifference thresholds to call `Winner (Decisive)`, `Winner (Narrow Edge)`, or `Tie` in every category, audits non-alignable differentiators, and reconciles the Category Win-Loss-Tie tally with the Weighted Composite Score ($U$) to deliver a calibrated overall winner and crossover conditions.
- **[fact-check](./skills/fact-check/SKILL.md)**: Deep-research and verify factual accuracy against Tier 1 primary sources. Decomposes topics, drafts, URLs, or prior AI answers into self-contained atomic claims, runs paired primary-source and Popperian falsification queries, traces secondary claims back to root sources to defeat circular reporting (citogenesis), assigns a calibrated 6-level verdict (`Verified`, `Refuted`, `Mixed / Needs Context`, `Outdated`, `Disputed`, `Unverifiable`), and supplies verbatim excerpts plus drop-in corrections.
- **[lightroom-match](./skills/lightroom-match/SKILL.md)**: Replicate a reference photo's color grade, tone curve, and look onto a source or RAW photo in Adobe Lightroom Mobile at 95% to 100% perceptual fidelity (`95%–100% Exact Lock`, `95%+ Match With Local Masks`, `Screenshot Check Needed for 95%+ Lock`, `85%–94% Close Approximation`, `Lighting or Time-of-Day Mismatch`, `Missing or Unclear Reference/Source`). Relentlessly interviews on the 5 recipe-flipping variables (consulting an optional `.agents/photo-profile.md` or `~/.agents/photo-profile.md`), neutralizes camera RAW sensor baselines (Sony ARW, Canon CR2/CR3, Nikon NEF, Fujifilm RAF X-Trans + Camera Matching, Leica/Ricoh DNG, Apple ProRAW `ProfileGainTableMap` Profile Amount slider, Samsung Expert RAW, and 8-bit JPEG/HEIC safe bounds), decomposes the 5 tonal zones and 8 HSL color bands, renders visual $4\times 4$ ASCII/Unicode Tone Curves alongside `(In %, Out %)` and `(0–255, 0–255)` coordinate tables across RGB, Red, Green, and Blue, maps Color Grading wheels ($0^\circ\text{–}360^\circ$), Effects, Detail/Optics, and Local Masks (plus Free-tier global workarounds), and includes a Pass 2 screenshot fine-tuning loop.
- **[should-i-buy](./skills/should-i-buy/SKILL.md)**: Evaluate buying and financial decisions across any category to deliver a calibrated 6-level verdict (`Buy`, `Buy With Conditions / Wait`, `Buy Alternative Instead`, `Rent / Borrow / Trial First`, `Keep Current / Repair`, `Do Not Buy`) with explicit reversal conditions. Gathers missing context on the 5 verdict-flipping variables (consulting an optional `.agents/buyer-profile.md` or `~/.agents/buyer-profile.md`), benchmarks against non-purchase baselines, audits independent tests and 1-to-3 star failure modes, computes 7-bucket Total Cost of Ownership (TCO) and 50%-deflated Cost-Per-Use (`CPU`), and runs a Diderot spiral check plus 12-month premortem.
- **[stress-test](./skills/stress-test/SKILL.md)**: Stress-test agent skills across happy paths, negative bounds, edge cases, invariance checks, and adversarial probes using weak-model subagents to expose instruction drift. Ingests any target skill, decomposes its procedural steps and gates, synthesizes a 5-suite behavioral test matrix (CheckList MFT, NEG, EDGE, INV, and ADV), fans out isolated parallel subagents running lightweight model constraints (such as Claude Haiku, GPT-4o-mini, or Gemini Flash-Lite), evaluates multi-turn transcripts using a hybrid deterministic-and-judge pipeline, computes reliability metrics ($R_{\text{INV}}$, $I_{\text{adhere}}$, $D_{\text{rate}}$, $pass^k$), and outputs an executive scorecard with line-by-line prompt remediations.
- **[trip-planner](./skills/trip-planner/SKILL.md)**: Plan stress-tested trips and day-by-day itineraries, audit draft itineraries, or compare flights, routes, hotels, and base neighborhoods to deliver a calibrated 6-level readiness verdict (`Ready to Book`, `Viable With Adjustments`, `Cut Stops / Slow Down`, `Reroute / Change Base`, `Shift Season / Dates`, `Do Not Book As Planned`) with explicit reversal conditions. Bounds the 5 verdict-flipping travel variables (consulting an optional `.agents/traveler-profile.md` or `~/.agents/traveler-profile.md`), clears the Logistics & Entry Knockout Gate (Schengen 10-year/3-month and 6-month passport rules, visa/ETA lead times, 1949/1968 IDP, $>2,500\text{ m}$ altitude acclimatization, weather, and macro-holidays), clusters stops around bases scored by True Location-Adjusted Nightly Cost ($C_{\text{night, true}}$), computes Door-to-Door transit math ($T_{\text{D2D}}$) and Single-PNR vs. Self-Transfer connection buffers, caps daily pacing at `1 Fixed Anchor + 1 Flexible Option` per half-day with native regional anti-tourist-trap vetting, and runs a 4-point Travel Premortem with If/Then pivots and a chronological Booking Action Timeline.

---

## Installation

Pick **one** installation route per platform so skills are not loaded twice.

### 1. Claude Desktop (Add from repo or GUI Upload)

**Option A: Add from repo (recommended, installs all skills and tracks this repo for updates)**
1. Open **Claude Desktop -> Customize -> Plugins**.
2. Choose **Add -> Add marketplace** and enter `bogart2020/ej-skills`.
3. Install the **ej-skills** plugin from that marketplace. Every skill in this repo is enabled in one step.
4. Turn on **Sync automatically** (or use **Check for updates**) so new pushes to `main` arrive.

**Option B: Upload standalone skill zip (works in any Claude Desktop plan with Skills enabled, no auto-update)**
1. Clone this repository and run `bash scripts/package-skills.sh`. It builds one archive per skill in `dist/` (for example `dist/compare.zip`).
2. Open **Claude Desktop -> Customize -> Skills**, then **+ -> Create skill -> Upload a skill**.
3. Select the `.zip` archive for the skill you want to add. Re-upload the zip after each change.

### 2. Claude Code

```bash
/plugin marketplace add bogart2020/ej-skills
/plugin install ej-skills@ej-skills
```

### 3. OpenAI Codex

```bash
codex plugin marketplace add bogart2020/ej-skills
codex plugin add ej-skills@ej-skills
```

### 4. GitHub Copilot (CLI and VS Code)

```bash
copilot plugin marketplace add bogart2020/ej-skills
copilot plugin install ej-skills@ej-skills
```

In VS Code, run **Chat: Install Plugin From Source** and enter `https://github.com/bogart2020/ej-skills`.

To install a single skill with GitHub CLI 2.90 or later: `gh skill install bogart2020/ej-skills <skill-name>`.

### 5. Gemini CLI

```bash
gemini skills install https://github.com/bogart2020/ej-skills.git --path skills
```

### 6. Cursor, Windsurf, OpenCode, Devin, Amp, Pi (`skills.sh`)

```bash
# Install all skills in the bundle:
npx skills@latest add bogart2020/ej-skills

# Or install a single skill:
npx skills@latest add bogart2020/ej-skills --skill=compare
npx skills@latest add bogart2020/ej-skills --skill=fact-check
npx skills@latest add bogart2020/ej-skills --skill=lightroom-match
npx skills@latest add bogart2020/ej-skills --skill=should-i-buy
npx skills@latest add bogart2020/ej-skills --skill=trip-planner
```

### 7. Local Development (Symlink)

```bash
bash scripts/link-skills.sh
```

---

## Repository Structure

```text
ej-skills/
├── .claude-plugin/
│   ├── marketplace.json        # Self-hosted marketplace index (Claude, Codex, Copilot)
│   └── plugin.json             # Plugin manifest (Claude, Codex, Copilot, VS Code)
├── plugin.json                 # Google Antigravity (AGY) root plugin manifest
├── AGENTS.md                   # Authoring rules (CLAUDE.md symlinked here)
├── scripts/
│   ├── link-skills.sh          # Symlinks skills to ~/.claude/skills & ~/.agents/skills
│   └── package-skills.sh       # Builds dist/<skill-name>.zip for Claude Desktop upload (git-ignored)
└── skills/
    ├── compare/
    │   ├── SKILL.md            # Core 6-step head-to-head comparison sequence & verdict rules
    │   ├── agents/
    │   │   └── openai.yaml     # OpenAI Codex UI metadata
    │   └── references/
    │       ├── entity-playbooks.md
    │       └── report-format.md
    ├── fact-check/
    │   ├── SKILL.md            # Core verification sequence & reference rules
    │   ├── agents/
    │   │   └── openai.yaml     # OpenAI Codex UI metadata
    │   └── references/
    │       └── domain-playbooks.md
    ├── lightroom-match/
    │   ├── SKILL.md            # Core 6-step Lightroom Mobile replication sequence & verdict rules
    │   ├── agents/
    │   │   └── openai.yaml     # OpenAI Codex UI metadata
    │   └── references/
    │       ├── camera-raw-and-style-playbooks.md
    │       ├── photo-profile-template.md
    │       └── recipe-output-format.md
    ├── should-i-buy/
    │   ├── SKILL.md            # Core 6-step buying decision sequence & verdict rules
    │   ├── agents/
    │   │   └── openai.yaml     # OpenAI Codex UI metadata
    │   └── references/
    │       ├── buyer-profile-template.md
    │       ├── category-playbooks.md
    │       ├── cost-math.md
    │       └── report-format.md
    └── trip-planner/
        ├── SKILL.md            # Core 6-step trip planning & audit sequence & verdict rules
        ├── agents/
        │   └── openai.yaml     # OpenAI Codex UI metadata
        └── references/
            ├── destination-and-mode-playbooks.md
            ├── planning-rules.md
            ├── report-format.md
            └── traveler-profile-template.md
```

## License

MIT. See [LICENSE](./LICENSE).
