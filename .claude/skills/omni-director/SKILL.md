---
name: omni-director
description: "Generate paired storyboard-preview, reference-plate, and video prompts for Google's Gemini omni media stack: Nano Banana Pro (Gemini 3 Pro Image) for stills and Veo 3.1 for video. Use for omni director, Nano Banana Pro prompts, Gemini image reference prompts, Veo 3.1 storyboard-to-video prompts, character/prop/location reference plates, asset and style reference images, camera/cinematography-driven shot design, and any handoff where reference images must render as intended and the target style must hold. Do not use this for Kling/Seedance-style @tag prompting — Google's models bind references through prose and typed API fields, not symbolic tags, and reusing tag syntax here produces broken output."
---

# omni-director Prompt Generator

Create a small set of prompt files for one scene, targeting two Google models:

- **Nano Banana Pro** (Gemini 3 Pro Image) generates: a sparse **storyboard preview sheet** (human staging pre-viz only) and one or more **reference plates** (clean, single-subject identity/prop/location/style anchors).
- **Veo 3.1** generates the **video**, conditioned on prose plus the reference plates attached through Veo's typed reference-image slots.

## Why this is not a ported Seedance/Kling skill

Kling and Seedance parse literal `@image1`/`@image2`/`@element_name` tokens in the prompt text and resolve them to specific uploaded images. **Gemini and Veo have no such parser.** Nano Banana Pro binds multiple input images to a prompt through plain descriptive prose — ordinal position ("the first image," "the second image") or lettered role labels ("Image A," "Image B") stated in a sentence, not a symbol. Veo binds reference images through **typed API fields** (`referenceType: "asset"` or `"style"`) that are separate from the prompt string entirely; the prompt text then just needs to describe the subject using a consistent role-noun ("the detective," "the courier") that matches the reference's description.

If you write `@image1` into a Gemini or Veo prompt, the model either ignores it as noise or — worse, since Nano Banana Pro renders text very accurately — draws it as literal text in the image. That mismatch is the most likely cause of "the reference doesn't look like it's supposed to" and "the style is wrong." **Never write `@image#`, `@element_name`, or any bracketed image-index token into a prompt destined for Gemini or Veo.** See `references/gemini-image-prompting.md` and `references/veo-video-prompting.md` for the exact binding mechanics.

A second structural difference: Seedance-style workflows feed one composited storyboard sheet into the video model as a layout anchor. **Veo has no "layout anchor" reference type.** Its typed slots are `asset` (identity) and `style` (aesthetic) only — neither is a composition/staging anchor. So in this skill the storyboard sheet is retargeted as a **human preview artifact only**: it lets you validate blocking and camera choices before spending on video generation, but it is **never** attached to a Veo call. Composition and blocking live entirely in the video prompt's own prose and timestamped beats. Character/prop/location consistency comes from separate, clean **reference plates**, attached as typed `asset`/`style` images — this mirrors Google's own documented "Ingredients to Video" workflow.

## Authority Model

- **Craft phase**: run the cinema-language, shot-tag, and cinematography passes in `references/craft-guide.md` before writing anything. Build one shared `P##` sequence spine: visible event, camera angle, shot scale, framing, pose/blocking, screen direction, prop/effect state, count/entity state per beat. This spine drives every artifact below.
- **Reference phase**: for every recurring character, hero prop, fixed location, or enforced aesthetic, decide whether it needs a generated or user-supplied reference plate (see Reference Architecture). Plates are the *sole* authority for final identity, wardrobe, prop design, and location geometry. Nothing in the storyboard preview sheet overrides a plate.
- **Generation phase**: the storyboard preview sheet is a staging/camera reference for the human only — extract its panel blocking into the video prompt's own prose, never attach the sheet file to a Veo call. The video prompt's prose plus the attached `asset`/`style` plates are Veo's only real inputs; the plates are authoritative for appearance, the prose is authoritative for action, camera, timing, and audio.

## Reference Architecture (read this before writing any prompt)

