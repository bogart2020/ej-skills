# AGENTS.md

Authoring rules for `ej-skills`, a personal skill repo for Claude Desktop, Claude Code, OpenAI Codex, GitHub Copilot, Google Antigravity, Gemini CLI, and `skills.sh` (Cursor, Windsurf, OpenCode, Devin, Amp, Pi). `CLAUDE.md` is a symlink to this file; edit `AGENTS.md` only.

## 1. One Flat Skill Tree

**Every harness reads `skills/<skill-name>/SKILL.md` directly. Keep it flat.**

```text
skills/<skill-name>/
├── SKILL.md              # Required: frontmatter + instructions
├── agents/openai.yaml    # Required: Codex UI metadata and invocation policy
├── references/           # Optional: reference docs reached by pointer
└── scripts/              # Optional: helper code, run by path relative to SKILL.md's folder
```

- Scripts depend only on the Python standard library, `numpy`, and `pillow` (preinstalled in Claude's code sandbox); treat anything else as optional with a fallback.

## 2. Standalone Skills

**Users install one skill at a time. Each skill works alone.**

- Never reference or depend on a sibling skill or its files.
- Never point a skill at repo-only files (`AGENTS.md`, `README.md`, `research/`, root `scripts/`, `docs/`, `*-stress-test-report.md`) or local machine paths. Every relative link stays inside the skill's folder.

## 3. Write for Agents, Answer in Plain Language

**Technical terms live in instructions. Users get plain language.**

- Frontmatter keys: only `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`, plus `disable-model-invocation` for user-invoked skills. Claude Desktop rejects others.
- No `anthropic` or `claude` in `name`; no `<` or `>` in `name` or `description`.
- `SKILL.md` stays under 500 lines and about 13,500 characters, with steps and hard rules first: Claude Code keeps only the first 5,000 tokens after compaction.
- Follow `writing-for-agents`: front-load trigger branches in `description`, one trigger per branch.
- Give every step a checkable completion criterion.
- Keep core steps in `SKILL.md`; move branch-specific detail to `references/`, each pointer saying when to read it. A reference over 100 lines opens with `## Contents`.
- Frame instructions positively; no em-dashes in prose.
- Name looks and styles with neutral labels, never after real people, handles, sites, or paid presets. Author names appear only in source citations.
- Every skill has a `## Plain-language output` section (ISO 24495-1:2023): map internal terms to user-facing labels, show math as labeled plain arithmetic, explain unavoidable terms on first use.

## 4. Keep Metadata in Sync

**Every harness reads its own manifest. Update them together.**

- Model-invoked (default): omit `disable-model-invocation` and the `policy` block. User-invoked: set `disable-model-invocation: true` and `policy.allow_implicit_invocation: false`.
- `interface.short_description` in `agents/openai.yaml`: 25 to 64 characters.
- Register `./skills/<skill-name>` in `.claude-plugin/plugin.json`. Omit `version` there and in `.claude-plugin/marketplace.json` entries, so Claude Code updates on every push.
- Root `plugin.json` (Codex and Antigravity): keep the Agent Plugins 1.0.0 `$schema`, use only Antigravity v1 keys (`name`, `displayName`, `description`, `version`, `disabled`, `logo`, `suggestedPrompts`, `skills`, `author`, `homepage`, `repository`, `license`, `keywords`, `extensions`), and keep exactly 3 `suggestedPrompts` that together name every skill.
- List each skill in `README.md` with its link and invocation type.
- Never commit a `.zip`. `bash scripts/package-skills.sh` builds `dist/<skill-name>.zip` (git-ignored) for single-skill upload in Claude Desktop.

## 5. Ground and Test Every Skill

**Research before writing, test before shipping.**

- Save research to `research/YYYY-MM-DD-<slug>-best-practices.md` (git-ignored, local only). Save specs and plans to `docs/superpowers/specs/` and `docs/superpowers/plans/`, with no local paths.
- Test with blind runs on a weak model (such as Claude Haiku) told to ignore this file: once without the skill as a baseline, then with it until every scenario passes.
- Record scenarios, pass rates, and fixes in `<skill-name>-stress-test-report.md` at the repo root.

## 6. Keep This File Current

**Update this file when it would otherwise be wrong. Not otherwise.**

- Update it in the same change when you add a repo-wide convention, move a path it names, change a script or manifest it describes, or find a rule wrong. Skip it for edits inside one skill.
- Keep this style: numbered headings, one bold summary line, short imperative bullets. Replace stale rules instead of appending.

---

**These rules are working if:** every skill installs and runs alone, no harness misses a skill, and users never see a term they would have to look up.
