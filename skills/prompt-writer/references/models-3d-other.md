# 3D, App Builders, Slides, and Anything Else

Read at Step 2 of [../SKILL.md](../SKILL.md) when the target makes 3D models, apps or UI, slides, or anything not covered by another file.

### Text-to-3D (Meshy and similar)

- **Fields and limits:** prompt up to 800 characters on Meshy; art style, topology, and polycount are settings.
- **Format:** subject, material, art style, scale, viewpoint, colors, visible features.
- **Detail slots:** one subject, material and wear, style (realistic, stylized, low-poly), real-world scale, key features, intended use (game asset, print, render).
- **Negatives:** short plain exclusions are accepted ("no background elements, no text").
- **Known failure modes:** several objects in one prompt give floating fragments, so describe one subject; realistic styles give dense meshes, stylized styles give cleaner topology; vague one-word prompts make the model guess.
- **Source:** verified https://docs.meshy.ai/en/webapp/text-to-3d

### App and UI builders

- **Fields and limits:** one prompt, often with follow-up chat.
- **Format:** what the app does, who uses it, the screens, the data each screen shows, the main actions, and the visual direction.
- **Detail slots:** users and their main task, screens, data, actions, empty and error states, typography choice with reason, a 4 to 6 color palette with hex values, layout idea, one motion moment, exact button labels.
- **Negatives:** describe the wanted design; use the Design table in `slop-patterns.md` to steer away from default fonts, gradients, and card grids.
- **Known failure modes:** without visual direction it returns the generic default design.
- **Source:** lead

### Slide makers

- **Fields and limits:** one prompt and often an outline or document.
- **Format:** audience, goal, number of slides, one message per slide, data to show, visual direction.
- **Detail slots:** audience, the one decision the deck should drive, slide count, per-slide headline as a full sentence, charts with their data, palette and type.
- **Negatives:** describe the wanted design.
- **Known failure modes:** bullet-heavy slides and stock icons; ask for one idea per slide and real data.
- **Source:** lead

### Anything else

Use this when the model has no profile and its official guide cannot be opened.

1. **Find the boxes:** ask yourself what the tool takes in (text only, text plus image, separate fields) and what it lets you set outside the prompt. Use only what the user told you or what is visible.
2. **Write plain sentences:** describe the result fully and positively, most important details first. Use no special syntax.
3. **Fill the shared details:** subject, purpose, style, materials or voice, setting, constraints, and the output format.
4. **Say what you assumed** in one line of the reply, so the user can correct it.
