# Royalti Studios — Prompt Pack Changelog

All pack releases and amendments, newest first. Every amendment archives the
previous PDF and a snapshot of its data file into `versions/` before rebuilding.

---

## Mystery & Crime Short Master Prompt Pack — v1.0 (2026-09-21)

**Status:** New release · Adult Fiction Line · 22 prompts across 6 phases · 30 pages

- New catalog entry under General/Other (section 12 → 13). The second of the three
  short-fiction packs flagged as worth building beyond the general Short Story
  pack; Horror Short remains open.
- **Prompt count: 22 — exactly the adult baseline.** No approval needed either way.
  It lands there because Phase 3 (the clue system) is four prompts no other pack in
  the library needs, which is precisely what takes it from the Short Story pack's
  20 up to baseline.
- **The problem the pack exists to solve:** a novel conceals a clue by DISTANCE
  (the reader met it two hundred pages ago and forgot). A short story has four
  thousand words and no distance to spend, so concealment has to be TECHNIQUE.
  Prompt 12 teaches eight of them — the list, the disguise, the discounted source,
  the overshadow, the premature, the absence, the split, the plain statement — each
  demonstrated on the author's own material.
- **Built backwards, like the Short Film pack.** Prompt 2 writes the true sequence
  of what actually happened (a document never published), Prompt 3 writes the
  solution before any story exists, and every prompt after is the craft of hiding
  it fairly.
- Phases: 1 Lock the Case (4) · 2 Build the Case (4) · 3 The Clue System (4) ·
  4 Structure It (3) · 5 Write It (3) · 6 Audit and Send (4).
- Load-bearing pieces: P1 is honest that a whodunit is the HARD short form (suspects
  need words) and points toward howdunit, whydunit and inverted; P4 writes out an
  explicit fair-play contract as numbered rules, adjusted to sub-genre, so Phase 6
  has something to measure against; P9's clue ladder places every clue with a
  concealment method and argues for putting the load-bearing clue EARLY, where the
  reader has no framework for it; P10 holds the line that a red herring is a true
  fact pointed wrong, never a lie, and sets the ratio giving real clues LESS
  attention than herrings; P11 tracks two timelines and audits whether information
  is delayed because the detective has not found it (structure) or because the
  author is hiding it (a breach); P15 caps the reveal at 250-400 words.
- P19, the fair-play audit, is the reason the pack exists. It runs adversarially,
  instructs the model to QUOTE the exact text supporting each step of the reasoning
  chain (asking whether a clue is present gets a yes; asking for the sentence gets
  the truth), and attempts to construct an alternative solution from what is on the
  page.
- P8 item 8 addresses the genre's hardest craft problem directly: how a first-person
  or close-third detective can register a realisation without either revealing it or
  cheating.
- Submission prompts explain principles rather than naming markets, since guidelines
  change; P22 additionally covers whether the detective should recur.
- Cover subtitle: "From the Solution Backwards to a Submittable Story".

Files:
- `Adult Fiction Line/Mystery_Crime_Short_Master_Prompt_Pack_v1.0.pdf`
- `_generator/mystery_crime_short_pack_data.py`

---

## Youth & Family Superhero Series Master Prompt Pack — v1.0 (2026-09-21)

**Status:** New release · AI Video Line · 26 prompts across 6 phases · 37 pages

- New catalog entry in the AI Video Line (section 28 → 29). The largest pack in
  the library, because it spans three jobs the other packs split up: the story and
  cast work the Superhero reading packs do, the screen production and continuity
  work the AI Short Film pack does, and the packaging (key art, title treatment)
  that nothing else covered.
- **Prompt count: 26, above the 22 baseline — and NOT because of the audience.**
  A youth pack would normally run fewer. It is up because the scope is three
  packs in one: story and cast (5 prompts), continuity and design (4), series and
  episodes (5), generation (4), packaging (2). Stated to the user in chat before
  building, with an offer to split it into a pair instead; the user chose one pack.
