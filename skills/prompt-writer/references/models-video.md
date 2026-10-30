# Video

Read at Step 2 of [../SKILL.md](../SKILL.md) when the target makes or edits video, lip-sync, or avatars.

## Detail slots (all video models)

Style, subject, one action in beats, setting (place, era, weather, time of day), camera angle, one camera move, lens and focus, light (quality and 3 to 5 palette colors), pacing (real time, slow motion, time-lapse), audio (sound effects, ambience, dialogue with speaker and tone), duration and aspect ratio (as settings).

### Veo

- **Fields and limits:** prompt, optional negative prompt; length and aspect ratio set in the tool. Modes include text to video, first frame to video, first and last frames, reference images, extend, and edit.
- **Format:** cover subject, action, scene, camera angle, camera movement, lens effects, visual style, and timing. Camera moves: static, pan, tilt, dolly, truck, pedestal, zoom, crane, aerial, handheld, whip pan, arc. Describe audio in separate sentences.
- **Detail slots:** the shared list above.
- **Negatives:** in the negative prompt, list unwanted items plainly ("wall, frame"); avoid "no" or "don't" wording.
- **Known failure modes:** some advanced camera terms are not supported and vary; long events need clip-length planning.
- **Source:** verified https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide

### Sora

- **Fields and limits:** prompt; duration, resolution, and character references set in the API or app, not in prose.
- **Format:** a prose scene description, then a Cinematography block (shot, angle, depth of field, mood), an Actions list in beats, and a Dialogue block. One camera setup, one subject action, one lighting recipe per shot.
- **Detail slots:** the shared list above. Name 3 to 5 palette colors to keep shots consistent.
- **Negatives:** describe the wanted result.
- **Known failure modes:** short clips follow instructions better (two 4-second clips beat one 8-second clip); long speeches do not sync; small wording changes alter a character, so keep descriptions identical across shots; vague verbs give inconsistent motion ("pedals three times, then stops at the crosswalk" beats "rides around").
- **Source:** verified https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide

### Runway, Kling, and other video models

- **Fields and limits:** prompt plus an optional start image; duration as a setting.
- **Format:** with a start image, describe the motion and camera, not what the image already shows. Without one, follow the shared slots.
- **Detail slots:** the shared list above.
- **Negatives:** describe the wanted result.
- **Known failure modes:** several moves in one shot cause drift.
- **Source:** lead

### Lip-sync and avatars

- **Fields and limits:** a face image or avatar, an audio file or script, and a short motion description.
- **Format:** keep head motion and expression notes brief; match script emotion to the voice.
- **Detail slots:** face source, script or audio, expression, head movement range, framing.
- **Negatives:** none special.
- **Known failure modes:** extreme head turns and fast speech break sync. Real people: their own likeness or with consent.
- **Source:** lead
