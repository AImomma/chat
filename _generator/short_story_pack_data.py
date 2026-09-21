# -*- coding: utf-8 -*-
"""
Royalti Studios - Short Story Master Prompt Pack (Adult Fiction Line).

GENRE-GENERAL by design. Prompt 1 is a genre-and-form lock that routes the rest
of the pack. Short story craft is genre-independent in a way novel craft is not:
single effect, late entry, compression, the turn, an ending that lands. Genre
changes the furniture, not the engine.

Distinct from the catalog's planned "Short Story Collection" entry, which is
about assembling and selling a collection rather than writing one story.

Build with:
    python pack_builder.py short_story_pack_data \
        "Short_Story_Master_Prompt_Pack_v1.0.pdf"

VERSIONING POLICY: v1.0 is the first release. Any amendment archives the old
PDF and a snapshot of this file into versions/, bumps the version
(+0.1 content fix, +1.0 restructure), and logs the change in CHANGELOG.md.

PROMPT COUNT: 20, below the 22 baseline. Approved by the user on 2026-09-21.
Reasons: no subplot architecture, no chapter plan, no series runway, no
multi-batch drafting - a short story is drafted in one pass.
"""

DATA = {
    # ---------- COVER ----------
    "genre_title": "SHORT STORY",
    "total_prompts": 20,
    "hook_line": "One effect, one turn, entered late and left early - the hardest form to pad and the fastest one to master.",
    "keyword_lines": [
        "Any genre • Single effect • Late entry • Compression • The turn",
        "Literary • Horror • Romance • Sci-fi • Fantasy • Crime • Speculative • Slipstream",
    ],
    "subgenres_line": "Lengths: Flash (under 1,000), Short Short (1,000-2,500), Standard Short Story (2,500-7,500), Long Short Story (7,500-12,000), Novelette (12,000-17,500)",
    "brand_name": "Royalti Studios",
    "version": "1.0",
    "version_date": "2026-09-21",
    "audience_line": "Adult Fiction Line",
    "cover_h2": "From One Idea to a Submittable Story",
    "closing_tagline": "A novel can survive a weak chapter. A short story cannot survive a weak paragraph.",

    # ---------- HOW TO USE ----------
    "how_to_use_intro": (
        "This pack is deliberately genre-general, because short story craft is. Whether you are writing "
        "literary, horror, romance, science fiction, crime or something between, the machinery is the same: "
        "one effect, one turn, entered as late as possible and left before the reader is finished with it. "
        "Genre changes the furniture, not the engine. So Prompt 1 locks your genre AND your target length, "
        "and every later prompt inherits both - the structure prompts will offer you shapes that fit your "
        "length, and the craft prompts will apply your genre's specific expectations. Work in order and "
        "keep every output in one document. By Prompt 20 you have a finished, submittable story plus the "
        "materials to send it out with."
    ),
    "phase_summaries": [
        "Phase 1 (Prompts 1-4) - Find the story. Lock genre and length, name the single effect the story "
        "exists to produce, test honestly whether what you have is a story at all, and decide where it is "
        "going before you write it.",
        "Phase 2 (Prompts 5-7) - Build the situation. A character established in a paragraph rather than a "
        "history, the latest possible point of entry, and a world built from three details instead of "
        "three pages.",
        "Phase 3 (Prompts 8-11) - Structure it. Choose from the shapes short fiction actually uses, budget "
        "your words scene by scene, design the turn, and build an ending that lands rather than stops.",
        "Phase 4 (Prompts 12-14) - Write it. The opening paragraph - the highest-leverage hundred words in "
        "the form - then the whole draft in one pass, then a compression pass that cuts it hard.",
        "Phase 5 (Prompts 15-17) - Revise. A line-level voice pass, a craft audit for the technical "
        "failures editors reject on, and the so-what test that decides whether the story is finished.",
        "Phase 6 (Prompts 18-20) - Send it out. Market fit and a submission strategy, the cover letter and "
        "bio, and the plan for the next story and the eventual collection.",
    ],
    "placeholder_note": (
        "What you need: Any AI chat tool and a place to save your outputs between prompts. Brackets like "
        "[THIS] are placeholders - replace them with your content from previous prompts."
    ),
    "skip_note": (
        "Skip what doesn't apply - the system is modular, and Prompt 1 tells you which prompts your length "
        "needs. Writing flash under 1,000 words? Prompt 9 collapses to a single paragraph plan and Prompt "
        "14 becomes the most important prompt in the pack. Writing a novelette? Prompt 9 does real work "
        "and you may need two drafting passes rather than one."
    ),

    # ---------- CHEAT SHEET ----------
    "cheat_sheet": {
        "makes": [
            "One effect - the single feeling or understanding the whole story is engineered to deliver",
            "Entry as late as possible; the story starts at the last moment it can still make sense",
            "A character the reader knows from one paragraph of behaviour, not a page of history",
            "Compression: every sentence doing at least two jobs - character and plot, setting and mood",
            "A turn the reader did not see and cannot dismiss, built from information they already had",
            "An ending that lands - the last line reframes rather than summarises",
            "Setting built from three specific details and left at that",
            "Exit before the reader is finished; a short story should end slightly too early",
            "Genre expectations met precisely, then one of them subverted on purpose",
            "A title that does work the prose then does not have to",
        ],
        "kills": [
            "A compressed novel - three settings, a subplot, five years and a cast of eight in 5,000 words",
            "Starting with waking up, weather, travel, or a character alone thinking about their situation",
            "Backstory front-loaded because the writer needed it and assumed the reader does",
            "An ending that stops rather than ends, on the assumption that ambiguity reads as depth",
            "A twist that withholds information rather than recontextualising it",
            "Two protagonists, because there is only room to make the reader care about one",
            "Dialogue used to deliver exposition to the reader through a character who already knows it",
            "A theme stated - in the last line, by a wise secondary character, or in a closing reflection",
            "Padding disguised as voice: an opening page of beautiful prose about nothing happening",
            "Submitting the first draft, which in this form is almost always fifteen percent too long",
        ],
        "voice": [
            "Concrete nouns over abstractions; in this form a named object outperforms a described feeling",
            "One point of view, one tense, held without slipping - editors reject on this alone",
            "Cut filtering: she saw, he felt, it seemed, she noticed - go straight to the thing",
            "Vary sentence length deliberately; a three-word sentence after a long one is the form's best tool",
            "Let the reader do the arithmetic - imply rather than explain, and trust the gap",
            "Dialogue carries character, not information; people talk around what they want",
            "Paragraph breaks are pacing, and white space is free emphasis",
            "Earn one beautiful sentence per thousand words and do not spend it in the first paragraph",
        ],
        "formula": (
            "THE SINGLE EFFECT (decided first) -> Entry at the Latest Possible Moment -> The Character "
            "Revealed in Behaviour -> The Want, Concrete and Visible -> The Situation Tightens -> The "
            "Complication (it is worse or stranger than it looked) -> THE TURN (reversal, revelation, or "
            "decision - exactly one) -> The Consequence, Enacted -> The Last Line, Reframing"
        ),
        "reader_expectations": (
            "Short story readers are the most practised readers in fiction, and the first person to read "
            "yours is usually an editor with a hundred more in the queue. They make a decision in the first "
            "paragraph and a second one at the end of page one. They are reading for a story that could not "
            "be any other length - one that uses compression as a tool rather than suffering it as a "
            "constraint. They expect a single clear point of view held without slipping, a want they can "
            "name by the end of page one, and an ending that changes the meaning of what came before. They "
            "will forgive a small subject and never forgive a padded one. Genre readers additionally expect "
            "their genre's promises met - the scare, the resolution, the wonder, the connection - inside "
            "the word count, which is precisely what makes genre short fiction hard and worth doing."
        ),
    },

    # ---------- FINAL WORDS ----------
    "final_words": (
        "The short story is the only form where you can hold the whole thing in your head at once, which "
        "means it is the only form where every choice is visible. That is what makes it uncomfortable and "
        "what makes it the fastest way to get better. You chose a single effect in Prompt 2 and everything "
        "since has been a matter of removing what does not serve it. When a draft feels flat, do not add - "
        "check three things: are you entering too early, is the turn earned or merely withheld, and does "
        "the last line reframe or summarise. Then cut fifteen percent. It is almost always in there, and "
        "the story is almost always better without it. Write the next one before this one comes back."
    ),

    "phases": [],
}


