# Director Craft Guide (model-agnostic)

This is the part of the process that has nothing to do with which model you're targeting — it's the same shot-design discipline regardless of whether the output goes to Veo, Seedance, or anything else. Run this before writing any Nano Banana Pro or Veo prompt text.

## Video Direction Pass

Run this before building the shared `P##` spine:

- Define the sequence intent in one sentence: start state, end state, conflict, key prop/effect, and the one visual idea the sequence must communicate.
- Create a cinematic title: 2–5 words, scene-specific, memorable, atmospheric. Favor a concrete image plus dramatic pressure, consequence, or irony over a literal slug or genre label.
- Pick one scene-appropriate cinema language and hold it for the whole sequence: `rain-noir compression`, `kinetic close-quarters action`, `procedural prop-chain escalation`, `developing master`, `immersive tracking long-take`, `suspense reveal`, `slow-burn dread`, `action chase`, `standoff escalation`, `emotional close progression`, `lyrical romantic flow`, `comedic timing coverage`, `montage`, `parallel action`, `static formal symmetry`, `epic scale vista`, `subjective POV immersion`, `surreal shift`, or `simple coverage`.
- Let the chosen cinema language control shot-angle pattern, shot-scale progression, camera motion/edit rhythm, and beat naming.
- Choose shot size by story function: geography, action readability, reaction, detail, reveal, threat, intimacy, scale, or consequence.
- Treat camera angle as dramatic language, not a neutral label — every shot needs a reason: pressure, vulnerability, scale, concealment, impact, intimacy, irony, surveillance, ritual order, speed, confusion, release.
- Avoid generic coverage drift: don't let a sequence collapse into repeated `low wide` / `side medium` / `frontal close` / `overhead wide` unless the repetition is a deliberate formal idea. Adjacent shots should normally change at least one meaningful camera dimension: height, axis, distance, foreground obstruction, subject scale, negative space, geometric emphasis.
- Add a master geography beat early (P01/P02) for multiple characters, combat, pursuit, vehicles, doors, room transitions, or changing geography.

## Dramatic Camera Language

Give each beat one primary camera idea: occlusion, negative space, compression, foreground obstruction, scale contrast, surveillance view, subject isolation, reflection, threshold framing, top-down geometry, ground evidence, object POV, silhouette, symmetry, canted imbalance, impact proximity.

Match camera ideas to genre pressure: horror/suspense → occlusion, empty space, surveillance angles, withheld threat. Action → low impact angles, diagonals, parallax layers, readable collision lines. Martial arts/dance → full-body clarity, pose geometry, arc paths, rhythm changes. Romance → distance, eyeline, shared negative space, soft barriers. Comedy → static reveals, clean wide timing, object irony. Epic scale → tiny figures against large architecture/sky/terrain. Ritual/formal → symmetry, frontal geometry, measured progression.

Design the camera progression as a sentence, not a list of coverage: `wide geography -> obstructed approach -> detail evidence -> compressed pressure -> release wide`; `clean master -> kinetic diagonals -> impact insert -> reaction isolation`; `formal symmetry -> small deviation -> broken symmetry -> consequence`. Use stronger nouns in shot tags — `void`, `trap`, `witness`, `evidence`, `impact`, `release`, `isolation`, `surveillance`, `threshold`, `pressure`, `scale`, `aftermath`, `realization` — because they name the shot's job. Prefer tags like `low root track / dark advance` or `overhead void / rear absence` over plain `low wide` or `close-up`.

## Cinematography Layer

Pick one coherent option per dimension so the whole sequence reads as a single emotional look; feed the result into the video prompt's `[Style & Ambiance]` field:

- **Lighting key**: high-key open, naturalistic motivated, low-key chiaroscuro, hard single-source, soft wrap, silhouette backlight, practical-lit, firelight/neon/screen glow. Name a motivated source.
- **Color/emotion**: warm-dominant, cool-dominant, warm/cool split, complementary tension, desaturated bleak, monochrome plus one accent, saturated heightened. Treat temperature as emotion, not decoration.
- **Lens/DOF feel**: wide = space/isolation/distortion/immersion; normal = grounded realism; long = compression/voyeurism/intimacy. Shallow DOF isolates the subject; deep DOF holds context.
- **Atmosphere**: at most one unifying layer — haze, rain, smoke, dust, heat shimmer, bloom, fine grain, clean air.

