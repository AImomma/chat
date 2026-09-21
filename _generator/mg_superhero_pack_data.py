# -*- coding: utf-8 -*-
"""
Royalti Studios - MG Superhero Master Prompt Pack (Middle Grade Line, ages 8-12).

Build with:
    python pack_builder.py mg_superhero_pack_data \
        "MG_Superhero_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "MG SUPERHERO",
    "total_prompts": 18,
    "hook_line": "Give a kid a power too big for them, a neighbourhood worth saving, and three friends who will absolutely tell on them.",
    "keyword_lines": [
        "Secret identity • Friend crew • One trusted grown-up • Training montages • Very close calls",
        "Costume made of what was in the garage • Bedtime as a plot problem • A bully who has a reason",
    ],
    "subgenres_line": "Subgenres: Funny Hero, Reluctant Hero, Sidekick Story, Hero Team, Legacy/Family Hero, School-Powers Story, Animal Sidekick, Accidental Hero, Hero-in-Training Academy",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-21",
    "audience_line": "Middle Grade Line",
    "reading_level": "Ages 8-12  |  Grades 3-7  |  Lexile 650L-950L  |  Guided Reading Q-X",
    "cover_h2": "From Origin Story to Finished Middle Grade Novel",
    "closing_tagline": "The power is the fun part. Being eleven and responsible for something - that is the story.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "A middle grade superhero novel is not a shorter YA one. Its engine is different: the reader is "
        "eight to twelve, they want the power to be genuinely fun, and they need to close the book "
        "believing that trying was worth it. That does not mean soft - MG readers handle real fear, real "
        "loss and real unfairness - but it does mean a hope floor you never go below, one grown-up who can "
        "be trusted, and an antagonist who can be understood and beaten. This pack builds all of that, "
        "plus the things MG lives on and adult fiction ignores: a friend crew with real jobs, a bedtime "
        "that is an actual plot obstacle, and prose that sounds right read aloud. Work the prompts in "
        "order and keep every output in one document. By Prompt 18 that document is your series bible."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-3) - Set it up. Lock the tone with a hope floor, build a power system with "
        "kid-scale rules and funny-but-real costs, and lock the reader promise for 8-12 plus the "
        "gatekeepers who buy the book.",
        "Phase 2 (Prompts 4-6) - Build the world. What grown-ups do about kids with powers, the "
        "neighbourhood and school your hero can actually reach, and the other powered kids.",
        "Phase 3 (Prompts 7-10) - Forge the cast. A protagonist with a want and a worry, the family plus "
        "the one trusted grown-up, the friend crew who each have a job, and an antagonist a kid can "
        "understand and beat.",
        "Phase 4 (Prompts 11-13) - Architect the story. The problem and first act, the full beat sheet "
        "with a hope floor and short-chapter pacing, and a set-piece generator for action that thrills "
        "without gore.",
        "Phase 5 (Prompts 14-16) - Write the book. Chapter outline with cliffhangers, an opening chapter "
        "that starts fast, and a batch-drafting engine with a read-aloud check built in.",
        "Phase 6 (Prompts 17-18) - Finish it. The age, read-aloud and power-logic audit, then the blurb, "
        "metadata and series plan.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool and a place to save your outputs between prompts. Brackets like "
        "[THIS] are placeholders - replace them with your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular. Writing a solo hero? Prompt 6 becomes a light "
        "pass. Writing a hero team? Prompt 9 becomes the most important prompt in the pack. Writing a "
        "sidekick story? Run Prompt 8 with the mentor as a main character rather than a safety net."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "A power that is genuinely fun before it is ever a burden - MG readers came for the fun and will stay for the rest",
            "Kid-scale stakes that feel enormous: the school play, a friendship, a pet, a street, a grandmother's house",
            "A friend crew where every member has a real job the plan cannot work without",
            "One trusted grown-up who helps - not solving it, but making it survivable",
            "Obstacles made of childhood logistics: bedtime, a curfew, no money, no lift, a locked gate, a teacher taking attendance",
            "An antagonist whose reason a ten-year-old can understand, and who can actually be beaten",
            "Real fear and real unfairness, always with a hope floor underneath",
            "Humour on nearly every page, including from the power going wrong",
            "Short chapters that each end on a pull, because this reader is deciding one more chapter at bedtime",
            "A protagonist who fixes it themselves, with help - never rescued at the last second by an adult",
        ],
        "kills": [
            "Grimness with no floor - despair, hopeless endings, or cruelty the book does not answer",
            "Grown-ups who solve the problem, which steals the only thing MG is actually about",
            "Powers with no limits, which removes every obstacle a nine-year-old can enjoy watching",
            "Stakes that are too big to feel - a planet in danger reads as less scary than a friend not speaking to you",
            "Talking down: explained jokes, stated morals, simplified feelings, a narrator who tells the reader what to think",
            "Gore, on-page cruelty to animals, or violence with no consequence",
            "A protagonist with no flaw, or one whose flaw is being too nice",
            "Long unbroken chapters with no hook, which lose a reader between sittings",
            "Slang that dates instantly, or an adult's idea of what kids find funny",
            "A first book that ends on a cliffhanger instead of a resolution - at this age that reads as being cheated",
        ],
        "voice": [
            "Read-aloud rhythm: vary sentence length hard, and put the funny word at the end of the sentence",
            "Close first person or close third; this reader wants to be inside one head",
            "Concrete nouns always - the brand of cereal, the name of the dog, the number of the bus",
            "Short paragraphs and lots of white space; a wall of text loses this reader on sight",
            "Let feelings be named plainly, then shown - MG readers are still learning the vocabulary of their own insides",
            "Physical comedy works on the page; the power misfiring is funnier than a joke about it",
            "Dialogue does the heavy lifting; kids read dialogue fastest and remember it longest",
            "Fear is allowed to be real, but the chapter after a scary one should let everyone breathe",
        ],
        "formula": (
            "The Ordinary Kid (a want, a worry, a neighbourhood) -> The Power Arrives (and it is FUN) -> "
            "The First Mistake (the power goes wrong, funny and costly) -> The Secret Begins (and bedtime "
            "becomes a problem) -> The Crew Finds Out -> The Real Problem Shows Up -> Training, Failing, "
            "Improving -> The Trusted Grown-Up Learns Something -> The Plan That Nearly Works -> The Low "
            "Point (the hero is caught, grounded, alone, or has lost a friend) -> The Understanding (what "
            "the antagonist actually wants) -> The Kid-Made Plan -> Fixed By Them, With Help -> The "
            "Neighbourhood, A Little Better"
        ),
        "reader_expectations": (
            "Readers aged 8-12 want the power to be fun, the friends to be real, and the ending to be "
            "earned by the kid. They will follow you into genuine fear - being caught, being alone, losing "
            "a friend, an unfair grown-up - as long as the book does not leave them there. They need short "
            "chapters with pulls, because they read in twenty-minute sittings and decide each time whether "
            "to keep going. They notice instantly when they are being talked down to. And the adults in "
            "their lives - parents, teachers, librarians - are buying the book, so it has to be "
            "recommendable: funny, kind at the bottom, and honest about how hard being ten is. What they "
            "reward: a crew they want to join, a power with a hilarious downside, and a hero who fixes it "
            "themselves."
        ),
        "level_spec": [
            "Band: Lexile 650L-950L / Guided Reading Q-X / grades 3-7, ages 8-12",
            "Manuscript length: 30,000-50,000 words; 30-45 chapters of 800-1,400 words",
            "Chapters: short, one scene or two, each ending on a question, a pull or a surprise",
            "Sentences: mostly 8-16 words, with deliberate short ones for punch; full paragraphs kept to 3-5 sentences",
            "Vocabulary: rich but contextual - hard words are fine when the sentence teaches them; no glossary",
            "Protagonist age: 10-13. This reader reads up, never down - never write a hero younger than the reader",
            "Content in range: real peril, being lost or trapped, a grown-up who is unfair, grief handled "
            "gently, family difficulty, a friendship breaking and mending",
            "Content out of range: gore, on-page death of a main character without careful handling, cruelty "
            "to animals shown, romance beyond a first crush, swearing, hopeless endings",
        ],
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "The best middle grade superhero books understand something the adult versions forget: at ten, the "
        "fantasy is not being powerful. It is being taken seriously. Your reader is someone who is told "
        "what to do all day by people who do not explain themselves, and you are handing them a character "
        "who is finally responsible for something real. Let that be fun. Let the power misfire and be "
        "embarrassing. Let bedtime genuinely ruin a plan. And then let your hero fix it themselves, with "
        "help, and let the neighbourhood be a little better because a kid decided to bother. When a "
        "chapter goes flat, check whether the friends have anything to do and whether anything in it is "
        "funny. Those two fixes solve almost everything at this age band."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: SET IT UP",
        "intro": (
            "Three prompts to set the contract: how funny and how scary this book is allowed to be, a "
            "power with rules a ten-year-old can enjoy watching, and the reader promise - including the "
            "grown-ups who will actually buy it."
        ),
        "prompts": [
            {
                "title": "Lock the Tone and the Hope Floor",
                "desc": (
                    "Middle grade can go genuinely dark, but never without a floor. This prompt sets how "
                    "funny, how scary, and what must still be true on the last page."
                ),
                "prompt_text": (
                    "You are a developmental editor who has worked on middle grade fiction for fifteen "
                    "years and knows the superhero space specifically.\n\n"
                    "My rough idea is: [DESCRIBE IN 2-4 SENTENCES - a power, a kid, an image, whatever I "
                    "have]\n\n"
                    "Do the following:\n\n"
                    "1. Place my idea on the FUNNY AXIS from 1 to 10, where 1 = sincere and earnest "
                    "throughout and 10 = comedy first. Explain the placement, and tell me what a book at my "
                    "number feels like chapter to chapter.\n"
                    "2. Place me on the SCARY AXIS from 1 to 10, where 1 = gentle and 10 = as frightening "
                    "as middle grade gets. Then tell me exactly what my number permits and forbids on the "
                    "page for readers aged 8-12.\n"
                    "3. THE HOPE FLOOR: name the specific thing that must still be true at the end of this "
                    "book, even in its saddest version. One sentence. This is non-negotiable at this age "
                    "band - write it down and do not go below it.\n"
                    "4. THE STAKES SCALE: MG stakes work best small and personal. Take whatever scale my "
                    "idea currently has and give me the kid-sized version of it - the friendship, the pet, "
                    "the street, the grandmother's house, the team, the one adult who believes them. Tell "
                    "me honestly whether my current stakes are too big to feel.\n"
                    "5. Name my primary subgenre and two secondaries from: funny hero, reluctant hero, "
                    "sidekick story, hero team, legacy/family hero, school-powers story, animal sidekick, "
                    "accidental hero, hero-in-training academy. Justify each.\n"
                    "6. THE MG OBLIGATION: name the three things this genre gains from a ten-to-thirteen "
                    "year-old lead that an adult version could not do, and which one my idea is wasting.\n"
                    "7. THE GROWN-UP RULE: state who the adults are and what they are doing about this. "
                    "Then confirm the hard rule - adults may help, adults may not solve it - and tell me "
                    "where my idea is currently at risk of breaking it.\n"
                    "8. Write my LANE STATEMENT in two sentences: what kind of MG superhero book this is "
                    "and what it promises a ten-year-old.\n\n"
                    "End by asking me what the funniest thing about this power is, because if I cannot "
                    "answer that, the book is missing its engine."
                ),
                "pro_tip": (
                    "Write the hope floor on a sticky note. Around chapter twenty of a draft where you have "
                    "grounded your hero, split up the crew and let the antagonist win, that one sentence is "
                    "what stops you writing an ending an eight-year-old should not have to hold."
                ),
            },
            {
                "title": "The Power System, Kid-Scale",
                "desc": (
                    "An MG power needs rules, a cost that is funny before it is serious, and limits that "
                    "create problems a young reader can enjoy solving alongside the hero."
                ),
                "prompt_text": (
                    "You are a systems designer building a power system for a middle grade novel. You know "
                    "that at this age band the limits are the fun and the costs are the comedy.\n\n"
                    "My lane statement and funny axis: [PASTE FROM PROMPT 1]\n"
                    "My hero's power, roughly: [DESCRIBE, or say 'you choose']\n\n"
                    "Build my POWER SYSTEM:\n\n"
                    "1. THE MECHANISM: what the power does, in three plain sentences a ten-year-old could "
                    "repeat to a friend. If a reader cannot explain it at the dinner table, simplify it.\n"
                    "2. THE FIVE HARD LIMITS: things it can never do. Write them as rules I may not break. "
                    "At least two should be annoying rather than dramatic, because annoying limits are "
                    "funny and generate plot.\n"
                    "3. THE EMBARRASSING COST: what using it does to my hero that is funny and public - "
                    "hiccups, glowing, a smell, hair standing up, uncontrollable hunger, losing a shoe. MG "
                    "readers love a power with a humiliating price.\n"
                    "4. THE REAL COST: what heavy use actually takes - exhaustion, a nosebleed, sleeping "
                    "through a whole day, a headache that lasts. Give me the cost at three levels and the "
                    "recovery time for each, so I cannot cheat.\n"
                    "5. THE KID-LIFE COLLISIONS: 6 concrete ways this power runs into being a kid - a "
                    "school uniform, a shared bedroom, a swimming lesson, a car journey, a sleepover, a "
                    "parent doing the laundry.\n"
                    "6. THE SKILL CURVE: what they can do now, what practice unlocks during this book, and "
                    "what is permanently out of reach. State plainly what they will NOT learn, so the "
                    "climax cannot be a new trick.\n"
                    "7. THE FAILURE MODES: 5 ways it goes wrong, at least three of them comic.\n"
                    "8. THE FUN LIST: 8 things my hero does with this power purely because it is brilliant "
                    "- no heroism involved. This is the list young readers came for, and most writers "
                    "include two.\n"
                    "9. THE COUNTERS: 4 ways an ordinary grown-up, or a locked door, beats my hero. If "
                    "there are none, the power is broken - redesign it.\n\n"
                    "End by asking me which limit my hero will try hardest to break, and whether they "
                    "should succeed."
                ),
                "pro_tip": (
                    "Item 8 is the whole reason a nine-year-old picks up the book. Spend a full early "
                    "chapter on the hero just enjoying the power, being silly with it and getting into "
                    "trouble - the rest of the book earns its weight against that chapter."
                ),
            },
            {
                "title": "Reader Promise, Age Calibration & Gatekeepers",
                "desc": (
                    "This prompt calibrates for 8-12 and, crucially, for the parents, teachers and "
                    "librarians who actually hand this book to a child."
                ),
                "prompt_text": (
                    "You are a publishing strategist positioning middle grade fiction, who understands "
                    "that children choose books and adults buy them.\n\n"
                    "My lane statement and axis placements: [PASTE FROM PROMPT 1]\n"
                    "My power system: [PASTE FROM PROMPT 2]\n\n"
                    "Do the following:\n\n"
                    "1. Write my READER PROMISE in one paragraph, addressed to a ten-year-old, in the "
                    "second person ('You will...').\n"
                    "2. THE AGE TARGET: my band is 8-12, which is wide. Tell me which end I am actually "
                    "writing for, what my protagonist's age should be (readers read up, never down), and "
                    "the three markers on the page that will signal the younger or older end.\n"
                    "3. THE CONTENT CALIBRATION: given readers aged 8-12 at my scary-axis score, state "
                    "specifically what is in range and out of range. Cover peril, injury, death and grief, "
                    "bullying, family difficulty, a first crush, unfair adults, and scary imagery. For each "
                    "give the range and the framing that would take it out of range.\n"
                    "4. THE GATEKEEPER TEST: for each of parents, teachers and librarians, name the one "
                    "thing about my book that would make them recommend it, and the one thing that would "
                    "make them hesitate. Then tell me how to keep the first without softening the book.\n"
                    "5. THE CONDESCENSION AUDIT: list 6 ways MG manuscripts talk down to readers, with an "
                    "early warning sign for each in my own drafting.\n"
                    "6. Write 3 one-line pitches: one funny, one exciting, one about the friendship.\n"
                    "7. THE SCHOOL AND LIBRARY ANGLE: what about this book makes it work as a read-aloud, "
                    "a class set, or a series a librarian restocks. Be concrete.\n"
                    "8. CATEGORIES AND PROMISES: 5 retail categories ranked, plus the 4 promises I must "
                    "not break with the review or complaint each breach would generate.\n"
                    "9. THE ORIGINALITY CHECK: the 5 most familiar elements of my concept and one specific "
                    "way to make each mine.\n\n"
                    "End by asking me whether a reluctant reader would get past chapter three, and what in "
                    "chapter three would hold them."
                ),
                "pro_tip": (
                    "Item 7 pays for itself for years. An MG superhero book that works read aloud to a "
                    "class of thirty gets adopted, re-ordered and remembered - and read-aloud quality is "
                    "almost entirely a matter of short chapters and good dialogue."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: BUILD THE WORLD",
        "intro": (
            "Three prompts. MG worldbuilding is small and concrete: what grown-ups do about powered kids, "
            "the few streets your hero can actually reach, and the other kids who have powers too."
        ),
        "prompts": [
            {
                "title": "What Grown-Ups Do About Kids With Powers",
                "desc": (
                    "The MG version of the institutional layer - concrete, kid's-eye, and built so the "
                    "adults are real without being able to solve the story."
                ),
                "prompt_text": (
                    "You are a worldbuilding consultant advising on a middle grade novel set in a world "
                    "where some children have powers. Everything must be described as a ten-year-old would "
                    "experience it, not as a policy document.\n\n"
                    "My power system: [PASTE FROM PROMPT 2]\n"
                    "My lane statement: [FROM PROMPT 1]\n"
                    "How long powers have existed publicly: [SPECIFY - NEW, A FEW YEARS, ALWAYS, OR "
                    "'STILL SECRET']\n\n"
                    "Build my GROWN-UP WORLD:\n\n"
                    "1. THE RULE: what the rule is about kids with powers - must they be registered, "
                    "tested, taught separately, kept quiet? State it the way a kid would hear it, in one "
                    "or two sentences.\n"
                    "2. AT SCHOOL: what happens at school - a form, a special class, a teacher who is "
                    "supposed to watch them, a drill, an exemption from PE, a rumour. Give me 6 concrete "
                    "details a kid would actually notice.\n"
                    "3. THE PLACE THEY SEND YOU: if there is a programme, camp, academy or test centre, "
                    "describe it as a kid would find it - the smell, the waiting room, the person on the "
                    "desk, what other kids say about it, and the thing about it that is genuinely a bit "
                    "wrong.\n"
                    "4. WHAT PARENTS MUST DO: what a parent or carer is required to do, what they lose if "
                    "they hide it, and how frightened the ones who love their kid actually are. Keep it "
                    "emotional rather than legal.\n"
                    "5. IF YOU GET CAUGHT: what actually happens to a kid who uses powers in public. Not "
                    "prison - a phone call home, a form, a visit, being taken out of class, being on the "
                    "news. Make the consequence age-appropriate and genuinely unwanted.\n"
                    "6. THE HELPERS AND THE UNFAIR ONES: name 3 adults in this system - one who helps, one "
                    "who is unfair, one who is just tired and doing their job badly. None may be cartoon "
                    "villains.\n"
                    "7. THE GAPS: 5 places this system does not look, where a determined kid could "
                    "operate. My plot runs here.\n"
                    "8. THE ADULT LIMIT: state plainly why the grown-ups cannot solve my story's problem. "
                    "It must be a real reason - they do not believe it, they cannot get there, they are not "
                    "allowed, they are being lied to - never simple stupidity.\n\n"
                    "End by asking me which adult in this system my hero is most afraid of, and whether "
                    "that fear is fair."
                ),
                "pro_tip": (
                    "Item 8 is the prompt that saves your book. Write the reason down now; every time a "
                    "reader could ask 'why doesn't she just tell her mum', you need that sentence to be "
                    "already true and already on the page."
                ),
            },
            {
                "title": "The Neighbourhood and the Patch",
                "desc": (
                    "A kid protects what they can walk or bike to. This prompt builds a small, vivid, "
                    "concrete world and narrows the hero's territory until the stakes are legible."
                ),
                "prompt_text": (
                    "You are a setting specialist building a small, specific world for a middle grade "
                    "novel.\n\n"
                    "My grown-up world: [PASTE FROM PROMPT 4]\n"
                    "My hero's power and how they get around: [FROM PROMPT 2]\n"
                    "Place it resembles, if any: [SPECIFY OR SAY 'YOU CHOOSE']\n\n"
                    "Build my SETTING:\n\n"
                    "1. THE PLACE: what this neighbourhood or town is like, who lives here, what it is "
                    "known for, and what it has lost. One paragraph, warm and specific.\n"
                    "2. THE REACH PROBLEM: how far can my hero actually get, given their age, their power, "
                    "no money, a bike or a bus, and having to be home for dinner? Be concrete. This "
                    "constraint is a gift - do not soften it.\n"
                    "3. THE SIX PLACES: name and describe 6 locations in a short paragraph each - the "
                    "school, home, and four others kids actually go. Give each one a landmark, a smell, and "
                    "a reason to come back.\n"
                    "4. THE PATCH: the specific few streets my hero really looks after, and why those.\n"
                    "5. THE ACTION SITES: 5 places something exciting could happen, each with a reason the "
                    "geography is interesting and a reason a fight there would wreck something a kid cares "
                    "about.\n"
                    "6. THE HIDEOUT: where the crew meets. It must be real and slightly rubbish - a shed, "
                    "a den, a garage, a bit of woodland, the back of a shop. Describe what is in it.\n"
                    "7. THE BEDTIME MAP: what my hero can reach and get home from before anyone notices, "
                    "versus what needs a whole excuse. Two lists. This is my plot's real geography.\n"
                    "8. THE SENSORY KIT: for each location, one sound, one smell and one detail that "
                    "identifies it instantly.\n\n"
                    "End by asking me what my hero would lose if this neighbourhood changed, because that "
                    "is what the book is defending."
                ),
                "pro_tip": (
                    "Item 7 is the most useful thing in this phase. Once you have a list of what is "
                    "reachable before dinner, half your plot problems solve themselves and the other half "
                    "become genuinely tense."
                ),
            },
            {
                "title": "The Other Powered Kids",
                "desc": (
                    "Your hero is not the only one. This prompt builds the other kids with powers - the "
                    "ones doing better, doing worse, and doing something dangerous."
                ),
                "prompt_text": (
                    "You are a worldbuilding consultant mapping the other powered children in a middle "
                    "grade novel's world.\n\n"
                    "My power system and its source: [PASTE FROM PROMPT 2]\n"
                    "My grown-up world: [PASTE FROM PROMPT 4]\n"
                    "My school and neighbourhood: [FROM PROMPT 5]\n\n"
                    "Build my POWERED KIDS:\n\n"
                    "1. HOW MANY: roughly how many kids have powers, how rare that makes my hero, and "
                    "whether my hero's power is common, unusual, or the only one of its kind. Say it "
                    "plainly.\n"
                    "2. WHERE THEY COME FROM: why anyone has powers here, told simply, plus the version "
                    "kids believe at school, which should be wrong in an interesting way.\n"
                    "3. THE FOUR KIDS: 4 other powered children. For each: name, age, power, whether it is "
                    "known, and how they are handling it. One must be handling it much better than my hero "
                    "and be annoying about it. One must be handling it much worse and need help. One must "
                    "be using it for something small and selfish. One must be hiding it completely.\n"
                    "4. THE ONE WHO SCARES THEM: which of these kids my hero is wary of, and why - it "
                    "should be about behaviour, not power level.\n"
                    "5. THE OLDER KID: a teenager with powers who has been through what my hero is going "
                    "through. What they tell my hero, what they get wrong, and why my hero half-believes "
                    "them.\n"
                    "6. THE POWER LEVELS: a simple, clear sense of who is stronger than whom, so a reader "
                    "always knows what an opponent means. Place my hero and my antagonist on it.\n"
                    "7. THE KID RULES: 5 unwritten rules powered kids have made up among themselves. These "
                    "are not laws - they are playground rules, and breaking one should have social "
                    "consequences.\n\n"
                    "End by asking me which of these kids joins my hero's crew and which becomes a "
                    "problem, because the answer might be the same kid."
                ),
                "pro_tip": (
                    "Item 7 is pure MG gold. Kids invent rules and enforce them ferociously - a playground "
                    "code among powered children gives you social stakes that matter more to a ten-year-old "
                    "reader than any law the grown-ups wrote."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: FORGE THE CAST",
        "intro": (
            "Four prompts, and the crew one matters most. Middle grade readers come back for the friends: "
            "a hero with a want and a worry, a family plus one trusted grown-up, a crew where everyone has "
            "a job, and an antagonist a ten-year-old can understand and beat."
        ),
        "prompts": [
            {
                "title": "The Protagonist: A Want and a Worry",
                "desc": (
                    "MG heroes run on a want they can name and a worry they cannot. This prompt builds "
                    "both, plus a flaw that actually causes problems."
                ),
                "prompt_text": (
                    "You are a character-development editor for middle grade fiction.\n\n"
                    "My power, its costs and kid-life collisions: [PASTE FROM PROMPT 2]\n"
                    "My neighbourhood and school: [PASTE FROM PROMPT 5]\n"
                    "My rough protagonist idea: [DESCRIBE, or say 'you choose']\n\n"
                    "Build my PROTAGONIST:\n\n"
                    "1. THE BASICS: name, age (10-13), year at school, who they live with, what their "
                    "bedroom looks like, what they are into.\n"
                    "2. THE WANT: what they wanted before any of this started - something small, concrete "
                    "and achievable that a reader can root for. A place on a team, a friend back, a part in "
                    "the play, a dog, their dad to come to one thing.\n"
                    "3. THE WORRY: the fear underneath, which they could not put into words. One or two "
                    "sentences.\n"
                    "4. THE FLAW: a real flaw that causes real problems - not shyness, not being too kind. "
                    "They lie, they show off, they give up, they take over, they cannot say sorry. Then "
                    "name 3 specific moments the flaw will make things worse.\n"
                    "5. HOW THE POWER ARRIVED: what happened, told in the way a kid would remember it - "
                    "one weird sensory detail and one embarrassing part.\n"
                    "6. THE FIRST TIME IT WENT WRONG: a funny disaster that also cost something.\n"
                    "7. WHY THEY KEEP GOING: the reason they do not just tell a grown-up and stop. It must "
                    "be a reason a ten-year-old would actually have.\n"
                    "8. THE ARC: 5 stages from who they are to who they become, each pushed by an outside "
                    "event, not a change of heart. One must be a step backwards caused by the flaw.\n"
                    "9. THE THING THEY WILL NOT RISK: the person, pet or place they will not put in "
                    "danger. The antagonist will threaten it.\n\n"
                    "End by asking me whether my hero gets the want from item 2, because MG readers "
                    "remember that more than they remember the fight."
                ),
                "pro_tip": (
                    "Item 2 is the heart of the book and item 9 is the climax. Keep the want small - a "
                    "reader who wants your hero to get a place on the team will read four hundred pages of "
                    "superheroics to see it happen."
                ),
            },
            {
                "title": "The Family and the One Trusted Grown-Up",
                "desc": (
                    "MG needs adults who are present and real, plus exactly one who can be trusted. This "
                    "prompt builds both without letting any of them solve the story."
                ),
                "prompt_text": (
                    "You are a character editor who specialises in families in middle grade fiction and "
                    "believes absent or foolish adults are the genre's laziest habit.\n\n"
                    "My protagonist: [PASTE FROM PROMPT 7]\n"
                    "What parents must do, and the adult limit: [PASTE FROM PROMPT 4 ITEMS 4 AND 8]\n"
                    "My power's embarrassing and real costs: [FROM PROMPT 2]\n\n"
                    "Build my HOME:\n\n"
                    "1. THE HOUSEHOLD: who my hero lives with, the actual arrangement, the money "
                    "situation, the rules of the house, and what dinner is like.\n"
                    "2. THE GROWN-UPS AT HOME: for each - name, what they do, what they are worried "
                    "about, what they want for my hero, and their one blind spot. None may be stupid.\n"
                    "3. WHAT THEY HAVE NOTICED: 6 specific things the adults in this house have observed - "
                    "hours, washing, appetite, a torn coat, homework, mood, a lie that did not hold. Then "
                    "say what they currently think is going on, which should be plausible and wrong.\n"
                    "4. THE WORRIED WRONG IDEA: what a loving parent would actually conclude from that "
                    "evidence at this age - bullying, a friendship going bad, something wrong at school, "
                    "illness. This misunderstanding is one of my strongest engines; develop it.\n"
                    "5. THE SIBLING: if there is one, their age, what they know, what they want, and what "
                    "they would trade the secret for. Younger siblings who half-know are excellent trouble.\n"
                    "6. THE TRUSTED GROWN-UP: the one adult who can be told and will help. Not a parent, "
                    "usually - a grandparent, a neighbour, a teacher, a coach, a librarian, a shopkeeper. "
                    "Describe who they are, why my hero trusts them, what they can actually offer, and what "
                    "helping costs them.\n"
                    "7. THE LIMIT OF THAT HELP: state exactly what the trusted grown-up cannot do, so my "
                    "hero still has to fix it. This is the most important line in the prompt.\n"
                    "8. THE GROUNDING: what happens when my hero is caught out - the actual consequence at "
                    "home, and how it wrecks the plan at the worst moment. Every MG superhero book needs "
                    "one chapter where the hero is simply not allowed out.\n\n"
                    "End by asking me whether the family learns the truth in this book, because that "
                    "decision reshapes the whole ending."
                ),
                "pro_tip": (
                    "Item 8 is the single most underused obstacle in the subgenre. Being grounded at the "
                    "climax is funnier, more painful and more true than any cage a villain could build."
                ),
            },
            {
                "title": "The Crew",
                "desc": (
                    "Middle grade readers come back for the friends. This prompt builds a crew where every "
                    "member has a job the plan genuinely cannot work without."
                ),
                "prompt_text": (
                    "You are an ensemble developer for middle grade fiction.\n\n"
                    "My protagonist, their flaw and their want: [PASTE FROM PROMPT 7]\n"
                    "My powered kids: [PASTE FROM PROMPT 6]\n"
                    "My hideout and bedtime map: [FROM PROMPT 5]\n\n"
                    "Build my CREW of 2-4 friends:\n\n"
                    "1. For each: name, age, what they are like in one line, and how they and my hero "
                    "became friends.\n"
                    "2. THE JOB: the specific, real job each one does that the plan cannot work without - "
                    "the planner, the one with the bike, the one whose mum works at the place, the one who "
                    "can talk to adults, the one who actually reads the instructions, the lookout, the "
                    "liar. No passengers.\n"
                    "3. THE SKILL THEY ACTUALLY HAVE: something practical and unpowered - they can climb, "
                    "code, cook, draw, swim, fix a bike, remember everything. Kids love competence in other "
                    "kids.\n"
                    "4. WHAT THEY THINK ABOUT THE POWER: each one's honest opinion of what my hero is "
                    "doing. At least one must think it is a terrible idea and say so repeatedly.\n"
                    "5. THE FRICTION: for each, the thing that would make them fall out with my hero. At "
                    "this age band friendship trouble is a bigger stake than physical danger - use it.\n"
                    "6. WHO FINDS OUT AND HOW: how each member learns the secret, in what order, and which "
                    "discovery goes badly.\n"
                    "7. THE ONE WHO TELLS: at least one member should, at some point, tell an adult - for "
                    "good reasons. Say who, when, and why they were arguably right.\n"
                    "8. THE FUNNY ONE'S LIMIT: if one is the comic character, give them one scene where "
                    "they are not funny, so they are a person rather than a device.\n"
                    "9. THE GROUP VOICE: how these four sound together - the running joke, the nickname, "
                    "the argument they have every time. Give me a sample eight-line exchange.\n\n"
                    "End by asking me which friend the reader will love most, and whether I am prepared to "
                    "put that friendship at risk."
                ),
                "pro_tip": (
                    "Item 7 is what separates a good MG book from a formulaic one. A friend who breaks the "
                    "secret because they are genuinely frightened for your hero is not a traitor - and "
                    "letting the book admit they were right is the most grown-up thing you can do at this "
                    "age band."
                ),
            },
            {
                "title": "The Antagonist a Kid Can Understand",
                "desc": (
                    "MG antagonists need a reason a ten-year-old can follow, a threat that is genuinely "
                    "frightening, and a defeat the hero can actually achieve."
                ),
                "prompt_text": (
                    "You are an antagonist developer for middle grade fiction. You know that at this age "
                    "band the villain must be understandable, beatable, and frightening in a way the book "
                    "can resolve.\n\n"
                    "My protagonist, their flaw and what they will not risk: [PASTE FROM PROMPT 7]\n"
                    "My scary axis and hope floor: [PASTE FROM PROMPT 1]\n"
                    "My powered kids and power levels: [FROM PROMPT 6]\n"
                    "My grown-up world: [FROM PROMPT 4]\n\n"
                    "Build my ANTAGONIST LAYER:\n\n"
                    "1. THE MAIN ANTAGONIST: who they are, what they want, and - crucially - the reason "
                    "they want it, stated so simply that a ten-year-old would say 'oh, I get it'. Not "
                    "chaos. Something wanted, lost, or owed.\n"
                    "2. ARE THEY A KID OR A GROWN-UP: decide, and give me the trade-off. A kid antagonist "
                    "is more personal and more redeemable; an adult one is more frightening and harder to "
                    "beat believably. Recommend one for my book.\n"
                    "3. THE THREAT: what they actually do, kept inside my scary-axis score from Prompt 1. "
                    "Be specific about what appears on the page and what happens off it.\n"
                    "4. WHY MY HERO CAN BEAT THEM: the honest answer. Not stronger - smarter, better "
                    "helped, more willing, or because they understood something. Name it now so the climax "
                    "cannot be a power-up.\n"
                    "5. THE UNDERSTANDING SCENE: the moment my hero works out what the antagonist actually "
                    "wants. Describe it. This scene is the spine of MG antagonism.\n"
                    "6. REDEMPTION OR NOT: decide whether this antagonist can be turned, and say what the "
                    "book gains and loses either way. If yes, name the price. If no, give the reader "
                    "something else - understanding, pity, or a clear reason they chose this.\n"
                    "7. THE SECONDARY TROUBLE: two lesser antagonists - one a kid at school, one an adult "
                    "who is unfair rather than evil. Each should press a different part of my hero than the "
                    "main one does.\n"
                    "8. THE BULLY RULE: if one of them is a bully, give them a reason that is real and "
                    "does not excuse them. MG readers know bullies; they will not accept one made of "
                    "nothing.\n"
                    "9. THE LINE: the moment the antagonist does something the reader cannot forgive, or - "
                    "if they are to be redeemed - the moment they stop just short of it.\n\n"
                    "End by asking me whether my antagonist is lonely, because at this age band that is "
                    "almost always the true answer and it changes how I write them."
                ),
                "pro_tip": (
                    "Item 5 is the scene the book is for. A hero who wins by finally understanding what "
                    "the other person wanted teaches something no fight scene can, and MG readers "
                    "genuinely feel the difference."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: ARCHITECT THE STORY",
        "intro": (
            "Three prompts to build the machine: the problem that starts it, a beat sheet with a hope "
            "floor and short-chapter pacing, and a set-piece generator for action that thrills an "
            "eight-year-old without going anywhere it should not."
        ),
        "prompts": [
            {
                "title": "The Problem and the First Act",
                "desc": (
                    "MG books must start fast. This prompt finds the problem that arrives early and builds "
                    "an act one that has the power, the fun, the crew and the trouble all in place quickly."
                ),
                "prompt_text": (
                    "You are a story architect for middle grade fiction. You know this reader decides by "
                    "chapter three.\n\n"
                    "My protagonist, want and flaw: [PASTE FROM PROMPT 7]\n"
                    "My antagonist and their reason: [PASTE FROM PROMPT 10]\n"
                    "My crew: [PASTE FROM PROMPT 9]\n"
                    "My household and the grounding: [FROM PROMPT 8]\n\n"
                    "Build my FIRST ACT:\n\n"
                    "1. THE ORDINARY DAY: the opening scene - my hero in their life, wanting the thing from "
                    "Prompt 7 item 2, with the worry underneath. Two paragraphs. Something must be "
                    "happening; no waking up, no weather, no explaining.\n"
                    "2. THE POWER CHAPTER: where the fun goes. Describe the early chapter that is mostly "
                    "my hero enjoying and misusing the power, using the fun list from Prompt 2 item 8. Say "
                    "which chapter number it is - it should be early.\n"
                    "3. THE FIRST MISTAKE: the funny disaster that costs something real and starts the "
                    "secret.\n"
                    "4. THE PROBLEM ARRIVES: the event that brings the antagonist or the real trouble into "
                    "my hero's life. Give me 3 options and recommend one that keeps the stakes kid-sized.\n"
                    "5. THE CREW FINDS OUT: how and when, and which member takes it worst.\n"
                    "6. WHY NOT TELL A GROWN-UP: the scene or moment that closes off that option, using "
                    "the adult limit from Prompt 4 item 8. It must be on the page, not assumed.\n"
                    "7. THE DECISION: the moment my hero decides to do something about it, said out loud "
                    "to the crew.\n"
                    "8. THE ACT ONE BEATS: 10-12 sequential beats from the opening image to the decision, "
                    "one sentence each, naming who is present and what changes. Mark which beat lands in "
                    "which chapter, and confirm that something exciting happens by chapter three.\n\n"
                    "End by asking me what my hero gives up in act one to start doing this, and whether "
                    "they notice at the time."
                ),
                "pro_tip": (
                    "Put the power chapter as early as chapter two. Every draft that holds the fun back "
                    "until chapter eight loses readers in chapter four - the enjoyment is not a reward, it "
                    "is the hook."
                ),
            },
            {
                "title": "The Full Beat Sheet",
                "desc": (
                    "This prompt maps the whole novel onto the MG spine, keeps the funny and the scary in "
                    "alternation, and guarantees the hope floor holds."
                ),
                "prompt_text": (
                    "You are a story architect building a complete beat sheet for a middle grade superhero "
                    "novel.\n\n"
                    "My first act: [PASTE FROM PROMPT 11]\n"
                    "My antagonist, the understanding scene and the redemption decision: [PASTE FROM "
                    "PROMPT 10]\n"
                    "My crew and their frictions: [PASTE FROM PROMPT 9]\n"
                    "My grounding scene and trusted grown-up: [FROM PROMPT 8]\n"
                    "My hope floor and axis scores: [FROM PROMPT 1]\n"
                    "My power's hard limits: [FROM PROMPT 2]\n"
                    "Target length: [E.G. 42,000 WORDS IN 38 CHAPTERS]\n\n"
                    "Build my BEAT SHEET across these stations. For each: 2-3 sentences, an approximate "
                    "chapter number, and a note on whether the beat is mostly funny, mostly exciting, or "
                    "mostly feelings:\n\n"
                    "1. The Ordinary Kid\n"
                    "2. The Power Arrives, and It Is Fun\n"
                    "3. The First Mistake\n"
                    "4. The Secret Begins\n"
                    "5. The Crew Finds Out\n"
                    "6. The Real Problem Shows Up\n"
                    "7. Training, Failing, Getting Better\n"
                    "8. The Trusted Grown-Up Learns Something\n"
                    "9. Midpoint: The Plan That Nearly Works\n"
                    "10. The Flaw Makes It Worse - my hero's own fault, per Prompt 7 item 4\n"
                    "11. The Low Point - grounded, alone, or a friendship broken\n"
                    "12. The Understanding - what the antagonist actually wants\n"
                    "13. The Kid-Made Plan - built from the crew's real jobs\n"
                    "14. Fixed By Them, With Help\n"
                    "15. The Want, Answered - and the neighbourhood a little better\n\n"
                    "Then check and flag: any stretch of more than three chapters with nothing funny in "
                    "it, any place the grown-ups should obviously have stepped in, any point where the "
                    "story goes below my hope floor, any place the climax needs a power beyond my hard "
                    "limits, any crew member with nothing to do for more than five chapters, and whether "
                    "beat 15 pays off the want from Prompt 7.\n\n"
                    "End by asking me whether an eight-year-old could summarise this plot in four "
                    "sentences, and if not, what to simplify."
                ),
                "pro_tip": (
                    "Beat 14 is the rule of the whole age band: fixed by them, with help. The help can be "
                    "substantial and the adults can be in the room - but the decisive act must belong to "
                    "the kid, or you have written a book about being rescued."
                ),
            },
            {
                "title": "The Set-Piece Generator",
                "desc": (
                    "Reusable for every exciting sequence - a chase, a rescue, a break-in, a showdown, a "
                    "school event gone wrong. Built for thrill without gore, and for a crew who all get to "
                    "do something."
                ),
                "prompt_text": (
                    "You are an action choreographer for middle grade fiction. You build excitement from "
                    "constraint, teamwork and near-misses rather than from violence.\n\n"
                    "My power, limits, costs and counters: [PASTE FROM PROMPT 2]\n"
                    "My crew and their jobs: [PASTE FROM PROMPT 9]\n"
                    "My action sites and bedtime map: [FROM PROMPT 5]\n"
                    "My scary axis score: [FROM PROMPT 1]\n"
                    "The sequence I need: [E.G. A CHASE THROUGH THE SCHOOL / A RESCUE FROM SOMEWHERE "
                    "FLOODING / SNEAKING INTO THE PLACE THEY SEND YOU / A SHOWDOWN AT THE SCHOOL FAIR / "
                    "GETTING HOME BEFORE DINNER WITH SOMETHING ENORMOUS]\n"
                    "Where it sits: [BEAT AND CHAPTER FROM PROMPT 12]\n\n"
                    "Design the sequence:\n\n"
                    "1. THE GOAL: what my hero and crew are trying to do - specific, and losable.\n"
                    "2. THE CLOCK: the deadline, and it should be domestic wherever possible - before the "
                    "bell, before dinner, before the bus leaves, before a parent gets home. A kid-scale "
                    "clock beats a bomb every time.\n"
                    "3. THE PLACE: the space in concrete detail - what can be climbed, what is locked, "
                    "what is slippery, where a grown-up will appear from, what the power cannot do here.\n"
                    "4. EVERYONE'S JOB: what each crew member is doing during this sequence. Nobody waits "
                    "in the hideout.\n"
                    "5. THE CONSTRAINTS: which of my power's hard limits and costs bite, and when. List "
                    "them beat by beat - this is where the tension comes from.\n"
                    "6. WHAT GOES WRONG: two stages - a small thing they handle, then the real problem, "
                    "which must come from an established limit or from my hero's flaw, never from luck.\n"
                    "7. THE BEATS: 10-14 sequential beats, one sentence each, with the clock noted every "
                    "few beats.\n"
                    "8. THE SCARY LINE: confirm what stays inside my scary-axis score - what a reader sees "
                    "and what happens off the page. Name anything currently over the line.\n"
                    "9. THE FUNNY BEAT: one genuinely funny moment inside the sequence. Tension and comedy "
                    "together is the MG house style.\n"
                    "10. THE COST: what this costs - a broken thing, a grounding, a friendship strained, "
                    "an exhausted hero who sleeps through something important.\n"
                    "11. THE AFTER: the quiet scene straight afterwards, and the one thing said in it that "
                    "matters.\n\n"
                    "End by asking me which crew member saves it, because it should not always be my hero."
                ),
                "pro_tip": (
                    "Item 2 is the trick. A ten-year-old reader feels 'before Mum gets home' far more "
                    "acutely than 'before the city is destroyed', because they have actually lived the "
                    "first one."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 5: WRITE THE BOOK",
        "intro": (
            "Three prompts: a chapter plan built for short chapters and bedtime pulls, an opening chapter "
            "that starts fast, and a drafting engine with a read-aloud check built into every batch."
        ),
        "prompts": [
            {
                "title": "Chapter Outline with Cliffhangers",
                "desc": (
                    "MG pacing is a chapter-level craft. This prompt builds a plan of short chapters, each "
                    "with a job and a pull strong enough to win 'one more chapter' at bedtime."
                ),
                "prompt_text": (
                    "You are a novel outliner working in middle grade fiction. You understand that this "
                    "reader stops at chapter ends and decides whether to continue.\n\n"
                    "My beat sheet: [PASTE FROM PROMPT 12]\n"
                    "My crew and their jobs: [PASTE FROM PROMPT 9]\n"
                    "My set pieces: [LIST THOSE DESIGNED WITH PROMPT 13]\n"
                    "Target: [E.G. 42,000 WORDS IN 38 CHAPTERS OF ABOUT 1,100 WORDS]\n"
                    "Point of view: [FIRST PERSON PAST / FIRST PERSON PRESENT / CLOSE THIRD]\n\n"
                    "Build my CHAPTER OUTLINE. For every chapter give me:\n\n"
                    "1. Chapter number, a working title that a kid would want to read, and a target word "
                    "count.\n"
                    "2. Where it happens and who is in it.\n"
                    "3. The chapter's job in one sentence.\n"
                    "4. The turn: what is true at the end that was not true at the start.\n"
                    "5. Whether it is mostly funny, mostly exciting, or mostly feelings.\n"
                    "6. THE PULL: the last line's job - a question, a threat, a surprise, a door opening, "
                    "someone arriving. Every single chapter needs one.\n\n"
                    "Then check and flag: any chapter over 1,600 words (split it), any three consecutive "
                    "chapters with nothing funny, any chapter with no pull, any chapter where my hero is "
                    "only watching, any crew member absent for more than five chapters, and whether the "
                    "power chapter arrives by chapter three.\n\n"
                    "Then give me the SHAPE CHECK: list which chapters are funny, exciting and feelings, "
                    "and tell me whether the alternation works or whether I have three sad chapters in a "
                    "row.\n\n"
                    "End by asking me which chapter a reluctant reader would stop at, so I can fix it now."
                ),
                "pro_tip": (
                    "Chapter titles are marketing inside the book. A contents page a kid reads for fun - "
                    "'Chapter 7: In Which I Set Fire To The Wrong Shed' - sells the next chapter before "
                    "they get to it."
                ),
            },
            {
                "title": "The Opening Chapter",
                "desc": (
                    "MG openings have three chapters to win a reader and really only one. This prompt "
                    "drafts a first chapter that starts inside something happening."
                ),
                "prompt_text": (
                    "You are a novelist drafting the opening chapter of a middle grade superhero novel in "
                    "the voice described below.\n\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET, PLUS NOTES "
                    "ON YOUR OWN STYLE]\n"
                    "My protagonist, their want, worry and flaw: [PASTE FROM PROMPT 7]\n"
                    "My household: [PASTE FROM PROMPT 8]\n"
                    "My neighbourhood and its sensory kit: [FROM PROMPT 5]\n"
                    "My crew: [FROM PROMPT 9]\n"
                    "POV and tense: [SPECIFY]\n"
                    "Target length: [E.G. 1,000-1,400 WORDS]\n\n"
                    "Write chapter one, following these rules:\n\n"
                    "1. Open inside something already happening, with a problem on the first page.\n"
                    "2. Establish the want from Prompt 7 item 2 within the first two pages, concretely.\n"
                    "3. Put at least one crew member on the page, and make them funny.\n"
                    "4. Put one grown-up on the page who is real - noticing something, wanting something, "
                    "being slightly in the way.\n"
                    "5. Keep paragraphs to 3-5 sentences, with lots of dialogue.\n"
                    "6. Include at least two genuinely funny moments - ideally one physical.\n"
                    "7. Hint at the power or the trouble in the last quarter, without delivering it yet.\n"
                    "8. No explaining, no backstory paragraph, no describing the weather or the town for "
                    "its own sake.\n"
                    "9. End on the pull from my chapter outline.\n\n"
                    "After the chapter: read it aloud in your head and flag every sentence that is hard to "
                    "say. Then list what a reader knows about my hero after one chapter, and flag any line "
                    "that sounds like an adult writing a child, or any joke that is an adult's idea of what "
                    "kids find funny.\n\n"
                    "End by asking me whether a nine-year-old would start chapter two, and what specific "
                    "line makes them."
                ),
                "pro_tip": (
                    "Read the finished chapter out loud to an actual child if you possibly can. You will "
                    "know within ninety seconds whether the jokes land, and nothing else in the process "
                    "tells you that."
                ),
            },
            {
                "title": "The Batch Drafting Engine",
                "desc": (
                    "The prompt you will reuse most. It drafts four to six short chapters at a time while "
                    "holding voice, power costs, the crew's jobs, the grown-ups' suspicion and the "
                    "read-aloud rhythm."
                ),
                "prompt_text": (
                    "You are my drafting partner on a middle grade superhero novel. You write in my "
                    "established voice and hand control back to me at the end of every batch.\n\n"
                    "STANDING CONTEXT (reuse and update this block every batch):\n"
                    "- Voice sample: [PASTE 300-500 WORDS OF YOUR APPROVED CHAPTER ONE FROM PROMPT 15]\n"
                    "- Hero, want, worry and flaw: [FROM PROMPT 7, PLUS WHERE THEY ARE NOW]\n"
                    "- Power rules I must not break: [THE FIVE HARD LIMITS AND COSTS FROM PROMPT 2]\n"
                    "- Body and energy state: [TIRED, HURT, WHAT IS RECOVERING AND HOW LONG MY RULES SAY "
                    "IT TAKES]\n"
                    "- Crew status: [WHO KNOWS, WHO IS CROSS WITH WHOM, WHO IS GROUNDED]\n"
                    "- Grown-ups: [WHAT THEY NOW SUSPECT, FROM PROMPT 8; WHETHER THE TRUSTED ADULT KNOWS]\n"
                    "- Trouble level: [WHAT THE ANTAGONIST HAS DONE SO FAR AND WHAT THEY WANT NEXT]\n"
                    "- Where we are in the school term, and the time of day: [STATE IT]\n\n"
                    "THIS BATCH: write chapters [X] to [Y] from my outline:\n"
                    "[PASTE THE OUTLINE ENTRIES FROM PROMPT 14]\n\n"
                    "Rules for this batch:\n"
                    "1. Match the voice sample in rhythm and sentence length. Short paragraphs, plenty of "
                    "dialogue.\n"
                    "2. Never let the power exceed its hard limits or recover faster than my rules allow.\n"
                    "3. Something funny in every chapter, unless the outline says this is a sad one.\n"
                    "4. Every crew member present in the batch must do something useful.\n"
                    "5. At least one grown-up per batch notices something and acts on it.\n"
                    "6. My hero solves things themselves, with help - no adult rescues.\n"
                    "7. Stay inside the scary line and the hope floor from Prompt 1.\n"
                    "8. End every chapter on its pull.\n\n"
                    "After the chapters, give me: a STATUS REPORT (energy, crew, grown-ups' suspicion, "
                    "trouble level, time and date, anything I now owe the reader), and a READ-ALOUD FLAG "
                    "list - every sentence that is hard to say out loud, plus every joke that feels like an "
                    "adult wrote it.\n\n"
                    "End by asking me which chapter in this batch was the least fun, because that is the "
                    "one to fix."
                ),
                "pro_tip": (
                    "Keep the read-aloud flag list in every batch. It is the cheapest quality control in "
                    "middle grade, and it catches the long clause-stacked sentences that quietly creep in "
                    "when an adult writes for hours."
                ),
            },
        ],
    },

    {
        "name": "PHASE 6: FINISH IT",
        "intro": (
            "Two prompts to close out: one combined audit for age, read-aloud quality and power logic, and "
            "one that handles the blurb, the metadata and the series plan together."
        ),
        "prompts": [
            {
                "title": "The Age, Read-Aloud and Power-Logic Audit",
                "desc": (
                    "Three audits in one pass, because at this age band they fail together: content that "
                    "has drifted, prose that has got too old, and a power system a clever child can break."
                ),
                "prompt_text": (
                    "You are a middle grade editor who audits for age-band fit, read-aloud quality and "
                    "internal logic. You are merciless about all three.\n\n"
                    "My power system, hard limits, costs and skill curve: [PASTE FROM PROMPT 2]\n"
                    "My content calibration and scary axis: [PASTE FROM PROMPTS 1 AND 3]\n"
                    "My level spec: [PASTE THE LEVEL SPEC FROM THIS PACK'S CHEAT SHEET]\n"
                    "My grown-up world and the adult limit: [FROM PROMPT 4]\n"
                    "My manuscript or detailed chapter summaries: [PASTE - WORK IN SECTIONS IF LONG]\n\n"
                    "PART A - AGE AND CONTENT. Cite the chapter for every issue:\n"
                    "1. CONTENT DRIFT: anything outside the 8-12 range or my scary-axis score - violence, "
                    "injury detail, cruelty, grief, language, romance beyond a first crush, imagery that "
                    "would frighten without resolution.\n"
                    "2. THE HOPE FLOOR: every place the book currently dips below the floor I set in "
                    "Prompt 1, and how long it stays there before relief arrives.\n"
                    "3. THE CONDESCENSION SWEEP: explained jokes, stated morals, simplified feelings, a "
                    "narrator telling the reader how to feel, an adult delivering the theme.\n"
                    "4. THE AGENCY CHECK: every place an adult solves my hero's problem, or my hero is "
                    "rescued rather than deciding. This is the most important check in the audit.\n"
                    "5. CREW USEFULNESS: any friend who becomes a passenger, and where.\n"
                    "\n"
                    "PART B - READ-ALOUD AND LEVEL:\n"
                    "6. SENTENCE AUDIT: flag sentences over 25 words, paragraphs over 6 sentences, and any "
                    "sentence that is hard to say in one breath. Give me the worst 15 with rewrites.\n"
                    "7. CHAPTER LENGTH: flag every chapter over 1,600 words and propose the split point.\n"
                    "8. THE PULL CHECK: every chapter that does not end on a pull.\n"
                    "9. VOCABULARY: flag words that will genuinely stop a nine-year-old where the sentence "
                    "does not teach them. Keep the good hard words; fix the unsupported ones.\n"
                    "10. THE FUNNY MAP: mark where the laughs are. Flag any stretch of three chapters "
                    "without one.\n"
                    "\n"
                    "PART C - POWER AND LOGIC:\n"
                    "11. LIMIT BREACHES: every place the power does something the hard limits forbid.\n"
                    "12. COST EVASION: uses that should have cost more, injuries healing too fast, energy "
                    "that never runs out.\n"
                    "13. NEW-TRICK CLIMAX: any ability appearing near the end without setup.\n"
                    "14. THE OBVIOUS SOLUTION PROBLEM: any obstacle an established power should have "
                    "solved instantly.\n"
                    "15. THE 'WHY NOT TELL A GROWN-UP' TEST: go chapter by chapter and ask it. Every "
                    "chapter where the answer is not already on the page is a problem - list them.\n\n"
                    "Rank all findings CRITICAL, MODERATE or MINOR, with a fix for every CRITICAL.\n\n"
                    "End by asking me which critical fix needs a structural change, so I can plan that "
                    "repair before touching the prose."
                ),
                "pro_tip": (
                    "Item 15 is the audit that matters most in this subgenre. A clever ten-year-old asks "
                    "that question in every chapter, and a book that cannot answer it loses their trust "
                    "permanently around chapter twelve."
                ),
            },
            {
                "title": "Blurb, Metadata and Series Plan",
                "desc": (
                    "Everything needed to publish and to continue: retail copy aimed at a kid and their "
                    "gatekeeper, plus the series architecture MG readers reward more than any other age "
                    "band."
                ),
                "prompt_text": (
                    "You are a book marketing copywriter and series architect for middle grade fiction.\n\n"
                    "My reader promise, age target and calibration: [PASTE FROM PROMPT 3]\n"
                    "My hero, want, power and flaw: [PASTE FROM PROMPTS 2 AND 7]\n"
                    "My antagonist and the redemption decision: [FROM PROMPT 10]\n"
                    "My crew: [FROM PROMPT 9]\n"
                    "My ending: [FROM PROMPT 12]\n\n"
                    "PART A - THE RETAIL KIT:\n"
                    "1. THE BLURB: 100-150 words - shorter than adult copy. Open with the funny or the "
                    "exciting hook, name the hero and the power, name the trouble, end on a question. Write "
                    "it so a ten-year-old reads the whole thing.\n"
                    "2. THE FIRST LINE OF THE BLURB: give me 4 options. At this age band the first line "
                    "does almost all the work in a bookshop.\n"
                    "3. THE GATEKEEPER PARAGRAPH: a separate 60-80 word paragraph aimed at parents, "
                    "teachers and librarians - what the book is about underneath, what it handles, and why "
                    "it is a good read-aloud. Honest, not worthy.\n"
                    "4. AGE SIGNAL: the specific words and phrasing that tell a browser this is middle "
                    "grade and not YA or chapter book. Be concrete about the markers.\n"
                    "5. CATEGORIES: 6 retail categories ranked by how well I compete in each.\n"
                    "6. KEYWORDS: 20 search phrases grouped into trope, mood and situation terms, written "
                    "the way a parent or a kid would actually search.\n"
                    "7. COMP POSITIONING: 4 comparable reading experiences described as types of book, "
                    "each with a 'for readers who loved X but wanted Y' line.\n"
                    "8. THE COVER BRIEF: 5 visual directions tied to specific images from my book, 3 "
                    "clichés to forbid, and a judgement on whether the cover should be illustrated or "
                    "photographic, and whether it should be funny.\n"
                    "9. THE CHAPTER-TITLE PASS: if my chapter titles are plain, rewrite 6 of them to be "
                    "the kind a kid reads for fun.\n\n"
                    "PART B - THE SERIES:\n"
                    "10. THE SHAPE: recommend a series shape - a new trouble per book with the same crew, "
                    "one escalating arc, or standalone adventures - and justify it against my ending. Note "
                    "that MG readers reward long, consistent series more than any other age band.\n"
                    "11. THE POWER-CREEP CONTRACT: state what my hero's power will and will not become "
                    "across the series, then name 5 things to escalate instead - the crew's problems, a "
                    "harder antagonist reason, more of the world found out, a friendship at real risk, an "
                    "adult who is now involved. Commit in writing.\n"
                    "12. THE AGE PROBLEM: my hero will not stay twelve. Give me the three honest options - "
                    "keep them the same age across books, let them grow up and age the series with them, or "
                    "hand it to a younger character - with the cost of each, then recommend one.\n"
                    "13. BOOK TWO: a one-page premise - the new trouble, the returning cost from book one, "
                    "and a hook in the first two chapters. It must not undo book one's ending.\n"
                    "14. THE SEEDS: 6 things planted or plantable in book one that pay off later.\n"
                    "15. THE STANDALONE GUARANTEE: confirm book one ends properly. At this age band a "
                    "cliffhanger instead of a resolution reads as being cheated - flag anything that does "
                    "that.\n\n"
                    "End by asking me which promise in the blurb I am least confident the book delivers, so "
                    "we can fix the blurb or fix the book."
                ),
                "pro_tip": (
                    "Item 15 is not optional here. Adult and YA readers will tolerate a cliffhanger; a "
                    "ten-year-old feels tricked by one. Resolve book one completely, then make them want "
                    "book two because they miss the crew."
                ),
            },
        ],
    },
]
