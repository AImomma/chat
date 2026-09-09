# -*- coding: utf-8 -*-
"""
Royalti Studios - Cyberpunk Master Prompt Pack (Adult Fiction Line).

Build with:
    python pack_builder.py cyberpunk_pack_data \
        "Cyberpunk_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "CYBERPUNK",
    "total_prompts": 22,
    "hook_line": "High tech, low life - one expendable person versus a city that has already priced their body, their data, and their loyalty.",
    "keyword_lines": [
        "Neon • Chrome • Corps • The Net • Augmentation • Debt",
        "Street samurai • Hacker crews • Black clinics • Dirty jobs • Bad implants • Worse contracts",
    ],
    "subgenres_line": "Subgenres: Corporate Noir, Street-Level Heist, Netrunner/Hacker Thriller, Biopunk & Body Horror, AI Emergence, Post-Cyberpunk & Solarpunk-Adjacent, Cyber-Noir Detective, Chrome Western",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-09",
    "audience_line": "Adult Fiction Line",
    "cover_h2": "From Neon Concept to Published Novel",
    "closing_tagline": "The city always wins. The book is about what your character refuses to sell before it does.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "Cyberpunk is not a colour palette. It is an argument: technology accelerates, power concentrates, "
        "and the people at the bottom pay for both with their bodies. This pack builds that argument into a "
        "novel - a city with an economy, a corporate power structure that behaves like a real institution, "
        "an augmentation system with prices and consequences, a job that goes wrong, and a protagonist whose "
        "body is collateral. Work the prompts in order and save every output in one document. By Prompt 22 "
        "that document is your series bible."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-3) - Set the argument. Find your cyberpunk thesis, place yourself on the "
        "chrome-to-flesh axis, and lock the reader promise and shelf position.",
        "Phase 2 (Prompts 4-8) - Build the city. The corporate power map, the street economy, the "
        "augmentation and body-mod system, the net and its rules, and the sensory signature of your sprawl.",
        "Phase 3 (Prompts 9-12) - Cast the expendables. A protagonist with a body debt, the crew and their "
        "specialisations, the corporate antagonist who is just doing quarterly numbers, and the fixer who "
        "connects everyone.",
        "Phase 4 (Prompts 13-16) - Run the job. The contract, the heist or investigation architecture, the "
        "double-cross ladder, and the escalation that turns a job into a war.",
        "Phase 5 (Prompts 17-19) - Write the book. Chapter outline with hooks, an opening that teaches the "
        "city, and a batch-drafting engine that holds the voice and the tech rules steady.",
        "Phase 6 (Prompts 20-22) - Polish, publish, expand. A tech and continuity audit, a neon-noir voice "
        "pass, and the blurb, metadata and series architecture kit.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool and a place to save your outputs between prompts. Brackets like "
        "[THIS] are placeholders - replace them with your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular. Writing cyber-noir detective rather than a heist? "
        "Prompt 14 becomes an investigation structure. Writing biopunk with no net? Prompt 7 becomes a light "
        "pass on information control. Everything else runs the same."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "A thesis about technology and power that the plot argues, not a setting that merely looks futuristic",
            "Street level first - the story belongs to people the system has already written off",
            "Technology with a price tag: every implant, every run, every favour has a cost in money, body, or loyalty",
            "Corporations that behave like institutions - quarterly pressure, internal politics, legal departments, middle managers",
            "A city with working economics: who owns the water, the housing, the clinics, the network access",
            "Body horror kept intimate - the reader should feel the port site, the rejection, the maintenance schedule",
            "Information as the real currency, and a plot where knowing something is more dangerous than owning a gun",
            "A crew whose specialisations force interdependence and whose loyalties are purchasable",
            "Noir moral weather - nobody is clean, and the choice is always between two compromised outcomes",
            "A win that is small, local and personal against a system that continues unbothered",
        ],
        "kills": [
            "Aesthetic without argument - neon, rain and katanas draped over a story that has nothing to say about power",
            "Magic hacking, where the netrunner types fast and any door opens with no cost or countermeasure",
            "Corporations run by a single cackling executive with no board, no shareholders and no legal team",
            "Augmentation with upside only - chrome that never fails, never needs servicing, never costs anything",
            "A protagonist who can out-shoot, out-hack and out-fight everyone, which erases the genre's core power imbalance",
            "Exposition-dump worldbuilding delivered by a character explaining the city to someone who lives in it",
            "Nostalgia tech that dates the book - specify function, not brand-model numbers you invented",
            "The lone hero who topples a megacorp singlehandedly, which betrays the genre's central thesis",
            "Sex work, addiction and poverty used as scenery rather than as economics with people inside them",
            "An ending where the technology is simply destroyed, as if the problem were the machine rather than who owns it",
        ],
        "voice": [
            "Present-tense pressure even in past tense - short clauses, hard stops, forward motion",
            "Brand and product names as texture; people in this world talk in trademarks and model numbers",
            "Sensory specificity of the artificial: coolant smell, static taste, the hum of a bad power coupling",
            "Technical vocabulary used casually and never explained - readers should infer, not be taught",
            "Noir interiority - the narrator notices what it costs, and undercuts their own feelings",
            "Class register in dialogue: corporate speech is euphemism, street speech is compression and slang",
            "Body awareness as constant background - what aches, what needs charging, what is overdue for service",
            "One clean image of beauty per chapter, so the ugliness has something to measure against",
        ],
        "formula": (
            "The Body Debt (we meet a protagonist who owes something in flesh or money) -> The Contract "
            "(a job too good to refuse) -> The Crew Assembles -> The Run Begins -> First Complication "
            "(the intel was wrong) -> The Double-Cross -> The Thing They Actually Stole (the real payload "
            "revealed) -> Corporate Response (the system notices them) -> Burned (safehouses gone, crew "
            "scattered, body failing) -> The Choice: Sell It or Spend It -> The Counter-Move on Corporate "
            "Ground -> A Small Permanent Win -> The City, Unchanged, Still Running"
        ),
        "reader_expectations": (
            "Cyberpunk readers are buying momentum plus argument. They want a city they can smell, technology "
            "with rules and costs they can track, and a job structure that keeps pages turning - but they also "
            "want the book to mean something about who owns what. They expect the protagonist to lose most of "
            "the fight, because a genre about structural power that ends in a clean victory is a lie. What they "
            "will not forgive: hacking with no rules, corporations with no economics, and chrome with no price. "
            "What they reward: a specific city, a crew they would follow into a sequel, and a final win that is "
            "small enough to be believable and personal enough to hurt."
        ),
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "The city does not fall at the end of a cyberpunk novel. That is not a failure of ambition - it is the "
        "genre's honesty. What changes is one person, one crew, one block, one piece of information that gets "
        "out. You spent Phase 2 building an economy precisely so that the small win at the end lands as real "
        "rather than sentimental, and you spent Phase 4 taking things away so the reader knows what it cost. "
        "When a scene goes slack, check the price: someone is running on free chrome, free access, or free "
        "loyalty. Put the meter back on and the scene will bite. Now go finish the book - the sprawl is lit and "
        "the contract is on the table."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: SET THE ARGUMENT",
        "intro": (
            "Cyberpunk without a thesis is set dressing. These three prompts find the argument your book is "
            "making about technology and power, place you precisely within the genre's range, and turn that "
            "into a market position. Everything downstream refers back to this page."
        ),
        "prompts": [
            {
                "title": "Your Cyberpunk Thesis",
                "desc": (
                    "The genre exists to argue that technology concentrates power rather than distributing it. "
                    "This prompt finds the specific version of that argument only your book can make, and turns "
                    "it into a plot engine rather than a theme."
                ),
                "prompt_text": (
                    "You are a developmental editor who has worked on cyberpunk and near-future science fiction "
                    "for twenty years and who is impatient with aesthetic-only submissions.\n\n"
                    "My rough idea is: [DESCRIBE IN 2-4 SENTENCES - even if it is only an image or a vibe]\n\n"
                    "Do the following:\n\n"
                    "1. Extract MY THESIS: the specific claim about technology and power that my book will "
                    "argue. State it in one sentence of 25 words or fewer. If my idea currently has no thesis, "
                    "say so plainly and offer me three.\n"
                    "2. Name THE TECHNOLOGY AT THE CENTRE - the single innovation, system, or capability my "
                    "thesis depends on. Describe what it does in plain language, in three sentences, with no "
                    "invented jargon.\n"
                    "3. WHO WINS AND WHO PAYS: list the specific groups who profit from this technology and "
                    "the specific groups whose bodies, labour, or data are the input. Be concrete about the "
                    "transaction between them.\n"
                    "4. THE PLOT ENGINE: convert my thesis into a story situation - a job, a crime, a "
                    "disappearance, a leak, a debt - that would force a character to live the argument rather "
                    "than state it. Give me three options and recommend one.\n"
                    "5. THE CHEAP VERSION: describe the shallow, aesthetic-only version of my idea so I know "
                    "exactly what to avoid writing.\n\n"
                    "End by asking me which part of my original image or vibe I am unwilling to give up, so we "
                    "can make sure the thesis is built around it rather than over it."
                ),
                "pro_tip": (
                    "If your thesis can be stated as 'technology is bad', you do not have one yet. Push until "
                    "it names a transaction: whose data, whose body, whose labour, and what they get in "
                    "exchange."
                ),
            },
            {
                "title": "The Chrome-to-Flesh Axis",
                "desc": (
                    "Cyberpunk runs from full-chrome street action to biopunk body horror to post-cyberpunk "
                    "rebuilding. This prompt places you exactly, and tells you what your position obligates you "
                    "to do well."
                ),
                "prompt_text": (
                    "You are a genre specialist who maps cyberpunk subgenres for editors and agents.\n\n"
                    "My thesis and central technology: [PASTE FROM PROMPT 1]\n\n"
                    "Do the following:\n\n"
                    "1. Place my idea on the CHROME-TO-FLESH AXIS from 1 to 10, where 1 = purely biological "
                    "(biopunk, engineered bodies, wetware, plague economics) and 10 = purely digital and "
                    "mechanical (netrunning, AI, full-body prosthetics, virtual space). Explain the placement in "
                    "3-4 sentences.\n"
                    "2. Place me on the HOPE AXIS from 1 to 10, where 1 = classic nihilist noir and 10 = "
                    "post-cyberpunk rebuilding, where communities claw back some control. Say what each end "
                    "demands of my ending.\n"
                    "3. Name my primary subgenre and two secondaries from: corporate noir, street-level heist, "
                    "netrunner thriller, biopunk/body horror, AI emergence, cyber-noir detective, "
                    "post-cyberpunk. Justify each in one sentence.\n"
                    "4. Tell me what my position OBLIGATES. For a high chrome score, name the tech-rule rigour "
                    "readers will demand. For a low score, name the biological and medical rigour they will "
                    "demand. Then name the single thing writers at my position most often get wrong.\n"
                    "5. THE TIME HORIZON: how far from now is this - 10 years, 30, 80? Give me the pros and "
                    "cons of each for my thesis, then recommend one and name three details that will sell that "
                    "distance to a reader.\n\n"
                    "End by asking me whether I want readers to leave this book angry, sad, or oddly hopeful, "
                    "because that answer should set my hope-axis score, not the other way round."
                ),
                "pro_tip": (
                    "Near horizons are harder but hit harder. A book set fifteen years out has to survive the "
                    "reader's own knowledge of how things work today - and in exchange, it reads as a warning "
                    "rather than a fantasy."
                ),
            },
            {
                "title": "Reader Promise & Shelf Position",
                "desc": (
                    "This prompt turns your thesis and axis position into a market stance - who this is for, "
                    "what it promises, and which promises you cannot break."
                ),
                "prompt_text": (
                    "You are a publishing strategist positioning science fiction for adult readers.\n\n"
                    "My thesis: [PASTE FROM PROMPT 1]\n"
                    "My axis placement and subgenres: [PASTE FROM PROMPT 2]\n\n"
                    "Do the following:\n\n"
                    "1. Write my READER PROMISE in one paragraph, in the second person ('You will feel...').\n"
                    "2. Identify the 3 reader appeals I am leading with, from: heist and crew competence, "
                    "noir mystery, body horror, intellectual argument about power, street-level action, "
                    "AI and consciousness questions, romance under surveillance, revenge on an institution.\n"
                    "3. Write 3 one-line pitches in different registers: one hard-boiled and propulsive, one "
                    "literary and thematic, one that leads with the crew.\n"
                    "4. Name my ideal reader in a paragraph - not demographics, but what they have read "
                    "recently and what they are hungry for that the market is underserving.\n"
                    "5. List the 4 promises I must NOT break given this positioning, and the review complaint "
                    "each breach would generate, in the reviewer's own words.\n"
                    "6. Tell me which single element of my concept is the most commercially distinctive, and "
                    "how to make sure it appears in the first three chapters.\n\n"
                    "End by asking me which pitch sounds most like the book I actually want to write, since "
                    "that will govern the voice work in Phase 5."
                ),
                "pro_tip": (
                    "Keep the winning pitch visible while you draft. Cyberpunk worlds are seductive enough to "
                    "swallow a plot whole, and the one-liner is the fastest test for whether a chapter is "
                    "story or tourism."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: BUILD THE CITY",
        "intro": (
            "Your city is a machine for extracting value from bodies. These five prompts build its power "
            "structure, its street economy, its augmentation market, its information layer, and its sensory "
            "signature. Do this work properly and your plot will generate itself from the pressures you have "
            "installed."
        ),
        "prompts": [
            {
                "title": "The Corporate Power Map",
                "desc": (
                    "Corporations are your antagonist system, and they are only frightening when they behave "
                    "like real institutions. This prompt builds the power structure with economics, politics "
                    "and internal weakness."
                ),
                "prompt_text": (
                    "You are a worldbuilding consultant with a background in corporate strategy and political "
                    "economy.\n\n"
                    "My thesis and central technology: [PASTE FROM PROMPT 1]\n"
                    "My time horizon: [FROM PROMPT 2]\n\n"
                    "Build my CORPORATE POWER MAP:\n\n"
                    "1. THE MAJORS: 4-5 dominant corporations. For each - name, core business, what it "
                    "actually sells and to whom, its public reputation, and the ugly thing everyone suspects.\n"
                    "2. THE BALANCE: who is ascendant, who is declining, who is quietly desperate, and what "
                    "the current flashpoint between two of them is. My plot will live in that flashpoint.\n"
                    "3. WHAT REPLACED THE STATE: which public functions are now corporate - policing, "
                    "healthcare, water, courts, education, identity - and which ones are still nominally "
                    "public but underfunded. Name the seams where the two systems fail to meet.\n"
                    "4. THE INTERNAL STRUCTURE of the corporation my plot will target: the division that "
                    "matters, the executive under quarterly pressure, the compliance function, the security "
                    "arm and whether it is in-house or contracted, and the department everyone else resents.\n"
                    "5. THE PRESSURE: what this corporation is currently afraid of - a regulator, a rival, a "
                    "leak, a failing product line, a shareholder revolt. This is the lever my crew will pull.\n"
                    "6. THE VOCABULARY: 10 pieces of corporate euphemism used in this world for firing, "
                    "killing, surveilling, indenturing, and disposing.\n\n"
                    "End by asking me whether my protagonist has ever worked for one of these companies, "
                    "because an ex-insider changes the entire access structure of the plot."
                ),
                "pro_tip": (
                    "Give your target corporation a mundane, boring problem - a delayed product launch, an "
                    "audit, a merger. Villains with quarterly deadlines are far scarier than villains with "
                    "ambitions, because deadlines make institutions reckless."
                ),
            },
            {
                "title": "The Street Economy",
                "desc": (
                    "This prompt builds the ground level - how your characters eat, sleep, get paid, and stay "
                    "housed - so that their choices are driven by economics rather than by plot convenience."
                ),
                "prompt_text": (
                    "You are an urban economist consulting on a near-future city.\n\n"
                    "My corporate power map: [PASTE FROM PROMPT 4]\n"
                    "My protagonist's rough social position: [DESCRIBE - e.g. gig courier, unlicensed "
                    "medic, ex-corporate security, squatter]\n\n"
                    "Build my STREET ECONOMY:\n\n"
                    "1. THE MONEY: what currency people use, who controls it, what happens to someone with no "
                    "verified identity, and how the grey and black economies settle debts.\n"
                    "2. THE JOBS: 8 ways an ordinary person at street level earns, from legal to lethal, with "
                    "typical pay and typical risk for each.\n"
                    "3. THE COSTS: what a month costs my protagonist - housing, food, network access, power, "
                    "medical maintenance, protection money, transport. Give me actual numbers relative to the "
                    "pay rates in item 2, so the reader can feel the squeeze.\n"
                    "4. THE HOUSING: describe the four tiers of where people live in this city, from corporate "
                    "arcology to the worst option, in one vivid paragraph each.\n"
                    "5. THE DEBT SYSTEM: how a person becomes indentured here - medical debt, implant "
                    "financing, contract terms, family obligation - and what the endgame of unpaid debt looks "
                    "like.\n"
                    "6. THE SAFETY NET: what informal systems fill the gap - mutual aid, gangs, clinics, "
                    "religious groups, family - and what each one demands in return.\n\n"
                    "End by asking me how many days from destitution my protagonist currently is, because that "
                    "number is the real clock in act one."
                ),
                "pro_tip": (
                    "Write the monthly cost sheet and keep it beside you while drafting. Every time your "
                    "character accepts or refuses a job, the reader should be able to feel the arithmetic "
                    "behind the decision without you stating it."
                ),
            },
            {
                "title": "The Augmentation System",
                "desc": (
                    "Chrome without cost is the fastest way to lose a cyberpunk reader. This prompt builds an "
                    "augmentation market with prices, maintenance, failure modes and social meaning."
                ),
                "prompt_text": (
                    "You are a speculative technology consultant designing a consistent body-modification "
                    "system for a novel.\n\n"
                    "My chrome-to-flesh axis position: [FROM PROMPT 2]\n"
                    "My street economy and costs: [PASTE FROM PROMPT 5]\n\n"
                    "Build my AUGMENTATION SYSTEM:\n\n"
                    "1. THE TIERS: define 4 tiers of modification from cheap street work to corporate-grade, "
                    "with the price range, the quality difference, and who installs each.\n"
                    "2. THE CATALOGUE: 10 specific augmentations relevant to my story. For each: what it does, "
                    "what it costs, what it requires to run (power, coolant, drugs, calibration), and its "
                    "failure mode.\n"
                    "3. THE MAINTENANCE BURDEN: what an augmented person must do daily, weekly and monthly to "
                    "stay functional, and what happens when they cannot afford it.\n"
                    "4. THE BODY'S LIMIT: the biological ceiling - rejection, nerve damage, immune load, "
                    "psychological effects, the point at which more chrome makes a person less capable. Name "
                    "the condition that people in this world fear most.\n"
                    "5. THE SOCIAL READ: what visible augmentation signals about class, occupation and legal "
                    "status. How does a corporate employee's chrome differ from a courier's on sight?\n"
                    "6. THE BLACK CLINIC: describe one specific unlicensed clinic my characters use - the "
                    "person who runs it, what they are good at, what they are dangerous at, and what they want.\n"
                    "7. MY PROTAGONIST'S LOADOUT: given all the above, list what my protagonist actually has "
                    "installed, what it cost them, what it still costs them monthly, and what is currently "
                    "overdue.\n\n"
                    "End by asking me which augmentation my protagonist will lose during the book, because "
                    "planning that now lets me establish its value in act one."
                ),
                "pro_tip": (
                    "Decide early what the maintenance smells like, sounds like, or feels like. A recurring "
                    "physical sensation - a hot port, a click in the wrist, an eye that needs recalibrating in "
                    "cold weather - does more for immersion than any spec sheet."
                ),
            },
            {
                "title": "The Net and Its Rules",
                "desc": (
                    "Hacking with no rules destroys tension. This prompt defines what the network is, what it "
                    "costs to enter, what defends it, and what a run actually feels like from the inside."
                ),
                "prompt_text": (
                    "You are a systems designer building a consistent, tension-preserving network layer for a "
                    "cyberpunk novel. You are hostile to hand-waving.\n\n"
                    "My chrome-to-flesh axis and time horizon: [FROM PROMPT 2]\n"
                    "My corporate power map: [PASTE FROM PROMPT 4]\n\n"
                    "Build my NET RULES:\n\n"
                    "1. WHAT IT IS: describe the network layer in plain language - is it immersive, "
                    "overlay-based, purely conventional infrastructure, or something else? Three sentences, no "
                    "invented jargon.\n"
                    "2. ACCESS: what hardware and permissions a person needs to operate at each level, what it "
                    "costs, and what an unlicensed connection looks like.\n"
                    "3. THE FOUR CONSTRAINTS: define the hard limits that keep hacking from solving every "
                    "plot - time, physical proximity, detection risk, and one more specific to my world. State "
                    "each as a rule I can never break.\n"
                    "4. THE DEFENCES: 6 countermeasures a serious target deploys, from passive to lethal, and "
                    "the specific counter-tactic for each. Include at least two that are human rather than "
                    "technical.\n"
                    "5. THE COST OF A RUN: what a serious intrusion takes out of the runner physically, "
                    "financially and legally. Include the recovery time.\n"
                    "6. WHAT CANNOT BE HACKED: 5 things in my world that are deliberately analogue, "
                    "air-gapped or human-verified, and why. These are where my plot's real difficulty lives.\n"
                    "7. THE SENSORY GRAMMAR: how I will describe a run on the page without resorting to "
                    "cliched neon-grid metaphors. Give me three fresh approaches and one paragraph of sample "
                    "prose in each.\n\n"
                    "End by asking me whether my protagonist can run the net themselves, because if they can, "
                    "item 6 has to carry the entire weight of my plot's difficulty."
                ),
                "pro_tip": (
                    "The list at item 6 is the most valuable output in this phase. A world where the payroll "
                    "server is air-gapped and the courier is human is a world where your crew has to walk in "
                    "the front door - which is where stories happen."
                ),
            },
            {
                "title": "The Sensory Signature of the Sprawl",
                "desc": (
                    "Every cyberpunk city risks reading like every other one. This prompt gives yours a "
                    "specific, ownable physical identity built from climate, industry, history and decay."
                ),
                "prompt_text": (
                    "You are a setting specialist who makes fictional cities feel like specific places rather "
                    "than genre wallpaper.\n\n"
                    "My city so far: [PASTE FROM PROMPTS 4-5]\n"
                    "Real-world region or climate it resembles, if any: [SPECIFY OR SAY 'YOU CHOOSE']\n\n"
                    "Build my CITY'S SIGNATURE:\n\n"
                    "1. THE HISTORY IN THE ARCHITECTURE: what this city was before, and what physical traces "
                    "of that remain - industry, war, water, migration, a disaster.\n"
                    "2. THE CLIMATE: the weather that defines daily life, how people dress and move because of "
                    "it, and what that weather does to technology.\n"
                    "3. THE FIVE DISTRICTS: name and describe 5 districts in a paragraph each - who lives "
                    "there, who owns it, what it smells like, and its one unmistakable landmark.\n"
                    "4. THE SENSORY KIT: for each district, one sound, one smell, one texture and one visual "
                    "detail that identifies it instantly without a location tag.\n"
                    "5. THE FOOD: what people actually eat here, at three price points, with specific dish "
                    "names. Food is the fastest shortcut to a city that feels real.\n"
                    "6. THE LANGUAGE: 12 pieces of local slang for money, police, corporate employees, "
                    "augmented people, unaugmented people, outsiders, and getting killed.\n"
                    "7. THE ANTI-CLICHE PASS: list the 8 most overused cyberpunk city images and give me a "
                    "specific replacement for each drawn from the material above.\n\n"
                    "End by asking me which district my protagonist avoids, and why, so we can plan the "
                    "chapter that forces them into it."
                ),
                "pro_tip": (
                    "Ration the rain. If it is always night and always raining, the reader stops seeing the "
                    "city. One hot, dry, bright chapter will make your neon-and-drizzle scenes land twice as "
                    "hard."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: CAST THE EXPENDABLES",
        "intro": (
            "Cyberpunk casts are built from specialisation and debt. These four prompts give you a "
            "protagonist whose body is collateral, a crew who need each other and cannot fully trust each "
            "other, an antagonist who is simply doing their job well, and the fixer who sits between "
            "everyone and takes a cut."
        ),
        "prompts": [
            {
                "title": "The Protagonist and the Body Debt",
                "desc": (
                    "The strongest cyberpunk protagonists are already mortgaged - to a clinic, a contract, a "
                    "corporation, or their own hardware. This prompt builds that debt and the arc that pays it."
                ),
                "prompt_text": (
                    "You are a character-development editor for noir and science fiction.\n\n"
                    "My street economy and augmentation system: [PASTE FROM PROMPTS 5-6]\n"
                    "My rough protagonist idea: [DESCRIBE, or say 'you choose']\n\n"
                    "Build my PROTAGONIST:\n\n"
                    "1. THE BASICS: name, age, what they do for money, where they sleep, who they are "
                    "responsible for.\n"
                    "2. THE BODY DEBT: what they owe and to whom - a financed implant, a clinic bill, a "
                    "contract with a termination clause, a favour that has not been called yet. State the exact "
                    "amount or the exact terms.\n"
                    "3. THE COMPETENCE: their professional specialisation, described precisely enough that I "
                    "can write them working. Three things they are genuinely excellent at and the one thing "
                    "everyone assumes they can do that they cannot.\n"
                    "4. THE PAST EMPLOYMENT: what they did before, why it ended, and who from that life is "
                    "still out there. In this genre, the past is always a creditor.\n"
                    "5. THE LINE: the one thing they will not do for money. Name it precisely, because act "
                    "three will require them to stand on it or cross it.\n"
                    "6. THE ARC: five stages from mercenary self-interest to a chosen loyalty, each triggered "
                    "by a specific external event rather than a change of heart.\n"
                    "7. THE ANCHOR: the person, place, or piece of hardware they will not sell. This is what "
                    "the antagonist will eventually put on the table.\n\n"
                    "End by asking me whether my protagonist gets to keep the anchor, because that decision "
                    "sets the emotional temperature of the whole book."
                ),
                "pro_tip": (
                    "Make the debt small enough to be humiliating rather than epic. A character who could be "
                    "destroyed by a four-figure clinic bill is far more gripping than one being hunted by a "
                    "continent-spanning conspiracy."
                ),
            },
            {
                "title": "The Crew",
                "desc": (
                    "A cyberpunk crew is an interlocking set of specialisations where every member is also a "
                    "liability. This prompt builds one where dependence and distrust are the same structure."
                ),
                "prompt_text": (
                    "You are an ensemble developer for heist and crime fiction.\n\n"
                    "My protagonist: [PASTE FROM PROMPT 9]\n"
                    "My net rules and their limits: [PASTE FROM PROMPT 7]\n"
                    "My city districts: [FROM PROMPT 8]\n\n"
                    "Build my CREW of 3-5 characters. Cover the specialisations my plot actually needs given "
                    "the net constraints in Prompt 7 - do not default to the standard roster if my world makes "
                    "a role unnecessary. For each member:\n\n"
                    "1. Name, age, district, and the specialisation they own outright.\n"
                    "2. THE INDISPENSABILITY: the specific thing the job cannot be done without them.\n"
                    "3. THE LIABILITY: their addiction, debt, grudge, ex-employer, failing hardware, or "
                    "family obligation - the thing an enemy could use.\n"
                    "4. THE PRICE: what would actually buy their loyalty away from the crew. Everyone has a "
                    "number or a name; give me theirs.\n"
                    "5. THEIR HISTORY WITH MY PROTAGONIST: how they met, what is owed between them in which "
                    "direction, and the thing neither has said.\n"
                    "6. THE HUMANISING DETAIL: something impractical they still care about.\n\n"
                    "Then: identify which two crew members should not be left alone together and why, name the "
                    "one whose skill overlaps with another's (so I can cut or differentiate), and tell me which "
                    "member I am most likely to under-write.\n\n"
                    "End by asking me which crew member the reader is supposed to love most, so we can decide "
                    "whether the book is brave enough to spend them."
                ),
                "pro_tip": (
                    "Assign every crew member a different answer to 'what would you do with real money?' It is "
                    "the fastest way to make an ensemble argue in character, and it pre-loads every "
                    "double-cross in Phase 4."
                ),
            },
            {
                "title": "The Corporate Antagonist",
                "desc": (
                    "Your antagonist is not a villain - they are a competent professional with a mandate. This "
                    "prompt builds someone the reader recognises from their own working life, which is what "
                    "makes them frightening."
                ),
                "prompt_text": (
                    "You are an editor who specialises in institutional antagonists.\n\n"
                    "My corporate power map and the target company: [PASTE FROM PROMPT 4]\n"
                    "My protagonist: [PASTE FROM PROMPT 9]\n\n"
                    "Build my ANTAGONIST LAYER:\n\n"
                    "1. THE MANDATE: state in two sentences what the corporation actually wants, in business "
                    "terms. Not domination - a number, a launch date, a suppressed liability, an acquisition.\n"
                    "2. THE MANAGER: create the person responsible for delivering that mandate. Name, title, "
                    "how long they have held the role, what happens to them personally if they fail, and how "
                    "they speak.\n"
                    "3. THE JUSTIFICATION: 150-200 words in their voice explaining why what they are doing is "
                    "reasonable and even beneficial. It must contain one point that is genuinely true.\n"
                    "4. THE ASSET: the operative they send after my crew - a contractor, an in-house security "
                    "specialist, an investigator, an AI, a former colleague of my protagonist. Give them a "
                    "professional style and one weakness that is a consequence of their competence.\n"
                    "5. THE ESCALATION POLICY: how the corporation responds at each stage of trouble - "
                    "ignore, legal, financial pressure, contractor, in-house wet work. State what triggers each "
                    "escalation, so my plot has a predictable machine to push against.\n"
                    "6. THE INTERNAL ENEMY: someone inside the corporation who would benefit from the "
                    "manager's failure, and what my crew could offer them.\n\n"
                    "End by asking me whether my protagonist and the manager ever meet face to face before the "
                    "climax, because one civil, almost pleasant conversation in act two is worth three "
                    "shootouts."
                ),
                "pro_tip": (
                    "Item 5 is a gift to your plotting. Once escalation has published triggers, your crew can "
                    "make tactical choices about how much heat to draw - and every reader loves watching "
                    "characters decide how loud to be."
                ),
            },
            {
                "title": "The Fixer and the Favour Economy",
                "desc": (
                    "Fixers are the connective tissue of this genre - the reason a crew gets a job, gets "
                    "burned, and gets a way out. This prompt builds yours plus the wider network of obligation."
                ),
                "prompt_text": (
                    "You are a plot architect specialising in criminal networks and information brokers.\n\n"
                    "My crew: [PASTE FROM PROMPT 10]\n"
                    "My city and its districts: [FROM PROMPT 8]\n"
                    "My corporate structure: [FROM PROMPT 4]\n\n"
                    "Build my FAVOUR ECONOMY:\n\n"
                    "1. THE FIXER: name, base of operations, how they present themselves, how they actually "
                    "make money, and what they are protecting. Include the reason they use my crew rather than "
                    "someone cheaper.\n"
                    "2. THE FIXER'S CONSTRAINT: who the fixer answers to or is afraid of. A fixer with no "
                    "leash is a plot hole.\n"
                    "3. THE NETWORK: 6 other contacts my crew can call on - a medic, a document forger, a "
                    "hardware supplier, an information broker, a transport specialist, and one wildcard. For "
                    "each: what they provide, what they charge, and the condition under which they will refuse.\n"
                    "4. THE LEDGER: what my crew currently owes and is owed across this network, and who is "
                    "overdue.\n"
                    "5. THE INFORMATION MARKET: what a piece of information is worth here relative to money, "
                    "who buys, and how a seller proves they have something without giving it away.\n"
                    "6. THE BURN PROTOCOL: what happens to a crew that becomes too hot to work with - how the "
                    "network cuts them off, in what order, and which contact holds out longest.\n\n"
                    "End by asking me which contact is going to sell my crew out, and whether the reader should "
                    "suspect them beforehand."
                ),
                "pro_tip": (
                    "Item 6 is your act-three engine. Watching the network close one door at a time is more "
                    "tense than any chase scene, because the reader can count the doors remaining."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: RUN THE JOB",
        "intro": (
            "Now the structure. These four prompts build the contract that starts everything, the "
            "architecture of the run or investigation, the double-cross ladder that turns it inside out, and "
            "the corporate escalation that turns a job into a war your crew cannot win conventionally."
        ),
        "prompts": [
            {
                "title": "The Contract",
                "desc": (
                    "Every cyberpunk plot starts with a job that is too good, too strange, or too urgent. "
                    "This prompt designs the contract and, crucially, what it is really for."
                ),
                "prompt_text": (
                    "You are a story architect for heist and crime fiction.\n\n"
                    "My thesis: [PASTE FROM PROMPT 1]\n"
                    "My protagonist's body debt: [PASTE FROM PROMPT 9]\n"
                    "My fixer: [PASTE FROM PROMPT 12]\n"
                    "My target corporation and its pressure: [PASTE FROM PROMPTS 4 AND 11]\n\n"
                    "Design THE CONTRACT:\n\n"
                    "1. THE STATED JOB: what my crew is hired to do, for how much, by when, and what the "
                    "client claims to want it for. One paragraph.\n"
                    "2. WHY THEM: the specific reason this crew and no other - a skill, an access, a history, "
                    "or expendability. Be honest about which.\n"
                    "3. THE REAL JOB: what the payload actually is and what it is really for. This must "
                    "connect to my thesis from Prompt 1 - the object at the centre of the plot should embody "
                    "the argument the book is making.\n"
                    "4. WHY THEY CAN'T REFUSE: the pressure that makes this contract unrefusable given the "
                    "protagonist's debt and the crew's liabilities.\n"
                    "5. THE WARNING SIGNS: 5 details visible at the briefing that will look damning on "
                    "reread - a payment that is too high, a detail the client should not know, a deadline that "
                    "matches something else.\n"
                    "6. THE OBJECT: describe the payload physically. If it is data, give it a container, a "
                    "size, a transfer time, and a reason it cannot simply be copied and sent.\n\n"
                    "End by asking me whether my crew ever learns what the payload really was, because a book "
                    "where they never find out is a very different and sometimes better book."
                ),
                "pro_tip": (
                    "Item 6 matters more than writers expect. Data that can be emailed has no story in it. "
                    "Give the payload weight, latency, a physical carrier, or a living host, and your plot "
                    "gets a spine."
                ),
            },
            {
                "title": "The Run: Heist or Investigation Architecture",
                "desc": (
                    "This prompt builds the central operation in full - the plan, the terrain, the failure "
                    "points, and the two-stage collapse that turns competence into desperation."
                ),
                "prompt_text": (
                    "You are a heist and procedural architect. If my book is an investigation rather than a "
                    "heist, translate every step below into its investigative equivalent - the plan becomes a "
                    "line of inquiry, the security becomes what people will not say, the alarm becomes the "
                    "moment the subject learns they are being looked at.\n\n"
                    "My contract: [PASTE FROM PROMPT 13]\n"
                    "My crew and their specialisations: [PASTE FROM PROMPT 10]\n"
                    "My net rules and what cannot be hacked: [PASTE FROM PROMPT 7]\n"
                    "My corporate escalation policy: [PASTE FROM PROMPT 11 ITEM 5]\n\n"
                    "Build THE RUN:\n\n"
                    "1. THE TARGET: describe the site or the subject in operational detail - layout, staffing "
                    "patterns, access control, the human element, and the thing nobody thought to secure.\n"
                    "2. THE RECON: 4 things my crew learns beforehand, how they learn each one, and the cost "
                    "or risk of each.\n"
                    "3. THE PLAN: the crew's approach in 6-8 steps, with each member's role and the "
                    "assumption the whole plan rests on.\n"
                    "4. THE FIRST FAILURE: a complication in the first third that the crew absorbs, and what "
                    "it costs them to absorb it.\n"
                    "5. THE REAL FAILURE: the point at which the plan stops existing. It must come from the "
                    "assumption in item 3 being wrong, not from bad luck.\n"
                    "6. THE IMPROVISATION: how they get out, who takes the damage, and what they leave behind "
                    "that will be traced back to them.\n"
                    "7. THE BEATS: 12-16 sequential beats of the whole sequence, one sentence each, with the "
                    "resource clock (time, power, ammunition, exposure) noted every few beats.\n\n"
                    "End by asking me which crew member's plan-role fails, because whoever fails here should "
                    "be the one who redeems it in act three."
                ),
                "pro_tip": (
                    "Never let the plan fail because of a coincidence. It has to fail because the crew "
                    "believed something reasonable that was not true - that is the difference between a "
                    "thriller and a series of accidents."
                ),
            },
            {
                "title": "The Double-Cross Ladder",
                "desc": (
                    "Cyberpunk plots turn on stacked betrayals. This prompt builds a ladder where each reveal "
                    "recontextualises the last, without collapsing into incoherence."
                ),
                "prompt_text": (
                    "You are a plot architect who specialises in layered betrayal without confusing the "
                    "reader.\n\n"
                    "My contract and the real job: [PASTE FROM PROMPT 13]\n"
                    "My crew and their prices: [PASTE FROM PROMPT 10]\n"
                    "My fixer and network: [PASTE FROM PROMPT 12]\n"
                    "My run: [PASTE FROM PROMPT 14]\n\n"
                    "Build my DOUBLE-CROSS LADDER:\n\n"
                    "1. THE RUNGS: design exactly three betrayals, no more. For each: who does it, when it is "
                    "committed, when it is revealed, their entirely rational reason, and what it "
                    "recontextualises about earlier scenes.\n"
                    "2. THE ORDER: sequence the reveals for maximum effect and explain why that order. The "
                    "smallest betrayal should land first and the most personal one last.\n"
                    "3. THE CLARITY CHECK: for each rung, state in one plain sentence what the reader now "
                    "knows. If any of the three cannot be stated plainly, simplify it.\n"
                    "4. THE PLANTING: 8 details to seed earlier that read innocently first time - a phrasing, "
                    "an absence, a payment, a piece of knowledge, a hesitation. Say roughly where each goes.\n"
                    "5. THE FALSE SUSPECT: who the reader will suspect instead, what makes them look guilty, "
                    "and the scene that clears them.\n"
                    "6. THE UNBETRAYED: the one character who stays loyal throughout, and what it costs them. "
                    "Every stack of betrayals needs one fixed point or the reader stops caring.\n\n"
                    "End by asking me whether my protagonist commits one of these betrayals, because a "
                    "protagonist who does is the more interesting book and the harder one to land."
                ),
                "pro_tip": (
                    "Three rungs is the ceiling. A fourth reveal does not double the tension - it tells the "
                    "reader nothing on the page can be trusted, and once they stop trusting the page they "
                    "stop reading it."
                ),
            },
            {
                "title": "Corporate Response and the Endgame",
                "desc": (
                    "This prompt escalates from a burned job to a war your crew cannot win conventionally, and "
                    "designs the asymmetric ending the genre demands."
                ),
                "prompt_text": (
                    "You are a story architect closing out a cyberpunk novel.\n\n"
                    "My escalation policy: [PASTE FROM PROMPT 11 ITEM 5]\n"
                    "My double-cross ladder: [PASTE FROM PROMPT 15]\n"
                    "My burn protocol: [PASTE FROM PROMPT 12 ITEM 6]\n"
                    "My protagonist's line and anchor: [PASTE FROM PROMPT 9]\n"
                    "My thesis: [FROM PROMPT 1]\n\n"
                    "Build my ENDGAME:\n\n"
                    "1. THE SQUEEZE: 6 escalating moves the corporation makes, in order, each one drawn from "
                    "the escalation policy. Show the crew's options narrowing with each move.\n"
                    "2. THE LOSSES: what my crew loses at each stage - safehouses, contacts, hardware, "
                    "members, body parts. Nothing should be recoverable.\n"
                    "3. THE ALL-IS-LOST: the moment the anchor from Prompt 9 is taken or threatened, and what "
                    "the corporation offers in exchange for the payload.\n"
                    "4. THE ASYMMETRIC MOVE: my crew cannot beat this corporation in a fight, so design the "
                    "move that works instead - publication, a regulator, a rival corporation, an internal "
                    "enemy from Prompt 11 item 6, a market consequence, a personal ruin. Give me three "
                    "options with their costs, then recommend one that best serves my thesis.\n"
                    "5. THE PRICE OF WINNING: what this move costs my protagonist permanently. In this genre "
                    "the win must be paid for in body, freedom, relationship, or self-image.\n"
                    "6. THE SMALL PERMANENT CHANGE: what is actually different afterwards. Be specific and "
                    "modest - one clinic that stays open, one person out of a contract, one document in "
                    "public. Then state plainly what has NOT changed.\n"
                    "7. THE LAST IMAGE: the final scene, showing both the change and the city continuing "
                    "regardless.\n\n"
                    "End by asking me whether my protagonist is still in the same city on the last page, "
                    "because leaving and staying are two different arguments about my thesis."
                ),
                "pro_tip": (
                    "Item 6's second half - what has not changed - is what separates cyberpunk from a "
                    "superhero story. Name it explicitly in your final chapter and readers will call your "
                    "ending honest rather than bleak."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 5: WRITE THE BOOK",
        "intro": (
            "Structure becomes prose. These three prompts turn your endgame into a chapter plan, draft an "
            "opening that teaches the city without explaining it, and give you a reusable engine for drafting "
            "in batches while holding voice, tech rules and the resource clock steady."
        ),
        "prompts": [
            {
                "title": "Chapter Outline with Hooks",
                "desc": (
                    "This prompt converts the run and the endgame into a chapter-by-chapter plan where every "
                    "chapter has a job, a turn, a price, and a reason to keep reading."
                ),
                "prompt_text": (
                    "You are a novel outliner working in crime and science fiction.\n\n"
                    "My run: [PASTE FROM PROMPT 14]\n"
                    "My double-cross ladder: [PASTE FROM PROMPT 15]\n"
                    "My endgame: [PASTE FROM PROMPT 16]\n"
                    "Target: [E.G. 95,000 WORDS IN 45 CHAPTERS OF ABOUT 2,100 WORDS]\n"
                    "Point of view: [FIRST PERSON PRESENT / THIRD LIMITED PAST / MULTI-POV - and who]\n\n"
                    "Build my CHAPTER OUTLINE. For every chapter give me:\n\n"
                    "1. Chapter number and working title.\n"
                    "2. POV character and district (using a district name from Prompt 8).\n"
                    "3. The chapter's job in one sentence.\n"
                    "4. The turn: what is true at the end that was not true at the start.\n"
                    "5. The price paid in this chapter - money, body, exposure, a favour spent, a contact "
                    "burned - or 'none' if it is a breath chapter.\n"
                    "6. The closing hook, as a one-line description.\n\n"
                    "Then flag: any chapter that is only travel or exposition, any three consecutive chapters "
                    "in the same district, any stretch of more than four chapters with no price paid, and any "
                    "place where a double-cross reveal lands too close to another.\n\n"
                    "End by asking me where my quiet chapters are, because a book that is all pressure reads "
                    "as flat as one with none."
                ),
                "pro_tip": (
                    "Put a breath chapter immediately before each double-cross reveal. Readers need a moment "
                    "of apparent safety to fall for, or the betrayal lands as noise rather than as a hit."
                ),
            },
            {
                "title": "The Opening Chapter",
                "desc": (
                    "Chapter one has to teach the city, the tech rules and the voice while a story is already "
                    "moving. This prompt drafts it with no exposition dump and no tourist gaze."
                ),
                "prompt_text": (
                    "You are a novelist drafting the opening chapter of a cyberpunk novel in the voice "
                    "described below.\n\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET, PLUS NOTES ON "
                    "YOUR OWN STYLE]\n"
                    "My protagonist and their body debt: [PASTE FROM PROMPT 9]\n"
                    "My city sensory kit and slang: [PASTE FROM PROMPT 8]\n"
                    "My augmentation loadout for the protagonist: [PASTE FROM PROMPT 6 ITEM 7]\n"
                    "POV and tense: [SPECIFY]\n"
                    "Target length: [E.G. 2,000-2,500 WORDS]\n\n"
                    "Write chapter one, following these rules:\n\n"
                    "1. Open on my protagonist working - doing the job that pays their rent, mid-task.\n"
                    "2. Establish the body debt through a concrete, physical detail rather than a thought - a "
                    "maintenance warning, a declined payment, a port that will not seal.\n"
                    "3. Use at least four pieces of in-world slang and two pieces of technical vocabulary in "
                    "context, none of them explained.\n"
                    "4. Show the class structure through one interaction, not through narration.\n"
                    "5. Give me the district's sensory kit - one sound, one smell, one texture - without a "
                    "location tag.\n"
                    "6. Include one image of genuine beauty.\n"
                    "7. Introduce the pressure that will make the contract in Prompt 13 unrefusable.\n"
                    "8. End on the hook from my chapter outline.\n\n"
                    "After the chapter, list the world rules a reader can infer from it, and flag anything I "
                    "explained that I should have implied.\n\n"
                    "End by asking me which line sounds most like generic cyberpunk rather than my book, so I "
                    "can replace it before the voice sets."
                ),
                "pro_tip": (
                    "Delete your first paragraph after drafting. Nine times out of ten it is throat-clearing "
                    "about the skyline, and the real opening is the sentence where your protagonist touches "
                    "something."
                ),
            },
            {
                "title": "The Batch Drafting Engine",
                "desc": (
                    "The prompt you will reuse most. It drafts three to five chapters at a time while holding "
                    "voice, tech rules, money, body condition and the favour ledger consistent."
                ),
                "prompt_text": (
                    "You are my drafting partner on a cyberpunk novel. You write in my established voice and "
                    "hand control back to me at the end of every batch.\n\n"
                    "STANDING CONTEXT (reuse and update this block every batch):\n"
                    "- Voice sample: [PASTE 300-500 WORDS OF YOUR APPROVED CHAPTER ONE FROM PROMPT 18]\n"
                    "- Protagonist and arc stage: [FROM PROMPT 9, PLUS WHERE THEY ARE NOW]\n"
                    "- Body status: [WHAT IS INSTALLED, WHAT IS DAMAGED, WHAT MAINTENANCE IS OVERDUE]\n"
                    "- Money: [CURRENT BALANCE AGAINST THE MONTHLY COSTS FROM PROMPT 5]\n"
                    "- Crew status: [WHO IS ALIVE, WHO IS TRUSTED, WHO IS COMPROMISED]\n"
                    "- Favour ledger: [WHO IS OWED, WHO OWES, WHICH CONTACTS ARE BURNED - FROM PROMPT 12]\n"
                    "- Heat level: [WHERE THE CORPORATION IS ON ITS ESCALATION POLICY, FROM PROMPT 11]\n"
                    "- Net rules I must not break: [THE FOUR CONSTRAINTS AND THE UNHACKABLE LIST FROM PROMPT 7]\n\n"
                    "THIS BATCH: write chapters [X] to [Y] from my outline:\n"
                    "[PASTE THE OUTLINE ENTRIES FROM PROMPT 17]\n\n"
                    "Rules for this batch:\n"
                    "1. Match the voice sample in rhythm, sentence length and level of interiority.\n"
                    "2. Never solve a problem with technology in a way that breaks the four constraints.\n"
                    "3. Every chapter spends something specific - money, body, exposure, or a favour.\n"
                    "4. Use trademarks, model names and slang as texture; explain nothing.\n"
                    "5. Corporate characters speak in euphemism; street characters speak in compression.\n"
                    "6. End each chapter on its outlined hook.\n\n"
                    "After the chapters, give me a STATUS REPORT: money, body condition, heat level, favours "
                    "spent, time elapsed, and any promise you made on the page that I now owe the reader.\n\n"
                    "End by asking me which chapter drifted furthest from my voice, so the next batch does not "
                    "inherit the drift."
                ),
                "pro_tip": (
                    "Never skip updating the heat level between batches. It is the single number that keeps a "
                    "cyberpunk middle from feeling like a series of errands, because it tells you how loudly "
                    "the world is allowed to react."
                ),
            },
        ],
    },

    {
        "name": "PHASE 6: POLISH, PUBLISH, EXPAND",
        "intro": (
            "The last three prompts protect your reviews and set up what comes next: a tech-rule and "
            "continuity audit, a neon-noir line pass that strips the genre's default clichés out of your "
            "prose, and a combined publishing and series kit."
        ),
        "prompts": [
            {
                "title": "Tech Rules and Continuity Audit",
                "desc": (
                    "Cyberpunk readers audit your technology for free and complain about it publicly. This "
                    "prompt finds the breaches before they do."
                ),
                "prompt_text": (
                    "You are a continuity editor who specialises in near-future science fiction and who is "
                    "merciless about technology that solves problems it should not be able to solve.\n\n"
                    "My net rules and the four constraints: [PASTE FROM PROMPT 7]\n"
                    "My augmentation system: [PASTE FROM PROMPT 6]\n"
                    "My street economy and costs: [PASTE FROM PROMPT 5]\n"
                    "My corporate escalation policy: [PASTE FROM PROMPT 11]\n"
                    "My manuscript or detailed chapter summaries: [PASTE - WORK IN SECTIONS IF LONG]\n\n"
                    "Audit for the following, citing the chapter for every issue:\n\n"
                    "1. NET BREACHES: every place a character does something the four constraints forbid, or "
                    "accesses something on the unhackable list.\n"
                    "2. AUGMENTATION CONSISTENCY: capabilities that appear without being installed, chrome "
                    "that never needs power or maintenance, injuries that heal faster than the system allows.\n"
                    "3. MONEY: track my protagonist's balance against the monthly costs. Where do they afford "
                    "something they cannot afford?\n"
                    "4. HEAT LOGIC: does the corporation escalate according to its own published policy, or "
                    "does it become conveniently passive when my plot needs breathing room?\n"
                    "5. TIME AND GEOGRAPHY: travel times across districts, recovery times after a run, "
                    "elapsed days against deadlines.\n"
                    "6. KNOWLEDGE STATE: who knows what, when. Flag any character acting on information they "
                    "should not have, especially around the double-cross reveals.\n"
                    "7. THE FREE LUNCH LIST: every gain that currently has no price attached.\n\n"
                    "Rank all findings as CRITICAL, MODERATE or MINOR, and propose a fix for every CRITICAL "
                    "item.\n\n"
                    "End by asking me which critical fix would require a structural change, so I can plan that "
                    "repair before touching the prose."
                ),
                "pro_tip": (
                    "Audit in ten-chapter chunks with the rules pasted in each time. Fed a whole manuscript, "
                    "any AI skims; fed ten chapters against explicit constraints, it will catch the run you "
                    "let your netrunner make in chapter 30 that chapter 7 said was impossible."
                ),
            },
            {
                "title": "The Neon-Noir Voice Pass",
                "desc": (
                    "This genre has the strongest default style of any in science fiction, and defaults are "
                    "what make a book forgettable. This prompt strips the borrowed voice out and sharpens what "
                    "is yours."
                ),
                "prompt_text": (
                    "You are a line editor working on noir-influenced science fiction.\n\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET]\n"
                    "My city signature and anti-cliché replacements: [PASTE FROM PROMPT 8]\n"
                    "Chapter to edit: [PASTE ONE CHAPTER]\n\n"
                    "Do a line-level pass:\n\n"
                    "1. THE CLICHE SWEEP: flag every borrowed cyberpunk image - rain on neon, mirrored "
                    "shades, jacked-in trance states, chrome reflections, ramen in the rain, skyline "
                    "establishing shots. Replace each with something drawn from my own city signature.\n"
                    "2. ABSTRACTION HUNT: find general nouns (the corporation, the tech, the street, security) "
                    "where a specific name, model or brand from my world would land harder.\n"
                    "3. RHYTHM MAP: mark passages where sentence length does not match tension, and rewrite "
                    "one paragraph to demonstrate.\n"
                    "4. EXPLANATION AUDIT: find every place I explain a piece of technology or slang, and show "
                    "me how to let context carry it instead.\n"
                    "5. CLASS REGISTER: check that corporate dialogue runs on euphemism and street dialogue "
                    "on compression. Flag any character who speaks in the wrong register.\n"
                    "6. BODY AWARENESS: mark places where I could ground a scene in a physical sensation from "
                    "my protagonist's loadout - heat, lag, a maintenance alert, a numb finger.\n"
                    "7. THE ONE BEAUTIFUL THING: find or add a single image of real beauty in this chapter.\n\n"
                    "Return edits as a list - original line, proposed line, one-line reason. Do not rewrite "
                    "the chapter.\n\n"
                    "End by asking me which of your changes I rejected, so you can calibrate to my voice for "
                    "the next chapter."
                ),
                "pro_tip": (
                    "Keep a private list of the cliché images you refuse to use. It becomes a style guide by "
                    "subtraction, and by chapter twenty you will be writing sentences no other cyberpunk novel "
                    "could contain."
                ),
            },
            {
                "title": "Blurb, Metadata and Series Architecture",
                "desc": (
                    "The combined publishing kit - retail copy, categories, keywords, cover brief - plus the "
                    "architecture for the books that follow without cheapening this one's ending."
                ),
                "prompt_text": (
                    "You are a book marketing copywriter and series architect for adult science fiction.\n\n"
                    "My reader promise and pitches: [PASTE FROM PROMPT 3]\n"
                    "My thesis, protagonist and contract: [PASTE FROM PROMPTS 1, 9 AND 13]\n"
                    "My endgame and what changed: [PASTE FROM PROMPT 16]\n"
                    "My surviving cast: [LIST]\n\n"
                    "PART A - THE RETAIL KIT:\n"
                    "1. THE BLURB: 150-200 words in three movements - the city and the protagonist's "
                    "situation, the contract and what it costs, the stakes and hook. Nothing past the "
                    "midpoint.\n"
                    "2. TWO ALTERNATIVES: a punchy 100-word version, and one that leads with the crew.\n"
                    "3. THE HOOK LINE: three options for the line above the blurb.\n"
                    "4. CATEGORIES: 6 retail categories ranked by how well I compete in each.\n"
                    "5. KEYWORDS: 20 reader-search phrases grouped into trope, mood and situation terms.\n"
                    "6. COMP POSITIONING: 4 comparable reading experiences described as types of book, each "
                    "with a 'for readers who loved X but wanted Y' line.\n"
                    "7. THE COVER BRIEF: 5 visual directions tied to specific images from my book rather than "
                    "genre wallpaper, and 3 cover clichés to forbid.\n\n"
                    "PART B - THE SERIES:\n"
                    "8. THE SHAPE: recommend a series shape - a crew series with a new job per book, an "
                    "escalating campaign against one corporation, or a mosaic across the same city - and "
                    "justify it against my ending.\n"
                    "9. BOOK TWO: a one-page premise. The new pressure, the returning cost from book one, and "
                    "a hook in the first three chapters. It must not undo book one's small permanent change.\n"
                    "10. THE SEEDS: 6 things planted or plantable in book one that pay off later - a contact, "
                    "a district, an unpaid favour, a piece of hardware, an unanswered question, a survivor.\n"
                    "11. THE STANDALONE GUARANTEE: confirm book one satisfies alone, and name anything in my "
                    "ending that reads as an unpaid promise rather than an open door.\n\n"
                    "End by asking me which promise in the blurb I am least confident the book delivers, so we "
                    "can fix the blurb or fix the book."
                ),
                "pro_tip": (
                    "Sell the crew, not the setting. Every cyberpunk blurb on the shelf promises a neon city; "
                    "the ones that convert promise specific people with a specific problem and a deadline."
                ),
            },
        ],
    },
]