Coherence rule: lighting, color, lens, and atmosphere must reinforce one emotional read that matches the cinema language. Rain-noir compression pairs low-key chiaroscuro, cool neon palette, long-lens compression, wet haze. Comedic timing coverage pairs bright high-key light, clean warm palette, normal lenses, clear air. Avoid contradictory looks (e.g. bright high-key comedy lighting on a dread sequence).

## Effect and Prop Separation

Whenever the scene has magic, aura, smoke, dust, debris, sparks, spray, motion lines, impact bursts, light beams, or any abstract effect:

- Name the effect's origin and attachment point explicitly: from the hand, from the impact face, behind the wheel, around the doorway, along the floor path.
- Never describe an effect as a standalone object, creature, tool, or prop unless the story genuinely contains a physical object.
- If a physical prop and an effect appear together, separate them in wording: "the same physical sword remains in the lead figure's hand; one short impact arc touches the blade edge." Don't let the effect inherit prop verbs (held, carried, dropped).
- State final effect behavior in material terms in the video prompt — light, dust, smoke, debris, water, energy, motion — so it renders as a physical phenomenon, not an invented object.

## Count, Entity, and Single-Instant Locks

For any duplicate-prone scene (crowds, combat, pursuit, repeated bodies, vehicles, weapons, debris, mirrored formations):

- State the exact total and enumerate natural role/position names (`far-left guard`, `center-front guard`) rather than shorthand ranges when omission is likely.
- A fallen/dropped/broken/opened/blocked/glowing/damaged/wet/marked/missing/carried entity is the *same* role/object continuing from an earlier beat, not an extra copy — write "the same fallen guard remains in the rear lane," not "repeat fallen bodies."
- Each storyboard panel is one frozen instant — never combine two time states for the same entity in one panel (upright-then-falling, held-then-dropped). Avoid `then`, `after`, `before`, `first`, `next`, `later` inside a single panel description; split into separate `P##` beats instead.
- Each video beat is one continuous action with a visible result — cause, movement, and consequence in one beat, not a montage of unrelated states.

## Rhythm and Escalation

Write one compact prose line (not a table or per-beat score notation) describing overall tempo, build, peak, release, or unresolved ending. Use these values as internal planning vocabulary, then convert to plain prose in the actual prompt:

- Tempo: `hold`, `slow reveal`, `build`, `burst`, `impact`, `pause`, `recover`, `final hit`.
- Block: `short block`, `medium block`, `long block`.
- Beat-feel: `clean beat`, `match beat`, `smash beat`, `held beat`, `whip beat`.
- Escalation: `L1 calm` → `L5 peak`; curve: `flat`, `rise`, `spike`, `drop`, `release`, `unresolved`.

## Panel and Beat Writing

**Storyboard panel** (one frozen instant, drawable, dramatically framed):
`P## / viewpoint-function tag / beat name: camera angle + shot scale + composition pressure + role silhouette pose + screen position + object/effect state + spatial relation + visible result.`

> `P05 / low rear evidence / skyscraper pass: camera looks downhill from behind the rider's trailing head; the rider silhouette lies feet-first in the slide, one hand in water, simple tower blocks outside, water streaks show downhill direction.`

Keep storyboard panels free of: camera movement terms (dolly, orbit, crane — convert to a still angle/viewpoint instead), numeric/named lens tags (unless the user explicitly wants them in panel headers), time-progression wording (`then`/`after`/`before`), audio/SFX, final render style, palette, or material finish. Panels are open-outline, sparse, schematic — enough to validate blocking and camera, not a finished illustration, and never the source of final color or identity.

**Video beat** (one continuous action, final completion detail):
`camera angle/movement + story-motivated lens behavior + trigger + movement + reaction gesture + spatial relation + final physical prop identity + final effect behavior/material + visible result.`

Convert emotion into visible behavior: posture, distance, eye-line, hand tension, pace, hesitation, recoil, commitment, stillness. Preserve world logic through props and consequences (carried, dropped, broken, opened, blocked, glowing, damaged, missing, wet, marked, changed). Every beat should advance action, emotion, geography, or consequence — end sequences with impact, reveal, unresolved motion, pursuit, danger, collision, transformation, or changed meaning where the premise calls for a payoff.
