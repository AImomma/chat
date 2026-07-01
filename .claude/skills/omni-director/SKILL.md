---
name: omni-director
description: "Generate paired storyboard/scene-grid, reference-plate, and video prompts for Google's Gemini omni media stack: Nano Banana Pro (Gemini 3 Pro Image) for stills and Omni/Veo 3.1 for video, built for Google Flow's real ingredient + @filename workflow. Use for omni director, Nano Banana Pro prompts, Gemini image reference prompts, Omni Flash / Veo 3.1 storyboard-to-video prompts, character/prop/location reference plates, scene grids, ingredient tagging, and any handoff where reference images must render as intended and the target style must hold. Do not reuse Kling/Seedance-style @image1/@element_name placeholder tags here — Flow's @tags only resolve against a real uploaded ingredient's exact filename, and the raw Gemini/Veo API has no tag syntax at all."
---

# omni-director Prompt Generator

Create a small set of prompt files for one scene, targeting Google's image and video models. This skill has **two target surfaces** — pick the one the user is actually using, ask if unclear:

- **Google Flow + Omni (primary, default)**: the real product most people use. References are uploaded as **ingredients** and tagged in-prompt with `@<exact_filename>`. A rendered, captioned **scene grid** (one image, multiple panels) is a real, working generation input, not just a preview. Max **10 seconds per generation call** — longer sequences are stitched from multiple calls afterward, not produced in one call. See `references/flow-omni-ingredients.md`.
- **Raw Gemini/Vertex API (secondary)**: for anyone calling the API directly instead of using Flow. No tag syntax at all — binding is prose (Nano Banana Pro) or typed `referenceImages` fields (`asset`/`style`, standard Veo 3.1, 8s base + extension chaining). See `references/veo-video-prompting.md`.

Both surfaces share the same underlying models and the same director craft (`references/craft-guide.md`, `references/gemini-image-prompting.md` for stills). They differ in how references bind to a prompt and how a multi-panel board is used — get this right or output looks wrong even when everything else is correct.

## Why `@image1`/`@element_name` still doesn't work here

Kling and Seedance resolve an arbitrary symbolic token (`@image1`, `@element_name`) that you define once against an elements array. **Neither Google surface works that way.** On the raw API there is no tag parser at all — binding is prose-only or typed fields. On Flow, `@` tags are real, but they only resolve by **exact match against an uploaded ingredient's actual filename** — `@image1` fails unless you happened to name a file `image1`. The fix is the same in spirit either way: never invent a placeholder token. On Flow, name your ingredient files descriptively before uploading (`enchantress_ref.png`, `grid_shot_01.png`) and reference that exact name. On the raw API, don't use `@` at all — use ordinal/role-noun prose or the typed `asset`/`style` fields instead.

## Authority Model

- **Craft phase**: run the cinema-language, shot-tag, and cinematography passes in `references/craft-guide.md` before writing anything. Build one shared `P##` sequence spine: visible event, camera angle, shot scale, framing, pose/blocking, screen direction, prop/effect state, count/entity state, and approximate duration per beat. This spine drives every artifact below.
- **Reference phase**: for every recurring character, hero prop, fixed location, or enforced aesthetic, decide whether it needs a generated or user-supplied reference plate. Plates are the *sole* authority for final identity, wardrobe, prop design, and location geometry.
- **Generation phase (Flow/Omni)**: group `P##` beats into ~10s calls. For each call, build one rendered, captioned **scene grid** (one panel per beat, caption = duration + action/dialogue) — this is a real generation input, not a preview. Upload it plus every recurring character/prop plate as ingredients; the video prompt references all of them by `@filename` and tells Omni to use the grid's panels as scenes in order. The grid is authoritative for staging/composition/timing; the character plates are authoritative for appearance; the prompt prose carries audio and any style rules the captions can't.
- **Generation phase (raw API)**: no grid mechanism exists here. The storyboard stays a **human preview only**, never attached to a call. Composition/blocking live entirely in the video prompt's own prose and timestamped beats; the `asset`/`style` plates carry appearance. See the raw-API workflow note in Step 8 below.

## Reference Architecture

**Flow ingredients — `@filename` binding (primary).** Every uploaded image/video/audio is an ingredient, added via "Add Ingredient" (choosing category Character/Object/Style) and then referenced in-prompt as `@<exact filename>`. Name files descriptively before upload; the filename *is* the token. Tag people/creatures as **Character** specifically (not a bare upload) — it likely gets the same dedicated identity-preservation handling as the raw API's `asset` type. A scene grid counts as one ingredient like any other. **Google's own guidance caps Ingredients-to-Video at 3 ingredients per call** — design for 3, not more; if a call needs a grid plus more than 2 character/prop ingredients, drop the least drift-prone one and lean on the grid's own rendering + prose for it. See `references/flow-omni-ingredients.md`.

