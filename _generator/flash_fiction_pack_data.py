# -*- coding: utf-8 -*-
"""
Royalti Studios - Flash Fiction Master Prompt Pack (Adult Fiction Line).

Companion to the Short Story pack, not a subset of it. That pack treats flash as
one of five length bands; this one treats it as its own form, including the micro
sub-forms (drabble, dribble, hint fiction) that a general short story pack has no
room for.

Build with:
    python pack_builder.py flash_fiction_pack_data \
        "Flash_Fiction_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.

PROMPT COUNT: 16, below the 22 baseline. Approved by the user on 2026-09-21.
Reasons: the form has no scenes, no subplot, no chapter or scene budget, no
series runway and no multi-pass drafting. Compression is the spine rather than
a phase.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "FLASH FICTION",
    "total_prompts": 16,
    "hook_line": "A whole story under a thousand words - where the title is part of the text, the last line is the turn, and there is nowhere to hide a single wasted syllable.",
    "keyword_lines": [
        "Any genre • One image • One turn • The title does the work • Exact counts",
        "Flash • Micro • Drabble (100) • Dribble (50) • Hint fiction • Borrowed forms",
    ],
    "subgenres_line": "Forms: Flash (500-1,000), Micro (100-500), Drabble (exactly 100), Dribble (exactly 50), Hint Fiction (under 25), Prose-Poem Adjacent, Borrowed-Form Flash",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-21",
    "audience_line": "Adult Fiction Line",
    "cover_h2": "From One Image to a Finished Piece",
    "closing_tagline": "You do not have room for a scene. You have room for a life, if you choose the right sentence.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "Flash is not a short story that ran out of road. It is its own form, with its own rules, and "
        "most of what makes a 4,000-word story work will sink a 400-word one. There is no room for a "
        "scene, so character arrives in a sentence. There is no room for a structure, so the shape is "
        "borrowed or built from a single move. The title is not a label - it is a line of the text, often "
        "the line carrying the most meaning. And the last line is usually the turn itself, which means "
        "you write backwards from it. This pack treats all of that as the craft rather than as "
        "compromise, and it covers the micro forms too - the drabble at exactly one hundred words, the "
        "dribble at fifty, hint fiction under twenty-five - where the count is the form. Work in order "
        "and keep every output in one document. By Prompt 16 you have a finished piece and a plan for the "
        "next twenty."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-3) - Lock the form. Pick your exact form and count, name the single thing the "
        "piece delivers, and test honestly whether what you have is flash, a fragment, or a short story "
        "in hiding.",
        "Phase 2 (Prompts 4-6) - Build it. A character established in one sentence, a title written as "
        "part of the text, and the one concrete detail that carries the entire world.",
        "Phase 3 (Prompts 7-9) - Shape it. The structures flash actually uses, the first fifteen words, "
        "and the last line - which in this form is usually the whole point.",
        "Phase 4 (Prompts 10-12) - Write it. The draft, compression to an exact count, and a read-aloud "
        "pass, because at this length rhythm is most of the effect.",
        "Phase 5 (Prompts 13-16) - Finish and send. The craft audit, the resonance test, the flash market "
        "and contest ecosystem, and a volume practice that turns single pieces into a body of work.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool and a place to save your outputs between prompts. Brackets like "
        "[THIS] are placeholders - replace them with your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular, and Prompt 1 tells you which prompts your form "
        "needs. Writing hint fiction under 25 words? Prompts 4 and 7 collapse almost entirely and Prompt 5 "
        "becomes the most important prompt in the pack. Writing a drabble at exactly 100? Prompt 11 is "
        "where the real work happens."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "One thing - a single image, turn or recognition, chosen before a word is written",
            "A title that is part of the text, doing work the prose then does not have to repeat",
            "Character delivered in one sentence of behaviour, never a description and never a history",
            "A last line that is the turn, not a summary of it",
            "One concrete detail standing in for an entire world, and no second one",
            "Implication over statement - the reader assembles most of the story and that is the pleasure",
            "A shape borrowed from something that is not a story: a list, a recipe, a form, an instruction",
            "Rhythm as structure, because at this length the sentences are the architecture",
            "Present-tense pressure or a single retrospective glance - one temporal position, held",
            "An exact count met precisely where the form demands it, because in a drabble the count IS the form",
        ],
        "kills": [
            "A short story with the middle deleted - three characters, a setting paragraph, and a rushed turn",
            "A setup that takes half the word count before anything happens",
            "Backstory, in any quantity, at any point",
            "Two characters given equal weight, when there is only room to make one land",
            "A twist that is just withheld information, which at this length reads as a cheat immediately",
            "A last line that explains the piece, or a last line that is a pun",
            "Naming the emotion, which in 400 words is the whole word count spent on nothing",
            "Adjective stacking to compensate for having no room for events",
            "A title that labels rather than participates - 'The Visit', 'The Letter', 'Goodbye'",
            "Calling something flash because it is short, when it is actually a fragment of a longer piece",
        ],
        "voice": [
            "Every sentence carries at least two of: character, situation, image, tone, turn",
            "Vary length hard - a two-word sentence next to a thirty-word one is the form's entire toolkit",
            "Concrete nouns exclusively; at this length an abstraction is a wasted line",
            "Cut every filtering verb - she saw, he felt, it seemed - without exception here",
            "One tense, one point of view, one temporal position; no flashbacks, ever",
            "Read it aloud at every stage, because rhythm does the work that structure does in longer forms",
            "Trust the gap: what is not said is the majority of a flash piece",
            "Spend your one beautiful sentence in the last third, never the first",
        ],
        "formula": (
            "THE ONE THING (chosen first) -> The Title, Carrying Part of the Meaning -> The First Fifteen "
            "Words, Already Inside the Situation -> The Character in a Sentence -> The One Detail -> The "
            "Pressure, in Two or Three Moves -> THE LAST LINE, Which Is the Turn"
        ),
        "reader_expectations": (
            "Flash readers read fast, read a lot, and are reading for the one that stops them. They expect "
            "to be inside the situation by the first line and to understand the piece only at the last, and "
            "they expect that final understanding to be worth the trip. They will assemble enormous amounts "
            "of story from very little if you give them the right details - and they will abandon a piece "
            "in ten words if it begins with setup. Editors of flash markets read hundreds a week and make a "
            "decision in the first sentence; they reject on padded openings, on titles that do no work, and "
            "on endings that explain. What they reward: a shape they have not seen, a detail that implies a "
            "whole life, and a last line they want to read twice. Where the form specifies an exact count, "
            "hitting it is not pedantry - it is the entry requirement."
        ),
        "level_spec": [
            "Flash: 500-1,000 words. Room for two or three moves and one character with a want",
            "Micro: 100-500 words. One move, one character, one detail. No scene",
            "Drabble: exactly 100 words, title excluded (confirm per market). The count is the form",
            "Dribble: exactly 50 words. A single image or single reversal",
            "Hint fiction: under 25 words. Implies a whole story without telling any of it",
            "Titles: in most flash markets the title is not counted; confirm per market, and assume it IS part of the text",
            "No flashbacks, no scene breaks below 500 words, no more than two named characters below 300 words",
        ],
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "Flash rewards the thing every other form makes you unlearn: trusting the reader completely. You "
        "have no room to explain, so you cannot, and the pieces that work are the ones where the writer "
        "gave three details and let a stranger build the rest. That is also why it is the best practice "
        "available - you can write one in an afternoon, learn something specific, and write another "
        "tomorrow. Choose the one thing, write backwards from the last line, cut to the exact count, and "
        "read it aloud. When a piece is not landing, the fault is almost always at the front: you are "
        "still setting up. Delete the first sentence and see what happens. It usually improves."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: LOCK THE FORM",
        "intro": (
            "Three prompts. In flash the exact count is not a target, it is a constraint that determines "
            "what the piece can contain - so lock it first. Then name the one thing the piece delivers, "
            "and find out honestly whether what you have is flash or a fragment of something longer."
        ),
        "prompts": [
            {
                "title": "The Form and Count Lock",
                "desc": (
                    "Flash spans 25 words to 1,000, and those are not the same form. This prompt picks "
                    "your exact form, locks the count, names your genre, and tells you what that "
                    "combination can hold."
                ),
                "prompt_text": (
                    "You are an editor of a flash fiction market who has read tens of thousands of "
                    "submissions across every micro form.\n\n"
                    "My idea is: [DESCRIBE IN 1-3 SENTENCES - or say 'I have an image and nothing else, "
                    "here it is']\n"
                    "My genre, if I know it: [NAME IT, OR SAY 'YOU TELL ME']\n"
                    "A count I have in mind, if any: [STATE IT, OR SAY 'YOU CHOOSE']\n\n"
                    "Do the following:\n\n"
                    "1. THE FORM LOCK: recommend one from - flash (500-1,000), micro (100-500), drabble "
                    "(exactly 100), dribble (exactly 50), hint fiction (under 25), prose-poem adjacent, "
                    "borrowed-form flash. Justify it against my idea.\n"
                    "2. THE EXACT COUNT: state my target count as a number. If my form has a fixed count, "
                    "say so plainly and note that the count is the entry requirement, not a guideline. "
                    "Also tell me whether the title is typically counted in my form, and that this varies "
                    "by market and must be checked.\n"
                    "3. WHAT THIS COUNT HOLDS: state precisely how many characters, how many moves, how "
                    "many details and how much time this count can carry. Write these as hard limits. Be "
                    "strict - most flash fails by trying to hold one thing too many.\n"
                    "4. THE GENRE LOCK: name my genre, then state the 3 things a flash reader of that "
                    "genre expects and the 2 things that get a flash piece in it rejected. Flash genre "
                    "expectations are different from novel ones - a horror flash needs one image, not a "
                    "dread arc.\n"
                    "5. THE GENRE'S FLASH PROBLEM: every genre has one thing that is nearly impossible in "
                    "under a thousand words. Name mine and tell me the technique flash writers use to get "
                    "around it.\n"
                    "6. THE COUNT REALITY CHECK: tell me honestly whether my idea fits my chosen count. "
                    "If it needs 800 words and I want a drabble, say so and tell me what to cut or what "
                    "the 100-word version of this idea actually is.\n"
                    "7. THE ROUTING NOTE: which prompts in this pack matter most for my form and genre, "
                    "and which are a light pass.\n\n"
                    "End by asking me whether I am writing to an exact count because a market requires "
                    "it, or because I chose it, since a required count is a different kind of problem."
                ),
                "pro_tip": (
                    "Item 3 is the whole discipline. Write the limits down. Nearly every failed flash "
                    "piece has one character, one detail or one move too many, and the fix is always "
                    "subtraction rather than better writing."
                ),
            },
            {
                "title": "The One Thing",
                "desc": (
                    "Flash delivers exactly one thing. This prompt names it, so everything else in the "
                    "piece can be measured against it or cut."
                ),
                "prompt_text": (
                    "You are a flash fiction editor who believes a piece under a thousand words can carry "
                    "one idea and no more.\n\n"
                    "My form, count and genre: [PASTE FROM PROMPT 1]\n"
                    "My idea: [PASTE OR DESCRIBE]\n\n"
                    "Do the following:\n\n"
                    "1. THE ONE THING: state in a single sentence the one thing this piece delivers. Then "
                    "classify it - is it an IMAGE (the reader is left with a picture), a TURN (the reader's "
                    "understanding reverses), a RECOGNITION (the reader sees something true they had not "
                    "articulated), or a VOICE (the pleasure is the person talking)? Say which, because each "
                    "builds differently.\n"
                    "2. FOUR ALTERNATIVES: four other one-things this material could deliver, and what "
                    "kind of piece each would make. Mark the least obvious.\n"
                    "3. THE BUILD METHOD: for my chosen type, the specific way flash constructs it. For an "
                    "image, what must be withheld until the end. For a turn, what the reader must believe "
                    "first. For a recognition, what specific must stand in for the general. For a voice, "
                    "what the speaker must want and not say.\n"
                    "4. THE TWO OR THREE MOVES: list the moves this piece makes, in order, inside my count "
                    "limits. A move is anything that changes what the reader understands. If you list more "
                    "than three, cut until you have two or three.\n"
                    "5. WHAT GETS CUT: everything about my idea that will not fit. List it explicitly, so "
                    "I stop trying to include it.\n"
                    "6. THE ONE-SENTENCE VERSION: write the whole piece as one sentence. If it does not "
                    "work as one sentence, the one thing is not yet clear - tell me.\n"
                    "7. THE ANTI-EFFECT: what I might accidentally produce instead - cleverness, "
                    "sentimentality, a joke, obscurity - and the warning sign for each.\n\n"
                    "End by asking me which of the four alternatives I would rather read, because that is "
                    "often the piece I should be writing."
                ),
                "pro_tip": (
                    "Item 1's classification is more useful than it looks. An image piece and a turn piece "
                    "are built in opposite directions - one withholds the picture, the other withholds the "
                    "meaning - and mixing the methods produces a piece that does neither."
                ),
            },
            {
                "title": "Is This Flash?",
                "desc": (
                    "The prompt that stops you submitting a fragment. Many flash drafts are openings, "
                    "scenes, or compressed short stories - this tells you which you have."
                ),
                "prompt_text": (
                    "You are a flash fiction first reader who is direct about what is not a finished "
                    "piece.\n\n"
                    "My form, count and the one thing: [PASTE FROM PROMPTS 1-2]\n"
                    "My idea or draft: [PASTE]\n\n"
                    "Do the following:\n\n"
                    "1. THE DIAGNOSIS: tell me plainly which of these I have - a flash piece, a fragment "
                    "(the opening of something longer), a scene (part of a story, not a whole one), a "
                    "compressed short story (too much material for the count), a vignette (a situation "
                    "with no move), or a prose poem (an image with no story). Explain in 2-3 sentences.\n"
                    "2. THE COMPLETENESS TEST: does this piece stand alone? State what a reader would "
                    "still be waiting for at the end, and whether that waiting is the effect or a "
                    "failure.\n"
                    "3. THE MOVE CHECK: confirm something changes - a situation, an understanding, a "
                    "relationship, a fact. If nothing does, name the smallest change I could add.\n"
                    "4. THE FRAGMENT FIX: if this is a fragment, tell me where the actual flash piece is "
                    "inside it. It is usually the last third.\n"
                    "5. THE TOO-MUCH FIX: if this is a compressed short story, name the single moment to "
                    "keep and tell me what the flash version of this idea is.\n"
                    "6. THE PROSE-POEM QUESTION: if it sits between flash and prose poetry, tell me which "
                    "it should be sold as and what would push it either way. Both are legitimate; the "
                    "markets are different.\n"
                    "7. THE SO-WHAT, EARLY: in one sentence, why a stranger should spend ninety seconds on "
                    "this. If the answer is thin, better to know now.\n"
                    "8. THREE SHARPER VERSIONS: three one-line alternatives that are definitely complete "
                    "pieces, using the same material.\n\n"
                    "End by asking me whether I would keep reading past the first line if a stranger had "
                    "written this, because in flash that is the entire test."
                ),
                "pro_tip": (
                    "Item 4 is the most common rescue in the form. When a flash draft feels unfinished, "
                    "the finished piece is usually the final third with the setup deleted - try reading "
                    "from two thirds in and see whether it stands."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: BUILD IT",
        "intro": (
            "Three prompts for the three things flash actually needs: a person the reader gets in one "
            "sentence, a title that is part of the text, and one detail that carries a world. Note that "
            "the title prompt is not cosmetic - in this form it is a structural component."
        ),
        "prompts": [
            {
                "title": "The Character in a Sentence",
                "desc": (
                    "No paragraph, no description, no history. This prompt builds a person a reader knows "
                    "from a single sentence of behaviour."
                ),
                "prompt_text": (
                    "You are a flash fiction editor teaching characterisation at extreme compression.\n\n"
                    "My form, count and what it holds: [PASTE FROM PROMPT 1]\n"
                    "My one thing and its type: [PASTE FROM PROMPT 2]\n"
                    "My rough character idea: [DESCRIBE, or say 'you choose']\n\n"
                    "Do the following, staying inside the character limit my count allows:\n\n"
                    "1. THE CHARACTER SENTENCE: write the single sentence that delivers this person - "
                    "doing something specific that implies everything else. Not 'she was tired and "
                    "forty-three'. Something she does.\n"
                    "2. FIVE ALTERNATIVES: five other character sentences for the same person, each "
                    "implying a slightly different life. Mark the one that implies the most with the "
                    "fewest words.\n"
                    "3. THE IMPLICATION AUDIT: for your recommended sentence, list what a reader can now "
                    "infer - age, class, situation, state of mind, history. If the list is short, the "
                    "sentence is not working hard enough.\n"
                    "4. THE NAME DECISION: whether this character should be named at all. At under 300 "
                    "words a name often costs more than it gives - recommend named, unnamed, or a role "
                    "('the driver', 'my sister'), and say why for my count.\n"
                    "5. THE SECOND CHARACTER QUESTION: whether my count can afford one. If yes, their "
                    "single sentence and their one function. If no, say so plainly and tell me how to "
                    "deliver their effect through absence, reference or dialogue.\n"
                    "6. THE WANT: what this character wants inside these few hundred words, concrete "
                    "enough to be visible in one action.\n"
                    "7. WHAT WE NEVER LEARN: 4 things deliberately withheld. In flash this is the "
                    "majority of the character and it is the point.\n"
                    "8. THE BEHAVIOUR BANK: 4 specific actions this person could perform that would "
                    "reveal them. I will use one.\n\n"
                    "End by asking me whether the reader needs to like this person, because at this length "
                    "there is no room to earn it back."
                ),
                "pro_tip": (
                    "Item 4 catches people out. Under 300 words, 'the woman with the keys' often lands "
                    "harder than a name, because a name asks the reader to remember something while an "
                    "epithet does work every time it appears."
                ),
            },
            {
                "title": "The Title as Part of the Story",
                "desc": (
                    "In flash the title is a line of the text, frequently the one carrying the most "
                    "meaning. This prompt writes it as a structural component rather than a label."
                ),
                "prompt_text": (
                    "You are a flash fiction editor who judges a piece partly on whether its title is "
                    "doing work.\n\n"
                    "My one thing and its type: [PASTE FROM PROMPT 2]\n"
                    "My form and count: [PASTE FROM PROMPT 1]\n"
                    "My character sentence: [PASTE FROM PROMPT 4]\n"
                    "My draft or premise: [PASTE]\n\n"
                    "Do the following:\n\n"
                    "1. THE TITLE'S JOB: in flash a title can do one of several jobs. Explain each and "
                    "say which suits my piece:\n"
                    "   - CONTEXT: supplying the situation so the prose does not have to (a date, a place, "
                    "a relationship, an occasion)\n"
                    "   - FRAME: telling the reader what kind of document they are reading\n"
                    "   - IRONY: sitting against the content so the gap creates the meaning\n"
                    "   - THE MISSING PIECE: supplying the fact the prose withholds, so the piece only "
                    "resolves when the reader looks back at the title\n"
                    "   - FIRST LINE: functioning as the opening clause, with the text continuing from it\n"
                    "2. EIGHT TITLES: write eight candidates across those jobs. For each, state its job "
                    "and what the prose then no longer needs to say.\n"
                    "3. THE WORD SAVINGS: for your top three, state precisely how many words of prose each "
                    "title makes unnecessary. At this length that is real currency.\n"
                    "4. THE LABEL PURGE: identify any of my candidates that merely label - 'The Visit', "
                    "'Goodbye', 'The Letter' - and discard them with a reason.\n"
                    "5. THE LONG TITLE OPTION: write one deliberately long title, since a long title on a "
                    "very short piece is a recognised flash move. Say whether it suits mine.\n"
                    "6. THE COUNT QUESTION: remind me whether my form counts the title, and note this "
                    "varies by market and must be checked - it can be the difference between a valid and "
                    "invalid drabble.\n"
                    "7. THE TITLE-LAST TEST: for your recommended title, confirm the piece reads "
                    "differently when a reader returns to it after the last line. If it does not, it is "
                    "not yet earning its place.\n\n"
                    "End by asking me whether my title gives something away that should be withheld, "
                    "because the title is read first and cannot be un-read."
                ),
                "pro_tip": (
                    "The Missing Piece is the strongest title job in flash and the most under-used. Put "
                    "the one fact the prose refuses to state into the title, and the reader completes the "
                    "story themselves at the moment they look back."
                ),
            },
            {
                "title": "The One Detail",
                "desc": (
                    "Flash has room for one concrete specific to carry the entire world. This prompt finds "
                    "the right one and forbids the second."
                ),
                "prompt_text": (
                    "You are a flash fiction editor who knows that one exact detail outperforms three "
                    "approximate ones.\n\n"
                    "My one thing and genre: [PASTE FROM PROMPTS 1-2]\n"
                    "My character sentence: [PASTE FROM PROMPT 4]\n"
                    "My count limits: [FROM PROMPT 1 ITEM 3]\n\n"
                    "Do the following:\n\n"
                    "1. THE DETAIL CANDIDATES: eight specific, concrete details that could carry this "
                    "piece's world - an object, a brand, a smell, a sound, a piece of clothing, a price, a "
                    "piece of institutional language, a measurement. For each, state what a reader would "
                    "infer from it.\n"
                    "2. THE CHOICE: recommend one, or two if my count permits, and explain why those imply "
                    "the most. Then forbid the others explicitly.\n"
                    "3. THE INFERENCE CHAIN: for your recommended detail, trace what the reader deduces - "
                    "the era, the class, the region, the situation, the character's state. This chain is "
                    "what the detail is buying.\n"
                    "4. THE GENRE DETAIL: if my genre needs a world signalled - speculative, historical, "
                    "science fiction, horror - name the one detail that establishes it without "
                    "explanation, and give me the sentence containing it. One unexplained noun used "
                    "casually does what a paragraph cannot.\n"
                    "5. THE RECURRENCE: whether this detail should appear once or twice. Twice - once "
                    "neutral, once at the turn - is the strongest structure available in the form.\n"
                    "6. THE SENSE CHOICE: which single sense this piece works in. Flash that tries all "
                    "five gets none of them.\n"
                    "7. THE CUT LIST: every piece of setting, description or world detail I am tempted to "
                    "include and must not. Be aggressive.\n"
                    "8. THE PRECISION UPGRADE: take my chosen detail and make it three degrees more "
                    "specific. Show each degree, so I can see what precision buys.\n\n"
                    "End by asking me which detail is true, from my own life or observation, because those "
                    "are the ones that land and cannot be invented."
                ),
                "pro_tip": (
                    "Item 5 is the cheapest structure in flash. One object mentioned casually early and "
                    "again at the last line does the work of an entire arc, and costs you perhaps eight "
                    "words."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: SHAPE IT",
        "intro": (
            "Three prompts on form. Flash borrows its shapes from things that are not stories, and its "
            "last line usually carries the whole piece - so this phase covers the structures, the opening "
            "fifteen words, and the ending, in that order of difficulty."
        ),
        "prompts": [
            {
                "title": "Flash Structures",
                "desc": (
                    "The shapes flash actually uses - most of them borrowed from documents rather than "
                    "from fiction. This prompt picks yours."
                ),
                "prompt_text": (
                    "You are a flash fiction editor who has seen every structure the form uses.\n\n"
                    "My one thing and its type: [PASTE FROM PROMPT 2]\n"
                    "My form, count and genre: [PASTE FROM PROMPT 1]\n"
                    "My character sentence, title and detail: [PASTE FROM PROMPTS 4-6]\n\n"
                    "Do the following:\n\n"
                    "1. THE STRUCTURE OPTIONS: describe these shapes, with the count and one-thing type "
                    "each suits:\n"
                    "   - THE SINGLE IMAGE: one moment held, described precisely, meaning arriving last\n"
                    "   - THE TWO-BEAT: a thing happens, then a second thing reframes it\n"
                    "   - THE LIST: numbered or unnumbered items that accumulate into a story\n"
                    "   - THE BORROWED FORM: a recipe, an instruction manual, a form, a set of rules, an "
                    "obituary, a classified ad, a set of directions\n"
                    "   - THE MONOLOGUE: one voice, talking, revealing more than it intends\n"
                    "   - THE CATALOGUE OF A LIFE: compressed time, a sequence of years in a few "
                    "sentences\n"
                    "   - THE REVEAL: the situation withheld until the last line recontextualises it\n"
                    "   - THE REPETITION: one sentence pattern repeated with variation\n"
                    "2. THE RECOMMENDATION: pick the one that fits my one thing and count, and defend it. "
                    "Then name the shape I was probably going to default to and say why it is weaker here.\n"
                    "3. THE SHAPE'S RULES: the 3 rules my chosen shape imposes, and where it collapses.\n"
                    "4. THE BORROWED-FORM OPTION: whether my piece would be stronger written as a "
                    "non-story document. Propose a specific one - the form, the recipe, the rules, the "
                    "review - and give me its opening two lines so I can judge.\n"
                    "5. THE MOVES, PLACED: take my two or three moves from Prompt 2 and place them inside "
                    "this structure, with an approximate word position for each.\n"
                    "6. THE POV AND TENSE: recommend both for this shape and count, and state what each "
                    "alternative would cost. Then confirm one temporal position with no flashbacks.\n"
                    "7. THE WHITE SPACE: whether this piece uses paragraph breaks, section breaks, or is "
                    "a single unbroken block, and what each choice signals.\n"
                    "8. THE FAILURE MODE: how pieces in my chosen shape most often fail, with the early "
                    "warning sign.\n\n"
                    "End by asking me whether I have read a piece in this shape that I admired, because "
                    "borrowed structures are best learned from one good example."
                ),
                "pro_tip": (
                    "The Borrowed Form is where flash is most alive and least crowded. A story told as a "
                    "set of assembly instructions or a lost-property notice gives you structure for free "
                    "and a voice you could not have invented directly."
                ),
            },
            {
                "title": "The First Fifteen Words",
                "desc": (
                    "In flash the opening is not a page or a paragraph - it is a clause. This prompt "
                    "builds it, and proves there is no room for setup."
                ),
                "prompt_text": (
                    "You are a flash fiction first reader who decides within one line.\n\n"
                    "My structure and its rules: [PASTE FROM PROMPT 7]\n"
                    "My title and its job: [PASTE FROM PROMPT 5]\n"
                    "My character sentence and detail: [PASTE FROM PROMPTS 4 AND 6]\n"
                    "My count: [FROM PROMPT 1]\n\n"
                    "Do the following:\n\n"
                    "1. THE FIRST LINE: write it. The reader must already be inside the situation. No "
                    "setup, no weather, no waking, no scene-setting, no establishing clause.\n"
                    "2. SIX ALTERNATIVES: six more first lines, each using a different strategy - a "
                    "statement of fact, a voice, an action mid-motion, a strange juxtaposition, a piece of "
                    "dialogue, a number or measurement. Say what each promises.\n"
                    "3. THE INFORMATION AUDIT: for your recommended line, list what a reader knows after "
                    "it. Then list what they are curious about. Both lists should be non-empty.\n"
                    "4. THE TITLE HANDOFF: confirm the first line works WITH the title rather than "
                    "repeating it. If the title supplies the context, the first line must not supply it "
                    "again - that is a wasted line.\n"
                    "5. THE SETUP PURGE: identify anything in my draft opening that is setup, and show me "
                    "where the piece should actually begin. At this length the correct answer is usually "
                    "the second or third sentence of whatever I wrote.\n"
                    "6. THE FIRST FIFTY WORDS: extend your recommended opening to fifty words, and confirm "
                    "something has already changed or been revealed by then.\n"
                    "7. THE PROPORTION CHECK: state what percentage of my total count the opening should "
                    "occupy, scaled to my form. At 100 words it is one sentence; at 1,000 it might be "
                    "three.\n"
                    "8. THE GENRE SIGNAL: confirm a reader of my genre knows what kind of piece this is by "
                    "the end of the first line.\n\n"
                    "End by asking me what my current first sentence is doing that the title could do "
                    "instead, because that swap buys words I do not have."
                ),
                "pro_tip": (
                    "Item 5 is the note to apply mechanically. Delete your first sentence, read from the "
                    "second, and check whether anything was lost. In flash the answer is no far more often "
                    "than any writer expects."
                ),
            },
            {
                "title": "The Last Line",
                "desc": (
                    "In flash the last line usually IS the turn, which is why you write backwards from it. "
                    "This prompt builds it and tests whether it lands or merely stops."
                ),
                "prompt_text": (
                    "You are a flash fiction editor who judges a piece almost entirely on its final "
                    "line.\n\n"
                    "My one thing and its type: [PASTE FROM PROMPT 2]\n"
                    "My structure: [PASTE FROM PROMPT 7]\n"
                    "My title and its job: [PASTE FROM PROMPT 5]\n"
                    "My recurring detail: [FROM PROMPT 6]\n\n"
                    "Do the following:\n\n"
                    "1. THE LAST LINE: write it. It should deliver the one thing rather than describe it.\n"
                    "2. SIX ALTERNATIVES: six candidates using different mechanisms - the withheld fact "
                    "arriving, the detail recurring, an action taken, a line of dialogue, a shift in "
                    "tense or distance, a plain statement. For each, say what it makes the piece mean.\n"
                    "3. THE VERDICT PER CANDIDATE: for each, classify it as LANDS (reframes what came "
                    "before), STOPS (just ends), EXPLAINS (tells the reader what to think), or JOKES (a "
                    "punchline that closes the piece down). Discard everything that is not LANDS, unless "
                    "my genre wants a punchline and I say so.\n"
                    "4. THE TITLE LOOP: confirm the last line sends the reader back to the title. If it "
                    "does not, propose the version that does.\n"
                    "5. THE DETAIL RETURN: if my recurring detail from Prompt 6 should appear here, show "
                    "me the version where it does.\n"
                    "6. THE ONE-WORD-SHORTER TEST: take your recommended line and cut it by a word, then "
                    "by two. Show all three. Flash endings are usually one word too long.\n"
                    "7. THE STOP POINT: identify the sentence after which I must stop writing, and confirm "
                    "there is nothing after it explaining anything.\n"
                    "8. THE REREAD TEST: name 2 things a reader will read differently on a second pass. If "
                    "you cannot find two, the ending is thin - say so.\n\n"
                    "End by asking me whether I am withholding a fact or delivering a meaning, because "
                    "only the second one survives a second reading."
                ),
                "pro_tip": (
                    "Item 6 is a real technique, not a gimmick. Flash endings almost always land harder a "
                    "word or two shorter - trim the final clause to its bone and the silence afterwards "
                    "does the rest."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: WRITE IT",
        "intro": (
            "Three prompts, and a flash piece takes about twenty minutes to draft. The real work is the "
            "two passes after: cutting to an exact count, then reading it aloud - because at this length "
            "rhythm is most of the effect."
        ),
        "prompts": [
            {
                "title": "The Draft",
                "desc": (
                    "The whole piece in one pass, from everything locked in Phases 1 to 3. Deliberately "
                    "written over count, because you will cut in the next prompt."
                ),
                "prompt_text": (
                    "You are my drafting partner on a flash fiction piece. You write in my voice and hand "
                    "control back at the end.\n\n"
                    "CONTEXT:\n"
                    "- My form, exact count and genre: [PASTE FROM PROMPT 1]\n"
                    "- My one thing, its type and my two or three moves: [PASTE FROM PROMPT 2]\n"
                    "- My character sentence and what is withheld: [PASTE FROM PROMPT 4]\n"
                    "- My title and its job: [PASTE FROM PROMPT 5]\n"
                    "- My one detail and whether it recurs: [PASTE FROM PROMPT 6]\n"
                    "- My structure, POV, tense and white space plan: [PASTE FROM PROMPT 7]\n"
                    "- My first line: [PASTE FROM PROMPT 8]\n"
                    "- My last line: [PASTE FROM PROMPT 9]\n"
                    "- My voice notes: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET, PLUS ANY NOTES "
                    "ON YOUR OWN STYLE]\n\n"
                    "Write the piece, following these rules:\n\n"
                    "1. Draft at roughly 130 percent of my target count. I will cut in the next prompt, "
                    "and cutting produces a better piece than writing to length.\n"
                    "2. Open on my approved first line and close on my approved last line.\n"
                    "3. Hold my structure, POV and tense. No flashbacks.\n"
                    "4. Use only my one detail and my named characters. No new world, no new people.\n"
                    "5. Make every sentence carry at least two of: character, situation, image, tone, "
                    "turn.\n"
                    "6. No filtering verbs, no named emotions, no backstory, no explanation.\n"
                    "7. Vary sentence length hard.\n\n"
                    "After the piece, give me: the word count, a note on which of my moves landed and "
                    "which did not, anything in my plan that fought the writing, and the three sentences "
                    "you think are weakest.\n\n"
                    "Then write ONE alternative version of the middle section, taking a different route "
                    "between my first and last lines, so I can compare.\n\n"
                    "End by asking me which version's middle I prefer, and why, so the compression pass "
                    "knows what to protect."
                ),
                "pro_tip": (
                    "Drafting long on purpose is the counter-intuitive move that works. A 400-word piece "
                    "cut down from 520 is consistently better than one written to 400, because the cutting "
                    "is where the density comes from."
                ),
            },
            {
                "title": "Compression to Exact Count",
                "desc": (
                    "The heart of the form. This prompt cuts to your target - and where the form demands "
                    "an exact number, hits it precisely."
                ),
                "prompt_text": (
                    "You are a line editor compressing a flash piece to an exact word count. You are "
                    "ruthless and you count accurately.\n\n"
                    "My draft: [PASTE IT]\n"
                    "My current count and my exact target: [STATE BOTH]\n"
                    "Whether the title counts: [FROM PROMPT 1 ITEM 2]\n"
                    "My one thing: [FROM PROMPT 2]\n\n"
                    "Do the following:\n\n"
                    "1. THE COUNT: state my actual current count and how many words must go.\n"
                    "2. THE FAT MAP: where the excess sits. In flash it is nearly always the opening, "
                    "dialogue tags, stage business, and any sentence containing 'that', 'just', 'really', "
                    "'began to', 'started to', or 'was able to'.\n"
                    "3. THE FREE WORDS: every instance of the words above and their kin. Cut them all and "
                    "report the saving - this alone often covers half the gap.\n"
                    "4. THE SENTENCE COMPRESSIONS: every sentence that can lose words with no loss of "
                    "meaning. Give me original, compressed, and words saved for each.\n"
                    "5. THE MERGE PASS: pairs of sentences that can become one doing both jobs.\n"
                    "6. THE STAGE BUSINESS: every standing, sitting, turning, looking, reaching, walking "
                    "across. Cut all that is not meaningful.\n"
                    "7. THE TAG PURGE: every dialogue tag the line does not need.\n"
                    "8. THE TITLE TRANSFER: anything in the prose the title could carry instead. In flash "
                    "this is the highest-value trade available.\n"
                    "9. THE STRUCTURAL CUT: if sentence work is not enough, name the move, sentence or "
                    "section to remove entirely, and confirm the one thing survives without it.\n"
                    "10. THE EXACT LANDING: if my form requires an exact count, get me to it precisely. "
                    "Show the final tally, and if we are one or two words out, give me two options for "
                    "each direction. Never pad to reach a count - cut elsewhere and rephrase.\n"
                    "11. THE FINAL COUNT: state it and confirm it matches my target exactly.\n\n"
                    "Return the cuts as a list with running totals. Then give me the final compressed "
                    "piece in full, since at this length I need to see it whole.\n\n"
                    "End by asking me which cut I want to reverse, so we can find those words somewhere "
                    "else."
                ),
                "pro_tip": (
                    "Item 8 wins drabbles. When you are three words over an exact count, move a fact into "
                    "the title rather than hunting for adjectives - the title is usually free, and the "
                    "piece gets stronger rather than merely shorter."
                ),
            },
            {
                "title": "The Read-Aloud and Rhythm Pass",
                "desc": (
                    "At this length rhythm is the structure. This pass fixes what the eye misses and the "
                    "ear catches immediately."
                ),
                "prompt_text": (
                    "You are a line editor working on the sound of a flash piece. You know that at this "
                    "length rhythm does the work structure does in longer forms.\n\n"
                    "My compressed piece: [PASTE IT]\n"
                    "My one thing and its type: [FROM PROMPT 2]\n"
                    "My voice notes: [PASTE FROM THIS PACK'S CHEAT SHEET]\n\n"
                    "Do the following:\n\n"
                    "1. THE SENTENCE LENGTH MAP: list the word count of every sentence in order. Then tell "
                    "me where the rhythm is flat - three similar-length sentences in a row - and what to "
                    "do about it.\n"
                    "2. THE SHORT SENTENCE PLACEMENT: identify where a very short sentence would land "
                    "hardest. Usually immediately before or after the turn. Show me the rewrite.\n"
                    "3. THE MOUTHFEEL PASS: every phrase that is hard to say aloud - consonant clusters, "
                    "accidental rhymes, repeated sounds, tongue-twisters. Flag and fix.\n"
                    "4. THE LAST-LINE RHYTHM: read the final line aloud several ways. Tell me whether it "
                    "ends on a stressed or unstressed syllable and which would land better here. At this "
                    "length the final syllable genuinely matters.\n"
                    "5. THE FIRST-LINE RHYTHM: the same for the opening, which sets the piece's whole "
                    "cadence.\n"
                    "6. THE REPETITION CHECK: any word repeated within earshot of itself, excluding "
                    "deliberate motifs. At 300 words a repeat two sentences apart is audible.\n"
                    "7. THE PARAGRAPH SHAPE: how this piece looks on a page, and whether the visual "
                    "shape supports it. Flash is read partly as an object.\n"
                    "8. THE BREATH TEST: mark where a reader would naturally pause, and whether the "
                    "punctuation agrees.\n"
                    "9. THE KEEP LIST: the 3 sentences working best, so I do not edit them away.\n\n"
                    "Return everything as a list - original, proposed, reason. Then confirm the word count "
                    "has not changed, or tell me by how much it has.\n\n"
                    "End by asking me to read it aloud myself and report which sentence I stumbled on, "
                    "because that is the one to fix."
                ),
                "pro_tip": (
                    "Actually read it out loud, every time, before submitting. Flash is close enough to "
                    "poetry that the ear catches in one pass what the eye misses in six - and it takes "
                    "ninety seconds."
                ),
            },
        ],
    },

    {
        "name": "PHASE 5: FINISH AND SEND",
        "intro": (
            "Four prompts to close out: the craft audit, the resonance test that decides whether the piece "
            "lingers, the flash market and contest ecosystem, and a volume practice - because in this form "
            "the writers who place work are the ones producing steadily."
        ),
        "prompts": [
            {
                "title": "The Craft Audit",
                "desc": (
                    "The technical pass, tuned to the failures specific to very short fiction rather than "
                    "to stories in general."
                ),
                "prompt_text": (
                    "You are a flash fiction first reader listing the technical reasons a piece gets "
                    "rejected.\n\n"
                    "My form, exact count and genre expectations: [PASTE FROM PROMPT 1]\n"
                    "My one thing: [FROM PROMPT 2]\n"
                    "My level spec: [PASTE THE LEVEL SPEC FROM THIS PACK'S CHEAT SHEET]\n"
                    "My piece: [PASTE IT]\n\n"
                    "Audit and cite the location for each issue:\n\n"
                    "1. THE COUNT: confirm the exact count and whether it meets my form's requirement. If "
                    "my form has a fixed number and I am out by one, that is a CRITICAL finding.\n"
                    "2. THE SETUP CHECK: any words spent establishing rather than moving. At this length "
                    "this is the number one rejection cause.\n"
                    "3. POV AND TENSE: any slip, any flashback, any shift in temporal position.\n"
                    "4. FILTERING AND NAMED EMOTIONS: every instance. There should be none.\n"
                    "5. THE EXPLANATION SWEEP: any sentence telling the reader what to understand, "
                    "especially in the last third.\n"
                    "6. THE CHARACTER COUNT: more named people than my count can support, per my level "
                    "spec.\n"
                    "7. THE DETAIL COUNT: more world detail than my count allows. Flag the second and "
                    "third details if my count only affords one.\n"
                    "8. THE TITLE AUDIT: is my title doing a job from Prompt 5, or labelling? Is it giving "
                    "away something that should be withheld?\n"
                    "9. THE GENRE CHECK: the piece against my genre's three flash expectations and two "
                    "rejection triggers from Prompt 1 item 4.\n"
                    "10. THE FIRST-LINE RE-READ: read only the first line and tell me whether an editor "
                    "reading three hundred submissions continues. Answer honestly.\n"
                    "11. THE COMPLETENESS RE-CHECK: confirm this is a whole piece and not a fragment, per "
                    "Prompt 3.\n"
                    "12. FORMATTING: standard prose submission conventions, and anything that would mark "
                    "this as amateur - noting that each market's guidelines override the default.\n\n"
                    "Rank findings CRITICAL, MODERATE or MINOR, with a fix for every CRITICAL.\n\n"
                    "End by asking me which finding I disagree with, because in a piece this short every "
                    "disagreement is worth examining."
                ),
                "pro_tip": (
                    "Item 1 is not a formality. Markets running exact-count forms check, and a 101-word "
                    "drabble is rejected unread - which is the cheapest rejection to avoid in all of "
                    "writing."
                ),
            },
            {
                "title": "The Resonance Test",
                "desc": (
                    "The final judgement. Flash is judged on whether it stays with a reader after ninety "
                    "seconds, and this prompt decides honestly whether yours does."
                ),
                "prompt_text": (
                    "You are a flash fiction editor deciding whether to accept a piece. Be honest rather "
                    "than kind.\n\n"
                    "My one thing and its type: [PASTE FROM PROMPT 2]\n"
                    "My genre and form: [FROM PROMPT 1]\n"
                    "My finished piece: [PASTE IT]\n\n"
                    "Do the following:\n\n"
                    "1. THE ONE-THING VERDICT: does this piece deliver the one thing I designed it for? "
                    "Answer plainly, and if not, say where it fails.\n"
                    "2. THE LINGER TEST: what will a reader still be holding in five minutes? If the "
                    "answer is 'the twist' rather than an image, a recognition or a feeling, the piece is "
                    "a trick and will be read once - say so.\n"
                    "3. THE IMPLICATION AUDIT: list everything a reader infers that the piece does not "
                    "state. This list is the actual size of the story. If it is short, the piece is only "
                    "as big as its word count and that is the problem.\n"
                    "4. THE SECOND-READ VALUE: what changes on a reread. Flash lives or dies here.\n"
                    "5. THE AMBIGUITY SPLIT: separate deliberately open from simply unclear. At this "
                    "length readers have no room to recover from confusion.\n"
                    "6. THE SO-WHAT: one sentence on why a stranger should spend ninety seconds here.\n"
                    "7. THE COMPARISON VERDICT: against the kind of flash that gets published in my "
                    "genre, does this compete? Answer as an editor, not a friend.\n"
                    "8. THE TWO-MINUTE FIXES: the three changes with the highest improvement per unit of "
                    "effort.\n"
                    "9. THE LIKELY REJECTION REASON: if this were rejected, what it would be for. Answer "
                    "as the person rejecting it.\n"
                    "10. THE VERDICT: submit as is, one more pass, or set aside and write the next one. "
                    "Pick one.\n\n"
                    "End by asking me whether I would remember this piece if a stranger had written it, "
                    "which is the only test in this form."
                ),
                "pro_tip": (
                    "Item 3 is the real measure of a flash piece. Count the inferences - a 300-word story "
                    "that produces twenty is enormous, and one that produces three is 300 words long and "
                    "nothing more."
                ),
            },
            {
                "title": "Flash Markets, Contests and Exact-Count Calls",
                "desc": (
                    "Where flash goes, which is a different ecosystem from short story markets - faster, "
                    "more numerous, and full of hard word ceilings."
                ),
                "prompt_text": (
                    "You are a submissions strategist who specialises in flash fiction. You explain "
                    "principles rather than naming markets, since guidelines, counts and reading periods "
                    "change constantly.\n\n"
                    "My form, exact count and genre: [PASTE FROM PROMPT 1]\n"
                    "My finished piece and its verdict: [PASTE FROM PROMPT 14]\n\n"
                    "Do the following:\n\n"
                    "1. THE ECOSYSTEM: explain how flash markets differ from short story markets - volume, "
                    "response times, payment norms, how many pieces they take, and why the acceptance "
                    "maths is different.\n"
                    "2. THE MARKET PROFILE: describe the kinds of venue this specific piece suits - by "
                    "count ceiling, genre, tone, payment tier and register - so I can find current ones "
                    "myself in a market database.\n"
                    "3. THE COUNT CEILING RULE: explain why flash markets enforce their limits absolutely, "
                    "and how to decide whether to cut a piece to fit a ceiling or find a different venue. "
                    "Then tell me which is right for mine.\n"
                    "4. THE EXACT-COUNT CALLS: how to approach venues and contests that require a precise "
                    "number - the drabble markets, the fifty-word calls, the themed exact-count "
                    "anthologies - and why these are among the most winnable because most entrants get the "
                    "count wrong.\n"
                    "5. THE MULTIPLE SUBMISSION QUESTION: how flash differs here, since many venues accept "
                    "several pieces at once. Explain the convention and the etiquette.\n"
                    "6. THE CONTEST LANDSCAPE: how to judge a flash contest worth entering, what entry "
                    "fees are reasonable against the prize, and why themed contests with tight counts are "
                    "good value for a writer with a body of work.\n"
                    "7. THE BATCH STRATEGY: how to submit flash in groups rather than singly, and the "
                    "tracking table to keep - piece, count, venue, date, outcome, next venue.\n"
                    "8. THE REPRINT QUESTION: how reprints work in flash, which is more permissive than "
                    "longer fiction, and what a piece can do after its first publication.\n"
                    "9. THE SOCIAL AND MICRO VENUES: the trade-offs of publishing very short work on "
                    "public platforms, and what it costs in first rights.\n\n"
                    "End by asking me how many finished pieces I currently have, because flash strategy is "
                    "a volume strategy and one piece is not a strategy."
                ),
                "pro_tip": (
                    "Item 4 is the genuine opportunity. Exact-count calls disqualify a large share of "
                    "entrants on the count alone - if you can reliably land on 100 words, you are "
                    "competing against a much smaller field than the submission numbers suggest."
                ),
            },
            {
                "title": "Volume, Practice and Collecting Flash",
                "desc": (
                    "Flash is the only fiction form where you can finish something before dinner. This "
                    "prompt builds the practice that turns that into a body of work."
                ),
                "prompt_text": (
                    "You are a writing coach who uses flash fiction as both a form and a training "
                    "method.\n\n"
                    "My finished piece, its form and what it does well: [PASTE FROM PROMPTS 1-2 AND 14]\n"
                    "My verdict and likely rejection reason: [PASTE FROM PROMPT 14]\n"
                    "What I want from flash: [PUBLICATION, PRACTICE, A COLLECTION, MATERIAL FOR A "
                    "NEWSLETTER, OR SOMETHING ELSE]\n\n"
                    "Do the following:\n\n"
                    "1. WHAT THIS PIECE TAUGHT ME: the specific skill it demonstrates and the specific "
                    "weakness it exposed.\n"
                    "2. THE NEXT PIECE: what to attack next. Name a specific constraint - a different "
                    "structure from Prompt 7, a shorter count, a borrowed form, a genre I have not tried, "
                    "a single-sentence piece.\n"
                    "3. THE TEN-PIECE PLAN: ten one-line prompts for my own next ten pieces, each "
                    "targeting a different skill, ordered easiest to hardest.\n"
                    "4. THE CONSTRAINT LADDER: how to use decreasing word counts as deliberate practice - "
                    "write it at 1,000, then at 500, then at 100, and what each cut teaches.\n"
                    "5. THE PRACTICE RHYTHM: a realistic working pattern for someone with limited time, "
                    "given that a flash piece can be drafted in twenty minutes. Include how to keep pieces "
                    "in circulation while drafting new ones.\n"
                    "6. THE FLASH-AS-TRAINING ARGUMENT: what flash teaches that transfers to longer forms "
                    "- opening lines, compression, trusting the reader, endings - and the one thing it will "
                    "not teach me.\n"
                    "7. THE COLLECTION PATH: how many pieces a flash collection needs, what makes a set of "
                    "very short pieces cohere into a book rather than a pile, and how flash collections "
                    "differ from short story collections in ordering and pacing.\n"
                    "8. THE UNIFYING PRINCIPLE: three candidates for what could bind my collection, based "
                    "on this piece - a setting, a form, a recurring image, a single question, a voice.\n"
                    "9. THE SEED CHECK: whether anything in this piece wants to be longer - a character, a "
                    "world, a premise - and whether to resist that or follow it.\n\n"
                    "End by asking me what I am afraid I cannot write in under a thousand words, because "
                    "that is exactly what the next piece should be."
                ),
                "pro_tip": (
                    "Item 4 is the best deliberate practice in prose. Write the same piece at 1,000, then "
                    "500, then 100 words. The 100-word version is usually the best one, and what you "
                    "learn cutting to it changes how you write everything else."
                ),
            },
        ],
    },
]
