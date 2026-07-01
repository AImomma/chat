# Veo 3.1 Prompting Reference

Source: Google Cloud Blog "Ultimate prompting guide for Veo 3.1" (directly fetched), Vertex AI reference-image docs (WebSearch-synthesized, cross-checked against independent third-party API-doc mirrors), Google AI Developer Forum threads (live, dated), blog.google "Ingredients to Video" post. Claims marked **[verify live]** reflect either forum-reported bugs/partial rollouts or third-party-only corroboration and should be re-checked against the current API before being treated as fixed behavior.

## Prompt formula

`[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]`

> "Medium shot, a tired corporate worker, rubbing his temples in exhaustion, in front of a bulky 1980s computer in a cluttered office late at night. The scene is lit by the harsh fluorescent overhead lights and the green glow of the monochrome monitor. Retro aesthetic, shot as if on 1980s color film, slightly grainy."

An equivalent official breakdown used for enterprise/agent-platform guidance separates the same content into: Subject, Action, Scene/Context, Camera angle/movement, Style/aesthetic, Ambiance/lighting/mood, Audio/dialogue. Use whichever grouping is clearer for a given beat; the content required is the same, and this skill's video-prompt template keeps audio as its own explicit block since Veo's audio channels are a distinct authoring surface (see below).

## Camera vocabulary

Be literal and specific with film-industry terms, not vaguely suggestive:

- Movement: dolly shot, tracking shot, crane shot, aerial view, slow pan, POV shot.
- Composition: wide shot, close-up, extreme close-up, low angle, two-shot.
- Lens/focus: shallow depth of field, wide-angle lens, soft focus, macro lens, deep focus.

> "Crane shot starting low on a lone hiker and ascending high above, revealing they are standing on the edge of a colossal, mist-filled canyon at sunrise, epic fantasy style, awe-inspiring, soft morning light."

## Reference images: typed API fields, not prompt tags

Veo's reference mechanism lives in a `referenceImages` array on the request, separate from the prompt string. Each entry has a `referenceType`:

- **`asset`** — up to **3** images of a single person/character/product, used for identity and appearance preservation. Multiple asset images are treated as the *same* subject from different angles/contexts — not three different subjects.
- **`style`** — up to **1** image, applied as an aesthetic reference only (palette, texture, rendering style). **[verify live]** A Google AI Developer Forum thread reports `referenceImages.style` not working on Veo 3.1 as of the thread's date, with guidance to fall back to `veo-2.0-generate-exp` for style references. Confirm current support before promising a style plate will work on 3.1 — if it doesn't, fold the style intent into the video prompt's own `[Style & Ambiance]` prose instead.
- **[verify live]** A separate forum thread reports `referenceImages` (asset-type) currently limited to `16:9` output on some endpoints, i.e. portrait (`9:16`) + reference-image combinations may not be supported yet. Default to `16:9` for any shot using asset references unless you've confirmed portrait works.

Request shape (Vertex AI REST):

```json
{
  "instances": [{
    "prompt": "TEXT_PROMPT",
    "referenceImages": [
      { "image": {"bytesBase64Encoded": "...", "mimeType": "image/png"}, "referenceType": "asset" }
    ]
  }],
  "parameters": { "aspectRatio": "16:9", "durationSeconds": 8, "storageUri": "OUTPUT_STORAGE_URI" }
}
```

`google-genai` SDK shape:

```python
config=GenerateVideosConfig(
    reference_images=[
        VideoGenerationReferenceImage(
            image=Image(gcs_uri="...", mime_type="image/png"),
            reference_type="asset",
        ),
    ],
    aspect_ratio="9:16",
)
```

This skill produces prompt text plus an `ATTACH AS ASSET:` / `ATTACH AS STYLE:` header block naming which plate files go in which slot — it does not call the API directly. In the Gemini app or Google Flow, this maps to literally attaching the named image files in the "ingredients"/reference slots the UI exposes; in code, it maps to the `referenceImages` field above.

## How the prompt text refers to a reference subject

Not by ordinal, not by tag — by a consistent **role-noun description** matching how the plate was described. Official example from the "Ingredients to Video" workflow:

> "Using the provided images for the detective, the woman, and the office setting, create a medium shot of the detective behind his desk. He looks up at the woman and says in a weary voice, 'Of all the offices in this town, you had to walk into mine.'"

Note this uses role-nouns ("the detective," "the woman," "the office setting"), not "the first image" or "Image A" — Veo's documented convention differs from Nano Banana Pro's ordinal/lettered convention because the image-to-role binding already happened at the typed-field level; the prompt text just needs to name the same role consistently. Use the fixed identity-descriptor sentence from the craft phase every time a character's role-noun appears.

## First-frame / last-frame conditioning

A separate conditioning mode from `asset`/`style` references — do not conflate them. Generate a start frame and an end frame (typically with Nano Banana Pro), then prompt Veo with the **camera/motion transition connecting them**, not a content description (the endpoints are already pixel-defined):

> "The camera performs a smooth 180-degree arc shot, starting with the front-facing view of the singer and circling around her to seamlessly end on the POV shot from behind her on stage. The singer sings 'when you look me in the eyes, I can see a million stars.'"

