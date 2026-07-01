# Nano Banana Pro (Gemini 3 Pro Image) Prompting Reference

Source: Google Cloud Blog "Ultimate prompting guide for Nano Banana," blog.google "7 tips" post, Google Developers Blog "How to prompt Gemini 2.5 Flash Image Generation," `ai.google.dev` prompting-strategies docs, cross-checked against third-party implementer docs where noted. Claims marked **[verify live]** could not be confirmed against a directly-fetched official page during research and should be checked against current docs before treating as fixed.

## Core doctrine: narrative prose, not tag soup

Google's own guidance explicitly tells users to stop writing keyword lists (`dog, park, 4k, realistic`) and instead write full descriptive paragraphs, "acting like a Creative Director" rather than listing disconnected tags. This is a **hard requirement carried into every prompt this skill writes** — no comma-separated tag dumps, no bracketed keyword lists, no symbolic reference tokens. Full sentences describing relationships between elements.

## Two prompt formulas

**No-reference generation:**
`[Subject] + [Action] + [Location/context] + [Composition] + [Style]`

> "A striking fashion model wearing a tailored brown dress, sleek boots, and holding a structured handbag. Posing with a confident, statuesque stance, slightly turned. A seamless, deep cherry red studio backdrop. Medium-full shot, center-framed. Fashion magazine style editorial, shot on medium-format analog film, pronounced grain, high saturation, cinematic lighting effect."

**Multimodal (with reference images):**
`[Reference images, named and scoped] + [Relationship instruction] + [New scenario]`

> "Using the attached napkin sketch as the structure and the attached fabric sample as the texture, transform this into a high-fidelity 3D armchair render. Place it in a sun-drenched, minimalist living room."

Always start with a strong verb naming the primary operation: transform, combine, place, recreate, render.

## How multiple reference images bind to text

There is no symbolic tag syntax. Images are ordered parts in the request; the prompt text then binds to them by **ordinal position** or **lettered role label**, stated in prose, before the target scene is described:

> "Take the blue floral dress from the first image and let the woman from the second image wear it."

or

> "Use Image A for the character's pose, Image B for the art style, and Image C for the background environment."

Name the references and their exact role **first**, then describe the target scene — reversing this order (describing the scene, then mentioning references as an afterthought) produces weaker binding.

## Reference image limits

- Up to **14** reference images can be mixed into a single prompt (Nano Banana Pro and Nano Banana 2/Flash both list this in the official spec table — treat 14 as the ceiling for either tier unless a fetched page says otherwise).
- Reliable **person-identity preservation** drops off well before 14 images: expect solid results up to roughly **5 distinct human identities** in one composition. **[verify live]**
- Practical guidance: start with 2–4 references per generation; if using more, put the images that must survive most faithfully in the first several slots.
- Supported input types: PNG, JPEG, WEBP, HEIC, HEIF.

## Character/subject consistency technique

Dominant documented pattern is a bootstrapped reference chain, not a single mega-prompt:

1. Generate (or accept a user photo as) one primary reference plate for the character.
2. Feed that plate back in as an input reference for every subsequent plate or scene involving the same character.
3. State explicitly in every prompt: "keep facial features, proportions, and wardrobe exactly the same as the attached reference."

This mirrors what this skill calls the identity-descriptor + repeated-plate-attachment discipline: image and text both carry the same fixed identity claim, every time.

## Style transfer and bleed prevention

Style transfer is documented directly: "recreate its exact content in a different artistic style" (e.g., a street photo → Van Gogh-style painting). No official page names "reference bleed" as a failure mode explicitly, but the consistent mitigation implied by the "name each reference's role first" doctrine is **explicit scoping**: state what a reference contributes and, when multiple people/subjects are present, what it must *not* contribute — e.g., "use Image B only for palette, lighting, and brushstroke style; do not carry over any facial features, clothing, or identity from Image B." This kind of reference-role exclusion is distinct from scene negation (see below) and is the correct tool for preventing one character's likeness or wardrobe from leaking onto another.

