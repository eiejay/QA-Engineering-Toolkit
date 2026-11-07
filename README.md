# QA Engineering Toolkit

I did my QA years inside a healthcare network company, where a missed defect is not an embarrassment, it is a clinician somewhere working around your bug. This repo is how I still practice the craft: templates I actually fill in, a full sample test cycle with its failures left in, and three tools, including a text similarity engine I built to catch duplicate defects before they waste a triage meeting.

## The tools

- projects/duplicate-defect-detector: TF-IDF plus cosine similarity ranks the defect log against a new report. It caught both planted paraphrase duplicates in its sample data (0.65 and 0.56 similarity), because rare shared words are a bug's fingerprint and this math knows it.
- projects/sample-test-cycle: a complete practice cycle on a fictional clinic portal: plan, ten executed cases, two real failures, defect reports, and the CSV logs. The failures stay in. A test cycle with no failures teaches nothing.
- projects/api-test-cases: a documented REST test set for a fictional appointments API, including the cross patient authorization case that healthcare software lives or dies by, plus the runnable Postman collection.
- projects/accessibility-test-checklist: a WCAG 2.2 AA working checklist for healthcare web forms, the CSV version, and a contrast ratio calculator I verified against known color pairs.

## The documents

- test-plan-template.md, test-case-template.md, defect-report-template.md: the shapes I write in, with the fields that survive contact with a real defect.
- regression-checklist.md: what gets retested before anything ships, and why each line earned its place.

## How I use this repo

WALKTHROUGH.md reproduces every claim: the Postman collection parses, the contrast math matches the published ratios, the duplicate finder finds its duplicates. If I cannot run it in front of you, I do not list it as a skill.

## License

MIT.