**Nano Banana Pro — prose binding.** When a prompt includes multiple input images, name each one's exact contribution *before* describing the target scene: `"Using the first attached image for the character's face and hair, and the second for the jacket's exact texture and stitching, generate..."` or `"Image A controls pose and body proportions only. Image B controls environment and lighting only. Do not carry Image A's clothing or Image B's color palette into the other's role."` Scope exclusions like that last sentence are permitted and necessary for preventing bleed between references — they are not the same as the "no X" scene-negation Google discourages (see `references/gemini-image-prompting.md` §Negative phrasing). Always state scene content positively; only reference *role* is ever phrased as an exclusion.

**Veo 3.1 — typed field binding.** Reference images are not typed into the prompt text at all. They are passed as a separate `referenceImages` list, each tagged `asset` (≤3 images, same subject/identity, different angles or context) or `style` (≤1 image, aesthetic only — verify this still works on 3.1 before relying on it, see caveat in `references/veo-video-prompting.md`). The prompt prose then refers to the subject with a short, consistent role-noun description that matches the plate — e.g. if the plate prompt calls the character "a weathered courier in a patched leather coat," the video prompt calls her the same thing every time, never `@C1` or `Image 2`.

**Identity-drift mitigation.** Veo regenerates a "new person who loosely matches the description" on every call unless anchored redundantly. For every character that appears in more than one shot: (1) attach the same 2–3 asset plates to every Veo call they appear in, and (2) write one fixed **identity-descriptor sentence** per character during the craft phase and reuse it verbatim in every plate prompt and every video beat mentioning them. Image + repeated text is a stronger anchor than either alone.

**Asset-slot priority when recurring entities outnumber the 3-slot cap.** A single Veo call has only 3 `asset` slots total, shared across every subject in that shot — not 3 per character. When a shot has more identity-critical recurring entities (lead character, a plot-critical prop or vehicle, a secondary character, etc.) than available slots, allocate in this order: (1) the shot's point-of-view/lead character, (2) any entity whose *exact* appearance is plot-critical (a specific weapon, a specific vehicle, a distinguishing mark the story depends on), (3) secondary characters, last. Everything that doesn't get a slot falls back to prose-only consistency: its fixed identity-descriptor sentence, repeated verbatim, with no image anchor. Record which entities didn't get a slot in `00_notes.txt` so drift can be checked there first if it shows up.

**Location and style plates are not always attachable.** Veo has exactly two reference types, `asset` and `style` — there is no location/environment type. A location plate, if you generate one, is never attached to a Veo call; its only job is to keep the *prose* description of that location consistent across every shot's `CONTEXT` line (and, optionally, as an input reference when generating other plates or the storyboard sheet in Nano Banana Pro, where there's no such type restriction). Say this explicitly in `00_notes.txt` for any project that includes a location plate, so it doesn't read as an oversight.

**Storyboard sheet isolation.** The preview sheet stays sparse and schematic (open-outline blocking, minimal detail) precisely so it is never mistaken for a style or identity source. Do not put final color, material, or likeness detail into the storyboard prompt — that all belongs in reference plates and the video prompt.

**Entity-token isolation.** Use internal IDs (`C1`, `C2`, `P1`) for your own planning only. Translate every ID into a natural description before it goes into any prompt string. Nano Banana Pro will render a stray `C1` as literal on-image text if you leave it in.

## Defaults

