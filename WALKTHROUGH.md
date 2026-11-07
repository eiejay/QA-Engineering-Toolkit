# Walkthrough

A guided tour of the projects in this repository: how to open each artifact, run what runs, and read the results the way a QA lead would.

## 1. Sample Test Cycle (projects/sample-test-cycle)

Start with the README for the story: the plan, the ten cases, the two defects. Then open the data:

- test_cases.csv opens in any spreadsheet program (Excel, Google Sheets, LibreOffice). Filter the Status column to Fail and exactly two rows remain: TC-04 and TC-07, the cases that found the defects.
- defect_log.csv holds the same two defects as records: DEF-001 (reset link reuse) and DEF-002 (double booking).

How to talk about this cycle: the two failures are the value of the project. A test cycle where everything passes demonstrates typing. A cycle that catches a security defect (a reusable reset link) and a data integrity defect (a race condition on the last slot) demonstrates testing. The retest note in the README closes the loop: a fix cycle re-runs the two failed cases plus the full regression checklist before sign-off.

To reuse the format on a real project: copy the CSV, replace the cases, keep the columns. Preconditions and expected results are the two columns new testers skip and experienced testers insist on.

## 2. REST API Test Cases (projects/api-test-cases)

### Run the collection

1. In Postman, choose File, Import, and select appointments_api.postman_collection.json.
2. Set the collection variables: baseUrl to your test environment, token to a valid test token.
3. Send API-01 (list appointments), then API-02 (create). Copy the returned id into the appointmentId variable.
4. Send API-03 (get) and confirm the fields match what API-02 created. Send API-04 (delete), then API-03 again: expect a 404.
5. Send API-07 with the token removed: expect a 401.

The remaining cases (API-05, 06, 08 to 12 in the README table) are variations: a missing field, a double booking, another patient's record, a past date, malformed JSON, an unknown provider, a double delete. Each is a two-minute edit of a request already in the collection.

### The case to be able to explain cold

API-08: asking for another patient's appointment with your own valid token. A 200 response there is not a bug, it is a reportable privacy incident. In healthcare software, authorization between patients is the highest-stakes test in the set, and it is the one most often missing from junior test plans.

## 3. Accessibility Checklist and Contrast Calculator (projects/accessibility-test-checklist)

### The calculator

    python3 contrast_ratio.py 767676 FFFFFF

    Foreground: #767676  Background: #FFFFFF
    Contrast ratio: 4.54 to 1
      AA normal text (needs 4.5): PASS
      AA large text (needs 3.0): PASS
      AAA normal text (needs 7.0): FAIL

Two reference points worth memorizing: black on white is 21.00 to 1, the maximum ratio that exists, and #767676 is the lightest gray that still passes AA for normal text on white. #949494 (3.03 to 1) is the classic almost: fine for large headings, a failure for body text.

### The checklist

accessibility_checklist.csv carries one row per check with its WCAG reference and how to test it. A real pass works in the order the README gives: keyboard first (it finds the structural problems), then labels and errors, then a screen reader pass, then visual checks with the calculator where color is in question. Automated scanners find roughly a third of accessibility issues; the checklist exists for the other two thirds.

## The thread through all three

Each project produces evidence, not opinions: executed cases with actual results, a runnable API collection, recorded contrast measurements. QA work that can be shown beats QA work that can only be described, which is why every artifact here is a file and not a claim.
