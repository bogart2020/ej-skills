# prompt-writer: Design Spec

**Date:** 2026-10-30
**Research:** `research/2026-10-30-ai-slop-detection-and-anti-slop-prompting-best-practices.md` (sections 1 to 4, plus Addendum section 5)
**Status:** Approved in design interview (2026-10-30)

## Purpose

Write a prompt for any AI model on any topic, or sharpen a prompt the user already has, so the target model returns specific, non-typical, unbiased output. Avoiding the generic AI look and sound (stock words, sentence shapes, fonts, gradients, waxy faces, default demographics) is the built-in quality check, not a separate job.

## Decisions

| # | Decision | Value |
| :--- | :--- | :--- |
| D1 | Name | `prompt-writer` |
| D2 | Invocation | Model-invoked (no `disable-model-invocation`, no `policy` in openai.yaml); `/prompt-writer` also works |
| D3 | Scope | Public: `.claude-plugin/plugin.json`, root `plugin.json` suggestedPrompts, `README.md` |
| D4 | Jobs | Main: write a new prompt. Second: improve a prompt the user pastes, for the same model. Cleanup of general essays, emails, or web pages is out of scope |
| D5 | Coverage | One general method for any model, plus seven profile groups: text and chat; agents and coding; image generation; image editing with references; video; audio; 3D and other generators |
| D6 | Target model | When the user has not named the model, ask one question: which model will run the prompt ("Not sure" yields a model-neutral prompt) |
| D7 | Unknown or new model | Open its official prompt guide if browsing is available; otherwise use the general method, state the assumption in one line |
| D8 | Input surface first | Before writing, map the target's fields and limits: separate boxes (system and user, style and lyrics, positive and negative), character caps, settings that live outside the prose (aspect ratio, duration, seed), whether negatives are supported and in what form |
| D9 | Output | Copy-ready prompt in a code block per field, in the target's native format, then a "Choices I made" list of every detail that replaced a typical default, then any setting to change outside the prompt |
| D10 | People | When people appear and the user did not describe them, choose specific, plausible, non-stereotyped age, ethnicity, body type, gender, and setting that fit the brief; list them under "Choices I made" |
| D11 | Variety | Open creative briefs only: privately sketch five unusual directions, pick the most specific fitting one, name the other four in one line |
| D12 | User choices win | Every detail the user fixed appears verbatim; the skill fills only what the user left open. A user who asks for the typical look (stock photo, corporate tone) gets it |
| D13 | Sets | Storyboards, character sheets, multi-shot, and series prompts repeat one locked description of each character and style word for word in every prompt |
| D14 | Rights and safety | Real people: assume the user's own or permitted photos; decline deceptive, sexual, or harassing depictions of real people and any sexual content involving minors. Named living artists or copyrighted characters: describe the visual traits instead of the name |
| D15 | Language | Text meant to appear in the output (signs, lyrics, captions) is kept exactly as given, in its own language and script, in quotes |
| D16 | Files | `SKILL.md`, `agents/openai.yaml`, `references/slop-patterns.md`, `references/models-text.md`, `references/models-agents.md`, `references/models-image.md`, `references/models-image-edit.md`, `references/models-video.md`, `references/models-audio.md`, `references/models-3d-other.md` |
| D17 | Verification | Blind fresh Haiku subagent runs with project instructions neutralized, before (baseline) and after the skill; loop until clean; then commit to `main` |

## Final check

1. **Slop scan:** the prompt's own words, and any text it asks the target to write, contain no pattern from `slop-patterns.md` (unless D12 says the user wants it).
2. **Fit check:** every field matches the target's format, each field is under its character cap (count shown), negatives use the target's supported form.
3. **Choices check:** every user-fixed detail is present verbatim; every open slot has a value a reader could not guess from the topic alone.
