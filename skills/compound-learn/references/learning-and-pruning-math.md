# Continual Learning, Retention Decay, and Competency Calibration Math

## Contents

- Purpose and Workflow Link
- Ebbinghaus Memory Retention and Spaced Reinforcement
- Single-Source-of-Truth Exclusivity Scoring
- Tri-Factor Composite Memory Utility
- Core Instruction Token Budget and 1-In/1-Pruned Gate
- Five-Stage Competency Index (Dreyfus Progression)

---

## Purpose and Workflow Link

This reference defines the mathematical formulas, scoring rubrics, and decision thresholds used during Steps 3, 4, and 5 of the continual learning and pruning pipeline. For the primary workflow sequence, see [../SKILL.md](../SKILL.md).

---

## Ebbinghaus Memory Retention and Spaced Reinforcement

Grounded in **MemoryBank** (`arXiv:2305.10250`), every rule or memory item stored in the project ledger decays over elapsed sessions unless reinforced by real usage or live codebase verification.

### 1. Stability Strength (`Stability_Strength`)
- **Initial Stability (`S_0`):** Set `Stability_Strength = 5` when a new rule or lesson is first recorded.
- **Reinforcement Step:** Each time a rule is actively applied during a session or verified against live codebase files, increment its stability by `+5`:
  `New_Stability_Strength = Current_Stability_Strength + 5`
- **Partial Drift Reset:** If a rule required minor path or command updating during a session, reset its `Stability_Strength = 5` and `Sessions_Since_Verified = 0`.

### 2. Memory Retention Formula (`Retention`)
Compute the retention score (called **Memory Freshness Score** in user-facing output) on a `0.00` to `1.00` scale:

`Retention = exp(- Sessions_Since_Verified / Stability_Strength)`

| `Sessions_Since_Verified` | `Stability_Strength = 5` (New) | `Stability_Strength = 10` (1x Reinforced) | `Stability_Strength = 20` (3x Reinforced) | Action Threshold |
| :--- | :--- | :--- | :--- | :--- |
| `0 sessions` | `1.00` | `1.00` | `1.00` | Active and fresh |
| `2 sessions` | `0.67` | `0.82` | `0.90` | Keep active |
| `5 sessions` | `0.37` | `0.61` | `0.78` | Borderline if unreinforced |
| `6+ sessions` | `0.30` (Below `0.35`) | `0.55` | `0.74` | Flag unreinforced rule for re-verification or pruning |

**Decay Gate:** Any non-pinned rule with `Retention < 0.35` that has not been triggered in 6 or more sessions must be re-verified against the live codebase; if its target module or workflow was superseded, prune it.

---

## Single-Source-of-Truth Exclusivity Scoring

A persistent instruction file is a behavioral contract, not a mirror of files the agent can inspect directly. Score every rule on **Exclusivity (`Exclusivity`)** from `0.00` to `1.00`:

| Score | Category | Examples | Retention Policy |
| :--- | :--- | :--- | :--- |
| `1.00` | **Tacit Unwritten Knowledge** | User corrections, non-obvious edge cases, business domain invariants, reasons why a seemingly simpler approach fails | Keep in core instructions or project memory ledger |
| `0.70` | **Cross-Module Workflow & Guardrails** | Multi-step verification recipes, coupling between distant directories, review gates not enforced by linters | Keep; disclose to scoped rule files if over 25 lines |
| `0.30` | **Convenient Pointer** | Single-line context pointer to a canonical config or deep reference doc | Keep only if it saves repeated multi-file searches |
| `0.00` | **Environment Cache (Redundant)** | Full directory trees, boilerplate tech stack lists ("Uses TypeScript and React"), copy-pasted script lists from `package.json`, rules already enforced by pre-commit/linter | **Prune immediately**; let the live environment serve as the single source of truth |

---

## Tri-Factor Composite Memory Utility

Grounded in **Generative Agents** (`arXiv:2304.03442`), rank every memory item by combining Freshness (`Retention`), Importance (`Importance`), and Exclusivity (`Exclusivity`):