- **TWO LOCKS RUN THE PACK.** Prompt 1 sets the audience LEAN inside a
  youth-and-family band — MG-lean (8-12, protagonist 10-13) or YA-lean (13-17,
  protagonist 15-18) — rather than forcing a single audience, because family
  content plays to a young viewer with an adult in the room. Prompt 2 is the MODE
  LOCK — cinematic live-action look, or animated cartoon — and it carries a routing
  table stating exactly how the choice changes the design bible, the style lock,
  the plate method, the engine assignment and the kind of poster Prompt 23
  produces. The mode prompt is honest that photoreal young human faces are the
  hardest continuity problem in generated video and recommends cartoon mode for a
  first series.
- Phases: 1 Lock It (4) · 2 Cast and World (5) · 3 Lock the Look and the
  Continuity (4) · 4 The Series and the Episodes (5) · 5 Make It (4) ·
  6 Package and Release (4).
- Series-specific machinery the single-film pack does not need: a silhouette test
  so every character is identifiable at thumbnail size (P9); an expression plate
  set, because a face locked only in neutral drifts the moment a character laughs
  (P11); a locked power-effect phrase that must never be paraphrased, since it is
  the most repeated visual in a superhero series (P13 item 1); a reusable episode
  template with four rotating cold-open strategies (P15); a cliffhanger ladder
  that classifies every episode ending as PROMISES / WITHHOLDS / RESOLVES / FLAT
  and rewrites the last two (P18); establishing-shot reuse across episodes (P19
  item 9); an episode assembly template built once (P22 item 9); and a
  cross-episode drift check comparing episode one against the newest (P25 item 13).
- The key art request is answered in full at P23: mode-routed poster design
  (live-action key art conventions vs animated movie poster conventions), a
  thumbnail-size survival test, a cliché forbid list, then the actual generation
  prompt with a hard no-text rule and reserved space for the title — all text
  added in post, per P24.
- P26 item 1 carries a deliberate caution: platform policy for content aimed at
  children is strict, specific and enforced, and the prompt instructs the author to
  read current policy rather than assume.
- Cover subtitle: "From Character to Finished Episodes, Cover Included".

Files:
- `AI Video Line/Youth_Family_Superhero_Series_Master_Prompt_Pack_v1.0.pdf`
- `_generator/youth_superhero_series_pack_data.py`

---

## Flash Fiction Master Prompt Pack — v1.0 (2026-09-21)

**Status:** New release · Adult Fiction Line · 16 prompts across 5 phases

- New catalog entry under General/Other (section 11 → 12). Companion to the Short
  Story pack rather than a subset of it: that pack treats flash as one of five
  length bands (four touchpoints — the length lock, the skip note, the opening
  allocation), this one treats it as its own form.
- **Prompt count: 16, below the 22 baseline. User-approved on 2026-09-21 before
  building,** per the count policy. Reasons: the form has no scenes, no subplot,
  no scene budget, no series runway and no multi-pass drafting. Compression is the
  spine rather than a phase. 5 phases rather than 6, since revision and submission
  combine at this length.
- Covers what the general pack has no room for: the **micro sub-forms** — drabble
  at exactly 100 words, dribble at 50, hint fiction under 25 — where the count IS
  the form; **title-as-text** (P5) treated as a structural component with five
  distinct jobs, including the Missing Piece where the title supplies the fact the
  prose withholds; **character in a sentence** rather than a paragraph (P4),
  including whether to name the character at all; **flash-specific structures**
  (P7) — single image, two-beat, list, borrowed form, monologue, catalogue of a
  life, reveal, repetition — rather than the seven shapes scaled for 2,500+ words;
  the **first fifteen words** rather than a first page (P8); and **compression to
  an exact count** (P11) with a title-transfer trade for landing precisely on a
  fixed number.
- P10 deliberately instructs drafting at 130 percent of target, because cutting
  down produces a denser piece than writing to length.
- P12 is a dedicated read-aloud and rhythm pass, including final-syllable stress —
  at this length rhythm does the work structure does in longer forms.
- P15 covers the flash market ecosystem as distinct from short story markets, and
  flags exact-count calls as unusually winnable because most entrants miss the count.
