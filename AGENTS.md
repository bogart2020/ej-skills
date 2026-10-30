# AGENTS.md

Authoring rules for `ej-skills`, a personal skill repository that must work in Claude Desktop, Claude Code, OpenAI Codex, GitHub Copilot (CLI and VS Code), Google Antigravity (AGY), Gemini CLI, and `skills.sh` (Cursor, Windsurf, OpenCode, Devin, Amp, Pi). `CLAUDE.md` is a symlink to this file.

## 1. One Flat Skill Tree

**Every harness resolves skills from one path. Keep it flat.**

```text
skills/<skill-name>/
├── SKILL.md              # Required: agentskills.io frontmatter + instructions
├── agents/
│   └── openai.yaml       # Required: OpenAI Codex UI metadata and invocation policy
└── references/           # Optional: Disclosed reference docs reached by pointer
```

- Google Antigravity, Gemini CLI (`--path skills`), `.claude-plugin/plugin.json`, and `skills.sh` all read `skills/<skill-name>/SKILL.md` directly.

## 2. Standalone Skills

**Users install one skill at a time. Each skill works alone.**

- Never reference, route to, or depend on a sibling skill or its files. Users install a single `.zip` in Claude Desktop or a single skill via `npx skills@latest add bogart2020/ej-skills --skill=<skill-name>`.
- Never point a skill at repo-only files (`AGENTS.md`, `README.md`, `research/`, `scripts/`, `docs/`, `*-stress-test-report.md`) or local machine paths.
- Every relative link resolves inside the skill's own folder.

## 3. Write for Agents, Answer in Plain Language

**Technical terms live in instructions. Users get plain language.**

- Use only the Agent Skills frontmatter keys: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` (plus `disable-model-invocation` for user-invoked skills). Claude Desktop rejects any other key.
- Never put `anthropic` or `claude` in `name`, or `<` / `>` in `name` or `description`.
- Keep `SKILL.md` under 500 lines and about 13,500 characters (about 5,000 tokens). Put the step sequence and hard rules first: Claude Code keeps only the first 5,000 tokens of a skill after compaction.
- Follow `writing-for-agents`: front-load trigger branches in `description` (model-invoked skills), one trigger per branch.
- Give every procedural step a checkable, exhaustive completion criterion.
- Keep universal steps and core rules in `SKILL.md`; push branch-specific reference into `references/`, with each pointer naming when to read the file. A reference over 100 lines opens with a `## Contents` list.
- Frame instructions positively and avoid em-dashes in prose.
- Name looks, styles, and recipes with neutral descriptive labels, never after real people, their handles, sites, or paid presets. Author names belong only in source citations.
- Every skill keeps a `## Plain-language output` section that tells the agent to answer per ISO 24495-1:2023 (relevant, findable, understandable, usable): map each internal term to a user-facing label, show math as labeled plain arithmetic, and explain any unavoidable technical term in a short clause on first use.

## 4. Keep Metadata in Sync

**Every harness reads its own manifest. Update all of them together.**

- Model-invoked (default): omit `disable-model-invocation` in `SKILL.md` and omit `policy` in `agents/openai.yaml`.
- User-invoked only: set `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
- Keep `interface.short_description` in `agents/openai.yaml` between 25 and 64 characters.
- Register `./skills/<skill-name>` in `.claude-plugin/plugin.json` under `"skills"`. Omit `version` there and in every `.claude-plugin/marketplace.json` plugin entry so Claude Code versions by commit SHA and auto-updates on every push.
- Root `plugin.json` serves Agent Plugins 1.0.0 (Codex) and Google Antigravity: keep `"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"`, use only Antigravity v1 keys (`name`, `displayName`, `description`, `version`, `disabled`, `logo`, `suggestedPrompts`, `skills`, `author`, `homepage`, `repository`, `license`, `keywords`, `extensions`), and at most 3 `suggestedPrompts`.
- When adding or removing a skill, rework the 3 `suggestedPrompts` so every skill still appears in one of them (merge related skills into one prompt).
- List the skill in `README.md` with its link and invocation type.

## 5. Zips Are Build Output

**Claude Desktop installs from this repo as a marketplace. The repo never stores zips.**

- Primary Claude Desktop route: `Customize > Plugins > Add > Add marketplace`, then `bogart2020/ej-skills`.
- Single-skill route: `bash scripts/package-skills.sh` builds `dist/<skill-name>.zip` for `Customize > Skills > + > Create skill > Upload a skill`.
- Never commit a `.zip`; `dist/` is git-ignored.

## 6. Ground and Test Every Skill

**Research before writing, test before shipping.**

- Save primary-source research to `research/YYYY-MM-DD-<slug>-best-practices.md`. `research/` is git-ignored and stays on the author's machine.
- Save design specs to `docs/superpowers/specs/` and implementation plans to `docs/superpowers/plans/`. Keep local machine paths out of them; the pre-commit hook blocks them.
- Test with blind runs on a weak model (such as Claude Haiku) told to ignore this file: once without the skill as a baseline, then with it until every scenario passes.
- Record the scenarios, baseline and final pass rates, and each fix in `<skill-name>-stress-test-report.md` at the repo root.

## 7. Keep This File Current

**Update this file when it would otherwise be wrong. Not otherwise.**

- Update it in the same change when you add a repo-wide convention, rename or move a path it names, change a script or manifest it describes, or find a rule here is wrong.
- Skip it for content edits inside a single skill.
- Edit `AGENTS.md` only; `CLAUDE.md` follows through the symlink.
- Keep this style: numbered principle headings, one bold summary line, short imperative bullets. Replace or delete stale rules instead of appending new ones.

---

**These rules are working if:** every skill installs and runs alone, no harness misses a skill, and users never see a term they would have to look up.
