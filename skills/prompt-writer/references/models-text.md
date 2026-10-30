# Chat and Text Models

Read at Step 2 of [../SKILL.md](../SKILL.md) when the target is a chat or text model: writing, extraction, classification, translation, personas, system prompts.

## Detail slots (all text models)

Task, audience, purpose of the output, voice (with one example sentence), length, format, inputs (wrapped and labeled), constraints with a reason each, one or two examples of good output, and how to handle missing information.

### Claude

- **Fields and limits:** system prompt and user message. Long context; put long documents first and the question last.
- **Format:** clear sections in XML-style tags (`<context>`, `<instructions>`, `<examples>`, `<input>`). Explain the reason behind each rule, because Claude generalizes from the reason. Treat it as a capable new colleague with no context.
- **Detail slots:** the shared list above.
- **Negatives:** say what to do instead of what to avoid ("write in flowing prose paragraphs" in place of "no markdown"). Match the prompt's own style to the output style you want: a prompt with no markdown gets less markdown back.
- **Known failure modes:** without guidance it converges on generic, typical output, so name the defaults to steer away from. Newer models write dense, metaphor-heavy prose; the line "Please remove all mannered prose." helps. Newer models also format less, so drop old blanket "no bullets" rules and state when lists are useful instead. Opus 5 replies run long; ask for concision directly.
- **Source:** verified https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices and https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1

### GPT (ChatGPT, OpenAI API)

- **Fields and limits:** system or developer message, user message. API settings outside the prompt: `verbosity` (answer length) and `reasoning_effort`.
- **Format:** structured sections; XML-style spec blocks improve adherence. State the desired length in words.
- **Detail slots:** the shared list above.
- **Negatives:** allowed, but contradictions are costly.
- **Known failure modes:** contradictory or vague rules hurt GPT-5 more than other models, because it spends reasoning reconciling them; read the prompt once for conflicts. Overly forceful "be thorough" wording makes it overdo tool use. Markdown is off by default in the API; ask for it when wanted, and repeat in long chats.
- **Source:** verified https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide

### Gemini

- **Fields and limits:** system instruction and user content.
- **Format:** clear sections, the task stated plainly, examples for format.
- **Detail slots:** the shared list above.
- **Negatives:** prefer positive instructions.
- **Known failure modes:** not checked against a primary source here.
- **Source:** lead

### Open-weight and local models (Llama, Mistral, Qwen, others)

- **Fields and limits:** often a short context window and a fixed chat template that the runtime applies.
- **Format:** short, direct instructions; one or two examples matter more than long rules.
- **Detail slots:** the shared list above, trimmed to what fits.
- **Negatives:** prefer positive instructions.
- **Known failure modes:** smaller models follow fewer rules at once; keep to the five that matter most.
- **Source:** lead