- P16 item 4 records the constraint ladder as deliberate practice: write the same
  piece at 1,000, then 500, then 100 words.
- Cover subtitle: "From One Image to a Finished Piece".
- Catalog note updated: of the three genre/form-specific short fiction packs
  identified as worth building, Flash is now done; Mystery/Crime Short and Horror
  Short remain open.

Files:
- `Adult Fiction Line/Flash_Fiction_Master_Prompt_Pack_v1.0.pdf`
- `_generator/flash_fiction_pack_data.py`

---

## Short Story Master Prompt Pack — v1.0 (2026-09-21)

**Status:** New release · Adult Fiction Line · 20 prompts across 6 phases

- New catalog entry under General/Other (section 10 → 11). Distinct from the
  planned "Short Story Collection" entry, which is a different job — assembling
  and selling a set rather than writing one story. A note in the catalog records
  the distinction.
- **GENRE-GENERAL BY DESIGN**, and this is the pack's central design decision.
  Short story craft is genre-independent in a way novel craft is not: single
  effect, late entry, compression, the turn, an ending that reframes. Genre
  changes the furniture, not the engine. So Prompt 1 is a genre-and-form lock
  that names the genre, states its 5 expectations and 3 rejection triggers, names
  that genre's specific short-form problem, locks a target length from five bands,
  and issues a routing note telling the author which later prompts matter most for
  their combination. Every later prompt inherits both locks — the craft audit at
  Prompt 16 checks the story against the genre contract set at Prompt 1.
- **Prompt count: 20, below the 22 baseline. User-approved on 2026-09-21 before
  building,** per the count policy. Reasons: no subplot architecture, no chapter
  plan, no series runway, and no multi-batch drafting — a short story is drafted
  in one pass. It gains craft-density prompts instead, so it lands near baseline
  rather than far below.
- Phases: 1 Find the Story (4) · 2 Build the Situation (3) · 3 Structure It (4) ·
  4 Write It (3) · 5 Revise (3) · 6 Send It Out (3).
- Load-bearing pieces: P2 names the single effect and derives four requirements
  that become the cut test for every scene; P3 diagnoses honestly whether the idea
  is a story, an anecdote, a situation, a sketch, a premise or a compressed novel;
  P6 finds the latest possible entry point and sets a backstory budget; P8 offers
  seven short-fiction shapes rather than three acts and settles POV and tense;
  P10 separates an earned turn from withheld information; P14 is a dedicated
  compression pass instructed to cut 15 percent, to be run even when already under
  word count.
- P18-19 deliberately explain submission principles rather than naming markets,
  since guidelines, rates and reading periods change.
- Cover subtitle: "From One Idea to a Submittable Story".

Files:
- `Adult Fiction Line/Short_Story_Master_Prompt_Pack_v1.0.pdf`
- `_generator/short_story_pack_data.py`

---

## AI Short Film Master Prompt Pack — v1.0 (2026-09-21)

**Status:** New release · AI Video Line · 22 prompts across 6 phases (AI Video baseline)

- Production half of a pair: the Short Film Screenplay pack writes the script,
  this one generates it. Written to stand alone — it does NOT assume the reader
  has the three AI Video Line packs the catalog marks as released (Micro-Drama
  Foundations, 15-Second Episode System, Long-Form AI Film), whose PDFs are not
  in this repo.
- Phases: 1 Define the Film (4) · 2 Lock Continuity (4) · 3 Architect the Shots (4) ·
  4 Generate (4) · 5 Audio and Assembly (3) · 6 Finish and Release (3).
- Deliberately **engine-agnostic**. Clip lengths, costs and feature sets change
  constantly, so the prompts tell the user what to ask each model for and how to
  test it, and instruct them to check current limits rather than trusting a
  figure printed in a PDF.
- Phase 2 is the pack's argument: continuity locked before any final clip is
  generated. Includes a simplification pass (P5 item 5) that tells the author
  which character and set details to REMOVE, since every added detail is another
  thing forty generations can get wrong.
