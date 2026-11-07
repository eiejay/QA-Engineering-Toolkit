# Sample Test Cycle: Demo Clinic Patient Portal

A complete practice test cycle run against a fictional demo patient portal with two features: patient sign-in and appointment booking. Everything here is a practice exercise on invented software and invented data; the value is the method, shown end to end.

## Test plan summary

- Scope: sign-in, password reset, appointment search and booking, booking cancellation
- Out of scope: payments, medical record content, messaging
- Approach: scripted cases for the core flows, one exploratory session on booking edge cases, defect logging per the toolkit template
- Entry criteria: demo build available, test accounts seeded
- Exit criteria: all high priority cases executed, no open critical defects

## Executed cases and results

| ID | Case | Result |
| --- | --- | --- |
| TC-01 | Sign in with valid credentials | Pass |
| TC-02 | Sign in with wrong password shows a generic error | Pass |
| TC-03 | Account locks after repeated failures per policy | Pass |
| TC-04 | Password reset link signs the user in after reset | Fail, see DEF-001 |
| TC-05 | Search appointments by provider returns only that provider | Pass |
| TC-06 | Book the last open slot, then search again | Pass |
| TC-07 | Two sessions book the same slot at the same time | Fail, see DEF-002 |
| TC-08 | Cancel a booking and confirm the slot reopens | Pass |
| TC-09 | Book an appointment in the past using a hand-edited request | Pass, server rejects |
| TC-10 | Session times out during booking and resumes safely | Pass |

Result: 8 pass, 2 fail. Both failures are defects, logged below.

## Defects found

### DEF-001: Used password reset link works a second time

- Severity: High (account security)
- Steps: request a reset link, use it to set a new password, then open the same link again within its validity window.
- Expected: the link is dead after first use.
- Actual: the link opens the reset form again and accepts a second password change.
- Note: single-use tokens are the whole point of a reset link. Fix before release.

### DEF-002: Double booking of the same slot from two sessions

- Severity: High (data integrity)
- Steps: open the same open slot in two browser sessions, confirm booking in both within seconds.
- Expected: the second confirmation fails with a clear message; one booking exists.
- Actual: both confirmations succeed; two bookings exist for one slot.
- Note: the availability check and the booking write are not atomic. Needs a server-side uniqueness guard, not a front-end fix.

## Retest note

Both defects were verified against the case steps after logging. A fix cycle would re-run TC-04 and TC-07 plus the full regression checklist before sign-off.
