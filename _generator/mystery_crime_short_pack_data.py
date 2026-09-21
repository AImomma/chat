# -*- coding: utf-8 -*-
"""
Royalti Studios - Mystery & Crime Short Master Prompt Pack (Adult Fiction Line).

Companion to the Short Story pack, not a subset. That pack covers short fiction
craft generally; this one adds the machinery a mystery needs and no other genre
does - a fair-play clue ladder, honest misdirection, two timelines, and a
solvability test.

The short-form problem this pack exists to solve: a novel conceals a clue by
distance (two hundred pages back). A short story has four thousand words and no
distance available, so concealment has to be technique.

Build with:
    python pack_builder.py mystery_crime_short_pack_data \
        "Mystery_Crime_Short_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.

PROMPT COUNT: 22 - the adult baseline. The clue system takes a full phase that
no other pack needs, which is exactly what brings it from the Short Story pack's
20 up to baseline.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "MYSTERY & CRIME SHORT",
    "total_prompts": 22,
    "hook_line": "Every clue on the page, the answer in plain sight, and a reader who never saw it coming and cannot claim they were cheated.",
    "keyword_lines": [
        "Fair play • The clue ladder • Honest misdirection • Two timelines • The reveal",
        "Whodunit • Howdunit • Whydunit • Inverted • Noir • Heist • Cozy • Procedural",
    ],
    "subgenres_line": "Sub-genres: Whodunit, Howdunit, Whydunit, Inverted (we know who from page one), Cozy Short, Noir & Hardboiled, Heist, Police Procedural Short, Crime Without a Detective, Domestic Suspense",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-21",
    "audience_line": "Adult Fiction Line",
    "cover_h2": "From the Solution Backwards to a Submittable Story",
    "closing_tagline": "Write the answer first. Then hide it in plain sight, fairly, in four thousand words.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "Mystery is the one genre where a short story is harder than a novel, and the reason is "
        "concealment. A novel hides a clue by distance - the reader met it two hundred pages ago and has "
        "forgotten. A short story has four thousand words and no distance to spend, so every clue has to "
        "be hidden by technique instead: buried inside a list, disguised as characterisation, delivered by "
        "someone the reader is not listening to, or stated so plainly it reads as scenery.\n\n"
        "That is what this pack is built around. You write the solution first, in Prompt 3, and everything "
        "after is the craft of hiding it fairly. Phase 3 is the clue system - four prompts no other pack "
        "in the library needs - and Phase 6 audits the result against the fair-play standard your "
        "sub-genre actually owes its readers. Prompt 1 locks that sub-genre, because a whodunit and an "
        "inverted crime story are almost opposite machines. Work in order, keep every output in one "
        "document, and by Prompt 22 you have a story that survives the only test that matters here: a "
        "reader going back to check."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-4) - Lock the case. Sub-genre and length, the true sequence of what actually "
        "happened, the solution written before anything else, and the fair-play contract you are signing.",
        "Phase 2 (Prompts 5-8) - Build the case. The victim, the culprit, a suspect set sized to your word "
        "count, and the detective or viewpoint figure whose method the reader has to be able to follow.",
        "Phase 3 (Prompts 9-12) - The clue system. The clue ladder with every clue placed and concealed, "
        "honest misdirection and red herrings, the two timelines, and the concealment techniques that "
        "replace distance at short length. This phase is the pack.",
        "Phase 4 (Prompts 13-15) - Structure it. The shapes mystery shorts actually use, the investigation "
        "beat map against word count, and the reveal - which should be far shorter than instinct suggests.",
        "Phase 5 (Prompts 16-18) - Write it. The opening, which in this genre has a specific job; the "
        "draft; and a compression pass that knows you cannot cut a clue.",
        "Phase 6 (Prompts 19-22) - Audit and send. The fair-play audit, the craft audit, the solvability "
        "test, and markets plus the question of whether this detective recurs.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool and a place to save your outputs between prompts. Brackets like "
        "[THIS] are placeholders - replace them with your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular, and Prompt 1 tells you which prompts your "
        "sub-genre needs. Writing inverted crime, where the reader knows the culprit from page one? Prompt "
        "10 becomes a light pass and Prompt 14 carries the tension instead. Writing noir or crime without "
        "a detective? Prompts 9 and 19 become lighter, and Prompt 8 becomes a character prompt rather than "
        "a method prompt. Writing a howdunit or whydunit? Prompt 7 shrinks - you may need only one suspect."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "The solution written first, so every line afterwards is built to conceal it fairly",
            "Every clue the detective uses present on the page, in the reader's view, before the reveal",
            "Concealment by technique rather than distance - buried in a list, disguised as character, said by someone being ignored",
            "Red herrings made of true information pointed the wrong way, never of lies",
            "A suspect count sized to the word count: three or four in a short, one or two in flash",
            "A detective whose method is visible, so the reader can follow the reasoning rather than admire it",
            "A reveal that is short - a page at most, because explanation is not drama",
            "Two timelines held separately: what actually happened, and the order the reader learns it",
            "A culprit who is the least likely and, on rereading, the only possible one",
            "An ending where the reader goes back to check - and finds it was all there",
        ],
        "kills": [
            "A clue the reader never saw, which is the one unforgivable failure in this genre",
            "The culprit introduced late, or a character who appears only to be guilty",
            "A confession that arrives instead of a deduction, with no evidence forcing it",
            "Withheld interiority - a viewpoint character who knows the answer and does not think about it",
            "Six suspects in four thousand words, none of whom the reader can tell apart",
            "A detective who solves it by a leap the reader cannot reconstruct afterwards",
            "Three pages of explanation at the end, which is a lecture rather than a climax",
            "Red herrings that are simply false statements, which make the story a trick",
            "Coincidence doing the work of investigation - an overheard conversation, a lucky document",
            "A twist that changes who did it without changing what anything earlier meant",
        ],
        "voice": [
            "Concrete detail always - in this genre a specific object is both texture and evidence",
            "Hold one point of view and its knowledge state absolutely; a single slip destroys the contract",
            "Let the prose linger equally on clues and non-clues, so emphasis never gives the game away",
            "Dialogue carries suspicion - people evade, over-explain, and answer questions nobody asked",
            "Keep the detective's reasoning on the page in fragments as it forms, not all at the end",
            "Understate the reveal; the flat delivery of a devastating fact outperforms any flourish",
            "Description does double duty - what a room contains is characterisation and also the case",
            "Vary the rhythm around clues deliberately, so a planted detail never sits in a conspicuous spot",
        ],
        "formula": (
            "THE SOLUTION (written first, never shown) -> The Crime, Discovered -> The Detective Engaged -> "
            "The Suspect Field Established -> First Pass of Clues, Planted Flat -> The Obvious Theory, "
            "Which Is Wrong -> Misdirection Peaks -> The Contradiction (something cannot be true) -> "
            "The Reframe (the detail that was always there) -> THE DEDUCTION, Shown -> The Confrontation -> "
            "The Consequence, Which Is Not Always Justice"
        ),
        "reader_expectations": (
            "Mystery readers are the most adversarial audience in fiction, and they are reading to beat "
            "you. They expect a contract: everything the detective knows, they know, at the same time, and "
            "the solution follows from evidence rather than from confession or coincidence. They will "
            "happily be fooled and will not tolerate being cheated, and they can tell the difference "
            "instantly. In short form they additionally expect efficiency - a suspect field they can hold "
            "in their head, a detective whose method is legible, and a reveal that does not stop the story "
            "for three pages of explanation. Editors of crime markets read for the reread: the test is "
            "whether a reader who goes back to check finds the clue sitting there in plain sight. If it is "
            "not, nothing else about the story will save it."
        ),
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "Everything in this genre comes down to one moment you will never see: a reader reaching the last "
        "line, going back to page two, and finding it there. That moment is worth more than any twist, and "
        "it is the only thing you are actually building. You wrote the solution in Prompt 3 precisely so "
        "that every sentence since has had a job - to place something true where a reader would look past "
        "it. When a draft is not working, check the three usual faults: a clue that is not on the page, a "
        "red herring that is a lie rather than a truth pointed wrong, or a reveal that explains instead of "
        "lands. Fix any one and the story stands. Then run Prompt 19 honestly, even when you would rather "
        "not - it is the only audit in this pack that a reader will run for you if you do not."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: LOCK THE CASE",
        "intro": (
            "Four prompts, and the order matters more here than in any other genre. You lock the "
            "sub-genre, write down what actually happened, then write the solution - all before a word of "
            "story. Everything after Prompt 3 is the craft of concealment."
        ),
        "prompts": [
            {
                "title": "The Sub-Genre and Length Lock",
                "desc": (
                    "A whodunit and an inverted crime story are almost opposite machines. This prompt picks "
                    "yours, sizes it to a word count, and states what that combination obligates."
                ),
                "prompt_text": (
                    "You are a crime fiction editor who has read for mystery magazines and anthologies and "
                    "knows what each sub-genre owes its readers.\n\n"
                    "My idea is: [DESCRIBE IN 2-5 SENTENCES - a crime, a situation, an image, whatever I "
                    "have]\n"
                    "My sub-genre, if I know it: [NAME IT, OR SAY 'YOU TELL ME']\n\n"
                    "Do the following:\n\n"
                    "1. THE SUB-GENRE LOCK: name mine precisely from - whodunit, howdunit, whydunit, "
                    "inverted (reader knows the culprit from the start), cozy short, noir or hardboiled, "
                    "heist, police procedural short, crime without a detective, domestic suspense. Justify "
                    "it and say what my idea would become in the nearest alternative.\n"
                    "2. THE SHORT-FORM FIT: rank my sub-genre for short length. Be honest - a whodunit "
                    "needs suspects and suspects need words, so howdunit, whydunit and inverted often work "
                    "better at four thousand words. If my chosen form is the hard one, say so and tell me "
                    "what it will cost.\n"
                    "3. THE CONTRACT: state the 5 things a reader of my specific sub-genre expects and the "
                    "3 things that get a story in it rejected. This list is what Prompt 19 audits against.\n"
                    "4. THE FAIR-PLAY LEVEL: not every sub-genre owes strict fair play. State plainly how "
                    "much mine owes - a classical whodunit owes everything, noir owes far less, domestic "
                    "suspense trades in dread rather than deduction. Define the standard I am held to.\n"
                    "5. THE LENGTH LOCK: recommend a target word count and say how many suspects, scenes, "
                    "locations and clues that count can hold. Write these as hard limits.\n"
                    "6. THE SUSPECT MATH: for my length, the maximum number of viable suspects a reader "
                    "can hold and tell apart. Then tell me how many I was probably planning, and to cut to "
                    "the number.\n"
                    "7. THE STRUCTURAL CONSEQUENCE: explain how my sub-genre changes the shape - an "
                    "inverted story front-loads the crime and runs on tension rather than puzzle; a "
                    "howdunit needs the method concealed rather than the person; a whydunit hides motive in "
                    "character.\n"
                    "8. THE ROUTING NOTE: which prompts in this pack matter most for my sub-genre and "
                    "which are a light pass.\n\n"
                    "End by asking me whether I want the reader to solve this or to be fooled by it, "
                    "because those are two different stories and both are legitimate."
                ),
                "pro_tip": (
                    "Take item 2 seriously. The inverted form - the reader knows who did it from the first "
                    "page and the tension is whether they get caught - is enormously effective at short "
                    "length and badly under-used, because it needs no suspect field at all."
                ),
            },
            {
                "title": "The Crime: What Actually Happened",
                "desc": (
                    "Before any story, the truth. This prompt writes the real sequence of events in full, "
                    "as a police report would have it - the document you will spend the rest of the pack "
                    "concealing."
                ),
                "prompt_text": (
                    "You are a crime writer's case consultant. You write the true version of events, in "
                    "full, before any story exists.\n\n"
                    "My sub-genre, length and limits: [PASTE FROM PROMPT 1]\n"
                    "My idea: [PASTE OR DESCRIBE]\n\n"
                    "Write THE TRUE SEQUENCE. This document is never published - it is what I conceal.\n\n"
                    "1. THE CRIME: what was actually done, by whom, to whom. Stated plainly in one "
                    "paragraph.\n"
                    "2. THE TIMELINE: every event in real chronological order, with times where they "
                    "matter - before, during and after. Include what the culprit did in the hours either "
                    "side, because those are where clues come from.\n"
                    "3. THE METHOD: exactly how it was done, in practical detail. If the method is my "
                    "puzzle (howdunit), this is the thing I am hiding, so make it genuinely ingenious "
                    "rather than merely unusual.\n"
                    "4. THE MOTIVE: why. In one paragraph, and it must be a reason a reader will accept as "
                    "sufficient for this crime. Weak motive is the most common failure in short crime.\n"
                    "5. THE MISTAKE: the thing the culprit got wrong. Every solvable crime has one - name "
                    "it, because it is the spine of the solution.\n"
                    "6. THE EVIDENCE THAT EXISTS: everything physically or testimonially left behind, "
                    "listed. Mark which pieces are discoverable by my detective and which are not.\n"
                    "7. WHO SAW WHAT: for every character, what they actually witnessed or know, and "
                    "whether they realise its significance. Most useful clues come from people who do not "
                    "know what they saw.\n"
                    "8. THE LIES: who will lie, about what, and for what innocent reason. Innocent people "
                    "lying about unrelated things is the engine of a good suspect field.\n"
                    "9. THE PLAUSIBILITY CHECK: tell me honestly whether this crime would work in reality, "
                    "and flag anything that relies on improbable luck or improbable competence.\n\n"
                    "End by asking me whether the culprit would be caught in real life, because if the "
                    "answer is obviously yes or obviously no, the case needs adjusting."
                ),
                "pro_tip": (
                    "Item 7 is where the best clues live. A neighbour who mentions the wrong car in "
                    "passing, with no idea it matters, gives you a fair clue that is almost impossible to "
                    "spot - and it costs one sentence."
                ),
            },
            {
                "title": "The Solution First",
                "desc": (
                    "Write the reveal before the story. This is the mystery equivalent of designing the "
                    "last image first, and skipping it is why most drafts collapse in the final third."
                ),
                "prompt_text": (
                    "You are a mystery editor who believes a story cannot be written until its solution "
                    "exists on paper.\n\n"
                    "My true sequence: [PASTE FROM PROMPT 2]\n"
                    "My sub-genre and fair-play level: [PASTE FROM PROMPT 1]\n\n"
                    "Do the following:\n\n"
                    "1. THE SOLUTION, AS THE DETECTIVE STATES IT: write the actual reveal - what my "
                    "detective says or realises, in the words they would use. Keep it under 250 words, "
                    "because that is roughly how long a reveal should be.\n"
                    "2. THE CHAIN OF REASONING: break the solution into the 4-6 logical steps that lead "
                    "from evidence to conclusion. Each step must rest on something the reader can be given. "
                    "Number them - this chain becomes my clue list in Prompt 9.\n"
                    "3. THE LOAD-BEARING CLUE: the single piece of evidence the whole solution depends on. "
                    "Name it. This is the one I will conceal most carefully and the one Prompt 19 will "
                    "check hardest.\n"
                    "4. THE INEVITABILITY TEST: state why the culprit is the ONLY person this could have "
                    "been. If more than one person could have done it with the evidence given, the "
                    "solution is not yet tight - fix it.\n"
                    "5. THE ALTERNATIVE SOLUTIONS: list 3 other explanations a clever reader might "
                    "construct from my evidence, and for each, the specific detail that rules it out. Those "
                    "details must appear in the story.\n"
                    "6. THE 'OF COURSE' MOMENT: the detail that, on rereading, makes the answer obvious. "
                    "Describe it and where it will sit.\n"
                    "7. THE REVEAL MECHANISM: how the solution reaches the reader - a deduction spoken "
                    "aloud, a realisation in viewpoint, a confrontation, a document, an action taken "
                    "without explanation. Recommend one for my sub-genre, and note that the last is often "
                    "the most elegant.\n"
                    "8. THE COST: what the solution costs someone. A solved case that costs nobody "
                    "anything is a puzzle rather than a story.\n\n"
                    "End by asking me whether justice happens, because in short crime the answer is "
                    "frequently no and that is often the better ending."
                ),
                "pro_tip": (
                    "Keep item 1 under 250 words and hold yourself to it. A reveal that runs to three pages "
                    "has become a lecture, and the reader's pleasure is in the click of understanding, not "
                    "in the length of the explanation."
                ),
            },
            {
                "title": "Reader Promise and the Fair-Play Contract",
                "desc": (
                    "What you are promising, written down explicitly, so the audit in Phase 6 has "
                    "something to measure against."
                ),
                "prompt_text": (
                    "You are a crime fiction editor setting the contract between a story and its reader.\n\n"
                    "My sub-genre, contract and fair-play level: [PASTE FROM PROMPT 1]\n"
                    "My solution and chain of reasoning: [PASTE FROM PROMPT 3]\n\n"
                    "Do the following:\n\n"
                    "1. THE READER PROMISE: one paragraph in the second person ('You will...').\n"
                    "2. THE FAIR-PLAY CONTRACT: write out, as numbered rules, exactly what I am promising "
                    "this reader. Cover: every clue the detective uses appears in the reader's view before "
                    "the reveal; the culprit is present and characterised before the final scene; no "
                    "supernatural solution unless established; no undisclosed twin, secret passage or "
                    "unmentioned poison; the viewpoint character does not conceal their own knowledge; "
                    "coincidence does not solve the case. Then adjust each rule to my sub-genre's actual "
                    "standard from Prompt 1 item 4, since noir and suspense owe less than a classical "
                    "whodunit.\n"
                    "3. THE RULES I AM BREAKING: any of the above I intend to break. For each, say whether "
                    "my sub-genre permits it and what it will cost me with readers if it does not.\n"
                    "4. THE VIEWPOINT PROBLEM: state how my chosen viewpoint interacts with fair play. A "
                    "first-person detective must not hide their own thoughts; a third-limited narrator must "
                    "not skip a realisation; an unreliable narrator changes the contract entirely. Name my "
                    "specific risk.\n"
                    "5. THE THREE APPEALS I am leading with, from - puzzle pleasure, dread, character "
                    "study, procedural texture, moral question, revenge, atmosphere, voice.\n"
                    "6. THE DESTINATION: where this story is aimed - a crime or mystery magazine, a "
                    "general literary market, an anthology call, a contest, a collection - and what each "
                    "requires. Explain the principles rather than naming markets, since guidelines change.\n"
                    "7. THE TONE LOCK: where this sits from cozy to bleak, and what that permits on the "
                    "page - violence, the body, the victim's suffering, the fate of the culprit.\n"
                    "8. THE FOUR PROMISES I must not break, with the review or rejection each breach "
                    "generates.\n\n"
                    "End by asking me whether I would feel cheated by my own solution if I read it cold, "
                    "which is the only honest version of this question."
                ),
                "pro_tip": (
                    "Write item 2 out properly rather than assuming you know it. A contract on paper is "
                    "what makes the Phase 6 audit possible - and half the failures in this genre are "
                    "writers breaking a rule they never consciously agreed to."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: BUILD THE CASE",
        "intro": (
            "Four prompts for the people. In short crime everyone must be doing double duty - a victim who "
            "generates motive, suspects who are distinguishable in a line, and a detective whose method "
            "the reader can actually follow."
        ),
        "prompts": [
            {
                "title": "The Victim",
                "desc": (
                    "In short crime the victim is a plot engine as much as a person. This prompt builds "
                    "one who generates motive, suspects and clues at once."
                ),
                "prompt_text": (
                    "You are a crime fiction editor who knows that a thin victim produces a thin case.\n\n"
                    "My true sequence and motive: [PASTE FROM PROMPT 2]\n"
                    "My sub-genre and length limits: [PASTE FROM PROMPT 1]\n\n"
                    "Do the following:\n\n"
                    "1. THE VICTIM: name, age, what they did, and the one behaviour that tells a reader who "
                    "they were. If my story has no death, treat the wronged party or the target the same "
                    "way.\n"
                    "2. THE MOTIVE GENERATOR: what about this person gave more than one character a reason "
                    "to want them gone, harmed or robbed. List the reasons - this list becomes my suspect "
                    "field.\n"
                    "3. THE SYMPATHY DIAL: how much the reader should care. State it deliberately - a "
                    "wholly unsympathetic victim removes urgency, a wholly sympathetic one narrows the "
                    "motive field. Recommend a position and say why for my sub-genre.\n"
                    "4. THE SECRET: what this person was hiding. In short crime the victim's secret is the "
                    "most efficient source of both clue and red herring - name it and say who knew.\n"
                    "5. THE BODY OR THE SCENE: what the discovery actually looks like, in concrete detail. "
                    "Mark which details are clues, which are red herrings, and which are neither - and note "
                    "that the third category must exist or the scene reads as a puzzle board.\n"
                    "6. THE DISCOVERY: who finds it, how, and what that person does in the first ten "
                    "minutes. Their behaviour is characterisation and often evidence.\n"
                    "7. THE ABSENCE: what the victim's removal changes for each other character - "
                    "practically, financially, emotionally. This is where motive becomes visible.\n"
                    "8. THE LAST DAY: what the victim did in their final hours, as the reader will "
                    "eventually learn it. Mark which parts are known early and which emerge.\n"
                    "9. THE TONE CHECK: how the body or the crime is described, against my tone lock. "
                    "Cozy and bleak describe the same event completely differently.\n\n"
                    "End by asking me whether the victim deserved it, because the reader will ask and the "
                    "story should have a position."
                ),
                "pro_tip": (
                    "Item 5's third category is what most drafts miss. A crime scene where every single "
                    "detail is either a clue or a herring reads as a puzzle board - you need neutral "
                    "detail for the significant ones to hide inside."
                ),
            },
            {
                "title": "The Culprit",
                "desc": (
                    "The least likely and, on rereading, the only possible one. This prompt builds someone "
                    "who can be present throughout without being suspected."
                ),
                "prompt_text": (
                    "You are a mystery editor who specialises in culprits readers do not see and cannot "
                    "dispute afterwards.\n\n"
                    "My true sequence, method, motive and mistake: [PASTE FROM PROMPT 2]\n"
                    "My solution and inevitability test: [PASTE FROM PROMPT 3]\n"
                    "My fair-play contract: [FROM PROMPT 4]\n\n"
                    "Do the following:\n\n"
                    "1. THE CULPRIT: name, relationship to the victim, and the one behaviour that "
                    "characterises them. They must appear early and be memorable for something other than "
                    "suspicion.\n"
                    "2. THE HIDING PLACE: the role this person occupies in the story that keeps them off "
                    "the reader's list. Name the mechanism - they are the one reporting the facts, the one "
                    "helping, the one with the obvious alibi, the one the reader likes, the one who seems "
                    "too minor to matter, or the one already cleared.\n"
                    "3. THE EARLY APPEARANCE: their first scene, and what they do in it that is both "
                    "characterising and, in hindsight, damning.\n"
                    "4. WHY THEY ARE NOT SUSPECTED: the specific reason the detective and reader pass over "
                    "them. It must be an honest reason, not an absence of attention.\n"
                    "5. THE ALIBI OR THE COVER: what protects them, and the precise flaw in it. The flaw is "
                    "a clue - decide now where it shows.\n"
                    "6. THEIR BEHAVIOUR THROUGHOUT: how a guilty person actually behaves in each scene "
                    "they appear in. Give me 6 specific actions or lines that read as innocent first time "
                    "and unbearable second time.\n"
                    "7. THE MISTAKE ON THE PAGE: the error from Prompt 2 item 5, and the exact moment it "
                    "becomes visible to a reader who is paying attention.\n"
                    "8. THE HUMANITY: what makes this person more than a solution. At short length one "
                    "well-chosen detail does it.\n"
                    "9. THE CONFRONTATION: how they respond when it lands - denial, collapse, relief, "
                    "explanation, silence. Recommend one for my tone, and note that relief is the most "
                    "under-used and often the truest.\n\n"
                    "End by asking me whether the reader will feel sorry for them, because in short crime "
                    "that is usually what makes the ending land."
                ),
                "pro_tip": (
                    "Item 2's most reliable mechanism is the helpful one. A character actively assisting "
                    "the investigation is nearly invisible to readers, is present for every scene "
                    "naturally, and gives you constant opportunities to plant clues in their own dialogue."
                ),
            },
            {
                "title": "The Suspect Field",
                "desc": (
                    "Three or four people a reader can tell apart in four thousand words, each with a real "
                    "reason and a real secret."
                ),
                "prompt_text": (
                    "You are a mystery editor building a suspect field sized to a short story.\n\n"
                    "My suspect math - the maximum my length allows: [PASTE FROM PROMPT 1 ITEM 6]\n"
                    "My victim's motive generator: [PASTE FROM PROMPT 6 ITEM 2]\n"
                    "My culprit and their hiding place: [PASTE FROM PROMPT 6]\n"
                    "My true sequence's lies: [FROM PROMPT 2 ITEM 8]\n\n"
                    "Build my SUSPECT FIELD, staying inside my maximum. For each suspect:\n\n"
                    "1. Name, relationship to the victim, and the ONE distinguishing feature that lets a "
                    "reader tell them apart instantly - a job, a manner, an object, a verbal habit. At this "
                    "length a suspect the reader confuses with another is a suspect wasted.\n"
                    "2. THE MOTIVE: their real reason to want the victim harmed, drawn from the motive "
                    "generator.\n"
                    "3. THE SECRET: what they are actually hiding, which is NOT the crime. Innocent people "
                    "with guilty secrets are the engine of a suspect field - an affair, a theft, a "
                    "humiliation, a small fraud, a kindness they are ashamed of.\n"
                    "4. THE LIE: what they lie about and the innocent reason for it.\n"
                    "5. THE CLEARING: the specific fact that eventually rules them out, and where it "
                    "appears.\n"
                    "6. THE SUSPICION PEAK: which part of the story this suspect looks guiltiest in, so "
                    "suspicion rotates rather than sitting on one person.\n\n"
                    "Then give me:\n"
                    "7. THE ROTATION MAP: the order in which suspicion moves across the field, mapped to "
                    "approximate word positions. A short mystery needs the reader's theory to change at "
                    "least twice.\n"
                    "8. THE DISTINGUISHABILITY AUDIT: check every suspect against every other. Any two who "
                    "could be confused - by role, name, age, manner or function - get changed. Name the "
                    "collisions.\n"
                    "9. THE CUT RECOMMENDATION: if I have more suspects than my length allows, which to "
                    "merge or remove, and what their function transfers to.\n"
                    "10. THE NAME CHECK: any two suspect names too similar to hold apart at speed. Rename "
                    "one.\n\n"
                    "End by asking me which suspect the reader will most want to be innocent, because that "
                    "is the one to threaten."
                ),
                "pro_tip": (
                    "Item 3 does most of the work in this genre. Every suspect should be guilty of "
                    "something and innocent of this - it gives them a reason to behave suspiciously, a "
                    "reason to lie, and a payoff when their real secret finally surfaces."
                ),
            },
            {
                "title": "The Detective or Viewpoint Figure",
                "desc": (
                    "Whoever carries the reader through. Their method has to be visible, because a reader "
                    "who cannot reconstruct the reasoning feels cheated even when they were not."
                ),
                "prompt_text": (
                    "You are a crime fiction editor developing an investigating character for short "
                    "fiction.\n\n"
                    "My sub-genre and fair-play level: [PASTE FROM PROMPT 1]\n"
                    "My solution's chain of reasoning: [PASTE FROM PROMPT 3 ITEM 2]\n"
                    "My viewpoint problem: [PASTE FROM PROMPT 4 ITEM 4]\n"
                    "My rough detective idea: [DESCRIBE, or say 'you choose']\n\n"
                    "Do the following:\n\n"
                    "1. THE FIGURE: name, age, and their standing - professional investigator, amateur, "
                    "someone with a personal stake, a bystander, or the culprit themselves if I am writing "
                    "inverted. Recommend a type for my sub-genre and length.\n"
                    "2. THE ACCESS PROBLEM: why this person gets to investigate at all, and what they "
                    "cannot do. An amateur cannot compel answers; a professional cannot trespass. This "
                    "constraint is a gift - name mine.\n"
                    "3. THE METHOD: how they actually think. Observation of physical detail, reading "
                    "people, procedure, persistence, specialist knowledge, or a mind that will not let an "
                    "inconsistency go. Pick one and make it consistent, because the reader must be able to "
                    "follow it.\n"
                    "4. THE METHOD ON THE PAGE: 5 specific moments where their method is visible in small "
                    "things, before it matters - so the final deduction reads as characteristic rather "
                    "than convenient.\n"
                    "5. THE PERSONAL STAKE: what this case costs them. At short length a detective with "
                    "nothing at risk is a device.\n"
                    "6. THE BLIND SPOT: the thing about themselves or people that makes them miss the "
                    "answer for most of the story. This must be the same thing that eventually lets them "
                    "see it.\n"
                    "7. THE KNOWLEDGE STATE: exactly what they know and when, tracked against my clue "
                    "ladder. Confirm the reader is never behind them by more than a moment, per my "
                    "contract.\n"
                    "8. THE INTERIORITY RULE: if this is first person or close third, state precisely how "
                    "to handle the moment they realise the truth without either revealing it or cheating. "
                    "This is the single hardest craft problem in the genre - give me the technique and one "
                    "sample sentence.\n"
                    "9. THE VOICE: 3 lines of their narration or dialogue, so I know the register.\n\n"
                    "End by asking me whether this detective could carry more than one story, because that "
                    "answer matters for Prompt 22."
                ),
                "pro_tip": (
                    "Item 8 is where honest writers accidentally cheat. The fair technique is to let the "
                    "viewpoint register the realisation as a reaction rather than a content - the held "
                    "breath, the sudden need to check something - without narrating what was understood."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: THE CLUE SYSTEM",
        "intro": (
            "Four prompts no other pack in this library needs, and the reason this one exists. A novel "
            "hides a clue by distance; you have four thousand words and none to spend. Everything here is "
            "about concealing true information in plain sight, fairly."
        ),
        "prompts": [
            {
                "title": "The Clue Ladder",
                "desc": (
                    "Every clue the solution needs, placed on the page, in order, with its concealment "
                    "method assigned. This is the central document of the pack."
                ),
                "prompt_text": (
                    "You are a mystery editor who builds clue ladders - the map of what the reader is "
                    "given, where, and how it is hidden.\n\n"
                    "My chain of reasoning, numbered: [PASTE FROM PROMPT 3 ITEM 2]\n"
                    "My load-bearing clue: [PASTE FROM PROMPT 3 ITEM 3]\n"
                    "My alternative solutions and their ruling-out details: [PASTE FROM PROMPT 3 ITEM 5]\n"
                    "My target word count: [FROM PROMPT 1]\n"
                    "My culprit's mistake and alibi flaw: [FROM PROMPT 6]\n\n"
                    "Build my CLUE LADDER. For every clue the solution requires:\n\n"
                    "1. Clue number, and which step of the chain of reasoning it supports.\n"
                    "2. WHAT IT IS: the specific fact, object, statement, absence or inconsistency.\n"
                    "3. WHO DELIVERS IT: the detective's own observation, a suspect's statement, a "
                    "document, a bystander who does not know what they saw, or the culprit themselves. "
                    "Vary these - a story where the detective notices everything is inert.\n"
                    "4. WHERE IT LANDS: an approximate word position, and which scene.\n"
                    "5. THE CONCEALMENT METHOD: how it hides. Choose from - buried in a list of similar "
                    "items; disguised as characterisation; stated so plainly it reads as scenery; "
                    "delivered by someone the reader has reason to discount; overshadowed by a more "
                    "dramatic event in the same paragraph; given before the reader knows what matters; an "
                    "absence rather than a presence; or split across two places so neither half signifies "
                    "alone. Name the one used and why it suits this clue.\n"
                    "6. THE FALSE SIGNIFICANCE: what the reader will think it means instead.\n\n"
                    "Then give me:\n"
                    "7. THE COMPLETENESS CHECK: confirm every step of my chain of reasoning has at least "
                    "one clue supporting it. Any step without one is a leap - name it.\n"
                    "8. THE DISTRIBUTION MAP: where the clues fall across the word count. Flag any cluster "
                    "- three clues in one scene is a signpost - and any long stretch with none.\n"
                    "9. THE LOAD-BEARING PLACEMENT: where my most important clue sits, and the argument "
                    "for putting it EARLY. Early clues are better hidden, because the reader does not yet "
                    "know what matters.\n"
                    "10. THE RULING-OUT CLUES: confirm each alternative solution's disqualifying detail is "
                    "on the ladder. A solution that is merely the most likely is not a solution.\n"
                    "11. THE NEUTRAL DETAIL BUDGET: how much non-significant specific detail the story "
                    "needs so clues have somewhere to hide. Give me a ratio.\n\n"
                    "End by asking me which clue I am most worried is too obvious, because that is usually "
                    "the one that is fine and the one I am confident about is usually the problem."
                ),
                "pro_tip": (
                    "Item 9 is counter-intuitive and reliable. Put your most important clue in the first "
                    "quarter, stated flatly, before the reader has any framework for it - they will read "
                    "straight past it and find it instantly on the reread."
                ),
            },
            {
                "title": "Red Herrings and Honest Misdirection",
                "desc": (
                    "Misdirection built from true information pointed the wrong way. Red herrings made of "
                    "lies turn a mystery into a trick, and readers can tell."
                ),
                "prompt_text": (
                    "You are a mystery editor who distinguishes misdirection from cheating.\n\n"
                    "My clue ladder: [PASTE FROM PROMPT 9]\n"
                    "My suspect field with secrets and lies: [PASTE FROM PROMPT 7]\n"
                    "My fair-play contract: [FROM PROMPT 4]\n\n"
                    "Do the following:\n\n"
                    "1. THE PRINCIPLE: state it plainly - a red herring is a true fact that points the "
                    "wrong way, never a false statement. Explain what goes wrong when a writer breaks "
                    "this, and how readers detect it.\n"
                    "2. THE HERRING LIST: 5-7 red herrings for my story. For each: the true fact, why it "
                    "points at the wrong person or theory, who it implicates, and the innocent explanation "
                    "that eventually surfaces.\n"
                    "3. THE SECRET HERRINGS: for each suspect, how their genuine secret from Prompt 7 "
                    "functions as misdirection. This is the highest-value source - it costs nothing and is "
                    "always honest.\n"
                    "4. THE OBVIOUS SUSPECT: which character the reader will settle on, why, and the "
                    "moment they are cleared. Every short mystery needs one and needs to dispose of it.\n"
                    "5. THE DOUBLE BLUFF: whether my story uses the too-obvious-to-be-guilty move, and if "
                    "so how to keep it from reading as a cliche.\n"
                    "6. THE ATTENTION BUDGET: how much page time goes to herrings versus real clues. Real "
                    "clues should get LESS attention, not more - state the ratio and the reason.\n"
                    "7. THE EMPHASIS TRAP: places where my prose currently signals importance - a "
                    "paragraph break before a detail, a character remarking on it, a scene ending on it. "
                    "Flag them, because emphasis is the most common accidental tell.\n"
                    "8. THE DEAD END: at least one line of investigation that goes nowhere, honestly. Real "
                    "investigations have them, and their absence makes a story feel engineered.\n"
                    "9. THE REREAD PROMISE: for each herring, confirm that on a second reading it is "
                    "clearly innocent rather than clearly a cheat. Name any that fails.\n"
                    "10. THE COINCIDENCE AUDIT: any place I am relying on coincidence to misdirect. "
                    "Replace each with something caused.\n\n"
                    "End by asking me whether any of my red herrings are more interesting than my solution, "
                    "because if so I may be writing the wrong story."
                ),
                "pro_tip": (
                    "Item 6 is the rule that separates competent from good. Give your real clues less "
                    "attention than your herrings - a detail the prose lingers on is a detail the reader "
                    "files, and a detail the prose passes over is one they will not remember until they "
                    "need to."
                ),
            },
            {
                "title": "The Two Timelines",
                "desc": (
                    "What happened, and the order the reader learns it. Holding these apart deliberately "
                    "is how a mystery is constructed rather than merely written."
                ),
                "prompt_text": (
                    "You are a mystery structural editor who works in two timelines at once.\n\n"
                    "My true sequence with real chronology: [PASTE FROM PROMPT 2 ITEM 2]\n"
                    "My clue ladder with word positions: [PASTE FROM PROMPT 9]\n"
                    "My suspicion rotation map: [PASTE FROM PROMPT 7 ITEM 7]\n\n"
                    "Do the following:\n\n"
                    "1. TIMELINE A - THE TRUTH: restate the real chronology as a clean numbered list. This "
                    "never appears in the story in this form.\n"
                    "2. TIMELINE B - THE REVELATION ORDER: the order in which the reader learns things, as "
                    "a numbered list mapped to word positions. This IS the story's structure.\n"
                    "3. THE DIVERGENCE MAP: show where the two timelines differ most - which true events "
                    "the reader learns last, and which they learn early but misunderstand. The gap between "
                    "the two lists is the entire craft of the genre.\n"
                    "4. THE READER'S THEORY, TRACKED: at four points across the word count, state what the "
                    "reader currently believes happened. If their theory never changes, the story is flat - "
                    "flag it.\n"
                    "5. THE DETECTIVE'S KNOWLEDGE, TRACKED: the same four points, for the investigator. "
                    "Confirm the reader is never more than a beat behind, per my contract.\n"
                    "6. THE INFORMATION GAPS: any place the reader knows more than the detective, and "
                    "whether that is deliberate dread (good) or an accident (bad).\n"
                    "7. THE WITHHOLDING AUDIT: everything the story delays. For each, is it delayed "
                    "because the detective has not found it, or because I am hiding it from the reader? "
                    "The first is structure; the second is a fair-play breach unless my sub-genre permits "
                    "it.\n"
                    "8. THE FLASHBACK QUESTION: whether this story needs one. At short length the answer "
                    "is usually no - say whether mine is the exception and what it would cost.\n"
                    "9. THE RECONSTRUCTION: how much of Timeline A the reader is given at the reveal. "
                    "Recommend the minimum, since a reveal that replays the whole crime is the most common "
                    "way short mysteries end badly.\n\n"
                    "End by asking me at which point the reader should first suspect the truth, because "
                    "the answer should never be 'the last page'."
                ),
                "pro_tip": (
                    "Item 7 is the audit that catches genuine cheating. If information is delayed because "
                    "the author is hiding it rather than because the detective has not found it, you have "
                    "broken the contract - and that is the distinction readers articulate as 'unfair' "
                    "without being able to name why."
                ),
            },
            {
                "title": "Concealment at Short Length",
                "desc": (
                    "The techniques that replace distance. This is the craft that makes a four-thousand-"
                    "word mystery possible at all."
                ),
                "prompt_text": (
                    "You are a mystery craft specialist teaching concealment in short fiction, where the "
                    "novel's main tool - distance - is unavailable.\n\n"
                    "My clue ladder with concealment methods assigned: [PASTE FROM PROMPT 9]\n"
                    "My word count: [FROM PROMPT 1]\n"
                    "My load-bearing clue: [FROM PROMPT 3 ITEM 3]\n\n"
                    "Do the following:\n\n"
                    "1. THE TECHNIQUE SET: explain each concealment technique available at short length, "
                    "with a worked example of each using MY material:\n"
                    "   - THE LIST: the clue is item three of five similar things, none emphasised\n"
                    "   - THE DISGUISE: the clue reads as characterisation or setting rather than evidence\n"
                    "   - THE DISCOUNTED SOURCE: it comes from someone the reader has reason not to attend "
                    "to - a child, a drunk, a gossip, a bore, someone the detective dislikes\n"
                    "   - THE OVERSHADOW: it sits in the same paragraph as something more dramatic\n"
                    "   - THE PREMATURE: it arrives before the reader has any framework for it\n"
                    "   - THE ABSENCE: what is missing rather than what is present\n"
                    "   - THE SPLIT: half here, half there, neither meaning anything alone\n"
                    "   - THE PLAIN STATEMENT: told flatly and completely, trusting that no one believes "
                    "the answer would simply be given\n"
                    "2. THE ASSIGNMENT REVIEW: go through my clue ladder and check each clue's assigned "
                    "technique suits it. Reassign any that do not, and flag any technique I have used more "
                    "than twice - repetition makes a method visible.\n"
                    "3. THE LOAD-BEARING TREATMENT: for my most important clue, design the concealment in "
                    "detail. Write the actual sentence or short passage containing it, in three different "
                    "techniques, so I can choose.\n"
                    "4. THE PROSE-LEVEL TELLS: the specific ways prose accidentally signals a clue - a "
                    "sentence that is shorter than its neighbours, a paragraph ending on the detail, a word "
                    "choice more precise than the surrounding text, a character pausing. Audit my habits "
                    "and name my likely tell.\n"
                    "5. THE RHYTHM CAMOUFLAGE: how to place clues so the sentence rhythm does not mark "
                    "them. Give me the rule and one demonstration.\n"
                    "6. THE REREAD DESIGN: for each concealed clue, write the one sentence a reader will "
                    "think on the second pass. If you cannot write it, the clue is not actually there.\n"
                    "7. THE OVER-CONCEALMENT WARNING: any clue now hidden so well it is effectively "
                    "absent. This is as bad as omitting it - name any that crossed the line.\n"
                    "8. THE FLASH ADAPTATION: if my story is under 1,500 words, how these techniques "
                    "change. At that length there is room for perhaps two clues and one herring - tell me "
                    "which of mine survive.\n\n"
                    "End by asking me to hand the draft to someone and ask them to guess, because the only "
                    "real test of concealment is a reader who has not seen the solution."
                ),
                "pro_tip": (
                    "The Discounted Source is the most powerful technique in short mystery and the least "
                    "used. Put the load-bearing clue in the mouth of a character the detective finds "
                    "tedious - readers stop listening exactly when the detective does."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: STRUCTURE IT",
        "intro": (
            "Three prompts on shape. Mystery shorts use their own forms, the investigation has to move "
            "against a word budget, and the reveal needs to be far shorter than instinct suggests."
        ),
        "prompts": [
            {
                "title": "The Mystery Short Shapes",
                "desc": (
                    "The structures short crime actually uses, most of which are not the novel's "
                    "investigation arc scaled down."
                ),
                "prompt_text": (
                    "You are a structural editor who works specifically in short crime fiction.\n\n"
                    "My sub-genre and length: [PASTE FROM PROMPT 1]\n"
                    "My revelation-order timeline: [PASTE FROM PROMPT 11 ITEM 2]\n"
                    "My detective and their access problem: [PASTE FROM PROMPT 8]\n\n"
                    "Do the following:\n\n"
                    "1. THE SHAPE OPTIONS: describe these, with the sub-genre and length each suits:\n"
                    "   - THE SINGLE INTERVIEW: one conversation, real time, the truth emerging inside it\n"
                    "   - THE CLASSIC MINIATURE: discovery, suspects, investigation, reveal, compressed\n"
                    "   - THE INVERTED: we watch the crime, then watch it unravel\n"
                    "   - THE REFRAME: a situation presented one way, then shown to be another\n"
                    "   - THE PROCEDURAL SLICE: one step of a case, complete in itself\n"
                    "   - THE CONFESSION: someone telling it, with the truth leaking through\n"
                    "   - THE SCENE-AND-SOLVE: one scene of crime, one of solution, nothing between\n"
                    "   - THE FRAME: a case recounted later, with the telling itself significant\n"
                    "2. THE RECOMMENDATION: pick the one that fits my material and defend it. Then name "
                    "the shape I was probably defaulting to and say why it is weaker at my length.\n"
                    "3. THE SHAPE'S RULES: the 4 rules mine imposes, and where it collapses.\n"
                    "4. THE SCENE COUNT: how many scenes my length and shape support. Warn me what happens "
                    "above it.\n"
                    "5. THE OPENING POSITION: where this shape starts relative to the crime - before, at "
                    "discovery, mid-investigation, or after everything. Recommend one.\n"
                    "6. THE INTERROGATION PROBLEM: short mysteries often become a queue of interviews. "
                    "Tell me how many my length can hold, and give me 4 alternatives to an interview scene "
                    "that deliver the same information.\n"
                    "7. THE POV AND TENSE: recommend both for my shape and sub-genre, checked against my "
                    "viewpoint problem from Prompt 4.\n"
                    "8. THE FAILURE MODE: how stories in my chosen shape fall apart, with the early "
                    "warning sign.\n\n"
                    "End by asking me whether the reader is solving alongside the detective or watching "
                    "them solve it, because that governs the whole structure."
                ),
                "pro_tip": (
                    "The Single Interview is the most under-attempted shape in short crime and the most "
                    "efficient. One room, two people, real time - the whole case emerges through what one "
                    "of them will not say."
                ),
            },
            {
                "title": "The Investigation Beat Map",
                "desc": (
                    "Scene by scene against word count, with every clue and herring placed - the document "
                    "you draft from."
                ),
                "prompt_text": (
                    "You are a mystery editor mapping a short story's beats before drafting.\n\n"
                    "My shape and its rules: [PASTE FROM PROMPT 13]\n"
                    "My clue ladder with positions: [PASTE FROM PROMPT 9]\n"
                    "My red herrings: [PASTE FROM PROMPT 10]\n"
                    "My suspicion rotation map: [PASTE FROM PROMPT 7 ITEM 7]\n"
                    "My revelation-order timeline: [FROM PROMPT 11]\n"
                    "My word count and scene count: [FROM PROMPTS 1 AND 13]\n\n"
                    "Build my BEAT MAP. For each scene:\n\n"
                    "1. Scene number, location, who is present, and the word allocation with running "
                    "total.\n"
                    "2. THE SCENE'S JOB in one sentence.\n"
                    "3. THE CLUES PLANTED here, by number from my ladder, with their concealment method.\n"
                    "4. THE HERRINGS deployed here.\n"
                    "5. THE READER'S THEORY at the end of this scene - what they now believe.\n"
                    "6. THE TURN: what is different at the end of the scene than the start. A scene with "
                    "no turn is a candidate for cutting even if it carries a clue - the clue relocates.\n"
                    "7. HOW IT GETS OUT: the last beat, and the pull into the next scene.\n\n"
                    "Then give me:\n"
                    "8. THE PACING AUDIT: whether clues and herrings are distributed or clustered, and "
                    "whether the reader's theory changes often enough. At least two shifts in a short "
                    "story.\n"
                    "9. THE INTERVIEW COUNT: how many scenes are people being questioned. If it is more "
                    "than my shape allows, name which to convert into something else.\n"
                    "10. THE STAKES CHECK: what is at risk beyond the puzzle. A short mystery where only "
                    "curiosity is at stake reads as an exercise - name the human cost and where it appears.\n"
                    "11. THE CUT LIST: any scene not planting a clue, deploying a herring, changing the "
                    "theory, or raising the stakes.\n"
                    "12. THE ENTRY CHECK: for each scene, whether it starts too early. Most should begin "
                    "later than instinct suggests, especially interviews - start on the answer, not the "
                    "greeting.\n\n"
                    "End by asking me which scene exists mainly because I enjoy writing it, so we can "
                    "check the story needs it."
                ),
                "pro_tip": (
                    "Item 12 applied to interviews will find you a thousand words. Cut the arrival, the "
                    "offer of tea and the first three questions - start on the line that matters and the "
                    "scene reads twice as sharp."
                ),
            },
            {
                "title": "The Reveal",
                "desc": (
                    "Shorter than you think. This prompt builds the climax so it lands as a click of "
                    "understanding rather than a lecture."
                ),
                "prompt_text": (
                    "You are a mystery editor who believes most reveals are three times too long.\n\n"
                    "My solution as the detective states it: [PASTE FROM PROMPT 3 ITEM 1]\n"
                    "My chain of reasoning: [PASTE FROM PROMPT 3 ITEM 2]\n"
                    "My reveal mechanism: [PASTE FROM PROMPT 3 ITEM 7]\n"
                    "My culprit's confrontation behaviour: [PASTE FROM PROMPT 6 ITEM 9]\n"
                    "My reconstruction minimum: [FROM PROMPT 11 ITEM 9]\n"
                    "My tone lock: [FROM PROMPT 4 ITEM 7]\n\n"
                    "Do the following:\n\n"
                    "1. THE REVEAL, DRAFTED: write it. Hold to 250-400 words depending on my length. It "
                    "must deliver the chain of reasoning without restating the whole crime.\n"
                    "2. WHAT TO LEAVE OUT: everything the reader can now reconstruct themselves. List it "
                    "explicitly - this list is usually longer than what stays.\n"
                    "3. TWO ALTERNATIVES: the same reveal by two other mechanisms - one spoken, one "
                    "enacted without explanation. The second is frequently stronger; say whether it suits "
                    "my sub-genre.\n"
                    "4. THE TRIGGER: what prompts the detective to see it. It must be something that "
                    "happens, not simply thinking harder - a remark, an object, a repetition, a "
                    "contradiction surfacing.\n"
                    "5. THE 'OF COURSE' PLACEMENT: where my rereadable detail from Prompt 3 item 6 gets "
                    "referenced, and how lightly. One touch, not a recap.\n"
                    "6. THE CONFRONTATION: whether the culprit is present, and what that changes. Consider "
                    "the version where they are not - it is often more devastating and always shorter.\n"
                    "7. THE AFTERMATH: how many words remain after the reveal, and what they do. Warn me "
                    "about both failures - stopping so fast the reveal cannot land, and explaining for a "
                    "page afterwards.\n"
                    "8. THE LAST LINE: 5 candidates. For each, say whether it reframes, summarises or "
                    "explains, and discard the last two categories.\n"
                    "9. THE JUSTICE QUESTION: what happens to the culprit, and whether the story shows it. "
                    "In short crime, leaving it unshown is frequently the stronger choice.\n"
                    "10. THE COST DELIVERED: confirm the solution costs someone something, per Prompt 3 "
                    "item 8, and that the reader feels it.\n\n"
                    "End by asking me whether the reader will want to go back to the beginning, because "
                    "that impulse is the entire measure of a mystery's ending."
                ),
                "pro_tip": (
                    "Item 3's second option deserves a real attempt. A detective who says nothing and "
                    "simply does something - makes a call, returns an object, walks away - lets the reader "
                    "complete the deduction themselves, which is the most satisfying version of this "
                    "genre's pleasure."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 5: WRITE IT",
        "intro": (
            "Three prompts. The opening has a job specific to this genre, the draft has to plant "
            "everything on the ladder, and the compression pass has to cut fifteen percent without "
            "touching a clue."
        ),
        "prompts": [
            {
                "title": "The Opening",
                "desc": (
                    "A mystery opening does a job no other genre's does: it must promise a puzzle, "
                    "establish the contract, and already be hiding something."
                ),
                "prompt_text": (
                    "You are a crime fiction first reader who decides on the first paragraph.\n\n"
                    "My shape and opening position: [PASTE FROM PROMPT 13]\n"
                    "My beat map, scene one: [PASTE FROM PROMPT 14]\n"
                    "My detective and their voice: [PASTE FROM PROMPT 8]\n"
                    "My sub-genre and tone lock: [FROM PROMPTS 1 AND 4]\n"
                    "My clue ladder - anything planted early: [FROM PROMPT 9]\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET, PLUS NOTES "
                    "ON YOUR OWN STYLE]\n\n"
                    "Do the following:\n\n"
                    "1. THE OPENING'S JOB: state what a mystery opening specifically owes - a promise of "
                    "puzzle, a voice, a situation, and the genre signal that tells a reader what kind of "
                    "crime story this is. Then say what mine must do given my shape.\n"
                    "2. THE OPENING PARAGRAPH: write it. Something already happening. No weather, no "
                    "waking, no scene-setting, no body described in loving detail before anyone cares.\n"
                    "3. THREE ALTERNATIVES: three more, each with a different strategy - opening on the "
                    "crime, on the detective mid-task, on a voice, or on a detail that will matter later.\n"
                    "4. THE EARLY PLANT: if my ladder puts a clue in the first quarter, show me the "
                    "version of the opening that contains it, concealed. Early clues are the best-hidden "
                    "ones.\n"
                    "5. THE FIRST PAGE: extend the strongest version to roughly 400 words.\n"
                    "6. THE CONTRACT SIGNAL: confirm the opening tells the reader what standard of fair "
                    "play to expect. A cozy and a noir make different promises in their first lines - name "
                    "how mine does it.\n"
                    "7. THE FIRST-PAGE AUDIT: what a reader knows, what they are curious about, and "
                    "anything I explained that I should have implied.\n"
                    "8. THE HOOK CHECK: what question the opening plants that a reader needs answered. In "
                    "this genre it does not have to be 'who did it' - it can be smaller and stranger.\n\n"
                    "End by asking me whether an editor with a hundred crime submissions would read the "
                    "second paragraph, and which line makes them."
                ),
                "pro_tip": (
                    "Item 4 is the move worth taking. An opening that carries a concealed clue is doing "
                    "two jobs at once - and a clue placed before the reader knows a crime has happened is "
                    "the most invisible placement available anywhere in the form."
                ),
            },
            {
                "title": "The Draft",
                "desc": (
                    "The whole story in one pass, with every clue and herring planted where the ladder "
                    "says and concealed by the assigned method."
                ),
                "prompt_text": (
                    "You are my drafting partner on a mystery short story. You write in my voice and hand "
                    "control back at the end.\n\n"
                    "CONTEXT:\n"
                    "- My approved opening and voice sample: [PASTE FROM PROMPT 16]\n"
                    "- My sub-genre, fair-play level and contract: [PASTE FROM PROMPTS 1 AND 4]\n"
                    "- My beat map with word allocations: [PASTE FROM PROMPT 14]\n"
                    "- My clue ladder with concealment methods: [PASTE FROM PROMPT 9]\n"
                    "- My red herrings: [PASTE FROM PROMPT 10]\n"
                    "- My cast - victim, culprit, suspects, detective: [PASTE FROM PROMPTS 5-8]\n"
                    "- My revelation-order timeline: [FROM PROMPT 11]\n"
                    "- My reveal and last line: [PASTE FROM PROMPT 15]\n"
                    "- POV, tense and the interiority rule: [FROM PROMPTS 8 AND 13]\n"
                    "- Target word count: [FROM PROMPT 1]\n\n"
                    "Write the complete story, following these rules:\n\n"
                    "1. Match the voice sample in rhythm and psychic distance.\n"
                    "2. Hold one POV and one tense. Never let the viewpoint conceal its own knowledge - "
                    "use the interiority technique from Prompt 8 item 8 when the detective realises "
                    "something.\n"
                    "3. Plant EVERY clue on the ladder, in its assigned scene, using its assigned "
                    "concealment method. Do not emphasise them.\n"
                    "4. Deploy every red herring as true information pointed wrong. Never write a false "
                    "statement as narration.\n"
                    "5. Give real clues LESS attention than herrings.\n"
                    "6. Include the neutral detail budget so clues have somewhere to hide.\n"
                    "7. Start every scene late, especially interviews.\n"
                    "8. Hit the word allocations. If a scene runs long, cut something else and say what.\n"
                    "9. End on my approved last line.\n\n"
                    "After the story, give me: the word count, a per-scene breakdown against allocations, "
                    "a CLUE PLACEMENT REPORT confirming every ladder item appears and where, any clue you "
                    "could not conceal as assigned, and anything in my plan that did not work once "
                    "written.\n\n"
                    "End by asking me which clue felt most conspicuous while you were writing it, because "
                    "that is the one to re-conceal."
                ),
                "pro_tip": (
                    "The clue placement report is the deliverable to insist on. A draft that quietly "
                    "dropped clue four is a story that cannot be solved - and you will not notice reading "
                    "it yourself, because you already know the answer."
                ),
            },
            {
                "title": "The Compression Pass",
                "desc": (
                    "Cut fifteen percent - but in this genre you cannot cut a clue, so the compression has "
                    "to come from everywhere else."
                ),
                "prompt_text": (
                    "You are a line editor compressing a mystery short story. You know that clues are "
                    "load-bearing and everything else is negotiable.\n\n"
                    "My draft: [PASTE IT]\n"
                    "My clue ladder: [PASTE FROM PROMPT 9]\n"
                    "My current and target word count: [STATE BOTH]\n\n"
                    "Do the following:\n\n"
                    "1. THE PROTECTED LIST: identify every sentence containing a clue or a ruling-out "
                    "detail. These are protected - no cuts, and no rewording that changes their "
                    "concealment.\n"
                    "2. THE FAT MAP: where the excess sits. In mystery shorts it is nearly always "
                    "interview preamble, the detective travelling between locations, restated suspicion, "
                    "and the paragraph after the reveal.\n"
                    "3. THE INTERVIEW COMPRESSION: for each questioning scene, cut the arrival, the "
                    "pleasantries and any question whose answer the reader can infer. Show me the cuts.\n"
                    "4. THE TRAVEL CUT: every transition between locations that could be a section break.\n"
                    "5. THE RESTATEMENT SWEEP: every place the detective or narration recaps what we "
                    "already know. In a short story the reader has not forgotten - cut all of it.\n"
                    "6. THE SENTENCE COMPRESSIONS: the 20 highest-value sentence-level cuts outside the "
                    "protected list, with original, compressed, and words saved.\n"
                    "7. THE SUSPECT CONSOLIDATION: if I am still over, which suspect to merge or remove, "
                    "and where their clues and herrings relocate. This is the structural cut of last "
                    "resort - warn me what it costs.\n"
                    "8. THE REVEAL TRIM: the reveal against my target from Prompt 15. Cut it to length.\n"
                    "9. THE FINAL PARAGRAPH CHECK: the sentence the story should end on, and what to "
                    "delete after it.\n"
                    "10. THE CLUE INTEGRITY RE-CHECK: after all cuts, confirm every ladder item is still "
                    "present and still concealed. Name anything the compression damaged.\n"
                    "11. THE COUNT: the new word count against target.\n\n"
                    "Return the cuts as a list with running totals. Do not rewrite the whole story.\n\n"
                    "End by asking me whether any cut removed a clue's hiding place, because a clue that "
                    "is now conspicuous is as broken as one that is gone."
                ),
                "pro_tip": (
                    "Item 11's warning is real and easy to miss. Compression often deletes the neutral "
                    "detail a clue was hiding among, leaving the clue sitting alone and obvious - always "
                    "re-check concealment after cutting, not just presence."
                ),
            },
        ],
    },

    {
        "name": "PHASE 6: AUDIT AND SEND",
        "intro": (
            "Four prompts, and the first is the one this whole pack was built for. A reader will run the "
            "fair-play audit whether you do or not - the only question is whether you find the breach "
            "first."
        ),
        "prompts": [
            {
                "title": "The Fair-Play Audit",
                "desc": (
                    "The audit the genre lives or dies on. Every clue checked for presence, placement and "
                    "honest concealment, against the contract you signed in Prompt 4."
                ),
                "prompt_text": (
                    "You are an adversarial mystery reader whose job is to find the cheat. You are on the "
                    "reader's side, not the writer's.\n\n"
                    "My fair-play contract and the rules I said I was breaking: [PASTE FROM PROMPT 4]\n"
                    "My clue ladder with concealment methods: [PASTE FROM PROMPT 9]\n"
                    "My chain of reasoning: [PASTE FROM PROMPT 3 ITEM 2]\n"
                    "My alternative solutions and ruling-out details: [PASTE FROM PROMPT 3 ITEM 5]\n"
                    "My finished story: [PASTE IT]\n\n"
                    "Audit, citing a location for every finding:\n\n"
                    "1. THE PRESENCE CHECK: go through the chain of reasoning step by step. For each step, "
                    "quote the exact text where the reader was given the supporting evidence. Any step "
                    "where you cannot quote something is a BREACH - the most serious finding in this "
                    "genre.\n"
                    "2. THE TIMING CHECK: confirm every clue appears before the reveal, and that the "
                    "reader had it at the same time the detective did.\n"
                    "3. THE CULPRIT PRESENCE CHECK: confirm the culprit appears early, is characterised, "
                    "and is not introduced or first made significant in the final act.\n"
                    "4. THE VIEWPOINT INTEGRITY CHECK: every place the viewpoint character knew something "
                    "and the narration did not report it. Quote each. This is the most common accidental "
                    "cheat.\n"
                    "5. THE HERRING HONESTY CHECK: every red herring, confirmed as a true fact pointed "
                    "wrong rather than a false statement. Flag any that is a lie in narration.\n"
                    "6. THE ALTERNATIVE SOLUTION TEST: construct the strongest case you can that someone "
                    "ELSE did it, using only what is on the page. If you can build one that the story does "
                    "not rule out, the solution is not tight - show me the gap.\n"
                    "7. THE COINCIDENCE CHECK: every place the case advances by luck rather than by "
                    "investigation.\n"
                    "8. THE CONFESSION CHECK: whether the solution rests on someone admitting it. If so, "
                    "confirm the evidence forced the admission rather than the admission supplying the "
                    "evidence.\n"
                    "9. THE CONTRACT AUDIT: check the story against each numbered rule from Prompt 4. Name "
                    "every rule broken that I did not declare.\n"
                    "10. THE CONCEALMENT CHECK, BOTH DIRECTIONS: any clue now too obvious, and any clue "
                    "now so hidden it is effectively absent. Both are failures.\n"
                    "11. THE REREAD SIMULATION: list the details a reader will find on a second pass. If "
                    "the list is short, the story does not reward rereading and that is the genre's main "
                    "pleasure.\n\n"
                    "Rank findings CRITICAL (a breach), MODERATE, or MINOR, with a fix for every CRITICAL.\n\n"
                    "End by asking me which finding I want to argue with, because in this genre the one I "
                    "defend hardest is usually the real breach."
                ),
                "pro_tip": (
                    "Item 1's instruction to QUOTE the text is what makes this audit work. Asking whether "
                    "a clue is present gets you a yes; asking for the exact sentence gets you the truth, "
                    "and that is how you find the step you only ever established in your own head."
                ),
            },
            {
                "title": "The Craft Audit",
                "desc": (
                    "The technical pass - the non-mystery failures that get a crime story rejected before "
                    "anyone assesses the puzzle."
                ),
                "prompt_text": (
                    "You are a crime magazine first reader listing the technical reasons a story is "
                    "rejected before its mystery is even considered.\n\n"
                    "My sub-genre contract and rejection triggers: [PASTE FROM PROMPT 1 ITEM 3]\n"
                    "My POV, tense and interiority rule: [PASTE FROM PROMPT 8]\n"
                    "My tone lock: [FROM PROMPT 4 ITEM 7]\n"
                    "My story: [PASTE IT]\n\n"
                    "Audit and cite each location:\n\n"
                    "1. POV AND TENSE SLIPS: every inconsistency, including inside recollections.\n"
                    "2. THE CAST CLARITY CHECK: any two characters a reader could confuse - by name, role, "
                    "age, manner or function. In mystery this is fatal, because confusing two suspects "
                    "destroys the puzzle.\n"
                    "3. THE DIALOGUE ATTRIBUTION: every exchange where it is unclear who is speaking. In a "
                    "multi-suspect scene this is a common and serious failure.\n"
                    "4. TELLING VERSUS SHOWING: emotions named rather than enacted, with the eight worst "
                    "dramatised. Then note where telling is correct and efficient in this genre, because "
                    "often it is.\n"
                    "5. THE EXPOSITION SWEEP: information delivered for the reader's benefit rather than "
                    "earned in the scene, especially in interviews.\n"
                    "6. THE PROCEDURE PLAUSIBILITY: anything about how an investigation, a scene, a body, "
                    "a lab result, an arrest or a legal process is handled that a knowledgeable reader "
                    "would reject. Flag what needs checking rather than inventing, and note where the "
                    "story should simply avoid specificity.\n"
                    "7. THE TIMELINE CONSISTENCY: every reference to time, duration and sequence checked "
                    "against my true chronology.\n"
                    "8. THE STATED THEME: any place the story explains its own meaning.\n"
                    "9. THE TONE CONSISTENCY: anything outside my tone lock - a cozy that turns grim, a "
                    "noir that goes cute.\n"
                    "10. FORMATTING AND MECHANICS: anything marking this as an amateur submission, noting "
                    "each market's guidelines override defaults.\n"
                    "11. THE OPENING-PAGE RE-READ: read only page one and give me the three strongest "
                    "reasons an editor stops there.\n\n"
                    "Rank findings CRITICAL, MODERATE or MINOR, with a fix for every CRITICAL.\n\n"
                    "End by asking me which critical fix requires restructuring, so I can plan it before "
                    "touching sentences."
                ),
                "pro_tip": (
                    "Item 2 matters more here than in any other genre. If a reader cannot hold your four "
                    "suspects apart, they cannot play the game - and they will blame the puzzle rather "
                    "than the naming, which means you never find out why the story failed."
                ),
            },
            {
                "title": "The Solvability Test",
                "desc": (
                    "The final judgement, and the hardest to run on your own work: could a reader actually "
                    "get there, and should they?"
                ),
                "prompt_text": (
                    "You are a mystery editor deciding whether to buy a story. Be honest rather than "
                    "encouraging.\n\n"
                    "My sub-genre, fair-play level and the appeals I am leading with: [PASTE FROM PROMPTS "
                    "1 AND 4]\n"
                    "My clue ladder: [PASTE FROM PROMPT 9]\n"
                    "My story: [PASTE IT]\n\n"
                    "Do the following:\n\n"
                    "1. THE COLD READ: read the story as though you do not know the solution. State, "
                    "honestly, at what point you worked it out - or that you did not.\n"
                    "2. THE DIFFICULTY VERDICT: rate the puzzle from 1 (a reader gets it on page two) to "
                    "10 (nobody gets it). Then tell me the target for my sub-genre, since a cozy wants a "
                    "solvable puzzle and a noir may want none at all.\n"
                    "3. THE TOO-EASY DIAGNOSIS: if it is too easy, name the specific tell - an "
                    "over-emphasised clue, a suspect field too small, a culprit too obviously positioned, "
                    "a conspicuous absence. Give me the fix.\n"
                    "4. THE TOO-HARD DIAGNOSIS: if it is unsolvable, name which step of the chain the "
                    "reader cannot make and what to add. Note that unsolvable is worse than easy - an easy "
                    "mystery is satisfying and an unfair one is not.\n"
                    "5. THE 'OF COURSE' CHECK: after the reveal, does the answer feel inevitable or "
                    "arbitrary? If arbitrary, name what is missing.\n"
                    "6. THE MEMORABLE ELEMENT: what a reader remembers in a week - the trick, a character, "
                    "an image, a line. If it is only the trick, the story is a puzzle rather than fiction "
                    "and will be read once.\n"
                    "7. THE HUMAN VERDICT: whether anything is at stake beyond the answer, and whether the "
                    "reader feels the cost.\n"
                    "8. THE COMPARISON VERDICT: against the kind of crime short that gets published, does "
                    "this compete? Answer as an editor.\n"
                    "9. THE TWO-MINUTE FIXES: the three changes with the highest improvement per unit of "
                    "effort.\n"
                    "10. THE LIKELY REJECTION REASON: what it would be. Answer as the person rejecting "
                    "it.\n"
                    "11. THE VERDICT: submit as is, one more pass, or set aside. Pick one.\n\n"
                    "End by asking me to give the draft to one person who reads crime and ask only 'who "
                    "did it and when did you know', because their answer is worth more than this whole "
                    "audit."
                ),
                "pro_tip": (
                    "Item 4's note is the one to internalise. Readers forgive an easy mystery and never "
                    "forgive an unfair one - if you must err, err toward solvable, because the pleasure of "
                    "being right is nearly as good as the pleasure of being fooled."
                ),
            },
            {
                "title": "Markets, Contests and the Recurring Detective",
                "desc": (
                    "Where crime shorts go - a healthier market than most short fiction - plus the "
                    "question of whether this detective comes back."
                ),
                "prompt_text": (
                    "You are a submissions strategist for crime and mystery short fiction. You explain "
                    "principles rather than naming markets, since guidelines and rates change.\n\n"
                    "My sub-genre, length and tone: [PASTE FROM PROMPTS 1 AND 4]\n"
                    "My story and its verdict: [PASTE FROM PROMPT 21]\n"
                    "My detective and whether they could carry more: [FROM PROMPT 8]\n\n"
                    "Do the following:\n\n"
                    "1. THE ECOSYSTEM: how crime and mystery short markets differ from general literary "
                    "ones - the dedicated genre magazines, the anthology culture, themed calls, and why "
                    "this is one of the healthier short fiction markets.\n"
                    "2. THE MARKET PROFILE: the kinds of venue this specific story suits - by sub-genre, "
                    "length, tone and payment tier - so I can find current ones in a market database.\n"
                    "3. THE ANTHOLOGY ROUTE: how themed crime anthologies work, why they are unusually "
                    "accessible, and how to write toward a call without writing something that only fits "
                    "that call.\n"
                    "4. THE CONTEST LANDSCAPE: the crime-specific competitions, how to judge one worth "
                    "entering, and what entry fees are reasonable against prize and prestige.\n"
                    "5. THE SUBMISSION LADDER: how to order submissions, and why to start at the top of "
                    "what is plausible.\n"
                    "6. THE MECHANICS: simultaneous submissions, response times, querying, and the note "
                    "that each market's rules differ and must be read.\n"
                    "7. THE TRACKING TABLE: the columns to keep.\n"
                    "8. THE REJECTION READ: distinguishing a form rejection, a higher-tier form, and a "
                    "personal one - and what each says about the story.\n"
                    "9. THE RECURRING DETECTIVE QUESTION: whether mine should return. Cover what a series "
                    "detective needs that a one-off does not - a method that generates cases, a personal "
                    "thread that can develop, a setting with a supply of crime, and a voice worth "
                    "revisiting. Then say honestly whether mine has them.\n"
                    "10. THE SERIES ECONOMICS: why a recurring detective is valuable in short crime "
                    "specifically - editors buy familiar characters, and a body of linked stories becomes "
                    "a collection more naturally than unlinked ones.\n"
                    "11. THE NEXT CASE: if my detective recurs, three case concepts that would demonstrate "
                    "range rather than repeat this one - a different sub-genre shape, a different "
                    "relationship to the crime, a case they fail.\n"
                    "12. THE COLLECTION PATH: how many linked crime stories make a book, and what binds "
                    "them beyond the detective.\n\n"
                    "End by asking me whether I want to write about this person again, because that answer "
                    "is worth more than any market analysis."
                ),
                "pro_tip": (
                    "Item 11's third option is the one to take seriously. A story where your detective "
                    "fails - gets it wrong, or solves it too late - is the one that turns a series "
                    "character into a person, and editors remember it."
                ),
            },
        ],
    },
]
