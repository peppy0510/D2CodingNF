#!/bin/sh
# Patch every font in original/ into output/, then publish the results at the repository root.
set -e
cd "$(dirname "$0")"

rm -rf output
for font in original/*.ttf; do
    fontforge -script patcher.py "$font" --windows --complete --careful --postprocess ./postprocess.py \
        --removeligatures --adjust-line-height --glyphdir "glyphs/" --outputdir "output/" --extension "ttf" \
        --quiet --no-progressbars --use-single-width-glyphs
done

rm -f D2CodingNF-*.ttf
cp output/D2CodingNF-*.ttf .
ls -l D2CodingNF-*.ttf