### 1. Importance Scale (`Importance`)
- `1.00` (**Pinned Invariant**): Explicit user hard rule, security/data-safety boundary, or production guardrail. Exempt from automatic pruning.
- `0.80` (**Architectural Rule**): Cross-cutting module boundary, state-management convention, or testing standard.
- `0.60` (**Workflow Heuristic**): Tool flag preference, build/test shortcut, or debugging sequence.
- `0.30` (**Minor Preference / One-Off Note**): Narrow formatting tweak or situational note from a single session.

### 2. Composite Utility Formula (`Utility`)
`Utility = (0.40 * Retention) + (0.35 * Importance) + (0.25 * Exclusivity)`

### 3. Decision Thresholds
- `Utility >= 0.70`: **Promote / Retain in Core Memory** (high-value, fresh, unwritten knowledge).
- `0.45 <= Utility < 0.70`: **Consolidate or Move to Scoped Reference** (merge with sibling notes or move to path-specific rules).
- `Utility < 0.45` (or `Exclusivity == 0.00`): **Prune** from active instruction files.

---

## Core Instruction Token Budget and 1-In/1-Pruned Gate

Always-loaded workspace instruction files spend context tokens on every turn of every session:

1. **Token Estimation:**
   `Estimated_Tokens = Characters / 2.7`
2. **Default Core Budget:**
   `Max_Core_Tokens = 1500` (approximately `4,050` characters or `120 to 150` lines).
3. **80% Saturation Gate (`1,200` tokens):**
   Once core instructions exceed `80%` of `--budget`, enforce **Zero-Net-Bloat**: every new rule added to core instructions requires consolidating, disclosing, or pruning at least an equal number of tokens from existing rules.

---

## Five-Stage Competency Index (Dreyfus Progression)

Grounded in the **Dreyfus Model of Skill Acquisition** (Dreyfus & Dreyfus, 1980, 1986), project memory maturity advances across five objective engineering stages based on verified experience and instruction health.

### 1. Instruction Health Score (`Instruction_Health`)
`Instruction_Health = Verified_Live_Rules / Total_Active_Rules`
- A rule counts as `Verified_Live` only if all paths, scripts, and symbols it names exist in the workspace and its `Exclusivity > 0.00`.

### 2. Compounding Maturity Score (`Maturity_Score`)
`Maturity_Score = ((Verified_Sessions * 5) + (Grounded_Rules * 3) + (Consolidated_Patterns * 8)) * Instruction_Health`

- `Verified_Sessions`: Total sessions where continual learning and pruning completed.
- `Grounded_Rules`: Active rules with `Utility >= 0.65` and verified live paths.
- `Consolidated_Patterns`: Higher-order principles synthesized from 3 or more episodic session notes, or reusable workflow playbooks.

### 3. Five-Stage Calibration Rubric

| Stage | Maturity Label | Dreyfus Equivalent | Score Range | Gate Requirements & Operational Focus |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1** | **Baseline Capture** | Novice | `0 to 24` | Initial discovery. Captures primary build/test commands, top-level seams, and explicit user boundaries. |
| **Stage 2** | **Pattern Recognition** | Advanced Beginner | `25 to 59` | Recognizes recurring repo idioms and module couplings; eliminates environment caches (`Exclusivity = 0.0`). |
| **Stage 3** | **Autonomous Execution** | Competent | `60 to 119` | Requires `Instruction_Health >= 0.90` and at least `2` consolidated patterns. Plans multi-file changes with zero stale rules. |
| **Stage 4** | **Architectural Stewardship** | Proficient | `120 to 219` | Requires `Instruction_Health >= 0.92` and at least `5` consolidated patterns. Converts repeated human corrections into scoped rules or automated checks. |
| **Stage 5** | **Institutional Mastery** | Expert / Mastery | `220+` | Requires `Instruction_Health >= 0.95`, core tokens under budget, and zero stale drift. Maintains a compact, high-leverage institutional memory. |