## Text rendering

- Put desired in-image text in quotes: `'Happy Birthday'`, `'URBAN EXPLORER'`.
- Specify typography by description or named font: "bold, white, sans-serif" or "Century Gothic 12px."
- Can request translated/localized text in the same prompt.
- If text placement/wording needs iteration, resolve the copy in a separate conversational turn first, then request the image with that finalized text — Nano Banana Pro's text rendering is strong enough to make this two-step approach worthwhile for anything longer than a short label.
- Nano Banana Pro specifically handles long, legible in-image text (full sentences/paragraphs), not just short taglines — a capability advantage over most competing image models, and a reason to be precise: any stray internal planning label (`C1`, `P##`) left in a prompt risks being rendered as literal visible text.

## Resolution and aspect ratio

- Resolutions: `1K`, `2K`, `4K` (Nano Banana Pro and Nano Banana 2); Nano Banana 2 additionally supports `0.5K` (512px).
- Aspect ratios: `1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` (both tiers); Nano Banana 2 additionally supports `1:4`, `4:1`, `1:8`, `8:1`.
- API shape **[verify live, cross-checked third-party]**: `generationConfig.imageConfig.aspectRatio` (e.g. `"16:9"`) and `generationConfig.imageConfig.imageSize` (`"1K"` / `"2K"` / `"4K"`, uppercase K; the `0.5K` value does not take the K suffix). Default aspect ratio if unspecified is `1:1`.
- If the aspect ratio must exactly match a downstream Veo generation, set it explicitly rather than relying on the default.

## Thinking / grounding

Nano Banana Pro runs a "Thinking" pass before generating — it can plan composition and, per Google, ground output in live Google Search results for factual content (current weather, real-world data, correct diagrams). Because of this planning step, you can give somewhat higher-level compositional intent ("arrange these three elements into a balanced hero shot with the logo legible") rather than hand-placing every element — though this is an inference from the capability description, not an explicit official claim that literalism matters less. When precision matters (identity, exact framing, exact text), stay literal regardless.

Search-grounded formula: `[Search/source request] + [Analytical task] + [Visual translation]`, e.g. "[Search for current weather and date in San Francisco] + [use this data to modify the scene...] + [visualize this as a miniature city-in-a-cup concept...]."

## Negative phrasing

Google explicitly discourages literal scene negation. Describe the desired positive state instead:

- Instead of "no cars" → "an empty, deserted street with no signs of traffic."
- Instead of "no clouds" → "an unbroken, solid blue sky."
- Instead of "no furniture" → "a completely bare, empty room with exposed floors."

Naming the unwanted object still feeds its tokens into generation and can cause it to appear. **This applies to scene content.** Reference-role scoping ("do not carry over Image B's facial features") is a different kind of instruction — bounding what an input contributes — and is fine to phrase with "not/only."

## Camera and material vocabulary

Use literal, specific photographic/cinematic terms, not vague mood words:

- Camera/format: "GoPro" (immersive, distorted, action feel), "Fujifilm camera" (authentic color science), "disposable camera" (raw, nostalgic flash aesthetic).
- Lens/DOF: "low-angle shot with a shallow depth of field (f/1.8)," "wide-angle lens" for scale, "macro lens" for intricate detail.
- Lighting: "three-point softbox setup," "chiaroscuro lighting with harsh, high contrast," "golden hour backlighting creating long shadows."
- Film stock/grade: "as if on 1980s color film, slightly grainy," "cinematic color grading with muted teal tones."
- Materials: name the actual material, not the category — "navy blue tweed," not "suit jacket"; "ornate elven plate armor etched with silver leaf patterns," not "armor."

## Watermarking

All Nano Banana Pro output includes an invisible SynthID watermark and C2PA content credentials. No prompting implication, but worth knowing if a generated plate is later re-used as an input reference for another generation or for Veo — the watermark does not affect usability as a reference.