- Other load-bearing pieces: clip math with an attempt multiplier by difficulty
  and a go/no-go call (P1); a hard-zone audit for the known failure areas —
  legible text, hands, crowds, reflections, object counts (P1 item 6); a reusable
  look block pasted verbatim into every prompt (P3); the dialogue decision framed
  as the single biggest production choice, with an aggressive off-ramp audit
  (P2 item 5, P15 item 2); keyframe chaining (P11 item 3); a regeneration
  stopping rule (P16 item 3); and the best-two-seconds principle throughout.
- Audio is its own layer from P4, before any picture exists, because deciding it
  late forces regeneration.
- Cover subtitle: "From Script to Finished AI Short Film". Works-with line carries
  the AI Video Line tool stack.

Files:
- `AI Video Line/AI_Short_Film_Master_Prompt_Pack_v1.0.pdf`
- `_generator/ai_short_film_pack_data.py`

---

## Short Film Screenplay Master Prompt Pack — v1.0 (2026-09-21)

**Status:** New release · Screenwriting Line (NEW LINE) · 18 prompts across 6 phases

- **Establishes the Screenwriting Line** — scripts for human production. This is a
  new line in the catalog, distinct from the AI Video Line: 13 entries, 1 released.
  Releases live in `Screenwriting Line/`.
- **Prompt count: 18, below the 22 baseline. User-approved on 2026-09-21 before
  building,** per the count policy. Reasons: a short film has no subplot
  architecture, no series runway, no multi-batch drafting (a 10-page script is
  written in one or two passes), and no retail/metadata phase — it goes to
  festivals and production, not retail.
- Phases: 1 Find the One Thing (3) · 2 Build the Situation (3) · 3 Structure It (3) ·
  4 Write the Script (3) · 5 Make It Shootable (3) · 6 Send It Out (3).
- Built on the form's actual discipline: P1 diagnoses whether the idea is even a
  short (half of all short scripts are features with the middle deleted); P3
  writes the LAST image first and derives a backward chain of what the ending
  requires, which becomes the cut test for every later scene; P7 offers six short-film
  shapes rather than defaulting to three acts; P9 distinguishes an earned turn from
  withheld information.
- Production is treated as part of the writing: P13 is a line-producer breakdown
  against the author's real resources, P14 estimates screen time scene by scene
  rather than trusting page count, and P2 locks constraints as rules before drafting.
- Cover subtitle: "From One Idea to a Shootable Script".

**Provisional add-on modules recorded, not included:** two 4-prompt modules
(Writer-Director, Craft-Depth) are documented in `_generator/addon_modules.md`
for recommendation on future packs where they fit, at the user's request.

Files:
- `Screenwriting Line/Short_Film_Screenplay_Master_Prompt_Pack_v1.0.pdf`
- `_generator/short_film_screenplay_pack_data.py`

---

## MG Superhero Master Prompt Pack — v1.0 (2026-09-21)

**Status:** New release · Middle Grade Line · 18 prompts across 6 phases

- New catalog entry (Middle Grade Line 12 → 13). Companion to the YA and Adult
  superhero packs, but built from a different engine rather than scaled down.
