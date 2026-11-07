# QA Engineering Toolkit

Quality assurance templates and practice documents: test plans, test cases, defect reports, and regression checklists.

This repository collects the working documents of QA practice for web and software applications: how testing gets planned, how cases get written so anyone can run them, how defects get reported so a developer can reproduce them on the first try, and how a release gets regression tested without surprises.

## Projects

1. [Sample Test Cycle](projects/sample-test-cycle/): a complete practice test cycle for a demo clinic patient portal: plan, executed cases with results, and the defects found.
2. [REST API Test Cases](projects/api-test-cases/): a documented test set for a sample appointments API, covering happy paths, error codes, and negative cases.
3. [Accessibility Test Checklist](projects/accessibility-test-checklist/): a WCAG based checklist for testing healthcare web forms, the pages where accessibility failures shut real patients out.

## Templates

- [Test Plan Template](test-plan-template.md): scope, approach, entry and exit criteria for a test cycle.
- [Test Case Template](test-case-template.md): case format with preconditions, steps, and expected results, plus worked examples.
- [Defect Report Template](defect-report-template.md): the fields that make a bug report actionable.
- [Regression Checklist](regression-checklist.md): the pass that runs before every release.

## Skills covered

- Test planning and test design: equivalence partitioning, boundary values, negative testing
- Functional, regression, and exploratory testing
- API testing fundamentals
- Accessibility testing against WCAG criteria
- Defect lifecycle: report, triage, fix verification, closure
- Test case management and traceability to requirements
- Web application testing across browsers and devices
- Privacy and data handling review in test scope

## License

MIT
