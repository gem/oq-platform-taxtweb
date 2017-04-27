#!/bin/bash
set -x
echo "class bagu(object):"
cat "$1" | \
    sed "s/^    /        /g" | \
    sed "s/function \([a-zA-Z0-9_]\+\)().*/    def \1(self):/g" | \
    sed "s/gem\$('#\([a-zA-Z0-9_]\+\)')/self.\1/g" | \
    sed "s/.*\.push({'_text': '//g;t lab;b;:lab ;s/'.*//g;s/\(.*\)/                '\1',/g" | \
    sed "s/\.prop(\"\([a-zA-Z0-9_]\+\)\", \([a-zA-Z0-9_]\+\))/.\1(\2)/g" | \
    sed "s/var \([a-zA-Z0-9_]\+\) = \[\]/self.\1.items([/g" | \
    sed "s/select_populate('\([a-zA-Z0-9_]\+\)', .*)/], val=0)/g" | \
    sed "s/\bif (\(.*\)) {/if \1:/g" | \
    sed "s/\belse if/elif/g" | \
    sed "s/\(^ *if \)(\(.*\)) *\$/\1\2:/g" | \
    #    grep -v '^{ *$'| \
    #    grep -v '^ *} *$'| \
    sed 's/\btrue\b/True/g' | \
    sed 's/\bfalse\b/False/g' | \
    sed 's/^{ *$//g' | \
    sed 's/ *} *$//g' | \
    sed 's/) {$/):/g' | \
    sed 's/else {/else:/g' | \
    sed 's/;$//g' | \
    sed 's/||/or/g' | \
    sed 's/&&/and/g' | \
    sed 's@//@#@g' | \
    cat
