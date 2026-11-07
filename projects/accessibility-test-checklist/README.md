# Accessibility Test Checklist: Healthcare Web Forms

A practical checklist for testing registration, intake, and appointment forms against WCAG 2.2 AA, the standard healthcare organizations are asked to meet. Forms are where accessibility failures hurt most: a patient who cannot complete intake cannot get care.

## Files

- accessibility_checklist.csv: this checklist as data, with a WCAG reference and a how-to-test note per item, plus Result and Notes columns to fill during a pass.
- contrast_ratio.py: a small calculator for the contrast checks. Give it a foreground and a background hex color; it returns the WCAG contrast ratio and the AA and AAA verdicts.

Run it:

    python3 contrast_ratio.py 767676 FFFFFF

Verified output on known pairs:

    #000000 on #FFFFFF: 21.00 to 1 (the maximum possible ratio)
    #767676 on #FFFFFF: 4.54 to 1, passes AA for normal text
    #949494 on #FFFFFF: 3.03 to 1, fails AA for normal text, passes for large text only

## Keyboard

- [ ] Every control reachable by Tab, in a visual order
- [ ] Focus indicator visible on every control, never removed by styling
- [ ] No keyboard traps: focus can always move on or back out
- [ ] Dialogs move focus inside on open and return it on close
- [ ] Skip link present and works on long pages

## Labels and instructions

- [ ] Every field has a programmatic label, not placeholder text alone
- [ ] Required fields announced as required, not marked by color alone
- [ ] Format hints (date format, phone format) given before entry, not only in the error
- [ ] Errors identify the field, say what is wrong, and suggest the fix
- [ ] Error summary at the top of the form receives focus on submit

## Screen reader pass

- [ ] Full form completable with a screen reader alone (NVDA or VoiceOver)
- [ ] Fieldsets and legends group related questions (address, insurance)
- [ ] Dynamic content (slot availability results) announced through a live region
- [ ] Page title and headings describe the step in the process
- [ ] Autocomplete attributes set on name, address, phone, email, and birth date fields

## Visual and motor

- [ ] Text contrast at least 4.5 to 1, large text 3 to 1 (verify with contrast_ratio.py)
- [ ] Page usable at 200 percent zoom with no horizontal scrolling
- [ ] Touch targets at least 24 by 24 CSS pixels, 44 preferred
- [ ] No information carried by color alone (slot status, error state)
- [ ] Session timeout warns before expiring and allows extension; intake data is not lost

## Healthcare specific

- [ ] Date of birth entry works without a calendar widget, for patients who know the date but struggle with pickers
- [ ] Insurance fields allow the card to be read in any order: no forced sequence across group and member numbers
- [ ] Error recovery never clears the whole form; a patient re-typing a long intake form will abandon it
- [ ] Plain language: reading level of instructions checked, medical terms explained

## Method note

Automated scanners catch roughly a third of accessibility problems. The rest only appear in a keyboard-only pass and a screen reader pass, which is why both are separate sections here and neither is optional.
