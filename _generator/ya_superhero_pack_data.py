# -*- coding: utf-8 -*-
"""
Royalti Studios - YA Superhero Master Prompt Pack (Young Adult Line,
grade 12 / upper YA).

Build with:
    python pack_builder.py ya_superhero_pack_data \
        "YA_Superhero_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "YA SUPERHERO",
    "total_prompts": 20,
    "hook_line": "Give a seventeen-year-old more power than the adults around them - in the one year they are supposed to be deciding who they become.",
    "keyword_lines": [
        "Powers at seventeen • Secret identity • Final year • Rivals • Chosen family",
        "Guardians who notice • School as cover • Registration • First real loss • Graduating anyway",
    ],
    "subgenres_line": "Subgenres: Bright Heroic, Street-Level Vigilante, Powered School Story, Team/Ensemble, Powered-World Social Fiction, Superhero Romance, Reluctant-Hero, Legacy Hero, Villain-Curious",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-21",
    "audience_line": "Young Adult Line",
    "reading_level": "Grade 12  |  Ages 17-18  |  Lexile 1010L+  |  Guided Reading X-Z+  |  Upper YA",
    "cover_h2": "From Origin Story to Finished Upper-YA Novel",
    "closing_tagline": "The mask is not the metaphor. Deciding who to be while everyone is watching - that is the metaphor.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "A YA superhero novel is not an adult one with a younger lead. The genre's central machinery - a "
        "secret identity, a power you did not ask for, a world that has opinions about you - lands "
        "differently on someone who is seventeen, still living under someone else's roof, and eight months "
        "from leaving. That is an enormous gift and this pack is built to use it: the dual life runs "
        "through school and guardians rather than a job and a mortgage, the institutional response has to "
        "deal with a minor, and the deadline is graduation. Grade 12 also means the content gates are wide "
        "- real romance, real violence, real grief, real moral failure - and the one unforgivable thing is "
        "condescension. Work the prompts in order and keep every output in one document. By Prompt 20 that "
        "document is your series bible."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-3) - Lock the lane. Place yourself on the tone and scale axes, build a power "
        "system with hard limits and real costs that arrived at the worst possible age, and lock the reader "
        "promise with grade-12 calibration.",
        "Phase 2 (Prompts 4-7) - Build the world that has powers and minors in it. The institutional "
        "response to a powered teenager, the school and the powered cohort inside it, the street and the "
        "press, and the town or city your hero actually protects.",
        "Phase 3 (Prompts 8-11) - Forge the cast. A protagonist with a declared intention and a graduation "
        "deadline, the guardians and family who are present and paying attention, the rival and the peer "
        "cohort, and the antagonist who is an argument - sorted by who knows.",
        "Phase 4 (Prompts 12-14) - Architect the story. The crisis and first act, a full beat sheet running "
        "the heroic, identity and coming-of-age threads against the school-year clock, and a set-piece "
        "generator.",
        "Phase 5 (Prompts 15-17) - Write the book. Chapter outline with hooks and a masked-to-unmasked "
        "balance, an opening chapter, and a batch-drafting engine that tracks body, lies, grades and "
        "guardians.",
        "Phase 6 (Prompts 18-20) - Polish, publish, expand. The grade-12 and power-logic audit, the blurb "
        "and metadata kit, and series architecture built around graduation and the escalation problem.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool and a place to save your outputs between prompts. Brackets like "
        "[THIS] are placeholders - replace them with your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular. Writing a solo hero with no powered peers? "
        "Prompt 6 becomes a light pass and Prompt 10 covers the rival only. Writing a legacy hero with a "
        "family already in the life? Prompt 9 becomes the most important prompt in the pack."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "A power that arrived at the worst possible age, when the character has the least control over their own life",
            "A secret identity that costs school, family trust and a relationship - things a seventeen-year-old cannot simply replace",
            "Guardians who are present, intelligent, and noticing - the adults must be real or the stakes are fake",
            "A hard power system whose limits the reader can reason about, and which never grows to solve a climax",
            "The final-year clock: applications, last seasons, scholarships, the scattering of a friend group",
            "A rival who wants the same thing and whose respect matters more than beating them",
            "Consequences that land on named people, including the ones your hero goes to school with",
            "A declared intention - the thing your protagonist says out loud that the plot then tests to destruction",
            "Content that trusts the reader: real intimacy, real grief, real failure, handled without flinching or leering",
            "An ending that resolves who this person has decided to be, even if the world is unfinished",
        ],
        "kills": [
            "Absent or idiot adults, which grade-12 readers read as a cheat - they are about to be adults themselves",
            "A secret identity with no cost, never nearly blown by anything as mundane as a group chat",
            "Powers that escalate whenever the plot needs them to, which makes the climax arbitrary",
            "School as set dressing - a building the hero leaves, with no teachers, workload or social consequence",
            "The chosen-one shortcut, which removes the one thing YA is actually about: choosing",
            "Teen dialogue built from googled slang, which dates the book inside a year",
            "Romance that pauses for the plot, or a love interest with no life of their own",
            "Collateral damage with no named victim and no lawsuit, insurance claim or grieving classmate",
            "Talking down - simplified sentences, explained themes, or a moral stated in the last chapter",
            "A first book that is all setup, betting on a sequel the reader has no reason yet to want",
        ],
        "voice": [
            "Close, unguarded interiority - at this age the inside of the head is louder than the outside world",
            "Full adult syntax; deliberate fragments and long spiralling sentences are both in range",
            "Let the character state convictions plainly, then let the narration undercut or complicate them",
            "Sensation over choreography in action - what the power does to the body, not what a camera would see",
            "Mundanity as ballast: the bus, the assignment, the shift, the sibling, the group chat",
            "Write teen voice from pressure and specificity rather than slang - what they fear dates better than how they talk",
            "Different registers masked and unmasked, and let the seam show",
            "Ration awe to two or three genuinely astonishing moments, and put one of them somewhere quiet",
        ],
        "formula": (
            "The Managed Year (a powered teenager, coping, final year beginning) -> The Crisis That Breaks "
            "the Arrangement -> The First Public Act, and the Cost -> The Declaration (what they say they "
            "will do) -> The Adults Respond (guardians, school, the state) -> The Rival Reframes the Goal "
            "-> The Identity Frays (a mundane near-miss) -> The Antagonist States the Argument and Makes an "
            "Offer -> Someone Learns the Truth -> The Failure (the power is not enough, or is the problem) "
            "-> The Person They Love Is On the Line -> The Choice About Who To Be -> Won by Understanding, "
            "Not by a New Ability -> Graduation, Altered"
        ),
        "reader_expectations": (
            "Grade-12 readers are months from adulthood and read a powered teenager as a story about "
            "themselves: too much responsibility, not enough authority, and a deadline. They want a power "
            "system they can reason about, adults who are real opponents and real allies, and a secret that "
            "genuinely damages a life they can recognise - friendships, college plans, a parent's trust. "
            "Content gates are wide; the line is exploitative framing, not subject matter. They will not "
            "forgive condescension, cardboard adults, slang that tries too hard, or a climax won by a power "
            "the book never established. What they reward: a rival they love, a promise kept at cost, a "
            "romance with two whole people in it, and a first book that actually ends."
        ),
        "level_spec": [
            "Band: Lexile 1010L+ / Guided Reading X-Z+ / grades 7-12 - this pack targets the TOP of that band",
            "Manuscript length: 75,000-95,000 words, 45-55 chapters of roughly 1,700-2,100 words",
            "Sentence craft: no ceiling - full adult syntax, fragments and long sentences both deliberate",
            "Vocabulary: unrestricted; no glossing, no explaining",
            "Protagonist age: 17-18. Readers of this band read up one or two years, never down",
            "Content in range (grade 12): on-page romance including implied intimacy, violence with real "
            "consequence, death and grief, addiction, self-harm handled responsibly, protagonist moral failure",
            "Content out of range: sexualised framing of teenage bodies, violence without consequence, a "
            "world where competent adults conveniently do not exist",
        ],
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "Every superhero story is about power arriving before wisdom, which is why the genre belongs to "
        "seventeen-year-olds more honestly than it belongs to anyone else. Your protagonist has more force "
        "than the adults in the room and less standing than any of them, and that gap is the whole novel - "
        "you do not need to invent tension on top of it. When a chapter feels weightless, check three "
        "things: does the power still cost what Prompt 2 said it costs, is there a named person paying for "
        "the last rescue, and has anyone's guardian noticed anything. Fix any one of those and the chapter "
        "stands up. Your readers are eighteen and deciding who to be while everybody watches. Take that as "
        "seriously as they do."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: LOCK THE LANE",
        "intro": (
            "Three prompts to set the contract: where you sit in a genre that runs from bright heroism to "
            "bitter deconstruction, a power system with limits you will not break, and the market position "
            "for a grade-12 reader who is months from adulthood."
        ),
        "prompts": [
            {
                "title": "Lock Your Lane and Your Scale",
                "desc": (
                    "The tonal range here is enormous and readers of one end reject the other. This prompt "
                    "places you deliberately and names the specific trap of a YA book at your position."
                ),
                "prompt_text": (
                    "You are a developmental editor who has worked on young adult speculative fiction for "
                    "fifteen years and knows the superhero space specifically.\n\n"
                    "My rough idea is: [DESCRIBE IN 2-4 SENTENCES - a power, a character, an image, "
                    "whatever I have]\n\n"
                    "Do the following:\n\n"
                    "1. Place my idea on the TONE AXIS from 1 to 10, where 1 = bright heroism that works "
                    "and 10 = full deconstruction where heroism is a lie. Explain in 3-4 sentences.\n"
                    "2. Place me on the SCALE AXIS from 1 to 10, where 1 = one school and one "
                    "neighbourhood and 10 = world-ending. Then tell me honestly: for a YA novel, what does "
                    "a score above 7 cost me in intimacy, and is it worth it?\n"
                    "3. Name my primary subgenre and two secondaries from: bright heroic, street-level "
                    "vigilante, powered school story, team ensemble, powered-world social fiction, "
                    "superhero romance, reluctant hero, legacy hero, villain-curious. Justify each.\n"
                    "4. THE YA OBLIGATION: name the three things this genre gains by having a "
                    "seventeen-year-old lead - the things an adult version of my story could not do - and "
                    "tell me which one my idea is currently wasting.\n"
                    "5. THE AGE TRAP: warn me about the specific failure mode of a YA superhero book at my "
                    "tone score. For a low score, the risk is writing down to readers. For a high score, "
                    "the risk is nihilism that a seventeen-year-old reader has no use for. Be specific to "
                    "my idea.\n"
                    "6. THE ADULT QUESTION: state plainly what the adults in my world are doing about all "
                    "this, in one paragraph. If my answer is 'nothing' or 'they don't know', tell me why "
                    "grade-12 readers will reject that and how to fix it.\n"
                    "7. Write my LANE STATEMENT in two sentences: what kind of YA superhero book this is "
                    "and what it believes about power.\n\n"
                    "End by asking me what my protagonist is supposed to be doing with this year of their "
                    "life instead, because that is the cost of the whole plot."
                ),
                "pro_tip": (
                    "Item 6 is the one writers skip and grade-12 readers punish. A world where capable "
                    "adults exist, notice, and have their own plan is harder to write and twice as tense - "
                    "your hero then has to work around people who love them."
                ),
            },
            {
                "title": "The Power System and Its Hard Limits",
                "desc": (
                    "A power with no rules makes every climax arbitrary. This prompt builds the system with "
                    "costs and limits, and ties the power specifically to the body and life of someone "
                    "seventeen."
                ),
                "prompt_text": (
                    "You are a systems designer who builds rigorous power systems for fiction and who is "
                    "hostile to hand-waving.\n\n"
                    "My lane statement: [PASTE FROM PROMPT 1]\n"
                    "My hero's power, roughly: [DESCRIBE, or say 'you choose']\n\n"
                    "Build my POWER SYSTEM:\n\n"
                    "1. THE MECHANISM: what the power does, in three plain sentences, no mystical vagueness.\n"
                    "2. THE FIVE HARD LIMITS: things it can never do. Write them as rules I may not break "
                    "for plot convenience. At least one should be inconvenient rather than dramatic.\n"
                    "3. THE COST: what using it takes - calories, pain, sleep, memory, hearing, time. Give "
                    "the cost at three levels (casual, hard, everything they have) with recovery times.\n"
                    "4. THE TEENAGE BODY: how the cost interacts with being seventeen specifically - a "
                    "growing body, a school timetable, no money, no privacy, a parent who notices bruises, "
                    "a coach who notices exhaustion. Give me 5 concrete collisions.\n"
                    "5. THE SKILL CURVE: what they can do now, what practice would unlock during this book, "
                    "and what is permanently out of reach. State plainly what they will NOT learn, so I "
                    "cannot cheat the climax.\n"
                    "6. THE FAILURE MODES: 5 ways it goes wrong - misfires, overreach, side effects, "
                    "something it does that they did not ask for.\n"
                    "7. THE COUNTERS: 5 ways an unpowered adult could stop my hero. If there are none, the "
                    "power is broken - redesign it and say why.\n"
                    "8. THE MUNDANE USES: 4 ways this power makes teenage life easier or worse in ways "
                    "unrelated to fighting. This is where readers fall in love with a power.\n"
                    "9. THE SIGNATURE MOMENT: the one use that will be the image readers remember.\n\n"
                    "End by asking me which hard limit my hero will try hardest to break, because that "
                    "attempt is a whole act of the book."
                ),
                "pro_tip": (
                    "Item 4 is what makes this a YA power system rather than a generic one. A hero who "
                    "cannot explain the nosebleeds to their mother is in more trouble than one being "
                    "hunted by an agency."
                ),
            },
            {
                "title": "Reader Promise, Grade-12 Calibration & Shelf",
                "desc": (
                    "This prompt sets the market position and, critically, calibrates content and voice for "
                    "readers aged 17-18 - the top of YA, where the gates are wide and condescension is "
                    "fatal."
                ),
                "prompt_text": (
                    "You are a publishing strategist positioning young adult fiction, with specific "
                    "experience at the upper end of the age band.\n\n"
                    "My lane statement and axis placement: [PASTE FROM PROMPT 1]\n"
                    "My power system: [PASTE FROM PROMPT 2]\n\n"
                    "Do the following:\n\n"
                    "1. Write my READER PROMISE in one paragraph, in the second person ('You will feel...').\n"
                    "2. Identify the 3 reader appeals I am leading with, from: power fantasy and agency, "
                    "romance, found family, moral dilemma, identity and becoming, rivalry, social "
                    "commentary, the cost of responsibility, mystery.\n"
                    "3. THE GRADE-12 CALIBRATION: given a target reader of 17-18, tell me specifically "
                    "what is in range and what is not. Cover romance and intimacy, violence, death, "
                    "substance use, self-harm, swearing, and protagonist moral failure. For each, state "
                    "the range and the framing that would take it out of range.\n"
                    "4. THE UPPER-YA POSITION: tell me honestly whether this book sits as upper YA or is "
                    "actually crossover-adult, and what to change if I want it read by both. Name the "
                    "three markers that signal upper YA rather than adult on the page.\n"
                    "5. THE CONDESCENSION AUDIT: list the 6 ways YA superhero manuscripts talk down to "
                    "readers, and give me an early warning sign for each in my own drafting.\n"
                    "6. Write 3 one-line pitches: one leading with the power, one with the cost, one with "
                    "the relationship.\n"
                    "7. CATEGORIES AND PROMISES: 5 retail categories ranked, plus the 4 promises I must "
                    "not break with the one-star review each breach would generate.\n"
                    "8. THE ORIGINALITY CHECK: name the 5 most familiar elements in my concept and one "
                    "specific way to make each mine.\n\n"
                    "End by asking me whether I am willing to let my protagonist do something genuinely "
                    "unforgivable, because at this age band that is allowed and it changes the book."
                ),
                "pro_tip": (
                    "Item 3 is not a restriction list, it is a targeting tool. Knowing exactly how far your "
                    "book goes lets you signal it in the blurb, which gets you the right readers and "
                    "spares you the reviews from the wrong ones."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: BUILD THE WORLD THAT HAS POWERS AND MINORS IN IT",
        "intro": (
            "A world with powered teenagers in it has built things an adult-focused world has not: "
            "programmes, consent forms, school policies, a guardian's legal position. These four prompts "
            "build that machinery, the school it runs through, the public that has opinions, and the "
            "territory your hero actually defends."
        ),
        "prompts": [
            {
                "title": "The Institutional Response to a Powered Minor",
                "desc": (
                    "This is the prompt that makes a YA superhero world specific. A state that discovers a "
                    "powered sixteen-year-old does something quite different from what it does with an "
                    "adult - and that difference is your plot."
                ),
                "prompt_text": (
                    "You are a worldbuilding consultant with a background in law, education policy and "
                    "child welfare, advising on a world where some people have superhuman abilities and "
                    "some of them are minors.\n\n"
                    "My power system: [PASTE FROM PROMPT 2]\n"
                    "My lane and scale: [FROM PROMPT 1]\n"
                    "How long powers have existed publicly: [SPECIFY - 5 YEARS, 40 YEARS, GENERATIONS, OR "
                    "'STILL SECRET']\n\n"
                    "Build my INSTITUTIONAL LAYER, with the minor question at the centre:\n\n"
                    "1. THE LEGAL STATUS: is having powers registered, licensed, criminalised, protected, "
                    "or unaddressed? Then answer separately: what changes when the powered person is under "
                    "eighteen?\n"
                    "2. THE GUARDIAN'S POSITION: what a parent or guardian is legally required to do, what "
                    "they lose if they conceal it, and what the state can do to a family. This is enormous "
                    "leverage on my plot - be specific.\n"
                    "3. THE SCHOOL'S OBLIGATION: what a school must do about a powered student. Policy, "
                    "disclosure, separate provision, exclusion, an accommodation plan. Include the "
                    "paperwork.\n"
                    "4. THE PROGRAMME: is there a training or containment programme for powered minors? "
                    "Describe it, who runs it, what it promises, what it actually is, and who has gone "
                    "missing from it.\n"
                    "5. VIGILANTISM BY A MINOR: what charge my hero faces if identified, how it differs "
                    "from an adult's, and who would be held responsible alongside them.\n"
                    "6. LIABILITY: who pays when a powered seventeen-year-old destroys property. The "
                    "family? A fund? Nobody? This single answer decides how the neighbourhood feels.\n"
                    "7. THE SEAMS: 5 places this system fails or cannot reach - where my plot runs.\n"
                    "8. THE PAPERWORK: 6 specific documents, forms or bureaucratic phrases that exist "
                    "because powered minors exist. Institutional texture sells a world faster than action.\n\n"
                    "End by asking me whether my hero's guardian has signed any of these forms, and "
                    "whether my hero knows."
                ),
                "pro_tip": (
                    "Item 2 is the engine of the whole subgenre. A hero whose heroics could cost their "
                    "mother custody, a job or a prosecution is in a bind no adult hero can be in - and it "
                    "is entirely made of love."
                ),
            },
            {
                "title": "The School and the Powered Cohort",
                "desc": (
                    "School is the container that holds a YA cast. This prompt builds it as a real "
                    "institution with workload and social physics, plus the other powered kids inside it."
                ),
                "prompt_text": (
                    "You are a consultant on secondary-school settings and adolescent social dynamics, "
                    "advising on a novel where some students have powers.\n\n"
                    "My institutional layer: [PASTE FROM PROMPT 4]\n"
                    "My hero's power: [FROM PROMPT 2]\n"
                    "Type of school and place: [DESCRIBE OR SAY 'YOU CHOOSE']\n\n"
                    "Build my SCHOOL:\n\n"
                    "1. THE INSTITUTION: name, size, funding, reputation, what it is good at, what it "
                    "neglects, and what kind of adult runs it.\n"
                    "2. THE FINAL-YEAR PRESSURE: the actual calendar of a grade-12 year here - "
                    "applications, exams, deadlines, last seasons, the events everyone is counting down to. "
                    "Give me 8 dated pressure points I can hang plot on.\n"
                    "3. THE WORKLOAD: what my hero owes academically, what happens if they fail it, and "
                    "what they are giving up by patrolling instead. Name the specific consequence.\n"
                    "4. THE SOCIAL PHYSICS: the groups, the hierarchy, where my hero sits, and the two "
                    "people whose opinion of them actually matters.\n"
                    "5. THE STAFF: 4 adults who work here. For each: what they teach or do, what they have "
                    "noticed about my hero, and whether they would help or report. At least one must be "
                    "genuinely perceptive.\n"
                    "6. THE POWERED COHORT: 4 other powered students. For each: name, power, whether it is "
                    "known, how they are handling it, and their relationship to my hero. At least one "
                    "should be handling it better and one much worse.\n"
                    "7. THE SCHOOL'S RESPONSE IN PRACTICE: how policy from Prompt 4 item 3 actually plays "
                    "out day to day - the drills, the exemptions, the rumours, the quiet accommodations.\n"
                    "8. THE SENSORY KIT: 6 specific details of this school - a smell, a sound, a place "
                    "people go to be unseen, a notice board, a broken thing nobody fixes.\n\n"
                    "End by asking me which powered classmate my hero will need and resent, because that "
                    "relationship carries a subplot."
                ),
                "pro_tip": (
                    "Item 3 is where most YA superhero books cheat. If patrolling costs nothing academically "
                    "- no failed assignment, no lost scholarship, no dropped place on a team - then the "
                    "heroics are free, and free heroics have no stakes at seventeen."
                ),
            },
            {
                "title": "The Street and the Press",
                "desc": (
                    "How the public and media treat a powered teenager specifically - which is not how they "
                    "treat an adult hero. This prompt builds opinion, coverage, and the turn."
                ),
                "prompt_text": (
                    "You are a consultant on media and public opinion in a world with superhuman people, "
                    "focused on how the public treats powered young people.\n\n"
                    "My institutional layer: [PASTE FROM PROMPT 4]\n"
                    "My school and town: [FROM PROMPT 5]\n\n"
                    "Build my PUBLIC LAYER:\n\n"
                    "1. THE ORDINARY ADJUSTMENTS: 8 mundane, specific ways daily life differs because "
                    "powered people exist - drills, signage, insurance, apps, prices, jokes, precautions.\n"
                    "2. THE MEDIA: 3 outlets or channels with distinct angles - one sensational, one "
                    "serious, one hostile. Give me each one's headline about my hero's first public act.\n"
                    "3. THE MINOR ANGLE: how coverage changes when the public learns the hero is a "
                    "teenager. Sympathy, outrage on their behalf, outrage at whoever let them, "
                    "infantilising, exploitation. Pick the dominant note and say why.\n"
                    "4. THE SOCIAL LAYER: how my hero's own age group talks about powered heroes online "
                    "and at school - accounts, group chats, edits, jokes, a fan account that gets too "
                    "close. Be specific and current-feeling without naming real platforms.\n"
                    "5. PUBLIC OPINION NOW: the split on powered people, the lines it falls along, and the "
                    "event that last moved it.\n"
                    "6. THE TURN: what would turn opinion against my hero specifically. Design it now - I "
                    "will use it in act two.\n"
                    "7. THE SLANG: 10 terms people use for powered individuals, heroics, collateral damage "
                    "and the unpowered - neutral, affectionate and cruel, and who uses which.\n"
                    "8. THE UNPOWERED VIEW: a paragraph in the voice of an adult neighbour who has lived "
                    "through three of these incidents and is tired.\n\n"
                    "End by asking me which of these public details my hero finds most humiliating, "
                    "because that friction is character."
                ),
                "pro_tip": (
                    "Item 4 is the piece an adult-focused pack cannot give you. A fan account that has "
                    "worked out which school the hero attends is a slow, mundane, entirely modern horror."
                ),
            },
            {
                "title": "The Territory",
                "desc": (
                    "A seventeen-year-old without a car protects what they can reach. This prompt builds "
                    "the place and narrows the hero's real patch until the stakes become legible."
                ),
                "prompt_text": (
                    "You are a setting specialist making a town or city district feel like a specific "
                    "place rather than generic backdrop.\n\n"
                    "My school and public layer: [PASTE FROM PROMPTS 5-6]\n"
                    "My hero's power and how they move: [FROM PROMPT 2]\n"
                    "Place it resembles, if any: [SPECIFY OR SAY 'YOU CHOOSE']\n\n"
                    "Build my SETTING:\n\n"
                    "1. THE IDENTITY: what this place is for, what built it, who lives there now, what it "
                    "is proud of and ashamed of. Two paragraphs.\n"
                    "2. THE REACH PROBLEM: given my hero's power, age, money and curfew, how far can they "
                    "actually get and how fast? Be concrete - bus routes, a bike, a lift from a friend, "
                    "their own power. This constraint is a gift; do not soften it.\n"
                    "3. THE FIVE PLACES: name and describe 5 locations in a paragraph each - who is there, "
                    "what it smells like, its landmark, what kind of trouble happens there. At least two "
                    "must be places teenagers actually go.\n"
                    "4. THE HERO'S PATCH: the specific few blocks or the one neighbourhood they really "
                    "protect, and why those. A hero guarding a whole city guards nowhere.\n"
                    "5. THE FIGHT SITES: 5 locations where a set piece could happen, each with a reason "
                    "the geography is interesting and a reason a fight there would be a disaster for "
                    "someone named.\n"
                    "6. THE SANCTUARY: the place my hero goes to be nobody. One paragraph, and it must not "
                    "be a lair - at this age it is somebody's garage, a roof, a bus at the end of its line.\n"
                    "7. THE SENSORY KIT: for each location, one sound, one smell and one visual that "
                    "identifies it with no location tag.\n"
                    "8. THE ANTI-GENERIC PASS: the 8 most overused superhero-setting images, with a "
                    "specific replacement for each from the material above.\n\n"
                    "End by asking me what my hero would lose if this place changed, since that is what "
                    "they are actually defending."
                ),
                "pro_tip": (
                    "Item 2 is the best constraint in YA superhero fiction and writers keep handing it "
                    "away. A hero who has to be home by eleven, and who cannot explain why they were not, "
                    "generates plot for free."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: FORGE THE CAST",
        "intro": (
            "Four prompts, and the second one is the one that separates YA from adult: the guardians. A "
            "powered teenager's hardest opponent is usually someone who loves them and is paying "
            "attention."
        ),
        "prompts": [
            {
                "title": "The Protagonist, the Declaration and the Deadline",
                "desc": (
                    "This prompt builds a hero whose origin is a wound, whose conviction is stated out "
                    "loud, and whose final year is being spent on this instead of on their own future."
                ),
                "prompt_text": (
                    "You are a character-development editor for young adult fiction.\n\n"
                    "My power, its costs and teenage collisions: [PASTE FROM PROMPT 2]\n"
                    "My school and its final-year pressure points: [PASTE FROM PROMPT 5]\n"
                    "My institutional layer: [FROM PROMPT 4]\n"
                    "My rough protagonist idea: [DESCRIBE, or say 'you choose']\n\n"
                    "Build my PROTAGONIST:\n\n"
                    "1. THE BASICS: name, age (17 or 18), who they live with, what their room is like, what "
                    "they do outside school, what money they have.\n"
                    "2. THE ORIGIN AS A WOUND: how the power arrived, and what they lost, failed at, or "
                    "were subjected to around it. Three sentences. Then explain how the power and the wound "
                    "rhyme - if they do not, redesign one and say which.\n"
                    "3. THE FIRST USE: the first time they used it, what went wrong, and what it taught "
                    "them to fear about themselves.\n"
                    "4. THE DECLARATION: the thing they say out loud about what they are going to do. Give "
                    "me the exact wording in their voice. The book will test it to destruction.\n"
                    "5. THE LIE UNDERNEATH: the sentence they tell themselves about why they really do "
                    "this, which the declaration is covering for.\n"
                    "6. THE STOLEN YEAR: what this protagonist was supposed to be doing with grade 12 - "
                    "the application, the audition, the season, the job, the plan with a friend. Name it "
                    "precisely, and name who else was counting on it.\n"
                    "7. THE COMPETENCE MAP: 3 things they are genuinely good at, 3 they are dangerously bad "
                    "at, and one skill that will matter more than they think.\n"
                    "8. THE ARC: 5 stages from where they start to where they end, each triggered by an "
                    "external event rather than a change of heart. At least one must be a step backwards.\n"
                    "9. THE ANCHOR: the person they will not risk. The antagonist will put them on the "
                    "table.\n\n"
                    "End by asking me whether my protagonist gets the stolen year back, because that "
                    "answer is the book's argument about whether any of this was worth it."
                ),
                "pro_tip": (
                    "Item 6 is the YA version of collateral damage. The cost that hurts a "
                    "seventeen-year-old reader most is not a broken city - it is the audition they missed "
                    "and cannot reschedule."
                ),
            },
            {
                "title": "Guardians, Family and the Adults Who Notice",
                "desc": (
                    "The single biggest difference between YA and adult superhero fiction. This prompt "
                    "builds adults who are present, competent and loving - which makes them the hardest "
                    "obstacle in the book."
                ),
                "prompt_text": (
                    "You are a character editor who specialises in parents and guardians in young adult "
                    "fiction, and who believes absent or stupid adults are the genre's laziest habit.\n\n"
                    "My protagonist: [PASTE FROM PROMPT 8]\n"
                    "The guardian's legal position: [PASTE FROM PROMPT 4 ITEM 2]\n"
                    "My hero's power costs and physical evidence: [FROM PROMPT 2]\n\n"
                    "Build my HOME:\n\n"
                    "1. THE HOUSEHOLD: who my protagonist lives with, the actual arrangement, the money "
                    "situation, and what the rules of the house are.\n"
                    "2. THE GUARDIANS: for each adult responsible for my hero - name, work, what they are "
                    "afraid of, what they want for my hero, and their single blind spot. None may be "
                    "stupid, and at most one may be absent, with a reason that costs something.\n"
                    "3. WHAT THEY HAVE NOTICED: a specific, itemised list of 8 things the adults in this "
                    "house have observed - hours, injuries, laundry, appetite, grades, mood, a missing "
                    "jacket, a lie that did not hold. Then state what they currently believe is going on, "
                    "which should be plausible and wrong.\n"
                    "4. THE WORSE EXPLANATION: what a loving, intelligent guardian would actually conclude "
                    "from that evidence - drugs, an abusive relationship, self-harm, a criminal job. This "
                    "misreading is one of the strongest engines available to me; develop it.\n"
                    "5. THE SIBLING OR EQUIVALENT: if there is one, what they know, what they want, and "
                    "what they would trade it for.\n"
                    "6. THE CONFRONTATION: script the beats of the scene where a guardian confronts my hero "
                    "with the evidence from item 3. Do not write the dialogue - give me the 8 beats and "
                    "what each side is protecting.\n"
                    "7. THE DISCLOSURE DECISION: the case for telling them and the case against, each in "
                    "its strongest form. Then tell me what telling them would actually cost the guardian, "
                    "legally and personally, using Prompt 4.\n"
                    "8. THE ALLY ADULT: one adult somewhere in my hero's life who could be told and would "
                    "help. Say who, what they can offer, and what it costs them. A book with no such adult "
                    "reads as fantasy to grade-12 readers.\n\n"
                    "End by asking me whether the guardians learn the truth during this book, because that "
                    "single decision reshapes the whole second half."
                ),
                "pro_tip": (
                    "Item 4 is the most powerful thing in this pack. A mother who has quietly concluded her "
                    "child is being hurt by someone, and is acting on that belief with love and "
                    "competence, will generate more tension than any villain you can design."
                ),
            },
            {
                "title": "The Rival and the Peer Cohort",
                "desc": (
                    "In YA the rival matters more than the villain. This prompt builds someone chasing the "
                    "same thing whose respect your hero wants, plus the peer group and the love interest."
                ),
                "prompt_text": (
                    "You are an ensemble developer for young adult fiction.\n\n"
                    "My protagonist and their declaration: [PASTE FROM PROMPT 8]\n"
                    "My powered cohort from school: [PASTE FROM PROMPT 5 ITEM 6]\n"
                    "My power tiers and limits: [FROM PROMPT 2]\n\n"
                    "Build my PEER LAYER:\n\n"
                    "1. THE RIVAL: name, power or method, and the crucial detail - they want the same thing "
                    "my hero wants, for reasons that are not worse. Describe what they are better at, what "
                    "they are wrong about, and why my hero wants their respect specifically.\n"
                    "2. THE RIVAL'S ARGUMENT: 150 words in their voice on why my hero is doing this wrong. "
                    "It must contain one thing my hero is genuinely getting wrong.\n"
                    "3. THE RIVAL'S ARC: how the relationship changes across the book. It must not resolve "
                    "into simple friendship or simple enmity - give me the third option.\n"
                    "4. THE CREW: 3-4 friends or teammates. For each: name, what they bring, their opinion "
                    "of what my hero is doing, and the pressure that would make them break or tell. At "
                    "least one must not know about the powers.\n"
                    "5. THE LOVE INTEREST, IF ANY: who, what they want out of their own life, and the "
                    "specific way the secret deforms the relationship. They must have a plot of their own "
                    "that would exist without my hero.\n"
                    "6. THE KNOWLEDGE TIERS: sort every character here into knows, suspects, has no idea, "
                    "or knows and my hero does not realise it. Fill that last tier with at least one "
                    "person.\n"
                    "7. THE GROUP CHAT: what these people say to each other when my hero is not reading, "
                    "and the one message that will matter later.\n"
                    "8. THE SCATTERING: where each of these people is going after graduation, and which "
                    "goodbye is already coming. This is the clock under every friendship scene.\n\n"
                    "End by asking me which friend the reader will love most, so I can decide whether I am "
                    "willing to put them in danger."
                ),
                "pro_tip": (
                    "Item 3 is the hard one and the good one. The best YA rivalries end somewhere between "
                    "friendship and enmity - two people permanently important to each other who will never "
                    "quite be on the same side."
                ),
            },
            {
                "title": "The Antagonist as Argument",
                "desc": (
                    "One antagonist, built as a thesis rather than a threat - and at this age band, often "
                    "someone offering your hero a genuinely better deal than heroism."
                ),
                "prompt_text": (
                    "You are an editor who specialises in antagonists that function as arguments.\n\n"
                    "My protagonist's declaration, lie and wound: [PASTE FROM PROMPT 8]\n"
                    "My institutional layer and its programme: [PASTE FROM PROMPT 4]\n"
                    "My rival: [FROM PROMPT 10]\n"
                    "My tone axis placement: [FROM PROMPT 1]\n\n"
                    "Build my ANTAGONIST:\n\n"
                    "1. THE THESIS: one sentence stating the claim about power that this person embodies "
                    "and my hero cannot yet refute.\n"
                    "2. THE PERSON: name, age, what they were before, how they arrived at the thesis, how "
                    "they speak, what they are genuinely good at. Consider making them an adult who was "
                    "once a powered teenager and was failed by the system in Prompt 4.\n"
                    "3. THE PARALLEL: how their history rhymes with my hero's - same wound, different "
                    "conclusion. Make the divergence a specific choice.\n"
                    "4. THE ARGUMENT, IN FULL: 200 words in their voice at their most persuasive, "
                    "containing one point my hero is currently living as a hypocrite about.\n"
                    "5. THE OFFER: what they offer my hero at the midpoint. At this age it should be "
                    "genuinely attractive - safety, an explanation, the stolen year back from Prompt 8 item "
                    "6, an adult who finally tells them the truth, a way out from under the guardians. "
                    "Write the offer in their words.\n"
                    "6. THE METHOD: what they actually do. Their acts must follow from the thesis.\n"
                    "7. THE LINE THEY CROSS: the act where reader sympathy must break. Name it and place "
                    "it in the story.\n"
                    "8. THE SECONDARY OPPOSITION: two lesser antagonists - one a peer, one institutional - "
                    "each pressing a different part of my hero than the main antagonist does.\n"
                    "9. THE REBUTTAL: what my hero must be able to say or do by the end that answers the "
                    "thesis. If I cannot answer it, my ending is a fudge - tell me plainly.\n\n"
                    "End by asking me whether my antagonist is right about something my hero is wrong "
                    "about, and whether the book is brave enough to say so."
                ),
                "pro_tip": (
                    "Item 5 is the YA masterstroke. An antagonist who offers a tired seventeen-year-old the "
                    "chance to stop carrying this, and means it, is harder to refuse than any threat - and "
                    "the refusal is the whole character arc."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: ARCHITECT THE STORY",
        "intro": (
            "Three prompts to build the machine: the crisis that breaks the arrangement, a beat sheet "
            "running three threads against the school-year calendar, and a reusable set-piece generator "
            "built on constraint rather than choreography."
        ),
        "prompts": [
            {
                "title": "The Crisis and the First Act",
                "desc": (
                    "The book starts when the arrangement my hero has made with their own power stops "
                    "working. This prompt finds that moment and builds act one around it."
                ),
                "prompt_text": (
                    "You are a story architect for young adult speculative fiction.\n\n"
                    "My protagonist and their stolen year: [PASTE FROM PROMPT 8]\n"
                    "My guardians and what they have noticed: [PASTE FROM PROMPT 9]\n"
                    "My school calendar: [PASTE FROM PROMPT 5 ITEM 2]\n"
                    "My antagonist: [FROM PROMPT 11]\n\n"
                    "Build my FIRST ACT:\n\n"
                    "1. THE ARRANGEMENT: the opening scene showing how my hero currently manages school, "
                    "home and the power - competent, tired, sustainable for now. Two paragraphs. Include "
                    "one small use of the power that costs something measurable.\n"
                    "2. THE CRISIS: the event that breaks it. Give me 4 options - one personal, one at "
                    "school, one institutional, one from the antagonist - then recommend one that fits my "
                    "scale axis without spending it.\n"
                    "3. THE FIRST PUBLIC ACT: the moment the world sees my hero do something undeniable, "
                    "and the immediate reaction from the press, the school and the state.\n"
                    "4. THE COST ARRIVES: who pays. It must be named and specific, and at least one "
                    "consequence must land on my hero's own life - a grade, a place on a team, a "
                    "friendship, their guardian's job.\n"
                    "5. THE REFUSAL: what they try in order to go back to the old arrangement, and why it "
                    "fails.\n"
                    "6. THE POINT OF NO RETURN: the moment retreat becomes impossible.\n"
                    "7. THE ACT ONE BEATS: 10-12 sequential beats from the opening image to the point of "
                    "no return, one sentence each, naming who is present and what changes. Anchor at least "
                    "three of them to dated pressure points from my school calendar.\n"
                    "8. THE DRAMATIC QUESTION: what act one asks, as a yes/no the ending answers.\n\n"
                    "End by asking me what my hero loses in act one that they cannot get back, and whether "
                    "the last chapter acknowledges it."
                ),
                "pro_tip": (
                    "Anchor your beats to the school calendar from the start. A plot that has to happen "
                    "before the application deadline is tighter than one that happens over an unspecified "
                    "autumn, and the deadline costs you nothing to install."
                ),
            },
            {
                "title": "The Full Beat Sheet",
                "desc": (
                    "This prompt maps the novel onto the genre's spine while keeping three threads in step: "
                    "the heroic plot, the identity plot, and the coming-of-age plot."
                ),
                "prompt_text": (
                    "You are a story architect building a complete beat sheet for a YA superhero novel.\n\n"
                    "My first act: [PASTE FROM PROMPT 12]\n"
                    "My antagonist, their offer and the rebuttal: [PASTE FROM PROMPT 11]\n"
                    "My guardians and the disclosure decision: [PASTE FROM PROMPT 9]\n"
                    "My rival and the scattering: [FROM PROMPT 10]\n"
                    "My power's hard limits: [FROM PROMPT 2]\n"
                    "My public-opinion turn: [FROM PROMPT 6 ITEM 6]\n"
                    "Target length: [E.G. 85,000 WORDS]\n\n"
                    "Build my BEAT SHEET across these stations. For each: 2-4 sentences, an approximate "
                    "word-count position, a note on which thread it serves (heroic, identity, "
                    "coming-of-age), and where it falls in the school year:\n\n"
                    "1. The Managed Year\n"
                    "2. The Crisis\n"
                    "3. The First Public Act, and the Cost\n"
                    "4. The Declaration - my hero says what they will do\n"
                    "5. The Adults Respond - school, state, guardians\n"
                    "6. The Rival Reframes the Goal\n"
                    "7. Midpoint: The Antagonist's Argument and the Offer\n"
                    "8. The Identity Frays - a mundane near-miss, and public opinion turns\n"
                    "9. The Guardian Confrontation, per Prompt 9 item 6\n"
                    "10. The Failure - the power is not enough, or is exactly the problem\n"
                    "11. All Is Lost - the anchor from Prompt 8 item 9 is on the table\n"
                    "12. The Choice About Who To Be\n"
                    "13. The Confrontation, Won by Understanding Rather Than a New Ability\n"
                    "14. A Changed Rule, and What It Cost\n"
                    "15. Graduation, or the Threshold - altered\n\n"
                    "Then flag: any beat relying on coincidence, any two beats doing the same job, any "
                    "stretch where a thread goes dark for too long, any place the climax depends on "
                    "exceeding the hard limits from Prompt 2, and any place the school year and the plot "
                    "have drifted out of sync.\n\n"
                    "End by asking me whether beat 15 answers the coming-of-age question or only the "
                    "heroic one, because YA readers came for the first."
                ),
                "pro_tip": (
                    "Beat 15 is the one that makes this a YA novel. Resolve the world if you like, but the "
                    "reader needs to close the book knowing who this person has decided to be - that is the "
                    "promise the age band makes."
                ),
            },
            {
                "title": "The Set-Piece Generator",
                "desc": (
                    "Reusable for every major sequence - a fight, a rescue, a chase, a confrontation in "
                    "front of phones. Built on constraint, consequence and the one decision in the middle."
                ),
                "prompt_text": (
                    "You are an action choreographer for prose fiction who builds sequences around "
                    "decisions and constraints rather than moves.\n\n"
                    "My power, limits, costs and counters: [PASTE FROM PROMPT 2]\n"
                    "My opponent for this sequence: [PASTE THE RELEVANT ENTRY FROM PROMPT 10 OR 11]\n"
                    "My fight sites: [FROM PROMPT 7 ITEM 5]\n"
                    "The sequence I need: [E.G. A RESCUE AT SCHOOL / A ROOFTOP PURSUIT / A FIGHT IN FRONT "
                    "OF PHONES / A CONFRONTATION WITH THE PROGRAMME / A FIGHT MY HERO MUST LOSE]\n"
                    "Where it sits: [BEAT AND CHAPTER FROM PROMPT 13]\n\n"
                    "Design the sequence:\n\n"
                    "1. THE OBJECTIVE: what my hero is trying to achieve - specific and losable, not "
                    "'win'. Then what the opponent wants, which should not simply be 'stop them'.\n"
                    "2. THE WITNESS PROBLEM: who else is present, how many have phones, and what my hero "
                    "has to do about being seen. At this age band, exposure is a live cost in every fight.\n"
                    "3. THE GEOGRAPHY: the space in detail - what is load-bearing, where the exits are, "
                    "what the terrain does to my power specifically.\n"
                    "4. THE CONSTRAINT STACK: which hard limits and costs bite during this sequence, and "
                    "at what point. List them by beat - this is where all the tension comes from.\n"
                    "5. THE TURN: how the plan fails in two stages - a setback absorbed, then the real "
                    "one, which must come from an established limit rather than luck.\n"
                    "6. THE BEATS: 12-16 sequential beats, one sentence each, with the cost clock noted - "
                    "energy, pain, time, how long before someone arrives.\n"
                    "7. THE DECISION: the moment my hero must choose between the objective and a person. "
                    "Write it out.\n"
                    "8. THE PROSE PLAN: 3 sensations from inside my hero's body that will carry this on "
                    "the page, since a reader cannot see a fight.\n"
                    "9. THE COST: what this takes permanently, including one named non-principal affected "
                    "and one consequence that follows my hero back to school on Monday.\n"
                    "10. THE AFTER: the quiet scene immediately following, and the one thing said in it "
                    "that changes a relationship.\n\n"
                    "End by asking me whether my hero achieved the objective, because a sequence where "
                    "they win the fight and lose the objective is the strongest version of this scene."
                ),
                "pro_tip": (
                    "Item 9's second half is the YA discipline. Every fight should have a Monday - a "
                    "bruise someone asks about, a missed test, a rumour, a parent who was called. Fights "
                    "without a Monday are weightless."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 5: WRITE THE BOOK",
        "intro": (
            "Three prompts: a chapter plan with a masked-to-unmasked balance, an opening chapter that puts "
            "the ordinary life first, and a drafting engine that tracks the things a YA superhero novel "
            "actually loses track of - body, lies, grades and guardians."
        ),
        "prompts": [
            {
                "title": "Chapter Outline with Hooks",
                "desc": (
                    "This prompt turns the beat sheet into a chapter plan where every chapter has a job, a "
                    "turn and a cost - and where the school life gets as much room as the heroics."
                ),
                "prompt_text": (
                    "You are a novel outliner working in young adult speculative fiction.\n\n"
                    "My beat sheet: [PASTE FROM PROMPT 13]\n"
                    "My school calendar: [PASTE FROM PROMPT 5 ITEM 2]\n"
                    "My set pieces: [LIST THOSE DESIGNED WITH PROMPT 14]\n"
                    "Target: [E.G. 85,000 WORDS IN 48 CHAPTERS OF ABOUT 1,800 WORDS]\n"
                    "Point of view: [FIRST PERSON PRESENT / FIRST PERSON PAST / THIRD LIMITED - and who]\n\n"
                    "Build my CHAPTER OUTLINE. For every chapter give me:\n\n"
                    "1. Chapter number and working title.\n"
                    "2. POV character, location, the date or point in the school year, and whether my hero "
                    "is masked or unmasked.\n"
                    "3. The chapter's job in one sentence.\n"
                    "4. The turn: what is true at the end that was not true at the start.\n"
                    "5. Which thread it serves - heroic, identity, or coming-of-age.\n"
                    "6. The cost paid - body, grade, trust, friendship, a lie added - or 'none' for a "
                    "breath chapter.\n"
                    "7. The closing hook, as a one-line description.\n\n"
                    "Then flag: any three consecutive masked chapters, any stretch of more than four "
                    "chapters with no cost, any two set pieces too close together, any chapter where a "
                    "guardian should plausibly have intervened and does not, any thread dark for more than "
                    "five chapters, and any place the plot has drifted off the school calendar.\n\n"
                    "End by telling me my masked-to-unmasked ratio and asking whether it matches the book "
                    "I said I wanted in Prompt 3."
                ),
                "pro_tip": (
                    "Aim for more unmasked chapters than instinct suggests - at least half. The school and "
                    "kitchen-table scenes are what prose can do that no film can, and they are the ones "
                    "readers quote back to you."
                ),
            },
            {
                "title": "The Opening Chapter",
                "desc": (
                    "This prompt drafts chapter one to establish the voice, the arrangement and its cost "
                    "before any spectacle - so a reader commits to the person, not the power."
                ),
                "prompt_text": (
                    "You are a novelist drafting the opening chapter of a YA superhero novel in the voice "
                    "described below.\n\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET, PLUS NOTES "
                    "ON YOUR OWN STYLE]\n"
                    "My protagonist, origin fragment and declaration: [PASTE FROM PROMPT 8]\n"
                    "My power, its costs and one mundane use: [PASTE FROM PROMPT 2]\n"
                    "My household and what they have noticed: [PASTE FROM PROMPT 9]\n"
                    "My school and its sensory kit: [FROM PROMPT 5]\n"
                    "POV and tense: [SPECIFY]\n"
                    "Target length: [E.G. 1,800-2,400 WORDS]\n\n"
                    "Write chapter one, following these rules:\n\n"
                    "1. Open in the ordinary life, mid-task - school, home, a shift, a bus.\n"
                    "2. Show the power early but small, using a mundane use from Prompt 2 item 8, and let "
                    "it cost something measurable.\n"
                    "3. Establish the dual life through a concrete logistical problem, not through "
                    "reflection: a deadline, a lie, an injury to hide, a message not answered.\n"
                    "4. Put one adult on the page who notices something.\n"
                    "5. Deliver the powered world as background texture only - a drill, a notice, a news "
                    "item, a joke - never as explanation.\n"
                    "6. Give me nothing of the origin except one fragment a person would actually think in "
                    "passing.\n"
                    "7. Include one moment of warmth or humour.\n"
                    "8. Put the final-year clock on the page once, lightly.\n"
                    "9. Bring in the pressure that becomes the crisis, at low volume.\n"
                    "10. End on the hook from my chapter outline.\n\n"
                    "After the chapter, list what a reader can infer about the power, the world, the "
                    "household and the hero, and flag anything I explained that I should have implied. "
                    "Then flag any line that reads as an adult writing a teenager.\n\n"
                    "End by asking me whether a reader who stopped here would care about this person "
                    "independent of the power, and what specifically would make them."
                ),
                "pro_tip": (
                    "Do not open with a rescue. The scene you want is a tired teenager using something "
                    "extraordinary to solve something trivial while somebody's mother watches - it "
                    "establishes power, cost, tone, voice and stakes in one page."
                ),
            },
            {
                "title": "The Batch Drafting Engine",
                "desc": (
                    "The prompt you will reuse most. It drafts three to five chapters while holding voice, "
                    "power costs, the lie ledger, school standing, public opinion and the guardians' "
                    "suspicion steady."
                ),
                "prompt_text": (
                    "You are my drafting partner on a YA superhero novel. You write in my established "
                    "voice and hand control back to me at the end of every batch.\n\n"
                    "STANDING CONTEXT (reuse and update this block every batch):\n"
                    "- Voice sample: [PASTE 300-500 WORDS OF YOUR APPROVED CHAPTER ONE FROM PROMPT 16]\n"
                    "- Hero and arc stage: [FROM PROMPT 8, PLUS WHERE THEY ARE NOW]\n"
                    "- Power rules I must not break: [THE FIVE HARD LIMITS AND COST STRUCTURE FROM PROMPT 2]\n"
                    "- Body state: [INJURIES, EXHAUSTION, WHAT IS HEALING AND HOW LONG MY RULES SAY IT TAKES]\n"
                    "- School standing: [GRADES, DEADLINES MISSED OR DUE, TEAM OR CLUB STATUS, WHO HAS "
                    "NOTICED]\n"
                    "- Household: [WHAT THE GUARDIANS NOW SUSPECT, ON THE SCALE FROM PROMPT 9]\n"
                    "- The lie ledger: [WHICH LIES ARE ACTIVE, WHICH ARE FRAYING]\n"
                    "- Knowledge tiers: [WHO KNOWS, WHO SUSPECTS - FROM PROMPT 10]\n"
                    "- Public opinion: [WHERE IT STANDS, WHAT LAST MOVED IT]\n"
                    "- Date in the school year: [STATE IT]\n\n"
                    "THIS BATCH: write chapters [X] to [Y] from my outline:\n"
                    "[PASTE THE OUTLINE ENTRIES FROM PROMPT 15]\n\n"
                    "Rules for this batch:\n"
                    "1. Match the voice sample in rhythm, sentence length and level of interiority.\n"
                    "2. Never let the power exceed its hard limits or heal faster than its cost structure "
                    "allows.\n"
                    "3. Every chapter spends something specific - body, grade, trust, standing, or a lie.\n"
                    "4. Masked and unmasked chapters read in noticeably different registers.\n"
                    "5. Any public use of power generates a reaction - press, school, state, or neighbour.\n"
                    "6. At least one adult per batch notices something and acts on it.\n"
                    "7. No slang I have not already established in chapter one.\n"
                    "8. End each chapter on its outlined hook.\n\n"
                    "After the chapters, give me a STATUS REPORT: body state, school standing, household "
                    "suspicion level, lies added or broken, who now knows what, public opinion movement, "
                    "date reached, and any promise you made on the page that I now owe the reader.\n\n"
                    "End by asking me which chapter drifted furthest from my voice, and which line sounded "
                    "most like an adult writing a teenager."
                ),
                "pro_tip": (
                    "The household suspicion line is the one to guard. If the guardians' belief about what "
                    "is going on has not moved in five chapters, either they are being written as furniture "
                    "or your hero is being suspiciously lucky."
                ),
            },
        ],
    },

    {
        "name": "PHASE 6: POLISH, PUBLISH, EXPAND",
        "intro": (
            "Three prompts to finish: the grade-12 and power-logic audit, the retail kit with the age "
            "positioning that this band lives or dies on, and a series plan built around graduation."
        ),
        "prompts": [
            {
                "title": "The Grade-12 and Power-Logic Audit",
                "desc": (
                    "Two audits in one pass, because they fail together: a power system readers can break, "
                    "and a teen voice that reads as an adult impersonating one."
                ),
                "prompt_text": (
                    "You are a continuity and age-band editor for young adult fiction. You are merciless "
                    "about powers that solve problems they were never established to solve, and about "
                    "adults ventriloquising teenagers.\n\n"
                    "My power system, hard limits, costs and skill curve: [PASTE FROM PROMPT 2]\n"
                    "My institutional rules: [PASTE FROM PROMPT 4]\n"
                    "My grade-12 calibration: [PASTE FROM PROMPT 3 ITEM 3]\n"
                    "My level spec: [PASTE THE LEVEL SPEC FROM THIS PACK'S CHEAT SHEET]\n"
                    "My manuscript or detailed chapter summaries: [PASTE - WORK IN SECTIONS IF LONG]\n\n"
                    "PART A - POWER AND CONTINUITY. Audit and cite the chapter for each issue:\n"
                    "1. LIMIT BREACHES: every place the power does something the five hard limits forbid.\n"
                    "2. COST EVASION: uses that should have cost more, and injuries healing faster than my "
                    "own rules allow. Track injuries chapter by chapter.\n"
                    "3. THE COMPETENCE CURVE: any new ability appearing without setup, especially near the "
                    "climax.\n"
                    "4. THE OBVIOUS SOLUTION PROBLEM: for each major obstacle, could an established power "
                    "have solved it trivially? Flag every place my hero should have won instantly.\n"
                    "5. INSTITUTIONAL AND GUARDIAN CONSISTENCY: do the school, the state and the "
                    "guardians act according to their stated capability, or go conveniently passive when "
                    "my plot needs room? This is the most common failure in the subgenre.\n"
                    "6. THE SECRET'S INTEGRITY: who knows what, when; every near-miss the world should "
                    "have followed up on and did not.\n"
                    "7. THE SCHOOL CLOCK: does the plot stay in sync with the academic calendar, and do "
                    "the academic consequences actually arrive?\n\n"
                    "PART B - AGE AND VOICE:\n"
                    "8. THE VENTRILOQUISM SWEEP: every line where an adult author is audible - dated "
                    "slang, an adult's vocabulary, a teenager explaining a theme, a joke from the wrong "
                    "decade.\n"
                    "9. CONTENT GATES: anything outside the grade-12 range from Prompt 3, in either "
                    "direction - too explicit in framing, or too coy for a reader who is eighteen.\n"
                    "10. THE CONDESCENSION SWEEP: simplified syntax, over-explained emotion, a moral "
                    "stated rather than dramatised, an adult character delivering the book's thesis.\n"
                    "11. THE AGENCY CHECK: every place an adult solves my hero's problem for them.\n"
                    "12. AUTHENTICITY WINS: name the 5 moments that read as most truthfully seventeen, so "
                    "I know what to protect.\n\n"
                    "Rank all findings CRITICAL, MODERATE or MINOR, with a fix for every CRITICAL.\n\n"
                    "End by asking me which critical fix requires a structural change, so I can plan that "
                    "repair before touching the prose."
                ),
                "pro_tip": (
                    "Item 11 matters more than any other line in this audit. YA is the genre of agency - "
                    "every problem an adult solves is a scene stolen from your protagonist, and grade-12 "
                    "readers feel the theft even when they cannot name it."
                ),
            },
            {
                "title": "Blurb, Metadata and Age Positioning",
                "desc": (
                    "The retail kit, plus the age signalling that upper YA depends on - because the wrong "
                    "reader arriving is the fastest route to bad reviews in this band."
                ),
                "prompt_text": (
                    "You are a book marketing copywriter specialising in young adult fiction, with "
                    "experience at the upper end of the band.\n\n"
                    "My reader promise, calibration and pitches: [PASTE FROM PROMPT 3]\n"
                    "My hero, power and declaration: [PASTE FROM PROMPTS 2 AND 8]\n"
                    "My antagonist's thesis: [FROM PROMPT 11]\n"
                    "My tone and scale placement: [FROM PROMPT 1]\n"
                    "My ending: [FROM PROMPT 13]\n\n"
                    "Build my retail kit:\n\n"
                    "1. THE BLURB: 150-200 words in three movements - the person and their power in two "
                    "sentences, the impossible position, the stakes and hook. Lead with the person. Nothing "
                    "past the midpoint.\n"
                    "2. TWO ALTERNATIVES: a punchy 100-word version, and one leading with the "
                    "relationship.\n"
                    "3. THE HOOK LINE: three options for the line above the blurb.\n"
                    "4. THE AGE SIGNAL: the specific words and phrasing in this blurb that tell a browser "
                    "this is upper YA rather than middle grade or adult. This band is crowded at both "
                    "edges - be concrete about the markers.\n"
                    "5. THE TONE SIGNAL: what in the blurb tells a reader where I sit on the "
                    "bright-to-deconstruction axis, so the right reader self-selects.\n"
                    "6. CATEGORIES: 6 retail categories ranked by how well I compete in each.\n"
                    "7. KEYWORDS: 20 reader-search phrases grouped into trope, mood and situation terms.\n"
                    "8. COMP POSITIONING: 4 comparable reading and viewing experiences described as types "
                    "of work, each with a 'for readers who loved X but wanted Y' line.\n"
                    "9. THE GATEKEEPER NOTE: a short, honest content note aimed at the adults who buy "
                    "books for and recommend books to seventeen-year-olds - librarians, teachers, parents. "
                    "Non-spoiling, drawn from my calibration in Prompt 3.\n"
                    "10. THE COVER BRIEF: 5 visual directions tied to specific images from my book, 3 "
                    "clichés to forbid, and a judgement on whether a costumed figure should appear at all.\n\n"
                    "End by asking me which promise in the blurb I am least confident the book delivers, "
                    "so we can fix the blurb or fix the book."
                ),
                "pro_tip": (
                    "Item 9 is worth writing even if it never goes on the book. Librarians and teachers "
                    "move enormous numbers of upper-YA copies, and a clear, unembarrassed content note is "
                    "what gets a book recommended rather than quietly skipped."
                ),
            },
            {
                "title": "Series Architecture and Graduation",
                "desc": (
                    "YA superhero series face a structural problem no adult series has: the protagonist "
                    "ages out of the premise. This prompt plans for that instead of pretending otherwise."
                ),
                "prompt_text": (
                    "You are a series architect for young adult fiction, with specific expertise in the "
                    "problem of a protagonist who is about to leave school.\n\n"
                    "My book one and its ending: [PASTE FROM PROMPT 13]\n"
                    "My antagonist and whether the thesis was answered: [FROM PROMPT 11]\n"
                    "My rival and the scattering: [FROM PROMPT 10]\n"
                    "My power's skill curve and hard limits: [FROM PROMPT 2]\n"
                    "My surviving cast and knowledge tiers: [FROM PROMPTS 9-10]\n"
                    "My scale ceiling: [FROM PROMPT 1 ITEM 2]\n\n"
                    "Design my SERIES:\n\n"
                    "1. THE GRADUATION PROBLEM: my protagonist finishes school at the end of this book or "
                    "soon after. Give me the three honest options - compress the series inside one school "
                    "year, follow them out into the wider world and lose the school container, or hand the "
                    "series to a younger character - with the cost of each. Then recommend one.\n"
                    "2. THE SHAPE: given that answer, recommend a series shape and length and justify it "
                    "against my ending.\n"
                    "3. THE SERIES QUESTION: the question the whole series answers, distinct from book "
                    "one's.\n"
                    "4. THE POWER-CREEP CONTRACT: state explicitly what my hero's power will and will not "
                    "become across the series. Then name 5 things I will escalate INSTEAD of raw power - "
                    "intimacy of the threat, institutional pressure, moral compromise, the number of people "
                    "depending on them, public exposure, the cost per use. Commit in writing.\n"
                    "5. THE IDENTITY CLOCK: how long the secret survives, and what the books look like "
                    "after it breaks. This is the biggest structural decision in the series - decide now.\n"
                    "6. BOOK TWO: a one-page premise - the new pressure, the returning cost from book one, "
                    "and a rupture in the first three chapters. It must not undo book one's ending or "
                    "un-graduate my hero.\n"
                    "7. BOOK THREE AND BEYOND: a paragraph each, ending with the final image of the "
                    "series.\n"
                    "8. THE SEEDS: 6 things planted or plantable in book one that pay off later - a rival, "
                    "a named collateral victim, an institutional enemy, a powered classmate in the wrong "
                    "knowledge tier, an unanswered question, a debt.\n"
                    "9. THE STANDALONE GUARANTEE: confirm book one satisfies alone, and name anything in "
                    "my ending that reads as an unpaid promise rather than an open door.\n\n"
                    "End by asking me whether my hero still has the power at the end of the series, "
                    "because that answer changes what I plant in book one."
                ),
                "pro_tip": (
                    "Take option one in item 1 more seriously than you want to. A trilogy that all happens "
                    "inside a single final year is tight, thematically honest, and avoids the book-four "
                    "problem where a twenty-two-year-old is still narrating a high-school premise."
                ),
            },
        ],
    },
]
