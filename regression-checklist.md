# Regression Checklist

Run before every release. The goal is not to test everything; it is to prove nothing important broke.

## Access and accounts

- [ ] Sign up, sign in, sign out
- [ ] Password reset end to end
- [ ] Role permissions: what each role can and cannot see

## Core flows

- [ ] The product's main happy path, start to finish
- [ ] Create, edit, save, delete on the main object types
- [ ] Search and filtering return correct results
- [ ] File upload and download

## Forms and validation

- [ ] Required fields enforced
- [ ] Invalid input rejected with a clear message
- [ ] Long input, special characters, and empty states handled

## Money and data, if applicable

- [ ] Prices and totals calculate correctly
- [ ] Saved data persists across sessions
- [ ] Reports match the underlying records

## Cross-cutting

- [ ] Supported browsers and one mobile device
- [ ] Error pages: 404 and server error show something helpful
- [ ] No console errors on the main pages
- [ ] Performance sanity: main pages load at normal speed

## Sign-off

- [ ] All boxes checked or an exception written and accepted
- [ ] Open defects listed with their release decision
