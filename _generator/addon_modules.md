# Royalti Studios — Provisional Add-On Modules

Four-prompt modules that are **not** part of any released pack, kept here so they
resurface when a relevant pack is built. Each is sized to take a pack from 18 to
22 prompts, or to extend a 22-prompt pack to 26.

**How to use this file:** when building a new pack, check the "Recommend for"
line on each module. If it matches, offer the module to the user *before*
writing — do not add it silently, and do not pad a pack with it to hit a count.
A module is only worth adding when the pack's audience would actually use it.

Origin: proposed during the Short Film Screenplay pack build (2026-09-21) as
alternatives to an 18-prompt pack. The user approved 18 and asked that both
options be recorded as provisional and recommended later where they fit.

---

## Module A — The Writer-Director Four

**Recommend for:** any screen pack whose reader is likely to direct their own
work, or to use the script as a pitch rather than a sale. Strongest fit: short
film, web series, proof-of-concept, music video, branded work, any AI Video Line
pack aimed at solo creators.

1. **The Shot-and-Coverage Pass** — converting the script into a director's
   shot plan without cluttering the page with camera direction; what belongs in
   the script versus a separate director's document.
2. **Festival and Submission Strategy** — tiers, sequencing, premiere status,
   what a submission budget should be relative to production spend, and when to
   stop.
3. **The Proof-of-Concept Pitch Package** — what the short must demonstrate that
   a script cannot, plus the accompanying feature or series materials.
4. **Short-to-Feature Expansion** — whether the piece expands, what would have to
   be built out, and the honest answer when it should not.

**Note:** items 2 and 3 partially overlap Prompts 17-18 of the released Short
Film Screenplay pack. If adding this module to that pack in a future version,
merge rather than duplicate.

---

## Module B — The Craft-Depth Four

**Recommend for:** packs aimed at writers working on prose-level craft rather
than production; dialogue-driven or character-driven genres; any pack where the
user asks for "more on the writing itself". Strongest fit: feature screenplay,
TV pilot, two-hander, literary or character-led genres, adaptation packs.

1. **Dialogue Subtext Work** — building scenes where what is said and what is
   meant diverge, and auditing a draft for characters who say what they want.
2. **The Silent / Visual Storytelling Pass** — carrying story on image and
   behaviour alone; the sound-off test and what survives it.
3. **The Single-Location Constraint** — designing a piece that never leaves one
   space, and turning that limit into the form's strength.
4. **Cold-Open and Last-Image Pairing** — designing the first and last beats as
   a matched pair so the ending answers the opening.

**Note:** item 2 partially overlaps Prompt 15 of the Short Film Screenplay pack
and item 4 partially overlaps its Prompt 3. Merge rather than duplicate.

---

## Adding a module to an existing pack

This is an amendment, not a new pack. Follow the standard versioning policy:
archive the current PDF and a snapshot of the data file into `versions/`, bump
the version (+1.0, since adding four prompts is a restructure), update
`version_date` and `total_prompts`, rebuild with the new version in the
filename, and log the change in `CHANGELOG.md`.
