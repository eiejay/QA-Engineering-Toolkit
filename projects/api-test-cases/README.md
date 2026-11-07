# REST API Test Cases: Sample Appointments API

A documented test set for a fictional appointments API. The endpoints are invented; the testing method is the real content: status codes, payload checks, and the negative cases inexperienced testers skip.

Base path: /api/v1  |  Auth: bearer token  |  Format: JSON

## Endpoints under test

- GET /appointments?provider={id}&date={yyyy-mm-dd}
- POST /appointments
- GET /appointments/{id}
- DELETE /appointments/{id}

## Test cases

### Happy path

| ID | Request | Expected |
| --- | --- | --- |
| API-01 | GET appointments for a provider and date with open slots | 200, list contains only that provider and date |
| API-02 | POST a valid booking | 201, response includes the new appointment id and echoes the booked slot |
| API-03 | GET the created appointment | 200, fields match the POST body |
| API-04 | DELETE the appointment | 204, a following GET returns 404 |

### Error and negative cases

| ID | Request | Expected |
| --- | --- | --- |
| API-05 | POST with a missing required field | 400, error names the missing field |
| API-06 | POST a slot that is already booked | 409, no second record created |
| API-07 | GET with no auth token | 401 |
| API-08 | GET another patient's appointment with a valid token | 403 or 404, never the record |
| API-09 | POST with a date in the past | 400 |
| API-10 | POST with malformed JSON | 400, no server error, no stack trace in the response |
| API-11 | GET with an unknown provider id | 200 with an empty list, or 404; must not be 500 |
| API-12 | DELETE the same appointment twice | First 204, second 404, no error state |

## Sample payloads

Valid booking request:

    {
      "providerId": "prov-100",
      "patientId": "pat-500",
      "date": "2026-12-01",
      "time": "09:30",
      "reason": "follow-up"
    }

Expected 201 response shape:

    {
      "id": "appt-9001",
      "providerId": "prov-100",
      "patientId": "pat-500",
      "date": "2026-12-01",
      "time": "09:30",
      "status": "booked"
    }

## Testing notes

- API-08 is the case that matters most in healthcare software: authorization between patients. A 200 there is a reportable incident, not a bug ticket.
- Error responses are part of the contract. A 500 with a stack trace is two defects: the crash, and the leak.
- Every POST case is run twice where idempotency matters; networks retry, and the API has to survive it.
