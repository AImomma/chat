# -*- coding: utf-8 -*-
"""
Royalti Studios - Dystopian & Post-Apocalyptic Master Prompt Pack (Adult Fiction Line).

Build with:
    python pack_builder.py dystopian_postapoc_pack_data \
        "Dystopian_Post-Apocalyptic_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "DYSTOPIAN & POST-APOCALYPTIC",
    "total_prompts": 25,
    "hook_line": "Break the world on purpose - then make one ordinary person survive it, question it, and change it.",
    "keyword_lines": [
        "Collapse • Regime • Resistance • Scarcity • Rebellion • The Road",
        "Chosen family • Found crew • Betrayal • Rationing • Propaganda • Hope earned the hard way",
    ],
    "subgenres_line": "Subgenres: Political Dystopia, Corporate/Surveillance Dystopia, Climate Collapse, Pandemic/Plague, Nuclear Aftermath, Zombie & Infected, Survivalist Road Story, Bunker & Enclave, Rebuilding/Hopepunk",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-09",
    "audience_line": "Adult Fiction Line",
    "cover_h2": "From Broken World to Published Novel",
    "closing_tagline": "The world ends in chapter one. What you build after that is the book.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "This pack takes you from a single unsettling idea to a finished, publishable dystopian or "
        "post-apocalyptic novel. It covers both lanes because most books in this space live on the line "
        "between them: a regime that controls what is left, and a landscape that has stopped cooperating. "
        "Work the prompts in order. Each one produces an artifact - a premise, a collapse timeline, a "
        "control map, a beat sheet, drafted chapters - that the next prompt consumes. Save every output "
        "in one document; by Prompt 25 that document is your series bible."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-4) - Define the break. Choose your lane, find the one broken rule your whole "
        "book argues with, set the reader promise, and calibrate exactly how dark this book is allowed to get.",
        "Phase 2 (Prompts 5-9) - Build the broken world. Collapse timeline, the machinery of control, the "
        "arithmetic of scarcity, the map of danger, and the culture that grew in the ruins.",
        "Phase 3 (Prompts 10-13) - Forge the people. A protagonist shaped by compliance, an antagonist with "
        "a human face on an inhuman system, the crew who will not all make it, and the betrayal map.",
        "Phase 4 (Prompts 14-17) - Architect the story. The rupture that starts it, a full beat sheet, an "
        "escalation ladder that never repeats itself, and a cost ledger that keeps the stakes honest.",
        "Phase 5 (Prompts 18-21) - Write the book. Chapter outline with hooks, an opening that shows ordinary "
        "wrongness, a batch-drafting engine that holds voice across chapters, and a set-piece generator.",
        "Phase 6 (Prompts 22-25) - Polish, publish, expand. World-logic audit, a line-level voice pass, your "
        "blurb and metadata kit, and the architecture for book two and the long war.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool and a place to save your outputs between prompts. Brackets like "
        "[THIS] are placeholders - replace them with your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular. Pure dystopia? Prompt 7 becomes a light pass. "
        "Pure post-apocalypse with no regime? Prompt 6 becomes a sketch of whoever is filling the vacuum. "
        "Everything else runs the same either way."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "One broken rule the whole book argues with - not a list of bad things, a single premise pushed to its logical end",
            "A world with working arithmetic: where food, water, fuel, medicine and power actually come from, and who controls the supply",
            "Ordinary wrongness on page one - a detail the character finds normal and the reader finds horrifying",
            "A protagonist who is complicit before they are heroic; their compliance is the wound the book heals",
            "Control that is felt in small daily humiliations, not just announced in exposition",
            "Scarcity that forces real choices - every gain costs something specific and named",
            "An antagonist with a coherent, almost persuasive justification for the system they defend",
            "A found crew whose loyalties are tested by resource pressure, not just by villains",
            "Hope that is earned in inches and can be lost again - never handed over",
            "An ending that changes the world's rules, even if it only changes them for one town, one block, one family",
        ],
        "kills": [
            "Exposition dumps about the collapse before the reader cares about anyone standing in it",
            "A regime that is evil for no reason and has no economy, no logistics, and no internal politics",
            "Infinite bullets, fuel and batteries - the moment resources stop mattering, tension dies",
            "A protagonist who is instantly good at survival with no cost, no failure and no learning curve",
            "Villains who monologue their whole ideology instead of enacting it on the page",
            "The 'chosen one' shortcut in a genre whose entire point is that systems crush individuals",
            "A love story that pauses the apocalypse instead of being deformed by it",
            "Cruelty as set dressing - suffering that has no consequence and changes no one",
            "Endings where the regime collapses because one speech was given in one square",
            "Grimness with no texture: if nothing in the world is beautiful or funny, nothing is at stake",
        ],
        "voice": [
            "Concrete over abstract - name the ration card, the brand of the filter, the number on the door",
            "Short sentences under threat; longer, looser sentences in the rare safe moments",
            "Sensory specificity of decay: what the water tastes like, what the building smells like in August",
            "Understatement for horror - the flat delivery of an unbearable fact lands harder than adjectives",
            "Language shaped by the regime: euphemism, acronyms, official vocabulary the characters use without irony",
            "Interiority under pressure - what the character notices reveals what they are afraid of",
            "Withhold the collapse backstory; feed it in fragments a survivor would actually think about",
            "Let humor and tenderness survive in small doses; they are the proof that something is worth saving",
        ],
        "formula": (
            "Ordinary Wrongness -> The Rupture (a rule breaks, or the world does) -> Forced Movement "
            "(flee, join, hide, travel) -> The Crew Forms -> First Real Cost (someone pays) -> "
            "The System Reveals Its Logic (a persuasive antagonist scene) -> False Sanctuary -> Betrayal from Inside -> "
            "All Is Lost (the shelter falls, the plan fails, the truth lands) -> The Choice That Costs Everything -> "
            "Confrontation on the System's Own Ground -> A Changed Rule (not a fixed world) -> The New Ordinary, Uneasy"
        ),
        "reader_expectations": (
            "These readers are buying pressure and consequence. They want a world whose logistics hold up under "
            "scrutiny, a protagonist who starts compliant or unprepared and is remade by the pressure, and a "
            "system that is intellectually coherent enough to be frightening. They expect real loss - a book "
            "where the crew all survives feels like a lie - but they also expect a reason to keep going: one "
            "rule changed, one enclave saved, one child who will grow up differently. They will forgive a slow "
            "opening if the wrongness is specific, and they will forgive almost nothing if the resource math is "
            "sloppy or the regime makes no sense."
        ),
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "The end of the world is the easy part. Anyone can burn a city. What makes a dystopian or "
        "post-apocalyptic novel last is the arithmetic underneath it - who eats, who decides, who is allowed "
        "to speak, and what one ordinary person is willing to trade to change that. You built that arithmetic "
        "in Phase 2 and you spent it in Phases 4 and 5. Trust it. When a scene feels flat, it is almost always "
        "because the cost is missing: someone is getting something for free. Take it back, make them pay, and "
        "the scene will stand up. Now go finish the book - the world is already broken and it is waiting for "
        "someone to decide what comes next."
    ),

    "phases": [],
}


# ============================================================================
# PHASES
# ============================================================================

DATA["phases"] = [

    # ------------------------------------------------------------------
    {
        "name": "PHASE 1: DEFINE THE BREAK",
        "intro": (
            "Before you build a world you have to decide what kind of broken it is, what single rule your "
            "book is arguing with, and how dark you are willing to go. These four prompts produce the "
            "one-page contract that every later prompt refers back to. Do not skip Prompt 1 - the lane you "
            "choose changes the shape of the entire outline."
        ),
        "prompts": [
            {
                "title": "Lock Your Lane: Dystopian, Post-Apocalyptic, or the Line Between",
                "desc": (
                    "Dystopian and post-apocalyptic stories run on opposite engines: one is about too much "
                    "control, the other about none. Most strong books sit somewhere on the line. This prompt "
                    "puts you on a precise spot and tells you what that spot demands."
                ),
                "prompt_text": (
                    "You are a developmental editor who specialises in speculative fiction and has worked on "
                    "dystopian and post-apocalyptic novels for fifteen years.\n\n"
                    "My rough idea is: [DESCRIBE YOUR IDEA IN 2-4 SENTENCES - even if it is vague]\n\n"
                    "Do the following:\n\n"
                    "1. Place my idea on the CONTROL AXIS from 1 to 10, where 1 = total collapse, no functioning "
                    "authority (pure post-apocalyptic) and 10 = total control, everything functions and that is "
                    "the horror (pure dystopian). Explain in 3-4 sentences why it sits there.\n"
                    "2. Tell me what that position OBLIGATES me to do well. For a low score, name the survival "
                    "systems readers will scrutinise. For a high score, name the institutional detail readers "
                    "will scrutinise. For a middle score, name both and warn me which one writers usually fumble.\n"
                    "3. Name the TIME DISTANCE from the break: is this during the collapse, 6 months after, "
                    "10 years after, or generations later? Give me the pros and cons of each for my specific "
                    "idea, then recommend one.\n"
                    "4. List 5 published-feeling comparison points (describe the type of book, do not just name "
                    "titles) that occupy the same spot on the axis, and say what each one does that I will be "
                    "measured against.\n"
                    "5. Write my LANE STATEMENT in exactly two sentences: what kind of broken world this is, and "
                    "when in the breaking we meet it.\n\n"
                    "End by asking me one question: what part of my idea am I most protective of, so you can "
                    "make sure the lane does not crush it?"
                ),
                "pro_tip": (
                    "If your answer to the closing question is 'the ending', you probably have a dystopia. If it "
                    "is 'the relationship between two characters', you probably have a post-apocalyptic road "
                    "story. Let that pull your axis score before you lock it."
                ),
            },
            {
                "title": "The One Broken Rule",
                "desc": (
                    "Great books in this genre are not about many bad things. They are about one rule pushed to "
                    "its logical end until it becomes monstrous. This prompt finds your rule and stress-tests it."
                ),
                "prompt_text": (
                    "You are a speculative fiction editor known for finding the single premise underneath a messy "
                    "idea.\n\n"
                    "Here is my LANE STATEMENT from Prompt 1: [PASTE IT]\n"
                    "Here is everything else I know about my idea: [PASTE OR DESCRIBE]\n\n"
                    "Do the following:\n\n"
                    "1. Extract THE ONE BROKEN RULE - the single law, scarcity, technology, or social contract "
                    "that everything else in my world follows from. State it in one sentence of 20 words or fewer.\n"
                    "2. Give me 4 alternative versions of that rule that would make a sharper book, each in one "
                    "sentence, and say what kind of story each one would produce.\n"
                    "3. For my chosen rule, run a CONSEQUENCE CASCADE: list 10 downstream consequences in order "
                    "of distance from the rule (immediate, one year out, one generation out). Mark which 3 are "
                    "the most story-rich and say why.\n"
                    "4. Identify the rule's LOGICAL END - the point where following it all the way becomes "
                    "unbearable. That is my climax territory. Describe it in 3-4 sentences.\n"
                    "5. Name 3 ways a reader could poke a hole in this rule, and give me a defensible in-world "
                    "answer for each.\n\n"
                    "End by asking me which of the alternative rules tempted me, so we can decide together "
                    "whether to switch before I build a world on the wrong foundation."
                ),
                "pro_tip": (
                    "If your broken rule can be summarised as 'the government is bad' or 'a virus killed "
                    "everyone', you have a setting, not a premise. Push until the rule contains a specific "
                    "mechanism: who is counted, what is rationed, who is allowed to reproduce, what the "
                    "infected retain."
                ),
            },
            {
                "title": "Reader Promise & Shelf Position",
                "desc": (
                    "This prompt turns your premise into a market position - who this book is for, what emotional "
                    "experience it promises, and which shelf it sits on. Write it now and every later decision "
                    "gets easier."
                ),
                "prompt_text": (
                    "You are a publishing strategist who positions speculative fiction for adult readers.\n\n"
                    "My LANE STATEMENT: [PASTE FROM PROMPT 1]\n"
                    "My ONE BROKEN RULE: [PASTE FROM PROMPT 2]\n\n"
                    "Do the following:\n\n"
                    "1. Write my READER PROMISE in one paragraph: the emotional experience a reader is buying, "
                    "in the second person ('You will feel...').\n"
                    "2. Name my primary subgenre and two secondary ones from this list, and justify each: "
                    "political dystopia, corporate/surveillance dystopia, climate collapse, pandemic/plague, "
                    "nuclear aftermath, zombie/infected, survivalist road story, bunker/enclave, "
                    "rebuilding/hopepunk.\n"
                    "3. Identify the 3 reader appeals I am leading with (choose from: intellectual horror of the "
                    "system, visceral survival tension, found family, romance under pressure, mystery of what "
                    "happened, revolution and payback, moral dilemma, rebuilding and hope).\n"
                    "4. Write 3 one-line pitches in different registers: one bleak and literary, one "
                    "commercial and propulsive, one that leads with the relationship.\n"
                    "5. Tell me the 3 promises I must NOT break given this positioning, and what breaking each "
                    "one would cost me in reviews.\n\n"
                    "End by asking me which of the three pitches sounds most like the book I actually want to "
                    "write, since that answer will set the tone dial in the next prompt."
                ),
                "pro_tip": (
                    "Save the winning one-line pitch somewhere you can see it while drafting. In a genre this "
                    "sprawling, it is the fastest test for whether a chapter belongs in the book."
                ),
            },
            {
                "title": "The Bleakness Dial",
                "desc": (
                    "Readers will follow you almost anywhere if you are consistent about how dark this world is. "
                    "This prompt sets the ceiling and the floor - what can happen on the page, what stays off it, "
                    "and how much hope survives to the last chapter."
                ),
                "prompt_text": (
                    "You are a developmental editor calibrating tone for a dystopian / post-apocalyptic novel.\n\n"
                    "My READER PROMISE and pitch: [PASTE FROM PROMPT 3]\n"
                    "My instinct is that this book should feel: [DESCRIBE - e.g. bleak but humane, pulpy and "
                    "propulsive, quietly devastating, angry and political]\n\n"
                    "Do the following:\n\n"
                    "1. Set my BLEAKNESS DIAL from 1 to 10 (1 = cosy rebuilding, 10 = unrelenting) and describe "
                    "in 4-5 sentences what a book at that setting feels like page to page.\n"
                    "2. Define my ON-PAGE / OFF-PAGE LINE: list what kinds of violence, loss, and cruelty appear "
                    "in scene, what is reported after the fact, and what is only implied. Be specific to my "
                    "premise, not generic.\n"
                    "3. Set my HOPE FLOOR: name the specific thing that must still be true at the end of the "
                    "book, even in the worst version of my ending. One sentence.\n"
                    "4. Give me my RELIEF VALVES: 5 specific sources of warmth, beauty, or humour that can "
                    "survive in this world without breaking the tone (a food, a ritual, a piece of music, a "
                    "running joke, an animal, a small kindness). Make them specific to my setting.\n"
                    "5. Warn me about the 3 tonal drift risks for a book at this setting - the ways writers at "
                    "this dial accidentally slide up or down - and give me an early warning sign for each.\n\n"
                    "End by asking me whether my hope floor feels like a promise I actually believe, because if "
                    "I do not believe it, the reader will not either."
                ),
                "pro_tip": (
                    "Write your relief valves on a sticky note. Around chapter 15 of a bleak draft, every writer "
                    "forgets that a scene can be tender; the list is there to remind you it is allowed."
                ),
            },
        ],
    },

    # ------------------------------------------------------------------
    {
        "name": "PHASE 2: BUILD THE BROKEN WORLD",
        "intro": (
            "This is the phase that separates a book readers trust from one they argue with. You are building "
            "arithmetic, not atmosphere: a timeline that holds, a control system with a payroll, a scarcity "
            "model with real numbers, a map where danger has geography, and a culture that grew in the gap. "
            "Prompt 6 leans dystopian and Prompt 7 leans post-apocalyptic - run both, weighting them to the "
            "lane you locked in Prompt 1."
        ),
        "prompts": [
            {
                "title": "The Collapse Timeline",
                "desc": (
                    "You need to know far more about how the world broke than you will ever put on the page. "
                    "This prompt builds the full timeline so your fragments are consistent and your survivors "
                    "remember the right things."
                ),
                "prompt_text": (
                    "You are a worldbuilding consultant with a background in history and disaster response.\n\n"
                    "My ONE BROKEN RULE: [PASTE FROM PROMPT 2]\n"
                    "My LANE STATEMENT and time distance from the break: [PASTE FROM PROMPT 1]\n\n"
                    "Build my COLLAPSE TIMELINE:\n\n"
                    "1. THE BEFORE: 5 bullet points about the world as it was, focused on the pressure points "
                    "that made the break possible. No nostalgia - just the fault lines.\n"
                    "2. THE TRIGGER: what actually broke first, and why that specific thing. One paragraph.\n"
                    "3. THE CASCADE: a dated sequence of 8-12 events from the trigger to the present of my "
                    "story, showing how the failure spread across systems (power, food, water, medicine, "
                    "communications, transport, law, information). Note which system failed in an order that "
                    "will surprise readers.\n"
                    "4. THE STABILISATION: what stopped the fall - who or what filled the vacuum, and what "
                    "price was paid for that stability. This is where my antagonist system is born.\n"
                    "5. THE PRESENT: 6 bullet points describing daily life at the moment my story opens.\n"
                    "6. THE FRAGMENTS: 8 specific details from this timeline that an ordinary survivor would "
                    "actually remember or repeat - a rumour, a date everyone knows, a phrase, a smell, a lie "
                    "everyone tells. These are what I will put on the page instead of exposition.\n\n"
                    "End by asking me which single event on this timeline my protagonist was closest to, so we "
                    "can wire their personal history into the world's."
                ),
                "pro_tip": (
                    "The order in which systems fail is where originality lives. Everyone writes the power going "
                    "out. Try having the water hold and the courts go first, and watch how different your book "
                    "becomes."
                ),
            },
            {
                "title": "Regime Architecture: How Control Actually Works",
                "desc": (
                    "A regime is not a mood - it is a payroll, a supply chain, and a set of incentives. This "
                    "prompt builds the machinery of control so your antagonist system behaves like a real "
                    "institution instead of a fog of menace."
                ),
                "prompt_text": (
                    "You are a political scientist who consults on fiction about authoritarian systems.\n\n"
                    "My world: [PASTE THE PRESENT AND STABILISATION SECTIONS FROM PROMPT 5]\n"
                    "My broken rule: [PASTE FROM PROMPT 2]\n\n"
                    "Build my CONTROL ARCHITECTURE. If my world has no formal regime, build this for whoever or "
                    "whatever is filling the vacuum - a militia, a company, a religion, a family, a crew that "
                    "holds the water tower.\n\n"
                    "1. WHO RULES: the governing body, its name, its origin story, and the story it tells about "
                    "why it deserves power.\n"
                    "2. THE LEVERS: rank the 5 mechanisms of control it actually relies on, from most to least "
                    "important (choose from: food and water, medicine, information, surveillance, violence, "
                    "documentation/permits, employment, housing, religion, family/reproduction, debt, "
                    "transport permission). For each, describe exactly how it is enforced at street level.\n"
                    "3. THE PEOPLE WHO MAKE IT WORK: 5 job roles inside the system, from senior to lowly, with "
                    "one sentence each on what that person gets out of complying. Include at least one role that "
                    "is sympathetic.\n"
                    "4. THE CRACKS: 5 structural weaknesses - things the system cannot do, places it cannot "
                    "reach, resources it is short of, internal factions that hate each other. My resistance plot "
                    "will run through these.\n"
                    "5. THE VOCABULARY: 10 official words or euphemisms citizens use without irony (for "
                    "punishment, for the dead, for rationing, for informing, for the outside). Include the "
                    "chilling ones and the boring ones.\n"
                    "6. THE DAILY HUMILIATION: 6 small, specific, repeated indignities an ordinary person "
                    "experiences - the queue, the check, the form, the greeting, the inspection. These carry my "
                    "worldbuilding better than any exposition.\n\n"
                    "End by asking me which of the five cracks I want my protagonist to fall into first."
                ),
                "pro_tip": (
                    "The sympathetic insider from item 3 is the most useful character in the whole pack. Give "
                    "that person a scene in act one where they are kind, and act three will hurt in exactly the "
                    "right way."
                ),
            },
            {
                "title": "Scarcity Math & Survival Logistics",
                "desc": (
                    "Tension in this genre is arithmetic. This prompt gives you the real numbers - what is short, "
                    "how short, how long it lasts, and what people trade - so every scene can cost something "
                    "specific."
                ),
                "prompt_text": (
                    "You are a survival logistics consultant helping a novelist make scarcity feel real and "
                    "consistent.\n\n"
                    "My world and its present-day conditions: [PASTE FROM PROMPTS 5 AND 6]\n\n"
                    "Build my SCARCITY MODEL:\n\n"
                    "1. THE SHORTAGE LADDER: rank these by scarcity in my world, from most to least desperate, "
                    "with a one-line reason each: clean water, calories, salt, fuel, batteries/power, "
                    "antibiotics, ammunition, shoes/clothing, working tools, information, and one wildcard "
                    "specific to my premise.\n"
                    "2. THE NUMBERS: for my top 3 scarcities, give me concrete figures a character would think "
                    "in - litres per person per day, days of stock, distance to the nearest source, what a dose "
                    "costs in trade. Keep them plausible.\n"
                    "3. THE CURRENCY: what people actually trade in, and the exchange rates for 6 common "
                    "transactions. Include at least one thing whose value would surprise a reader.\n"
                    "4. THE ROUTINE: describe an ordinary day of acquisition for my protagonist - where they go, "
                    "what they carry, what they risk, how long it takes. Two paragraphs.\n"
                    "5. THE FAILURE MODES: 6 ways this system fails an individual (a lost card, a spoiled cache, "
                    "an infected wound, a broken filter, a raided store, a price shift). Each of these is a "
                    "potential inciting incident or midpoint disaster.\n"
                    "6. THE MEDICAL REALITY: what happens to a person with a broken arm, an infection, a "
                    "pregnancy, or a chronic condition in this world. Be specific and unsentimental.\n\n"
                    "End by asking me which scarcity I want to be the one my protagonist cannot solve, because "
                    "that is the one the ending will be built on."
                ),
                "pro_tip": (
                    "Track your protagonist's supplies in a spreadsheet while you draft. Readers of this genre "
                    "notice when the water bottle refills itself, and that single lapse costs you their trust "
                    "for the rest of the book."
                ),
            },
            {
                "title": "The Map of Danger",
                "desc": (
                    "Geography is plot in this genre. This prompt turns your world into zones with rules, "
                    "distances, and chokepoints so travel and territory generate tension by themselves."
                ),
                "prompt_text": (
                    "You are a worldbuilding cartographer for speculative fiction.\n\n"
                    "My world so far: [PASTE KEY POINTS FROM PROMPTS 5-7]\n"
                    "My story's home base is: [DESCRIBE - a city, a settlement, a compound, a road]\n\n"
                    "Build my MAP OF DANGER:\n\n"
                    "1. THE ZONES: define 5-7 named zones, each with: what it is, who controls it, the rule for "
                    "surviving there, the reason someone would still go, and its danger rating from 1 to 5.\n"
                    "2. THE DISTANCES: give me realistic travel times between the key zones on foot, by bicycle, "
                    "and by vehicle if vehicles exist, plus what makes each route dangerous.\n"
                    "3. THE CHOKEPOINTS: 4 places everyone must pass through - a bridge, a checkpoint, a tunnel, "
                    "a water source. For each, name who controls it and what the toll is.\n"
                    "4. THE SANCTUARIES: 3 places that feel safe, with the hidden cost or fragility of each. At "
                    "least one should be a false sanctuary that will fail in act two.\n"
                    "5. THE FORBIDDEN PLACE: the one location everyone avoids, why, and what is actually there. "
                    "My climax may live here.\n"
                    "6. THE SENSORY SIGNATURE: for each zone, one sound, one smell, and one visual detail that "
                    "tells a reader instantly where we are without a location tag.\n\n"
                    "End by asking me which zone my protagonist has never been to, so we can plan the chapter "
                    "where they finally cross into it."
                ),
                "pro_tip": (
                    "Give every zone a rule that can be broken and a toll that can be paid in more than one "
                    "currency. A chokepoint where the guard will take food, information, or a favour is a scene "
                    "engine you can run three times without repeating yourself."
                ),
            },
            {
                "title": "Culture After the Fall",
                "desc": (
                    "People do not stop being people. This prompt builds the rituals, slang, superstitions, and "
                    "art that grew in your broken world - the texture that makes it feel lived in rather than "
                    "staged."
                ),
                "prompt_text": (
                    "You are a cultural anthropologist consulting on a novel set in a collapsed or controlled "
                    "society.\n\n"
                    "My world: [PASTE HIGHLIGHTS FROM PROMPTS 5-8]\n"
                    "Time since the break: [FROM PROMPT 1]\n\n"
                    "Build my POST-BREAK CULTURE:\n\n"
                    "1. RITUALS: 5 practices people have developed around death, birth, food, arrival, and "
                    "departure. Each should reveal something about what this world fears or values.\n"
                    "2. SLANG: 12 words or phrases people use now - for outsiders, for the sick, for the dead, "
                    "for the authorities, for good luck, for the time before. Give each a one-line origin.\n"
                    "3. SUPERSTITIONS: 4 beliefs that are not true but that everyone half-observes, and the real "
                    "event each one grew from.\n"
                    "4. WHAT SURVIVED: 5 pieces of the old world that persist in mutated form - a song, a brand "
                    "name, a holiday, a sport, a piece of technology used for the wrong purpose.\n"
                    "5. THE GENERATION GAP: how someone who remembers the before differs from someone born "
                    "after, in 5 concrete behaviours. Include one way the younger generation is better adapted "
                    "and one way they are dangerously naive.\n"
                    "6. THE ART: what people make now, with what materials, and what it is about. One paragraph.\n\n"
                    "End by asking me which of these details my protagonist finds embarrassing or beneath them, "
                    "because that friction is character."
                ),
                "pro_tip": (
                    "Use no more than a third of what this prompt gives you. Culture works by implication - three "
                    "well-placed slang words make a reader believe in a whole society, while twelve make them "
                    "feel they are reading a glossary."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    # ------------------------------------------------------------------
    {
        "name": "PHASE 3: FORGE THE PEOPLE",
        "intro": (
            "A broken world is only as frightening as the people standing in it. These four prompts build a "
            "protagonist whose compliance is the wound the book heals, an antagonist who is almost persuasive, "
            "a crew whose loyalties are tested by scarcity rather than by villains, and the betrayal map that "
            "will drive your middle act."
        ),
        "prompts": [
            {
                "title": "The Protagonist and the Compliance Wound",
                "desc": (
                    "In this genre the strongest protagonists start complicit, adapted, or willfully blind. This "
                    "prompt builds a character whose survival strategy is exactly what has to break."
                ),
                "prompt_text": (
                    "You are a character-development editor for literary and commercial speculative fiction.\n\n"
                    "My world: [PASTE THE PRESENT-DAY SUMMARY FROM PROMPTS 5-7]\n"
                    "My rough protagonist idea: [DESCRIBE, or say 'you choose']\n\n"
                    "Build my PROTAGONIST:\n\n"
                    "1. THE BASICS: name, age, what they do to survive, who depends on them, where they sleep.\n"
                    "2. THE ADAPTATION: the specific strategy they use to get through each day in this world - "
                    "compliance, invisibility, usefulness to the system, hoarding, denial, small-scale cheating. "
                    "Describe it in a paragraph and name one thing they do daily that a pre-collapse reader "
                    "would find shameful.\n"
                    "3. THE COMPLIANCE WOUND: the thing they did, or failed to do, to survive - the moment they "
                    "chose themselves. State it in 3-4 sentences. This is the wound the plot will press on.\n"
                    "4. THE LIE THEY TELL: the sentence they repeat to justify their adaptation. Give me the "
                    "exact wording, in their voice.\n"
                    "5. THE COMPETENCE MAP: 3 things they are genuinely good at, 3 things they are dangerously "
                    "bad at, and one skill they have that will matter far more than they think.\n"
                    "6. THE ARC: a 5-stage arc from adaptation to action, where each stage is triggered by a "
                    "specific external pressure, not by a change of heart. Name the pressure each time.\n"
                    "7. THE ANCHOR: the one person, object, or place they will not abandon. This is what the "
                    "antagonist will eventually put on the table.\n\n"
                    "End by asking me whether I am willing to let this character do something genuinely "
                    "unforgivable in act two, because the answer determines how hard this book can hit."
                ),
                "pro_tip": (
                    "The compliance wound must be something the reader could imagine doing themselves. A "
                    "protagonist who betrayed a neighbour to feed a child is a novel. A protagonist who is "
                    "secretly a monster is a different, easier book."
                ),
            },
            {
                "title": "The System and Its Human Face",
                "desc": (
                    "Your real antagonist is a system, but systems cannot be punched. This prompt builds the "
                    "person who embodies it, complete with a justification your reader will have to work to "
                    "dismiss."
                ),
                "prompt_text": (
                    "You are an editor who specialises in antagonists that readers find uncomfortably "
                    "reasonable.\n\n"
                    "My control architecture: [PASTE FROM PROMPT 6]\n"
                    "My protagonist and their wound: [PASTE FROM PROMPT 10]\n\n"
                    "Build my ANTAGONIST LAYER:\n\n"
                    "1. THE SYSTEM: restate in two sentences what the true antagonist force is - the rule, the "
                    "regime, the scarcity, the infection, the vacuum.\n"
                    "2. THE FACE: create the individual who embodies it in my protagonist's life. Name, role, "
                    "how much actual power they hold, and how they first appear to my protagonist.\n"
                    "3. THE JUSTIFICATION: write their argument for the system in their own voice, 150-200 "
                    "words, at its most persuasive. It should contain at least one point I cannot easily "
                    "refute.\n"
                    "4. THE COST THEY PAID: what this person gave up to hold their position, and who they lost "
                    "doing it.\n"
                    "5. THE OVERLAP: 3 things this antagonist and my protagonist have in common, including one "
                    "the protagonist would deny.\n"
                    "6. THE PRESSURE POINTS: how this antagonist would apply leverage to my protagonist, ranked "
                    "from mild to unbearable, ending with the anchor from Prompt 10 item 7.\n"
                    "7. THE TRUE BELIEVER AND THE CYNIC: give me one secondary antagonist of each type, and say "
                    "which one is more dangerous in my specific world and why.\n\n"
                    "End by asking me whether my antagonist is allowed to be right about one thing, and if so, "
                    "which thing."
                ),
                "pro_tip": (
                    "Write the justification speech before you write a single scene with this character. Every "
                    "line of their dialogue afterwards should be a person who believes that speech, not a "
                    "person performing menace."
                ),
            },
            {
                "title": "The Crew That Will Not All Make It",
                "desc": (
                    "Found family is the beating heart of this genre - and its cruelty. This prompt builds an "
                    "ensemble where each member holds a resource, a viewpoint, and a fracture line."
                ),
                "prompt_text": (
                    "You are an ensemble-cast developer for survival and resistance fiction.\n\n"
                    "My protagonist: [PASTE FROM PROMPT 10]\n"
                    "My world's scarcities: [PASTE THE SHORTAGE LADDER FROM PROMPT 7]\n"
                    "My bleakness dial: [FROM PROMPT 4]\n\n"
                    "Build my CREW of 4-6 characters. For each one give me:\n\n"
                    "1. Name, age, and what they did before the break (or what they were raised into if born "
                    "after).\n"
                    "2. THE RESOURCE: the specific thing they bring that the group cannot survive without - a "
                    "skill, an access, a supply, a relationship, a piece of knowledge.\n"
                    "3. THE POSITION: their answer to the question 'what should we do about the system?' - "
                    "collaborate, hide, flee, resist, destroy, rebuild. No two crew members should hold the "
                    "same position.\n"
                    "4. THE FRACTURE LINE: the pressure that would make them betray, abandon, or endanger the "
                    "group. Be specific about the scenario.\n"
                    "5. THEIR RELATIONSHIP TO MY PROTAGONIST: what they need from them, what they cannot "
                    "forgive.\n"
                    "6. ONE HUMANISING DETAIL: a habit, a joke, a possession, a thing they still care about "
                    "that is completely impractical.\n\n"
                    "Then: rank the crew by narrative expendability, tell me which death would hurt the most and "
                    "why, and warn me which one I am most likely to under-write.\n\n"
                    "End by asking me which crew member I would most want to survive, so we can decide whether "
                    "the honest version of this book lets them."
                ),
                "pro_tip": (
                    "Give the character with the most useful skill the worst position on the system question. "
                    "Dependence plus disagreement is the engine that keeps an ensemble arguing for three "
                    "hundred pages."
                ),
            },
            {
                "title": "The Betrayal Map",
                "desc": (
                    "Every strong book in this genre turns on someone from the inside. This prompt lays out who "
                    "breaks, when, why, and what the reader is allowed to suspect beforehand."
                ),
                "prompt_text": (
                    "You are a plot architect specialising in trust, betrayal, and paranoia in survival "
                    "fiction.\n\n"
                    "My crew: [PASTE FROM PROMPT 12]\n"
                    "My antagonist and their pressure points: [PASTE FROM PROMPT 11]\n"
                    "My scarcity failure modes: [PASTE FROM PROMPT 7 ITEM 5]\n\n"
                    "Build my BETRAYAL MAP:\n\n"
                    "1. THE TRUST LEDGER: for each pair of characters who matter, one line on the current state "
                    "of trust and what it is based on.\n"
                    "2. THE BREAK: choose the character whose betrayal would do the most damage. State what "
                    "they do, when in the story, and the completely understandable reason they do it. It must "
                    "not be greed alone.\n"
                    "3. THE PLANTING: 6 details I can seed earlier in the book that will read as innocent on "
                    "first pass and damning on reread. Tell me roughly where each belongs.\n"
                    "4. THE RED HERRING: a second character who looks guiltier, what makes them look that way, "
                    "and how their innocence is proved.\n"
                    "5. THE SMALL BETRAYALS: 4 minor breaches of trust in acts one and two - hoarded food, a "
                    "withheld message, a lie about a wound - that establish that people here do break.\n"
                    "6. THE AFTERMATH: what the group does with the betrayer. Give me three options - exile, "
                    "execution, forgiveness under conditions - and say what each choice says about my book.\n\n"
                    "End by asking me whether my protagonist forgives the betrayer, because that answer defines "
                    "the moral position of the entire novel."
                ),
                "pro_tip": (
                    "The best betrayals in this genre are committed for the crew, not against it - someone trades "
                    "one member to save four. Write it that way and your reader will spend the last hundred "
                    "pages genuinely unsure who was right."
                ),
            },
        ],
    },

    # ------------------------------------------------------------------
    {
        "name": "PHASE 4: ARCHITECT THE STORY",
        "intro": (
            "You have a world and a cast. Now you build the machine. These four prompts give you the rupture "
            "that starts the book, a full beat sheet shaped for this genre, an escalation ladder that keeps "
            "act two from repeating itself, and a cost ledger that makes sure nothing is ever free."
        ),
        "prompts": [
            {
                "title": "The Rupture: Opening Situation and First Act",
                "desc": (
                    "Your book does not start when the world breaks - it starts when your protagonist's "
                    "adaptation stops working. This prompt finds that exact moment and builds act one around it."
                ),
                "prompt_text": (
                    "You are a story architect for dystopian and post-apocalyptic novels.\n\n"
                    "My protagonist and their adaptation: [PASTE FROM PROMPT 10]\n"
                    "My scarcity failure modes: [PASTE FROM PROMPT 7]\n"
                    "My control cracks: [PASTE FROM PROMPT 6 ITEM 4]\n\n"
                    "Build my FIRST ACT:\n\n"
                    "1. THE ORDINARY WRONGNESS: describe the opening scene - a normal day for my protagonist "
                    "that contains at least three details the reader will find horrifying and the character "
                    "will not remark on. Two paragraphs.\n"
                    "2. THE RUPTURE: the specific event that makes their survival strategy stop working. Give "
                    "me 4 options of increasing severity, then recommend one and explain why it fits my lane "
                    "and bleakness dial.\n"
                    "3. THE REFUSAL: what my protagonist tries first to restore the old arrangement, and why "
                    "it fails. This is where readers learn the rules of the world by watching them bite.\n"
                    "4. THE FORCED MOVEMENT: the moment they must leave, join, hide, or travel. Name the point "
                    "of no return and what is burned behind them.\n"
                    "5. THE ACT ONE BEATS: 8-10 sequential beats from the opening image to the point of no "
                    "return, each one sentence, each naming who is present and what changes.\n"
                    "6. THE QUESTION: the dramatic question act one plants, phrased as a yes/no the ending will "
                    "answer.\n\n"
                    "End by asking me what my protagonist loses in act one that they will spend the rest of the "
                    "book trying to get back - and whether they should get it."
                ),
                "pro_tip": (
                    "Resist opening with the collapse. A reader who watches an ordinary Tuesday in a wrong world "
                    "is far more unsettled than one who watches a city burn on page one, because the Tuesday "
                    "implies that everyone got used to it."
                ),
            },
            {
                "title": "The Full Beat Sheet",
                "desc": (
                    "This prompt maps the whole novel onto the genre's structural spine - compliance to revolt, "
                    "or shelter to road - with every major turn placed and justified."
                ),
                "prompt_text": (
                    "You are a story architect building a complete beat sheet for a dystopian / "
                    "post-apocalyptic novel.\n\n"
                    "My act one: [PASTE FROM PROMPT 14]\n"
                    "My crew and betrayal map: [PASTE FROM PROMPTS 12 AND 13]\n"
                    "My antagonist: [PASTE FROM PROMPT 11]\n"
                    "My map of danger: [PASTE THE ZONE LIST FROM PROMPT 8]\n"
                    "Target length: [E.G. 90,000 WORDS]\n\n"
                    "Build my BEAT SHEET across these stations, giving each one 2-4 sentences plus an "
                    "approximate word-count position:\n\n"
                    "1. Ordinary Wrongness\n"
                    "2. The Rupture\n"
                    "3. Forced Movement / Point of No Return\n"
                    "4. The Crew Forms (or the Cell Recruits)\n"
                    "5. First Real Cost - someone pays, and the reader learns this book is serious\n"
                    "6. The System Reveals Its Logic - the antagonist scene where the justification lands\n"
                    "7. Midpoint: False Sanctuary or Devastating Truth - state which one my book uses and why\n"
                    "8. The Small Betrayals Compound\n"
                    "9. The Break - the betrayal from Prompt 13\n"
                    "10. All Is Lost - the shelter falls, the plan fails, the anchor is taken\n"
                    "11. The Choice That Costs Everything - my protagonist acts against their adaptation\n"
                    "12. Confrontation on the System's Own Ground\n"
                    "13. A Changed Rule - what is actually different afterwards, and what is not\n"
                    "14. The New Ordinary, Uneasy\n\n"
                    "Then: flag any beat where I am relying on coincidence, and tell me which two beats are "
                    "currently doing the same job so I can cut or differentiate one.\n\n"
                    "End by asking me whether the changed rule at beat 13 is worth what my characters paid, "
                    "because if it is not, readers will call the ending nihilistic rather than honest."
                ),
                "pro_tip": (
                    "Beat 13 is the beat that separates this genre from misery. You do not have to fix the "
                    "world - you have to change one rule, permanently, and show the reader the first person "
                    "who benefits."
                ),
            },
            {
                "title": "The Escalation Ladder",
                "desc": (
                    "Middles sag in this genre because every chapter becomes another supply run. This prompt "
                    "builds an escalation ladder where each act-two sequence raises a different axis of pressure."
                ),
                "prompt_text": (
                    "You are a developmental editor fixing act-two repetition in survival fiction.\n\n"
                    "My beat sheet: [PASTE FROM PROMPT 15]\n"
                    "My scarcity model: [PASTE FROM PROMPT 7]\n"
                    "My zones: [PASTE FROM PROMPT 8]\n\n"
                    "Build my ESCALATION LADDER for act two:\n\n"
                    "1. THE AXES: list the 6 axes of pressure available to me - physical danger, resource "
                    "depletion, group cohesion, moral compromise, proximity to the antagonist, and the "
                    "protagonist's self-knowledge. Rate where each one stands at the start of act two on a "
                    "1-10 scale.\n"
                    "2. THE LADDER: design 8-10 act-two sequences in order. For each: what happens in one "
                    "sentence, which axis it raises, which axis it temporarily relieves, and the new number on "
                    "the raised axis. No axis may be raised twice in a row.\n"
                    "3. THE VARIETY CHECK: confirm that across these sequences I have at least one of each - a "
                    "journey, a siege, a negotiation, a quiet interpersonal scene, a discovery about the past, "
                    "an encounter with a stranger group, and a scene where the antagonist is not present but "
                    "their system is.\n"
                    "4. THE TIGHTENING: identify where the time pressure enters (a deadline, a countdown, a "
                    "dwindling supply with a knowable end date) and how I telegraph it.\n"
                    "5. THE BREATH: mark the two places I am allowed a scene of warmth, using the relief valves "
                    "from Prompt 4, and say what each one sets up for later.\n\n"
                    "End by asking me which sequence I am least excited to write, since that is usually the one "
                    "to cut or combine."
                ),
                "pro_tip": (
                    "The scene where the antagonist is absent but their system still hurts someone is the most "
                    "underused tool in the genre. A form, a queue, a closed clinic door - it does the villain's "
                    "work without a villain in the room."
                ),
            },
            {
                "title": "The Cost Ledger",
                "desc": (
                    "Nothing in a broken world should be free. This prompt audits every major story gain and "
                    "assigns it a price, keeping your stakes honest from first chapter to last."
                ),
                "prompt_text": (
                    "You are a story editor auditing stakes and consequence in a survival narrative.\n\n"
                    "My beat sheet and escalation ladder: [PASTE FROM PROMPTS 15 AND 16]\n"
                    "My crew: [PASTE FROM PROMPT 12]\n\n"
                    "Build my COST LEDGER:\n\n"
                    "1. THE GAINS: list every significant thing my characters acquire, achieve, or escape "
                    "across the novel - supplies, safety, information, allies, freedom, revenge.\n"
                    "2. THE PRICE: for each gain, assign a specific, named cost paid at the time or shortly "
                    "after. Costs may be material (supplies, a vehicle, a limb), relational (trust, a person, a "
                    "promise), or moral (a line crossed). Flag any gain that currently has no price.\n"
                    "3. THE BODY COUNT: which named characters die, when, at whose hands, and what each death "
                    "changes for the survivors. Warn me if any death is currently decorative.\n"
                    "4. THE PERMANENT MARKS: 5 things that cannot be undone by the end - an injury, a "
                    "reputation, a lost skill, a broken relationship, a memory. Readers measure a book like "
                    "this by what stays broken.\n"
                    "5. THE FINAL ACCOUNT: write the closing balance in one paragraph - what was won, what it "
                    "cost, and whether a reader will feel the trade was worth it.\n"
                    "6. THE THREE CHEAPEST MOMENTS: identify the three places where my story is currently "
                    "letting someone off easy, and give me a harder alternative for each.\n\n"
                    "End by asking me which permanent mark my protagonist carries into the last scene, and "
                    "whether the final image shows it."
                ),
                "pro_tip": (
                    "Run this ledger again after your first draft. Drafting brains are generous - they hand out "
                    "fuel, antibiotics and forgiveness without noticing. The second pass is where the book gets "
                    "its teeth back."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    # ------------------------------------------------------------------
    {
        "name": "PHASE 5: WRITE THE BOOK",
        "intro": (
            "Architecture becomes prose here. These four prompts give you a chapter outline with hooks, a "
            "first chapter that teaches the reader how to read your world, a batch-drafting engine that holds "
            "voice and continuity across long stretches, and a set-piece generator for the big sequences."
        ),
        "prompts": [
            {
                "title": "Chapter Outline with Hooks",
                "desc": (
                    "This prompt converts your beat sheet into a chapter-by-chapter plan where every chapter "
                    "has a job, a turn, and a reason the reader cannot stop."
                ),
                "prompt_text": (
                    "You are a novel outliner working in dystopian and post-apocalyptic fiction.\n\n"
                    "My beat sheet: [PASTE FROM PROMPT 15]\n"
                    "My escalation ladder: [PASTE FROM PROMPT 16]\n"
                    "My cost ledger: [PASTE FROM PROMPT 17]\n"
                    "Target: [E.G. 90,000 WORDS IN 40 CHAPTERS OF ABOUT 2,250 WORDS]\n"
                    "Point of view: [FIRST PERSON PRESENT / THIRD LIMITED PAST / MULTI-POV - and who]\n\n"
                    "Build my CHAPTER OUTLINE. For every chapter give me:\n\n"
                    "1. Chapter number and a working title.\n"
                    "2. POV character and location (using a zone name from Prompt 8).\n"
                    "3. The chapter's job in one sentence - what it must accomplish for the plot.\n"
                    "4. The turn: what is true at the end of the chapter that was not true at the start.\n"
                    "5. The cost paid in this chapter, drawn from my cost ledger, or 'none' if it is a breath "
                    "chapter.\n"
                    "6. The closing hook in the form of a one-line description (a revelation, a threat "
                    "arriving, a decision made, a door opening).\n\n"
                    "Then flag: any chapter whose job is only 'travel' or 'gather supplies', any three "
                    "consecutive chapters in the same location, and any stretch of more than four chapters "
                    "without a named cost.\n\n"
                    "End by asking me which chapter I am most afraid to write, so we can talk about why before "
                    "I get there."
                ),
                "pro_tip": (
                    "If a chapter's turn and its hook are the same thing, the chapter is one scene long. Either "
                    "give it a second movement or fold it into its neighbour."
                ),
            },
            {
                "title": "The Opening Chapter",
                "desc": (
                    "Chapter one teaches the reader how to read your world. This prompt drafts it with the "
                    "ordinary-wrongness technique, seeding rules, voice, and threat without a word of "
                    "exposition dump."
                ),
                "prompt_text": (
                    "You are a novelist drafting the opening chapter of a dystopian / post-apocalyptic novel, "
                    "writing in the style and voice described below.\n\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET, PLUS ANY NOTES "
                    "ON YOUR OWN STYLE]\n"
                    "My protagonist: [PASTE FROM PROMPT 10]\n"
                    "My opening situation: [PASTE FROM PROMPT 14 ITEM 1]\n"
                    "My daily humiliations and slang: [PASTE FROM PROMPTS 6 AND 9]\n"
                    "POV and tense: [SPECIFY]\n"
                    "Target length: [E.G. 2,000-2,500 WORDS]\n\n"
                    "Write chapter one, following these rules:\n\n"
                    "1. Open inside an ordinary task, mid-motion. No weather, no waking up, no dream.\n"
                    "2. Deliver at least three details of ordinary wrongness that my protagonist does not "
                    "remark on.\n"
                    "3. Use at least two pieces of in-world vocabulary in context, without defining them.\n"
                    "4. Show the protagonist's adaptation in action - let the reader watch them comply, hide, "
                    "or trade.\n"
                    "5. Include one moment of warmth or humour drawn from my relief valves.\n"
                    "6. Introduce the pressure that will become the rupture, at low volume.\n"
                    "7. Give me nothing about the collapse except what a person living in it would think about "
                    "in passing.\n"
                    "8. End on the hook from my chapter outline.\n\n"
                    "After the chapter, list the world rules a reader can infer from it and flag anything I "
                    "explained that I should have implied.\n\n"
                    "End by asking me which paragraph sounds least like me, so I can rewrite it in my own voice "
                    "before we go further."
                ),
                "pro_tip": (
                    "Read the finished chapter aloud and mark every sentence where you explained something. In "
                    "an opening chapter, the ratio you want is roughly one explanation for every ten "
                    "implications."
                ),
            },
            {
                "title": "The Batch Drafting Engine",
                "desc": (
                    "This is the prompt you will reuse most. It drafts three to five chapters at a time while "
                    "holding voice, continuity, supply levels, and the cost ledger steady across the batch."
                ),
                "prompt_text": (
                    "You are my drafting partner on a dystopian / post-apocalyptic novel. You will write "
                    "chapters in my established voice and hand control back to me at the end.\n\n"
                    "STANDING CONTEXT (reuse this block every batch):\n"
                    "- Voice sample: [PASTE 300-500 WORDS OF YOUR APPROVED CHAPTER ONE FROM PROMPT 19]\n"
                    "- Protagonist and arc stage: [PASTE FROM PROMPT 10, PLUS WHERE THEY ARE NOW]\n"
                    "- Crew status: [WHO IS ALIVE, WHO IS TRUSTED, WHO IS INJURED]\n"
                    "- Supply status: [WATER, FOOD, FUEL, AMMUNITION, MEDICINE - ACTUAL NUMBERS FROM PROMPT 7]\n"
                    "- Location and zone rules: [FROM PROMPT 8]\n"
                    "- Open threats and countdowns: [LIST]\n"
                    "- Costs already paid: [FROM PROMPT 17]\n\n"
                    "THIS BATCH: write chapters [X] to [Y] from my outline:\n"
                    "[PASTE THE OUTLINE ENTRIES FOR THOSE CHAPTERS FROM PROMPT 18]\n\n"
                    "Rules for this batch:\n"
                    "1. Match the voice sample in rhythm, sentence length, and level of interiority.\n"
                    "2. Every chapter must pay or bank a specific cost - never let a gain be free.\n"
                    "3. Track supplies across the batch and report the closing numbers.\n"
                    "4. Use concrete nouns; name the object, the brand, the door number, the ration.\n"
                    "5. Dialogue does the arguing - characters hold the positions assigned in Prompt 12.\n"
                    "6. End each chapter on its outlined hook.\n\n"
                    "After the chapters, give me: a CONTINUITY REPORT (supplies, injuries, time elapsed, "
                    "distance travelled, who knows what), and a list of any promises you made on the page that "
                    "I now owe the reader.\n\n"
                    "End by asking me which chapter in this batch drifted furthest from my voice, so I can fix "
                    "it before the next batch inherits the drift."
                ),
                "pro_tip": (
                    "Update the standing context block after every batch and never skip the supply numbers. "
                    "That one habit prevents the most common continuity complaint this genre attracts."
                ),
            },
            {
                "title": "The Set-Piece Generator",
                "desc": (
                    "Sieges, raids, crossings, tribunals, and quarantines are the big sequences readers "
                    "remember. This prompt designs one from the ground up with geography, stakes, and a real "
                    "cost."
                ),
                "prompt_text": (
                    "You are an action and suspense choreographer for survival fiction.\n\n"
                    "My world and zones: [PASTE FROM PROMPT 8]\n"
                    "My crew and their skills: [PASTE FROM PROMPT 12]\n"
                    "My supply status: [CURRENT NUMBERS]\n"
                    "The set piece I need: [E.G. A NIGHT CROSSING OF A CONTROLLED BRIDGE / A SIEGE OF THE "
                    "SHELTER / A RATION-DEPOT RAID / A PUBLIC TRIBUNAL / A QUARANTINE SWEEP]\n"
                    "Where it sits in my outline: [CHAPTER NUMBER AND BEAT]\n\n"
                    "Design the sequence:\n\n"
                    "1. THE GEOGRAPHY: map the space in specifics - entrances, sightlines, cover, the thing "
                    "that will go wrong about the terrain, and the one route nobody has considered.\n"
                    "2. THE PLAN: what my crew intends, who does what, and the assumption the plan rests on.\n"
                    "3. THE BREAK: how the plan fails, in two stages - a small failure that is absorbed, then "
                    "the real one.\n"
                    "4. THE BEATS: 10-14 sequential beats of the sequence, each one sentence, with the tension "
                    "rising and at least two reversals.\n"
                    "5. THE RESOURCE CLOCK: what is being spent during the sequence - rounds, minutes, "
                    "daylight, battery, blood - and where it runs out.\n"
                    "6. THE COST: what this sequence takes permanently, drawn from my cost ledger.\n"
                    "7. THE AFTER: the quiet scene immediately following, and the one thing said in it that "
                    "changes a relationship.\n\n"
                    "End by asking me whether the crew member who solves this sequence is the one I expected, "
                    "because the answer tells us whether my ensemble is balanced."
                ),
                "pro_tip": (
                    "Write the quiet scene at item 7 before you write the action. Knowing exactly which "
                    "relationship the sequence is meant to change keeps a big set piece from becoming a "
                    "well-choreographed detour."
                ),
            },
        ],
    },

    # ------------------------------------------------------------------
    {
        "name": "PHASE 6: POLISH, PUBLISH, EXPAND",
        "intro": (
            "A finished draft in this genre lives or dies on internal consistency and on the promise your "
            "cover and blurb make. These final four prompts audit your world logic, tune your prose at the "
            "line level, build your publishing kit, and lay the architecture for the books that follow."
        ),
        "prompts": [
            {
                "title": "World-Logic and Continuity Audit",
                "desc": (
                    "This is the prompt that protects your reviews. It hunts the specific inconsistencies this "
                    "genre's readers are trained to catch - supply math, timelines, distances, and institutional "
                    "behaviour."
                ),
                "prompt_text": (
                    "You are a continuity editor who specialises in dystopian and post-apocalyptic fiction and "
                    "who is known for being merciless about logistics.\n\n"
                    "My world rules: [PASTE PROMPTS 5-9 SUMMARY]\n"
                    "My manuscript or detailed chapter summaries: [PASTE - WORK IN SECTIONS IF LONG]\n\n"
                    "Audit for the following, listing every issue with the chapter where it occurs:\n\n"
                    "1. SUPPLY MATH: water, food, fuel, ammunition, medicine, batteries. Where does something "
                    "appear, refill, or last longer than established?\n"
                    "2. TIMELINE: elapsed days, healing times for injuries, travel durations against the "
                    "distances set in Prompt 8, seasons and daylight.\n"
                    "3. INSTITUTIONAL BEHAVIOUR: does my regime or controlling group act consistently with the "
                    "levers, cracks and staffing I defined in Prompt 6? Where are they conveniently competent "
                    "or conveniently incompetent?\n"
                    "4. KNOWLEDGE STATE: track who knows what and when. Flag any character acting on "
                    "information they should not have.\n"
                    "5. TECHNOLOGY AND INFRASTRUCTURE: what is still working, who maintains it, and what "
                    "should have failed by now.\n"
                    "6. WOUND AND ILLNESS REALISM: check every injury against the medical reality from Prompt "
                    "7 item 6.\n"
                    "7. THE FREE LUNCH LIST: every place a character gains something without paying.\n\n"
                    "Rank all findings as CRITICAL (breaks reader trust), MODERATE (a careful reader notices), "
                    "or MINOR. Give me a fix suggestion for every CRITICAL item.\n\n"
                    "End by asking me which of the critical fixes would force a structural change, so we can "
                    "plan that repair before I touch the prose."
                ),
                "pro_tip": (
                    "Run this audit in chunks of ten chapters. Fed a whole manuscript at once, any AI will "
                    "skim; fed ten chapters with the world rules attached, it will catch things you have read "
                    "past twenty times."
                ),
            },
            {
                "title": "The Line-Level Voice Pass",
                "desc": (
                    "Bleak prose curdles easily. This prompt tunes your sentences for grit without mush - "
                    "concrete nouns, controlled rhythm, understated horror, and language shaped by the world."
                ),
                "prompt_text": (
                    "You are a line editor for literary-leaning speculative fiction.\n\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET]\n"
                    "My bleakness dial: [FROM PROMPT 4]\n"
                    "Chapter to edit: [PASTE ONE CHAPTER]\n\n"
                    "Do a line-level pass:\n\n"
                    "1. ABSTRACTION HUNT: find every abstract or general noun where a specific one would land "
                    "harder (supplies, danger, the authorities, food) and propose the concrete replacement my "
                    "world would actually use.\n"
                    "2. ADJECTIVE AUDIT: flag places where I am asserting bleakness with adjectives instead of "
                    "showing it with detail. Rewrite three of the worst offenders.\n"
                    "3. RHYTHM MAP: mark passages where sentence length does not match tension - long sentences "
                    "in danger, clipped sentences in calm - and show me one rewritten paragraph.\n"
                    "4. UNDERSTATEMENT PASS: find the two most horrifying moments in the chapter and rewrite "
                    "them flatter, letting the fact do the work.\n"
                    "5. IN-WORLD LANGUAGE: identify where my characters use pre-collapse vocabulary they would "
                    "no longer use, and swap in the slang and euphemisms from Prompts 6 and 9.\n"
                    "6. INTERIORITY CHECK: mark places where the protagonist notices what the plot needs "
                    "instead of what a frightened person would notice.\n"
                    "7. THE ONE BEAUTIFUL THING: find or add a single image of beauty in this chapter, "
                    "consistent with my relief valves.\n\n"
                    "Return the edits as a list with the original line, the proposed line, and a one-line "
                    "reason - not a rewritten chapter.\n\n"
                    "End by asking me which of your changes I rejected, so you can calibrate to my voice on the "
                    "next chapter."
                ),
                "pro_tip": (
                    "Ask for a list of proposed edits, never a rewritten chapter. The moment an AI hands you a "
                    "clean rewrite, your voice quietly becomes its voice, and in a genre this tonally specific "
                    "that is the difference between your book and everyone's book."
                ),
            },
            {
                "title": "Blurb, Metadata and Category Kit",
                "desc": (
                    "This prompt builds the whole retail package - blurb, categories, keywords, and comparison "
                    "positioning - matched to the reader promise you set back in Prompt 3."
                ),
                "prompt_text": (
                    "You are a book marketing copywriter specialising in speculative fiction for adult readers.\n\n"
                    "My reader promise and pitches: [PASTE FROM PROMPT 3]\n"
                    "My premise, protagonist and stakes: [PASTE FROM PROMPTS 2, 10 AND 15]\n"
                    "My bleakness dial and hope floor: [PASTE FROM PROMPT 4]\n"
                    "My subgenres: [FROM PROMPT 3]\n\n"
                    "Build my retail kit:\n\n"
                    "1. THE BLURB: 150-200 words in three movements - the world in two sentences, the "
                    "protagonist and their impossible choice, the stakes and the hook line. Do not summarise "
                    "the plot past the midpoint.\n"
                    "2. TWO ALTERNATIVES: a shorter, punchier 100-word version, and one that leads with the "
                    "found-family or relationship angle.\n"
                    "3. THE HOOK LINE: three options for the single line that sits above the blurb.\n"
                    "4. CATEGORIES: 6 retail categories and subcategories this book belongs in, ranked by how "
                    "well it competes there.\n"
                    "5. KEYWORDS: 20 reader-search phrases, grouped into trope terms, mood terms, and "
                    "situation terms.\n"
                    "6. COMP POSITIONING: describe 4 comparable reading experiences (types of book, not just "
                    "titles) and write the one-sentence 'for readers who loved X but wanted Y' line for each.\n"
                    "7. THE CONTENT NOTE: an honest, non-spoiling note about the darkness level, drawn from my "
                    "on-page / off-page line in Prompt 4.\n"
                    "8. THE COVER BRIEF: 5 visual directions a designer could work from, each tied to a "
                    "specific image from my book rather than genre wallpaper.\n\n"
                    "End by asking me which promise in the blurb I am least confident the book delivers, so we "
                    "can either fix the blurb or fix the book."
                ),
                "pro_tip": (
                    "The content note is not a legal disclaimer - it is a targeting tool. Readers who want "
                    "unrelenting bleakness search for it, and readers who do not will one-star you for a "
                    "surprise. Naming your dial wins both."
                ),
            },
            {
                "title": "Series Architecture: Book Two and the Long War",
                "desc": (
                    "Dystopian and post-apocalyptic stories scale naturally into series. This prompt designs "
                    "the arc across books, decides what escalates and what stays intimate, and sets up book two "
                    "without cheapening book one's ending."
                ),
                "prompt_text": (
                    "You are a series architect for speculative fiction.\n\n"
                    "My book one, ending included: [PASTE THE BEAT SHEET FROM PROMPT 15 AND THE FINAL ACCOUNT "
                    "FROM PROMPT 17]\n"
                    "My world's control architecture and cracks: [PASTE FROM PROMPT 6]\n"
                    "My surviving cast: [LIST]\n\n"
                    "Design my SERIES:\n\n"
                    "1. THE SHAPE: recommend a series shape and justify it - a trilogy with one escalating war, "
                    "an open-ended survival series with standalone arcs, or a mosaic across different "
                    "characters in the same world. Say which fits my ending.\n"
                    "2. THE SERIES QUESTION: the single question the whole series answers, distinct from book "
                    "one's dramatic question.\n"
                    "3. THE ESCALATION RULE: what gets bigger across books (scale of the system, geography, "
                    "number of people depending on my protagonist) and what must stay intimate so the series "
                    "does not lose its spine.\n"
                    "4. BOOK TWO: a one-page premise - the new pressure, the new zone or faction, the returning "
                    "cost from book one, and a rupture in the first three chapters. It must not undo book one's "
                    "changed rule.\n"
                    "5. BOOK THREE AND BEYOND: a paragraph each on the remaining books, ending with what the "
                    "final image of the series is.\n"
                    "6. THE SEEDS: 6 things I should plant or have already planted in book one that pay off "
                    "later - a character, a place, a rumour, an object, an unanswered question, a debt.\n"
                    "7. THE STANDALONE GUARANTEE: confirm that book one still satisfies alone, and name "
                    "anything in my ending that currently reads as an unpaid promise rather than an open door.\n\n"
                    "End by asking me whether my protagonist survives the series, because planning that now "
                    "changes what I plant in book one."
                ),
                "pro_tip": (
                    "Never end book one on a cliffhanger in this genre. Change the rule, let your protagonist "
                    "pay for it, and let the open door be a new pressure rather than an unresolved crisis - "
                    "readers reward the completed arc and will follow you anywhere afterwards."
                ),
            },
        ],
    },
]
