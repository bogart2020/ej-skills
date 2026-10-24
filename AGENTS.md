# Authoring Rules for `ej-skills`

Personal AI plugin and skill repository designed for universal compatibility across **Claude Desktop**, **Claude Code**, **OpenAI Codex**, **GitHub Copilot (CLI and VS Code)**, **Google Antigravity (AGY)**, **Gemini CLI**, and **`skills.sh`** (Cursor, Windsurf, OpenCode, Devin, Amp, Pi).

## Repository layout

Keep all skills in a flat directory under `skills/<skill-name>/`:

```text
skills/<skill-name>/
├── SKILL.md              # Required: agentskills.io frontmatter + instructions
├── agents/
│   └── openai.yaml       # Required: OpenAI Codex UI metadata and invocation policy
└── references/           # Optional: Disclosed reference docs reached by pointer
```

A flat `skills/<skill-name>/SKILL.md` tree is required so Google Antigravity, Gemini CLI (`--path skills`), `.claude-plugin/plugin.json`, and `skills.sh` all resolve every skill from a single path.

## Adding or modifying a skill

Whenever you add, rename, or update a skill under `skills/`:

1. **Follow `writing-for-agents`**:
   - Front-load trigger branches in `description` (for model-invoked skills) with one trigger per branch.
   - Give every procedural step a checkable, exhaustive **completion criterion**.
   - Keep universal steps and core rules in `SKILL.md`; push branch-specific reference into `skills/<skill-name>/references/`.
   - Frame instructions positively and avoid em-dashes in prose.
   - **Keep every skill 100% standalone and self-contained**: never reference, route to, or depend on another sibling skill or another skill's files inside `skills/<skill-name>/`, because users frequently install a single `.zip` archive in Claude Desktop or a single skill via `npx skills@latest add bogart2020/ej-skills --skill=<skill-name>`.
2. **Keep invocation metadata synchronized**:
   - **Model-invoked** (default): omit `disable-model-invocation` in `SKILL.md` and omit `policy` in `agents/openai.yaml`.
   - **User-invoked only**: set `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
3. **Update manifests and documentation**:
   - Register `./skills/<skill-name>` in `.claude-plugin/plugin.json` under `"skills"`.
   - Keep `version` omitted from `.claude-plugin/plugin.json` so Claude Code uses the git commit SHA as the version and auto-updates on every push.
   - Keep root `plugin.json` restricted strictly to Google Antigravity's supported top-level keys (`name`, `displayName`, `version`, `description`, `logo`, `suggestedPrompts`, `disabled`).
   - Add the skill to `README.md` with its link and invocation type.
4. **Rebuild Claude Desktop zip archives**:
   - Run `bash scripts/package-skills.sh` to regenerate `<skill-name>.zip` at the repository root for **Claude Desktop** (`Settings -> Capabilities -> Skills -> Upload skill`).