**Nano Banana Pro — prose binding (both surfaces, for still generation).** When a still-image prompt includes multiple input images, name each one's exact contribution *before* describing the target scene — ordinal ("the first image," "the second image") or lettered role labels ("Image A," "Image B"), never a symbol. Scope exclusions ("do not carry Image A's clothing into Image B's role") are permitted and necessary for preventing bleed; they are not the same as the scene-negation Google discourages (see `references/gemini-image-prompting.md`). This applies to the raw API always, and also describes *within* a Flow prompt when you're not using `@filename` tags for some reason — but when targeting Flow, prefer `@filename` since it's the surface's native mechanism.

**Raw Veo 3.1 — typed field binding (secondary path only).** `referenceImages`, each tagged `asset` (≤3, same subject) or `style` (≤1, verify-live on 3.1). No tag syntax in the prompt text; role-noun prose instead. Full mechanics in `references/veo-video-prompting.md`. Don't use this section's rules when the target is actually Flow — the two surfaces are not interchangeable.

**Identity-drift mitigation (both surfaces).** The model regenerates "a new person who loosely matches the description" on every call unless anchored redundantly. For every character appearing in more than one call: (1) attach/upload the same reference plate(s) to every call they appear in, and (2) write one fixed **identity-descriptor sentence** per character during the craft phase, reused verbatim in every plate prompt, every grid caption, and every video prompt mentioning them.

**Location plates.** Neither surface has a dedicated "location" reference type. A location plate, if generated, isn't attached/tagged on its own — its job is keeping the *prose* description of that location consistent across every call's context/caption, and optionally serving as an input reference when generating the scene grid itself in Nano Banana Pro. Say this explicitly in `00_notes.txt` whenever a project has one.

**Grid/storyboard isolation is surface-dependent.** On Flow, the scene grid is a real, attached, load-bearing input — render it in final style and caption every panel with duration + action (`"3 sec — description"`), per `references/flow-omni-ingredients.md`. On the raw API, keep the old sparse/monochrome, human-preview-only convention — it is never attached there, so detail in it is wasted effort and risks being mistaken for a style source.

**Entity-token isolation.** Use internal IDs (`C1`, `C2`, `P1`) for your own planning only. Translate every ID into a natural description before it goes into any prompt or grid caption — Nano Banana Pro renders stray IDs as literal on-image text if you leave them in.

## Defaults

