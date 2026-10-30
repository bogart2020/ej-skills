# Image Editing with Reference Photos

## Contents

- Rules for every edit
- Face swap
- Virtual try-on
- Inpaint and outpaint
- Background swap
- Relight
- Style transfer
- Character consistency
- Upscale and restore
- Model notes

Read at Step 2 of [../SKILL.md](../SKILL.md) when the user supplies photos to change or reuse. The Hard rules in SKILL.md on real people apply to every section.

## Rules for every edit

1. **Number each image and give its role:** "Image 1 is the face reference. Image 2 is the wedding photo to edit."
2. **Change only one thing, and say what stays:** "Change only X. Keep everything else in image 2 exactly the same." Repeat the keep line in every follow-up turn, because results drift.
3. **Name what to preserve** in a keep-list: identity features, pose, clothing, background, framing.
4. **Match the photo:** light direction, color temperature, sharpness, grain, lens perspective, and camera angle of the image being edited, so the change does not look pasted on.
5. **Use "change" or "replace", not "transform"**, which invites a full redraw.
6. **One edit per turn** for complex jobs: background first, then the person, then the light.
7. **Images not attached yet:** write the prompt anyway and tell the user which image goes in which slot.

**Detail slots:** image roles, the one change, the keep-list, the match list, output size.

## Face swap

Keep-list from the face reference: face shape, eye shape and color, nose, mouth, skin tone and texture, freckles, moles, scars, eyebrows, hairline, age. Keep from the target photo: head angle, expression (or name a new one), hair (unless asked), lighting, body, clothes, everyone else. Ask the model to blend skin tone at the neck and match grain. Real people: their own face or one they have permission to use.

## Virtual try-on

Image roles: the person and the garment. Keep: the person's face, body shape, pose, and background. Describe how the garment should fit (size, drape, tucked or loose) and keep its exact color, pattern, logo, and fabric texture.

## Inpaint and outpaint

Inpaint: describe only what fills the masked area and how it meets the edges. Outpaint: name the direction, the new aspect ratio, and what the extended area contains, matching perspective and light.

## Background swap

Keep the subject's edges, hair detail, and pose. Describe the new place fully (place, time, light) and make the subject's light match it, or say the new background should match the subject's existing light.

## Relight

Keep everything except the light. Name the new source, direction, hardness, color temperature, and time of day, plus where shadows fall.

## Style transfer

Image roles: the content image and the style image (or a described style). Keep the content's layout, faces, and proportions. Describe the style traits (palette, brushwork, line, texture). Use described traits in place of a living artist's name.

## Character consistency

Write one locked character description (name, age, face, hair, build, signature clothing, one distinctive mark) and paste it word for word in every prompt. Supply the same reference image each time when the tool allows. Change only pose, action, place, or camera.

## Upscale and restore

Keep identity and composition. Name what to fix (blur, noise, scratches, faded color) and what not to invent (new facial features, extra detail on text).

## Model notes

- **GPT Image:** refer to images by index and description; pair "change only X" with "keep everything else the same"; repeat the keep-list each turn. Source: verified https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide
- **Gemini Image:** reference images plus a reused character name keep subjects consistent; edit one element at a time. Source: verified https://deepmind.google/models/gemini-image/prompt-guide/
- **FLUX Kontext and similar editors:** template "Change [object] to [new state], keep [what to preserve] unchanged"; add "while preserving facial features" when people are involved; precise facial alignment is a weak spot. Source: lead