DATA["phases"] = [

    {
        "name": "PHASE 1: FIND THE STORY",
        "intro": (
            "Four prompts to establish what you are actually writing. Prompt 1 locks genre and length and "
            "routes the rest of the pack, so do not skip it. Prompt 3 will tell you honestly if what you "
            "have is an anecdote rather than a story, which is worth knowing before you spend three "
            "thousand words on it."
        ),
        "prompts": [
            {
                "title": "The Genre and Form Lock",
                "desc": (
                    "This pack is genre-general, and this prompt is how it becomes yours. It locks the "
                    "genre and target length, then tells you what both of those obligate for the rest of "
                    "the pack."
                ),
                "prompt_text": (
                    "You are a short fiction editor who has read for literary and genre magazines and "
                    "knows the demands of each.\n\n"
                    "My idea is: [DESCRIBE IN 2-5 SENTENCES - or say 'I have no idea yet, here is what I "
                    "want to write about']\n"
                    "My genre, if I know it: [NAME IT, OR SAY 'YOU TELL ME']\n\n"
                    "Do the following:\n\n"
                    "1. THE GENRE LOCK: name my genre precisely - literary, horror, romance, science "
                    "fiction, fantasy, crime or mystery, speculative, slipstream, humour, historical, or "
                    "something else. If my idea sits between two, say which one it should be sold as and "
                    "which is the flavour.\n"
                    "2. THE GENRE CONTRACT: state the 5 things a reader of this specific genre expects a "
                    "short story in it to deliver, and the 3 things that will get it rejected by an editor "
                    "in that genre specifically. Be concrete - this list is what my later craft audit "
                    "checks against.\n"
                    "3. THE GENRE'S SHORT-FORM PROBLEM: every genre has one thing that is hard to do in "
                    "few words - a mystery needs fair clues, horror needs dread, romance needs a "
                    "believable connection, science fiction needs a world. Name mine and tell me how short "
                    "fiction in my genre usually solves it.\n"
                    "4. THE LENGTH LOCK: recommend a target word count from - flash (under 1,000), short "
                    "short (1,000-2,500), standard (2,500-7,500), long short story (7,500-12,000), "
                    "novelette (12,000-17,500). Justify it against my idea, and tell me what my idea can "
                    "and cannot support.\n"
                    "5. WHAT THE LENGTH ALLOWS: for my chosen length, state plainly how many characters, "
                    "how many scenes, how many locations and how much time this story can hold. Write these "
                    "as limits.\n"
                    "6. THE GENRE FURNITURE: 8 elements a reader of my genre will recognise and enjoy - "
                    "the props, settings, situations and moves that signal I know the form. Then name the 4 "
                    "that are so overused I should avoid them.\n"
                    "7. THE ROUTING NOTE: tell me which prompts in this pack matter most for my genre and "
                    "length, and which will be a light pass.\n\n"
                    "End by asking me whether I am writing this story for a market or for myself, because "
                    "the answer changes how strictly I should meet the genre contract."
                ),
                "pro_tip": (
                    "Save items 2 and 6 somewhere you can see them. The genre contract is what your craft "
                    "audit in Prompt 16 checks against, and the overused list is what separates a story an "
                    "editor has read four times this month from one they have not."
                ),
            },
            {
                "title": "The Single Effect",
                "desc": (
                    "A short story is engineered to do one thing to a reader. This prompt names that thing "
                    "so every later choice can be measured against it."
                ),
                "prompt_text": (
                    "You are a short fiction editor who believes a story should be built backwards from "
                    "the feeling it leaves behind.\n\n"
                    "My genre, length and idea: [PASTE FROM PROMPT 1]\n\n"
                    "Do the following:\n\n"
                    "1. THE SINGLE EFFECT: state in one sentence the one thing this story should do to a "
                    "reader by its last line - a feeling, a recognition, a dread, a grief, a delight, a "
                    "discomfort. Not a theme and not a moral. The effect.\n"
                    "2. FOUR ALTERNATIVES: four other effects this same material could produce, and what "
                    "kind of story each would make. Say which is the least obvious.\n"
                    "3. THE EFFECT TEST: for my chosen effect, name the 4 things a reader must be made to "
                    "feel or understand along the way for it to land. These become my scene requirements - "
                    "anything in the story not serving one of them is a candidate for cutting.\n"
                    "4. THE DELIVERY MECHANISM: how the effect arrives - through a revelation, a decision, "
                    "an image, a juxtaposition, a withheld detail finally given, or a line of dialogue. "
                    "Recommend one for my genre.\n"
                    "5. THE ANTI-EFFECT: name the feeling I might accidentally produce instead - "
                    "confusion, boredom, cleverness, sentimentality, contempt - and the specific warning "
                    "sign for each in my drafting.\n"
                    "6. THE ONE-SENTENCE STORY: write my story as a single sentence that contains the "
                    "effect. This is my compass while drafting.\n"
                    "7. THE TITLE CANDIDATES: 6 titles, and note which ones do work the prose then does "
                    "not have to.\n\n"
                    "End by asking me whether I have ever felt the effect I am aiming for, and where, "
                    "because a borrowed effect reads as borrowed."
                ),
                "pro_tip": (
                    "Item 3 is the list to print. Short stories fail by accumulation - a scene that is "
                    "merely good, a paragraph that is merely nice - and that four-item list is the only "
                    "defence against it."
                ),
            },
            {
                "title": "Is This Actually a Story?",
                "desc": (
                    "The prompt that saves you three thousand wasted words. Many short story ideas are "
                    "anecdotes, situations, or novels - this tells you which you have."
                ),
                "prompt_text": (
                    "You are a short fiction editor who reads slush and is direct about what is not a "
                    "story.\n\n"
                    "My idea, genre, length and single effect: [PASTE FROM PROMPTS 1-2]\n\n"
                    "Do the following:\n\n"
                    "1. THE DIAGNOSIS: tell me plainly which of these I have - a story, an anecdote "
                    "(something happened but nothing changed), a situation (a state of affairs with no "
                    "event), a character sketch, a premise (a world with no story in it yet), or a novel "
                    "compressed. Explain in 3-4 sentences.\n"
                    "2. THE FIX: if it is not a story, tell me specifically what to add or find. Usually "
                    "one of - a want, an obstacle, a decision, a cost, or a change. Name which is missing.\n"
                    "3. THE CHANGE TEST: state what is different at the end of this story from the "
                    "beginning. If the answer is only that the reader knows more, that is a problem in most "
                    "genres - tell me whether it is a problem in mine.\n"
                    "4. THE WANT: name what my protagonist wants, concretely and visibly, and confirm a "
                    "reader could state it by the end of page one. If it is abstract, give me the object or "
                    "action that stands in for it.\n"
                    "5. THE NOVEL TEST: is there a novel trying to happen here? If so, name the short "
                    "story inside it - the single hour or single scene that carries the same effect.\n"
                    "6. THE SO-WHAT, EARLY: answer now, in one sentence, why a stranger should spend "
                    "twenty minutes on this. If the answer is thin, better to know at Prompt 3 than at "
                    "Prompt 17.\n"
                    "7. THE FIVE SHARPER VERSIONS: five one-sentence alternatives, each a real story, "
                    "using the same material. Say which you would read.\n\n"
                    "End by asking me which of the sharper versions made me defensive, because that is "
                    "usually the one closest to what I actually want to write."
                ),
                "pro_tip": (
                    "Take the diagnosis at face value even when it stings. An anecdote can be rescued by "
                    "adding a decision; a situation can be rescued by adding a want. Both are ten-minute "
                    "fixes at this stage and unfixable at draft stage."
                ),
            },
            {
                "title": "Reader Promise and Where This Goes",
                "desc": (
                    "Deciding the destination before you write changes the writing. This prompt sets the "
                    "reader promise and the target market or purpose."
                ),
                "prompt_text": (
                    "You are a short fiction strategist who understands magazine, contest and "
                    "self-publishing routes for short stories.\n\n"
                    "My genre, length, effect and story: [PASTE FROM PROMPTS 1-3]\n\n"
                    "Do the following:\n\n"
                    "1. THE READER PROMISE: one paragraph in the second person ('You will feel...').\n"
                    "2. THE DESTINATION: recommend where this story should go, from - a genre magazine, a "
                    "literary magazine, a contest, an anthology call, a reader magnet or newsletter piece, "
                    "a collection I am building, or a serial platform. Give me the strongest two and say "
                    "what each requires of the story.\n"
                    "3. THE LENGTH CONSEQUENCE: tell me how my target market's preferred word count "
                    "compares to my length lock from Prompt 1, and whether to adjust. Many markets have "
                    "hard ceilings - explain the principle rather than naming specific magazines, since "
                    "their guidelines change.\n"
                    "4. THE CONTENT CONSIDERATIONS: anything in my story that will narrow where it can go "
                    "- explicit content, extreme violence, subject matter some markets avoid - stated "
                    "neutrally so I can decide rather than discover.\n"
                    "5. THE OPENING-PAGE STANDARD: given my destination, what the first page has to do. "
                    "Be specific about how much time I get before a first reader stops.\n"
                    "6. THE THREE PROMISES: the promises I must not break given this genre and "
                    "destination, and what breaking each would cost.\n"
                    "7. THE COMPARISON SET: 4 kinds of short story that occupy similar ground - describe "
                    "the type of story rather than naming titles - and what each does that mine will be "
                    "measured against.\n"
                    "8. THE ORIGINALITY CHECK: the 4 most familiar elements in my idea, with one specific "
                    "way to make each mine.\n\n"
                    "End by asking me what I want to happen after someone reads this, because that governs "
                    "how the last line should work."
                ),
                "pro_tip": (
                    "Decide the destination now, not after the draft. A story written for a contest, a "
                    "genre magazine and a reader magnet are three different stories at the sentence level, "
                    "and retrofitting one into another rarely works."
                ),
            },
        ],
    },

    {
        "name": "PHASE 2: BUILD THE SITUATION",
        "intro": (
            "Three prompts and you have everything the story needs to stand on: a person the reader knows "
            "from a paragraph, the latest possible place to begin, and a world implied rather than "
            "described."
        ),
        "prompts": [
            {
                "title": "The Character in a Paragraph",
                "desc": (
                    "Short fiction has no room for a history and does not need one. This prompt builds "
                    "people a reader understands from behaviour inside the first page."
                ),
                "prompt_text": (
                    "You are a short fiction editor teaching characterisation under severe word "
                    "constraints.\n\n"
                    "My genre, length limits and what the length allows: [PASTE FROM PROMPT 1]\n"
                    "My single effect and its requirements: [PASTE FROM PROMPT 2]\n"
                    "My want from the change test: [PASTE FROM PROMPT 3]\n"
                    "My rough character idea: [DESCRIBE, or say 'you choose']\n\n"
                    "Do the following, staying inside the character count my length allows:\n\n"
                    "1. THE PROTAGONIST: name, age, and the one behaviour that tells a reader who they are "
                    "in their first hundred words. The behaviour, not the biography.\n"
                    "2. THE FIVE BEHAVIOURS: five specific, observable actions that reveal this person "
                    "without a word of backstory - how they handle an object, a delay, a stranger, money, "
                    "a question they do not want to answer.\n"
                    "3. THE WANT IN THIS STORY: not their life goal. What they want inside these few "
                    "thousand words, stated concretely.\n"
                    "4. THE FLAW THAT COSTS THEM: a flaw that will actually cause a problem in the plot. "
                    "Name it and name the moment it bites.\n"
                    "5. THE CONTRADICTION: the one inconsistency that makes them a person rather than a "
                    "function.\n"
                    "6. THE OTHER CHARACTERS: for each remaining character my length permits - who they "
                    "are, their single function, and the one detail that stops them being a device. If any "
                    "exists only to receive exposition, tell me to cut them.\n"
                    "7. WHAT WE NEVER LEARN: 5 things about my protagonist the story deliberately withholds. "
                    "This restraint is what makes short fiction feel larger than its word count.\n"
                    "8. THE INTRODUCTION SENTENCE: write the actual sentence that introduces my "
                    "protagonist, as it will appear in the story - doing character, situation and voice at "
                    "once.\n\n"
                    "End by asking me whether my protagonist changes or is revealed, because at this length "
                    "most stories do the second and pretend to the first."
                ),
                "pro_tip": (
                    "Item 7 is counter-intuitive and correct. The characters who stay with readers after a "
                    "short story are the ones where a whole life was implied and never shown - every fact "
                    "you add closes that space."
                ),
            },
            {
                "title": "The Moment of Entry",
                "desc": (
                    "Where to start is the single most consequential decision in short fiction. This "
                    "prompt finds the latest possible point that still makes sense."
                ),
                "prompt_text": (
                    "You are a short fiction editor who rejects most submissions on the first page, "
                    "usually because they began too early.\n\n"
                    "My story, character and want: [PASTE FROM PROMPTS 3 AND 5]\n"
                    "My single effect: [FROM PROMPT 2]\n"
                    "My genre and length: [FROM PROMPT 1]\n\n"
                    "Do the following:\n\n"
                    "1. THE LATEST POSSIBLE ENTRY: identify the last moment this story could begin and "
                    "still be comprehensible. Describe that moment in a paragraph. It is almost certainly "
                    "later than I think.\n"
                    "2. FOUR ENTRY POINTS: four candidate opening moments, from earliest to latest, and "
                    "what each costs and gains. Then recommend one.\n"
                    "3. WHAT THE READER NEEDS BY PAGE ONE: the specific facts a reader must have to follow "
                    "the story - and, crucially, how each can be delivered inside action rather than before "
                    "it.\n"
                    "4. THE BACKSTORY BUDGET: how many words of history this length can afford, where they "
                    "belong, and the 3 pieces of backstory I think I need that I do not. Be strict.\n"
                    "5. THE FORBIDDEN OPENINGS: confirm which of the standard bad openings my draft is "
                    "drifting toward - waking up, weather, travel, a mirror, a character alone thinking, "
                    "dialogue with no context, a prologue of world-explanation - and what to replace it "
                    "with.\n"
                    "6. THE FIRST-LINE OPTIONS: 6 candidate first lines, each doing a different job - "
                    "situation, voice, image, disturbance, question, statement of fact. Say which suits my "
                    "genre.\n"
                    "7. THE IN MEDIAS RES CHECK: if I start in the middle, what the reader will be "
                    "confused about, and the minimum I must give them to prevent confusion becoming "
                    "abandonment.\n\n"
                    "End by asking me what happens in the first three hundred words, because if the answer "
                    "is 'setup', we have not started late enough."
                ),
                "pro_tip": (
                    "Whatever entry point you choose, try cutting your first two paragraphs after drafting "
                    "and reading from paragraph three. It works far more often than anyone expects, and "
                    "the information you lose was almost never load-bearing."
                ),
            },
            {
                "title": "The World in Three Details",
                "desc": (
                    "Setting in short fiction is built from implication. This prompt gives you the few "
                    "specifics that do the work of pages - handled according to your genre's demands."
                ),
                "prompt_text": (
                    "You are a short fiction editor who specialises in economical setting and world "
                    "delivery.\n\n"
                    "My genre and its short-form problem: [PASTE FROM PROMPT 1]\n"
                    "My character and entry point: [PASTE FROM PROMPTS 5-6]\n"
                    "My length and what it allows: [FROM PROMPT 1]\n\n"
                    "Do the following:\n\n"
                    "1. THE PLACE: where this story happens, in one paragraph of concrete detail - what is "
                    "in it, what it smells like, what the light does, what is worn or broken.\n"
                    "2. THE THREE DETAILS: from that paragraph, select the three specifics that will "
                    "actually appear in the story and carry the whole setting. Say why those three.\n"
                    "3. THE GENRE DELIVERY: if my genre requires a built world - science fiction, fantasy, "
                    "historical, speculative - tell me how to deliver it at this length. Cover the specific "
                    "techniques: the telling detail, the unexplained noun used in context, the "
                    "consequence shown before the cause, the character who takes it for granted. Give me "
                    "5 sentences of sample prose demonstrating the method.\n"
                    "4. THE NO-EXPLANATION RULE: for my genre, state exactly what I am allowed to explain "
                    "and what must be inferred. Then name the one thing a reader genuinely cannot work out "
                    "for themselves and will need given plainly.\n"
                    "5. THE SENSORY ANCHOR: one sound, one smell and one texture that recur, so the place "
                    "stays present without re-description.\n"
                    "6. THE TIME AND SCALE: when this happens and over how long. Confirm the span fits my "
                    "length - a story spanning years at 4,000 words is usually a novel in hiding.\n"
                    "7. THE OBJECT: one physical object that carries meaning and can recur. In short "
                    "fiction a single object does more than any amount of description.\n"
                    "8. THE CUT LIST: what worldbuilding I have in mind that must not appear. Be "
                    "aggressive - this is where genre short fiction most often bloats.\n\n"
                    "End by asking me what I most want to explain, because that is almost always the thing "
                    "to leave out."
                ),
                "pro_tip": (
                    "Item 7 is the cheapest depth available in the form. One object handled twice - once "
                    "casually, once at the turn - will do more for a 4,000-word story than a page of "
                    "beautiful setting."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 3: STRUCTURE IT",
        "intro": (
            "Four prompts on shape. Short fiction does not use three acts - it uses a smaller set of forms "
            "that fit its length. Pick the right one, budget your words, design the turn, and build an "
            "ending that reframes rather than summarises."
        ),
        "prompts": [
            {
                "title": "The Short Story Shapes",
                "desc": (
                    "Three-act structure is a novel and screenplay tool. This prompt picks the shape that "
                    "actually fits your length, genre and effect."
                ),
                "prompt_text": (
                    "You are a structure specialist in short fiction who does not default to three acts.\n\n"
                    "My genre, length and effect: [PASTE FROM PROMPTS 1-2]\n"
                    "My character, want and entry point: [PASTE FROM PROMPTS 5-6]\n\n"
                    "Do the following:\n\n"
                    "1. THE SHAPE OPTIONS: describe 7 shapes short fiction actually uses, with the length "
                    "and genre each suits:\n"
                    "   - The Single Scene (one continuous scene, real time, pressure to a break)\n"
                    "   - The Two-Scene Hinge (a scene, a gap, a second scene that reframes the first)\n"
                    "   - The Escalating Sequence (the same action three or four times, changed each time)\n"
                    "   - The Frame (a present-tense situation containing a remembered one)\n"
                    "   - The Braid (two threads alternating, converging at the turn)\n"
                    "   - The Accumulation (a series of fragments or vignettes building one effect)\n"
                    "   - The Journey (a character moves through a short span and is changed by what they "
                    "meet)\n"
                    "2. THE RECOMMENDATION: pick the one that best fits my material and defend it. Then "
                    "name the shape I was probably about to use by default and say why it is worse here.\n"
                    "3. THE SHAPE'S RULES: for my chosen shape, the 4 rules it imposes - what must happen "
                    "by what point, what it cannot tolerate, where it collapses.\n"
                    "4. THE SCENE COUNT: how many scenes a story of my length and shape should have. Give "
                    "a number and warn me what happens above it.\n"
                    "5. THE GENRE FIT: whether this shape serves my genre's expectations from Prompt 1 "
                    "item 2, and any adjustment needed.\n"
                    "6. THE POV AND TENSE DECISION: recommend point of view and tense for this shape, "
                    "genre and effect - first or third, past or present, and how close the psychic "
                    "distance should be. Justify it, and name what each alternative would cost.\n"
                    "7. THE FAILURE MODE: the specific way stories of my chosen shape fall apart, with the "
                    "early warning sign in my own draft.\n\n"
                    "End by asking me whether I want the reader ahead of my protagonist, behind them, or "
                    "level with them, because that choice governs the whole structure."
                ),
                "pro_tip": (
                    "The Two-Scene Hinge is the most reliable shape in the form and the least attempted. "
                    "A scene, a white-space gap, then a second scene that makes the first mean something "
                    "different - it delivers a turn without needing a twist."
                ),
            },
            {
                "title": "The Word Budget",
                "desc": (
                    "This prompt allocates your word count scene by scene before you draft, so you know "
                    "what each has to do and how much room it gets."
                ),
                "prompt_text": (
                    "You are a short fiction editor allocating word count before a draft.\n\n"
                    "My shape and scene count: [PASTE FROM PROMPT 8]\n"
                    "My effect requirements - the four things a reader must feel: [PASTE FROM PROMPT 2 "
                    "ITEM 3]\n"
                    "My entry point: [FROM PROMPT 6]\n"
                    "My target word count: [FROM PROMPT 1]\n\n"
                    "Build my WORD BUDGET. For each scene or section:\n\n"
                    "1. Its number, and where and when it happens.\n"
                    "2. Word allocation, and the running total.\n"
                    "3. Who is present.\n"
                    "4. The scene's job in one sentence - and which of my four effect requirements it "
                    "serves. A scene serving none is a candidate for cutting.\n"
                    "5. The turn: what is different at the end of the scene than at the start.\n"
                    "6. How it gets out - the last beat and how it hands to the next.\n\n"
                    "Then give me:\n"
                    "7. THE CUT LIST: any scene not serving an effect requirement, or with no turn, or "
                    "duplicating another's job.\n"
                    "8. THE BUDGET AUDIT: whether allocations total my target, and which scene I have "
                    "over-funded. In short fiction the middle is almost always too fat.\n"
                    "9. THE OPENING ALLOCATION: how many words the opening gets before something must "
                    "happen. Be strict, and scale it to my length - flash gets a sentence, a novelette "
                    "gets a page.\n"
                    "10. THE WHITE SPACE PLAN: where a section break does work that transitional prose "
                    "would otherwise have to. Breaks are free and most writers under-use them.\n"
                    "11. THE ENTRY CHECK: for each scene, whether I am starting it too early. Most should "
                    "begin a beat or two later than instinct suggests.\n\n"
                    "End by asking me which scene I am most attached to, so we can check whether the story "
                    "needs it."
                ),
                "pro_tip": (
                    "Item 10 is the most under-used tool in the form. A section break can carry a week, a "
                    "change of mind or a death - and it costs zero words, which at 4,000 is the whole game."
                ),
            },
            {
                "title": "The Turn",
                "desc": (
                    "Every short story delivers one reversal. This prompt designs it, places it, and "
                    "separates an earned turn from withheld information."
                ),
                "prompt_text": (
                    "You are a short fiction editor who specialises in the single reversal at the heart of "
                    "a story.\n\n"
                    "My effect and its delivery mechanism: [PASTE FROM PROMPT 2]\n"
                    "My word budget: [PASTE FROM PROMPT 9]\n"
                    "My genre contract: [FROM PROMPT 1 ITEM 2]\n\n"
                    "Do the following:\n\n"
                    "1. THE TURN: state in two sentences the one reversal this story delivers - a "
                    "revelation, a decision, a refusal, a recognition, or a change of understanding. "
                    "Exactly one.\n"
                    "2. THE PLACEMENT: which scene and roughly which word count it lands on. Then tell me "
                    "whether that is too early or too late for my shape and length.\n"
                    "3. EARNED VERSUS WITHHELD: state plainly whether my turn works because the reader had "
                    "everything and still did not see it, or because I hid something. If it is the second, "
                    "say so and help me fix it - withheld turns read as tricks and do not survive a second "
                    "reading.\n"
                    "4. THE PLANTS: 5 details to seed earlier that read as innocent first time and "
                    "inevitable second time. Say which scene each belongs in, using my word budget.\n"
                    "5. THE MISDIRECTION: what the reader believes instead, and the honest reason they "
                    "believe it. Misdirection is true information pointed the wrong way, never a lie.\n"
                    "6. THE COST: what the turn costs my protagonist. A reversal with no cost is a plot "
                    "event rather than a story.\n"
                    "7. THE GENRE-SPECIFIC CHECK: for my genre, the particular standard a turn must meet - "
                    "fair clueing in mystery, escalation in horror, emotional inevitability in romance, "
                    "conceptual consistency in science fiction. Audit my turn against mine.\n"
                    "8. THE AFTERMATH BUDGET: how many words should remain after the turn. Warn me about "
                    "both failure modes - ending so abruptly the turn cannot be felt, and explaining it for "
                    "three paragraphs afterwards.\n"
                    "9. THE REREAD TEST: 3 things that will read differently on a second pass. If you "
                    "cannot find three, my turn is thin - say so.\n\n"
                    "End by asking me whether my protagonist understands the turn or only the reader does, "
                    "because those are two different stories."
                ),
                "pro_tip": (
                    "Item 3 is the line between a story and a gimmick, and the test is simple: could a "
                    "sharp reader have worked it out from what you gave them? If not, you hid something "
                    "rather than built a reversal."
                ),
            },
            {
                "title": "The Ending That Lands",
                "desc": (
                    "The difference between an ending and a stopping. This prompt builds the last lines - "
                    "the part of a short story readers actually remember."
                ),
                "prompt_text": (
                    "You are a short fiction editor who believes a story is judged on its last "
                    "paragraph.\n\n"
                    "My single effect: [PASTE FROM PROMPT 2]\n"
                    "My turn and its aftermath budget: [PASTE FROM PROMPT 10]\n"
                    "My genre contract: [FROM PROMPT 1]\n"
                    "My protagonist's want: [FROM PROMPT 5]\n\n"
                    "Do the following:\n\n"
                    "1. THE ENDING TYPES: describe the endings short fiction actually uses - the resonant "
                    "image, the decision enacted, the line of dialogue, the reframing statement, the "
                    "deliberate cut mid-motion, the return to the opening image changed. Say which suit my "
                    "genre and effect.\n"
                    "2. THE RECOMMENDATION: pick one and write my final paragraph. Then write two "
                    "alternatives using different types, so I can compare.\n"
                    "3. THE LAST LINE: 5 candidate final lines. For each, say whether it reframes, "
                    "summarises, or explains - and cut the ones that summarise or explain.\n"
                    "4. THE WANT RESOLUTION: state whether my protagonist gets what they wanted, and "
                    "whether the reader should feel that as a win, a loss, or something more complicated. "
                    "Check it against my genre contract - some genres require the want answered.\n"
                    "5. THE STOP-VERSUS-END TEST: for each candidate ending, whether it ends the story or "
                    "merely stops it. Be strict; ambiguity is only earned when everything except the "
                    "withheld thing is clear.\n"
                    "6. THE OPENING RHYME: how the ending relates to my first line from Prompt 6. If there "
                    "is no relationship, propose one.\n"
                    "7. THE EXIT-EARLY CHECK: identify the sentence after which I should stop. Short "
                    "stories should end slightly before the reader is ready - find my over-run.\n"
                    "8. THE EFFECT CONFIRMATION: state whether this ending delivers the single effect from "
                    "Prompt 2. If not, the problem is the ending, not the effect - say which to change.\n\n"
                    "End by asking me what I want the reader to do in the ten seconds after the last line, "
                    "because that is what the ending is actually for."
                ),
                "pro_tip": (
                    "Item 7 is the highest-value note here. Nearly every short story draft has one "
                    "paragraph too many at the end - find the sentence that lands and delete everything "
                    "after it."
                ),
            },
        ],
    },

    {
        "name": "PHASE 4: WRITE IT",
        "intro": (
            "Three prompts and you have a story. The opening paragraph first, because it is the highest-"
            "leverage hundred words in the form. Then the whole draft in one pass - the advantage of short "
            "fiction is that it all fits in your head. Then cut it hard."
        ),
        "prompts": [
            {
                "title": "The Opening Paragraph",
                "desc": (
                    "Editors decide in the first paragraph. This prompt drafts it properly, several ways, "
                    "before the rest of the story commits to a voice."
                ),
                "prompt_text": (
                    "You are a short fiction writer and first reader who knows that the opening paragraph "
                    "makes the decision.\n\n"
                    "My genre and its contract: [PASTE FROM PROMPT 1]\n"
                    "My entry point and first-line candidates: [PASTE FROM PROMPT 6]\n"
                    "My protagonist and their introduction sentence: [PASTE FROM PROMPT 5]\n"
                    "My three setting details: [PASTE FROM PROMPT 7]\n"
                    "My POV and tense: [FROM PROMPT 8 ITEM 6]\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET, PLUS NOTES "
                    "ON YOUR OWN STYLE]\n\n"
                    "Do the following:\n\n"
                    "1. THE OPENING PARAGRAPH: write it. It must establish voice, a person, a situation, "
                    "and something already in motion. No weather, no waking, no mirror, no reflection on a "
                    "state of affairs.\n"
                    "2. THREE ALTERNATIVES: three more versions using different first-line strategies from "
                    "Prompt 6 item 6 - one leading with voice, one with image, one with disturbance.\n"
                    "3. THE OPENING PAGE: extend the strongest version to roughly 300 words, hitting my "
                    "opening allocation from Prompt 9 item 9.\n"
                    "4. THE FIRST-PAGE AUDIT: for the version you recommend, list what a reader knows, "
                    "what they are curious about, and anything I explained that I should have implied.\n"
                    "5. THE GENRE SIGNAL: confirm a reader of my genre knows within the first three "
                    "sentences what kind of story this is. If not, say what to add.\n"
                    "6. THE VOICE SAMPLE: identify the 3 sentences that best define this story's voice, so "
                    "I have a reference for the rest of the draft.\n"
                    "7. THE PROMISE CHECK: what this opening promises the reader, and whether my plan "
                    "delivers it.\n\n"
                    "End by asking me whether an editor with a hundred submissions would read the second "
                    "paragraph, and which specific line makes them."
                ),
                "pro_tip": (
                    "Always generate the alternatives. The opening you would have written alone is almost "
                    "always the second-best of four, and comparing them side by side shows you that in a "
                    "way rereading one never does."
                ),
            },
            {
                "title": "The Draft",
                "desc": (
                    "Short fiction's real advantage: you can draft the whole thing in one pass with the "
                    "entire structure in view. This prompt writes it."
                ),
                "prompt_text": (
                    "You are my drafting partner on a short story. You write in my established voice and "
                    "hand control back to me at the end.\n\n"
                    "CONTEXT:\n"
                    "- My approved opening page and voice sample: [PASTE FROM PROMPT 12]\n"
                    "- My genre and its contract: [PASTE FROM PROMPT 1]\n"
                    "- My word budget, scene by scene: [PASTE FROM PROMPT 9]\n"
                    "- My character, behaviours and what is withheld: [PASTE FROM PROMPT 5]\n"
                    "- My three setting details and recurring object: [PASTE FROM PROMPT 7]\n"
                    "- My turn, its plants and placement: [PASTE FROM PROMPT 10]\n"
                    "- My ending and last line: [PASTE FROM PROMPT 11]\n"
                    "- POV and tense: [FROM PROMPT 8]\n"
                    "- Target word count: [FROM PROMPT 1]\n\n"
                    "Write the complete story, following these rules:\n\n"
                    "1. Match the voice sample in rhythm, sentence length and psychic distance.\n"
                    "2. Hold one POV and one tense throughout. No slips.\n"
                    "3. Hit the word allocations from my budget. If a scene wants to run long, cut "
                    "something else and tell me what.\n"
                    "4. Start every scene as late as possible, per my entry check.\n"
                    "5. Plant every item from Prompt 10 item 4 in its assigned scene, written to read as "
                    "incidental.\n"
                    "6. Use only my three setting details and the recurring object - no new worldbuilding.\n"
                    "7. No filtering verbs, no stated theme, no character explaining the situation to "
                    "someone who knows it.\n"
                    "8. Use section breaks where my white space plan calls for them.\n"
                    "9. End on my approved last line.\n\n"
                    "After the story, give me: the final word count, a per-scene breakdown against my "
                    "allocations, any rule you had to strain, and anything in my plan that did not work "
                    "once written.\n\n"
                    "End by asking me which scene fought back hardest, because that is usually where the "
                    "structure has a problem."
                ),
                "pro_tip": (
                    "Ask for the per-scene word breakdown every time. A story that comes in 800 words over "
                    "is not a trimming job - it usually means one scene is doing work the structure never "
                    "assigned it."
                ),
            },
            {
                "title": "The Compression Pass",
                "desc": (
                    "The prompt that makes the difference. Almost every short story draft is fifteen "
                    "percent too long, and the cut version is almost always better."
                ),
                "prompt_text": (
                    "You are a line editor doing a compression pass on a short story. Your instruction is "
                    "to cut fifteen percent without losing anything the story needs.\n\n"
                    "My draft: [PASTE IT]\n"
                    "My current and target word count: [STATE BOTH]\n"
                    "My single effect and its four requirements: [PASTE FROM PROMPT 2]\n\n"
                    "Do the following:\n\n"
                    "1. THE FAT MAP: identify where the excess is concentrated. Usually the opening, "
                    "transitions between scenes, dialogue tags and stage business, and the paragraph after "
                    "the turn.\n"
                    "2. THE OPENING CUT: try deleting my first paragraph, then my first two. Show me where "
                    "the story reads best from, and what information I would need to relocate.\n"
                    "3. THE SENTENCE-LEVEL CUTS: the 20 sentences that could lose words with no loss of "
                    "meaning. Give me original and compressed for each.\n"
                    "4. THE DOUBLE-DUTY REWRITES: 8 places where two sentences could become one that does "
                    "both jobs.\n"
                    "5. THE STAGE BUSINESS: every instance of characters standing, sitting, walking "
                    "across rooms, opening doors, picking up and putting down. Cut all that is not "
                    "meaningful.\n"
                    "6. THE DIALOGUE TAG PASS: replace every tag that is not 'said' or 'asked' unless it "
                    "earns itself, and cut every tag the dialogue does not need.\n"
                    "7. THE ADVERB AND FILTER SWEEP: every adverb propping a weak verb, and every "
                    "filtering construction - she saw, he felt, it seemed, she realised, he noticed.\n"
                    "8. THE SCENE-LEVEL CUT: if sentence work is not enough, name the scene or section to "
                    "cut entirely and what to relocate from it.\n"
                    "9. THE TRANSITION CUT: every transitional passage that could become a section break.\n"
                    "10. THE FINAL PARAGRAPH CHECK: find the sentence the story should end on, and show me "
                    "what to delete after it.\n"
                    "11. THE COUNT: report the new word count and confirm the fifteen percent.\n\n"
                    "Return the pass as a list - original, proposed, reason. Do not rewrite the whole "
                    "story.\n\n"
                    "End by asking me which cut I refuse to make, so we can check whether I am protecting "
                    "the story or my own writing."
                ),
                "pro_tip": (
                    "Do this pass even when you are already under your word count. The fifteen percent is "
                    "not about length - it is about density, and a story at 3,400 words that was 4,000 is "
                    "measurably better than one written to 3,400."
                ),
            },
        ],
    },
]


DATA["phases"] += [

    {
        "name": "PHASE 5: REVISE",
        "intro": (
            "Three prompts between a draft and a submittable story: a line-level voice pass, a craft audit "
            "against the technical failures editors reject on, and the so-what test that decides whether "
            "this is finished."
        ),
        "prompts": [
            {
                "title": "The Voice and Line Pass",
                "desc": (
                    "Sentence-level work, where short fiction is actually won. This pass sharpens the "
                    "prose without flattening it into competence."
                ),
                "prompt_text": (
                    "You are a line editor for short fiction. You sharpen a writer's voice rather than "
                    "replacing it with a neutral one.\n\n"
                    "My voice essentials: [PASTE THE VOICE LIST FROM THIS PACK'S CHEAT SHEET]\n"
                    "My voice sample - the three defining sentences: [PASTE FROM PROMPT 12 ITEM 6]\n"
                    "My compressed draft: [PASTE IT]\n\n"
                    "Do a line pass:\n\n"
                    "1. THE ABSTRACTION HUNT: every abstract noun where a concrete one would land harder. "
                    "Propose the specific replacement.\n"
                    "2. THE VERB PASS: weak verb-plus-adverb constructions replaced with one strong verb. "
                    "Give me the 15 highest-value swaps.\n"
                    "3. THE RHYTHM MAP: mark where sentence length does not match the moment - long "
                    "sentences at high tension, uniform length across a page. Rewrite one paragraph to "
                    "demonstrate.\n"
                    "4. THE PSYCHIC DISTANCE CHECK: mark any place the narration moves closer to or "
                    "further from the character than intended, and whether it was deliberate.\n"
                    "5. THE CLICHE SWEEP: every phrase I did not invent. Flag them and replace the worst "
                    "eight with something of mine.\n"
                    "6. THE BEAUTIFUL SENTENCE AUDIT: identify my attempts at fine writing. Keep the best "
                    "one per thousand words and cut the rest - unspent beauty reads as showing off.\n"
                    "7. THE REPETITION PASS: words, images and constructions I have used more than the "
                    "story can bear, excluding deliberate motifs.\n"
                    "8. THE DIALOGUE SPEAKABILITY: read every line as a person speaking. Flag the "
                    "unspeakable ones and give me the spoken version.\n"
                    "9. THE VOICE CONSISTENCY: any passage that does not sound like my voice sample. This "
                    "usually means a section I wrote on a different day.\n"
                    "10. THE KEEP LIST: name the 5 sentences that are working best, so I know what the "
                    "register is and do not edit them away.\n\n"
                    "Return everything as a list - original, proposed, one-line reason. Do not rewrite the "
                    "story.\n\n"
                    "End by asking me which of your changes I rejected, so you can calibrate to my voice "
                    "for the next pass."
                ),
                "pro_tip": (
                    "Item 10 matters as much as the cuts. Revision that only removes drifts toward "
                    "competent and grey - knowing which five sentences are yours protects the thing that "
                    "makes the story worth publishing."
                ),
            },
            {
                "title": "The Craft Audit",
                "desc": (
                    "The technical pass. These are the failures short fiction editors reject on before "
                    "they reach any judgement about the story itself."
                ),
                "prompt_text": (
                    "You are a short fiction first reader listing the technical reasons a story gets "
                    "rejected before an editor even considers its merits.\n\n"
                    "My genre contract and its three rejection triggers: [PASTE FROM PROMPT 1 ITEM 2]\n"
                    "My POV and tense decision: [PASTE FROM PROMPT 8 ITEM 6]\n"
                    "My single effect: [FROM PROMPT 2]\n"
                    "My revised draft: [PASTE IT]\n\n"
                    "Audit and cite the location for every issue:\n\n"
                    "1. POV SLIPS: every place the story enters a head it should not, or drifts to "
                    "omniscient, or tells us something the viewpoint character cannot know.\n"
                    "2. TENSE SLIPS: every inconsistency, including inside flashbacks and habitual "
                    "actions.\n"
                    "3. TELLING WHERE SHOWING IS NEEDED: emotions named rather than enacted. Give me the "
                    "eight worst with dramatised replacements. Then note where telling is correct and "
                    "efficient, because in short fiction it often is.\n"
                    "4. THE EXPOSITION SWEEP: information delivered to the reader rather than earned in "
                    "the scene - especially dialogue between characters who both already know.\n"
                    "5. THE BACKSTORY AUDIT: every passage of history, against my backstory budget from "
                    "Prompt 6 item 4. Flag anything over.\n"
                    "6. THE STATED THEME: any place the story explains itself - a closing reflection, a "
                    "wise secondary character, a line that tells the reader what to take away. Cut them "
                    "all.\n"
                    "7. THE CHARACTER COUNT: whether I have more named characters than my length can "
                    "support, and which to merge or unname.\n"
                    "8. THE TIMELINE: any inconsistency in sequence, duration or elapsed time.\n"
                    "9. THE GENRE CONTRACT AUDIT: check the story against each of my genre's five "
                    "expectations and three rejection triggers from Prompt 1. Name anything unmet.\n"
                    "10. THE FORMATTING AND MECHANICS: anything that would mark this as an amateur "
                    "submission - dialogue punctuation, em-dash and ellipsis use, section break markers, "
                    "paragraph indentation and spacing conventions for prose submission.\n"
                    "11. THE OPENING-PAGE RE-READ: read only the first page and tell me the three "
                    "strongest reasons an editor would stop there.\n\n"
                    "Rank findings CRITICAL, MODERATE or MINOR, with a fix for every CRITICAL.\n\n"
                    "End by asking me which critical fix requires restructuring, so I can plan that before "
                    "touching sentences."
                ),
                "pro_tip": (
                    "Item 1 is the most common rejection reason in short fiction and the easiest to miss "
                    "in your own work. A single sentence of head-hopping on page two is enough to end a "
                    "submission at a competitive market."
                ),
            },
            {
                "title": "The So-What Test",
                "desc": (
                    "The final judgement before it goes out. Does the story do the thing it was built to "
                    "do, and is it finished?"
                ),
                "prompt_text": (
                    "You are a short fiction editor deciding whether to accept a story. Be honest rather "
                    "than encouraging.\n\n"
                    "My single effect and its four requirements: [PASTE FROM PROMPT 2]\n"
                    "My genre and destination: [PASTE FROM PROMPTS 1 AND 4]\n"
                    "My story: [PASTE IT]\n\n"
                    "Do the following:\n\n"
                    "1. THE EFFECT VERDICT: does this story produce the effect I designed it for? Answer "
                    "plainly, and if not, say where it fails.\n"
                    "2. THE FOUR REQUIREMENTS: check each of my effect requirements from Prompt 2 item 3 "
                    "against the finished story. Name any that are unmet or under-delivered.\n"
                    "3. THE SO-WHAT: in one sentence, why a stranger should have spent twenty minutes on "
                    "this. If you cannot answer it, that is the note.\n"
                    "4. THE MEMORABLE ELEMENT: name the one thing a reader will remember in a week. If "
                    "there is nothing, the story is competent and will be rejected as such - say so.\n"
                    "5. THE FIRST-PARAGRAPH AND LAST-PARAGRAPH TEST: read only those two. Do they belong "
                    "to the same story, and does the last one reframe the first?\n"
                    "6. THE AMBIGUITY AUDIT: separate the places the story is deliberately open from the "
                    "places it is simply unclear. Readers cannot tell the difference and assume the second.\n"
                    "7. THE COMPARISON VERDICT: against the comparison set from Prompt 4 item 7, tell me "
                    "honestly whether this competes.\n"
                    "8. THE TWO-MINUTE FIXES: the three changes with the highest ratio of improvement to "
                    "effort.\n"
                    "9. THE HARD QUESTION: if this story were rejected, what would the most likely reason "
                    "be? Answer as the editor rejecting it.\n"
                    "10. THE VERDICT: submit as is, one more revision pass, or set aside and write the "
                    "next one. Pick one.\n\n"
                    "End by asking me whether I would keep reading this if a stranger had written it, "
                    "because that is the only test that matters."
                ),
                "pro_tip": (
                    "Item 10's third option is a real answer and not a failure. Setting a story aside and "
                    "writing the next one is how short fiction writers improve - some stories are how you "
                    "learned something rather than the thing you sell."
                ),
            },
        ],
    },

    {
        "name": "PHASE 6: SEND IT OUT",
        "intro": (
            "Three prompts to place it and keep going. Market fit and a submission strategy, the materials "
            "that go with it, and the plan that turns one story into a body of work."
        ),
        "prompts": [
            {
                "title": "Market Fit and Submission Strategy",
                "desc": (
                    "Where this story should go and in what order. Principles rather than named markets, "
                    "because guidelines and rates change constantly."
                ),
                "prompt_text": (
                    "You are a short fiction submissions strategist. You are realistic about acceptance "
                    "rates and you explain principles rather than naming specific markets, since their "
                    "guidelines, rates and reading periods change.\n\n"
                    "My genre, length and destination: [PASTE FROM PROMPTS 1 AND 4]\n"
                    "My finished story and its verdict: [PASTE FROM PROMPT 17]\n\n"
                    "Do the following:\n\n"
                    "1. THE HONEST ASSESSMENT: given this story's genre, length and quality, what tier of "
                    "market it realistically fits, and what the acceptance odds look like at each tier.\n"
                    "2. THE MARKET PROFILE: describe the kinds of market this story suits - by genre "
                    "focus, length preference, tone, payment tier and reputation - so I can go and find "
                    "them myself in a current market database rather than trusting a list that has aged.\n"
                    "3. THE SUBMISSION LADDER: how to order submissions. Explain the reasoning: start at "
                    "the top of what is plausible, work down, and why submitting to your dream market "
                    "first costs you nothing but time.\n"
                    "4. THE MECHANICS: how to think about simultaneous submissions, multiple submissions, "
                    "reprint rights versus first rights, response times, and when to query. Explain the "
                    "conventions and warn me that each market's rules differ and must be read.\n"
                    "5. THE TRACKING SYSTEM: the columns to keep - story, market, date sent, response "
                    "time, outcome, notes, where it goes next. Give me the table.\n"
                    "6. THE REJECTION READ: how to distinguish a form rejection, a higher-tier form "
                    "rejection, and a personal rejection - and what each actually tells me about the story.\n"
                    "7. THE REVISION TRIGGER: how many rejections before revising rather than resubmitting, "
                    "and what signal in the rejections indicates a fixable problem.\n"
                    "8. THE FORMATTING STANDARD: the standard manuscript format for prose short fiction "
                    "submission - font, spacing, header, title block, word count, scene break marker - and "
                    "the note that each market's guidelines override this.\n"
                    "9. THE CONTEST QUESTION: whether contests are worth it for this story, how to judge a "
                    "legitimate one, and what entry fees are reasonable relative to prize and prestige.\n\n"
                    "End by asking me how long I am prepared to keep this story in circulation, because "
                    "the writers who place stories are the ones who resubmit within a week of a rejection."
                ),
                "pro_tip": (
                    "Item 3 is the discipline that separates published writers from unpublished ones. "
                    "Submit to the best plausible market first and work down - the only cost is response "
                    "time, and you cannot be accepted somewhere you never sent it."
                ),
            },
            {
                "title": "The Cover Letter and Bio",
                "desc": (
                    "The short materials that go with every submission. Brief, plain, and easy to get "
                    "subtly wrong."
                ),
                "prompt_text": (
                    "You are a magazine editor explaining what you actually want in a cover letter, and "
                    "what makes you sigh.\n\n"
                    "My story - title, genre, length: [STATE THEM]\n"
                    "My publication history: [LIST IT, OR SAY 'NONE']\n"
                    "Anything genuinely relevant about me: [DESCRIBE, OR SAY 'NOTHING']\n\n"
                    "Do the following:\n\n"
                    "1. THE COVER LETTER: write mine. Keep it short - title, word count, genre if not "
                    "obvious, a brief bio, and thanks. No plot summary unless a market asks for one, no "
                    "explanation of the story's meaning, no claims about how much the editor will enjoy it.\n"
                    "2. THE NO-LIST: 8 things writers put in cover letters that damage their chances, and "
                    "why each one does.\n"
                    "3. THE BIO, WITH CREDITS: if I have publications, write the two-sentence version that "
                    "uses them well without listing everything.\n"
                    "4. THE BIO, WITHOUT CREDITS: if I have none, write the version that is honest, brief "
                    "and does not apologise. Explain why 'this is my first submission' is neither "
                    "necessary nor harmful, and what to write instead of nothing.\n"
                    "5. THE THIRD-PERSON BIO: the publication-ready version for when the story is "
                    "accepted, at 40 and 75 words.\n"
                    "6. THE QUERY LETTER: the short, polite note to send when a market has exceeded its "
                    "stated response time.\n"
                    "7. THE WITHDRAWAL NOTE: how to withdraw a story from a simultaneous submission when "
                    "it is accepted elsewhere. Write it.\n"
                    "8. THE ACCEPTANCE RESPONSE: what to say and what to check when a story is accepted - "
                    "rights, payment, publication date, edits, and what is reasonable to ask.\n\n"
                    "End by asking me whether any of my existing credits are worth leading with, since one "
                    "good one is worth more than five weak ones."
                ),
                "pro_tip": (
                    "Keep it to four sentences. Editors are reading the story, not the letter - a short, "
                    "plain, correctly addressed note is the entire goal, and every additional sentence is "
                    "another chance to make a bad impression."
                ),
            },
            {
                "title": "The Next Story and the Collection Path",
                "desc": (
                    "One story is a story; a body of work is a career. This prompt plans what comes next "
                    "and how these eventually add up to a book."
                ),
                "prompt_text": (
                    "You are a career advisor for short fiction writers who thinks in bodies of work "
                    "rather than individual pieces.\n\n"
                    "My finished story - genre, effect, what it does well: [PASTE FROM PROMPTS 1-2 AND 17]\n"
                    "My verdict and the hard question: [PASTE FROM PROMPT 17]\n"
                    "What I want from short fiction: [PUBLICATION CREDITS, A COLLECTION, PRACTICE FOR A "
                    "NOVEL, READER MAGNETS, OR SOMETHING ELSE]\n\n"
                    "Do the following:\n\n"
                    "1. WHAT THIS STORY DEMONSTRATES: the specific skill this piece shows, and the "
                    "specific weakness it revealed.\n"
                    "2. THE NEXT STORY: what my next one should do differently to build range rather than "
                    "repeat this one. Name the specific craft problem to attack next - a different POV, a "
                    "different length, a different shape from Prompt 8, a genre I have not tried.\n"
                    "3. THE THREE-STORY PLAN: three story concepts that together would demonstrate range, "
                    "each in two sentences, each targeting a different skill.\n"
                    "4. THE VOLUME QUESTION: how many stories a year is realistic for me, and the honest "
                    "relationship between volume and placement in this form.\n"
                    "5. THE COLLECTION PATH: how many stories a collection needs, what makes a set cohere "
                    "into a book rather than a pile, and whether my current story belongs in one. Note "
                    "that assembling and selling a collection is a separate job from writing the stories.\n"
                    "6. THE UNIFYING PRINCIPLE: if I am building toward a collection, what could bind mine "
                    "- a setting, a preoccupation, a form, a voice, a single question asked repeatedly. "
                    "Give me three candidates based on this story.\n"
                    "7. THE REUSE QUESTION: whether anything in this story - a character, a world, a "
                    "premise - is worth returning to, either in another story or as a novel.\n"
                    "8. THE NOVEL BRIDGE: if I want to write novels, what this story taught me that "
                    "transfers, and the specific thing short fiction will not teach me.\n"
                    "9. THE PRACTICE PLAN: a realistic working pattern - drafting, revising and submitting "
                    "in parallel rather than in sequence, so I always have work in circulation.\n\n"
                    "End by asking me what I am afraid I cannot write yet, because that is what the next "
                    "story should be."
                ),
                "pro_tip": (
                    "Item 9 is the habit that changes everything. Writers who place stories have three in "
                    "circulation, one in revision and one being drafted at all times - so a rejection is an "
                    "administrative task rather than a verdict on their week."
                ),
            },
        ],
    },
]
