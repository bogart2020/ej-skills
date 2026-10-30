# Music, Voice, and Sound

Read at Step 2 of [../SKILL.md](../SKILL.md) when the target makes songs, speech, or sound effects.

### Song generators (Suno, Udio, others)

- **Fields and limits:** separate **Style** and **Lyrics** boxes, plus a title. Suno style box about 1,000 characters on newer versions (about 200 on older ones); lyrics about 5,000. Limits change by version, so show the count and note it.
- **Format:** Style is comma-separated tags in this order: genre and era, mood, tempo or BPM, key instruments, vocal type and delivery, production feel. Lyrics carry structure tags on their own lines: `[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Outro]`.
- **Detail slots:** genre and era, tempo, two to four named instruments, vocal (range, texture, delivery), mood arc, song structure, and lyric details taken from the user's own story (names, objects, places, times).
- **Negatives:** some versions offer an exclude-styles box; otherwise leave unwanted styles out.
- **Known failure modes:** contradicting tags confuse it; fewer than about 15 lyric lines tends to give a short song; stock lyric images (see `slop-patterns.md`) make it sound generic. Avoid naming real artists; describe the sound.
- **Source:** lead (no official limits page; third-party guides disagree)

### Voice and speech (ElevenLabs and others)

- **Fields and limits:** the script text, plus voice choice and settings such as speed (0.7 to 1.2 on ElevenLabs) outside the prompt.
- **Format:** the script itself carries delivery. On Eleven v3, bracketed audio tags such as `[whispering]`, `[laughing]`, `[sighs]` control delivery; ellipses add pauses and weight; capitals add emphasis; normal punctuation sets rhythm.
- **Detail slots:** voice (age, accent, texture described plainly, "low, gravelly voice"), pace, emotion per line, pauses, speaker labels for dialogue.
- **Negatives:** none; describe the delivery wanted.
- **Known failure modes:** tags that read like sounds may play as sound effects; playful tags on a serious voice work poorly; v3 has no SSML break tags, so use ellipses; professional voice clones are less reliable on v3.
- **Source:** verified https://elevenlabs.io/docs/best-practices/prompting/eleven-v3

### Sound effects

- **Fields and limits:** one short description and a duration setting.
- **Format:** the source, the action, the space, and the distance: "heavy oak door creaks open slowly in a stone stairwell, close mic".
- **Detail slots:** source material, action, room or environment, distance, duration, loop or one-shot.
- **Negatives:** describe a clean source instead.
- **Known failure modes:** vague words ("cool whoosh") give generic results.
- **Source:** lead
