# Agents and Coding Tools

Read at Step 2 of [../SKILL.md](../SKILL.md) when the target acts with tools: coding agents, research and browser agents, multi-step chains, or a prompt that will write other prompts.

## Detail slots (all agents)

1. **Goal:** the outcome in one sentence, with the reason it matters.
2. **Scope:** which files, folders, pages, or sources to touch, and which to leave alone.
3. **Context:** stack, conventions, and existing patterns to follow ("match the existing CSS variables in `theme.css`").
4. **Constraints:** each with its reason.
5. **Done check:** an observable result that proves the work is finished (a passing test, a command's output, a screenshot state).
6. **Verification:** the exact command or step to run before claiming success.
7. **Stop and ask:** what to do when blocked or when a choice is the user's to make.
8. **Report:** what to return at the end, and how long.

### Coding agents (Claude Code, Codex, Cursor, Copilot, others)

- **Fields and limits:** one task message; persistent project rules live in the tool's instruction file.
- **Format:** goal first, then the slots above as short sections. Ask it to look at the codebase before choosing an approach.
- **Detail slots:** the list above. For UI work add the design slots from `slop-patterns.md`.
- **Negatives:** state allowed and off-limits actions plainly ("leave the API layer unchanged").
- **Known failure modes:** without a done check it stops early or over-claims; without scope it rewrites too much; heavy "be thorough" wording makes newer models over-explore. Name the tests to add and run.
- **Source:** verified https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (agentic sections) and https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide (stop conditions, scoped specs)

### Research and browser agents

- **Fields and limits:** one task message, sometimes a source allow-list.
- **Format:** the question, the kinds of sources to trust (official docs, primary data), how recent they must be, how to handle disagreement, and the output shape with citations.
- **Detail slots:** the list above, with "sources" as the scope.
- **Negatives:** list sources to skip by type.
- **Known failure modes:** summarizing secondary blogs as fact; stopping at the first answer. Ask for each claim's source link.
- **Source:** lead

### Multi-step chains and prompts that write prompts

- **Fields and limits:** one prompt per step.
- **Format:** give each step one job and a fixed output format the next step reads. For a prompt-writing prompt, give the target model, the slot list, and one example of a finished prompt.
- **Detail slots:** per step: input, job, output format, check.
- **Negatives:** none special.
- **Known failure modes:** steps drift when the hand-off format is loose.
- **Source:** lead
