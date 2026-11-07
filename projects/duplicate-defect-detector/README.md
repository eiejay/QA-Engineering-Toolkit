# Duplicate Defect Finder: Catching the Same Bug Twice

Every QA team pays a quiet tax: the same defect filed two or three times, triaged two or three times, argued about in two or three threads. I wrote this after living that meeting. It reads a defect log, turns every report into a TF-IDF vector, and ranks the existing defects by cosine similarity to a new report, so the first thing a tester sees is: has someone already filed this, in different words?

## Run it

    python3 duplicate_finder.py defects.csv
    python3 duplicate_finder.py defects.csv "text of the new report"

## What I got

    Indexed defects: 8

    New report: The reset password link works more than once after being used
      0.65  DEF-101  Password reset link can be reused  (LIKELY DUPLICATE)

    New report: Two different patients were able to reserve the same time slot
      0.56  DEF-102  Double booking on appointment slot  (LIKELY DUPLICATE)

    New report: Charts take a long time to load on slow connections
      0.19  (best match; nothing close, correctly reads as new)

The two duplicates are paraphrases, not copies: different words, same bug. That is the whole game, and word weighting is what wins it. Terms that appear in every report (patient, error) count for almost nothing; terms that appear in one or two (reset link, time slot) carry the signal. That weighting is the IDF half of TF-IDF, and it is why the naive keyword search in most trackers misses what this catches.

## How I would run it in a real team

- Wire it into intake: a new report gets its top three matches attached before triage, and the filer confirms or rejects the match. Those confirmations become labeled data.
- Set the duplicate bar with the team, not alone. Mine is 0.45 on this tiny corpus; a real log recalibrates it in a week.
- Never auto close. The tool ranks, the tester decides. A false merge hides a real bug, and hidden bugs are the expensive kind.

## The honest limits

Eight defects is a toy index. Similarity is wording, not understanding: two reports can describe the same failure with zero shared vocabulary, and this will miss them while a human catches them in one read. It is a first pass that saves the easy hours, and I present it as exactly that.
