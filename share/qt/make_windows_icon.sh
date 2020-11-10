#!/bin/bash
# create multiresolution windows icon
ICON_SRC=../../src/qt/res/icons/dmomint.png
ICON_DST=../../src/qt/res/icons/dmomint.ico
convert ${ICON_SRC} -resize 16x16 dmomint-16.png
convert ${ICON_SRC} -resize 32x32 dmomint-32.png
convert ${ICON_SRC} -resize 48x48 dmomint-48.png
convert dmomint-16.png dmomint-32.png dmomint-48.png ${ICON_DST}

