"""One Word for the Boss — entry program.

Final word: "Ghost" — 5 characters (G=1, h=2, o=3, s=4, t=5), one word, no spaces.
Gate (competition.yaml): /output/entry.txt must be UTF-8 text of 1 to 30
characters, not only white space. 5 is inside the gate.

Judge brief (in order): 1) a single word a person would actually use about
the boss they report to; 2) funny on its own, the kind a colleague repeats at
lunch; 3) rings true, catching a real habit of bosses; 4) fresh, not the first
word anyone would reach for; 5) travels across kitchen, warehouse or office.

DECISION RECORD — candidates weighed against the brief, in its own order:

A. "Micromanager" (12 chars) — REJECTED. The truest cliche in the book, which
   is exactly the problem: it is the FIRST word anyone reaches for, so it
   fails criterion 4 (fresh) outright, and it is a job description, not a
   joke — it lands with a shrug, not a laugh.

B. "Seagull" (7 chars) — REJECTED. Funny and true (flies in, makes a lot of
   noise, leaves a mess, flies out) and it travels — but "seagull manager" is
   already a known office joke with its own punchline, so the surprise is
   borrowed, not fresh. A judge who has read a thousand office jokes has
   read this one.

C. "Echo" (4 chars) — CLOSE SECOND. The boss who repeats your idea back
   louder in the meeting and gets the credit for it: a real habit, fresh,
   travels anywhere. Loses to the winner on criterion 2: the laugh needs a
   half-beat of translation ("echo" as a noun label is less idiomatic than
   the verb), and it has only one punch where the winner has two.

D. "Ghost" (5 chars) — CHOSEN. The boss who vanishes the moment a hard
   decision is needed and reappears the moment there is credit to take. It
   lands alone, instantly — everyone knows ghosting, no caption required.
   It is funny (criterion 2) because the image is vivid, true (criterion 3)
   because the double habit is one every worker has met, fresh (criterion 4)
   because as a boss label it is not the first word anyone reaches for, and
   it travels (criterion 5): a ghost boss haunts a kitchen, a warehouse and
   an office alike. A colleague would genuinely say it at lunch: "my boss
   ghosted the whole project."

E. "Sun" (3 chars) — REJECTED. Elegant (everything revolves around him) and
   the shortest word here, but it needs its caption to be funny — "the sun,
   because everything revolves around him" — and the brief says a word that
   needs a caption is doing less than a word that stands alone.

PASS 1: drafted "Ghost" (5 chars) after weighing the five candidates above.
PASS 2 (critique and tighten): tested "Ghosted" (7 chars — past tense, reads
as an action, not a label for the boss, and loses the noun punch), "Ghosting"
(8 chars — gerund, weaker, sounds like a HR complaint), and lowercase
"ghost" (reads as a common noun, not a name for the boss). All three rejected;
the draft "Ghost" stands verbatim.
"""

import os

WORD = "Ghost"

# Hand count, letter by letter: G(1) h(2) o(3) s(4) t(5) = 5 characters.
# Gate: 1 to 30 characters. 5 is inside the gate. One word, no spaces.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)
    # Validate: re-read what was just written and assert it decodes to
    # exactly the single word "Ghost" — 5 chars, no spaces, no trailing newline.
    with open(os.path.join(out_dir, "entry.txt"), "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD and len(written) == 5 and " " not in written
    print(f"Verified: {len(WORD)} characters, 1 word.")


if __name__ == "__main__":
    main()
