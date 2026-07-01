# Google Flow + Omni Flash: Ingredient Conventions

**Source: user-supplied screenshots and working example prompts from Google Flow's actual product UI, 2026-07-01 — not from Google's own published docs (which describe the raw Vertex AI API surface, covered in `veo-video-prompting.md`).** Treat this file as the primary, practical path for anyone generating through Flow rather than calling the API directly. Where this conflicts with `veo-video-prompting.md`, that's because Flow's product layer adds capabilities beyond the raw `referenceImages: asset/style` field — it is not a contradiction, it's a different, more flexible surface.

## Core mechanism: ingredients + `@filename` tags

Flow calls every uploaded reference (image, video, or audio) an **ingredient**. The workflow:

1. Upload a background/environment image, a character reference (sheet or single base image), a source video, and/or an audio file as ingredients.
2. Pull ingredients into the prompt box.
3. Choose the model (**Omni Flash** for the fastest/cheapest tier), aspect ratio, number of videos, and duration (**max 10s**).
4. **Reference each ingredient in the prompt text using `@` followed by its exact filename** — e.g. `@image.png`, `@Forest_Background.png`, `@video_0.mp4`, `@audio_0.wav`.
5. Generate, then download.

This is a real, working `@`-tag mechanism — but it is fundamentally different from Kling/Seedance's `@image1`/`@element_name` symbolic placeholders, and different from the raw Vertex API (which has no tag syntax at all). The critical distinction:

- **Kling/Seedance**: `@element_name` is an arbitrary label you define once against an `elements` array; the model/preprocessor resolves it.
- **Raw Gemini/Veo API**: no tag syntax exists; binding is prose-only (ordinal/role-noun) or via typed `referenceImages` fields, entirely separate from the prompt string.
- **Flow + Omni**: `@<exact_ingredient_filename>` is a **literal filename match** against whatever you named the file before uploading it. There is no arbitrary/symbolic index — the token only resolves if it matches an uploaded ingredient's actual name.

**Practical rule: name your ingredient files descriptively before uploading, then use that exact name as the `@` token in the prompt.** `enchantress_ref.png`, `bird_blue_ref.png`, `forest_background.png` — not `image1.png`, `ref_a.png`, or any placeholder that doesn't describe the actual content. This is the one context in this skill where writing an `@` token into the prompt is correct and expected; everywhere else (raw API prompts, Nano Banana Pro prompts, non-Flow Veo calls) it is still wrong, per `references/veo-video-prompting.md` and `references/gemini-image-prompting.md`.

## Grid sheets as direct scene input — this is what "storyboard" means on Omni

A multi-cell reference/scene grid (e.g. a 3x3 character sheet, or a purpose-built N-cell staging grid) can be uploaded as a single ingredient and the prompt can explicitly map each grid cell to a distinct video scene:

> `@image.png is a reference for consistency. create a video that uses grid image 1 - 9 as video scenes. On each video scene, the character says one word: Scene 1: "The" Scene 2: "Gemini" ... `

This is confirmed working (with a reported minor glitch at the very first scene transition in the source example — expect scene-boundary artifacts to need iteration, not treat the mechanism as unreliable). **This is the actual mechanism experienced Flow users mean by "using a storyboard with success."** It is not the sparse, never-attached preview sheet this skill originally specified — it is a rendered, final-style grid image, uploaded as a real ingredient, with each cell's content explicitly assigned in prose by grid position.

**Extended pattern — burned-in per-panel captions carry both content and duration.** A second user-supplied example: a fully rendered, polished 3x3 storyboard grid (finished character art, consistent background, panel borders) with a caption bar under every panel reading like `"3 sec — Kimmy and Brandon arrive at Riverside Park."` — i.e. each panel's visible text states both the scene's duration and its action, baked directly into the image. Uploaded as the ingredient, this drove a full video generation that honored both the per-panel content and the stated per-panel timing. The user confirmed the resulting ~30-second video was **stitched from multiple generated clips**, not one single call exceeding 10s. **Confirmed design rule: 10s is the real per-call ceiling.** Any sequence needing more than ~10s of screen time must be split into multiple grid+call pairs (one rendered scene grid, one Omni call, per ~10s segment) and stitched afterward — exactly the multi-shot structure this skill already defaults to (independent calls per cut, matching `ATTACH`/ingredient sets, continuity carried by consistent references + explicit restated starting state). Do not attempt a single call for content that adds up to more than ~10s.

Practical technique worth adopting regardless of the duration question: **write duration + action into each grid panel's own caption text** (`"3 sec — description"`), rather than relying only on a separate `Scene N:` prose block in the prompt. This makes the grid image self-documenting and reduces how much the prompt text has to carry, and it's confirmed to work for driving per-scene timing.