## Dialogue and audio syntax

Veo 3/3.1 natively synthesizes three audio channels, all driven by prompt text — there is no separate audio API parameter:

- **Dialogue**: quote the literal line, attribute it in prose. `A woman says, "We have to leave now."`
- **SFX**: `SFX: thunder cracks in the distance.`
- **Ambience**: `Ambient noise: the quiet hum of a starship bridge.`

## Timestamped multi-beat prompting within one clip

An 8-second call can carry multiple sub-shots addressed by timecode — this is the direct mechanism for fitting several `P##` beats into a single Veo generation:

```
[00:00-00:02] Medium shot from behind a young explorer as she pushes aside a jungle vine to reveal a hidden path.
[00:02-00:04] Reverse shot of the explorer's face, cautious. SFX: rustle of dense leaves, distant bird calls.
[00:04-00:06] Tracking shot following her into the clearing. Emotion: wonder and reverence.
[00:06-00:08] Wide, high-angle crane shot revealing the ruins. SFX: swelling orchestral score begins.
```

Use this instead of trying to cram unrelated content into one un-timestamped paragraph — each bracketed range is effectively one storyboard panel's worth of direction.

## Duration, extension, resolution, aspect ratio

- Base generation: **8 seconds** on standard Veo 3.1 (verified against Google's published spec), resolutions `720p`/`1080p`/`4K` (4K in preview on some tiers), native synchronized audio. **[practitioner-reported, not independently verified against an official spec page]** Google's Omni model/mode currently extends single-clip generation to **10 seconds**. This skill defaults to Omni/10s unless the user asks for a shorter clip in a given request — that default is a project decision, not an official spec claim, so if you're working from this doc directly against another surface, confirm which one applies.
- Aspect ratio: `16:9` and `9:16` (portrait is a 3.1-era addition — see the reference-image + portrait caveat above).
- **Extension**: seeds from the final ~1 second (24 frames) of a prior Veo-generated clip, generates **+7 seconds** per call. **[verify live, third-party corroborated]** Up to ~20 chained extensions, ~148s max total (8 + 7×20). Extension input must itself be Veo-generated footage (not arbitrary video), 720p/1080p @ 24fps MP4. Reuse the same `asset`/`style` reference plates on every extension call for continuity — extension does not automatically carry reference bindings forward.
- Model tiers: Veo 3.1 (standard, full audio, up to 4K), Veo 3.1 Fast (cheaper/quicker, quality tradeoff), Veo 3.1 Lite (720p; verify current audio support on this tier before relying on it). **[verify live]** Third-party sources indicate Veo 2 and non-3.1 Veo 3 were slated for retirement around mid-2026 — confirm the current model roster at generation time and target Veo 3.1 by default rather than assuming an older model ID is still available.

## Negative phrasing

Same "describe what you want, not what to exclude" doctrine as Nano Banana Pro applies to visual content: "a desolate landscape with no buildings or roads" rather than "no man-made structures." **Exception, audio only:** literal negation is widely used and effective for suppressing an audio channel — `"clear dialogue; no music"`, `"no background music"`, `"faint cafe murmur; no music, no dialogue"`. This is community-validated practice, not an explicit official carve-out, but it is consistently reported as effective and is not contradicted by any official source found — treat it as the one place `no X` phrasing is the right tool.

## JSON prompting — not an API format

Some third-party guides describe "JSON prompting" for Veo. This is an authoring convention some tools' front-ends (e.g. Google's "Flow" editor) parse and flatten into prose before it ever reaches the model — it is **not** a documented raw-JSON input to the Gemini/Vertex `prompt` string field, which is plain text. If a JSON-shaped planning document is useful internally while building a prompt, that's fine, but always render it down to natural-language prose (with timestamped beats as shown above) before treating it as the final deliverable, unless the user is specifically targeting the Flow editor's JSON-import feature.

## Identity drift: why naive prompting fails, and how to fix it

Documented mechanism (Google Cloud field engineering writeup): writing the same character description twice does not reproduce the same person — the model generates a new person who loosely matches the description each time, because description-only conditioning under-constrains identity ("feature entanglement" in the model's latent space). This is very likely a direct contributor to "the reference doesn't look right" complaints when a skill relies on text description alone.

**Default mitigation (use for every recurring character):**
1. Attach the same 2–3 `asset` plates to every Veo call that character appears in.
2. Reuse the fixed identity-descriptor sentence verbatim in every beat mentioning them.
3. If a character must appear in a plate generated by Nano Banana Pro before ever reaching Veo, chain that plate as an input reference for any further plates of the same character (see `gemini-image-prompting.md`), rather than regenerating from the text description alone each time.

**Escalation if drift persists (heavier, optional):** Google's documented "forensic" pipeline uses an LLM to derive a structured facial-composite description (a machine-readable breakdown of stable facial features) from a reference image, then feeds **both** the original image and a natural-language translation of that structured profile into the generation prompt together — redundant pixel + verbal anchoring is stronger than either alone. This is a multi-stage pipeline (analysis → keyframe generation/editing → video generation), not a single-prompt trick; reserve it for characters where the default mitigation above isn't holding up across many shots, and otherwise don't add this complexity by default.