- Output language: English unless the user requests another language.
- Target surface: **Flow/Omni unless told otherwise.** Ask once if it's genuinely ambiguous; don't ask on every request.
- Aspect ratio: `16:9` unless the user requests otherwise.
- Image resolution: `2K` by default (`1K` for quick iteration, `4K` for finals).
- Video duration: **10 seconds per call, confirmed ceiling on Omni.** Sequences needing more are built as multiple ~10s call+grid pairs, stitched afterward — never attempt one call for content adding up to more than ~10s. (Raw-API Veo 3.1 stays at its verified 8s base + extension chaining if that's the actual target — see `references/veo-video-prompting.md`.)
- Scene grid (Flow default): one rendered, final-style grid image per ~10s call, one panel per `P##` beat in that call, each panel captioned `"<N> sec — <action/dialogue>"`. Not sparse, not monochrome — it's a real input now, render it accordingly.
- Reference plates per recurring character: 1 clean image is enough if the user supplies one usable photo; generate 2 (front + action/expression pose) when building from scratch and more angle coverage is needed. Hero props: up to 2. Location: 1, never attached/tagged on its own.
- No hard prompt character ceiling. Write dense narrative prose, not tag lists, and don't invent an arbitrary length cap.
- Negative phrasing: describe desired visual content positively. Exception: audio-channel suppression commonly and effectively uses literal negation (`"no background music"`).
- File output: save everything under `od_prompts/<short_slug>/` (see Output Layout).
- Final response: return the saved file paths, a one-line ingredient/attachment summary, and a short confirmation — full prompt text only if asked.

## Workflow

1. Extract premise, mood, genre, location, character/entity count, action arc, props/effects, count-sensitive entities, start/end state, continuity locks, any user-supplied title, and any user-supplied reference photos. Confirm the target surface (Flow/Omni vs. raw API) if unclear.
2. Run the Craft Pass from `references/craft-guide.md`: cinema language, cinematic title, dramatic shot tags, cinematography layer — lock these before writing beats.
3. Build the shared `P##` sequence spine: camera angle, shot scale, framing, pose/blocking, screen direction, prop/effect state, count/entity state, visible result, and an approximate duration per beat. Add a master geography beat early for multiple characters, combat, pursuit, or changing geography.
4. Decide the reference set and write one fixed identity-descriptor sentence per recurring character/prop now, reused verbatim everywhere.
5. Write reference plate prompts (Nano Banana Pro) for anything not already covered by a usable user-supplied photo, using `templates/reference_plate_template.txt`.
6. Group `P##` beats into ~10s calls (Flow/Omni) or ~8s calls (raw API). **Default to independent calls per cut**, one grid/set of references per call; reserve any continuous-shot mechanic for a genuinely unbroken camera move, not general multi-shot sequencing.
7. **Flow/Omni path**: for each call, write one scene-grid image prompt (`templates/flow_scene_grid_template.txt`) — rendered final-style panels, one per beat, each captioned with duration + action/dialogue. Then write the matching video prompt (`templates/flow_video_prompt_template.txt`) using `@filename` tags for the grid and every character/prop ingredient needed in that call, per `references/flow-omni-ingredients.md`.
   **Raw API path**: write one sparse, human-preview-only storyboard prompt (`templates/storyboard_preview_template.txt`) covering the full sequence, then one video prompt per ~8s call (`templates/video_prompt_template.txt`) using role-noun prose plus the `ATTACH AS ASSET`/`ATTACH AS STYLE` block, per `references/veo-video-prompting.md`.
8. Apply the craft-guide's effect/prop separation and count/entity/single-instant locks to every beat; keep one frozen instant per grid panel and one continuous action per video beat.
9. Write `00_notes.txt`: ingredient filenames and what each is used for (Flow) or attach-map (raw API), generation order, continuity notes between calls, and any unverified/live-risk items worth a cheap test generation first.
10. Validate against the checklist below before returning file paths.

## Output Layout

```
od_prompts/<short_slug>/
  00_notes.txt                  # ingredient/attach map + generation order + risk notes
  grids/                        # Flow/Omni path
    grid_shot_01.txt             # rendered, captioned scene-grid prompt, one per ~10s call
    grid_shot_02.txt
  storyboard_preview.txt        # raw-API path only: sparse, human preview, never attached
  refs/
    <descriptive_name>_ref.txt  # one Nano Banana Pro prompt per plate, named for its @filename use
  video/
    shot_01.txt                 # one video prompt per call (~10s Flow/Omni, ~8s raw API)
    shot_02.txt
```

## Validation

Before finalizing an omni-director request, verify:

- No arbitrary placeholder token (`@image1`, `@element_name`, `@C1`, bracketed indices) appears anywhere — on Flow, every `@tag` matches a real, descriptively-named ingredient filename; on the raw API, there is no `@tag` at all.
- Flow path: every scene grid is rendered in final style (not sparse/monochrome), every panel is captioned with duration + action/dialogue, and the matching video prompt tells Omni explicitly to use the grid's panels as scenes in order.
- Flow path: every call's total caption duration stays at or under ~10s; anything longer is split into another grid+call pair, not crammed into one call.
- Raw API path: the storyboard stays sparse, monochrome, and is never attached to a video call; its own text says so.
- Every reference plate prompt names exactly one clean subject and states which prior image (if any) it must match exactly.
- Every recurring character/prop uses the same fixed identity-descriptor sentence in every plate, grid caption, and video prompt mentioning them — no drifted rewording.
- No location plate is ever tagged/attached on its own — location consistency is carried by repeated prose/captions, and `00_notes.txt` says so if one exists.
- Scene content is phrased positively everywhere except audio-suppression lines and reference-role scope exclusions.
- The shared `P##` spine is identical in coverage across every grid/storyboard and every video call — same order, same visible events — only the wording/format differs per surface's conventions.
- Each grid panel/storyboard panel is one frozen instant; each video beat has one continuous action with a visible result.
- Count-sensitive entities carry an explicit total and one-instance-only language everywhere they appear.
- `00_notes.txt` names the target surface explicitly, stays within the 3-ingredient-per-call guidance (with an explicit fallback priority if a call needs more), and flags anything unverified/live-risk (style-reference support on raw Veo 3.1, current model roster) rather than asserting it works.
- Final response returns file paths and a short ingredient/attachment summary, not full prompt text, unless asked.

## Reference Files

- `references/flow-omni-ingredients.md` — **primary path.** Google Flow's real `@filename` ingredient mechanism, scene-grid-as-input pattern, captioned-panel duration convention, multi-modal (image/video/audio) ingredients, confirmed 10s-per-call ceiling.
- `references/gemini-image-prompting.md` — Nano Banana Pro conventions: prompt formulas, multi-image binding, plate/identity technique, style-transfer scoping, text rendering, resolution/aspect values, positive-phrasing rule, camera/lens/lighting vocabulary.
- `references/veo-video-prompting.md` — **secondary/raw-API path.** Veo 3.1 conventions: prompt formula, `asset`/`style` typed reference fields and JSON shapes, first/last-frame conditioning, dialogue/SFX/ambient syntax, timestamped multi-beat prompting, duration/extension mechanics, identity-drift mitigation, live-verification caveats.
- `references/craft-guide.md` — model-agnostic director craft: cinema-language selection, dramatic shot-tag construction, cinematography layer, effect/prop separation, count/entity/single-instant locks, rhythm-and-escalation prose.
- `templates/flow_scene_grid_template.txt`, `templates/flow_video_prompt_template.txt` — Flow/Omni path skeletons.
- `templates/storyboard_preview_template.txt`, `templates/video_prompt_template.txt` — raw-API path skeletons.
- `templates/reference_plate_template.txt`, `templates/assembly_notes_template.txt` — shared by both paths.
