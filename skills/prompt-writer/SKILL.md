---
name: prompt-writer
description: Write or sharpen prompts for any AI model on any topic, with specific, non-generic detail. Use when writing a prompt for a chat model, system prompt, or agent, writing an image, photo-edit, face swap, or character-consistency prompt, writing a video, music, voice, or 3D prompt, or improving a prompt that gives generic, biased, or AI-looking results.
license: MIT
---

# Prompt Writer

Write a prompt for any AI model, or sharpen one the user already has, so the model returns specific, unusual, unbiased output instead of its most typical answer. Models drift toward the most common answer because their training rewards familiar output. A prompt beats that drift by fixing every detail the model would otherwise pick on its own.

## Steps

Work through the steps in order. Each ends with a **Done when** check.

### Step 1: Understand the request

Find five things: the **target model**, the **medium** (text, agent, image, image edit, video, audio, 3D or other), the **purpose** (where the result will be used), the **details the user already fixed**, and whether this is a **new prompt** or an **improvement** of a pasted one.

- Tool type named but not the tool ("a coding agent", "a chatbot", "an LLM"): for chat, text, and agent prompts, the prompt barely changes between tools. Skip the question and write a model-neutral prompt for that type.
- Target model unknown otherwise: reply with exactly one question and stop. Use this wording: "Which AI tool will run this prompt? For example ChatGPT, Claude, Gemini, Midjourney, Flux, Stable Diffusion, Veo, Sora, Suno, or ElevenLabs. If you are not sure, say so and I will write one that works anywhere." Ask nothing else in that reply, and write no prompt yet.
- User answers "not sure": write a model-neutral prompt in plain sentences, with no tool-specific syntax.
- Everything else unclear (purpose, mood, style): decide it yourself in Step 3 and show it under "Choices I made". Ask no further questions.

**Done when:** all five are known, or the one model question is sent.

### Step 2: Map the input surface

Load the profile file for the medium:

| Medium | Read |
| :--- | :--- |
| Chat or text model | [references/models-text.md](references/models-text.md) |
| Agent that uses tools: coding, browsing, research, multi-step | [references/models-agents.md](references/models-agents.md) |
| Image from text | [references/models-image.md](references/models-image.md) |
| Edit or reuse photos the user supplies (face swap, try-on, restyle) | [references/models-image-edit.md](references/models-image-edit.md) |
| Video, lip-sync, avatars | [references/models-video.md](references/models-video.md) |
| Songs, speech, sound effects | [references/models-audio.md](references/models-audio.md) |
| 3D, app or UI builders, slides, anything else | [references/models-3d-other.md](references/models-3d-other.md) |

From the profile, list in your thinking: the **fields** (one box, or several such as system and user, style and lyrics, positive and negative), each field's **character limit**, how **exclusions** work (a separate negative field, plain listed items, or positive description only), and **settings outside the prompt** (aspect ratio, duration, seed, voice, model version).

- Model not in any profile: if you can browse, open the model's official prompt guide and use it. Otherwise use the "Anything else" block in `models-3d-other.md`, and say in one line of the reply: "I have no tips on file for <model>, so I assumed <assumption>." Use only syntax you found in a profile or an official guide.

**Done when:** fields, limits, exclusion form, and outside settings are listed.

### Step 3: Fill every detail

Take the profile's **Detail slots** and give each one a value:

