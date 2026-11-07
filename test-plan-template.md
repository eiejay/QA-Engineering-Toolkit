# Test Plan Template

## 1. Overview

What is being tested and why: the feature, the release, and the business risk it carries.

## 2. Scope

In scope:
- 

Out of scope, and why:
- 

## 3. Test approach

- Functional testing of new features against requirements
- Regression testing of existing critical paths (see the regression checklist)
- Exploratory sessions on high-risk areas, timeboxed
- Negative testing: invalid input, interrupted flows, permission edges

## 4. Test environment

- Environments: staging, production-like
- Browsers and devices in the support matrix
- Test data needed, and how it is created without touching real user data

## 5. Entry criteria

- Build deployed to the test environment
- Requirements and designs available
- Known blocking defects: none open

## 6. Exit criteria

- All planned cases executed
- No open critical or high defects
- Regression checklist complete
- Risks of anything untested written down and accepted

## 7. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Late build | Compressed test window | Test highest-risk paths first |
| Missing test data | Blocked cases | Prepare data set in advance |