- **Prompt count: 18, below the 22 adult baseline — pre-approved for MG, stated
  in chat.** The manuscript is 30,000-50,000 words (roughly a third of the adult
  pack's target), which needs fewer drafting-batch prompts, and the genre has no
  rogues-gallery phase here: one understandable antagonist carries the book. The
  two audit prompts and the publish/series prompts are also combined, since MG
  retail copy and series planning are shorter jobs.
- Phases: 1 Set It Up (3) · 2 Build the World (3) · 3 Forge the Cast (4) ·
  4 Architect the Story (3) · 5 Write the Book (3) · 6 Finish It (2).
- MG-specific machinery: a mandatory hope floor set in P1 and audited in P17;
  a power system whose costs are comic before they are serious, with a "fun list"
  (P2) the book is expected to spend an early chapter on; one trusted grown-up
  with an explicit stated limit (P8) so the hero still has to fix it; a crew where
  every member has a job the plan cannot work without (P9); a kid-scale clock
  ("before Mum gets home") in the set-piece generator (P13); and read-aloud flag
  lists built into both the drafting engine and the audit.
- P4 item 8 requires a written answer to "why can't the grown-ups solve this",
  and P17 item 15 audits that answer chapter by chapter.
- Level spec on cover: Ages 8-12, Grades 3-7, Lexile 650L-950L, GR Q-X.
- Cover subtitle: "From Origin Story to Finished Middle Grade Novel".

Files:
- `Middle Grade Line/MG_Superhero_Master_Prompt_Pack_v1.0.pdf`
- `_generator/mg_superhero_pack_data.py`

---

## YA Superhero Master Prompt Pack — v1.0 (2026-09-21)

**Status:** New release · Young Adult Line · 20 prompts across 6 phases

- New catalog entry (Young Adult Line 18 → 19), targeted at grade 12 / upper YA
  per the request. Not a revision of the Adult superhero pack — a different
  audience line means a separate pack with its own v1.0; the Adult pack is
  unchanged.
- **Prompt count: 20, below the 22 adult baseline — pre-approved for teen packs,
  stated in chat.** The identity plot absorbs what the adult pack spends on
  separate institutional machinery, so the rogues-gallery and arch-enemy prompts
  consolidate into one antagonist prompt and the two world prompts merge.
- Phases: 1 Lock the Lane (3) · 2 Build the World That Has Powers and Minors In It
  (4) · 3 Forge the Cast (4) · 4 Architect the Story (3) · 5 Write the Book (3) ·
  6 Polish, Publish, Expand (3).
- YA-specific machinery: the institutional layer is rebuilt around the powered
  MINOR — the guardian's legal exposure, the school's obligation, the programme
  (P4); a guardians prompt (P9) whose core move is the "worried wrong idea", where
  loving, intelligent adults conclude something plausible and wrong from the
  evidence; the rival as someone whose respect matters more than victory (P10);
  an antagonist whose midpoint offer is to let a tired seventeen-year-old stop
  carrying this (P11); the school-year calendar as the structural clock; and the
  "stolen year" as the YA form of collateral damage.
- P18 runs a combined power-logic and grade-12 voice audit, including a
  ventriloquism sweep and an agency check for every place an adult solves the
  protagonist's problem.
- P20 handles the graduation problem — the protagonist ages out of the premise —
  alongside a power-creep contract.
- Level spec on cover: Grade 12, Ages 17-18, Lexile 1010L+, GR X-Z+.
- Cover subtitle: "From Origin Story to Finished Upper-YA Novel".

Files:
- `Young Adult Line/YA_Superhero_Master_Prompt_Pack_v1.0.pdf`
- `_generator/ya_superhero_pack_data.py`

---

## Superhero Fiction Master Prompt Pack — v1.0 (2026-09-21)

**Status:** New release · Adult Fiction Line · 24 prompts across 6 phases

- New catalog entry under Adult Fiction Line — SFF/Speculative (section count 17 → 18).
  Superhero was not previously on the roadmap.
- **Prompt count: 24, above the 22 adult baseline.** The genre carries systems a
  single-protagonist novel in another genre does not: the world's institutional
  response to powers (P5 legal/oversight/liability, P6 media and public opinion),
  a recurring rogues gallery as a plural cast plus a separate arch-enemy who
  functions as an argument (P11, P12), and a dedicated action-prose pass (P21),
  since rendering a fight in sentences rather than panels is this genre's
  distinctive craft problem.
- Phases: 1 Define the Lane (4) · 2 Build the World That Has Powers In It (4) ·
  3 Forge the Cast (5) · 4 Architect the Story (4) · 5 Write the Book (4) ·
  6 Polish, Publish, Expand (3).
- Structural spine runs three threads in parallel — heroic plot, identity plot,
  public-opinion plot — tracked per chapter in P18 and audited in P22.
- P24 carries a power-creep contract: the author commits in writing to what the
  power will not become, and names five things to escalate instead.
- Cover subtitle: "From Origin Story to Published Novel".

Files:
- `Adult Fiction Line/Superhero_Fiction_Master_Prompt_Pack_v1.0.pdf`
- `_generator/superhero_pack_data.py`

---

## Space Opera Master Prompt Pack — v1.0 (2026-09-09)

**Status:** New release · Adult Fiction Line · 22 prompts across 6 phases (baseline)

- Standalone pack for the SFF/Speculative catalog entry. Built around the genre's
  core problem: holding galactic scale and one crew in the same book. Prompt 2
  sets a stakes ceiling the author commits to, and Prompt 20 audits for stakes
  creep against it.
- Phases: 1 Set the Scale (3) · 2 Build the Galaxy (5) · 3 Forge the Cast (4) ·
  4 Architect the Story (4) · 5 Write the Book (3) · 6 Polish, Publish, Expand (3).
- Distinctive prompts: travel rules derived into political geography (P4),
  species built from a single biological premise (P6), a reusable
  set-piece/fleet-battle generator (P15), and a multi-viewpoint braid manager
  with an information ladder (P16).
- Cover subtitle: "From Galactic Concept to Published Novel".

Files:
- `Adult Fiction Line/Space_Opera_Master_Prompt_Pack_v1.0.pdf`
- `_generator/space_opera_pack_data.py`

---

## Cyberpunk Master Prompt Pack — v1.0 (2026-09-09)

**Status:** New release · Adult Fiction Line · 22 prompts across 6 phases (baseline)

- Standalone pack for the SFF/Speculative catalog entry. Built to force an
  argument rather than an aesthetic: Prompt 1 extracts a thesis about technology
  and power, and Prompt 13 requires the plot's payload to embody it.
- Phases: 1 Set the Argument (3) · 2 Build the City (5) · 3 Cast the Expendables (4) ·
  4 Run the Job (4) · 5 Write the Book (3) · 6 Polish, Publish, Expand (3).
- Distinctive prompts: net rules with four hard constraints plus an explicit
  unhackable list (P7), an augmentation system with prices and maintenance
  burden (P6), a corporate escalation policy the plot can push against (P11),
  and a double-cross ladder capped at three rungs (P15).
- Cover subtitle: "From Neon Concept to Published Novel".

Files:
- `Adult Fiction Line/Cyberpunk_Master_Prompt_Pack_v1.0.pdf`
- `_generator/cyberpunk_pack_data.py`

---

## Dystopian & Post-Apocalyptic Master Prompt Pack — v1.0 (2026-09-09)

**Status:** New release · Adult Fiction Line · 25 prompts across 6 phases

- Covers both SFF/Speculative catalog entries (Dystopian and Post-Apocalyptic)
  in one combined pack, since most books in this space sit on the line between
  a regime that controls what is left and a landscape that has stopped
  cooperating. Prompt 1 places the author on a 1-10 control axis and routes the
  rest of the pack accordingly.
- **Prompt count: 25, above the 22 adult baseline.** The pack carries two
  distinct world engines, so it needs four prompts a single-lane pack would not:
  Prompt 1 (lane lock on the control axis), Prompt 6 (regime/control
  architecture — the dystopian engine), Prompt 7 (scarcity math and survival
  logistics — the post-apocalyptic engine), and Prompt 17 (cost ledger, which
  audits stakes across both).
- Phases: 1 Define the Break (4) · 2 Build the Broken World (5) · 3 Forge the
  People (4) · 4 Architect the Story (4) · 5 Write the Book (4) ·
  6 Polish, Publish, Expand (4).
- Cheat sheet: 10 makes, 10 kills, 8 voice essentials, a 13-station structure
  formula, and a reader-expectations paragraph.
- Cover subtitle set to "From Broken World to Published Novel".
- Catalog updated: both SFF/Speculative entries marked released, with a note
  that they ship as one pack. Catalog total recounted from the entry marks
  (181 planned + released; count recorded at that release) — the previous printed total of 179 was
  stale.

Files:
- `Adult Fiction Line/Dystopian_Post-Apocalyptic_Master_Prompt_Pack_v1.0.pdf`
- `_generator/dystopian_postapoc_pack_data.py`
