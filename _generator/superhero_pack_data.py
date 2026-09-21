# -*- coding: utf-8 -*-
"""
Royalti Studios - Superhero Fiction Master Prompt Pack (Adult Fiction Line).

Build with:
    python pack_builder.py superhero_pack_data \
        "Superhero_Fiction_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "SUPERHERO FICTION",
    "total_prompts": 24,
    "hook_line": "Give one person power the world was not built to hold - then make them live in that world, in prose, with the mask off at the kitchen table.",
    "keyword_lines": [
        "Origins • Secret identities • Rogues galleries • Teams • Capes and consequences",
        "Powered people • Collateral damage • Public opinion • Arch-enemies • The next city over",
    ],
    "subgenres_line": "Subgenres: Four-Color Heroic, Street-Level Vigilante, Deconstruction & Cape Noir, Team/Ensemble, Powered-World Social Fiction, Superhero Romance, Villain POV, Retired-Hero Story, Supers Procedural",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-21",
    "audience_line": "Adult Fiction Line",
    "cover_h2": "From Origin Story to Published Novel",
    "closing_tagline": "The powers are the easy part. The book is about the world that has to absorb them.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "Superhero fiction in prose is not a comic without pictures. It loses the splash page and gains "
        "interiority, which means it has to earn its spectacle with consequence and its consequence with "
        "rules. This pack builds the whole machine: a power system with hard costs, an origin that is a "
        "wound rather than an accident, a world whose laws and media and ordinary people have actually "
        "reacted to the existence of powers, a rogues gallery rather than a single villain, and a "
        "collateral ledger that makes every fight cost somebody something. Work the prompts in order and "
        "save every output in one document. By Prompt 24 that document is your series bible - which this "
        "genre, being serial by nature, will demand of you."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-4) - Define the lane. Place yourself on the four-color-to-deconstruction axis, "
        "build a power system with hard limits and real costs, write the origin as a wound, and lock the "
        "reader promise.",
        "Phase 2 (Prompts 5-8) - Build the world that has powers in it. The institutional response (law, "
        "government, oversight), the street-level and media reality, the wider power landscape and its "
        "history, and the city as a character.",
        "Phase 3 (Prompts 9-13) - Forge the cast. The civilian life and dual-life ledger, the costume and "
        "the symbol, a rogues gallery of recurring antagonists, the arch-enemy who is an argument against "
        "your hero, and the supporting cast sorted by who knows.",
        "Phase 4 (Prompts 14-17) - Architect the story. The inciting crisis and first act, the full beat "
        "sheet, the collateral ledger that keeps the fights honest, and a set-piece generator with "
        "geography and consequence.",
        "Phase 5 (Prompts 18-21) - Write the book. Chapter outline with hooks, an opening that shows the "
        "cost before the spectacle, a batch-drafting engine, and an action-prose pass - because rendering a "
        "fight in sentences is this genre's distinctive craft problem.",
        "Phase 6 (Prompts 22-24) - Polish, publish, expand. A power-logic and continuity audit, the blurb "
        "and metadata kit, and series architecture including the power-creep problem that kills long runs.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool and a place to save your outputs between prompts. Brackets like "
        "[THIS] are placeholders - replace them with your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular. Writing a street-level vigilante with no "
        "registration regime? Prompt 5 becomes a light pass on police and press. Writing a solo hero with "
        "no team? Prompt 13 covers the supporting cast only. Writing villain POV? Run Prompts 9-12 with the "
        "roles inverted - the pack works the same from the other side."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "A power with a hard rule and a real cost - what it cannot do matters more than what it can",
            "An origin that is a wound, not an accident; the power should be shaped like the damage",
            "A world that has visibly reacted to powers - law, insurance, journalism, protest, merchandise, fear",
            "Consequence that lands on named people: a fight that wrecks a block should wreck someone specific in it",
            "A dual life with real logistics - the missed shift, the unexplained injury, the lie told to someone who deserved better",
            "A rogues gallery, plural, where each antagonist argues with a different part of the hero",
            "An arch-enemy who is a thesis: the person your hero could have been, or the argument they cannot answer",
            "Restraint as drama - the moments the hero does not use the power are where character lives",
            "Public opinion as a live force that can turn, and does",
            "Spectacle paid for in prose currency: interiority, sensation and aftermath rather than panel description",
        ],
        "kills": [
            "Powers with no rules, which turn every climax into an arbitrary negotiation the reader cannot follow",
            "Escalating power to raise stakes - the fastest way to make a reader stop caring by book three",
            "A world where nothing institutional has changed despite people flying over it",
            "Collateral damage as scenery: buildings fall, nobody named is hurt, nobody sues, nobody grieves",
            "A secret identity that costs nothing and is never nearly blown by anything mundane",
            "One-note villains defined only by a power set and a grudge",
            "Fight scenes written as camera directions, blow by blow, with no interiority and no stakes between hits",
            "The hero winning by discovering a new ability at the exact moment it is needed",
            "Civilians who exist only to be rescued and to cheer",
            "Grimness as sophistication - a deconstruction that has contempt for the genre it is standing on",
        ],
        "voice": [
            "Sensation over choreography - what the power feels like in the body beats what it looks like from outside",
            "Keep the prose close in a fight; the reader should be inside the decisions, not above the arena",
            "Let the mundane register carry the dual life: shift rosters, bus fare, a landlord, a sister's birthday",
            "Institutional language as texture - incident reports, press-conference phrasing, oversight jargon",
            "Understatement for aftermath; the flat inventory of what broke lands harder than lament",
            "Distinct voices for masked and unmasked selves, and let the seam between them show",
            "Ration the awe: two or three genuinely astonishing uses of power per book",
            "Humour survives in this genre and should - the mask does not make people less funny",
        ],
        "formula": (
            "The Ordinary Life (a person with a power, managing) -> The Crisis That Cannot Be Ignored -> "
            "The First Public Act (the world sees, and reacts) -> The Cost Arrives (someone pays for the "
            "rescue) -> The Rogues Gallery Notices -> The Institutional Response Tightens -> The Identity "
            "Is Strained (the mundane nearly exposes everything) -> The Arch-Enemy States the Argument -> "
            "The Failure (the power is not enough, or is exactly the problem) -> The Renunciation or the "
            "Escalation (a choice about what the power is for) -> The Confrontation on Human Terms -> "
            "A Changed Rule, Publicly -> The Life, Resumed and Altered"
        ),
        "reader_expectations": (
            "Readers of superhero prose are buying two things comics cannot give them: the inside of the "
            "mask, and consequences that persist. They want a power system with rules they can reason about, "
            "a world that has plausibly adjusted to powered people, and an antagonist roster with enough "
            "personality to carry a series. They expect the fights to matter - to cost money, lives, "
            "reputation, or a relationship - and they expect the hero's private life to be genuinely damaged "
            "by the secret. They will not forgive power creep, ability inflation at the climax, or "
            "destruction with no named victim. What they reward: restraint, specificity, a villain they can "
            "argue for, and a hero whose worst problem is not a fight but a conversation."
        ),
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "Every draft in this genre reaches a point where the writer is tempted to solve a problem with more "
        "power. Resist it once and you have a novel; resist it every time and you have a series. The rules "
        "you set in Prompt 2 and the ledger you built in Prompt 16 exist precisely for that moment - they "
        "are not restrictions, they are the reason anything in your book is difficult. When a scene feels "
        "weightless, check two things: does the power cost what you said it costs, and is there a named "
        "person standing in the rubble? Fix either one and the scene stands up. Now go finish the book - "
        "someone out there is holding more than they can carry, and the world has not decided yet what to "
        "do about it."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: DEFINE THE LANE",
        "intro": (
            "Superhero fiction spans a wider tonal range than almost any genre - from bright heroic "
            "adventure to bitter deconstruction to satire - and readers of one end will reject the other. "
            "These four prompts place you deliberately, build a power system with hard limits, write the "
            "origin as a wound, and turn all of it into a market position."
        ),
        "prompts": [
            {
                "title": "Lock Your Lane: Four-Color to Deconstruction",
                "desc": (
                    "This genre's tonal range is its biggest trap. This prompt puts you on a precise spot, "
                    "tells you what that spot obligates, and names the failure mode of the position you are "
                    "probably drifting toward."
                ),
                "prompt_text": (
                    "You are a developmental editor who has worked on superhero prose fiction and comics "
                    "for twenty years.\n\n"
                    "My rough idea is: [DESCRIBE IN 2-4 SENTENCES - a power, a character, an image, a "
                    "situation, whatever I have]\n\n"
                    "Do the following:\n\n"
                    "1. Place my idea on the TONE AXIS from 1 to 10, where 1 = bright four-color heroic "
                    "adventure (the power is a gift, heroism works) and 10 = full deconstruction (the power "
                    "is a pathology, heroism is a lie people tell). Explain the placement in 3-4 sentences.\n"
                    "2. Place me on the SCALE AXIS from 1 to 10, where 1 = street-level (one neighbourhood, "
                    "human-sized threats) and 10 = world-ending. Say what each end demands of my climax.\n"
                    "3. Name my primary subgenre and two secondaries from: four-color heroic, street-level "
                    "vigilante, deconstruction/cape noir, team ensemble, powered-world social fiction, "
                    "superhero romance, villain POV, retired-hero story, supers procedural. Justify each.\n"
                    "4. Tell me what my position OBLIGATES. For a low tone score, name the sincerity I must "
                    "sustain without irony. For a high score, name the affection for the genre I must keep "
                    "so the book is not merely contemptuous. For the middle, warn me which way writers "
                    "usually slide mid-draft.\n"
                    "5. THE DECONSTRUCTION TRAP: if my score is 7 or above, tell me plainly what my book "
                    "must offer beyond 'superheroes would actually be bad', since that observation is now "
                    "forty years old.\n"
                    "6. Write my LANE STATEMENT in two sentences: what kind of superhero book this is and "
                    "what it believes about power.\n\n"
                    "End by asking me whether I love this genre or am arguing with it, because both make "
                    "good books and they are not the same book."
                ),
                "pro_tip": (
                    "The middle of the tone axis is the hardest place to stand and the most commercially "
                    "rewarding. A book that takes heroism seriously and still counts the cost outsells both "
                    "the pure romp and the pure teardown."
                ),
            },
            {
                "title": "The Power System and Its Hard Limits",
                "desc": (
                    "A power with no rules makes every climax arbitrary. This prompt builds a system with "
                    "costs, limits and failure modes - the constraints that make your plot difficult and "
                    "therefore possible."
                ),
                "prompt_text": (
                    "You are a systems designer who builds rigorous power systems for fiction and who is "
                    "hostile to hand-waving.\n\n"
                    "My lane statement: [PASTE FROM PROMPT 1]\n"
                    "My hero's power, roughly: [DESCRIBE, or say 'you choose']\n\n"
                    "Build my POWER SYSTEM:\n\n"
                    "1. THE MECHANISM: what the power actually does, stated in three plain sentences with "
                    "no mystical vagueness. If it has a physical basis, name it; if it does not, say so "
                    "clearly and consistently.\n"
                    "2. THE FIVE HARD LIMITS: things the power cannot do, ever. Write them as rules I may "
                    "never break for plot convenience. At least one should be inconvenient rather than "
                    "dramatic.\n"
                    "3. THE COST: what using it takes - calories, pain, time, memory, blood, hearing, "
                    "sleep, years. Give me the cost at three usage levels: casual, hard, and everything "
                    "they have. Include the recovery time for each.\n"
                    "4. THE SKILL CURVE: what my hero can do now, what practice would unlock, and what is "
                    "permanently out of reach. State plainly what they will NOT learn during this book, so "
                    "I cannot cheat the climax.\n"
                    "5. THE FAILURE MODES: 5 ways the power goes wrong - misfires, overreach, side effects, "
                    "an unintended consequence, a thing it does that they did not ask for.\n"
                    "6. THE COUNTERS: 5 ways an ordinary, unpowered opponent could beat or neutralise my "
                    "hero. If there are none, the power is broken - redesign it and tell me why.\n"
                    "7. THE MUNDANE USES: 4 ways this power makes daily life easier or worse in ways that "
                    "have nothing to do with fighting. This is where readers fall in love with a power set.\n"
                    "8. THE SIGNATURE MOMENT: the one use of this power that will be the image readers "
                    "remember from the book.\n\n"
                    "End by asking me which hard limit my hero will try hardest to break, because that "
                    "attempt is a whole act of my story."
                ),
                "pro_tip": (
                    "Item 7 earns more reader affection than item 8. A hero who uses telekinesis to reach "
                    "the cereal on the high shelf is a person; one who only uses it to throw cars is a "
                    "power set with a name."
                ),
            },
            {
                "title": "The Origin as a Wound",
                "desc": (
                    "Accidents are not origins. This prompt builds an origin where the power is shaped like "
                    "the damage, and where the hero's whole arc is already implied."
                ),
                "prompt_text": (
                    "You are a character-development editor who specialises in origin stories.\n\n"
                    "My power system: [PASTE FROM PROMPT 2]\n"
                    "My lane statement: [FROM PROMPT 1]\n"
                    "My rough origin idea, if I have one: [DESCRIBE, or say 'you choose']\n\n"
                    "Build my ORIGIN:\n\n"
                    "1. THE EVENT: how the power arrived - in one paragraph, concrete and specific, with "
                    "the sensory detail a person would actually retain.\n"
                    "2. THE WOUND: what my hero lost, failed at, or was subjected to in that event or the "
                    "life around it. State it in three sentences. This is the engine of the book.\n"
                    "3. THE SHAPE MATCH: explain how the power and the wound rhyme - how what they can now "
                    "do is a distorted answer to what happened to them. If they do not rhyme, redesign one "
                    "of them and tell me which.\n"
                    "4. THE FIRST USE: the first time they used it, what went wrong, and what that taught "
                    "them to fear about themselves.\n"
                    "5. THE WITNESS: who knew or suspected from the beginning, and where that person is now.\n"
                    "6. THE LIE THEY TELL THEMSELVES: the sentence my hero repeats about why they do this. "
                    "Give me the exact wording, in their voice. The book will disprove it.\n"
                    "7. THE WHY-NOW: what makes this the year the story happens, rather than any of the "
                    "years before it.\n"
                    "8. THE WITHHOLDING PLAN: how much of this origin appears in chapter one, how much is "
                    "revealed mid-book, and what stays back until the climax. Give me the actual split.\n\n"
                    "End by asking me whether my hero would give the power up if offered, honestly, today - "
                    "and what that answer says about the wound."
                ),
                "pro_tip": (
                    "Never open with the full origin. Item 8 is the real deliverable here: a hero already "
                    "living with the power, whose origin arrives in fragments, is far more gripping than a "
                    "first chapter that explains everything before the reader cares."
                ),
            },
            {
                "title": "Reader Promise & Shelf Position",
                "desc": (
                    "Superhero prose sits in an awkward retail spot and needs deliberate positioning. This "
                    "prompt sets who it is for and which promises are load-bearing."
                ),
                "prompt_text": (
                    "You are a publishing strategist positioning genre fiction for adult readers, with "
                    "specific experience in superhero and powered-world prose.\n\n"
                    "My lane statement and axis placement: [PASTE FROM PROMPT 1]\n"
                    "My power system and origin: [PASTE FROM PROMPTS 2-3]\n\n"
                    "Do the following:\n\n"
                    "1. Write my READER PROMISE in one paragraph, in the second person ('You will feel...').\n"
                    "2. Identify the 3 reader appeals I am leading with, from: power fantasy and "
                    "competence, moral dilemma, found family or team dynamics, romance complicated by a "
                    "secret, mystery or procedural investigation, social commentary on power and "
                    "institutions, revenge, the cost of heroism.\n"
                    "3. THE CROSSOVER QUESTION: tell me honestly whether this book reads as science "
                    "fiction, urban fantasy, thriller, or literary fiction with powers - because superhero "
                    "prose usually has to be shelved as something. Recommend the shelf and say what to "
                    "emphasise for it.\n"
                    "4. Write 3 one-line pitches in different registers: one that leads with the power, "
                    "one that leads with the cost, one that leads with the relationship.\n"
                    "5. Name my ideal reader in a paragraph - what they have read and watched recently, and "
                    "what they are hungry for that the market underserves.\n"
                    "6. List the 4 promises I must NOT break, and write the one-star review each breach "
                    "would generate in the reviewer's own words.\n"
                    "7. THE ORIGINALITY CHECK: name the 5 most familiar elements in my concept and, for "
                    "each, one specific way to make it mine.\n\n"
                    "End by asking me which pitch sounds most like the book I actually want to write, since "
                    "that decides how much page time goes to fights versus consequences."
                ),
                "pro_tip": (
                    "Lead with the cost, not the power. Every book in this space promises someone who can "
                    "do something extraordinary; the ones that sell promise what it is doing to them."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: BUILD THE WORLD THAT HAS POWERS IN IT",
        "intro": (
            "This is where superhero prose earns credibility that comics can skip. If people have been "
            "flying over this city for twenty years, the insurance industry knows, the courts know, the "
            "press knows, and the person who lives under the flight path knows. These four prompts build "
            "that world so your plot has institutions to push against."
        ),
        "prompts": [
            {
                "title": "The Institutional Response",
                "desc": (
                    "Law, government, oversight, liability. This prompt builds the machinery a state builds "
                    "when some of its citizens can level a building - and the seams in it your plot will "
                    "live in."
                ),
                "prompt_text": (
                    "You are a worldbuilding consultant with a background in law and public policy, "
                    "advising on a world where a minority of people have superhuman abilities.\n\n"
                    "My power system: [PASTE FROM PROMPT 2]\n"
                    "My lane and scale placement: [FROM PROMPT 1]\n"
                    "How long powers have existed publicly: [SPECIFY - 5 YEARS, 40 YEARS, GENERATIONS, "
                    "OR 'THEY ARE STILL SECRET']\n\n"
                    "Build my INSTITUTIONAL LAYER:\n\n"
                    "1. THE LEGAL STATUS: is having powers registered, licensed, criminalised, protected, "
                    "or unaddressed? Describe the actual law in plain terms, including what a powered person "
                    "must or must not do.\n"
                    "2. THE ENFORCEMENT BODY: who polices powered people. Name it, describe its capability, "
                    "its funding, its public reputation, and its internal politics. Include what it cannot "
                    "do.\n"
                    "3. VIGILANTISM: how the law treats unsanctioned heroics specifically. What charge does "
                    "my hero face if identified? Is there tolerance in practice, and who decides?\n"
                    "4. LIABILITY AND MONEY: who pays when a fight destroys property. Insurance, a public "
                    "fund, the powered individual, nobody? This single answer shapes how the public feels "
                    "about my hero.\n"
                    "5. THE MEDICAL AND SCIENTIFIC RESPONSE: who studies powers, what they have figured "
                    "out, what treatment or suppression exists, and who is denied access to it.\n"
                    "6. THE SEAMS: 5 places this system fails or cannot reach. My plot runs through these.\n"
                    "7. THE PAPERWORK: 6 specific documents, forms, procedures or bureaucratic phrases that "
                    "exist in this world. Concrete institutional texture sells a powered world faster than "
                    "any action scene.\n\n"
                    "End by asking me whether my hero is operating legally, illegally, or in a grey zone, "
                    "because that status is the pressure under every scene."
                ),
                "pro_tip": (
                    "Item 4 is the most underused engine in the genre. A world where the hero's rescues "
                    "generate lawsuits, and a neighbourhood that resents being saved expensively, gives you "
                    "conflict that never needs a villain."
                ),
            },
            {
                "title": "The Street and the Press",
                "desc": (
                    "This prompt builds the ground-level reality: how ordinary people actually live with "
                    "powers, how media covers them, and how public opinion is made and turned."
                ),
                "prompt_text": (
                    "You are a consultant on media, public opinion and everyday life in a world with "
                    "superhuman people.\n\n"
                    "My institutional layer: [PASTE FROM PROMPT 5]\n"
                    "My city, roughly: [DESCRIBE OR SAY 'YOU CHOOSE']\n\n"
                    "Build my STREET-LEVEL REALITY:\n\n"
                    "1. THE ORDINARY ADJUSTMENTS: 8 ways daily life differs because powered people exist - "
                    "building codes, transit, school drills, signage, apps, jokes, precautions, prices. Make "
                    "them mundane and specific.\n"
                    "2. THE MEDIA LAYER: who covers powered people and how. Name 3 outlets or channels with "
                    "distinct angles - one sensational, one serious, one hostile - and give me a headline "
                    "from each about my hero's first public act.\n"
                    "3. PUBLIC OPINION: the current split on powered people. Give me the percentages, the "
                    "demographic lines it falls along, and the event that last moved it.\n"
                    "4. THE TURN: what would make public opinion turn against my hero specifically. Design "
                    "it now - I will use it in act two.\n"
                    "5. THE FANDOM AND THE BACKLASH: how people who admire powered heroes behave, and how "
                    "people who fear them organise. Give each a specific, plausible form.\n"
                    "6. THE COMMERCE: what gets sold because of powers - merchandise, security products, "
                    "insurance riders, tours, protective gear, quack remedies.\n"
                    "7. THE SLANG: 10 terms ordinary people use for powered individuals, heroics, "
                    "collateral damage, and the powerless. Include the neutral, the affectionate and the "
                    "slurs, and say who uses which.\n"
                    "8. THE UNPOWERED VIEW: one paragraph in the voice of an ordinary resident who has "
                    "lived through three of these fights and is tired.\n\n"
                    "End by asking me which of these ordinary details my hero finds most humiliating, "
                    "because that friction is character."
                ),
                "pro_tip": (
                    "Write item 8 and keep it. When the book drifts into spectacle, that tired resident's "
                    "voice is the fastest way back to why any of it matters."
                ),
            },
            {
                "title": "The Power Landscape",
                "desc": (
                    "Your hero is not alone, and the shape of the wider powered population determines "
                    "everything about how their story reads. This prompt builds the demographics, the "
                    "history and the other players."
                ),
                "prompt_text": (
                    "You are a worldbuilding consultant mapping the powered population of a fictional "
                    "world.\n\n"
                    "My power system and its origin mechanism: [PASTE FROM PROMPT 2]\n"
                    "My institutional layer: [PASTE FROM PROMPT 5]\n\n"
                    "Build my POWER LANDSCAPE:\n\n"
                    "1. THE NUMBERS: how many powered people exist, in what proportion of the population, "
                    "and how strong the typical one is compared to my hero. State plainly whether my hero is "
                    "ordinary, notable, or unique among them.\n"
                    "2. THE SOURCE: why anyone has powers in this world - one cause or many? Describe it, "
                    "and say who understands it and who is lying about understanding it.\n"
                    "3. THE DISTRIBUTION: are powers inherited, random, acquired, purchasable, "
                    "geographically clustered? Spell out the social consequence of the answer - inherited "
                    "powers make dynasties, purchasable powers make class war.\n"
                    "4. THE OTHER HEROES: 4 other powered individuals operating publicly. For each: name, "
                    "power, method, public standing, and their opinion of my hero.\n"
                    "5. THE TEAMS AND INSTITUTIONS: any organised groups - sanctioned teams, private "
                    "security firms, criminal crews, mutual-aid networks, religious movements. Name 3 and "
                    "give each a purpose and an internal problem.\n"
                    "6. THE HISTORY: 4 landmark events in the public history of powers, ending with the one "
                    "that everybody still argues about.\n"
                    "7. THE POWER TIERS: a clear internal ranking of capability in my world, so a reader "
                    "always knows what a given opponent means. Place my hero and my major antagonists on it.\n"
                    "8. THE MISSING: what happened to the powered people who did not become heroes or "
                    "villains - the ones with useless powers, the ones who quit, the ones who were "
                    "institutionalised.\n\n"
                    "End by asking me which other powered person my hero will need and resent, because that "
                    "relationship carries a whole subplot."
                ),
                "pro_tip": (
                    "Item 8 is where original superhero fiction hides. The person whose power is mildly "
                    "useful and socially ruinous is a character no comic has room for and a prose novel does."
                ),
            },
            {
                "title": "The City as Character",
                "desc": (
                    "Superhero stories are geographically loyal - the hero belongs to a place. This prompt "
                    "builds yours with specificity, verticality and a map of where fights can happen."
                ),
                "prompt_text": (
                    "You are a setting specialist making a fictional or fictionalised city feel like a "
                    "specific place rather than a generic urban backdrop.\n\n"
                    "My street-level reality: [PASTE FROM PROMPT 6]\n"
                    "My hero's power and how they move: [FROM PROMPT 2]\n"
                    "Real city it resembles, if any: [SPECIFY OR SAY 'YOU CHOOSE']\n\n"
                    "Build my CITY:\n\n"
                    "1. THE IDENTITY: what this city is for - what industry built it, who lives there now, "
                    "what it is proud of and ashamed of. Two paragraphs.\n"
                    "2. THE FIVE DISTRICTS: name and describe 5 in a paragraph each - who lives there, what "
                    "it smells like, its landmark, and what kind of trouble happens there.\n"
                    "3. THE VERTICALITY: if my hero moves in three dimensions, describe the city from that "
                    "angle - rooftops, bridges, the height of things, where the sightlines are, where you "
                    "cannot be seen. If they do not, describe the city at street speed instead.\n"
                    "4. THE HERO'S TERRITORY: the specific few blocks my hero actually protects, and why "
                    "those. A hero who guards a whole city guards nowhere.\n"
                    "5. THE FIGHT SITES: 5 locations where a set piece could happen, each with a reason the "
                    "geography makes it interesting and a reason a fight there would be a disaster for "
                    "someone.\n"
                    "6. THE SANCTUARY: the place my hero goes to be nobody. One paragraph, and it must not "
                    "be a lair.\n"
                    "7. THE SENSORY KIT: for each district, one sound, one smell and one visual that "
                    "identifies it without a location tag.\n"
                    "8. THE ANTI-GENERIC PASS: list the 8 most overused superhero-city images and give me a "
                    "specific replacement for each from the material above.\n\n"
                    "End by asking me what my hero would lose if this city changed, since that is what they "
                    "are really defending."
                ),
                "pro_tip": (
                    "Item 4 does the heavy lifting. Narrow the hero's real territory to something walkable "
                    "and the stakes become legible - readers can hold four blocks and the people on them in "
                    "their head, and they cannot hold a metropolis."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: FORGE THE CAST",
        "intro": (
            "Five prompts, because this genre needs more cast architecture than most: a civilian life with "
            "real logistics, a costume that means something, a rogues gallery rather than one villain, an "
            "arch-enemy who is an argument, and a supporting cast sorted by who knows the secret."
        ),
        "prompts": [
            {
                "title": "The Civilian Life and the Dual-Life Ledger",
                "desc": (
                    "The secret identity is where superhero prose beats every other medium. This prompt "
                    "builds the ordinary life in enough detail that the mask has something to cost."
                ),
                "prompt_text": (
                    "You are a character-development editor who specialises in dual-life narratives.\n\n"
                    "My hero's origin and wound: [PASTE FROM PROMPT 3]\n"
                    "My power and its costs: [PASTE FROM PROMPT 2]\n"
                    "My institutional layer - what happens if they are identified: [FROM PROMPT 5]\n\n"
                    "Build my HERO'S CIVILIAN LIFE:\n\n"
                    "1. THE BASICS: name, age, job, income, where they live, what their apartment or house "
                    "is actually like, who they live with.\n"
                    "2. THE WORK: what they do for money in specific detail - hours, colleagues, a "
                    "supervisor, what they are good at and bad at, and whether the job is compatible with "
                    "disappearing at short notice.\n"
                    "3. THE MONEY: what heroics cost them in cash - equipment, repairs, medical care they "
                    "cannot claim, missed shifts, transport. Give me a monthly figure against their income.\n"
                    "4. THE LEDGER OF LIES: 8 specific lies they have told, to whom, and which one is "
                    "closest to collapsing. Include at least two that are mundane and pathetic rather than "
                    "dramatic.\n"
                    "5. THE BODY EVIDENCE: what their body looks like up close - scars, exhaustion, the "
                    "injury they are currently hiding - and the 4 situations in ordinary life where that is "
                    "hard to explain.\n"
                    "6. THE NEAR MISSES: 5 mundane ways the secret almost comes out. Not surveillance and "
                    "villains - a laundry mix-up, a dentist, a shared phone, a photo tag, a sibling who "
                    "notices.\n"
                    "7. THE THING THEY GAVE UP: the relationship, career, or plan that the secret has "
                    "already cost. Name it and say whether they admit it was the secret's fault.\n"
                    "8. THE SUSTAINABILITY QUESTION: state plainly how much longer this arrangement can "
                    "last, and what forces the answer.\n\n"
                    "End by asking me who my hero most wants to tell, and what specifically stops them."
                ),
                "pro_tip": (
                    "Item 6 is the genre's most reliable tension source and the one writers skip. A hero "
                    "nearly exposed by a dental X-ray is more suspenseful than one nearly exposed by a "
                    "government satellite, because the reader has been to the dentist."
                ),
            },
            {
                "title": "The Costume, the Name and the Symbol",
                "desc": (
                    "In prose, the costume has to work practically and mean something thematically, because "
                    "nobody can see it. This prompt builds both, plus how the public names your hero."
                ),
                "prompt_text": (
                    "You are a costume and identity designer working on a prose superhero novel, where "
                    "every visual choice must be conveyable in sentences and must mean something.\n\n"
                    "My hero, their power and their wound: [PASTE FROM PROMPTS 2-3 AND 9]\n"
                    "My tone axis placement: [FROM PROMPT 1]\n"
                    "My institutional and public context: [FROM PROMPTS 5-6]\n\n"
                    "Build my HERO'S PRESENTATION:\n\n"
                    "1. THE PRACTICAL PROBLEM: what my hero actually needs from an outfit given their power "
                    "and their opposition - protection, concealment, mobility, pockets, fire resistance, "
                    "something the power requires. List the requirements before the aesthetics.\n"
                    "2. THE BUILD: what they are actually wearing, where each piece came from, what it "
                    "cost, and what is improvised. Include the thing that does not work well and has not "
                    "been fixed.\n"
                    "3. THE CONCEALMENT: how the face and identity are hidden, and the specific weakness of "
                    "that method.\n"
                    "4. THE MEANING: what the costume says, and whether my hero chose that meaning or it "
                    "was assigned to them. One paragraph.\n"
                    "5. THE THREE PROSE DETAILS: since readers cannot see it, give me the three specific "
                    "details I will repeat throughout the book to make the image stick - a texture, a "
                    "sound it makes, a colour, a smell, the way it sits wrong on the shoulder.\n"
                    "6. THE NAME: how my hero got their public name. Give me 5 options for the name and, "
                    "crucially, say whether the hero chose it, the press coined it, or a child did. The "
                    "answer is characterisation.\n"
                    "7. THE HERO'S OPINION: what they think of the name and the costume. Embarrassment is "
                    "usually more interesting than pride.\n"
                    "8. THE EVOLUTION: how the presentation changes across the book, and what event drives "
                    "each change.\n\n"
                    "End by asking me whether my hero was ever photographed badly, because a humiliating "
                    "public image is a gift to a novel."
                ),
                "pro_tip": (
                    "Let the press name your hero. A name the hero did not choose and cannot shake gives "
                    "you an ongoing relationship with public opinion for free, and it is funnier and truer "
                    "than a self-chosen codename."
                ),
            },
            {
                "title": "The Rogues Gallery",
                "desc": (
                    "Superhero fiction is serial by nature and needs recurring antagonists, not one villain. "
                    "This prompt builds a roster where each one argues with a different part of your hero."
                ),
                "prompt_text": (
                    "You are an antagonist developer for serial fiction.\n\n"
                    "My hero, their power, limits and wound: [PASTE FROM PROMPTS 2-3]\n"
                    "My power landscape and tiers: [PASTE FROM PROMPT 7]\n"
                    "My city and its fight sites: [FROM PROMPT 8]\n\n"
                    "Build my ROGUES GALLERY of 4-5 recurring antagonists. Crucially, each must press on a "
                    "different part of my hero. For each:\n\n"
                    "1. Name, public name if any, and what they actually want - a concrete goal, not "
                    "'chaos'.\n"
                    "2. THE POWER OR METHOD: what they can do, placed on my power tiers from Prompt 7, and "
                    "specifically how it interacts with my hero's hard limits from Prompt 2. At least one "
                    "should have no powers at all.\n"
                    "3. THE ARGUMENT: which of my hero's beliefs, fears or compromises this antagonist "
                    "attacks. No two may attack the same one.\n"
                    "4. THE SYMPATHY: the reason a reasonable reader might side with them at least once.\n"
                    "5. THE PERSONAL HOOK: how they are or could become connected to my hero's civilian "
                    "life.\n"
                    "6. THE RECURRENCE PLAN: whether they survive this book, and what state they are left "
                    "in.\n\n"
                    "Then: rank them by how much of this book each should occupy, tell me which one is the "
                    "book-one antagonist and which are seeded for later, and warn me which one I am most "
                    "likely to write as a cliche.\n\n"
                    "End by asking me which rogue my hero secretly likes, because that relationship will "
                    "outlast the plot."
                ),
                "pro_tip": (
                    "Make one antagonist entirely unpowered. A determined human with money, patience or a "
                    "badge is the hardest opponent to write and the one readers remember, because your "
                    "hero's powers do not solve them."
                ),
            },
            {
                "title": "The Arch-Enemy as Argument",
                "desc": (
                    "The arch-enemy is not the strongest opponent - they are the thesis your hero cannot "
                    "answer. This prompt builds that person and the debate the book is really staging."
                ),
                "prompt_text": (
                    "You are an editor who specialises in antagonists that function as arguments.\n\n"
                    "My hero's wound, lie and lane statement: [PASTE FROM PROMPTS 1 AND 3]\n"
                    "My rogues gallery: [PASTE FROM PROMPT 11]\n"
                    "My institutional layer: [FROM PROMPT 5]\n\n"
                    "Build my ARCH-ENEMY:\n\n"
                    "1. THE THESIS: state in one sentence the claim about power that this person embodies "
                    "and my hero cannot refute.\n"
                    "2. THE PERSON: name, history, what they were before, how they arrived at the thesis, "
                    "how they speak, and what they are genuinely good at.\n"
                    "3. THE PARALLEL ORIGIN: how their origin rhymes with my hero's from Prompt 3 - same "
                    "event, same wound, different conclusion. Make the divergence a specific choice, not a "
                    "difference of character.\n"
                    "4. THE ARGUMENT, IN FULL: 200 words in their voice, at their most persuasive, making "
                    "the case. It must contain at least one point my hero is currently living as a "
                    "hypocrite about.\n"
                    "5. THE METHOD: what they actually do. Their acts must follow from the thesis - if they "
                    "are just cruel, the thesis is decoration.\n"
                    "6. THE LINE THEY CROSS: the specific act where a reader's sympathy has to break. Name "
                    "it precisely and place it in the story.\n"
                    "7. THE OFFER: what they offer my hero at the midpoint - not a temptation to be evil, "
                    "but a genuinely appealing alternative. Write the offer in their words.\n"
                    "8. THE REBUTTAL: what my hero must be able to say or do by the end that answers the "
                    "thesis. If I cannot answer it, the book's ending is a fudge - tell me so.\n\n"
                    "End by asking me whether my hero is, in fact, wrong about something the arch-enemy is "
                    "right about, and whether the book is brave enough to admit it."
                ),
                "pro_tip": (
                    "Item 8 is the whole book. Write the rebuttal before you write the plot; if your hero's "
                    "only answer to the arch-enemy's argument is winning the fight, readers will read the "
                    "ending as an evasion."
                ),
            },
            {
                "title": "The Supporting Cast and Who Knows",
                "desc": (
                    "In this genre the supporting cast is sorted by information. This prompt builds them and "
                    "maps exactly who knows, who suspects, and what each would do with the truth."
                ),
                "prompt_text": (
                    "You are an ensemble developer for dual-life fiction.\n\n"
                    "My hero's civilian life and ledger of lies: [PASTE FROM PROMPT 9]\n"
                    "My rogues gallery and arch-enemy: [PASTE FROM PROMPTS 11-12]\n"
                    "My city and hero's territory: [FROM PROMPT 8]\n\n"
                    "Build my SUPPORTING CAST of 5-7 characters, and sort every one of them into a "
                    "KNOWLEDGE TIER: knows, suspects, has no idea, or knows and my hero does not realise "
                    "it. For each:\n\n"
                    "1. Name, age, relationship to my hero, and how they met.\n"
                    "2. THEIR KNOWLEDGE TIER, and the specific evidence they hold or the specific reason "
                    "they have never wondered.\n"
                    "3. WHAT THEY WANT FROM MY HERO, which must have nothing to do with heroics for at "
                    "least three of them.\n"
                    "4. WHAT THEY WOULD DO WITH THE TRUTH: protect, expose, exploit, leave, or ask to be "
                    "involved. Be specific and unsentimental.\n"
                    "5. THE COST OF THEM KNOWING: the danger, burden or disappointment the knowledge would "
                    "bring them.\n"
                    "6. ONE HUMANISING DETAIL: a habit, a possession, a running complaint.\n\n"
                    "Then give me:\n"
                    "7. THE CONFIDANT QUESTION: whether my hero has one person who knows. If yes, say what "
                    "that person provides and what it costs them. If no, say what carries that narrative "
                    "function instead, because a hero with nobody gets monotonous fast.\n"
                    "8. THE REVEAL PLAN: who learns the truth during this book, in what order, and how each "
                    "reveal changes the story's shape.\n"
                    "9. THE HOSTAGE RISK: which of these people an antagonist would go after, and how my "
                    "hero has failed to protect against that.\n\n"
                    "End by asking me which supporting character the reader will love most, so I can decide "
                    "whether I am willing to put them in item 9."
                ),
                "pro_tip": (
                    "Fill the 'knows and my hero does not realise it' tier with at least one person. A "
                    "character who has quietly known for two years and said nothing, for their own reasons, "
                    "is worth more than any reveal you can engineer."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: ARCHITECT THE STORY",
        "intro": (
            "Now the machine. These four prompts build the crisis that starts the book, a beat sheet shaped "
            "for this genre's particular arc, a collateral ledger that keeps the fights from being free, "
            "and a set-piece generator built around geography and consequence rather than choreography."
        ),
        "prompts": [
            {
                "title": "The Crisis and the First Act",
                "desc": (
                    "Your book does not start with the origin - it starts when the arrangement my hero has "
                    "made with their own power stops working. This prompt finds that moment."
                ),
                "prompt_text": (
                    "You are a story architect for superhero and powered-world fiction.\n\n"
                    "My hero's civilian life and sustainability question: [PASTE FROM PROMPT 9]\n"
                    "My rogues gallery and book-one antagonist: [PASTE FROM PROMPT 11]\n"
                    "My institutional layer and public opinion: [FROM PROMPTS 5-6]\n\n"
                    "Build my FIRST ACT:\n\n"
                    "1. THE WORKING ARRANGEMENT: the opening scene showing how my hero currently manages "
                    "both lives - competent, tired, sustainable for now. Two paragraphs. Include one small "
                    "use of the power that costs them something.\n"
                    "2. THE CRISIS: the event that breaks the arrangement. Give me 4 options of increasing "
                    "severity - one personal, one public, one institutional, one from the rogues gallery - "
                    "then recommend one that fits my scale axis without spending it.\n"
                    "3. THE FIRST PUBLIC ACT: the moment the world sees my hero do something undeniable, "
                    "and the immediate press and official reaction, using the outlets from Prompt 6.\n"
                    "4. THE COST ARRIVES: who pays for that first act - a bystander, a building, a "
                    "colleague, a relationship, a legal exposure. It must be named and specific. This beat "
                    "is what separates superhero prose from a comic.\n"
                    "5. THE REFUSAL: what my hero tries in order to go back to the old arrangement, and why "
                    "it fails.\n"
                    "6. THE POINT OF NO RETURN: the moment the secret, the city or the antagonist makes "
                    "retreat impossible.\n"
                    "7. THE ACT ONE BEATS: 10-12 sequential beats from the opening image to the point of no "
                    "return, one sentence each, naming who is present and what changes.\n"
                    "8. THE DRAMATIC QUESTION: what act one asks, phrased as a yes/no the ending answers.\n\n"
                    "End by asking me what my hero loses in act one from their civilian life, and whether "
                    "they ever get it back."
                ),
                "pro_tip": (
                    "Item 4 is non-negotiable. Give the first heroic act a named victim - someone helped at "
                    "someone else's expense - and you have taught the reader in chapter three that this "
                    "book keeps accounts."
                ),
            },
            {
                "title": "The Full Beat Sheet",
                "desc": (
                    "This prompt maps the whole novel onto the genre's spine, tracking the heroic plot, the "
                    "identity plot and the public-opinion plot in step with each other."
                ),
                "prompt_text": (
                    "You are a story architect building a complete beat sheet for a superhero novel.\n\n"
                    "My first act: [PASTE FROM PROMPT 14]\n"
                    "My arch-enemy and their offer: [PASTE FROM PROMPT 12]\n"
                    "My supporting cast and reveal plan: [PASTE FROM PROMPT 13]\n"
                    "My public-opinion turn: [FROM PROMPT 6 ITEM 4]\n"
                    "My power's hard limits: [FROM PROMPT 2]\n"
                    "Target length: [E.G. 100,000 WORDS]\n\n"
                    "Build my BEAT SHEET across these stations. For each: 2-4 sentences, an approximate "
                    "word-count position, and which of the three threads it serves - the heroic plot, the "
                    "identity plot, or the public-opinion plot:\n\n"
                    "1. The Working Arrangement\n"
                    "2. The Crisis\n"
                    "3. The First Public Act, and the Cost\n"
                    "4. The Rogues Gallery Notices\n"
                    "5. The Institutional Response Tightens\n"
                    "6. The Identity Is Strained - a mundane near-miss from Prompt 9 item 6\n"
                    "7. Midpoint: The Arch-Enemy States the Argument and Makes the Offer\n"
                    "8. Public Opinion Turns\n"
                    "9. A Reveal - someone learns the truth, per Prompt 13 item 8\n"
                    "10. The Failure - the power is not enough, or is exactly the problem\n"
                    "11. All Is Lost - the hostage risk from Prompt 13 item 9 comes due\n"
                    "12. The Choice About What the Power Is For\n"
                    "13. The Confrontation, Won on Human Terms - not by a new ability\n"
                    "14. A Changed Rule, Publicly\n"
                    "15. The Life, Resumed and Altered\n\n"
                    "Then flag: any beat where I am relying on coincidence, any two beats doing the same "
                    "job, any stretch where one of the three threads goes dark for too long, and any place "
                    "the climax currently depends on my hero exceeding the hard limits from Prompt 2.\n\n"
                    "End by asking me whether beat 13 answers the arch-enemy's thesis or merely defeats "
                    "them, because readers can tell the difference."
                ),
                "pro_tip": (
                    "Beat 13 is where this genre most often cheats. If your hero wins by doing something "
                    "the power was never established to do, you have not written a climax - you have "
                    "written a deus ex machina in a cape."
                ),
            },
            {
                "title": "The Collateral Ledger",
                "desc": (
                    "Nothing in a superhero novel should be free. This prompt audits every fight and rescue "
                    "and assigns it a named cost, in money, bodies, reputation and relationships."
                ),
                "prompt_text": (
                    "You are a story editor auditing consequence in a superhero narrative. You are "
                    "unsentimental about damage.\n\n"
                    "My beat sheet: [PASTE FROM PROMPT 15]\n"
                    "My liability and insurance rules: [PASTE FROM PROMPT 5 ITEM 4]\n"
                    "My city's fight sites: [FROM PROMPT 8 ITEM 5]\n"
                    "My hero's monthly finances: [FROM PROMPT 9 ITEM 3]\n\n"
                    "Build my COLLATERAL LEDGER:\n\n"
                    "1. THE INCIDENTS: list every fight, rescue and public use of power across the novel.\n"
                    "2. THE PHYSICAL COST: for each, what was actually damaged - be specific about "
                    "buildings, vehicles, infrastructure - and who owned it.\n"
                    "3. THE HUMAN COST: for each incident, at least one named person affected who is not a "
                    "principal character. Give me their name, what happened to them, and whether my hero "
                    "ever learns about it.\n"
                    "4. THE FINANCIAL TRAIL: who pays, under my liability rules, and what that does to "
                    "public opinion and to my hero's own finances.\n"
                    "5. THE BODY COUNT: who dies in this book, at whose hands or through whose failure, and "
                    "what each death changes. Flag any death that is currently decorative.\n"
                    "6. THE HERO'S OWN DAMAGE: the cumulative physical toll across the novel, measured "
                    "against the cost structure from Prompt 2. Confirm they are not recovering faster than "
                    "my own rules allow.\n"
                    "7. THE RELATIONAL COST: what each incident costs in trust, missed obligations and lies "
                    "added to the ledger from Prompt 9.\n"
                    "8. THE PERMANENT MARKS: 5 things that cannot be undone by the last page.\n"
                    "9. THE THREE FREEST MOMENTS: the three places my story currently lets my hero off "
                    "without a cost, with a harder alternative for each.\n"
                    "10. THE RECKONING SCENE: identify the one chapter where my hero is forced to confront "
                    "the total of this ledger. If there is no such chapter, tell me where to put it.\n\n"
                    "End by asking me which named person from item 3 should come back in act three, because "
                    "a victim who returns is the strongest scene this genre can build."
                ),
                "pro_tip": (
                    "Run this ledger again after the first draft. Drafting brains hand out free rescues; "
                    "the second pass, where you make somebody pay for each one, is where the book stops "
                    "reading like a comic and starts reading like a novel."
                ),
            },
            {
                "title": "The Set-Piece Generator",
                "desc": (
                    "Reusable for every major sequence - a fight, a rescue, a chase, a siege, a public "
                    "confrontation. Built around geography, constraint and consequence rather than "
                    "blow-by-blow choreography."
                ),
                "prompt_text": (
                    "You are an action choreographer for prose fiction who builds sequences around decisions "
                    "and constraints, not moves.\n\n"
                    "My power, its limits, costs and counters: [PASTE FROM PROMPT 2]\n"
                    "My opponent for this sequence: [PASTE THE RELEVANT ENTRY FROM PROMPT 11 OR 12]\n"
                    "My city's fight sites: [FROM PROMPT 8]\n"
                    "The sequence I need: [E.G. A RESCUE UNDER A COLLAPSING STRUCTURE / A ROOFTOP PURSUIT / "
                    "A FIGHT IN A CROWDED PLACE / A SIEGE OF MY HERO'S HOME / A PUBLIC CONFRONTATION IN "
                    "FRONT OF CAMERAS]\n"
                    "Where it sits: [BEAT AND CHAPTER FROM PROMPT 15]\n\n"
                    "Design the sequence:\n\n"
                    "1. THE OBJECTIVE: what my hero is actually trying to achieve - specific and losable. "
                    "Not 'win'. Then state what the opponent wants, which should not be simply 'stop them'.\n"
                    "2. THE CIVILIAN PROBLEM: who else is in this space, how many, and what my hero has to "
                    "do about them. This constraint should shape every tactical choice.\n"
                    "3. THE GEOGRAPHY: the physical space in detail - what is load-bearing, what is "
                    "flammable, where the exits are, what the terrain does to my hero's power specifically.\n"
                    "4. THE CONSTRAINT STACK: which of my power's hard limits and costs bite during this "
                    "sequence, and at what point. This is the source of all tension - list them by beat.\n"
                    "5. THE TURN: how my hero's plan fails, in two stages - a first setback absorbed, then "
                    "the real one, which must come from an established limit rather than from luck.\n"
                    "6. THE BEATS: 12-16 sequential beats, one sentence each, with the cost clock noted - "
                    "energy, pain, time, structural integrity, how long the crowd has.\n"
                    "7. THE DECISION: the one moment in the middle where my hero must choose between the "
                    "objective and a person. Write it out.\n"
                    "8. THE PROSE PLAN: 3 sensations from inside my hero's body during this sequence that "
                    "will carry it on the page, since a reader cannot see a fight.\n"
                    "9. THE COST: what this sequence takes permanently, drawn from the ledger in Prompt 16, "
                    "including at least one named non-principal affected.\n"
                    "10. THE AFTER: the quiet scene immediately following, and the one thing said in it "
                    "that changes a relationship.\n\n"
                    "End by asking me whether my hero achieved the objective at item 1, because a sequence "
                    "where they win the fight and lose the objective is the strongest version of this scene."
                ),
                "pro_tip": (
                    "Item 7 is the reason the sequence exists. If your set piece has no moment where the "
                    "hero must abandon the mission to catch someone falling, it is exercise rather than "
                    "story - and readers skim exercise."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 5: WRITE THE BOOK",
        "intro": (
            "Four prompts, because this genre has one craft problem the others do not: a fight rendered in "
            "sentences instead of panels. You get a chapter outline, an opening chapter, the batch-drafting "
            "engine, and a dedicated action-prose pass."
        ),
        "prompts": [
            {
                "title": "Chapter Outline with Hooks",
                "desc": (
                    "This prompt converts your beat sheet and ledger into a chapter plan where every "
                    "chapter has a job, a turn, a cost, and a hook - and where the three threads stay in "
                    "balance."
                ),
                "prompt_text": (
                    "You are a novel outliner working in superhero and powered-world fiction.\n\n"
                    "My beat sheet: [PASTE FROM PROMPT 15]\n"
                    "My collateral ledger: [PASTE FROM PROMPT 16]\n"
                    "My set pieces: [LIST THOSE DESIGNED WITH PROMPT 17]\n"
                    "Target: [E.G. 100,000 WORDS IN 46 CHAPTERS OF ABOUT 2,200 WORDS]\n"
                    "Point of view: [FIRST PERSON PRESENT / THIRD LIMITED PAST / MULTI-POV - and who]\n\n"
                    "Build my CHAPTER OUTLINE. For every chapter give me:\n\n"
                    "1. Chapter number and working title.\n"
                    "2. POV character, location (using a district from Prompt 8), and whether my hero is "
                    "masked or unmasked in it.\n"
                    "3. The chapter's job in one sentence.\n"
                    "4. The turn: what is true at the end that was not true at the start.\n"
                    "5. Which thread it serves - heroic, identity, or public opinion.\n"
                    "6. The cost paid, drawn from the ledger, or 'none' if it is a breath chapter.\n"
                    "7. The closing hook, as a one-line description.\n\n"
                    "Then flag: any three consecutive chapters with my hero masked (the civilian life is "
                    "half the book), any stretch of more than four chapters without a cost, any two set "
                    "pieces sitting too close together, any chapter whose only job is to convey "
                    "information, and any thread that goes dark for more than five chapters.\n\n"
                    "End by asking me what my ratio of masked to unmasked chapters turned out to be, "
                    "because that number is the single best predictor of whether this reads as a novel or "
                    "as a comic script."
                ),
                "pro_tip": (
                    "Aim for more unmasked chapters than you instinctively want - somewhere near half. The "
                    "civilian scenes are what prose can do that the visual medium cannot, and they are what "
                    "readers quote back to you."
                ),
            },
            {
                "title": "The Opening Chapter",
                "desc": (
                    "This prompt drafts chapter one to show the arrangement and its cost before any "
                    "spectacle - the opening move that tells a reader this is a novel about a person, not a "
                    "highlight reel."
                ),
                "prompt_text": (
                    "You are a novelist drafting the opening chapter of a superhero novel in the voice "
                    "described below.\n\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET, PLUS NOTES ON "
                    "YOUR OWN STYLE]\n"
                    "My hero, civilian life and ledger of lies: [PASTE FROM PROMPTS 9 AND 3]\n"
                    "My power, its costs and one mundane use: [PASTE FROM PROMPT 2]\n"
                    "My city and district sensory kit: [FROM PROMPT 8]\n"
                    "My street-level details and slang: [FROM PROMPT 6]\n"
                    "POV and tense: [SPECIFY]\n"
                    "Target length: [E.G. 2,200-2,800 WORDS]\n\n"
                    "Write chapter one, following these rules:\n\n"
                    "1. Open in the civilian life, mid-task, with my hero managing something ordinary.\n"
                    "2. Show the power early but small - one of the mundane uses from Prompt 2 item 7 - and "
                    "let it cost something measurable.\n"
                    "3. Establish the dual life through a concrete logistical problem, not through "
                    "reflection: a shift, a lie, an injury that needs hiding, a bill.\n"
                    "4. Deliver the world's adjustment to powers as background texture only - signage, a "
                    "news item, a drill, a joke - never as explanation.\n"
                    "5. Use in-world slang from Prompt 6 in context, unexplained.\n"
                    "6. Give me nothing about the origin except one fragment a person would actually think "
                    "in passing.\n"
                    "7. Include one moment of warmth or humour.\n"
                    "8. Bring in the pressure that will become the crisis, at low volume.\n"
                    "9. End on the hook from my chapter outline.\n\n"
                    "After the chapter, list what a reader can infer about the power, the world and the "
                    "hero, and flag anything I explained that I should have implied.\n\n"
                    "End by asking me whether a reader who stopped here would care about this person "
                    "independent of the power, and what specifically would make them."
                ),
                "pro_tip": (
                    "Do not open with a rescue. The scene you want is a person late for work using "
                    "something extraordinary to solve something trivial - it establishes the power, the "
                    "cost, the tone and the character in one page, and it is the opening nobody else wrote."
                ),
            },
            {
                "title": "The Batch Drafting Engine",
                "desc": (
                    "The prompt you will reuse most. It drafts three to five chapters at a time while "
                    "holding voice, the power's cost accounting, the lie ledger, public opinion and the "
                    "collateral record steady."
                ),
                "prompt_text": (
                    "You are my drafting partner on a superhero novel. You write in my established voice "
                    "and hand control back to me at the end of every batch.\n\n"
                    "STANDING CONTEXT (reuse and update this block every batch):\n"
                    "- Voice sample: [PASTE 300-500 WORDS OF YOUR APPROVED CHAPTER ONE FROM PROMPT 19]\n"
                    "- Hero and arc stage: [FROM PROMPTS 3 AND 9, PLUS WHERE THEY ARE NOW]\n"
                    "- Power rules I must not break: [THE FIVE HARD LIMITS AND THE COST STRUCTURE FROM "
                    "PROMPT 2]\n"
                    "- Body state: [CURRENT INJURIES, EXHAUSTION LEVEL, WHAT IS STILL HEALING AND HOW LONG "
                    "MY OWN RULES SAY THAT TAKES]\n"
                    "- Civilian state: [JOB STANDING, MONEY, WHAT WAS MISSED, WHAT IS DUE]\n"
                    "- The lie ledger: [WHICH LIES ARE ACTIVE, WHICH ARE FRAYING - FROM PROMPT 9]\n"
                    "- Knowledge tiers: [WHO KNOWS, WHO SUSPECTS - FROM PROMPT 13]\n"
                    "- Public opinion: [WHERE IT STANDS AND WHAT LAST MOVED IT - FROM PROMPT 6]\n"
                    "- Collateral to date: [FROM PROMPT 16, INCLUDING NAMED PEOPLE AFFECTED]\n"
                    "- Elapsed time: [STATE IT]\n\n"
                    "THIS BATCH: write chapters [X] to [Y] from my outline:\n"
                    "[PASTE THE OUTLINE ENTRIES FROM PROMPT 18]\n\n"
                    "Rules for this batch:\n"
                    "1. Match the voice sample in rhythm, sentence length and level of interiority.\n"
                    "2. Never let the power exceed its hard limits or recover faster than its cost "
                    "structure allows.\n"
                    "3. Every chapter spends something specific - body, money, trust, standing, or a lie.\n"
                    "4. Masked and unmasked chapters should read in noticeably different registers.\n"
                    "5. Any public use of power generates a reaction - press, official, or neighbour.\n"
                    "6. Ground every large event in one named person standing in it.\n"
                    "7. End each chapter on its outlined hook.\n\n"
                    "After the chapters, give me a STATUS REPORT: body state, money, elapsed time, lies "
                    "added or broken, who now knows what, public opinion movement, collateral added, and "
                    "any promise you made on the page that I now owe the reader.\n\n"
                    "End by asking me which chapter drifted furthest from my voice, so the next batch does "
                    "not inherit the drift."
                ),
                "pro_tip": (
                    "Never skip the body state line. Injury amnesia - a hero with three broken ribs "
                    "sprinting two chapters later - is the single most common complaint about superhero "
                    "prose, and this one field prevents it."
                ),
            },
            {
                "title": "The Action-Prose Pass",
                "desc": (
                    "Fights in prose fail differently than fights in panels. This prompt rebuilds an action "
                    "sequence to run on decisions, sensation and stakes rather than blow-by-blow "
                    "choreography."
                ),
                "prompt_text": (
                    "You are a line editor who specialises in action prose, working on a superhero novel. "
                    "You are hostile to choreography that reads like camera directions.\n\n"
                    "My power, its costs and sensations: [PASTE FROM PROMPT 2]\n"
                    "My voice essentials: [PASTE FROM THIS PACK'S CHEAT SHEET]\n"
                    "The action chapter to edit: [PASTE ONE CHAPTER OR SEQUENCE]\n\n"
                    "Do an action-prose pass:\n\n"
                    "1. THE CHOREOGRAPHY AUDIT: flag every passage that is a sequence of physical moves "
                    "with no decision, sensation or stake between them. Show me how to compress three such "
                    "moves into one, and what to put in the space you save.\n"
                    "2. THE DECISION DENSITY: mark where my hero is choosing and where they are merely "
                    "reacting. Aim for a choice every half page; tell me where the gaps are.\n"
                    "3. THE COST ON THE PAGE: check that the power's price from Prompt 2 is felt in the "
                    "prose as it accrues - not stated afterwards. Rewrite one passage to demonstrate.\n"
                    "4. THE SENSATION PASS: replace three external descriptions with what it feels like "
                    "from inside my hero's body.\n"
                    "5. THE CLARITY TEST: after each of my paragraphs, state in one plain sentence what "
                    "just happened physically. Anywhere you cannot, the blocking is broken - flag it.\n"
                    "6. THE STAKES REMINDERS: find the places where a reader could lose track of what is "
                    "at risk, and give me a single-clause reminder for each that does not stop the scene.\n"
                    "7. THE RHYTHM MAP: check that sentences shorten at maximum danger and open up in the "
                    "pauses. Show me one rewritten paragraph.\n"
                    "8. THE CIVILIAN ANCHOR: confirm there is at least one named non-principal in the "
                    "sequence whose fate the reader is tracking. If not, tell me where to put them.\n"
                    "9. THE ENDING: check that the sequence ends on consequence rather than on the last "
                    "blow.\n\n"
                    "Return edits as a list - original line, proposed line, one-line reason. Do not rewrite "
                    "the chapter.\n\n"
                    "End by asking me which of your changes I rejected, so you can calibrate to my voice "
                    "for the next action chapter."
                ),
                "pro_tip": (
                    "Item 5 is brutal and worth it. If an editor cannot say plainly what happened in a "
                    "paragraph of your fight, no reader will picture it - and a blurry fight is worse than "
                    "a short one."
                ),
            },
        ],
    },

    {
        "name": "PHASE 6: POLISH, PUBLISH, EXPAND",
        "intro": (
            "Three prompts to finish: an audit of power logic and continuity, the retail kit, and series "
            "architecture built specifically around the power-creep problem that ends long superhero runs."
        ),
        "prompts": [
            {
                "title": "Power-Logic and Continuity Audit",
                "desc": (
                    "Readers of this genre reason about your power system for fun and will find every "
                    "breach. This prompt finds them first."
                ),
                "prompt_text": (
                    "You are a continuity editor who specialises in power systems and who is merciless "
                    "about abilities that solve problems they were never established to solve.\n\n"
                    "My power system, hard limits, costs and skill curve: [PASTE FROM PROMPT 2]\n"
                    "My institutional and legal rules: [PASTE FROM PROMPT 5]\n"
                    "My power tiers: [FROM PROMPT 7]\n"
                    "My collateral ledger: [FROM PROMPT 16]\n"
                    "My manuscript or detailed chapter summaries: [PASTE - WORK IN SECTIONS IF LONG]\n\n"
                    "Audit for the following, citing the chapter for every issue:\n\n"
                    "1. LIMIT BREACHES: every place the power does something the five hard limits forbid.\n"
                    "2. COST EVASION: every use that should have cost more than it did, and every recovery "
                    "faster than my own rules allow. Track injuries chapter by chapter.\n"
                    "3. THE COMPETENCE CURVE: does my hero learn only what the skill curve permits? Flag "
                    "any new ability that appears without setup, especially near the climax.\n"
                    "4. THE OBVIOUS SOLUTION PROBLEM: for each major obstacle, ask whether an established "
                    "power could have solved it trivially. Flag every place my hero should have won "
                    "instantly and did not.\n"
                    "5. TIER CONSISTENCY: do opponents perform at the level Prompt 7 assigns them?\n"
                    "6. INSTITUTIONAL CONSISTENCY: does the enforcement body act according to its stated "
                    "capability and politics, or become conveniently absent when my plot needs room?\n"
                    "7. THE SECRET'S INTEGRITY: track who knows what, when. Flag any character acting on "
                    "knowledge they should not have, and any near-miss the world should have followed up on "
                    "and did not.\n"
                    "8. COLLATERAL FOLLOW-THROUGH: does the damage from earlier chapters persist - the "
                    "rubble, the lawsuit, the injured person, the press cycle?\n"
                    "9. THE FREE LUNCH LIST: every gain with no price.\n\n"
                    "Rank findings CRITICAL, MODERATE or MINOR, with a fix for every CRITICAL item.\n\n"
                    "End by asking me which critical fix requires a structural change, so I can plan that "
                    "repair before touching the prose."
                ),
                "pro_tip": (
                    "Item 4 is the audit nobody runs and every reader performs. Half the plot holes in this "
                    "genre are not the hero doing too much - they are the hero inexplicably failing to do "
                    "something you already told us they could."
                ),
            },
            {
                "title": "Blurb, Metadata and Positioning",
                "desc": (
                    "Superhero prose has a shelving problem, so its retail copy has to work harder. This "
                    "prompt builds the whole kit, matched to the promise from Prompt 4."
                ),
                "prompt_text": (
                    "You are a book marketing copywriter specialising in genre fiction for adult readers, "
                    "with experience positioning superhero and powered-world prose.\n\n"
                    "My reader promise, pitches and recommended shelf: [PASTE FROM PROMPT 4]\n"
                    "My hero, power and wound: [PASTE FROM PROMPTS 2-3]\n"
                    "My arch-enemy's thesis: [FROM PROMPT 12]\n"
                    "My tone and scale placement: [FROM PROMPT 1]\n"
                    "My ending and what changed: [FROM PROMPT 15]\n\n"
                    "Build my retail kit:\n\n"
                    "1. THE BLURB: 150-200 words in three movements - the person and their power in two "
                    "sentences, the impossible position they are put in, the stakes and hook. Lead with the "
                    "person. Nothing past the midpoint.\n"
                    "2. TWO ALTERNATIVES: a punchy 100-word version, and one that leads with the cost "
                    "rather than the power.\n"
                    "3. THE HOOK LINE: three options for the line above the blurb.\n"
                    "4. THE TONE SIGNAL: tell me the specific words and phrasing choices in this blurb that "
                    "tell a reader where I sit on the four-color-to-deconstruction axis, so the right reader "
                    "self-selects. This matters more in this genre than in any other.\n"
                    "5. CATEGORIES: 6 retail categories ranked by how well I compete in each, given the "
                    "shelving question from Prompt 4.\n"
                    "6. KEYWORDS: 20 reader-search phrases grouped into trope, mood and situation terms.\n"
                    "7. COMP POSITIONING: 4 comparable reading and viewing experiences described as types "
                    "of work, each with a 'for readers who loved X but wanted Y' line.\n"
                    "8. THE COVER BRIEF: 5 visual directions tied to specific images from my book, plus 3 "
                    "clichés to forbid. Say whether a costumed figure should appear at all.\n"
                    "9. THE CONTENT NOTE: an honest, non-spoiling note on the darkness level, drawn from my "
                    "tone placement.\n\n"
                    "End by asking me which promise in the blurb I am least confident the book delivers, so "
                    "we can fix the blurb or fix the book."
                ),
                "pro_tip": (
                    "Item 4 is the one that sells this genre. Readers who want sincere heroism and readers "
                    "who want a teardown are both browsing the same shelf, and a blurb that signals clearly "
                    "gets fewer sales and far better reviews."
                ),
            },
            {
                "title": "Series Architecture and the Power-Creep Problem",
                "desc": (
                    "This genre is serial by nature and dies of escalation. This prompt designs the series "
                    "and commits you to escalating something other than power."
                ),
                "prompt_text": (
                    "You are a series architect for serial genre fiction, with specific expertise in why "
                    "long superhero runs collapse.\n\n"
                    "My book one, ending included: [PASTE FROM PROMPT 15]\n"
                    "My rogues gallery and who survived: [PASTE FROM PROMPT 11]\n"
                    "My arch-enemy's thesis and whether it was answered: [FROM PROMPT 12]\n"
                    "My power's skill curve and hard limits: [FROM PROMPT 2]\n"
                    "My surviving cast and knowledge tiers: [FROM PROMPT 13]\n"
                    "My scale ceiling: [FROM PROMPT 1 ITEM 2]\n\n"
                    "Design my SERIES:\n\n"
                    "1. THE SHAPE: recommend a shape and justify it against my ending - a trilogy with one "
                    "escalating conflict, an open-ended series with a rogue per book, or a generational or "
                    "ensemble mosaic.\n"
                    "2. THE SERIES QUESTION: the question the whole series answers, distinct from book "
                    "one's.\n"
                    "3. THE POWER-CREEP CONTRACT: this is the important one. State explicitly what my "
                    "hero's power will and will not become across the series. Then name 5 things I will "
                    "escalate INSTEAD of raw power - intimacy of the threat, institutional pressure, moral "
                    "compromise, the number of people depending on them, public exposure, the cost per use. "
                    "Commit to them in writing.\n"
                    "4. THE THREAT LADDER: how each book's antagonist is harder without being stronger. "
                    "Give me the specific mechanism per book.\n"
                    "5. THE IDENTITY CLOCK: how long the secret survives across the series, and what "
                    "happens to the books after it breaks. Plan this now - it is the single biggest "
                    "structural decision in a superhero series.\n"
                    "6. BOOK TWO: a one-page premise - the new pressure, the returning cost from book one, "
                    "the rogue promoted from the gallery, and a rupture in the first three chapters. It must "
                    "not undo book one's changed rule.\n"
                    "7. BOOK THREE AND BEYOND: a paragraph each, ending with the final image of the series.\n"
                    "8. THE SEEDS: 6 things planted or plantable in book one that pay off later - a rogue "
                    "left alive, a named collateral victim, an unanswered question, a supporting character "
                    "in the wrong knowledge tier, an institutional enemy, a debt.\n"
                    "9. THE STANDALONE GUARANTEE: confirm book one satisfies alone, and name anything in my "
                    "ending that reads as an unpaid promise rather than an open door.\n\n"
                    "End by asking me whether my hero keeps the power to the end of the series, because "
                    "that answer changes what I plant in book one."
                ),
                "pro_tip": (
                    "Item 3 is the difference between a series and a decline. Write the power-creep "
                    "contract, keep it visible, and when book four tempts you to add a new ability, "
                    "escalate the intimacy of the threat instead - move it closer to the people the reader "
                    "already loves."
                ),
            },
        ],
    },
]
