# -*- coding: utf-8 -*-
"""
Royalti Studios - Youth & Family Superhero Series Master Prompt Pack
(AI Video Line).

One pack spanning three jobs the other packs split: story and cast (as the
Superhero reading packs do), screen production with continuity locks across
episodes, and the packaging - key art and title treatment.

Prompt 1 locks the audience lean (MG or YA within a youth-and-family band).
Prompt 2 is the MODE LOCK - cinematic live-action look or animated cartoon -
and it routes every later prompt: design language, continuity method,
generation approach, and which kind of poster Prompt 23 produces.

Build with:
    python pack_builder.py youth_superhero_series_pack_data \
        "Youth_Family_Superhero_Series_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.

PROMPT COUNT: 26, above the 22 baseline. NOT because of the audience - a youth
pack would normally run fewer. It is up because the scope is three packs' worth
in one: story and cast (5), continuity and design (4), series and episodes (5),
generation (4), packaging (2). Stated to the user in chat on 2026-09-21.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "YOUTH & FAMILY SUPERHERO SERIES",
    "total_prompts": 26,
    "hook_line": "Build the hero, the villain, the crew and the world - then lock the look, generate the episodes, and put a real poster on the front.",
    "keyword_lines": [
        "Cinematic mode or cartoon mode • Continuity across episodes • Key art • Title treatment",
        "Powers with rules • A villain kids can understand • One trusted grown-up • Cliffhangers • Season arc",
    ],
    "subgenres_line": "Modes: Cinematic Live-Action Look, Animated Cartoon (2D or 3D). Formats: Micro-Episode (1-3 min), Short-Episode Series (3-8 min), Short Film Pilot (8-15 min), Animated Movie-Length (20-40 min)",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-21",
    "audience_line": "AI Video Line",
    "reading_level": "Ages 8-17  |  Youth & Family  |  MG-lean or YA-lean (locked at Prompt 1)",
    "cover_h2": "From Character to Finished Episodes, Cover Included",
    "works_with_line": "Works with ChatGPT • Claude • Midjourney • Nano Banana Pro • Google Veo • Kling • Seedance",
    "closing_tagline": "The powers are the fun. The continuity is the work. The poster is what makes anyone press play.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "This pack does three jobs in one document, because making one episode should not require holding "
        "three PDFs open. First it builds the story the way the Superhero reading packs do - hero, "
        "villain, crew, world, a power system with real rules. Then it locks the look and the continuity, "
        "which is the hard part of a series rather than a single film: faces and costumes have to survive "
        "not just forty shots but ten episodes. Then it writes and generates the episodes, and finishes "
        "with the packaging you actually need to publish - key art and a title treatment.\n\n"
        "Two locks run the whole pack. Prompt 1 sets your audience LEAN inside a youth-and-family band - "
        "MG-leaning for 8 to 12, YA-leaning for 13 to 17 - because family content has to work for kids "
        "with adults in the room, and the lean changes the stakes, the content gates and the humour. "
        "Prompt 2 is the MODE LOCK: cinematic live-action look, or animated cartoon. That single choice "
        "routes the design language, the continuity method, the generation approach and the kind of poster "
        "you end up with. Set both honestly and every later prompt does the right thing. Work in order and "
        "keep every output in one document - by Prompt 26 it is your series bible."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-4) - Lock it. Audience lean and episode format, the mode lock that routes "
        "everything, a power system with rules and a genuinely fun upside, and the series premise.",
        "Phase 2 (Prompts 5-9) - Cast and world. The hero, a villain a young viewer can understand and see "
        "beaten, the crew, the world including the grown-ups, and a design bible that gives every character "
        "a readable silhouette.",
        "Phase 3 (Prompts 10-13) - Lock the look and the continuity. The style lock as a reusable block, "
        "character reference plates, location and set locks, and costume, prop and power-effect locks. This "
        "phase is what makes a series possible rather than a set of unrelated clips.",
        "Phase 4 (Prompts 14-18) - The series and the episodes. Season architecture, an episode template "
        "you reuse, the pilot script, batch episode scripts, and the season beat map with its cliffhanger "
        "ladder.",
        "Phase 5 (Prompts 19-22) - Make it. Shot list with clip math, generation prompts routed by mode, "
        "audio as its own layer including voice for young characters, then assembly and pacing.",
        "Phase 6 (Prompts 23-26) - Package and release. The cover - a cinematic key art poster or an "
        "animated movie poster depending on your mode - the title treatment and episode thumbnails, the "
        "youth-and-family content audit alongside continuity QC, and the release plan with season two.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool, your image and video generation tools, and a place to save your "
        "outputs and asset IDs between prompts. Brackets like [THIS] are placeholders - replace them with "
        "your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular, and Prompts 1 and 2 tell you which prompts your "
        "combination needs. Cartoon mode? Prompt 11 gets easier and Prompt 10 carries more weight. "
        "Cinematic mode? Prompt 11 is the most important prompt in the pack. Making a single pilot rather "
        "than a season? Prompts 14, 17 and 18 become light passes. No dialogue? Prompt 21 shrinks and "
        "Prompt 19 gets much cheaper."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "A power that is fun before it is a burden, with rules a young viewer can reason about",
            "A villain whose reason a ten-year-old can restate, and who can actually be beaten",
            "Continuity locked before episode one - faces, costumes and sets have to survive a whole season",
            "One readable silhouette per character, so a viewer identifies everyone in one second at any size",
            "One trusted grown-up who helps without solving it, and adults who are present and real",
            "A hope floor the series never goes below, whatever the episode does on the way",
            "Episode-shaped stories: a complete beat every episode plus one thread that pulls to the next",
            "Cliffhangers that promise rather than withhold - a young viewer should want the next one, not feel tricked",
            "A locked look block pasted verbatim into every prompt, so ten episodes read as one show",
            "Key art that tells a scroller the genre, the tone and the age in under a second",
        ],
        "kills": [
            "Generating pretty clips before the continuity is locked, producing a cast that changes face every episode",
            "A design so detailed it cannot be reproduced - patterned costumes, intricate emblems, tiny props",
            "Grown-ups who are absent or stupid, which older youth viewers read as a cheat",
            "Power escalation as the only escalation, which flattens a season into bigger numbers",
            "Peril with no consequence, or consequence with no comfort - youth and family needs both",
            "A first episode that is all setup, betting on an audience that has not decided to care yet",
            "Legible text asked of a video generator - titles, signs and screens belong in post",
            "Dialogue-heavy episodes with on-screen lip-sync, which is the most expensive and most failure-prone choice available",
            "A poster that is a character standing still - no situation, no tone, no reason to press play",
            "Mode drift: a cinematic look in one episode and a stylised one in the next",
        ],
        "voice": [
            "Write prompts as camera-and-action instructions, one action per clip, concrete nouns and verbs",
            "Keep the look block and the negative block identical in every prompt - paste, never retype",
            "Name shot size and lens or animation language rather than a mood word",
            "Specify light by source and direction; in cartoon mode specify the lighting convention instead",
            "Describe characters using their canonical block verbatim, every single time",
            "Script dialogue for the age: kids speak in short bursts, interrupt, and do not explain themselves",
            "Let the jokes be physical - in both modes, a power going wrong is funnier than a line about it",
            "Log every prompt, seed and asset ID; an unreproducible good result is a lost result",
        ],
        "formula": (
            "Audience Lean + Mode Lock -> Power System With Rules -> The Hero, The Villain, The Crew -> "
            "The World and the Grown-Ups -> Design Bible and Readable Silhouettes -> Style Lock -> "
            "Reference Plates for Faces, Sets and Costumes -> Season Architecture -> Episode Template -> "
            "Pilot, Then Batches -> Shot List and Clip Math -> Generation, Hero Shots First -> Audio as "
            "Its Own Layer -> Assembly -> KEY ART AND TITLE -> Content and Continuity QC -> Release"
        ),
        "reader_expectations": (
            "A youth-and-family audience is two audiences at once. The young viewer wants the power to be "
            "exciting, the crew to be people they would join, the villain to be genuinely scary and "
            "genuinely beatable, and the episode to end somewhere. The adult in the room wants it to be "
            "kind at the bottom, funny enough to sit through, and honest about how hard being that age is. "
            "Both notice instantly when the show talks down to the young one. For a generated series they "
            "forgive a surprising amount of texture strangeness and forgive nothing about consistency - a "
            "face that changes between episodes ends the show for them. Platforms and parents additionally "
            "read the key art before anything else, which is why it is a prompt in this pack rather than an "
            "afterthought."
        ),
        "level_spec": [
            "MG lean (ages 8-12): protagonist 10-13. Peril yes, injury light, no death of a main character "
            "without great care, no romance beyond a first crush, hope floor mandatory and visible",
            "YA lean (ages 13-17): protagonist 15-18. Real loss, real moral failure, a real romance, harder "
            "consequences - still no gore, still a hope floor, still adults who are real",
            "Family band, both leans: no gore, no cruelty shown, no sexualised framing of young characters, "
            "no violence without consequence, and no episode that ends in despair",
            "Episode length: micro 1-3 min, short-episode 3-8 min, pilot 8-15 min, animated movie 20-40 min",
            "Season shape: 6-10 episodes is the workable range for a generated series",
            "Dialogue: keep on-screen lip-synced lines to a minimum in both modes; cartoon mode tolerates "
            "more, cinematic mode very little",
            "Cast size: 4-6 named characters maximum for a generated series - every face is a full "
            "continuity problem across every episode",
        ],
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "Two things will decide whether this series exists: whether you locked the continuity before you "
        "started generating, and whether the poster makes anyone press play. Everything in the middle is "
        "craft you can learn as you go, but those two are structural. Phase 3 is not admin - it is the "
        "reason episode seven still looks like episode one, and it is the phase everyone skips because "
        "reference plates are not as fun as clips. Do it anyway. And build the key art in Prompt 23 as "
        "seriously as you build the pilot, because for a young audience scrolling past, the cover IS the "
        "show until they click. Then keep the hope floor. Whatever happens in episode five, the kid "
        "watching needs the thing you wrote down in Prompt 1 to still be true at the end."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: LOCK IT",
        "intro": (
            "Four prompts, and the first two run the rest of the pack. Prompt 1 sets your audience lean "
            "inside the youth-and-family band. Prompt 2 is the mode lock - cinematic or cartoon - which "
            "routes design, continuity, generation and the poster. Set both honestly before anything else."
        ),
        "prompts": [
            {
                "title": "Audience Lean and Episode Format",
                "desc": (
                    "Youth and family is a band, not a single audience. This prompt sets your lean, your "
                    "episode length and your season shape, and tells you what all three permit."
                ),
                "prompt_text": (
                    "You are a development executive for youth and family screen content who understands "
                    "the difference between an eight-year-old's show and a sixteen-year-old's.\n\n"
                    "My idea is: [DESCRIBE IN 2-5 SENTENCES]\n"
                    "Who I picture watching: [DESCRIBE, OR SAY 'YOU TELL ME']\n"
                    "Where it would live: [A PLATFORM, A CHANNEL, SHORT-FORM VERTICAL, OR 'UNDECIDED']\n\n"
                    "Do the following:\n\n"
                    "1. THE LEAN LOCK: recommend MG-LEAN (ages 8-12, protagonist 10-13) or YA-LEAN (ages "
                    "13-17, protagonist 15-18). Justify it against my idea, and state plainly what the "
                    "other lean would change.\n"
                    "2. THE FAMILY TEST: youth and family means a young viewer with an adult in the room. "
                    "Name the 3 things my show must give the young viewer and the 3 things it must give the "
                    "adult, and the one element that can serve both at once.\n"
                    "3. THE CONTENT GATES: for my lean, state specifically what is in range and out of "
                    "range - peril, injury, death, grief, bullying, romance, family difficulty, scary "
                    "imagery, humour. For each, the range and the framing that would take it out of range.\n"
                    "4. THE HOPE FLOOR: the specific thing that must still be true at the end of every "
                    "episode and at the end of the season, even in the darkest version. One sentence. "
                    "Non-negotiable in this band.\n"
                    "5. THE EPISODE FORMAT: recommend one from - micro-episode (1-3 min), short-episode "
                    "series (3-8 min), short film pilot (8-15 min), animated movie-length (20-40 min). "
                    "Justify it against my platform and my resources.\n"
                    "6. THE SEASON SHAPE: how many episodes, and why that number. Then state the total "
                    "runtime and warn me what that means in generation terms.\n"
                    "7. WHAT THE FORMAT HOLDS: for my episode length, state how many scenes, how many "
                    "speaking characters and how much story one episode can carry. Write these as limits.\n"
                    "8. THE ATTENTION REALITY: what the first fifteen seconds of an episode must do for my "
                    "lean and platform. Be specific - a young viewer scrolling decides faster than any "
                    "other audience.\n\n"
                    "End by asking me whether I want a kid to watch this alone or with a parent, because "
                    "that answer changes the jokes more than anything else."
                ),
                "pro_tip": (
                    "Write the hope floor from item 4 somewhere you will see it every session. Around "
                    "episode five of any series, the temptation is to end dark for impact - that one "
                    "sentence is what keeps the show the thing you set out to make."
                ),
            },
            {
                "title": "The Mode Lock: Cinematic or Cartoon",
                "desc": (
                    "The single most consequential choice in the pack. This prompt picks live-action "
                    "cinematic or animated cartoon and routes every later prompt accordingly."
                ),
                "prompt_text": (
                    "You are an AI production supervisor who has delivered both photoreal and animated "
                    "generated series and is honest about the trade-offs.\n\n"
                    "My idea, lean and format: [PASTE FROM PROMPT 1]\n"
                    "My tools: [NAME YOUR IMAGE AND VIDEO ENGINES]\n"
                    "My budget and timeline: [BE HONEST]\n\n"
                    "Do the following:\n\n"
                    "1. THE MODE OPTIONS: describe the two modes properly:\n"
                    "   - CINEMATIC MODE: a live-action look. Photoreal human faces, real-world lighting, "
                    "lens language, a film grade. Reads as a show or a film.\n"
                    "   - CARTOON MODE: animated, 2D or 3D. Stylised characters, animation lighting "
                    "conventions, a design language rather than a photographic one.\n"
                    "2. THE HONEST COMPARISON: for my specific idea, compare the two across - continuity "
                    "difficulty, cost per episode, how forgiving each is of generation error, how well "
                    "each suits my audience lean, dialogue and lip-sync feasibility, and how each ages. Be "
                    "blunt: photoreal young human faces are the hardest continuity problem in generated "
                    "video, and stylised characters are considerably more forgiving.\n"
                    "3. THE RECOMMENDATION: pick one and defend it in a paragraph. If my idea would work "
                    "in either, say which is the safer first series and which is the more ambitious one.\n"
                    "4. IF CARTOON: recommend a specific animation register - 2D flat, 2D painterly, 3D "
                    "stylised, 3D toy-like, cut-paper, storybook - and say what each signals to my audience "
                    "lean. Note which registers current tools hold most consistently.\n"
                    "5. IF CINEMATIC: state the specific constraints this imposes - how much of a face "
                    "can be shown and for how long, whether characters can be the same age throughout, how "
                    "to handle close-ups, and which shots to simply avoid.\n"
                    "6. THE ROUTING TABLE: tell me exactly how my chosen mode changes each later phase - "
                    "what Prompt 9's design bible produces, what Prompt 10's style lock contains, how "
                    "Prompt 11's plates work, which engines Prompt 20 should use, and what kind of poster "
                    "Prompt 23 will make.\n"
                    "7. THE MODE DISCIPLINE: state the rule plainly - the mode is locked for the whole "
                    "series and cannot drift between episodes. Name the three ways drift happens.\n"
                    "8. THE HYBRID WARNING: if I am tempted to mix modes, explain when that works (a "
                    "stylised sequence inside a cinematic show, for a memory or a power effect) and when it "
                    "reads as inconsistency.\n\n"
                    "End by asking me which mode I actually want to watch, because a series takes long "
                    "enough that the answer matters."
                ),
                "pro_tip": (
                    "For a first generated series with young characters, cartoon mode is the "
                    "recommendation almost every time. Stylised faces hold across episodes where photoreal "
                    "ones drift, and the audience reads style as a choice rather than a limitation."
                ),
            },
            {
                "title": "The Power System",
                "desc": (
                    "A power with rules a young viewer can reason about, a cost that is funny before it is "
                    "serious, and a visual signature the generation can actually reproduce."
                ),
                "prompt_text": (
                    "You are a systems designer building a power for a youth-and-family series that must "
                    "also be renderable consistently in generated video.\n\n"
                    "My lean and content gates: [PASTE FROM PROMPT 1]\n"
                    "My mode: [PASTE FROM PROMPT 2]\n"
                    "My hero's power, roughly: [DESCRIBE, or say 'you choose']\n\n"
                    "Do the following:\n\n"
                    "1. THE MECHANISM: what the power does, in three sentences a viewer of my lean could "
                    "repeat to a friend. If it cannot be explained that simply, simplify it.\n"
                    "2. THE FIVE HARD LIMITS: what it can never do. Write them as rules I may not break "
                    "for plot convenience. At least two should be inconvenient rather than dramatic, "
                    "because inconvenient limits generate episodes.\n"
                    "3. THE COST: what using it takes, at three levels with recovery times. For my lean, "
                    "calibrate how serious the cost can get.\n"
                    "4. THE FUNNY COST: the embarrassing, public, visible price of using it. For a youth "
                    "audience this is as important as the dramatic one.\n"
                    "5. THE FUN LIST: 8 things the hero does with this power purely because it is "
                    "brilliant. An early episode should spend real time here - the enjoyment is the hook.\n"
                    "6. THE VISUAL SIGNATURE: this is the generation question. Describe how the power LOOKS "
                    "when used, in terms my mode can reproduce consistently. Simple, bold and repeatable "
                    "beats intricate - name the specific effect (a colour, a distortion, a light, a "
                    "particle, a posture) and write it as a reusable phrase for prompts.\n"
                    "7. THE GENERATION REALITY CHECK: tell me honestly whether my power is cheap or "
                    "expensive to render consistently. Flag anything that lands in a known failure zone - "
                    "fine hand movement, exact object counts, text, precise physics, transformations "
                    "mid-shot - and give me the cheaper visual alternative that reads the same.\n"
                    "8. THE SKILL CURVE: what the hero can do now, what the season unlocks, and what is "
                    "permanently out of reach. State what they will NOT learn, so no finale is won by a "
                    "new trick.\n"
                    "9. THE COUNTERS: 4 ways an ordinary adult, or a locked door, beats my hero. If there "
                    "are none, redesign the power.\n\n"
                    "End by asking me what the funniest thing about this power is, because if I cannot "
                    "answer that, the series is missing its engine."
                ),
                "pro_tip": (
                    "Item 6 is where most generated superhero series fall apart. Pick a power whose visual "
                    "is one bold repeatable element - a single colour of light, one kind of distortion - "
                    "and you will get consistency across a season for free."
                ),
            },
            {
                "title": "The Series Premise and Viewer Promise",
                "desc": (
                    "What the show is, in the form a platform, a parent and a ten-year-old each need to "
                    "hear it - plus the promises you cannot break."
                ),
                "prompt_text": (
                    "You are a development strategist positioning youth and family series.\n\n"
                    "My lean, format and season shape: [PASTE FROM PROMPT 1]\n"
                    "My mode: [PASTE FROM PROMPT 2]\n"
                    "My power system: [PASTE FROM PROMPT 3]\n\n"
                    "Do the following:\n\n"
                    "1. THE PREMISE: the series in two sentences - who, the power, the trouble, the "
                    "ongoing situation. Written so a viewer of my lean would want to watch.\n"
                    "2. THE THREE PITCHES: one for a young viewer (what they get), one for a parent (why "
                    "it is worth their kid's time), one for a platform (why it travels). Each one or two "
                    "sentences.\n"
                    "3. THE VIEWER PROMISE: one paragraph in the second person, addressed to my target age "
                    "('You will...').\n"
                    "4. THE APPEALS: the 3 I am leading with, from - power fantasy and agency, found "
                    "family, humour, mystery, moral dilemma, adventure, rivalry, the cost of "
                    "responsibility, wonder.\n"
                    "5. THE ENGINE QUESTION: what generates a new episode every week? Name the specific "
                    "recurring source of trouble - a rogues roster, a place that produces problems, a "
                    "secret that keeps nearly coming out, a rival, an institution. A series with no engine "
                    "runs out at episode three.\n"
                    "6. THE SEASON QUESTION: the one question the season answers, distinct from any "
                    "episode's.\n"
                    "7. THE FOUR PROMISES: what I must not break given this lean and mode, and what "
                    "breaking each would cost me in audience or in reviews.\n"
                    "8. THE COMPARISON SET: 4 kinds of youth or family show that occupy similar ground - "
                    "describe the type rather than naming titles - and what each does that mine will be "
                    "measured against.\n"
                    "9. THE ORIGINALITY CHECK: the 5 most familiar elements in my concept and one specific "
                    "way to make each mine.\n"
                    "10. THE TITLE: 8 series title options. Mark which ones a ten-year-old would say out "
                    "loud to a friend, because that is the test at this age.\n\n"
                    "End by asking me what I want a kid to do after watching an episode, because that is "
                    "what the series is actually for."
                ),
                "pro_tip": (
                    "Item 5 is the one that decides whether you have a series or a short film. Write the "
                    "episode engine down explicitly - if you cannot name what generates next week's "
                    "trouble, you have a pilot and nothing after it."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: CAST AND WORLD",
        "intro": (
            "Five prompts building everything the reading packs build - hero, villain, crew, world - plus "
            "one the prose packs never need: a design bible, because on screen every character has to be "
            "identifiable in one second at thumbnail size."
        ),
        "prompts": [
            {
                "title": "The Hero",
                "desc": (
                    "A protagonist with a want, a worry and a flaw that causes real problems - built for "
                    "the age lean and for a season rather than one story."
                ),
                "prompt_text": (
                    "You are a character developer for youth and family series.\n\n"
                    "My lean and content gates: [PASTE FROM PROMPT 1]\n"
                    "My power, its costs and kid-life collisions: [PASTE FROM PROMPT 3]\n"
                    "My premise and episode engine: [PASTE FROM PROMPT 4]\n"
                    "My rough hero idea: [DESCRIBE, or say 'you choose']\n\n"
                    "Build my HERO:\n\n"
                    "1. THE BASICS: name, age (inside my lean's protagonist range), who they live with, "
                    "school or situation, what they are into, what their room looks like.\n"
                    "2. THE WANT: what they wanted before any of this - small, concrete, achievable, and "
                    "something a viewer can root for across a season.\n"
                    "3. THE WORRY: the fear underneath, which they could not put into words.\n"
                    "4. THE FLAW: a real flaw that causes real problems. Not shyness, not being too kind. "
                    "Then 3 specific episodes where the flaw makes things worse.\n"
                    "5. HOW THE POWER ARRIVED: told the way this age would remember it - one strange "
                    "sensory detail and one embarrassing part.\n"
                    "6. WHY THEY KEEP GOING: the reason they do not just tell a grown-up and stop. It must "
                    "be a reason someone this age would actually have.\n"
                    "7. THE SEASON ARC: 5 stages from who they are to who they become, each pushed by an "
                    "external event. One must be a step backwards caused by the flaw. Map each stage to a "
                    "rough episode number.\n"
                    "8. THE THING THEY WILL NOT RISK: the person, pet or place the villain will threaten.\n"
                    "9. THE PERFORMANCE NOTE: since this is generated, describe how this character MOVES "
                    "and holds themselves - posture, walk, a habitual gesture. In generated video, "
                    "behaviour is what makes a character read as a person.\n"
                    "10. THE CATCHPHRASE QUESTION: whether this character has a repeated line or verbal "
                    "habit. For a youth series this is a real asset - recommend one or say why not.\n\n"
                    "End by asking me whether my hero gets the want from item 2 by the end of the season, "
                    "because young viewers remember that more than they remember any fight."
                ),
                "pro_tip": (
                    "Item 9 is specific to generated production and easy to overlook. A character with one "
                    "distinctive way of standing or moving survives inconsistent rendering far better than "
                    "one defined only by their face."
                ),
            },
            {
                "title": "The Villain",
                "desc": (
                    "An antagonist a young viewer can understand and see beaten - frightening inside your "
                    "content gates, and designed to recur across a season."
                ),
                "prompt_text": (
                    "You are an antagonist developer for youth and family screen content. You know the "
                    "villain must be understandable, genuinely threatening, and beatable.\n\n"
                    "My lean, content gates and hope floor: [PASTE FROM PROMPT 1]\n"
                    "My hero, their flaw and what they will not risk: [PASTE FROM PROMPT 5]\n"
                    "My power system and its counters: [PASTE FROM PROMPT 3]\n"
                    "My mode: [FROM PROMPT 2]\n\n"
                    "Build my ANTAGONIST LAYER:\n\n"
                    "1. THE MAIN VILLAIN: who they are, what they want, and the reason they want it - "
                    "stated so simply a viewer of my lean would say 'oh, I get it'. Not chaos. Something "
                    "wanted, lost or owed.\n"
                    "2. KID OR GROWN-UP: decide, and give the trade-off. A young antagonist is more "
                    "personal and more redeemable; an adult is more frightening and harder to beat "
                    "believably. Recommend one for my lean.\n"
                    "3. THE THREAT, GATED: what they actually do, kept inside my content gates. Be "
                    "specific about what appears on screen and what happens off it.\n"
                    "4. WHY MY HERO CAN BEAT THEM: the honest answer. Not stronger - smarter, better "
                    "helped, more willing, or because they understood something. Name it now so no finale "
                    "is won by a power-up.\n"
                    "5. THE UNDERSTANDING SCENE: the moment my hero works out what the villain actually "
                    "wants. Place it in the season. This scene is the spine of youth antagonism.\n"
                    "6. REDEMPTION OR NOT: decide, and say what the season gains and loses either way. If "
                    "yes, name the price. If no, give the viewer something else - understanding, pity, or a "
                    "clear reason they chose this.\n"
                    "7. THE VISUAL DESIGN: since this is generated, describe the villain in terms my mode "
                    "can reproduce - one bold silhouette, one signature colour, one repeatable feature. "
                    "Simpler than instinct suggests. Flag anything intricate and simplify it.\n"
                    "8. THE THREAT ESCALATION ACROSS THE SEASON: how they get harder without getting "
                    "stronger. Give the specific mechanism per episode block.\n"
                    "9. THE SECONDARY TROUBLE: two lesser antagonists for episodic use - one a peer, one "
                    "an adult who is unfair rather than evil. Each presses a different part of my hero.\n"
                    "10. THE SCARE CALIBRATION: for my lean, exactly how frightening this villain is "
                    "allowed to be on screen, and the technique for making them scary without breaking the "
                    "gates - implication, sound, reaction shots, what is not shown.\n\n"
                    "End by asking me whether my villain is lonely, because at this age band that is "
                    "almost always the true answer and it changes how I write them."
                ),
                "pro_tip": (
                    "Item 10 is the youth-and-family craft. The scariest thing a young viewer sees is "
                    "usually another character's face reacting to something off screen - it costs nothing "
                    "to generate and stays inside every content gate."
                ),
            },
            {
                "title": "The Crew",
                "desc": (
                    "The friends or team a young audience comes back for - where every member has a job "
                    "the plan cannot work without."
                ),
                "prompt_text": (
                    "You are an ensemble developer for youth and family series, working within a hard cast "
                    "limit because every face is a continuity problem across every episode.\n\n"
                    "My hero, their flaw and want: [PASTE FROM PROMPT 5]\n"
                    "My cast size limit: [FROM THIS PACK'S LEVEL SPEC - 4-6 NAMED CHARACTERS MAXIMUM]\n"
                    "My lean: [FROM PROMPT 1]\n"
                    "My mode: [FROM PROMPT 2]\n\n"
                    "Build my CREW of 2-4, staying inside my total cast limit:\n\n"
                    "1. For each: name, age, what they are like in one line, and how they and my hero "
                    "became friends.\n"
                    "2. THE JOB: the specific, real job each does that the plan cannot work without - the "
                    "planner, the one with the bike, the one who can talk to adults, the one who reads the "
                    "instructions, the lookout, the liar. No passengers.\n"
                    "3. THE UNPOWERED SKILL: something practical each one actually has - climbing, coding, "
                    "cooking, drawing, fixing, remembering everything. Young audiences love competence in "
                    "other young people.\n"
                    "4. THEIR POSITION: each one's honest opinion of what my hero is doing. At least one "
                    "must think it is a terrible idea and say so repeatedly.\n"
                    "5. THE FRICTION: for each, what would make them fall out with my hero. At this age a "
                    "broken friendship is a bigger stake than physical danger.\n"
                    "6. WHO KNOWS: how each learns the secret, in what order, across which episodes, and "
                    "which discovery goes badly.\n"
                    "7. THE ONE WHO TELLS: at least one should, at some point, tell an adult for good "
                    "reasons. Say who, when, and why they were arguably right.\n"
                    "8. THE VISUAL DISTINCTION: this is the generation requirement. For each crew member, "
                    "the ONE bold visual element that distinguishes them at a glance - hair shape, a "
                    "colour, a garment, a silhouette, an accessory. Everyone must be identifiable at "
                    "thumbnail size, in my mode.\n"
                    "9. THE GROUP VOICE: how they sound together - the running joke, the nickname, the "
                    "argument they have every episode. Give me a sample eight-line exchange at my lean.\n"
                    "10. THE DIALOGUE LOAD: which crew members carry the most lines, and a warning about "
                    "what that costs in generation if I am doing on-screen lip-sync.\n\n"
                    "End by asking me which crew member a viewer will love most, and whether I am prepared "
                    "to put that friendship at risk in the season."
                ),
                "pro_tip": (
                    "Item 8 is not cosmetic in this workflow. If two characters have similar hair and "
                    "similar clothes, the generation will merge them across episodes - one bold, distinct "
                    "visual per person is a continuity tool disguised as design."
                ),
            },
            {
                "title": "The World and the Grown-Ups",
                "desc": (
                    "The container that holds a youth series - school, town, the adults who notice - built "
                    "so the grown-ups are real without being able to solve the show."
                ),
                "prompt_text": (
                    "You are a worldbuilding consultant for youth and family series who believes absent or "
                    "foolish adults are the genre's laziest habit.\n\n"
                    "My lean and hope floor: [PASTE FROM PROMPT 1]\n"
                    "My hero and what they will not risk: [PASTE FROM PROMPT 5]\n"
                    "My power's visibility and costs: [PASTE FROM PROMPT 3]\n"
                    "My episode engine: [FROM PROMPT 4]\n\n"
                    "Build my WORLD:\n\n"
                    "1. THE PLACE: the town, city or neighbourhood in one warm, specific paragraph - who "
                    "lives here, what it is known for, what it has lost.\n"
                    "2. THE REACH PROBLEM: how far my hero can actually get, given their age, money, "
                    "transport and having to be home. Be concrete - this constraint generates episodes for "
                    "free.\n"
                    "3. THE SIX PLACES: name and describe 6 recurring locations - school, home, the "
                    "hideout, and three others. Each needs a landmark and a reason to return. Recurring "
                    "locations are also a continuity asset: fewer sets, more consistency.\n"
                    "4. THE SCHOOL OR EQUIVALENT: the institution that holds the cast together - who runs "
                    "it, what the pressure is, the calendar of events I can hang episodes on.\n"
                    "5. THE HOUSEHOLD: who my hero lives with, the rules of the house, and 6 specific "
                    "things the adults have already noticed. Then what they currently believe is going on, "
                    "which should be plausible and wrong.\n"
                    "6. THE TRUSTED GROWN-UP: the one adult who can be told and will help. Describe them, "
                    "why my hero trusts them, what they can offer - and then state EXACTLY what they cannot "
                    "do, so my hero still has to fix it. That limit is the most important line here.\n"
                    "7. THE ADULT LIMIT: state plainly why the grown-ups cannot solve the series' problem. "
                    "It must be a real reason - they do not believe it, cannot get there, are not allowed, "
                    "are being lied to - never stupidity.\n"
                    "8. WHAT THE WORLD KNOWS ABOUT POWERS: whether powers are public, secret, rumoured or "
                    "brand new, and what the town, the school and the authorities do about it at my lean's "
                    "scale.\n"
                    "9. THE GROUNDING EPISODE: every youth series needs one where the hero is simply not "
                    "allowed out at the worst moment. Place it in the season.\n"
                    "10. THE SET LIMIT: given generation cost, confirm which of my six locations are "
                    "essential and which could be implied by a fragment, a doorway or a sound.\n\n"
                    "End by asking me which adult my hero is most afraid of, and whether that fear is fair."
                ),
                "pro_tip": (
                    "Item 7 is the prompt that saves the series. Write the reason down now - every time a "
                    "viewer could ask 'why doesn't she just tell her mum', you need that sentence to be "
                    "already true and already on screen."
                ),
            },
            {
                "title": "The Design Bible",
                "desc": (
                    "The prompt the prose packs never need. Every character gets a readable silhouette, a "
                    "colour, and a design simple enough to survive a whole season of generation."
                ),
                "prompt_text": (
                    "You are a character designer and art director for animated and live-action-look "
                    "series, working to the constraint that every design must be reproducible across many "
                    "generated episodes.\n\n"
                    "My mode and its animation register if cartoon: [PASTE FROM PROMPT 2]\n"
                    "My hero, villain and crew, including their visual distinctions: [PASTE FROM PROMPTS "
                    "5-7]\n"
                    "My lean: [FROM PROMPT 1]\n"
                    "My power's visual signature: [FROM PROMPT 3 ITEM 6]\n\n"
                    "Build my DESIGN BIBLE:\n\n"
                    "1. THE SILHOUETTE TEST: for each character, describe their silhouette - the shape "
                    "they make in black against white. Every one must be distinguishable from every other "
                    "at thumbnail size. Where two collide, change one and say what.\n"
                    "2. THE COLOUR ASSIGNMENT: one signature colour per character, chosen so the cast "
                    "reads as a set and no two are confusable. Give the palette, and note how it works in "
                    "my mode - cartoon mode can push saturation, cinematic mode works through wardrobe.\n"
                    "3. THE CANONICAL DESCRIPTION: for each character, a 25-50 word block using concrete "
                    "physical nouns only - no mood, no backstory, nothing an engine cannot render. These "
                    "blocks get pasted into every prompt verbatim, so write them to be reused.\n"
                    "4. THE SIMPLIFICATION PASS: go through every design and tell me what to REMOVE. "
                    "Patterns, logos, text, intricate fastenings, jewellery, complex hair, layered "
                    "costumes - none survive a season of generation. Recommend the plainer version of "
                    "each, and explain that a simple design is a continuity asset rather than a "
                    "compromise.\n"
                    "5. THE HERO COSTUME: if my hero has a suit or costume, design it to my mode's "
                    "constraints - one bold shape, one or two colours, one emblem simple enough to render "
                    "at any angle. Then describe how they look out of costume, and how the two read as the "
                    "same person.\n"
                    "6. THE COSTUME CHANGE PROBLEM: state how many distinct outfits this series can afford "
                    "across its cast, and recommend keeping most characters in one recognisable look per "
                    "season. Note this is how animated series have always worked and it is not a "
                    "limitation.\n"
                    "7. THE AGE READ: confirm each character reads as their stated age in my mode. This is "
                    "a known generation weakness - young characters drift older. Name the specific design "
                    "choices that hold an age.\n"
                    "8. THE POWER EFFECT DESIGN: the visual language of the power as a reusable phrase, "
                    "consistent with my mode.\n"
                    "9. THE MODE CONSISTENCY RULE: a short reusable block describing the design language of "
                    "the whole show, to be pasted alongside the style lock in Prompt 10.\n\n"
                    "End by asking me which character I have designed in the most complicated way, so we "
                    "can simplify it before it costs me the season."
                ),
                "pro_tip": (
                    "Run the silhouette test literally - describe each cast member as a black shape and "
                    "check they are all different. It is how animation has always solved readability, and "
                    "in generated video it doubles as insurance against the engine merging two characters."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: LOCK THE LOOK AND THE CONTINUITY",
        "intro": (
            "Four prompts, and this is the phase that makes a series possible. A single film needs "
            "continuity across forty shots; a season needs it across ten episodes generated weeks apart. "
            "Do not generate a single final clip until this phase is finished."
        ),
        "prompts": [
            {
                "title": "The Style Lock",
                "desc": (
                    "One reusable block, routed by your mode, pasted verbatim into every prompt for the "
                    "whole season. This is what makes episode seven look like episode one."
                ),
                "prompt_text": (
                    "You are a cinematographer (cinematic mode) or an art director (cartoon mode) writing "
                    "a reusable style specification for a generated series.\n\n"
                    "My mode and register: [PASTE FROM PROMPT 2]\n"
                    "My design bible and mode consistency block: [PASTE FROM PROMPT 9]\n"
                    "My lean and tone: [FROM PROMPT 1]\n\n"
                    "Do the following, writing for my mode specifically:\n\n"
                    "1. THE STYLE BLOCK: a single paragraph of 60-90 words specifying this series' visual "
                    "identity in engine-readable terms. For CINEMATIC mode cover aspect ratio, sensor or "
                    "stock character, grain, lens character and focal range, depth of field, palette with "
                    "named colours, contrast, and light quality. For CARTOON mode cover the animation "
                    "register, line treatment, shading convention (flat, cel, soft), outline presence, "
                    "palette, background style, and how light is handled as a convention rather than "
                    "physically. This block goes verbatim into every prompt for the whole season.\n"
                    "2. TWO ALTERNATIVES: two other style blocks for the same series, each implying a "
                    "different register, so I can compare before locking a season to one.\n"
                    "3. THE NEGATIVE BLOCK: a short reusable list of what must NEVER appear - specific "
                    "artifacts, styles, colour casts, on-screen text, and for cartoon mode any drift "
                    "toward photorealism, and for cinematic mode any drift toward stylisation. This goes "
                    "into every prompt alongside the style block.\n"
                    "4. THE CAMERA OR ANIMATION VOCABULARY: the deliberately limited set of shot sizes and "
                    "camera behaviours this series uses. Name 5-7 and forbid everything else. In cartoon "
                    "mode include the animation-specific moves the register permits.\n"
                    "5. THE MOVEMENT RULE: how much camera movement this series allows. Generated video "
                    "handles slow simple moves far better than complex ones - set a rule and keep it.\n"
                    "6. THE LIGHTING RULES: 5 rules about light. In cartoon mode these are conventions "
                    "(where shadows fall, whether rim light is used) rather than physics.\n"
                    "7. THE EPISODE CONSISTENCY PLAN: how to keep the look identical across episodes "
                    "generated weeks apart - what to record, what to re-test at the start of each episode, "
                    "and the specific check that catches slow drift.\n"
                    "8. THE THREE-SUBJECT TEST: instruct me to test the style block on three unrelated "
                    "subjects - a face, a room, an exterior - and confirm they all read as the same show "
                    "before locking. Tell me what to look for.\n\n"
                    "End by asking me whether this style is achievable consistently in my chosen engine, "
                    "and what to test first with one throwaway generation."
                ),
                "pro_tip": (
                    "Re-run the three-subject test at the start of every episode, not just once. Engines "
                    "update, and a style block that held in episode one can quietly produce a different "
                    "show by episode six - catching that early costs one generation."
                ),
            },
            {
                "title": "Character Reference Plates",
                "desc": (
                    "The plates that lock every face for the whole season. In cinematic mode this is the "
                    "most important prompt in the pack; in cartoon mode it is easier but still essential."
                ),
                "prompt_text": (
                    "You are a character reference artist producing season-long lock plates for a "
                    "generated series.\n\n"
                    "My canonical character blocks: [PASTE FROM PROMPT 9 ITEM 3]\n"
                    "My style block and negative block: [PASTE FROM PROMPT 10]\n"
                    "My mode: [FROM PROMPT 2]\n"
                    "My image engine: [NAME IT]\n\n"
                    "For each character, do the following:\n\n"
                    "1. THE PLATE SET: which reference images I need - a neutral front, a three-quarter, a "
                    "profile, a full-length for proportion and costume, an expression set, and one in the "
                    "series' actual lighting or shading. Say which are essential for my mode and which are "
                    "optional at my scale.\n"
                    "2. THE PLATE PROMPTS: the actual generation prompt for each plate. Each must contain "
                    "the character's canonical block verbatim, a neutral background, even light for the "
                    "identity plates, and my negative block. For cinematic mode, lock identity on flat "
                    "light BEFORE applying the series look. For cartoon mode, the style block is part of "
                    "the identity and goes in from the start - explain why the two modes differ here.\n"
                    "3. THE EXPRESSION SET: because this is a series, I need the same face across "
                    "emotions. Specify which expressions to plate and how many, and note this matters far "
                    "more for a season than for a single film.\n"
                    "4. THE AGE HOLD: the specific instruction that keeps a young character reading their "
                    "stated age. This is a known weakness - young faces drift older across generations. "
                    "Give me the wording that counteracts it and the check that catches it.\n"
                    "5. THE CONSISTENCY TEST: the test to run before approving a lock - generate the same "
                    "character in three different described situations and compare. State exactly what to "
                    "compare and what tolerance is acceptable.\n"
                    "6. THE REJECTION CRITERIA: what disqualifies a plate - an ambiguous age, asymmetry "
                    "that will not repeat, hair that could read two ways, an invented costume detail, a "
                    "silhouette that now collides with another character's.\n"
                    "7. THE ASSET DISCIPLINE: naming, storing and logging approved plates so every later "
                    "prompt references the right file. Give me a naming convention built for a season - it "
                    "must survive ten episodes and a break of weeks.\n"
                    "8. THE REFERENCE METHOD: the difference between locking identity by reference image "
                    "versus text alone, which my engine supports, and how many references work best.\n"
                    "9. THE PRIORITY ORDER: which character to plate first, and the instruction to stop "
                    "and report before proceeding - everything downstream depends on the lead's lock "
                    "holding.\n\n"
                    "End by asking me to generate the lead's plates first and report back, because if that "
                    "lock does not hold, the series scope needs rethinking before anything else is made."
                ),
                "pro_tip": (
                    "The expression set is what separates a series from a single film. A face locked only "
                    "in neutral will drift the moment a character laughs or shouts - plate the emotions "
                    "you know you need in episode one and you will use them all season."
                ),
            },
            {
                "title": "Location and Set Locks",
                "desc": (
                    "Recurring locations are a youth series' biggest continuity asset and its biggest "
                    "continuity risk. This prompt plates them and fixes their geography."
                ),
                "prompt_text": (
                    "You are a production designer creating location lock plates for a generated series.\n\n"
                    "My six recurring locations: [PASTE FROM PROMPT 8 ITEM 3]\n"
                    "My set limit: [FROM PROMPT 8 ITEM 10]\n"
                    "My style block and negative block: [PASTE FROM PROMPT 10]\n"
                    "My mode: [FROM PROMPT 2]\n\n"
                    "For each location, do the following:\n\n"
                    "1. THE ESTABLISHING PLATE: the prompt for the wide reference image that defines this "
                    "space - layout, contents, where light enters.\n"
                    "2. THE ANGLE SET: prompts for 3-4 further plates covering the angles my episodes will "
                    "need, each consistent with the establishing plate.\n"
                    "3. THE GEOGRAPHY NOTE: where things sit relative to each other - door, window, light "
                    "source, furniture. Generated shots contradict each other unless this is written down "
                    "and stated in every prompt.\n"
                    "4. THE SCREEN-DIRECTION RULE: which way characters face, enter and exit in each "
                    "space, so cuts do not flip the geography. One rule per location.\n"
                    "5. THE SIGNATURE ELEMENT: for each location, the ONE object or feature present in "
                    "every shot of that space, so a viewer knows instantly where they are. In a series "
                    "this does enormous work for almost nothing.\n"
                    "6. THE SIMPLIFICATION PASS: what to strip from each space. Cluttered environments do "
                    "not repeat - tell me what to remove and what single distinctive element to keep.\n"
                    "7. THE TIME-OF-DAY VERSIONS: for any location appearing at more than one time of day, "
                    "a plate per version, with what stays fixed.\n"
                    "8. THE SEASON REUSE PLAN: which locations appear in which episodes, so I can see "
                    "which plates are doing the most work and deserve the most care.\n"
                    "9. THE IMPLY LIST: for any location I cannot afford to lock, how to imply it - a "
                    "fragment, a doorway, a sound, a reaction shot.\n\n"
                    "End by asking me which location appears in the most episodes, because that is the one "
                    "whose geography I must write down most carefully."
                ),
                "pro_tip": (
                    "Fewer locations, used more often, is the correct answer for a generated series. Six "
                    "well-locked sets that recur build a world a viewer believes in; fifteen loosely "
                    "described ones build a slideshow."
                ),
            },
            {
                "title": "Costume, Prop and Power-Effect Locks",
                "desc": (
                    "The small elements where continuity most visibly fails - plus the power effect, which "
                    "in a superhero series has to look identical every single time."
                ),
                "prompt_text": (
                    "You are a props and costume supervisor locking small elements for a generated "
                    "superhero series.\n\n"
                    "My design bible and simplification pass: [PASTE FROM PROMPT 9]\n"
                    "My power's visual signature: [PASTE FROM PROMPT 3 ITEM 6]\n"
                    "My style block: [FROM PROMPT 10]\n"
                    "My mode: [FROM PROMPT 2]\n\n"
                    "Do the following:\n\n"
                    "1. THE POWER EFFECT LOCK: this is the most repeated visual in a superhero series, so "
                    "it comes first. Write the canonical description of the power effect as a reusable "
                    "phrase, then generate plate prompts showing it at three intensities. State exactly "
                    "what must be identical every time and what may vary.\n"
                    "2. THE COSTUME LOCKS: each character's outfit as a canonical block, already "
                    "simplified. Flag any pattern, logo, text, intricate fastening or jewellery and give "
                    "the plain replacement.\n"
                    "3. THE HERO SUIT DETAIL: if there is a suit, plate it from front, back and "
                    "three-quarter, plus the emblem alone so it can be matched. Note that an emblem with "
                    "fine detail or lettering will not survive - simplify now.\n"
                    "4. THE STORY PROPS: every object that matters across the season - handled, exchanged, "
                    "hidden, broken. For each, its canonical block and which episodes it appears in.\n"
                    "5. THE HANDLING WARNING: for each prop, flag whether a character must manipulate it "
                    "on screen. Hands plus small objects is the hardest thing to generate - for each "
                    "instance give the workaround: cut away, show the reaction, have it already done, "
                    "frame it out, or use sound.\n"
                    "6. THE STATE PROGRESSION: any prop or costume that changes across the season - "
                    "damaged, dirtied, upgraded, repaired - with the state per episode and a plate per "
                    "state.\n"
                    "7. THE TEXT PROBLEM: every place the series needs legible text - a sign, a phone, a "
                    "note, a school banner, an episode title card. For each, the post solution. Never ask "
                    "a video generator for text.\n"
                    "8. THE COUNT PROBLEM: anywhere the series needs a specific number of objects or "
                    "people. Flag and simplify.\n"
                    "9. THE ACCEPT-DRIFT LIST: the elements where inconsistency genuinely will not be "
                    "noticed, so I stop spending attention on them.\n\n"
                    "End by asking me which prop the season finale depends on, so we over-plate that one "
                    "now."
                ),
                "pro_tip": (
                    "Item 1 is where superhero series live or die visually. If the power looks different "
                    "in every episode, nothing else you lock will save the show - write one phrase for it "
                    "and never paraphrase."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: THE SERIES AND THE EPISODES",
        "intro": (
            "Five prompts turning a premise into a season. Architecture first, then a reusable episode "
            "template, then the pilot written properly, then batches - and a beat map so the cliffhangers "
            "pull rather than cheat."
        ),
        "prompts": [
            {
                "title": "Season Architecture",
                "desc": (
                    "How the season is shaped - what each episode does, what threads run through, and what "
                    "escalates when the power is not allowed to."
                ),
                "prompt_text": (
                    "You are a series architect for youth and family episodic content.\n\n"
                    "My premise, episode engine and season question: [PASTE FROM PROMPT 4]\n"
                    "My hero's season arc: [PASTE FROM PROMPT 5 ITEM 7]\n"
                    "My villain and their escalation: [PASTE FROM PROMPT 6]\n"
                    "My season shape and episode length: [FROM PROMPT 1]\n"
                    "My hope floor: [FROM PROMPT 1 ITEM 4]\n\n"
                    "Build my SEASON:\n\n"
                    "1. THE SHAPE: recommend one - episodic with a light thread (each episode "
                    "self-contained, one arc humming underneath), serialised (one continuous story in "
                    "parts), or hybrid. Justify it against my lean and episode length, noting that younger "
                    "viewers are better served by episodes that resolve.\n"
                    "2. THE EPISODE GRID: for each episode in my season - a working title, the trouble of "
                    "the week, which thread it advances, which crew member it features, and its one-line "
                    "hook. Every episode must do something no other episode does.\n"
                    "3. THE THREAD MAP: the 3 threads running through the season - the villain thread, the "
                    "secret-identity thread, and the personal thread from my hero's want. Mark which "
                    "episodes advance each, and flag any thread dark for more than two episodes.\n"
                    "4. THE ESCALATION RULE: what grows across the season, given that raw power may not. "
                    "Name 5 things to escalate instead - the intimacy of the threat, how many people "
                    "depend on the hero, how close the secret comes out, the cost per use, an adult "
                    "getting involved. Commit to them.\n"
                    "5. THE MIDPOINT: what changes halfway through so the back half is not the front half "
                    "repeated.\n"
                    "6. THE FINALE SHAPE: what the last episode does, how the season question is answered, "
                    "and how the hope floor holds.\n"
                    "7. THE RESET QUESTION: what returns to normal at the end of each episode and what "
                    "carries forward permanently. Get this explicit - a series where nothing carries "
                    "forward feels weightless, and one where everything does becomes impossible to enter "
                    "midway.\n"
                    "8. THE ENTRY-POINT RULE: how a viewer who starts at episode four can follow. For "
                    "youth content on a platform this matters enormously.\n"
                    "9. THE PRODUCTION ORDER: which episodes to make first - and note it should not be "
                    "episode order. Recommend starting with a mid-season episode as a test before "
                    "committing to the pilot.\n\n"
                    "End by asking me whether I could make just three of these episodes and still have "
                    "something, because that is probably what season one actually is."
                ),
                "pro_tip": (
                    "Take item 9 seriously. Making a mid-season episode first teaches you the workflow "
                    "cheaply, and the pilot - which has to be the best one - benefits from being made "
                    "second or third rather than while you are still learning."
                ),
            },
            {
                "title": "The Episode Template",
                "desc": (
                    "One reusable shape you apply to every episode, so the series has a rhythm and you "
                    "are not designing structure from scratch ten times."
                ),
                "prompt_text": (
                    "You are a showrunner designing the repeatable episode shape for a youth and family "
                    "series.\n\n"
                    "My episode length and what it holds: [PASTE FROM PROMPT 1]\n"
                    "My season shape and reset rule: [PASTE FROM PROMPT 14]\n"
                    "My lean and hope floor: [FROM PROMPT 1]\n"
                    "My power's rules and costs: [FROM PROMPT 3]\n\n"
                    "Build my EPISODE TEMPLATE:\n\n"
                    "1. THE BEAT SHAPE: the beats every episode hits, with a time or word allocation for "
                    "each, scaled to my episode length. Cover: the cold open hook, the ordinary situation, "
                    "the trouble arriving, the first attempt failing, the crew regrouping, the cost, the "
                    "fix built by the kids, the resolution, and the thread tag that pulls to next episode. "
                    "Adjust the list for my length - a 3-minute episode cannot hold all of it, so tell me "
                    "which beats survive.\n"
                    "2. THE COLD OPEN: what the first fifteen seconds must do, and 4 different cold-open "
                    "strategies I can rotate across the season so they do not feel identical.\n"
                    "3. THE FUNNY QUOTA: how many laughs per episode at my lean, and where they belong. "
                    "Then the rule about the physical joke - in both modes, the power going wrong is "
                    "funnier than a line about it.\n"
                    "4. THE COST BEAT: confirm every episode spends something specific - a grade, a "
                    "friendship, a lie, exhaustion, a broken thing. Give me the checklist.\n"
                    "5. THE KIDS-FIX-IT RULE: state the hard rule that the young characters solve it "
                    "themselves, with help, and name the 3 ways episodes accidentally break it.\n"
                    "6. THE THREAD TAG: how each episode ends on a pull without cheating. Explain the "
                    "difference between a cliffhanger that promises and one that withholds, and why the "
                    "second one loses a young audience's trust.\n"
                    "7. THE TITLE CARD AND RECAP: whether this series uses a recap, a title sequence, or "
                    "neither, given my episode length. Be strict - a 3-minute episode cannot afford 20 "
                    "seconds of titles.\n"
                    "8. THE RUNTIME DISCIPLINE: the actual target runtime and the maximum, and what to cut "
                    "first when an episode runs long.\n"
                    "9. THE TEMPLATE AS A FORM: write the template out as a blank fill-in structure I can "
                    "copy for every episode.\n\n"
                    "End by asking me whether a viewer could tell my episodes apart, because a template "
                    "applied too rigidly produces ten versions of the same episode."
                ),
                "pro_tip": (
                    "Item 2 matters more than it sounds. A series where every episode opens the same way "
                    "teaches viewers to skip the first fifteen seconds - rotate four cold-open strategies "
                    "and they keep watching from the first frame."
                ),
            },
            {
                "title": "The Pilot Script",
                "desc": (
                    "The episode that has to work hardest. It introduces everything, proves the tone, and "
                    "gives a young viewer a reason to come back."
                ),
                "prompt_text": (
                    "You are a screenwriter drafting the pilot of a youth and family superhero series.\n\n"
                    "My hero, crew, villain and world: [PASTE FROM PROMPTS 5-8]\n"
                    "My power system including the fun list: [PASTE FROM PROMPT 3]\n"
                    "My episode template: [PASTE FROM PROMPT 15]\n"
                    "My episode one entry from the grid: [PASTE FROM PROMPT 14 ITEM 2]\n"
                    "My lean, content gates and hope floor: [FROM PROMPT 1]\n"
                    "My mode: [FROM PROMPT 2]\n\n"
                    "Write the pilot, following these rules:\n\n"
                    "1. Use my episode template's beat shape and runtime target.\n"
                    "2. Open inside something already happening. No narrated introduction, no origin "
                    "recap, no explaining the world.\n"
                    "3. Establish the hero's want from Prompt 5 item 2 in the first two minutes, "
                    "concretely.\n"
                    "4. Put the power on screen early and let it be FUN before it is a problem, using the "
                    "fun list.\n"
                    "5. Introduce the crew with each one doing their job, not being described.\n"
                    "6. Put one adult on screen who notices something.\n"
                    "7. Deliver the villain or the trouble without over-explaining it - a young audience "
                    "will accept a threat before they understand it.\n"
                    "8. Keep the cast and locations inside my locked sets and canonical blocks. No new "
                    "characters, no new places.\n"
                    "9. Stay inside my content gates and above my hope floor.\n"
                    "10. Minimise on-screen lip-synced dialogue - prefer lines delivered off-screen, over "
                    "a reaction, or in wider shots. Tell me the count of on-screen speaking lines when you "
                    "are done.\n"
                    "11. End on the thread tag from my template.\n\n"
                    "Write it as a screenplay in standard format, or as a shot-by-shot treatment if that "
                    "suits my episode length better - tell me which you chose and why.\n\n"
                    "After the script, give me: estimated runtime, the on-screen dialogue count, which "
                    "locked assets it needs, anything in my plan that did not work once written, and the "
                    "three moments that will be hardest to generate.\n\n"
                    "End by asking me whether a viewer of my lean would start episode two, and which "
                    "specific moment makes them."
                ),
                "pro_tip": (
                    "Item 10's count is the single best predictor of how hard this pilot will be to "
                    "produce. If it comes back above a dozen on-screen speaking lines, rework them "
                    "off-screen before you generate anything."
                ),
            },
            {
                "title": "Episode Batch Scripts",
                "desc": (
                    "The prompt you reuse most. It writes two or three episodes at a time while holding "
                    "the template, the threads, the continuity and the content gates."
                ),
                "prompt_text": (
                    "You are my writing partner on a youth and family superhero series. You write episodes "
                    "to my template and hand control back at the end of every batch.\n\n"
                    "STANDING CONTEXT (reuse and update this block every batch):\n"
                    "- Approved pilot and its voice: [PASTE 500 WORDS OF YOUR APPROVED PILOT FROM PROMPT "
                    "16]\n"
                    "- My episode template: [PASTE FROM PROMPT 15]\n"
                    "- My lean, content gates and hope floor: [FROM PROMPT 1]\n"
                    "- My canonical characters and locked locations: [FROM PROMPTS 9 AND 12]\n"
                    "- Power rules I must not break: [THE FIVE HARD LIMITS AND COSTS FROM PROMPT 3]\n"
                    "- Thread state: [WHERE EACH OF THE THREE THREADS STANDS - FROM PROMPT 14]\n"
                    "- Who knows the secret: [CURRENT STATE, FROM PROMPT 7]\n"
                    "- Adults' suspicion level: [FROM PROMPT 8]\n"
                    "- Carried-forward consequences: [WHAT HAS NOT RESET, PER PROMPT 14 ITEM 7]\n"
                    "- Episode number and where we are in the season: [STATE IT]\n\n"
                    "THIS BATCH: write episodes [X] to [Y] from my season grid:\n"
                    "[PASTE THE GRID ENTRIES FROM PROMPT 14 ITEM 2]\n\n"
                    "Rules for this batch:\n"
                    "1. Follow the template's beat shape and hit the runtime target.\n"
                    "2. Rotate cold-open strategies so no two consecutive episodes open alike.\n"
                    "3. Every episode spends something specific and the kids fix it themselves.\n"
                    "4. Never exceed the power's hard limits or recover faster than the cost structure "
                    "allows.\n"
                    "5. Use only locked characters, locations and props. If an episode needs something "
                    "new, flag it rather than inventing it - new assets cost a plate.\n"
                    "6. Hit the funny quota.\n"
                    "7. Advance at least one thread per episode and do not leave any thread dark for more "
                    "than two.\n"
                    "8. Minimise on-screen lip-synced lines and report the count per episode.\n"
                    "9. Stay inside the content gates and above the hope floor.\n"
                    "10. End each episode on a thread tag that promises rather than withholds.\n\n"
                    "After the episodes, give me a STATUS REPORT: runtime per episode, on-screen dialogue "
                    "counts, thread state, who now knows, adults' suspicion, carried-forward consequences, "
                    "any new asset an episode requires, and anything I now owe the viewer.\n\n"
                    "End by asking me which episode in this batch is weakest, because in a season that is "
                    "the one to cut rather than fix."
                ),
                "pro_tip": (
                    "Rule 5 is the money-saver. Every episode that invents a new character or location "
                    "costs you a full plating cycle - a writing partner that flags rather than invents "
                    "keeps a season inside budget."
                ),
            },
            {
                "title": "The Season Beat Map and Cliffhanger Ladder",
                "desc": (
                    "A single view of the whole season - every beat, every thread, every cliffhanger - so "
                    "you can see the shape and fix it before you generate ten episodes."
                ),
                "prompt_text": (
                    "You are a showrunner auditing a full season before production.\n\n"
                    "My season architecture and episode grid: [PASTE FROM PROMPT 14]\n"
                    "My pilot and batch episodes: [PASTE THE SCRIPTS OR DETAILED SUMMARIES]\n"
                    "My hero's arc stages: [FROM PROMPT 5 ITEM 7]\n"
                    "My villain's escalation: [FROM PROMPT 6 ITEM 8]\n\n"
                    "Do the following:\n\n"
                    "1. THE BEAT MAP: a single table - episode by episode - showing the trouble, the cost "
                    "paid, which threads moved, the hero's arc stage, the villain's position, and the "
                    "closing tag.\n"
                    "2. THE CLIFFHANGER LADDER: list every episode ending and classify it - PROMISES "
                    "(makes the viewer want more), WITHHOLDS (hides information to force a click), "
                    "RESOLVES (closes cleanly), or FLAT (no pull). Rewrite every WITHHOLDS and every FLAT, "
                    "and confirm the season has enough RESOLVES that a young viewer never feels strung "
                    "along.\n"
                    "3. THE ARC PACING: whether the hero's five arc stages are evenly spread or bunched. "
                    "Name the episode where the arc stalls.\n"
                    "4. THE THREAD AUDIT: any thread dark too long, any thread that resolves too early, "
                    "any thread carrying no weight.\n"
                    "5. THE REPETITION SWEEP: any two episodes doing the same job, using the same trouble "
                    "shape, or featuring the same crew member twice in a row.\n"
                    "6. THE ESCALATION CHECK: confirm the season escalates the five things from Prompt 14 "
                    "item 4 rather than raw power. Flag any episode that cheats.\n"
                    "7. THE CONTENT ARC: whether the season's darkness rises appropriately for my lean and "
                    "never breaks the hope floor. Name the darkest episode and confirm the one after it "
                    "lets everyone breathe.\n"
                    "8. THE ASSET LOAD: which episodes need the most locked assets, so I can plan "
                    "generation order and spot the expensive ones.\n"
                    "9. THE CUT LIST: if I can only make part of this season, which episodes form a "
                    "coherent short run, in what order.\n"
                    "10. THE FINALE CHECK: does the last episode answer the season question and pay off "
                    "the hero's want? If it only resolves the villain, say so.\n\n"
                    "End by asking me which episode I am most excited to make, because that is the one to "
                    "produce first."
                ),
                "pro_tip": (
                    "Item 9 is the realistic one. Almost nobody finishes a ten-episode generated season - "
                    "knowing which four episodes stand alone as a run means you ship something rather than "
                    "abandoning something."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 5: MAKE IT",
        "intro": (
            "Four prompts and you are producing episodes. Shot list with real clip math, generation "
            "prompts routed by mode, audio as its own layer, then assembly. Generate a mid-season episode "
            "first, not the pilot."
        ),
        "prompts": [
            {
                "title": "Shot List and Clip Math",
                "desc": (
                    "Per episode, every shot with its duration, difficulty and generation budget - and an "
                    "honest answer about whether the season is affordable."
                ),
                "prompt_text": (
                    "You are a first assistant director and producer building shot lists for a generated "
                    "series and budgeting the season.\n\n"
                    "My episode script: [PASTE ONE EPISODE]\n"
                    "My camera or animation vocabulary and movement rule: [PASTE FROM PROMPT 10]\n"
                    "My engine's usable clip length and cost: [STATE IT - CHECK CURRENT VALUES, DO NOT "
                    "GUESS]\n"
                    "My mode: [FROM PROMPT 2]\n"
                    "My season length: [FROM PROMPT 1]\n\n"
                    "Do the following:\n\n"
                    "1. THE SHOT LIST for this episode. Per shot: number, scene, shot size and camera or "
                    "animation behaviour from my approved vocabulary, duration in seconds (inside my "
                    "engine's usable clip length), ONE clear action with a start and end state, which "
                    "locked assets appear, difficulty (simple, moderate, hard), generation attempts "
                    "budgeted, and whether audio must sync.\n"
                    "2. THE SPLIT RULE: any shot containing two actions gets split. Any beat needing "
                    "longer than my clip limit gets split. Do it and say what you split.\n"
                    "3. THE EPISODE TOTALS: shot count, runtime from the durations, total budgeted "
                    "generations, and whether they match the episode target.\n"
                    "4. THE SEASON EXTRAPOLATION: multiply this episode by my season length and give me "
                    "the total cost and total wall-clock time, including queue time, selection and "
                    "assembly. Then tell me plainly whether the season is affordable. If it is not, say "
                    "so now.\n"
                    "5. THE MODE COST NOTE: how my mode affects all of this. Cartoon mode is generally "
                    "cheaper per usable clip because it is more forgiving; cinematic mode needs more "
                    "attempts per shot, especially on faces. Give me the multiplier to plan with.\n"
                    "6. THE DIFFICULTY DISTRIBUTION: how many shots in each band. If more than a third are "
                    "hard, name the ones to rewrite as moderate.\n"
                    "7. THE HERO SHOTS: the 3-5 shots this episode cannot succeed without. These get the "
                    "attempts; everything else is rationed.\n"
                    "8. THE GENERATION ORDER: hero shots first, then hardest, then simple. Never script "
                    "order.\n"
                    "9. THE REUSE OPPORTUNITIES: shots that could be reused across episodes - "
                    "establishing shots of locked locations, a title-sequence beat, a recurring "
                    "transition. In a series this is significant savings and it is how animated series "
                    "have always worked.\n"
                    "10. THE CUT-FIRST LIST: the shots to abandon if budget runs out, ranked.\n\n"
                    "End by asking me whether I have generated a test episode yet, because these numbers "
                    "are estimates until one real episode exists."
                ),
                "pro_tip": (
                    "Item 9 is the series-specific saving nobody plans for. Generate your establishing "
                    "shots once, well, and reuse them all season - every animated series in history has "
                    "done exactly this and no viewer minds."
                ),
            },
            {
                "title": "Generation Prompts, Routed by Mode",
                "desc": (
                    "Reference images and video prompts written for your mode and your engines, with the "
                    "locked blocks pasted in verbatim."
                ),
                "prompt_text": (
                    "You are a prompt engineer for generative image and video, producing an episode of a "
                    "series in a locked style.\n\n"
                    "My shot list: [PASTE FROM PROMPT 19]\n"
                    "My mode and its routing table: [PASTE FROM PROMPT 2]\n"
                    "My style block and negative block: [PASTE FROM PROMPT 10]\n"
                    "My canonical character, location, costume and power-effect blocks: [PASTE FROM "
                    "PROMPTS 9 AND 11-13]\n"
                    "My approved plates: [LIST THEM]\n"
                    "My engines: [NAME THEM, WITH CURRENT CLIP LIMITS AND WHETHER EACH TAKES A START "
                    "FRAME, END FRAME OR TEXT ONLY]\n\n"
                    "Do the following:\n\n"
                    "1. THE MODE ROUTING: state how my mode changes prompt construction. Cartoon mode "
                    "needs the style block doing heavy lifting and tolerates simpler subject description; "
                    "cinematic mode needs reference plates carrying identity and the style block carrying "
                    "light and lens. Say which of my engines suits my mode best and flag anything I should "
                    "verify myself, since engine behaviour changes.\n"
                    "2. THE KEYFRAME DECISION: for each shot, whether to generate a controlled still first "
                    "or go text-to-video, based on how much compositional control it needs.\n"
                    "3. THE IMAGE PROMPT TEMPLATE: the reusable structure for keyframes - subject and "
                    "canonical block, action or pose, framing, lens or animation language, light or "
                    "shading convention, environment, style block, negative block.\n"
                    "4. THE IMAGE PROMPTS: the actual prompt for every keyframe this episode needs, using "
                    "the template, with canonical blocks verbatim and the right plates named as "
                    "references.\n"
                    "5. THE VIDEO PROMPT TEMPLATE: the reusable structure per engine.\n"
                    "6. THE VIDEO PROMPTS: the actual prompt for every shot, in its engine's grammar, with "
                    "its keyframe referenced where applicable. One continuous action each, explicit start "
                    "and end state, speed stated plainly.\n"
                    "7. THE CHAINING MAP: every place one shot's last frame should seed the next shot's "
                    "first frame for continuous action - and every place it should NOT, across a cut or a "
                    "new scene.\n"
                    "8. THE POWER-EFFECT INSERTION: confirm the power-effect phrase from Prompt 13 appears "
                    "verbatim in every prompt where the power is used. This is the most repeated visual in "
                    "the series and must never be paraphrased.\n"
                    "9. THE SELECTION CRITERIA: what makes a clip usable - identity holding against the "
                    "plate for the full duration, no morphing, the action completing, the age reading "
                    "correctly, no artifacts in the portion I need. Note a clip can be unusable overall and "
                    "perfect for two seconds.\n"
                    "10. THE LOGGING: what to record per approved asset so a good result is reproducible "
                    "next episode - prompt, references, seed or ID, shot number, episode number.\n\n"
                    "End by asking me to run one hero shot and one simple shot before the batch, so we "
                    "calibrate the prompts against reality."
                ),
                "pro_tip": (
                    "Item 10's episode number is the field people leave out and then need. A season means "
                    "coming back to these assets weeks later - a log without episode numbers is a log you "
                    "cannot navigate."
                ),
            },
            {
                "title": "Audio: Score, Voice and Sound",
                "desc": (
                    "The layer the video generator never produced - and the one a youth audience notices "
                    "most, because a theme tune is how a series becomes a series."
                ),
                "prompt_text": (
                    "You are a composer and sound designer building the audio for a youth and family "
                    "generated series.\n\n"
                    "My lean, tone and mode: [PASTE FROM PROMPTS 1-2]\n"
                    "My episode template and runtime: [PASTE FROM PROMPT 15]\n"
                    "My episode script and its dialogue: [PASTE ONE EPISODE]\n"
                    "My voice source: [HUMAN PERFORMER, VOICE GENERATOR, OR BOTH]\n\n"
                    "Do the following:\n\n"
                    "1. THE LAYER MAP: every audio layer - voice, ambience per locked location, spot "
                    "effects, the power-effect sound, score, theme, silence - and which tool or method "
                    "produces each. Make clear none of this comes out of the video generator.\n"
                    "2. THE THEME: this is a series, so it needs one. A brief for the main theme - "
                    "instrumentation, tempo, length, and how it works as both a full title version and a "
                    "short sting. For a youth series a theme a kid can hum is a genuine asset.\n"
                    "3. THE POWER SOUND: the single sound the power makes, specified so it is identical "
                    "every episode. Like the visual signature, this must never vary.\n"
                    "4. THE SCORE CUES: per episode, where music enters and stops, and what each cue does. "
                    "Include the deliberate absences.\n"
                    "5. THE VOICE CASTING BRIEF: for each speaking character, age, texture, pace and "
                    "register - usable for a human performer or a voice generator. Note the specific "
                    "difficulty of young voices: a generated child voice is hard to get right and an adult "
                    "performing a child is usually worse. Give me the honest options.\n"
                    "6. THE PERFORMANCE DIRECTION: for each line in this episode, the direction that gets "
                    "it delivered right. Voice generators need this stated rather than implied.\n"
                    "7. THE ROOM MATCH: how to make a clean voice recording sit inside a generated space, "
                    "which differs by mode - cartoon mode wants a cleaner, flatter voice consistent with "
                    "animation convention; cinematic mode needs matched reverb.\n"
                    "8. THE AMBIENCE BEDS: for each locked location, the layered bed plus one sound unique "
                    "to that place. Build these once and reuse all season.\n"
                    "9. THE SWEETENING LIST: 6 small sounds that make generated picture feel physical - "
                    "footsteps, cloth, a breath, a door, a distant street. The cheapest credibility "
                    "available.\n"
                    "10. THE MIX AND LOUDNESS: the relative levels, and a note on delivering audio that "
                    "works on a phone speaker, since that is where a youth audience will hear it.\n\n"
                    "End by asking me whether I can get real human voices for the young characters, "
                    "because that one resource changes more than any other choice in this phase."
                ),
                "pro_tip": (
                    "Item 2 is the series-maker. A theme tune does more to make ten disconnected generated "
                    "episodes feel like one show than any amount of visual consistency work - and it is "
                    "the cheapest thing in this phase."
                ),
            },
            {
                "title": "Assembly and Pacing",
                "desc": (
                    "Cutting each episode - including cutting around whatever the generation left you - "
                    "and building the repeatable episode assembly so episode six is faster than episode "
                    "one."
                ),
                "prompt_text": (
                    "You are an editor assembling episodes of a generated youth and family series. You cut "
                    "around weakness rather than hiding it.\n\n"
                    "My episode shot list and script: [PASTE]\n"
                    "My audio elements: [FROM PROMPT 21]\n"
                    "My episode template and runtime target: [FROM PROMPT 15]\n"
                    "What I actually ended up with, including what failed or is weak: [DESCRIBE]\n\n"
                    "Do the following:\n\n"
                    "1. THE ASSEMBLY ORDER: where to start, and why it is not the episode's running "
                    "order.\n"
                    "2. THE BEST-SECONDS PASS: for each clip, the criteria for finding its strongest "
                    "continuous portion and cutting to that.\n"
                    "3. THE WEAKNESS MAP: for each weak clip I described, which technique applies - "
                    "shorten it, use it as sound only over something else, reframe or crop in, slow it "
                    "down, freeze the last good frame, cover with a reaction, or cut entirely.\n"
                    "4. THE PACING AUDIT for my lean: where a young viewer's attention will drift, with a "
                    "timecode. Note that youth content tolerates faster cutting than adult content and "
                    "punishes slow openings much harder.\n"
                    "5. THE RUNTIME RECONCILIATION: actual runtime against target, and the specific cuts "
                    "to close the gap, ranked least to most painful.\n"
                    "6. THE HOLD DECISIONS: which shots earned a longer hold, and which to cut short.\n"
                    "7. THE SOUND-FIRST PASS: how to lay audio early rather than last, since in this "
                    "workflow sound determines pacing more than picture.\n"
                    "8. THE GRADE AND MATCH PASS: bringing clips generated on different days into one look "
                    "- matching exposure, contrast and colour, then a unifying treatment over everything. "
                    "In cartoon mode this is a consistent colour pass; in cinematic mode a grain and grade. "
                    "Either way one treatment across the whole series hides enormous variance.\n"
                    "9. THE EPISODE ASSEMBLY TEMPLATE: the reusable project structure - where titles, "
                    "theme, recap and end tag sit - so every subsequent episode assembles faster. Build "
                    "this once.\n"
                    "10. THE FRESH-EYES PROTOCOL: what to ask two people who have not seen it, including "
                    "at least one person in my target age band, and the three questions that produce "
                    "useful answers.\n\n"
                    "End by asking me whether the episode is still about what I said it was about, since "
                    "edits change that and it affects the thumbnail and the description."
                ),
                "pro_tip": (
                    "Item 9 pays for itself by episode three. Build the assembly template once - theme in, "
                    "title card, body, end tag - and every later episode drops into a finished shape "
                    "instead of being rebuilt from scratch."
                ),
            },
        ],
    },

    {
        "name": "PHASE 6: PACKAGE AND RELEASE",
        "intro": (
            "Four prompts to finish. The cover you asked for - a cinematic key art poster or an animated "
            "movie poster, routed by your mode - then the title treatment and thumbnails, the "
            "youth-and-family content audit alongside continuity QC, and the release plan."
        ),
        "prompts": [
            {
                "title": "The Cover: Key Art and Movie Poster",
                "desc": (
                    "The prompt that produces your actual cover. Routed by mode: a cinematic key art "
                    "poster, or an animated-movie poster. For a young audience scrolling, this IS the show "
                    "until they click."
                ),
                "prompt_text": (
                    "You are a key art designer who makes posters for youth and family film and series, "
                    "and who also writes generation prompts to produce them.\n\n"
                    "My mode and register: [PASTE FROM PROMPT 2]\n"
                    "My lean: [FROM PROMPT 1]\n"
                    "My series title: [FROM PROMPT 4 ITEM 10]\n"
                    "My hero, villain and crew with their designs, colours and silhouettes: [PASTE FROM "
                    "PROMPTS 5-7 AND 9]\n"
                    "My style block and negative block: [PASTE FROM PROMPT 10]\n"
                    "My power's visual signature: [FROM PROMPT 3 ITEM 6]\n"
                    "My approved plates: [LIST THEM]\n\n"
                    "PART A - THE DESIGN:\n"
                    "1. THE POSTER TYPE, ROUTED BY MODE: if CINEMATIC, design live-action key art - the "
                    "conventions are a dominant figure or group, dramatic light, a defined depth, a "
                    "photographic grade, and space reserved for the title and billing. If CARTOON, design "
                    "an animated movie poster - the conventions are a character group with clear "
                    "silhouettes and expressions, saturated colour, a legible background that establishes "
                    "the world, and bold title space. Say which you are making and describe its layout.\n"
                    "2. THE COMPOSITION: 4 layout options, each named and described - the hero portrait, "
                    "the ensemble group, the world-establishing wide with figures small, the "
                    "action-moment. For each, what it promises a viewer and which suits my lean.\n"
                    "3. THE AGE SIGNAL: the specific visual choices that tell a scroller this is for their "
                    "age band - and the ones that would misfire by reading too young or too adult. This "
                    "matters more than anything else on the poster.\n"
                    "4. THE TONE SIGNAL: what tells a viewer whether this is funny, exciting or serious. "
                    "Youth and family posters usually need to promise both fun and stakes.\n"
                    "5. THE THUMBNAIL TEST: describe how this poster reads at the size of a phone "
                    "thumbnail. Then simplify the design until it survives that - the silhouettes from "
                    "Prompt 9 are what carry it.\n"
                    "6. THE CLICHE FORBID LIST: 6 youth and family poster clichés to avoid, with a "
                    "specific replacement drawn from my own material for each.\n\n"
                    "PART B - THE GENERATION PROMPT:\n"
                    "7. THE POSTER PROMPT: the actual image-generation prompt for my recommended "
                    "composition. It must contain the relevant canonical character blocks verbatim, my "
                    "style block, my negative block, poster-appropriate framing and lighting, deliberate "
                    "empty space for title placement, and an instruction that NO TEXT be generated. State "
                    "the aspect ratio for both a vertical poster and a horizontal platform banner.\n"
                    "8. THE ALTERNATIVES: prompts for two other compositions so I can compare.\n"
                    "9. THE REFERENCE INSTRUCTION: which approved plates to supply alongside, and how.\n"
                    "10. THE NO-TEXT RULE: state plainly that all text - title, credits, taglines, age "
                    "rating - is added in post, never generated. Then describe what to leave room for.\n"
                    "11. THE SELECTION CRITERIA: what makes a poster generation usable - character "
                    "identity matching the plates, silhouette clarity, composition holding at thumbnail, "
                    "clean space for text, no invented text or logos.\n"
                    "12. THE VARIANT SET: the other sizes and crops I will need - vertical poster, "
                    "horizontal banner, square, and a character-alone variant per lead for social use.\n\n"
                    "End by asking me whether the poster promises the show I actually made, because a "
                    "cover that oversells is the fastest way to lose a young audience in episode one."
                ),
                "pro_tip": (
                    "Item 5 decides whether this works. Shrink your poster to the size of a stamp and look "
                    "at it - if you cannot tell who the characters are or what kind of show it is, the "
                    "design is too busy, and no amount of detail will help at the size it will actually be "
                    "seen."
                ),
            },
            {
                "title": "Title Treatment, Logo and Thumbnails",
                "desc": (
                    "Everything text-shaped, added in post where it belongs - the series logo, the title "
                    "card, the episode thumbnails and the end tag."
                ),
                "prompt_text": (
                    "You are a title designer and packaging specialist for youth and family series.\n\n"
                    "My title: [FROM PROMPT 4 ITEM 10]\n"
                    "My mode, style block and palette: [PASTE FROM PROMPTS 2 AND 10]\n"
                    "My poster and its empty space: [PASTE FROM PROMPT 23]\n"
                    "My lean: [FROM PROMPT 1]\n"
                    "My episode grid: [FROM PROMPT 14]\n\n"
                    "Do the following:\n\n"
                    "1. THE LOGO BRIEF: a design brief for the series title treatment - letterform "
                    "character, weight, whether it has an effect or a device, how it sits with my palette, "
                    "and how it works in one colour. Keep it simple: youth series logos need to be legible "
                    "at thumbnail size and reproducible on merchandise, not clever.\n"
                    "2. THE FOUR DIRECTIONS: four distinct logo directions, described, with what each "
                    "signals about tone and age.\n"
                    "3. THE LEGIBILITY RULES: the constraints - minimum size, contrast against my poster, "
                    "how it behaves on light and dark, and what happens when it is 40 pixels wide.\n"
                    "4. THE TITLE CARD: how the title appears in the episode itself, how long it holds, "
                    "over picture or black, and whether it has a sound. Scale this to my episode length - "
                    "a 3-minute episode can afford about two seconds.\n"
                    "5. THE EPISODE TITLE CARDS: whether episodes have on-screen titles, and if so the "
                    "format. Note that for a youth series, episode titles a kid would read aloud are worth "
                    "having.\n"
                    "6. THE THUMBNAIL SYSTEM: a repeatable thumbnail design for every episode - what stays "
                    "constant so the series is recognisable in a list, and what changes per episode. Then "
                    "which frame from each episode to use, and the rules for picking one.\n"
                    "7. THE THUMBNAIL TEXT RULE: whether to put text on thumbnails for my platform and "
                    "lean, and how much. Be specific about size and placement.\n"
                    "8. THE END TAG: what appears at the end of each episode - a next-episode prompt, a "
                    "credit, a logo sting - and how long it lasts.\n"
                    "9. THE CREDITS: what a generated series should credit, in what order, including how "
                    "to credit AI tools honestly and human collaborators properly.\n"
                    "10. THE AI DISCLOSURE: how to state the use of generative tools clearly and without "
                    "embarrassment, in the credits and in platform descriptions. Note that some platforms "
                    "now require disclosure and that requirements change, so check current rules rather "
                    "than assuming.\n"
                    "11. THE ASSET CHECKLIST: everything text-shaped I need to produce in post, in one "
                    "list, so nothing gets asked of a video generator.\n\n"
                    "End by asking me whether my title is one a ten-year-old would say out loud, because "
                    "that is how a youth series actually spreads."
                ),
                "pro_tip": (
                    "Item 6 is the underrated one. A thumbnail system with a constant element - a colour "
                    "bar, a logo corner, a consistent frame treatment - makes a list of ten episodes read "
                    "as a show instead of ten unrelated videos."
                ),
            },
            {
                "title": "The Youth-and-Family Audit and Continuity QC",
                "desc": (
                    "Two audits in one pass, because they are the two things that sink a generated youth "
                    "series: content that drifted out of band, and a cast that stopped looking like itself."
                ),
                "prompt_text": (
                    "You are a standards editor and continuity supervisor reviewing a finished episode of "
                    "a youth and family generated series. You look for what the maker can no longer see.\n\n"
                    "My lean, content gates and hope floor: [PASTE FROM PROMPT 1]\n"
                    "My level spec: [PASTE THE LEVEL SPEC FROM THIS PACK'S CHEAT SHEET]\n"
                    "My canonical blocks and plates: [PASTE FROM PROMPTS 9 AND 11-13]\n"
                    "My power's hard limits: [FROM PROMPT 3]\n"
                    "My adult limit: [FROM PROMPT 8 ITEM 7]\n"
                    "My episode: [DESCRIBE IT SHOT BY SHOT, OR PASTE THE EDIT LIST AND CONTINUITY LOG]\n\n"
                    "PART A - YOUTH AND FAMILY STANDARDS. Cite the timecode for each:\n"
                    "1. CONTENT DRIFT: anything outside my lean's gates - peril, injury, cruelty, grief, "
                    "language, romance, frightening imagery without resolution.\n"
                    "2. THE HOPE FLOOR: any point the episode dips below it, and how long before relief "
                    "arrives.\n"
                    "3. THE AGENCY CHECK: every place an adult solves the problem instead of the young "
                    "characters. The most important check in this audit.\n"
                    "4. THE ADULT-LIMIT CHECK: any place the grown-ups should obviously have intervened "
                    "and conveniently did not, against my stated reason from Prompt 8.\n"
                    "5. THE CONDESCENSION SWEEP: explained jokes, stated morals, a character voicing the "
                    "theme, a narrator telling the viewer how to feel.\n"
                    "6. THE AGE READ: whether the characters look and sound their stated ages throughout.\n"
                    "7. THE CREW USEFULNESS: any crew member who became a passenger.\n"
                    "\n"
                    "PART B - CONTINUITY AND CRAFT:\n"
                    "8. IDENTITY DRIFT: every shot where a character does not match their plate - face, "
                    "age, build, hair, costume, silhouette. Rank by how noticeable each is in context.\n"
                    "9. THE POWER-EFFECT CONSISTENCY: every shot where the power looks different from its "
                    "locked description. In a superhero series this is the most visible failure of all.\n"
                    "10. SPACE DRIFT: locations contradicting their established geography, and cuts that "
                    "flip screen direction.\n"
                    "11. MODE CONSISTENCY: any shot drifting toward the other mode - stylisation in a "
                    "cinematic episode, photorealism in a cartoon one.\n"
                    "12. ARTIFACT SWEEP: hands, extra or missing limbs, morphing between frames, unstable "
                    "backgrounds, physics that does not hold, text resolved into nonsense.\n"
                    "13. THE SERIES CHECK: compare this episode against the previous ones. Has the look, "
                    "the cast or the power quietly drifted across episodes? This is the check a single-film "
                    "workflow never needs.\n"
                    "14. AUDIO QC: levels, dialogue intelligibility, ambience continuity across cuts, the "
                    "power sound matching, and whether the mix holds on a phone speaker.\n"
                    "15. THE COMPREHENSION CHECK: 6 questions a first-time viewer of my lean would have. "
                    "Any the episode does not intend to leave open is a problem.\n"
                    "16. THE TRIAGE: split every finding into must-fix, should-fix-if-cheap, and "
                    "accept-and-move-on. Be realistic - a generated series with zero artifacts does not "
                    "exist, and chasing them all is how series never ship.\n\n"
                    "End by asking me what my remaining budget and time are, so the triage is honest."
                ),
                "pro_tip": (
                    "Item 13 is the check unique to series work and the one that catches the killer. Look "
                    "at episode one and your newest episode side by side every single time - drift happens "
                    "so gradually that you will not see it any other way."
                ),
            },
            {
                "title": "Release, Platform and Season Two",
                "desc": (
                    "Where this goes, how a youth audience finds it, and what season two does - plus an "
                    "honest read on how generated youth content is currently received."
                ),
                "prompt_text": (
                    "You are a distribution strategist for youth and family content with specific "
                    "knowledge of how AI-generated work and children's content are currently treated. You "
                    "are realistic rather than encouraging.\n\n"
                    "My series, lean, mode and episode format: [PASTE FROM PROMPTS 1-2]\n"
                    "My season and what I actually finished: [FROM PROMPTS 14 AND 18]\n"
                    "My packaging: [FROM PROMPTS 23-24]\n"
                    "What I want this to do: [STATE IT]\n\n"
                    "Do the following:\n\n"
                    "1. THE HONEST ASSESSMENT: what this series can realistically achieve. Include a "
                    "straight answer on how AI-generated content is currently received, and separately on "
                    "how platforms treat content made for children - which is a heavily regulated and "
                    "policy-sensitive area with its own rules about data, advertising, comments and "
                    "labelling. Tell me to read each platform's current children's-content policy rather "
                    "than assuming, because these change and getting them wrong has real consequences.\n"
                    "2. THE PLATFORM DECISION: recommend a primary home given my episode length, lean and "
                    "mode, and explain the trade-offs. Cover the difference between a made-for-kids "
                    "designation and general audiences, and what each does to reach, comments and "
                    "monetisation.\n"
                    "3. THE DISCOVERY REALITY: how a youth audience actually finds a new series, and what "
                    "that means for my title, thumbnail, first fifteen seconds and episode length.\n"
                    "4. THE RELEASE PATTERN: all at once, weekly, or a pilot followed by a run. Recommend "
                    "one for my situation and say why.\n"
                    "5. THE VERTICAL CUT-DOWN: whether this series has short-form vertical versions in it - "
                    "which 30-60 seconds per episode, recut for a phone, with what changes to framing, "
                    "pacing and sound. For a youth audience this is often where the show is actually "
                    "found.\n"
                    "6. THE PARENT-FACING MATERIALS: what an adult needs to see to let their kid watch - a "
                    "clear age indication, an honest content note, and a description that says what the "
                    "show is about rather than selling it.\n"
                    "7. THE SAFETY AND COMMENTS QUESTION: the considerations around audience interaction "
                    "on content aimed at young viewers, and the conservative default.\n"
                    "8. THE CRITICISM PREPARATION: the objections this will attract - both about AI "
                    "generation and about content for children - with an honest, non-defensive answer to "
                    "each. Decide these now rather than in a comment thread.\n"
                    "9. SEASON TWO: a one-page premise. The new pressure, the returning cost from season "
                    "one, the escalation that is not raw power, and a hook in the first episode. It must "
                    "not undo season one's ending.\n"
                    "10. THE POWER-CREEP CONTRACT: state in writing what the power will and will not "
                    "become across seasons, and the five things to escalate instead.\n"
                    "11. THE ASSET CARRY-FORWARD: what to archive so season two can match season one - "
                    "plates, blocks, logs, style block, project templates, audio beds. Give me a folder "
                    "structure.\n"
                    "12. THE NEXT-SERIES LESSON: based on what this taught me, what to do differently next "
                    "time, technically and dramatically.\n\n"
                    "End by asking me whether I would let a child I know watch this, because for this "
                    "audience that is the only test that matters."
                ),
                "pro_tip": (
                    "Item 1's children's-content warning is the one to act on rather than skim. Platform "
                    "rules for content aimed at young viewers are strict, specific and enforced - read the "
                    "current policy for your platform before you upload, not after."
                ),
            },
        ],
    },
]
