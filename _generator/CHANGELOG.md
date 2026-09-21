# Royalti Studios — Prompt Pack Changelog

All pack releases and amendments, newest first. Every amendment archives the
previous PDF and a snapshot of its data file into `versions/` before rebuilding.

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