1. **User-fixed details go in word for word.** Keep the user's exact terms ("85mm", "red coat"), even when you would choose differently.
2. **Open slots get a specific choice** a reader could not guess from the topic alone. Swap "a woman in a cafe" for "a woman in her late 50s with cropped grey hair, wiping down a zinc counter at closing time". Name materials, light source and direction, lens, era, texture, small imperfections, and for text the audience, voice, and one concrete example.
3. **People:** when people appear and the user did not describe them, choose a specific, believable age, ethnicity, build, gender, and setting that fit the brief. Avoid stereotypes, such as tying a job, a skill, or a setting to one group. List the choices so the user can swap them.
4. **Open creative briefs** (album covers, posters, stories, concept art, songs): in your thinking, sketch five unusual directions that a typical answer would not take. Pick the most specific one that still fits the brief. In the reply, name the other four in one line.
5. **The user wants the typical look** ("generic stock photo", "standard corporate tone"): give them the conventional version done well. The specificity rule still applies to light, framing, and usage, with no unusual twist.
6. **Sets** (storyboards, multi-shot video, character sheets, series): write one locked description of each character, place, and style. Paste it word for word into every prompt in the set, and change only the action, camera, or moment.
7. **Text that must appear in the output** (signs, captions, lyrics, labels): keep it exactly as given, in its own language and script, inside quotation marks.
8. **Exclusions:** write them the way the profile says. When the model has no negative field, describe what should be there instead ("an empty, quiet street" in place of "no cars").

**Done when:** every slot holds the user's value or a specific choice.

### Step 4: Write the prompt

Write each field in the model's native format from the profile. Put the most important details first, because some tools shorten or rewrite long prompts. Count the characters of every field that has a limit. When a field is over its limit, cut the least specific words first and keep every user-fixed detail.

**Improving a pasted prompt:** keep its model, intent, and every concrete detail. Remove filler quality tags ("masterpiece", "8k", "best quality", "ultra detailed", "trending"), replace vague words with specific ones, and move parts into the right fields.

**Done when:** every field is written and fits its limit.

### Step 5: Final check

Read [references/slop-patterns.md](references/slop-patterns.md), then check:

1. **Generic-pattern scan:** the prompt's own words, and any text it asks the model to write (lyrics, copy, dialogue, bot replies), contain no pattern from the file, unless the user asked for the typical look.
2. **Fit check:** every field matches the model's format, each limited field shows its count under the limit, and exclusions use the model's supported form.
3. **Choices check:** every user-fixed detail is present word for word, and every open slot has a specific value.

**Done when:** all three pass. A failure sends you back to Step 3 for the slots involved.

### Step 6: Reply

Use this order, and leave out sections that are empty:

1. One fenced code block per field. Put a bold label above each block, with the count when the field has a limit: **Style** (412 / 1000 characters).
2. **Choices I made:** one short bullet per detail you chose in place of the model's default, people details included.
3. **Other directions:** one line naming the four unused ideas (open creative briefs only).
4. **Settings outside the prompt:** aspect ratio, duration, voice, or seed to set in the tool.
5. For an improved prompt, **What changed:** one bullet per change.

## Hard rules

- Real people: assume photos of the user or people who agreed. Write no prompt that shows a real, identifiable person in a deceptive, sexual, or humiliating scene, or doing something they did not do. Say why in one sentence and offer a legitimate option, such as an invented character or clearly labeled satire.
- Write no sexual content involving anyone under 18 or anyone described as childlike.
- Named living artists or copyrighted characters: describe the visual traits (palette, brushwork, lighting, shapes, era) in place of the name.
- Use only tool syntax from a profile or an official guide.
- Keep every detail the user fixed.

## Plain-language output

The reply is for a non-specialist. Use these labels in place of internal terms:

| Internal term | Say to the user |
| :--- | :--- |
| Input surface, fields | the boxes and limits the tool gives you |
| Detail slot | detail |
| Typical default | what the tool would pick on its own |
| Profile | tips for that tool |
| Negative prompt | the "leave out" box |
| Tail direction | unusual idea |
| Mode collapse, typicality bias | every answer coming out alike |

- Show limits as labeled arithmetic: `Characters used / Limit = Share of limit`, for example `412 / 1000 = 41%`.
- Explain any unavoidable technical term in a short clause the first time it appears, for example "seed (a number that repeats the same result)".
- Keep the reply short. The prompt blocks are the main content.
