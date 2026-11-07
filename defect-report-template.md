# Defect Report Template

A defect report has one job: let a developer reproduce the problem on the first try.

- Title: [Area] short summary of the failure, stated as observed behavior
- Severity (Critical / High / Medium / Low):
- Priority, if different from severity, and why:
- Environment: build number, browser or device, operating system
- Account or role used:

## Steps to reproduce

Numbered, exact, starting from a known state. Include the data used (test data only).

## Expected result

What should have happened, per the requirement.

## Actual result

What happened instead. Quote error messages exactly.

## Evidence

- Screenshot or recording, with any personal or customer data removed
- Console or log excerpt, if relevant
- Frequency: always, intermittent (how often), or once

## Impact

Who is affected and what they cannot do. This is what sets real priority.

## Severity guide

- Critical: system down, data loss, or a core flow blocked with no workaround
- High: core flow broken, workaround exists but is painful
- Medium: a feature misbehaves, work continues
- Low: cosmetic, wording, alignment
