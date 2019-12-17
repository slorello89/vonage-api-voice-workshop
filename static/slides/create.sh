#!/bin/sh

FILE=$1
if [ -z "$FILE" ]; then
    FILE=intro-to-voice
fi

rst2pdf ${FILE}.rst \
    -b1 \
    --fit-background-mode=scale \
    --fit-literal-mode=overflow \
    -s "lj-light,lj-code-light"\
    --output=${FILE}.pdf

python notes.py ${FILE}.pdf > notes.rst
rst2pdf notes.rst -s "twocolumn,notes.style"

pdfjam --suffix handout --nup '4x3' --frame 'true' --noautoscale 'false' --delta '0.2cm 2cm' --scale '0.9' --landscape -- ${FILE}.pdf -

