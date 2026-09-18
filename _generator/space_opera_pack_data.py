# -*- coding: utf-8 -*-
"""
Royalti Studios - Space Opera Master Prompt Pack (Adult Fiction Line).

Build with:
    python pack_builder.py space_opera_pack_data \
        "Space_Opera_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "SPACE OPERA",
    "total_prompts": 22,
    "hook_line": "Empires, fleets and a thousand worlds - and one crew small enough to slip between them and change everything.",
    "keyword_lines": [
        "Star empires • Found family crews • Fleet battles • First contact • Succession • Rebellion",
        "Jump drives • Generation ships • Alien civilisations • Dynasties • Long wars • Impossible odds",
    ],
    "subgenres_line": "Subgenres: Military Space Opera, Crew/Found-Family Adventure, Political & Dynastic, New Space Opera (hard-leaning), Planetary Romance, First Contact Epic, Post-Human & Ascension, Space Western",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-09",
    "audience_line": "Adult Fiction Line",
    "cover_h2": "From Galactic Concept to Published Novel",
    "closing_tagline": "The galaxy is the stage. The book is about the people small enough to be crushed by it - and who are not.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "Space opera is the genre of enormous stakes told through people you would follow anywhere. It fails "
        "in two directions: too small, and it is a ship story with a galaxy painted behind it; too large, and "
        "it is a history book nobody cries at. This pack keeps both ends honest. You will build travel rules "
        "that generate politics, factions with real economies, a cast whose personal wants are wired into the "
        "galactic ones, and a structure that can carry a war without losing a crew. Work the prompts in "
        "order, save every output in one document, and by Prompt 22 that document is your series bible - "
        "which this genre will absolutely require of you."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-3) - Set the scale. Find the operatic premise, calibrate the distance between "
        "the intimate and the galactic, and lock your reader promise and shelf position.",
        "Phase 2 (Prompts 4-8) - Build the galaxy. Travel rules as political geography, the great powers and "
        "their economies, species and cultures, the technology of war and trade, and the deep history that "
        "everyone is still arguing about.",
        "Phase 3 (Prompts 9-12) - Forge the cast. A protagonist standing at a hinge of history, the crew or "
        "command ensemble, the antagonist power with a legitimate claim, and the loyalty web that will be "
        "tested by orders.",
        "Phase 4 (Prompts 13-16) - Architect the story. The incident that starts the war, the full beat "
        "sheet, a set-piece and fleet-battle generator, and a system for braiding multiple point-of-view "
        "threads without losing the reader.",
        "Phase 5 (Prompts 17-19) - Write the book. Chapter outline with hooks, an opening that establishes "
        "scale through one person, and a batch-drafting engine that holds voice, scale and continuity.",
        "Phase 6 (Prompts 20-22) - Polish, publish, expand. A scale and continuity audit, a wonder-and-voice "
        "pass, and the blurb, metadata and multi-book series architecture kit.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool and a place to save your outputs between prompts. Brackets like "
        "[THIS] are placeholders - replace them with your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular. Writing a single-ship found-family adventure? "
        "Prompt 15's fleet-battle section becomes a boarding-action section, and Prompt 16 is a light pass. "
        "Writing dynastic political opera with one viewpoint? Prompt 16 becomes a court-intrigue thread map."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "Galactic stakes felt through one specific person's want - the war matters because she does",
            "Travel rules that create political geography: what is close, what is unreachable, what a message costs in time",
            "Factions with economies, succession problems and internal politics, not costumes and flags",
            "A crew or command group with real interdependence, competence and unresolved history",
            "Wonder delivered as physical experience - the size of the thing, the sound of it, what it does to a human body",
            "An antagonist power whose claim is legitimate enough that a reasonable person could serve it",
            "Consequences that scale: a decision on a bridge that shows up as a burnt city three chapters later",
            "Alien cultures built from a different premise about life, not humans with foreheads and a proper noun",
            "A war whose logistics exist - fuel, yards, crews, supply lines, casualty replacement",
            "An ending that resolves the personal story completely, even when the galactic one continues",
        ],
        "kills": [
            "Infodump chapters where a character explains the political situation to someone who lives in it",
            "A galaxy of one-note planets: the desert planet, the ice planet, the trade planet",
            "Fleet battles with no geometry, no logistics and no cost - ships as counters rather than places",
            "Aliens who are humans with a single exaggerated trait and no material culture",
            "A protagonist who happens to be present at every historically significant event",
            "Stakes inflation, where each act must threaten more worlds until the reader stops feeling any of it",
            "Faster-than-light rules that change whenever the plot needs someone to arrive on time",
            "Empires with no economy - no taxation, no food, no shipyards, no reason anyone obeys",
            "Named characters dying in job lots to signal seriousness, with no one grieving anyone",
            "A finale resolved by a superweapon or a single unrepeatable technology nobody thought to use earlier",
        ],
        "voice": [
            "Ground the enormous in the bodily - acceleration, cold, recycled air, the smell of a hangar deck",
            "Scale by comparison, not by numbers - one image the reader can hold beats six digits",
            "Competence register: professionals speak in procedure and shorthand, and the reader keeps up",
            "Let awe be rare; three genuinely astonishing moments outperform constant grandeur",
            "Distinct faction voices - court speech, service jargon, spacer creole, alien syntax",
            "Interiority under command pressure: what it costs to give an order, and who the character is not saying it to",
            "Concrete logistics in dialogue - fuel states, transit times, casualty numbers spoken plainly",
            "Keep sentences short in vacuum and combat; open them up planetside and in council chambers",
        ],
        "formula": (
            "The Small Life (we meet the protagonist inside a specific, ordinary duty) -> The Incident "
            "(something happens that the great powers cannot ignore) -> Conscription (they are pulled into "
            "the machine, willing or not) -> The Crew or Command Forms -> First Engagement (the cost of this "
            "war made physical) -> The Wider Picture (the reader learns what is really being fought over) -> "
            "The Order That Cannot Be Obeyed -> Betrayal or Political Reversal -> Catastrophic Loss (a world, "
            "a fleet, a friend) -> The Hinge (a choice only this person can make) -> The Decisive Engagement "
            "on the Enemy's Terms -> A Settled Personal Story, an Unsettled Galaxy -> The Cost, Counted"
        ),
        "reader_expectations": (
            "Space opera readers want two things at once and will not accept either alone: the awe of scale "
            "and the intimacy of a crew they would follow into a sequel. They expect the politics to hold up "
            "under thought - factions that want things for reasons, wars with supply lines, travel rules that "
            "stay fixed - and they expect at least three moments of genuine wonder. They will tolerate a large "
            "cast if every viewpoint is distinct and earns its pages. They will not forgive stakes inflation, "
            "a superweapon ending, or a galaxy where nobody eats. Above all they expect the personal story to "
            "land: the war can continue past the last page, but the character's question must be answered."
        ),
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "Space opera is the only genre that asks you to hold a galaxy and a single face in the same sentence. "
        "Every technique in this pack exists to serve that one trick. The travel rules from Prompt 4 are there "
        "so distance can hurt someone. The faction economies from Prompt 5 are there so a supply decision can "
        "starve a character you love. The wonder discipline in Prompt 21 is there so the astonishing moments "
        "still astonish on page four hundred. When a chapter feels weightless, the fault is almost always the "
        "same: the galactic event has drifted loose from the person it should be happening to. Tie it back to "
        "one body in one room and the scale returns. Now go finish the book - the fleets are waiting, and so "
        "is the person they are going to cost."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: SET THE SCALE",
        "intro": (
            "Space opera lives or dies on the distance between the biggest thing in your book and the "
            "smallest. These three prompts find your operatic premise, calibrate that distance deliberately, "
            "and turn both into a market position you can steer by."
        ),
        "prompts": [
            {
                "title": "The Operatic Premise",
                "desc": (
                    "This genre needs a premise big enough to justify a galaxy and specific enough to fit in "
                    "one person's hands. This prompt finds both halves and welds them together."
                ),
                "prompt_text": (
                    "You are a developmental editor who has worked on space opera and epic science fiction "
                    "for twenty years.\n\n"
                    "My rough idea is: [DESCRIBE IN 2-4 SENTENCES - a situation, an image, a ship, a war, "
                    "whatever I have]\n\n"
                    "Do the following:\n\n"
                    "1. THE GALACTIC QUESTION: name the large-scale question my book is really about - "
                    "succession, secession, first contact, resource control, an ideology, a returning threat, "
                    "the ethics of a technology. State it in one sentence.\n"
                    "2. THE PERSONAL QUESTION: name the intimate question that will carry it - belonging, "
                    "loyalty versus conscience, revenge, duty versus love, the price of command, whether one "
                    "person's life matters at this scale. One sentence.\n"
                    "3. THE WELD: describe in a paragraph how these two questions are the same question seen "
                    "at different magnifications. If they are not, tell me plainly and offer me two personal "
                    "questions that would weld properly to my galactic one.\n"
                    "4. THE HINGE: identify the moment where one specific person's decision changes the "
                    "galactic outcome, and give me a plausible reason they are the one standing there - "
                    "position, access, knowledge, or accident. Never 'chosen'.\n"
                    "5. THE OPENING IMAGE AND THE CLOSING IMAGE: propose both, and show me how the second "
                    "answers the first.\n"
                    "6. THE CHEAP VERSION: describe the generic version of my idea so I know exactly what to "
                    "avoid.\n\n"
                    "End by asking me which of the two questions I care about more, because that answer "
                    "decides whether this is a war story with a heart or a character story with a war in it."
                ),
                "pro_tip": (
                    "If your hinge requires your protagonist to be uniquely special, replace it with a hinge "
                    "that requires them to be uniquely placed. Position is more believable than destiny and "
                    "produces better plots."
                ),
            },
            {
                "title": "Scale Calibration",
                "desc": (
                    "How wide is your galaxy, how many viewpoints, how long a timespan? This prompt sets those "
                    "dials on purpose instead of letting them drift upward during drafting."
                ),
                "prompt_text": (
                    "You are a structural editor specialising in large-canvas science fiction.\n\n"
                    "My galactic and personal questions: [PASTE FROM PROMPT 1]\n"
                    "Target length: [E.G. 120,000 WORDS] and planned series length: [E.G. TRILOGY]\n\n"
                    "Calibrate my scale:\n\n"
                    "1. THE CANVAS: how many inhabited systems does my story actually need? Give me a number "
                    "and a justification. Then name the 5-7 locations that will carry the whole book, because "
                    "readers remember places they revisit.\n"
                    "2. THE VIEWPOINT COUNT: recommend a number of point-of-view characters for my length and "
                    "premise, with the trade-offs. Warn me about the specific failure mode of the count I am "
                    "probably tempted by.\n"
                    "3. THE TIMESPAN: over what period does book one take place - weeks, months, years? Tell "
                    "me what each choice does to the emotional continuity of a crew.\n"
                    "4. THE SUBGENRE PLACEMENT: name my primary subgenre and two secondaries from: military "
                    "space opera, crew/found-family adventure, political and dynastic, new space opera "
                    "(hard-leaning), planetary romance, first contact epic, post-human and ascension, space "
                    "western. Justify each.\n"
                    "5. THE RIGOUR DIAL: from 1 to 10, how much physics does my book owe the reader? Say what "
                    "my chosen number obligates me to handle carefully and what it lets me wave past.\n"
                    "6. THE STAKES CEILING: state now, in one sentence, the largest thing that will ever be "
                    "threatened in this series - and commit to it, so I never have to inflate past it.\n\n"
                    "End by asking me which single location I want the reader to feel homesick for, because "
                    "that place needs to appear in the first three chapters."
                ),
                "pro_tip": (
                    "Setting the stakes ceiling early is the most valuable thing in this prompt. Books that "
                    "escalate to 'the whole galaxy' by act two have nowhere to go, and readers stop feeling "
                    "anything the moment the numbers exceed imagination."
                ),
            },
            {
                "title": "Reader Promise & Shelf Position",
                "desc": (
                    "This prompt turns premise and scale into a market stance - who it is for, what it "
                    "promises, and which promises are load-bearing."
                ),
                "prompt_text": (
                    "You are a publishing strategist positioning science fiction for adult readers.\n\n"
                    "My premise: [PASTE FROM PROMPT 1]\n"
                    "My scale calibration and subgenres: [PASTE FROM PROMPT 2]\n\n"
                    "Do the following:\n\n"
                    "1. Write my READER PROMISE in one paragraph, in the second person ('You will feel...').\n"
                    "2. Identify the 3 reader appeals I am leading with, from: found family, military "
                    "competence and tactics, political intrigue, sense of wonder and exploration, first "
                    "contact and xenology, romance across a divide, revenge, big ideas about consciousness or "
                    "civilisation.\n"
                    "3. Write 3 one-line pitches in different registers: one epic and sweeping, one that "
                    "leads with the crew, one that leads with the central moral problem.\n"
                    "4. Name my ideal reader in a paragraph - what they have read recently, and what they are "
                    "hungry for that the market underserves.\n"
                    "5. List the 4 promises I must NOT break, and write the one-star review each breach would "
                    "generate in the reviewer's own words.\n"
                    "6. Tell me which element of my concept is most commercially distinctive, and how to get "
                    "it onto the page within the first three chapters.\n\n"
                    "End by asking me which pitch sounds most like the book I actually want to write, since "
                    "that governs how much page time goes to war versus to people."
                ),
                "pro_tip": (
                    "In this genre the crew pitch almost always outsells the epic pitch. Readers commit to "
                    "people and stay for empires - write the sweeping version for your own clarity and lead "
                    "with the human one everywhere it counts."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: BUILD THE GALAXY",
        "intro": (
            "Space opera worldbuilding is not decoration - it is the source of your plot. Travel rules make "
            "political geography. Economies make wars. History makes grievance. These five prompts build a "
            "galaxy that generates conflict on its own, so you never have to force one."
        ),
        "prompts": [
            {
                "title": "Travel Rules as Political Geography",
                "desc": (
                    "How people cross space determines who rules whom, what a message costs, and where power "
                    "concentrates. This prompt sets the rules once, permanently, and derives your map's "
                    "politics from them."
                ),
                "prompt_text": (
                    "You are a worldbuilding consultant who designs travel systems for science fiction and "
                    "then derives their political consequences.\n\n"
                    "My rigour dial and canvas size: [PASTE FROM PROMPT 2]\n"
                    "My premise: [FROM PROMPT 1]\n\n"
                    "Build my TRAVEL SYSTEM:\n\n"
                    "1. THE MECHANISM: how ships cross interstellar distance. Describe it in plain language "
                    "in four sentences. Choose a system that suits my rigour dial - jump points, warp, "
                    "relativistic slower-than-light, gates, or something else.\n"
                    "2. THE CONSTRAINTS: state 5 hard rules I can never break - what it costs, how long it "
                    "takes, what it requires, where it cannot be done, and what it does to the people aboard. "
                    "Write them as rules, not as flavour.\n"
                    "3. COMMUNICATION: how fast does information travel compared to ships? This single answer "
                    "determines whether my galaxy has central authority or de facto independence. Spell out "
                    "the political consequence explicitly.\n"
                    "4. THE CHOKEPOINTS: given the mechanism, which systems are strategically decisive and "
                    "why? Name 4 and describe who holds each one now.\n"
                    "5. THE FRONTIER: where does control genuinely stop, and what lives past it?\n"
                    "6. THE TRAVEL EXPERIENCE: what a transit actually feels like for a passenger - duration, "
                    "sensation, danger, boredom, ritual. Give me one paragraph I could adapt into prose.\n"
                    "7. THE MAP CONSEQUENCE: summarise in a paragraph how these rules shape who can rule "
                    "whom, where rebellion is feasible, and why the war in my book is fought where it is.\n\n"
                    "End by asking me whether any faction has a travel advantage the others do not, because "
                    "that asymmetry is worth an entire trilogy."
                ),
                "pro_tip": (
                    "Item 3 is the most consequential decision in your whole galaxy. Messages slower than "
                    "ships gives you feudal governors and honest miscommunication; messages faster gives you "
                    "surveillance, central command and a very different kind of story."
                ),
            },
            {
                "title": "Powers, Factions and Their Economies",
                "desc": (
                    "Empires need food, fuel, shipyards and a reason people obey. This prompt builds your "
                    "great powers as functioning entities with pressures your plot can exploit."
                ),
                "prompt_text": (
                    "You are a political economist consulting on interstellar polities.\n\n"
                    "My travel rules and their political consequences: [PASTE FROM PROMPT 4]\n"
                    "My galactic question: [FROM PROMPT 1]\n\n"
                    "Build my POWERS:\n\n"
                    "1. THE MAJORS: 3-4 great powers. For each - name, form of government, how it legitimises "
                    "itself, its core economic base, its military doctrine, and the internal problem it is "
                    "currently managing badly.\n"
                    "2. THE MINORS: 3 smaller entities that matter - a corporate concern, a religious order, "
                    "a trade league, an independent world, a nomad fleet, a criminal syndicate. What each one "
                    "controls that the majors need.\n"
                    "3. THE ECONOMY: what actually moves between systems given my travel constraints, and "
                    "what does not because it is uneconomic to ship. Name the 3 commodities worth fighting "
                    "over and why.\n"
                    "4. WHO EATS: how each major power feeds itself, and what happens to a system whose supply "
                    "line is cut. This is where sieges and blockades get their teeth.\n"
                    "5. THE SUCCESSION PROBLEM: for the power most central to my plot, describe how authority "
                    "transfers and what is currently going wrong with that process.\n"
                    "6. THE FLASHPOINT: the current dispute between two powers - what it is over, who is "
                    "escalating, and what each side would accept. My plot lives here.\n"
                    "7. THE FACTION VOICES: for each major, 3 phrases and one piece of etiquette that "
                    "identifies a citizen instantly in dialogue.\n\n"
                    "End by asking me which power my protagonist was born under, and whether they still "
                    "believe in it."
                ),
                "pro_tip": (
                    "Give every power a genuine virtue and a genuine crime. Readers who can construct an "
                    "argument for the enemy will argue about your book online for years, which is the best "
                    "marketing there is."
                ),
            },
            {
                "title": "Species, Cultures and Xenology",
                "desc": (
                    "Aliens built from a different premise about life are the genre's greatest pleasure. This "
                    "prompt builds yours from biology upward, or builds divergent human cultures if your book "
                    "has no aliens."
                ),
                "prompt_text": (
                    "You are a xenologist and cultural anthropologist consulting on science fiction. If my "
                    "book has no non-human species, apply every step below to divergent human cultures shaped "
                    "by centuries of separation instead.\n\n"
                    "My galaxy and powers: [PASTE FROM PROMPTS 4-5]\n"
                    "My premise: [FROM PROMPT 1]\n\n"
                    "Build my PEOPLES. For each of 2-3 species or cultures:\n\n"
                    "1. THE PREMISE: the single biological, environmental or historical fact everything else "
                    "follows from - how they reproduce, how they sense the world, how long they live, what "
                    "their homeworld demanded of them.\n"
                    "2. THE CONSEQUENCES: 6 downstream traits - social structure, attitude to death, concept "
                    "of property, family arrangement, art, what they find disgusting - each traceable to the "
                    "premise in item 1.\n"
                    "3. THE MATERIAL CULTURE: what their ships, buildings, clothing and tools look like and "
                    "why, given their bodies and their premise.\n"
                    "4. THE MISUNDERSTANDING: the specific thing humans consistently get wrong about them, "
                    "and the thing they consistently get wrong about humans. Both should be plot-usable.\n"
                    "5. THE LANGUAGE SHAPE: how their speech works differently - tense, register, evidential "
                    "markers, silence, scent, whatever fits - and how I render that in English without "
                    "resorting to broken grammar.\n"
                    "6. THE INTERNAL DIVERSITY: 3 factions or subcultures within them, so they are never a "
                    "monolith.\n"
                    "7. ONE SCENE SEED: a situation where their premise creates conflict with my protagonist "
                    "that neither party is being unreasonable about.\n\n"
                    "End by asking me which of these peoples my protagonist has a personal history with, so "
                    "the xenology can arrive as relationship rather than as lecture."
                ),
                "pro_tip": (
                    "Item 4 is where your best scenes come from. Mutual, sympathetic misunderstanding "
                    "generates more story than hostility ever will, because the reader can see both sides "
                    "being reasonable and heading for a wall."
                ),
            },
            {
                "title": "Ships, War and the Technology of Power",
                "desc": (
                    "This prompt builds the hardware and the doctrine - what ships are, how battles work, what "
                    "war costs, and what technology means politically."
                ),
                "prompt_text": (
                    "You are a military and technology consultant for science fiction, working strictly "
                    "within the travel constraints already established.\n\n"
                    "My travel rules and constraints: [PASTE FROM PROMPT 4]\n"
                    "My powers and their doctrines: [PASTE FROM PROMPT 5]\n"
                    "My rigour dial: [FROM PROMPT 2]\n\n"
                    "Build my MILITARY AND TECHNOLOGICAL LAYER:\n\n"
                    "1. THE SHIP CLASSES: 5 classes from smallest to largest, with crew size, role, endurance, "
                    "and what each one cannot do. Include what it costs and how long it takes to build one.\n"
                    "2. LIFE ABOARD: the daily reality on my protagonist's ship - watches, food, gravity or "
                    "its absence, noise, smell, privacy, what the crew complains about.\n"
                    "3. COMBAT DOCTRINE: how engagements actually work given my travel and communication "
                    "rules - ranges, detection, timescale, what wins. State whether battles are decided in "
                    "seconds or days, because it changes every action scene I write.\n"
                    "4. THE COST OF WAR: casualty rates, how ships are lost, what happens to survivors, "
                    "replacement times for hulls and trained crews, and what a long war does to a society's "
                    "economy.\n"
                    "5. THE FIVE TECHNOLOGIES THAT MATTER: for each - what it does, who has it, what it costs, "
                    "and its political consequence. Include at least one that is uncomfortable rather than "
                    "cool.\n"
                    "6. THE LIMITS: 5 things technology cannot do in my galaxy. This list is what makes my "
                    "plot difficult and therefore possible.\n"
                    "7. THE PERSONAL SCALE: what a single soldier, pilot or spacer carries, wears and relies "
                    "on. Wonder is delivered at this scale, not at fleet scale.\n\n"
                    "End by asking me whether my protagonist has ever been in a real engagement, because a "
                    "veteran and a novice require completely different opening chapters."
                ),
                "pro_tip": (
                    "Decide item 3 before you write a single battle. A genre where engagements take days of "
                    "manoeuvring produces tension and dread; one where they take seconds produces terror and "
                    "aftermath. Mixing them accidentally is the most common structural failure in the genre."
                ),
            },
            {
                "title": "Deep History and the Grievance Map",
                "desc": (
                    "Space opera runs on old wounds. This prompt builds the history everyone is still arguing "
                    "about, the myth that is half-true, and the grievances your plot will detonate."
                ),
                "prompt_text": (
                    "You are a historian consulting on the deep past of a fictional galaxy.\n\n"
                    "My powers and peoples: [PASTE FROM PROMPTS 5-6]\n"
                    "My galactic question: [FROM PROMPT 1]\n\n"
                    "Build my HISTORY:\n\n"
                    "1. THE ERAS: 4 named periods from earliest to present, one paragraph each, ending in the "
                    "present day of my story.\n"
                    "2. THE FOUNDING CRIME: the event at the root of the current order that its beneficiaries "
                    "have reframed as something noble. Give me both the official version and what actually "
                    "happened.\n"
                    "3. THE GRIEVANCE MAP: for each major power and people, what they will not forgive, whom "
                    "they blame, and what they teach their children about it.\n"
                    "4. THE HALF-TRUE MYTH: a widely believed story about the past that is partly accurate. "
                    "Say which part is true, and how my plot can turn on the difference.\n"
                    "5. THE DEEP PAST: is there an older civilisation, a ruin, a precursor, an unexplained "
                    "artefact? If it fits my premise, describe it and state clearly what it is NOT going to "
                    "do, so I never resolve my plot with it.\n"
                    "6. THE LIVING MEMORY: which characters in my story were alive for which events, and what "
                    "that does to how they behave now.\n"
                    "7. THE ANNIVERSARY: a commemoration, holiday or ritual observed differently by different "
                    "powers - an excellent scene setting for confrontation.\n\n"
                    "End by asking me whether the truth about the founding crime gets out during my book, "
                    "because that decision shapes the whole third act."
                ),
                "pro_tip": (
                    "Item 5's second half is a discipline, not a limitation. Precursor technology that can "
                    "solve your climax will always tempt you in draft two - writing down now that it cannot "
                    "is how you protect your ending."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: FORGE THE CAST",
        "intro": (
            "The galaxy is built. Now the people who will make the reader care about it. These four prompts "
            "give you a protagonist standing where history bends, an ensemble with real interdependence, an "
            "antagonist power with a legitimate claim, and the loyalty web that command will eventually break."
        ),
        "prompts": [
            {
                "title": "The Protagonist at the Hinge",
                "desc": (
                    "This prompt builds a protagonist whose personal want is wired directly into the galactic "
                    "question, and who is positioned - not chosen - to matter."
                ),
                "prompt_text": (
                    "You are a character-development editor for epic science fiction.\n\n"
                    "My galactic and personal questions, and my hinge: [PASTE FROM PROMPT 1]\n"
                    "My powers and the flashpoint: [PASTE FROM PROMPT 5]\n"
                    "My rough protagonist idea: [DESCRIBE, or say 'you choose']\n\n"
                    "Build my PROTAGONIST:\n\n"
                    "1. THE BASICS: name, age, origin world, current duty or role, and the exact position "
                    "that places them near the hinge.\n"
                    "2. THE COMPETENCE: what they are professionally excellent at, described precisely enough "
                    "that I can write them working. Readers of this genre come for competence - make it "
                    "specific.\n"
                    "3. THE WANT AND THE NEED: what they are pursuing at the start, and what the book will "
                    "prove they actually need. State how the galactic question forces the gap open.\n"
                    "4. THE LOYALTY: what or whom they serve at the start - a power, a ship, a family, an "
                    "oath, a debt - and the exact conditions under which that loyalty would break.\n"
                    "5. THE PRIVATE COST: what serving has already taken from them, named specifically.\n"
                    "6. THE ARC: 5 stages from their opening loyalty to their final position, each triggered "
                    "by an external event rather than a change of heart. At least one stage must be a step "
                    "backwards.\n"
                    "7. THE THING THEY CANNOT DO: the order they will refuse, the line that defines them. Act "
                    "three will put them on it.\n"
                    "8. THE SMALL LIFE: three ordinary, non-heroic details - a habit, a possession, a private "
                    "pleasure - that will make the scale land when it arrives.\n\n"
                    "End by asking me whether my protagonist survives the series, because in this genre that "
                    "answer changes what I plant in book one."
                ),
                "pro_tip": (
                    "Item 8 does more work than any other. The reader feels a burning world through the "
                    "character's ruined ordinary things - the mug, the letter, the routine. Establish them "
                    "early and cheaply so they can cost you later."
                ),
            },
            {
                "title": "The Crew or Command Ensemble",
                "desc": (
                    "Whether it is a ship's crew, a command staff or a political household, this genre needs a "
                    "group the reader would follow for four books. This prompt builds one with real "
                    "interdependence and unresolved history."
                ),
                "prompt_text": (
                    "You are an ensemble developer for character-driven science fiction.\n\n"
                    "My protagonist: [PASTE FROM PROMPT 9]\n"
                    "My ship classes and life aboard: [PASTE FROM PROMPT 7]\n"
                    "My powers and peoples: [PASTE FROM PROMPTS 5-6]\n\n"
                    "Build my ENSEMBLE of 5-7 characters:\n\n"
                    "1. For each: name, role, origin (which power or people), how long they have served "
                    "together, and the competence they own outright.\n"
                    "2. THE INTERDEPENDENCE: what the group cannot do without each member. If two overlap, "
                    "say so and tell me which to cut or differentiate.\n"
                    "3. THE POSITION: each member's answer to my galactic question. No two identical, and at "
                    "least one should hold a view the reader will find uncomfortable.\n"
                    "4. THE HISTORY: 4 pieces of shared past - a mission that went wrong, a debt, a "
                    "relationship that ended, a promotion someone else deserved - that can surface as "
                    "friction under pressure.\n"
                    "5. THE FRACTURE LINES: for each member, the order or revelation that would make them "
                    "break with the group.\n"
                    "6. THE TEXTURE: for each, one habit, one possession and one thing they say. This is how "
                    "a reader tells seven people apart at speed.\n"
                    "7. THE ROTATION PLAN: which members carry viewpoint chapters (matching the count from "
                    "Prompt 2) and which are seen only from outside, plus the reason for each choice.\n\n"
                    "Then tell me which two deaths would hurt most, and which member I am most likely to "
                    "under-write.\n\n"
                    "End by asking me which crew member disagrees with my protagonist most sharply, because "
                    "that person should get more page time than my instincts will give them."
                ),
                "pro_tip": (
                    "Give the ensemble one running, low-stakes argument - about food, a card game, a "
                    "regulation, a piece of music - that recurs across the book. It is the cheapest way to "
                    "make a reader feel they have lived aboard, and it becomes unbearable to reread after "
                    "someone dies."
                ),
            },
            {
                "title": "The Antagonist Power and Its Legitimate Claim",
                "desc": (
                    "The best space opera antagonists have a case. This prompt builds the opposing power, the "
                    "person who represents it, and the argument the reader will struggle to dismiss."
                ),
                "prompt_text": (
                    "You are an editor who specialises in antagonists that readers argue about.\n\n"
                    "My powers and the flashpoint: [PASTE FROM PROMPT 5]\n"
                    "My grievance map and founding crime: [PASTE FROM PROMPT 8]\n"
                    "My protagonist and their loyalty: [PASTE FROM PROMPT 9]\n\n"
                    "Build my ANTAGONIST LAYER:\n\n"
                    "1. THE OPPOSING POWER: what it wants, in concrete terms, and the historical grievance "
                    "that justifies the want. Two paragraphs.\n"
                    "2. THE LEGITIMATE CLAIM: state the strongest version of their case in 150-200 words. It "
                    "must be strong enough that a decent person could serve them, and it should draw on the "
                    "founding crime from Prompt 8.\n"
                    "3. THE FACE: the individual who embodies the opposition for my protagonist. Name, rank, "
                    "how they rose, what they have sacrificed, how they speak, and what they are genuinely "
                    "good at.\n"
                    "4. THE MIRROR: 3 things this person and my protagonist share, including one my "
                    "protagonist would deny.\n"
                    "5. THE MEANS THEY EXCEED: the specific point where their legitimate claim becomes an "
                    "unjustifiable act. Name it precisely, because that is where the reader's sympathy has to "
                    "break.\n"
                    "6. THE INTERNAL OPPOSITION: someone on their side who thinks they have gone too far, and "
                    "what my protagonist could offer that person.\n"
                    "7. THE THIRD PARTY: a power that benefits from both sides fighting, and what they are "
                    "quietly doing about it.\n\n"
                    "End by asking me whether my antagonist could have been persuaded at any point in the "
                    "book, and if so, who failed to do it."
                ),
                "pro_tip": (
                    "Write the legitimate claim at item 2 before any battle scene. Every tactical decision the "
                    "opposition makes afterwards should be the act of someone who believes it, which turns "
                    "your fleet engagements into arguments rather than fireworks."
                ),
            },
            {
                "title": "Orders, Loyalty and the Relationship Web",
                "desc": (
                    "In this genre, relationships are broken by duty rather than by malice. This prompt maps "
                    "the web and designs the orders that will tear it."
                ),
                "prompt_text": (
                    "You are a plot architect specialising in loyalty, command and moral pressure.\n\n"
                    "My ensemble: [PASTE FROM PROMPT 10]\n"
                    "My protagonist's loyalty and the thing they cannot do: [PASTE FROM PROMPT 9]\n"
                    "My antagonist's claim: [PASTE FROM PROMPT 11]\n\n"
                    "Build my LOYALTY STRUCTURE:\n\n"
                    "1. THE CHAIN: who gives my protagonist orders, who gives them theirs, and where the "
                    "chain becomes political rather than operational.\n"
                    "2. THE WEB: for each significant pair in my cast, one line on the bond and one on what "
                    "would strain it.\n"
                    "3. THE THREE ORDERS: design three orders my protagonist receives across the book, "
                    "escalating in moral difficulty. The first is obeyed with unease, the second is obeyed at "
                    "a cost, the third is the one from Prompt 9 item 7. Give me the tactical justification "
                    "for each, from the issuer's point of view.\n"
                    "4. THE DIVIDED CREW: for the third order, state where each ensemble member stands and "
                    "why, using their positions from Prompt 10.\n"
                    "5. THE ROMANCE OR DEEP BOND: if my book has one, name the pair, what draws them, and the "
                    "duty that stands between them. If not, name the friendship that carries the same weight.\n"
                    "6. THE BETRAYAL: one member acts against the group. Who, when, why it is defensible, and "
                    "the 5 details I can plant beforehand that read innocently first time.\n"
                    "7. THE AFTERMATH OPTIONS: three ways the group can respond to the betrayal, and what "
                    "each choice says about the book's moral position.\n\n"
                    "End by asking me whether my protagonist obeys the third order, because everything in "
                    "Phase 4 is built on that answer."
                ),
                "pro_tip": (
                    "Make the third order tactically correct. An order that is both militarily sound and "
                    "morally intolerable is the single strongest situation this genre can generate - and it "
                    "is ruined the moment you make the issuer a fool."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: ARCHITECT THE STORY",
        "intro": (
            "Now the machine. These four prompts build the incident that pulls your protagonist into "
            "history, the full beat sheet, a generator for the genre's big sequences, and a system for "
            "braiding multiple viewpoints so a large canvas never loses the reader."
        ),
        "prompts": [
            {
                "title": "The Incident and the First Act",
                "desc": (
                    "Space opera begins with a small life interrupted by something the great powers cannot "
                    "ignore. This prompt designs that interruption and builds act one around it."
                ),
                "prompt_text": (
                    "You are a story architect for epic science fiction.\n\n"
                    "My protagonist and their small life: [PASTE FROM PROMPT 9]\n"
                    "My flashpoint: [PASTE FROM PROMPT 5 ITEM 6]\n"
                    "My travel and communication rules: [PASTE FROM PROMPT 4]\n\n"
                    "Build my FIRST ACT:\n\n"
                    "1. THE ORDINARY DUTY: the opening scene - my protagonist doing their job competently, "
                    "with the scale of the galaxy present only as background texture. Two paragraphs.\n"
                    "2. THE INCIDENT: the event that cannot be contained. Give me 4 options at increasing "
                    "scale, then recommend one that fits my stakes ceiling from Prompt 2 without spending it.\n"
                    "3. WHY IT REACHES THEM: the specific reason this event lands on my protagonist rather "
                    "than on anyone else - position, witness, possession, order, accident.\n"
                    "4. THE INFORMATION PROBLEM: given my communication rules, who learns what and when? "
                    "Build at least one act-one complication out of the lag.\n"
                    "5. THE CONSCRIPTION: how my protagonist is pulled in - orders, necessity, revenge, "
                    "obligation - and the moment they can no longer step back.\n"
                    "6. THE ACT ONE BEATS: 10-12 sequential beats from the opening image to the point of no "
                    "return, one sentence each, naming who is present and what changes.\n"
                    "7. THE PROMISE: what act one promises the reader about the shape and scale of what "
                    "follows, stated in one sentence.\n\n"
                    "End by asking me what my protagonist loses in act one from their small life, and whether "
                    "they ever get it back."
                ),
                "pro_tip": (
                    "Spend a full chapter on the ordinary duty before the incident. Readers cannot feel a "
                    "galaxy at risk until they have felt one deck plate under one pair of boots - and the "
                    "chapter you are tempted to cut is the one that makes chapter thirty devastating."
                ),
            },
            {
                "title": "The Full Beat Sheet",
                "desc": (
                    "This prompt maps the whole novel onto the genre's spine, placing every major turn and "
                    "keeping the personal and galactic threads in step."
                ),
                "prompt_text": (
                    "You are a story architect building a complete beat sheet for a space opera novel.\n\n"
                    "My act one: [PASTE FROM PROMPT 13]\n"
                    "My ensemble and the three orders: [PASTE FROM PROMPTS 10 AND 12]\n"
                    "My antagonist and their claim: [PASTE FROM PROMPT 11]\n"
                    "My locations: [FROM PROMPT 2]\n"
                    "Target length: [E.G. 120,000 WORDS]\n\n"
                    "Build my BEAT SHEET across these stations. For each: 2-4 sentences, an approximate "
                    "word-count position, and a note on whether the beat serves the galactic thread, the "
                    "personal thread, or both:\n\n"
                    "1. The Small Life\n"
                    "2. The Incident\n"
                    "3. Conscription / Point of No Return\n"
                    "4. The Crew or Command Forms\n"
                    "5. First Engagement - the cost of this war made physical\n"
                    "6. The Wider Picture - the reader learns what is really being fought over\n"
                    "7. Midpoint: The Second Order, obeyed at a cost\n"
                    "8. Political Reversal - an ally becomes a problem, or a truth from Prompt 8 surfaces\n"
                    "9. The Betrayal from Prompt 12\n"
                    "10. Catastrophic Loss - a world, a fleet, or a member of the ensemble\n"
                    "11. The Third Order - the hinge from Prompt 1\n"
                    "12. The Decisive Engagement, on the enemy's terms\n"
                    "13. A Settled Personal Story, an Unsettled Galaxy\n"
                    "14. The Cost, Counted\n\n"
                    "Then: flag any beat relying on coincidence, any two beats doing the same job, any place "
                    "where the galactic thread runs for more than three beats without a personal one, and any "
                    "point where I exceed the stakes ceiling I set in Prompt 2.\n\n"
                    "End by asking me whether beat 13 answers the personal question from Prompt 1, because if "
                    "it only resolves the war, readers will call the ending hollow."
                ),
                "pro_tip": (
                    "Check the alternation deliberately. The genre's most common structural failure is three "
                    "or four consecutive chapters of fleets and politics with no one to be frightened for - "
                    "and it is always fixable by moving a personal beat, never by adding explanation."
                ),
            },
            {
                "title": "Set-Piece and Fleet-Battle Generator",
                "desc": (
                    "Reusable for every large sequence: fleet actions, boarding actions, sieges, evacuations, "
                    "planetary landings and council confrontations. Built for geometry, cost and consequence."
                ),
                "prompt_text": (
                    "You are a tactical and dramatic choreographer for science fiction set pieces.\n\n"
                    "My combat doctrine and ship classes: [PASTE FROM PROMPT 7]\n"
                    "My travel and communication constraints: [PASTE FROM PROMPT 4]\n"
                    "My ensemble and their roles: [PASTE FROM PROMPT 10]\n"
                    "The sequence I need: [E.G. A FLEET ACTION AT A CHOKEPOINT / A BOARDING ACTION / AN "
                    "EVACUATION UNDER FIRE / A SIEGE OF A STATION / A COUNCIL CONFRONTATION]\n"
                    "Where it sits: [BEAT NUMBER AND CHAPTER FROM PROMPT 14]\n\n"
                    "Design the sequence:\n\n"
                    "1. THE OBJECTIVE: what each side is actually trying to achieve. Not 'win' - a specific, "
                    "losable objective, plus what each will settle for.\n"
                    "2. THE GEOMETRY: the physical situation - distances, timescale, what can be detected and "
                    "when, what the terrain or orbital mechanics do to the options. Work strictly within my "
                    "doctrine from Prompt 7.\n"
                    "3. THE PLAN AND ITS ASSUMPTION: my side's approach, who executes what, and the one "
                    "assumption everything rests on.\n"
                    "4. THE TURN: how the assumption proves wrong, in two stages - a first shock that is "
                    "absorbed, then the real one.\n"
                    "5. THE BEATS: 12-16 sequential beats, one sentence each, with the clock noted every few "
                    "beats - fuel, time to intercept, remaining ordnance, casualties, air, whatever my "
                    "situation runs on.\n"
                    "6. THE HUMAN SCALE: 3 moments inside this sequence experienced by one named person at "
                    "arm's length - what they see, hear, smell and do. These are what the reader remembers, "
                    "not the tactics.\n"
                    "7. THE COST: what is permanently lost - ships, people, a position, a reputation, a "
                    "relationship - and who has to report it to whom afterwards.\n"
                    "8. THE AFTER: the quiet scene that follows and the one line spoken in it that changes a "
                    "relationship.\n\n"
                    "End by asking me whether the objective at item 1 was achieved, because a sequence where "
                    "my side wins the fight and loses the objective is the strongest version of this scene."
                ),
                "pro_tip": (
                    "Write item 6 first. Fleet actions become abstract the moment they leave a body, and "
                    "three grounded arm's-length moments will carry a forty-page engagement that no amount of "
                    "tactical clarity can save."
                ),
            },
            {
                "title": "Braiding the Viewpoints",
                "desc": (
                    "Multiple threads are how space opera covers a galaxy - and how it loses readers. This "
                    "prompt orders your viewpoints, balances their page time, and keeps every thread earning "
                    "its place."
                ),
                "prompt_text": (
                    "You are a structural editor who specialises in multi-viewpoint novels.\n\n"
                    "My viewpoint characters and rotation plan: [PASTE FROM PROMPT 10 ITEM 7]\n"
                    "My beat sheet: [PASTE FROM PROMPT 14]\n"
                    "My locations: [FROM PROMPT 2]\n\n"
                    "Build my BRAID:\n\n"
                    "1. THE THREAD AUDIT: for each viewpoint, state its own arc in one sentence, what "
                    "information only it can deliver, and what the book would lose if I cut it. Recommend "
                    "cutting or merging any thread that fails this test.\n"
                    "2. THE PAGE SHARE: recommend a percentage of the book for each thread, and warn me which "
                    "one I will over-write and which I will neglect.\n"
                    "3. THE INTERLEAVE: propose a chapter-by-chapter viewpoint order for the first quarter, "
                    "and the rule I should follow for the rest - never two consecutive chapters in the same "
                    "thread at high tension, always cut away on a hook, and so on. State my rules explicitly.\n"
                    "4. THE CONVERGENCE POINTS: name the 3 places where threads meet, and what each meeting "
                    "changes. Threads that never meet are a different book.\n"
                    "5. THE INFORMATION LADDER: track what each viewpoint knows that the others do not, and "
                    "mark the two places where the reader knows more than a character - the genre's most "
                    "reliable source of dread.\n"
                    "6. THE ORIENTATION KIT: how each chapter re-establishes viewpoint, place and time within "
                    "its first three lines without a header dump. Give me two sample openings per thread.\n"
                    "7. THE DROPPED THREAD CHECK: identify any thread absent for more than four chapters and "
                    "tell me how to bridge the gap.\n\n"
                    "End by asking me which thread I would cut if my editor demanded 20,000 words gone, "
                    "because knowing that now will make the draft cleaner."
                ),
                "pro_tip": (
                    "Answer the closing question honestly and then consider cutting that thread before you "
                    "draft it. The thread you would sacrifice under pressure is almost always the one you were "
                    "writing out of worldbuilding enthusiasm rather than story need."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 5: WRITE THE BOOK",
        "intro": (
            "Structure becomes prose. These three prompts turn your braid into a chapter plan, draft an "
            "opening that delivers scale through one person, and give you a reusable engine for drafting in "
            "batches while holding voice, viewpoint discipline and galactic continuity steady."
        ),
        "prompts": [
            {
                "title": "Chapter Outline with Hooks",
                "desc": (
                    "This prompt converts your beat sheet and braid into a chapter-by-chapter plan where every "
                    "chapter has a viewpoint, a job, a turn and a hook."
                ),
                "prompt_text": (
                    "You are a novel outliner working in multi-viewpoint science fiction.\n\n"
                    "My beat sheet: [PASTE FROM PROMPT 14]\n"
                    "My braid rules and interleave: [PASTE FROM PROMPT 16]\n"
                    "My set pieces: [LIST THOSE DESIGNED WITH PROMPT 15]\n"
                    "Target: [E.G. 120,000 WORDS IN 55 CHAPTERS OF ABOUT 2,200 WORDS]\n\n"
                    "Build my CHAPTER OUTLINE. For every chapter give me:\n\n"
                    "1. Chapter number and working title.\n"
                    "2. Viewpoint character, location, and elapsed time since that thread's last chapter.\n"
                    "3. The chapter's job in one sentence.\n"
                    "4. The turn: what is true at the end that was not true at the start.\n"
                    "5. Which thread it serves - galactic, personal, or both.\n"
                    "6. The closing hook, as a one-line description.\n\n"
                    "Then flag: any chapter that only conveys information, any three consecutive chapters "
                    "serving only the galactic thread, any thread absent for more than four chapters, any "
                    "chapter where the viewpoint character is a spectator to their own scene, and any place "
                    "two set pieces sit too close together.\n\n"
                    "End by asking me which chapter I am least able to justify, so we can cut or combine it "
                    "before I write 2,200 words I will delete."
                ),
                "pro_tip": (
                    "Watch for the spectator flag. In big-canvas fiction it is easy to write a viewpoint "
                    "character who watches history happen; if they cannot affect the scene, either give them "
                    "agency in it or hand the chapter to someone who has some."
                ),
            },
            {
                "title": "The Opening Chapter",
                "desc": (
                    "This prompt drafts chapter one so that it delivers competence, world and scale through "
                    "one person doing one job - the genre's hardest and most important opening move."
                ),
                "prompt_text": (
                    "You are a novelist drafting the opening chapter of a space opera in the voice described "
                    "below.\n\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET, PLUS NOTES ON "
                    "YOUR OWN STYLE]\n"
                    "My protagonist and their small life: [PASTE FROM PROMPT 9]\n"
                    "Life aboard and the personal scale of technology: [PASTE FROM PROMPT 7 ITEMS 2 AND 7]\n"
                    "My faction voices: [FROM PROMPT 5 ITEM 7]\n"
                    "POV and tense: [SPECIFY]\n"
                    "Target length: [E.G. 2,500-3,000 WORDS]\n\n"
                    "Write chapter one, following these rules:\n\n"
                    "1. Open with my protagonist performing their duty competently, mid-task.\n"
                    "2. Establish their competence by showing them solve one small professional problem.\n"
                    "3. Deliver the physical reality of this world through the body - gravity, air, noise, "
                    "temperature, the feel of the equipment.\n"
                    "4. Let the galaxy exist only as background: a routine mention of distance, a faction "
                    "name, a transit time, a piece of news that is not yet about them.\n"
                    "5. Use faction and service vocabulary in context, explaining nothing.\n"
                    "6. Include the three ordinary details from Prompt 9 item 8, placed so they seem "
                    "incidental.\n"
                    "7. Deliver exactly one moment of genuine wonder, at arm's length and through the senses.\n"
                    "8. End on the hook from my chapter outline.\n\n"
                    "After the chapter, list what a reader can infer about the galaxy from it, and flag "
                    "anything I explained that I should have implied.\n\n"
                    "End by asking me whether a reader who stopped here would want to spend four hundred more "
                    "pages with this person, and what specifically would make them want to."
                ),
                "pro_tip": (
                    "Keep the wonder to one moment. A first chapter that gasps at everything teaches the "
                    "reader to skim the descriptions, and by the time you reach the thing you actually wanted "
                    "them to marvel at, they have stopped looking."
                ),
            },
            {
                "title": "The Batch Drafting Engine",
                "desc": (
                    "The prompt you will reuse most. It drafts three to five chapters at a time while holding "
                    "voice, viewpoint discipline, travel-rule consistency and the state of the war."
                ),
                "prompt_text": (
                    "You are my drafting partner on a space opera novel. You write in my established voice "
                    "and hand control back to me at the end of every batch.\n\n"
                    "STANDING CONTEXT (reuse and update this block every batch):\n"
                    "- Voice sample: [PASTE 300-500 WORDS OF YOUR APPROVED CHAPTER ONE FROM PROMPT 18]\n"
                    "- Viewpoint characters and their current arc stage: [LIST]\n"
                    "- Ensemble status: [WHO IS ALIVE, WHO IS ABOARD, WHO IS INJURED, WHO IS ESTRANGED]\n"
                    "- Ship and fleet status: [DAMAGE, SUPPLIES, FUEL, ORDNANCE, CREW LOSSES]\n"
                    "- The war: [WHO HOLDS WHAT, WHAT HAPPENED LAST, WHAT EACH POWER BELIEVES]\n"
                    "- Travel and communication rules I must not break: [THE FIVE CONSTRAINTS FROM PROMPT 4]\n"
                    "- Information ladder: [WHAT EACH VIEWPOINT KNOWS THAT THE OTHERS DO NOT, FROM PROMPT 16]\n"
                    "- Elapsed time and current date: [STATE IT]\n\n"
                    "THIS BATCH: write chapters [X] to [Y] from my outline:\n"
                    "[PASTE THE OUTLINE ENTRIES FROM PROMPT 17]\n\n"
                    "Rules for this batch:\n"
                    "1. Match the voice sample in rhythm, sentence length and level of interiority.\n"
                    "2. Never let information travel faster than my communication rules allow.\n"
                    "3. Every chapter must change something in the standing context.\n"
                    "4. Faction characters speak in their own register; service characters use procedure and "
                    "shorthand.\n"
                    "5. Ground every large-scale event in one body in one room.\n"
                    "6. Re-establish viewpoint, place and time in the first three lines without a header "
                    "dump.\n"
                    "7. End each chapter on its outlined hook.\n\n"
                    "After the chapters, give me a STATUS REPORT: elapsed time, ship and fleet condition, "
                    "casualties, who now knows what, and any promise you made on the page that I owe the "
                    "reader.\n\n"
                    "End by asking me which chapter drifted furthest from my voice, so the next batch does "
                    "not inherit the drift."
                ),
                "pro_tip": (
                    "Update the information ladder every single batch. Nothing unravels a multi-viewpoint "
                    "space opera faster than a character reacting to news that, under your own communication "
                    "rules, is still six days from reaching them."
                ),
            },
        ],
    },

    {
        "name": "PHASE 6: POLISH, PUBLISH, EXPAND",
        "intro": (
            "The last three prompts protect your reviews and build what follows: an audit of scale, "
            "logistics and continuity, a voice pass that rations wonder and sharpens the enormous, and a "
            "combined publishing and multi-book series kit."
        ),
        "prompts": [
            {
                "title": "Scale, Logistics and Continuity Audit",
                "desc": (
                    "This genre's readers check your distances, your fuel and your timelines. This prompt "
                    "finds the breaches before a reviewer does."
                ),
                "prompt_text": (
                    "You are a continuity editor who specialises in large-canvas science fiction and who is "
                    "merciless about travel times, supply lines and information lag.\n\n"
                    "My travel and communication constraints: [PASTE FROM PROMPT 4]\n"
                    "My combat doctrine and the cost of war: [PASTE FROM PROMPT 7]\n"
                    "My powers and their economies: [PASTE FROM PROMPT 5]\n"
                    "My stakes ceiling: [FROM PROMPT 2]\n"
                    "My manuscript or detailed chapter summaries: [PASTE - WORK IN SECTIONS IF LONG]\n\n"
                    "Audit for the following, citing the chapter for every issue:\n\n"
                    "1. TRAVEL TIMES: every journey measured against my own constraints. Flag anything that "
                    "arrives too conveniently.\n"
                    "2. INFORMATION LAG: every place a character knows something before my communication "
                    "rules would allow.\n"
                    "3. LOGISTICS: fuel, ordnance, food, spare hulls, trained crew replacement. Where does a "
                    "fleet operate on supplies it does not have?\n"
                    "4. COMBAT CONSISTENCY: does every engagement obey the doctrine and timescale I set, or "
                    "do battles change speed to suit the scene?\n"
                    "5. STAKES CREEP: mark any point where the threatened scale exceeds the ceiling I set in "
                    "Prompt 2, and tell me the cost of leaving it in.\n"
                    "6. CAST TRACKING: who is where, who is alive, who has been off-page too long, and any "
                    "character acting on knowledge they do not have.\n"
                    "7. THE ECONOMY CHECK: does anyone in this book eat, get paid, and get replaced? Flag "
                    "where the galaxy runs on nothing.\n"
                    "8. NAME COLLISION: flag any names, places or ships too similar to tell apart at speed.\n\n"
                    "Rank findings CRITICAL, MODERATE or MINOR, with a fix for every CRITICAL item.\n\n"
                    "End by asking me which critical fix would require a structural change, so I can plan "
                    "that repair before touching the prose."
                ),
                "pro_tip": (
                    "Run item 8 before you finish drafting, not after. Two captains named Vey and Vela is a "
                    "problem you can fix in an afternoon at chapter twenty and a nightmare to untangle at "
                    "chapter fifty-five."
                ),
            },
            {
                "title": "The Wonder and Voice Pass",
                "desc": (
                    "This prompt tunes prose at the line level for the genre's specific demand: making the "
                    "enormous felt, keeping competence readable, and rationing awe so it still works late in "
                    "the book."
                ),
                "prompt_text": (
                    "You are a line editor working on epic science fiction.\n\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET]\n"
                    "Chapter to edit: [PASTE ONE CHAPTER]\n\n"
                    "Do a line-level pass:\n\n"
                    "1. THE SCALE TEST: find every place I state size, distance or quantity in numbers, and "
                    "propose a comparison, sensation or consequence that would land harder.\n"
                    "2. THE WONDER BUDGET: identify every moment of awe in this chapter. If there is more "
                    "than one, tell me which to keep and demote the rest to plain description.\n"
                    "3. THE BODY CHECK: mark places where a large event is described from nowhere, and show "
                    "me how to anchor it in one character's physical experience.\n"
                    "4. COMPETENCE REGISTER: check that professionals speak in procedure and shorthand rather "
                    "than explaining their jobs to each other. Rewrite the worst offender.\n"
                    "5. FACTION VOICE: flag any character speaking in generic register rather than their own "
                    "faction's, using my faction voices from Prompt 5.\n"
                    "6. RHYTHM MAP: check that sentences tighten in vacuum and combat and open up planetside "
                    "and in council. Show me one rewritten paragraph.\n"
                    "7. THE ABSTRACTION HUNT: find general nouns - the fleet, the enemy, the system, the "
                    "council - where a specific name from my world would land harder.\n"
                    "8. INFODUMP SWEEP: find every passage where the narrative explains politics or history, "
                    "and propose how to deliver it as friction between characters instead.\n\n"
                    "Return edits as a list - original line, proposed line, one-line reason. Do not rewrite "
                    "the chapter.\n\n"
                    "End by asking me which of your changes I rejected, so you can calibrate to my voice for "
                    "the next chapter."
                ),
                "pro_tip": (
                    "The wonder budget is the single most useful discipline in this pack. Three astonishments "
                    "per book, placed at the quarter marks, will do more for a reader than thirty - and the "
                    "ones you cut become ordinary description that makes the kept ones enormous."
                ),
            },
            {
                "title": "Blurb, Metadata and Series Architecture",
                "desc": (
                    "The combined publishing and series kit - retail copy, categories, cover brief, and the "
                    "multi-book architecture this genre almost always requires."
                ),
                "prompt_text": (
                    "You are a book marketing copywriter and series architect for adult science fiction.\n\n"
                    "My reader promise and pitches: [PASTE FROM PROMPT 3]\n"
                    "My premise, protagonist and hinge: [PASTE FROM PROMPTS 1 AND 9]\n"
                    "My beat sheet and ending: [PASTE FROM PROMPT 14]\n"
                    "My stakes ceiling: [FROM PROMPT 2]\n"
                    "My surviving cast and unresolved threads: [LIST]\n\n"
                    "PART A - THE RETAIL KIT:\n"
                    "1. THE BLURB: 150-200 words in three movements - the galaxy and its flashpoint in two "
                    "sentences, my protagonist and their impossible position, the stakes and hook. Nothing "
                    "past the midpoint. Lead with the person, not the empire.\n"
                    "2. TWO ALTERNATIVES: a punchy 100-word version, and one that leads with the crew.\n"
                    "3. THE HOOK LINE: three options for the line above the blurb.\n"
                    "4. CATEGORIES: 6 retail categories ranked by how well I compete in each.\n"
                    "5. KEYWORDS: 20 reader-search phrases grouped into trope, mood and situation terms.\n"
                    "6. COMP POSITIONING: 4 comparable reading experiences described as types of book, each "
                    "with a 'for readers who loved X but wanted Y' line.\n"
                    "7. THE COVER BRIEF: 5 visual directions tied to specific images from my book, and 3 "
                    "cover clichés to forbid.\n\n"
                    "PART B - THE SERIES:\n"
                    "8. THE SHAPE: recommend a series shape - a trilogy with one escalating war, an "
                    "open-ended crew series, or a generational mosaic across the same galaxy - and justify it "
                    "against my ending and my stakes ceiling.\n"
                    "9. THE SERIES QUESTION: the question the whole series answers, distinct from book one's.\n"
                    "10. THE ESCALATION RULE: what grows across books and what must stay intimate. Confirm "
                    "the series never exceeds the ceiling from Prompt 2, and say what I escalate instead of "
                    "scale.\n"
                    "11. BOOK TWO: a one-page premise - the new pressure, the returning cost from book one, "
                    "and a hook in the first three chapters. It must not undo book one's ending.\n"
                    "12. THE SEEDS: 6 things planted or plantable in book one that pay off later - a "
                    "character, a world, a debt, a technology, an unanswered question, a survivor.\n"
                    "13. THE STANDALONE GUARANTEE: confirm book one satisfies alone, and name anything in my "
                    "ending that reads as an unpaid promise rather than an open door.\n\n"
                    "End by asking me which promise in the blurb I am least confident the book delivers, so we "
                    "can fix the blurb or fix the book."
                ),
                "pro_tip": (
                    "Item 10 is what keeps a series alive past book two. When scale cannot grow, escalate "
                    "intimacy instead - move the war closer to the people the reader already loves, and the "
                    "stakes will feel larger while the numbers stay the same."
                ),
            },
        ],
    },
]