- Output language: English unless the user requests another language.
- Aspect ratio: `16:9` for both stills and video unless the user requests otherwise. Veo 3.1 also supports `9:16`; note the live caveat in `references/veo-video-prompting.md` about reference images and portrait mode before promising it works.
- Image resolution: `2K` by default (`1K` for quick iteration, `4K` for finals).
- Video: **default to Omni, 10-second clips.** Only build shorter (8s standard Veo 3.1, or less) when the user explicitly asks for it in that request — don't ask each time, just assume Omni/10s unless told otherwise. (Standard Veo 3.1's verified base is 8s; Omni's 10s is practitioner-confirmed, not from an official spec page — see `references/veo-video-prompting.md`.) Use timestamped sub-beats (`[00:00-00:02] ...`) to fit multiple `P##` beats in one clip; for sequences that need more than one clip, default to **independent calls** with matching `ATTACH` blocks at any cut point, and reserve Veo's extension mechanic (chains +7s per call, up to ~20 times, ~148s max, reusing the same reference plates) for genuinely continuous, uncut camera moves. See `references/veo-video-prompting.md`.
- Reference plates per recurring character: 2 by default (front-facing + a three-quarter or action/expression pose), 3 maximum (Veo's `asset` cap). Hero props needing multi-angle clarity: up to 2. Fixed location: 1. Style: 0 or 1 — only add a style plate when prose alone can't lock the aesthetic, and flag the Veo 3.1 support caveat to the user.
- No hard prompt character ceiling. Google's guidance rewards specific, narrative, image-model-tuned prose over terse tag lists — write dense, not padded, and do not invent an arbitrary length cap the way tag-based systems do.
- Negative phrasing: describe desired visual content positively (`"an empty street"`, not `"no cars"`). Exception: Veo audio-channel suppression commonly and effectively uses literal negation (`"no background music"`), per `references/veo-video-prompting.md`.
- File output: save everything under `od_prompts/<short_slug>/` (see Output Layout below).
- Final response: return the saved file paths, a one-line note on which plates to attach where, and a short confirmation — full prompt text only if the user explicitly asks to see it printed.

## Workflow

1. Extract premise, mood, genre, location, character/entity count, action arc, props/effects, count-sensitive entities, start/end state, continuity locks, any user-supplied title, and any user-supplied reference photos.
2. Run the Craft Pass from `references/craft-guide.md`: pick a scene-appropriate cinema language, a cinematic title, dramatic shot tags (viewpoint + function, not neutral size labels), and the cinematography layer (lighting key, color/palette emotion, lens/DOF feel, atmosphere) — lock these before writing beats.
3. Build the shared `P##` sequence spine: one entry per beat with camera angle, shot scale, framing, pose/blocking, screen direction, prop/effect state, count/entity state, visible result. Add a master geography beat early if the scene has multiple characters, combat, pursuit, or changing geography.
4. Decide the reference set: for every character/prop/location/style that must stay consistent across beats, note whether the user supplied a photo (identity-lock refinement) or it needs generating from scratch (bootstrap a primary plate, then reuse it as the *input* reference for any secondary plate of the same subject so later generations lock onto the first, not onto the raw text description).
5. Write one fixed identity-descriptor sentence per recurring character/prop now. Reuse it verbatim everywhere that entity appears.
6. Write the reference plate prompts (Nano Banana Pro), one file per plate, using `templates/reference_plate_template.txt` and the conventions in `references/gemini-image-prompting.md`: narrative paragraph, positive scene phrasing, explicit "keep exactly the same" identity-lock language when refining from a photo, one clean uncluttered subject per image, no background clutter unless it's a location plate.
7. Write the storyboard preview prompt (Nano Banana Pro), one file, using `templates/storyboard_preview_template.txt`: sparse open-outline blocking panels covering every `P##` beat, camera/composition/pose only, explicitly labeled internally as a human preview never intended for Veo input.
8. Group `P##` beats into Veo calls by an 8-second-per-call budget (use judgment on how many beats fit — fast beats can share timestamps, a single complex beat may need the full 8s). **Default to independent calls, each with its own full `ATTACH` block**, one call per distinct camera setup/cut. Only use the extend mechanic when the cinema language chosen in step 2 is a genuinely unbroken camera move (`developing master`, `immersive tracking long-take`) or the user explicitly asks for one continuous take that runs past 8s — extend is for physically continuing a single shot, not a general tool for stringing together a multi-shot sequence. A cut-based sequence (most chases, dialogue scenes, montages) should be independent calls with consistent references, not chained extensions. Write one video prompt file per call using `templates/video_prompt_template.txt` and `references/veo-video-prompting.md`: the 5-part formula (cinematography, subject, action, context, style/ambiance), role-noun subject references matching the plate identity descriptors, dialogue in quotes, `SFX:` and `Ambient noise:` lines, timestamped beats, and an explicit `ATTACH AS ASSET:` / `ATTACH AS STYLE:` header block naming the exact plate files for that call, allocated per the asset-slot priority rule above.
9. Apply the craft-guide's effect/prop separation and count/entity/single-instant locks to every beat; keep one frozen instant per storyboard panel and one continuous action per video beat.
10. Write `00_notes.txt`: which plate attaches where and as which type, extension/continuation steps for sequences spanning multiple Veo calls (reuse the same plates on every extension call; note that Veo's native extend feature seeds from the prior clip's last ~1s automatically), and the live-verification caveats from `references/veo-video-prompting.md` (style-reference support, portrait + reference combos, current model roster).
11. Validate against the checklist below before returning file paths.

## Output Layout

```
od_prompts/<short_slug>/
  00_notes.txt                  # attach-what-where + extension guidance + live caveats
  storyboard_preview.txt        # one Nano Banana Pro prompt, human preview only
  refs/
    ref_<role>_<angle>.txt      # one Nano Banana Pro prompt per plate, e.g. ref_c1_front.txt
    ref_prop_<name>.txt
    ref_location.txt
    ref_style.txt               # only if a style plate is used
  video/
    shot_01.txt                 # one Veo 3.1 prompt per ~8s call, covers a P## range
    shot_02.txt
```

## Validation

Before finalizing an omni-director request, verify:

- No `@image#`, `@element_name`, or bracketed image-index token appears anywhere in any generated prompt file.
- Every reference plate prompt names exactly one clean subject and states, in prose, which prior image (if any) it must match exactly.
- Every video prompt's `ATTACH AS ASSET:` / `ATTACH AS STYLE:` block lists real plate filenames, respects the ≤3 asset / ≤1 style caps per call (shared across every subject in that shot, not per-character), and any recurring entity that had to be dropped from the slot allocation is named in `00_notes.txt` with a note to watch it for drift.
- No location plate is ever listed in an `ATTACH` block — location consistency is carried by repeated prose in each shot's `CONTEXT` line, and `00_notes.txt` says so explicitly if a location plate exists.
- Extend is used only for a genuinely continuous camera move; a cut-based sequence uses independent calls with matching `ATTACH` blocks per shot instead.
- Every recurring character/prop uses the same fixed identity-descriptor sentence in every plate and every video beat that includes them — no drifted rewording.
- The storyboard preview prompt contains no final color, material, or likeness detail, and its own text states it is a staging preview, not a generation input.
- Scene content is phrased positively everywhere except Veo audio-suppression lines, and reference-role exclusions (not scene negations) are the only other permitted "not/only" phrasing.
- The shared `P##` spine is identical in coverage across the storyboard preview and every video shot file — same order, same visible events, same camera/shot-scale intent — only the wording differs per model's conventions.
- Each storyboard panel is one frozen instant (no `then`/`before`/`after` inside a panel); each video beat has one continuous action with a visible result.
- Count-sensitive entities (crowds, duplicate props, repeated marks) carry an explicit total and one-instance-only language in both the storyboard and video prompts.
- `00_notes.txt` flags any Veo capability the research notes as unverified-live (style-reference support on 3.1, portrait aspect ratio with reference images, current model availability) rather than asserting it works.
- Final response returns file paths and a short attachment summary, not full prompt text, unless the user asked to see it.

## Reference Files

- `references/gemini-image-prompting.md` — Nano Banana Pro conventions: prompt formulas, multi-image binding, plate/identity technique, style-transfer scoping, text rendering, resolution/aspect values, positive-phrasing rule, camera/lens/lighting vocabulary.
- `references/veo-video-prompting.md` — Veo 3.1 conventions: prompt formula, `asset`/`style` typed reference fields and JSON shapes, first/last-frame conditioning, dialogue/SFX/ambient syntax, timestamped multi-beat prompting, duration/extension mechanics, identity-drift failure mode and mitigations, live-verification caveats.
- `references/craft-guide.md` — model-agnostic director craft carried over from prior work: cinema-language selection, dramatic shot-tag construction, cinematography layer, effect/prop separation, count/entity/single-instant locks, rhythm-and-escalation prose.
- `templates/storyboard_preview_template.txt`, `templates/reference_plate_template.txt`, `templates/video_prompt_template.txt`, `templates/assembly_notes_template.txt` — fill-in skeletons for each output file.
