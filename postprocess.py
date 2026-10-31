#!/usr/bin/env python3
# coding=utf8
"""Restore Windows monospace metadata and unify family names after patching.

FontForge recalculates OS/2.xAvgCharWidth over every glyph (885 instead of 500,
because of the double-width Hangul and CJK glyphs) and clears post.isFixedPitch.
GDI lays out double-width characters at 2 x tmAveCharWidth, so that value spreads
Hangul apart in GDI clients. Restoring the source values lets a single font render
correctly in both GDI and DirectWrite clients.

Usage: postprocess.py <patched font path>
"""

import os
import re
import sys

from fontTools.ttLib import TTFont

FAMILY = 'D2CodingNF'
AVG_CHAR_WIDTH = 500


def postprocess(path: str) -> str:
    font = TTFont(path)
    font['post'].isFixedPitch = 1
    font['OS/2'].xAvgCharWidth = AVG_CHAR_WIDTH

    bold = bool(font['head'].macStyle & 1)
    style = 'Bold' if bold else 'Regular'
    match = re.search(r'Version ([\d.]+); Build (\d+)', font['name'].getDebugName(5))
    version = f'{match.group(1)}-{match.group(2)}'
    names = {
        1: FAMILY,
        2: style,
        3: f'{FAMILY} {style} {version}',
        4: f'{FAMILY} {style}' if bold else FAMILY,
        6: f'{FAMILY}-Bold' if bold else FAMILY,
        16: FAMILY,
        17: style,
    }
    table = font['name']
    for record in list(table.names):
        if record.nameID in names and record.platformID in (1, 3):
            table.removeNames(nameID=record.nameID, platformID=record.platformID,
                              platEncID=record.platEncID, langID=record.langID)
    for name_id, value in names.items():
        for lang_id in (0x409, 0x412):
            table.setName(value, name_id, 3, 1, lang_id)

    output = os.path.join(os.path.dirname(path), f'{FAMILY}{"-Bold" if bold else ""}-Ver{version}.ttf')
    font.save(output)
    if os.path.abspath(output) != os.path.abspath(path):
        os.remove(path)
    return output


if __name__ == '__main__':
    print(postprocess(sys.argv[1]))
