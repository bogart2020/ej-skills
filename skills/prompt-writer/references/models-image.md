# Image Generation

Read at Step 2 of [../SKILL.md](../SKILL.md) when the target makes images from text.

## Detail slots (all image models)

Style or medium, subject (appearance, clothing, pose, expression), setting (place, era, season, time of day), action, composition (shot size, angle, subject placement), lens and depth of field, light (source, direction, color temperature), palette (3 to 5 named colors), material texture and small imperfections, any text in the image (exact words in quotes, plus font style, size, color, placement), aspect ratio, and intended use (poster, slide background, product page).

### GPT Image (ChatGPT images, DALL-E, OpenAI API)

- **Fields and limits:** one prompt; size and quality set outside the prompt.
- **Format:** order the prompt as scene or background, then subject, then key details, then constraints. Use short labeled lines for complex requests. State the intended use.
- **Detail slots:** the shared list above.
- **Negatives:** short plain exclusions are fine ("no watermark, no logos").
- **Known failure modes:** words that imply studio polish or staging give a plastic look; camera and light terms steer realism better than quality tags; ask for real texture (pores, wrinkles, fabric wear). Put literal text in quotes and spell rare words letter by letter. Iterate with one change at a time.
- **Source:** verified https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide

### Gemini Image (Nano Banana)

- **Fields and limits:** one prompt; aspect ratio and resolution chosen in the tool.
- **Format:** a descriptive sentence or short paragraph built as Style + Subject + Setting + Action + Composition. State the purpose of the image. Use clear wording that asks for an image, so the model does not answer in text.
- **Detail slots:** the shared list above.
- **Negatives:** describe what you want, not what you don't: "an empty, quiet street" in place of "no cars". Avoid "no" lists.
- **Known failure modes:** complex scenes come out better when split into ordered steps (background, then foreground, then key object). Give each recurring character a name and reuse it.
- **Source:** verified https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/gemini-image-generation-best-practices and https://deepmind.google/models/gemini-image/prompt-guide/

### Midjourney

- **Fields and limits:** one prompt line followed by parameters.
- **Format:** descriptive phrase first, parameters at the end: `--ar` for aspect ratio (for example `--ar 2:3`), `--no` for exclusions, `--stylize`, `--chaos`, `--raw` for a less stylized look, `--sref` for a style reference image.
- **Detail slots:** the shared list above. Keep the description tight; it weighs early words more.
- **Negatives:** `--no item, item` at the end.
- **Known failure modes:** quality-tag stuffing adds nothing; named living artists should be replaced by described traits.
- **Source:** lead (official docs returned an access error)

### Stable Diffusion and Flux

- **Fields and limits:** Stable Diffusion has a **positive** box and a **negative** box. Flux has a single prompt and reads natural sentences. Sampler, steps, seed, and size are settings outside the prompt.
- **Format:** Stable Diffusion: comma-separated descriptive phrases, most important first. Flux: plain descriptive sentences.
- **Detail slots:** the shared list above.
- **Negatives:** Stable Diffusion: list unwanted items in the negative box (blurry, extra fingers, watermark, text). Flux: describe the wanted scene positively.
- **Known failure modes:** "masterpiece, best quality, 8k, trending on artstation" stuffing gives the generic look; replace it with camera, light, and texture.
- **Source:** lead

### Logos, icons, and vector art

- **Fields and limits:** as the chosen model.
- **Format:** state flat vector, the number of colors, the shape idea, and where it will be used (favicon, sign, embroidery).
- **Detail slots:** the brand's subject, one visual idea, color count with hex values, line weight, negative space, legibility at small size, exact wordmark text in quotes.
- **Negatives:** as the chosen model.
- **Known failure modes:** generic gradients and glossy 3D effects; too many ideas in one mark. See the Design table in `slop-patterns.md`.
- **Source:** lead
