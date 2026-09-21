# -*- coding: utf-8 -*-
"""
Royalti Studios - Short Film Screenplay Master Prompt Pack (Screenwriting Line).

Build with:
    python pack_builder.py short_film_screenplay_pack_data \
        "Short_Film_Screenplay_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.

PROMPT COUNT: 18, below the 22 baseline. Approved by the user on 2026-09-21.
Reasons: a short film has no subplot architecture, no series runway, no
multi-batch drafting, and no retail/metadata phase. Two provisional 4-prompt
add-on modules are recorded in _generator/addon_modules.md for genre-specific
follow-ups.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "SHORT FILM SCREENPLAY",
    "total_prompts": 18,
    "hook_line": "A short film is not a small movie. It is one moment, built backwards from its last image, written to be shot with what you can actually get.",
    "keyword_lines": [
        "One idea • One turn • One location • The last image first",
        "Format discipline • Silent storytelling • Page-to-screen time • Festival cut",
    ],
    "subgenres_line": "Formats: Festival Short (7-15 min), Micro-Short (under 3 min), Proof-of-Concept for a Feature, Single-Location Piece, Dialogue Two-Hander, Silent/Visual Short, Genre Calling-Card, Anthology Segment",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-21",
    "audience_line": "Screenwriting Line",
    "cover_h2": "From One Idea to a Shootable Script",
    "works_with_line": "Works with ChatGPT • Claude • Gemini • Copilot • Any LLM",
    "closing_tagline": "Find the one moment. Build backwards from the last image. Cut everything that is not load-bearing.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "Most bad short films are features with the middle removed. This pack builds the other kind: a "
        "piece designed at short length, about one thing, ending on an image that reframes everything "
        "before it. It works in the order the form actually demands - find the single idea, lock the "
        "constraints you can really afford, write the ending first, then work backwards into the "
        "situation. It also takes production seriously, because a short script that cannot be shot is a "
        "writing exercise. Work the prompts in order and keep every output in one document. By Prompt 18 "
        "you have a formatted, shootable script plus the package to send it out with."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-3) - Find the one thing. Isolate the single idea, lock runtime and the "
        "constraints you can genuinely afford, and write the ending before anything else.",
        "Phase 2 (Prompts 4-6) - Build the situation. A character established through behaviour rather "
        "than backstory, a location that earns its place, and the want-obstacle-clock that makes the piece "
        "move.",
        "Phase 3 (Prompts 7-9) - Structure it. Choose the short-film shape that fits (shorts rarely use "
        "three acts), map it scene by scene against page count, and design the one turn the whole film "
        "exists to deliver.",
        "Phase 4 (Prompts 10-12) - Write the script. Format discipline and a first page that sets the "
        "contract, a full draft in one pass, and a dialogue pass that cuts everything the picture already "
        "says.",
        "Phase 5 (Prompts 13-15) - Make it shootable. A production reality audit against your actual "
        "resources, a runtime and table-read audit, and a visual pass that moves story onto the screen "
        "and off the page.",
        "Phase 6 (Prompts 16-18) - Send it out. The rewrite audit against this form's specific failure "
        "modes, the logline and pitch package, and a plan for what this short is actually for.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool and a place to save your outputs between prompts. Brackets like "
        "[THIS] are placeholders - replace them with your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular. Writing a silent piece? Prompt 12 becomes a "
        "sound-and-image pass. Writing a proof-of-concept for a feature? Prompt 18 is the most important "
        "prompt in the pack. Not directing it yourself? Prompt 15 becomes notes for whoever will."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "One idea, one turn - a short film is a single moment examined, not a plot summarised",
            "An ending you designed first, so every earlier choice is pointed at it",
            "Character revealed through behaviour under pressure; there is no room for backstory and no need for it",
            "Constraints chosen deliberately - locations, cast and days you can actually get - so the script is makeable",
            "A clock: something that must happen or be prevented inside the runtime",
            "Story carried by image wherever possible, with dialogue doing only what the picture cannot",
            "A first page that establishes tone, world and contract inside 60 seconds of screen time",
            "Silence used on purpose - the pauses are the form's most powerful tool and cost nothing",
            "A last image that reframes what came before, rather than a last line that explains it",
            "Length honesty: a 9-minute film that is 9 minutes of film, not 14 minutes hoping to be trimmed",
        ],
        "kills": [
            "A feature premise compressed - three acts, a subplot and a montage crammed into 12 pages",
            "A twist ending that reframes nothing and rewards no rewatch, just withholds information",
            "Backstory delivered in dialogue because there was no room to dramatise it",
            "Voiceover explaining what the audience could have inferred from a look",
            "Characters who announce their own themes in the last scene",
            "Locations, crowds, vehicles, children, animals or weather the production cannot afford",
            "A script that is 22 pages and described as a short - that is a runtime problem, not a style",
            "Dialogue written to be read rather than spoken; unspeakable lines survive in short scripts because nobody table-reads them",
            "A dream, a hallucination or 'it was all a game' used to excuse a situation that did not cohere",
            "An ending that stops rather than ends, on the assumption that ambiguity reads as depth",
        ],
        "voice": [
            "Present tense, active, lean - screen direction describes what a camera can record, nothing else",
            "No unfilmables: what a character thinks, remembers or used to be cannot appear in an action line",
            "White space is pacing; short blocks of action read fast and shoot fast",
            "One idea per action paragraph, and rarely more than four lines",
            "Dialogue in speech rhythm - contractions, interruptions, incomplete sentences",
            "Character names introduced in caps once, with an age and one defining behaviour, never a biography",
            "Sound cues written sparingly and deliberately, because in a short they land hard",
            "Scene headings kept simple and consistent; a short script should never confuse a reader about where they are",
        ],
        "formula": (
            "THE LAST IMAGE (designed first) -> The Opening Image that it will answer -> The Situation "
            "Established in Behaviour (who, where, what is wrong - inside a minute) -> The Want Declared or "
            "Revealed -> The Obstacle and the Clock -> The Attempt -> The Complication (the situation is "
            "worse or stranger than it looked) -> THE TURN (the one reversal the film exists for) -> The "
            "Consequence, Played Out in Action -> The Last Image, Reframing Everything"
        ),
        "reader_expectations": (
            "Your readers are a festival programmer with 400 submissions, a producer deciding whether you "
            "can handle a feature, and an actor deciding whether the part is worth two unpaid days. All "
            "three read the first page and make a provisional judgement, and all three are asking the same "
            "question: does this person know what a short film is for? They want one idea executed "
            "precisely, a script whose page count matches its claimed runtime, and dialogue an actor wants "
            "to say. They will forgive a small idea and never forgive a padded one. A producer is also "
            "reading for makeability - locations, cast size, night exteriors, anything expensive - and a "
            "script that ignores that reads as inexperience regardless of how good the writing is."
        ),
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "The discipline of the short film is subtraction. You designed the ending in Prompt 3, and "
        "everything after that has been a process of removing whatever does not point at it. That is why "
        "the form is such good training and such an unforgiving calling card - there is nowhere to hide a "
        "scene that is merely nice. When the script feels flat, do not add. Ask what the last image needs "
        "the audience to understand, and cut the scenes that were teaching them something else. Then read "
        "it out loud with a stopwatch. The page count will lie to you; the clock will not."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: FIND THE ONE THING",
        "intro": (
            "Three prompts that decide whether this will be a short film or a squashed feature. Isolate "
            "one idea, lock the constraints you can actually afford, and write the ending before you write "
            "anything else - because in this form everything is built backwards from the last image."
        ),
        "prompts": [
            {
                "title": "The Single Idea",
                "desc": (
                    "Short films are about one thing. This prompt strips your concept to that one thing and "
                    "tells you plainly whether what you have is a short, a feature, or a scene."
                ),
                "prompt_text": (
                    "You are a short film development executive who has programmed a festival and read "
                    "several thousand short scripts. You are direct about what is not a short film.\n\n"
                    "My idea is: [DESCRIBE IN 2-5 SENTENCES]\n\n"
                    "Do the following:\n\n"
                    "1. THE DIAGNOSIS: tell me plainly whether this is a short film, a feature premise, a "
                    "single scene, or a TV pilot. Explain in 3-4 sentences. If it is not a short, tell me "
                    "what the short film inside it would be.\n"
                    "2. THE ONE THING: state in a single sentence of 20 words or fewer what this film is "
                    "about. Not the plot - the one thing it examines.\n"
                    "3. THE MOMENT: short films work best on one moment in a life where something shifts. "
                    "Identify that moment in my idea. If my idea currently spans weeks or years, name the "
                    "single hour it should actually cover.\n"
                    "4. WHAT TO CUT: list everything in my idea that belongs to a longer form - the "
                    "subplot, the second location, the backstory, the third character, the time jump. Be "
                    "ruthless and specific.\n"
                    "5. THE FIVE ALTERNATIVES: give me 5 sharper one-sentence versions of this idea, each "
                    "with a different angle of attack, and say what kind of film each would be.\n"
                    "6. THE FORMAT: recommend one from - festival short (7-15 min), micro-short (under 3 "
                    "min), proof-of-concept for a feature, single-location piece, dialogue two-hander, "
                    "silent/visual short, genre calling-card, anthology segment. Justify it.\n"
                    "7. THE COMPARISON SET: describe 4 types of short film that occupy similar ground "
                    "(describe the kind of film, do not just name titles) and say what each does that I "
                    "will be measured against.\n\n"
                    "End by asking me what I am making this short FOR - a festival run, a feature pitch, a "
                    "directing reel, a cast showcase - because the answer changes every choice after this."
                ),
                "pro_tip": (
                    "Take item 1 seriously even when it stings. Half of all short scripts are features "
                    "with the middle deleted, and the fastest route to a good short is admitting yours is "
                    "one of them and finding the single hour inside it."
                ),
            },
            {
                "title": "Runtime, Format and the Constraint Lock",
                "desc": (
                    "A short script that cannot be shot is a writing exercise. This prompt locks runtime, "
                    "page count, and the real production limits you will write inside."
                ),
                "prompt_text": (
                    "You are a line producer for independent short films who has budgeted hundreds of "
                    "them, advising a writer before they draft.\n\n"
                    "My one thing and format: [PASTE FROM PROMPT 1]\n"
                    "What I actually have access to: [BE HONEST - MONEY, DAYS, CREW, CAST, LOCATIONS, "
                    "EQUIPMENT, OR SAY 'ALMOST NOTHING']\n\n"
                    "Lock my constraints:\n\n"
                    "1. THE RUNTIME TARGET: recommend a target runtime and the page count that "
                    "corresponds. State the page-to-minute rule you are using and the specific ways it "
                    "lies - dialogue-heavy pages run faster, action and silence run far slower.\n"
                    "2. THE HARD PAGE CEILING: the number of pages I may not exceed, and what to do when I "
                    "hit it.\n"
                    "3. THE SHOOTING MATH: given my resources, how many shooting days this supports, how "
                    "many pages per day is realistic for my situation, and therefore how long the script "
                    "can actually be. If my resources do not support my runtime, say so now.\n"
                    "4. THE CONSTRAINT LIST: state as hard rules what I may write - number of locations, "
                    "number of speaking parts, number of night exteriors, whether vehicles, crowds, "
                    "children, animals, water, rain, fire, or period dressing are permitted. Write these as "
                    "rules I must not break.\n"
                    "5. THE EXPENSIVE LIST: name the 10 things that cost the most in a short film and are "
                    "invisible to writers. I will check my script against this.\n"
                    "6. THE CHEAP POWER LIST: 8 things that are free or nearly free and read as high "
                    "production value - a specific time of day, weather that already exists, one excellent "
                    "location, a face, silence, a practical light, a single well-chosen prop, sound.\n"
                    "7. THE CONSTRAINT AS ENGINE: for each of my three tightest limits, describe how it "
                    "could become the film's strength rather than its compromise.\n"
                    "8. THE ONE SPLURGE: identify the single thing worth spending everything on in a film "
                    "like mine.\n\n"
                    "End by asking me which constraint I am most tempted to break, so we can decide now "
                    "rather than in the edit."
                ),
                "pro_tip": (
                    "Item 7 is the whole craft of low-budget filmmaking. A film set in one room at night "
                    "because that is all you had reads as a stylistic choice if you write it as one - and "
                    "reads as a limitation if you write around it."
                ),
            },
            {
                "title": "The Ending First",
                "desc": (
                    "Shorts are built backwards. This prompt writes your last image before anything else, "
                    "then derives the opening image that it will answer."
                ),
                "prompt_text": (
                    "You are a short film editor and story consultant who believes a short film is its "
                    "last thirty seconds and everything else is preparation.\n\n"
                    "My one thing: [PASTE FROM PROMPT 1]\n"
                    "My format and runtime: [FROM PROMPT 2]\n\n"
                    "Do the following:\n\n"
                    "1. THE LAST IMAGE: write my final shot as a single paragraph of pure action - what the "
                    "camera sees, what the audience understands, and what is deliberately withheld. This is "
                    "the target everything else aims at.\n"
                    "2. FOUR ALTERNATIVES: give me 4 completely different last images for this same idea, "
                    "each implying a different film, and say what each one makes the piece mean.\n"
                    "3. THE REFRAME TEST: for my chosen ending, state exactly what the audience now "
                    "understands that they did not ninety seconds earlier. If the answer is only 'what "
                    "happened', the ending is information rather than meaning - tell me and fix it.\n"
                    "4. THE LAST LINE QUESTION: decide whether this film should end on an image or on a "
                    "line of dialogue, and defend it. Default to image and make me argue otherwise.\n"
                    "5. THE OPENING IMAGE: now write the first shot, designed so the last one answers it. "
                    "Describe the rhyme between them.\n"
                    "6. THE TITLE: 6 title options, and say which ones do work the film then does not have "
                    "to.\n"
                    "7. THE BACKWARD CHAIN: working from the last image, list the 5 things an audience must "
                    "already know or feel for it to land. These become my scene requirements - anything not "
                    "on this list is a candidate for cutting.\n\n"
                    "End by asking me whether my ending is sad, hopeful or unresolved, and whether that "
                    "matches what I said the film was for in Prompt 1."
                ),
                "pro_tip": (
                    "Item 7 is the most useful list in this pack. Print it. Every time you are unsure "
                    "whether a scene belongs, check whether it delivers one of those five things - and if "
                    "it does not, it goes."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: BUILD THE SITUATION",
        "intro": (
            "Three prompts to construct what the camera will actually point at: a character the audience "
            "reads in under a minute from behaviour alone, a location that earns its place, and the "
            "pressure that makes the whole thing move."
        ),
        "prompts": [
            {
                "title": "The Character in One Page",
                "desc": (
                    "A short has no room for backstory and no need for it. This prompt builds people the "
                    "audience understands from what they do in the first minute."
                ),
                "prompt_text": (
                    "You are a screenwriting teacher who specialises in characterisation under extreme "
                    "length constraints.\n\n"
                    "My one thing and moment: [PASTE FROM PROMPT 1]\n"
                    "My last image and backward chain: [PASTE FROM PROMPT 3]\n"
                    "My speaking-part limit: [FROM PROMPT 2]\n\n"
                    "Build my CAST, staying inside my speaking-part limit:\n\n"
                    "1. THE PROTAGONIST: name, age, and - crucially - the single behaviour that tells an "
                    "audience who they are within their first thirty seconds on screen. Describe the "
                    "behaviour, not the biography.\n"
                    "2. THE FIVE BEHAVIOURS: five specific, filmable actions that reveal this person "
                    "without a word of exposition - how they handle an object, a queue, a phone, another "
                    "person, a delay.\n"
                    "3. WHAT THEY WANT IN THIS HOUR: not their life goal. The thing they want in the "
                    "runtime of this film. One sentence.\n"
                    "4. THE CONTRADICTION: the one inconsistency that makes them a person rather than a "
                    "function. Name it and name the moment it shows.\n"
                    "5. THE OTHER ROLES: for each remaining speaking part - who they are, the single "
                    "function they serve, and the one detail that stops them being a device. If any role "
                    "exists only to receive exposition, tell me to cut them.\n"
                    "6. THE CASTABILITY NOTE: for each part, what an actor gets to play. A short with no "
                    "actable moments will not attract anyone worth having.\n"
                    "7. WHAT WE NEVER LEARN: list 5 things about my protagonist the film deliberately does "
                    "not tell us. Restraint here is what makes shorts feel larger than their runtime.\n"
                    "8. THE ONE-LINE INTRODUCTIONS: write the exact character-introduction line for each "
                    "part as it will appear in the script - name in caps, age, one defining behaviour, no "
                    "biography.\n\n"
                    "End by asking me whether my protagonist changes in this film or is revealed, because "
                    "shorts usually do the second and pretend to do the first."
                ),
                "pro_tip": (
                    "Item 7 is counter-intuitive and correct. The short films that linger are the ones "
                    "where you sense a whole life you were not shown - and every fact you add closes that "
                    "space down."
                ),
            },
            {
                "title": "The Location That Earns Its Place",
                "desc": (
                    "In a short, every location costs a move, a permit and half a day. This prompt makes "
                    "each one do real work, and tests whether the film should be single-location."
                ),
                "prompt_text": (
                    "You are a location manager and production designer advising a short film writer "
                    "before they draft.\n\n"
                    "My situation and cast: [PASTE FROM PROMPTS 1 AND 4]\n"
                    "My constraint list: [PASTE FROM PROMPT 2 ITEM 4]\n"
                    "My backward chain: [FROM PROMPT 3 ITEM 7]\n\n"
                    "Do the following:\n\n"
                    "1. THE SINGLE-LOCATION TEST: tell me honestly whether this film could happen in one "
                    "location. If yes, describe the version that does and what it gains. If no, state the "
                    "specific story reason a second location is unavoidable.\n"
                    "2. THE LOCATION LIST: name each location I actually need, and for each: what it is, "
                    "what happens there, why the story cannot happen elsewhere, and roughly what it costs "
                    "to get.\n"
                    "3. THE PRIMARY SPACE: describe my main location in full production detail - its "
                    "layout, what is in it, where the light comes from, what it sounds like, what the walls "
                    "are made of, what is worn or broken. Two paragraphs.\n"
                    "4. THE SPACE AS CHARACTER: 6 specific details of this place that say something about "
                    "the person who lives or works in it. In a short, the set does the exposition.\n"
                    "5. THE GEOGRAPHY OF THE SCENE: where people can stand, sit, hide, leave from and be "
                    "trapped in. Blocking possibilities are story possibilities - list 5.\n"
                    "6. THE TIME OF DAY: choose it deliberately and defend it, accounting for cost - "
                    "night exteriors and magic hour are expensive, an overcast afternoon is free and "
                    "consistent.\n"
                    "7. THE SOUND OF THE PLACE: what the audience hears here, including the thing they "
                    "hear only once.\n"
                    "8. THE CHEAT LIST: 4 ways to imply a location I cannot afford with something I can - "
                    "a corridor for a hospital, a doorway for a house, sound for a crowd.\n\n"
                    "End by asking me which location I have written because I like it rather than because "
                    "the story needs it."
                ),
                "pro_tip": (
                    "Item 1 deserves a real attempt. Single-location shorts shoot in two days, look "
                    "deliberate, and force the writing to carry the film - which is exactly what a "
                    "calling-card short should demonstrate."
                ),
            },
            {
                "title": "The Want, the Obstacle and the Clock",
                "desc": (
                    "This prompt installs the pressure. Without a clock, a short becomes a mood piece; "
                    "with one, twelve minutes feels like no time at all."
                ),
                "prompt_text": (
                    "You are a story consultant who specialises in dramatic pressure in short-form "
                    "narrative.\n\n"
                    "My protagonist and what they want in this hour: [PASTE FROM PROMPT 4]\n"
                    "My location and its geography: [PASTE FROM PROMPT 5]\n"
                    "My last image and backward chain: [FROM PROMPT 3]\n\n"
                    "Do the following:\n\n"
                    "1. THE WANT, SHARPENED: restate what my protagonist is trying to get or avoid in this "
                    "runtime, as something concrete and physically visible. If it is abstract, give me the "
                    "object or action that stands in for it.\n"
                    "2. THE OBSTACLE: what stands in the way. Give me three versions - a person, a "
                    "circumstance, and the protagonist themselves - and recommend one for a film of my "
                    "length. Shorts usually work best with a human obstacle in the room.\n"
                    "3. THE CLOCK: what must happen or be prevented before the film can end, and how the "
                    "audience knows time is running out. Give me 4 options - an appointment, an arrival, a "
                    "process finishing, a decision someone else is making - and recommend one.\n"
                    "4. HOW THE CLOCK IS SHOWN: 5 visible or audible ways the audience feels the clock "
                    "without anyone mentioning it.\n"
                    "5. THE STAKES, MADE SMALL: state what happens if my protagonist fails, at the "
                    "smallest honest scale. In a short, small and specific beats large and abstract - name "
                    "the actual loss.\n"
                    "6. THE ESCALATION: 4 steps by which the situation gets worse across the runtime, each "
                    "raising a different kind of pressure.\n"
                    "7. THE TRAP: why my protagonist cannot simply leave, or take the obvious easy option. "
                    "State it plainly; every short film needs this answer on the page, not in your head.\n"
                    "8. THE PRESSURE-TO-PAGE MAP: given my page ceiling, roughly which page each "
                    "escalation step lands on.\n\n"
                    "End by asking me what my protagonist is willing to do at the end of this film that "
                    "they would not have done at the start."
                ),
                "pro_tip": (
                    "Item 7 is where readers stop believing scripts. If an audience can think of an "
                    "obvious way out that the film never addresses, you lose them - and it usually takes "
                    "one line or one closed door to fix."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: STRUCTURE IT",
        "intro": (
            "Three prompts on shape. Short films rarely use three acts - they use a smaller set of forms "
            "that fit their length. Pick the right one, map it against your page ceiling, and design the "
            "single turn the film exists to deliver."
        ),
        "prompts": [
            {
                "title": "The Short-Film Shape",
                "desc": (
                    "Three-act structure is a feature tool. This prompt picks the shape that actually "
                    "suits a short at your length and idea."
                ),
                "prompt_text": (
                    "You are a story structure specialist who works specifically in short form and does "
                    "not default to three acts.\n\n"
                    "My one thing, last image and pressure: [PASTE FROM PROMPTS 1, 3 AND 6]\n"
                    "My runtime and page ceiling: [FROM PROMPT 2]\n\n"
                    "Do the following:\n\n"
                    "1. THE SHAPE OPTIONS: describe 6 shapes that short films actually use, with the "
                    "length each suits best and the kind of idea each serves:\n"
                    "   - The Single Situation (one scene, real time, pressure builds to a break)\n"
                    "   - The Reveal (the audience is shown a situation, then shown what it really was)\n"
                    "   - The Escalating Repetition (the same action three times, changed each time)\n"
                    "   - The Journey (a character moves through a small space or short distance and is "
                    "changed by what they meet)\n"
                    "   - The Two-Hander (two people, one conversation, a negotiation that shifts)\n"
                    "   - The Vignette-and-Turn (a slice of life that pivots once, late)\n"
                    "2. THE RECOMMENDATION: pick the one that fits my idea and defend it in a paragraph. "
                    "Then name the shape I was probably about to use by default and say why it is worse "
                    "here.\n"
                    "3. THE SHAPE'S RULES: for my chosen shape, state the 4 rules it imposes - what must "
                    "happen by what point, what it cannot tolerate, where its danger of collapse is.\n"
                    "4. THE SCENE COUNT: how many scenes a film of my length and shape should have. Give "
                    "me a number and a range, and warn me what happens above it.\n"
                    "5. THE FIRST-MINUTE CONTRACT: what the opening sixty seconds must establish for my "
                    "shape to work - tone, world, who to watch, what kind of film this is.\n"
                    "6. THE MIDPOINT QUESTION: does a film of my length need a midpoint shift? Answer "
                    "honestly for my runtime, and if yes, say what it should be.\n"
                    "7. THE SHAPE FAILURE MODE: the specific way films of my chosen shape fall apart, and "
                    "the early warning sign I should watch for in my own draft.\n\n"
                    "End by asking me whether I want the audience ahead of my protagonist, behind them, or "
                    "level with them - because that choice governs the whole structure."
                ),
                "pro_tip": (
                    "The Single Situation is the most under-attempted and most effective shape for a "
                    "first short. One room, real time, rising pressure - it shoots in two days and it is "
                    "the hardest thing to fake, which is precisely why it impresses."
                ),
            },
            {
                "title": "The Scene Map",
                "desc": (
                    "This prompt lays out every scene against page count, so you know before drafting "
                    "exactly what each one does and how long it has to do it."
                ),
                "prompt_text": (
                    "You are a script consultant building a scene-by-scene map for a short film before the "
                    "writer drafts.\n\n"
                    "My shape and its rules: [PASTE FROM PROMPT 7]\n"
                    "My backward chain - what the ending requires: [PASTE FROM PROMPT 3 ITEM 7]\n"
                    "My escalation steps and clock: [PASTE FROM PROMPT 6]\n"
                    "My locations: [FROM PROMPT 5]\n"
                    "My page ceiling and scene count: [FROM PROMPTS 2 AND 7]\n\n"
                    "Build my SCENE MAP. For each scene give me:\n\n"
                    "1. Scene number, slugline (INT./EXT., location, time of day).\n"
                    "2. Page length allocated, and the running page total.\n"
                    "3. Who is in it.\n"
                    "4. The scene's job in one sentence - what it delivers that the ending requires. Cite "
                    "which item of my backward chain it serves.\n"
                    "5. The turn: what is different at the end of the scene than at the start. A scene "
                    "with no turn is a candidate for cutting.\n"
                    "6. How it gets out - the last beat, and how it hands off to the next scene.\n\n"
                    "Then give me:\n"
                    "7. THE CUT LIST: any scene that does not serve an item on my backward chain, or has "
                    "no turn, or duplicates another scene's job. Recommend cuts or merges.\n"
                    "8. THE PAGE AUDIT: whether my allocations add up to my ceiling, and where I am "
                    "over-spending. Name the scene I have given too many pages to.\n"
                    "9. THE SILENCE BUDGET: which scenes should have little or no dialogue, and where the "
                    "film's quietest moment belongs.\n"
                    "10. THE ENTRY POINT CHECK: for each scene, whether I am starting it too early. Most "
                    "short scenes should begin two beats later than instinct suggests.\n\n"
                    "End by asking me which scene I am most attached to, so we can check honestly whether "
                    "the film needs it."
                ),
                "pro_tip": (
                    "Item 10 is the single highest-value note in short filmmaking. Cut the arrival, the "
                    "greeting and the settling-in from every scene - start on the line that matters and "
                    "you will find two minutes of runtime you did not know you had."
                ),
            },
            {
                "title": "The Turn",
                "desc": (
                    "Every short film exists to deliver one reversal. This prompt designs it, places it, "
                    "and sets up the information the audience needs for it to land rather than merely "
                    "surprise."
                ),
                "prompt_text": (
                    "You are a story consultant who specialises in the single reversal at the heart of a "
                    "short film.\n\n"
                    "My one thing: [PASTE FROM PROMPT 1]\n"
                    "My last image and reframe test: [PASTE FROM PROMPT 3]\n"
                    "My scene map: [PASTE FROM PROMPT 8]\n\n"
                    "Do the following:\n\n"
                    "1. THE TURN: state in two sentences the one reversal this film delivers. It may be a "
                    "revelation, a decision, a refusal, an arrival, or a change of understanding - but "
                    "there should be exactly one.\n"
                    "2. THE PLACEMENT: which scene and roughly which page it lands on. Then tell me whether "
                    "that is too early or too late for my shape and length.\n"
                    "3. EARNED VERSUS WITHHELD: state plainly whether my turn works because the audience "
                    "was given everything and still did not see it, or because information was hidden from "
                    "them. If it is the second, tell me and help me fix it - withheld turns feel like "
                    "tricks and kill rewatch value.\n"
                    "4. THE PLANTS: 5 specific details to seed earlier that will read as innocent first "
                    "time and inevitable second time. Say which scene each belongs in, using my scene map.\n"
                    "5. THE MISDIRECTION: what the audience believes instead, and the honest reason they "
                    "believe it. Misdirection must be true information pointed the wrong way, not a lie.\n"
                    "6. THE CHARACTER COST: what the turn costs my protagonist. A reversal with no cost is "
                    "a plot event rather than a story.\n"
                    "7. THE AFTERMATH LENGTH: how much film should remain after the turn. Give me a page "
                    "figure and warn me about both failure modes - ending too abruptly to feel the turn, "
                    "or explaining it for two pages afterwards.\n"
                    "8. THE REWATCH TEST: name 3 things that will read completely differently on a second "
                    "viewing. If you cannot find three, my turn is thin - say so.\n\n"
                    "End by asking me whether my protagonist understands the turn or only the audience "
                    "does, because those are two very different films."
                ),
                "pro_tip": (
                    "Item 3 is the line between a good short and a gimmick. The test is simple: could a "
                    "sharp viewer have worked it out from what you showed them? If not, you have hidden "
                    "information rather than constructed a reversal."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: WRITE THE SCRIPT",
        "intro": (
            "Three prompts and you have a draft. Shorts are one of the few forms you can genuinely draft "
            "in a single pass, so this phase sets the format contract, writes the whole thing, then takes "
            "the dialogue apart."
        ),
        "prompts": [
            {
                "title": "Format Discipline and the First Page",
                "desc": (
                    "Readers judge a script's competence on page one before they judge the story. This "
                    "prompt sets the format rules and drafts an opening page that earns the next fourteen."
                ),
                "prompt_text": (
                    "You are a professional screenwriter and script reader who can tell an amateur script "
                    "from its first page.\n\n"
                    "My opening image: [PASTE FROM PROMPT 3 ITEM 5]\n"
                    "My scene map, scene one: [PASTE FROM PROMPT 8]\n"
                    "My protagonist's introduction line and behaviours: [PASTE FROM PROMPT 4]\n"
                    "My location: [FROM PROMPT 5]\n"
                    "My first-minute contract: [FROM PROMPT 7 ITEM 5]\n\n"
                    "PART A - THE FORMAT RULES. Give me a reference list I will work from:\n"
                    "1. The standard elements - slugline, action, character cue, dialogue, parenthetical, "
                    "transition - and how each is used and abused.\n"
                    "2. THE NO-LIST: 10 things that mark a script as amateur - camera directions in the "
                    "action, unfilmables, dense action blocks, overuse of parentheticals, CONTINUED, "
                    "novelistic description, character thoughts, adverbs in dialogue cues, "
                    "we-see/we-hear, and one more.\n"
                    "3. THE DENSITY RULES: maximum action-paragraph length, how white space controls pace, "
                    "and how a page should look from across a room.\n\n"
                    "PART B - THE FIRST PAGE:\n"
                    "4. Write my actual first page in correct screenplay format. It must establish tone, "
                    "place, who to watch, and the kind of film this is - and it must contain something "
                    "happening.\n"
                    "5. Then give me 2 alternative versions of the same first page with different entry "
                    "points - one starting later, one starting on a different character or detail.\n"
                    "6. THE PAGE-ONE AUDIT: for the version you recommend, list what a reader knows after "
                    "one page, what they are curious about, and anything I have explained that I should "
                    "have shown.\n"
                    "7. THE TITLE PAGE: what goes on it and what does not. Keep it plain - a short script "
                    "title page with a logline, a WGA number and a quote reads as inexperience.\n\n"
                    "End by asking me whether a reader with 400 submissions would turn to page two, and "
                    "which specific line makes them."
                ),
                "pro_tip": (
                    "Ask for alternative entry points every time. The opening you wrote first is almost "
                    "always ninety seconds early, and comparing three versions side by side makes that "
                    "obvious in a way rereading one never does."
                ),
            },
            {
                "title": "The Draft",
                "desc": (
                    "Shorts can be drafted in one pass, which is a real advantage - the whole thing stays "
                    "in your head at once. This prompt writes the complete script from your scene map."
                ),
                "prompt_text": (
                    "You are my drafting partner on a short film screenplay. You write in correct "
                    "screenplay format and hand control back to me at the end.\n\n"
                    "CONTEXT:\n"
                    "- My approved first page and format rules: [PASTE FROM PROMPT 10]\n"
                    "- My full scene map with page allocations: [PASTE FROM PROMPT 8]\n"
                    "- My cast, their behaviours and introduction lines: [PASTE FROM PROMPT 4]\n"
                    "- My locations and their sound: [PASTE FROM PROMPT 5]\n"
                    "- My clock and escalation steps: [PASTE FROM PROMPT 6]\n"
                    "- My turn, its plants and its placement: [PASTE FROM PROMPT 9]\n"
                    "- My last image: [PASTE FROM PROMPT 3]\n"
                    "- My page ceiling: [FROM PROMPT 2]\n"
                    "- My constraint list - locations, cast, no night exteriors, and so on: [FROM PROMPT 2 "
                    "ITEM 4]\n\n"
                    "Write the complete screenplay, following these rules:\n\n"
                    "1. Correct format throughout. No camera direction, no unfilmables, no we-see.\n"
                    "2. Hit the page allocations from my scene map. If a scene wants to run long, cut "
                    "something else and tell me what.\n"
                    "3. Start every scene as late as possible - use the entry-point notes from Prompt 8 "
                    "item 10.\n"
                    "4. Plant every item from Prompt 9 item 4 in the scene assigned to it, written so it "
                    "reads as incidental.\n"
                    "5. Break nothing on my constraint list. No location, character or element that is not "
                    "already approved.\n"
                    "6. Respect the silence budget - the scenes marked quiet stay quiet.\n"
                    "7. Dialogue in speech rhythm: contractions, interruptions, incomplete sentences. "
                    "Nobody explains the theme.\n"
                    "8. End on my last image exactly as designed.\n\n"
                    "If the script runs long or short, work in sections rather than truncating - tell me "
                    "which scenes you are delivering and continue on my go-ahead.\n\n"
                    "After the script, give me: the final page count, a per-scene page breakdown against "
                    "my allocations, any constraint you had to strain, and anything in my scene map that "
                    "did not work once written.\n\n"
                    "End by asking me which scene fought back hardest while you were writing it, because "
                    "that is usually the one with a structural problem."
                ),
                "pro_tip": (
                    "Ask for the per-scene page breakdown every time. A short script that comes in three "
                    "pages over is not a trimming job - it usually means one scene is doing a job the "
                    "structure never assigned it."
                ),
            },
            {
                "title": "The Dialogue Pass: Say Less",
                "desc": (
                    "Short film dialogue fails by doing the picture's work. This prompt cuts everything "
                    "the image already says and makes the rest speakable."
                ),
                "prompt_text": (
                    "You are a dialogue editor and script doctor who has worked with actors and knows "
                    "which lines they quietly rewrite on set.\n\n"
                    "My draft, or the scene to work on: [PASTE THE SCRIPT OR ONE SCENE]\n"
                    "My cast and their behaviours: [PASTE FROM PROMPT 4]\n\n"
                    "Do a dialogue pass:\n\n"
                    "1. THE REDUNDANCY CUT: every line that says what the picture already shows. Mark each "
                    "and propose either a cut or a replacement action.\n"
                    "2. THE EXPOSITION SWEEP: every line delivering information for the audience's benefit "
                    "rather than the character's. Rewrite the three worst so the information arrives "
                    "through behaviour, an object, or an argument instead.\n"
                    "3. THE THEME POLICE: any line where a character states what the film is about. Cut "
                    "them all and tell me what is lost, honestly.\n"
                    "4. THE SPEAKABILITY TEST: read every line as an actor would. Flag anything "
                    "unspeakable - too literary, too long, too neat, wrong rhythm - and give me the spoken "
                    "version.\n"
                    "5. THE VOICE SEPARATION: cover the character names and tell me whether I could still "
                    "tell who is speaking. For any two characters who sound alike, give each a distinct "
                    "speech habit - length, vocabulary, what they avoid saying, whether they finish "
                    "sentences.\n"
                    "6. THE HALF-LINE PASS: find 8 lines that would land harder cut in half, and halve "
                    "them.\n"
                    "7. THE SILENCE SWAP: 5 places a line could be replaced by a look, a pause or an "
                    "action. Show me the replacement in action-line form.\n"
                    "8. THE PARENTHETICAL PURGE: remove every parenthetical that an actor would find "
                    "insulting or that the line already implies. Keep only the ones that change meaning.\n"
                    "9. THE BEST LINE: name the one line worth keeping exactly as written, so I know what "
                    "the register is when I rewrite the rest.\n\n"
                    "Return the pass as a list - original line, proposed change, one-line reason. Do not "
                    "rewrite the whole script.\n\n"
                    "End by asking me which character I most enjoy writing, because that is usually the "
                    "one whose dialogue needs cutting most."
                ),
                "pro_tip": (
                    "Item 5 is worth doing on paper. Print the dialogue with the names covered - if you "
                    "cannot tell your two characters apart, neither can a reader, and in a two-hander that "
                    "is fatal."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 5: MAKE IT SHOOTABLE",
        "intro": (
            "Three prompts that separate a script from a film. A production audit against your real "
            "resources, a runtime check with a stopwatch rather than a page count, and a visual pass that "
            "moves story off the page and onto the screen."
        ),
        "prompts": [
            {
                "title": "The Production Reality Audit",
                "desc": (
                    "This is the prompt that stops you writing a short you cannot make. It audits the "
                    "script line by line against what you actually have."
                ),
                "prompt_text": (
                    "You are a line producer breaking down a short film script for the first time. You "
                    "are blunt about what cannot be afforded.\n\n"
                    "My script: [PASTE IT]\n"
                    "My constraint list and resources: [PASTE FROM PROMPT 2]\n\n"
                    "Do a production breakdown:\n\n"
                    "1. THE ELEMENT LIST: go through the script and list every location, speaking part, "
                    "non-speaking extra, vehicle, animal, child, prop of consequence, costume change, "
                    "stunt, effect, weather condition and time-of-day requirement. Cite the scene for "
                    "each.\n"
                    "2. THE CONSTRAINT BREACHES: every place the script breaks a rule from my constraint "
                    "list. For each, give me the cheap rewrite that keeps the story beat.\n"
                    "3. THE EXPENSIVE FIVE: the five costliest things in this script, in order, with what "
                    "each will realistically cost me in money, time or goodwill.\n"
                    "4. THE SCHEDULE: a rough shooting schedule - how many days, which scenes group into "
                    "which day by location and time of day, and where the schedule is fragile.\n"
                    "5. THE CAST LOAD: how many days each actor is needed. Flag any part that requires an "
                    "actor for three days to deliver four lines - that part needs restructuring or "
                    "cutting.\n"
                    "6. THE WEATHER AND LIGHT RISK: every scene dependent on specific weather or light, "
                    "and the fallback for each.\n"
                    "7. THE PERMISSION PROBLEMS: anything requiring a permit, a closure, a release, a "
                    "licence, or an owner's cooperation. Name the three most likely to fall through.\n"
                    "8. THE SOUND PROBLEMS: locations where clean dialogue audio will be difficult, and "
                    "what to do about each. Bad sound sinks more shorts than bad images.\n"
                    "9. THE REWRITE FOR HALF: describe the version of this film that could be made for "
                    "half of what it currently needs, and tell me honestly what it would lose.\n\n"
                    "End by asking me which element I would cancel the shoot over rather than lose, so we "
                    "know what the film actually is."
                ),
                "pro_tip": (
                    "Item 8 is the note nobody gives writers. A scene set beside a main road or in a "
                    "reverberant hall can be unusable regardless of performance - and moving it one room "
                    "over at the writing stage costs you nothing."
                ),
            },
            {
                "title": "The Runtime and Table-Read Audit",
                "desc": (
                    "Page count lies. This prompt estimates real screen time scene by scene and finds the "
                    "cuts that bring the film to length before you shoot it rather than after."
                ),
                "prompt_text": (
                    "You are an editor and script supervisor estimating screen time from a short film "
                    "script. You know that the one-page-per-minute rule is a fiction.\n\n"
                    "My script: [PASTE IT]\n"
                    "My target runtime: [FROM PROMPT 2]\n\n"
                    "Do a runtime audit:\n\n"
                    "1. THE SCENE-BY-SCENE ESTIMATE: for each scene, estimate actual screen time, "
                    "accounting for the real factors - dialogue pace, pauses the scene requires, physical "
                    "action described, silence, entrances and exits, and any process that must play out. "
                    "Give me a running total.\n"
                    "2. THE DISCREPANCY: compare your total to my page count and to my target. Tell me by "
                    "how much I am over or under, and where the difference is concentrated.\n"
                    "3. THE SLOW SCENES: the three scenes that will play significantly longer than they "
                    "read, and why.\n"
                    "4. THE FAST SCENES: any scene that will play shorter than it reads, which usually "
                    "means the writing is thinner than it looks.\n"
                    "5. THE CUT CANDIDATES: to reach my target, name the cuts in order of least to most "
                    "painful - lines, then beats, then whole scenes. Give me the specific cut, not a "
                    "general suggestion.\n"
                    "6. THE FESTIVAL LENGTH NOTE: tell me what my runtime does to programming chances. Be "
                    "specific about where the thresholds are and what a film of my length is competing "
                    "against.\n"
                    "7. THE TABLE-READ SCRIPT: give me instructions for running a table read of a short - "
                    "who to invite, what to time, what to listen for, and the three questions to ask "
                    "afterwards that actually produce useful answers.\n"
                    "8. THE ACTOR QUESTIONS: 6 questions an actor will ask about their part that the "
                    "script does not currently answer. These are holes.\n\n"
                    "End by asking me whether I am willing to lose my favourite scene to hit my runtime, "
                    "because that is usually the choice."
                ),
                "pro_tip": (
                    "Actually run the table read, with a stopwatch, before the shoot. Every short film "
                    "that came in four minutes long in the edit could have found those minutes in a room "
                    "with four friends and a timer for the cost of an afternoon."
                ),
            },
            {
                "title": "The Visual Pass",
                "desc": (
                    "This prompt moves story from the dialogue into the frame - what is told by image, "
                    "blocking, objects and sound, and what a director needs from the page."
                ),
                "prompt_text": (
                    "You are a director and cinematographer reading a short film script for what is "
                    "actually on screen.\n\n"
                    "My script: [PASTE IT]\n"
                    "My location and its geography: [PASTE FROM PROMPT 5]\n"
                    "My last image and opening image: [FROM PROMPT 3]\n\n"
                    "Do a visual pass:\n\n"
                    "1. THE IMAGE INVENTORY: list the images this film actually gives an audience, in "
                    "order. Then tell me which ones are memorable and how many there really are - most "
                    "short scripts have two and think they have ten.\n"
                    "2. THE DIALOGUE-TO-IMAGE CONVERSIONS: 6 places where a line could become a shot. Give "
                    "me the action-line version of each.\n"
                    "3. THE OBJECT PASS: what physical objects carry story here? Name them, and identify "
                    "one object that could recur and accumulate meaning across the film.\n"
                    "4. THE BLOCKING NOTES: for my three most important scenes, how the physical "
                    "arrangement of people in the space could carry the subtext - who stands, who is "
                    "seated, who is between whom and the door, who turns away.\n"
                    "5. THE SILENT VERSION TEST: describe how much of this film would still be "
                    "comprehensible with the sound off. Then name the three story points that currently "
                    "exist only in dialogue and would be lost.\n"
                    "6. THE SOUND DESIGN OPPORTUNITIES: 5 places where sound rather than image does the "
                    "work - something heard and not seen, an absence of sound, a sound arriving before its "
                    "source.\n"
                    "7. THE ONE SHOT: identify the single shot this film should be remembered for, and "
                    "tell me whether the script currently sets it up or wastes it.\n"
                    "8. THE COVERAGE WARNING: any scene written in a way that will require expensive or "
                    "time-consuming coverage, with a simpler staging that achieves the same thing.\n"
                    "9. WHAT NOT TO WRITE: remind me which of these visual notes belong in the script and "
                    "which belong in a separate director's document, so I do not clutter the page with "
                    "camera direction.\n\n"
                    "End by asking me whether I am directing this myself, because the answer changes how "
                    "much of this goes on the page."
                ),
                "pro_tip": (
                    "Item 5 is the best diagnostic in the pack. Run the silent test honestly - if your "
                    "film collapses with the sound off, it is a radio play with pictures, and shorts that "
                    "travel are almost never that."
                ),
            },
        ],
    },

    {
        "name": "PHASE 6: SEND IT OUT",
        "intro": (
            "Three prompts to finish and place it. An audit against this form's specific failure modes, "
            "the package that goes out with the script, and an honest plan for what this short is "
            "actually for."
        ),
        "prompts": [
            {
                "title": "The Rewrite Audit",
                "desc": (
                    "A final pass against the failure modes particular to short films - the ones a feature "
                    "checklist will not catch."
                ),
                "prompt_text": (
                    "You are a script consultant doing a final pass on a short film screenplay. You know "
                    "the specific ways this form fails.\n\n"
                    "My one thing, last image and backward chain: [PASTE FROM PROMPTS 1 AND 3]\n"
                    "My turn: [PASTE FROM PROMPT 9]\n"
                    "My script: [PASTE IT]\n\n"
                    "Audit for the following, citing the page for every issue:\n\n"
                    "1. THE COMPRESSED-FEATURE TEST: any place this is behaving like a feature - a "
                    "subplot, a second want, a time jump, a montage, a character arc that needs ninety "
                    "minutes.\n"
                    "2. THE BACKWARD-CHAIN CHECK: every scene that does not deliver something my ending "
                    "requires. List them for cutting or merging.\n"
                    "3. THE ONE-THING DRIFT: has the film wandered off the single idea from Prompt 1? Name "
                    "where.\n"
                    "4. THE UNFILMABLES: every action line describing something a camera cannot record - "
                    "thoughts, memories, history, intentions.\n"
                    "5. THE LATE START CHECK: every scene that begins before it needs to, with the "
                    "specific line to start on instead.\n"
                    "6. THE EXPLAINING END: does anything after the turn exist to explain the turn? Cut "
                    "it.\n"
                    "7. THE AMBIGUITY AUDIT: distinguish honestly between the places my film is "
                    "deliberately open and the places it is simply unclear. Readers cannot tell the "
                    "difference and will assume the second - name each one.\n"
                    "8. THE FIRST-PAGE AND LAST-PAGE TEST: reread only page one and the last page. Do they "
                    "rhyme? Does the last one answer the first?\n"
                    "9. THE SO-WHAT: state in one sentence what an audience takes away from this film. If "
                    "you cannot, tell me - that is the most important note in the audit.\n"
                    "10. THE TITLE CHECK: does my title do work, mislead, or waste an opportunity?\n\n"
                    "Rank findings CRITICAL, MODERATE or MINOR, with a fix for every CRITICAL.\n\n"
                    "End by asking me which critical note I am going to argue with, because that is "
                    "usually the one that is right."
                ),
                "pro_tip": (
                    "Item 7 is where most first shorts lose their audience. Deliberate ambiguity requires "
                    "the audience to be certain about everything except the one thing you are withholding "
                    "- if they are confused about the basics, the ending reads as a mistake."
                ),
            },
            {
                "title": "The Package: Logline, Synopsis and Pitch",
                "desc": (
                    "What goes out with the script - to festivals, producers, cast and crew. This prompt "
                    "builds all of it from the material you already have."
                ),
                "prompt_text": (
                    "You are a producer's reader and festival submissions advisor who writes materials for "
                    "short films.\n\n"
                    "My one thing and format: [PASTE FROM PROMPT 1]\n"
                    "My protagonist, want, obstacle and clock: [PASTE FROM PROMPTS 4 AND 6]\n"
                    "My turn and ending: [PASTE FROM PROMPTS 3 AND 9]\n"
                    "My runtime and production scale: [FROM PROMPTS 2 AND 13]\n"
                    "What the film is for: [FROM PROMPT 1's CLOSING QUESTION]\n\n"
                    "Build my package:\n\n"
                    "1. THE LOGLINE: one sentence - protagonist, situation, want, obstacle. Give me 4 "
                    "versions, then say which is strongest and why. Do not reveal the turn.\n"
                    "2. THE ONE-PARAGRAPH SYNOPSIS: 80-120 words for submissions and programmers. No "
                    "spoiler, but a clear sense of what kind of film this is.\n"
                    "3. THE FULL SYNOPSIS: a one-page version for producers, which DOES include the "
                    "ending, because they need to know it works.\n"
                    "4. THE DIRECTOR'S STATEMENT: 150-200 words on why this film, why now, why me - "
                    "written without pretension. Then flag the three phrases that would read as "
                    "pretentious so I can avoid them.\n"
                    "5. THE TONE REFERENCES: how to describe this film's tone in comparisons without "
                    "over-claiming. Give me the sentence.\n"
                    "6. THE CAST PITCH: what to say to an actor to make them want the lead - which means "
                    "naming what they get to play, not summarising the plot.\n"
                    "7. THE CREW PITCH: the two-sentence version for a cinematographer, a sound recordist "
                    "and an editor - each emphasising something different.\n"
                    "8. THE FUNDING PARAGRAPH: if I am applying for money, the paragraph that states what "
                    "this film is, what it costs, and why it is a safe bet to finish.\n"
                    "9. THE PAGE-ONE-OF-THE-DECK: if I need a one-page look document, what goes on it.\n\n"
                    "End by asking me who the single most important person to send this to is, so we can "
                    "tailor the materials to them."
                ),
                "pro_tip": (
                    "Item 6 is the one to spend time on. A good actor will do a short for nothing if the "
                    "part is real - and 'here is a plot summary' has never persuaded anyone, while 'you "
                    "spend nine minutes deciding whether to tell the truth' has."
                ),
            },
            {
                "title": "What This Short Is For",
                "desc": (
                    "Shorts are means, not ends. This prompt builds the plan - festivals, production path, "
                    "and what the film is supposed to get you."
                ),
                "prompt_text": (
                    "You are a short film strategist who advises filmmakers on festival runs and career "
                    "use of shorts. You are realistic about outcomes.\n\n"
                    "My film, its runtime and scale: [PASTE FROM PROMPTS 1, 2 AND 13]\n"
                    "My package: [PASTE FROM PROMPT 17]\n"
                    "What I want this film to do for me: [STATE IT]\n\n"
                    "Build my plan:\n\n"
                    "1. THE HONEST ASSESSMENT: given what this film is, tell me plainly what it can "
                    "realistically achieve and what it cannot. No encouragement I have not earned.\n"
                    "2. THE FESTIVAL STRATEGY: how to think about tiers, submission order and timing, what "
                    "a premiere status actually costs and protects, and how to build a run rather than "
                    "scattering entries. Explain the principles rather than naming specific festivals, "
                    "since those change.\n"
                    "3. THE CATEGORY FIT: which kinds of festival and programme strand this film belongs "
                    "in, and the ones it will waste money on.\n"
                    "4. THE BUDGET FOR SUBMISSIONS: how to think about submission spend relative to "
                    "production budget, and the point at which to stop.\n"
                    "5. THE PROOF-OF-CONCEPT PATH: if this short is a feature pitch, what it must "
                    "demonstrate that a script alone cannot, and whether my current version does it. Then "
                    "tell me what the accompanying feature materials need to be.\n"
                    "6. THE CALLING-CARD PATH: if this is a directing or writing sample, name the specific "
                    "skill it demonstrates and whether that skill is what I want to be hired for.\n"
                    "7. THE ONLINE RELEASE QUESTION: when and whether to put this online, and what it "
                    "costs me in festival terms. Be specific about sequencing.\n"
                    "8. THE NEXT FILM: based on what this one demonstrates, what my next short should do "
                    "differently to build on it rather than repeat it.\n"
                    "9. THE SHORT-TO-FEATURE TEST: could this expand to a feature? Answer honestly - most "
                    "shorts cannot, because they are complete. If yes, name what would have to be built "
                    "out; if no, say so and tell me what feature idea it points toward instead.\n\n"
                    "End by asking me what I want to be making in five years, because that should decide "
                    "which of these paths I take."
                ),
                "pro_tip": (
                    "Item 8 is the one filmmakers skip and it compounds. Two shorts that demonstrate the "
                    "same skill are one short; two that demonstrate range are a body of work, and that is "
                    "what gets you the next thing."
                ),
            },
        ],
    },
]
