# Memory Ledger Schema, Verdict Taxonomy, and Report Format

## Contents

- Purpose and Workflow Link
- Portable Project Memory Ledger Schema (`.agents/compound-memory.md`)
- Calibrated 6-Level Verdict Taxonomy
- Standard Session Compounding and Pruning Report Template

---

## Purpose and Workflow Link

This reference defines the file structure for `.agents/compound-memory.md`, the 6-level calibration verdict taxonomy, and the user-facing report template used in Steps 5 and 6. For the primary workflow sequence, see [../SKILL.md](../SKILL.md).

---

## Portable Project Memory Ledger Schema (`.agents/compound-memory.md`)

Maintain the project's compounding memory ledger at `.agents/compound-memory.md` (creating `.agents/` if absent). Keep this file clean, human-readable, and under `300` lines by pruning decayed entries during Step 4.

```markdown
# Project Compound Memory Ledger

**Last Updated:** YYYY-MM-DD  
**Verified Sessions:** <Integer>  
**Competency Stage:** Stage <1-5> - <Stage Name>  
**Maturity Score:** <Score>  
**Instruction Health:** <Verified Rules> / <Total Rules> (<Percentage>%)  
**Core Token Load:** <Characters> / 2.7 = <Estimated Tokens> tokens (Budget: <Budget>)

---

## 1. Pinned Invariants (Protected Core Rules)

| ID | Rule & Positive Target Behavior | Target Scope | Verified Session | Stability (`S`) |
| :--- | :--- | :--- | :--- | :--- |
| `INV-01` | <Non-negotiable architectural or safety invariant> | `<path or global>` | `Session #N` | `<S>` |

---

## 2. Active Compounded Rules & Architecture Seams

| ID | Learned Principle / Seam | Channel | Scope / Path | Sessions Since Verified | Stability (`S`) | Freshness (`R`) | Value (`U`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `MEM-01` | <Positively framed rule or hidden seam> | `Correction / Bug / Seam / Workflow` | `<file or module>` | `0` | `10` | `1.00` | `0.93` |

---

## 3. Consolidated Workflow Patterns

- **<Pattern Name> (`<trigger scope>`):** <1-to-3 line deterministic command or verification sequence synthesized from multiple sessions>

---

## 4. Pruning & Consolidation Changelog (Last 5 Sessions)

- **YYYY-MM-DD (Session #N):** Added `<count>` lessons, consolidated `<count>` notes into `<rule>`, pruned `<count>` stale/cache items (`<net token delta>` tokens).
```

---

## Calibrated 6-Level Verdict Taxonomy

Select exactly one verdict for the session report based on the actions executed:

| Verdict | When to Assign |
| :--- | :--- |
| **`Compounded & Pruned`** | Extracted 1 or more verified session lessons AND pruned stale rules, environment caches, or no-ops, leaving Instruction Health at `95%+` and tokens within budget. |
| **`Fine-Tuned With Consolidations`** | Merged scattered episodic notes into consolidated principles or positively reframed rules without needing new external deletions. |
| **`Pruned Stale Drift`** | No new session lessons were added (`--mode=prune` or clean session), and 1 or more broken paths, environment caches, or decayed rules were evicted. |
| **`Promoted To Scoped Reference`** | Core instructions exceeded or approached the token budget, and detailed branch rules were extracted into scoped rule files with context pointers. |
| **`Baseline Initialized`** | First run in a workspace with no prior `.agents/compound-memory.md`; initialized Stage 1 ledger and grounded baseline workspace instructions. |
| **`Confirmation Needed On Invariants`** | Safe refinements are ready, and 1 or more Pinned Invariants (`Importance = 1.0`) or major user-authored sections require explicit user approval before removal or rewrite. |

---

## Standard Session Compounding and Pruning Report Template

Render the user-facing report in chat using this plain-language structure:

```markdown
## Compound Learn Verdict: `<Verdict Label>`

**Project Memory Maturity:** Stage `<1-5>` (`<Stage Label>`) | **Maturity Score:** `<Calculation> = <Score>`  
**Instruction Health:** `<Verified Live Rules> / <Total Active Rules> = <Percentage>%` (Target: `95% to 100%`)  
**Core Token Load:** `<Characters> / 2.7 = <After Tokens> tokens` (Before: `<Before Tokens> tokens`, Delta: `<Tokens Saved>` tokens, Budget: `under <Budget>`)

---

### 1. New Lessons Compounded This Session

| Lesson ID | New Lesson From This Session | Evidence / Root Cause | Target File & Line | Rule Value Score |
| :--- | :--- | :--- | :--- | :--- |
| `MEM-XX` | <Plain-language positive rule> | <User correction, bug fix, or seam discovered> | `path/to/file.md:1-10` | `(0.40 * <R>) + (0.35 * <I>) + (0.25 * <E>) = <U>` |

*(If no new lessons were added in this pass, write: `No new lessons added in this pass; focused on pruning and instruction health.`)*

---

### 2. Stale Data Pruned & Instructions Fine-Tuned (Before -> After)

| Action | Location | Before (Stale, Cached, or Negative) | After (Refined Positive Rule or Pruned) | Reason & Freshness Math |
| :--- | :--- | :--- | :--- | :--- |
| `Pruned Cache` / `Reframed` / `Consolidated` / `Fixed Path` | `path/to/file.md:10-20` | `<Original text snippet>` | `<Replacement text or Removed>` | `<Plain-language reason + exp(- t / S) = Freshness>` |

---

### 3. Next High-Leverage Learning Target

- **<Focus Area>:** <1 sentence naming the next blind spot, unverified module boundary, or mechanical rule ready to become an automated check.>
```
