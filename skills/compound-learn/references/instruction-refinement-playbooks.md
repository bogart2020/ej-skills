# Instruction Refinement and Pruning Playbooks

## Contents

- Purpose and Workflow Link
- Playbook 1: Extracting High-Signal Session Deltas (Reflexion Loop)
- Playbook 2: Purging Stale Drift, Environment Caches, and No-Ops
- Playbook 3: Semantic Consolidation (Episodic Notes to Principles)
- Playbook 4: Positive Reframing and Leading-Word Compression
- Playbook 5: Progressive Disclosure into Scoped Rule Files
- Playbook 6: Converting Mechanical Rules into Deterministic Checks

---

## Purpose and Workflow Link

This reference provides step-by-step transformation playbooks for Step 2 (Delta Extraction) and Step 4 (Instruction Fine-Tuning and Sediment Pruning). For the primary workflow sequence, see [../SKILL.md](../SKILL.md).

---

## Playbook 1: Extracting High-Signal Session Deltas (Reflexion Loop)

When reviewing a session transcript, git diff, or user correction history, separate **durable project knowledge** from **ephemeral task state**:

| Signal Type | Ephemeral Task Noise (Discard) | Durable Compounding Lesson (Extract) |
| :--- | :--- | :--- |
| **User Correction** | "Fix the typo on line 42 of `auth.ts`." | "Always validate JWT expiry in `src/middleware/auth.ts` using UTC timestamps before session lookup." |
| **Command / Tool Failure** | "Ran `npm test` and fixed a missing semicolon." | "Run `pnpm --filter @app/core test:unit` for unit tests; root `npm test` triggers slow end-to-end containers." |
| **Navigation Discovery** | "Read 6 files to find the billing webhook." | "Billing webhook handlers live in `packages/payments/src/webhooks/` and require signature verification via `verifyStripeSig`." |
| **Architectural Constraint** | "Added a button to the settings modal." | "State mutations in `src/store/` must dispatch through domain actions rather than mutating slice fields directly." |

**Extraction Checklist:**
1. State the exact module, directory, or command scope.
2. Pair the action with the one-clause reason or failure mode it prevents.
3. Verify the path or command exists right now before recording.

---

## Playbook 2: Purging Stale Drift, Environment Caches, and No-Ops

Audit every line of existing workspace instruction files against four pruning filters:

### Filter A: Dead Path and Command Verification
- Extract every inline path (`src/...`, `packages/...`, `bin/...`) and command (`npm run ...`, `make ...`, `pytest ...`).
- Check existence via file lookup or manifest inspection.
- **Action:** If a file moved, update the path pointer in place. If the feature or script was deleted, prune the rule completely.

### Filter B: Environment Cache Purge (`Exclusivity = 0.0`)
- Identify blocks that copy information directly from the filesystem or package configs:
  - ASCII directory trees (`src/ -> components/, utils/, hooks/`).
  - Dependency lists copied from `package.json` or `pyproject.toml`.
  - Standard framework defaults that have no project-specific customization.
- **Action:** Delete the cached block. If a specific directory has a non-obvious purpose, keep a single-line context pointer naming only the non-obvious seam.

### Filter C: Model No-Op Elimination
- Test each sentence: *Does this instruction change agent behavior compared to the model's default baseline?*
- Examples of **No-Ops** to delete in full:
  - "Write clean, maintainable, and well-structured code."
  - "Think carefully before answering and avoid making mistakes."
  - "Follow best practices for error handling and security."
- **Action:** Delete the entire sentence, or replace it with the specific repository rule (for example, "Return typed `Result<T, AppError>` objects from all service methods in `src/services/`").

### Filter D: Duplicate Rule Collapse
- When the same rule appears in multiple sections or across root and subdirectory files, keep it in the single most specific location and remove all copies.

---

## Playbook 3: Semantic Consolidation (Episodic Notes to Principles)

When session-by-session learning accumulates 3 or more granular notes on the same topic, synthesize them into one unified principle:

### Before Consolidation (Scattered Episodic Sediment, 58 tokens):
- *Session 2 note:* "When adding a new API route, remember to register the Zod schema in `src/api/schemas.ts`."
- *Session 5 note:* "API routes in `src/api/routes/` failed review because error responses did not use `ApiError`."
- *Session 8 note:* "Make sure every new endpoint in `src/api/routes/` has an integration test in `tests/api/`."

### After Consolidation (Single Co-Located Rule, 26 tokens):
- **API Endpoint Contract (`src/api/routes/`):** Validate inputs via a registered schema in `src/api/schemas.ts`, return errors via `ApiError`, and pair every route with a test in `tests/api/`.

---

## Playbook 4: Positive Reframing and Leading-Word Compression

Negative prohibitions ("do not", "never", "avoid") activate the banned tokens in smaller models and increase instruction drift. Rewrite every rule into an affirmative target behavior anchored by a compact leading word:

| Negative / Verbose Original | Positively Framed & Compressed Replacement |
| :--- | :--- |
| "Do not use `moment.js` or native `Date` parsing anywhere in the frontend; never format dates manually." | "**Date handling:** Use `date-fns` helpers in `src/lib/dates.ts` for all parsing and formatting." |
| "Never commit directly to main or push without running the typechecker and unit tests first." | "**Pre-push gate:** Run `pnpm typecheck && pnpm test:unit` until green before every commit." |
| "Do not scatter database queries inside controller files; keep controllers thin." | "**Data access seam:** Place all SQL and ORM queries inside `src/repositories/`; controllers call repository methods only." |

---

## Playbook 5: Progressive Disclosure into Scoped Rule Files

Root instruction files load on every turn regardless of task. When a section applies only to a specific subsystem, file extension, or occasional workflow:

1. **Check the 25-Line Branch Rule:** Any topic block exceeding 25 lines that only applies to a subset of tasks (such as database migrations, UI component styling, or release publishing) belongs outside the root instruction file.
2. **Extract to Scoped Rules or Disclosed Docs:**
   - Move path-specific rules into `.claude/rules/<domain>.md` or `.agents/rules/<domain>.md` (with path globs where supported) or `docs/<domain>.md`.
   - Leave a single-line **context pointer** in the root file that front-loads the trigger condition:
     `For database schema changes or migrations, read .agents/rules/database-migrations.md.`

---

## Playbook 6: Converting Mechanical Rules into Deterministic Checks

At **Stage 4 (Architectural Stewardship)** and **Stage 5 (Institutional Mastery)**, audit whether recurring human corrections are mechanical:

- **Mechanical Rule:** Enforces a fixed syntax pattern, import restriction, file naming convention, or formatting rule.
  - *Action:* Recommend encoding the check into the project's linter, typechecker, or pre-commit script, and remove the prose rule once the automated guardrail is active.
- **Judgment Rule:** Requires architectural trade-off evaluation, domain modeling, or cross-module design coherence.
  - *Action:* Retain as a high-signal principle in the workspace instructions.
