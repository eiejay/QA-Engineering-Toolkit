# Test Case Template

## Format

- Case ID:
- Title: one line, states the condition and the expectation
- Requirement or story it traces to:
- Priority (High / Medium / Low):
- Preconditions: account state, data state, starting page
- Steps: numbered, one action per step
- Expected result: observable, specific, one per step where it matters
- Actual result (filled during execution):
- Status (Pass / Fail / Blocked):

## Worked examples

### TC-01: Login with valid credentials

- Preconditions: a registered account exists; tester is logged out.
- Steps:
  1. Open the login page.
  2. Enter the valid email and password.
  3. Select Sign in.
- Expected result: the user lands on the dashboard, signed in as that account.

### TC-02: Login with a wrong password

- Preconditions: a registered account exists; tester is logged out.
- Steps:
  1. Open the login page.
  2. Enter the valid email and an incorrect password.
  3. Select Sign in.
- Expected result: a generic error appears that does not say which field was wrong; the user stays on the login page; the account is not locked after a single failure.

### TC-03: Boundary value, text field limit

- Preconditions: a form with a 100 character field is open.
- Steps:
  1. Enter exactly 100 characters and save.
  2. Try to enter a 101st character.
- Expected result: 100 characters save successfully; the 101st character is refused or clearly flagged, and no silent truncation corrupts saved data.

## Writing rules

- A case anyone can run beats a clever case only its author understands.
- Expected results must be observable on screen or in data, never assumed.
- One condition per case. A case that tests three things fails in three confusing ways.
