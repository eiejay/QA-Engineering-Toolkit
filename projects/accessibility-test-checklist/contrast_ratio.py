#!/usr/bin/env python3
"""WCAG contrast ratio calculator.

Usage:
    python3 contrast_ratio.py <foreground-hex> <background-hex>
    python3 contrast_ratio.py 767676 FFFFFF

Computes the WCAG 2.x contrast ratio between two colors and reports
which levels the pair passes: AA for normal text (4.5 to 1), AA for
large text (3 to 1), and AAA for normal text (7 to 1).
"""

import sys


def hex_to_rgb(value):
    value = value.lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    if len(value) != 6:
        raise ValueError("expected a 3 or 6 digit hex color")
    return tuple(int(value[i:i + 2], 16) / 255 for i in (0, 2, 4))


def relative_luminance(rgb):
    def channel(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg_hex, bg_hex):
    lum_fg = relative_luminance(hex_to_rgb(fg_hex))
    lum_bg = relative_luminance(hex_to_rgb(bg_hex))
    lighter, darker = max(lum_fg, lum_bg), min(lum_fg, lum_bg)
    return (lighter + 0.05) / (darker + 0.05)


def verdict(ratio):
    lines = [
        f"AA normal text (needs 4.5): {'PASS' if ratio >= 4.5 else 'FAIL'}",
        f"AA large text (needs 3.0): {'PASS' if ratio >= 3.0 else 'FAIL'}",
        f"AAA normal text (needs 7.0): {'PASS' if ratio >= 7.0 else 'FAIL'}",
    ]
    return lines


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 contrast_ratio.py <foreground-hex> <background-hex>")
        return 2
    try:
        ratio = contrast_ratio(sys.argv[1], sys.argv[2])
    except ValueError as error:
        print(f"Input error: {error}")
        return 2
    print(f"Foreground: #{sys.argv[1].lstrip('#').upper()}  Background: #{sys.argv[2].lstrip('#').upper()}")
    print(f"Contrast ratio: {ratio:.2f} to 1")
    for line in verdict(ratio):
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
