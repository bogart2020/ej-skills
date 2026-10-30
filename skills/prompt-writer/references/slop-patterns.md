# Generic AI Patterns

## Contents

- How to use this file
- Text
- Design
- Images and video
- Music and voice
- Over-correction guards

Read at Step 5 of [../SKILL.md](../SKILL.md). Check two things against these tables: the prompt's own words, and any text the prompt asks the model to write.

## How to use this file

These patterns come from the most typical answer a model gives. One pattern alone proves nothing. A cluster of them makes output read as generic. Fix the shape, not just the word: swapping "delve" for "dig into" keeps the same habit. When the user asked for the typical look, skip this file for the parts they asked for.

## Text

| Pattern | Looks like | Write instead |
| :--- | :--- | :--- |
| Inflated significance | stands as, serves as a testament, pivotal moment, crucial role, evolving landscape, indelible mark, deeply rooted, setting the stage | State the fact and its concrete effect |
| Trailing "-ing" analysis | "..., highlighting its importance", "..., underscoring", "..., fostering", "..., ensuring" | End the sentence at the fact, or give the effect its own sentence with a subject |
| Promotional tone | boasts, vibrant, rich, profound, nestled, in the heart of, groundbreaking, renowned, diverse array, showcase | A measurable or sensory detail |
| Stock vocabulary (2023 to 2025) | delve, tapestry, testament, intricate, meticulous, robust, seamless, elevate, enhance, garner, interplay, underscore, align with, bolster, realm, embark | The plain verb or noun |
| Newer stock vocabulary | leverage, multifaceted, quietly, steady, dependable, matters, prioritize, universally, echoed, foster | The plain word, or cut it |
| Copula avoidance | serves as, functions as, stands as, represents (meaning "is") | is, are, has |
| Negative parallelism | not just X but Y; it's not X, it's Y; no X, no Y, just Z | Say Y directly |
| Rule of three | Three adjectives or three clauses chosen for rhythm | Keep the one that carries information |
| Vague authority | experts say, studies show, many believe, observers note | Name the source, or drop the claim |
| Formulaic opener or closer | In today's fast-paced world; Despite these challenges; In conclusion; Ultimately | Start with the point; end on the last real point |
| Mannered prose | Metaphor in place of a literal phrase: "a dial worth turning", "earns its keep" | The literal phrase |
| Chat residue | Certainly!, Great question, I hope this helps, Let me know if | Remove it |
| Formatting tells | Title Case headings, bold on every phrase, emoji bullets, a table for two facts, "Label: text" bullets everywhere | Sentence case, bold only for scanning, prose when the content is prose |

**Text a prompt asks the model to write** (bot replies, ad copy, posts): add an instruction that states the voice positively, with a reason and one example line. "Write the way a helpful coworker texts: short sentences, plain words, one concrete next step. Customers trust plain answers." works better than a list of banned words.

## Design

Use for UI, web, slides, posters, logos, and app-builder prompts.

| Pattern | Looks like | Write instead |
| :--- | :--- | :--- |
| Default fonts | Inter, Roboto, Arial, system fonts; then drifting to Space Grotesk | Pick one or two families for the brand's voice and name the reason (a sturdy slab serif for a hardware store) |
| Purple gradient | Purple-to-blue gradient on white, gradient washes behind sections | A 4 to 6 color palette with named hex values drawn from the subject |
| Warm-cream default | Cream background near #F4F1EA with a terracotta accent | Colors taken from the product, place, or material |
| Dark-mode default | Near-black (#0B0B0B, #111) with one acid-green or vermilion accent | A dark palette with a named reason, or a light one |
| Card kit | Identical rounded cards, uniform soft shadows, three-feature grid | A layout shaped by the content's real structure |
| Eyebrow labels | Tracked-out ALL CAPS label above every heading | Headings that work alone |
| Decorative meta | Middle-dot strings ("5 min · Design · 2026"), mono micro-labels, arrows on every link | Only the metadata a reader uses |
| Hero formula | Big number, small label, supporting stats, gradient accent | A hero built from the product's actual proof |
| Motion everywhere | Fade-and-slide on every section, hover lift on every card | One purposeful motion moment, with reduced-motion support |
| Vague UI copy | Submit, Get started, Unlock your potential | The exact action: "Save changes", "Book a table" |

Give a method, not one replacement font or color, so the fix does not become the next default.

## Images and video

| Pattern | Looks like | Write instead |
| :--- | :--- | :--- |
| Quality-tag stuffing | masterpiece, best quality, 8k, ultra detailed, hyperrealistic, trending on artstation, award-winning | Camera, lens, light source and direction, and material texture |
| Studio polish | flawless, perfect skin, glossy, pristine, stunning, beautiful | Real texture: pores, fine wrinkles, worn fabric, scuffs, dust, stray hairs |
| Waxy faces | Smooth, shiny, overly symmetrical faces, "too gorgeous" | A specific face: age, asymmetry, marks, expression mid-movement |
| Oversaturation | vibrant colors, vivid, neon everywhere | A named palette of 3 to 5 colors and the light that makes them |
| Centered hero framing | Subject dead center, eye level, symmetrical | A chosen angle and placement: low three-quarter, subject on the left third |
| Cinematic filler | cinematic, epic, dramatic lighting, moody | The concrete light: "single sodium streetlight from camera right, wet asphalt reflections" |
| Default people | Young, slim, light-skinned adults unless told otherwise; jobs matched to stereotypes | Deliberate, believable choices listed for the user |
| Default places | Generic modern office, generic cafe, generic city skyline | A specific place, era, and season |
| Video drift | Several actions and camera moves in one shot, vague verbs ("moves around") | One camera move, one action in counted beats per shot |

## Music and voice

| Pattern | Looks like | Write instead |
| :--- | :--- | :--- |
| Stock lyric images | neon lights, echoes of the past, tapestry of dreams, symphony of, fire in my soul, chasing the stars, broken wings | Concrete objects from the user's story (the flour-dusted till, the 6 a.m. oven bell) |
| Abstract feeling words | Lines that name emotions ("I feel so lost") | Show the feeling through an action or object |
| Forced rhyme | Rhyme that bends meaning or grammar | Slant rhyme, or no rhyme on that line |
| Contradicting style tags | "calm aggressive", "lo-fi orchestral epic" with no reason | Tags that agree, ordered genre, mood, instruments, vocal |
| Tag and voice mismatch | Playful delivery tags on a serious narration voice | Tags that suit the chosen voice |

## Over-correction guards

- Keep lists that are real lists and groups of three that are really three items.
- Keep conventions the user asked for (a stock photo, a formal tone, a symmetrical logo).
- Avoid replacing a banned word with a near-synonym in the same sentence shape.
- Avoid making everything strange: "unusual" means specific and fitting, not random.
- Keep the user's wording when they fixed it, even when it appears in a table above.
