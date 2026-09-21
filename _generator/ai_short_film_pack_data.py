# -*- coding: utf-8 -*-
"""
Royalti Studios - AI Short Film Master Prompt Pack (AI Video Line).

Companion to the Short Film Screenplay pack (Screenwriting Line): that one gets
you a shootable script, this one gets that script generated.

Build with:
    python pack_builder.py ai_short_film_pack_data \
        "AI_Short_Film_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.

NOTE: the catalog marks three AI Video Line packs as released (Micro-Drama
Foundations, 15-Second Episode System, Long-Form AI Film & Clip-Down System)
whose PDFs are not in this repo. This pack is written to stand alone and does
not assume the reader has them.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "AI SHORT FILM",
    "total_prompts": 22,
    "hook_line": "Turn one script into one finished short film - continuity locked, shot by shot, clip by clip, with audio built as its own layer.",
    "keyword_lines": [
        "Continuity locks • Reference plates • Clip math • Keyframe chaining • Regeneration budget",
        "Look lock • Per-engine prompts • Dialogue and lip-sync • Score and sound design • Assembly",
    ],
    "subgenres_line": "Suits: Narrative Short (3-15 min), Micro-Short, Proof-of-Concept, Silent/Visual Piece, Genre Calling-Card, Book Trailer, Music-Led Short, Animated Short",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-21",
    "audience_line": "AI Video Line",
    "cover_h2": "From Script to Finished AI Short Film",
    "works_with_line": "Works with ChatGPT • Claude • Midjourney • Nano Banana Pro • Google Veo • Kling • Seedance",
    "closing_tagline": "The engines are not the hard part. Continuity is. Lock it first and the film assembles itself.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "This pack takes a finished short film script and generates it. It is the production half of a "
        "pair - the Short Film Screenplay pack writes the script, this one shoots it. If you do not have a "
        "script yet, Prompt 2 will help you shape a premise that AI can actually deliver, but you will get "
        "a far better film by writing it properly first. The order here is deliberate and unforgiving: "
        "feasibility and look before anything, then continuity locks, then shots, then generation. Every "
        "team that skips the locks and starts generating pretty clips ends up with forty beautiful shots "
        "of four different people. Engines change constantly, so this pack is written to be "
        "engine-agnostic: it tells you what to ask each model for and how to test it, and never assumes a "
        "specific clip length or feature set. Check your engine's current limits and fill them in where "
        "the prompts ask."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-4) - Define the film. Feasibility and clip math against your real budget, a "
        "premise shaped for what AI does well, a look lock, and an audio plan - because audio is always "
        "its own layer and deciding it late costs the most.",
        "Phase 2 (Prompts 5-8) - Lock continuity. The continuity bible, character reference plates, "
        "location and set locks, and prop and wardrobe locks. This phase is the whole game.",
        "Phase 3 (Prompts 9-12) - Architect the shots. Shot list with clip math, scene-by-scene "
        "breakdown, the keyframe plan, and transitions and chaining between clips.",
        "Phase 4 (Prompts 13-16) - Generate. Reference-image prompts, video prompts per engine, the "
        "dialogue and lip-sync plan, and a regeneration strategy with a fix-it budget.",
        "Phase 5 (Prompts 17-19) - Audio and assembly. Score and sound design, voice and dialogue "
        "production, then edit assembly and pacing.",
        "Phase 6 (Prompts 20-22) - Finish and release. The QC audit for continuity and artifacts, titles "
        "and deliverables, and the release plan.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool, your image and video generation tools, and a place to save your "
        "outputs and asset IDs between prompts. Brackets like [THIS] are placeholders - replace them with "
        "your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular. Making a silent piece? Prompt 15 becomes a light "
        "pass and Prompt 17 becomes the most important prompt in the pack. No human characters? Prompts 6 "
        "and 15 shrink dramatically. Animated rather than photoreal? Prompt 3's look lock carries more "
        "weight and your continuity problem gets easier."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "Continuity locked BEFORE a single final clip is generated - reference plates for every face, set and prop",
            "Clip math done honestly: shot count times attempts per shot against your actual budget and time",
            "A look lock written as a reusable text block that goes into every single prompt, unchanged",
            "Shots designed for what the engines do well - short duration, single clear action, limited camera moves",
            "Keyframe chaining, where the last frame of one clip seeds the first of the next",
            "Audio treated as its own layer from Prompt 4, never as something added at the end",
            "A regeneration budget assigned per shot, so the hero shots get the attempts and the rest do not",
            "A script and shot list that exist before generation, so you are producing a film rather than collecting clips",
            "Deliberate limits on what you ask of the tools - the films that work avoid the things that break",
            "An edit that cuts around weakness, using the strongest two seconds of each generated clip",
        ],
        "kills": [
            "Generating pretty clips first and hoping a film emerges - it never does",
            "No reference plates, producing a cast whose faces drift between every shot",
            "A look described differently in each prompt, so the grade, lens character and lighting wander",
            "Asking a single clip to contain multiple actions, a dialogue exchange, and a camera move",
            "Long clips where short ones would cut better and cost a fraction",
            "Discovering the audio plan after the picture is locked, which forces re-generation",
            "Unlimited regeneration on shot one, leaving no budget for the shot the film depends on",
            "Hiding weak generation behind faster cutting until the film reads as a trailer with no scenes",
            "Text, hands, crowds, reflections, specific logos and continuity of small objects - the known failure zones, walked into",
            "Claiming a runtime the shot count cannot support, and padding with drone shots and dissolves",
        ],
        "voice": [
            "Write prompts as camera-and-action instructions, not as prose - the engines reward concrete nouns and verbs",
            "One action per clip, stated plainly, with a clear start state and end state",
            "Keep the look block identical across every prompt; paste it, never retype it",
            "Name the shot size and lens character rather than a feeling: medium close, 40mm character, shallow",
            "Specify light by source and direction, not by mood word",
            "Say what is NOT in frame when it matters, because engines fill space",
            "Give the subject a single, unambiguous physical description that matches the reference plate exactly",
            "Log every prompt and its seed or asset ID; an unreproducible good result is a lost result",
        ],
        "formula": (
            "Feasibility and Clip Math -> The Look Lock -> The Audio Plan -> The Continuity Bible -> "
            "Character, Set and Prop Plates -> The Shot List -> The Keyframe Plan -> Reference Image "
            "Generation -> Clip Generation, Hero Shots First -> Selects and Regeneration -> Audio Layers "
            "Built Separately -> Assembly and Pacing -> QC Pass -> Titles and Deliverables -> Release"
        ),
        "reader_expectations": (
            "An audience watching an AI short is asking two questions at once: is this a story, and is it "
            "holding together? They forgive a great deal of texture weirdness if the characters stay the "
            "same person, the space stays the same space, and the cutting has intention. They stop "
            "watching when a face changes between shots, when the film is a sequence of beautiful "
            "unconnected images, or when the audio is obviously an afterthought. Festival programmers and "
            "producers watching these are additionally asking whether you made choices or accepted "
            "outputs. The films that travel are the ones where the limitations look like style - a locked "
            "look, deliberate shot vocabulary, and an edit that knows exactly which two seconds of each "
            "clip are good."
        ),
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "The hard part of AI filmmaking is not generation. It is that generation has no memory - every "
        "clip is a fresh guess, and your job is to constrain those guesses until they agree with each "
        "other. That is what Phase 2 is for, and it is the phase everyone skips because reference plates "
        "are not fun and clips are. Do it anyway. Lock your look, plate your cast, budget your "
        "regenerations, and your film will assemble. Then cut it hard: find the best two seconds of every "
        "clip and build from those. Engines will change again before you finish reading this - the "
        "discipline will not."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: DEFINE THE FILM",
        "intro": (
            "Four prompts before you generate anything. Work out whether the film is makeable at your "
            "budget, shape the premise around what the engines actually do well, lock the look as a "
            "reusable block, and plan audio now rather than later."
        ),
        "prompts": [
            {
                "title": "Feasibility and Clip Math",
                "desc": (
                    "The prompt that prevents abandoned projects. It converts your script into a shot "
                    "count, a generation count and a real cost, before you spend anything."
                ),
                "prompt_text": (
                    "You are an AI film producer who budgets generative video projects and is blunt about "
                    "what cannot be finished.\n\n"
                    "My script or premise: [PASTE THE SCRIPT, OR DESCRIBE THE FILM IN 3-5 SENTENCES]\n"
                    "Target runtime: [E.G. 8 MINUTES]\n"
                    "My tools and their current limits: [NAME YOUR IMAGE AND VIDEO ENGINES, AND STATE THE "
                    "MAX CLIP LENGTH AND COST PER GENERATION AS THEY STAND TODAY - CHECK, DO NOT GUESS]\n"
                    "My budget and deadline: [BE HONEST]\n\n"
                    "Do the following:\n\n"
                    "1. THE SHOT COUNT: from my script or premise, estimate how many distinct shots this "
                    "film needs. Then divide my target runtime by my engine's usable clip length to sanity "
                    "check it, and tell me the realistic shot count.\n"
                    "2. THE ATTEMPT MULTIPLIER: state how many generation attempts per shot to budget for "
                    "at three difficulty levels - simple (a landscape, an object, no people), moderate (one "
                    "character, one clear action), hard (dialogue, hands, two characters interacting, "
                    "specific continuity). Be realistic rather than optimistic.\n"
                    "3. THE TOTAL GENERATION BUDGET: shot count times attempts, split by difficulty, "
                    "against my stated budget and cost per generation. Tell me plainly whether this film "
                    "is affordable. If it is not, say so now.\n"
                    "4. THE TIME BUDGET: how long this takes in wall-clock hours, including generation "
                    "queue time, selection, and the assembly work. Filmmakers underestimate this by a "
                    "factor of three - correct me.\n"
                    "5. THE CUT-DOWN OPTIONS: three versions of this film that cost less - a shorter "
                    "runtime, a reduced shot count with longer holds, or a narrower scope (fewer "
                    "characters, one location). Say what each loses.\n"
                    "6. THE HARD-ZONE AUDIT: go through my script and flag everything that sits in a known "
                    "failure zone for current generative video - legible text, hands doing fine tasks, "
                    "crowds, mirrors and reflections, specific branded objects, an animal behaving to "
                    "instruction, two characters touching, continuity of a small object across shots, "
                    "anything requiring an exact number of things. For each, give me the workaround or the "
                    "rewrite.\n"
                    "7. THE HERO SHOTS: identify the 3-5 shots the film cannot succeed without. These get "
                    "the regeneration budget; everything else gets rationed.\n"
                    "8. THE GO/NO-GO: state plainly whether to proceed as scoped, proceed with a named "
                    "cut-down, or rescope entirely.\n\n"
                    "End by asking me what I would cut first if I ran out of money halfway, so we build "
                    "the shot order around that answer."
                ),
                "pro_tip": (
                    "Item 7 governs everything downstream. Decide your hero shots now and generate them "
                    "FIRST, not last - if the shot the film depends on turns out to be impossible, you "
                    "want to know on day one, not after you have paid for thirty others."
                ),
            },
            {
                "title": "The Premise, Shaped for Generation",
                "desc": (
                    "Some stories are far cheaper to generate than others. This prompt reshapes your "
                    "premise toward what the tools do well without hollowing out the film."
                ),
                "prompt_text": (
                    "You are an AI film director who has finished several generative shorts and knows "
                    "which story choices make production possible.\n\n"
                    "My script or premise: [PASTE OR DESCRIBE]\n"
                    "My hard-zone audit and hero shots: [PASTE FROM PROMPT 1]\n\n"
                    "Do the following:\n\n"
                    "1. THE GENERATION-FRIENDLY AUDIT: rate my premise 1-10 on how well it suits current "
                    "generative video, and explain the score.\n"
                    "2. WHAT THESE TOOLS DO BEATIFULLY: list 10 things generative video is currently "
                    "excellent at - atmosphere, weather, scale, landscape, slow movement, texture, "
                    "isolation, faces in repose, water, light through things. Then tell me which of these "
                    "my film is currently using, and which it is leaving on the table.\n"
                    "3. THE REPLACEMENTS: for each item in my hard-zone audit, propose a story-level "
                    "replacement that achieves the same beat - a reaction instead of an action, sound "
                    "instead of sight, a cut away instead of a continuous move, one character instead of "
                    "two, an object held still instead of manipulated.\n"
                    "4. THE CHARACTER COUNT: state how many distinct human characters this film should "
                    "have given my budget, and which of my current characters to merge or cut. Every "
                    "additional face is a full continuity problem.\n"
                    "5. THE DIALOGUE DECISION: recommend one of - no dialogue at all, off-screen or "
                    "voiceover dialogue, or on-screen lip-synced dialogue - and be explicit about the cost "
                    "and risk difference between them. This is the single biggest production decision in "
                    "an AI short.\n"
                    "6. THE LIMITATION-AS-STYLE MOVES: 5 ways to make my constraints read as deliberate "
                    "aesthetic choices - a locked-off camera vocabulary, a single time of day, a "
                    "consistently obscured face, a format or aspect ratio, a grain and colour treatment.\n"
                    "7. THE REVISED PREMISE: restate my film in 4-5 sentences with all of the above "
                    "applied, and tell me honestly what it lost and what it gained.\n\n"
                    "End by asking me which story element I refuse to compromise, so we design the "
                    "production around protecting it."
                ),
                "pro_tip": (
                    "Item 5 is the decision to make consciously. A short with no dialogue, or with all its "
                    "dialogue off-screen, removes the single largest source of AI-video failure and buys "
                    "you the budget to make everything else excellent."
                ),
            },
            {
                "title": "The Look Lock",
                "desc": (
                    "One reusable text block that goes into every prompt unchanged. This is what stops "
                    "your film's grade, lens character and lighting from wandering shot to shot."
                ),
                "prompt_text": (
                    "You are a cinematographer and colourist writing a reusable look specification for a "
                    "generative film.\n\n"
                    "My revised premise: [PASTE FROM PROMPT 2]\n"
                    "My tone and genre: [DESCRIBE]\n"
                    "Reference feelings or images I am drawn to: [DESCRIBE, OR SAY 'YOU CHOOSE']\n\n"
                    "Do the following:\n\n"
                    "1. THE LOOK BLOCK: write a single paragraph of 60-90 words that specifies this film's "
                    "visual identity in engine-readable terms - format and aspect ratio, film stock or "
                    "sensor character, grain, lens character and focal length range, depth of field, colour "
                    "palette with specific colours named, contrast and black level, and light quality. This "
                    "block goes verbatim into every single prompt. Make it tight enough to paste and "
                    "specific enough to constrain.\n"
                    "2. THREE ALTERNATIVES: two other look blocks for the same film, each implying a "
                    "different register, so I can compare before locking.\n"
                    "3. THE LIGHTING RULES: 5 rules about light in this film - where it comes from, what "
                    "time of day, what is never lit, whether faces are ever fully visible.\n"
                    "4. THE CAMERA VOCABULARY: the specific and deliberately limited set of shot sizes and "
                    "camera behaviours this film uses. Name 5-7 and forbid everything else. A limited "
                    "vocabulary is the cheapest route to a film that looks directed.\n"
                    "5. THE MOVEMENT RULE: state how much camera movement this film permits. Generative "
                    "video handles slow, simple moves far better than complex ones - set a rule and stick "
                    "to it.\n"
                    "6. THE PALETTE: 5 specific colours with their role - the dominant, the environment, "
                    "the accent that appears only at the turn, the skin-tone treatment, the black.\n"
                    "7. THE TEXTURE PASS: what this film's surfaces look like - wet, dusty, worn, clinical "
                    "- as a phrase I can append.\n"
                    "8. THE NEGATIVE BLOCK: a short reusable list of what must NEVER appear - specific "
                    "artifacts, styles, colour casts, lens effects, on-screen text. This goes into every "
                    "prompt alongside the look block.\n\n"
                    "End by asking me whether this look is achievable consistently in my chosen engine, "
                    "and what to test first with a single throwaway generation."
                ),
                "pro_tip": (
                    "Test the look block on three completely unrelated subjects before you lock it. If a "
                    "face, a room and a landscape all come back feeling like the same film, the block is "
                    "working - if not, it is too vague and will drift across forty shots."
                ),
            },
            {
                "title": "The Audio Plan",
                "desc": (
                    "Audio is always its own layer, and deciding it late is the most expensive mistake in "
                    "AI filmmaking. This prompt plans it before a frame is generated."
                ),
                "prompt_text": (
                    "You are a sound designer and composer planning the audio for a generative short film "
                    "before picture generation begins.\n\n"
                    "My revised premise and dialogue decision: [PASTE FROM PROMPT 2]\n"
                    "My look and tone: [PASTE FROM PROMPT 3]\n"
                    "My runtime: [FROM PROMPT 1]\n\n"
                    "Do the following:\n\n"
                    "1. THE LAYER MAP: list every audio layer this film needs - dialogue or voice, "
                    "ambience per location, specific sound effects, foley, score, silence - and state which "
                    "tool or method produces each. Make clear that none of these come out of the video "
                    "generator.\n"
                    "2. THE DIALOGUE PRODUCTION PATH: given my dialogue decision from Prompt 2, specify "
                    "how the voice is produced - recorded human, synthesised voice, or none - and what that "
                    "requires. If synthesised, note that voice and lip-sync are separate problems and say "
                    "how each is solved.\n"
                    "3. THE PICTURE CONSEQUENCES: state what this audio plan requires from the picture. "
                    "Lip-synced dialogue demands specific shot choices; voiceover frees the camera "
                    "entirely. Name every shot-level constraint my audio plan imposes, so Phase 3 respects "
                    "it.\n"
                    "4. THE SCORE BRIEF: 100-150 words describing this film's music - instrumentation, "
                    "tempo, where it enters and where it stops, and whether it ever carries the film alone. "
                    "Written so it can be handed to a composer or a music generator.\n"
                    "5. THE SILENCE PLAN: where this film has no music and no ambience. In a short, silence "
                    "is the strongest audio tool available and it is free.\n"
                    "6. THE AMBIENCE LIST: for each location, the specific bed of sound that establishes "
                    "it, plus one sound unique to that place.\n"
                    "7. THE SOUND-CARRIES-STORY LIST: 5 moments where sound rather than picture does the "
                    "work. These are also the cheapest moments in the film - a sound with a static or "
                    "simple shot costs a fraction of an action clip.\n"
                    "8. THE SYNC RISK: name every place the audio must match picture precisely, since "
                    "that is where generated footage will fight you.\n\n"
                    "End by asking me whether I can get a real human voice for this film, because that one "
                    "resource changes more than any other single choice."
                ),
                "pro_tip": (
                    "Item 7 is a budget tool as much as a craft one. A held shot of a face with the right "
                    "sound off-screen is both the most affordable moment you can generate and often the "
                    "best one in the film."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: LOCK CONTINUITY",
        "intro": (
            "This phase is the whole game, and it is the one everyone skips because plates are not as fun "
            "as clips. Four prompts: the continuity bible, then reference plates for every face, every "
            "space and every object that must stay the same. Do not generate a single final clip until "
            "this is done."
        ),
        "prompts": [
            {
                "title": "The Continuity Bible",
                "desc": (
                    "The master document every later prompt draws from. One place where every locked "
                    "description lives, worded identically every time it is used."
                ),
                "prompt_text": (
                    "You are a continuity supervisor building the reference document for a generative "
                    "short film. You know that generation has no memory and that consistency comes only "
                    "from identical wording.\n\n"
                    "My revised premise: [PASTE FROM PROMPT 2]\n"
                    "My look block and negative block: [PASTE FROM PROMPT 3]\n"
                    "My script or scene list: [PASTE]\n\n"
                    "Build my CONTINUITY BIBLE:\n\n"
                    "1. THE LOCK INVENTORY: list everything in this film that must stay consistent across "
                    "shots - each character, each location, each significant prop, each costume, any "
                    "vehicle, any animal, and the time of day per scene. This is my lock list.\n"
                    "2. THE WORDING RULE: explain why each locked element needs one fixed description used "
                    "verbatim every time, and what happens when a writer paraphrases it instead.\n"
                    "3. THE DESCRIPTION BLOCKS: for every item on the lock list, write its canonical "
                    "description as a short block of 25-50 words, using concrete physical nouns only - no "
                    "mood, no backstory, no adjectives an engine cannot render. These blocks get pasted "
                    "into prompts unchanged.\n"
                    "4. THE DRIFT RISKS: for each character, name the specific features most likely to "
                    "drift between generations - hair length, exact age, build, a scar, eye colour, a "
                    "garment detail - and tell me which to over-specify as a result.\n"
                    "5. THE SIMPLIFICATION PASS: go through my locked elements and tell me which details "
                    "to REMOVE to make consistency achievable. An intricate costume, patterned fabric, "
                    "jewellery, a specific tattoo or legible text will not survive forty generations - "
                    "recommend the simpler version of each.\n"
                    "6. THE CONTINUITY LOG TEMPLATE: give me the table I should keep while generating - "
                    "shot number, elements present, asset or seed IDs used, what was approved, what "
                    "drifted. Specify the columns.\n"
                    "7. THE STATE CHANGES: any element that must change during the film - a wound, a "
                    "stain, wet clothing, a broken object - with its state written per scene, since "
                    "progression is as hard as consistency.\n"
                    "8. THE ONE-FACE RULE: state which single character absolutely must stay identical, "
                    "and accept looser tolerance on the rest. Ranking this now means the regeneration "
                    "budget goes to the right face.\n\n"
                    "End by asking me which locked element I have described in the most complicated way, "
                    "so we can simplify it before it costs me the film."
                ),
                "pro_tip": (
                    "Item 5 is the counter-intuitive one that saves projects. Every detail you add to a "
                    "character is another thing the engine can get wrong - a plain grey coat is a "
                    "continuity asset, and an embroidered jacket is a forty-shot liability."
                ),
            },
            {
                "title": "Character Reference Plates",
                "desc": (
                    "Reference images that lock each face before any clip is made. This prompt writes the "
                    "plate prompts and the test that proves a lock is holding."
                ),
                "prompt_text": (
                    "You are a character reference artist producing lock plates for a generative film.\n\n"
                    "My character description blocks: [PASTE FROM PROMPT 5 ITEM 3]\n"
                    "My look block and negative block: [PASTE FROM PROMPT 3]\n"
                    "My drift risks and one-face rule: [PASTE FROM PROMPT 5]\n"
                    "My image engine: [NAME IT]\n\n"
                    "For each character, do the following:\n\n"
                    "1. THE PLATE SET: specify which reference images I need to lock this person - a "
                    "neutral front, a three-quarter, a profile, a full-length for wardrobe and proportion, "
                    "and one in the film's actual lighting. Say which are essential and which are optional "
                    "for a film of my scale.\n"
                    "2. THE PLATE PROMPTS: write the actual generation prompt for each plate. Each must "
                    "contain the character's canonical description block verbatim, a neutral background, "
                    "even lighting for the identity plates, and my negative block. Do not include the "
                    "film's stylised look in the identity plates - lock the person first, style later.\n"
                    "3. THE IN-FILM PLATE: a separate prompt placing the locked character in the film's "
                    "look and lighting, to confirm the identity survives the style.\n"
                    "4. THE CONSISTENCY TEST: a specific test to run before approving a lock - generate "
                    "the same character in three different described situations and compare. Tell me "
                    "exactly what to compare and what tolerance is acceptable.\n"
                    "5. THE REJECTION CRITERIA: what disqualifies a plate. Be specific - asymmetry that "
                    "will not repeat, an ambiguous age, hair that could read two lengths, a garment detail "
                    "the engine invented.\n"
                    "6. THE ASSET DISCIPLINE: how to name, store and log approved plates so every later "
                    "prompt references the right file. Give me a naming convention.\n"
                    "7. THE REFERENCE METHOD: explain the difference between locking identity by reference "
                    "image versus by text description alone, and tell me which my engine supports and how "
                    "to use it. If my engine accepts reference images, say how many and what kind work "
                    "best.\n"
                    "8. THE DRIFT MONITOR: how to check for slow drift across a long generation session, "
                    "and when to stop and re-plate.\n\n"
                    "End by asking me to generate the one-face-rule character's plates first and report "
                    "back before going further, because everything else depends on that lock holding."
                ),
                "pro_tip": (
                    "Lock identity on a plain background with flat light before you ever apply the film's "
                    "look. Style and identity fight each other, and a face locked inside a heavy grade "
                    "will fall apart the moment the lighting changes."
                ),
            },
            {
                "title": "Location and Set Locks",
                "desc": (
                    "Spaces drift as badly as faces, and audiences notice a room rearranging itself. This "
                    "prompt plates every location and establishes its geography."
                ),
                "prompt_text": (
                    "You are a production designer creating location lock plates for a generative film.\n\n"
                    "My location description blocks: [PASTE FROM PROMPT 5 ITEM 3]\n"
                    "My look block, lighting rules and camera vocabulary: [PASTE FROM PROMPT 3]\n"
                    "My scene list and time of day per scene: [PASTE]\n\n"
                    "For each location, do the following:\n\n"
                    "1. THE ESTABLISHING PLATE: a prompt for the wide reference image that defines this "
                    "space - its layout, what is in it, where light enters.\n"
                    "2. THE ANGLE SET: prompts for 3-4 additional plates covering the angles my shot list "
                    "will need from this space, each consistent with the establishing plate.\n"
                    "3. THE GEOGRAPHY NOTE: write down where things are in relation to each other - the "
                    "door, the window, the light source, the furniture. Generated shots will contradict "
                    "each other unless this is fixed and stated in every prompt.\n"
                    "4. THE SCREEN-DIRECTION RULE: which way characters face, enter and exit in this "
                    "space, so cuts do not flip the geography. State the rule per location.\n"
                    "5. THE TIME-OF-DAY VERSIONS: if a location appears at more than one time of day, a "
                    "plate prompt for each, with what stays fixed and what changes.\n"
                    "6. THE SIMPLIFICATION PASS: what to strip out of each space. Cluttered environments "
                    "will not repeat - tell me what to remove and what single distinctive element to keep "
                    "as the space's signature.\n"
                    "7. THE SIGNATURE ELEMENT: for each location, the one object or feature that appears "
                    "in every shot of that space so an audience knows where they are instantly.\n"
                    "8. THE CHEAT LIST: 4 ways to imply a space I cannot generate consistently - a "
                    "fragment, a sound, a doorway, a reflection avoided.\n\n"
                    "End by asking me which location appears in the most shots, because that is the one "
                    "whose geography I must write down most carefully."
                ),
                "pro_tip": (
                    "Item 7 does an enormous amount of work for almost nothing. One distinctive lamp, "
                    "window shape or piece of graffiti in every shot of a room convinces an audience it is "
                    "the same room even when everything around it has quietly rearranged."
                ),
            },
            {
                "title": "Prop, Wardrobe and Small-Object Locks",
                "desc": (
                    "The failure zone nobody plans for. A prop that changes shape between shots breaks a "
                    "scene more visibly than a whole set drifting."
                ),
                "prompt_text": (
                    "You are a props and costume supervisor locking small elements for a generative film. "
                    "You know these are where continuity most visibly fails.\n\n"
                    "My lock inventory: [PASTE FROM PROMPT 5 ITEM 1]\n"
                    "My script or scene list: [PASTE]\n"
                    "My look block: [FROM PROMPT 3]\n\n"
                    "Do the following:\n\n"
                    "1. THE STORY PROPS: every object that matters to the plot - it is handled, exchanged, "
                    "hidden, broken, or looked at. For each: its canonical description block, and how many "
                    "shots it appears in.\n"
                    "2. THE HANDLING WARNING: for each story prop, flag whether the script requires a "
                    "character to manipulate it on screen. Hands plus small objects is the single hardest "
                    "thing to generate - for each instance, give me the workaround: cut away, shoot the "
                    "reaction, have it already done, frame it out, or use sound.\n"
                    "3. THE WARDROBE LOCKS: each character's costume as a canonical block, deliberately "
                    "simplified. Flag any pattern, logo, text, intricate fastening or jewellery and "
                    "recommend the plain replacement.\n"
                    "4. THE PLATE PROMPTS: reference plate prompts for each story prop and each costume, "
                    "shot plain against neutral background so they can be matched later.\n"
                    "5. THE STATE PROGRESSION: for any prop or costume that changes across the film - "
                    "dirtied, torn, wet, bloodied, emptied - write the state per scene, with a plate prompt "
                    "per state.\n"
                    "6. THE TEXT PROBLEM: list every place my film needs legible text on screen - a sign, "
                    "a note, a phone, a label, a headline. For each, give me the production solution: "
                    "add it in post, frame it out, replace with voiceover, or use a shape the audience "
                    "reads without reading.\n"
                    "7. THE COUNT PROBLEM: anywhere the film requires a specific number of objects, "
                    "people, fingers or repetitions. Flag each and simplify.\n"
                    "8. THE ACCEPT-DRIFT LIST: the elements where inconsistency genuinely does not matter, "
                    "so I stop spending attention on them.\n\n"
                    "End by asking me which prop the film's ending depends on, so we over-plate that one "
                    "and route the regeneration budget toward it."
                ),
                "pro_tip": (
                    "Item 6 is non-negotiable: never ask a video generator for legible text. Add titles, "
                    "signs and screens in post, where they cost nothing and are correct every time."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: ARCHITECT THE SHOTS",
        "intro": (
            "Four prompts converting a script into a generation plan: a shot list with real clip math, a "
            "scene-by-scene breakdown, a keyframe plan, and the transitions that stitch clips into scenes "
            "rather than a slideshow."
        ),
        "prompts": [
            {
                "title": "The Shot List and Clip Math",
                "desc": (
                    "Every shot, its duration, its difficulty and its generation budget - the document you "
                    "will actually work from for the rest of the production."
                ),
                "prompt_text": (
                    "You are a first assistant director building a shot list for a generative film, "
                    "working within engine clip limits.\n\n"
                    "My script: [PASTE]\n"
                    "My camera vocabulary and movement rule: [PASTE FROM PROMPT 3]\n"
                    "My engine's usable clip length and cost: [STATE IT]\n"
                    "My hero shots and attempt multipliers: [PASTE FROM PROMPT 1]\n"
                    "My audio plan's shot constraints: [FROM PROMPT 4 ITEM 3]\n\n"
                    "Build my SHOT LIST. For every shot:\n\n"
                    "1. Shot number and the scene it belongs to.\n"
                    "2. Shot size and camera behaviour, drawn only from my approved camera vocabulary.\n"
                    "3. Duration in seconds - and confirm it is inside my engine's usable clip length. "
                    "Where a beat needs longer, split it into two shots and say so.\n"
                    "4. What happens: ONE clear action with a start state and an end state. If a shot "
                    "contains two actions, split it.\n"
                    "5. Which locked elements appear - characters, location, props - referenced by their "
                    "canonical blocks.\n"
                    "6. Difficulty rating: simple, moderate or hard, using the definitions from Prompt 1.\n"
                    "7. Generation attempts budgeted, with hero shots getting the largest allocation.\n"
                    "8. Whether audio needs to sync to this shot.\n\n"
                    "Then give me:\n"
                    "9. THE TOTALS: shot count, total runtime from the durations, total budgeted "
                    "generations, and whether all three match what Prompt 1 said was affordable.\n"
                    "10. THE DIFFICULTY DISTRIBUTION: how many shots in each band. If more than a third "
                    "are hard, tell me which to rewrite as moderate.\n"
                    "11. THE GENERATION ORDER: the order to actually generate in - hero shots first, then "
                    "hardest, then simple. Never script order.\n"
                    "12. THE CUT-FIRST LIST: the shots to abandon if budget runs out, ranked.\n\n"
                    "End by asking me whether any single shot is carrying too much of the film, so we can "
                    "build a fallback for it now."
                ),
                "pro_tip": (
                    "Item 11 matters more than it sounds. Generating in script order means discovering on "
                    "day six that the shot your ending needs is impossible - generate the hero shots on "
                    "day one while you still have the budget to rethink."
                ),
            },
            {
                "title": "The Scene Breakdown",
                "desc": (
                    "Scene by scene, how the shots assemble - what the audience understands, where the "
                    "geography holds, and what each scene needs to deliver."
                ),
                "prompt_text": (
                    "You are a director breaking a script into scenes for generative production.\n\n"
                    "My shot list: [PASTE FROM PROMPT 9]\n"
                    "My location geography and screen-direction rules: [PASTE FROM PROMPT 7]\n"
                    "My script: [PASTE]\n\n"
                    "For each scene, give me:\n\n"
                    "1. The scene's job in one sentence, and its screen time from the shot durations.\n"
                    "2. THE SHOT ORDER: the shots in cutting order, with the reason for that order.\n"
                    "3. THE GEOGRAPHY CHECK: confirm every shot in this scene agrees with the location's "
                    "geography and screen-direction rule. Flag any cut that would flip the space or leave "
                    "the audience disoriented.\n"
                    "4. THE ESTABLISH-AND-RETURN: whether this scene establishes its space clearly enough "
                    "before going closer, and where it returns wide to re-orient.\n"
                    "5. THE COVERAGE MINIMUM: the fewest shots that could carry this scene if I have to "
                    "economise, and what is lost.\n"
                    "6. THE HOLD: which shot in this scene should be held longest, and why. Generated "
                    "footage rewards a confident hold on a good clip over rapid cutting between weak ones.\n"
                    "7. THE WEAK LINK: the shot most likely to fail generation, and the alternative way to "
                    "cover the beat if it does.\n"
                    "8. THE ENTRY AND EXIT: how the scene starts and how it gets out - the first frame the "
                    "audience sees and the last one.\n\n"
                    "Then give me:\n"
                    "9. THE SCENE RHYTHM MAP: across the whole film, which scenes are fast and which are "
                    "slow, and whether the alternation works or whether I have four slow scenes together.\n"
                    "10. THE RUNTIME RECONCILIATION: total screen time against my target, and where the "
                    "difference is.\n\n"
                    "End by asking me which scene I am least confident about, because that is where to "
                    "spend a test generation before committing."
                ),
                "pro_tip": (
                    "Item 6 is the difference between a film and a showreel. One eight-second hold on a "
                    "clip that genuinely worked is worth six two-second cuts hiding clips that did not - "
                    "and audiences read the hold as confidence."
                ),
            },
            {
                "title": "The Keyframe Plan",
                "desc": (
                    "Most engines generate from a first frame. This prompt plans those frames as still "
                    "images you control, rather than letting the video model invent them."
                ),
                "prompt_text": (
                    "You are a technical director planning keyframes for generative video production.\n\n"
                    "My shot list: [PASTE FROM PROMPT 9]\n"
                    "My reference plates - characters, locations, props: [PASTE THE ASSET LIST FROM "
                    "PROMPTS 6-8]\n"
                    "My engine's capabilities: [STATE WHETHER IT ACCEPTS A START FRAME, AN END FRAME, BOTH, "
                    "OR NEITHER - CHECK, DO NOT GUESS]\n\n"
                    "Do the following:\n\n"
                    "1. THE METHOD DECISION: given my engine, state whether I should generate each clip "
                    "from a controlled still start frame, from text alone, or from start-and-end frames. "
                    "Explain the control and cost trade-off of each.\n"
                    "2. THE KEYFRAME LIST: for every shot that needs one, specify the still image to "
                    "generate first - its composition, which locked elements are in it, and the exact "
                    "moment of the action it represents.\n"
                    "3. THE CHAINING MAP: identify every place where one shot's last frame should seed the "
                    "next shot's first frame, so continuous action stays continuous. Mark these pairs "
                    "explicitly - this is the single most effective continuity technique available.\n"
                    "4. THE CHAIN BREAKS: where chaining is NOT appropriate - across a cut to a new angle, "
                    "a time jump, or a new scene - so I do not force continuity where the edit wants a "
                    "clean break.\n"
                    "5. THE FIRST-FRAME PROMPTS: for the 5 most important keyframes, write the actual "
                    "image-generation prompt, each containing the relevant canonical blocks, my look "
                    "block, and my negative block.\n"
                    "6. THE MOTION BRIEF PER KEYFRAME: for each keyframe, the one sentence describing what "
                    "moves and how, which will become the video prompt in Prompt 14.\n"
                    "7. THE CONTROL LADDER: rank my shots by how much control I need over composition. "
                    "High-control shots get generated keyframes; low-control shots can go text-to-video "
                    "and save money.\n"
                    "8. THE ASPECT AND RESOLUTION PLAN: what to generate at, accounting for any reframing "
                    "or cropping I will do in the edit, and whether to generate wider than my final frame "
                    "to leave room.\n\n"
                    "End by asking me whether I want to lock every composition myself or let the engine "
                    "surprise me on the simple shots, since that decision sets the whole production's pace."
                ),
                "pro_tip": (
                    "Item 3 is the technique that makes AI films feel continuous. Feeding the last frame "
                    "of a clip in as the first frame of the next costs nothing and does more for coherence "
                    "than any amount of prompt engineering."
                ),
            },
            {
                "title": "Transitions and Cut Points",
                "desc": (
                    "How clips become scenes. This prompt plans the joins, so the film reads as edited "
                    "rather than assembled."
                ),
                "prompt_text": (
                    "You are an editor planning cut points and transitions for a generative short film "
                    "before generation.\n\n"
                    "My scene breakdown: [PASTE FROM PROMPT 10]\n"
                    "My keyframe and chaining map: [PASTE FROM PROMPT 11]\n"
                    "My audio plan: [FROM PROMPT 4]\n\n"
                    "Do the following:\n\n"
                    "1. THE CUT INVENTORY: for every join in the film, specify the type - a straight cut, "
                    "a cut on action, a match cut, a sound-led cut, a dissolve, a cut to black. Justify "
                    "each. Default to straight cuts and make me argue for anything else.\n"
                    "2. THE GENERATION IMPLICATIONS: for each cut type, what it demands from the clips on "
                    "either side. A cut on action needs overlapping movement generated in both; a match cut "
                    "needs deliberate compositional similarity. Tell me what to build in.\n"
                    "3. THE HANDLE RULE: how much extra duration to generate at the head and tail of each "
                    "clip so I have something to cut with. State a figure, and note that generated clips "
                    "are often weakest at their start and end.\n"
                    "4. THE BEST-TWO-SECONDS PRINCIPLE: explain the practice of generating longer than "
                    "needed and cutting to the strongest portion, and mark which shots this matters most "
                    "for.\n"
                    "5. THE SOUND BRIDGE PLAN: where audio carries across a cut to bind two shots "
                    "together. This is the cheapest way to make disconnected clips feel like one scene - "
                    "mark every opportunity.\n"
                    "6. THE MOTION CONTINUITY CHECK: any two adjacent shots whose movement direction or "
                    "speed will clash. Flag and fix at the shot-list level.\n"
                    "7. THE FORBIDDEN TRANSITIONS: transitions that will make this film look amateur, "
                    "given its register. Name them and forbid them.\n"
                    "8. THE BLACK AND THE BREATH: where the film should cut to black or hold on stillness. "
                    "In a short this is punctuation, and it is free.\n\n"
                    "End by asking me whether I plan to edit this myself, because that determines how much "
                    "of this plan needs to survive contact with an editor."
                ),
                "pro_tip": (
                    "Item 5 is the technique that rescues AI shorts in the edit. Run a sound across a cut "
                    "- an ambience, a line, a note - and two clips generated hours apart become a single "
                    "continuous moment."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: GENERATE",
        "intro": (
            "Four prompts and you are producing footage. Reference images first, then clips, then the "
            "dialogue decision executed, then a disciplined regeneration strategy so the budget lands "
            "where the film needs it."
        ),
        "prompts": [
            {
                "title": "Reference Image Prompts",
                "desc": (
                    "The still-image generation layer - keyframes, plates and any composition you want to "
                    "control before it moves."
                ),
                "prompt_text": (
                    "You are a prompt engineer for image generation, producing the still layer of a "
                    "generative film.\n\n"
                    "My keyframe list and first-frame briefs: [PASTE FROM PROMPT 11]\n"
                    "My canonical blocks for characters, locations and props: [PASTE FROM PROMPT 5]\n"
                    "My look block and negative block: [PASTE FROM PROMPT 3]\n"
                    "My image engine: [NAME IT]\n\n"
                    "Do the following:\n\n"
                    "1. THE PROMPT TEMPLATE: build the reusable structure every image prompt in this film "
                    "will follow - subject and canonical block, action or pose, framing and shot size, "
                    "lens and depth, light source and direction, environment, look block, negative block. "
                    "Give me the template with the slots marked.\n"
                    "2. THE FULL SET: write the actual image prompt for every keyframe on my list, using "
                    "the template. Each must include the relevant canonical blocks verbatim.\n"
                    "3. THE REFERENCE-IMAGE INSTRUCTION: for each prompt, state which of my approved "
                    "plates should be supplied as a reference alongside the text, and how my engine expects "
                    "them.\n"
                    "4. THE ORDER: which images to generate first so I learn fastest - one test of the "
                    "hardest composition before committing to the batch.\n"
                    "5. THE SELECTION CRITERIA: what to accept and reject. Be specific - identity match "
                    "against the plate, composition, light direction consistency, hands, background "
                    "coherence, artifacts, anything the engine invented that is not in my blocks.\n"
                    "6. THE CONSISTENCY SPOT-CHECK: after every batch, the specific comparison to run "
                    "against the plates to catch drift before it propagates.\n"
                    "7. THE LOGGING: exactly what to record per approved image - prompt used, references "
                    "supplied, seed or ID, shot number it serves.\n"
                    "8. THE FIX-IN-POST LIST: problems not worth regenerating for, because they are "
                    "cheaper to correct in an image editor - a colour cast, a small artifact, a crop, "
                    "removing something the engine added.\n\n"
                    "End by asking me to generate the hardest keyframe first and report back, so we "
                    "calibrate the prompts before spending the batch."
                ),
                "pro_tip": (
                    "Item 8 saves real money. A one-pixel artifact or a stray object is thirty seconds of "
                    "retouching and often four failed regenerations - fix the frame rather than rolling "
                    "the dice again."
                ),
            },
            {
                "title": "Video Prompts, Per Engine",
                "desc": (
                    "Turning keyframes and shot briefs into clip prompts, written to each engine's "
                    "grammar, with the motion described the way models actually respond to."
                ),
                "prompt_text": (
                    "You are a prompt engineer for generative video who writes for multiple engines and "
                    "knows they do not share a grammar.\n\n"
                    "My shot list with durations and motion briefs: [PASTE FROM PROMPTS 9 AND 11]\n"
                    "My approved keyframes: [LIST THEM]\n"
                    "My look block, camera vocabulary and movement rule: [PASTE FROM PROMPT 3]\n"
                    "My video engine or engines: [NAME THEM, AND STATE CURRENT CLIP LENGTH LIMITS AND "
                    "WHETHER EACH TAKES A START FRAME, END FRAME, OR TEXT ONLY]\n\n"
                    "Do the following:\n\n"
                    "1. THE ENGINE BRIEF: for each engine I named, summarise how it wants to be prompted - "
                    "how literal or descriptive, how it handles camera instructions, how it handles "
                    "duration, whether it responds to shot-size language. Flag anything I should verify "
                    "myself, since engine behaviour changes frequently.\n"
                    "2. THE ASSIGNMENT: which shots go to which engine and why, based on what each does "
                    "well - one may handle human motion better, another camera movement, another "
                    "stylisation.\n"
                    "3. THE PROMPT TEMPLATE PER ENGINE: the reusable structure for each, with slots for "
                    "subject, action, camera, duration, look block and negatives.\n"
                    "4. THE FULL SET: write the actual video prompt for every shot on my list, in the "
                    "grammar of its assigned engine, with its keyframe referenced where applicable.\n"
                    "5. THE MOTION LANGUAGE: rewrite my motion briefs into the phrasing these models "
                    "respond to - single continuous actions, explicit start and end states, speed stated "
                    "plainly. Flag any brief that asks for two actions and split it.\n"
                    "6. THE CAMERA INSTRUCTION RULES: how to specify camera behaviour so it is obeyed, and "
                    "which moves to simply avoid asking for.\n"
                    "7. THE DURATION STRATEGY: how long to generate each clip relative to its cut length, "
                    "applying the handle rule from Prompt 12.\n"
                    "8. THE SELECTION CRITERIA: what makes a clip usable - identity holding for its full "
                    "duration, no morphing, coherent physics, the action actually completing, no artifacts "
                    "in the portion I need. Note that a clip can be unusable overall and perfect for two "
                    "seconds.\n"
                    "9. THE LOGGING: what to record per clip so a good result is reproducible.\n\n"
                    "End by asking me to run one hero shot on two different engines and compare, before "
                    "committing the whole film to either."
                ),
                "pro_tip": (
                    "Item 8's last sentence is the working truth of this craft. Judge every clip on its "
                    "best two seconds rather than its whole duration - most 'failed' generations contain "
                    "exactly the shot you needed."
                ),
            },
            {
                "title": "Dialogue and Lip-Sync",
                "desc": (
                    "The hardest thing in AI filmmaking, executed according to the decision made in Prompt "
                    "2 - and with the off-ramps clearly marked."
                ),
                "prompt_text": (
                    "You are a post-production supervisor handling voice and lip-sync for a generative "
                    "film. You are honest about how hard this is.\n\n"
                    "My dialogue decision: [PASTE FROM PROMPT 2 ITEM 5]\n"
                    "My audio plan and dialogue production path: [PASTE FROM PROMPT 4]\n"
                    "My script's dialogue: [PASTE]\n"
                    "My shots requiring sync: [FROM PROMPT 9]\n\n"
                    "Do the following:\n\n"
                    "1. THE PATH CONFIRMATION: restate my chosen approach - no dialogue, off-screen or "
                    "voiceover, or on-screen lip-synced - and tell me plainly what each line of my script "
                    "will cost under it.\n"
                    "2. THE OFF-RAMP AUDIT: go through my dialogue line by line and mark which lines could "
                    "be delivered off-screen, over a reaction shot, over a cutaway, or cut entirely. Every "
                    "line moved off-screen is a lip-sync problem eliminated - be aggressive here.\n"
                    "3. THE VOICE BRIEF: for each speaking character, a casting brief - age, texture, "
                    "pace, accent, emotional register - usable for a human performer or a voice generator.\n"
                    "4. THE PERFORMANCE DIRECTION: for each line staying in the film, the direction that "
                    "gets it delivered right. Voice generators need this stated explicitly rather than "
                    "implied.\n"
                    "5. THE SYNC METHOD: if any lines are on-screen and synced, specify the workflow - "
                    "generate the clip then sync the audio to it, or drive the clip from the audio. State "
                    "the order of operations and where it breaks.\n"
                    "6. THE SYNC-SHOT DESIGN RULES: how to frame and stage a synced shot to maximise "
                    "success - shot size, whether the mouth is fully visible, head movement, duration, how "
                    "many words per clip. Give me hard rules.\n"
                    "7. THE FALLBACK LADDER: for every synced line, the retreat if sync fails - reframe "
                    "wider, cut to a listener, move the line off-screen, replace with an action. Have this "
                    "ready before generation, not after.\n"
                    "8. THE AUDIO QUALITY BASELINE: the standard the voice track must hit, and why "
                    "audiences forgive strange pictures and never forgive bad audio.\n"
                    "9. THE MIX NOTE: how dialogue sits against the ambience and score from Prompt 4.\n\n"
                    "End by asking me how many lines survived item 2, because that number is the real "
                    "difficulty of this production."
                ),
                "pro_tip": (
                    "Item 2 is the highest-leverage pass in the entire pack. Most short films lose nothing "
                    "by moving two thirds of their dialogue off-screen, and every line you move removes a "
                    "failure mode that would have cost you a day."
                ),
            },
            {
                "title": "The Regeneration Strategy",
                "desc": (
                    "How to spend attempts. This prompt sets a fix-it budget and a stopping rule, so you "
                    "do not burn the film's resources on shot three."
                ),
                "prompt_text": (
                    "You are a producer managing generation spend on an AI film in progress. You enforce "
                    "stopping rules.\n\n"
                    "My shot list with attempt budgets: [PASTE FROM PROMPT 9]\n"
                    "My total generation budget and hero shots: [PASTE FROM PROMPT 1]\n"
                    "What I have generated so far and what failed: [DESCRIBE]\n\n"
                    "Do the following:\n\n"
                    "1. THE DIAGNOSIS PROTOCOL: when a clip fails, the order to check things in - is the "
                    "prompt asking for two actions, is the keyframe wrong, is the duration too long, is "
                    "the subject description contradicting the reference, is this simply in a known failure "
                    "zone. Give me the checklist.\n"
                    "2. THE FIX HIERARCHY: the order to try fixes in, cheapest first - reword the action, "
                    "shorten the duration, change the keyframe, simplify the composition, change the shot "
                    "size, change engine, redesign the shot, cut the shot. Explain when to jump straight "
                    "to the end of this list.\n"
                    "3. THE STOPPING RULE: after how many failed attempts on a single shot I should stop "
                    "and redesign rather than retry. Give me a number and hold me to it.\n"
                    "4. THE THREE-STRIKE REDESIGN: for a shot that has failed repeatedly, how to redesign "
                    "the beat so it becomes generatable - the reaction instead of the action, the aftermath "
                    "instead of the event, sound instead of sight, a tighter frame, a static camera.\n"
                    "5. THE BUDGET REALLOCATION: given what I have spent, how to redistribute remaining "
                    "attempts. Protect the hero shots; ration everything else.\n"
                    "6. THE GOOD-ENOUGH TEST: how to judge whether a clip is acceptable in context rather "
                    "than in isolation. A shot that looks weak alone can be fine at 1.5 seconds inside a "
                    "cut sequence - give me the test.\n"
                    "7. THE SALVAGE PASS: for clips I have already rejected, how to review them for "
                    "usable fragments, reframes, slow-downs, freeze frames, or reversal.\n"
                    "8. THE ESCALATION POINT: the signal that means this film needs rescoping rather than "
                    "more attempts, and what to do at that point.\n\n"
                    "End by asking me which shot I have spent the most on so far, because that is usually "
                    "the shot that needs redesigning rather than retrying."
                ),
                "pro_tip": (
                    "Enforce item 3 literally. Writers and directors both fall into the sunk-cost loop of "
                    "one more attempt; a hard number - three, or five - turns a spiral into a decision and "
                    "usually produces a better shot than the one you were chasing."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 5: AUDIO AND ASSEMBLY",
        "intro": (
            "Three prompts to build the layers the video generator never produced, then cut the film. "
            "Audio is where AI shorts are won - it is the one layer that is not generated, so it can be "
            "genuinely excellent."
        ),
        "prompts": [
            {
                "title": "Score and Sound Design",
                "desc": (
                    "Building the sound world as its own production, from the plan you made in Prompt 4 "
                    "before any picture existed."
                ),
                "prompt_text": (
                    "You are a composer and sound designer building the audio for a finished-picture "
                    "generative short.\n\n"
                    "My audio plan, layer map and score brief: [PASTE FROM PROMPT 4]\n"
                    "My scene breakdown and runtime: [PASTE FROM PROMPT 10]\n"
                    "My look and tone: [FROM PROMPT 3]\n"
                    "My music tool or composer situation: [DESCRIBE]\n\n"
                    "Do the following:\n\n"
                    "1. THE CUE SHEET: every music cue in the film - where it starts, where it ends, its "
                    "length, and what it is doing dramatically. Include every deliberate absence of music.\n"
                    "2. THE CUE BRIEFS: for each cue, a generation or composition brief - "
                    "instrumentation, tempo, key feeling, whether it builds or holds, and what it must not "
                    "do. Written so it can be handed to a music generator or a composer.\n"
                    "3. THE THEME QUESTION: whether this film needs a recurring musical idea, and if so "
                    "what it is attached to - a character, a place, a memory.\n"
                    "4. THE AMBIENCE BEDS: for each location, the layered bed to build, listed as "
                    "separate elements so I can mix rather than dropping in one stock loop.\n"
                    "5. THE SPOT EFFECTS LIST: every specific sound the film needs, scene by scene, with "
                    "how to source or generate each.\n"
                    "6. THE SOUND-DOES-THE-WORK MOMENTS: the moments identified in Prompt 4 item 7 - now "
                    "specify exactly what is heard, at what level, and what the audience is looking at "
                    "while they hear it.\n"
                    "7. THE SILENCE CUES: where everything drops out. Give me the exact in and out points "
                    "relative to the picture.\n"
                    "8. THE SWEETENING PASS: 6 places where a small added sound will make generated "
                    "picture feel physically real - a footstep, cloth, a breath, a distant vehicle, an "
                    "electrical hum, a door. This is the cheapest credibility in AI filmmaking.\n"
                    "9. THE MIX ORDER: the order to build the mix in, and the relative levels of dialogue, "
                    "score, ambience and effects.\n\n"
                    "End by asking me whether the film works with the picture off, because a film that "
                    "works as audio alone will survive weak clips."
                ),
                "pro_tip": (
                    "Item 8 is the single highest-value trick in this pack. Generated footage reads as "
                    "unreal partly because it is silent - add footsteps, cloth movement and breath and the "
                    "same clip becomes physical."
                ),
            },
            {
                "title": "Voice and Dialogue Production",
                "desc": (
                    "Producing the actual voice track to the standard the film needs - the layer audiences "
                    "judge most harshly and forgive least."
                ),
                "prompt_text": (
                    "You are a dialogue editor and voice producer finishing the voice track for a "
                    "generative short film.\n\n"
                    "My dialogue path and surviving lines: [PASTE FROM PROMPT 15]\n"
                    "My voice briefs and performance directions: [PASTE FROM PROMPT 15 ITEMS 3-4]\n"
                    "My voice source: [HUMAN PERFORMER, VOICE GENERATOR, OR BOTH]\n\n"
                    "Do the following:\n\n"
                    "1. THE RECORD LIST: every line to produce, with its character, its performance "
                    "direction, and the shot it plays over.\n"
                    "2. IF USING A HUMAN: how to get a clean recording without a studio - the room, the "
                    "mic position, what to put on the walls, what to turn off, how many takes, and how to "
                    "direct a performer who cannot see the picture yet.\n"
                    "3. IF USING A GENERATOR: how to structure the input for the best result - punctuation "
                    "and pacing, how to get emphasis, how to handle names and unusual words, how many "
                    "attempts per line, and what to do about lines that will not land.\n"
                    "4. THE ALTERNATES: which lines to produce in two or three different readings, because "
                    "the edit will want options.\n"
                    "5. THE CLEANUP CHAIN: the processing order for the voice track - noise reduction, "
                    "de-essing, EQ, compression, level - with a caution about over-processing.\n"
                    "6. THE ROOM MATCH: how to make a clean voice recording sit inside a generated "
                    "environment - matching reverb and space so the voice does not float above the "
                    "picture. This is what separates finished from unfinished.\n"
                    "7. THE SYNC CHECK: for any on-screen synced lines, the checking pass and the "
                    "tolerance. Note that being slightly early reads better than slightly late.\n"
                    "8. THE BREATH AND PAUSE PASS: where to keep breaths and add pauses, since generated "
                    "and synthesised voice both tend to be unnaturally smooth.\n"
                    "9. THE FALLBACK EXECUTION: if a line still does not work, execute the fallback ladder "
                    "from Prompt 15 item 7 and tell me what changes in the picture as a result.\n\n"
                    "End by asking me which line is doing the most dramatic work in the film, so we spend "
                    "the takes there."
                ),
                "pro_tip": (
                    "Item 6 is what most AI shorts miss. A pristine voice over a generated room sounds "
                    "like narration pasted on top; add a small matching reverb and the same take suddenly "
                    "belongs inside the frame."
                ),
            },
            {
                "title": "Assembly and Pacing",
                "desc": (
                    "Cutting the film - which includes cutting around every weakness the generation left "
                    "you, and finding the real runtime."
                ),
                "prompt_text": (
                    "You are a film editor assembling a generative short from approved clips. You cut "
                    "around weakness rather than hiding it.\n\n"
                    "My scene breakdown and shot order: [PASTE FROM PROMPT 10]\n"
                    "My cut plan and sound bridges: [PASTE FROM PROMPT 12]\n"
                    "My audio elements: [FROM PROMPTS 17-18]\n"
                    "What I actually ended up with - including what failed or is weak: [DESCRIBE]\n\n"
                    "Do the following:\n\n"
                    "1. THE ASSEMBLY ORDER: the order to build the edit in, and why it is not the film's "
                    "running order. Start where the material is strongest.\n"
                    "2. THE BEST-SECONDS PASS: for each clip, instruct me to identify its strongest "
                    "continuous portion and cut to that. Give me the criteria for choosing.\n"
                    "3. THE WEAKNESS MAP: given what I have described as weak, tell me for each one which "
                    "technique applies - shorten it, hold on something else and use it as sound only, "
                    "reframe or crop in, slow it down, freeze the last good frame, cover it with a "
                    "reaction, or cut it entirely.\n"
                    "4. THE PACING AUDIT: where the assembly will drag and where it will feel rushed, and "
                    "the fix for each. Note that AI shorts almost always run long in the first assembly.\n"
                    "5. THE RUNTIME RECONCILIATION: my actual runtime against target, and the specific "
                    "cuts to close the gap, ranked least to most painful.\n"
                    "6. THE HOLD DECISIONS: which shots to hold longer than instinct suggests, because "
                    "they earned it, and which to cut short.\n"
                    "7. THE SOUND-FIRST PASS: how to lay audio early in the assembly rather than at the "
                    "end, since in this workflow sound determines pacing more than picture does.\n"
                    "8. THE GRADE AND MATCH PASS: how to bring clips generated at different times into "
                    "one consistent look - matching exposure, contrast and colour, and adding a unifying "
                    "grain or grade over everything. A single consistent treatment across the whole film "
                    "hides an enormous amount of generation variance.\n"
                    "9. THE FRESH-EYES PROTOCOL: what to ask two people who have not seen it, and the "
                    "three questions that produce useful answers rather than politeness.\n\n"
                    "End by asking me what the film is now actually about, since edits change that and it "
                    "will affect the titles and the release materials."
                ),
                "pro_tip": (
                    "Item 8 is the great equaliser. One grain structure and one grade laid across every "
                    "shot makes forty clips generated over three weeks read as one photographic world - "
                    "it is the closest thing to a magic button in this workflow."
                ),
            },
        ],
    },

    {
        "name": "PHASE 6: FINISH AND RELEASE",
        "intro": (
            "Three prompts to deliver. A QC pass that catches what you have stopped being able to see, "
            "titles and deliverables done properly, and an honest plan for where this film goes."
        ),
        "prompts": [
            {
                "title": "The QC Audit",
                "desc": (
                    "The pass that catches continuity drift, artifacts and audio problems you have gone "
                    "blind to after weeks inside the project."
                ),
                "prompt_text": (
                    "You are a quality control supervisor reviewing a finished generative short film "
                    "before release. You are looking for what the filmmaker can no longer see.\n\n"
                    "My continuity bible and canonical blocks: [PASTE FROM PROMPT 5]\n"
                    "My shot list: [FROM PROMPT 9]\n"
                    "My film: [DESCRIBE IT SHOT BY SHOT, OR PASTE YOUR EDIT LIST AND CONTINUITY LOG]\n\n"
                    "Audit for the following, citing the shot or timecode for each:\n\n"
                    "1. IDENTITY DRIFT: every shot where a character does not match their reference plate "
                    "- face, age, build, hair, costume. Rank by how noticeable each is in context.\n"
                    "2. SPACE DRIFT: every shot where a location contradicts its established geography, "
                    "and every cut that flips screen direction.\n"
                    "3. PROP AND COSTUME CONTINUITY: objects that change, appear, vanish, or fail their "
                    "state progression.\n"
                    "4. ARTIFACT SWEEP: the specific generative artifacts to look for - hands, extra or "
                    "missing limbs, morphing between frames, background instability, physics that does not "
                    "hold, text that resolved into nonsense, faces in the background.\n"
                    "5. THE LOOK CONSISTENCY: shots that do not match the grade, exposure, grain or colour "
                    "of their neighbours.\n"
                    "6. AUDIO QC: levels across the film, dialogue intelligibility, ambience continuity "
                    "across cuts, anything that drops out unintentionally, and whether the mix holds on "
                    "both headphones and a phone speaker.\n"
                    "7. THE PACING PASS: where a viewer's attention will drift, with a timecode.\n"
                    "8. THE COMPREHENSION CHECK: 6 questions a first-time viewer would have. Any question "
                    "the film does not intend to leave open is a problem - flag it.\n"
                    "9. THE TRIAGE: split every finding into must-fix, should-fix-if-cheap, and "
                    "accept-and-move-on. Be realistic - a generative film with zero artifacts does not "
                    "exist, and chasing them all is how films never ship.\n\n"
                    "End by asking me what my remaining budget and time actually are, so the triage is "
                    "honest rather than aspirational."
                ),
                "pro_tip": (
                    "Item 9 is the one that gets films finished. Perfection is not available in this "
                    "medium; a clear-eyed list of what a viewer will actually notice, fixed in order, is."
                ),
            },
            {
                "title": "Titles, Credits and Deliverables",
                "desc": (
                    "The finishing layer - and the place to put every piece of text the video generator "
                    "could never have rendered correctly."
                ),
                "prompt_text": (
                    "You are a post-production supervisor preparing deliverables for a short film's "
                    "release.\n\n"
                    "My film, its look and its tone: [PASTE FROM PROMPT 3 AND DESCRIBE THE FINISHED FILM]\n"
                    "My text problem list: [PASTE FROM PROMPT 8 ITEM 6]\n"
                    "Where this film is going: [FESTIVALS, ONLINE, A PITCH, OR UNDECIDED]\n\n"
                    "Do the following:\n\n"
                    "1. THE TITLE DESIGN BRIEF: where the title appears, how long it holds, typeface "
                    "character, whether it is over picture or black, and how it relates to my look. Keep it "
                    "simple - over-designed titles are the most common tell of an inexperienced short.\n"
                    "2. THE IN-FILM TEXT: every item from my text problem list, now executed as a post "
                    "graphic - a sign, a note, a phone screen, a location card. Specify each, and remind me "
                    "this is where that text always belonged.\n"
                    "3. THE CREDITS: what a short film's credits must contain, in what order, and how long "
                    "they should run. Include how to credit AI tools honestly and how to credit human "
                    "collaborators properly.\n"
                    "4. THE AI DISCLOSURE: how to describe the film's use of generative tools in credits "
                    "and submission materials - clear and unembarrassed, without either hiding it or "
                    "making it the whole identity of the work. Note that many festivals now require "
                    "disclosure, so check each one's rules rather than assuming.\n"
                    "5. THE DELIVERABLE LIST: what to export and at what specification - master, festival "
                    "screener, online version, vertical or square cut-down if wanted, stills, and a "
                    "captions or subtitle file.\n"
                    "6. THE STILLS PASS: which frames to pull as promotional stills. Generated films have "
                    "an advantage here - choose frames that are flawless at full resolution.\n"
                    "7. THE SUBTITLE FILE: why to make one even for an English-language film, and the "
                    "format to deliver it in.\n"
                    "8. THE ARCHIVE: what to keep - prompts, seeds, reference plates, the continuity log, "
                    "project files, source clips including rejects. Specify a folder structure, because a "
                    "sequel or a recut in six months will need all of it.\n\n"
                    "End by asking me whether I want a vertical cut-down of this film, because that "
                    "decision changes what I export now rather than re-doing it later."
                ),
                "pro_tip": (
                    "Item 8 is not admin, it is insurance. The prompt, seed and plate that produced your "
                    "best shot is the only way to ever make a matching shot again - lose the log and the "
                    "world of that film is gone."
                ),
            },
            {
                "title": "Release and Platform Strategy",
                "desc": (
                    "Where this film goes and what it is for - including the specific considerations that "
                    "apply to AI-generated work right now."
                ),
                "prompt_text": (
                    "You are a distribution strategist for short films with specific knowledge of how "
                    "AI-generated work is currently received. You are realistic rather than encouraging.\n\n"
                    "My film, runtime and register: [DESCRIBE]\n"
                    "What I want it to do for me: [STATE IT]\n"
                    "My deliverables: [FROM PROMPT 21]\n\n"
                    "Do the following:\n\n"
                    "1. THE HONEST ASSESSMENT: what this film can realistically achieve. Include a "
                    "straight answer about how AI-generated shorts are currently received by festivals, "
                    "audiences and industry - the doors that are open, the ones that are not, and the ones "
                    "where disclosure changes the answer.\n"
                    "2. THE ROUTE DECISION: recommend a primary route - festival submission, direct online "
                    "release, a platform-native release, or a private pitch tool - and justify it against "
                    "what I said I want.\n"
                    "3. THE FESTIVAL PATH: if submitting, how to think about which festivals accept or "
                    "welcome AI work, why to read each one's eligibility rules rather than assuming, what "
                    "premiere status protects, and how to sequence submissions. Explain the principles "
                    "rather than naming festivals, since both the festivals and their AI policies change.\n"
                    "4. THE ONLINE PATH: if releasing online, platform choice against my film's length and "
                    "register, thumbnail and title strategy, the first-five-seconds problem, and how to "
                    "describe the film honestly in the copy.\n"
                    "5. THE VERTICAL CUT-DOWN: whether this film has a short-form vertical version in it - "
                    "which 30-60 seconds, recut for a phone, with what changes to framing, pacing and "
                    "sound. This is often where an AI short finds its actual audience.\n"
                    "6. THE CREDIBILITY PACKAGE: for industry use, what to show alongside the film - the "
                    "continuity bible, the shot list, the reference plates, the process breakdown. For AI "
                    "work the process is often more persuasive than the result, because it demonstrates "
                    "you can direct rather than prompt.\n"
                    "7. THE CRITICISM PREPARATION: the objections this film will attract, and an honest, "
                    "non-defensive answer to each. Decide these now rather than in a comment thread.\n"
                    "8. THE NEXT FILM: based on what this one taught me, what my next one should do "
                    "differently - technically and dramatically.\n"
                    "9. THE PORTFOLIO QUESTION: whether this film belongs in front of people at all, or "
                    "whether it is a training run. Answer honestly; a first generative short is often "
                    "worth more as education than as a calling card.\n\n"
                    "End by asking me what I learned making this that I did not know at Prompt 1, because "
                    "that answer is the real output of the project."
                ),
                "pro_tip": (
                    "Item 6 is the counter-intuitive one. Producers looking at AI work are assessing "
                    "whether you made decisions or accepted outputs - showing the continuity bible and the "
                    "shot list proves direction in a way the finished film alone cannot."
                ),
            },
        ],
    },
]