Design implications for this skill:
- Build the "storyboard" as one **rendered, final-style grid image per Veo call** (not sparse/monochrome — see the direct-visual-vs-sketch discussion this skill's workflow should now default to direct/rendered when the target is Flow+Omni), sized so each cell maps cleanly to one `P##` beat in that call.
- Reference it with `@<grid_filename>` and an explicit `Scene N:` mapping in the video prompt, one line per grid cell, mirroring the beat content (dialogue, action, visible result) instead of (or alongside) timestamp-range beats.
- Still attach separate character/prop ingredient images (e.g. `@enchantress_ref.png`) for identity reinforcement — the grid image already carries correct appearance (since you generate it using those same references), but redundant anchoring is still the documented mitigation for drift within a single generation.
- **Unverified**: whether Omni Flash's ingredient count has a hard cap analogous to the raw API's 3-asset/1-style limit. Flow's own UI copy doesn't state a number. Design for however many ingredients the shot genuinely needs (grid + each recurring character), and treat exceeding ~4 ingredients in one call as something to test rather than assume works or fails.

## Multi-modal ingredients: image, video, and audio together

Omni ("turns any reference — image, text, video or audio — into a single, cohesive output") accepts mixed ingredient types in one prompt, each referenced the same `@filename` way:

> `Dynamic sci-fi film style video based on image_0.png. Elements light up similar to video_0.mp4 synchronized to the beat of the music from audio_0.wav`

> `Referring to the extreme camera movement, perspective, and distortion in video-0, create a front-facing full-body walk cycle of the character from image-0, quickly style-shifting into multiple visual styles during the walk cycle, starting from realistic cinema. Keep the environment, only change styles. Hard cut backgrounds always centering the sky. Continuous walking, continuous audio, and style shifts in perfect sync to the beat of the audio. Cinematic, 16:9.`

Notable patterns from these examples, worth reusing:
- A **video ingredient** can supply camera movement/perspective/distortion style, independent of its subject matter — cite it in prose ("referring to the extreme camera movement... in video-0") the same way an image ingredient supplies appearance or an audio ingredient supplies rhythm.
- **Audio-sync** is a first-class instruction: "synchronized to the beat of the music from audio_0.wav" is enough; no separate timestamp math is required for beat-matching.
- Style-shift-on-a-single-continuous-action prompts ("quickly style-shifting into multiple visual styles... starting from realistic cinema... only change styles") work as a single instruction, not per-beat micromanagement — useful for anything needing an intentional in-shot style change, including a deliberate two-style contrast if that's ever wanted within one continuous shot rather than across cuts.
- Text ingredients are also accepted per Google's own framing ("image, text, video or audio") though no example above demonstrates one explicitly — treat plain prose in the main prompt as covering this by default.

## Realism/texture descriptors

One example prompt includes explicit anti-uncanny-valley detail: *"Use visible skin texture, uneven eyebrow thickness, subtle oily shine on forehead, faint smile lines, natural asymmetry, fabric texture on clothing."* Worth keeping as a reusable line whenever a shot needs to avoid a too-smooth/synthetic look on a human or human-like character — add it to `STYLE & AMBIANCE` rather than treating it as one-off flavor text.

## On-screen text

Confirmed working pattern for burned-in captions/dialogue text: *"The word is displayed near the bottom of the scene in white uppercase lettering with a 1px black outline."* Specify position, case, color, and outline/stroke explicitly — this mirrors Nano Banana Pro's text-rendering guidance (quote the exact text, describe the typography) and evidently carries into Omni video generation too.

## How this changes the skill's defaults for Flow/Omni targets

- **Storyboard**: build as a rendered scene grid (one ingredient), not a sparse preview-only sheet — see `templates/flow_scene_grid_template.txt`.
- **Video prompt**: use `@<ingredient_filename>` tags for every reference (grid + character/prop plates), plus explicit `Scene N:` mapping when using a grid — see `templates/flow_video_prompt_template.txt`.
- **Duration**: 10s max per generation on Omni Flash (confirmed in the product UI, matches the earlier practitioner-reported figure).
- **File naming discipline is now load-bearing, not cosmetic**: every ingredient filename IS the reference token. Get it right before uploading, since the prompt text has to match it exactly.
- The raw-API path (`references/veo-video-prompting.md`, `templates/video_prompt_template.txt`) remains valid for anyone calling the Gemini/Vertex API directly instead of using Flow — keep both documented since they're genuinely different surfaces with different rules, and ask the user which one they're targeting if it's ambiguous.
